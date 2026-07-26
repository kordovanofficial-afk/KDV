#!/bin/bash
# ============================================================================
# KORDOVAN WhatsApp bridge — one-shot installer for Ubuntu (Oracle / GCP / any)
#
# Installs Node, writes the bridge, generates passwords, sets it to auto-restart
# forever, and opens a public web address. Prints everything you need at the end.
#
# Safe to run twice — it will just reinstall cleanly.
# ============================================================================
set -e

GREEN='\033[0;32m'; YEL='\033[1;33m'; NC='\033[0m'
say() { echo -e "${GREEN}==>${NC} $1"; }

DIR="$HOME/wa-bridge"
WORKER_INBOUND="https://kordovan-postex-sync.kordovan-official.workers.dev/wa-inbound"

# ── 1. System packages ──────────────────────────────────────────────────────
say "Installing Node.js (about a minute)…"
if ! command -v node >/dev/null 2>&1; then
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - >/dev/null 2>&1
  sudo apt-get install -y nodejs >/dev/null 2>&1
fi
say "Node $(node -v) ready"

# ── 2. Folder ───────────────────────────────────────────────────────────────
mkdir -p "$DIR" && cd "$DIR"

# ── 3. package.json ─────────────────────────────────────────────────────────
cat > package.json <<'PKGEOF'
{
  "name": "kordovan-wa-bridge",
  "version": "1.1.0",
  "private": true,
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": {
    "@whiskeysockets/baileys": "^6.7.9",
    "express": "^4.21.2",
    "pino": "^9.5.0",
    "qrcode": "^1.5.4"
  },
  "engines": { "node": ">=20" }
}
PKGEOF

# ── 4. server.js is fetched from the repo copy placed next to this script ────
if [ ! -f "$DIR/server.js" ]; then
  if [ -f "$(dirname "$0")/server.js" ]; then
    cp "$(dirname "$0")/server.js" "$DIR/server.js"
  else
    echo "ERROR: server.js not found next to install.sh. Put both files in the same folder."
    exit 1
  fi
fi

# ── 5. Passwords — generated, never typed ───────────────────────────────────
if [ ! -f .env ]; then
  BRIDGE_SECRET=$(head -c 32 /dev/urandom | base64 | tr -dc 'A-Za-z0-9' | head -c 40)
  ADMIN_KEY=$(head -c 32 /dev/urandom | base64 | tr -dc 'A-Za-z0-9' | head -c 24)
  cat > .env <<ENVEOF
BRIDGE_SECRET=$BRIDGE_SECRET
ADMIN_KEY=$ADMIN_KEY
WORKER_INBOUND=$WORKER_INBOUND
AUTH_DIR=./auth
PORT=8787
ENVEOF
  say "Generated new passwords"
else
  say "Keeping the .env that is already here"
fi
set -a; . ./.env; set +a

# ── 6. Dependencies ─────────────────────────────────────────────────────────
say "Installing the WhatsApp library (2–3 minutes, be patient)…"
npm install --omit=dev --no-audit --no-fund >/dev/null 2>&1
say "Installed"

# ── 7. Keep it alive forever ────────────────────────────────────────────────
say "Setting up auto-restart…"
sudo npm install -g pm2 >/dev/null 2>&1 || true
pm2 delete wa-bridge >/dev/null 2>&1 || true
pm2 start server.js --name wa-bridge --update-env >/dev/null
pm2 save >/dev/null 2>&1
sudo env PATH=$PATH pm2 startup systemd -u "$USER" --hp "$HOME" >/dev/null 2>&1 || true
pm2 save >/dev/null 2>&1

# ── 8. Public web address (Cloudflare Tunnel — free, no firewall changes) ────
say "Setting up the web address…"
ARCH=$(uname -m); CF_ARCH=amd64
[ "$ARCH" = "aarch64" ] && CF_ARCH=arm64
if ! command -v cloudflared >/dev/null 2>&1; then
  curl -sL "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-$CF_ARCH" -o /tmp/cloudflared
  chmod +x /tmp/cloudflared && sudo mv /tmp/cloudflared /usr/local/bin/cloudflared
fi
pm2 delete tunnel >/dev/null 2>&1 || true
pm2 start cloudflared --name tunnel -- tunnel --url http://localhost:8787 >/dev/null
pm2 save >/dev/null 2>&1

say "Waiting for the web address…"
URL=""
for i in $(seq 1 30); do
  sleep 2
  URL=$(pm2 logs tunnel --lines 200 --nostream 2>/dev/null | grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' | tail -1 || true)
  [ -n "$URL" ] && break
done

# ── 9. Done ─────────────────────────────────────────────────────────────────
echo
echo "============================================================"
echo -e "${GREEN}  DONE — everything is installed and running${NC}"
echo "============================================================"
echo
if [ -n "$URL" ]; then
  echo -e "${YEL}1) OPEN THIS TO LINK WHATSAPP (scan the QR):${NC}"
  echo "   $URL/qr?k=$ADMIN_KEY"
  echo
  echo -e "${YEL}2) BOOKMARK THIS to check on it any time:${NC}"
  echo "   $URL/status?k=$ADMIN_KEY"
  echo
  echo -e "${YEL}3) SEND CLAUDE THIS LINE (copy it exactly):${NC}"
  echo "   BRIDGE_URL=$URL"
  echo "   BRIDGE_SECRET=$BRIDGE_SECRET"
else
  echo -e "${YEL}The web address is still starting. Run this in a minute:${NC}"
  echo "   pm2 logs tunnel --lines 50 --nostream | grep trycloudflare"
  echo "   ADMIN_KEY=$ADMIN_KEY"
  echo "   BRIDGE_SECRET=$BRIDGE_SECRET"
fi
echo
echo "Useful later:  pm2 list   ·   pm2 logs wa-bridge   ·   pm2 restart wa-bridge"
echo "============================================================"
