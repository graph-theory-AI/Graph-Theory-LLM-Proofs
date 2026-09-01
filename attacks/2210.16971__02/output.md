```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Classical Sidorenko is equivalent to an exact transpose-product inequality, which proves the conjectured equivalence for color-class-reversible bipartite graphs and gives a weaker one-sided bound in general.",
  "would_publish": false,
  "caveats": "The smaller of the two oriented homomorphism densities remains uncontrolled; novelty of the elementary tensor argument is not asserted."
}
```

## 1. Formulation

I use the standard bigraphon formulation. Let \(H=(A,B;E)\) be a finite bipartite graph with a fixed bipartition, and put \(e=|E(H)|\). For a measurable \(W:X\times Y\to[0,1]\) on probability spaces \(X,Y\), define

\[
t_H(W)=
\int_{X^A\times Y^B}
\prod_{ab\in E(H)}W(x_a,y_b)\,d\mathbf x\,d\mathbf y
\]

and

\[
d(W)=\int_{X\times Y}W(x,y)\,dx\,dy.
\]

The transpose bigraphon is

\[
W^\top(y,x)=W(x,y).
\]

Thus \(t_H(W^\top)\) is the homomorphism density obtained by sending \(A\) to \(Y\) and \(B\) to \(X\).

The classical Sidorenko property is

\[
t_H(U)\ge d(U)^e
\tag{1}
\]

for every symmetric graphon \(U\). The asymmetric Sidorenko property is the same inequality for every bigraphon \(W\). Since \(W^\top\) is also an allowed bigraphon, the latter is equivalent to

\[
\min\{t_H(W),t_H(W^\top)\}\ge d(W)^e
\tag{2}
\]

for every \(W\).

## 2. A transpose-product characterization of the classical property

### Theorem

For every finite bipartite \(H\), the following are equivalent.

1. \(H\) has the classical Sidorenko property.
2. Every bigraphon \(W\) satisfies
   \[
   t_H(W)t_H(W^\top)\ge d(W)^{2e}.
   \tag{3}
   \]
3. Every bigraphon \(W\) satisfies
   \[
   \frac{t_H(W)+t_H(W^\top)}2\ge d(W)^e.
   \tag{4}
   \]

Thus the classical property already gives the exact geometric-mean, and hence arithmetic-mean, asymmetric inequality. The open step is replacing the mean by the minimum.

### Proof of \(1\Rightarrow 2\)

Isolated vertices are irrelevant. Let \(H_1,\dots,H_c\) be the connected components of \(H\) containing edges, and let \(v_+\) be their total number of vertices.

Given \(W:X\times Y\to[0,1]\), form the tensor product bigraphon

\[
K=W\otimes W^\top
\]

whose row space is \(X\times Y\), whose column space is \(Y\times X\), and whose value is

\[
K\bigl((x,y),(y',x')\bigr)
   =W(x,y')W(x',y).
\]

Tensor factorization gives

\[
d(K)=d(W)^2
\]

and, for every component \(H_i\),

\[
t_{H_i}(K)
 =t_{H_i}(W)t_{H_i}(W^\top)
 =t_{H_i}(K^\top).
\tag{5}
\]

Set

\[
z_i=t_{H_i}(W)t_{H_i}(W^\top).
\]

For an integer \(n\ge1\), let \(K_n=K^{\otimes n}\). Then

\[
d(K_n)=d(W)^{2n},\qquad
t_{H_i}(K_n)=t_{H_i}(K_n^\top)=z_i^n.
\]

Now take the symmetric dilation \(U_n\) of \(K_n\): its probability space is the disjoint union of the row and column spaces of \(K_n\), each given mass \(1/2\); it equals \(K_n\) across the two parts and is zero inside either part. Consequently,

\[
d(U_n)=\frac{d(W)^{2n}}2.
\tag{6}
\]

For each connected component \(H_i\), a nonzero homomorphism into \(U_n\) has exactly two possible orientations across the two blocks. Hence

\[
t_{H_i}(U_n)
 =2^{-|V(H_i)|}
   \bigl(t_{H_i}(K_n)+t_{H_i}(K_n^\top)\bigr)
 =2^{1-|V(H_i)|}z_i^n.
\]

Multiplying over components,

\[
t_H(U_n)
 =2^{c-v_+}
  \left(t_H(W)t_H(W^\top)\right)^n.
\tag{7}
\]

Applying the classical Sidorenko inequality to the symmetric graphon \(U_n\), equations (6) and (7) give

\[
2^{c-v_+}
\left(t_H(W)t_H(W^\top)\right)^n
\ge
2^{-e}d(W)^{2en}.
\]

Therefore

\[
t_H(W)t_H(W^\top)
\ge
2^{(v_+-c-e)/n}d(W)^{2e}.
\]

Letting \(n\to\infty\) proves (3).

### Proof of the remaining implications

By the arithmetic-geometric mean inequality, (3) implies (4).

Conversely, if \(U\) is symmetric, then \(U^\top=U\), so (4) reduces to

\[
t_H(U)\ge d(U)^e.
\]

Thus (4) implies the classical property. ∎

## 3. Consequences

### 3.1 Color-class-reversible graphs

