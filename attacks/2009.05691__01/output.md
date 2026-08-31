```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but there is an O(n^5) algorithm for shortest-path-decomposable target holes, an exact bounded-treewidth algorithm, and explicit triangle-free obstructions to extending the shortest-path method directly.",
  "would_publish": false,
  "caveats": "No unrestricted polynomial-time algorithm or hardness proof is obtained; the main O(n^5) routine is one-sided outside its stated class."
}
```

# Mathematical writeup

## 1. Statement and notation

All graphs are finite, simple, and undirected. A **hole** is an induced cycle of length at least four. The problem is to decide whether a graph \(G\) contains a hole \(C\) with

\[
|C|\equiv 0 \pmod 3.
\]

Thus the possible lengths are \(6,9,12,\ldots\); triangles do not count.

I do not obtain a complete algorithm or a hardness result. I give:

1. an exact reduction to a residue-constrained induced-path problem;
2. a polynomial algorithm for holes admitting a geodesic decomposition;
3. structural restrictions on a shortest target hole in triangle-free graphs;
4. triangle-free examples showing that the geodesic method is not complete;
5. exact algorithms for bounded treewidth and for a natural deletion parameter.

---

## 2. Exact induced-path formulation

For \(v\in V(G)\) and two nonadjacent vertices \(x,y\in N(v)\), define

\[
G_{v;x,y}
=
G-\left(\{v\}\cup \bigl(N(v)\setminus\{x,y\}\bigr)\right).
\]

### Proposition 2.1

A graph \(G\) contains a hole of length divisible by three if and only if, for some \(v\) and some nonadjacent \(x,y\in N(v)\), the graph \(G_{v;x,y}\) contains an induced \(x\)-\(y\) path whose number of edges is congruent to \(1\pmod 3\).

#### Proof

Suppose \(C\) is a target hole and \(v\in V(C)\). Let \(x,y\) be the two neighbors of \(v\) on \(C\). Since \(C\) is induced, \(x,y\) are nonadjacent, and no internal vertex of the path \(C-v\) is adjacent to \(v\). Hence \(C-v\) is an induced \(x\)-\(y\) path in \(G_{v;x,y}\). Its length is

\[
|C|-2\equiv 1\pmod 3.
\]

Conversely, let \(P\) be such an induced path. No internal vertex of \(P\) is adjacent to \(v\), by the definition of \(G_{v;x,y}\). Since \(x,y\) are nonadjacent, adding the edges \(vx\) and \(vy\) produces an induced cycle. Its length is

\[
|E(P)|+2\equiv 0\pmod 3.
\]

Because \(x,y\) are nonadjacent, \(|E(P)|\neq 1\); the first possible value congruent to \(1\pmod 3\) is \(4\), so the resulting cycle has length at least six. ∎

This formulation isolates the difficulty: replacing the required path by an ordinary shortest path loses control of its residue, while finding a terminal induced path of prescribed residue is not known to be polynomial-time solvable in this generality.

---

## 3. A structural restriction in triangle-free graphs

Let \(C\) be a shortest target hole, of length \(L\), in a triangle-free graph. For \(z\notin V(C)\), list its neighbors on \(C\) cyclically. A **\(z\)-sector** is a subpath of \(C\) between two cyclically consecutive neighbors of \(z\), and its length is its number of edges.

### Lemma 3.1

Let \(G\) be triangle-free, and let \(C\) be a shortest hole with \(L\equiv0\pmod3\). If a \(z\)-sector has length \(d\equiv1\pmod3\), then

\[
d=L-2,
\]

\(z\) has exactly two neighbors on \(C\), and the other sector has length two.

Consequently, if \(z\) has at least three neighbors on \(C\), every \(z\)-sector has residue \(0\) or \(2\pmod3\), and the number of sectors having residue \(2\) is divisible by three.

#### Proof

Triangle-freeness implies that every sector has length at least two. A sector of length \(d\), together with \(z\), induces a hole of length \(d+2\): by definition, \(z\) has no neighbor in the interior of that sector.

If \(d\equiv1\pmod3\), then \(d+2\equiv0\pmod3\). Since \(C\) was chosen shortest among target holes,

