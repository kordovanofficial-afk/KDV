// Kordovan Social Scheduler — free Cloudflare Worker (v1.0, Nov 21 2026)
// Posts scheduled Instagram + Facebook STORIES and FEED posts through Meta's free Graph API.
// Cron (every 10 min) publishes due jobs. Claude queues jobs via POST /queue (header x-sched-key).
//
// Bindings / settings (Cloudflare dashboard → Worker → Settings):
//   KV namespace binding:  SOCIAL            (any new KV namespace)
//   Secret:  META_PAGE_TOKEN   long-lived Facebook PAGE access token (see setup guide)
//   Secret:  SCHED_KEY         random key Claude uses to queue jobs
//   Vars:    PAGE_ID=2738478432836892  IG_USER_ID=17841440239172690  GRAPH_VERSION=v25.0
//   Trigger: Cron  */10 * * * *
//
// Job shape: { id, at: ISO-8601 time, type: "story"|"post", platforms: ["ig","fb"],
//              image_url: public https JPG/PNG, caption?: string }
// Limits (Meta): no link/poll stickers via API; stories live 24h; IG ~100 API posts per 24h.

const VERSION = 'social-1.0';

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname === '/health') return json({ ok: true, version: VERSION });
    if (req.headers.get('x-sched-key') !== env.SCHED_KEY || !env.SCHED_KEY) return json({ error: 'unauthorized' }, 401);

    if (url.pathname === '/queue' && req.method === 'GET') return json(await loadJobs(env));
    if (url.pathname === '/queue' && req.method === 'POST') {
      const body = await req.json();
      const items = Array.isArray(body) ? body : [body];
      const jobs = await loadJobs(env);
      const added = [];
      for (const it of items) {
        const err = validate(it);
        if (err) return json({ error: err, item: it }, 400);
        const job = { id: it.id || crypto.randomUUID(), at: new Date(it.at).toISOString(), type: it.type,
          platforms: it.platforms || ['ig', 'fb'], image_url: it.image_url, caption: it.caption || '',
          status: 'pending', tries: 0, results: {} };
        const i = jobs.findIndex(j => j.id === job.id);
        if (i >= 0) jobs[i] = job; else jobs.push(job);
        added.push(job.id);
      }
      jobs.sort((a, b) => a.at.localeCompare(b.at));
      await saveJobs(env, jobs);
      return json({ ok: true, added });
    }
    if (url.pathname === '/delete' && req.method === 'POST') {
      const { id } = await req.json();
      const jobs = (await loadJobs(env)).filter(j => j.id !== id);
      await saveJobs(env, jobs);
      return json({ ok: true, remaining: jobs.length });
    }
    if (url.pathname === '/run' && req.method === 'POST') return json(await runDue(env));
    if (url.pathname === '/test') {
      // Checks the token can see the Page and the Instagram account. Publishes nothing.
      const page = await g(env, 'GET', `${env.PAGE_ID}`, { fields: 'id,name' });
      const ig = await g(env, 'GET', `${env.IG_USER_ID}`, { fields: 'id,username' });
      const perms = await g(env, 'GET', 'me/permissions', {});
      return json({ page, ig, perms });
    }
    return json({ error: 'not found' }, 404);
  },

  async scheduled(event, env, ctx) {
    ctx.waitUntil(runDue(env));
  },
};

function validate(it) {
  if (!it || !it.at || isNaN(new Date(it.at))) return 'missing/invalid "at"';
  if (!['story', 'post'].includes(it.type)) return 'type must be story or post';
  if (!/^https:\/\//.test(it.image_url || '')) return 'image_url must be a public https URL';
  if (it.platforms && !it.platforms.every(p => ['ig', 'fb'].includes(p))) return 'platforms must be ig/fb';
  return null;
}

async function loadJobs(env) { return JSON.parse((await env.SOCIAL.get('jobs')) || '[]'); }
async function saveJobs(env, jobs) {
  // keep finished jobs for 14 days for the record
  const cutoff = Date.now() - 14 * 864e5;
  await env.SOCIAL.put('jobs', JSON.stringify(jobs.filter(j => j.status === 'pending' || new Date(j.at) > cutoff)));
}

async function runDue(env) {
  const jobs = await loadJobs(env);
  const now = Date.now();
  const ran = [];
  for (const job of jobs) {
    if (job.status !== 'pending' || new Date(job.at).getTime() > now) continue;
    job.tries = (job.tries || 0) + 1;
    for (const p of job.platforms) {
      if (job.results[p] && job.results[p].ok) continue; // already posted on this platform
      try {
        const id = p === 'ig' ? await publishIG(env, job) : await publishFB(env, job);
        job.results[p] = { ok: true, id, at: new Date().toISOString() };
      } catch (e) {
        job.results[p] = { ok: false, error: String(e.message || e).slice(0, 300), at: new Date().toISOString() };
      }
    }
    const allOk = job.platforms.every(p => job.results[p] && job.results[p].ok);
    job.status = allOk ? 'done' : (job.tries >= 3 ? 'failed' : 'pending');
    ran.push({ id: job.id, status: job.status, results: job.results });
  }
  await saveJobs(env, jobs);
  return { ran };
}

async function publishIG(env, job) {
  const params = { image_url: job.image_url };
  if (job.type === 'story') params.media_type = 'STORIES';
  else params.caption = job.caption;
  const c = await g(env, 'POST', `${env.IG_USER_ID}/media`, params);
  // wait for the container to be ready (up to ~30s)
  for (let i = 0; i < 10; i++) {
    const s = await g(env, 'GET', c.id, { fields: 'status_code' });
    if (s.status_code === 'FINISHED') break;
    if (s.status_code === 'ERROR') throw new Error('IG container error');
    await sleep(3000);
  }
  const pub = await g(env, 'POST', `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  return pub.id;
}

async function publishFB(env, job) {
  if (job.type === 'post') {
    const r = await g(env, 'POST', `${env.PAGE_ID}/photos`, { url: job.image_url, message: job.caption, published: 'true' });
    return r.post_id || r.id;
  }
  const photo = await g(env, 'POST', `${env.PAGE_ID}/photos`, { url: job.image_url, published: 'false' });
  const st = await g(env, 'POST', `${env.PAGE_ID}/photo_stories`, { photo_id: photo.id });
  return st.post_id || st.id || photo.id;
}

async function g(env, method, path, params) {
  const v = env.GRAPH_VERSION || 'v25.0';
  const u = new URL(`https://graph.facebook.com/${v}/${path}`);
  const body = new URLSearchParams({ ...params, access_token: env.META_PAGE_TOKEN });
  let res;
  if (method === 'GET') { body.forEach((val, k) => u.searchParams.set(k, val)); res = await fetch(u); }
  else res = await fetch(u, { method, body });
  const data = await res.json();
  if (!res.ok || data.error) throw new Error((data.error && data.error.message) || `HTTP ${res.status}`);
  return data;
}

const sleep = ms => new Promise(r => setTimeout(r, ms));
const json = (o, s = 200) => new Response(JSON.stringify(o, null, 2), { status: s, headers: { 'content-type': 'application/json' } });
