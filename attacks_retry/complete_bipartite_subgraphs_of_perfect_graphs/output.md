```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A depth-independent split-composition lemma proves the desired bound for a strictly larger decomposable subclass than the one in the supplied attempt.",
  "would_publish": false,
  "caveats": "This does not improve the unrestricted perfect-graph bound; the comparability extension uses the Fox bound supplied in the question, and novelty is not claimed."
}
```

# 1. Result and scope

I do not resolve the conjecture. I extend the supplied construction from substitutions to **split compositions, also called 1-joins**. The extension is genuine: below I give an explicit 48-vertex perfect graph covered by the new theorem but not by the structural class in the supplied attempt.

The principal result is an abstract transfer lemma: a suitable weighted homogeneous-pair bound for the labels of a split-decomposition tree transfers to the whole graph with a constant loss, independently of the depth of the tree.

I checked the weighted line-graph calculation and the blow-up rounding idea in the supplied attempt. Versions of both are proved below; its conclusions are not used as black boxes.

For disjoint vertex sets \(A,B\), call \((A,B)\) a **pure pair** if \(A\) is complete or anticomplete to \(B\). Define
\[
b(G)=\max\{\min(|A|,|B|):(A,B)\text{ is a pure pair in }G\},
\]
with \(b(G)=0\) when \(|V(G)|\le 1\). Thus \(b(G)=b(\overline G)\), and the original question asks whether
\[
b(G)\ge n^{1-o(1)}
\]
for every perfect \(n\)-vertex graph.

## The base classes

Let \(\mathcal B\) consist of:

1. perfect graphs partitionable into at most four cliques or independent sets;
2. line graphs of bipartite loopless multigraphs, and their complements.

Let
\[
\mathcal C=\mathcal B\cup
\{\text{comparability and cocomparability graphs}\}.
\]

For a graph class \(\mathcal X\), let \(\mathcal X^+\) consist of its members and their extensions by one new universal vertex.

The comparability part uses the following input supplied with the problem, in its complement-symmetric form:
\[
\tag{F}
b(H)\ge c_F\frac{m}{\log_2(2m)}
\]
for every comparability graph \(H\) on \(m\ge2\) vertices, where \(c_F>0\) is absolute. The literal formulation about a biclique in \(H\) alone cannot hold for an edgeless comparability graph. The linear theorem below does not use (F).

## Split composition

Given disjoint graphs \(H_1,H_2\), each with a marked vertex \(x_i\), their **1-join** is obtained by deleting \(x_1,x_2\), retaining all other edges, and making
\[
N_{H_1}(x_1)\quad\text{complete to}\quad N_{H_2}(x_2).
\]
There are no other edges between the two remaining vertex sets.

We use the following precise tree representation of iterated 1-joins.

A **graph-labelled tree** is a tree \(T\) whose leaves are the vertices of the resulting graph. Each internal node \(x\) has a label graph \(H_x\), with one label vertex for every edge incident with \(x\). Distinct leaves \(u,v\) are adjacent if, at every internal node on their tree path, the two label vertices corresponding to the entering and leaving edges are adjacent.

Write \(\operatorname{Split}(\mathcal L)\) for the graphs represented this way with all labels in \(\mathcal L\), including the trivial graphs. Contracting an edge between two internal nodes performs precisely a 1-join of their labels.

Finally, \(\operatorname{CS}(\mathcal Y)\) denotes repeated clique-sums of graphs in \(\mathcal Y\): two operands overlap in a clique, all their edges are retained, and no edges are added between their exclusive vertex sets.

Set
\[
\mathcal D_{\mathcal X}
=\operatorname{CS}\bigl(\operatorname{Split}(\mathcal X^+)\bigr).
\]

### Theorem

Put
\[
\lambda=\min\{1/32,c_F/2\}.
\]
For every \(n\ge1\):

1. Every \(G\in\mathcal D_{\mathcal B}\) satisfies
   \[
   b(G)\ge \left\lfloor\frac n{256}\right\rfloor.
   \]
