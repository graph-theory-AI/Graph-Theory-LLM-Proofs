```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove 3-choosability for reflection-paired great-circle arrangements, including examples outside the cyclic-normal class, but do not resolve arbitrary arrangements.",
  "would_publish": false,
  "caveats": "The argument requires additional reflection symmetry; novelty of this special case is unchecked."
}
```

# A partial result: reflection-paired arrangements are 3-choosable

Let \(G(S)\) denote the arrangement graph of \(S\), under the stated no-triple-intersection assumption.

Call \(S\) **reflection-paired** if there is an orthogonal reflection \(\rho\) of the sphere such that
\[
\rho(S)=S
\qquad\text{and}\qquad
\rho(C)\ne C\quad\text{for every }C\in S.
\]
Thus the circles occur in pairs exchanged by \(\rho\). This is an additional symmetry, not the antipodal symmetry possessed by every great-circle arrangement.

## Theorem
Every reflection-paired arrangement of great circles in general position has a \(3\)-choosable arrangement graph.

A useful family covered by the theorem is obtained as follows. Take any centrally symmetric set
\[
P=\{\pm p_1,\ldots,\pm p_m\}\subset\mathbb R^2
\]
of distinct points, with no three collinear. For each \(p=(a,b)\in P\), take the great circle with normal
\[
(a,b,1).
\]
The resulting arrangement graph is \(3\)-choosable. The points of \(P\) need not be in convex position.

The proof uses the hemisphere-sweep idea from the supplied lead, reverified below, together with a sum-of-squares graph-polynomial argument. It does not assume the lead’s colouring constructions or fractional bounds.

The cases with at most two circles are immediate. Henceforth, in the reflection-paired case, there are \(n\ge4\) circles and \(n\) is even.

---

## 1. A graph-polynomial doubling lemma

For a loopless graph \(K\), choose an order for the endpoints of every edge and define
\[
P_K(\mathbf x)=\prod_{uv\in E(K)}(x_u-x_v).
\]
Parallel edges, if present, are included with multiplicity.

We use the following coefficient criterion:

> If \(K\) is \(4\)-regular and
> \[
> \left[\prod_{v\in V(K)}x_v^2\right]P_K\ne0,
> \]
> then \(K\) is \(3\)-choosable.

For completeness, assign distinct real numbers to the colour labels. For lists \(L(v)\) of size three, multivariate Lagrange interpolation gives, for every polynomial of total degree at most \(2|V(K)|\),
\[
\left[\prod_vx_v^2\right]P_K
=
\sum_{\mathbf a\in\prod_vL(v)}
\frac{P_K(\mathbf a)}
{\displaystyle\prod_v\prod_{b\in L(v)\setminus\{a_v\}}(a_v-b)}.
\]
A nonzero coefficient therefore implies an assignment with \(P_K(\mathbf a)\ne0\), which is a proper list-colouring.

### Lemma 1: doubling criterion

Let \(H\) have a vertex partition
\[
V(H)=I\mathbin{\dot\cup}B
\]
such that
\[
\deg_H(v)=4\quad(v\in I),
\qquad
\deg_H(b)=2\quad(b\in B).
\]
Form \(\operatorname{Dbl}(H)\) from two copies of \(H\) by identifying corresponding vertices of \(B\), without identifying any edges.

Suppose \(H\) has an acyclic orientation in which every vertex of \(I\) has outdegree two. Then \(\operatorname{Dbl}(H)\) is \(3\)-choosable.

### Proof

Use variables \(\mathbf x\) on \(I\) and \(\mathbf t\) on \(B\), and put
\[
F(\mathbf t)
=
\left[\prod_{v\in I}x_v^2\right]P_H(\mathbf x,\mathbf t)
=
\sum_{\alpha\in\{0,1,2\}^{B}}a_\alpha\mathbf t^\alpha.
\]

Write \(e=|E(H)|\). Replacing every variable by its reciprocal gives
\[
P_H(\mathbf x,\mathbf t)
=
(-1)^e
\left(\prod_{v\in I}x_v^4\right)
\left(\prod_{b\in B}t_b^2\right)
P_H(\mathbf x^{-1},\mathbf t^{-1}).
\]
Extracting the coefficient of \(\prod_{v\in I}x_v^2\), we obtain
\[
F(\mathbf t)
=
(-1)^e
\left(\prod_{b\in B}t_b^2\right)F(\mathbf t^{-1}),
\]
and hence
\[
a_{\mathbf2-\alpha}=(-1)^e a_\alpha. \tag{1}
\]

