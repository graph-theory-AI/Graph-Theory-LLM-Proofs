```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but c must be at least 1, and the coefficient 4/3 holds with an explicit O(n^2) additive term.",
  "would_publish": false,
  "caveats": "The additive term is not uniform in n; the supplied Theorem 1.1 is used, and literature novelty has not been checked."
}
```

# 1. Partial results

Let \(K=\max_i\kappa_i\). I obtain three results.

**Theorem A — the additive constant cannot be zero.** For every odd \(t\ge 3\),
\[
\operatorname{diam}\mathrm{PP}(\underbrace{3,\ldots,3}_{2t\text{ clusters}})=5.
\]
In particular,
\[
\boxed{\operatorname{diam}\mathrm{PP}(3,3,3,3,3,3)=5.}
\]
Consequently, any constant satisfying the conjecture must satisfy \(c\ge 1\).

The lower bound is proved below for arbitrary graph paths, including paths that temporarily misplace items. The upper bound \(5\) is Theorem 1.1 as supplied in the question.

**Theorem B — repeated-permutation discrepancies.** Suppose that, for some permutation \(\sigma\) of the clusters and integer \(d\), the discrepancy between two vertices consists of exactly \(d\) items going from \(i\) to \(\sigma(i)\) for every nonfixed point \(i\), and no other discrepancies. Then
\[
\operatorname{dist}(P,Q)
\le
8\left\lfloor\frac d6\right\rfloor
+
\left\lceil\frac{3(d\bmod 6)}2\right\rceil
\le
\left\lceil\frac{4d}{3}\right\rceil+1.
\]
Thus the conjectured bound, with the optimal universal additive constant \(1\), holds for this class without restricting the number of clusters.

**Theorem C — bounded-cluster version.** For arbitrary cluster sizes,
\[
\boxed{
\operatorname{diam}\mathrm{PP}(\kappa_1,\ldots,\kappa_n)
\le
\left\lceil
\frac{4K}{3}
+\frac56\bigl((n-1)^2+1\bigr)
\right\rceil.
}
\]
In particular, the conjectured coefficient \(4/3\) holds for every fixed number of clusters, with an explicit additive constant depending on that number. More generally, this gives
\[
\operatorname{diam}\le (4/3+o(1))K
\qquad\text{when }n^2=o(K).
\]

These statements do **not** establish an absolute additive constant independent of \(n\).

# 2. The graph model and adjacency

A vertex is a labelled partition
\[
P=(P_1,\ldots,P_n),\qquad |P_i|=\kappa_i.
\]
For vertices \(P,Q\), make a directed multigraph \(D(P,Q)\) on the clusters: an item in \(P_i\cap Q_j\), with \(i\ne j\), gives a labelled arc \(i\to j\). Then
\[
d_D^+(i)=d_D^-(i)=d_i,
\qquad
d_i=|P_i\setminus Q_i|.
\]
Thus the discrepancy digraph is Eulerian. Write \(d=\max_i d_i\le K\).

I reuse this model from the previous attempt, but verify the needed adjacency fact. Its four-cluster routing certificates are not used.

## Adjacency lemma

Two distinct partition vertices are adjacent if and only if their discrepancy is one directed simple cycle, with a directed \(2\)-cycle allowed.

Indeed, use the transportation realization
\[
\mathrm{PP}(\kappa_1,\ldots,\kappa_n)
=
\left\{
x\ge0:
\sum_i x_{i,e}=1,\quad
\sum_e x_{i,e}=\kappa_i
\right\}.
\]
The smallest face containing two vertices has support equal to the union of their supports. Its dimension is the cycle rank of the corresponding bipartite support graph.

Deleting unchanged-item leaves and contracting changed-item vertices preserves this cycle rank and gives the underlying multigraph of \(D(P,Q)\). Every nontrivial Eulerian component has minimum undirected degree at least two. Consequently, cycle rank one means that there is exactly one nontrivial component and every vertex in it has indegree and outdegree one. That is precisely a directed simple cycle.

Therefore one polytope edge moves one item out of each cluster in a directed simple cycle. In particular, it moves at most one item out of any given cluster.

All subsequent arguments use this exact graph model.

# 3. A counterexample to the \(c=0\) strengthening

Fix odd \(t\ge3\). There are \(2t\) clusters of size three, grouped into pairs
\[
\{a_1,b_1\},\ldots,\{a_t,b_t\}.
\]
Choose \(P,Q\) so that all three items in \(a_i\) must go to \(b_i\), and all three items in \(b_i\) must go to \(a_i\).

