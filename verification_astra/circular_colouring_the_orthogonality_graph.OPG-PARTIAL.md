<!--
NOT a review of a campaign target. This report was produced by a referee that was
briefed with the wrong leg: it reviewed attacks_opg/circular_colouring_the_orthogonality_graph
(verdict `partial`, would_publish false, never selected) instead of
attacks_retry/circular_colouring_the_orthogonality_graph (verdict `proved`,
would_publish true), which is the actual target. Kept because it is a sound review of
the OPG writeup and because its own computation improves the recorded lower bound for
the circular chromatic number of the orthogonality graph from 7/2 to 19/5. The target's
review is in circular_colouring_the_orthogonality_graph.md.
-->

---
id: circular_colouring_the_orthogonality_graph
leg: attacks_opg
claimed_verdict: partial
review_verdict: CONFIRMED
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: Every step of both propositions checks out and is confirmed computationally, but the writeup badly undersells itself — its own Proposition 1 plus a routine finite computation (the 289 lines of sup-norm ≤ 4 admit no homomorphism to K_{19/5}) already forces χ_c(O) ≥ 23/6, far above the 7/2 the writeup says it cannot improve.
---

## Interpretation

The problem (OpenProblemGarden, DeVos–Ghebleh–Goddyn–Mohar–Naserasr, 2008) asks whether
χ_c(𝒪) = 4, where 𝒪 has as vertices **all lines through the origin in ℝ³**, adjacent when
perpendicular. This is the *continuous* version. The writeup works in exactly this graph
throughout: vertices are lines in ℝ³, common neighbours are produced by cross products,
and Section 3 projects unit vectors onto z^⊥. There is no drift into the ±1-hypercube
orthogonality graph of Frankl–Rödl / Godsil–Newman, and no conflation of the sphere and
hypercube versions anywhere. The "finite subgraph" statements are about genuine finite
subgraphs of the continuous 𝒪, which is the right notion. **Interpretation: fair.**

The writeup does **not** claim to resolve the problem: `verdict = partial`,
`would_publish = false`, and Section 5 states plainly that "numbers strictly below 4 can
have supremum 4", so Proposition 2 does not disprove the conjecture. There is no
interpretation gaming and no strawman. Two things are actually claimed:

* **Proposition 1.** χ_c(𝒪) ∈ {4 − 1/k : k ≥ 2} ∪ {4}, and if χ_c(𝒪) < 4 the value is
  attained by a homomorphism 𝒪 → K_{(4k−1)/k}.
* **Proposition 2.** Every finite F ⊆ 𝒪 has χ_c(F) < 4; quantitatively
  χ_c(F) ≤ 4 − 1/⌊(n+1)/4⌋ for n = |V(F)| ≥ 3.

