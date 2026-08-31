```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The universal threshold remains open, but exponential decay follows whenever S is more than half dense in an additive subgroup, resolving many boundary cases and sets of size as small as 3 in extension fields.",
  "would_publish": false,
  "caveats": "Balanced boundary sets and arbitrary nonlinear sets in the prime-field two-point case remain untreated."
}
```

# 1. Statement and notation

Write \(\operatorname{ex}_{q,S}(n)\) for the largest size of \(A\subseteq\mathbb F_q^n\) such that there are no
\[
x,\quad x+d,\quad x+2d\in A
\]
with \(0\ne d\in S^n\). The target is to prove
\[
\operatorname{ex}_{q,S}(n)\le q^{(1-\varepsilon)n}
\tag{1}
\]
for a wider range of \(S\) than \(|S|>(q+1)/2\).

I obtain an unconditional structured extension, a reduction of the two-point problem to prime fields, and an exact result for affine subspaces.

# 2. A section lemma

## Proposition 2.1

Let \(q=p^k\), let \(H\le (\mathbb F_q,+)\) be an additive subgroup of size \(h=p^r\), and let
\[
T\subseteq S\cap H,\qquad 0\in T.
\]
Choose an additive isomorphism \(\phi:H\to\mathbb F_h\). Suppose that for some \(\eta>0\),
\[
\operatorname{ex}_{h,\phi(T)}(n)\le h^{(1-\eta)n}
\quad\text{for every }n.
\tag{2}
\]
Then
\[
\operatorname{ex}_{q,S}(n)
 \le q^n h^{-\eta n}
 =q^{(1-\eta\log_q h)n}.
\tag{3}
\]

### Proof

Partition \(\mathbb F_q^n\) into the \((q/h)^n\) cosets of \(H^n\). For each coset \(u+H^n\), the section
\[
A_u=\{v\in H^n:u+v\in A\}
\]
contains no progression with nonzero difference in \(T^n\), since \(T^n\subseteq S^n\). The coordinatewise map induced by \(\phi\) preserves addition and doubling, so (2) gives
\[
|A_u|\le h^{(1-\eta)n}.
\]
Summing over all cosets proves (3). \(\square\)

## Corollary 2.2: local half-density criterion

If some nontrivial additive subgroup \(H\le\mathbb F_q\), of size \(h\), satisfies
\[
|S\cap H|>\frac{h+1}{2},
\tag{4}
\]
then (1) holds.

Indeed, apply the supplied Theorem 1 over the additive group \(H\), identified with \(\mathbb F_h\), and then Proposition 2.1.

This is a genuine improvement over a cardinality-only threshold: \(S\) itself can be very small compared with \(q\).

## Corollary 2.3: additive subgroups contained in \(S\)

If \(S\) contains a nontrivial additive subgroup \(H\), then (1) holds. Here one takes \(T=H\), for which
\[
|T|=h>\frac{h+1}{2}.
\]

For example, if \(q=3^k\) and
\[
\{0,a,-a\}\subseteq S
\]
for some \(a\ne0\), then
\[
|A|\le q^{(1-\varepsilon)n}
\]
for some \(\varepsilon>0\), even though \(|S|\) may be only \(3\).

# 3. Consequence for the boundary \(|S|=(q+1)/2\)

Let \(q=p^k\). The nonzero elements of \(\mathbb F_q\) partition into the one-dimensional \(\mathbb F_p\)-subspaces
\[
L=a\mathbb F_p,
\]
of which there are \((q-1)/(p-1)\). If
\[
|S|=\frac{q+1}{2},
\]
then
\[
\sum_L |(S\setminus\{0\})\cap L|=\frac{q-1}{2},
\]
so the average intersection is
\[
\frac{p-1}{2}.
\]

Hence:

## Corollary 3.1

Suppose \(|S|=(q+1)/2\). Unless
\[
|(S\setminus\{0\})\cap L|=\frac{p-1}{2}
\tag{5}
\]
for every one-dimensional \(\mathbb F_p\)-subspace \(L\), the desired exponential bound holds.

### Proof

If (5) fails, some line \(L\) has more than \((p-1)/2\) nonzero elements of \(S\). Thus
\[
|S\cap L|>\frac{p+1}{2}.
\]
Apply Corollary 2.2 with \(H=L\). \(\square\)

