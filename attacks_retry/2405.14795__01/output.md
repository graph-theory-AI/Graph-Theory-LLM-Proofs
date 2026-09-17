```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every pair of cyclic midpoint colorings admits a rainbow stacking in every odd order, with an extension to midpoint colorings over abelian groups whose Sylow subgroups are homocyclic.",
  "would_publish": false,
  "caveats": "Arbitrary proper colorings remain untreated; the literature novelty of the auxiliary affine-avoidance result has not been checked."
}
```

# 1. The partial result

Fixing the first coloring, the question is whether there is a vertex bijection \(\pi\) such that
\[
\chi_1(\{u,v\})\ne \chi_2(\{\pi(u),\pi(v)\})
\qquad(u\ne v).
\]
Color labels remain fixed throughout.

I pursue the midpoint-coloring route from the previous attempt. The midpoint identity is verified below; the new ingredient replaces the field-based \(2\)-transitivity argument with an integrality argument. I do not use the previous sparse-overlap or second-moment claims.

Let \(G\) be a finite abelian group of odd order \(n\). Its **midpoint coloring** is
\[
\kappa_G(\{x,y\})=\frac{x+y}{2}.
\]
Division by \(2\) is well-defined because multiplication by \(2\) is an automorphism of \(G\). This coloring is proper: for fixed \(x\), the displayed expression determines \(y\) uniquely. Each color \(c\) is a matching of size \((n-1)/2\), missing precisely the vertex \(c\).

Here is the special case proved in this writeup.

## Theorem 1

Suppose
\[
G=\prod_{i=1}^{t}
   \bigl(\mathbb Z/p_i^{\,k_i}\mathbb Z\bigr)^{d_i},
\]
where the \(p_i\) are distinct odd primes and \(k_i,d_i\ge 1\).

Every pair of colorings obtained from \(\kappa_G\) by arbitrary vertex relabelings and arbitrary injective color relabelings admits a rainbow stacking. The two palettes need not coincide.

In particular, taking \(G=\mathbb Z/n\mathbb Z\):

> **Every pair of cyclic midpoint colorings admits a rainbow stacking for every odd \(n\).**

The case \(n=1\) is vacuous. This includes composite orders such as \(15\) and \(105\), as well as cyclic prime-power groups that are not elementary abelian.

The main auxiliary result is an affine-avoidance theorem. Its proof occupies the next two sections.

# 2. An integral balancing lemma

Write
\[
R_k=\mathbb Z/p^k\mathbb Z,\qquad
\Omega_k=R_k^d,\qquad h=p^d.
\]

## Lemma 2

Let \(M=(M_{xy})_{x,y\in\Omega_k}\) be an integer matrix. Suppose:

1. every row and every column has sum \(m\);
2. for every \(L\in\operatorname{GL}_d(R_k)\) and \(b\in\Omega_k\),
   \[
   \sum_{x\in\Omega_k}M_{x,Lx+b}=m. \tag{1}
   \]

Then
\[
p^d\mid m.
\]

### Proof

We use induction on \(k\). First we establish the block divisibility needed for the induction.

Set
\[
\mathcal L=\operatorname{GL}_d(R_k),
\qquad
H=p^{k-1}\Omega_k.
\]
Thus \(|H|=h\).

For \(u\in\Omega_k\), define its valuation by
\[
\nu(u)=\max\{r:u\in p^r\Omega_k\},
\]
with \(\nu(0)=k\). The group \(\mathcal L\) is transitive on each set of vectors of a fixed valuation. Indeed, a vector of valuation \(r<k\) is \(p^r\) times a primitive vector, and elementary invertible row operations send any primitive vector to the first standard basis vector.

Consequently, the number
\[
C(u,v)=|\{L\in\mathcal L:Lu=v\}|
\]
depends only on the valuations of \(u,v\): it is zero when those valuations differ, and is constant when both vectors belong to a specified common orbit.

In particular, \(\mathcal L\) is transitive on \(H\setminus\{0\}\). Put
\[
\lambda=\frac{|\mathcal L|}{h-1}.
\]
For nonzero \(u,v\in H\), we therefore have \(C(u,v)=\lambda\), while \(C(0,0)=|\mathcal L|\).

For \(x,y\in\Omega_k\), consider
\[
S_{xy}
 =\sum_{L\in\mathcal L}\sum_{z\in\Omega_k}
       M_{z,L(z-x)+y}.
\]
By (1), each inner sum is \(m\), so
\[
S_{xy}=|\mathcal L|m. \tag{2}
\]
Equivalently,
\[
S_{xy}=\sum_{z,w\in\Omega_k}M_{zw}\,C(z-x,w-y). \tag{3}
\]

Fix cosets \(X,Y\) of \(H\), and let \(x\in X,y\in Y\).

