```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the sharp bound 16 for planar graphs of treewidth at most three, with an explicit 540-vertex example, but do not determine the unrestricted planar maximum.",
  "would_publish": false,
  "caveats": "The supplied interval [18,80] is unchanged; novelty of the subclass result is not claimed."
}
```

# Result and scope

Write \(\underline D\) for the underlying undirected graph of an oriented graph \(D\).

I prove the following special case completely.

## Theorem
\[
\max_{\operatorname{tw}(\underline D)\le 3}\chi_o(D)
=
\max_{\substack{\underline D\text{ planar}\\
                 \operatorname{tw}(\underline D)\le 3}}\chi_o(D)
=16.
\]
An explicit planar example attaining \(16\) has \(540\) vertices.

Thus the upper bound holds even without planarity, while sharpness already holds for planar graphs. This does **not** improve the interval \(18\le M\le80\) supplied for unrestricted planar graphs.

The seven-vertex tournament and fan used below also appeared in the previous attempt. I verify their needed properties here. I do not use that attempt’s obstruction concerning the \(80\)-label construction.

Throughout, an oriented colouring is a homomorphism to a tournament. In particular, adjacent vertices, and the endpoints of a directed two-edge path, must receive different colours.

# 1. A seven-vertex tournament

Let \(Q\) be the tournament on \(\mathbb Z_7\) defined by
\[
x\to y \quad\Longleftrightarrow\quad y-x\in\{1,2,4\}.
\]

We will need four elementary properties.

### (Q1) Every in- and out-neighbourhood is a directed triangle

Translations are automorphisms, so it suffices to inspect \(0\):
\[
N^+(0)=\{1,2,4\},\qquad N^-(0)=\{3,5,6\}.
\]
Their cyclic orientations are
\[
1\to2\to4\to1,\qquad 3\to5\to6\to3.
\]
In particular, \(Q\) has no transitive four-vertex subtournament.

Also, \(Q\) is isomorphic to its converse, by negating the vertex labels.

### (Q2) A reversing matching between the two neighbourhoods

For a vertex \(v\), put \(I=N^-(v)\) and \(O=N^+(v)\). The arcs from \(I\) to \(O\) form a perfect matching. Its bijection \(I\to O\) reverses cyclic order.

At \(v=0\), the matching is
\[
3\to4,\qquad 5\to2,\qquad 6\to1.
\]
The cyclic order \(3,5,6\) is sent to \(4,2,1\), which is the reverse of the cyclic order on \(O\).

Here and below, a bijection between directed triangles *reverses cyclic order* if \(a\to b\) implies that the image of \(b\) points to the image of \(a\).

### (Q3) The complement of a directed triangle

Deleting any directed triangle from \(Q\) leaves a directed triangle together with either a source or a sink.

Indeed, \(Q\) has
\[
\binom73-7\binom32=14
\]
directed triangles. They are precisely the translates of
\[
\{0,1,3\}\quad\text{and}\quad\{0,1,5\}.
\]
For the first representative, the remaining vertices are
\[
\{2,4,5,6\},
\]
where \(2,4,5\) form a directed triangle and \(6\) is a sink. For the second, the remaining vertices are
\[
\{2,3,4,6\},
\]
where \(3,4,6\) form a directed triangle and \(2\) is a source.

### (Q4) Uniqueness among seven-vertex tournaments without a transitive four-set

Suppose a tournament \(R\) on seven vertices has no transitive four-vertex subtournament.

Every tournament on four vertices contains a transitive triple: some vertex has at least two out-neighbours. Consequently every vertex of \(R\) has in- and outdegree at most three. Both degrees therefore equal three, and both neighbourhoods must be directed triangles.

Fix \(v\), with in-triangle \(I\) and out-triangle \(O\). Degree counting shows that the arcs from \(I\) to \(O\) form a perfect matching. This matching cannot preserve cyclic order. To see this, label the triangles cyclically as
\[
i_0\to i_1\to i_2\to i_0,\qquad
o_0\to o_1\to o_2\to o_0,
\]
and suppose the matching is \(i_j\to o_j\). Then
\[
N^+(o_0)=\{o_1,i_1,i_2\}
\]
is transitive, a contradiction.

The matching therefore reverses cyclic order. Up to relabelling, this uniquely specifies the tournament, and (Q2) identifies it as \(Q\).

# 2. A 16-vertex target for every partial \(3\)-tree

