```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds when the 1-skeleton has treewidth O(d), in particular when it is chordal.",
  "would_publish": false,
  "caveats": "General d-degenerate skeletons can have arbitrarily larger treewidth, and the argument does not handle them; novelty relative to the literature was not checked."
}
```

# Statement of the partial result

Write \(G=\partial_1H\) for the \(1\)-skeleton of a \(3\)-uniform hypergraph \(H\), and let \(\operatorname{tw}(G)\) denote its treewidth.

## Theorem

Let \(H\) be a \(3\)-uniform hypergraph on \(n\) vertices, let \(q\ge 2\), and suppose
\[
\operatorname{tw}(\partial_1H)\le t.
\]
Set
\[
\ell=\max\{3,t+1\},\qquad R=r(K_\ell^{(3)};q).
\]
Then
\[
r(H;q)\le
8q\,\ell^2 2^\ell \binom{R}{\ell}\,n.
\]
Consequently,
\[
r(H;q)\le \exp^{(2)}(O_q(t))\,n.
\]

In particular, if \(d_1(H)=d\) and
\[
\operatorname{tw}(\partial_1H)=O(d),
\]
then
\[
r(H;q)\le \exp^{(2)}(O_q(d))\,n,
\]
as conjectured.

This applies, for example, when the \(1\)-skeleton is chordal. Indeed, for a chordal graph,
\[
\operatorname{tw}(G)=\omega(G)-1=\operatorname{degeneracy}(G).
\]

The proof is self-contained modulo the elementary bound
\[
r(K_\ell^{(3)};q)\le \exp^{(2)}(O_q(\ell)),
\]
for which a standard Erdős–Rado-style argument is recalled below.

# 1. Many monochromatic cliques of one color

Let a \(q\)-coloring of \(\binom{[N]}3\) be fixed, where \(N\ge R\).

Every \(R\)-element set contains a monochromatic \(K_\ell^{(3)}\). If \(\mathcal K\) denotes the family of all monochromatic \(\ell\)-sets, double-counting pairs
\[
(K,X),\qquad K\in\mathcal K,\quad |X|=R,\quad K\subseteq X,
\]
gives
\[
|\mathcal K|\binom{N-\ell}{R-\ell}\ge \binom NR.
\]
Hence
\[
|\mathcal K|
 \ge \frac{\binom NR}{\binom{N-\ell}{R-\ell}}
 =\frac{\binom N\ell}{\binom R\ell}.
\]
By pigeonhole, some color \(c\) occurs on at least
\[
\delta\binom N\ell
\quad\text{monochromatic \(\ell\)-sets},\qquad
\delta:=\frac1{q\binom R\ell}.
\]

Let \(\mathcal G\) be the \(\ell\)-uniform hypergraph whose edges are precisely these color-\(c\) monochromatic \(\ell\)-sets. Thus
\[
e(\mathcal G)\ge \delta\binom N\ell.
\]

# 2. A robust subhypergraph

We need clique extensions of every separator that has already appeared inside one of our monochromatic cliques.

For \(1\le s\le \ell-1\), define
\[
a_s=
\frac{\delta\binom N\ell}{2\ell\binom Ns}
=
\frac{\delta}{2\ell\binom\ell s}
 \binom{N-s}{\ell-s}.
\]

Starting from \(\mathcal G\), repeatedly perform the following deletion:

- if some \(s\)-set \(S\), \(1\le s\le \ell-1\), has
  \[
  0<d_{\mathcal G}(S)<a_s,
  \]
  delete every edge containing \(S\).

Each particular \(S\) can trigger a deletion at most once. Thus the total number of deleted edges is less than
\[
\sum_{s=1}^{\ell-1}\binom Ns a_s
=
\frac{\ell-1}{2\ell}\delta\binom N\ell
<
\frac12\delta\binom N\ell.
\]
We therefore obtain a nonempty \(\ell\)-uniform hypergraph \(\mathcal G^*\) such that

\[
e(\mathcal G^*)\ge \frac{\delta}{2}\binom N\ell,
\tag{1}
\]
and, for every \(S\) with \(1\le |S|=s\le \ell-1\),
\[
d_{\mathcal G^*}(S)>0
\quad\Longrightarrow\quad
d_{\mathcal G^*}(S)\ge a_s.
\tag{2}
\]

All edges of \(\mathcal G^*\) are color-\(c\) copies of \(K_\ell^{(3)}\).

## Extension property

Let \(U\subseteq[N]\), with \(|U|\le n\), be the set of host vertices already used.

Suppose \(S\subseteq U\), \(|S|=s\ge1\), and \(S\) is contained in an edge of \(\mathcal G^*\). By (2),
\[
d_{\mathcal G^*}(S)\ge
\frac{\delta}{2\ell\binom\ell s}
 \binom{N-s}{\ell-s}.
\]
The number of \(\ell\)-sets containing \(S\) and also meeting \(U\setminus S\) is at most
\[
|U|\binom{N-s-1}{\ell-s-1}.
\]
The ratio of the degree lower bound to the latter binomial coefficient is
\[
\frac{\delta(N-s)}
 {2\ell\binom\ell s(\ell-s)}.
\tag{3}
\]

Take
\[
N\ge 8\ell^2 2^\ell\delta^{-1}n
 =8q\,\ell^2 2^\ell\binom R\ell\,n.
\tag{4}
\]
Since \(N-s\ge N/2\), \(\binom\ell s\le2^\ell\), and \(\ell-s\le\ell\), expression (3) is at least \(2n\). Therefore there is an edge \(W\in\mathcal G^*\) such that
\[
S\subseteq W,\qquad W\cap U=S.
\tag{5}
\]

