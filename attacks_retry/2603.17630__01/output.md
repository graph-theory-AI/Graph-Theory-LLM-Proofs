```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The sharp exponent holds when a bounded vertex set exposes linearly many bounded components, and fixed repeated-piece families have an exact computable polynomial-growth exponent.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved; constants depend on the fixed structural parameters, and novelty of these partial results has not been checked."
}
```

# 1. Results obtained

Write \(s(G)\) for the number of isomorphism classes of spanning trees of a finite simple graph \(G\). I interpret the conjecture asymptotically for each fixed \(d\).

The main partial result is the following.

## Theorem A
Fix integers \(d\ge 2\), \(k,B\ge 1\), and a real number \(\alpha>0\). There are constants \(c>0\) and \(n_0\), depending only on these parameters, such that the following holds.

Suppose \(G\) is connected, has \(n\ge n_0\) vertices and minimum degree at least \(d\), and has a set \(C\) with
\[
1\le |C|\le k
\]
such that
\[
\sum_{\substack{Q\text{ a component of }G-C\\ |V(Q)|\le B}}
|V(Q)|\ge \alpha n.
\]
Then
\[
s(G)\ge c n^{d-1}.
\]

In particular, the conjectured exponent holds whenever deleting a bounded number of vertices leaves components of bounded order. This extends both the bounded-vertex-cover and bounded-petal bouquet cases from the supplied attempt. It also permits an arbitrary large remainder, provided a positive proportion of the vertices lie in the bounded components.

A second result, proved in Section 5, gives the **exact polynomial-growth exponent** for any graph family formed from a fixed core and repeated copies of a fixed bounded piece.

The rooted-block argument suggested by the previous attempt is re-established below. The additional ingredients are:

* an affine-dimension lemma for pieces attached to **several** boundary vertices;
* an intrinsic way to control unrooted isomorphisms, without assuming that the boundary vertices remain individually identifiable.

# 2. A local affine-dimension lemma

Let \(W\) and \(S\) be disjoint finite vertex sets, with \(W\ne\varnothing\), \(S\ne\varnothing\). Consider a graph \(L\) on \(W\cup S\), where:

* \(L[W]\) is connected;
* every vertex of \(S\) has a neighbor in \(W\);
* edges within \(S\) are ignored.

An **admissible forest** is a spanning forest \(F\) of \(L\) in which every component contains exactly one vertex of \(S\).

For each component of \(F-S\), root it at its unique vertex adjacent in \(F\) to \(S\). Define the profile
\[
\beta(F)_{s,R}
\]
to be the number of these rooted branches of rooted-tree type \(R\) attached to \(s\in S\).

Only rooted trees of order at most \(b:=|W|\) occur. Thus the profiles lie in a finite-dimensional integer vector space. They satisfy
\[
\sum_{s,R}|V(R)|\,\beta(F)_{s,R}=b.
\]

## Lemma 1
If every \(w\in W\) has degree at least \(d\ge2\) in \(L\), then the affine dimension of the admissible profiles is at least \(d-1\).

### Proof

Identify all vertices of \(S\) to a single vertex \(r\). Keep parallel edges, recording their original endpoints in \(S\) as colors. This gives a multigraph \(M\), whose only possible parallel edges are incident with \(r\). Let \(\overline M\) be its underlying simple graph.

Spanning trees of \(M\), with these edge colors retained, correspond to admissible forests of \(L\): split \(r\) back into the vertices of \(S\).

We consider three cases.

### Case 1: \(|W|=1\)

The unique vertex of \(W\) has at least \(d\) distinct neighbors in \(S\). Attaching it to any one of those neighbors gives a different unit-vector profile. Hence the affine dimension is at least \(d-1\).

### Case 2: \(\overline M\) is 2-connected

We first find a neighbor \(v\) of \(r\) such that \(L[W]-v\) is connected.

