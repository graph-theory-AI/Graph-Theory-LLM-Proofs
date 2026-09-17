---
id: circular_colouring_the_orthogonality_graph
leg: attacks_retry
claimed_verdict: proved
review_verdict: CONFIRMED
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The geometric odd-walk lemma is correct (re-verified in exact arithmetic on seven explicit triples and on ~4000 random ones), the locally-bipartite reduction and the K_{p/q} lemma are correct and sharp, so the proof that χ_c(𝒪) = 4 stands; it resolves Conjecture 4.41 of Ghebleh's 2007 SFU thesis, whose Theorem 4.40 (χ_c ≥ 11/3, not the catalog's 3.5) is the true published state of the art.
---

<!--
NOTE ON THE TWO REPORTS FOR THIS ID.  `circular_colouring_the_orthogonality_graph.OPG-PARTIAL.md`
reviews `attacks_opg/…` (verdict `partial`, would_publish false) — a different, weaker
writeup that a mis-briefed referee reviewed.  THIS file reviews the actual campaign
target, `attacks_retry/…` (verdict `proved`, would_publish true).
-->

## Interpretation

The problem (OpenProblemGarden, DeVos–Ghebleh–Goddyn–Mohar–Naserasr, 2008) asks whether
χ_c(𝒪) = 4 for the **continuous** orthogonality graph 𝒪: vertices are all lines through
the origin in ℝ³, adjacent when perpendicular. The writeup opens with exactly this object
("the one-dimensional subspaces of ℝ³, with adjacency given by orthogonality") and never
leaves it. There is no drift into the ±1-hypercube orthogonality graph of Frankl–Rödl /
Godsil–Newman, no substitution of a finite subgraph for 𝒪, and no weakening of the
question.

Both standard definitions of χ_c for an infinite graph are handled: the homomorphism
(finite-palette) definition χ_c(G) = inf{p/q : G → K_{p/q}} in §3, and the real-circle
definition (colours in ℝ/rℤ, adjacent vertices at circular distance ≥ 1) in the second half
of §3. The answer claimed — χ_c(𝒪) = 4, i.e. **yes** to the problem — is the intended
reading, and the author of the original problem would consider it resolved. There is no
"as literally stated" gaming and no strawman.

The writeup in fact proves something strictly stronger than asked:

> **Theorem.** 𝒪 has no homomorphism to any *finite* graph in which every open
> neighbourhood induces a bipartite graph ("locally bipartite").

χ_c(𝒪) ≥ 4 is the corollary, because K_{p/q} is locally bipartite exactly when p < 4q.
Equivalently: **every finite homomorphic image of 𝒪 contains an odd wheel.** The
one-line verdict is an accurate, if slightly understated, description of what is proved.

**Interpretation: fair.**

## Step-by-step findings

I number the steps L* (§1 lemma), C (corollary), H* (§2), K* (§3), U* (§4), W* (§5).

