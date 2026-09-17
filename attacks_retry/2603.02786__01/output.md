```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "The conjectured asymptotic follows from an exact packing lemma for arithmetic-progression blocks of differences and the dense-subset Green–Tao theorem.",
  "would_publish": true,
  "caveats": "Uses the established relative-density Green–Tao theorem; novelty has not been checked against the full source paper."
}
```

# Proof of the conjecture

The restriction in the previous attempt—that nonconsecutive convex hulls must be disjoint—can be bypassed. For suitable arithmetic-progression blocks of prime differences, one can coordinate **every pair** of progressions, even when many convex hulls overlap. The dense-subset Green–Tao theorem supplies a partition of almost all primes into such blocks.

All shifts below are integers. An integer interval of length \(L\) contains \(L\) consecutive integers; using diameter instead changes the packing parameter by one.

Write
\[
A_d(b)=\{b,b+d,\ldots,b+(n-1)d\},
\qquad
S(n)=\sum_{p\le n}p(n-p).
\]

We prove the slightly more informative statement
\[
\boxed{\;
M_{\mathbb P(n)}(n)
=
S(n)+o\!\left(\frac{n^3}{\log n}\right).
\;}
\]
The prime number theorem then gives the conjectured constant \(1/6\).

## 1. An exact pairwise avoidance criterion