If \(L[W]\) has no cutvertex, any neighbor of \(r\) works. Otherwise, take an end block \(Q\) of \(L[W]\), with its unique cutvertex \(x\). Since \(\overline M-x\) is connected, some vertex
\[
v\in V(Q)\setminus\{x\}
\]
is adjacent to \(r\). Such a vertex is not a cutvertex of \(L[W]\).

Put
\[
a=\deg_{L[W]}(v),\qquad t=|N_L(v)\cap S|.
\]
Then \(a,t\ge1\) and \(a+t\ge d\).

For every \(i\in\{1,\ldots,a\}\), there is a spanning tree \(U_i\) of \(L[W]\) with
\[
\deg_{U_i}(v)=i.
\]
Indeed, retain any \(i\) edges incident with \(v\), together with all edges of \(L[W]-v\). This graph is connected, and the retained \(i\)-edge star extends to a spanning tree of it.

For every pair
\[
i\in\{1,\ldots,a\},\qquad s\in N_L(v)\cap S,
\]
attach the whole tree \(U_i\) to \(s\) using \(sv\). Its profile is a unit vector indexed by \(s\) and the rooted tree \((U_i,v)\). These give \(at\) distinct unit vectors, since the root degrees distinguish the \(U_i\). Moreover,
\[
at\ge a+t-1\ge d-1.
\]

There is also a spanning tree of \(M\) in which \(r\) has degree at least two: extend two edges from \(r\) to distinct neighbors to a spanning tree. Every branch at \(r\) in this tree has fewer than \(b\) vertices.

Choose \(d-1\) of the unit profiles above. They are supported on distinct coordinates corresponding to branches of order \(b\), whereas the last profile is supported only on branches of smaller order. These \(d\) profiles are affinely independent.

### Case 3: \(\overline M\) has a cutvertex

Because \(\overline M-r=L[W]\) is connected, \(r\) is not a cutvertex. Choose an end block \(Q\) of \(\overline M\) not containing \(r\), and let \(x\) be its unique cutvertex.

Every vertex of \(Q-x\) has all its neighbors in \(Q\). In particular, it has degree at least \(d\) within \(Q\). Thus \(Q\) cannot be a bridge block, and it is 2-connected.

The argument in Case 2, applied to \(Q\) with the sole boundary vertex \(x\), gives \(d\) pairwise non-isomorphic \(x\)-rooted spanning trees of \(Q\).

The graph
\[
L\bigl[W\setminus(V(Q)\setminus\{x\})\bigr]
\]
is connected. Choose a fixed spanning tree of it and a fixed vertex \(w\) in it adjacent to some \(s\in S\). Grafting the \(d\) rooted trees of \(Q\) at \(x\) gives \(d\) distinct \(w\)-rooted spanning-tree types of \(L[W]\).

Here we use the following elementary cancellation fact:

> Grafting a variable rooted tree at a fixed vertex of a fixed rooted tree is injective on rooted isomorphism types.

To verify it, induct on the distance from the global root to the grafting vertex. At each step, equality of the multisets of rooted branches allows the common fixed branches to be cancelled.

Finally, attach each resulting spanning tree of \(L[W]\) to \(s\) using \(sw\). The resulting profiles are \(d\) distinct unit vectors. They are affinely independent. ∎

# 3. Turning local dimension into unrooted spanning-tree types

The following lemma handles the isomorphism issue.

## Lemma 2
Fix \(b,t\ge1\) and \(\eta>0\). Suppose a connected \(n\)-vertex graph \(G\) contains disjoint sets
\[
W_1,\ldots,W_m,\qquad |W_i|=b,\qquad m\ge\eta n,
\]
and a common boundary set \(S\), \(|S|=t\), such that:

1. all neighbors of \(W_i\) outside \(W_i\) lie in \(S\);
2. the graphs on \(W_i\cup S\), with \(S\) individually labelled, are copies of the same local graph \(L\);
3. \(L[W_i]\) is connected, and every vertex of \(S\) has a neighbor in each copy;
4. \(G-\bigcup_i W_i\) is connected.