A \(3\)-tree can be constructed from a triangle by repeatedly adding a vertex adjacent to all three vertices of an existing triangle. A partial \(3\)-tree is a subgraph of a \(3\)-tree; equivalently, it has treewidth at most three.

## 2.1. The target

First form a tournament \(R\) on
\[
\{\infty\}\cup\mathbb Z_7
\]
by taking \(Q\) and making \(\infty\) a source.

Define an oriented graph \(H\) with vertices
\[
V(H)=\{(x,\varepsilon):x\in V(R),\ \varepsilon\in\{0,1\}\}.
\]
There is no edge between \((x,0)\) and \((x,1)\). For \(x\ne y\):

- if \(\varepsilon=\delta\), the direction between \((x,\varepsilon)\) and \((y,\delta)\) agrees with the direction between \(x,y\) in \(R\);
- if \(\varepsilon\ne\delta\), that direction is reversed.

Thus \(H\) has \(16\) vertices. Completing its eight missing edges arbitrarily gives a tournament, so a homomorphism to \(H\) is an oriented \(16\)-colouring.

## 2.2. The required extension property

**Claim.** Given three pairwise adjacent vertices of \(H\), every prescription of the three directions between them and a new vertex is realized by some vertex of \(H\).

Pairwise adjacent vertices have distinct first coordinates. Start with three vertices whose second coordinates are all zero. For an unused first coordinate \(w\), record a three-bit word, with bit \(i\) equal to \(1\) when the \(i\)-th chosen vertex points to \((w,0)\). The other lift \((w,1)\) realizes the complementary word.

The following table suffices:
\[
\begin{array}{c|c|c}
\text{Chosen first coordinates}&
\text{Unused first coordinates}&
\text{Words for their zero lifts}\\ \hline
(\infty,0,1)&2,3,4,5,6&
111,\ 101,\ 110,\ 101,\ 100\\
(0,1,2)&\infty,3,4,5,6&
000,\ 011,\ 101,\ 010,\ 001\\
(0,1,3)&\infty,2,4,5,6&
000,\ 110,\ 101,\ 011,\ 000\\
(0,1,5)&\infty,2,3,4,6&
000,\ 111,\ 010,\ 100,\ 001
\end{array}
\]
In each row, the displayed words together with their complements include all eight three-bit words.

For completeness, these are all cases up to automorphisms and reordering:

- The affine automorphisms
  \[
  x\mapsto ax+b,\qquad a\in\{1,2,4\},
  \]
  act transitively on the arcs of \(Q\). Thus triples containing \(\infty\) reduce to the first row.
- There are \(21\) transitive triples in \(Q\). The affine group has order \(21\), and a transitive triple has trivial stabilizer because its source, middle vertex and sink are individually distinguished. Hence all transitive triples reduce to \(\{0,1,2\}\).
- The fourteen cyclic triples are the two translation families in (Q3).

Finally, changing a chosen vertex’s second coordinate flips the corresponding bit for every candidate. This merely permutes the eight prescribed words. The claim follows.

## 2.3. Colouring a \(3\)-tree

Orient a \(3\)-tree arbitrarily. Its initial triangle maps to \(H\): both a transitive triangle and a directed triangle occur in \(H\).

Proceed in construction order. The three earlier neighbours of each new vertex form a triangle, so their images are pairwise adjacent in \(H\). The extension property supplies an image with the required three incident directions.

Thus every oriented \(3\)-tree maps to \(H\). Complete a partial \(3\)-tree to a \(3\)-tree, orient the added edges arbitrarily, and restrict the resulting homomorphism. Graphs with fewer than three vertices are immediate.

We have proved
\[
\boxed{\operatorname{tw}(\underline D)\le3\ \Longrightarrow\ \chi_o(D)\le16.}
\tag{1}
\]

# 3. A small-tournament obstruction

The lower-bound construction will force a hypothetical \(15\)-vertex target to have every neighbourhood isomorphic to \(Q\). The following lemma rules this out.

## Lemma
There is no tournament \(T\) on fifteen vertices such that
\[
T[N^+(v)]\cong T[N^-(v)]\cong Q
\qquad\text{for every }v\in V(T).
\tag{2}
\]

### Proof

Assume otherwise. Every vertex has indegree and outdegree seven.

Fix an arc \(x\to y\), and partition the other vertices into
\[
\begin{aligned}
A&=N^+(x)\cap N^-(y),&
B&=N^-(x)\cap N^-(y),\\
C&=N^+(x)\cap N^+(y),&
W&=N^-(x)\cap N^+(y).
\end{aligned}
\]

