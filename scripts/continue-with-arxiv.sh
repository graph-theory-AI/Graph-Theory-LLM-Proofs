#!/usr/bin/env bash
# Second leg of the astra campaign. Waits for the running sweep to finish, then
# spends whatever is left of the same EUR 600 wallet (attacks_opg/spend.json) on
# the arXiv records the first campaign never reached — the 58 tier-4/5 rows that
# were still pending when its budget ran out.
#
#   MIN_EUR=20 JOBS=16 HOURS=6 TIER=flex scripts/continue-with-arxiv.sh
#
# Writes to attacks_arxiv_astra/ so the gpt-5.6-sol artifacts in attacks/ stay
# intact, and passes --done-dir attacks so nothing already attacked is redone.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

MIN_EUR="${MIN_EUR:-20}"
JOBS="${JOBS:-16}"
HOURS="${HOURS:-6}"
TIER="${TIER:-flex}"
PY="$ROOT/.venv/bin/python"

echo "=== continue-with-arxiv: waiting for the running sweep $(date -Is) ==="
while pgrep -f '[a]ttack.py sweep' >/dev/null; do sleep 60; done
echo "=== previous sweep finished $(date -Is) ==="

left=$("$PY" - <<'PY'
import json
d = json.load(open("attacks_opg/spend.json"))
print(f"{d['budget_eur'] - d['safety_margin_eur'] - d['spent_eur']:.2f}")
PY
)
echo "usable left on the shared wallet: EUR $left (minimum to start: EUR $MIN_EUR)"
if "$PY" -c "import sys; sys.exit(0 if float('$left') >= float('$MIN_EUR') else 1)"; then
  :
else
  echo "not enough budget left; not starting the arXiv leg"
  exit 0
fi

"$PY" - <<'PY'
import argparse, attack
attack.configure(argparse.Namespace(corpus="arxiv", model="gpt-6-astra", service_tier="flex",
                                    attacks_dir="attacks_arxiv_astra", wallet="attacks_opg",
                                    done_dir=["attacks"]))
rows = attack.corpus_records()
done = attack.attacked_ids()
pending = [r for r in rows if r["id"] not in done]
print(f"{len(rows)} arXiv rows, {len(done)} already attacked, {len(pending)} pending")
PY

# Artifacts are committed by hand. To commit periodically instead, run the loop
# yourself in another shell:
#   INTERVAL=900 COMMIT_SCRIPT=scripts/commit-opg-attacks.sh scripts/commit-loop.sh

echo "launching arXiv leg jobs=$JOBS hours=$HOURS tier=$TIER $(date -Is)"
exec "$PY" -u "$ROOT/attack.py" sweep --corpus arxiv --model gpt-6-astra \
  --attacks-dir attacks_arxiv_astra --wallet attacks_opg --done-dir attacks \
  --service-tier "$TIER" --jobs "$JOBS" --hours "$HOURS"
