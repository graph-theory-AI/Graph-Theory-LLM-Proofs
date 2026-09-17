Attack the following open graph-theory problem.

Catalog id: counting_3_colorings_of_the_hex_lattice
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/counting_3_colorings_of_the_hex_lattice/
Original entry: http://www.openproblemgarden.org/op/counting_3_colorings_of_the_hex_lattice
Problem attributed to: Thomassen, Carsten (posted 2008-07-05)

=== Problem statement (OpenProblemGarden) ===
Title: Counting 3-colorings of the hex lattice
Problem Find $ \lim_{n \rightarrow \infty} (\chi( H_n , 3)) ^{ 1 / |V(H_n)| } $ .

=== Discussion / context (OpenProblemGarden) ===
We'll begin by putting in place the necessary notation. Let $ {\mathcal T} $ be the regular triangular tiling of the plane. For every $ n \ge 1 $ there is a regular map which triangulates the torus, denoted $ T_n $ , which may be obtained from a regular hexagonal piece of $ {\mathcal T} $ of side-length $ n $ by identifying points on opposite edges of this hexagon. Let $ H_n $ be the dual of $ T_n $ (on the torus). Then $ H_n $ is a regular map on the torus - a hexagonal tiling. One last definition: for any graph $ G $ and any positive integer $ k $ we let $ \chi(G,k) $ denote the number of proper $ k $ -coloring of $ G $ . A famous theorem of Lieb [L] shows that $ \lim_{n \rightarrow \infty} (\chi(Q_n,3))^{1 / |V(Q_n)|} = (\frac{4}{3})^{3/2} $ where $ Q_n $ denotes the $ n \times n $ quadrangulation of the torus. This theorem is usually stated in terms of Eulerian orientations, and is of interest to physicists as the constant $ (\frac{4}{3})^{3/2} $ (called Lieb's Ice Constant) determines the "residual entropy for square ice". Thomassen proved that every planar graph $ G $ with girth $ \ge 5 $ has exponentially many proper 3-colorings. More precisely, he showed that $ (\chi(G,3))^{ 1 / |V(G)| } \ge 2 ^{1 / 10000} $ . This gives a lower bound on the limit in the above problem (assuming it exists).

=== References listed by OpenProblemGarden ===
- [L] E. H. Lieb, Exact Solution of the Problem of the Entropy of Two-Dimensional Ice. Phys. Rev. Lett. 18, 692-694, 1967.

=== Catalog page (statement + literature review) ===
Counting 3-colorings of the hex lattice — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem asks for the exact value of $\lim_{n\to\infty}(\chi(H_n,3))^{1/|V(H_n)|}$ for proper vertex 3-colorings of the hexagonal tiling $H_n$ of the torus, the analogue of Lieb's ice-constant theorem for the square lattice. No post-2008 rigorous mathematical proof establishing the existence or value of this limit has been found; the physics literature contains closely related entropy calculations (Baxter 1970 for bond/edge colorings of the hexagonal lattice, giving $W\approx 1.2087$), but the vertex-coloring version appears to remain open as a mathematical theorem. A 2016 physics paper by Cépas studies structural properties of these vertex colorings (even/odd chirality classes), confirming equal entropy for the two classes but not proving the per-site limit.

 Cited literature (1)

 
 
 
partial Colorings of odd or even chirality on hexagonal lattices
 (2017)
 

 
 O. Cépas · Physical Review B · arXiv:1611.02925

