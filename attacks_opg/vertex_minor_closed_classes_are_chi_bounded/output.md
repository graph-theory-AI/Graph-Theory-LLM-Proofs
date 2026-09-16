```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Yes: James Davies proved that every proper vertex-minor-closed class of finite simple graphs is chi-bounded.",
  "would_publish": false,
  "caveats": "This is a literature resolution, not a new proof; the argument below invokes Davies's published theorem rather than reproducing its proof."
}
```

## Statement and literature status

The question is no longer open. The affirmative result is the theorem in the paper identified in the supplied catalog:

James Davies, **“Vertex-minor-closed classes are χ-bounded,”** *Combinatorica* (2022), 1049–1079.  
arXiv:2008.05069; DOI:10.1007/s00493-021-4767-3.

A fixed-forbidden-graph formulation of the result is:

> **Theorem (Davies).** For every finite simple graph \(H\) and every positive integer \(k\), there exists an integer \(c(H,k)\) such that every finite simple graph \(G\) satisfying
> \[
> \omega(G)\le k
> \qquad\text{and}\qquad
> \chi(G)>c(H,k)
> \]
> has a vertex-minor isomorphic to \(H\).

Here “has a vertex-minor isomorphic to \(H\)” allows any sequence of vertex deletions and local complementations, exactly as in the question.

## Deduction of the requested assertion

We give the complete deduction from this established theorem. As usual, graph classes are understood to be closed under isomorphism.

Let \(\mathcal C\) be a proper vertex-minor-closed class of finite simple graphs. If \(\mathcal C\) is empty, it is trivially \(\chi\)-bounded. Otherwise, because \(\mathcal C\) is proper, choose a finite simple graph
\[
H\notin\mathcal C.
\]

No graph in \(\mathcal C\) can have \(H\) as a vertex-minor. Indeed, if \(G\in\mathcal C\) had such a vertex-minor, closure under vertex-minors and isomorphism would imply \(H\in\mathcal C\), a contradiction. Consequently,
\[
\mathcal C\subseteq
\operatorname{Ex}_{\mathrm{vm}}(H)
:=
\{G:H\text{ is not a vertex-minor of }G\}.
\]

For \(k\ge1\), define
\[
f(k)=\max_{1\le j\le k}c(H,j).
\]
This is a nondecreasing function depending only on the chosen excluded graph \(H\), and hence suitable for bounding the class \(\mathcal C\).

Take any nonempty \(G\in\mathcal C\), and put \(k=\omega(G)\). If
\[
\chi(G)>f(k),
\]
then \(\chi(G)>c(H,k)\), so Davies’s theorem gives \(H\) as a vertex-minor of \(G\), contradicting the preceding exclusion. Therefore
\[
\boxed{\chi(G)\le f\bigl(\omega(G)\bigr)}
\qquad\text{for every nonempty }G\in\mathcal C.
\]
The empty graph causes no difficulty: its chromatic and clique numbers are both zero, and we may set \(f(0)=0\). Thus \(\mathcal C\) is \(\chi\)-bounded.

For completeness, the fixed-\(H\) formulation is equivalent to the class formulation: \(\operatorname{Ex}_{\mathrm{vm}}(H)\) is proper because it excludes \(H\) itself, and it is vertex-minor closed by transitivity of the vertex-minor relation.

## Scope of the argument

The substantial ingredient is Davies’s theorem. Its proof is **not** reconstructed here; the deduction from that theorem to the precise question is complete. No additional conjecture is assumed, and no new quantitative bound or original research result is claimed.