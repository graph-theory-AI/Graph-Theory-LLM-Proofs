```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an exact characterization for planar transposition graphs and determine t(8)=16, extending the verified exact values through k=8.",
  "would_publish": false,
  "caveats": "The general function remains undetermined here for k≥9; novelty and subsequent literature status have not been checked."
}
```

# 1. Results

Associate the transposition \((ij)\) with the edge \(ij\). Call a simple graph **product-one-free** if no nonempty set of its edges can be ordered so that the corresponding transpositions multiply to the identity.

I prove the following partial results.

**Theorem A — planar characterization.**  
A planar graph \(G\) is product-one-free if and only if
\[
e_G(U)\le 2|U|-3
\qquad\text{for every }U\subseteq V(G),\quad |U|\ge2.
\]
Consequently, the maximum number of edges in a product-one-free planar graph on \(k\ge2\) vertices is exactly \(2k-3\).

**Theorem B — small values.**
\[
\boxed{
t(2)=2,\quad t(3)=4,\quad t(4)=6,\quad
t(5)=8,\quad t(6)=11,\quad t(7)=14,\quad t(8)=16.
}
\]

The case \(k=8\), and the sufficiency direction of the planar characterization, go beyond the supplied attempt. I verify the structural observation used from that attempt below. No computational results are assumed.

As usual,
\[
t(k)=1+\max\{e(G):G\text{ is product-one-free on }k\text{ vertices}\}.
\]
For \(k=2,3\), the resulting thresholds exceed the number of available transpositions, so the universal statement at the threshold is vacuous.

---

# 2. The edge-order embedding

We first establish the necessary condition underlying the argument.

## Lemma 2.1
Let an ordering of the edges of a connected graph \(H\) give a product \(\pi\) of the corresponding transpositions. There is an orientable cellular embedding of \(H\) having \(c(\pi)\) faces, where \(c(\pi)\) counts cycles on the support vertices of \(H\).

### Proof
Give every vertex the cyclic ordering of its incident edges induced by the global edge ordering. This is an orientable rotation system.

At each vertex put a mark between its last and first incident edges. Trace a face beginning at the mark at a vertex \(x\). Until the next mark, its edge labels increase strictly: after traversing an edge, take the next incident edge in the cyclic ordering at the new vertex, stopping if that step passes the mark.

This is precisely the trajectory of a token initially at \(x\) when the edge transpositions are performed in their prescribed order. Thus the next mark is at \(\pi(x)\), using the convention that permutations act on the right. Every face contains a mark, since a mark-free traversal would have strictly increasing edge labels indefinitely.

The cyclic sequences of marks on the faces are therefore exactly the cycles of \(\pi\). Capping the boundary components gives the asserted embedding. ∎

## Corollary 2.2
If a connected graph with \(v\) vertices and \(m\) edges supports an identity ordering, then
\[
m=2v-2+2g
\]
for some integer \(g\ge0\). In particular,
\[
m\ge2v-2,
\]
and equality implies planarity.

### Proof
There are \(v\) faces in Lemma 2.1. Euler's formula gives
\[
v-m+v=2-2g.
\]
∎

A product supported on disconnected components is the identity only if its restriction to each component is the identity. Hence it suffices throughout to consider connected nonempty identity supports.

We will also use a stronger bound for bipartite supports.

## Corollary 2.3
A connected simple bipartite graph supporting an identity ordering satisfies
\[
m\ge2v.
\]

### Proof
Such a support has no vertex of degree one: a position participating in just one transposition cannot return to its original token. Thus its minimum degree is at least two.

In the embedding from Lemma 2.1, every facial walk is nonbacktracking. A nonbacktracking closed walk in a simple bipartite graph has length at least four. There are \(v\) faces, so
\[
2m\ge4v.
\]
∎

---

# 3. A sufficient condition in the plane

The important additional fact is that the minimum-length obstruction is sufficient in the planar setting.

## Proposition 3.1
Let \(H\) be a connected plane graph with
\[
e(H)=2|V(H)|-2
\]
and
\[
e_H(U)\le2|U|-2
\qquad\text{for every nonempty }U\subseteq V(H).
\]
Then all edges of \(H\) can be ordered to give the identity.

### Proof

Write \(n=|V(H)|\). Euler's formula gives exactly \(n\) faces.

### Step 1: a strict Hall condition in the radial graph

