```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A localized-dependency packing argument gives D = Ω(min{k, √(log n/log k)}) for fixed C, with complete rigidity when D ≤ 2, but it does not close the remaining √L-to-L gap.",
  "would_publish": false,
  "caveats": "The desired o(log n/log k) construction is neither produced nor ruled out; C is interpreted as an absolute maximum Lipschitz constant."
}
```

# 1. Statement and conventions

Write \(Q_n=\{0,1\}^n\), with Hamming distance. I interpret a bijection from Dictator to XOR as a bijection
\[
\phi:Q_n\longrightarrow Q_n
\]
such that
\[
x_1=\bigoplus_{j=1}^n \phi_j(x)                     \tag{1}
\]
for every \(x\in Q_n\).

Let
\[
C=\operatorname{Lip}(\phi),\qquad
D=\operatorname{Lip}(\phi^{-1}),
\]
where it suffices to maximize over pairs at Hamming distance one. These quantities are integers. Assume every coordinate function \(\phi_j\) essentially depends on at most \(k\) input coordinates.

The main partial result below improves the general lower bound in a substantial range.

---

# 2. A localized-dependency bound

For integers \(r\ge1\) and \(d\ge0\), define
\[
q(r,d)=
\begin{cases}
1, & d=0,\\[2mm]
\left(\dfrac dr\right)^d
\left(1-\dfrac dr\right)^{r-d},
  & 1\le d\le r/2,\\[3mm]
2^{-r},& d>r/2.
\end{cases}                                           \tag{2}
\]

## Theorem 1

Suppose \(n\ge2\), \(k\ge2\), and \(\phi\) satisfies the hypotheses above. Put
\[
r=k-1,\qquad d=D-1,\qquad M=\frac{C}{q(r,d)}.
\]
Then
\[
\boxed{\quad
n\le M\sum_{s=0}^{D-1}(kM)^s .
\quad}                                                  \tag{3}
\]

In particular, since \(kM\ge2\),
\[
n\le 2k^{D-1}M^D.                                      \tag{4}
\]

When \(1\le D-1\le (k-1)/2\), the entropy estimate
\[
q(k-1,D-1)^{-1}
   \le
\left(\frac{e(k-1)}{D-1}\right)^{D-1}
\]
gives
\[
\boxed{\quad
n\le
2C^D k^{D-1}
\left(\frac{e(k-1)}{D-1}\right)^{D(D-1)} .
\quad}                                                  \tag{5}
\]

## Consequences

For arbitrary \(C\),
\[
D=\Omega\!\left(
\min\left\{
k,\sqrt{\frac{\log n}{\log(2Ck)}}
\right\}\right).                                       \tag{6}
\]
The absolute constant implicit in \(\Omega\) is independent of \(n,k,C\).

Using the uniform measure instead of the localized estimate also recovers
\[
D=\Omega\!\left(
\frac{\log n}{k+\log C+\log k}
\right),                                                \tag{7}
\]
which is the order of the general lower bound stated in the catalog.

Thus, for fixed \(C\),
\[
D=\Omega\!\left(
\max\left\{
\frac{\log n}{k},
\min\left\{
k,\sqrt{\frac{\log n}{\log(2k)}}
\right\}
\right\}\right).                                       \tag{8}
\]

For example, when \(k=\log n\), the previously stated general estimate is only \(D=\Omega(1)\), whereas (6) gives
\[
D=\Omega\!\left(\sqrt{\frac{\log n}{\log\log n}}\right).
\]

For each fixed \(D\ge2\) and fixed \(C\), (5) gives
\[
n=O_D\!\left(k^{D^2-1}\right).                          \tag{9}
\]
Consequently, bounded inverse stretch requires locality polynomial in \(n\). In particular, if \(C=O(1)\) and \(k=n^{o(1)}\), then necessarily \(D\to\infty\).

---

# 3. Proof of Theorem 1

## 3.1. Nearby dependencies of one input coordinate

For an input coordinate \(i\) and output coordinate \(a\), let
\[
E_{i,a}
=
\{z\in Q_n:\phi_a(z)\ne \phi_a(z\oplus e_i)\}.
\]
If \(\phi_a\) depends on a set \(S_a\) of at most \(k\) coordinates, then \(E_{i,a}\) depends on at most \(k-1\) coordinates: the Boolean derivative in direction \(i\) is invariant under changing coordinate \(i\).

Fix \(x\in Q_n\), an input coordinate \(i\), and an integer \(d\ge0\). Define
\[
N_i(x,d)
=
\{a:E_{i,a}\cap B_d(x)\ne\varnothing\}.
\]

