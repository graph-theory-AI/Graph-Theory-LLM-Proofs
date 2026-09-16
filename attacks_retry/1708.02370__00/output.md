```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a clustered-colouring bound within one colour of optimal for excluded cycles, and deduce the conjectured bound for every wheel.",
  "would_publish": false,
  "caveats": "Uses the established bounded-treedepth theorem supplied in the question; novelty of these corollaries is not claimed, and the general conjecture remains unresolved."
}
```

## 1. Formulation and partial result

I use the intended source formulation
\[
\chi^\star(\mathcal M_H)\le 2\,\operatorname{ctd}(H)-2,
\]
where \(\operatorname{ctd}\) is connected tree-depth: the minimum height of a single rooted tree whose closure contains \(H\). For connected \(H\), this equals ordinary tree-depth.

The previous \(2K_1\) argument is therefore discarded: \(\operatorname{ctd}(2K_1)=2\), so it is not a counterexample.

Here is a special-case result, obtained using the established bounded-treedepth theorem stated in the question.

**Proposition.** Let \(n\ge3\), put \(k=\lceil\log_2 n\rceil\), and let
\[
W_{n+1}=K_1\vee C_n
\]
be the wheel with \(n\) rim vertices. Then
\[
\boxed{\quad
k\le \chi^\star(\mathcal M_{C_n})\le k+1
\quad}
\tag{1}
\]
and
\[
\boxed{\quad
\chi^\star(\mathcal M_{W_{n+1}})\le 2k+2
   =2\,\operatorname{ctd}(W_{n+1})-2.
\quad}
\tag{2}
\]
Consequently, the conjectured inequality holds for every cycle and every wheel.

The classes \(\mathcal M_{C_n}\) themselves do **not** have bounded tree-depth or bounded pathwidth: they contain all forests. Thus an additional argument is needed to apply the supplied bounded-treedepth result.

All graphs below are finite and simple.

## 2. The established bounded-treedepth input

Let \(U_{h,m}\) be the closure of the complete rooted \(m\)-ary tree of height \(h\), with height counting vertices. Equivalently,
\[
U_{1,m}=K_1,\qquad
U_{h,m}=K_1\vee\bigl(mU_{h-1,m}\bigr).
\]

The bounded-treedepth theorem of Norin–Scott–Wood cited in the question gives the following consequence:

> **Bounded-treedepth input.** If a minor-closed class \(\mathcal A\) has bounded ordinary tree-depth and excludes a fixed graph \(H\), then
> \[
> \chi^\star(\mathcal A)\le \operatorname{ctd}(H)-1.
> \tag{3}
> \]

Indeed, if \(t=\operatorname{ctd}(H)\), then \(H\) is a subgraph of \(U_{t,m}\) for sufficiently large \(m\). Hence the tree-closure number of \(\mathcal A\) is at most \(t\), and the quoted theorem
\(\chi^\star(\mathcal A)=\operatorname{tcn}(\mathcal A)-1\)
implies (3).

This is the only substantial external colouring theorem used below.

## 3. Bounded circumference gives bounded tree-depth inside blocks

For \(n\ge3\), a graph contains a \(C_n\)-minor if and only if it contains a cycle with at least \(n\) vertices. One direction follows by contracting a longer cycle. For the other, a cycle-minor model can be unfolded through its branch sets into a cycle meeting all \(n\) branch sets.

Thus \(C_n\)-minor-free graphs have circumference at most \(n-1\).

We need a bound on paths in their 2-connected blocks. The following deliberately nonoptimal estimate has an elementary proof.

**Lemma 1.** If a 2-connected graph \(B\) has circumference at most \(s\), then every path in \(B\) has at most \(s(s-1)\) edges. Consequently,
\[
\operatorname{td}(B)\le s(s-1)+1.
\tag{4}
\]

**Proof.** Let
\[
P=v_0v_1\cdots v_\ell
\]
be a path. The assertion is immediate for \(\ell\le1\), so assume \(\ell\ge2\).

Associate intervals with the following paths having their interiors outside \(P\):

* A chord \(v_av_b\) of \(P\), where \(a<b\), gives the interval \((a,b)\).
* For each component \(X\) of \(B-V(P)\), let \(a\) and \(b\) be its smallest and largest attachment indices on \(P\). Choose a \(v_a\)-\(v_b\) path through \(X\), and associate the interval \((a,b)\).

