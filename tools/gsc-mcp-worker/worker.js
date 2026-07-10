/**
 * Kordovan — Google Search Console MCP server (Cloudflare Worker, zero-dependency)
 * -----------------------------------------------------------------------------
 * A remote MCP server that gives Claude live read access to Google Search Console.
 * 100% free: Cloudflare Workers free tier + Google Search Console API (free).
 *
 * Secrets to set in the Worker (Settings → Variables and Secrets):
 *   GOOGLE_SA_EMAIL        — service account email (kdv-seo-reader@…​.iam.gserviceaccount.com)
 *   GOOGLE_SA_PRIVATE_KEY  — the "private_key" value from the service-account JSON (paste as-is; \n handled)
 *   MCP_SECRET             — a random hard-to-guess string; becomes part of the connector URL
 *   GSC_SITE               — default property, e.g. "sc-domain:kordovanleather.com"
 *
 * Connector URL to add in claude.ai:  https://<worker-subdomain>.workers.dev/mcp/<MCP_SECRET>
 */

const GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token";
const GSC_BASE = "https://searchconsole.googleapis.com/webmasters/v3";
const GSC_INSPECT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect";
const SCOPE = "https://www.googleapis.com/auth/webmasters.readonly";
const PROTOCOL_VERSION = "2024-11-05";

let _token = { value: null, exp: 0 }; // in-isolate cache