| step | label | note |
|---|---|---|
| L0. Setup: P_a = a^⊥, J_a(x) = a×x; J_a(x) ≠ 0 represents a line ⊥ [x] lying in P_a | VALID | Immediate: (a×x)·x = 0 and (a×x)·a = 0. Adjacency in 𝒪 is exactly perpendicularity of the two lines, and perpendicular lines are automatically distinct, so no loop can be created. |
| L1. Case "two normals perpendicular", say a ⊥ b: [a],[b],[a×b] is a triangle inside P_a ∪ P_b ∪ P_c | VALID | [a] ⊆ P_b and [b] ⊆ P_a because a ⊥ b; [a×b] ⊆ P_a ∩ P_b. All three pairwise perpendicular. Verified exactly in code for ([1,0,0],[0,1,0],[1,2,3]) — the triangle is the standard basis. Note this case needs only *two* of the three planes; c is not used, which is fine. |
| L2. Normalisation a = (0,0,1), b = (s,0,t) with s > 0, 0 < t < 1, and c = (u,v,w) | VALID | Unit-normalise; t = a·b ≠ 0 by non-orthogonality, flip the sign of b to get t > 0; rotate about a to get s ≥ 0, and s > 0 because b ∦ a; then t < 1. The sign/rotation choices are stated only as "choose their signs and an orthonormal coordinate system", but they are exactly the two just described and change nothing projectively. |
| L3. Condition (1): v ≠ 0, w ≠ 0, su + tw ≠ 0 | VALID | a,b span the xz-plane, so linear independence of a,b,c ⟺ v ≠ 0. w = a·c ≠ 0 and su + tw = b·c ≠ 0 are the two remaining non-orthogonality hypotheses. |
| L4. Injectivity: J_d : P_e → P_d is injective whenever d·e ≠ 0 | VALID | ker J_d = ℝd, and ℝd ∩ P_e = 0 ⟺ d ∉ P_e ⟺ d·e ≠ 0. The blanket claim "this applies to every transition below" is true: the transitions actually used are P_a→P_b (needs a·b≠0), P_b→P_b and P_a→P_a (need b·b, a·a ≠ 0), P_b→P_c (b·c≠0), P_c→P_a (a·c≠0), P_b→P_a (a·b≠0). All are covered by pairwise non-orthogonality plus |a|=|b|=1. So no vector in any walk is ever zero. |
| L5. Matrix formulas (2): E = J_a²J_b² = diag(t²,1) and F = J_aJ_cJ_b = [[0, su+tw],[−tw, sv]] on P_a | VALID | Re-derived by hand and confirmed symbolically. J_b(x₁,x₂,0) = (−tx₂, tx₁, sx₂); J_b²x = (−t²x₁, −x₂, stx₁); J_a(y) = (−y₂,y₁,0), so J_a²J_b²x = (t²x₁, x₂, 0). For F: J_cJ_bx = (svx₂ − twx₁, −(su+tw)x₂, t(ux₁+vx₂)), then J_a gives ((su+tw)x₂, svx₂ − twx₁, 0). Both matched numerically on a basis of P_a for 4000 random triples and exactly (sympy) on six explicit integer triples. |
| L6. Walk interpretation: F is a 3-edge walk P_a→P_b→P_c→P_a, E a 4-edge walk P_a→P_b→P_b→P_a→P_a | VALID | Composition order is right (rightmost operator applied first). Each intermediate vector lies in the plane of the operator just applied, hence inside P_a ∪ P_b ∪ P_c; each consecutive pair is perpendicular by L0; none is zero by L4. The one step that could look odd, J_b applied to a vector already in P_b, is legitimate — it is the 90° rotation of P_b, and b ∉ P_b. |
| L7. E^nF = [[0, t^{2n}(su+tw)],[−tw, sv]] and discriminant (3) Δ_n = (sv)² − 4t^{2n}·tw(su+tw) | VALID | E^n = diag(t^{2n},1); the product and the char-poly discriminant λ² − (sv)λ + t^{2n}(su+tw)tw are re-derived correctly. Checked numerically against trace²−4·det on every random triple (agreement to 1e-9 relative). |
| L8. Δ_n → (sv)² > 0, so some n ≥ 0 has Δ_n > 0 | VALID | 0 < t < 1 forces t^{2n} → 0; s > 0 and v ≠ 0 give (sv)² > 0. The n is *effective*: if tw(su+tw) ≤ 0 then n = 0 works, otherwise n = ⌈log((sv)²/(4t·w(su+tw)))/(2 log t)⌉. See Caveats for how large this can get. |
| L9. E^nF invertible, so the real eigenvalue λ is nonzero | VALID | det(E^nF) = t^{2n}(su+tw)·tw ≠ 0 by (1) and t > 0. Δ_n > 0 gives two distinct **real** eigenvalues, hence a real eigenvector x₀ ≠ 0 in P_a. |
| L10. Conclusion: closed walk of odd length 3 + 4n inside P_a ∪ P_b ∪ P_c, so the induced subgraph is non-bipartite | VALID | The walk ends at [E^nF x₀] = [λx₀] = [x₀]; working with **lines** rather than vectors is what makes λ < 0 harmless, and the writeup is right to phrase it projectively. Length 3 + 4n is odd; a closed odd walk in a simple loopless graph contains an odd cycle. Verified in exact arithmetic (below). |
| C. Corollary: 𝒪[N_𝒪(S)] bipartite ⟹ span(S) has dimension ≤ 2 | VALID | N_𝒪([a]) is precisely the set of lines contained in P_a, so for [a],[b],[c] ∈ S independent the lemma's subgraph is an *induced* subgraph of 𝒪[N_𝒪(S)]; non-bipartite induced subgraph ⟹ non-bipartite. |
| H1. For h : 𝒪 → H and S_α = h^{-1}(α), one has 𝒪[N_𝒪(S_α)] → H[N_H(α)] | VALID | If L ~ M with M ∈ S_α then h(L) ~ α, so h(L) ∈ N_H(α); and an edge inside N_𝒪(S_α) maps to an edge inside N_H(α). H locally bipartite ⟹ target bipartite ⟹ source bipartite. (Incidentally H has no loops: a loop at α would make N_H(α) ∋ α non-bipartite.) |
| H2. Hence every fibre S_α spans dimension ≤ 2 | VALID | Direct from C. |
| H3. Pigeonhole: the 2m+1 moment-curve lines [(1,j,j²)], 1 ≤ j ≤ 2m+1, with m = \|V(H)\| | VALID | ⌈(2m+1)/m⌉ = 3, so some fibre contains three of them; the Vandermonde determinant (j−i)(k−i)(k−j) ≠ 0 makes any three independent, contradicting H2. Determinant identity verified symbolically for all triples with 1 ≤ i<j<k ≤ 25. The lines are pairwise distinct. |
| K1. Lemma: K_{p/q} is locally bipartite when p < 4q | VALID | N(0) = {q,…,p−q} ⊆ {q,…,3q−1} because p − q < 3q; A = N(0)∩{q,…,2q−1} and B = N(0)∩{2q,…,3q−1} cover it, and any q consecutive residues are pairwise non-adjacent (difference in [1,q−1] ⊄ [q,p−q], using p ≥ 2q). Vertex-transitivity handles all vertices. Verified exhaustively for q = 1..12, p = 2q..6q: locally bipartite **exactly** when p < 4q, so the lemma is sharp. |
| K2. Therefore 𝒪 ↛ K_{p/q} for p/q < 4, i.e. χ_c(𝒪) ≥ 4 (finite-palette definition) | VALID | Immediate from the Theorem + K1. (For p/q < 2 the circular clique is not defined, but 𝒪 contains triangles so χ_c ≥ 3 anyway; not an issue.) |
| K3. Real-circle definition: scale an r-colouring (r < 4) to rational circumference R ∈ (r,4), round to a grid of mesh 1/q | VALID | After scaling, every edge has distance ≥ R/r > 1. Rounding moves each colour by ≤ 1/(2q), hence each distance by ≤ 1/q (the writeup's 2/q is a safe over-estimate), so distances stay ≥ R/r − 2/q > 1. Rounded colours live on p = Rq points, and distance ≥ 1 means the ℤ_p difference lies in [q, p−q]: a homomorphism to K_{p/q} with p/q = R < 4. The estimate is uniform in the vertex, which is exactly why infinitely many vertices are harmless. |
| U1. Explicit proper 4-colouring with boundary rule (z>0, else y>0, else x>0) | VALID | All representatives have z ≥ 0, so two same-quadrant non-pole lines have u·v = (x,y)·(x′,y′) + zz′ > 0 (half-open quadrant ⟹ planar angle < π/2 ⟹ positive planar term). Equatorial representatives have argument in [0,π), so colour 3 (the interval [π,3π/2)) is never used on the equator; every other colour-3 line has z > 0 and so is not ⊥ e₃. Verified: zero monochromatic edges among 5502 orthogonal pairs on the 865 primitive integer directions of sup-norm ≤ 6, and on 200 000 random exactly-perpendicular real pairs. |
| U2. χ_c(𝒪) ≤ χ(𝒪) ≤ 4, hence χ_c(𝒪) = 4 | VALID | Standard, and the upper bound is anyway given in the problem statement. |
| W1. Finite witness F_m: the 2m+1 moment-curve lines plus, for every triple, the lines of its odd walk; F_m ↛ any locally bipartite graph on ≤ m vertices | VALID | The argument is the finite shadow of H1–H3 and is correct: three initial lines share a fibre, and their odd closed walk lives in N(S_α) and would have to map into a bipartite neighbourhood. Two omissions are cosmetic: triples with two perpendicular normals use the L1 triangle instead, and the least n is not bounded (see Caveats). |
| W2. Compatibility with the previous attempt (finite subgraphs all have χ_c < 4) | VALID | No contradiction: the palette that realises χ_c(F_m) < 4 has more than m vertices. This is exactly the previous attempt's Proposition 2, and the two statements sit together consistently — see Caveats and Computational check. |
| W3. "No unproved conjecture, regularity assumption, or computational assertion is used" | VALID | Accurate. The writeup invokes *no external theorem at all*; the only facts used are the definitions of χ_c, "odd closed walk ⟹ non-bipartite", "homomorphism into bipartite ⟹ bipartite", and χ_c ≤ χ. |

No step was found to be a GAP or an ERROR.

## Reference check

The writeup is genuinely self-contained: it cites no paper, no named theorem, and nothing
"from the source paper". The usual failure mode of a misquoted citation therefore cannot
occur here, and `references_ok: true` records that every fact it does use is standard and
used correctly (listed in W3 above).

What remains is the **priority check (step 2b)**, which turned up one important document
that neither the catalog, nor the OpenProblemGarden entry, nor the earlier referee had
located.

### The real prior art: Ghebleh's 2007 thesis

**M. Ghebleh, "Theorems and computations in circular colourings of graphs", Ph.D. thesis,
Simon Fraser University, 2007** — https://summit.sfu.ca/item/8399 (PDF:
`https://summit.sfu.ca/_flysystem/fedora/sfu_migrate/8399/etd3278.pdf`). **§4.4, "The
Projective Plane Orthogonality Graph"**, is exactly this problem, with 𝒪 defined as the lines
through the origin in ℝ³ adjacent when perpendicular, and the Kochen–Specker motivation. It
contains, with G_n := the subgraph of 𝒪 induced by primitive integer vectors of sup-norm ≤ n:

