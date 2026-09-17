---
id: random_stable_roommates
leg: attacks_opg
claimed_verdict: partial
review_verdict: MINOR_GAPS
confidence: medium
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The planted-matching/short-cycle argument holds up under full re-derivation and simulation, and its P_n = O(n^{-1/6} sqrt(log n)) genuinely improves the published Chin-Michelen bound n^{-1/17}; the Mertens conjecture itself is untouched, and the only real defects are one unproved (but true) truncated-binomial inequality, a missing trivial case in the exchange lemma, and a total failure to cite or position against Chin-Michelen and Pittel.
---

## Interpretation

The source problem is Mertens' conjecture `P_n = Theta(n^{-1/4})`. The writeup does **not**
claim to resolve it, and its verdict block says so. Its formalization of the model
(preference lists = independent uniform permutations of the other `n-1` people, generated
by i.i.d. `U_{vw} ~ Unif[0,1]` with smaller = more preferred) is the standard one and is
exactly the model of Pittel and of Chin-Michelen. No interpretation gaming: the writeup
does not refute a strawman, does not silently change the model, and §8 states plainly both
what is missing (the exponent 1/4) and why the method cannot produce a lower bound at all.

What is actually established: a new **upper** bound
`P_n = O(n^{-1/6} sqrt(log n))`. What this does to the source problem: the known window
moves from `Omega(n^{-1/2}) <= P_n <= n^{-1/17}` (Pittel 1993 / Chin-Michelen 2026) to
`Omega(n^{-1/2}) <= P_n <= O(n^{-1/6} sqrt(log n))`. The conjectured truth `n^{-1/4}` still
lies strictly inside the window, so the conjecture is **not** resolved and not even
half-resolved: neither the matching upper bound nor any lower-bound improvement is obtained.
It is a quantitative advance on the best published upper bound, nothing more. The verdict
`partial` with `would_publish: true` is therefore a fair self-assessment of the mathematics
— but see **Reference check**: as written the document would be rejected on scholarship
grounds, not on correctness grounds.

Sanity check against the source problem's own data: at `n = 20000` Mertens' simulated value
is `e sqrt(2/pi) n^{-1/4} ~ 0.182`, while the writeup's bound (implied constant 1) gives
`~0.60`. Consistent; the new bound does not contradict the conjecture, the Pittel lower
bound, or the simulations.

## Step-by-step findings

`M` = planted matching, `x_v = U_{v,M(v)}`, `S = sum x_v`, `a = max x_v`, `Z` = number of
stable matchings, `m_n = E Z`, `q_v = x_{M(v)}/S`, `K` = cycle-length cutoff,
`C_K` = number of directed `F`-cycles of length in `[2,K]`, `lambda_K = H_K - 1`.

