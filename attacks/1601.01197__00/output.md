```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is a linear-time output algorithm for the precoloring-extension problem at girth at least six, and more generally when the protected 3-core has only boundedly many vertices of degree at least four.",
  "would_publish": false,
  "caveats": "The argument does not handle 4- or 5-cycles, including the large quadrangulations central to the open problem."
}
```

# 1. Statement and scope

All graphs below are finite and simple. Let \(H\subseteq V(G)\) be a precolored set, and let
\[
\psi:H\to\{1,2,3\}
\]
be proper on \(G[H]\).

The following gives a genuine linear-time special case of the open problem.

## Partial theorem

Let \(\Sigma\) be a fixed surface and \(k\) a fixed integer. There is a linear-time algorithm which, given

- a graph \(G\) of girth at least \(6\) embedded in \(\Sigma\),
- a set \(H\subseteq V(G)\) with \(|H|\le k\), and
- a proper precoloring \(\psi\) of \(H\),

decides whether \(\psi\) extends to a 3-coloring of \(G\), and outputs such an extension whenever one exists.

In fact, for variable Euler genus \(\gamma\), the running time obtained below is
\[
3^{O(\gamma+|H|)}\bigl(|V(G)|+|E(G)|\bigr).
\]

The proof uses two ingredients:

1. a linear constructive precoloring-extension algorithm when all unprecolored vertices have degree at most three;
2. Euler's formula, which implies that after protected \(2\)-degeneracy peeling, only \(O_\Sigma(|H|+1)\) vertices can have degree at least four when the girth is at least six.

# 2. A constructive subcubic extension lemma

## Lemma 2.1

Let \(F\) be a triangle-free graph, let \(P\subseteq V(F)\), and let \(\eta\) be a proper 3-coloring of \(F[P]\). Suppose
\[
d_F(v)\le 3\qquad\text{for every }v\in V(F)\setminus P.
\]
Then one can decide in \(O(|V(F)|+|E(F)|)\) time whether \(\eta\) extends to \(F\), and output an extension if one exists.

Notice that the precolored vertices themselves may have arbitrarily large degree, and \(P\) need not be bounded.

### Reduction to degree-list-coloring

Put \(Q=F-P\). For \(v\in V(Q)\), define
\[
L(v)=\{1,2,3\}\setminus \eta(N_F(v)\cap P).
\]
A proper \(L\)-coloring of \(Q\) is exactly an extension of \(\eta\).

Let
\[
r=|N_F(v)\cap P|,\qquad
s=|\eta(N_F(v)\cap P)|.
\]
Then
\[
|L(v)|=3-s\ge 3-r\ge d_F(v)-r=d_Q(v).
\]
Thus it suffices to solve the following special list-coloring problem.

## Lemma 2.2

Let \(Q\) be triangle-free and let \(L(v)\subseteq\{1,2,3\}\) satisfy
\[
|L(v)|\ge d_Q(v)
\]
for every \(v\). There is a linear-time algorithm which either outputs an \(L\)-coloring of \(Q\) or correctly determines that none exists.

### Proof

Work separately in each connected component.

#### Case 1: a vertex has surplus

Suppose some vertex \(z\) satisfies
\[
|L(z)|>d_Q(z).
\]
Root a spanning tree at \(z\), and order all other vertices before their parents, with \(z\) last. Color greedily in this order.

Every non-root vertex has an uncolored parent when it is colored, and therefore sees at most \(d_Q(v)-1\) already used colors. The root sees at most \(d_Q(z)\) colors and has a strictly larger list. Hence the greedy procedure succeeds.

Thus the only nontrivial case is
\[
|L(v)|=d_Q(v)\quad\text{for all }v.
\tag{2.1}
\]

An isolated vertex with an empty list is immediately rejected.

#### Case 2: every block is an edge or an odd cycle

In this case \(Q\) is an odd cactus: its block-cutvertex graph is a tree, and every nontrivial 2-connected block is an odd cycle.

A linear dynamic program on the block-cutvertex tree decides list-colorability. For each articulation vertex, keep the subset of its at most three colors that can be extended through each descendant block.

- For an edge block, test the at most nine ordered pairs of endpoint colors.
- For a cycle block, fix the color of the parent articulation and run a three-state path dynamic program around the cycle, including the closing edge.
- Store predecessors to reconstruct a coloring.

Every block edge is processed only a constant number of times, so the total running time is linear.

#### Case 3: there is another 2-connected block

