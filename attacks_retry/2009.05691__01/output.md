```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Given a k-vertex chordal deletion set, the problem has a deterministic 2^{O(k log(k+2))}n^4 algorithm, but the unrestricted polynomial-time question remains unresolved.",
  "would_publish": false,
  "caveats": "The deletion set is supplied; novelty of the restricted-class algorithm is not claimed, and no unrestricted algorithm or hardness result is obtained."
}
```

# 1. Results and scope

A **hole** is an induced cycle of length at least four. Call a hole **target** if its length is divisible by three; its possible lengths are therefore \(6,9,12,\ldots\).

I obtain the following restricted algorithm.

### Theorem 1
Let \(G\) be an \(n\)-vertex graph, and suppose that a set \(S\subseteq V(G)\) of size \(k\) is supplied such that \(G-S\) is chordal. One can detect a target hole, and recover one when it exists, deterministically in time
\[
2^{O(k\log(k+2))}n^4.
\]

There is also a randomized decision algorithm using
\[
2^{O(k)}n^4
\]
field operations over a field of size \(O(n)\). It never falsely reports that a target hole exists, and its false-negative probability is at most \(1/2\).

Consequently, for each fixed \(k\), detection is polynomial on graphs that can be made chordal by deleting at most \(k\) vertices. If the deletion set is not supplied, it can be found on this promised class by enumerating the sets of size at most \(k\) and testing chordality.

This is different from applying a bounded-treewidth algorithm to \(G\): even when \(k=0\), the graph can have arbitrarily large cliques and treewidth.

I also strengthen the obstruction to the shortest-path approach in the supplied attempt. There are planar, bipartite, subcubic graphs with a **unique** target hole \(C\) such that:

- every vertex outside \(C\) has at most one neighbor on \(C\);
- no pair of opposite vertices of \(C\) has its two rim arcs shortest in the graph;
- the shortcuts responsible for this failure can branch arbitrarily far from \(C\).

Thus eliminating vertices with several separated neighbors on a shortest target hole is not sufficient to obtain the proposed geodesic decomposition.

Neither result resolves the unrestricted question.

# 2. Deterministic algorithm with a chordal deletion set

Write
\[
H=G-S.
\]

The essential observation is that a hole of length at least four meets any clique in at most two vertices. This permits a dynamic program over the clique bags of a chordal graph, even though those bags can be arbitrarily large.

## 2.1. A suitable decomposition

We use the standard characterization of chordal graphs by perfect-elimination orderings. It gives a tree decomposition of \(H\) with at most \(|V(H)|\) bags, every bag being a clique.

For completeness, from a perfect-elimination ordering \(v_1,\ldots,v_h\), take
\[
K_i=\{v_i\}\cup N^+(v_i),
\]
where \(N^+(v_i)\) denotes the later neighbors of \(v_i\). If \(N^+(v_i)\neq\varnothing\), let \(p(i)\) be its earliest vertex and attach bag \(K_i\) to \(K_{p(i)}\). Because \(N^+(v_i)\) is a clique,
\[
N^+(v_i)\subseteq K_{p(i)}.
\]
This gives the running-intersection property; roots belonging to different components may be connected arbitrarily. When \(H\) is empty, use one empty bag.

Every target hole meets \(S\), since \(H\) is chordal. Enumerate its possible nonempty intersection
\[
R=V(C)\cap S.
\]
For this iteration delete \(S\setminus R\), and require all vertices of \(R\) to be selected.

Add \(R\) to every bag of the clique-bag decomposition of \(H\). Normalize the resulting decomposition so that:

- its root and leaves have bag \(R\);
- vertices of \(H\) are introduced and forgotten one at a time;
- it has binary join nodes;
- every graph edge has exactly one edge-introduction node;
- edges with both ends in \(R\) are introduced at the top, after the other processing.

There are \(O(n^2)\) nodes. Throughout normalization, the portion of every bag outside \(R\) remains a clique: when moving between two clique bags, first remove vertices down to their intersection and then add vertices from the new bag.

