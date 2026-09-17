```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds at maximum degree six if deleting at most three vertices makes the degree-six subgraph bipartite, and hence if there are at most eleven degree-six vertices.",
  "would_publish": false,
  "caveats": "A structural special case, not a resolution; novelty and current literature status have not been independently checked."
}
```

## 1. Result

All graphs are finite and simple. Write
\[
H_k(G)=G[\{v:d_G(v)=k\}].
\]

I prove the following extension of the supplied attempt’s two-vertex criterion.

**Theorem.** Let \(q\ge 3\), let \(G\) be triangle-free with maximum degree at most \(q+1\), and put \(H=H_{q+1}(G)\). If
\[
\chi(H-S)\le q-3
\]
for some \(S\subseteq V(H)\) with \(|S|\le 3\), then \(G\) is \(q\)-colorable.

Here, a graph is \(0\)-colorable precisely when it is empty.

For \(q=5\), this gives the main partial result.

**Corollary 1.** A triangle-free graph of maximum degree at most six is \(5\)-colorable if its degree-six subgraph can be made bipartite by deleting at most three vertices.

An elementary small-order argument gives:

**Corollary 2.** A triangle-free graph of maximum degree at most six with at most eleven degree-six vertices is \(5\)-colorable.

Consequently, a counterexample at \(\Delta=6\) must satisfy
\[
|V(H_6(G))|\ge 12,
\qquad
\operatorname{oct}(H_6(G))\ge 4,
\]
where \(\operatorname{oct}\) denotes the minimum number of vertices whose deletion makes a graph bipartite. These bounds are not claimed to be best known.

The list-coloring mechanism from the supplied attempt is proved again below. The additional ingredient is a two-color lemma for uncolorable degree-list assignments; it handles the difficult case where the three exceptional vertices induce exactly one edge.

---

## 2. Degree-list tools

An \(A\)-coloring assigns each vertex \(v\) a color from its list \(A(v)\), properly.

Call a block an **end block** if it contains at most one cutvertex. Thus a graph consisting of one block has that block as an end block.

### Lemma 1: structure of an uncolorable degree-list assignment

Let \(F\) be connected and triangle-free, and suppose
\[
|A(v)|\ge d_F(v)\qquad(v\in V(F)).
\]
If \(F\) is not \(A\)-colorable, then:

1. \(|A(v)|=d_F(v)\) for every vertex;
2. every block is an edge or an odd cycle, except for the possible one-vertex graph;
3. for each block \(B\), there is a color set \(C_B\), of size one for an edge and two for an odd cycle, such that
   \[
   A(v)=\mathop{\dot\bigcup}_{B\ni v} C_B.
   \tag{1}
   \]
   In particular, the block color sets incident with any vertex are pairwise disjoint.

**Proof.** We first record two greedy observations.

If \(|A(z)|>d_F(z)\), root a spanning tree at \(z\) and color children before parents. Every vertex other than \(z\) has an uncolored neighbor when it is colored, and \(z\) has a spare color at the end. Thus an uncolorable assignment has equality everywhere.

Also, if \(uv\in E(F)\), \(F-u\) is connected, and
\[
A(u)\setminus A(v)\ne\varnothing,
\tag{2}
\]
color \(u\) with a color in this difference and then greedily color \(F-u\) toward \(v\). At the last vertex \(v\), the color on \(u\) does not forbid a color from \(A(v)\). This gives an \(A\)-coloring.

Suppose a block \(B\) is neither complete nor an odd cycle. Greedily color the vertices outside \(B\) in decreasing order of distance from \(B\). The residual lists on \(B\) have size at least the corresponding degrees in \(B\). If those lists are not all identical, apply (2) to an adjacent pair with different lists, using the 2-connectivity of \(B\). If they are identical, their common size is at least \(\Delta(B)\), and Brooks’ theorem colors \(B\). Hence every block of an uncolorable graph is complete or an odd cycle. Triangle-freeness leaves only edges and odd cycles.

