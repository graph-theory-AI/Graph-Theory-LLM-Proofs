```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The limit is not settled, but two refined upper bounds force the conjectured constant 1/2 under checkable overlap or inertia conditions.",
  "would_publish": false,
  "caveats": "The remaining case permits both quadratically many two-orientation coordinate overlaps and linearly many positive eigenvalues; novelty relative to the cited preprints was not verified."
}
```

# Mathematical writeup

## 1. Statement and outcome

Work in the equivalent code formulation. For \(x,y\in\{0,1,*\}^d\), put
\[
\delta(x,y)=\bigl|\{i:\{x_i,y_i\}=\{0,1\}\}\bigr|.
\]
A code \(\mathcal C\subseteq\{0,1,*\}^d\) is 2-neighborly when
\[
1\leq \delta(x,y)\leq 2
\qquad(x\neq y\in\mathcal C).
\]
Then \(n(2,d)\) is the largest possible \(|\mathcal C|\).

I do not prove existence of the limit. I obtain the following self-contained partial results.

### Theorem

Let \(\mathcal C\) be a 2-neighborly code of length \(d\), and let \(N=|\mathcal C|\).

1. For each \(i<j\), let \(c_{ij}\in\{0,1,2\}\) be the number of antipodal pairs
   \[
   (00,11),\qquad (01,10)
   \]
   both of whose cells occur among codewords which are nonstar in coordinates \(i,j\). Then
   \[
   N\leq 1+d+\sum_{i<j}c_{ij}. \tag{1}
   \]
   In particular,
   \[
   N\leq d^2+1. \tag{2}
   \]

2. If \(b\) is the number of pairs \(i<j\) for which all four binary patterns \(00,01,10,11\) occur, and \(z\) is the number for which neither antipodal pair occurs, then
   \[
   N\leq 1+d+\binom d2+b-z. \tag{3}
   \]
   Consequently, if extremal codes can be chosen with \(b-z=o(d^2)\), then
   \[
   \lim_{d\to\infty}\frac{n(2,d)}{d^2}=\frac12.
   \]

3. Let \(M\) be the coverage matrix
   \[
   M_{xy}=\delta(x,y),
   \]
   with zero diagonal, and put
   \[
   p=n_+(M),\qquad q=n_-(M).
   \]
   Then \(p,q\leq d\) and
   \[
   N\leq q+\binom{p+1}{2}+\binom{q+1}{2}. \tag{4}
   \]
   Thus, if \(p=o(d)\), then
   \[
   N\leq \left(\frac12+o(1)\right)d^2.
   \]
   In particular, if \(M\) has exactly one positive eigenvalue, then
   \[
   N\leq \binom{d+2}{2}. \tag{5}
   \]

4. If \(\mathcal C\) contains a word with no stars, then
   \[
   N\leq 1+\binom{d+1}{2}. \tag{6}
   \]

Combining (2) with the supplied lower bound gives the unconditional interval
\[
\frac12
\leq
\liminf_{d\to\infty}\frac{n(2,d)}{d^2}
\leq
\limsup_{d\to\infty}\frac{n(2,d)}{d^2}
\leq 1.
\]

The significance of (3) and (4) is that any failure of the conjectured limit must occur in a rather specific simultaneous regime.

---

## 2. Signed biclique decomposition

For each coordinate \(i\), define
\[
A_i=\{x\in\mathcal C:x_i=0\},\qquad
B_i=\{x\in\mathcal C:x_i=1\},
\]
and let \(E_i\) be the adjacency matrix of the complete bipartite graph between \(A_i\) and \(B_i\). Then
\[
M=\sum_{i=1}^d E_i
\]
and \(M_{xy}=\delta(x,y)\in\{1,2\}\) for \(x\neq y\).

Since
\[
t-\binom t2=1\qquad(t=1,2),
\]
entrywise we have
\[
J-I
=
\sum_{i=1}^dE_i-\sum_{i<j}E_i\circ E_j, \tag{7}
\]
where \(\circ\) denotes Hadamard product.

For fixed \(i<j\), set
\[
C_{ab}^{ij}=\{x\in\mathcal C:x_i=a,\ x_j=b\},
\qquad a,b\in\{0,1\}.
\]
The graph represented by \(E_i\circ E_j\) is the disjoint union of at most two bicliques:
\[
K_{C_{00}^{ij},C_{11}^{ij}}
\quad\text{and}\quad
K_{C_{01}^{ij},C_{10}^{ij}}. \tag{8}
\]
The number of nonempty bicliques in (8) is precisely \(c_{ij}\).

We use the signed form of the Graham–Pollak inertia argument.

### Lemma