Let \(R\) be the bipartite radial multigraph of the embedding. Its two vertex classes are
\[
V(H)\quad\text{and}\quad F(H),
\]
and each corner gives an edge between its vertex and its face.

I claim that
\[
|N_R(S)|\ge |S|+1
\qquad
(\varnothing\ne S\subsetneq V(H)).
\tag{3.1}
\]

Put \(W=V(H)\setminus S\). A face not adjacent to \(S\) has its entire boundary in \(H[W]\). Let \(q(W)\) be the number of such faces.

The boundary vectors of any proper subset of the faces of a connected plane graph are linearly independent over \(\mathbb F_2\). For completeness, a dependence would select a nonempty proper set of faces whose boundary sum is zero; no dual edge could cross from that set to its complement, contradicting connectivity of the plane dual.

The faces counted by \(q(W)\) form a proper subset of all faces, and their boundary vectors lie in the cycle space of \(H[W]\). Therefore
\[
q(W)\le e_H(W)-|W|+c(H[W]).
\]
Applying the sparsity assumption separately to the components of \(H[W]\) gives
\[
e_H(W)-|W|+c(H[W])
\le |W|-c(H[W])
\le |W|-1.
\]
Consequently,
\[
|N_R(S)|=n-q(W)\ge n-|W|+1=|S|+1,
\]
proving (3.1).

Hall's theorem now supplies a perfect matching \(M\) of \(R\).

### Step 2: the matching breaks all directed medial cycles

Construct the directed medial graph \(D\). Its vertices are the edges of \(H\). At each original vertex, put a directed cycle through its incident edges in their clockwise cyclic order.

The faces of this medial embedding are naturally indexed by \(V(H)\cup F(H)\). Orienting dual edges consistently identifies the directed dual with \(R\), all of whose edges point from the \(V(H)\)-class to the \(F(H)\)-class.

Contract the edges of \(M\) in this directed radial graph. The resulting digraph is strongly connected. Indeed, a nonempty proper set of contracted vertices with no outgoing edge would correspond to a vertex set \(S\subset V(H)\) whose face-neighbours were contained in its \(|S|\) matched faces, contradicting (3.1).

Let \(A\) be the set of medial arcs dual to \(M\). I claim that \(D-A\) is acyclic. Otherwise, a simple directed cycle in \(D-A\) would, by the Jordan curve theorem, determine a directed cut in the dual missing \(M\). Contracting \(M\) would preserve that directed cut, contradicting strong connectivity.

### Step 3: recover a global edge order

At every vertex of \(H\), exactly one arc of its directed medial cycle belongs to \(A\). Thus \(D-A\) contains a directed path specifying the entire cyclic order of the edges at that vertex, with one break.

Take a topological ordering of \(D-A\). This orders \(E(H)\) globally and induces the original rotation at every vertex. By Lemma 2.1, the product has as many cycles as the embedding has faces, namely \(n\). Hence the product is the identity. ∎

## Proof of Theorem A

If \(G\) has an identity subset, take a connected nonempty component of its support. Corollary 2.2 shows that its vertex set \(U\) satisfies
\[
e_G(U)\ge2|U|-2.
\]

Conversely, suppose a planar graph has a set \(U\), \(|U|\ge2\), with
\[
e_G(U)\ge2|U|-2.
\]
Choose such a vertex set \(U\) inclusion-minimally, and retain exactly \(2|U|-2\) edges of \(G[U]\), obtaining \(H\). Every proper vertex subset of size at least two spans at most \(2|W|-3\) edges. Thus \(H\) satisfies the sparsity assumption of Proposition 3.1. It is connected, since otherwise summing the sparsity bounds over components would give fewer than \(2|U|-2\) edges. Proposition 3.1 supplies an identity ordering.

Finally, the graph consisting of two adjacent vertices joined to all the other \(k-2\) vertices is planar, has \(2k-3\) edges, and satisfies the displayed sparsity condition in Theorem A. This proves the extremal assertion. ∎

In particular, we may repeatedly use:

> **Planar certificate.** A planar graph on \(v\ge2\) vertices with at least \(2v-2\) edges contains an identity subset.

---

# 4. Explicit identity certificates

The proof for eight vertices uses a short library of certificates. Their verification is included to make the subsequent finite case analysis self-contained.

## 4.1. A seven-vertex certificate

