```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Exponential decay holds for an explicit family S in F_{p^2} of size (p^2+6p-3)/4, including a balanced boundary example in F_25.",
  "would_publish": false,
  "caveats": "This is a structured-set result, not a uniform cardinality improvement; novelty relative to the full source paper is unchecked."
}
```

# 1. A structured improvement below the threshold

Call \(A\subseteq \mathbb F_q^n\) **\(S\)-difference-free** if there are no
\[
x,\quad x+d,\quad x+2d\in A,
\qquad 0\ne d\in S^n.
\]

The general problem is not solved here. I prove an explicit family of additional cases, including a boundary case that is outside the additive-subgroup half-density criterion in the previous attempt.

## Theorem

Let \(p\ge 5\) be prime, and identify the additive group of \(\mathbb F_{p^2}\) with \(\mathbb F_p^2\). Put
\[
m=\frac{p-3}{2},\qquad R=\{1,2,\ldots,m\}\subseteq\mathbb F_p,
\]
and define
\[
S_p=\{(u,v)\in\mathbb F_p^2:
u\notin R,\ v\notin R,\ u+v\ne -2\}.
\tag{1}
\]
Then:

1. \(0\in S_p\), and
   \[
   |S_p|=\frac{p^2+6p-3}{4}.
   \tag{2}
   \]

2. Every \(S_p\)-difference-free \(A\subseteq\mathbb F_{p^2}^n\) satisfies
   \[
   |A|\le p^{2n}\exp\!\left(-\frac{n}{9(p-1)^2}\right).
   \tag{3}
   \]
   Thus the desired exponential density bound holds.

3. For every nontrivial additive subgroup \(H\le\mathbb F_{p^2}\),
   \[
   |S_p\cap H|\le \frac{|H|+1}{2}.
   \tag{4}
   \]
   Consequently, the local half-density sufficient condition from the previous attempt does not apply.

For \(p=5\), this gives
\[
S_5=\{(u,v)\in\mathbb F_5^2:u\ne1,\ v\ne1,\ u+v\ne3\},
\tag{5}
\]
with
\[
|S_5|=13=\frac{25+1}{2}.
\]
Moreover, every one-dimensional \(\mathbb F_5\)-subspace meets \(S_5\) in exactly \(3\) points: this is a balanced boundary example.

For \(p>5\), the family lies strictly below the boundary, since
\[
\frac{p^2+1}{2}-|S_p|
=\frac{(p-1)(p-5)}4>0.
\tag{6}
\]
For example, the construction gives sets of sizes \(22\) in \(\mathbb F_{49}\) and \(46\) in \(\mathbb F_{121}\). As \(p\) grows, \(|S_p|/p^2\) tends to \(1/4\).

The proof uses low-degree polynomials in **prime-field coordinates**, rather than just the cardinality of \(S\).

# 2. A low-degree certificate criterion

## Proposition

Let \(q=p^k\), where \(p\) is an odd prime, and identify \(\mathbb F_q\) additively with \(\mathbb F_p^k\). Suppose there is a polynomial
\[
P\in\mathbb F_p[X_1,\ldots,X_k]
\]
of total degree \(d\) such that
\[
P(0)\ne0,\qquad
P(v)=0\quad\text{for every }v\notin S,
\tag{7}
\]
and
\[
d<\frac{k(p-1)}2.
\tag{8}
\]
Then every \(S\)-difference-free \(A\subseteq\mathbb F_q^n\) satisfies
\[
|A|\le q^n e^{-\eta n},
\qquad
\eta=
\frac{2\bigl(k(p-1)/2-d\bigr)^2}
     {9k(p-1)^2}>0.
\tag{9}
\]

A slightly stronger, implicitly optimized bound is
\[
|A|\le
\left[
\inf_{0<t<1}
\frac{(1+t+\cdots+t^{p-1})^k}
     {t^{(k(p-1)+d)/3}}
\right]^n,
\tag{10}
\]
whose bracket is strictly smaller than \(q\).

### Proof

Write each coordinate of \(x\in\mathbb F_q^n\) as
\[
x_i=(x_{i1},\ldots,x_{ik})\in\mathbb F_p^k.
\]
Consider the tensor
\[
T(x,y,z)=
\prod_{i=1}^n
\left[
P(y_i-x_i)
\prod_{j=1}^k
\left(1-(x_{ij}+z_{ij}-2y_{ij})^{p-1}\right)
\right].
\tag{11}
\]

The second product is the indicator of \(x+z=2y\). By (7), \(T(x,y,z)\) can be nonzero only if
\[
x+z=2y,\qquad y-x\in S^n.
\]
Therefore, on \(A^3\), progression-freeness implies
\[
T(x,y,z)=
\begin{cases}
P(0)^n,&x=y=z,\\
0,&\text{otherwise}.
\end{cases}
\tag{12}
\]

We use the standard diagonal slice-rank fact:
\[
\operatorname{srank}(T|_{A^3})=|A|.
\tag{13}
\]