Call a transition between the two clusters of one pair a **mate transition**.

## 3.1. What a four-edge path would have to look like

Consider any path of \(q\) polytope edges between these vertices. Let

- \(L\) be the total number of item-movements;
- \(s\) be the number of items moved exactly once;
- \(T\) be the number of mate transitions.

All \(6t\) items are initially misplaced. Thus
\[
L\ge s+2(6t-s)=12t-s.
\]
An item moved exactly once must use a mate transition, so \(s\le T\).

A simple cycle on the \(2t\) clusters contains at most \(t\) mate transitions. For cycles of length at least three, it contains at most one transition from each pair. A \(2\)-cycle contains at most two, and \(2\le t\). Hence
\[
T\le tq.
\]
Also,
\[
L\le 2tq.
\]
Combining these inequalities gives
\[
2tq\ge12t-s\ge12t-T\ge12t-tq,
\]
and therefore \(q\ge4\).

Suppose now that \(q=4\). Equality must hold throughout. It follows that:

1. Every move is a Hamilton cycle on all \(2t\) clusters.
2. Every move contains exactly one mate transition in each pair.
3. Exactly \(4t\) items move once, and the other \(2t\) items move exactly twice.
4. Every mate transition moves a once-moved item; both transitions of a twice-moved item go between different pairs.

In each move, the two clusters of every pair consequently appear consecutively. Contracting each pair gives a directed Hamilton cycle on the \(t\) pairs.

Each pair contains six original items and makes four mate transitions over the four moves. Therefore exactly two original items of each pair move twice. Moreover, exactly two items pass through each pair as their intermediate pair: among its four outgoing cross-pair transitions, two start original items and two forward intermediate items.

## 3.2. The first move would force a perfect matching on an odd cycle

Contract the pairs in the first move. Color each edge of this directed \(t\)-cycle by the move—\(2\), \(3\), or \(4\)—in which the item sent along that edge makes its second transition.

Consider one pair. In the first move, write its internal transition as
\[
u\longrightarrow v.
\]
Thus the first cross-pair item arrives at \(u\), while another item leaves \(v\). The latter item's target is \(u\).

Let

- \(p\) be the color of the incoming edge: the first arriving item is forwarded in move \(p\);
- \(q\) be the color of the outgoing edge: the first departing item returns to its target in move \(q\).

First, \(p\ne q\). If both occurred in one move, that move would have both its cross-pair incoming and cross-pair outgoing transition at \(u\). But in a Hamilton move containing one internal transition for this pair, those two cross-pair transitions occur at different clusters.

Second, the two colors cannot be \(2\) and \(4\).

- If \(p=2\) and \(q=4\), the pair's other original twice-moved item must start in move \(2\) and finish in move \(3\): it cannot start in move \(1\), and it cannot finish in move \(4\), because those cross-pair transitions are already occupied by the first departing item. But forwarding the first arriving item already uses the outgoing cross-pair transition in move \(2\), a contradiction.
- If \(p=4\) and \(q=2\), the pair's other intermediate item must arrive in move \(2\) and leave in move \(3\). But the first departing item's return already uses the incoming cross-pair transition in move \(2\), again a contradiction.

Consequently, the two incident colors at every vertex of the contracted first-move cycle are either
\[
\{2,3\}\quad\text{or}\quad\{3,4\}.
\]
The edges colored \(3\) therefore form a perfect matching of that cycle.

This is impossible because \(t\) is odd.

Thus no four-edge path exists, and
\[
\operatorname{dist}(P,Q)\ge5.
\]
The supplied Theorem 1.1 gives diameter at most
\[
\left\lceil\frac{3\cdot3}{2}\right\rceil=5,
\]
proving Theorem A.

In particular, the exact bound “diameter at most \(4\) whenever \(K=3\)” is false for the standard labelled partition polytope. This does not disprove the stated conjecture, which allows an additive constant.

# 4. Six identical permutation layers can be routed in eight moves

This is the main constructive ingredient in the upper bounds.

## 4.1. Six copies of disjoint swaps

First consider \(t\ge2\) pairs of clusters
\[
v_{i,0},v_{i,1}\qquad (i\in\mathbb Z/t\mathbb Z).
\]
At each cluster there are six selected items, all destined for its mate. Other items, if any, will remain untouched.

