# Catalog issues for Marc Lelarge

Findings from Graph-Theory-Auto against
[mlelarge.github.io/graph-conjectures](https://mlelarge.github.io/graph-conjectures)
(data snapshot of `mlelarge/graph-conjectures`: `data/arxiv_conjectures.json`, 762 records).

We only list **severe** defects: the official statement block is empty, a
placeholder, or the displayed math is cut off. We do **not** list the many
records whose extractor notes say “PDF source — math may be garbled” when the
statement itself is still a complete sentence.

Confirmed live on the public site on 2026-08-30.

## How we noticed

The first Sol attack in this repo targeted the ranking’s “easiest” open
record, [`2309.04460__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2309.04460__00/).
The catalog page’s statement is the placeholder

> [Full statement not available in the provided paper content excerpt.]

Sol (max, pro) correctly returned `ill_posed` and we spent €0.04 on that
call. Subsequent `--next` attacks now skip this class without an API call.

A scan of all 762 arXiv-mined records then found **18** of the same kind.

## A. Official statement missing (empty or placeholder)

These are the ones that cannot be attacked as stated. Several have the
**review** recover a usable statement while the official **Question /
Conjecture / Problem** block stays empty — so the site contradicts itself.

| id | live page | paper | official statement | review recovered a statement? |
| --- | --- | --- | --- | --- |
| `2309.04460__00` | [page](https://mlelarge.github.io/graph-conjectures/arxiv/2309.04460__00/) | [2309.04460](https://arxiv.org/abs/2309.04460) Alon–Bucić–Sauermann–Zakharov–Zamir, Question 10.1 | placeholder `[Full statement not available…]` | no (review also says HTML truncates before §10) |
| `2602.16333__03` | [page](https://mlelarge.github.io/graph-conjectures/arxiv/2602.16333__03/) | [2602.16333](https://arxiv.org/abs/2602.16333) Bucić–Hendrey–Mohar–Steiner–Yepremyan, Question 4.4 | **empty** | **yes** — review quotes: “Does there exist C>0 such that in any vertex transitive digraph, the length of a longest path is by at most a factor of C larger than the length of a longest directed cycle?” |
| `2208.10074__01` | [page](https://mlelarge.github.io/graph-conjectures/arxiv/2208.10074__01/) | [2208.10074](https://arxiv.org/abs/2208.10074) Dvořák–Wood, Open Problem 6 | placeholder `[Statement not available: only the theorem-environment label…]` | **yes** — review states the product-structure / `sep(G)∈O(n^{1-ε})` question in full, and even cites later progress (arXiv:2410.20333) |
| `2304.04690__00` | [page](https://mlelarge.github.io/graph-conjectures/arxiv/2304.04690__00/) | [2304.04690](https://arxiv.org/abs/2304.04690) Aboulker–Aubian–Charbit, §9 (2-extremal digraphs) | placeholder `[Statement unavailable — Section 9 content absent from PDF extraction]` | no on the live page. The in-repo file `ABOULKER_CONJECTURES_RANKED.md` already restored the TeX statement (“A digraph D is 2-extremal iff D ∈ H₂ …”) but that was **not** written back to `arxiv_conjectures.json` / the site |
| `2308.15387__01` | [page](https://mlelarge.github.io/graph-conjectures/arxiv/2308.15387__01/) | [2308.15387](https://arxiv.org/abs/2308.15387) The power of many colours, Question 4.3 | placeholder `[Verbatim statement not available…]` | only a paraphrase of the surrounding paragraph |
| `2211.14218__01` | [page](https://mlelarge.github.io/graph-conjectures/arxiv/2211.14218__01/) | [2211.14218](https://arxiv.org/abs/2211.14218) Shotgun assembly of random graphs | placeholder that *is* the inferred question (r-reconstructibility of G(n,p) for r∈{1,2}) | inferred, not verbatim |

## B. Statement truncated mid-formula

The official block is present but the mathematical conclusion is replaced by
an extractor comment. These should be re-extracted from the arXiv HTML/TeX.

| id | paper | what is missing |
| --- | --- | --- |
| `2603.02786__02` | [2603.02786](https://arxiv.org/abs/2603.02786) Conjecture 5 | asymptotic formula for `m_k(n)` |
| `2603.02786__03` | same, Conjecture 6 | both formulas for `M_k(n)` |
| `2603.02786__04` | same, Conjecture 7 | asymptotic as `k→∞` |
| `2604.09449__00` | [2604.09449](https://arxiv.org/abs/2604.09449) Conjecture 6.1 | RHS bound on `‖∑_{e∈M} h(e)‖_1` (notes guess `O(√k)`) |
| `2601.15245__02` | [2601.15245](https://arxiv.org/abs/2601.15245) Problem 6.2 | conclusion after the Δ-bound hypothesis |
| `2505.05339__00` | [2505.05339](https://arxiv.org/abs/2505.05339) Question 4.1 | condition on all edges of a cubic 3-edge-colourable graph |
| `2505.05339__01` | same, Question 4.2 | same for `d`-regular, `d≥4` |
| `2401.00359__00` | [2401.00359](https://arxiv.org/abs/2401.00359) Conjecture 6.1 | bound after `d₁(H)=d` |
| `2401.00359__01` | same, Conjecture 6.2 | bound for k-uniform k-partite H |
| `2310.04265__03` | [2310.04265](https://arxiv.org/abs/2310.04265) Conjecture 3.13 | ends at “such that:” |
| `2310.04265__04` | same, Conjecture 3.16 | ends at “such:” |
| `2003.01846__00` | [2003.01846](https://arxiv.org/abs/2003.01846) informal (outerplanar strongly perfect) | truncated in source |

## Suggested fixes (on the catalog repo)

1. Re-extract the 18 records above from arXiv HTML, falling back to the `.tex`
   source when HTML truncates (this is exactly what happened for
   `2304.04690` §9 and `2309.04460` §10).
2. When the *review* later recovers a verbatim statement (as for
   `2602.16333__03` and `2208.10074__01`), write it back into
   `statement_text` so the official block matches the review.
3. Do not rank placeholder records as “open / tier 1”.
   `2309.04460__00` is currently the easiest row in
   `ARXIV_OPEN_DIFFICULTY_RANKING.md`.
4. Optional: a CI check that fails if `statement_text` is empty or matches
   `Full statement not available|Statement unavailable|truncated in source`.

Machine-readable copy of this list: `catalog/issues_severe.json`.
Live log of issues hit during attacks: `catalog/issues.jsonl`.