Shows that even and odd chirality classes of vertex 3-colorings of the hexagonal lattice have the same entropy in the thermodynamic limit, and introduces an ergodic Monte Carlo algorithm for sampling them; does not prove the per-site limit asked by the problem.
 

 

 Reviewer notes. Baxter's 1970 paper 'Colorings of a Hexagonal Lattice' (J. Math. Phys. 11:784) is behind a paywall and could not be fully verified; search results indicate it computes entropy for bond (edge) 3-colorings of the hexagonal lattice (W≈1.2087 = √3·Γ(1/3)^{3/2}/(2π)), which is a different problem from the vertex 3-colorings asked here. The OPG problem formulation explicitly presents the hexagonal case as open (in contrast to Lieb's proved square-lattice result), suggesting no pre-2008 rigorous mathematical proof existed for vertex colorings. The paper arXiv:0805.0669 (submitted May 2008) studies functional equations for the three-coloring statistical model with domain wall boundary conditions, extending Baxter's toroidal calculation, but without explicit chromatic-polynomial asymptotics. No post-2008 paper proving the limit was found in four search passes.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Problem. Find $ \lim_{n \rightarrow \infty} (\chi( H_n , 3)) ^{ 1 / |V(H_n)| } $ .

Keywords:
coloring · Lieb's Ice Constant · tiling · torus

Discussion

We'll begin by putting in place the necessary notation. Let $ {\mathcal T} $ be the regular triangular tiling of the plane. For every $ n \ge 1 $ there is a regular map which triangulates the torus, denoted $ T_n $ , which may be obtained from a regular hexagonal piece of $ {\mathcal T} $ of side-length $ n $ by identifying points on opposite edges of this hexagon. Let $ H_n $ be the dual of $ T_n $ (on the torus). Then $ H_n $ is a regular map on the torus - a hexagonal tiling. One last definition: for any graph $ G $ and any positive integer $ k $ we let $ \chi(G,k) $ denote the number of proper $ k $ -coloring of $ G $ . A famous theorem of Lieb [L] shows that $ \lim_{n \rightarrow \infty} (\chi(Q_n,3))^{1 / |V(Q_n)|} = (\frac{4}{3})^{3/2} $ where $ Q_n $ denotes the $ n \times n $ quadrangulation of the torus. This theorem is usually stated in terms of Eulerian orientations, and is of interest to physicists as the constant $ (\frac{4}{3})^{3/2} $ (called Lieb's Ice Constant) determines the "residual entropy for square ice". Thomassen proved that every planar graph $ G $ with girth $ \ge 5 $ has exponentially many proper 3-colorings. More precisely, he showed that $ (\chi(G,3))^{ 1 / |V(G)| } \ge 2 ^{1 / 10000} $ . This gives a lower bound on the limit in the above problem (assuming it exists).