Choose a proper coloring
\[
\gamma:\mathbb Z/t\mathbb Z\longrightarrow\{1,2,3\}
\]
of the cyclic order of the pairs. For \(t=2\), simply give the two pairs different colors. Such a coloring can be given explicitly: alternate colors \(1,2\) when \(t\) is even; when \(t\) is odd, alternate them on \(1,\ldots,t-1\) and give the last pair color \(3\).

For \(x=(x_1,x_2)\in\mathbb F_2^2\), define
\[
\ell_1(x)=x_1,\qquad
\ell_2(x)=x_2,\qquad
\ell_3(x)=x_1+x_2,
\]
and put
\[
\varepsilon_i(x)=\ell_{\gamma(i)}(x).
\]

Two properties will be used:

- each \(\varepsilon_i\) takes the values \(0,1\) twice each;
- for consecutive pairs \(i,j\), the four values
  \[
  \bigl(\varepsilon_i(x),\varepsilon_j(x)\bigr),
  \qquad x\in\mathbb F_2^2,
  \]
  are exactly the four binary pairs.

The second property holds because distinct nonzero linear forms on \(\mathbb F_2^2\) are linearly independent.

### First four moves

For each \(x\in\mathbb F_2^2\), perform the Hamilton cycle whose transitions are
\[
v_{i,1-\varepsilon_i(x)}
\longrightarrow
v_{i,\varepsilon_i(x)}
\longrightarrow
v_{i+1,1-\varepsilon_{i+1}(x)}
\qquad\text{for all }i.
\]
Use the order \(x=00,01,10,11\), and in these four moves always send a previously unmoved original item from each cluster.

After these four moves, every cluster contains:

- two unmoved original items;
- two correctly delivered items from its mate;
- two intermediate items from the preceding pair.

Moreover, the two intermediate items are destined for different clusters of the preceding pair. This follows from the four possible binary pairs occurring exactly once on each consecutive pair of indices.

### Last four moves

For the same four choices of \(x\), perform the Hamilton cycle
\[
v_{i,1-\varepsilon_i(x)}
\longrightarrow
v_{i,\varepsilon_i(x)}
\longrightarrow
v_{i-1,1-\varepsilon_{i-1}(x)}
\qquad\text{for all }i.
\]

On an internal mate transition, send an unmoved original item. On a cross-pair transition, send the intermediate item whose target is its head.

These choices are always available:

- each cluster is the source of an internal transition twice, exactly matching its two unmoved original items;
- for consecutive pairs, the four cross-pair transitions occurring over these moves include each ordered choice of source cluster and target cluster exactly once, exactly matching the intermediate items already present.

Every item is now correctly placed. Hence six copies of any collection of disjoint swaps can be routed in eight moves.

For a single pair, six swaps suffice, so the same upper bound holds.

## 4.2. Subdividing a demand cycle preserves the routing bound

We need to pass from swaps to arbitrary permutation cycles.

Consider a class of \(k\) parallel demands \(a\to b\), and replace it by
\[
a\to w_1\to\cdots\to w_s\to b,
\]
with multiplicity \(k\) on every arc and with new internal clusters. Suppose the original demands have a routing in \(q\) moves.

For each original \(a\)-item, consider its first departure from \(a\). If that departure uses a transition \(a\to z\), replace that transition in the move by
\[
a\to w_1\to\cdots\to w_s\to z.
\]
Send the original \(a\)-item to \(w_1\), send one previously unmoved original item along each internal transition, and let the item sent from \(w_s\) continue along the old routing trace of the original \(a\)-item.

This is valid because:

- the \(k\) first departures occur in distinct moves;
- each new cluster has one fresh item available for each such departure;
- inserting a private path into a simple cycle keeps it simple;
- the original \(a\)-items and the internal items except the last are delivered immediately, while the last items inherit traces ending at \(b\).

Several subdivisions with disjoint internal clusters can be performed simultaneously.

Every directed cycle of length at least two is a subdivision of a directed \(2\)-cycle. Therefore:

> **Six-layer routing lemma.** Six copies of any permutation discrepancy can be routed in at most eight polytope edges, using only those selected items.

Fixed points require no items and are omitted. A permutation with only one nontrivial cycle can also be handled directly in six moves.

## 4.3. Arbitrarily many identical layers

Write
\[
d=6a+r,\qquad 0\le r\le5.
\]
Route the \(a\) six-layer blocks in \(8a\) moves. Fix those items, and route the remaining \(r\) layers using the supplied Theorem 1.1, in at most \(\lceil3r/2\rceil\) moves.

