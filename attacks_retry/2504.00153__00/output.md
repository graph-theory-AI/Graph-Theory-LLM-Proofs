```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain exact characterizations for hereditary cograph classes and for classes of line graphs, but not for arbitrary graph classes.",
  "would_publish": false,
  "caveats": "The general characterization remains unresolved here; overlap of these special-case results with the full source paper has not been checked."
}
```

# Partial solution: cographs and line graphs

All graphs below are finite and simple. I use the induced-subgraph definition of \(\chi\)-boundedness: a class \(\mathcal D\) is bounded by \(f\) if
\[
\chi(B[X])\le f(\omega(B[X]))
\]
for every \(B\in\mathcal D\) and \(X\subseteq V(B)\). We may take \(f\) nondecreasing. Factors can therefore be restricted to their common vertex set.

The main results established below are:

**Theorem A — cographs.**  
Let \(\mathcal C\) be a hereditary class of cographs. Then \(\mathcal C\) is intersectionwise \(\chi\)-guarding if and only if

- \(\mathcal C\) does not contain all complete multipartite graphs, and
- \(\mathcal C\) does not contain all trivially perfect graphs.

Here cographs are the graphs generated from single vertices by disjoint union and complete join. Trivially perfect graphs are the comparability graphs of rooted forests under the ancestor relation.

**Theorem B — line graphs.**  
For any class \(\mathcal F\) of graphs, the class
\[
L(\mathcal F)=\{L(F):F\in\mathcal F\}
\]
is intersectionwise \(\chi\)-guarding if and only if
\[
\sup_{F\in\mathcal F}\chi(F)<\infty.
\]

In fact, for line-graph classes, it suffices to test intersection with the single perfect class
\[
\mathcal P=\{\overline{L(D)}:D\text{ is bipartite}\}.
\]

The complete-multipartite shift obstruction from the supplied attempt is checked directly below. The line-graph obstruction is strengthened: its second factor can be chosen perfect, rather than merely linearly \(\chi\)-bounded.

---

## 1. A coloring condition that guarantees guarding

We first isolate the positive condition used for cographs.

### Lemma 1

Fix positive integers \(c\) and \(s\ge2\). Suppose every \(A\in\mathcal C\) has a partition
\[
V(A)=V_1\cup\cdots\cup V_c
\]
such that every connected component of every \(A[V_i]\) has independence number less than \(s\). Then \(\mathcal C\) is intersectionwise \(\chi\)-guarding.

More precisely, if \(\mathcal D\) is \(\chi\)-bounded by \(f\), then its graph-intersection with \(\mathcal C\) is bounded by
\[
q\longmapsto c\,f\bigl(R(s,q+1)-1\bigr),
\tag{1}
\]
where \(R\) denotes a Ramsey number.

#### Proof

Let \(G=A\cap B\), where \(A\in\mathcal C\), \(B\in\mathcal D\), and \(\omega(G)\le q\). Fix a component \(C\) of some \(A[V_i]\).

If \(K\subseteq V(C)\) is a clique of \(B\), then
\[
G[K]=A[K].
\]
Consequently \(A[K]\) has neither an independent set of size \(s\) nor a clique of size \(q+1\). Thus
\[
|K|<R(s,q+1).
\]
It follows that
\[
\chi(G[V(C)])
\le \chi(B[V(C)])
\le f\bigl(R(s,q+1)-1\bigr).
\]

Different components of \(A[V_i]\) are anticomplete in \(G\), so they can reuse colors. Using disjoint palettes for the \(c\) parts proves (1). The same argument applies to every induced subgraph of \(G\). \(\square\)

---

## 2. Two hereditary non-guarding classes

### 2.1 Complete multipartite graphs

Let
\[
V(S_n)=\{(i,j):1\le i<j\le n\},
\]
where \((i,j)\) and \((j,k)\) are adjacent whenever \(i<j<k\). This is the shift graph.

It is triangle-free: in a hypothetical triangle, order the first coordinates as \(a<b<c\). The vertex with first coordinate \(a\) would need second coordinate both \(b\) and \(c\).