Bibliography

 [L]
 E. H. Lieb, Exact Solution of the Problem of the Entropy of Two-Dimensional Ice. Phys. Rev. Lett. 18, 692-694, 1967.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The limit exists and is effectively approximable, with √11/2 ≤ W ≤ √(1+2 cos(π/9)), but its exact value is not obtained.",
  "would_publish": false,
  "caveats": "No exact evaluation or claim of novelty; the literature status of these partial results has not been verified."
}
```

## Partial result

Write \(Z(G)=\chi(G,3)\). I prove that the limit in the question exists. Denoting it by \(W\), I also obtain the explicit bounds
\[
\boxed{\frac{\sqrt{11}}2\ \leq\ W\ \leq\
\sqrt{1+2\cos(\pi/9)}}
\]
or numerically
\[
1.658312395\ldots\ \leq W\leq 1.696875140\ldots.
\]

In addition, I give a fully specified finite-enumeration procedure producing certified upper and lower bounds whose logarithmic gap is \(O(1/m)\).

These are partial results, not an exact evaluation of \(W\). In particular, I do not assert that either endpoint above is the answer.

## 1. An extension lemma

The following elementary fact is useful because the honeycomb lattice is bipartite and has maximum degree three.

**Lemma.** Let \(G\) be a finite bipartite graph of maximum degree at most three, and let \(S\subseteq V(G)\). If every component of \(G-S\) contains a cycle, then every proper 3-coloring of \(G[S]\) extends to \(G\).

**Proof.** Treat the components of \(G-S\) separately. In one such component, choose a shortest cycle \(C\). It is induced and even.

Color the vertices outside \(C\) in decreasing order of their distance from \(C\). Each vertex being colored has a neighbor closer to \(C\) which is still uncolored. It therefore has at most two already-colored neighbors, including neighbors in \(S\), and can be colored.

Each vertex of \(C\) now has a list of at least two available colors: its two cycle neighbors are still uncolored. An even cycle is colorable from arbitrary lists of size at least two. To see this, reduce each list to size two. If all lists agree, alternate their two colors. Otherwise, choose adjacent vertices with different lists, color the first with a color absent from the second's list, and greedily color around the cycle, ending at the second vertex. At the last step only one color in its list is forbidden.

This extends the coloring on every component. \(\square\)

## 2. Coordinates and existence of the limit

### 2.1 The particular tori in the question

Let \(e_1,e_2\) be the standard coordinate vectors of \(\mathbb Z^2\), corresponding geometrically to two directions at angle \(60^\circ\). Represent the infinite honeycomb graph by vertices
\[
b_x,w_x\qquad (x\in\mathbb Z^2)
\]
and edges
\[
b_xw_x,\qquad b_xw_{x-e_1},\qquad b_xw_{x-e_2}.
\]

Set
\[
u=e_1+e_2,\qquad v=2e_1-e_2.
\]
The opposite-side translations of the regular hexagon of side length \(n\) generate
\[
\Lambda_n=\langle nu,nv\rangle.
\]
Consequently, \(H_n\) is the quotient of the graph above by \(\Lambda_n\). Since
\[
|\det(u,v)|=3,
\]
we have
\[
|V(H_n)|=6n^2.
\]

Partition the infinite graph into six-vertex cells
\[
C_{a,b}
 =\{b_{au+bv+re_1},w_{au+bv+re_1}:r=0,1,2\}.
\]
Abbreviate these vertices as \(b_{a,b,r},w_{a,b,r}\). Within each cell the edges form the path
\[
b_0-w_0-b_1-w_1-b_2-w_2.
\]
The edges between different cells are exactly
\[
\begin{aligned}
&b_{a,b,0}w_{a-1,b-1,2},\\
&b_{a,b,r}w_{a-1,b,r+1}\qquad(r=0,1),\\
&b_{a,b,2}w_{a,b+1,0}.
\end{aligned}
\]
In particular, contracting each cell gives a graph containing the ordinary horizontal and vertical grid edges.

Let \(B_m\) be the induced graph consisting of the cells
\[
C_{a,b},\qquad 0\leq a,b<m.
\]
Thus \(|V(B_m)|=6m^2\).

### 2.2 Free-boundary entropy

Put
\[
a_m=\frac{\log Z(B_m)}{6m^2}.
\]
For fixed \(m\), partition the cell square defining \(B_N\) into
\(\lfloor N/m\rfloor^2\) complete \(m\times m\) squares and the remaining cells. Deleting edges between pieces gives
\[
Z(B_N)\leq
Z(B_m)^{\lfloor N/m\rfloor^2}
3^{\,6(N^2-m^2\lfloor N/m\rfloor^2)}.
\]
Hence
\[
\limsup_{N\to\infty}a_N\leq a_m
\]
for every \(m\). Since every \(a_N\) is at least \(\inf_m a_m\), it follows that
\[
\boxed{\lim_{m\to\infty}a_m
=\alpha:=\inf_{m\geq1}a_m.}
\]

### 2.3 Comparing free and toroidal boundaries

The graph \(H_n\), with cell indices interpreted modulo \(n\), is obtained from \(B_n\) by adding wrap-around edges. Therefore
\[
Z(H_n)\leq Z(B_n).
\]

For the reverse comparison, retain only the cells
\[
1\leq a,b\leq n-2.
\]
Their induced graph is a translate of \(B_{n-2}\). The uncolored cells form the frame
\[
a\in\{0,n-1\}\quad\text{or}\quad b\in\{0,n-1\}.
\]
This frame is connected. It contains a cycle: two adjacent cells \(C_{0,0},C_{1,0}\), their internal paths, and the two edges between them contain a 6-cycle. Thus, for all sufficiently large \(n\), the extension lemma applies to every coloring of the retained graph.

We obtain
\[
\boxed{Z(B_{n-2})\leq Z(H_n)\leq Z(B_n).}
\]
After taking logarithms and dividing by \(6n^2\), both bounds tend to \(\alpha\). Thus
\[
\boxed{\lim_{n\to\infty}Z(H_n)^{1/(6n^2)}=e^\alpha.}
\]

This proves existence for the specific hexagonal fundamental domains in the question, not merely for a convenient subsequence of rectangular tori.

## 3. Certified finite-volume approximation

There is also an effective converse to the upper bound \(\alpha\leq a_m\).

Take \(N=k(m+1)\). In the cell torus of side \(N\), retain \(k^2\) disjoint \(m\times m\) cell squares, leaving every \((m+1)\)-st cell row and column uncolored. Distinct retained squares have no edges between them. The uncolored grid of cells is connected and contains a cycle.

The extension lemma therefore shows that all independent choices of colorings of the retained squares extend:
\[
Z(H_N)\geq Z(B_m)^{k^2}.
\]
Letting \(k\to\infty\) gives
\[
\boxed{
Z(B_m)^{1/[6(m+1)^2]}
\leq W\leq
Z(B_m)^{1/(6m^2)}.}
\]

The logarithmic gap between these two bounds is at most
\[
\frac{(2m+1)\log 3}{(m+1)^2},
\]
because \(Z(B_m)\leq 3^{6m^2}\).

This is a certified approximation algorithm: construct \(B_m\) using the explicit edge list above and enumerate its \(3^{6m^2}\) color assignments, counting precisely those satisfying every edge constraint. The two displayed powers then bracket \(W\), with an explicit error guarantee. This is computationally expensive, but requires no unproved convergence assumption. I have not run this enumeration here.

## 4. A symmetric transfer matrix with the same entropy

To obtain explicit bounds, use the brick-wall representation of the honeycomb lattice. Its vertices are \((i,j)\in\mathbb Z^2\), with all vertical edges and with horizontal edges
\[
(i,j)(i+1,j)\quad\text{when }i+j\text{ is even}.
\]
An explicit isomorphism from the preceding coordinates is
\[
b_{p,q}\mapsto(p+q,q-p),\qquad
w_{p,q}\mapsto(p+q+1,q-p).
\]

For even \(L,M\), let \(F_{L,M}\) be the induced \(L\times M\) rectangle and let \(R_{L,M}\) be its periodic version.

### Equality of the relevant entropies

Here are the boundary comparisons needed below.

* For fixed even \(L,M\), copies of \(F_{L,M}\) tile the infinite vertex set by graph-preserving translations. Packing complete such copies into \(B_N\), and discarding edges between pieces, gives
  \[
  \alpha\leq \frac{\log Z(F_{L,M})}{LM}.
  \]
  The uncovered portion has \(O_{L,M}(N)\) vertices.

* Conversely, for fixed \(m\), packing translated \(B_m\)'s into \(F_{L,M}\) leaves \(O_m(L+M)\) vertices. It follows that
  \[
  \lim_{\substack{\min(L,M)\to\infty\\L,M\text{ even}}}
  \frac{\log Z(F_{L,M})}{LM}=\alpha.
  \]

* In \(R_{L,M}\), delete a boundary frame of width two. Its complement is a translated \(F_{L-4,M-4}\). The frame is connected and contains the cycle formed by the first two brick-wall rows, of length \(2L\). The extension lemma gives
  \[
  Z(F_{L-4,M-4})\leq Z(R_{L,M})\leq Z(F_{L,M}).
  \]

Consequently,
\[
\lim_{\substack{\min(L,M)\to\infty\\L,M\text{ even}}}
\frac{\log Z(R_{L,M})}{LM}=\alpha.
\]

### Definition of the transfer matrix

Write \(L=2m\), with all horizontal indices read modulo \(L\), and define
\[
\Omega_L=
\{a\in\{1,2,3\}^{L}:a_{2j}\ne a_{2j+1}\text{ for every }j\}.
\]
Thus \(|\Omega_L|=6^m\).

Reflection \(i\mapsto-i\) turns the matching in an even row into the matching in an odd row. Define the matrix \(T_L\), indexed by \(\Omega_L\), by
\[
(T_L)_{a,b}
=\prod_{i=0}^{L-1}\mathbf 1[a_i\ne b_{-i}].
\]
This matrix is nonnegative and symmetric. For even \(M\),
\[
Z(R_{L,M})=\operatorname{tr}(T_L^M).
\]

Let \(\lambda_L\) be its spectral radius. Since \(M\) is even,
\[
\lambda_L^M\leq\operatorname{tr}(T_L^M)
\leq 6^m\lambda_L^M.
\]
Taking \(M=L\to\infty\) in the established entropy limit yields
\[
\boxed{\lim_{m\to\infty}\lambda_{2m}^{1/(2m)}=W.}
\]

## 5. Lower bound \(W\geq\sqrt{11}/2\)

Define
\[
f(x,y)=
\begin{cases}
2,&x=y,\\
3,&x\ne y.
\end{cases}
\]
For \(a\in\Omega_{2m}\), the row sum of \(T_{2m}\) is
\[
v(a)=\prod_{j=0}^{m-1}f(a_{2j+1},a_{2j+2}).
\]
Indeed, each odd-row dimer has two possible colorings when the two vertically forbidden colors agree, and three when they differ.

Thus \(v=T_{2m}\mathbf1\). By the Rayleigh principle,
\[
\lambda_{2m}\geq\frac{v^{\mathsf T}T_{2m}v}{v^{\mathsf T}v}.
\]

### Denominator

Let \(J\) be the \(3\times3\) all-ones matrix, and put
\[
K=J-I,\qquad Q=9J-5I.
\]
The entries of \(Q\) are \(f(x,y)^2\). Therefore
\[
v^{\mathsf T}v
=\operatorname{tr}((KQ)^m).
\]
Since
\[
KQ=13J+5I,
\]
we get the exact formula
\[
v^{\mathsf T}v=44^m+2\cdot5^m.
\]

### Numerator

Use the six states \((x,y)\) with \(x\ne y\), and define
\[
\begin{aligned}
A_{(x,y),(x',y')}&=K_{x,x'}f(y,y'),\\
B_{(x,y),(x',y')}&=f(x,x')K_{y,y'}.
\end{aligned}
\]
Expanding the two reflected rows column by column gives
\[
v^{\mathsf T}T_{2m}v=\operatorname{tr}((AB)^m).
\]

Every row of \(A\) and every row of \(B\) sums to \(11\). For example, the three possibilities for \(y'\), relative to a fixed distinct pair \((x,y)\), contribute \(2,6,3\). Also, \(AB\) is strictly positive. Its Perron eigenvalue is consequently \(121\), and
\[
\operatorname{tr}((AB)^m)=121^m(1+o(1)).
\]

It follows that
\[
W\geq
\lim_{m\to\infty}
\left(\frac{121^m(1+o(1))}
{44^m+2\cdot5^m}\right)^{1/(2m)}
=\sqrt{\frac{121}{44}}
=\boxed{\frac{\sqrt{11}}2}.
\]

## 6. Upper bound \(W\leq\sqrt{1+2\cos(\pi/9)}\)

This bound follows from a positive test vector and a finite collection of \(2\times2\) matrix inequalities.

Set
\[
c=1+2\cos(\pi/9),\qquad
r=1-\frac1c,\qquad t=c-2.
\]
The number \(c\) is the root in \((11/4,3)\) of
\[
c^3-3c^2+1=0.
\]
In particular, \(0<r,t<1\), and
\[
\frac{1+t}{r}=c,\qquad
1+r=(c-1)t,\qquad
r(1+r)>1.
\]

Define
\[
g(x,y)=
\begin{cases}
r,&x=y,\\
1,&x\ne y,
\end{cases}
\qquad
w(a)=\prod_{j=0}^{m-1}g(a_{2j+1},a_{2j+2}).
\]

### A two-state expansion

Fix \(a\in\Omega_{2m}\). After reflecting the second row, its color at position \(i\) has the two-element list
\[
\{1,2,3\}\setminus\{a_i\}.
\]
Group positions into even dimers. If an even dimer of \(a\) has colors \((1,2)\), order the corresponding two lists as \((2,3)\) and \((1,3)\). The soft interaction within that dimer is the matrix
\[
\mathsf M=\begin{pmatrix}1&1\\1&r\end{pmatrix}.
\]

The hard inequality across the next odd edge gives one of the following matrices:
\[
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad
D_1=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\quad
D_2=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]
\[
D_3=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad
D_4=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]
For completeness, all six possibilities for the next ordered color-pair are:

| Next pair | Hard-interaction matrix | Divisor from \(w(a)\) |
|---|---:|---:|
| \((1,2)\) | \(D_1\) | \(1\) |
| \((1,3)\) | \(D_2\) | \(1\) |
| \((2,1)\) | \(P\) | \(r\) |
| \((2,3)\) | \(I\) | \(r\) |
| \((3,1)\) | \(D_3\) | \(1\) |
| \((3,2)\) | \(D_4\) | \(1\) |

Relabeling the colors at each even dimer therefore gives
\[
\frac{(T_{2m}w)(a)}{w(a)}
=\operatorname{tr}(A_1\cdots A_m),
\]
where each \(A_j\) belongs to
\[
\mathcal A=
\left\{
\frac{\mathsf M}{r},
\frac{\mathsf MP}{r},
\mathsf MD_1,\mathsf MD_2,\mathsf MD_3,\mathsf MD_4
\right\}.
\]

### A common positive-vector bound

Let \(u=(1,t)^{\mathsf T}\). Direct calculation gives
\[
\mathsf MD_1u=cu,
\qquad
\frac{\mathsf M}{r}u\leq cu.
\]
The second inequality uses \(r(1+r)\geq1\). The remaining cases follow componentwise from
\[
\frac{\mathsf MP}{r}u\leq\frac{\mathsf M}{r}u,
\]
\[
\mathsf MD_3u\leq\mathsf MD_2u\leq\mathsf MD_1u,
\qquad
\mathsf MD_4u\leq\mathsf MD_1u,
\]
using \(0<r,t<1\). Thus
\[
Au\leq cu\qquad\text{for every }A\in\mathcal A.
\]

For any product \(R=A_1\cdots A_m\), nonnegativity gives \(Ru\leq c^m u\). Each diagonal entry of \(R\) is then at most \(c^m\), so
\[
\operatorname{tr}(R)\leq2c^m.
\]
Consequently,
\[
\frac{(T_{2m}w)(a)}{w(a)}\leq2c^m
\qquad\text{for every }a.
\]
The standard positive-vector bound for a nonnegative matrix now yields
\[
\lambda_{2m}\leq2c^m.
\]
Taking \(2m\)-th roots and passing to the limit proves
\[
\boxed{W\leq\sqrt c
=\sqrt{1+2\cos(\pi/9)}}.
\]

## What remains unresolved

The existence issue can be handled by the extension lemma and boundary comparisons above. Moreover, the finite-volume inequalities give unconditional, certified approximation of the constant.

What is missing is an **exact evaluation** of \(W\), or equivalently an exact evaluation of
\[
\lim_{m\to\infty}\lambda_{2m}^{1/(2m)}.
\]
The transfer-matrix estimates do not establish equality at either endpoint. I would therefore not present this as a resolution of the stated problem, and I make no novelty claim for these partial results without a verified literature review.
