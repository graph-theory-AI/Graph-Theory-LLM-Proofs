```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A quotient-transfer argument proves the conjectured bound for a concrete planar subclass containing graphs of unbounded treewidth, but not for all planar graphs.",
  "would_publish": false,
  "caveats": "Special-case result only; no claim of novelty or of a representation theorem covering every planar graph."
}
```

# A partial result via thin outerplanar quotients

I do not prove or disprove Conjecture 4. The partial result below covers, in particular, planar subgraphs of
\[
H\boxtimes P\boxtimes K_q,
\]
where \(H\) is outerplanar, \(P\) is a path, and \(q\) is a fixed constant. This is an unbounded-treewidth subclass, since it contains all square grids.

The argument also identifies a precise obstruction to extending this method using paths that are geodesic only after previously chosen vertices have been deleted.

## 1. Definitions and the partial theorem

For a linear order \(L\) of \(V(G)\), let
\[
\operatorname{WReach}_r(G,L,v)
\]
be the set of vertices \(u\) for which there is a \(v\)-\(u\) path of length at most \(r\) on which \(u\) is the \(L\)-minimum vertex. Length-zero paths are allowed. Thus
\[
\operatorname{wcol}_r(G)
=\min_L\max_{v\in V(G)}
|\operatorname{WReach}_r(G,L,v)|.
\]

Let \(\mathcal P\) be a partition of \(V(G)\). Its quotient \(Q\) has vertex set \(\mathcal P\), with two distinct parts adjacent whenever an edge of \(G\) joins them. Parts need not be connected. Define
\[
b_r(\mathcal P)
=\max_{\substack{v\in V(G)\\ A\in\mathcal P}}
|B_r^G(v)\cap A|.
\]

**Partial theorem.** If \(Q\) is outerplanar, then, for every integer \(r\ge1\),
\[
\boxed{\quad
\operatorname{wcol}_r(G)
\le
b_r(\mathcal P)(2r+1)
\bigl(\lceil\log_2 r\rceil+2\bigr).
\quad}                                                    \tag{1}
\]
Consequently, if
\[
b_r(\mathcal P)\le q(2r+1)
\]
with \(q\) independent of \(G\) and \(r\), then
\[
\boxed{\quad
\operatorname{wcol}_r(G)
\le q(2r+1)^2
\bigl(\lceil\log_2 r\rceil+2\bigr)
=O_q(r^2\log(r+2)).
\quad}                                                    \tag{2}
\]

The outerplanar \(O(r\log r)\) bound is already part of the supplied source. I include a proof of the particular bound used here so that the partial argument is self-contained.

## 2. The quotient-transfer inequality

**Lemma 1.** For every partition \(\mathcal P\) and its quotient \(Q\),
\[
\operatorname{wcol}_r(G)
\le b_r(\mathcal P)\operatorname{wcol}_r(Q).                 \tag{3}
\]

**Proof.**
Choose an order \(L_Q\) witnessing \(\operatorname{wcol}_r(Q)\). Order the vertices of \(G\) in consecutive parts according to \(L_Q\), and order vertices within each part arbitrarily. Call the resulting order \(L\).

Suppose \(u\in\operatorname{WReach}_r(G,L,v)\), witnessed by a path \(R\). Let \(A_u,A_v\) be the parts containing \(u,v\). No vertex of \(R\) belongs to a part preceding \(A_u\) in \(L_Q\), because such a vertex would precede \(u\) in \(L\).

Projecting \(R\) onto \(Q\), suppressing consecutive repetitions, and then deleting cycles gives an \(A_v\)-\(A_u\) path of length at most \(r\) on which \(A_u\) is minimum. Hence
\[
A_u\in\operatorname{WReach}_r(Q,L_Q,A_v).
\]
There are at most \(\operatorname{wcol}_r(Q)\) possible parts \(A_u\). Within each such part, every possible \(u\) lies in \(B_r^G(v)\), giving at most \(b_r(\mathcal P)\) choices. This proves (3). \(\square\)

