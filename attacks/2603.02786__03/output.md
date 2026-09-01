```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Integer-translate packings satisfy M_k(n) >= (6619/10800-o(1))nk^2/ln k when k=o(n), contradicting the conjectured constant 1/2.",
  "would_publish": false,
  "caveats": "This uses the intended definition in which all translations are integral; only the first regime is needed for the disproof."
}
```

# Statement

Let
\[
B_d=\{d,2d,\ldots,nd\},\qquad 1\le d\le k,
\]
and suppose integral translates \(t_d+B_d\) are pairwise disjoint and contained in one interval. Write \(M_k(n)\) for the minimum possible interval length.

I prove the following stronger lower bound.

**Theorem.** If \(k\to\infty\) and \(k=o(n)\), then
\[
M_k(n)\ge
\left(\frac{6619}{10800}-o(1)\right)\frac{nk^2}{\log k}.
\]
Equivalently,
\[
M_k(n)\ge
\left(\frac{6619}{5400}-o(1)\right)
\frac{nk^2}{2\log k}.
\]
Since
\[
\frac{6619}{5400}=1.225740\ldots>1,
\]
this contradicts the conjectured asymptotic
\[
M_k(n)\sim \frac{nk^2}{2\log k}.
\]

For an explicit counterexample sequence, one may take \(n=k^4\).

## 1. A core-overlap lemma

Let
\[
P_d=t_d+B_d
 =\{\alpha_d,\alpha_d+d,\ldots,\alpha_d+(n-1)d\},
\qquad \alpha_d=t_d+d.
\]
Its convex hull is
\[
H_d=[\alpha_d,\alpha_d+(n-1)d].
\]

Set \(L=k^2\), and define the core
\[
C_d=[\alpha_d+L,\alpha_d+(n-1)d-L],
\]
interpreted as empty if the right endpoint is smaller than the left endpoint.

### Lemma 1
If \(P_d\cap P_e=\varnothing\) and \(C_d\cap C_e\ne\varnothing\), then
\[
\alpha_d\not\equiv\alpha_e\pmod{\gcd(d,e)}.
\]

### Proof
Suppose instead that
\[
\alpha_d\equiv\alpha_e\pmod g,\qquad g=\gcd(d,e).
\]
Then the infinite lattices
\[
\alpha_d+d\mathbb Z,\qquad \alpha_e+e\mathbb Z
\]
intersect in a residue class modulo
\[
\ell=\operatorname{lcm}(d,e)\le de\le k^2=L.
\]
Choose \(x\in C_d\cap C_e\). There is a common lattice point \(y\) with
\[
|x-y|\le \ell/2\le L.
\]
Because \(x\) is at distance at least \(L\) from both endpoints of both hulls, \(y\in H_d\cap H_e\). A lattice point of \(\alpha_d+d\mathbb Z\) lying in \(H_d\) belongs to \(P_d\), and similarly for \(P_e\). Thus \(y\in P_d\cap P_e\), a contradiction. ∎

In particular, if \(\gcd(d,e)=1\), their cores are disjoint.

## 2. Prime cores

Let
\[
S(x)=\sum_{\substack{p\le x\\p\ \mathrm{prime}}}p.
\]
The cores \(C_p\), over all primes \(p\le k\), are pairwise disjoint by Lemma 1. Put
\[
U=\bigcup_{p\le k,\ p\text{ prime}} C_p.
\]
Since
\[
|C_d|\ge (n-1)d-2L
\]
even when the right side is negative, we have
\[
|U|
 =\sum_{p\le k}|C_p|
 \ge (n-1)S(k)-2k^2\pi(k).
\tag{1}
\]

## 3. Three families of prime multiples

For \(a\in\{2,3,5\}\), consider
\[
\mathcal B_a=\{C_{ap}: p>5\text{ prime},\ ap\le k\}.
\]
Assign weights
\[
\lambda_2=\frac12,\qquad
\lambda_3=\frac13,\qquad
\lambda_5=\frac16.
\]
Notice that
\[
\lambda_2+\lambda_3+\lambda_5=1.
\]

For a point \(x\), define the weighted multiplicity
\[
N(x)=
\sum_{a\in\{2,3,5\}}
\lambda_a\,
\#\{p>5:ap\le k,\ x\in C_{ap}\}.
\]

### Lemma 2
For every \(x\),
\[
N(x)\le1.
\]

### Proof
Fix \(a\in\{2,3,5\}\). For distinct primes \(p,q>5\),
\[
\gcd(ap,aq)=a.
\]
If both cores contain \(x\), Lemma 1 says their phases must be distinct modulo \(a\). Thus at most \(a\) members of \(\mathcal B_a\) can contain \(x\). Consequently, if only one family is represented, its weighted multiplicity is at most
\[
2\lambda_2=1,\qquad
3\lambda_3=1,\qquad
5\lambda_5=\frac56.
\]

