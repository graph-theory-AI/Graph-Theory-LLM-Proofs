```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I determine the circular chromatic number exactly for the cubic planar family G(2n,2), including the dodecahedron, and verify the 20/7 bound throughout this family.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of this family calculation has not been checked."
}
```

## 1. An exact special case in the genuinely cubic regime

I do not use the previous attempt’s matching-core argument. Instead, I consider an infinite family in which **every vertex has degree three**, and which contains the dodecahedron.

For \(n\ge 4\), define \(H_n\) by
\[
V(H_n)=\{a_i,b_i,x_i,y_i:i\in\mathbb Z_n\},
\]
with edges
\[
a_i a_{i+1},\quad b_i b_{i+1},\quad
a_i x_i,\quad b_i y_i,\quad
x_i y_i,\quad y_i x_{i+1}
\qquad(i\in\mathbb Z_n).
\tag{1}
\]
This is the generalized Petersen graph usually denoted \(G(2n,2)\).

**Theorem.** For \(n\ge4\),
\[
\boxed{
\chi_c(H_n)=
\begin{cases}
\dfrac83, & n\text{ even},\\[2mm]
\dfrac{20}{7}, & n=5,\\[2mm]
\dfrac{14}{5}, & n=7,\\[2mm]
\dfrac{36}{13}, & n=9,\\[2mm]
\dfrac{11}{4}, & n\ge11\text{ odd}.
\end{cases}}
\tag{2}
\]
Consequently, every graph in this family satisfies the proposed \(20/7\) bound, with equality precisely for \(H_5\), the dodecahedral graph.

The proof below is self-contained. Its lower bounds use facial winding constraints, and its upper bounds are explicit colorings.

### The planar embedding

Draw the \(a\)-cycle, the alternating \(x,y\)-cycle, and the \(b\)-cycle on three concentric circles, with the appropriate spokes between consecutive circles. The faces are the two \(n\)-cycles and the \(2n\) pentagons
\[
\begin{aligned}
P_i&=(a_i,a_{i+1},x_{i+1},y_i,x_i),\\
Q_i&=(b_i,b_{i+1},y_{i+1},x_{i+1},y_i).
\end{aligned}
\tag{3}
\]
Thus \(H_n\) is planar and cubic, with \(4n\) vertices and \(6n\) edges.

It is triangle-free for \(n\ge4\). Indeed, a triangle meeting the \(a\)-vertices or the \(b\)-vertices would have to lie entirely in the corresponding \(n\)-cycle; the remaining vertices induce a \(2n\)-cycle.

Let \(D_n\) be the plane dual. Each \(P_i,Q_i\) has degree five. Moreover, the subgraph induced by these \(2n\) dual vertices is
\[
C_{2n}^{\,2},
\tag{4}
\]
in the cyclic order
\[
P_0,Q_0,P_1,Q_1,\ldots,P_{n-1},Q_{n-1}.
\]
Here the square of a cycle joins vertices at cyclic distance one or two. This follows directly from the face lists in (3).

---

## 2. A necessary facial inequality for circular colorings

We use two equivalent descriptions of circular coloring.

* A circular \(r\)-coloring assigns points of the unit circle to vertices so that adjacent points have circular distance at least \(1/r\).
* A \((p,q)\)-coloring assigns elements of \(\mathbb Z_p\) so that every edge difference belongs to
  \[
  \{q,q+1,\ldots,p-q\}.
  \]
  It certifies \(\chi_c(G)\le p/q\).

The following necessary condition will supply the lower bounds.

**Facial inequality.** Suppose a connected plane graph has a circular \(r\)-coloring, where \(r\ge2\), and put
\[
c=1-\frac2r.
\]
There are integers \(b_F\), one for each face, satisfying
\[
b_F\equiv |F|\pmod2,\qquad |b_F|\le c|F|,
\tag{5}
\]
\[
\sum_F b_F=0,
\tag{6}
\]
and, for every set \(S\) of faces,
\[
\left|\sum_{F\in S}b_F\right|
   \le c\,|\delta_D(S)|.
\tag{7}
\]
Face lengths count boundary edges with multiplicity.

**Proof.** For an oriented edge \(uv\), let \(d(uv)\in(0,1)\) represent the difference between the two unit-circle colors. Then
\[
\frac1r\le d(uv)\le1-\frac1r.
\]
Set
\[
t(uv)=2d(uv)-1.
\]
We have \(t(vu)=-t(uv)\) and \(|t(uv)|\le c\).

Orient each facial boundary with the face on its left, and define
\[
b_F=\sum_{uv\in\partial F}t(uv).
\]
The sum of the \(d(uv)\)'s around a closed walk is an integer. Hence
\[
b_F=2k-|F|
\]
for some integer \(k\), proving the parity assertion and (5).

Summing over all faces cancels every edge contribution, giving (6). Summing over a set of faces cancels its internal edges; only the dual cut remains. Bounding each remaining contribution by \(c\) gives (7). \(\square\)