If the admissible profiles of \(L\) contain \(\rho+1\) affinely independent vectors, then, for sufficiently large \(n\),
\[
s(G)=\Omega_{b,t,\eta,\rho}(n^\rho).
\]

### Proof

Choose admissible forests with affinely independent profiles
\[
\beta_0,\ldots,\beta_\rho.
\]

Set
\[
q=\left\lfloor\frac{m}{2t}\right\rfloor.
\]
For each \(s\in S\), reserve \(q\) copies. In each such copy, attach the entire connected piece as a single branch at \(s\). This is possible by taking a spanning tree inside the piece and one edge to \(s\).

Start with a fixed spanning tree of \(G-\bigcup_i W_i\), and add all these reserved copies. Denote the resulting tree by \(T_0\). Every \(s\in S\) now has degree at least \(q\).

There remain
\[
M=m-tq\ge m/2
\]
variable copies. For every weak composition
\[
c_0+\cdots+c_\rho=M,
\]
use the local forest with profile \(\beta_j\) in exactly \(c_j\) copies. Their union with \(T_0\) is a spanning tree \(T_{\mathbf c}\).

For sufficiently large \(n\),
\[
q>b+t-1
\quad\text{and}\quad
q>b.
\]
Every vertex in a variable piece has degree at most \(b+t-1\). Consequently the set
\[
H=\{v:\deg_{T_{\mathbf c}}(v)\ge q\}
\]
is independent of \(\mathbf c\): it contains \(S\), and outside \(S\) membership is fixed. Also,
\[
|H|q\le 2(n-1).
\]
Since \(q\ge m/(4t)\) for large \(m\),
\[
|H|\le \frac{8t}{\eta}.
\]

For \(v\in H\), let \(p_T(v)\) record the numbers of rooted branches at \(v\) having order at most \(b\).

A component of \(T_0-v\) containing a vertex \(s\in S\setminus\{v\}\) has at least \(q>b\) vertices: it contains \(s\) and all but at most one of its neighbors in \(T_0\). Therefore adding the variable copies cannot change whether such a component contributes to the small-branch profile.

It follows that there are fixed vectors \(\gamma_v\) such that
\[
p_{T_{\mathbf c}}(v)
=
\gamma_v+\sum_{j=0}^{\rho}c_j\beta_j(v),
\]
where \(\beta_j(v)=0\) for \(v\notin S\), and for \(v\in S\) it denotes the corresponding row of the local profile.

Because the \(\beta_j\) are affinely independent and \(\sum_jc_j=M\), the ordered tuple
\[
\bigl(p_{T_{\mathbf c}}(v):v\in H\bigr)
\]
determines \(\mathbf c\).

An unrooted isomorphism preserves the degree threshold defining \(H\), and hence permutes its vertices. Thus an unrooted isomorphism class accounts for at most \(|H|!\) of these distinct ordered tuples. Therefore
\[
s(G)\ge
\frac{1}{|H|!}\binom{M+\rho}{\rho}.
\]
Since \(|H|\) is bounded and \(M\ge\eta n/2\), this is \(\Omega(n^\rho)\). ∎

The use of high degrees here is only to make the **set** \(H\) intrinsic. Individual boundary vertices need not be identifiable.

# 4. Proof of Theorem A

Let \(C\) be as in the theorem.

First retain at most \(|C|-1\) components of \(G-C\) so that their union with \(C\) induces a connected graph. To see this, start with the components of \(G[C]\). Whenever there is more than one, connectivity of \(G\) provides a component of \(G-C\) adjacent to at least two current components; adding it reduces their number. At most \(|C|-1\) additions are needed.

Call the resulting connected graph the backbone. Every other component of \(G-C\) has a neighbor in \(C\), so removing any selection of those other components leaves a connected graph.

There are at least
\[
\frac{\alpha n}{B}-(k-1)
\]
unretained components of order at most \(B\).

