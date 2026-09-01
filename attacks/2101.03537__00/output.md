```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general polylogarithmic question remains open, but linear bounds hold for all extreme-star patterns, and the exact value for the 2-by-2 identity is ceil(n/2).",
  "would_publish": false,
  "caveats": "The polylogarithmic quantifiers are informal, and these elementary special cases may overlap the prior two-row results mentioned in the source."
}
```

## 1. Precise formulation

Rows and columns are ordered, and containment means taking increasing subsequences of rows and columns. Write \(\overline H\) for the entrywise complement of \(H\). Thus the admissible matrices are those containing neither \(H\) nor \(\overline H\).

For an \(n\times n\) matrix \(M\), let
\[
\phi(M)=\max\{\min(|A|,|B|):M[A,B]\text{ is constant}\}.
\]
Then
\[
f_H(n)=\min\{\phi(M):M\text{ contains neither }H\text{ nor }\overline H\}.
\]

A natural precise interpretation of the informal polylogarithmic proposal is:

\[
(\mathrm{PL})_H:\qquad
\exists c_H>0,\ C_H<\infty,\ n_0(H)
\quad
f_H(n)\ge \frac{c_Hn}{(\log(2+n))^{C_H}}
\quad(n\ge n_0(H)).
\]

The phrase in the source does not specify whether \(C_H\) may depend on \(H\); I use the usual, weaker interpretation that it may.

I do not prove \((\mathrm{PL})_H\) for every acyclic \(H\), nor do I construct an acyclic \(H\) for which \(f_H(n)=o(n)\). The results below establish the stronger linear conclusion for some explicit infinite families.

---

## 2. Two elementary lemmas

### Lemma 2.1: avoiding a binary subsequence bounds alternation

Let \(w\) be a binary word of length \(q\), and let \(x\) be a binary word which does not contain \(w\) as a subsequence. Then \(x\) has at most \(2q-1\) runs, and hence at most
\[
2q-2
\]
transitions between consecutive positions.

#### Proof

Suppose that \(x\) has at least \(2q\) nonempty runs. Number the runs in order. To embed \(w=w_1\cdots w_q\), choose a run of bit \(w_1\) among the first two runs. Having chosen a run for \(w_i\), choose the next run if \(w_{i+1}\ne w_i\), and the run two places later if \(w_{i+1}=w_i\). The run chosen for \(w_q\) has index at most \(2q\). Choosing one position from every selected run gives \(w\) as a subsequence, a contradiction. ∎

### Lemma 2.2: bounded row alternation gives a linear pure rectangle

Let \(N\) be an \(m\times s\) binary matrix in which every row has at most \(T\) transitions. Put
\[
L=2T+1.
\]
Then \(N\) has a constant submatrix \(N[A,B]\) with
\[
|A|\ge \left\lfloor\frac m4\right\rfloor,
\qquad
|B|\ge \left\lfloor\frac sL\right\rfloor.
\]

#### Proof

Partition the columns, in order, into \(L\) intervals whose sizes differ by at most one. Call a row-block pair bad if the row is nonconstant on that block. Each row is bad on at most \(T\) blocks, so there are at most \(Tm\) bad row-block pairs.

Consequently, some block is bad for at most
\[
\frac{Tm}{L}<\frac m2
\]
rows. More than \(m/2\) rows are constant on that block, and at least half of those constant rows have the same value there. The chosen block has at least \(\lfloor s/L\rfloor\) columns. ∎

---

## 3. One-row patterns

### Proposition 3.1

Let \(H\) be a \(1\times q\) matrix. Then, whenever the admissible class is nonempty,
\[
f_H(n)\ge
\min\left\{
\left\lfloor\frac n4\right\rfloor,
\left\lfloor\frac{n}{4q-3}\right\rfloor
\right\}.
\]
In particular, \(f_H(n)=\Omega_H(n)\). The same holds for \(q\times1\) patterns.

#### Proof

Write \(H\) as the word \(h\). Since \(M\) contains no copy of \(H\), every row of \(M\) avoids \(h\) as a subsequence. By Lemma 2.1, every row has at most \(T=2q-2\) transitions. Apply Lemma 2.2 with \(L=4q-3\).

The column version follows by transposition. ∎

This proof does not even use the assumption that \(\overline M\) avoids \(H\).

---

## 4. Extreme-star matrices

Call a \(p\times q\) matrix an extreme-star matrix if all its \(1\)'s lie in its first row or all lie in its last row. Its \(1\)-graph is a star together with isolated vertices, hence is acyclic.

