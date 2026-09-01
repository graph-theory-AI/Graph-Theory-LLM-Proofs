```json
{
  "verdict": "disproved",
  "confidence": "medium",
  "one_line": "For the standard unnormalised ℓ1 representative discrepancy, the signing h(x_i y_j)=s_j e_i on K_{k,k} forces f_h(M)=k for every perfect matching.",
  "would_publish": false,
  "caveats": "The prompt omits the definition of f_h; the counterexample is conclusive if f_h is the unnormalised centred ℓ1 error described by the catalog."
}
```

## Interpretation of \(f_h\)

The statement is not formally self-contained because \(f_h(M)\) is undefined. I use the standard definition of representative discrepancy indicated by the catalog prose:
\[
f_h(M)
 =
 \left\|
 \sum_{e\in M}h(e)
 -
 \frac1n\sum_{e\in E(K_{n,n})}h(e)
 \right\|_1.
\tag{1}
\]
Equivalently, the coefficient \(1/n\) is \(|M|/|E(K_{n,n})|\). Under this interpretation the conjecture is false, with a linear lower bound.

## Counterexample

Let \(k\) be even and put \(n=k\). Write the two vertex classes as
\[
L=\{x_1,\dots,x_k\},
\qquad
R=\{y_1,\dots,y_k\}.
\]
Let \(e_1,\dots,e_k\) be the standard basis of \(\mathbb R^k\), and define
\[
s_j=
\begin{cases}
 1,&1\le j\le k/2,\\
 -1,&k/2<j\le k.
\end{cases}
\]
For every edge \(x_i y_j\), set
\[
h(x_i y_j)=s_j e_i.
\tag{2}
\]
Then
\[
\|h(x_i y_j)\|_1=1
\]
for every edge, as required.

Moreover, the total edge-label is zero:
\[
\sum_{e\in E(K_{k,k})}h(e)
 =
 \sum_{i=1}^k\sum_{j=1}^k s_j e_i
 =
 \sum_{i=1}^k e_i\left(\sum_{j=1}^k s_j\right)
 =0.
\tag{3}
\]

Every perfect matching has the form
\[
M_\pi=\{x_i y_{\pi(i)}:i\in[k]\}
\]
for a permutation \(\pi\). Its label sum is
\[
\sum_{e\in M_\pi}h(e)
 =
 \sum_{i=1}^k s_{\pi(i)}e_i.
\tag{4}
\]
Every coordinate of this vector is either \(1\) or \(-1\). Consequently,
\[
f_h(M_\pi)
 =
 \left\|\sum_{e\in M_\pi}h(e)\right\|_1
 =
 \sum_{i=1}^k |s_{\pi(i)}|
 =
 k.
\tag{5}
\]
Thus every perfect matching has discrepancy exactly \(k\).

If a universal constant \(C\) satisfied the conjectured bound, then for all sufficiently large even \(k\) this instance would have a matching with
\[
k=f_h(M)\le C\sqrt{k},
\]
which is impossible once \(k>C^2\).

Hence the worst-case discrepancy is at least \(k\), not \(O(\sqrt{k})\), under definition (1).

## Robust variants

### Nonnegative labels

The obstruction is not dependent on signed labels. Define instead
\[
h(x_i y_j)=
\begin{cases}
e_i,&j\le k/2,\\
0,&j>k/2.
\end{cases}
\]
Then
\[
\frac1k\sum_{e\in E(K_{k,k})}h(e)=\frac12\mathbf 1.
\]
For a perfect matching \(M_\pi\), its \(i\)-th coordinate is either \(0\) or \(1\), so every coordinate differs from \(1/2\) by exactly \(1/2\). Therefore
\[
f_h(M_\pi)=\frac{k}{2}
\]
for every perfect matching.

### Even row- and column-balanced labels

Even additional local zero-sum conditions would not repair the \(\ell_1\) formulation. Define
\[
u_i=\frac{e_i-k^{-1}\mathbf1}{2(1-1/k)}
\quad\text{and}\quad
h(x_i y_j)=s_j u_i.
\]
Then \(\|u_i\|_1=1\), and
\[
\sum_jh(x_i y_j)=0
\quad\text{for every }x_i,
\qquad
\sum_i h(x_i y_j)=0
\quad\text{for every }y_j.
\]
For a perfect matching, putting \(\varepsilon_i=s_{\pi(i)}\), one has \(\sum_i\varepsilon_i=0\), and hence
\[
\sum_{e\in M_\pi}h(e)
 =\frac{1}{2(1-1/k)}(\varepsilon_1,\dots,\varepsilon_k).
\]
Thus
\[
f_h(M_\pi)=\frac{k}{2(1-1/k)}=\Omega(k)
\]
for every matching.

## Gap caused by the missing definition

The conclusion above depends critically on \(f_h\) being the unnormalised centred \(\ell_1\)-norm in (1). If the source actually defines \(f_h\) using, for example, the Euclidean norm, then the first construction gives only
\[
\left\|\sum_{e\in M}h(e)\right\|_2=\sqrt{k},
\]
which is consistent with the conjectured order. Likewise its \(\ell_\infty\)-discrepancy is \(1\).

Therefore either:

1. \(f_h\) is the centred \(\ell_1\)-discrepancy described by the catalog, in which case the conjecture as extracted is disproved by (2); or
2. the source uses a different definition or has an omitted hypothesis, in which case that definition or hypothesis is indispensable and the extracted statement is ill-posed.