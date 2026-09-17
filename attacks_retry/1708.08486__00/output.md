```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured exponential base 3 holds for affine images of low-degree polynomial graphs, but the unrestricted problem remains unresolved here.",
  "would_publish": false,
  "caveats": "The degree bound must be independent of the ambient dimension; no reduction of arbitrary extremal sets to this class is proved, and no novelty is claimed."
}
```

# A partial result for polynomial graphs

I obtain a concrete algebraic special case with matching exponential base \(3\). The argument uses polynomial equations and a Chevalley–Warning argument, rather than the recursively Fourier-uniform hypothesis in the previous attempt.

This does **not** prove the catalogued conjecture.

## 1. The unrestricted question

Let
\[
r(n,m)=\max\{|A|:A\subseteq\mathbb F_3^n
\text{ contains no affine }m\text{-flat}\},
\]
and define
\[
\varepsilon_m^*
=
1-\limsup_{n\to\infty}\frac{\log_3 r(n,m)}n.
\]
The question is whether
\[
\varepsilon_m^*=3^{-m+o(m)}.
\]

The missing direction is an upper bound on the size of **every** \(m\)-flat-free set, giving
\[
\varepsilon_m^*\ge 3^{-m-o(m)}.
\]

Below, I prove this direction—and a matching exponential-scale construction—for polynomial graphs.

## 2. Statement of the special-case theorem

For integers \(k,t\ge0\), a polynomial map
\[
P:\mathbb F_3^k\longrightarrow\mathbb F_3^t
\]
has degree at most \(D\) if each coordinate function has a polynomial representative of total degree at most \(D\). Its graph is
\[
\Gamma_P=\{(x,P(x)):x\in\mathbb F_3^k\}
\subseteq\mathbb F_3^{k+t}.
\]

Let \(R_D(n,m)\) be the largest size of an \(m\)-flat-free set that is affinely equivalent to such a graph, where \(k+t=n\) and \(\deg P\le D\).

Define
\[
H_m=(2m+1)3^{m-1}-2m+2.
\]

### Theorem
For every \(m\ge1\), writing \(N=3^n\),
\[
\frac13 N^{\,1-(m+1)3^{-m}}
\le R_{2m}(n,m)
\le
3^{(m-1)/H_m}N^{\,1-1/H_m}.
\tag{1}
\]

Consequently, if
\[
\varepsilon_m^{\mathrm{pg}}
=
1-\limsup_{n\to\infty}\frac{\log_3 R_{2m}(n,m)}n,
\]
then
\[
\frac1{H_m}
\le \varepsilon_m^{\mathrm{pg}}
\le \frac{m+1}{3^m}.
\tag{2}
\]
Since
\[
H_m\sim \frac{2m}{3}\,3^m,
\]
this proves
\[
\boxed{\varepsilon_m^{\mathrm{pg}}=3^{-m+o(m)}}.
\]

Thus the desired exponential base is exactly \(3\) in this algebraic class.

A useful observation throughout is:

> The graph \(\Gamma_P\) contains an affine \(m\)-flat if and only if \(P\) is affine on some affine \(m\)-flat of its domain.

Indeed, projection onto the domain is injective on every subset of a graph. An \(m\)-flat in the graph therefore projects injectively onto an \(m\)-flat, and its inverse is affine. The converse is immediate.

## 3. The polynomial zero lemma

We use the following elementary form of Chevalley–Warning.

### Lemma
Let \(F_1,\dots,F_s\) be polynomials over \(\mathbb F_3\) in \(h\) variables. If
\[
\sum_{i=1}^s\deg F_i<h,
\]
then the number of their common zeros in \(\mathbb F_3^h\) is divisible by \(3\). In particular, if \(0\) is a common zero, there is another common zero.

### Proof
Modulo \(3\), the number of common zeros equals
\[
\sum_{x\in\mathbb F_3^h}
\prod_{i=1}^s\bigl(1-F_i(x)^2\bigr).
\]
The polynomial being summed has total degree less than \(2h\). Every monomial in it therefore has some variable with exponent \(0\) or \(1\). Summing over that variable gives zero in \(\mathbb F_3\), since
\[
\sum_{a\in\mathbb F_3}1=0,
\qquad
\sum_{a\in\mathbb F_3}a=0.
\]
Thus the number of common zeros is divisible by \(3\). If one zero exists, the number cannot be one. ∎

## 4. Forcing a flat in a low-degree polynomial graph

Set
\[
B_m=H_m-1=(2m+1)3^{m-1}-2m+1.
\]

We prove the following stronger, pointwise assertion.