## 3. An explicit outerplanar bound

Put
\[
f(r)=\lceil\log_2 r\rceil+2 \qquad (r\ge1).
\]

### Paths

**Lemma 2.** Every path \(P\) satisfies
\[
\operatorname{wcol}_r(P)\le f(r).
\]

**Proof.**
Index the path vertices consecutively. Mark anchors at positions
\[
0,r,2r,\ldots.
\]
Order all anchors first, from left to right. Each component remaining after deleting the anchors has at most \(r-1\) vertices. Within each such component, use the recursive order that places a middle vertex first and then recursively orders the two remaining subpaths.

The recursion tree in a component has height at most \(\lceil\log_2 r\rceil\). Any vertex weakly reachable within that component must be an ancestor in this recursion tree: otherwise the path to it contains an earlier separating middle vertex.

A non-anchor cannot weakly reach a non-anchor in a different component, since the intervening anchor is earlier than the target. It can weakly reach at most two anchors within distance \(r\). An anchor can weakly reach only itself and possibly its preceding anchor. Thus the bound is \(f(r)\). \(\square\)

### Outerplanar graphs

**Lemma 3.** Every outerplanar graph \(H\) satisfies
\[
\operatorname{wcol}_r(H)\le (2r+1)f(r).                     \tag{4}
\]

**Proof.**
Graphs on at most two vertices are immediate. Otherwise, extend \(H\) to a maximal outerplanar graph \(M\) on the same vertex set. Weak coloring numbers are monotone under taking subgraphs, so it suffices to order \(M\). Recall that a maximal outerplanar graph is chordal.

Choose a root and let \(L_0,L_1,\ldots\) be its BFS layers. We need two properties.

**(a) Every layer induces a linear forest.**  
For \(j\ge1\), contract the connected ball formed by the layers below \(L_j\) to one vertex, and delete higher layers. The resulting outerplanar minor contains \(M[L_j]\) together with a vertex adjacent to every vertex of \(L_j\).

If \(M[L_j]\) contained a cycle, this cone would contain a \(K_4\) minor. If it contained a vertex with three neighbors in \(L_j\), the cone would contain \(K_{2,3}\) as a subgraph. Neither is possible in an outerplanar graph. Thus \(M[L_j]\) is acyclic and has maximum degree at most two. The assertion for \(L_0\) is immediate.

**(b) Upper-component shadows are cliques of size at most two.**  
Let \(C\) be a component of
\[
M\Big[\bigcup_{k>j}L_k\Big],
\qquad
S(C)=N(C)\cap L_j.
\]
The set \(S(C)\) is a clique. Indeed, if nonadjacent \(x,y\in S(C)\) existed, take an induced \(x\)-\(y\) path with interior in \(C\). For \(j\ge1\), also take an induced \(x\)-\(y\) path with interior in the layers below \(L_j\). The two interiors have no edges between them, since their BFS levels differ by at least two. Their union is therefore an induced cycle of length at least four, contradicting chordality. For \(j=0\), the shadow has at most one vertex.

By (a), a clique in \(M[L_j]\) has size at most two.

Now order layers increasingly. Within each layer, use the orders from Lemma 2 on its path components.

Fix \(v\in L_i\), and suppose \(u\in L_j\) is weakly \(r\)-reachable from \(v\). Necessarily
\[
\max\{0,i-r\}\le j\le i.
\]
A witnessing path cannot visit a layer below \(L_j\), since every vertex there precedes \(u\).

Any excursion of this path above \(L_j\), between two vertices of \(L_j\), can be replaced by an edge: the two endpoints belong to the same upper-component shadow, which is a clique. These replacements do not increase length or introduce earlier vertices.

If \(j=i\), this gives a witnessing path inside \(M[L_i]\) starting at \(v\), so there are at most \(f(r)\) possible targets.

If \(j<i\), the path first enters \(L_j\) through the shadow of the upper component containing \(v\). There are at most two possible entry vertices. After the replacements, \(u\) is weakly \(r\)-reachable inside \(M[L_j]\) from one of these two vertices. Thus there are at most \(2f(r)\) possible targets in \(L_j\).

