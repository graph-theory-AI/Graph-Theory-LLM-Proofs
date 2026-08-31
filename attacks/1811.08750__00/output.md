```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "As written, T=K1 and F={K2} satisfy the blow-up hypothesis, but ex(G,K1,{K2})=n is exactly computable.",
  "would_publish": false,
  "caveats": "The counterexample uses an edgeless target; if e(T)>0 is a standing assumption omitted by the catalog, the full claim remains open, though the consecutive-clique case is proved below."
}
```

## 1. The literal statement has a degenerate counterexample

I use the standard convention that a blow-up replaces every vertex by an independent set and every edge by the corresponding complete bipartite graph.

Take
\[
T=K_1,\qquad \mathcal F=\{K_2\}.
\]

Every blow-up of \(K_1\) is edgeless. Consequently \(K_2\) is not a subgraph of any blow-up of \(K_1\), so the stated hypothesis is satisfied.

Let \(G\) be any \(n\)-vertex graph. The spanning empty subgraph
\[
H=(V(G),\varnothing)
\]
is \(K_2\)-free and contains exactly \(n\) copies of \(K_1\). No subgraph of \(G\) can contain more than \(n\) copies of \(K_1\). Hence
\[
\operatorname{ex}(G,K_1,\{K_2\})=n.
\]
Thus the value, and an optimal subgraph, can be found exactly in polynomial time. In particular, for every \(\epsilon>0\), it is approximated with additive error \(0\), rather than merely \(n^{1-\epsilon}\).

More generally, for the edgeless graph \(\overline K_t\),
\[
\operatorname{ex}(G,\overline K_t,\{K_2\})=\binom nt.
\]

There is a second scope defect if the empty forbidden family is allowed: for \(T=K_2\) and \(\mathcal F=\varnothing\),
\[
\operatorname{ex}(G,K_2,\varnothing)=e(G)
\]
is again exactly computable, while the blow-up condition is vacuous. Thus a repaired formulation should at least require
\[
e(T)>0\quad\text{and}\quad \mathcal F\ne\varnothing.
\]

Strictly speaking, membership in polynomial time does not unconditionally prove non-NP-hardness without separating \(P\) from \(NP\). The conclusion above uses the standard interpretation of such conjectures: under \(P\ne NP\), an exactly polynomial-time solvable case contradicts the claimed hardness dichotomy. If the full source paper has a standing assumption \(e(T)>0\) that was omitted from the catalog statement, then this is a defect only in the cataloged formulation.

## 2. A nondegenerate partial result: consecutive cliques

Even after imposing \(e(T)>0\), one natural boundary case is not covered by Theorem 1.7 as quoted. The following proves it.

### Theorem

For every fixed \(m\ge 2\) and every fixed \(\epsilon>0\), it is NP-hard to approximate
\[
\operatorname{ex}(G,K_m,\{K_{m+1}\})
\]
within additive error \(n^{m-\epsilon}\).

Since a blow-up of \(K_m\) is \(m\)-partite, it contains no \(K_{m+1}\). Thus these pairs satisfy the conjecture's hypothesis.

### 2.1 Exact hardness for maximum triangle-free edge subgraphs

Write
\[
z(Q)=\operatorname{ex}(Q,K_2,\{K_3\}),
\]
the maximum number of edges in a triangle-free subgraph of \(Q\).

We first show that computing \(z(Q)\) is NP-hard even when \(\omega(Q)\le 3\).

Let \(\tau(Y)\) denote the minimum vertex-cover number of a graph \(Y\). We use the elementary identity
\[
\tau(Y)=\min_{S\subseteq V(Y)}\bigl(|S|+e(Y-S)\bigr).
\tag{1}
\]
Indeed, a vertex cover \(S\) gives equality with \(e(Y-S)=0\). Conversely, from arbitrary \(S\), add one endpoint of every edge of \(Y-S\); this produces a vertex cover of size at most \(|S|+e(Y-S)\).

