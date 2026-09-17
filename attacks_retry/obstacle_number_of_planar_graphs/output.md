```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove obs(G) <= 1 + binom(b,2) - e(G[B]), where B is the set of b vertices of degree at least three, including a one-obstacle theorem when B is a clique.",
  "would_publish": false,
  "caveats": "The universal planar bound remains unresolved here; novelty is not claimed, and the supplied computer-assisted lower bound is not independently reverified."
}
```

# A bound in terms of branching vertices

According to the literature record supplied in the question, the first question has already been answered affirmatively: the icosahedral graph has obstacle number \(2\). I do not independently verify that computer-assisted result here.

The result below concerns the remaining boundedness question. It gives a bound independent of the lengths and multiplicities of subdivided paths, and an exact one-obstacle result for a class of planar graphs containing \(K_4\).

I use—and reprove the needed versions of—the face-certificate and perturbation ideas from the previous attempt. The additional ingredients are a degree-two subdivision operation and a construction using thin outward extensions of clique edges.

All graphs below are finite and simple. Obstacles are bounded simple polygonal regions. Edge segments may cross: these are representations for **ordinary obstacle number**, not planar obstacle number.

## 1. Main partial result

Write
\[
B(G)=\{v\in V(G):\deg_G(v)\ge 3\},
\qquad b=|B(G)|,
\]
and let
\[
q_B=\binom b2-|E(G[B(G)])|.
\]

### Theorem 1
Every graph \(G\) satisfies
\[
\boxed{\operatorname{obs}(G)\le 1+q_B.}
\]

The principal geometric statement behind this bound is stronger in the case \(q_B=0\).

### Theorem 2
Suppose that \(G\) has a clique \(C\) containing every vertex of degree at least three. Then \(G\) has an obstacle representation with at most one obstacle. The obstacle can lie in the unbounded face of the union of the drawn edge segments.

Consequently, if \(G[B(G)]\) is a clique and \(G\) is noncomplete, then
\[
\operatorname{obs}(G)=1.
\]

“An obstacle in the unbounded face” does not mean that the obstacle must lie outside the convex hull of all vertex points. It means that it is contained in the unbounded component of the complement of the edge-and-vertex set.

The proof occupies Sections 2–5.

---

## 2. Exterior certificates and stability

For a point drawing \(D\), put
\[
S(D)=\{\text{vertex points}\}\cup
      \bigcup_{uv\in E(G)}[u,v].
\]
Let \(F_\infty(D)\) be the unbounded component of
\(\mathbb R^2\setminus S(D)\).

Call \(D\) **exterior-certified** if every nonedge segment has an interior point in \(F_\infty(D)\).

### Lemma 3: An exterior certificate gives one obstacle
An exterior-certified drawing can be supplied with at most one simple polygonal obstacle.

#### Proof
For each nonedge \(uv\), choose a point
\[
z_{uv}\in (u,v)\cap F_\infty(D).
\]
An open connected subset of the plane is polygonally connected. Thus these finitely many witnesses can be joined by finitely many polygonal paths in \(F_\infty(D)\).

Subdivide their union at intersections and take a spanning tree containing all witness points. A sufficiently thin closed polygonal regular neighborhood of this embedded tree:

* is a simple polygonal region;
* remains in \(F_\infty(D)\);
* contains every witness in its interior.

It therefore blocks every nonedge and no edge. If there are no nonedges, no obstacle is needed. ∎

We will use the following elementary stability principle.

