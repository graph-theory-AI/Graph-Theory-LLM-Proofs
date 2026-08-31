```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A complement-matching ordering gives the explicit bound M_{P(n)}(n) <= (1/4+o(1))n^3/ln n, and the conjectured constant is attained for primes at most alpha n when alpha <= 1/2.",
  "would_publish": false,
  "caveats": "Endpoint conventions are asymptotically irrelevant; I have not checked whether the 1/4 upper bound is already implicit in the full source paper."
}
```

# Mathematical writeup

## 1. Model and results

Write
\[
P_d(a)=\{a,a+d,\ldots,a+(n-1)d\}.
\]
This is a translate of \(\{d,2d,\ldots,nd\}\). Let \(M_D(n)\) be the least length of an integer interval containing pairwise disjoint sets \(P_d(a_d)\), \(d\in D\).

I prove the following partial results.

### Theorem A
For \(D=\mathbb P(n)=\{p\le n:p\text{ prime}\}\),
\[
\left(\frac16-o(1)\right)\frac{n^3}{\log n}
\le M_{\mathbb P(n)}(n)
\le
\left(\frac14+o(1)\right)\frac{n^3}{\log n}.
\]

Thus the conjectured lower constant \(1/6\) is recovered, while the construction gives an explicit upper constant \(1/4\).

### Theorem B: a sharp truncated-prime case
For every fixed \(0<\alpha\le \frac12\),
\[
M_{\mathbb P(\alpha n)}(n)
\sim
\left(\frac{\alpha^2}{2}-\frac{\alpha^3}{3}\right)
\frac{n^3}{\log n}.
\]
Here \(\mathbb P(\alpha n)\) denotes the primes at most \(\alpha n\).

Theorem B is a genuine sharp special case of the conjectural mechanism.

---

## 2. A CRT packing lemma

The main construction is elementary.

### Lemma 1
Let \(d_1,\ldots,d_s\le n\) be distinct pairwise coprime positive integers satisfying
\[
d_i+d_{i+2}\le n\qquad(1\le i\le s-2).
\]
Define
\[
b_1=0,\qquad
b_{i+1}=b_i+d_i(n-d_{i+1})+d_{i+1}.
\]
Then the progressions
\[
B_i=\{b_i+j d_i:0\le j<n\}
\]
are pairwise disjoint.

Moreover, they lie in an interval of length at most
\[
\sum_{i=1}^{s-1}d_i(n-d_{i+1})+n d_s+O(sn).
\]

#### Proof

Put \(p=d_i\) and \(q=d_{i+1}\). Suppose two adjacent progressions intersect:
\[
b_i+up=b_{i+1}+vq
\]
for some \(0\le u,v<n\). From the definition of \(b_{i+1}\),
\[
up=p(n-q)+q(v+1),
\]
and hence
\[
p(u-n+q)=q(v+1).
\]
Since \(\gcd(p,q)=1\), \(q\mid u-n+q\). The right-hand side is positive, so
\[
u-n+q>0.
\]
On the other hand \(u\le n-1\), giving
\[
u-n+q\le q-1.
\]
This is impossible. Thus adjacent progressions are disjoint.

For nonadjacent progressions, put \(p=d_i,q=d_{i+1},r=d_{i+2}\). We have
\[
\begin{aligned}
b_{i+2}-b_i
&=p(n-q)+q+q(n-r)+r.
\end{aligned}
\]
Subtracting the span \((n-1)p\) of \(B_i\) gives
\[
b_{i+2}-b_i-(n-1)p
=q(n-p-r+1)+p+r>0,
\]
because \(p+r\le n\). Hence \(B_{i+2}\) begins strictly after the end of \(B_i\). Since the \(b_i\) are increasing, every \(B_j\), \(j\ge i+2\), also begins after \(B_i\).

Finally,
\[
b_s=\sum_{i=1}^{s-1}\bigl(d_i(n-d_{i+1})+d_{i+1}\bigr),
\]
and the last endpoint is \(b_s+(n-1)d_s\). This gives the asserted length bound. ∎

The crucial point is that only consecutive intervals are allowed to overlap, and their residues have been aligned so that even those consecutive progressions are disjoint.

---

## 3. Sharp packing below \(n/2\)

Let
\[
p_1<p_2<\cdots<p_k\le \alpha n,
\qquad \alpha\le \frac12.
\]
Then
\[
p_i+p_{i+2}\le 2\alpha n\le n.
\]
Lemma 1 therefore gives
\[
M_{\mathbb P(\alpha n)}(n)
\le
\sum_{i=1}^{k-1}p_i(n-p_{i+1})+n p_k+O(n^2).
\]
Since
\[
\sum_{i=1}^{k-1}p_i(p_{i+1}-p_i)
\le p_k\sum_{i=1}^{k-1}(p_{i+1}-p_i)
=O(n^2),
\]
the right-hand side equals
\[
\sum_{p\le \alpha n}p(n-p)+O(n^2).
\]

