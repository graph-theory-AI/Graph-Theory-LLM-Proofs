---
id: mixing_circular_colourings_0
leg: attacks_opg
claimed_verdict: proved
review_verdict: MINOR_GAPS
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The argument (difference-constraint encoding of orientation classes + a Farey-type bound on zero-weight cycles) is sound and survived a full re-implementation against brute force on 360+ parameter pairs; the only real omission is that the writeup adopts a mixing convention and an unrestricted infimum taken from OPG's truncated rendering of Brewster-Noel Definition 1.2 without checking they agree with the source's "inf{r in Q : r >= chi_c(G) ...}" - they do, so the theorem stands as stated.
---

## Interpretation

**Source definitions (verified against the actual paper, arXiv:1412.3493, §1, Definition 1.2):**

> `mc(G) := inf{k/q ∈ Q : k/q ≥ χc(G) and G is (k, q)-mixing}`
> `Mc(G) := inf{r ∈ Q : r ≥ χc(G) and G is (k, q)-mixing for all k/q ≥ r}`

and, earlier in §1,

> "Given graphs G and H such that G → H, define the H-colour graph of G, denoted C_H(G), to be the graph on vertex set HOM(G,H) where f ∼ g if f(v) ≠ g(v) for exactly one v ∈ V(G). The graph G is said to be H-mixing if C_H(G) is connected." … "Thus, G is k-mixing or (k, q)-mixing if the corresponding colour graph is connected."

Two conventions therefore matter, and the OpenProblemGarden rendering in `prompt.md` **drops** the clause `r ≥ χc(G)` from the definition of `Mc`. The writeup follows OPG, and compensates by declaring (§0) that "mixing means that this graph is nonempty and connected", and by taking the infimum over all rationals `ℓ`.

I checked that the two readings define the same number, which the writeup does **not** do:

* Let `S_src = {r ∈ Q : r ≥ χc(G) and ∀(k,q) with k/q ≥ r, C_{k,q}(G) is connected}`; let `S_wr = {r ∈ Q : ∀(k,q) with k/q ≥ r, C_{k,q}(G) is non-empty and connected}`.
* For `r ≥ χc(G)`: `k/q ≥ r ≥ χc(G)` implies `G → G_{k,q}` (standard: `G → G_{k,q} ⟺ k/q ≥ χc(G)`, and `χc` is rational and attained for finite `G`), so non-emptiness is automatic and the two conditions coincide.
* For `r < χc(G)`: `χc(G)` is rational, so there is a rational `k/q ∈ [r, χc(G))`; then `G` has no `(k,q)`-colouring, so `r ∉ S_wr`; and `r ∉ S_src` by the explicit clause. So `S_src = S_wr` and the infima agree.

Hence the writeup's object **is** Brewster–Noel's `Mc(G)`, and OPG's Question ("Is `Mc(G)` always rational?") is the one being answered. The interpretation is fair, not a strawman: the writeup proves a *strictly stronger* statement (reduced numerator ≤ n+1) than mere rationality, and does not lean on any literal-reading loophole. Its one interpretation-driven contortion — the paragraph claiming edgeless graphs would give `Mc = −∞` "if the displayed definition is read literally" — is an artefact of OPG's truncation only; under the real Definition 1.2 an edgeless graph has `χc = 1` and `Mc = 1`, which is rational with numerator `1 ≤ n+1`, so the excluded case is not actually an exception. This is over-caution, not gaming.

Scope note: Brewster–Noel's Question 1 in §7.1 reads "Is the circular mixing threshold **(number)** always rational?", i.e. it covers both `Mc` and `mc`. The writeup only treats `Mc`. (Its machinery does give `mc ∈ E_{n+1}` by the identical argument — the infimum of a finite union of open rational intervals with endpoints in `E_{n+1}` plus a subset of `E_{n+1}` again lies in `E_{n+1}` — but this is not stated or proved.)

Notation used below: `E_N := {a/b : a,b ∈ Z_{>0}, 2b ≤ a ≤ N}` = the (finite) set of rationals `≥ 2` whose *reduced* numerator is at most `N`.