There are at most \(r\) relevant layers below \(L_i\), giving
\[
|\operatorname{WReach}_r(M,L,v)|
\le f(r)+2r f(r).
\]
This proves (4). \(\square\)

Combining Lemmas 1 and 3 proves (1) and (2).

## 4. Concrete subclasses covered

### 4.1. Outerplanar–path products

**Corollary 4.** Let \(H\) be outerplanar, \(P\) a path, and \(q\ge1\). Every subgraph
\[
G\subseteq H\boxtimes P\boxtimes K_q
\]
satisfies
\[
\operatorname{wcol}_r(G)
\le q(2r+1)^2f(r).
\]

**Proof.**
Partition \(V(G)\) by the \(H\)-coordinate. The quotient is a subgraph of \(H\), hence outerplanar.

Along every edge of the strong product, the \(P\)-coordinate changes by at most one. Therefore, for fixed \(v\), vertices in \(B_r^G(v)\) have at most \(2r+1\) possible \(P\)-coordinates. Within a fixed part, each such coordinate supports at most \(q\) vertices. Hence
\[
b_r(\mathcal P)\le q(2r+1),
\]
and (2) applies. \(\square\)

The corollary does not require \(G\) itself to be planar. Its planar members give the claimed special case of Conjecture 4.

In particular, an \(m\times n\) grid has a partition into rows whose quotient is a path. Using Lemma 2 directly in (3) gives the stronger estimate
\[
\operatorname{wcol}_r(P_m\square P_n)
\le (2r+1)f(r)=O(r\log(r+2)).
\]
Thus the partial result is not restricted to bounded-treewidth planar graphs.

### 4.2. Globally geodesic path partitions

A second sufficient condition is geometric.

Suppose every part of \(\mathcal P\) is covered by at most \(q\) paths that are isometric **in the original graph \(G\)**. For an isometric path \(R\), consider the first and last vertices \(x,y\) of \(R\cap B_r^G(v)\), if this intersection is nonempty. Then
\[
d_R(x,y)=d_G(x,y)
\le d_G(x,v)+d_G(v,y)\le2r.
\]
Consequently,
\[
|R\cap B_r^G(v)|\le2r+1.
\]
Summing over the paths covering a part yields
\[
b_r(\mathcal P)\le q(2r+1).
\]

Therefore:

> If a graph has an outerplanar quotient partition whose parts are each covered by a fixed number of globally isometric paths, then it satisfies the conjectured \(O(r^2\log r)\) bound.

This is a sufficient-condition theorem, not a claim that all planar graphs possess such a partition.

## 5. The gap in extending this approach

The missing ingredient is control of the parts in the **original metric**, compatible with an order having small weak coloring number on the quotient. Planarity alone has not supplied that control here.

In particular, “isometric after deleting earlier parts” cannot simply be substituted for global isometry when the parts are subsequently reordered.

Consider the fan consisting of a path
\[
p_1p_2\cdots p_n
\]
and a vertex \(z\) adjacent to every \(p_i\). This is outerplanar. Delete \(z\) first; the remaining path is certainly isometric in the remaining graph. The two-part quotient of
\[
\{z\},\qquad \{p_1,\ldots,p_n\}
\]
is just \(K_2\). Nevertheless,
\[
|B_1(z)\cap\{p_1,\ldots,p_n\}|=n,
\]
so the required thinness estimate fails arbitrarily badly.

Moreover, if the path part is ordered before \(z\), then
\[
|\operatorname{WReach}_1(G,L,z)|=n+1.
\]
This does not contradict any weak-coloring-number bound—the minimum over orders can put \(z\) first. It shows exactly why an arbitrary good quotient order cannot be combined with paths that were geodesic only in a different deletion order.

Hence the argument establishes a uniform \(O(r^2\log r)\) bound for the stated subclasses, but gives neither an improved bound for arbitrary planar graphs nor a counterexample. No novelty is claimed for these special-case consequences.