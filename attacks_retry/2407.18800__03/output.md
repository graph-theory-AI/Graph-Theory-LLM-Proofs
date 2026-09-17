```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any counterexample has at least twelve non-ring triangular faces; one with at most thirteen has exactly two degree-six interior vertices and at most sixteen vertices in total.",
  "would_publish": false,
  "caveats": "The remaining small cases have not been enumerated, and the unrestricted conjecture is not proved."
}
```

# A sharper face bound and a small residual case

I retain the degree-choosability approach from the supplied attempt, after checking it, but strengthen its conclusions. In particular, the lower bound of ten non-ring triangular faces can be improved to **twelve**. The entire case of at most thirteen such faces reduces to a rather restricted family on at most sixteen vertices.

No computational verification is claimed.

## 1. Definitions and results

I use the following standard formulation. Let \(G\) be a finite simple graph embedded in a cylinder whose boundary components are disjoint triangles \(T_1,T_2\), and put
\[
S=T_1\cup T_2.
\]
Every vertex outside \(S\) has a list of size at least five. The canvas is \(S\)-critical if, for every proper subgraph \(G'\supseteq S\), some \(L\)-coloring of \(S\) extends to \(G'\) but not to \(G\).

Assume throughout that
\[
\operatorname{dist}_G(T_1,T_2)\ge 5.
\]
Cap the two boundary triangles to obtain a plane embedding. Write
\[
H=G-V(S),\qquad n=|V(H)|,
\]
and define
\[
q=\sum_{v\in V(H)}(\deg_G(v)-5),\qquad
r=3n-6-|E(H)|.
\]
Let \(t\) be the number of triangular faces other than the two cap faces.

### Theorem

For a critical prism-canvas of spacing at least five:

1. \(n\ge 8\) and \(q\ge 1\).
2. If exactly one interior vertex has degree greater than five, then
   \[
   q+r\ge 4.
   \]
   In particular, such a canvas has \(t\ge 14\).
3. If \(r=0\), so that \(H\) is a plane triangulation, then \(n\ge 10\).
4. Always,
   \[
   \boxed{t\ge 12.}
   \]
   Moreover, if \(t\le 13\), then necessarily
   \[
   \boxed{q=2,\quad r=1,\quad 8\le n\le 10.}
   \]
   Thus exactly two interior vertices have degree six, all other interior vertices have degree five, and \(H\) is 2-connected with one quadrilateral face and all other faces triangular.

In the last case, if \(t=12\), all non-cap faces of \(G\) are triangles or quadrilaterals. If \(t=13\), precisely one is a pentagon and all the others are triangles or quadrilaterals.

These conclusions do not settle the conjecture.

---

## 2. Basic consequences of criticality

We use two established list-coloring facts:

- a proper precoloring of a facial triangle in a plane graph extends when every other vertex has a list of size at least five;
- a connected graph is degree-choosable unless every block is a complete graph or an odd cycle.

The first is a standard consequence of the precolored-edge form of Thomassen’s planar 5-list-coloring theorem. The second is the degree-choosability theorem. A graph whose components have only complete-graph and odd-cycle blocks will be called a **Gallai forest**.

The first fact also lets us assume \(G\) is connected. If the rings were in different components, every coloring of \(S\) would extend componentwise. Any additional component containing neither ring could be removed without changing which colorings of \(S\) extend, contrary to criticality.

### Lemma 2.1: minimum degree

For every \(v\in V(H)\),
\[
\deg_G(v)\ge |L(v)|\ge 5.
\]

**Proof.** Apply criticality to \(G-v\). If \(\deg_G(v)<|L(v)|\), any coloring of \(G-v\) extends to \(v\), contradicting the criticality witness. ∎

Call an interior vertex **low** if its degree in \(G\) is five, and **high** otherwise.

### Lemma 2.2: the low vertices induce a Gallai forest

**Proof.** Let \(K\) be a component of the graph induced by the low vertices. Criticality gives a coloring \(\psi\) of \(G-V(K)\) that does not extend to \(G\). For \(v\in V(K)\), remove from \(L(v)\) the colors used by its neighbors outside \(K\), obtaining \(M(v)\). Then
\[
|M(v)|\ge 5-\bigl(\deg_G(v)-\deg_K(v)\bigr)=\deg_K(v).
\]
Thus \(K\) cannot be degree-choosable and is a Gallai tree. ∎

