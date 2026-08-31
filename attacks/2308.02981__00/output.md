```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full polynomial bound remains open, but the separable indices of both monotone-avoidance classes Av(12...k) and Av(k...21) are Theta(log k).",
  "would_publish": false,
  "caveats": "This treats only monotone forbidden patterns and gives no worst-case upper bound over all patterns of size k."
}
```

## 1. Statement of the partial result

Write \(\operatorname{Sep}\) for the class of separable permutations and define
\[
\operatorname{si}(\sigma)
 =\min\{d:\sigma=\alpha_1\circ\cdots\circ\alpha_d,\ 
                   \alpha_i\in\operatorname{Sep}\}.
\]
The convention concerning the empty product changes only additive constants.

For a pattern \(\pi\), let
\[
I(\pi)=\sup_{\sigma\in\operatorname{Av}(\pi)}\operatorname{si}(\sigma).
\]
The problem asks whether
\[
F(k):=\max_{\pi\in S_k}I(\pi)
\]
is bounded by a polynomial in \(k\).

Let
\[
\iota_k=12\cdots k,\qquad \delta_k=k(k-1)\cdots1.
\]

### Theorem
For every \(k\ge2\),
\[
\frac{\log((k-1)!)}{(k-1)\log 8}
\le I(\iota_k),\,I(\delta_k)
\le 4\left\lceil\log_2(k-1)\right\rceil+1.
\]
Consequently,
\[
I(\iota_k)=I(\delta_k)=\Theta(\log k).
\]

The proof is constructive and does not use the doubly exponential theorem from the source paper.

---

## 2. Permutations with few increasing runs

We use the standard characterization
\[
\operatorname{Sep}=\operatorname{Av}(2413,3142).
\]

### Lemma 2.1
If the one-line notation of a permutation \(p\) is the concatenation of two increasing sequences, then
\[
\operatorname{si}(p)\le2.
\]

#### Proof
Write
\[
p=A\,B,
\]
where \(A\) and \(B\) are increasing and have lengths \(a\) and \(b\). Let
\[
\beta=\iota_a\oplus\delta_b.
\]
Thus \(\beta\) fixes the first block and reverses the second block. It is separable.

Set
\[
q=p\circ\beta.
\]
The one-line notation of \(q\) is \(A\) followed by \(B\) in decreasing order. We claim that every permutation consisting of an increasing block followed by a decreasing block is separable.

Indeed, suppose an occurrence of \(2413\) or \(3142\) uses \(t\) points from the first block. Since the first block precedes the second, the first \(t\) entries of the pattern must be increasing and the remaining \(4-t\) entries must be decreasing.

For \(2413\), the only potentially increasing nontrivial prefix is \(24\), but its remaining suffix \(13\) is increasing, not decreasing; the suffix \(413\) arising for \(t=1\) is also not decreasing. For \(3142\), the prefix \(31\) already fails to be increasing, while the suffix \(142\) arising for \(t=1\) is not decreasing. The cases \(t=0,4\) are impossible because neither forbidden pattern is monotone. Hence \(q\) avoids both \(2413\) and \(3142\).

Since \(\beta\) is an involution,
\[
p=q\circ\beta,
\]
a product of two separable permutations. \(\square\)

### Lemma 2.2
If the one-line notation of \(p\) is the concatenation of at most \(r\) increasing runs, then
\[
\operatorname{si}(p)\le 2\left\lceil\log_2 r\right\rceil
\]
for \(r\ge2\).

#### Proof
Label each value of \(p\) by the run in which it occurs, using labels
\[
0,1,\ldots,r-1.
\]
Starting from the increasing list \(1,2,\ldots,n\), stable sorting by these labels produces \(p\): elements with the same label remain in increasing value order.

Encode the labels with
\[
q=\left\lceil\log_2 r\right\rceil
\]
bits and perform least-significant-digit radix sorting. Thus one makes \(q\) successive stable binary sorts.

At any binary sort, the permutation of the current positions lists first all positions carrying bit \(0\), in their previous order, and then all positions carrying bit \(1\), again in their previous order. Its one-line notation is therefore the concatenation of two increasing sequences. By Lemma 2.1 it is a product of at most two separable permutations.

The \(q\) binary sorts consequently give a factorization of \(p\) into at most \(2q\) separable permutations. \(\square\)

As a byproduct, every permutation of length \(n\) has separable index at most \(2\lceil\log_2n\rceil\), by splitting its one-line notation into singleton runs.

---

## 3. Parallelizing colored subpermutations

The following lemma converts a coloring into a factorization with only logarithmic overhead.

### Lemma 3.1
Suppose the entries of \(\sigma\) are colored with \(r\) colors and every color-induced permutation has separable index at most \(d\). Then
\[
\operatorname{si}(\sigma)
\le d+4\left\lceil\log_2 r\right\rceil.
\]

In particular, if every color induces a separable permutation, then
\[
\operatorname{si}(\sigma)
\le 1+4\left\lceil\log_2 r\right\rceil.
\]

