```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A subgroup reduction gives exponential upper bounds for every fixed k and, combined with a matching binary construction, proves s((Z/2^a Z)^n)=(2^a-1)2^n+1.",
  "would_publish": false,
  "caveats": "The odd-modulus exponential base remains open already for k=3, and the reduction and power-of-two case are likely standard."
}
```

## 1. Statement and interpretation

Write
\[
s_k(n):=\mathfrak s\bigl((\mathbb Z/k\mathbb Z)^n\bigr),
\qquad
T_k(n):=s_k(n)-1.
\]
Thus \(T_k(n)\) is the maximum length of a sequence in \((\mathbb Z/k\mathbb Z)^n\) having no zero-sum subsequence of length \(k\).

The question “estimate \(s_k(n)\)” is not a yes/no conjecture. The following gives:

1. a general reduction from composite \(k\) to its prime divisors;
2. an elementary exponential upper bound for every fixed \(k\);
3. the exact answer for every power of two;
4. a precise explanation of why the odd case is already difficult for \(k=3\).

## 2. Subgroup reduction

### Lemma 2.1
For all integers \(a,b\ge 2\) and \(n\ge1\),
\[
T_{ab}(n)\le bT_a(n)+T_b(n).
\tag{2.1}
\]

### Proof

Let
\[
G=(\mathbb Z/ab\mathbb Z)^n,\qquad H=bG.
\]
Then
\[
H\cong(\mathbb Z/a\mathbb Z)^n,\qquad G/H\cong(\mathbb Z/b\mathbb Z)^n.
\]

Consider a sequence in \(G\) of length
\[
b\bigl(s_a(n)-1\bigr)+s_b(n).
\]
As long as at least \(s_b(n)\) terms remain, their images in \(G/H\) contain a zero-sum subsequence of length \(b\). Repeating this, we obtain \(s_a(n)\) pairwise disjoint blocks
\[
B_1,\dots,B_{s_a(n)},
\]
each of size \(b\), whose sums lie in \(H\).

The block sums form a sequence of length \(s_a(n)\) in \(H\). Hence some \(a\) of them sum to zero. The union of the corresponding blocks has \(ab\) terms and sum zero in \(G\). Therefore
\[
s_{ab}(n)\le b(s_a(n)-1)+s_b(n),
\]
which is equivalent to (2.1). ∎

By interchanging \(a\) and \(b\), one also has
\[
T_{ab}(n)\le aT_b(n)+T_a(n).
\]

### Prime-power consequence

Iterating (2.1) gives, for a prime \(p\) and \(e\ge1\),
\[
T_{p^e}(n)
 \le (1+p+\cdots+p^{e-1})T_p(n)
 =\frac{p^e-1}{p-1}T_p(n).
\tag{2.2}
\]

More generally, if \(k=\prod_{p^e\parallel k}p^e\), applying the reduction first inside each prime power and then among the distinct prime powers yields
\[
T_k(n)
 \le
 k\sum_{p^e\parallel k}
 \frac{1-p^{-e}}{p-1}\,T_p(n).
\tag{2.3}
\]
Indeed, for any ordering \(q_1,\dots,q_m\) of the distinct prime-power factors,
\[
T_k(n)
 \le \sum_{i=1}^m
 \left(\prod_{j>i}q_j\right)T_{q_i}(n),
\]
and \(\prod_{j>i}q_j\le k/q_i\); inserting (2.2) gives (2.3).

In particular,
\[
\limsup_{n\to\infty}T_k(n)^{1/n}
\le
\max_{p\mid k}\limsup_{n\to\infty}T_p(n)^{1/n}.
\tag{2.4}
\]
Thus composite moduli create no larger upper exponential base than their prime divisors.

## 3. Elementary exponential bounds for every fixed \(k\)

For a prime \(p\),
\[
T_p(n)\le (p-1)p^n,
\tag{3.1}
\]
because a longer sequence contains \(p\) copies of some element, and these \(p\) copies sum to zero.

Substitution in (2.3) gives
\[
T_k(n)
\le
k\sum_{p^e\parallel k}(1-p^{-e})p^n
\le k\,\omega(k)\,P(k)^n,
\tag{3.2}
\]
where \(P(k)\) is the largest prime divisor of \(k\) and \(\omega(k)\) is the number of distinct prime divisors.

There is also a universal lower bound.

### Lemma 3.1
For all \(k\ge2\) and \(n\ge1\),
\[
T_k(n)\ge (k-1)2^n.
\tag{3.3}
\]

### Proof

Regard \(\{0,1\}^n\) as a subset of \((\mathbb Z/k\mathbb Z)^n\), and take \(k-1\) copies of every vector in \(\{0,1\}^n\).

Suppose \(k\) selected terms had sum zero. In each coordinate, the sum of their \(0\)-\(1\) entries is an integer between \(0\) and \(k\) divisible by \(k\), hence is either \(0\) or \(k\). Thus all \(k\) selected vectors agree in every coordinate, so they are \(k\) copies of one vector. Only \(k-1\) copies were included, a contradiction. ∎

Consequently, for every fixed \(k\),
\[
(k-1)2^n+1
\le s_k(n)
\le 1+k\omega(k)P(k)^n.
\tag{3.4}
\]
In particular,
\[
s_k(n)=2^{\Theta_k(n)}.
\]

This also shows that the catalog sentence claiming that the Alon–Dubiner bound \((cn\log n)^n k\) is the relevant fixed-composite-\(k\) upper bound cannot be read literally. Even the direct pigeonhole bound
\[
s_k(n)\le (k-1)k^n+1
\]
is exponential for fixed \(k\), and (3.2) improves its base from \(k\) to the largest prime divisor of \(k\). The Alon–Dubiner estimate is useful for a different parameter regime, particularly when \(k\) varies.