For completeness, its lower bound follows by elementary linear algebra. Suppose a nonzero diagonal tensor on an \(N\)-element index set is expressed using \(r_x,r_y,r_z\) slices of the three respective types. The annihilator of the \(x\)-slice factors contains a vector \(h\) with at least \(N-r_x\) nonzero coordinates: any subspace of dimension \(d\) has a coordinate projection onto \(d\) coordinates that is an isomorphism, and one may prescribe all those coordinates to be \(1\). Contracting against \(h\) produces a diagonal matrix of rank at least \(N-r_x\), while the remaining slices give rank at most \(r_y+r_z\). Hence
\[
N\le r_x+r_y+r_z.
\]

The polynomial in (11) has total degree at most
\[
\bigl(k(p-1)+d\bigr)n.
\tag{14}
\]
Reduce its individual variable degrees to at most \(p-1\), using \(X^p=X\) as an identity of functions on \(\mathbb F_p\). This does not increase total degree.

Set
\[
\beta=\frac{k(p-1)+d}{3}.
\]
In every resulting monomial, one of the three variable blocks \(x,y,z\) has degree at most \(\beta n\). Assign each monomial to such a block and group by its monomial in that block. This yields
\[
|A|\le 3M_n,
\tag{15}
\]
where
\[
M_n=
\#\left\{
(a_1,\ldots,a_{kn})\in\{0,\ldots,p-1\}^{kn}:
\sum_{\ell=1}^{kn}a_\ell\le\beta n
\right\}.
\tag{16}
\]

For \(0<t<1\),
\[
M_n\le
t^{-\beta n}(1+t+\cdots+t^{p-1})^{kn}.
\tag{17}
\]
The logarithmic derivative of the bracket in (10), at \(t=1\), is
\[
\frac{k(p-1)}2-\beta
=\frac{k(p-1)/2-d}{3}>0.
\]
Thus taking \(t<1\) sufficiently close to \(1\) gives an exponential saving.

Here is an explicit estimate. Let
\[
\Delta=\frac{k(p-1)}2-\beta>0.
\]
If \(U\) is uniform on \(\{0,\ldots,p-1\}\), symmetry gives, for \(\lambda\ge0\),
\[
\mathbb E e^{-\lambda(U-(p-1)/2)}
\le \cosh\!\left(\frac{\lambda(p-1)}2\right)
\le \exp\!\left(\frac{\lambda^2(p-1)^2}{8}\right).
\tag{18}
\]
Applying this independently to \(kn\) variables,
\[
M_n\le q^n
\exp\!\left(
-\lambda\Delta n+
\frac{kn\lambda^2(p-1)^2}{8}
\right).
\]
Taking
\[
\lambda=\frac{4\Delta}{k(p-1)^2}
\]
gives
\[
M_n\le q^n
\exp\!\left(-\frac{2\Delta^2}{k(p-1)^2}n\right)
=q^n e^{-\eta n}.
\tag{19}
\]

Finally, the factor \(3\) in (15) can be removed. For every positive integer \(\ell\), the Cartesian power \(A^\ell\) is \(S\)-difference-free in dimension \(n\ell\): a nonzero allowed difference has a nonzero block, which would give a forbidden progression in \(A\). Hence
\[
|A|^\ell\le 3q^{n\ell}e^{-\eta n\ell}.
\]
Take \(\ell\)-th roots and let \(\ell\to\infty\). This proves (9), and the same argument proves (10). \(\square\)

# 3. Verification of the explicit family

We now prove all assertions of the theorem.

## 3.1 The polynomial certificate

For \(S_p\) defined in (1), take
\[
P(U,V)
=(U+V+2)
\prod_{a=1}^m(U-a)(V-a).
\tag{20}
\]
It is nonzero precisely on \(S_p\), and
\[
P(0,0)=2(m!)^2\ne0
\]
in \(\mathbb F_p\). Its degree is
\[
d=2m+1=p-2.
\]
Since \(k=2\), the cutoff in (8) is \(p-1\), so the inequality is strict.

The proposition gives
\[
\eta
=
\frac{2((p-1)-(p-2))^2}{9\cdot2(p-1)^2}
=\frac1{9(p-1)^2},
\]
which proves (3).

Only the additive identification \(\mathbb F_{p^2}\cong\mathbb F_p^2\) is used: it preserves addition and doubling, and therefore preserves the progressions under consideration.

## 3.2 Cardinality

Let
\[
B=\mathbb F_p\setminus R,
\qquad |B|=\frac{p+3}{2}.
\]
The set \(S_p\) is \(B^2\) with the points on \(u+v=-2\) removed.

For a point on this line to belong to \(B^2\), its first coordinate must avoid
\[
R\cup(-2-R).
\]
Using the usual representatives,
\[
R=\{1,\ldots,m\},\qquad
-2-R=\{m+1,\ldots,2m\}.
\]
Thus exactly three first coordinates remain: \(0,-2,-1\). The removed points are precisely
\[
(0,-2),\qquad(-2,0),\qquad(-1,-1).
\]
Consequently,
\[
|S_p|=|B|^2-3
=\left(\frac{p+3}{2}\right)^2-3
=\frac{p^2+6p-3}{4}.
\]

