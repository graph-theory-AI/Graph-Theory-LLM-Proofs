#!/usr/bin/env bash
# Commit-and-push attack files every INTERVAL seconds while a sweep is
# running, then once more after it exits.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INTERVAL="${INTERVAL:-600}"
empty=0
cd "$ROOT"
echo "commit-loop every ${INTERVAL}s starting $(date -Is)"
while true; do
  sleep "$INTERVAL"
  if "$ROOT/scripts/commit-attacks.sh"; then
    empty=0
  else
    : # commit-attacks already printed the reason
  fi
  if ! pgrep -f '[a]ttack.py sweep' >/dev/null; then
    "$ROOT/scripts/commit-attacks.sh" || true
    if [[ -z "$(git status --porcelain)" ]]; then
      empty=$((empty + 1))
      if [[ "$empty" -ge 2 ]]; then
        echo "sweep gone and tree clean; commit-loop exiting $(date -Is)"
        exit 0
      fi
    else
      empty=0
    fi
  fi
done
