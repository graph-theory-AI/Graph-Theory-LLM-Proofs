```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For induced-diamond-free subgraphs, I prove an exact sparse-end criterion and confine the unresolved dense-end range to 1-p of order 1/n.",
  "would_publish": false,
  "caveats": "The arbitrary-property characterization remains unresolved; the sparse argument uses the established random triangle Turán theorem, and novelty has not been checked."
}
```

## 1. Formulation and scope

For a hereditary family \(\mathcal P\), write
\[
\operatorname{ex}_{\mathcal P}(G)
=\max\{e(H):H\subseteq G,\ H\in\mathcal P\}.
\]
The subgraph \(H\) need not be induced or spanning. Put
\[
N=\binom n2,\qquad
k=k(\mathcal P)=\min\{\chi(F):F\notin\mathcal P\},
\qquad
\pi_k=1-\frac1{k-1}.
\]
For \(0<p=p(n)<1\), the assertion under investigation is
\[
\frac{\operatorname{ex}_{\mathcal P}(G(n,p))}{pN}
\xrightarrow{\mathbb P}\pi_k.
\tag{1}
\]

I treat the question property by property, rather than asking only for a range that works simultaneously for every fixed property.

The main result below concerns the genuinely non-monotone hereditary family of graphs with no induced diamond. It gives a sharp sparse-end characterization and bounds the dense-end transition within constant factors. I also give a general endpoint criterion when \(n(1-p)\to0\).

The safe-edge idea from the supplied attempt is rederived below in the triangle case. None of its other classification claims is needed.

---

## 2. Main partial result: induced-diamond-free subgraphs

Let
\[
D=K_4-e,\qquad
\mathcal D=\{H:H\text{ contains no induced }D\}.
\]
Since \(\chi(D)=3\), we have \(k(\mathcal D)=3\), so the predicted coefficient is \(1/2\).

### Theorem 2.1

Let \(q=1-p\).

1. A necessary condition for
   \[
   \frac{\operatorname{ex}_{\mathcal D}(G(n,p))}{pN}
   \xrightarrow{\mathbb P}\frac12
   \tag{2}
   \]
   is
   \[
   p\sqrt n\longrightarrow\infty.
   \tag{3}
   \]

2. If \(nq\to\infty\), condition (3) is also sufficient. Thus, throughout this regime, (2) holds **if and only if** \(p\sqrt n\to\infty\).

3. More generally, (2) holds if
   \[
   p\sqrt n\longrightarrow\infty
   \quad\text{and}\quad
   \liminf_{n\to\infty}nq\ge 8\log 2.
   \tag{4}
   \]

4. Along any subsequence on which \(nq\le1\), with high probability
   \[
   \operatorname{ex}_{\mathcal D}(G(n,p))
   \ge
   \left(\frac12+\frac1{2e^2}-o(1)\right)pN.
   \tag{5}
   \]
   Consequently, (2) fails on such a subsequence.

In particular, for this property the unresolved dense-end behavior is confined to the constant-scale window
\[
1-p=\Theta(1/n).
\]
For example, the theorem holds at \(p=1-6/n\), but fails at \(p=1-1/n\).

The diamond statements also hold if spanning subgraphs are required: adding isolated vertices does not create an induced diamond.

---

## 3. Local structure of induced-diamond-free graphs

Two elementary observations drive the proof.

### Lemma 3.1

If \(H\) is induced-diamond-free, then:

1. the common neighborhood of the endpoints of every edge is a clique;
2. if \(C\) is a maximal clique, every vertex outside \(C\) has at most one neighbor in \(C\).

#### Proof

For the first assertion, if \(uv\) is an edge and two common neighbors \(x,y\) are nonadjacent, then \(H[\{u,v,x,y\}]\) is an induced diamond.

For the second, suppose \(v\notin C\) has two neighbors \(a,b\in C\). Maximality supplies a nonneighbor \(c\in C\). Then \(\{v,a,b,c\}\) induces a diamond. \(\square\)

Let \(T(H)\) denote the number of triangles in \(H\). The first assertion immediately gives
\[
3T(H)
=\sum_{uv\in E(H)}|N_H(u)\cap N_H(v)|
\le (\omega(H)-2)e(H).
\tag{6}
\]

Thus an induced-diamond-free graph with small clique number has few triangles relative to its number of edges.

---

