```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove wsat(K_9,Q_3)=16 and wsat(K_11,Q_3)=19, and strengthen the general lower bound to wsat(K_n,Q_3) >= ceil(5n/3) for n >= 8.",
  "would_publish": false,
  "caveats": "The general exact function remains undetermined; novelty and current literature status have not been verified."
}
```

# Partial results

Write
\[
w(n)=\operatorname{wsat}(K_n,Q_3).
\]

The following are proved below:
\[
\boxed{w(n)\ge \left\lceil\frac{5n}{3}\right\rceil\qquad(n\ge8),}
\tag{1}
\]
and
\[
\boxed{w(9)=16,\qquad w(11)=19.}
\tag{2}
\]

Together with constructions from the supplied attempt, checked and reproduced below, this gives
\[
\boxed{
\left\lceil\frac{5n}{3}\right\rceil
\le w(n)\le
\left\lceil\frac{7n-1}{4}\right\rceil
\qquad(n\ge11).
}
\tag{3}
\]
It also gives
\[
17\le w(10)\le18.
\]

The new ingredient is a strengthened version of the edge-block invariant in the previous attempt. It detects not just insufficient edge density, but also when a block must remain bipartite or become bipartite after deleting one vertex. The previous attempt's separate eight-vertex case analysis is not used here.

All copies of the cube are non-induced.

---

## 1. Elementary properties of the cube

We use the representation
\[
Q_3=K_{4,4}-M,
\]
where \(M\) is a perfect matching.

### 1.1. A density defect

For a nonempty proper edge-subgraph \(J\subsetneq Q_3\), discard isolated vertices and define
\[
\varepsilon(J)=5v(J)-7-3e(J).
\]
Then
\[
\varepsilon(J)\ge0.
\tag{4}
\]

Indeed, the maximum possible edge counts are bounded as follows:
\[
\begin{array}{c|rrrrrrr}
v(J)&2&3&4&5&6&7&8\\ \hline
e(J)&1&2&4&5&7&9&11.
\end{array}
\]
For five, six and seven vertices, these bounds follow by deleting vertices from the cubic graph \(Q_3\).

We need three consequences.

**(a) Small defect forces connectedness.** If \(J\) has \(c\) nontrivial components \(J_1,\ldots,J_c\), then
\[
\varepsilon(J)
=\sum_{j=1}^c\varepsilon(J_j)+7(c-1).
\]
Consequently,
\[
\varepsilon(J)\le6\quad\Longrightarrow\quad J\text{ is connected}.
\tag{5}
\]

**(b) Defect zero.** The possibilities with \(\varepsilon(J)=0\) are a single edge and a cube with one edge deleted.

**(c) Defect one.** The possibilities with \(\varepsilon(J)=1\) are a \(4\)-cycle and \(Q_3-v\) for a vertex \(v\). Both are 2-vertex-connected.

For the last assertion, \(Q_3-v\) consists of a \(6\)-cycle and a seventh vertex adjacent to three alternating vertices of that cycle.

### 1.2. Bipartite and apex-bipartite graphs are preserved

Call a graph **apex-bipartite** if deleting at most one vertex makes it bipartite.

Both bipartiteness and apex-bipartiteness are preserved by cube additions.

For bipartiteness, the two endpoints of the missing edge in \(Q_3-e\) are joined by an odd-length path. Thus any proper two-colouring of the current graph already gives those endpoints opposite colours.

For apex-bipartiteness, fix a vertex \(p\) such that the current graph minus \(p\) is bipartite. Consider an added edge \(xy\).

- If \(p\in\{x,y\}\), deleting \(p\) removes the new edge.
- If the witnessing cube avoids \(p\), use the preceding argument.
- Otherwise use \(Q_3-p-e\). This graph is connected: \(Q_3-p\), described above, has no bridges.

Hence \(x\) and \(y\) are still forced to have opposite colours in the graph minus \(p\).

In particular, an apex-bipartite graph cannot be weakly cube-saturated in \(K_n\) when \(n\ge8\).

### 1.3. Few edges inside a cut

For any partition of a cube's vertices into two classes, let \(I\) be the set of cube edges lying inside the classes. Then
\[
|I|=0\quad\text{or}\quad |I|\ge3,
\tag{6}
\]
and if \(|I|=3\), those three edges form a star.

