#!/usr/bin/env bash
# Pull Clarity Data Export (read-only). Token lives OUTSIDE git at /root/.config/clarity_token (never commit it).
# Usage: ./pull.sh [days 1-3] [dimension1: URL|Device|Source|...] [dimension2]
# API limit: ~10 calls/day, last 1-3 days only, aggregated metrics (no recordings).
D=${1:-3}; D1=${2:-URL}; D2=$3
Q="numOfDays=$D&dimension1=$D1"; [ -n "$D2" ] && Q="$Q&dimension2=$D2"
curl -sS -m 30 -H "Authorization: Bearer $(cat /root/.config/clarity_token)" -H "Content-Type: application/json" \
  "https://www.clarity.ms/export-data/api/v1/project-live-insights?$Q"
