```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove DP-3-colorability when every block has at most seven triangles in the C4–C7-free case, or at most five triangles in the C4–C6-free case.",
  "would_publish": false,
  "caveats": "The unrestricted high-triangle blocks remain untreated, and I have not checked whether this bounded-triangle result is already in the literature."
}
```

## 1. Statement attacked

All graphs below are finite and simple. Write \(C_4\text{--}C_s\)-free for having no cycle of any length \(4,\ldots,s\).

The two questions are whether every planar

1. \(C_4\text{--}C_7\)-free graph is 3-choosable; and
2. \(C_4\text{--}C_6\)-free graph is 3-choosable, or even 3-colorable.

I do not resolve either question. I prove the following special case, in the stronger correspondence-coloring sense.

### Theorem 1

Let \(G\) be planar.

1. If \(G\) is \(C_4\text{--}C_6\)-free and every block of \(G\) contains at most five triangles, then \(G\) is DP-3-colorable.
2. If \(G\) is \(C_4\text{--}C_7\)-free and every block of \(G\) contains at most seven triangles, then \(G\) is DP-3-colorable.

In fact, for every specified vertex \(r\), there is an ordering
\[
v_1,\ldots,v_{n-1},r
\]
such that \(v_i\) has at most two neighbors among
\(\{v_{i+1},\ldots,v_{n-1},r\}\). Thus any prescribed permissible color at \(r\) extends to a list coloring, and also to a DP-coloring.

Consequently, a counterexample to the first question must have a block containing at least eight triangles, while a counterexample to the second must have a block containing at least six triangles.

---

## 2. A small auxiliary planar fact

We use the following elementary observation.

### Lemma 2

There is no simple planar triangle-free graph with either

- five vertices and seven edges, or
- seven vertices, ten edges, and degree sequence
  \[
  3,3,3,3,3,3,2.
  \]

#### Proof

The first assertion follows from the planar triangle-free bound
\[
m\le 2n-4.
\]

For the second, suppose \(Q\) were such a graph. Then
\[
m=10=2\cdot 7-4.
\]
Equality in the triangle-free planar bound forces \(Q\) to be a quadrangulation. For completeness, this also follows blockwise: if \(a\) is the number of cyclic blocks and \(b\) the number of bridge blocks, then
\[
m\le 2(n-1)-2a-b.
\]
Since \(Q\) has minimum degree two and contains a cycle, \(a\ge1\); equality \(m=2n-4\) therefore forces \(a=1\) and \(b=0\). Hence \(Q\) is 2-connected and all its faces have length four.

Thus \(Q\) is bipartite. In a bipartite graph each bipartition class has degree sum \(m=10\), but no subset of
\[
\{3,3,3,3,3,3,2\}
\]
sums to ten. Indeed, neither \(3a=10\) nor \(3a+2=10\) has an integral solution. This is a contradiction. ∎

---

## 3. The local low-degree lemma

The main point is the following rooted strengthening of a degree-two conclusion.

### Lemma 3

Let \(B\) be a 2-connected planar graph and let \(r\in V(B)\).

1. If \(B\) is \(C_4\text{--}C_6\)-free and has at most five triangles, then some vertex in \(V(B)\setminus\{r\}\) has degree at most two in \(B\).
2. If \(B\) is \(C_4\text{--}C_7\)-free and has at most seven triangles, then some vertex in \(V(B)\setminus\{r\}\) has degree at most two in \(B\).

#### Preliminary observations

Let \(n=|V(B)|\), \(m=|E(B)|\), and let \(t\) be the number of triangles of \(B\). Let \(U\) be the union of their vertex sets and put \(u=|U|\).

Because \(B\) has no 4-cycle, two distinct triangles cannot share an edge: two triangles \(abx\) and \(aby\) would give the 4-cycle
\[
xabyx.
\]
Consequently, if a vertex \(v\) lies in \(k(v)\) triangles, these triangles use \(2k(v)\) distinct edges at \(v\), and hence
\[
d(v)\ge 2k(v).
\]
Also,
\[
\sum_{v\in U} k(v)=3t.
\]

Assume, for contradiction, that
\[
d(v)\ge3\qquad\text{for all }v\ne r.
\]
Since \(B\) is 2-connected, \(d(r)\ge2\). Define the nonnegative integer
\[
x:=2m-(3n-1).
\]
At a non-root vertex in \(k\) triangles, its excess over the baseline degree three is at least \(k-1\); at the root, its excess over the baseline degree two is at least \(k-1\). Therefore
\[
x\ge \sum_{v\in U}(k(v)-1)=3t-u. \tag{1}
\]

Fix a plane embedding of \(B\). Unless \(B=K_3\), which is immediate, each face boundary is a cycle and each graph triangle bounds at most one face. Let \(q\le t\) be the number of triangular faces.

### The \(C_4\text{--}C_6\)-free case

