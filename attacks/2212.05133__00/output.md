```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained inertia argument gives n(2,d) <= d^2+1 and the conjectured half-quadratic upper bound under two broad structural conditions, but the unrestricted case remains open.",
  "would_publish": false,
  "caveats": "Dense incompatibility among coordinate splits and a linear number of spectral eigenvalues below -2 remain uncontrolled; the formal Section 3 lamination conjecture was not supplied."
}
```

# 1. Statement and encoding

The formal conjecture from Section 3 is not quoted in the prompt, so I address the unambiguous asymptotic assertion
\[
\lim_{d\to\infty}\frac{n(2,d)}{d^2}=\frac12.
\tag{C}
\]

Using the biclique-cover formulation, encode a vertex by a word
\[
x=(x_1,\ldots,x_d)\in\{0,1,*\}^d.
\]
For two words put
\[
c(x,y)=\bigl|\{i:\{x_i,y_i\}=\{0,1\}\}\bigr|.
\]
Thus \(n(2,d)\) is the maximum size of a family \(\mathcal F\subseteq\{0,1,*\}^d\) satisfying
\[
c(x,y)\in\{1,2\}\qquad(x\ne y).
\tag{1}
\]

The supplied paper proves the lower bound
\[
n(2,d)\ge \left(\frac12-o(1)\right)d^2.
\]
What remains is the corresponding upper bound.

# 2. A quantitative bound in terms of incompatible coordinate splits

For each coordinate \(i\), let
\[
A_i=\{x\in\mathcal F:x_i=0\},\qquad
B_i=\{x\in\mathcal F:x_i=1\}.
\]
These are the two sides of the \(i\)-th biclique.

For \(i<j\), define
\[
t_{ij}=
\mathbf 1_{\{A_i\cap A_j\ne\varnothing,\ B_i\cap B_j\ne\varnothing\}}
+
\mathbf 1_{\{A_i\cap B_j\ne\varnothing,\ B_i\cap A_j\ne\varnothing\}}.
\tag{2}
\]
Thus \(t_{ij}\in\{0,1,2\}\). Moreover, \(t_{ij}=2\) precisely when all four binary patterns \(00,01,10,11\) occur in the projection of \(\mathcal F\) onto coordinates \(i,j\).

Let
\[
\mu(\mathcal F)=\bigl|\{\{i,j\}:t_{ij}=2\}\bigr|.
\]
In split-system language, \(\mu(\mathcal F)\) is the number of incompatible pairs of coordinate splits.

## Theorem 1

Every \(2\)-neighborly family \(\mathcal F\subseteq\{0,1,*\}^d\) satisfies
\[
|\mathcal F|
   \le d+1+\sum_{1\le i<j\le d}t_{ij}
   \le 1+d+\binom d2+\mu(\mathcal F).
\tag{3}
\]
Consequently,
\[
n(2,d)\le d^2+1.
\tag{4}
\]
More importantly, if \(\mu(\mathcal F)=o(d^2)\), then
\[
|\mathcal F|\le \left(\frac12+o(1)\right)d^2.
\tag{5}
\]

### Proof

Write \(a_i,b_i\in\{0,1\}^{\mathcal F}\) for the indicator vectors of \(A_i,B_i\), and let
\[
M_i=a_i b_i^{\mathsf T}+b_i a_i^{\mathsf T}.
\]
Then \(M_i\) is the adjacency matrix of the \(i\)-th biclique, and
\[
M=\sum_{i=1}^d M_i
\]
has diagonal zero and
\[
M_{xy}=c(x,y)\in\{1,2\}\qquad(x\ne y).
\]

Let \(J\) denote the all-one matrix. Entrywise,
\[
M\circ M-3M+2J=2I,
\tag{6}
\]
because \(s^2-3s+2=0\) for \(s=1,2\), while the diagonal gives \(2\).

Since each \(M_i\) is a \(0\)-\(1\) matrix,
\[
M\circ M=M+2\sum_{i<j}M_i\circ M_j.
\]
Substitution into (6) yields
\[
I=J-M+\sum_{i<j}M_i\circ M_j.
\tag{7}
\]

We use \(n_+(X)\) and \(n_-(X)\) for the positive and negative inertia of a real symmetric matrix \(X\). Positive inertia is subadditive:
\[
n_+(X+Y)\le n_+(X)+n_+(Y).
\tag{8}
\]

Let \(A=[a_1\ \cdots\ a_d]\) and \(B=[b_1\ \cdots\ b_d]\). Then
\[
M=
[A\ B]
\begin{pmatrix}
0&I_d\\
I_d&0
\end{pmatrix}
[A\ B]^{\mathsf T}.
\]
The middle matrix has \(d\) positive and \(d\) negative eigenvalues. Hence
\[
n_-(M)\le d.
\tag{9}
\]

