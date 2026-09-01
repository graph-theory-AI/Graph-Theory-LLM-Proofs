```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The specific graph U_t remains unresolved, but an alternative induced-universal graph has O(sqrt(n)) separators, while the generic bound for U_t improves to O_t(n^(3/4)(log n)^(3/4)).",
  "would_publish": false,
  "caveats": "The alternative graph need not retain U_t's no-infinite-subdivision feature, and no counterexample or bounded-fibre description is obtained for U_t itself."
}
```

# 1. Statement and outcome

Fix \(t\), and let \(U_t\) be the particular induced-universal graph constructed in the source paper. I do not prove or disprove that every finite \(n\)-vertex subgraph of \(U_t\) has a balanced separator of order \(O_t(\sqrt n)\).

I obtain three partial results.

1. A bounded-fibre transfer lemma shows that the non-induced universal graph from the earlier part of the paper can be converted into a different induced-universal graph while preserving \(O(\sqrt n)\) separators. Thus induced universality itself is not the obstruction.
2. Using the quantitative Plotkin–Rao–Smith theorem and optimizing its parameter gives the slightly sharper bound
   \[
   O_t\!\left(n^{3/4}(\log n)^{3/4}\right)
   \]
   for finite subgraphs of the actual \(U_t\).
3. Linear expansion, linear strong coloring numbers, bounded degree, and exclusion of a subdivision of \(K_{\aleph_0}\) do not by themselves imply \(O(\sqrt n)\) separators. A countable disjoint union of suitably subdivided cubic expanders has all these properties but has finite \(n\)-vertex subgraphs whose minimum balanced separator has order
   \[
   \Theta(\sqrt{n\log n}).
   \]

Throughout, “balanced” means that every component after deleting the separator has at most \(2n/3\) vertices.

# 2. A separator-transfer lemma

## Lemma 2.1: weighted separators

Let \(H\) be a graph such that every finite \(q\)-vertex subgraph has a balanced separator of order at most \(C\sqrt q\). Let \(Q\) be a finite subgraph of \(H\), with nonnegative vertex weights of total weight \(W\). Then \(Q\) has a set \(S\) of order at most
\[
\frac{C}{1-\sqrt{2/3}}\sqrt{|V(Q)|}
\]
such that every component of \(Q-S\) has weight at most \(2W/3\).

### Proof

Start with \(Q_0=Q\). Take an unweighted balanced separator \(S_0\) in \(Q_0\). If every component of \(Q_0-S_0\) has weight at most \(2W/3\), stop.

Otherwise there is a unique component \(Q_1\) of weight greater than \(2W/3\). Since \(S_0\) is unweighted-balanced,
\[
|V(Q_1)|\le \frac23|V(Q_0)|.
\]
Repeat inside \(Q_1\). At stage \(i\), if a component of weight greater than \(2W/3\) remains, it has at most \(2/3\) as many vertices as the preceding component. Hence
\[
|V(Q_i)|\le \left(\frac23\right)^i |V(Q)|.
\]
The union \(S\) of all separators used therefore has order at most
\[
C\sum_{i\ge0}\sqrt{|V(Q_i)|}
 \le C\sqrt{|V(Q)|}\sum_{i\ge0}\left(\sqrt{\frac23}\right)^i
 =\frac{C}{1-\sqrt{2/3}}\sqrt{|V(Q)|}.
\]
Every component discarded during the process has weight at most \(2W/3\), as does every final component. ∎

## Lemma 2.2: bounded-fibre transfer

Suppose \(\pi:G\to H\) satisfies:

- every fibre \(\pi^{-1}(v)\) has order at most \(m\);
- for every edge \(xy\in E(G)\), either \(\pi(x)=\pi(y)\) or \(\pi(x)\pi(y)\in E(H)\).

If every finite \(q\)-vertex subgraph of \(H\) has a balanced separator of order at most \(C\sqrt q\), then every finite \(n\)-vertex subgraph of \(G\) has a balanced separator of order
\[
O(mC\sqrt n).
\]

### Proof