### Proposition
Suppose
\[
P:\mathbb F_3^k\longrightarrow\mathbb F_3^t,
\qquad \deg P\le2m.
\]
If
\[
k\ge m+tB_m,
\tag{3}
\]
then \(P\) is affine on an \(m\)-dimensional linear subspace of its domain.

By translating the domain, the same conclusion holds through any prescribed domain point.

### Proof
We construct subspaces
\[
U_0<U_1<\cdots<U_m
\]
with \(\dim U_j=j\), such that \(P|_{U_j}\) is affine.

Suppose \(U_j\) has been constructed, where \(0\le j<m\), and fix a basis \(u_1,\dots,u_j\). Choose a linear complement \(W\) of \(U_j\), so
\[
\dim W=k-j.
\]
We seek a nonzero \(v\in W\) for which \(P\) is affine on \(U_j+\langle v\rangle\).

For each coordinate \(P_i\), consider
\[
P_i\!\left(\sum_{\ell=1}^j a_\ell u_\ell+zv\right),
\]
as a polynomial in the parameters \(a_1,\dots,a_j,z\), with coefficients polynomial in \(v\).

Reduce the parameter exponents using \(w^3=w\). The resulting expression is
\[
P_i\!\left(\sum_{\ell=1}^j a_\ell u_\ell\right)
+
\sum_{\substack{e\in\{0,1,2\}^j\\ b\in\{1,2\}}}
C_{i,e,b}(v)a^e z^b.
\tag{4}
\]
The first term is affine in \(a\), by the induction hypothesis.

It is sufficient to impose
\[
C_{i,e,b}(v)=0
\quad\text{for every }(e,b)\ne(0,1).
\tag{5}
\]
Then (4) is affine in all \(j+1\) parameters.

Every equation in (5) vanishes at \(v=0\). We now bound the sum of their degrees.

### Degree accounting

Write \(|e|=\sum_\ell e_\ell\). A term contributing to \(C_{i,e,b}\) arose before parameter reduction with some positive power \(z^h\), where

- \(h\) has the same parity as \(b\);
- its degree in \(v\) is \(h\);
- \(h\le2m-|e|\).

Consequently, for \(e\ne0\), the two degree bounds corresponding to \(b=1,2\) have sum at most
\[
2(2m-|e|)-1.
\]
Here \(2m-|e|\ge2\), because \(j\le m-1\). The remaining imposed coefficient \(C_{i,0,2}\) has degree at most \(2m\).

Thus, for each coordinate \(i\), the sum of the degrees of the equations is at most
\[
\begin{aligned}
b_j
&=
2m+\sum_{\substack{e\in\{0,1,2\}^j\\e\ne0}}
(4m-2|e|-1)\\
&=(4m-2j-1)3^j-2m+1,
\end{aligned}
\tag{6}
\]
where we used
\[
\sum_{e\in\{0,1,2\}^j}|e|=j3^j.
\]
Identically zero equations can simply be omitted.

For \(0\le j\le m-2\),
\[
b_{j+1}-b_j
=
4(2m-j-2)3^j>0.
\]
Therefore
\[
b_j\le b_{m-1}=B_m.
\]

Across all \(t\) coordinates, the degree sum is at most \(tB_m\). But (3) gives
\[
\dim W=k-j\ge tB_m+m-j>tB_m.
\]
The polynomial zero lemma supplies a nonzero common zero \(v\in W\) of (5).

Then \(U_{j+1}=U_j+\langle v\rangle\) has dimension \(j+1\), and \(P\) is affine on it. Iterating constructs \(U_m\). ∎

### Deduction of the upper bound

If \(\Gamma_P\) is \(m\)-flat-free, the proposition implies
\[
k\le m-1+tB_m.
\]
Since \(n=k+t\),
\[
n\le m-1+tH_m,
\qquad
t\ge\frac{n-m+1}{H_m}.
\]
It follows that
\[
|\Gamma_P|=3^k=3^{n-t}
\le
3^{(m-1)/H_m}N^{1-1/H_m}.
\]
Affine transformations preserve both cardinality and flat-freeness, proving the upper bound in (1).

## 5. Random polynomial graphs give the matching base

Let
\[
q=3^m,
\qquad
s=q-m-1>0.
\]
For a given \(n\), choose
\[
k=\left\lfloor\frac{s}{q}n\right\rfloor,
\qquad
t=n-k.
\tag{7}
\]

Choose the coordinates of
\[
P:\mathbb F_3^k\longrightarrow\mathbb F_3^t
\]
independently and uniformly from the vector space of polynomial functions of degree at most \(2m\).

### Uniformity of restriction to a fixed flat

