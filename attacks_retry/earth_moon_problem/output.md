```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every biplanar graph obtained by replacing the vertices of an outerplanar graph by nonempty cliques is 9-colourable.",
  "would_publish": false,
  "caveats": "This is a restricted upper bound, not a solution; the general 9–12 gap is unchanged, and neither novelty nor sharpness is claimed."
}
```

# A restricted Earth–Moon theorem

For a graph \(H\) and positive integers \(a_v\), let
\[
B(H;\mathbf a)
\]
be the **clique blowup** obtained by replacing each vertex \(v\) by a clique \(A_v\) of order \(a_v\), with all possible edges between \(A_u\) and \(A_v\) precisely when \(uv\in E(H)\).

The bag sizes need not be equal.

**Theorem.** If \(H\) is outerplanar and \(B(H;\mathbf a)\) is the union of two planar graphs, then
\[
\chi\bigl(B(H;\mathbf a)\bigr)\le 9.
\]

In fact, the proof gives four explicit obstructions accounting for every \(K_9\)-free, ten-chromatic clique blowup of an outerplanar graph.

I use one classical established input:
\[
\theta(K_9)=3.
\tag{1}
\]
Thus every biplanar graph is \(K_9\)-free. This exceptional complete-graph thickness fact is not proved here; importantly, it does **not** follow from the ordinary Euler edge bound.

The triangle-free density argument in the previous attempt is valid and is reproved below. Its constructive forest decomposition is not needed.

## 1. A necessary density condition

**Lemma 1.** If a triangle-free graph \(F\) on \(N\ge3\) vertices is biplanar, then
\[
|E(F)|\le 4N-8.
\tag{2}
\]

**Proof.** Restrict both planar layers to \(E(F)\). Each resulting graph is planar and triangle-free, so has at most \(2N-4\) edges. Summing gives (2). The planar bound also holds for disconnected graphs, since their components can be connected by bridges without introducing triangles. \(\square\)

Consequently, (2) holds for **every triangle-free subgraph** of a biplanar graph.

For a cycle blowup
\[
B=C_\ell[a_0,a_1,\ldots,a_{\ell-1}],\qquad \ell\ge4,
\]
delete all within-bag edges. The resulting subgraph \(T\) is triangle-free and satisfies
\[
|V(T)|=\sum_i a_i,\qquad
|E(T)|=\sum_i a_i a_{i+1},
\tag{3}
\]
where indices are cyclic. Hence biplanarity requires
\[
\sum_i a_i a_{i+1}\le 4\sum_i a_i-8.
\tag{4}
\]

## 2. Exact colouring of weighted cycles

The following elementary formula will locate all possible obstructions.

**Lemma 2.** For positive integer bag sizes:

- If \(\ell\ge4\) is even, then
  \[
  \chi(C_\ell[\mathbf a])=\max_i(a_i+a_{i+1}).
  \tag{5}
  \]
- If \(\ell=2s+1\ge5\), then
  \[
  \chi(C_{2s+1}[\mathbf a])
  =
  \max\left\{
  \max_i(a_i+a_{i+1}),
  \left\lceil\frac{\sum_i a_i}{s}\right\rceil
  \right\}.
  \tag{6}
  \]

**Proof.** Adjacent bags form a clique, giving the first lower bound. In an odd cycle blowup, an independent set meets at most \(s\) bags and takes at most one vertex from each, giving the second.

For an even cycle, put
\[
q=\max_i(a_i+a_{i+1}).
\]
Use the first \(a_i\) colours in alternate bags and the last \(a_i\) colours in the other bags. Adjacent palettes are disjoint, proving (5).

For (6), we prove that \(q\) colours suffice whenever
\[
a_i+a_{i+1}\le q\quad\text{for every }i,
\qquad
\sum_i a_i\le sq.
\tag{7}
\]
Allow zero bag sizes during the proof.

If some bag has size zero, the remaining graph is a disjoint union of path blowups. The alternating first/last-palette construction colours each with \(q\) colours.

Suppose therefore that all bags are nonempty. Not every adjacent sum can equal \(q\): on an odd cycle this would force every \(a_i=q/2\), contradicting \(\sum_i a_i\le sq\). Choose an edge \(e\) with adjacent sum at most \(q-1\).

There is an independent set \(I\) of \(s\) cycle vertices meeting every cycle edge except \(e\), and meeting each of those edges exactly once. Remove one vertex from every bag indexed by \(I\). The new sizes satisfy
\[
a'_i+a'_{i+1}\le q-1,\qquad
\sum_i a'_i\le s(q-1).
\]
Induction on \(q\) colours the remaining graph with \(q-1\) colours. The removed vertices form an independent set and receive one additional colour. This proves (6). \(\square\)

## 3. Four unavoidable ten-colour configurations

Consider these four weighted cycle blowups:
\[
\begin{aligned}
F_1&=C_5[3,4,4,4,4],\\
F_2&=C_5[3,3,5,3,5],\\
F_3&=C_5[3,4,4,3,5],\\
F_4&=C_7[4,4,4,4,4,4,4].
\end{aligned}
\tag{8}
\]

All four have clique number \(8\) and chromatic number \(10\), by Lemma 2.

**Lemma 3.** Every \(K_9\)-free cycle blowup with chromatic number at least \(10\) contains one of \(F_1,F_2,F_3,F_4\) as a subgraph.

**Proof.** A triangle blowup is itself a clique, so is excluded immediately. Even cycle blowups are covered by (5).