It remains to calculate the inertia of \(M_i\circ M_j\). We have
\[
\begin{aligned}
M_i\circ M_j={}&
(a_i\circ a_j)(b_i\circ b_j)^{\mathsf T}
+(b_i\circ b_j)(a_i\circ a_j)^{\mathsf T}\\
&+(a_i\circ b_j)(b_i\circ a_j)^{\mathsf T}
+(b_i\circ a_j)(a_i\circ b_j)^{\mathsf T}.
\end{aligned}
\tag{10}
\]
The four supports here are pairwise disjoint. Thus \(M_i\circ M_j\) is the adjacency matrix of the disjoint union of at most two nonempty complete bipartite graphs. Each nonempty complete bipartite graph contributes exactly one positive eigenvalue. Therefore
\[
n_+(M_i\circ M_j)=t_{ij}.
\tag{11}
\]

Applying (8) to (7), and using \(n_+(J)=1\), (9), and (11), gives
\[
|\mathcal F|=n_+(I)
 \le 1+n_+(-M)+\sum_{i<j}t_{ij}
 \le 1+d+\sum_{i<j}t_{ij}.
\]
This proves the first inequality in (3).

Since \(t_{ij}\le 1+\mathbf 1_{\{t_{ij}=2\}}\),
\[
\sum_{i<j}t_{ij}\le \binom d2+\mu(\mathcal F),
\]
which proves the second inequality. Finally, \(t_{ij}\le2\) gives
\[
|\mathcal F|\le 1+d+2\binom d2=d^2+1.
\]
∎

## Consequence for lamination-type systems

If the coordinate splits are pairwise compatible—equivalently, for every \(i<j\), at least one of
\[
A_i\cap A_j,\quad A_i\cap B_j,\quad B_i\cap A_j,\quad B_i\cap B_j
\]
is empty—then \(\mu(\mathcal F)=0\), and Theorem 1 gives
\[
|\mathcal F|\le 1+d+\binom d2
=\frac{d^2+d+2}{2}.
\tag{12}
\]
This is precisely the required asymptotic upper bound. Pairwise-compatible splits are naturally tree-like, so this is directly relevant to lamination constructions, although I cannot identify it with the omitted formal definition of “total lamination.”

# 3. Families containing a binary word

There is another simple structural case giving essentially the same bound.

## Proposition 2

If \(\mathcal F\) contains a word \(x\in\{0,1\}^d\) with no stars, then
\[
|\mathcal F|\le 1+d+\binom d2.
\tag{13}
\]

### Proof

For \(y\ne x\), define its conflict signature relative to \(x\):
\[
D_x(y)=\{i:x_i\ne y_i,\ y_i\ne *\}.
\]
By (1), \(D_x(y)\) is a nonempty subset of \([d]\) of size at most two.

The map \(y\mapsto D_x(y)\) is injective. Indeed, suppose
\[
D_x(y)=D_x(z)=S.
\]
At every \(i\in S\), both \(y_i\) and \(z_i\) equal \(1-x_i\). At every \(i\notin S\), each of \(y_i,z_i\) is either \(x_i\) or \(*\). Hence \(y\) and \(z\) have no opposing coordinate, so \(c(y,z)=0\), contrary to (1).

There are \(d+\binom d2\) possible nonempty signatures of size at most two. Adding \(x\) proves (13). ∎

Thus any asymptotic counterexample must, in particular, avoid all full-support words.

# 4. A spectral sufficient condition

The following gives a second, rather different, route to the conjectured upper bound.

Let \(G_1=G_1(\mathcal F)\) be the graph on \(\mathcal F\) in which
\[
xy\in E(G_1)\quad\Longleftrightarrow\quad c(x,y)=1.
\]
Define
\[
N=2J-M.
\]
Then
\[
N=A(G_1)+2I:
\]
its diagonal entries are \(2\), and its off-diagonal entries are \(1\) on singly covered pairs and \(0\) on doubly covered pairs.

Let
\[
P=n_+(N),\qquad Q=n_-(N).
\]
Equivalently, \(Q\) is the number of adjacency eigenvalues of \(G_1\) strictly below \(-2\).

## Lemma 3: Hadamard-square inertia

If a real symmetric matrix \(S\) has \(p\) positive and \(q\) negative eigenvalues, then
\[
n_+(S\circ S)
\le \binom{p+1}{2}+\binom{q+1}{2}.
\tag{14}
\]

### Proof

Write
\[
S=UU^{\mathsf T}-VV^{\mathsf T},
\]
where \(U\) has \(p\) columns and \(V\) has \(q\) columns. Then
\[
\begin{aligned}
S\circ S={}&
(UU^{\mathsf T})\circ(UU^{\mathsf T})
+(VV^{\mathsf T})\circ(VV^{\mathsf T})\\
&-2(UU^{\mathsf T})\circ(VV^{\mathsf T}).
\end{aligned}
\]
All three Hadamard products on the right are positive semidefinite. The first two have ranks at most
\[
\binom{p+1}{2}\quad\text{and}\quad\binom{q+1}{2},
\]
because they are Gram matrices of the symmetric tensors \(u_x\otimes u_x\) and \(v_x\otimes v_x\). Subtracting a positive semidefinite matrix cannot increase positive inertia beyond the rank of the sum of the first two terms. This proves (14). ∎

## Proposition 4

