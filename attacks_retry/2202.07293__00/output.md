```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The proposed n-bound for Theorem 2 fails even for touching graphs of compact metric balls in proper geodesic spaces of Assouad–Nagata dimension n.",
  "would_publish": false,
  "caveats": "This does not settle Theorem 1 for compact convex subsets of Euclidean space, nor determine the optimal general upper bound."
}
```

# 1. Result

The general-metric-space version, under the hypotheses stated in the question, has a counterexample substantially stronger than the one in the supplied attempt.

## Theorem

For every integer \(n\ge 1\), there exist a proper geodesic metric space \((X_n,\rho)\) and a family \(\mathcal B_n\) of compact closed metric balls such that:

1. \(\dim_{\mathrm{AN}}X_n=n\);
2. the interiors of the balls are pairwise disjoint, and two distinct balls intersect in at most one point;
3. \(\mathcal B_n\) is \(f_n\)-space-filling, where
   \[
   f_n(t)=O_n((1+t)^n);
   \]
4. the intersection graph has maximum degree at most \(2n+2\) and
   \[
   \operatorname{asdim} I(\mathcal B_n)=n+1.
   \]

Thus the proposed bound \(n\) is false for Theorem 2, even with connected objects that are actual balls and with a geodesic ambient space.

The useful idea from the supplied attempt is a multiscale graph modelling a hyperbolic horoball. I retain that idea, but replace its disconnected objects and non-geodesic ambient space. All ingredients needed below, including the horoball lower bound, are justified.

The Euclidean compact-convex question in Theorem 1 remains unresolved by this construction.

# 2. A multiscale grid and its weighted realization

Fix \(n\ge1\), and put \(a_i=2^i\), for \(i\ge0\). Define a graph \(G_n\) with vertex set
\[
V_i=\left\{\left(\frac{a_i}{2}z,a_i\right):z\in\mathbb Z^n\right\},
\qquad
V(G_n)=\bigcup_{i\ge0}V_i.
\]

View these vertices as points in \(\mathbb R^n\times[1,\infty)\). Add the following axis-parallel edges.

* **Horizontal edges:** at height \(a_i\), join nearest neighbours in the grid \((a_i/2)\mathbb Z^n\).
* **Vertical edges:** for every \(z\in\mathbb Z^n\), join
  \[
  (a_i z,a_i)\quad\text{to}\quad(a_i z,2a_i).
  \]

These segments intersect only at common endpoints. Every vertex has \(2n\) horizontal neighbours, at most one upward neighbour, and at most one downward neighbour. The graph is connected and has maximum degree at most \(2n+2\).

For a vertex \(v\) at height \(a\), set
\[
r_v=\frac a4.
\]
Give every edge \(uv\) length
\[
\ell(uv)=r_u+r_v.
\]
Consequently:

* horizontal edges at height \(a\) have length \(a/2\), equal to their Euclidean length;
* vertical edges from height \(a\) to \(2a\) have length \(3a/4\), three quarters of their Euclidean length.

Let \(X_n\) be this weighted metric graph, with its path metric \(\rho\). Since the degree is bounded and every edge has length at least \(1/2\), \(X_n\) is proper and geodesic.

Define
\[
B_v=\overline B_\rho(v,r_v),
\qquad
\mathcal B_n=\{B_v:v\in V(G_n)\}.
\]

## 2.1. The balls realize exactly \(G_n\)

Every edge incident with \(v\) has length strictly greater than \(r_v\). Thus \(B_v\) is precisely a finite star consisting of the initial segment of length \(r_v\) on each incident edge. In particular, it is compact and connected.

For any vertex path
\[
v=v_0,v_1,\ldots,v_k=w,
\]
its weighted length is
\[
r_v+r_w+2\sum_{j=1}^{k-1}r_{v_j}. \tag{2.1}
\]
It follows that:

* if \(v,w\) are adjacent, their unique shortest path is their common edge, of length \(r_v+r_w\);
* if they are not adjacent, then
  \[
  \rho(v,w)>r_v+r_w.
  \]

