```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A matching-based extension of the treewidth-three argument proves Jones’ inequality for an additional unbounded-treewidth class, including radial completions of plane triangulations.",
  "would_publish": false,
  "caveats": "The unrestricted planar case is not resolved; novelty of these special-case results has not been checked."
}
```

# A supported-pair extension of the treewidth-three case

Write
\[
\nu(G)=cp(G),\qquad \tau(G)=cc(G).
\]
All graphs below are finite, simple, and undirected.

I do **not** resolve Jones’ conjecture for arbitrary planar graphs. I checked the local-reduction argument in the previous attempt and found it sound; a self-contained proof is included in Section 3. The additional result here extends that special case to a class with **unbounded treewidth and unbounded maximum degree**.

A concrete consequence is the following.

> **Planar special case.** Let \(T\) be a plane triangulation. Insert a new vertex in every face, adjacent to its three boundary vertices, and then delete any chosen subset of the original edges of \(T\). The resulting graph \(G\) satisfies
> \[
> \tau(G)\le 2\nu(G).
> \]
> Indeed, \(\nu(G)\) is exactly the maximum matching size of \(T\). If no original edges are deleted, \(\tau(G)\) is exactly the minimum vertex-cover size of \(T\).

Thus the result includes both vertex–face incidence graphs of plane triangulations and their full face-stellations.

## 1. A general sufficient condition

For a graph \(J\), let \(\mu(J)\) denote its maximum matching size and \(\operatorname{vc}(J)\) its minimum vertex-cover size.

Suppose
\[
V(G)=U\mathbin{\dot\cup}W,
\]
where \(W\) is independent and every vertex of \(W\) has degree at most three.

Define an auxiliary graph \(F\) on \(U\) by
\[
uv\in E(F)
\quad\Longleftrightarrow\quad
\text{some }w\in W\text{ is adjacent to both }u\text{ and }v.
\]
Edges of \(F\) need not be edges of \(G\).

Assume the following **support condition**:
\[
uv\in E(F)\setminus E(G[U])
\quad\Longrightarrow\quad
|N_G(u)\cap N_G(v)\cap W|\ge 2.
\tag{S}
\]
In other words, every pair in \(F\) supports either a triangle or a four-cycle whose only vertices in \(U\) are that pair.

Let
\[
R=\bigl(U,\ E(G[U])\setminus E(F)\bigr).
\]
This is the graph of original edges not accounted for by the supported pairs.

**Theorem 1.** Under these assumptions:

1. If \(\operatorname{tw}(R)\le 3\), then
   \[
   \tau(G)\le 2\nu(G).
   \]
2. If \(R\) is a forest, then
   \[
   \nu(G)=\mu(F),
   \qquad
   \tau(G)\le \operatorname{vc}(F)\le 2\mu(F).
   \tag{1}
   \]
3. In the forest case, equality
   \[
   \tau(G)=\operatorname{vc}(F)
   \tag{2}
   \]
   holds if every vertex of \(W\) is either of degree at most two or is simplicial in \(G\).

Here a vertex is *simplicial* if its neighborhood is a clique. Planarity is not required for this theorem.

The theorem contains the entire treewidth-three case: take \(W=\varnothing\), so \(F\) is empty and \(R=G\).

## 2. Proof of the supported-pair theorem

### Packing the supported cycles

For each edge \(uv\in E(F)\), choose a cycle \(C_{uv}\) as follows:

- If \(uv\in E(G)\), choose a common neighbor \(w\in W\), obtaining the triangle \(uvw\).
- Otherwise, condition (S) supplies distinct common neighbors \(w,w'\in W\), obtaining the four-cycle \(uwvw'u\).

If \(M\) is a matching in \(F\), these chosen cycles are vertex-disjoint. Their vertices in \(U\) are disjoint because \(M\) is a matching. Moreover, a vertex of \(W\) cannot occur in cycles belonging to two matching edges: it would have to be adjacent to their four distinct endpoints, contrary to its degree being at most three.

Consequently, every matching of size \(r\) in \(F\) gives \(r\) vertex-disjoint cycles in \(G\).

### A maximal matching exposes the residual graph

Choose a maximal matching \(M\) in \(F\), and put
\[
A=V(M),\qquad r=|M|.
\]
The set \(A\) is a vertex cover of \(F\).

Every two neighbors of a vertex \(w\in W\) are adjacent in \(F\). Therefore, after deleting \(A\), each vertex of \(W\) has at most one remaining neighbor. Also,
\[
G[U]-A=R-A,
\]
because no edge of \(F\) has both endpoints outside \(A\).

Thus \(G-A\) is obtained from \(R-A\) by adding isolated vertices and leaves. In particular, all its cycles lie in \(R-A\).

The \(r\) supported cycles belonging to \(M\) are disjoint from every cycle in \(R-A\), giving
\[
\nu(G)\ge r+\nu(R-A).
\tag{3}
\]
Deleting \(A\), followed by a feedback vertex set of \(R-A\), gives
\[
\tau(G)\le 2r+\tau(R-A).
\tag{4}
\]

