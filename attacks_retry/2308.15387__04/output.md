```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For s >= 1, only r = 2s+1, 2s+2, or 2s+3 are possible, with exact design characterizations and strong arithmetic restrictions in the latter two cases.",
  "would_publish": false,
  "caveats": "The supplied structural reduction checks out, but the residual design-existence families are not settled here; their current literature status has not been verified."
}
```

# A rigorous partial classification

I verified the structural reduction in the supplied attempt. It is valid. In particular, the power-of-two and primality conditions it obtains are **necessary arithmetic conditions, not existence theorems**.

Below I give a self-contained proof, including a verification of the small affirmative examples without relying on an unexecuted program. I also prove an additional symmetry obstruction for the first remaining halving case. This does **not** finish the parameter classification.

Throughout, \(r,s\) are integers with \(1\le s\le r\), and hypergraphs are initially taken to be simple. A remark below shows that allowing edge multiplicities does not change which parameter pairs are possible.

## 1. The partial classification

A \(t\)-\((v,k,\lambda)\) design is a collection of \(k\)-subsets of a \(v\)-set such that every \(t\)-subset belongs to exactly \(\lambda\) blocks. Write \(S(t,k,v)\) when \(\lambda=1\).

### Theorem

An \(r\)-vertex, \((s+1)\)-uniform intersecting hypergraph in which every \((r-s)\)-set contains the same positive number of edges can exist only in the following cases:

\[
\begin{array}{c|c|c}
r & \text{Exact required structure} & \text{Necessary arithmetic condition}\\ \hline
2s+1 & \text{the complete }(s+1)\text{-graph} & \text{none}\\[2mm]
2s+2 &
s\text{-}\bigl(2s+2,s+1,(s+2)/2\bigr)\text{ design}
& s+2\text{ is a power of }2\\[2mm]
2s+3 &
S(s,s+1,2s+3)
& s+3\text{ is prime}.
\end{array}
\]

Conversely, every simple design in the middle column has the required property. In the second row it automatically contains exactly one member of every complementary pair of \((s+1)\)-sets. In the third row it is automatically intersecting.

The common number of edges in an \((r-s)\)-set is forced to be
\[
1\quad\text{if }r=2s+1,
\qquad
\frac{s+2}{2}\quad\text{in either exceptional case}.
\]

In particular:

- \(r=2s+1\) always works;
- if \(s\) is odd, it is the **only** possibility;
- the unresolved portion of this argument concerns existence of the two indicated design families.

---

## 2. The uniformity condition is a design condition

Put
\[
n=r,\qquad k=s+1,\qquad t=k-1.
\]
Let \(\mathcal H\subseteq\binom Vk\), and let \(b=|\mathcal H|\).

Positivity immediately requires
\[
n-k+1\ge k,
\qquad\text{so}\qquad n\ge 2k-1. \tag{1}
\]

For \(U\subseteq V\), define
\[
D(U)=|\{B\in\mathcal H:B\cap U=\varnothing\}|,
\qquad
N(U)=|\{B\in\mathcal H:U\subseteq B\}|.
\]
The hypothesis says that \(D(U)\) is constant for all \(t\)-subsets \(U\).

Suppose \(D(U)\) is constant on \(j\)-subsets. For a \((j-1)\)-subset \(W\),
\[
\sum_{x\notin W}D(W\cup\{x\})
=(n-k-j+1)D(W). \tag{2}
\]
Indeed, an edge disjoint from \(W\) is counted once for each vertex outside \(W\cup B\). The coefficient on the right is positive by (1). Descending induction therefore shows that \(D(U)\) depends only on \(|U|\) whenever \(|U|\le k-1\).

Inclusion-exclusion gives
\[
N(S)=\sum_{I\subseteq S}(-1)^{|I|}D(I).
\]
Thus \(N(S)\) also depends only on \(|S|\) for \(|S|\le k-1\). Consequently, \(\mathcal H\) is a \((k-1)\)-design.

Writing
\[
\rho=\frac{b}{\binom nk},
\]
its parameters are
\[
\lambda_j
=b\frac{\binom kj}{\binom nj}
=\rho\binom{n-j}{k-j}
\qquad(0\le j\le k-1). \tag{3}
\]

Conversely, a nonempty \((k-1)\)-design has constant \(D(U)\) on \((k-1)\)-sets. Its value is
\[
D(U)=\rho\binom{n-k+1}{k}>0
\]
under (1). Hence the original uniformity condition is exactly the design condition in the relevant range.

---

## 3. A useful inclusion-exclusion identity

