```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove bounded twin-width for subgraphs of bounded-ply Euclidean ball-intersection graphs with arbitrary radii, and an elementary O(sqrt(n)) bound for arbitrary polynomial-expansion classes.",
  "would_publish": false,
  "caveats": "The geometric special case does not cover arbitrary polynomial-expansion classes; no novelty claim is made."
}
```

# A multiscale geometric special case

The general question is not settled here. The main partial result extends the fixed-scale Euclidean approach in the previous attempt to **balls of arbitrarily different radii**, allowing unbounded vertex degrees. All arguments below are self-contained.

For a finite graph \(G\), let
\[
\nabla_r(G)=\max_H\frac{|E(H)|}{|V(H)|},
\]
where \(H\) ranges over its nonempty \(r\)-shallow minors. Branch sets have radius at most \(r\) in their defining connected subgraphs.

## 1. Statement of the partial result

A finite family of positive-radius closed balls in \(\mathbb R^d\) is **\(p\)-ply** if every point belongs to the interiors of at most \(p\) balls.

Let \(\mathcal B_{d,p}\) consist of graphs admitting a \(p\)-ply ball representation
\[
B_v=B(c_v,\rho_v),\qquad v\in V(G),
\]
such that
\[
uv\in E(G)\quad\Longrightarrow\quad B_u\cap B_v\ne\varnothing.
\tag{1}
\]
Thus arbitrary edges of the intersection graph may be deleted. There is no restriction on the ratio between the largest and smallest radii.

### Theorem 1

Fix integers \(d,p\ge1\), and put
\[
M=\left\lceil p(2\sqrt d+4)^d\right\rceil,
\qquad
a=2^{d+M}+M.
\]
Every \(G\in\mathcal B_{d,p}\) satisfies
\[
\boxed{\operatorname{tww}(G)\le 7^d a-1}
\tag{2}
\]
and, for every integer \(r\ge0\),
\[
\boxed{\nabla_r(G)\le p(16r+4)^d.}
\tag{3}
\]

Consequently, \(\mathcal B_{d,p}\) is a subgraph-closed polynomial-expansion class of bounded twin-width.

The constants are deliberately not optimized.

The key distinction from a fixed-scale spatial contraction is this: a large ball can meet arbitrarily many small balls. We therefore keep large balls uncontracted and group small balls by their **exact adjacencies to the remaining large balls**. Bounded ply ensures that only boundedly many large balls are relevant within any one small spatial cell.

---

## 2. Two elementary observations

### 2.1. Contractions as partitions

At any stage of a contraction sequence, each trigraph vertex represents a part of a partition of \(V(G)\). For distinct parts \(X,Y\):

- their relation is black if \(G[X,Y]\) is complete;
- it is a nonedge if \(G[X,Y]\) is empty;
- it is red otherwise.

This follows directly by induction from the contraction rule. In particular,
\[
XY\text{ red}\quad\Longrightarrow\quad E_G(X,Y)\ne\varnothing.
\tag{4}
\]

Also, if a singleton \(u\) has the same adjacency to every vertex of \(X\), then the relation between \(u\) and \(X\) is not red.

### 2.2. A packing lemma for large balls

**Lemma 2.** In a \(p\)-ply family of balls in \(\mathbb R^d\), the number of balls of radius at least \(R>0\) that meet \(B(x,tR)\) is at most
\[
p[2(t+1)]^d
\qquad(t\ge0).
\tag{5}
\]

**Proof.** For each such ball \(B\), choose a point
\[
z\in B\cap B(x,tR).
\]
Inside \(B\), one can place a ball of radius \(R/2\) whose center is at distance at most \(R/2\) from \(z\): if necessary, move from \(z\) toward the center of \(B\).

Every chosen subball lies in \(B(x,(t+1)R)\). These subballs are still \(p\)-ply. Comparing volumes gives
\[
N\,\operatorname{vol}(B(0,R/2))
\le
p\,\operatorname{vol}(B(0,(t+1)R)),
\]
which is (5). Boundary intersections do not affect the volume argument. \(\square\)

---

## 3. Polynomial expansion of the ball class

Let \(H\) be an \(r\)-shallow minor of \(G\), with disjoint branch sets \(X\). For each branch set, choose a vertex whose representing ball has maximum radius, and write
\[
R_X=\max_{v\in X}\rho_v,
\qquad
c_X=\text{center of a chosen ball attaining }R_X.
\]

Orient every edge of \(H\) toward the branch set with larger \(R_X\), breaking ties by a fixed total order. We bound every outdegree.

Fix a branch set \(X\), and put \(R=R_X\). Consider an outneighbor \(Y\), so \(R_Y\ge R\). Choose an original edge \(uv\) witnessing the adjacency, with \(u\in X\) and \(v\in Y\).

Inside \(X\), there is a path of length at most \(2r\) from its chosen maximum-radius vertex to \(u\). Inside \(Y\), there is a path of length at most \(2r\) from \(v\) to a maximum-radius vertex of \(Y\).