If \(\operatorname{tw}(R)\le3\), then \(\operatorname{tw}(R-A)\le3\). The independently proved treewidth-three lemma in Section 3 now yields
\[
\tau(G)
\le 2r+2\nu(R-A)
\le 2\nu(G).
\]

This proves the first assertion.

### Exact packing number when \(R\) is a forest

We already know that
\[
\nu(G)\ge \mu(F).
\]

For the reverse inequality, consider any cycle \(C\) of \(G\).

- If \(C\) contains \(w\in W\), its two neighbors along \(C\) are distinct vertices \(u,v\in U\), and \(uv\in E(F)\).
- If \(C\) lies entirely in \(U\), it must contain an edge of \(F\), since \(R\) is a forest.

We can therefore associate with every cycle an edge of \(F\) whose endpoints lie on that cycle. Vertex-disjoint cycles give vertex-disjoint associated edges. Hence
\[
\nu(G)\le\mu(F),
\]
proving equality.

Now let \(X\) be any vertex cover of \(F\). In \(G-X\), every vertex of \(W\) has degree at most one, and the remaining graph on \(U\) is a subgraph of \(R\). Thus \(G-X\) is a forest, and
\[
\tau(G)\le\operatorname{vc}(F).
\]
Finally, the endpoints of a maximum matching form a vertex cover, so
\[
\operatorname{vc}(F)\le2\mu(F).
\]
This proves (1).

### Moving a feedback vertex set off \(W\)

Suppose additionally that each \(w\in W\) has degree at most two or is simplicial.

Start with a feedback vertex set \(X\). If \(w\in X\cap W\), then at most two neighbors of \(w\) lie outside \(X\):

- this is immediate when \(d_G(w)\le2\);
- otherwise those surviving neighbors form a clique in the forest \(G-X\), so there are at most two.

If at most one neighbor survives, restore \(w\). If exactly two survive, first delete one of them and then restore \(w\). In both cases the remaining graph is still a forest, because the restored vertex has degree at most one. The size of the feedback vertex set does not increase.

