```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for forests, complete bipartite graphs, a two-terminal doubled-tree family, and in particular every admissible oriented graph with at most six arcs.",
  "would_publish": false,
  "caveats": "The general asymmetric Sidorenko inequality remains open, and no novelty is claimed for these special classes."
}
```

# Partial results

## 1. Matrix formulation

Let \(B\to\vec K_2\), and write its corresponding bipartition as
\[
V(B)=X\sqcup Y,
\]
with every arc directed from \(X\) to \(Y\). Let \(m=e(B)\) and \(v=v(B)\).

For an oriented host \(G\) on \(n\) vertices, let \(A\) be its adjacency matrix and put
\[
M=\sum_{i,j}A_{ij},\qquad p=\frac{M}{n^2}=t(\vec K_2,G).
\]
Write
\[
Z_B(A)=
\sum_{\phi:V(B)\to[n]}
\prod_{xy\in E(B)}A_{\phi(x),\phi(y)}.
\]
Then the directed Sidorenko inequality is
\[
Z_B(A)\ge n^v p^m=M^m n^{v-2m}. \tag{1}
\]

All arguments below work, more strongly, for every nonnegative \(n\times n\) matrix \(A\); neither antisymmetry nor the \(0\)-\(1\) condition is used.

Disjoint unions cause no difficulty:
\[
t(B_1\sqcup B_2,A)=t(B_1,A)t(B_2,A).
\]

---

## 2. The tree inequality

### Lemma 2.1
If \(T\to\vec K_2\) is an oriented tree with \(m\ge1\) arcs, then
\[
Z_T(A)\ge \frac{M^m}{n^{m-1}}. \tag{2}
\]
Consequently \(T\) has the directed Sidorenko property.

### Proof

Let
\[
\pi(i,j)=\frac{A_{ij}}M,\qquad
\alpha(i)=\frac{\sum_jA_{ij}}M,\qquad
\beta(j)=\frac{\sum_iA_{ij}}M.
\]
Thus \(\pi\) is a probability distribution on weighted directed edges, with source marginal \(\alpha\) and sink marginal \(\beta\).

Root \(T\) arbitrarily. Construct a tree-indexed Markov random homomorphism \(\Phi\) as follows:

- sample the root according to \(\alpha\) or \(\beta\), depending on its side;
- recursively, across every edge, use the conditional distribution induced by \(\pi\).

Every oriented edge of \(T\) then has joint distribution \(\pi\), and every source and sink vertex has marginal \(\alpha\) and \(\beta\), respectively.

For this tree-indexed Markov law,
\[
H(\Phi)
=
mH(\pi)
-\sum_{u\in V(T)}(\deg_T(u)-1)H(\mu_u), \tag{3}
\]
where \(\mu_u\) is \(\alpha\) or \(\beta\) according to the side of \(u\).

The Gibbs variational inequality gives
\[
\log Z_T(A)
\ge
H(\Phi)+
\mathbb E\log\prod_{xy\in E(T)}A_{\Phi(x),\Phi(y)}.
\]
Since
\[
H(\pi)+\mathbb E_\pi\log A_{ij}=\log M,
\]
equation (3) yields
\[
\log Z_T(A)
\ge
m\log M-
\sum_u(\deg_T(u)-1)H(\mu_u).
\]
Each marginal entropy is at most \(\log n\), while
\[
\sum_u(\deg_T(u)-1)=2m-(m+1)=m-1.
\]
Hence
\[
\log Z_T(A)\ge m\log M-(m-1)\log n,
\]
which is (2). Dividing by \(n^{m+1}\) gives
\[
t(T,A)\ge\left(\frac{M}{n^2}\right)^m.
\]
\(\square\)

Thus every oriented forest satisfying \(B\to\vec K_2\) has the directed Sidorenko property.

---

## 3. Complete bipartite graphs

### Proposition 3.1
Every orientation of \(K_{a,b}\) in which all edges point from its \(a\)-vertex side to its \(b\)-vertex side has the directed Sidorenko property.

### Proof

For \(\mathbf i=(i_1,\ldots,i_a)\), put
\[
c(\mathbf i)=\sum_j\prod_{\ell=1}^a A_{i_\ell j}.
\]
Then
\[
Z_{K_{a,b}}(A)=\sum_{\mathbf i}c(\mathbf i)^b.
\]
Power-mean gives
\[
Z_{K_{a,b}}(A)
\ge
n^{a(1-b)}
\left(\sum_{\mathbf i}c(\mathbf i)\right)^b.
\]
If \(e_j=\sum_iA_{ij}\) is the weighted indegree of \(j\), then
\[
\sum_{\mathbf i}c(\mathbf i)=\sum_j e_j^a
\ge n\left(\frac Mn\right)^a
=\frac{M^a}{n^{a-1}}.
\]
Therefore
\[
Z_{K_{a,b}}(A)
\ge
M^{ab}n^{a+b-2ab},
\]
which is exactly (1). \(\square\)