Let \(T_7\) consist of a disjoint triangle and \(4\)-cycle, together with two independent joining edges. Their endpoints on the \(4\)-cycle are adjacent. Let
\[
R_7=\overline{T_7}.
\]
Then \(R_7\) has twelve edges and supports an identity ordering.

To verify this, work on \(\mathbb Z_7\). Define
\[
r_i(x)=2i-x.
\]
The transpositions making up \(r_i\) form a matching \(M_i\), and these seven matchings partition \(E(K_7)\). Moreover,
\[
r_3r_4r_6r_5=1.
\]
Thus \(M_3\cup M_4\cup M_5\cup M_6\) is an identity support.

Its complement is
\[
\begin{aligned}
M_0\cup M_1\cup M_2
=\{&16,25,34,\;02,36,45,\;04,13,56\}.
\end{aligned}
\]
This is the triangle \(1\,3\,6\,1\), the \(4\)-cycle \(0\,2\,5\,4\,0\), and the joining edges \(34,65\), so it is \(T_7\).

Notice also that \(T_7\) contains both a spanning \(C_3\cup C_4\) and a spanning \(C_7\). For the latter, remove the edge between the two joining-edge endpoints in each of the triangle and the \(4\)-cycle, and use the two joining edges.

## 4.2. Three six-vertex planar certificates

Each of
\[
\overline{P_6},\qquad
\overline{C_4\cup K_2},\qquad
\overline{C_5\cup K_1}
\tag{4.1}
\]
is planar and has ten edges. Hence each contains an identity subset.

Here are explicit planarity descriptions.

* \(\overline{C_5\cup K_1}\) is a wheel.
* \(\overline{C_4\cup K_2}\) is \(K_{2,4}\) with a matching added among its four degree-two vertices. Draw the four length-two paths cyclically, pairing consecutive paths for the added edges.
* For \(\overline{P_6}\), start with a plane \(K_4\), subdivide two opposite edges, and join each subdivision vertex to an endpoint of the other subdivided edge, putting the two new edges in distinct faces. This gives \(\overline{P_6}\).

We will also use a \(4\)-cycle with two nonadjacent additional vertices, each joined to three cycle vertices. It is planar—put one new vertex inside and the other outside the cycle—and has ten edges.

## 4.3. Four certificates obtained from \(K_{4,4}\)

The following sixteen-edge graphs all support identity orderings. In the descriptions, letters in \(A\) and \(B\) belong to the two parts of \(K_{4,4}\).

1. \(K_{4,4}\).
2. \(K_{4,4}-ax+e\), where \(e\) is **any** edge inside either part.
3. \(K_{4,4}-ax-by+ab+xy\), where \(a\ne b\) and \(x\ne y\).
4. \(K_{4,4}-ax-ay+ap+xy\), where \(a\ne p\) and \(x\ne y\).

Here and below, a displayed graph difference deletes the named edges and then adds the named edges.

### Verification

Index both parts by \(\mathbb F_2^2\):
\[
A=\{A_z:z\in\mathbb F_2^2\},\qquad
B=\{B_z:z\in\mathbb F_2^2\}.
\]
For \(d\in\mathbb F_2^2\), let
\[
M_d=\prod_z(A_z\,B_{z+d}).
\]
These are commuting involutions, their edge sets partition \(K_{4,4}\), and
\[
\prod_{d\in\mathbb F_2^2}M_d=1.
\tag{4.2}
\]

For item 2, delete \(A_0B_0\) from the first matching \(M_0\). The remaining fifteen-edge word \(Q\) has product \((A_0\,B_0)\). Cyclically moving a prefix to the end conjugates this transposition, moving its endpoints by that prefix.

Choose distinct nonzero \(u,v\), and put \(w=u+v\).

* During \(M_u\), perform \(A_0B_u\) before \(A_uB_0\). At that intermediate point the conjugated transposition has endpoints \(B_0,B_u\).
* After all of \(M_u\), its endpoints are \(B_u,A_u\). During \(M_v\), perform \(A_uB_w\) before \(A_wB_u\). The endpoints then become \(B_u,B_w\).

These give every type of internal edge of \(B\), either incident or nonincident to \(B_0\); symmetry gives the same conclusion in \(A\). Append that internal transposition to the cyclically shifted word.

