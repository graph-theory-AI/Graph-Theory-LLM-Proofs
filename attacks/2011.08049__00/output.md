```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The literal average-degree-at-most-6 problem is approximation-preserving equivalent to unrestricted genus, even when the constructed instances are connected, simple, and have minimum degree at least three.",
  "would_publish": false,
  "caveats": "This yields neither a constant-factor algorithm nor an inapproximability theorem, and it does not reduce arbitrary graphs to cubic or irreducible 3-connected graphs."
}
```

# Mathematical writeup

## 1. Statement and interpretation

Let \(\gamma(G)\) denote the minimum orientable genus of a finite simple graph \(G\), and let
\[
\overline d(G)=\frac{2|E(G)|}{|V(G)|}.
\]
I interpret a \(C\)-approximation as an algorithm returning either an integer or an embedding of genus \(h\) satisfying
\[
\gamma(G)\le h\le C\gamma(G).
\]

I do not resolve the existence of such an algorithm or prove approximation hardness. I prove instead that the literal average-degree restriction is not an algorithmic simplification: it admits exact, genus-preserving padding reductions from unrestricted graphs.

## 2. Basic genus-preserving operations

We use three elementary facts.

### Lemma 2.1

1. Subdividing edges does not change orientable genus.
2. If a planar graph \(P\) is attached to \(G\) by identifying one vertex of \(P\) with one vertex of \(G\), then the resulting graph has genus \(\gamma(G)\).
3. Suppose \(uv\in E(G)\), \(ab\in E(P)\), and \(P\) is planar. Form an edge-amalgam by identifying \(a\) with \(u\), \(b\) with \(v\), and \(ab\) with \(uv\). The resulting graph also has genus \(\gamma(G)\).

#### Proof

For subdivision, an embedding of \(G\) can be subdivided by marking points on its edge-arcs. Conversely, suppressing the resulting degree-two vertices in any embedding recovers an embedding of \(G\) on the same surface.

In the other two cases, the resulting graph contains \(G\), so its genus is at least \(\gamma(G)\). For the reverse inequality, take a minimum-genus embedding of \(G\). A planar graph attached at one vertex can be drawn in a sufficiently small disk tangent to that vertex. For an edge-amalgam, choose a planar embedding of \(P\) with \(ab\) on the boundary of its outer face and draw \(P-ab\) in a sufficiently small one-sided lens along the embedded edge \(uv\). Thus the attachment creates no additional handles. \(\square\)

## 3. Exact reduction to bipartite graphs of average degree below four

Let \(S(G)\) be obtained by subdividing every edge of \(G\) exactly once. If \(G\) has \(n\) vertices and \(m\) edges, then
\[
|V(S(G))|=n+m,\qquad |E(S(G))|=2m,
\]
and hence
\[
\overline d(S(G))=\frac{4m}{n+m}<4
\]
for every nonempty \(G\). Moreover, \(S(G)\) is bipartite, with one part consisting of the original vertices and the other of the subdivision vertices. By Lemma 2.1,
\[
\gamma(S(G))=\gamma(G).
\]

Consequently:

### Theorem 3.1

For every constant \(C\), a polynomial-time \(C\)-approximation for genus on bipartite graphs of average degree below \(4\) would give a polynomial-time \(C\)-approximation for unrestricted genus.

The reduction has no additive error and no distortion of the approximation ratio. If an embedding is returned, suppressing the subdivision vertices recovers an embedding of \(G\) on the same surface.

The same conclusion holds for PTASs, EPTASs, randomized approximation schemes, and approximation-hardness results, subject only to their usual polynomial-time conventions.

### A sharp connected version

If every edge is subdivided \(t\) times, the resulting graph \(S_t(G)\) has
\[
N=n+tm,\qquad M=(t+1)m,
\]
and therefore
\[
\overline d(S_t(G))
 =\frac{2(t+1)m}{n+tm}
 =2+\frac{2(m-n)}{n+tm}
 <2+\frac2t.
\]
If \(t\) is odd, \(S_t(G)\) is bipartite. Thus, for every fixed \(D>2\), choosing a sufficiently large odd \(t\) gives an exact genus-preserving reduction from connected graphs to connected bipartite graphs of average degree below \(D\).

This threshold is sharp for connected graphs: if \(G\) is connected and \(\overline d(G)\le2\), then \(m\le n\), so its cyclomatic number \(m-n+1\) is at most one. Hence \(G\) is a tree or unicyclic and is planar.

Without connectedness, even this threshold disappears: adding sufficiently many isolated vertices reduces the global average degree below any fixed positive constant without changing genus.

## 4. Removing the degree-two padding objection

The subdivision reduction might be dismissed if the intended density is measured after suppressing degree-two vertices. The next construction avoids vertices of degree below three.

### Theorem 4.1

For every connected simple graph \(G\), one can construct in polynomial time a connected simple graph \(H\) such that
\[
\delta(H)\ge3,\qquad \overline d(H)\le6,\qquad \gamma(H)=\gamma(G).
\]

#### Proof

Write \(n=|V(G)|\), \(m=|E(G)|\), and let
\[
r=\bigl|\{v\in V(G):d_G(v)<3\}\bigr|.
\]
A rooted \(K_4\)-attachment at \(v\) means taking a fresh copy of \(K_4\) and identifying one of its vertices with \(v\). It adds three vertices and six edges, raises the degree of \(v\) by three, and gives each new vertex degree three. By Lemma 2.1 it does not change genus.

