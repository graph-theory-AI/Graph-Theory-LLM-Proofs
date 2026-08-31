```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "With prime meaning module-prime, and apart from convention-dependent graphs of order at most two, the product is prime exactly when d is at least two, every n_i is at least two, and at most one n_i equals two.",
  "would_publish": false,
  "caveats": "The only ambiguity concerns whether graphs on one or two vertices are called prime."
}
```

## Statement

A **module** (or homogeneous set) in a graph \(G\) is a set \(M\subseteq V(G)\) such that
\[
2\le |M|<|V(G)|
\]
and every vertex outside \(M\) is either adjacent to every vertex of \(M\), or to none of them. A graph is prime if it has no module.

Let
\[
G=\prod_{i=1}^{d}K_{n_i},
\qquad
N=\prod_{i=1}^{d}n_i,
\]
where the product is the tensor/direct product. Thus \(V(G)=\prod_i A_i\), with \(|A_i|=n_i\), and
\[
xy\in E(G)\quad\Longleftrightarrow\quad x_i\ne y_i\text{ for every }i.
\]

### Theorem

Under the definition above,
\[
G\text{ is prime}
\]
if and only if either

1. \(N\le 2\), or
2. \(d\ge2\), every \(n_i\ge2\), and at most one \(n_i\) equals \(2\).

If one adopts the convention that a prime graph must have at least four vertices, then only condition 2 remains.

In particular, in the nondegenerate range \(N\ge3\),
\[
\boxed{\;
\prod_{i=1}^{d}K_{n_i}\text{ is prime}
\iff
d\ge2,\quad n_i\ge2\ \forall i,\quad
|\{i:n_i=2\}|\le1.
\;}
\]

## 1. Connectivity of the product

Assume first that every \(n_i\ge2\).

### Lemma 1

The graph \(G\) is connected if and only if at most one of the \(n_i\) equals \(2\).

#### Proof

Suppose first that \(n_p=n_q=2\) for two distinct coordinates \(p,q\). Label both coordinate sets by \(\{0,1\}\). Along every edge, both binary coordinates are flipped. Hence
\[
x_p\oplus x_q
\]
is constant on every connected component. In particular,
\[
C=\{x:x_p=x_q\}
\]
has no edges to its complement, so \(G\) is disconnected.

Conversely, suppose at most one coordinate has size \(2\).

If all \(n_i\ge3\), then for any vertices \(x,y\), choose \(w_i\in A_i\setminus\{x_i,y_i\}\). This gives
\[
x\sim w\sim y.
\]

Now suppose exactly one coordinate, say \(r\), has size \(2\).

- If \(x_r=y_r\), choose \(w_r\ne x_r\), and for \(i\ne r\) choose
  \[
  w_i\notin\{x_i,y_i\}.
  \]
  Again \(x\sim w\sim y\).

- If \(x_r\ne y_r\), construct a three-edge walk \(x\sim a\sim b\sim y\). Put
  \[
  a_r=y_r,\qquad b_r=x_r.
  \]
  For each \(i\ne r\), choose \(a_i\ne x_i\), and then choose
  \[
  b_i\notin\{a_i,y_i\},
  \]
  which is possible because \(n_i\ge3\). Every consecutive pair then differs in every coordinate.

Thus \(G\) is connected. ∎

## 2. A connected nontrivial product is prime

The following is the essential argument.

### Lemma 2

Suppose \(d\ge2\), every \(n_i\ge2\), and \(G\) is connected. Then \(G\) is prime.

#### Proof

Suppose, for a contradiction, that \(M\) is a module with
\[
2\le |M|<|V(G)|.
\]
Since \(G\) is connected, there is an edge between \(M\) and its complement. Choose
\[
z\notin M,\qquad x_0\in M,\qquad z\sim x_0.
\]
Because \(M\) is a module, \(z\) must in fact be adjacent to every vertex of \(M\).

Choose distinct \(x,y\in M\). There is a coordinate \(j\) with \(x_j\ne y_j\). Since \(z\) is adjacent to both \(x\) and \(y\),
\[
z_j\ne x_j,\qquad z_j\ne y_j.
\]
Choose another coordinate \(k\ne j\), possible because \(d\ge2\).

Construct a vertex \(u\) as follows:
\[
u_j=y_j,\qquad u_k=z_k,
\]
and for every \(i\notin\{j,k\}\), choose any
\[
u_i\ne x_i,
\]
which is possible because \(n_i\ge2\).

Then:

- \(u\sim x\), since \(u_i\ne x_i\) in every coordinate;
- \(u\not\sim y\), since \(u_j=y_j\);
- \(u\not\sim z\), since \(u_k=z_k\).

Thus \(u\) distinguishes the two vertices \(x,y\in M\). Consequently \(u\) cannot lie outside \(M\), because every outside vertex must be either complete or anticomplete to \(M\). Hence \(u\in M\).

But \(z\) is complete to \(M\), so \(z\sim u\), contradicting \(u_k=z_k\). Therefore no such module exists. ∎

Combining Lemmas 1 and 2 proves primeness whenever
\[
d\ge2,\qquad n_i\ge2\text{ for all }i,\qquad
|\{i:n_i=2\}|\le1.
\]

## 3. Necessity of the conditions

Assume \(N\ge3\).

### A factor \(K_1\)

If some \(n_i=1\), no two vertices can differ in every coordinate. Hence \(G\) is edgeless. Every two-vertex subset is then a proper module, so \(G\) is not prime.

### Only one factor

If \(d=1\), then \(G=K_{n_1}\). For \(n_1\ge3\), every two-vertex subset is a proper module, since every outside vertex is complete to it. Thus \(G\) is not prime.

### At least two binary factors

Suppose \(n_p=n_q=2\) for distinct \(p,q\). As in Lemma 1, label these coordinates by \(\{0,1\}\) and set
\[
M=\{x:x_p=x_q\}.
\]
Every edge flips both binary coordinates, so there are no edges between \(M\) and \(V(G)\setminus M\). Moreover,
\[
|M|=\frac{N}{2}\ge2.
\]
Thus \(M\) is a proper module, and \(G\) is not prime.

These cases exhaust the failure of the stated conditions.

## 4. Small orders

If \(N\le2\), there is no set \(M\) satisfying
\[
2\le |M|<N.
\]
Thus such graphs are prime under the literal “no proper nontrivial module” definition. Some authors instead require a prime graph to have at least four vertices; under that convention these vacuous cases are omitted.

## 5. Status and gaps

There are no mathematical gaps in the characterization above. The catalog entry is internally inconsistent: it labels the question open while also stating that it is addressed by Theorem 4.35 of the source paper. The elementary argument above independently confirms the characterization, so the appropriate status is “already resolved,” not open.