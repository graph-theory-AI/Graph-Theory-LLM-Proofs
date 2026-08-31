```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but an atomwise bounded clique-cover transversal of the induced pyramids gives an explicit constant bound, and a natural unbounded family containing many pyramids has tree-α exactly 2.",
  "would_publish": false,
  "caveats": "The argument uses the source theorem as a black box and does not bound the transversal parameter for arbitrary atoms."
}
```

# 1. Statement and notation

For a tree decomposition \(\mathcal T=(T,(B_t)_{t\in V(T)})\) of \(G\), put
\[
\alpha(\mathcal T)=\max_{t\in V(T)}\alpha(G[B_t]),
\qquad
\operatorname{tree}\alpha(G)=\min_{\mathcal T}\alpha(\mathcal T).
\]

The conjecture asks whether there is an absolute constant \(c\) such that
\[
\operatorname{tree}\alpha(G)\le c
\]
for every graph \(G\) containing neither an induced even hole nor an induced diamond.

I do not prove this and do not have a counterexample. I prove a parameterized extension of the source theorem that covers graphs with controlled systems of pyramids, together with an exact pyramid-containing special case.

Let \(c_0\) denote a universal constant supplied by the source theorem:
\[
\tag{\(*\)}
\operatorname{tree}\alpha(H)\le c_0
\quad\text{for every (even-hole, diamond, pyramid)-free graph }H.
\]

The numerical value of \(c_0\) is immaterial below.

# 2. Two useful formulations of tree-\(\alpha\)

## 2.1 Chordal-completion formulation

For every graph \(G\),
\[
\tag{1}
\operatorname{tree}\alpha(G)
=
\min_{\substack{H\supseteq G\\ H\text{ chordal}}}
\ \max_{Q\in\mathcal K(H)}\alpha(G[Q]),
\]
where \(\mathcal K(H)\) denotes the maximal cliques of \(H\).

Indeed, given a tree decomposition of \(G\), associate with each vertex \(v\) its occurrence subtree \(T_v\). Join two vertices whenever their subtrees intersect. The resulting graph \(H\) is chordal and contains \(G\). By the Helly property for subtrees of a tree, every clique of \(H\) is contained in a bag.

Conversely, the maximal cliques of a chordal supergraph \(H\) admit a clique-tree decomposition. This is also a tree decomposition of \(G\), and its bag independence numbers are measured in \(G\).

In particular,
\[
\operatorname{tree}\alpha(G)=1
\quad\Longleftrightarrow\quad
G\text{ is chordal}.
\]

## 2.2 Clique-cover width in diamond-free graphs

For \(X\subseteq V(G)\), let \(\theta_G(X)\) be the minimum number of cliques of \(G\) whose union contains \(X\). Define
\[
\operatorname{tree}\theta(G)
=
\min_{\mathcal T}\max_t\theta_G(B_t).
\]
Always
\[
\operatorname{tree}\alpha(G)\le \operatorname{tree}\theta(G).
\]

For diamond-free graphs the two parameters are qualitatively equivalent.

### Lemma 2.1

For every integer \(k\), there is a constant \(f(k)\) such that every diamond-free graph \(J\) with \(\alpha(J)\le k\) is the union of at most \(f(k)\) cliques.

#### Proof

Set \(f(1)=1\), and for \(k\ge2\) let
\[
f(k)=\max\{R(k+1,k+1)-1,\ f(k-1)+1\}.
\]

Let \(K\) be a maximum clique of \(J\).

If \(|K|\le k\), then \(J\) has neither a clique nor an independent set of size \(k+1\). Hence
\[
|V(J)|\le R(k+1,k+1)-1,
\]
and singleton cliques give the required cover.

Suppose \(|K|\ge k+1\). Every vertex \(x\notin K\) has at most one neighbor in \(K\). Otherwise, since \(K\) is maximal, \(x\) has two neighbors and a nonneighbor in \(K\), and those four vertices induce a diamond.

