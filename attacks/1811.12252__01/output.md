```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full question remains open, but it is equivalent to the rank-width formulation and is FPT on a broad subclass defined by biclique-free prime modular quotients.",
  "would_publish": false,
  "caveats": "The additional biclique parameter is unbounded already on prime clique-width-3 half-graphs, and no novelty claim is made."
}
```

# Mathematical writeup

## 1. Statement and status

For two input graphs \(G,H\), put
\[
k=\max\{\operatorname{cw}(G),\operatorname{cw}(H)\},
\qquad N=|V(G)|+|V(H)|.
\]
The open question asks whether Graph Isomorphism can be decided in time
\[
f(k)N^{O(1)}.
\]

I do not resolve this question. I prove the following partial results.

1. FPT parameterization by clique-width is equivalent to FPT parameterization by rank-width.
2. On \(K_{t,t}\)-subgraph-free graphs, GI is FPT parameterized by clique-width and \(t\). In particular, it is FPT parameterized by clique-width plus degeneracy or maximum degree.
3. This extends through modular decomposition: GI is FPT if, after a canonical choice of complementation, all prime modular quotients have bounded biclique number.
4. The extra hypothesis is genuinely additional: prime half-graphs have clique-width at most \(3\), but unbounded biclique number and treewidth.

## 2. Equivalence with rank-width

The standard inequalities are
\[
\operatorname{rw}(G)\leq \operatorname{cw}(G)
   \leq 2^{\operatorname{rw}(G)+1}-1.
\]

Consequently, the two FPT questions are equivalent.

- An algorithm running in \(f(\operatorname{rw}(G))N^{O(1)}\) is immediately FPT in clique-width because \(\operatorname{rw}(G)\leq \operatorname{cw}(G)\).
- Conversely, if GI has running time \(g(\operatorname{cw}(G))N^{O(1)}\), then on rank-width \(r\) it runs in
  \[
  \max_{s\le 2^{r+1}-1}g(s)\,N^{O(1)},
  \]
  which is FPT in \(r\).

Thus it is enough, and equally difficult, to seek an FPT algorithm parameterized by rank-width.

## 3. A structural lemma for biclique-free graphs

### Lemma 3.1

Let \(F\) have clique-width at most \(q\), and suppose \(F\) contains no \(K_{t,t}\) as a—not necessarily induced—subgraph, where \(t\geq2\). Then
\[
\operatorname{tw}(F)\leq 3q(t-1)-1.
\]

### Proof

Fix a \(q\)-expression for \(F\). Contracting unary operation nodes in its parse tree gives a subcubic tree whose leaves are the vertices of \(F\). Every edge of this tree gives a cut \(X,V(F)\setminus X\), where \(X\) is the vertex set of a subexpression.

At the point when that subexpression is completed, partition \(X\) into its at most \(q\) label classes \(C_1,\dots,C_s\). Vertices in a common class \(C_i\) receive identical treatment above the subexpression, and hence have identical final neighborhoods outside \(X\). Write
\[
D_i=N_F(C_i)\setminus X.
\]
All edges between \(C_i\) and \(D_i\) are present. Since \(F\) is \(K_{t,t}\)-free,
\[
\min\{|C_i|,|D_i|\}\leq t-1.
\]
For each \(i\), choose the smaller of \(C_i,D_i\). The union of the chosen sets is a vertex cover of all edges crossing the cut and has size at most
\[
q(t-1).
\]

We use the following standard conversion. If a subcubic vertex-branch decomposition has, for every cut, a vertex cover of its crossing edges of size at most \(b\), then
\[
\operatorname{tw}(F)+1\leq 3b.
\]
For completeness, this follows from bramble duality. If there were a bramble of order exceeding \(3b\), orient each decomposition-tree edge toward the unique side containing every bramble member disjoint from the corresponding crossing cover. Uniqueness follows because two such members on opposite sides would neither meet nor have an edge between them. At a sink of the oriented tree, the union of the at most three incident covers has size at most \(3b\). A bramble member avoiding this union must lie entirely in one incident branch, contradicting the orientation of that edge. A leaf sink is handled by additionally including its corresponding vertex.

Taking \(b=q(t-1)\) proves the claimed bound. ∎

### Corollary 3.2

Graph Isomorphism on \(K_{t,t}\)-free graphs is FPT parameterized by clique-width plus \(t\). More precisely, if both input graphs have clique-width at most \(k\), then their treewidth is at most
\[
3k(t-1)-1,
\]
so the treewidth-parameterized GI algorithm quoted in the question applies.

