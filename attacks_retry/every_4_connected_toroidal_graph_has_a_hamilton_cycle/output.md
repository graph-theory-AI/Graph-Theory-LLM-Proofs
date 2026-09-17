```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Constructive proofs cover the flat extremal cases, and a residue argument excludes exactly one triangular face, but the general conjecture remains unresolved here.",
  "would_publish": false,
  "caveats": "No novelty claim; the general minimum-degree-four or five case with multiple triangular faces is not solved."
}
```

# Partial results: flat embeddings and a single-triangle obstruction

All graphs below are finite and simple. Face lengths count edge occurrences in facial boundary walks.

I do **not** prove or disprove the full conjecture. I checked the square-grid and cycle-splicing arguments in the supplied attempt; those arguments are valid, and I give a self-contained version below. The additional conclusions are:

* a connected graph of minimum degree at least four cannot have a cellular torus embedding with exactly one triangular face;
* every connected toroidal graph of minimum degree at least six has a Hamilton cycle through each of its edges.

The first assertion uses a short complex-analytic obstruction for square cellulations of the torus.

## 1. Statements proved here

**Theorem 1.** Let \(G\) be a connected simple graph. Every edge of \(G\) lies on a Hamilton cycle in each of the following situations:

1. \(G\) is toroidal, triangle-free, and \(\delta(G)\ge 4\).
2. \(G\) has a cellular torus embedding with \(\delta(G)\ge 4\) and at most one triangular face.
3. \(G\) is toroidal and \(\delta(G)\ge 6\).

In situation 2, an embedding with exactly one triangular face is impossible.

Thus none of these special cases needs a separate 4-connectivity assumption.

I also verify the necessary cut condition from the supplied attempt:

**Proposition 2.** Every 4-connected toroidal graph is 1-tough: if \(G-S\) has at least two components, then
\[
c(G-S)\le |S|.
\]

Neither conclusion settles the remaining case.

---

## 2. Euler equality forces two flat structures

We first handle embeddings that are not assumed cellular.

Let \(G\) be connected and embedded in the torus. Put
\[
n=|V(G)|,\qquad m=|E(G)|.
\]
Take a closed regular neighbourhood \(N\) of the embedded graph, and let \(R_1,\dots,R_f\) be the components of the closure of its complement. Since \(N\) retracts onto \(G\),
\[
0=\chi(\mathbb T^2)=n-m+\sum_{i=1}^f\chi(R_i).
\]
Every \(R_i\) has nonempty boundary and satisfies \(\chi(R_i)\le 1\). Hence
\[
m-n\le f. \tag{1}
\]

The boundary walks of \(N\) have total length \(2m\). If every such walk has length at least \(g\), then there are at least \(f\) boundary walks, and therefore
\[
2m\ge gf. \tag{2}
\]

In a simple graph of minimum degree at least two, a boundary walk cannot have length one or two. In particular, immediate reversal along an edge at a vertex would require that vertex to have degree one. A boundary walk of length three traces a triangle.

### 2.1. Minimum degree four, with no triangles

If \(G\) is triangle-free and \(\delta(G)\ge4\), then (2) holds with \(g=4\). Thus
\[
m-n\le f\le \frac m2,
\]
giving \(m\le2n\). The degree condition gives \(m\ge2n\), so equality holds throughout.

Consequently:

* every vertex has degree four;
* every \(R_i\) is a disk;
* every face has length four.

The facial walks are genuine 4-cycles: a repeated vertex in a length-four closed walk in a simple graph would force an immediate edge reversal.

The same conclusion follows if the embedding is already cellular and has no triangular faces, whether or not \(G\) has nonfacial triangles.

### 2.2. Minimum degree six

If \(\delta(G)\ge6\), simplicity gives (2) with \(g=3\). Hence
\[
m-n\le f\le\frac{2m}{3},
\]
so \(m\le3n\). The degree condition gives the reverse inequality. Equality now implies:

* every vertex has degree six;
* the embedding is cellular;
* every face is a triangle.

