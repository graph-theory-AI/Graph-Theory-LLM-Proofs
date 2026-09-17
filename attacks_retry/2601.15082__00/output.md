```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I characterize bounded ratio for all finitely based hereditary claw-free classes, and for every pair of forbidden induced graphs in which one forbidden graph is a star.",
  "would_publish": false,
  "caveats": "The unrestricted hereditary and dense cases remain unresolved; the literature novelty of these special-case characterizations has not been verified."
}
```

# 1. Statements of the partial results

All graphs are finite and simple. Distances between different components are infinite. Write \(\alpha(G)\) for the ordinary independence number and
\[
\alpha_2(G)=\max\{|I|:\operatorname{dist}_G(u,v)>2
\text{ for distinct }u,v\in I\}.
\]
Empty graphs can be omitted when taking ratios.

A **forest line graph** is a graph \(L(F)\), where \(F\) is a forest. Isolated vertices of \(F\) do not affect \(L(F)\).

The following gives an exact characterization for an infinite collection of dense hereditary classes, allowing arbitrary finite lists of forbidden induced subgraphs.

## Theorem 1: finitely based claw-free classes

Let \(\mathcal H\) be a finite family of nonempty graphs, and let
\[
\mathcal C=
\operatorname{Forb}_{\mathrm{ind}}
\bigl(\{K_{1,3}\}\cup\mathcal H\bigr).
\]
Then
\[
\sup_{G\in\mathcal C}\frac{\gamma(G)}{\alpha_2(G)}<\infty
\]
if and only if \(\mathcal H\) contains a forest line graph.

More quantitatively, if \(H=L(F)\in\mathcal H\), where \(F\) has no isolated vertices and \(f=|V(F)|\), then every \(G\in\mathcal C\) satisfies
\[
\gamma(G)\le \alpha(G)
\le \max\{1,4f-9\}\,\alpha_2(G).
\]

There is also a complete classification when one forbids a larger star and one additional graph.

## Theorem 2: a star and one other forbidden graph

Fix \(r\ge4\) and a nonempty graph \(H\). Then
\[
\sup_{G\in\operatorname{Forb}_{\mathrm{ind}}(K_{1,r},H)}
\frac{\gamma(G)}{\alpha_2(G)}<\infty
\]
if and only if \(H\) is both a split graph and a forest line graph.

Equivalently, the positive cases are precisely:

- \(H\) is edgeless; or
- \(H\) consists of isolated vertices together with one component obtained from a clique by attaching at most one pendant vertex to each clique vertex.

For \(r=3\), Theorem 1 supplies the classification. For \(r=1,2\), the ratio is always at most one: the graphs are respectively edgeless graphs and disjoint unions of cliques.

The proofs below are self-contained; they do not assume the previous attempt’s classification or extremal estimate.

---

# 2. An obstruction family with prescribed small induced subgraphs

The necessity direction of Theorem 1 rests on the following observation.

## Lemma 2.1

For every fixed integer \(g\), there exist claw-free graphs \(Q_n\) such that
\[
\frac{\gamma(Q_n)}{\alpha_2(Q_n)}\longrightarrow\infty,
\]
while every induced subgraph of \(Q_n\) on at most \(g\) vertices is a forest line graph.

### Proof

We first construct graphs \(B_n\) of girth greater than \(g\) such that
\[
\alpha(B_n)=o(|V(B_n)|).
\]
Increase \(g\) to at least three if necessary. For a large integer \(n\), set
\[
p=n^{-1+1/(2g)},\qquad
s=\left\lceil 4p^{-1}\log n\right\rceil,
\]
and sample \(B\sim G(n,p)\).

The expected number of cycles of lengths between three and \(g\) is at most
\[
\sum_{\ell=3}^{g}\frac{n^\ell p^\ell}{2\ell}
\le g n^{1/2}.
\]
Thus, with probability \(1-o(1)\), there are at most \(n^{3/4}\) such cycles.

Also,
\[
\Pr(\alpha(B)\ge s)
\le \binom ns(1-p)^{\binom s2}
\le \exp\left(s\log n-\frac{ps(s-1)}2\right)
=o(1).
\]
Indeed, \(p(s-1)\ge3\log n\) for all sufficiently large \(n\). Notice that \(s=o(n)\).

Choose an outcome satisfying both conclusions, and delete one vertex from each cycle of length at most \(g\). The resulting graph \(B_n\) has
\[
|V(B_n)|\ge n-n^{3/4},\qquad
\alpha(B_n)<s=o(n),
\]
and girth greater than \(g\).

