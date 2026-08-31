```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted value remains open, but affine-linear strategies over every field satisfy q≤n for n≥3, so attaining the upper bound n+1 would necessarily require a genuinely nonlinear strategy.",
  "would_publish": false,
  "caveats": "The nonlinear problem is untouched; no SAT computation was run, and overlap with the cited 2021 linear work was not checked."
}
```

# Mathematical writeup

## 1. Statement and outcome

Let the two parts of \(K_{n,n}\) be \(A=\{a_1,\dots,a_n\}\) and \(B=\{b_1,\dots,b_n\}\). Write the hat vectors on the two parts as
\[
x=(x_1,\dots,x_n),\qquad y=(y_1,\dots,y_n)\in Q^n,
\]
where \(|Q|=q\).

The known unrestricted bounds supplied in the question are
\[
\Omega\!\left(n^{1/2-o(1)}\right)\le HG(K_{n,n})\le n+1.
\]
I do not resolve the unrestricted endpoint \(q=n+1\). I prove the following restricted obstruction.

### Theorem 1
Let \(q\) be a prime power. Suppose all guesses in a \(q\)-color strategy on \(K_{n,n}\) are affine-linear over \(\mathbb F_q\). Then
\[
q\le n+1.
\]
Moreover, if \(n=q-1\) and \(q\ge4\), no such affine-linear winning strategy exists. Consequently, for \(n\ge3\), every affine-linear winning strategy satisfies
\[
q\le n.
\]

Thus any strategy attaining the unrestricted upper bound \(HG(K_{n,n})=n+1\), for \(n+1\) a prime power and \(n\ge3\), must be nonlinear.

As an actual unrestricted small case,
\[
HG(K_{1,1})=2,\qquad HG(K_{2,2})=3.
\]
In particular,
\[
3\le HG(K_{3,3})\le4,
\]
and a \(4\)-color strategy, if one exists, cannot be affine-linear over \(\mathbb F_4\).

---

## 2. A useful exact reformulation

For \(z\in Q^n\), put
\[
D(z)=\{w\in Q^n:w_i\ne z_i\text{ for every }i\}.
\]

A strategy is specified by two maps
\[
F,G:Q^n\longrightarrow Q^n,
\]
where \(F_i(y)\) is the guess made by \(a_i\), and \(G_j(x)\) is the guess made by \(b_j\).

The assignment \((x,y)\) is losing exactly when
\[
x\in D(F(y))\quad\text{and}\quad y\in D(G(x)).
\]
Since \(x\in D(F(y))\) is equivalent to \(F(y)\in D(x)\), we obtain:

### Proposition 2
A \(q\)-color strategy exists on \(K_{n,n}\) if and only if there is a map \(F:Q^n\to Q^n\) such that, for every \(x\in Q^n\), there is some \(a_x\in Q^n\) satisfying
\[
F^{-1}(D(x))\cap D(a_x)=\varnothing.
\]
Given such an \(F\), one may set \(G(x)=a_x\).

This is an exact one-map formulation of the unrestricted problem.

---

## 3. A rank bound for affine hyperplane covers

We first need a finite-geometric lemma.

### Lemma 3
Let \(H_1,\dots,H_m\) be proper affine hyperplanes covering \(\mathbb F_q^d\). If their normal vectors span an \(s\)-dimensional vector space, then
\[
m\ge q+s-1.
\]

#### Proof

We use the following projective blocking-set bound.

> If a set \(B\) of projective points spans a projective space of vector rank \(r\) and meets every projective hyperplane, then
> \[
> |B|\ge q+r-1.
> \]

This follows by induction on \(r\). For \(r=2\), the ambient projective space is a projective line, and every one of its \(q+1\) points is a hyperplane, so all \(q+1=q+r-1\) points are required.

For \(r\ge3\), choose a hyperplane \(H\) such that \(B\cap H\) spans \(H\). If \(B\cap H\) blocks all hyperplanes of \(H\), induction gives
\[
|B\cap H|\ge q+r-2,
\]
and at least one point lies outside \(H\).

