```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Equality holds if some pair-crossing-optimal drawing has a crossing graph whose connected components are split graphs; the general conjecture is not resolved.",
  "would_publish": false,
  "caveats": "A self-contained structural special case and drawing-dependent bound; novelty is not claimed."
}
```

## 1. Statement of the partial result

For a drawing \(D\) of \(G\), let
\[
p(D)=\#\{\{e,f\}:e\text{ and }f\text{ cross in }D\}.
\]
Define its **crossing graph** \(X_D\) to have vertex set \(E(G)\), with two vertices adjacent precisely when the corresponding edges cross.

Drawings are in general position: edges are simple arcs, crossings are transverse and finite, and no three edge interiors meet. Crossings of adjacent edges, if present, are counted.

Recall that a graph is **split** if its vertex set can be partitioned into a clique and an independent set; the adjacencies between these two parts are arbitrary.

### Theorem
Let \(X_1,\ldots,X_m\) be the connected components of \(X_D\). For each \(i\), choose a vertex cover \(C_i\subseteq V(X_i)\). Then
\[
\boxed{\displaystyle
\operatorname{cr}(G)\le p(D)+
\sum_{i=1}^{m}
\left[
\binom{|C_i|}{2}-|E(X_i[C_i])|
\right].}
\tag{1}
\]

Thus the loss in this bound is the number of missing clique edges inside the selected vertex covers.

### Consequence
If \(D\) attains \(\operatorname{pair\text{-}cr}(G)\), and every component of \(X_D\) is split, then
\[
\operatorname{cr}(G)=\operatorname{pair\text{-}cr}(G).
\tag{2}
\]

In particular, the argument proves equality whenever
\[
\operatorname{pair\text{-}cr}(G)\le 3.
\tag{3}
\]

These are structural partial results, not a solution of the general conjecture. I do not claim that they are new.

## 2. A local redrawing lemma

The essential point is to control two kinds of crossings separately.

### Lemma
Suppose \(S\subseteq E(G)\) satisfies the following conditions in a drawing:

1. No edge of \(S\) crosses an edge outside \(S\).
2. \(S=C\mathbin{\dot\cup}L\), where the edges of \(L\) are mutually noncrossing.

Let
\[
r=\#\{(c,\ell)\in C\times L:c\text{ crosses }\ell\}.
\]
Then one can redraw only the edges of \(C\), leaving every other edge fixed, so that:

- no edge of \(S\) crosses an edge outside \(S\); and
- the total number of crossings within \(S\) is at most
  \[
  r+\binom{|C|}{2}.
  \tag{4}
  \]

The redrawing may change which \(C\)-\(L\) pairs cross.

### Proof

#### Step 1: Bound the number of \(C\)-\(L\) crossing points

Initially, permit arbitrary crossings between edges of \(C\), but require that:

- no edge of \(C\) crosses an edge outside \(S\);
- a \(C\)-\(L\) pair may cross only if it crossed in the original drawing.

Among these drawings, minimize the number \(q\) of **crossing points** between \(C\) and \(L\). This class is nonempty because it contains the original drawing. Since \(q\) is a nonnegative integer, a minimum exists.

I claim that each \(C\)-\(L\) pair crosses at most once in such a minimum drawing.

Suppose instead that \(c\in C\) and \(\ell\in L\) cross at least twice. Choose two crossings \(x,y\) consecutive along \(\ell\), among its crossings with \(c\). The interior of \(\ell[x,y]\) is disjoint from \(c\).

Replace the portion of \(c\) between \(x\) and \(y\) by an arc running in a sufficiently thin ribbon around \(\ell[x,y]\). At the joins, the surviving portions of \(c\) approach one or the other side of this ribbon. They can be joined while crossing \(\ell\) at most once: stay on one side if possible, and otherwise switch sides once.

This operation:

- removes at least the two \(c\)-\(\ell\) crossings \(x,y\);
- creates at most one \(c\)-\(\ell\) crossing;
- creates no crossing with any other edge of \(L\), since the edges of \(L\) are mutually noncrossing;
- creates no crossing with an edge outside \(S\);
- may create crossings with other edges of \(C\), which are unrestricted.

The ribbon can be chosen disjoint from the surviving portions of \(c\), except at the joins, because \(\ell[x,y]\) has no other intersection with \(c\). All modifications avoid graph vertices.

Consequently \(q\) decreases, a contradiction. Every allowed \(C\)-\(L\) pair therefore contributes at most one crossing, giving
\[
q\le r.
\tag{5}
\]

#### Step 2: Simplify crossings within \(C\) while preserving the budget

Now drop the restrictions on **which** \(C\)-\(L\) pairs may cross, retaining only:

- the fixed drawing of all edges outside \(C\);
- the prohibition on \(C\)-\((E(G)\setminus S)\) crossings;
- the numerical constraint \(q\le r\).

This class is nonempty by Step 1. Choose a drawing minimizing the total number \(T\) of crossings within \(S\).

Suppose two edges \(c,d\in C\) cross at least twice, at \(x,y\). Exchange their portions between \(x\) and \(y\), reconnecting so that each edge retains its original endpoints. At both selected crossings, use a noncrossing smoothing.

