```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The universal conjecture is false: for H = 2K2 there are x_n with Pr(X_H = x_n) = Omega(n^{-5/2}), whereas Var(X_H) = Theta(n^6), so the conjecture would require O(n^{-3}).",
  "would_publish": false,
  "caveats": "The counterexample below is self-contained for ordinary non-induced subgraph counts; the positive connected case is cited rather than reproved."
}
```

# Mathematical writeup

## 1. Statement and conclusion

The anti-concentration assertion is understood uniformly in \(x\), namely as
\[
\sup_{x\in\mathbb N}\Pr(X_H=x)
 =O_{H,p}\!\left(\frac1{\sqrt{\operatorname{Var}(X_H)}}\right).
\]
This is the only meaningful interpretation when \(x\) may vary with \(n\).

The conjecture is false for the disconnected graph
\[
H=2K_2,
\]
which has \(h=4\) non-isolated vertices.

### Proposition

For every fixed \(p\in(0,1)\), if \(X=X_{2K_2}\) in \(G(n,p)\), then
\[
\operatorname{Var}(X)=\Theta_p(n^6),
\]
but for every sufficiently large \(n\) there is an integer \(x_n\) such that
\[
\Pr(X=x_n)\ge c_p n^{-5/2}.
\]
Consequently,
\[
\Pr(X=x_n)\sqrt{\operatorname{Var}(X)}
   =\Omega_p(n^{1/2})\longrightarrow\infty,
\]
contradicting the conjectured \(O(n^{-3})\) bound.

Here copies are unlabelled, non-induced copies. For labelled embeddings the count is multiplied by \(|\operatorname{Aut}(2K_2)|=8\), which does not affect the argument.

---

## 2. The basic identity

Let
\[
M=e(G)
\]
and let \(W\) be the number of unordered pairs of incident edges of \(G\), equivalently the number of wedges.

Every unordered pair of distinct edges is either incident or vertex-disjoint. Hence
\[
X=\binom{M}{2}-W. \tag{1}
\]

The obstruction is that, after conditioning on \(M\), the first term in (1) is fixed and the remaining statistic \(W\) fluctuates on a much smaller scale.

---

## 3. Conditional fluctuations of the wedge count

Write
\[
N=\binom n2,
\qquad
D=2(n-2).
\]
Thus \(N\) is the number of possible edges, and every edge of \(K_n\) is incident to exactly \(D\) other possible edges.

Let \(\mathcal W\) be the collection of wedges in \(K_n\). Its size is
\[
Q=|\mathcal W|=\frac{ND}{2}=N(n-2).
\]

Condition on \(M=m\). The edge set is then a uniformly random \(m\)-subset of the \(N\) possible edges. Put
\[
\pi_k=\frac{(m)_k}{(N)_k},
\]
the probability that any fixed \(k\) distinct possible edges are all selected.

For \(\alpha\in\mathcal W\), let \(I_\alpha\) indicate that both edges of \(\alpha\) are selected. Then
\[
W=\sum_{\alpha\in\mathcal W}I_\alpha.
\]

Two distinct wedges can share one possible edge or have four distinct possible edges. The number of unordered pairs of wedges sharing one edge is
\[
R=N\binom D2.
\]
Therefore
\[
\mathbb E(W\mid M=m)=Q\pi_2
\]
and
\[
\mathbb E(W^2\mid M=m)
 =Q\pi_2+2R\pi_3
  +2\left(\binom Q2-R\right)\pi_4.
\]
Consequently,
\[
\operatorname{Var}(W\mid M=m)
 =Q(\pi_2-\pi_4)
  +2R(\pi_3-\pi_4)
  +Q^2(\pi_4-\pi_2^2). \tag{2}
\]

