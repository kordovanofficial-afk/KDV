#!/usr/bin/env bash
# Kordovan WhatsApp bridge → v1.2 (Baileys 7, LID-aware). Nov 12 2026.
# Backs everything up, installs, starts fresh. Needs ONE QR scan afterwards.
set -e
cd ~/wa-bridge
BASE=https://raw.githubusercontent.com/kordovanofficial-afk/KDV/claude/hopeful-mccarthy-grntwn/tools/wa-bridge
TS=$(date +%Y%m%d-%H%M)
echo "1/5 Downloading new bridge..."
curl -fsSL $BASE/server.js -o /tmp/kdv-server-new.js
curl -fsSL $BASE/package.json -o /tmp/kdv-package-new.json
node --check /tmp/kdv-server-new.js
echo "2/5 Backing up to ~/bridge-backup-$TS ..."
pm2 stop wa-bridge >/dev/null
mkdir -p ~/bridge-backup-$TS && cp -r auth server.js package.json ~/bridge-backup-$TS/ 2>/dev/null || true
echo "3/5 Installing WhatsApp library v7 (2-4 minutes)..."
mv /tmp/kdv-server-new.js server.js; mv /tmp/kdv-package-new.json package.json
rm -rf node_modules package-lock.json
npm install --omit=dev --no-audit --no-fund --loglevel=error
node -e "import('baileys').then(B=>{if(typeof B.makeWASocket!=='function')process.exit(1);console.log('   library OK')})"
echo "4/5 Clearing the old (damaged) session..."
rm -rf auth lid-map.json sent-store.json
pm2 flush wa-bridge >/dev/null
echo "5/5 Starting..."
pm2 restart wa-bridge --update-env >/dev/null
sleep 20
pm2 logs wa-bridge --lines 6 --nostream
echo
echo "DONE. Now open your /qr link and scan it from the office phone."
echo "Undo: pm2 stop wa-bridge; cp -r ~/bridge-backup-$TS/* ~/wa-bridge/; cd ~/wa-bridge; npm install; pm2 restart wa-bridge"