Let \(F\) be an \(n\)-vertex subgraph of \(G\), and let \(Q\) be the subgraph of \(H\) induced by \(\pi(V(F))\). Give \(v\in V(Q)\) weight
\[
w(v)=|V(F)\cap\pi^{-1}(v)|.
\]
The total weight is \(n\).

Apply Lemma 2.1 to obtain a weighted balanced separator \(S\subseteq V(Q)\) of order \(O(C\sqrt{|V(Q)|})\). Delete from \(F\) every vertex whose projection lies in \(S\). This deletes at most
\[
m|S|=O(mC\sqrt n)
\]
vertices. Every remaining component projects into a component of \(Q-S\), so it has at most \(2n/3\) vertices. ∎

# 3. An alternative induced-universal graph with \(O(\sqrt n)\) separators

Let \(B_t\) denote the source paper’s earlier, not necessarily induced, universal graph: every countable \(K_t\)-minor-free graph occurs in \(B_t\) as a subgraph, and finite subgraphs of \(B_t\) have \(O_t(\sqrt n)\) separators and bounded density.

Because \(\nabla_0(B_t)\) is bounded, there is an integer \(D_t\) such that
\[
|E(B_t[X])|\le D_t|X|
\]
for every finite \(X\subseteq V(B_t)\). By the finite orientation criterion and compactness, \(B_t\) admits an orientation with maximum indegree at most \(D_t\).

For each \(v\in V(B_t)\), let \(N^-(v)\) be its set of in-neighbours. Define a graph \(\widehat B_t\) by
\[
V(\widehat B_t)=\{(v,A):v\in V(B_t),\ A\subseteq N^-(v)\}.
\]
There are at most \(2^{D_t}\) vertices over each \(v\). For an oriented edge \(u\to v\) of \(B_t\), put
\[
(u,A)(v,B)\in E(\widehat B_t)
\quad\Longleftrightarrow\quad
u\in B.
\]
There are no other edges.

## Proposition 3.1

Every countable \(K_t\)-minor-free graph is an induced subgraph of \(\widehat B_t\), and every finite \(n\)-vertex subgraph of \(\widehat B_t\) has a balanced separator of order \(O_t(\sqrt n)\).

### Proof

Let \(G\) be countable and \(K_t\)-minor-free, and let
\[
\phi:G\hookrightarrow B_t
\]
be a subgraph embedding. For \(x\in V(G)\), put
\[
A_x=\{\phi(y)\in N^-(\phi(x)):xy\in E(G)\}.
\]
Map
\[
x\longmapsto (\phi(x),A_x).
\]
If \(\phi(x)\to\phi(y)\), then the two selected vertices in \(\widehat B_t\) are adjacent exactly when \(\phi(x)\in A_y\), which is exactly when \(xy\in E(G)\). Thus this is an induced embedding.

The projection \((v,A)\mapsto v\) has fibres of order at most \(2^{D_t}\) and maps edges to edges of \(B_t\). Lemma 2.2 therefore gives the separator bound. ∎

This settles the following related existential question:

> There exists a countable induced-universal graph for the countable \(K_t\)-minor-free graphs whose finite \(n\)-vertex subgraphs have \(O_t(\sqrt n)\) balanced separators.

It does not settle the catalog problem, which concerns the particular \(U_t\). In particular, \(\widehat B_t\) need not retain the source construction’s additional exclusion of a subdivision of \(K_{\aleph_0}\).

# 4. A small improvement of the known bound for \(U_t\)

I use the standard quantitative form of the Plotkin–Rao–Smith theorem: there are absolute constants \(a,b\) such that, for integers \(\ell,h\ge1\), every \(n\)-vertex graph either

- contains \(K_h\) as a minor whose branch sets have radius at most \(a\ell\log n\), or
- has a balanced separator of order at most
  \[
  b\left(\frac n\ell+\ell h^2\log n\right).
  \]

Property (K4) for \(U_t\) says that, for some \(c_t\),
\[
\nabla_r(U_t)\le c_t(r+1).
\]
The same bound holds for every finite subgraph \(F\subseteq U_t\).