For an arbitrary \(k\)-set \(X\), put
\[
x_X=\mathbf 1_{\{X\in\mathcal H\}},
\qquad
q=\binom{n-k}{k}.
\]

Using (3) for all proper subsets of \(X\), and then comparing with inclusion-exclusion in the complete \(k\)-graph, gives
\[
\begin{aligned}
D(X)
&=\sum_{j=0}^{k-1}(-1)^j\binom kj\lambda_j+(-1)^k x_X\\
&=\rho\bigl(q-(-1)^k\bigr)+(-1)^k x_X. \tag{4}
\end{aligned}
\]

This identity accounts for most of the restriction.

### The boundary \(n=2k-1\)

Here \(q=0\). Taking \(X\) to be an edge, intersectingness gives \(D(X)=0\), so (4) forces \(\rho=1\). Thus the complete \(k\)-graph is forced. It works because two \(k\)-sets on \(2k-1\) vertices intersect.

### Even \(k\)

Suppose \(n\ge2k\). Then \(q\ge1\). If \(k\) is even and \(X\) is an edge, (4) says
\[
0=\rho(q-1)+1,
\]
which is impossible.

Thus even \(k\), equivalently odd \(s\), permits only \(n=2k-1\).

### Odd \(k\)

For an edge \(X\), equation (4) becomes
\[
0=\rho(q+1)-1.
\]
Therefore
\[
\rho=\frac1{q+1},
\qquad
b=\frac{\binom nk}{\binom{n-k}{k}+1}, \tag{5}
\]
and
\[
\lambda_{k-1}
=\frac{n-k+1}{\binom{n-k}{k}+1}. \tag{6}
\]

If \(n\ge2k+2\), put \(m=n-k\). Then \(m\ge k+2\), and
\[
\binom mk>m.
\]
For example, this follows from \(2\le k\le m-2\) and
\(\binom mk\ge\binom m2>m\). Equation (6) would consequently give
\[
0<\lambda_{k-1}<1,
\]
contradicting integrality.

Hence only
\[
n=2k-1,\quad 2k,\quad 2k+1 \tag{7}
\]
can occur.

Notice also that, for every surviving odd-\(k\) example, (4) simplifies to
\[
D(X)=1-x_X
\qquad\text{for every }X\in\binom Vk. \tag{8}
\]

---

## 4. The two exceptional cases

### 4.1. \(n=2k\): a halving

Here \(q=1\), so
\[
\rho=\frac12,
\qquad
\lambda_j=\frac12\binom{2k-j}{k-j},
\qquad
\lambda_{k-1}=\frac{k+1}{2}. \tag{9}
\]

Conversely, suppose a simple
\[
(k-1)\text{-}\bigl(2k,k,(k+1)/2\bigr)
\]
design exists. Its index is integral only when \(k\) is odd, and its density is \(1/2\). Since the only \(k\)-set disjoint from \(X\) is \(X^c\), equation (4) gives
\[
x_{X^c}=1-x_X.
\]
It therefore contains exactly one member of each complementary pair and is intersecting.

#### All parameter divisibilities are equivalent to \(k+1\) being a power of two

In (9), set \(a=k-j\). Integrality requires
\[
\binom{k+a}{a}\equiv0\pmod2
\qquad(1\le a\le k). \tag{10}
\]

The elementary binary parity rule says
\[
\binom{k+a}{a}\text{ is odd}
\quad\Longleftrightarrow\quad
k\mathbin{\&}a=0, \tag{11}
\]
where \(\&\) is bitwise intersection. One obtains this, for example, from
\[
(1+x)^m=\prod_{i:m_i=1}(1+x^{2^i})
\quad\text{over }\mathbb F_2.
\]

If a binary digit of \(k\) below its leading digit is zero, choosing \(a\) to have just that digit set violates (10). Conversely, if all these digits are one, every \(1\le a\le k\) shares a nonzero binary digit with \(k\), so (10) holds.

Thus all the parameter divisibilities hold exactly when
\[
k=2^a-1,
\quad\text{or equivalently}\quad
s+2=2^a. \tag{12}
\]

This proves arithmetic admissibility, **not** existence.

### 4.2. \(n=2k+1\): a Steiner system

Now \(q=k+1\), giving
\[
\rho=\frac1{k+2},
\qquad
\lambda_{k-1}=1.
\]
Thus the required hypergraph must be
\[
S(k-1,k,2k+1). \tag{13}
\]

