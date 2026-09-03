# Adversarial verification of the 77 claimed proofs/disproofs

Generated 2026-09-03T00:34:38Z from the per-target reports in this directory (see `REFEREE_PROMPT.md` for the review protocol; `verdicts.json` for machine-readable verdicts; `scripts/<id>/` for reproducible computational checks).

Each of the 77 `proved`/`disproved` self-reports in `../attacks/` was reviewed by an independent adversarial referee agent (model `claude-fable-5`) instructed to assume the writeup wrong, re-derive every step, verify every citation against fetched sources, and brute-force every finite construction.

## Verdict counts

| review verdict | n | share |
| --- | ---: | ---: |
| CONFIRMED | 25 | 32% |
| MINOR_GAPS | 9 | 12% |
| MAJOR_GAP | 3 | 4% |
| FATAL_ERROR | 14 | 18% |
| ALREADY_KNOWN | 26 | 34% |
| **total** | **77** | |

## By model's claimed verdict

| | CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---:
| proved | 10 | 8 | 0 | 0 | 13 | 31 |
| disproved | 15 | 1 | 3 | 14 | 13 | 46 |

## By model's claimed confidence

| | CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---:
| high | 23 | 5 | 2 | 14 | 25 | 69 |
| medium | 2 | 4 | 1 | 0 | 1 | 8 |

## By model's would_publish flag

| | CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---:
| True | 12 | 4 | 0 | 0 | 10 | 26 |
| False | 13 | 5 | 3 | 14 | 16 | 51 |

## Headline reading

- **25 claims fully CONFIRMED** (correct, fairly interpreted, apparently new), plus 9 MINOR_GAPS (correct modulo routine repairs). Of the model's 26 would_publish claims, 12 were fully confirmed.
- **Every FATAL_ERROR is an interpretation failure, not a computational error**: all 14 refute catalog transcription artifacts (lost overlines, > vs ≥, dropped hypotheses, inverted inequalities) or degenerate literal readings (p=1, p=2, K₁, tiny spheres); the internal mathematics was verified correct in every one.
- **The ALREADY_KNOWN pile (26) indicts catalog freshness more than the model**: most were scooped by 2024–2026 papers the 2026-05 auto-review missed or misjudged, several by mere weeks; a few statements were already settled inside the source papers themselves.

## Confirmed claims (correct and apparently new)