* **Theorem 4.37.** χ(𝒪) = 4 (Kochen–Specker for the lower bound; the 4-colouring is credited
  to Godsil–Zaks, "Coloring the sphere", Waterloo technical report, 1988).
* **Proposition 4.39.** χ_c(𝒪) ≥ 7/2, via χ_c(G₁) = 7/2 on the 13-vertex G₁. *This is the
  "3.5" that OPG and the catalog record.*
* **Theorem 4.40.** **χ_c(𝒪) ≥ 11/3**, proved by computer on a 44-vertex, 117-edge subgraph
  H₂ ⊆ G₂ with χ_c(H₂) = 11/3.
* G₃ (145 vertices, 546 edges) admits a (27,7)-colouring, so 11/3 ≤ χ_c(G₃) ≤ 27/7 = 4 − 1/7.
* **Conjecture 4.41: χ_c(𝒪) = 4** — the conjecture stated verbatim, a year before the OPG
  posting.

Three consequences for this review.

1. **The recorded state of the art is stale in the catalog's favour, not the writeup's.**
   The published record lower bound is **11/3 ≈ 3.667, not 3.5**; and the earlier referee's
   own SAT computation (χ_c(𝒪) > 19/5 = 3.8, and ≥ 23/6 with the previous attempt's
   Proposition 1) already beat *that*. None of this touches the writeup, which claims the
   full χ_c(𝒪) = 4 and does not lean on any recorded bound.
