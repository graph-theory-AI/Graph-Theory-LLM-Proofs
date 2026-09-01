```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Diplanarity admits an exact bipartite-interlacement test, and the circulant digraphs with arcs i→i−1 and i→i+2 form an infinite family of simple obstructions for odd order.",
  "would_publish": false,
  "caveats": "The arbitrary obstruction case remains, and these structural facts or examples may already be known in this specialized literature."
}
```

# Mathematical writeup

## 1. Statement of the partial result

A connected quartic Eulerian digraph has indegree and outdegree two at every vertex. An embedding is directed precisely when incoming and outgoing darts alternate around every vertex.

I prove two results.

### Theorem 1: Interlacement criterion

Let \(D\) be a connected quartic Eulerian digraph, let \(W\) be a directed Euler circuit, and form the interlacement graph \(I(W)\): its vertices are \(V(D)\), and \(x,y\) are adjacent when their two occurrences in the cyclic double-occurrence word \(W\) alternate.

Then
\[
D\text{ is diplanar}\quad\Longleftrightarrow\quad I(W)\text{ is bipartite}.
\]

Thus diplanarity can be recognized in \(O(|V(D)|^2)\) time from any Euler circuit.

### Theorem 2: An infinite family of obstructions

For \(n\ge 3\), let \(D_n\) be the digraph with vertex set \(\mathbb Z_n\) and arcs
\[
i\longrightarrow i-1,\qquad i\longrightarrow i+2
\]
for every \(i\in\mathbb Z_n\), with the two arcs distinguished when \(n=3\).

Then:

1. \(D_n\) is diplanar if and only if \(n\) is even.
2. For every odd \(n\ge 3\), \(D_n\) is an obstruction under directed-cycle removal and suppression.
3. For odd \(n\ge 5\), \(D_n\) has no loops, parallel arcs, or antiparallel pairs. Hence the problem has infinitely many obstructions in the simple oriented case.

Theorem 2 is a complete result only for this circulant family, not a classification of all obstructions.

---

## 2. The interlacement criterion

Fix a directed Euler circuit \(W\) of \(D\). Since every vertex has outdegree two, each vertex occurs exactly twice in the cyclic word of vertices visited by \(W\).

Two vertices \(x,y\) are interlaced if their occurrences appear cyclically as
\[
x\,\cdots\,y\,\cdots\,x\,\cdots\,y.
\]

### Proof of Theorem 1

Suppose first that \(D\) has a directed plane embedding. At every vertex the incident darts alternate in, out, in, out. Consequently, either of the two possible directed transition systems at that vertex can be smoothed without crossings.

Smooth every vertex according to the transitions used by \(W\). Since \(W\) is one Euler circuit, the result is a single embedded Jordan curve \(J\). Each original vertex now corresponds to two marked points of \(J\). Reversing the smoothing amounts to joining those two points by a small connector lying on one of the two sides of \(J\).

Color a vertex according to the side of \(J\) on which its connector lies. Connectors on the same side are disjoint. Two pairs of points whose endpoints alternate on \(J\) cannot be joined disjointly on the same side of \(J\). Hence interlaced vertices receive different colors, and this gives a bipartition of \(I(W)\).

Conversely, suppose \(I(W)\) is bipartite, with parts \(A,B\). Draw an oriented circle carrying the cyclic word \(W\). For every \(x\in A\), join its two occurrences by an arc in the interior of the circle; for every \(x\in B\), use the exterior of the circle, viewed on the sphere.

No two pairs belonging to \(A\) alternate, so all interior arcs can be drawn disjointly. The same holds for \(B\) in the exterior. Contract every connector arc to a point. The intervening portions of the oriented circle become the arcs of \(D\). A local check at a contracted connector shows that the four resulting darts occur in alternating in/out order. Thus this is a directed plane embedding of \(D\).

This proves the equivalence. ∎

### Algorithmic consequence

An explicit recognition algorithm is:

1. Find a directed Euler circuit by Hierholzer's algorithm.
2. Record the two positions of every vertex in the cyclic word.
3. Join \(x,y\) in \(I(W)\) exactly when one occurrence of \(y\), but not both, lies between the two occurrences of \(x\).
4. Test \(I(W)\) for bipartiteness.

The straightforward implementation takes \(O(n^2)\) time for \(n=|V(D)|\). A bipartition also constructs a directed plane embedding by the proof.

---