- `1601.01886__00` (proved) — The construction and all proofs check out (computationally verified up to |V|=764); the factor 2 in Lemma 4 is indeed unavoidable, with the exact optimum being height 2k-1 in the paper's edge-counting height convention (the writeup itself proves and flags this 2k vs 2k-1 convention point).
- `1611.03196__03` (proved) **(would_publish)** — The elementary proof of Conjecture 1.15 with c(m)=32(m+1)^3 (Koenig + Caratheodory + Stromquist-Woodall interval splitting + alternating-cycle interpolation) survives full step-by-step re-derivation, its combinatorial core and the entire pipeline verify computationally, and no prior resolution exists in the literature.
- `1702.01094__01` (disproved) **(would_publish)** — The writeup's two-lemma construction (nested-upset stable-set covers from a coloring of the distance-two graph, applied to high-girth high-chromatic random graphs) is correct in every step and genuinely answers the Scott-Seymour question in the negative for every s >= 3.
- `1704.00125__01` (disproved) — The counterexample (bipartite graphs of maximum degree 20) is mathematically correct and verified end-to-end, and it does refute the universal statement Dvořák wrote, but the refutation is assembled from textbook facts and kills only the "for example" formalization of a deliberately hedged prose question, not the underlying research program.
- `1809.05439__00` (disproved) — The 23-vertex two-wheel construction is a correct, computationally verified counterexample to the concrete conjectured statement (subsets of {1..9}, all vertices >= 3 colors, x gets 5) under the intended triangle-free-planar quantifiers of Theorem 5.
- `1812.02420__02` (proved) **(would_publish)** — The digon-matching two-layer reduction from 2-dichromatic colourability is correct as written; every step re-derives cleanly, both cited results check out against the sources, and brute-force LP computation on 125 instances (including bidirected K3 and the digon-free Paley tournament ST7) confirms chi_f(R(D)) <= 2 iff chi(D) <= 2, so NP-completeness of the p = 2 case of Problem 3.21 is established.
- `1812.02420__03` (disproved) **(would_publish)** — The writeup's complete classification (a directed Kneser graph K(k,b) with the Problem 5.40 property exists iff b<=2 or k<=b+1) is correct; every step checks out, the digon convention matches the source paper exactly, and both the (5,3) impossibility and the positive constructions were independently verified by exhaustive computation.
- `1902.06473__00` (proved) — The writeup correctly proves ln e(P) <= QLB(P) <= log2 e(P) for all finite posets via Stanley's rank log-concavity, hence LB(P)/2 <= QLB(P) <= LB(P)/ln 2, resolving the source paper's conjecture with explicit constants; every step re-derived, all references verified against the arXiv TeX sources, and all claims confirmed computationally on every poset with at most 6 elements plus random posets on 7-8 elements.
- `1902.10878__01` (disproved) **(would_publish)** — The explicit 42-vertex biconstrained triple checks out exactly (psi(2/7,5/7) <= 23/28), the rigidity proof of psi(5/7,2/7) = 6/7 is valid step by step with its finite core machine-verified, and 23/28 < 6/7 genuinely refutes psi-symmetry as posed by Chudnovsky-Hompe-Scott-Seymour-Spirkl.
- `1904.12273__01` (disproved) — The four-vertex counterexample is correct and computationally verified, and it even lives inside a "candidate" graph in the source paper's sense, so the heavy path extension of Chudnovsky-Scott-Seymour fails for every threshold ell >= 6 under any reasonable reading.
- `1907.06019__01` (proved) — The characterization of extremal mutually annihilating pairs as common v-stars is correct; every step checks out, the set-system equality lemma agrees with Matsumoto-Tokushige 1989 and with exhaustive computation, and the rigidity lemma was confirmed by exact nullspace computations.
- `2103.15175__00` (proved) **(would_publish)** — The writeup's vertex-by-vertex greedy/union-bound "separation lemma" is correct and, combined with the classical product-coloring upper bound, validly proves R_ell(H_s,k) = s^k + 1, matching the Fox–He–Luo–Xu conjecture; every step checks out and exhaustive computation confirms the case s=2, k=2.
- `2204.10119__01` (disproved) — The 28-vertex 4-clique amalgam of two apex graphs is fully machine-verified (degrees 6^22 7^4 8^2, both pieces apex-over-planar with certified embeddings) and the two supporting lemmas are sound textbook facts, so the graph has no K6 minor and genuinely refutes the parenthetical conjecture.
- `2208.06858__01` (disproved) **(would_publish)** — The block-tribes construction is correct under the source paper's exact definitions and disproves Conjecture 2.2 by showing p_monotone(t) = 1/2 for every t; every step was re-derived by hand and verified by exhaustive and exact computation.
- `2209.09107__00` (disproved) — The disproof is correct — Question 6.1 as actually printed (no floor) forces on C_3 an Eulerian orientation with an odd number of arcs, which is never Alon-Tarsi (verified exhaustively by computer); only the unfloored statement falls, and Conjecture 1.1 itself is untouched.
- `2304.03567__04` (disproved) — The diamond-chain construction is correct and machine-verified; under the source paper's own verbatim definition of forward cover it refutes Conjecture 1 of arXiv:2304.03567 with an n/3 lower bound.
- `2307.15512__00` (disproved) — The clique-plus-random-attachment construction is sound — it yields connected k-graphs with k = Theta(sqrt(n)) and c(H) = Omega(sqrt(n/k) log n), refuting the uniform O(sqrt(n/k)) bound of Conjecture 1.4; every step re-derived by hand and validated by machine.
- `2310.04265__09` (disproved) **(would_publish)** — The explicit circulant family T_n = Cay(Z_{2n+1}, {1,...,n-1,n+1}) is verified (exhaustively for 7-15 vertices, by SAT up to 61 vertices, structurally to 121 vertices) to have clique number 3 with every proper subtournament of clique number at most 2, so Question 5.9 is answered negatively at k=3; every proof step checks out and no prior unconditional disproof was found in the literature.
- `2310.04265__11` (disproved) — The counterexample is correct — a hereditary class of oriented graphs with dic = diomega <= 2 whose substitution closure contains digraphs with diomega = 2 and unbounded dichromatic number, refuting Conjecture 6.1 as stated; every lemma checks out by hand and the base instances were verified exhaustively by computer.
- `2401.00299__02` (proved) **(would_publish)** — The four-layer lifting from f_{0,2}(d-2) to f_2(d) is correct in every detail, matches the exact statements of Propositions 1.6 and 1.10 in the source TeX, and machine verification of the construction (810,000 lifted partitions of Q_6, plus exhaustive censuses of f_2(d) for d <= 5) found no fault, so the conjectured asymptotic log f_2(d) = (1+o(1)) 2^{d-1} log d is established modulo the source paper's own published propositions.
- `2405.03455__00` (proved) **(would_publish)** — The writeup's elementary alteration/transfer argument bootstrapping the source paper's own diagonal bound ES_n(n) < n^2 2^{n+C sqrt(n log n)} to a uniform linear-in-l upper bound ES_l(n) <= l 2^{n+C_1 sqrt(n log n)} is correct in every step, matches the linear lower bound, and does not appear in the indexed literature (the only citing paper, Furukawa arXiv:2501.03645, obtains a strictly weaker l * 4^{n+O(sqrt(n log n))}).
- `2408.02400__00` (proved) **(would_publish)** — The 13-vertex circulant-complement seed and the Mycielski cochromatic lemma both check out completely (seed and the k=5 iterate verified by brute force, lemma verified line-by-line and tested exhaustively on all graphs up to 5 vertices), so Problem 1.5 of arXiv:2408.02400 is answered affirmatively.
- `2508.08870__00` (disproved) — The disproof is correct — two parallel arithmetic progressions give a noncollinear planar n-point set with at most (3/2)n-2 distinct distances in every norm, and the general-d variant caps the coefficient at d-1+1/(2(d-1)) < d, refuting Conjecture 1.5 of arXiv:2508.08870 as stated (in both v1 and v2) for every d >= 2 and every norm, not just generic ones.
- `2512.10438__00` (proved) **(would_publish)** — The (q,N)=(6,9) construction is correct and exhaustively machine-verified — p(T)=7 while f_{6,5}(9)=8 — so Problem 5.1 of arXiv:2512.10438 as literally stated is answered affirmatively.
- `2603.02786__03` (disproved) — The writeup's elementary weighted-core counting argument is correct and yields M_k(n) >= (6619/10800 - o(1)) nk^2/ln k for k -> infinity, k = o(n), genuinely refuting the constant 1/2 in the first clause of Conjecture 6 of arXiv:2603.02786 while remaining consistent with the paper's proven bounds.

