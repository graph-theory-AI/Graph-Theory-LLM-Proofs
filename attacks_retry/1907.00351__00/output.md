```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I identify explicit excluded minors on eight and nine vertices, both of treewidth four, and prove that eight is the minimum order of an obstruction of treewidth at most four.",
  "would_publish": false,
  "caveats": "The full excluded-minor set and the planar case are not determined; novelty of these partial results has not been checked."
}
```

# 1. Interpretation and partial results

All graphs below are finite and simple. An orientation has no digons. A vertex colouring of a digraph is **acyclic** if each colour class induces an acyclic digraph.

Write
\[
\mathcal U_2=\{G:\text{every orientation of }G\text{ has an acyclic 2-colouring}\}.
\]
The class in the question is precisely
\[
\mathcal G_2
=\{G:\text{every minor of }G\text{ belongs to }\mathcal U_2\}.
\tag{1}
\]
Indeed, this is minor-closed and contained in \(\mathcal U_2\), and every minor-closed subclass of \(\mathcal U_2\) is contained in it.

I do not determine \(\mathcal G_2\). I prove the following unconditional results.

## Partial theorem

Define two graphs as follows.

* **The eight-vertex graph \(B\):** start with a clique on \(\{0,1,2,3,4\}\), and add three independent vertices \(z_0,z_1,z_2\), where
  \[
  N(z_i)=\{0,1,2,3,4\}\setminus\{i\}.
  \]
* **The nine-vertex graph \(J\):**
  \[
  J=K_3\vee(3K_2),
  \]
  where \(\vee\) denotes the join.

Then:

1. \(B\) and \(J\) are both excluded minors for \(\mathcal G_2\).
2. Both are chordal and have treewidth \(4\).
3. Every graph of treewidth at most \(4\) on at most seven vertices belongs to \(\mathcal G_2\). Thus eight is the minimum order of an obstruction of treewidth at most \(4\).
4. Every graph of treewidth at most \(3\), and every graph with vertex-cover number at most \(4\), belongs to \(\mathcal G_2\). Both numerical thresholds are sharp.
5. For every \(m\ge 0\),
   \[
   K_3\vee(mK_2)\in\mathcal G_2
   \quad\Longleftrightarrow\quad m\le 2.
   \tag{2}
   \]

The treewidth-\(3\) argument in the previous attempt is valid and is reproved below. I do not rely on its claimed minor-minimality of the twelve-vertex graph.

# 2. Elementary tools and positive results

We use four elementary observations.

### Subgraph heredity

The class \(\mathcal U_2\) is closed under taking subgraphs: extend an orientation to the larger graph and restrict an acyclic colouring.

### Inserting a vertex of degree at most three

An acyclic 2-colouring extends over a new vertex having at most three neighbours. One colour occurs on at most one neighbour; assigning that colour to the new vertex cannot create a monochromatic directed cycle.

### Gluing along a clique

Suppose two oriented graphs intersect in a clique, with no edges between their remaining vertices. Acyclic colourings agreeing on the intersection combine to an acyclic colouring.

To see this, fix one colour. Its vertices in the common clique form a transitive tournament. Any directed path in either piece between two common vertices must follow the order of that tournament: a path in the opposite direction would close a directed cycle using the common edge. A directed cycle crossing between pieces would therefore force a cyclic sequence of strict increases in this order.

### Chordal graphs

In an orientation of a chordal graph, every directed cycle contains a directed triangle. Indeed, a shortest directed cycle of length at least four cannot have a chord: either orientation of a chord gives a shorter directed cycle.

Consequently, in an oriented chordal graph, a colouring is acyclic exactly when it has no monochromatic directed triangle.

## 2.1. Treewidth at most three

A \(3\)-degenerate graph can be partitioned into two induced forests. In reverse degeneracy order, give each vertex a colour occurring on at most one already-coloured neighbour. A monochromatic undirected cycle would contradict this rule at its earliest vertex in the degeneracy order.

Every minor of a graph of treewidth at most \(3\) is again of treewidth at most \(3\), and hence \(3\)-degenerate. Therefore
\[
\operatorname{tw}(G)\le 3\implies G\in\mathcal G_2.
\tag{3}
\]

## 2.2. Vertex-cover number at most four

Suppose \(G\) has a vertex cover \(C\) of size at most four. Graphs with fewer than four vertices are immediate; otherwise enlarge \(C\) to size four, complete it to a clique, and extend the orientation arbitrarily.

