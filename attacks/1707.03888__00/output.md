```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There are uniform additive bounds for substantial subclasses, while exact coloring is NP-hard even for triangle-free K13-minor-free graphs, but neither argument settles additive error at least one in all proper minor-closed classes.",
  "would_publish": false,
  "caveats": "The general case remains open; the lower bound assumes P != NP and uses the source paper's one-sided coloring notion."
}
```

# 1. Formulation

All graphs are finite and simple. I interpret “additive approximation” in the constructive, one-sided sense used in the source paper:

> For a fixed proper minor-closed class \(\mathcal C\), the algorithm receives a triangle-free \(G\in\mathcal C\) and returns a proper coloring using at most
> \[
> \chi(G)+\alpha
> \]
> colors. The algorithm may depend on \(\mathcal C\), but \(\alpha\) must not.

Under this interpretation, an error \(\alpha<1\) is exact, since the number of colors is integral.

I obtain:

1. a uniform additive \(2\)-approximation for triangle-free graphs on every fixed surface;
2. a uniform additive \(3\)-approximation for every class of graphs having bounded vertex-planarization number;
3. the same \(+3\) bound under certain clique-sum constructions;
4. unless \(P=NP\), no universal \(\alpha<1\) is possible: in fact, deciding whether a triangle-free \(K_{13}\)-minor-free graph has chromatic number \(3\) or \(4\) is NP-hard.

The fourth result also explains why a natural triangle-elimination gadget does not yield hardness for larger additive errors: every produced graph is automatically \(4\)-colorable.

# 2. A core-stripping lemma

For a graph \(G\), let \(K_5(G)\) denote its \(5\)-core, obtained by repeatedly deleting vertices of current degree at most \(4\).

## Lemma 2.1

Suppose \(K=K_5(G)\) can be optimally colored in polynomial time. Then one can, in polynomial time,

- color \(G\) optimally if \(G\) is bipartite, and
- otherwise color \(G\) with at most \(\chi(G)+2\) colors.

### Proof

Test bipartiteness first. Thus suppose \(G\) is non-bipartite, so \(\chi(G)\ge 3\).

Let
\[
q=\chi(K),
\]
with \(q=0\) if \(K\) is empty, and optimally color \(K\). Put
\[
Q=\max\{q,5\}.
\]

Record the order in which the vertices outside \(K\) were deleted. Reinsert them in reverse order. When a vertex is reinserted, at most four of its neighbors have already been colored. Hence one of the \(Q\ge5\) colors is available.

Since \(K\) is an induced subgraph,
\[
q\le \chi(G).
\]
Consequently,
\[
Q\le \max\{\chi(G),5\}\le \chi(G)+2,
\]
the last inequality following from \(\chi(G)\ge3\). ∎

## Corollary 2.2: fixed surfaces

For every fixed Euler genus \(g\), triangle-free graphs embeddable in a surface of Euler genus at most \(g\) admit a polynomial-time additive \(2\)-approximation. The constant \(2\) is independent of \(g\).

### Proof

Let \(K=K_5(G)\), with \(n=|V(K)|\) and \(m=|E(K)|\). Since \(K\) is triangle-free and embeddable in Euler genus \(g\), the standard Euler bound gives
\[
m\le 2n-4+2g.
\]
On the other hand, \(\delta(K)\ge5\), so
\[
m\ge \frac52n.
\]
Therefore
\[
\frac52n\le2n-4+2g,
\qquad\text{and hence}\qquad
n\le4g-8.
\]

Thus, for fixed \(g\), the \(5\)-core has bounded order and can be optimally colored by exhaustive search in constant time depending on \(g\). Lemma 2.1 applies. Notice that the embedding itself is not needed by the algorithm; it is only used to prove that the core is bounded. ∎

If one invokes a constructive version of the fixed-surface triangle-free \(3\)-colorability algorithm mentioned in the question, the same argument improves the bound to \(+1\): first handle bipartite and \(3\)-colorable instances exactly; otherwise \(\chi(G)\ge4\), and
\[
\max\{\chi(K),5\}\le\chi(G)+1.
\]

# 3. Uniform \(+3\) for bounded vertex-planarization

Let
\[
\mathcal A_a=\{G:\text{there is }A\subseteq V(G),\ |A|\le a,\text{ such that }G-A\text{ is planar}\}.
\]
For each fixed \(a\), this is a proper minor-closed class.

## Theorem 3.1

For every \(a\ge0\), triangle-free graphs in \(\mathcal A_a\) can be colored in polynomial time with at most
\[
\chi(G)+3
\]
colors. The additive constant \(3\) does not depend on \(a\).

### Proof

For fixed \(a\), enumerate all subsets of at most \(a\) vertices and use planarity testing to find \(A\) such that \(G-A\) is planar. This takes \(O(n^a\operatorname{poly}(n))\) time.

