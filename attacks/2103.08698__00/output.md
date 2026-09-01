```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Fixed subdivisions of cliques disprove the literal memberwise formulation, but they are excluded by the intended hereditary/all-subgraphs formulation, for which only special cases are proved here.",
  "would_publish": false,
  "caveats": "The precise meaning of 'class with sublinear separators' is decisive; the robust hereditary conjecture remains unresolved."
}
```

# 1. Statement and the necessary convention

For \(0<\varepsilon<1\), call a probability distribution \(\mu\) on subsets \(X\subseteq V(G)\) an \((\varepsilon,t)\)-distribution if

\[
\operatorname{tw}(G-X)\le t
\quad\text{for every }X\in\operatorname{supp}(\mu),
\]

and

\[
\Pr_{\mu}(v\in X)\le \varepsilon
\quad\text{for every }v\in V(G).
\]

A class is fractionally treewidth-fragile if for every \(\varepsilon>0\) there is a common \(t=t(\varepsilon)\) such that every graph in the class has such a distribution.

There are two materially different meanings of “a class with sublinear separators.”

1. **Memberwise meaning:** every \(n\)-vertex member of the class has a balanced separator of size \(o(n)\).
2. **Robust meaning:** every induced subgraph, or every subgraph, of every class member has a balanced separator of size \(o(h)\), where \(h\) is the order of that subgraph. Equivalently, one often assumes that the class is hereditary and has memberwise sublinear separators.

The conjecture is false under the first meaning. The catalog context strongly suggests that the intended conjecture uses the second meaning or assumes heredity. I do not resolve that intended version.

# 2. A connected counterexample to the literal memberwise statement

For fixed \(L\ge 1\), let \(Q_m^L\) be obtained from \(K_m\) by replacing every edge by a path with exactly \(L\) internal vertices. Let \(B_m\) denote the \(m\) original, or branch, vertices. Thus

\[
|V(Q_m^L)|=m+L\binom m2.
\]

## 2.1 Memberwise separators are strongly sublinear

Deleting \(B_m\) leaves \(\binom m2\) disjoint paths, each with \(L\) vertices. Hence \(B_m\) is a balanced separator for all sufficiently large \(m\), and

\[
|B_m|=m=O_L\!\left(\sqrt{|V(Q_m^L)|}\right).
\]

Consequently, the non-hereditary class

\[
\mathcal Q_L=\{Q_m^L:m\ge 3\}
\]

has memberwise strongly sublinear separators.

This remains true under the slightly stronger host-normalized convention in which one considers the largest separator needed by a subgraph of \(Q_m^L\), but normalizes by \(|V(Q_m^L)|\): since \(\operatorname{tw}(Q_m^L)=m-1\), every subgraph has a balanced separator of order at most \(m\).

## 2.2 Nevertheless \(\mathcal Q_L\) is not fractionally treewidth-fragile

For a graph \(G\), put

\[
\lambda_t(G)=
\min_{\mu}
\max_{v\in V(G)}\Pr_{\mu}(v\in X),
\]

where the minimum is over distributions supported on sets \(X\) satisfying
\(\operatorname{tw}(G-X)\le t\).

Define

\[
\phi_L=\frac{L+2-\sqrt{L^2+4L}}{2};
\]

this is the smaller root of

\[
Lp=(1-p)^2.
\]

### Proposition

For every fixed \(L\ge1\) and \(t\ge1\),

\[
\lim_{m\to\infty}\lambda_t(Q_m^L)=\phi_L>0.
\]

In particular, \(\mathcal Q_L\) is not fractionally treewidth-fragile.

### Lower bound

Let \(\mu\) be supported on sets \(X\) with
\(\operatorname{tw}(Q_m^L-X)\le t\), and suppose every vertex is deleted with probability at most \(p\).

For a realization \(X\), let \(r\) be the number of undeleted branch vertices. Form a graph \(F_X\) on those \(r\) vertices by retaining \(ij\) precisely when no internal vertex on the subdivided \(ij\)-path was deleted. Then \(F_X\) is a minor of \(Q_m^L-X\), and hence

\[
\operatorname{tw}(F_X)\le t.
\]

A graph of treewidth at most \(t\) has at most \(t|V|\) edges, so \(F_X\) has at most \(tm\) edges.

Let \(Y_X\) be the number of deleted internal vertices. Every pair of surviving branch vertices which is not an edge of \(F_X\) accounts for at least one deleted internal vertex, and distinct pairs have internally disjoint paths. Therefore