For every \(2\)-neighborly family,
\[
|\mathcal F|
\le \binom{P+1}{2}+\binom{Q+1}{2}+Q,
\tag{15}
\]
where
\[
P\le d+1,\qquad Q\le d.
\tag{16}
\]
Consequently, if \(Q=o(d)\), then
\[
|\mathcal F|\le \left(\frac12+o(1)\right)d^2.
\tag{17}
\]

### Proof

Since
\[
N=-M+2J,
\]
and \(2J\) is positive semidefinite of rank one, (9) and its positive-inertia analogue give
\[
P\le n_+(-M)+1=n_-(M)+1\le d+1,
\]
and
\[
Q\le n_-(-M)=n_+(M)\le d.
\]

Because \(N\) has diagonal \(2\) and off-diagonal entries in \(\{0,1\}\),
\[
N\circ N=N+2I.
\]
Hence
\[
2I=N\circ N-N.
\]
Using inertia subadditivity and Lemma 3,
\[
\begin{aligned}
|\mathcal F|
 &=n_+(2I)\\
 &\le n_+(N\circ N)+n_+(-N)\\
 &\le \binom{P+1}{2}+\binom{Q+1}{2}+Q.
\end{aligned}
\]
This proves (15). Substituting \(P\le d+1\) gives
\[
|\mathcal F|
\le \binom{d+2}{2}+\binom{Q+1}{2}+Q.
\tag{18}
\]
If \(Q=o(d)\), the right side is \(\frac12d^2+o(d^2)\). ∎

In particular, if
\[
\lambda_{\min}(A(G_1))\ge-2,
\]
then \(Q=0\), and
\[
|\mathcal F|\le \binom{d+2}{2}.
\tag{19}
\]

The condition \(Q=0\) is not automatic. For example, take
\[
\mathcal F=\{0^d,e_1,\ldots,e_d\},
\]
where \(e_i\) has a single \(1\). This is \(2\)-neighborly: \(0^d\) and \(e_i\) conflict once, while \(e_i,e_j\) conflict twice. Here \(G_1=K_{1,d}\), whose least eigenvalue is \(-\sqrt d<-2\) for \(d\ge5\). Nevertheless \(Q=1=o(d)\), so Proposition 4 still applies.

# 5. What any asymptotic counterexample must look like

Suppose that for some fixed \(\varepsilon>0\) there are arbitrarily large \(d\) and families satisfying
\[
|\mathcal F|\ge \left(\frac12+\varepsilon\right)d^2.
\tag{20}
\]
Then the preceding results force all of the following.

1. **A positive density of incompatible coordinate pairs.**  
   From (3),
   \[
   \mu(\mathcal F)\ge \varepsilon d^2-\frac d2-1.
   \tag{21}
   \]

2. **Linear spectral indefiniteness.**  
   From (18),
   \[
   \varepsilon d^2
   \le \frac12Q^2+\frac32Q+\frac32d+1,
   \]
   and therefore
   \[
   Q\ge \bigl(\sqrt{2\varepsilon}-o(1)\bigr)d.
   \tag{22}
   \]
   Thus the singly covered-edge graph must have linearly many adjacency eigenvalues below \(-2\).

3. **No binary member.**  
   This follows from Proposition 2 for sufficiently large \(d\).

These are simultaneous necessary conditions. The missing step is a theorem excluding a family that is both densely incompatible in the split sense and highly indefinite in the spectral sense while still having quadratic size above \(d^2/2\).

The split condition is genuinely nonautomatic. For example,
\[
\{000,011,101,110\}\subseteq\{0,1\}^3
\]
is \(2\)-neighborly, and every pair of coordinates exhibits all four binary patterns, so \(\mu=3=\binom32\).

# 6. Exact computational formulation

For finite \(d\), the problem is exactly a maximum-clique problem. Let \(H_d\) have vertex set \(\{0,1,*\}^d\), with \(x,y\) adjacent when \(c(x,y)\in\{1,2\}\). Then
\[
n(2,d)=\omega(H_d).
\]
Equivalently, the following \(0\)-\(1\) integer program is exact:
\[
\max \sum_{x\in\{0,1,*\}^d}z_x
\]
subject to
\[
z_x+z_y\le1
\quad\text{whenever }x\ne y\text{ and }c(x,y)\notin\{1,2\},
\qquad z_x\in\{0,1\}.
\]
Coordinate permutations and independent \(0\leftrightarrow1\) swaps give the symmetry group \(S_d\ltimes C_2^d\). I have not run this computation and claim no new exact values.

# 7. Conclusion and gap

The argument establishes:

\[
\left(\frac12-o(1)\right)d^2
\le n(2,d)\le d^2+1,
\]
and proves the desired upper asymptotic in each of the following cases:

- the coordinate split system has \(o(d^2)\) incompatible pairs;
- the singly covered-edge graph has \(o(d)\) eigenvalues below \(-2\);
- the family contains a binary word.

The unrestricted conjecture remains open. In particular, I do not have a bound forcing either \(\mu(\mathcal F)=o(d^2)\) or \(Q=o(d)\) for an arbitrary extremal family. The arguments are self-contained, but I have not verified whether some or all of these partial bounds already occur in the full source or its follow-up.