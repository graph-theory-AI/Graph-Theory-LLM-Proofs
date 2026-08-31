```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I do not prove the polynomial upper bound, but obtain an exact Sidon-type reformulation, an explicit Ω(n^{1/3}) construction, and an n^{2/5} upper bound for relatively Fourier-uniform sets.",
  "would_publish": false,
  "caveats": "The unconditional upper bound remains o(sqrt(n)); the Fourier argument does not control arithmetically structured sets, and no novelty claim is made for the lower-bound construction."
}
```

# 1. Statement and convention

Let \(r(n)\) denote the largest size of \(A\subseteq [n]\) such that every solution in \(A^5\) of
\[
x_1+x_2+2x_3=x_4+3x_5                                      \tag{1}
\]
is trivial.

Here the zero-sum proper subsets of the coefficient sequence
\[
(1,1,2,-1,-3)
\]
give precisely the following two trivial patterns:
\[
x_1=x_4,\qquad x_2=x_3=x_5,                                 \tag{T1}
\]
or
\[
x_2=x_4,\qquad x_1=x_3=x_5.                                 \tag{T2}
\]
The all-equal solutions belong to both classes.

The source paper proves
\[
r(n)=o(\sqrt n).
\]
The question is whether there exists an absolute \(\varepsilon>0\) such that
\[
r(n)=O\bigl(n^{1/2-\varepsilon}\bigr).                       \tag{2}
\]

I do not prove (2). I give three rigorous partial results.

---

# 2. An exact Sidon-type reformulation

## Proposition 2.1

If \(A\) has no nontrivial solution of (1), then \(A\) is a Sidon set: every equality
\[
a+b=c+d,\qquad a,b,c,d\in A,
\]
satisfies
\[
\{a,b\}=\{c,d\}
\]
as multisets.

### Proof

Given \(a+b=c+d\), set
\[
(x_1,x_2,x_3,x_4,x_5)=(a,b,d,c,d).
\]
Then
\[
x_1+x_2+2x_3=a+b+2d=c+3d=x_4+3x_5.
\]
If this solution has type (T1), then \(a=c\) and \(b=d\). If it has type (T2), then \(b=c\) and \(a=d\). These are exactly the two trivial Sidon equalities. ∎

In particular,
\[
E(A):=\#\{a+b=c+d:\ a,b,c,d\in A\}=2|A|^2-|A|.              \tag{3}
\]

Define the off-diagonal set
\[
T^*(A):=\{3u-2v:\ u,v\in A,\ u\ne v\}.
\]

## Proposition 2.2

A set \(A\subseteq\mathbb Z\) is solution-free for (1) if and only if

1. \(A\) is Sidon, and
2. 
   \[
   T^*(A)\cap(A+A-A)=\varnothing.                            \tag{4}
   \]

Consequently, every solution-free set satisfies
\[
(3A-2A)\cap(A+A-A)=A.                                       \tag{5}
\]

### Proof

Suppose first that \(A\) is solution-free. It is Sidon by Proposition 2.1. If
\[
3u-2v=a+b-c
\]
with \(u\ne v\), then
\[
a+b+2v=c+3u
\]
is a solution of (1) with \(x_3=v\ne u=x_5\). Both trivial patterns have \(x_3=x_5\), so this is nontrivial, a contradiction. Thus (4) holds.

Conversely, suppose that \(A\) is Sidon and (4) holds. Consider a solution of (1).

If \(x_3=x_5\), then
\[
x_1+x_2=x_4+x_5.
\]
The Sidon property gives either
\[
x_1=x_4,\quad x_2=x_5=x_3,
\]
or
\[
x_2=x_4,\quad x_1=x_5=x_3,
\]
so the solution is trivial.

If \(x_3\ne x_5\), then
\[
3x_5-2x_3=x_1+x_2-x_4
\]
belongs to both \(T^*(A)\) and \(A+A-A\), contradicting (4).

Finally, the diagonal choices \(u=v\) show \(A\subseteq 3A-2A\), and clearly \(A\subseteq A+A-A\). On the other hand, (4) excludes every off-diagonal element of \(3A-2A\) from \(A+A-A\), proving (5). ∎

This formulation isolates the difficulty: two naturally quadratic-sized derived sets must be disjoint.

