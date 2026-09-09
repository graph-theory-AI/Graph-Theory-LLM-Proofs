---
id: 2312.13061__01
claimed_verdict: disproved
review_verdict: MINOR_GAPS
confidence: high
interpretation_ok: true
references_ok: false
computation_run: true
one_line: The counterexample is correct and Conjecture 4 as stated is disproved — I independently verified every structural hypothesis and the viability of the precoloring by computer, using the paper's actual definition of viability — but the writeup misattributes to the source a "signed weak-dual balance" definition of viability that is not the paper's definition, a gap I had to close myself.
---

## Interpretation

The catalog statement is a verbatim copy of Conjecture 4 of arXiv:2312.13061 (Dvořák,
Moore, Seifrtová, Šámal, "Precoloring extension in planar near-Eulerian-triangulations").
I downloaded the arXiv v1 TeX source and the published journal version (Europ. J. Comb.
127 (2025) 104138, open PDF via the ISTA research explorer): the conjecture and the
definition of "viable" are identical in both, and arXiv has only v1. So there is no
statement drift.

The one term not defined in the catalog excerpt is **viable**. The paper defines it
precisely (Section 2): fix the proper 3-coloring ψ of the near-Eulerian-triangulation G
(the "hue"; unique up to permutation when G is 2-connected, per the paper's remark after
Observation 5, and verified by propagation for the construction here); a 4-coloring φ of
the hued cycle C is *viable* iff the dappled cycle C^φ (hue + color) has a homomorphism
to the dappled triangular grid — equivalently, iff the induced closed walk on the torus
triangulation K_{Z_3} × K_{Z_2^2} is contractible. The paper proves (Corollary 8) that
viability is necessary for extension and explicitly notes it is *not* sufficient in
general; Conjecture 4 asserts that under the stated "genericity" hypotheses it becomes
sufficient.

The writeup's interpretation of every hypothesis is the intended one (I checked each
against the source text): near-Eulerian-triangulation, U independent and disjoint from C
with G−U bipartite, S a set of exactly d faces of length ≥ 6 with the two bulleted
separation conditions, ℓ = 6 even, and the ∀ℓ∃d quantifier structure is handled
correctly (for each candidate d, a counterexample with |S| = d and pairwise face distance
12d+9 > d is produced).

**Is the refutation one a reasonable author would accept?** Yes, as a refutation of the
written statement: the example satisfies every stated hypothesis and the precoloring is
viable under the authors' own definition, yet fails to extend for a trivial local reason
(a vertex of U adjacent to four precolored vertices carrying all four colors). It is,
however, a loophole-style counterexample: nothing in the conjecture constrains the faces
of G−U *outside* S, and the construction plants an extra huge face f of G−U that hugs
the boundary along four consecutive vertices of C. The authors almost certainly had in
mind the regime of their Lemma 26 (all faces of G−U outside S of length four, i.e., a
near-quadrangulation plus a few well-separated long faces); with that extra hypothesis
the construction is excluded and the "intended" conjecture remains open. A reasonable
author would concede the stated conjecture is false and needs reformulation, while
regarding the underlying program as untouched. The writeup itself flags a related caveat
honestly. I therefore count the interpretation as fair: this is a genuine counterexample
to the literal, published Conjecture 4, not a strawman misreading — but the verdict
"Conjecture 4 disproved" should be read with the reformulation remark above.

## Step-by-step findings

