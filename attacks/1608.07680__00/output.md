```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For loopless multigraphs, uniform thickening of K5 gives an exact cone-crossing formula and the explicit bound f(k) <= k + 2 sqrt(k) + O(k^(1/4)); I also determine f(0) and f(1).",
  "would_publish": false,
  "caveats": "The main construction uses parallel edges, gives no matching lower bound, and the quoted phi_s values cannot be total cone crossing numbers."
}
```

# 1. Statement and conventions

Write
\[
F_{\mathrm m}(k)=\min\{\operatorname{cr}(CG):\operatorname{cr}(G)\ge k\}
\]
for loopless multigraphs, where the cone adds one new edge from the apex to each vertex, irrespective of edge multiplicities. Let \(F_{\mathrm s}\) denote the simple-graph version.

Since \(G\subseteq CG\),
\[
F_{\mathrm m}(k),F_{\mathrm s}(k)\ge k.
\]
Consequently, the quoted equality \(\phi_s(6)=5\) cannot be an equality for the total function \(F_{\mathrm s}\). If, as appears to be the case, \(\phi_s(q)\) denotes the minimum excess
\[
\delta_s(q)=\min_{\operatorname{cr}(G)=q}
  \bigl(\operatorname{cr}(CG)-\operatorname{cr}(G)\bigr),
\]
then the relation with the function in the question is
\[
F_{\mathrm s}(k)=\min_{q\ge k}\bigl(q+\delta_s(q)\bigr).
\]

The main partial result below is for \(F_{\mathrm m}\).

# 2. Uniform thickening lemma

For a simple graph \(H\) and an integer \(m\ge1\), let \(H^{(m)}\) be the multigraph obtained by replacing every edge of \(H\) by \(m\) parallel copies.

## Lemma 2.1

Let
\[
h=\operatorname{cr}(H),\qquad q=\operatorname{cr}(CH).
\]
Suppose \(CH\) has an optimal drawing with exactly \(h\) crossings between two edges of \(H\), and hence \(q-h\) crossings involving an apex edge. Then
\[
\boxed{\operatorname{cr}\bigl(C(H^{(m)})\bigr)
      =m^2h+m(q-h).}
\]

Moreover,
\[
\operatorname{cr}(H^{(m)})=m^2h.
\]

### Proof

It is standard that an optimal drawing may be assumed good: no self-crossings, no crossings between adjacent edges, and no triple crossing points.

Let \(e=|E(H)|\). In a drawing of \(H^{(m)}\), choose one edge from each parallel class. There are \(m^e\) such transversal copies of \(H\). Every crossing between copies of two distinct original edges occurs in exactly \(m^{e-2}\) transversals. Since each transversal has at least \(h\) crossings,
\[
A\,m^{e-2}\ge h\,m^e,
\]
where \(A\) is the total number of crossings. Thus \(A\ge m^2h\). Replacing every edge in an optimal drawing of \(H\) by a narrow bundle gives the reverse inequality, proving
\[
\operatorname{cr}(H^{(m)})=m^2h.
\]

Now consider an optimal drawing of \(C(H^{(m)})\). Let

- \(A\) be the number of crossings between two base edges;
- \(B\) be the number of crossings between a base edge and an apex edge.

Apex edges do not cross each other in a good drawing. The base transversals again give
\[
A\ge m^2h. \tag{1}
\]

For every choice of one copy from each base-edge class, retain also all apex edges. The resulting subdrawing is a drawing of \(CH\), and hence has at least \(q\) crossings. A base-base crossing occurs in \(m^{e-2}\) transversals, while a base-apex crossing occurs in \(m^{e-1}\). Therefore
\[
A m^{e-2}+B m^{e-1}\ge q m^e,
\]
or equivalently
\[
\frac{A}{m^2}+\frac{B}{m}\ge q. \tag{2}
\]

If \(A\le q m^2\), then (1) and (2) give
\[
\begin{aligned}
A+B
&\ge A+mq-\frac{A}{m}\\
&=mq+\left(1-\frac1m\right)A\\
&\ge mq+\left(1-\frac1m\right)m^2h\\
&=m^2h+m(q-h).
\end{aligned}
\]
If \(A\ge q m^2\), then
\[
A+B\ge qm^2\ge m^2h+m(q-h),
\]
because \(q\ge h\) and \(m^2\ge m\).

