```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A polynomial-time algorithm is proved when the determinant bound is fixed and deleting some nonsingular row basis leaves bounded rank, covering in particular a fixed excess of inequalities over variables.",
  "would_publish": false,
  "caveats": "The unrestricted IP conjecture is not settled; no novelty is claimed, and the graph-clause literature status is taken from the supplied review."
}
```

## 1. Scope

Interpret “bounded sub-determinants” as a bound by a **fixed constant** \(\Delta\), with all input numbers encoded in binary. The general problem is
\[
\min\{c^{\mathsf T}x:Ax\le b,\ x\in\mathbb Z^n\},
\tag{IP}
\]
where \(A,b,c\) are integral and every square submatrix of \(A\) has determinant of absolute value at most \(\Delta\).

The supplied review reports that the bounded-odd-cycle-packing stable-set clause has already been settled. I do not independently verify or reprove that algorithm here.

Below I give:

1. a self-contained polynomial-time algorithm for a restricted class of general integer programs; and
2. an exact determinant calculation explaining the stable-set implication.

Neither establishes the unrestricted IP conjecture.

## 2. A tractable special case of general IP

For a full-column-rank matrix \(A\in\mathbb Z^{m\times n}\), write
\[
\Delta_n(A)=\max_{\substack{I\subseteq[m]\\ |I|=n}}|\det A_I|,
\]
where \(A_I\) consists of the rows indexed by \(I\).

### Proposition

Fix integers \(\Delta\ge1\) and \(r\ge0\). Problem (IP) is solvable in polynomial time under these assumptions:

1. \(\operatorname{rank}A=n\);
2. \(\Delta_n(A)\le\Delta\);
3. there is a nonsingular \(n\)-row submatrix \(B\) such that the matrix of remaining rows has rank at most \(r\).

The algorithm detects infeasibility and unboundedness and otherwise returns an optimal integer solution. The submatrix \(B\) need not be supplied.

In particular, this applies whenever \(\operatorname{rank}A=n\) and \(m-n\) is fixed.

Only the full-size determinants are bounded in this proposition; the smaller minors need not be bounded. I present it as a restricted result, not as a novelty claim.

### 2.1. Finding a suitable row basis

For fixed \(r\), the third condition can be recognized and a suitable \(B\) found in polynomial time.

Enumerate sets \(R\) of at most \(r\) rows, and let \(W\) be their linear span. Check whether the collection of all rows of \(A\) lying outside \(W\) is linearly independent. If so, extend that collection to a row basis \(B\) of \(A\). Every remaining row lies in \(W\), so the remaining matrix has rank at most \(r\).

Conversely, suppose a suitable \(B\) exists. Choose \(R\) to be a row basis of its complement. Every row outside \(\operatorname{span}R\) belongs to \(B\), and hence those rows are independent. Thus the enumeration finds a suitable basis.

There are at most \(\sum_{j=0}^r\binom mj\) choices, and all the tests are rational linear algebra.

Assume henceforth that, after permuting rows,
\[
A=\begin{pmatrix}B\\ A'\end{pmatrix},
\qquad
b=\begin{pmatrix}b_B\\ b'\end{pmatrix},
\qquad
\operatorname{rank}A'\le r.
\]
The case \(n=0\) is immediate, so assume \(n\ge1\).

### 2.2. Bounded coefficients after a change of coordinates

Put
\[
d=|\det B|,\qquad D=dB^{-1},\qquad F=A'D.
\]
Then \(1\le d\le\Delta\), and \(D,F\) are integral.