For a target hole with intersection \(R\), its selected vertices in a bag \(B\) consequently have the form
\[
A=R\cup X,\qquad X\subseteq B\setminus R,\qquad |X|\leq 2. \tag{1}
\]

## 2.2. States and invariant

Fix \(R\neq\varnothing\). A state at a bag \(B\) consists of:

1. the set \(X\) from (1), determining the selected bag vertices \(A=R\cup X\);
2. a partial degree
   \[
   d(a)\in\{0,1,2\}\qquad(a\in A);
   \]
3. a partition \(\pi\) of \(A\), recording connectivity in the selected, already-processed graph;
4. the number of selected, already-forgotten vertices of \(H\), both:
   - modulo three;
   - capped at six.

The invariant additionally requires:

- every selected forgotten vertex has degree exactly two;
- every component of the selected processed graph meets the current bag.

The last condition is legitimate because \(R\) is nonempty and remains in every bag. A component that disappears from a bag can never attach to any future vertex. If it contains no bag vertex, it therefore cannot be part of a final connected graph containing \(R\).

The degree counters concern introduced edges only. Crucially, **an edge whose two endpoints are selected is compulsory when it is introduced**.

## 2.3. Transitions

At a leaf, the selected graph consists of the vertices \(R\), with no edges yet processed. All degrees are zero, the partition consists of singleton blocks, and both counters are zero.

### Introduce a vertex \(v\in H\)

There are two choices:

- leave \(v\) unselected;
- select \(v\), give it degree zero, and add a singleton block \(\{v\}\).

The second choice is allowed only if \(|X|\leq 2\) remains true.

### Introduce an edge \(uv\)

If either endpoint is unselected, nothing changes.

If both endpoints are selected, increment both degree counters and merge their connectivity blocks. Reject if either degree exceeds two. The edge cannot be omitted.

### Forget a vertex \(v\in H\)

If \(v\) is unselected, simply remove it from the bag.

If \(v\) is selected:

1. require \(d(v)=2\);
2. reject if its connectivity block is \(\{v\}\), since that component would disappear from the bag;
3. otherwise remove \(v\) from its block;
4. increment both counting records.

All incident edges of a forgotten vertex have already been processed.

### Join

The selected bag set must agree in both children. For such a pair of states:

- add the degree counters and reject values exceeding two;
- take the least common coarsening of the two partitions;
- add the modulo-three counts;
- add the capped counts, saturating at six.

The introduced edge sets in the two child subtrees are disjoint. Their forgotten-vertex sets are also disjoint, so no correction to the counting records is needed.

## 2.4. Acceptance and correctness

At the root, the bag is \(R\). Let \(a\) be the modulo-three count and \(b\) the count capped at six. Accept precisely when
\[
d(r)=2\quad\text{for every }r\in R,
\]
\[
\pi=\{R\},
\]
\[
a+|R|\equiv 0\pmod 3,
\qquad
b+|R|\geq 6. \tag{2}
\]

### Soundness

An accepting state describes a connected selected graph in which every vertex has degree two. Every edge of \(G\) between selected vertices was compulsory, so this graph is exactly the induced subgraph on its selected vertex set.

A finite connected simple 2-regular graph is a cycle. Conditions (2) say that its length is at least six and divisible by three. Thus it is a target hole.

### Completeness

Suppose \(C\) is a target hole. Since \(H\) is chordal,
\[
R=V(C)\cap S\neq\varnothing,
\]
so this \(R\) is considered.

Select precisely the vertices of \(C\). Every clique bag of \(H\) meets \(C\) in at most two vertices, so restriction (1) is satisfied. Inducedness ensures that compulsory edges never give a selected degree greater than two.

No component of the selected partial graph can disappear from a bag: it would then have no possible connection to the rest of \(C\), whereas \(C\) is connected and contains the persistent set \(R\). All the transitions are therefore available, and the root satisfies (2).

