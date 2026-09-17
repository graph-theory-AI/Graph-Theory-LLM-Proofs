# Adversarial verification of the gpt-6-astra campaign's publishable claims

Generated 2026-09-17T13:00:45Z from the per-target reports in this directory. See `REFEREE_PROMPT.md` for the review protocol, `verdicts.json` for machine-readable verdicts, `targets.json` for the claim each report answers, and `scripts/<id>/` for the reproducible computational checks.

The gpt-6-astra campaign produced 31 claims that the model itself flagged `would_publish: true`, across `attacks_opg/`, `attacks_arxiv_astra/` and `attacks_retry/`. Each is reviewed here by an independent adversarial referee agent instructed to assume the writeup wrong, re-derive every step, verify every citation against fetched sources, and brute-force every finite construction. **26 of 31 reviews are complete.**

A formal verdict is not a result. `CONFIRMED` means one LLM referee could not break one LLM writeup; novelty was checked only against what could be found online, and several reports flag that a load-bearing lemma turned out to be an existing named theorem. Human review is still wanted.

## Verdict counts

| review verdict | n | share |
| --- | ---: | ---: |
| CONFIRMED | 11 | 42% |
| MINOR_GAPS | 9 | 35% |
| ALREADY_KNOWN | 6 | 23% |
| **total** | **26** | |

## By model's claimed verdict

| | CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---:
| proved | 2 | 6 | 0 | 0 | 5 | 13 |
| disproved | 7 | 1 | 0 | 0 | 1 | 9 |

## By model's claimed confidence

| | CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---:
| high | 11 | 8 | 0 | 0 | 6 | 25 |
| medium | 0 | 1 | 0 | 0 | 0 | 1 |

## By model's would_publish flag

| | CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---:
| True | 11 | 9 | 0 | 0 | 6 | 26 |
| False | 0 | 0 | 0 | 0 | 0 | 0 |

## Headline reading

- **11 claims fully CONFIRMED** (correct, fairly interpreted, apparently new), plus 9 MINOR_GAPS (correct modulo routine repairs). Of the model's 26 would_publish claims, 11 were fully confirmed.
- **Every FATAL_ERROR is an interpretation failure, not a computational error**: all 14 refute catalog transcription artifacts (lost overlines, > vs ≥, dropped hypotheses, inverted inequalities) or degenerate literal readings (p=1, p=2, K₁, tiny spheres); the internal mathematics was verified correct in every one.
- **The ALREADY_KNOWN pile (26) indicts catalog freshness more than the model**: most were scooped by 2024–2026 papers the 2026-05 auto-review missed or misjudged, several by mere weeks; a few statements were already settled inside the source papers themselves.

## Confirmed claims (correct and apparently new)

