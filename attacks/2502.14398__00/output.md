```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained argument proves the conjectured converse for all composite n divisible by 2 or 3 and gives stronger structural obstructions, but it does not settle composite n coprime to 6, beginning with n=25.",
  "would_publish": false,
  "caveats": "The unresolved case t(25) in {22,23}, and hence the general coprime-to-6 case, remains open."
}
```

## 1. Reformulation in terms of cycle counts

Write \(G=\mathbb Z_n\), let
\[
\rho(x)=x+1,
\]
and let \(c(\sigma)\) denote the number of cycles of a permutation \(\sigma\), including fixed points.

The transposition length of \(\sigma\in S_n\) is
\[
\ell(\sigma)=n-c(\sigma).
\]
Indeed, each transposition changes the number of cycles by at most one, while every cycle of length \(m\) can be split into fixed points using \(m-1\) transpositions.

For \(\pi\in S_n\), put
\[
f_a=\rho^a\pi,\qquad a\in G,
\]
where \(f_a(x)=\pi(x)+a\). Up to reversing the multiplication convention, these are exactly the representatives obtained by rotating a circular permutation. Thus the sorting distance of the circular class represented by \(\pi\) is
\[
\delta(\pi)=\min_{a\in G}\ell(f_a)
           =n-\max_{a\in G}c(f_a).
\]
Consequently
\[
t(n)=n-\min_{\pi\in S_n}\max_{a\in G}c(f_a).
\tag{1}
\]

A useful universal identity is
\[
\sum_{a\in G}\operatorname{fix}(f_a)=n.
\tag{2}
\]
For every \(x\), exactly one value
\[
a=x-\pi(x)
\]
makes \(f_a(x)=x\).

Since some \(f_a\) has a fixed point and \(n>1\), that \(f_a\) has at least two cycles. Hence
\[
t(n)\le n-2.
\tag{3}
\]
Equality \(t(n)=n-2\) is therefore equivalent to the existence of a permutation \(\pi\) satisfying
\[
c(f_a)\le2\qquad\text{for every }a\in G.
\tag{4}
\]

## 2. The prime construction

Let \(p\) be an odd prime and let \(g\) be a primitive root modulo \(p\). Set
\[
\pi(x)=gx.
\]
For every \(a\), the affine permutation
\[
f_a(x)=gx+a
\]
has a unique fixed point \(r=a(1-g)^{-1}\). Translation by \(r\) conjugates \(f_a\) to multiplication by \(g\):
\[
f_a(r+x)-r=gx.
\]
Multiplication by \(g\) fixes \(0\) and is a single \((p-1)\)-cycle on \(G\setminus\{0\}\). Thus
\[
c(f_a)=2
\]
for every \(a\), proving \(t(p)=p-2\). The case \(p=2\) is immediate.

This supplies the known prime direction without invoking the source paper.

## 3. Structure of a hypothetical extremizer

Assume \(n>2\) and that (4) holds.

### 3.1 Even \(n\) is impossible

If \(n\) is even, then
\[
\operatorname{sgn}(f_a)=(-1)^a\operatorname{sgn}(\pi).
\]
Exactly \(n/2\) of the \(f_a\)'s are odd and \(n/2\) are even. Since
\[
\operatorname{sgn}(\sigma)=(-1)^{n-c(\sigma)}=(-1)^{c(\sigma)}
\]
for even \(n\), condition \(c(f_a)\le2\) implies:

- every odd \(f_a\) has exactly one cycle and hence no fixed point;
- every even \(f_a\) has exactly two cycles and, for \(n>2\), at most one fixed point.

It follows that
\[
\sum_a\operatorname{fix}(f_a)\le n/2,
\]
contradicting (2). Therefore
\[
t(n)\le n-3\qquad(n>2\text{ even}).
\tag{5}
\]

### 3.2 Odd extremizers have cycle type \((1,n-1)\)

Now suppose \(n\) is odd. The rotations \(\rho^a\) are even, so all \(f_a\) have the same parity as \(\pi\).

If \(\pi\) were even, then \(c(f_a)\) would be odd. Under (4), every \(f_a\) would therefore be an \(n\)-cycle and would have no fixed point, again contradicting (2). Hence \(\pi\) is odd.

It follows that every \(c(f_a)\) is even, and therefore
\[
c(f_a)=2\qquad\text{for every }a.
\]
A permutation with two cycles has at most one fixed point when \(n>2\). Identity (2) now forces every \(f_a\) to have exactly one fixed point. Thus every \(f_a\) has cycle type
\[
(1,n-1).
\tag{6}
\]

