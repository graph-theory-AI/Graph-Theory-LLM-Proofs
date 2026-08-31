```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "Without an independent definition of twin-width for rational matrices the claimed equivalence is tautological or undefined; bounded grid rank does satisfy it over every infinite field, while the natural equality-contraction extension is false.",
  "would_publish": false,
  "caveats": "The full source question is truncated, and the grid-rank conclusion uses the precise definition stated below."
}
```

# Mathematical writeup

## 1. Status of the stated question

As written, the assertion
\[
\mathcal C\text{ has bounded twin-width}
\quad\Longleftrightarrow\quad
\operatorname{LM}(\mathcal C)\ne\operatorname{Mat}(\mathbb Q)
\tag{1}
\]
does not have a definite truth value, because “twin-width” of a \(\mathbb Q\)-matrix has not been independently defined.

There are three natural readings.

1. If bounded twin-width over \(\mathbb Q\) is **defined** by the right-hand side of (1), then (1) is tautological.
2. If twin-width means the usual equality-based contraction parameter for edge-coloured matrices, extended to infinitely many colours, then (1) is false; an explicit rank-one counterexample is given in Section 5.
3. If the intended independent parameter is the usual field-valued **grid rank**, then (1) has a clean affirmative analogue over every infinite field. This is proved below.

Thus the catalogued statement needs an independent definition before it can be classified simply as true or false.

---

## 2. Linear minors and grid rank

Let \(F\) be a field, and let all matrices be finite and have fixed row and column orders.

A matrix \(B\) is a **linear minor** of \(A\) if it is obtained by repeatedly replacing consecutive rows, or consecutive columns, by arbitrary linear combinations. Equivalently,
\[
B=XAY,
\tag{2}
\]
where the supports of the rows of \(X\) form consecutive, pairwise disjoint row intervals of \(A\), in their natural order, and the supports of the columns of \(Y\) similarly form consecutive column intervals.

For \(A\in F^{p\times q}\), define its field grid rank \(\operatorname{gr}_F(A)\) to be the largest \(k\) for which there are partitions
\[
[p]=R_1\sqcup\cdots\sqcup R_k,\qquad
[q]=C_1\sqcup\cdots\sqcup C_k
\]
into nonempty consecutive intervals such that
\[
\operatorname{rank}_F A[R_i,C_j]\ge k
\qquad\text{for all }i,j\in[k].
\tag{3}
\]

This is the grid-rank convention used throughout the argument.

---

## 3. Grid rank is monotone under linear minors

### Lemma 3.1
If \(B\) is a linear minor of \(A\), then
\[
\operatorname{gr}_F(B)\le \operatorname{gr}_F(A).
\]

### Proof

Write \(B=XAY\) as in (2). Suppose \(B\) has a \(k\)-division witnessing \(\operatorname{gr}_F(B)\ge k\). Each interval of output rows lifts to the union of the corresponding consecutive source-row intervals; hence it lifts to a consecutive interval of rows of \(A\). The same holds for columns.

For every lifted pair \((\widehat R_i,\widehat C_j)\),
\[
B[R_i,C_j]
=
X_i\,A[\widehat R_i,\widehat C_j]\,Y_j
\]
for suitable restrictions \(X_i,Y_j\). Consequently,
\[
\operatorname{rank} B[R_i,C_j]
\le
\operatorname{rank} A[\widehat R_i,\widehat C_j].
\]
Thus a rank-\(k\), \(k\times k\) division of \(B\) lifts to one of \(A\). ∎

---

## 4. Over an infinite field, a rank grid is universal

The following is the main observation.

### Lemma 4.1
Let \(F\) be infinite. If \(\operatorname{gr}_F(A)\ge k\), then every \(k\times k\) matrix over \(F\) is a linear minor of \(A\).

### Proof