It remains to obtain (1). This follows by stripping end blocks.

For an end edge \(xz\), with \(x\) a non-cutvertex, write \(A(x)=\{c\}\). Observation (2) implies \(c\in A(z)\). Delete \(x\) and delete \(c\) from \(A(z)\). The resulting degree-list assignment remains uncolorable, since any coloring of it extends by giving \(x\) color \(c\).

For an end odd cycle with cutvertex \(z\), all its non-cutvertices have identical two-element lists: otherwise (2) applies along their path. Write their common list as \(\{a,b\}\). Applying (2) at a non-cutvertex adjacent to \(z\) shows
\[
\{a,b\}\subseteq A(z).
\]
Delete the non-cutvertices of the cycle and delete \(a,b\) from \(A(z)\). Again the resulting assignment is uncolorable: a coloring of the remainder gives \(z\) a color outside \(\{a,b\}\), after which the deleted path can be colored with \(a,b\).

Induction, including the single-block cases, proves (1). ∎

### Lemma 2: two nearly universal colors

Let \(F,A\) satisfy the hypotheses of Lemma 1, and suppose \(F\) is not \(A\)-colorable. Let \(\beta,\gamma\) be distinct colors such that
\[
\gamma\in A(v)\quad\text{for every }v,
\qquad
|\{v:\beta\notin A(v)\}|\le 3.
\tag{3}
\]
Then either:

- \(F\) has an odd-cycle end block; or
- \(F\) is a path on an even number of vertices, its endpoint lists are \(\{\gamma\}\), and all its internal lists are \(\{\beta,\gamma\}\).

**Proof.** Use the block color sets from Lemma 1. Every vertex belongs to exactly one block whose color set contains \(\gamma\), and to at most one whose color set contains \(\beta\).

Construct an auxiliary graph using the blocks whose color sets contain exactly one of \(\beta,\gamma\):

- a vertex belonging to distinct \(\gamma\)- and \(\beta\)-blocks supplies an edge between those block-nodes;
- a vertex whose list omits \(\beta\) supplies a new leaf adjacent to its \(\gamma\)-block.

This auxiliary graph is a forest: it is obtained from a subgraph of the block–vertex incidence tree by suppressing degree-two vertex-nodes. Each block-node has degree \(|V(B)|\), hence degree two for an edge block and at least five for a cycle block. Its leaves are exactly the vertices whose lists omit \(\beta\).

A tree containing a vertex of degree at least five has at least five leaves. By (3), no block containing exactly one of \(\beta,\gamma\) can therefore be a cycle. Moreover, there is at most one auxiliary component, since each component has at least two leaves. Consequently, all the one-color blocks together form at most one path \(Q\), whose edge colors alternate \(\gamma,\beta\), beginning and ending with \(\gamma\).

Every remaining \(\gamma\)-block contains both colors and is therefore an odd cycle. The path \(Q\), if present, and these odd cycles partition \(V(F)\).

Contract these pieces in the block–vertex incidence tree. Every remaining block-node has degree at least two. If a piece other than \(Q\) exists, the resulting tree has an odd-cycle piece as a leaf—also allowing the one-piece case. That cycle is an end block of \(F\).

Otherwise \(F=Q\). Its alternating edge-block colors give exactly the path and lists stated in the lemma. ∎

---

## 3. Proof of the theorem

Put
\[
r=q-3,\qquad H=H_{q+1}(G),\qquad L=V(G)\setminus V(H).
\]
Choose \(S\) inclusion-minimal subject to \(|S|\le3\) and \(\chi(H-S)\le r\), and fix an \(r\)-coloring of \(H-S\).

Call its colors **ordinary**, and reserve three additional colors
\[
\alpha,\beta,\gamma.
\]

### 3.1. Neighbor budgets and residual lists

