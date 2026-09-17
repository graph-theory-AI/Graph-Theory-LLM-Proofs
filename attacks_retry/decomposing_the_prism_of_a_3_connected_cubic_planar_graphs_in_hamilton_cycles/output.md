```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove that at most n/2-2 triangle expansions suffice to make the prism Hamilton-decomposable, and give a 3-edge-colouring criterion requiring no expansions.",
  "would_publish": false,
  "caveats": "The original conjecture is not resolved; the novelty of these partial results has not been checked."
}
```

# 1. Results established

Write \(\Pi(G)=G\square K_2\), with copies \(v_0,v_1\) of each vertex \(v\). The edge \(v_0v_1\) is its **rung**.

A **triangle expansion** at a cubic vertex \(v\) replaces \(v\) by a triangle, attaching its three former incident edges to distinct triangle vertices. For \(S\subseteq V(G)\), let \(G^\triangle(S)\) be the graph obtained by expanding precisely the vertices in \(S\).

The main partial result is the following.

**Theorem 1 — bounded triangle expansion.**  
Let \(G\) be a finite simple, 3-edge-connected cubic graph on \(n\) vertices admitting a proper 3-edge-colouring. There is a set
\[
S\subseteq V(G),\qquad |S|\le \frac n2-2,
\]
such that \(\Pi(G^\triangle(S))\) has a Hamilton decomposition.

Moreover, \(S\) can be chosen so that the same conclusion holds for every
\[
S\subseteq U\subseteq V(G).
\]

Consequently:

**Corollary 2.**  
Every 3-connected cubic planar graph \(G\) on \(n\) vertices can be changed into a 3-connected cubic planar graph \(H\) on at most \(2n-4\) vertices, by triangle expansions, such that \(\Pi(H)\) has a Hamilton decomposition.

This does not prove the conjecture for \(G\) itself. The proof also gives a directly applicable special case.

For a proper 3-edge-colouring with colour classes \(A,B,M\), let
\[
s=c(A\cup B)+c(A\cup M)+c(B\cup M),
\]
where \(c(F)\) denotes the number of components of a 2-factor \(F\).

**Theorem 3 — an unexpanded special case.**  
Let \(G\) be a connected simple cubic graph with a proper 3-edge-colouring.

* If \(s=4\), then \(\Pi(G)\) has a Hamilton decomposition.
* If \(s=3\) and \(G\) is nonbipartite, then \(\Pi(G)\) has a Hamilton decomposition.

More quantitatively, in Theorem 1, a fixed colouring with \(s\ge4\) permits
\[
|S|\le s-4.
\]
If \(s=3\), one triangle expansion suffices; none is needed when \(G\) is nonbipartite.

The argument below is independent of the supplied cube-insertion attempt. I set that lead aside rather than assume any of its certificates.

# 2. A square-switch construction

Fix a proper 3-edge-colouring
\[
E(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}M.
\]
Each colour class is a perfect matching. Write \(A_i,B_i,M_i\) for their copies in layer \(i\), and let \(L\) be the set of all rungs.

Start with the edge partition
\[
\mathcal R_0=A_0\cup B_1\cup L,
\qquad
\mathcal B_0=B_0\cup A_1\cup M_0\cup M_1.
\tag{1}
\]
Both subgraphs are spanning 2-factors.

The components of \(\mathcal R_0\) correspond exactly to the cycles of \(A\cup B\). Indeed, on each such cycle, the red walk alternates between a horizontal edge and a rung, following the base cycle and visiting both copies of every vertex.

The blue components are the cycles of \(B\cup M\) in layer \(0\) and of \(A\cup M\) in layer \(1\). Thus, putting
\[
c=c(A\cup B),\qquad
q=c(A\cup M)+c(B\cup M),
\]
the initial component counts are \(c\) and \(q\).

For \(e=uv\in M\), its two horizontal copies and the two rungs form a square
\[
u_0v_0v_1u_1u_0.
\]
Initially the horizontal edges are blue and the rungs are red. A **switch at \(e\)** exchanges their colours.

Because \(M\) is a matching, switches at different edges of \(M\) have disjoint vertex sets. Any collection of them therefore leaves an edge partition into two spanning 2-factors.

We will repeatedly use two elementary facts:

1. If the two removed edges lie in different cycles of one factor, the switch merges those cycles.
2. If they lie in one cycle, the switch leaves either one or two cycles in their place.

These follow by deleting the two edges and examining the resulting paths.

