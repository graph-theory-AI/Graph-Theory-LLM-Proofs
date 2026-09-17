```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture, with any prescribed edge forbidden, for a periodic two-family cycle class containing all connected I-graphs.",
  "would_publish": false,
  "caveats": "The general conjecture is not settled; novelty of this special case has not been checked."
}
```

# A constructive extension to two periodic cycle families

I do not resolve the conjecture for arbitrary cubic 3-connected graphs. I prove a special-case theorem that extends the single outer-cycle construction in the supplied attempt.

The extension allows **both sides of the spoke matching to consist of several cycles**. It includes every connected simple \(I\)-graph, defined below. The factor can avoid any prescribed edge.

All paths are ordinary paths, not necessarily induced. The paired-transversal argument from the supplied attempt is verified below rather than assumed. The additional ingredient is a two-host construction for a case in which one host cycle is too short.

## 1. The class and the theorem

Let \(a,b,h\) be positive integers satisfying
\[
ah\ge 3,\qquad bh\ge 3.
\]

A **periodic cycle array with parameters \((a,b,h)\)** is a graph \(G\) with the following decomposition.

1. A spanning 2-factor consists of cycles
   \[
   A_0,\ldots,A_{a-1},\qquad B_0,\ldots,B_{b-1},
   \]
   where
   \[
   |A_i|=bh,\qquad |B_j|=ah.
   \]

2. The remaining edges form a perfect matching \(M\), every edge of which joins an \(A\)-cycle to a \(B\)-cycle. Call these edges **spokes**.

3. The attachments are periodic in both directions:
   * around each \(A_i\), in a suitable orientation and from a suitable starting point, the indices of the \(B\)-cycles containing its spoke partners are
     \[
     (0,1,\ldots,b-1)^h;
     \]
   * around each \(B_j\), the indices of the \(A\)-cycles containing its spoke partners are
     \[
     (0,1,\ldots,a-1)^h.
     \]

There is no further restriction on which occurrences are joined by the spokes. In particular, every pair \(A_i,B_j\) is joined by exactly \(h\) spokes.

The graph has \(2abh\) vertices.

**Theorem.** Every periodic cycle array is cubic and 3-connected. If
\[
3\mid abh,
\]
then, for every edge \(e\in E(G)\), the graph \(G-e\) has a \(P_3\)-factor.

The construction takes linear time when the displayed decomposition is supplied.

For the divisible-order question, this contains the class in the previous attempt: take
\[
a=d,\qquad b=1,\qquad h=\ell,
\]
with the \(A_i\) as its inner cycles and \(B_0\) as its outer cycle.

## 2. Verification of 3-connectivity

Cubicity is immediate. Contracting the cycles and retaining the spokes gives the complete bipartite multigraph \(K_{a,b}\) with \(h\) parallel edges replacing every edge. Thus \(G\) is connected.

Suppose a nonempty proper vertex set \(S\) has
\[
|\delta_G(S)|\le 2.
\]
A cycle meeting both \(S\) and its complement contributes at least two cut edges. There are consequently two possibilities.

### No cycle is split

Then \(S\) is a union of entire \(A\)- and \(B\)-cycles. Every nontrivial cut in the contracted multigraph has size at least
\[
h\min(a,b)=\min(ah,bh)\ge 3,
\]
a contradiction.

For completeness, selecting \(r\) of the \(A\)-cycles and \(t\) of the \(B\)-cycles gives cut size
\[
h\bigl(r(b-t)+(a-r)t\bigr),
\]
from which this bound follows directly.

### Exactly one cycle is split

It contributes exactly two cut edges, so no spoke crosses the cut. By symmetry, suppose the split cycle is an \(A\)-cycle.

If \(a\ge 2\), choose another \(A\)-cycle. It lies entirely on one side. Since it has spokes to every \(B\)-cycle, and no spoke crosses, all \(B\)-cycles lie on that same side. Every vertex of the allegedly split \(A\)-cycle must then lie on that side as well, a contradiction.

If \(a=1\), membership in \(S\) around \(A_0\) is determined by which whole \(B\)-cycles belong to \(S\). This is a nonconstant binary pattern repeated \(h\) times. It has at least \(2h\) transitions. But
\[
h=ah\ge 3,
\]
so there are at least six cycle edges in the cut, again a contradiction.

