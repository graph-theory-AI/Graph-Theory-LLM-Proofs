```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A counterexample is reduced to a rainbow-precoloring obstruction on a triangulated quadrilateral, and any vertex-minimal counterexample must have at least five internal degree-five vertices, at least two internal vertices anticomplete to the boundary, and a strong Kempe-locking property.",
  "would_publish": false,
  "caveats": "The decisive step that Kempe locking forces an internal degree-four vertex remains open; the reported computation through 28 vertices was not independently rerun."
}
```

## 1. Statement and notation

Let \(T\) be a 4-connected plane triangulation, let \(uv\in E(T)\), and let \(uvx\) and \(uvy\) be the two facial triangles incident with \(uv\). Put
\[
G=T+xy.
\]
The four vertices
\[
B=\{x,u,y,v\}
\]
are external, and all other vertices are internal. Since \(T\) is 4-connected, \(xy\notin E(T)\), apart from the irrelevant tetrahedral degeneracy.

The conjecture is:

> If \(G\) is not 4-colorable, then some internal vertex has degree four.

I do not prove or disprove this. The main output below is an exact disk reformulation and several necessary conditions for a minimal counterexample.

---

## 2. Exact quadrilateral reformulation

Delete the edge \(uv\) from \(T\), and regard the union of the two faces \(uvx,uvy\) as the outer face. The resulting graph
\[
P=T-uv
\]
has chordless outer cycle
\[
C=xuyvx,
\]
all bounded faces are triangles, and \(P\) has no separating triangle. The internal degrees in \(P\) are the same as in \(T\).

The graph \(G\) is obtained from \(P\) by adding both diagonals \(uv\) and \(xy\). Thus \(B\) induces a \(K_4\) in \(G\).

### Lemma 2.1: Rainbow-boundary formulation

The following are equivalent:

1. \(G\) is 4-colorable.
2. \(T\) has a 4-coloring with \(x\ne y\).
3. \(P\) has a 4-coloring in which the four boundary vertices \(x,u,y,v\) receive four distinct colors.
4. Any prescribed assignment of four distinct colors to \(x,u,y,v\) extends to \(P\).

#### Proof

The equivalence of 1 and 2 is immediate from \(G=T+xy\).

In every coloring of \(T\), the triangles \(xuv\) and \(yuv\) imply that \(x\) and \(y\) each avoid the two distinct colors on \(u,v\). If \(x\ne y\), all four external vertices therefore have different colors. Conversely, a rainbow coloring of the boundary of \(P\) satisfies both added diagonals.

Finally, all rainbow assignments differ only by a global permutation of the four colors. ∎

Thus a counterexample without an internal degree-four vertex is precisely a nonextendable rainbow precoloring of a triangulated quadrilateral whose internal degrees are at least five.

---

## 3. The disk formulation is genuinely equivalent

For completeness, one must check that arbitrary triangulated quadrilateral instances of the above type can be completed to members of \({\cal C}_0\).

Call \(P\) an admissible disk if:

- its outer boundary is a chordless cycle \(abcd\);
- every bounded face is triangular;
- it has no separating triangle;
- every internal vertex has degree at least five.

### Lemma 3.1: Safe diagonal lemma

For every admissible disk \(P\), at least one of the two diagonals \(ac,bd\) can be added in the outer face so that the resulting plane triangulation is 4-connected.

#### Proof

Adding \(ac\) can create a new nonfacial triangle only if there is an internal vertex adjacent to both \(a\) and \(c\). Thus call \(ac\) unsafe if such a vertex exists; define unsafe for \(bd\) analogously.

Suppose both diagonals are unsafe. Then there are internal vertices \(w,z\) and paths
\[
a-w-c,\qquad b-z-d.
\]
These paths join alternating pairs on the boundary of a disk. By planarity they must meet. Since their boundary endpoints are distinct and each path has only one internal vertex, \(w=z\). Hence \(w\) is adjacent to all four boundary vertices.

The four cycles
\[
abw,\quad bcw,\quad cdw,\quad daw
\]
are triangles. As \(P\) has no separating triangle, each bounds a face. These four faces fill the disk, so \(w\) has degree four, contrary to admissibility. Hence at least one diagonal is safe.

After a safe diagonal is added, there is no separating triangle. A degree-three vertex would also force an internal common neighbor of the endpoints of the safe diagonal, so the resulting triangulation has minimum degree at least four. The standard separator characterization of plane triangulations now gives 4-connectivity. ∎

