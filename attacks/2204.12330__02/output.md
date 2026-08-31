```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "No separation is obtained, but bounded queue number follows for sparse graphs with bounded-front contraction sequences, for sparse bounded-rank-width classes, and for virtually left-orderable groups.",
  "would_publish": false,
  "caveats": "These are special-case reductions, likely overlapping standard facts; ordinary twin-width and the uniform group variants remain unresolved."
}
```

# 1. Precise formulation

Every finite graph has finite twin-width and finite queue-number. Thus the separation problem must concern either:

- a class \(\mathcal C\) of finite sparse graphs such that
  \[
  \sup_{G\in\mathcal C}\operatorname{tww}(G)<\infty
  \quad\text{but}\quad
  \sup_{G\in\mathcal C}\operatorname{qn}(G)=\infty,
  \]
  or
- a locally finite infinite graph, in particular a Cayley graph, with the corresponding uniform bounds over finite subgraphs.

Here “sparse” is most usefully interpreted as bounded maximum degree, bounded degeneracy, or at least exclusion of some \(K_{t,t}\) as a subgraph.

I do not obtain either a separation or a converse theorem. I prove several restrictions on where a counterexample can occur.

# 2. Queue layouts and rainbows

Fix a total order \(<\) on \(V(G)\). Write an edge as \((\ell(e),r(e))\), where \(\ell(e)<r(e)\). A set of edges is a **rainbow** if it can be written
\[
\ell(e_1)<\ell(e_2)<\cdots<\ell(e_k)
 <r(e_k)<\cdots<r(e_2)<r(e_1).
\]

For this fixed order, the minimum number of queues equals the maximum size of a rainbow. Indeed, define a partial order on \(E(G)\) by strict interval containment:
\[
e\prec f
\quad\Longleftrightarrow\quad
\ell(f)<\ell(e)<r(e)<r(f).
\]
Its chains are precisely rainbows. Coloring each edge by the length of a longest chain ending at that edge partitions the edges into as many antichains as the height of the poset, and each antichain is a queue.

This elementary observation will be used repeatedly.

# 3. A bounded-front special case of the conjectured converse

The following is a direct twin-width-type special case.

## Theorem 3.1

Let \(G\) be \(K_{t,t}\)-free. Suppose that \(V(G)\) has an order
\[
v_1,\ldots,v_n
\]
with the following property. For every prefix
\[
P_i=\{v_1,\ldots,v_i\},
\]
there is a partition
\[
P_i=A^i_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A^i_{r_i},
\qquad r_i\le s,
\]
such that every \(A^i_j\) has mixed adjacency to at most \(d\) vertices of \(V(G)\setminus P_i\). Here adjacency between \(A^i_j\) and a vertex \(y\) is mixed if \(y\) has both a neighbor and a non-neighbor in \(A^i_j\).

Then
\[
\operatorname{qn}(G)\le s(d+t-1).
\]

### Proof

Use the given vertex order. Let \(R\) be a rainbow of size \(k\), and choose the cut immediately after the last left endpoint of \(R\). Thus every left endpoint is in some prefix \(P_i\), while every right endpoint is outside \(P_i\).

Partition the right endpoints into two types.

1. A right endpoint is **mixed** if it has mixed adjacency to at least one \(A^i_j\). There are at most \(sd\) such vertices, by the union bound over the at most \(s\) prefix bags.

2. Otherwise the right endpoint \(y\) is homogeneous to every \(A^i_j\). Let \(x\in A^i_j\) be its corresponding left endpoint. Since \(xy\in E(G)\), \(y\) is complete to \(A^i_j\).

Assign this edge to \(A^i_j\). If at least \(t\) such rainbow edges were assigned to the same bag \(A^i_j\), their \(t\) distinct left endpoints and \(t\) distinct right endpoints would induce a \(K_{t,t}\) as a subgraph: every one of these right endpoints is complete to \(A^i_j\). Therefore at most \(t-1\) non-mixed rainbow edges are assigned to each prefix bag.

Consequently
\[
k\le sd+s(t-1)=s(d+t-1).
\]
The rainbow characterization now gives the asserted queue bound. \(\square\)

## Corollary 3.2: one-growing-bag contraction sequences

Suppose \(G\) has a \(d\)-contraction sequence of the following restricted form: for some order \(v_1,\ldots,v_n\), at stage \(i\) the only non-singleton part is
\[
P_i=\{v_1,\ldots,v_i\},
\]
and \(P_i\) is contracted with \(\{v_{i+1}\}\) at the next step. If \(G\) is \(K_{t,t}\)-free, then
\[
\operatorname{qn}(G)\le d+t-1.
\]

Indeed, a mixed adjacency between \(P_i\) and a suffix singleton is a red adjacency, so Theorem 3.1 applies with \(s=1\).

In particular, if \(\Delta(G)\le\Delta\), then \(G\) is \(K_{\Delta+1,\Delta+1}\)-free and
\[
\operatorname{qn}(G)\le d+\Delta.
\]