Now put \(Q_n=L(B_n)\). Every line graph is claw-free.

For any graph \(B\) with at least one edge, a dominating set of \(L(B)\) corresponds to a set \(D\subseteq E(B)\) whose endpoints form a vertex cover of \(B\). Consequently,
\[
2|D|\ge |V(B)|-\alpha(B),
\]
so
\[
\gamma(L(B))\ge \frac{|V(B)|-\alpha(B)}2.
\]

Moreover, a 2-independent set in \(L(B)\) is an induced matching in \(B\). Choosing one endpoint of each edge of an induced matching gives an independent set in \(B\). Hence
\[
\alpha_2(L(B))\le \alpha(B).
\]
It follows that
\[
\frac{\gamma(Q_n)}{\alpha_2(Q_n)}
\ge
\frac{|V(B_n)|-\alpha(B_n)}{2\alpha(B_n)}
\longrightarrow\infty.
\]

Finally, an induced subgraph of \(Q_n\) on at most \(g\) vertices corresponds to a set of at most \(g\) edges of \(B_n\). Those edges form a forest, since \(B_n\) has girth greater than \(g\). The induced subgraph is therefore a forest line graph. \(\square\)

This argument supplies, in particular, simultaneous obstructions for any finite list of graphs none of which is a forest line graph.

---

# 3. A line-graph representation inside claw-free graphs

We next prove the sufficient direction of Theorem 1.

Let \(I\) be an independent set of a graph \(G\). Define its **conflict graph** \(J_I\) on vertex set \(I\) by
\[
uv\in E(J_I)
\quad\Longleftrightarrow\quad
N_G(u)\cap N_G(v)\ne\varnothing.
\]
Because \(I\) is independent, independent sets of \(J_I\) are 2-independent in \(G\). Thus
\[
\alpha(J_I)\le \alpha_2(G). \tag{3.1}
\]

The useful point is that claw-freeness imposes a strong representation on \(J_I\).

## Lemma 3.1

Suppose \(G\) is claw-free and \(I\subseteq V(G)\) is independent. For every edge \(uv\in E(J_I)\), choose a common neighbor \(x_{uv}\).

There is a simple graph \(B\), with a perfect matching indexed by \(I\), such that
\[
G\bigl[I\cup\{x_{uv}:uv\in E(J_I)\}\bigr]\cong L(B).
\]
The graph \(B\) has \(2|I|\) vertices and
\[
|I|+|E(J_I)|
\]
edges.

### Proof

Every vertex outside \(I\) has at most two neighbors in \(I\), since three would induce a claw. Hence
\[
N_G(x_{uv})\cap I=\{u,v\}.
\]
In particular, the chosen witnesses for distinct edges of \(J_I\) are distinct.

Two elementary restrictions govern their adjacencies.

**Disjoint pairs.** If \(\{u,v\}\cap\{a,b\}=\varnothing\), then \(x_{uv}\) and \(x_{ab}\) are nonadjacent. Otherwise \(x_{uv}\), with leaves \(u,v,x_{ab}\), would induce a claw.

**Pairs sharing one endpoint.** Fix \(v\in I\), and consider
\[
X_v=\{x_{vu}:vu\in E(J_I)\}.
\]
The graph \(G[X_v]\) has no induced \(P_3\). Indeed, if
\[
x_{va}-x_{vb}-x_{vc}
\]
were an induced \(P_3\), then \(x_{vb}\), with leaves \(x_{va},x_{vc},b\), would induce a claw.

Thus \(G[X_v]\) is a disjoint union of cliques. There are at most two such cliques, because three vertices from different components, together with \(v\), would induce a claw.

For each \(v\in I\), create two vertices \(v^0,v^1\) of \(B\), joined by an edge \(m_v\). Assign the at most two clique components of \(G[X_v]\) to \(v^0,v^1\), allowing an empty component.

For every \(uv\in E(J_I)\), add an edge joining the copy of \(u\) assigned to \(x_{uv}\) to the copy of \(v\) assigned to \(x_{uv}\).

Under the correspondence
\[
v\longleftrightarrow m_v,\qquad
x_{uv}\longleftrightarrow
\text{the added edge for }uv,
\]
the adjacencies are exactly those of a line graph:

- the edges \(m_v\) form a matching;
- an added edge for \(uv\) meets precisely \(m_u,m_v\);
- added edges for disjoint pairs do not meet;
- added edges sharing \(v\) meet exactly when their witnesses belong to the same clique component of \(G[X_v]\).

This proves the asserted induced-subgraph representation. \(\square\)

## Lemma 3.2

Let \(F\) be a forest without isolated vertices, and put \(f=|V(F)|\). Every claw-free, induced-\(L(F)\)-free graph \(G\) satisfies
\[
\alpha(G)\le \max\{1,4f-9\}\,\alpha_2(G).
\]

### Proof

The case \(f=2\) means \(L(F)=K_1\), so there are no nonempty graphs to consider. Assume \(f\ge3\).

Choose a maximum independent set \(I\) of \(G\), and construct \(J_I\) and \(B\) as in Lemma 3.1.

The graph \(B\) contains no copy of \(F\) as a subgraph. Such a copy, even if not induced, would give an induced copy of \(L(F)\) in \(L(B)\), and hence in \(G\).

Every \(F\)-subgraph-free graph is \((f-2)\)-degenerate. To see this, any graph of minimum degree at least \(f-1\) contains \(F\): order the vertices of each tree component with parents preceding children, and embed greedily, starting each new component at an unused vertex.

Put \(d=f-2\). For every nonempty \(U\subseteq I\), let \(B_U\) consist of:

- the two vertices and matching edge corresponding to each \(u\in U\);
- the added edges corresponding to \(E(J_I[U])\).

Then \(B_U\) is \(F\)-free and therefore \(d\)-degenerate. Consequently,
\[
|U|+|E(J_I[U])|
=|E(B_U)|
\le d|V(B_U)|
=2d|U|.
\]
Thus
\[
|E(J_I[U])|\le(2d-1)|U|.
\]
Every induced subgraph of \(J_I\) has average degree at most \(4d-2\). Therefore \(J_I\) is \((4d-2)\)-degenerate and can be colored with \(4d-1=4f-9\) colors.

Using (3.1),
\[
\alpha(G)=|I|
\le(4f-9)\alpha(J_I)
\le(4f-9)\alpha_2(G).
\]
\(\square\)

### Proof of Theorem 1

If some \(H=L(F)\) belongs to \(\mathcal H\), Lemma 3.2 applies. Since a maximum independent set is dominating,
\[
\gamma(G)\le\alpha(G),
\]
giving the stated bound.

Conversely, suppose no member of \(\mathcal H\) is a forest line graph. Choose \(g\) at least as large as the order of every graph in \(\mathcal H\). By Lemma 2.1, there are claw-free graphs of unbounded ratio whose induced subgraphs on at most \(g\) vertices are all forest line graphs. They avoid every member of \(\mathcal H\), so they belong to \(\mathcal C\). Thus the ratio is unbounded. \(\square\)

---

# 4. Larger stars: the necessary obstructions

For Theorem 2, Lemma 2.1 already shows that \(H\) must be a forest line graph: its obstruction graphs are claw-free, and hence \(K_{1,r}\)-free for every \(r\ge3\).

A second family shows that \(H\) must be split.

## Lemma 4.1

There are split, \(K_{1,4}\)-free graphs \(S_m\) satisfying
\[
\alpha_2(S_m)=1,\qquad
\gamma(S_m)=\left\lceil\frac m2\right\rceil.
\]

### Proof

For \(m\ge2\), take:

- an independent set \(A=\{a_1,\ldots,a_m\}\);
- a clique \(C=\{c_{ij}:1\le i<j\le m\}\);
- edges from \(a_i\) to \(c_{jk}\) exactly when \(i\in\{j,k\}\).

Every two vertices have distance at most two. In particular, \(a_i,a_j\) have common neighbor \(c_{ij}\). Thus \(\alpha_2(S_m)=1\).

Every vertex dominates at most two vertices of \(A\), so
\[
\gamma(S_m)\ge\left\lceil\frac m2\right\rceil.
\]
Conversely, choose \(\lceil m/2\rceil\) pairs covering \([m]\). Their clique vertices dominate both \(A\) and \(C\), proving equality.

Finally, the neighborhood of a vertex of \(A\) is a clique. The neighborhood of \(c_{ij}\) contains only two vertices of \(A\), and its remaining vertices form a clique. Hence no neighborhood has an independent set of size four, so \(S_m\) is \(K_{1,4}\)-free. \(\square\)

