---
id: three_chromatic_0_2_graphs
leg: attacks_opg
claimed_verdict: proved
review_verdict: ALREADY_KNOWN
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The proof is correct — I could not break any step, and exhaustive enumeration of all (0,2)-graphs on at most 9 vertices (all graphs, 63 of them), all connected ones up to 14 vertices, and 500+ cube-like (0,2)-graphs up to 64 vertices found chi in {1,2,4} only and confirmed the load-bearing lemma every time — but the identical theorem, with the same two-lemma architecture (unique-4-cycle matching plus "square-closed edge label is a gradient" via a divergence argument), was posted to arXiv as 2607.10125 (Christopher Williamson, 11 July 2026), two months before this attack.
---

## Interpretation

**Definition check (done first, as required).** I fetched the live OpenProblemGarden
entry <http://www.openproblemgarden.org/op/three_chromatic_0_2_graphs>. It gives
verbatim: *"A (0,2)-graph is a graph such that every pair of distinct vertices has
either 0 or 2 common neighbours"*, and the question *"Are there any (0,2)-graphs with
chromatic number exactly three?"*. The writeup uses exactly this definition — the
condition is imposed on **all** pairs of distinct vertices, adjacent ones included,
which is the only reading OPG supports and the one the writeup uses (its §1 applies the
condition to the pair `{v,a}` where `a` may or may not be adjacent to `v`). No
interpretation gaming here.

**Finiteness.** The writeup restricts to finite simple graphs. This is not a weakening
of the intended question: the live OPG page carries a comment (confirmed by my fetch,
and independently by the arXiv note discussed below) that an **infinite** three-chromatic
(0,2)-graph can be constructed, so the open question has always been the finite one.
The writeup's verdict block states the finiteness caveat explicitly. Interpretation is
fair; a reasonable author of the original problem would consider this the intended
statement.

**Faithfulness of the reduction.** "chi(G) = 3" means 3-colourable and not bipartite.
The writeup proves "3-colourable ⟹ bipartite", which is exactly equivalent to "no
finite (0,2)-graph has chi exactly 3". No gap between the theorem proved and the
question asked.

## Step-by-step findings

I numbered every assertion in the writeup. I re-derived each one independently; I did
not find a single step that fails.

