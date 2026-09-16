```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove reconstructibility when some card has a nonsingular walk matrix and an odd-sized degree class.",
  "would_publish": false,
  "caveats": "This is a sufficient condition only; novelty is not claimed, and the general conjecture is not settled."
}
```

## 1. A reconstruction criterion

All graphs below are finite, simple, and undirected. I do not obtain a proof or counterexample to the general conjecture.

For a graph \(F\) on \(m\) vertices, with adjacency matrix \(A\), write \(\mathbf e=(1,\ldots,1)^{T}\), and define its **walk matrix**
\[
W(F)=\bigl[\mathbf e,\ A\mathbf e,\ A^2\mathbf e,\ldots,A^{m-1}\mathbf e\bigr].
\]
Whether this matrix is nonsingular is independent of the ordering of the vertices.

### Theorem
Let \(G\) have \(n\ge 3\) vertices. Suppose its deck contains a card \(F\) such that

1. \(W(F)\) is nonsingular; and
2. some degree occurs an odd number of times in \(F\).

Then \(G\) is reconstructible.

In particular, **every even-order graph with a card having nonsingular walk matrix is reconstructible**.

The proof gives more information about the cases not covered by condition 2.

### Residual ambiguity
Suppose \(G,H\) have the same deck, and identify a common card \(F\), of order \(m=n-1\), whose walk matrix is nonsingular. Let \(b,c\in\{0,1\}^{m}\) describe the neighborhoods of the added vertex in \(G,H\), respectively.

Then either \(b=c\), or all the following hold:
\[
c=\mathbf e-b,\qquad |b|=|c|=m/2,
\]
and \(b\) selects exactly half the vertices of **every degree class of \(F\)**.

Thus a nonsingular-walk-matrix card leaves at most two possible neighborhood vectors compatible with the entire deck. Any distinct second possibility must be the complementary neighborhood.

The rest of the writeup proves these assertions without invoking external reconstruction results.

## 2. Two polynomial identities supplied by the deck

For a graph \(X\), define
\[
p_X(x)=\det(xI-A_X),\qquad
s_X(x)=\mathbf e_X^{T}\operatorname{adj}(xI-A_X)\mathbf e_X.
\]
The rank-one determinant identity gives
\[
\det(xI-A_X+yJ)=p_X(x)+y\,s_X(x).
\]
Differentiating a determinant with respect to its common diagonal variable gives
\[
\frac{\partial}{\partial x}\det(xI-A_X+yJ)
 =
 \sum_{v\in V(X)}
 \det(xI-A_{X-v}+yJ).
\]
Consequently,
\[
p_X'(x)=\sum_v p_{X-v}(x),
\qquad
s_X'(x)=\sum_v s_{X-v}(x).
\tag{1}
\]
These are sums over the deck, with multiplicities.

In particular, if \(G,H\) have the same deck, then
\[
p_G-p_H=\kappa,\qquad s_G-s_H=\lambda
\tag{2}
\]
for constants \(\kappa,\lambda\).

Now identify a common card \(F\), with adjacency matrix \(A\), and write the two extensions as
\[
B_b=\begin{pmatrix}A&b\\b^T&0\end{pmatrix},
\qquad
B_c=\begin{pmatrix}A&c\\c^T&0\end{pmatrix}.
\]
Set
\[
R(x)=(xI-A)^{-1},
\quad
\alpha_b=b^TR(x)b,
\quad
\beta_b=\mathbf e^TR(x)b,
\quad
\gamma=\mathbf e^TR(x)\mathbf e,
\]
and define \(\alpha_c,\beta_c\) similarly.

Schur complementation and block inversion give
\[
p_{G}(x)=p_F(x)\bigl(x-\alpha_b(x)\bigr)
\tag{3}
\]
and
\[
s_G(x)
 =
 p_F(x)\left[
 \bigl(x-\alpha_b(x)\bigr)\gamma(x)
 +\bigl(1+\beta_b(x)\bigr)^2
 \right].
\tag{4}
\]
The same formulas hold for \(H\) with \(c\).

Combining (2)–(4),
\[
\alpha_b-\alpha_c=-\frac{\kappa}{p_F},
\tag{5}
\]
and
\[
p_F(\beta_b-\beta_c)(2+\beta_b+\beta_c)
   =\lambda-\kappa\gamma.
\tag{6}
\]
Here \(p_F\) has degree \(m\), while \(\beta_b,\beta_c,\gamma=O(x^{-1})\) at infinity. Equations (5) and (6) therefore imply
\[
\alpha_b-\alpha_c=O(x^{-m}),
\qquad
\beta_b-\beta_c=O(x^{-m}).
\]
Using the formal Laurent expansion
\[
R(x)=\sum_{r\ge0}A^r x^{-r-1},
\]
we obtain the two sets of identities
\[
b^TA^rb=c^TA^rc,
\qquad
\mathbf e^TA^rb=\mathbf e^TA^rc,
\qquad 0\le r\le m-2.
\tag{7}
\]

