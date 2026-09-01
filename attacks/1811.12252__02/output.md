```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I do not settle the five classes, but prove bounded clique-width for natural low-independence and split subcases and obtain strong shortest-odd-cycle reductions for the two triangle-free cases.",
  "would_publish": false,
  "caveats": "The high-independence cores, short-odd-cycle cases, and unbounded-width cyclic interfaces remain unresolved; no priority claim is made."
}
```

# 1. Statement and interpretation

The extracted catalog statement omits the actual five pairs. Up to interchanging \(H_1,H_2\) and simultaneously complementing both forbidden graphs, the five cases in the source are

\[
\begin{array}{ll}
\text{(T1)} &(K_3,\;P_1+S_{1,1,3}),\\
\text{(T2)} &(K_3,\;S_{1,2,3}),\\
\text{(D1)} &(\mathrm{diamond},\;P_1+P_2+P_3),\\
\text{(D2)} &(\mathrm{diamond},\;P_1+P_5),\\
\text{(G)}  &(\mathrm{gem},\;P_2+P_3).
\end{array}
\]

Here \(S_{a,b,c}\) is the tree with one degree-three vertex and three arms of lengths \(a,b,c\).

I prove the following partial results.

### Partial results

1. Every diamond-free graph with independence number at most \(3\) has bounded clique-width. More generally, diamond-free graphs whose vertices can be covered by at most three cliques have bounded clique-width.

   Consequently, any unbounded-width sequence in either (D1) or (D2) must eventually have independence number at least \(4\).

2. Every gem-free graph with independence number at most \(2\) has bounded clique-width; a crude explicit bound obtained below is \(127\).

   Consequently, an unbounded-width sequence for (G) must eventually have independence number at least \(3\).

3. Every gem-free split graph has clique-width at most \(3\). Hence the split-graph portions of (D1), (D2), and (G) all have bounded clique-width. The triangle-free split portions of (T1) and (T2) also have bounded clique-width.

4. In the two triangle-free cases, a shortest odd cycle strongly controls the entire graph:
   - for (T2), if a connected graph has shortest odd cycle \(C\) of length at least \(7\), then every vertex outside \(C\) has exactly two neighbors on \(C\), at cyclic distance two;
   - if moreover \(|C|\ge 11\), vertices can be partitioned into cyclic bags \(B_i\), with edges only between consecutive bags;
   - for (T1), the same two-neighbor conclusion holds when \(|C|\ge 9\).

These statements do not settle any of the five full cases.

---

# 2. Clique-width closure facts

I use rank-width only to justify standard closure operations. For every graph \(G\),

\[
\operatorname{rw}(G)\leq \operatorname{cw}(G)
   \leq 2^{\operatorname{rw}(G)+1}-1.
\]

For a cut \(X\mid V(G)\setminus X\), complementing all edges inside a fixed set changes the corresponding binary cut matrix by a matrix of rank at most \(1\). Complementing all edges between two fixed disjoint sets changes it by rank at most \(2\). Thus:

- graph complementation preserves bounded clique-width;
- any fixed number of subgraph or bipartite complementations preserves bounded clique-width;
- adding or deleting a bounded number of vertices preserves bounded clique-width.

These facts will be used without further comment.

---

# 3. Diamond-free graphs of small independence number

## 3.1 Three clique parts

### Lemma 3.1
Let \(A,B\) be cliques in a diamond-free graph. After deleting at most two vertices from \(A\cup B\), the edge set between the remaining portions of \(A\) and \(B\) is either complete, empty, or a matching.

#### Proof
For \(a\in A\), suppose that \(a\) has two neighbors \(b_1,b_2\in B\) and a non-neighbor \(b_0\in B\). Since \(B\) is a clique,

\[
G[\{a,b_0,b_1,b_2\}]
\]

is a diamond, a contradiction. Hence

\[
|N(a)\cap B|\in\{0,1,|B|\}.
\]

The analogous statement holds with \(A,B\) interchanged.

Assume first that there are at least two vertices of \(A\) complete to \(B\). Every vertex of \(B\) then has at least two neighbors in \(A\), and hence must be complete to \(A\). Thus the relation is complete.

Suppose there is exactly one vertex \(a^\ast\in A\) complete to \(B\). Every \(b\in B\) is then either complete to \(A\) or has \(a^\ast\) as its unique neighbor in \(A\). There can be at most one vertex of \(B\) complete to \(A\), since two such vertices would force all rows to be complete. Deleting \(a^\ast\) and this possible exceptional vertex of \(B\) leaves no cross-edges.

