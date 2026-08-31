```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but the prime-indexed subfamily is solved for primes at most sqrt(n/2), and its general upper constant is improved to (8sqrt(2)-7)/3.",
  "would_publish": false,
  "caveats": "The construction does not accommodate the composite-indexed progressions, so it does not improve the stated 5/3 upper bound for m(n)."
}
```

# 1. Statement and normalization

Write
\[
A_d=A_d(n):=\{d,2d,\ldots,r_dd\},
\qquad r_d:=\left\lfloor\frac nd\right\rfloor .
\]
Translations are by integers. Changing between interval cardinality and interval diameter affects all estimates by \(O(1)\).

For a set \(D\subseteq[n]\), let \(m_D(n)\) denote the minimum length of an interval containing pairwise disjoint translates of all \(A_d\), \(d\in D\). Thus the problem asks about
\[
m(n)=m_{[n]}(n).
\]

Put
\[
x:=\sqrt n,\qquad T_n:=\frac{n^{3/2}}{\log n}=\frac{x^3}{\log n}.
\]

I prove the following partial results.

## Theorem A: an exact truncated-prime case

For fixed \(0<\alpha\le 1/\sqrt2\), let
\[
\mathcal P_\alpha(n):=\{p\text{ prime}:p\le \alpha\sqrt n\}.
\]
Then
\[
m_{\mathcal P_\alpha(n)}(n)
=
\left(2\alpha-\frac{2}{3}\alpha^3+o(1)\right)T_n.
\]

In particular, the lower-bound mechanism coming from primes is sharp throughout the range \(p\le\sqrt{n/2}\).

## Theorem B: a better upper bound for the whole prime obstruction

Let
\[
\mathcal P(n):=\{p\text{ prime}:p\le\sqrt n\}.
\]
Then
\[
\left(\frac43-o(1)\right)T_n
\le m_{\mathcal P(n)}(n)
\le
\left(\frac{8\sqrt2-7}{3}+o(1)\right)T_n,
\]
where
\[
\frac{8\sqrt2-7}{3}=1.437902\ldots .
\]

The lower bound is the usual prime obstruction. The upper bound is strictly below \(5/3\), but only for the prime-indexed subfamily.

# 2. A pairwise separation lemma

We first record the lower-bound fact behind the constant \(4/3\).

### Lemma 2.1

Let \(d,e\) be coprime and \(de\le n\). Suppose that
\[
t+A_d,\qquad u+A_e
\]
are disjoint and \(u\ge t\). Then
\[
u-t>r_dd-de.
\]

### Proof

Put \(\delta=u-t\). Suppose instead that
\[
0\le\delta\le r_dd-de.
\]
Because \(\gcd(d,e)=1\), there is a \(j\in\{1,\ldots,d\}\) such that
\[
\delta+je\equiv0\pmod d.
\]
Set
\[
i:=\frac{\delta+je}{d}.
\]
Then \(i\ge1\). Moreover,
\[
id=\delta+je
\le r_dd-de+de=r_dd,
\]
so \(i\le r_d\). Also \(j\le d\le r_e\), since \(de\le n\). Consequently
\[
t+id=u+je
\]
belongs to both translates, a contradiction. ∎

For primes \(p,q\le x\), this gives
\[
u-t\ge n-pq-O(p).
\]

Now sort the translation bases of the prime-indexed progressions:
\[
t_{p_1}\le t_{p_2}\le\cdots\le t_{p_s}.
\]
Applying Lemma 2.1 to consecutive bases gives
\[
t_{p_{i+1}}-t_{p_i}
\ge n-p_ip_{i+1}-O(p_i).
\]
Furthermore,
\[
\sum_{i=1}^{s-1}p_ip_{i+1}
\le \frac12\sum_{i=1}^{s-1}(p_i^2+p_{i+1}^2)
\le \sum_{p\in D}p^2.
\]
The bases of progressions lying in one interval differ by at most the interval length plus \(O(x)\). Therefore, for any set \(D\) of primes at most \(x\),
\[
m_D(n)\ge |D|n-\sum_{p\in D}p^2-o(T_n).
\tag{2.1}
\]

