```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but it reduces to a single coloring-count inequality and holds for every graph obtained by inserting an alternating decagonal collar, ruling out a natural 36-vertex test family.",
  "would_publish": false,
  "caveats": "The collar operation is not reversible, and general plane near-cubic graphs need not contain such a collar."
}
```

## 1. Statement and coordinate form

Let the five edges incident with the distinguished vertex be indexed cyclically by \(\mathbb Z_5\). In every 3-edge-coloring away from the distinguished vertex, the colors on these five edges have multiplicities \((3,1,1)\). Thus a boundary-coloring type is determined by the unordered pair of positions occupied by the two singleton colors.

Write

\[
a_i:=\{i,i+1\},\qquad b_i:=\{i,i+2\},\qquad i\in\mathbb Z_5,
\]

and use the same symbols for the corresponding coordinates of a coloring-count vector.

In these coordinates, \(B_5\) is the nonnegative circulation cone determined by

\[
a_i+b_{i-2}=a_{i-1}+b_i
\qquad (i\in\mathbb Z_5).
\tag{1}
\]

Indeed, regard \(a_i\) as an arc \(i+1\to i\) and \(b_i\) as an arc \(i\to i+2\) in a directed graph on \(\mathbb Z_5\). Equation (1) is flow conservation.

The twelve extreme-ray directions are the simple directed cycles:

\[
\begin{aligned}
P&:=\sum_i a_i,\\
S&:=\sum_i b_i,\\
X_i&:=a_i+b_i+b_{i+2}+b_{i-1},\\
Y_i&:=b_i+a_i+a_{i+1}.
\end{aligned}
\tag{2}
\]

Here \(P\), the five \(X_i\), and the five \(Y_i\) are the eleven planar rays, while \(S\) is the excluded ray represented by \(\tilde R_{5,12}\). Hence

\[
B'_5=\operatorname{cone}\bigl(P,X_i,Y_i:i\in\mathbb Z_5\bigr).
\]

This is a relabeling of the source's twelve ray directions.

---

## 2. \(B'_5\) has one additional inequality

For a vector \(x\), put

\[
A(x)=\sum_i x(a_i),\qquad D(x)=\sum_i x(b_i).
\]

### Lemma 1

For \(x\in B_5\),

\[
x\in B'_5
\quad\Longleftrightarrow\quad
D(x)\le 3A(x).
\tag{3}
\]

### Proof

On the generators in (2),

\[
\begin{array}{c|cccc}
 &P&S&X_i&Y_i\\ \hline
A&5&0&1&2\\
D&0&5&3&1.
\end{array}
\]