Every entry of \(F\) has absolute value at most \(\Delta\). Indeed, if \(a_j\) is a row of \(A'\), then
\[
F_{ji}=d\,a_jB^{-1}e_i
       =\frac{d}{\det B}\det B(i\leftarrow a_j),
\]
where \(B(i\leftarrow a_j)\) is obtained by replacing row \(i\) of \(B\) by \(a_j\). Its determinant is an \(n\times n\) minor of \(A\), up to row order. Therefore
\[
|F_{ji}|\le\Delta.
\tag{1}
\]

Also \(\operatorname{rank}F\le r\).

We use the following elementary observation:

> A rank-at-most-\(r\) integer matrix whose entries lie in \([-\Delta,\Delta]\) has at most
> \[
> Q=(2\Delta+1)^r
> \]
> distinct rows, and at most \(Q\) distinct columns.

For rows, choose a basis of the column space: a row is determined by its entries in those at most \(r\) columns. The column assertion is analogous.

Since \(D\) is invertible, equal rows of \(F\) correspond exactly to equal rows of \(A'\). For repeated inequalities with the same left-hand side, retain the smallest right-hand side. Consequently, we may assume that \(A'\) has
\[
q\le Q
\tag{2}
\]
rows.

### 2.3. Slack variables and a finite quotient group

For the subsystem \(Bx\le b_B\), introduce integral slacks
\[
s=b_B-Bx\in\mathbb Z_{\ge0}^n.
\]
Conversely,
\[
x=B^{-1}(b_B-s)
\]
is integral precisely when
\[
s\equiv b_B\pmod{B\mathbb Z^n}.
\tag{3}
\]

The finite abelian group
\[
\Gamma=\mathbb Z^n/B\mathbb Z^n
\]
has order \(d\). Let \(\gamma_i=e_i+B\mathbb Z^n\).

Define the **type** of slack coordinate \(i\) to be
\[
\bigl(F_{\bullet i},\gamma_i\bigr).
\]
There are at most
\[
T\le dQ\le \Delta(2\Delta+1)^r
\tag{4}
\]
types.

These types are computable without constructing an abstract group decomposition: \(\gamma_i=\gamma_j\) if and only if
\[
D e_i\equiv D e_j\pmod d
\]
coordinatewise.

The remaining inequalities and objective are
\[
A'x=A'B^{-1}b_B-\frac1d Fs
\]
and
\[
c^{\mathsf T}x
=c^{\mathsf T}B^{-1}b_B+\frac1d\sum_{i=1}^n w_i s_i,
\qquad
w_i=-c^{\mathsf T}De_i\in\mathbb Z.
\tag{5}
\]

For each type \(t\), choose a representative coordinate \(i_t\) minimizing \(w_i\) within that type.

Given any feasible slack vector, move all slack in each type to its representative. This operation:

- preserves nonnegativity and integrality;
- preserves \(Fs\);
- preserves the class of \(s\) in \(\Gamma\);
- does not increase the objective.

Thus it preserves feasibility and cannot worsen the solution. It follows that the original problem is equivalent, including infeasibility and unboundedness, to its restriction to slack vectors
\[
s=\sum_{t=1}^T y_t e_{i_t},
\qquad y\in\mathbb Z_{\ge0}^T.
\tag{6}
\]

### 2.4. Eliminating the congruence

Write, uniquely,
\[
y_t=\rho_t+d z_t,
\qquad
0\le\rho_t<d,\quad z_t\in\mathbb Z_{\ge0}.
\]
There are at most \(d^T\) possible residue vectors \(\rho\), a constant depending only on \(\Delta,r\).

For each one, put
\[
x_\rho
=B^{-1}\left(b_B-\sum_{t=1}^T\rho_t e_{i_t}\right).
\]
Since \(De_{i_t}\) is integral,
\[
x=x_\rho-\sum_{t=1}^T De_{i_t}z_t.
\tag{7}
\]
Therefore the residue case is impossible if \(x_\rho\notin\mathbb Z^n\); otherwise every integral \(z\) gives an integral \(x\).

Let \(F_*\) consist of the representative columns of \(F\). For a surviving residue case, the problem becomes
\[
\begin{array}{ll}
\text{minimize}
 & c^{\mathsf T}x_\rho+\displaystyle\sum_{t=1}^T w_{i_t}z_t\\[2mm]
\text{subject to}
 & -F_*z\le b'-A'x_\rho,\\
 & z\in\mathbb Z_{\ge0}^T.
\end{array}
\tag{8}
\]
It has at most \(Q\) inequalities, at most \(\Delta Q\) variables, and constraint coefficients bounded by \(\Delta\).

For completeness, the following elementary subroutine solves these reduced programs.

### 2.5. Solving the reduced programs

Consider
\[
\min\{g^{\mathsf T}z:Cz\le h,\ z\in\mathbb Z_{\ge0}^T\},
\tag{9}
\]
where \(C\) has \(q\) rows, \(|C_{ij}|\le\Delta\), and \(q,T,\Delta\) are fixed.

Add nonnegative integral slacks:
\[
\widehat C u=h,\qquad
u\in\mathbb Z_{\ge0}^{N},
\qquad
\widehat C=[\,C\ I_q\,],\quad N=T+q.
\tag{10}
\]
Extend the objective by assigning zero costs to the added slacks. Put
\[
H=q!\Delta^q,
\]
with \(H=1\) when \(q=0\).

**Bounded-dependence fact.** Any dependent collection of columns of \(\widehat C\) contains a nonzero integral dependence \(v\) supported on that collection with
\[
\|v\|_\infty\le H.
\tag{11}
\]
To see this, take a minimally dependent subcollection. It has at most \(q+1\) columns. The usual cofactor construction, on a maximal independent collection of its rows, produces an integral dependence whose coefficients are determinants of order at most \(q\). The Leibniz bound gives (11).

Now suppose (10) is feasible, and choose its lexicographically first integral feasible point \(u\). The columns indexed by
\[
L(u)=\{j:u_j\ge H\}
\]
must be independent. Otherwise (11) gives a nonzero kernel vector supported on \(L(u)\), and both \(u+v\) and \(u-v\) remain nonnegative and feasible. One is lexicographically smaller.

The same conclusion holds for the lexicographically first optimal point whenever the integer objective is bounded below. Such an optimum exists because its values are integral. If the indicated dependence changes the objective, one sign improves it; if it does not, one sign improves the lexicographic tie-break.

Consequently, both feasibility and a finite optimum can be found by this finite enumeration:

1. enumerate independent sets \(S\) of columns of \(\widehat C\);
2. assign each \(u_j\), \(j\notin S\), a value in \(\{0,\ldots,H-1\}\);
3. solve
   \[
   \widehat C_Su_S
   =h-\sum_{j\notin S}\widehat C_{\bullet j}u_j;
   \]
4. retain solutions that are consistent, integral, and nonnegative.

The unknown coordinates \(u_S\) are uniquely determined because the columns in \(S\) are independent. The enumeration has constant size for fixed \(q,T,\Delta\).

If no candidate is found, the integer program is infeasible. Otherwise, solve its rational LP relaxation to test unboundedness. If that LP is unbounded below, it has a rational recession direction of negative cost. Scaling this direction to an integral vector and adding its nonnegative integer multiples to a feasible integer point proves integer unboundedness. If the LP is bounded below, the least-cost enumerated candidate is an integer optimum.

This covers all outcomes of (9).

### 2.6. Complexity and conclusion

All enumeration bounds after choosing \(B\) depend only on \(\Delta,r\). Importantly, they do **not** depend on the numerical magnitudes of \(b\) or \(c\).

Computing \(B^{-1}\), the signatures, and the reduced right-hand sides uses polynomial-bit-length exact arithmetic. The candidate solutions in the subroutine are obtained from constant-size linear systems, so their bit lengths are polynomial in the input length. Rational linear programming is polynomial-time.

Combining the residue cases and reconstructing \(x\) by (7) proves the proposition.

If \(B\) is supplied, the running time has the form
\[
f(\Delta,r)\operatorname{poly}(L),
\]
where \(L\) is the binary input length. Finding \(B\) adds an \(m^{O(r)}\) factor. In the special case \(m-n\le r\), any row basis works, so no such search is needed.

The determinant bound is a promise; no efficient verification of all full-size minors is being asserted.

## 3. The exact stable-set determinant bound

Here is the precise algebra behind the catalog’s “in particular.”

Let \(G=(V,E)\) be a finite simple graph. Let \(M_G\) be its edge–vertex incidence matrix:
\[
(M_G)_{ev}=
\begin{cases}
1,&v\text{ is an endpoint of }e,\\
0,&\text{otherwise}.
\end{cases}
\]
Set
\[
A_G=\begin{pmatrix}M_G\\ I\\-I\end{pmatrix}.
\]
The integer points satisfying
\[
M_Gx\le\mathbf1,\qquad 0\le x\le1
\]
are exactly the characteristic vectors of stable sets.

Let \(\Delta(A_G)\) denote the largest absolute square subdeterminant, including the empty determinant \(1\).

### Proposition
\[
\boxed{\Delta(A_G)=2^{\operatorname{ocp}(G)}.}
\tag{12}
\]

### Proof

Consider a nonzero square minor of \(A_G\). Repeatedly expand along any row having exactly one nonzero entry. Such an entry is \(1\) or \(-1\), so this preserves the absolute determinant. A zero row would make the determinant zero.

Unless the matrix becomes empty, the remaining rows all have exactly two entries equal to \(1\). They are incidence rows of a graph on the remaining column vertices.

For the determinant to be nonzero, every connected component of this graph must have equally many edges and vertices. Indeed, otherwise the corresponding rectangular blocks force a rank deficiency. Each component is therefore unicyclic.

Expanding along leaf columns reduces each component to its unique cycle. The edge–vertex incidence matrix of a cycle of length \(\ell\) has determinant
\[
1-(-1)^\ell.
\]
Thus an even cycle gives determinant zero, and an odd cycle contributes absolute determinant \(2\).

It follows that every nonzero minor has absolute determinant \(2^t\), where its \(t\) odd cycles are vertex-disjoint in \(G\). Hence
\[
\Delta(A_G)\le2^{\operatorname{ocp}(G)}.
\]

Conversely, take \(\operatorname{ocp}(G)\) vertex-disjoint odd cycles and select their edge rows and vertex columns. The resulting matrix is block diagonal, with each block having determinant of absolute value \(2\). Its determinant has absolute value \(2^{\operatorname{ocp}(G)}\). For packing number zero, an identity minor—or the empty minor—gives \(1\). This proves (12). ∎

Therefore bounded odd cycle packing places the stable-set formulation precisely inside a bounded-subdeterminant class whose rows have at most two nonzeros. Equation (12) explains the implication; it is not itself a stable-set algorithm.

## 4. The remaining gap

The extra hypothesis in the IP proposition does not follow from a determinant bound.

For example,
\[
A=\begin{pmatrix}I_n\\-I_n\end{pmatrix}
\]
has every square subdeterminant in \(\{0,\pm1\}\). Nevertheless, every nonsingular \(n\)-row subsystem chooses exactly one of \(e_i^{\mathsf T}\) and \(-e_i^{\mathsf T}\) for each \(i\), leaving a complementary matrix of rank \(n\).

This example is not a counterexample to the conjecture—it is an easy integer program—but it shows exactly why the bounded-residual-rank argument cannot establish the general claim.

Thus the rigorous outcome is a tractable restricted class, together with the exact graph determinant identity. No complete proof or counterexample for the unrestricted bounded-subdeterminant IP conjecture is obtained.