## Step-by-step findings

| # | Step | Label | Note |
|---|------|-------|------|
| 1 | Statement of `E_N`; Theorem `Mc(G) ∈ E_{n+1}`; "reduced numerator ≤ n+1" | VALID | If `a/b ≥ 2` with `a ≤ N`, the reduced numerator is `≤ a ≤ N`. `E_N` is finite, `max E_N = N`. |
| 2 | **Lemma 1**, closure of `P` under coordinatewise min | VALID | With `z = min(x,y)`: if `z_i = x_i` then `z_j − z_i ≤ x_j − x_i ≤ c_ij`; symmetric otherwise. Box constraints preserved. |
| 3 | **Lemma 1**, "blocked ⟹ blocking `j ∈ D`" | VALID | If `x_j = z_j` and `x_i ≥ z_i + 1`, then `z_j − z_i ≥ x_j − (x_i − 1) = c_ij + 1`, contradicting `z ∈ P`. Correctly re-derived. |
| 4 | **Lemma 1**, "all of `D` blocked ⟹ zero-weight cycle" | VALID | Iterating the blocking map `β : D → D` yields a *simple* directed cycle of tight arcs; summing `x_j − x_i = c_ij` around it telescopes to `0 = Σ c`. Contradiction. Descent terminates since `Σ(x_i − z_i)` strictly decreases. Also correct that only *out*-arcs of `i` can block a decrease of `x_i`, and that the lower box bound cannot, since `x_i > z_i ≥ 0`. |
| 5 | §2: `X_D(k,q)` = integer points of the difference system `x_u − x_v ≤ −q`, `x_v − x_u ≤ k − q` (for `u→v` in `D`), `0 ≤ x ≤ k−1` | VALID | Matches the standard `G_{k,q}` definition (`q ≤ \|f(u)−f(v)\| ≤ k−q`, linear not modular). `x_u − x_v ≤ −q` forces `x_u < x_v`, so every feasible point induces *exactly* `D`; conversely every colouring inducing `D` is feasible. Equality of the two sets, hence the partition, is correct. |
| 6 | §2: a simple directed cycle has weight `ak − bq`; zero weight ⟹ `k/q = b/a ∈ E_n` | VALID | `a` arcs of weight `k−q`, `b−a` of weight `−q`, total `a(k−q) − (b−a)q = ak − bq`. `a = 0` gives `−bq < 0 ≠ 0`, so `a ≥ 1`. `b ≤ n` (simple cycle in an `n`-vertex digraph). `k/q ≥ 2` forces `b ≥ 2a`, hence `b/a ∈ E_n`. |
| 7 | **Lemma 2** (`k/q ∉ E_n` ⟹ every non-empty `X_D` is connected by unit recolourings) | VALID | Immediate from 4+6. Unit moves are legal single-vertex recolourings and all intermediates are genuine `(k,q)`-colourings. Verified computationally (see below). |
| 8 | **Lemma 3**: `*`-augmentation encodes `0 ≤ x_i ≤ k−1`; feasibility ⟺ no negative cycle; integrality of shortest-path distances | VALID | `x_* = 0`, arcs `*→i` of weight `k−1` and `i→*` of weight `0` give exactly the box. All vertices reachable from `*`; with integer weights and no negative cycle the distances are finite integers satisfying every constraint, and lie in `[0, k−1]`. Restricting to simple cycles is legitimate (any negative closed walk contains a negative simple cycle). |
| 9 | **Lemma 3**: taxonomy of simple cycles; `*`-free cycles `ak − bq`, `1 ≤ b ≤ s`, `0 ≤ a ≤ b` | VALID | Re-derived. The `a = 0` case (`D` contains a directed cycle) is *always* negative, i.e. a ratio-independent obstruction — so it does not break the claimed constancy. |
| 10 | **Lemma 3**: `*`-cycles have weight `ak − bq − 1` with `0 ≤ b ≤ s−1`, `1 ≤ a ≤ b+1` | VALID | A simple `*`-cycle is `* → i ⇝ j → *`; the internal path has `a'` arcs of weight `k−q` and `b'` of weight `−q` with `a'+b' ≤ s−1`. Setting `a = a'+1`, `b = a'+b'` gives exactly the stated ranges. |
| 11 | **Lemma 3**: the integrality trick `ak − bq − 1 ≥ 0 ⟺ ak − bq > 0 ⟺ k/q > b/a` | VALID | `ak − bq ∈ Z`, so `≥ 1 ⟺ > 0`; `a ≥ 1` so division is legitimate. This is the load-bearing step that removes all dependence on the *scale* of `(k,q)` (the `k−1` box bound is the only place `k` entered non-homogeneously). Verified computationally: the set of feasible orientation classes never depended on the representation of `k/q`. |
| 12 | **Lemma 3** conclusions (1) ratio-only, (2) constant on components of `(2,∞)\E_s` | VALID | All comparison points are `b/a` with `b ≤ s`; if `b/a ≥ 2` then `b/a ∈ E_s`, and if `b/a < 2` the comparison is constantly true on `(2,∞)`. On a component interval no comparison point is interior, so weak and strict comparisons agree and are constant. |
| 13 | §4: definition of `Q_{k,q}(G)` | VALID | Vertex set = non-empty orientation classes; edges = existence of a one-vertex-apart pair. Well defined. |
| 14 | §4: twin-graph test for `D ~ D'` | VALID | If two colourings differ only at `v`, then `D, D'` agree off `v`. The twin graph (`v_0, v_1` non-adjacent, each with `N(v)`; edges at `v_0` oriented by `D`, at `v_1` by `D'`, the rest by their common direction) is simple and loopless on `n+1` vertices, and its feasible points biject with the desired transitions. `x_{v_0} ≠ x_{v_1}` is automatic: `D ≠ D'` means some incident edge is reversed, forcing `x_{v_0} < x_u < x_{v_1}` (or the reverse). So the `n+1` in the theorem is exactly where it comes from. |
| 15 | §4: `R_{k,q}(G)` non-empty+connected ⟺ `Q_{k,q}(G)` non-empty+connected, when `k/q ∉ E_n` | VALID | (⇐) lift a `Q`-path using Lemma 2 inside each class; (⇒) project an `R`-path (consecutive colourings have equal or `Q`-adjacent orientations). Non-emptiness transfers trivially. Verified computationally end-to-end. |
| 16 | **Proposition 4** (mixing constant on each component `I` of `(2,∞)\E_{n+1}`) | VALID | Vertex tests are Lemma-3 tests on `n` vertices, edge tests on `n+1`; `E_n ⊆ E_{n+1}`, so `I` avoids both exceptional sets and `Q_{k,q}(G)` is literally the same finite graph throughout `I`. The `E_n ⊆ E_{n+1}` inclusion is used but not stated; trivial. |
| 17 | §5: palette `C = {0,q,…,nq}` is a clique of `G_{k,q}` when `k/q ≥ n+1` | VALID | `k ≥ (n+1)q` gives `nq ≤ k−q ≤ k−1` (palette inside range) and any two palette colours differ by between `q` and `nq ≤ k−q`. |
| 18 | §5: topological order of the acyclic `D_f` gives an injective palette colouring in `X_{D_f}`; Lemma 2 connects `f` to it | VALID | `D_f` acyclic since colours strictly increase along arcs; assigning increasing palette colours along a topological order reproduces exactly `D_f`. `k/q ≥ n+1 ⟹ k/q ∉ E_n` since every element of `E_n` is `≤ n`. |
| 19 | §5: injective palette maps are mutually reachable; hence `k/q ≥ n+1 ⟹ (k,q)`-mixing | VALID | `n+1` colours vs `n` vertices leaves a free colour at every stage; the "fix one vertex at a time, evict the blocker to a free colour" argument is correct and all intermediates are injective, hence proper. No computational counterexample found. |
| 20 | §6: `2 ∈ B_G` for a graph with an edge | VALID | `(2,1)`-colourings are proper 2-colourings. Non-bipartite: none exist (empty ⟹ not mixing under the stated convention). Bipartite with an edge: every vertex in a non-trivial component is frozen, so `C_{2,1}(G)` has `≥ 2` isolated vertices. Confirmed by brute force. |
| 21 | §6: `B_G ∩ [n+1, ∞) = ∅`; `B_G` is a union of `Q∩I` over selected components plus a subset of `E_{n+1}` | VALID | Direct from 19 and Proposition 4. |
| 22 | §6: `sup B_G ∈ E_{n+1}` | VALID | `B_G ≠ ∅` (`2 ∈ B_G ⊆ E_{n+1}` for `n ≥ 1`) and `B_G ⊆ [2, n+1)`. If the sup is attained it cannot lie inside an included interval (which contains larger rationals), so it lies in `E_{n+1}`; if not attained it is the right endpoint of one of the finitely many included intervals, and since `(n+1,∞)` is excluded that endpoint is finite, hence in `E_{n+1}`. |
| 23 | §6: `Mc(G) = sup B_G` | VALID | Writing `σ = sup B_G ≥ 2`: every rational `ℓ > σ` lies in the defining set (any `k/q ≥ ℓ > σ ≥ 2` is outside `B_G`, so *all* its representations mix); every rational `ℓ < σ` fails it (pick `r ∈ B_G` with `r > ℓ`). Hence `inf = σ` irrespective of the behaviour at `ℓ = σ`. Also `σ ≥ χc(G)`, so the source's extra clause `r ≥ χc(G)` is satisfied (see Interpretation). |
| 24 | "Scope and exceptional cases" (edgeless graphs, non-integrality, non-attainment) | GAP (harmless) | The `Mc = −∞` worry for edgeless graphs is an artefact of OPG's truncated definition; under Brewster–Noel Definition 1.2 (`r ≥ χc(G)`) an edgeless graph has `Mc = 1`. The writeup correctly disclaims integrality and attainment. |

