```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open; I reduce its universal form to the path cases, give an FPT algorithm for 2P4-free graphs parameterized by anti-neighborhood components, and prove a mixed-list NP-completeness barrier to the obvious induction.",
  "would_publish": false,
  "caveats": "No unrestricted polynomial algorithm is obtained for P8-free or 2P4-free graphs; the NP-hardness result concerns an auxiliary mixed-list problem."
}
```

# Mathematical writeup

## 1. Statement and a reduction to connected forbidden paths

All subgraphs below are induced. Write
\[
H=P_{a_1}+\cdots+P_{a_r},
\qquad h=\sum_{i=1}^r a_i.
\]

### Proposition 1
The graph \(H\) is an induced subgraph of
\[
P_M,\qquad M=h+r-1.
\]
Consequently, every \(H\)-free graph is \(P_M\)-free.

#### Proof
In \(P_M\), select \(a_1\) consecutive vertices, omit one vertex, select the next \(a_2\) consecutive vertices, and so on. The selected vertices induce \(H\).

Thus, if \(G\) contained an induced \(P_M\), it would also contain an induced \(H\). Hence \(H\)-free implies \(P_M\)-free. ∎

The value \(M=h+r-1\) is the smallest path order that works in general: distinct components of an induced subgraph of a path must be separated by at least one unselected vertex.

### Consequence
The universal conjecture for all linear forests is equivalent to the apparently narrower assertion

> for every fixed \(t\), 3-Coloring is polynomial-time solvable on \(P_t\)-free graphs.

Indeed, the latter assertion implies the conjecture by Proposition 1, while the converse follows by taking \(H=P_t\).

In particular, \(2P_4\) is an induced subgraph of \(P_9\), so every \(2P_4\)-free graph is \(P_9\)-free. This does not settle the currently open \(2P_4\) case because no \(P_9\)-free algorithm is known from the supplied literature status.

A further elementary consequence is that every connected \(H\)-free graph has diameter at most \(M-2\), since every shortest path is induced.

---

## 2. The seed-and-\(2\)-SAT observation

Let \(S\subseteq V(G)\) be precolored with colors \(\{1,2,3\}\). Starting from full lists \(\{1,2,3\}\), remove from each uncolored vertex the colors used by its neighbors in \(S\). Every vertex in \(N(S)\setminus S\) then has a list of size at most two. Only
\[
A(S):=V(G)\setminus N[S]
\]
can retain all three colors.

We use the following standard algorithmic lemma.

### Lemma 2
If a graph \(G\) has a dominating set \(D\) of size \(d\), then 3-Coloring can be decided in time
\[
3^d\,|V(G)|^{O(1)}.
\]

#### Proof
Enumerate all maps \(D\to\{1,2,3\}\), discarding those that are not proper on \(G[D]\). After fixing one such map, every vertex outside \(D\) loses at least one color because it has a neighbor in \(D\). Thus every remaining list has size at most two.

List-coloring with lists of size at most two reduces to \(2\)-SAT. For each vertex with list \(\{a,b\}\), introduce a Boolean choice. For every edge \(uv\) and every common color \(c\in L(u)\cap L(v)\), insert the clause
\[
\neg[u=c]\ \lor\ \neg[v=c].
\]
Singleton and empty lists are treated as unit clauses and immediate rejection, respectively. The resulting formula is satisfiable exactly when the precoloring of \(D\) extends. ∎

---

## 3. An FPT result for the \(2P_4\)-free bottleneck

We first need an elementary fact about \(P_4\)-free graphs.

### Lemma 3
Every connected \(P_4\)-free graph with at least two vertices has a dominating edge.

#### Proof
We first show that the complement of a connected \(P_4\)-free graph \(F\) on at least two vertices is disconnected.

This follows by induction on \(|V(F)|\). Choose a vertex \(v\) that is a leaf of some spanning tree, so \(F-v\) is connected. By induction, \(\overline{F-v}\) is disconnected; let its connected components be \(A_1,\dots,A_k\), with \(k\geq2\). Thus \(F\) is complete between distinct \(A_i\).

Suppose for a contradiction that \(\overline F\) is connected. Then \(v\) has a nonneighbor in every \(A_i\), since otherwise an \(A_i\) would be a component of \(\overline F\). Since \(F\) is connected, \(v\) has a neighbor in some \(A_i\). Along a path in \(\overline{F[A_i]}\) from such a neighbor to a nonneighbor, choose consecutive vertices \(p,q\) such that \(vp\in E(F)\), \(vq\notin E(F)\), and \(pq\notin E(F)\). Choose \(z\in A_j\), \(j\ne i\), nonadjacent to \(v\). Since distinct \(A_i\) are complete to one another in \(F\),
\[
v-p-z-q
\]
is an induced \(P_4\), a contradiction.

