```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not settled; I prove qn(G) <= 3k-2 for layered pathwidth k and qn(G) <= 3p+1 when a width-one layered tree decomposition has an index tree of pathwidth p.",
  "would_publish": false,
  "caveats": "The bound still depends on an auxiliary pathwidth parameter, and no counterexample or constant bound for arbitrary decomposition trees is obtained."
}
```

# Mathematical writeup

## 1. Statement and outcome

The problem asks whether, for every fixed \(k\), there is a constant \(Q(k)\) such that every graph of layered treewidth at most \(k\) has queue-number at most \(Q(k)\).

The reduction reported in the prompt shows that it is enough to treat layered treewidth \(1\). I do not resolve that case. I give:

1. an exact reduction, up to a factor \(2\), to queue layouts respecting the given layering;
2. the bound
   \[
   \operatorname{qn}(G)\le 3k-2
   \]
   for graphs of layered pathwidth \(k\);
3. consequently, if a layered-width-\(k\) tree decomposition is indexed by a tree of pathwidth \(p\), then
   \[
   \operatorname{qn}(G)\le 3k(p+1)-2;
   \]
   in particular, for layered width \(1\),
   \[
   \operatorname{qn}(G)\le 3p+1;
   \]
4. the sharper bound \(3\) when the decomposition tree is a star;
5. a concrete obstruction showing why one cannot simply order the layers successively, even though every consecutive two-layer graph is a forest.

These results do not remove the dependence on \(p\), which is the unresolved point.

---

## 2. Width-one layered decompositions as subtree models

Fix a layering
\[
\mathcal L=(L_0,L_1,\dots,L_h)
\]
of \(G\), so every edge has both ends in one layer or in two consecutive layers.

Let \((T,\{B_x:x\in V(T)\})\) be a tree decomposition. For each \(v\in V(G)\), define
\[
S_v:=\{x\in V(T):v\in B_x\}.
\]
Then \(S_v\) is a nonempty connected subtree of \(T\), and if \(uv\in E(G)\), then
\[
S_u\cap S_v\neq\varnothing.
\]

If the decomposition has layered width \(1\), then for distinct \(u,v\in L_i\),
\[
S_u\cap S_v=\varnothing.
\]
Conversely, any such family of subtrees, with same-layer subtrees pairwise disjoint and with every graph edge represented by an intersection, defines a layered-width-one tree decomposition.

Two immediate consequences are useful.

### 2.1 There are no same-layer edges

If \(u,v\in L_i\) and \(uv\in E(G)\), some bag contains both \(u\) and \(v\), contradicting layered width \(1\). Hence every edge joins consecutive layers.

### 2.2 Every two consecutive layers induce a forest

More generally, if a layered-width-\(k\) tree decomposition is restricted to \(r\) consecutive layers, every restricted bag has size at most \(kr\). Thus
\[
\operatorname{tw}\bigl(G[L_i\cup\cdots\cup L_{i+r-1}]\bigr)\le kr-1.
\]
For \(k=1\) and \(r=2\),
\[
\operatorname{tw}(G[L_i\cup L_{i+1}])\le 1,
\]
so \(G[L_i\cup L_{i+1}]\) is a forest.

The difficult point is therefore not any individual consecutive-layer forest, but finding compatible vertex orders for all these forests simultaneously.

---

## 3. It suffices, up to a factor two, to respect the layering

For a fixed independent layering \(\mathcal L\), let
\(\operatorname{lqn}_{\mathcal L}(G)\) denote the minimum number of queues in a layout whose vertex order is
\[
L_0<L_1<\cdots<L_h,
\]
with an arbitrary order inside each layer.

### Lemma 3.1
If every edge of \(G\) joins consecutive layers, then
\[
\operatorname{qn}(G)\le
\operatorname{lqn}_{\mathcal L}(G)
\le 2\operatorname{qn}(G).
\]

#### Proof

The first inequality is immediate.

Take a \(q\)-queue layout with vertex order \(\prec\). Form a new order \(\prec_{\mathcal L}\) by putting the layers consecutively and preserving the old order within each layer.

For an edge \(uv\), where \(u\in L_i\) and \(v\in L_{i+1}\), retain its old queue and add one bit recording whether
\[
u\prec v \qquad\text{or}\qquad v\prec u.
\]
This gives \(2q\) classes.

