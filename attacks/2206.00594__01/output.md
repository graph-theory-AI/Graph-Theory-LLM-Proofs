```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is equivalent to its K_{2,2}-free, and even arbitrarily high-girth, case, and it holds for bounded-chordality graphs and proper subdivisions, but the high-girth core remains unresolved.",
  "would_publish": false,
  "caveats": "No twin-width bound or unbounded-twin-width construction is obtained for the C4-free high-girth core."
}
```

# 1. Statement and summary

Let \(\mathcal C_{t,k}\) be the class of graphs which

1. contain no \(K_{t,t}\) as a subgraph, and
2. contain no \(k\) vertex-disjoint cycles with no edges between distinct cycles.

The question is whether \(\mathcal C_{t,k}\) has bounded twin-width for every fixed \(t,k\).

I do not resolve this. I prove:

- a quantitative bound on the packing number of bounded-length cycles;
- every graph in \(\mathcal C_{t,k}\) can be made arbitrarily high-girth by deleting a bounded number of vertices;
- consequently, the full question is equivalent to the case \(t=2\), and also to its restriction to graphs of any prescribed fixed girth;
- the conjecture holds if induced-cycle length is bounded;
- the conjecture holds for graphs in which every edge has an endpoint of degree at most \(2\), including proper subdivisions.

The remaining case is therefore already present among \(C_4\)-free graphs of arbitrarily large girth and unbounded induced-cycle length.

Throughout, all graphs are finite and simple. If the definition of \(\mathcal O_k\) requires the individual cycles to be induced, the arguments are unchanged: inside the vertex set of any cycle one may choose a shortest, hence induced, cycle.

# 2. Bounded packing of short cycles

We use the standard extremal estimate
\[
\operatorname{ex}(n,K_{t,t})\le c_t n^{2-1/t}
\tag{2.1}
\]
for a constant \(c_t\) depending only on \(t\).

## Proposition 2.1

Fix \(t,k\ge 2\) and \(L\ge 3\). There is a constant
\[
M_{t,k}(L)=O_{t,k}\!\left(L^{2t-1}\right)
\]
such that every graph \(G\in\mathcal C_{t,k}\) contains at most \(M_{t,k}(L)\) pairwise vertex-disjoint cycles of length at most \(L\).

One may take, for example,
\[
M_{t,k}(L)=
\max\left\{
2(k-1),
\left\lceil [4(k-1)c_t]^t L^{2t-1}\right\rceil
\right\}.
\tag{2.2}
\]

### Proof

Let \(C_1,\dots,C_m\) be vertex-disjoint cycles, each of length at most \(L\). Define an auxiliary graph \(Q\) on \([m]\) by declaring
\[
ij\in E(Q)
\quad\Longleftrightarrow\quad
E_G(V(C_i),V(C_j))\ne\varnothing.
\]

Since \(G\) is \(\mathcal O_k\)-free, \(Q\) has no independent set of size \(k\). Thus \(\overline Q\) is \(K_k\)-free. By Turán's theorem,
\[
e(Q)\ge \frac{m^2}{2(k-1)}-\frac m2.
\]
In particular, if \(m\ge 2(k-1)\), then
\[
e(Q)\ge \frac{m^2}{4(k-1)}.
\tag{2.3}
\]

Let
\[
U=\bigcup_{i=1}^m V(C_i).
\]
Then \(|U|\le Lm\). Every edge of \(Q\) is witnessed by a distinct edge of \(G[U]\) joining the corresponding two cycle vertex sets. Hence
\[
e(Q)\le e(G[U]).
\]
Since \(G[U]\) is \(K_{t,t}\)-free, (2.1) gives
\[
e(Q)\le c_t(Lm)^{2-1/t}.
\tag{2.4}
\]
Combining (2.3) and (2.4),
\[
\frac{m^2}{4(k-1)}
 \le c_t L^{2-1/t}m^{2-1/t},
\]
and therefore
\[
m^{1/t}\le 4(k-1)c_tL^{2-1/t}.
\]
Raising to the \(t\)-th power gives
\[
m\le [4(k-1)c_t]^tL^{2t-1}.
\]
This proves the claim. \(\square\)

## Corollary 2.2: bounded short-cycle transversal

For every \(G\in\mathcal C_{t,k}\) and every fixed \(L\ge3\), there is a set
\[
X\subseteq V(G),\qquad
|X|\le R_{t,k}(L):=L M_{t,k}(L)
 =O_{t,k}(L^{2t}),
\tag{2.5}
\]
such that \(G-X\) has no cycle of length at most \(L\).

### Proof

Take a maximal family of pairwise vertex-disjoint cycles of length at most \(L\), and let \(X\) be the union of their vertex sets. Proposition 2.1 bounds the number of cycles. By maximality, every cycle of length at most \(L\) intersects \(X\). \(\square\)