Hence \(\overline F\) is disconnected. Choose \(x,y\) in distinct components of \(\overline F\). They are adjacent in \(F\), and every vertex of \(F\) is adjacent to at least one of \(x,y\). Thus \(xy\) is a dominating edge. ∎

Now let \(G\) be a connected \(2P_4\)-free graph containing an induced \(P_4\), say \(S\). Put
\[
A=G-N[S],
\qquad
c(S)=\operatorname{cc}(G[A]).
\]
Because \(G\) is \(2P_4\)-free, \(G[A]\) is \(P_4\)-free.

### Theorem 4
For every induced \(P_4\), \(S\), in a \(2P_4\)-free graph \(G\), 3-Coloring can be decided in time
\[
3^{\,4+2c(S)}\,|V(G)|^{O(1)}.
\]
Consequently, if
\[
\kappa(G)=\min\{c(S):S\text{ is an induced }P_4\},
\]
then 3-Coloring on \(2P_4\)-free graphs is fixed-parameter tractable parameterized by \(\kappa(G)\).

#### Proof
Let \(C_1,\dots,C_c\) be the components of \(G[A]\). For each \(C_i\), choose one vertex if \(|C_i|=1\), and otherwise choose a dominating edge supplied by Lemma 3. Let the resulting set be \(D_i\), so \(|D_i|\leq2\), and define
\[
D=S\cup D_1\cup\cdots\cup D_c.
\]

The set \(D\) dominates \(G\): vertices in \(N(S)\) are dominated by \(S\), while every vertex in \(A\) is dominated by the appropriate \(D_i\). Hence
\[
|D|\leq4+2c(S),
\]
and Lemma 2 applies.

The minimum \(\kappa(G)\) can be found by enumerating all induced \(P_4\)'s and computing the components of their anti-neighborhoods. If \(G\) is \(P_4\)-free, its connected components can instead be solved separately using Lemmas 2 and 3. ∎

Thus the \(2P_4\) case is polynomial whenever some induced \(P_4\) has only a bounded number of anti-neighborhood components.

### Why this does not settle \(2P_4\)

The parameter \(\kappa\) is unbounded even on bipartite \(2P_4\)-free graphs. Let \(G_n\) be obtained from a core \(K_{n,n}\), with sides \(X,Y\), by attaching one private leaf to every core vertex.

Every induced \(P_4\) contains a core vertex from each side. Therefore two vertex-disjoint induced \(P_4\)'s have a cross-edge between their core vertices, so \(G_n\) is \(2P_4\)-free. On the other hand, for any induced \(P_4\), \(S\), every core vertex lies in \(N[S]\), while every private leaf whose parent is not in \(S\) lies as an isolated component of \(G_n-N[S]\). Since \(S\) contains at most three core vertices,
\[
c(S)\geq 2n-3.
\]
Hence \(\kappa(G_n)\) grows linearly.

---

## 4. Why the obvious induction on components fails

For \(2P_4\)-free \(G\), fixing a \(P_4\), \(S\), leaves:

- full three-element lists on the \(P_4\)-free anti-neighborhood \(A\);
- lists of size at most two on \(N(S)\setminus S\).

It is tempting to hope that the \(P_4\)-freeness of the full-list vertices suffices. The following shows that it does not.

### Theorem 5
The following restricted form of List-3-Coloring is NP-complete:

- the vertices with list \(\{1,2,3\}\) form an independent set \(U\);
- every other vertex has a list of size exactly two;
- \(G-U\) is a matching;
- every vertex of \(G-U\) has degree two in \(G\).

#### Proof
Membership in NP is immediate. Reduce from ordinary 3-Coloring.

Given a graph \(F\), create a terminal \(t_v\) with list \(\{1,2,3\}\) for every \(v\in V(F)\). The terminals are pairwise nonadjacent.

Orient each edge \(uv\) arbitrarily. For every two-element set
\[
Q\in \binom{\{1,2,3\}}2,
\]
introduce vertices \(x_{uv,Q},y_{uv,Q}\), both with list \(Q\), and edges
\[
t_u x_{uv,Q},\qquad x_{uv,Q}y_{uv,Q},\qquad y_{uv,Q}t_v.
\]
There are no other edges.

Fix colors \(\alpha,\beta\) on \(t_u,t_v\). For a particular \(Q\), the edge \(x_{uv,Q}y_{uv,Q}\) is uncolorable exactly when
\[
\alpha=\beta\in Q:
\]
in that case both internal vertices are forced to the same other color of \(Q\). In every other case the two internal vertices can receive different colors from their remaining lists.