Thus \(G\) is 3-edge-connected.

Here 3-edge-connectivity implies 3-vertex-connectivity. Indeed, a cut vertex in a cubic graph would leave a component with at most one boundary edge. If \(\{x,y\}\) were a two-vertex separator, 3-edge-connectivity and degree counting would force exactly two components of \(G-\{x,y\}\), each with three boundary edges, and \(xy\notin E(G)\). Since neither \(x\) nor \(y\) is a cut vertex, each component attaches to both. Adding to one component the separator vertex having two neighbors in it produces a two-edge cut. This is impossible.

## 3. Two elementary tiling lemmas

A path whose order is divisible by three can be partitioned into consecutive \(P_3\)'s. A cycle of such an order can be treated similarly after ignoring one edge.

### Lemma 1: paired transversal

For every positive integer \(m\), one can choose
\[
p_t\in\{2t,2t+1\},\qquad 0\le t<m,
\]
so that the residues \(p_t\bmod m\) are all distinct. Moreover, the choice can satisfy \(p_0=0\).

**Proof.** If \(m\) is odd, choose \(p_t=2t\).

If \(m=2c\), choose
\[
p_t=
\begin{cases}
2t,&0\le t<c,\\
2t+1,&c\le t<2c.
\end{cases}
\]
The first group represents the even residues modulo \(m\), and the second represents the odd residues. ∎

This is the transversal step used in the supplied attempt.

### Lemma 2: two prescribed roots on a cycle

Let \(C\) be a cycle of order \(q\equiv1\pmod3\), and let \(x,y\) be distinct vertices of \(C\). There are vertex-disjoint cycle edges
\[
xx',\qquad yy'
\]
such that every component of
\[
C-\{x,x',y,y'\}
\]
is a path of order divisible by three.

**Proof.** Write
\[
C=z_0z_1\cdots z_{q-1}z_0,\qquad x=z_0,\quad y=z_d,
\]
where \(1\le d\le q-1\). Use the following choices.

| \(d\bmod3\) | First edge | Second edge | Orders of the two remaining gaps |
|---|---|---|---|
| \(0\) | \(z_0z_1\) | \(z_{d-1}z_d\) | \(d-3,\ q-d-1\) |
| \(1\) | \(z_{q-1}z_0\) | \(z_dz_{d+1}\) | \(d-1,\ q-d-3\) |
| \(2\) | \(z_0z_1\) | \(z_dz_{d+1}\) | \(d-2,\ q-d-2\) |

In each row the gap orders are nonnegative multiples of three. The chosen edges are therefore vertex-disjoint and have the required property. Empty gaps are allowed. ∎

The important point is that the roots \(x,y\) can be arbitrary.

## 4. Constructing the factor

Assume \(3\mid abh\).

If both \(ah\) and \(bh\) are divisible by three, tile every cycle independently. Hence suppose that one cycle family has orders not divisible by three.

By exchanging the families if necessary, we may assume
\[
3\mid ah,\qquad 3\nmid bh.
\]
It follows that
\[
3\mid a,\qquad 3\nmid b,\qquad 3\nmid h.
\]
Put
\[
\ell=bh.
\]
Thus every \(B\)-cycle already has order divisible by three, while every \(A\)-cycle has the same nonzero residue \(\ell\bmod3\).

### Case I: \(\ell\equiv2\pmod3\)

Choose a host cycle \(B_0\), and take \(a\) consecutive vertices
\[
x_0,\ldots,x_{a-1}
\]
on it. Periodicity says that their spoke partners lie one in each \(A\)-cycle.

