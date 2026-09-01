```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A weak-regularity argument gives a uniform o(n^2) upper bound when t=o(n), with an explicit logarithmic rate, and the induced-P3-free case has order Theta_c(nt).",
  "would_publish": false,
  "caveats": "The logarithmic rate is very weak and non-sharp, gives no matching lower bound, and does not determine ex(Gamma,P) for an individual host."
}
```

## 1. Statement of the partial result

I use the standard convention that a \((c,t)\)-sparse graph satisfies
\[
d_\Gamma(A,B):=\frac{e_\Gamma(A,B)}{|A||B|}\le 1-c
\]
for every two disjoint vertex sets \(A,B\) of size at least \(t\). The argument remains valid if the definition quantifies over possibly intersecting sets.

Let \(H\) be a fixed bipartite graph with a bipartition \(X\cup Y\), where
\[
a=|X|,\qquad b=|Y|,\qquad s=ab,
\]
and suppose \(H\) has at least one edge. Put
\[
h=v(H),\qquad q=\binom h2-e(H).
\]

### Theorem 1
There are constants \(C_H,R_H>0\) such that the following holds. Let \(0<c\le 1\), let \(\Gamma\) be an \(n\)-vertex \((c,t)\)-sparse graph, and let \(G\subseteq\Gamma\) be induced-\(H\)-free. If \(n/t\ge R_H\), then
\[
\frac{2e(G)}{n^2}
 \le
 C_H\,c^{-q/s}
 \bigl(\log(n/t)\bigr)^{-1/(2s)}.
\tag{1}
\]

Consequently, if \(\mathcal P\) is hereditary and misses a bipartite graph, then for every fixed \(c>0\),
\[
t=o(n)
\quad\Longrightarrow\quad
\sup_{\substack{\Gamma:\,|V(\Gamma)|=n\\
\Gamma\text{ is }(c,t)\text{-sparse}}}
\frac{\operatorname{ex}(\Gamma,\mathcal P)}{n^2}
\longrightarrow 0.
\tag{2}
\]

Thus the full problem has at least the following uniform qualitative answer: no such hereditary property can retain a positive proportion of all possible edges in a \((c,t)\)-sparse host when \(c\) is fixed and \(t=o(n)\).

If the bipartite graph originally omitted by \(\mathcal P\) has no edges, replace it by its disjoint union with \(K_2\). This larger bipartite graph is also omitted, by heredity, and has an edge.

---

## 2. A weak-regularity lemma adapted to \((c,t)\)-sparsity

For an \(n\)-vertex graph \(F\), let \(W_F\) be its usual adjacency graphon and use the normalized cut norm
\[
\|U\|_\square
 =
 \sup_{S,T\subseteq[0,1]}
 \left|\int_{S\times T}U(x,y)\,dx\,dy\right|.
\]

### Lemma 2
Let \(0<\eta\le 1/2\) and \(k_0\ge1\). Define
\[
r_* = k_0\,4^{\lceil\eta^{-2}\rceil},
\qquad
K=2\eta^{-1}r_*.
\]
If \(n/t\ge K\), then every \(n\)-vertex graph \(F\) has pairwise disjoint equal-sized sets
\[
V_1,\ldots,V_k,
\]
each of size at least \(t\), with \(k_0\le k\le K\), such that the weighted graphon \(U\) defined by

- \(U=d_F(V_i,V_j)\) on \(V_i\times V_j\) for \(i\ne j\);
- \(U=0\) on \(V_i\times V_i\);
- \(U=0\) whenever at least one coordinate lies outside \(\bigcup_iV_i\),

satisfies
\[
\|W_F-U\|_\square\le 4\eta+\frac1{k_0}.
\tag{3}
\]

If \(F\) is \((c,t)\)-sparse, then in addition
\[
0\le U\le1-c
\quad\text{almost everywhere}.
\tag{4}
\]

#### Proof
Start with any partition into \(k_0\) nonempty classes. For a partition \(\mathcal Q\), let \(W_{\mathcal Q}\) be the graphon obtained by replacing each pair of classes by its edge density.

If
\[
\|W_F-W_{\mathcal Q}\|_\square>\eta,
\]
choose witnessing sets \(S,T\), and refine every class according to membership in \(S\) and \(T\). This multiplies the number of classes by at most four. By the usual orthogonal-projection calculation, the energy
\[
\|W_{\mathcal Q}\|_2^2
\]
increases by more than \(\eta^2\). Since this energy is at most one, after at most \(\lceil\eta^{-2}\rceil\) refinements one obtains a partition \(\mathcal Q\) into \(r\le r_*\) classes satisfying
\[
\|W_F-W_{\mathcal Q}\|_\square\le\eta.
\tag{5}
\]

