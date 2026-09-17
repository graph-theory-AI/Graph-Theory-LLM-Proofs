---
id: melnikovs_valency_variety_problem
leg: attacks_opg
claimed_verdict: disproved
review_verdict: CONFIRMED
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The 37-vertex graph was rebuilt from the prose and verified exactly (w=30, chi=3, RHS=3), the minimality proof checks out line by line and is corroborated by an independent mechanisation, so the problem is disproved as literally stated — but the counterexample lives entirely on the degenerate isolated vertex, and the min-degree->=1 version of Melnikov's question is untouched and remains open.
---

## Interpretation

The writeup formalises the problem as: for every simple graph `G` with `|V(G)| >= 2`,

```
chi(G) > ceil( floor(w(G)/2) / (|V(G)| - w(G)) )
```

where `w(G)` is the number of distinct degrees, **with degree 0 counted as a degree** and
with no connectivity or minimum-degree restriction. I fetched the live OpenProblemGarden
entry (http://www.openproblemgarden.org/op/melnikovs_valency_variety_problem) and it
reproduces exactly the statement in `prompt.md`, verbatim, with the sole restriction
"any graph `G` with at least two vertices" and no further hypothesis.

Two observations argue that this literal reading is the intended one:

* The restriction `|V(G)| >= 2` is *precisely* the well-definedness condition: for `n >= 2`
  two vertices must share a degree, so `w <= n-1` and the denominator `n - w` is positive;
  only `n = 1` makes it zero. So the author did consider the degenerate cases and excluded
  exactly the one that breaks the formula — and did **not** exclude isolated vertices or
  disconnected graphs.
* Degree 0 counting toward `w` is forced by the definition "the number of different degrees".

Two observations argue the other way, and they are the substantive caveat of this review:

* The counterexample is *entirely* powered by the isolated vertex. Deleting it leaves a
  connected 36-vertex graph that satisfies the inequality (I verified: `n=36`, `w=29`,
  `t=7`, RHS `= ceil(14/7) = 2 < 3`). The writeup says so itself, honestly, in its final
  paragraph and in the `caveats` field.
* The primary source (Jensen–Toft, *Graph Coloring Problems*, p. 90, §4.13/4.14) could not
  be obtained verbatim. OPG is a secondary transcription. If Jensen–Toft (or Zykov/Vizing,
  from the Russian school where "graph" often tacitly means connected graph) state the
  problem for connected graphs, the disproof evaporates. This is the one load-bearing
  item I could not verify.

**Would a reasonable author consider the problem resolved?** Partly. The disproof is
correct and genuinely non-trivial for the statement as posed and as recorded by OPG — the
hard part (a connected 36-vertex 3-chromatic graph with 29 distinct degrees, which sits
*exactly* on the boundary of the best available counting bound) is real extremal
combinatorics, not a semantic trick. But the mathematical substance of Melnikov's question
survives: for graphs of minimum degree `>= 1` the inequality is still open, and my
mechanisation of the writeup's own method (below) shows that method cannot decide it. A
referee would classify this as "the stated conjecture is false; the interesting conjecture
is still open", not as "problem solved". The writeup does not oversell this — its scope
paragraph states the limitation explicitly — so I do not count it as interpretation gaming.

## Step-by-step findings

Notation as in the writeup: `n = |V|`, `k = chi`, `t = n - w`, `m = n/2` for even order.

| step | label | note |
|---|---|---|
| 1. Construction (parts A,B,C,T,U,z; edge rules 1–6) | VALID | Unambiguous. I rebuilt it from the prose alone (`build_and_check.py`): 37 vertices, 263 edges. |
| 2. Degree table (z:0; u_i:i; a1,a2,T:13; a3,a4,a5:14,15,16; c_j:17+j; b_j:24+j) | VALID | Every entry reproduced exactly by code; zero mismatches. |
| 3. `{d(v)} = {0,...,29}`, `w(G)=30` | VALID | Verified: degree set is exactly `{0,1,...,29}`, `w = 30`. |
| 4. `I1, I2, I3` are independent and partition `V` | VALID | Verified: sizes 21+6+10 = 37, union is `V`, all three independent (0 internal edges each). So `chi <= 3`. |
| 5. `a1 b0 c0` is a triangle, hence `chi = 3` | VALID | Verified; 603 triangles in total. `chi >= 3` re-confirmed two further ways (see Computational check). |
| 6. `RHS = ceil(15/7) = 3`, so `3 > 3` fails | VALID | `t = 37-30 = 7`, `floor(30/2)=15`, `ceil(15/7)=3`. Counterexample confirmed. |
| 7. Reformulation: conjecture `<=> floor(w/2) <= (k-1)t <=> n <= (2k-1)t+1` (eq. 1) | VALID | I re-derived it and also checked the equivalence exhaustively over `2<=n<=199`, all `w`, all `k`: 0 disagreements. Graph: `37 > 5*7+1 = 36`. |
| 8. Reduction of minimality to "bipartite" + "t<=6" | VALID | A counterexample has `k>=3`, so `n >= (2k-1)t+2 >= 5t+2`; `n<=36` forces `t<=6`. Arithmetic correct. |
| 9. §3.1 bipartite, no isolated vertices: `w<=b`, `w<=2a`, hence `n <= 3t` (eq. 2) | VALID | Degrees of the `B`-side lie in `{1..a}` (`<=a` values), the `A`-side has `a` vertices, so `w<=2a`; all degrees `<= b` so `w<=b`; `n=a+b >= 3w/2`. Correct, and correct for disconnected bipartite graphs too (any fixed bipartition works). |
| 10. §3.1 with `r>=1` isolated vertices: `n <= 3t-2r+3 <= 3t+1` | VALID | `n0=n-r`, `w0=w-1`, `t0=t-r+1`; substitution correct. Edgeless case (`k=1`) satisfies eq. (1) with equality. |
| 11. §3.2 eq. (3): `D = sum|d_i-b| = 2e(H)-2e(L)`, `D` even | VALID | Both identities re-derived (`sum_H d = 2e(H)+e(H,L)`). |
| 12. §3.2 eq. (4): `D >= D_0 = floor(w^2/4)` | VALID | Min total distance from an integer to `w` distinct integers is `r(r+1)` (`w=2r+1`) or `r^2` (`w=2r`), both `= floor(w^2/4)`. |
| 13. §3.2 eqs. (5),(6) refinements using `delta = min degree` | VALID | I re-derived both algebraically. With `s=b-delta`, `u=r-s`: `sum_{j=0}^{2r}|j-s| = r^2+r+u^2` gives (5); `sum_{j=0}^{2r-1}|j-s| = r^2+u(u+1)` gives (6). Exactly the stated right-hand sides. |
| 14. §3.3 eq. (7): `D + 2e + sum h_i^2 <= m^2` | VALID | `D+2e = 2e(H)` and `e(H) <= (m^2 - sum h_i^2)/2` since colour classes are independent. |
| 15. §3.3 eq. (8): `b <= m-a+e` | VALID | The `m`-th vertex lies in `L`; it misses the `>= a` same-coloured vertices of `H`, and has `<= e(L)` neighbours inside `L`. |
| 16. `D_0 = m^2 - tm + floor(t^2/4)` and eq. (9) `m^2/k <= Q_k(m) <= tm - floor(t^2/4)` | VALID | `w = 2m-t`; `floor((2m-t)^2/4) = m^2-mt+floor(t^2/4)`. Cauchy–Schwarz gives `Q_k(m) >= m^2/k`. |
| 17. Table (10): `m <= k, 2k-1, 3k-1, 4k-2, 5k-2, 6k-2` for `t=1..6` | VALID | Proved the general inequalities by hand *and* checked by brute force that these are the exact integer maxima of (9) for every `k in 2..300` and `t in 1..6`: perfect match. The quoted residuals `1+1/k, 1, 2, 1/k, 1+1/k, 3+1/k` at one past the bound are all correct. |
| 18. `X = D-D_0 >= 0`, `E = sum h_i^2 - Q_k(m) >= 0` even; eq. (11) `X+2e+E <= m^2-D_0-Q_k(m)` | VALID | `E` even because `x^2 = x mod 2`. |
| 19. Table (12) for `t=1,3,5,6`: `Q_k(m) = k, 9k-5, 25k-18, 36k-22`; budgets `0,0,2,1`; `a = 1,2,4,5` | VALID | Each entry recomputed: e.g. `t=6`, `m=6k-2`, balanced split `6^(k-2) 5^2` gives `36k-22`, budget `6m-9-(36k-22)=1`, `a=5`. The balanced minimiser is unique up to permutation, so `E=0` does pin down `a`. (Needs `k>=2`, which the writeup states.) |
| 20. Boundaries `t=1,3` (assume `delta>=1`) | VALID | Budget 0 forces `X=e=E=0`; then `b <= m-a = r`, while `X=0` plus (5) forces `b = delta+r >= r+1`. Contradiction. |
| 21. Boundary `t=5` (assume `delta>=1`) | VALID | `X` even since `D_0=r(r+1)` and `D` are even. The "`E<=2` forces `a>=3`" transfer argument is correct (moving a unit from a part `>=6` to a part `<=2` drops the square-sum by `>=6`). Both `X=0` (giving `b<=m-3 < delta+r = m-2`) and `X=2` (giving `b<=m-4`, penalty `>=4`) contradict. |
| 22. Boundary `t=6` (no `delta` assumption) | VALID | `r = 6k-5` odd so `D_0=r^2` odd, `D` even, hence `X` odd and `>=1`; budget 1 forces `X=1, e=E=0, a=5, b <= r-2`; then (6) with `delta>=0` gives `D >= r^2+2`, i.e. `X>=2`. Contradiction. |
| 23. §3.4 eq. (13) for even order, then (14) `n <= (2k-1)t` for graphs without isolated vertices | VALID | The "add an isolated vertex to an odd-order graph" step keeps `t` and `k` and makes the order even; applying (13) gives (14) in both parity cases. Degenerate `k=1` never has `t` even at even order, so the `k>=2` restriction in (10) is harmless. |
| 24. §3.4 final reduction for `r>=1` isolated vertices: `n <= (2k-1)t - (2k-2)r + (2k-1) <= (2k-1)t+1` | VALID | The last inequality is `2k-2 <= (2k-2)r`, true for `r>=1`. `t0 = t-r+1 <= t <= 6`, and `chi` is unchanged by deleting isolated vertices. |
| 25. Conclusion "minimum counterexample order is 37" | VALID | Follows from steps 8, 10, 24. Independently corroborated by my mechanisation (below). |
| 26. Scope remark: the isolated vertex is material; the connected version is not refuted | VALID | Verified computationally (`G - z` satisfies the inequality) and the honesty of the remark is confirmed by my own analysis, which shows the method cannot settle the `delta >= 1` version. |

I found **no** step labelled GAP or ERROR.

## Reference check

* **OpenProblemGarden entry** — fetched live. The statement, the "at least two vertices"
  restriction, the discussion paragraph and the bibliography match `prompt.md` word for
  word. The entry is still listed as **open** in the OPG vertex-coloring category
  (last updated 3 March 2013). No comment, update or claimed resolution on the page.
* **Literature search for a resolution** — four searches (counterexample / solved /
  valency-variety / Melnikov) returned nothing post-1995 on this specific problem, and
  the Jensen–Toft problem archive at imada.sdu.dk has no update page for §4.13/4.14. I
  found no evidence the result is ALREADY_KNOWN, but absence of evidence here is weak:
  this is a Low-importance, rarely-cited problem.
* **Jensen–Toft p. 90; Dirac 1964; Nettleton 1960; Vizing 1968; Zykov 1968** — none of
  these could be obtained in full text (the book is not freely available; the Dirac and
  Nettleton papers are pre-digital). **This does not damage the proof**: the writeup
  invokes *no* external theorem. Its argument is self-contained, as it explicitly claims
  ("No computational search or unverified literature result is used in the argument").
  The only exposure is the faithfulness of OPG's transcription of Jensen–Toft's wording,
  discussed under Interpretation.
* The Dirac–Nettleton upper bound `chi <= n - floor(w/2)` is quoted only as context and
  is not used anywhere. (For the counterexample it reads `3 <= 37-15 = 22`, consistent.)

## Computational check

Scripts: `verification_astra/scripts/melnikovs_valency_variety_problem/`
(`build_and_check.py`, `small_cases.py`, `necessary_conditions.py`), run with system
`python3` and networkx 3.6.1.

**1. The graph** (rebuilt from the prose of §1 only, not from the degree table):

* `|V| = 37`, `|E| = 263`, 603 triangles, components of sizes `36 + 1`.
* Degree sequence: `z:0`, `u_i:i` for `i=1..12`, `a1,a2:13`, `t_1..t_6:13`,
  `a3,a4,a5:14,15,16`, `c_0..c_6:17..23`, `b_0..b_5:24..29`.
  **Zero mismatches** against the writeup's degree table.
* Degree set `= {0,1,...,29}` exactly, so **`w(G) = 30`**.
* `I1 (21 vertices), I2 (6), I3 (10)` partition `V` and each has **0 internal edges**,
  so `chi <= 3`.
* `chi >= 3` confirmed three independent ways: (i) `nx.is_bipartite(G) = False`;
  (ii) exhaustive backtracking 2-colouring search fails, 3-colouring search succeeds;
  (iii) hand-rolled BFS 2-colouring of each component forces a monochromatic edge
  (`u3 b4`) in the 36-vertex component. So **`chi(G) = 3` exactly** — not merely an
  upper bound.
* `t = 37 - 30 = 7`, `floor(w/2) = 15`, `RHS = ceil(15/7) = 3`. The conjecture asserts
  `3 > 3`: **FALSE**. Equivalently `n = 37 > (2k-1)t+1 = 36`.
* `G - z`: `n=36`, degrees `{1,...,29}`, `w=29`, `t=7`, `RHS = ceil(14/7) = 2 < 3`,
  connected. The inequality **holds** there — the isolated vertex is indeed essential.

**2. Sensitivity to the placement of the ceiling** (the formula's fragile point):
with `n,w,k = 37,30,3` the claim fails only for the stated nesting.
`chi > ceil(floor(w/2)/t)`: `3 > 3` false (counterexample).
`chi > floor(w/2)/t`: `3 > 2.143` true. `chi > ceil(w/2)/t`: true.
`chi > floor(floor(w/2)/t)`: `3 > 2` true.
So the disproof depends on the ceiling being outside the fraction — which is exactly how
both `prompt.md` and the live OPG page render it. Worth stating, because a transcription
slip here would void the whole thing.

**3. Exhaustive small cases**: all 1251 graphs on 2..7 vertices (networkx atlas) satisfy
the conjecture. Notably the minimum slack `(2k-1)t+1-n` is **0 at every order 2..7**, i.e.
the conjecture is tight everywhere — consistent with Zykov's report that Melnikov showed
the bound best possible, and an indication that a counterexample was a priori plausible.

**4. Table (10) verified exactly**: for every `k in 2..300` and `t in 1..6`, the true
largest integer `m` with `m^2/k <= tm - floor(t^2/4)` equals the writeup's claimed
`k, 2k-1, 3k-1, 4k-2, 5k-2, 6k-2`. No off-by-one anywhere.

**5. Independent mechanisation of §3** (`necessary_conditions.py`): I encoded eqs.
(4)–(8)+(11) as a feasibility test over `(X, e, E)` with the parity constraints, and
computed the largest even order not excluded, for `k = 2..6` and `t = 1..7`. The output
reproduces the writeup's (13) exactly — e.g. for `k=3`: max even order is
`6, 10, 16, 20, 26, 30, 36` for `t = 1..7`, i.e. `(2k-1)t+1` for odd `t <= 5`,
`(2k-1)t` for even `t` (including the `t=6` boundary exclusion the writeup has to work
for), and `36` for `t=7`. With `delta >= 1` imposed the values drop to
`4, 10, 14, 20, 24, 30, 36`. Two consequences:

* The minimality claim (37) is corroborated by a second, independently written
  implementation of the same counting scheme.
* **The construction sits exactly on the boundary the method permits**: `G - z` realises
  the maximum even order `36` at `k=3, t=7, delta>=1`. It is not slack; it was engineered
  against this bound.

**6. The open residue.** Running the same test for `k=3` and `t` up to 40 asking whether a
counterexample with `delta >= 1` is excluded: it is excluded for `t <= 9`, but from
`t = 10` onwards it is **not** (e.g. `t=10` needs `n >= 52` and the method permits even
orders up to `52`; `t=11` needs `57` and permits `58`; the permitted order grows like
`~5.45t` against the required `5t+2`). So the writeup's technique provably cannot decide
the minimum-degree-`>=1` version of Melnikov's problem, and that version is untouched.

## Caveats

1. **The isolated vertex is the whole mechanism.** `G - z` has `w = 29` (odd), so
   `floor(w/2) = 14 = (k-1)t` exactly — tight. Adding an isolated vertex bumps `w` to 30
   and `floor(w/2)` to 15 while leaving `n - w`, `chi` unchanged, consuming the free `+1`
   that the floor grants at odd `w`. Any reader who reads "graph" as "graph without
   isolated vertices", or as "connected graph", is not served by this counterexample.
2. **Primary source not verified.** Jensen–Toft p. 90 could not be read verbatim; the
   review rests on the live OPG transcription, which does match `prompt.md` exactly.
3. **Ceiling placement is load-bearing** (see Computational check 2). Any variant nesting
   of the floor/ceiling makes the graph a non-counterexample.
4. **`k=1` / edgeless / `n=1` edge cases**: handled correctly and separately by the
   writeup; `n=1` is excluded by the problem statement itself (it is the only case with
   `n = w`, i.e. zero denominator). For `n >= 2`, `t >= 1` always.
5. **Minimality is over all graphs, not over connected graphs**, and says nothing about
   how far above 37 a `delta >= 1` counterexample (if any) would have to sit.
6. **Novelty is unverified.** The writeup says so. I found no published resolution, but
   this is a Low-importance problem with little literature, so the search is weak
   evidence. A 1968-era reader with a tight example in hand could have made this same
   observation; I cannot rule out that it is folklore.
7. **Gap between the verdict block and what is proved**: the `one_line` says "making the
   proposed right-hand side equal to 3; moreover, 37 vertices is minimum" — both
   verified. The `verdict: disproved` is correct for the problem as stated. It would be
   misleading only if read as "Melnikov's question is settled", which the body of the
   writeup explicitly disclaims.

## Referee summary

I set out to break this and could not. Reconstructing the 37-vertex graph from the prose
alone (not from the degree table) reproduces every claimed property exactly: 263 edges,
degree set precisely `{0,1,...,29}` so `w = 30`, a verified partition into three
independent sets, and `chi = 3` established as an exact value — non-2-colourability
confirmed by three independent methods, not just an upper bound from a colouring. With
`n - w = 7` the proposed right-hand side is `ceil(15/7) = 3`, so the assertion `chi > 3`
fails, and the live OpenProblemGarden entry states the problem with no hypothesis beyond
`|V| >= 2` (which is exactly the condition making the denominator nonzero), so this is a
genuine counterexample to the problem as the source states it, not to a strawman. The
minimality argument — the long part — also survives a full line-by-line audit: I
re-derived eqs. (1)–(14) by hand, checked table (10) against brute force for all `k` up to
300, and re-implemented the whole counting scheme independently, which reproduces the
writeup's bounds exactly and confirms that no counterexample exists below 37 vertices. The
one substantive reservation is interpretive rather than mathematical: the counterexample
lives entirely on the isolated vertex (deleting it yields a connected 36-vertex graph that
satisfies the inequality), so what is refuted is the degenerate-inclusive reading, while
the minimum-degree-`>=1` question — which is what most readers would call Melnikov's
problem — is untouched; my mechanisation further shows the writeup's own method cannot
decide that version for `t >= 10`. The writeup states this limitation itself, which is why
I do not score it as interpretation gaming. Verdict CONFIRMED, with the caveat that this
is a correct disproof of the literal statement rather than a resolution of the underlying
question, and that the primary source (Jensen–Toft p. 90) could not be read verbatim.