For \(D=\{p\le\alpha x\}\), the prime number theorem and partial summation give
\[
|D|n
=
\left(2\alpha+o(1)\right)T_n
\]
and
\[
\sum_{p\le\alpha x}p^2
=
\left(\frac23\alpha^3+o(1)\right)T_n.
\]
Thus
\[
m_{\mathcal P_\alpha(n)}(n)
\ge
\left(2\alpha-\frac23\alpha^3-o(1)\right)T_n.
\tag{2.2}
\]

For \(\alpha=1\), this is the \(4/3\) lower bound.

# 3. A path-packing lemma

The following construction allows almost the full pairwise overlap \(d_ie_{i+1}\), provided nonconsecutive convex hulls can be kept disjoint.

### Lemma 3.1

Let \(d_1,\ldots,d_s\) be distinct primes satisfying
\[
d_id_{i+1}\le n
\tag{3.1}
\]
and
\[
d_{i+1}(d_i+d_{i+2})\le n
\qquad(1\le i\le s-2).
\tag{3.2}
\]
Then the \(A_{d_i}\) have pairwise disjoint translates in an interval of length at most
\[
\sum_{i=1}^s r_{d_i}d_i
-\sum_{i=1}^{s-1}d_id_{i+1}
+\sum_{i=1}^{s-1}d_i+O(1).
\tag{3.3}
\]
In particular, this is
\[
sn-\sum_{i=1}^{s-1}d_id_{i+1}
+O\left(\sum_{i=1}^s d_i\right).
\tag{3.4}
\]

### Proof

Write \(r_i=r_{d_i}\). Define translation bases recursively by
\[
b_1=0,\qquad
b_{i+1}=b_i+d_i(r_i-d_{i+1}+1).
\tag{3.5}
\]
The increment is positive because \(d_id_{i+1}\le n\), hence \(r_i\ge d_{i+1}\).

Put
\[
B_i=b_i+A_{d_i}.
\]

## Adjacent progressions

The number \(b_{i+1}\) lies in the infinite residue class \(b_i+d_i\mathbb Z\), and it is the omitted zeroth term of \(b_{i+1}+A_{d_{i+1}}\). Since \(d_i,d_{i+1}\) are coprime, the common points of the two infinite residue classes are
\[
b_{i+1}+k d_id_{i+1},\qquad k\in\mathbb Z.
\]
The next common point after \(b_{i+1}\) is
\[
b_{i+1}+d_id_{i+1}
=b_i+d_i(r_i+1),
\]
which lies strictly after the final point \(b_i+r_id_i\) of \(B_i\). Hence \(B_i\cap B_{i+1}=\varnothing\).

## Nonadjacent progressions

Let
\[
L_i=b_i+d_i,\qquad R_i=b_i+r_id_i
\]
be the first and last points of \(B_i\). Both sequences \(L_i\) and \(R_i\) are strictly increasing.

A direct calculation gives
\[
\begin{aligned}
L_{i+2}-R_i
={}&r_{i+1}d_{i+1}
-d_{i+1}(d_i+d_{i+2})\\
&\quad+d_i+d_{i+1}+d_{i+2}.
\end{aligned}
\]
Since
\[
r_{i+1}d_{i+1}>n-d_{i+1}
\]
and condition (3.2) holds, this difference is positive. Thus \(B_i\) and \(B_{i+2}\) have disjoint convex hulls. Monotonicity of the \(L_j\) then shows that \(B_i\) is hull-disjoint from every \(B_j\) with \(j\ge i+2\).

Finally,
\[
R_s
=
\sum_{i=1}^s r_id_i
-\sum_{i=1}^{s-1}d_id_{i+1}
+\sum_{i=1}^{s-1}d_i,
\]
which proves (3.3). ∎