Let the cycle length be \(2s+1\ge5\), and write
\[
S=\sum_i a_i.
\]
Since adjacent bags form cliques and the graph is \(K_9\)-free,
\[
a_i+a_{i+1}\le8.
\]
Summing gives
\[
S\le 8s+4.
\tag{9}
\]

If \(s\ge4\), then \(8s+4\le9s\), so Lemma 2 gives a nine-colouring. Thus only lengths five and seven remain.

### Length seven

Here \(s=3\). Requiring ten colours means \(S\ge28\), while (9) gives \(S\le28\). Equality forces every adjacent sum to be \(8\). Since the cycle is odd, every bag has size \(4\). This is \(F_4\).

### Length five

Here ten colours require \(S\ge19\), while \(S\le20\).

If \(S=20\), every bag has size \(4\), and deleting one vertex yields \(F_1\).

Suppose \(S=19\). Define nonnegative integer edge deficits
\[
d_i=8-a_i-a_{i+1}.
\]
Then
\[
\sum_i d_i=40-2S=2.
\tag{10}
\]
Up to rotation and reversal, there are just three possibilities:

1. one deficit equals \(2\);
2. two adjacent deficits equal \(1\);
3. two nonadjacent deficits equal \(1\).

For an odd cycle, the equations \(a_i+a_{i+1}=8-d_i\) uniquely determine the bag sizes. Solving gives, respectively,
\[
(3,3,5,3,5),\qquad
(3,4,4,4,4),\qquad
(3,4,4,3,5).
\]
These are \(F_2,F_1,F_3\). \(\square\)

### Each configuration is non-biplanar

For each \(F_i\), retain only the edges between consecutive bags, as in (3).

| Graph | \(N\) | Inter-bag edges \(M\) | Biplanar bound \(4N-8\) |
|---|---:|---:|---:|
| \(F_1=C_5[3,4,4,4,4]\) | 19 | 72 | 68 |
| \(F_2=C_5[3,3,5,3,5]\) | 19 | 69 | 68 |
| \(F_3=C_5[3,4,4,3,5]\) | 19 | 70 | 68 |
| \(F_4=C_7[4,4,4,4,4,4,4]\) | 28 | 112 | 104 |

Every row violates Lemma 1. Thus all four graphs are non-biplanar.

Combining this with (1) and Lemma 3 proves:

**Corollary.** Every biplanar clique blowup of a cycle is nine-colourable.

The unequal patterns \(F_2\) and \(F_3\) are relevant additions to the uniform-blowup obstruction: their triangle-free subgraphs exceed the biplanar edge bound by only one and two edges, respectively.

## 4. Passing from cycles to outerplanar bases

Two elementary observations finish the theorem.

### Colourings glue across clique separators

Suppose
\[
G=G_1\cup G_2
\]
and \(G_1\cap G_2\) is a clique, with no other edges between the two sides. Then
\[
\chi(G)=\max\{\chi(G_1),\chi(G_2)\}.
\tag{11}
\]

Indeed, colour both sides using the larger palette. Since the shared vertices form a clique, their colours are distinct on each side. A permutation of the colours on \(G_2\) makes the two colourings agree there.

### Outerplanar graphs split into edges and cycles

An outerplanar graph can be decomposed recursively as follows:

- split disconnected graphs into components;
- split at cutvertices;
- in a 2-connected outerplanar graph, the boundary of the outer face is a cycle containing every vertex;
- if that cycle has a chord \(xy\), split along \(xy\) into two smaller outerplanar graphs whose intersection is the edge \(xy\);
- if there is no chord, the graph is a cycle.

The terminal pieces are isolated vertices, edges, and cycles.

Clique blowups respect these decompositions. A shared base vertex becomes a shared clique \(A_x\), and a shared base edge becomes the shared clique
\[
A_x\cup A_y.
\]
Thus every splitting step permits the colouring gluing in (11).

Now suppose \(B(H;\mathbf a)\) is biplanar. Every piece in the decomposition is a subgraph and hence is biplanar.

- Pieces arising from isolated vertices or edges are cliques and have order at most \(8\), by (1).
- Triangle pieces are likewise cliques of order at most \(8\).
- All other cycle pieces are nine-colourable by the preceding corollary.

Repeatedly applying (11) gives
\[
\boxed{\chi(B(H;\mathbf a))\le9}.
\]
This proves the theorem, including disconnected bases and all possible separator cases. \(\square\)

## 5. An exact restricted obstruction statement

The same argument proves a purely chromatic characterization:

> If \(G\) is a \(K_9\)-free clique blowup of an outerplanar graph, then
> \[
> \chi(G)\ge10
> \quad\Longleftrightarrow\quad
> G\text{ contains at least one of }F_1,F_2,F_3,F_4
> \text{ as a subgraph}.
> \]

The forward implication follows from the clique-separator decomposition and Lemma 3. The reverse implication follows because every \(F_i\) is ten-chromatic.

This characterizes the need for a tenth colour **inside this restricted family**. It does not characterize biplanarity: graphs avoiding these four configurations can still be non-biplanar for other reasons.

## 6. What remains open

This argument excludes all clique blowups of outerplanar bases as sources of a ten-colour Earth–Moon example. It allows arbitrary positive bag sizes, rather than only the uniform four-vertex bags treated in the previous attempt.

It does **not** establish that the restricted bound nine is attained, nor that the theorem is new. More importantly, arbitrary biplanar graphs need not have the clique-separator structure used here. There is no reduction of the general problem to this family.

Accordingly, the supplied general bounds
\[
9\le M_2\le12
\]
are unchanged: no ten-chromatic biplanar graph has been constructed here, and no general nine-, ten-, or eleven-colour upper bound has been proved.