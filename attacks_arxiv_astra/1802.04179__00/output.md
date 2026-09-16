```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The candidate bound 3 holds for every graph in this planar class whose 3-core is claw-free, but the unrestricted extremal constant is not determined.",
  "would_publish": false,
  "caveats": "No improved general bound is obtained, and no novelty is claimed for the special case."
}
```

## 1. Interpretation and result

Let \(\mathcal P\) be the class of finite simple planar graphs containing no cycles of length \(4\) or \(5\). Following the catalog’s clarification, the intended quantity is
\[
c_*=\sup_{G\in\mathcal P}\chi_f(G)
=\inf\{c:\chi_f(G)\le c\text{ for every }G\in\mathcal P\}.
\]
It is not the literal infimum of the individual fractional chromatic numbers.

The triangle gives \(c_*\ge3\). Taking the later upper bound reported in the question as given, the interval is \(3\le c_*\le7/2\). I have not independently verified the 2025 bibliographic claims, and the argument below does not use them.

Here is a special case in which the candidate value \(3\) can be established.

**Theorem.** Let \(G\in\mathcal P\). If the \(3\)-core of \(G\) is claw-free, then
\[
\chi_f(G)\le3.
\]
Consequently, the supremum restricted to this subclass is exactly \(3\).

The \(3\)-core is obtained by repeatedly deleting vertices of degree at most two. A graph is claw-free if it has no induced \(K_{1,3}\).

I also obtain the following necessary conditions for an obstruction to the candidate bound \(3\).

**Proposition.** If some graph in \(\mathcal P\) has fractional chromatic number greater than \(3\), then a vertex-minimal such graph:

1. has minimum degree at least three;
2. has no clique cutset, and every triangle bounds a face;
3. contains an induced claw;
4. has at least twelve degree-three vertices incident with triangular faces.

The main theorem follows from a line-graph representation and the classical matching-polytope theorem.

## 2. A line-graph representation

**Lemma 1.** Every claw-free \(G\in\mathcal P\) is the line graph of a simple planar graph \(H\) with maximum degree at most three and no cycles of length less than six.

### Proof

First observe that, for every \(v\in V(G)\), the graph \(G[N(v)]\) is a matching together with isolated vertices. Indeed, a path \(a b c\) in \(G[N(v)]\) would give the \(4\)-cycle
\[
v a b c v.
\]

Because \(G\) is claw-free, \(G[N(v)]\) has at most two components: choosing one vertex from each of three components would give three pairwise nonadjacent neighbors of \(v\).

Let \(\mathcal K\) consist of all triangles and all edges not belonging to a triangle. These are exactly the maximal cliques of \(G\) having at least two vertices. Every edge belongs to exactly one member of \(\mathcal K\): two distinct triangles sharing an edge would produce a \(4\)-cycle.

The neighborhood observation shows that every nonisolated vertex belongs to one or two members of \(\mathcal K\).

Construct \(H\) as follows:

- introduce a vertex \(q_K\) for every \(K\in\mathcal K\);
- if \(v\in V(G)\) belongs to two members \(K,L\), introduce the edge \(q_Kq_L\), labeled \(v\);
- if \(v\) belongs to only one member \(K\), introduce an edge from \(q_K\) to a new private leaf, labeled \(v\);
- represent each isolated vertex of \(G\) by a separate component \(K_2\).

Distinct members of \(\mathcal K\) intersect in at most one vertex. Hence \(H\) has neither loops nor parallel edges. Also,
\[
d_H(q_K)=|K|\le3.
\]
Two edges of \(H\) meet precisely when their labels are adjacent in \(G\), so
\[
G=L(H).
\]

It remains to check planarity and girth.

### Planarity

Fix a plane embedding of \(G\). At a vertex belonging to two cliques, the incident edges belonging to each clique occur consecutively in the cyclic order.