2. Using (F), every \(G\in\mathcal D_{\mathcal C}\) satisfies
   \[
   b(G)\ge
   \left\lfloor
   \lambda\frac n{8\log_2(2n)}
   \right\rfloor.
   \]

All graphs in these two classes are perfect.

The order of operations is part of the statement: first split composition of the specified labels, then clique-sums. Arbitrary alternation of unrelated decomposition operations is not asserted.

# 2. Perfection and inclusion of the earlier construction

## 2.1. A 1-join of perfect marked graphs is perfect

Here the marked vertices belong to the perfect operands; perfection of the two graphs after deleting their markers would not suffice.

Write
\[
X_i=V(H_i)\setminus\{x_i\},\qquad A_i=N_{H_i}(x_i).
\]
Consider any induced subgraph of the 1-join, restricting these sets accordingly. Its clique number is
\[
k=\max\{\omega(X_1),\omega(X_2),\omega(A_1)+\omega(A_2)\}.
\]

Use the standard replication lemma for perfect graphs: replacing a vertex by a clique preserves perfection. In the first marked operand, replace \(x_1\) by a clique of size \(k-\omega(A_1)\), interpreting size zero as deletion. The resulting perfect graph has clique number at most \(k\). A \(k\)-coloring therefore colors \(A_1\) with at most \(\omega(A_1)\) colors: it must avoid all colors on the replicated marker clique.

Similarly, \(X_2\) can be \(k\)-colored with \(A_2\) using at most \(\omega(A_2)\) colors. Permute the two palettes so that the colors on \(A_1\) and \(A_2\) are disjoint. This is possible because
\[
\omega(A_1)+\omega(A_2)\le k.
\]
The colorings now combine into a proper \(k\)-coloring of the 1-join.

This works for every induced subgraph, proving perfection.

The base classes are perfect, as are their universal-vertex extensions. Thus contracting the internal edges of a graph-labelled tree proves that every graph in \(\operatorname{Split}(\mathcal X^+)\), for \(\mathcal X=\mathcal B,\mathcal C\), is perfect. Clique-sums preserve perfection by permuting optimal colorings to agree on the common clique.

## 2.2. Substitution is included

Let \(\operatorname{Sub}(\mathcal X)\) denote finite substitution composites with quotient graphs in \(\mathcal X\).

A substitution tree becomes a graph-labelled tree as follows:

- the root label is its quotient graph;
- at every other internal node, add a universal label vertex corresponding to the edge toward its parent;
- the remaining label vertices correspond to its children.

The path-adjacency rule is exactly the adjacency rule for substitution. Consequently,
\[
\operatorname{Sub}(\mathcal X)
\subseteq \operatorname{Split}(\mathcal X^+),
\]
and hence
\[
\operatorname{CS}(\operatorname{Sub}(\mathcal X))
\subseteq \mathcal D_{\mathcal X}.
\]

Section 6 proves that this inclusion is strict for both base classes under consideration.

# 3. Weighted bounds for the labels

Weights in this section are positive integers, except that the first lemma also holds for positive real weights. Their sum is \(W\), and \(w(S)\) denotes the weight of a vertex set \(S\).

Zero-weight label vertices may simply be discarded; all the label classes used here are hereditary.

## Lemma 1: basic labels, including universal extensions

For every weighted \(H\in\mathcal B^+\), either

- a vertex has weight at least \(W/32\), or
- \(H\) has a pure pair with both weights at least \(W/32\).

### Proof

Assume every vertex weight is less than
\[
\tau=W/32.
\]

**At most five homogeneous parts.**  
A universal extension of a graph with four homogeneous parts has at most five such parts. One part has weight at least \(W/5\). Greedily select vertices from that part until their weight first reaches \(\tau\). The selected weight is less than \(2\tau\), and the remaining weight exceeds
\[
W/5-2\tau>\tau.
\]
Splitting the part gives the required pair.