## 2.1 The case \(s=4\)

Since each bicoloured union has at least one cycle, \(s=4\) means that their component counts are \(2,1,1\). Rename colours so that \(A\cup B\) has two cycles.

Connectedness of \(G\) supplies an edge \(e\in M\) joining these two cycles. In (1), switching at \(e\):

* merges the two red cycles;
* merges the two blue Hamilton cycles, which initially lie in different layers.

Both factors become Hamilton cycles. This proves the first part of Theorem 3.

## 2.2 The case \(s=3\) with \(G\) nonbipartite

Now all three bicoloured unions are Hamilton cycles. In particular, \(\mathcal R_0\) is Hamilton and \(\mathcal B_0\) consists of two Hamilton cycles, one in each layer.

Give the vertices of the Hamilton cycle \(A\cup B\) their alternating two-colouring. Since \(G\) is nonbipartite, some edge \(e=uv\in M\) has endpoints of the same colour.

Orient \(\mathcal R_0\). The directions in which it traverses rungs alternate along \(A\cup B\). Hence the rungs at \(u\) and \(v\) are traversed in the same direction.

Switching at \(e\) preserves the connectedness of the red factor. To see this explicitly, suppose those directed rungs are
\[
u_0\longrightarrow u_1,\qquad v_0\longrightarrow v_1.
\]
Their deletion leaves directed paths
\[
u_1\longrightarrow v_0,\qquad v_1\longrightarrow u_0.
\]
Adding \(u_0v_0\) and \(u_1v_1\) joins these paths into one cycle.

The same switch merges the two blue layer cycles. Thus both factors are Hamilton, proving the second part of Theorem 3.

For example, \(K_4\) satisfies this second condition. The cube satisfies the first condition: colour its two opposite 4-cycles alternately with \(A,B\), using opposite alternations on the two cycles, and colour the four joining edges with \(M\).

# 3. Choosing switches with a connected remainder

For the general construction, it is not enough to make the red factor Hamilton. We also want enough surviving rungs to connect its complementary blue cycles.

Contract every cycle of \(A\cup B\) to a vertex. The edges of \(M\) give a connected multigraph \(Q\); loops are allowed.

Every vertex of \(Q\) has even degree, because the corresponding \(A\cup B\)-cycle has even length. Moreover, every nontrivial edge cut of \(Q\) corresponds to an edge cut of \(G\). Since \(G\) is 3-edge-connected, such a cut has size at least three; since \(Q\) is Eulerian, its size is even. Therefore
\[
|\delta_Q(X)|\ge4
\tag{2}
\]
for every nonempty proper vertex set \(X\).

It follows that \(Q\) has two edge-disjoint spanning trees. Here is the precise standard theorem being used: a multigraph has two edge-disjoint spanning trees if every partition into \(r\) nonempty vertex classes has at least \(2(r-1)\) edges joining different classes. Condition (2) implies this, because summing the cuts of the classes gives at least \(4r\), and each interclass edge is counted twice.

If \(Q\) has only one vertex, use two empty trees.

Choose one spanning tree \(T\subseteq M\) whose complement contains another spanning tree. Then
\[
Q-T\text{ is connected},
\qquad\text{and hence}\qquad
G-T\text{ is connected}.
\tag{3}
\]

Perform the switches at all edges of \(T\). Since \(T\) is a tree on the \(A\cup B\)-cycles, each switch merges two different current red components. The resulting red factor \(\mathcal R\) is therefore Hamilton. Let \(\mathcal B\) be its complementary 2-factor.

The red rungs are precisely those at vertices not incident with \(T\). The blue horizontal edges project onto
\[
(A\cup B)\cup(M\setminus T)=G-T.
\tag{4}
\]
In this projection, some edges occur twice, which is irrelevant to connectedness.

There is also a useful local feature.

> At every original vertex, the two horizontal edges belonging to the colour of its rung project to different base edges.

For a red rung, those horizontal edges are the \(A\)-edge in layer \(0\) and the \(B\)-edge in layer \(1\). For a blue rung, the roles are reversed. Call such a vertex **skew**.

The next lemma exploits exactly this feature.

# 4. Triangle expansion at a skew vertex

**Lemma 4.**  
Suppose \(\Pi(G)\) is partitioned into a red Hamilton cycle \(\mathcal R\) and a blue 2-factor \(\mathcal B\). Let \(v\) be skew, with a red rung.

Triangle expansion at \(v\) can preserve red Hamiltonicity and:

* merge the two blue cycles containing \(v_0,v_1\), if they are different;
* preserve the blue component count, if \(v_0,v_1\) lie in the same blue cycle.

Every edge outside the replaced vertex keeps its colour.

### Proof

Write
\[
N_G(v)=\{a,b,c\},
\]
with red horizontal edges
\[
v_0a_0,\qquad v_1b_1.
\]
Skewness means \(a\ne b\).

Replace \(v\) by a triangle \(xyzx\), attaching \(x,y,z\) to \(a,b,c\), respectively. Retain the colours on the six attachment edges. The required internal red endpoints are \(x_0,y_1\), and the blue terminals are
\[
y_0,z_0,x_1,z_1.
\]

The internal graph is the triangular prism, with nine edges. The following are explicit edge partitions of it.

### Merge certificate
\[
\begin{aligned}
R_{\mathrm m}&=
x_0\,y_0\,z_0\,z_1\,x_1\,y_1,\\
B_{\mathrm m}^{(1)}&=
y_0\,y_1\,z_1,\\
B_{\mathrm m}^{(2)}&=
z_0\,x_0\,x_1.
\end{aligned}
\tag{5}
\]

### Preserve certificate
\[
\begin{aligned}
R_{\mathrm p}&=
x_0\,x_1\,z_1\,z_0\,y_0\,y_1,\\
B_{\mathrm p}^{(1)}&=
y_0\,x_0\,z_0,\\
B_{\mathrm p}^{(2)}&=
x_1\,y_1\,z_1.
\end{aligned}
\tag{6}
\]

In each certificate, the red path spans all six vertices and uses five edges. The two blue paths are vertex-disjoint, together span all six vertices, and use exactly the remaining four edges. These assertions follow directly from the displayed paths.

Deleting \(v_0,v_1\) from the red Hamilton cycle leaves one spanning path, because their rung is red. Either internal red path reconnects it to a Hamilton cycle.

For blue, there are two cases.

**Different blue cycles.**  
Deleting \(v_0,v_1\) leaves two paths whose endpoint pairing, using the new terminal labels, is
\[
\{\{y_0,z_0\},\{x_1,z_1\}\}.
\]
Certificate (5) instead pairs
\[
\{\{y_0,z_1\},\{z_0,x_1\}\}.
\]
These different pairings join the two outside paths into one cycle.

**The same blue cycle.**  
Deleting \(v_0,v_1\) leaves two paths, each joining a layer-\(0\) terminal to a layer-\(1\) terminal. Certificate (6) pairs the terminals within their respective layers:
\[
\{\{y_0,z_0\},\{x_1,z_1\}\}.
\]
Again, the inside and outside pairings are different, so their union is one cycle.

All other blue cycles are unchanged. This proves the lemma. \(\square\)

# 5. Connecting all complementary cycles

Return to the factors \(\mathcal R,\mathcal B\) constructed in Section 3, with \(\mathcal R\) Hamilton.

Form a multigraph \(J\) whose vertices are the cycles of \(\mathcal B\). For every red rung \(v_0v_1\), put an edge in \(J\) between the blue cycles containing its endpoints. This edge is a loop when both endpoints belong to the same blue cycle.

**Claim.** \(J\) is connected.

Indeed, adding all red rungs to \(\mathcal B\) is the same as adding all rungs. Contracting those rungs gives the connected graph \(G-T\), with possibly doubled edges, by (3)–(4). Thus \(\mathcal B\) together with the red rungs is connected. Contracting its blue cycles proves the claim.

Let \(b=c(\mathcal B)\), and choose a spanning tree of \(J\). Its \(b-1\) edges correspond to distinct original vertices of \(G\); let \(S\) be this vertex set.

Expand these vertices one at a time, using the merge certificate (5).

Each unprocessed selected vertex still has its original skew configuration. Moreover, the endpoints of its rung lie in different current blue components: the already processed edges form a forest in the chosen spanning tree, so they cannot have connected the endpoints of an unprocessed tree edge.

Consequently every expansion:

* preserves the red Hamilton cycle;
* decreases the number of blue components by exactly one.

After \(b-1\) expansions, blue is also Hamilton. Therefore
\[
|S|=b-1.
\tag{7}
\]

This also proves the assertion about supersets. Once both colours are Hamilton cycles, any remaining original vertex is still skew. Rename the two colours if necessary so that its rung is red, and use the preserve certificate (6). Hence any additional original vertices may be expanded without destroying the Hamilton decomposition.