Every tournament on four vertices has a transitive triple: some vertex has two out-neighbours. Give such a triple colour \(0\). Give the remaining vertex of \(C\), together with \(V(G)\setminus C\), colour \(1\). The latter colour class induces a subgraph of a star.

Vertex-cover number does not increase under minors. Hence
\[
\tau(G)\le4\implies G\in\mathcal G_2.
\tag{4}
\]

# 3. A small join lemma and the seven-vertex boundary

## Lemma 3.1

If \(H\) is a forest with at most five vertices, then
\[
K_3\vee H\in\mathcal U_2.
\]

### Proof

Consider an arbitrary orientation, and let \(C=\{x_0,x_1,x_2\}\) be the central triangle.

If \(C\) is transitive, colour \(C\) with one colour and \(H\) with the other.

Suppose \(C\) is directed cyclically. For a vertex \(v\in V(H)\), there is at most one index \(i\) such that
\[
\{v\}\cup(C\setminus\{x_i\})
\]
is a directed triangle. Call this index the **label** of \(v\), if it exists.

The assertion about labels follows directly by considering the number of out-neighbours of \(v\) in the directed triangle \(C\): it is zero, one, two or three, and in the two nonconstant cases exactly one central edge completes a directed triangle with \(v\).

Since \(|V(H)|\le5\), some label \(i\) occurs at most once. Properly 2-colour the forest \(H\), requiring that vertex, if present, to have colour \(0\). Give \(x_i\) colour \(0\) and the other two central vertices colour \(1\).

The colour-\(0\) graph is a star together with isolated vertices. In colour \(1\), the vertices of \(H\) are independent, and none forms a directed triangle with the central edge. Gluing the corresponding triangles along that edge proves acyclicity. ∎

## Proposition 3.2

Every graph \(G\) with
\[
|V(G)|\le7,\qquad \operatorname{tw}(G)\le4
\]
belongs to \(\mathcal G_2\).

### Proof

It suffices first to prove membership in \(\mathcal U_2\). Add isolated vertices if necessary to obtain seven vertices, and complete to a \(4\)-tree. Here we use the elementary completion property that a graph of treewidth at most \(k\), with at least \(k+1\) vertices, is a subgraph of a \(k\)-tree on the same vertex set.

There are exactly two \(4\)-trees on seven vertices.

After the first added vertex, the graph is \(K_6-xy\). The final vertex has four neighbours forming a clique, so its two non-neighbours must include at least one of \(x,y\).

* If they are \(x,y\), the complement of the resulting graph is a triangle together with four isolated vertices. The graph is \(K_4\vee3K_1\).
* Otherwise the complement is a \(P_4\) together with three isolated vertices. Since \(P_4\) is self-complementary, the graph is \(K_3\vee P_4\).

The first graph is also \(K_3\vee K_{1,3}\). Both are covered by Lemma 3.1.

Every minor of \(G\) still has at most seven vertices and treewidth at most four, so the same argument applies to all its minors. ∎

# 4. An eight-vertex obstruction

Recall the graph \(B\) with core clique \(C=\{0,1,2,3,4\}\) and independent vertices \(z_0,z_1,z_2\), each missing just its indexed core vertex.

It is a \(4\)-tree: start with the core \(K_5\), then attach each \(z_i\) to a \(4\)-clique. Thus
\[
|V(B)|=8,\qquad |E(B)|=22,\qquad \operatorname{tw}(B)=4.
\tag{5}
\]

## 4.1. A non-2-colourable orientation

Orient the core as the regular tournament \(R\):
\[
i\longrightarrow j
\quad\Longleftrightarrow\quad
j-i\pmod5\in\{1,2\}.
\tag{6}
\]
For \(i=0,1,2\), orient the edges incident with \(z_i\) by
\[
z_i\to i+1,\ i+3,
\qquad
i+2,\ i+4\to z_i,
\tag{7}
\]
with indices modulo five.

The only transitive triples in \(R\) are
\[
T_i=\{i,i+1,i+2\},\qquad i\in\mathbb Z_5.
\tag{8}
\]
Indeed, the source of a transitive triple must use both its out-neighbours. Also, \(R\) has no transitive four-set, since every vertex has out-degree two.

Thus an acyclic 2-colouring of the core must have a triple \(T_j\) as one colour class and its complementary pair as the other.