## Broken claims (FATAL_ERROR / MAJOR_GAP)

- `1611.03196__00` (disproved, FATAL_ERROR) — The P_7 counterexample is arithmetically correct but only refutes a rounding artifact of the literal "integer b_i" wording; the intended Conjecture 1.6, as read and cited explicitly by Alishahi-Meunier (EJC 2017), was PROVED by them in 2017, so the "disproved" verdict is untenable.
- `1708.02370__00` (disproved, FATAL_ERROR) — The "counterexample" H = 2K_1 refutes only a transcription artifact — the paper's actual Conjecture 4 uses connected tree-depth ctd(H) (typeset as td with an overline, lost in PDF extraction), and since ctd(2K_1) = 2 the real conjecture holds comfortably for 2K_1 and remains open.
- `1708.08486__01` (disproved, FATAL_ERROR) — Every internal step of the writeup is correct and computationally confirmed, but it "disproves" only the degenerate p=2 case that the source authors demonstrably never intended (their own adjacent sentence and the odd-prime companion paper I exclude p=2), so the intended conjecture for the odd primes 3,5,7,11,13,17 remains untouched and the claimed disproof fails.
- `1710.10663__00` (disproved, FATAL_ERROR) — The writeup's mathematics is internally correct, but it "disproves" only a catalog transcription error — the source paper's actual constant is c_L = 2^{-L}⌊L/2⌋·C(L-1,⌊L/2⌋), giving c_2 = 1/4, so the intended conjecture is untouched (its L=2 instance is proved true in the very same paper) and remains open.
- `1710.11281__02` (disproved, MAJOR_GAP) — The tiny-sphere/antipodal-shadowing argument is mathematically correct and computationally verified, but it refutes only a degenerate literal reading in which "the cops catch the robber" holds vacuously because the surface's diameter (1/4) is below the capture radius 1/2 — Mohar's intended question remains open.
- `1806.09726__00` (disproved, FATAL_ERROR) — The writeup's mathematics (r̃_rand(4,n) = Θ(n²)) is correct but refutes only a mis-read literal statement; the source paper's own Theorem 13 and Conjecture 9 already give exponent 2 at m=4, so the intended Conjecture 7 (o(1) as m→∞) is untouched and remains open.
- `1811.08750__00` (disproved, MAJOR_GAP) — The T=K1 counterexample is mathematically correct against the literal wording (which I verified matches the paper) but only exploits a degenerate loophole (e(T)=0 / empty family) that no reasonable author would accept as refuting Conjecture 1.8; the intended conjecture remains open, while the writeup's separate k=m+1 hardness proof checks out and in fact answers an open question from Section 6 of the paper.
- `2004.07457__01` (disproved, FATAL_ERROR) — The K_2 "counterexample" only exploits the degenerate wording artifact log(1)=0 at Delta_A=Delta_B=1; every internal step is correct, but the claimed disproof is a strawman refutation that leaves the intended (asymptotic) Conjecture 7 — the actual open problem — untouched, as the writeup itself concedes.
- `2008.03587__01` (disproved, FATAL_ERROR) — The paper's actual Question 4.2 (verified in the arXiv TeX source, main.tex line 432) reads "z(G'_k) >= z(G)+1", so the writeup's K2 "counterexample" refutes only a garbled catalog transcription (">") and in fact satisfies — indeed supports — the real open question, which remains open.
- `2009.03418__00` (disproved, MAJOR_GAP) — Every internal step of the writeup is correct and computationally verified (cr(M_{7,t}) = 6, 4, 3 for t = 1, 2, 3), but it refutes only the catalog's over-generalized extraction with k = floor(n/2) — a clause not in Mohar's paper, where Conjecture 5 lives in the context n = 2k even — so the intended conjecture remains open and is not disproved.
- `2207.07775__02` (disproved, FATAL_ERROR) — The writeup's counterexample refutes a strawman reading of "(k,t)-generalized lollipop"; under the paper's actual definition (a t-vertex graph containing a K_k whose deletion is a forest) the construction is not in the conjecture's family at all — it contains no K_4 — so Conjecture 5.4 is untouched and remains open.
- `2211.01032__00` (disproved, FATAL_ERROR) — The isolated-K2 "counterexample" is arithmetically correct but counts faces with a componentwise convention that the source paper explicitly rejects — arXiv:2211.01032 defines F(n,p) = F(M) - c(M) + 1, under which every tree component (isolated K2 included) contributes exactly zero, so Conjecture 1.13 is not disproved.
- `2211.01032__01` (disproved, FATAL_ERROR) — The refutation works only under an additive-over-components face count, but the source paper explicitly defines the number of faces of a disconnected embedding as F(M) - c(M) + 1 (so every tree component, in particular every isolated K_2, contributes exactly zero), which annihilates the entire argument; Conjecture 9.1 remains open.
- `2307.15048__00` (disproved, FATAL_ERROR) — The writeup "disproves" only the degenerate p=1 endpoint (G(n,0) is edgeless, chi_DP = 1), a transcription-level artifact of the paper's quantifier "positive p <= 1"; this is textbook interpretation gaming and leaves the intended conjecture (0 < p < 1) completely untouched, as the writeup itself concedes.
- `2308.15721__00` (disproved, FATAL_ERROR) — The writeup correctly refutes the catalog's mis-reconstructed statement, but the actual Conjecture 2 of arXiv:2308.15721 asserts chi_star <= 2td(H)-2 (an inequality, not equality with td(H)-1), and the K_{1,3} example satisfies it — the real open conjecture is untouched.
- `2409.18220__00` (disproved, FATAL_ERROR) — The K_4 "counterexample" is arithmetically correct but refutes only a strawman n>=4 reading that the source authors demonstrably never intended (their own paper computer-verifies s(G) >= n-1 for n <= 10 and notes trees have s = n-1), and the intended conjecture (n >= 5) is in fact TRUE, being an immediate corollary of the July 2026 Liu-Tang-Zhang proof of the full s(G) >= n-1 conjecture (arXiv:2607.18031) — so "disproved" is irreparably the wrong verdict.
- `2503.16882__00` (disproved, FATAL_ERROR) — All arithmetic in the writeup is correct and computationally verified, but the counterexample refutes only the catalog's mis-extracted P_n-comparator statement, while the paper's actual Conjecture 2 uses K_n as comparator and remains unrefuted (proven for p>=3, open at p=2), so the claimed "disproved" verdict does not apply to the real open problem.