### Corollary 3.2

The original conjecture is equivalent to the following disk statement:

> Every admissible disk admits an extension of a rainbow coloring of its outer 4-cycle.

Indeed, after adding a safe diagonal, adding the other diagonal gives a member of \({\cal C}_0\), and its 4-colorings are exactly the rainbow-boundary extensions.

This formulation removes the apparently asymmetric role of the originally chosen diagonal \(uv\).

---

## 4. Exact counting restrictions

Let \(P\) be an admissible disk, let \(I\) be its internal vertex set, and put
\[
N=|I|,\qquad
q=\sum_{z\in I}\bigl(d_P(z)-5\bigr)\ge 0.
\]

Let \(e(B,I)\) denote the number of edges between the boundary and the interior.

### Lemma 4.1: Boundary-incidence identity

\[
e(B,I)=N+2-q.
\]

#### Proof

A triangulated disk with outer boundary of length four and \(N\) internal vertices has
\[
|E(P)|=3N+5.
\]
There are four boundary edges. If \(m_I\) is the number of edges with both ends internal and \(b=e(B,I)\), then
\[
m_I+b=3N+1.
\]
Consequently,
\[
\sum_{z\in I}d_P(z)=2m_I+b=6N+2-b.
\]
The left side is \(5N+q\), giving \(b=N+2-q\). ∎

For \(0\le j\le 3\), let
\[
n_j=\bigl|\{z\in I:|N(z)\cap B|=j\}\bigr|.
\]
No internal vertex can be adjacent to all four boundary vertices: as in Lemma 3.1, such a vertex would have degree four.

Each of the four boundary edges has an internal third vertex in its incident triangular face. A vertex with two boundary neighbors can account for at most one such boundary edge, while a vertex with three boundary neighbors accounts for at most two. Therefore
\[
n_2+2n_3\ge 4.
\]

On the other hand, Lemma 4.1 gives
\[
\sum_{z\in I}\bigl(|N(z)\cap B|-1\bigr)=2-q,
\]
or
\[
-n_0+n_2+2n_3=2-q.
\]
Hence:

### Corollary 4.2: Deep internal vertices

\[
n_0=n_2+2n_3-2+q\ge q+2.
\]

Thus every hypothetical counterexample without an internal degree-four vertex has at least two internal vertices with no neighbor among the four external vertices. More generally, each unit of degree excess above five forces an additional such vertex.

This seems useful for any layer-by-layer or reducibility attack: an obstruction cannot be concentrated entirely near the crossed \(K_4\).

---

## 5. A reduction for minimal counterexamples

Assume the disk statement is false, and choose a nonextendable admissible disk \(P\) with as few vertices as possible.

A boundary vertex has degree at least three. An internal vertex adjacent to three boundary vertices is naturally associated with a boundary vertex of degree three:

- if \(b\) has boundary neighbors \(a,c\) and \(d_P(b)=3\), its unique internal neighbor is adjacent to \(a,b,c\);
- conversely, an internal vertex adjacent to \(a,b,c\) forces \(b\) to have degree three.

Hence \(n_3\) is exactly the number of degree-three boundary vertices.

### Lemma 5.1

A minimal nonextendable admissible disk has at most one degree-three boundary vertex.

#### Proof

First, two adjacent boundary vertices cannot both have degree three. Suppose \(b,c\) are adjacent degree-three boundary vertices of \(abcd\). The triangular face incident with \(bc\) shows that their unique internal neighbors coincide, say at \(w\). Then \(w\) is adjacent to all four boundary vertices. The no-separating-triangle condition forces \(d(w)=4\), a contradiction.

It remains to exclude two opposite degree-three vertices, say \(b,d\). Let \(p\) and \(q\) be their unique internal neighbors. Then
\[
N(b)=\{a,c,p\},\qquad N(d)=\{a,c,q\}.
\]
The vertices \(p,q\) are distinct, since otherwise their common value would be adjacent to all four boundary vertices and have degree four.