Considering all three choices of \(Q\), all three gadgets extend exactly when \(\alpha\ne\beta\). Thus a coloring of the terminals extends if and only if it is a proper 3-coloring of \(F\).

The full-list vertices are independent, and deleting them leaves a disjoint union of the internal edges. Each internal vertex has one terminal neighbor and its matching partner, hence degree two. ∎

This proves that there is no generic polynomial algorithm based only on the fact that the full-list vertices induce a \(P_4\)-free graph, unless \(\mathrm P=\mathrm{NP}\). It does **not** prove NP-hardness for \(2P_4\)-free graphs: when the source graph has two vertex-disjoint edges, the construction visibly contains two anticomplete gadget \(P_4\)'s.

---

## 5. A complementary polynomial subcase with an unbounded anti-neighborhood

The full \(2P_4\)-free condition does restore tractability in the sparsest version of the mixed-list setting.

### Theorem 6
Let \((R,L)\) be a list-coloring instance with \(V(R)=A\cup B\) such that:

1. \(A\) is independent and \(L(a)=\{1,2,3\}\) for every \(a\in A\);
2. \(R[B]\) has maximum degree at most one;
3. \(|L(b)|\leq2\) for every \(b\in B\);
4. every \(b\in B\) has at most one neighbor in \(A\);
5. \(R\) is \(2P_4\)-free.

Then \(L\)-colorability is decidable in polynomial time.

#### Proof
Each component of \(R[B]\) has one or two vertices and touches at most two vertices of \(A\). By trying constantly many colorings, eliminate each such component and record the resulting unary or binary relation on its neighbors in \(A\).

Let \(F\) be the graph on \(A\) in which \(uv\) is an edge if some two-vertex component \(xy\) of \(R[B]\) has \(x\) adjacent to \(u\) and \(y\) adjacent to \(v\), where \(u\ne v\). Then
\[
u-x-y-v
\]
is an induced \(P_4\).

If \(F\) had two vertex-disjoint edges, the corresponding two \(P_4\)'s would be anticomplete: \(A\) is independent, distinct components of \(R[B]\) are anticomplete, and every \(B\)-vertex has at most one \(A\)-neighbor. Therefore
\[
\nu(F)\leq1.
\]

Every graph with matching number at most one is either a star together with isolated vertices, or a triangle together with isolated vertices. In the star case, enumerate the three possible colors of the center; all leaf choices are then independent. In the triangle case, enumerate the at most \(3^3\) colorings of its three vertices. Unary constraints and the previously computed binary relations can be checked directly. Once the colors of \(A\) are fixed, the components of \(R[B]\) extend independently. ∎

Consequently, a \(2P_4\)-free graph is polynomial-time 3-colorable if it has an induced \(P_4\), \(S\), for which, writing
\[
A=G-N[S],\qquad B=N(S)\setminus S,
\]
the set \(A\) is independent, \(G[B]\) has maximum degree at most one, and every \(b\in B\) has at most one neighbor in \(A\). One enumerates the constantly many colorings of \(S\) and applies Theorem 6.

---

## 6. A general high-girth special case

Proposition 1 also gives a uniform sparse regime.

### Proposition 7
Let \(H\) be a fixed linear forest and \(M=|V(H)|+\operatorname{cc}(H)-1\). List-3-Coloring is polynomial-time solvable on \(H\)-free graphs of girth at least \(M+1\).

#### Proof
An \(H\)-free graph is \(P_M\)-free. In a graph of girth at least \(M+1\), every simple path on \(M\) vertices is induced: any chord would create a cycle of length at most \(M\). Thus such a graph contains no simple path on \(M\) vertices.

Run depth-first search. Every root-to-leaf path has at most \(M-1\) vertices. Moreover, every edge of an undirected DFS joins an ancestor to a descendant. Taking for each vertex the bag consisting of that vertex and all its DFS ancestors gives a tree decomposition of width at most \(M-2\). Standard dynamic programming over this decomposition solves List-3-Coloring in
\[
O(3^{M-1}|V(G)|)
\]
time for fixed \(H\). ∎

---

## 7. Remaining gap

None of the arguments covers unrestricted \(P_8\)-free graphs or unrestricted \(2P_4\)-free graphs.

The central obstruction is now explicit. Coloring a bounded seed converts its neighborhood to a \(2\)-list instance, but leaves a three-list anti-neighborhood. Even when that anti-neighborhood is independent and the two-list part is a matching, the resulting mixed problem is NP-complete unless one exploits additional global consequences of \(H\)-freeness. Theorem 6 handles one particularly sparse situation where \(2P_4\)-freeness forces the constraint graph to have matching number at most one, but arbitrary boundary graphs remain untreated.

Thus this is a partial structural and algorithmic attack, not a proof or counterexample to the conjecture.