Fix intervals \(R_1,\dots,R_k\) and \(C_1,\dots,C_k\) witnessing (3), and write
\[
A_{ij}=A[R_i,C_j].
\]
For each \(i,j\), regard \(A_{ij}\) as a linear map
\[
T_{ij}:F^{C_j}\longrightarrow F^{R_i},
\qquad
z\longmapsto A_{ij}z.
\]
Its image has dimension at least \(k\).

We first choose vectors \(z_j\in F^{C_j}\) such that, for every fixed \(i\),
\[
T_{i1}z_1,\ldots,T_{ik}z_k
\tag{4}
\]
are linearly independent.

For a fixed \(i\), consider the vector-valued polynomial
\[
\Phi_i(z_1,\ldots,z_k)
=
T_{i1}z_1\wedge\cdots\wedge T_{ik}z_k
\in \bigwedge^k F^{R_i}.
\]
It is not identically zero. Indeed, for this fixed \(i\), choose the \(z_j\) successively. After \(j-1\) choices, the span of the previously chosen images has dimension at most \(j-1<k\), whereas
\[
\dim\operatorname{im}T_{ij}\ge k.
\]
Thus \(\operatorname{im}T_{ij}\) is not contained in that span, and \(z_j\) can be chosen so that independence is preserved.

Choose a nonzero scalar coordinate polynomial \(f_i\) of \(\Phi_i\). The product
\[
f=\prod_{i=1}^k f_i
\]
is a nonzero polynomial. Since \(F\) is infinite, a nonzero polynomial over \(F\) cannot vanish at every point of its affine space. Hence there is a simultaneous choice of \(z_1,\dots,z_k\) with \(f\ne0\). For that choice, (4) is independent for every \(i\).

Now let \(D=(d_{ij})\in F^{k\times k}\) be arbitrary. For each \(i\), the vectors in (4) are independent, so there is a linear functional
\[
x_i^{\mathsf T}:F^{R_i}\longrightarrow F
\]
such that
\[
x_i^{\mathsf T}A_{ij}z_j=d_{ij}
\qquad (j\in[k]).
\]
Combine the rows in \(R_i\) using coefficients \(x_i\), and combine the columns in \(C_j\) using coefficients \(z_j\). The resulting matrix has entry
\[
(x_i^{\mathsf T}A_{ij}z_j)_{i,j}=D.
\]
The supports are the prescribed consecutive intervals, so this is a linear-minor operation. ∎

The infinitude of \(F\) is used only when finding a common point outside finitely many proper algebraic zero sets. That step is not valid over a fixed finite field.

---

## 5. Exact infinite-field characterization by grid rank

### Theorem 5.1
Let \(F\) be any infinite field and let \(\mathcal C\) be a class of ordered \(F\)-matrices. Then
\[
\operatorname{LM}(\mathcal C)\ne\operatorname{Mat}(F)
\quad\Longleftrightarrow\quad
\sup_{A\in\mathcal C}\operatorname{gr}_F(A)<\infty.
\tag{5}
\]

### Proof

#### Unbounded grid rank implies all matrices occur

Suppose the grid ranks in \(\mathcal C\) are unbounded. Given \(D\in F^{m\times n}\), let \(k=\max\{m,n\}\), and pad \(D\) with zero rows and columns to a \(k\times k\) matrix \(\widetilde D\).

Choose \(A\in\mathcal C\) with \(\operatorname{gr}_F(A)\ge k\). By Lemma 4.1, \(\widetilde D\) is a linear minor of \(A\). Combining the padded zero rows and columns into the final retained row and column, using coefficient zero on the padded entries, gives \(D\) as a further linear minor. Thus every finite \(F\)-matrix belongs to \(\operatorname{LM}(\mathcal C)\).

#### Bounded grid rank gives an explicit excluded matrix

