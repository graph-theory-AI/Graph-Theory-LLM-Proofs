```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The complete dichotomy remains unresolved; I prove polynomial-time GI for every residual class at fixed chordal-deletion distance and derive a restrictive C5-layer structure for the (gem,P5)-free case.",
  "would_publish": false,
  "caveats": "No residual pair is fully classified, and the post-2021 literature status and novelty were not independently verified."
}
```

# Mathematical writeup

## 1. The six residual cases

Write \(+\) for disjoint union. Let

- \(D=\overline{2P_1+P_2}=K_4-e\), the diamond;
- \(J=\overline{P_1+P_4}\), the gem;
- \(S_{1,2,3}\) be the subdivided claw with arms of lengths \(1,2,3\).

Up to interchanging \(H_1,H_2\) and complementing both forbidden graphs, the source paper leaves the following six cases:

\[
\begin{array}{c|c}
H_1&H_2\\ \hline
K_3&P_7\\
K_3&S_{1,2,3}\\
D&P_1+P_2+P_3\\
D&P_1+P_5\\
J&P_2+P_3\\
J&P_5.
\end{array}
\]

I do not settle any of these six classes completely. The first result below gives a common polynomial-time slice of all six.

---

## 2. A common polynomial-time slice

For a graph \(G\), let \(\operatorname{chdel}(G)\) denote the minimum size of a vertex set \(S\) such that \(G-S\) is chordal.

### Theorem 1

Let \(H\in\{K_3,D,J\}\). If \(G\) is \(H\)-free and \(\operatorname{chdel}(G)\leq k\), then

\[
\operatorname{cw}(G)\leq 3\cdot 2^k+k.
\]

Consequently, for every fixed \(k\), Graph Isomorphism is polynomial-time solvable on each of the six residual classes restricted to graphs of chordal-deletion number at most \(k\).

### Proof

We use two standard facts about distance-hereditary graphs:

1. A graph is distance-hereditary if and only if it has no induced gem, house, domino, or induced cycle of length at least \(5\).
2. Every distance-hereditary graph has clique-width at most \(3\).

Now let \(S\subseteq V(G)\), \(|S|\leq k\), such that \(G-S\) is chordal.

We first show that \(G-S\) is gem-free.

- This is immediate if \(H=J\).
- If \(H=K_3\), it follows because the gem contains a triangle.
- If \(H=D\), note that a gem with path vertices \(p_1p_2p_3p_4\) and universal vertex \(u\) contains the diamond induced by
  \[
  \{u,p_1,p_2,p_3\}.
  \]

Thus \(G-S\) is chordal and gem-free. A chordal graph has no induced cycle of length at least \(4\). Moreover, both the house and the domino contain an induced \(C_4\). Hence \(G-S\) has none of the distance-hereditary obstructions, so it is distance-hereditary. Therefore

\[
\operatorname{cw}(G-S)\leq 3.
\]

It remains to bound the effect of adding \(S\).

### Extension lemma

If \(\operatorname{cw}(X)\leq r\) and \(G\) is obtained from \(X\) by adding a set \(S\) of \(k\) vertices with arbitrary adjacencies, then

\[
\operatorname{cw}(G)\leq r2^k+k.
\]

Indeed, partition \(V(X)\) according to the sets \(N_G(x)\cap S\); there are at most \(2^k\) such types. Starting with an \(r\)-expression for \(X\), replace every label \(i\) by product labels \((i,T)\), where \(T\subseteq S\) is the type of the vertex. Every join and relabelling operation in the original expression is applied separately to all relevant type labels. This uses at most \(r2^k\) labels and constructs \(X\) while retaining each vertex's type.

Create the vertices of \(S\) with \(k\) private labels, create \(G[S]\) using pairwise join operations, and join each \(s\in S\) to precisely those product labels whose type contains \(s\). This proves the extension lemma.

Taking \(X=G-S\) and \(r=3\) gives

\[
\operatorname{cw}(G)\leq 3\cdot 2^k+k.
\]

The supplied context states the polynomial-time solvability of GI on every bounded-clique-width class. Since \(k\) is fixed, the claimed algorithm follows. ∎

### Explicit isomorphism reduction

