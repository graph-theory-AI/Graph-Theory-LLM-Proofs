```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A vertex-replication construction proves the conjecture for vertex-cover number at most three and gives an explicit size bound for bounded-cover counterexamples.",
  "would_publish": false,
  "caveats": "Restricted, possibly known results; no general or orientable solution is claimed, and the proposed finite search was not executed."
}
```

# Partial results

I use the intended **closed 2-cell** formulation: the graph is embedded in a closed connected surface, every face is an open disc, and every facial boundary is a simple cycle. Graphs below are finite and simple; 2-connected graphs have at least three vertices.

The general conjecture is not resolved here. The unconditional results proved below are:

1. A closure theorem for replacing a vertex by independent vertices with the same neighbourhood.
2. The conjecture for every 2-connected graph with vertex-cover number at most three, with an embedding of **minimum possible Euler genus**.
3. If a counterexample with vertex-cover number at most \(k\) exists, one exists on at most
   \[
   5\cdot 2^{k-1}-k^2-k-2
   \]
   vertices. In particular, the vertex-cover-four case reduces to an explicitly described family of \(49\,152\) templates on at most 18 vertices.

These arguments are self-contained. I do not claim that the elementary closure results are new.

## 1. The local criterion: connected vertex links

Let \(\mathcal F\) be a multiset of simple cycles covering every edge of a connected graph \(G\) exactly twice.

For each vertex \(v\), define a multigraph \(L_v\):

- its vertices are the edges of \(G\) incident with \(v\);
- each occurrence of a cycle in \(\mathcal F\) containing the subpath \(u v w\) contributes an edge between \(uv\) and \(vw\).

Every vertex of \(L_v\) has degree two, because each edge of \(G\) occurs twice in \(\mathcal F\).

**Link criterion.** The cycles in \(\mathcal F\) are the facial boundaries of a circular embedding if and only if every \(L_v\) is connected.

Indeed, attach a separate disc along each cycle occurrence. Interior points of graph edges have disc neighbourhoods because exactly two discs meet there. The link of a graph vertex \(v\) is precisely \(L_v\). A finite connected 2-regular multigraph is topologically a circle, so its cone is a disc. Consequently, connected links make the resulting space a closed connected surface.

Conversely, the link of a vertex in a surface is a circle. Because each attaching cycle is simple, each face closure in this construction is an embedded closed disc.

Parallel edges in these *auxiliary link graphs* are allowed. In particular, the link at a degree-two vertex is a pair of parallel edges.

## 2. A vertex-replication theorem

For a vertex \(v\) of degree \(d\), its **independent \(q\)-fold replication** means deleting \(v\) and introducing \(q\) pairwise nonadjacent vertices, each adjacent to every vertex of \(N(v)\).

Write
\[
\varepsilon(S)=2-\chi(S)
\]
for Euler genus.

**Theorem 1.** Suppose \(G\) has a circular embedding in a surface of Euler genus \(\varepsilon\), and \(v\) has degree \(d\ge 2\). Its independent \(q\)-fold replication has a circular embedding whenever either

- \(q\) is odd, or
- \(d\) is even.

The resulting embedding can have Euler genus
\[
\varepsilon+\frac{(q-1)(d-2)}2.
\]
The construction preserves the lengths of the old facial cycles and adds
\[
\frac{(q-1)d}{2}
\]
quadrilateral faces.

### 2.1 Triplication at arbitrary degree

It suffices first to handle \(q=3\).

The vertex link at \(v\) gives a cyclic ordering
\[
a_0,a_1,\ldots,a_{d-1}
\]
of its neighbours. Let \(F_i\) be the face containing the turn
\[
a_i\,v\,a_{i+1},
\]
with indices modulo \(d\). These \(d\) face occurrences are distinct, since a facial cycle cannot visit \(v\) twice.

Choose colours
\[
c_i\in\{0,1,2\},\qquad c_{i-1}\ne c_i.
\]
Such a cyclic colouring exists for every \(d\ge2\): alternate two colours when \(d\) is even, and use a third colour at the last position when \(d\) is odd.

Replace \(v\) by \(v_0,v_1,v_2\). In \(F_i\), replace
\[
a_i\,v\,a_{i+1}
\quad\text{by}\quad
a_i\,v_{c_i}\,a_{i+1}.
\]
If \(\{p_i,q_i\}=\{0,1,2\}\setminus\{c_i\}\), add the quadrilateral
\[
Q_i=a_i\,v_{p_i}\,a_{i+1}\,v_{q_i}\,a_i.
\]

All resulting facial walks are simple cycles. Each new edge \(a_i v_j\) occurs once in the cycles associated with index \(i-1\), and once in those associated with index \(i\). All other edge multiplicities are unchanged.