For the upper bound, thicken the base edges in the assumed optimal drawing of \(CH\). Each base-base crossing becomes \(m^2\) crossings, and each base-apex crossing becomes \(m\) crossings. This gives exactly
\[
m^2h+m(q-h)
\]
crossings. ∎

# 3. An exact infinite family from \(K_5\)

We need only the elementary facts
\[
\operatorname{cr}(K_5)=1,\qquad \operatorname{cr}(K_6)=3.
\]

For completeness, the lower bound for \(K_6\) follows by considering its six \(K_5\)-subgraphs. In a good drawing, every crossing uses four vertices and therefore survives in exactly two of the six vertex-deleted \(K_5\)'s. Since every one of these six graphs has at least one crossing,
\[
2\operatorname{cr}(K_6)\ge6.
\]
A standard three-crossing drawing gives equality. One construction starts with the planar octahedron
\[
K_6-\{uv,13,24\}
\]
and inserts the three missing edges, each across one suitable octahedral edge.

The same counting proves an important compatibility fact. In any three-crossing drawing of \(K_6\), each of the six vertex-deleted \(K_5\)'s has exactly one crossing. Thus, regarding any chosen vertex as the cone apex, exactly one crossing is internal to the base \(K_5\), and the other two involve apex edges.

Applying Lemma 2.1 gives:

## Proposition 3.1

Let \(G_m=K_5^{(m)}\). Then
\[
\boxed{\operatorname{cr}(G_m)=m^2,\qquad
       \operatorname{cr}(CG_m)=m^2+2m.}
\]

In particular,
\[
F_{\mathrm m}(m^2)\le m^2+2m.
\]
This is an exact calculation of the cone crossing number of the witness, not a claim that it is extremal among all graphs.

# 4. An explicit all-\(k\) upper bound

Crossing number is additive over disjoint unions. Moreover, if \(G\) is a disjoint union of \(G_1,\dots,G_t\), then \(CG\) is the union of \(CG_i\)'s sharing only their apex, and
\[
\operatorname{cr}(CG)=\sum_i\operatorname{cr}(CG_i).
\]
Indeed, restriction to each block gives the lower bound, while optimal drawings can be placed in disjoint sectors around the common apex.

Define the arithmetic function
\[
s(k)=\min\left\{
\sum_{i=1}^t m_i:
k=\sum_{i=1}^t m_i^2,\quad m_i\in\mathbb Z_{\ge0}
\right\}.
\]
Using disjoint copies of \(G_{m_i}\), Proposition 3.1 yields
\[
\boxed{F_{\mathrm m}(k)\le k+2s(k).} \tag{3}
\]

This construction has base crossing number exactly \(k\), rather than merely at least \(k\).

Let
\[
n=\lfloor\sqrt{k}\rfloor,\qquad r=k-n^2.
\]
By Lagrange's four-square theorem,
\[
r=a_1^2+a_2^2+a_3^2+a_4^2.
\]
Cauchy–Schwarz gives
\[
a_1+a_2+a_3+a_4\le2\sqrt r.
\]
Consequently,
\[
s(k)\le n+2\sqrt r,
\]
and hence
\[
\boxed{
F_{\mathrm m}(k)
\le k+2\lfloor\sqrt{k}\rfloor
       +4\sqrt{k-\lfloor\sqrt{k}\rfloor^2}.
} \tag{4}
\]
Since \(r\le2n\),
\[
\boxed{
F_{\mathrm m}(k)
\le k+2\sqrt{k}+4\sqrt2\,k^{1/4}.
} \tag{5}
\]
In particular,
\[
\limsup_{k\to\infty}
\frac{F_{\mathrm m}(k)-k}{\sqrt{k}}\le2.
\]

Iterating the largest-square decomposition improves the lower-order \(O(k^{1/4})\) term, but not the leading constant \(2\) produced by the \(K_5\) seed.

## General seed consequence

