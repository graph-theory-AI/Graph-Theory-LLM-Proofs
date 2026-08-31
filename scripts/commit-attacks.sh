#!/usr/bin/env bash
# Stage attack artifacts, commit if anything changed, push.
# Relies on .gitignore for .env, raw.json, claimed.json, sweep.log.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

git add -A -- attacks README.md attack.py catalog scripts

if git diff --cached --name-only | grep -E '(^|/)(\.env|raw\.json|claimed\.json|spend\.lock)$' >/dev/null; then
  echo "refusing to commit secrets or in-flight lock files" >&2
  git reset HEAD >/dev/null
  exit 1
fi

if git diff --cached --quiet; then
  echo "nothing to commit"
  exit 0
fi

n_verdicts=$(git diff --cached --name-only | grep -c '/verdict.json$' || true)
spent="unknown"
n_attacks="?"
if [[ -f attacks/spend.json ]]; then
  spent=$(python3 -c "import json; s=json.load(open('attacks/spend.json')); print(f\"{s['spent_usd']*s['eur_per_usd']:.2f}\")")
  n_attacks=$(python3 -c "import json; print(json.load(open('attacks/spend.json')).get('n_attacks','?'))")
fi

git commit -m "$(cat <<EOF
Snapshot attack artifacts (${n_verdicts} new/updated verdicts).

Spend €${spent} / budget, ${n_attacks} finished calls.
EOF
)"
git push origin HEAD
echo "pushed $(git rev-parse --short HEAD)"