Also,
\[
\chi(S_n)\ge \lceil\log_2 n\rceil.
\tag{2}
\]
Indeed, given a coloring with colors in \([t]\), define
\[
C_i=\{\text{colors of }(i,j):j>i\},\qquad C_n=\varnothing.
\]
For \(i<j\), the color of \((i,j)\) belongs to \(C_i\setminus C_j\). Thus the \(n\) sets \(C_i\) are distinct, giving \(n\le2^t\).

Partition the vertices into
\[
P_i=\{(i,j):j>i\}.
\]
Let \(M_n\) be the complete multipartite graph with these nonempty parts. Let \(D_n\) be obtained from \(S_n\) by making every \(P_i\) a clique. Then
\[
M_n\cap D_n=S_n.
\tag{3}
\]

The hereditary closure of the \(D_n\) is \(\chi\)-bounded by \(2\omega\). To see this, fix \(X\subseteq V(D_n)\), and put \(r=\omega(D_n[X])\). Each \(P_i\cap X\) has at most \(r\) vertices. Order \(X\) by increasing first coordinate. A vertex \((i,j)\) has at most \(r-1\) later neighbors in \(P_i\), and at most \(r\) later neighbors in \(P_j\). Reverse greedy coloring therefore gives
\[
\chi(D_n[X])\le2r.
\]

Together with (2) and (3), this proves:

### Proposition 2

The class of complete multipartite graphs is not intersectionwise \(\chi\)-guarding. Failure is witnessed by a class bounded by \(2\omega\).

---

### 2.2 Trivially perfect graphs

The following obstruction is useful because it lies in a much smaller class than the interval graphs used in the supplied attempt.

### Lemma 3: an online forest strategy

For every \(t\ge1\), there is a strategy presenting a forest one vertex at a time that forces every proper online coloring to use at least \(t\) colors. At most \(2^t-1\) vertices are presented.

The strategy can additionally maintain a distinguished set \(S\), with at most one vertex in each component, on which at least \(t\) colors occur.

#### Proof

For \(t=1\), present one vertex.

Suppose the assertion holds for \(t\). Run two copies of the strategy, on disjoint forests, obtaining distinguished sets \(S_1,S_2\). If their union uses at least \(t+1\) colors, retain \(S_1\cup S_2\).

Otherwise both sets use the same set of exactly \(t\) colors. Present a new vertex adjacent to every vertex of \(S_1\). This creates no cycle, since \(S_1\) has at most one vertex in each component. Its color is new relative to \(S_1\). Retain the new vertex together with \(S_2\).

The number of presented vertices is at most
\[
2(2^t-1)+1=2^{t+1}-1.
\]
All stated invariants are preserved. \(\square\)

### Proposition 4

The class of trivially perfect graphs is not intersectionwise \(\chi\)-guarding. Again, failure is witnessed by a class bounded by \(2\omega\).

#### Proof

Fix \(k\ge1\), and run the strategy of Lemma 3 for \(t=k+1\), allowing responses only from the palette \([k]\).

Form the finite rooted tree \(T_k\) of all possible proper response histories:

- a node represents the next vertex requested by the strategy;
- its children represent the possible legal colors assigned to that vertex, followed by the next request.

Every branch has at most \(2^{k+1}-1\) nodes. No branch can finish the strategy successfully using only \(k\) colors, so every terminal request has no legal color.

Define a graph \(H_k\) on \(V(T_k)\). Two nodes can be adjacent only when one is an ancestor of the other; their adjacency is the adjacency prescribed by the forest presentation along that history.

Two properties follow.

1. **Every root-to-leaf path induces a forest in \(H_k\).**  
   Such a path is a partial run of the strategy, including its final request.

2. **\(\chi(H_k)>k\).**  
   A proper \(k\)-coloring of \(H_k\) would determine a path through \(T_k\): at each request follow the child corresponding to its color. This is always a legal response, contradicting the terminal request.