**Note on the briefing.** The task description I was given ("Claim: proved, high
confidence — a geometric odd-walk lemma excludes every homomorphism from the orthogonality
graph to some target") does not describe this writeup. There is no odd-walk lemma, no
homomorphism-exclusion argument, and no claim of a proof. The briefing appears to have
been mismatched to the target; this review is of the file actually present.

## Step-by-step findings

| step | label | note |
|---|---|---|
| S0. Definitions: χ_c(G) = inf{p/q : G → K_{p/q}} also for infinite G | VALID | The stated recipe works: rescaling an r-colouring to circumference r(1+ε) gives *uniform* slack 1+ε on every edge simultaneously (this is exactly what makes the argument insensitive to |V|), after which rounding to a grid of mesh δ < ε perturbs each colour by ≤ δ/2 and each distance by ≤ δ, leaving > 1. |
| S1. Lemma 1: an optimal colouring exists | VALID | Standard compactness on (ℝ/ℤ)^V for finite H. Terse but correct. |
| S2. Lemma 1: the tight-edge digraph has a directed cycle | VALID | Re-derived. If acyclic, take h strictly increasing along arcs and set f + εh. A tight edge's forward arc becomes 1 + δ and its backward arc R − 1 − δ; both exceed 1 for small ε because R > 2 (the case R = 2 is separated out). Non-tight edges have strict slack, finitely many. Uniform slack ⇒ rescale below R, contradiction. |
| S3. Lemma 1: ℓ = mR and p ≤ ℓ ≤ \|V(H)\| | VALID | ℓ·1 ≡ 0 (mod R) gives ℓ = mR; with R = p/q in lowest terms, ℓq = mp and gcd(p,q)=1 force p \| ℓ, so p ≤ ℓ ≤ \|V(H)\| as the cycle is simple. |
| S4. Lemma 1: the colouring contains a regular p-gon | VALID | On a circle of circumference p/q, the orbit of +1 is, after scaling by q, the orbit of +q mod p, of size p/gcd(p,q) = p, equally spaced by 1/q. Since p \| ℓ, the tight cycle traverses the whole orbit. |
| S5. p/q-colouring ⇒ homomorphism to K_{p/q} | VALID | After scaling by q the forward separation d lies in [q, p−q]; flooring both ends changes it to ⌊d⌋ or ⌈d⌉, and both q and p−q are integers, so the value stays in [q, p−q]. |
| S6. 𝒪 has the common-neighbour property (incl. a vertex with itself) | VALID | Distinct lines [u] ≠ [v]: u×v ≠ 0 is perpendicular to both. A line with itself: any line in its perpendicular plane. |
| S7. Neighbours of a vertex lie in an arc of length R−2 | VALID | Colours at circular distance ≥ 1 from f(v) form the arc [f(v)+1, f(v)+R−1]. |
| S8. Every pair of *used colours* is at circular distance ≤ R−2 | VALID | For used colours α, β pick preimages u, v and a common neighbour w; α, β ∈ [f(w)+1, f(w)+R−1], so δ(α,β) ≤ R−2. The "possibly equal" clause of the hypothesis is what makes this work for α = β as well. |
| S9. ⌊p/2⌋/q ≤ p/q − 2 ⟹ p = 4q−1, R = 4 − 1/q | VALID | Re-derived: the largest distance inside the p-gon is ⌊p/2⌋/q; the inequality is ⌊p/2⌋ ≤ p − 2q, i.e. ⌈p/2⌉ ≥ 2q, i.e. p ≥ 4q−1 (p = 4q−2 gives ⌈p/2⌉ = 2q−1, too small). With R < 4, i.e. p ≤ 4q−1, equality follows. |
| S10. Infinite case: finite-palette approximation | VALID | Immediate from S0. |
| S11. The image H ⊆ K_{p/q} inherits the property; R ≤ χ_c(H) ≤ p/q | VALID | Colours of common neighbours are common neighbours of the colours, and are used. G → H gives χ_c(G) ≤ χ_c(H); H ⊆ K_{p/q} gives χ_c(H) ≤ p/q. |
| S12. Discreteness of {4 − 1/k} below 4 pins R; attainment | VALID | For R < 4 the set {4 − 1/k} ∩ [R, 4) has a minimum 4 − 1/k₀; taking η < (4 − 1/k₀) − R forces R = 4 − 1/k₀. Then χ_c(H) = R with H finite gives H → K_{(4k−1)/k}, and (4k−1, k) are coprime so the ratio is already in lowest terms. |
| S13. Application to 𝒪: k = 1 excluded, so k ≥ 2 (Proposition 1) | VALID | χ_c = 3 would give 𝒪 → K_3 by the attainment clause, contradicting Kochen–Specker non-3-colourability. |
| S14. Remark: this rederives the 7/2 lower bound | VALID | Correct, and worth emphasising: the published 7/2 is a two-line consequence of S9 + non-3-colourability. |
| S15. Proposition 2: the projection colouring | VALID | Generic z avoids finitely many great circles (⊥) and finitely many points (∥). With u_L·z > 0 and v_L = u_L − (u_L·z)z, orthogonality gives v_L·v_M = −(u_L·z)(u_M·z) < 0 **strictly**, so the planar angle exceeds π/2 strictly; on a circle of circumference 4 the induced distance exceeds 1 strictly. Finiteness gives λ > 1 and χ_c(F) ≤ 4/λ < 4. Clean and correct. |
| S16. Remark on "real three-dimensional orthogonal representation" | VALID (terminology) | The mathematics is right, but "orthogonal representation" is standardly used (Lovász) for the *opposite* convention — non-adjacent vertices orthogonal. Here it means adjacent vertices perpendicular. Cosmetic. |
| S17. Count bound, case q ≤ k | VALID | p/q ≤ (4q−1)/q = 4 − 1/q ≤ 4 − 1/k. |
| S18. Count bound, case q ≥ k+1 | VALID | k = ⌊(n+1)/4⌋ gives 4k ≤ n+1 ≤ 4k+3, hence n ≤ 4k+2; then p/q ≤ n/(k+1) ≤ (4k+2)/(k+1) = 4 − 2/(k+1) ≤ 4 − 1/k for all k ≥ 1. n ≥ 3 ensures k ≥ 1. Edgeless case (χ_c = 1) covered. |
| S19. Corollary: χ_c(F) > 4 − 1/k needs n ≥ 4k+3 | VALID | Contrapositive of S17–S18 plus monotonicity of j ↦ 4 − 1/j. |
| S20. Section 4, identity (3): N(a) ∩ N(a+2k−1) = {a+3k−1} | VALID | Re-derived and verified by code for k = 1..11. N(0) = {k,…,3k−1}, N(2k−1) = {3k−1,…,4k−2} ∪ {0,…,k−1}, intersection {3k−1}. |
| S21. Cross-product rigidity consequence | VALID | [u] ≠ [v] because their colours differ, so u×v ≠ 0 and its line is a common neighbour; (3) then forces its colour. The writeup honestly reports that no contradiction follows. |
| S22. Section 5, compactness identity (4) | VALID | Edge constraints are closed in the compact product (ℝ/rℤ)^{V(𝒪)}; every finite subfamily is satisfiable for r above the sup; Tychonoff + FIP. |
| S23. "Nothing above excludes even 7/2" | UNDER-CLAIM | Not an error, but false as a statement about what Proposition 1 can deliver: see **Computational check**. A 289-vertex subgraph of 𝒪 with no homomorphism to K_{19/5} plus Proposition 1 gives χ_c(𝒪) ≥ 23/6. |

No step was found to be a GAP or an ERROR.

## Reference check

* **Kochen–Specker (χ(𝒪) ≥ 4, equivalently no independent set meeting every triangle).**
  Invoked only as "stated in the question"; it is stated in the prompt's own discussion and
  is the standard 1967 result. The implication used is immediate: if χ(𝒪) = 3 then each of
  the three colour classes meets every orthogonal basis. Confirmed.
* **The 7/2 lower bound attributed to DeVos, Ghebleh, Goddyn, Mohar, Naserasr.** I fetched
  the OpenProblemGarden entry in full: it gives **no bibliographic reference** for the 3.5
  bound, and a 2009 comment says the problem is still open. The bound appears to be
  unpublished. The writeup only uses it as background and does not lean on it.
* **Catalog mis-citation (not the writeup's fault).** The catalog's reviewer note guesses
  that DOI 10.1137/050639715 — "Coloring an Orthogonality Graph" — is the source of the 3.5
  bound. I fetched arXiv `math/0509151`: that paper is **Godsil & Newman**, and it concerns
  the ±1-hypercube orthogonality graph and its *ordinary* chromatic number in a quantum
  communication setting, not χ_c of the ℝ³ line graph. It is not the source.
* **DeVos, Ebrahimi, Ghebleh, Goddyn, Mohar, Naserasr, "Circular Coloring the Plane",
  SIAM J. Discrete Math. 21 (2007) 461–465, DOI 10.1137/060664276.** I retrieved and read
  the full PDF (mohar's reprint page). It proves χ_c(R) ≥ 4 for the plane unit-distance
  graph by a completely different (H = K_4 − e, √3-distance) argument. It contains **no**
  common-neighbour lemma and nothing about 𝒪. Notably it closes with: *"It remains open
  whether or not R has a finite subgraph with the same property"* — i.e. the analogue of
  the writeup's Proposition 2 was, for the plane, explicitly open. That makes Proposition 2
  a meaningful (if short) observation rather than a restatement of published work.
* **Priority check (step 2b).** I searched for the common-neighbour spectrum lemma as a
  named result (gap theorems for χ_c, "every two vertices have a common neighbour",
  4 − 1/k spectra), for 2026 arXiv work resolving χ_c(𝒪), and for any improvement of the
  3.5 bound. Nothing was found. Zhu's survey-level facts that the writeup does use
  (rationality, p ≤ |V|, tight cycles) are genuinely standard and are used correctly.
* **Self-contamination check (step 2c).** I searched explicitly for this campaign's own
  artifacts (`circular_colouring_the_orthogonality_graph`, `graph-theory-auto`,
  `gpt-6-astra`). No search result traced back to this repository, and no purported prior
  art surfaced at all. So there is nothing to mistake for prior art here — but equally, I
  could not *confirm* novelty of Propositions 1 and 2, and I record them as unverified for
  novelty rather than as either known or new. The writeup itself asserts no novelty.

**references_ok: true** — every external result invoked is real, correctly stated, and
correctly used.

## Computational check

Scripts: `verification_astra/scripts/circular_colouring_the_orthogonality_graph/`
(`circ.py`, `geom.py`, `test1_lemma2.py`, `test2_ortho.py`, `test3_more.py`,
`test4_core.py`, `test5_z3.py`, `test6_exact.py`, `test7_push.py`). Exact χ_c is computed
as the least p/q in lowest terms with p ≤ n admitting a homomorphism to K_{p/q}, by
backtracking with forward checking; validated against χ_c(C₅) = 5/2, χ_c(K₄) = 4,
χ_c(Petersen) = 3, χ_c(K_{7/2}) = 7/2, χ_c(K_{11/3}) = 11/3. All negative (non-existence)
results below were re-derived a second time with **z3**, on an orthogonality graph rebuilt
from scratch in **exact integer arithmetic** (primitive integer direction vectors,
adjacency iff the integer dot product is 0 — no floating point), with encoding sanity
checks on circular cliques themselves.

**1. Lemma 2 (finite case) — no counterexample.**
Exhaustively over *all* graphs on 5 and 6 vertices with the common-neighbour property
(141 and 4503 graphs respectively) and over 4000 random graphs on 4–10 vertices: **zero
violations**. The only values below 4 ever observed were exactly 3 and 7/2, as Lemma 2
predicts. K_{(4k−1)/k} does have the common-neighbour property with χ_c = 4 − 1/k for
k = 1, 2, 3, so the conclusion is not vacuous.

**2. Section 4's identity (3).** Verified for k = 1..11 and all a: in K_{(4k−1)/k},
N(a) ∩ N(a+2k−1) = {a+3k−1} exactly.

**3. Proposition 2's projection colouring — works as described.** On real finite subgraphs
of 𝒪, a random generic z gives min edge distance λ > 1 on the circumference-4 circle:

| subgraph | n | edges | best λ | bound 4/λ |
|---|---|---|---|---|
| 25-ray Kochen–Specker configuration | 25 | 42 | 1.03015 | 3.8829 |
| 𝒪₂ (integer directions, sup-norm ≤ 2) | 49 | 138 | 1.00639 | 3.9746 |
| 𝒪₃ (sup-norm ≤ 3) | 145 | 546 | 1.00217 | 3.9914 |

λ → 1 as the line set grows, exactly as the proof predicts (the bound degrades but never
reaches 4 for a finite graph).

**4. Proposition 2 and the count bound — confirmed on explicit subgraphs.** The 25-ray
Kochen–Specker configuration has χ_c = **7/2** exactly (no homomorphism to any K_{p/q}
with 3 < p/q < 7/2; it is not 3-colourable). Prop. 2 (< 4) ✓; count bound
4 − 1/⌊26/4⌋ = 23/6 ✓. Sixty random subgraphs of 𝒪₃ on 6–13 vertices: zero violations of
either statement.

**5. The finding: Proposition 1 is much stronger than the writeup realises.**
With z3, on the exact-integer orthogonality graphs:

| graph | n | edges | → K₃ | → K_{7/2} | → K_{18/5} | → K_{11/3} | → K_{15/4} | → K_{19/5} | → K₄ |
|---|---|---|---|---|---|---|---|---|---|
| 𝒪₂ | 49 | 138 | unsat | unsat | unsat | **sat** | sat | sat | sat |
| 𝒪₃ | 145 | 546 | unsat | unsat | unsat | **unsat** | **unsat** | — | sat |
| 𝒪₄ | 289 | 1326 | — | — | — | unsat | unsat | **unsat** | sat |

A full scan of all 10 candidate ratios in (7/2, 11/3] with numerator ≤ 49 gives
**χ_c(𝒪₂) = 11/3 exactly** (χ_c(𝒪₂) > 7/2 because 𝒪₂ ↛ K_{7/2}, and the scan rules out
every ratio strictly between). 𝒪₃ admits no homomorphism to K_{15/4}, so
**χ_c(𝒪₃) > 15/4 = 3.75**. And 𝒪₄ — the 289 lines of sup-norm ≤ 4 — admits none to
K_{19/5}, so **χ_c(𝒪₄) > 19/5 = 3.8**, while 𝒪₄ → K₄ remains satisfiable (as it must, by
the octahedron 4-colouring).

The z3 encoding was validated on nine circular-clique-to-circular-clique instances that
exercise precisely the ratios used, all matching the known answers: K_{7/2} → K_{7/2} sat,
K_{11/3} → K_{7/2} unsat, K_{7/2} → K_{11/3} sat, K_{15/4} → K_{11/3} unsat,
K_{11/3} → K_{15/4} sat, K₄ → K_{15/4} unsat, K_{5/2} → K_{5/2} sat, K_{7/3} → K_{5/2}
sat, K_{5/2} → K_{7/3} unsat. My own backtracking solver and z3 agree on every instance
both were run on.

Consequences (𝒪₂, 𝒪₃ are induced subgraphs of 𝒪, and χ_c is monotone):

* **Unconditionally, χ_c(𝒪) > 19/5 = 3.8** — already well beyond the 7/2 = 3.5 that the
  catalog and the writeup both record as the state of the art. This uses none of the
  writeup's results.
* **Combined with the writeup's Proposition 1**, whose spectrum is {4 − 1/k}, this forces
  **χ_c(𝒪) ≥ 23/6 ≈ 3.8333.**

So the writeup's closing sentence — "Nothing above excludes even 7/2, so no stronger lower
bound or resolution is claimed" — is an under-claim. Proposition 1 converts *any* finite
certificate above 4 − 1/k into the next value up, and such certificates are cheap to
produce. The pattern is monotone and shows no sign of stopping — 𝒪₂ excludes 7/2, 𝒪₃
excludes 15/4, 𝒪₄ excludes 19/5, each one step further up the spectrum — which suggests
that letting the line set grow drives the bound to 4. That would be evidence for the
conjecture and possibly a route to it: the obvious next step is to find a *uniform*
construction realising the pattern, i.e. for every k a finite subgraph of 𝒪 with no
homomorphism to K_{(4k−1)/k}, which together with Proposition 1 would prove
χ_c(𝒪) = 4 outright. This is the experiment the writeup's own Proposition 1 makes worth
running, and it did not run it.

I emphasise that this improved bound is *my* computation, not a claim of the writeup. It
should be independently reproduced (and checked against the authors of the 3.5 bound, whose
argument is unpublished) before being presented as new.

## Caveats

1. **Nothing here resolves the problem.** Proposition 1 leaves 7/2, 11/3, 15/4, … open (my
   computation removes the first four of them, but infinitely many remain) and
   Proposition 2 explicitly does not disprove the conjecture. The writeup is honest about
   this.
2. **Proposition 1 depends on an external fact**, Kochen–Specker non-3-colourability, which
   is assumed from the prompt rather than proved. That is legitimate but worth stating.
3. **"Orthogonal representation" in Section 3 is used with the reverse of the standard
   convention** (standard: *non*-adjacent vertices get orthogonal vectors). Cosmetic.
4. **Lemma 1's compactness step is terse** ("an optimal colouring exists by compactness").
   Correct and standard, but a referee of a real submission would ask for a line more.
5. **Edge cases are handled**: edgeless graphs (χ_c = 1), R = 2 in Lemma 1, n ≥ 3 in the
   count bound, and the "possibly equal" clause in the common-neighbour property (which is
   load-bearing in S8 and which 𝒪 does satisfy).
6. **Novelty is unverified in both directions.** I could not locate Proposition 1 or
   Proposition 2 in the literature, nor could I rule out that they are folklore among the
   original authors — the 3.5 bound itself is unpublished, and Proposition 1 reproduces it
   in two lines, which is at least consistent with Lemma 2 being how DeVos et al. obtained
   it. The writeup asserts no novelty, so this does not affect the verdict.
7. **Verdict block vs. what is proved**: they match exactly. The one-line claim
   ("Any value of χ_c(𝒪) below 4 must be 4−1/k for an integer k≥2, while every finite
   subgraph of 𝒪 has circular chromatic number strictly below 4") is precisely
   Propositions 1 and 2, with no overreach.
8. **The task briefing did not match this target** (it described a proof by a "geometric
   odd-walk lemma"). If that briefing was generated from a different writeup, that other
   file should be reviewed separately.

## Referee summary

I set out to break this writeup and could not. Every one of the 24 steps I isolated is
valid: Lemma 1 is the standard tight-cycle argument, correctly executed down to the
divisibility p | ℓ and the p-gon orbit; Lemma 2's finite case turns on the clean inequality
⌈p/2⌉ ≥ 2q, which I re-derived and which is exactly right at the boundary p = 4q−1; the
infinite case is handled properly via the finite image H and the discreteness of
{4 − 1/k} below 4; Proposition 2's projection argument is correct and, unusually for a
single-pass LLM proof, gets the *strict* inequality v_L·v_M < 0 for the right reason.
Computationally nothing failed: Lemma 2 survives an exhaustive check over all
common-neighbour graphs on 5 and 6 vertices and 4000 random ones, the Section 4 identity
holds for k = 1..11, the projection colouring really does give λ > 1 on genuine subgraphs
of 𝒪, and the 25-ray Kochen–Specker configuration has χ_c exactly 7/2, comfortably inside
both of Proposition 2's bounds. The writeup's interpretation is faithful to the ℝ³ line
graph and never drifts to the hypercube version. The one substantive criticism is the
reverse of the usual one: the writeup is **too modest**. Its own Proposition 1 says the
answer lives in {4 − 1/k}, so any finite subgraph certificate ratchets the lower bound to
the next value; I produced such certificates with z3 in exact integer arithmetic (the 49
lines of sup-norm ≤ 2 have χ_c = 11/3; the 145 lines of sup-norm ≤ 3 admit no homomorphism
to K_{15/4}; the 289 lines of sup-norm ≤ 4 admit none to K_{19/5}), which gives
χ_c(𝒪) > 19/5 unconditionally and χ_c(𝒪) ≥ 23/6 via Proposition 1 — well above the 7/2
the writeup declares it cannot improve, and the pattern climbs one spectrum step per
enlargement with no sign of stopping. The
mathematics as written is correct, so I record CONFIRMED, with the caveat that the result
is a partial structural one that does not resolve the conjecture, and with the strong
recommendation that the Proposition 1 + finite-certificate combination be pushed further,
since it appears to improve the state of the art recorded for this problem.