## 4. The sharp sparse-end result

### 4.1 An established input

I use the sparse random Turán theorem only in its triangle case:

> For every \(\eta>0\), there is \(C=C(\eta)>0\) such that, for
> \[
> r=Cn^{-1/2},
> \]
> with high probability every triangle-free subgraph of \(G(n,r)\) has at most
> \[
> \left(\frac12+\eta\right)rN
> \]
> edges.

This is an established theorem, not an additional conjectural assumption. The transfer argument needed here is included next.

### Lemma 4.1: transfer from triangle-free subgraphs

Suppose
\[
p\sqrt n\to\infty
\quad\text{and}\quad
\omega(G(n,p))=o_{\mathbb P}(np^2).
\tag{7}
\]
Then
\[
\operatorname{ex}_{\mathcal D}(G(n,p))
=\left(\frac12+o_{\mathbb P}(1)\right)pN.
\tag{8}
\]

#### Proof

The lower bound is deterministic up to concentration: every graph has a bipartite subgraph containing at least half its edges, and every bipartite graph belongs to \(\mathcal D\).

For the upper bound, fix \(\varepsilon>0\). Apply the random triangle Turán theorem with error \(\varepsilon/4\), obtaining \(C\). Set
\[
r=Cn^{-1/2},
\qquad
\theta=\frac rp.
\]
For all sufficiently large \(n\), \(\theta\le1\).

