---
id: geodesic_cycles_and_tuttes_theorem
leg: attacks_opg
claimed_verdict: disproved
review_verdict: CONFIRMED
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The eight-vertex Kleetope of K4 really is a counterexample to Georgakopoulos–Sprüssel Problem 3 — every step of the writeup checks out, and an exact QF_LRA decision procedure (z3) proves UNSAT, i.e. no positive edge-length assignment on this graph makes all geodesic cycles peripheral.
---

## Interpretation

The writeup uses exactly the definitions of the source. I retrieved the published
Georgakopoulos–Sprüssel paper (arXiv:0911.3999, *Geodetic topological cycles in locally
finite graphs*, Electron. J. Combin. 16 (2009) #R144) and checked the wording verbatim:

* §3.1: "A cycle `C` in `G` is ℓ-geodetic, if for any `x, y ∈ V(C)` there is no `x–y`
  path in `G` of length strictly less than that of each of the two `x–y` paths on `C`."
  This is precisely the writeup's reading: `C` is geodesic iff `d_ℓ(x,y) = d_C(x,y) =
  min(arc1, arc2)` for all pairs of **vertices** of `C`. Strictness of the inequality
  (ties do not destroy geodesicity) is used by the writeup and is the source's convention.
* §5: "Call a cycle in a finite graph peripheral, if it is induced and non-separating."
  The writeup's "induced, and `G − V(C)` connected" is the same, and is also the
  definition OPG points to (Wikipedia / Tutte).
* §5, Problem 3, verbatim: "If `G` is a 3-connected finite graph, is there an assignment
  of lengths ℓ to the edges of `G`, such that every ℓ-geodetic cycle is peripheral? We
  were not able to give an answer to this problem."

So the writeup refutes the problem as its authors posed it, with the intended
quantifier order (∃ℓ ∀ geodesic cycles), over arbitrary positive real lengths, and with
"cycle" meaning a circuit of the finite graph. This is **not** an "as literally stated"
strawman: a reasonable author of the original problem would consider Problem 3 answered
in the negative. Note the writeup correctly refrains from claiming anything about Tutte's
theorem itself; only the proposed route to a new proof of it is blocked.

One convention worth recording (see Caveats): GS's §2 *topological* notion of an
ℓ-geodetic **circle** quantifies over all *points* of `C`, not just vertices. For finite
graphs the relevant definition is the §3.1 one (vertices), which is also the one quoted on
the OPG page ("for every two vertices `x,y` on `C`"), and which the writeup uses.

## Step-by-step findings

`G`: `B = {b1..b4}` induces a `K4`, `S = {s1..s4}` independent, `s_i ~ B \ {b_i}`. This is
the Kleetope of the tetrahedron (triakis-tetrahedron graph), 8 vertices, 18 edges.

| # | step | label | note |
|---|------|-------|------|
| 1 | Definition of peripheral (induced + non-separating) | VALID | matches GS §5 verbatim |
| 2 | Construction of `G`; "insert a vertex in every face of a tetrahedron" | VALID | the planar description agrees with the algebraic one: `s_i` sits in the face opposite `b_i`; 8−18+12=2 |
| 3 | `G` is 3-connected (deleting ≤2 vertices leaves ≥2 adjacent `b`'s, and every surviving `s_i` keeps a neighbour) | VALID | verified: `node_connectivity = 3` |
| 4 | `dim_F2 C(G) = 18 − 8 + 1 = 11` | VALID | arithmetic re-derived; `G` connected |
| 5 | Every induced cycle of `G` is a triangle (an induced cycle of length ≥4 cannot use any `s_i`, since its two cycle-neighbours lie in the clique `B`; and a ≥4-cycle inside `B` has a chord) | VALID | brute force: exactly 16 induced cycles, all triangles, out of 239 simple cycles |
| 6 | The four core triangles `T_i = G[B \ {b_i}]` are induced but **not** peripheral (`s_i` is isolated in `G − V(T_i)`) | VALID | verified for all four |
| 7 | The twelve triangles `P_{i;jk} = s_i b_j b_k` are peripheral | VALID | verified; they are exactly the 12 faces of the planar embedding |
| 8 | `G` has exactly 12 peripheral cycles, each containing exactly one core edge; each core edge lies in exactly two of them | VALID | verified by incidence count (core edge → 2 faces; spoke edge → 2 faces) |
| 9 | Fact 1: for any positive ℓ the ℓ-geodesic cycles generate `C(G)` (shortcut `Q` internally disjoint from `C`, `C = C1 △ C2`, both shorter, induct) | VALID | this is GS Theorem 3.1, whose published proof is the same argument; the "every excursion of `P` can be replaced by a no-longer arc of `C`" sentence is the source's own "it is easy to see" step |
| 10 | Fact 2: an ℓ with the property can be perturbed to one with the property **and** unique shortest paths | VALID | the finitely many witness inequalities `ℓ(P) < arc1`, `ℓ(P) < arc2` are strict, hence hold on an open neighbourhood; equalities `ℓ(P) = ℓ(Q)` between distinct simple paths with the same ends are proper hyperplanes (distinct simple paths have distinct edge sets — the writeup does not say this, a one-line omission), whose union has empty interior. Crucially the writeup only needs "every non-peripheral cycle stays non-geodesic", which is exactly what the open conditions give; it does not need peripheral cycles to stay geodesic, and it says so. |
| 11 | (1) At most one peripheral triangle is non-geodesic (12 spanning vectors in dimension 11) | VALID | verified: the 12 peripheral cycles have GF(2)-rank 11, and **every** choice of 10 of them has rank exactly 10, so two failures already break generation |
| 12 | If a core edge `e = b_jb_k` is non-tight then `P_{p;jk}` and `P_{q;jk}` cannot both be geodesic (else both 2-paths would be shortest `b_j`–`b_k` paths, contradicting uniqueness) | VALID | re-derived: geodesicity at the pair `(b_j,b_k)` forces `d = min(ℓ(e), 2-path)`; `d < ℓ(e)` forces `d =` the 2-path |
| 13 | (2) At most one core edge is non-tight | VALID | each non-tight core edge kills a *different* peripheral triangle by step 8, and (1) allows at most one |
| 14 | Some core triangle `T_i` has all three edges tight | VALID | verified: the minimum number of edges of `K4` meeting all four of its triangles is 2, so one exceptional edge cannot hit every core triangle |
| 15 | An all-tight triangle is geodesic | VALID | for each pair, `d(x,y) = ℓ(xy) ≥ min(arcs)`, so nothing is strictly shorter than both arcs |
| 16 | Contradiction: `T_i` is geodesic and not peripheral | VALID | closes the proof |
| 17 | Closing remarks (planar, simple, 3-connected; self-contained; novelty unchecked) | VALID | all three adjectives verified; the novelty caveat is honest |

No step is labelled GAP or ERROR. The only blemishes are stylistic: the internally-disjoint
shortcut in Fact 1 and the properness of the hyperplanes in Fact 2 are asserted rather than
proved, both being one-liners and the former being the source paper's own phrasing.

## Reference check

* **[GS] arXiv:0911.3999 / Electron. J. Combin. 16 (2009) #R144** — fetched and converted
  to text. Confirmed: the definition of ℓ-geodetic cycle (§3.1) as used; **Theorem 3.1**
  ("For every finite graph `G` and every metric representation `(|G|,ℓ)`, every cycle `C`
  of `G` can be written as a sum of ℓ-geodetic cycles of length at most `ℓ(C)`"), which is
  the writeup's Fact 1 in a slightly stronger form; the definition of peripheral (§5); and
  **Problem 3** verbatim, together with "We were not able to give an answer to this
  problem" and the remark that a positive answer would reprove Tutte's theorem. Also
  confirmed: "any assignment of edge lengths yields a metric representation" for finite
  graphs, so no hidden restriction on ℓ.
* **[T] Tutte, "How to draw a graph", Proc. LMS 13 (1963) 743–768** — invoked only as
  background (peripheral cycles generate the cycle space of a 3-connected graph); used
  nowhere in the proof. Consistent with the computation (the 12 peripheral cycles of `G`
  do have rank 11).
* **OPG entry** — fetched; statement identical, no comment or update announcing a
  solution or counterexample.
* **Novelty** — web searches (OPG, arXiv, Georgakopoulos's page, follow-ups on peripheral
  cycles) surfaced no published counterexample to Problem 3, in agreement with the catalog
  page's 2026 literature review. The model itself flags that it did not check novelty. I
  found no reason to call this ALREADY_KNOWN, but "not found" is weaker than "not there".

## Computational check

Scripts in `verification_astra/scripts/geodesic_cycles_and_tuttes_theorem/`
(run with system `python3`, networkx 3.6.1, z3 4.16.0).

**`check_graph.py`** — structure of `G`:
`n = 8`, `m = 18`, degrees `b_i = 6`, `s_i = 3`; `node_connectivity = 3`; planar = True;
`dim C(G) = 11`; 239 simple cycles (16 triangles, 33 C4, 60 C5, 76 C6, 48 C7, 6 C8);
**16 induced cycles, all triangles**; **12 peripheral cycles**, exactly the
`{b_j, b_k, s_i}` triangles; the four `{b_i,b_j,b_k}` triangles are induced but not
peripheral. GF(2)-rank of the 12 peripheral cycles = 11; the maximum rank of any 10 of
them = 10 (so at most one may fail to be geodesic). All of these match the writeup exactly.

**`proof_lemmas.py`** — each peripheral triangle contains exactly one core edge; each core
edge and each spoke edge lies in exactly two peripheral triangles; the minimum number of
`K4`-edges meeting all four core triangles is 2.

**`z3_decide_lean.py`** — the decisive test. Exact QF_LRA encoding of
"∃ ℓ: E → ℝ_{>0} such that every ℓ-geodesic cycle is peripheral": length variables
`l_e > 0`, distance variables with the Bellman characterisation (`d ≤` every relaxation,
and equality attained at some predecessor — for positive lengths this forces the true
distance, and true distances always satisfy it, so the encoding cannot spuriously
over-constrain), and, for each of the **227 non-peripheral cycles**, the disjunction over
vertex pairs `x,y ∈ C` of `d(x,y) < arc1 ∧ d(x,y) < arc2`.
**Result: `unsat`.** Since linear real arithmetic is decided exactly (no floating point),
this is a machine proof that *no* positive real length assignment on `G` makes every
geodesic cycle peripheral — the writeup's theorem, obtained independently of its argument.

**`z3_controls.py`** — positive controls for that encoding, to rule out an encoding bug
producing a vacuous `unsat`. Same code returns `sat` for `K4`, `K5`, the cube `Q3`, the
triangular prism, the octahedron and the wheel `W4`, and in every case the returned
rational length vector was re-checked independently with Dijkstra: 0 non-peripheral
geodesic cycles. E.g. `K4` with `l(01)=l(12)=l(13)=1/8`, `l(02)=l(03)=l(23)=3/8`.

**`z3_variants.py`** — robustness of the `unsat` to the definition of "peripheral" on the
same graph `G`: standard (induced + non-separating, 12 cycles) → `unsat`; "non-separating
only" (120 cycles) → `sat`; "induced only" (16 cycles) → `sat`. So the counterexample
lives exactly on the standard definition, and specifically on the core triangles being
induced but separating — which is the mechanism the writeup identifies.

**`random_search.py`** — 40 000 random assignments over four distributions (uniform,
log-uniform over `e^{±8}`, discrete-ratio, exponential): the number of non-peripheral
geodesic cycles was never 0; its distribution was `{2: 42, 3: 893, 4: 4784, 5: 9210,
6: 11645, 7: 10075, 8: 3129, 9: 222}`, minimum 2. Simulated annealing (20 000 steps on
log-lengths) got stuck at 4. In 3 000 samples the number of non-geodesic faces was always
≥ the number of non-tight core edges, corroborating step 12–13.

(`z3_decide.py`, a second encoding that enumerates all simple paths explicitly, is correct
but blows up — aborted after ~25 min; it is kept only for reference and is superseded by
`z3_decide_lean.py`.)

## Caveats

1. **Definition sensitivity (not a flaw, but load-bearing).** The refutation needs
   "peripheral = induced *and* non-separating". Under either half alone the same graph
   admits valid assignments (explicit rational models produced above). The used definition
   is GS's own, so this is fine — but any restatement of the result must keep it.
2. **Vertices vs points.** GS's topological definition for *circles* (§2) quantifies over
   all points of `C`; for finite graphs, Problem 3 lives under the §3.1 vertex definition
   (also OPG's phrasing). Step 15 ("an all-tight triangle is geodesic") is a vertex-level
   statement and would need re-examination under a point-level reading. This is not the
   intended reading, but the writeup never remarks on the distinction.
3. **Minimality is neither claimed nor established.** Eight vertices is small but no
   smaller counterexample is excluded; my controls show `K4`, `K5`, `Q3`, the prism, the
   octahedron and `W4` are *not* counterexamples, which is consistent but not a proof of
   minimality.
4. **Novelty unverified by the author** (it says so). My searches found nothing, but the
   topic is niche; a referee should still ask the authors of [GS] whether this example was
   known to them. If it were known folklore, the verdict would move to ALREADY_KNOWN.
5. **Small omissions** in Facts 1–2 (internally-disjoint shortcut; properness of the
   hyperplanes `ℓ(P) = ℓ(Q)`), both one-line repairs, neither affecting correctness.
6. **Scope.** The result kills the proposed route to a new proof of Tutte's theorem via
   geodesic cycles for this graph; it says nothing against Tutte's theorem, and the
   writeup does not pretend otherwise. It also leaves open the natural weakening (which
   graphs do admit such an ℓ?) and the infinite version of Problem 3 mentioned in [GS].
7. **Cost of a wrong encoding.** My `unsat` depends on my own model of the problem; I
   guarded against that with six positive controls and two relaxed variants on the same
   graph that return `sat`, plus 40 000 randomized trials that agree with `unsat`.

## Referee summary

I set out to break this writeup and could not. The graph is the Kleetope of `K4`
(tetrahedron with a vertex stacked in each face); every structural claim about it —
3-connectivity, 18 edges, cycle-space dimension 11, "all induced cycles are triangles",
the split into 4 separating core triangles and 12 peripheral face triangles, the
one-core-edge-per-face incidence — is verified by brute force and matches the text
exactly. The argument is a clean two-branch squeeze: with unique shortest paths (obtained
by an open-condition perturbation that only needs the *non-peripheral* cycles to stay
non-geodesic, a point the writeup makes explicitly and correctly), each non-tight core
edge kills a distinct face, but at most one face may be non-geodesic since 12 face
vectors in an 11-dimensional cycle space tolerate only one loss; hence ≥5 core edges are
tight, hence some core triangle is all-tight, hence geodesic, hence a non-peripheral
geodesic cycle. Every cited ingredient checks out against the published source (GS
Theorem 3.1 and Problem 3, quoted verbatim), and the interpretation is the intended one
rather than a literal-reading strawman. Independently of the argument, an exact z3
decision procedure over linear real arithmetic returns `unsat` for "∃ℓ>0 with every
ℓ-geodesic cycle peripheral" on this graph, while returning verified `sat` models on six
control graphs and on the same graph under two weakened notions of peripheral; 40 000
random assignments never got below 2 non-peripheral geodesic cycles. Verdict: CONFIRMED,
with the single reservation that novelty against the literature has not been established
(nothing found, but the topic is niche), and the two cosmetic gaps noted above.