The chosen paths have pairwise disjoint interiors. For every internal index \(i\), 2-connectivity implies that some associated interval satisfies
\[
a<i<b;
\]
otherwise \(v_i\) separates the two sides of \(P\). Since all interval endpoints are integers, these open intervals cover \((0,\ell)\).

Choose an inclusion-minimal subcover, and denote its intervals and corresponding paths by
\[
(a_1,b_1),\ldots,(a_m,b_m),\qquad Q_1,\ldots,Q_m,
\]
ordered by their left endpoints. Minimality gives
\[
a_1=0,\qquad b_m=\ell,
\]
\[
a_i<a_{i+1}<b_i<b_{i+1},
\qquad
b_i\le a_{i+2}
\tag{5}
\]
whenever the indices exist.

Each
\[
D_i=Q_i\cup P[a_i,b_i]
\]
is a cycle. Therefore
\[
b_i-a_i+|E(Q_i)|\le s,
\qquad\text{so}\qquad b_i-a_i\le s-1.
\tag{6}
\]

The symmetric difference of the edge sets of \(D_1,\ldots,D_m\) is a single simple cycle containing every \(Q_i\). To verify this, add the cycles in order. At step \(i+1\), the current cycle meets \(D_{i+1}\) exactly in the nontrivial path \(P[a_{i+1},b_i]\); replacing that path by its complementary arc preserves a single cycle. The endpoint ordering (5) and disjoint interiors of the \(Q_i\) justify this assertion.

This cycle has at least \(m\) edges, so \(m\le s\). Since the intervals cover \((0,\ell)\), (6) yields
\[
\ell\le\sum_{i=1}^m(b_i-a_i)
     \le m(s-1)
     \le s(s-1).
\]

Finally, a depth-first-search spanning tree has every graph edge between comparable vertices. Its height is at most the maximum number of vertices in a path. Its closure therefore witnesses (4). ∎

## 4. Passing from bounded-treedepth blocks to the whole graph

The price of gluing clustered-coloured blocks is at most one colour.

**Lemma 2.** Suppose every block of every graph in a class admits a \(q\)-colouring with clustering at most \(c\). Then every graph in the class admits a \((q+1)\)-colouring with clustering at most \(\max\{c,1\}\).

Here bridges are regarded as \(K_2\)-blocks.

**Proof.** Work in one connected component and root its block-incidence tree at a vertex \(r\). Give \(r\) any colour from a palette of \(q+1\) colours.

Process the blocks away from \(r\). When a block \(B\) is reached, its parent vertex \(v\) is already coloured and its other vertices are uncoloured. Restrict a clustered \(q\)-colouring of \(B\) to \(B-v\), and relabel its colours into the \(q\) colours different from the colour of \(v\).

Thus every edge from \(v\) to \(B-v\) is bichromatic. A monochromatic component cannot pass through a parent vertex into a child block. Every monochromatic component is consequently contained in one coloured \(B-v\), or is the singleton \(r\), and has the required size. Different connected components can use the same palette. ∎

### Applying the lemmas to excluded cycles

Let \(\mathcal B_n\) be the minor-closure of the collection consisting of:

* all 2-connected \(C_n\)-minor-free graphs;
* \(K_2\) and \(K_1\).

By Lemma 1 and minor-monotonicity of tree-depth,
\[
\operatorname{td}(B)\le (n-1)(n-2)+1
\qquad\text{for every }B\in\mathcal B_n.
\]
Also, \(\mathcal B_n\) excludes \(C_n\).

The standard tree-depth recurrence gives
\[
\operatorname{td}(P_m)=\lceil\log_2(m+1)\rceil
\]
by splitting a path at its root. Since deleting any vertex of \(C_n\) leaves \(P_{n-1}\),
\[
\operatorname{ctd}(C_n)
=\operatorname{td}(C_n)
=1+\operatorname{td}(P_{n-1})
=k+1.
\tag{7}
\]

Apply (3) to \(\mathcal B_n\), with \(H=C_n\). There is a constant \(c_n\) such that every member of \(\mathcal B_n\) is \(k\)-colourable with clustering at most \(c_n\).