Set
\[
m=\left\lfloor\frac{\eta n}{r}\right\rfloor.
\]
The hypothesis \(n/t\ge 2r_*/\eta\) ensures \(m\ge t\). Split every class of \(\mathcal Q\) into sets of size \(m\), putting all remainders into an exceptional set \(V_0\). Then
\[
|V_0|<rm\le\eta n.
\]
The number \(k\) of full classes satisfies
\[
k_0\le k\le\frac{2r}{\eta}\le K.
\]

Passing from \(W_{\mathcal Q}\) to the actual densities on the refined full classes increases the cut error on \(V\setminus V_0\) by at most another \(\eta\): conditional expectation is contractive in cut norm, up to the triangle inequality. Zeroing all pairs incident with \(V_0\) costs at most \(2\eta\) in \(L^1\), hence in cut norm. Thus the error before zeroing the diagonal class-pairs is at most \(4\eta\).

Finally, the total measure of the diagonal class-pairs is
\[
k\left(\frac mn\right)^2\le\frac1k\le\frac1{k_0},
\]
which proves (3). If \(F\) is \((c,t)\)-sparse, then for \(i\ne j\),
\[
d_F(V_i,V_j)\le1-c,
\]
because \(|V_i|=|V_j|\ge t\). This proves (4). ∎

---

## 3. Induced copies in a weighted graph bounded away from one

For a graphon \(W\), define
\[
t_{\mathrm{ind}}(H,W)
 =
 \int_{[0,1]^h}
 \prod_{ij\in E(H)}W(x_i,x_j)
 \prod_{ij\notin E(H)}(1-W(x_i,x_j))
 \,d\mathbf x.
\]

### Lemma 3
If \(0\le U\le1-c\) almost everywhere and
\[
r=\int_{[0,1]^2}U,
\]
then
\[
t_{\mathrm{ind}}(H,U)\ge c^q r^{ab}.
\tag{6}
\]

#### Proof
Every nonedge factor satisfies \(1-U\ge c\), so
\[
t_{\mathrm{ind}}(H,U)\ge c^q t(H,U).
\]
Since \(H\) is a subgraph of \(K_{a,b}\) and \(0\le U\le1\),
\[
t(H,U)\ge t(K_{a,b},U).
\]
Moreover,
\[
\begin{aligned}
t(K_{a,b},U)
&=
\int_{x_1,\dots,x_a}
\left(\int_y\prod_{i=1}^aU(x_i,y)\,dy\right)^b
\,d\mathbf x\\
&\ge
\left(
\int_y
\left(\int_x U(x,y)\,dx\right)^a
\,dy
\right)^b\\
&\ge
\left(\int_{[0,1]^2}U\right)^{ab}
=r^{ab},
\end{aligned}
\]
by Jensen's inequality twice. ∎

We also need the elementary cut-norm counting estimate
\[
\left|
t_{\mathrm{ind}}(H,W)-t_{\mathrm{ind}}(H,U)
\right|
\le
\binom h2\|W-U\|_\square.
\tag{7}
\]
Indeed, telescope over the \(\binom h2\) edge or nonedge factors. After fixing all variables except those belonging to the factor being changed, the remaining multiplier has the form \(f(x)g(y)\) with \(0\le f,g\le1\), and its integral against \(W-U\) is bounded by the cut norm.

Finally, if \(G\) is an \(n\)-vertex induced-\(H\)-free graph, then
\[
t_{\mathrm{ind}}(H,W_G)\le\frac{\binom h2}{n}.
\tag{8}
\]
For an injective choice of the \(h\) vertices the integrand is zero; the probability that a uniformly random ordered \(h\)-tuple has a collision is at most \(\binom h2/n\).

---

## 4. Proof of Theorem 1

Write
\[
p=\int W_G=\frac{2e(G)}{n^2},
\qquad
M=\binom h2.
\]
Suppose \(p>0\), and define
\[
L=c^q\left(\frac p2\right)^s,
\qquad
\eta=\frac{L}{32M},
\qquad
k_0=\left\lceil\frac{8M}{L}\right\rceil.
\tag{9}
\]

Apply Lemma 2, provided \(n/t\) is at least its corresponding value of \(K\). Since \(G\subseteq\Gamma\), the graph \(G\) is itself \((c,t)\)-sparse. We therefore obtain \(U\le1-c\) and
\[
\delta:=\|W_G-U\|_\square
\le4\eta+\frac1{k_0}
\le\frac{L}{4M}.
\tag{10}
\]
Because \(L\le p/2\), this also gives
\[
\int U\ge p-\delta\ge\frac p2.
\tag{11}
\]

Lemma 3 now gives
\[
t_{\mathrm{ind}}(H,U)
\ge
c^q\left(\frac p2\right)^s
=L.
\tag{12}
\]
On the other hand, (7), (8), and (10) give
\[
t_{\mathrm{ind}}(H,U)
\le
\frac Mn+M\delta
\le
\frac Mn+\frac L4.
\tag{13}
\]
Thus a contradiction follows whenever
\[
\frac Mn\le\frac L2.
\tag{14}
\]