In characteristic \(3\), condition (5) says that \(S\) contains exactly one element from each pair \(\{a,-a\}\). Thus every characteristic-\(3\) boundary case is resolved except the “skew” case
\[
S\cap(-S)=\{0\},
\qquad
S\cup(-S)=\mathbb F_q.
\tag{6}
\]

This includes the core example \(q=3\), \(S=\{0,1\}\).

# 4. Reduction of the two-point problem to prime fields

The following is conditional and is not being claimed as a proof of the conjecture.

## Proposition 4.1

Fix an odd prime \(p\). Suppose there is \(\eta_p>0\) such that
\[
\operatorname{ex}_{p,\{0,1\}}(n)\le p^{(1-\eta_p)n}
\tag{7}
\]
for every \(n\). Then for every \(q=p^k\) and every \(S\subseteq\mathbb F_q\) with \(0\in S\) and \(|S|\ge2\),
\[
\operatorname{ex}_{q,S}(n)\le q^{(1-\eta_p/k)n}.
\tag{8}
\]

### Proof

Choose \(s\in S\setminus\{0\}\) and let
\[
H=s\mathbb F_p.
\]
Under \(as\mapsto a\), the set \(\{0,s\}\) corresponds to \(\{0,1\}\). Proposition 2.1 gives
\[
|A|\le (q/p)^n p^{(1-\eta_p)n}
=q^n p^{-\eta_p n}
=q^{(1-\eta_p/k)n}.
\]
\(\square\)

Thus the proposed extension down to \(|S|=2\), in every field of characteristic \(p\), would follow from the single prime-field case \((\mathbb F_p,\{0,1\})\).

# 5. Exact answer for affine subspaces

The nonlinear problem remains open, but the two-point case can be solved exactly when \(A\) is required to be affine-linear.

## Theorem 5.1

Let \(p\) be an odd prime and \(S=\{0,1\}\). Among affine subspaces \(A\subseteq\mathbb F_p^n\) containing no nontrivial \(S^n\)-difference progression, the maximum dimension is
\[
n-\left\lceil\frac{n}{p-1}\right\rceil.
\tag{9}
\]
Equivalently, the largest such affine subspace has size
\[
p^{\,n-\lceil n/(p-1)\rceil}.
\tag{10}
\]

### Proof

Write \(A=x_0+V\), where \(V\le\mathbb F_p^n\). Such an affine space is progression-free precisely when
\[
V\cap\bigl(\{0,1\}^n\setminus\{0\}\bigr)=\varnothing.
\tag{11}
\]

Let \(m=\operatorname{codim}V\), and choose a rank-\(m\) linear map
\[
L:\mathbb F_p^n\to\mathbb F_p^m
\]
with kernel \(V\). Put \(v_i=L(e_i)\). A nonempty binary vector \(1_I\) belongs to \(V\) exactly when
\[
\sum_{i\in I}v_i=0.
\tag{12}
\]

We use the standard zero-sum bound
\[
N>m(p-1)\quad\Longrightarrow\quad
\text{every sequence of \(N\) elements of \(\mathbb F_p^m\) has a nonempty zero-sum subsequence.}
\tag{13}
\]

For completeness, let \(G=\mathbb F_p^m\) and work in \(\mathbb F_p[G]\). Its augmentation ideal \(J\) satisfies
\[
J^{m(p-1)+1}=0,
\]
because
\[
\mathbb F_p[G]\cong
\mathbb F_p[y_1,\dots,y_m]/(y_1^p,\dots,y_m^p).
\]
If \(v_1,\dots,v_N\) had no nonempty zero-sum subsequence and \(N>m(p-1)\), then
\[
\prod_{i=1}^N(1-g^{v_i})=0.
\]
But the coefficient of the identity in the expansion would be \(1\), contributed only by the empty subset, a contradiction. This proves (13).

Applying (13) to the columns \(v_i\), condition (11) forces
\[
n\le m(p-1),
\]
and hence
\[
m\ge\left\lceil\frac{n}{p-1}\right\rceil.
\]

Conversely, let \(m=\lceil n/(p-1)\rceil\), and choose positive integers
\[
r_1+\cdots+r_m=n,\qquad 1\le r_j\le p-1.
\]
Take the columns of \(L\) to consist of \(r_j\) copies of the \(j\)-th standard basis vector of \(\mathbb F_p^m\). A subset sum is zero only if each basis vector is used a multiple of \(p\) times; since at most \(p-1\) copies of each are available, only the empty subset sums to zero. Thus \(\ker L\) satisfies (11) and has the claimed dimension. \(\square\)