No clique-width expression needs to be supplied. One may use an adaptive FPT treewidth-recognition/decomposition algorithm and then invoke bounded-treewidth GI.

### Corollary 3.3

GI is FPT parameterized by clique-width plus degeneracy.

Indeed, a graph of degeneracy \(d\) cannot contain \(K_{d+1,d+1}\), since the latter has degeneracy \(d+1\). Therefore
\[
\operatorname{tw}(G)\leq 3\,\operatorname{cw}(G)\,d-1
\]
for \(d\geq1\). The same conclusion holds with maximum degree in place of degeneracy.

## 4. A modular-decomposition extension

The preceding result fails on dense graphs such as complete graphs, even though their isomorphism problem is trivial. Modular decomposition allows one to remove this artificial obstruction.

### Definitions

A set \(M\subseteq V(G)\) is a module if every vertex outside \(M\) is adjacent either to all of \(M\) or to none of \(M\). The canonical strong modular decomposition has three kinds of internal nodes:

- parallel nodes, whose quotient is edgeless;
- series nodes, whose quotient is complete;
- prime nodes, whose quotient has no nontrivial modules.

For a modular-decomposition node \(X\), let \(X_1,\dots,X_r\) be its maximal proper strong submodules, and let \(R_X\) be the quotient graph on \(\{1,\dots,r\}\).

Choosing one representative from each \(X_i\) realizes \(R_X\) as an induced subgraph of \(G\). Hence
\[
\operatorname{cw}(R_X)\leq \operatorname{cw}(G).
\]

For a graph \(R\), define its biclique number
\[
\beta(R)=\max\{s:K_{s,s}\text{ is a subgraph of }R\},
\]
with \(\beta(R)=0\) if \(R\) has no edge.

For a graph \(R\) on \(r\) vertices, define a canonical sparse orientation
\[
R^\circ=
\begin{cases}
R, & 2|E(R)|\leq \binom r2,\\
\overline R, & 2|E(R)|>\binom r2.
\end{cases}
\]
This choice is invariant under isomorphism.

Finally, let
\[
\mu(G)=\max\{\beta(R_X^\circ):X\text{ is a prime node of the modular decomposition of }G\},
\]
where the maximum over an empty set is \(0\).

### Theorem 4.1

Graph Isomorphism is FPT parameterized by
\[
\max\{\operatorname{cw}(G),\operatorname{cw}(H)\}
+
\max\{\mu(G),\mu(H)\}.
\]

### Proof

Let
\[
k=\max\{\operatorname{cw}(G),\operatorname{cw}(H)\},
\qquad
b=\max\{\mu(G),\mu(H)\}.
\]

First bound the treewidth of every oriented prime quotient. If \(R_X^\circ=R_X\), then its clique-width is at most \(k\). If \(R_X^\circ=\overline{R_X}\), use rank-width. Across every cut, complementing changes the binary adjacency matrix by the all-ones matrix, so
\[
\operatorname{rw}(\overline{R_X})
 \leq \operatorname{rw}(R_X)+1.
\]
Consequently,
\[
\operatorname{cw}(\overline{R_X})
 \leq 2^{\operatorname{rw}(\overline{R_X})+1}-1
 \leq 2^{k+2}-1.
\]
Thus, with
\[
h(k)=2^{k+2}-1,
\]
every \(R_X^\circ\) has clique-width at most \(h(k)\).

Moreover, \(R_X^\circ\) excludes \(K_{b+1,b+1}\). Lemma 3.1 therefore gives, for \(b\geq1\),
\[
\operatorname{tw}(R_X^\circ)\leq 3h(k)b-1.
\]

It remains to explain how quotient isomorphism tests combine.

Compute the canonical modular decompositions of \(G\) and \(H\). Process all pairs of decomposition nodes bottom-up. For a pair \(X,Y\):

- At leaves, the answer is immediate.
- At parallel or series nodes, \(G[X]\cong H[Y]\) precisely when the multisets of isomorphism types of their children agree.
- At prime nodes, color each quotient vertex by the already-computed isomorphism type of the corresponding child module. If the quotient orders or edge counts differ, return no. Otherwise both quotients make the same choice between the graph and its complement. Test color-preserving isomorphism between \(R_X^\circ\) and \(R_Y^\circ\) using bounded-treewidth GI.

The use of colors does not alter treewidth; the usual treewidth GI dynamic program permits arbitrary initial vertex colors. Alternatively, colors can be regarded as unary relations.

Correctness follows inductively from the canonical nature of strong modules. Every isomorphism maps maximal proper strong modules to maximal proper strong modules and hence induces a color-preserving quotient isomorphism. Conversely, a quotient isomorphism together with isomorphisms between corresponding child modules combines to an isomorphism because adjacency between distinct modules is uniform.