We first need a standard counting lemma.

### Lemma 4.1: a fixed-height monochromatic rectangle

Let \(k\ge1\), and let \(N\) be an \(m\times s\) binary matrix with \(m\ge4k\). Then there are \(k\) rows and at least
\[
\frac{s}{4^k}
\]
columns on which all \(k\) selected rows have the same value.

#### Proof

One of the two values, say \(a\), occurs in at least \(ms/2\) positions. Let \(d_j\) be the number of occurrences of \(a\) in column \(j\). Then
\[
\sum_{j=1}^s d_j\ge \frac{ms}{2}.
\]
Counting pairs consisting of a \(k\)-set of rows and a column in which all those rows have value \(a\), and using the discrete convexity of \(d\mapsto\binom dk\), gives
\[
\sum_{j=1}^s\binom{d_j}{k}
 \ge
s\binom{\lfloor m/2\rfloor}{k}.
\]
Hence some \(k\)-set of rows has at least
\[
s\frac{\binom{\lfloor m/2\rfloor}{k}}{\binom mk}
\]
common \(a\)-columns. Since \(m\ge4k\), every factor in the quotient is at least \(1/4\), so the quotient is at least \(4^{-k}\). ∎

### Theorem 4.2: linear bound for extreme stars

Let
\[
H=
\begin{pmatrix}
h\\
0^q\\
\vdots\\
0^q
\end{pmatrix}
\]
be a \(p\times q\) matrix, where \(h\) is an arbitrary binary word. Then
\[
f_H(n)=\Omega_{p,q}(n).
\]
More explicitly, for \(p\ge2\), \(n\ge8(p-1)\), and \(L=4q-3\),
\[
f_H(n)\ge
\min\left\{
\left\lfloor\frac{\lfloor n/2\rfloor}{4}\right\rfloor,\,
\left\lfloor\frac{n}{4^{p-1}L}\right\rfloor
\right\}.
\]
The same conclusion holds if the nonzero row is last, or, by transposition, if all \(1\)'s lie in the first or last column.

#### Proof

Put \(k=p-1\). Divide the rows of an admissible \(n\times n\) matrix \(M\) into a first half \(R^-\) and a last half \(R^+\).

Apply Lemma 4.1 to \(M[R^+,[n]]\). It gives \(k\) rows
\[
Z\subseteq R^+
\]
and a column set \(S\), with
\[
|S|\ge \frac{n}{4^k},
\]
such that every entry of \(M[Z,S]\) is the same value \(a\).

Consider any row \(i\in R^-\).

- If \(a=0\), then \(M[i,S]\) cannot contain \(h\) as a subsequence: together with the rows \(Z\), this would form \(H\).
- If \(a=1\), then \(M[i,S]\) cannot contain \(\overline h\): together with \(Z\), this would form \(\overline H\).

Thus all rows of \(M[R^-,S]\) avoid the same word of length \(q\). By Lemma 2.1, each has at most \(2q-2\) transitions. Lemma 2.2 now gives a constant rectangle with at least
\[
\left\lfloor\frac{|R^-|}{4}\right\rfloor
\]
rows and at least
\[
\left\lfloor\frac{|S|}{4q-3}\right\rfloor
\ge
\left\lfloor\frac{n}{4^{p-1}(4q-3)}\right\rfloor
\]
columns.

If the exceptional row of \(H\) is last, reverse the row orders. Transposition gives the column versions. ∎

This proves the linear conjecture for an infinite family of ordered acyclic matrices of arbitrarily large dimensions.

### A sharper repeated-star subcase

Let \(H_p\) be the \(p\times2\) matrix all of whose rows are \((1,0)\). Then
\[
f_{H_p}(n)\ge
\left\lfloor
\frac{\lceil n/2\rceil+p-1}{p}
\right\rfloor.
\]

Indeed, for every ordered pair of columns, at most \(p-1\) rows have trace \(10\), and at most \(p-1\) rows have trace \(01\). Fix the first column and choose a value \(a\) occurring there on at least \(\lceil n/2\rceil\) rows. In every other column, at most \(p-1\) of these rows disagree with \(a\). For
\[
b=
\left\lfloor
\frac{\lceil n/2\rceil+p-1}{p}
\right\rfloor,
\]
the union of the exceptional rows over the first \(b\) columns leaves at least \(b\) rows, giving a constant \(b\times b\) submatrix.