It remains to estimate the number of classes required by Lemma 2. From (9),
\[
\eta^{-1}=O_H(c^{-q}p^{-s}),
\qquad
k_0=O_H(c^{-q}p^{-s}),
\]
and hence
\[
\log K
\le
D_H c^{-2q}p^{-2s}
\tag{15}
\]
for a constant \(D_H\).

Let \(R=n/t\). If
\[
p>
C_H c^{-q/s}(\log R)^{-1/(2s)}
\tag{16}
\]
and \(C_H^{2s}>2D_H\), then (15) implies
\[
K\le R^{1/2}\le R.
\]
Thus Lemma 2 is applicable. Moreover, (16) gives
\[
L=c^q(p/2)^s
>
(C_H/2)^s(\log R)^{-1/2}.
\]
Since \(n\ge R\), condition (14) holds for all sufficiently large \(R\), depending only on \(H\). This contradiction proves (1).

For a hereditary property \(\mathcal P\) omitting \(H\), every \(G\in\mathcal P\) is induced-\(H\)-free: otherwise heredity would imply \(H\in\mathcal P\). This proves (2).

If the definition of \(\operatorname{ex}(\Gamma,\mathcal P)\) permits non-spanning subgraphs, apply the theorem with \(m=|V(G)|\). For \(m/t\) large, the function
\[
\frac{m^2}{(\log(m/t))^{1/(2s)}}
\]
is increasing in \(m\); for bounded \(m/t\), the trivial bound \(e(G)=O_H(t^2)\) is absorbed into the \(n\)-vertex estimate after changing the constant.

---

## 5. A sharp-order special case: induced \(P_3\)

Let
\[
\mathcal C=\operatorname{Forb}_{\mathrm{ind}}(P_3).
\]
A graph is induced-\(P_3\)-free exactly when every connected component is a clique. Consequently,
\[
\operatorname{ex}(\Gamma,\mathcal C)
=
\max
\left\{
\sum_i\binom{|C_i|}{2}:
C_1,C_2,\ldots
\text{ are pairwise disjoint cliques of }\Gamma
\right\}.
\tag{17}
\]

Indeed, the components of any induced-\(P_3\)-free subgraph are cliques of \(\Gamma\), while any family of disjoint cliques of \(\Gamma\), with all edges between distinct cliques deleted, produces an induced-\(P_3\)-free subgraph.

If \(\Gamma\) is \((c,t)\)-sparse with \(c>0\), it cannot contain a clique on \(2t\) vertices: two disjoint \(t\)-subsets of such a clique would have density one. Therefore every \(C_i\) in (17) has size at most \(2t-1\), and
\[
\operatorname{ex}(\Gamma,\mathcal C)
\le
\sum_i(t-1)|C_i|
\le
(t-1)n.
\tag{18}
\]

This has the correct order. Fix \(0<c<1\) and let
\[
\ell=\lfloor(1-c)t\rfloor.
\]
Take \(\Gamma\) to be a disjoint union of cliques of order at most \(\ell\). For arbitrary vertex sets \(A,B\) of size at least \(t\), writing
\[
a_i=|A\cap C_i|,\qquad b_i=|B\cap C_i|,
\]
we have
\[
e_\Gamma(A,B)
\le
\sum_i a_ib_i
\le
\ell\min\{|A|,|B|\}.
\]
Hence
\[
d_\Gamma(A,B)\le\frac{\ell}{\max\{|A|,|B|\}}\le1-c.
\]
Thus \(\Gamma\) is \((c,t)\)-sparse even under the stronger convention allowing \(A\cap B\ne\varnothing\). Taking \(G=\Gamma\) gives, when \(\ell\mid n\),
\[
e(G)=\frac{\ell-1}{2}n
=
\left(\frac{1-c}{2}+o(1)\right)tn.
\tag{19}
\]
Therefore
\[
\sup_{\Gamma\text{ \((c,t)\)-sparse}}
\operatorname{ex}(\Gamma,\operatorname{Forb}_{\mathrm{ind}}(P_3))
=
\Theta_c(nt).
\]

Under the disjoint-set definition of \((c,t)\)-sparsity, the clique size in the construction can be increased to approximately \(2(1-c)t\).

---

## 6. What remains open

The logarithmic estimate (1) is only a compactness/weak-regularity bound. It does not approach the polynomial estimates known in more structured hosts such as dense random graphs, and it is unlikely to be close to optimal.

In particular, this argument does not:

1. determine the correct dependence on \(n,t,c\) and the omitted bipartite graph;
2. give matching lower bounds;
3. exploit any information about the individual host beyond \((c,t)\)-sparsity;
4. resolve the regime \(t=\Theta(n)\), where the estimate is vacuous;
5. produce a unified constant-factor formula of the type requested in Problem 1.1.

Thus the general problem remains open, but the theorem above establishes a uniform \(o(n^2)\) conclusion for all hereditary properties in the full \((c,t)\)-sparse setting when \(t=o(n)\).