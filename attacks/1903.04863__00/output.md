```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The near-linear question remains open, but the example has an explicit Omega(sqrt(N)) construction, while the natural quadratic-graph method cannot exceed exponent one half.",
  "would_publish": false,
  "caveats": "Avoidance is interpreted as allowing only x=y=w=z; the broader informal class of coefficient patterns is not resolved."
}
```

## 1. Precise formulation

Taken literally, every nonempty set contains a solution, since
\[
2a+2a=3a+a.
\]
I therefore use the natural “genus-one” convention that these diagonal solutions are trivial. Define
\[
r_E(N)=\max\bigl\{|A|:A\subseteq[N],\ 
2x+2y=3w+z,\ x,y,w,z\in A
\Longrightarrow x=y=w=z\bigr\}.
\]

The catalog question asks whether
\[
r_E(N)=N^{1-o(1)}.
\]
I do not resolve this. I prove
\[
\left(\frac12-o(1)\right)\sqrt N\le r_E(N)=o(N),
\]
give an explicit obstruction to the ordinary sphere argument, and prove a barrier showing why quadratic finite-field graph constructions do not improve the exponent \(1/2\).

---

## 2. A finite-field parabola construction

### Lemma 2.1

Let \(p\ne2,3\) be a prime for which \(3\) is a quadratic nonresidue modulo \(p\). Then
\[
P_p=\{(t,t^2):t\in\mathbb F_p\}\subseteq\mathbb F_p^2
\]
has only diagonal solutions to
\[
2X+2Y=3W+Z.
\]

### Proof

Suppose that the four points corresponding to \(x,y,w,z\in\mathbb F_p\) satisfy the equation in both coordinates. Thus
\[
2x+2y=3w+z                                      \tag{2.1}
\]
and
\[
2x^2+2y^2=3w^2+z^2.                              \tag{2.2}
\]
Set
\[
u=x+y-2w,\qquad v=x-y.
\]
Using \(z=2x+2y-3w\), direct expansion gives
\[
2x^2+2y^2-3w^2-z^2=v^2-3u^2.
\]
Consequently,
\[
v^2=3u^2.
\]
Since \(3\) is a nonsquare, this implies \(u=v=0\). Hence \(x=y\), and then \(x+y=2w\) gives \(w=x\); equation (2.1) finally gives \(z=x\). ∎

---

## 3. Lifting the parabola to the integers

### Proposition 3.1

For every prime \(p\equiv5\pmod {12}\),
\[
r_E(4p^2)\ge p.
\]

### Proof

For \(t\in\{0,\dots,p-1\}\), let \(q(t)\in\{0,\dots,p-1\}\) be the least residue of \(t^2\pmod p\). Put
\[
B=4p,\qquad
A_p=\{\,1+t+Bq(t):0\le t<p\,\}.
\]
The elements are distinct, and
\[
A_p\subseteq[\,4p^2-3p\,]\subseteq[4p^2].
\]

Suppose
\[
2a_x+2a_y=3a_w+a_z
\]
for four elements of \(A_p\). Translation by \(1\) cancels because the coefficients sum to zero. We obtain
\[
D_0+B D_1=0,
\]
where
\[
D_0=2x+2y-3w-z
\]
and
\[
D_1=2q(x)+2q(y)-3q(w)-q(z).
\]
Since \(0\le x,y,w,z<p\),
\[
|D_0|\le4(p-1)<B.
\]
But \(D_0\) is a multiple of \(B\), so \(D_0=0\), and hence \(D_1=0\).

Reducing these two equalities modulo \(p\) gives
\[
2x+2y=3w+z,\qquad
2x^2+2y^2=3w^2+z^2
\]
in \(\mathbb F_p\). For \(p\equiv5\pmod {12}\), \(3\) is a quadratic nonresidue. Lemma 2.1 therefore gives
\[
x=y=w=z,
\]
and hence the original four integers are equal. ∎

The prime number theorem in arithmetic progressions supplies, for every sufficiently large \(N\), a prime
\[
p\equiv5\pmod {12},\qquad
p=(1-o(1))\frac{\sqrt N}{2},
\]
with \(4p^2\le N\). Therefore:

### Corollary 3.2

\[
r_E(N)\ge\left(\frac12-o(1)\right)\sqrt N.
\]

This construction is stronger than merely forbidding solutions with four distinct entries: it forbids every solution except \(x=y=w=z\).

---

## 4. General weighted-parabola principle

The finite-field argument is not peculiar to the numbers \(2,2,3,1\). Suppose
\[
ax+by=cw+dz,\qquad a+b=c+d=S,
\]
and impose the corresponding square relation
\[
ax^2+by^2=cw^2+dz^2.
\]
The identity
\[
S(ax^2+by^2)-(ax+by)^2=ab(x-y)^2
\]
and its \(w,z\) analogue give
\[
ab(x-y)^2=cd(w-z)^2.                              \tag{4.1}
\]
Thus, over a field where \(cd/(ab)\) is a nonsquare and all relevant coefficients are nonzero, equation (4.1) forces \(x=y\) and \(w=z\), and the first-moment equation then forces all four variables to agree.

For the present equation,
\[
\frac{cd}{ab}=\frac{3}{4},
\]
whose square class is that of \(3\).

---

## 5. An upper bound inherited from Roth's theorem

