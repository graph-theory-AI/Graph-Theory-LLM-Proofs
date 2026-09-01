```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For s>=1 only r=2s+1, 2s+2, or 2s+3 can occur, with the latter two cases equivalent to sharply constrained halving and Steiner-design existence problems.",
  "would_publish": false,
  "caveats": "The residual design-existence cases are not settled here; simple hypergraphs are assumed."
}
```

# 1. Statement of the reduction

Throughout, a hypergraph is simple. Put
\[
n=r,\qquad k=s+1,\qquad t=k-1=s.
\]
Thus the hypothesis asks for an intersecting \(k\)-uniform hypergraph \(\mathcal H\) on \(n\) vertices such that every \((n-k+1)\)-set contains the same positive number of edges.

The following gives a nearly complete classification.

## Theorem

Assume \(k\ge 2\). Such a hypergraph exists only in one of the following three cases.

1. **The automatic case**
   \[
   n=2k-1.
   \]
   Here \(\mathcal H=\binom{V}{k}\) is forced, and it works.

2. **The halving case**
   \[
   n=2k.
   \]
   Here \(\mathcal H\) must be a simple
   \[
   (k-1)\text{-}(2k,k,(k+1)/2)
   \]
   design which contains exactly one member of each complementary pair of \(k\)-sets. Equivalently, it is a halving of the complete \((k-1)\)-design. A necessary divisibility condition is
   \[
   k=2^a-1.
   \]

3. **The Steiner case**
   \[
   n=2k+1.
   \]
   Here \(\mathcal H\) must be a Steiner system
   \[
   S(k-1,k,2k+1).
   \]
   A necessary divisibility condition is
   \[
   k+2\ \text{is prime}.
   \]
   Every such Steiner system is automatically intersecting and satisfies the original condition.

Conversely, every design in cases 2 or 3 gives a hypergraph with the required properties.

In the original variables, for \(s\ge1\):

- \(r=2s+1\) always works;
- \(r=2s+2\) can work only if \(s+2\) is a power of two, and is equivalent to the indicated halving;
- \(r=2s+3\) can work only if \(s+3\) is prime, and is equivalent to \(S(s,s+1,2s+3)\);
- no other \(r\) can work.

In particular, if \(s\) is odd, then the complete case \(r=2s+1\) is the only possibility.

# 2. The uniformity condition forces a design

For \(U\subseteq V\), write
\[
D(U)=|\{B\in\mathcal H:B\cap U=\varnothing\}|.
\]
The original condition says exactly that \(D(U)\) is a fixed positive constant for all \(t=k-1\) element sets \(U\).

First, positivity requires
\[
n-k+1\ge k,
\]
and hence
\[
n\ge 2k-1.
\]

We now descend from \((k-1)\)-sets. Suppose \(D(U)\) is constant for all \(j\)-sets \(U\). If \(W\) has size \(j-1\), then
\[
\sum_{x\in V\setminus W}D(W\cup\{x\})
=(n-k-j+1)D(W).
\]
Indeed, an edge disjoint from \(W\) is counted once for each
\[
x\in V\setminus(W\cup B),
\]
of which there are \(n-k-j+1\). Since \(n\ge2k-1\) and \(j\le k-1\), this coefficient is positive. Hence \(D(W)\) is constant over all \((j-1)\)-sets. Induction shows that \(D(U)\) depends only on \(|U|\) for every \(|U|\le k-1\).

For \(S\subseteq V\), let
\[
N(S)=|\{B\in\mathcal H:S\subseteq B\}|.
\]
Inclusion-exclusion gives
\[
D(S)=\sum_{I\subseteq S}(-1)^{|I|}N(I),
\]
and Möbius inversion gives
\[
N(S)=\sum_{I\subseteq S}(-1)^{|I|}D(I).
\]
Thus \(N(S)\) also depends only on \(|S|\) for every \(|S|\le k-1\).

Consequently, \(\mathcal H\) is a \((k-1)\)-design. If
\[
b=|\mathcal H|
\]
and \(\lambda_j\) denotes the number of edges through a fixed \(j\)-set, then
\[
\lambda_j=b\,\frac{\binom{k}{j}}{\binom{n}{j}}
\qquad (0\le j\le k-1).
\]

Conversely, any nonempty \((k-1)\)-design has constant positive \(D(U)\) on \((k-1)\)-sets when \(n\ge2k-1\). Thus the original uniformity condition is exactly a design condition in the relevant range.

# 3. Counting blocks disjoint from one edge

Fix \(B\in\mathcal H\). Since \(\mathcal H\) is intersecting, no edge is disjoint from \(B\). Inclusion-exclusion therefore gives
\[
0
=\sum_{J\subseteq B}(-1)^{|J|}N(J)
=b\sum_{j=0}^{k-1}(-1)^j
   \frac{\binom{k}{j}^2}{\binom{n}{j}}
  +(-1)^k.
\]

