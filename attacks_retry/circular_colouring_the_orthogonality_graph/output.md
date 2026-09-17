```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A geometric odd-walk lemma excludes every homomorphism from O to a finite locally bipartite graph, and consequently proves χ_c(O)=4.",
  "would_publish": true,
  "caveats": "Literature priority has not been checked; the argument below is self-contained."
}
```

# Circular chromatic number of the orthogonality graph

Let \(\mathcal O\) be the graph whose vertices are the one-dimensional subspaces of \(\mathbb R^3\), with adjacency given by orthogonality.

We prove the following stronger statement.

**Theorem.** There is no homomorphism from \(\mathcal O\) to a finite graph in which every open neighborhood induces a bipartite graph. Consequently,
\[
\boxed{\chi_c(\mathcal O)=4.}
\]

The key geometric fact is that the union of the neighborhoods of three linearly independent directions always contains an odd closed walk.

## 1. The geometric odd-walk lemma

For a nonzero vector \(a\), write
\[
P_a=a^\perp,\qquad J_a(x)=a\times x.
\]
Thus \(J_a(x)\), when nonzero, represents a line perpendicular to \([x]\) and belonging to \(P_a\).

**Lemma.** Let \(a,b,c\in\mathbb R^3\) be linearly independent. The subgraph of \(\mathcal O\) induced by all lines contained in
\[
P_a\cup P_b\cup P_c
\]
is not bipartite.

**Proof.** First suppose that two of the normals, say \(a,b\), are perpendicular. Then
\[
[a],\quad [b],\quad [a\times b]
\]
form a triangle, and all three belong to the specified union. This covers that case.

We may therefore assume that \(a,b,c\) are pairwise nonorthogonal. Normalize them to unit vectors and choose their signs and an orthonormal coordinate system so that
\[
a=(0,0,1),\qquad b=(s,0,t),\qquad c=(u,v,w),
\]
where
\[
s>0,\qquad 0<t<1,\qquad s^2+t^2=1.
\]
Linear independence and pairwise nonorthogonality give
\[
v\ne0,\qquad w\ne0,\qquad su+tw\ne0. \tag{1}
\]

We will construct walks using successive cross products. All the cross products involved are nonzero: whenever \(d\cdot e\ne0\), the restriction
\[
J_d:P_e\longrightarrow P_d
\]
is injective, because the kernel of \(J_d\) is \(\mathbb R d\), which does not meet \(P_e\) nontrivially. This applies to every transition below.

Identify \(P_a\) with \(\mathbb R^2\) using \((x,y,0)\leftrightarrow(x,y)\). Consider the two operators on \(P_a\)
\[
E=J_a^2J_b^2,\qquad F=J_aJ_cJ_b.
\]
Direct calculation gives
\[
E=
\begin{pmatrix}
t^2&0\\
0&1
\end{pmatrix},
\qquad
F=
\begin{pmatrix}
0&su+tw\\
-tw&sv
\end{pmatrix}. \tag{2}
\]

These operators have a walk interpretation:

- \(F\) is a three-edge walk, with successive planes
  \[
  P_a\ \xrightarrow{J_b}\ P_b\
  \xrightarrow{J_c}\ P_c\
  \xrightarrow{J_a}\ P_a.
  \]
- \(E\) is a four-edge walk, with successive planes
  \[
  P_a\ \xrightarrow{J_b}\ P_b\
  \xrightarrow{J_b}\ P_b\
  \xrightarrow{J_a}\ P_a\
  \xrightarrow{J_a}\ P_a.
  \]