**A line graph, with at most one exceptional vertex.**  
After possibly complementing \(H\) and deleting its added vertex, the remaining graph is \(L(F)\), where \(F\) is a loopless multigraph. Regard its vertex weights as edge weights of \(F\). Their total \(M\) satisfies
\[
M>31W/32.
\]
If there is no exceptional vertex, take \(M=W\).

Set
\[
d_w(x)=\sum_{e\ni x}w(e),\qquad \Delta_w=\max_xd_w(x).
\]

If \(\Delta_w\ge W/8=4\tau\), the edges incident with a corresponding vertex form a clique of weight at least \(4\tau\). Greedily splitting this clique, as above, gives two sides of weight at least \(\tau\).

Suppose \(\Delta_w<W/8\). Color the vertices of \(F\) independently red or blue with probability \(1/2\). Let \(X\) and \(Y\) be the total weights of edges with two red and two blue endpoints, respectively. Then
\[
\mathbb E[XY]
=\frac1{16}\sum_{e\cap f=\varnothing}w(e)w(f),
\]
where the sum is over ordered pairs.

Every ordered pair of intersecting edges is counted at least once in \(\sum_xd_w(x)^2\), including parallel edges. Hence
\[
\begin{aligned}
\sum_{e\cap f=\varnothing}w(e)w(f)
&\ge M^2-\sum_xd_w(x)^2\\
&\ge M^2-2\Delta_wM\\
&>M(M-W/4)\\
&>W^2/2.
\end{aligned}
\]
The last inequality follows from \(M>31W/32\).

Thus some coloring has
\[
XY>W^2/32.
\]
Since \(X,Y\le W\), both exceed \(W/32\). The two corresponding edge families are anticomplete in \(L(F)\).

Complementation preserves the pure-pair conclusion. ∎

## Lemma 2: rounding independent blow-ups

Replace each vertex \(i\) of a graph \(H\) by an independent set of integer size \(w_i\). Suppose the blow-up has a pure pair \((P,Q)\) with
\[
|P|,|Q|\ge t,
\]
and every \(w_i<t/2\). Then the weighted graph \(H\) has a pure pair with both weights at least \(t/2\).

### Proof

If \(P,Q\) are complete to each other, they cannot meet the same replacement set. Their supports give the desired complete pair, with both weights at least \(t\).

Suppose they are anticomplete. Let \(S,T,R\) be the indices of replacement sets meeting only \(P\), only \(Q\), and both, respectively. Then \(S,T\), \(S,R\), and \(T,R\) are anticomplete pairs, and \(R\) is independent. Moreover,
\[
\begin{split}
w(S)+w(R)&\ge t,\\
w(T)+w(R)&\ge t,\\
w(S)+w(T)+w(R)&\ge2t.
\end{split}
\]
The last inequality uses the disjointness of \(P,Q\).

If \(w(S),w(T)\ge t/2\), we are done. Otherwise, say \(w(S)<t/2\), add vertices of \(R\) to \(S\) until its weight first reaches \(t/2\). This is possible by the first inequality. The resulting weight is less than \(t\), because each added weight is less than \(t/2\). The unused vertices of \(T\cup R\) have total weight greater than \(t\). These are the two required anticomplete sides. ∎

## Lemma 3: comparability labels

Using (F), every integer-weighted \(H\in\mathcal C^+\) has either

- a vertex of weight at least
  \[
  h(W)=\lambda\frac W{\log_2(2W)},
  \]
  or
- a pure pair with both weights at least \(h(W)\).

### Proof

Assume every vertex weight is less than \(h(W)\).

If \(H\in\mathcal B^+\), Lemma 1 applies because \(h(W)\le W/32\).

Otherwise \(H\) is a comparability or cocomparability graph. Indeed, universal extensions preserve both classes: add a greatest element to a poset for the comparability case, or an element incomparable with every existing element for the cocomparability case.

Independent blow-ups also preserve both classes:

- replace a poset element by an antichain for a comparability graph;
- replace it by a chain for a cocomparability graph.