Because \(G\) is triangle-free, \(G-A\) is triangle-free planar and can be constructively \(3\)-colored. Since \(|A|\le a\), optimally color \(G[A]\) by exhaustive search. Let
\[
q=\chi(G[A]).
\]
Use disjoint palettes on \(A\) and \(G-A\). This gives a proper coloring of \(G\) with at most \(q+3\) colors. Since \(G[A]\) is induced,
\[
q\le\chi(G),
\]
and therefore
\[
q+3\le\chi(G)+3.
\]
∎

The class \(\mathcal A_a\) is proper, for example because it excludes \(K_{a+5}\). Indeed, if \(G-A\) is planar and \(G\) had a \(K_{a+5}\)-minor model, at least five branch sets would avoid \(A\), giving a \(K_5\)-minor in \(G-A\).

Thus the same additive constant works for an infinite sequence of proper minor-closed classes whose permitted apex number tends to infinity.

# 4. A safe clique-sum extension

The preceding argument survives clique-sums when the adhesion is an actual clique in the final graph.

## Proposition 4.1

Suppose \(G\) is obtained from triangle-free graphs \(G_i\) by a tree of clique-sums along retained cliques of order at most \(2\). If every \(G_i\) can be colored with at most \(\chi(G_i)+c\) colors, then \(G\) can be colored with at most
\[
\chi(G)+c
\]
colors.

### Proof

Color every piece \(G_i\), and let
\[
Q=\max_i\{\text{number of colors used on }G_i\}.
\]
Pad every palette to \(Q\) colors.

Root the clique-sum tree. When attaching a child piece:

- over an empty adhesion, no adjustment is needed;
- over one vertex, permute the child’s colors so the shared vertex agrees;
- over a two-vertex adhesion, the adhesion is an edge, since it is a retained clique. Its endpoints have distinct colors on both sides, so a permutation maps the ordered color pair on the child side to that on the parent side.

Applying the permutation to the entire child-side subtree preserves all agreements already made there. Thus all local colorings combine into a \(Q\)-coloring of \(G\). Finally,
\[
Q\le\max_i(\chi(G_i)+c)\le\chi(G)+c.
\]
∎

In particular, the \(+3\) result holds for tree-like clique-sums of bounded-apex-to-planar pieces, even when the resulting graph has unbounded global vertex-planarization number.

The qualification “retained clique” is essential. General graph-minor structure decompositions allow edges of the summing clique to be deleted. A two-vertex adhesion can therefore become an independent pair in the final triangle-free graph, and colorings on the two sides may induce incompatible “equal versus distinct” patterns. The hardness construction below already exploits precisely this phenomenon.

# 5. Exact coloring remains hard

The next construction gives a concrete lower bound on any possible universal constant.

## 5.1 Equality and inequality gadgets

Fix \(q\ge3\). There exists a finite triangle-free \((q+1)\)-chromatic graph: start with \(C_5\) and repeatedly apply the Mycielski construction. Take a subgraph \(F_q\) minimal under deletion subject to
\[
\chi(F_q)=q+1.
\]
Thus \(F_q\) is \((q+1)\)-critical.

Choose an edge \(ab\in E(F_q)\), and put
\[
E_q=F_q-ab.
\]
Then:

1. \(\chi(E_q)=q\);
2. in every \(q\)-coloring of \(E_q\), \(a\) and \(b\) have the same color.

For the first point, criticality gives \(\chi(E_q)\le q\), while adding one edge raises chromatic number by at most one, so \(\chi(E_q)\ge q\). For the second, if a \(q\)-coloring assigned different colors to \(a\) and \(b\), it would also color \(F_q\).

Create a two-terminal graph \(I_q\) as follows:

- the first terminal is \(x=a\);
- add a fresh second terminal \(y\);
- add the edge \(by\).

The graph \(I_q\) is triangle-free. In every \(q\)-coloring of \(I_q\),
\[
\operatorname{col}(x)=\operatorname{col}(b)\ne\operatorname{col}(y).
\]
Conversely, every prescribed pair of distinct colors on \(x,y\) extends to a \(q\)-coloring of \(I_q\), by permuting a \(q\)-coloring of \(E_q\).

Thus \(I_q\) simulates an edge under \(q\)-colorings while its terminals are nonadjacent.

## 5.2 Replacing all edges

Given a graph \(B\), orient its edges arbitrarily. Replace every oriented edge \(uv\) by a fresh copy of \(I_q\), identifying \(x\) with \(u\) and \(y\) with \(v\), and delete all original edges. Denote the resulting graph by \(T_q(B)\).

The original vertices of \(B\) are independent in \(T_q(B)\), different gadget interiors are disjoint, and every gadget is triangle-free. Hence \(T_q(B)\) is triangle-free.

Moreover,
\[
T_q(B)\text{ is \(q\)-colorable}
\quad\Longleftrightarrow\quad
B\text{ is \(q\)-colorable}.
\]

Indeed, a \(q\)-coloring of \(T_q(B)\) assigns distinct colors to the endpoints of every original edge. Conversely, a \(q\)-coloring of \(B\) extends independently over every gadget.