Along the latter path, let \(w\) be the first vertex whose ball has radius at least \(R\). All balls encountered before \(B_w\) on the combined path have radius at most \(R\). Consecutive centers of such balls are at distance at most \(2R\), by (1).

There are at most \(4r\) edges before the predecessor of \(w\). Hence the predecessor ball is contained in
\[
B(c_X,(8r+1)R).
\]
Since it meets \(B_w\), the ball \(B_w\) also meets this ambient ball.

We have therefore associated with every outneighbor \(Y\) a ball satisfying
\[
\rho_w\ge R,
\qquad
B_w\cap B(c_X,(8r+1)R)\ne\varnothing.
\]
Different branch sets \(Y\) give distinct balls. Lemma 2 yields
\[
d_H^+(X)
\le
p[2(8r+2)]^d
=
p(16r+4)^d.
\]
Summing outdegrees proves (3).

This argument applies directly to edge-deleted intersection graphs: it uses only implication (1).

---

## 4. A bounded-width multiscale contraction sequence

We now prove (2).

Assume \(G\) is nonempty. Rescale and translate the representation so that:

1. every radius is greater than \(1\);
2. for some integer \(L\), every radius is at most \(2^L\), and every center lies in the half-open cube
   \[
   [0,2^L)^d.
   \]

These operations preserve intersections and ply.

For \(i=0,\ldots,L\), set
\[
s_i=2^i.
\]
Use the nested dyadic grids whose cells at level \(i\) have side length \(s_i\).

### 4.1. Partitions at a fixed scale

Call a vertex **large at level \(i\)** if \(\rho_v>s_i\), and write
\[
L_i=\{v:\rho_v>s_i\}.
\]
Every vertex in \(L_i\) remains a singleton.

For the other vertices, use two pieces of information:

1. the dyadic cell containing their centers;
2. their exact neighborhood in \(L_i\).

For a cell \(Q\) and a set \(S\subseteq L_i\), form the nonempty parts
\[
P(Q,S)=
\{v:\rho_v\le s_i,\ c_v\in Q,\ N_G(v)\cap L_i=S\}.
\]
Together with the large singletons, these parts form a partition \(\mathcal P_i\).

By construction, no large singleton has a red relation to any part of \(\mathcal P_i\).

### 4.2. There are boundedly many profiles in one cell

Fix a cell \(Q\) of side \(s=s_i\), with center \(x_Q\). A large ball that is adjacent to a small vertex centered in \(Q\) must meet
\[
B\!\left(x_Q,\left(1+\frac{\sqrt d}{2}\right)s\right).
\]
Indeed, the small ball has radius at most \(s\).

By Lemma 2, the number of such large balls is at most
\[
p(\sqrt d+4)^d\le M.
\]
Thus there are at most
\[
2^M
\tag{6}
\]
nonempty small-vertex parts in each cell.

The bound concerns relevant large vertices, not all large vertices in the graph.

### 4.3. The partitions are nested

Consider the transition from \(s=s_i\) to \(2s=s_{i+1}\).

An old small part lies in one child cell of a new cell. Its vertices have identical neighborhoods in \(L_i\), and therefore also in
\[
L_{i+1}\subseteq L_i.
\]
Thus every old small part lies in a single part of \(\mathcal P_{i+1}\).

Vertices with
\[
s<\rho_v\le2s
\]
were singletons and now become small. Vertices with radius greater than \(2s\) remain singletons.

Consequently, \(\mathcal P_i\) refines \(\mathcal P_{i+1}\). We realize the transition by binary merges, processing the parts of \(\mathcal P_{i+1}\) one at a time.

### 4.4. Boundedly many active parts per new cell

Call all vertices of radius at most \(2s\) **active during this transition**.

A new cell \(Q\), of side \(2s\), contains:

- at most \(2^d2^M\) old small parts, by (6);
- at most \(M\) newly small singleton vertices.

For the second assertion, the newly small balls have radius greater than \(s\), and their centers lie in \(Q\). They therefore meet
\[
B(x_Q,\sqrt d\,s).
\]
Lemma 2 bounds their number by
\[
p(2\sqrt d+2)^d\le M.
\]

Hence, throughout the transition, each new cell contains at most
\[
2^d2^M+M=a
\tag{7}
\]
current active parts. Merging can only decrease this number.

### 4.5. Red-degree bound throughout the transition

There are two types of current parts.

**Remaining large singletons.** These have radius greater than \(2s\). Every current active part is contained in one part of \(\mathcal P_{i+1}\), so all its vertices have the same adjacency to each remaining large singleton. Such singletons consequently have red degree zero.

**Active parts.** Each is contained in one new cell, and every ball represented in it has radius at most \(2s\).