By partial summation and the prime number theorem,
\[
\sum_{p\le \alpha n}p(n-p)
\sim
\frac1{\log n}\int_0^{\alpha n}x(n-x)\,dx,
\]
and therefore
\[
\sum_{p\le \alpha n}p(n-p)
\sim
\left(\frac{\alpha^2}{2}-\frac{\alpha^3}{3}\right)
\frac{n^3}{\log n}.
\]

It remains to record the matching lower bound.

### Lemma 2
Let \(D\subseteq\{1,\ldots,n-1\}\) be pairwise coprime. Then every packing satisfies
\[
M_D(n)\ge
(n-1)\sum_{d\in D}d-\sum_{d\in D}d^2-O(1).
\]

#### Proof

Order the progressions by their first terms:
\[
a_1<a_2<\cdots<a_k,
\]
and let their differences in this order be \(q_1,\ldots,q_k\).

Consider consecutive progressions of differences \(p=q_i\) and \(q=q_{i+1}\). If
\[
a_{i+1}-a_i\le (n-1)p-pq,
\]
then both convex hulls contain the integer interval
\[
[a_{i+1},a_{i+1}+pq-1].
\]
Indeed, the first progression extends at least \(pq\) beyond \(a_{i+1}\), while the second has span \((n-1)q\ge pq\), since \(p\le n-1\).

The two residue classes have a common solution modulo \(pq\), so this interval contains a point belonging to both progressions, a contradiction. Consequently,
\[
a_{i+1}-a_i>(n-1)q_i-q_iq_{i+1}.
\]
After summing and adding the span of the last progression,
\[
M_D(n)\ge
(n-1)\sum_{i=1}^kq_i-\sum_{i=1}^{k-1}q_iq_{i+1}-O(1).
\]
Finally,
\[
\sum_{i=1}^{k-1}q_iq_{i+1}
\le
\frac12\sum_{i=1}^{k-1}(q_i^2+q_{i+1}^2)
\le \sum_{i=1}^kq_i^2.
\]
This proves the claim. ∎

Applying Lemma 2 to the primes at most \(\alpha n\) gives
\[
M_{\mathbb P(\alpha n)}(n)
\ge
\sum_{p\le\alpha n}p(n-p)-O\left(\sum_{p\le\alpha n}p\right),
\]
which has the same leading asymptotic as the upper bound. This proves Theorem B.

For \(\alpha=\frac12\), the constant is
\[
\frac{(1/2)^2}{2}-\frac{(1/2)^3}{3}
=\frac1{12}.
\]

---

## 4. Complement matching for all primes

To handle primes above \(n/2\), we arrange almost all primes in a sequence satisfying the two-step condition in Lemma 1.

### Lemma 3
For every fixed \(\eta>0\) and all sufficiently large \(n\), all but
\[
O\!\left(\eta\frac n{\log n}\right)+o_\eta\!\left(\frac n{\log n}\right)
\]
primes up to \(n\) can be partitioned into pairs
\[
(h_i,\ell_i),\qquad h_i>\frac n2,\quad \ell_i\le\frac n2,
\]
such that
\[
0\le n-h_i-\ell_i\le 2\eta n.
\]

#### Proof

For simplicity take \(\eta\) so that the relevant endpoints are integral multiples of \(\eta\). Partition most of \((n/2,(1-\eta)n]\) into intervals
\[
H_a=(an,(a+\eta)n],
\]
and associate to \(H_a\) the reflected, slightly shifted interval
\[
L_a=((1-a-2\eta)n,(1-a-\eta)n].
\]
If \(h\in H_a\) and \(\ell\in L_a\), then
\[
(1-2\eta)n<h+\ell\le n.
\]

Both intervals have length \(\eta n\). For fixed \(\eta\), the prime number theorem gives
\[
|H_a|=(\eta+o_\eta(1))\frac n{\log n},
\qquad
|L_a|=(\eta+o_\eta(1))\frac n{\log n}.
\]
There are only \(O_\eta(1)\) bins, so in each associated pair of bins we can match all but \(o_\eta(n/\log n)\) primes. The omitted top and middle boundary intervals have total length \(O(\eta n)\), hence contain \(O(\eta n/\log n)\) primes. ∎

Order these pairs so that
\[
h_1>h_2>\cdots>h_m.
\]
After discarding at most one pair, assume \(m\) is even. Consider the sequence
\[
h_1,h_2,\ell_1,\ell_2,
h_3,h_4,\ell_3,\ell_4,\ldots,
h_{m-1},h_m,\ell_{m-1},\ell_m.
\]