**Summary of labels:** 22 VALID, 1 GAP (step 24, cosmetic), 0 ERROR. The only substantive omission is the unchecked equivalence of conventions described under *Interpretation*; I closed it above, and it does not change the theorem.

## Reference check

The writeup invokes **no external theorem at all** — it is fully self-contained (it deliberately re-proves its own `Mc ≤ n+1` instead of citing Brewster–Noel's sharper `max{(|V|+1)/2, M(G)}`). So the reference check reduces to (a) confirming the problem's own definitions and (b) confirming the problem is still open.

1. **Brewster & Noel, "Mixing Homomorphisms, Recolourings, and Extending Circular Precolourings", arXiv:1412.3493** (fetched, text extracted with `pdftotext`). Confirmed:
   * Definition 1.2 as quoted above, including the clause `r ≥ χc(G)` that OPG drops.
   * `(k,q)`-mixing = `C_{k,q}(G) = C_{G_{k,q}}(G)` connected, defined for `G → H`.
   * **Theorem 4.12**: "For a graph G, `Mc(G) ≤ max{(|V(G)|+1)/2, M(G)}`" — confirmed verbatim, exactly as quoted in `prompt.md`.
   * **§7.1 "Questions for future study", Question 1**: "Is the circular mixing threshold (number) always rational?" — confirmed; also Q2 (integrality) and Q3 (attainment), which the writeup explicitly does *not* claim.
   * Confirmed the `G_{19,7}` remark ("`Mc(G_{19,7}) ≥ 19/2`"). This is a useful independent consistency check on the new theorem: `19/2` has reduced numerator `19 ≤ |V(G_{19,7})| + 1 = 20`, so the claimed bound is *not* contradicted, and it is close to tight.
   * The paper contains no result asserting that `(k,q)`-mixing depends only on `k/q`; its scaling machinery (Lemmas 4.3/4.6/4.11, "lower parents", `(kd,qd)`-flexibility, Prop. 4.8) is Farey-based and strictly weaker than the writeup's Lemma 3.
2. **Brewster, McGuinness, Moore, Noel, arXiv:1508.05573** (dichotomy: poly-time for `2 ≤ p/q < 4`, PSPACE-complete for `p/q ≥ 4`). Fetched; the abstract confirms the dichotomy but says nothing about rationality of `Mc` or ratio-only dependence.
3. **Brewster & Moore, "Characterizing circular colouring mixing for p/q < 4", arXiv:2008.12185 / JGT 2023.** Fetched the HTML version. It gives a wind-based characterization for `2 < p/q < 4` and settles the bipartite `mc = 2` conjecture; it does **not** prove rationality of `Mc`, nor a general local-constancy/finiteness statement.

No citation could be faulted, because none is made; the two definitional facts the writeup silently relies on (`G → G_{k,q} ⟺ k/q ≥ χc(G)`, and `χc` rational/attained for finite graphs) are standard and are stated in the source paper's §1 ("`G_{k',q'} → G_{k,q}` if and only if `k'/q' ≤ k/q`"; "`χc(G) = min{k/q : G → G_{k,q}}`").

**Priority.** I found no source claiming the result. The problem is listed as open in the source paper's §7.1, on OPG, and in the catalog page's 2026-05 literature review. So this is **not** ALREADY_KNOWN on the evidence available; I cannot of course rule out an unindexed preprint.

## Computational check

Scripts in `verification_astra/scripts/mixing_circular_colourings_0/`. All use exact `Fraction` arithmetic and the convention "mixing = reconfiguration graph non-empty and connected".

**(a) `brute.py` — brute-force mixing and the Theorem's prediction.**
Enumerates every `(k,q)`-colouring, builds the reconfiguration graph, tests connectivity, for all `k ≤ K`, `1 ≤ q ≤ k/2`.

| graph | n | `E_{n+1}` | bad ratios (some representation not mixing) | Prop. 4 violations | bad ratio `≥ n+1` |
|---|---|---|---|---|---|
| K2 | 2 | {2,3} | {2} | 0 | none |
| P3 | 3 | {2,3,4} | {2} | 0 | none |
| K3 | 3 | {2,3,4} | all 53 tested rationals in `[2, 23/6]` (`K ≤ 26`), none `≥ 4` | 0 | none |
| P4, C4, star(K_{1,3}) | 4 | {2,5/2,3,4,5} | {2} | 0 | none |
| K4 | 4 | {2,5/2,3,4,5} | all tested rationals in `[2, 9/2]`, none `≥ 5` | 0 | none |
| C5, bull | 5 | {2,5/2,3,4,5,6} | all tested in `[2, 11/3]`, none `≥ 4` | 0 | none |
| K23 | 5 | {2,5/2,3,4,5,6} | {2} | 0 | none |

"Prop. 4 violations" counts ordered pairs of tested ratios lying in the *same* component interval of `(2,∞)\E_{n+1}` with different mixing status: **0 in every case**, over `K ≤ 13` (and `K ≤ 26` for `K3`/`P3`). No ratio was ever representation-dependent in range. No counterexample to §5 (`k/q ≥ n+1 ⟹ mixing`).

Resulting thresholds, all in `E_{n+1}` as the Theorem requires: `Mc(K2)=2` (matches the value quoted on OPG), `Mc(P3)=Mc(P4)=Mc(C4)=Mc(K_{1,3})=Mc(K_{2,3})=2`, `Mc(K3)=4`, `Mc(K4)=5`, `Mc(C5)=Mc(bull)=4`.

**(b) `lemmas.py` — direct tests of Lemmas 1–3 and the quotient criterion.** For `K2, P3, K3, P4, C4, paw, K4` and all `k ≤ 12`:
* Lemma 2 failures (a non-empty class `X_D` disconnected) at `k/q ∉ E_n`: **none**, in any case, under either unit moves or arbitrary single-vertex recolourings.
* Lemma 2 failures at `k/q ∈ E_n`: present exactly as the writeup predicts and needs — e.g. `K2` at `(4,2),(6,3),(8,4),(10,5)` (ratio `2`), `K3` at `(6,2),(9,3),(12,4)` (ratio `3`), `K4` at `(8,2),(12,3)` (ratio `4`), `C4` at ratios `2` and `4`. So `E_n` is genuinely necessary and the writeup is right to quarantine it.
* Quotient-criterion failures (`R` connected `≠` `Q` connected) at `k/q ∉ E_n`: **none**.
* Lemma 3(1) (the set of feasible orientation classes depends only on `k/q`, not on the representation): **no violation**, i.e. the integrality trick of step 11 checks out empirically.
* Lemma 3(2) (that set is constant on component intervals of `(2,∞)\E_{n+1}`): **no violation**.

**(c) `endtoend.py` — decisive test.** I re-implemented the writeup's *algorithm* from scratch: build `Q_{k,q}(G)` using nothing but Bellman–Ford negative-cycle detection on the `*`-augmented difference-constraint digraphs of §3 (class feasibility on `n` vertices, transition feasibility on the `n+1`-vertex twin graph of §4), then answer "non-empty and connected". Compared against brute-force mixing for `K2, P3, K3, P4, C4, paw, K4, diamond, C5, bull, house, K23` and all `k ≤ 11`:

> **360 (k,q) pairs tested; 0 mismatches — including 0 mismatches even at the exceptional ratios in `E_n`, where the theory only promises agreement off `E_n`.**

This simultaneously validates Lemma 1, Lemma 2, Lemma 3 and the §4 quotient reduction as an executable specification.

**(d) `threshold.py` — larger graphs via the validated algorithm** (`k ≤ 16`):

| graph | n | max bad ratio | min good ratio above it | `E_{n+1}` point forced to be the threshold | Prop. 4 violations | rep.-dependent ratios |
|---|---|---|---|---|---|---|
| C6 (= `L_3`) | 6 | 15/4 | 4 | **4** | 0 | none |
| C7 | 7 | 15/4 | 4 | **4** | 0 | none |
| prism (`K_3 □ K_2`) | 6 | 15/4 | 4 | **4** | 0 | none |
| K5 | 5 | 11/2 | 6 | **6** | 0 | none |

Every observed threshold is in `E_{n+1}`, no ratio was representation-dependent, and no bad ratio `≥ n+1` appeared. `Mc(C6) = 4` agrees with Brewster–Noel's `M(L_m) = m+1` combined with their Theorem 4.12 (`Mc(L_3) ≤ max{7/2, 4} = 4`).

**Tightness observation.** `Mc(K_n) = n+1` for `n = 2,3,4,5` (values `3`? no — `2, 4, 5, 6`; note `Mc(K_2) = 2 < 3` is the known `K_2` exception, while `Mc(K_3)=4`, `Mc(K_4)=5`, `Mc(K_5)=6` all equal `n+1`). Hence the §5 bound `Mc ≤ n+1` is attained and the index `n+1` in `E_{n+1}` cannot be lowered to `E_n`: the theorem's constant is sharp in that sense.

**No computational check failed.**

## Caveats

1. **Convention/definition gap (the one real omission).** The writeup adopts (i) "mixing = non-empty *and* connected" and (ii) an infimum over *all* rationals `ℓ`, both inherited from OPG's rendering, which drops Brewster–Noel's clause `r ≥ χc(G)`. It never verifies that this yields the same number as the source definition. It does (proof under *Interpretation*), but the check is load-bearing for the claim's relevance and is missing from the writeup.
2. **Edgeless graphs.** The final paragraph's `Mc = −∞` scenario does not arise under the real definition (`χc = 1`, `Mc = 1`). The theorem's hypothesis "at least one edge" is therefore unnecessary, and the writeup's framing of this as "a trivial normalization issue in the quoted statement" over-dramatizes a non-issue.
3. **`mc` not covered.** Brewster–Noel's Question 1 is phrased for "the circular mixing threshold (number)", i.e. also for `mc(G)`. The writeup silently restricts to `Mc`. The same machinery yields `mc(G) ∈ E_{n+1}` but this is neither stated nor proved.
4. **Nothing about integrality or attainment** — correctly disclaimed in the verdict block's `caveats`. In particular the writeup does **not** answer OPG's companion questions ("Is `Mc` always an integer?", "Is `Mc` attained for non-bipartite graphs?"). Its result is consistent with, and does not settle, the observation that no non-integer example is known. Note that a non-integer value is *permitted* by the theorem (e.g. `19/2` for `G_{19,7}` would be allowed).
5. **`E_n ⊆ E_{n+1}`** is used in Proposition 4 without comment; trivially true.
6. **Simple loopless finite graphs only.** The writeup says "finite loopless"; multigraphs are harmless (parallel edges give duplicate constraints), but loops make the colouring set empty and are correctly excluded. Directed/infinite graphs are out of scope, as they are for the original problem.
7. **The numerator bound is on the *reduced* numerator only.** The statement gives no bound on the denominator, hence no effective bound on the *size* of `Mc(G)` beyond `≤ n+1` (which §5 gives anyway). The writeup does not claim more.
8. **Sharpness of `n+1` vs Brewster–Noel's `max{(|V|+1)/2, M(G)}`.** §5's self-contained bound is much weaker than the published one; this is a deliberate, harmless choice (it keeps the proof independent), but it means the paper does not recover or improve the known bound. Combining the numerator bound with Theorem 4.12 would in fact give a stronger conclusion than either alone.
9. **Verification limits.** All computations are on graphs with `n ≤ 7` and `k ≤ 26`. The lemmas were verified as executable specifications, not proved by machine; the proofs themselves I checked by hand and found sound.

## Referee summary

I set out to break this and could not. The architecture is: (1) partition the `(k,q)`-colourings by the edge-orientation they induce, at which point each class is exactly the integer-point set of a system of difference constraints with arc weights only `−q` and `k−q`; (2) observe that such a system's unit-step graph is connected unless there is a zero-weight simple cycle, which pins `k/q` to a rational `b/a` with `b ≤ n`; (3) observe that *feasibility* of such a system — including the inhomogeneous box `0 ≤ x ≤ k−1` — is a finite boolean combination of comparisons of `k/q` with rationals of numerator `≤ n+1`, the inhomogeneity being killed by the integrality identity `ak − bq − 1 ≥ 0 ⟺ ak − bq > 0`; (4) reduce mixing to connectivity of a quotient graph on orientations whose vertices and edges are exactly such feasibility tests, the edge tests living on an `(n+1)`-vertex twin graph. Every one of these steps re-derived correctly by hand, and I re-implemented the whole pipeline independently and matched brute-force mixing on 360 parameter pairs across 12 graphs with zero mismatches, plus threshold computations on four 5–7-vertex graphs that all landed in `E_{n+1}`. The exceptional set `E_n` is genuinely needed (orientation classes do disconnect at `k/q ∈ E_n` — e.g. `K_4` at `(8,2)` and `(12,3)`), and the writeup correctly quarantines those ratios rather than assuming them away; the bound `n+1` is sharp, since `Mc(K_n) = n+1` for `3 ≤ n ≤ 5`. No supremum is assumed attained anywhere — indeed the argument is carefully built so that the behaviour *at* the exceptional ratios is irrelevant to the supremum, which is exactly the trap the claim type invites. The single genuine defect is that the writeup formalizes `Mc` from OpenProblemGarden's rendering, which truncates Brewster–Noel's Definition 1.2 by dropping the clause `r ≥ χc(G)`, and then patches it with an unverified non-emptiness convention; the two readings do coincide, and I proved they do, but the writeup owes that half-page. Add that, delete the misleading edgeless-graph paragraph, and (optionally) extend the one-line argument to the circular mixing *number* `mc`, and this is a correct and publishable resolution of Brewster–Noel Question 7.1(1) / OPG "Mixing Circular Colourings", strictly stronger than the question asked. **MINOR_GAPS**, high confidence.