For \(S=\varnothing\), (1) and the estimate
\[
|\{W\in\mathcal G^*:W\cap U\ne\varnothing\}|
 \le |U|\binom{N-1}{\ell-1}
\]
similarly show that there is an edge \(W\in\mathcal G^*\) disjoint from \(U\).

Thus every already supported separator of size at most \(\ell-1\) can be extended to a fresh color-\(c\) monochromatic \(\ell\)-clique.

# 3. Embedding along a tree decomposition

Take a width-\(t\) tree decomposition of \(G=\partial_1H\). We may use a forest, one decomposition tree for each connected component. Contracting a child bag into its parent whenever the child bag is contained in the parent, we may assume:

1. every bag has size at most \(t+1\le\ell\);
2. every non-root bag \(B\) contains a vertex not in its parent bag \(P\);
3. if bags are processed parent before child, then
   \[
   B\cap\bigcup_{\text{previous }B'}B'=B\cap P.
   \tag{6}
   \]

Property (6) follows from the connectedness condition for the bags containing any fixed graph vertex.

Every hyperedge of \(H\) is contained in a bag. Indeed, its three vertices form a triangle in \(G\). The subtrees of bags containing the three vertices are pairwise intersecting, and subtrees of a tree have the Helly property.

We now embed the bags in parent-before-child order.

- For a root bag \(B\), choose an edge \(W_B\in\mathcal G^*\) disjoint from all currently used host vertices. Map the vertices of \(B\) injectively into \(W_B\).

- For a non-root bag \(B\) with parent \(P\), put
  \[
  S=B\cap P.
  \]
  By induction, the image of \(P\) is contained in some edge \(W_P\in\mathcal G^*\); hence the image of \(S\) is supported, i.e. is contained in an edge of \(\mathcal G^*\). Since \(B\not\subseteq P\), we have \(|S|\le\ell-1\). Apply (5) to find an edge \(W_B\in\mathcal G^*\) containing the image of \(S\) and otherwise avoiding all previously used vertices. Map the vertices of \(B\setminus S\) injectively into \(W_B\setminus S\).

This is possible because
\[
|B\setminus S|\le\ell-|S|.
\]
Property (6) ensures that no vertex of \(B\setminus S\) was embedded earlier, so the maps agree on bag intersections and remain globally injective.

Finally, every hyperedge \(e\in E(H)\) lies in some bag \(B\). Its image is consequently contained in \(W_B\), and every triple in \(W_B\) has color \(c\). Thus the image of \(H\) is monochromatic.

Together with (4), this proves
\[
r(H;q)\le
8q\,\ell^2 2^\ell\binom{R}{\ell}\,n.
\]

# 4. Size of the constant

For fixed \(q\), the elementary hypergraph Ramsey estimate is
\[
R=r(K_\ell^{(3)};q)\le 2^{2^{O_q(\ell)}}.
\]

For completeness, one may obtain this as follows. Construct vertices
\[
v_1,\ldots,v_{M+1}
\]
such that for every \(i<j\), the color of
\[
\{v_i,v_j,x\}
\]
is constant over all subsequently selected \(x\). At stage \(j\), the reservoir loses a factor at most \(q^{j-1}\). Taking
\[
M=r(K_{\ell-1};q)
\]
in the ordinary graph Ramsey problem, the induced coloring of pairs among the first \(M\) vertices contains a monochromatic \(K_{\ell-1}\); adding \(v_{M+1}\) gives a monochromatic \(K_\ell^{(3)}\). Since the elementary graph bound gives \(M=2^{O_q(\ell)}\), this construction requires at most
\[
2^{2^{O_q(\ell)}}
\]
vertices.

It follows that
\[
\log_2\binom R\ell
 \le \ell\log_2 R
 =2^{O_q(\ell)},
\]
and hence
\[
8q\,\ell^2 2^\ell\binom R\ell
 =2^{2^{O_q(\ell)}}.
\]
Therefore
\[
r(H;q)\le \exp^{(2)}(O_q(t))\,n.
\]

# 5. Consequences

If \(d_1(H)=d\) and \(\operatorname{tw}(\partial_1H)\le A d\) for a fixed \(A\), then
\[
r(H;q)\le \exp^{(2)}(O_{q,A}(d))\,n.
\]

Notable covered classes include:

- chordal \(1\)-skeletons;
- partial \(d\)-trees;
- graphs obtained as clique-sums of \(O(d)\)-vertex pieces;
- trees of copies of \(K_{d+1}\), whose chromatic number is \(d+1\) and hence is not bounded independently of \(d\);
- \(1\)-skeletons with vertex cover \(O(d)\).

Thus this is not a consequence of the bounded-chromatic-number case quoted in the source context.

# 6. Remaining gap

A degeneracy ordering \(v_1,\dots,v_n\) provides sets
\[
B_i=\{v_i\}\cup N^-(v_i),\qquad |B_i|\le d+1,
\]
and every hyperedge is contained in one such \(B_i\). This superficially resembles the bag argument above. The essential missing property is that \(N^-(v_i)\) need not be contained in any previously constructed monochromatic clique. In a genuine tree decomposition, each separator lies inside the parent bag and is therefore “supported”; this is exactly what permits the robust extension lemma to be applied.

General \(d\)-degenerate graphs can have arbitrarily large treewidth. For instance, triangulated grids have bounded degeneracy and unbounded treewidth, and taking their triangular faces as hyperedges realizes the grid as a \(1\)-skeleton. Thus the theorem does not imply Conjecture 6.1 in general. A proof of the full conjecture would need a way to handle these unsupported backward neighborhoods without paying the additional \(\log d\) appearing in the known general bound.