One can also avoid treating the deletion set as part of the input. For two promised graphs \(G,G'\):

1. Enumerate \(S\subseteq V(G)\) and \(S'\subseteq V(G')\) of equal size at most \(k\).
2. Retain choices for which \(G-S\) and \(G'-S'\) are chordal.
3. Enumerate bijections \(\phi:S\to S'\) preserving the induced subgraphs.
4. Color every \(x\in G-S\) by the bit vector describing \(N(x)\cap S\), with coordinates transported through \(\phi\), and analogously color \(G'-S'\).
5. Test color-preserving isomorphism of the two distance-hereditary remainders.

An isomorphism maps a chordal deletion set to a chordal deletion set, so the enumeration contains a successful choice whenever the original graphs are isomorphic. Conversely, any color-preserving isomorphism of the remainders extends \(\phi\) to an isomorphism of the original graphs. This is polynomial for every fixed \(k\).

---

## 3. Structure around a \(C_5\) in the \((J,P_5)\)-free case

The obstruction to applying Theorem 1 globally is not merely technical: residual classes can have unbounded distance from distance-hereditary graphs. Nevertheless, one obtains a fairly rigid layering around an induced \(C_5\).

### Lemma 2

Let \(G\) be a connected \((J,P_5)\)-free graph, and let

\[
C=c_0c_1c_2c_3c_4c_0
\]

be an induced \(C_5\), with indices modulo \(5\). Then:

1. For every \(x\notin C\), the set \(N_C(x)=N(x)\cap V(C)\) is one of:
   - the empty set;
   - a pair of nonadjacent vertices of \(C\);
   - a three-element subset of \(V(C)\).

2. Every vertex of \(G\) is at distance at most \(2\) from \(C\).

3. If \(x\) is at distance \(2\) from \(C\), \(xy\in E(G)\), and \(y\) is at distance \(1\) from \(C\), then
   \[
   |N_C(y)|=3
   \]
   and the two vertices of \(C\setminus N_C(y)\) are nonadjacent.

4. For every nonempty \(S\subseteq V(C)\), the cell
   \[
   X_S=\{x\notin C:N_C(x)=S\}
   \]
   induces a cograph.

### Proof

#### Possible \(C\)-neighborhoods

If \(|N_C(x)|\geq4\), four neighbors of \(x\) on \(C\) induce a \(P_4\), and \(x\) is universal to it. This is an induced gem, impossible.

If \(N_C(x)=\{c_i\}\), then

\[
x,c_i,c_{i+1},c_{i+2},c_{i+3}
\]

induce a \(P_5\).

If \(N_C(x)=\{c_i,c_{i+1}\}\), then

\[
x,c_{i+1},c_{i+2},c_{i+3},c_{i+4}
\]

induce a \(P_5\); the other neighbor \(c_i\) of \(x\) is not among these five vertices.

Thus a two-element neighborhood must consist of nonadjacent cycle vertices, and the only remaining nonempty possibility is a three-element set. This proves part 1.

#### No third distance layer

Suppose there is \(z\) at distance \(3\) from \(C\), and choose a shortest path

\[
z-x-y-a
\]

where \(x\) is at distance \(2\), \(y\) at distance \(1\), and \(a\in C\). By part 1, \(N_C(y)\) is nonempty and proper. Since \(C\) is connected, there is an edge \(a'b\) of \(C\) with

\[
a'\in N_C(y),\qquad b\notin N_C(y).
\]

Then

\[
z-x-y-a'-b
\]

is an induced \(P_5\): all potential chords are excluded by the distance layers, except \(yb\), which is absent by construction. This contradiction proves part 2.

#### First-layer vertices that see the second layer

Let \(x\) be at distance \(2\), with \(xy\in E(G)\), where \(y\) is at distance \(1\).

If \(N_C(y)\) is a nonadjacent pair, by symmetry let it be \(\{c_0,c_2\}\). Then

\[
x-y-c_0-c_4-c_3
\]

is an induced \(P_5\).

If \(|N_C(y)|=3\) and the two nonneighbors are consecutive, say

\[
C\setminus N_C(y)=\{c_3,c_4\},
\]

then

\[
x-y-c_2-c_3-c_4
\]

is an induced \(P_5\).

Hence \(N_C(y)\) has size \(3\), and its two missing cycle vertices must be nonadjacent. This proves part 3.

#### The cells are cographs

In any gem-free graph, the open neighborhood of every vertex is \(P_4\)-free: an induced \(P_4\) in \(N(v)\), together with \(v\), would induce a gem.

For nonempty \(S\), choose \(c_i\in S\). Then \(X_S\subseteq N(c_i)\), and consequently \(G[X_S]\) is \(P_4\)-free, that is, a cograph. ∎

Thus, once a \(C_5\) is fixed, its first distance layer splits into only

\[
5+\binom{5}{3}=15
\]

possible neighborhood cells, each inducing a cograph. Only five of the ten three-neighbor cells can have neighbors in the second distance layer.

This does not yet give an isomorphism algorithm: the edges between distinct cells and inside the second layer remain insufficiently controlled.

---

## 4. Why bounded deletion distance does not settle the case

Let \(B_m\) be the independent blow-up of \(C_5\): replace every \(c_i\) by an independent set \(A_i\) of size \(m\), make \(A_i\) complete to \(A_{i-1}\) and \(A_{i+1}\), and add no other edges.

Then:

- \(B_m\) is triangle-free, hence gem-free.
- \(B_m\) is \(P_5\)-free. If an induced \(P_5\) used two vertices from the same bag, those two vertices would be false twins in the induced subgraph, whereas \(P_5\) has no false-twin pair. Hence an induced \(P_5\) would use one vertex from every bag, but those five vertices induce \(C_5\), not \(P_5\).
- Deleting fewer than \(m\) vertices leaves every bag nonempty, so the remainder still contains an induced \(C_5\). Since distance-hereditary graphs contain no induced \(C_5\), the distance-hereditary deletion number, and also the chordal deletion number, of \(B_m\) is at least \(m\).

Therefore Theorem 1 does not cover the whole \((J,P_5)\)-free class, even on connected graphs. The example has large modules, suggesting that any complete algorithm must combine the \(C_5\)-layer analysis with modular or split decomposition rather than relying only on a bounded deletion set.

---

## 5. Remaining gaps

1. The relations between the fifteen \(C_5\)-neighborhood cells in Lemma 2 are not characterized.
2. The second distance layer can still carry nontrivial structure.
3. No analogous decomposition is completed for the other five residual pairs.
4. Nothing here distinguishes polynomial-time solvability from GI-completeness on any full residual class.

Accordingly, this is a genuine but limited partial result, not a resolution of the catalog question.