* If \(z\notin X\) and \(w\notin Y\), then the valuations of \(z-x\) and \(w-y\) do not change as \(x,y\) vary within their respective cosets. Thus this part of (3) is constant on \(X\times Y\).
* If exactly one of \(z\in X,w\in Y\) holds, the valuations differ, so the contribution is zero.
* Inside \(X\times Y\), the coefficient is \(|\mathcal L|\) at \((z,w)=(x,y)\), zero when exactly one coordinate agrees, and \(\lambda\) when neither agrees.

Write
\[
B_{XY}=\sum_{z\in X,w\in Y}M_{zw},\quad
r_x=\sum_{w\in Y}M_{xw},\quad
c_y=\sum_{z\in X}M_{zy}.
\]
The contribution from \(X\times Y\) is
\[
\lambda\bigl(hM_{xy}+B_{XY}-r_x-c_y\bigr).
\]
Together with (2), this shows that
\[
hM_{xy}-r_x-c_y=D_{XY} \tag{4}
\]
is constant on the block \(X\times Y\). It is an integer.

Summing (4) over the \(h^2\) entries of the block gives
\[
-hB_{XY}=h^2D_{XY}.
\]
Hence
\[
h\mid B_{XY}. \tag{5}
\]

### Base case: \(k=1\)

Now \(H=\Omega_1\), so there is just one block. Its row and column sums are \(m\), and its total sum is \(hm\). Equations (2)–(3) give
\[
|\mathcal L|m
 =\lambda\bigl(hM_{xy}+(h-2)m\bigr).
\]
Since \(|\mathcal L|=\lambda(h-1)\), this simplifies to
\[
hM_{xy}=m.
\]
The entries are integers, so \(h\mid m\).

### Inductive step

Suppose \(k>1\). Define an integer matrix on \(\Omega_k/H\) by
\[
M'_{X,Y}=\frac{B_{XY}}h.
\]
This is integral by (5). Its row and column sums are \(m\).

Identify
\[
\Omega_k/H\cong
\bigl(\mathbb Z/p^{k-1}\mathbb Z\bigr)^d.
\]
Every invertible linear map on this quotient lifts to an element of \(\mathcal L\): any entrywise lift of its matrix has determinant nonzero modulo \(p\), and hence is invertible modulo \(p^k\).