Therefore
\[
B_v\cap B_w\ne\varnothing
\quad\Longleftrightarrow\quad
vw\in E(G_n).
\]
For an edge \(vw\), the intersection is the single point dividing that edge into lengths \(r_v,r_w\). Hence the balls have pairwise disjoint interiors and
\[
I(\mathcal B_n)=G_n. \tag{2.2}
\]

Also,
\[
\operatorname{diam}_\rho B_v=2r_v=\frac a2. \tag{2.3}
\]
The upper bound follows from the triangle inequality. For the lower bound, take the points at distance \(r_v\) from \(v\) in two opposite horizontal directions. Their horizontal displacement is \(2r_v\), and any path between them has weighted length at least that displacement.

# 3. The ambient space has Assouad–Nagata dimension \(n\)

We first compare its metric with its Euclidean embedding, then establish the required dimension bound.

## 3.1. The embedding is bi-Lipschitz

Write \(|p-q|\) for Euclidean distance in \(\mathbb R^{n+1}\). From the edge lengths,
\[
\rho(p,q)\ge \frac34 |p-q|. \tag{3.1}
\]

For the converse, the following ascent operation is useful.

Starting at a vertex of height \(a\), move each horizontal coordinate, if necessary, by one grid step \(a/2\) to make every coordinate a multiple of \(a\). Then take the vertical edge to height \(2a\). This uses at most \(n+1\) graph edges and has weighted length at most
\[
c_n a,\qquad c_n=\frac n2+\frac34.
\]
Iterating from height \(a\) to a dyadic height \(A\ge a\):

* the weighted cost is at most \(c_n(A-a)\);
* each horizontal coordinate changes by at most \((A-a)/2\);
* the number of graph edges used is at most
  \[
  (n+1)\log_2(A/a). \tag{3.2}
  \]

Now let \(u,v\) be distinct vertices at heights \(a,b\), and put \(D=|u-v|\). Because the heights are dyadic and the horizontal mesh at height \(a\) is \(a/2\),
\[
D\ge \frac12\max\{a,b\}.
\]
Choose the least dyadic \(A\ge\max\{a,b,D\}\); then \(A\le4D\).

Ascend both vertices to height \(A\), then join the resulting vertices horizontally. The ascent costs are at most \(2c_nA\), and the horizontal cost is at most
\[
\sqrt n\,D+nA.
\]
Consequently,
\[
\rho(u,v)\le K_n|u-v| \tag{3.3}
\]
for a constant \(K_n\).

This extends uniformly to edge-interior points. Here are the details to rule out a local-geometry issue. For \(p,q\in X_n\), put
\[
D=|p-q|,
\qquad
H=\max\{\text{height}(p),\text{height}(q)\}.
\]

If \(D\ge H/32\), join \(p,q\) to endpoints of their respective edges. Each added segment has length at most \(H\), so (3.3) gives \(\rho(p,q)=O_n(D)\).

If \(D<H/32\), the base heights of the two edges containing \(p,q\) are both greater than \(H/4\). Let \(c\) be the smaller of these two dyadic base heights. All endpoints of these edges lie in the lattice
\[
(c/2)\mathbb Z^{n+1}.
\]
Two disjoint axis-parallel segments with endpoints in this lattice have distance at least \(c/2>H/8\). Thus the two edges must coincide or share an endpoint. In that case, the path within those edges has length at most \(\sqrt2D\).

Together with (3.1), this proves
\[
\frac34|p-q|\le \rho(p,q)\le L_n|p-q| \tag{3.4}
\]
for all \(p,q\in X_n\).

## 3.2. A dimension lemma for porous Euclidean subsets

We use the following elementary fact, including its proof.

### Lemma

If \(Z\subseteq\mathbb R^d\) is uniformly porous, then
\[
\dim_{\mathrm{AN}}Z\le d-1.
\]

Here uniformly porous means that some \(\delta>0\) has the following property: every ball \(B(z,R)\), with \(z\in Z\) and \(R>0\), contains a Euclidean ball of radius \(\delta R\) disjoint from \(Z\).

### Proof

We construct, at every scale \(r\), a cover by \(d\) families of \(r\)-separated sets of diameter \(O(r)\).

