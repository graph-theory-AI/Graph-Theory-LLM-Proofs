```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it has an exact transition-quotient formulation and is proved here for claw-free cubic graphs and for a broad even-2-factor class.",
  "would_publish": false,
  "caveats": "No argument controls the chromatic number after changing transition choices in general; finite simple graphs are assumed."
}
```

# 1. Statement and status

Throughout, graphs are finite and simple. A coloring \(c\) of a cubic graph \(G\) is **2-homogeneous** if it is proper and, for every \(v\in V(G)\), the multiset of colors on \(N(v)\) has multiplicity pattern \(2+1\).

I do not resolve the conjecture. I give:

1. an exact reformulation as a minimization over transition quotients;
2. an example showing that one cannot simply coarsen an arbitrary given 2-homogeneous coloring to four colors;
3. proofs of the conjecture for two nontrivial classes;
4. a fully specified exhaustive-search formulation.

# 2. Transition-quotient formulation

For each vertex \(v\), choose an unordered pair
\[
P_v=\{p_v,q_v\}\subseteq N(v),
\]
and let \(r_v\) be the third neighbor.

Define a multigraph \(S_P\) on \(V(G)\) by adding the edge \(p_vq_v\) for every \(v\). These edges represent required color equalities. Let \([x]\) denote the connected component of \(x\) in \(S_P\).

Define the simple constraint graph \(Q_P\) as follows:

- its vertices are the components of \(S_P\);
- for every \(xy\in E(G)\), add the edge \([x][y]\);
- for every \(v\), add the edge \([p_v][r_v]\).

Loops are retained conceptually as evidence that \(P\) is inadmissible.

## Proposition 2.1

For a fixed transition choice \(P=(P_v)_{v\in V(G)}\), the colorings in which \(p_v\) and \(q_v\) are the equal-colored pair in \(N(v)\) are in bijection with proper colorings of \(Q_P\), pulled back to \(V(G)\). Consequently,
\[
\chi_{2h}(G)
=
\min\bigl\{\chi(Q_P): Q_P\text{ is loopless}\bigr\},
\]
where the minimum is \(+\infty\) if there is no loopless \(Q_P\).

### Proof

Suppose first that \(c\) is a 2-homogeneous coloring realizing \(P\). Since
\[
c(p_v)=c(q_v)
\]
for every \(v\), \(c\) is constant on each component of \(S_P\). Every graph edge \(xy\) has differently colored endpoints, so \([x]\) and \([y]\) receive different colors. Moreover,
\[
c(p_v)\ne c(r_v),
\]
so the additional edge \([p_v][r_v]\) is also properly colored. Thus \(c\) induces a proper coloring of \(Q_P\).

Conversely, let \(\varphi\) be a proper coloring of a loopless \(Q_P\), and put
\[
c(x)=\varphi([x]).
\]
Every edge of \(G\) becomes a constraint edge of \(Q_P\), so \(c\) is proper. Also \([p_v]=[q_v]\), whereas \([p_v]\ne[r_v]\) and these two quotient vertices are adjacent. Hence
\[
c(p_v)=c(q_v)\ne c(r_v),
\]
so exactly two colors occur in \(N(v)\). ∎

For each \(v\), the three quotient vertices
\[
[v],\qquad [p_v]=[q_v],\qquad [r_v]
\]
form a triangle in \(Q_P\). Thus \(Q_P\) is a union of local triangles, but this alone does not imply 4-colorability.

# 3. A fixed transition quotient can require five colors

The freedom to change the equal pair in some neighborhoods is essential.

Let \(G=C_5\square K_2\), with vertices
\[
x_0,\dots,x_4,\qquad y_0,\dots,y_4
\]
and edges \(x_ix_{i+1}\), \(y_iy_{i+1}\), and \(x_iy_i\), with indices modulo \(5\).

Define a 5-coloring, with colors in \(\mathbb Z_5\), by
\[
c(x_i)=i,\qquad c(y_i)=i-1.
\]
At \(x_i\), the neighbor colors are
\[
i-1,\ i+1,\ i-1,
\]
and at \(y_i\), they are
\[
i-2,\ i,\ i.
\]
Thus this is a proper 2-homogeneous coloring.

Its equality graph \(S_P\) has components
\[
C_i=\{x_i,y_{i+1}\};
\]
indeed each pair receives two parallel equality edges. Ordinary graph edges induce the cycle
\[
C_0C_1C_2C_3C_4C_0,
\]
while the pair-versus-singleton constraints induce all distance-two edges of this cycle. Therefore
\[
Q_P=C_5^2=K_5.
\]
Hence no coloring retaining these equality decisions can use fewer than five colors.