## 4. Exact evaluation for powers of two

### Theorem 4.1
For every \(a,n\ge1\),
\[
\boxed{
s_{2^a}(n)=(2^a-1)2^n+1.
}
\tag{4.1}
\]

### Proof

First,
\[
s_2(n)=2^n+1,
\]
because a two-term zero sum in \(\mathbb F_2^n\) is exactly a repeated element. Hence
\[
T_2(n)=2^n.
\]

Applying (2.2) with \(p=2\),
\[
T_{2^a}(n)
\le (2^a-1)T_2(n)
=(2^a-1)2^n.
\]
Lemma 3.1 supplies the reverse inequality. Therefore equality holds. ∎

Thus the fixed-\(k\) problem is completely settled when \(k\) is a power of two, not merely up to exponential order but exactly for every \(n\).

More generally, the same argument shows that, for fixed \(n\), if
\[
T_a(n)=(a-1)2^n,\qquad T_b(n)=(b-1)2^n,
\]
then
\[
T_{ab}(n)=(ab-1)2^n.
\]
Indeed, (2.1) gives the matching upper bound and Lemma 3.1 gives the lower bound.

## 5. Incorporating progression-free bounds

Let \(r_p(n)=r(\mathbb F_p^n)\). The Fox–Sauermann theorem supplied in the question gives, for prime \(p\),
\[
s_p(n)\le 2p\,r_p(n).
\tag{5.1}
\]

Combining (5.1) with (2.3), and using \(T_2(n)=2^n\), gives
\[
T_k(n)
\le
k\,\mathbf 1_{2\mid k}\,2^n
+
3k\sum_{\substack{p\mid k\\p\ \mathrm{odd}}}r_p(n).
\tag{5.2}
\]
Here we used
\[
2\,\frac{p}{p-1}\le3
\qquad(p\ge3).
\]

For completeness, the polynomial-method bound can be written as
\[
r_p(n)\le 3\Gamma_p^n,
\qquad
\Gamma_p:=
\min_{0<x<1}
(1+x+\cdots+x^{p-1})x^{-(p-1)/3}.
\tag{5.3}
\]
For every odd \(p\), \(\Gamma_p<p\). Hence, with
\[
\rho_k=
\max\left(
\{2:2\mid k\}
\cup
\{\Gamma_p:p\mid k,\ p\text{ odd}\}
\right),
\]
equation (5.2) implies
\[
\limsup_{n\to\infty}s_k(n)^{1/n}\le \rho_k.
\tag{5.4}
\]

For fixed odd \(k\), the bounds quoted in the question therefore give the rigorous interval
\[
2.08
\le
\liminf_{n\to\infty}s_k(n)^{1/n}
\le
\limsup_{n\to\infty}s_k(n)^{1/n}
\le
\max_{p\mid k}\Gamma_p.
\tag{5.5}
\]
The two ends remain far apart.

## 6. The obstruction already present at \(k=3\)

For \(p=3\), there is an exact relation.

### Proposition 6.1
For every \(n\ge1\),
\[
\boxed{s_3(n)=2r_3(n)+1.}
\tag{6.1}
\]

### Proof

In a sequence with no three-term zero sum, every element has multiplicity at most two. Moreover, its support contains no three distinct elements \(x,y,z\) with
\[
x+y+z=0.
\]
Over \(\mathbb F_3\), this is exactly a nontrivial three-term arithmetic progression. Thus the support has size at most \(r_3(n)\), and the sequence has length at most \(2r_3(n)\).

Conversely, take a progression-free set \(A\) of size \(r_3(n)\) and include two copies of every element. A zero-sum triple cannot consist of three distinct elements by progression-freeness. If it contains two equal elements, say \(x,x,y\), then
\[
2x+y=0
\]
implies \(y=x\) in characteristic three, requiring three copies of \(x\), which are unavailable. Hence the resulting sequence of length \(2r_3(n)\) is admissible. ∎

Cartesian products of cap sets show that \(r_3(n+m)\ge r_3(n)r_3(m)\). Therefore
\[
\lambda_3:=\lim_{n\to\infty}r_3(n)^{1/n}
\]
exists, and (6.1) gives
\[
\lim_{n\to\infty}s_3(n)^{1/n}=\lambda_3.
\]

A completely explicit cap of size \(9\) in \(\mathbb F_3^3\) is
\[
A=\{(x,y,x^2+y^2):x,y\in\mathbb F_3\}.
\]
Indeed, for a nonzero \(d=(d_1,d_2)\),
\[
f(u+d)+f(u-d)-2f(u)=2(d_1^2+d_2^2)\ne0
\]
in \(\mathbb F_3\). Taking Cartesian powers gives
\[
\lambda_3\ge 9^{1/3}=2.08008\ldots,
\]
while (5.3) gives
\[
\lambda_3\le\Gamma_3
=
\min_{0<x<1}(1+x+x^2)x^{-2/3}
<2.756.
\]
This explicit lower bound is only a benchmark, not a claim about the best currently known cap-set construction.

For powers of three, (2.2) and (6.1) give
\[
(3^a-1)2^n+1
\le
s_{3^a}(n)
\le
(3^a-1)r_3(n)+1.
\tag{6.2}
\]

## 7. What remains open

The exact power-of-two formula is complete, and the composite-to-prime reduction is unconditional. However:

- there is no matching reverse reduction showing that a composite modulus has the same exponential base as one of its prime divisors;
- for odd \(k\), even the case \(k=3\) asks for the exponential growth constant of cap sets in \(\mathbb F_3^n\);
- consequently, the principal odd-modulus gap in (5.5) remains unresolved.

Thus this is a genuine partial result rather than a solution of the full fixed-\(k\) asymptotic problem.