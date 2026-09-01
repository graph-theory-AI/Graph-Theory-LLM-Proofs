```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it reduces quantitatively to prime graphs and holds with a constant bound for line graphs and proper subdivisions.",
  "would_publish": false,
  "caveats": "The arbitrary prime case, where chords destroy a wall model, remains unresolved; standard small-parameter conventions are assumed."
}
```

# Mathematical writeup

## 1. Setup and status

Write \(W_t=W_{t\times t}\), and let \(\mathcal C_t\) denote the hereditary class in the conjecture. All graphs below are finite and simple. To avoid irrelevant exceptional cases, put
\[
\ell(n)=\log_2\max\{2,n\}.
\]

I do not prove or disprove Conjecture 1.10. I prove the following partial results.

1. It is enough to prove the conjecture for **prime graphs with respect to modular decomposition**. This reduction is quantitative.
2. Consequently, the conjecture holds for graphs whose prime modular quotients satisfy the three-path-configuration theorem from the source paper.
3. On line graphs, and on proper subdivisions of arbitrary graphs, the conjectured logarithmic bound can be strengthened to a constant depending only on \(t\).
4. The first two forbidden configurations imply an ordinary biclique exclusion and hence a hereditary extremal edge bound, though this alone does not control treewidth.

The modular-decomposition reduction appears to be the most useful of these observations: substitution cannot hide a counterexample.

---

## 2. Ramsey consequences of excluding \(K_t\) and induced \(K_{t,t}\)

Let
\[
r=R(t,t)
\]
be the diagonal Ramsey number.

### Lemma 2.1

If \(G\) has no \(K_t\) and no induced \(K_{t,t}\), then \(G\) contains no ordinary, not necessarily induced, \(K_{r,r}\).

#### Proof

Suppose \(A,B\) are the shores of a \(K_{r,r}\) subgraph. Since \(G[A]\) has no \(K_t\), Ramsey's theorem gives an independent set \(A'\subseteq A\) of size \(t\). Similarly, \(G[B]\) contains an independent set \(B'\) of size \(t\). Every vertex of \(A'\) is adjacent to every vertex of \(B'\), so \(G[A'\cup B']\cong K_{t,t}\), a contradiction. ∎

Thus every \(m\)-vertex induced subgraph \(H\) of \(G\) satisfies
\[
|E(H)|=O_t\!\left(m^{2-1/r}\right).
\]
Indeed, the usual counting proof of the Kővári–Sós–Turán bound begins with
\[
\sum_{v\in V(H)}\binom{d_H(v)}r
   \le (r-1)\binom mr,
\]
because an \(r\)-set has at most \(r-1\) common neighbors.

This hereditary sparsity is not enough by itself: bounded-degree expander families exclude large ordinary bicliques and have linear treewidth. The two wall exclusions remain essential.

---

## 3. A quantitative reduction to prime graphs

A set \(M\subseteq V(G)\) is a **module** if every vertex outside \(M\) is either complete or anticomplete to \(M\). Given a partition
\[
V(H)=M_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}M_q
\]
into modules, its quotient \(Q\) has vertices \(1,\dots,q\), with \(ij\in E(Q)\) precisely when \(M_i\) is complete to \(M_j\).

A graph is **prime** if its only modules are the trivial ones. The standard modular decomposition expresses every graph recursively using quotients that are complete, edgeless, or prime.

### Lemma 3.1: boundaries of large modules are bounded

Let \(H\) have no \(K_t\) and no induced \(K_{t,t}\), and let \(M\) be a module of \(H\). If \(|M|\ge r\), then
\[
|N_H(M)|<r.
\]

#### Proof

Since \(H[M]\) is \(K_t\)-free and \(|M|\ge r\), it contains an independent set \(A\) of size \(t\).

Every vertex in \(N_H(M)\) is complete to \(M\), by the module property. If \(|N_H(M)|\ge r\), then \(H[N_H(M)]\), being \(K_t\)-free, contains an independent set \(B\) of size \(t\). Then \(H[A\cup B]\cong K_{t,t}\), a contradiction. ∎

In particular, two disjoint modules of size at least \(r\) cannot be complete to one another.

### Lemma 3.2: lifting a quotient decomposition