Every triangle in \(H_k\) would consist of pairwise comparable nodes, hence lie on a root-to-leaf path. Thus \(H_k\) is triangle-free.

Let \(A_k\) be the ancestor-comparability graph of \(T_k\), and set
\[
B_k=H_k\cup\overline{A_k}.
\]
Then \(A_k\) is trivially perfect and
\[
A_k\cap B_k=H_k.
\tag{4}
\]

It remains to bound the \(B_k\). Fix \(X\subseteq V(T_k)\), and put
\[
r=\omega(B_k[X]).
\]
Every antichain of the rooted-tree order is a clique in \(B_k\). In particular, \(X\) has at most \(r\) maximal elements. Assign each vertex of \(X\) to one maximal descendant. Each assigned set is a chain, so \(X\) is partitioned into at most \(r\) chains.

On a chain, \(B_k\) agrees with \(H_k\), and hence induces a forest. Coloring each chain with a separate two-color palette gives
\[
\chi(B_k[X])\le2r.
\]
Thus the hereditary closure of the \(B_k\) is bounded by \(2\omega\), while (4) produces triangle-free graphs of unbounded chromatic number. \(\square\)

---

## 3. Exact characterization for hereditary cograph classes

For integers \(r,s\ge2\), write
\[
M_{r,s}=K_{\underbrace{s,\ldots,s}_{r\text{ parts}}}.
\]
Define trivially perfect graphs recursively by
\[
Q_{1,s}=K_{1,s},
\qquad
Q_{h+1,s}=K_1\vee(Q_{h,s}\mathbin{\dot\cup}Q_{h,s}),
\tag{5}
\]
where \(\vee\) denotes complete join. Notice that
\[
\alpha(Q_{h,s})=s\,2^{h-1}.
\]

### Lemma 5: quantitative cograph decomposition

Fix \(r,s\ge2\) and \(h\ge1\). Every cograph with no induced \(M_{r,s}\) or \(Q_{h,s}\) has a partition into \(c_h\) parts such that every monochromatic component has independence number less than \(s\), where
\[
c_1=1,\qquad
c_h=(r-1)(r c_{h-1}+1)\quad(h\ge2).
\tag{6}
\]

#### Proof

We use induction on \(h\). Different connected components may reuse palettes.

For \(h=1\), let \(G\) be a connected cograph. If \(G\) is nontrivial, it is a complete join of at least two nonempty cographs. An independent set of size \(s\) must lie in one join factor; a vertex in another factor would complete it to an induced \(K_{1,s}\). Therefore every \(K_{1,s}\)-free connected cograph has independence number less than \(s\). This proves the base case.

Now let \(h\ge2\), and assume \(G\) is connected and nontrivial. Use an alternating cotree for \(G\):

- leaves are vertices;
- internal nodes are labeled union or join;
- labels alternate along internal edges;
- every internal node has at least two children;
- adjacency of two leaves is determined by the label of their least common ancestor.

Since \(G\) is connected, the root is a join node. For a cotree node \(t\), let \(G_t\) be the graph induced by its descendant leaves.

Call \(t\) **heavy** if \(G_t\) contains an induced \(Q_{h-1,s}\). If the root is not heavy, induction already gives the desired partition. Otherwise the heavy nodes form an ancestor-closed subtree.

We need two observations.

#### Observation 1: union nodes have at most one heavy child

Every union node has a join parent. If a union node had two heavy children, take an induced \(Q_{h-1,s}\) from each, and take one vertex from a different child of its join parent. These vertices induce \(Q_{h,s}\), contrary to hypothesis.

#### Observation 2: the heavy subtree has at most \(r-1\) leaves

Two distinct terminal heavy nodes have a join node as their least common ancestor, by Observation 1. Their descendant vertex sets are therefore complete to one another.

Each terminal heavy node contains an independent set of size \(s\). Thus \(r\) terminal heavy nodes would yield an induced \(M_{r,s}\).

Partition the heavy subtree into at most \(r-1\) downward paths. Every graph vertex lies in a nonheavy child subtree attached to one of these paths: cotree leaves themselves are not heavy.