2. **The conjecture is published; the theorem is not.** Conjecture 4.41 is the statement being
   proved, so the writeup is answering a named published conjecture, not a folklore question.
   The odd-walk lemma, the three-planes construction and the locally-bipartite reduction are
   **not** in the thesis: §4.4 proceeds entirely by computer search on finite G_n. So this is
   **not** ALREADY_KNOWN.
3. **Ghebleh's data cross-validates the whole computational picture.** His G₁, G₂, G₃ are
   exactly the 13-, 49- and 145-vertex graphs the earlier referee called 𝒪₁, 𝒪₂, 𝒪₃, with the
   same edge counts (13/24, 49/138, 145/546 — I rebuilt them). His χ_c(H₂) = 11/3 with
   H₂ ⊆ G₂ agrees with the earlier referee's independent χ_c(𝒪₂) = 11/3, and his
   χ_c(G₃) ≤ 27/7 = 3.857 sits correctly above the earlier referee's 𝒪₃ ↛ K_{15/4} (3.75) and
   𝒪₃ ↛ K_{11/3}. Two independent computations, twenty years apart, agree.

### Everything else searched

* **OpenProblemGarden entry** (fetched in full): still listed **open**, bibliography section
  **empty**, last comment 2009 — "I am pretty confident this is still open. Apart from this
  one many-author paper, I don't think it has received any significant attention."
* **arXiv.** 0 results for `all:"circular chromatic" AND all:"orthogonality graph"`. The 40
  most recent `abs:"orthogonality graph" AND cat:math.CO` papers (2005 → 2026-07) contain
  nothing on ℝ³ lines or circular colouring (nearest: `2512.01195`, quantum chromatic number;
  `2105.03657`, Kunszenti-Kovács–Lovász–Szegedy on random homomorphisms into the
  orthogonality graph). The 60 most recent `abs:"circular chromatic number" AND cat:math.CO`
  papers likewise contain nothing on 𝒪.
* **zbMATH, OpenAlex (including its full-text index), Crossref, Semantic Scholar.** No paper
  proves χ_c(𝒪) = 4 or improves 11/3. Ghebleh's complete 35-item zbMATH list contains nothing
  on 𝒪 — §4.4 was never turned into a paper.
* **Citations of DeVos–Ebrahimi–Ghebleh–Goddyn–Mohar–Naserasr, "Circular Coloring the Plane",
  SIAM J. Discrete Math. 21 (2007) 461–465, DOI 10.1137/060664276 (Zbl 1140.05303).** Four to
  five citers: Junosza-Szaniawski ×2 and Chybowska-Sokół–Junosza-Szaniawski–Wesek (all on the
  *plane* unit-distance graph), a Coxeter-spectral paper, and the thesis itself. The SIAM
  paper is thesis §4.3 and concerns **only** the plane; its proof is a supremum argument over
  √3-pairs with a K₄−e gadget, **not** a locally-bipartite argument, and the obstruction used
  here could not work there — in the plane unit-distance graph a vertex neighbourhood is a
  unit circle whose induced graph is a disjoint union of 6-cycles, hence bipartite. Nobody
  transferred the method to 𝒪.
