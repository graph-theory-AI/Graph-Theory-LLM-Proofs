#!/usr/bin/env bash
# Regenerate the campaign pull request description from the artifacts on disk.
# Run it after pushing new results:  scripts/update-pr.sh [PR_NUMBER]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PY="$ROOT/.venv/bin/python"; [[ -x "$PY" ]] || PY=python3

PR="${1:-}"
if [[ -z "$PR" ]]; then
  PR=$(gh pr list --head "$(git branch --show-current)" --json number --jq '.[0].number')
fi
[[ -n "$PR" && "$PR" != "null" ]] || { echo "no open PR for this branch" >&2; exit 1; }

BODY="$(mktemp)"; trap 'rm -f "$BODY"' EXIT
"$PY" "$ROOT/scripts/pr_body.py" > "$BODY"
gh pr edit "$PR" --body-file "$BODY"
echo "updated PR #$PR ($(wc -c <"$BODY") bytes)"