To see this, compare the chosen partition with a proper bipartition of the cube. The edges in \(I\) are precisely an edge cut \(\delta(S)\) of the cube. Taking \(|S|\le4\),
\[
|\delta(S)|=3|S|-2e(S).
\]
For \(|S|=1,2,3,4\), respectively, a nonempty cut has size at least \(3,4,5,4\). Thus a 3-edge cut isolates one vertex.

It follows that:

> **Cut obstruction.** If \(n\ge8\) and a graph has a vertex bipartition with at most two edges inside its parts, it is not weakly cube-saturated in \(K_n\).

If those two edges meet, deleting their common endpoint makes the graph bipartite. If they are disjoint, a first new internal edge would have to complete a three-edge internal star, which is impossible. The cases of zero or one internal edge are immediate.

---

## 2. A stronger edge-block invariant

Let \(F\) be weakly cube-saturated in \(K_n\), where \(n\ge8\), and fix a valid addition sequence.

Initially, put each edge of \(F\) in its own block. When a new edge is added using a witnessing cube, merge the blocks containing its eleven old edges and place the new edge in that merged block.

For a block \(B\), write

- \(V(B)\) for the vertices incident with its current edges;
- \(m(B)\) for the number of original edges of \(F\) assigned to it;
- and
  \[
  D(B)=3m(B)-5|V(B)|+7.
  \tag{7}
  \]

We prove the following invariant:
\[
\begin{array}{ll}
\text{(i)}&D(B)\ge0;\\[2mm]
\text{(ii)}&D(B)\le4\ \Longrightarrow\ B\text{ is bipartite};\\[2mm]
\text{(iii)}&D(B)\le6\ \Longrightarrow\ B\text{ is apex-bipartite}.
\end{array}
\tag{8}
\]

A singleton original edge has defect zero, so the invariant holds initially.

### 2.1. Exact bookkeeping for a merge

Suppose an addition merges \(k\ge2\) blocks \(B_1,\ldots,B_k\). Partition the eleven old edges of the witnessing cube according to these blocks, obtaining nonempty subgraphs \(J_1,\ldots,J_k\).

Put
\[
s_i=v(J_i),\qquad
t=\sum_i|V(B_i)|-\left|\bigcup_iV(B_i)\right|,
\]
and
\[
d=t-\left(\sum_i s_i-8\right).
\tag{9}
\]
Then \(d\) is a nonnegative integer.

More explicitly, \(d\) counts:

- extra occurrences of cube vertices in blocks beyond their occurrences in the \(J_i\); and
- excess multiplicities of shared vertices outside the cube.

Thus, if \(d=0\), the blocks intersect only as prescribed by the \(J_i\). If \(d=1\), deleting one vertex removes the unique extra overlap.

The endpoints of the added edge already occur among the eleven old edges, so the merged block has vertex set \(\bigcup_iV(B_i)\). Direct calculation gives
\[
\boxed{
D(B)=\sum_iD(B_i)+\sum_i\varepsilon(J_i)+5d.
}
\tag{10}
\]
This proves nonnegativity.

We also use the following colouring observation.

> If the blocks are bipartite, all \(J_i\) are connected, and \(d=0\), then the merged block is bipartite.

Indeed, orient a proper two-colouring of each block to agree on \(J_i\) with a fixed proper two-colouring of the witnessing cube. Connectedness makes this possible, and \(d=0\) ensures that there are no other compatibility conditions. The new edge also receives opposite colours at its endpoints.

If the same hypotheses hold except that \(d=1\), deleting the vertex responsible for the extra overlap gives an apex-bipartite merged block.

### 2.2. Defect at most four

Suppose \(D(B)\le4\). By (10), every child block has defect at most four, \(d=0\), and every \(J_i\) has defect at most four.

Inductively the child blocks are bipartite, and (5) makes all \(J_i\) connected. The colouring observation proves that \(B\) is bipartite.

### 2.3. Defect at most six

Suppose \(D(B)\le6\).

First suppose every child block has defect at most four. They are all bipartite.

- If \(d=0\), every \(J_i\) is connected by (5), so \(B\) is bipartite.
- If \(d=1\), deleting the unique extra-overlap vertex makes \(B\) bipartite.
- Larger \(d\) is impossible by (10).