In particular, whenever \(r<3\), every pentagonal face has
\[
b_F\in\{-1,1\},
\tag{8}
\]
because \(5c<5/3<3\) and \(b_F\) is odd.

---

## 3. Lower bounds

### 3.1. Every \(H_n\) requires at least \(8/3\)

Suppose \(H_n\) had a circular \(r\)-coloring with \(r<8/3\). Then \(c<1/4\), and all pentagonal faces have signs \(b_F=\pm1\).

The dual contains a triangle consisting of three pentagonal faces. Two of these faces have the same sign. Let \(S\) be that pair. They are adjacent and each has degree five, so
\[
|\delta_{D_n}(S)|\le 5+5-2=8.
\]
But (7) gives
\[
2=\left|\sum_{F\in S}b_F\right|
  \le 8c<2,
\]
a contradiction. Therefore
\[
\chi_c(H_n)\ge\frac83.
\tag{9}
\]

### 3.2. Odd \(n\) requires at least \(11/4\)

Suppose \(n\ge5\) is odd and \(r<11/4\). Then
\[
c<\frac3{11}.
\]
Again all pentagonal faces have signs \(\pm1\).

Three connected pentagonal faces of the same sign would form a set \(S\) with at least two internal dual edges. Therefore
\[
|\delta_{D_n}(S)|\le15-4=11,
\]
contradicting
\[
3\le c|\delta_{D_n}(S)|<3.
\]
Thus every monochromatic component in the signed graph \(C_{2n}^{\,2}\) from (4) has at most two vertices.

We now check that this is impossible when \(n\) is odd.

Consider a cyclic binary sequence describing the signs on \(C_{2n}\). No run can have length at least three. Nor can there be a singleton run: if position \(i\) has sign \(+\) and positions \(i-1,i+1\) have sign \(-\), the latter two are adjacent in the square of the cycle. Avoiding a third vertex in their monochromatic component forces both positions \(i-2,i+2\) to have sign \(+\). But then
\[
i-2,\ i,\ i+2
\]
form a connected monochromatic triple in the square.

Consequently every run has length exactly two. The number of runs on a two-colored cycle is even, so \(2n\) must be divisible by four. This contradicts odd \(n\).

Hence
\[
\chi_c(H_n)\ge\frac{11}{4}
\qquad(n\ge5\text{ odd}).
\tag{10}
\]

### 3.3. Stronger bounds for the small odd cases

Let
\[
n\in\{5,7,9,11\},
\]
and suppose
\[
r<\frac{8n}{3n-1}.
\]
Then
\[
c<\frac{n+1}{4n},
\qquad
nc<\frac{n+1}{4}\le3.
\tag{11}
\]

All faces have odd length, and their lengths are at most \(n\). Equations (5) and (11) therefore force
\[
b_F\in\{-1,1\}
\]
for **every** face, including the two \(n\)-gonal faces.

There are \(2n+2\) faces. By (6), exactly \(n+1\) have sign \(+1\). Let \(S\) be this positive set.

Because \(H_n\) is cubic, \(D_n\) is a triangulation with \(4n\) triangular faces. Every triangular face contains either zero or two edges of a given cut. Counting cut-edge incidences with dual faces gives
\[
|\delta_{D_n}(S)|\le4n.
\tag{12}
\]
Using (7),
\[
n+1=\sum_{F\in S}b_F
 \le c|\delta_{D_n}(S)|
 \le4nc<n+1,
\]
a contradiction.

Thus
\[
\chi_c(H_n)\ge\frac{8n}{3n-1}
\qquad(n=5,7,9,11).
\tag{13}
\]
For \(n=5\), this is a self-contained proof of the dodecahedral lower bound \(20/7\).

---

## 4. An explicit \(8/3\)-coloring when \(n\) is even

Use the following colors in \(\mathbb Z_8\):
\[
\begin{array}{c|rrrr}
 &a_i&b_i&x_i&y_i\\ \hline
i\text{ even}&0&4&3&7\\
i\text{ odd}&5&1&2&6
\end{array}
\tag{14}
\]
For every edge type in (1), its color difference belongs to
\[
\{3,4,5\}\pmod8.
\]
For example, \(x_i y_i\) always has difference four, while the cross-column edges \(y_i x_{i+1}\) have differences three or five. Since \(n\) is even, the same verification applies at the cyclic boundary.

This proves
\[
\chi_c(H_n)\le\frac83
\qquad(n\text{ even}),
\]
which matches (9).

---

## 5. Explicit optimal colorings for \(n=5,7,9,11\)

The next construction uses a Hamilton cycle whose remaining edges have a particularly simple pattern.

Let \(n=2k+1\ge5\), and write \(p=4n\). Construct an ordered list of vertices as follows.

1. Start with
   \[
   x_1,a_1,a_0,a_{2k},x_{2k}.
   \]
2. For \(j=k-1,k-2,\ldots,1\), append
   \[
   y_{2j+1},b_{2j+1},b_{2j},y_{2j},
   x_{2j+1},a_{2j+1},a_{2j},x_{2j}.
   \]