Gallai forests are closed under taking induced subgraphs. Consequently, finding an induced non-Gallai graph consisting entirely of low vertices gives a contradiction.

For later use, spacing gives two immediate observations:

- an interior vertex has neighbors in at most one ring, and at most three ring neighbors;
- if \(x\) has a neighbor in \(T_1\) and \(y\) has a neighbor in \(T_2\), then
  \[
  \operatorname{dist}_H(x,y)\ge 3. \tag{2.1}
  \]

We label such a vertex \(x\) by the ring it meets.

### Lemma 2.3: \(n\ge 8\)

**Proof.** Suppose \(n\le 7\), and take a shortest ring-to-ring path. Let \(u,v\) be its first and last interior vertices, and \(x,y\) its second and penultimate interior vertices.

The vertices \(x,y\) have no ring neighbors, so
\[
\deg_H(x),\deg_H(y)\ge 5.
\]
Also \(xv,yu\notin E(H)\). Therefore \(n\ge 7\), and equality forces \(x\) to be adjacent to every interior vertex except \(v\), and \(y\) to every interior vertex except \(u\).

Put \(R=V(H)\setminus\{u,v\}\), so \(|R|=5\). Besides \(x,y\), every vertex of \(R\) is adjacent to both \(x\) and \(y\). Such a vertex cannot meet either ring: a ring adjacency would produce a ring-to-ring path of length at most four. Thus every vertex of \(R\) has degree at least five in \(H\).

The vertices \(u,v\) have no common neighbor, by (2.1). Hence each vertex of \(R\) has at most one neighbor in \(\{u,v\}\), and therefore must be adjacent to all four other vertices of \(R\). This gives a \(K_5\), contradicting planarity. ∎

---

## 3. A Gallai interior cannot join distant rings

The next observation slightly strengthens the degree-five argument in the supplied attempt: it needs only minimum interior degree five, not equality.

### Lemma 3.1: an octahedral cap is unique

Let \(T\) be a facial triangle. On its non-cap side, there cannot be two vertex-disjoint triangles \(X,Y\), each of whose vertices has exactly two neighbors in \(T\).

**Proof.** The graph \(T\cup X\), including its six attachment edges, has six vertices and twelve edges. It is therefore a plane triangulation.

Every vertex of \(X\) has degree four in this triangulation. A vertex of \(T\) cannot have degree two. Nor can it have degree three: its three neighbors would have to form a triangle, forcing its unique neighbor in \(X\) to be adjacent to all three vertices of \(T\). Consequently every vertex has degree four, and \(T\cup X\) is the octahedral graph.

The same reasoning applies to \(T\cup Y\), so the vertices of \(Y\) collectively meet all three vertices of \(T\). But the connected triangle \(Y\) must lie in a single face of \(T\cup X\). The only face of this octahedron containing all three vertices of \(T\) on its boundary is the graph-free cap bounded by \(T\). This is impossible. ∎

### Lemma 3.2: a Gallai component of \(H\) cannot meet both rings

Assume only that every interior vertex has degree at least five.

**Proof.** Suppose a Gallai component \(K\) meets both rings. For \(v\in V(K)\), let
\[
b(v)=|N_G(v)\cap V(S)|.
\]
Then
\[
\deg_K(v)+b(v)\ge 5,\qquad b(v)\le 3,
\]
so \(\deg_K(v)\ge 2\).

All complete blocks of \(K\) have order at most four.

If \(K\) is a single block, it cannot be \(K_2\). In an odd-cycle block, every vertex has three ring neighbors; two adjacent vertices must have the same label, and together with that ring form a \(K_5\). If \(K=K_4\), every vertex has ring neighbors, all with the same label, so \(K\) does not meet both rings.

Now suppose \(K\) has multiple blocks. Consider an end block with cutvertex \(c\).

- It cannot be \(K_2\), because its non-cutvertex would need at least four ring neighbors.
- It cannot be an odd cycle: two adjacent non-cutvertices would each have three neighbors in the same ring, again giving a \(K_5\).
- Thus it is \(K_4\).

Its three private vertices form a triangle \(X\). Each has at least two ring neighbors, and all have the same label. Planarity of the six-vertex graph consisting of \(X\) and that ring implies that there are at most six attachment edges. Hence each private vertex has exactly two ring neighbors.