# 6. Bounding the number of expansions

We first establish an elementary bound on the total number \(s\) of bicoloured cycles.

**Lemma 5.**  
For every connected properly 3-edge-coloured cubic graph on \(n\) vertices,
\[
s\le \frac n2+2.
\tag{8}
\]

### Proof

Work in the binary cycle space of \(G\). Consider the incidence vectors of all \(s\) bicoloured cycles.

Their sum is zero, since every edge belongs to exactly two of these cycles. This is their only nonzero linear dependence.

To see that, suppose coefficients assigned to the bicoloured cycles give a zero sum. At every edge, the coefficients of its two containing bicoloured cycles must agree. At each vertex, this forces agreement among the three bicoloured cycles through that vertex. Connectedness then forces all coefficients to agree.

Thus these vectors have rank \(s-1\). The cycle space of a connected cubic graph has dimension
\[
|E(G)|-|V(G)|+1=\frac n2+1.
\]
Hence \(s-1\le n/2+1\), proving (8). \(\square\)

Now suppose \(s\ge4\). Rename colours so that
\[
c=c(A\cup B)\ge2.
\]
Recall that the initial blue factor has \(q=s-c\) components, and that we perform \(c-1\) switches.

The first switch merges two blue cycles, because before any switch its two blue horizontal edges lie in different layers. Each subsequent switch increases the blue component count by at most one. Therefore
\[
b\le q-1+(c-2)=s-3.
\]
By (7),
\[
|S|\le s-4\le \frac n2-2.
\tag{9}
\]

If \(s=3\), take \(T=\varnothing\). The initial red factor is Hamilton, the initial blue factor has two components, and the graph \(J\) is connected. Thus one triangle expansion suffices.

For \(n\ge6\),
\[
1\le \frac n2-2.
\]
The only simple cubic graph on four vertices is \(K_4\); it is nonbipartite and is covered by the no-expansion construction of Section 2.2.

This proves Theorem 1, including all order cases and its quantitative refinements.

# 7. Returning to 3-connected cubic planar graphs

For a 3-connected cubic planar graph:

1. It is 3-edge-connected.
2. The Four-Colour Theorem gives a proper 3-edge-colouring by the standard Tait correspondence.

For completeness, in the latter correspondence, colour the faces by elements of \(\mathbb Z_2^2\), and colour each edge by the difference of the colours of its two incident faces. At a cubic vertex, the three resulting nonzero differences are distinct.

It remains to check that triangle expansions preserve the class.

## Planarity and cubicity

Insert each triangle into a small disk around the old vertex, respecting the cyclic order of its incident edges. This preserves planarity. Each new vertex has two triangle edges and one attachment edge, so the graph remains cubic and simple.

## 3-connectivity

Consider one triangle expansion, with new triangle \(K\), and delete a set \(X\) of at most two vertices.

* If \(X\cap V(K)=\varnothing\), contracting the intact triangle gives \(G-X\), which is connected. Hence the expanded graph minus \(X\) is connected.
* If exactly one triangle vertex is deleted, the outside graph is \(G-v\) with at most one additional vertex deleted, so it is connected. The two surviving triangle vertices are adjacent, and at least one of their attachment edges survives.
* If two triangle vertices are deleted, no outside vertex is deleted. The outside graph \(G-v\) is connected, and the remaining triangle vertex retains its attachment edge.

Thus a triangle expansion preserves 3-connectivity. Iteration proves the claim for \(G^\triangle(S)\).

Finally,
\[
|V(G^\triangle(S))|
=n+2|S|
\le n+2\left(\frac n2-2\right)
=2n-4.
\]
This establishes Corollary 2.

# 8. What remains open in this attack

The construction makes the red factor Hamilton and ensures that the auxiliary graph \(J\) of complementary blue cycles is connected. It does **not** show that \(J\) has only one vertex.

Triangle expansion supplies a local operation that merges blue cycles while preserving the red Hamilton cycle. That operation cannot simply be contracted away: reversing a merge certificate can split the blue Hamilton cycle back into two cycles. Thus the bounded-expansion theorem does not descend to a Hamilton decomposition of the original prism.

The results proved here are therefore:

* a direct sufficient condition on a 3-edge-colouring of \(G\);
* a constructive bound of \(n/2-2\) triangle expansions for every graph in the conjectured class;
* preservation under any further triangle expansions at original vertices.

No counterexample to the original conjecture is obtained, and no argument here eliminates the expansions in general. The novelty of these partial results remains unchecked.