- `1812.09215__00` (disproved) **(would_publish)** — The counting argument is correct as written and I could not break it — every k-local Dictator-to-XOR bijection satisfies n <= 1+(k-1)+...+(k-1)^{D-1}, so Lip(phi^-1) >= 1 + log n/log k and the answer to Johnston-Scott's question is "no"; the matching construction in Section 3, however, is Rao-Shinkar's tree construction (arXiv:1501.03016, Theorem 2 and the generalisation remark) reproduced without attribution.
- `1904.02595__00` (proved) **(would_publish)** — Every step re-derived and every load-bearing inequality independently verified by exhaustive computation; the rank-refined social bound t+2rho(A) <= 2^n and the weighted rank-defect inequality alpha_w - W(A) >= 2^n - 2rho(A) are both correct and tight, and together they do prove Alon-Defant Conjecture 1.2.
- `1912.01570__00` (disproved) **(would_publish)** — The 12-vertex counterexample is real — exhaustive enumeration of all 32 planar embeddings gives fp = 2 while brute force gives fvs = 5, so Conjecture 2 (= Conjecture 14 of the published EJC version) is false as stated, and every step of the writeup's general-family argument checks out.
- `2008.03587__00` (disproved) **(would_publish)** — The explicit 59-vertex cactus works exactly as claimed — an independent exact game solver gives z(G) = 3 and z(H) = 2 with (v0, v11) the unique winning pair on H — so Question 4.1 of arXiv:2008.03587 is genuinely disproved.
- `2106.03261__00` (partial) **(would_publish)** — The construction is correct and genuinely disproves countability of the Petersen graph in the exact sense of Conlon-Fox-Sudakov-Zhao Definition 1.3 (which I retrieved verbatim); every step checks out, the load-bearing forced-orthogonality Lemma 1 was verified symbolically and exhaustively over PG(2,5) and PG(2,7), and the twisted/untwisted canonical-copy counts (0 vs 95/436/930/2930/4337 at q=101..191) confirm the mechanism -- but this settles only the Petersen half of Open Problem 2.17, not the catalog's main characterization question, and it duplicates the result already confirmed for the sibling target 2106.03261__01.
- `2106.03261__01` (partial) **(would_publish)** — The construction is correct and does disprove countability of the Petersen graph in the exact sense of Conlon-Fox-Sudakov-Zhao Definition 1.3; every step checks out, the key forced-orthogonality lemma (a polarity form of Desargues' theorem) was verified exhaustively by computer, and the question is still listed as open in Conlon's August 2026 survey.
- `2506.08810__03` (disproved) **(would_publish)** — The five-vertex tournament C3[TT2,TT2,1] really is a counterexample to Conjecture 24 of arXiv:2506.08810 — every step checks out, the two finite engines of the proof are verified by complete enumeration, and the interpretation matches the paper's own definitions verbatim.
- `2507.10840__01` (proved) **(would_publish)** — The odd-polygon-plus-central-cluster construction is correct and gives pi(A) >= 3n/4 - O(sqrt n), affirmatively answering Problem 9 of arXiv:2507.10840; exact-arithmetic ILP confirms pi = 4, 5, 6 for n = 6, 8, 10 against the trivial bounds 3, 4, 5.
- `covering_powers_of_cycles_with_equivalence_subgraphs` (disproved) **(would_publish)** — The construction and the rank lower bound are both correct and verified by brute force (eq(C_8^3)=eq(C_12^3)=3, eq(C_10^4)=4), so eq(C_n^k)=Theta(log k) and the Omega(k) conjecture is genuinely disproved — but the lower-bound half is a rediscovery of Alon (1986) Thm 1.1/Cor 1.2, and the source literature it contradicts (West's REGS page) contains a false assertion "eq(C_n^k)=k+1 when (k+1)|n" that Alon's own 1986 corollary already refutes.
- `geodesic_cycles_and_tuttes_theorem` (disproved) **(would_publish)** — The eight-vertex Kleetope of K4 really is a counterexample to Georgakopoulos–Sprüssel Problem 3 — every step of the writeup checks out, and an exact QF_LRA decision procedure (z3) proves UNSAT, i.e. no positive edge-length assignment on this graph makes all geodesic cycles peripheral.
- `melnikovs_valency_variety_problem` (disproved) **(would_publish)** — The 37-vertex graph was rebuilt from the prose and verified exactly (w=30, chi=3, RHS=3), the minimality proof checks out line by line and is corroborated by an independent mechanisation, so the problem is disproved as literally stated — but the counterexample lives entirely on the degenerate isolated vertex, and the min-degree->=1 version of Melnikov's question is untouched and remains open.

## Broken claims (FATAL_ERROR / MAJOR_GAP)


## Correct but already known

- `2510.11311__04` (disproved) — The proof is correct and I verified it by exhaustive/MILP search on D_2 and D_3, but it is Theorem 1.3 of Lei, Wang, Xu and Yang, arXiv:2609.14368 (13 Sep 2026) — the same layered Eulerian construction with the same parameters, posted four days before this attack ran.
- `2603.02786__01` (proved) — The proof is correct as written (every step re-derived, Lemma 2 verified exhaustively by computer), but Conjecture 4 had already been proved ten days earlier by Hou, Liu and Zhao, arXiv:2609.07487 (7 Sep 2026), Theorem 1.2, by a different (lattice-covering) route.
- `2603.02786__04` (proved) — The proof is, as far as I can check, correct and complete, but Conjecture 7 was already solved — with the same random-permutation/composition fractional-packing mechanism — by Mao, Wang, Wei and Yang, arXiv:2607.06113 (7 July 2026), two months before this attack ran.
- `finding_k_edge_outerplanar_graph_embeddings` (proved) — The SPQR dynamic program is, as far as I could check, correct — every recurrence (S, P, Q, R, the two-arm P-node scheduling DP, the block-cut gluing lemma) reproduces brute force on thousands of small instances — but the theorem was already published two months earlier as arXiv:2607.08110 (H. Yu, 9 July 2026), which resolves Bentz's question by a different route.
- `imbalance_conjecture` (proved) — The proof is mathematically correct in every step I could check, but the identical theorem and the identical load-bearing "capacity"/truncated-tail lemma were posted to arXiv as 2608.09191 (Schreib & Yavari, v1 10 Aug 2026, v2 17 Aug 2026), five weeks before this attack ran.
- `three_chromatic_0_2_graphs` (proved) — The proof is correct — I could not break any step, and exhaustive enumeration of all (0,2)-graphs on at most 9 vertices (all graphs, 63 of them), all connected ones up to 14 vertices, and 500+ cube-like (0,2)-graphs up to 64 vertices found chi in {1,2,4} only and confirmed the load-bearing lemma every time — but the identical theorem, with the same two-lemma architecture (unique-4-cycle matching plus "square-closed edge label is a gradient" via a divergence argument), was posted to arXiv as 2607.10125 (Christopher Williamson, 11 July 2026), two months before this attack.

## Full table

| id | claimed | conf. | publish? | review verdict | interp. ok | refs ok | code run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`1602.05184__00`](1602.05184__00.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`1812.09215__00`](1812.09215__00.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`1904.02595__00`](1904.02595__00.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`1912.01570__00`](1912.01570__00.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`2008.03587__00`](2008.03587__00.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`2105.15195__00`](2105.15195__00.md) | proved | high | yes | MINOR_GAPS | y | n | y |
| [`2106.03261__00`](2106.03261__00.md) | partial | high | yes | CONFIRMED | y | y | y |
| [`2106.03261__01`](2106.03261__01.md) | partial | high | yes | CONFIRMED | y | y | y |
| [`2207.13651__00`](2207.13651__00.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`2211.01032__03`](2211.01032__03.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`2304.03567__03`](2304.03567__03.md) | partial | high | yes | MINOR_GAPS | y | y | y |
| [`2506.08810__03`](2506.08810__03.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`2507.10840__01`](2507.10840__01.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`2510.11311__04`](2510.11311__04.md) | disproved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2603.02786__01`](2603.02786__01.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2603.02786__04`](2603.02786__04.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`a_generalization_of_vizings_theorem`](a_generalization_of_vizings_theorem.md) | disproved | high | yes | MINOR_GAPS | y | y | y |
| [`chromatic_number_of_random_lifts_of_complete_graphs`](chromatic_number_of_random_lifts_of_complete_graphs.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`covering_powers_of_cycles_with_equivalence_subgraphs`](covering_powers_of_cycles_with_equivalence_subgraphs.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`finding_k_edge_outerplanar_graph_embeddings`](finding_k_edge_outerplanar_graph_embeddings.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`geodesic_cycles_and_tuttes_theorem`](geodesic_cycles_and_tuttes_theorem.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`imbalance_conjecture`](imbalance_conjecture.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`melnikovs_valency_variety_problem`](melnikovs_valency_variety_problem.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`mixing_circular_colourings_0`](mixing_circular_colourings_0.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`random_stable_roommates`](random_stable_roommates.md) | partial | medium | yes | MINOR_GAPS | y | y | y |
| [`three_chromatic_0_2_graphs`](three_chromatic_0_2_graphs.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |

