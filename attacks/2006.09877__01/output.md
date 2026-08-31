```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general question remains open, but local graphs in uniformly doubling metrics—including every subgraph of a fixed-dimensional grid—have bounded twin-width, while every polynomial-expansion class has an explicit sublinear twin-width bound.",
  "would_publish": false,
  "caveats": "The doubling hierarchy is not implied by polynomial expansion, and the general estimate is only o(n); the separator step uses the established Plotkin–Rao–Smith theorem."
}
```

# Mathematical writeup

## 1. Statement and scope

For a graph \(G\), write

\[
\nabla_r(G)=\max_H \frac{|E(H)|}{|V(H)|},
\]

where the maximum is over all \(r\)-shallow minors \(H\) of \(G\). A class \(\mathcal C\) has polynomial expansion if, for some constants \(A\) and integer \(k\ge 0\),

\[
\nabla_r(G)\le A(r+1)^k
\qquad
(G\in\mathcal C,\ r\ge 0).
\]

The open question asks whether this implies

\[
\sup_{G\in\mathcal C}\operatorname{tww}(G)<\infty.
\]

I do not prove or disprove this. I establish:

1. a bounded-contact hierarchy criterion for bounded twin-width;
2. as a concrete consequence, every finite subgraph of the \(d\)-dimensional integer grid has twin-width at most
   \[
   (2d+1)2^d-1;
   \]
   in particular, every subgraph of the three-dimensional grid has twin-width at most \(55\);
3. more generally, graphs locally realized in a uniformly doubling metric have bounded twin-width;
4. every polynomial-expansion class satisfies an explicit uniform sublinear estimate
   \[
   \operatorname{tww}(G)
   =
   O_{A,k}\!\left(
   (n\log(n+1))^{\,1-\frac1{2k+2}}
   \right).
   \]

The last estimate falls short of a constant bound.

---

## 2. A bounded-contact hierarchy lemma

At every stage of a contraction sequence, each trigraph vertex represents a part of a partition of \(V(G)\). For two parts \(X,Y\):

- \(XY\) is a black edge if \(G[X,Y]\) is complete;
- \(XY\) is a nonedge if \(G[X,Y]\) is empty;
- \(XY\) is red otherwise.

This follows inductively from the contraction rule. In particular:

\[
XY\text{ red}\quad\Longrightarrow\quad E_G(X,Y)\ne\varnothing.
\tag{2.1}
\]

### Lemma 2.1 — bounded-contact hierarchies

Suppose \(G\) admits partitions

\[
\mathcal P_0,\mathcal P_1,\ldots,\mathcal P_L
\]

such that:

1. \(\mathcal P_0\) is the singleton partition and \(\mathcal P_L=\{V(G)\}\);
2. every part of \(\mathcal P_{i+1}\) is the union of at most \(a\) parts of \(\mathcal P_i\);
3. for every \(i\), the contact graph on \(\mathcal P_i\), where distinct parts are adjacent when at least one edge of \(G\) runs between them, has maximum degree at most \(b\).

Then

\[
\operatorname{tww}(G)\le a(b+1)-1.
\]

#### Proof

For each \(i\), transform \(\mathcal P_i\) into \(\mathcal P_{i+1}\) by processing the parts \(P\in\mathcal P_{i+1}\) one at a time and merging all current clusters contained in \(P\). There are at most \(a\) such clusters.

During this transition, every current cluster lies in a unique part \(P\in\mathcal P_{i+1}\), and each such \(P\) contains at most \(a\) current clusters. Let \(X\subseteq P\) be a current cluster. If \(X\) has a red edge to a current cluster \(Y\subseteq Q\), then by (2.1) there is an original edge between \(X\) and \(Y\). Hence either \(P=Q\), or \(P\) and \(Q\) are adjacent in the contact graph of \(\mathcal P_{i+1}\).

There are at most \(b+1\) possibilities for \(Q\), including \(Q=P\), and at most \(a\) current clusters in each \(Q\). Thus the red degree of \(X\) is at most

\[
a(b+1)-1.
\]

After all levels are processed, only one cluster remains. ∎

---

## 3. All subgraphs of a fixed-dimensional grid have bounded twin-width

Let \(\mathcal L_d\) be the class of finite graphs \(G\) admitting an injective map

\[
\varphi:V(G)\longrightarrow \mathbb Z^d
\]

such that every edge \(uv\in E(G)\) satisfies

\[
\|\varphi(u)-\varphi(v)\|_1=1.
\]

Edges of the ambient grid may be deleted arbitrarily.

### Theorem 3.1

For every \(G\in\mathcal L_d\),

\[
\operatorname{tww}(G)\le (2d+1)2^d-1.
\tag{3.1}
\]

Moreover,

\[
\nabla_r(G)\le d(2r+1)^d.
\tag{3.2}
\]

Thus \(\mathcal L_d\) is a hereditary, indeed subgraph-closed, polynomial-expansion class of bounded twin-width.

#### Proof of the twin-width bound

Choose an axis-parallel integer cube of side length \(2^L\) containing \(\varphi(V(G))\). Recursively divide it into \(2^d\) congruent subcubes. For \(0\le i\le L\), let \(\mathcal P_i\) be the partition of \(V(G)\) obtained from the occupied cubes of side length \(2^i\).

At level \(0\), every cube contains at most one lattice point, so \(\mathcal P_0\) is the singleton partition. At level \(L\), there is one part.

Each cube has \(2^d\) children, so the refinement arity is

\[
a=2^d.
\]

Two distinct same-sized cubes can contain endpoints of a grid edge only if they share a codimension-one face. Every cube has at most \(2d\) such neighboring cubes. Thus every contact graph has maximum degree

\[
b\le 2d.
\]

Lemma 2.1 gives (3.1).

For \(d=3\), this yields

\[
\operatorname{tww}(G)\le 8\cdot 7-1=55.
\]

#### Proof of polynomial expansion

Let \(H\) be an \(r\)-shallow minor of \(G\), and let \(B\) be one of its branch sets. Since \(B\) has graph radius at most \(r\), it lies in an \(\ell_1\)-ball of radius \(r\) in \(\mathbb Z^d\). Hence

\[
|B|\le (2r+1)^d.
\]

Every vertex of \(G\) has degree at most \(2d\), so at most

\[
2d(2r+1)^d
\]

edges leave \(B\). Consequently,

\[
\Delta(H)\le 2d(2r+1)^d,
\]

and therefore

\[
\frac{|E(H)|}{|V(H)|}\le d(2r+1)^d.
\]

This proves (3.2). ∎

This eliminates arbitrary edge-deleted three-dimensional grids as a possible counterexample: despite their not belonging to any fixed proper minor-closed class, the spatial hierarchy gives a bounded contraction sequence.

---

## 4. Extension to doubling metrics

The preceding argument is not specific to cubical partitions.

A metric space \((X,\rho)\) is \(\lambda\)-doubling if every ball of radius \(R\) can be covered by at most \(\lambda\) balls of radius \(R/2\).

### Theorem 4.1

Let \(G\) be a finite graph whose vertices form a \(1\)-separated subset of a \(\lambda\)-doubling metric space \((X,\rho)\), and suppose

\[
uv\in E(G)\quad\Longrightarrow\quad \rho(u,v)\le 1.
\]

Then

\[
\operatorname{tww}(G)\le \lambda^7-1.
\tag{4.1}
\]

The class of all such graphs, for fixed \(\lambda\), has polynomial expansion.

#### Proof

Set \(s_i=2^i\). Let \(N_0=V(G)\), and recursively let \(N_{i+1}\) be a maximal \(s_{i+1}\)-separated subset of \(N_i\). Assign every \(q\in N_i\) to a parent \(p\in N_{i+1}\) with

\[
\rho(p,q)<s_{i+1}=2s_i.
\]

Selected points are assigned to themselves. For sufficiently large \(L\), \(N_L\) consists of one point.

The parent maps define nested partitions \(\mathcal P_i\). A standard packing estimate in a doubling metric gives:

- every parent has at most \(\lambda^3\) children, since its children are \(s_i\)-separated and lie in a ball of radius \(2s_i\);
- every part of \(\mathcal P_i\) lies within distance less than
  \[
  s_1+\cdots+s_i<2s_i
  \]
  of its net point.

If parts centered at \(p,q\in N_i\) contain endpoints of an edge, then

\[
\rho(p,q)<2s_i+1+2s_i\le 5s_i.
\]

The \(s_i\)-separated points in a ball of radius \(5s_i\) number at most \(\lambda^4\): after four applications of doubling, the covering balls have diameter less than \(s_i\). Thus the contact graph of \(\mathcal P_i\) has maximum degree at most \(\lambda^4-1\).

Lemma 2.1, with \(a=\lambda^3\) and \(b=\lambda^4-1\), now gives

\[
\operatorname{tww}(G)
\le
\lambda^3\lambda^4-1
=
\lambda^7-1.
\]

For expansion, the \(1\)-separation and doubling condition imply

\[
|V(G)\cap B_\rho(x,r)|
=
O_\lambda\!\left(r^{\log_2\lambda}\right).
\]

They also give \(\Delta(G)=O_\lambda(1)\). A radius-\(r\) branch set is contained in such a metric ball because every graph edge has metric length at most \(1\). Its number of outgoing edges is consequently

\[
O_\lambda\!\left(r^{\log_2\lambda}\right).
\]

Every \(r\)-shallow minor therefore has maximum degree, and hence density, bounded by a polynomial in \(r\). ∎

In particular, graphs of uniformly bounded shortest-path doubling dimension have bounded twin-width. The ambient formulation is stronger: arbitrary edge-subgraphs of a fixed doubling host are covered even if deleting edges destroys doubling of the intrinsic graph metric.

---

## 5. A general sublinear bound from polynomial expansion

The following does not yield bounded twin-width, but it applies to every polynomial-expansion class.

### Theorem 5.1

Suppose

\[
\nabla_r(G)\le A(r+1)^k
\]

for every \(G\in\mathcal C\) and every \(r\ge0\). If \(G\in\mathcal C\) has \(n\) vertices, then

\[
\operatorname{tww}(G)
=
O_{A,k}\!\left(
(n\log(n+1))^{\frac{2k+1}{2k+2}}
\right).
\tag{5.1}
\]

In particular, \(\operatorname{tww}(G)=o(n)\) uniformly over \(\mathcal C\).

### 5.1. Separators

Use the established Plotkin–Rao–Smith shallow-minor separator theorem in the following standard form: there are absolute constants \(c_0,c_1\) such that, for integers \(\ell,h\ge1\), every \(m\)-vertex graph either

- contains \(K_h\) as a \(c_0\ell\log(m+1)\)-shallow minor, or
- has a \(2/3\)-balanced separator of size at most
  \[
  c_1\left(\frac m\ell+\ell h^2\log(m+1)\right).
  \tag{5.2}
  \]

Let \(F\) be any subgraph of \(G\). Its shallow-minor densities satisfy the same expansion bound. Put

\[
R=\left\lceil c_0\ell\log(m+1)\right\rceil
\]

and choose

\[
h=\left\lfloor 2A(R+1)^k\right\rfloor+2.
\]

Then \(K_h\) cannot be an \(R\)-shallow minor, because otherwise

\[
\nabla_R(F)\ge \frac{h-1}{2}>A(R+1)^k.
\]

Thus \(F\) has a balanced separator of size

\[
O_{A,k}\left(
\frac m\ell+
\ell^{2k+1}(\log(m+1))^{2k+1}
\right).
\tag{5.3}
\]

Set

\[
p=2k+1,
\qquad
\beta=\frac p{p+1}
=\frac{2k+1}{2k+2},
\]

and choose

\[
\ell\asymp
\frac{m^{1/(p+1)}}{(\log(m+1))^{p/(p+1)}}.
\]

Both terms in (5.3) are then

\[
O_{A,k}\bigl((m\log(m+1))^\beta\bigr).
\tag{5.4}
\]

Hence every subgraph of \(G\) has a \(2/3\)-balanced separator of the order in (5.4).

### 5.2. From separators to pathwidth

Recursively separate the graph. If \(S\) is a balanced separator and \(C_1,\ldots,C_t\) are the components of \(F-S\), take path decompositions of each \(F[C_i]\), add all of \(S\) to every bag, and concatenate the decompositions.

Along any recursion branch, the number of vertices decreases by a factor at most \(2/3\). Therefore

\[
\begin{aligned}
\operatorname{pw}(G)
&\le
O_{A,k}\left(
\sum_{j\ge0}
\left(
(2/3)^j n\log(n+1)
\right)^\beta
\right)\\
&=
O_{A,k}\left(
(n\log(n+1))^\beta
\right).
\tag{5.5}
\end{aligned}
\]

### 5.3. From pathwidth to twin-width

For completeness, a graph of pathwidth \(q\) has twin-width at most \(q+1\).

Take a path decomposition \(B_1,\ldots,B_t\) of width \(q\). Each vertex \(v\) occurs on an interval \([a(v),b(v)]\). Order the vertices \(v_1,\ldots,v_n\) by nondecreasing right endpoint \(b(v_i)\), and successively merge the prefix

\[
A_i=\{v_1,\ldots,v_i\}
\]

into one cluster.

If an uncontracted vertex \(v_j\), \(j>i\), has a neighbor \(v_h\in A_i\), then the two decomposition intervals intersect, and

\[
a(v_j)\le b(v_h)\le b(v_i)\le b(v_j).
\]

Thus \(v_j\in B_{b(v_i)}\). Every red neighbor of \(A_i\) must have at least one edge into \(A_i\), so \(A_i\) has at most \(q+1\) red neighbors. All uncontracted vertices remain singletons and can have a red edge only to \(A_i\). This is a \((q+1)\)-contraction sequence.

Combining this with (5.5) proves (5.1). ∎

As a separate endpoint observation, if \(k=0\), then the expansion function is uniformly bounded for all depths. Such a class excludes a fixed complete graph as a minor, since every finite minor model is an \(r\)-shallow model for some \(r\). The established bounded-twin-width theorem for proper minor-closed classes therefore gives a constant bound in this degree-zero case.

---

## 6. Remaining gap

The conjecture asks for a bound depending only on \(A\) and \(k\), whereas Theorem 5.1 still grows as a positive power of \(n\).

The hierarchy lemma explains one obstruction in the present approach. It needs, simultaneously:

- bounded refinement arity; and
- bounded maximum degree of every scale-contact graph.

Doubling geometry supplies both. Polynomial expansion only controls the density of shallow minors by \(O(r^k)\), which permits contact complexity to grow polynomially with the scale. The separator theorem converts this into strongly sublinear separators and pathwidth, but not into a constant-width contraction hierarchy.

Nor is doubling a consequence of polynomial expansion: finite binary trees have uniformly bounded expansion, while their shortest-path doubling constants are unbounded. Trees are nevertheless of bounded twin-width for different reasons, showing that a full proof would need to combine geometric and tree-like mechanisms rather than rely on doubling alone.

Thus no case in the argument yields either a counterexample or a uniform bound for arbitrary polynomial-expansion classes.