Before any self-intersections are removed:

- the two selected crossing points disappear;
- every other intersection with an edge of \(L\) remains a \(C\)-\(L\) intersection, although its central-edge label may change;
- no crossing with an edge outside \(S\) is introduced.

The two resulting edge-walks may have self-intersections. Delete closed subwalks and smooth the resulting joins to obtain simple arcs. This only deletes crossings; it does not introduce any. Thus the resulting drawing still satisfies \(q\le r\), and its total crossing count is at most \(T-2\), contradicting minimality.

Hence every pair of edges in \(C\) crosses at most once. Since \(L\) has no internal crossings,
\[
T
=q+\#\{\text{crossings between edges of }C\}
\le r+\binom{|C|}{2}.
\]
This proves the lemma. \(\square\)

**Important distinction.** Step 2 does not preserve the original set of crossing pairs. Exchanging central portions can transfer a crossing with a leaf edge from one central edge to another. What is preserved is the aggregate \(C\)-\(L\) crossing budget. Requiring preservation of the original pairs would invalidate that step.

## 3. Proof of the theorem

For each component \(X_i\), let \(S_i\subseteq E(G)\) be its corresponding set of graph edges, and put
\[
L_i=S_i\setminus C_i.
\]

Because \(C_i\) is a vertex cover of \(X_i\), the edges of \(L_i\) are mutually noncrossing. Because \(X_i\) is a component of the crossing graph, no edge of \(S_i\) crosses an edge outside \(S_i\).

Define
\[
a_i=|E(X_i[C_i])|,
\qquad
b_i=|E(X_i[C_i,L_i])|.
\]
Then
\[
|E(X_i)|=a_i+b_i.
\tag{6}
\]

Apply the lemma to \(S_i=C_i\dot\cup L_i\). It gives at most
\[
b_i+\binom{|C_i|}{2}
\]
crossing points within this component, without creating crossings with other components.

These redrawings can be performed successively: a redrawing in one component leaves every other component’s edges fixed and maintains their separation. Therefore
\[
\begin{aligned}
\operatorname{cr}(G)
&\le \sum_i\left(b_i+\binom{|C_i|}{2}\right)\\
&=\sum_i(a_i+b_i)
  +\sum_i\left(\binom{|C_i|}{2}-a_i\right)\\
&=p(D)+
  \sum_i\left(\binom{|C_i|}{2}-|E(X_i[C_i])|\right).
\end{aligned}
\]
This proves (1).

If \(X_i\) is split, choose its clique part as \(C_i\). Its complement is independent, so \(C_i\) is a vertex cover, and
\[
|E(X_i[C_i])|=\binom{|C_i|}{2}.
\]
All defect terms vanish. If \(D\) is pair-crossing-optimal, we obtain
\[
\operatorname{cr}(G)
\le p(D)
=\operatorname{pair\text{-}cr}(G)
\le \operatorname{cr}(G),
\]
proving (2).

## 4. Small values and the first uncovered patterns

### At most three crossing pairs

A connected simple graph with between one and three edges is one of
\[
K_2,\quad P_3,\quad K_3,\quad K_{1,3},\quad P_4.
\]
All are split:

- for a star, take its center as the clique part;
- for \(K_3\), take the whole graph;
- for \(P_4\), take its two middle vertices.

Isolated vertices are also split. Consequently, if \(p(D)\le3\), every component of \(X_D\) is split. Applied to an optimal drawing, this proves
\[
\boxed{\operatorname{pair\text{-}cr}(G)\le3
\quad\Longrightarrow\quad
\operatorname{cr}(G)=\operatorname{pair\text{-}cr}(G).}
\]

### Four crossing pairs

The only connected simple graphs with at most four edges that are not split are
\[
C_4\quad\text{and}\quad P_5.
\]
Indeed, a connected four-edge graph is either a five-vertex tree or a four-vertex unicyclic graph. Among the former, only \(P_5\) is nonsplit; among the latter, only \(C_4\) is nonsplit.

Both \(C_4\) and \(P_5\) have a two-vertex cover consisting of nonadjacent vertices. For that cover, the defect in (1) is exactly one. Thus this argument also gives
\[
\operatorname{pair\text{-}cr}(G)=4
\quad\Longrightarrow\quad
4\le\operatorname{cr}(G)\le5.
\tag{7}
\]
It gives equality \(4\) whenever some optimal crossing graph avoids those two exceptional patterns. This is only a limitation of the present proof, not a claim that the remaining small cases are open in the literature.

## 5. What remains missing

For an arbitrary crossing graph, a vertex cover need not be a clique. Shortcutting central edges along mutually noncrossing edges can create crossings between central edges that were formerly disjoint. Formula (1) pays for each such possible pair.

The unresolved step is to eliminate that payment—or to show that another redrawing can always compensate for it. Nothing above establishes that an optimal drawing can be chosen with split crossing components, and nothing above produces a graph with strict inequality.

Accordingly, this is a complete proof of the stated structural special case and defect bound, but neither a proof nor a counterexample for the general conjecture. It is also not a uniform asymptotic improvement over the bound quoted in the question.