A component type is determined by its internal graph and its neighborhood incidence with the individually labelled vertices of \(C\). The number of possible types is at most
\[
R=\sum_{b=1}^{B}2^{\binom b2+kb}.
\]
Thus, for sufficiently large \(n\), some type occurs in at least
\[
m\ge \frac{\alpha n}{2BR}
\]
unretained components.

Let \(S\subseteq C\) be the set of boundary vertices used by this type. It is nonempty. Every vertex of such a component has all its graph neighbors inside the component or in \(S\), so its degree in the local graph is at least \(d\).

Lemma 1 provides \(d\) affinely independent local profiles. Lemma 2, with
\[
\rho=d-1,\qquad \eta=\frac{\alpha}{2BR},
\]
then gives
\[
s(G)=\Omega_{d,k,B,\alpha}(n^{d-1}).
\]
All constants are uniform over the finitely many possible local types. This proves Theorem A. ∎

# 5. Exact growth for fixed repeated-piece families

The same framework gives more than a lower bound for a natural class of families.

Fix:

* a core \(C\) of order \(k\), with any fixed graph on it;
* a connected piece \(W\) of order \(b\);
* fixed edges between \(W\) and \(C\).

Let \(G_m\) consist of the core and \(m\) copies of \(W\), with the prescribed incidence to \(C\) and no edges between distinct copies. Assume \(G_1\) is connected.

Let \(\mathcal A\) be the set of admissible profiles of one piece, with \(C\) as the boundary; unused boundary vertices are allowed as isolated roots. Put
\[
\rho=\dim_{\mathrm{aff}}\mathcal A.
\]

## Theorem B
For this fixed family,
\[
s(G_m)=\Theta_{C,W}(m^\rho).
\]
If every non-core vertex has degree at least \(d\ge2\), then
\[
\rho\ge d-1.
\]

Thus the polynomial-growth exponent is an explicitly finite, computable affine rank.

### Proof: lower bound

Retain one copy together with the core as a connected backbone. The remaining \(m-1\) pieces satisfy Lemma 2 and constitute a linear proportion of the vertices. Using \(\rho+1\) affinely independent profiles gives
\[
s(G_m)=\Omega(m^\rho).
\]

The assertion \(\rho\ge d-1\) is Lemma 1, after omitting unused boundary coordinates.

### Proof: upper bound

Let \(T\) be any spanning tree of \(G_m\). For the \(i\)-th piece, let \(F_i\) consist of the edges of \(T\) internal to that piece or joining it to \(C\), regarded as a forest on \(W_i\cup C\).

Every component of \(F_i\) contains at least one core vertex. Otherwise it would be disconnected from the rest of \(T\).

If \(F_i\) has \(c_i\) components, write
\[
\mu_i=k-c_i\ge0.
\]
Then
\[
|E(F_i)|=b+k-c_i=b+\mu_i.
\]
Partitioning the edges of \(T\) according to the pieces and the core gives
\[
\sum_{i=1}^{m}\mu_i+|E(T[C])|=k-1.
\]

Consequently, at most \(k-1\) pieces have \(\mu_i>0\). Call these exceptional pieces. All other pieces have \(\mu_i=0\), so each of their local components contains exactly one core vertex: they are admissible forests.

The core together with the exceptional pieces has at most
\[
k+(k-1)b
\]
vertices. There are therefore only finitely many possibilities for its abstract tree structure with the vertices of \(C\) marked.

Once this bounded structure is fixed, the rest of \(T\) is completely determined by the aggregate profile of the ordinary pieces. Grouping branches according to their original pieces is irrelevant to the resulting abstract tree.

If there are \(\ell\le k-1\) exceptional pieces, the aggregate profile belongs to
\[
\underbrace{\mathcal A+\cdots+\mathcal A}_{m-\ell\text{ summands}}.
\]
Let \(V\) be the linear space spanned by differences of elements of \(\mathcal A\), so \(\dim V=\rho\). Choose a projection onto \(\rho\) coordinates that is injective on \(V\). It is then injective on the affine space containing these sums.