Choose corresponding edge-factor orders in the two copies of \(H\). With \(\mathbf y\) denoting the second copy’s interior variables,
\[
P_{\operatorname{Dbl}(H)}
=
P_H(\mathbf x,\mathbf t)P_H(\mathbf y,\mathbf t).
\]
Consequently, its central coefficient is
\[
\begin{aligned}
&\left[
\left(\prod_{v\in I}x_v^2y_v^2\right)
\left(\prod_{b\in B}t_b^2\right)
\right]P_{\operatorname{Dbl}(H)}
\\
&\qquad=
\left[\prod_{b\in B}t_b^2\right]F(\mathbf t)^2
=
\sum_\alpha a_\alpha a_{\mathbf2-\alpha}
=
(-1)^e\sum_\alpha a_\alpha^2. \tag{2}
\end{aligned}
\]

It remains to prove that \(F\ne0\).

Order the factors of \(P_H\) according to the assumed acyclic orientation: an edge directed from \(u\) to \(v\) contributes \(x_u-x_v\). Selecting the tail variable in every factor produces the monomial
\[
\left(\prod_{v\in I}x_v^2\right)
\prod_{b\in B}t_b^{d^+(b)}.
\]
Its coefficient is \(1\). Indeed, another selection producing the same exponent vector would correspond to reversing a nonempty set of edges while preserving every outdegree. Those edges would form a balanced directed subgraph of the original orientation, and therefore would contain a directed cycle—a contradiction.

Thus at least one \(a_\alpha\) is nonzero. Equation (2) is nonzero, and \(\operatorname{Dbl}(H)\) is \(4\)-regular. The coefficient criterion proves \(3\)-choosability. \(\square\)

The important feature is that the two halves contribute the **same** polynomial. Reciprocity then turns their pairing into a sum of squares.

---

## 2. Applying the doubling lemma to great circles

Rotate coordinates so that
\[
\rho(x,y,z)=(x,y,-z),
\]
whose fixed great circle is
\[
D=\{z=0\}\cap\mathbb S^2.
\]

Let
\[
B=V(G(S))\cap D.
\]
Every point of \(C\cap D\) is fixed by \(\rho\), and consequently belongs also to \(\rho(C)\). Since \(C\ne\rho(C)\), these are arrangement vertices. Conversely, general position ensures that a vertex on \(D\) belongs to precisely one paired pair of circles.

In particular:

* every intersection of an arrangement circle with \(D\) is a graph vertex;
* no graph edge crosses \(D\) in its interior;
* every vertex in \(B\) has exactly two incident edges in each closed hemisphere.

Let \(H\) be the graph in the closed northern hemisphere, including \(B\), and let \(I\) be its vertices in the open northern hemisphere. Then
\[
\deg_H(v)=4\quad(v\in I),
\qquad
\deg_H(b)=2\quad(b\in B).
\]
Reflection identifies the southern graph with an identical copy of \(H\), fixing \(B\) pointwise. Thus
\[
G(S)=\operatorname{Dbl}(H). \tag{3}
\]

### Constructing the required acyclic orientation

Gnomonic projection maps \(z>0\) to the affine plane \(z=1\). A paired pair of circles can be represented by normals
\[
(a,b,c),\qquad(a,b,-c).
\]
Because neither circle is individually fixed by \(\rho\), we have \(c\ne0\) and \((a,b)\ne(0,0)\). Their projected lines are
\[
aX+bY+c=0,
\qquad
aX+bY-c=0,
\]
which are distinct parallel lines.

Choose a linear functional \(\ell\) that is nonconstant on every projected line and takes distinct values at the finite intersection points. Orient every line in the direction of increasing \(\ell\), and orient the graph edges accordingly.

At each finite intersection, exactly one edge on each of the two lines points outwards. Thus
\[
d^+(v)=2\qquad(v\in I).
\]

A boundary vertex \(b\in B\) joins two parallel rays approaching the same point at infinity. Along both rays, \(\ell\) tends either to \(+\infty\) or to \(-\infty\). Hence \(b\) is respectively a sink or a source.

No directed cycle can contain a boundary vertex. A directed cycle among finite vertices is also impossible, because \(\ell\) strictly increases along every directed edge. The orientation is therefore acyclic.

Lemma 1 and (3) prove the theorem. \(\square\)

This also gives an elementary ordinary \(3\)-colouring algorithm: the acyclic orientation makes \(H\) \(2\)-degenerate, so colour \(H\) greedily and copy its colouring by reflection. The polynomial argument is needed to handle arbitrary, possibly different, lists in the two hemispheres.

---

## 3. An explicit example outside the cyclic-normal class

Here is a concrete eight-circle example covered by the theorem:
\[
\begin{array}{llll}
(1,0,1),&(-1,0,1),&(0,1,1),&(0,-1,1),\\
(1,1,1),&(-1,-1,1),&(1,2,10),&(-1,-2,10).
\end{array} \tag{4}
\]
These are normal vectors; multiplying a normal by a nonzero scalar does not change its circle.