### Lemma 1
Let \(p,q\) be coprime positive integers. Suppose
\[
b'-b=Ap+Bq
\]
for integers \(A,B\) satisfying
\[
A\ge n-q,\qquad B\ge1.
\]
Then \(A_p(b)\) and \(A_q(b')\) are disjoint.

### Proof
An intersection would give
\[
b+up=b'+vq
\]
for some \(0\le u,v<n\), and hence
\[
(u-A)p=(v+B)q.
\]
Since the right-hand side is positive and \(\gcd(p,q)=1\), the integer \(u-A\) is a positive multiple of \(q\). Consequently,
\[
u\ge A+q\ge n,
\]
a contradiction. ∎

The next lemma arranges for this criterion to hold simultaneously for every pair in a block.

## 2. Packing an arithmetic-progression block of differences

### Lemma 2
Fix \(k\ge2\), and put
\[
Q=\operatorname{lcm}(1,2,\ldots,k-1).
\]
Suppose
\[
d_i=a+ih,\qquad 0\le i<k,
\]
are pairwise coprime positive integers satisfying
\[
d_0<d_1<\cdots<d_{k-1}\le n,
\qquad Q\mid h.
\]
Then their \(n\)-term progressions can be packed into an integer interval of length at most
\[
\boxed{\;
\sum_{i=0}^{k-1}d_i(n-d_i)+n^2+2Qkn.
\;}
\]

### Proof
Choose the integer \(n_*\) satisfying
\[
n\le n_*\le n+Q-1,
\qquad n_*\equiv a\pmod Q.
\]
Thus every \(n_*-d_i\) is a nonnegative multiple of \(Q\).

Set \(b_0=0\), and recursively define
\[
b_{i+1}
=
b_i+d_i(n_*-d_{i+1})+Qd_{i+1}
\qquad(0\le i<k-1).
\]
We claim that all sets \(A_{d_i}(b_i)\) are pairwise disjoint.

Fix \(i<j\), and write
\[
m=j-i,\qquad p=d_i,\qquad q=d_j.
\]
For \(0\le t<m\), the arithmetic-progression structure gives
\[
d_{i+t}=\frac{m-t}{m}p+\frac{t}{m}q
\]
and
\[
d_{i+t+1}
=\frac{m-t-1}{m}p+\frac{t+1}{m}q.
\]
Therefore
\[
\begin{aligned}
d_{i+t}(n_*-d_{i+t+1})
&=
\frac{(m-t)(n_*-d_{i+t+1})}{m}\,p\\
&\quad+
\frac{t(n_*-d_{i+t+1})}{m}\,q,
\end{aligned}
\]
while
\[
Qd_{i+t+1}
=
\frac{Q(m-t-1)}m\,p
+
\frac{Q(t+1)}m\,q.
\]

**Every coefficient displayed here is a nonnegative integer.** Indeed,
\(m\le k-1\), so \(m\mid Q\), and \(Q\mid n_*-d_{i+t+1}\).

Summing these identities over \(t=0,\ldots,m-1\), we obtain
\[
b_j-b_i=Ap+Bq
\]
with integer coefficients. The first term of the first sum contributes
\((n_*-d_{i+1})p\), so
\[
A\ge n_*-d_{i+1}\ge n-q.
\]
The last term of the second sum contributes \(Qq\), so
\[
B\ge Q\ge1.
\]
Lemma 1 now proves disjointness for this pair. Since \(i<j\) was arbitrary, all pairs are covered.

It remains to bound the containing interval. The \(b_i\) increase strictly, and the \(d_i\) increase, so the largest endpoint belongs to the last progression. Its containing interval has length
\[
\Lambda
=
\sum_{i=0}^{k-2}
\bigl[d_i(n_*-d_{i+1})+Qd_{i+1}\bigr]
+(n-1)d_{k-1}+1.
\]
For \(i<k-1\), using \(d_{i+1}\ge d_i\),
\[
d_i(n_*-d_{i+1})
\le d_i(n-d_i)+(n_*-n)d_i.
\]
Also,
\[
(n-1)d_{k-1}+1
=
d_{k-1}(n-d_{k-1})
+d_{k-1}^2-d_{k-1}+1
\le d_{k-1}(n-d_{k-1})+n^2.
\]
Because \(n_*-n<Q\) and all \(d_i\le n\), these inequalities give
\[
\Lambda
\le
\sum_{i=0}^{k-1}d_i(n-d_i)+n^2+2Qkn.
\]
This proves the lemma. ∎

The crucial feature is the cost: a block of \(k\) differences incurs only one \(n^2\)-sized boundary overhead, plus \(O_k(n)\). No separation condition on nonconsecutive convex hulls is imposed.

## 3. Almost all primes can be partitioned into suitable blocks

The non-elementary input is the following established form of the Green–Tao theorem.

### Dense-subset Green–Tao theorem
For every fixed \(k\ge3\) and \(\delta>0\), all sufficiently large \(N\) have the following property: every set
\[
E\subseteq\mathbb P(N),
\qquad |E|\ge\delta\,\pi(N),
\]
contains a nonconstant \(k\)-term arithmetic progression.

The dense-subset form matters here: the mere existence of arbitrarily long prime arithmetic progressions would not suffice.

### Lemma 3
For any fixed positive integers \(k\ge3\) and \(Q\), all but
\[
o_{k,Q}(\pi(n))
\]
primes up to \(n\) can be partitioned into \(k\)-term arithmetic progressions whose common differences are divisible by \(Q\).

### Proof
Take a maximal collection of disjoint \(k\)-term arithmetic progressions of primes up to \(n\), each with common difference divisible by \(Q\). Let \(R_n\) be the unused primes.

If \(|R_n|\ge\delta\pi(n)\), some residue class modulo \(Q\) contains at least
\[
\frac{\delta}{Q}\pi(n)
\]
members of \(R_n\). For sufficiently large \(n\), the dense-subset Green–Tao theorem supplies a \(k\)-term arithmetic progression within that residue class. Its common difference is divisible by \(Q\), contradicting maximality.

This works for every fixed \(\delta>0\), proving the claim. ∎

## 4. The asymptotically optimal upper bound

Fix \(k\ge3\), and let
\[
Q=\operatorname{lcm}(1,\ldots,k-1).
\]
Apply Lemma 3. Let \(t_n\) be the number of resulting blocks and \(u_n\) the number of unused primes. Then
\[
kt_n+u_n=\pi(n),
\qquad
u_n=o_k(\pi(n)).
\]

Each block consists of distinct primes, hence its differences are pairwise coprime. Lemma 2 applies.

Pack the blocks into consecutive, disjoint integer intervals. Pack each unused prime progression into its own interval. For a singleton prime \(p\le n\), the required length satisfies
\[
(n-1)p+1
=
p(n-p)+(p^2-p+1)
\le p(n-p)+n^2.
\]
Adding all block and singleton costs gives
\[
\begin{aligned}
M_{\mathbb P(n)}(n)
&\le S(n)+(t_n+u_n)n^2+2Qkn\,t_n\\
&\le S(n)+\frac{n^2\pi(n)}k
       +u_n n^2+2Qn\pi(n).
\end{aligned}
\]
Here \(k\) and \(Q\) are fixed. Consequently,
\[
\limsup_{n\to\infty}
\frac{M_{\mathbb P(n)}(n)-S(n)}{n^2\pi(n)}
\le \frac1k.
\]
Since this holds for every fixed \(k\ge3\),
\[
\boxed{\;
\limsup_{n\to\infty}
\frac{M_{\mathbb P(n)}(n)-S(n)}{n^2\pi(n)}
\le0.
\;}
\]

The order of limits is important: first \(n\to\infty\) with \(k\) fixed, and only then \(k\to\infty\). Thus the rapid growth of \(Q\), and the lack of a useful quantitative Green–Tao bound, cause no difficulty.

## 5. Matching lower bound

For completeness, here is an independent proof of the required lower bound.

Consider any packing, and restrict it to the primes \(p<n\). Order these progressions by their first terms:
\[
a_1<a_2<\cdots<a_s,
\]
with corresponding differences \(p_1,\ldots,p_s\).

For consecutive progressions, put \(p=p_i\), \(q=p_{i+1}\). If
\[
a_{i+1}-a_i\le (n-1)p-pq,
\]
then the integer interval
\[
[a_{i+1},\,a_{i+1}+pq-1]
\]
lies inside both convex hulls. For the second hull, this uses
\[
(n-1)q\ge pq,
\]
since \(p\le n-1\). The Chinese remainder theorem supplies a point in this interval congruent to \(a_i\pmod p\) and to \(a_{i+1}\pmod q\). Such a point belongs to both progressions, a contradiction.

Hence
\[
a_{i+1}-a_i>(n-1)p_i-p_ip_{i+1}.
\]
Summing and adding the span of the last progression yields the weaker, sufficient inequality
\[
M_{\mathbb P(n)}(n)
\ge
(n-1)\sum_{i=1}^s p_i
-\sum_{i=1}^{s-1}p_ip_{i+1}.
\]
Using \(2xy\le x^2+y^2\),
\[
\sum_{i=1}^{s-1}p_ip_{i+1}
\le \sum_{i=1}^s p_i^2.
\]
It follows that
\[
M_{\mathbb P(n)}(n)
\ge
\sum_{p<n}p(n-p)-\sum_{p<n}p.
\]
If \(n\) itself is prime, its contribution to \(S(n)\) is zero. Therefore
\[
M_{\mathbb P(n)}(n)\ge S(n)-n\pi(n).
\]
In particular,
\[
\liminf_{n\to\infty}
\frac{M_{\mathbb P(n)}(n)-S(n)}{n^2\pi(n)}
\ge0.
\]

Together with the upper bound, this proves
\[
M_{\mathbb P(n)}(n)
=
S(n)+o\bigl(n^2\pi(n)\bigr).
\]

## 6. Evaluating the main term

By the prime number theorem and partial summation,
\[
\sum_{p\le n}p
=
\left(\frac12+o(1)\right)\frac{n^2}{\log n},
\qquad
\sum_{p\le n}p^2
=
\left(\frac13+o(1)\right)\frac{n^3}{\log n}.
\]
Thus
\[
\begin{aligned}
S(n)
&=n\sum_{p\le n}p-\sum_{p\le n}p^2\\
&=
\left(\frac16+o(1)\right)\frac{n^3}{\log n}.
\end{aligned}
\]
Also \(n^2\pi(n)\sim n^3/\log n\). Consequently,
\[
\boxed{\displaystyle
M_{\mathbb P(n)}(n)\sim \frac16\,\frac{n^3}{\log n}.
}
\]

All collision cases, including nonconsecutive progressions and primes above \(n/2\), are covered by Lemma 2. The proof uses no unproved prime-pattern hypothesis; its only deep input is the established dense-subset Green–Tao theorem.