Suppose two active parts have a red relation. By (4), they contain endpoints of an original edge. The corresponding centers are at distance at most
\[
2s+2s=4s.
\]
The new cells have side length \(2s\). Thus their cell indices differ by at most \(3\) in each coordinate. A cell has at most \(7^d\) possible contact cells, including itself.

By (7), each contains at most \(a\) active parts. Therefore every active part has red degree at most
\[
7^d a-1.
\]

This holds at every individual binary merge.

Finally, \(\mathcal P_0\) is the singleton partition, because all radii exceed \(1\). At level \(L\), there are no large vertices, and all centers lie in one cell, so \(\mathcal P_L=\{V(G)\}\). We have constructed a complete contraction sequence of width at most \(7^d a-1\), proving Theorem 1. \(\square\)

---

## 5. What this adds to the fixed-scale approach

The bounded-contact hierarchy idea from the previous attempt is sound in its fixed-scale geometric setting. Applying it without modification to variable-radius balls would fail: a large ball can contact arbitrarily many small spatial cells.

The profile refinement above addresses exactly that obstruction. It does **not** bound the total degree of every quotient vertex. Large singleton vertices may have arbitrarily many black neighbors, but their red degree remains zero until the spatial scale is comparable to their radius.

This is a genuine enlargement of the geometric special case. For example, in the plane a unit disk can be externally tangent to arbitrarily many pairwise interior-disjoint tiny disks. Thus \(\mathcal B_{2,1}\) contains stars of arbitrarily large degree. Such a family cannot have a fixed separated, bounded-edge-length representation in a uniformly doubling metric, since that condition forces bounded degree.

Nevertheless, Theorem 1 supplies a uniform twin-width bound.

---

# An elementary general \(O(\sqrt n)\) estimate

There is also a simple improvement over the previous attempt’s size-dependent estimate. It needs only the density bound at depth zero, not a separator theorem.

### Proposition 3

Every graph with \(m\) edges satisfies
\[
\boxed{\operatorname{tww}(G)\le \left\lceil2\sqrt m\right\rceil.}
\tag{8}
\]

**Proof.** The case \(m=0\) is immediate. Otherwise, put
\[
T=\lceil2\sqrt m\rceil
\]
and give each vertex weight \(w(v)=\deg_G(v)\).

Keep every vertex of weight greater than \(T\) as a singleton bin. Call these vertices heavy.

Pack all remaining vertices into bins of total weight at most \(T\), using the next-fit rule: fill the current bin until the next vertex would exceed the capacity, and then start a new bin. Isolated vertices can be included in these bins; if there are no other light vertices, use one zero-weight bin.

Let:

- \(h\) be the number of heavy vertices;
- \(W_H\) be their total weight;
- \(W_L\) be the total weight of the other vertices;
- \(q_L\) be the number of light bins.

Consecutive light bins have combined weight greater than \(T\). Therefore
\[
q_L\le \frac{2W_L}{T}+1.
\]
Also \(h\le W_H/T\). The total number \(q=h+q_L\) of bins satisfies
\[
q
\le
\frac{W_H+2W_L}{T}+1
\le
\frac{4m}{T}+1
\le T+1.
\tag{9}
\]

Now contract each light bin to one part, one bin at a time.

Any nonsingleton part \(X\) formed in this phase has
\[
\sum_{v\in X}\deg_G(v)\le T.
\]
By (4), its red degree is at most the number of original edges leaving it, and hence at most \(T\). A light singleton also has red degree at most its original degree, at most \(T\).

A heavy singleton can have red relations only to nonsingleton parts. There are at most \(q_L\) such parts. If heavy vertices exist, then
\[
q_L\le q-1\le T.
\]
Thus the whole first phase has width at most \(T\).

Afterwards there are at most \(T+1\) parts by (9). Arbitrary further merges have red degree at most \(T\). This proves (8). \(\square\)

### Corollary 4

If
\[
\nabla_r(G)\le A(r+1)^k
\]
and \(G\) has \(n\) vertices, then
\[
\boxed{\operatorname{tww}(G)\le\left\lceil2\sqrt{An}\right\rceil.}
\tag{10}
\]

Indeed, \(m\le An\). This bound applies to every uniformly linear-density class, so it does not exploit the polynomial control at positive depths. In particular, it is not a substitute for the constant bound sought in the conjecture.

---

# Remaining gap

Theorem 1 proves the desired constant bound for a multiscale geometric subclass, with both its polynomial expansion and its contraction sequence established directly.

The general conjecture remains untouched at the following precise point:

> I do not show, and do not assume, that an arbitrary polynomial-expansion class admits bounded-ply ball representations—or any equivalent multiscale partition structure.

The geometric proof requires a bounded number of relevant larger objects in each cell at every scale. Polynomial expansion provides bounds on shallow-minor density, but no argument here converts those bounds into that incidence property.

Thus the outcome is a proved special case and a stronger elementary size-dependent bound, not a proof or counterexample for arbitrary polynomial-expansion classes.