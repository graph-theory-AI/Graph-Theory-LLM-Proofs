```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but it holds whenever the number of vertices is at most three times the minimum edge size minus one, and for a substantial class with a spanning tree of 2-edges.",
  "would_publish": false,
  "caveats": "The remaining cases include large 3-uniform hypergraphs and hypergraphs with a disconnected or empty 2-edge skeleton."
}
```

# 1. Statement and conventions

A proper coloring of a hypergraph is a vertex-coloring with no monochromatic hyperedge. I use the minor convention from the source paper: vertex deletion deletes every incident hyperedge, hyperedges may be deleted, and contracting a hyperedge identifies all of its vertices. Hyperedges have size at least two.

The question is:

> Does every hypergraph with no \(K_3\)-minor admit a proper 3-coloring?

I do not resolve the question. I prove two affirmative special cases and give a fairly rigid obstruction satisfied by every minor-minimal counterexample.

# 2. A branch-set description of \(K_3\)-minors

Call a nonempty set \(X\subseteq V(H)\) contractibly connected if either \(|X|=1\), or \(H[X]\) contains a connected spanning subhypergraph, so that \(X\) can be collapsed to one vertex using only hyperedges contained in \(X\).

## Lemma 2.1
A hypergraph \(H\) contains a \(K_3\)-minor if and only if there are pairwise disjoint contractibly connected sets
\[
X_1,X_2,X_3
\]
and three distinct hyperedges \(e_{12},e_{13},e_{23}\) such that, for each \(ij\in\{12,13,23\}\),
\[
e_{ij}\subseteq X_i\cup X_j,\qquad
e_{ij}\cap X_i\neq\varnothing,\qquad
e_{ij}\cap X_j\neq\varnothing.
\]

### Proof
Given such sets, contract each \(X_i\), delete all other hyperedges and vertices, and retain the three \(e_{ij}\). They become the three edges of a triangle.

Conversely, track the inverse images of the three vertices of a final \(K_3\) through a minor sequence. Every inverse image is connected by the hyperedges contracted into it. Each final graph edge originates from an uncontracted hyperedge all of whose vertices lie in the corresponding two inverse images. ∎

In particular, any graph cycle occurring among the 2-element hyperedges of \(H\) gives a \(K_3\)-minor.

# 3. An order-versus-edge-size result

Let
\[
r(H)=\min\{|e|:e\in E(H)\}.
\]

## Theorem 3.1
Let \(H\) be a nonempty hypergraph with \(r=r(H)\). If
\[
|V(H)|\le 3r-1
\]
and \(H\) has no \(K_3\)-minor, then \(H\) is 3-colorable.

Equivalently, every counterexample must satisfy
\[
|V(H)|\ge 3r(H).
\]

### Proof

Write \(n=|V(H)|\).

## Case 1: \(n\le 3r-3\)

Partition \(V(H)\) into three sets, each of size at most \(r-1\), and use these sets as the color classes. No color class can contain a hyperedge.

## Case 2: \(n=3r-2\)

Suppose \(H\) is not 3-colorable. Let \(S\) be any \(r\)-subset of \(V(H)\). The complement of \(S\) can be partitioned into two sets of size \(r-1\). If \(S\) were not itself an edge, these three sets would be independent color classes. Therefore every \(r\)-subset is a hyperedge.

For \(r=2\), the graph of 2-edges is complete and contains a triangle.

For \(r\ge3\), choose disjoint \(r\)-sets \(A,B\) and a vertex \(x\notin A\cup B\); this is possible because
\[
3r-2\ge 2r+1.
\]
The sets \(A\) and \(B\) are internal contraction edges. There are also \(r\)-edges

- contained in \(A\cup B\) and meeting both,
- of the form \(\{x\}\cup A'\), where \(A'\in\binom{A}{r-1}\),
- of the form \(\{x\}\cup B'\), where \(B'\in\binom{B}{r-1}\).

Thus \(A,B,\{x\}\) form a \(K_3\)-minor model, a contradiction.

## Case 3: \(n=3r-1\)

Let
\[
\mathcal F=\{S\in \tbinom{V(H)}r:S\in E(H)\},
\qquad
\mathcal I=\tbinom{V(H)}r\setminus\mathcal F .
\]

If \(I_1,I_2\in\mathcal I\) were disjoint, the remaining \(r-1\) vertices, together with \(I_1,I_2\), would form three independent color classes. Hence \(\mathcal I\) is intersecting.

