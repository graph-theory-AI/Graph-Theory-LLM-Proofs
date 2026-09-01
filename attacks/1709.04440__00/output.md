```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exponent is determined for k=3, and the lower-endpoint exponent is exact for systems with bounded cycle-to-matching ratio, but the unrestricted k>3 gap remains.",
  "would_publish": false,
  "caveats": "The high-dimensional case with many off-diagonal cycles is not controlled, so no new exact value for k>3 is proved."
}
```

# Mathematical writeup

## 1. Normalized formulation

Let \(V=\mathbb F_p^n\), \(N=|V|=p^n\), and let \(X_1,\dots,X_k\subseteq V\). Write
\[
T(X_1,\dots,X_k)
 =
\#\{(x_1,\dots,x_k)\in X_1\times\cdots\times X_k:
x_1+\cdots+x_k=0\}.
\]

Regard the \(X_i\) as disjoint color classes, even if the same vector occurs in several of them. Let \(\tau(X_1,\dots,X_k)\) be the minimum total number of colored elements that must be deleted to destroy all \(k\)-cycles.

Changing between a total deletion budget and a budget of \(\varepsilon N\) in each color changes \(\varepsilon\) by at most a factor of \(k\), and hence does not change the optimal polynomial exponent.

Call \(C\) admissible if there is \(a_{p,k,C}>0\) such that
\[
\tau(X_1,\dots,X_k)\ge \varepsilon N
\quad\Longrightarrow\quad
T(X_1,\dots,X_k)\ge
a_{p,k,C}\varepsilon^C N^{k-1}
\tag{1}
\]
for all \(n\) and \(0<\varepsilon\le 1\). Let \(C^*_{p,k}\) be the infimum of the admissible exponents. The formulation in the source, with \(\delta=(\varepsilon/2)^C\), is of this form.

## 2. The constants \(c_{p,k}\)

Put
\[
S_p(x)=1+x+\cdots+x^{p-1},
\]
and define
\[
\Gamma_{p,k}
 =
\inf_{0<x<1} S_p(x)x^{-(p-1)/k},
\qquad
c_{p,k}=1-\log_p\Gamma_{p,k}.
\tag{2}
\]
Thus
\[
\Gamma_{p,k}=p^{1-c_{p,k}}.
\]

