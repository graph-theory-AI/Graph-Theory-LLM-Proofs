```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a structural characterization and polynomial-time exact coloring algorithm for even-hole-free graphs with independence number at most three and no induced five-cycle.",
  "would_publish": false,
  "caveats": "The full problem is not resolved, and novelty of this elementary special-case result is not claimed."
}
```

## 1. Result obtained

I do not resolve Coloring on the full even-hole-free class. I pursue the bounded-independence direction from the previous attempt, but do not use its complexity assertions or separator arguments.

The special case settled here is:

> **Corollary.** Exact Coloring is polynomial-time solvable on even-hole-free graphs \(G\) satisfying
> \[
> \alpha(G)\le 3
> \quad\text{and}\quad
> G\text{ contains no induced }C_5.
> \]
> Every nonchordal graph in this class is a clique joined to a clique expansion of \(C_7\).

In fact, this follows from a structural characterization for every independence bound \(r\). All arguments needed for that characterization and its coloring algorithm are given below. This is a proved special case, not a claim that the special case was previously open.

## 2. A structural characterization

A **clique expansion** of a cycle \(C_m\) replaces its vertices by nonempty cliques
\[
Q_0,\ldots,Q_{m-1},
\]
with \(Q_i\) complete to \(Q_{i-1}\cup Q_{i+1}\) and anticomplete to every other bag. Indices are taken modulo \(m\).

The **join** \(G_1\vee G_2\) adds all edges between two disjoint graphs.

### Theorem 1

Let \(r\ge 2\). Suppose that \(G\) satisfies:

1. \(\alpha(G)\le r\);
2. \(G\) has no hole of any length in \(\{4,5,\ldots,2r\}\).

Then either \(G\) is chordal, or
\[
G\cong K_u\vee C_{2r+1}[K_{a_0},\ldots,K_{a_{2r}}],
\]
where \(u\ge0\) and every \(a_i\ge1\).

Conversely, every graph of the displayed form has independence number \(r\), and all its holes have length \(2r+1\).

### Proof

Suppose that \(G\) is not chordal. A hole of length \(\ell\) contains an independent set of size \(\lfloor \ell/2\rfloor\), so every hole has length at most \(2r+1\). By hypothesis, every hole therefore has length exactly
\[
m=2r+1.
\]
Fix one:
\[
C=c_0c_1\cdots c_{m-1}c_0.
\]

#### Step 1: Attachments to \(C\)

We claim that every \(v\notin V(C)\) is either complete to \(C\), or has exactly three consecutive neighbors on \(C\).

First, \(v\) has at least three neighbors on \(C\). Otherwise choose two cycle vertices containing all its neighbors on \(C\). Deleting those two vertices from \(C\) leaves a bipartite graph on \(2r-1\) vertices, hence an independent set of size at least \(r\). Together with \(v\), this contradicts \(\alpha(G)\le r\).

List the neighbors of \(v\) in cyclic order. The lengths of the rim segments between consecutive such neighbors are positive integers summing to \(m\).

Consider a segment of length \(\ell\ge2\). Its interior has no neighbor of \(v\). Since \(v\) has at least three neighbors on \(C\), we have \(\ell\le m-2\), so the segment’s endpoints are nonadjacent. Thus the segment together with \(v\) is a hole of length \(\ell+2\). Every hole has length \(m\), so
\[
\ell=m-2.
\]
The remaining segments consequently have total length two. There must be exactly two of them, both of length one. Thus \(v\) has three consecutive neighbors on \(C\).

If there is no segment of length at least two, all segments have length one, and \(v\) is complete to \(C\). This proves the claim.

Define
\[
U=\{v\notin V(C):v\text{ is complete to }C\}
\]
and
\[
Q_i=\{c_i\}\cup
\{v\notin V(C):N(v)\cap V(C)=\{c_{i-1},c_i,c_{i+1}\}\}.
\]
These sets partition \(V(G)\).

#### Step 2: The bags are cliques, and \(U\) is universal

In a \(C_4\)-free graph, the common neighborhood of two nonadjacent vertices is a clique.

The vertices \(c_{i-1}\) and \(c_{i+1}\) are nonadjacent. Every vertex of \(Q_i\) is adjacent to both, so \(Q_i\) is a clique.

Similarly, \(U\) is a clique: two nonadjacent vertices in \(U\), together with \(c_0,c_2\), would induce a \(C_4\).