Conversely, the parameters of such a system force \(k\) to be odd: its number of blocks through a fixed \((k-2)\)-set is \((k+3)/2\). Its density is \(1/(k+2)\), so equation (4) gives (8). It is therefore intersecting.

#### All parameter divisibilities are equivalent to \(k+2\) being prime

Put \(p=k+2\). With \(d=k-j\), equation (3) becomes
\[
\lambda_j=\frac1p\binom{p+d-1}{d},
\qquad 1\le d\le p-2. \tag{14}
\]
Thus the divisibility requirements are
\[
p\mid \binom{p+d-1}{d}
\qquad(1\le d\le p-2). \tag{15}
\]

If \(p\) is prime, these hold: the numerator product contains \(p\), while \(d!\) is coprime to \(p\).

If \(p\) is composite, let \(q\) be its least prime divisor and take \(d=q\). Among
\[
p,p+1,\ldots,p+q-1,
\]
only \(p\) is divisible by \(q\), whereas \(q!\) contributes one factor of \(q\). Consequently,
\[
v_q\!\left(\binom{p+q-1}{q}\right)=v_q(p)-1,
\]
so the binomial coefficient is not divisible by \(p\). This contradicts (15).

Hence the parameter divisibilities hold exactly when
\[
k+2=s+3\text{ is prime}. \tag{16}
\]

Again, this is not a sufficiency proof.

### An equivalent extension

Equation (8) also gives a useful exact equivalence:
\[
S(k-1,k,2k+1)
\quad\Longleftrightarrow\quad
S(k,k+1,2k+2). \tag{17}
\]

For the forward direction, add \(\infty\) and take the blocks
\[
\{B\cup\{\infty\}:B\in\mathcal H\}
\ \cup\
\{V\setminus B:B\in\mathcal H\}.
\]
A \(k\)-set containing \(\infty\) is covered uniquely by the original Steiner property. A \(k\)-set \(X\subseteq V\) is covered
\[
x_X+D(X)=1
\]
times, by (8). The reverse direction follows by taking the derived design at one point.

---

## 5. Self-contained affirmative examples

Besides the complete examples, the first two exceptional values of \(s\) can be verified explicitly.

### \(s=2,r=6\)

On
\[
V=\{\infty\}\cup\mathbb Z_5,
\]
take
\[
\{\infty,i,i+1\},
\qquad
\{i,i+1,i+3\}
\qquad(i\in\mathbb Z_5).
\]

Every pair containing \(\infty\) occurs twice. A consecutive pair of finite vertices occurs in one block of each type; a nonconsecutive pair occurs in two blocks of the second type. This is a \(2\)-\((6,3,2)\) design.

By Section 4.1 it is intersecting, and every \(4\)-set contains two edges.

### \(s=2,r=7\)

On \(\mathbb Z_7\), take the seven translates of
\[
\{0,1,3\}.
\]
The six ordered nonzero differences of this triple exhaust \(\mathbb Z_7\setminus\{0\}\), so every pair occurs in exactly one block. This is \(S(2,3,7)\), giving the required example.

### \(s=4,r=11\)

Here is a self-contained construction of \(S(4,5,11)\).

Let
\[
V=\mathbb Z_{11},
\qquad
Q=\{1,3,4,5,9\},
\qquad
P_i=Q+i.
\]
Take the eleven sets \(P_i\) and the fifty-five sets
\[
V\setminus(P_i\triangle P_j)
\qquad(i<j). \tag{18}
\]

To verify the construction, observe directly that
\[
|P_i\cap P_j|=2\qquad(i\ne j).
\]
Define a sign vector \(a_i\in\{\pm1\}^{11}\) to be positive on \(P_i\) and negative elsewhere. Then
\[
\sum_x a_i(x)=-1,
\qquad
a_i\cdot a_j=-1\quad(i\ne j).
\]
Consequently the twelve rows
\[
r_\infty=(1,1,\ldots,1),
\qquad
r_i=(1,a_i)\quad(i\in\mathbb Z_{11})
\]
are mutually orthogonal sign vectors of length \(12\).

The blocks in (18), together with the \(P_i\), are exactly the positive coordinates outside the first coordinate of the products \(r_i r_j\), over all unordered pairs of distinct rows. Each has size five.

We need the following elementary fact about these twelve orthogonal rows:

> For four distinct rows, the sum of their coordinatewise product is \(4\) or \(-4\).

