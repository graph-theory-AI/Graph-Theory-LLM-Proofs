```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For p(n)=1/n, a graph in G(n,p) has linearly many isolated K_2 components a.a.s., each of which forces one face in every componentwise random embedding.",
  "would_publish": false,
  "caveats": "This refutes the catalog statement under the canonical componentwise definition; a version conditioned on connectedness or concerning one distinguished component is different."
}
```

## Statement and convention

For a graph \(G\), write
\[
f(G):=\mathbb E_{\rho}[F(G,\rho)],
\]
where \(\rho\) is the collection of independent uniform local rotations.

The source abstract initially defines this for connected graphs. There is a canonical extension to disconnected graphs: the face permutation acts separately on the darts of each connected component, equivalently each component is embedded in its own orientable surface. Under this extension, the number of faces is additive over components.

Under that standard interpretation, the catalog conjecture is false.

## Isolated edges force faces

Let \(uv\) be an isolated \(K_2\)-component of \(G\). Both \(u\) and \(v\) have degree one, so their local rotations are uniquely determined. On the two darts of \(uv\), the edge-reversal involution swaps the darts, while both vertex rotations are identities. Consequently, the face permutation has one \(2\)-cycle on these darts.

Thus every isolated \(K_2\)-component contributes exactly one face, independently of all rotation choices. If \(X(G)\) denotes the number of isolated \(K_2\)-components, then deterministically
\[
F(G,\rho)\ge X(G)
\quad\text{and hence}\quad
f(G)\ge X(G).
\]

## Isolated edges in \(G(n,1/n)\)

Set \(p=1/n\), and let
\[
X=\sum_{e\in\binom{[n]}2} I_e,
\]
where \(I_e\) indicates that \(e\) is an isolated \(K_2\)-component.

For a fixed edge \(e\),
\[
q:=\mathbb P(I_e=1)
=p(1-p)^{2(n-2)}.
\]
Therefore
\[
\mu:=\mathbb E X
=\binom n2\frac1n\left(1-\frac1n\right)^{2n-4}
=\left(\frac{e^{-2}}2+o(1)\right)n.
\]

We also have \(\operatorname{Var}X=O(n)\). Indeed:

- If two candidate edges share a vertex, they cannot both be isolated components, so their covariance is negative.
- If \(e,f\) are disjoint, then
  \[
  \mathbb P(I_e=I_f=1)
  =p^2(1-p)^{4n-12},
  \]
  whereas
  \[
  q^2=p^2(1-p)^{4n-8}.
  \]
  Hence
  \[
  \operatorname{Cov}(I_e,I_f)
  =q^2\bigl((1-p)^{-4}-1\bigr)
  =O(n^{-3})
  \]
  when \(p=1/n\). There are \(O(n^4)\) disjoint pairs, so their total covariance is \(O(n)\); the sum of individual variances is also \(O(n)\).

It follows from Chebyshev's inequality that
\[
\frac{X}{n}\xrightarrow{\mathrm p}\frac{e^{-2}}2.
\]
In particular, \(X=\Theta(n)\) asymptotically almost surely.

Consequently,
\[
f(G)\ge X(G)=\Theta(n)
\qquad\text{a.a.s. for }G\sim G(n,1/n).
\]
For every fixed \(C\),
\[
\mathbb P\bigl(f(G)\le C\log n\bigr)
\le
\mathbb P\bigl(X\le C\log n\bigr)
\longrightarrow 0.
\]
This is the opposite of the asserted conclusion.

The same obstruction persists even when \(np\to\infty\). For example, with
\[
p=\frac{\log n}{4n},
\]
the expected number of isolated edges is
\[
\binom n2p(1-p)^{2n-4}
=(1+o(1))\frac18 n^{1/2}\log n,
\]
and the same second-moment argument gives concentration.

## Connectedness caveat

If the paper defines \(F(G)\) only when \(G\) is connected, then the catalog formulation is not well-posed for arbitrary \(p(n)\): for \(p=1/n\), \(G(n,p)\) is disconnected asymptotically almost surely, so \(F(G)\) is undefined on almost every sample.

Possible corrected formulations include:

1. restrict to \(p\) for which \(G(n,p)\) is connected a.a.s.;
2. condition \(G(n,p)\) on being connected;
3. consider only the giant component or the \(2\)-core;
4. alter the face statistic by removing contributions from separate tree components.

These formulations are inequivalent. The isolated-\(K_2\) argument does not resolve a version conditioned on connectedness or restricted to a distinguished component; such a corrected conjecture may remain open.