There is also a universal \((q+1)\)-coloring of \(T_q(B)\), independent of \(B\). Give every original vertex one fresh color \(*\). In each copy of \(E_q\), start with a \(q\)-coloring in which \(a,b\) have color \(1\), and recolor \(a=x\) with \(*\). This remains proper because \(a,b\) are nonadjacent in \(E_q\), and the edge \(by\) has colors \(1,*\).

Consequently, provided \(B\) has an edge,
\[
\chi(T_q(B))=
\begin{cases}
q,& B\text{ is \(q\)-colorable},\\
q+1,& B\text{ is not \(q\)-colorable}.
\end{cases}
\tag{5.1}
\]

This collapse to the adjacent values \(q,q+1\) is exactly why the gadget does not prove hardness for larger additive errors.

## 5.3 The output still excludes a fixed complete minor

Let
\[
R_q=I_q+xy,
\]
where the terminal edge \(xy\) is added. Then \(T_q(B)\) is obtained by taking two-clique-sums of \(B\) with copies of the fixed graph \(R_q\), and deleting each common edge after the sum.

A standard branch-set argument shows that if \(s\ge4\), a \(K_s\)-minor in a two-clique-sum is contained in one of the completed summands: \(K_s\) is \(3\)-connected and cannot genuinely straddle a separation of order two. Therefore, if both \(B\) and \(R_q\) are \(K_s\)-minor-free, then so is \(T_q(B)\).

## Theorem 5.1

For every fixed \(q\ge3\), there is an \(s=s(q)\) such that \(q\)-colorability is NP-complete for triangle-free \(K_s\)-minor-free graphs. The reduction produces only graphs of chromatic number \(q\) or \(q+1\).

### Proof

Start with an instance \(P\) of planar \(3\)-colorability, and put
\[
B=K_{q-3}\vee P,
\]
where \(\vee\) denotes the join. Then
\[
\chi(B)=q-3+\chi(P),
\]
so \(B\) is \(q\)-colorable exactly when \(P\) is \(3\)-colorable.

Deleting the \(q-3\) clique vertices leaves a planar graph, so \(B\) is \((q-3)\)-apex and excludes \(K_{q+2}\). Choose
\[
s>\max\{q+1,\ |V(R_q)|\}.
\]
Then both \(B\) and \(R_q\) are \(K_s\)-minor-free, and hence so is \(T_q(B)\). The equivalence and the \(q\) versus \(q+1\) promise follow from (5.1). ∎

For \(q=3\), one may start with the \(11\)-vertex Mycielskian of \(C_5\). A \(4\)-critical subgraph has at most \(11\) vertices, so \(R_3\) has at most \(12\) vertices. Thus one can take \(s=13\).

## Corollary 5.2

Unless \(P=NP\), there is no universal additive error \(\alpha<1\), even restricted to triangle-free \(K_{13}\)-minor-free graphs.

Indeed, an algorithm using at most \(\chi(G)+\alpha\) colors with \(\alpha<1\) must return an optimal coloring, and would distinguish the two cases \(\chi=3\) and \(\chi=4\).

# 6. What remains open

The results give, under \(P\ne NP\),

\[
\alpha_{\mathrm{universal}}\ge1,
\]
if a universal constant exists at all. They give uniform upper bounds on several substantial families:

- fixed Euler genus: \(+2\), or \(+1\) using constructive fixed-surface \(3\)-colorability;
- bounded vertex-planarization: \(+3\);
- retained clique-sums of bounded-planarization pieces: \(+3\).

They do not cover arbitrary proper minor-closed classes.

A concrete sufficient structural statement for a positive solution would be:

> For every proper minor-closed class \(\mathcal C\), there is \(w_\mathcal C\) and a polynomial-time algorithm which, for every triangle-free \(G\in\mathcal C\), finds \(X\subseteq V(G)\) such that
> \[
> \operatorname{tw}(G[X])\le w_\mathcal C
> \quad\text{and}\quad
> G-X\text{ is planar}.
> \]

If this held, one could color \(G[X]\) optimally by bounded-treewidth dynamic programming, color \(G-X\) with three fresh colors, and obtain a universal \(+3\) approximation. I do not have a proof of this structural assertion, and the ordinary graph-minor structure theorem does not immediately imply it: its bounded adhesions are cliques only in completed torsos, and can be large independent sets in the original triangle-free graph.

Conversely, a negative resolution would require, for arbitrarily large \(r\), a fixed excluded minor and an NP-hard promise gap of the form
\[
\chi(G)\le q
\qquad\text{versus}\qquad
\chi(G)\ge q+r
\]
on triangle-free graphs. The explicit gadget above yields only the adjacent gap \(q\) versus \(q+1\), because one fresh color simultaneously destroys all simulated edge constraints.

Thus the central case—coordinating colors across deleted or non-clique adhesions with only universal additive slack—remains unresolved.