\[
\binom r2\le tm+Y_X.
\]

Taking expectations gives

\[
\mathbb E\binom r2
   \le tm+\mathbb E Y_X
   \le tm+pL\binom m2.
\]

Moreover, \(\mathbb E r\ge (1-p)m\), and \(x\mapsto \binom x2\) is convex. Thus, for large \(m\),

\[
\binom{(1-p)m}{2}
   \le tm+pL\binom m2.
\]

After division by \(\binom m2\) and passage to the limit,

\[
(1-p)^2\le Lp.
\]

Hence \(p\ge\phi_L-o(1)\).

### Matching upper bound

Choose uniformly a set \(D\subseteq B_m\) of \(d\) branch vertices. Delete \(D\). For every pair \(i,j\notin D\), delete one uniformly chosen internal vertex of the subdivided \(ij\)-path.

The remaining graph is a forest: no two surviving branch vertices remain connected, and all surviving path pieces are pendant paths or isolated paths. A branch vertex is deleted with probability \(d/m\), while each internal vertex is deleted with probability

\[
\frac1L\frac{(m-d)(m-d-1)}{m(m-1)}.
\]

Taking \(d/m\to\alpha\), the maximum marginal tends to

\[
\max\left\{\alpha,\frac{(1-\alpha)^2}{L}\right\}.
\]

This is minimized when \(L\alpha=(1-\alpha)^2\), namely at
\(\alpha=\phi_L\). This proves the proposition.

For \(L=1\),

\[
\phi_1=\frac{3-\sqrt5}{2}\approx0.381966.
\]

Thus even allowing any fixed residual treewidth, some vertex must be deleted with probability asymptotically at least \(0.3819\).

# 3. Why this does not refute the intended hereditary conjecture

Let \(\overline{\mathcal Q_L}\) be the hereditary closure of \(\mathcal Q_L\). This class does not have robust sublinear separators.

Indeed, take a family \(F_b\) of cubic edge-expanders. The graph obtained by \(L\)-subdividing every edge of \(F_b\) occurs as an induced subgraph of \(Q_m^L\) for \(m\ge b\): retain the branch vertices corresponding to \(V(F_b)\), and retain the internal vertices precisely on paths corresponding to \(E(F_b)\).

For fixed \(L\), bounded subdivision preserves linear separator lower bounds. To see this, suppose \(S\) is a set of \(o(b)\) vertices in the \(L\)-subdivision of \(F_b\). In \(F_b\), remove:

- all branch vertices belonging to \(S\), and
- both endpoints of every original edge whose subdivided path meets \(S\).

This removes \(o(b)\) original vertices. Expansion implies that the remaining original graph has a component on \(b-o(b)\) vertices. Since \(F_b\) is cubic, its corresponding component in the subdivided graph contains all but \(o(b)\) vertices of the subdivision. It is therefore larger than two thirds of the graph. Thus a balanced separator has order \(\Omega(b)\), which is linear in the order of the fixed-length subdivision.

Hence the fixed-subdivision counterexample is inadmissible under either:

- an explicit hereditary assumption, or
- a separator condition quantified over all induced subgraphs/subgraphs relative to their own order.

# 4. Exact behavior of the obvious hereditary subdivision test family

The preceding obstruction has a clean positive counterpart.

Let \(m_i\to\infty\), let \(L_i\ge1\), and let \(G_i=Q_{m_i}^{L_i}\). Let \(\mathcal H\) be the hereditary closure of \(\{G_i:i\ge1\}\).

## Theorem

The following hold.

1. \(\mathcal H\) has robust sublinear separators if and only if \(L_i\to\infty\).
2. If \(L_i\to\infty\), then \(\mathcal H\) is fractionally treewidth-fragile; in fact, outside finitely many host graphs, an arbitrarily thin deletion distribution leaves a forest.

## Proof of the separator assertion when \(L_i\to\infty\)

Let \(H\) be an induced subgraph of \(Q_m^L\), and write \(n=|V(H)|\). Call an original edge-path *complete in \(H\)* if both branch endpoints and all \(L\) internal vertices belong to \(H\). Let \(e\) be the number of complete paths, and let \(U\) be the set of their branch endpoints. Since the internal vertices of distinct paths are disjoint,

\[
e\le \frac nL,
\qquad
|U|\le 2e\le \frac{2n}{L}.
\]

The graph \(H-U\) is a forest. Indeed, distinct subdivided edge-paths meet only at branch vertices, and every connection between two surviving branch vertices would have been a complete path.