Independently retain every edge of \(G=G(n,p)\) with probability \(\theta\). The resulting graph \(G'\) has distribution \(G(n,r)\).

We show that, with probability \(o(1)\), \(G\) contains an induced-diamond-free \(H\) with
\[
e(H)\ge\left(\frac12+\varepsilon\right)pN.
\tag{9}
\]
If such an \(H\) exists, choose one by a fixed tie-breaking rule.

By (7), there is a deterministic \(b_n=o(np^2)\) such that
\[
\omega(G)\le b_n
\]
with high probability. Also \(e(G)\le2pN\) with high probability. On these events, let \(H'=H\cap G'\). Conditional on \(G,H\),
\[
\mathbb E e(H')=\theta e(H)
\ge\left(\frac12+\varepsilon\right)rN.
\]
Standard binomial concentration, uniformly over the possible chosen \(H\), gives
\[
e(H')\ge\left(\frac12+\frac{3\varepsilon}{4}\right)rN
\tag{10}
\]
with conditional probability \(1-o(1)\).

On the other hand, (6) gives
\[
\begin{aligned}
\mathbb E[T(H')\mid G,H]
&=\theta^3T(H)\\
&\le \frac{\theta^3b_ne(H)}3\\
&\le \frac23\,\theta^2b_n\,rN
=o(rN),
\end{aligned}
\tag{11}
\]
because
\[
\theta^2b_n=\frac{C^2b_n}{np^2}=o(1).
\]
By Markov's inequality, with conditional probability \(1-o(1)\), deleting one edge from each triangle of \(H'\) removes at most \(\varepsilon rN/4\) edges. Together with (10), this produces a triangle-free subgraph of \(G'\) with at least
\[
\left(\frac12+\frac{\varepsilon}{2}\right)rN
\]
edges.

If the event (9) had probability bounded away from zero, the construction would contradict the random triangle Turán theorem for \(G'\sim G(n,r)\). Hence its probability is \(o(1)\). \(\square\)

### Lemma 4.2

If
\[
p\sqrt n\to\infty
\quad\text{and}\quad
n(1-p)\to\infty,
\]
then
\[
\omega(G(n,p))=o_{\mathbb P}(np^2).
\tag{12}
\]

#### Proof

Split into three ranges.

* If \(p\le n^{-1/3}\), then
  \[
  \mathbb E[\#K_8]\le n^8p^{28}\le n^{-4/3}.
  \]
  Thus \(\omega(G)\le7\) with high probability, while \(np^2\to\infty\).

* If \(n^{-1/3}<p\le1/2\), a first-moment bound gives
  \[
  \omega(G)=O(\log n)
  \]
  with high probability, whereas \(np^2>n^{1/3}\).

* If \(p>1/2\), then \(np^2\ge n/4\). For every fixed \(a>0\),
  \[
  \mathbb E[\#K_{\lceil an\rceil}]
  \le
  2^n\exp\!\left(-q\binom{\lceil an\rceil}{2}\right)
  =o(1),
  \]
  since \(nq\to\infty\). Thus \(\omega(G)=o_{\mathbb P}(n)\).

These cover all possibilities. \(\square\)

Lemmas 4.1 and 4.2 prove sufficiency in Theorem 2.1(2).

### 4.2 Necessity of \(p\sqrt n\to\infty\)

Suppose (3) fails. Pass to a subsequence on which
\[
p\sqrt n\le C.
\tag{13}
\]
Write \(\mu=pN\).

Call a present edge **safe** if it lies in no triangle of \(G\), and let \(S\) count safe edges. Conditional on \(xy\in E(G)\), the events that a third vertex completes a triangle with \(xy\) are independent. Hence
\[
\mathbb ES
=\mu(1-p^2)^{n-2}
\ge\delta\mu
\tag{14}
\]
for a constant \(\delta=\delta(C)>0\).

Suppose first that \(\mu\to\infty\). Since \(S\le e(G)\),
\[
\mathbb ES^2\le\mathbb Ee(G)^2\le\mu^2+\mu.
\]
Paley–Zygmund therefore gives
\[
\mathbb P\left(S\ge\frac{\delta\mu}{2}\right)
\ge
\frac{\delta^2}{4(1+1/\mu)}.
\tag{15}
\]

Now randomly two-colour the vertices, keeping every cross-colour edge and every safe edge. The resulting graph is triangle-free: a triangle would have a monochromatic edge, which would have to be safe, a contradiction. Averaging over the colourings gives a triangle-free subgraph with at least
\[
\frac{e(G)}2+\frac S2
\tag{16}
\]
edges.

Since \(e(G)/\mu\to1\), equations (15)–(16) show that, with probability bounded away from zero,
\[
\operatorname{ex}_{\mathcal D}(G)
\ge\left(\frac12+\frac{\delta}{8}\right)\mu.
\]
Thus (2) fails.

If \(\mu\) is bounded along a further subsequence, the probability that \(G\) has no edges is bounded away from zero. On that event the normalized extremal number is zero, again ruling out convergence to \(1/2\). Passing to a further subsequence covers the remaining possibilities for \(\mu\).

This proves Theorem 2.1(1), and hence the claimed equivalence in part (2).

---

## 5. A dense-end upper bound at \(q=\Theta(1/n)\)

The preceding transfer argument requires \(\omega(G)=o(n)\) when \(p\to1\). The following deterministic estimate allows linear cliques and consequently reaches \(q=C/n\).

### Lemma 5.1

Every induced-diamond-free graph \(H\) on \(n\) vertices satisfies
\[
e(H)\le
\frac{n^2}{4}
+\frac n2\left(\omega(H)-\frac n2\right)_+
+2n^{3/2},
\tag{17}
\]
where \(x_+=\max\{x,0\}\).

#### Proof

Let \(L=\lceil\sqrt n\rceil\). Repeatedly remove a maximal clique of size at least \(L\), until the remaining graph \(R\) has clique number less than \(L\). Let the removed clique sizes be \(t_1,\dots,t_j\), and put
\[
u=v(R),\qquad S=\sum_i t_i=n-u.
\]

By Lemma 3.1, each removed clique sends at most one edge to each vertex remaining at that step. Since \(j\le n/L\), all these cross-edges together number at most \(n^2/L\).

Write \(m=e(R)\). By Lemma 3.1,
\[
3T(R)\le Lm.
\]
Conversely,
\[
\begin{aligned}
3T(R)
&=\sum_{xy\in E(R)}|N_R(x)\cap N_R(y)|\\
&\ge \sum_{xy\in E(R)}(d_R(x)+d_R(y)-u)\\
&=\sum_{x\in V(R)}d_R(x)^2-um\\
&\ge \frac{4m^2}{u}-um.
\end{aligned}
\]
Interpreting the empty cases separately, this yields
\[
m\le\frac{u^2}{4}+\frac{uL}{4}.
\]

Consequently,
\[
e(H)\le
\frac12\sum_i t_i^2+\frac{u^2}{4}
+\frac{nL}{4}+\frac{n^2}{L}.
\tag{18}
\]
Let
\[
b=\left(\omega(H)-\frac n2\right)_+.
\]
Since every \(t_i\le n/2+b\),
\[
\begin{aligned}
\frac12\sum_i t_i^2+\frac{u^2}{4}
&\le \frac{(n/2+b)S}{2}+\frac{u^2}{4}\\
&=\frac{n^2}{4}-\frac{uS}{4}+\frac{bS}{2}\\
&\le\frac{n^2}{4}+\frac{bn}{2}.
\end{aligned}
\]
The last two terms in (18) are at most \(2n^{3/2}\). \(\square\)

### Dense-end consequence

Suppose \(p\to1\) and
\[
\liminf nq\ge8\log2.
\tag{19}
\]
For every fixed \(a>1/2\),
\[
\mathbb E[\#K_{\lceil an\rceil}]
\le
2^n\exp\!\left(-q\binom{\lceil an\rceil}{2}\right)
=o(1),
\]
because
\[
\log2-\frac{(8\log2)a^2}{2}<0.
\]
Thus
\[
\left(\omega(G)-\frac n2\right)_+=o_{\mathbb P}(n).
\]
Applying Lemma 5.1 to every induced-diamond-free subgraph of \(G\),
\[
\operatorname{ex}_{\mathcal D}(G)
\le\frac{n^2}{4}+o_{\mathbb P}(n^2)
=\left(\frac12+o_{\mathbb P}(1)\right)pN.
\]
The bipartite-subgraph lower bound matches this.

To obtain Theorem 2.1(3) for arbitrary sequences satisfying (4), split the indices into
\[
nq\le\log n
\quad\text{and}\quad
nq>\log n.
\]
On the first part, \(p\to1\) and the dense argument applies. On the second, \(nq\to\infty\), so Section 4 applies.

---

## 6. Failure throughout \(q\le1/n\)

Assume \(q\le1/n\), and let
\[
Q=\overline{G}\sim G(n,q).
\]

Let \(Z\) be the number of simple cycles in \(Q\). Then
\[
\mathbb EZ
=
\sum_{\ell=3}^{n}\frac{(n)_\ell q^\ell}{2\ell}
\le
\frac12\sum_{\ell=3}^{n}\frac1\ell
=O(\log n).
\]
With high probability, deleting \(o(n)\) vertices makes \(Q\) a forest: choose one vertex from each cycle.

Let \(I\) be the number of isolated vertices of \(Q\). We have
\[
\mathbb EI=n(1-q)^{n-1}\ge(e^{-1}-o(1))n.
\]
Also \(\operatorname{Var}(I)=O(n)\). Indeed, for distinct \(x,y\),
\[
\mathbb P(x,y\text{ both isolated})=(1-q)^{2n-3},
\]
so their covariance is \(O(q)=O(1/n)\). Hence
\[
I\ge(e^{-1}-o(1))n
\tag{20}
\]
with high probability.

The deleted cycle vertices do not include isolated vertices. Two-colour each remaining tree, orienting its bipartition so that the larger class is placed in \(A\). Put all isolated vertices in \(A\). If \(B\) is the other class, then
\[
|A|+|B|=n-o(n),
\qquad
|A|-|B|\ge I.
\tag{21}
\]
Both \(A\) and \(B\) are independent in \(Q\), hence cliques in \(G\).

Keep the two cliques \(G[A]\) and \(G[B]\), and no edges between them. This is induced-diamond-free. Its edge count is
\[
\begin{aligned}
\binom{|A|}{2}+\binom{|B|}{2}
&=
\frac{(|A|+|B|)^2+(|A|-|B|)^2}{4}
-\frac{|A|+|B|}{2}\\
&\ge
\left(\frac14+\frac1{4e^2}-o(1)\right)n^2.
\end{aligned}
\]
Since \(pN=(1-o(1))n^2/2\), this proves (5).

More precisely, if \(nq\to c\in[0,1]\), the same argument gives
\[
\operatorname{ex}_{\mathcal D}(G(n,p))
\ge
\left(\frac{1+e^{-2c}}2-o(1)\right)pN.
\tag{22}
\]

---

## 7. A general characterization at the ultra-dense endpoint

There is also a useful property-specific result for arbitrary hereditary families.

Let \(\mathcal M(\mathcal P)\) be the ordinary subgraph closure of \(\mathcal P\):
\[
\mathcal M(\mathcal P)
=\{H:H\subseteq J\text{ for some }J\in\mathcal P\}.
\]
This is a monotone family. Define
\[
\ell=\min\{\chi(F):F\notin\mathcal M(\mathcal P)\},
\]
with \(\ell=\infty\) if \(\mathcal M(\mathcal P)\) is the family of all graphs, and set \(\pi_\infty=1\). Necessarily \(\ell\ge k\).

### Proposition 7.1

Assume \(2\le k<\infty\).

1. If \(n(1-p)\to0\), then
   \[
   \frac{\operatorname{ex}_{\mathcal P}(G(n,p))}{pN}
   \xrightarrow{\mathbb P}\pi_\ell.
   \tag{23}
   \]

2. If \(\ell=k\), the desired conclusion (1) holds for **every** sequence \(p\to1\), without any restriction on \(1-p\).

Thus, in the ultra-dense regime \(n(1-p)\to0\), the assertion of Theorem 1.1 holds exactly when
\[
k\bigl(\mathcal M(\mathcal P)\bigr)=k(\mathcal P).
\tag{24}
\]

#### Proof

First,
\[
\operatorname{ex}_{\mathcal M(\mathcal P)}(K_n)
=
\operatorname{ex}_{\mathcal P}(K_n).
\tag{25}
\]
Indeed, if \(H\in\mathcal M(\mathcal P)\), heredity allows us to take a graph \(J\in\mathcal P\) on exactly \(V(H)\) with \(H\subseteq J\).

The classical Erdős–Stone theorem gives
\[
\operatorname{ex}_{\mathcal P}(K_n)
=(\pi_\ell+o(1))N.
\tag{26}
\]
For finite \(\ell\), the lower bound follows because \(\mathcal M(\mathcal P)\) contains every \((\ell-1)\)-colourable graph; the upper bound follows by choosing an excluded \(\ell\)-chromatic graph and applying Erdős–Stone. If \(\ell=\infty\), (25) gives the assertion directly.

Now suppose \(nq\to0\). The complement \(Q\) has
\[
e(Q)=o_{\mathbb P}(n).
\]
Deleting one endpoint of each complement edge leaves a clique of order \(n-o_{\mathbb P}(n)\) in \(G\). Consequently, (26) sandwiches the random extremal number between
\[
\operatorname{ex}_{\mathcal P}(K_{n-o_{\mathbb P}(n)})
\quad\text{and}\quad
\operatorname{ex}_{\mathcal P}(K_n),
\]
proving (23).

Finally, if \(\ell=k\) and merely \(p\to1\), (26) supplies the upper bound. For the lower bound, every \((k-1)\)-colourable graph belongs to \(\mathcal P\), and a random \((k-1)\)-colouring retains an expected \(\pi_k e(G)\) edges. Therefore
\[
\operatorname{ex}_{\mathcal P}(G)\ge\pi_k e(G),
\]
which gives the matching asymptotic lower bound. \(\square\)

### Consequences

* Every monotone family has \(\mathcal M(\mathcal P)=\mathcal P\), so there is no dense-end restriction for such a family.
* If \(\mathcal P\) is the family excluding one induced **noncomplete** graph \(F\), then \(\mathcal P\) contains every clique. Hence \(\ell=\infty\), and
  \[
  \operatorname{ex}_{\mathcal P}(G(n,p))
  =(1+o_{\mathbb P}(1))pN
  \qquad\text{when }n(1-p)\to0.
  \]
  This conclusion does not require \(G\) itself to avoid induced \(F\). One can discard the few vertices needed to obtain a nearly spanning clique.

---

## 8. What remains unresolved

These arguments do **not** characterize the admissible sequences for an arbitrary prescribed hereditary family.

They do establish the following sharper special-case picture:

* For induced-diamond-free subgraphs, whenever \(n(1-p)\to\infty\), the exact condition is
  \[
  p\sqrt n\to\infty.
  \]
* At the dense endpoint, \(n(1-p)\le1\) forces failure, whereas asymptotic values at least \(8\log2\) suffice.
* For arbitrary hereditary families, the ultra-dense endpoint is governed exactly by the chromatic parameter of the ordinary subgraph closure.

Even for induced diamonds, these methods do not decide all sequences with
\[
1<n(1-p)<8\log2.
\]
In that window, linear cliques and collections of disjoint cliques can compete with the bipartite construction. The bounds above do not identify precisely when that competition increases the optimum above \(pN/2\).

I have not checked whether these special-case refinements already appear in the literature, so I make no novelty claim.