The binomial identity
\[
\sum_{j=0}^{k}(-1)^j
\frac{\binom{k}{j}^2}{\binom{n}{j}}
=
\frac{\binom{n-k}{k}}{\binom nk}
\]
is simply inclusion-exclusion for the probability that a random \(k\)-set avoids a fixed \(k\)-set. Hence, putting
\[
q=\binom{n-k}{k},
\]
we obtain
\[
b\bigl(q-(-1)^k\bigr)+(-1)^k\binom nk=0. \tag{1}
\]

## The boundary \(n=2k-1\)

Here \(q=0\), and (1) gives
\[
b=\binom{2k-1}{k}.
\]
Thus every \(k\)-set is an edge. This also follows directly because the tested subsets themselves have size \(k\). The complete \(k\)-graph on \(2k-1\) vertices is intersecting.

## Even \(k\)

Suppose \(n\ge2k\) and \(k\) is even. Then (1) becomes
\[
b(q-1)=-\binom nk.
\]
For \(n=2k\), \(q=1\), giving an immediate contradiction. For \(n>2k\), the left coefficient is positive and the equation forces \(b<0\). Thus no case beyond \(n=2k-1\) is possible when \(k\) is even.

## Odd \(k\)

For odd \(k\), equation (1) gives
\[
b=\frac{\binom nk}{\binom{n-k}{k}+1}. \tag{2}
\]
The number of blocks through a fixed \((k-1)\)-set is therefore
\[
\lambda_{k-1}
=b\frac{k}{\binom n{k-1}}
=
\frac{n-k+1}{\binom{n-k}{k}+1}. \tag{3}
\]

Write \(n=2k+a\), with \(a\ge0\). If \(a\ge2\) and \(k\ge2\), then
\[
\binom{k+a}{k}>k+a,
\]
so (3) gives \(0<\lambda_{k-1}<1\), impossible because \(\lambda_{k-1}\) is an integer. Hence
\[
n\le2k+1.
\]

This proves that only \(2k-1,2k,2k+1\) can occur.

# 4. The case \(n=2k\): halvings

For odd \(k\), equations (2) and (3) give
\[
b=\frac12\binom{2k}{k},
\qquad
\lambda_{k-1}=\frac{k+1}{2}.
\]
More generally,
\[
\lambda_j
=\frac12\binom{2k-j}{k-j}
\qquad(0\le j\le k-1). \tag{4}
\]
Thus \(\mathcal H\) contains exactly half of all \(k\)-sets and is a halving of the complete \((k-1)\)-design.

The fixed-edge calculation above shows that every block has no disjoint block in \(\mathcal H\). Since disjoint \(k\)-sets on \(2k\) vertices are exactly complementary pairs, and since \(b\) equals the number of complementary pairs, \(\mathcal H\) contains exactly one set from each pair
\[
\{E,V\setminus E\}.
\]
Thus every such halving is automatically intersecting.

## Divisibility obstruction

All quantities in (4) must be integers. Let \(a=k-j\). This requires
\[
\binom{k+a}{a}\equiv0\pmod 2
\qquad(1\le a\le k). \tag{5}
\]
By Lucas' parity criterion,
\[
\binom{k+a}{a}\ \text{is odd}
\quad\Longleftrightarrow\quad
(k\mathbin{\&}a)=0,
\]
where \(\&\) denotes bitwise intersection.

Condition (5) holds for every \(1\le a\le k\) exactly when every binary digit below the leading digit of \(k\) is \(1\), namely
\[
k=2^m-1.
\]

This proves the stated necessary arithmetic condition. It is not a sufficiency proof: one still needs a simple halving with the indicated parameters.

The first nontrivial unresolved-by-this-argument instance is
\[
6\text{-}(14,7,4),
\]
corresponding to \(k=7\), \(s=6\), \(r=14\).

# 5. The case \(n=2k+1\): Steiner systems

For odd \(k\), equations (2) and (3) now give
\[
b=\frac{\binom{2k+1}{k}}{k+2},
\qquad
\lambda_{k-1}=1.
\]
Therefore \(\mathcal H\) is precisely a Steiner system
\[
S(k-1,k,2k+1).
\]

Conversely, suppose such a Steiner system exists. Its parameters force the value of \(b\) above. Applying the same inclusion-exclusion calculation to a block shows that it has no disjoint block, so it is automatically intersecting.

In fact, for any \(k\)-set \(X\),
\[
|\{B\in\mathcal H:B\cap X=\varnothing\}|
=
1-\mathbf 1_{\{X\in\mathcal H\}}. \tag{6}
\]
Thus every nonblock has exactly one disjoint block, while every block has none.

## Divisibility obstruction

For a Steiner system \(S(k-1,k,2k+1)\), the number of blocks through a fixed \(j\)-set is
\[
\lambda_j
=
\frac{\binom{2k+1-j}{k-1-j}}
     {\binom{k-j}{k-1-j}}.
\]
Set
\[
a=k-1-j,\qquad p=k+2.
\]
Then
\[
\lambda_j
=\frac{\binom{p+a}{a}}{a+1}
=\frac1p\binom{p+a}{a+1}. \tag{7}
\]
Writing \(d=a+1\), the required divisibility is
\[
p\mid \binom{p+d-1}{d}
\qquad(1\le d\le p-2). \tag{8}
\]

