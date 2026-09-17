```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The sharp conjectured bound holds for independent-set blow-ups of graphs formed by clique-sums of cycles and cliques, including all outerplanar base graphs.",
  "would_publish": false,
  "caveats": "This is a structural special case, not a general solution; novelty is not claimed, and the clique-gluing step does not establish a list-colouring version."
}
```

# 1. A larger sharp special case

All graphs below are finite and simple. Write
\[
B(D)=D^2+\left\lfloor\frac D2\right\rfloor^2.
\]
This equals the proposed Erdős–Nešetřil bound, including its odd-degree correction.

An **independent-set blow-up** of a graph \(H\) replaces each vertex \(v\) by a nonempty independent set \(A_v\), and each edge \(uv\) by all edges between \(A_u\) and \(A_v\).

Let \(\mathcal C\) be the class generated from complete graphs and cycles by disjoint unions and **clique-sums without edge deletion**. Explicitly, a clique-sum takes the union of two graphs whose intersection is a complete graph, with no edges between their remaining vertices.

**Theorem.** If \(H\in\mathcal C\), and \(G\) is an independent-set blow-up of \(H\), then
\[
s\chi'(G)\le B(\Delta(G)).
\]
In particular, the conjecture holds for independent-set blow-ups of every outerplanar graph. The bound is sharp within this subclass for every maximum degree.

The blow-up \(G\) itself need not be outerplanar.

I checked and reuse the cycle-elimination calculation from the supplied attempt, reproducing it below. The additional step is a clique-separator gluing lemma. This extends the pseudoforest result to base graphs with arbitrarily many cycles, including cycles joined along edges.

# 2. A simplicial-class deletion lemma

Put
\[
a_v=|A_v|,
\qquad
d_v=\sum_{w\in N_H(v)}a_w.
\]
Every vertex of \(A_v\) has degree \(d_v\). Throughout the proof, \(D\ge1\) is an upper bound on \(\Delta(G)\).

The conflict graph is
\[
J(G)=L(G)^2.
\]
Its vertices are the edges of \(G\), and strong edge-colouring of \(G\) is precisely proper vertex-colouring of \(J(G)\).

For \(uv\in E(H)\), call the set of \(a_ua_v\) edges between \(A_u\) and \(A_v\) a **bundle**. Each bundle is a clique in \(J(G)\). Between two bundles the conflict relation is uniform: either all pairs conflict or none do. Two distinct bundles conflict exactly when their base edges share a vertex or have an edge joining their endpoints.

A vertex \(u\) of \(H\) is **simplicial** if \(N_H(u)\) is a clique.

**Lemma 1.** Suppose \(u\) is simplicial. Every edge in a bundle incident with \(A_u\) has at most \(D^2-1\) neighbours in \(J(G)\).

**Proof.** Take \(v\in N_H(u)\) and \(e\in E(A_u,A_v)\). Since \(u\) is simplicial,
\[
N_H[u]\subseteq N_H[v].
\]
Consequently, every edge in the closed conflict neighbourhood of \(e\) has an endpoint in a class indexed by \(N_H[v]\).

Count first all edges incident with \(A_v\), and then, for each \(x\in N_H(v)\), the edges incident with \(A_x\) but not with \(A_v\). Some edges can be counted twice, which is harmless. Thus
\[
\begin{aligned}
|N_{J(G)}[e]|
&\le a_vd_v+
   \sum_{x\in N_H(v)}a_x(d_x-a_v)\\
&\le a_vd_v+
   \sum_{x\in N_H(v)}a_x(D-a_v)\\
&=Dd_v\\
&\le D^2.
\end{aligned}
\tag{1}
\]
This proves the lemma. \(\square\)

We may therefore delete all bundles incident with a simplicial class, in any order, with at most \(D^2-1\) remaining conflicts at every deletion.

After removing the entire class \(A_u\), the conflict graph on retained edges is exactly \(J(G-A_u)\). Indeed, whether two retained edges conflict depends only on their endpoints and edges joining those endpoints; none of these vertices belongs to \(A_u\).