Each projected coordinate is an integer between \(0\) and \(bm\). Hence the number of aggregate profiles is at most
\[
(bm+1)^\rho.
\]
There are only finitely many bounded structures and possible values of \(\ell\). Thus
\[
s(G_m)=O(m^\rho).
\]
Together with the lower bound, this proves the theorem. ∎

This is a growth classification, not a claim that \(s(G_m)\) is literally a polynomial in \(m\).

# 6. Examples and sharper special-case counts

## 6.1. The proposed extremal family

For \(K_{d,N}\), take the part of order \(d\) as the core and each vertex of the other part as a one-vertex piece.

The local profiles are precisely
\[
e_1,\ldots,e_d.
\]
Their affine dimension is \(d-1\). Theorem B therefore gives
\[
s(K_{d,N})=\Theta_d(N^{d-1}).
\]

This reobtains the proposed extremal order, now as one instance of the profile-rank classification.

## 6.2. Cliques attached to a fixed clique

Let
\[
G_m=K_k\vee(mK_b),
\]
where \(mK_b\) is a disjoint union of \(m\) copies of \(K_b\), and the join adds all edges from the core \(K_k\) to every piece.

Let \(R_b\) be the number of rooted-tree isomorphism types having between \(1\) and \(b\) vertices, inclusive. Then
\[
s(G_m)=\Theta_{k,b}\bigl(m^{\,kR_b-1}\bigr).
\]

To verify the exponent, use one coordinate for every pair consisting of a core vertex and a rooted tree of order at most \(b\). There are \(kR_b\) coordinates. Since the piece is complete and has complete adjacency to the core, its admissible profiles are exactly the nonnegative integer vectors satisfying
\[
\sum_{\gamma} w_\gamma x_\gamma=b,
\]
where \(w_\gamma\) is the order of the rooted tree indexed by \(\gamma\).

Their affine dimension is \(kR_b-1\). Indeed, choose a reference coordinate \(\gamma_0\) corresponding to a singleton branch. The admissible profiles
\[
b e_{\gamma_0}
\quad\text{and}\quad
e_\gamma+(b-w_\gamma)e_{\gamma_0}
\qquad(\gamma\ne\gamma_0)
\]
have linearly independent difference vectors
\[
e_\gamma-w_\gamma e_{\gamma_0}.
\]

Since \(R_2=2\), taking \(k=d-1\) and \(b=2\) gives the explicit sharp count
\[
s\bigl(K_{d-1}\vee(mK_2)\bigr)
=\Theta_d(m^{2d-3}).
\]
These graphs have minimum degree \(d\). For \(d\ge3\), they are 2-connected and have unbounded vertex-cover number, so this example lies outside both the bounded-vertex-cover and cutvertex-bouquet arguments in the supplied attempt.

As another consequence, a bouquet of \(m\) copies of \(K_{d+1}\) meeting at one vertex has
\[
\Theta_d(m^{R_d-1})
\]
spanning-tree types. Thus these highly symmetric clique bouquets generally have a substantially larger exponent than \(d-1\).

# 7. Remaining gap

These results do **not** prove the unrestricted conjecture.

The missing step is structural: minimum degree at least \(d\) does not supply a bounded separator exposing a linear number of bounded pieces. Lemma 1 guarantees \(d-1\) independent local parameters, but Lemma 2 needs linearly many opportunities to repeat them.

In particular, the argument gives no sharp bound for a large graph in which every bounded vertex deletion leaves all but \(o(n)\) vertices in components whose orders grow with \(n\). Inside such a large piece, the local affine-dimension statement alone supplies only finitely many states, not \(n^{d-1}\) abstract tree shapes.

Accordingly, the general claim remains unresolved here. The established progress is the sharp lower bound in Theorem A and the exact, computable growth exponent in Theorem B.