```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "On closed surfaces, the cited hyperbolic theorem gives cop number exactly two and, together with Gauss–Bonnet and known genus bounds, a genus-independent bound for every constant-curvature metric.",
  "would_publish": false,
  "caveats": "Closed compact boundaryless asymptotic game only; exact flat/spherical values and smooth general lower-bound examples are not established here."
}
```

# Mathematical writeup

## 1. Precise interpretation

The word “simpler” does not define a mathematical property. A natural precise interpretation is:

> Is the cop number of closed constant-curvature surfaces bounded independently of their genus, in contrast with arbitrary metrics on surfaces?

Let \(c(M)\) denote the metric cop number in the geodesic-space version used in the cited papers: in round \(n\), each player may move a distance at most \(\tau_n\), where the legal agility sequence has divergent total length, and the cops win by forcing the distance from the robber to some cop to have infimum zero. The argument below also gives the same one-cop lower bound for exact-capture variants.

We restrict to closed, connected Riemannian surfaces. Boundaries and noncompact surfaces materially change the problem.

## 2. Precise partial answer

Let \(\gamma(M)=2-\chi(M)\) be the Euler genus.

### Proposition

For the standard metric Cops and Robber game:

1. Every closed constant-negative-curvature surface \(M\) has
   \[
   c(M)=2.
   \]
2. There is an absolute constant \(C\) such that every closed constant-curvature surface satisfies
   \[
   c(M)\le C,
   \]
   independently of its topology, area, curvature magnitude, and genus.
3. More precisely, for every \(\gamma>2\),
   \[
   \sup\{c(M):\gamma(M)=\gamma,\ M\text{ has constant curvature}\}=2.
   \]

Thus constant curvature gives a genuine genus-independent simplification. The substantive part is the two-cop theorem for hyperbolic surfaces from Iršič–Mohar–Wesolek, arXiv:2402.05753.

## 3. One cop never suffices on a closed Riemannian surface

This supplies the lower bound needed to turn the cited hyperbolic upper bound into an exact value.

### Lemma

If \(M\) is a closed Riemannian manifold of positive dimension, then \(c(M)\ge 2\).

### Proof

Let \(\iota>0\) be the injectivity radius of \(M\). Choose \(0<\rho\) with
\[
2\rho<\iota,
\]
and let the robber use a legal agility sequence \((\tau_n)\) satisfying
\[
0<\tau_n<\rho/2
\]
for every \(n\), with \(\sum_n\tau_n=\infty\). For example, a suitably scaled harmonic sequence works.

After the single cop chooses its initial point \(x\), the robber chooses a point at distance \(\rho\) from \(x\). We maintain separation at least \(\rho\) after each complete round.

Suppose first that the cop moves first. Before the cop's move, assume the separation is at least \(\rho\). After a move of length at most \(\tau_n\), the separation \(d\) is at least \(\rho-\tau_n>0\).

- If \(d\ge\rho\), the robber may stay put.
- If \(d<\rho\), take the unique minimizing geodesic from the cop to the robber and extend it beyond the robber by length \(\tau_n\).

Since
\[
d+\tau_n<\rho+\tau_n<2\rho<\iota,
\]
the extended geodesic remains minimizing. The new separation is \(d+\tau_n\ge\rho\).

If the robber moves first, the analogous strategy is:

- stay if the current separation is at least \(\rho+\tau_n\);
- otherwise extend the minimizing cop–robber geodesic beyond the robber by \(\tau_n\).

The subsequent cop move can reduce the separation by at most \(\tau_n\), leaving it at least \(\rho\).

In either move convention, even during the cop's move the separation remains greater than \(\rho/2\). Thus one cop cannot force the distance to zero or obtain exact capture. ∎

## 4. The hyperbolic case

A constant-negative-curvature metric can be rescaled to curvature \(-1\), and rescaling does not change the cop number: one simply rescales every legal move length by the same factor.

The cited 2024 result states that two cops suffice on every compact hyperbolic surface. Hence
\[
c(M)\le2.
\]
The lemma gives \(c(M)\ge2\), so:

\[
\boxed{c(M)=2\quad\text{for every closed hyperbolic surface}.}
\]

This includes surfaces of arbitrarily large genus. If the published theorem is formulated only for orientable hyperbolic surfaces, the nonorientable case follows from the orientable double cover: a winning strategy upstairs projects to a winning strategy downstairs.

## 5. Covering all three curvature signs

For a closed constant-curvature surface, Gauss–Bonnet gives
\[
K\,\operatorname{area}(M)=2\pi\chi(M).
\]

Consequently:

| Curvature | Possible closed topologies | Cop-number conclusion |
|---|---|---|
| \(K>0\) | \(S^2\), \(\mathbb{RP}^2\) | bounded by the general low-genus surface bound |
| \(K=0\) | \(T^2\), Klein bottle | bounded by the general low-genus surface bound |
| \(K<0\) | all closed surfaces with \(\chi<0\) | exactly \(2\) |

The general surface result reported for arXiv:2205.11633 gives an estimate of the form
\[
c(X)\le A\gamma(X)+B
\]
for compact geodesic surfaces, with absolute constants \(A,B\). For \(K\ge0\), Gauss–Bonnet gives \(\gamma(M)\le2\). Therefore
\[
c(M)\le 2A+B.
\]
Combining this with the hyperbolic two-cop theorem gives the uniform constant
\[
C=\max\{2,2A+B\}.
\]

Thus all closed constant-curvature surfaces have uniformly bounded cop number. If the three-cop low-genus estimate summarized on the catalog page applies to all Euler genera at most \(2\) under exactly the same rules, then one may sharpen the displayed conclusion to \(C=3\); I do not need that numerical sharpening for the main conclusion.

## 6. Comparison with general surface metrics

Let
\[
C_{\mathrm{all}}(\gamma)
 =\sup\{c(X):X\text{ is a compact geodesic surface of Euler genus }\gamma\}.
\]
The result summarized for arXiv:2205.11633 gives, along an infinite sequence of genera,
\[
C_{\mathrm{all}}(\gamma)=\Omega(\sqrt{\gamma}),
\]
as well as an \(O(\gamma)\) upper bound.

By contrast, for constant-curvature metrics,
\[
C_{\mathrm{const}}(\gamma)=2\qquad(\gamma>2).
\]

Hence the known results give the sharp qualitative separation
\[
C_{\mathrm{const}}(\gamma)=O(1),
\qquad
C_{\mathrm{all}}(\gamma)=\Omega(\sqrt{\gamma}).
\]

This is a rigorous affirmative answer if “simpler” means “having cop number bounded independently of genus.”

## 7. Remaining gaps

1. The exact cop numbers of the round sphere, projective plane, flat tori, and flat Klein bottles are not determined by the argument above; it only gives
   \[
   2\le c(M)\le C.
   \]
2. The supplied description of the lower-bound theorem concerns compact geodesic surfaces. Without checking its construction, one should not automatically claim that the \(\Omega(\sqrt{\gamma})\) examples are smooth Riemannian metrics; cop number need not be stable under smoothing or metric approximation.
3. Surfaces with boundary, noncompact or finite-area cusped surfaces, strong/finite-capture variants, and algorithmic meanings of “tractable” are not covered.
4. The essential hyperbolic upper bound is an existing theorem rather than a new proof here.

Accordingly, the natural cop-number interpretation is strongly and essentially affirmatively resolved in negative curvature, while the original informal question remains too broad for an unconditional “proved” verdict.