Take a cubical grid of mesh \(\ell\). Uniform porosity implies that, in every grid cube \(P\), one can choose a point \(c_P\) such that
\[
\operatorname{dist}(c_P,Z)\ge\varepsilon\ell,
\qquad
\operatorname{dist}(c_P,\partial P)\ge\varepsilon\ell,
\]
where \(\varepsilon>0\) depends only on the porosity constant and \(d\). Indeed, either a ball about the cube centre already avoids \(Z\), or apply porosity at a nearby point of \(Z\).

Radially project \(Z\cap P\) from \(c_P\) onto \(\partial P\). These maps agree on cube boundaries and define
\[
\pi:Z\longrightarrow S,
\]
where \(S\) is the \((d-1)\)-skeleton of the grid. Their displacement is at most \(\sqrt d\,\ell\).

Moreover, \(\pi\) is Lipschitz with a constant independent of \(\ell\). Within a cube, radial projection is uniformly Lipschitz outside the ball of radius \(\varepsilon\ell/2\) about \(c_P\). If \(p,q\in Z\) satisfy \(|p-q|<\varepsilon\ell/2\), their joining segment avoids all these smaller balls, so the cellwise Lipschitz estimates combine. For more distant pairs, the bounded-displacement estimate gives the same conclusion.

Barycentrically subdivide the cubical grid. Color each subdivision vertex by the dimension of the original face whose barycentre it is. On \(S\), these are \(d\) colors, and vertices of one color never occur together in a simplex.

For each such vertex \(v\), let \(\lambda_v\) be its piecewise-affine nodal function, and put
\[
U_v=\{x\in S:\lambda_v(x)\ge 1/d\}.
\]
These sets cover \(S\). Their diameters are \(O_d(\ell)\). Distinct sets of the same color are separated by at least \(\eta_d\ell\): the nodal functions have Lipschitz constants \(O_d(1/\ell)\), and \(\lambda_v\) vanishes on \(U_w\) when \(v,w\) have the same color.

Pulling the \(U_v\) back under \(\pi\) gives \(d\) families with diameter \(O(\ell)\) and same-color separation at least a fixed positive multiple of \(\ell\). Choose \(\ell\) to be a sufficiently large constant multiple of \(r\). This is the required Assouad–Nagata cover. ∎

## 3.3. Porosity of the embedded graph

Let \(d=n+1\). The embedded \(X_n\) lies in the union of the boundaries of the cubes
\[
W_{i,z}
=
a_i\bigl(z+[0,1]^n\bigr)\times[a_i,2a_i],
\qquad
i\ge0,\ z\in\mathbb Z^n. \tag{3.5}
\]
These cubes tile \(\mathbb R^n\times[1,\infty)\). In particular, their interiors avoid \(X_n\).

We verify uniform porosity. Let \(p=(x,h)\in X_n\) and \(R>0\).

If
\[
R\le16\sqrt d\,h,
\]
take a cube \(W\) containing \(p\), of side \(a\), where \(h/2\le a\le h\). Put
\[
s=\min\left\{\frac a4,\frac{R}{4\sqrt d}\right\}.
\]
Move each coordinate of \(p\), if necessary, into the interval of points at distance at least \(s\) from the corresponding faces of \(W\). The resulting point \(c\) satisfies
\[
|c-p|\le\sqrt d\,s\le R/4,
\]
and \(B(c,s)\) lies in the interior of \(W\). Also,
\[
s\ge \frac{R}{128\sqrt d}.
\]

If \(R>16\sqrt d\,h\), choose a dyadic \(a\) with
\[
\frac{R}{16\sqrt d}\le a<\frac{R}{8\sqrt d}.
\]
Take a cube \(W\) of side \(a\) whose horizontal projection contains \(x\). Its centre \(c\) has distance at most \(R/4\) from \(p\), and \(B(c,a/4)\) lies in its interior.

Thus \(X_n\), in its Euclidean embedding, is uniformly porous. The lemma and (3.4) imply
\[
\dim_{\mathrm{AN}}X_n\le n.
\]

For the reverse inequality, the vertices at height \(1\), with the metric inherited from \(X_n\), form an isometric copy of
\[
\left(\tfrac12\mathbb Z^n,\|\cdot\|_1\right).
\]
Indeed, a horizontal grid path realizes the \(\ell_1\)-distance, while any path has horizontal cost at least that distance. Since the grid has asymptotic dimension \(n\), its Assouad–Nagata dimension is at least \(n\). Hence
\[
\boxed{\dim_{\mathrm{AN}}X_n=n.} \tag{3.6}
\]