A forest has a balanced separator of order at most one: if one component has more than half the vertices, take a centroid of that tree; otherwise take the empty set. Consequently \(H\) has a balanced separator of order at most

\[
\frac{2n}{L}+1.
\]

If \(L_i\to\infty\), this bound is \(o(n)\) uniformly, apart from finitely many finite host graphs.

Conversely, if \(L_i\not\to\infty\), an infinite subsequence has a common bounded subdivision length. The expander construction from Section 3 then gives induced subgraphs with linear balanced separators.

## Proof of fractional treewidth-fragility

Fix \(\varepsilon>0\). For all sufficiently large \(i\),

\[
L_i\ge \frac1\varepsilon.
\]

Let \(H\) be an induced subgraph of such a \(G_i\). For every original edge-path complete in \(H\), independently choose one of its \(L_i\) internal vertices uniformly and delete it. Branch vertices are never deleted, and every internal vertex is deleted with probability either zero or

\[
\frac1{L_i}\le\varepsilon.
\]

As above, the residual graph is a forest, so it has treewidth at most one.

Only finitely many \(G_i\) fail \(L_i\ge1/\varepsilon\). Their hereditary closures have uniformly bounded treewidth, so increasing \(t(\varepsilon)\) handles all of them. This proves the theorem.

Thus the simplest attempted high-degree counterexamples—subdivided dense cores—obey the conjecture exactly when their hereditary closures acquire sublinear separators.

# 5. A further special case without a degree bound

Here is another genuine special case of the intended robust conjecture.

## Proposition

Suppose constants \(c>0\), \(\delta>0\), and \(\alpha>0\) satisfy:

1. every induced subgraph \(H\) of every \(G\in\mathcal C\) has a balanced separator of size at most
   \[
   c|V(H)|^{1-\delta};
   \]
2. every orbit of \(\operatorname{Aut}(G)\) has size at least
   \(\alpha |V(G)|\).

Then \(\mathcal C\) is fractionally component-fragile, and hence fractionally treewidth-fragile. In particular, this holds for vertex-transitive classes with robust strongly sublinear separators.

### Proof

Recursively remove balanced separators until every component has at most \(k\) vertices. If \(X\) is the union of the removed separators, a standard charging argument gives

\[
|X|
\le
\frac{c}{1-(2/3)^\delta}\,|V(G)|\,k^{-\delta}.
\]

Indeed, at a recursive node on \(h\) vertices, charge \(ch^{-\delta}\) to each of its vertices. This pays for its separator. Along any root-to-leaf recursion chain, node sizes decrease by a factor at most \(2/3\), so the total charge to one vertex is at most

\[
\frac{c k^{-\delta}}{1-(2/3)^\delta}.
\]

Choose \(k\) so that \(|X|\le\alpha\varepsilon |V(G)|\). Now choose a uniformly random automorphism \(\sigma\) of \(G\) and delete \(\sigma(X)\). For a vertex \(v\) in an automorphism orbit \(O\),

\[
\Pr(v\in\sigma(X))
=
\frac{|X\cap O|}{|O|}
\le
\frac{|X|}{\alpha |V(G)|}
\le\varepsilon.
\]

Every component of \(G-\sigma(X)\) has at most \(k\) vertices, so its treewidth is at most \(k-1\).

# 6. The remaining weighted gap

For fixed \(t\), finite minimax gives the exact identity

\[
\lambda_t(G)
=
\max_{\substack{w:V(G)\to\mathbb R_{\ge0}\\w(V(G))=1}}
\;
\min_{\operatorname{tw}(G-X)\le t} w(X).
\]

Thus fractional treewidth-fragility is equivalent to the following weighted statement:

> For every \(\varepsilon>0\), there is \(t\) such that, for every graph \(G\) in the class and every nonnegative vertex weighting \(w\), one can delete weight at most \(\varepsilon w(V(G))\) and leave treewidth at most \(t\).

Ordinary separator hypotheses are unweighted. Recursive separator arguments can control the total number of deleted vertices, especially under a strongly sublinear power bound, but do not control deletion cost for arbitrary weights. High-degree vertices or small automorphism orbits can carry essentially all the relevant weight. The bounded-degree theorem and the symmetry proposition overcome this in different ways; no argument above handles arbitrary weights in a general hereditary class.

Accordingly:

- the statement as literally written, without a hereditary/all-subgraphs convention, is false;
- the intended hereditary or robust-separator conjecture is not proved or disproved here;
- fixed and growing subdivisions of dense graphs are completely understood and do not yield a robust counterexample.