Items 3 and 4 follow from the identities
\[
(ax)(by)(bx)=(bx)(ab)(xy),
\tag{4.3}
\]
and
\[
(ax)(ay)(px)=(xy)(px)(ap).
\tag{4.4}
\]
For (4.3), put \(ax,by\) last in one matching of (4.2) and \(bx\) first in the next. For (4.4), put \(ax\) last in one matching and \(ay,px\) first in the next. The indexing can be chosen to make these the requisite matching edges. Replacing the indicated three-factor segment gives exactly the asserted graph. ∎

## 4.4. \(K_{3,5}\) plus an internal edge

**Lemma 4.1.** Adding any edge inside either part of \(K_{3,5}\) gives an identity support.

### Proof
Use labels
\[
A_0,A_1,A_2,\quad B_0,B_1,B_2,\quad C_1,C_2,
\]
with subscripts interpreted modulo three. Define
\[
R_j=\prod_{i=0}^2(A_i\,B_{i+j}),
\]
and
\[
S_j=\prod_{\substack{i\in\mathbb Z_3\\i+j\ne0}}
(A_i\,C_{i+j}).
\]
The word
\[
Q=R_0S_0R_1S_2R_2S_1
\tag{4.5}
\]
uses every edge of \(K_{3,5}\) exactly once. Directly following the eight labels gives
\[
Q=(A_2\,B_0):
\]
\(A_2\) and \(B_0\) are exchanged, and all other labels are fixed.

Order the commuting factors of \(R_0\) so that \((A_0B_0)\) is first. Moving this first factor to the end conjugates \(Q\) to \((A_0A_2)\). Alternatively, put \((A_2B_2)\) first; the corresponding cyclic shift has product \((B_0B_2)\).

Appending the resulting transposition gives an identity. Relabeling within the two parts covers every internal edge. ∎

---

# 5. Exact values through seven vertices

These values were asserted in the supplied attempt; the following gives an independently checked route to them.

A nonempty connected identity support has at least four vertices. On four vertices it must be \(K_4\), by Corollary 2.2.

## \(k=2,3,4\)

Two distinct transpositions cannot multiply to the identity, and an identity word has even length. Thus the full sets in \(S_2,S_3\) are product-one-free.

For \(k=4\), \(K_4-e\) is product-one-free, while
\[
((12)(34))((13)(24))((14)(23))=1.
\]
Therefore
\[
t(2)=2,\qquad t(3)=4,\qquad t(4)=6.
\]

## \(k=5\)

The graph \(K_{2,3}\) plus the edge inside its two-vertex part has seven edges, no \(K_4\), and too few edges for an identity support on five vertices.

An eight-edge graph on five vertices has two missing edges. If these meet, the graph contains \(K_4\). If they are disjoint, the graph is a wheel with four rim vertices, hence planar with eight edges and so has an identity subset. Thus
\[
t(5)=8.
\]

## \(k=6\)

The graph \(K_{3,3}+e\), with \(e\) internal to one part, has ten edges and is product-one-free. Supports on at most five vertices have too few edges. A support on all six vertices would have to use all ten edges and be planar, whereas the graph contains \(K_{3,3}\).

Every eleven-edge graph on six vertices has a vertex of degree at most three. Deleting it leaves at least eight edges on five vertices. Hence
\[
t(6)=11.
\]

## \(k=7\)

The graph \(K_{3,4}+e\), with \(e\) inside the three-vertex part, is product-one-free and has thirteen edges.

Indeed, supports on at most five vertices have too few edges. A six-vertex identity support would have to be \(K_{3,3}+e\) with ten edges, which is nonplanar. A seven-vertex support would have twelve edges; every such subgraph still contains \(K_{3,3}\), whereas Corollary 2.2 requires planarity.

Now let \(G\) have fourteen edges on seven vertices. A vertex of degree at most three reduces the problem to \(k=6\). Otherwise \(G\) is \(4\)-regular, and its complement is either \(C_7\) or \(C_3\cup C_4\). Both are spanning subgraphs of \(T_7\), so \(G\) contains \(R_7\). Thus
\[
t(7)=14.
\]

---

# 6. The eight-vertex lower bound

The graph \(K_{3,5}\) is product-one-free.

A connected subgraph using \(a\le3\) vertices in one part and \(b\le5\) in the other has
\[
m\le ab<2(a+b).
\]
This contradicts Corollary 2.3 if it were an identity support. Consequently,
\[
t(8)\ge16.
\tag{6.1}
\]

We now prove the matching upper bound. The proof is a finite structural classification, not a computational enumeration.

---

# 7. Every sixteen-edge graph on eight vertices has an identity subset