By Lemma 3.1, there is at most one end block of each label. Thus the block-cutvertex tree has exactly two leaves, with different labels, and is a path.

An internal odd-cycle block of length at least five has two adjacent non-cutvertices, which gives the same \(K_5\) contradiction. Therefore the non-edge blocks along the path are triangles and \(K_4\)'s. Each has a labeled private vertex.

Two consecutive non-edge blocks sharing a cutvertex have private vertices at distance at most two, so their labels agree by (2.1). If they are separated by edge blocks, every vertex along that intervening chain has degree at most four in \(K\), hence has a ring neighbor. Labels again propagate unchanged.

The two end blocks consequently have the same label, a contradiction. ∎

If all interior vertices were low, Lemma 2.2 would make \(H\) a Gallai forest, while a ring-to-ring path would supply a component meeting both rings. Hence
\[
\boxed{q\ge 1.} \tag{3.1}
\]

---

## 4. A single high vertex requires \(q+r\ge 4\)

We first record a small extremal fact.

### Lemma 4.1: small planar Gallai forests

Let \(F\) be a planar Gallai forest with maximum degree at most five. Then:

\[
\begin{array}{c|c|l}
|V(F)| & |E(F)|\text{ at most} & \text{structure at equality}\\ \hline
7&10&\text{one }K_4,\text{ one }K_3,\text{ and one }K_2\text{ block}\\
8&13&\text{two disjoint }K_4\text{'s joined by a bridge}\\
9&15&\text{not needed}
\end{array}
\]

In the seven-vertex equality case, the block-cutvertex tree is a path.

**Proof.** If \(F\) has \(k\) vertices and \(c\) components, then
\[
|E(F)|\le 2(k-c). \tag{4.1}
\]
Indeed, for each permissible block \(B\),
\[
|E(B)|\le 2(|V(B)|-1).
\]
Equality holds only for \(K_4\).

More precisely, a \(K_2\) or \(K_3\) block contributes deficit one to (4.1), a \(K_4\) contributes zero, and an odd cycle of length at least five contributes deficit at least three.

For \(k=7\), twelve edges would require two \(K_4\)'s sharing a cutvertex, giving degree six; eleven edges is incompatible with the block-order sum. At ten edges the deficit and order sums force precisely \(K_4,K_3,K_2\). These three blocks cannot share one cutvertex, again because that would give degree six.

For \(k=8\), fourteen edges is incompatible with the order sum for a connected union of \(K_4\) blocks. Thirteen edges forces two \(K_4\)'s and one \(K_2\); the degree bound forces the \(K_2\) to join the two \(K_4\)'s.

For \(k=9\), sixteen edges would require a connected union of \(K_4\) blocks, whose order is \(1\pmod 3\), not nine. ∎

### Proposition 4.2

If there is exactly one high vertex, then \(q+r\ge 4\).

**Proof.** Let the high vertex be \(z\). Suppose \(q+r\le 3\). Its degree in \(G\) is \(5+q\), and \(K=H-z\) is a Gallai forest of maximum degree at most five. Thus
\[
\begin{aligned}
|E(K)|
&=3n-6-r-\deg_H(z)\\
&\ge 3n-11-(q+r)\\
&\ge 3n-14. \tag{4.2}
\end{aligned}
\]

By Lemma 2.3, \(n\ge 8\). For \(n\ge 11\), (4.2) contradicts (4.1). For \(n=10\), it contradicts the nine-vertex bound in Lemma 4.1.

There remain \(n=8,9\). In both cases equality is forced in (4.2), so
\[
q+r=3,\qquad \deg_H(z)=\deg_G(z)=5+q\ge 6. \tag{4.3}
\]
In particular, \(z\) has no ring neighbor.

#### Case \(n=9\)

Here \(K\) consists of two \(K_4\)'s joined by a bridge \(xy\). Let
\[
X=V(K_4^{(1)})\setminus\{x\},\qquad
Y=V(K_4^{(2)})\setminus\{y\}.
\]
Every vertex of \(X\cup Y\) has degree three in \(K\), at most one additional neighbor \(z\), and degree five in \(G\). Thus all these vertices have ring neighbors.

Each of the triangles \(X,Y\) has a single label. Their labels must differ: otherwise any ring adjacency at \(x\) or \(y\) also has that same label, leaving the other ring unattached to \(H\).

The vertex \(z\) cannot have a neighbor in both \(X\) and \(Y\), since that would give a ring-to-ring path of length four. Consequently
\[
\deg_H(z)\le 3+2=5,
\]
contradicting (4.3).

#### Case \(n=8\)

Here \(K\) has blocks \(K_4,K_3,K_2\), arranged in a path. Every non-cutvertex of \(K\) has degree at most three in \(K\), so has a ring neighbor.

Since \(\deg_H(z)\ge 6\), at most one vertex \(w\) of \(K\) is nonadjacent to \(z\). All labeled neighbors of \(z\) must have the same label. Because both rings attach to \(H\), there must be exactly one such nonneighbor \(w\), and \(w\) has the opposite label.

In a three-block path with blocks \(K_4,K_3,K_2\), every vertex is at distance at most two from a different non-cutvertex. To see this, the only case not immediate inside a non-edge block is the private vertex of an internal triangle or the leaf of an end edge; an adjacent block supplies the required non-cutvertex at distance two.

Apply this observation to \(w\). The resulting different non-cutvertex is adjacent to \(z\), hence has the other label. This contradicts (2.1). ∎

---

## 5. A triangulated interior needs at least ten vertices

### Proposition 5.1

If \(r=0\), then \(n\ge 10\).

**Proof.** Suppose \(n\le 9\). By Lemma 2.3, \(n=8\) or \(9\). Since \(r=0\), \(H\) is a plane triangulation.

Let
\[
A_i=N_G(V(T_i))\cap V(H).
\]
The connected triangle \(T_i\) lies in one face of \(H\), so \(A_i\) is a nonempty subset of a facial triangle, hence a clique.

The closed neighborhoods \(N_H[A_1]\) and \(N_H[A_2]\) are disjoint by spacing. Since \(H\) is 3-connected and \(A_{3-i}\) lies outside \(N_H[A_i]\),
\[
|N_H(A_i)\setminus A_i|\ge 3.
\]
Therefore
\[
n\ge |A_1|+|A_2|+6. \tag{5.1}
\]
Thus there are only the following cases.

### Case 1: \(n=8\)

Equation (5.1) forces \(A_1=\{u\}\), \(A_2=\{v\}\). Their disjoint closed neighborhoods and minimum degree three force
\[
\deg_H(u)=\deg_H(v)=3,
\]
and these neighborhoods partition \(V(H)\).

Deleting \(u,v\) leaves a six-vertex triangulation \(J\). Every vertex of \(J\) has exactly one neighbor in \(\{u,v\}\), no ring neighbor, and degree at least five in \(G\). Thus every vertex has degree at least four in \(J\). Its degree sum is twenty-four, so \(J\) is 4-regular, hence the octahedron.

All six vertices of \(J\) are low in \(G\). This contradicts Lemma 2.2.

### Case 2: \(n=9\) and \(|A_1|+|A_2|=2\)

Again write \(A_1=\{u\}\), \(A_2=\{v\}\). Disjointness of their closed neighborhoods gives
\[
6\le \deg_H(u)+\deg_H(v)\le 7.
\]

If the sum is seven, the other seven vertices have total degree
\[
42-7=35.
\]
They are therefore all low. They induce a seven-vertex graph with fourteen edges, which cannot be a planar Gallai forest by (4.1).

If the sum is six, both degrees are three. Deleting \(u,v\) leaves a seven-vertex triangulation \(J\). Its vertices have total degree thirty-six in \(G\), so exactly one of them, say \(w\), has degree six, and the other six are low.

The graph \(J-w\) is 2-connected because \(J\) is 3-connected. It is a planar graph on six vertices, so it is neither a complete graph nor an odd cycle. Hence it is not a Gallai graph, again contradicting Lemma 2.2.

### Case 3: \(n=9\) and \(|A_1|+|A_2|=3\)

Write
\[
A_1=\{u\},\qquad A_2=\{v,w\}.
\]
Equality in (5.1) gives
\[
\deg_H(u)=3,\qquad
|N_H(\{v,w\})\setminus\{v,w\}|=3.
\]
Put
\[
P=N_H(u),\qquad
Q=N_H(\{v,w\})\setminus\{v,w\}.
\]
The triples \(P,Q\) are disjoint and partition the other six vertices.

The set \(Q\) is a three-vertex separator in a plane triangulation, so it induces a triangle. The side containing \(v,w\) is a triangulated disk with exactly two interior vertices. Hence \(\{v,w\}\) has five edges to \(Q\), distributed as
\[
2,2,1
\]
among the vertices of \(Q\).

Deleting \(u,v,w\) leaves a six-vertex triangulation \(J\), in which \(P,Q\) are disjoint facial triangles. Every vertex of \(P\) has degree at least four in \(J\).

We need a small elementary fact: a six-vertex triangulation that is not the octahedron has at least two degree-three vertices, and these are nonadjacent. Indeed, deleting a degree-three vertex leaves the five-vertex triangulation \(K_5-e\), whose two degree-three vertices are nonadjacent; reinsertion into a triangular face can increase the degree of at most one of them. Adjacent degree-three vertices in a triangulation of order greater than four would contradict 3-connectivity.

In the present \(J\), any degree-three vertices must lie in the clique \(Q\), so there can be at most one. Thus \(J\) is the octahedron.

The three vertices of \(P\) are low in \(G\). The vertex \(a\in Q\) having only one neighbor in \(\{v,w\}\) is also low. In the octahedron, \(a\) is adjacent to exactly two vertices of \(P\). Therefore \(J[P\cup\{a\}]\) is an induced diamond, contradicting Lemma 2.2.

All cases are excluded. ∎

---

## 6. Face counting and the final reduction

Let \(m\) be the number of edges between \(S\) and \(H\). Summing degrees over \(V(H)\) gives
\[
2|E(H)|+m=5n+q,
\]
and hence
\[
m=12-n+q+2r. \tag{6.1}
\]

Define
\[
\sigma=\sum_{\substack{F\text{ non-cap face}\\ |F|\ge 4}}(|F|-4).
\]
Face lengths are counted with boundary-walk multiplicity. Euler’s formula and the face-degree sum give the exact identity
\[
\boxed{t=6+2q+2r+\sigma.} \tag{6.2}
\]
In particular,
\[
t\ge 6+2q+2r. \tag{6.3}
\]

Two further estimates will be useful.

- If \(r=0\), \(H\) has \(2n-4\) triangular faces. Inserting the two rings affects at most two faces of \(H\), so
  \[
  t\ge 2n-6. \tag{6.4}
  \]

- If \(r=1\), then \(H\) is 2-connected. Indeed, its minimum degree is at least two; disconnectedness would give \(r\ge 6\), and a cutvertex would give \(r\ge 3\). The face-excess sum of \(H\) is one, so \(H\) has one quadrilateral face and all other faces triangular. Therefore
  \[
  t\ge 2n-8. \tag{6.5}
  \]

Now suppose \(t\le 13\). By (6.3),
\[
q+r\le 3.
\]
We know \(q\ge 1\). Proposition 4.2 rules out exactly one high vertex, so there are at least two and \(q\ge 2\). Thus \(r\le 1\).

If \(r=0\), Proposition 5.1 and (6.4) give
\[
t\ge 2n-6\ge 14,
\]
a contradiction.

Consequently
\[
r=1,\qquad q=2.
\]
There are exactly two high vertices, both of degree six. Equation (6.5) gives \(n\le 10\), while Lemma 2.3 gives \(n\ge 8\). Finally, (6.2) becomes
\[
t=12+\sigma.
\]
This proves both the universal bound \(t\ge 12\) and the stated description of the cases \(t=12,13\).

## 7. What remains unresolved

The conjecture is still open in this attack.

The remaining case with at most thirteen non-ring triangular faces is now constrained to:

- \(14\), \(15\), or \(16\) total vertices;
- exactly two degree-six interior vertices;
- all other interior vertices of degree five;
- an interior graph with exactly one quadrilateral face and otherwise triangular faces;
- either only triangular and quadrilateral non-cap faces in \(G\), or one additional pentagonal face.

I have **not** checked all such embeddings and list assignments, so even this small residual family is not claimed to be eliminated. Canvases with at least fourteen non-ring triangular faces also remain unrestricted by this argument beyond the structural conditions proved above.