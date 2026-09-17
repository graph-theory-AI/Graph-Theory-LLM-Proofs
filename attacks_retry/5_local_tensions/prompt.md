Attack the following open graph-theory problem.

Catalog id: 5_local_tensions
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/5_local_tensions/
Original entry: http://www.openproblemgarden.org/op/5_local_tensions
Problem attributed to: DeVos, Matt (posted 2007-06-22)

=== Problem statement (OpenProblemGarden) ===
Title: 5-local-tensions
Conjecture There exists a fixed constant $ c $ (probably $ c=4 $ suffices) so that every embedded (loopless) graph with edge-width $ \ge c $ has a 5-local-tension.

=== Discussion / context (OpenProblemGarden) ===
The edge-width of an embedded graph is the length of the shortest non-contractible cycle. Definition Let $ G $ be a directed graph, let $ \Gamma $ be an abelian group, and let $ \phi : E(G) \rightarrow \Gamma $ . Define the height of a walk $ W $ to be the sum of $ \phi $ on the forward edges of $ W $ minus the sum of $ \phi $ on the backward edges of $ W $ (edges are counted according to multiplicity). We call $ \phi $ a tension if the height of every closed walk is zero, and if $ G $ is an embedded graph, we call $ \phi $ a local-tension if the height of every closed walk which forms a contractible curve is zero. If in addition, $ \Gamma = {\mathbb Z} $ and $ 0 < \phi(e) < k $ for some $ k \in {\mathbb Z} $ , we say that $ \phi $ is a $ k $ - tension or a $ k $ - local-tension . If we reverse an edge $ e $ and replace $ \phi(e) $ by $ -\phi(e) $ , this preserves the properties of tension or local-tension. Accordingly, we say that an undirected graph (embedded graph) $ G $ has a $ k $ -tension ( $ k $ -local-tension) if some and thus every orientation of it admits such a map. Proposition A graph has a $ k $ -tension if and only if it is $ k $ -colorable. Proof To see the "if" direction, let $ f : V(G) \rightarrow \{0,\ldots,k-1\} $ be a coloring, orient the edges of $ G $ arbitrarily, and defining $ \phi : E(G) \rightarrow {\mathbb Z} $ by the rule $ \phi(uv) = f(v) - f(u) $ . It is straightforward to check that $ \phi $ is a $ k $ -tension. For the "only if" direction, let $ \phi : E(G) \rightarrow {\mathbb Z} $ be a $ k $ -tension. Now choose a point $ u \in V(G) $ and define the map $ f : V(G) \rightarrow {\mathbb Z}_k $ by the rule that $ f(v) $ is the height of some (and thus every) walk from $ u $ to $ v $ modulo $ k $ . Again, it is straightforward to check that this defines a proper $ k $ -coloring. For graphs on orientable surfaces, local-tensions are dual to flows. More precisely, if $ G $ and $ G^* $ are dual graphs embedded in an orientable surface, then $ G $ has a $ k $ -local-tension if and only if $ G^* $ has a nowhere-zero $ k $ -flow. On non-orientable surfaces, there is a duality between $ k $ -local-tensions in $ G $ and nowhere-zero $ k $ -flows in a bidirected $ G^* $ . Based on this duality we have a couple of conjectures. The first follows from Tutte's 5-flow conjecture , the second from Bouchet's 6-flow conjecture . Conjecture (Tutte) Every loopless graph embedded in an orientable surface has a 5-local-tension. Conjecture (Bouchet) Every loopless graph embedded in any surface has a 6-local-tension. So although, graphs on surfaces may have high chromatic number, thanks to some partial results toward the above conjectures, we know that they always have small local-tensions. For orientable surfaces, there is a famous Conjecture of Grunbaum which is equivalent to the following. Conjecture (Grunbaum) If $ G $ is a simple loopless graph embedded in an orientable surface with edge-width $ \ge 3 $ , then $ G $ has a 4-local-tension. On non-orientable surfaces, it is known that there are graphs of arbitrarily high edge-width which do not admit 4-local-tensions (see [DGMVZ]). However, it remains open whether sufficiently high edge-width forces the existence of a 5-local-tension. Indeed, as suggested by the conjecture at the start of this page, it may be that edge-width at least 4 is enough. Edge-width 3 does not suffice since the embedding of $ K_6 $ in the projective plane does not admit a 5-local-tension.