---

## 4. A doubled-tree construction

This gives a fairly broad unicyclic family.

### Theorem 4.1
Let \(T\) be a bipartite tree with two distinguished vertices \(a,b\) at distance at least two. Form \(D(T;a,b)\) from two disjoint copies of \(T\) by identifying the two copies of \(a\), and likewise identifying the two copies of \(b\).

Optionally, add one new pendant edge at either or both identified vertices. Orient every edge according to the bipartition. Every graph obtained this way has the directed Sidorenko property.

### Proof

Let \(s=e(T)\). For fixed images \(i,j\) of \(a,b\), let
\[
h(i,j)
\]
be the total weight of homomorphisms of \(T\) extending \(a\mapsto i\), \(b\mapsto j\).

For a distinguished vertex \(x\in\{a,b\}\), let \(\delta_x(z)\) be the appropriate outdegree or indegree of \(z\), according to the side containing \(x\). In either case
\[
\sum_z\delta_x(z)=M.
\]

Let \(\varepsilon_a,\varepsilon_b\in\{0,1\}\) record whether an additional leaf is placed at \(a\) or \(b\), and set \(q=\varepsilon_a+\varepsilon_b\). The homomorphism count of the doubled graph is
\[
Z=
\sum_{i,j}
\delta_a(i)^{\varepsilon_a}
\delta_b(j)^{\varepsilon_b}
h(i,j)^2.
\]
Weighted Cauchy–Schwarz gives
\[
Z\ge
\frac{
\left(
\sum_{i,j}
\delta_a(i)^{\varepsilon_a}
\delta_b(j)^{\varepsilon_b}
h(i,j)
\right)^2
}{
n^{\,2-q}M^q
}. \tag{4}
\]

The numerator before squaring is the homomorphism count of the tree obtained from \(T\) by adding the indicated \(q\) leaves. That tree has \(s+q\) edges, so Lemma 2.1 gives
\[
\sum_{i,j}
\delta_a(i)^{\varepsilon_a}
\delta_b(j)^{\varepsilon_b}
h(i,j)
\ge
\frac{M^{s+q}}{n^{s+q-1}}.
\]
Substitution into (4) yields
\[
Z\ge
\frac{M^{2s+q}}{n^{2s+q}}. \tag{5}
\]

Because the two copies share exactly two vertices, the doubled graph with its \(q\) extra leaves has
\[
e=v=2s+q.
\]
Thus (5) is exactly the required bound (1). \(\square\)

### Consequences

1. Taking \(T\) to be a path of \(k\ge2\) edges gives \(C_{2k}\). Hence every even cycle has the directed Sidorenko property.

2. Every admissible \(B\) of maximum degree at most two has the property, since each component is a path, an even cycle, or an isolated vertex.

3. The theorem also permits symmetric tree decorations on the two halves of an even cycle, as well as one additional unmatched leaf at either of the two identified vertices.

---

## 5. Two six-edge configurations not immediately covered above

For the finite edge bound below, two additional unicyclic graphs need direct estimates.

Put
\[
d_i=\sum_jA_{ij},\qquad
c_j=\sum_iA_{ij},\qquad
Q=AA^\top.
\]

### 5.1. A \(2\)-edge path attached to a \(C_4\)

Suppose a path of two edges is attached at a source-side vertex of \(C_4\). Given that the attachment vertex maps to \(i\), the attached path has
\[
r_i=(Q\mathbf1)_i
\]
extensions. Hence the total homomorphism count is
\[
Z=\sum_i r_i\sum_jQ_{ij}^2.
\]
For every \(i\),
\[
\sum_jQ_{ij}^2\ge \frac{r_i^2}{n}.
\]
Therefore
\[
Z\ge \frac1n\sum_i r_i^3
\ge \frac{(\sum_i r_i)^3}{n^3}. \tag{6}
\]
Moreover,
\[
\sum_i r_i
=\mathbf1^\top Q\mathbf1
=\sum_j c_j^2
\ge \frac{M^2}{n}.
\]
Using this in (6),
\[
Z\ge\frac{M^6}{n^6}.
\]
The graph has six vertices and six edges, so this is precisely its Sidorenko bound. Attachment at a sink-side vertex follows by transposing \(A\).