Suppose two independent edges \(uv\) and \(xy\), both between \(L_i\) and \(L_{i+1}\), are nested in the new order. Relabel them so that
\[
u\prec_{\mathcal L}x\prec_{\mathcal L}y\prec_{\mathcal L}v,
\]
where \(u,x\in L_i\) and \(v,y\in L_{i+1}\). Since within-layer orders were preserved,
\[
u\prec x,\qquad y\prec v.
\]

If both edges are forward in the old order, then
\[
u\prec x\prec y\prec v,
\]
so \(uv\) nests \(xy\) in the old layout.

If both are backward, then
\[
y\prec v\prec u\prec x,
\]
so \(xy\) nests \(uv\) in the old layout.

Thus two edges in the same new class cannot nest. Edges belonging to different consecutive layer pairs cannot nest in a layer-respecting order. Therefore the new layout has at most \(2q\) queues. ∎

Consequently, a counterexample may be sought among layer-respecting layouts: unbounded layer-respecting queue-number would imply unbounded ordinary queue-number.

For fixed orders of the layers, the nesting relation on edges is strict interval containment and hence a partial order. By Mirsky's theorem, the minimum number of queues for that fixed vertex order equals the largest size of a rainbow, that is, a set of pairwise nested edges.

---

## 4. A linear bound for layered pathwidth

The following is the main positive partial result.

### Theorem 4.1
If \(G\) has layered pathwidth at most \(k\), then
\[
\operatorname{qn}(G)\le 3k-2.
\]

In particular, every graph of layered pathwidth \(1\) has queue-number at most \(1\).

### Proof

Fix a layering \((L_0,\dots,L_h)\) and a path decomposition of layered width \(k\). Let \(I_v\) be the interval of path-decomposition nodes whose bags contain \(v\).

For each fixed layer \(L_i\), at most \(k\) of the intervals \(\{I_v:v\in L_i\}\) contain any one point. Hence these intervals can be colored with colors
\[
1,\dots,k
\]
so that intervals of the same color are pairwise disjoint. This is the standard greedy coloring of an interval graph.

Inside each layer \(L_i\), order the vertices first by color and then, among vertices of the same color, by increasing left endpoint of \(I_v\). Finally, concatenate the layers in increasing order.

We use the following elementary interval observation.

#### Interval reversal observation

Suppose \(I_u,I_x\) are disjoint with \(I_u\) to the left of \(I_x\), and \(I_y,I_v\) are disjoint with \(I_y\) to the left of \(I_v\). It is impossible to have both
\[
I_u\cap I_v\neq\varnothing
\quad\text{and}\quad
I_x\cap I_y\neq\varnothing.
\]
Indeed, writing \(\ell(I)\) and \(r(I)\) for the endpoints, these assumptions would give
\[
\ell(I_x)\le r(I_y)<\ell(I_v)\le r(I_u)<\ell(I_x),
\]
a contradiction.

We now define the queues.

### Edges between consecutive layers

For \(uv\), with \(u\in L_i\), \(v\in L_{i+1}\), let
\[
a=\operatorname{col}(u),\qquad b=\operatorname{col}(v),
\]
and put \(uv\) into queue
\[
V_{b-a}.
\]
There are \(2k-1\) possible differences.

Suppose two edges \(uv\) and \(xy\) in the same \(V_\delta\) are nested, with
\[
u<x<y<v,
\]
where \(u,x\in L_i\) and \(v,y\in L_{i+1}\). Set
\[
a=\operatorname{col}(u),\quad
c=\operatorname{col}(x),\quad
d=\operatorname{col}(y),\quad
b=\operatorname{col}(v).
\]
The vertex order gives \(a\le c\) and \(d\le b\), while equality of queue indices gives
\[
b-a=d-c.
\]
Therefore
\[
(c-a)+(b-d)=0,
\]
and hence \(a=c\) and \(b=d\).

Thus \(I_u\) lies to the left of \(I_x\), while \(I_y\) lies to the left of \(I_v\). But the two graph edges imply
\[
I_u\cap I_v\neq\varnothing,\qquad
I_x\cap I_y\neq\varnothing,
\]
contradicting the interval reversal observation.

Edges from distinct consecutive layer pairs cannot nest in a layer-respecting order. Thus every \(V_\delta\) is a queue.

### Edges inside one layer