Let \(M_1,\ldots,M_q\) be a modular partition of \(H\), with quotient \(Q\). Call \(M_i\) **large** if \(|M_i|\ge r\), and let
\[
B_i=N_H(M_i)
\]
for each large \(M_i\). Then
\[
\operatorname{tw}(H)
 \le
 \max\left\{
   (r-1)(\operatorname{tw}(Q)+1)-1,\,
   \max_{M_i\text{ large}}
       \bigl(\operatorname{tw}(H[M_i])+r-1\bigr)
 \right\}.
\tag{3.1}
\]

#### Proof

By Lemma 3.1, \(|B_i|\le r-1\), and no two large modules are adjacent in \(Q\). Hence every \(B_i\) is contained in the union \(C\) of the small modules.

Let \((T,\{X_x:x\in V(T)\})\) be a tree decomposition of \(Q\) of width \(k\). For each \(x\in V(T)\), define
\[
Y_x=
 \bigcup_{\substack{j\in X_x\\ M_j\text{ small}}}M_j
 \ \cup\
 \bigcup_{\substack{i\in X_x\\ M_i\text{ large}}}B_i.
\]
Each summand has at most \(r-1\) vertices, so
\[
|Y_x|\le (r-1)|X_x|\le (r-1)(k+1).
\tag{3.2}
\]

These bags form a tree decomposition of \(H[C]\) after adding all missing edges inside every \(B_i\):

- An edge inside a small module \(M_j\) is covered by every bag corresponding to a quotient bag containing \(j\).
- An edge between two small modules is covered by a quotient bag containing the corresponding adjacent quotient vertices.
- Each \(B_i\) occurs together in every bag corresponding to a quotient bag containing \(i\).
- For \(z\in M_j\), its bags are the quotient subtree for \(j\), together with the quotient subtrees for large neighbors \(i\) of \(j\). Each such latter subtree intersects the subtree for \(j\), so the total set of bags containing \(z\) is connected.

For each large module \(M_i\), take a tree decomposition of \(H[M_i]\) and add all of \(B_i\) to every bag. Its width is at most
\[
\operatorname{tw}(H[M_i])+|B_i|
 \le \operatorname{tw}(H[M_i])+r-1.
\]
Attach this decomposition to any core bag corresponding to a quotient bag containing \(i\); that core bag contains \(B_i\). This covers all edges between \(M_i\) and \(B_i\). There are no edges between two large modules.

Combining these decompositions gives (3.1). ∎

### Theorem 3.3: prime reduction

Let \(\mathcal C\) be a hereditary class with no \(K_t\) and no induced \(K_{t,t}\). Suppose \(f\) is nondecreasing and every prime \(q\)-vertex graph \(Q\in\mathcal C\) satisfies
\[
\operatorname{tw}(Q)\le f(q).
\]
Then every \(n\)-vertex \(G\in\mathcal C\) satisfies
\[
\boxed{
\operatorname{tw}(G)
 \le
 (r-1)\bigl(\max\{f(n),t-2\}+t\bigr)-1.
}
\tag{3.3}
\]

#### Proof

Use the canonical modular decomposition.

At an edgeless quotient node, the graph is a disjoint union of its child modules, so treewidth is the maximum of the child treewidths; there is no additive loss.

At a complete quotient node, choosing one representative from each child gives a clique in \(G\). Thus the quotient has at most \(t-1\) vertices and treewidth at most \(t-2\).

At a prime quotient node \(Q\), choosing one representative from each module realizes \(Q\) as an induced subgraph of \(G\). Hence \(Q\in\mathcal C\), and
\[
\operatorname{tw}(Q)\le f(|V(Q)|)\le f(n).
\]

It remains to bound how often the second term of (3.1) can be followed down a chain of large modules. Consider such a chain through non-edgeless quotient nodes:
\[
M^0\supsetneq M^1\supsetneq\cdots\supsetneq M^d,
\]
where \(M^{j+1}\) is a large child module of \(M^j\). At a complete or prime quotient node, the child \(M^{j+1}\) has a nonempty external neighborhood inside \(M^j\). Choose
\[
x_j\in N_{G[M^j]}(M^{j+1}).
\]
Because \(M^{j+1}\) is a module, \(x_j\) is complete to \(M^{j+1}\). For \(i<j\), the vertex \(x_j\) lies inside \(M^{i+1}\), so \(x_i x_j\in E(G)\). Hence
\[
\{x_0,\dots,x_{d-1}\}
\]
is a clique. Since \(G\) is \(K_t\)-free,
\[
d\le t-1.
\tag{3.4}
\]

