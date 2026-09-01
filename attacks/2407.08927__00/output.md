```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general problem remains open, but chordless even-hole-free graphs are exactly odd cacti and admit linear-time MWIS, while several natural extensions of chordal-graph methods have explicit obstructions.",
  "would_publish": false,
  "caveats": "No polynomial algorithm or hardness result is obtained for all even-hole-free graphs."
}
```

# 1. Statement and outcome

A **hole** is an induced cycle of length at least four. The problem asks whether Maximum Weight Independent Set (MWIS) is polynomial-time solvable on graphs with no even hole.

I do not obtain a solution for the whole class. I prove:

1. a structural treewidth consequence of the polylogarithmic tree-independence theorem quoted in the question;
2. an exact characterization and linear-time MWIS algorithm for chordless even-hole-free graphs, including all proper subdivisions that are even-hole-free;
3. NP-hardness of MWIS under a local elimination property stronger than merely having bisimplicial vertices, showing that such an ordering alone is insufficient;
4. an explicit even-hole-free obstruction to the natural stable-set relaxation consisting of clique and odd-cycle inequalities.

The later literature mentioned in the prompt is not used here and has not been independently verified.

# 2. A consequence of the tree-independence bound

Let \(d(G)\) denote the degeneracy of \(G\).

## Proposition 2.1

Assume the theorem quoted in the question: every \(n\)-vertex even-hole-free graph \(G\) has a tree decomposition \((T,\{B_t\})\) such that

\[
\alpha(G[B_t])\le c\log^{10}n
\]

for every bag \(B_t\). Then

\[
\operatorname{tw}(G)\le c(d(G)+1)\log^{10}n-1.
\]

### Proof

Every induced subgraph of a \(d(G)\)-degenerate graph is \((d(G)+1)\)-colorable. Hence \(G[B_t]\) has a proper coloring with at most \(d(G)+1\) colors. Its largest color class is independent, so

\[
\alpha(G[B_t])\ge \frac{|B_t|}{d(G)+1}.
\]

Consequently,

\[
|B_t|
 \le (d(G)+1)\alpha(G[B_t])
 \le c(d(G)+1)\log^{10}n.
\]

The asserted treewidth bound follows from the definition of treewidth. \(\square\)

Thus, if a decomposition of the type produced in the source theorem is explicitly available, ordinary treewidth dynamic programming solves MWIS in

\[
2^{O(d(G)\log^{10} n)}\,n^{O(1)}
\]

time, apart from the cost of obtaining the decomposition. For fixed degeneracy this remains quasi-polynomial rather than polynomial, so it does not resolve even the bounded-degeneracy case.

The following example shows that even degeneracy two does not force treewidth at most three.

## Proposition 2.2

There is a \(2\)-degenerate even-hole-free graph of treewidth exactly \(4\).

### Construction

Take vertices \(a,b,c_1,c_2,c_3\). Add

\[
ab,\qquad ac_i,\qquad bc_i\quad (i=1,2,3).
\]

For every \(1\le i<j\le3\), join \(c_i\) and \(c_j\) by an internally vertex-disjoint path of length three,

\[
c_i-x_{ij}-y_{ij}-c_j.
\]

Call the resulting graph \(F\).

### Verification

Order all six internal path vertices first, then \(c_1,c_2,c_3\), and finally \(a,b\). Every vertex has at most two later neighbors. Thus \(F\) is \(2\)-degenerate. It contains the triangle \(abc_1a\), so its degeneracy is exactly two.

To check that \(F\) is even-hole-free, let \(C\) be an induced cycle.

- If \(C\) contains both \(a\) and \(b\), then either \(ab\) is a chord, or \(a,b\) are consecutive on \(C\). In the latter case the two terminals adjacent to \(a,b\) on the rest of the cycle create cross-chords because both \(a\) and \(b\) are adjacent to every \(c_i\). Thus there is no hole containing both \(a,b\).
- If \(C\) contains exactly one of \(a,b\), say \(a\), then it cannot contain all three terminals \(c_i\), since the third one would be adjacent to \(a\) and create a chord. Hence \(C\) consists of \(a\), two terminals \(c_i,c_j\), and their dedicated length-three path. It has length five.
- If \(C\) contains neither \(a\) nor \(b\), it lies in the subdivision of the triangle on \(c_1,c_2,c_3\), which is a \(9\)-cycle.

Hence every hole of \(F\) has odd length.

Finally, \(F\) is a subdivision of \(K_5\), so contracting the three length-three paths gives a \(K_5\) minor and

