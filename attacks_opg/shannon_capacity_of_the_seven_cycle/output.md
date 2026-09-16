```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I determine the optimal affine-linear codes over F7 for block lengths at most 12, but do not determine the unrestricted Shannon capacity of C7.",
  "would_publish": false,
  "caveats": "Restricted-family result, not claimed new; it does not improve the general capacity bounds supplied in the question."
}
```

## 1. Scope and statement of the partial result

I do not close the gap for \(\Theta(C_7)\). The result below concerns independent sets that are affine subspaces over \(\mathbb F_7\), a substantial restriction.

Label the vertices of \(C_7\) by \(\mathbb F_7\), with adjacency given by differences \(\pm1\). Define
\[
A_n=\max\bigl\{|a+L|:\ L\le \mathbb F_7^n,\ 
a+L\text{ is independent in }C_7^{\boxtimes n}\bigr\}.
\]

**Restricted-code theorem.** For \(1\le n\le12\),
\[
\boxed{A_n=7^{\lfloor 3n/5\rfloor}.}
\]
For every \(n\ge1\), the lower bound
\[
A_n\ge 7^{\lfloor 3n/5\rfloor}
\]
holds.

In particular, there is an explicit affine-linear independent set of size \(343\) in \(C_7^{\boxtimes5}\), and no larger affine-linear independent set in that power. This is weaker than the unrestricted \(367\)-word construction reported in the question.

I also show that no finite strong power attains the Lovász upper bound exactly. That observation does **not** establish a strict asymptotic gap.

## 2. Coding formulation

Put
\[
B=\{0,1,-1\}\subseteq\mathbb F_7.
\]
Two distinct words \(u,v\in\mathbb F_7^n\) are adjacent in \(C_7^{\boxtimes n}\) precisely when
\[
u-v\in B^n.
\]
Consequently, a linear subspace \(L\) is independent exactly when
\[
L\cap B^n=\{0\}. \tag{1}
\]
Translations preserve adjacency, so an affine subspace \(a+L\) is independent exactly when \(L\) is independent.

Write
\[
a_n=\alpha(C_7^{\boxtimes n}).
\]
Products of independent sets give \(a_{m+n}\ge a_ma_n\), and hence
\[
\Theta(C_7)=\lim_{n\to\infty}a_n^{1/n}
          =\sup_{n\ge1}a_n^{1/n}.
\]
The factor \(1/n\) inside the displayed definition in the question is harmless: \(n^{-1/n}\to1\).

## 3. An explicit optimal affine-linear five-coordinate code

Consider
\[
L_5=
\left\{
\bigl(x,y,z,\ x+2y+3z,\ 2x-y-3z\bigr):
x,y,z\in\mathbb F_7
\right\}. \tag{2}
\]
Its dimension is three, since its first three coordinates are \(x,y,z\). Thus \(|L_5|=343\).

### Verification of independence

Suppose a word of \(L_5\) belongs to \(B^5\). Its first three coordinates force \(x,y,z\in B\). Set
\[
\ell_1=x+2y+3z,\qquad \ell_2=2x-y-3z.
\]

We must show that no nonzero triple in \(B^3\) makes both \(\ell_1,\ell_2\) belong to \(B\).

Using integer representatives \(x,y,z\in\{-1,0,1\}\), we have \(-6\le\ell_1\le6\). Thus \(\ell_1\in B\) modulo seven means
\[
\ell_1\in\{-6,-1,0,1,6\}
\]
as an integer. Solving these possibilities gives, up to simultaneous negation, exactly the following nonzero triples:
\[
\begin{array}{c|c|c}
(x,y,z)&\ell_1\pmod7&\ell_2\pmod7\\ \hline
(1,0,0)&1&2\\
(1,-1,0)&-1&3\\
(0,1,-1)&-1&2\\
(1,1,1)&-1&-2\\
(1,1,-1)&0&-3
\end{array}
\]
In every case \(\ell_2\notin B\). Therefore
\[
L_5\cap B^5=\{0\},
\]
proving independence. No computer search is used here.

### Optimality within the affine-linear class

There is a useful elementary obstruction.

**Binary-cube injection lemma.** If \(L\le\mathbb F_7^n\) is independent and has dimension \(d\), then
\[
2^n\le 7^{n-d}. \tag{3}
\]

**Proof.** The quotient map
\[
q:\mathbb F_7^n\longrightarrow\mathbb F_7^n/L
\]
is injective on \(\{0,1\}^n\). Indeed, if distinct binary vectors \(u,v\) had \(q(u)=q(v)\), their difference would be a nonzero member of \(L\cap B^n\), contrary to (1). The quotient has \(7^{n-d}\) elements. \(\square\)

For \(n=5\), a dimension of at least four would give
\[
32=2^5\le7^{5-d}\le7,
\]
a contradiction. Thus \(d\le3\), and construction (2) proves
\[
\boxed{A_5=343.}
\]

### Product constructions in every length

The one-dimensional subspace
\[
L_2=\{(x,2x):x\in\mathbb F_7\}
\]
is independent: if \(x\ne0\) and \(x\in B\), then \(2x\notin B\).

Write \(n=5q+r\), where \(0\le r\le4\). Take the product of:

- \(q\) copies of \(L_5\);
- \(\lfloor r/2\rfloor\) copies of \(L_2\);
- one fixed coordinate if \(r\) is odd.

The resulting independent linear subspace has dimension
\[
3q+\lfloor r/2\rfloor
=\left\lfloor\frac{3n}{5}\right\rfloor.
\]
This proves the claimed lower bound for every \(n\).

## 4. A self-contained tensor upper bound

For completeness, the upper bound needed to finish the short-block theorem can be proved directly.

