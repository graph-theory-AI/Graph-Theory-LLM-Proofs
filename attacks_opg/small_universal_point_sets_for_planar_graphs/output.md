```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I construct explicit O(k^2 n)-point universal sets for planar n-vertex graphs with vertex-cover number at most k, but do not resolve the unrestricted problem.",
  "would_publish": false,
  "caveats": "No improvement to the unrestricted bounds; novelty of this restricted-class result is not asserted."
}
```

## 1. A parameterized special case

I do not settle whether \(f(n)=O(n)\). The following gives a restricted-class bound, using the grid-drawing theorem supplied in the question.

Graphs below are finite and simple. Let \(f_k(n)\) be the minimum size of a point set universal for the \(n\)-vertex planar graphs having a vertex cover of size at most \(k\).

**Theorem.** For all integers \(k,n\ge 1\),
\[
f_k(n)\le \min\{n^2,\;54k^2n\}.
\]
The \(54k^2n\) construction is explicit and has rational coordinates of bit length \(O(\log k+\log n)\).

Thus fixed vertex-cover number admits linear-size universal point sets. More generally, the bound is subquadratic when \(k=o(\sqrt n)\).

The argument has two ingredients:

1. such a graph has a planar core on at most \(3k\) vertices, with all remaining vertices being leaves, isolated vertices, or degree-two twins attached to core edges;
2. all possible edge midpoints in a square grid occupy only quadratically many positions. Small pools near those midpoints accommodate arbitrary multiplicities of degree-two twins.

Unused points of a universal set are not graph vertices and impose no restrictions on a drawing.

## 2. Reduction to a small planar core

Let \(G\) be planar, and let \(C\) be a vertex cover of size \(c\le k\). Its complement \(I\) is independent. Put
\[
J=\{v\in I:\deg_G(v)\ge 3\},\qquad h=|J|.
\]

If \(h>0\), then \(c\ge3\). The bipartite planar graph consisting of the edges between \(C\) and \(J\) satisfies
\[
3h\le |E(C,J)|\le 2(c+h)-4.
\]
Consequently,
\[
h\le 2c-4.
\]
If \(h=0\), no estimate is needed. In either case,
\[
|C\cup J|\le 3k.
\]

Construct a simple graph \(H\) on \(C\cup J\) as follows:

- keep every edge of \(G[C\cup J]\);
- for each degree-two vertex \(w\in I\), with neighbors \(u,v\in C\), add the edge \(uv\) if it is not already present.

The graph \(H\) is planar. Indeed, delete the degree-zero and degree-one vertices in \(I\), suppress every degree-two vertex in \(I\), and then discard parallel edges. These operations preserve planarity. No loop is created because each suppressed vertex has two distinct neighbors.

The original \(G\) can therefore be recovered from \(H\) by:

1. adding leaves at core vertices;
2. for each appropriate edge \(uv\in E(H)\), adding independent vertices adjacent precisely to \(u\) and \(v\);
3. adding isolated vertices;
4. deleting the auxiliary edges of \(H\) that were not edges of \(G\).

Each multiplicity in these operations is at most \(n\). The case \(C=\varnothing\) simply gives an empty core and \(n\) isolated vertices.

## 3. A geometric augmentation lemma

Here is the point-set construction supporting those operations.

Fix integers \(q\ge3\) and \(n\ge1\). Define
\[
S=\{0,1,\ldots,q-1\}^2
\]
and the half-grid
\[
M=\left\{0,\frac12,1,\ldots,q-1\right\}^2.
\]
Every midpoint of two points of \(S\) belongs to \(M\), and
\[
|S|=q^2,\qquad |M|=(2q-1)^2.
\]

Set
\[
\delta=\frac1{100q^4},
\qquad
d=\left(1,\frac1{2q}\right).
\]

We use three types of pools.

### Leaf pools

For each \(p\in S\), include
\[
B_j(p)=p+\delta(1,t_j),
\qquad
t_j=\frac{n+1+j}{3q(n+1)},
\qquad 1\le j\le n.
\]
Thus
\[
\frac1{3q}<t_j<\frac2{3q}.
\]
The points of this pool lie on a short vertical segment not containing \(p\), so the segments from \(p\) to distinct pool points form a noncrossing fan.

### Degree-two pools

For each \(m\in M\), include
\[
D_j(m)=m+\frac{\delta j}{n+1}d,
\qquad 1\le j\le n.
\]

The direction \(d\) is not parallel to any segment joining distinct points of \(S\). Indeed, parallelism with a nonzero integer vector \((a,b)\), where \(|a|,|b|\le q-1\), would imply
\[
a=2qb,
\]
which is impossible.

### Isolated-vertex pool

Include
\[
A_j=\left(\frac{j}{n+1},-1\right),
\qquad 1\le j\le n.
\]

Let \(P(q,n)\) be the union of \(S\) and all these pools. Its size satisfies
\[
\begin{aligned}
|P(q,n)|
&\le q^2+nq^2+n(2q-1)^2+n\\
&=q^2+n(5q^2-4q+2)\\
&\le 6q^2n.
\end{aligned}
\]

**Augmentation lemma.** Suppose a planar graph \(H\) has a straight-line drawing whose vertex set is a subset of \(S\). Keeping the core vertices fixed, the set \(P(q,n)\) supports every graph obtained by adding:

- at most \(n\) leaves at each core vertex;
- at most \(n\) new degree-two vertices on each core edge \(uv\), each adjacent to \(u\) and \(v\);
- at most \(n\) isolated vertices.

### Proof: each individual bundle is valid

For leaves at \(p\), use the required number of points \(B_j(p)\).