\[
\operatorname{tw}(F)\ge4.
\]

Conversely, one tree decomposition has central bag

\[
\{a,b,c_1,c_2,c_3\}
\]

and, for each \(i<j\), an attached bag

\[
\{c_i,x_{ij},y_{ij},c_j\}.
\]

Its width is four. Thus \(\operatorname{tw}(F)=4\). \(\square\)

# 3. A polynomial special case: chordless graphs

Call a graph **chordless** if every cycle is induced.

## Theorem 3.1

For a graph \(G\), the following are equivalent:

1. \(G\) is chordless and even-hole-free;
2. \(G\) has no even cycle, induced or otherwise;
3. every nontrivial block of \(G\) is either a bridge \(K_2\) or an odd cycle.

Consequently, chordless even-hole-free graphs have treewidth at most two, and MWIS on this class is solvable in linear time, measured in arithmetic operations on the weights.

### Proof

The implication \(1\Rightarrow2\) is immediate: every even cycle in a chordless graph would be an even hole.

For \(2\Rightarrow3\), we use the following elementary fact.

> Every \(2\)-connected graph which is not a cycle contains a theta: three internally vertex-disjoint paths with the same two distinct endpoints.

Indeed, let \(B\) be \(2\)-connected and let \(C\) be a cycle in \(B\). If \(V(B)=V(C)\) but \(B\ne C\), a chord of \(C\), together with the two arcs of \(C\), gives a theta. Otherwise, some component of \(B-V(C)\) has two distinct attachment vertices on \(C\); a path through that component, together with the two arcs of \(C\), again gives a theta.

Let the three paths in a theta have lengths \(\ell_1,\ell_2,\ell_3\). Two of these lengths have the same parity, and their union is therefore an even cycle. Thus a graph with no even cycle cannot have a \(2\)-connected block other than a cycle. Each such cycle must be odd.

For \(3\Rightarrow1\), every cycle lies in one block and hence is one of the specified odd-cycle blocks. Such a graph is chordless and has no even hole.

Graphs satisfying condition 3 are often called **odd cacti**. They have treewidth at most two. Explicitly:

- use a bag \(\{u,v\}\) for each bridge \(uv\);
- for an odd-cycle block \(v_1v_2\cdots v_kv_1\), use the path of bags
  \[
  \{v_1,v_i,v_{i+1}\},\qquad i=2,\ldots,k-1;
  \]
- glue the decompositions of different blocks through bags containing their common articulation vertex.

This produces a width-two decomposition with \(O(n+m)\) bags. Standard MWIS dynamic programming on it takes \(O(n+m)\) arithmetic operations.

The class can also be recognized in \(O(n+m)\) time by computing the blocks and checking that each block is a bridge or an odd cycle. \(\square\)

## Corollary 3.2: proper subdivisions

Let \(S\) be obtained from a simple graph \(H\) by replacing every edge by a path of length at least two, with distinct edges receiving internally disjoint paths. If \(S\) is even-hole-free, then \(S\) is an odd cactus, has treewidth at most two, and MWIS on \(S\) is linear-time solvable.

### Proof

Every cycle in \(S\) traverses each replacement path that it meets in its entirety. Since no original edge remains, an unused replacement path cannot supply a chord: its internal vertices lie outside the cycle. Hence every cycle of \(S\) is induced.

The result now follows from Theorem 3.1. Equivalently, \(H\) must itself be a cactus, and the sum of the replacement-path lengths around each cycle of \(H\) must be odd. \(\square\)

Thus standard hardness reductions based solely on subdividing all edges cannot establish hardness on even-hole-free graphs: their even-hole-free outputs have treewidth at most two.

# 4. Why a local bisimplicial-type ordering is insufficient

A common structural hope is that an ordering in which every later neighborhood is the union of two cliques might support a chordal-style elimination algorithm. The following shows that this promise alone is too weak.

## Proposition 4.1

MWIS is NP-hard, even with weights in \(\{1,2\}\), on graphs supplied with an ordering in which every vertex has at most two later neighbors. In particular, every later neighborhood is the union of at most two cliques.

### Proof

Reduce from Independent Set. Given a graph \(H=(V,E)\), replace every edge \(e=uv\) by

\[
u-a_e-b_e-v.
\]

Give every original vertex weight one and every subdivision vertex weight two.

For \(X\subseteq V(H)\), consider independent sets whose intersection with the original vertices is exactly \(X\). For an edge \(e=uv\):