The only potentially problematic case is a degree-four vertex \(v\) belonging to two triangles \(vab\) and \(vcd\). Their edge pairs cannot alternate around \(v\): otherwise \(c\) and \(d\) would lie on opposite sides of the Jordan curve \(vabv\), forcing \(cd\) to cross that curve.

We may therefore split every vertex belonging to two cliques into two adjacent vertices, assigning one clique to each. At a vertex belonging to only one clique, attach a private leaf. These are planar operations.

After the splitting, the subgraphs representing distinct members of \(\mathcal K\) are vertex-disjoint. Contract each of them to one vertex, discarding the loops produced by contracting triangles. The resulting graph is precisely \(H\), apart from the separately handled isolated vertices of \(G\). Thus \(H\) is planar.

### Girth

Suppose \(H\) had a triangle. Its three edges would correspond to a triangle of \(G\). Each pair of those three vertices would belong to the clique represented by their common endpoint in \(H\). Uniqueness of the clique containing an edge of \(G\) would force all three endpoints of the supposed triangle in \(H\) to represent the same clique, a contradiction.

A cycle of length four or five in \(H\) gives a cycle of the same length in \(L(H)=G\), by taking its edges in cyclic order. Thus \(H\) has no such cycle either. ∎

## 3. Fractionally coloring the line graph with three colors

**Lemma 2.** If \(H\) is a simple planar graph of maximum degree at most three and girth at least six, then
\[
\chi_f(L(H))\le3.
\]

### Proof

Write \(E_H(S)\) for the edges of \(H\) with both endpoints in \(S\).

We first establish that every nonempty \(S\subseteq V(H)\) satisfies
\[
|E_H(S)|\le \frac32(|S|-1). \tag{1}
\]

Consider each connected component \(J\) of \(H[S]\).

- If \(J\) is a tree, then
  \[
  |E(J)|=|V(J)|-1.
  \]
- If \(J\) contains a cycle, Euler’s formula and girth at least six give
  \[
  |E(J)|\le\frac32(|V(J)|-2).
  \]

In either case,
\[
|E(J)|\le\frac32(|V(J)|-1).
\]
Summing over components proves (1), including components consisting of single vertices.

Now use the classical matching-polytope theorem. It states that the convex hull of the incidence vectors of matchings of \(H\) is defined by
\[
x_e\ge0,
\qquad
\sum_{e\ni v}x_e\le1,
\]
and
\[
\sum_{e\in E_H(S)}x_e\le\frac{|S|-1}{2}
\quad\text{for every odd-cardinality }S\subseteq V(H).
\]

Set
\[
x_e=\frac13\qquad(e\in E(H)).
\]
The vertex constraints follow from \(\Delta(H)\le3\). The odd-set constraints follow from (1):
\[
\sum_{e\in E_H(S)}x_e
=\frac{|E_H(S)|}{3}
\le\frac{|S|-1}{2}.
\]

Consequently, there are matchings \(M_1,\ldots,M_r\) and coefficients \(p_i\ge0\), with \(\sum_i p_i=1\), such that
\[
\sum_{i:e\in M_i}p_i=\frac13
\quad\text{for every }e\in E(H).
\]

Each matching \(M_i\) is an independent set in \(L(H)\). Assigning fractional-color weight \(3p_i\) to that independent set gives total weight three and covers each vertex with weight exactly one. Hence
\[
\chi_f(L(H))\le3.
\]
∎

Combining Lemmas 1 and 2 proves
\[
\chi_f(G)\le3
\quad\text{for every claw-free }G\in\mathcal P. \tag{2}
\]

This argument handles arbitrary vertex weights, not merely the unweighted independence ratio.

## 4. Extending from the \(3\)-core

We now prove the stated theorem.

Let \(C\) be the \(3\)-core of \(G\). If \(C\) is claw-free, (2) gives \(\chi_f(C)\le3\).

For a finite graph, a fractional coloring can be chosen rational. Thus, for some positive integer \(b\), \(C\) has a \((3b:b)\)-coloring. This also follows directly by choosing rational coefficients in the matching-polytope decomposition and clearing denominators.