The two directed triangles
\[
z_i\to i+1\to i+2\to z_i,
\qquad
z_i\to i+3\to i+4\to z_i
\]
prevent extending the core partitions with triples \(T_i\) and \(T_{i-2}\). The three leaves therefore exclude, respectively,
\[
\{T_0,T_3\},\qquad
\{T_1,T_4\},\qquad
\{T_2,T_0\}.
\]
All five core partitions are excluded. Hence
\[
B\notin\mathcal U_2.
\tag{9}
\]

Together with Proposition 3.2, this already proves the minimum-order assertion. To prove that \(B\) itself is an excluded minor, edge-minimality remains to be checked.

# 5. Minor-minimality of \(B\)

The proof below is finite and elementary, but some tournament bookkeeping is necessary. All cases are included.

## 5.1. Two easy types of edge deletion

If \(e\) is incident with a leaf \(z_i\), then \(z_i\) has degree three in \(B-e\). Colour \(B-z_i\) using Proposition 3.2 and insert \(z_i\).

Next suppose that \(e=ij\), where \(i,j\in\{0,1,2\}\). Let \(k\) be the third index. Adding the edge \(kz_k\) to \(B-ij\) gives \(K_3\vee P_5\): the three universal vertices are \(k,3,4\), and the remaining path is
\[
z_j-i-z_k-j-z_i.
\]
Lemma 3.1 therefore gives
\[
B-ij\in\mathcal U_2.
\tag{10}
\]

We must handle deletions of the other core edges.

## 5.2. The possible non-2-colourable orientations of \(B\)

We first describe all the information needed about such orientations.

If the core tournament contains a transitive four-set, colour that set with one colour and the remaining core vertex and all leaves with the other. The latter induces a star. Thus the core of a non-2-colourable orientation must have no transitive four-set.

### The three possible core tournaments

Up to isomorphism, there are precisely three tournaments on five vertices without a transitive four-set:

1. \(R\), the regular tournament in (6).
2. \(Q\): a directed triangle \(A=\{0,1,2\}\), together with \(p,q\), oriented
   \[
   A\to p\to q\to A.
   \tag{11}
   \]
3. \(U\): the tournament obtained from \(R\) by reversing \(3\to4\).

Here is a short verification of completeness. Such a tournament has no source or sink. It has at most one vertex of out-degree one: if \(x,y\) both had out-degree one and \(x\to y\), the three in-neighbours of \(y\) would form a transitive triple, giving a transitive four-set. Dually, there is at most one vertex of out-degree three. The degree sequence is therefore either \(2,2,2,2,2\), or \(1,2,2,2,3\).

The regular tournament on five vertices is uniquely determined by its degrees, giving \(R\). In the second case let \(p\) have out-degree one and \(q\) out-degree three.

* If \(p\to q\), the other three vertices form a directed triangle and we obtain \(Q\).
* If \(q\to p\), let \(a\) be the sole out-neighbour of \(p\), and \(b\) the sole in-neighbour of \(q\). Avoiding a transitive four-set forces \(a\ne b\). If \(c\) is the remaining vertex, the out-neighbourhood of \(q\) and the in-neighbourhood of \(p\) must each be cyclic; these conditions, followed by the degree condition at \(a\), force
  \[
  a\to c\to b,\qquad a\to b.
  \]
  This is \(U\), with \(p=3,q=4,a=0,c=1,b=2\).

### What can a leaf forbid?

After relabelling the core, let \(I\) denote the three core vertices omitted from leaf neighbourhoods, and call the corresponding leaves \(z_i\), \(i\in I\).

A core acyclic 2-colouring has parts of sizes two and three. A leaf can fail to extend it only when its omitted vertex lies in the triple. Its four neighbours then split into two monochromatic pairs, and extension fails precisely when the leaf forms a directed triangle with each pair.

Moreover, a leaf can forbid at most one perfect matching of its four neighbours. If it formed directed triangles with the pairs of two different perfect matchings, their union would force all arcs between two pairs of core vertices in the same direction. Those four core vertices would then be transitive, a contradiction.

For \(R\), the nonempty sets of core partitions that a leaf \(z_i\) can forbid are
\[
\{T_i,T_{i-2}\}\quad\text{or}\quad\{T_{i-1}\}.
\tag{12}
\]
Up to rotating the indices, the omitted set \(I\) is either \(\{0,1,2\}\) or \(\{0,1,3\}\). Covering all five partitions forces:

* \(I=\{0,1,2\}\): all three leaves use the two-element option in (12);
* \(I=\{0,1,3\}\): \(z_0,z_1\) use the two-element option and \(z_3\) forbids \(T_2\).

For \(Q\), the six core partitions have triples
\[
(A\setminus\{x\})\cup\{p\},
\qquad
(A\setminus\{x\})\cup\{q\},
\qquad x\in A.
\]
A leaf omitting \(p\) or \(q\) can exclude at most one of these partitions; a leaf omitting a vertex of \(A\) can exclude at most two. Covering all six therefore forces \(I=A\). Each leaf must use a matching pairing one vertex of \(A\) with \(p\) and the other with \(q\). In particular,
\[
p\to z_i\to q\qquad(i\in A).
\tag{13}
\]

For \(U\), its transitive triples are \(T_0,\ldots,T_4\), together with
\[
T_*=\{1,3,4\}.
\]
The possible nonempty forbidden sets are:

| Omitted vertex \(i\) | Possible forbidden sets |
|---|---|
| \(0\) | \(\{T_0,T_3\}\), \(\{T_4\}\) |
| \(1\) | \(\{T_0,T_*\}\), \(\{T_1,T_4\}\) |
| \(2\) | \(\{T_0,T_2\}\), \(\{T_1\}\) |
| \(3\) | \(\{T_1,T_3\}\), \(\{T_2\}\), \(\{T_*\}\) |
| \(4\) | \(\{T_2,T_4\}\), \(\{T_3\}\), \(\{T_*\}\) |

To cover six partitions with three leaves, each must exclude two. The only two-element set containing \(T_*\) comes from \(z_1\); the remaining four partitions then force \(z_3,z_4\). Thus
\[
I=\{1,3,4\},
\]
with forbidden sets \(\{T_0,T_*\},\{T_1,T_3\},\{T_2,T_4\}\).

A forbidden matching fixes all four incident leaf arcs. We have therefore obtained the following necessary forms for every non-2-colourable orientation of \(B\):

| Form | Core | Omitted set \(I\) | Leaf out-neighbours in the core |
|---|---|---|---|
| \(R_1\) | \(R\) | \(\{0,1,2\}\) | \(N^+(z_i)=\{i+1,i+3\}\) |
| \(R_2\) | \(R\) | \(\{0,1,3\}\) | \(z_0:\{1,3\};\ z_1:\{2,4\};\ z_3:\{0,2\}\) |
| \(Q\) | (11) | \(A\) | \(p\to z_i\to q\); the other arcs are not needed below |
| \(U_1\) | \(U\) | \(\{1,3,4\}\) | \(z_1:\{0,4\};\ z_3:\{1,4\};\ z_4:\{0,2\}\) |

The chordality observation ensures that excluding all core partitions is exactly the obstruction: if every leaf extends a chosen core partition, those choices combine without creating a new directed cycle.

## 5.3. Deleting any remaining core edge

Take an arbitrary orientation of \(B-e\), where \(e\) is a core edge, and orient \(e\) arbitrarily to obtain \(D\).

If \(D\) is 2-colourable, we are done. Otherwise \(D\) has one of the forms just listed.

Whenever deleting \(e\) leaves an acyclic four-set in the core, colour that set with one colour and the remaining core vertex and all leaves with the other. Thus only the following core edges need further attention:

| Core | Edges potentially needing further attention |
|---|---|
| \(R\) | \(i(i+1)\), \(i\in\mathbb Z_5\) |
| \(Q\) | \(ip,iq\), \(i\in A\) |
| \(U\) | \(34,04,23\) |

For completeness, the acyclic-four-set assertion can be checked as follows.

* In \(R\), deleting \(i(i+2)\) leaves the acyclic order
  \[
  i+2,\ i+3,\ i+4,\ i.
  \]
* In \(Q\), deleting an edge of the directed triangle makes \(A\), together with \(q\), acyclic. Deleting \(pq\) leaves \(q\), any two vertices of \(A\), and \(p\), in that order.
* In \(U\), the other seven edges have the following acyclic four-vertex orders after deletion:
  \[
  \begin{array}{c|c}
  e&\text{order}\\ \hline
  02&(2,4,3,0)\\
  13&(4,3,0,1)\\
  24&(4,0,1,2)\\
  03&(0,1,2,3)\\
  14&(1,2,4,3)\\
  01&(4,1,3,0)\\
  12&(2,4,1,3)
  \end{array}
  \]