Thus the desired separation cannot be witnessed by bounded-degree graphs admitting bounded-width “one-growing-bag” sequences. More generally, Theorem 3.1 handles any contraction scheme with a bounded number of active prefix bags.

The obstruction to extending this proof to ordinary twin-width is important: in a general contraction sequence, a red neighbor is a whole bag, not a singleton. One red bag may contain arbitrarily many right endpoints of a rainbow.

# 4. Bounded rank-width cannot witness the separation

This section gives a second, independent restriction.

I use the standard queue-layout fact
\[
\operatorname{tw}(G)\le w
\quad\Longrightarrow\quad
\operatorname{qn}(G)\le 2^w-1.
\]
Only the existence of some function of \(w\) is needed below.

## Theorem 4.1

Let \(G\) be \(K_{t,t}\)-free and suppose
\[
\operatorname{rw}(G)\le k.
\]
Then
\[
\operatorname{tw}(G)
 \le 3(t-1)(2^k-1)-1,
\]
and hence
\[
\operatorname{qn}(G)
 \le
 2^{\,3(t-1)(2^k-1)-1}-1.
\]

### Proof

Take a rank-decomposition of width at most \(k\). An edge of the decomposition tree determines a cut
\[
V(G)=A\mathbin{\dot\cup}B
\]
whose \(A\times B\) adjacency matrix has rank at most \(k\) over \(\mathbb F_2\).

There are at most \(2^k\) distinct rows. Partition the vertices of \(A\) into classes \(C_1,\ldots,C_m\) according to their neighborhoods in \(B\), omitting the zero row. Thus
\[
m\le 2^k-1.
\]
For each class \(C_j\), let \(N_j\subseteq B\) be its common nonempty neighborhood. The crossing graph contains the complete bipartite graph
\[
C_j\times N_j.
\]
Since \(G\) is \(K_{t,t}\)-free,
\[
\min\{|C_j|,|N_j|\}\le t-1.
\]
Choose the smaller of \(C_j\) and \(N_j\), and take the union over all row classes. This gives a vertex cover of all crossing edges of size at most
\[
b:=(t-1)(2^k-1).
\]
In particular, every decomposition cut has crossing matching number at most \(b\).

For completeness, here is the standard deduction of treewidth from these crossing covers. Let \(\mathcal B\) be any bramble in \(G\). For every decomposition-tree edge \(e\), choose a crossing vertex cover \(Z_e\) with \(|Z_e|\le b\).

If some \(Z_e\) meets every member of \(\mathcal B\), then \(\mathcal B\) has order at most \(b\). Otherwise, after deleting \(Z_e\), every connected bramble member avoiding \(Z_e\) lies entirely on one side of the corresponding cut. Moreover, all such members lie on the same side, since members on opposite sides would neither intersect nor be joined by an edge. Orient \(e\) toward this distinguished side.

The oriented decomposition tree has a sink. If the sink is an internal node with incident edges \(e_1,e_2,e_3\), then
\[
Z_{e_1}\cup Z_{e_2}\cup Z_{e_3}
\]
meets every bramble member. Otherwise, a bramble member avoiding this union would have to lie simultaneously in the three sink sides, whose intersection is empty. Thus the bramble has order at most \(3b\). If the sink is a leaf corresponding to a vertex \(v\), then \(Z_e\cup\{v\}\) meets the bramble, again with size at most \(3b\) when \(b\ge1\).

By treewidth–bramble duality,
\[
\operatorname{tw}(G)+1\le 3b,
\]
which is the desired bound. The queue-number estimate follows from bounded treewidth. \(\square\)

## Consequences

1. If a graph class has rank-width at most \(k\) and degeneracy at most \(r\), then it excludes \(K_{r+1,r+1}\), and
   \[
   \operatorname{qn}(G)
   \le
   2^{\,3r(2^k-1)-1}-1.
   \]

2. The same applies to bounded maximum degree.

3. Since bounded clique-width and bounded rank-width are equivalent up to parameter functions, a sparse separating class must have unbounded rank-width and unbounded clique-width.

Therefore a counterexample must genuinely exploit the gap between twin-width and rank-width; bounded-rank-width constructions cannot work.

# 5. A group-theoretic positive result

The following gives an explicit queue layout for a broad group class.

## Proposition 5.1

Let \(\Gamma\) be finitely generated by a finite symmetric set \(S\). If \(\Gamma\) has a left-orderable subgroup \(H\) of finite index \(m\), then its Cayley graph has
\[
\operatorname{qn}(\operatorname{Cay}(\Gamma,S))
 \le 2m|S|.
\]

In particular, every virtually left-orderable group has finite queue-number.

### Proof

It is enough to use the left Cayley graph, since inversion identifies the usual right Cayley graph with a left Cayley graph.

Choose left-coset representatives
\[
\Gamma=t_1H\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}t_mH.
\]
Order the cosets as consecutive blocks, and within \(t_iH\) use the given left-invariant order of \(H\):
\[
t_i h<t_i h' \quad\Longleftrightarrow\quad h<h'.
\]

