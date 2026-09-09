# Graph Theory LLM Proofs

AI-assisted attempts at the open graph-theory problems catalogued by Marc
Lelarge and Laurent Viennot at
[graph-theory-ai.github.io/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).

For each problem, [GPT-5.6 Sol](https://openai.com) is asked to look for a
proof, a counterexample, or a meaningful partial result. It may also report
that it could not make progress. These outputs are research artifacts, not
established mathematics: a `proved` or `disproved` label is the model's own
assessment.

[Claude Fable](https://www.anthropic.com/claude/fable) was asked to act as an adversarial reviewer: look for errors, check cited sources, and reproduce computational
claims where possible. This is not human peer review, but its classification
is the status used in this repository. The reports, methodology, and
reproducible checks are in [`verification/`](verification/).

For an overview of the campaign, see [RESULTS.md](RESULTS.md).

## Results

The model completed 633 attacks. Claude Fable reviewed the 77 cases in which GPT-5.6 Sol reported a proof or a counterexample; the remaining categories were not independently reviewed.

| GPT-5.6 Sol verdict | Records | Claude Fable review |
| --- | ---: | --- |
| proved | 31 | all 31 reviewed |
| disproved | 46 | all 46 reviewed |
| already_resolved | 25 | not reviewed |
| partial | 471 | not reviewed |
| ill_posed | 23 | not reviewed |
| unknown | 37 | not reviewed |

### Claims reviewed by Claude Fable (77)

| id | GPT-5.6 Sol verdict | Claude Fable review |
| --- | --- | --- |
| [1601.01886__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1601.01886__00/) | `proved` | [CONFIRMED](verification/1601.01886__00.md) |
| [1610.00239__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1610.00239__00/) | `proved` | [ALREADY_KNOWN](verification/1610.00239__00.md) |
| [1611.03196__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__00/) | `disproved` | [FATAL_ERROR](verification/1611.03196__00.md) |
| [1611.03196__03](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__03/) | `proved` | [CONFIRMED](verification/1611.03196__03.md) |
| [1702.01094__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1702.01094__01/) | `disproved` | [CONFIRMED](verification/1702.01094__01.md) |
| [1704.00125__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1704.00125__01/) | `disproved` | [CONFIRMED](verification/1704.00125__01.md) |
| [1708.02370__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1708.02370__00/) | `disproved` | [FATAL_ERROR](verification/1708.02370__00.md) |
| [1708.08486__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1708.08486__01/) | `disproved` | [FATAL_ERROR](verification/1708.08486__01.md) |
| [1709.09050__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1709.09050__01/) | `proved` | [ALREADY_KNOWN](verification/1709.09050__01.md) |
| [1710.10663__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1710.10663__00/) | `disproved` | [FATAL_ERROR](verification/1710.10663__00.md) |
| [1710.11281__02](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1710.11281__02/) | `disproved` | [MAJOR_GAP](verification/1710.11281__02.md) |
| [1802.03727__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1802.03727__00/) | `proved` | [ALREADY_KNOWN](verification/1802.03727__00.md) |
| [1802.05582__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1802.05582__00/) | `proved` | [MINOR_GAPS](verification/1802.05582__00.md) |
| [1802.05582__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1802.05582__01/) | `proved` | [MINOR_GAPS](verification/1802.05582__01.md) |
| [1806.09726__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1806.09726__00/) | `disproved` | [FATAL_ERROR](verification/1806.09726__00.md) |
| [1809.05439__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1809.05439__00/) | `disproved` | [CONFIRMED](verification/1809.05439__00.md) |
| [1811.08750__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1811.08750__00/) | `disproved` | [MAJOR_GAP](verification/1811.08750__00.md) |
| [1811.12650__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1811.12650__00/) | `proved` | [MINOR_GAPS](verification/1811.12650__00.md) |
| [1812.02420__02](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__02/) | `proved` | [CONFIRMED](verification/1812.02420__02.md) |
| [1812.02420__03](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__03/) | `disproved` | [CONFIRMED](verification/1812.02420__03.md) |
| [1902.06473__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1902.06473__00/) | `proved` | [CONFIRMED](verification/1902.06473__00.md) |
| [1902.10878__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1902.10878__00/) | `disproved` | [ALREADY_KNOWN](verification/1902.10878__00.md) |
| [1902.10878__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1902.10878__01/) | `disproved` | [CONFIRMED](verification/1902.10878__01.md) |
| [1904.12273__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1904.12273__01/) | `disproved` | [CONFIRMED](verification/1904.12273__01.md) |
| [1907.06019__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.06019__00/) | `proved` | [ALREADY_KNOWN](verification/1907.06019__00.md) |
| [1907.06019__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.06019__01/) | `proved` | [CONFIRMED](verification/1907.06019__01.md) |
| [1909.11578__02](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1909.11578__02/) | `disproved` | [ALREADY_KNOWN](verification/1909.11578__02.md) |
| [2001.09679__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2001.09679__00/) | `proved` | [MINOR_GAPS](verification/2001.09679__00.md) |
| [2004.07214__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2004.07214__00/) | `proved` | [ALREADY_KNOWN](verification/2004.07214__00.md) |
| [2004.07457__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2004.07457__01/) | `disproved` | [FATAL_ERROR](verification/2004.07457__01.md) |
| [2005.09767__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2005.09767__00/) | `proved` | [MINOR_GAPS](verification/2005.09767__00.md) |
| [2008.03587__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2008.03587__01/) | `disproved` | [FATAL_ERROR](verification/2008.03587__01.md) |
| [2009.03418__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2009.03418__00/) | `disproved` | [MAJOR_GAP](verification/2009.03418__00.md) |
| [2009.12189__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2009.12189__00/) | `disproved` | [ALREADY_KNOWN](verification/2009.12189__00.md) |
| [2103.15175__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2103.15175__00/) | `proved` | [CONFIRMED](verification/2103.15175__00.md) |
| [2106.14762__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2106.14762__00/) | `proved` | [MINOR_GAPS](verification/2106.14762__00.md) |
| [2108.00991__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2108.00991__00/) | `disproved` | [ALREADY_KNOWN](verification/2108.00991__00.md) |
| [2111.00532__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2111.00532__00/) | `proved` | [ALREADY_KNOWN](verification/2111.00532__00.md) |
| [2111.00532__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2111.00532__01/) | `proved` | [ALREADY_KNOWN](verification/2111.00532__01.md) |
| [2204.10119__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2204.10119__01/) | `disproved` | [CONFIRMED](verification/2204.10119__01.md) |
| [2204.12330__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2204.12330__00/) | `proved` | [ALREADY_KNOWN](verification/2204.12330__00.md) |
| [2207.07775__02](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2207.07775__02/) | `disproved` | [FATAL_ERROR](verification/2207.07775__02.md) |
| [2208.06858__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2208.06858__01/) | `disproved` | [CONFIRMED](verification/2208.06858__01.md) |
| [2208.10074__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2208.10074__00/) | `disproved` | [ALREADY_KNOWN](verification/2208.10074__00.md) |
| [2209.09107__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2209.09107__00/) | `disproved` | [CONFIRMED](verification/2209.09107__00.md) |
| [2211.01032__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__00/) | `disproved` | [FATAL_ERROR](verification/2211.01032__00.md) |
| [2211.01032__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__01/) | `disproved` | [FATAL_ERROR](verification/2211.01032__01.md) |
| [2211.01032__02](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__02/) | `proved` | [MINOR_GAPS](verification/2211.01032__02.md) |
| [2304.03567__04](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2304.03567__04/) | `disproved` | [CONFIRMED](verification/2304.03567__04.md) |
| [2306.04710__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2306.04710__01/) | `proved` | [ALREADY_KNOWN](verification/2306.04710__01.md) |
| [2307.15048__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2307.15048__00/) | `disproved` | [FATAL_ERROR](verification/2307.15048__00.md) |
| [2307.15512__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2307.15512__00/) | `disproved` | [CONFIRMED](verification/2307.15512__00.md) |
| [2308.15387__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2308.15387__00/) | `disproved` | [ALREADY_KNOWN](verification/2308.15387__00.md) |
| [2308.15721__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2308.15721__00/) | `disproved` | [FATAL_ERROR](verification/2308.15721__00.md) |
| [2310.04265__09](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2310.04265__09/) | `disproved` | [CONFIRMED](verification/2310.04265__09.md) |
| [2310.04265__11](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2310.04265__11/) | `disproved` | [CONFIRMED](verification/2310.04265__11.md) |
| [2312.13061__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2312.13061__01/) | `disproved` | [MINOR_GAPS](verification/2312.13061__01.md) |
| [2401.00299__02](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2401.00299__02/) | `proved` | [CONFIRMED](verification/2401.00299__02.md) |
| [2405.03455__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2405.03455__00/) | `proved` | [CONFIRMED](verification/2405.03455__00.md) |
| [2405.14795__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2405.14795__00/) | `proved` | [ALREADY_KNOWN](verification/2405.14795__00.md) |
| [2408.02400__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2408.02400__00/) | `proved` | [CONFIRMED](verification/2408.02400__00.md) |
| [2409.18220__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2409.18220__00/) | `disproved` | [FATAL_ERROR](verification/2409.18220__00.md) |
| [2410.13008__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2410.13008__00/) | `disproved` | [ALREADY_KNOWN](verification/2410.13008__00.md) |
| [2503.16882__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2503.16882__00/) | `disproved` | [FATAL_ERROR](verification/2503.16882__00.md) |
| [2503.23191__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2503.23191__00/) | `disproved` | [ALREADY_KNOWN](verification/2503.23191__00.md) |
| [2505.24100__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2505.24100__00/) | `proved` | [ALREADY_KNOWN](verification/2505.24100__00.md) |
| [2505.24100__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2505.24100__01/) | `proved` | [MINOR_GAPS](verification/2505.24100__01.md) |
| [2506.07264__01](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2506.07264__01/) | `proved` | [ALREADY_KNOWN](verification/2506.07264__01.md) |
| [2507.04254__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2507.04254__00/) | `disproved` | [ALREADY_KNOWN](verification/2507.04254__00.md) |
| [2508.08870__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2508.08870__00/) | `disproved` | [CONFIRMED](verification/2508.08870__00.md) |
| [2511.02892__03](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2511.02892__03/) | `disproved` | [ALREADY_KNOWN](verification/2511.02892__03.md) |
| [2512.10438__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2512.10438__00/) | `proved` | [CONFIRMED](verification/2512.10438__00.md) |
| [2512.17232__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2512.17232__00/) | `disproved` | [ALREADY_KNOWN](verification/2512.17232__00.md) |
| [2512.17342__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2512.17342__00/) | `disproved` | [ALREADY_KNOWN](verification/2512.17342__00.md) |
| [2602.16333__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2602.16333__00/) | `proved` | [ALREADY_KNOWN](verification/2602.16333__00.md) |
| [2603.02786__03](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2603.02786__03/) | `disproved` | [CONFIRMED](verification/2603.02786__03.md) |
| [2604.09449__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2604.09449__00/) | `disproved` | [ALREADY_KNOWN](verification/2604.09449__00.md) |

### Review-status definitions

| Review status | Meaning |
| --- | --- |
| `CONFIRMED` | Every step was found valid, sources were checked, the interpretation was judged fair, and any finite construction was computationally verified where applicable. |
| `MINOR_GAPS` | The main result appears correct, but routine, repairable details remain. |
| `MAJOR_GAP` | A substantial gap remains. It may be repairable, but the current write-up does not resolve it. |
| `FATAL_ERROR` | The claim contains an irreparable error or fails a computational check. |
| `ALREADY_KNOWN` | The result appears correct, but was already established in the literature. |


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
