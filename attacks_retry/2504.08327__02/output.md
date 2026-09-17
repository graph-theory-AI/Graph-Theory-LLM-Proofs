```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A local extension lemma and two shrinking reductions give a seven-unit internal-curvature bound for a smallest counterexample, while an explicit family shows that the required degree-four vertex can be unique and arbitrarily far from the crossing.",
  "would_publish": false,
  "caveats": "The conjecture is not resolved; novelty is not assessed, and the reported enumeration through 28 vertices was not rerun."
}
```

# 1. Results obtained

I do not prove or disprove the conjecture. The main rigorous conclusions are:

1. **A local special case.** Suppose \(T\) is the underlying 4-connected plane triangulation, with incident faces \(uvx,uvy\). If
   \[
   d_T(u)=d_T(x)=4,
   \]
   or one of the three symmetric degree conditions holds, then the conjecture is true for this instance: either there is an internal degree-four vertex, or \(T+xy\) is 4-colorable.

2. **A stronger restriction on a smallest counterexample.** If a counterexample without an internal degree-four vertex exists, choose one with the fewest vertices. Let \(n_5\) be its number of internal degree-five vertices, and put
   \[
   h=\sum_{\substack{z\text{ internal}\\d(z)\ge 7}}(d(z)-6).
   \]
   Then
   \[
   \boxed{n_5\ge 7+h.}
   \]
   In particular, it has at least seven internal degree-five vertices, improving the five-vertex restriction in the supplied attempt.

3. **Sharpness and a limitation on local approaches.** There are explicit non-4-colorable graphs in \(\mathcal C_0\) with exactly one internal degree-four vertex. Its distance from the external vertices can be arbitrarily large. These are not counterexamples: they satisfy the proposed conclusion sharply.

I also give an exact identity for four boundary-coloring extension counts.

I rechecked the disk reformulation and the opposite-degree-three-corner reduction from the supplied attempt. They are reproved below. No computational or literature assertion from that attempt is needed.

# 2. Disk formulation

Let \(T\) be a 4-connected plane triangulation, with facial triangles \(uvx,uvy\), and let
\[
G=T+xy.
\]
Delete \(uv\), and use the resulting quadrilateral as the outer face. Thus
\[
P=T-uv
\]
is a triangulated disk with chordless outer cycle \(xuyv\).

The internal degrees are unchanged. Moreover,
\[
G\text{ is 4-colorable}
\quad\Longleftrightarrow\quad
P\text{ has a 4-coloring with four distinct boundary colors}.
\tag{2.1}
\]
Indeed, \(G\) adds both diagonals of the outer quadrilateral, so its four external vertices induce \(K_4\).

Call a disk \(P\) **admissible** if:

- its outer boundary is a chordless 4-cycle;
- every bounded face is triangular;
- it has no separating triangle;
- every internal vertex has degree at least five.

The conjecture is equivalent to saying that every admissible disk has a rainbow-boundary 4-coloring.

Here is the completion argument needed for that equivalence.

## Lemma 2.1 — Diagonal completion

At least one diagonal of the boundary of an admissible disk can be added to obtain a 4-connected plane triangulation.

### Proof

Write the boundary as \(abcd\). Adding \(ac\) can create a separating triangle only if an internal vertex is adjacent to both \(a,c\). Call \(ac\) unsafe in that case, and define unsafe for \(bd\) similarly.

If both diagonals are unsafe, there are paths
\[
a-p-c,\qquad b-q-d
\]
whose endpoints alternate on the disk boundary. The paths must intersect. Their only possible common vertex is \(p=q\), which is consequently adjacent to all four boundary vertices.

Every triangle in \(P\) bounds a bounded face: the exterior of any triangle contains at least one boundary vertex, so a nonfacial triangle would be separating. Therefore the four triangles around a vertex adjacent to all four boundary vertices fill the disk. That vertex has degree four, a contradiction.

A safe diagonal creates no separating triangle. The resulting simple plane triangulation has more than four vertices and no separating triangle, hence is 4-connected. ∎