We next claim that \(\mathcal F\) contains two disjoint members. Otherwise both \(\mathcal F\) and \(\mathcal I\) would be intersecting. The Erdős–Ko–Rado bound gives, since \(n>2r\),
\[
|\mathcal F|,|\mathcal I|
   \le \binom{n-1}{r-1}.
\]
But
\[
2\binom{n-1}{r-1}
 =\frac{2r}{n}\binom nr
 <\binom nr,
\]
contradicting that \(\mathcal F\) and \(\mathcal I\) partition \(\binom{V(H)}r\).

Choose disjoint \(A,B\in\mathcal F\), and put
\[
R=V(H)\setminus(A\cup B),
\qquad |R|=r-1.
\]

Fix \(x\in R\). Consider three classes of possible connector edges:

\[
\mathcal A_x=\bigl\{\{x\}\cup(A\setminus\{a\}):a\in A\bigr\},
\]
\[
\mathcal B_x=\bigl\{\{x\}\cup(B\setminus\{b\}):b\in B\bigr\},
\]
and the crossing \(r\)-sets contained in \(A\cup B\) and meeting both \(A\) and \(B\).

Not all crossing \(r\)-sets can belong to \(\mathcal I\): a crossing \(r\)-set and its complement in \(A\cup B\) can be chosen both crossing, and they are disjoint. Hence at least one crossing set is an edge.

If both \(\mathcal A_x\) and \(\mathcal B_x\) contained an edge, then \(A,B,\{x\}\), together with these two edges and a crossing edge, would give a \(K_3\)-minor. Thus, for each \(x\in R\), either
\[
\mathcal A_x\subseteq\mathcal I
\quad\text{or}\quad
\mathcal B_x\subseteq\mathcal I.
\tag{3.1}
\]

Assume first \(r\ge3\), so \(|R|\ge2\). If \(x\neq y\), an element of \(\mathcal A_x\) is disjoint from an element of \(\mathcal B_y\). Since \(\mathcal I\) is intersecting, opposite alternatives in (3.1) cannot occur for two distinct vertices. After interchanging \(A\) and \(B\), we may therefore assume
\[
\mathcal A_x\subseteq\mathcal I
\quad\text{for every }x\in R.
\tag{3.2}
\]

It follows that every \(r\)-set \(S\) satisfying
\[
|S\cap A|\le1
\quad\text{and}\quad
R\nsubseteq S
\tag{3.3}
\]
belongs to \(\mathcal F\). Indeed, choose \(x\in R\setminus S\), and choose \(a\in A\) so that \(S\cap A\subseteq\{a\}\). Then
\[
S\cap\bigl(\{x\}\cup(A\setminus\{a\})\bigr)=\varnothing.
\]
The second set is in \(\mathcal I\) by (3.2), so \(S\notin\mathcal I\).

Choose \(z\in B\), and partitions
\[
B\setminus\{z\}=B_1\dot\cup B_2,\qquad
R=R_1\dot\cup R_2
\]
such that all four parts are nonempty and
\[
|B_i|+|R_i|=r-1.
\]
For example, take
\[
|B_1|=1,\quad |R_1|=r-2,\quad
|B_2|=r-2,\quad |R_2|=1.
\]
Choose distinct \(a_1,a_2\in A\), and define
\[
C=\{a_1\}\cup B_1\cup R_1,\qquad
D=\{a_2\}\cup B_2\cup R_2.
\]
Condition (3.3) shows that \(C,D\in\mathcal F\). It also shows that the following are edges:
\[
E_C=\{z\}\cup B_1\cup R_1,
\qquad
E_D=\{z\}\cup B_2\cup R_2,
\]
and
\[
J=(B\setminus\{z\})\cup\{w\},
\]
where \(w\in R\). The edge \(J\) meets both \(C\) and \(D\), since \(B_1,B_2\neq\varnothing\).

Thus \(C,D,\{z\}\) are branch sets, \(C,D\) are their internal contraction edges, and \(E_C,E_D,J\) are the three connectors. This is a \(K_3\)-minor, a contradiction.

It remains to handle \(r=2\). Then \(|R|=1\), say \(R=\{x\}\). Suppose, by symmetry, that both pairs joining \(x\) to the two vertices of \(A\) are in \(\mathcal I\). Any missing pair not containing \(x\) would have to meet both of these pairs, and hence would have to equal \(A\), which is an edge. Therefore every pair in \(V(H)\setminus\{x\}\) is an edge. The 2-edge graph contains \(K_4\), hence a \(K_3\)-minor.

All cases give contradictions. ∎

## Consequences

- A counterexample with minimum edge size \(3\) has at least \(9\) vertices.
- More generally, any counterexample satisfies \(r(H)\le |V(H)|/3\).
- The theorem does not require uniformity.