Attach one rooted \(K_4\) at each vertex of degree below three. Then attach further rooted copies at any vertex until the total number \(s\) of copies satisfies
\[
s\ge r
\quad\text{and}\quad
3s\ge m-3n.
\]
The resulting graph has
\[
N=n+3s,\qquad M=m+6s.
\]
Thus
\[
M-3N=m-3n-3s\le0,
\]
so \(2M/N\le6\). Every original low-degree vertex has had its degree increased by three, every other original vertex already had degree at least three, and every new vertex has degree three. Hence \(\delta(H)\ge3\).

The copies intersect the old graph only at their roots, so simplicity and connectedness are preserved. Repeated application of Lemma 2.1 gives
\[
\gamma(H)=\gamma(G).
\]
Finally, \(s=O(n+m)\), so the construction is polynomial. \(\square\)

Therefore a constant-factor approximation on connected simple graphs satisfying both \(\delta(G)\ge3\) and \(\overline d(G)\le6\) would already solve unrestricted connected genus with exactly the same factor.

### General threshold \(D>3\)

The value \(6\) is not special here. Let \(P\) be a sufficiently large planar cubic graph on \(p\) vertices, rooted at one vertex. Attaching \(P\) at a vertex adds \(p-1\) vertices and \(3p/2\) edges. Its incremental average degree is
\[
\frac{3p}{p-1}=3+\frac{3}{p-1}.
\]
For every fixed \(D>3\), choose \(p\) so large that this is below \(D\). Repeating these planar rooted attachments both raises low degrees and eventually reduces the global average below \(D\), while preserving genus.

At the boundary \(D=3\), the situation changes: if \(\delta(G)\ge3\) and \(\overline d(G)\le3\), then every vertex has degree exactly three. Thus the cubic case is precisely the limiting case that this padding cannot reach.

## 5. A 2-connected strengthening

Even cutvertex padding is not essential at average degree six.

Let \(uv\in E(G)\). Glue a fresh \(K_4\) to \(G\) along the edge \(uv\). Equivalently, add two new vertices \(x,y\) and the five edges
\[
ux,\ uy,\ vx,\ vy,\ xy,
\]
retaining \(uv\).

This operation:

- preserves genus by Lemma 2.1;
- preserves simplicity;
- preserves 2-connectivity when \(G\) is 2-connected;
- gives \(x,y\) degree three and increases each of \(d(u),d(v)\) by two;
- changes the counts by
  \[
  \Delta n=2,\qquad \Delta m=5,
  \]
  and therefore decreases \(m-3n\) by one.

Starting from a 2-connected simple graph, first apply the operation at an edge incident with each degree-two vertex that remains. It creates no new degree-two vertices. Then repeat it arbitrarily until \(m\le3n\).

### Theorem 5.1

Every 2-connected simple graph \(G\) admits a polynomial-time genus-preserving transformation into a 2-connected simple graph \(H\) satisfying
\[
\delta(H)\ge3,\qquad \overline d(H)\le6.
\]

More generally, replacing \(K_4\) by a sufficiently large planar cubic graph \(P\) glued along a distinguished edge gives the same conclusion with any fixed average-degree cap \(D>3\). If \(P\) has \(p\) vertices, each attachment adds
\[
p-2\ \text{vertices},\qquad \frac{3p}{2}-1\ \text{edges},
\]
whose incremental average degree is
\[
\frac{3p-2}{p-2}=3+\frac4{p-2}.
\]
This can be made smaller than any prescribed \(D>3\).

Thus even deleting leaves, suppressing degree-two vertices, and decomposing at cutvertices does not by itself make the cap \(6\) structurally restrictive. Planar attachments along 2-separators can still dilute the average degree.

## 6. A limited positive approximation result

There is a simple constant approximation under a linear-genus promise.

For a connected graph let
\[
\beta(G)=m-n+1
\]
be its cyclomatic number. Choose arbitrary cyclic orders of the incident edges at all vertices. This rotation system gives a cellular orientable embedding. If it has \(f\ge1\) faces and genus \(h\), Euler's formula gives
\[
2-2h=n-m+f=1-\beta+f,
\]
and hence
\[
2h=1+\beta-f\le\beta.
\]
Therefore
\[
h\le \left\lfloor\frac{\beta}{2}\right\rfloor.
\]

Consequently, on the promised class
\[
\gamma(G)\ge\varepsilon\beta(G),
\]
an arbitrary rotation system is a \(1/(2\varepsilon)\)-approximation:
\[
\gamma(G)\le h\le\frac{\beta(G)}2
 \le\frac{\gamma(G)}{2\varepsilon}.
\]
This is constructive and polynomial-time. It only covers graphs whose genus is a fixed positive fraction of their cycle rank and does not recognize whether the promise holds.

## 7. What remains open

The reductions above do not produce a constant-factor algorithm or any new hardness theorem. Instead, they show that the literal condition \(\overline d(G)\le6\) contains exact encodings of unrestricted genus instances, even under connectedness and minimum-degree-three restrictions.

The essential missing step for the proposed cubic hardness direction is a genus-controlled reduction that also lowers all high degrees to three. None of the padding constructions does this: they preserve or increase old degrees. Indeed, minimum degree three together with average degree at most three forces cubicity, which is exactly the sharp boundary of these reductions.

If “spherical density regime” is intended to mean average degree after removing all genus-neutral planar 1- and 2-sum attachments, or if it includes a 3-connectivity or cubic hypothesis, then that normalization must be stated explicitly; the present reductions only address the literal catalog formulation.

Finally, under standard terminology, APX-hardness rules out a PTAS under the usual complexity assumptions but does not by itself rule out a constant-factor approximation. Thus “constant-factor approximation or APX-hardness” is not a logically exclusive dichotomy.