Finally, \(U\) is complete to every \(Q_i\). Adjacency to \(c_i\) holds by definition. If \(u\in U\) and \(x\in Q_i\setminus\{c_i\}\) were nonadjacent, then
\[
u,c_{i-1},x,c_{i+1}
\]
would induce a \(C_4\).

#### Step 3: Nonconsecutive bags are anticomplete

Suppose that \(x\in Q_0\), \(y\in Q_d\), and \(xy\in E(G)\), where after reversing and rotating the cycle we may assume
\[
2\le d\le r.
\]
If either \(x\) or \(y\) lies on \(C\), their prescribed cycle neighborhoods already rule out this edge. Thus both are outside \(C\).

If \(d=2\), then
\[
x,y,c_3,c_4,\ldots,c_{m-1},x
\]
is an induced cycle of length \(m-1\), a contradiction.

If \(d\ge3\), then
\[
x,c_1,c_2,\ldots,c_{d-1},y,x
\]
is an induced cycle of length \(d+1\). Here
\[
4\le d+1<m,
\]
again a contradiction. The asserted cycles are induced directly from the prescribed neighborhoods of \(x,y\) on \(C\).

Hence nonconsecutive bags are anticomplete.

#### Step 4: Consecutive bags are complete

Suppose that \(x\in Q_i\), \(y\in Q_{i+1}\), and \(xy\notin E(G)\).

Delete
\[
c_{i-1},c_i,c_{i+1},c_{i+2}
\]
from \(C\). The remaining graph is a path on
\[
m-4=2r-3
\]
vertices, and therefore contains an independent set \(I\) of size \(r-1\). Both \(x\) and \(y\) are anticomplete to this path. Consequently,
\[
I\cup\{x,y\}
\]
is an independent set of size \(r+1\), a contradiction.

Thus consecutive bags are complete. Together with the preceding steps, this proves the required representation.

For the converse, a hole cannot contain a vertex of \(U\), because that vertex would give a chord. Nor can a hole contain two vertices from one bag \(Q_i\): those vertices are adjacent true twins, which cannot both lie on an induced cycle of length at least four. A hole therefore projects to an induced cycle of \(C_m\), so it uses all \(m\) bags and has length \(m\).

Finally, an independent set outside \(U\) uses at most one vertex from each bag and corresponds to an independent set of \(C_m\). Its maximum size is \(r\), and this size is attained. ∎

## 3. Exact coloring of the resulting graphs

The structural theorem reduces the nonchordal case to weighted coloring of an odd cycle. The following formula includes a constructive proof.

### Lemma 2

Let \(r\ge2\), and let \(H\) be a clique expansion of \(C_{2r+1}\), with bag sizes \(a_0,\ldots,a_{2r}\). Then
\[
\boxed{
\chi(H)=
\max\left\{
\max_i(a_i+a_{i+1}),
\left\lceil\frac{\sum_i a_i}{r}\right\rceil
\right\}.
}
\]

An optimal coloring can be constructed in polynomial time in \(|V(H)|\).

### Proof

For the induction, allow some \(a_i\) to be zero, interpreting those bags as empty. Set
\[
A=\sum_i a_i,
\qquad
k=\max\left\{
\max_i(a_i+a_{i+1}),
\left\lceil A/r\right\rceil
\right\}.
\]

Two lower bounds are immediate:

- \(Q_i\cup Q_{i+1}\) is a clique;
- every independent set contains at most \(r\) vertices, so every color class has size at most \(r\).

It remains to construct a coloring with at most \(k\) colors.

If some \(a_i=0\), the nonempty bags form disjoint paths of cliques. Color each path sequentially, choosing for the current bag colors not used on the preceding bag. This succeeds because every adjacent pair has total size at most \(k\). The same palette can be reused on different components.

Now suppose that all \(a_i>0\). There is an edge \(i(i+1)\) of the cycle with
\[
a_i+a_{i+1}\le k-1.
\]
Indeed, if every adjacent sum equaled \(k\), summing these equalities would give
\[
2A=(2r+1)k,
\]
contradicting \(A\le rk\), since \(k>0\).

For any specified edge of an odd cycle, there is an independent set \(S\) of size \(r\) meeting every other edge and missing both endpoints of the specified edge. For example, for the edge \(01\), take
\[
S=\{2,4,\ldots,2r\}.
\]