For \(s\in S\), minimality implies
\[
|N(s)\cap(V(H)\setminus S)|\ge r.
\]
For \(r>0\), otherwise the fixed coloring of \(H-S\) could be extended to \(s\); for \(r=0\), the inequality is automatic. Hence, writing \(d_L(s)=|N(s)\cap L|\) and \(d_S(s)=|N(s)\cap S|\),
\[
d_L(s)\le (r+4)-r-d_S(s)=4-d_S(s).
\tag{4}
\]

After any proper precoloring of \(H\), give \(v\in L\) the residual list
\[
A(v)=\{\text{all }q\text{ colors}\}
       \setminus\{\text{colors on }N(v)\cap V(H)\}.
\]
Since \(d_G(v)\le q\),
\[
|A(v)|\ge q-|N(v)\cap V(H)|\ge d_{G[L]}(v).
\tag{5}
\]

If a component \(F\) of \(G[L]\) is uncolorable, Lemma 1 makes both inequalities in (5) equalities at every vertex of \(F\). Therefore
\[
d_G(v)=q,
\quad\text{and all neighbors of }v\text{ in }H
\text{ have distinct colors}.
\tag{6}
\]
In particular, a repeated color among the high-degree neighbors of one vertex makes its whole component list-colorable.

We will also use the following simple extension observation.

**Reserved-color observation.** If the vertices of \(S\) receive distinct reserved colors, and every vertex of \(L\) has at most one neighbor in \(S\), the coloring extends.

Indeed, every residual list then has size at least two. An uncolorable component would have an odd-cycle end block. Adjacent non-cutvertices on it would have identical two-element lists. Their common forbidden set has size \(q-2=r+1\), so it includes a reserved color. Because every reserved color is used at a unique vertex of \(S\), those adjacent vertices would have a common neighbor in \(S\), creating a triangle.

### 3.2. Sets of size at most two

If \(|S|\le1\), or \(S\) consists of two adjacent vertices, the reserved-color observation applies. In the adjacent case, triangle-freeness prevents a low-degree vertex from being adjacent to both.

Suppose \(S=\{s,t\}\) is independent. Color both vertices \(\alpha\). All low-degree lists contain \(\beta,\gamma\).

If this does not extend, an uncolorable component \(F\) has minimum degree at least two, and all its end blocks are odd cycles. Every degree-two non-cutvertex has list \(\{\beta,\gamma\}\). By (6), it has exactly one neighbor in \(\{s,t\}\). Label it by that neighbor. Adjacent labeled vertices have different labels.

The component cannot be a single odd cycle, since its labels would give a proper 2-coloring. Thus it has at least two end cycles. Each contributes at least two neighbors of \(s\) and two of \(t\). By (4), this exhausts both four-neighbor budgets.

All low-degree neighbors of \(s,t\) are therefore among these non-cutvertices, each adjacent to exactly one of \(s,t\). Recoloring \(s,t\) with distinct reserved colors now satisfies the reserved-color observation.

This reproves the two-vertex case rather than assuming it from the supplied attempt.

### 3.3. Three-vertex pair patterns

For the remaining cases, let \(|S|=3\). A **pair pattern** means:

- a nonadjacent pair \(P\subset S\) receives color \(\alpha\);
- the remaining vertex \(w\) receives color \(\beta\);
- \(\gamma\) is unused on \(H\).

We record the consequences of an uncolorable low-degree component \(F\) under such a pattern.

**Edge end blocks.** If \(x\) is the non-cutvertex of an edge end block, then
\[
A(x)=\{\gamma\}.
\]
By (6), \(x\) has exactly one neighbor in \(P\), is adjacent to \(w\), and sees every ordinary color. Thus this end block supplies two incidences with \(S\).

**Odd-cycle end blocks.** The non-cutvertices of an odd-cycle end block have identical two-element lists. They contain \(\gamma\). They must also contain \(\beta\): otherwise adjacent non-cutvertices would both be adjacent to \(w\), forming a triangle. Thus their lists are
\[
\{\beta,\gamma\}.
\]
Each has exactly one neighbor in \(P\), and these neighbors alternate along the path of non-cutvertices. Consequently, the end block supplies at least two neighbors of each member of \(P\).