We have therefore reduced the relevant cases to:

\[
\begin{array}{c|c}
\text{vertex degrees}&\text{face lengths}\\ \hline
4&4\\
6&3
\end{array}
\]

---

## 3. Flat tilings and Hamilton cycles

### 3.1. The quotient structure

Give every quadrilateral in the first case the metric of a Euclidean unit square. Exactly four square corners meet at each vertex, so the total angle there is \(2\pi\).

In the second case, give every triangular face the metric of a unit equilateral triangle. Six triangle corners meet at each vertex, again giving angle \(2\pi\).

In either case this defines an everywhere-flat metric on the torus. Its universal cover is a complete simply connected flat surface, hence isometric to \(\mathbb R^2\). Developing the lifted faces gives, respectively, the standard square tiling or triangular tiling.

A deck transformation preserves orientation and the Euclidean metric. A nonidentity orientation-preserving Euclidean isometry is either a translation or a rotation. A rotation has a fixed point, whereas a nonidentity deck transformation does not. Thus all deck transformations are translations.

It follows that the embedded graph is a quotient of the appropriate lattice by a finite-index translation subgroup.

For the square tiling, write the vertex group as
\[
A=\mathbb Z^2/\Lambda
\]
and let \(a,b\) be the images of the two unit coordinate vectors. Its edges are
\[
x\sim x\pm a,\qquad x\sim x\pm b. \tag{3}
\]

For the triangular tiling, choose two unit lattice vectors making an angle of \(60^\circ\). Using their images \(a,b\), its edges are
\[
x\sim x\pm a,\qquad x\sim x\pm b,\qquad x\sim x\pm(a-b). \tag{4}
\]

Simplicity and the indicated degrees ensure that the listed neighbours are distinct. In particular, every listed direction has order at least three.

### 3.2. A two-generator construction

**Lemma 3.** Let \(A\) be a finite abelian group generated by \(a,b\), where
\[
a,-a,b,-b
\]
are distinct nonzero elements. Then the graph with edges (3) has a Hamilton cycle through each of its edges.

**Proof.**
Put
\[
r=\operatorname{ord}(a),\qquad s=[A:\langle a\rangle].
\]
Since \(a,b\) generate \(A\), the quotient \(A/\langle a\rangle\) is cyclic and generated by the image of \(b\). Its cosets are
\[
\langle a\rangle,\ b+\langle a\rangle,\ldots,(s-1)b+\langle a\rangle.
\]

The \(a\)-edges form disjoint row cycles
\[
C_j=(jb,\ jb+a,\ldots,jb+(r-1)a,\ jb),
\qquad 0\le j<s.
\]
They span the graph. Between consecutive rows there are matching edges
\[
jb+ia\sim(j+1)b+ia,\qquad 0\le j<s-1.
\]

Start with \(C_0\), and join the rows successively. Suppose the current cycle spans rows \(0,\ldots,j\). Choose an available \(a\)-edge \(xy\) in row \(j\), and put
\[
x'=x+b,\qquad y'=y+b.
\]
Delete \(xy\) and the corresponding edge \(x'y'\) of \(C_{j+1}\), and add
\[
xx',\qquad yy'.
\]
Two vertex-disjoint cycles have thereby been joined into one cycle.

To ensure availability, alternate between the two row-edge positions
\[
\{jb,jb+a\},\qquad \{jb+a,jb+2a\}.
\]
These are distinct because \(r\ge3\). Thus in an intermediate row, the edge chosen for the next splice differs from the edge removed by the preceding splice.

After \(s-1\) splices, the cycle is Hamiltonian. This construction also covers \(s=1\), when the original row cycle is already Hamiltonian.

Each row loses at most two \(a\)-edges, so at least one \(a\)-edge remains. Translations of \(A\) are graph automorphisms and are transitive on the \(a\)-edges. Translating the constructed cycle therefore puts any prescribed \(a\)-edge on a Hamilton cycle.

Repeating the construction with \(a,b\) interchanged proves the same assertion for every \(b\)-edge. ∎