Now suppose some child block \(B_j\) has defect at least five. There is at most one such child, and
\[
\sum_i\varepsilon(J_i)+5d\le1.
\]
In particular, \(d=0\).

Inductively \(B_j\) becomes bipartite after deleting a vertex \(p\). Every interface \(J_i\) is either a single edge, or the unique defect-one interface is a \(4\)-cycle or \(Q_3-v\). Here we used \(k\ge2\), which excludes \(J_i=Q_3-e\).

Thus \(J_j-p\), after discarding an empty edge if necessary, is connected: an edge leaves at least one endpoint, while the two possible larger interfaces are 2-vertex-connected.

A colouring of \(B_j-p\) can therefore be oriented to agree with the cube colouring on its surviving interface. All other blocks are bipartite and can be oriented in the same way. Since \(d=0\), the union minus \(p\) is bipartite.

This proves (iii).

### 2.4. Additions contained in one block

If all eleven old edges already lie in one block, its weight, vertex set and defect do not change. Properties (ii) and (iii) are preserved by Section 1.2. Thus this case is covered as well.

### 2.5. Merging complete cubes after saturation

After reaching \(K_n\), additionally permit merging all blocks meeting a complete cube.

For a merge of \(k\ge2\) blocks, the twelve cube edges are partitioned into nonempty proper subgraphs \(J_i\), and the corresponding calculation becomes
\[
D(B)=\sum_iD(B_i)+\sum_i\varepsilon(J_i)+5d+3.
\tag{11}
\]
Nonnegativity is preserved.

If \(D(B)\le6\), then \(d=0\), each child has defect at most three, and each \(J_i\) has defect at most three. Hence every child is bipartite and every interface is connected. The merged block is bipartite. Thus all of (8) remains valid.

Any two edges of \(K_n\) lie together in a cube when \(n\ge8\): this holds for both adjacent and disjoint pairs by embedding an appropriate pair of cube edges. Consequently these extra operations can merge all blocks into one.

The final block is \(K_n\), which is not apex-bipartite. Its defect is therefore at least seven:
\[
3e(F)-5n+7\ge7.
\]
This proves
\[
\boxed{w(n)\ge\left\lceil\frac{5n}{3}\right\rceil.}
\]

---

## 3. Checked upper-bound constructions

For completeness, the constructions needed for the claimed exact values and upper bound are given explicitly.

### 3.1. Three addition rules

**Absorption into a clique.** If a clique \(C\) has at least seven vertices and \(x\notin C\) has two neighbours in \(C\), then every remaining edge from \(x\) to \(C\) can be added. For a desired edge \(xr\), use \(x\), its two old neighbours, \(r\), and four further vertices of \(C\) as a cube.

**Absorption on one side.** Suppose all edges between \(A,B\) are present, with \(|A|\ge4\), \(|B|\ge3\). If \(x\) has two neighbours in \(A\), then all remaining \(xA\)-edges can be added. Use four vertices of \(A\), including the two old neighbours and the target, together with \(x\) and three vertices of \(B\), as a copy of \(K_{4,4}-M\).

**Internal stars.** Suppose \(K_{A,B}\) is present, \(|A|,|B|\ge4\), and the internal edges \(up,uq\) in \(A\) and \(br\) in \(B\) are present. Any missing internal edge \(bs\) can be added.

Choose
\[
a\in A\setminus\{u,p,q\},\qquad
t\in B\setminus\{b,r,s\}.
\]
The squares
\[
(u,p,r,b),\qquad(q,t,a,s)
\]
and matching edges
\[
uq,\quad pt,\quad ra,\quad bs
\]
form a cube with only \(bs\) missing.

It follows that
\[
K_{A,B}+P_3\text{ in }A+\text{an edge in }B
\tag{12}
\]
generates the complete graph on \(A\cup B\): first grow a spanning star in \(B\), then one in \(A\), and then fill both internal graphs.

### 3.2. A thirteen-edge seed for \(K_{5,4}\)

Let
\[
A_0=\{a_0,a_1,a_2,a_3\},\qquad
B=\{b_0,b_1,b_2,b_3\},
\]
and let
\[
Q=\{a_ib_j:i\ne j\}.
\]
Introduce \(z\), put \(A=A_0\cup\{z\}\), and start with
\[
(Q-a_0b_1)\cup\{zb_0,zb_1\}.
\tag{13}
\]
This has thirteen edges.