**There are at least two end blocks.** A one-vertex component is colorable because \(\gamma\) is available. A single edge cannot be uncolorable, since both endpoints would be adjacent to \(w\). A single odd cycle would have alternating labels from the two members of \(P\), which is impossible. Hence an uncolorable component has at least two blocks and at least two end blocks.

In particular, every such component uses at least four incidences with \(S\).

Two switching facts will be useful:

- If an uncolorable component has an odd-cycle end block, every different proper pair pattern splits its old pair \(P\). Adjacent non-cutvertices then have different residual lists, so the component becomes colorable by Lemma 1.
- If it has an edge end block whose non-cutvertex has \(S\)-neighbors \(a,b\), grouping \(a,b\) together gives a repeated high-neighbor color. By (5)–(6), the component becomes colorable. The pair \(a,b\) is nonadjacent because it has a common neighbor in a triangle-free graph.

In particular, when \(S\) is independent, every component is colorable under at least one of the three pair patterns.

### 3.4. Three independent exceptional vertices

Suppose \(S\) is independent. By (4),
\[
\sum_{s\in S}d_L(s)\le12.
\tag{7}
\]

Initially color all three vertices \(\alpha\). All residual lists contain \(\beta,\gamma\). If the coloring does not extend, choose an uncolorable component \(F_0\).

Every end block of \(F_0\) is an odd cycle, and each degree-two non-cutvertex has exactly one neighbor in \(S\). Thus \(F_0\) uses at least five incidences with \(S\): five if it is a single cycle, and at least eight if it has multiple blocks.

There are two possibilities.

**First possibility: \(F_0\) is uncolorable under some pair pattern.** Its minimum degree is at least two, so it has no edge end blocks. The pair-pattern observations therefore give at least four low-degree neighbors of each member of the chosen pair. By (4), both budgets are exhausted inside \(F_0\).

No other component can then be uncolorable under any pair pattern: every such obstruction uses at least two distinct vertices of \(S\), whereas outside \(F_0\) only the third vertex can have low-degree neighbors. Also, \(F_0\) becomes colorable under either other pair pattern. Choose one of them.

**Second possibility: \(F_0\) is colorable under all three pair patterns.** At most seven incidences with \(S\) remain outside \(F_0\), by (7). Every component uncolorable under some pair pattern uses at least four such incidences. Hence at most one other component can be uncolorable under any of the three patterns.

That component is colorable under at least one pattern, by the switching facts. Choose that pattern. All components are then colorable.

This handles independent \(S\).

### 3.5. The exceptional vertices induce a path

Suppose \(G[S]\) is the path \(s-t-u\). Use the pair pattern
\[
P=\{s,u\},\qquad w=t.
\]
By (4),
\[
d_L(s),d_L(u)\le3.
\]

An edge end block in an uncolorable component would require a low-degree vertex adjacent to \(t\) and one of \(s,u\), which creates a triangle. Thus every end block would be an odd cycle.

There would be at least two such end blocks, supplying at least four low-degree neighbors of each of \(s,u\), contrary to their budgets. The coloring therefore extends.

### 3.6. The exceptional vertices induce exactly one edge

This is the remaining case. Write
\[
S=\{s,t,u\},\qquad st\in E(G),\qquad su,tu\notin E(G).
\]
Equation (4) gives
\[
d_L(s),d_L(t)\le3,\qquad d_L(u)\le4.
\tag{8}
\]

There are two proper pair patterns:
\[
\{s,u\}\mid\{t\},
\qquad
\{t,u\}\mid\{s\}.
\tag{9}
\]

Consider an uncolorable component \(F\) for the first pattern, with \(s,u\) colored \(\alpha\) and \(t\) colored \(\beta\). Every list contains \(\gamma\), and \(\beta\) is missing only at neighbors of \(t\), of which there are at most three. Lemma 2 applies.