Fix one heavy path \(P\). Consider its attached nonheavy subtrees.

- **Attachments at union nodes** are pairwise anticomplete. Each avoids \(Q_{h-1,s}\), so all of these attachments together can use the same \(c_{h-1}\) palettes from induction.

- **Attachments at join nodes** are pairwise complete. At most \(r-1\) of them can have independence number at least \(s\), since \(r\) such attachments would induce \(M_{r,s}\). Color each of these large attachments using its own \(c_{h-1}\) palettes.

- All remaining join attachments have independence number less than \(s\). Since they are pairwise complete, their entire union has independence number less than \(s\), and can be assigned one additional part.

Thus the vertices assigned to \(P\) require at most
\[
c_{h-1}+(r-1)c_{h-1}+1=r c_{h-1}+1
\]
parts. Use disjoint palettes for the at most \(r-1\) heavy paths. This gives (6). \(\square\)

### Universality of the obstruction sequences

Every complete multipartite graph is an induced subgraph of some \(M_{r,s}\).

Also, for fixed \(s\ge2\), every trivially perfect graph is an induced subgraph of some \(Q_{h,s}\). Here is a direct verification.

Let \(U_m\) be the ancestor-comparability graph of the complete binary rooted tree with \(m\) levels. Every trivially perfect graph on \(m\) vertices embeds inducedly in \(U_m\), by induction:

- for a disconnected graph, put one component in one principal subtree and the remaining components in the other;
- for a connected graph, choose a universal vertex, map it to the root, and embed the remaining trivially perfect graph in one principal subtree.

By (5), \(Q_{h,s}\) contains \(U_{h+1}\).

### Proof of Theorem A

Suppose first that \(\mathcal C\) is guarding. Propositions 2 and 4 show that it can contain neither all complete multipartite graphs nor all trivially perfect graphs.

Conversely, suppose that \(\mathcal C\) is hereditary and misses a complete multipartite graph \(M\) and a trivially perfect graph \(T\). By the preceding universality observations, there exist \(r,s\ge2\) and \(h\ge1\) such that every member of \(\mathcal C\) avoids both \(M_{r,s}\) and \(Q_{h,s}\).

Lemma 5 supplies a uniform partition with bounded independence number in every monochromatic component. Lemma 1 then proves that \(\mathcal C\) is guarding. Explicitly, against a class bounded by \(f\), a bound is
\[
q\longmapsto c_h f\bigl(R(s,q+1)-1\bigr).
\]
This proves Theorem A. \(\square\)

### Consequences

1. **Two minimal hereditary non-guarding classes.**  
   Every proper hereditary subclass of the complete multipartite graphs is guarding. The same is true of every proper hereditary subclass of the trivially perfect graphs.

   Indeed, complete multipartite graphs omit the trivially perfect graph \(2K_2\), while trivially perfect graphs omit the complete multipartite graph \(C_4\).

2. **Forbidden-subgraph characterization within cographs.**  
   For any family \(\mathcal H\) of nonempty graphs,
   \[
   \{\text{cographs}\}\cap\operatorname{Forb}(\mathcal H)
   \]
   is guarding if and only if \(\mathcal H\) contains a complete multipartite graph and a trivially perfect graph. These may be the same member.

3. **Linear witnesses suffice for cographs.**  
   Whenever a hereditary cograph class is not guarding, failure is witnessed by a class bounded by \(2\omega\).

---

## 4. Exact characterization for line-graph classes

### 4.1 Bounded chromatic number of roots is sufficient

Suppose
\[
\chi(F)\le d
\]
for every \(F\in\mathcal F\), where \(d\ge2\). Put
\[
\ell=\lceil\log_2 d\rceil.
\]

A proper \(d\)-coloring of \(F\), encoded by \(\ell\)-bit strings, partitions \(E(F)\) into \(\ell\) bipartite graphs: assign an edge to the first bit on which its endpoint colors differ.