For each \(i\), let \(z_i\) be the spoke partner of \(x_i\), and choose a cycle neighbor \(z_i'\) of \(z_i\). Select
\[
x_i-z_i-z_i'.
\]

These paths are disjoint. In every \(A\)-cycle, deleting the selected adjacent pair leaves a path of order
\[
\ell-2\equiv0\pmod3.
\]
Tile these paths.

The remaining part of \(B_0\) is a path of order
\[
ah-a=a(h-1),
\]
which is divisible by three. Tile it, and tile all the other \(B\)-cycles independently.

### Case II: \(\ell\equiv1\pmod3\) and \(h\ge2\)

Choose a host \(B_0\), and take \(2a\) consecutive vertices
\[
x_0,\ldots,x_{2a-1}.
\]
Split them into pairs
\[
\{x_{2t},x_{2t+1}\},\qquad 0\le t<a.
\]

The sequence of \(A\)-cycle labels is periodic with period \(a\). By Lemma 1, choose one vertex \(x_{p_t}\) from each pair so that their spoke partners lie one in each \(A\)-cycle. Let \(q_t\) denote the other index in that pair, and let \(z_t\) be the spoke partner of \(x_{p_t}\). Select
\[
z_t-x_{p_t}-x_{q_t}.
\]

Each \(A\)-cycle loses one vertex, leaving a path of order
\[
\ell-1\equiv0\pmod3.
\]
The host loses one consecutive block of \(2a\) vertices, leaving a path of order
\[
a(h-2)\equiv0\pmod3.
\]
Tile these paths and all other \(B\)-cycles.

### Case III: \(\ell\equiv1\pmod3\) and \(h=1\)

This is the case requiring two hosts. Here
\[
\ell=b\equiv1\pmod3,\qquad b\ge4,
\]
and every \(B\)-cycle has order \(a\), with \(3\mid a\).

Choose two distinct hosts \(B_0,B_1\). Their attachment orders agree, so write
\[
B_0=x_0x_1\cdots x_{a-1}x_0,\qquad
B_1=y_0y_1\cdots y_{a-1}y_0,
\]
where the spoke partners
\[
z_i\text{ of }x_i,\qquad w_i\text{ of }y_i
\]
both lie in \(A_i\).

Partition the \(A\)-cycles into consecutive triples
\[
(A_{3t},A_{3t+1},A_{3t+2}),\qquad 0\le t<a/3.
\]

For each triple, do the following.

* In \(A_{3t}\), apply Lemma 2 to the distinct roots \(z_{3t},w_{3t}\). Obtain disjoint edges
  \[
  z_{3t}z'_{3t},\qquad w_{3t}w'_{3t}.
  \]
* Select the four paths
  \[
  \begin{aligned}
  &z'_{3t}-z_{3t}-x_{3t},\\
  &w'_{3t}-w_{3t}-y_{3t},\\
  &z_{3t+1}-x_{3t+1}-x_{3t+2},\\
  &w_{3t+2}-y_{3t+2}-y_{3t+1}.
  \end{aligned}
  \]

These paths cover all six corresponding host vertices. They remove four vertices from \(A_{3t}\), one from \(A_{3t+1}\), and one from \(A_{3t+2}\).

By Lemma 2, the remainder of \(A_{3t}\) is tileable. The other two cycles leave paths of order \(b-1\), also tileable.

Doing this for every triple covers both hosts completely. All remaining \(B\)-cycles have order \(a\equiv0\pmod3\), so tile them independently.

This finishes the factor construction in every case.

## 5. Avoiding a prescribed edge

The freedom in these constructions proves the stronger edge-avoidance assertion.

### When all cycles have orders divisible by three

No spoke is used. A prescribed cycle edge can be avoided by using it as the edge at which its cycle is opened before tiling.

### In either one-host construction

These are Cases I and II.

**A prescribed edge in an \(A\)-cycle.** Choose one of its endpoints \(u\), choose as host the \(B\)-cycle containing the spoke partner \(x\) of \(u\), and start the selected host block at \(x\).

* In Case I, choose the other cycle neighbor of \(u\) for the crossing path.
* In Case II, use the transversal of Lemma 1, which selects the first host vertex.

In both cases the prescribed edge is incident with a deleted \(A\)-vertex and is not used.

**A prescribed edge in \(B_j\), or a prescribed spoke incident with \(B_j\).** If \(b\ge2\), use another \(B\)-cycle as host. Then the spoke is unused, and \(B_j\) can be tiled avoiding any specified cycle edge.

If \(b=1\), the selected block is strictly shorter than the host:

* in Case I, \(h=\ell\ge5\), and its length is \(a<ah\);
* in Case II, \(h=\ell\ge4\), and its length is \(2a<ah\).

For a prescribed host edge, start the block immediately after it, so it becomes an unused boundary edge. For a prescribed spoke, choose the block to avoid its host endpoint.

### In the two-host construction

Here \(b\ge4\).

* For an edge in \(B_j\), choose both hosts different from \(B_j\), and tile \(B_j\) avoiding the edge.
* For a spoke incident with \(B_j\), again choose both hosts elsewhere.
* For an edge in \(A_i\), choose one endpoint \(u\), and use the \(B\)-cycle containing its spoke partner as the first host. Rotate the common grouping into triples so that \(A_i\) is a middle cycle \(A_{3t+1}\). The construction then deletes \(u=z_{3t+1}\) singly, so the prescribed edge is unused.

Every edge type is covered. Thus \(G-e\) has a \(P_3\)-factor for every \(e\).

All steps consist of traversing cycles, selecting local paths, and tiling the remaining path intervals, so the construction is linear-time.

## 6. Application to all connected simple \(I\)-graphs

Define
\[
I(N;j,k)
\]
on vertices
\[
\{u_i,v_i:i\in\mathbb Z_N\}
\]
by the edges
\[
u_iu_{i+j},\qquad v_iv_{i+k},\qquad u_iv_i,
\]
where
\[
1\le j,k<N/2.
\]
These restrictions ensure a simple cubic graph.

Connectivity is equivalent to
\[
\gcd(N,j,k)=1:
\]
the possible index changes are generated by \(j,k\), and spokes allow switching between the two layers.

Assume this gcd condition, and set
\[
a=\gcd(N,j),\qquad b=\gcd(N,k).
\]
Then \(\gcd(a,b)=1\), so
\[
h=\frac{N}{ab}
\]
is an integer.

The \(u\)-edges form \(a\) cycles of length \(bh\), indexed by residues modulo \(a\). The \(v\)-edges form \(b\) cycles of length \(ah\), indexed by residues modulo \(b\).

Moreover,
\[
\gcd(j,b)=1,\qquad \gcd(k,a)=1.
\]
Consequently:

* traversing any \(u\)-cycle visits the \(v\)-cycle labels in one common cyclic order, repeated \(h\) times;
* traversing any \(v\)-cycle visits the \(u\)-cycle labels in one common cyclic order, repeated \(h\) times.

After relabelling the two cycle families, these are exactly the periodic cycle-array conditions. Therefore:

**Corollary.** Every connected simple \(I(N;j,k)\) is 3-connected. If \(3\mid N\), then
\[
I(N;j,k)-e
\]
has a \(P_3\)-factor for every edge \(e\).

Generalized Petersen graphs are the subfamily
\[
\operatorname{GP}(N,k)=I(N;1,k).
\]
The corollary also covers cases in which neither layer is a single cycle.

For example, \(I(12;3,4)\) has three \(u\)-cycles of length four and four \(v\)-cycles of length three. It is the two-host case \(a=3,b=4,h=1\). The construction gives the eight paths
\[
\begin{array}{llll}
u_3-u_0-v_0,&u_6-u_9-v_9,&u_4-v_4-v_8,&u_5-v_5-v_1,\\
u_7-u_{10}-u_1,&u_8-u_{11}-u_2,&v_2-v_6-v_{10},&v_3-v_7-v_{11}.
\end{array}
\]
Their vertex sets partition all 24 vertices.

## 7. What remains unresolved

The special-case theorem is complete, including its connectivity and edge-avoidance assertions. It does **not** establish the original conjecture.

The essential extra hypothesis is the periodic two-family decomposition. In a general cubic 3-connected graph, a 2-factor can have unequal cycle lengths and an arbitrary pattern of matching edges between its cycles. There need not be:

* a host cycle with the required repeated attachment order; or
* two host cycles with aligned orders for the exceptional construction.

Thus no decomposition argument for arbitrary cubic 3-connected graphs has been obtained. The unrestricted packing question for orders not divisible by three is also not settled here. No literature novelty claim is made for this constructive special case.