# 4. The local structure of a minor-minimal counterexample

The next lemma records what goes wrong when one tries to lift a coloring through a hyperedge contraction.

First delete every hyperedge properly containing another hyperedge. This does not alter the set of proper colorings: a nonmonochromatic subedge makes every containing edge nonmonochromatic. Thus a minimal counterexample may be assumed to be a clutter.

## Lemma 4.1
Let \(H\) be vertex-minimal among \(K_3\)-minor-free non-3-colorable hypergraphs, and suppose \(H\) is a clutter. Let \(e\in E(H)\), contract \(e\) to a vertex \(z\), and let \(\varphi\) be any proper 3-coloring of \(H/e\). Relabel the colors so that \(\varphi(z)=1\).

Then, for every \(x\in e\) and each \(c\in\{2,3\}\), there is an edge \(f_{x,c}\) satisfying
\[
f_{x,c}\cap e=\{x\}
\]
and
\[
\varphi(v)=c\quad\text{for every }v\in f_{x,c}\setminus e.
\]

### Proof
Lift \(\varphi\) to \(H\) by assigning color \(1\) to every vertex of \(e\). Since \(H\) is a clutter, no edge other than \(e\) is contained in \(e\). Hence every edge except \(e\) remains nonmonochromatic.

Now recolor one vertex \(x\in e\) with color \(c\in\{2,3\}\). The edge \(e\) becomes nonmonochromatic. If the resulting coloring were improper, a newly monochromatic edge \(f\) must contain \(x\), contain no other vertex of \(e\), and have every vertex outside \(e\) colored \(c\). Since \(H\) is not 3-colorable, such an edge must exist. ∎

If \(r=r(H)\), this gives
\[
|f_{x,c}\setminus e|\ge r-1.
\]
Moreover, \(f_{x,2}\setminus e\) and \(f_{x,3}\setminus e\) are disjoint, and
\[
e,\ f_{x,2},\ f_{x,3}
\]
pairwise intersect exactly in \(x\).

The obstruction to immediately obtaining a triangle minor is important: each set \(f_{x,c}\setminus e\) is monochromatic in \(H/e\), and consequently contains no hyperedge. Thus, when it has more than one vertex, it need not be contractibly connected. This is precisely the phenomenon exhibited by complete uniform examples such as \(K_6^{(3)}\).

A second standard consequence is that a vertex-minimal counterexample has minimum vertex degree at least \(3\): in a coloring of \(H-v\), each of the three colors must be blocked by a distinct edge through \(v\).

# 5. A special case with a spanning tree of 2-edges

Let \(H^\circ\) denote the clutter of inclusion-minimal edges of \(H\), and let \(T\) be the graph consisting of the 2-element edges of \(H^\circ\).

## Theorem 5.1
Suppose \(H\) has no \(K_3\)-minor and \(T\) is connected and spanning. Let \(A,B\) be the bipartition of \(T\). Then:

1. Every hyperedge of \(H^\circ\) is contained in \(A\) or in \(B\), unless it is an edge of \(T\).
2. Both \(H^\circ[A]\) and \(H^\circ[B]\) are \(K_2\)-minor-free.
3. Consequently, \(H\) is 3-colorable in either of the following situations:
   - all hyperedges of size at least \(3\) lie in one bipartition class; or
   - for every component \(C\) of \(H^\circ[A]\) and component \(D\) of \(H^\circ[B]\), at most one edge of \(T\) joins \(C\) to \(D\).

### Proof

Since any graph cycle gives a \(K_3\)-minor, \(T\) is a tree.

Let \(e\) be an edge of \(H^\circ\) of size at least \(3\). Since \(H^\circ\) is a clutter, \(e\) contains no edge of \(T\); thus \(e\) is an independent set in \(T\).

Suppose \(e\) met both \(A\) and \(B\). Choose \(u,v\in e\) in opposite sides. Along the unique \(u\)-\(v\) path in \(T\), list consecutive vertices belonging to \(e\). Because \(e\) is independent, the gaps between consecutive listed vertices have length at least \(2\). The total path length is odd, so one such gap has odd length at least \(3\). After contracting \(e\), this path segment becomes a simple graph cycle. Hence \(H/e\), and therefore \(H\), contains a \(K_3\)-minor, a contradiction. This proves assertion 1.