* **Catalog mis-citation (not the writeup's fault).** The catalog's reviewer note guesses DOI
  10.1137/050639715, "Coloring an Orthogonality Graph", as the source of the 3.5 bound. That
  is Godsil–Newman (arXiv `math/0509151`) on the ±1-hypercube orthogonality graph's *ordinary*
  chromatic number. It is not the source; the source is Ghebleh's thesis §4.4.
* **The §3 lemma as a named result.** K1 is equivalent to "a graph with a non-bipartite
  neighbourhood contains an odd wheel, hence χ_c ≥ 4". χ_c(odd wheel) = 4 is standard and
  citable (Zhu, "Circular chromatic number: a survey", Discrete Math. 229 (2001) 371–410,
  DOI 10.1016/S0012-365X(00)00217-X), and I re-verified it exactly for W₃, W₅, W₇, W₉. The
  explicit general form "K_{p/q} is locally bipartite iff p < 4q" has no located source, but
  it is a four-line verification the writeup supplies. Note that "locally bipartite" as a term
  is already in use for an unrelated question (F. Illingworth, "The chromatic profile of
  locally bipartite graphs", JCTB 156 (2022) 343–388) — a terminology collision, not a
  mathematical one.
* **Self-contamination check (step 2c).** Clean. Zero hits anywhere traceable to this
  campaign: no `graph-theory-auto`, no `gpt-6-astra`, no AI-generated writeup; and
  `graph-theory-ai.github.io` currently returns GitHub Pages "Site not found", so the catalog
  is not even live to be indexed. Every source named above has real authors, a date, and a
  venue, DOI, arXiv id or institutional-repository record (the thesis is
  `oai:summit.sfu.ca:8399`).
* **Limitation to record honestly.** Every general web engine was unusable from this session
  (the WebSearch budget was exhausted, and Google/Bing/DuckDuckGo/Ecosia/Mojeek/Startpage/
  searx/BASE/CORE all returned a consent wall, CAPTCHA or 403 through WebFetch and curl;
  the Internet Archive was down). The sweep was therefore run through bibliographic APIs —
  zbMATH Open, OpenAlex full text, Crossref, Semantic Scholar, arXiv — plus direct fetches of
  openproblemgarden.org and summit.sfu.ca. For a mathematics priority check that is stronger
  coverage than a keyword web search, but it would miss an unindexed preprint on a personal
  page. **No prior art for the theorem or the lemma was found; novelty is unrefuted rather
  than positively established.**

## Computational check

Scripts (new, this review): `verification_astra/scripts/circular_colouring_the_orthogonality_graph/retry_test1_oddwalk.py`,
`retry_test2_locbip.py`, `retry_test3_exact.py`, `retry_test4_fourcol.py`,
`retry_test5_witness.py`, `retry_test6_wheels.py`, `retry_test7_ghebleh.py`. (The
`test1..test7` scripts in the same
directory are the earlier referee's, for the OPG writeup; I did not rely on them.)

**1. The odd-walk lemma, exact arithmetic (`retry_test3_exact.py`).** For explicit integer
triples the construction is carried out with **no floating point at all**: the matrices E, F
are exact integer matrices in the basis (a×b, a×(a×b)) of P_a, and the eigenvector and the
whole walk live in the real quadratic field ℚ(√Δ_n), implemented as exact pairs
(x, y) ↔ x + y√Δ_n over ℚ. Every orthogonality, every non-vanishing, every plane-membership
and the projective closure are checked as exact identities.

| a, b, c | dots (a·b, a·c, b·c) | E | F | n | walk length | result |
|---|---|---|---|---|---|---|
| (1,0,0),(0,1,0),(1,2,3) | (0,1,2) | — | — | — | 3 | perpendicular case: exact triangle e₁,e₂,e₃ |
| (0,0,1),(1,0,2),(1,1,1) | (2,1,3) | diag(5,4) | [[1,2],[−3,0]] | 15 | **63** | all checks exact |
| (1,1,1),(1,2,3),(2,1,5) | (6,8,19) | diag(42,36) | [[5,48],[−19,0]] | 33 | **135** | all checks exact |
| (0,0,1),(3,0,4),(1,1,7) | (4,7,31) | diag(25,16) | [[3,28],[−31,0]] | 14 | **59** | all checks exact |
| (2,−1,3),(1,4,1),(5,2,−2) | (1,2,11) | diag(252,1) | [[−81,2],[−11,0]] | 0 | **3** | exact *triangle* although a,b,c are pairwise non-orthogonal |
| (1,0,0),(1,1,0),(1,1,1) | (1,1,2) | diag(2,1) | [[1,1],[−2,0]] | 4 | **19** | all checks exact |
| (3,1,2),(1,−2,4),(2,5,1) | (9,13,−4) | diag(294,81) | [[−41,117],[4,0]] | 0 | **3** | all checks exact |

**2. The odd-walk lemma, 4000 random triples (`retry_test1_oddwalk.py`).** 3988 generic
triples fully built (3 skipped for exceeding an n-cap of 4000): **zero failures** of
orthogonality, non-vanishing, plane-membership or closure; every walk length odd and equal
to 3 + 4n. Length histogram: 2097 triples give a triangle (n = 0), and the tail reaches
9607. A dedicated stress test with a, b nearly parallel (t = a·b → 1) produced 67 further
successes, 0 failures, max walk length 15183.

**3. K_{p/q} local bipartiteness (`retry_test2_locbip.py`).** For every q = 1..12 and every
p = 2q..6q, K_{p/q} is locally bipartite **if and only if p < 4q** — the lemma is correct
*and* sharp. The writeup's explicit A/B bipartition of N(0) was checked to cover N(0) and
to consist of independent blocks in every case with p < 4q. K_{7/2}, K_{11/3}, K_{15/4},
K_{19/5}, K_{23/6} are locally bipartite; K₄ (in any representation p/q = 4) and K_{9/2}
are not.

**4. Odd wheels (`retry_test6_wheels.py`), cross-checking §3 from the other side.** With an
independently written exact χ_c solver (calibrated on χ_c(C₅) = 5/2, χ_c(K₄) = 4,
χ_c(Petersen) = 3, χ_c(K_{7/2}) = 7/2, χ_c(K_{11/3}) = 11/3): χ_c(W₃) = χ_c(W₅) = χ_c(W₇) =
χ_c(W₉) = **4**, exactly as K1 requires. Had K1 been wrong, W₅ = K₁ + C₅ would have mapped
to K_{7/2}; it does not.

**5. The four-colouring (`retry_test4_fourcol.py`).** On the 865 primitive integer
directions of sup-norm ≤ 6 (5502 exactly-orthogonal pairs, integer dot products, no floating
point): **0 monochromatic edges**; class sizes 228/228/205/204; the 48 equatorial lines use
only colours 0 and 1, and the pole takes colour 2 — exactly the boundary bookkeeping the
writeup claims. Also 200 000 random exactly-perpendicular real pairs: 0 monochromatic.

**6. Sharpness of the "finite" hypothesis (`retry_test5_witness.py`).** 𝒪 itself **is**
locally bipartite — N_𝒪(L) is the set of lines of the plane L^⊥, in which every line has
exactly one perpendicular, i.e. a perfect matching. Confirmed on the 577 integer directions
of sup-norm ≤ 5: every neighbourhood bipartite, maximum degree inside a neighbourhood = 1.
Since 𝒪 → 𝒪, the finiteness of H in the Theorem is *essential*, and the pigeonhole step H3
is genuinely load-bearing rather than decorative. The writeup states "finite" correctly but
does not remark on this.

**7. The finite witness F₇ (`retry_test5_witness.py`).** Taking m = 7 (the smallest palette,
K_{7/2}) and the 15 moment-curve lines [(1,j,j²)], all C(15,3) = 455 triples were processed:
311 walks fully built with **zero** violations (worst numerical residual over all
orthogonality / containment / closure checks: **5.3 × 10⁻¹⁵**), lengths from 39 to 11927
(median 639); 144 triples were skipped because the required n exceeds 3000, the largest
being **n = 1 037 597**, i.e. a single walk of ≈ 4.15 million edges. So F₇ exists and is
finite, but with these starting lines |V(F₇)| runs to the order of 10⁷.

**8. Consistency with the prior computations.** The earlier referee's SAT results on exact
integer orthogonality graphs — 𝒪₂ ↛ K_{7/2}, 𝒪₃ ↛ K_{11/3} and ↛ K_{15/4}, 𝒪₄ ↛ K_{19/5},
while 𝒪₄ → K₄ — are precisely the finite shadow of this Theorem, and the monotone pattern
that referee observed ("the obvious next step is to find a *uniform* construction realising
the pattern, i.e. for every k a finite subgraph of 𝒪 with no homomorphism to K_{(4k−1)/k}")
is exactly what §5 supplies. Nothing in the new proof contradicts that data; it subsumes it.
Nor does it contradict the previous attempt's Proposition 2 (every finite F ⊆ 𝒪 has
χ_c(F) < 4): F_m does map to some K_{p/q} with p/q < 4, but only for p > m. Quantitatively,
Proposition 2's bound χ_c(F) ≤ 4 − 1/⌊(n+1)/4⌋ gives ≈ 4 − 4·10⁻⁷ for F₇ — perfectly
compatible with F₇ ↛ K_{7/2} = 4 − 1/2, and merely showing that this particular witness is
far from vertex-optimal.

**9. Cross-check against Ghebleh's published finite data (`retry_test7_ghebleh.py`, z3 with a
one-hot boolean encoding).** I rebuilt his G_n from scratch in exact integer arithmetic
(primitive integer directions of sup-norm ≤ n, adjacency iff the integer dot product is 0)
and re-ran the homomorphism questions. The solver was calibrated on eight
circular-clique-to-circular-clique instances with known answers, all matching (K_{7/2}→K_{7/2}
sat, K_{11/3}→K_{7/2} unsat, K_{7/2}→K_{11/3} sat, K₄→K_{15/4} unsat, K_{11/3}→K_{27/7} sat,
K_{27/7}→K_{11/3} unsat, K₄→K_{27/7} unsat, K_{15/4}→K_{27/7} sat).

| graph | \|V\| | \|E\| | → K_{7/2} | → K_{11/3} | → K_{15/4} | → K_{27/7} | → K₄ |
|---|---|---|---|---|---|---|---|
| G₁ | 13 | 24 | sat | sat | sat | sat | sat |
| G₂ | 49 | 138 | **unsat** | sat | sat | sat | sat |
| G₃ | 145 | 546 | **unsat** | **unsat** | (too slow) | **sat** | sat |

Vertex and edge counts match the thesis exactly (145/546 for G₃). Every `sat` came with an
explicit colouring that I re-verified edge by edge against the K_{p/q} adjacency rule
(0 bad edges in every case). Three things follow. (a) Ghebleh's Theorem 4.40 chain is
reproduced: χ_c(G₁) ≤ 7/2 and χ_c(G₂) > 7/2. (b) His (27,7)-colouring of G₃ is confirmed —
and it is exactly the kind of object that would *refute* an over-strong reading of the new
theorem, so its existence is a real test the theorem passes: G₃ is finite, contains none of
the (generally irrational) lines of the odd walks, and maps to a locally bipartite target with
27 vertices. (c) G₃ ↛ K_{11/3} reproduces the earlier referee's independent result and pushes
χ_c(G₃) strictly above Ghebleh's 11/3, so 11/3 < χ_c(G₃) ≤ 27/7.

No computational check failed.

## Caveats

1. **Novelty is not established, only unrefuted.** Correctness and priority are separate.
   I found no prior art (see Reference check) but could not run a general web sweep, and the
   writeup's own caveat field says "literature priority has not been checked". Treat the
   result as *correct and apparently new*, with novelty unconfirmed.
2. **The "finite" hypothesis in the Theorem is essential and unremarked.** 𝒪 is itself
   locally bipartite, so "no homomorphism to a locally bipartite graph" is false without
   finiteness. A reader could misread the Theorem's headline sentence; the statement itself
   is correct.
3. **The least n in the lemma is unbounded.** Δ_n > 0 is guaranteed only asymptotically, and
   n ≈ log((sv)²/(4tw(su+tw)))/(2 log t) blows up as a·b → ±1 (nearly parallel normals) or
   as sv → 0. Measured maxima: n ≈ 10⁶ for some moment-curve triples. This is a size, not a
   soundness, issue — but §5's "terminating search for n" and "this construction uses only
   arithmetic, square roots, and a terminating search" undersell how large F_m becomes
   (≈ 10⁷ vertices already for m = 7, versus the ≥ 11 vertices that Proposition 2 shows are
   information-theoretically necessary to block K_{7/2}). The moment curve is a poor choice
   of starting lines for this purpose; any 2m+1 pairwise well-separated lines would do.
4. **§5 forgets the degenerate sub-case.** A triple of the 2m+1 starting lines with two
   perpendicular normals must use the L1 triangle rather than the E/F construction. The
   moment-curve lines do contain such triples in general. Purely cosmetic.
5. **§3's rounding constant is loose.** "2/q < R/r − 1" with a change of "less than 1/q" per
   colour is a safe over-estimate (nearest-grid rounding moves a colour by ≤ 1/(2q)); and
   "R = p/q, choosing a sufficiently large common multiple of its numerator and denominator"
   means p/q is no longer in lowest terms, which is harmless since K_{p/q} is defined for any
   p ≥ 2q. Correct as written.
6. **L2's normalisation is stated, not derived.** Getting a = (0,0,1), b = (s,0,t) with
   s > 0 and 0 < t < 1 requires flipping the sign of b when a·b < 0 and rotating about a.
   Both are legitimate and projectively invisible, but the writeup compresses them into
   "choose their signs and an orthonormal coordinate system".
7. **Edge cases checked and harmless.** m = 0 (empty H): no homomorphism from a non-empty
   graph anyway. p/q < 2: K_{p/q} undefined, but 𝒪 contains triangles. Loops in H: excluded
   automatically, since a loop at α makes H[N_H(α)] non-bipartite. Degenerate triples with
   all three normals mutually orthogonal: covered by L1.
8. **A natural objection that does *not* land, worth recording because it looks fatal.**
   One might argue: "K_{7/2} is locally bipartite, yet for its triangle {0,2,4} the union
   N(0) ∪ N(2) ∪ N(4) is all of ℤ₇, which is non-bipartite — so an odd walk inside a union of
   three neighbourhoods cannot exclude a homomorphism to K_{7/2}." This is a misreading of the
   argument, and the writeup is not guilty of it. The three lines [a],[b],[c] are not
   arbitrary: they lie in a **single fibre** S_α = h^{-1}(α), so all three map to the *same*
   vertex α, and the union of their neighbourhoods maps into the *single* neighbourhood
   N_H(α) — not into a union of three. That single neighbourhood is bipartite by hypothesis,
   so the odd walk cannot map into it. The whole force of §2 is that the pigeonhole is applied
   to fibres, not to triangles. I checked this reading against the text twice: H1 speaks of
   S_α = h^{-1}(α) throughout, and H3 selects three lines "with the same image under h".
   Relatedly, Ghebleh's G₃ → K_{27/7} is no obstacle either: G₃ is a 145-line *finite*
   subgraph and contains none of the (generally irrational) lines of the odd walks.
9. **What is *not* claimed, correctly.** The writeup does not claim any single finite
   subgraph of 𝒪 has χ_c = 4, and explicitly says so — which is right, since the previous
   attempt proves the opposite. The verdict block's `caveats` field is honest.

## Referee summary

I set out to find the error and did not find one. The three ways a
homomorphism-exclusion argument of this shape normally fails are all closed here. (i) *The
parity obstruction established only on a sub-structure*: the odd closed walk is built
entirely inside P_a ∪ P_b ∪ P_c, and that union is exactly contained in N_𝒪(S) for a fibre
S containing [a],[b],[c] — I re-checked the containment vertex by vertex in exact arithmetic.
(ii) *The target's structure misidentified*: "K_{p/q} is locally bipartite" is not only true
for p < 4q but false for p ≥ 4q, verified exhaustively, and cross-checked from the other side
by computing χ_c of odd wheels. (iii) *Finite and continuous versions conflated mid-proof*:
they are not — the whole argument runs in the continuous 𝒪, and finiteness is used in exactly
one place, the pigeonhole on |V(H)|, which is genuinely necessary because 𝒪 is itself locally
bipartite.

The mechanism, stated in the language the writeup avoids, is a projective holonomy argument:
the lines of each plane form an ℝP¹, the cross-product transitions are projective-linear maps
between these circles, an odd cycle is a fixed point of an odd-length composite, and since the
3-step composite F may be elliptic (no real fixed point) one pads it with the 4-step hyperbolic
composite E, whose n-th power drives the discriminant to (sv)² > 0. That padding is what makes
the length 3 + 4n and keeps the parity odd. It is short, elementary, correct, and I have not
seen it elsewhere.

The one genuinely new thing my priority check turned up is that the recorded state of the
art is wrong in the *catalog's* disfavour: the published record is not 7/2 but **11/3**,
from Theorem 4.40 of Ghebleh's 2007 SFU thesis, whose §4.4 is devoted to this exact graph and
whose Conjecture 4.41 is precisely the statement here proved. That thesis should be the
citation in any writeup of this result, and the catalog's 3.5 and its Godsil–Newman
mis-citation should both be corrected. It does **not** make the result known: §4.4 is a
computer search over finite G_n and contains nothing resembling the odd-walk lemma. It does,
however, cross-validate the computational record — his G₁, G₂, G₃ are the earlier referee's
𝒪₁, 𝒪₂, 𝒪₃ down to the edge counts, and his χ_c(H₂) = 11/3 and χ_c(G₃) ≤ 27/7 sit exactly
where that referee's independent SAT runs put them.

The tension flagged in my briefing — that the earlier referee's exact-arithmetic SAT
computation reached only χ_c(𝒪) > 19/5 — resolves cleanly in the writeup's favour. That
computation bounds χ_c of *finite* subgraphs, which the previous attempt proved can never
reach 4; the new theorem is about 𝒪 itself, and the finite witnesses it produces (§5) are the
uniform family the earlier referee identified as the missing ingredient. 𝒪₂ ↛ K_{7/2},
𝒪₃ ↛ K_{15/4}, 𝒪₄ ↛ K_{19/5} are exactly the first three instances of the pattern the new
proof explains. The two are consistent, and the new result is strictly stronger.

Verdict **CONFIRMED**, high confidence on the mathematics: every step is VALID, no external
reference is invoked at all, the interpretation is the intended one, and every finite object
in the writeup (the matrices, the walks, the bipartitions, the four-colouring, the witness
construction) was verified independently in code — the core lemma in exact arithmetic over a
real quadratic field. The single reservation is priority: I found no prior art for either the
theorem or the odd-walk lemma across zbMATH, OpenAlex full text, Crossref, Semantic Scholar,
arXiv and the thesis literature, but no general web engine was reachable from this session, so
novelty should be regarded as unrefuted rather than proven. Subject to that, this is a
resolution of the 2008 DeVos–Ghebleh–Goddyn–Mohar–Naserasr problem, and of Ghebleh's
Conjecture 4.41: χ_c(𝒪) = 4.