To prove it, multiply columns by one of the four rows, making that row all positive. Call the other three rows \(u,v,w\), and let
\[
Z=\sum_x u(x)v(x)w(x).
\]
Their first- and second-order correlations vanish. Thus the number of columns with sign pattern \((a,b,c)\) is
\[
\frac{12+abcZ}{8}.
\]
It follows that \(Z\in\{-12,-4,4,12\}\). If \(|Z|=12\), then \(w=\pm uv\). The four classes determined by \((u,v)\) each have three columns. Any fifth row orthogonal to \(1,u,v,w\) would have sign-sum zero in each class, impossible on three columns. Hence \(Z=\pm4\).

Now consider two of the proposed blocks. If their row pairs share one row, orthogonality shows that their intersection has size two. If their row pairs are disjoint, writing \(I\) for their intersection size gives
\[
4I-8=\pm4,
\]
so \(I\in\{1,3\}\).

Thus the proposed blocks are distinct, and no two contain the same \(4\)-set. There are
\[
\binom{12}{2}=66
\]
blocks, and
\[
66\binom54=\binom{11}{4}.
\]
Therefore every \(4\)-set occurs exactly once. This proves the construction is \(S(4,5,11)\).

These examples and the exclusion theorem give the complete small classification
\[
\begin{array}{c|c}
s&\text{all possible }r\\ \hline
1&3\\
2&5,6,7\\
3&7\\
4&9,11\\
5&11.
\end{array}
\]

---

## 6. An additional obstruction for the first remaining halving

The first halving not settled above is
\[
6\text{-}(14,7,4), \tag{19}
\]
corresponding to \((r,s)=(14,6)\).

The following rules out one natural symmetry-based construction.

### Lemma

A \(6\)-\((14,7,4)\) design cannot have both:

1. a subgroup of automorphisms whose orbits are seven pairs of vertices; and
2. an automorphism permuting these seven pairs with cycle structure
   \[
   (1)(3)(3).
   \]

### Proof

Let \(T\) be the union of the three pairs in one of the \(3\)-cycles. Then \(|T|=6\).

The subgroup in condition 1 preserves \(T\), as does the automorphism in condition 2. On the eight vertices outside \(T\), the group they generate has two orbits:

- the pair fixed in the permutation of pairs, of size \(2\);
- the union of the other three pairs, of size \(6\).

The set
\[
E(T)=\{x\notin T:T\cup\{x\}\text{ is a block}\}
\]
must be invariant under this group. Therefore its size belongs to
\[
\{0,2,6,8\}.
\]
But the design requires \(|E(T)|=4\), a contradiction. \(\square\)

For example, view the fourteen vertices as the affine hyperplanes of \(\mathbb F_2^3\). Translations have seven two-point orbits, pairing complementary hyperplanes. A linear transformation of order three with one-dimensional fixed space induces cycle structure \((1)(3)(3)\) on these pairs. Hence a design in (19) cannot be invariant under both of these natural actions.

This is a symmetry obstruction only; it does not rule out an unrestricted design in (19).

---

## 7. Multiplicities do not create additional parameter pairs

The simple-hypergraph convention is not essential.

Suppose edges have positive multiplicities, and counts include multiplicity. The descent and inclusion-exclusion arguments remain valid. If \(w_X\) is the multiplicity of a \(k\)-set \(X\), equation (4) becomes
\[
D(X)=\rho\bigl(q-(-1)^k\bigr)+(-1)^k w_X,
\]
where \(\rho\) is total multiplicity divided by \(\binom nk\).

For every edge \(X\), intersectingness gives \(D(X)=0\). Thus every positive \(w_X\) has the same value. Dividing by that value produces a simple hypergraph satisfying the original condition. So the existence classification is unchanged.

If \(s=0\) is admitted and isolated vertices are allowed, one singleton edge works for every \(r\ge1\).

---

## 8. What remains unresolved here

The argument leaves two existence questions:

1. For \(s+2=2^a\), does the required simple halving
   \[
   s\text{-}\bigl(2s+2,s+1,(s+2)/2\bigr)
   \]
   exist? The first case not settled here is \(6\)-\((14,7,4)\).

2. For \(s+3\) prime, does
   \[
   S(s,s+1,2s+3)
   \]
   exist? After the verified examples with \(s=2,4\), the first case not settled here is
   \[
   S(8,9,19),
   \]
   equivalently \(S(9,10,20)\).

I have not proved that arithmetic admissibility is sufficient in either family, nor proved general nonexistence beyond the small examples. I also do not assert that every individual residual case remains open in the current design-theory literature.

Thus the established result is the parameter exclusion theorem, the exact structural characterizations, the small complete classifications, and the additional symmetry obstruction—not a complete solution of Question 4.6.