First restore \(a_0b_1\). Next add \(zb_2\) and \(zb_3\), using cubes obtained by replacing \(a_3\) and \(a_2\), respectively, by \(z\).

Add \(a_0b_0\) using the cube on \(\{a_0,a_2,a_3,z\}\cup B\) whose omitted perfect matching is
\[
\{a_2b_2,a_3b_3,a_0b_1,zb_0\}.
\]
Finally, for \(i=1,2,3\), add \(a_ib_i\) using
\[
Q-\{a_0b_i,a_ib_0\}+\{a_0b_0,a_ib_i\}.
\]
Thus all of \(K_{A,B}\) is generated.

Adding two adjacent edges inside \(A\) and one edge inside \(B\), then using (12), proves
\[
w(9)\le16.
\tag{14}
\]
Clique absorption also gives \(w(10)\le18\).

### 3.3. Nineteen edges on eleven vertices

Start with (13), introduce \(x,y\), and include the six additional edges
\[
a_0a_1,\quad b_1b_2,\quad
xa_0,\quad xb_0,\quad
yb_1,\quad ya_2.
\tag{15}
\]
There are nineteen initial edges.

First generate \(K_{A,B}\). The next three additions are certified by cubes with common first square
\[
(x,a_0,b_1,y)
\]
and the following second squares and matching edges:
\[
\begin{array}{c|c|c}
\text{edge added}&\text{second square}&\text{matching edges}\\ \hline
xy&(b_0,a_1,b_2,a_2)&xb_0,\ a_0a_1,\ b_1b_2,\ ya_2\\
ya_3&(b_0,a_1,b_2,a_3)&xb_0,\ a_0a_1,\ b_1b_2,\ ya_3\\
xb_3&(b_3,a_1,b_2,a_2)&xb_3,\ a_0a_1,\ b_1b_2,\ ya_2
\end{array}
\]
In each row, only the indicated added edge is missing.

Now \(y\) has two neighbours in \(A\), and \(x\) has two neighbours in \(B\). One-side absorption fills \(yA\) and \(xB\).

The graph now contains all crossing edges between
\[
A'=A\cup\{x\},\qquad B'=B\cup\{y\},
\]
and the internal paths
\[
a_1-a_0-x,\qquad b_2-b_1-y.
\]
Rule (12) completes the clique. Therefore \(w(11)\le19\). Combining this with (1),
\[
\boxed{w(11)=19.}
\]

### 3.4. Four vertices for seven edges

Suppose a seed generates a clique \(C\) of order at least seven. Add four vertices \(u_0,u_1,u_2,u_3\) with initial edges

- the path \(u_0u_1u_2u_3\);
- \(u_ic_i\) for four distinct vertices \(c_i\in C\).

The cost is seven edges.

After completing \(C\), add \(u_3u_0\), using the two squares
\[
(u_0,u_1,u_2,u_3),\qquad(c_0,c_1,c_2,c_3)
\]
and their matching.

Choose \(z\in C\setminus\{c_0,c_1,c_2,c_3\}\). Each \(u_iz\) can then be added by replacing \(c_i\) by \(z\) in the inner square. Every new vertex now has two neighbours in \(C\), so clique absorption finishes.

Starting from the eleven-vertex seed, write \(n=11+4q+r\), where \(0\le r\le3\). Use \(q\) such gadgets and \(r\) two-edge single-vertex extensions. The edge count is
\[
19+7q+2r
=\left\lceil\frac{7n-1}{4}\right\rceil.
\]

---

## 4. The exact value on nine vertices

It remains to prove \(w(9)\ge16\).

Suppose that \(F\) is weakly cube-saturated in \(K_9\) and has at most fifteen edges. Every vertex of \(F\) has degree at least two: otherwise its first new incident edge could not complete a cubic graph.

Immediately after the first addition, the graph contains a cube \(Q\) on eight vertices and at most four extra edges. Let \(z\) be the remaining vertex, let \(L,R\) be the bipartition of \(Q\), and let \(d=\deg(z)\). Thus \(2\le d\le4\).

### 4.1. Reduction to two configurations