Nevertheless, the same prism has the following 4-color 2-homogeneous coloring:
\[
\begin{array}{c|ccccc}
i&0&1&2&3&4\\ \hline
c(x_i)&1&2&3&4&2\\
c(y_i)&4&3&4&2&1
\end{array}
\]
A direct check gives the neighbor-color sets
\[
\begin{array}{c|ccccc}
v&x_0&x_1&x_2&x_3&x_4\\ \hline
c(N(v))&\{2,4\}&\{1,3\}&\{2,4\}&\{2,3\}&\{1,4\}
\end{array}
\]
and
\[
\begin{array}{c|ccccc}
v&y_0&y_1&y_2&y_3&y_4\\ \hline
c(N(v))&\{1,3\}&\{2,4\}&\{2,3\}&\{1,4\}&\{2,4\}.
\end{array}
\]

Thus the stronger assertion

> every admissible transition choice \(P\) has \(\chi(Q_P)\le4\)

is false. Any proof of the conjecture must sometimes change the local equal-pair choices.

# 4. Bichromatic-chain structure

A useful structural consequence of any 2-homogeneous coloring is the following.

## Lemma 4.1

Let \(c\) be a 2-homogeneous coloring of an \(n\)-vertex cubic graph. The edges of \(G\) decompose into bichromatic paths and even cycles such that every vertex is internal in exactly one member of the decomposition and is an endpoint of exactly one path member. In particular, there are exactly \(n/2\) path members.

### Proof

For every unordered pair of colors \(\{a,b\}\), consider the subgraph formed by edges with one endpoint of color \(a\) and the other of color \(b\). At a vertex of color \(a\), at most two neighbors can have color \(b\), because all three neighbors cannot have one color in a 2-homogeneous coloring. Hence every such bichromatic subgraph has maximum degree at most two and is a union of paths and cycles. Its cycles are even because it is bipartite between the two color classes.

At every vertex \(v\), the two edges leading to the repeated neighbor color place \(v\) internally in one bichromatic path or cycle. The edge leading to the singleton neighbor color gives degree one in another bichromatic component, making \(v\) an endpoint of a path. Thus there are \(n\) path-end incidences, and therefore \(n/2\) path components. ∎

This decomposition is potentially useful, but the prism example shows that preserving it rigidly may require five colors.

# 5. Positive special case: claw-free cubic graphs

## Theorem 5.1

Let \(G\) be a cubic graph in which every vertex lies in a triangle. If \(G\) has no \(K_4\) component, then \(G\) has a 3-color 2-homogeneous coloring.

In particular, the conjecture holds for all claw-free cubic graphs admitting a 2-homogeneous coloring.

### Proof

It is enough to consider a connected component. A connected cubic graph other than \(K_4\) has a proper 3-coloring by Brooks' theorem.

Let \(c\) be such a coloring, and fix \(v\). Since \(v\) lies in a triangle, two of its neighbors, say \(x,y\), are adjacent. The three vertices \(v,x,y\) therefore receive three distinct colors. Thus \(x\) and \(y\) use precisely the two colors different from \(c(v)\).

The third neighbor \(z\) of \(v\) cannot receive \(c(v)\), by properness. Since only three colors are in use, \(c(z)\) equals either \(c(x)\) or \(c(y)\). Therefore exactly two colors occur in \(N(v)\).

A \(K_4\) component cannot satisfy the premise: every proper coloring of \(K_4\) gives three distinct colors in each open neighborhood. ∎

The unresolved part consequently contains a vertex whose neighborhood is an independent set, and in particular includes the triangle-free and bipartite cases.

# 6. Positive special case: a bipartite contraction of an even 2-factor

## Theorem 6.1

Let \(G\) be cubic and let \(M\) be a perfect matching such that:

1. every cycle of \(F=G-M\) is even;
2. after contracting each cycle of \(F\), the multigraph formed by the edges of \(M\) is bipartite and loopless.

Then \(G\) has a 4-color 2-homogeneous coloring.

### Proof

Let the cycles of \(F\) be partitioned into classes \(\mathcal C_0,\mathcal C_1\) so that every matching edge joins cycles in opposite classes.

On each even cycle \(C\), choose an alternating binary coloring
\[
\epsilon_C:V(C)\longrightarrow\{0,1\}.
\]
If \(C\in\mathcal C_i\), define
\[
c(v)=\bigl(i,\epsilon_C(v)\bigr)\in\{0,1\}^2.
\]

