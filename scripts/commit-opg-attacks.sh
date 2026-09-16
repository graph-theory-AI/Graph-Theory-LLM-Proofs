#!/usr/bin/env bash
# Stage the OPG/astra campaign artifacts, commit if anything changed, push.
# Mirrors commit-attacks.sh but for attacks_opg/ and RESULTS_OPG.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PY="$ROOT/.venv/bin/python"
[[ -x "$PY" ]] || PY=python3
"$PY" "$ROOT/attack.py" summary --corpus opg >/dev/null || true

git add -A -- attacks_opg RESULTS_OPG.md attack.py scripts .gitignore

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
if [[ -f attacks_opg/spend.json ]]; then
  spent=$("$PY" -c "import json;d=json.load(open('attacks_opg/spend.json'));print(f\"{d['spent_eur']:.2f}/{d['budget_eur']:.0f} EUR, {d['n_attacks']} attacks\")")
fi
git commit -q -m "OPG/astra sweep snapshot ($n_verdicts new verdicts; $spent)."
git push -q origin HEAD
echo "committed and pushed ($n_verdicts new verdicts; $spent)"