It remains to check the links.

- At each \(v_j\), every consecutive neighbour pair \(a_i,a_{i+1}\) occurs exactly once, either in the modified \(F_i\) or in \(Q_i\). Thus its link is the original cyclic link.
- At \(a_i\), the old link vertex corresponding to \(a_iv\) is replaced by three link vertices corresponding to \(a_iv_0,a_iv_1,a_iv_2\). The two added link edges, from \(Q_{i-1}\) and \(Q_i\), form a path through these three vertices. Its endpoints are \(c_{i-1}\) and \(c_i\), because those colours differ. The two old link adjacencies attach at these endpoints.
- All remaining link edges are unchanged.

Thus every link remains connected. The link criterion supplies the required surface.

The changes in the numbers of vertices, edges and faces are
\[
\Delta n=2,\qquad \Delta m=2d,\qquad \Delta f=d.
\]
Hence
\[
\Delta\varepsilon=-\Delta\chi=d-2.
\]

### 2.2 Duplication at even degree

We need an elementary matching fact.

**Matching fact.** If \(M_0,M_1\) are perfect matchings on \(2r\) points whose union is a single cycle, there is a perfect matching \(M_2\) such that both \(M_0\cup M_2\) and \(M_1\cup M_2\) are single cycles. Unions count edge multiplicity, so a two-edge cycle is allowed when \(r=1\).

To prove this, construct, for every even order, a cubic edge-coloured multigraph with colours \(0,1,2\), in which every two colour classes form a Hamiltonian cycle.

Start with two vertices joined by three differently coloured parallel edges. To increase the order by two, replace a vertex by a triangle with vertices \(u_0,u_1,u_2\). Attach the old colour-\(i\) edge to \(u_i\), and colour \(u_i u_j\) by the third colour. For any two colours \(i,j\), the old vertex is replaced in the corresponding Hamiltonian cycle by the three-vertex path through \(u_i,u_k,u_j\). Thus the property is preserved.

Finally, identify the cycle formed by colours 0 and 1 with the prescribed alternating cycle \(M_0\cup M_1\), and transport the third matching.

Now suppose \(d=2r\). Using the notation above, replace \(v\) by \(x,y\), putting \(x\) in the even-indexed faces \(F_i\) and \(y\) in the odd-indexed faces.

The neighbour pairs belonging to the even-indexed turns form a perfect matching \(M_0\); the odd-indexed turns form a perfect matching \(M_1\). Their union is the original vertex link. Choose \(M_2\) as in the matching fact. For each \(\{a_i,a_j\}\in M_2\), add the quadrilateral
\[
x\,a_i\,y\,a_j\,x.
\]

Each new edge occurs in one modified old face and one added quadrilateral. The links at \(x,y\) are \(M_0\cup M_2\) and \(M_1\cup M_2\), respectively. At every old neighbour, the old link vertex is replaced by a two-vertex path. All links are therefore connected.

Here
\[
\Delta n=1,\qquad \Delta m=d,\qquad \Delta f=d/2,
\]
so
\[
\Delta\varepsilon=(d-2)/2.
\]

Repeated triplication proves the theorem for odd \(q\); repeated duplication proves it for arbitrary \(q\) when \(d\) is even. ∎

In particular, arbitrary odd independent blow-ups of a circularly embeddable graph remain circularly embeddable. This includes odd blow-ups of 2-connected planar graphs.

## 3. Vertex-cover number at most three

Here is a complete special case, including its optimal genus.

**Theorem 2.** Let \(G\) be a 2-connected graph with a vertex cover
\[
X=\{a,b,c\}.
\]
Put
\[
t=\bigl|\{v\notin X:N(v)=X\}\bigr|.
\]
Then \(G\) has a circular embedding whose Euler genus is
\[
\boxed{\max\left\{0,\left\lceil\frac{t-2}{2}\right\rceil\right\}.}
\]
This is the minimum Euler genus of \(G\).

Consequently, every 2-connected graph of vertex-cover number at most three satisfies the circular embedding conjecture.

A smaller vertex cover can be enlarged to three vertices, since \(G\) has at least three vertices.

### 3.1 Embeddings of \(K_{3,t}\) with three reserved quadrilateral faces

For every \(t\ge2\), we construct a circular embedding of \(K_{3,t}\) with:

- a quadrilateral face containing \(a,b\);
- a distinct quadrilateral face containing \(b,c\);
- a distinct quadrilateral face containing \(c,a\);
- Euler genus \(\lceil(t-2)/2\rceil\).