Insert the deleted vertices in reverse deletion order. At the moment a vertex is inserted, it has at most two already colored neighbors. Their assigned sets forbid at most \(2b\) of the \(3b\) colors, leaving at least \(b\) available colors. Assign any \(b\) of them to the new vertex.

This produces a \((3b:b)\)-coloring of \(G\). If the core is empty, the same argument starts with \(b=1\). Therefore
\[
\chi_f(G)\le3.
\]

Finally, \(K_3\) belongs to this subclass and has fractional chromatic number three, so the restricted supremum is exactly three. ∎

No fixed bound on the denominator \(b\) is claimed.

## 5. Necessary structure of a counterexample to the bound \(3\)

Suppose \(G\in\mathcal P\) is vertex-minimal subject to \(\chi_f(G)>3\).

### Minimum degree and clique cutsets

The extension argument above immediately gives
\[
\delta(G)\ge3.
\]

Fractional \(3\)-colorings also glue across clique cutsets. To see this, suppose \(G=G_1\cup G_2\), where \(G_1,G_2\) are proper induced subgraphs, their intersection is a clique \(K\), and there are no edges between their exclusive vertex sets.

By minimality, both graphs admit \((3b:b)\)-colorings after passing to a common denominator. The color sets on the vertices of \(K\) are pairwise disjoint. A permutation of the palette on \(G_2\) can make these sets agree with those on \(G_1\). The two colorings then combine.

Thus \(G\) has no clique cutset. In particular, it is connected and has no cutvertex, hence is \(2\)-connected.

A triangle with vertices on both sides would be a clique cutset. Therefore every triangle bounds a face in a plane embedding of \(G\).

Since \(G\) is its own \(3\)-core, the main theorem also implies that \(G\) contains an induced claw.

### At least twelve triangular degree-three vertices

Fix a plane embedding. Let \(n,m,f\) denote the numbers of vertices, edges, and faces, and let \(t\) be the number of triangular faces. Because \(G\) is \(2\)-connected, every face boundary is a cycle, so each nontriangular face has length at least six.

Define the nonnegative face excess
\[
\eta=\sum_{\substack{F\text{ a face}\\ |F|\ge6}}(|F|-6).
\]
Counting edge-sides gives
\[
2m=3t+6(f-t)+\eta.
\]
Using Euler’s formula yields
\[
6n-4m+3t=12+\eta. \tag{3}
\]

For a vertex \(v\), let \(r(v)\) be the number of incident triangular faces. Triangles cannot share an edge, so
\[
r(v)\le\left\lfloor\frac{d(v)}2\right\rfloor.
\]
Equation (3) becomes
\[
\sum_{v\in V(G)}\bigl(6-2d(v)+r(v)\bigr)=12+\eta. \tag{4}
\]

Since \(\delta(G)\ge3\):

- a degree-three vertex contributes \(1\) if it is incident with a triangular face, and \(0\) otherwise;
- a vertex of degree at least four contributes at most \(0\).

If \(a\) is the number of degree-three vertices incident with triangular faces, (4) therefore gives
\[
a\ge12+\eta\ge12.
\]

This proves all four assertions of the proposition. ∎

## 6. What remains unresolved

The line-graph argument depends essentially on claw-freeness. In this class, a claw-free vertex belongs to at most two maximal cliques, so it can be represented by an edge of \(H\). An induced-claw center belongs to at least three maximal cliques, and that representation is no longer available. The matching-polytope proof does not establish the required fractional coloring for those graphs.

Thus the argument:

- proves the candidate value \(3\) for the claw-free-\(3\)-core subclass;
- gives structural restrictions on any example with \(\chi_f>3\);
- does **not** prove \(\chi_f\le3\) for all of \(\mathcal P\);
- does **not** construct a graph in \(\mathcal P\) with \(\chi_f>3\);
- does **not** improve the reported general upper bound \(7/2\).

The unrestricted determination of \(c_*\) is therefore left open here.