---

## 5. Exact solution for the \(2\times2\) identity

Let
\[
I_2=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

### Theorem 5.1

For every \(n\ge1\),
\[
f_{I_2}(n)=\left\lceil\frac n2\right\rceil.
\]

#### Proof: lower bound

Let \(M\) contain neither \(I_2\) nor \(\overline{I_2}\), and for each row \(r\), let \(N_r\) be the set of columns containing a \(1\) in that row.

Any two row-neighborhoods are comparable by inclusion. Indeed, if rows \(r<s\) were incomparable, choose
\[
x\in N_r\setminus N_s,\qquad
y\in N_s\setminus N_r.
\]
If \(x<y\), rows \(r,s\) and columns \(x,y\) form \(I_2\); if \(y<x\), they form \(\overline{I_2}\).

Order the row-neighborhoods as
\[
N_1\subseteq N_2\subseteq\cdots\subseteq N_n,
\]
where this is an abstract inclusion ordering, not necessarily the original row order. Put \(k=\lceil n/2\rceil\) and \(S=N_k\).

If \(|S|\ge\lceil n/2\rceil\), then the rows \(k,k+1,\ldots,n\) are all \(1\) on \(S\), giving a square of order \(\lceil n/2\rceil\).

If \(|S|<\lceil n/2\rceil\), then the first \(k\) rows are all \(0\) on \([n]\setminus S\), and both dimensions are at least \(\lceil n/2\rceil\).

Thus
\[
f_{I_2}(n)\ge\left\lceil\frac n2\right\rceil.
\]

#### Proof: upper bound

Take the lower-triangular matrix
\[
M_{ij}=1\quad\Longleftrightarrow\quad j\le i.
\]
Its row-neighborhoods are nested, so it avoids both checkerboards.

For an all-\(1\) rectangle \(A\times B\), one must have
\[
\max B\le \min A.
\]
If it contains a \(t\times t\) square, then for \(r=\min A\),
\[
t\le r,\qquad t\le n-r+1,
\]
and hence \(t\le\lceil n/2\rceil\).

For an all-\(0\) rectangle one must have
\[
\min B>\max A,
\]
which gives \(t\le\lfloor n/2\rfloor\). Therefore the largest pure square in this matrix has order exactly \(\lceil n/2\rceil\). ∎

### Corollary 5.2

Every nonconstant acyclic \(2\times2\) matrix satisfies the linear conclusion.

Indeed:

- one or three \(1\)'s reduce, after possibly complementing, to an extreme-star matrix;
- two adjacent \(1\)'s reduce to an extreme-star matrix after possibly transposing;
- two diagonal \(1\)'s are \(I_2\) or \(\overline{I_2}\).

---

## 6. Why this does not settle the general problem

The arguments above rely on strong structural features which fail for a general ordered forest.

For example,
\[
P=
\begin{pmatrix}
1&1&0\\
0&1&1\\
0&0&1
\end{pmatrix}
\]
is acyclic: its \(1\)-graph is the path
\[
c_1-r_1-c_2-r_2-c_3-r_3.
\]
It has no constant row or column and is not covered by the extreme-star argument.

Moreover, forbidding such a multirow pattern does not bound the alternation of individual rows. For instance, a matrix all of whose rows equal
\[
010101\cdots
\]
contains neither \(P\) nor \(\overline P\), because every selected collection of rows is identical while the rows of \(P\) are distinct. Thus the bounded-transition mechanism cannot be applied row by row. This example itself has a large pure pair, so it is not a counterexample; it only demonstrates the failure of the local approach.

Finally, the established \(n^{1-o(1)}\) result does not formally imply a polylogarithmic loss. For example,
\[
g(n)=n\exp(-\sqrt{\log n})
\]
satisfies \(g(n)=n^{1-o(1)}\), but for every fixed \(C\),
\[
\frac{g(n)}{n/(\log n)^C}
=(\log n)^C e^{-\sqrt{\log n}}\longrightarrow0.
\]

Thus the remaining gap is genuine:

1. no acyclic \(H\) with \(f_H(n)=o(n)\) is constructed here;
2. no \(n/\operatorname{polylog}n\) bound is proved for arbitrary acyclic \(H\);
3. synchronization among several distinct row and column patterns is the obstacle not addressed by the arguments above.

The source notes that some two-row cases were previously known. I have not verified the exact scope of that result, so I do not claim the special cases above are new.