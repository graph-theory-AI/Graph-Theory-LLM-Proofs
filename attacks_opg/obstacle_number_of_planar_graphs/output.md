```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A graph grown from a seed H by isolated, pendant, and twin additions has obstacle number at most max(1, the number of nonedges of H).",
  "would_publish": false,
  "caveats": "The universal planar bound is not settled here, and novelty of the special-case bound is not asserted."
}
```

## 1. Status and scope

The supplied literature review already answers the first question affirmatively, reporting that the icosahedral graph has obstacle number \(2\). I have not independently rechecked the computer-assisted lower-bound proof.

The remaining question is whether planar graphs have uniformly bounded obstacle number. I do not settle it. The partial result below shows that **arbitrarily many pendant and twin expansions of a fixed graph cannot produce unbounded obstacle number**. In particular, it proves a one-obstacle theorem for a precisely specified class containing planar graphs that are neither outerplanar nor bipartite.

The argument is self-contained. Importantly, its straight-line edge drawings may have crossings; it concerns ordinary obstacle number, not the planar-obstacle-number variant.

## 2. A fixed-seed expansion theorem

The following operations add one vertex \(x\), leaving all old adjacencies unchanged:

1. **Isolated addition:** \(x\) has no neighbors.
2. **Pendant addition at \(v\):** \(N(x)=\{v\}\).
3. **False-twin addition at \(v\):** \(N(x)=N(v)\), where the right-hand side is taken before the addition.
4. **True-twin addition at \(v\):** \(N(x)=N(v)\cup\{v\}\).

### Theorem

Let \(H\) be a nonempty graph, and suppose that \(G\) is obtained from \(H\) by a sequence of the four operations above. Put
\[
q(H)=\binom{|V(H)|}{2}-|E(H)|.
\]
Then
\[
\boxed{\operatorname{obs}(G)\le \max\{1,q(H)\}.}
\]

The representation can be chosen with all vertices in strictly convex position.

In particular, every noncomplete graph obtainable from one vertex by these operations has obstacle number exactly \(1\). Its single obstacle can lie in the unbounded face of the straight-line edge drawing.

Here “lying in the unbounded face” does **not** mean lying entirely outside the convex hull: the obstacle may have fingers entering the convex hull through gaps between edges.

### Interpretation as a reduction

Equivalently, suppose that repeatedly deleting isolated vertices, pendant vertices, and one vertex of a true- or false-twin pair reduces \(G\) to \(H\). Then the displayed bound applies. No uniqueness of the remaining graph \(H\) is asserted.

Consequently, a family with a uniformly bounded-size remainder under these reductions has uniformly bounded obstacle number, whether or not its graphs are planar.

## 3. Obstacles can be replaced by face certificates

For a straight-line drawing \(D\), let
\[
S(D)=\{\text{vertex points}\}\;\cup\!
       \bigcup_{uv\in E(G)}[u,v].
\]
The faces are the connected components of \(\mathbb R^2\setminus S(D)\). Crossings of drawn edges are allowed.

### Lemma 1: One obstacle per selected face suffices

Suppose that faces \(F_1,\ldots,F_r\) have been selected so that every nonedge segment has an interior point in at least one selected face. Then the drawing can be supplied with at most \(r\) simple polygonal obstacles representing \(G\).

#### Proof

Assign each nonedge \(uv\) to a selected face that it meets, and choose a witness
\[
z_{uv}\in (u,v)\cap F_i.
\]

Fix a selected face \(F_i\) receiving at least one witness. Since \(F_i\) is open and connected, its finitely many witnesses can be joined by finitely many polygonal paths contained in \(F_i\). Subdivide at intersections and take a spanning tree of the resulting finite embedded graph. This gives a polygonal tree \(T_i\subset F_i\) containing all assigned witnesses.

A sufficiently thin closed polygonal regular neighborhood of \(T_i\):

- is a simple polygonal region;
- remains inside \(F_i\);
- contains every assigned witness in its interior.

For completeness, the simple-polygon assertion follows by taking the neighborhood sufficiently thin to avoid unintended intersections between nonincident tree edges. A regular neighborhood of a finite embedded tree is a disk; its boundary can be chosen polygonal.