The infimum is attained at the unique \(\rho=\rho_{p,k}\in(0,1)\) satisfying
\[
\frac{\rho S'_p(\rho)}{S_p(\rho)}
 =
\frac{p-1}{k}.
\tag{3}
\]
In particular \(0<c_{p,k}<1\).

For \(p=2\), the optimizer is \(\rho=1/(k-1)\), giving
\[
c_{2,k}=1-h_2(1/k),
\tag{4}
\]
where \(h_2(t)=-t\log_2t-(1-t)\log_2(1-t)\).

Also \(c_{p,k}\) is strictly increasing in \(k\). Indeed, if
\[
G(\mu)=\inf_{0<x<1}S_p(x)x^{-\mu},
\]
then \(G(\mu)\) is strictly increasing for \(0<\mu<(p-1)/2\). Since \((p-1)/k\) decreases with \(k\), \(c_{p,k}=1-\log_pG((p-1)/k)\) strictly increases.

## 3. The certified interval and the solved case \(k=3\)

The source theorem gives
\[
C^*_{p,k}
\le
1+\frac{k-2}{c_{p,3}}.
\tag{5}
\]

On the other hand, the multicolored sum-free constructions give
\[
C^*_{p,k}
\ge
1+\frac{k-2}{c_{p,k}}.
\tag{6}
\]

For completeness, here is the deduction of (6). A \(k\)-multicolored sum-free family of size \(m\) consists of vectors
\[
(x_{1,i},\dots,x_{k,i})\in V^k,\qquad i=1,\dots,m,
\]
such that
\[
x_{1,i}+\cdots+x_{k,i}=0
\]
and
\[
x_{1,i_1}+\cdots+x_{k,i_k}=0
\quad\Longrightarrow\quad
i_1=\cdots=i_k.
\tag{7}
\]
The verified Lovász result quoted in the prompt gives, for fixed \(p,k\),
\[
m=N^{1-c_{p,k}-o(1)}.
\tag{8}
\]

Set \(X_j=\{x_{j,i}:1\le i\le m\}\). Condition (7) implies that the only cycles are the \(m\) diagonal ones. These cycles are vertex-disjoint, so \(T=\tau=m\). Consequently
\[
\varepsilon=\frac{m}{N}=N^{-c_{p,k}-o(1)}
\]
and
\[
\delta=\frac{T}{N^{k-1}}
 =N^{-(k-2+c_{p,k})-o(1)}
 =\varepsilon^{\,1+(k-2)/c_{p,k}+o(1)}.
\]
Thus no exponent smaller than \(1+(k-2)/c_{p,k}\) can satisfy (1).

Combining (5) and (6),
\[
\boxed{
1+\frac{k-2}{c_{p,k}}
\le C^*_{p,k}
\le
1+\frac{k-2}{c_{p,3}}.
}
\tag{9}
\]

For \(k=3\), the two endpoints agree. Hence the question is completely answered in that case:

\[
\boxed{
C^*_{p,3}=1+\frac{1}{c_{p,3}}.
}
\tag{10}
\]

For example,
\[
c_{2,3}=1-h_2(1/3)\approx0.0817042,
\]
so
\[
C^*_{2,3}\approx13.2393.
\]

For comparison, when \(p=2,k=4\), the present interval is
\[
11.5976\ldots
=
1+\frac{2}{1-h_2(1/4)}
\le C^*_{2,4}
\le
1+\frac{2}{1-h_2(1/3)}
=
25.4786\ldots.
\]

Since \(c_{p,k}>c_{p,3}\) for every \(k>3\), the bounds in (9) are then genuinely distinct.

## 4. A robust matching-to-sum-free extraction lemma

The following elementary lemma gives a concrete partial use of \(c_{p,k}\) on the upper-bound side. No novelty claim is made.

Let \(A_{p,k}(n)\) denote the maximum size of a \(k\)-multicolored sum-free family in \(\mathbb F_p^n\). The polynomial/slice-rank argument gives
\[
A_{p,k}(n)\le kN^{1-c_{p,k}}.
\tag{11}
\]

Indeed, the zero-sum indicator is represented over \(\mathbb F_p\) by
\[
P(z_1,\dots,z_k)
 =
\prod_{\ell=1}^n
\left(1-(z_{1,\ell}+\cdots+z_{k,\ell})^{p-1}\right).
\]
Every monomial in its expansion has total degree at most \((p-1)n\), so some block has degree at most \((p-1)n/k\). The number of possible monomials in one such block is at most
\[
\inf_{0<x<1}
\bigl(S_p(x)x^{-(p-1)/k}\bigr)^n
=
N^{1-c_{p,k}}.
\]
Grouping by the low-degree block gives slice rank at most \(kN^{1-c_{p,k}}\). Restriction to a multicolored sum-free family is a diagonal tensor of slice rank equal to the family size, proving (11).

Now suppose
\[
\mathcal M=
\{(x_{1,i},\dots,x_{k,i}):1\le i\le m\}
\]
is a vertex-disjoint family of \(k\)-cycles. Let
\[
T_{\mathcal M}
 =
\#\{(i_1,\dots,i_k)\in[m]^k:
x_{1,i_1}+\cdots+x_{k,i_k}=0\}.
\]

### Lemma
\[
T_{\mathcal M}
\ge
\frac{m^2}{4A_{p,k}(n)}
\ge
\frac{m^2}{4kN^{1-c_{p,k}}}.
\tag{12}
\]

### Proof

Select every index \(i\in[m]\) independently with probability
\[
q=\frac{m}{2T_{\mathcal M}}\le \frac12.
\]
Every non-diagonal cycle uses at least two distinct indices, so its probability of surviving is at most \(q^2\). If \(R\) is the selected index set and \(Z\) is the number of surviving non-diagonal cycles, then
\[
\mathbb E(|R|-Z)
\ge
qm-q^2T_{\mathcal M}
=
\frac{m^2}{4T_{\mathcal M}}.
\]
For some outcome, therefore,
\[
|R|-Z\ge\frac{m^2}{4T_{\mathcal M}}.
\]
Delete one index from each surviving non-diagonal cycle. At most \(Z\) indices are deleted, leaving a multicolored sum-free subfamily of size at least \(m^2/(4T_{\mathcal M})\). This size is at most \(A_{p,k}(n)\), yielding (12). ∎