Repeatedly applying (3.1), every passage into a large child costs at most \(r-1\). A local quotient contributes at most
\[
(r-1)\bigl(\max\{f(n),t-2\}+1\bigr)-1,
\]
and by (3.4) at most \(t-1\) further terms of \(r-1\) can be accumulated. This yields (3.3). ∎

### Corollary 3.4

For each fixed \(t\), Conjecture 1.10 is equivalent to its restriction to prime graphs.

Indeed, the forward implication is immediate. Conversely, if every prime \(Q\in\mathcal C_t\) satisfies
\[
\operatorname{tw}(Q)\le a_t\ell(|V(Q)|),
\]
then Theorem 3.3 gives, for \(n\ge2\),
\[
\operatorname{tw}(G)
 \le
 (r-1)(a_t+2t-2)\ell(n).
\]

Thus a counterexample sequence, if one exists, can be sought among prime graphs.

As a simple further consequence, if the modular decomposition has no prime nodes—equivalently, the graph is built only by disjoint unions and complete joins—then the first two exclusions already imply the constant bound
\[
\operatorname{tw}(G)\le (r-1)(2t-2)-1.
\]

---

## 4. Consequences of the source paper's three-path theorem

Let \(\tau_{\mathrm{3PC}}(G)\) be the minimum size of a set \(X\) such that \(G-X\) has no induced theta, prism, or pyramid.

The main theorem of the supplied source paper gives a constant \(a_t\) such that every \(K_t\)-free, three-path-configuration-free graph \(H\) satisfies
\[
\operatorname{tw}(H)\le a_t\ell(|V(H)|).
\]

Therefore every \(K_t\)-free graph \(G\) satisfies
\[
\boxed{
\operatorname{tw}(G)
 \le
 \tau_{\mathrm{3PC}}(G)+a_t\ell(|V(G)|).
}
\tag{4.1}
\]

Indeed, take an optimal deletion set \(X\), apply the source theorem to \(G-X\), and add \(X\) to every bag of a tree decomposition of \(G-X\).

Consequently:

- Conjecture 1.10 holds for members of \(\mathcal C_t\) satisfying
  \[
  \tau_{\mathrm{3PC}}(G)=O_t(\log |V(G)|).
  \]
- More generally, by Theorem 3.3 it is enough that every prime quotient \(Q\) in the modular decomposition satisfies
  \[
  \tau_{\mathrm{3PC}}(Q)=O_t(\log |V(Q)|).
  \]
- In particular, the conjecture holds when all prime modular quotients are three-path-configuration-free.

What is missing is any deduction of such a transversal bound from the four forbidden induced families.

---

## 5. Constant bounds for line graphs and proper subdivisions

The next two propositions verify the conjecture, in stronger constant form, on two natural ambient classes.

Let \(g_t\) be a constant such that every graph with no \(W_t\) minor has treewidth at most \(g_t\). Such a finite \(g_t\) exists because \(W_t\) is planar, by the excluded-grid theorem.

We also use the standard fact:

> If a graph \(F\) has maximum degree at most three and \(F\) is a minor of \(H\), then \(H\) contains a subdivision of \(F\) as a subgraph.

For completeness, take a minor model of \(F\). In each branch set, at most three attachment vertices have to be connected. A minimal tree connecting them is a subdivided star with at most one branch vertex. Taking these trees together with the inter-branch-set edges gives a topological model of \(F\).

Walls are subcubic, so this applies to \(W_t\).

### Proposition 5.1: line graphs

Suppose \(G=L(H)\) belongs to \(\mathcal C_t\). Then
\[
\operatorname{tw}(G)
 \le
 (t-1)(g_t+1)-1.
\]

#### Proof

If \(H\) contained \(W_t\) as a minor, it would contain a subdivision \(S\) of \(W_t\) as a subgraph. For the corresponding edge set,
\[
L(H)[E(S)]\cong L(S).
\]
This is an induced subgraph identity: two selected edges are adjacent in \(L(H)\) exactly when they share an endpoint, which is also their adjacency relation in \(L(S)\). This contradicts the exclusion of induced line graphs of subdivisions of \(W_t\). Hence
\[
\operatorname{tw}(H)\le g_t.
\]

Furthermore, all edges incident with a fixed vertex of \(H\) form a clique in \(L(H)\). Since \(G\) has no \(K_t\),
\[
\Delta(H)\le t-1.
\]