Edges with both ends in \(I\) were already handled in (10). All remaining cases for \(R_1,R_2,U_1\) are certified in the next table. Each column lists one colour class in topological order.

| Form | Deleted edge | First colour class, in order | Second colour class, in order |
|---|---|---|---|
| \(R_1\) | \(23\) | \(1,3,z_1,2\) | \(4,z_0,z_2,0\) |
| \(R_1\) | \(04\) | \(0,z_1,4,1\) | \(2,z_0,z_2,3\) |
| \(R_1\) | \(34\) | \(0,1,z_1,2\) | \(4,z_0,z_2,3\) |
| \(R_2\) | \(12\) | \(0,2,z_0,1\) | \(3,z_1,4,z_3\) |
| \(R_2\) | \(23\) | \(1,3,z_1,2\) | \(4,z_0,z_3,0\) |
| \(R_2\) | \(34\) | \(4,z_0,3,0\) | \(1,z_1,z_3,2\) |
| \(R_2\) | \(04\) | \(0,z_1,4,1\) | \(z_3,2,z_0,3\) |
| \(U_1\) | \(04\) | \(1,2,3,z_1\) | \(z_4,0,z_3,4\) |
| \(U_1\) | \(23\) | \(z_1,4,0,1\) | \(3,z_4,2,z_3\) |

These are direct certificates: every arc within a displayed colour class points from left to right.

Finally consider form \(Q\). If the deleted edge is \(ip\), use
\[
\{i,p,q,z_i\}
\]
as one colour class, in the order
\[
p,z_i,q,i.
\]
If the deleted edge is \(iq\), use the same class in the order
\[
i,p,z_i,q.
\]
In either case the other colour class consists of the two remaining vertices of \(A\) and their two leaves; its underlying graph is a path.

This covers every edge and proves
\[
B-e\in\mathcal U_2\qquad(e\in E(B)).
\tag{14}
\]

## 5.4. All proper minors

Every proper minor of \(B\) with fewer than eight vertices belongs to \(\mathcal G_2\) by Proposition 3.2. A proper minor retaining eight vertices is a proper spanning subgraph, and is covered by (14) and subgraph heredity.

Thus every proper minor of \(B\) belongs to \(\mathcal U_2\), and hence to \(\mathcal G_2\). Together with (9),
\[
\boxed{B\in\operatorname{Ex}_m(\mathcal G_2).}
\tag{15}
\]

Also \(\tau(B)=5\). The core itself is a vertex cover of size five. A cover of size four would have to use four core vertices to cover the \(K_5\), leaving an edge from the omitted core vertex to a leaf uncovered. This proves sharpness of (4), while (5) proves sharpness of (3).

# 6. A nine-vertex excluded minor

Let
\[
J=K_3\vee(3K_2).
\]
Write its central triangle as \(C=\{x_0,x_1,x_2\}\), and its three private pairs as \(P_0,P_1,P_2\). Each \(C\cup P_i\) induces a \(K_5\). These three cliques meet exactly in \(C\).

The graph is chordal and has treewidth four.

## 6.1. A bad orientation

Orient
\[
x_0\to x_1\to x_2\to x_0.
\]
For each \(i\), write \(P_i=\{a_i,b_i\}\), and orient the block \(C\cup P_i\) as follows:
\[
x_{i+1}\to x_{i+2},
\]
\[
x_{i+2}\to x_i,a_i,b_i,
\qquad
x_i,a_i,b_i\to x_{i+1},
\]
and
\[
x_i\to a_i\to b_i\to x_i.
\tag{16}
\]
The three block orientations agree on the central triangle.

In an acyclic 2-colouring, \(x_{i+1}\) and \(x_{i+2}\) cannot have the same colour. If they did, their directed triangles with each of \(x_i,a_i,b_i\) would force those three vertices to the other colour, making their directed triangle monochromatic.

Thus all three edges of the central triangle would have differently coloured ends, which is impossible. Hence
\[
J\notin\mathcal U_2.
\tag{17}
\]

## 6.2. Extensions across a \(K_5\) with a prescribed central triangle

We need two observations.

### Observation A

For any orientation of a \(K_5\) containing a specified cyclic triangle \(C\), at most one of the three acyclic 2-colour patterns on \(C\), up to swapping colours, fails to extend.

