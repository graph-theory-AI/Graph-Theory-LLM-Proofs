# Graph Theory LLM Proofs

AI-assisted attempts at the open graph-theory problems catalogued by Marc
Lelarge and Laurent Viennot at
[graph-theory-ai.github.io/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).

For each problem, [GPT-5.6 Sol](https://openai.com) is asked to look for a
proof, a counterexample, or a meaningful partial result. It may also report
that it could not make progress. These outputs are research artifacts, not
established mathematics: a `proved` or `disproved` label is the model's own
assessment.

A [Claude Fable](https://www.anthropic.com/claude/fable) was
asked to act as an adversarial reviewer: look for errors, check cited sources, and reproduce computational
claims where possible. This is not human peer review, but its classification
is the status used in this repository. The reports, methodology, and
reproducible checks are in [`verification/`](verification/).

For an overview of the campaign, see [RESULTS.md](RESULTS.md).

## Method

- **Queue.** Easiest-first open/partial arXiv records from Lelarge's difficulty
  ranking, plus six questions restored after
  [catalog extraction fixes](https://github.com/mlelarge/graph-conjectures/pull/3).
  Open Problem Garden entries were not attacked.
- **Prompt.** Catalog page + extracted statement JSON + arXiv abstract.
- **Attack model.** [GPT-5.6 Sol](https://openai.com), one Responses API call
  per record with effort `max`, `reasoning.mode=pro`, and
  `max_output_tokens=128000`.
- **Review model.** The 77 claimed proofs/counterexamples were adversarially
  reviewed with [Claude Fable](https://www.anthropic.com/claude/fable); see
  [`verification/`](verification/) for the review protocol and reports.
- **Budget.** Hard euro cap in `attacks/spend.json`, with a per-call USD
  reserve so parallel jobs cannot overspend. Pricing is the Sol promo schedule
  through 2026-11-21 ($4 / $0.40 cached / $20 per 1M tokens; reasoning bills as
  output). Prepaid EUR→USD is taken from the first wallet (€250 credit ≈
  $241.36 API), not from a market FX rate.
- **Artifact.** `attacks/<id>/{prompt.md,output.md,verdict.json,usage.json}`.

A single call is capped at 128k output tokens (~$2.56 of output at promo
rates). The preflight reserve is a conservative **$3.50** because `mode=pro`
can do extra internal work.

## Layout

```
attack.py          # queue / run / sweep / summary
catalog/           # snapshot of the Lelarge catalog (not authored here)
attacks/<id>/      # one directory per attempted record
RESULTS.md         # generated index of verdicts
verification/      # adversarial reviews of claimed proofs/counterexamples
scripts/           # commit loop and campaign ops
```

## Setup

```bash
uv venv
uv pip install -r requirements.txt
# .env must contain OPENAI_API_KEY (gitignored)
```

```bash
python attack.py summary          # rebuild RESULTS.md
python attack.py spend            # remaining budget
python attack.py queue            # easiest-first leftover queue
python attack.py run --id ID      # one record, e.g. 2402.10782__01
python attack.py sweep --jobs 24 --hours 16
```

## Acknowledgements

The ChatGPT-based attack campaign used API access provided by the Lamarr
Institute for Machine Learning and Artificial Intelligence.

<p align="center">
  <img src="assets/lamarr-logo-2023-negative.svg" alt="Lamarr Institute for Machine Learning and Artificial Intelligence" width="300">
</p>

## License

Code is [MIT](LICENSE). Catalog JSON/Markdown under `catalog/` is copied from
[graph-theory-ai/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures/);
see that repository for its data license. Model outputs in `attacks/` are
provided as research artifacts, not as verified mathematics.