Fix \(s\in S\) and a source coset \(t_iH\). There is a target coset \(t_jH\) and an element \(a_{s,i}\in H\) such that
\[
s t_i=t_j a_{s,i}.
\]
Consequently left multiplication by \(s\) sends
\[
t_i h\longmapsto t_j a_{s,i}h.
\]
The coordinate map \(h\mapsto a_{s,i}h\) is increasing because the order on \(H\) is left-invariant.

If \(i\ne j\), the corresponding edges join two distinct ordered blocks, and both endpoint orders agree. Therefore they form one queue.

If \(i=j\), split the edges into
\[
h<a_{s,i}h
\qquad\text{and}\qquad
h>a_{s,i}h.
\]
Each subfamily is a queue: for two increasing inputs \(h<h'\), the corresponding outputs also satisfy
\[
a_{s,i}h<a_{s,i}h',
\]
which rules out strict containment of the two edge intervals when their directions agree.

There are \(m|S|\) pairs \((s,i)\), and at most two queues per pair. Duplicate representations of an undirected edge may simply be assigned to one of the covering families. \(\square\)

This covers, among others, all left-orderable and virtually left-orderable groups. Hence a group separation cannot come from this class. The argument does not address the stronger “uniform queue-number” variant if that variant requires a bound independent of the generating data.

# 6. A subdivision transfer lemma

Subdivisions are a natural possible source of sparse bounded-twin-width examples. The following quantifies what would be needed.

## Proposition 6.1

Let \(H\) be obtained from \(G\) by replacing every edge by an internally vertex-disjoint path of length at most \(\ell\). If
\[
\operatorname{qn}(H)\le q,
\]
then
\[
\operatorname{qn}(G)
 \le \sum_{r=1}^{\ell}(2q)^r
 <2(2q)^\ell
\]
for \(q\ge1\).

### Proof

Fix a \(q\)-queue layout of \(H\), and restrict its vertex order to the branch vertices \(V(G)\).

Consider a rainbow of \(k\) edges of \(G\):
\[
a_1<\cdots<a_k<b_k<\cdots<b_1.
\]
The corresponding subdivision paths are pairwise vertex-disjoint. Orient the path corresponding to \(a_i b_i\) from \(a_i\) to \(b_i\). Its **signature** records:

- its length \(r\le\ell\);
- for every path edge, its queue color;
- whether that path edge goes forward or backward in the vertex order of \(H\).

There are at most
\[
\sum_{r=1}^{\ell}(2q)^r
\]
possible signatures.

Two paths in the rainbow cannot have the same signature. Indeed, suppose their starting vertices satisfy \(x_0<y_0\). Inductively assume \(x_j<y_j\). Their next edges have the same queue color and the same direction. If both point forward, reversing the order of their next vertices would give
\[
x_j<y_j<y_{j+1}<x_{j+1},
\]
a forbidden nesting. If both point backward, a reversal similarly gives one edge strictly containing the other. Hence
\[
x_{j+1}<y_{j+1}.
\]
Induction would preserve the order of the two paths' endpoints, contradicting the reversed order of the right endpoints in the original rainbow.

Thus every path in the rainbow has a distinct signature, proving the bound. \(\square\)

For every fixed \(\ell\), bounded-length subdivision preserves unbounded queue-number. Consequently, a separation would follow if one could find a bounded-degree class of unbounded queue-number whose fixed-length subdivisions have uniformly bounded twin-width.

On the other hand, the exponential dependence on \(\ell\) explains why logarithmic-length subdivision constructions are insufficient by themselves: when \(\ell=\Theta(\log |V(G)|)\), the lower bound obtained by inverting Proposition 6.1 may remain constant.

# 7. Remaining gap

The central unresolved point is the following.

In a \(d\)-contraction sequence, red degree controls the number of red **bags**, whereas queue layouts must control large nested families of individual edges. In a general branching contraction sequence, one red bag may contain arbitrarily many endpoints with complicated mixed adjacency. Neither bounded degree nor \(K_{t,t}\)-exclusion directly bounds this contribution:

- bounded degree limits each vertex locally, but not the number of vertices in the red bag;
- \(K_{t,t}\)-exclusion controls complete bipartite pairs, but a red pair is precisely one with non-homogeneous adjacency.

Theorem 3.1 works only when the future side consists of singleton bags, or more generally when only boundedly many prefix bags face singleton future vertices. Theorem 4.1 works because cut-rank bounds the total number of neighborhood types, which ordinary twin-width does not provide.

Thus the original problem remains open. The partial results show that a separating class must, at minimum:

1. use genuinely branching contraction sequences with unbounded active front;
2. have unbounded rank-width and clique-width;
3. avoid the virtually left-orderable group setting if the example is a group; and
4. if based on subdivisions, either use a fixed/sublogarithmic subdivision with bounded twin-width or require a substantially sharper queue-number transfer argument than Proposition 6.1.