If \(uv\) is an edge inside a layer, then \(I_u\cap I_v\neq\varnothing\), so \(u\) and \(v\) have different colors. Orient the notation so that
\[
a=\operatorname{col}(u)<\operatorname{col}(v)=b,
\]
and put \(uv\) into queue
\[
H_{b-a}.
\]
There are \(k-1\) possible positive differences.

Suppose \(uv\) and \(xy\) in the same \(H_\delta\) are nested:
\[
u<x<y<v.
\]
Let their color pairs be \((a,b)\) and \((c,d)\). Then
\[
a\le c<d\le b
\]
and
\[
b-a=d-c.
\]
Again,
\[
(c-a)+(b-d)=0,
\]
so \(a=c\) and \(b=d\). The same interval reversal contradiction applies.

Edges lying inside different layers cannot nest. We use disjoint names for the \(H\)- and \(V\)-queues, so no interaction between the two types has to be considered.

The total number of queues is
\[
(2k-1)+(k-1)=3k-2.
\]
∎

For \(k=1\), there are no same-layer edges and all inter-layer edges lie in the single queue \(V_0\).

---

## 5. A bound in terms of the pathwidth of the decomposition tree

### Theorem 5.1
Suppose \(G\) has a layered-width-\(k\) tree decomposition indexed by a tree \(T\), and
\[
\operatorname{pw}(T)=p.
\]
Then
\[
\operatorname{qn}(G)\le 3k(p+1)-2.
\]

#### Proof

Let
\[
(X_1,\dots,X_s)
\]
be a path decomposition of \(T\) of width \(p\), so \(|X_j|\le p+1\).

For each \(j\), define
\[
Y_j:=\{v\in V(G):S_v\cap X_j\neq\varnothing\},
\]
where \(S_v\) is the occurrence subtree of \(v\) in the original tree decomposition.

The bags \(Y_1,\dots,Y_s\) form a path decomposition of \(G\):

- If \(uv\in E(G)\), then \(S_u\cap S_v\neq\varnothing\). Any path-decomposition bag \(X_j\) containing a node of this intersection gives \(u,v\in Y_j\).
- For fixed \(v\), the set of indices \(j\) for which \(S_v\cap X_j\neq\varnothing\) is an interval. Indeed, each tree node has an interval of occurrences in the path decomposition of \(T\), and intervals belonging to adjacent nodes of the connected subtree \(S_v\) overlap.

For a fixed graph layer \(L_i\),
\[
|Y_j\cap L_i|
 \le \sum_{x\in X_j}|B_x\cap L_i|
 \le k|X_j|
 \le k(p+1).
\]
Thus \(G\) has layered pathwidth at most \(k(p+1)\). Theorem 4.1 gives
\[
\operatorname{qn}(G)
 \le 3k(p+1)-2.
\]
∎

For layered width \(1\), this gives
\[
\operatorname{qn}(G)\le 3p+1.
\]

Consequences include:

- if the decomposition tree is itself a path, then Theorem 4.1 directly gives queue-number \(1\) in the width-one case;
- if the decomposition tree is a caterpillar, then \(p\le1\), giving queue-number at most \(4\).

### Relation to the known logarithmic bound

A witness decomposition can be normalized to have at most \(n\) index nodes. Indeed, the intersection graph of the occurrence subtrees \(S_v\) is chordal; its maximal cliques are contained in original bags by the Helly property for subtrees of a tree. A clique-tree decomposition therefore preserves the layered-width bound and has at most \(n\) bags.

Every \(N\)-vertex tree has pathwidth at most \(\lceil\log_2N\rceil\), by recursively taking a centroid, adding it to decompositions of the components, and concatenating those path decompositions. Hence the preceding argument gives
\[
\operatorname{qn}(G)
 \le 3k\bigl(\lceil\log_2 n\rceil+1\bigr)-2.
\]
This only recovers the logarithmic type of bound stated in the prompt; it does not remove the logarithm.

---

## 6. The star-indexed case

One nontrivial branching case admits a constant bound.

### Proposition 6.1
If a graph has a layered-width-one tree decomposition whose index tree is a star, then
\[
\operatorname{qn}(G)\le3.
\]

#### Proof

Let \(z\) be the center of the star. Call \(v\) central if \(z\in S_v\). There is at most one central vertex in each graph layer.

A noncentral occurrence subtree avoids \(z\), and hence consists of a single leaf of the star. Fix an order of the leaves. In every graph layer, put the central vertex first, followed by the noncentral vertices in leaf order.