Indeed, if \(m=|A|\), then
\[
|A+A-A|\ge |A+A|=\frac{m(m+1)}2.                            \tag{6}
\]
Also,
\[
|3A-2A|\ge \frac{m^2}{2}.                                   \tag{7}
\]
To verify (7), let \(r(z)\) count representations \(z=3a-2b\). There are \(m^2\) representations in total. The energy
\[
\sum_z r(z)^2
=\#\{3a-2b=3a'-2b'\}
\]
is at most \(2m^2-m\): the \(a=a'\) solutions contribute \(m^2\), while for each ordered pair \(a\ne a'\), the Sidon property permits at most one ordered pair \((b,b')\) satisfying
\[
2(b-b')=3(a-a').
\]
Cauchy–Schwarz gives (7).

Both sets in (4) lie in an interval of length \(O(n)\), so cardinality alone recovers only \(m=O(\sqrt n)\). Any polynomial improvement must exploit more than their sizes.

---

# 3. A construction of size \(\boldsymbol{\Omega(n^{1/3})}\)

The next result constrains the possible value of \(\varepsilon\).

## Theorem 3.1

There is an absolute constant \(c>0\) such that, for all sufficiently large \(n\),
\[
r(n)\ge c n^{1/3}.                                          \tag{8}
\]
Consequently, an upper bound of the form (2), if true, must have
\[
\varepsilon\le \frac16.                                     \tag{9}
\]

The construction uses the first three moments.

## Lemma 3.2: moment rigidity

Let \(F\) be a field of characteristic greater than \(3\) in which \(-2\) is not a square. Suppose \(t_1,\dots,t_5\in F\) satisfy
\[
t_1^j+t_2^j+2t_3^j=t_4^j+3t_5^j,\qquad j=1,2,3.             \tag{10}
\]
Then either
\[
t_1=t_4,\qquad t_2=t_3=t_5,
\]
or
\[
t_2=t_4,\qquad t_1=t_3=t_5.
\]

### Proof

Consider
\[
P(X)=(X-t_1)(X-t_2)(X-t_3)^2
\]
and
\[
Q(X)=(X-t_4)(X-t_5)^3.
\]
The identities (10), together with Newton's identities, imply that \(P\) and \(Q\) have the same first three elementary symmetric coefficients. Hence they differ only in their constant terms, and therefore
\[
P'(X)=Q'(X).                                                 \tag{11}
\]

Write \(u=t_4\) and \(v=t_5\). Then
\[
Q'(X)=(X-v)^2\bigl(4X-v-3u\bigr).
\]
Since \(t_3\) is a double root of \(P\), equation (11) gives
\[
t_3=v
\quad\text{or}\quad
t_3=\frac{v+3u}{4}.                                         \tag{12}
\]

If \(t_3=v\), then \(P(v)=Q(v)=0\). Since \(P-Q\) is constant, it follows that \(P=Q\). Thus
\[
\{t_1,t_2,t_3,t_3\}=\{t_4,t_5,t_5,t_5\}
\]
as multisets, which gives precisely the two asserted trivial patterns.

It remains to exclude the second case in (12). Assume \(u\ne v\) and set
\[
z=\frac{X-v}{u-v}.
\]
Then \(t_3=(v+3u)/4\) corresponds to \(z=3/4\). Since \(P-Q\) is constant and \(P(t_3)=0\),
\[
P(X)=Q(X)-Q(t_3).
\]
After division by \((u-v)^4\), this polynomial is
\[
z^4-z^3+\frac{27}{256}
  =\left(z-\frac34\right)^2
   \left(z^2+\frac12z+\frac{3}{16}\right).                  \tag{13}
\]
The remaining quadratic has discriminant
\[
\frac14-\frac34=-\frac12.
\]
Since \((-1/2)/(-2)=1/4\) is a square, \(-1/2\) is nonsquare whenever \(-2\) is nonsquare. Thus the quadratic in (13) has no root in \(F\), whereas its roots would have to be \(t_1,t_2\) after the affine change of variables. This is impossible. ∎

## Proof of Theorem 3.1

Choose a prime
\[
p\equiv 5\pmod 8.
\]
Then \(-2\) is a nonsquare in \(\mathbb F_p\).

Let
\[
L=\left\lfloor\frac p8\right\rfloor,\qquad
I_0=\{0,1,\dots,L-1\}\subset\mathbb F_p.
\]
Choose shifts \(\mu_1,\mu_2,\mu_3\in\mathbb F_p\), and put
\[
T=\{t\in\mathbb F_p:\ t^j+\mu_j\in I_0\text{ for }j=1,2,3\},
\]
where elements of \(I_0\) are interpreted by their standard integer representatives.

Averaging independently over the three shifts gives
\[
\mathbb E_{\mu_1,\mu_2,\mu_3}|T|
 =p\left(\frac Lp\right)^3
 =\frac{L^3}{p^2}.
\]
Hence some choice of shifts satisfies
\[
|T|\ge \frac{L^3}{p^2}\ge c_0p                              \tag{14}
\]
for an absolute \(c_0>0\).

For \(t\in T\), let
\[
y_j(t)\in I_0
\]
be the standard representative of \(t^j+\mu_j\pmod p\), and define
\[
a(t)=y_1(t)+p\,y_2(t)+p^2y_3(t).
\]
The first coordinate \(y_1(t)=t+\mu_1\pmod p\) is injective in \(t\), so all \(a(t)\) are distinct. Moreover,
\[
0\le a(t)<p^3.
\]

Suppose that five such integers satisfy
\[
a(t_1)+a(t_2)+2a(t_3)=a(t_4)+3a(t_5).                       \tag{15}
\]
For \(j=1,2,3\), put
\[
S_j=y_j(t_1)+y_j(t_2)+2y_j(t_3)-y_j(t_4)-3y_j(t_5).
\]
Equation (15) says
\[
S_1+pS_2+p^2S_3=0.
\]
Because the total positive and negative coefficient weights are both \(4\),
\[
|S_j|\le 4(L-1)<p.
\]
Reducing modulo \(p\) therefore gives \(S_1=0\). Dividing by \(p\) and repeating gives
\[
S_2=S_3=0.
\]
Reducing these identities in \(\mathbb F_p\), and using \(\sum_i c_i=0\) to cancel the shifts \(\mu_j\), yields
\[
t_1^j+t_2^j+2t_3^j=t_4^j+3t_5^j,\qquad j=1,2,3.
\]
Lemma 3.2 shows that the parameters, and hence the integers \(a(t_i)\), have one of the two trivial patterns.

Thus
\[
A_p:=\{a(t)+1:t\in T\}\subseteq[p^3]
\]
is solution-free and has size at least \(c_0p\). The translation by \(1\) is harmless because (1) is translation-invariant.

Finally, the prime number theorem in arithmetic progressions implies that, for every sufficiently large \(X\), there is a prime \(p\equiv5\pmod8\) in \([X,2X]\). Taking \(X=n^{1/3}/2\) gives \(p^3\le n\) and \(p\gg n^{1/3}\). This proves (8). ∎

---

# 4. A polynomial upper bound in a Fourier-uniform special case

The next result identifies a concrete obstruction to a polynomial improvement.

For \(A\subseteq[n]\), write \(m=|A|\), \(\alpha=m/n\), and define the relative Fourier discrepancy
\[
U(A):=
\sup_{\theta\in\mathbb R/\mathbb Z}
\left|
 \sum_{a\in A}e^{2\pi ia\theta}
 -\alpha\sum_{x=1}^n e^{2\pi ix\theta}
\right|.                                                     \tag{16}
\]

## Theorem 4.1

If \(A\subseteq[n]\) is solution-free, then
\[
m^3\le Cn\bigl(1+U(A)\bigr)                                 \tag{17}
\]
for an absolute constant \(C\).

Consequently, if for some \(0<\delta\le1\) and fixed \(K\),
\[
U(A)\le K m^{1-\delta},                                     \tag{18}
\]
then
\[
m\le C_K n^{1/(2+\delta)}.                                  \tag{19}
\]
In particular, the relative Salem-type condition
\[
U(A)\le K\sqrt m
\]
implies
\[
m=O_K(n^{2/5}).                                              \tag{20}
\]

Thus the conjectured polynomial gain holds, with \(\varepsilon=1/10\), for this Fourier-uniform subclass.

### Proof

For finitely supported functions \(f_1,\dots,f_5:\mathbb Z\to\mathbb C\), let
\[
\Lambda(f_1,\dots,f_5)
=
\sum_{x_1+x_2+2x_3=x_4+3x_5}
f_1(x_1)f_2(x_2)f_3(x_3)f_4(x_4)f_5(x_5).
\]
With
\[
\widehat f(\theta)=\sum_x f(x)e^{2\pi ix\theta},
\]
orthogonality gives
\[
\Lambda(f_1,\dots,f_5)
=
\int_0^1
\widehat f_1(\theta)\widehat f_2(\theta)
\widehat f_3(2\theta)
\overline{\widehat f_4(\theta)\widehat f_5(3\theta)}
\,d\theta.                                                   \tag{21}
\]

Put
\[
g=1_A,\qquad h=\alpha 1_{[n]},\qquad f=g-h.
\]
By telescoping the five slots,
\[
\Lambda(g,g,g,g,g)-\Lambda(h,h,h,h,h)
\]
is a sum of five terms, each containing one copy of \(f\), with every other slot occupied by \(g\) or \(h\).

For \(g\), Proposition 2.1 and (3) give
\[
\|\widehat g\|_4^4=2m^2-m.                                  \tag{22}
\]
For \(h\),
\[
\|\widehat h\|_4^4
=\alpha^4E([n])
\le \alpha^4n^3
=\frac{m^4}{n}.                                             \tag{23}
\]
A Sidon set in \([n]\) has distinct positive differences, so
\[
\binom m2\le n-1;
\]
hence \(m^2\le 4n\), say, and (23) is \(O(m^2)\). Thus every \(g\)- or \(h\)-factor in (21) has \(L^4\)-norm \(O(\sqrt m)\). Multiplication of \(\theta\) by \(2\) or \(3\) preserves Haar measure on the circle.

Using the \(L^\infty\)-bound \(U(A)\) for the one \(f\)-factor and Hölder's inequality for the other four factors yields
\[
\left|
\Lambda(g,g,g,g,g)-\alpha^5\Lambda(1_{[n]},\dots,1_{[n]})
\right|
\le C_1 U(A)m^2.                                            \tag{24}
\]

There are at least \(c_1n^4\) solutions of (1) in \([n]^5\). For example, choose \(x_1,x_2,x_3,x_5\) in an interval of radius \(n/100\) around \((n+1)/2\); then
\[
x_4=x_1+x_2+2x_3-3x_5
\]
still lies in \([n]\). Therefore
\[
\alpha^5\Lambda(1_{[n]},\dots,1_{[n]})
\ge c_2\frac{m^5}{n}.                                       \tag{25}
\]

Since \(A\) is solution-free, its only solutions are the \(m^2\) solutions of type (T1) and the \(m^2\) solutions of type (T2), with the \(m\) all-equal solutions counted twice. Hence
\[
\Lambda(g,g,g,g,g)=2m^2-m.                                 \tag{26}
\]
Combining (24)–(26),
\[
c_2\frac{m^5}{n}
\le 2m^2+C_1U(A)m^2.
\]
After division by \(m^2\), this is (17).

Under (18),
\[
m^3\le Cn(1+K)m^{1-\delta},
\]
which gives (19). Taking \(\delta=1/2\) proves (20). ∎

An unconditional consequence of the same calculation is the following structural statement:
\[
U(A)\ge c\,\frac{m^3}{n}-C.                                 \tag{27}
\]
Thus any solution-free set substantially larger than \(n^{1/3}\) must have a large Fourier bias relative to the ambient interval. For instance, if \(m=n^{1/2-\eta}\), then, up to constants,
\[
\frac{U(A)}m\gtrsim \frac{m^2}{n}=n^{-2\eta}.                \tag{28}
\]

---

# 5. What remains open

The argument above leaves a genuine structured alternative. A large value of \(U(A)\) may arise from concentration on a long progression, a Bohr set, or another arithmetically structured subset. Passing to such a subset preserves the original equation and its Sidon consequence, but I do not obtain a density-increment iteration with polynomially controlled losses. Controlling this alternative is precisely what would be needed to turn Theorem 4.1 into an unconditional \(n^{1/2-\varepsilon}\) bound.

The current conclusions are therefore:

\[
c n^{1/3}\le r(n)=o(\sqrt n),
\]
with the lower estimate proved above;

- any successful exponent must satisfy \(\varepsilon\le1/6\);
- relatively Fourier-uniform solution-free sets satisfy the stronger bound
  \[
  |A|=O(n^{2/5});
  \]
- an arbitrary large solution-free set must exhibit the quantitative Fourier structure in (27).

No argument here covers that structured case, so the catalogued conjecture remains unresolved.