If \(\tau\ge\varepsilon N\), take a maximal vertex-disjoint family of cycles of size \(m\). Its \(km\) vertices form a cycle cover, so
\[
m\ge\frac{\varepsilon N}{k}.
\]
Since \(T\ge T_{\mathcal M}\), (12) gives the unconditional dimension-dependent bound
\[
\boxed{
T\ge
\frac{\varepsilon^2}{4k^3}N^{1+c_{p,k}}.
}
\tag{13}
\]

This is genuine supersaturation, but it is not an arithmetic removal bound because after normalization it reads
\[
\frac{T}{N^{k-1}}
\ge
\frac{\varepsilon^2}{4k^3}
N^{-(k-2-c_{p,k})},
\]
which still deteriorates with \(n\).

## 5. Exact lower-endpoint exponent for sparse cycle systems

The extraction lemma does give an exact special case for every \(p,k\).

Let \(\nu\) be the maximum number of vertex-disjoint cycles. Fix \(L\ge1\), and consider systems satisfying
\[
T\le L\nu.
\tag{14}
\]

### Proposition
For systems satisfying (14),
\[
\tau\ge\varepsilon N
\quad\Longrightarrow\quad
T\ge
\frac{1}{k(4k^2L)^{(k-2)/c_{p,k}}}
\varepsilon^{\,1+(k-2)/c_{p,k}}N^{k-1}.
\tag{15}
\]
Consequently, for every fixed \(L\), the optimal exponent in this sparse class is exactly
\[
1+\frac{k-2}{c_{p,k}}.
\]

### Proof

Take a maximum matching \(\mathcal M\) of size \(m=\nu\). Then
\[
m\ge\frac{\tau}{k}\ge\frac{\varepsilon N}{k}.
\tag{16}
\]
Moreover \(T_{\mathcal M}\le T\le Lm\). By (12),
\[
\frac{m^2}{4kN^{1-c_{p,k}}}
\le T_{\mathcal M}\le Lm,
\]
and hence
\[
m\le4kL N^{1-c_{p,k}}.
\]
Together with (16), this gives
\[
N^{c_{p,k}}\le\frac{4k^2L}{\varepsilon}.
\tag{17}
\]
Finally,
\[
T\ge m\ge\frac{\varepsilon N}{k}
 =
\frac{\varepsilon}{kN^{k-2}}N^{k-1}.
\]
Using (17),
\[
N^{k-2}
\le
\left(\frac{4k^2L}{\varepsilon}\right)^{(k-2)/c_{p,k}},
\]
which yields (15).

Sharpness follows from the multicolored sum-free examples: there \(T=\nu=m\), so (14) holds already with \(L=1\), and the calculation in Section 3 rules out every smaller exponent. ∎

Thus any construction forcing
\[
C^*_{p,k}>1+\frac{k-2}{c_{p,k}}
\]
must have \(T/\nu\to\infty\); isolated or boundedly clustered cycles cannot do it.

## 6. Why this does not settle \(k>3\)

A maximal matching of cycles need not itself be multicolored sum-free. For example, over \(\mathbb F_2\) with \(k=4\), take a nonzero \(v\) and the two disjoint cycles
\[
(0,0,0,0),\qquad (v,v,v,v).
\]
The mixed tuple
\[
(v,v,0,0)
\]
is also a cycle. In fact, all choices having an even number of \(v\)'s are cycles.

The extraction lemma controls such mixed cycles only by discarding indices. In the unrestricted high-dimensional regime, this loses too much: (13) has scale \(N^{1+c_{p,k}}\), whereas the desired lower-endpoint removal estimate would have scale \(N^{k-1}\):
\[
T\stackrel{?}{\gtrsim}
\varepsilon^{\,1+(k-2)/c_{p,k}}N^{k-1}.
\tag{18}
\]
The two scales meet around \(N\asymp\varepsilon^{-1/c_{p,k}}\), but for substantially larger \(N\), (13) is weaker.

The source proof handles the necessary multiscale structure using a tri-colored sum-free input, which is why its denominator is \(c_{p,3}\). The argument above does not provide a way to replace that input by \(c_{p,k}\) when the matching vertices support an unbounded number of off-diagonal cycles.

Hence the unrestricted result remains
\[
1+\frac{k-2}{c_{p,k}}
\le C^*_{p,k}
\le
1+\frac{k-2}{c_{p,3}},
\]
with equality proved here only for \(k=3\) and for the sparse class \(T=O(\nu)\).