=== References listed by OpenProblemGarden ===
- *[DGMVZ] M. DeVos, L. Goddyn, B. Mohar, D. Vertigan, and X. Zhu, Coloring-flow duality of embedded graphs. Trans. Amer. Math. Soc. 357 (2005), no. 10 MathSciNet

=== Catalog page (statement + literature review) ===
5-local-tensions — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that every loopless graph embedded in a non-orientable surface with edge-width at least some fixed constant $c$ (probably $c=4$) admits a $5$-local-tension remains open. No post-2007 paper resolving or substantially advancing this specific conjecture was found in the literature. Related progress on Bouchet's 6-flow conjecture for signed/bidirected graphs (e.g., DeVos 2013 establishing a nowhere-zero 12-flow bound for bidirected graphs) does not directly settle this edge-width-conditioned variant.

 Reviewer notes. The OPG page itself (http://www.openproblemgarden.org/op/5_local_tensions) returned ECONNREFUSED and could not be checked for editorial updates. The arXiv search for 'local tension' combined with 'non-orientable' and 'edge-width' returned no results, suggesting the specific conjecture has attracted little direct attention in the literature under that terminology. DeVos's 2013 arXiv preprint 1310.8406 (Flows on Bidirected Graphs) is the closest post-2007 related work: it shows every bidirected graph admitting a nowhere-zero ℤ-flow has a nowhere-zero 12-flow, which by the non-orientable duality framework of DGMVZ gives a 12-local-tension bound for embedded graphs—far weaker than the conjectured 5-local-tension. Progress on Bouchet's 6-flow conjecture for signed graphs (recent papers proving it for cyclically 5-edge-connected cubic signed graphs, arxiv 2601.05692) is in a closely related but technically distinct setting. The Grünbaum conjecture (4-local-tension on orientable surfaces with edge-width ≥ 3) remains open on the orientable side; the non-orientable 5-local-tension conjecture is separate.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 226s.
 

Conjecture. There exists a fixed constant $ c $ (probably $ c=4 $ suffices) so that every embedded (loopless) graph with edge-width $ \ge c $ has a 5-local-tension.

Keywords:
coloring · surface · tension

Discussion

The edge-width of an embedded graph is the length of the shortest non-contractible cycle. Definition Let $ G $ be a directed graph, let $ \Gamma $ be an abelian group, and let $ \phi : E(G) \rightarrow \Gamma $ . Define the height of a walk $ W $ to be the sum of $ \phi $ on the forward edges of $ W $ minus the sum of $ \phi $ on the backward edges of $ W $ (edges are counted according to multiplicity). We call $ \phi $ a tension if the height of every closed walk is zero, and if $ G $ is an embedded graph, we call $ \phi $ a local-tension if the height of every closed walk which forms a contractible curve is zero. If in addition, $ \Gamma = {\mathbb Z} $ and $ 0 < \phi(e) < k $ for some $ k \in {\mathbb Z} $ , we say that $ \phi $ is a $ k $ - tension or a $ k $ - local-tension . If we reverse an edge $ e $ and replace $ \phi(e) $ by $ -\phi(e) $ , this preserves the properties of tension or local-tension. Accordingly, we say that an undirected graph (embedded graph) $ G $ has a $ k $ -tension ( $ k $ -local-tension) if some and thus every orientation of it admits such a map. Proposition A graph has a $ k $ -tension if and only if it is $ k $ -colorable. Proof To see the "if" direction, let $ f : V(G) \rightarrow \{0,\ldots,k-1\} $ be a coloring, orient the edges of $ G $ arbitrarily, and defining $ \phi : E(G) \rightarrow {\mathbb Z} $ by the rule $ \phi(uv) = f(v) - f(u) $ . It is straightforward to check that $ \phi $ is a $ k $ -tension. For the "only if" direction, let $ \phi : E(G) \rightarrow {\mathbb Z} $ be a $ k $ -tension. Now choose a point $ u \in V(G) $ and define the map $ f : V(G) \rightarrow {\mathbb Z}_k $ by the rule that $ f(v) $ is the height of some (and thus every) walk from $ u $ to $ v $ modulo $ k $ . Again, it is straightforward to check that this defines a proper $ k $ -coloring. For graphs on orientable surfaces, local-tensions are dual to flows. More precisely, if $ G $ and $ G^* $ are dual graphs embedded in an orientable surface, then $ G $ has a $ k $ -local-tension if and only if $ G^* $ has a nowhere-zero $ k $ -flow. On non-orientable surfaces, there is a duality between $ k $ -local-tensions in $ G $ and nowhere-zero $ k $ -flows in a bidirected $ G^* $ . Based on this duality we have a couple of conjectures. The first follows from Tutte's 5-flow conjecture , the second from Bouchet's 6-flow conjecture . Conjecture (Tutte) Every loopless graph embedded in an orientable surface has a 5-local-tension. Conjecture (Bouchet) Every loopless graph embedded in any surface has a 6-local-tension. So although, graphs on surfaces may have high chromatic number, thanks to some partial results toward the above conjectures, we know that they always have small local-tensions. For orientable surfaces, there is a famous Conjecture of Grunbaum which is equivalent to the following. Conjecture (Grunbaum) If $ G $ is a simple loopless graph embedded in an orientable surface with edge-width $ \ge 3 $ , then $ G $ has a 4-local-tension. On non-orientable surfaces, it is known that there are graphs of arbitrarily high edge-width which do not admit 4-local-tensions (see [DGMVZ]). However, it remains open whether sufficiently high edge-width forces the existence of a 5-local-tension. Indeed, as suggested by the conjecture at the start of this page, it may be that edge-width at least 4 is enough. Edge-width 3 does not suffice since the embedding of $ K_6 $ in the projective plane does not admit a 5-local-tension.

Bibliography

★ [DGMVZ]
 M. DeVos, L. Goddyn, B. Mohar, D. Vertigan, and X. Zhu, Coloring-flow duality of embedded graphs. Trans. Amer. Math. Soc. 357 (2005), no. 10 MathSciNet
 MathSciNet

Related conjectures

 
 related to
 5-flow conjecture
 partial
 The connection is flow/local-tension surface duality: as the source page states, Tutte's 5-flow conjecture implies the companion conjecture 'every loopless graph embedded in an ORIENTABLE surface has a 5-local-tension' (local-tensions on G dualize to flows on G*). But the headline 5-local-tensions conjecture (edge-width >= c implies 5-local-tension) ranges over all surfaces; on non-orientable surfaces duality produces flows on BIDIRECTED graphs (Bouchet's setting, parameter 6, not 5), so the 5-flow conjecture covers only the orientable subfamily of the source conjecture. Nor does the source imply the 5-flow conjecture (it is a statement about embedded graphs of large edge-width, not all bridgeless graphs). Subfamily implication only, hence related_only.
 

 
 related to
 Bouchet's 6-flow conjecture
 partial
 Bouchet's conjecture concerns nowhere-zero 6-flows on bidirected graphs, which by duality (as both pages note: 'flows on bidirected graphs arise naturally as duals of local-tensions on a non-orientable surface') implies a 6-LOCAL-TENSION statement for graphs embedded in non-orientable surfaces. The headline source conjecture asks for a 5-local-tension under an edge-width >= c hypothesis; the parameters differ (6 vs 5), so Bouchet's conjecture does not imply it, and the source conjecture, being restricted to large edge-width embeddings and to the number 5, does not imply Bouchet's statement about all bidirected graphs. They are linked by the same duality framework and Bouchet's conjecture is evidence/motivation, but there is no implication in either direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every loopless 6-regular cellular triangulation has a 5-local-tension, and edge-width at least 4 suffices for graphs of maximum degree at most 5.",
  "would_publish": false,
  "caveats": "Only special cases are proved; no constant for unrestricted embeddings is established, and no literature novelty is claimed."
}
```

## 1. Results obtained

I do not resolve the unrestricted conjecture. I prove two special cases.

**Theorem A — Flat triangulations.**  
Let \(G\) be a finite loopless graph cellularly embedded in a closed connected surface, with every face triangular and every vertex of degree \(6\). Then \(G\) has a \(5\)-local-tension.

Such a surface necessarily has Euler characteristic zero, so this theorem concerns the torus and Klein bottle. The proof is constructive and requires **no edge-width assumption**.

**Theorem B — Bounded maximum degree.**  
Every loopless embedded graph of maximum degree at most \(5\) and edge-width at least \(4\) has an ordinary \(5\)-tension, hence a \(5\)-local-tension.

The threshold \(4\) in Theorem B is best possible, using the projective-plane embedding of \(K_6\) described in the question.

Throughout, on a fixed orientation I use the condition
\[
1\leq |\phi(e)|\leq k-1.
\]
Reorienting negatively valued edges gives the positive-value convention in the question.

## 2. Local tensions as equivariant integer heights

The following elementary formulation will supply both the construction and its verification.

**Height lemma.**  
Let \(G\) be a connected cellularly embedded graph in a surface \(S\). Let \(\widetilde G\) be its lift to the universal covering surface, and let \(\Gamma\) be the deck group. A \(k\)-local-tension on \(G\) is equivalent to a function
\[
H:V(\widetilde G)\longrightarrow \mathbb Z
\]
such that

1. for every edge \(uv\) of \(\widetilde G\),
   \[
   1\leq |H(v)-H(u)|\leq k-1;
   \]
2. for every \(\gamma\in\Gamma\), there is an integer \(\tau(\gamma)\), independent of \(v\), satisfying
   \[
   H(\gamma v)=H(v)+\tau(\gamma).
   \]

Moreover, \(\tau:\Gamma\to\mathbb Z\) is a homomorphism.

**Proof.** Pull back a local tension to \(\widetilde G\). Its integral around every closed walk is zero: the projected walk is null-homotopic in \(S\). Equivalently, one may use vanishing on facial boundaries and simple connectedness of the covering surface. Integration from a fixed vertex therefore defines \(H\).

Deck invariance of the pulled-back edge values implies that \(H\circ\gamma-H\) has zero difference across every edge, and hence is constant. Composition gives the homomorphism property.

Conversely, condition 2 makes the edge differences of \(H\) descend to \(G\). A contractible closed walk lifts to a closed walk, on which these differences telescope to zero. This verifies the full contractible-walk condition, not merely the facial conditions. ∎

## 3. Proof of Theorem A

### 3.1. The universal cover is the triangular lattice

Write \(v,e,f\) for the numbers of vertices, edges and faces. The assumptions give
\[
2e=6v,\qquad 3f=2e,
\]
so
\[
\chi(S)=v-e+f=0.
\]

Give each face the metric of a unit equilateral triangle. Exactly six angles of size \(\pi/3\) meet at each vertex, so this is a flat metric without singularities. Its universal cover is a complete simply connected flat surface, hence the Euclidean plane. The lifted triangulation is the standard triangular tiling.

Use coordinates
\[
V(T)=\mathbb Z^2,
\]
with edge differences
\[
\pm(1,0),\qquad \pm(0,1),\qquad \pm(-1,1).
\]
The corresponding Euclidean coordinates are
\[
(i,j)\longmapsto \left(i+\frac j2,\frac{\sqrt3\,j}{2}\right).
\]

The deck group consists of Euclidean isometries preserving this tiling and acts freely. An orientation-preserving Euclidean isometry other than a translation has a fixed point. Consequently every orientation-preserving deck transformation is a translation.

If orientation-reversing transformations occur, all have the same linear reflection part: otherwise the product of two would be a nontranslation orientation-preserving isometry. Up to a symmetry of the triangular lattice, the reflection axis is either parallel or perpendicular to an edge direction.

We handle these possibilities separately.

### 3.2. Translations, and reflections parallel to an edge direction

If all deck transformations are translations, set
\[
H(i,j)=2i+j.
\]
Its differences on the three edge directions are \(2,1,-1\). Translation by \((p,q)\) changes \(H\) by the constant \(2p+q\). The height lemma therefore gives a \(3\)-local-tension.

The same construction works when the common reflection axis is parallel to an edge direction. Choose coordinates so that its linear part is
\[
R_{\parallel}(i,j)=(i+j,-j).
\]
Then
\[
H(R_{\parallel}(i,j))=2(i+j)-j=2i+j=H(i,j).
\]
Adding a translational part again changes \(H\) by a constant. Thus this case also has a \(3\)-local-tension.

### 3.3. Reflections perpendicular to an edge direction

It remains to consider the linear reflection
\[
R_{\perp}(i,j)=(-i-j,j).
\]

We first put the deck group into a useful normal form:
\[
a(i,j)=(i+m,j),\qquad
b(i,j)=(-i-j+s,j+n),
\tag{1}
\]
where \(m,n\) are positive integers and \(s\in\mathbb Z\), and
\[
\Gamma=\langle a,b\rangle.
\]

Here is a justification. Vertical displacement is a homomorphism \(\Gamma\to\mathbb Z\). An orientation-reversing element of zero vertical displacement would be a reflection with a fixed line, so cannot be a deck transformation. Thus the kernel consists of horizontal translations. It is nontrivial because the index-two translation subgroup is a full-rank lattice; choose its least positive horizontal displacement \(m\).

The image of vertical displacement is \(n\mathbb Z\) for some \(n>0\). Choose an element \(b\) with displacement \(n\). Every element of \(\Gamma\) is then a product of a power of \(b\) and a horizontal translation. If \(b\) were a translation, all elements would be translations, contrary to the case under consideration. Thus \(b\) has the form in (1).

Since the quotient graph is loopless,
\[
m\geq 2:
\]
if \(m=1\), the horizontal edge from \((i,j)\) to \((i+1,j)\) would project to a loop.

Every vertex orbit has a unique representative with
\[
0\leq i<m,\qquad 0\leq j<n.
\tag{2}
\]
We will define a function \(g\) on these representatives and extend it \(\Gamma\)-invariantly. Put
\[
H(i,j)=2j+g(i,j).
\tag{3}
\]
Invariance of \(g\) gives
\[
H(av)=H(v),\qquad H(bv)=H(v)+2n.
\]
Thus the equivariance requirement is automatic. Only the edge bounds remain.

#### Case 1: \(m\) is even

For the representatives in (2), set
\[
g(i,j)=i\bmod 2\in\{0,1\}.
\]
This is proper on every horizontal cycle. Its invariant extension remains proper on all horizontal edges, since deck transformations preserve horizontal edges.

Across an edge going from row \(j\) to row \(j+1\), the height difference is
\[
2+g(\text{upper endpoint})-g(\text{lower endpoint})
   \in\{1,2,3\}.
\]
Horizontal differences have absolute value \(1\).

Hence \(H\) gives a \(4\)-local-tension in this case.

#### Case 2: \(m\) is odd

Now \(m\geq3\). Choose \(x\in\mathbb Z_m\) satisfying
\[
2x\equiv s+1\pmod m.
\tag{4}
\]
This is possible because \(m\) is odd.

Define \(p_x:\mathbb Z_m\to\{0,1,2\}\) by
\[
p_x(x)=2,
\]
and, for \(1\leq r\leq m-1\),
\[
p_x(x+r)=
\begin{cases}
0,&r\text{ odd},\\
1,&r\text{ even}.
\end{cases}
\]
This is a proper coloring of the horizontal \(m\)-cycle. In particular,
\[
p_x(x-1)=1,\qquad p_x(x+1)=0.
\tag{5}
\]

For \(0\leq j<n\), set
\[
g(i,j)=p_x(i),
\]
and extend \(\Gamma\)-invariantly. Horizontal edges have nonzero height differences of absolute value at most \(2\).

The two upper neighbors of \((i,j)\) are
\[
(i,j+1),\qquad (i-1,j+1).
\]
For either corresponding edge, the upward height difference lies in
\[
2+\{0,1,2\}-\{0,1,2\}=\{0,1,2,3,4\}.
\]
It can be zero only when the lower endpoint has \(g\)-value \(2\) and the upper endpoint has \(g\)-value \(0\).

It therefore suffices to check the upper neighbors of the unique \(2\)-colored vertex in each representative row.

For \(0\leq j<n-1\), that vertex is \((x,j)\), and its upper neighbors have \(g\)-values
\[
p_x(x)=2,\qquad p_x(x-1)=1.
\]

At the seam, invariance under \(b\) gives
\[
g(i,n)=g(s-i,0)=p_x(s-i).
\]
Using (4), the upper neighbors of \((x,n-1)\) have values
\[
g(x,n)=p_x(s-x)=p_x(x-1)=1
\]
and
\[
g(x-1,n)=p_x(s-x+1)=p_x(x)=2.
\]
Thus zero never occurs.

Every upward edge difference is consequently between \(1\) and \(4\), and every horizontal difference is nonzero with absolute value at most \(2\). Equation (3) and the height lemma give a \(5\)-local-tension.

This covers every possible deck group and completes the proof of Theorem A. ∎

## 4. Two checks on the flat-triangulation result

### Arbitrarily large edge-width occurs in the nonorientable case

The perpendicular-reflection family is not confined to small edge-width.

Every deck transformation has a unique expression \(a^p b^q\). If \(q\ne0\), it changes the row coordinate by \(qn\); any lattice path joining a vertex to its image therefore has length at least \(n\). If \(q=0\) and the transformation is nonidentity, it changes the horizontal coordinate by a nonzero multiple of \(m\), requiring at least \(m\) edges.

It follows that these quotients satisfy
\[
\operatorname{ew}(G)\geq \min\{m,n\}.
\]
Taking \(m,n\) arbitrarily large gives nonorientable examples of arbitrarily large edge-width covered by the construction.

### Why a three-coloring of the universal cover is insufficient

In fact, **no perpendicular-reflection quotient above has a \(3\)-local-tension**.

Suppose one did, and let \(H\) be its equivariant height. Reducing \(H\) modulo \(3\) gives a proper \(3\)-coloring of \(T\). Every such coloring is, up to permutation of colors,
\[
c(i,j)=i-j\pmod3.
\]
Indeed, the coloring of one triangle determines the third color across every adjacent triangle, and triangle adjacency is connected.

But
\[
c(b(i,j))=-c(i,j)+s-n\pmod3.
\]
This acts on the three colors as a transposition. Equivariance of \(H\), on the other hand, says that \(b\) acts on its reduced colors by
\[
z\longmapsto z+\tau(b),
\]
which is either the identity or a \(3\)-cycle. Conjugating by a color permutation cannot reconcile these cycle types.

Thus the \(4\)-local-tension bound proved when \(m\) is even is optimal. The argument above does not determine which odd-\(m\) quotients also admit a \(4\)-local-tension.

## 5. Proof of Theorem B

First observe that a \(K_6\) subgraph in any surface embedding must contain a noncontractible triangle.

Suppose all its triangles were contractible. Choose a vertex \(v_0\), a lift \(\widetilde v_0\) to the universal covering surface, and lift each edge \(v_0v_i\) to choose vertices \(\widetilde v_i\). Contractibility of every triangle \(v_0v_iv_j\) forces the lifted edge \(v_iv_j\) to join these chosen lifts.

We would thereby obtain an embedded \(K_6\) in the universal covering surface. That surface is a sphere or is homeomorphic to the plane, where \(K_6\) cannot embed. This is a contradiction.

Consequently, edge-width at least \(4\) excludes \(K_6\). Apply Brooks's theorem to the underlying simple graph. A graph of maximum degree at most \(5\), with no \(K_6\) component, is \(5\)-colorable; the odd-cycle exception is harmless.

Choose a proper coloring
\[
f:V(G)\to\{0,1,2,3,4\}
\]
and define
\[
\phi(uv)=f(v)-f(u).
\]
Then
\[
1\leq |\phi(uv)|\leq4,
\]
and the height of every closed walk telescopes to zero. This is an ordinary \(5\)-tension, proving Theorem B. ∎

For sharpness, on the projective plane every integer local tension is an ordinary tension: in the height lemma,
\[
\tau:\pi_1(\mathbb{RP}^2)\cong\mathbb Z_2\longrightarrow\mathbb Z
\]
must be zero, so the height descends to the original vertices. The projective-plane embedding of \(K_6\) therefore has no \(5\)-local-tension. It has maximum degree \(5\) and edge-width \(3\).

## 6. Remaining gap

Neither theorem controls unrestricted embeddings.

- Theorem A uses a globally flat triangular metric. Euler characteristic zero is essential to its coordinate construction.
- Theorem B uses a degree restriction that large edge-width does not impose.
- Restricting the tension from Theorem A to embedded subgraphs gives further examples, but does not reach arbitrary surface graphs.

Thus no universal constant \(c\), no proof of the proposed \(c=4\), and no counterexample of unbounded edge-width is obtained. The claims here are complete special-case proofs, not a claimed resolution or a claim that these special cases are new.