This also applies to \(S=\{0,s\}\) after scaling.

# 6. Exact small cases for the unresolved core

Take \(q=3\) and \(S=\{0,1\}\).

## Proposition 6.1

\[
\operatorname{ex}_{3,\{0,1\}}(1)=2,
\qquad
\operatorname{ex}_{3,\{0,1\}}(2)=6.
\]

### Proof

The first equality is immediate.

For \(n=2\), the fixed allowed direction \((1,0)\) partitions \(\mathbb F_3^2\) into three affine lines, each of which contributes at most two points. Hence \(|A|\le6\).

For equality, let
\[
B=\{(0,0),(1,2),(2,1)\}
  =\{(t,-t):t\in\mathbb F_3\},
\qquad
A=\mathbb F_3^2\setminus B.
\]
The allowed projective directions are
\[
(1,0),\quad(0,1),\quad(1,1).
\]
The set \(B\) meets every line in each of these three parallel classes exactly once: the relevant invariants \(y\), \(x\), and \(y-x\) respectively take all three values on \(B\). Consequently every allowed line contains exactly two points of \(A\), so \(A\) is progression-free. \(\square\)

Cartesian products of progression-free sets are progression-free. Therefore
\[
\operatorname{ex}_{3,\{0,1\}}(2k)\ge6^k,
\qquad
\operatorname{ex}_{3,\{0,1\}}(2k+1)\ge2\cdot6^k.
\tag{14}
\]
Thus nonlinear examples already substantially exceed the best affine-subspace construction.

More generally, for \(q=p\), \(S=\{0,1\}\), there are progression-free sets of size
\[
\frac{(p-1)^n}{(n+1)^{p-2}}.
\tag{15}
\]
Indeed, take a largest fixed-composition class of words in \((\mathbb F_p\setminus\{0\})^n\). If \(y=x+d\) with \(d\in\{0,1\}^n\) and \(x,y\) have the same composition, let \(D_j\) count active coordinates starting with symbol \(j\). Equality of compositions gives
\[
D_j=D_{j-1}\quad\text{for every }j\in\mathbb F_p.
\]
Since \(D_0=0\), all \(D_j=0\), so \(d=0\).

# 7. Why the existing total-degree argument stops at the boundary

Let
\[
P(t)=\prod_{a\notin S}(t-a).
\]
Then \(P\) vanishes outside \(S\), is nonzero on \(S\), and has degree \(q-|S|\). The natural one-coordinate tensor is represented by
\[
\bigl(1-(x+z-2y)^{q-1}\bigr)P(y-x),
\tag{16}
\]
of total degree
\[
D=(q-1)+(q-|S|).
\]

At the boundary
\[
|S|=\frac{q+1}{2},
\qquad
r=\frac{q-1}{2},
\]
one has \(D=3r\). For \(n\) coordinates, every monomial has total degree at most \(3rn\), so one of its three variable blocks has degree at most \(rn\). But
\[
M_q(n)=
\#\left\{(a_1,\dots,a_n)\in\{0,\dots,q-1\}^n:
\sum_i a_i\le rn\right\}
\ge\frac{q^n}{2},
\]
by the involution \(a_i\mapsto q-1-a_i\). Hence the standard slice decomposition gives only
\[
|A|\le3M_q(n),
\]
which is worse than the trivial \(q^n\) bound. Thus the straightforward total-degree argument genuinely gives no exponential saving at equality; a new ingredient is needed.

# 8. Remaining gap

The results above do not establish a universal cardinality improvement. In particular, they do not handle:

1. balanced boundary sets satisfying (5);
2. the prime-field problem \(q=p,\ S=\{0,1\}\);
3. arbitrary nonlinear \(A\) in that two-point case.

The smallest unresolved core is already
\[
q=3,\qquad S=\{0,1\}.
\]
A completely reproducible finite computation of further cases is the \(0\)-\(1\) integer program
\[
\max\sum_{v\in\mathbb F_q^n}X_v
\]
subject to
\[
X_x+X_{x+d}+X_{x+2d}\le2
\]
for every \(x\in\mathbb F_q^n\) and every \(0\ne d\in S^n\), with \(X_v\in\{0,1\}\). No unreported computational values are being claimed here.