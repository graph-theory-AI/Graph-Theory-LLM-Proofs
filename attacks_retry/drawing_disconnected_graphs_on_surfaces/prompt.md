Attack the following open graph-theory problem.

Catalog id: drawing_disconnected_graphs_on_surfaces
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/drawing_disconnected_graphs_on_surfaces/
Original entry: http://www.openproblemgarden.org/op/drawing_disconnected_graphs_on_surfaces
Problem attributed to: DeVos, Matt, Mohar, Bojan, Samal, Robert (posted 2007-05-12)

=== Problem statement (OpenProblemGarden) ===
Title: Drawing disconnected graphs on surfaces
Conjecture Let $ G $ be the disjoint union of the graphs $ G_1 $ and $ G_2 $ and let $ \Sigma $ be a surface. Is it true that every optimal drawing of $ G $ on $ \Sigma $ has the property that $ G_1 $ and $ G_2 $ are disjoint?

=== Discussion / context (OpenProblemGarden) ===
We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph ). Although both crossing numbers and embeddings of graphs on general surfaces are rich and well-studied subjects, their common generalization - drawing graphs on general surfaces has received very little attention. The question highlighted here appears to be quite basic in nature, but due to the combined difficulties of crossings and general surfaces, it may be quite difficult to resolve. This conjecture is trivially true when $ \Sigma $ is the plane, and DeVos, Mohar, and Samal have proved that it also holds when $ \Sigma $ is the projective plane. It is open for all other surfaces to the best of my (M. DeVos) knowledge.

=== Catalog page (statement + literature review) ===
Drawing disconnected graphs on surfaces — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Since the problem was posted, the conjecture has been proved for the Klein bottle by Beaudou, Gerbaud, Grappe, and Palesi (2010): every optimal drawing of a disconnected graph on the Klein bottle draws the connected components disjointly. The conjecture thus holds for the plane (trivially), the projective plane (DeVos–Mohar–Šámal, pre-posting), and the Klein bottle, but remains open for the torus and all other surfaces. A 2015 extended abstract by Cabello, Mohar, and Šámal reports a partial result for the torus by reducing the problem to a question in the geometry of numbers, but the torus case is not fully resolved.

 Cited literature (1)

 
 
 
partial Drawing disconnected graphs on the Klein bottle
 (2010)
 

 
 Laurent Beaudou, Antoine Gerbaud, Roland Grappe, Frederic Palesi · Graphs and Combinatorics · arXiv:0810.0508 · doi:10.1007/s00373-010-0928-7

Proves the DeVos–Mohar–Šámal conjecture for the Klein bottle: in any crossing-optimal drawing of a disconnected graph on the Klein bottle, the connected components must be drawn in disjoint regions.
 

 

 Reviewer notes. A 2015 extended abstract 'Drawing a disconnected graph on the torus' by Cabello, Mohar, and Šámal (Electronic Notes in Discrete Mathematics 49, pp. 779–786, arXiv not found) reports reduction to a geometry-of-numbers question and a partial result for the torus, but could not be verified via WebFetch (ScienceDirect and PDF returned 403/binary). This paper was therefore not included in since_posted despite strong search-result evidence of its existence. The DOI 10.1007/s00373-010-0928-7 for the Klein bottle paper was confirmed by multiple search results but the Springer page required authentication; the arXiv preprint at 0810.0508 was directly verified. No papers resolving the conjecture for the torus or any orientable surface of genus ≥ 1 were found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ G $ be the disjoint union of the graphs $ G_1 $ and $ G_2 $ and let $ \Sigma $ be a surface. Is it true that every optimal drawing of $ G $ on $ \Sigma $ has the property that $ G_1 $ and $ G_2 $ are disjoint?

Keywords:
crossing number · surface

Discussion

We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph ). Although both crossing numbers and embeddings of graphs on general surfaces are rich and well-studied subjects, their common generalization - drawing graphs on general surfaces has received very little attention. The question highlighted here appears to be quite basic in nature, but due to the combined difficulties of crossings and general surfaces, it may be quite difficult to resolve. This conjecture is trivially true when $ \Sigma $ is the plane, and DeVos, Mohar, and Samal have proved that it also holds when $ \Sigma $ is the projective plane. It is open for all other surfaces to the best of my (M. DeVos) knowledge.