A boundary vertex of an admissible disk has degree at least three. We will also repeatedly use the observation from the proof:

\[
\boxed{\text{No internal vertex of an admissible disk is adjacent to all four boundary vertices.}}
\tag{2.2}
\]

# 3. Three boundary reductions

Throughout this section, the boundary of \(P\) is \(abcd\) in cyclic order.

## Lemma 3.1 — A degree-three corner next to a degree-four corner

If
\[
d_P(b)=3,\qquad d_P(a)=4,
\]
then \(P\) has a rainbow-boundary 4-coloring.

### Proof

Let \(p\) be the unique internal neighbor of \(b\). Facial triangulation gives
\[
N(b)=\{a,c,p\},
\]
with \(ap,cp\in E(P)\).

Since \(a\) has degree four, it has exactly one other internal neighbor \(r\), and
\[
N(a)=\{b,d,p,r\}.
\]
The facial fan at \(a\) gives the edges \(pr,rd\).

Delete \(a,b\). The remaining graph \(Q\) is a plane disk with outer cycle
\[
p\,c\,d\,r\,p.
\]
It is harmless if this cycle has the chord \(cr\). On the other hand, \(pd\notin E(P)\), since otherwise \(p\) would be adjacent to all four original boundary vertices, contrary to (2.2).

Add \(pd\) in the outer face of \(Q\), contract this added edge, and discard parallel edges. The resulting graph is planar, so the Four Color Theorem gives a coloring which pulls back to a coloring of \(Q\) with
\[
c(p)=c(d).
\]
Because \(c,r\) are adjacent to both \(p,d\), a global permutation of colors allows us to arrange
\[
c(p)=c(d)=4,\qquad c(c)=3,\qquad c(r)\in\{2,3\}.
\]
Now set
\[
c(a)=1,\qquad c(b)=2.
\]
All edges incident with \(a\) or \(b\) are properly colored. The original boundary receives \(1,2,3,4\), as required. ∎

### Consequence for the original problem

In the original representation \(P=T-uv\), the vertices \(u,v\) lose one incident edge, whereas \(x,y\) do not. Hence Lemma 3.1 proves the conjecture whenever
\[
d_T(u)=d_T(x)=4,
\]
or symmetrically for \((u,y),(v,x),(v,y)\).

Equivalently, in a nonextendable admissible disk, the two boundary neighbors of any degree-three boundary vertex must both have degree at least five.

---

## Lemma 3.2 — Opposite degree-three corners

A vertex-minimal nonextendable admissible disk has at most one degree-three boundary vertex.

### Proof

Two adjacent degree-three boundary vertices are impossible even without minimality. If \(b,c\) both had degree three, the face incident with \(bc\) would show that their unique internal neighbors coincide. This vertex would be adjacent to all four boundary vertices, contradicting (2.2).

Suppose, then, that \(b,d\) have degree three. Let their unique internal neighbors be \(p,q\), respectively. Thus
\[
N(b)=\{a,c,p\},\qquad N(d)=\{a,c,q\}.
\]
The vertices \(p,q\) are distinct by (2.2).

Delete \(b,d\). The remaining disk \(Q\) has boundary
\[
a\,p\,c\,q\,a.
\]
It has no chord \(ac\). Nor can \(pq\) be an edge: the triangles \(apq,cpq\) would both be facial, leaving \(p\) with precisely the neighbors \(a,b,c,q\), contrary to its internal degree being at least five.

Thus \(Q\) has chordless boundary. It inherits the absence of separating triangles. Every vertex internal in \(Q\) retains its degree, since the only internal neighbors of the deleted vertices were \(p,q\). Hence \(Q\) is admissible.

Fix boundary colors
\[
c(a)=1,\quad c(b)=2,\quad c(c)=3,\quad c(d)=4.
\]
Any extension forces
\[
c(p)=4,\qquad c(q)=2.
\]
Consequently, the prescribed rainbow coloring of \(P\) extends if and only if the rainbow assignment
\[
(c(a),c(p),c(c),c(q))=(1,4,3,2)
\]
extends to \(Q\). A nonextendable \(P\) therefore gives a smaller nonextendable admissible disk, contradicting minimality. ∎