There are \(O(N)\) modular-decomposition nodes and therefore at most \(O(N^2)\) node-pair tests. All prime quotient tests have treewidth bounded by a function of \(k+b\), so the total running time is
\[
f_{\mathrm{tw}}\!\left(3(2^{k+2}-1)(b+1)\right)N^{O(1)}.
\]
This is FPT in \(k+b\). ∎

This result includes arbitrary series and parallel substitutions; large complete or independent quotients cause no difficulty. I do not claim that this formulation is new.

## 5. Why the extra parameter cannot be removed by this argument

Consider the half-graph \(L_m\) with bipartition
\[
A=\{a_1,\dots,a_m\},\qquad B=\{b_1,\dots,b_m\},
\]
and
\[
a_i b_j\in E(L_m)\quad\Longleftrightarrow\quad i\leq j.
\]

### Clique-width at most \(3\)

Process \(i=m,m-1,\dots,1\), maintaining all existing \(A\)-vertices in label \(1\) and all existing \(B\)-vertices in label \(2\):

1. create \(b_i\) with label \(3\), then relabel \(3\to2\);
2. create \(a_i\) with label \(3\);
3. join labels \(2\) and \(3\);
4. relabel \(3\to1\).

This constructs exactly \(L_m\), so
\[
\operatorname{cw}(L_m)\leq3.
\]

### The graph is prime

Suppose a proper module \(M\) meets both sides, say \(a_i,b_j\in M\).

- Every \(b_q\) with \(q\geq i\) must belong to \(M\), because it distinguishes \(a_i\) from \(b_j\). In particular, \(b_m\in M\).
- Every \(a_p\) with \(p\leq j\) must belong to \(M\), so \(a_1\in M\).

Any \(a_p\notin M\) distinguishes \(b_m\) from \(a_i\), forcing all of \(A\) into \(M\). Similarly, any \(b_q\notin M\) distinguishes \(a_1\) from \(b_j\), forcing all of \(B\) into \(M\). Thus \(M=V(L_m)\).

If a module contains two vertices \(a_i,a_j\) with \(i<j\), then \(b_i\) distinguishes them. Similarly, \(a_j\) distinguishes \(b_i,b_j\). Hence there is no nontrivial proper module.

### Unbounded biclique number and treewidth

Let
\[
s=\left\lfloor\frac{m+1}{2}\right\rfloor.
\]
Then
\[
\{a_1,\dots,a_s\}
\quad\text{and}\quad
\{b_{m-s+1},\dots,b_m\}
\]
span a \(K_{s,s}\). Thus \(\beta(L_m)\geq s\).

Moreover,
\[
|E(L_m)|=\frac{m(m+1)}2
 \leq \frac12\binom{2m}{2}
\]
for \(m\geq2\), so the canonical orientation leaves \(L_m\) unchanged. Since \(L_m\) is prime,
\[
\mu(L_m)\geq \left\lfloor\frac{m+1}{2}\right\rfloor.
\]
Also,
\[
\operatorname{tw}(L_m)\geq s,
\]
because treewidth is subgraph-monotone and \(\operatorname{tw}(K_{s,s})=s\).

Therefore the modular biclique-free theorem does not yield an FPT algorithm even on all clique-width-\(3\) graphs. The treewidth route cannot handle the half-graph family, despite its very simple isomorphism structure.

## 6. A local rank-width observation and the remaining gap

There is no local \(n^{\Theta(r)}\) obstruction at a single cut. If a specified bipartite graph has binary adjacency-matrix rank at most \(r\), then it has at most \(2^r\) distinct rows and at most \(2^r\) distinct columns. Grouping equal rows and columns produces a weighted bipartite quotient with at most \(2^{r+1}\) vertices. Brute-force canonization of this quotient takes
\[
(2^r)!^2\,N^{O(1)}
 =2^{O(r2^r)}N^{O(1)}.
\]
Thus the crossing relation at one rank-\(r\) cut can be canonized in FPT time.

The unresolved issue is global: an isomorphism need not map a chosen rank decomposition to a chosen rank decomposition of the other graph, and the identifications made at different, nested cuts must be mutually compatible. The local compression above does not supply an isomorphism-invariant decomposition or solve this consistency problem.

Hence neither a full FPT algorithm nor a parameterized hardness result follows. The half-graph example shows precisely why reducing bounded clique-width to bounded treewidth, even after ordinary modular decomposition, cannot settle the original conjecture.