Set
\[
R=\lceil a\ell\log n\rceil,\qquad
h=\left\lceil 2c_t(R+1)+2\right\rceil.
\]
If \(F\) contained \(K_h\) as an \(R\)-shallow minor, then
\[
\frac{h-1}{2}\le \nabla_R(F)\le c_t(R+1),
\]
contrary to the choice of \(h\). Hence the separator alternative applies. Since
\[
h=O_t(\ell\log n),
\]
we obtain
\[
|S|
 =O_t\left(\frac n\ell+\ell^3(\log n)^3\right).
\]
Choosing
\[
\ell\asymp \frac{n^{1/4}}{(\log n)^{3/4}}
\]
gives:

## Proposition 4.1

Every finite \(n\)-vertex subgraph of \(U_t\) has a balanced separator of order
\[
O_t\!\left(n^{3/4}(\log n)^{3/4}\right).
\]

This only improves the logarithmic factor in the quoted \(O(n^{3/4}\log n)\) estimate.

# 5. The known properties do not imply \(O(\sqrt n)\) separators

The following construction shows why one must exploit more of the specific structure of \(U_t\).

Let \((X_N)\) be an infinite family of connected cubic edge-expanders: for some fixed \(\eta>0\),
\[
|\delta_{X_N}(A)|\ge \eta|A|
\qquad
\text{whenever }|A|\le N/2.
\]
Such a family exists by the standard probabilistic construction of bounded-degree expanders.

Put
\[
L_N=\left\lceil\frac{N}{\log_2N}\right\rceil,
\]
and let \(G_N\) be obtained from \(X_N\) by replacing every edge by a path of length \(L_N\). Finally let
\[
W=\bigsqcup_N G_N.
\]

## Proposition 5.1

The countable graph \(W\) has the following properties:

1. \(\Delta(W)\le3\);
2. \(\nabla_r(W)=O(r+1)\);
3. its strong coloring numbers satisfy
   \[
   \operatorname{scol}_r(W)=O(r+1);
   \]
4. \(W\) contains no subdivision of \(K_{\aleph_0}\);
5. the minimum balanced-separator order of \(G_N\) is \(\Theta(N)\), while
   \[
   |V(G_N)|=\Theta\left(\frac{N^2}{\log N}\right).
   \]

Consequently \(W\) has finite \(n\)-vertex subgraphs requiring separators of order
\[
\Theta(\sqrt{n\log n}),
\]
and hence \(W\) does not satisfy an \(O(\sqrt n)\) separator bound.

### Proof of the separator lower bound

Let \(S\subseteq V(G_N)\), with \(s=|S|\). Let

- \(Z=S\cap V(X_N)\);
- \(F\subseteq E(X_N)\) consist of base edges whose subdivided paths contain a vertex of \(S\) internally.

Then
\[
|Z|\le s,\qquad |F|\le s.
\]
In \(X_N-Z-F\), all but \(O_\eta(s)\) vertices lie in one component \(C\), provided \(s<c_\eta N\).

Indeed, if every component had at most \(N/2\) vertices, one could take a union \(A\) of components with
\[
N/4\le |A|\le N/2.
\]
All edges in \(\delta_{X_N}(A)\) would then either lie in \(F\) or be incident with \(Z\), so
\[
\eta N/4\le|\delta(A)|\le |F|+3|Z|\le4s,
\]
a contradiction for sufficiently small \(s/N\). Once the largest component \(C\) has more than \(N/2\) vertices, applying expansion to the union of the remaining components gives
\[
|V(X_N)\setminus(C\cup Z)|\le \frac{4s}{\eta}.
\]

Thus at least
\[
\frac32N-O_\eta(s)
\]
base edges have both endpoints in \(C\) and have intact subdivided paths. These paths all belong to one component of \(G_N-S\). For sufficiently small \(c_\eta\), if \(s<c_\eta N\), that component contains more than
\[
N(L_N-1)+\frac{2N}{3}
   =\frac23|V(G_N)|
\]
vertices. Therefore every balanced separator has order \(\Omega_\eta(N)\).

Conversely, deleting the \(N\) original vertices leaves disjoint open edge-paths, so the separator number is \(O(N)\).