Now suppose two different coefficient families are represented. If \(a\ne b\) and
\[
x\in C_{ap}\cap C_{bq},
\]
then, since \(a,b\in\{2,3,5\}\) are distinct primes and \(p,q>5\),
\[
\gcd(ap,bq)=1
\]
unless \(p=q\). Lemma 1 therefore forces \(p=q\). It follows that if several coefficient families occur at \(x\), each contributes at most one core, all with the same large-prime label. Their total weight is at most
\[
\lambda_2+\lambda_3+\lambda_5=1.
\]
∎

## 4. How much weighted work can lie over prime cores?

Let \(J\) be a containing interval and let \(W=|J|\), up to the immaterial additive-one convention for an interval of integers. Define
\[
T=
\sum_{a\in\{2,3,5\}}\lambda_a
\sum_{\substack{5<p\le k/a\\p\ \mathrm{prime}}}|C_{ap}|
=\int_J N(x)\,dx.
\]

For a prime \(q>5\), a core \(C_{ap}\) can meet \(C_q\) only when \(p=q\), because otherwise
\[
\gcd(ap,q)=1.
\]
The prime cores \(C_2,C_3,C_5\) contribute only \(O(n)\). Hence
\[
\int_U N(x)\,dx
\le
\sum_{a\in\{2,3,5\}}\lambda_a
\sum_{\substack{5<p\le k/a\\p\ \mathrm{prime}}}|C_p|
+O(n).
\]
Using \(|C_p|\le(n-1)p\), this gives
\[
\int_U N(x)\,dx
\le
(n-1)\sum_a\lambda_aS(k/a)+O(n).
\tag{2}
\]

On the other hand,
\[
\begin{aligned}
T
&\ge
\sum_a\lambda_a
\sum_{\substack{5<p\le k/a\\p\ \mathrm{prime}}}
\big((n-1)ap-2k^2\big)\\
&\ge
(n-1)\sum_a\lambda_a aS(k/a)
-O\!\left(k^2\pi(k)+n\right).
\end{aligned}
\tag{3}
\]

By Lemma 2, \(N(x)\le1\) on \(J\setminus U\). Therefore
\[
T
\le \int_U N(x)\,dx+|J\setminus U|
=\int_U N(x)\,dx+W-|U|.
\]
Combining this with (1), (2), and (3) yields
\[
W\ge
(n-1)\left(
S(k)+\sum_{a\in\{2,3,5\}}
\lambda_a(a-1)S(k/a)
\right)
-O\!\left(k^2\pi(k)+n\right).
\tag{4}
\]

## 5. Evaluation of the constant

The prime number theorem and partial summation give
\[
S(x)\sim\frac{x^2}{2\log x}.
\]
For each fixed \(a\),
\[
S(k/a)\sim\frac1{a^2}S(k).
\]
Thus the factor multiplying \(S(k)\) in (4) is
\[
\begin{aligned}
1+\sum_a\lambda_a\frac{a-1}{a^2}
&=
1+\frac12\frac1{2^2}
 +\frac13\frac2{3^2}
 +\frac16\frac4{5^2}\\
&=
1+\frac18+\frac2{27}+\frac2{75}\\
&=
1+\frac{1219}{5400}
=\frac{6619}{5400}.
\end{aligned}
\]

Moreover,
\[
k^2\pi(k)=O\!\left(\frac{k^3}{\log k}\right)
=o\!\left(\frac{nk^2}{\log k}\right)
\]
whenever \(k=o(n)\). Therefore (4) gives
\[
M_k(n)\ge
\left(\frac{6619}{5400}-o(1)\right)
\frac{nk^2}{2\log k}
=
\left(\frac{6619}{10800}-o(1)\right)
\frac{nk^2}{\log k}.
\]

This is incompatible with the claimed coefficient \(1/2\).

## 6. Simpler subargument

Using only the family \(d=2p\) and weight \(1/2\) already gives
\[
M_k(n)\ge
\left(\frac{9}{16}-o(1)\right)\frac{nk^2}{\log k},
\]
since the prime baseline contributes \(1/2\) and doubled primes contribute an additional \(1/16\). Thus the extra \(3p\) and \(5p\) families are not needed for the disproof; they merely strengthen the lower constant to \(6619/10800\).

## Gaps and scope

There is no remaining mathematical gap under the standard definition that translates are integral. The congruence argument would not apply to arbitrary real translations, but that interpretation would make the stated packing problem essentially trivial and is inconsistent with the source paper’s quoted orders of magnitude. The second, \(k\asymp n\), regime need not be analyzed because the first clause is already false.