Repeating gives a feedback vertex set \(X'\subseteq U\) with
\[
|X'|\le |X|.
\]
Such a set must cover every edge \(uv\) of \(F\): otherwise the supported triangle or four-cycle for \(uv\) survives, since none of its vertices in \(W\) is deleted. Therefore
\[
\operatorname{vc}(F)\le |X'|\le |X|.
\]
Together with (1), this proves (2). \(\square\)

## 3. Verification of the treewidth-three ingredient

For completeness, here is a proof of the result reused from the previous attempt.

**Lemma 2.** Every graph \(H\) of treewidth at most three satisfies
\[
\tau(H)\le2\nu(H).
\]

### The structural claim

**Claim.** A nonempty graph of treewidth at most three and minimum degree at least three contains either

- a triangle containing a degree-three vertex; or
- a four-cycle whose opposite vertices both have degree three.

Take a tree decomposition with bags of size at most four. Contract any decomposition edge whose one bag is contained in the other, retaining the larger bag. Thus adjacent bags are incomparable under inclusion.

If there is only one bag, minimum degree three forces the graph to be \(K_4\).

Otherwise, root the decomposition tree and choose a deepest node \(B\) having a child. All its children are leaves. For a child leaf bag \(L\), every vertex in \(L\setminus B\) occurs only in \(L\). Minimum degree three therefore implies that \(L\) has four vertices and every vertex in \(L\setminus B\) has degree three and is adjacent to the other three vertices of \(L\).

If \(L\setminus B\) contains two vertices, they lie in a triangle with a degree-three vertex. Otherwise write
\[
L=S\cup\{u\},\qquad S=L\cap B,\qquad |S|=3.
\]
Here \(N(u)=S\). If \(S\) contains an edge, there is again a triangle through a degree-three vertex. We may consequently assume that every such \(S\) is independent.

If \(B\) has two child leaves, their three-element intersections with \(B\) overlap in at least two vertices. Their private degree-three vertices, together with two common neighbors, give the required four-cycle.

It remains that \(B\) has exactly one child \(L=S\cup\{u\}\). Incomparability of adjacent bags implies
\[
B=S\cup\{w\}.
\]
If \(B\) is the root, then \(w\) occurs only in \(B\), so minimum degree gives \(N(w)=S\). Together with \(u\), this gives the four-cycle.

Otherwise let \(P\) be the parent bag. Choose \(x\in B\setminus P\). If \(x\in S\), then \(x\) occurs only in \(B\) and \(L\); independence of \(S\) leaves it at most the two possible neighbors \(u,w\), a contradiction. Thus
\[
B\setminus P=\{w\}.
\]
The vertex \(w\) occurs only in \(B\), so again \(N(w)=S\), producing the four-cycle. This proves the claim.

### Induction

Proceed by induction on the number of vertices.

Vertices of degree at most one can be deleted without changing either parameter.

If a degree-two vertex \(v\) has nonadjacent neighbors \(a,b\), suppress \(v\), replacing \(avb\) by \(ab\). This is an edge contraction and preserves treewidth at most three. Both parameters are preserved:

- cycles correspond under subdivision, preserving vertex-disjointness;
- a feedback vertex set using \(v\) can replace it by \(a\), while a feedback vertex set in the suppressed graph also works before suppression.

If the neighbors of a degree-two vertex are adjacent, there is a triangle through a vertex of degree at most three. Otherwise the graph has minimum degree at least three, and the structural claim applies.

In either remaining configuration, choose a cycle \(C\) and a two-element set \(A\subseteq V(C)\):

- for a triangle, let \(A\) be the other two vertices besides its low-degree vertex;
- for a four-cycle, let \(A\) be the other opposite pair.

Every vertex of \(C-A\) has degree at most one in \(H-A\). Thus cycles of \(H-A\) avoid all vertices of \(C\), and
\[
\nu(H)\ge1+\nu(H-A),
\qquad
\tau(H)\le2+\tau(H-A).
\]
By induction,
\[
\tau(H)
\le2+2\nu(H-A)
\le2\nu(H).
\]
All cases are covered. \(\square\)

## 4. Planar applications beyond bounded treewidth

### Radial completions of triangulations

Let \(T\) be a connected simple plane triangulation, with every face bounded by a triangle. It is convenient to regard the embedding on the sphere, so the outer face is treated identically to other faces.

For each face \(f\), introduce a vertex \(w_f\) adjacent to its three boundary vertices. Retain an arbitrary set
\[
E_0\subseteq E(T)
\]
of the original edges. Call the resulting graph \(G(T,E_0)\).

This construction is planar: insert each face vertex and its three incident edges inside its face, then delete the unwanted original edges.

Apply Theorem 1 with
\[
U=V(T),\qquad W=\{w_f:f\text{ a face of }T\}.
\]
The auxiliary graph \(F\) is exactly \(T\):

- every two vertices on a triangular face are adjacent in \(T\);
- every edge of \(T\) lies on a triangular face.

Each edge of \(T\) has two distinct incident faces, so its endpoints have two common neighbors in \(W\). Thus condition (S) holds regardless of whether that original edge is retained.

Finally, every retained original edge belongs to \(F\), so \(R\) is edgeless. We obtain
\[
\boxed{\nu(G(T,E_0))=\mu(T)}
\]
and
\[
\boxed{\tau(G(T,E_0))
\le\operatorname{vc}(T)
\le2\mu(T)
=2\nu(G(T,E_0)).}
\]

Two cases deserve emphasis.

- **No original edges retained:** \(G(T,\varnothing)\) is the vertex–face incidence, or radial, graph of \(T\).
- **All original edges retained:** every \(w_f\) is simplicial, so
  \[
  \boxed{\tau(G(T,E(T)))=\operatorname{vc}(T).}
  \]

These are genuinely beyond the bounded-treewidth argument: a full face-stellation contains \(T\) as a subgraph, and plane triangulations have unbounded treewidth. Their maximum degree is also unbounded.

The factor two is sharp even here. For \(T=K_3\), the full face-stellation is \(K_5-e\), and
\[
\nu(K_5-e)=1,\qquad \tau(K_5-e)=2.
\]

### A quadrangulation formulation

There is also a direct bipartite special case.

**Corollary 3.** Let \(Q\) be a 2-connected plane bipartite graph whose faces are all four-cycles. If one bipartition class \(W\) has maximum degree at most three, then
\[
\tau(Q)\le2\nu(Q).
\]

To check the support condition, take two neighbors \(u,v\) of \(w\in W\). Because \(d(w)\le3\), the two incident edges \(wu,wv\) are consecutive in the rotation at \(w\). The intervening face is a four-cycle
\[
u\,w\,v\,w'\,u,
\]
providing a second common neighbor \(w'\in W\). Since the other bipartition class \(U\) is independent, \(R\) is empty. Theorem 1 applies, and in fact identifies \(\nu(Q)\) with the matching number of its auxiliary graph \(F\).

## 5. What remains unresolved

The supported-pair hypothesis is a real restriction, not a disguised proof for all planar graphs.

For example, the planar octahedral graph has every vertex of degree four. In any partition satisfying the theorem’s degree condition, \(W\) must therefore be empty. Its residual graph is then the octahedron itself, whose minimum degree four rules out treewidth at most three. Thus even this small planar graph lies outside the sufficient condition.

Nor can one prove the original conjecture merely by adding face witnesses and applying the theorem. Such augmentation can increase the cycle-packing number: \(K_4\) has packing number one, whereas its full face-stellation has packing number
\[
\mu(K_4)=2.
\]
The resulting upper bound does not transfer back with the required right-hand side.

The verified progress is therefore:

- a supported-pair extension containing the entire treewidth-three case;
- additional planar examples of arbitrarily large treewidth;
- exact matching formulas for their cycle-packing numbers;
- exact vertex-cover formulas for full face-stellations.

A proof or counterexample for unrestricted planar graphs is still missing from this argument.