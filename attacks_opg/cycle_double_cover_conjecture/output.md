```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained splitting argument proves CDC for bridgeless graphs with at most ten odd-degree vertices, but does not settle the conjecture.",
  "would_publish": false,
  "caveats": "Elementary special case; no novelty claimed, and unrestricted cubic cores remain untreated."
}
```

## 1. A proved special case

I do not obtain a proof or counterexample to the full conjecture. The following is a self-contained special case, not a claimed improvement over the literature.

**Theorem.** Let \(G\) be a finite bridgeless graph.
1. If \(G\) has at most ten vertices of odd degree, then \(G\) has a cycle double cover.
2. If \(G\) has at most eight vertices of odd degree, then there are three even subgraphs of \(G\) covering each edge exactly twice. Decomposing these into cycles gives a cycle double cover.

The graph may have arbitrarily many even-degree vertices, so this is not merely a small-order verification.

An **even subgraph** has even degree at every vertex. During reductions, parallel edges and loops are allowed: two parallel edges form a 2-cycle, and a loop forms a 1-cycle. For an original simple graph, the final cover consists only of ordinary simple cycles. Covers are multisets.

The proof uses no computer enumeration.

## 2. Splitting down to the odd-degree vertices

### 2.1. Covers lift through splitting

Let \(va,vb\) be distinct nonloop edges incident with \(v\), allowing \(a=b\). **Splitting off** this pair means deleting \(va,vb\) and adding a distinguished new edge \(ab\).

**Lemma 1.** If the split graph has a cycle double cover, then the original graph has one.

**Proof.** In every covering cycle containing the new edge \(ab\), replace that edge by the two-edge walk \(a,v,b\). The result is a closed trail: its edges are distinct, although it may repeat \(v\).

Every closed trail decomposes into edge-disjoint simple cycles, by splitting at repeated vertices. After making these decompositions, every unchanged edge is still covered twice, while each of \(va,vb\) is covered twice because \(ab\) was covered twice. ∎

The same operation preserves the stronger property of having three even subgraphs covering every edge twice: replace \(ab\) by \(av,vb\) in whichever two subgraphs contain it. Degrees remain even.

Suppressing a degree-two vertex is another instance of this operation. A deleted loop can be restored by adding two copies of its 1-cycle—or by placing it in two of the three even subgraphs.

### 2.2. A bridgelessness-preserving pair always exists

Here is the splitting fact needed for the reduction.

**Lemma 2.** Let \(G\) be a connected loopless bridgeless multigraph, and let \(d_G(v)\ge 4\). Some pair of edges incident with \(v\) can be split off so that the resulting graph remains connected and bridgeless.

**Proof.** Write \(H=G-v\), and regard the \(d=d_G(v)\) incident edges as distinct labelled attachments to \(H\).