These are the deck constraints used in the argument.

## 3. Nonsingularity forces complementary neighborhoods

Assume \(W(F)\) is nonsingular. Put
\[
z=b-c,\qquad u=b+c.
\]
Because \(A\) is symmetric, (7) becomes
\[
z^TA^r\mathbf e=0,
\qquad
z^TA^ru=0,
\qquad 0\le r\le m-2.
\tag{8}
\]

If \(z=0\), the two extensions are identical. Suppose \(z\ne0\).

Nonsingularity of \(W(F)\), together with the first set of equations in (8), gives
\[
z^TA^{m-1}\mathbf e\ne0.
\tag{9}
\]
I claim that
\[
z,Az,\ldots,A^{m-2}z
\]
form a basis of \(\mathbf e^\perp\).

They belong to \(\mathbf e^\perp\) by (8). For independence, suppose
\[
\sum_{r=0}^{m-2}a_rA^rz=0,
\]
and let \(j\) be the largest index with \(a_j\ne0\). Taking the inner product with \(A^{m-1-j}\mathbf e\), all terms with \(r<j\) vanish by (8), leaving
\[
a_j z^TA^{m-1}\mathbf e=0,
\]
contrary to (9). The claim follows.

The second set of equations in (8) now says that \(u\) is perpendicular to \(\mathbf e^\perp\), so \(u=t\mathbf e\). Since \(b,c\) are binary and differ in at least one coordinate, that coordinate has \(b_i+c_i=1\). Hence \(t=1\), and
\[
c=\mathbf e-b.
\tag{10}
\]
Finally, the \(r=0\) linear identity in (7) gives
\[
\mathbf e^Tb=\mathbf e^Tc=m/2.
\tag{11}
\]
In particular, \(m\) must be even.

This already proves the even-order corollary: when \(n\) is even, \(m=n-1\) is odd, making (11) impossible.

## 4. The degree classes must also split evenly

The deck determines the edge count because
\[
|E(G)|=\frac{1}{n-2}\sum_{D\in\mathcal D(G)}|E(D)|.
\tag{12}
\]
It then determines the degree sequence: the degree of a deleted vertex is
\[
|E(G)|-|E(D)|.
\tag{13}
\]

Continue under the possibility \(c=\mathbf e-b\). Let
\[
N_d=\bigl|\{i:\deg_F(i)=d\}\bigr|,
\qquad
a_d=\bigl|\{i:\deg_F(i)=d,\ b_i=1\}\bigr|.
\]
The \(c\)-neighborhood contains \(N_d-a_d\) vertices of this degree class.

The two added vertices have the same degree by (11), so their contributions cancel when comparing degree sequences. Among the remaining vertices, the number of degree-\(j\) vertices in the \(b\)-extension is
\[
N_j-a_j+a_{j-1}.
\]
Define
\[
\delta_d=2a_d-N_d,\qquad \delta_{-1}=0.
\]
Equality of the two degree sequences gives
\[
\delta_{j-1}-\delta_j=0.
\]
Starting with \(j=0\), induction yields \(\delta_j=0\) for every \(j\). Thus
\[
a_d=N_d/2
\qquad\text{for every degree }d.
\tag{14}
\]

Every \(N_d\) must therefore be even. If any degree class of \(F\) has odd size, the alternative \(b\ne c\) is impossible. Hence \(b=c\), proving the theorem. \(\square\)

A further usable exclusion follows from the proof. The kernel of
\[
\bigl[\mathbf e,A\mathbf e,\ldots,A^{m-2}\mathbf e\bigr]^T
\]
is one-dimensional. If its nonzero vectors do not have all coordinates of the same nonzero absolute value, then (10) is impossible, since \(b-c=2b-\mathbf e\) would have every coordinate in \(\{-1,1\}\).

## 5. Effective reconstruction on this class

The sufficient condition also gives a polynomial-time reconstruction procedure for a deck promised to come from a graph satisfying it.

First compute \(p_D,s_D\) for every card. By (1), integrate their sums to obtain polynomials \(p^*,s^*\) with constant terms chosen to be zero. The true \(p_G,s_G\) differ from these by constants.