An edge of \(F\) has endpoints with equal first coordinate and different second coordinates. An edge of \(M\) has endpoints with different first coordinates. Hence \(c\) is proper.

For \(v\in C\), its two \(F\)-neighbors both have color
\[
\bigl(i,1-\epsilon_C(v)\bigr).
\]
Its matching neighbor lies on a cycle in \(\mathcal C_{1-i}\), so its color has first coordinate \(1-i\) and is therefore different from the common color of the two \(F\)-neighbors. Thus \(N(v)\) contains exactly two colors. ∎

This condition does not require the premise: it directly constructs the desired coloring.

# 7. A bipartite two-palette criterion

Let \(G\) be cubic bipartite with parts \(X,Y\).

## Proposition 7.1

Suppose there are maps
\[
\alpha:X\to\{0,1\},\qquad \beta:Y\to\{0,1\}
\]
such that every \(y\in Y\) has neighbors of both \(\alpha\)-values and every \(x\in X\) has neighbors of both \(\beta\)-values. Then \(G\) has a 4-color 2-homogeneous coloring.

### Proof

Use colors
\[
c(x)=(0,\alpha(x)),\qquad c(y)=(1,\beta(y)).
\]
The palettes on the two sides are disjoint, so the coloring is proper. Every neighborhood lies wholly in the opposite side and, by assumption, contains both colors of that side's palette. ∎

Equivalently, both 3-uniform neighborhood hypergraphs must have Property B. This criterion does not cover all bipartite cubic graphs and therefore does not settle the central bipartite case.

# 8. Small-order hand check

For connected simple cubic graphs on at most six vertices:

- On four vertices, the only graph is \(K_4\), which does not satisfy the premise.
- On six vertices, the only two graphs are \(K_{3,3}\) and the triangular prism. This follows by taking complements: the complement is 2-regular and hence is either \(C_6\) or \(C_3\cup C_3\).

For \(K_{3,3}\), color one side \(1,1,2\) and the other side \(3,3,4\). Every neighborhood contains exactly the two colors used on the opposite side.

For the triangular prism, color one triangle \(1,2,3\) and the other \(2,3,1\), respecting the matching order. This is a 3-color 2-homogeneous coloring.

Thus the conjecture holds for all connected simple cubic graphs on at most six vertices.

# 9. Fully specified computational search

A counterexample search can be performed without guessing an a priori number of colors for the premise.

## Testing the premise

For each vertex \(v\), enumerate one of the three pairs in \(N(v)\). There are \(3^n\) raw transition choices.

For each choice \(P\):

1. use union-find to contract every selected pair \(p_v,q_v\);
2. reject if some graph edge \(xy\) has \([x]=[y]\);
3. reject if \([p_v]=[r_v]\) for some \(v\).

By Proposition 2.1, a choice surviving these tests is exactly a certificate that \(G\) admits some 2-homogeneous coloring.

## Testing four colors

Introduce Boolean variables \(X_{v,i}\), \(i\in\{0,1,2,3\}\), meaning that \(v\) has color \(i\).

Add:

- exactly-one clauses for each vertex;
- for every edge \(uv\) and color \(i\),
  \[
  \neg X_{u,i}\lor\neg X_{v,i};
  \]
- for each \(v\) with ordered neighbors \(a,b,c\), and every ordered color triple \((i,j,k)\) using either one or three distinct colors, the clause
  \[
  \neg X_{a,i}\lor\neg X_{b,j}\lor\neg X_{c,k}.
  \]

There are \(4\) forbidden monochromatic triples and \(4\cdot3\cdot2=24\) forbidden rainbow triples per vertex. Thus these 28 clauses enforce exactly two colors in every neighborhood.

Connected simple cubic graphs of order \(n\) can, for example, be generated in graph6 format by the nauty command
```text
geng -c -d3 -D3 n
```
for even \(n\). A rigorous computational disproof should provide:

1. the graph in graph6 or adjacency-list form;
2. an admissible transition choice certifying the premise;
3. an independently checkable UNSAT proof, such as DRAT, for the 4-color SAT instance.

I have not run this enumeration and claim no computational range beyond the hand check above.

# 10. Remaining gap

The exact target is
\[
\min_{P:\,Q_P\text{ loopless}}\chi(Q_P)\le4.
\]
The prism example proves that an arbitrary admissible \(P\) may have \(\chi(Q_P)=5\), even when another transition choice gives four colors. Thus a successful proof must establish a controlled operation that changes several local equal-pair choices while preserving admissibility and eventually lowers the quotient chromatic number. I do not have such an operation, nor an explicit graph for which every admissible transition quotient is at least 5-chromatic.