### Lemma 4: Protected exterior witnesses
Fix finitely many witness points in \(F_\infty(D)\). There are small closed disks around them and an \(\varepsilon>0\) such that, whenever
\[
S(D')\subseteq N_\varepsilon(S(D)),
\]
all those disks remain in \(F_\infty(D')\).

#### Proof
Join the witness disks by polygonal paths in \(F_\infty(D)\), and join the resulting connected set to a ray to infinity outside a large disk containing \(S(D)\).

The bounded portions of this protected set are compact and disjoint from \(S(D)\), so they have positive distance from it. The ray can also be chosen with positive clearance. Take \(\varepsilon\) smaller than that clearance.

The protected set then avoids \(S(D')\) and still connects every witness disk to infinity. ∎

Two consequences will be useful.

1. **Small perturbations preserve exterior certificates.**  
   If
   \[
   z=(1-t)u+tv,\qquad 0<t<1,
   \]
   is a protected witness, then sufficiently small perturbations \(u',v'\) give
   \[
   (1-t)u'+tv'
   \]
   in the same protected disk.

2. **A nearby copy inherits nonedge witnesses.**  
   If a new vertex \(x\) is sufficiently close to \(v\), every new nonedge \(xw\) corresponding to an old nonedge \(vw\) inherits its protected witness.

In particular, an exterior-certified configuration with some collinearities can be perturbed into general position, provided the perturbation is sufficiently small. Any vertex that was strictly exposed on the convex hull remains so.

---

## 3. Three operations at a convex-hull vertex

Only the vertex where an operation is performed must be a convex-hull vertex. Other vertices may lie inside the hull.

### Lemma 5
Suppose \(D\) is a general-position, exterior-certified drawing, and \(v\) is a vertex of its convex hull. Each of the following operations preserves these properties:

1. adding a pendant vertex at \(v\);
2. adding a false twin of \(v\);
3. subdividing an edge \(vb\), provided \(\deg(v)=2\).

The new vertex and every old convex-hull vertex can remain convex-hull vertices.

#### Geometric placement
Let \(v,h\) be consecutive hull vertices. One can insert a new point \(x\), arbitrarily close to \(v\), between \(v\) and \(h\) on the hull while retaining every old hull vertex. Move a little from \(v\) toward \(h\), then make a much smaller displacement to the exterior side of \(vh\).

We always choose the placement small enough for Lemma 4 and avoid the finitely many forbidden collinearities.

We also use this observation: at a hull vertex, an initial segment in a direction outside the cone spanned by its incident edge rays belongs to the unbounded face. Indeed, a sufficiently small neighborhood contains no nonincident edge, and that angular sector connects to the exterior of the convex hull.

#### Pendant addition
Insert \(x\) near \(v\) and add only \(xv\).

The new edge lies arbitrarily close to \(v\), so old witnesses survive. At the hull vertex \(x\), there is only one incident edge ray. Every new nonedge \(xw\), \(w\ne v\), has an initial portion in the unbounded face.

#### False-twin addition
Insert \(x\) next to \(v\), set
\[
N(x)=N(v),
\]
and leave \(xv\) absent.

Each new edge \(xw\) is close to the old edge \(vw\). Old witnesses therefore survive, and every new nonedge \(xw\), \(w\ne v\), inherits the witness of \(vw\).

The remaining nonedge \(xv\) is a missing hull side, so its interior meets the unbounded face.

#### Subdivision at a degree-two vertex
Let
\[
N(v)=\{a,b\},
\]
and suppose we want to subdivide \(vb\).

Choose the hull side at \(v\) from which the ray toward \(a\) precedes the ray toward \(b\) when scanning through the interior hull angle. Insert \(x\) next to \(v\) on that side, retain \(va\), delete \(vb\), and add
\[
vx,\quad xb.
\]

The new segments lie arbitrarily close to the old edge-and-vertex set. All old nonedges retain their protected witnesses.

For a new nonedge \(xw\) with \(w\notin\{v,a,b\}\), the old pair \(vw\) was a nonedge, so its witness is inherited.

There are exactly two additional pairs to check:
\[
vb,\qquad xa.
\]
For a sufficiently close insertion, the relevant angular orders are
\[
x,a,b \quad\text{at }v,
\qquad
a,b,v \quad\text{at }x.
\]
Thus the ray \(vb\) is outside the cone spanned by the new incident rays \(vx,va\), and the ray \(xa\) is outside the cone spanned by \(xb,xv\). Both nonedges have exterior witnesses near the indicated endpoints.

This covers every new nonedge. ∎

The third operation is the useful extension beyond pendant and twin additions: it allows arbitrarily long degree-two paths without increasing the obstacle count.

---

## 4. A one-obstacle construction for clique branching sets

We now prove Theorem 2.

### 4.1. The graph’s structure

Suppose \(C\) is a clique and every vertex outside \(C\) has degree at most two.

Every component of \(G-C\) is a path or a cycle. A cycle component has no neighbor in \(C\). In a nontrivial path component, only its endpoints can have neighbors in \(C\), and each endpoint has at most one such neighbor. A one-vertex component has at most two neighbors in \(C\).

Accordingly, the part containing \(C\) consists of \(C\), together with internally disjoint:

* paths between distinct vertices of \(C\);
* cycles attached at one vertex of \(C\);
* pendant paths attached at a vertex of \(C\).

All other components are paths or cycles.

We may assume \(|C|\ge3\): otherwise, add dummy vertices to enlarge \(C\) to a triangle, joining them only to one another and to \(C\). Deleting these dummy vertices after constructing a representation cannot increase obstacle number or destroy an exterior certificate.

### 4.2. A small geometric fact about outward tips

We need to place many short outward segments at the vertices of a convex polygon, with all their outer endpoints exposed on the final convex hull.

#### Lemma 6
Let \(Q\) be a strictly convex polygon. At each vertex \(c\), choose a supporting line that strictly separates all other vertices of \(Q\) from its outward side. Prescribe finitely many distinct rays from \(c\) into that outward half-plane.

One can choose a tip on each prescribed ray, arbitrarily close to its base vertex, such that every tip is a vertex of the convex hull of \(Q\) and all the tips.

#### Proof
Here are explicit local coordinates. Put \(c=(0,0)\), with all other vertices of \(Q\) in \(y>0\). A prescribed outward ray has direction \((a,-b)\), where \(b>0\).

For small positive \(\eta,\varepsilon\), intersect the rays with
\[
y=-\varepsilon+\frac{\eta}{\varepsilon}x^2.
\]
Writing a point on the ray as \((ta,-tb)\), its positive intersection parameter solves
\[
bt+\frac{\eta a^2}{\varepsilon}t^2=\varepsilon.
\]
There is a unique positive solution, of order \(\varepsilon\).

The chosen tips lie on a strictly convex parabola. Their tangent slopes are bounded in absolute value by
\[
2\eta\max\frac{|a|}{b}.
\]
Choose \(\eta\) small enough that these tangent directions remain close to the original supporting line. Then, for sufficiently small \(\varepsilon\), every vertex of \(Q\) other than \(c\), and every tip based at another vertex, lies strictly above each such tangent. The point \(c\) also lies strictly above them.

Thus each tip has a strictly supporting tangent line. ∎

Small additional perturbations along the prescribed rays preserve this exposed-tip property. We use that freedom to avoid unintended incidences with other prescribed lines.

### 4.3. An auxiliary configuration with outward segments

Draw \(C\) in strictly convex position, with convex hull \(Q\).

We first make a shortened version of the graph.

#### Paths between distinct clique vertices
For each pair \(u,v\in C\) having one or more additional internally disjoint \(u\)-\(v\) paths, initially introduce just one vertex \(p_{uv}\), adjacent to \(u\) and \(v\).

Choose one endpoint, say \(u\), and put \(p_{uv}\) on the extension of \(vu\) beyond \(u\), very close to \(u\). Then
\[
[p_{uv},v]=[p_{uv},u]\cup[u,v].
\]
Since \(uv\) is already a clique edge, geometrically this adds only the short outward segment \([u,p_{uv}]\) to the old segment union.

#### Cycles attached at one clique vertex
For every cycle based at \(c\), start with a triangle \(c,a,b\). Place \(a,b\) on a fresh outward ray from \(c\), with \(a\) between \(c\) and \(b\). Geometrically its three edges add only the segment \([c,b]\).

#### Pendant paths
For every pendant path at \(c\), start with one leaf on a fresh outward ray from \(c\).

Choose all these short outward segments inside disjoint small neighborhoods of their base vertices. At the same base vertex, use distinct rays. Apply Lemma 6 so that:

* every \(p_{uv}\);
* every outer triangle vertex \(b\); and
* every initial pendant leaf

is a strictly exposed convex-hull vertex.

The inner triangle vertices \(a\) need not be hull vertices.

The configuration has some deliberate collinearities. They are temporary and will be removed shortly.

### 4.4. Why every nonedge has an exterior witness

The auxiliary segment union is precisely:

* the drawing of the clique \(C\), inside \(Q\); and
* finitely many short outward segments, meeting one another only when they have the same base vertex.

The exterior of \(Q\), after these outward segments are removed, is connected. To see this directly, a path crossing one of the segments can be detoured along its sides and around its free end. The relevant part of that segment has positive distance from \(Q\) and from all other outward segments.

Every nonedge has an endpoint outside \(C\), because \(C\) is a clique. At that endpoint, a nonedge segment immediately leaves its outward-segment line and enters this unbounded face.

We arrange that the only vertex sets lying on an outward-segment line are the intended adjacent sets:

* \(u,v,p_{uv}\), which form a triangle;
* \(c,a,b\), which form a triangle; or
* a pendant leaf and its neighbor.

All unintended incidences can be avoided by generic choices of the rays and sufficiently small changes in the selected distances. Hence a nonedge never follows one of these outward segments for an initial interval.

The auxiliary configuration is therefore exterior-certified.

Apply Lemma 4 and perturb all vertex positions sufficiently slightly into general position. The exterior certificate survives, and all designated exposed tips remain hull vertices. This also removes every deliberate edge-through-vertex collinearity.

### 4.5. Restore all multiplicities and lengths

Now apply Lemma 5.

* **Multiple paths between \(u\) and \(v\):** add false twins of \(p_{uv}\), producing the required number of length-two paths. These vertices remain degree-two hull vertices.
* **Longer paths:** subdivide an edge incident with the corresponding degree-two hull vertex as many times as required.
* **Longer attached cycles:** start at the designated outer vertex \(b\) of its initial triangle and use degree-two subdivisions.
* **Longer pendant paths:** repeatedly add a pendant vertex at the current hull tip.

All designated hull vertices remain available while other paths are being expanded. Every operation preserves the exterior certificate.

Thus the entire part containing \(C\) is exterior-certified.

### 4.6. Separate path and cycle components

A cycle is obtained from a triangle by degree-two subdivisions, so it is exterior-certified. Paths are induced subgraphs of cycles, and vertex deletion preserves an exterior certificate.

The property is also closed under disjoint union. Place the component drawings in pairwise disjoint closed disks. Their exterior witnesses remain connected to the common exterior. A segment joining vertices in different disks contains an interval outside all the disks, and hence has an exterior witness.

We have now covered every component of \(G\). Lemma 3 supplies a single polygonal obstacle.

This proves Theorem 2. ∎

---

## 5. Completing the proof of the branching-vertex bound

Let
\[
B=B(G).
\]
Form \(G^+\) by adding all \(q_B\) missing edges among vertices of \(B\).

Then \(B\) is a clique in \(G^+\), and every vertex outside \(B\) still has degree at most two. Theorem 2 gives \(G^+\) a general-position representation with at most one obstacle.

For each added edge \(uv\), choose an interior point of \([u,v]\) lying on no other edge segment. Such a point exists: general position excludes collinear overlap, and there are only finitely many crossings.

Place a sufficiently small triangular obstacle around that point. It can be chosen to avoid:

* every edge of \(G\);
* every vertex;
* the original obstacle; and
* all the other new triangular obstacles.

This blocks the newly required nonedge \(uv\). The original obstacle still blocks all nonedges of \(G^+\).

Using one new obstacle for each of the \(q_B\) deleted clique-completion edges gives
\[
\operatorname{obs}(G)\le 1+q_B,
\]
as claimed in Theorem 1. ∎

---

## 6. Consequences for planar graphs

### 6.1. All subdivisions of a fixed graph have a uniform bound

Let \(H\) be fixed, and let \(b(H)\) be its number of vertices of degree at least three. Subdivision does not change the degrees of old vertices, and every new vertex has degree two.

Thus every subdivision \(H'\) of \(H\) satisfies
\[
\boxed{\operatorname{obs}(H')\le 1+\binom{b(H)}2.}
\]

This applies in particular to planar \(H\), regardless of the subdivision lengths or their parities. It does not require the subdivided graph to be bipartite.

### 6.2. A nonouterplanar, nonbipartite one-obstacle class

Start with \(K_4\). For each of its six edges, retain that edge and add any number of additional internally vertex-disjoint paths between its endpoints, of arbitrary lengths at least two.

These graphs are planar: in a plane drawing of \(K_4\), the additional paths can be routed in narrow neighborhoods of the corresponding edges. Their only vertices of degree at least three are the four original clique vertices. Consequently,
\[
\operatorname{obs}(G)=1
\]
whenever any additional vertex is present.

These graphs:

* contain \(K_4\), so are not outerplanar;
* contain triangles, so are not bipartite;
* allow arbitrarily many added paths and arbitrarily long degree-two chains.

Attached cycles and pendant paths at the clique vertices may also be included.

---

## 7. What is—and is not—settled

The proved statements are:

1. graphs whose degree-at-least-three vertices form a clique have obstacle number at most one;
2. arbitrary graphs satisfy
   \[
   \operatorname{obs}(G)
   \le
   1+\binom{|B(G)|}{2}-|E(G[B(G)])|;
   \]
3. subdivisions of a fixed graph have uniformly bounded obstacle number, independently of subdivision lengths.

These bounds do **not** establish a universal constant for planar graphs. A planar graph can have arbitrarily many branching vertices; in particular, triangulations may have \(B(G)=V(G)\). In that regime, the displayed parameter bound does not improve the linear bound recorded in the supplied review.

Thus the first question has the affirmative answer reported in the supplied literature, while neither a universal constant nor an unbounded planar family is established here.