#### Proof
For each color \(c\), list its positions in increasing order:
\[
x_{c,1}<\cdots<x_{c,m_c},
\]
and list the values appearing on that color in increasing order:
\[
y_{c,1}<\cdots<y_{c,m_c}.
\]

Let \(P\) be the permutation whose one-line notation is obtained by concatenating the lists of positions, color by color. Define \(Q\) analogously using the lists of values. Both \(P\) and \(Q\) have at most \(r\) increasing runs. Therefore, with \(q=\lceil\log_2r\rceil\),
\[
\operatorname{si}(P),\operatorname{si}(Q)\le2q.
\]
The inverse of a separable permutation is separable, so the same bound holds for \(P^{-1}\).

Now set
\[
D=Q^{-1}\circ\sigma\circ P.
\]
Both the domain and range of \(D\) are grouped by color. Hence
\[
D=D_1\oplus D_2\oplus\cdots\oplus D_r,
\]
where \(D_c\) is the permutation induced by color \(c\).

If
\[
D_c=\alpha_{c,1}\circ\cdots\circ\alpha_{c,d},
\]
padding shorter factorizations with identities, then
\[
D=
\left(\bigoplus_c\alpha_{c,1}\right)
\circ\cdots\circ
\left(\bigoplus_c\alpha_{c,d}\right).
\]
Direct sums of separable permutations are separable, so
\[
\operatorname{si}(D)\le d.
\]
Finally,
\[
\sigma=Q\circ D\circ P^{-1},
\]
giving
\[
\operatorname{si}(\sigma)\le2q+d+2q.
\]
\(\square\)

---

## 4. Upper bound for monotone avoidance

Put \(r=k-1\).

If \(\sigma\) avoids \(\delta_k\), then its longest decreasing subsequence has length at most \(r\). By Dilworth’s theorem applied to the usual permutation poset, its entries can be partitioned into at most \(r\) increasing subsequences. Each color-induced permutation is increasing and hence separable. Lemma 3.1 gives
\[
\operatorname{si}(\sigma)
\le 4\left\lceil\log_2r\right\rceil+1.
\]

Similarly, if \(\sigma\) avoids \(\iota_k\), its entries can be partitioned into at most \(r\) decreasing subsequences. Each induced decreasing permutation is separable, and the same bound follows:
\[
\operatorname{si}(\sigma)
\le 4\left\lceil\log_2r\right\rceil+1.
\]

This proves the asserted logarithmic upper bounds.

---

## 5. Matching counting lower bound

Let \(s_n\) be the number of separable permutations of length \(n\). Every separable permutation has a representation by a plane full binary tree with \(n\) leaves, with each internal vertex labeled by either direct sum or skew sum. Therefore
\[
s_n\le 2^{n-1}C_{n-1}<8^n,
\]
where \(C_{n-1}<4^{n-1}\) is the corresponding Catalan number.

Consequently, the number of permutations of length \(n\) expressible as a product of at most \(D\) separable permutations is at most
\[
s_n^D\le8^{Dn},
\]
because factorizations with fewer than \(D\) factors can be padded with identities.

Now fix \(r=k-1\) and \(m\ge1\). For every tuple
\[
(\tau_1,\ldots,\tau_m)\in S_r^m,
\]
consider
\[
\tau_1\oplus\cdots\oplus\tau_m.
\]
These \((r!)^m\) permutations are distinct. A decreasing subsequence cannot cross between two direct-sum blocks, so all of them avoid \(\delta_{r+1}=\delta_k\).

Thus, if all \(\delta_k\)-avoiders had separable index at most \(D\), then
\[
(r!)^m\le8^{Dmr}.
\]
Taking logarithms and cancelling \(m\) gives
\[
D\ge\frac{\log(r!)}{r\log8}.
\]

For \(\iota_k\), use skew sums
\[
\tau_1\ominus\cdots\ominus\tau_m.
\]
An increasing subsequence cannot cross between skew-sum blocks, giving the identical lower bound.

Since
\[
\frac{\log(r!)}r=\log r-1+O\!\left(\frac{\log r}{r}\right),
\]
both lower bounds are \(\Omega(\log r)\). Together with the upper bounds,
\[
I(\iota_k)=I(\delta_k)=\Theta(\log k).
\]

---

## 6. Scope and remaining gap

The argument completely settles the quantitative problem for the two monotone forbidden patterns. More generally, Lemma 3.1 shows that a partition into \(r\) separable induced subpermutations incurs only \(O(\log r)\) separable factors.

However, for an arbitrary pattern \(\pi\in S_k\), no bound is obtained here on such a partition, nor directly on \(I(\pi)\). Hence this does not improve the catalogued doubly exponential worst-case upper bound for
\[
F(k)=\max_{\pi\in S_k}I(\pi),
\]
and it does not approach the stronger known worst-case lower bound coming from growth rates. The original polynomial-upper-bound question remains open.