Thus \(D\le 3A\) on every generator of \(B'_5\).

Conversely, write

\[
x=pP+sS+\sum_i u_iX_i+\sum_i v_iY_i
\]

with all coefficients nonnegative. Then

\[
D(x)-3A(x)=5\left(s-3p-\sum_i v_i\right).
\tag{4}
\]

The following vector identities hold:

\[
P+3S=\sum_i X_i,
\qquad
S+Y_i=X_i+X_{i+1}.
\tag{5}
\]

If \(D(x)\le3A(x)\), equation (4) gives

\[
s\le 3p+\sum_i v_i.
\]

Use the second identity in (5) to eliminate as much of the coefficient \(s\) as possible against the \(Y_i\)-coefficients. Any remaining amount \(r\) satisfies \(r\le3p\), and the first identity eliminates \(rS\) against \((r/3)P\). This produces a nonnegative decomposition using only \(P,X_i,Y_i\). Hence \(x\in B'_5\). \(\square\)

Thus Conjecture 8 is exactly the assertion

\[
\boxed{\ \sum_i n_{\tilde G}(b_i)\le
3\sum_i n_{\tilde G}(a_i)\ }.
\tag{6}
\]

---

## 3. Equivalent formulation for near-triangulations

Under the usual duality with a near-triangulation \(G\) whose outer boundary is \(C_5\):

- the \(a_i\)-types correspond to boundary colorings using exactly three colors;
- the \(b_i\)-types correspond to boundary colorings using all four colors.

Let \(T\) be obtained by adding a vertex \(v\) adjacent to all five vertices of the outer cycle. Then \(T\) is a plane triangulation and \(d_T(v)=5\). Every 3-colored boundary coloring extends uniquely to \(v\), while a 4-colored boundary coloring does not extend.

Every boundary-coloring orbit has \(24\) labeled colorings. Consequently,

\[
P(T,4)=24A(n_{\tilde G}),\qquad
P(T-v,4)=24\bigl(A(n_{\tilde G})+D(n_{\tilde G})\bigr).
\]

Therefore (6) is equivalent, in the standard simple outer-cycle setting, to

\[
\boxed{\ P(T-v,4)\le 4P(T,4)\ }
\tag{7}
\]

for every plane triangulation \(T\) and every degree-five vertex \(v\).

This makes the quantitative strengthening of the Four Color Theorem particularly transparent: among the 4-colorings of \(T-v\), at least one quarter would have to extend to \(v\).

---

## 4. A decagonal-collar reduction

Define an annular gadget \(\mathcal A\) as follows. It has a cycle

\[
u_0,z_0,u_1,z_1,\ldots,u_4,z_4,u_0.
\]

The five \(u_i\) are joined inward to a new distinguished vertex, and the five \(z_i\) are joined outward to the five boundary edges of another near-cubic 5-pole \(H\), preserving cyclic order. This is an alternating decagonal collar.

Let \(T_{\mathcal A}\) be the induced linear map on coloring-count vectors.

### Lemma 2: transfer equations

For \(x=n_H\),

\[
\begin{aligned}
(T_{\mathcal A}x)(a_i)
 &=x(a_i)+x(a_{i-1})+2x(b_{i-1}),\\
(T_{\mathcal A}x)(b_i)
 &=2x(a_i)+x(b_i)+2x(b_{i+2})+x(b_{i-1}).
\end{aligned}
\tag{8}
\]

### Proof

Represent the three edge colors by the nonzero elements of \(\mathbb F_2^2\). Let \(s_i\) be the color of the inward edge at \(u_i\), \(t_i\) the outward color at \(z_i\), and \(r_{i-1},r_i\) the two cycle-edge colors bordering the pair \(u_i,z_i\).

At \(u_i\), once \(r_{i-1}\ne s_i\), the third edge has color \(r_{i-1}+s_i\). At \(z_i\), the two remaining colors are \(r_{i-1}\) and \(s_i\). Hence exactly two transitions are possible:

\[
(r_i,t_i)=(r_{i-1},s_i)
\quad\text{or}\quad
(r_i,t_i)=(s_i,r_{i-1}).
\tag{9}
\]

One also imposes \(r_4=r_{-1}\).

For representatives \(a_0\) and \(b_0\), enumerating the closed three-state walks from (9) gives

\[
\begin{array}{c|c}
\text{inward type}&\text{outward types and multiplicities}\\ \hline
a_0&a_0+a_4+2b_4,\\
b_0&2a_0+b_0+2b_2+b_4.
\end{array}
\]

Rotation gives (8). \(\square\)

### Proposition 3

\[
T_{\mathcal A}(B_5)\subseteq B'_5.
\tag{10}
\]

### Proof

Direct substitution in (8) gives

\[
\begin{aligned}
T_{\mathcal A}(P)
 &=\frac43P+\frac23\sum_jX_j,\\
T_{\mathcal A}(S)
 &=\frac23P+\frac43\sum_jX_j,\\
T_{\mathcal A}(X_i)
 &=X_i+X_{i+1}+2X_{i+3}+2Y_i,\\
T_{\mathcal A}(Y_i)
 &=2X_{i+1}+Y_i+Y_{i+1}.
\end{aligned}
\tag{11}
\]

Every coefficient is nonnegative and every ray on the right belongs to \(B'_5\). Since the rays in (2) generate \(B_5\), (10) follows. \(\square\)

Equivalently, summing (8) gives

\[
A(T_{\mathcal A}x)=2A(x)+2D(x),\qquad
D(T_{\mathcal A}x)=2A(x)+4D(x),
\]

and hence

\[
3A(T_{\mathcal A}x)-D(T_{\mathcal A}x)
=4A(x)+2D(x)\ge0.
\]

### Corollary 4

Every plane near-cubic graph obtained by inserting an alternating decagonal collar around the distinguished vertex satisfies Conjecture 8, irrespective of the graph outside the collar.

Thus a counterexample cannot have this separating collar around its distinguished vertex.

---

## 5. An exact family beyond the published computation

Let \(H_0\) be the wheel consisting of the distinguished vertex joined to a surrounding 5-cycle. Its vector is

\[
n_{H_0}=P;
\]

for each \(a_i\)-precoloring the rim coloring is unique, while no \(b_i\)-precoloring extends.

Define recursively

\[
H_{k+1}=\mathcal A[H_k].
\]

The graph \(H_k\) has \(6+10k\) vertices. In particular, \(H_3\) has \(36\) vertices and lies beyond the source's verification below \(30\) vertices.

By rotational symmetry write

\[
n_{H_k}(a_i)=A_k,\qquad n_{H_k}(b_i)=D_k.
\]

Equation (8) gives

\[
\binom{A_{k+1}}{D_{k+1}}
=
\begin{pmatrix}
2&2\\
2&4
\end{pmatrix}
\binom{A_k}{D_k},
\qquad
(A_0,D_0)=(1,0).
\]

Thus

\[
(A_1,D_1)=(2,2),\quad
(A_2,D_2)=(8,12),\quad
(A_3,D_3)=(40,64).
\]

For the first unverified member,

\[
D_3=64<3\cdot40=120,
\]

so the 36-vertex graph is not a counterexample. In fact \(D_k/A_k\) tends to

\[
\frac{1+\sqrt5}{2}<3,
\]

so the entire family lies safely inside \(B'_5\).

---

## 6. Remaining gap

The argument does not resolve Conjecture 8. Inserting the collar maps even the excluded ray \(S\) into \(B'_5\), so the transfer is not reversible and cannot be used to infer \(n_H\in B'_5\) from \(n_{\mathcal A[H]}\in B'_5\). General plane near-cubic graphs need not contain such a collar.

The unresolved core is therefore the counting inequality

\[
\sum_i n_{\tilde G}(b_i)\le3\sum_i n_{\tilde G}(a_i),
\]

or equivalently \(P(T-v,4)\le4P(T,4)\) at a degree-five vertex. I do not have either a proof of this inequality for arbitrary plane triangulations or an explicit graph violating it. The collar lemma may also be implicit in the source's computational framework; I have not verified novelty sufficient for publication.