We first reduce Vertex Cover to Vertex Cover on triangle-free graphs. Given \(Y\), replace each edge \(uv\) by the path
\[
u-a_{uv}-b_{uv}-v,
\]
with all new vertices distinct; call the resulting graph \(X\). The graph \(X\) is triangle-free. If \(S\subseteq V(Y)\) is the set of original vertices selected for a vertex cover of \(X\), then on the path replacing \(uv\):

- one internal vertex is needed if \(u\in S\) or \(v\in S\);
- both internal vertices are needed if \(u,v\notin S\).

Consequently, if \(r=e(Y)\),
\[
\tau(X)
 =r+\min_{S\subseteq V(Y)}\bigl(|S|+e(Y-S)\bigr)
 =r+\tau(Y).
\tag{2}
\]
Thus Vertex Cover remains NP-hard on triangle-free graphs.

Now let \(X\) be triangle-free and form the cone \(Q\) by adding one vertex \(c\) adjacent to every vertex of \(X\). The triangles of \(Q\) are exactly
\[
cuv,\qquad uv\in E(X).
\]
Let \(\delta_\triangle(Q)\) be the minimum number of edges that must be deleted to make \(Q\) triangle-free. For a deletion set \(D\), put
\[
S=\{v\in V(X):cv\in D\}.
\]
For every edge \(uv\) of \(X-S\), neither spoke \(cu\) nor \(cv\) was deleted, so the base edge \(uv\) itself must be deleted. Conversely, deleting the spokes \(cv\) for \(v\in S\), together with every edge of \(X-S\), destroys all triangles. Hence
\[
\delta_\triangle(Q)
 =\min_{S\subseteq V(X)}\bigl(|S|+e(X-S)\bigr)
 =\tau(X)
\]
by (1). Therefore
\[
z(Q)=e(Q)-\tau(X).
\tag{3}
\]
This proves exact NP-hardness of \(z(Q)\). Moreover, because \(X\) is triangle-free, the cone \(Q\) has clique number at most \(3\).

### 2.2 Lifting exact hardness to \(K_m\) versus \(K_{m+1}\)

Define
\[
W_m(R)=\operatorname{ex}(R,K_m,\{K_{m+1}\}).
\]

For \(m=2\), this is just \(z(R)\). Fix \(m\ge3\), and put
\[
r=m-2.
\]
Let \(Q\) be one of the graphs from the previous subsection, with \(q=v(Q)\) and \(\omega(Q)\le3\). Set
\[
C_q=\binom q3,\qquad M=2rC_q+1.
\]
Let \(B\) be the complete \(r\)-partite graph with \(M\) vertices in each part, and let
\[
R=B\vee Q
\]
be the join of \(B\) and \(Q\).

We claim that
\[
M^r z(Q)
 \le W_m(R)
 \le M^r z(Q)+rM^{r-1}C_q
 <M^r\left(z(Q)+\frac12\right).
\tag{4}
\]

#### Lower bound

Let \(J\subseteq Q\) be a triangle-free subgraph with \(e(J)=z(Q)\). Retain all edges of \(B\), all edges between \(B\) and \(Q\), and only the edges of \(J\) inside \(Q\).

A \(K_{m+1}=K_{r+3}\) would have to use one vertex from every one of the \(r\) parts of \(B\) and three vertices forming a triangle in \(J\), which is impossible. Every edge of \(J\), together with one vertex from each part of \(B\), gives a \(K_m\). Thus this subgraph has exactly
\[
M^r z(Q)
\]
copies of \(K_m\).

#### Upper bound

Let \(H\subseteq R\) be \(K_{m+1}\)-free. Since \(B\) has only \(r=m-2\) parts and \(\omega(Q)\le3\), every \(K_m\) in \(H\) has one of two forms:

1. \(r\) vertices in \(B\) and two vertices in \(Q\);
2. \(r-1\) vertices in \(B\) and three vertices in \(Q\).

For the first type, fix a transversal
\[
\mathbf b=(b_1,\dots,b_r)
\]
of the parts of \(B\) that forms a clique in \(H\). Let \(S_{\mathbf b}\subseteq V(Q)\) be its common neighborhood in \(H\). The graph \(H[S_{\mathbf b}]\) must be triangle-free, since a triangle there together with \(\mathbf b\) would form a \(K_{m+1}\). It therefore has at most \(z(Q)\) edges. There are at most \(M^r\) transversals, so the number of first-type \(K_m\)'s is at most
\[
M^r z(Q).
\]