Let \(B\) be a 2-connected block which is neither an edge nor an odd cycle. Since \(Q\) is triangle-free and (2.1) implies \(\Delta(Q)\le3\), the following elementary constructive fact applies.

> **Cycle fact.** A 2-connected triangle-free subcubic graph which is not an odd cycle contains an even cycle \(C\) such that \(B[V(C)]\) consists of \(C\) and at most one chord. Such a cycle can be found in linear time.

For completeness, existence follows by taking a shortest even cycle. Such an even cycle exists: a 2-connected graph which is not a cycle contains a theta subgraph, and among the three cycles of a theta at least one is even. If a shortest even cycle has a chord whose endpoints occur at opposite parities around the cycle, that chord produces a shorter even cycle. If it has two chords whose endpoints occur at equal parities, a direct check of the two possible cyclic orders of the four endpoints again produces a shorter even cycle. Hence at most one chord remains.

The constructive version does not require a global shortest-cycle computation. Start with any cycle found by DFS. If it is odd, 2-connectivity supplies a path with distinct endpoints on the cycle and interior outside it; one of the two resulting cycles is even. Then repeatedly apply the two chord-shortening operations. In a subcubic graph the chords of the current cycle form a matching, and a stack implementation of the arc replacements processes every discarded arc and every chord only constantly many times. Hence this takes linear time.

Let
\[
J=Q[V(C)].
\]
Thus \(J\) is either an even cycle or an even cycle with one chord.

Color \(Q-V(J)\) first. Every component of \(Q-V(J)\) has a neighbor in \(J\). Choose a spanning forest directed toward \(J\), and color vertices from the leaves toward \(J\). Each such vertex still has an uncolored neighbor, so by (2.1) greedy coloring succeeds.

Afterward, delete from each \(L(v)\), \(v\in V(J)\), the colors used by its already colored neighbors outside \(J\). The resulting lists \(L_J\) satisfy
\[
|L_J(v)|\ge d_J(v).
\tag{2.2}
\]

It remains to color \(J\).

- If \(J\) is an even cycle, every list has size at least two. If some list has size three, the surplus argument applies. If all lists are the same two-element set, alternate the two colors. Otherwise choose adjacent vertices \(v_1,v_t\) with different lists, select
  \[
  c\in L_J(v_1)\setminus L_J(v_t),
  \]
  color \(v_1\) with \(c\), and greedily color along the remaining path ending at \(v_t\). Since \(c\notin L_J(v_t)\), the closing edge is automatically proper.

- Suppose \(J\) is an even cycle with chord \(xy\). By (2.2), the chord endpoints have all three colors available. Let \(a,b\) be the two cycle-neighbors of \(x\). Choose \(c\in\{1,2,3\}\) so that at least one of
  \[
  |L_J(a)\setminus\{c\}|,\qquad |L_J(b)\setminus\{c\}|
  \]
  is at least two. Such a color exists: a color is bad for both endpoints only when both endpoint lists have size two and contain that color, and the intersection of two two-element subsets of a three-element palette has size at most two.

  Color \(x\) with \(c\) and remove \(x\). The graph \(J-x\) is a path. Its endpoint lists have size at least one, all internal lists have size at least two, and at least one endpoint list has size at least two. The surplus greedy argument colors this path.

This completes the proof of Lemma 2.2 and hence Lemma 2.1. \(\square\)

# 3. The protected 3-core reduction

For an instance \((G,H,\psi)\), repeatedly delete any vertex
\[
v\in V(G)\setminus H
\]
whose current degree is at most two. Record the deletion order. Let \(R\) be the graph left at termination. Thus
\[
d_R(v)\ge3\qquad\text{for every }v\in V(R)\setminus H.
\tag{3.1}
\]

Every 3-coloring of \(R\) extending \(\psi\) extends to all of \(G\): reinsert the deleted vertices in reverse order. At the time a vertex is reinserted, at most two of its neighbors have already been colored, so at least one of the three colors is available.

Consequently,
\[
\psi\text{ extends to }G
\quad\Longleftrightarrow\quad
\psi\text{ extends to }R.
\tag{3.2}
\]

Define
\[
X=\{v\in V(R)\setminus H:d_R(v)\ge4\}.
\]

## Proposition 3.1

For a triangle-free graph \(G\), the extension problem can be solved, with a coloring output, in time
\[
O\!\left(3^{|X|}\bigl(|V(G)|+|E(G)|\bigr)\right).
\]

### Proof