Let
\[
G=L(F)\cap B,\qquad \omega(G)\le q,
\]
where \(B\) belongs to a class bounded by \(f\). For each root vertex \(v\in V(F)\), let \(S_v\) be the set of edges incident with \(v\). It is a clique in \(L(F)\), so
\[
G[S_v]=B[S_v].
\]
Choose a proper coloring
\[
c_v:G[S_v]\longrightarrow[f(q)].
\]

For an edge \(e=uv\) assigned to bit \(i\), write the endpoints so that \(u\) has bit \(0\) and \(v\) has bit \(1\), and give \(e\), as a vertex of \(G\), the color
\[
\bigl(i,c_u(e),c_v(e)\bigr).
\tag{7}
\]
If two adjacent vertices of \(G\) have the same bit index, they share a root vertex whose bit determines the same coordinate in (7). Their local colors in that coordinate differ. Thus (7) is proper, and
\[
\chi(G)\le
\lceil\log_2 d\rceil\,f(q)^2.
\tag{8}
\]

If \(d\le1\), all root graphs are edgeless and their line graphs are empty. This covers the remaining case.

---

### 4.2 Unbounded chromatic number of roots is necessary

Fix a graph \(F\) and a total order on \(V(F)\). Orient each edge forward.

Define \(S(F)\) on \(E(F)\), with two edges adjacent exactly when their orientations form a directed two-edge path:
\[
(u,v)\sim(v,w).
\]
As for the shift graph, \(S(F)\) is triangle-free.

If \(S(F)\) has a coloring with \(t\) colors, assign to each \(v\in V(F)\) the set of colors occurring on edges directed out of \(v\). For every directed edge \((u,v)\), its color belongs to the set at \(u\) but not the set at \(v\). These sets properly color \(F\), so
\[
\chi(F)\le2^t.
\]
Consequently,
\[
\chi(S(F))\ge \lceil\log_2\chi(F)\rceil.
\tag{9}
\]

Now define \(B_F\) on the directed edges of \(F\) by
\[
(u,v)\sim(x,y)
\quad\Longleftrightarrow\quad
u\ne x\ \text{ and }\ v\ne y.
\tag{10}
\]
Then
\[
L(F)\cap B_F=S(F).
\tag{11}
\]
Indeed, two edges meeting at a common tail or a common head are removed by (10), while edges meeting head-to-tail are retained.

Crucially, \(B_F\) is perfect. Construct a bipartite graph \(D_F\) with a left and right copy of \(V(F)\), replacing each directed edge \((u,v)\) by \(u_Lv_R\). Equation (10) says precisely that
\[
B_F=\overline{L(D_F)}.
\]