Let
\[
c=\cos(\pi/7),\qquad
\tau=\frac{7c}{1+c}.
\]
I claim that
\[
a_n\le\tau^n\qquad(n\ge1). \tag{4}
\]

Let \(D\) be the adjacency matrix of \(C_7\), and put
\[
M=I+\frac{1}{2c}D.
\]
Its eigenvalues are
\[
1+\frac{\cos(2\pi j/7)}{c},\qquad 0\le j\le6.
\]
The minimum cosine here is \(-c\), so \(M\) is positive semidefinite.

Choose real unit vectors \(u_0,\ldots,u_6\) with Gram matrix \(M\). Distinct nonadjacent vertices receive orthogonal vectors. Every row sum of \(M\) equals
\[
r=1+\frac1c.
\]
Hence
\[
h=\frac{\sum_{i=0}^6u_i}{\sqrt{7r}}
\]
is a unit vector satisfying
\[
\langle h,u_i\rangle=\sqrt{\frac r7}
\]
for every \(i\).

For a word \(x=(x_1,\ldots,x_n)\), assign
\[
U_x=u_{x_1}\otimes\cdots\otimes u_{x_n}.
\]
If \(S\) is independent in \(C_7^{\boxtimes n}\), the vectors \(U_x\), \(x\in S\), are orthonormal: each distinct pair has some coordinate containing distinct nonadjacent vertices of \(C_7\). Bessel’s inequality applied to \(h^{\otimes n}\) gives
\[
|S|\left(\frac r7\right)^n\le1.
\]
Since \(7/r=\tau\), this proves (4), and therefore
\[
\Theta(C_7)\le\tau\approx3.317667.
\]

## 5. Completing the affine-linear theorem through length 12

We need a convenient exact estimate on \(\tau\).

The cosine identity
\[
8c^3-4c^2-4c+1=0
\]
follows by putting \(z=e^{i\pi/7}\), expanding \((z^7+1)/(z+1)=0\), and dividing by \(z^3\). Substituting \(c=\tau/(7-\tau)\) gives
\[
f(\tau)=0,\qquad
f(t)=t^3+7t^2-49t+49. \tag{5}
\]

We have \(\tau>3\), since \(c>\cos(\pi/6)>3/4\). Moreover, \(f\) is strictly increasing for \(t\ge3\), and
\[
f(10/3)=\frac{13}{27}>0.
\]
Thus
\[
\tau<\frac{10}{3}.
\]
Also,
\[
\left(\frac{10}{3}\right)^8<7^5,
\]
as is verified by
\[
100000000<7^5\,3^8=110270727.
\]
Consequently,
\[
\tau<7^{5/8}. \tag{6}
\]

If an independent affine subspace has dimension \(d\), (4) and (6) imply
\[
7^d\le a_n\le\tau^n<7^{5n/8},
\]
so
\[
d<\frac{5n}{8}. \tag{7}
\]
For \(1\le n\le12\), the resulting integer upper bounds are
\[
\begin{array}{c|rrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
d\text{ at most}&0&1&1&2&3&3&4&4&5&6&6&7
\end{array}
\]
and these are exactly \(\lfloor3n/5\rfloor\). The product constructions from Section 3 attain every entry. This proves
\[
A_n=7^{\lfloor3n/5\rfloor}\qquad(1\le n\le12).
\]

In particular, concatenating affine-linear blocks of lengths at most twelve cannot achieve a rate exceeding
\[
7^{3/5}\approx3.214096,
\]
and repeating \(L_5\) attains that rate within this construction class. This does not bound affine-linear codes of arbitrary block length by the same rate.

## 6. No finite power attains the Lovász bound

There is an algebraic obstruction to reproducing the finite-block phenomenon of \(C_5\).

The polynomial \(f\) in (5) is irreducible over \(\mathbb Q\): modulo three it is
\[
t^3+t^2+2t+1,
\]
which has no root in \(\mathbb F_3\).

Another root of \(f\) is
\[
\tau'=
\frac{7\cos(3\pi/7)}{1+\cos(3\pi/7)},
\]
with
\[
0<\tau'<\tau.
\]
If \(\tau^n\) were rational for some positive integer \(n\), the minimal polynomial \(f\) would divide \(t^n-\tau^n\). It would follow that
\[
(\tau')^n=\tau^n,
\]
a contradiction. Thus every positive integer power of \(\tau\) is irrational.

Since \(a_n\) is an integer, we obtain
\[
\boxed{a_n\le\lfloor\tau^n\rfloor<\tau^n
\quad\text{for every finite }n.}
\]

Crucially, this does **not** imply \(\Theta(C_7)<\tau\): indeed,
\[
\lim_{n\to\infty}\lfloor\tau^n\rfloor^{1/n}=\tau.
\]
A strict inequality at each finite block length need not yield a strict asymptotic inequality.

## 7. What remains unresolved

The arguments above leave the central problem open:

- They give no improvement on the upper bound for arbitrary independent sets.
- The affine-linear theorem does not constrain nonlinear constructions such as the larger five-coordinate code reported in the question.
- Even within affine-linear codes, the argument stops being exact at length thirteen: it gives an achievable dimension of seven and an upper bound of eight.
- Finite-block nonattainment of \(\tau\) supplies no uniform asymptotic separation.

Using the \(367\)-word construction reported in the supplied literature summary, the outstanding interval therefore remains
\[
\boxed{
367^{1/5}\approx3.2578
\ \le\ \Theta(C_7)\
\le\ \frac{7\cos(\pi/7)}{1+\cos(\pi/7)}
\approx3.3177.
}
\]
The restricted-code theorem is fully proved above, but it is not asserted to be new and is not a resolution of the Shannon-capacity problem.