Suppose, for a contradiction, that \(G\) is product-one-free, with eight vertices and sixteen edges. Let
\[
F=\overline G,
\qquad e(F)=12.
\]

The already proved values for five, six, and seven vertices imply:

\[
\Delta(F)\le4;
\tag{7.1}
\]
\[
\text{any two degree-four vertices of }F\text{ are adjacent};
\tag{7.2}
\]
\[
e_F(U)\ge3\qquad\text{for every five-element }U.
\tag{7.3}
\]

Indeed, deleting one vertex from \(F\) must leave at least eight edges. Deleting two must leave at least five edges, giving (7.2). Condition (7.3) is \(t(5)=8\) in the complement.

Let \(C\) be the set of degree-four vertices of \(F\), put \(r=|C|\), and let \(R=V(F)\setminus C\). By (7.2), \(C\) is a clique, so \(0\le r\le5\).

We examine these six possibilities.

## 7.1. \(r=5\)

Here \(F[C]=K_5\), there are no edges from \(C\) to \(R\), and \(F[R]=P_3\). Hence
\[
G=K_{3,5}+\text{an internal edge}.
\]
Lemma 4.1 gives an identity, a contradiction.

## 7.2. \(r=4\)

Each vertex of \(C\) has exactly one neighbour in \(R\), and \(F[R]\) has two edges.

### Case \(F[R]=2K_2\)

For any \(z\in R\), apply (7.3) to two vertices of \(C\) and \(R\setminus\{z\}\). At most one vertex of \(C\) can have its external neighbour at \(z\). Thus the four edges between \(C\) and \(R\) form a matching.

In \(G\), take all of \(R\) and any two vertices of \(C\). The resulting graph is a \(4\)-cycle with two independent vertices each adjacent to three cycle vertices. This is a planar ten-edge graph on six vertices, one of the certificates in Section 4.2.

### Case \(F[R]=P_3\cup K_1\)

Write the path as \(p-q-s\), with isolated vertex \(w\). Applying (7.3) to two vertices of \(C\) and \(\{p,s,w\}\) shows that no vertex of \(C\) is adjacent to \(q\).

Applying it with \(\{q,p,w\}\) or \(\{q,s,w\}\) shows that at most one vertex of \(C\) is adjacent to each of \(p,s\). Since \(w\notin C\), at most three are adjacent to \(w\). Therefore some vertex of \(C\) is adjacent to \(w\), and another to a path endpoint, say \(p\).

On those two vertices and \(R\), the graph \(F\) is \(P_6\). Thus \(G\) contains \(\overline{P_6}\), again a certificate.

## 7.3. \(r=3\)

Each vertex of \(C\) has two neighbours in \(R\), and \(F[R]\) has three edges.

For \(c\in C\) and \(z\in R\), apply (7.3) to \(\{c\}\cup(R\setminus\{z\})\). It gives
\[
d_{F[R]}(z)+\mathbf 1_{cz\in E(F)}\le2.
\tag{7.4}
\]
Consequently, \(F[R]\) has maximum degree two, and its degree-two vertices have no neighbours in \(C\). The possibilities are
\[
P_4\cup K_1,\qquad P_3\cup K_2,\qquad K_3\cup2K_1.
\]

* If \(F[R]=P_4\cup K_1\), the two neighbours of any \(c\in C\) are either both path endpoints, or one endpoint and the isolated vertex. Accordingly, \(F[R\cup\{c\}]\) is \(C_5\cup K_1\) or \(P_6\).
* If \(F[R]=P_3\cup K_2\), choose \(c\in C\) whose neighbours are not both endpoints of the \(K_2\). Such a \(c\) exists, since otherwise those endpoints would also have degree four in \(F\). Then \(F[R\cup\{c\}]\) is \(C_4\cup K_2\) or \(P_6\).
* If \(F[R]=K_3\cup2K_1\), all edges from \(C\) go to the two isolated vertices. The complement is \(K_{3,5}\) plus an internal edge.

Every case has a certificate from Section 4.

## 7.4. \(r=2\)

Write \(C=\{a,b\}\). They are adjacent, each has three neighbours in \(R\), and \(F[R]\) has five edges.

Removing any one vertex from \(F[R]\) and using (7.3) shows that \(F[R]\) has maximum degree two. Thus it is one of
\[
P_6,\quad C_4\cup K_2,\quad C_5\cup K_1,\quad K_3\cup P_3.
\]
The first three immediately give a six-vertex certificate.