For the second type, one of the \(r\) parts of \(B\) is omitted. There are at most
\[
rM^{r-1}
\]
choices for the vertices in \(B\), and at most \(C_q\) choices for the three vertices in \(Q\). Hence there are at most
\[
rM^{r-1}C_q
\]
such copies.

This proves (4). Since \(M>2rC_q\), one can recover \(z(Q)\) from the exact value \(W_m(R)\) by
\[
z(Q)=\left\lfloor\frac{W_m(R)}{M^r}\right\rfloor.
\]
Thus computing \(W_m\) exactly is NP-hard for every fixed \(m\ge2\).

### 2.3 Balanced blow-ups amplify exact hardness

For a graph \(G\), let \(G^{(s)}\) be its balanced blow-up in which every vertex is replaced by an independent set of size \(s\).

For all \(m<k\),
\[
\operatorname{ex}(G^{(s)},K_m,\{K_k\})
 =
s^m\operatorname{ex}(G,K_m,\{K_k\}).
\tag{5}
\]

For the lower bound, blow up an optimal \(K_k\)-free subgraph of \(G\). A \(K_k\) in the blow-up would project to a \(K_k\) in the base graph, while each base \(K_m\) gives exactly \(s^m\) copies.

For the upper bound, let \(H\subseteq G^{(s)}\) be \(K_k\)-free and choose independently one uniformly random vertex from each blow-up class. Every resulting transversal is a \(K_k\)-free subgraph of \(G\). Every \(K_m\) of \(H\) uses \(m\) distinct classes and is selected with probability \(s^{-m}\). Thus
\[
\frac{N(K_m,H)}{s^m}
 =
\mathbb E\,N(K_m,\text{random transversal})
 \le \operatorname{ex}(G,K_m,\{K_k\}),
\]
which proves (5).

Now fix \(m\ge2\) and \(\epsilon>0\), and suppose there were an algorithm with additive error \(N^{m-\epsilon}\). Given an exact-hardness instance \(R\) on \(p\) vertices, choose
\[
a=\left\lceil\frac m\epsilon\right\rceil,\qquad
L=\left\lceil4^{1/\epsilon}\right\rceil,\qquad
s=Lp^a.
\]
Then \(s^\epsilon\ge4p^m\). For \(N=ps\),
\[
N^{m-\epsilon}
 =s^m\frac{p^{m-\epsilon}}{s^\epsilon}
 \le \frac{s^m}{4p^\epsilon}
 \le \frac{s^m}{4}.
\]
By (5),
\[
W_m(R^{(s)})=s^mW_m(R).
\]
An additive approximation therefore determines \(W_m(R)\) exactly by rounding to the nearest multiple of \(s^m\). Since \(s\) is polynomial in \(p\) for fixed \(m,\epsilon\), this is a polynomial reduction. The theorem follows.

Consequently, accepting Theorem 1.7 as quoted, the singleton clique cases are covered for every
\[
2\le m<k:
\]
the source theorem handles \(k\ge m+2\), and the argument above handles \(k=m+1\).

## 3. Remaining gap

After adding the natural hypotheses \(e(T)>0\) and \(\mathcal F\ne\varnothing\), the general conjecture remains unresolved by this argument.

The clique amplification identity (5) is special. For a noncomplete \(T\), a copy of \(T\) in a blow-up may place several nonadjacent vertices in the same blow-up class, so random transversals do not recover all copies with a uniform \(s^{-v(T)}\) factor. Moreover, blow-ups need not preserve general \(F\)-freeness: for example, a triangle is \(C_5\)-free, but a sufficiently large blow-up of a triangle contains a \(C_5\). These are genuine obstacles to extending the proof to arbitrary \(T\) and \(\mathcal F\).

I have not verified whether the consecutive-clique argument is already present elsewhere; it is self-contained here and is not asserted to be novel.