The independent blow-up has \(W\) vertices. By (F) and complement invariance, it has a pure pair with both sides at least
\[
t=c_F\frac W{\log_2(2W)}.
\]
Every replacement set has size less than \(h(W)\le t/2\). Lemma 2 gives a weighted pure pair with both weights at least \(t/2\ge h(W)\).

For \(W=1\), the heavy-vertex alternative holds automatically. ∎

# 4. The split-composition transfer lemma

This is the main additional argument.

## Lemma 4

Let \(\mathcal L\) be a hereditary graph class. Suppose \(f\) is a positive function on the positive integers such that

\[
f(W)\le W/32,
\qquad
\frac{f(W)}W\text{ is nonincreasing},
\]
and every integer-weighted graph in \(\mathcal L\), of total weight \(W\), has either

- a vertex of weight at least \(f(W)\), or
- a pure pair with both weights at least \(f(W)\).

Then every \(n\)-vertex graph \(G\in\operatorname{Split}(\mathcal L)\) satisfies
\[
b(G)\ge \left\lfloor\frac{f(n)}2\right\rfloor.
\]

No perfection assumption is needed for this transfer.

### Proof

The statement is immediate for \(n\le2\). Let \(n\ge3\), and take a graph-labelled tree representing \(G\).

Give each leaf weight one and each internal node weight zero. Choose a weighted centroid \(x\). It is internal, and every branch of \(T-x\) contains at most \(n/2\) leaves. Let their leaf sets be
\[
V_1,\ldots,V_k,\qquad s_i=|V_i|\le n/2.
\]

For each branch, let \(U_i\subseteq V_i\) consist of the leaves for which all label-adjacency tests along the path to \(x\), excluding the test at \(x\), succeed. Put
\[
R_i=V_i\setminus U_i.
\]

Identify the vertices of the label \(H_x\) with the branches. The path rule gives, for \(u\in V_i,v\in V_j\), \(i\ne j\),
\[
\tag{1}
uv\in E(G)
\quad\Longleftrightarrow\quad
u\in U_i,\ v\in U_j,\ ij\in E(H_x).
\]
In particular, every vertex of \(R_i\) is anticomplete to \(V(G)\setminus V_i\).

Let
\[
R=\sum_i|R_i|,
\qquad
W=\sum_i|U_i|=n-R.
\]

### Case 1: \(R\ge n/2\)

Independently color the branches red or blue with probability \(1/2\). Define
\[
P=\bigcup_{\text{red }i}R_i,
\qquad
Q=\bigcup_{\text{blue }j}V_j.
\]
They are anticomplete. Furthermore,
\[
\begin{aligned}
\mathbb E[|P||Q|]
&=\frac14\sum_i |R_i|(n-s_i)\\
&\ge \frac{nR}{8}\\
&\ge \frac{n^2}{16}.
\end{aligned}
\]
Thus some choice has \(|P||Q|\ge n^2/16\). Since each side has order at most \(n\), both have order at least \(n/16\), more than required.

### Case 2: \(W>n/2\)

Give label vertex \(i\) weight \(|U_i|\), discarding zero-weight vertices.

If the weighted label has a pure pair of weight at least \(f(W)\), take the corresponding unions of the \(U_i\). Equation (1) shows that these unions form a pure pair in \(G\).

Otherwise, some \(U_i\) has size at least \(f(W)\). Every vertex outside \(V_i\) is either complete or anticomplete to \(U_i\), again by (1). There are at least \(n/2\) vertices outside \(V_i\), so one of these two classes has size at least \(n/4\). Since
\[
f(W)\le W/32\le n/32,
\]
this gives a pure pair with both sides at least \(f(W)\).

Finally,
\[
f(W)\ge \frac Wn f(n)>\frac{f(n)}2.
\]
This proves the lemma. ∎

The active/inactive distinction is essential. The leaves of a branch need not form a module. Its active leaves have a uniform relationship to each outside vertex, while its inactive leaves have no outside neighbors. The proof handles both possibilities without descending further into the tree.

# 5. Clique-sums and completion of the theorem

