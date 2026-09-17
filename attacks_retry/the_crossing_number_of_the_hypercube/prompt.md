Attack the following open graph-theory problem.

Catalog id: the_crossing_number_of_the_hypercube
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_crossing_number_of_the_hypercube/
Original entry: http://www.openproblemgarden.org/op/the_crossing_number_of_the_hypercube
Problem attributed to: Erdos, Paul, Guy, Richard K. (posted 2007-05-11)

=== Problem statement (OpenProblemGarden) ===
Title: The Crossing Number of the Hypercube
The crossing number $ cr(G) $ of $ G $ is the minimum number of crossings in all drawings of $ G $ in the plane. The $ d $ -dimensional (hyper)cube $ Q_d $ is the graph whose vertices are all binary sequences of length $ d $ , and two of the sequences are adjacent in $ Q_d $ if they differ in precisely one coordinate. Conjecture $ \displaystyle \lim \frac{cr(Q_d)}{4^d} = \frac{5}{32} $

=== Discussion / context (OpenProblemGarden) ===
It is known that $ cr(Q_d) = 0 $ for $ d = 1,2,3 $ and that $ cr(Q_4) = 8 $ . No other exact values are known. Madej [M] proved that $ cr(Q_d) \le 4^d/6 + o(4^d/6) $ . Faria and de Figueiredo [FF] improved the upper bound to $ (165/1024) 4^d $ . Sykora and Vrto [SV] proved that $ 4^d/20 + o(4^d/20) $ is a lower bound on $ cr(Q_d) $ .

=== References listed by OpenProblemGarden ===
- *[EG] P. Erdős and R.K. Guy, Crossing number problems, Amer. Math. Monthly 80 (1973) 52-58.
- [FF] L. Faria, C.M.H. de Figueiredo, On Eggleton and Guy's conjectured upper bound for the crossing number of the -cube, Math. Slovaca 50 (2000) 271-287.
- [M] T. Madej, Bounds for the crossing number of the -cube, J. Graph Theory 15 (1991) 81-97.
- [SV] O. Sykora and I. Vrto, On crossing numbers of hypercubes and cube connected cycles, BIT 33 (1993) 232-237.

=== Catalog page (statement + literature review) ===
The Crossing Number of the Hypercube — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Yang, Wang, Wang, and Zhou (arXiv 2012, published J. Graph Theory 2022) disproved the exact Erdős-Guy formula $\mathrm{cr}(Q_n) = \frac{5}{32}4^n - \lfloor\frac{n^2+1}{2}\rfloor 2^{n-2}$ by constructing drawings of $Q_n$ with strictly fewer crossings for $n > 6$. The OPG limit conjecture $\lim \mathrm{cr}(Q_d)/4^d = 5/32$ is not directly resolved by this disproof, and the asymptotic question remains open with bounds roughly in $[1/20,\, 5/32]$. Separately, Faria, de Figueiredo, Sýkora, and Vrťo (J. Graph Theory 2008) improved the upper bound beyond the 2000 result cited at OPG, matching the EG formula's leading term before Yang et al. showed even that was not tight.

 Cited literature (1)

 
 
 
counterexample Disproof of a conjecture by Erdős and Guy on the crossing number of hypercubes
 (2012)
 

 
 Yuansheng Yang, Guoqing Wang, Haoli Wang, Yan Zhou · arXiv preprint · arXiv:1201.4700 · doi:10.1002/jgt.22787