---

## Lemma 3.3 — A square collar can be stripped

Suppose all four boundary vertices of an admissible disk have degree four. Then there is a smaller admissible disk \(Q\) such that
\[
P\text{ has a rainbow-boundary coloring}
\quad\Longleftrightarrow\quad
Q\text{ has a rainbow-boundary coloring}.
\]

### Proof

Write the boundary as
\[
v_0v_1v_2v_3v_0,
\]
with indices modulo four. Let \(w_i\) be the third vertex of the face incident with \(v_iv_{i+1}\).

These four vertices are distinct. Equality of consecutive \(w_i\)'s would make their common boundary corner have degree three. Equality of opposite \(w_i\)'s would produce an internal vertex adjacent to all four boundary vertices.

Because \(v_i\) has degree four, its two internal neighbors are exactly \(w_{i-1},w_i\), and the edge \(w_{i-1}w_i\) is present. The eight faces incident with the boundary therefore form an annulus, whose inner boundary is
\[
W=w_0w_1w_2w_3w_0.
\]

The cycle \(W\) has no chord. A chord would split it into two triangles, both facial. The two vertices not incident with the chord would then have degree four in \(P\), a contradiction.

Let \(Q\) be the disk bounded by \(W\). All its internal vertices retain their degrees, so \(Q\) is admissible.

Now give \(v_0,v_1,v_2,v_3\) four distinct colors. The vertices \(w_i,w_{i+2}\) cannot have the same color: together their boundary neighbors use all four colors. Adjacent \(w_i\)'s are joined by edges. Thus every extension makes \(W\) rainbow.

Conversely, a compatible rainbow assignment on \(W\) is obtained by assigning \(w_i\) the color of \(v_{i+2}\). If \(Q\) admits a rainbow-boundary coloring, a global color permutation supplies precisely this assignment, which extends across the annulus. ∎

In fact, if \(D(P)\) denotes the number of extensions of one fixed rainbow boundary assignment, the proof gives
\[
D(P)=2D(Q),
\tag{3.1}
\]
because there are exactly two compatible rainbow assignments on \(W\).

# 4. A smallest counterexample has at least seven units of internal curvature

Assume a counterexample exists, and choose a nonextendable admissible disk \(P\) with as few vertices as possible.

By Lemma 3.2, at most one boundary vertex has degree three.

- If one boundary vertex has degree three, its two boundary neighbors have degree at least five by Lemma 3.1, and the opposite boundary vertex has degree at least four. Therefore
  \[
  \sum_{v\in B}d_P(v)\ge 3+5+4+5=17.
  \]

- If no boundary vertex has degree three, all four degrees are at least four. Equality in
  \[
  \sum_{v\in B}d_P(v)\ge16
  \]
  would mean that all four degrees are four, contrary to minimality and Lemma 3.3.

Thus, in every case,
\[
\boxed{\sum_{v\in B}d_P(v)\ge17.}
\tag{4.1}
\]

Let \(N\) be the number of internal vertices. Euler's formula gives
\[
|E(P)|=3N+5.
\]
Consequently,
\[
\sum_{z\text{ internal}}(6-d_P(z))
=\sum_{v\in B}d_P(v)-10.
\tag{4.2}
\]
Since internal degrees are at least five, the left-hand side is
\[
n_5-h,
\qquad
h=\sum_{\substack{z\text{ internal}\\d_P(z)\ge7}}(d_P(z)-6).
\]
Combining (4.1) and (4.2) proves
\[
\boxed{n_5\ge7+h.}
\tag{4.3}
\]

This is a structural restriction, not an improvement on the supplied computational lower bound on the total number of vertices.

There is also a precise description of the equality case.

## Corollary 4.1

If a vertex-minimal counterexample has exactly seven internal degree-five vertices, then:

- every other internal vertex has degree six;
- up to cyclic order and reversal, its boundary-degree sequence is one of
  \[
  (5,4,4,4)
  \quad\text{or}\quad
  (5,3,5,4).
  \]

### Proof

Equation (4.3) forces \(h=0\), and (4.2) then forces boundary-degree sum \(17\). The boundary restrictions established above give exactly the two listed possibilities. ∎

# 5. An exact identity for boundary-coloring counts

The following identity applies to every triangulated disk with outer boundary \(abcd\); the internal minimum-degree assumption is unnecessary.

Represent the four colors by
\[
\mathbb F_2^2=\{0,\alpha,\beta,\gamma\},
\qquad \alpha+\beta=\gamma.
\]
Let \(A,B,C,D\) count extensions of the following fixed boundary assignments:

\[
\begin{array}{c|cccc}
 &a&b&c&d\\ \hline
A&0&\alpha&0&\alpha\\
B&0&\alpha&0&\beta\\
C&0&\alpha&\gamma&\alpha\\
D&0&\alpha&\gamma&\beta
\end{array}
\]

Thus \(A\) is the two-color boundary pattern, \(B,C\) are the two three-color patterns, and \(D\) is the rainbow pattern.

## Proposition 5.1

\[
\boxed{A+D=B+C.}
\tag{5.1}
\]

### Proof

Give each primal edge \(rs\) the label
\[
c(r)+c(s).
\]
The three labels around every triangular face are \(\alpha,\beta,\gamma\). Passing to the disk dual gives a proper 3-edge-coloring of a cubic graph with four dangling boundary edges.

Conversely, such a dual edge-coloring integrates to a primal vertex-coloring once \(c(a)=0\) is fixed: the sum of the edge labels around each triangular face is zero, and the bounded face boundaries generate the cycle space.

In boundary order, the four dangling-edge labels for the four patterns are
\[
\begin{array}{c|cccc}
A&\alpha&\alpha&\alpha&\alpha\\
B&\alpha&\alpha&\beta&\beta\\
C&\alpha&\beta&\beta&\alpha\\
D&\alpha&\beta&\alpha&\beta .
\end{array}
\]

The subgraph using colors \(\alpha,\beta\) consists of cycles and two paths ending at the four boundary terminals. Planarity allows only the pairings
\[
\mathsf P=(12)(34),
\qquad
\mathsf Q=(14)(23).
\]
Subscript a coloring count by its pairing.

Interchanging \(\alpha,\beta\) on a specified terminal-to-terminal path preserves the pairing and gives the following bijections:

\[
\begin{array}{c|c}
\text{Bijection}&\text{Path switched}\\ \hline
A_{\mathsf P}\leftrightarrow B_{\mathsf P}&34\\
A_{\mathsf Q}\leftrightarrow C_{\mathsf Q}&23\\
D_{\mathsf P}\leftrightarrow C_{\mathsf P}&34\\
D_{\mathsf Q}\leftrightarrow B_{\mathsf Q}&23 .
\end{array}
\]
Adding these equalities proves (5.1). ∎

The Four Color Theorem applied after adding either boundary diagonal gives
\[
B+D>0,\qquad C+D>0.
\]
Hence a nonextendable rainbow boundary satisfies
\[
\boxed{D=0,\qquad A=B+C,\qquad B,C>0.}
\tag{5.2}
\]

This is an exact counting constraint rather than just a necessary Kempe-path condition. I do not know how to combine it with the degree assumptions to force \(D>0\).

# 6. A sharp family: one degree-four vertex at unbounded distance

Here is an explicit family showing that neither “at least two internal degree-four vertices” nor “an internal degree-four vertex within bounded distance of the crossing” can replace the conjectured conclusion.

Fix \(k\ge1\). Take disjoint 4-cycles
\[
R_i=v_{i,0}v_{i,1}v_{i,2}v_{i,3}v_{i,0},
\qquad 0\le i\le k,
\]
and a vertex \(z\).

Construct a plane disk \(P_k\) as follows:

- join \(z\) to all four vertices of \(R_0\);
- for \(1\le i\le k\), join each inner vertex \(v_{i-1,j}\) to
  \[
  v_{i,j}\quad\text{and}\quad v_{i,j+1},
  \]
  with indices modulo four;
- use \(R_k\) as the outer boundary.

Each annulus between consecutive rings is triangulated. Let
\[
T_k=P_k+v_{k,0}v_{k,2},
\]
adding the diagonal in the outer face, and then let
\[
G_k=T_k+v_{k,1}v_{k,3}.
\]

## Proposition 6.1

For every \(k\ge1\):

1. \(T_k\) is a 4-connected plane triangulation, so \(G_k\in\mathcal C_0\).
2. \(\chi(G_k)=5\).
3. \(z\) is the unique degree-four vertex of \(G_k\).
4. The distance from \(z\) to the external vertex set \(V(R_k)\) is \(k+1\).

### Proof

**Membership in \(\mathcal C_0\).**  
Every triangle of \(P_k\) is one of the displayed faces: either a triangle incident with \(z\), or one of the two types of annular triangles. Adding \(v_{k,0}v_{k,2}\) creates just the two outer triangular faces. No vertex of \(R_{k-1}\) is adjacent to both endpoints of that diagonal.

Thus \(T_k\) is a simple plane triangulation without a separating triangle. Since it has \(4k+5\ge9\) vertices, it is 4-connected.

**Non-4-colorability.**  
In \(G_k\), the outer ring together with its two diagonals is \(K_4\), so \(R_k\) must be rainbow in any 4-coloring.

Suppose \(R_i\) is rainbow. Opposite vertices of \(R_{i-1}\) have, between them, neighbors of all four colors on \(R_i\); therefore they cannot receive the same color. Adjacent vertices of \(R_{i-1}\) are joined by edges. Hence \(R_{i-1}\) is rainbow as well.

Inductively \(R_0\) is rainbow, leaving no color for \(z\).

Conversely, four colors suffice for all rings: starting from a rainbow outer ring, assign each inner vertex the color of the outer vertex two positions ahead. Assign a fifth color to \(z\). Therefore \(\chi(G_k)=5\).

**Degrees.**  
The degrees in \(G_k\) are
\[
d(z)=4,
\]
\[
d(v_{0,j})=5,
\]
\[
d(v_{i,j})=6\quad(1\le i<k),
\]
and
\[
d(v_{k,j})=5.
\]
Thus \(z\) is the unique degree-four vertex, and it is internal.

**Distance.**  
Every edge changes the ring index by at most one, and \(z\) is adjacent only to \(R_0\). There are radial paths achieving the resulting lower bound, so
\[
\operatorname{dist}_{G_k}(z,V(R_k))=k+1.
\]
∎

These graphs have \(4k+5\) vertices and exactly one crossing in the prescribed drawing. They satisfy, rather than refute, the conjecture.

They also explain why the square-collar reduction is necessary: an obstruction can be surrounded by arbitrarily many degree-six layers without bringing its degree-four vertex any closer to the crossing.

# 7. Remaining gap

After the reductions, a smallest hypothetical counterexample still has to satisfy all of the following:

- its boundary is a chordless 4-cycle;
- it has no separating triangle;
- every internal degree is at least five;
- at most one boundary vertex has degree three;
- if a degree-three boundary vertex exists, both its boundary neighbors have degree at least five;
- its boundary-degree sum is at least \(17\);
- its internal degrees satisfy
  \[
  n_5-\sum_{d(z)\ge7}(d(z)-6)\ge7;
  \]
- its extension counts satisfy \(D=0\) and \(A=B+C>0\).

No argument above excludes these remaining configurations. In particular, I cannot rule out the boundary-degree patterns
\[
(5,4,4,4),\qquad (5,3,5,4)
\]
with internal degrees five and six.

The missing step remains a genuinely global coloring argument: proving that every admissible disk has \(D>0\). The reductions and identities sharpen the obstruction, but do not establish that assertion.