## Lemma 5

For any tree decomposition of an \(n\)-vertex graph, either

- there is an anticomplete pair with both sides of order at least \(n/4\), or
- some bag has order at least \(n/4\).

### Proof

Assign each graph vertex to one bag containing it, and take a weighted centroid \(x\) of the decomposition tree. Every component after deleting \(x\) has assigned weight at most \(n/2\).

A vertex outside the bag \(B_x\) occurs only in bags in one such component. Let the resulting vertex sets be \(V_1,\ldots,V_r\). They are pairwise anticomplete and satisfy \(|V_i|\le n/2\).

If \(|B_x|\ge n/4\), we are done. Otherwise their total size exceeds \(3n/4\). If some \(V_i\) has size between \(n/4\) and \(n/2\), use it and the union of the others. If all have size below \(n/4\), greedily combine them until their union first reaches \(n/4\). That union has size below \(n/2\), and the remaining union has size above \(n/4\). ∎

A clique-sum construction gives a tree decomposition whose bags induce its original pieces. Inductively, join bags containing the common clique. Such bags exist because the subtrees representing the vertices of a clique pairwise intersect and hence have a common intersection.

Combining Lemmas 4 and 5 gives the following general conclusion under the hypotheses of Lemma 4:
\[
\tag{2}
G\in\operatorname{CS}(\operatorname{Split}(\mathcal L))
\quad\Longrightarrow\quad
b(G)\ge\left\lfloor\frac{f(n)}8\right\rfloor.
\]
Indeed, a bag of order \(m\ge n/4\) supplies a pair of size at least
\[
\left\lfloor \frac{f(m)}2\right\rfloor
\ge
\left\lfloor\frac{m}{2n}f(n)\right\rfloor
\ge
\left\lfloor\frac{f(n)}8\right\rfloor.
\]

Apply (2) first with
\[
\mathcal L=\mathcal B^+,\qquad f(W)=W/32,
\]
using Lemma 1. This gives \(b(G)\ge\lfloor n/256\rfloor\).

Next apply it with
\[
\mathcal L=\mathcal C^+,\qquad
f(W)=\lambda W/\log_2(2W),
\]
using Lemma 3. Both required properties of \(f\) hold, giving
\[
b(G)\ge
\left\lfloor\lambda\frac n{8\log_2(2n)}\right\rfloor.
\]
This completes the theorem.

# 6. An explicit graph newly covered by the theorem

Here is a strictness example, not a counterexample to the conjecture.

Let \(R_5=L(K_{5,5})\), the rook graph on \([5]\times[5]\): two cells are adjacent when they share a row or column. Take two copies, mark \((1,1)\) in each, and perform their 1-join.

Call the resulting graph \(G\). Its two sides \(X_1,X_2\) each induce
\[
Q=R_5-(1,1).
\]
In each side, write
\[
A_i=\{(1,c)_i:c\ne1\}\cup\{(r,1)_i:r\ne1\},
\qquad
Z_i=\{(r,c)_i:r,c\ne1\}.
\]
The only cross-edges are all edges between \(A_1\) and \(A_2\).

Thus
\[
|V(G)|=48,\qquad
G\in\operatorname{Split}(\mathcal B)\subseteq\mathcal D_{\mathcal B},
\]
and \(G\) is perfect by Section 2.

I verify that
\[
G\notin\operatorname{CS}(\operatorname{Sub}(\mathcal C)),
\]
the larger of the two classes treated in the supplied attempt.

## 6.1. \(G\notin\mathcal C\)

Each \(X_i\) has independence number at most \(5\), so \(\alpha(G)\le10\). A clique lying in one side has size at most \(5\). A clique meeting both sides lies in \(A_1\cup A_2\); each \(A_i\) induces two anticomplete \(K_4\)'s, so it has size at most \(8\). Thus every clique or independent set has at most ten vertices. Four such sets cannot cover all 48 vertices.