Constructs drawings of $Q_n$ with strictly fewer crossings than the Erdős-Guy formula predicts for $n > 6$, disproving the exact equality $\mathrm{cr}(Q_n) = \frac{5}{32}4^n - \lfloor\frac{n^2+1}{2}\rfloor 2^{n-2}$.
 

 

 Reviewer notes. The OPG states the conjecture as a limit (lim cr(Q_d)/4^d = 5/32), whereas the original 1973 Erdős-Guy paper conjectured the exact formula cr(Q_n) = (5/32)4^n - floor((n²+1)/2)·2^(n-2). Yang et al. disprove the exact formula; the asymptotic limit question is not explicitly addressed and remains open. The Faria, de Figueiredo, Sýkora, Vrťo (2008, J. Graph Theory doi:10.1002/jgt.20330) paper improved the upper bound beyond the 2000 result cited at OPG (achieving exactly the EG formula's leading term), and is a relevant post-posting result, but the Wiley/JGT page returned 403 and the PDF was binary-only, so it could not be verified and is not included in since_posted. The Mohar/SFU problem page was last updated June 2001 and does not reflect post-2007 developments.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. $ \displaystyle \lim \frac{cr(Q_d)}{4^d} = \frac{5}{32} $

Keywords:
crossing number · hypercube

Discussion

It is known that $ cr(Q_d) = 0 $ for $ d = 1,2,3 $ and that $ cr(Q_4) = 8 $ . No other exact values are known. Madej [M] proved that $ cr(Q_d) \le 4^d/6 + o(4^d/6) $ . Faria and de Figueiredo [FF] improved the upper bound to $ (165/1024) 4^d $ . Sykora and Vrto [SV] proved that $ 4^d/20 + o(4^d/20) $ is a lower bound on $ cr(Q_d) $ .

Bibliography

★ [EG]
 P. Erdős and R.K. Guy, Crossing number problems, Amer. Math. Monthly 80 (1973) 52-58.

 [FF]
 L. Faria, C.M.H. de Figueiredo, On Eggleton and Guy's conjectured upper bound for the crossing number of the $ n $ -cube, Math. Slovaca 50 (2000) 271-287.

 [M]
 T. Madej, Bounds for the crossing number of the $ n $ -cube, J. Graph Theory 15 (1991) 81-97.

 [SV]
 O. Sykora and I. Vrto, On crossing numbers of hypercubes and cube connected cycles, BIT 33 (1993) 232-237.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The normalized crossing numbers converge and admit an explicit finite-dimensional upper envelope, but their limit is not determined here.",
  "would_publish": false,
  "caveats": "No numerical improvement to the quoted asymptotic interval; the convergence observation may be standard, and no novelty claim is made."
}
```

# Partial result: convergence and a finite-drawing amplification criterion

I do not prove or disprove the value \(5/32\). I prove that the limit exists, independently of the quoted asymptotic bounds, and give a quantitative criterion by which a sufficiently good drawing in one dimension would disprove the proposed value.

Write
\[
c_d=\operatorname{cr}(Q_d),\qquad a_d=\frac{c_d}{4^d},
\qquad
\epsilon_d=
\begin{cases}
0,&d\text{ even},\\
1,&d\text{ odd}.
\end{cases}
\]

## 1. Statement of the partial result

**Theorem.** Define
\[
R_d=\frac{d^2+d+(4+\epsilon_d)/3}{2^{d+3}}.
\]
Then
\[
a_{d+1}+R_{d+1}\le a_d+R_d
\qquad(d\ge1).
\]
Consequently, the limit
\[
L=\lim_{d\to\infty}\frac{\operatorname{cr}(Q_d)}{4^d}
\]
exists, and
\[
\boxed{\quad
L=\inf_{d\ge1}\left(
\frac{\operatorname{cr}(Q_d)}{4^d}
+\frac{d^2+d+(4+\epsilon_d)/3}{2^{d+3}}
\right).
\quad}                                                    \tag{1}
\]

In particular, every drawing of \(Q_d\) with \(C\) crossings supplies the bound
\[
\boxed{\quad
L\le
\frac{C+2^{d-3}\bigl(d^2+d+(4+\epsilon_d)/3\bigr)}{4^d}.
\quad}                                                    \tag{2}
\]

This also gives the one-sided estimate
\[
c_d\ge L4^d-
2^{d-3}\bigl(d^2+d+(4+\epsilon_d)/3\bigr).                    \tag{3}
\]
It does **not** give a two-sided error estimate for \(a_d-L\).

The proof uses a doubling construction that applies to an arbitrary drawing of the cube; no special rotation pattern is required.

## 2. Doubling an arbitrary cube drawing

For an integer \(r\ge1\), set
\[
f(r)=
\binom{\lfloor r/2\rfloor}{2}
+\binom{\lceil r/2\rceil}{2}
=\frac{r^2-2r+\epsilon_r}{4}.                               \tag{4}
\]

We first describe the geometric construction, including its possible edge twists.

### Local construction at a vertex

Take a drawing of \(Q_d\) with \(c_d\) crossings in general position. Choose mutually disjoint small disks around its vertices and crossings, with narrow edge corridors between these disks.

At each old vertex \(v\), put two new vertices \(v^0,v^1\) close together on a horizontal segment. Replace every incident edge by two strands, one incident with each new vertex, and add the edge \(v^0v^1\).

The strands inside the vertex disk can be arranged to have exactly \(f(d)\) crossings, without crossings on \(v^0v^1\). Here is an explicit local arrangement.

Place the new vertices at \((-\eta,0)\) and \((\eta,0)\). Choose \(d\) distinct, nonhorizontal ray directions, with
\[
\lfloor d/2\rfloor
\]
in the upper half-plane and the remaining directions in the lower half-plane. From each new vertex draw a ray in each chosen direction.

For two directions in the same half-plane, exactly one of the two cross-pairs of rays intersects. Directions in opposite half-planes give no intersection. Rays corresponding to the same direction are parallel. Thus the number of crossings is precisely
\[
\binom{\lfloor d/2\rfloor}{2}
+\binom{\lceil d/2\rceil}{2}.
\]
The horizontal segment joining the new vertices has no interior intersection with a ray.

Choose the directions generically and then choose \(\eta\) sufficiently small. All the indicated intersections lie inside the vertex disk, and the two rays associated with each old edge exit as an adjacent pair. The cyclic order of the old edge ports can be preserved: choose which consecutive ports belong to the upper and lower groups, and connect the resulting ordered pairs through an annulus without crossings.

Thus this construction works for every original rotation at \(v\).

### Crossings and twists along old edges

At every original crossing, the two strands replacing one edge cross the two strands replacing the other edge, producing four crossings.

Along each old edge corridor, there are two possibilities for connecting equally labelled endpoints:

* the two strands can be connected without crossing; or
* they require one crossing, which can be inserted in a private portion of the corridor.

Call the second possibility a **twist**. If \(t\) old edges require twists, the resulting drawing of \(Q_d\square K_2=Q_{d+1}\) has at most
\[
4c_d+2^d f(d)+t                                             \tag{5}
\]
crossings.

It remains to control \(t\).

### Choosing the labels

At each vertex, we may exchange the labels \(0,1\) on the two new vertices. For an old edge \(uv\), whether it requires a twist is determined by a binary constraint
\[
s_u\oplus s_v=b_{uv},
\]
where \(s_v\) records whether the labels at \(v\) were exchanged. The constants \(b_{uv}\) depend on the geometric choices, but need not satisfy any compatibility condition.

Use the bipartition of \(Q_d\). Choose all label switches on the first part independently and uniformly. Then choose each switch on the second part to minimize its number of incident twisted edges.

Let
\[
\mu_d=\mathbb E\left|\xi_1+\cdots+\xi_d\right|,
\]
where the \(\xi_i\) are independent uniform signs. At a vertex in the second part, the \(d\) incident constraints are independent fair binary constraints before its own switch is chosen. Hence the expected number left unsatisfied after choosing that switch optimally is
\[
\frac{d-\mu_d}{2}.
\]
There are \(2^{d-1}\) vertices in that part. By linearity of expectation, some label choice therefore has
\[
t\le 2^{d-2}(d-\mu_d).
\]

Substituting this and (4) into (5) proves the stronger recurrence
\[
\boxed{\quad
c_{d+1}\le
4c_d+2^{d-2}\bigl(d^2-d+\epsilon_d-\mu_d\bigr).
\quad}                                                    \tag{6}
\]

All crossings in the construction have been accounted for: four per old crossing, the local vertex crossings, and at most one per twisted corridor.

For the simpler closed-form bound, observe that \(\mu_d\ge1\) for \(d\ge1\). Indeed, \(\mu_1=1\), and
\[
\frac{|x+1|+|x-1|}{2}\ge |x|
\]
shows that \(\mu_d\) is nondecreasing. Consequently,
\[
\boxed{\quad
c_{d+1}\le
4c_d+2^{d-2}\bigl(d^2-d-1+\epsilon_d\bigr).
\quad}                                                    \tag{7}
\]

The case \(d=1\) is included: the added term is zero.

## 3. Proof of convergence and the explicit envelope

Dividing (7) by \(4^{d+1}\) gives
\[
a_{d+1}\le a_d+e_d,
\qquad
e_d=\frac{d^2-d-1+\epsilon_d}{2^{d+4}}.                      \tag{8}
\]
These errors are nonnegative and summable.

Their tail has a closed form:
\[
\sum_{k=d}^{\infty}e_k
=
\frac{d^2+d+(4+\epsilon_d)/3}{2^{d+3}}
=R_d.                                                     \tag{9}
\]
For verification, the required sums are
\[
\sum_{k=d}^{\infty}\frac{k^2-k-1}{2^k}
=2^{1-d}(d^2+d+1)
\]
and
\[
\sum_{k=d}^{\infty}\frac{\epsilon_k}{2^k}
=\frac{2(1+\epsilon_d)}{3}\,2^{-d}.
\]

Since \(R_d=e_d+R_{d+1}\), equation (8) implies
\[
a_{d+1}+R_{d+1}\le a_d+R_d.
\]
The corrected sequence is nonnegative and nonincreasing, so it converges. Because \(R_d\to0\), the uncorrected sequence \(a_d\) converges to the same limit. Its corrected sequence has infimum equal to that limit, proving (1). Equations (2) and (3) follow immediately.

Taking the asymptotic bounds quoted in the question as given, this establishes a well-defined constant satisfying
\[
\frac1{20}\le L\le\frac5{32}.
\]
It does not improve that interval.

## 4. What finite improvement would disprove \(L=5/32\)?

Equation (2) yields a sufficient, drawing-independent criterion.

**Corollary.** If, for some \(d\), there is a drawing of \(Q_d\) with
\[
C<
\frac5{32}4^d
-
2^{d-3}\left(d^2+d+\frac{4+\epsilon_d}{3}\right),            \tag{10}
\]
then \(L<5/32\).

For comparison, write the exact Erdős–Guy expression appearing in the question as
\[
F_d=
\frac5{32}4^d
-\left\lfloor\frac{d^2+1}{2}\right\rfloor2^{d-2}
=
\frac5{32}4^d-(d^2+\epsilon_d)2^{d-3}.
\]
Thus a sufficient margin below \(F_d\), supplied by this universal construction, is
\[
C<F_d-
\begin{cases}
\left(d+\dfrac43\right)2^{d-3},&d\text{ even},\\[2mm]
\left(d+\dfrac23\right)2^{d-3},&d\text{ odd}.
\end{cases}                                               \tag{11}
\]

This is only a sufficient threshold. Smaller improvements might propagate through a more specialized construction. Conversely, merely knowing that \(C<F_d\), without quantitative information or a compatible continuation scheme, does not establish a different leading constant.

### A sharper, explicitly computable threshold

Keeping \(\mu_d\) in (6) improves the envelope to
\[
R_d^{*}
=
\sum_{k=d}^{\infty}
\frac{k^2-k+\epsilon_k-\mu_k}{2^{k+4}}
\le R_d,
\]
and the same argument proves
\[
L\le \frac{C}{4^d}+R_d^{*}.                                \tag{12}
\]

The coefficients are explicit:
\[
\mu_k=
\frac{k}{2^{k-1}}
\binom{k-1}{\lfloor(k-1)/2\rfloor}.
\]
For example, this gives the following concrete target:
\[
\boxed{\text{A drawing of \(Q_7\) with at most \(1657\) crossings
would imply \(L<5/32\).}}
\]

Here is the exact calculation, so this target does not rely on an unspecified numerical computation. The generating function is
\[
\sum_{k\ge1}\mu_k x^k
=\frac{x}{(1-x)\sqrt{1-x^2}},
\]
obtained from
\[
\mu_k-\mu_{k-1}
=\Pr(\xi_1+\cdots+\xi_{k-1}=0).
\]
Consequently,
\[
\sum_{k\ge1}\frac{\mu_k}{2^k}=\frac2{\sqrt3},
\qquad
\sum_{k=1}^{6}\frac{\mu_k}{2^k}=\frac{573}{512}.
\]
Substitution gives
\[
4^7R_7^{*}
=\frac{6254}{3}-\frac{2048}{\sqrt3}
\approx902.253315.
\]
Since
\[
\frac5{32}4^7=2560,
\]
condition (12) disproves the proposed value whenever
\[
C<
2560-4^7R_7^{*}
=
\frac{1426}{3}+\frac{2048}{\sqrt3}
\approx1657.746685.
\]

**No drawing attaining this target is constructed or claimed here.**

## 5. Remaining gap

The partial result settles existence of the normalized limit and provides a quantitative amplification mechanism. It does not supply either ingredient needed to determine its value:

* a lower bound approaching \((5/32)4^d\); or
* an actual drawing meeting one of the strict amplification thresholds above.

I have not independently examined the full formulas and constructions in the post-2007 references supplied in the question, so I do not infer their asymptotic consequences from the catalog summary alone. The argument here is self-contained, but may be standard; I would not submit it as a paper without a novelty check and a substantive further advance.