Since split graphs are closed under induced subgraphs, if \(H\) is not split, every \(S_m\) is \(H\)-free. Thus, for \(r\ge4\), bounded ratio requires that \(H\) be both split and a forest line graph.

---

# 5. A Ramsey bound for a star and a clique with private leaves

For \(t\ge2\), let \(T_t\) have a clique
\[
\{c_1,\ldots,c_t\}
\]
and independent vertices
\[
\{\ell_1,\ldots,\ell_t\},
\]
where \(\ell_i\) is adjacent precisely to \(c_i\). Thus \(T_t\) is a clique with one private pendant vertex at each clique vertex.

## Lemma 5.1

Fix \(r\ge3\) and \(t\ge2\), and put
\[
B(t,r)=\binom{t+r-2}{t-1},
\qquad
M(r,t)=(r-2)\bigl(B(t,r)-1\bigr)+1.
\]
Every \(\{K_{1,r},T_t\}\)-free graph \(G\) satisfies
\[
\gamma(G)\le\alpha(G)\le M(r,t)\alpha_2(G).
\]

### Proof

The elementary Ramsey bound says that every graph on \(B(t,r)\) vertices has either a clique of size \(t\) or an independent set of size \(r\). This follows by induction from the neighborhood/nonneighborhood recurrence and Pascal’s identity.

Choose a maximum independent set \(I\), and form its conflict graph \(J_I\).

Fix \(u\in I\). For each \(x\in N_G(u)\), define
\[
A_x=(N_G(x)\cap I)\setminus\{u\}.
\]
Since \(G\) is \(K_{1,r}\)-free,
\[
|A_x|\le r-2.
\]
Also,
\[
N_{J_I}(u)=\bigcup_{x\in N_G(u)}A_x.
\]

Choose an inclusion-minimal subfamily \(X\subseteq N_G(u)\) covering this union. Each \(x\in X\) has a private point
\[
v_x\in A_x\setminus\bigcup_{y\in X\setminus\{x\}}A_y.
\]
These private points are distinct and belong to \(I\).

The graph \(G[X]\) has no independent set of size \(r\), because all vertices of \(X\) are adjacent to \(u\). If \(|X|\ge B(t,r)\), it therefore contains a \(t\)-clique. That clique, together with its private points \(v_x\), induces \(T_t\), a contradiction.

Hence
\[
|X|\le B(t,r)-1,
\]
and
\[
d_{J_I}(u)
\le(r-2)|X|
\le M(r,t)-1.
\]
Thus \(J_I\) has maximum degree at most \(M(r,t)-1\), and
\[
|I|\le M(r,t)\alpha(J_I)
\le M(r,t)\alpha_2(G).
\]
\(\square\)

---

# 6. Completing the classification for larger stars

We need the following elementary structural description.

## Lemma 6.1

A graph is both split and a forest line graph if and only if it is edgeless, or consists of isolated vertices together with one component obtained from a clique by attaching at most one pendant vertex to each clique vertex.

### Proof

A split graph contains no induced \(2K_2\), so it has at most one component containing an edge.

Forest line graphs are claw-free and diamond-free. For the latter assertion, every triangle in the line graph of a forest comes from three edges sharing one endpoint. Two triangles sharing an edge therefore cannot induce a diamond.

Consider the nontrivial component of a split forest line graph. Choose a split partition \(C\cup A\) with \(C\) an inclusion-maximal clique. We may assume \(|C|\ge2\).

Every nonisolated \(a\in A\) has exactly one neighbor in \(C\). It cannot be complete to \(C\), by maximality. If it had at least two neighbors and a nonneighbor in \(C\), those vertices together with \(a\) would induce a diamond.

Thus the vertices of \(A\) in this component are pendant vertices. No vertex of \(C\) can have two such pendant neighbors: together with another vertex of \(C\), they would form the leaves of a claw.

Conversely, \(T_t\) is the line graph of the tree obtained by subdividing every edge of \(K_{1,t}\) once. Removing some pendant vertices from \(T_t\), and adding isolated vertices, still gives the line graph of a forest. The resulting graphs are visibly split. \(\square\)

### Proof of Theorem 2

Necessity was proved in Section 4.

For sufficiency, first suppose \(H=sK_1\). Every \(H\)-free graph satisfies
\[
\gamma(G)\le\alpha(G)\le s-1,
\]
so the ratio is bounded.