If \(d\ge3\), place \(z\) on whichever side gives at most \(\lfloor d/2\rfloor\) internal incident edges. There are at most \(4-d\) other extra edges, so the total number of internal edges is at most
\[
\lfloor d/2\rfloor+4-d\le2.
\]
The cut obstruction applies.

If \(d=2\) and both neighbours of \(z\) lie in the same part of \(Q\), put \(z\) in the other part. Again there are at most two internal edges.

Thus \(z\) has neighbours
\[
a\in L,\qquad b\in R.
\]
If at most one of the other extra edges is internal to \(L\) or \(R\), there is again a cut with at most two internal edges.

The only remaining configurations are therefore
\[
Q+za+zb+e_1+e_2,
\tag{16}
\]
where \(e_1,e_2\) are internal edges on the original eight vertices.

### 4.2. A next addition must meet \(z\)

No cube containing \(z\) can witness an edge not incident with \(z\), since \(z\) currently has degree two.

A cube avoiding \(z\) would be spanning on the original eight vertices. In a balanced \(4\)-by-\(4\) cut, the internal edge counts in the two parts are equal. By (6), a nonzero internal edge count is therefore at least four.

Such a witness cannot use any internal edges: even after adding a new internal edge there are at most three available.

Nor can a new crossing edge be added using only crossing edges. The crossing graph is \(Q\), and a cubic spanning graph plus one nonedge has no different cubic spanning subgraph containing that nonedge. All old edges are forced by the unchanged degrees of vertices other than its endpoints.

Hence every possible next addition must be \(zt\).

For a cube with \(r\) vertices in \(L\cup\{z\}\), let \(i_L,i_R\) be its internal edge counts. Cubicity gives
\[
i_L-i_R=3(r-4).
\tag{17}
\]
Here \(r\) is either four or five.

### 4.3. Both extra edges in one part

By symmetry, suppose \(e_1,e_2\subseteq L\), and put \(z\) on the \(L\)-side.

First consider adding \(zt\) with \(t\in L\). The witnessing cube must use both internal edges \(za,zt\).

- If \(r=4\), (17) requires \(i_L=i_R=0\), impossible.
- If \(r=5\), it requires \(i_L=3\), \(i_R=0\). These three internal edges form a star. Since \(za,zt\) share \(z\), that star would have to be centred at \(z\), but \(z\) has only two internal neighbours after the addition.

Now consider \(t\in R\). The edge \(za\) is mandatory in the witness, so its internal edge set is nonempty. The only available internal edges are \(za,e_1,e_2\). They must form a three-edge star.

This is possible only if both \(e_1,e_2\) meet \(a\). But then deleting \(a\) makes (16) bipartite, so the entire graph is apex-bipartite and cannot percolate.

Thus this case cannot yield a weakly saturated graph.

### 4.4. One extra edge in each part

Now let \(e_1\subseteq L\), \(e_2\subseteq R\), again putting \(z\) on the \(L\)-side.

If \(t\in R\), the added edge is crossing. Any witnessing cube must use \(za\), but the available internal edges consist of two on the \(L\)-side and one on the \(R\)-side. They cannot form the required three-edge star in one part.

If \(t\in L\), the cube must use \(za,zt\), so \(i_L\ge2\), whereas \(i_R\le1\).

- For \(r=4\), this contradicts \(i_L=i_R\).
- For \(r=5\), the only possible counts are \(i_L=3,i_R=0\). As before, the required internal star would be centred at \(z\), which has only two internal neighbours.

So no next addition is possible.

All cases contradict weak saturation. Therefore \(w(9)\ge16\), and (14) proves
\[
\boxed{w(9)=16.}
\]

---

## 5. What remains open here

The argument does **not** determine the general function. Its asymptotic bounds remain
\[
\frac53n\le w(n)\le\frac74n+O(1).
\]
In particular, it does not establish the correct leading coefficient.

The strengthened invariant improves the previous lower bound by two or three edges, depending on \(n\bmod3\), and makes the nineteen-edge construction on eleven vertices optimal. The separate nine-vertex argument makes the sixteen-edge construction optimal as well.

For \(n<8\), trivially \(w(n)=\binom n2\), since no edge can be added using a cube. No computational assertions or external literature claims are used in the proofs above.