```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The CAT(0) case is known in every dimension, while cubical inflation and an explicit locally CAT(0) pair show that substantially weaker unrestricted hypotheses cannot suffice.",
  "would_publish": false,
  "caveats": "No necessary-and-sufficient characterization is obtained; the all-dimensional CAT(0) theorem is used as reported, and the examples use regular cube complexes with topological boundary vertices."
}
```

# Mathematical writeup

## 1. Formulation and status

Let \(X\) be a finite, connected, regular, pure \(k\)-dimensional cube complex embedded topologically in \(\mathbb R^k\). Write

\[
G_X=X^{(1)},\qquad B(X)=V(X)\cap \partial |X|,
\]

and let the boundary-distance datum be the matrix

\[
D_X=(d_{G_X}(u,v))_{u,v\in B(X)},
\]

considered up to simultaneous permutation of rows and columns.

Reconstruction statements of this kind must be interpreted relative to a promised class \(\mathcal C\): the map \(X\mapsto D_X\) is required to be injective, up to cubical isomorphism, on \(\mathcal C\). Without such a promise, the problem has a universal local obstruction described below.

The supplied literature record reports the following theorem.

**Known theorem (Chalopin–Chepoi, arXiv:2310.04223).**  
The boundary-distance map is injective on the class of finite CAT(0) cube complexes. No bound on the dimension and no embedding in \(\mathbb R^k\) is required.

Thus the intended missing \(k\ge 4\) CAT(0) case from the source paper is already resolved. The literal broader question—finding useful conditions beyond CAT(0), or a natural characterization—is still open-ended. I do not reproduce the Chalopin–Chepoi corner-peeling proof here; the self-contained contributions below concern obstructions and elementary additional classes.

---

## 2. Unrestricted reconstruction is impossible for every \(k\ge 2\)

The following operation gives a boundary-isometric nontrivial refinement of every top-dimensional cube.

### Proposition 2.1: collar–core inflation

Let \(k\ge 2\), and let \(X\) be a finite regular \(k\)-dimensional cube complex embedded in \(\mathbb R^k\). Then there is a nonisomorphic cube complex \(X^+\), with the same underlying topological space and the same boundary cubulation, such that

\[
d_{G_X}(u,v)=d_{G_{X^+}}(u,v)
\]

for every pair of old vertices \(u,v\). In particular, \(D_X=D_{X^+}\).

#### Construction

Let \(C\) be a \(k\)-cell of \(X\), combinatorially a cube \(Q^k\). Replace \(C\) by

\[
R_k=\bigl(\partial Q^k\times [0,1]\bigr)
\mathbin{\cup}_{\partial Q^k\times\{1\}}
Q^k_{\mathrm{in}},
\]

where \(Q^k_{\mathrm{in}}\) is a new \(k\)-cube attached along its entire boundary to the inner end of the collar.

The outer boundary \(\partial Q^k\times\{0\}\) is identified with \(\partial C\). The complex \(R_k\) is a \(k\)-ball: it consists of \(2k\) collar \(k\)-cubes, one for each facet of \(Q^k\), and one central cube. It is homeomorphic to \(Q^k\) relative to the outer boundary. Consequently,

\[
X^+=(X\setminus \mathring C)\cup_{\partial C}R_k
\]

embeds in the same copy of \(|X|\subseteq\mathbb R^k\).

#### Boundary

All new vertices are vertices of the inner cube and can be placed in the interior of \(C\). Their links in \(R_k\) are topological \((k-1)\)-spheres, so they are interior vertices. Every old boundary face and vertex retains exactly the same boundary status. Thus

\[
B(X^+)=B(X)
\]

as labeled sets, and in fact the entire boundary cubical subcomplex is unchanged.

#### Distances

Label the outer and inner cube vertices by \(a\in\{0,1\}^k\), writing \(a\) and \(\widehat a\), respectively. The new local graph consists of

- the outer hypercube graph on the \(a\)'s;
- the inner hypercube graph on the \(\widehat a\)'s;
- radial edges \(a\widehat a\).

For \(k\ge2\), every edge of the original cube lies in \(\partial C\), so the old graph \(G_X\) is a subgraph of \(G_{X^+}\). Therefore

\[
d_{G_{X^+}}(u,v)\le d_{G_X}(u,v)
\]

for old vertices \(u,v\).

Conversely, define a projection on vertices by

