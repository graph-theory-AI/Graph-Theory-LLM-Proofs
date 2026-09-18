---
id: covering_powers_of_cycles_with_equivalence_subgraphs
leg: attacks_opg
claimed_verdict: disproved
review_verdict: CONFIRMED
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The construction and the rank lower bound are both correct and verified by brute force (eq(C_8^3)=eq(C_12^3)=3, eq(C_10^4)=4), so eq(C_n^k)=Theta(log k) and the Omega(k) conjecture is genuinely disproved — but the lower-bound half is a rediscovery of Alon (1986) Thm 1.1/Cor 1.2, and the source literature it contradicts (West's REGS page) contains a false assertion "eq(C_n^k)=k+1 when (k+1)|n" that Alon's own 1986 corollary already refutes.
---

## Interpretation

**Definitions used.** The writeup uses: an *equivalence subgraph* of `G` is a spanning
subgraph whose connected components are cliques of `G`; `eq(G)` is the least number of
such subgraphs whose edge sets cover `E(G)`. This matches the OpenProblemGarden entry
verbatim ("a subgraph `H` of `G` is an equivalence subgraph of `G` if `H` [is] a
disjoint union of cliques... the least number of equivalence subgraphs needed to cover
the edges of `G`"), Alon's 1986 definition ("an equivalence covering of a graph `G` is a
family of equivalence subgraphs of `G` such that every edge of `G` is an edge of at
least one member"), and Esperet–Gimbel–King's ("an equivalence graph is a disjoint union
of cliques, and the equivalence number `eq(G)` ... is the minimum number of equivalence
subgraphs needed to cover the edges of `G`"). The writeup's sentence "All equivalence
subgraphs below may be made spanning by adding isolated vertices" is the correct and
standard reconciliation between the "subgraph" and "equivalence relation on `V`"
formulations. **No definition gaming.**

`C_n^k` is used with the standard convention: `u ~ v` iff their cyclic distance is in
`[1,k]`. This matches West's REGS page ("each vertex adjacent to the closest `k` vertices
in each direction"). No off-by-one: `k+1` consecutive vertices form a clique, `C_n^k = K_n`
iff `n <= 2k+1`.

**Is the refutation of the intended conjecture, or of a strawman?** It is the intended
conjecture. The OPG discussion is explicit that the interesting regime is `n` large
relative to `k` ("even for `n` very large compared to `k`, no upper bound is known beyond
trivial linear bounds of order `Theta(k)`"). The writeup does *not* exploit small `n`:
its bounds hold uniformly for every `n >= 2k+2`, and it exhibits families with
`n/k -> infinity` and `eq/k -> 0` (e.g. `k = 2^q - 1`, `n = 2^q · 2^q`). It also correctly
disposes of the degenerate regime `n <= 2k+1` (complete graph, `eq = 1`), so the claim
covers all `n >= 3`. The result simultaneously answers *both* halves of West's REGS
Problem 1 ("is the value unbounded for fixed `k`?" — no, `eq <= 2r+1` uniformly in `n`;
"is there an upper bound sublinear in `k`?" — yes, `O(log k)`).

An author of the original problem would consider it resolved.

## Step-by-step findings

`s = k+1`, `r = ceil(log2 s)`. Claim: `r+1 <= eq(C_n^k) <= 2r+1` for `n >= 2s`, with
equality `eq = r+1` when `s | n`.

| # | step | label | note |
|---|------|-------|------|
| 0 | Scope: `n <= 2k+1` (and `n>=3`) gives `C_n^k = K_n`, `eq = 1` | VALID | max cyclic distance is `floor(n/2) <= k`, so the graph is complete; `eq(K_n)=1`. |
| 1 | §1 property 1: `x in I_h^1(p)`, `y in I_h^0(p)` implies `x > y` | VALID | They share the first `h-1` bits and differ at bit `h` with `x_h=1 > y_h=0`; lower bits are irrelevant. |
| 2 | §1 property 2: `x > y` implies both lie in a common `(h,p)` pair | VALID | Take `h` = first differing bit position of the `r`-bit representations; `x>y` forces `x_h=1, y_h=0`, and `p` = common prefix. |
| 3 | §2: `H_0` (block cliques) is an equivalence subgraph | VALID | Each block is `s = k+1` cyclically consecutive vertices, hence a clique; blocks partition `V`. |
| 4 | §2: each `Q_{i,h,p}` is a clique | VALID | Same-block pairs: within a block, distance `<= s-1 = k`. Cross pairs `v_{i,x}, v_{i+1,y}`: positions `is+x` and `(i+1)s+y`, clockwise gap `s+y-x <= s-1 = k` by step 1. Crucially, *every* `x` in the 1-part exceeds *every* `y` in the 0-part, which is exactly step 1 — the writeup states this correctly. |
| 5 | §2: at each level `h` the `Q`'s are pairwise vertex-disjoint | VALID | Each `v_{i,x}` lies in exactly one `Q` at level `h`: in `Q_{i,h,p}` if `x_h = 1`, in `Q_{i-1,h,p}` if `x_h = 0`, where `p` is `x`'s length-`(h-1)` prefix. Distinct prefixes give disjoint index sets; the left/right dichotomy is what prevents collisions. Verified by code for all `m(k+1) <= 300`, `k <= 24`. |
| 6 | §2: every edge is covered | VALID | An edge has short arc of length `<= s-1 < s`, so it meets at most two consecutive blocks. Intra-block: `H_0`. Inter-block `v_{i,x} v_{i+1,y}`: adjacency gives `s+y-x <= s-1`, i.e. `x>y`, and step 2 supplies `(h,p)`. Includes the `m=2` case correctly (a pair of blocks is adjacent on both sides, but each orientation is handled by a different index `i`). |
| 7 | §2 conclusion `eq(C_{ms}^{s-1}) <= r+1` | VALID | Exactly `r+1` layers. Empty/singleton `Q`'s (which occur when `s` is not a power of two) are discarded harmlessly. |
| 8 | §3 path-power cover with `r+1` layers | VALID (minor hand-wave) | Same argument with no wraparound. The only under-argued point is "Missing vertices in the final block cause no difficulty": when the last block is short one simply drops the out-of-range local indices, which cannot break cliqueness or disjointness and cannot orphan an edge. One line of prose; I verified it computationally for every `n in [2s, 300]`, `k <= 24`. |
| 9 | §3 wrap cover with `r` layers | VALID | `A = {n-s..n-1}`, `B = {0..s-1}` are disjoint since `n >= 2s`, both cliques. For `a_x = n-s+x`, `b_y = y`, the wrap gap is `s-x+y`, which is `<= k` iff `x>y`; and every wrapping edge indeed has both ends in `A ∪ B` (its endpoints are within `s-1` of the cut). Same disjointness argument, only one block pair involved. |
| 10 | §3 conclusion `eq <= (r+1)+r = 2r+1` | VALID | Layers of the two covers are simply concatenated. Verified for 7390 parameter pairs. |
| 11 | §4: labels give `M_{uv}=0` iff `u=v` or `uv in E` | VALID | Components of a layer are cliques of `G`, so `c_l(u)=c_l(v)` with `u≠v` forces `uv in E`; conversely every edge is covered by some layer. Requires layers to be spanning, which the writeup arranged. |
| 12 | §4 rank bound `rank M <= 2^t` | VALID | `prod_l (c_l(u)-c_l(v)) = sum_{S⊆[t]} (-1)^{t-|S|} a_S(u) a_{[t]\S}(v)`, a sum of `2^t` outer products. Re-derived; the sign convention is right. |
| 13 | §4 triangular minor `N_{ij} = M_{i,(s+j) mod n}`, `0<=i,j<2s` | VALID | Rows `0..2s-1` and columns `s..3s-1 (mod n)` are each distinct because `2s <= n`. For `i>j`: `|s+j-i| <= s-1` so the two vertices are equal or adjacent, giving `N_{ij}=0`. On the diagonal the offset is exactly `s`, with cyclic distance `min(s, n-s) = s > k` since `n >= 2s`, so `N_{ii} ≠ 0`. Hence `rank N = 2s`. |
| 14 | §4 conclusion `t >= ceil(log2(2s)) = r+1` | VALID | `2s <= rank N <= rank M <= 2^t`; `ceil(log2 2s) = 1 + ceil(log2 s)`. Verified numerically (see below). **Not new**: this is Alon 1986, Theorem 1.1, instantiated at the same pair of vertex sequences (see Reference check). |
| 15 | Combination: `eq(C_{ms}^{s-1}) = r+1` for `m>=2`; `eq = Theta(log(k+1))` for all `n>=2k+2` | VALID | `r+1 <= eq <= 2r+1` with `r = ceil(log2(k+1))` is `Theta(log(k+1))` including at `k=1` (`2 <= eq <= 3`). |
| 16 | Verdict-block claim "disproves the `Omega(k)` conjecture" | VALID | `eq/k -> 0` along `k=2^q-1`, `n=m·2^q`, with `n/k -> infinity`. |

No step is labelled GAP or ERROR. The only prose weaknesses are step 8's one-line
dismissal of the short last block and the tacit use of "empty sets are omitted"; both are
genuinely routine and were checked exhaustively by code.

## Reference check

The writeup cites nothing and says so ("No unproved conjecture or external theorem is
used"), so the reference check here is a *prior-art* check. Sources fetched:

1. **OpenProblemGarden entry**
   (http://www.openproblemgarden.org/op/covering_powers_of_cycles_with_equivalence_subgraphs)
   — fetched. Conjecture and discussion are quoted accurately in `prompt.md`; no comments
   have ever been posted on the entry. Its definition of `eq` matches the writeup's.

2. **D. West, "Equivalence covering of cycle-powers" (REGS 2010/2011)**
   (https://dwest.web.illinois.edu/regs/eqcov.html) — fetched in raw form. This is the
   primary source for the problem ("Originators: L. Esperet, J. Gimbel, A. King, presented
   by Andrew King"). It states verbatim:
   > "Any `k+1` consecutive vertices form a clique, and eq(`C_n^k`)=`k+1` when `k+1`
   > divides `n`. Always `2k` is an upper bound. Although no sublinear upper bound
   > construction is known, also no good general lower bound is known."
   and Problem 1: "Determine the asymptotics of eq(`C_n^k`). In particular, is the value
   unbounded for fixed `k`? Is there an upper bound that is sublinear in `k`?"

   **The asserted equality `eq(C_n^k) = k+1` when `(k+1) | n` is false.** My exhaustive
   computation gives `eq(C_8^3) = 3 ≠ 4`, `eq(C_12^3) = 3 ≠ 4`, `eq(C_10^4) = 4 ≠ 5`.
   It is refuted by a 1986 corollary cited on that very page (item 3 below). This is
   almost certainly the origin of the OPG conjecture, and it means the problem was
   "wide open" partly on the strength of an error.

3. **N. Alon, "Covering graphs by the minimum number of equivalence relations",
   Combinatorica 6 (1986) 201–206** — full text retrieved and read
   (https://web.math.princeton.edu/~nalon/PDFS/Publications/...pdf, extracted with
   `pdftotext`). Two items are directly load-bearing for this review:
   - **Theorem 1.1** (verbatim): "Let `G=(V,E)` be a graph and suppose
     `U=(u_1,...,u_s)`, `W=(w_1,...,w_s)` are two (not necessarily disjoint) sequences of
     vertices. If `u_i w_i ∉ E` for all `1<=i<=s` and for all `1<=i<j<=s` either `u_i=w_j`
     or `u_i w_j ∈ E`, then `eq(G) >= log2 s`." Proved by exterior algebra.
     **The writeup's §4 is exactly this theorem**, with a (weaker but sufficient) outer-
     product/rank proof in place of Alon's exterior-algebra proof, applied to
     `u_i = 2s-1-i`, `w_i = (s + 2s-1-i) mod n`, `i=0..2s-1`. I verified by code that
     Alon's hypotheses hold verbatim for that pair of sequences for every tested
     `n = m(k+1)`, `m>=2`, `k<=15`, giving `eq >= log2(2(k+1))`. So §4 is a rediscovery,
     not new mathematics. (The writeup does not claim otherwise; it explicitly says it
     has not checked the literature.)
   - **Corollary 1.2** (verbatim): "Let `T_n` denote the complement of a matching of `n/2`
     edges. Then `eq(T_n) = ceil(log2 n)` for all even `n>=2`." Since
     `C_{2k+2}^k = T_{2k+2}`, this says `eq(C_{2k+2}^k) = ceil(log2(2k+2)) = r+1`,
     i.e. **the `n = 2k+2` case of the writeup's theorem has been known since 1986** —
     and it already contradicts West's `eq = k+1` claim (`k=3`: `3 ≠ 4`).
   Alon's Section 4 "Concluding remarks" contains no statement about cycle powers.

4. **L. Esperet, J. Gimbel, A. King, "Covering line graphs with equivalence relations",
   Discrete Appl. Math. 158 (2010) 1902–1907** — extended abstract retrieved
   (https://imada.sdu.dk/u/btoft/GT2009/esperet.pdf) and text-extracted. Main theorem
   confirmed as `(1/3) log2 log2 χ(G) < eq(L(G)) <= 2 log2 log2 χ(G) + 2`. The paper is
   about line graphs and the orientation covering number `σ(G)`; **it contains nothing
   about `C_n^k`**, so it is not prior art for this claim. The writeup does not cite it.

5. **Post-2011 literature.** Searches for a sublinear upper bound or any resolution of
   West's Problem 1 returned nothing: arXiv:2010.04450 ("A note on the orientation
   covering number") proves `σ(G)=σ(K_{χ(G)})` and does not touch cycle powers;
   arXiv:1608.07723 (Javadi–Hajebi) is about the *edge clique cover* number `cc(C_n^k)=n`,
   a different and larger parameter. This agrees with the catalog page's own 2026 review.

**Conclusion of the reference check:** the *lower bound* and the special case `n = 2k+2`
are classical (Alon 1986). The *upper bound for general `n`* — in particular for
`n >> k`, the regime the conjecture is about — is not in the literature I could find, and
it is what actually refutes the `Omega(k)` conjecture.

## Computational check

Scripts in `verification_astra/scripts/covering_powers_of_cycles_with_equivalence_subgraphs/`
(run with system `python3` 3.x + numpy 1.26.4; networkx not needed):

* `construction_check.py` — re-implements the §2 and §3 constructions from the writeup's
  own definitions and independently verifies, against a freshly built edge set of
  `C_n^k`, that (a) every part is a clique, (b) the parts of a layer are pairwise
  disjoint, (c) the layers cover every edge.
* `brute_force_eq.py` — computes `eq(C_n^k)` **exactly** by enumerating *all* partitions
  of `V` into cliques of `G` and solving the resulting minimum set cover exactly
  (maximal-set reduction + iterative deepening branching on a least-coverable edge).
* `curated_cases.py` — exact `eq` on a curated list, cross-checked against the writeup's
  formula and against West's `eq = k+1` claim.
* `rank_lower_bound.py` — builds the §4 matrix `M` from an actual cover with random real
  labels and checks the zero pattern, `rank M <= 2^t`, the triangularity of the `2s x 2s`
  minor `N` and `rank N = 2s`; also tests Alon's Theorem 1.1 hypothesis on the same
  sequences.
* `witnesses.py` — prints explicit small covers.

**Result 1 — constructions valid (7390 parameter pairs, 0 failures).** §2 verified for
every `n = m(k+1) <= 300` with `m>=2, k<=24`, always using exactly `r+1` layers; §3
verified for every `n in [2k+2, 300]`, `k <= 24`, never exceeding `2r+1` layers.

**Result 2 — exact `eq` by exhaustive search.** (`r+1` = writeup's lower bound / exact
value in the divisible case; `2r+1` = writeup's upper bound.)

| n | k | exact eq | r+1 | 2r+1 | k+1 | (k+1)\|n | |
|---|---|---|-----|------|-----|---------|--|
| 4 | 1 | 2 | 2 | 3 | 2 | yes | ok |
| 5 | 1 | 3 | 2 | 3 | 2 | no | ok |
| 6 | 1 | 2 | 2 | 3 | 2 | yes | ok |
| 7 | 1 | 3 | 2 | 3 | 2 | no | ok |
| 8 | 1 | 2 | 2 | 3 | 2 | yes | ok |
| 9 | 1 | 3 | 2 | 3 | 2 | no | ok |
| 6 | 2 | 3 | 3 | 5 | 3 | yes | ok |
| 7 | 2 | 4 | 3 | 5 | 3 | no | ok |
| 8 | 2 | 3 | 3 | 5 | 3 | no | ok |
| 9 | 2 | 3 | 3 | 5 | 3 | yes | ok |
| 10 | 2 | 3 | 3 | 5 | 3 | no | ok |
| 11 | 2 | 3 | 3 | 5 | 3 | no | ok |
| 12 | 2 | 3 | 3 | 5 | 3 | yes | ok |
| **8** | **3** | **3** | **3** | 5 | **4** | yes | **West's eq=k+1 refuted** |
| 9 | 3 | 4 | 3 | 5 | 4 | no | ok |
| 10 | 3 | 4 | 3 | 5 | 4 | no | ok |
| 11 | 3 | 4 | 3 | 5 | 4 | no | ok |
| **12** | **3** | **3** | **3** | 5 | **4** | yes | **West's eq=k+1 refuted** |
| **10** | **4** | **4** | **4** | 7 | **5** | yes | **West's eq=k+1 refuted** |
| 11 | 4 | 4 | 4 | 7 | 5 | no | ok |

Every value lies in `[r+1, 2r+1]`; **every divisible case equals `r+1` exactly**, as the
writeup claims, and never equals `k+1` when `k >= 3`. Cases with `n >= 12` and `k >= 4`
exceeded the enumeration budget (the number of clique partitions explodes) and were not
completed; they are not needed, since the upper bound is constructive and the lower bound
is Alon's theorem.

Note that `n=12, k=3` is an `m=3` case — it is *not* covered by Alon's Corollary 1.2, so
the new regime of the writeup's theorem is independently confirmed by exhaustive search.

**Result 3 — explicit witnesses** (all machine-verified to be equivalence covers):

```
C_8^3  (k+1 = 4, 2k = 6), 3 layers:
  {0,1,2,3} {4,5,6,7}
  {2,3,4,5} {0,1,6,7}
  {1,4} {3,6} {0,5} {2,7}
C_12^3 (k+1 = 4, 2k = 6), 3 layers:
  {0,1,2,3} {4,5,6,7} {8,9,10,11}
  {2,3,4,5} {6,7,8,9} {0,1,10,11}
  {1,4} {3,6} {5,8} {7,10} {0,9} {2,11}
C_24^7 (k+1 = 8, 2k = 14), 4 layers:
  {0..7} {8..15} {16..23}
  {4..11} {12..19} {0,1,2,3,20,21,22,23}
  {2,3,8,9} {6,7,12,13} {10,11,16,17} {14,15,20,21} {0,1,18,19} {4,5,22,23}
  {1,8} {3,10} {5,12} {7,14} {9,16} {11,18} {13,20} {15,22} {0,17} {2,19} {4,21} {6,23}
```

**Result 4 — §4 verified numerically.** For all tested `(n,k)` with `n=m(k+1)`, `m in {2,3}`,
`k <= 15`: the zero pattern of `M` is exactly "`u=v` or `uv in E`"; the `2s x 2s` minor `N`
is triangular with nonzero diagonal and has rank exactly `2s`; `rank M <= 2^t`; and
`2s <= 2^t` in every case (e.g. `n=32, k=15`: `t=5`, `rank N = 2s = 32 = 2^5`, tight).
Alon's Theorem 1.1 hypothesis holds verbatim on the (order-reversed) same sequences.

## Caveats

1. **Prior art, lower bound.** §4 is Alon (1986) Theorem 1.1 rediscovered, with a rank
   proof instead of exterior algebra. The writeup makes no novelty claim, but a submitted
   version must cite it.
2. **Prior art, special case.** `eq(C_{2k+2}^k) = ceil(log2(2k+2))` is Alon (1986)
   Corollary 1.2. The `n = 2k+2` slice of the "new" theorem is 40 years old; the novelty
   is the extension to `m >= 3` blocks (and hence to `n >> k`).
3. **The contradicted claim in the source is itself erroneous.** West's REGS page asserts
   `eq(C_n^k) = k+1` when `(k+1) | n`, which is false and is contradicted by Alon's
   corollary cited on the same page. The problem's "wide open" status rests partly on
   that slip, which lowers the novelty bar considerably — the disproof is a natural
   `m`-block generalization of a 1986 construction. The verdict block's `would_publish:
   true` is optimistic on that ground (the mathematics is right; the contribution is
   modest and needs the 1986 context).
4. **Not determined:** the exact value of `eq(C_n^k)` when `(k+1) ∤ n`. The writeup says
   so. My data show the gap is real (`eq(C_7^2)=4 > r+1 = 3`, `eq(C_9^3)=eq(C_10^3)=
   eq(C_11^3)=4 > 3`), so the non-divisible case is genuinely harder and `r+1` is not the
   answer there. The `2r+1` upper bound is not claimed tight and is not tight (`eq(C_7^2)
   = 4 < 5`).
5. **Edge cases.** `k=0` is excluded (`C_n^0` is edgeless, `eq = 0`); the writeup assumes
   `k>=1`. `n <= 2k+1` is handled (`K_n`, `eq=1`), with the implicit assumption `n>=3`.
   `n = 2k+2` exactly is fine (`m=2`): the two blocks are cyclically adjacent on both
   sides, and the construction handles each orientation with a different index `i`; I
   checked this case explicitly. The `s` not a power of two case leaves some `I_h^1(p)`
   empty, producing singleton "cliques" that are discarded — harmless, and the layer count
   can only drop below `r+1`.
6. **Convention dependence.** The result would change if "equivalence subgraph" were
   required to be *induced* or to consist of *maximal* cliques of `G` — but no source uses
   such a definition, and the writeup's §2 layers do use non-maximal and non-consecutive
   cliques (e.g. `{1,4}` in `C_8^3`), which the writeup flags honestly ("Some of these
   cliques have gaps in the cyclic order. That is allowed").
7. **Uniformity in `n`.** The claim is `eq = Theta(log(k+1))` uniformly over `n >= 2k+2`;
   the hidden constants are `1` and `2` on `r`, so the statement is genuinely uniform.
   No hidden dependence on `n` slipped in.

## Referee summary

I attacked this writeup expecting the usual failure modes and found none. The
construction is a clean binary "left/right boundary" layering: `H_0` is the partition into
`k+1`-blocks, and level `h` merges the vertices whose `h`-th bit is `1` in block `i` with
those whose `h`-th bit is `0` in block `i+1`; the cliqueness relies on the fact that every
index in the 1-part exceeds every index in the 0-part, and the disjointness on the fact
that a vertex crosses either its right or its left boundary but never both. Both facts
are stated correctly and I verified all three required properties by code for 7390
parameter pairs (`k <= 24`, `n <= 300`, zero failures). The lower bound is a correct rank
argument, but it is Alon's 1986 Theorem 1.1 rediscovered, and its `n = 2k+2` instance is
Alon's Corollary 1.2, so the exact formula is only new for `m >= 3` blocks. Exhaustive
computation of `eq(C_n^k)` over *all* clique partitions confirms the formula in every
divisible case I could complete (`eq(C_6^2)=eq(C_9^2)=eq(C_12^2)=3`, `eq(C_8^3)=
eq(C_12^3)=3`, `eq(C_10^4)=4`) and confirms `r+1 <= eq <= 2r+1` in every non-divisible
case. The conjecture `eq(C_n^k) = Omega(k)` is therefore genuinely false, in the intended
regime `n >> k`. The one uncomfortable discovery is that the problem's own source page
(West's REGS page, the origin of the OPG entry) asserts `eq(C_n^k) = k+1` when `(k+1) | n`,
which my brute force refutes at `n=8,k=3` and which Alon's Corollary 1.2 — cited on that
same page — already refuted in 1986. The mathematics in the writeup is sound and the
disproof stands; its novelty is real but narrower than the verdict block suggests, and
any publishable version must cite Alon (1986) for the lower bound and for the `n=2k+2`
case.