If \(J-K\) had an independent set \(I\) of size \(k\), at most \(k\) vertices of \(K\) would have a neighbor in \(I\). Since \(|K|\ge k+1\), some \(z\in K\) would be anticomplete to \(I\), giving an independent set \(I\cup\{z\}\) of size \(k+1\), a contradiction. Thus
\[
\alpha(J-K)\le k-1.
\]
Induction covers \(J-K\) with at most \(f(k-1)\) cliques, and adding \(K\) completes the proof. \(\square\)

Consequently, for diamond-free \(G\),
\[
\tag{2}
\operatorname{tree}\alpha(G)
\le \operatorname{tree}\theta(G)
\le f(\operatorname{tree}\alpha(G)).
\]
Thus the original conjecture is equivalently a bounded tree clique-cover-width assertion on this class.

# 3. A parameterized extension of the pyramid-free theorem

A set \(S\subseteq V(G)\) is a **pyramid transversal** if every induced pyramid of \(G\) contains a vertex of \(S\). Define its clique-cover cost by
\[
\rho(G)=\min\left\{
q:
\begin{array}{l}
\text{there are cliques }Q_1,\ldots,Q_q\text{ of }G,\\
S=\bigcup_{i=1}^qQ_i\text{ is a pyramid transversal}
\end{array}
\right\}.
\]
We set \(\rho(G)=0\) when \(G\) is pyramid-free.

The following elementary inequality is the key.

### Lemma 3.1

For every graph \(G\) and \(S\subseteq V(G)\),
\[
\tag{3}
\operatorname{tree}\alpha(G)
\le
\operatorname{tree}\alpha(G-S)+\alpha(G[S]).
\]

#### Proof

Take a tree decomposition of \(G-S\) and add every vertex of \(S\) to every bag. All edges incident with \(S\) are then covered, and the occurrence set of every vertex in \(S\) is the entire decomposition tree. In every new bag \(B\cup S\),
\[
\alpha(G[B\cup S])
\le \alpha((G-S)[B])+\alpha(G[S]).
\]
If \(G-S\) is empty, use the single bag \(S\). \(\square\)

Since a union of \(q\) cliques has independence number at most \(q\), Lemma 3.1 and \((*)\) immediately give:

### Proposition 3.2

If \(G\) is even-hole-free and diamond-free, then
\[
\tag{4}
\operatorname{tree}\alpha(G)\le c_0+\rho(G).
\]

#### Proof

Let \(S\) be a pyramid transversal covered by \(\rho(G)\) cliques. Then \(G-S\) is even-hole-free, diamond-free and pyramid-free. Hence
\[
\operatorname{tree}\alpha(G-S)\le c_0,
\qquad
\alpha(G[S])\le \rho(G),
\]
and (4) follows from Lemma 3.1. \(\square\)

The global parameter \(\rho(G)\) is too crude for disconnected or clique-separated collections of pyramids. It can be localized to clique-cutset atoms.

### Lemma 3.3: clique-sum gluing

Suppose
\[
G=G_1\cup G_2,\qquad V(G_1)\cap V(G_2)=K,
\]
where \(K\) is a clique and there are no edges between
\(V(G_1)\setminus K\) and \(V(G_2)\setminus K\). Then
\[
\operatorname{tree}\alpha(G)
=
\max\{\operatorname{tree}\alpha(G_1),
      \operatorname{tree}\alpha(G_2)\}.
\]

#### Proof

The lower bound follows by induced-subgraph monotonicity. For the upper bound, in every tree decomposition of \(G_i\), some bag contains all of \(K\): the occurrence subtrees of the vertices of \(K\) pairwise intersect and hence have a common node. Connect such a bag of the decomposition of \(G_1\) to such a bag of the decomposition of \(G_2\). No bag is enlarged. \(\square\)

Recursively decompose \(G\) along clique cutsets, and let \(\mathcal A\) be the resulting terminal blocks.

### Theorem 3.4

Let \(G\) be even-hole-free and diamond-free. For any recursive clique-cutset decomposition with terminal blocks \(\mathcal A\),
\[
\tag{5}
\operatorname{tree}\alpha(G)
\le
c_0+\max_{A\in\mathcal A}\rho(A).
\]

#### Proof