\[
p(\widehat a)=a,\qquad p(x)=x
\]

for every old vertex \(x\). An inner cube edge projects to the corresponding outer cube edge, while a radial edge projects to a vertex. Hence every \(G_{X^+}\)-path between old vertices projects to a \(G_X\)-walk of no greater length. Thus

\[
d_{G_X}(u,v)\le d_{G_{X^+}}(u,v).
\]

The two distances are equal.

Finally, \(X^+\) has \(2^k\) more vertices than \(X\), so the two complexes are not combinatorially isomorphic. ∎

### Why CAT(0) excludes this operation

At a new inner vertex, let \(e_1,\ldots,e_k\) denote the inner coordinate edge germs and let \(r\) denote the radial edge germ. The central cube gives a simplex on \(\{e_1,\ldots,e_k\}\). For each \(i\), one incident collar cube gives a simplex on

\[
\{r,e_1,\ldots,\widehat{e_i},\ldots,e_k\}.
\]

Consequently, the link is exactly the boundary of a \(k\)-simplex:

\[
\operatorname{Lk}(v,R_k)\cong \partial\Delta^k.
\]

Its \(k+1\) vertices form a clique, but the corresponding \(k\)-simplex is absent. Thus the link is not flag. This explains why the construction does not contradict CAT(0) boundary rigidity.

### Consequences

1. For \(k\ge2\), no complex is reconstructible among all finite embedded \(k\)-dimensional cube complexes without a promise on the comparison class.
2. Contractibility, simple connectivity, being a \(k\)-ball, being a cubical manifold, purity, and embeddability in \(\mathbb R^k\) are individually insufficient: the operation preserves all these topological properties.
3. More generally, any proposed class closed under collar–core inflation cannot be boundary rigid.
4. The operation even preserves the complete boundary cubulation, not just the boundary vertex set.

For comparison, the connected \(k=1\) case is elementary and rigid: a finite pure one-dimensional complex embedded in \(\mathbb R\) is a path, and the distance between its two boundary vertices determines its number of edges.

---

## 3. Local nonpositive curvature alone is insufficient

The next pair is fully explicit and shows that flag links without simple connectivity do not suffice.

### Proposition 3.1

There are two nonisomorphic finite, pure, locally CAT(0) square complexes embedded in \(\mathbb R^2\) with identical boundary-distance matrices.

#### Construction

Start with the \(7\times7\) array of unit squares

\[
Q_{ij}=[i,i+1]\times[j,j+1],\qquad 0\le i,j\le6.
\]

Let

\[
\mathcal D=\{Q_{2,2},Q_{4,2},Q_{2,4},Q_{4,4}\},
\qquad C=Q_{3,3}.
\]

Define:

- \(K\): the square complex generated by all \(Q_{ij}\notin\mathcal D\);
- \(L\): the square complex generated by all \(Q_{ij}\notin\mathcal D\cup\{C\}\).

No two deleted squares share an edge, and all deleted squares are strictly interior. Therefore every grid edge still belongs to at least one retained square. Hence

\[
G_K=G_L=P_8\square P_8.
\]

In particular, both graphs have all \(64\) grid vertices and all \(112\) grid edges.

#### Boundary vertices

For such a planar union of squares, an interior grid vertex is a boundary vertex exactly when it is incident with a deleted square.

The four corners of \(C\) are

\[
(3,3),\ (4,3),\ (3,4),\ (4,4).
\]

These are already corners, respectively, of

\[
Q_{2,2},\ Q_{4,2},\ Q_{2,4},\ Q_{4,4}.
\]

Thus deleting \(C\) creates no new boundary vertices. Consequently,

\[
B(K)=B(L).
\]

More explicitly, this common set consists of the \(28\) outer grid vertices and the \(16\) pairwise distinct corners of the four squares in \(\mathcal D\), for a total of \(44\) vertices.

Since the full one-skeleton is the same, the common boundary metric is simply

\[
d\bigl((i,j),(i',j')\bigr)=|i-i'|+|j-j'|.
\]

Thus the two \(44\times44\) boundary-distance matrices are literally identical under the identity labeling.

#### Nonisomorphism

The complexes have different numbers of squares:

\[
f_2(K)=49-4=45,\qquad f_2(L)=49-5=44.
\]

Hence they are not combinatorially isomorphic.

#### Local nonpositive curvature