Use this neighborhood as the obstacle for \(F_i\). It meets all assigned nonedges and no graph edge or vertex. Obstacles belonging to distinct faces are disjoint. Unused selected faces require no obstacle. ∎

Thus it is enough to maintain a bounded collection of faces meeting all nonedges.

Call such a collection an **\(r\)-face certificate with an exterior face** if it contains at most \(r\) faces, includes the unbounded face, and meets every nonedge segment.

## 4. Stability under sufficiently small additions

The perturbation issue is essential: adding edges can split faces. The following observation prevents the relevant portions of selected faces from being split apart.

### Lemma 2: Protected witnesses

Fix a drawing with an \(r\)-face certificate with an exterior face. For every nonedge, choose a witness in an assigned selected face.

There are neighborhoods of these witnesses and a number \(\varepsilon>0\) with the following property. If a new drawing has edge-and-vertex set
\[
S'\subseteq N_\varepsilon(S(D)),
\]
then:

- the protected witness neighborhoods assigned to each selected face remain in one common face of \(\mathbb R^2\setminus S'\);
- those assigned to the exterior face remain in the unbounded face.

Here \(N_\varepsilon(S(D))\) is the closed \(\varepsilon\)-neighborhood of \(S(D)\).

#### Proof

Within each selected face, join its witnesses by finitely many polygonal paths. Around each witness choose a small closed disk contained in that face, and include these disks in the protected set.

For the unbounded face, also choose a path from the protected set to a point beyond a sufficiently large disk containing \(S(D)\), followed by a ray to infinity outside that disk. If the exterior face has no assigned witness, start from an arbitrary point in it.

All bounded portions of these protected sets are compact and disjoint from \(S(D)\), so their distance from \(S(D)\) is positive. Choose \(\varepsilon\) smaller than that distance and small enough that the chosen ray remains outside \(N_\varepsilon(S(D))\).

The protected connected sets then avoid \(S'\). Hence each remains in a single face, and the exterior protected set remains connected to infinity. ∎

We will use the following immediate consequence. Suppose \(x\) is very close to an old vertex \(v\), and \(vw\) is an old nonedge with protected witness
\[
z=(1-t)v+tw,\qquad 0<t<1.
\]
Then the point
\[
z'=(1-t)x+tw
\]
on the new segment \(xw\) is arbitrarily close to \(z\). For sufficiently small \(|x-v|\), it belongs to the same protected witness neighborhood.

## 5. Preservation under the four operations

### Lemma 3

Suppose a graph has a drawing in strictly convex position with an \(r\)-face certificate with an exterior face. Each of the four permitted additions preserves this property.

#### Geometric setup

Let \(v,u\) be consecutive vertices of the old convex hull \(P\). There are points \(x\), arbitrarily close to \(v\), such that:

- all old vertices and \(x\) remain in strictly convex position;
- \(x\) is inserted between \(v\) and \(u\) in the hull order;
- the new hull is
  \[
  P'=P\cup T,\qquad T=\operatorname{conv}\{v,x,u\};
  \]
- \(P\cap T=[v,u]\).

One obtains such an \(x\) by moving a little way from \(v\) toward \(u\), then making a much smaller displacement to the exterior side of the hull edge \(vu\). Avoiding finitely many lines ensures strict convexity.

Cases with at most three total vertices are immediate: every possible nonedge is a hull side and meets the unbounded face. We therefore assume the old hull is a polygon.

### True- and false-twin additions

Insert \(x\) next to \(v\) as above.

Every new edge \(xw\), other than a possible edge \(xv\), is arbitrarily close to the old edge \(vw\). The possible edge \(xv\) is arbitrarily close to the old vertex \(v\). Thus
\[
S'\subseteq N_\varepsilon(S(D))
\]
when \(x\) is sufficiently close to \(v\).

All old nonedges retain their protected witnesses. Every new nonedge \(xw\) with \(w\ne v\) corresponds to an old nonedge \(vw\), so the consequence of Lemma 2 supplies it with a witness in the corresponding protected face.

For a true twin, this handles every new nonedge. For a false twin, the additional nonedge \(xv\) is a hull side. Its interior therefore meets the unbounded face, which is already selected.

Hence no additional selected face is necessary.

### Pendant additions

Again insert \(x\) between \(v\) and its hull neighbor \(u\), and add only the edge \(xv\).

Because \(xv\) is arbitrarily close to \(v\), Lemma 2 preserves all old nonedge witnesses.

Consider a new nonedge \(xw\), where \(w\ne v\).

- If \(w=u\), then \(xu\) is a missing hull side, so it meets the unbounded face.
- Otherwise, an initial portion of \(xw\), immediately after \(x\), lies in the interior of the ear triangle \(T\).

No old edge enters the interior of \(T\), since all old edges lie in \(P\). The only new edge is \(xv\), a boundary side of \(T\). Moreover, the side \(xu\) is absent. Thus the interior of \(T\) is connected to the exterior across \(xu\), and lies in the unbounded face of the new edge drawing.

Every new nonedge therefore meets the already selected exterior face.

### Isolated additions

Use the same placement, but add no edge at \(x\). The argument for pendant additions applies, and \(xv\) is now also a missing hull side.

This proves Lemma 3. ∎

## 6. Proof of the theorem

First suppose \(q(H)>0\). Choose a nonedge \(ab\) of \(H\), and draw the vertices of \(H\) in strictly convex position with \(a,b\) consecutive on the hull.

The segment \(ab\) is a missing hull side, so its interior meets the unbounded face.

For every other nonedge \(cd\), choose an interior point of \(cd\) outside \(S(D)\). Such a point exists: strict convexity rules out collinear overlap with an edge, and there are only finitely many edge crossings along \(cd\).

Select the faces containing these witnesses. There are at most \(q(H)\) selected faces, and one is the unbounded face. We have therefore initialized a \(q(H)\)-face certificate with an exterior face.

If \(q(H)=0\), draw the complete graph \(H\) in strictly convex position and select only its unbounded face. There are no nonedges to cover, so this is a valid one-face certificate.

Apply Lemma 3 throughout the construction of \(G\). The final drawing has a certificate using at most
\[
\max\{1,q(H)\}
\]
faces. Lemma 1 converts it into an obstacle representation with at most that many obstacles. ∎

## 7. Concrete planar consequences

### 7.1 Graphs built from one vertex

Taking \(H=K_1\) gives
\[
\operatorname{obs}(G)\le 1
\]
for every graph admitting the specified isolated/pendant/twin construction.

If \(G\) is noncomplete, equality holds: with zero obstacles, every pair of vertex points is visible.

### 7.2 Cliques attached along cutvertices

This includes every graph assembled by repeatedly attaching a clique along one existing vertex:

- add a pendant vertex \(x\) at the attachment vertex \(v\);
- add true twins of \(x\) until the desired clique has been formed.

Consequently, every noncomplete graph assembled from copies of \(K_2,K_3,K_4\) along cutvertices is a planar graph of obstacle number \(1\).

These examples may contain \(K_4\), so they need not be outerplanar, and they need not be bipartite.

### 7.3 Arbitrarily many triangles sharing an edge

Let
\[
B_t=K_2\vee \overline{K_t}.
\]
This is the planar graph consisting of \(t\) triangles sharing a common edge.

Start with \(K_3\), then repeatedly add false twins of its third vertex. The theorem gives
\[
\operatorname{obs}(B_t)=1\qquad(t\ge 2).
\]
For \(t\ge 3\), these graphs are neither bipartite nor outerplanar.

## 8. What remains unresolved

The theorem excludes one possible route to unbounded planar obstacle number: repeatedly inflating a fixed finite seed using isolated, pendant, or twin vertices.

It does **not** cover all planar graphs. For example, every cycle \(C_n\) with \(n\ge 5\) has:

- no isolated or pendant vertex;
- no true-twin pair;
- no false-twin pair.

Thus even planar graphs can have arbitrarily large irreducible remainders under these operations. The bounded-seed argument cannot, by itself, yield a universal planar constant.

Accordingly:

- the affirmative answer to the first question is supplied by the cited literature status, not newly proved here;
- the fixed-seed expansion bound above is proved;
- neither a universal constant for all planar graphs nor a family of planar graphs with unbounded obstacle number is established.