# 4. Verification of the space-filling condition

We prove the stronger statement that the **total number** of qualifying balls is bounded; pairwise disjointness is unnecessary.

Fix \(p=(x,h)\in X_n\) and \(r,s>0\). Consider \(B_v\), with centre at height \(a\), satisfying
\[
\operatorname{diam}_\rho B_v\ge s,
\qquad
\operatorname{dist}_\rho(p,B_v)\le r.
\]
By (2.3),
\[
a\ge2s. \tag{4.1}
\]

The star \(B_v\) extends horizontally by at most \(a/4\) and vertically by at most \(a/3\). Thus
\[
B_v\subseteq
\left\{(y,t):
\|y-x_v\|_\infty\le a/3,\quad
2a/3\le t\le4a/3
\right\}.
\]
By (3.1), its Euclidean distance from \(p\) is at most \(4r/3\). Consequently,
\[
\frac34h-r\le a\le\frac32h+2r, \tag{4.2}
\]
and
\[
\|x_v-x\|_\infty\le \frac a3+\frac{4r}{3}.
\]

At a fixed height \(a\), the centres lie in \((a/2)\mathbb Z^n\). Therefore their number is at most
\[
\left(4+\frac{6r}{a}\right)^n. \tag{4.3}
\]

If \(h>4r\), (4.2) restricts \(a\) to an interval contained in \((h/2,2h)\), so there are at most three possible dyadic heights. By (4.1), the total is at most
\[
3(4+3r/s)^n.
\]

If \(h\le4r\), then \(a\le8r\). For \(a\le r\), sum (4.3) over dyadic heights:
\[
\begin{aligned}
\sum_{\substack{a=2^i\\2s\le a\le r}}
\left(4+\frac{6r}{a}\right)^n
&\le
10^n
\sum_{\substack{a=2^i\\2s\le a\le r}}
\left(\frac ra\right)^n\\
&\le
\frac{10^n}{1-2^{-n}}
\left(\frac rs\right)^n.
\end{aligned}
\]
There are at most four additional dyadic heights in \((r,8r]\), each contributing at most \(10^n\).

For example, the explicit function
\[
f_n(t)=\left\lceil A_n(1+t)^n\right\rceil,
\]
where
\[
A_n=
3\cdot4^n+
\frac{10^n}{1-2^{-n}}+
4\cdot10^n,
\]
works. Thus \(\mathcal B_n\) is \(f_n\)-space-filling.

# 5. The intersection graph has asymptotic dimension \(n+1\)

Let
\[
H=\{(x,y)\in\mathbb H^{n+1}:y\ge1\}
\]
be a closed horoball in the upper-half-space model, with metric
\[
ds^2=\frac{\|dx\|_2^2+dy^2}{y^2}.
\]

## 5.1. \(G_n\) is quasi-isometric to \(H\)

Map each vertex of \(G_n\) to its defining point \((x,a)\in H\).

A horizontal graph edge has a hyperbolic realization of length \(1/2\), and a vertical edge has length \(\log2\). Hence
\[
d_H(u,v)\le d_{G_n}(u,v). \tag{5.1}
\]

The vertex image is coarsely dense. Given \((x,y)\in H\), choose dyadic \(a\le y<2a\) and a nearest point of \((a/2)\mathbb Z^n\). A vertical move followed by a horizontal move gives distance at most
\[
C_n=\log2+\frac{\sqrt n}{4}.
\]

For the reverse coarse inequality, fix \(T>0\). If vertices \((x,a),(z,b)\) have hyperbolic distance at most \(T\), then
\[
e^{-T}\le a/b\le e^T
\]
and, by the upper-half-space distance formula,
\[
\|x-z\|_2\le 2\sqrt{ab}\sinh(T/2).
\]
Thus their heights differ by only \(O_T(1)\) dyadic levels, and their horizontal displacement is at most \(O_T(1)\) times either mesh size.