The symmetric case is identical. If neither side has a vertex complete to the other, all cross-degrees are at most one, so the cross-edges form a matching. ∎

### Proposition 3.2
Every diamond-free graph whose vertex set is the union of at most three cliques has bounded clique-width.

#### Proof
Let the clique partition be \(C_1,C_2,C_3\). Apply Lemma 3.1 to each of the three pairs. Delete the union \(Z\) of the exceptional sets; \(|Z|\leq 6\).

In \(G-Z\), each pair \(C_i,C_j\) is joined either completely, not at all, or by a matching. Now:

1. complement the edges inside each \(C_i\), making the three parts independent;
2. bipartite-complement each pair that was completely joined.

The resulting graph has at most one edge from each vertex to either of the other two parts, and hence has maximum degree at most \(2\). It is therefore a disjoint union of paths and cycles, whose clique-width is at most \(4\).

Only a fixed number of complementations was used, and at most six vertices were deleted. Hence the original class has bounded clique-width. ∎

## 3.2 Independence number at most three

### Theorem 3.3
The class of diamond-free graphs \(G\) with \(\alpha(G)\leq 3\) has bounded clique-width.

#### Proof
Let \(C\) be a maximum clique.

If \(|C|\leq 3\), then both \(\omega(G)\) and \(\alpha(G)\) are at most \(3\), so Ramsey's theorem bounds \(|V(G)|\) by an absolute constant.

Assume \(|C|\geq 4\). Every vertex \(x\notin C\) has at most one neighbor in \(C\). Indeed, if \(x\) has two neighbors in \(C\), maximality of \(C\) gives a non-neighbor \(c\in C\), and \(x\), two of its neighbors in \(C\), and \(c\) induce a diamond.

Put \(R=V(G)\setminus C\). We claim that \(\alpha(G[R])\leq 2\). Otherwise, let \(x,y,z\in R\) be independent. Together they have at most three neighbors in \(C\). Since \(|C|\geq4\), some \(c\in C\) is adjacent to none of \(x,y,z\), giving an independent set \(\{c,x,y,z\}\), a contradiction.

If \(\omega(G[R])\leq2\), then Ramsey's theorem bounds \(|R|\), so \(G\) is a clique plus a bounded number of vertices and has bounded clique-width.

Otherwise choose a maximum clique \(A\) in \(G[R]\), with \(|A|\geq3\). As above, every vertex of \(R\setminus A\) has at most one neighbor in \(A\). If two vertices \(x,y\in R\setminus A\) were nonadjacent, some \(a\in A\) would be adjacent to neither, producing an independent set \(\{a,x,y\}\) in \(R\). Hence \(R\setminus A\) is a clique.

Thus \(V(G)\) is the union of the three cliques

\[
C,\qquad A,\qquad R\setminus A.
\]

Proposition 3.2 applies. ∎

Since

\[
\alpha(P_1+P_5)=\alpha(P_1+P_2+P_3)=4,
\]

this treats the natural low-independence part of both diamond cases.

---

# 4. Gem-free graphs of independence number two

The complement of the gem is \(P_1+P_4\), because \(P_4\) is self-complementary. We first classify the triangle-free \((P_1+P_4)\)-free graphs sufficiently for clique-width.

## 4.1 The bipartite case

For a bipartite graph with fixed bipartition \(X,Y\), its bipartite complement toggles all \(X\)-\(Y\) edges.

### Lemma 4.1
If a bipartite graph \(H\) is connected and \((P_1+P_4)\)-free, then its bipartite complement is disconnected.

#### Proof
Suppose both \(H\) and its bipartite complement \(\widetilde H\) are connected. Choose an edge \(xy\in E(H)\), with \(x\in X\), \(y\in Y\), and let

\[
x=p_0,p_1,\ldots,p_k=y
\]

be a shortest \(x\)-\(y\) path in \(\widetilde H\). Since \(xy\notin E(\widetilde H)\), \(k\geq3\) and \(k\) is odd.

If \(k\geq5\), then in \(H\)

\[
p_3-p_0-p_5-p_2
\]

is an induced \(P_4\): the three displayed edges are non-consecutive odd-distance pairs on the shortest path in \(\widetilde H\), while all nonedges follow either from the bipartition or from consecutive edges of \(\widetilde H\). The vertex \(p_1\) is anticomplete to this \(P_4\), giving a forbidden \(P_1+P_4\).