Fix an affine \(m\)-flat \(W\subseteq\mathbb F_3^k\). Restriction from degree-\(\le2m\) polynomial functions on \(\mathbb F_3^k\) to functions on \(W\) is surjective.

To see this, identify \(W\) affinely with \(\mathbb F_3^m\). Every function on \(\mathbb F_3^m\) has a reduced polynomial representative with individual exponents at most \(2\), hence total degree at most \(2m\). The affine coordinate functions on \(W\) extend to affine functions on the ambient domain. Composing gives the required extension.

Thus \(P|_W\) is uniformly distributed among all maps
\[
W\longrightarrow\mathbb F_3^t.
\]
There are \(3^{qt}\) such maps, of which \(3^{(m+1)t}\) are affine. Hence
\[
\Pr(P|_W\text{ is affine})=3^{-st}.
\tag{8}
\]

### Counting bad flats

For \(k\ge m\), the number of affine \(m\)-flats in \(\mathbb F_3^k\) is
\[
L_{k,m}
=
3^{k-m}
\prod_{i=0}^{m-1}
\frac{3^k-3^i}{3^m-3^i}.
\]
In particular,
\[
L_{k,m}\le \kappa_m3^{(m+1)k},
\qquad
\kappa_m=
\frac{3^{-m}}{\prod_{i=0}^{m-1}(3^m-3^i)}<1.
\]
By (8), the expected number of \(m\)-flats on which \(P\) is affine is at most
\[
\kappa_m3^{(m+1)k-st}
=
\kappa_m3^{qk-sn}
\le\kappa_m<1,
\]
where the final inequality follows from (7).

Some \(P\) therefore has no such flat. Its graph is \(m\)-flat-free and has size
\[
3^k\ge\frac13\,3^{sn/q}
=
\frac13 N^{1-(m+1)/3^m}.
\]
If \(k<m\), every graph over \(\mathbb F_3^k\) is already \(m\)-flat-free, so the same size conclusion holds. This completes the proof of (1). ∎

## 6. Extension to other degree bounds

The refined degree calculation above is not needed to obtain the exponential base.

For a map of degree at most \(D\), at induction stage \(j\) there are at most
\[
t(2\cdot3^j-1)
\]
coefficient equations, each of degree at most \(D\). The same argument therefore gives:

### Corollary
Every \(m\)-flat-free degree-\(\le D\) polynomial graph satisfies
\[
|\Gamma_P|
\le
3^{(m-1)/K_{m,D}}
N^{1-1/K_{m,D}},
\qquad
K_{m,D}=1+D(2\cdot3^{m-1}-1).
\tag{9}
\]

In particular, the conjectured upper-bound direction holds for polynomial graphs whose degree bound \(D_m\) satisfies
\[
\log D_m=o(m),
\]
with \(D_m\) independent of \(n\).

If additionally \(D_m\ge2m\), the random construction above belongs to the class, so its exponent deficit has exactly exponential base \(3\).

### A check at \(m=1\)

For quadratic graphs, the upper argument gives \(k\le2t\). This is sharp.

Partition the \(k\) input coordinates into \(t\) blocks of size at most two, and let each output coordinate be the sum of squares in its block. A block of size at most two has zero sum of squares over \(\mathbb F_3\) only when all its entries vanish. Thus \(P(d)=0\) only for \(d=0\).

For this homogeneous quadratic map,
\[
P(x)+P(x+d)+P(x-d)=2P(d).
\]
Its graph consequently contains no affine line. Choosing
\[
k=\lfloor2n/3\rfloor,\qquad t=n-k
\]
shows that
\[
R_2(n,1)=3^{\lfloor2n/3\rfloor}.
\]

## 7. What remains missing

The theorem rules out polynomial graphs of subexponential-in-\(m\) degree as counterexamples to the proposed base \(3\).

It does not control arbitrary subsets:

1. An arbitrary \(m\)-flat-free set need not be a full graph.
2. Even an arbitrary full graph need not have bounded-degree coordinate functions. A function on \(\mathbb F_3^k\) can require degree \(2k\).
3. Substituting a degree bound growing linearly with \(n\) into (9) gives no positive exponent deficit independent of \(n\).

Most importantly,
\[
R_{2m}(n,m)\le r(n,m);
\]
an upper bound for the smaller class is not an upper bound for \(r(n,m)\).

Thus the unrestricted assertion
\[
\varepsilon_m^*\ge3^{-m-o(m)}
\]
remains unproved here. The rigorous progress is the matching base-\(3\) theorem for a concrete algebraic family, including a self-contained flat-forcing argument and a matching exponential-scale construction.