Thus every graph under consideration differs by a bounded number of vertices from a graph of arbitrarily prescribed fixed girth.

# 3. Adding finitely many arbitrary vertices preserves bounded twin-width

For the reductions below, one needs the fact that deleting a bounded set cannot hide unbounded twin-width.

## Lemma 3.1

Let \(X\subseteq V(G)\), \(|X|=r\), and put \(H=G-X\). Then
\[
\operatorname{tww}(G)
 \le \Psi_r(\operatorname{tww}(H)),
\qquad
\Psi_r(d):=2^r(3d+4)+r.
\tag{3.1}
\]

The bound is deliberately non-optimized.

### Proof

Use the partition formulation of twin-width: a pair of parts is red when the adjacency between them in the original graph is neither complete nor empty.

Let \(d=\operatorname{tww}(H)\), and fix a \(d\)-contraction sequence of \(H\). Give every vertex \(v\in H\) its type
\[
\sigma(v)=N_G(v)\cap X.
\]
There are at most \(q=2^r\) types.

At each stage of the contraction sequence of \(H\), replace every current part \(P\) by its nonempty type pieces
\[
P_\sigma=\{v\in P:\sigma(v)=\sigma\}.
\]
This refined sequence can be realized by mergers: when the original sequence merges \(A\) and \(B\), merge \(A_\sigma\) with \(B_\sigma\), separately for every \(\sigma\).

At a stable refined stage, a piece \(P_\sigma\) can have mixed adjacency to pieces arising from at most \(d\) other original parts, with at most \(q\) type pieces in each, and to at most \(q-1\) other pieces of \(P\).

During the simulation of one original merger \(A,B\mapsto A\cup B\), a mixed adjacency involving one of the partially merged pieces can only arise from:

- an old red neighbor of \(A\);
- an old red neighbor of \(B\);
- a new red neighbor of \(A\cup B\); or
- one of the at most \(2q\) pieces currently arising from \(A\) and \(B\).

Thus the red degree is at most
\[
q(3d+2)
\]
during these intermediate steps. Moreover, every type piece has homogeneous adjacency to each vertex of \(X\), so no red edge to \(X\) is created at this stage.

After the original sequence has contracted \(H\) to one part, at most \(q\) type pieces remain. Merge these arbitrarily, and then merge the vertices of \(X\). During this last phase there are at most \(q+r\) parts. The bound in (3.1) dominates all the preceding estimates. \(\square\)

Consequently, for fixed \(r\), a class obtained by adding at most \(r\) arbitrary vertices to a bounded-twin-width class still has bounded twin-width.

# 4. Reduction of the entire problem to \(t=2\)

Recall that excluding \(K_{2,2}\) as a subgraph is exactly excluding a \(4\)-cycle as a not-necessarily-induced subgraph.

## Theorem 4.1

For every fixed \(k\), the following are equivalent.

1. For every \(t\), the class \(\mathcal C_{t,k}\) has bounded twin-width.
2. The class of \(K_{2,2}\)-free, \(\mathcal O_k\)-free graphs has bounded twin-width.
3. For some fixed \(L\ge4\), the class of all \(\mathcal O_k\)-free graphs of girth greater than \(L\) has bounded twin-width.
4. For every fixed \(L\ge4\), the class of all \(\mathcal O_k\)-free graphs of girth greater than \(L\) has bounded twin-width.

### Proof

The implications \(1\Rightarrow2\) and \(2\Rightarrow4\Rightarrow3\) are immediate, since a graph of girth greater than \(4\) is \(K_{2,2}\)-free.

Suppose 2 holds, with twin-width bound \(d_k\). Let \(G\in\mathcal C_{t,k}\). Apply Corollary 2.2 with \(L=4\), obtaining
\[
|X|\le R_{t,k}(4)
\]
such that \(G-X\) has girth greater than \(4\). In particular, \(G-X\) is \(K_{2,2}\)-free and remains \(\mathcal O_k\)-free. Hence
\[
\operatorname{tww}(G-X)\le d_k.
\]
Lemma 3.1 gives
\[
\operatorname{tww}(G)
 \le \Psi_{R_{t,k}(4)}(d_k).
\]
Thus 2 implies 1.

Finally, suppose 3 holds for some \(L\ge4\). Let \(G\) be \(K_{2,2}\)-free and \(\mathcal O_k\)-free. Apply Corollary 2.2 with \(t=2\) and this \(L\). Deleting at most \(R_{2,k}(L)\) vertices leaves a graph of girth greater than \(L\), whose twin-width is bounded by assumption. Lemma 3.1 then bounds the twin-width of \(G\). Hence 3 implies 2. \(\square\)

In particular:

> A counterexample for any fixed \(t\ge2,k\) would yield, after deleting a bounded number of vertices from each graph, a counterexample with \(t=2\), and even with arbitrarily large prescribed girth.