### Lemma 2
With \(q\) as in (2),
\[
|N_i(x,d)|\le \frac{C}{q(k-1,d)}.                       \tag{10}
\]

### Proof

At every \(z\),
\[
\sum_{a=1}^n \mathbf 1_{E_{i,a}}(z)
=
d_H\bigl(\phi(z),\phi(z\oplus e_i)\bigr)
\le C.                                                  \tag{11}
\]

Let \(r=k-1\). Suppose first that \(1\le d\le r/2\), and generate a random \(Z\) from \(x\) by flipping each coordinate independently with probability
\[
p=\frac dr.
\]

For \(a\in N_i(x,d)\), choose a witness \(z\in E_{i,a}\cap B_d(x)\). On the at most \(r\) coordinates determining \(E_{i,a}\), the corresponding assignment differs from \(x\) in at most \(d\) positions. Since the derivative is constant on the resulting cylinder,
\[
\Pr(Z\in E_{i,a})
\ge p^d(1-p)^{r-d}
=q(r,d).                                                \tag{12}
\]
The same lower bound remains valid when the actual support has fewer than \(r\) coordinates.

Taking expectations in (11),
\[
|N_i(x,d)|q(r,d)
\le
\sum_{a\in N_i(x,d)}\Pr(Z\in E_{i,a})
\le C.
\]

If \(d>r/2\), take \(p=1/2\). Every nonempty derivative event contains a cylinder of codimension at most \(r\), so it has probability at least \(2^{-r}\). The case \(d=0\) follows directly from (11). ∎

---

## 3.2. A connectedness lemma