Thus \(k=3\); write the path as \(x-a-b-y\). In \(H\), \(a\) and \(b\) are nonadjacent. Let a shortest \(a\)-\(b\) path in \(H\) be chosen. If it has length at least \(5\), its first four vertices and its sixth vertex induce \(P_1+P_4\). Hence it has length three, say

\[
a-c-d-b.
\]

The vertex \(x\) is nonadjacent to \(a,c,b\), so it must be adjacent to \(d\), or it would be isolated from this induced \(P_4\). Similarly, \(y\) must be adjacent to \(c\).

But then

\[
x-y-c-a
\]

is an induced \(P_4\), and \(b\) is anticomplete to it, another contradiction. ∎

### Corollary 4.2
Bipartite \((P_1+P_4)\)-free graphs have clique-width at most \(4\).

#### Proof
If such a graph is disconnected and one component contains a \(P_4\), a vertex in another component is isolated from that \(P_4\). Hence a disconnected member is \(P_4\)-free and therefore is a disjoint union of complete bipartite graphs.

If it is connected, Lemma 4.1 says its bipartite complement has at least two components. Between different bipartite-complement components, all possible opposite-side edges are present. Recursing on the induced subgraphs gives a decomposition using:

- disjoint union; and
- bipartite join between blocks.

Four labels suffice. Maintain labels \(1,2\) for the two sides of the accumulated graph and labels \(3,4\) for the two sides of a new block; join \(1\) to \(4\) and \(2\) to \(3\), and then merge \(3\) into \(1\) and \(4\) into \(2\). ∎

## 4.2 The nonbipartite case

### Lemma 4.3
Every connected, nonbipartite, triangle-free, \((P_1+P_4)\)-free graph is a complete blow-up of \(C_5\) by independent sets.

#### Proof
Let \(C\) be a shortest odd cycle. It is induced. Since the graph is triangle-free, \(|C|\geq5\). If \(|C|\geq7\), four consecutive vertices of \(C\), together with a cycle vertex at distance at least two from all four, induce \(P_1+P_4\). Hence \(C\) is a \(5\)-cycle, say

\[
v_0v_1v_2v_3v_4v_0.
\]

Let \(x\notin V(C)\). It cannot have zero neighbors on \(C\). Nor can it have exactly one neighbor \(v_i\), since \(C-v_i\) is an induced \(P_4\) anticomplete to \(x\). Triangle-freeness implies that \(N_C(x)\) is independent, and an independent set in \(C_5\) has size at most two. Therefore

\[
N_C(x)=\{v_{i-1},v_{i+1}\}
\]

for a unique \(i\).

Let \(B_i\) consist of \(v_i\) and all outside vertices of this type. Each \(B_i\) is independent, and \(B_i\) is anticomplete to \(B_{i+2}\), since vertices in these bags have a common neighbor on \(C\).

It remains to prove that \(B_i\) is complete to \(B_{i+1}\). Take \(x\in B_i\) and suppose that \(y\in B_{i+1}\) is nonadjacent to \(x\). Then

\[
v_{i-2}-v_{i-1}-x-v_{i+1}
\]

is an induced \(P_4\). The vertex \(y\) is anticomplete to all four vertices, a contradiction.

Thus precisely the consecutive bag pairs are complete, which is a complete independent-set blow-up of \(C_5\). ∎

### Theorem 4.4
Triangle-free \((P_1+P_4)\)-free graphs have clique-width at most \(5\).

#### Proof
If disconnected, they are \(P_4\)-free, as above. Connected bipartite members have clique-width at most \(4\) by Corollary 4.2. Connected nonbipartite members are five-bag blow-ups of \(C_5\) by Lemma 4.3 and can be constructed with one label per bag. ∎

### Corollary 4.5
Gem-free graphs with independence number at most \(2\) have bounded clique-width.

#### Proof
Let \(G\) be gem-free with \(\alpha(G)\leq2\). Then \(\overline G\) is \((P_1+P_4)\)-free and triangle-free. By Theorem 4.4,

\[
\operatorname{cw}(\overline G)\leq5.
\]

Using rank-width invariance up to one under complementation gives, for example,

\[
\operatorname{cw}(G)\leq 2^{7}-1=127.
\]

The precise constant is immaterial. ∎

Since \(\alpha(P_2+P_3)=3\), this handles the low-independence part of (G).

---

# 5. Split graphs