At every grid vertex, the link is obtained from the four-cycle of coordinate directions by deleting some link edges corresponding to deleted squares. It is therefore a subgraph of \(C_4\), hence has no triangles. A one-dimensional simplicial complex is flag exactly when it has no unfilled triangle. Thus all vertex links of \(K\) and \(L\) are flag, and both square complexes are locally CAT(0).

They are not globally CAT(0). Indeed,

\[
\chi(K)=64-112+45=-3,\qquad
\chi(L)=64-112+44=-4,
\]

whereas a finite CAT(0) cube complex is contractible and has Euler characteristic \(1\). ∎

This pair also shows why simple connectivity in the passage from locally CAT(0) to CAT(0) is substantive rather than cosmetic. The complex \(L\) is not a surface at the four vertices where the central deleted square touches another deleted square only at a corner; thus the example does not settle the more restrictive class of locally CAT(0) cubical manifolds with boundary.

### Higher-dimensional extension

For \(k\ge3\), set \(m=k-2\) and define

\[
K_k=K\times Q^m,\qquad L_k=L\times Q^m.
\]

Then:

- both are finite pure \(k\)-dimensional cube complexes embedded in \(\mathbb R^k\);
- their links are joins of flag complexes, hence are flag;
- their one-skeletons are identical;
- every product vertex lies on the boundary because every vertex of \(Q^m\) lies on \(\partial Q^m\);
- they have different numbers of top-dimensional cubes.

Therefore local CAT(0) is insufficient in every dimension \(k\ge2\).

---

## 4. A concrete sufficient condition beyond CAT(0)

There are strong but natural classes containing non-CAT(0) complexes for which reconstruction is immediate.

Call a finite regular square complex \(X\):

1. **boundary-full** if \(B(X)=V(X)\);
2. **square-saturated** if its 2-cells are in bijection with the induced four-cycles of \(G_X\).

### Proposition 4.1

Boundary distances determine every boundary-full, square-saturated square complex, within the class of complexes satisfying these two conditions.

#### Proof

Because every vertex is a boundary vertex, the distance matrix contains the entire vertex set. The one-skeleton is recovered by

\[
uv\in E(G_X)\quad\Longleftrightarrow\quad d_X(u,v)=1.
\]

The induced four-cycles of the reconstructed graph can then be enumerated. Square-saturation says precisely that these cycles are the boundaries of the 2-cells. Hence the entire face poset, and therefore the combinatorial type, is determined. ∎

A naive reconstruction algorithm takes \(O(n^4)\) time by enumerating vertex quadruples after recovering adjacency.

### A non-CAT(0) example in this class

Take the \(4\times4\) square grid and retain exactly the twelve squares in the outer one-cell-thick ring; equivalently,

\[
A=[0,4]^2\setminus (1,3)^2
\]

with its evident square-cell structure.

Every vertex of \(A\) lies either on the outer boundary or on the inner boundary, so \(A\) is boundary-full. Every four-cycle in its graph is the boundary of a retained unit square: a missing central unit square does not give a graph four-cycle because at least two of its edges lie entirely inside the deleted \(2\times2\) block and are absent. Hence \(A\) is square-saturated.

On the other hand, \(|A|\) is an annulus, so \(A\) is not CAT(0). Thus CAT(0) is not logically necessary for a class-level reconstruction theorem, although the replacement conditions above are much stronger and less useful than the CAT(0) hypothesis when interior vertices are present.

---

## 5. Conclusions and remaining gaps

The presently justified picture is:

- **Resolved:** Finite CAT(0) cube complexes are boundary rigid in every dimension, by Chalopin–Chepoi.
- **Impossible without a promise:** For every \(k\ge2\), collar–core inflation preserves the boundary and all old graph distances while changing the combinatorial type.
- **Topology alone is insufficient:** The inflation can be performed inside a cubical \(k\)-ball and preserves the underlying homeomorphism type.
- **Local curvature alone is insufficient:** The explicit \(7\times7\) grid pair has flag links and identical boundary metrics.
- **CAT(0) is not formally necessary:** Boundary-full graph-determined classes can contain locally CAT(0) annuli and still be reconstructible.

What remains genuinely open is a useful characterization of broader natural classes, especially classes allowing interior vertices but weakening either simple connectivity or the flag-link condition. The locally CAT(0) cubical-manifold case with nontrivial topology is not settled by the examples above. No necessary-and-sufficient characterization is proved here.