Define
\[
d(x)=x-\pi(x),\qquad s(x)=x+\pi(x).
\]
The unique fixed point of \(f_a\) is a solution of \(d(x)=a\), so \(d\) is a permutation.

If \(n\ge5\) and \(s(x)=s(y)\) for distinct \(x,y\), put
\[
a=y-\pi(x).
\]
Then
\[
f_a(x)=y
\]
and, using \(x+\pi(x)=y+\pi(y)\),
\[
f_a(y)=\pi(y)+y-\pi(x)=x.
\]
Thus \((x\,y)\) would be a 2-cycle of \(f_a\), impossible under (6), whose nontrivial cycle has length \(n-1\ge4\). Hence \(s\) is also a permutation.

Therefore any odd-order extremizer with \(n\ge5\) is necessarily a strong complete mapping:
\[
\pi,\qquad x-\pi(x),\qquad x+\pi(x)
\]
are all permutations of \(\mathbb Z_n\).

## 4. Excluding multiples of \(3\)

Let
\[
S_2=\sum_{x=0}^{n-1}x^2.
\]
If \(\pi,d,s\) are permutations, then modulo \(n\),
\[
\sum_x\pi(x)^2\equiv
\sum_xd(x)^2\equiv
\sum_xs(x)^2\equiv S_2.
\]
But pointwise
\[
d(x)^2+s(x)^2
=(x-\pi(x))^2+(x+\pi(x))^2
=2x^2+2\pi(x)^2.
\]
Summing gives
\[
2S_2\equiv4S_2\pmod n,
\]
and hence
\[
2S_2\equiv0\pmod n.
\tag{7}
\]

If \(3\mid n\), write \(n=3m\). Since
\[
2S_2=\frac{n(n-1)(2n-1)}3
     =m(n-1)(2n-1)
\]
and
\[
(n-1)(2n-1)\equiv1\pmod3,
\]
the integer \(2S_2\) is not divisible by \(n=3m\), contradicting (7).

Thus no composite odd multiple of \(3\) can satisfy (4). Together with (5),
\[
t(n)\le n-3
\quad\text{for every composite }n\text{ with }2\mid n\text{ or }3\mid n.
\tag{8}
\]

In particular, the conjecture holds for every \(n<25\). This portion overlaps the result reported in the supplied literature review.

## 5. A local block obstruction

For \(r\in G\), define the based difference permutation
\[
D_r(x)=\pi(r+x)-\pi(r).
\tag{9}
\]
It is conjugate to one of the circular representatives. Indeed, with
\[
a_r=r-\pi(r),
\]
one has
\[
\rho^{-r}f_{a_r}\rho^r=D_r.
\tag{10}
\]

Let \(H\) be a nonzero proper subgroup of \(G\). Suppose that for some \(r\),
\[
\pi(r+H)=\pi(r)+H.
\tag{11}
\]
Then \(D_r(H)=H\). Since \(D_r(0)=0\), the three nonempty sets
\[
\{0\},\qquad H\setminus\{0\},\qquad G\setminus H
\]
are \(D_r\)-invariant. Hence
\[
c(D_r)\ge3.
\]
By (10),
\[
\max_a c(f_a)\ge3.
\tag{12}
\]

Thus a hypothetical extremizer at a composite \(n\) must map no coset of any nontrivial proper subgroup onto a coset of the same subgroup. In particular, a candidate for \(n=25\) must mix every coset of \(5\mathbb Z_{25}\) across at least two residue classes modulo \(5\).

## 6. A stronger bound for congruence-preserving permutations

Let \(\Omega(n)\) denote the number of prime factors of \(n\), counted with multiplicity.

Call \(\pi\) congruence-preserving if, for every divisor \(m\mid n\),
\[
x\equiv y\pmod m\quad\Longrightarrow\quad
\pi(x)\equiv\pi(y)\pmod m.
\]
Every permutation represented by an integer polynomial modulo \(n\) has this property.

Choose a maximal chain of subgroups
\[
\{0\}=H_0<H_1<\cdots <H_k=G,
\qquad k=\Omega(n),
\]
where each successive index is prime. Congruence preservation implies
\[
D_r(H_i)=H_i
\]
for every \(i\): inclusion follows from congruence preservation, and equality follows because \(D_r\) is a permutation.