This proves Theorem 1 for the square-tiling cases.

For the triangular tiling, the directions \(a,b\) give a spanning square-grid-type subgraph, so Lemma 3 supplies Hamilton cycles through all edges in those two directions. For an edge in direction
\[
c=a-b,
\]
apply the lemma to \(c,b\): these elements generate \(A\), because \(a=c+b\). This proves the minimum-degree-six case as well.

---

## 4. Exactly one triangular face is impossible

The missing step for Theorem 1(2) is not a Hamilton-cycle construction: it is an embedding obstruction.

### 4.1. A square-cellulation obstruction

The following lemma allows multiple edges and identifications among the corners of a face. Degrees count incident corners with multiplicity.

**Lemma 4.** There is no quadrilateral cellulation of the orientable torus having exactly one vertex of degree three and all other vertices of degree at least four.

**Proof.**
Give every face the metric of a Euclidean unit square, glued according to the cellulation. A vertex of degree \(k\) has cone angle
\[
\frac{k\pi}{2}.
\]

Away from the vertices, oriented square coordinates have transition maps
\[
z\longmapsto \zeta z+c,\qquad \zeta^4=1.
\]
Consequently, the local expressions
\[
q=(dz)^4
\]
define a global quartic differential away from the vertices.

The metric induces a conformal structure extending over the cone points. At a degree-\(k\) vertex, a local coordinate \(z\) can be chosen so that a developed Euclidean coordinate is
\[
w=z^{k/4}.
\]
Thus, up to a nonzero constant,
\[
q=(dw)^4
  =\left(\frac{k}{4}\right)^4 z^{k-4}(dz)^4.
\]
Therefore \(q\) extends meromorphically across the vertices, with order \(k-4\) at a degree-\(k\) vertex.

Under the hypotheses, \(q\) has exactly one pole, and that pole is simple.

A compact Riemann surface of genus one has a nowhere-vanishing holomorphic one-form \(\omega\). For example, this follows by uniformizing it as \(\mathbb C/L\) and descending \(dz\). Hence
\[
\eta=\frac{q}{\omega^3}
\]
is a meromorphic one-form with exactly one pole, again simple.

The residue at a simple pole of a one-form is nonzero. This contradicts the global residue theorem, which says that the sum of all residues on a compact Riemann surface is zero. ∎

### 4.2. Applying the obstruction to the graph

Let \(G\) have a cellular torus embedding with \(\delta(G)\ge4\). Write \(t\) for its number of triangular faces, and put
\[
D=\sum_{v\in V(G)}(d(v)-4),\qquad
L=\sum_{\ell(F)\ge5}(\ell(F)-4).
\]
Euler’s formula gives
\[
\sum_v(d(v)-4)+\sum_F(\ell(F)-4)=0.
\]
Equivalently,
\[
\boxed{t=D+L.} \tag{5}
\]

Both \(D\) and \(L\) are nonnegative. Moreover,
\[
D=2m-4n
\]
is even.

Suppose that \(t=1\). Equation (5) forces
\[
D=0,\qquad L=1.
\]
Therefore:

* \(G\) is 4-regular;
* there is exactly one triangular face;
* there is exactly one pentagonal face;
* every other face is quadrilateral.

Now take the cellular dual \(Q\). Since \(G\) is 4-regular, every face of \(Q\) is a quadrilateral. Its vertex degrees are the face lengths of \(G\), so \(Q\) has exactly one degree-three vertex, exactly one degree-five vertex, and all other vertices have degree four.

This contradicts Lemma 4.

Thus:

\[
\boxed{\text{A cellular torus embedding with }\delta(G)\ge4
       \text{ cannot have exactly one triangular face.}}
\]

In particular, “at most one triangular face” in Theorem 1(2) reduces to the zero-triangle case already proved. This completes the proof of Theorem 1.

---

## 5. The stronger edge conclusion already fails at two triangular faces

The triangular-face threshold above is sharp for the assertion that **every edge** lies on a Hamilton cycle. This is not a counterexample to ordinary Hamiltonicity.