The graph is not a line graph: the vertex \((1,2)_1\) is the center of a claw with leaves
\[
(2,2)_1,\quad (1,2)_2,\quad (2,1)_2.
\]
Its complement is not a line graph either: in \(Z_1\), the three vertices
\[
(2,2)_1,\ (2,3)_1,\ (2,4)_1
\]
form a triangle anticomplete to \((3,5)_1\), giving an induced complement of a claw.

It is not a comparability graph. It contains an induced \(R_3\). In a transitive orientation of a row triangle of \(R_3\), its middle vertex has an incoming and an outgoing row edge. Either direction of an incident column edge then creates a directed two-edge path whose endpoints are nonadjacent.

It is not a cocomparability graph. The same \(R_3\) contains an induced \(C_6\). Its complement is a triangular prism, which has no transitive orientation: the middle vertex of either oriented triangle has a matching neighbor, and either orientation of that matching edge creates the same obstruction.

These observations exclude every member type in \(\mathcal C\).

## 6.2. \(G\) has no nontrivial module

First, \(Q=R_5-(1,1)\) is prime.

If a module contains two adjacent cells, a cell in the column of one and outside their common row distinguishes the two and must also belong to the module. This produces an induced three-vertex path. If it initially contains two nonadjacent cells, a suitable third cell adjacent to exactly one first produces an adjacent pair, and the same argument applies.

An induced three-vertex path in a rook graph has no vertex adjacent to all three. Therefore a module containing such a path is anticomplete to its complement. Since \(Q\) is connected, that module must be all of \(Q\).

Now let \(M\) be a module of \(G\). Each \(M\cap X_i\) is a module of \(Q\). If one intersection contains at least two vertices, it equals \(X_i\). Every vertex of \(A_{3-i}\) distinguishes \(A_i\) from \(Z_i\), so all of \(A_{3-i}\) must then lie in \(M\); primeness of the other \(Q\) forces \(M=V(G)\).

A remaining nontrivial proper module would therefore consist of one vertex from each side. This is impossible: every vertex of \(X_i\) has a neighbor in \(Z_i\), whereas every vertex of the opposite side is anticomplete to \(Z_i\).

## 6.3. \(G\) has no clique cutset

For any clique \(K\) of \(G\), each \(K\cap X_i\) is contained in a row or a column. Removing such a clique from \(Q\) leaves a connected graph. One way to see this is in \(K_{5,5}\): deleting some edges incident with one vertex, together with the already deleted marked edge, leaves its nonisolated part connected.

Also, \(K\cap X_i\) cannot cover \(A_i\), since \(A_i\) contains two nonempty anticomplete \(K_4\)'s. Consequently, after deleting \(K\), the two connected remaining sides still have a cross-edge. Hence \(G-K\) is connected.

A graph with no clique cutset cannot be a nontrivial clique-sum. A prime graph cannot be a nontrivial substitution. Thus membership of \(G\) in \(\operatorname{CS}(\operatorname{Sub}(\mathcal C))\) would force \(G\in\mathcal C\), contrary to Section 6.1.

This proves the claimed strict extension.

# 7. What remains unresolved

The theorem does not supply a decomposition of an arbitrary perfect graph into the allowed pieces.

In particular:

- a general 2-join has two cross-edge rectangles, not the single rectangle used in a split;
- marker-path replacements in general 2-join decompositions are not automatically graph-labelled trees of the form used here;
- balanced skew partitions need not be splits or clique separators.

No argument above reorganizes these phenomena into an allowed construction. Therefore the strong perfect graph theorem does not complete this proof.

For unrestricted perfect graphs, the bound justified here remains
\[
b(G)\ge\left\lfloor\frac{\sqrt n}{2}\right\rfloor:
\]
perfection gives \(\chi(G)=\omega(G)\), so \(\alpha(G)\omega(G)\ge n\), and one can split a clique or independent set of order at least \(\sqrt n\).

The progress is consequently structural: **weighted near-linear bounds survive arbitrarily deep split composition, followed by clique-sums, with only a constant loss**, and this covers graphs outside the subclass established in the supplied attempt.