Let \(F:Q_n\to Q_n\) be injective, and suppose
\[
F(x)\oplus F(x')=e_a.                                  \tag{13}
\]
Let
\[
R=\{i:x_i\ne x'_i\}.
\]
Restrict the coordinate functions of \(F\) to the subcube obtained by varying only coordinates in \(R\). Form a bipartite graph whose left side is \(R\), whose right side is the output coordinates, and where \(i\) is adjacent to \(b\) if the restricted function \(F_b\) essentially depends on \(i\).

### Lemma 3
All left vertices in \(R\), together with output vertex \(a\), lie in one connected component.

### Proof

Every left vertex has a neighbor, since otherwise changing that input coordinate inside the restricted subcube would leave every output unchanged, contradicting injectivity.

Suppose the left vertices split into distinct components
\[
R_1,\ldots,R_m.
\]
No restricted output function can depend on variables from two different components.

For each \(t\), let \(x^{(t)}\) be obtained from \(x\) by changing precisely the coordinates in \(R_t\) to their values in \(x'\). Since \(x^{(t)}\ne x\), injectivity implies
\[
F(x^{(t)})\ne F(x).
\]
Moreover, the set of output coordinates changed by passing from \(x\) to \(x^{(t)}\) belongs entirely to the right-hand vertices of component \(t\). These changed-output sets are nonempty and pairwise disjoint.

Changing all components gives \(x'\). Hence the support of \(F(x)\oplus F(x')\) is the disjoint union of \(m\) nonempty sets. By (13) it has size one, so \(m=1\). Since output \(a\) changes between the endpoints, it is nonconstant on the restricted subcube and belongs to this component. ∎

---

## 3.3. Applying the lemmas to inverse edges

Fix \(x\), and write \(y=\phi(x)\). For every output coordinate \(a\), put
\[
x^{(a)}=\phi^{-1}(y\oplus e_a),
\qquad
R_a=\{i:x_i\ne x_i^{(a)}\}.
\]
The inverse Lipschitz assumption gives
\[
|R_a|\le D.                                             \tag{14}
\]

Equation (1) implies
\[
(\phi^{-1}(y))_1=\bigoplus_j y_j.
\]
Thus toggling any output bit toggles the first input bit, so
\[
1\in R_a                                                   \tag{15}
\]
for every \(a\).

Apply Lemma 3 to \(x,x^{(a)}\). It gives a path in the restricted dependency graph from input vertex \(1\) to output vertex \(a\), using at most \(|R_a|\le D\) left vertices.

If an edge \(i-b\) occurs in this restricted graph, there is a witness to
\[
\phi_b(z)\ne\phi_b(z\oplus e_i)
\]
inside the \(R_a\)-subcube. Since this derivative is invariant under flipping \(i\), the witness can be chosen with \(z_i=x_i\). It therefore differs from \(x\) in at most
\[
|R_a|-1\le D-1
\]
coordinates.

Now form a global bipartite graph \(G_x\) between input and output coordinates by joining \(i\) to \(b\) whenever
\[
E_{i,b}\cap B_{D-1}(x)\ne\varnothing .
\]
Lemma 2 says every left degree is at most
\[
M=\frac{C}{q(k-1,D-1)}.
\]
Every right degree is at most \(k\), because each output coordinate depends on at most \(k\) input coordinates.

The preceding argument shows that every one of the \(n\) output vertices can be reached from input vertex \(1\) by an alternating path containing at most \(D\) left vertices. The number of reachable output vertices is at most
\[
M+M(kM)+\cdots+M(kM)^{D-1},
\]
which proves (3).

For \(d\le r/2\),
\[
q(r,d)^{-1}
=
\left(\frac rd\right)^d
\left(\frac r{r-d}\right)^{r-d}
\le
\left(\frac{er}{d}\right)^d.
\]
Substitution into (4) proves (5). ∎

---

# 4. Complete rigidity for inverse stretch at most two

The preceding general estimate is far from sharp for \(D=2\). In that case there is a complete classification.

## Proposition 4
Let \(n\ge2\), and suppose \(\phi\) is a Dictator-to-XOR bijection with
\[
\operatorname{Lip}(\phi^{-1})\le2.
\]
Then \(\phi^{-1}\) is affine, and some coordinate of \(\phi\) depends on all \(n\) input coordinates. Consequently,
\[
k\ge n.
\]
No such bijection has inverse Lipschitz constant \(1\).

### Proof

Let \(\psi=\phi^{-1}\). For adjacent \(y,y\oplus e_j\), equation (1) implies that
\[
\psi(y)\oplus\psi(y\oplus e_j)
\]
contains coordinate \(1\). Its weight is at most two. Thus it belongs to
\[
\mathcal B=
\{e_1,\ e_1\oplus e_2,\ldots,e_1\oplus e_n\}.           \tag{16}
\]
This set has exactly \(n\) elements.

For fixed \(y\), the \(n\) points \(\psi(y\oplus e_j)\) are distinct. Hence their \(n\) difference vectors from \(\psi(y)\) are distinct elements of \(\mathcal B\), and therefore exhaust \(\mathcal B\).

Let \(T\) be the invertible linear map whose columns are
\[
e_1,\ e_1\oplus e_2,\ldots,e_1\oplus e_n.
\]
Then
\[
h=T^{-1}\circ\psi
\]
is a vertex bijection of \(Q_n\) taking every edge to an edge. It is therefore a graph automorphism of \(Q_n\). Every cube automorphism has the form
\[
h(y)=a\oplus Py,
\]
where \(P\) is a permutation matrix. Hence
\[
\psi(y)=T(a\oplus Py).                                  \tag{17}
\]

The first coordinate of \(Tz\) is \(\bigoplus_i z_i\). The Dictator-to-XOR condition therefore requires \(\bigoplus_i a_i=0\).

Inverting (17),
\[
\phi(x)=P^{-1}\bigl(T^{-1}x\oplus a\bigr).
\]
A direct calculation gives
\[
T^{-1}x
=
\left(
x_1\oplus x_2\oplus\cdots\oplus x_n,\,
x_2,\ldots,x_n
\right).                                                \tag{18}
\]
Thus, up to an output permutation and constants, one coordinate of \(\phi\) is the parity of all \(n\) input coordinates. It essentially depends on all \(n\) inputs.

If \(D\le1\), the only possible difference vector is \(e_1\), so all \(n\) neighbors of a fixed \(y\) would have the same image under \(\psi\), contradicting injectivity. ∎

---

# 5. Relation to the open problem

Let
\[
L=\frac{\log n}{\log k}.
\]
The supplied linear construction has inverse stretch \(O(L)\). Theorem 1 gives, in the natural regime \(D=o(k)\) and fixed \(C\),
\[
D=\Omega(\sqrt L),                                      \tag{19}
\]
rather than merely \(\Omega((\log n)/k)\).

Thus an affirmative solution with
\[
D=o(L)
\]
is not ruled out, but in the subpolynomial-locality regime it cannot have bounded \(D\); broadly, it would have to lie in a window resembling
\[
\sqrt L\ \lesssim\ D\ \ll L.
\]

The proof loses a factor of roughly \(D\) in the exponent because a connected inverse fiber of size \(D\) may use dependency witnesses lying at different corners of its \(D\)-dimensional subcube. Eliminating that loss would change the bound \(n\le k^{O(D^2)}\) into \(n\le k^{O(D)}\), which would yield the desired \(\Omega(\log n/\log k)\) lower bound. The present argument does not justify such an improvement, and no construction attaining the square-root scale is provided.