Proposition 3.2 gives
\[
\operatorname{tree}\alpha(A)\le c_0+\rho(A)
\]
for every terminal block \(A\). Repeated application of Lemma 3.3 glues their decompositions without increasing the largest bag independence number. \(\square\)

This gives several concrete special cases extending beyond pyramid-free graphs.

### Corollary 3.5

The target class has bounded tree-\(\alpha\) on each of the following subclasses:

1. in every clique-cutset atom, all induced pyramids share a common vertex;
2. in every atom, there is one clique meeting every induced pyramid;
3. in every atom, the base triangles of all induced pyramids lie in at most \(q\) prescribed maximal cliques;
4. in every atom, there are at most \(p\) pairwise vertex-disjoint triangles that occur as bases of induced pyramids.

The respective bounds are \(c_0+1,c_0+1,c_0+q,c_0+p\).

For the last assertion, choose a maximal family \(T_1,\ldots,T_r\) of pairwise disjoint pyramid-base triangles. Then \(r\le p\), and
\[
S=V(T_1)\cup\cdots\cup V(T_r)
\]
meets every other pyramid base, by maximality. Since each \(T_i\) is a clique,
\[
\alpha(G[S])\le r\le p.
\]

# 4. Structural restrictions on pyramids

Two elementary observations clarify why maximal cliques are natural objects here.

### Lemma 4.1

In a diamond-free graph, two distinct maximal cliques intersect in at most one vertex. Consequently, every triangle belongs to a unique maximal clique.

#### Proof

Suppose distinct maximal cliques \(K,L\) share vertices \(u,v\). Choose
\(x\in K\setminus L\) and \(y\in L\setminus K\). If \(xy\notin E(G)\), then
\(\{u,v,x,y\}\) induces a diamond. Hence every vertex of \(K\setminus L\) is complete to every vertex of \(L\setminus K\), and \(K\cup L\) is a clique, contradicting maximality. \(\square\)

Also, if \(K\) is a maximal clique with \(|K|\ge3\), every vertex outside \(K\) has at most one neighbor in \(K\).

### Lemma 4.2: parity of pyramid arms

Let \(P\) be an induced pyramid in an even-hole-free graph. If its three apex-to-base path lengths are
\(\ell_1,\ell_2,\ell_3\), then
\[
\ell_1\equiv\ell_2\equiv\ell_3\pmod 2.
\]

#### Proof

For every pair \(i\ne j\), the union of the \(i\)-th and \(j\)-th paths and the corresponding base edge is an induced cycle of length
\[
\ell_i+\ell_j+1.
\]
The pyramid definition allows at most one arm of length one, so these cycles have length at least four. They cannot be even, whence
\(\ell_i+\ell_j\) is even for every pair. \(\square\)

These restrictions do not by themselves produce a decomposition for arbitrary overlapping pyramids.

# 5. An exact pyramid-containing strip family

The following natural family illustrates that arbitrarily many pyramids can coexist while tree-\(\alpha\) remains exactly \(2\).

Let \(A,B\) be disjoint, anticomplete cliques, and let \(F\) be a simple bipartite graph with bipartition \((A,B)\). For every edge \(e=ab\in E(F)\), introduce a vertex \(x_e\) adjacent exactly to \(a\) and \(b\). Let all \(x_e\) be pairwise nonadjacent. Denote the resulting graph by \(G(F)\).

### Proposition 5.1

For every such \(F\):

1. \(G(F)\) is diamond-free;
2. \(\operatorname{tree}\alpha(G(F))\le2\);
3. \(G(F)\) is even-hole-free if and only if the matching number of \(F\) is at most one;
4. if \(|E(F)|\ge2\), then \(\operatorname{tree}\alpha(G(F))=2\);
5. if \(F\) is a star with at least three edges, then \(G(F)\) contains an induced pyramid.

#### Proof

Every triangle of \(G(F)\) lies wholly in \(A\) or wholly in \(B\), since each \(x_e\) has two nonadjacent neighbors. An induced diamond contains two triangles sharing an edge. Hence all four of its vertices would have to lie in \(A\) or all in \(B\), where they instead induce \(K_4\). Thus \(G(F)\) is diamond-free.