This proves correctness. Storing predecessor choices recovers a hole.

## 2.5. Running time

For fixed \(R\), there are \(O(n^2)\) possibilities for \(X\). Once \(X\) is fixed, there are at most
\[
3^{|R|+2}\operatorname{Bell}(|R|+2)\cdot O(1)
=
2^{O(|R|\log(|R|+2))}
\]
states.

At a join, group states by their common selected bag set. Squaring the number of states within one group still gives
\[
2^{O(|R|\log(|R|+2))},
\]
not an additional factor \(n^2\).

There are \(O(n^2)\) decomposition nodes. Summing over the nonempty subsets \(R\subseteq S\) gives
\[
2^{O(k\log(k+2))}n^4.
\]
This proves the deterministic part of Theorem 1.

# 3. Single-exponential randomized refinement

Here is a self-contained counting refinement that removes the partition factor.

Fix a nonempty \(R\subseteq S\), and choose an anchor \(r_0\in R\). Replace the connectivity partition by a side assignment
\[
\sigma:A\longrightarrow\{\mathrm L,\mathrm R\},
\qquad \sigma(r_0)=\mathrm L.
\]

Require every introduced edge whose endpoints are selected to have both endpoints on the same side. At joins, side assignments must agree.

Keep the degree and counting records, but discard the condition that a component must continue meeting the bag. Thus selected components are now allowed to be completed and forgotten.

Assign an indeterminate \(x_v\) to each vertex \(v\in H\). When a selected \(v\in H\) is forgotten, multiply the state value by \(x_v\). Sum and multiply state values in characteristic two.

Consider a selected vertex set \(F\) satisfying the degree, size, residue, and bag-selection conditions, with \(F\cap S=R\). If \(G[F]\) has \(c\) components, there are exactly
\[
2^{c-1}
\]
consistent side assignments with \(r_0\) on the left. Therefore, in characteristic two, disconnected selected graphs cancel, while connected ones contribute once.

The resulting polynomial is exactly
\[
Q_R(\mathbf x)=
\sum_{\substack{C\text{ a target hole}\\V(C)\cap S=R}}
\ \prod_{v\in V(C)\setminus R}x_v, \tag{3}
\]
where each hole is counted by its vertex set.

There is no cancellation between distinct holes in (3): for fixed \(R\), distinct vertex sets give distinct monomials. Consequently,
\[
Q_R\not\equiv 0
\quad\Longleftrightarrow\quad
\text{some target hole has intersection }R\text{ with }S.
\]

Evaluate the dynamic program at independent uniform elements of a field of characteristic two and size
\[
q\geq 2(n+1).
\]
A nonzero polynomial in (3) has total degree at most \(n\), so its probability of evaluating to zero is at most \(n/q<1/2\), by the elementary polynomial identity-testing bound.

Run this test for every nonempty \(R\subseteq S\), and report YES if any evaluation is nonzero.

- If no target hole exists, all these polynomials are identically zero: there is no false positive.
- If a target hole exists, fix one corresponding set \(R\). The probability that the whole algorithm reports NO is at most the probability that this particular nonzero polynomial evaluates to zero, hence at most \(1/2\).

Repeating independently reduces the false-negative probability exponentially.

For fixed selected bag set, degree and side assignments now contribute only
\[
3^{|R|+2}2^{|R|+2}=2^{O(|R|)}
\]
states. The same decomposition and join analysis gives
\[
2^{O(k)}n^4
\]
field operations. The field elements have \(O(\log n)\) bits.

# 4. A stronger obstruction to geodesic reconstruction

The following construction addresses the shortest-path lead independently of the algorithm above.

Choose integers \(h,s\) satisfying
\[
h\equiv 0\pmod 6,\qquad s\geq 2,\qquad s\not\equiv 0\pmod3,\qquad h>2s.
\]

Construct \(W(h,s)\) as follows:

1. take a rim cycle \(C\) of length \(3h\);
2. mark vertices \(a_0,a_1,a_2\), equally spaced by rim distance \(h\);
3. add a vertex \(z\);
4. join \(z\) to each \(a_i\) by a path of length \(s\), with the three paths internally disjoint and otherwise disjoint from \(C\);
5. add no other edges.

This is a subdivision of \(K_4\).

### Proposition 2
The graph \(W(h,s)\) is planar, bipartite, and of maximum degree three. Its unique target hole is its rim \(C\). Every vertex outside \(C\) has at most one neighbor on \(C\), but \(C\) has no geodesic decomposition into two opposite arcs.

## Proof

### All cycles and their residues

A cycle avoiding \(z\) must be the rim.

A cycle containing \(z\) uses exactly two spokes and one of the two rim arcs between their marked endpoints. Its length is therefore either
\[
h+2s
\quad\text{or}\quad
2h+2s.
\]
These are all the possibilities.

Moreover, every cycle in \(W(h,s)\) is induced. Indeed, the only vertices of degree three are \(z,a_0,a_1,a_2\), and no two of them are adjacent. A chord of a cycle would have two endpoints of degree at least three, which is impossible here.

The rim has length \(3h\equiv0\pmod3\), while every other cycle has residue
\[
2s\not\equiv0\pmod3.
\]
Thus the rim is the unique target hole.

All the listed cycle lengths are even, so the graph is bipartite. Planarity and the maximum-degree bound follow directly from the construction.

Because \(s\geq2\), no outside vertex is adjacent to two rim vertices.

### Every antipodal pair has a shortcut

Number the rim vertices modulo \(3h\), with marked vertices \(0,h,2h\). By rotation, an antipodal pair can be written as
\[
t,\ t+\frac{3h}{2},
\qquad 0\leq t<h.
\]

If \(0\leq t\leq h/2\), route the endpoints to marked vertices \(0\) and \(2h\). The total length of these two rim portions is
\[
t+\left(\frac h2-t\right)=\frac h2.
\]

If \(h/2\leq t<h\), use marked vertices \(h\) and \(2h\). The corresponding total is
\[
(h-t)+\left(t-\frac h2\right)=\frac h2.
\]

In either case, passing through the two spokes and \(z\) gives a path of length
\[
\frac h2+2s<\frac{3h}{2}.
\]
Both rim arcs between the antipodal endpoints have length \(3h/2\). Hence neither is shortest.

Thus no antipodal pair provides the even geodesic decomposition considered in the supplied attempt. ∎

For example, \(W(6,2)\) has a unique target hole of length \(18\); all its other holes have length \(10\) or \(16\).

There is also an arbitrary-radius version of the obstruction. Given a fixed radius \(r\), choose \(s>r\) and then an admissible \(h>2s\). The subgraph induced by the vertices at distance at most \(r\) from \(C\) consists of \(C\) with three pendant path segments. The rim is isometric in this neighborhood, although it has no geodesic antipodal decomposition in the full graph.

So the failure is not confined to outside vertices with large or widely spread neighborhoods directly on \(C\).

# 5. What remains open

The chordal-deletion parameter is not bounded on graphs without target holes. For example,
\[
K_{r,r}
\]
has only induced \(4\)-cycles, hence no target hole, but its minimum chordal deletion set has size \(r-1\): both bipartition classes must not retain two vertices.

Thus Theorem 1 does not turn into an unrestricted polynomial-time algorithm by proving that negative instances have bounded \(k\).

The obstruction in Section 4 also rules out a particular shortcut to completeness: even a unique shortest target hole with no outside vertex having two neighbors on it need not admit the proposed geodesic reconstruction.

The remaining task is an unrestricted polynomial-time algorithm or a hardness proof. Neither is established here. The results above are restricted algorithmic upper bounds and a precisely verified limitation of the shortest-path approach; I make no novelty claim for the restricted-class algorithms.