Inside \(N^+(x)\cong Q\), the vertex \(y\) has in-neighbourhood \(A\) and out-neighbourhood \(C\). Thus \(A,C\) are directed triangles, and the arcs \(A\to C\) form a cyclic-order-reversing perfect matching.

Inside \(N^-(y)\cong Q\), the vertex \(x\) has in-neighbourhood \(B\) and out-neighbourhood \(A\). Thus \(B\) is also a directed triangle, and \(B\to A\) is another reversing perfect matching. It follows that \(|W|=4\).

Now
\[
N^-(x)=B\cup W\cong Q.
\]
By (Q3), \(W\) consists of a directed triangle and a source or sink. Taking the converse and swapping \(x,y\) if necessary, we may assume
\[
W=\{z\}\cup E,\qquad z\to E,
\]
where \(E\) is a directed triangle.

In each of the copies
\[
T[B\cup\{z\}\cup E]\cong Q,\qquad
T[C\cup\{z\}\cup E]\cong Q,
\]
the vertex \(z\) already has its three out-neighbours in \(E\). Hence
\[
B\to z,\qquad C\to z.
\]
Since \(y\to z\), these give all seven in-neighbours of \(z\):
\[
N^-(z)=\{y\}\cup B\cup C,\qquad
N^+(z)=\{x\}\cup A\cup E.
\tag{3}
\]

Applying (Q2) in the appropriate neighbourhoods, each of
\[
B\to A,\qquad B\to C,\qquad B\to E,\qquad A\to C
\tag{4}
\]
is a reversing perfect matching.