Thus
\[
\operatorname{dist}(P,Q)\le8a+\left\lceil\frac{3r}{2}\right\rceil.
\]
The remainder costs are
\[
\begin{array}{c|rrrrrr}
r&0&1&2&3&4&5\\ \hline
\lceil3r/2\rceil&0&2&3&5&6&8 .
\end{array}
\]
They exceed \(\lceil4r/3\rceil\) only when \(r=3\) or \(5\), and then by one. This proves Theorem B.

The additive \(1\) is necessary within this class by Theorem A.

# 5. An \(O(n^2)\) additive term for arbitrary discrepancies

The six-layer lemma can be combined with a sparse integer decomposition into permutation matrices.

## 5.1. Sparse weighted permutation decomposition

Let \(D=D(P,Q)\), and let \(d=\max_i d_i\). If \(d=0\), there is nothing to prove.

Add \(d-d_i\) formal loops at cluster \(i\). The resulting multiplicity matrix \(A\) is a nonnegative integer matrix with every row and column sum equal to \(d\).

It admits a decomposition
\[
A=\sum_{j=1}^{h}\lambda_j P_j,
\qquad
\lambda_j\in\mathbb Z_{>0},
\qquad
\sum_j\lambda_j=d,
\]
where the \(P_j\) are permutation matrices and
\[
h\le (n-1)^2+1.
\tag{1}
\]

Here is a proof including the sparsity assertion.

A positive-degree regular bipartite multigraph has a perfect matching by Hall's theorem. Choose such a matching in the support of \(A\), and subtract the largest possible integer multiple \(\lambda P\), namely the minimum entry along that matching. Repeat.

To bound the number of iterations, normalize each nonzero remaining matrix by its common row sum. These normalized matrices lie in the Birkhoff polytope, whose dimension is \((n-1)^2\). At every nonfinal subtraction, at least one previously positive entry becomes zero. Hence the next normalized matrix lies in a proper face of the previous matrix's minimal face. There can be at most \((n-1)^2\) such strict face descents, followed by the final subtraction. This proves (1).

Formal loops correspond to fixed points of the permutations and are never routed.

## 5.2. Route the multiples of six, then the remainder

Write
\[
\lambda_j=6a_j+b_j,
\qquad
0\le b_j\le5,
\]
and set
\[
R=\sum_j b_j.
\]
By (1),
\[
R\le5h\le5\bigl((n-1)^2+1\bigr).
\tag{2}
\]

For every \(j\), use the six-layer routing lemma to route the \(6a_j\) copies of \(P_j\) in \(8a_j\) moves. Each such operation uses only the selected items, so the other discrepancy items remain in their original clusters.

The remaining discrepancy has maximum outdegree at most \(R\). Fixing every item outside this discrepancy leaves a partition polytope whose largest prescribed size is at most \(R\); zero-size clusters can be deleted. Its graph paths are also paths in the original polytope. Thus Theorem 1.1 routes the remainder in at most \(\lceil3R/2\rceil\) moves.

Since
\[
d=6\sum_j a_j+R,
\]
the total number of moves is at most
\[
\begin{aligned}
8\sum_j a_j+\left\lceil\frac{3R}{2}\right\rceil
&=
\left\lceil\frac{4d}{3}+\frac{R}{6}\right\rceil\\
&\le
\left\lceil
\frac{4d}{3}
+\frac56\bigl((n-1)^2+1\bigr)
\right\rceil.
\end{aligned}
\]
Finally \(d\le K\), proving Theorem C.

For a particular pair of vertices, \(n\) in this argument may be replaced by the number of active clusters.

# 6. What remains unresolved

The original conjecture requires an additive constant independent of both \(K\) and \(n\). Theorem C still has a quadratic dependence on \(n\). Its obstruction is precise: after extracting multiples of six from the weighted permutation decomposition, as many as
\[
5\bigl((n-1)^2+1\bigr)
\]
residual layers may remain. The argument does not coordinate these different permutation types with an \(n\)-independent overhead.

Theorem A shows that trying to establish the exact \(K=3\) bound \(4\) cannot succeed: the correct maximum is already \(5\) for the displayed six-cluster instance. It does **not** rule out the conjecture with \(c=1\), or with another absolute constant.

I have not independently checked whether these partial statements already occur in the full source paper or elsewhere. The claims here are mathematical results of the arguments above, not claims of literature novelty.