\[
d+2\ge L.
\]

On the other hand, the other sectors have total length at least two, so \(d\le L-2\). Hence \(d=L-2\). The remaining sectors have total length two; as every sector has length at least two, there is exactly one remaining sector, of length two.

If \(z\) has at least three neighbors, the exceptional case is impossible. Thus all sector residues are \(0\) or \(2\). If \(r\) sectors have residue \(2\), then

\[
0\equiv L\equiv 2r\pmod3,
\]

and hence \(r\equiv0\pmod3\). ∎

The all-zero possibility is important: a vertex may have three widely spaced neighbors on \(C\), all sectors having length divisible by three. The examples below show that this is a genuine obstruction rather than an artifact of the proof.

---

## 4. Polynomial detection of geodesically decomposable holes

Call a hole \(C\) **geodesically decomposable** if one of the following holds.

- If \(|C|=2d\), there are opposite vertices \(r,s\in V(C)\) such that both \(r\)-\(s\) arcs of \(C\) are shortest \(r\)-\(s\) paths in \(G\).
- If \(|C|=2d+1\), there are a vertex \(r\) and the edge \(xy\) opposite \(r\) such that the two paths from \(r\) to \(x\) and \(y\) in \(C-xy\), each of length \(d\), are shortest paths in \(G\).

Every isometric hole is geodesically decomposable, but the latter class is larger.

### Theorem 4.1

There is an \(O(n^5)\)-time algorithm that finds a geodesically decomposable hole of length divisible by three, or correctly reports that none exists.

### Proof

Fix a root \(r\), and compute the BFS layers

\[
L_i=\{v:\operatorname{dist}(r,v)=i\}.
\]

A path with one vertex in each of \(L_0,L_1,\ldots,L_i\) is a shortest path and is automatically induced: an edge joining vertices whose layer indices differ by at least two would contradict the distance labels.

For \(i\ge1\), maintain a set \(D_i\subseteq L_i\times L_i\). A pair \((p,q)\) belongs to \(D_i\) if there exist paths

\[
P=(r=p_0,p_1,\ldots,p_i=p),\qquad
Q=(r=q_0,q_1,\ldots,q_i=q)
\]

such that:

1. \(p_j,q_j\in L_j\);
2. \(p_j\neq q_j\) for \(j\ge1\);
3. apart from the common vertex \(r\), the two paths are vertex-disjoint;
4. there is no edge between \(P-r\) and \(Q-r\).

The initialization is

\[
D_1=\{(p,q):p,q\in L_1,\ p\neq q,\ pq\notin E(G)\}.
\]

For \((p,q)\in D_i\), choose

\[
p'\in N(p)\cap L_{i+1},\qquad
q'\in N(q)\cap L_{i+1}.
\]

Then put \((p',q')\) into \(D_{i+1}\) provided

\[
p'\neq q',\qquad
p'q'\notin E,\qquad
p'q\notin E,\qquad
q'p\notin E.
\]