Otherwise choose a hyperplane \(K\) of \(H\) disjoint from \(B\cap H\). There are \(q+1\) hyperplanes of the ambient projective space containing \(K\), one of which is \(H\). Each of the other \(q\) hyperplanes must contain a point of \(B\setminus H\), and their portions outside \(H\) are pairwise disjoint. Hence
\[
|B\setminus H|\ge q.
\]
Since \(B\cap H\) spans \(H\), it has at least \(r-1\) points. Again
\[
|B|\ge q+r-1.
\]

Now write
\[
H_i=\{z:a_i\cdot z=b_i\}.
\]
Homogenize \(H_i\) to the projective point
\[
p_i=[a_i:-b_i]\in PG(d,q),
\]
and add
\[
p_\infty=[0:\cdots:0:1].
\]
The resulting set meets every projective hyperplane: points with last homogeneous coordinate nonzero are handled by the affine cover, while \(p_\infty\) handles points at infinity.

The span of these projective points has vector rank \(s+1\), because the \(a_i\) span dimension \(s\) and \(p_\infty\) contributes the homogenizing direction. Therefore
\[
m+1\ge q+(s+1)-1=q+s,
\]
which is the claimed inequality. \(\square\)

---

## 4. Covering the multiplicative torus

The equality case of Lemma 3 reduces the hat problem to the following elementary statement.

### Lemma 4
Let \(q>2\), let \(n=q-1\), and put
\[
T=(\mathbb F_q^\ast)^n.
\]
If \(q-1\) affine hyperplanes cover \(T\), then the span of their normal vectors has dimension at most \(2\).

In particular, when \(q\ge4\), \(T\) cannot be covered by \(q-1\) affine hyperplanes having linearly independent normals.

#### Proof

Consider an affine equation
\[
r\cdot u=e
\]
whose normal \(r\) has exactly \(k\) nonzero entries. After scaling the corresponding variables, the number of solutions in \(T\) is
\[
(q-1)^{n-k}N_k(e),
\]
where
\[
N_k(0)=\frac{(q-1)^k+(q-1)(-1)^k}{q},
\]
and, for \(e\ne0\),
\[
N_k(e)=\frac{(q-1)^k-(-1)^k}{q}.
\]
These formulas follow directly by induction on \(k\), distinguishing whether the sum of the first \(k-1\) nonzero variables is zero.

Inspection gives
\[
|T\cap H|\le (q-1)^{n-1}=\frac{|T|}{q-1}.
\]
Equality occurs only in the following two cases:

1. \(k=1\) and \(e\ne0\), giving an equation
   \[
   u_i=c,\qquad c\in\mathbb F_q^\ast;
   \]
2. \(k=2\) and \(e=0\), giving an equation
   \[
   u_i=c\,u_j,\qquad c\in\mathbb F_q^\ast.
   \]

Since there are exactly \(q-1\) hyperplanes, a cover of \(T\) forces equality in the union bound. Hence every hyperplane is of one of these two types, and their intersections with \(T\) are pairwise disjoint.

Introduce an auxiliary coordinate \(u_0=1\). Both types can then be written as a ratio equation
\[
u_i=c\,u_j
\]
associated with an edge \(\{i,j\}\) of the complete graph on \(\{0,1,\dots,n\}\).

Two ratio equations based on distinct unordered pairs always have a common solution in \(T\): the graph formed by two distinct edges is a forest, so assign one nonzero value in each component and propagate using the two nonzero ratios. Therefore pairwise disjoint ratio sections must all use the same unordered pair.

If that pair is \(\{0,i\}\), all normal vectors are multiples of \(e_i\), so their span has dimension \(1\). If it is \(\{i,j\}\), all normals lie in
\[
\operatorname{span}\{e_i,e_j\}.
\]
Thus their span has dimension at most \(2\). \(\square\)

---

