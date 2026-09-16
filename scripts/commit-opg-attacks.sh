#!/usr/bin/env bash
# Stage the astra campaign artifacts, commit if anything changed, push.
# Mirrors commit-attacks.sh but for the astra legs: attacks_opg/ (OPG corpus)
# and attacks_arxiv_astra/ (the arXiv records the first campaign never reached),
# which share one wallet in attacks_opg/spend.json.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PY="$ROOT/.venv/bin/python"

# Retry metadata written before the fix stored an absolute path; keep every
# snapshot free of local paths, including files the running sweep just wrote.
if [[ -d "$ROOT/attacks_retry" ]]; then
  grep -rl -- "$ROOT/" "$ROOT/attacks_retry" --include=meta.json 2>/dev/null \
    | xargs -r sed -i "s|$ROOT/||g"
fi
[[ -x "$PY" ]] || PY=python3
"$PY" "$ROOT/attack.py" summary --corpus opg >/dev/null || true
if [[ -d "$ROOT/attacks_retry" ]]; then
  "$PY" "$ROOT/attack.py" summary --corpus retry --wallet attacks_opg >/dev/null || true
fi
if [[ -d "$ROOT/attacks_arxiv_astra" ]]; then
  "$PY" "$ROOT/attack.py" summary --corpus arxiv \
    --attacks-dir attacks_arxiv_astra --wallet attacks_opg --done-dir attacks >/dev/null || true
fi

git add -A -- attacks_opg attacks_arxiv_astra attacks_retry \
  RESULTS_OPG.md RESULTS_ARXIV_ASTRA.md RESULTS_RETRY.md \
  attack.py scripts .gitignore

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