For an edge \(uv\), put
\[
m=\frac{u+v}{2}
\]
and use the required number of points \(D_j(m)\). Distinct edges in a valid straight-line drawing cannot have the same midpoint: they would intersect there.

The line
\[
L=m+\mathbb R d
\]
strictly separates \(u\) and \(v\), because it passes through their midpoint and is not parallel to \(uv\). Hence:

- segments from \(u\) to distinct points of the pool meet only at \(u\);
- segments from \(v\) to distinct points of the pool meet only at \(v\);
- a segment from \(u\) and one from \(v\) have interiors in opposite half-planes bounded by \(L\).

Furthermore, all pool points lie strictly on one side of the supporting line of \(uv\), so none of the new edges crosses the retained edge \(uv\). Thus the entire bundle is drawn without crossings or nonincident vertex-edge incidences.

It remains to verify that different bundles do not interfere.

### Proof: separation between different bundles

Two elementary grid estimates suffice.

**Distance estimate.** Disjoint segments with endpoints in \(S\), or a point of \(S\) not on a segment with endpoints in \(S\), have distance at least
\[
\eta=\frac1{\sqrt2\,q}.
\]
For a noncollinear point and supporting line, this follows from the integer determinant formula for distance. If the nearest point is an endpoint, or the relevant objects are collinear and disjoint, the distance is at least \(1\). For two disjoint segments, a minimum-distance pair can be chosen to include an endpoint.

**Angle estimate.** Two distinct grid rays from a common grid point have angular separation at least
\[
\frac1{2q^2}.
\]
For noncollinear direction vectors this follows from their nonzero integer determinant and lengths at most \(\sqrt2(q-1)\). Opposite rays satisfy the estimate as well. Coincident rays cannot be two edges of a valid straight-line drawing.

For a core edge \(e=uv\), its entire augmented bundle lies in
\[
T_e=\operatorname{conv}
\left\{u,v,\frac{u+v}{2}+\delta d\right\}.
\]
Since \(\|d\|<2\), this triangle lies within distance \(2\delta\) of \(e\).

At either endpoint, its directions deviate from the original edge ray by at most \(8\delta\). To see this, the apex is obtained by perturbing the midpoint by a vector of length less than \(2\delta\). Its forward component from an endpoint is at least
\[
\frac{|e|}{2}-2\delta\ge\frac{|e|}{4},
\]
while its transverse component is at most \(2\delta\). Thus the angular deviation is at most
\[
\arctan\!\left(\frac{8\delta}{|e|}\right)\le 8\delta.
\]

Consequently:

- triangles belonging to nonincident core edges are disjoint because \(4\delta<\eta\);
- triangles belonging to distinct incident core edges meet only at their common endpoint because
  \[
  16\delta<\frac1{2q^2}.
  \]

Every leaf edge at \(p\) lies within distance \(2\delta\) of \(p\). Its direction has slope in
\[
\left(\frac1{3q},\frac2{3q}\right).
\]
This interval of directions has angular distance at least \(1/(6q)\) from every possible grid ray. For a ray pointing right and upward, its slope is either zero or at least \(1/(q-1)>1/q\); the remaining directions are farther away. For example,
\[
\arctan(1/q)-\arctan(2/(3q))
\ge \frac1{6q}.
\]
Since
\[
8\delta<\frac1{6q},
\]
leaf fans cannot meet incident edge bundles except at their common core vertex.

For nonincident edge bundles, the distance estimate applies. Leaf fans at different core vertices lie in disjoint radius-\(2\delta\) neighborhoods, since distinct grid points have distance at least \(1>4\delta\).

These same separations ensure that distinct active pools receive distinct vertex positions and that no edge passes through a nonincident assigned vertex. Interactions within one pool were handled above.

Finally, all core, leaf, and degree-two positions have nonnegative \(y\)-coordinate. Their edges therefore lie in \(y\ge0\), whereas the isolated-vertex pool lies on \(y=-1\).

This proves the augmentation lemma. \(\square\)

## 4. Completing the special-case theorem

Set
\[
q=3k.
\]
The core \(H\) constructed in Section 2 has at most \(q\) vertices. By the grid-drawing theorem stated in the question, it has a straight-line drawing on
\[
S=\{0,\ldots,q-1\}^2.
\]
One can pad \(H\) with isolated vertices before applying that theorem if necessary.

Apply the augmentation lemma:

- use leaf pools for the degree-one vertices outside the core;
- use midpoint pools for the degree-two vertices;
- use the pool below the grid for the isolated vertices.

Retain auxiliary core edges during this construction and delete them afterward. Deleting edges cannot invalidate the drawing.

The point set depends only on \(k,n\), not on \(G\), and
\[
|P(3k,n)|\le 6(3k)^2n=54k^2n.
\]
The alternative bound \(n^2\) is the supplied general grid bound.

For completeness, the coordinate complexity is also explicit: multiplying every coordinate in the construction by
\[
600q^5(n+1)
\]
makes all coordinates integers. Their magnitudes are \(O(q^6n)\), establishing the claimed bit-length bound. \(\square\)

## 5. What remains open

The restricted-class theorem has no remaining proof gap, but it does not approach a uniform linear constant when the vertex-cover parameter grows.

Planar graphs can have vertex-cover number \(\Theta(n)\). Substituting such a value into \(54k^2n\) is worse than the existing quadratic construction. Thus this argument neither proves nor disproves
\[
f(n)=O(n)
\]
and does not improve the unrestricted bounds quoted in the question.

The useful structural feature here is a **bounded core with only degree-one and degree-two independent attachments**. Extending the construction to arbitrary planar graphs would require a way to handle unbounded, interacting core structure—not merely a better choice of the constants or perturbation sizes.