It follows that if \(H_0\) is obtained from \(H\) by repeatedly deleting simplicial vertices, and \(G_0\) is the corresponding induced blow-up, then
\[
s\chi'(G)\le
\max\{D^2,s\chi'(G_0)\}.
\tag{2}
\]
To see this, colour \(G_0\) first and then colour the deleted edges in reverse deletion order.

The extension also works with lists, provided the retained core has been coloured from the lists and every deleted edge has a list of at least \(D^2\) colours. In particular, complete base graphs admit the stronger bound \(D^2\), even for lists.

# 3. The cycle calculation

We need the following verified part of the previous attempt.

**Lemma 2.** If \(G\) is an independent-set blow-up of a cycle and \(\Delta(G)\le D\), then \(J(G)\) is \((B(D)-1)\)-degenerate.

**Proof.** A triangle is covered by Lemma 1. For a \(4\)-cycle with cyclic part sizes \(a_0,a_1,a_2,a_3\),
\[
|E(G)|=(a_0+a_2)(a_1+a_3)\le D^2,
\]
so the assertion follows immediately.

Now suppose the cycle has length \(n\ge5\), with cyclic part sizes \(a_i\). We have
\[
a_{i-1}+a_{i+1}\le D
\qquad\text{for every }i.
\tag{3}
\]
Let \(E_i\) denote the bundle between \(A_i\) and \(A_{i+1}\).

An edge in \(E_i\) conflicts exactly with edges in the five bundles
\[
E_{i-2},E_{i-1},E_i,E_{i+1},E_{i+2}.
\]
For a selected bundle, abbreviate the six consecutive part sizes as
\[
(r,p,x,y,q,s)
=(a_{i-2},a_{i-1},a_i,a_{i+1},a_{i+2},a_{i+3}).
\]
When \(n=5\), \(r=s\), which causes no difficulty. The constraints we use are
\[
r+x\le D,\quad p+y\le D,\quad
x+q\le D,\quad y+s\le D.
\tag{4}
\]
The original closed conflict neighbourhood has size
\[
S=rp+px+xy+yq+qs
  =p(r+x)+xy+q(y+s).
\tag{5}
\]

Set
\[
k=\left\lfloor\frac D2\right\rfloor.
\]
Call a class large if its size exceeds \(k\), and small otherwise. Delete bundles in three phases, always taking induced subgraphs of the **fixed original conflict graph**. In particular, deleting a bundle does not erase conflicts mediated by its edges.

### Phase I: large–large bundles

For \(x,y\ge k+1\), equations (4)–(5) give
\[
\begin{aligned}
S
&\le D(p+q)+xy\\
&\le D(2D-x-y)+xy\\
&=D^2+(D-x)(D-y)\\
&\le D^2+k^2=B(D).
\end{aligned}
\tag{6}
\]
Here \(0\le D-x,D-y\le k\). Thus all large–large bundles can be deleted.

### Phase II: mixed bundles

Orient the selected bundle so that \(x\ge k+1\) and \(y\le k\).

If \(p\le k\), then even its original closed conflict neighbourhood satisfies
\[
\begin{aligned}
S
&\le D(p+q)+xy\\
&\le D(k+D-x)+xk\\
&=D^2+kD-x(D-k)\\
&\le D^2+k^2.
\end{aligned}
\tag{7}
\]
The last inequality uses \(x\ge k\).

If \(p\ge k+1\), the bundle of size \(px\) was deleted in Phase I. The remaining closed conflict neighbourhood therefore has size at most
\[
\begin{aligned}
rp+xy+yq+qs
&\le p(D-x)+xy+qD\\
&\le(D-x)(2D-y)+xy\\
&=D^2-(2x-D)(D-y)\\
&\le D^2.
\end{aligned}
\tag{8}
\]
The final inequality holds because \(2x\ge D\).

Thus all mixed bundles can also be deleted.

### Phase III: small–small bundles

Every remaining bundle has at most \(k^2\) edges. Each closed conflict neighbourhood meets at most five bundles, so its size is at most
\[
5k^2\le D^2+k^2=B(D).
\tag{9}
\]

Every individual edge deletion consequently has at most \(B(D)-1\) remaining neighbours. This proves the degeneracy assertion. \(\square\)

In particular, cycle blow-ups have strong chromatic index at most \(B(D)\), also for lists of size \(B(D)\).

# 4. Gluing across a clique in the base graph

The following lemma is the main extension.

**Lemma 3 — clique gluing.** Suppose
\[
H=H_1\cup H_2,
\qquad V(H_1)\cap V(H_2)=S,
\]
where \(S\) is a clique, both \(H_i\) are induced subgraphs of \(H\), and there are no edges between \(V(H_1)\setminus S\) and \(V(H_2)\setminus S\).

Let \(G\) be an independent-set blow-up of \(H\), with \(\Delta(G)\le D\), and let \(G_i\) be the induced blow-up of \(H_i\). Then
\[
\boxed{\quad
s\chi'(G)\le
\max\{D^2,s\chi'(G_1),s\chi'(G_2)\}.
\quad}
\tag{10}
\]

**Proof.** Let
\[
Q=\left\{e\in E(G):
e\text{ has an endpoint in }\bigcup_{v\in S}A_v\right\}.
\]
This is a clique in \(J(G)\).

Indeed, edges touching different classes indexed by \(S\) conflict because those base vertices are adjacent. Edges touching the same class also conflict, by the complete-bundle structure. This remains true when \(S\) consists of one vertex.

For each \(i\), construct a padded base graph \(H_i^+\) as follows:

* retain \(H_i\);
* for every vertex \(w\notin V(H_i)\) having a neighbour in \(S\), add \(w\) with its original weight \(a_w\);
* give this added vertex precisely its original neighbours in \(S\);
* put no edges between added vertices.

Let \(G_i^+\) be its blow-up.

Every added vertex of \(H_i^+\) is simplicial, because its neighbourhood is a subset of the clique \(S\). Moreover,
\[
\Delta(G_i^+)\le D:
\]
old classes have no more neighbours than in \(G\), and an added class retains only some of its original neighbours. Applying (2) gives
\[
s\chi'(G_i^+)
\le\max\{D^2,s\chi'(G_i)\}.
\tag{11}
\]

We next check precisely how these padded graphs represent conflicts in \(G\). Their edge sets identify naturally as
\[
E(G_i^+)=E(G_i)\cup Q.
\tag{12}
\]
Furthermore,
\[
J(G_i^+)=J(G)[E(G_i)\cup Q].
\tag{13}
\]

For (13), the only potentially relevant original edges omitted from \(G_i^+\) are edges between two added classes. If such an omitted edge witnesses a conflict between two retained edges, both retained edges touch classes indexed by \(S\). They therefore belong to \(Q\), and already conflict in \(G_i^+\). Thus no conflict is lost.

The two induced conflict graphs in (13) intersect exactly in \(Q\). There are no conflicts between
\[
E(G_1)\setminus Q
\quad\text{and}\quad
E(G_2)\setminus Q,
\]
because their endpoints lie on opposite sides of the separator and no edge joins those sides.

Set
\[
K=\max\{D^2,s\chi'(G_1),s\chi'(G_2)\}.
\]
By (11), each padded conflict graph has a proper colouring from the palette \(\{1,\ldots,K\}\). Since \(Q\) is a clique, its colours are distinct in either colouring. A permutation of the palette in the second colouring makes the two colourings agree on every vertex of \(Q\). They then combine into a proper colouring of \(J(G)\).

This proves (10). \(\square\)

The palette permutation is essential to this proof. It is not legitimate for arbitrary edge lists, so Lemma 3 is an ordinary-colouring assertion.

# 5. Completing the special-case theorem

Fix \(D\ge1\), and consider blow-ups of maximum degree at most \(D\).

* Complete base graphs satisfy the stronger bound \(D^2\), by Lemma 1.
* Cycle base graphs satisfy \(B(D)\), by Lemma 2.
* Disjoint unions preserve the bound by reusing the palette.
* Clique-sums preserve the bound by Lemma 3, since \(D^2\le B(D)\).

Induction on a construction of \(H\in\mathcal C\) proves
\[
s\chi'(G)\le B(D).
\]
Taking \(D=\Delta(G)\) proves the theorem. The edgeless case is immediate.

## Why this includes all outerplanar base graphs

Here is a direct decomposition argument.

A disconnected outerplanar graph splits into components. A connected graph with a cut vertex splits as a clique-sum over that single vertex. Single-edge pieces are complete graphs.

It remains to consider a \(2\)-connected outerplanar graph. In an outerplanar embedding, its outer boundary is a cycle containing every vertex. If there is no chord, the graph is a cycle. Otherwise, a chord \(uv\) divides the outer cycle into two arcs. No edge joins the interiors of the two arcs, since such an edge would cross the chord. Hence the graph is a clique-sum of two smaller outerplanar graphs over the edge \(uv\).

Induction therefore places every outerplanar graph in \(\mathcal C\).

## Sharpness

Every two edges in a blow-up of \(C_5\) conflict, so its strong chromatic index equals its number of edges.

For \(D=2k\), take all five part sizes equal to \(k\). Then
\[
s\chi'(G)=5k^2=B(D).
\]

For \(D=2k+1\), \(k\ge1\), take cyclic part sizes
\[
(k+1,k+1,k,k,k).
\]
The maximum degree is \(2k+1\), and
\[
\begin{aligned}
s\chi'(G)
&=(k+1)^2+2k(k+1)+2k^2\\
&=5k^2+4k+1\\
&=(2k+1)^2+k^2\\
&=B(D).
\end{aligned}
\]
A single edge gives equality for \(D=1\). Thus the special-case theorem cannot be improved uniformly.

# 6. Consequence for counterexamples, and the remaining gap

Lemma 3 also gives a structural consequence for the original problem:

**Corollary.** A vertex-minimal counterexample to the Erdős–Nešetřil conjecture has no clique cutset.

To prove this, take \(H=G\) with all part sizes equal to \(1\). A clique cutset splits \(G\) into two proper induced subgraphs. By minimality, both satisfy the conjecture. Since \(B\) is nondecreasing and \(D^2\le B(D)\), equation (10) then gives the conjectured bound for \(G\), a contradiction.

This does not settle the conjecture: clique-cutset-free graphs need not be cycles or complete graphs. The method provides no adequate colouring theorem for those general pieces.

There is also a genuine limitation to extending the elimination calculation. If \(G\) is \(D\)-regular of girth at least five, every vertex of \(L(G)^2\) has degree
\[
2(D-1)+2(D-1)^2=2D(D-1).
\]
For \(D\ge3\),
\[
2D(D-1)>B(D)-1.
\]
Thus the general conjecture cannot be proved simply by establishing the same \((B(D)-1)\)-degeneracy conclusion used for cycle blow-ups. For example, the Petersen graph has a \(12\)-regular conflict graph, whereas \(B(3)-1=9\).

So the outcome is a proved, sharp subclass theorem and a clique-separator gluing principle—not a proof or disproof for arbitrary graphs. No novelty claim is made for these partial results.