For \(t=2\), with other part \(\{x,y\}\), use the facial cycles
\[
a\,x\,b\,y\,a,\qquad
b\,x\,c\,y\,b,\qquad
c\,x\,a\,y\,c.
\]
Each edge occurs twice. Links are triangles at degree-three vertices and two-edge cycles at degree-two vertices. Euler’s formula gives
\[
\chi=5-6+3=2.
\]

For \(t=3\), with other part \(\{x,y,z\}\), use
\[
\begin{aligned}
&a\,x\,b\,y\,c\,z\,a,\\
&a\,y\,b\,z\,a,\\
&b\,z\,c\,x\,b,\\
&c\,x\,a\,y\,c.
\end{aligned}
\]
Again every edge occurs twice, and every vertex link is a triangle. Here
\[
\chi=6-9+4=1.
\]

Triplicate a degree-three vertex in the part of size \(t\). This changes \(K_{3,t}\) into \(K_{3,t+2}\), increases Euler genus by one, and adds three quadrilaterals. Every old quadrilateral retains its two vertices in \(\{a,b,c\}\). Thus the three reserved faces persist.

Starting from \(t=2\) or \(t=3\) proves the assertion for all \(t\ge2\). More precisely:

- if \(t\) is even, all faces are quadrilaterals;
- if \(t\) is odd, exactly one face is a hexagon and all others are quadrilaterals.

### 3.2 Adding the remaining vertices and edges

Since \(X\) is a vertex cover, \(V(G)\setminus X\) is independent. Since \(G\) is 2-connected, every vertex outside \(X\) has degree two or three.

Thus, besides the \(t\) vertices adjacent to all of \(X\), the graph consists of:

- vertices adjacent to one of the pairs \(ab,bc,ca\);
- an arbitrary subset of the three edges \(ab,bc,ca\).

Assume first that \(t\ge2\). Start with the embedding of \(K_{3,t}\) just constructed.

Consider its reserved quadrilateral for \(a,b\). Its boundary is the union of two internally disjoint \(a\)-\(b\) paths of length two. Inside this facial disc, insert:

- a length-two \(a\)-\(b\) path for each required degree-two vertex with neighbourhood \(\{a,b\}\);
- the edge \(ab\), if required.

The inserted paths can be drawn with pairwise disjoint interiors. The new faces lie between consecutive paths, and each boundary is a simple cycle. Perform the analogous operation in the other two reserved faces.

The three face interiors are disjoint, so these insertions do not interfere. They introduce exactly the missing vertices and edges of \(G\), without changing the surface. This gives the claimed upper bound.

For \(t=0\), the graph is planar: it is obtained from a subgraph of a triangle by placing length-two paths parallel to its edges.

For \(t=1\), it is likewise planar: start with a planar \(K_4\), whose fourth vertex is the unique vertex adjacent to all of \(X\); add length-two paths parallel to edges within \(X\), and delete any unwanted edges within \(X\).

In both cases, 2-connectivity ensures that every boundary in a plane embedding is a simple cycle. Indeed, a repeated vertex on a plane facial boundary would give a cutvertex by the Jordan curve separation argument.

### 3.3 Optimality of the genus

For \(t\ge2\), the graph contains \(K_{3,t}\).

Any embedding of a connected graph can be made cellular on a surface of no larger Euler genus by taking a regular neighbourhood and capping its boundary components. Thus the usual bipartite Euler bound applies to the minimum genus of \(K_{3,t}\).

In a cellular embedding of \(K_{3,t}\), every facial boundary walk has length at least four: the graph is bipartite and simple, and its minimum degree is at least two. Consequently,
\[
4f\le 2m=6t.
\]
Therefore
\[
\begin{aligned}
\varepsilon
&=2-(n-m+f)\\
&=2-\bigl((t+3)-3t+f\bigr)\\
&=2t-1-f\\
&\ge \frac{t-2}{2}.
\end{aligned}
\]
Euler genus is an integer, so
\[
\operatorname{eg}(G)\ge
\operatorname{eg}(K_{3,t})
\ge \left\lceil\frac{t-2}{2}\right\rceil.
\]
This matches the construction. For \(t\le1\), planarity already gives the optimal value zero. ∎

## 4. A bound on bounded-cover counterexamples

The replication theorem also limits the structure of a smallest counterexample.

**Theorem 3.** Let \(k\ge1\). If the circular embedding conjecture has a counterexample of vertex-cover number at most \(k\), it has one on at most
\[
\begin{aligned}
B(k)
&=k+
3\!\!\sum_{\substack{3\le j\le k\\j\text{ odd}}}\binom{k}{j}
+
2\!\!\sum_{\substack{4\le j\le k\\j\text{ even}}}\binom{k}{j}\\
&=5\cdot2^{k-1}-k^2-k-2
\end{aligned}
\]
vertices.