Every nontriangular face has length at least seven, so
\[
2m\ge 3q+7(f-q)=7f-4q.
\]
Using \(f=m-n+2\) and \(q\le t\),
\[
5m\le 7n-14+4t. \tag{2}
\]
Since \(2m=3n-1+x\), (2) gives
\[
n+23+5x\le 8t. \tag{3}
\]
Combining (1) and (3),
\[
n+23+5(3t-u)\le8t,
\]
or
\[
n+23+7t\le5u.
\]
As \(n\ge u\) and \(u\le3t\),
\[
23+7t\le4u\le12t.
\]
Thus \(t\ge5\).

If \(t\le4\), this is already a contradiction. Suppose \(t=5\). Then
\[
58\le4u\le60,
\]
so \(u=15\). Hence the five triangles are pairwise vertex-disjoint. From (3),
\[
15\le n\le17.
\]

If \(n=16\), (3) forces \(x=0\), but then
\[
2m=3n-1=47,
\]
impossible. Thus \(n=15\) or \(17\), and in either case \(x=0\). Consequently \(r\) has degree two and every other vertex has degree three.

Contract each of the five vertex-disjoint triangles, deleting its three internal edges, and call the resulting planar multigraph \(Q\).

- If \(n=15\), then
  \[
  |V(Q)|=5,\qquad |E(Q)|=m-15=22-15=7.
  \]
- If \(n=17\), then
  \[
  |V(Q)|=7,\qquad |E(Q)|=25-15=10,
  \]
  and its degree sequence is \(3,3,3,3,3,3,2\).

In both cases \(Q\) is simple. Parallel edges between two contracted triangles would lift to a 4-cycle. Two edges from an uncontracted vertex to one contracted triangle would form a second triangle sharing an edge with the contracted triangle, again yielding a 4-cycle.

Moreover, \(Q\) is triangle-free. At each contracted triangle, the two edges of a triangle of \(Q\) use distinct attachment vertices, since every original triangle vertex has at most one edge leaving its triangle. Replacing each contracted node by the corresponding triangle edge lifts a triangle of \(Q\) to a cycle of length \(3+s\), where \(s\) is the number of contracted nodes on that triangle. For \(n=15\), \(s=3\), giving a 6-cycle. For \(n=17\), there are only two uncontracted vertices, so \(1\le s\le3\), giving a cycle of length \(4,5\), or \(6\). All are forbidden.

Both possibilities now contradict Lemma 2.

### The \(C_4\text{--}C_7\)-free case

Here every nontriangular face has length at least eight. Hence
\[
2m\ge8f-5q,
\]
and therefore
\[
6m\le8n-16+5t. \tag{4}
\]
Using \(2m=3n-1+x\), this becomes
\[
n+13+3x\le5t. \tag{5}
\]
Together with (1),
\[
n+13+3(3t-u)\le5t,
\]
so
\[
n+13+4t\le3u.
\]
Since \(n\ge u\) and \(u\le3t\),
\[
13+4t\le2u\le6t.
\]
Thus \(t\ge7\).

If \(t\le6\), this is a contradiction. If \(t=7\), then
\[
41\le2u\le42,
\]
so \(u=21\); the seven triangles are pairwise vertex-disjoint. Equation (5) gives
\[
21\le n\le22.
\]
For \(n=22\), (5) forces \(x=0\), but then \(2m=65\), impossible. Thus \(n=21\), \(x=0\), and the degrees are again one 2 and twenty 3's.

Contracting the seven triangles gives a planar graph \(Q\) on seven vertices and ten edges, with degree sequence
\[
3,3,3,3,3,3,2.
\]
Exactly as above, \(Q\) is simple, and every triangle of \(Q\) would lift to a 6-cycle in \(B\). Thus \(Q\) is triangle-free, contradicting Lemma 2. This proves Lemma 3. ∎

---

## 4. Passing from blocks to an ordering

We now prove Theorem 1.

Call an ordering
\[
v_1,\ldots,v_{n-1},r
\]
a rooted 2-degeneracy ordering if every \(v_i\) has at most two neighbors later in the ordering.

Consider any subgraph \(H\subseteq G\) containing \(r\). Every 2-connected block of \(H\) is contained in a block of \(G\), and hence satisfies the appropriate triangle bound.

Suppose first that \(H\) is connected and has at least two vertices.

- If \(H\) has only one block and it is 2-connected, apply Lemma 3 with root \(r\).
- If its only block is \(K_2\), the other endpoint has degree one.
- Otherwise choose an end block \(B\) of the block-cutvertex tree so that \(r\) is not a non-cutvertex of \(B\). Let \(z\) be the unique cutvertex through which \(B\) meets the rest of \(H\).
  - If \(B=K_2\), its non-cutvertex has degree one in \(H\).
  - Otherwise apply Lemma 3 to \(B\) with distinguished vertex \(z\). It gives \(v\ne z\) with \(d_B(v)\le2\). Since \(B\) is an end block, \(v\) has no neighbors outside \(B\), and hence \(d_H(v)\le2\). By the choice of \(B\), \(v\ne r\).