For \(b\in B\), let \(a(b),c(b),e(b)\) be its unique out-neighbours in \(A,C,E\), and let \(b'\) be its successor in the directed triangle \(B\). Then
\[
N^+(b)=
\{x,y,z,b',a(b),c(b),e(b)\}.
\]
In this copy of \(Q\), the out-neighbours of \(b'\) are exactly
\[
X=\{x,y,z\},
\]
and its in-neighbours are
\[
F_b=\{a(b),c(b),e(b)\}.
\]
Indeed, the three matching bijections in (4) assign different images to \(b\) and \(b'\).

We have \(x\to y\to z\to x\). Moreover, the arcs from \(F_b\) to \(X\) are exactly
\[
a(b)\to y,\qquad c(b)\to z,\qquad e(b)\to x.
\]
By (Q2), this matching reverses cyclic order. Therefore
\[
c(b)\to a(b)\qquad\text{for every }b\in B.
\tag{5}
\]

But the matching maps \(b\mapsto a(b)\) and \(b\mapsto c(b)\) both reverse cyclic order. Consequently the induced bijection
\[
a(b)\longmapsto c(b)
\]
from \(A\) to \(C\) preserves cyclic order. The matching \(A\to C\) in (4) reverses cyclic order.

An order-preserving and an order-reversing bijection between directed triangles agree at exactly one vertex: in cyclic coordinates they have forms
\[
i\mapsto i+\alpha,\qquad i\mapsto -i+\beta,
\]
and their equality has one solution modulo \(3\). At that vertex,
\[
a(b)\to c(b),
\]
contradicting (5). \(\square\)

# 4. The explicit planar graph requiring sixteen colours

We construct the graph in three stages. All copies mentioned are fresh, except for explicitly shared vertices, and no additional edges are present.

## 4.1. A rigid seven-vertex fan

Let \(F\) have centre \(s\) and path vertices \(v_1,\dots,v_6\). Orient
\[
v_1\to v_2\to\cdots\to v_6,
\]
and orient the spokes by
\[
s\to v_1,v_2,v_3,\qquad
v_4,v_5,v_6\to s.
\]

Every two vertices must receive different colours:

- \(s\) is adjacent to every other vertex;
- within either triple \(v_1,v_2,v_3\) or \(v_4,v_5,v_6\), use an edge or a directed two-edge path;
- between the triples, use
  \[
  v_j\to s\to v_i\qquad(j\ge4,\ i\le3).
  \]

Thus every tournament homomorphism is injective on \(F\). Its underlying graph is an outerplanar fan of treewidth two.

## 4.2. A 35-vertex outerplanar forcing graph

Construct \(O\) from one copy of \(F\). For every vertex \(u\) of that copy, introduce four new vertices
\[
p_{u,1},p_{u,2},p_{u,3},p_{u,4},
\]
with arcs
\[
p_{u,1}\to p_{u,2}\to p_{u,3}\to p_{u,4},
\qquad
u\to p_{u,i}\quad(1\le i\le4).
\]
Then
\[
|V(O)|=7+7\cdot4=35.
\]
It is an outerplanar graph of treewidth at most two: it is obtained by joining outerplanar fans at single vertices.

**Forcing property.** If \(O\) maps to a tournament \(R\) of order seven, then \(R\cong Q\).

To prove this, the original \(F\) uses all seven target vertices. For every target vertex \(a\), the attachment at its preimage supplies a directed walk of length three inside \(N_R^+(a)\). Its first three vertices are distinct, so every target vertex has outdegree at least three. The average outdegree is three, hence every outdegree equals three.

A directed walk of length three in a three-vertex tournament requires a directed triangle. Thus every out-neighbourhood of \(R\) is a directed triangle. In particular \(R\) contains no transitive four-set. Property (Q4) gives \(R\cong Q\).

## 4.3. A rigid fifteen-vertex planar core

Take two copies \(F^-,F^+\) of \(F\) and a new vertex \(r\). Add all arcs
\[
F^-\to r\to F^+.
\]
Call the resulting graph \(P\). It has fifteen vertices.

Within either copy of \(F\), colours must be distinct. Vertices in different copies are separated by a directed two-edge path through \(r\), and \(r\) is adjacent to all of them. Hence
\[
\text{every tournament homomorphism is injective on }P.
\tag{6}
\]

The graph \(P\) is planar. Each subgraph induced by \(r\) and one copy of \(F\) is a cone over an outerplanar graph, and the two cones meet only at \(r\).

## 4.4. The final graph

For each of the fifteen vertices \(w\in V(P)\), take a fresh copy \(O_w\) of \(O\), and add all arcs
\[
w\to u\qquad(u\in V(O_w)).
\]
Call the resulting oriented graph \(G\). Its order is
\[
|V(G)|=15+15\cdot35=\boxed{540}.
\]

### Planarity and treewidth

A cone over an outerplanar graph is planar: draw the outerplanar graph with its vertices on a circle and put the apex, with its incident edges, on the other side of that circle on the sphere.

Adding an apex to a graph of treewidth at most two gives treewidth at most three: add the apex to every bag of a width-two tree decomposition.

Thus the two cones constituting \(P\), and every cone \(w\cup O_w\), are planar graphs of treewidth at most three. They are joined only at single vertices. Both planarity and the treewidth bound are preserved by these joins. Therefore
\[
\underline G\text{ is planar},\qquad
\operatorname{tw}(\underline G)\le3.
\tag{7}
\]

### Why fifteen colours are impossible

Suppose \(G\) maps to a tournament \(T\) of order fifteen.

By (6), the core \(P\) uses all fifteen target vertices. For each \(w\in V(P)\), its attached \(O_w\) maps into
\[
N_T^+(c(w)).
\]
Since \(O_w\) contains a rigid seven-vertex fan, every target vertex has outdegree at least seven. The average outdegree of \(T\) is seven, so all outdegrees, and all indegrees, equal seven.

The forcing property of \(O\) now yields
\[
T[N_T^+(a)]\cong Q
\qquad\text{for every }a\in V(T).
\tag{8}
\]
Because \(Q\) has no transitive four-set, (8) implies that \(T\) has no transitive five-set.

Each in-neighbourhood has seven vertices. It cannot contain a transitive four-set, since adjoining its common out-neighbour would produce a transitive five-set. By (Q4),
\[
T[N_T^-(a)]\cong Q
\qquad\text{for every }a\in V(T).
\]
This contradicts the lemma in Section 3.

Consequently
\[
\chi_o(G)\ge16.
\]
Combining (7) with the upper bound (1) gives
\[
\boxed{\chi_o(G)=16},
\]
and proves the theorem.

# 5. What remains open here

The argument settles the maximum for planar graphs of treewidth at most three, not for all planar graphs. In particular,
\[
\chi_o(D)\ge17\quad\Longrightarrow\quad
\operatorname{tw}(\underline D)\ge4.
\]

The upper-bound proof fundamentally uses a \(3\)-tree completion: the three previously coloured neighbours of a newly inserted vertex form a clique, so their target images avoid the nonadjacent paired vertices of \(H\). Arbitrary planar graphs need not admit such a completion.

The explicit lower-bound graph requires only \(16\) colours, below the supplied general lower bound \(18\). Thus neither a planar example requiring more than \(18\) colours nor an upper bound below \(80\) for all oriented planar graphs has been established.