Suppose the underlying graph \(H\) has an automorphism carrying \(A\) onto \(B\). Equivalently, \(H\), as a bigraph, is isomorphic to its transpose. Then for every \(W\),

\[
t_H(W)=t_H(W^\top).
\]

If \(H\) is classically Sidorenko, (3) therefore gives

\[
t_H(W)^2\ge d(W)^{2e},
\]

and hence

\[
t_H(W)\ge d(W)^e.
\]

Thus:

> **Corollary.** For every bipartite graph admitting a color-class-reversing automorphism, the classical and asymmetric Sidorenko properties are equivalent.

This includes connected bipartite graphs with an automorphism interchanging their color classes, as well as appropriately transpose-paired disconnected bigraphs.

More generally, the same conclusion holds whenever the identity

\[
t_H(W)=t_H(W^\top)
\]

holds for every bigraphon \(W\), regardless of how that identity is obtained.

### 3.2 A transpose-paired double

Let \(H^\top\) denote \(H\) with its color classes exchanged, and consider the fixed bigraph

\[
H\sqcup H^\top.
\]

Then

\[
t_{H\sqcup H^\top}(W)
 =t_H(W)t_H(W^\top).
\]

Consequently,

\[
H\text{ is classically Sidorenko}
\quad\Longleftrightarrow\quad
H\sqcup H^\top\text{ is asymmetrically Sidorenko}
\]

for this transpose-paired choice of bipartition. This does not imply that \(H\) itself is asymmetrically Sidorenko.

### 3.3 A general one-sided exponent

Let \(\nu(H)\) be the maximum matching size of \(H\). For \(0\le W\le1\), choose a matching \(M\) of size \(\nu(H)\). Pointwise,

\[
\prod_{ab\in E(H)}W(x_a,y_b)
\le
\prod_{ab\in M}W(x_a,y_b).
\]

Since the matching edges use disjoint variables, integration gives

\[
t_H(W)\le d(W)^{\nu(H)}.
\tag{8}
\]

Combining (3) with (8), applied to \(W^\top\), yields

\[
t_H(W)
 \ge \frac{d(W)^{2e}}{t_H(W^\top)}
 \ge d(W)^{2e-\nu(H)}.
\tag{9}
\]

Hence every classically Sidorenko graph satisfies the asymmetric lower bound

\[
\boxed{t_H(W)\ge d(W)^{\,2e-\nu(H)}}.
\]

This is weaker than the desired exponent \(e\), since \(\nu(H)\le e\), but it is a uniform one-sided estimate. It recovers the exact exponent only when \(H\) is a matching, up to isolated vertices.

### 3.4 Restrictions on a possible counterexample

If \(H\) is classically Sidorenko but fails the asymmetric property, there must be some \(W\) of density \(0<d<1\) such that, writing

\[
x=t_H(W),\qquad y=t_H(W^\top),
\]

one has, after possibly transposing \(W\),

\[
d^{2e-\nu(H)}
 \le x<d^e<\frac{d^{2e}}x\le y\le d^{\nu(H)}.
\tag{10}
\]

In particular:

- the two orientations must lie on opposite sides of the Sidorenko threshold;
- \(H\) cannot be color-class reversible;
- the orientation imbalance is essential.

Also, rank-one bigraphons cannot witness failure. Indeed, if \(W(x,y)=f(x)g(y)\), then

\[
t_H(W)
 =
 \prod_{a\in A}\int f^{\deg(a)}
 \prod_{b\in B}\int g^{\deg(b)}
 \ge
 \left(\int f\right)^e
 \left(\int g\right)^e
 =d(W)^e
\]

by Jensen's inequality.

## 4. Why this does not finish the conjecture

Normalize

\[
X=\frac{t_H(W)}{d(W)^e},
\qquad
Y=\frac{t_H(W^\top)}{d(W)^e}.
\]

The theorem proves exactly

\[
XY\ge1,
\]

whereas the asymmetric property asks for

\[
X\ge1\quad\text{and}\quad Y\ge1.
\]

There is no purely numerical implication: \(X<1<Y\) is compatible with \(XY\ge1\).

The obstruction is already visible in the usual two-block symmetrization. If \(H\) is connected, \(a=|A|\), \(b=|B|\), and the two blocks have masses \(p\) and \(1-p\), classical Sidorenko gives

\[
p^a(1-p)^b\,t_H(W)
+
p^b(1-p)^a\,t_H(W^\top)
\ge
\bigl(2p(1-p)d(W)\bigr)^e.
\tag{11}
\]

Both orientations persist with positive coefficients. The tensor argument above removes constant losses and gives the exact geometric mean, but it still cannot distinguish the smaller orientation.

Moreover, if \(t_H(W)\ne t_H(W^\top)\), tensor powers amplify rather than reduce the imbalance:

\[
\frac{t_H((W^\top)^{\otimes n})}{t_H(W^{\otimes n})}
=
\left(\frac{t_H(W^\top)}{t_H(W)}\right)^n.
\]

Thus no uniform constant-factor comparison between the two orientations can resolve the general case unless the two homomorphism functionals are identically equal.

The missing ingredient is therefore a genuinely orientation-separating argument showing that the pair of homomorphism densities arising from a classically Sidorenko graph cannot realize \(X<1<Y\). I do not have such an argument or an explicit counterexample. The general conjecture remains open under this attack.