Lemma 2.1 provides a systematic way to improve the leading constant. Suppose \(H\) has
\[
h=\operatorname{cr}(H)>0,\qquad
d=\operatorname{cr}(CH)-h,
\]
and has a compatible optimal cone drawing as in the lemma. Take
\[
m=\left\lfloor\sqrt{k/h}\right\rfloor
\]
and fill the remaining \(k-hm^2=O_H(\sqrt{k})\) crossings with the \(K_5^{(a)}\) square gadgets. Then
\[
\boxed{
F_{\mathrm m}(k)
\le k+\frac{d}{\sqrt h}\sqrt{k}
       +O_H(k^{1/4}).
} \tag{6}
\]
Thus finding a finite compatible seed with \(d/\sqrt h<2\) would immediately improve the global multigraph upper constant.

# 5. Exact values at \(k=0,1\)

Clearly
\[
F_{\mathrm s}(0)=F_{\mathrm m}(0)=0.
\]

For \(k=1\), the exact value is also elementary.

## Proposition 5.1

\[
\boxed{F_{\mathrm s}(1)=F_{\mathrm m}(1)=3.}
\]

### Proof

The upper bound follows from \(G=K_5\):
\[
\operatorname{cr}(K_5)=1,\qquad
\operatorname{cr}(CK_5)=\operatorname{cr}(K_6)=3.
\]

For the lower bound, every nonplanar graph contains a subdivision of either \(K_5\) or \(K_{3,3}\). Its cone therefore contains a subdivision of \(CK_5\) or \(CK_{3,3}\), using only the apex edges to the branch vertices.

We have \(\operatorname{cr}(CK_5)=3\). It remains only to show
\[
\operatorname{cr}(CK_{3,3})\ge3.
\]
Let \(a\) be the apex and let the bipartition of \(K_{3,3}\) be \(X,Y\). Inside \(CK_{3,3}\) there are seven distinguished \(K_{3,3}\)-subgraphs:

1. the original graph between \(X\) and \(Y\);
2. for each two-element \(X'\subset X\), the graph between \(X'\cup\{a\}\) and \(Y\);
3. for each two-element \(Y'\subset Y\), the graph between \(X\) and \(Y'\cup\{a\}\).

Every one of these seven subdrawings has a crossing. In a good drawing:

- a crossing between two base edges belongs to at most three of these subgraphs;
- a crossing between an apex edge and a base edge belongs to at most two;
- two apex edges do not cross.

Double-counting crossing incidences therefore gives
\[
7\le3\,\operatorname{cr}(CK_{3,3}),
\]
so \(\operatorname{cr}(CK_{3,3})\ge3\). Thus every cone over a nonplanar graph has at least three crossings. ∎

# 6. Why the construction does not immediately become simple

Replacing parallel edges by internally disjoint two-edge paths does preserve the crossing number of the base, but it badly changes the cone.

Indeed, suppose \(m\) parallel \(uv\)-edges are replaced by paths \(u z_i v\). In the cone, the vertices
\[
\{a,u,v,z_1,\dots,z_m\}
\]
contain a \(K_{3,m}\) subgraph with parts \(\{a,u,v\}\) and \(\{z_1,\dots,z_m\}\).

A self-contained quadratic lower bound follows by counting its \(\binom m3\) copies of \(K_{3,3}\). Each crossing is present in at most \(m-2\) of them, and therefore
\[
\operatorname{cr}(K_{3,m})
\ge \frac{\binom m3}{m-2}
=\frac{m(m-1)}6.
\]
Thus the naive subdivision of a parallel bundle creates \(\Omega(m^2)\) new cone complexity. This explains why Proposition 3.1 does not furnish a comparable simple-graph construction.

# 7. Gaps and status

1. No general formula for \(F_{\mathrm m}(k)\) or \(F_{\mathrm s}(k)\) is obtained.
2. The upper bound
   \[
   F_{\mathrm m}(k)\le k+2\sqrt{k}+O(k^{1/4})
   \]
   has no matching lower bound here; the leading constant is not determined.
3. The main construction uses parallel edges. The simple-graph version remains essentially untouched beyond \(k=0,1\).
4. The scaling lemma reduces improvement of the multigraph leading constant to finding a compatible finite seed with small
   \[
   \frac{\operatorname{cr}(CH)-\operatorname{cr}(H)}
        {\sqrt{\operatorname{cr}(H)}}.
   \]
   It does not prove that an optimal seed exists or identify one.
5. I have not verified whether the exact thickening calculation or the explicit leading constant \(2\) already appears implicitly in the full 2018 paper; accordingly I do not claim novelty suitable for publication.