## 3. The circulant family \(D_n\)

The digraph \(D_n\) has two outgoing and two incoming arcs at every vertex. Consider the cyclic word
\[
W_n=(w_0,w_1,\ldots,w_{2n-1}),
\qquad
w_{2i}=i,\quad w_{2i+1}=i-1
\]
with subscripts in \(\mathbb Z_n\). Explicitly,
\[
W_n=
0,n-1,1,0,2,1,3,2,\ldots,n-1,n-2.
\]

The arcs between consecutive terms alternate as
\[
i\longrightarrow i-1,\qquad i-1\longrightarrow i+1,
\]
so \(W_n\) uses every arc of \(D_n\) exactly once.

The two occurrences of \(i\) are at positions \(2i\) and \(2i+3\), cyclically. Between them lie one occurrence each of \(i-1\) and \(i+1\), and no occurrence of any other vertex. Therefore
\[
I(W_n)\cong C_n.
\]

By Theorem 1,
\[
D_n\text{ is diplanar}\quad\Longleftrightarrow\quad C_n\text{ is bipartite}
\quad\Longleftrightarrow\quad n\text{ is even}.
\]

It remains to prove minimality when \(n\) is odd.

---

## 4. A directed projective-plane embedding

Assume henceforth that \(n\ge 5\) is odd.

For each \(i\in\mathbb Z_n\), introduce the directed triangular face
\[
T_i:\quad i\longrightarrow i+2\longrightarrow i+1\longrightarrow i.
\]
Also introduce the directed Hamiltonian face
\[
H:\quad 0\longrightarrow 2\longrightarrow 4\longrightarrow\cdots,
\]
which uses all \(+2\) arcs because \(\gcd(2,n)=1\).

The triangular faces alone form a Möbius band. One direct construction is to start from the infinite strip with vertices \(\mathbb Z\), edges between integers at distance one or two, and triangles
\[
\{j,j+1,j+2\}.
\]
Its two boundary components consist of the even and odd distance-two edges. Quotienting by \(j\mapsto j+n\), with \(n\) odd, exchanges these two boundary components and produces a Möbius band. Its single boundary is \(H\). Capping \(H\) by a disk gives an embedding of \(D_n\) in the projective plane.

All the listed face boundaries are directed. In particular, the local rotations alternate incoming and outgoing darts.

### Homotopy class of a directed cycle

Lift a directed cycle \(C\) to the infinite strip. Give a \(+2\) arc increment \(+2\), and a \(-1\) arc increment \(-1\). If \(C\) contains \(p\) arcs of the first type and \(a\) of the second, its total increment is
\[
2p-a=qn
\]
for some integer \(q\).

In the Möbius band, \(q\) is its winding number. The boundary \(H\) has winding number \(2\), so capping \(H\) imposes the relation \(2=0\) in the fundamental group. Therefore, in the resulting projective plane,
\[
C\text{ is noncontractible}\quad\Longleftrightarrow\quad q\text{ is odd}.
\]

---

## 5. Classification of the directed cycles of \(D_n\)

Represent a directed cycle by its cyclic sequence of increments from
\[
\{-1,+2\}.
\]

Suppose a simple directed cycle of length greater than three contained three consecutive increments consisting of one \(+2\) and two \(-1\)'s, in any order. These three increments sum to zero, so the walk would return to the same lifted vertex after three steps. This contradicts simplicity unless the whole cycle is that triangle.

Consequently, in any longer mixed cycle:

- two \(-1\)'s cannot be consecutive, unless every increment is \(-1\);
- two \(-1\)'s cannot be separated by just one \(+2\);
- hence there are at least two \(+2\)'s between consecutive \(-1\)'s.

The possibilities are therefore as follows.

1. **All increments are \(-1\).**  
   The cycle is the Hamiltonian \(-1\)-cycle, with \(q=-1\).

2. **All increments are \(+2\).**  
   Since \(n\) is odd, this is the Hamiltonian \(+2\)-cycle, with \(q=2\).

3. **The cycle is a directed triangle.**  
   It has one \(+2\) and two \(-1\) increments, and \(q=0\). These are exactly
   \[
   i\longrightarrow i+2\longrightarrow i+1\longrightarrow i.
   \]