It remains to consider
\[
F[R]=K_3[X]\cup(y-z-w).
\]
For \(c\in\{a,b\}\), let \(s_c=|N_F(c)\cap X|\).

Condition (7.3), applied to \(c\), two vertices of \(X\), and \(y,w\), forces the following possibilities:
\[
\begin{array}{c|c}
s_c&N_F(c)\cap R\\ \hline
0&\{y,z,w\}\\
1&\{\text{one vertex of }X,y,w\}\\
2&\{\text{two vertices of }X,\text{ one of }y,w\}\\
3&X.
\end{array}
\tag{7.5}
\]
No vertex of \(X\) can be adjacent to both \(a,b\), and \(z\) cannot be adjacent to both. Up to exchanging \(a,b\), the possible pairs are therefore
\[
(s_a,s_b)\in\{(0,1),(0,2),(0,3),(1,1),(1,2)\}.
\]

The following table gives the certificates. “Delete \(a,x\)” means take the complement of \(F-\{a,x\}\) inside \(G\).
\[
\begin{array}{c|c|c}
(s_a,s_b)&\text{choice of }x\in X&F-\{a,x\}\\ \hline
(0,1)&\text{the }X\text{-neighbour of }b&C_4\cup K_2\\
(0,2)&\text{either }X\text{-neighbour of }b&P_6\\
(1,1)&\text{the }X\text{-neighbour of }b&C_4\cup K_2\\
(1,2)&\text{either }X\text{-neighbour of }b&P_6
\end{array}
\]
These descriptions follow directly from (7.5): the remaining edge on two vertices of \(X\) either joins a path to the remaining \(b\)-edge, or is separate from the \(4\)-cycle through \(b,y,z,w\).

For \((s_a,s_b)=(0,3)\), the graph \(G\) is \(K_{4,4}\) minus one cross-edge plus an internal edge. Section 4.3, item 2, applies.

## 7.5. \(r=1\)

Let \(C=\{a\}\), and put
\[
H=F-a.
\]
Then \(H\) has seven vertices and eight edges. Its degree-three vertices form a clique: two nonadjacent such vertices would leave only two edges after their deletion, violating (7.3).

Moreover, degree-three vertices of \(H\) are not adjacent to \(a\) in \(F\). Since \(a\) has four neighbours, there are at most three of them. The degree sum of \(H\) is sixteen, so there are exactly two or three.

### Three degree-three vertices

They form a triangle \(T\). The other four vertices \(U\) have degree sequence \(2,2,2,1\) in \(H\); each vertex of \(T\) has one neighbour in \(U\), and \(H[U]\) has two edges. Also \(a\) is adjacent in \(F\) to all of \(U\).

If \(H[U]=2K_2\), the three neighbours of \(T\) in \(U\) are distinct. Taking two vertices of \(T\), together with \(U\), gives either \(P_6\) or \(C_4\cup K_2\) in \(F\).

If \(H[U]=P_3\cup K_1\), the external-neighbour multiset from \(T\) is either:

* the two path endpoints and the isolated vertex, each once; or
* the isolated vertex twice and one path endpoint once.

This follows immediately from the required degrees \(2,2,2,1\). Choosing two suitable vertices of \(T\) gives \(P_6\) or \(C_5\cup K_1\) in \(F\).

Thus \(G\) again contains a six-vertex certificate.

### Two degree-three vertices

Call them \(u,v\). They are adjacent, and all other vertices of \(H\) have degree two.

The possibilities for \(H\) are:

1. a theta graph with path lengths \(1,2,5\);
2. a theta graph with path lengths \(1,3,4\);
3. a triangle and a \(4\)-cycle joined by the edge \(uv\);
4. a diamond \(K_4-e\) and a disjoint triangle.

This list follows by suppressing degree-two paths. In a connected component containing \(u,v\), the suppressed graph is a theta or two cycles joined by a path. Since \(uv\) is an edge, the joining path has length one. If there is another component, it must be a cycle, leaving only the diamond-plus-triangle possibility.

In each of the first three cases, adding one edge to \(H\) produces \(T_7\):

* for the \(1,2,5\) theta, close the four internal vertices of its length-five path into a \(4\)-cycle;
* for the \(1,3,4\) theta, close the three internal vertices of its length-four path into a triangle;
* for the joined triangle and \(4\)-cycle, add a second independent joining edge at adjacent endpoints.

