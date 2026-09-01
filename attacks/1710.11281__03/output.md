```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For the standard weak geodesic game, the extremal value is attained, hyperbolic metrics have the minimum cop number exactly two, and finite covers satisfy useful monotonicity inequalities, but no maximizing metric is identified.",
  "would_publish": false,
  "caveats": "Assumes compact connected closed orientable smooth surfaces and the weak arbitrarily-close game; literature claims are taken from the supplied review."
}
```

# Mathematical writeup

## 1. Formalization

The catalog question is informal and must be made precise. Let \(\Sigma_g\) be a compact connected closed orientable surface of genus \(g\), and let \(h\) range over its smooth Riemannian metrics.

I use the weak geodesic Cops and Robber game suggested by the phrase “come arbitrarily close.” The players have a common sequence of movement allowances \(\tau_n>0\), chosen by the robber in the usual formulation, with
\[
\sum_n \tau_n=\infty.
\]
In round \(n\), every move is along a path of length at most \(\tau_n\). The cops win if
\[
\inf_n\min_i d_h(r_n,c_{i,n})=0.
\]
Write \(c(\Sigma_g,h)\) for the least number of cops with a winning strategy, and define
\[
C_g=\sup_{h\in\operatorname{Met}^\infty(\Sigma_g)}c(\Sigma_g,h).
\]

The question then has two distinct parts:

1. determine the integer \(C_g\);
2. characterize
   \[
   \mathcal W_g=\{h:c(\Sigma_g,h)=C_g\}
   \]
   modulo diffeomorphism and homothety.

Neither part is resolved below.

---

## 2. Every closed Riemannian surface requires at least two cops

### Proposition 2.1
For every compact boundaryless Riemannian manifold \(M\) of positive dimension,
\[
c(M)\ge 2.
\]

### Proof

Let \(\rho>0\) be the injectivity radius of \(M\). Choose \(a,s>0\) with
\[
a+2s<\rho.
\]
After the cop chooses \(C_0\), the robber chooses \(R_0\) with
\[
d(C_0,R_0)=a.
\]
The robber chooses an agility sequence satisfying \(\tau_n\le s\), for example
\[
\tau_n=\frac{s}{n+1}.
\]
This has divergent sum and also tends to zero.

Suppose, just before a robber move of allowance \(\tau=\tau_n\), that
\[
d(C,R)=d\ge a.
\]

- If \(d\ge a+\tau\), the robber remains at \(R\). A subsequent cop move of length at most \(\tau\) leaves distance at least \(d-\tau\ge a\).