If \(A\) contains a nonconstant three-term arithmetic progression
\[
a-d,\ a,\ a+d,
\]
then setting
\[
x=a-d,\qquad y=a+d,\qquad w=z=a
\]
gives
\[
2x+2y=4a=3w+z.
\]
Hence every \(E\)-free set in the above all-equal sense is also three-term-progression-free. The standard form of Roth's theorem therefore gives
\[
r_E(N)=o(N).
\]

This does not answer the catalog question: a Behrend-size set
\[
N\exp(-O(\sqrt{\log N}))
\]
is simultaneously \(o(N)\) and \(N^{1-o(1)}\).

If “nontrivial” were instead defined to mean “four pairwise distinct variables,” this Roth implication would not apply because the displayed solution has \(w=z\).

---

## 6. Why the ordinary Behrend sphere argument fails

The failure is not merely a vague absence of convexity. There is an explicit nontrivial solution consisting of four integer vectors on the same Euclidean sphere.

Let
\[
\begin{aligned}
X&=(3,1,0,1,3,4),\\
Y&=(3,4,3,1,0,1),\\
W&=(4,3,1,0,1,3),\\
Z&=(0,1,3,4,3,1).
\end{aligned}
\]
A coordinatewise check gives
\[
2X+2Y=3W+Z.
\]
Moreover, all four vectors are permutations of
\[
(4,3,1,0,1,3),
\]
and hence
\[
\|X\|_2^2=\|Y\|_2^2=\|W\|_2^2=\|Z\|_2^2=36.
\]

One conceptual description is to put
\[
a_j=2+2\cos\frac{\pi j}{3},\qquad j\in\mathbb Z/6\mathbb Z,
\]
and take
\[
X_j=a_{j+1},\quad Y_j=a_{j-1},\quad W_j=a_j,\quad Z_j=a_{j+3}.
\]
Then
\[
2a_{j+1}+2a_{j-1}=3a_j+a_{j+3}.
\]

In fact, because the four vectors have the same coordinate multiset, they have the same value of every symmetric separable statistic
\[
\sum_i \phi(v_i).
\]
Thus simply adding further symmetric moment constraints to the usual sphere layer cannot rule out this particular configuration. This does not prove that every possible sphere fiber fails, but it rules out the standard strict-convexity certification used for three-term progressions.

---

## 7. A rigorous quadratic-graph barrier

The preceding construction comes from the quadratic graph \(t\mapsto t^2\). The following shows that a full-domain quadratic graph cannot improve its dimension ratio.

### Proposition 7.1

Let \(\mathbb F_q\) have characteristic different from \(2,3\), and let
\[
Q:\mathbb F_q^d\longrightarrow\mathbb F_q^r
\]
have coordinate polynomials of degree at most \(2\). If its graph
\[
\Gamma_Q=\{(t,Q(t)):t\in\mathbb F_q^d\}
\]
has only diagonal solutions to
\[
2X+2Y=3W+Z,
\]
then
\[
r\ge d.
\]

### Proof

Write \(H=(H_1,\dots,H_r)\) for the homogeneous quadratic part of \(Q\). For \(u,v\in\mathbb F_q^d\), consider
\[
G_j(u,v)=H_j(v)-3H_j(u),\qquad 1\le j\le r.
\]
These are \(r\) homogeneous quadratic equations in \(2d\) variables.

If \(d>r\), then
\[
\sum_{j=1}^r\deg G_j\le2r<2d.
\]
By the Chevalley–Warning theorem, the number of common zeros is divisible by the characteristic. Since the zero vector is a common zero, there must be a nonzero common zero \((u,v)\).

Now set
\[
w=0,\qquad
x=\frac{u+v}{2},\qquad
y=\frac{u-v}{2},\qquad
z=2u.
\]
Then
\[
2x+2y=3w+z.
\]
The constant and linear parts of \(Q\) cancel in the same affine relation, while the quadratic parallelogram identity gives
\[
2Q(x)+2Q(y)-3Q(0)-Q(2u)=H(v)-3H(u)=0.
\]
Thus the corresponding four points of \(\Gamma_Q\) form a non-diagonal solution, a contradiction. Therefore \(r\ge d\). ∎

Since
\[
|\Gamma_Q|=q^d,\qquad
|\mathbb F_q^{d+r}|=q^{d+r},
\]
the proposition gives
\[
\frac{\log_q|\Gamma_Q|}{d+r}
=\frac{d}{d+r}\le\frac12.
\]
Consequently, a standard coordinatewise no-carry lift of a quadratic graph cannot yield an integer exponent exceeding \(1/2\). The parabola construction attains this barrier with \(d=r=1\).

This is only a method barrier. It does not apply to high-degree graphs, asymmetric digit constructions, non-graph varieties, or other possible Behrend-style mechanisms.

---

## 8. Remaining gap

The established bounds are
\[
\left(\frac12-o(1)\right)\sqrt N
\le r_E(N)
=o(N).
\]
Nothing here distinguishes between an actual extremal size \(N^{1/2+o(1)}\) and the conjectural \(N^{1-o(1)}\). The explicit sphere configuration shows why the direct Behrend proof breaks, while Proposition 7.1 shows that merely replacing the sphere by a quadratic finite-field graph cannot cross exponent \(1/2\).

Thus the near-linear construction requested in the catalog remains open under the natural all-equal notion of triviality.