Let \(T'(X)=L'X+b'\) be an affine map of the quotient, and choose lifts \(L,b\). Applying (1) to the \(h\) maps
\[
z\longmapsto Lz+b+t,\qquad t\in H,
\]
and summing gives
\[
hm
 =\sum_{X\in\Omega_k/H} B_{X,T'(X)}
 =h\sum_X M'_{X,T'(X)}.
\]
Thus \(M'\) satisfies the hypotheses of the lemma for \(k-1\). Induction gives \(h\mid m\), completing the proof. \(\square\)

# 3. Affine maps avoiding an arbitrary permutation

The next theorem is independent of edge-coloring. Here the primes may also include \(2\).

## Theorem 3: affine avoidance

Let
\[
G=\prod_{i=1}^{t}
   \bigl(\mathbb Z/p_i^{\,k_i}\mathbb Z\bigr)^{d_i},
\]
where the \(p_i\) are distinct primes, and suppose \(|G|>1\).

For every permutation \(\sigma\) of \(G\), there is a product affine map
\[
T(x_1,\dots,x_t)
  =(L_1x_1+b_1,\dots,L_tx_t+b_t),
\qquad
L_i\in\operatorname{GL}_{d_i}(\mathbb Z/p_i^{k_i}\mathbb Z),
\]
such that
\[
T(x)\ne \sigma(x)\qquad\text{for every }x\in G. \tag{6}
\]

### Proof

For an allowed affine map \(T\), let
\[
A(T)=|\{x:T(x)=\sigma(x)\}|.
\]

Suppose, for a contradiction, that every allowed \(T\) has at least one agreement. For each fixed linear part \(L\),
\[
\sum_{b\in G}A(x\mapsto Lx+b)=|G|,
\]
because each \(x\) contributes for exactly one translation \(b\). There are \(|G|\) translations, and each agreement count is at least one. Hence
\[
A(T)=1\qquad\text{for every allowed affine }T. \tag{7}
\]

Fix an index \(i\), and write
\[
G_i=(\mathbb Z/p_i^{k_i}\mathbb Z)^{d_i},
\qquad
m=\frac{|G|}{|G_i|}.
\]
For \(u,v\in G_i\), define
\[
M_{uv}
 =|\{x\in G:x_i=u,\ \sigma(x)_i=v\}|.
\]
Every row has sum \(m\), and every column has sum \(m\), since \(\sigma\) is a permutation.

Fix an affine map \(T_i\) on \(G_i\). Extend it to \(G\) by using arbitrary translations on all the other factors. There are \(m\) such extensions, each having exactly one agreement by (7). Summing their agreement counts yields
\[
\sum_{u\in G_i}M_{u,T_i(u)}=m. \tag{8}
\]
Indeed, an \(x\) contributes to this sum precisely when
\(\sigma(x)_i=T_i(x_i)\), and then exactly one translation on the other factors supplies a full agreement.

Lemma 2, applied to \(M\), gives
\[
p_i^{d_i}\mid m.
\]
But \(m\) is a product of powers of primes different from \(p_i\). This is impossible. Therefore an affine map satisfying (6) exists. \(\square\)

For cyclic groups, this has a particularly simple formulation.

## Corollary 4

For every integer \(n\ge2\) and every permutation \(\sigma\) of \(\mathbb Z/n\mathbb Z\), there are
\[
a\in(\mathbb Z/n\mathbb Z)^\times,\qquad b\in\mathbb Z/n\mathbb Z
\]
such that
\[
ax+b\ne\sigma(x)\qquad\text{for all }x.
\]

### Proof

Apply Theorem 3 with \(d_i=1\) to the prime-power factors of \(n\), and combine the coordinatewise affine maps by the Chinese remainder theorem. \(\square\)

Notice that Corollary 4 does not assume \(n\) is odd. Oddness enters the graph-coloring application through division by \(2\).

# 4. Proof of the stacking theorem

We now prove Theorem 1.

Choose coordinates for the two vertex sets so that both are identified with \(G\). By hypothesis, there are injections \(\alpha,\beta\) into the global color set such that
\[
\chi_1(\{x,y\})
 =\alpha\!\left(\frac{x+y}{2}\right),
\qquad
\chi_2(\{x,y\})
 =\beta\!\left(\frac{x+y}{2}\right).
\]

For every common color, its two preimages define a correspondence
\[
\alpha(c)=\beta(d)
\quad\Longrightarrow\quad c\mapsto d.
\]
Because \(\alpha,\beta\) are injective, this is a partial bijection of \(G\). Extend it arbitrarily to a permutation \(\sigma\) of \(G\).

By Theorem 3, choose an allowed affine map \(T\) satisfying
\[
T(c)\ne\sigma(c)\qquad(c\in G).
\]
Every such \(T\) preserves midpoints:
\[
\frac{T(x)+T(y)}2
 =T\!\left(\frac{x+y}{2}\right). \tag{9}
\]

Use \(T\) as the relative vertex placement. If an edge with midpoint \(c\) produced a conflict, then (9) would give
\[
\alpha(c)=\beta(T(c)).
\]
By the definition of the partial bijection extended by \(\sigma\), this would force
\[
T(c)=\sigma(c),
\]
a contradiction. Thus every superimposed edge has different colors. Restoring the original vertex coordinates gives the required stacking. \(\square\)

## An explicit search procedure in the cyclic case

The proof gives a simple deterministic procedure once the cyclic coordinates and color relabelings are supplied.

After constructing \(\sigma\), for each unit \(a\pmod n\) form
\[
D_a=\{\sigma(x)-ax:x\in\mathbb Z/n\mathbb Z\}.
\]
Corollary 4 guarantees that at least one \(D_a\) is not all of \(\mathbb Z/n\mathbb Z\). Choose \(b\notin D_a\). Then
\[
T(x)=ax+b
\]
avoids \(\sigma\) everywhere and gives the desired stacking.

Checking all unit slopes uses \(O(n\varphi(n))\) ring operations and \(O(n)\) working memory. This is a proved algorithm for the stated family, not a claim that a computational search was run.

# 5. Scope and remaining gap

The result concerns dense colorings: every color class has the maximum possible size \((n-1)/2\). Nevertheless, the algebraic hypothesis is substantial.

Already at \(n=7\), there are optimal proper colorings outside the cyclic-midpoint class. For example, on
\[
V=\mathbb F_2^3\setminus\{0\},
\]
color \(\{x,y\}\) by \(x+y\). Color \(c\) misses vertex \(c\). After identifying each color with its missed vertex, its operation satisfies
\[
\mu(x,\mu(x,y))=y\qquad(x\ne y).
\]
For cyclic midpoints on \(\mathbb Z/7\mathbb Z\), the corresponding expression is
\[
\mu(x,\mu(x,y))=\frac{3x+y}{4}\ne y
\qquad(x\ne y).
\]
This missing-vertex-normalized identity is preserved under vertex and color relabeling, so the two colorings are not equivalent. This example is not an obstruction; it demonstrates that the theorem does not encompass all optimal proper colorings.

The unresolved step is therefore not in the affine-avoidance proof. It is the absence, for arbitrary proper colorings, of a vertex action that simultaneously induces a controlled permutation of entire color classes. In particular, the argument does not handle:

* one cyclic midpoint coloring paired with an arbitrary proper coloring;
* arbitrary pairs of near-one-factorizations;
* arbitrary pairs using more than \(n\) colors.

Thus the general odd-order question is **not resolved here**, and no counterexample is produced. The precise progress is the all-odd-order cyclic-midpoint theorem and its homocyclic-Sylow extension.