### Proof

Choose a counterexample \(G\) of minimum order among those of vertex-cover number at most \(k\).

#### Minimum degree is at least three

Suppose \(v\) has degree two, with neighbours \(a,b\). The three-vertex case is planar, so assume \(|V(G)|\ge4\).

Let
\[
H=(G-v)+ab,
\]
adding \(ab\) only if it is absent. Suppression of a degree-two vertex preserves 2-connectivity here. Explicitly, paths through \(a v b\) can be replaced by the edge \(ab\); after deleting \(a\) or \(b\), the vertex \(v\) was merely a leaf and can be discarded.

The vertex-cover number of \(H\) remains at most \(k\). If \(v\) belonged to a chosen cover, remove it and, if necessary, add one endpoint of the new edge \(ab\).

By minimality, \(H\) has a circular embedding.

- If \(ab\notin E(G)\), subdividing its embedded edge restores \(G\).
- If \(ab\in E(G)\), add the path \(a v b\) inside a face incident with \(ab\). This splits that face into a triangle and another simple-cycle face.

Both contradict the choice of \(G\). Hence \(\delta(G)\ge3\).

#### Bounds on equal-neighbourhood classes

Call vertices with identical open neighbourhoods **false twins**; in a simple graph they are pairwise nonadjacent.

Deleting false twins while retaining at least two members of their class preserves 2-connectivity. To see this, delete any additional vertex \(z\), and retain a twin \(w\ne z\). Any path using a removed twin can be converted into a walk using \(w\), since their neighbourhoods agree.

Now consider a false-twin class of common degree \(d\).

- If \(d\) is odd and the class has at least four vertices, delete two. The smaller graph is 2-connected and has a circular embedding by minimality. Triplicating a retained twin restores \(G\), a contradiction.
- If \(d\) is even and the class has at least three vertices, delete one. Duplicating a retained twin restores \(G\), again a contradiction.

Thus odd-degree classes have size at most three, and even-degree classes have size at most two.

Choose a vertex cover \(X\) of size \(k\), padding it if necessary; if \(|V(G)|<k\), the claimed bound is already immediate. Every vertex outside \(X\) has neighbourhood some subset \(S\subseteq X\) with \(|S|\ge3\). For a fixed \(S\), these vertices form a false-twin class.

Summing the class bounds gives \(B(k)\). The closed form follows from
\[
\sum_{\substack{j\ge3\\j\text{ odd}}}\binom{k}{j}=2^{k-1}-k,
\qquad
\sum_{\substack{j\ge4\\j\text{ even}}}\binom{k}{j}
=2^{k-1}-1-\binom{k}{2}.
\]
∎

### A fully specified next finite target

For \(k=4\), Theorem 3 gives \(B(4)=18\). Any minimum-order counterexample in this class is represented by the following construction:

1. Take four labelled cover vertices.
2. Choose any subset of the six edges among them.
3. For each of the four three-element subsets of the cover, add \(0,1,2,\) or \(3\) independent vertices having exactly that neighbourhood.
4. Add \(0,1,\) or \(2\) independent vertices adjacent to all four cover vertices.
5. Discard graphs that are not 2-connected or have minimum degree below three.

There are
\[
2^6\cdot4^4\cdot3=49\,152
\]
templates before filtering.

An exact feasibility test follows directly from the link criterion. Enumerate all simple cycles \(\mathcal C(G)\), and introduce variables
\[
x_C\in\{0,1,2\}\qquad(C\in\mathcal C(G)).
\]
Require
\[
\sum_{C\ni e}x_C=2
\qquad(e\in E(G)),
\]
and, for every vertex \(v\) and every nonempty proper subset
\(A\subsetneq\delta(v)\), require
\[
\sum_{\substack{C\ni v\\ |E(C)\cap A|=1}}x_C\ge2.
\]
The first constraints make every vertex link 2-regular. The second require every nontrivial link cut to be nonempty, hence every link to be connected. Thus this integer system is feasible exactly when \(G\) has a circular embedding.

For these templates, every simple cycle has length at most eight, since vertices outside the four-vertex cover are independent.

**I did not execute this search and claim no computational result for vertex-cover number four.**

## 5. Remaining gap

The constructions above do not provide an embedding for an arbitrary 2-connected graph. In particular, they do not handle arbitrary twin-free cubic graphs, so the principal cycle-double-cover difficulty remains.

Nor do these surgeries preserve orientability in general: disc gluing establishes a surface, but not a consistently orientable one.

Thus the established conclusion is restricted but complete: **the conjecture holds, at minimum Euler genus, for vertex-cover number at most three**, and independent vertex replication supplies additional closure and counterexample-size results.