For \(n\ge0\),
\[
E^nF=
\begin{pmatrix}
0&t^{2n}(su+tw)\\
-tw&sv
\end{pmatrix}.
\]
Its characteristic polynomial has discriminant
\[
\Delta_n
=(sv)^2-4t^{2n}tw(su+tw). \tag{3}
\]
Because \(0<t<1\) and \(sv\ne0\),
\[
\Delta_n\longrightarrow (sv)^2>0.
\]
Choose \(n\ge0\) with \(\Delta_n>0\). Then \(E^nF\) has a real eigenvector \(x_0\ne0\). Moreover, (1) shows that \(E^nF\) is invertible, so its corresponding eigenvalue \(\lambda\) is nonzero:
\[
E^nF(x_0)=\lambda x_0.
\]

Start at the line \([x_0]\), perform the three cross-product steps defining \(F\), and then perform \(n\) copies of the four steps defining \(E\). Every step joins perpendicular lines, every intermediate vector is nonzero, and every line lies in \(P_a\cup P_b\cup P_c\). The final line is
\[
[E^nF(x_0)]=[\lambda x_0]=[x_0].
\]
We have therefore obtained a closed walk of odd length
\[
3+4n.
\]
A bipartite graph cannot have an odd closed walk. This proves the lemma. \(\square\)

A useful reformulation is the following. For \(S\subseteq V(\mathcal O)\), let
\[
N_{\mathcal O}(S)=\bigcup_{L\in S}N_{\mathcal O}(L).
\]

**Corollary.** If \(\mathcal O[N_{\mathcal O}(S)]\) is bipartite, then the lines in \(S\) span a vector subspace of dimension at most \(2\).

Indeed, otherwise \(S\) contains three linearly independent directions, and the lemma supplies an odd closed walk inside \(N_{\mathcal O}(S)\).

## 2. No finite locally bipartite target

Call a graph *locally bipartite* if every open neighborhood induces a bipartite graph.

Suppose, for a contradiction, that
\[
h:\mathcal O\longrightarrow H
\]
is a homomorphism to a finite locally bipartite graph \(H\).

For any \(\alpha\in V(H)\), put
\[
S_\alpha=h^{-1}(\alpha).
\]
Every vertex of \(N_{\mathcal O}(S_\alpha)\) is mapped into \(N_H(\alpha)\). Consequently,
\[
\mathcal O[N_{\mathcal O}(S_\alpha)]
\longrightarrow H[N_H(\alpha)].
\]
The graph on the right is bipartite, so the graph on the left is bipartite as well. By the corollary, every fiber \(S_\alpha\) spans a subspace of dimension at most \(2\).

These finitely many fibers cannot cover all projective directions. Here is an explicit pigeonhole argument. If \(m=|V(H)|\), consider the \(2m+1\) lines
\[
L_j=[(1,j,j^2)],\qquad 1\le j\le 2m+1.
\]
Some three have the same image under \(h\). But any three distinct such lines are linearly independent, since
\[
\det
\begin{pmatrix}
1&i&i^2\\
1&j&j^2\\
1&k&k^2
\end{pmatrix}
=(j-i)(k-i)(k-j)\ne0.
\]
This contradicts the dimension bound on that fiber.

Thus \(\mathcal O\) has no homomorphism to a finite locally bipartite graph.

## 3. Circular colorings below \(4\) have locally bipartite targets

For positive integers \(p,q\) with \(p\ge2q\), let \(K_{p/q}\) be the circular clique on \(\mathbb Z_p\), with adjacency defined by
\[
a\sim b
\quad\Longleftrightarrow\quad
q\le (b-a\bmod p)\le p-q.
\]

**Lemma.** If \(p<4q\), then \(K_{p/q}\) is locally bipartite.

**Proof.** By translation symmetry, it is enough to consider the neighborhood of \(0\):
\[
N(0)=\{q,q+1,\ldots,p-q\}.
\]
Partition it into
\[
A=N(0)\cap\{q,\ldots,2q-1\},
\qquad
B=N(0)\cap\{2q,\ldots,3q-1\}.
\]
These sets cover \(N(0)\), because \(p-q<3q\). Each lies in a block of \(q\) consecutive colors, and such a block is independent in \(K_{p/q}\). Thus \(A,B\) are a bipartition of the neighborhood. \(\square\)