Use three queues:

1. edges whose two endpoints are noncentral;
2. edges whose lower-layer endpoint is central;
3. edges whose upper-layer endpoint is central, except that central-central edges are put in queue 2.

For queue 1, the two noncentral endpoints of an edge must correspond to the same leaf. Thus leaf order is preserved between the two layers, so no nesting occurs.

Within a fixed consecutive layer pair, all queue-2 edges share the unique lower central vertex, and all queue-3 edges share the unique upper central vertex. Edges from distinct layer pairs cannot nest. ∎

### A broad family that therefore does not give counterexamples

Every graph \(H\) has a subdivision of layered treewidth \(1\) and queue-number at most \(3\).

Order
\[
V(H)=\{v_1,\dots,v_n\}.
\]
For each edge \(v_iv_j\), \(i<j\), replace it by the monotone path
\[
v_i,x^e_{i+1},x^e_{i+2},\dots,x^e_{j-1},v_j,
\]
and put the displayed vertex with subscript \(t\) in layer \(L_t\).

Take one central bag containing \(v_1,\dots,v_n\), and for each original edge \(e=v_iv_j\), one leaf bag containing all vertices of the corresponding subdivided path. Every such bag contains at most one vertex from each layer. This is a star-indexed layered-width-one decomposition, so Proposition 6.1 applies.

Thus the class of layered-treewidth-one graphs is topologically very broad; arbitrary subdivisions alone do not provide a counterexample.

---

## 7. Why a greedy layer-by-layer ordering fails

Since each consecutive two-layer graph is a forest, one might try to choose an order of \(L_0\), then extend it to \(L_1\), and so on. The following elementary example shows that no constant extension lemma is possible when the order of one side is already fixed.

### Proposition 7.1
For every \(m\), there is a forest \(F_m\) with bipartition \(A\cup B\), and an order of \(A\), such that every order of \(B\) requires at least \(\lceil\sqrt m\rceil\) queues in the block order \(A<B\).

#### Proof

Let
\[
A=\{x_1,\dots,x_m,y_1,\dots,y_m\},\qquad
B=\{b_1,\dots,b_m\},
\]
and let
\[
E(F_m)=\{x_ib_i,y_ib_i:1\le i\le m\}.
\]
Thus \(F_m\) is a disjoint union of \(m\) copies of \(P_3\).

Fix the order
\[
x_1<\cdots<x_m<y_m<\cdots<y_1
\]
on \(A\). Let \(p_i\) be the position of \(b_i\) in an arbitrary order of \(B\).

If \(p_{i_1}>\cdots>p_{i_t}\) for
\[
i_1<\cdots<i_t,
\]
then the edges
\[
x_{i_1}b_{i_1},\dots,x_{i_t}b_{i_t}
\]
form a \(t\)-rainbow.

If instead
\[
p_{i_1}<\cdots<p_{i_t},
\]
then the edges
\[
y_{i_1}b_{i_1},\dots,y_{i_t}b_{i_t}
\]
form a \(t\)-rainbow, read in the reverse order of the \(y\)-vertices.

For every permutation, the product of the lengths of its longest increasing and decreasing subsequences is at least \(m\). Hence one of these two rainbows has size at least \(\lceil\sqrt m\rceil\). ∎

This is not a counterexample: if both bipartition orders are free, \(F_m\) has a one-queue block layout. It only shows that a proof cannot choose the layer orders greedily without exploiting global compatibility supplied by the common decomposition tree.

---

## 8. Remaining gap

For layered treewidth \(1\), the problem can be reformulated as follows.

- There is a tree \(T\).
- For every graph layer \(L_i\), the vertices are represented by pairwise disjoint subtrees of \(T\).
- Consecutive-layer edges correspond to selected intersections of these subtrees.
- One must simultaneously order every family \(L_i\) so that every consecutive-layer intersection forest has bounded rainbow number.

Theorem 4.1 solves this when the host tree is a path, and Theorem 5.1 solves it with a bound depending linearly on the pathwidth of the host tree. Proposition 6.1 handles a star directly. Proposition 7.1 explains why arbitrary one-sided orders cannot be propagated through the layers.

What is missing is either:

1. a simultaneous-ordering theorem with a constant independent of the host tree, or
2. a compatible sequence of subtree families for which every simultaneous choice of orders has unbounded rainbow number.

No such theorem or construction is provided here, so the original conjecture remains open.