## 3.3 No additive subgroup is more than half dense

The nontrivial proper additive subgroups of \(\mathbb F_{p^2}\) are the one-dimensional \(\mathbb F_p\)-subspaces.

The vertical line and the horizontal line each meet \(S_p\) in
\[
p-m-1=\frac{p+1}{2}
\]
points. The same is true of the line \(\{(t,t):t\in\mathbb F_p\}\), since its restrictions are
\[
t\notin R,\qquad t\ne-1.
\]

Now take a line
\[
L_a=\{(t,at):t\in\mathbb F_p\},
\qquad a\notin\{0,1\}.
\]
Membership in \(S_p\) requires
\[
t\notin R\cup a^{-1}R.
\]
The two sets \(R\) and \(a^{-1}R\) are distinct. Indeed, if they were equal, summing their elements would give
\[
a^{-1}\sum_{r\in R}r=\sum_{r\in R}r.
\]
But
\[
\sum_{r\in R}r=\frac{m(m+1)}2\ne0
\]
in \(\mathbb F_p\), forcing \(a=1\), a contradiction. Hence
\[
|R\cup a^{-1}R|\ge m+1,
\]
and therefore
\[
|S_p\cap L_a|
\le p-(m+1)=\frac{p+1}{2}.
\tag{21}
\]
This covers every prime-field line.

For the full additive group, (6) shows
\[
|S_p|\le\frac{p^2+1}{2}.
\]
Thus (4) follows.

When \(p=5\), \(S_5\setminus\{0\}\) has \(12\) elements, partitioned among six prime-field lines. Each line contains at most two of these elements by (21), so each contains exactly two. This verifies the claimed balanced boundary property.

# 4. Transfer to larger extension fields

The construction also yields small structured difference sets in larger fields.

Let \(q=p^k\), with \(p\ge5\) and \(k\ge2\). Suppose \(S\subseteq\mathbb F_q\) contains an additive image of \(S_p\) in a two-dimensional \(\mathbb F_p\)-subspace \(H\). Then
\[
|A|\le q^n\exp\!\left(-\frac{n}{9(p-1)^2}\right)
\tag{22}
\]
for every \(S\)-difference-free \(A\).

To verify the section argument used here, partition \(\mathbb F_q^n\) into the \((q/p^2)^n\) cosets of \(H^n\). Every section is free of progressions with differences in the embedded \(S_p^n\), and so has size at most the right-hand side of (3). Summing proves (22).

Thus, for example, in every field of characteristic \(5\) and degree at least \(2\), containing the explicit \(13\)-element pattern (5) suffices.

The section observation from the previous attempt is valid, but the new input is the bound for \(S_p\) itself. Its strict half-density hypothesis fails for every additive subgroup. This remains true when \(S_p\) is embedded into a larger field: every prime-field line is at most half dense, and summing over the prime-field lines of any additive subgroup gives the same conclusion.

# 5. What remains unresolved, and a barrier to this method

These results do **not** establish a smaller cardinality threshold valid for every \(S\). They establish a sufficient algebraic condition and an explicit family satisfying it.

There is also a precise reason this certificate method does not address the proposed extension to arbitrary two-point sets.

## Proposition: antipodal obstruction

Suppose
\[
S\cap(-S)=\{0\}.
\tag{23}
\]
Any polynomial \(P\) satisfying (7) must have
\[
\deg P\ge\frac{k(p-1)}2.
\tag{24}
\]

### Proof

As a function on \(\mathbb F_p^k\),
\[
P(X)P(-X)=P(0)^2\,1_{\{0\}}(X),
\]
because for every nonzero \(v\), at least one of \(v,-v\) lies outside \(S\).

The unique polynomial representation of this function with individual degrees at most \(p-1\) is
\[
P(0)^2\prod_{j=1}^k(1-X_j^{p-1}).
\]
It has total degree \(k(p-1)\). Reduction of \(P(X)P(-X)\) to individual degrees at most \(p-1\) cannot increase its total degree, so
\[
2\deg P\ge k(p-1).
\]
Here uniqueness follows from the usual univariate root bound, applied successively to the variables. \(\square\)

Every two-point set \(\{0,s\}\), \(s\ne0\), satisfies (23) in odd characteristic. Hence none can satisfy the strict low-degree hypothesis used above.

Likewise, in a prime field, a polynomial supported on a boundary set of size \((p+1)/2\) must vanish at \((p-1)/2\) distinct points, so its degree cannot be below the required cutoff.

Thus the universal boundary problem—and in particular \(\mathbb F_3\) with \(S=\{0,1\}\)—is not resolved by this argument. The established advance is the explicit extension-field family, including a balanced boundary example and families of asymptotic density \(1/4\) that evade the previous subgroup criterion. The argument is self-contained, but I have not checked whether the full source paper already records this low-degree refinement or these examples.