It follows from Section 2 that
\[
\mathcal O\nrightarrow K_{p/q}
\qquad\text{whenever }p/q<4.
\]
Using the finite-palette definition of circular chromatic number, this already proves
\[
\chi_c(\mathcal O)\ge4. \tag{4}
\]

For completeness, the conclusion is unchanged if circular chromatic number for infinite graphs is defined using real-circle colorings. Suppose a circular \(r\)-coloring exists for some \(r<4\). Choose a rational number
\[
r<R<4
\]
and scale the coloring to circumference \(R\). Every edge then has circular distance at least \(R/r>1\). Write \(R=p/q\), choosing a sufficiently large common multiple of its numerator and denominator that
\[
\frac{2}{q}<\frac Rr-1.
\]
Rounding every color to the grid of spacing \(1/q\) changes each color by less than \(1/q\), so every edge still has circular distance at least \(1\). This gives a homomorphism to the finite graph \(K_{p/q}\), a contradiction. The rounding estimate is uniform and therefore applies to infinitely many vertices.

## 4. A proper four-coloring, including boundary directions

Here is an explicit four-coloring to establish the upper bound without leaving boundary choices implicit.

For every line choose its unit representative \(u=(x,y,z)\) according to the rule:

- choose \(z>0\), if possible;
- if \(z=0\), choose \(y>0\), if possible;
- if \(z=y=0\), choose \(x>0\).

Except for the line \([e_3]\), the planar projection \((x,y)\) is nonzero. Color such a line by the half-open quadrant containing \((x,y)\), using the argument intervals
\[
[0,\pi/2),\quad [\pi/2,\pi),\quad
[\pi,3\pi/2),\quad [3\pi/2,2\pi).
\]
Give \([e_3]\) the third color.

Two nonzero planar vectors in the same half-open quadrant have strictly positive inner product. Since all selected representatives satisfy \(z\ge0\), two non-pole lines of the same color have
\[
u\cdot v
=(x,y)\cdot(x',y')+zz'>0.
\]
Thus they are not perpendicular.

The selected representatives of equatorial lines have arguments in \([0,\pi)\), so no equatorial line has the third color. Every other line of the third color has \(z>0\) and hence is not perpendicular to \(e_3\). Therefore the coloring is proper, and
\[
\chi_c(\mathcal O)\le\chi(\mathcal O)\le4. \tag{5}
\]

Combining (4) and (5) proves
\[
\boxed{\chi_c(\mathcal O)=4}.
\]

## 5. Finite witnesses and the previous attempt

The obstruction above can also be made into a fully specified finite construction for each palette size.

Fix \(m\). Start with the \(2m+1\) lines
\[
[(1,j,j^2)],\qquad 1\le j\le2m+1.
\]
For each triple, apply the geometric lemma, choosing the least \(n\ge0\) for which (3) is positive and an eigenline of the displayed matrix \(E^nF\). Include all lines of its resulting odd closed walk. Let \(F_m\) be the orthogonality graph induced on the resulting finite set of lines.

Then \(F_m\) has no homomorphism to any locally bipartite graph with at most \(m\) vertices: three of the initial lines would receive the same color, and their associated odd walk would map into that color’s bipartite neighborhood. This construction uses only arithmetic, square roots, and a terminating search for \(n\).

In particular, for each fixed circular clique \(K_{p/q}\) with \(p/q<4\), there is a finite obstruction. The obstruction depends on the palette size; the proof does **not** assert that one finite subgraph has circular chromatic number \(4\). It is therefore compatible with the previous attempt’s finite-subgraph projection observation.

The proposed discrete-spectrum reduction is not needed here. The decisive additional ingredient is the odd-walk lemma, which turns bipartiteness of a color’s neighborhood into a dimension restriction on its entire fiber. No unproved conjecture, regularity assumption on the coloring, or computational assertion is used.