Every pair of terms at distance two has sum at most \(n\). For example,
\[
h_i+\ell_i\le n,
\]
and, since the \(h_i\) decrease,
\[
\ell_i+h_{i+2}\le \ell_i+h_i\le n.
\]
Thus Lemma 1 applies.

---

## 5. Cost of the complement-matched sequence

Let
\[
\ell_i^*=n-h_i.
\]
By Lemma 3,
\[
|\ell_i-\ell_i^*|\le 2\eta n.
\]
The packing cost from Lemma 1 is governed by
\[
C(d_1,\ldots,d_s)
=
\sum_{j=1}^{s-1}d_j(n-d_{j+1})+n d_s.
\]

First replace every \(\ell_i\) by \(\ell_i^*\). Consider one complete transition block
\[
h_{2t-1},h_{2t},\ell_{2t-1}^*,\ell_{2t}^*,h_{2t+1}.
\]
Its four transition costs sum to
\[
\begin{aligned}
&h_{2t-1}(n-h_{2t})
+h_{2t}(n-\ell_{2t-1}^*)\\
&\quad+\ell_{2t-1}^*(n-\ell_{2t}^*)
+\ell_{2t}^*(n-h_{2t+1})\\
&=
n^2+(h_{2t-1}-h_{2t+1})(n-h_{2t}).
\end{aligned}
\]
Summing the error terms telescopes:
\[
\sum_t(h_{2t-1}-h_{2t+1})(n-h_{2t})
\le
n\sum_t(h_{2t-1}-h_{2t+1})
=O(n^2).
\]
The final incomplete block and final span contribute only \(O(n^2)\). Hence the idealized cost is
\[
\frac m2n^2+O(n^2).
\]

Changing \(\ell_i^*\) back to \(\ell_i\) changes each adjacent bilinear term by at most \(O(n|\ell_i-\ell_i^*|)\). Therefore the total change is at most
\[
O\left(n\sum_{i=1}^m|\ell_i-\ell_i^*|\right)
=O(\eta m n^2).
\]

The matching lemma gives
\[
m=\left(\frac12+O(\eta)+o_\eta(1)\right)\frac n{\log n}.
\]
Consequently, the matched primes can be packed in an interval of length
\[
\left(\frac14+O(\eta)+o_\eta(1)\right)\frac{n^3}{\log n}.
\]

The number of unmatched primes is
\[
O\!\left(\eta\frac n{\log n}\right)+o_\eta\!\left(\frac n{\log n}\right).
\]
Packing each unmatched progression separately costs at most \(n^2+1\), so the total additional cost is
\[
O\!\left(\eta\frac{n^3}{\log n}\right)
+o_\eta\!\left(\frac{n^3}{\log n}\right).
\]
Letting first \(n\to\infty\) and then \(\eta\to0\) proves
\[
M_{\mathbb P(n)}(n)
\le
\left(\frac14+o(1)\right)\frac{n^3}{\log n}.
\]

---

## 6. Lower bound for the full prime set

Apply Lemma 2 after omitting the possible prime \(p=n\), which affects only lower-order terms. The prime number theorem and partial summation give
\[
\sum_{p\le n}p
=
\left(\frac12+o(1)\right)\frac{n^2}{\log n},
\qquad
\sum_{p\le n}p^2
=
\left(\frac13+o(1)\right)\frac{n^3}{\log n}.
\]
Therefore
\[
\begin{aligned}
M_{\mathbb P(n)}(n)
&\ge
(n-1)\sum_{p\le n}p-\sum_{p\le n}p^2-o\left(\frac{n^3}{\log n}\right)\\
&=
\left(\frac16-o(1)\right)\frac{n^3}{\log n}.
\end{aligned}
\]

This is the known conjecturally sharp lower bound.

---

## 7. Remaining gap

The argument gives
\[
\frac16
\le
\liminf_{n\to\infty}
\frac{M_{\mathbb P(n)}(n)\log n}{n^3}
\le
\limsup_{n\to\infty}
\frac{M_{\mathbb P(n)}(n)\log n}{n^3}
\le
\frac14.
\]

The loss comes from imposing the strong condition
\[
d_i+d_{i+2}\le n,
\]
which makes every pair of nonconsecutive convex hulls disjoint. For primes above \(n/2\), this forces the \(HHLL\) complement-matching pattern and costs asymptotically \(n^2\) per four progressions.

Reaching \(1/6\) requires allowing several high-difference progressions to have overlapping convex hulls while coordinating their CRT intersection points. The present construction does not address that simultaneous residue-assignment problem, so the original conjecture remains open.