Consider the square-tiling quotient with
\[
A=\mathbb Z_4\times\mathbb Z_2,\qquad
a=(1,0),\qquad b=(1,1).
\]
Equivalently, its translation lattice is
\[
\Lambda=\langle(4,0),(-2,2)\rangle.
\]
The four neighbours of each vertex are exactly the four vertices having opposite first-coordinate parity. Thus the quotient graph is \(K_{4,4}\), embedded with quadrilateral faces.

One face has boundary
\[
0,\ a,\ a+b,\ b,\ 0.
\]
Add the diagonal joining \(0\) to \(a+b\), whose endpoints are in the same bipartition class.

The resulting graph \(G^+\):

* is toroidal;
* is 4-connected, since it contains the spanning 4-connected graph \(K_{4,4}\);
* has exactly two triangular faces, with every other face quadrilateral;
* is Hamiltonian, since \(K_{4,4}\) is Hamiltonian.

However, the new diagonal lies on no Hamilton cycle. The other bipartition class remains an independent set of four vertices in an eight-vertex graph. A Hamilton cycle has eight edges, and its incidences at those four independent vertices already account for all eight edges. Hence every Hamilton cycle must alternate between the two classes and cannot use the diagonal.

So the flat-case proof cannot be extended to a general prescribed-edge theorem, even at the first possible positive number of triangular faces.

---

## 6. Verification of the cut restriction

Let \(G\) be 4-connected and toroidal, and suppose \(G-S\) has components
\[
D_1,\ldots,D_c,\qquad c\ge2.
\]
Write \(s=|S|\).

Each \(D_i\) has at least four distinct neighbours in \(S\). Otherwise, its neighbourhood would be a vertex cut of size at most three separating it from another component of \(G-S\).

Contract each \(D_i\) to a vertex \(d_i\). Delete edges within \(S\), loops, and duplicate edges. The resulting graph \(H\) is a simple bipartite toroidal graph with
\[
|V(H)|=s+c,\qquad |E(H)|\ge4c.
\]

The bipartite torus Euler bound is
\[
|E(H)|\le2|V(H)|.
\]
For completeness, this bound also covers noncellular and disconnected embeddings: delete vertices of degree at most one by induction, and apply the regular-neighbourhood calculation from Section 2, with boundary-walk length at least four, to each remaining component.

Consequently,
\[
4c\le2(s+c),
\]
so \(c\le s\). This proves Proposition 2.

In particular, every independent set \(I\) satisfies
\[
|I|\le\frac{|V(G)|}{2}.
\]

These are necessary Hamiltonicity conditions, not sufficient ones.

---

## 7. What remains unresolved

The rigorous restrictions obtained here are as follows. Any counterexample to the original conjecture must:

1. be nonplanar, by the planar theorem stated in the question;
2. have minimum degree either four or five, by Theorem 1(3);
3. have at least two triangular faces in every cellular torus embedding;
4. satisfy \(c(G-S)\le |S|\) for every separating set \(S\).

The curvature identity gives a little more detail. If \(\delta(G)\ge5\), then
\[
t\ge D\ge |V(G)|.
\]

Already at \(t=2\), however, Euler’s formula permits two substantially different patterns:

* all vertices have degree four, and the nonquadrilateral faces are two triangles together with either one hexagon or two pentagons;
* all nontriangular faces are quadrilateral, and the degree excess consists of either one degree-six vertex or two degree-five vertices.

The square-grid construction does not handle these general defect patterns. In particular, **4-regularity alone does not imply a square-grid quotient**: triangular faces can be balanced by longer faces.

The residue obstruction also stops precisely here. With two or more simple poles, residues can cancel, so the contradiction used in Lemma 4 no longer follows. Finally, the cut inequality does not supply the internal routing needed to turn a spanning collection of cycles or paths into a Hamilton cycle.

Thus the argument gives complete proofs of the stated special cases and an additional embedding obstruction, but no proof or counterexample for the full 4-connected toroidal conjecture.