- If \(a\le d<a+\tau\), then
  \[
  d+\tau<a+2s<\rho.
  \]
  The unique minimizing geodesic from \(C\) to \(R\) can therefore be extended beyond \(R\) by length \(\tau\), while remaining minimizing from \(C\). The robber moves to the extended endpoint \(R'\). Then
  \[
  d(C,R')=d+\tau.
  \]
  After any cop move of length at most \(\tau\),
  \[
  d(C',R')\ge d(C,R')-\tau=d\ge a.
  \]

Thus the robber maintains distance at least \(a>0\) forever. The same argument also prevents interception during the paths, not merely at their endpoints.

If the convention has the cop moving first, use an \(a+s\) buffer: after a cop move the distance remains at least \(a\), and the robber extends the minimizing geodesic just enough to restore distance \(a+s\). Hence the conclusion is independent of the usual move-order convention. ∎

Consequently, two is the smallest possible weak cop number of a closed Riemannian surface.

---

## 3. Scaling invariance and existence of a maximizing value

### Proposition 3.1
For every \(\lambda>0\),
\[
c(\Sigma_g,\lambda^2h)=c(\Sigma_g,h).
\]

### Proof

All distances and path lengths are multiplied by \(\lambda\). A strategy with agility sequence \((\tau_n)\) for \(h\) corresponds exactly to the strategy with agility sequence \((\lambda\tau_n)\) for \(\lambda^2h\). Whether the infimum distance is zero is unchanged. ∎

Thus area or diameter normalization does not change the extremal value.

The supplied review reports a uniform finite genus-dependent upper bound. Therefore, for every fixed \(g\), there is an integer \(B_g<\infty\) such that
\[
c(\Sigma_g,h)\le B_g
\]
for every smooth metric \(h\).

### Proposition 3.2
Under that reported uniform bound, \(C_g\) is a maximum, not merely a supremum.

### Proof

The set
\[
\{c(\Sigma_g,h):h\in\operatorname{Met}^\infty(\Sigma_g)\}
\]
is a nonempty subset of the finite set
\[
\{2,3,\ldots,B_g\}.
\]
It therefore has a largest element, and some metric realizes that element. By scaling, a maximizing metric may also be required to have area one or diameter one. ∎

This existence statement uses only integrality and boundedness; no compactness of a moduli space or semicontinuity of cop number is needed.

There cannot be a unique unnormalized realization: if \(h\) is maximizing, so is every \(\lambda^2h\). The meaningful classification problem is therefore modulo diffeomorphism and homothety.

---

## 4. Cop number under finite Riemannian covers

This gives a systematic way to propagate geometrically interesting metrics between genera.

### Proposition 4.1
Let
\[
p:(\widetilde M,\widetilde h)\longrightarrow(M,h)
\]
be a connected \(d\)-sheeted Riemannian covering, with \(\widetilde h=p^*h\). Then
\[
c(M,h)\le c(\widetilde M,\widetilde h)\le d\,c(M,h).
\tag{4.1}
\]

### Proof of the lower inequality

Suppose \(k\) cops have a winning strategy upstairs. We construct a \(k\)-cop strategy downstairs.

Project the initial cop positions. Given any robber play downstairs, lift it internally to a robber play upstairs, beginning at an arbitrary lift of the robber's initial point. Legal moves lift to legal moves of the same length. Run the upstairs cop strategy against this lifted robber and project all cop moves.

Projection is length preserving locally and nonexpanding globally, so all projected moves are legal. Moreover,
\[
d_M(p(\widetilde r),p(\widetilde c))
 \le d_{\widetilde M}(\widetilde r,\widetilde c).
\]
Thus approach upstairs implies approach downstairs. Hence \(c(M)\le c(\widetilde M)\).

### Proof of the upper inequality

Let \(k=c(M,h)\), and run a virtual winning \(k\)-cop strategy downstairs. For each virtual cop at \(x\in M\), put one actual cop at every point of the fiber \(p^{-1}(x)\), using \(d\) actual cops per virtual cop.

When a virtual cop traverses a path \(\alpha\), lift \(\alpha\) from every point of the current fiber. Path lifting gives a bijection between the fibers over the two endpoints, so after every move all points of the new fiber remain occupied.

For every \(\widetilde r\in\widetilde M\) and \(x\in M\),
\[
\min_{\widetilde x\in p^{-1}(x)}
 d_{\widetilde M}(\widetilde r,\widetilde x)
 =
 d_M(p(\widetilde r),x).
\tag{4.2}
\]
Indeed, projection gives one inequality, and a minimizing geodesic downstairs from \(p(\widetilde r)\) to \(x\) lifts from \(\widetilde r\), giving the other.

Therefore, whenever a virtual cop approaches the projected robber downstairs, one of its \(d\) lifts approaches the actual robber upstairs. This proves \(c(\widetilde M)\le dk\). ∎

### Genus consequence

A connected degree-\(d\) cover of \(\Sigma_g\), for \(g\ge2\), has genus
\[
g'=1+d(g-1)
\]
by Euler characteristic. Such connected covers exist for every \(d\), for example from a surjection
\(\pi_1(\Sigma_g)\twoheadrightarrow\mathbb Z/d\mathbb Z\).

It follows that
\[
C_{1+d(g-1)}\ge C_g.
\tag{4.3}
\]
Equivalently,
\[
g-1\mid g'-1 \quad\Longrightarrow\quad C_{g'}\ge C_g.
\]

In particular,
\[
C_n\ge C_2\qquad\text{for every }n\ge2,
\]
by taking a degree-\((n-1)\) cover of a genus-two maximizing metric.

The same statement holds in the area-one class: a degree-\(d\) pullback multiplies area by \(d\), after which one rescales by \(d^{-1}\) at the level of the metric tensor; Proposition 3.1 preserves cop number.

This is only a divisibility monotonicity statement. It does not prove the full monotonicity \(C_{g+1}\ge C_g\).

---

## 5. Hyperbolic metrics realize the minimum, not the maximum

The supplied review attributes to Iršič–Mohar–Wesolek the result that two cops can come arbitrarily close to the robber on every closed constant-negative-curvature surface. Combining that upper bound with Proposition 2.1 gives:

### Corollary 5.1
For every closed hyperbolic surface \(S\),
\[
c(S)=2.
\]

Hence, for every \(g\ge2\),
\[
\min_h c(\Sigma_g,h)=2,
\]
and every hyperbolic metric realizes this minimum.

Using the supplied worst-case lower bound, there are constants \(a>0\) and \(g_0\) such that, in the range asserted by that result,
\[
C_g\ge a\sqrt g.
\]
Consequently, whenever \(a\sqrt g>2\), no hyperbolic metric can be maximizing. Asymptotically, hyperbolic metrics are therefore very far from worst:
\[
\frac{2}{C_g}=O(g^{-1/2}).
\]

A logical qualification is necessary: the hyperbolic two-cop theorem alone does not rule out hyperbolic metrics as maximizers for every small genus. One also needs a genus-by-genus construction with cop number at least three. The asymptotic \(\Omega(\sqrt g)\) statement guarantees this only for sufficiently large genera unless its underlying construction includes all small genera separately.

---

## 6. Why “take a thickened high-cop graph” is not automatically a proof

A useful monotonicity certificate is the following.

### Lemma 6.1
If a geodesic space \(X\) has a geodesic subspace \(Y\) and a \(1\)-Lipschitz retraction
\[
r:X\to Y,
\qquad r|_Y=\operatorname{id}_Y,
\]
then
\[
c(X)\ge c(Y).
\]

### Proof

Run a virtual winning cop strategy in \(X\) against a robber restricted to \(Y\), and project every virtual cop by \(r\). Projected paths have no greater length, and
\[
d_Y(R,r(C))\le d_X(R,C).
\]
Thus any \(k\)-cop winning strategy on \(X\) induces one on \(Y\). ∎

One might hope to construct bad Riemannian surfaces by taking a high-cop graph as such a retract. There is a local smooth obstruction.

### Lemma 6.2
No smooth Riemannian surface contains an isometric copy of a metric tripod with three positive-length arms.

### Proof

Suppose three arms \(\gamma_1,\gamma_2,\gamma_3\) meet at \(v\), and the embedding preserves the tripod metric. Each arm is then a unit-speed minimizing geodesic from \(v\), with initial tangent \(u_i\).

For points at equal distance \(t\) on two distinct arms, the tripod distance is \(2t\). In Riemannian normal coordinates,
\[
\lim_{t\downarrow0}
\frac{d(\gamma_i(t),\gamma_j(t))}{t}
=
\|u_i-u_j\|.
\]
Distance preservation forces \(\|u_i-u_j\|=2\), so \(u_j=-u_i\). Three unit tangent vectors cannot be pairwise antipodal. ∎

If a branching metric graph \(G\subset M\) were a \(1\)-Lipschitz retract, then for \(x,y\in G\),
\[
d_G(x,y)\le d_M(x,y)\le d_G(x,y),
\]
so the embedding would be isometric. Lemma 6.2 therefore rules out this exact mechanism for any graph with a degree-three vertex.

Thus a claim that the worst smooth surfaces are “thin thickenings of high-cop graphs” needs an additional robustness theorem. Smooth junctions create shortcuts, and equal-speed pursuit is not automatically stable under such approximations. Singular graph-like geodesic surfaces and their smooth approximations cannot simply be identified for purposes of cop number.

---

## 7. What remains open

The partial conclusions are:

- the extremal integer \(C_g\) is attained;
- maximizing metrics can be area- or diameter-normalized;
- every closed smooth surface has cop number at least two;
- hyperbolic metrics have cop number exactly two and hence realize the minimum for \(g\ge2\);
- finite covers satisfy (4.1), giving the genus relation (4.3);
- an exact graph-retraction description is locally impossible in the smooth category.

These do not determine \(C_g\) or characterize \(\mathcal W_g\). The principal unresolved issues are:

1. closing the reported gap
   \[
   \Omega(\sqrt g)\le C_g\le O(g);
   \]
2. identifying any intrinsic geometric feature—curvature concentration, thin regions, graph-like decompositions, or otherwise—that is necessary or sufficient for equality \(c(\Sigma_g,h)=C_g\);
3. proving a robust transfer theorem from combinatorial or singular graph-like models to smooth Riemannian metrics;
4. resolving the small genera separately;
5. checking that all cited lower constructions apply to smooth Riemannian surfaces rather than only to more general compact geodesic surfaces.

Accordingly, there is no complete answer here to which fixed-genus metrics are worst.