3. Append
   \[
   y_1,b_1,b_0,b_{2k},y_{2k},x_0,y_0,
   \]
   and close back to \(x_1\).

Every vertex appears exactly once, and every consecutive pair, including the closing pair, is an edge of \(H_n\). Denote this Hamilton cycle by
\[
v_0,v_1,\ldots,v_{p-1},v_0.
\]

The edges outside this Hamilton cycle have the following index gaps. A gap is recorded up to sign modulo \(p\).
\[
\begin{array}{c|c}
\text{edge}&\text{index gap}\\ \hline
a_0x_0,\ b_0y_0&4\\
x_1y_1,\ x_{n-1}y_{n-1}&7\\
x_i y_i,\quad 2\le i\le n-2&4\\
a_1a_2,\ b_{n-2}b_{n-1}&10\\
\text{all other unused edges of the }a\text{- and }b\text{-cycles}&7
\end{array}
\tag{15}
\]
This table follows directly from the displayed ordering and exhausts all edges outside the Hamilton cycle.

Now restrict to \(n=5,7,9,11\), and put
\[
q=\frac{3n-1}{2}.
\]
Assign
\[
f(v_i)=qi\pmod p.
\tag{16}
\]
Hamilton-cycle edges have allowed difference \(q\) or \(p-q\). For the other edges, the relevant residues are
\[
\begin{array}{c|c}
d&dq\bmod p\\ \hline
4&2n-2\\[1mm]
7&\dfrac{5n-7}{2}\\[2mm]
10&3n-5
\end{array}
\tag{17}
\]
and, for \(5\le n\le11\), all three lie in
\[
\left[q,p-q\right]
=
\left[\frac{3n-1}{2},\frac{5n+1}{2}\right].
\]
Negative index gaps are also allowed, since this interval is invariant under taking negatives modulo \(p\).

Thus (16) is a \((p,q)\)-coloring, proving
\[
\chi_c(H_n)\le\frac pq=\frac{8n}{3n-1}
\qquad(n=5,7,9,11).
\tag{18}
\]
Together with (13), this gives
\[
\chi_c(H_5)=\frac{20}{7},\quad
\chi_c(H_7)=\frac{14}{5},\quad
\chi_c(H_9)=\frac{36}{13},\quad
\chi_c(H_{11})=\frac{11}{4}.
\]

---

## 6. Extending the \(11/4\)-coloring to every larger odd \(n\)

A column state is the ordered quadruple of colors
\[
C=(a,b,x,y).
\]
It is internally valid if the three edges \(ax,by,xy\) are properly colored. An internally valid state \(C'=(a',b',x',y')\) may follow \(C\) precisely when
\[
aa',\qquad bb',\qquad yx'
\tag{19}
\]
are properly colored.

These conditions account for every edge in (1). Consequently, a valid coloring of \(H_n\) is exactly a cyclic sequence of \(n\) internally valid states satisfying (19).

Suppose two consecutive states \(C,C'\) also allow the reverse transition \(C'\to C\). Then replacing
\[
C,C'
\quad\text{by}\quad
C,C',C,C'
\tag{20}
\]
produces a coloring of \(H_{n+2}\) with the same target. The boundary transitions are unchanged.

For \(H_{11}\), construction (16) is a \((44,16)\)-coloring. Dividing its colors by four gives a \((11,4)\)-coloring. Its columns 2 and 3 have states
\[
C=(8,3,1,7),
\qquad
C'=(4,10,0,6)
\quad\text{in }\mathbb Z_{11}.
\tag{21}
\]
The forward transition is already part of the coloring. For the reverse transition, the two cap-edge conditions are automatic by symmetry. The only additional condition is the edge between \(y'=6\) and \(x=1\); its cyclic distance is five, so it is allowed in the \((11,4)\)-target.

We may therefore apply (20) repeatedly. This gives a \((11,4)\)-coloring of
\[
H_{11+2t}
\qquad\text{for every }t\ge0.
\]
Hence
\[
\chi_c(H_n)\le\frac{11}{4}
\qquad(n\ge11\text{ odd}).
\tag{22}
\]
The lower bound (10) proves equality. All cases of (2) are now covered. \(\square\)

---

## 7. What this does—and does not—settle

This establishes the conjectured bound for an infinite family of triangle-free **cubic planar** graphs, rather than only for graphs whose degree-three vertices are sparsely adjacent. It also independently verifies the extremal value for the dodecahedron.

The gap to the original problem is substantial. The upper-bound construction uses the specific four-vertex column structure of \(H_n\), and the initial odd colorings use a Hamilton cycle with chord gaps restricted to \(4,7,10\). An arbitrary triangle-free subcubic planar graph need not have either structure.

The facial inequality is a useful general obstruction, but it supplies necessary conditions, not a general coloring construction. No argument above proves that every graph in the original class has a \((20,7)\)-coloring, and no counterexample is produced. I also make no claim that the exact family calculation is new in the literature.