- if at most one of \(u,v\) belongs to \(X\), exactly one of \(a_e,b_e\) can be chosen, contributing weight two;
- if both \(u,v\) belong to \(X\), neither \(a_e\) nor \(b_e\) can be chosen.

Therefore the maximum weight of an extension of \(X\) is

\[
f(X)=|X|+2\bigl(|E|-e_H(X)\bigr),
\]

where \(e_H(X)\) is the number of edges of \(H\) with both endpoints in \(X\).

If \(X\) is not independent, choose \(u\in X\) with at least one neighbor in \(X\). Then

\[
f(X\setminus\{u\})-f(X)
   =-1+2d_{H[X]}(u)\ge1.
\]

Thus every maximizing \(X\) is independent, and

\[
\operatorname{MWIS}(G)=2|E(H)|+\alpha(H).
\]

Hence \(\alpha(H)\ge k\) if and only if the constructed graph has an independent set of weight at least \(2|E(H)|+k\).

Finally, put all subdivision vertices first in the ordering and all original vertices last. Each subdivision vertex has total degree two, and original vertices have no edges among themselves. Therefore every vertex has at most two later neighbors. The ordering can be included in the output of the reduction. \(\square\)

This construction does not prove hardness for even-hole-free graphs. Indeed, it is a proper subdivision and hence chordless. Every cycle of length \(\ell\) in \(H\) becomes an induced cycle of length \(3\ell\). Consequently, the constructed graph is even-hole-free exactly when \(H\) has no even cycle; by Theorem 3.1, those source graphs are odd cacti and already easy.

The conclusion is narrower but rigorous: an elimination ordering with two-clique later neighborhoods cannot by itself be the missing algorithmic ingredient. The parity restrictions on how those neighborhoods interact globally must also be used.

# 5. A polyhedral obstruction inside the target class

Another natural idea is to extend the stable-set description for perfect graphs by adding odd-cycle inequalities. Odd wheels already obstruct this.

Let \(W_{2q+1}\), \(q\ge2\), consist of a rim

\[
r_1r_2\cdots r_{2q+1}r_1
\]

and a hub \(h\) adjacent to every rim vertex.

## Proposition 5.1

The odd wheel \(W_{2q+1}\) is even-hole-free, but its stable-set polytope is not described by nonnegativity, clique inequalities, and all odd-cycle inequalities.

### Proof

The only hole not containing \(h\) is the odd rim. Any cycle of length at least four containing \(h\) has a chord from \(h\) to an internal rim vertex. Thus \(W_{2q+1}\) is even-hole-free.

Consider

\[
x_h=\frac1{2q+1},
\qquad
x_{r_i}=\frac q{2q+1}\quad\text{for every }i.
\]

Every maximal clique is a triangle \(\{h,r_i,r_{i+1}\}\), and its coordinates sum to one.

The rim odd-cycle inequality is also tight:

\[
\sum_i x_{r_i}=q.
\]

Any other odd cycle consists of \(h\) and a rim path of odd length \(L\ge1\). It contains \(L+1\) rim vertices, and

\[
x_h+(L+1)\frac q{2q+1}
 \le \frac{L+1}{2},
\]

because this inequality is equivalent to \(2\le L+1\). Hence the point satisfies every odd-cycle inequality, including those for cycles with chords.

However,

\[
q x_h+\sum_{i=1}^{2q+1}x_{r_i}\le q
\tag{1}
\]

is valid for every independent set. If \(h\) is chosen, the left side is \(q\); if \(h\) is not chosen, at most \(q\) rim vertices can be chosen. At the displayed fractional point, the left side of (1) is

\[
q+\frac q{2q+1}>q.
\]

Thus the relaxation is not integral even on even-hole-free graphs. Equivalently, assigning weight \(q\) to \(h\) and weight one to each rim vertex gives integral optimum \(q\), while the relaxation has value at least \(q+q/(2q+1)\). \(\square\)

This only rules out the most direct clique-plus-odd-cycle formulation; it does not preclude a polynomial algorithm based on stronger wheel or separator inequalities.

# 6. Remaining gap

The positive result applies only when every cycle is induced. General even-hole-free graphs may contain many even cycles, provided each has a chord, and those chords are precisely what invalidate the odd-cactus argument. The source decomposition yields only polylogarithmic, rather than constant, bag independence number. The NP-hardness construction above leaves the target class in hard instances, and the odd-wheel example only defeats one LP relaxation.

Accordingly, neither a polynomial-time MWIS algorithm nor an NP-hardness proof for general even-hole-free graphs is obtained. The catalogued problem remains unresolved.