If \(H\) is disconnected, apply the same argument to a component not containing \(r\), or to the component containing \(r\) if all others have already been deleted.

Thus every nontrivial current subgraph has a non-root vertex of degree at most two. Repeated deletion yields a rooted 2-degeneracy ordering.

Given lists of size at least three and a prescribed color at \(r\), color in reverse order. Each new vertex has at most two already colored neighbors and therefore at least one available color. For a DP-assignment, each already colored neighbor forbids at most one element of the current three-element fiber, so the identical greedy argument works.

This proves Theorem 1. ∎

---

## 5. Further unconditional structural bounds

The following estimates hold without any bound on the number of triangles.

### Proposition 4: density and 4-choosability

If \(G\) is connected and \(C_4\text{--}C_6\)-free, then
\[
|E(G)|\le \frac{21}{11}\bigl(|V(G)|-1\bigr).
\]
If it is \(C_4\text{--}C_7\)-free, then
\[
|E(G)|\le \frac{24}{13}\bigl(|V(G)|-1\bigr).
\]

Consequently, both classes are 3-degenerate and therefore 4-DP-colorable.

#### Proof sketch

In a 2-connected block \(B\ne K_3\), two triangular faces cannot share an edge. Thus if \(q\) is the number of triangular faces, \(3q\le m\).

For the \(C_4\text{--}C_6\)-free case,
\[
2m\ge7f-4q\ge7f-\frac43m,
\]
which with Euler's formula gives
\[
m\le \frac{21}{11}(n-2).
\]
Similarly, in the \(C_4\text{--}C_7\)-free case,
\[
2m\ge8f-5q\ge8f-\frac53m,
\]
giving
\[
m\le\frac{24}{13}(n-2).
\]
Summing over blocks, with \(K_2\) and \(K_3\) handled separately, yields the stated connected bounds. Since both constants are less than two, every subgraph has a vertex of degree at most three. ∎

There is also a sharp triangle threshold for a 2-connected minimum-degree-three core.

### Proposition 5

Let \(B\) be 2-connected and planar.

1. If \(B\) is \(C_4\text{--}C_6\)-free and \(\delta(B)\ge3\), then \(B\) contains at least six triangles.
2. If \(B\) is \(C_4\text{--}C_7\)-free and \(\delta(B)\ge3\), then \(B\) contains at least eight triangles.
3. In the second assertion, equality at eight triangles forces \(B\) to be the graph of the truncated cube.

#### Proof

Let \(t\) be the number of triangles, let \(u\) be the number of vertices lying in triangles, and put
\[
h=2m-3n\ge0.
\]
As before, no two triangles share an edge, and
\[
h\ge 3t-u. \tag{6}
\]

For the \(C_4\text{--}C_6\)-free case, the face inequality is
\[
5m\le7n-14+4t.
\]
Substituting \(2m=3n+h\) gives
\[
n+5h\le8t-28.
\]
On the other hand, using (6),
\[
n+5h\ge u+5(3t-u)=15t-4u\ge3t.
\]
Hence \(3t\le8t-28\), so \(t\ge6\).

For the \(C_4\text{--}C_7\)-free case,
\[
6m\le8n-16+5t,
\]
and therefore
\[
n+3h\le5t-16.
\]
But
\[
n+3h\ge u+3(3t-u)=9t-2u\ge3t.
\]
Thus \(3t\le5t-16\), giving \(t\ge8\).

If \(t=8\), equality holds throughout. Hence \(u=n=24\), \(h=0\), the eight triangles are vertex-disjoint and cover all vertices, and \(B\) is cubic. Contracting the eight triangles gives a simple planar cubic triangle-free graph \(Q\) on eight vertices and twelve edges. Equality in \(m\le2n-4\) makes \(Q\) bipartite. Its bipartition has four vertices in each part, and a 3-regular bipartite graph with parts of size four is \(K_{4,4}\) minus a perfect matching, namely the cube. Expanding its vertices back into triangles gives the truncated cube. ∎

The truncated cube indeed has no cycles of lengths \(4,\ldots,7\): every cycle other than one of its eight replacement triangles projects to a closed trail in the cube using at least four cube edges, and between consecutive projected edges it uses at least one edge inside a replacement triangle. Its length is therefore at least eight.

Thus the threshold seven in Lemma 3 is sharp for obtaining a degree-two vertex: the truncated cube is cubic and has exactly eight triangles.

---

## 6. What remains open

The proof handles graphs whose blocks do not contain large triangle systems. It gives no coloring reduction for a block containing

- at least eight triangles in the \(C_4\text{--}C_7\)-free case, or
- at least six triangles in the \(C_4\text{--}C_6\)-free case.

Such blocks can have minimum degree three, so greedy deletion genuinely stops. The truncated cube shows this already at eight triangles for the first forbidden range, although that particular cubic graph is not a counterexample.

Therefore neither original conjecture is proved or disproved here. The remaining issue is to color or reduce these high-triangle, minimum-degree-three cores; the face-counting argument alone cannot do so.