| step | label | note |
|---|---|---|
| S1. For an edge `uv` and `a ∈ A = N(u)\{v}`, the pair `{v,a}` has `u` as a common neighbour, hence exactly two; define `φ(a)=b` = the other one. | VALID | `a ≠ v` since `a ∈ N(u)\{v}`, so `{v,a}` is a pair of *distinct* vertices and the (0,2) condition applies; `u ∈ N(v) ∩ N(a)` is nonempty, so the count is 2, not 0. The second common neighbour is unique. |
| S2. `b ∈ B = N(v)\{u}`, `ab ∈ E`, and `u,v,b,a,u` is a quadrangle on four distinct vertices. | VALID | `b ∈ N(v)`, `b ≠ u` by construction; `b ∈ N(a)` gives `ab ∈ E`; `b ≠ a` (no loops, so `a ∉ N(a)`); `b ≠ v` (`b ∈ N(v)`); `a ≠ v`, `a ≠ u`, `u ≠ v`. So four distinct vertices and the four edges `uv, vb, ba, au` all exist. |
| S3. `φ` is a bijection `A → B`, with inverse "take the common neighbour of `u,b` other than `v`". | VALID | `v` and `a` are both common neighbours of `u` and `b`, they are distinct, and `u ≠ b`, so `N(u) ∩ N(b) = {v,a}` exactly (the count is 0 or 2 and we exhibited 2). Hence the reverse map sends `b ↦ a`, lands in `A`, and is a two-sided inverse. |
| S4. Adjacent vertices have equal degrees, hence components are regular. | VALID | Immediate from the bijection. (Not used later; the writeup says so.) |
| S5. Definitions of antisymmetric / square-closed edge functions. | VALID | Definition only. See caveat C2 on the meaning of "quadrangle". |
| S6. `Σ_x div ω(x) = 0` for antisymmetric `ω`. | VALID | Each edge `{x,y}` contributes `ω(x,y)+ω(y,x)=0`. |
| S7. On a finite connected graph, the image of the Laplacian is the space of zero-sum functions; its kernel is the constants. | VALID | Standard. With `Δh(x) = Σ_{y∈N(x)}(h(y)-h(x))` we have `Δ = -(D-A)`, symmetric, and `⟨h,-Δh⟩ = Σ_{xy∈E}(h(x)-h(y))²`, which vanishes iff `h` is constant on the (connected) graph. So `im Δ = (ker Δ)^⊥ = 1^⊥`. The writeup's own one-line justification is exactly this. |
| S8. Hence `h` exists with `Δh = div ω`; set `η = ω - dh`; then `η` is antisymmetric, square-closed and divergence-free. | VALID | `div ω` is zero-sum by S6, so it lies in `im Δ`. `dh(x,y)=h(y)-h(x)` is antisymmetric, telescopes to 0 around every closed walk (hence square-closed), and `div(dh) = Δh`, so `div η = div ω - Δh = 0`. |
| S9. If `η ≠ 0`, let `M = max η > 0` over ordered edges, attained at `uv`; for `a ∈ A`, `b=φ(a)`, square-closedness gives `η(u,v)+η(v,b)-η(a,b)-η(u,a)=0`. | VALID | The max over the finite set of ordered edges exists; antisymmetry forces `M > 0` if `η ≠ 0`. The identity is the quadrangle `u→v→b→a→u` of S2, with `η(b,a)=-η(a,b)` and `η(a,u)=-η(u,a)`. |
| S10. Therefore `η(v,b) - η(u,a) = η(a,b) - M ≤ 0`; summing over the matching gives `Σ_{b∈B} η(v,b) ≤ Σ_{a∈A} η(u,a)`. | VALID | `η(a,b) ≤ M` by maximality. Summation is legitimate precisely because `φ` is a **bijection** `A → B` (S3) — this is where the (0,2) hypothesis pays. |
| S11. `Σ_{b∈B} η(v,b) = -η(v,u) = M` and `Σ_{a∈A} η(u,a) = -η(u,v) = -M`. | VALID | `N(v) = B ⊔ {u}` and `div η(v) = 0` give the first; `N(u) = A ⊔ {v}` and `div η(u) = 0` give the second. |
| S12. Contradiction `M ≤ -M`; hence `η ≡ 0` and `ω = dh`. | VALID | `M > 0` contradicts `2M ≤ 0`. Lemma proved. |
| S13. From a proper 3-colouring `c : V → Z/3`, `ω(x,y)` is the unique element of `{-1,1}` congruent to `c(y)-c(x)` mod 3; well defined and antisymmetric. | VALID | On an edge `c(x) ≠ c(y)`, so `c(y)-c(x) ∈ {1,2} mod 3`, matched by `+1` and `-1` respectively; uniqueness because `1 ≢ -1 (mod 3)`. Antisymmetry is immediate. |
| S14. The sum of `ω` around any quadrangle is divisible by 3 and is an even integer in `[-4,4]`, hence 0; so `ω` is square-closed. | VALID | Telescoping of `c` mod 3 around a closed walk gives divisibility by 3; four summands from `{-1,1}` give a sum in `{-4,-2,0,2,4}`. The only common value is 0. (This is the step that makes the whole argument specific to **three** colours: with 5 colours the analogue would give a sum in `{-8,…,8}` divisible by 5, which does not force 0.) |
| S15. The Lemma gives `h` with `h(y)-h(x) = ω(x,y) ∈ {-1,1}` on every edge; normalising `h(r)=0` makes `h` integer-valued and adjacent vertices have opposite parities. | VALID | Connectivity plus unit steps gives integrality by induction along paths from `r`; `h(y) ≡ h(x)+1 (mod 2)` on each edge. |
| S16. `x ↦ h(x) mod 2` is a proper 2-colouring; applying this to each component makes `G` bipartite; hence no finite (0,2)-graph has chi exactly 3. | VALID | A graph is bipartite iff every component is. Disconnected graphs are handled explicitly and correctly (note also that a disjoint union of (0,2)-graphs is again a (0,2)-graph, since vertices in different components have 0 common neighbours — so the reduction to components is sound in both directions). |