### Proposition 5.1
Every gem-free split graph has clique-width at most \(3\).

#### Proof
Fix a split partition \(V(G)=C\cup I\), where \(C\) is a clique and \(I\) is independent.

For \(x,y\in I\), put \(A=N_C(x)\) and \(B=N_C(y)\). If \(A\cap B\neq\varnothing\), \(A\setminus B\neq\varnothing\), and \(B\setminus A\neq\varnothing\), choose

\[
z\in A\cap B,\quad p\in A\setminus B,\quad q\in B\setminus A.
\]

Then \(x-p-q-y\) is an induced \(P_4\), and \(z\) is universal to it, giving a gem. Conversely, every gem in a split graph has this form. Hence the family

\[
\mathcal F=\{N_C(x):x\in I\}
\]

is laminar: any two members are disjoint or one contains the other.

Represent the distinct nonempty sets in \(\mathcal F\) as a laminar inclusion forest, with an artificial root \(C\). Build it bottom-up. At a node \(S\):

1. combine its child expressions and residual clique vertices;
2. join all clique vertices belonging to different children, so that the vertices of \(S\) form a clique;
3. create all independent vertices whose neighborhood is exactly \(S\), join them to the clique label for \(S\), and then move them to the permanent independent-set label.

One label is used for constructed clique vertices, one for all independent vertices, and one temporary label for the next child or newly created neighborhood class. Thus three labels suffice. Vertices with empty neighborhood are added as isolated vertices. ∎

A gem contains an induced diamond, so every diamond-free graph is gem-free. Moreover, each of

\[
P_1+P_5,\qquad P_1+P_2+P_3,\qquad P_2+P_3
\]

contains an induced \(2P_2\), whereas split graphs are \(2P_2\)-free. Therefore Proposition 5.1 covers all split members of (D1), (D2), and (G).

For (T1) and (T2), a triangle-free split graph has a split clique of size at most two. Its independent vertices have at most four possible neighborhoods in that clique, so it has bounded neighborhood diversity and hence bounded clique-width.

---

# 6. Shortest odd cycles in the two triangle cases

We now turn to the two cases with \(K_3\) forbidden.

## 6.1 A general attachment observation

Let \(C=v_0v_1\cdots v_{\ell-1}v_0\) be a shortest odd cycle in a triangle-free graph. If \(x\notin C\) has two neighbors on \(C\), consider the two arcs between them, of lengths \(d\) and \(\ell-d\). Triangle-freeness gives both lengths at least two. The two cycles through \(x\) have lengths \(d+2\) and \(\ell-d+2\), exactly one of which is odd. Minimality of \(\ell\) forces one of the two arcs to have length exactly two.

If \(\ell\geq7\), this also implies that \(x\) has at most two neighbors on \(C\): three cycle vertices cannot be pairwise separated by a two-edge arc. Thus a vertex with at least two neighbors on \(C\) has exactly

\[
N_C(x)=\{v_{i-1},v_{i+1}\}
\]

for some \(i\).

## 6.2 The \(S_{1,2,3}\)-free case

### Proposition 6.1
Let \(G\) be connected, triangle-free, and \(S_{1,2,3}\)-free. If \(C\) is a shortest odd cycle of length at least \(7\), then every vertex outside \(C\) is adjacent to \(C\), and its neighborhood on \(C\) is \(\{v_{i-1},v_{i+1}\}\) for some \(i\).

#### Proof
Suppose first that \(x\) has exactly one neighbor \(v_0\) on \(C\). The center \(v_0\), together with the three arms

\[
v_0x,\qquad v_0v_1v_2,\qquad
v_0v_{-1}v_{-2}v_{-3},
\]

induces an \(S_{1,2,3}\), a contradiction.

Thus every vertex adjacent to \(C\) has the stated two-neighbor form.

If some vertex has distance at least two from \(C\), take adjacent vertices \(x,y\) on a shortest path to \(C\), where \(y\) has distance one and \(x\) distance two. Write

\[
N_C(y)=\{v_{-1},v_1\}.
\]

Then \(y\), with arms

\[
yx,\qquad yv_{-1}v_{-2},\qquad
yv_1v_2v_3,
\]

induces an \(S_{1,2,3}\). Hence no such \(x\) exists. ∎

Define

\[
B_i=\{v_i\}\cup
\{x\notin C:N_C(x)=\{v_{i-1},v_{i+1}\}\}.
\]