Now suppose \(H^\circ[A]\) has a \(K_2\)-minor, with disjoint connected branch sets \(X,Y\subseteq A\) and a connector edge contained in \(X\cup Y\). Choose \(x\in X\) and \(y\in Y\) minimizing their distance in \(T\). The internal vertices of the \(x\)-\(y\) path are disjoint from \(X\cup Y\). Let \(Z\) be the set of these internal vertices. Since \(x,y\in A\), the path has even length at least \(2\), so \(Z\neq\varnothing\). The path edges make \(Z\) connected, its two end edges connect \(Z\) to \(X\) and \(Y\), and the \(K_2\)-model supplies an edge between \(X\) and \(Y\). Hence \(X,Y,Z\) form a \(K_3\)-minor model, a contradiction.

Thus \(H^\circ[A]\) is \(K_2\)-minor-free; similarly for \(H^\circ[B]\). The proved bound \(h(2)\le 2g(2)=2\) from the source paper therefore gives proper binary colorings of these two induced hypergraphs.

If, say, \(H^\circ[B]\) has no edges, color \(H^\circ[A]\) properly with colors \(1,3\) and color every vertex of \(B\) with color \(2\). This proves the first coloring case.

For the second case, let \(\mathcal C_A,\mathcal C_B\) be the component sets of \(H^\circ[A]\) and \(H^\circ[B]\), including isolated vertices. Contract every component. Retaining the edges of \(T\) gives a bipartite graph \(Q\) on
\[
\mathcal C_A\cup\mathcal C_B.
\]
Its underlying simple graph is a graph minor of \(H\), so it is a forest. Under the additional hypothesis, each edge of \(Q\) comes from exactly one edge of \(T\).

Choose a proper binary coloring
\[
\sigma_C:C\to\{0,1\}
\]
of every component. Introduce a flip variable \(s_C\in\{0,1\}\). For \(C\in\mathcal C_A\), color \(v\in C\) by
\[
1\quad\text{if }\sigma_C(v)\oplus s_C=0,
\qquad
3\quad\text{otherwise}.
\]
For \(D\in\mathcal C_B\), use colors \(2,3\) in the analogous way.

An edge \(uv\in E(T)\), joining components \(C,D\), is monochromatic only when both endpoints receive color \(3\). This forbids exactly one of the four pairs \((s_C,s_D)\). Since \(Q\) is a forest, root each component of \(Q\), choose the root flip arbitrarily, and then choose each child flip to avoid the unique forbidden pair on its parent edge. All internal hyperedges remain properly colored, and every edge of \(T\) is proper.

Finally, every deleted nonminimal edge contains a properly colored minimal edge, so the coloring is proper for the original \(H\). ∎

A simple concrete corollary is that the conjecture holds whenever the 2-edge graph of the reduced clutter is a spanning star.

# 6. Complete uniform hypergraphs as a benchmark

For \(r\ge3\), let \(K_n^{(r)}\) denote the complete \(r\)-uniform hypergraph.

## Proposition 6.1
The largest \(t\) such that \(K_n^{(r)}\) has a \(K_t\)-minor is
\[
1+\left\lfloor\frac{n-1}{r}\right\rfloor .
\]

### Proof
In a clique-minor model, every nonsingleton branch set contains an internal \(r\)-edge and therefore has at least \(r\) vertices. There cannot be two singleton branch sets, since no \(r\)-edge is contained in their union. Thus a \(K_t\)-model needs at least
\[
r(t-1)+1
\]
vertices.

Conversely, take \(t-1\) disjoint \(r\)-sets and one singleton. Contract each \(r\)-set. Completeness supplies all connector edges between pairs of \(r\)-sets and between the singleton and every \(r\)-set. ∎

In particular,
\[
K_n^{(r)}\text{ is }K_3\text{-minor-free}
\quad\Longleftrightarrow\quad
n\le2r.
\]
Since
\[
\chi(K_n^{(r)})=\left\lceil\frac{n}{r-1}\right\rceil,
\]
the example \(K_{2r}^{(r)}\) is \(K_3\)-minor-free and 3-chromatic. For \(r=3\), this is \(K_6^{(3)}\), the basic sharpness example behind the source paper's lower bound.

# 7. Remaining gap

The arguments above leave two principal difficulties.

1. In the contraction obstruction of Lemma 4.1, the monochromatic traces \(f_{x,c}\setminus e\) are independent and need not be connected, so they cannot automatically serve as branch sets.

2. In Theorem 5.1, several 2-edges may join the same pair of components of \(H[A]\) and \(H[B]\). They induce several potentially incompatible flip constraints, while contraction records them only as one simple graph edge. Excluding a \(K_3\)-minor does not immediately resolve these parallel constraints.

Thus no proof or counterexample is obtained for general large 3-uniform hypergraphs, nor for general hypergraphs whose 2-edge graph is disconnected or empty.