| step | label | note |
|---|---|---|
| §1 Viability condition, eq. (1) | ERROR (misattribution; repaired by referee) | The claim "The source's viability condition is the signed balance condition (1)" is false: the source defines viability as existence of a homomorphism of C^φ to the dappled triangular grid (equivalently contractibility on the torus), not eq. (1). Eq. (1) itself *is* a valid necessary condition for extension (the counting derivation given is correct; I verified the weak dual of G is bipartite and the counting identity computationally), but the writeup never proves (1) equivalent to, or even implies, the source's viability. This is the writeup's only real flaw; see §5 row for the repair. |
| §2 Construction of H (subdivided grid + ear) | VALID | Verified by code (k = 1, 2): K bipartite, all cell faces length 12, girth(K) = 12; adding the odd ear A keeps H bipartite; face f has length \|D_0\| (192 for k=1, 360 for k=2), even; dist_K(x,y) = 3 and girth(H) = 6 (computed exactly). |
| §3 Stellation | VALID | Verified by code: every bounded face of G is a triangle (valid plane embedding: every edge on exactly two faces, Euler's formula holds for H and G, G planar and 2-connected); U independent, disjoint from C, G−U = H; every vertex not on C has even degree (apex deg = face length, internal H-vertices deg 2·deg_H); the six C-vertices have odd degrees (5,3,3,7,3,3), confirming eq. (3). So G is a planar near-Eulerian-triangulation. |
| §4 Set S (existence, distances, separators) | VALID | Verified by code: the k selected cell faces have length 12 ≥ 6; min pairwise distance in H is exactly 33 = 3(L−1) for k = 2, matching the writeup's bound 3(L−1) = 12k+9 > k = d; girth 6 ⟹ no 4-cycles at all, and any closed walk of length < 6 has a forest support (≤ 5 edges cannot contain a cycle of length ≥ 6), which cannot separate the plane — so both bulleted hypotheses hold with d = k under any reasonable convention. |
| §5 Viability of (1,2,3,4,3,2) | GAP as written (conclusion true; repaired) | The writeup verifies eq. (1): types (α,γ,α,α,γ,α) — re-derived, correct; sign alternation (7) from odd boundary degrees — verified computationally; \|D_+\| = \|D_-\| (8) via the apex-cycle partition of the weak dual — argument correct and verified (1632 = 1632, 5364 = 5364); the three signed sums are 0 — verified. But because of the §1 misattribution this only establishes (1), not viability. **Repair (referee):** using the paper's actual definitions, the hue on C alternates (bipartition of H, apexes hued 2; uniqueness up to permutation verified by triangle propagation), and the paper's δ-computation gives δ(C) = (0,0); brute force finds the (translation-unique) homomorphism of C^φ into the dappled grid explicitly, e.g. (0,0),(0,1),(1,2),(1,3),(1,2),(0,1). So φ IS viable per the source's definition. |
| §6 Nonextension + quantifiers | VALID | u_f (the apex of face f) is adjacent to c_0,c_1,c_2,c_3 = x,a_1,a_2,y (the boundary of f contains all of A), which carry the four distinct colors 1,2,3,4 — verified in the constructed graph. Hence no color is available for u_f and φ does not extend. Since the family works for every k = d, no d works for ℓ = 6, refuting the ∀ℓ statement. |

## Reference check

- **arXiv:2312.13061 (v1, the only version)** — fetched the full TeX source.
  Conjecture 4 matches the catalog statement verbatim. The definition of *viable*
  (Section 2): "A 4-coloring φ of a connected hued graph C is viable if and only if the
  dappled graph C^φ has a homomorphism to the dappled triangular grid." Also confirmed:
  Corollary 8 (extension ⟹ viable), the torus-contractibility reformulation, the explicit
  σ/δ formulas in the proof of Theorem 7 (which I reused for the independent viability
  computation), the remark that a 2-connected patch's 3-coloring is unique up to
  permutation, and the paper's own warning that "viability is a necessary but of course
  not sufficient condition".
- **Journal version, Europ. J. Comb. 127 (2025) 104138** — fetched the open-access PDF
  (ISTA research explorer) and extracted the text: Conjecture 4 and the viability
  definition are word-for-word identical to arXiv v1. This settles the writeup's own
  caveat about a possibly strengthened journal definition: there is none.
- **Europ. J. Comb. 129 (2025) 104183** — per dblp, an entry with the same title and
  authors (likely a publisher republication); the text is paywalled and I could not
  inspect it. Risk assessed as low given the 104138 text matches arXiv exactly.
- **"The source's viability condition is the signed balance condition (1)"** — DOES NOT
  CHECK OUT. No such formulation appears in the paper; hence `references_ok: false`.
  (The conclusion drawn from it was independently re-established, see above.)
- **Literature search** for any prior resolution of Conjecture 4 (would make this
  ALREADY_KNOWN): none found; the catalog's auto-review (2026-05) likewise found none.

## Computational check

Scripts in `verification/scripts/2312.13061__01/`
(`verify_construction.py`, `verify_hue_unique.py`; Python 3.14 + networkx 3.6.1). All
assertions pass for k = 1 and k = 2. Exact numbers obtained:

- k = 1 (L = 8, m = n = 16): |V(H)| = 1379, |E(H)| = 1635, 257 bounded faces of H
  (256 of length 12, f of length 192), girth(H) = 6; G: 1636 vertices, 4899 edges,
  3264 triangles, planar, 2-connected, Euler count 2; internal degrees all even,
  C-degrees (5,3,3,7,3,3); weak dual bipartite with |D_+| = |D_-| = 1632.
- k = 2 (L = 12, m = 36, n = 24): |V(H)| = 4503, 865 bounded faces (864 of length 12,
  f of length 360); min distance between the two S-faces = 33 = 3(L−1) ≥ d = 2;
  |D_+| = |D_-| = 5364.
- Viability (paper's definition): hue along C alternates ((1,0,1,0,1,0), and the
  propagation script confirms G's 3-coloring is unique up to permutation, so no other
  hue is possible); δ(C) = (0,0); brute force over all base points in a grid chunk finds
  exactly the translation orbit of the homomorphism
  (0,0),(0,1),(1,2),(1,3),(1,2),(0,1) — hues 0,1,0,1,0,1 and colors
  (0,0),(0,1),(1,0),(1,1),(1,0),(0,1) = 1,2,3,4,3,2 as required.
- Nonextension: u_f is adjacent to x,a_1,a_2,y colored 1,2,3,4 — checked in the graph.
- Writeup's auxiliary claims (6)–(8) and the three signed sums of (1): all verified
  (types α,γ,α,α,γ,α; signs +,−,+,−,+,−; all sums 0).

No claimed property failed.

## Caveats

1. **The repaired definition gap.** As written, the proof of viability rests on a
   definition the source does not contain. The counterexample survives only because the
   precoloring happens to also satisfy the paper's actual (homomorphism) definition —
   which the writeup never checks. This is the reason for MINOR_GAPS rather than
   CONFIRMED.
2. **Loophole character.** The hypotheses of Conjecture 4 constrain only the faces in S;
   the construction's extra long face f of G−U (length ≈ perimeter of the grid) touching
   C in four consecutive vertices is what kills extension. Adding the hypothesis "all
   faces of G−U other than the outer face and those in S have length four" (the paper's
   Lemma 26 regime) — or merely forbidding a face of G−U from meeting C in ≥ 4 vertices —
   excludes the counterexample; that repaired conjecture remains open.