Let \(q=m/N\), where \(q\) remains in a fixed compact subinterval of \((0,1)\). For each fixed \(k\le4\),
\[
\pi_k
 =q^k-\binom{k}{2}\frac{q^{k-1}(1-q)}{N}
  +O_p(N^{-2}).
\]
In particular, with \(a=q^3(1-q)\),
\[
\begin{aligned}
\pi_2-\pi_4&=q^2-q^4+O_p(N^{-1}),\\
\pi_3-\pi_4&=a+O_p(N^{-1}),\\
\pi_4-\pi_2^2&=-\frac{4a}{N}+O_p(N^{-2}).
\end{aligned}
\]
Substitution into (2), using \(2R=ND(D-1)\) and \(Q=ND/2\), gives
\[
\begin{aligned}
\operatorname{Var}(W\mid M=m)
&=\frac{ND}{2}(q^2-q^4)
  +ND(D-1)a-ND^2a+O_p(D^2+D)\\
&=\frac{ND}{2}q^2(1-q)^2+O_p(D^2+D)\\
&=\Theta_p(n^3). \tag{3}
\end{aligned}
\]
Only the upper bound \(O_p(n^3)\) is needed below.

---

## 4. A point with probability \(\Omega(n^{-5/2})\)

Choose \(m=m_n\) to be an integer nearest to \(pN\). Stirling’s formula gives
\[
\Pr(M=m)=\Theta_p(N^{-1/2})=\Theta_p(n^{-1}). \tag{4}
\]

By (3) and Chebyshev’s inequality, for a sufficiently large constant \(L=L(p)\),
\[
\Pr\!\left(
 |W-\mathbb E(W\mid M=m)|\le L n^{3/2}
 \,\middle|\,M=m
\right)\ge \frac34.
\]
The interval in question contains only \(O_p(n^{3/2})\) integers. Hence, by pigeonhole, there is an integer \(w_n\) such that
\[
\Pr(W=w_n\mid M=m)\ge c_p n^{-3/2}. \tag{5}
\]

Define
\[
x_n=\binom m2-w_n.
\]
Because \(w_n\) is in the conditional support, \(x_n\) is a valid nonnegative integer; indeed it is positive for large \(n\). From (1), (4), and (5),
\[
\begin{aligned}
\Pr(X=x_n)
&\ge \Pr(M=m,W=w_n)\\
&=\Pr(M=m)\Pr(W=w_n\mid M=m)\\
&\ge c'_p n^{-1}n^{-3/2}
 =c'_p n^{-5/2}. \tag{6}
\end{aligned}
\]

---

## 5. Verification of the variance scale

It remains to check that the conjectured Gaussian scale really is \(n^{-3}\).

Set
\[
A=\binom M2,
\]
so that \(X=A-W\). If \(Z_e\) is the indicator of a possible edge \(e\), then
\[
A=\sum_{\{e,f\}\in\binom{E(K_n)}2}Z_eZ_f.
\]
Two distinct summands are independent unless their two-edge index sets share one possible edge. There are
\[
N\binom{N-1}{2}=\Theta(N^3)
\]
unordered pairs of summands sharing one edge, and each such covariance equals
\[
p^3-p^4=p^3(1-p)>0.
\]
Thus
\[
\operatorname{Var}(A)=\Theta_p(N^3)=\Theta_p(n^6). \tag{7}
\]

For \(W\), the same dependency count gives
\[
\operatorname{Var}(W)
 =Qp^2(1-p^2)+2Rp^3(1-p)
 =O_p(n^4). \tag{8}
\]
Applying the triangle and reverse triangle inequalities in \(L^2\) to centered variables,
\[
\sqrt{\operatorname{Var}(A)}-\sqrt{\operatorname{Var}(W)}
 \le \sqrt{\operatorname{Var}(X)}
 \le \sqrt{\operatorname{Var}(A)}+\sqrt{\operatorname{Var}(W)}.
\]
Equations (7)–(8) yield
\[
\sqrt{\operatorname{Var}(X)}=\Theta_p(n^3),
\qquad
\operatorname{Var}(X)=\Theta_p(n^6). \tag{9}
\]

Combining (6) and (9),
\[
\Pr(X=x_n)=\Omega_p(n^{-5/2})
\not=O_p(n^{-3})
=O_p\!\left(\frac1{\sqrt{\operatorname{Var}(X)}}\right).
\]
This completes the disproof.

---

## 6. Status of the connected case and limitations

The supplied bibliographic record reports that Sah and Sawhney, *Local limit theorems for subgraph counts* (JLMS, 2022; arXiv:2006.11369), proved the optimal local central limit theorem for connected \(H\). Thus the conjectured estimate is valid for connected graphs but false under the original quantification over all graphs.

The argument above does not classify which disconnected graphs satisfy the estimate. It only gives a complete, explicit counterexample to the conjecture as stated.