Enumerate all assignments
\[
\alpha:X\to\{1,2,3\}.
\]
Discard assignments for which \(\psi\cup\alpha\) is not proper on
\[
P=H\cup X.
\]

For each remaining assignment, apply Lemma 2.1 to \(R\) with \(P\) precolored. Every vertex outside \(P\) has degree exactly three in \(R\), by (3.1) and the definition of \(X\). Hence Lemma 2.1 applies.

If an extension of \(R\) is found, reverse the peeling order to color all of \(G\). Conversely, any extension of \(\psi\) to \(G\) induces one of the enumerated assignments on \(X\). Thus the algorithm is correct. \(\square\)

This proposition is useful beyond the surface setting: it gives a linear-FPT algorithm parameterized by the number of degree-at-least-four vertices in the protected 3-core.

# 4. Applying Euler's formula at girth six

For each fixed surface \(\Sigma\), there is a constant \(c_\Sigma\) such that every graph \(J\) of girth at least six embedded in \(\Sigma\) satisfies
\[
|E(J)|\le \frac32|V(J)|+c_\Sigma.
\tag{4.1}
\]

This is the standard Euler estimate. After deleting tree and bridge parts, take cellular embeddings of the remaining bridgeless components. Every facial walk has length at least six, so
\[
6f\le2m.
\]
Combining this with Euler's formula gives
\[
m\le\frac32(n-2+\gamma)
\]
on a surface of Euler genus \(\gamma\); restoring bridges and components changes only the harmless additive \(O(\gamma+1)\) term. For a fixed surface this is (4.1).

Apply (4.1) to the protected core \(R\). Write
\[
r=|V(R)|,\qquad m=|E(R)|,\qquad h=|H|.
\]
Using (3.1),
\[
\begin{aligned}
2m-3(r-h)
  &=\sum_{v\in V(R)\setminus H}\bigl(d_R(v)-3\bigr)
    +\sum_{v\in H}d_R(v).
\end{aligned}
\tag{4.2}
\]
Every term on the right is nonnegative. By (4.1),
\[
2m-3(r-h)
 \le 2c_\Sigma+3h.
\]
Each vertex of \(X\) contributes at least one to the first sum in (4.2), and hence
\[
|X|\le 2c_\Sigma+3h\le 2c_\Sigma+3k.
\tag{4.3}
\]

Thus \(|X|\) is bounded solely in terms of \(\Sigma\) and \(k\). Proposition 3.1 now gives a linear-time algorithm, with constants depending on \(\Sigma\) and \(k\).

This proves the partial theorem.

# 5. Explicit algorithm

For fixed \(\Sigma\) and \(k\):

1. Check that \(\psi\) is proper on \(G[H]\).
2. Queue all unprecolored vertices of current degree at most two.
3. Peel them, storing the deletion order.
4. In the remaining graph \(R\), form
   \[
   X=\{v\in V(R)\setminus H:d_R(v)\ge4\}.
   \]
5. Enumerate the at most
   \[
   3^{\,2c_\Sigma+3k}
   \]
   color assignments to \(X\).
6. For each proper assignment, solve the resulting subcubic precoloring-extension instance using Lemma 2.1.
7. If one succeeds, reinsert peeled vertices in reverse order, greedily choosing a color not used by their at most two already colored neighbors.
8. If no assignment succeeds, report that \(\psi\) does not extend.

All degree updates, block decompositions, list operations, and reconstruction steps are linear in \(|V(G)|+|E(G)|\). Since graphs embedded in a fixed surface are sparse, this is \(O(|V(G)|)\).

# 6. What remains unresolved

The argument depends critically on the coefficient \(3/2\) in the girth-six Euler bound.

- At girth five, Euler's estimate is only
  \[
  m\le \frac53n+O_\Sigma(1),
  \]
  so the protected 3-core may contain linearly many vertices of degree at least four.
- At girth four, large 4-regular quadrangulations are unavoidable. For example,
  \[
  C_{2a}\square C_{2b}
  \]
  is a triangle-free 4-regular toroidal quadrangulation. With \(H=\varnothing\), the peeling removes nothing and \(X=V(G)\).

The toroidal grid is itself bipartite and easy to color, so this example is an obstruction to the method, not evidence of algorithmic hardness. It shows, however, that bounded branching on high-degree vertices cannot address the quadrangulation regime. A full solution still needs a bulk constructive treatment of the large 4- and 5-cycle structures used by the decision algorithm.

Accordingly, this does not resolve the catalogued problem, nor does it provide a generic linear search-to-decision conversion for Theorem 1.3.