Take a tree decomposition \((T,\{B_x\})\) of \(H\) of width at most \(g_t\), and replace each bag by
\[
B'_x=\{e\in E(H): e\text{ has an endpoint in }B_x\}.
\]
Then
\[
|B'_x|\le (t-1)|B_x|\le (t-1)(g_t+1).
\]

This is a tree decomposition of \(L(H)\). For an edge \(uv\in E(H)\), its occurrence set is the union of the occurrence subtrees of \(u\) and \(v\), which intersect because some original bag contains both \(u\) and \(v\). Two adjacent vertices of \(L(H)\), corresponding to two edges sharing a vertex \(w\), occur together in every bag containing \(w\). The asserted bound follows. ∎

The direct wall and biclique exclusions are not needed in this special case.

### Proposition 5.2: proper subdivisions

Suppose \(G\) is a proper subdivision of a graph \(H\), meaning that every edge of \(H\) is replaced by a path of length at least two. If \(G\) has no induced subdivision of \(W_t\), then
\[
\operatorname{tw}(G)\le \max\{g_t,2\}.
\]

#### Proof

Suppose \(H\) contained \(W_t\) as a minor. Since \(W_t\) is subcubic, \(H\) would contain a subdivision \(S\) of \(W_t\) as a subgraph.

For every edge of \(S\), include in \(G\) the whole replacement path corresponding to that edge. Let \(X\) be the union of their vertex sets. Then \(G[X]\) is an induced subdivision of \(W_t\). Indeed, an edge of \(H\) not used by \(S\) has a replacement path with at least one internal vertex, none of which lies in \(X\). Thus such an unused edge creates no chord in \(G[X]\). This contradicts the hypothesis. Therefore \(H\) is \(W_t\)-minor-free and
\[
\operatorname{tw}(H)\le g_t.
\]

Finally, subdivision does not increase treewidth above two. More precisely,
\[
\operatorname{tw}(G)\le \max\{\operatorname{tw}(H),2\}.
\]
To see this, retain a tree decomposition of \(H\). If \(uv\) is replaced by
\[
u=x_0,x_1,\ldots,x_\ell=v,
\]
attach to a bag containing \(u,v\) a path of bags of size at most three,
\[
\{u,x_{\ell-1},v\},\ 
\{u,x_{\ell-2},x_{\ell-1}\},\ldots,
\{u,x_1,x_2\}.
\]
This covers the replacement path and preserves connected occurrence sets. ∎

The adjective “proper” is essential for this argument: an unsubdivided unused edge may be a chord of the selected wall model.

---

## 6. The unresolved core

The excluded-grid theorem gives a subdivision of \(W_t\) as a subgraph once treewidth is sufficiently large, because \(W_t\) is subcubic. In an arbitrary graph, however, the vertex set of that subdivision may have many chords. Those chords can destroy the induced wall.

The two constant-bound special cases work precisely because they neutralize this issue:

- in a line graph, selecting the edges of a root subgraph automatically gives an induced line graph;
- in a proper subdivision, every unused root edge has an omitted internal vertex and therefore cannot become a chord.

For an arbitrary prime graph, neither mechanism is available. One would need to prove that the chords of a sufficiently large wall model either:

1. can be avoided while retaining a \(W_t\)-subdivision;
2. organize into an induced line graph of a wall subdivision;
3. produce an induced \(K_t\) or \(K_{t,t}\); or
4. force the graph to have exponentially many vertices relative to its treewidth.

Establishing the last alternative quantitatively would give the desired \(O_t(\log n)\) bound. No such argument is supplied here.

A sufficient, but currently unproved, structural statement would be that every member of \(\mathcal C_t\) has a balanced separator of bounded size depending only on \(t\). Since the class is hereditary, recursive use of such separators would give treewidth \(O_t(\log n)\). The main gap is obtaining such separators in arbitrary prime members of \(\mathcal C_t\).

---

## 7. Small parameters

Under standard conventions:

- For \(t=2\), exclusion of \(K_2\) makes \(G\) edgeless, so the conjecture is trivial.
- For \(t=1\), there is no nonempty admissible graph.
- The literal \(t=0\) formulation depends on conventions for \(K_0\), \(W_{0\times0}\), and \(\log 0\); the substantive conjecture is for positive integral \(t\), in practice \(t\ge3\).

Thus these convention issues do not affect the unresolved case.