I claim that \(F\) must have an odd-cycle end block. Otherwise Lemma 2 says that \(F\) is an even-order path with endpoint lists \(\{\gamma\}\) and internal lists \(\{\beta,\gamma\}\).

Each endpoint is adjacent to \(t\) and to one of \(s,u\). It cannot be adjacent to \(s\), since \(st\) is an edge. Hence both endpoints are adjacent to \(t,u\).

Each internal vertex has exactly one neighbor in \(\{s,u\}\). Its label alternates along the internal path. The internal vertex next to either endpoint must be labeled \(s\), since the endpoint is adjacent to \(u\). But the internal path has an even number of vertices, so its alternating labels have different labels at its two ends—a contradiction. The two-vertex path is also impossible, since its endpoints would share neighbor \(t\).

Thus \(F\) has an odd-cycle end block. There cannot be two: each would contribute two neighbors of \(s\), contradicting \(d_L(s)\le3\). Since \(F\) has at least two end blocks, it also has an edge end block.

The odd-cycle end block contributes at least two neighbors of \(u\), and the edge end block contributes another. Therefore every component uncolorable under the first pattern uses at least three neighbors of \(u\). By symmetry, the same holds for the second pattern.

Since \(d_L(u)\le4\), at most one component can be uncolorable under either pattern. Such a component has an odd-cycle end block and hence becomes colorable when the pair pattern is switched. Choosing the other pattern colors every component.

A triangle-free graph on three vertices is independent, a single edge plus an isolated vertex, or a path. All cases are now covered, completing the proof of the theorem. ∎

---

## 4. Why eleven degree-six vertices suffice

**Lemma 3.** Every triangle-free graph on at most eleven vertices can be made bipartite by deleting at most three vertices.

**Proof.** Add isolated vertices if necessary, so that the graph \(J\) has exactly eleven vertices.

If \(\Delta(J)\le3\), Brooks’ theorem gives a 3-coloring. A smallest color class has at most three vertices; deleting it leaves a bipartite graph.

Otherwise choose a vertex \(v\) of degree \(d\ge4\). Its neighborhood \(N(v)\) is independent. Put
\[
R=V(J)\setminus(N(v)\cup\{v\}).
\]
We seek an independent set \(I\subseteq R\) such that
\[
|N(v)|+|\{v\}\cup I|\ge8.
\]
The two sets \(N(v)\) and \(\{v\}\cup I\) then induce a bipartite graph.

The required choices are:

\[
\begin{array}{c|c|c}
d & |R| & \text{required }|I|\\ \hline
4 & 6 & 3\\
5 & 5 & 2\\
6 & 4 & 1\\
\ge7 & \le3 & 0
\end{array}
\]

The only nontrivial entry is the first: every triangle-free graph on six vertices has an independent triple. If some vertex has at least three neighbors, those neighbors suffice. Otherwise any vertex has at least three nonneighbors; two of those are nonadjacent, and together with the original vertex form an independent triple.

Thus \(J\) always contains an induced bipartite subgraph on at least eight vertices. Deleting the other at most three vertices proves the lemma. ∎

Apply Lemma 3 to \(H_6(G)\), then apply the theorem with \(q=5\). This proves Corollary 2.

---

## 5. Scope and remaining gap

The new sufficient condition is
\[
\operatorname{oct}(H_6(G))\le3,
\]
improving the supplied attempt’s threshold of two. The elementary numerical consequence improves its nine-vertex threshold to eleven.

There is no argument here that an arbitrary degree-six core satisfies this condition. For example, four disjoint \(5\)-cycles have odd-cycle transversal number four. They can occur as the degree-six core of a triangle-free graph by attaching four leaves to each cycle vertex. That graph is easily 3-colorable, so failure of the criterion is not evidence of a counterexample.

Thus the unrestricted \(\Delta=6\) case, and the full conjecture, are left unresolved by this answer. No computational enumeration, external small-graph classification, or catalog order estimate is used in the proof.