Apply the ascent operation from Section 3.1 to reach a common dyadic height comparable to
\[
\max\{a,b,\|x-z\|_\infty\}.
\]
This uses \(O_{n,T}(1)\) graph edges. At the common height, at most \(4n\) further horizontal edges are needed. Therefore
\[
d_H(u,v)\le T
\quad\Longrightarrow\quad
d_{G_n}(u,v)\le M_n(T). \tag{5.2}
\]

Sample a hyperbolic geodesic at unit intervals and choose nearby graph vertices. Equations (5.1)–(5.2), together with coarse density, prove the quasi-isometry.

## 5.2. A horoball has full hyperbolic asymptotic dimension

We use the standard facts that asymptotic dimension is quasi-isometry invariant and
\[
\operatorname{asdim}\mathbb H^d=d.
\]
The corresponding assertion for a horoball deserves justification: its one-point visual boundary does not give the desired lower bound.

### Lemma

A closed horoball in \(\mathbb H^d\) has asymptotic dimension \(d\).

### Proof

The upper bound follows from monotonicity.

For the lower bound, let \(L\) be a countable uniformly discrete net in \(\mathbb H^d\), so \(\operatorname{asdim}L=d\). Every finite subset of \(L\) has an isometric copy inside the horoball: in upper-half-space coordinates, the dilation
\[
(x,y)\longmapsto(\lambda x,\lambda y)
\]
is a hyperbolic isometry, and sufficiently large \(\lambda\) moves any prescribed finite set into \(y\ge1\).

Suppose the horoball had asymptotic dimension at most \(q<d\). Fix \(R>0\), and color the horoball with \(q+1\) colors so that its monochromatic \(R\)-components have diameter at most \(D_R\).

Take increasing finite sets exhausting \(L\), embed each into the horoball, and pull back the coloring. A diagonal subsequence gives a coloring of all of \(L\). Every finite monochromatic \(R\)-chain eventually occurs in one of the finite colorings, so its endpoints have distance at most \(D_R\). Hence all monochromatic \(R\)-components of the limiting coloring have diameter at most \(D_R\).

Doing this separately for every \(R\) gives \(\operatorname{asdim}L\le q\), a contradiction. ∎

Combining the lemma, the quasi-isometry, and (2.2),
\[
\boxed{\operatorname{asdim}I(\mathcal B_n)
=\operatorname{asdim}G_n
=n+1.} \tag{5.3}
\]

This proves the theorem.

# 6. The finite-graph-class interpretation

The construction also disproves a uniform \(n\)-dimensional bound if the source theorem is formulated for classes of finite intersection graphs.

Fix a vertex \(v_0\), and take the finite subfamilies indexed by graph balls
\[
V_j=B_{G_n}(v_0,j).
\]
Their intersection graphs are \(G_n[V_j]\), and all subfamilies satisfy the same \(f_n\)-space-filling bound in the same ambient space.

If these finite graphs admitted uniform asymptotic-dimension-\(n\) control, fix a scale \(R\) and take their uniformly controlled \((n+1)\)-colorings. Diagonal compactness gives a coloring of \(G_n\). Every fixed finite collection of shortest paths is eventually contained in \(G_n[V_j]\), so every finite monochromatic \(R\)-chain in \(G_n\) inherits the same diameter bound. This would imply
\[
\operatorname{asdim}G_n\le n,
\]
contradicting (5.3).

Thus the counterexample is not an artifact of allowing infinite intersection graphs.

# 7. What is settled and what remains open

For the general-metric-space question, the construction establishes
\[
\boxed{n+1\le \text{optimal universal bound}\le2n+1
\qquad(n\ge1).}
\]
In particular, replacing \(2n+1\) by \(n\) in Theorem 2 is impossible under the hypotheses quoted in the question.

The obstruction does **not** depend on disconnected sets or a non-geodesic ambient space. The objects here are compact metric balls, their ambient space is proper and geodesic, and even the intersection graph has bounded degree.

However, \(X_n\) is a branching metric graph with a multiscale geometry, not Euclidean \(\mathbb R^n\). Its balls are stars, not Euclidean convex bodies. Consequently, none of the argument proves or disproves
\[
\operatorname{asdim} I(\mathcal C)\le n
\]
for bounded-aspect-ratio compact convex subsets of \(\mathbb R^n\).

That Euclidean part of the original problem remains the substantive gap.