Related conjectures

 
 related to
 The Crossing Number of the Complete Graph
 partial
 The mention is purely definitional: the source page says 'We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph)', importing the standard good-drawing conditions and nothing more. There is no logical dependence: the truth of the exact formula for cr(K_n) in the plane neither forces nor follows from the statement that optimal drawings of a disconnected graph on an arbitrary surface keep the components disjoint (the latter is about arbitrary graphs G_1, G_2 and arbitrary surfaces, the former about one specific family in the plane). They share only the theme of crossing-minimal drawings.
 

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
  "one_line": "The conjecture holds on the torus when one summand has plane crossing number at most 7, and on every closed orientable surface when one has plane crossing number at most 1.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved here; the novelty of these special cases has not been checked."
}
```

# Partial results

Write \(\operatorname{cr}_0(H)\) for the crossing number of \(H\) in the plane. I prove the following special cases.

**Theorem 1.** Let \(G=G_1\sqcup G_2\).
1. On any closed orientable surface, if
   \[
   \min\{\operatorname{cr}_0(G_1),\operatorname{cr}_0(G_2)\}\le 1,
   \]
   then every optimal drawing draws \(G_1\) and \(G_2\) disjointly.
2. On the torus, the same conclusion holds if
   \[
   \min\{\operatorname{cr}_0(G_1),\operatorname{cr}_0(G_2)\}\le 7.
   \]

The torus result follows from a quantitative redrawing bound. In particular, **two connected components in an optimal torus drawing cannot cross each other between one and seven times**.

No literature result is needed for these arguments. I have not checked whether these special cases or the quantitative bound already appear in the literature.

## 1. Preliminaries

For a drawing of \(A\sqcup B\), let
- \(c_A,c_B\) be the numbers of crossings internal to \(A,B\), respectively;
- \(m\) be the number of crossings between \(A\) and \(B\).

A basic operation is to delete one summand and put a plane drawing of it into a small disk avoiding the rest of the drawing. Consequently, optimality implies
\[
c_A+m\le \operatorname{cr}_0(A),
\qquad
c_B+m\le \operatorname{cr}_0(B).
\tag{1}
\]

More generally, if \(C\) is one connected component of a graph in an optimal drawing, and \(t_C\) counts its crossings with all other components, then
\[
c_C+t_C\le \operatorname{cr}_0(C).
\tag{2}
\]

We will **planarize only internal crossings**: replace each internal crossing of \(A\) by a degree-four vertex, obtaining an embedded graph \(H_A\), while retaining its transverse intersections with \(H_B\).

A plane drawing of \(H_A\) with \(q\) crossings gives a plane drawing of \(A\) with at most \(q+c_A\) crossings. Indeed, in a small disk around each of the \(c_A\) designated vertices, join the prescribed pairs of incident arcs using at most one crossing. Any resulting violations of the usual good-drawing conditions can be removed without increasing the crossing count.

## 2. An orientable genus-overlap bound

Let the ambient surface be the closed orientable surface \(\Sigma_g\). Take regular neighborhoods \(N_A,N_B\) of the internally planarized graphs. They need not be connected. Let \(a,b\) denote the sums of the genera of their connected components.

### Lemma 2
For any such drawing,
\[
m\ge 2(a+b-g).
\tag{3}
\]
Moreover, if \(a+b\le g\), there is a drawing of \(A\sqcup B\) on \(\Sigma_g\) with disjoint summands and at most \(c_A+c_B\) crossings.

**Proof.**

Work over \(\mathbb F_2\). The handle cycles of \(N_A\) give a nondegenerate symplectic subspace
\[
U\subseteq H_1(\Sigma_g;\mathbb F_2),
\qquad \dim U=2a.
\]
Likewise \(N_B\) gives a subspace \(V\) of dimension \(2b\). These dimensions are preserved in the ambient surface because the intersection pairing on each chosen handle subspace is nondegenerate.

The rank of the intersection pairing restricted to \(U\times V\) is
\[
\dim U-\dim(U\cap V^\perp)
\ge 2a-(2g-2b)
=2(a+b-g).
\tag{4}
\]

On the other hand, represent the chosen cycles on \(H_A,H_B\), which are deformation retracts of their regular neighborhoods. Each of their mutual intersection points contributes a matrix of rank at most one to the restricted intersection matrix. There are \(m\) such points, so that matrix has rank at most \(m\). This proves (3).

If \(a+b\le g\), place homeomorphic copies of all the connected components of \(N_A,N_B\) in mutually disjoint subsurfaces of \(\Sigma_g\). There is sufficient genus to do this; extra boundary components are simply holes within the allocated subsurfaces. Carry along the embedded graphs and restore the designated internal crossings. The resulting drawing has no mutual crossings and retains at most \(c_A+c_B\) internal crossings. \(\square\)

### Consequences

An optimal drawing on an orientable surface cannot have exactly one crossing between its two summands. Indeed, if \(m=1\), (3) implies \(a+b\le g\), and the second part of the lemma removes that crossing without adding any.

Now suppose \(\operatorname{cr}_0(A)\le1\) and an optimal drawing has \(m>0\). By (1),
\[
c_A+m\le1,
\]
so \(m=1\), which is impossible. This proves Theorem 1(1), including when the summands are disconnected.

## 3. A quantitative torus redrawing lemma

Define
\[
F(m)=
\left\lfloor
\frac{\bigl(\lfloor m/2\rfloor+1\bigr)^2}{3}
\right\rfloor .
\tag{5}
\]

**Proposition 3.** Suppose connected graphs \(A,B\) are drawn on the torus with \(c_A,c_B\) internal crossings and \(m>0\) mutual crossings. Then
\[
\operatorname{cr}_0(A)\le c_A+F(m)
\quad\text{or}\quad
\operatorname{cr}_0(B)\le c_B+F(m).
\tag{6}
\]

Thus one component can be moved into a disk, leaving the other unchanged, at an additional internal-crossing cost of at most \(F(m)\).

### Proof

Internally planarize the drawings, obtaining connected embedded graphs \(H_A,H_B\).

If either graph has a genus-zero regular neighborhood, that neighborhood can be reproduced in the plane. Restoring the internal crossings gives
\(\operatorname{cr}_0(A)\le c_A\) or \(\operatorname{cr}_0(B)\le c_B\), and we are done.

We may therefore assume both regular neighborhoods have genus one. Both embedded graphs are then cellular: their faces are open disks. To see this, a connected genus-one neighborhood with \(b\) boundary curves has Euler characteristic \(-b\). If its complement has \(s\) components and total genus \(h\), the torus Euler characteristic gives
\[
0=-b+(2s-2h-b),
\]
so \(s=h+b\). Since every complementary component has boundary, \(s\le b\). Hence \(h=0\), \(s=b\), and every complementary component is a disk.

Cut each \(H_i\), for \(i\in\{A,B\}\), at its \(m\) mutual intersection points. Formally, delete a small open edge interval around each such point, avoiding all vertices. Let \(n_i\) be the number of remaining connected pieces.

Contract each piece to a vertex and regard the \(m\) deleted intervals as edges. This produces a connected multigraph \(Q_i\), whose edges are indexed by the mutual crossings. Its cycle-space dimension is
\[
r_i=m-n_i+1.
\tag{7}
\]

We prove two bounds:
\[
r_A+r_B\le m+2,
\tag{8}
\]
and
\[
\operatorname{cr}_0(i)\le c_i+
\left\lfloor\frac{r_i^2}{3}\right\rfloor
\qquad(i=A,B).
\tag{9}
\]

### 3.1. The cycle-space bound

Identify the edge sets of \(Q_A,Q_B\) with the same set of \(m\) crossing labels. Their binary cycle spaces are subspaces
\[
L_A,L_B\subseteq\mathbb F_2^m
\]
of dimensions \(r_A,r_B\).

Every \(x\in L_A\) can be lifted to a mod-two cycle in \(H_A\): use the selected connector intervals, and complete their ends inside the connected cut pieces. Choose these completions linearly, using fixed spanning trees within the pieces. Do the same for \(L_B\).

The completions avoid the other embedded graph. Therefore, for \(x\in L_A\), \(y\in L_B\), the intersection number of their lifts is exactly
\[
x\cdot y=\sum_{j=1}^m x_jy_j.
\tag{10}
\]
This bilinear form factors through the two-dimensional space
\(H_1(\mathbb T^2;\mathbb F_2)\), so its rank is at most two.

The restricted dot product on \(L_A\times L_B\) has rank at least
\[
r_A+r_B-m.
\]
Indeed, its left kernel is \(L_A\cap L_B^\perp\), of dimension at most \(m-r_B\). Thus
\[
r_A+r_B-m\le2,
\]
proving (8).

### 3.2. Turning one cut graph into a plane drawing

Fix \(i\in\{A,B\}\).

Because \(H_{3-i}\) is cellular, each cut piece of \(H_i\) lies in a disk face of \(H_{3-i}\). All its cut ends are exposed to the outer face of that piece: the deleted half-connector continues from each cut end to the boundary of the containing face without meeting the cut graph.

Consequently, each cut piece can be enclosed in a closed disk, with its attachment points on the disk boundary. These disks can be chosen mutually disjoint and otherwise disjoint from the connector arcs. One way to see this is to thicken each piece and fill its bounded complementary regions. No other cut piece can be trapped in such a region: every cut piece has an attachment end, and that end has an unobstructed continuation to the boundary of the containing face.

Choose a spanning tree of \(Q_i\). Thicken its \(n_i-1\) connector arcs into bands joining these disks. Since the selected edges form a tree, the resulting union is a single disk \(\Delta\). The part of \(H_i\) outside \(\Delta\) now consists of
\[
m-(n_i-1)=r_i
\]
pairwise disjoint arcs, each with two endpoints on \(\partial\Delta\).

Reproduce \(\Delta\), together with the graph it contains, on the sphere. Draw the remaining arcs as chords in the complementary disk. Two such chords cross precisely when their endpoint pairs alternate around \(\partial\Delta\), and then they need cross only once.

It remains to bound the number of alternating pairs.

Close each of the \(r_i\) original outside arcs by an arc inside \(\Delta\), and let its homology class in
\[
H_1(\mathbb T^2;\mathbb F_2)\cong\mathbb F_2^2
\]
be \(u_j\). Because the outside arcs are disjoint, two endpoint pairs alternate exactly when the corresponding homology classes have intersection number one.

There are three nonzero classes in \(\mathbb F_2^2\). Two classes have intersection number one precisely when they are distinct and nonzero. If their multiplicities among the \(u_j\) are \(a,b,c\), the chord drawing therefore introduces
\[
ab+bc+ca
\le \frac{(a+b+c)^2}{3}
\le \frac{r_i^2}{3}
\tag{11}
\]
crossings. Zero classes contribute none.

Restoring the \(c_i\) designated internal crossings proves (9).

Finally, (8) implies
\[
\min\{r_A,r_B\}\le
\left\lfloor\frac{m+2}{2}\right\rfloor
=\lfloor m/2\rfloor+1.
\]
Applying (9) to that index gives (6). \(\square\)

## 4. Optimality consequences on the torus

The first values of the bound are
\[
\begin{array}{c|rrrrrrrrr}
m&1&2&3&4&5&6&7&8&9\\ \hline
F(m)&0&1&1&3&3&5&5&8&8.
\end{array}
\tag{12}
\]

In particular,
\[
F(m)<m\qquad(1\le m\le7),
\]
and also when \(m=9\).

For a drawing of \(A\sqcup B\), Proposition 3 therefore gives a disjoint drawing with at most
\[
c_A+c_B+F(m)
\]
crossings. This is strictly better whenever \(F(m)<m\).

The same argument applies when further components are present. Move the component supplied by Proposition 3 into a disk avoiding **all** remaining components. This removes at least its \(m\) crossings with the other selected component, while adding fewer than \(m\) internal crossings.

We have proved:

**Corollary 4.** In an optimal torus drawing, the number of crossings between any two connected components is neither \(1,2,\ldots,7\) nor \(9\).

Now let \(C\) be a connected component with \(\operatorname{cr}_0(C)\le7\). If it meets another component in an optimal drawing, then (2) gives
\[
1\le t_C\le7.
\]
Some other connected component \(D\) therefore satisfies
\[
1\le m_D(C,D)\le7,
\]
contrary to Corollary 4. Thus every such \(C\) is disjoint from every other component.

If \(\operatorname{cr}_0(G_1)\le7\), each connected component of \(G_1\) also has plane crossing number at most seven. Hence all of \(G_1\) is disjoint from \(G_2\). This proves Theorem 1(2).

## 5. Where this attack stops

The first crossing count for which the torus estimate loses strictness is
\[
m=8,\qquad F(8)=8.
\]

There is a precise equality obstruction within the proof. If an optimal drawing had two connected components crossing eight times, the construction above would necessarily have
\[
r_A=r_B=5,\qquad n_A=n_B=4.
\]
Furthermore, for every spanning-tree choice used in the disk-and-band construction, the five remaining arc classes would have to be nonzero and distributed as
\[
(2,2,1)
\]
among the three nonzero torus homology classes. Any other distribution gives at most seven new crossings and hence a strict improvement.

I have not excluded these configurations. Nor does the quadratic estimate \(F(m)\) yield a strict improvement for all larger \(m\). Thus this argument does **not** resolve the unrestricted torus conjecture, and its higher-genus conclusion is only the plane-crossing-number-at-most-one special case above.