For a selected card \(F\), let \(\gamma=s_F/p_F\). Equations (3)–(4) show that the numbers
\[
q_r=b^TA^rb,\qquad h_r=\mathbf e^TA^rb,
\qquad 0\le r\le m-2,
\]
can be recovered from the Laurent expansions of
\[
x-\frac{p^*}{p_F}
\]
and
\[
\sqrt{
\frac{s^*}{p_F}-\frac{p^*}{p_F}\gamma
}-1,
\]
respectively. The square root is the formal branch with constant term \(1\). The unknown integration constants affect these expressions only at order \(x^{-m}\), beyond the coefficients being used.

Set
\[
K=[\mathbf e,A\mathbf e,\ldots,A^{m-2}\mathbf e].
\]
The system
\[
K^Tb=(h_0,\ldots,h_{m-2})^T
\]
has an affine line as its solution set. Such a line contains at most two binary vectors: choose a coordinate on which its direction vector is nonzero, and that coordinate being either \(0\) or \(1\) fixes the line parameter.

Test these at most two candidates against:

* the recovered quadratic moments \(q_r\); and
* the recovered degree sequence.

At least one survives because the deck is genuine. Under the theorem’s hypotheses, at most one survives: the proof above used only these moments and the degree sequence to establish uniqueness.

Polynomial determinants, truncated Laurent expansions, and exact linear algebra suffice. The coefficients and walk counts involved have polynomial bit length. No graph-isomorphism oracle is needed for this promised class.

## 6. An explicit example and an unbounded family

Let \(F_0\) be the seven-vertex tree with edges
\[
12,\ 13,\ 34,\ 15,\ 56,\ 67.
\]
It is a three-armed tree with arm lengths \(1,2,3\). Its walk matrix is
\[
W(F_0)=
\begin{pmatrix}
1&3&5&12&20&47&78\\
1&1&3&5&12&20&47\\
1&2&4&7&16&27&63\\
1&1&2&4&7&16&27\\
1&2&5&8&19&31&73\\
1&2&3&7&11&26&42\\
1&1&2&3&7&11&26
\end{pmatrix},
\qquad
\det W(F_0)=-8.
\]
Consequently, every graph obtained by adding one vertex with an arbitrary neighborhood to \(F_0\) is reconstructible.

For completeness, this construction extends to arbitrarily large orders. Define
\[
F_{r+1}=(F_r\vee K_1)\sqcup K_1,
\]
where \(\vee K_1\) adds a universal vertex.

The following elementary facts verify that every \(F_r\) has nonsingular walk matrix.

1. **Complementation preserves walk-matrix rank.** Indeed,
   \[
   \overline A^{\,j}\mathbf e
   =(-1)^jA^j\mathbf e+
   \operatorname{span}\{\mathbf e,A\mathbf e,\ldots,A^{j-1}\mathbf e\}.
   \]

2. **Adding an isolated vertex preserves nonsingularity of the walk matrix when \(A\) is nonsingular.** Expanding the new walk determinant along the isolated vertex’s row gives, up to sign,
   \[
   \det(A)\det W(F).
   \]

3. **Adding a universal vertex to a graph with nonsingular walk matrix and singular adjacency matrix produces a nonsingular adjacency matrix.**  
   Here \(\ker A\) is one-dimensional, spanned by some \(z\) with \(\mathbf e^Tz\ne0\); otherwise \(W(F)\) would be singular. The equations
   \[
   Ax+t\mathbf e=0,\qquad \mathbf e^Tx=0
   \]
   then force \(t=0\) and \(x=0\).

For the displayed base graph,
\[
\det A_{F_0}=0,\qquad \det A_{\overline{F_0}}=2.
\]
The three facts inductively show that \(F_r\) has nonsingular walk matrix, singular adjacency matrix, and nonsingular complement adjacency matrix.

Thus \(F_r\) has odd order \(7+2r\), and **every arbitrary one-vertex extension of \(F_r\)** is reconstructible by the theorem.

## 7. What remains unresolved

The argument has two substantial limitations.

* It requires a card with nonsingular walk matrix. Many graphs have no such card; for example, a regular card has walk-matrix rank \(1\).
* With such a card of even order, the argument can leave complementary neighborhoods that bisect every degree class.

The latter conditions are only necessary conditions for a same-deck ambiguity. They do **not** establish that the two extensions have equal decks, and they do not produce a counterexample.

Accordingly, the result here is a sufficient condition, an explicit reconstruction procedure on that class, and a restricted description of possible ambiguity—not a resolution of the Reconstruction Conjecture.