Since
\[
|V(G_N)|
 =N+\frac32N(L_N-1)
 =\Theta\left(\frac{N^2}{\log N}\right),
\]
the asserted \(\Theta(\sqrt{n\log n})\) lower bound follows.

### Proof of linear expansion

The cyclomatic number of \(G_N\) is
\[
|E(X_N)|-|V(X_N)|+1=\frac N2+1.
\]
It does not increase under taking minors. Hence every simple minor \(J\) of \(G_N\), with \(q=|V(J)|\), satisfies
\[
|E(J)|\le q+\frac N2
\]
and also
\[
|E(J)|\le\binom q2.
\]
Therefore
\[
\frac{|E(J)|}{q}\le 1+\frac{\sqrt N}{2}.
\]

For an \(r\)-shallow minor with \(4r+1<L_N\), every branch set avoiding the original cubic vertices lies in one subdivided edge and has degree at most two in the minor. Branch sets meeting original vertices are pairwise nonadjacent, since two such adjacent branch sets would give a path of length at most \(4r+1\) between distinct original vertices. Thus such a shallow minor is \(2\)-degenerate.

If \(4r+1\ge L_N\), then, for large \(N\),
\[
\sqrt N\le L_N\le4r+1,
\]
and the preceding cyclomatic-number estimate is \(O(r+1)\). This proves
\[
\nabla_r(W)=O(r+1).
\]

### Proof of linear strong coloring numbers

In each \(G_N\), order all original cubic vertices before all subdivision vertices.

For a subdivision vertex \(v\), a strongly reachable path cannot pass through an original vertex internally, since every original vertex precedes \(v\). Hence the path remains on one subdivided base edge, except possibly for its endpoint. Thus \(v\) strongly \(r\)-reaches at most \(2r+3\) vertices.

For an original vertex \(v\), every earlier reachable vertex is original. If it is reached by a path of length at most \(r\), then it lies within distance
\[
k=\left\lfloor\frac r{L_N}\right\rfloor
\]
of \(v\) in \(X_N\). A cubic ball of radius \(k\) has at most \(3\cdot2^k\) vertices, and of course at most \(N\) vertices. Writing \(a=\log_2N\), one has uniformly for \(k\ge1\)
\[
\min\{N,3\cdot2^k\}=O\left(\frac{kN}{a}\right)
 =O(kL_N)
 =O(r).
\]
Thus \(\operatorname{scol}_r(G_N)=O(r+1)\), with a constant independent of \(N\), and the same holds for their disjoint union.

Finally, \(W\) has maximum degree three and finite connected components, so it cannot contain a subdivision of \(K_{\aleph_0}\). ∎

# 6. Relation of the obstruction to \(U_t\)

For \(t\ge5\), \(U_t\) contains every countable planar graph and therefore, by the source paper’s lower theorem, contains \(K_{\aleph_0}\) as a minor. Consequently it contains every finite cubic graph as a minor. Since a subcubic graph is a minor of a graph if and only if some subdivision of it occurs as a subgraph, \(U_t\) necessarily contains a subdivision of every finite cubic expander.

This observation alone does not disprove (K2). The resulting subdivisions may be extremely large or have their subdivided-edge lengths concentrated on a small number of edges; in either situation their uniformly weighted balanced separators can be much smaller relative to their number of vertices. A counterexample would follow, for example, from finding in \(U_t\) uniformly or suitably well-distributed subdivisions of cubic expanders on \(N\) branch vertices, using \(o(N^2)\) vertices in total.

Thus a concrete remaining question is:

> Does the specific construction of \(U_t\) force every well-distributed cubic-expander subdivision on \(N\) branch vertices to use \(\Omega_t(N^2)\) vertices?

The established linear expansion and linear coloring-number bounds do not answer this, as Proposition 5.1 demonstrates.

# 7. Gap

No bounded-fibre edge-respecting projection from the actual \(U_t\) to the source’s product-universal graph is established; if such a projection existed, Lemma 2.2 would prove the conjecture immediately. Conversely, I have not located controlled expander subdivisions inside \(U_t\). Therefore the graph-specific \(O_t(\sqrt n)\) separator problem remains open.