Every \(B_i\) is independent, and \(B_i\) is anticomplete to \(B_{i+2}\).

### Proposition 6.2
Under the hypotheses of Proposition 6.1, if \(|C|\geq11\), then edges occur only between consecutive bags \(B_i,B_{i+1}\).

#### Proof
Suppose \(x\in B_0\), \(y\in B_j\), and \(xy\in E(G)\).

The following two potential induced copies of \(S_{1,2,3}\), centered at \(x\), must each have an extra edge from \(y\) into one of the cycle arms:

\[
\begin{array}{lll}
xy, & xv_{-1}v_{-2}, & xv_1v_2v_3,\\
xy, & xv_1v_2,       & xv_{-1}v_{-2}v_{-3}.
\end{array}
\]

Since \(N_C(y)=\{v_{j-1},v_{j+1}\}\), this forces

\[
j\in\{-3,-2,-1,0,1,2,3\}
\]

modulo \(|C|\). Triangle-freeness excludes \(j=0,\pm2\).

If \(j=3\), then \(x\) is the center of an induced \(S_{1,2,3}\) with arms

\[
xv_1,\qquad xv_{-1}v_{-2},\qquad xyv_4v_5.
\]

For \(|C|\geq11\), there are no wrap-around edges between these arms. This is a contradiction. The case \(j=-3\) is symmetric. Thus \(j=\pm1\). ∎

### Corollary 6.3
For every fixed \(b\), the graphs in Proposition 6.2 satisfying \(|B_i|\leq b\) for all \(i\) have bounded clique-width.

#### Proof
They have a path decomposition with bags

\[
B_0\cup B_i\cup B_{i+1},
\qquad 1\leq i\leq |C|-2.
\]

Its width is at most \(3b-1\). Bounded treewidth implies bounded clique-width. ∎

The unresolved issue is that the forbidden-subgraph condition has not been shown to bound the sizes of the \(B_i\) or to give compatible bounded-width descriptions of the bipartite graphs between consecutive bags.

## 6.3 The \(P_1+S_{1,1,3}\)-free case

### Proposition 6.4
Let \(G\) be connected, triangle-free, and \((P_1+S_{1,1,3})\)-free. If \(C\) is a shortest odd cycle of length at least \(9\), every vertex outside \(C\) is adjacent to \(C\), and its neighborhood on \(C\) is \(\{v_{i-1},v_{i+1}\}\) for some \(i\).

#### Proof
Suppose \(x\) has the unique neighbor \(v_0\) on \(C\). The vertices with center \(v_0\) and arms

\[
v_0x,\qquad v_0v_1,\qquad
v_0v_{-1}v_{-2}v_{-3}
\]

induce \(S_{1,1,3}\). The vertex \(v_3\) is anticomplete to this copy when \(|C|\geq9\), yielding \(P_1+S_{1,1,3}\), a contradiction.

Thus every distance-one vertex has the two-neighbor form.

Now let \(y\) have distance one from \(C\), with

\[
N_C(y)=\{v_{-1},v_1\},
\]

and suppose \(x\) is its neighbor at distance two. The center \(y\), with arms

\[
yx,\qquad yv_{-1},\qquad yv_1v_2v_3,
\]

induces an \(S_{1,1,3}\). The cycle vertex \(v_5\) is isolated from this copy for \(|C|\geq9\), again a contradiction. ∎

This gives the same cyclic neighborhood partition as in Proposition 6.1, but I have not obtained an analogue of Proposition 6.2 strong enough to control clique-width.

---

# 7. Remaining gaps

The full five-case classification remains open in this analysis.

- For (D1) and (D2), Theorem 3.3 only removes the region \(\alpha\leq3\); the forbidden linear forests do not themselves bound independence number.
- For (G), Corollary 4.5 removes \(\alpha\leq2\), and Proposition 5.1 handles split graphs, but graphs with \(\alpha\geq3\) and no useful split decomposition remain.
- For (T1), shortest odd cycles of length at least \(9\) dominate the graph in a rigid two-neighbor fashion, but edges between the resulting bags are not yet controlled.
- For (T2), long shortest odd cycles give a genuine cyclic strip with edges only between consecutive bags. However, unbounded bag sizes and potentially incompatible bipartite interfaces prevent a clique-width bound. Shortest odd cycles of lengths \(5,7,9\) also remain untreated by the localization argument.

No explicit unbounded clique-width construction satisfying any of the five pairs is produced here, and no full boundedness proof is claimed.