3. **Even the stronger necessary condition would not have saved the statement by
   itself:** I checked that φ is also *null-homotopic on C* (the grid walk reduces to a
   point by spur deletions), so replacing "viable" by "viable and null-homotopic on C"
   still would not exclude this example; the failure is only visible to the full
   topological condition of Lemma 25 applied to subgraphs containing the boundary of f.
4. Only ℓ = 6 is treated, which suffices to disprove the ∀ℓ statement; the conjecture
   restricted to other even ℓ is formally untouched (though the same trick plausibly
   generalizes).
5. Convention robustness: face-to-face "distance" (vertex, edge, or dual conventions)
   and "closed walk separating" are not defined in the excerpt; the margins (distance
   33 ≥ 2 for k = 2, and girth 6 versus walks of length ≤ 5 whose supports are forests)
   make every reasonable convention satisfied.
6. The EJC 129 (2025) 104183 duplicate entry could not be inspected (paywall); judged
   low-risk since the accessible journal text matches arXiv v1 verbatim.
7. The grid-size bookkeeping in §2/§4 (whether m × n counts cells or vertices) is
   ambiguous in the writeup; both readings work, and my implementation (vertices
   {0..m} × {0..n}) satisfies all claims with the stated margins.

## Referee summary

The writeup claims to disprove Conjecture 4 of arXiv:2312.13061 by an explicit family of
counterexamples at ℓ = 6: a 3-subdivided grid with an ear attached forming the outer
6-cycle, stellated to a near-Eulerian-triangulation, with d far-apart 12-faces as S and
precoloring (1,2,3,4,3,2). I rebuilt the construction from scratch and verified every
hypothesis and every claimed property computationally (girth, bipartiteness, embedding,
degrees, distances, weak-dual balance), and — crucially — verified that the precoloring
is viable under the paper's actual definition (homomorphism to the dappled triangular
grid), which the writeup replaces by a "signed balance" condition it wrongly attributes
to the source. Since the apex of the large face is adjacent to four boundary vertices
carrying all four colors, the viable precoloring does not extend, so the conjecture as
published (identically in arXiv v1 and EJC 127 (2025) 104138) is false. The single flaw
is the misattributed definition of viability, a gap that is real but repairable and here
repaired and machine-checked; hence MINOR_GAPS with high confidence rather than
CONFIRMED. Reviewers should note the counterexample exploits the conjecture's failure to
constrain faces of G−U outside S, and a strengthened formulation (e.g., all other faces
of length four) remains open.