Hence \(G-a\) contains \(R_7\).

For the last case, let the diamond have degree-three vertices \(u,v\) and degree-two vertices \(x,y\), and let the triangle be \(p,q,s\). The vertex \(a\) is adjacent to four of
\[
\{x,y,p,q,s\}.
\]

* If the omitted vertex is, say, \(x\), then
  \[
  G=K_{4,4}-ay+xy,
  \]
  using parts \(\{a,p,q,s\}\) and \(\{u,v,x,y\}\).
* If the omitted vertex is, say, \(p\), then
  \[
  G=K_{4,4}-ax-ay+ap+xy
  \]
  on the same parts.

These are items 2 and 4 of Section 4.3.

## 7.6. \(r=0\)

Now \(F\) is cubic. We first justify the small classification needed here.

If \(F\) is disconnected, it is \(2K_4\).

Suppose it is connected and has a triangle.

* If the three external neighbours of that triangle are distinct, contracting the triangle gives a simple cubic graph on six vertices. Its complement is \(2\)-regular, so that graph is either \(K_{3,3}\) or the triangular prism.
* If two external neighbours coincide, the triangle lies in a diamond. The other four vertices also form a diamond, and the two diamonds are joined by a matching of size two.

Finally, suppose \(F\) is triangle-free. Choose a vertex \(v\) and its three independent neighbours. The other four vertices induce a triangle-free three-edge graph, hence \(P_4\) or \(K_{1,3}\). Degree counting uniquely determines the remaining adjacencies in either case: these give the Möbius ladder \(M_8\) and the cube, respectively.

Thus the complete list is
\[
\begin{array}{c|c}
F&\text{identity certificate in }G=\overline F\\ \hline
2K_4&K_{4,4}\\
\text{cube}&K_4\text{ on a bipartition class}\\
M_8&\text{a planar sixteen-edge graph}\\
\text{triangle expansion of }K_{3,3}&
\text{a planar twelve-edge graph on seven vertices}\\
\text{triangle expansion of the triangular prism}&R_7\\
\text{two diamonds joined by two matching edges}&
\text{Section 4.3, item 3}.
\end{array}
\]

Here are details for the three less immediate entries.

* Label \(M_8\) by \(\mathbb Z_8\), with edges of differences \(1\) and \(4\). Its complement has differences \(2,3\). Multiplying labels by \(3\) identifies the complement with \(C_8^2\), the planar square-antiprism graph. The planar certificate applies.

* In a triangle expansion of \(K_{3,3}\), delete from \(G\) one of the two unexpanded vertices in the same original bipartition class as the expanded vertex. The resulting seven-vertex graph consists of a triangle \(B_1B_2B_3\), three vertices \(X_i\) each joined to the two \(B_j\) with \(j\ne i\), and a seventh vertex joined to all three \(X_i\). Draw the three triangles on the sides of \(B_1B_2B_3\), then place the seventh vertex in the outer face. This is planar with twelve edges.

* For a triangle expansion of the triangular prism, delete the expanded vertex whose external neighbour belongs to the opposite original triangle. The remaining complement is a triangle and a \(4\)-cycle with two independent joining edges at adjacent endpoints. Thus the corresponding seven-vertex subgraph of \(G\) is \(R_7\).

Every cubic case is therefore impossible.

This exhausts \(r=0,1,\ldots,5\), contradicting the assumed product-one-freeness of \(G\). Hence every sixteen-edge graph on eight vertices has an identity subset. Together with (6.1),
\[
\boxed{t(8)=16}.
\]

---

# 8. What is and is not settled

The complete function \(t(k)\) is not determined here.

The proved progress is:

1. An exact structural answer for **planar** transposition graphs:
   \[
   G\text{ is product-one-free}
   \iff
   e_G(U)\le2|U|-3\quad\text{for all }|U|\ge2.
   \]
2. The exact values through eight vertices, including
   \[
   \boxed{t(8)=16}.
   \]

The general obstruction from an identity ordering is
\[
m=2v-2+2g.
\]
The planar case \(g=0\) is now characterized, but the argument does not characterize the positive-genus supports. In particular, it gives no exact formula for \(t(k)\) for \(k\ge9\).

No claim of literature novelty is made. All conclusions above are supported by the supplied proofs rather than by an unverified citation or an unexecuted search.