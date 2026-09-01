```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not resolved, but the conjectured upper bound is proved with an explicit remainder, the disjoint-union-of-cliques case is determined, and the full conjecture is shown to imply asymptotic Harary–Hill.",
  "would_publish": false,
  "caveats": "No matching lower bound is obtained for arbitrary large-order simple graphs; the main upper-bound idea may already be implicit in the source."
}
```

# Mathematical writeup

## 1. Statement and notation

I use the definition suggested by the abstract:
\[
f_s(k)=\min\bigl\{\operatorname{cr}(CG):
  G\text{ simple and }\operatorname{cr}(G)\ge k\bigr\},
\]
where \(CG\) is obtained from \(G\) by adding a new vertex adjacent to every vertex of \(G\).

The conjecture is
\[
f_s(k)=k+\sqrt2\,k^{3/4}+o(k^{3/4}).
\]

Write
\[
a_n=\operatorname{cr}(K_n),\qquad d_n=a_{n+1}-a_n.
\]

The main partial results below are:

1. Unconditionally,
   \[
   f_s(k)\le k+\sqrt2\,k^{3/4}+O(k^{9/16}).
   \]
2. If
   \[
   \alpha=\lim_{n\to\infty}\frac{\operatorname{cr}(K_n)}{n^4},
   \]
   then for graphs that are disjoint unions of complete graphs, the corresponding minimum is
   \[
   k+4\alpha^{1/4}k^{3/4}+o(k^{3/4}).
   \]
3. Consequently, the full conjecture implies
   \[
   \operatorname{cr}(K_n)=\frac{n^4}{64}+o(n^4),
   \]
   the asymptotic Harary–Hill assertion.
4. For every simple \(n\)-vertex graph \(G\),
   \[
   \operatorname{cr}(CG)-\operatorname{cr}(G)
   \ge \frac{4\,\operatorname{cr}(G)}{n}.
   \]
   This proves the conjectured lower term for graphs whose order is asymptotically the minimum allowed by the standard complete-graph drawing bound, but not for arbitrary graphs.

---

## 2. The complete-graph crossing sequence

### 2.1. Basic bounds

The standard Hill drawing gives
\[
a_n\le Z(n):=
\frac14
\left\lfloor\frac n2\right\rfloor
\left\lfloor\frac {n-1}2\right\rfloor
\left\lfloor\frac {n-2}2\right\rfloor
\left\lfloor\frac {n-3}2\right\rfloor
=\frac{n^4}{64}+O(n^3).
\tag{2.1}
\]

There is also an elementary quartic lower bound. In any good drawing of \(K_n\), every set of five vertices induces a drawing of \(K_5\), hence contains a crossing. Each crossing has four endpoints and is counted in exactly \(n-4\) five-vertex subsets. Therefore
\[
(n-4)a_n\ge \binom n5,
\]
and hence
\[
a_n\ge \frac15\binom n4
=\frac{n^4}{120}+O(n^3).
\tag{2.2}
\]
Thus \(a_n=\Theta(n^4)\).

### 2.2. Vertex deletion

Take an optimal good drawing of \(K_{n+1}\). Each crossing survives deletion of exactly \(n-3\) of the \(n+1\) vertices. Every vertex-deleted drawing is a drawing of \(K_n\), so
\[
(n+1)a_n\le (n-3)a_{n+1}.
\]
Consequently,
\[
a_{n+1}\ge \frac{n+1}{n-3}a_n,
\qquad
d_n\ge \frac{4a_n}{n-3}.
\tag{2.3}
\]

Equivalently,
\[
\rho_n:=\frac{a_n}{\binom n4}
\]
is nondecreasing. By (2.1), \(\rho_n\le 3/8+o(1)\). Therefore \(\rho_n\) has a limit, and so does
\[
\alpha:=\lim_{n\to\infty}\frac{a_n}{n^4}.
\tag{2.4}
\]
The elementary bounds above give
\[
\frac1{120}\le \alpha\le \frac1{64}.
\tag{2.5}
\]

### 2.3. Duplicating a vertex

We need a matching upper estimate for \(d_n\).