The condition (3.2) can equivalently be read as saying that the two consecutive overlap savings
\[
d_id_{i+1},\qquad d_{i+1}d_{i+2}
\]
sum to at most \(n\).

# 4. Proof of Theorem A

List the primes at most \(\alpha x\) in increasing order:
\[
p_1<p_2<\cdots<p_s.
\]
When \(\alpha\le1/\sqrt2\),
\[
p_{i+1}(p_i+p_{i+2})
\le 2\alpha^2n\le n.
\]
Thus Lemma 3.1 applies.

Moreover,
\[
\sum_{i=1}^{s-1}p_ip_{i+1}
=
\sum_{p\le\alpha x}p^2+O(x^2).
\tag{4.1}
\]
Indeed,
\[
\sum_i p_i(p_{i+1}-p_i)
\le x\sum_i(p_{i+1}-p_i)=O(x^2),
\]
and the omitted endpoint contributes only \(O(x^2)\).

Since
\[
\sum_{p\le\alpha x}p=O\left(\frac{x^2}{\log x}\right)=o(T_n),
\]
Lemma 3.1 and (4.1) give
\[
m_{\mathcal P_\alpha(n)}(n)
\le
|\mathcal P_\alpha(n)|n
-\sum_{p\le\alpha x}p^2
+o(T_n).
\]
Combining with (2.2) proves
\[
m_{\mathcal P_\alpha(n)}(n)
=
\left(2\alpha-\frac23\alpha^3+o(1)\right)T_n.
\]

# 5. A stronger path for all primes up to \(\sqrt n\)

We next construct paths satisfying Lemma 3.1 that cover all primes \(p\le x\). The key is to pair large primes and put a suitably chosen small prime between successive large pairs.

Set
\[
a:=\frac1{\sqrt2}
\]
and, for \(a\le y\le1\), define
\[
f(y):=\frac1y-y.
\tag{5.1}
\]
Notice that
\[
y\bigl(y+f(y)\bigr)=1
\tag{5.2}
\]
and
\[
2y f(y)=2(1-y^2)\le1.
\tag{5.3}
\]

Thus, at the continuous level, the pattern
\[
yx,\ yx,\ f(y)x,\ yx,\ yx
\]
satisfies the triple condition (3.2), with equality possible at the endpoints.

To obtain strict inequalities, fix small \(\eta,\gamma>0\), restrict temporarily to
\[
a+\eta\le y\le1-\eta,
\]
and use separators close to
\[
(1-\gamma)f(y)x.
\]

## Availability of separator primes

Partition \([a+\eta,1-\eta]\) into intervals of small fixed width \(\delta\). Pair the primes \(p/x\) lying in each interval. For every two consecutive pairs in the same interval, choose one unused separator prime \(q\) with
\[
\frac qx=(1-\gamma)f(y)+O(\delta),
\tag{5.4}
\]
where \(y\) is the scale of that interval.

There are enough such primes. Indeed,
\[
|f'(y)|=1+\frac1{y^2}\ge2.
\]
Consequently, the image under \((1-\gamma)f\) of an interval of width \(\delta\) has width at least
\[
(2(1-\gamma)+O(\delta))\delta.
\]
By the prime number theorem, it contains asymptotically at least
\[
(2(1-\gamma)+o(1))\frac{\delta x}{\log x}
\]
primes, whereas only
\[
\left(\frac12+o(1)\right)\frac{\delta x}{\log x}
\]
separators are required. The images of disjoint high-prime intervals are disjoint because \(f\) is monotone.

For \(\delta\) sufficiently small relative to \(\eta,\gamma\), every resulting high-prime path has the pattern
\[
H_1,H_2,L_1,H_3,H_4,L_2,\ldots
\]
and satisfies
\[
d_{i+1}(d_i+d_{i+2})<n.
\]
Indeed, at a large-prime vertex this follows from
\[
y\bigl(y+(1-\gamma)f(y)\bigr)
=1-\gamma(1-y^2)<1,
\]
and at a separator vertex from
\[
2(1-\gamma)y f(y)<1.
\]

