# Graph Theory LLM Proofs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22706596.svg)](https://doi.org/10.5281/zenodo.22706596)

Thirty-six results in graph theory, each a complete proof or an explicit
counterexample to an open problem from the
[graph-conjectures catalogue](https://graph-theory-ai.github.io/graph-conjectures).
Each was produced by a language model and then checked by a second, adversarial
language model that could not break it.
**None has yet been read by a human mathematician.** That is what we are asking
for.

Every result below is a short self-contained note: the problem as it was posed,
the theorem, proof ideas in the text, full proofs in an appendix, and the
referee's report in a second appendix. Pick one in your area and read it as you
would a submission. Whether you find an error, a gap, a known result, or nothing
wrong at all, we would like to hear:
[open an issue](https://github.com/graph-theory-AI/Graph-Theory-LLM-Proofs/issues/new)
or write to `emanuele.natale🐌inria.fr`.

Two caveats before you start. "Confirmed" means one machine referee re-derived
every step, checked every citation, and brute-forced every finite object, then
failed to find an error; it is not a theorem. And novelty was checked only
against what could be found online: several results in this repository turned
out to have been published days or weeks before they were generated, and those
are excluded below, but the same could happen to any of these.

## Results awaiting human review


### Colouring, covering and flows

| Result | Problem | Notes |
|:--|:--|:--|
| [The list Ramsey number of the graphs with chromatic number greater than $s$ is exactly $s^k+1$](to_review/2103.15175__00__multicolor-list-Ramsey-number-equals-s-to-the-k-plus-1__note.pdf) | [Conjecture of Fox, He, Luo and Xu](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2103.15175__00/) | [Rocq proof](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/extremal-graph-theory/theories/applications/list_ramsey_graph.v) |
| [For every $k\ge 5$ a graph with clique number 4, cochromatic number $k$ and chromatic number $k+3$](to_review/2408.02400__00__chromatic-minus-cochromatic-number-Mycielski-construction__note.pdf) | [Problem 1.5 of Steiner](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2408.02400__00/) | [Rocq proof](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/chromatic-theory/theories/applications/cochromatic_gap/cochromatic_gap.v) |
| [The circular chromatic number of the orthogonality graph of $\mathbb{R}^3$ is exactly 4](to_review_astra/circular_colouring_the_orthogonality_graph__orthogonality-graph-circular-chromatic-number-is-4__note.pdf) | [OpenProblemGarden; Conjecture 4.41 of Ghebleh's thesis](https://graph-theory-ai.github.io/graph-conjectures/op/circular_colouring_the_orthogonality_graph/) | OpenProblemGarden |
| [The circular mixing threshold of a graph with an edge is rational with reduced numerator at most $n+1$](to_review_astra/mixing_circular_colourings_0__circular-mixing-threshold-rational-numerator-at-most-n-plus-1__note.pdf) | [OpenProblemGarden](https://graph-theory-ai.github.io/graph-conjectures/op/mixing_circular_colourings_0/) | OpenProblemGarden |
| [A random $h$-lift of $K_5$ is 3-chromatic asymptotically almost surely](to_review_astra/chromatic_number_of_random_lifts_of_complete_graphs__random-lifts-of-K5-are-3-chromatic__note.pdf) | [OpenProblemGarden](https://graph-theory-ai.github.io/graph-conjectures/op/chromatic_number_of_random_lifts_of_complete_graphs/) | OpenProblemGarden |
| [Rosenfeld's hypergraph generalization of Vizing's theorem is false: a simple 100-uniform counterexample (astronomically large)](to_review_astra/a_generalization_of_vizings_theorem__rosenfeld-hypergraph-vizing-disproof-100-uniform__note.pdf) | [OpenProblemGarden](https://graph-theory-ai.github.io/graph-conjectures/op/a_generalization_of_vizings_theorem/) | OpenProblemGarden |
| [Powers of cycles have equivalence covering number $\Theta(\log k)$, not $\Omega(k)$](to_review_astra/covering_powers_of_cycles_with_equivalence_subgraphs__equivalence-covering-powers-of-cycles-log-k__note.pdf) | [OpenProblemGarden, from West's REGS problems](https://graph-theory-ai.github.io/graph-conjectures/op/covering_powers_of_cycles_with_equivalence_subgraphs/) | OpenProblemGarden |
| [Triangle-free graphs of large chromatic number with a stable-set cover admitting no privately covered induced path](to_review/1702.01094__01__stable-set-covers-no-privately-covered-induced-path__note.pdf) | [Question of Scott and Seymour](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1702.01094__01/) | — |
| [Exponentially many $f$-avoiding flows for abelian groups of order 6 and 7](to_review/2005.09767__00__group-connectivity-exponentially-many-flows-Z6-Z7__note.pdf) | [Conjecture 1.10 of DeVos, Langhede, Mohar and Šámal](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2005.09767__00/) | — |

### Digraphs and tournaments

| Result | Problem | Notes |
|:--|:--|:--|
| [An infinite family of 3-critical tournaments: no bounded-size witness for tournament clique number](to_review/2310.04265__09__3-critical-tournaments-clique-number-question-5.9__note.pdf) | [Question 5.9 of Aboulker, Aubian, Charbit and Lopes](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2310.04265__09/) | [Rocq proof](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/digraph-theory/theories/applications/question_5_9_resolution.v) |
| [A 6-edge-coloured 9-vertex tournament whose longest colour-avoiding path is shorter than any transitive one allows](to_review/2512.10438__00__color-avoiding-paths-tournaments-q6-N9-example__note.pdf) | [Problem 5.1 of arXiv:2512.10438](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2512.10438__00/) | [Rocq proof](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/digraph-theory/theories/applications/color_avoiding_tournament.v) |
| [The five-vertex tournament $C_3[TT_2,TT_2,1]$ is a counterexample to Conjecture 24](to_review_astra/2506.08810__03__five-vertex-tournament-counterexample-conjecture-24__note.pdf) | [Bonamy, Groenland, Johnston, Morrison and Scott](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2506.08810__03/) | — |
| [Deciding whether the fractional dichromatic number is at most 2 is NP-complete](to_review/1812.02420__02__fractional-dichromatic-number-2-NP-complete__note.pdf) | [Problem 3.21 of arXiv:1812.02420](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__02/) | — |
| [Directed Kneser graphs with the acyclic-iff-intersecting property exist only for $b\le 2$ or $k\le b+1$](to_review/1812.02420__03__directed-Kneser-graphs-acyclic-iff-intersecting__note.pdf) | [Problem 5.40 of arXiv:1812.02420](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__03/) | [Rocq proof](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/digraph-theory/theories/applications/directed_kneser_nonexistence.v) |

### Extremal and structural graph theory

| Result | Problem | Notes |
|:--|:--|:--|
| [Fair representation by matchings in bipartite graphs holds with $c(m)=32(m+1)^3$](to_review/1611.03196__03__fair-representation-matchings-bipartite-c-of-m-bound__note.pdf) | [Conjecture 1.15 of Aharoni, Alon, Berger, Chudnovsky, Kotlar, Loebl and Ziv](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__03/) | — |
| [The biconstrained function $\psi$ is not symmetric: $\psi(2/7,5/7)\le 23/28<6/7=\psi(5/7,2/7)$](to_review/1902.10878__01__concatenating-bipartite-graphs-psi-not-symmetric__note.pdf) | [Question of Chudnovsky, Hompe, Scott, Seymour and Spirkl](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1902.10878__01/) | — |
| [Linear-size deletion-saturated graphs for even cycles, from line graphs of cubic hypohamiltonian graphs](to_review/2505.24100__01__induced-saturation-even-cycles-line-graphs-hypohamiltonian__note.pdf) | [Question 1.8 of Fan, Hajebi, Hajebi and Spirkl](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2505.24100__01/) | — |
| [The Szeged–Wiener difference of a 2-connected graph is at least $\min\{2n,3n-10\}$ outside three exceptional families](to_review_astra/1602.05184__00__szeged-wiener-strengthening-eta-at-least-2n-for-2-connected__note.pdf) | [Conjecture 5 of Bonamy, Knor, Lužar, Pinlou and Škrekovski](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1602.05184__00/) | — |
| [Upper irredundance equals independence in direct products of complete multipartite graphs](to_review_astra/1904.02595__00__tensor-rank-bound-retaining-lonely-vertices__note.pdf) | [Conjecture 1.2 of Alon and Defant](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1904.02595__00/) | — |
| [Nearly representative Hamilton cycles with vector discrepancy $O(k\log k)$ instead of $O(k^2)$](to_review_astra/2604.09449__03__colour-balanced-hamilton-cycles-k-log-k__note.pdf) | [Problem 6.4 of Hogan, Scott and Tsarev](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2604.09449__03/) | — |
| [A contraction- and subdivision-closed class refutes the quasi-isometry conjecture for such classes](to_review_astra/2509.09031__00__quasi-isometry-conjecture-contraction-closed-counterexample__note.pdf) | [Conjecture 1.2 of arXiv:2509.09031, also Conjecture 8 of Davies, Hatzel and Hickingbotham](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2509.09031__00/) | — |
| [The exact value of Dvořák's exponent $b_\varepsilon$ relating sublinear separators to expansion: $b_\varepsilon=\tfrac{1}{2\varepsilon}-1$](to_review/2001.09679__00__sublinear-separators-expansion-exponent-Dvorak-b-eps__note.pdf) | [Question of Dvořák](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2001.09679__00/) | — |
| [A 37-vertex counterexample to Melnikov's valency-variety inequality as stated (it relies on an isolated vertex; the connected version stays open)](to_review_astra/melnikovs_valency_variety_problem__melnikov-valency-variety-37-vertex-counterexample__note.pdf) | [OpenProblemGarden](https://graph-theory-ai.github.io/graph-conjectures/op/melnikovs_valency_variety_problem/) | OpenProblemGarden |

### Random graphs and probabilistic combinatorics

| Result | Problem | Notes |
|:--|:--|:--|
| [The expected number of faces of a random embedding of a dense simple graph is $\Theta(\log n)$](to_review/2211.01032__02__random-embeddings-expected-faces-Theta-log-n__note.pdf) | [Conjecture 9.3 of Campion Loth, Halasz, Masařík, Mohar and Šámal](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__02/) | — |
| [Non-orientable random embeddings of $K_n$ have at most $\ln n+O(1)$ expected faces](to_review_astra/2211.01032__03__nonorientable-random-embeddings-expected-faces-ln-n__note.pdf) | [Conjecture 9.5 of the same paper](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__03/) | — |
| [The random irregular subgraph has Property $(\ast)$ for all $d=o(n/\log n)$, removing eleven logarithms from the published bound](to_review_astra/2207.13651__00__fox-luo-pham-random-subgraph-threshold-d-log-n__note.pdf) | [Conjecture of Fox, Luo and Pham](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2207.13651__00/) | — |
| [Monotone strategies in Levine's hat problem reach success probability $\tfrac12$ for every number of players](to_review/2208.06858__01__Levine-hat-problem-monotone-strategies-reach-one-half__note.pdf) | [Conjecture 2.2 of arXiv:2208.06858](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2208.06858__01/) | — |

### Geometry, topology and games

| Result | Problem | Notes |
|:--|:--|:--|
| [A 12-vertex planar graph with feedback vertex set 5 and feedback path number 2 refutes $\mathrm{fvs}\le 2\,\mathrm{fp}$](to_review_astra/1912.01570__00__planar-fvs-vs-feedback-path-number-12-vertex-counterexample__note.pdf) | [Conjecture 2 of Bonamy, Dross, Masařík, Nadara, Pilipczuk and Pilipczuk](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1912.01570__00/) | — |
| [The Kleetope of $K_4$: a 3-connected graph in which no positive edge lengths make every geodesic cycle peripheral](to_review_astra/geodesic_cycles_and_tuttes_theorem__kleetope-of-K4-refutes-georgakopoulos-spruessel-problem-3__note.pdf) | [OpenProblemGarden; Problem 3 of Georgakopoulos and Sprüssel](https://graph-theory-ai.github.io/graph-conjectures/op/geodesic_cycles_and_tuttes_theorem/) | OpenProblemGarden |
| [Point sets whose complete geometric graph needs $\tfrac34 n-O(\sqrt n)$ crossing-free paths](to_review_astra/2507.10840__01__plane-path-partition-number-odd-polygon-central-cluster__note.pdf) | [Problem 9 of arXiv:2507.10840](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2507.10840__01/) | — |
| [Big line or big convex polygon: the dependence on the collinearity parameter $\ell$ is uniformly linear](to_review/2405.03455__00__Erdos-Szekeres-big-line-or-big-convex-polygon-linear-in-l__note.pdf) | [Open problem of arXiv:2405.03455](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2405.03455__00/) | — |
| [The number of partitions of the hypercube into squares has the conjectured asymptotic](to_review/2401.00299__02__hypercube-partitions-into-squares-asymptotics__note.pdf) | [Problem of Alon, Balogh and Potapov](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2401.00299__02/) | — |
| [Zombies can gain by waiting: a 59-vertex cactus whose zombie number drops when a leaf is attached](to_review_astra/2008.03587__00__deterministic-zombies-waiting-helps-59-vertex-cactus__note.pdf) | [Question 4.1 of arXiv:2008.03587](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2008.03587__00/) | — |
| [A Moore-type bound rules out local dictator-to-XOR bijections beyond a threshold](to_review_astra/1812.09215__00__moore-type-bound-disproves-bijection-existence__note.pdf) | [Question of Johnston and Scott](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.09215__00/) | — |

### Additive combinatorics

| Result | Problem | Notes |
|:--|:--|:--|
| [Packings of arithmetic progressions with all differences in $[n]$: the constant is $4/3$](to_review_astra/2603.02786__00__AP-packing-all-differences-constant-4-3-prime-blocks__note.pdf) | [Conjecture 1 of Alon, Dębski, Grytczuk and Przybyło](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2603.02786__00/) | — |
| [Monochromatic subset sums: $c_r=b_0^{\,r-1}/(2r)$ for every $r\ge 2$](to_review_astra/2105.15195__00__conlon-fox-pham-conjecture-10-constant-for-all-r__note.pdf) | [Conjecture 10 of Conlon, Fox and Pham](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2105.15195__00/) | — |

Where a "Rocq proof" is linked, the result has also been formalised in the
companion repository
[LLM4Rocq/graph-theory-rocq](https://github.com/LLM4Rocq/graph-theory-rocq),
checked against a source-verified formal statement with no added axioms; that
certifies the formal proposition, not its faithfulness to the paper's question,
so those notes still want a human reader.

Four further confirmed results that resolve part of the problem posed, rather
than all of it, will be added in a separate section. The full index of each
batch, with source-paper links and generation details, is in
[`to_review/`](to_review/README.md) and [`to_review_astra/`](to_review_astra/README.md).

## How these were produced

Two campaigns attacked the catalogue with one API call per problem, the model
asked for a proof, a counterexample, or an honest account of partial progress.

| campaign | model | attacks | claimed proofs or counterexamples | refereed | survived |
|:--|:--|--:|--:|--:|--:|
| August–September 2026 | GPT-5.6 Sol | 633 | 77 | 77, by Claude Fable | 16 notes |
| September 2026 | GPT-6 Astra | 563 | 45 | 31 flagged publishable, by Claude Opus | 20 notes |

Each claim was refereed by an independent agent told to assume the writeup
wrong: re-derive every step, fetch and check every cited theorem, brute-force
every finite construction, and search for prior art. The protocol and every
report are in [`verification/`](verification/) and
[`verification_astra/`](verification_astra/); a summary of what each pass found
is in [`verification/SUMMARY.md`](verification/SUMMARY.md) and
[`verification_astra/SUMMARY.md`](verification_astra/SUMMARY.md). The
recurring defect was not broken mathematics but missing attribution: several
load-bearing lemmas turned out to be existing named theorems, now cited in the
notes. Claims the referee found already published are excluded from the tables
above; the second campaign lost priority on six results by margins of two
months to four days, twice to papers whose own proofs were produced by a
language model.

The raw material for every attempt, including the ones that went nowhere, is
in [`attacks/`](attacks/), [`attacks_opg/`](attacks_opg/),
[`attacks_arxiv_astra/`](attacks_arxiv_astra/) and
[`attacks_retry/`](attacks_retry/), indexed in [`RESULTS.md`](RESULTS.md),
[`RESULTS_OPG.md`](RESULTS_OPG.md), [`RESULTS_ARXIV_ASTRA.md`](RESULTS_ARXIV_ASTRA.md)
and [`RESULTS_RETRY.md`](RESULTS_RETRY.md).

## Details

Methodology, repository layout and setup, for anyone who wants to reproduce or
extend the campaigns.

<details>
<summary><strong>Method</strong></summary>

- **Queues.** The original Sol campaign attacked easiest-first open/partial
  arXiv records from Lelarge's difficulty ranking, plus six questions restored
  after
  [catalog extraction fixes](https://github.com/mlelarge/graph-conjectures/pull/3).
  The Astra campaign then covered all 227 OpenProblemGarden entries, but not
  the full arXiv queue: it attacked 58 arXiv records the first campaign had not
  reached and made 181 selected arXiv retries. A further 97 retries came from
  OpenProblemGarden, for 278 second attempts in total.
- **Prompt.** Catalog page + extracted statement JSON + arXiv abstract where
  applicable.
- **Attack models.** [GPT-5.6 Sol and GPT-6 Astra](https://openai.com), one
  Responses API call per attempt with effort `max`, `reasoning.mode=pro`, and
  `max_output_tokens=128000`. Astra ran on the flex service tier.
- **Review model.** The 77 claimed proofs/counterexamples were adversarially
  reviewed with [Claude Fable](https://www.anthropic.com/claude/fable); see
  [`verification/`](verification/) for the review protocol and reports. The
  Astra claims are not yet reviewed.
- **Budget.** Each campaign has a hard euro cap and a per-call USD reserve so
  parallel jobs cannot overspend. The Astra legs shared one €600 wallet and
  spent €584.88 ($564.66) across 563 calls. Prepaid EUR→USD accounting is
  taken from the API wallet rather than a market FX rate.
- **Artifact.** Each attempt stores `prompt.md`, `output.md`, `verdict.json`,
  `usage.json`, and `meta.json` in its campaign directory.

Each call is capped at 128k output tokens. The preflight reserve is $3.50 for
Sol and $8.00 for Astra because `mode=pro` can do extra internal work.

</details>

<details>
<summary><strong>Layout</strong></summary>

```
attack.py          # queue / run / sweep / summary
catalog/           # snapshot of the Lelarge catalog (not authored here)
attacks/<id>/      # one directory per attempted record
RESULTS.md         # generated index of verdicts
attacks_opg/        # Astra OpenProblemGarden first pass
attacks_arxiv_astra/# Astra arXiv records not reached by Sol
attacks_retry/      # Astra second attempts across both sources
RESULTS_*.md        # generated indexes for the Astra legs
to_review_astra/    # unrefereed Astra candidate-writeup PDFs
verification/      # adversarial reviews of claimed proofs/counterexamples
scripts/           # commit loop and campaign ops
```

</details>

<details>
<summary><strong>Setup</strong></summary>

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

</details>

## How to cite

If you use these results, please cite this repository:

```bibtex
@dataset{lelarge2026aiassisted,
  author    = {Marc Lelarge and Emanuele Natale and Édouard Oyallon and
               Aurora Rossi and Laurent Viennot},
  title     = {AI-Assisted Proofs for Open Problems in Graph Theory},
  year      = {2026},
  version   = {1.0.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22706597},
  url       = {https://doi.org/10.5281/zenodo.22706597}
}
```

Machine-readable citation metadata are available in [`CITATION.cff`](CITATION.cff).

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