Otherwise, by Lemma 6.1, write
\[
H=H_0+zK_1,
\]
where \(H_0\) is connected, contains an edge, and is an induced subgraph of some \(T_t\).

Let \(G\) be \(\{K_{1,r},H\}\)-free.

If \(G\) is \(H_0\)-free, it is \(T_t\)-free, and Lemma 5.1 gives
\[
\gamma(G)\le M(r,t)\alpha_2(G).
\]

Suppose instead that \(X\subseteq V(G)\) induces \(H_0\). Then necessarily \(z\ge1\). Let
\[
U=\{v\in V(G)\setminus X:N_G(v)\cap X=\varnothing\}.
\]
The graph \(G[U]\) has independence number at most \(z-1\), since otherwise \(X\) together with \(z\) independent vertices of \(U\) would induce \(H\).

A maximal independent set \(I_U\) of \(G[U]\) dominates \(U\), and
\[
|I_U|\le z-1.
\]
Consequently, \(X\cup I_U\) dominates \(G\), giving
\[
\gamma(G)\le |V(H_0)|+z-1.
\]

Thus a valid ratio bound is
\[
\max\left\{
M(r,t),\,|V(H_0)|+z-1
\right\}.
\]
This proves sufficiency and completes Theorem 2. \(\square\)

---

# 7. Consequences and a sharper path bound

The two classifications immediately yield the following clean threshold.

## Corollary 7.1

For fixed integers \(r,t\ge1\),
\[
\sup_{G\in\operatorname{Forb}_{\mathrm{ind}}(K_{1,r},P_t)}
\frac{\gamma(G)}{\alpha_2(G)}<\infty
\]
if and only if
\[
r\le3\quad\text{or}\quad t\le4.
\]

Indeed, every path is a forest line graph, and \(P_t\) is split exactly when \(t\le4\). For \(r\ge4,t\ge5\), the graphs \(S_m\) give explicit unbounded-ratio examples: they are split, hence \(P_5\)-free, and are \(K_{1,4}\)-free.

For claw-free graphs, the constant for path exclusion can be improved substantially over Theorem 1.

## Proposition 7.2

For \(t\ge3\), every claw-free, \(P_t\)-free graph satisfies
\[
\gamma(G)\le\alpha(G)\le(t-2)\alpha_2(G).
\]

### Proof

Use the conflict graph \(J_I\) and witnesses from Section 3, with \(I\) a maximum independent set.

Suppose \(J_I\) contains a simple path
\[
u_0u_1\cdots u_\ell.
\]
Let \(x_i=x_{u_{i-1}u_i}\). Nonconsecutive witnesses are nonadjacent, by Lemma 3.1.

Construct a path in \(G\) starting at \(u_0\), proceeding through \(x_1,\ldots,x_\ell\), and ending at \(u_\ell\). Between \(x_i\) and \(x_{i+1}\), insert \(u_i\) precisely when those witnesses are nonadjacent.

This is an induced path: each witness has exactly its two specified neighbors in \(I\), and nonconsecutive witnesses are nonadjacent. It has at least \(\ell+2\) vertices. Therefore \(P_t\)-freeness implies
\[
\ell\le t-3.
\]

A graph with minimum degree at least \(t-2\) has a simple path with at least \(t-2\) edges. Hence \(J_I\) is \((t-3)\)-degenerate and is \((t-2)\)-colorable. Now use (3.1). \(\square\)

---

# 8. Scope and remaining gap

Theorem 1 genuinely needs a finite forbidden family. For example, the hereditary class of all forest line graphs has bounded ratio but excludes no forest line graph.

For completeness, its ratio is at most two. If \(F\) is a forest and \(M\) is a maximum matching, then \(M\) is an edge-dominating set, so
\[
\gamma(L(F))\le |M|.
\]
The conflict graph on \(M\), joining two matching edges when an edge of \(F\) connects their endpoints, is a forest: it is obtained by contracting \(M\) and deleting unmatched vertices. It has an independent set of size at least \(|M|/2\), corresponding to an induced matching in \(F\). Thus
\[
\gamma(L(F))\le2\alpha_2(L(F)).
\]

Accordingly, these results do **not** characterize:

- arbitrary hereditary claw-free classes with infinitely many forbidden induced subgraphs;
- general finitely based hereditary classes without the stated star restrictions;
- arbitrary dense or monotone classes.

They do give complete, proved classifications within two substantial hereditary settings, including dense classes. No assertion of literature novelty is made without an independent literature check.