For a proposed pair \(va,vb\), let \(G'\) be the split graph. For every nonempty \(S\subseteq V(G)\setminus\{v\}\),
\[
|\delta_{G'}(S)|=
\begin{cases}
|\delta_G(S)|-2,&a,b\in S,\\
|\delta_G(S)|,&\text{otherwise}.
\end{cases}
\]
Consequently, it suffices to choose a pair for which no set containing both endpoints has a cut of size two or three in \(G\).

**Case 1: \(H\) is disconnected.**  
Choose the two attachments in different components of \(H\). If \(S\) contains their endpoints, it meets at least two components of \(H\). Each nonempty componentwise part of \(S\) has at least two edges in its cut in \(G\), since \(G\) is connected and bridgeless. These contributions add, giving
\[
|\delta_G(S)|\ge 4.
\]

**Case 2: \(H\) is connected.**  
Suppose a set \(S\) containing both endpoints satisfies \(|\delta_G(S)|\le 3\). It cannot be all of \(V(H)\), whose cut has size \(d\ge4\). Thus
\[
|\delta_G(S)|
=
|\delta_H(S)|+\#\{\text{attachments in }S\}
\]
forces
\[
|\delta_H(S)|=1,\qquad
\#\{\text{attachments in }S\}=2.
\]
A forbidden pair therefore consists precisely of the two attachments on one side of a bridge of \(H\).

Distinct forbidden pairs are disjoint. Indeed, bridge cuts are compatible: for any two such bipartitions, one of their four intersections is empty. If two distinct two-element attachment sets overlapped, their intersection and their two differences would all be nonempty; because \(d\ge4\), their common complement would also be nonempty. This contradicts compatibility.

Thus the forbidden pairs form a matching on the \(d\) attachments. Since \(d\ge4\), some pair is not forbidden. Splitting that pair leaves every nontrivial cut with size at least two. ∎

### 2.3. The resulting cubic core

**Corollary 3.** Suppose a connected bridgeless graph has \(k>0\) odd-degree vertices. By deleting loops, suppressing degree-two vertices, and applying Lemma 2, it can be reduced to a connected bridgeless cubic multigraph on exactly \(k\) vertices. A cycle double cover of the final graph lifts to one of the original graph.

**Proof.** Repeatedly:

- delete and record loops;
- suppress degree-two vertices;
- split off an admissible pair at any vertex of degree at least four.

Suppressing a degree-two vertex preserves connectedness and bridgelessness: cycles using that vertex simply have their two-edge passage replaced by the new edge. Loop deletion does not affect connectivity between distinct vertices.

Every operation reduces the number of edges, so the process terminates. The operations preserve the degree parity of every surviving vertex, and only even-degree vertices are suppressed. Because \(k>0\), some odd-degree vertices remain throughout.

At termination, every vertex has degree three. Hence the remaining vertices are exactly the original \(k\) odd-degree vertices. Cover lifting follows from Lemma 1 and the observations following it. ∎

A component having no odd-degree vertices is already even: decompose its edges into cycles and take each cycle twice.

## 3. Cubic graphs on at most ten vertices

We next prove the small-core fact needed above.

**Lemma 4.** Every connected bridgeless cubic multigraph on fewer than ten vertices is 3-edge-colourable. Every such graph on ten vertices is either 3-edge-colourable or isomorphic to the Petersen graph.

A bridgeless cubic multigraph has no loops: a loop at a cubic vertex would leave its only nonloop edge as a bridge.

### Parallel edges

Suppose \(u,v\) have two parallel edges.

If there are three parallel edges, their connected component is immediately 3-edge-colourable. Otherwise let \(ua,vb\) be the remaining incident edges. Here \(a\ne b\): if \(a=b\), the third edge at that common neighbour would be a bridge.

Delete \(u,v\) and add \(ab\). The resulting cubic graph is bridgeless. To see this, any cycle using either external edge \(ua,vb\) uses both and one of the parallel \(uv\)-edges; replacing that passage by \(ab\) gives a cycle in the reduced graph. This also shows that the new edge lies on a cycle.

A 3-edge-colouring lifts: give \(ua,vb\) the colour of \(ab\), and give the two \(uv\)-edges the other two colours.

### Triangles

Contract a triangle to one vertex. This produces a smaller bridgeless cubic multigraph; a bridge after contraction would lift to a bridge before contraction.

In a 3-edge-colouring of the contracted graph, the three external edges have distinct colours. Colour each triangle edge with the colour of the external edge at the opposite triangle vertex. This extends the colouring.

### Squares

We may now assume the graph is simple and triangle-free. Let
\[
v_1v_2v_3v_4v_1
\]
be a square, and let \(x_i\) be the neighbour of \(v_i\) outside the square. Consider the two reductions obtained by deleting the square and adding respectively
\[
\{x_1x_2,x_3x_4\}
\quad\text{or}\quad
\{x_1x_4,x_2x_3\}.
\tag{1}
\]
The added edges are not loops, because equality of adjacent \(x_i\)'s would give a triangle.

At least one reduction is bridgeless. Here are the details.

Let \(H=G-\{v_1,v_2,v_3,v_4\}\), with its four attachments counted with multiplicity. Every component of \(H\) has at least two attachments, or its only attachment edge would be a bridge of \(G\). Thus \(H\) is connected, or has two components with two attachments each.

- If \(H\) is connected, every bridge of \(H\) separates the attachments as \(1+3\) or \(2+2\). Every pairing crosses a \(1+3\) separation. Moreover, all bridge-induced \(2+2\) separations are the same bipartition: two distinct \(2+2\) bipartitions would cross, contrary to compatibility of bridge cuts. Hence at most one of the three pairings of the attachments can leave a bridge. In particular, at least one pairing in (1) works. Newly added edges are not bridges because their endpoints were already connected in \(H\).

- If \(H\) has two components with two attachments each, pairing inside the components closes all their bridges into cycles. Pairing across the components joins them by two edges and again closes every bridge into a cycle. Thus either pairing in (1) works.

Suppose the first reduction is chosen, and its two new edges receive colours \(\alpha,\beta\). Give \(v_1x_1,v_2x_2\) colour \(\alpha\), and \(v_3x_3,v_4x_4\) colour \(\beta\).

If \(\alpha=\beta\), alternate the other two colours around the square. If \(\alpha\ne\beta\), writing \(\gamma\) for the third colour, colour the square edges in cyclic order by
\[
\beta,\gamma,\alpha,\gamma.
\]
This is a proper extension. The other reduction is symmetric.

### The only remaining ten-vertex graph

The preceding reductions strictly decrease order. Thus induction reduces the lemma to simple cubic graphs of girth at least five.

For any vertex \(r\), its three neighbours and their six other neighbours are all distinct. Therefore
\[
|V(G)|\ge 1+3+6=10.
\]

If equality holds, the six distance-two vertices induce a 2-regular graph of girth at least five, hence a 6-cycle. The two children of each neighbour of \(r\) cannot have distance one or two on this 6-cycle, as that would produce a triangle or a square. They must therefore be opposite vertices of the 6-cycle.

This determines a unique graph: the Petersen graph. Thus all graphs of order below ten are 3-edge-colourable, and the only possible exception at order ten is Petersen. ∎

## 4. Covers of the terminal graphs

### The 3-edge-colourable case

For a cubic graph with edge colours \(1,2,3\), let \(F_{ij}\) consist of the edges coloured \(i\) or \(j\). Each of
\[
F_{12},\quad F_{13},\quad F_{23}
\]
is 2-regular, and every edge belongs to exactly two of them. Their cycle components form a cycle double cover.

### An explicit Petersen cover

Use the standard Petersen labelling
\[
V(P)=\{u_i,v_i:i\in\mathbb Z/5\mathbb Z\},
\]
with edges
\[
u_iu_{i+1},\qquad u_iv_i,\qquad v_iv_{i+2}.
\]

Take the outer pentagon
\[
U=(u_0,u_1,u_2,u_3,u_4,u_0)
\]
and the five pentagons
\[
D_i=(u_i,u_{i+1},v_{i+1},v_{i+3},v_i,u_i),
\qquad i\in\mathbb Z/5\mathbb Z.
\]

These six cycles form a double cover:

- \(u_iu_{i+1}\) occurs in \(U\) and \(D_i\);
- \(u_iv_i\) occurs in \(D_i\) and \(D_{i-1}\);
- the two inner-edge positions in the cyclic family \(D_i\) each run through all five inner edges once.

Thus every Petersen edge occurs exactly twice.

### Completion of the theorem

Process the original graph componentwise.

- An all-even component has a cycle decomposition, which can be doubled.
- A component with \(k>0\) odd-degree vertices reduces, by Corollary 3, to a bridgeless cubic graph on \(k\) vertices.
- If \(k\le10\), Lemma 4 and the explicit constructions above provide a cycle double cover of that core.
- Undoing the reductions gives a cycle double cover of the original component.

If the total number of odd-degree vertices is at most eight, every cubic core is 3-edge-colourable. Its three even covering subgraphs lift through all the reductions. On an all-even component, place the entire component in two of the three subgraphs and leave the third empty. This proves the second assertion as well.

The construction is polynomial-time on this class: there are at most \(O(|E(G)|)\) reductions, admissible pairs can be found by testing pairs and checking bridges, and the terminal cubic graphs have constant order.

In particular:

**Corollary.** Any counterexample to CDC must have at least twelve odd-degree vertices.

## 5. A concrete obstruction to a tempting continuation

The colouring construction suggests trying to prescribe a 2-factor as part of the cover and then cover the remaining multiplicities. That stronger approach already fails for Petersen.

Let \(F\) be the Petersen 2-factor consisting of its outer and inner pentagons, and let \(M\) be its five spokes.

**Claim.** No cycle double cover of Petersen contains both pentagons of \(F\).

**Proof.** Suppose it did, and remove one copy of each prescribed pentagon. The remaining multiplicities are:

- one copy of every edge of \(F\);
- two copies of every edge of \(M\).

At each vertex, the remaining cycles must pair each of the two \(F\)-edges with a copy of the spoke. Indeed, the prescribed pentagon has already used the pairing of the two \(F\)-edges. Thus every remaining cycle alternates between \(F\) and \(M\).

Each spoke switches between the outer and inner vertex sets, while an \(F\)-edge stays in one set. A closed alternating cycle therefore uses an even number of spokes and has length divisible by four.

Petersen has girth five and ten vertices, so every such simple cycle has length eight. But the total remaining edge multiplicity is
\[
10+2\cdot5=20,
\]
which cannot be a sum of eights. Contradiction. ∎

This is **not** a counterexample to CDC—the six pentagons above give a CDC. It shows that an arbitrary chosen 2-factor cannot simply be fixed and extended.

## 6. The unresolved gap

The partial theorem is completely covered by the arguments above. The gap to the full conjecture is precise: after the splitting reduction, a graph with more odd-degree vertices may leave an unrestricted bridgeless cubic core. The small-cycle reductions and ten-vertex classification do not produce covers for those cores.

Thus the argument supplies a constructive special case and rules out one naive extension strategy, but makes no claim to resolve the general cycle double cover conjecture.