If \(p\) is prime, (8) holds because \(d<p\) and the numerator contains the factor \(p\).

Conversely, suppose \(p\) is composite and let \(q\) be its least prime divisor. Taking \(d=q\),
\[
v_q\!\left(\binom{p+q-1}{q}\right)=v_q(p)-1,
\]
because among \(p,p+1,\dots,p+q-1\), only \(p\) is divisible by \(q\), while \(q!\) contributes one factor of \(q\). Hence the binomial coefficient is not divisible by \(p\). Thus all the necessary divisibilities hold exactly when
\[
k+2=p\ \text{is prime}.
\]

Again, primality is only an admissibility condition, not a proof of existence.

# 6. Equivalent tight Steiner extension

The Steiner case has a useful equivalent formulation.

Given \(\mathcal H=S(k-1,k,2k+1)\) on \(V\), add a point \(\infty\) and define
\[
\widehat{\mathcal H}
=
\{B\cup\{\infty\}:B\in\mathcal H\}
\cup
\{V\setminus B:B\in\mathcal H\}.
\]
Using (6), every \(k\)-subset of \(V\cup\{\infty\}\) lies in exactly one member of \(\widehat{\mathcal H}\). Hence
\[
\widehat{\mathcal H}=S(k,k+1,2k+2).
\]

Conversely, any \(S(k,k+1,2k+2)\) is closed under complementation: inclusion-exclusion shows that every block has exactly one disjoint block, necessarily its complement. Taking the blocks through a fixed point and deleting that point recovers an \(S(k-1,k,2k+1)\).

Thus case 3 is equivalent to the existence of the “tight” Steiner system
\[
S(k,k+1,2k+2).
\]

# 7. Explicit examples and complete small cases

## The halving for \(k=3,n=6\)

Let
\[
V=\{\infty,0,1,2,3,4\},
\]
with arithmetic modulo \(5\). Take the ten triples
\[
A_i=\{\infty,i,i+1\},\qquad
C_i=\{i,i+1,i+3\}
\quad(i\in\mathbb Z_5).
\]
Every pair lies in exactly two blocks, so this is a \(2\)-\((6,3,2)\) design. It contains exactly one triple from each complementary pair and is therefore intersecting. Every \(4\)-set contains exactly two blocks.

## The Fano example for \(k=3,n=7\)

On \(\mathbb Z_7\), take the translates of
\[
\{0,1,3\}.
\]
This is \(S(2,3,7)\), and every \(5\)-set contains exactly two lines.

## The \(S(4,5,11)\) example

The small Witt design gives the case \(k=5,n=11\). Here is a fully specified finite construction and check.

```python
from itertools import combinations

V = frozenset(range(11))
Q = frozenset({1, 3, 4, 5, 9})

P = [
    frozenset((x + i) % 11 for x in Q)
    for i in range(11)
]

W = set(P)
for i, j in combinations(range(11), 2):
    W.add(frozenset(V.difference(P[i] ^ P[j])))

assert len(W) == 66

# Every 4-set is in exactly one block.
for T in combinations(range(11), 4):
    T = frozenset(T)
    assert sum(T <= B for B in W) == 1

# The blocks are pairwise intersecting.
assert all(A & B for A, B in combinations(W, 2))

# Every 7-set contains exactly three blocks.
counts = set()
for M in combinations(range(11), 7):
    M = frozenset(M)
    counts.add(sum(B <= M for B in W))
assert counts == {3}
```

Therefore, for \(1\le s\le5\), the classification is complete:

\[
\begin{array}{c|c}
s & \text{all possible }r\\ \hline
1 & 3\\
2 & 5,6,7\\
3 & 7\\
4 & 9,11\\
5 & 11
\end{array}
\]

# 8. Remaining gap

The reduction leaves two genuine design-existence families.

1. For
   \[
   r=2s+2,\qquad s+2=2^a,
   \]
   one needs a simple halving
   \[
   s\text{-}(2s+2,s+1,(s+2)/2).
   \]
   The first case not settled here is \(6\)-\((14,7,4)\).

2. For
   \[
   r=2s+3,\qquad s+3\ \text{prime},
   \]
   one needs
   \[
   S(s,s+1,2s+3),
   \]
   equivalently \(S(s+1,s+2,2s+4)\). The first case beyond the Fano and small Witt systems is
   \[
   S(8,9,19),
   \]
   equivalently \(S(9,10,20)\).

For example, the \(6\)-\((14,7,4)\) problem can be encoded exactly with binary variables \(x_E\), one per complementary pair of \(7\)-subsets of a \(14\)-set, and constraints
\[
\sum_{\substack{E\supseteq S\\|E|=7}}x_E=4
\qquad\text{for every }S\in\binom{[14]}6,
\]
with \(x_{E^c}=1-x_E\). This has \(1716\) binary variables before further reductions and \(3003\) local equations.

I have not resolved these residual existence questions, nor do I assert here that the current design-theory literature has not resolved any of them. The argument does, however, eliminate every other parameter pair and gives complete answers for all odd \(s\) and for \(s\le5\).