Delete \(b,d\). The remaining graph \(P'\) is a triangulated disk with outer cycle
\[
a\,p\,c\,q\,a.
\]
All vertices internal in \(P'\) retain their degrees, because \(b\) and \(d\) had no other neighbors. The no-separating-triangle property is inherited.

If \(pq\in E(P')\), then the triangles \(apq\) and \(cpq\) must both be facial, so \(P'\) has no internal vertex. It is then plainly rainbow-colorable, and so is \(P\), a contradiction. Thus the new outer 4-cycle is chordless and \(P'\) is admissible.

Now fix a rainbow boundary assignment
\[
c(a)=A,\quad c(b)=B,\quad c(c)=C,\quad c(d)=D.
\]
In any extension, adjacency to \(a,b,c\) forces \(c(p)=D\), and adjacency to \(a,c,d\) forces \(c(q)=B\). Therefore
\[
a,p,c,q
\]
are again prescribed four distinct colors. Moreover, this new rainbow coloring extends to \(P'\) if and only if the original one extends to \(P\). Hence \(P'\) is a smaller nonextendable admissible disk, contradicting minimality. ∎

For the original representation \(P=T-uv\), the only boundary vertices that can have degree three are \(u,v\), since
\[
d_P(u)=d_T(u)-1,\qquad d_P(v)=d_T(v)-1,
\]
while \(d_P(x)=d_T(x)\) and \(d_P(y)=d_T(y)\). Consequently:

> In a vertex-minimal counterexample with no internal degree-four vertex, at most one of \(u,v\) has degree four in \(T\).

---

## 6. At least five internal degree-five vertices

For a triangulated disk with outer 4-cycle,
\[
\sum_{z\in I}(6-d(z))+\sum_{b\in B}(4-d(b))=6.
\]

Let
\[
p=\sum_{\substack{z\in I\\d(z)\ge7}}(d(z)-6),
\]
and let \(n_5\) be the number of internal degree-five vertices. Then
\[
\sum_{z\in I}(6-d(z))=n_5-p.
\]

In a minimal counterexample, Lemma 5.1 says that at most one boundary vertex has degree three; all other boundary vertices have degree at least four. Therefore
\[
\sum_{b\in B}(4-d(b))\le 1.
\]
It follows that
\[
n_5-p\ge5.
\]

### Corollary 6.1

Every vertex-minimal counterexample without an internal degree-four vertex satisfies
\[
n_5\ge 5+p.
\]

In particular, it has at least five internal degree-five vertices. If no boundary vertex has degree three, then the same argument gives
\[
n_5\ge 6+p.
\]

A weaker conclusion not requiring minimality is that every violating counterexample has at least four internal degree-five vertices, directly from
\[
\sum_{v\in V(T)}(6-d_T(v))=12
\]
and the fact that the four external vertices contribute at most eight.

This also proves the conjecture in the elementary special case where there is no internal degree-five vertex: if there were also no internal degree-four vertex, all internal degrees would be at least six, contradicting Euler curvature.

---

## 7. Kempe locking

Let \(G=T+xy\) be non-4-colorable. By the Four Color Theorem, \(T\) has a 4-coloring. Every such coloring has \(x=y\).

Normalize one such coloring by
\[
c(x)=c(y)=1,\qquad c(u)=2,\qquad c(v)=3,
\]
with fourth color \(4\).

### Lemma 7.1

In every such coloring, \(x\) and \(y\) lie in the same component of the subgraph induced by colors \(1\) and \(4\).

#### Proof

If they were in different components, interchange colors \(1\) and \(4\) in the component containing \(x\). This is a valid Kempe change and produces a coloring of \(T\) with \(x\ne y\), hence a 4-coloring of \(G\). ∎

Thus any counterexample is Kempe-locked at the selected edge.

There is a useful dual strengthening. Let \(H=T^*\), and let \(e\) be the dual edge corresponding to \(uv\), with endpoints \(A,B\) corresponding to the faces \(uvx,uvy\).

Represent the four vertex colors by \(\mathbb Z_2^2\). Label each primal edge \(rs\) by
\[
c(r)+c(s)\in\mathbb Z_2^2\setminus\{0\}.
\]
The three edges of every triangle receive the three nonzero elements, so this is a proper 3-edge-coloring of \(H\). Conversely, every proper 3-edge-coloring of \(H\) integrates to a vertex 4-coloring of \(T\).

Suppose \(e\) has color \(\alpha\), and let \(\beta,\gamma\) be the other two colors. The \(\beta\gamma\)-edges form a spanning union of disjoint even cycles.

### Lemma 7.2: Dual locking condition

If \(G\) is non-4-colorable, then in every proper 3-edge-coloring of \(H\), the endpoints \(A,B\) of \(e\) lie on the same \(\beta\gamma\)-cycle.

#### Proof

If \(A,B\) lie on different \(\beta\gamma\)-cycles, interchange \(\beta,\gamma\) on the cycle containing \(A\). This changes the \(\beta/\gamma\) assignment at \(A\) but not at \(B\). In primal terms it toggles whether the two opposite vertices \(x,y\) have equal colors. Therefore one of the two Tait colorings yields \(x\ne y\), and hence colors \(G\). ∎

The converse is not valid: being on the same cycle does not itself determine the local parity at \(A,B\). Thus Lemma 7.2 is a necessary, not sufficient, characterization.

A modest aggregate consequence is also available. If, in some Tait coloring, the \(\beta\gamma\)-factor has \(k\ge2\) cycles, then every \(\alpha\)-edge joining two different cycles certifies colorability for the corresponding choice of crossed primal edge. Since \(H\) is cyclically 4-edge-connected, every one of the \(k\) cycles has at least four \(\alpha\)-edges leaving it. Hence at least \(2k\) \(\alpha\)-edges join distinct cycles. A genuinely locked edge must avoid all these certificates in every Tait coloring.

In dual language, the conjecture asks one to prove that such persistent local locking forces a quadrilateral face of \(H\) other than the four faces corresponding to \(x,u,y,v\).

---

## 8. A completely solved family

Suppose every internal vertex is adjacent to both \(x\) and \(y\). Then \(x\) and \(y\) are adjacent to every other vertex of \(T\).

The neighbors of \(x\) occur in a cycle. Since \(T\) has no separating triangle, no two nonconsecutive neighbors of \(x\) can be adjacent. Hence
\[
T=C_m\vee \overline{K_2},
\]
the suspension of a cycle, with suspension vertices \(x,y\). The chosen \(uv\) is an edge of \(C_m\), and
\[
G=C_m\vee K_2.
\]
Therefore
\[
\chi(G)=\chi(C_m)+2.
\]
If \(m\) is even, \(G\) is 4-colorable. If \(m\) is odd, \(G\) is 5-chromatic, but every cycle vertex has degree four; in particular every vertex of \(C_m-\{u,v\}\) is an internal degree-four vertex.

Thus the conjecture holds for this natural “bipyramid” family, which supplies the basic examples of non-4-colorable graphs in the broader one-crossing setting.

Also, if \(T\) is 3-colorable, then \(G\) is 4-colorable: in a 3-coloring the two opposite vertices \(x,y\) have the same third color, and recoloring \(y\) with a new fourth color gives a coloring of \(G\).

---

## 9. Reproducible computational test

The computation reported in the source paper through 28 vertices can be formulated particularly simply using the disk version.

For each unlabelled 4-connected plane triangulation \(T\) and each edge orbit representative \(uv\):

1. Determine the incident faces \(uvx,uvy\).
2. Discard the instance if an internal vertex has degree four.
3. Form \(P=T-uv\) with outer order \(x,u,y,v\).
4. Fix boundary colors
   \[
   c(x)=1,\quad c(u)=2,\quad c(y)=3,\quad c(v)=4.
   \]
5. For each internal vertex \(z\) and color \(i\), introduce a Boolean variable \(X_{z,i}\).
6. Add:
   - one “at least one color” clause for each \(z\);
   - pairwise “at most one color” clauses;
   - \(\neg X_{z,i}\vee\neg X_{w,i}\) for every internal edge \(zw\);
   - \(\neg X_{z,c(b)}\) whenever \(z\) is adjacent to a boundary vertex \(b\).

The conjecture fails exactly when one of these formulas is unsatisfiable. A fully auditable enumeration should retain the canonical-generation certificate for the triangulations and DRAT/LRAT certificates for every unsatisfiable instance. I have not rerun the source computation.

---

## 10. Remaining gap

The unresolved implication is now quite sharp:

> Let \(P\) be a minimal nonextendable rainbow-precolored admissible disk. Prove that \(P\) has an internal vertex of degree four.

The reductions above show that, if such a minimal obstruction exists with all internal degrees at least five, then:

- at most one boundary vertex has degree three;
- there are at least five internal degree-five vertices;
- at least \(q+2\) internal vertices are anticomplete to the boundary, where \(q=\sum(d-5)\);
- every coloring of either diagonal completion is Kempe-locked at the distinguished diagonal;
- in the cubic dual, the relevant dual-edge endpoints lie on the same complementary bicolored cycle in every Tait coloring.

I do not have a valid argument turning these conditions into a degree-four vertex. That is the substantive missing step, and it appears to contain the original difficulty rather than being a routine discharging conclusion.