Consequently all \(k+1\) nonempty layers
\[
H_0,\quad H_1\setminus H_0,\quad\ldots,\quad H_k\setminus H_{k-1}
\]
are invariant under \(D_r\). Therefore
\[
c(D_r)\ge \Omega(n)+1.
\]
Using (10),
\[
\boxed{\;
\delta(\pi)\le n-\Omega(n)-1
\;}
\tag{13}
\]
for every congruence-preserving permutation \(\pi\).

For composite \(n\), this already gives \(\delta(\pi)\le n-3\). It also yields a stronger bound when \(n\) has at least three prime factors counted with multiplicity.

## 7. Prime-power lower bounds and the precise \(n=25\) gap

Let \(n=p^k\), where \(p\) is odd, and choose a primitive root \(g\) modulo \(p^k\). For
\[
\pi(x)=gx,
\]
every \(f_a(x)=gx+a\) is conjugate to \(x\mapsto gx\), since \(g-1\) is a unit.

Multiplication by \(g\) has:

- the fixed point \(0\);
- one cycle on the elements of each \(p\)-adic valuation
  \[
  j=0,1,\ldots,k-1.
  \]

Indeed, on elements \(p^j u\), it acts regularly through the cyclic unit group modulo \(p^{k-j}\). Hence
\[
c(f_a)=k+1
\]
for every \(a\), and therefore
\[
t(p^k)\ge p^k-k-1.
\tag{14}
\]

For \(k=2\),
\[
p^2-3\le t(p^2)\le p^2-2.
\tag{15}
\]
Thus the conjecture for \(p^2\) is exactly the assertion that the lower value in (15) is correct.

For \(n=25\), take \(\pi(x)=2x\). The element \(2\) has order \(20\) modulo \(25\), so multiplication by \(2\) has three cycles:

- \(\{0\}\);
- one 20-cycle on the units;
- one 4-cycle on the nonzero multiples of \(5\).

All affine shifts are conjugate to it, so this circular permutation has distance
\[
25-3=22.
\]
Consequently
\[
\boxed{22\le t(25)\le23.}
\]
No argument above decides between these two possibilities.

## 8. Exact structural formulations of the remaining case

For odd \(n\ge5\), a permutation satisfies \(\max_a c(f_a)=2\) if and only if every \(D_r\) from (9) fixes \(0\) and is a single \((n-1)\)-cycle on \(G\setminus\{0\}\).

The forward implication follows from (6) and (10). Conversely, if every \(D_r\) has that cycle type, then the values \(a_r=r-\pi(r)\) are distinct: otherwise one \(f_a\) would have two fixed points. Hence the \(a_r\)'s exhaust \(G\), and all \(f_a\) have type \((1,n-1)\).

There is also an equivalent subset formulation. Let
\[
d(x)=x-\pi(x).
\]
Then \(\max_a c(f_a)=2\) is equivalent to:

1. \(d\) is a permutation; and
2. there is no subset \(S\subseteq G\) with
   \[
   2\le |S|\le n-2
   \]
   such that \(\pi(S)\) is a translate of \(S\).

Indeed, \(\pi(S)=S-a\) is equivalent to \(f_a(S)=S\). Once \(f_a\) has a unique fixed point, the absence of such a proper invariant subset says that all remaining \(n-1\) points form one cycle.

For checking a proposed candidate, the following exact \(O(n^2)\) procedure suffices:

```python
def is_extremal_candidate(pi):
    n = len(pi)
    if sorted(pi) != list(range(n)):
        return False

    for r in range(n):
        D = [(pi[(r + x) % n] - pi[r]) % n for x in range(n)]

        x = 1
        seen = set()
        for _ in range(n - 1):
            if x == 0 or x in seen:
                return False
            seen.add(x)
            x = D[x]

        if x != 1 or len(seen) != n - 1:
            return False

    return True
```

This is only a certificate checker; I have not performed or claimed an exhaustive computation for \(n=25\).

## 9. Remaining gap

For \(\gcd(n,6)=1\), the strong-complete-mapping obstruction alone is insufficient. For example,
\[
\pi(x)=2x
\]
makes \(\pi\), \(x-\pi(x)=-x\), and \(x+\pi(x)=3x\) permutations for every such \(n\). At composite \(n\), however, this map preserves proper additive subgroups, so it cannot be extremal.

What remains unproved is that every possibly highly nonlinear permutation of a composite cyclic group must still produce either:

- a based derivative \(D_r\) with at least three cycles, or equivalently
- a nontrivial subset \(S\) whose image is a translate of \(S\).

The arguments above do not force such a subset once all congruence blocks are thoroughly mixed. In particular, they do not settle \(n=25,35,49,\ldots\), and no counterexample is produced.