The unpaired primes from interval boundaries and the primes in the two omitted strips have total contribution \(O((\eta+\delta)T_n)\) if packed separately. These terms disappear after taking
\[
n\to\infty,\qquad \delta\to0,\qquad \gamma\to0,\qquad \eta\to0.
\]

All primes below \(ax\) not used as separators are placed in one increasing path. Every three of these satisfy
\[
d_{i+1}(d_i+d_{i+2})
\le 2a^2n=n.
\]

Thus Lemma 3.1 applies to every path.

# 6. Computing the resulting constant

Normalize primes by \(p=yx\). Prime density on a fixed proportional interval is
\[
\frac{x\,dy}{\log x}.
\]
An edge joining normalized values \(y,z\) contributes \(x^2yz\).

Let \(I\) be the normalized asymptotic edge-product sum, so that
\[
\sum_{\text{path edges}}pq
=
\left(I+o(1)\right)\frac{x^3}{\log x}.
\]

There are four contributions.

1. If no low primes were removed, the increasing path on \(0\le y\le a\) would contribute
   \[
   \int_0^a y^2\,dy.
   \]

2. There is one high-high edge per two high primes:
   \[
   \frac12\int_a^1 y^2\,dy.
   \]

3. Each high prime has asymptotically one edge to a separator:
   \[
   \int_a^1 y f(y)\,dy.
   \]

4. There is one separator per two high primes. Removing those primes from the low path loses
   \[
   \frac12\int_a^1 f(y)^2\,dy.
   \]

Hence
\[
I=
\int_0^a y^2\,dy+
\int_a^1
\left(
\frac12y^2+yf(y)-\frac12f(y)^2
\right)\,dy.
\tag{6.1}
\]
Using \(f(y)=y^{-1}-y\), the second integrand simplifies to
\[
2-y^2-\frac1{2y^2}.
\]
Therefore
\[
I=
\frac{13}{6}-2a-\frac1{2a}+\frac23a^3.
\]
For \(a=1/\sqrt2\),
\[
I=\frac{13}{6}-\frac{4\sqrt2}{3}.
\tag{6.2}
\]

Now
\[
n\pi(x)
=
(2+o(1))T_n,
\]
while
\[
\frac{x^3}{\log x}=2T_n.
\]
Lemma 3.1 therefore gives
\[
\begin{aligned}
m_{\mathcal P(n)}(n)
&\le
\left(2-2I+o(1)\right)T_n\\
&=
\left(\frac{8\sqrt2-7}{3}+o(1)\right)T_n.
\end{aligned}
\]
Together with (2.1), this proves Theorem B.

# 7. What remains open

These arguments do not prove an improved upper bound for the original \(m(n)\). The obstruction is substantive, not merely bookkeeping.

The path construction uses two facts specific to distinct primes:

1. Adjacent moduli are coprime, so their common infinite residue class has period exactly \(pq\).

2. Once the triple inequality
   \[
   d_{i+1}(d_i+d_{i+2})\le n
   \]
   is imposed, nonadjacent convex hulls are disjoint, so no simultaneous residue assignment is needed.

For the full family, many moduli \(ap,bq\) share factors. One can internally pack several multiples of \(p\) by assigning different residues modulo \(p\), but those residue choices interact with both neighboring groups. The pair-boundary construction in Lemma 3.1 no longer controls all cross-group intersections. I do not have a valid way to insert these composite-indexed progressions into the prime packing with \(o(T_n)\) additional length.

Thus the conjecture
\[
m(n)\sim\frac43\,T_n
\]
remains unresolved. The remaining difficulty is already visible for the full prime family above \(\sqrt{n/2}\): attaining the lower constant would require allowing three or more convex hulls to overlap while coordinating their residue phases, rather than making all nonadjacent hulls disjoint.