For the tree decomposition, use the central bag
\[
A\cup B
\]
and, for every \(e=ab\in E(F)\), a leaf bag
\[
\{a,b,x_e\}
\]
adjacent to the central bag. The running-intersection condition is immediate. The central bag is the union of two cliques and has independence number at most two. Each leaf induces the path \(a-x_e-b\), also of independence number two. Therefore
\[
\operatorname{tree}\alpha(G(F))\le2.
\]

If \(F\) has disjoint edges \(ab\) and \(a'b'\), then
\[
a,x_{ab},b,b',x_{a'b'},a'
\]
induce the \(6\)-cycle
\[
a-x_{ab}-b-b'-x_{a'b'}-a'-a.
\]
Thus \(G(F)\) is not even-hole-free.

Conversely, if \(F\) has no two disjoint edges, then all its edges share a common endpoint. Indeed, two distinct intersecting edges may be written \(ab_1,ab_2\); any edge meeting both must also contain \(a\). Thus \(F\) is a star.

Assume, by symmetry, that every edge of \(F\) contains \(a_0\in A\). Vertices of \(A\setminus\{a_0\}\) are simplicial and lie in no hole. Every cycle containing a vertex \(x_{a_0b}\) must contain both \(a_0\) and \(b\). Since a cycle uses only two edges at \(a_0\), any hole outside \(A\cup B\) contains exactly two subdivision vertices, say \(x_{a_0b_1},x_{a_0b_2}\). Its portion inside the clique \(B\) must be the single edge \(b_1b_2\), or it has a chord. Hence every hole is
\[
a_0-x_{a_0b_1}-b_1-b_2-x_{a_0b_2}-a_0,
\]
a \(5\)-hole. Thus \(G(F)\) is even-hole-free.

If \(F\) has at least two edges, the preceding pair of edges gives either an induced \(C_5\) or an induced \(C_6\). Hence \(G(F)\) is not chordal, so its tree-\(\alpha\) is not one. Together with the upper bound, it equals two.

Finally, if \(F\) is a star with center \(a_0\) and distinct edges \(a_0b_1,a_0b_2,a_0b_3\), then the three paths
\[
a_0-x_{a_0b_i}-b_i,\qquad i=1,2,3,
\]
together with the base triangle \(b_1b_2b_3\), induce a pyramid. \(\square\)

Taking a star with arbitrarily many leaves gives a target graph with \(\binom r3\) evident induced pyramids and tree-\(\alpha=2\). Thus merely counting pyramids, or even their base triangles, is not the right obstruction.

# 6. Exact finite search for the stronger bound \(2\)

Formula (1) gives a fully specified exhaustive test for
\(\operatorname{tree}\alpha(G)\le2\):

1. enumerate all subsets \(F\) of the nonedges of \(G\);
2. set \(H=(V(G),E(G)\cup F)\);
3. test whether \(H\) is chordal;
4. if it is, test whether any independent triple of \(G\) is a clique of \(H\).

Then
\[
\operatorname{tree}\alpha(G)\le2
\]
if and only if at least one fill set \(F\) passes both tests.

An exact search for a target graph with tree-\(\alpha\ge3\) on \(n\) vertices can therefore enumerate all labeled graphs and retain precisely those for which:

- no \(4\)-vertex set induces exactly five edges;
- no even-cardinality set \(S\), \(|S|\ge4\), induces a connected \(2\)-regular graph;
- every fill set fails the chordality/stable-triple test above.

This is exponential and I have not run it, so I make no small-order computational claim.

# 7. Remaining gap

Theorem 3.4 does not establish a universal bound on \(\rho(A)\) for clique-cutset atoms \(A\). More importantly, such a bound may be stronger than the original conjecture: a graph could admit local low-independence bags even though no bounded union of cliques meets all its pyramids.

Thus the unresolved case is a single clique-cutset atom containing a complicated, potentially widely distributed system of overlapping pyramids. The common parity of the arms and the uniqueness of each base maximal clique are useful restrictions, but the arguments above do not organize those maximal cliques into a bounded-width tree decomposition.

Accordingly, this is genuine partial progress only: no proof of the conjecture and no counterexample is obtained.