No step was labelled GAP or ERROR. I specifically attacked the failure modes flagged in
my brief: (i) **disconnected graphs** — handled, and I verified computationally that
disconnected (0,2)-graphs really do occur (`K_4 ⊔ K_4`, `C_4 ⊔ K_4`, isolated vertices
attached to anything) and none is 3-chromatic; (ii) **small cases** — `K_1`, `K_2`, the
edgeless graph all behave (the Lemma is vacuous/trivial there, and `chi ≤ 2`);
(iii) **a parity argument needing regularity** — the writeup deliberately does *not*
use regularity; it uses the stronger edge-local matching, and S10 shows why regularity
alone would be insufficient (one needs the *pairing* `a ↔ b` with `ab ∈ E`, not just
`|A| = |B|`); (iv) **local-to-global promotion** — the step from "each quadrangle" to
"all of `G`" is carried by the discrete maximum principle S9–S12, which is genuinely
global and which I checked term by term.

## Reference check

The writeup invokes **no** named external theorem. Its only external ingredient is the
standard fact about the image and kernel of the graph Laplacian (S7), which it proves in
place, correctly. So there is no misquoted citation to find.

The decisive reference issue is **priority**, which the writeup itself flags as unchecked
("literature priority has not been independently checked"). I checked it:

* **arXiv:2607.10125, "Finite Three-Colourable (0,2)-Graphs Are Bipartite", Christopher
  Williamson, submitted 11 July 2026** — <https://arxiv.org/abs/2607.10125>. I fetched
  both the abstract page and the HTML full text. Its Theorem is verbatim the writeup's
  theorem: *"If G is a finite three-colourable (0,2)-graph, then G is bipartite"*, and it
  states the same corollary that no finite (0,2)-graph has chromatic number three, and
  the same caveat that infinite three-chromatic (0,2)-graphs exist.
  The proof architecture is the same:
  - its **Lemma 5** — *"if `a−u−v` is a path of length two, then there is a unique vertex
    `b` such that `a−u−v−b−a` is a 4-cycle"*, which it describes as giving a bijection
    `N(u)\{v} → N(v)\{u}` — is the writeup's §1 property (1);
  - its **Lemma 6** — *"Suppose `α` is a real edge-label whose sum around every 4-cycle is
    zero. Then there is a function `F : V(G) → R` such that `α = dF`"* — is the writeup's
    §2 Lemma, proved there too by a minimisation/divergence argument ("edge-labels of the
    form `α + df` … of minimum norm");
  - the endgame (build the edge-label from the 3-colouring, conclude all cycles are even)
    is the writeup's §3.
  The attack was run 2026-09-16, two months after that posting.
  The writeup is therefore a rediscovery, not a new result.
* Payan, *On the chromatic number of cube-like graphs*, Discrete Math. **103** (1992)
  271–277 — the reference listed by OPG — covers only the cube-like subclass and is
  correctly *not* used by the writeup.
* Differences worth recording, in the writeup's favour: the arXiv note first proves
  triangle-freeness (its Corollary 4, via a cyclic orientation whose in-degree strictly
  increases along directed edges) and states Lemmas 5–6 only for triangle-free
  (0,2)-graphs. The writeup needs no such reduction — its §1 matching and §2 Lemma are
  proved for arbitrary (0,2)-graphs, with the quadrangle allowed to have chords. I
  verified computationally that this generalisation is sound: the Lemma holds on every
  (0,2)-graph I found that *does* contain triangles (`K_4`, `K_4 ⊔ K_4`, and the
  non-bipartite 8- and 12-vertex examples). So the writeup's proof is a slightly cleaner
  variant of the same argument, but the theorem and the two key ideas are the published
  ones.

## Computational check

Scripts are in `verification_astra/scripts/three_chromatic_0_2_graphs/`
(`enumerate_02.py` — (0,2) test, exact chromatic number by backtracking, and the
cycle-space rank test; `enum_fast.py` — bitset filter over `nauty` `geng` output;
`all_graphs_small.py` — all graphs, connected or not; `big_families.py` — hypercubes and
cube-like (0,2)-graphs from Sidon sets). Everything ran with system `python3`
(networkx 3.6.1, numpy 1.26.4) and `/usr/bin/geng`.

Two things were tested on every graph: (a) the **target claim** — is there a
non-bipartite 3-colourable (0,2)-graph? and (b) the **load-bearing Lemma** — the Lemma
is equivalent to *"the quadrangles span the cycle space over R"*, because the
square-closed antisymmetric functions form the kernel of the quadrangle matrix `Q`
(dimension `m - rank Q`), the gradients form a space of dimension `n - c`, gradients are
always square-closed, and equality of the two spaces holds iff
`rank Q = m - n + c` = the cycle-space dimension. I computed `rank Q` numerically in
every case.

**(1) All graphs on at most 9 vertices (connected or not), exhaustive.**
Scanned 1, 2, 4, 11, 34, 156, 1044, 12346, 274668 graphs for n = 1…9.
Result: **63 (0,2)-graphs**, chromatic numbers seen **{1, 2, 4}** — never 3. Every one
was component-regular, satisfied the writeup's matching property (1) at every edge
(checked edge by edge, both orientations), and satisfied the Lemma
(`rank Q = cycle-space dimension`) exactly. Non-bipartite examples do exist and all have
chi = 4: `K_4` (`C~`), `K_4 ⊔ K_4` (`GQhTQg`), `C_4 ⊔ K_4` (`GCdbCo`), the 8-vertex
4-regular graph `GQzTrg`, and their unions with isolated vertices.

**(2) All connected (0,2)-graphs up to 14 vertices, exhaustive over regular graphs.**
Pruning used (both proved, not assumed): a (0,2)-graph is regular (step S4), and every
vertex `u` has exactly `k(k-1)/2` vertices sharing two neighbours with it (the `k(k-1)`
length-2 paths out of `u` are used 2 per such vertex), so `n-1 ≥ k(k-1)/2` and
`4 | n·k·(k-1)`. Complete list of connected (0,2)-graphs found:

| n | k | graph6 | bipartite | chi | cycle dim | rank Q | Lemma |
|---|---|---|---|---|---|---|---|
| 2 | 1 | `A_` (K_2) | yes | 2 | 0 | 0 | ok |
| 4 | 2 | `C]` (C_4) | yes | 2 | 1 | 1 | ok |
| 4 | 3 | `C~` (K_4) | **no** | **4** | 3 | 3 | ok |
| 8 | 3 | `G?zTb_` (Q_3) | yes | 2 | 5 | 5 | ok |
| 8 | 4 | `GQzTrg` | **no** | **4** | 9 | 9 | ok |
| 12 | 5 | `KCpdQiqZeqEk` | **no** | **4** | 19 | 19 | ok |
| 14 | 4 | `M???FbKickF_U_X_?` | yes | 2 | 15 | 15 | ok |

Graph counts scanned along the way include 1544 (n=12, k=4), 7848 (n=12, k=5), 10778
(n=13, k=4), 88168 (n=14, k=4). **No (0,2)-graph with chi = 3 exists on at most 14
vertices**, and the Lemma held in every single case.

**(3) Larger cube-like (0,2)-graphs, 4 to 64 vertices.** `Cay(Z_2^m, S)` is a
(0,2)-graph exactly when `S` is a Sidon set in `Z_2^m` (the number of common neighbours
of `x ≠ y` is the number of ordered pairs `(s,t) ∈ S²` with `s+t = x+y`, which is 0 or 2
for all `x ≠ y` iff all pairwise sums of distinct elements of `S` are distinct). I ran
**530+ such graphs** for `m = 2..5` (up to 32 vertices), plus the hypercubes `Q_1..Q_6`
(up to 64 vertices, 192 edges). Every one: (0,2) property confirmed by brute force,
matching property (1) confirmed at every edge, `rank Q = cycle dim` exactly (e.g.
`Q_6`: 129 = 129; the 32-vertex 7-valent examples: 81 = 81), chromatic number computed
exactly, and **never 3** — the values seen were 2 and 4.

Nothing failed. The computational check therefore *supports* the writeup rather than
refuting it; there is no FATAL finding.

## Caveats

* **C1 (the real one): priority.** The theorem and its proof strategy were already public
  as arXiv:2607.10125 (11 July 2026), two months before this attack was run. The writeup
  is honest that it did not check ("literature priority has not been independently
  checked"), but the `would_publish: true` flag is not warranted: this is a rediscovery.
* **C2: "quadrangle" is never defined.** In §1 the quadrangle `u,v,b,a` may carry chords
  (`av` or `ub`) when `G` has triangles, so "quadrangle" must mean *any* 4-cycle, not
  *induced* 4-cycle. The proof survives either reading, because §3 establishes the sum-zero
  property for **all** 4-cycles (the mod-3 argument is indifferent to chords) while §2
  only ever uses the particular 4-cycles produced in §1. But a referee should ask for the
  word to be defined; the published note sidesteps the issue by reducing to triangle-free
  graphs first.
* **C3: finiteness is load-bearing and the writeup does not say why.** Finiteness is used
  twice — for the existence of the maximum `M` in S9, and for the Laplacian surjectivity in
  S7/S8 — and it is genuinely necessary: infinite three-chromatic (0,2)-graphs exist (per
  OPG's own comment and the arXiv note). The writeup's "Scope and gaps" section does not
  mention this; it should, since it is the reason the theorem is not simply false.
* **C4: degenerate cases.** `K_1` and the edgeless graph are (0,2)-graphs with chi = 1;
  the writeup covers them ("a one-vertex component is harmless"), and my exhaustive n ≤ 9
  run confirms chi = 1 occurs. `K_2` gives the empty matching and the Lemma's argument
  still runs (the two sums are empty, forcing `M ≤ -M` immediately).
* **C5: connectivity in the Lemma.** The Lemma is stated for connected graphs; §3 applies
  it componentwise, which is correct, and the componentwise reduction is valid because a
  disjoint union of (0,2)-graphs is a (0,2)-graph. Stated correctly by the writeup.
* **C6: the verdict block matches what is proved.** "Every finite 3-colourable
  (0,2)-graph is bipartite, so none has chromatic number exactly three" is exactly S16.
  No overclaim relative to the argument.

## Referee summary

I set out to break this proof and could not. Every one of the sixteen steps checks out
under line-by-line re-derivation: the (0,2) condition really does give, for each edge
`uv`, a *pairing* (not just an equinumerosity) between `N(u)\{v}` and `N(v)\{u}` with
matched vertices adjacent; the discrete maximum principle then converts "sum zero around
every quadrangle" into "gradient" without any hidden step — the sum in S10 is legitimate
exactly because the map is a bijection, and the divergence identities in S11 close the
contradiction cleanly; and the mod-3 / parity argument in S13–S14 is the genuinely
3-specific ingredient (it demonstrably does not generalise to 5 colours, which is
consistent with the known existence of 5-chromatic (0,2)-graphs). The computational
check corroborates rather than refutes: exhaustively, there are 63 (0,2)-graphs on at
most 9 vertices (all graphs, disconnected included) and 7 connected ones on at most 14
vertices, with chromatic numbers only in {1,2,4}, and the load-bearing lemma — quadrangles
spanning the cycle space over R — held numerically on all of these plus 530+ cube-like
(0,2)-graphs of up to 64 vertices. The one thing that sinks the `would_publish` claim is
priority: the identical theorem, with the same unique-4-cycle matching lemma and the same
"square-closed edge label is a gradient" lemma proved by the same divergence/minimisation
route, appeared as arXiv:2607.10125 (Christopher Williamson) on 11 July 2026, two months
before this attack. The writeup's mathematics is sound and its variant is marginally more
general (it needs no triangle-free reduction), but the result is already in the
literature, so the verdict is ALREADY_KNOWN rather than CONFIRMED.