To prove this, consider the pattern in which \(x_i\) alone has colour \(0\). A private vertex is forced to colour \(0\) exactly when it forms a directed triangle with \(C\setminus\{x_i\}\). As in Lemma 3.1, each private vertex has at most one such label.

Unless both private vertices have label \(i\), they can be given different colours respecting these restrictions. If both have label \(i\), failure occurs only when they and \(x_i\) form a directed triangle. Thus at most one central pattern fails.

A block of order at most four containing \(C\) extends every central pattern: give its possible private vertex the singleton colour.

### Observation B

Deleting any edge outside \(C\) from this \(K_5\) makes every central pattern extend, regardless of orientation.

For a prescribed pattern \(x_i\) of colour \(0\), the other two central vertices of colour \(1\):

* If the deleted edge is the private edge, give both private vertices colour \(0\).
* If it joins \(x_i\) to a private vertex, again give both private vertices colour \(0\).
* If it joins one of the other central vertices to a private vertex \(a\), give \(a\) colour \(1\) and the other private vertex colour \(0\).

In every case both resulting colour classes induce forests.

## 6.3. Edge deletions

If a central edge is deleted, colour all central vertices \(0\), and all private vertices \(1\). Both induced underlying graphs are forests.

Otherwise exactly one \(K_5\) block is damaged.

If the central triangle is transitive, colour it \(0\) and all private vertices \(1\). If it is cyclic, the two intact blocks exclude at most two of its three patterns by Observation A, and the damaged block extends every pattern by Observation B. Choose an unexcluded pattern and glue the local colourings along \(C\).

Therefore
\[
J-e\in\mathcal U_2\qquad(e\in E(J)).
\tag{18}
\]

## 6.4. Contraction quotients

Consider any nontrivial pure contraction quotient of \(J\), before deletions, and examine the images of the three central vertices.

The images of the original blocks remain cliques. Off the central images, vertices from different blocks remain disjoint and nonadjacent: a connected branch set meeting two different private pairs must contain a central vertex.

* **Three distinct central images.** The quotient consists of cliques of order at most five sharing the central triangle. At least one block has shrunk, so at most two blocks have order five. If the central triangle is transitive, colour it uniformly and all off-centre vertices oppositely. If it is cyclic, Observation A leaves an available pattern, and every smaller block extends it.
* **Two distinct central images.** Every block has order at most four, and all blocks share the central edge. Colour its ends differently. Each block extends this by putting at most one further vertex in each colour.
* **One central image.** Every block has order at most three. Give the common vertex one colour and all off-centre vertices the other.

Clique gluing proves acyclicity in all cases.

Every minor can be obtained by first contracting its connected branch sets and then deleting edges and vertices. Thus (18), the contraction argument, and subgraph heredity show that every proper minor of \(J\) belongs to \(\mathcal U_2\). Consequently,
\[
\boxed{J\in\operatorname{Ex}_m(\mathcal G_2).}
\tag{19}
\]

Equation (2) now follows: for \(m\le2\), the graph has at most seven vertices and treewidth at most four; for \(m\ge3\), it contains \(J\).

# 7. Consequences and the remaining gap

The proved bounds include
\[
\boxed{
\{G:\operatorname{tw}(G)\le3\}
\ \cup\
\{G:\tau(G)\le4\}
\ \subseteq\
\mathcal G_2
\ \subseteq\
\operatorname{Forb}_m(B,J,K_7).
}
\tag{20}
\]

For the last obstruction, no literature input is needed. A bad orientation of \(K_7\) consists of two directed triangles \(A,B\) and one vertex \(v\), with
\[
A\to B\to v\to A.
\]
Both colours must occur in each of \(A,B\); whichever colour \(v\) receives produces a monochromatic directed triangle through \(v\).

The results above establish, in particular:

* a genuine excluded minor on eight vertices, rather than merely an order-minimal bad orientation;
* another excluded minor of a different clique-sum type on nine vertices;
* the exact minimum obstruction order within treewidth at most four;
* sharp unconditional guarantees in terms of both treewidth and vertex-cover number.

They do **not** identify the full excluded-minor set. In particular, nothing here proves that the right-hand containment in (20) is an equality. Nor does the argument settle whether every planar graph belongs to \(\mathcal G_2\): that statement is equivalent to the planar dichromatic two-colour conjecture, since planar graphs are minor-closed.

No planar conjecture has been assumed, and no unverified literature claim is used in the proofs above.