Every block of a \(C_n\)-minor-free graph belongs to \(\mathcal B_n\). Lemma 2 therefore gives
\[
\chi^\star(\mathcal M_{C_n})\le k+1.
\tag{8}
\]

This is already stronger than the conjectured bound, since
\[
k+1\le 2k
=2\,\operatorname{ctd}(C_n)-2.
\]

### The lower bound in (1)

For completeness, the lower bound follows from the standard tree-closure obstruction, which can be checked directly.

For every \(h\ge1\) and \(c\ge1\), the graph \(U_{h,c}\) has no \((h-1)\)-colouring with clustering at most \(c\). Induct on \(h\). The case \(h=1\) is immediate. In a supposed colouring of \(U_{h,c}\), let \(a\) be the colour of its universal root. At most \(c-1\) other vertices can have colour \(a\). Among its \(c\) copies of \(U_{h-1,c}\), one therefore contains no colour \(a\). That copy would have an \((h-2)\)-colouring with clustering at most \(c\), contradicting induction.

Moreover,
\[
\operatorname{td}(U_{h,c})=h:
\]
the defining tree gives the upper bound, and a root-to-leaf chain gives a clique of order \(h\).

By (7) and minor-monotonicity of tree-depth, \(U_{k,c}\) is \(C_n\)-minor-free. Since this holds for every \(c\), the preceding obstruction gives
\[
\chi^\star(\mathcal M_{C_n})\ge k.
\]
Together with (8), this proves (1).

## 5. Wheels: the BFS-layer step meets the conjectured bound

Let \(G\) exclude \(W_{n+1}=K_1\vee C_n\) as a minor. In each connected component, take BFS layers
\[
L_0,L_1,L_2,\ldots.
\]

For \(i\ge1\), the subgraph induced by the preceding layers is connected, and every vertex of \(L_i\) has a neighbour in \(L_{i-1}\). If \(G[L_i]\) contained a \(C_n\)-minor, contracting all preceding layers to a single vertex would produce a \(K_1\vee C_n\)-minor. Therefore every layer is \(C_n\)-minor-free; this is also immediate for the singleton \(L_0\).

By (1), colour each layer with \(k+1\) colours and clustering at most \(c_n\). Use disjoint palettes on even and odd layers. Every edge joins vertices in the same or consecutive layers, so each monochromatic component lies within one layer. Hence
\[
\chi^\star(\mathcal M_{W_{n+1}})\le 2(k+1).
\tag{9}
\]

Adjoining a universal vertex increases tree-depth by exactly one. The upper bound follows by making it the root. For the reverse inequality, in any closure representation the universal vertex is comparable with every other vertex. Its ancestors form an unbranched initial chain, whose vertices can be reordered to put the universal vertex first, without increasing height. Deleting that root then gives a representation of the original graph with height one less.

Consequently,
\[
\operatorname{ctd}(W_{n+1})
=1+\operatorname{td}(C_n)
=k+2.
\]
Thus (9) is exactly
\[
\chi^\star(\mathcal M_{W_{n+1}})
\le 2\,\operatorname{ctd}(W_{n+1})-2,
\]
proving (2).

## 6. Scope and remaining gap

The proved statements cover all \(n\ge3\), with a clustering constant depending only on \(n\). No maximum-degree restriction is imposed.

The argument does not establish the general conjecture:

* The bounded-treedepth reduction for blocks is special to bounded circumference. For example, if \(H\) has a vertex of degree at least three, arbitrarily long cycles are \(H\)-minor-free, so the 2-connected members of \(\mathcal M_H\) need not have bounded tree-depth.
* The BFS step **doubles** the number of colours. If one only knows the conjectured bound \(2t-2\) for a graph \(J\) of connected tree-depth \(t\), this step gives \(4t-4\) colours for \(K_1\vee J\), whereas the desired bound is \(2t\). It works for wheels because the cycle estimate is stronger: \(\chi^\star(\mathcal M_{C_n})\le\operatorname{ctd}(C_n)\).

Thus there is a complete proof of the stated cycle and wheel special cases, but no proof or counterexample for the general conjecture. These are corollaries of the supplied established theorem; I have not verified whether these particular corollaries already appear in the literature, and make no novelty claim.