Conversely, proving the conjecture only for \(K_{2,2}\)-free graphs would settle it for every \(t\).

# 5. Positive special cases

## 5.1. Bounded chordality

Call the chordality of \(G\) the maximum length of an induced cycle in \(G\), with forests having no induced cycle.

## Theorem 5.1

For every fixed \(t,k,L\), the class of \(K_{t,t}\)-free, \(\mathcal O_k\)-free graphs of chordality at most \(L\) has bounded twin-width.

More explicitly,
\[
\operatorname{tww}(G)
 \le \Psi_{R_{t,k}(L)}(2).
\tag{5.1}
\]

### Proof

Use Corollary 2.2 to find \(X\) with
\[
|X|\le R_{t,k}(L)
\]
such that \(G-X\) has no cycle of length at most \(L\).

If \(G-X\) contained any cycle, a shortest such cycle would be induced. It would therefore be an induced cycle of \(G\) of length greater than \(L\), contrary to the chordality assumption. Thus \(G-X\) is a forest.

Forests have twin-width at most \(2\), so Lemma 3.1 gives (5.1). \(\square\)

This includes, for example, chordal graphs and any class with a uniform bound on hole length.

## 5.2. Proper subdivisions

The usual subdivision-based candidates for unbounded sparse twin-width cannot directly yield a counterexample here.

## Proposition 5.2

Suppose every edge of \(G\) has at least one endpoint of degree at most \(2\). If \(G\) is \(\mathcal O_k\)-free, then \(G\) has bounded feedback vertex set and hence bounded twin-width as a function of \(k\) alone.

In particular, this applies when \(G\) is obtained from an arbitrary graph by subdividing every edge at least once.

### Proof

First observe that any two vertex-disjoint cycles in \(G\) are automatically nonadjacent. Indeed, suppose \(uv\) joined two vertex-disjoint cycles. At least one endpoint, say \(u\), has degree at most \(2\). But \(u\) lies on one of the cycles, whose two cycle edges already exhaust its incident edges. Therefore \(uv\) cannot leave that cycle.

It follows that \(G\) has no \(k\) vertex-disjoint cycles at all. By the classical Erdős–Pósa theorem for cycles, there is a function \(p(k)=O(k\log k)\) and a set
\[
X\subseteq V(G),\qquad |X|\le p(k),
\]
meeting every cycle. Thus \(G-X\) is a forest. Lemma 3.1 gives
\[
\operatorname{tww}(G)\le \Psi_{p(k)}(2).
\]
For a proper subdivision, every edge has an internal degree-\(2\) endpoint, so the hypothesis applies. \(\square\)

The same argument applies to bipartite graphs having a bipartition class of maximum degree at most \(2\).

## 5.3. Trivial parameter cases

- If \(k=1\), then \(\mathcal O_1\)-free means acyclic, so twin-width is at most \(2\).
- If \(t=1\), then excluding \(K_{1,1}\) means the graph is edgeless.

# 6. Consequence for the source lower-bound construction

The source paper supplies an infinite family \(G_n\) which is

- \(\mathcal O_2\)-free,
- \(K_{2,3}\)-free, hence \(K_{3,3}\)-free, and
- of unbounded treewidth.

Fix any \(L\). Applying Corollary 2.2 with \(t=3\) and \(k=2\), there are sets \(X_n\) of uniformly bounded size such that
\[
H_n:=G_n-X_n
\]
has girth greater than \(L\).

Moreover,
\[
\operatorname{tw}(G_n)
 \le \operatorname{tw}(H_n)+|X_n|,
\]
because a tree decomposition of \(H_n\) can be extended by putting \(X_n\) into every bag. Hence \(\operatorname{tw}(H_n)\) is still unbounded.

Therefore:

> For every fixed \(L\), there are \(\mathcal O_2\)-free graphs of girth greater than \(L\) and unbounded treewidth.

Thus neither the reduction to \(t=2\) nor the reduction to high girth can be completed by proving bounded treewidth. This also explains precisely why the source lower-bound family does not by itself disprove the twin-width conjecture: unbounded treewidth does not imply unbounded twin-width.

# 7. Remaining gap

By Theorem 4.1, the unresolved core is:

> Are \(C_4\)-free \(\mathcal O_k\)-free graphs of bounded twin-width as a function of \(k\)?

Equivalently, one may impose any fixed lower bound on the girth. The arguments above provide no control over interactions among very long cycles. Such interactions can support unbounded feedback vertex set and unbounded treewidth while all short-cycle packings remain bounded.

To disprove the conjecture, it would now suffice to exhibit, for some fixed \(k\), a sequence of \(C_4\)-free—or arbitrarily high-girth—\(\mathcal O_k\)-free graphs of unbounded twin-width. To prove it, it suffices to handle this \(t=2\) core. No such twin-width lower bound or contraction sequence is established here.