Reflection across \(z=0\) exchanges the indicated opposite pairs of planar coordinates, up to changing the sign of the normal. Thus this is reflection-paired.

### General position

After normalizing the last coordinate to one, the planar normal points are
\[
\pm(1,0),\quad
\pm(0,1),\quad
\pm(1,1),\quad
\pm(1/10,1/5).
\]

The first six form a strictly convex hexagon. A triple containing an opposite planar pair is noncollinear because the four pair directions are distinct.

For two nonopposite old points \(p_i,p_j\) and a new point \(q\), the homogeneous determinant is
\[
\det(p_i,p_j)+\det(p_j-p_i,q).
\]
Its first term has absolute value \(1\), whereas the second has absolute value at most
\[
2(1/10)+2(1/5)=3/5.
\]
It is therefore nonzero. These observations cover all triples, proving general position.

By the theorem, the graph of (4) is \(3\)-choosable.

### Why this is not merely a cyclic-normal example

The cyclic-normal condition in the supplied lead was
\[
\det(v_i,v_j,v_k)>0\qquad(i<j<k). \tag{C}
\]
An arrangement satisfying (C) always has an \(n\)-gonal face. To see this, use indices cyclically and set
\[
q_i=\frac{v_i\times v_{i+1}}{\|v_i\times v_{i+1}\|}.
\]
Every other normal has positive scalar product with \(q_i\), by (C) and cyclic invariance of the determinant. Small perturbations of \(q_i\) enter the all-positive chamber
\[
v_j\cdot x>0\quad\text{for all }j.
\]
The points \(q_i\) exhibit consecutive pairs of its facets, so all \(n\) circles bound this chamber.

I now verify that (4) has no eight-sided face.

For the first six circles, northern gnomonic projection gives the lines
\[
X=\pm1,\qquad Y=\pm1,\qquad X+Y=\pm1. \tag{5}
\]
Their cells comprise:

* one bounded hexagon;
* six bounded triangles;
* six unbounded strip-type cells;
* six unbounded angular cells.

This enumeration can be checked without computation. Representatives of the last three types are, respectively,
\[
\begin{aligned}
&X<1,\quad Y<1,\quad X+Y>1,\\
&-1<X<1,\quad Y>1,\quad X+Y>1,\\
&X>1,\quad Y>1.
\end{aligned}
\]
The order-six transformation
\[
T(X,Y)=(-Y,X+Y)
\]
permutes the lines in (5) and generates the six cells of each type. These are all the cells: six lines with twelve finite crossings have \(1+6+12=19\) regions.

In the closed hemisphere, the representative strip cell has four boundary vertices:
\[
b_{\mathrm N},\quad(-1,2),\quad(0,1),\quad(1,1),
\]
where \(b_{\mathrm N}\) is its ideal vertex. It is therefore a quadrilateral. An angular cell has a two-edge boundary path between two ideal vertices; gluing it to its reflected cell produces a quadrilateral. Consequently, the six-circle spherical arrangement has precisely
\[
2\text{ hexagons},\qquad
12\text{ triangles},\qquad
18\text{ quadrilaterals}. \tag{6}
\]

The northern hexagon is
\[
z\ge |x|,\qquad z\ge |y|,\qquad z\ge |x+y|
\]
on the sphere; the other is its antipode. On either closed hexagon,
\[
|x+2y|\le 3|z|.
\]
The two new circles have equations
\[
x+2y=\pm10z,
\]
so they miss both closed hexagons.

Every other old face has at most four sides. Each refined face inside it is the intersection of that spherical convex polygon with two additional hemispheres, and hence has at most six sides. The old hexagons remain unchanged.

Thus every face of (4) has at most six sides. In particular, it has no eight-sided face and cannot satisfy (C) under any signing and indexing of its normals.

So the reflection-paired theorem genuinely applies beyond the cyclic-normal class considered in the lead.

---

## 4. What remains unresolved

The proof does **not** apply to a general great-circle arrangement.

Its decisive requirements are:

1. the hemispheres meet the graph only at arrangement vertices;
2. those boundary vertices have degree two in each half;
3. the two halves are identical while fixing the boundary vertices pointwise.

These properties produce the square \(F^2\) in (2). An arbitrary arrangement does not have such a reflection. The antipodal map is not a substitute: it fixes every circle setwise and exchanges, rather than fixes, boundary points.

Nor does adding reflected copies of the circles settle the original problem. Such an enlargement subdivides old edges, and \(3\)-colourability does not generally descend when subdivision vertices are suppressed.

Therefore the unrestricted conjecture, and its unrestricted \(3\)-choosability strengthening, are not proved or disproved here. What is established is a self-contained list-colouring theorem for an infinite symmetry class, including explicit noncyclic arrangements. I have not checked whether this special-case theorem is already in the literature.