If
\[
A(K_N)=\sum_{\ell=1}^m \lambda_\ell A(K_{X_\ell,Y_\ell}),
\]
where all \(\lambda_\ell\neq0\), then \(m\geq N-1\).

#### Proof

The adjacency matrix of a nonempty biclique has one positive and one negative eigenvalue. Multiplication by a nonzero real number preserves the fact that there is exactly one negative eigenvalue.

For real symmetric matrices,
\[
n_-(R+S)\leq n_-(R)+n_-(S).
\]
Indeed, intersect maximal subspaces on which \(R\) and \(S\) are nonnegative.

Since \(A(K_N)=J-I\) has \(N-1\) negative eigenvalues, at least \(N-1\) weighted biclique matrices are required. \(\square\)

Applying the lemma to (7) and (8) gives
\[
N-1\leq d+\sum_{i<j}c_{ij},
\]
proving (1).

Since \(c_{ij}\leq2\),
\[
N-1\leq d+2\binom d2=d^2,
\]
which proves (2).

If \(b=\#\{c_{ij}=2\}\) and \(z=\#\{c_{ij}=0\}\), then
\[
\sum_{i<j}c_{ij}=\binom d2+b-z.
\]
This proves (3).

A useful consequence is that if
\[
N\geq \left(\frac12+\varepsilon\right)d^2,
\]
then necessarily
\[
b-z\geq \varepsilon d^2-\frac d2-1. \tag{9}
\]
Thus an asymptotic counterexample to the constant \(1/2\) must have a positive quadratic excess of two-orientation coordinate pairs over zero-orientation pairs.

---

## 3. An inertia bound for the coverage matrix

Let the inertia of \(M\) be \((p,q,N-p-q)\). Each \(E_i\) has at most one positive and one negative eigenvalue, so inertia subadditivity gives
\[
p,q\leq d. \tag{10}
\]

Because the off-diagonal entries of \(M\) are \(1\) or \(2\),
\[
J-I=\frac{3M-M\circ M}{2}. \tag{11}
\]

We need a bound on the positive inertia of \(M\circ M\).

Write a spectral factorization
\[
M=XX^{\mathsf T}-YY^{\mathsf T},
\]
where \(X\) has \(p\) columns and \(Y\) has \(q\) columns. Then
\[
\begin{aligned}
M\circ M={}&
(XX^{\mathsf T})\circ(XX^{\mathsf T})
+(YY^{\mathsf T})\circ(YY^{\mathsf T})\\
&-2(XX^{\mathsf T})\circ(YY^{\mathsf T}).
\end{aligned} \tag{12}
\]
The first two summands are positive semidefinite Gram matrices of symmetric tensor-square features. Their combined rank is at most
\[
\binom{p+1}{2}+\binom{q+1}{2}-1. \tag{13}
\]
The subtraction of \(1\) follows from the zero diagonal of \(M\): if \(x_v,y_v\) are the corresponding rows of \(X,Y\), then
\[
\|x_v\|^2=\|y_v\|^2
\]
for every \(v\), so all concatenated tensor-square feature vectors lie in one fixed hyperplane.

The final summand in (12), before multiplication by \(-2\), is positive semidefinite. Hence
\[
n_+(M\circ M)
\leq
\binom{p+1}{2}+\binom{q+1}{2}-1. \tag{14}
\]

Taking negative inertia in (11),
\[
\begin{aligned}
N-1
&=n_-(J-I)\\
&\leq n_-(M)+n_+(M\circ M)\\
&\leq q+\binom{p+1}{2}+\binom{q+1}{2}-1.
\end{aligned}
\]
This is equivalent to (4):
\[
N\leq q+\binom{p+1}{2}+\binom{q+1}{2}.
\]

Using \(q\leq d\),
\[
N\leq d+\binom{p+1}{2}+\binom{d+1}{2}. \tag{15}
\]
Consequently \(p=o(d)\) implies
\[
N\leq \frac{d^2}{2}+o(d^2).
\]

If \(p=1\), then
\[
N\leq q+1+\binom{q+1}{2}
=\binom{q+2}{2}
\leq\binom{d+2}{2},
\]
proving (5).

Conversely, (15) shows that if
\[
N\geq \left(\frac12+\varepsilon\right)d^2,
\]
then
\[
\frac{p(p+1)}2\geq \varepsilon d^2-\frac{3d}{2},
\]
and hence
\[
p\geq \bigl(\sqrt{2\varepsilon}-o(1)\bigr)d. \tag{16}
\]

Thus any subsequence exceeding the conjectured constant must have both (9) and (16).

---

## 4. A full-support codeword

Suppose \(x\in\mathcal C\) has no stars. For \(y\neq x\), define
\[
S_y=\{i:y_i=1-x_i\}.
\]
Then
\[
|S_y|=\delta(x,y)\in\{1,2\}.
\]

The map \(y\mapsto S_y\) is injective. Indeed, if \(S_y=S_z\), then at coordinates in this set both words have the same symbol opposite to \(x\); outside it both have either \(x_i\) or \(*\). Hence \(y\) and \(z\) have no opposing coordinate, contrary to 2-neighborliness.

There are \(d+\binom d2\) nonempty subsets of \([d]\) of size at most two. Therefore
\[
N-1\leq d+\binom d2,
\]
which proves (6).

---

## 5. The lower construction and why the inertia condition is natural

For completeness, here is a direct construction attaining the known asymptotic lower constant.

Let
\[
L_m=
\{1^r0*^{\,m-r-1}:0\leq r<m\}\cup\{1^m\}.
\]
This is a 1-neighborly code of length \(m\) and size \(m+1\): every two distinct words have exactly one opposing coordinate.

Fix integers \(r,m\). Let the groups be indexed by the
\[
g=\binom r2
\]
edges of \(K_r\). Use:

- \(r\) factor blocks, each of length \(m\);
- one tag block of length \(g-1\), containing a copy of \(L_{g-1}\), one tag for each group.

For a group \(e=\{i,j\}\), take all \((m+1)^2\) words which contain arbitrary members of \(L_m\) in factor blocks \(i,j\), stars in all other factor blocks, and the fixed tag assigned to \(e\).

Two words in the same group have one or two oppositions in their two active factor blocks. Two words in different groups have one opposition in the tag block, plus at most one opposition in their unique common factor block. Thus the construction is 2-neighborly.

It has
\[
N=\binom r2(m+1)^2,\qquad
D=rm+\binom r2-1.
\]
Taking \(r\to\infty\) and \(r=o(m)\) gives
\[
\frac{N}{D^2}\longrightarrow\frac12.
\]

Its coverage matrix is a sum of \(r+1\) matrices each having one positive eigenvalue:

- the tag contribution is a complete multipartite adjacency matrix;
- each factor contribution is also a complete multipartite adjacency matrix on the vertices active in that factor.

Hence
\[
n_+(M)\leq r+1=o(D).
\]
Thus the inertia estimate (4) is asymptotically sharp on this natural lower-bound construction.

On the other hand, this construction has quadratically many coordinate pairs realizing all four binary patterns. Therefore the overlap condition \(b=o(d^2)\) is not automatic; the spectral condition is genuinely broader.

---

## 6. Exact small cases and an exact finite search formulation

The face corresponding to \(x\in\{0,1,*\}^d\) is
\[
F_x=\{u\in\{0,1\}^d:u_i=x_i\text{ whenever }x_i\neq *\}.
\]
Two such faces intersect exactly when \(\delta(x,y)=0\).

It follows immediately that
\[
n(2,1)=2,\qquad n(2,2)=4.
\]

For \(d=3\), pairwise disjointness of the faces gives the exact value
\[
n(2,3)=6.
\]
Indeed, if there are \(r\) nonsingleton faces and \(s\) singleton faces, then
\[
2r+s\leq8.
\]
The singleton vertices cannot contain an antipodal pair, so \(s\leq4\). Hence
\[
r+s\leq4+\frac s2\leq6.
\]
Equality is attained by
\[
00*,\quad 01*,\quad 100,\quad101,\quad110,\quad111.
\]

For larger \(d\), an exact integer program is:

- one binary variable \(x_w\) for each \(w\in\{0,1,*\}^d\);
- maximize \(\sum_w x_w\);
- impose
  \[
  x_u+x_v\leq1
  \]
  for every distinct \(u,v\) with \(\delta(u,v)\notin\{1,2\}\).

An optimality certificate from any exact MILP or CP-SAT solver certifies \(n(2,d)\).

---

## 7. Remaining gap

The supplied lower bound and the results above show that failure of the limit would require an extremal subsequence with all of the following properties:

1. no full-support codeword;
2. \(b-z=\Omega(d^2)\), where \(b,z\) are the two- and zero-orientation coordinate-pair counts;
3. \(n_+(M)=\Omega(d)\).

Neither condition 2 nor condition 3 is individually impossible. Dense four-pattern overlap occurs in product-type constructions, while linear positive inertia can be produced by tagged sums of small double-covered blocks. What is missing is a stability theorem ruling out their simultaneous occurrence in a code of size \((1/2+\varepsilon)d^2\).

Therefore the existence of
\[
\lim_{d\to\infty}\frac{n(2,d)}{d^2}
\]
remains unresolved by this argument. The inequalities above isolate a narrower structural regime in which a counterexample or oscillation would have to lie.