## Correct but already known

- `1610.00239__00` (proved) — The writeup's self-contained proof of Alon-Klartag Conjecture 2.4 survives a full step-by-step and numerical check, but the conjecture was already confirmed in the literature by Vishesh Jain (arXiv:2608.13782, posted 2026-08-13, Remark (iii)) two and a half weeks before this attack was generated.
- `1709.09050__01` (proved) — The proof is correct (verified step-by-step and by exhaustive computation on all 86,356 connected outerplanar graphs with n <= 8), but the exact result was published in 2019 as Theorem 3.9 of Bonato, Breen, Brimkov, Carlson, English, Geneson, Hogben, Perry, Reinhart (arXiv:1903.10087, J. Combinatorics 13(1), 2022), which explicitly resolves this open problem from the Bonato-Mohar survey.
- `1802.03727__00` (proved) — The writeup's proof of Conjecture 1.3 verifies completely (every step valid, key construction confirmed by exhaustive computation), but the conjecture as stated already follows from published work — Kwan, Letzter, Sudakov and Tran (arXiv:1810.12144, Combinatorica 2020) proved Esperet–Kang–Thomassé's Conjecture 1.4, which the source paper itself states implies Conjecture 1.3 — although the writeup's quantitative strengthening and its chromatic-number route appear to be new.
- `1902.10878__00` (disproved) — The writeup's counterexample is mathematically correct, but the precise statement it refutes is the "wild conjecture" that the source paper itself already declares false and refutes with an explicit (13/27, 1/9) example in its introduction; the genuinely open problem (the correct characterisation of phi, "maybe something like it is true") is untouched.
- `1907.06019__00` (proved) — The writeup's proof of the Scott-Wilmer extremal characterization checks out step by step and computationally, but the result was already proved (over any field, and in a stronger Hilton-Milner form) by Bulavka, Gandini, and Woodroofe, arXiv:2406.17857 (June 2024), published in Trans. London Math. Soc. 12 (2025), e70022.
- `1909.11578__02` (disproved) — The disproof is mathematically correct — every step verified analytically and computationally — but the construction and its consequence were already essentially known (Ellis–Kalai–Narayanan arXiv:1702.02607 runs family; Keller–Lifshitz–Marcus arXiv:2307.01356 publish the lifted transitive-symmetric vector family of density exp(-O(k log k log n)) "following a strategy suggested in [EKNS19, Section 4]").
- `2004.07214__00` (proved) — The proof is mathematically correct and verified computationally, but its "main new observation" (Lemma 1) is literally Proposition 3.6 of Kang-Kwon-Strømme-Telle (TCS 2017), which together with Golovach et al. (Algorithmica 2018) already resolved Conjecture 7.1 before it was posed.
- `2009.12189__00` (disproved) — The disproof is mathematically correct and computationally confirmed (the 25-vertex Tutte dual has va_f = 33/16 > 2, with the claimed certificate va_f >= 88/43 verified exactly), but Conjecture 1.1 was already refuted by Naserasr, Pham, Pujol and Zhou (arXiv:2505.16808, May 2025) and is also refuted a fortiori by the August 2026 counterexamples to the Albertson-Berman conjecture.
- `2108.00991__00` (disproved) — The writeup's disproof of CFSW Conjecture 3 is fully correct (every count verified by brute force for k = 4..8), but the conjecture was already disproved, with strictly stronger bounds, by Huang, Yang and Chen (arXiv:2606.01996, 1 June 2026).
- `2111.00532__00` (proved) — The proof is internally valid but resolves only a misquoted weakening of Question 1.3 (the catalog dropped the linear requirement |X| >= eps*W); the weakened statement is the K_3 case of Erdos-Hajnal-Pach (Theorem 1.2 of the same paper), and the actual open question remains open.
- `2111.00532__01` (proved) — The proof is correct but proves exactly Theorem 1.2 of the source paper (the Erdős–Hajnal–Pach theorem, Geombinatorics 10 (2000), 64-68) — the catalog garbled the actual open question, which is the asymmetric strengthening |X| >= eps*W, |Y| >= eps*W^c, and that remains open.
- `2204.12330__00` (proved) — The proof that Sym_fin(Z) has finite twin-width and infinite uniform twin-width is correct in every step I checked, but the separation was established three weeks before this review in Kontogeorgiou-Miraftab, "Quasirandomness and Uniform Twin-Width" (arXiv:2608.10150, 10 Aug 2026), by the same quasirandomness route with the same D^{1/4} exponent.
- `2208.10074__00` (disproved) — The writeup's disproof of the literal (tree-depth) catalog statement is mathematically correct, but it is exactly Theorem 20 of the source paper itself (d = 2 case), which explicitly notes that the tree-depth strengthening of its Open Problem 6 is false; the actual open conjecture is about bounded tree-width and is untouched.
- `2306.04710__01` (proved) — The writeup's proof is correct in every step (all lemmas re-derived and computationally verified), and it resolves the open problem negatively for all (m, m', F); however, the load-bearing theorem — claw-free, directed-triangle-free oriented graphs of unbounded dichromatic number — was already proved by Aubian and Kuffner (arXiv:2602.08736, Feb 2026), from which the Delta(1,m,m') resolution follows immediately.
- `2308.15387__00` (disproved) — The "counterexample" is verbatim the source paper's own Proposition 3.1 (Liu-Morris-Prince 2007), it refutes only an evident slip in the conjecture's stated range (the paper's own Theorem 1.1 already contradicts the literal "1 <= s" endpoint), and the intended open question — whether f(n,r,s) = s^2 (log r)^{1-o(1)} n / r for log log r <~ s <= sqrt(r)/log r — is untouched.
- `2405.14795__00` (proved) — The writeup's second-moment proof of a single sharp threshold at mN/(2 log n!) + (2m-1)/6 survives detailed checking, but the same result (same constant, essentially the same method) was already established by Liu, Ma, Xiang and Yan, arXiv:2606.31376 (30 June 2026).
- `2410.13008__00` (disproved) — The 12-vertex counterexample is correct and fully verified by exhaustive computation (it even survives the unsigned reading of "winding number one"), but the conjecture was already disproved by Daniel Carter in early 2025 — Seymour's own revised paper (April 16, 2025, Princeton website) relabels 1.2 "False conjecture".
- `2503.23191__00` (disproved) — The counterexample is correct and computationally verified, but the identical observation was published by the source paper's own authors in arXiv:2503.23191v2 (1 Aug 2026), whose revised Question 5.1 (excluding "bouncing" paths) remains open.
- `2505.24100__00` (proved) — The writeup's proof that K_{t-1} □ C_{2t-3} answers Question 1.7 is correct and was verified computationally for k=3..8, but the question's affirmative answer has been in the literature since Tennenhouse (2016), as the source paper's own authors acknowledge in arXiv:2606.24763 (Theorem 1.5), and is also subsumed by Choi's arXiv:2608.24202 (Aug 2026).
- `2506.07264__01` (proved) — The writeup's proof is mathematically correct (every step verified, formulas confirmed computationally), but the conjecture was already proved — by essentially the same matching-polynomial/Coulson-integral argument — in Ning & Zeng, arXiv:2605.24668 (May 23, 2026).
- `2507.04254__00` (disproved) — The writeup's disproof of Conjecture 13 (a bipartite 0_k-graph with chi'_k >= 7k/6) is correct in every step and verified computationally, but the conjecture was already refuted in the literature in August 2026 (arXiv:2608.10687, Guo-Wu, with the stronger bound (4-2sqrt(2)+o(1))k, and arXiv:2608.02239, Liu-Xu-Yang, refuting the underlying BCK conjecture with bound ~3k/2).
- `2511.02892__03` (disproved) — The writeup's mathematics is entirely correct, but its "counterexample" is the triangular prism — the exception already flagged in the problem's own preamble (Lv–Li–Zhang 2022) — so it refutes only a strawman literal reading; the intended conjecture is untouched by it (and was later genuinely disproved by an 18-vertex non-prism example, arXiv:2607.23462, July 2026).
- `2512.17232__00` (disproved) — The 16-vertex counterexample is correct (every claim verified by brute force) and refutes Conjecture 6 of arXiv:2512.17232v1 at k=2, but this refutation was already in the literature (Albrechtsen–Huynh–Jacobs–Knappe–Wollan, SIAM J. Discrete Math. 2024, Lemma 5 with d=2), and the source authors themselves revised the conjecture to |Z| <= k in arXiv v2 (2026-09-01), explicitly citing that construction.
- `2512.17342__00` (disproved) — The writeup's 38-vertex cubic planar counterexample is fully verified by exhaustive computation (all 235,856 simple cycles checked, twice, by independent enumerations), so F(G,5) is indeed disconnected — but Problem 1.1 was already answered negatively by Theorem 3.4 of the source paper itself (arXiv:2512.17342, since v2, April 2026), as the prompt's own abstract announces.
- `2602.16333__00` (proved) — The writeup's proof is correct in every step (machine-verified down to brute force), but the conjecture was already resolved with the identical bound n/12 by Li and Methuku (arXiv:2607.05807, posted 2026-07-07), eight weeks before this attack ran on 2026-08-31.
- `2604.09449__00` (disproved) — The counterexample is mathematically correct and refutes the catalog's extracted statement, but that statement is the erroneous v1 form of Conjecture 6.1, which the authors had already corrected in arXiv:2604.09449v2 (2026-07-11); the currently-open colour-balanced conjecture is untouched.

## Full table

| id | claimed | conf. | publish? | review verdict | interp. ok | refs ok | code run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`1601.01886__00`](1601.01886__00.md) | proved | high | no | CONFIRMED | y | y | y |
| [`1610.00239__00`](1610.00239__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`1611.03196__00`](1611.03196__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`1611.03196__03`](1611.03196__03.md) | proved | medium | yes | CONFIRMED | y | y | y |
| [`1702.01094__01`](1702.01094__01.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`1704.00125__01`](1704.00125__01.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`1708.02370__00`](1708.02370__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`1708.08486__01`](1708.08486__01.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`1709.09050__01`](1709.09050__01.md) | proved | high | no | ALREADY_KNOWN | y | y | y |
| [`1710.10663__00`](1710.10663__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`1710.11281__02`](1710.11281__02.md) | disproved | medium | no | MAJOR_GAP | n | y | y |
| [`1802.03727__00`](1802.03727__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`1802.05582__00`](1802.05582__00.md) | proved | medium | no | MINOR_GAPS | y | y | y |
| [`1802.05582__01`](1802.05582__01.md) | proved | medium | no | MINOR_GAPS | y | y | y |
| [`1806.09726__00`](1806.09726__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`1809.05439__00`](1809.05439__00.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`1811.08750__00`](1811.08750__00.md) | disproved | high | no | MAJOR_GAP | n | y | y |
| [`1811.12650__00`](1811.12650__00.md) | proved | high | no | MINOR_GAPS | y | y | y |
| [`1812.02420__02`](1812.02420__02.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`1812.02420__03`](1812.02420__03.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`1902.06473__00`](1902.06473__00.md) | proved | medium | no | CONFIRMED | y | y | y |
| [`1902.10878__00`](1902.10878__00.md) | disproved | high | no | ALREADY_KNOWN | n | y | y |
| [`1902.10878__01`](1902.10878__01.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`1904.12273__01`](1904.12273__01.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`1907.06019__00`](1907.06019__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`1907.06019__01`](1907.06019__01.md) | proved | high | no | CONFIRMED | y | y | y |
| [`1909.11578__02`](1909.11578__02.md) | disproved | high | no | ALREADY_KNOWN | y | y | y |
| [`2001.09679__00`](2001.09679__00.md) | proved | medium | yes | MINOR_GAPS | y | y | y |
| [`2004.07214__00`](2004.07214__00.md) | proved | high | no | ALREADY_KNOWN | y | y | y |
| [`2004.07457__01`](2004.07457__01.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2005.09767__00`](2005.09767__00.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`2008.03587__01`](2008.03587__01.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2009.03418__00`](2009.03418__00.md) | disproved | high | no | MAJOR_GAP | n | y | y |
| [`2009.12189__00`](2009.12189__00.md) | disproved | high | no | ALREADY_KNOWN | y | y | y |
| [`2103.15175__00`](2103.15175__00.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`2106.14762__00`](2106.14762__00.md) | proved | high | no | MINOR_GAPS | y | y | y |
| [`2108.00991__00`](2108.00991__00.md) | disproved | high | no | ALREADY_KNOWN | y | y | y |
| [`2111.00532__00`](2111.00532__00.md) | proved | high | no | ALREADY_KNOWN | n | y | y |
| [`2111.00532__01`](2111.00532__01.md) | proved | high | no | ALREADY_KNOWN | n | y | y |
| [`2204.10119__01`](2204.10119__01.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2204.12330__00`](2204.12330__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2207.07775__02`](2207.07775__02.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2208.06858__01`](2208.06858__01.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`2208.10074__00`](2208.10074__00.md) | disproved | high | no | ALREADY_KNOWN | n | y | y |
| [`2209.09107__00`](2209.09107__00.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2211.01032__00`](2211.01032__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2211.01032__01`](2211.01032__01.md) | disproved | high | no | FATAL_ERROR | n | n | y |
| [`2211.01032__02`](2211.01032__02.md) | proved | high | yes | MINOR_GAPS | y | y | y |
| [`2304.03567__04`](2304.03567__04.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2306.04710__01`](2306.04710__01.md) | proved | high | no | ALREADY_KNOWN | y | y | y |
| [`2307.15048__00`](2307.15048__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2307.15512__00`](2307.15512__00.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2308.15387__00`](2308.15387__00.md) | disproved | high | no | ALREADY_KNOWN | n | y | y |
| [`2308.15721__00`](2308.15721__00.md) | disproved | high | no | FATAL_ERROR | n | n | y |
| [`2310.04265__09`](2310.04265__09.md) | disproved | high | yes | CONFIRMED | y | y | y |
| [`2310.04265__11`](2310.04265__11.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2312.13061__01`](2312.13061__01.md) | disproved | medium | no | MINOR_GAPS | y | n | y |
| [`2401.00299__02`](2401.00299__02.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`2405.03455__00`](2405.03455__00.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`2405.14795__00`](2405.14795__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2408.02400__00`](2408.02400__00.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`2409.18220__00`](2409.18220__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2410.13008__00`](2410.13008__00.md) | disproved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2503.16882__00`](2503.16882__00.md) | disproved | high | no | FATAL_ERROR | n | y | y |
| [`2503.23191__00`](2503.23191__00.md) | disproved | high | no | ALREADY_KNOWN | y | y | y |
| [`2505.24100__00`](2505.24100__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2505.24100__01`](2505.24100__01.md) | proved | high | yes | MINOR_GAPS | y | n | y |
| [`2506.07264__01`](2506.07264__01.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2507.04254__00`](2507.04254__00.md) | disproved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2508.08870__00`](2508.08870__00.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2511.02892__03`](2511.02892__03.md) | disproved | high | no | ALREADY_KNOWN | n | y | y |
| [`2512.10438__00`](2512.10438__00.md) | proved | high | yes | CONFIRMED | y | y | y |
| [`2512.17232__00`](2512.17232__00.md) | disproved | high | no | ALREADY_KNOWN | y | y | y |
| [`2512.17342__00`](2512.17342__00.md) | disproved | high | no | ALREADY_KNOWN | y | y | y |
| [`2602.16333__00`](2602.16333__00.md) | proved | high | yes | ALREADY_KNOWN | y | y | y |
| [`2603.02786__03`](2603.02786__03.md) | disproved | high | no | CONFIRMED | y | y | y |
| [`2604.09449__00`](2604.09449__00.md) | disproved | medium | no | ALREADY_KNOWN | n | y | y |

## Review cost

- Model: `claude-fable-5` for all 77 reviews.
- Output tokens (incl. reasoning): 1,151,884 total (min 342 / median 12,223 / max 56,191 per review).
- Input tokens incl. cache reads/writes: 213,549,464.
- Per-review token detail lives in `verdicts.json` (`review_tokens`) and `usage.json`.