---

### 5.2. Leaves at two adjacent vertices of a \(C_4\)

Let \(i,j\) denote the source-side cycle vertices and \(u,v\) the sink-side vertices. Put
\[
P_{ijuv}=A_{iu}A_{iv}A_{ju}A_{jv}.
\]
If leaves are attached at the adjacent vertices \(i,u\), the homomorphism count is
\[
Z=\sum_{i,j,u,v}P_{ijuv}\,d_i c_u.
\]
By independently interchanging \(i,j\) and \(u,v\), the same sum is obtained with any of the four corner weights. Consequently,
\[
Z=
\frac14\sum P_{ijuv}
(d_ic_u+d_ic_v+d_jc_u+d_jc_v).
\]
Pointwise AM–GM gives
\[
Z\ge
\sum P_{ijuv}\sqrt{d_id_jc_uc_v}. \tag{7}
\]

Define
\[
R_{iu}=A_{iu}(d_ic_u)^{1/4}.
\]
The right-hand side of (7) equals
\[
\operatorname{tr}\big((RR^\top)^2\big).
\]
If \(S=\sum_{i,u}R_{iu}\), then the largest singular value of \(R\) is at least \(S/n\), and hence
\[
\operatorname{tr}\big((RR^\top)^2\big)\ge \frac{S^4}{n^4}. \tag{8}
\]

It remains to estimate \(S\). Sample \((I,U)\) from the weighted-edge distribution
\[
\Pr[(I,U)=(i,u)]=\frac{A_{iu}}M.
\]
Then
\[
\frac SM=\mathbb E[(d_Ic_U)^{1/4}].
\]
By arithmetic-geometric mean,
\[
\log\frac SM
\ge \frac14\big(\mathbb E\log d_I+\mathbb E\log c_U\big).
\]
The source marginal is \(d_i/M\), so
\[
\mathbb E\log d_I
=\sum_i\frac{d_i}{M}\log d_i
\ge \log\frac Mn,
\]
using the entropy bound \(H(d_i/M)\le\log n\). Similarly,
\[
\mathbb E\log c_U\ge\log\frac Mn.
\]
Thus
\[
S\ge M\left(\frac Mn\right)^{1/2}
=\frac{M^{3/2}}{n^{1/2}}.
\]
Equations (7) and (8) now give
\[
Z\ge\frac{M^6}{n^6},
\]
again exactly the required inequality.

---

## 6. All patterns with at most six arcs

### Corollary 6.1
If \(B\to\vec K_2\) and \(e(B)\le6\), then \(B\) has the directed Sidorenko property.

### Proof

Isolated vertices can be discarded, and disjoint unions preserve the property.

If the underlying graph is acyclic, Lemma 2.1 applies. Otherwise it contains an even cycle.

- A \(6\)-cycle uses all six edges and is covered by Theorem 4.1.
- Otherwise the graph contains a \(C_4\), with at most two further edges.

With one further edge, it is either a disjoint forest edge or a pendant edge; both cases are covered by product closure and Theorem 4.1.

With two further edges, up to swapping the bipartition, the possibilities are:

1. the extra edges lie in forest components;
2. a pendant edge together with a disjoint forest edge;
3. two leaves at the same cycle vertex;
4. one leaf at each of two opposite cycle vertices;
5. one leaf at each of two adjacent cycle vertices;
6. a pendant path of length two;
7. a new vertex adjacent to the two opposite vertices in one side of the \(C_4\), producing \(K_{2,3}\) or \(K_{3,2}\).

Cases 3 and 4 are instances of Theorem 4.1, case 5 is Section 5.2, case 6 is Section 5.1, and case 7 is Proposition 3.1. This exhausts the simple bipartite possibilities. \(\square\)

---

## 7. What remains open

The argument does not establish the conjecture for a general asymmetric decoration of a cycle, let alone for arbitrary higher-cycle-rank bipartite graphs. The doubled-tree proof works because the conditional homomorphism count appears as a square, allowing a lower bound by Cauchy–Schwarz; two nonisomorphic halves instead give a mixed product, for which Cauchy–Schwarz has the wrong direction.

Consequently, this does not resolve Conjecture 1.4. It does show that any minimal counterexample may be taken connected and must:

- have at least seven arcs;
- contain a cycle;
- have maximum degree at least three;
- lie outside the complete-bipartite and doubled-tree families above.

The source paper's general asymmetric Sidorenko reformulation remains the principal unresolved gap.