Take an optimal good drawing \(D\) of \(K_n\). For \(v\in V(K_n)\), let \(\lambda(v)\) be the number of crossings in which one of the two crossing edges is incident with \(v\). Every crossing has four distinct endpoints, so
\[
\sum_v\lambda(v)=4a_n.
\]
Choose \(v\) with
\[
\lambda(v)\le \frac{4a_n}{n}.
\]

Place a new vertex \(v'\) close to \(v\). For every \(w\ne v\), draw \(v'w\) parallel to \(vw\) outside a small disk around \(v\). This reproduces once every crossing counted by \(\lambda(v)\). Inside the small disk, the \(O(n)\) new initial arcs and the edge \(vv'\) can be connected with \(O(n^2)\) additional crossings. Hence
\[
a_{n+1}\le a_n+\frac{4a_n}{n}+O(n^2),
\]
or
\[
d_n\le \frac{4a_n}{n}+O(n^2).
\tag{2.6}
\]

Combining (2.1), (2.2), and (2.6), one gets the useful quantitative form
\[
d_n\le \sqrt2\,a_n^{3/4}+O(a_n^{1/2}).
\tag{2.7}
\]
Indeed, (2.1) implies
\[
\frac{a_n^{1/4}}n\le \frac1{2\sqrt2}+O(n^{-1}),
\]
while (2.2) gives \(n^2=O(a_n^{1/2})\).

Finally, (2.3), (2.4), and (2.6) squeeze the increments:
\[
d_n=4\alpha n^3+o(n^3)
   =\bigl(4\alpha^{1/4}+o(1)\bigr)a_n^{3/4}.
\tag{2.8}
\]

---

## 3. The conjectured upper bound

Crossing number is additive over disjoint unions. It is also additive over one-vertex unions: the lower bound follows by restricting a drawing to each summand, and the upper bound follows by drawing the summands in disjoint sectors around the common vertex.

Thus, if
\[
G=\dot\bigcup_i K_{n_i},
\]
then
\[
\operatorname{cr}(G)=\sum_i a_{n_i}
\]
and, because \(CG\) is the one-vertex union of the graphs \(K_{n_i+1}\),
\[
\operatorname{cr}(CG)=\sum_i a_{n_i+1}.
\]
Therefore
\[
\operatorname{cr}(CG)-\operatorname{cr}(G)=\sum_i d_{n_i}.
\tag{3.1}
\]

Since \(a_5=1\), every positive integer can be represented as a sum of numbers \(a_n\). Use the following greedy representation. Given a residual \(R\), choose the largest \(n\ge5\) such that \(a_n\le R\), and replace \(R\) by \(R-a_n\). Since \(R<a_{n+1}\),
\[
0\le R-a_n<d_n.
\tag{3.2}
\]

From (2.7), \(d_n=O(a_n^{3/4})\). A standard strong induction using (3.2) shows that the total increment cost of the greedy representation of \(R\) is \(O(R^{3/4})\).

Now apply this to \(R=k\), and let \(N\) be the first selected index. The first residual \(S=k-a_N\) satisfies
\[
S<d_N=O(k^{3/4}).
\]
The cost of representing the residual is therefore
\[
O(S^{3/4})=O(k^{9/16}).
\]
The first component costs, by (2.7),
\[
d_N\le \sqrt2\,a_N^{3/4}+O(a_N^{1/2})
\le \sqrt2\,k^{3/4}+O(k^{1/2}).
\]
Using the corresponding disjoint union of complete graphs in (3.1) gives

\[
\boxed{
f_s(k)\le k+\sqrt2\,k^{3/4}+O(k^{9/16}).
}
\tag{3.3}
\]

This establishes the upper half of the conjectured asymptotic, with an explicit lower-order error.

---

## 4. Exact asymptotics within the clique-union class

Define
\[
F_{\mathrm{cl}}(k)=
\min\left\{
\operatorname{cr}(CG):
G\text{ is a disjoint union of complete graphs and }
\operatorname{cr}(G)\ge k
\right\}.
\]

Set
\[
\beta=4\alpha^{1/4}.
\tag{4.1}
\]

### Theorem

\[
\boxed{
F_{\mathrm{cl}}(k)
=
k+\beta k^{3/4}+o(k^{3/4}).
}
\tag{4.2}
\]

### Upper bound

By (2.8),
\[
d_n=(\beta+o(1))a_n^{3/4}.
\]
Apply the same greedy representation as above. For the first selected \(a_N\),
\[
k-a_N=O(k^{3/4}),
\]
so \(a_N=k-o(k)\), and therefore
\[
d_N=(\beta+o(1))k^{3/4}.
\]
The residual contributes only \(O(k^{9/16})\). Hence
\[
F_{\mathrm{cl}}(k)\le k+\beta k^{3/4}+o(k^{3/4}).
\]

### Lower bound

Consider any collection of clique components, and write
\[
Q=\sum_i a_{n_i}\ge k,\qquad E=\sum_i d_{n_i}.
\]
Its cone has crossing number \(Q+E\).

Fix \(\varepsilon>0\). For all sufficiently large \(n\),
\[
d_n\ge(\beta-\varepsilon)a_n^{3/4}.
\tag{4.3}
\]
For the finitely many remaining \(n\ge5\), there is an \(\eta>0\) such that
\[
d_n\ge\eta a_n.
\tag{4.4}
\]

If \(Q-k\ge(\beta-2\varepsilon)k^{3/4}\), the overshoot alone gives the desired lower bound. Otherwise \(Q=k+O(k^{3/4})\).

Let \(S\) be the total \(a_{n_i}\)-weight of the bounded-size components. If \(S\ge k^{7/8}\), then (4.4) gives
\[
E\ge\eta k^{7/8}\gg k^{3/4}.
\]
Otherwise the large components have total weight \(k-o(k)\). Since \(x\mapsto x^{3/4}\) is subadditive,
\[
\sum_{\text{large }i}a_{n_i}^{3/4}
\ge
\left(\sum_{\text{large }i}a_{n_i}\right)^{3/4}.
\]
Using (4.3),
\[
E\ge(\beta-\varepsilon)(k-o(k))^{3/4}
=(\beta-\varepsilon+o(1))k^{3/4}.
\]
Letting \(\varepsilon\to0\) proves the lower bound in (4.2).

Because \(\alpha\le1/64\),
\[
\beta=4\alpha^{1/4}\le\sqrt2.
\tag{4.5}
\]
Thus, unconditionally,
\[
f_s(k)\le F_{\mathrm{cl}}(k)
=k+4\alpha^{1/4}k^{3/4}+o(k^{3/4})
\le k+\sqrt2\,k^{3/4}+o(k^{3/4}).
\]

---

## 5. The conjecture forces asymptotic Harary–Hill

The preceding theorem already shows this. If the proposed formula for \(f_s\) were true, then
\[
f_s(k)\le F_{\mathrm{cl}}(k)
\]
would imply
\[
\sqrt2\le 4\alpha^{1/4}.
\]
Together with \(\alpha\le1/64\), this forces
\[
\alpha=\frac1{64}.
\tag{5.1}
\]
Equivalently,
\[
\operatorname{cr}(K_n)=\frac{n^4}{64}+o(n^4)
=Z(n)(1+o(1)).
\tag{5.2}
\]

There is also a direct proof of the implication. Since \(CK_n=K_{n+1}\),
\[
f_s(a_n)\le a_{n+1}.
\]
The conjectured lower asymptotic would give
\[
a_{n+1}-a_n
\ge(\sqrt2-o(1))a_n^{3/4}.
\]
Putting \(b_n=a_n^{1/4}\),
\[
b_{n+1}
\ge
\left(b_n^4+(\sqrt2-o(1))b_n^3\right)^{1/4}
=
b_n+\frac{\sqrt2}{4}-o(1).
\]
Summation yields
\[
b_n\ge\left(\frac{\sqrt2}{4}-o(1)\right)n,
\]
and hence
\[
a_n\ge \left(\frac{\sqrt2}{4}\right)^4n^4-o(n^4)
=\frac{n^4}{64}-o(n^4).
\]
Together with the Hill drawing upper bound, this proves (5.2).

Thus the proposed constant \(\sqrt2\) is not merely suggested by complete graphs: proving the lower bound with this constant would settle the asymptotic complete-graph crossing-number problem. Conversely, if the actual constant \(\alpha\) were strictly less than \(1/64\), then the clique-union construction above would disprove the present conjecture with the smaller coefficient \(4\alpha^{1/4}\).

This is only a necessary condition: even proving \(\alpha=1/64\) would not exclude non-clique graphs with cheaper cones.

---

## 6. A general lower bound depending on the order

The following structural estimate is unconditional.

### Lemma

If \(G\) is a simple graph on \(n\) vertices and \(q=\operatorname{cr}(G)\), then
\[
\boxed{
\operatorname{cr}(CG)-q\ge \frac{4q}{n}.
}
\tag{6.1}
\]

### Proof

Take an optimal good drawing \(D\) of \(CG\), with cone vertex \(v\). Let

- \(X\) be the number of crossings between two edges of \(G\);
- \(Y\) be the number of crossings between a cone edge and an edge of \(G\).

Cone edges may be assumed not to cross one another. Put
\[
r=X-q\ge0,\qquad
\delta=\operatorname{cr}(CG)-q=r+Y.
\]

For \(x\in V(G)\), let \(y_x\) be the number of crossings on the cone edge \(vx\). For \(u\in V(G)\), let \(c(u)\) be the number of base-base crossings in which an edge incident with \(u\) participates. Since each base crossing has four distinct endpoints,
\[
\sum_{u\in V(G)}c(u)=4X.
\tag{6.2}
\]

Redraw \(G\) by deleting \(u\) and its incident base edges, placing \(u\) at the cone vertex \(v\), and drawing each edge \(ux\), for \(x\in N_G(u)\), along the former cone edge \(vx\). After small perturbations, this drawing has at most
\[
X-c(u)+\sum_{x\in N_G(u)}y_x
\]
crossings. Since every drawing of \(G\) has at least \(q\) crossings,
\[
c(u)\le r+\sum_{x\in N_G(u)}y_x.
\tag{6.3}
\]
Summing (6.3) over \(u\) and using simplicity,
\[
4X
\le nr+\sum_x d_G(x)y_x
\le nr+(n-1)Y
\le n(r+Y)
=n\delta.
\]
As \(X\ge q\), this proves (6.1). ∎

In particular, if a sequence of graphs satisfies
\[
n=(2\sqrt2+o(1))q^{1/4},
\]
then
\[
\operatorname{cr}(CG)-q
\ge(\sqrt2-o(1))q^{3/4}.
\tag{6.4}
\]
The standard complete-graph drawing bound implies that every \(n\)-vertex simple graph with crossing number \(q\) satisfies
\[
n\ge(2\sqrt2-o(1))q^{1/4}.
\]
Thus (6.4) covers graphs that are asymptotically as crossing-dense, per vertex, as the Hill upper bound permits.

The unresolved regime is precisely when a possible minimizing witness has
\[
n\gg q^{1/4}.
\]
The estimate (6.1) then becomes too weak. Large subdivisions and large crossing-critical structures show that order cannot simply be bounded in terms of \(q\) without using additional information about how the cone edges interact with the drawing.

---

## 7. Conclusion and remaining gap

The conjectured upper term is valid:
\[
f_s(k)\le k+\sqrt2\,k^{3/4}+O(k^{9/16}).
\]

Within the class of disjoint unions of complete graphs, the exact coefficient is
\[
4\alpha^{1/4},
\qquad
\alpha=\lim_{n\to\infty}\frac{\operatorname{cr}(K_n)}{n^4}.
\]
It equals \(\sqrt2\) exactly when the asymptotic Harary–Hill assertion holds.

What remains unproved is a universal lower bound
\[
f_s(k)\ge k+(\sqrt2-o(1))k^{3/4}.
\]
The order-dependent lemma proves this only for asymptotically maximally crossing-dense witnesses. It gives no adequate control over large-order simple graphs. No counterexample is produced, and no argument here excludes such graphs from having cone excess below the conjectured value.