4. **The cycle is mixed and has length greater than three.**  
   If \(a>0\) is the number of \(-1\) increments, then \(p\ge 2a\), so
   \[
   2p-a\ge 3a>0.
   \]
   Since the cycle is simple, its length is at most \(n\), and because \(a>0\),
   \[
   2p-a<2n.
   \]
   Thus the only positive multiple of \(n\) possible is
   \[
   2p-a=n,
   \]
   so \(q=1\).

Hence every directed cycle other than a triangle and the \(+2\) Hamiltonian cycle is noncontractible in the projective-plane embedding.

---

## 6. Removing a noncontractible directed cycle

We use the following elementary topological lemma.

### Lemma

Let a quartic Eulerian digraph be embedded in the projective plane with incoming and outgoing darts alternating at every vertex. If \(C\) is a noncontractible directed simple cycle, then deleting \(C\) and suppressing its vertices produces a diplanar digraph.

#### Proof

At a vertex of \(C\), the cycle uses one incoming and one outgoing dart. In an alternating rotation these two darts are adjacent. The two unused darts are also adjacent.

Inside a small vertex disk, smooth the two darts of \(C\) together and independently smooth the two unused darts together. The two smoothings can be made disjoint. Performing this at every vertex of \(C\) gives:

- a simple embedded circle isotopic to \(C\), and
- an embedded copy of the cycle-removal minor, with its degree-two vertices already suppressed.

A noncontractible simple closed curve in the projective plane is one-sided, and its complement is an open disk. The smoothed minor is disjoint from this curve and therefore lies in a disk. Its inherited local rotations still alternate incoming and outgoing darts, so this is a directed plane embedding. ∎

This handles the all-\(-1\) cycle and every mixed cycle of length greater than three. The \(+2\) cycle is Hamiltonian; after deleting it, only a directed 1-in/1-out subgraph remains, and the prescribed suppression plainly gives a diplanar result.

The only unresolved cycle-removals are the directed triangles.

---

## 7. Removing a directed triangle

By translation symmetry it suffices to remove
\[
0\longrightarrow 2\longrightarrow 1\longrightarrow 0.
\]

Let \(m=n-3\), and relabel the surviving vertices \(3,4,\ldots,n-1\) as \(0,1,\ldots,m-1\). For \(m\ge 4\), the resulting quartic Eulerian digraph has the following directed Euler circuit, written as concatenated pairs:
\[
W'_m=
(0,1)(0,2)(1,3)\cdots(m-3,m-1)(m-2,m-1).
\]

A direct examination of consecutive terms verifies that this is exactly the graph obtained after deleting the triangle and suppressing its three vertices. The exceptional new connections are
\[
0\to1,\qquad m-2\to m-1,\qquad m-1\to0,
\]
with all other arcs inherited from \(D_n\).

The two occurrences in \(W'_m\) interlace precisely for consecutive labels. Consequently,
\[
I(W'_m)\cong P_m,
\]
the path on \(m\) vertices. This is bipartite, so Theorem 1 shows that the triangle-removal minor is diplanar.

For \(n=5\), \(m=2\), the corresponding Euler word is \(0101\), whose interlacement graph is \(K_2\). For \(n=3\), deleting a directed cycle leaves only a directed 1-in/1-out graph, which is diplanar after suppression.

Thus every directed-cycle removal from odd \(D_n\) gives a diplanar digraph.

Since diplanarity is hereditary under further cycle removals, every proper minor of \(D_n\) is diplanar. As \(D_n\) itself is non-diplanar, it is an obstruction. ∎

---

## 8. Consequences and the remaining gap

For \(n\ge 5\),
\[
-1\not\equiv 2\pmod n,
\]
and no two arcs of \(D_n\) have the same ordered endpoints. In fact its underlying graph is the simple graph \(C_n^2\), and each underlying edge receives only one orientation. Therefore the odd members provide infinitely many pairwise distinct obstructions without parallel arcs.

This does not determine the complete obstruction set. The interlacement criterion does not reduce the problem merely to listing vertex-minimal non-bipartite graphs. Removing a directed cycle is not, in general, ordinary vertex deletion in the interlacement graph: suppressing the complementary transitions can change the cyclic order and hence the interlacement relation among all surviving vertices. In particular, the existence of an induced odd cycle in \(I(W)\) does not by itself yield that odd cycle as a cycle-removal minor.

What remains unproved is any assertion that an arbitrary obstruction must have interlacement graph \(C_{2k+1}\), must admit the projective-plane model above, or belongs to this family together with the parallel-arc obstructions classified in the source paper.