These local tests are sufficient. Indeed, an edge between \(p'\in L_{i+1}\) and an earlier vertex of \(Q\) can only go to layer \(L_i\) or \(L_{i+1}\); the only old possibility is \(q\in L_i\). The same applies symmetrically.

There are two closure operations.

### Even closure

Suppose \(d\ge3\), \(d\equiv0\pmod3\), and \((p,q)\in D_{d-1}\). If some \(s\in L_d\) is adjacent to both \(p\) and \(q\), then

\[
P+p s
\quad\text{and}\quad
Q+q s
\]

are two internally disjoint shortest \(r\)-\(s\) paths of length \(d\). Their union is an induced cycle of length \(2d\), hence a target hole.

No additional chord can meet \(s\): every earlier vertex lies in a layer at most \(d-2\), except the two intended predecessors \(p,q\).

### Odd closure

Suppose \(d\ge4\), \(d\equiv1\pmod3\), and \((p,q)\in D_{d-1}\). Choose distinct \(x,y\in L_d\) such that

\[
px,qy,xy\in E(G),\qquad xq,yp\notin E(G).
\]

Then the two shortest paths ending at \(x\) and \(y\), together with \(xy\), form an induced cycle of length

\[
2d+1\equiv0\pmod3.
\]

Conversely, every geodesically decomposable target hole appears in one of these tests: take its distinguished root \(r\); the vertices on the two geodesic arcs occupy the required BFS layers, and inducedness of the hole gives every nonadjacency used in the recurrence.

For a fixed root, there are at most \(n^2\) possible ordered endpoint pairs over all layers. For each state, naively examining all pairs of next-layer neighbors takes \(O(n^2)\) time. Thus one root costs \(O(n^4)\), and all \(n\) roots cost \(O(n^5)\). Predecessor pointers recover a witness. ∎

---

## 5. Triangle-free obstructions to the geodesic method

The preceding algorithm is not complete, even in triangle-free graphs and even when the target hole is unique.

For integers \(q\ge2\) and \(m\ge1\), define \(F(q,m)\) as follows.

- Start with a rim \(R=C_{3q}\).
- Mark vertices \(a_0,a_1,a_2\) such that each of the three rim sectors between consecutive marked vertices has length \(q\).
- Add an independent set \(D=\{z_1,\ldots,z_m\}\).
- Make every \(z_j\) adjacent exactly to \(a_0,a_1,a_2\).

Since the marked vertices are pairwise nonadjacent, \(F(q,m)\) is triangle-free.

### Lemma 5.1

The holes of \(F(q,m)\) are exactly:

1. the rim \(R\), of length \(3q\);
2. holes of length \(q+2\), consisting of one \(z_j\) and one rim sector;
3. induced \(4\)-cycles using two vertices of \(D\) and two marked vertices.

#### Proof

A hole avoiding \(D\) lies in the chordless rim, so it is the whole rim.

Suppose a hole contains exactly one \(z_j\). Since \(z_j\) has degree two in the hole, the hole uses exactly two marked vertices. Removing \(z_j\) leaves a rim path between those marked vertices. If this path contained the third marked vertex, its edge to \(z_j\) would be a chord. Hence the rim path is one sector of length \(q\).

Suppose a hole contains two vertices \(z_i,z_j\). Each must have exactly two marked neighbors in the hole. Thus exactly two marked vertices are present, and the induced subgraph on these four vertices is \(K_{2,2}=C_4\). The marked vertices already have degree two there, so no rim vertex can be added. Three or more vertices of \(D\) would give the marked vertices degree at least three. ∎

Therefore, whenever \(q\equiv0\pmod3\), the rim is the unique hole whose length is divisible by three:

\[
3q\equiv0,\qquad q+2\equiv2,\qquad 4\equiv1\pmod3.
\]

### Odd obstruction: \(F(3,m)\)

Here the unique target hole is \(C_9\). Number its vertices \(0,\ldots,8\), with marked vertices \(0,3,6\). For a root \(i\), the opposite edge has endpoints \(i+4,i+5\pmod9\).

By rotation it is enough to consider \(i=0,1,2\).

- For \(i=0\), the paths
  \[
  0-z_j-3-4,\qquad 0-z_j-6-5
  \]
  have length three, shorter than the two rim arms of length four.
- For \(i=1\), the path \(1-0-z_j-6\) has length three.
- For \(i=2\), the path \(2-3-z_j-6\) has length three.

Thus no root gives two geodesic arms, and the unique target \(C_9\) is not geodesically decomposable.

### Even obstruction: \(F(6,m)\)

Here the unique target hole is \(C_{18}\), with marked vertices \(0,6,12\). Every antipodal rim pair is at rim distance nine. After rotation, write the pair as \(t,t+9\), where \(0\le t\le5\).

- If \(0\le t\le3\), use marked vertices \(0\) and \(12\). The total rim distance from the endpoints to these marks is
  \[
  t+(3-t)=3.
  \]
- If \(t=4,5\), use marked vertices \(6\) and \(12\). The total is
  \[
  (6-t)+(t-3)=3.
  \]

Passing through any \(z_j\) adds two edges, so every antipodal pair has a path of length five, strictly shorter than nine. Hence the unique \(C_{18}\) is not geodesically decomposable.

These examples also realize the all-zero sector pattern in Lemma 3.1.

---

## 6. A deletion parameter

For a target hole \(C\), define

\[
\beta_G(C)=
\min\left\{
|X|:
X\subseteq V(G)\setminus V(C),\
C\text{ is geodesically decomposable in }G-X
\right\}.
\]

This is always finite because deleting every vertex outside \(C\) leaves an isolated cycle.

### Corollary 6.1

For every fixed \(k\), one can decide in time \(O(n^{k+5})\) whether \(G\) contains a target hole \(C\) with \(\beta_G(C)\le k\).

#### Proof

Enumerate all \(X\subseteq V(G)\) with \(|X|\le k\), and apply Theorem 4.1 to \(G-X\). Any hole found in \(G-X\) remains an induced hole in \(G\), because vertices outside a cycle do not affect edges within its vertex set. Conversely, a hole with \(\beta_G(C)\le k\) is found for a witnessing set \(X\). ∎

This is an XP algorithm, not an FPT algorithm.

The parameter cannot be bounded by a universal constant, even on triangle-free graphs with a unique target hole: in both \(F(3,m)\) and \(F(6,m)\), every remaining \(z_j\) destroys all geodesic decompositions of the rim, while deleting all \(m\) such vertices leaves an isolated cycle. Hence

\[
\beta_{F(3,m)}(C_9)=\beta_{F(6,m)}(C_{18})=m.
\]

---

## 7. Exact bounded-treewidth algorithm

### Theorem 7.1

Given a tree decomposition of width \(t\), MOD3-HOLE can be solved in

\[
2^{O(t\log t)}\,n
\]

time.

#### Argument

Use a nice tree decomposition with explicit edge-introduction nodes. A state records:

1. for each bag vertex, whether it is unselected or selected with current induced degree \(0,1,\) or \(2\);
2. a partition of the selected bag vertices describing their connected components in the processed subgraph;
3. whether a selected component has already become disjoint from the current bag;
4. the number of selected vertices modulo three;
5. the selected-set size capped at six.

At an edge-introduction node \(uv\), if both endpoints are selected, the edge is compulsory because the sought cycle is induced. Both degree counters are incremented, and their connectivity blocks are merged; a state is rejected if a degree exceeds two.

When a selected vertex is forgotten, its degree must be exactly two. A component that no longer meets the bag can never connect to a later component, so the standard connectivity condition rejects states that would create two completed components.

At the empty root, accept exactly when there is one completed connected component, every selected vertex has degree two, at least six vertices were selected, and their number is \(0\pmod3\).

A finite connected simple graph in which every vertex has degree two is a cycle. Since all edges between selected vertices were compulsory during the DP, this cycle is induced. The lower bound six excludes triangles.

There are \(4^{t+1}\) degree/selection assignments and at most \(2^{O(t\log t)}\) partitions of a bag, with only constantly many counting flags. This gives the stated running time.

Thus the conjecture has an exact positive answer on every fixed-treewidth class.

As another elementary special case, if \(\alpha(G)\le a\), then every hole has length at most \(2a+1\), since \(C_\ell\) has an independent set of size \(\lfloor\ell/2\rfloor\). For fixed \(a\), exhaustive induced-cycle testing is therefore polynomial.

---

## 8. Remaining gap

The unrestricted problem is not resolved.

The exact induced-path formulation in Proposition 2.1 still requires finding an induced terminal path of a specified residue. The \(O(n^5)\) method works when a target hole has two suitable shortest arcs, but the graphs \(F(3,m)\) and \(F(6,m)\) show that:

- the target hole may be unique;
- the graph may be triangle-free;
- every shortest target hole may fail the required geodesic decomposition;
- arbitrarily many outside vertices may have to be removed before shortest-path reconstruction works.

Lemma 3.1 gives a genuine modular restriction on attachments to a shortest target hole, but the permitted pattern of three or more sectors all congruent to zero already produces the explicit obstruction family. A complete algorithm would therefore need to handle such major attachments collectively, rather than by a bounded cleaning set or a direct replacement by shortest paths. No such unrestricted procedure, and no NP-hardness reduction, is established here.