| step | label | note |
|---|---|---|
| 1. §1 planted law `Q`: pick `M` uniform, condition on `M` stable | VALID | `dQ/dP = Z/m_n` since `P(M stable)` is the same for all `M` by symmetry and `m_n = N_n P(M stable)`. |
| 2. §1 eq. (1) `P_n = m_n E_Q[1/Z]` | VALID | `E_Q[1/Z] = E_P[(Z/m_n)(1/Z)1_{Z>0}] = P(Z>=1)/m_n`. Checked non-circularly by sampling `Q` directly (see Computational check): rel. error 0.03 % at `n=6`, 0.7 % at `n=8`. |
| 3. §1 conditional law of an off-`M` score pair = uniform on unit square minus `[0,x_v)x[0,x_w)`, normaliser `1 - x_v x_w` (2) | VALID | Stability factorises over unmatched pairs given `x`; the `x_v` are `n` i.i.d. uniforms (they are distinct entries of `U`). |
| 4. §2 eq. (3) `m_n = N_n int_{[0,1]^n} f(x) dx` | VALID | Standard Pittel integral; numerically `(n-1)!! P(M stable) = 1.1456` vs `E[Z] = 1.1497` at `n=6`. |
| 5. §2 normalisation `int_{R_+^n} e^{-S^2/2} dx = 1/(n-1)!!` | VALID | `= 2^{n/2-1}Gamma(n/2)/(n-1)!`; equals `1/(n-1)!!` (checked `n=2`: `1=1`; `n=4`: `1/3=1/3`). |
| 6. §2.1 `log W <= A/2 + B - D/2` | VALID | Re-derived: `sum_{v<w, not in M} x_v x_w = (S^2-A)/2 - B` and `log(1-z) <= -z - z^2/2`. |
| 7. §2.1 `B <= A/2`, `D >= A^2/2 - A` | VALID | `B <= sum (x_v^2+x_w^2)/2`; `sum x_v^4 <= A` and `sum_M x_v^2x_w^2 <= A/2` on the cube. |
| 8. §2.1 eq. (5) `0 <= W <= e^{9/4}` | VALID | `3A/2 - A^2/4` maximised at `A=3`, value `9/4`. Numerically the largest `W` found over 32 000 probes in `n = 4..200` is `7.375 < e^{9/4} = 9.488`. |
| 9. §2.2 `A -> 2`, `B -> 1/2`, `D -> 2`, `a -> 0`, hence eq. (6) `m_n -> sqrt(e)` | VALID (loosely stated) | LLN on the `x_v = S E_v/T` representation; the limit plus the uniform bound (5) gives bounded convergence. Numerically `E_mu[W] = 1.6473` (`n=1000`) and `1.6449` (`n=200`) vs `sqrt(e)=1.64872`. Matches Pittel's published `E[X] = (1+o(1))e^{1/2}` — rediscovered, not cited. Stated without quantification, but only the limit is used. |
| 10. §2.2 eq. (7) `Q(R_n^c) = O(n^{-9})` for `R_n = {sqrt(n)/2 <= S <= 2 sqrt(n), a <= 40 log n/sqrt(n)}` | VALID | `P(max E_v > 10 log n) <= n^{-9}` dominates; `S^2` and `T` tails are `e^{-cn}`; transfer from `mu_n` to `Q` uses (5) and `m_n = Theta(1)`. |
| 11. §3 eq. (8) `U_{v,f(v)} > x_v` | VALID | Otherwise `{v, f(v)}` blocks `M`. |
| 12. §3 Exchange lemma `Z >= 2^c` for a good collection | VALID, one trivial case omitted (GAP, cosmetic) | Re-derived in full: `F` permutes `D`, so `f: D -> M(D)` is a bijection and `D cap M(D) = empty` makes the switch a perfect matching; `D` strictly worse off, `M(D)` strictly better off; a block with one endpoint outside `D` contradicts minimality of `f(v)` (or, for `w = M(v)`, `w`'s strict improvement); a block inside `D` is exactly condition (9). **Omitted:** the case where *neither* endpoint is in `D` — then both are weakly better off, so the pair would block `M` itself. One line, trivially repairable. Brute-force verified: 8 298 good collections at `n=6` and 2 058 at `n=8`, **zero** unstable sub-collections and **zero** violations of `Z >= 2^c`. |
| 13. §4.1 impossibility of `f(v)=v` and of two required edges coinciding in opposite directions | VALID | `pi(v)=v` is excluded since `f(v) != M(v)`; the reversed-edge case would be a blocking pair of `M`. |
| 14. §4.1 eq. (12) upper bound `Q_x(E(C,pi)) <= (prod q_v)(1-a^2)^{-r}(1-2ra/S)^{-r}` | VALID | Required-edge density `x_{M(pi(v))}/(1-x_v x_{M(pi(v))})`; external survival `<= e^{-t_v x_w}`; `sum_{w not in C u M(C)} x_w >= S - 2ra`; `prod_{v in C} x_{M(pi(v))} = prod x_{M(v)}`. All pairs used are distinct so independence is legitimate. |
| 15. §4.1 eq. (13) | VALID | `(1-a^2)^{-r}(1-2ra/S)^{-r} = 1 + O(ra^2 + r^2a/S)`. |
| 16. §4.2 eq. (14) within-`C` factor `1 - (t_u x_v + t_v x_u)/(1-x_u x_v)` | VALID | The two bad regions `{U_{uv} in [x_u,x_u+t_u), U_{vu}<x_v}` and `{U_{vu} in [x_v,x_v+t_v), U_{uv}<x_u}` are disjoint with areas `t_u x_v`, `t_v x_u`. |
| 17. §4.2 eq. (16) `sum b <= S sum t_v/(1-a^2)`, `max b <= 2aL/(S(1-a^2))` | VALID | Row-wise collection; each row's thresholds sum to at most `S`. |
| 18. §4.2 eq. (17) lower bound | VALID | `log(1-b) >= -b-2b^2` for `b<=1/2` (in fact `-b-b^2`); box `t_v <= L/S` requires `L/S <= 1-a`, satisfied. Integration gives `(1+eta)^{-r}(1-e^{-(1+eta)L})^r`. |
| 19. §5 eq. (18)/(19) factorial moments `|E_x (C_K)_j - lambda_K^j| <= delta lambda_K^j`, `delta = O(Ra^2 + R^2a/S + RaL/S + Re^{-L})` | VALID | `r = sum k_i <= KJ = R`, so the relative error is uniform in `j <= J`. Upper: sum (13) over all lists, `sum_lists prod q_v = 1`, divide by `k_1...k_j`, sum `1/(k_1...k_j)` over `[2,K]^j` = `lambda_K^j`. Lower: restrict to injective, partner-free lists, losing at most `r^2a/S` by (20). |
| 20. §5 eq. (20) collision weight `<= r^2 a/S` | VALID | `sum q_v^2 <= a/S` and `sum q_v q_{M(v)} <= a/S`; `binom(r,2) * 2a/S <= r^2 a/S`. |
| 21. §5.1 `2^{-c} <= sum_{j=0}^{J} (-1/2)^j (c)_j/j!` for even `J` | TRUE but GAP (asserted, not proved; the stated reason is wrong) | The terms `binom(c,j)2^{-j}` are **not** monotone (`binom(30,j)2^{-j}` peaks at `j=10`), so "the alternating binomial truncation" does not follow from the alternating-series bound as implied. The inequality is nevertheless true; I verified it in exact rational arithmetic for all `c <= 120`, even `J <= 40` (zero violations), and it has a three-line repair: with `R_J(c) = T_J(c)-(1-x)^c` one gets `R_J(c) = R_J(c-1) - x R_{J-1}(c-1)`, so `(-1)^J R_J(c) >= 0` by induction on `c` over both parities, base `R_J(0)=0`, `R_0(c) = 1-(1-x)^c >= 0`. |
| 22. §5.1 eq. (21) | VALID | `|sum_j (-1/2)^j/j! (E(C_K)_j - lambda^j)| <= delta e^{lambda/2}`; Taylor remainder of `e^{-lambda/2}` truncated at `J`. |
| 23. §6 eq. (22) `Q_x(B_K) = O(K^2 a/S + K^2/S^2)` — **the crux** | VALID | See Computational check: measured `Q(B_K)/(K^2/n) = 0.82-0.86` at `n=400` and `0.59-0.98` at `n=1600`, flat in both `K` and `n`. Chin-Michelen's analogous Lemma 3 costs `n^{-1+4alpha} = K^4/n`; the `K^4/n` law is ruled out by a factor 30-100 in these ranges. |
| 24. §6.1 partner-collision count `O(K^2 a/S)` | VALID | One cycle: `k(k-1)` position pairs / `k` rotations, weight `sum_v q_v q_{M(v)} <= a/S` -> `O(k a/S)`, summed `O(K^2 a/S)`. Two cycles: `k*l` cross pairs cancel `k*l` rotations -> `O(K^2 a/S)`. A goodness failure always has a witness in at most two cycles — correct, since a collision or a blocking pair involves two vertices. |
| 25. §6.2 blocking rectangle `[x_u,x_u+t_u) x [x_v,x_v+t_v)`, area (24) | VALID, and the subtle point is right | The claim that the sub-threshold portions are excluded is correct and I checked it: if `U_{uv} < x_u` and `U_{vu} < x_v + t_v`, then `u in A(v)` and `U_{vu} < U_{v,f(v)}`, contradicting minimality of `f(v)`; symmetrically. (The doubly-sub-threshold corner is excluded by stability of `M`.) |
| 26. §6.2 eq. (25)/(26) extra `S^{-2}` and `O(K^2/S^2)` | VALID | `int t e^{-lambda t} dt = lambda^{-2}` supplies two extra powers of `(S-2ra)^{-1}`; `{u,v} subset C` is neither a required nor an external pair when `C cap M(C) = empty`, so independence holds. |
| 27. §7 parameters `K = n^{1/3}/log n`, `J = 2 ceil(10 log n)`, `L = 10 log n`, `R = O(n^{1/3})` and eq. (27) `delta = O(n^{-1/3} log n)` | VALID | Re-derived each term: `Ra^2 = n^{-2/3}log^2 n`, `R^2a/S = n^{-1/3} log n` (dominant), `RaL/S = n^{-2/3}log^2 n`, `Re^{-L} = n^{-29/3}`. |
| 28. §7 eq. (28) `E_x 2^{-C_K} = O(n^{-1/6} sqrt(log n))` | VALID | `e^{-lambda_K/2} = Theta(K^{-1/2}) = n^{-1/6}(log n)^{1/2}`; `delta e^{lambda_K/2} <= n^{-1/3}(log n) K^{1/2} = n^{-1/6}(log n)^{1/2}`; remainder `(lambda/2)^{J+1}/(J+1)! <= (e/40)^{20 log n} = O(n^{-2})`. The balance `-beta/2 = 5beta/2 - 1` indeed gives `beta = 1/3`. |
| 29. §7 eq. (29) `Q_x(B_K) = O(K^2 log n/n) = O(n^{-1/3}/log n)` | VALID | Negligible against (28). |
| 30. §7 `1/Z <= 2^{-C_K} + 1_{B_K}` and final assembly via (1), (6), (7) | VALID | `Z >= 1` under `Q`; on `B_K^c` the full short-cycle collection is good so `Z >= 2^{C_K}`. |
| 31. §8 discussion of what remains | VALID and honest | Correctly identifies that the method's ceiling is `K ~ sqrt(n)` (where `K^2/n` saturates), which would give exactly `n^{-1/4}` — a pleasing internal consistency with Mertens' conjectured exponent — and that no lower bound can follow. |

## Reference check

The writeup deliberately cites **nothing**: "All estimates below are proved directly; no
literature result is needed." There are therefore no citations to falsify, and I confirm
that the document is self-contained (every constant and estimate is derived in-document).
`references_ok: true` is true in that narrow sense. But the scholarship is a real defect:

* **Chin & Michelen, *The random stable roommates problem typically has no solution*,
  arXiv:2601.07612v1, 12 Jan 2026** — verified to exist, still v1, no later version. Its
  Theorem 1 is exactly `P(X >= 1) <= n^{-1/17}` for large `n`. I read the full PDF (saved at
  `verification_astra/scripts/random_stable_roommates/ref/`). **Its high-level architecture
  is the same as the writeup's**: condition on a matching `Pi` being stable, show many
  matchings are then stable, and convert via `E[X]= O(1)`. The writeup's framing
  ("independent of the cited literature") is accurate as to *derivation* but would badly
  mislead a reader about *novelty of approach*. A referee would demand the comparison be
  made explicitly. The two genuinely new ingredients, which I verified are absent from
  Chin-Michelen, are:
  1. **the canonical map `F(v) = M(f(v))`**. Chin-Michelen range over *all* stable
     single-cycle neighbours `M°_{<=n^alpha} cap S` and must union-bound over *pairs of
     arbitrary cycles* (their Lemma 10 counts pairs of cycles sharing `t` edges in `s`
     components), which costs them `P(D_1 | Pi) <= n^{-1+4alpha}` (Lemma 3) and
     `P(D_3 | Pi) <= n^{-1+4alpha}` (Lemma 5), i.e. `K^4/n`, capping `alpha < 1/4`. The
     writeup's collection has only `|C| ~ K` vertices, so its analogous cost is `K^2/n`,
     capping `beta < 1/2`. I confirmed there is no `F`-like "most-preferred candidate" map
     anywhere in Chin-Michelen.
  2. **the exact negative-exponential moment.** Chin-Michelen must prove a *lower-tail
     concentration* result for the cycle count (`D_2`, Lemma 4) and then split with Markov,
     yielding the four-way optimisation (7) `t* = max min{gamma log 2, 1-4alpha,
     alpha(1-e^{-s}) - s gamma, 1/3 - alpha(1-e^{-s}) - s gamma}`, optimum
     `alpha ~ 0.2348`, `gamma ~ 0.0877`, `t* >= 0.060766`, hence `1/17`. The concentration
     cost is what destroys them: their usable `gamma` is a third of the mean exponent
     `alpha`. The writeup pays *no* concentration cost because it computes
     `E[2^{-C_K}] = e^{-lambda_K/2}` exactly through the alternating factorial-moment
     expansion. This is the decisive improvement, and it is legitimate.
  So the crux holds: `1/6 > 1/17`, by a genuine mechanism, and `n^{-1/6}sqrt(log n)` is
  strictly stronger than `n^{-1/17}` for large `n`.
* **Pittel 1993** (`E[X] = (1+o(1))e^{1/2}`, lower bound `Omega(n^{-1/2})`) and the Pittel
  integral `prod_{ij not in Pi}(1 - x_i x_j)` — the writeup's §2 (3)/(6) is a rediscovery of
  this, uncited. Confirmed from Chin-Michelen §1.1 and my own numerics.
* **Pittel-Irving 1994** upper bound `e^{1/2}/2 = 0.8244` — confirmed as the previous
  published constant bound; the OPG page's `sqrt(e)/2` agrees.
* **Priority check.** arXiv API sweep of all `stable roommates` / `stable matching`+
  `roommates` submissions: nothing since Chin-Michelen addresses the solvability
  probability. The only 2026 wildcard, arXiv:2608.11682 "A Solution to the Roommate
  Problem" (Aug 2026), is econ.TH on priority/blocking-neutral matchings — unrelated. No
  paper achieves `n^{-1/6}`, `n^{-1/4}`, or an improved lower bound. **Not ALREADY_KNOWN:
  the theorem is new.** The OPG catalog entry is stale only in the sense that it already
  records Chin-Michelen correctly.
* **Self-contamination control (step 2c).** Nothing here was recorded as prior art on the
  strength of a search-engine paraphrase. The one piece of prior art that matters,
  Chin-Michelen, was confirmed by downloading the actual arXiv PDF (598 KB, `arXiv:2601.07612v1
  [math.CO] 12 Jan 2026`, authors Byron Chin and Marcus Michelen, MIT/UIC) and reading its
  text directly — Theorem 1, the proof-strategy section, and Lemmas 3, 5, 9 and 10 are quoted
  above from that extraction, not from a summary. The arXiv API sweep queried arXiv's own
  listing service, not the open web. No claimed prior art traced back to this repository or
  to this campaign's own artifacts, and no `ALREADY_KNOWN` finding is being recorded.

## Computational check

All scripts in `verification_astra/scripts/random_stable_roommates/` (`python3`, numpy).
`ref/` holds the Chin-Michelen PDF and its text extraction.

1. `brute_small.py` — **Exchange lemma by exhaustive enumeration.** All `(n-1)!!` matchings
   tested for stability; for every stable `M`, `F` and its cycles built, goodness tested,
   and *every* sub-collection's switched matching re-tested for stability.
   * `n=6`, 20 000 instances: `P_6 = 0.9330`, `E[Z] = 1.1515`; 8 298 good collections;
     **0** unstable sub-collections; **0** instances with `Z < 2^c`.
   * `n=8`, 4 000 instances: `P_8 = 0.9045`, `E[Z] = 1.2005`; 2 058 good collections;
     **0** unstable sub-collections; **0** instances with `Z < 2^c`.
2. `identity_check.py` — **eq. (1) without circularity.** `P_n`, `m_n` from uniform
   instances; `E_Q[1/Z]` from genuine rejection sampling of `Q` (resample `U` until the
   planted `M` is stable, then enumerate `Z`).
   * `n=6`: `P_n = 0.93278`, `m_n = 1.14972`, `E_Q[1/Z] = 0.81107`,
     `m_n E_Q[1/Z] = 0.93250` — rel. diff **0.03 %**. Also `(n-1)!! P(M stable) = 1.1456`.
   * `n=8`: `P_n = 0.91125`, `m_n = 1.22800`, `E_Q[1/Z] = 0.74727`,
     `m_n E_Q[1/Z] = 0.91765` — rel. diff **0.70 %**.
   * Necessity of goodness condition 2: in **4 268/4 268** (`n=6`) and **715/715** (`n=8`)
     collections where condition 2 fails but condition 1 holds, some sub-collection is
     unstable. The condition is binding, not decorative. (Condition 1 never failed alone at
     these sizes; its necessity is structural — the switch would not be a matching.)
3. `planted_sim.py` — **planted-measure simulation** (rejection sampler from `mu_n` with
   acceptance `W/e^{9/4}`, i.e. the writeup's own (4)+(5)).
   * eq. (6): `E_mu[W] = 1.6449` (`n=200`, 17 083 proposals) and `1.6473` (`n=1000`,
     8 590 proposals) vs `sqrt(e) = 1.64872`.
   * eq. (18), `j=1`: `E[#k-cycles]` vs `1/k` at `n=1000` — ratios
     `1.02, 1.08, 1.05, 0.94, 1.00, 0.99, 0.91, 0.94, 0.95` for `k=2..10`.
   * eq. (21) main term, `E[2^{-C_K}]` vs `e^{-lambda_K/2}` — this tests *all* factorial
     moments at once. At `n=1000` the ratio is `0.97-1.05` for every `K` up to 40. At
     `n=200` agreement holds to `K ~ 12` and then degrades upward (ratio 1.29 at `K=30`) —
     exactly the `delta ~ K^2 polylog/n` breakdown the writeup predicts, and the breakdown
     point moves out with `n` as it should.
4. `goodness_scaling.py` — **the crux, eq. (22).** Measured `Q(B_K)` (partner collisions +
   internal blocking pairs, separately) against `K^2/n` and `K^4/n`:
   | n | K | `Q(B_K)` | `K^2/n` | `K^4/n` | `Q(B_K)/(K^2/n)` |
   |---|---|---|---|---|---|
   | 400 | 3 | 0.0185 | 0.0225 | 0.203 | 0.822 |
   | 400 | 5 | 0.0540 | 0.0625 | 1.562 | 0.864 |
   | 400 | 8 | 0.1375 | 0.1600 | 10.24 | 0.859 |
   | 400 | 12 | 0.2460 | 0.3600 | 51.84 | 0.683 |
   | 1600 | 3 | 0.0033 | 0.0056 | 0.051 | 0.593 |
   | 1600 | 5 | 0.0133 | 0.0156 | 0.391 | 0.853 |
   | 1600 | 8 | 0.0392 | 0.0400 | 2.560 | 0.979 |
   | 1600 | 12 | 0.0833 | 0.0900 | 12.96 | 0.926 |
   The ratio to `K^2/n` is flat in `K` and in `n` over a 4x range of `n`; a `K^4/n` law is
   excluded by one to two orders of magnitude. The two failure modes (partner collision,
   blocking) contribute comparably, as the writeup's (23)+(26) predicts.
5. `bonferroni.py` — **eq. (21)'s truncated binomial inequality.** Exact rational
   arithmetic, `c <= 120`, even `J <= 40`: **0 violations** of `2^{-c} <= T_J(c)`; odd `J`
   reverses, as it must. Floating-point "violations" at `c = 57,58` are pure cancellation
   artefacts (`T ~ 1e-8` against a true value `1e-17`) and disappear in exact arithmetic.
   The printout also exhibits the non-monotonicity of the terms that invalidates the
   writeup's stated justification.
6. `encoding_check.py` — **encoding validation**, so that the above is not verifying a bug.
   The vectorised `build_F`/`cycles_of` used in 3 and 4 agrees with the independent
   brute-force implementation used in 1 and 2 on 4 000 random instances (`n = 6,8,10`):
   **0** `f`-mismatches, **0** cycle-set mismatches. Independent probe of eq. (5) over
   32 000 threshold vectors in `n = 4..200`: largest `W` found `7.375`, bound
   `e^{9/4} = 9.488` — holds with slack, and `max W -> e` as `n` grows.

No computational check failed.

## Caveats

1. **The conjecture is untouched.** Only an upper bound, only `1/6` not `1/4`, and §8
   correctly explains that the planted-model construction bounds `1/Z` from above and so can
   *never* give the `Omega(n^{-1/4})` half. The gap `[n^{-1/2}, n^{-1/6+o(1)}]` still
   strictly contains `n^{-1/4}`.
2. **Unproved inequality (step 21).** Load-bearing and asserted in one line with an
   incorrect implicit justification. True; repair supplied above.
3. **Missing trivial case in the exchange lemma (step 12):** blocking pairs with neither
   endpoint worse off. One line.
4. **§2.2 is stated qualitatively** ("the law of large numbers gives...") where the rest of
   the document is quantitative. Harmless — only the limit (6) is used, and (5) supplies the
   domination — but a journal version would need the rates written out.
5. **Uniformity claims are stated, not belaboured.** (18) must hold uniformly over
   `0 <= j <= J` and all length vectors with `sum k_i <= R`; this is correct because the
   per-configuration error depends on `r` only through `r <= R`, but the writeup asserts it
   rather than displaying the argument. Likewise "all constants in (13) and (17) are
   absolute, subject to their error terms being sufficiently small" is doing quiet work.
6. **No citations at all**, hence no positioning against Chin-Michelen (same architecture,
   published eleven months before the attack) or Pittel (whose `E[X] -> e^{1/2}` and whose
   stability integral are rederived). The writeup's own caveat field admits novelty was not
   checked. This is the single biggest obstacle to publication as written, and it is a
   scholarship defect rather than a mathematical one.
7. **Edge cases.** `n` even throughout, as the problem requires; `K >= 2` (cycles of length
   1 are impossible since `f(v) != M(v)`, correctly noted); all estimates are "for `n`
   sufficiently large" and the writeup never claims otherwise. The `o(1)`/`O()` constants
   are absolute but never exhibited, so the bound is genuinely asymptotic — no explicit
   threshold `n_0` is available.
8. I verified the argument at the level of the stated orders of magnitude and re-derived
   every inequality, but I did not track absolute constants through §§4-6; a fully rigorous
   journal check would need that. This is why confidence is `medium` rather than `high`.

## Referee summary

I set out to break this writeup and could not. Every one of the 31 numbered steps was
re-derived independently; every finite/structural claim was checked by code, including the
two items flagged as the crux. The exchange lemma is correct and was confirmed by exhaustive
enumeration at `n=6` and `n=8` (10 356 good collections, zero failures). The identity
`P_n = m_n E_Q[1/Z]` was confirmed by non-circular sampling of the planted measure. The
constant `m_n -> sqrt(e)` reproduces Pittel's published value. Most importantly, the
goodness-failure estimate (22), on which the whole improvement rests, is empirically
`Theta(K^2/n)` with a flat constant `~0.85` across `n = 400..1600` — decisively *not* the
`K^4/n` that Chin-Michelen's Lemma 3 pays — and the reason is structural and sound: the
writeup switches only along cycles of the canonical map `F(v) = M(f(v))`, whose vertex set
has size `O(K)`, whereas Chin-Michelen must union-bound over all pairs of stable single-cycle
neighbours. Combined with its second idea — computing `E[2^{-C_K}] = e^{-lambda_K/2}` exactly
via an alternating factorial-moment expansion, instead of paying Chin-Michelen's lower-tail
concentration cost and Markov split — the improvement from `n^{-1/17}` to
`O(n^{-1/6}sqrt(log n))` is real. Notably the method's own ceiling, `K ~ sqrt(n)`, would
deliver exactly the conjectured `n^{-1/4}`.

The defects are three small ones (an unproved but true truncated-binomial inequality, whose
stated justification is actually invalid since the terms are non-monotone — I supply a
three-line induction; one omitted trivial case in the exchange lemma; a qualitative §2.2)
plus one large non-mathematical one: the paper cites nothing and so neither acknowledges
nor positions itself against Chin-Michelen, whose overall strategy it independently
reinvents, nor against Pittel, whose first-moment constant it rederives. Hence
**MINOR_GAPS**, not CONFIRMED. The `partial` verdict is honest and `would_publish: true` is
defensible for the mathematics, provided the document is rewritten with the literature in
it; the Mertens conjecture `Theta(n^{-1/4})` itself remains open and is not meaningfully
approached from below.