/* ---------- base64url + PEM helpers ---------- */
function b64urlStr(str) {
  return btoa(unescape(encodeURIComponent(str)))
    .replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function b64urlBytes(bytes) {
  let s = "";
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function pemToDer(pem) {
  const clean = pem.replace(/\\n/g, "\n"); // JSON-escaped newlines → real newlines
  const b64 = clean
    .replace(/-----BEGIN [^-]+-----/, "")
    .replace(/-----END [^-]+-----/, "")
    .replace(/\s+/g, "");
  const bin = atob(b64);
  const der = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) der[i] = bin.charCodeAt(i);
  return der.buffer;
}

/* ---------- Google service-account → access token ---------- */
async function getToken(env) {
  const now = Math.floor(Date.now() / 1000);
  if (_token.value && _token.exp - 60 > now) return _token.value;

  const header = { alg: "RS256", typ: "JWT" };
  const claim = {
    iss: env.GOOGLE_SA_EMAIL,
    scope: SCOPE,
    aud: GOOGLE_TOKEN_URL,
    iat: now,
    exp: now + 3600,
  };
  const toSign = `${b64urlStr(JSON.stringify(header))}.${b64urlStr(JSON.stringify(claim))}`;
  const key = await crypto.subtle.importKey(
    "pkcs8",
    pemToDer(env.GOOGLE_SA_PRIVATE_KEY),
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sig = await crypto.subtle.sign(
    { name: "RSASSA-PKCS1-v1_5" },
    key,
    new TextEncoder().encode(toSign)
  );
  const jwt = `${toSign}.${b64urlBytes(new Uint8Array(sig))}`;

  const res = await fetch(GOOGLE_TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=${jwt}`,
  });
  const j = await res.json();
  if (!j.access_token) throw new Error("Google token error: " + JSON.stringify(j));
  _token = { value: j.access_token, exp: now + (j.expires_in || 3600) };
  return _token.value;
}

async function gscFetch(env, url, init = {}) {
  const token = await getToken(env);
  const res = await fetch(url, {
    ...init,
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json", ...(init.headers || {}) },
  });
  const text = await res.text();
  let data;
  try { data = JSON.parse(text); } catch { data = text; }
  if (!res.ok) throw new Error(`GSC ${res.status}: ${JSON.stringify(data)}`);
  return data;
}

/* ---------- date helper ---------- */
function daysAgo(n) {
  const d = new Date(Date.now() - n * 86400000);
  return d.toISOString().slice(0, 10);
}

/* ---------- MCP tool definitions ---------- */
const TOOLS = [
  {
    name: "gsc_list_sites",
    description: "List all Search Console properties the service account can access.",
    inputSchema: { type: "object", properties: {} },
  },
  {
    name: "gsc_query",
    description:
      "Query Search Console performance (clicks, impressions, CTR, position). Group by dimensions like query, page, country, device, date. Defaults to the last 28 days.",
    inputSchema: {
      type: "object",
      properties: {
        startDate: { type: "string", description: "YYYY-MM-DD (default: 28 days ago)" },
        endDate: { type: "string", description: "YYYY-MM-DD (default: today)" },
        dimensions: {
          type: "array", items: { type: "string" },
          description: 'e.g. ["query"], ["page"], ["query","page"], ["date"], ["country"], ["device"]',
        },
        rowLimit: { type: "number", description: "max rows (default 25, max 25000)" },
        searchType: { type: "string", description: 'web (default), image, video, news, discover' },
        siteUrl: { type: "string", description: "override default property (e.g. sc-domain:kordovanleather.com)" },
        query_contains: { type: "string", description: "optional: only rows whose query contains this text" },
      },
    },
  },
  {
    name: "gsc_list_sitemaps",
    description: "List submitted sitemaps and their status for a property.",
    inputSchema: { type: "object", properties: { siteUrl: { type: "string" } } },
  },
  {
    name: "gsc_inspect_url",
    description: "URL Inspection: index status, coverage, last crawl, canonical, rich-results for a specific page URL.",
    inputSchema: {
      type: "object",
      properties: {
        inspectionUrl: { type: "string", description: "full URL to inspect (required)" },
        siteUrl: { type: "string" },
      },
      required: ["inspectionUrl"],
    },
  },
];

/* ---------- tool execution ---------- */
async function runTool(env, name, args) {
  const site = args.siteUrl || env.GSC_SITE;
  if (name === "gsc_list_sites") {
    return await gscFetch(env, `${GSC_BASE}/sites`);
  }
  if (name === "gsc_query") {
    const body = {
      startDate: args.startDate || daysAgo(28),
      endDate: args.endDate || daysAgo(1),
      dimensions: args.dimensions && args.dimensions.length ? args.dimensions : ["query"],
      rowLimit: args.rowLimit || 25,
      type: args.searchType || "web",
    };
    if (args.query_contains) {
      body.dimensionFilterGroups = [
        { filters: [{ dimension: "query", operator: "contains", expression: args.query_contains }] },
      ];
    }
    return await gscFetch(env, `${GSC_BASE}/sites/${encodeURIComponent(site)}/searchAnalytics/query`, {
      method: "POST", body: JSON.stringify(body),
    });
  }
  if (name === "gsc_list_sitemaps") {
    return await gscFetch(env, `${GSC_BASE}/sites/${encodeURIComponent(site)}/sitemaps`);
  }
  if (name === "gsc_inspect_url") {
    return await gscFetch(env, GSC_INSPECT, {
      method: "POST",
      body: JSON.stringify({ inspectionUrl: args.inspectionUrl, siteUrl: site }),
    });
  }
  throw new Error("Unknown tool: " + name);
}

/* ---------- JSON-RPC / MCP handling ---------- */
function rpcResult(id, result) {
  return { jsonrpc: "2.0", id, result };
}
function rpcError(id, code, message) {
  return { jsonrpc: "2.0", id, error: { code, message } };
}

async function handleRpc(env, msg) {
  const { id, method, params } = msg;
  if (method === "initialize") {
    return rpcResult(id, {
      protocolVersion: PROTOCOL_VERSION,
      capabilities: { tools: {} },
      serverInfo: { name: "kordovan-gsc", version: "1.0.0" },
    });
  }
  if (method === "notifications/initialized" || method === "notifications/cancelled") {
    return null; // notification, no response
  }
  if (method === "ping") return rpcResult(id, {});
  if (method === "tools/list") return rpcResult(id, { tools: TOOLS });
  if (method === "tools/call") {
    const { name, arguments: args } = params || {};
    try {
      const data = await runTool(env, name, args || {});
      return rpcResult(id, { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] });
    } catch (e) {
      return rpcResult(id, { content: [{ type: "text", text: "ERROR: " + e.message }], isError: true });
    }
  }
  return rpcError(id, -32601, "Method not found: " + method);
}

/* ---------- Worker entrypoint ---------- */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization, Mcp-Session-Id",
        },
      });
    }

    // Secret-in-path gate
    if (url.pathname !== `/mcp/${env.MCP_SECRET}`) {
      return new Response("Not found", { status: 404 });
    }

    // Simple health check
    if (request.method === "GET") {
      return new Response("Kordovan GSC MCP server — OK. POST JSON-RPC to this URL.", {
        status: 200, headers: { "Content-Type": "text/plain" },
      });
    }

    if (request.method !== "POST") return new Response("Method not allowed", { status: 405 });

    let payload;
    try { payload = await request.json(); } catch { return new Response("Bad JSON", { status: 400 }); }

    const cors = { "Access-Control-Allow-Origin": "*", "Content-Type": "application/json" };

    // batch or single
    if (Array.isArray(payload)) {
      const out = [];
      for (const m of payload) {
        const r = await handleRpc(env, m);
        if (r) out.push(r);
      }
      return new Response(JSON.stringify(out), { headers: cors });
    }
    const r = await handleRpc(env, payload);
    if (!r) return new Response("", { status: 202, headers: cors }); // notification
    return new Response(JSON.stringify(r), { headers: cors });
  },
};