Suppose instead that
\[
\operatorname{gr}_F(A)\le d
\qquad\text{for all }A\in\mathcal C.
\]
Set \(t=d+1\), and define
\[
H_t=J_t\otimes I_t.
\]
Order its rows as pairs \((i,r)\in[t]^2\), first by \(i\), and its columns as pairs \((j,s)\), first by \(j\). Thus \(H_t\) is a \(t\times t\) block matrix in which every block is \(I_t\).

The block partition witnesses
\[
\operatorname{gr}_F(H_t)\ge t.
\]
In fact equality holds by the dimension bound, but only the lower bound is needed. By Lemma 3.1, \(H_t\) cannot be a linear minor of any member of \(\mathcal C\). Therefore the linear-minor closure is proper. ∎

### Quantitative form

If an \(m\times n\) matrix \(D\) is excluded from \(\operatorname{LM}(\mathcal C)\), then
\[
\operatorname{gr}_F(A)<\max\{m,n\}
\qquad\text{for every }A\in\mathcal C.
\]
Conversely, if all members have grid rank at most \(d\), the explicit matrix \(H_{d+1}\) is excluded.

Thus, if the intended infinite-field surrogate for bounded twin-width is **bounded field grid rank**, the desired linear-minor characterization is completely valid over \(\mathbb Q\), and indeed over every infinite field.

---

## 6. Counterexample to the equality-contraction interpretation

There is also a canonical way to extend ordinary matrix twin-width to an infinite alphabet: regard an \(F\)-matrix as an edge-coloured complete bipartite graph, one colour for each field element. A pair of row and column bags is red when the corresponding submatrix is not constant. Width is the maximum red degree during row- and column-bag contractions.

Under this interpretation, (1) is false.

For \(n\ge1\), let
\[
A_n=(2^i3^j)_{i,j=1}^n\in\mathbb Q^{n\times n}.
\]

### Linear-minor closure

We have
\[
A_n=
\begin{pmatrix}2\\2^2\\ \vdots\\2^n\end{pmatrix}
\begin{pmatrix}3&3^2&\cdots&3^n\end{pmatrix},
\]
so \(\operatorname{rank}_{\mathbb Q}(A_n)=1\). Ordinary rank cannot increase under row or column linear combinations. Hence every linear minor of every \(A_n\) has rank at most \(1\). In particular,
\[
I_2\notin \operatorname{LM}(\{A_n:n\ge1\}).
\]

### Equality-based contraction width

All entries of \(A_n\) are distinct, by unique factorization. More specifically, any two distinct rows differ in every column, and any two distinct columns differ in every row.

At the first contraction:

- if two rows are contracted, the resulting row bag is red-adjacent to every one of the \(n\) singleton column bags;
- if two columns are contracted, the analogous statement holds with rows and columns exchanged.

Thus every contraction sequence has width at least \(n\). This remains unbounded whether or not contractions are required to be consecutive.

Consequently, the class
\[
\mathcal A=\{A_n:n\ge1\}
\]
has proper linear-minor closure but unbounded equality-based twin-width. Notice also that every \(A_n\) has field grid rank at most \(1\), showing precisely why a field-sensitive notion cannot simply be the infinite-colour equality parameter.

---

## 7. Conclusion and remaining gap

The possibilities are therefore:

- **Definition by linear-minor freeness:** the catalogued statement is a definition, not a conjecture.
- **Definition by bounded field grid rank:** the characterization is true over every infinite field, by Theorem 5.1.
- **Usual equality-based contraction twin-width:** the characterization is false, by the rank-one family \(A_n\).

What remains genuinely unresolved from the supplied formulation is whether there is a useful field-sensitive contraction-sequence parameter over \(\mathbb Q\) that:

1. agrees, at the level of bounded classes, with bounded grid rank/linear-minor freeness;
2. supplies compact certificates analogous to bounded-width contraction sequences;
3. supports the matrix-product and algorithmic consequences proved over finite fields.

The argument above does not construct such contraction sequences and does not address closure under matrix multiplication. I also cannot determine from the truncated source whether the grid-rank equivalence was already observed there.