## 5. Proof of the affine-linear obstruction

Suppose the left and right guesses are
\[
F(y)=Ay+a,\qquad G(x)=Cx+b,
\]
where \(A,C\in\mathbb F_q^{n\times n}\) and \(a,b\in\mathbb F_q^n\).

The correctness hyperplanes have normal matrices
\[
U=[I_n\mid -A],\qquad V=[-C\mid I_n].
\]
Each of \(U,V\) has row rank \(n\). If \(s\) is the rank of the combined \(2n\) normals, Lemma 3 gives
\[
2n\ge q+s-1\ge q+n-1.
\]
Therefore
\[
q\le n+1.
\]

Now suppose \(n=q-1\). Then \(2n=q+n-1\), so equality forces
\[
s=n.
\]
Thus the row spaces of \(U\) and \(V\) coincide. There is an invertible matrix \(R\) with
\[
V=RU.
\]
Comparing the first and second blocks gives
\[
R=-C,\qquad -RA=I_n.
\]
Hence
\[
CA=I_n,
\]
so \(A\) and \(C\) are inverses.

Define
\[
u=x-Ay-a.
\]
The left-side players are all wrong exactly when \(u\in T=(\mathbb F_q^\ast)^n\). Meanwhile
\[
\begin{aligned}
y-Cx-b
 &=y-C(u+Ay+a)-b\\
 &=-Cu-Ca-b,
\end{aligned}
\]
using \(CA=I_n\). Thus, once the left side is wrong, the right-side correctness conditions are
\[
(Cu)_j=e_j,\qquad e=-Ca-b.
\]

Consequently, a winning strategy would require the \(n=q-1\) affine hyperplanes
\[
(Cu)_j=e_j,\qquad j=1,\dots,n,
\]
to cover \(T\). Their normals are the rows of the invertible matrix \(C\), hence are linearly independent. Lemma 4 rules this out when \(q\ge4\).

This proves Theorem 1. \(\square\)

---

## 6. The cases \(K_{1,1}\) and \(K_{2,2}\)

For \(K_{1,1}\), with colors \(\mathbb F_2\), let one player guess the other player's color and let the other guess its complement. This wins, and the supplied upper bound gives
\[
HG(K_{1,1})=2.
\]

For \(K_{2,2}\), use colors \(\mathbb F_3\). Write the hats as \(x_1,x_2\) and \(y_1,y_2\). Let the guesses be
\[
\begin{array}{ll}
a_1:\ -y_1-y_2, & a_2:\ -y_1+y_2,\\[2mm]
b_1:\ x_1+x_2, & b_2:\ x_1-x_2.
\end{array}
\]
Set
\[
r_1=x_1+y_1+y_2,\qquad r_2=x_2+y_1-y_2.
\]
The four correctness conditions are respectively equivalent to
\[
r_1=0,\qquad r_2=0,\qquad r_1+r_2=0,\qquad r_1-r_2=0.
\]
If both \(r_1,r_2\) are nonzero in \(\mathbb F_3\), then \(r_1/r_2\in\{1,-1\}\), so either \(r_1-r_2=0\) or \(r_1+r_2=0\). Thus the strategy always wins.

The known upper bound \(HG(K_{2,2})\le3\) therefore gives
\[
HG(K_{2,2})=3.
\]

---

## 7. A rigidity statement for a nonlinear permutation ansatz

There is also a restriction on the following natural nonlinear construction. Let
\[
H=K_q^{\times n}
\]
be the graph on \(Q^n\) in which two vectors are adjacent when they differ in every coordinate. Suppose one takes a permutation
\[
\pi:Q^n\to Q^n
\]
and uses
\[
F=\pi,\qquad G=\pi^{-1}.
\]
This strategy wins exactly when \(\pi\) maps every edge of \(H\) to a nonedge of \(H\).

### Proposition 5
Let \(n=q-1\ge2\). If such a permutation strategy wins, then:

1. whenever \(u,v\) differ in every input coordinate, \(\pi(u),\pi(v)\) agree in exactly one output coordinate;
2. for every output coordinate \(j\) and value \(c\), the centered indicator
   \[
   1_{\{\pi_j=c\}}-\frac1q
   \]
   lies entirely in the tensor-degree-\(2\) eigenspace of \(H\).

#### Proof sketch with full count

The graph \(H\) has
\[
N=q^n,\qquad d=(q-1)^n.
\]
Its adjacency matrix is
\[
A=(J_q-I_q)^{\otimes n}.
\]
On the orthogonal complement of the constant vector, its largest eigenvalue is
\[
\lambda_2=(q-1)^{n-2},
\]
coming from tensors nonconstant in exactly two coordinates.

For a fixed output coordinate \(j\), its \(q\) level sets form a balanced partition \(S_1,\dots,S_q\), each of size \(N/q\). Let \(M_j\) be the number of edges of \(H\) whose endpoints receive the same \(j\)-th output coordinate. Writing
\[
1_{S_c}=\frac1q\mathbf 1+v_c,
\]
the spectral bound gives
\[
\begin{aligned}
2M_j
 &=\sum_c 1_{S_c}^{T}A1_{S_c}\\
 &\le \frac{Nd}{q}+\lambda_2\frac{N(q-1)}q\\
 &=\frac{Nd}{q-1}.
\end{aligned}
\]
Therefore
\[
M_j\le \frac{|E(H)|}{q-1}.
\]

Every input edge must acquire at least one output-coordinate agreement. Since there are \(n=q-1\) output coordinates,
\[
|E(H)|\le\sum_{j=1}^{n}M_j\le n\frac{|E(H)|}{q-1}=|E(H)|.
\]
All inequalities are equalities. Thus every edge has exactly one output agreement, and equality in the spectral estimate forces every centered level-set indicator into the \(\lambda_2\)-eigenspace.

This does not rule out such permutations, but it makes any endpoint construction extremely rigid.

---

## 8. Fully specified SAT formulation for \(K_{3,3}\) with four colors

The unresolved smallest case can be checked exactly by SAT.

For each \(y\in[4]^3\), \(i\in[3]\), \(c\in[4]\), introduce
\[
A_{y,i,c},
\]
meaning that \(a_i\) guesses \(c\) on input \(y\). Similarly introduce
\[
B_{x,j,c}
\]
for the right-side guesses.

Impose exactly one true literal in every group
\[
\{A_{y,i,c}:c\in[4]\},\qquad
\{B_{x,j,c}:c\in[4]\}.
\]
For every \((x,y)\in[4]^3\times[4]^3\), add the winning clause
\[
\bigvee_{i=1}^3 A_{y,i,x_i}
\;\vee\;
\bigvee_{j=1}^3 B_{x,j,y_j}.
\]

This CNF has:

- \(2\cdot3\cdot4^4=1536\) Boolean variables;
- \(384\) exactly-one groups;
- \(4096\) winning clauses of length \(6\).

With pairwise at-most-one clauses, there are \(6784\) clauses in total. Satisfiability is exactly equivalent to \(HG(K_{3,3})\ge4\). I did not run this computation, so no computational conclusion is claimed.

---

## 9. Remaining gap

The affine proof depends crucially on correctness sets being affine hyperplanes. For arbitrary strategies they are graphs of arbitrary functions, and neither the rank-cover lemma nor the multiplicative-torus classification applies. Likewise, Proposition 5 only treats the special ansatz \(F=\pi\), \(G=\pi^{-1}\).

Thus the unrestricted alternatives remain:

- \(HG(K_{3,3})=3\) or \(4\);
- more generally, it remains unknown whether \(HG(K_{n,n})\) can attain \(n+1\), or even what its correct asymptotic order is beyond the bounds supplied in the question.

The affine-linear obstruction may overlap with the cited follow-up on linear hat guessing; I have not verified its precise theorem statements, so I make no novelty claim.