For completeness, if \(D'\) is any bipartite graph, then
\[
\omega(\overline{L(D')})=\nu(D'),
\]
the maximum matching size. By the bipartite matching–vertex-cover theorem, \(D'\) has a vertex cover of size \(\nu(D')\). Assigning each edge to one of its endpoints in that cover partitions the edges into \(\nu(D')\) stars, which are independent sets in \(\overline{L(D')}\). Hence
\[
\chi(\overline{L(D')})=\omega(\overline{L(D')}).
\]
The same argument applies after selecting any subset of edges, proving perfectness.

If \(\chi(F)\) is unbounded on \(\mathcal F\), equations (9) and (11) therefore give triangle-free intersections of unbounded chromatic number with the fixed perfect class
\[
\mathcal P=\{\overline{L(D)}:D\text{ bipartite}\}.
\]
Together with (8), this proves Theorem B. \(\square\)

---

## 5. A finite-forbidden characterization within line graphs

Theorem B gives another exact special case.

### Corollary 6

Let \(\mathcal H\) be a finite family of nonempty graphs. Then
\[
\{\text{line graphs}\}\cap\operatorname{Forb}(\mathcal H)
\]
is intersectionwise \(\chi\)-guarding if and only if some member of \(\mathcal H\) is the line graph of a forest.

#### Proof: sufficiency

Suppose \(L(T)\in\mathcal H\), where \(T\) is a forest. Delete isolated vertices from \(T\), and put \(t=|V(T)|\).

If \(L(F)\) is \(\mathcal H\)-free, then \(F\) cannot contain \(T\) as a subgraph: selecting the edges of such a copy would induce \(L(T)\) in \(L(F)\).

Every graph with chromatic number at least \(t\) contains \(T\) as a subgraph. Indeed, it has a subgraph of minimum degree at least \(t-1\), in which the \(t\)-vertex forest can be embedded greedily. Therefore
\[
\chi(F)\le t-1,
\]
and Theorem B applies.

#### Proof: necessity

Suppose no member of \(\mathcal H\) is the line graph of a forest, and set
\[
m=\max\bigl(\{3\}\cup\{|V(H)|:H\in\mathcal H\}\bigr).
\]
Let \(F\) have girth greater than \(m\). Every induced subgraph of \(L(F)\) on at most \(m\) vertices is the line graph of a forest: its vertices select at most \(m\) root edges, which cannot contain a cycle. Hence \(L(F)\) is \(\mathcal H\)-free.

Graphs of girth greater than \(m\) have unbounded chromatic number, so Theorem B proves non-guarding. \(\square\)

The high-girth fact used here has a short probabilistic proof. For fixed \(g,k\), take \(G(n,p)\) with
\[
p=n^{-1+1/(2g)}.
\]
The expected number of cycles of length at most \(g\) is \(O(n^{1/2})\), while the probability of an independent set of size \(\lceil n/(2k)\rceil\) tends to zero, since
\[
\binom{n}{\lceil n/(2k)\rceil}
(1-p)^{\binom{\lceil n/(2k)\rceil}{2}}
\le \exp\bigl(O(n)-\Omega(n^{1+1/(2g)})\bigr).
\]
Choose an outcome with at most \(n/4\) short cycles and no such independent set, and delete one vertex from each short cycle. The remaining graph has girth greater than \(g\) and chromatic number greater than \(k\).

In particular, for the original finite-forbidden problem we obtain the necessary condition
\[
\operatorname{Forb}(\mathcal H)\text{ guarding}
\quad\Longrightarrow\quad
\mathcal H\text{ contains the line graph of a forest}.
\tag{12}
\]
This strengthens the “some forbidden graph is a line graph” condition in the supplied attempt.

---

## 6. Why the cograph decomposition is not a general characterization

The partition condition in Lemma 1 is sufficient, and Theorem A shows it is necessary **within cographs**. It is not necessary for arbitrary guarding classes.

Consider
\[
A_n=L(K_{n,n}).
\]
These graphs belong to a guarding class by Theorem B, with bound \(f(q)^2\), since their roots are bipartite.

Nevertheless, there are no fixed \(c,s\) giving the partition condition of Lemma 1 for all \(A_n\).

To prove this, interpret a partition of \(V(A_n)\) into \(c\) parts as a coloring of \(E(K_{n,n})\). A monochromatic line-graph component has independence number equal to the matching number of the corresponding root component.

If every such matching number were at most \(s-1\), the endpoints of a maximal matching would cover the edges of each root component using at most \(2(s-1)\) vertices. Thus each color class has at most
\[
2(s-1)\sum_C |V(C)|
\le4(s-1)n
\]
edges. Summing over all colors gives
\[
n^2\le4c(s-1)n,
\]
which fails for sufficiently large \(n\).

Thus a full characterization must accommodate guarding mechanisms beyond bounded-independence monochromatic components.

---

## 7. Remaining gap

The general question is not resolved.

What is established here is:

- an exact characterization for every hereditary subclass of the cographs;
- an exact characterization for line-graph classes, with a fixed perfect testing class;
- an exact finite-forbidden characterization inside line graphs;
- stronger necessary forbidden-subgraph conditions for the original problem.

In particular, every guarding hereditary class must omit at least one complete multipartite graph and at least one trivially perfect graph. For a finite forbidden family, it must also forbid a line graph of a forest. No sufficiency argument is given for these conditions outside the special settings proved above.

I have not checked the full source paper, so these are self-contained mathematical conclusions, not claims of literature novelty.