Remove one vertex from each bag indexed by \(S\). Give these \(r\) vertices one new color. Let \(a'_i\) denote the remaining bag sizes. Every edge other than the specified edge loses exactly one unit of demand, while the specified edge already had demand at most \(k-1\). Hence
\[
a'_i+a'_{i+1}\le k-1
\quad\text{for all }i.
\]
Also,
\[
\sum_i a'_i=A-r\le r(k-1).
\]
By induction on \(A\), the remaining graph has a coloring with at most \(k-1\) colors. Adding the removed independent set gives a coloring with at most \(k\) colors.

Each reduction deletes vertices, and all required choices are explicit. Thus this also gives a polynomial-time construction. ∎

Since a universal clique requires colors disjoint from all other vertices, Theorem 1 yields the formula
\[
\boxed{
\chi(G)=
u+
\max\left\{
\max_i(a_i+a_{i+1}),
\left\lceil\frac{\sum_i a_i}{r}\right\rceil
\right\}
}
\]
in its nonchordal case.

For example, replacing every vertex of \(C_7\) by an \(s\)-vertex clique produces an even-hole-free graph with independence number three and
\[
\omega(G)=2s,
\qquad
\chi(G)=\left\lceil\frac{7s}{3}\right\rceil.
\]
Thus the special case includes nonperfect graphs with unbounded chromatic number and an unbounded additive gap between \(\chi\) and \(\omega\).

## 4. A fully specified polynomial algorithm

Theorem 1 is algorithmic, even when \(r\) is not supplied.

### Finding a hole

For each vertex \(v\) and each nonadjacent pair \(x,y\in N(v)\), search for an \(x\)-\(y\) path in
\[
G\bigl[(V(G)\setminus N[v])\cup\{x,y\}\bigr].
\]
If such a path exists, take a shortest one. It is induced, and adding \(v\) produces a hole.

Conversely, every hole is detected by taking \(v\) on the hole and \(x,y\) to be its two cycle neighbors.

There are \(O(n^3)\) searches. With an adjacency-matrix implementation, this takes \(O(n^5)\) time.

### Coloring

On an input satisfying Theorem 1:

1. **If no hole is found**, the graph is chordal. Find a perfect elimination ordering by repeatedly deleting a simplicial vertex, and color in reverse order. This is optimal: the already colored neighbors of each processed vertex form a clique. The standard simplicial-vertex property of chordal graphs guarantees that the deletion process succeeds.

2. **If a hole \(C\) is found**, its length is \(2r+1\). Classify every other vertex by its neighborhood on \(C\), obtaining \(U,Q_0,\ldots,Q_{2r}\). Theorem 1 guarantees the required structure. Count the bag sizes and apply Lemma 2, assigning additional distinct colors to \(U\).

The simple implementation above takes \(O(n^5)\) time, including construction of an optimal coloring.

### Application to the stated special case

If \(G\) is even-hole-free, \(\alpha(G)\le3\), and \(G\) is \(C_5\)-free, then it has no holes of lengths \(4,5,6\). Theorem 1 applies with \(r=3\).

Thus either \(G\) is chordal, or
\[
G=K_u\vee C_7[K_{a_0},\ldots,K_{a_6}],
\]
in which case
\[
\chi(G)=
u+
\max\left\{
\max_i(a_i+a_{i+1}),
\left\lceil\frac{\sum_{i=0}^{6}a_i}{3}\right\rceil
\right\}.
\]

On a promised even-hole-free input, the additional conditions for this special case can themselves be checked by enumerating independent four-sets and induced five-cycles.

## 5. What remains unresolved

The critical restriction is that a hole must attain the maximum length permitted by the independence bound.

For the \(\alpha(G)\le3\) slice, excluding \(C_5\) forces every hole to be a \(C_7\). The independence bound then forces every external vertex to have at least three neighbors on that hole, and forbidding shorter holes rigidifies those neighborhoods.

If an induced \(C_5\) is present, \(\alpha(G)\le3\) no longer supplies that rigidity. A vertex may have few or no neighbors on the five-cycle without immediately creating an independent four-set. The partition into a universal clique and cycle bags need not exist.

Accordingly:

- this does not settle the \(C_5\)-containing part of the \(\alpha(G)\le3\) slice;
- it does not settle the \(C_5\)-free class with unrestricted independence number;
- it gives neither an exact polynomial-time algorithm nor a hardness result for all even-hole-free graphs.

The structural and coloring arguments above are complete for their stated hypotheses. Their novelty has not been established, and they do not resolve the catalog problem.