```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For \(r=1\), a Ramsey-theoretic construction gives \(h(n,k,W_3)=\Omega(n^2/(k^{3/2}(\log k)^2))\), within a factor \((\log k)^2\) of the conjectured bound.",
  "would_publish": false,
  "caveats": "No constant-factor matching bound is obtained; the argument does not extend directly to \(r>1\), and the lower bound requires \(n\) sufficiently large in terms of \(k\)."
}
```

# 1. Statement and interpretation

Write
\[
d_k(G):=\min_{\phi:V(G)\to[k]}
 \bigl|\{uv\in E(G):\phi(u)=\phi(v)\}\bigr|,
\]
so that
\[
h(n,k,H)=\max\{d_k(G): |V(G)|=n,\ H\nsubseteq G\}.
\]

I use the convention
\[
W_{2r+1}=K_1\vee C_{2r+1};
\]
in particular, \(W_3=K_4\).

The intended conjecture is that, for fixed \(r\), there is \(c_r>0\) such that, for every \(k\) and all sufficiently large \(n=n(k,r)\),
\[
h(n,k,W_{2r+1})
 \ge c_r\frac{n^2}{k^{\,2-1/(r+1)}}.
\]
Together with the source paper's upper bound, this would determine the order of magnitude.

The qualification on \(n\) is necessary. A lower bound of this form cannot hold uniformly for all \(n\ge k\): when \(k=n\), every \(n\)-vertex graph is already \(k\)-colorable and hence \(h(n,n,H)=0\).

# 2. Two elementary lemmas

## Lemma 2.1: Independence number forces monochromatic edges

If \(F\) has \(N\) vertices and independence number \(a=\alpha(F)\), then
\[
d_k(F)\ge \frac{N^2}{2ak}-\frac N2.
\]
In particular, if \(N\ge 2ak\), then
\[
d_k(F)\ge \frac N2.
\]

### Proof

Let \(V(F)=V_1\cup\cdots\cup V_k\) be any \(k\)-coloring, not necessarily proper, and put \(s_i=|V_i|\). Since \(\overline{F[V_i]}\) has clique number at most \(a\), Turán's theorem gives
\[
e(\overline{F[V_i]})
 \le \frac12\left(1-\frac1a\right)s_i^2.
\]
Consequently,
\[
e(F[V_i])
\ge \binom{s_i}{2}
   -\frac12\left(1-\frac1a\right)s_i^2
=\frac{s_i^2}{2a}-\frac{s_i}{2}.
\]
Summing and using \(\sum_i s_i^2\ge N^2/k\),
\[
\sum_i e(F[V_i])
\ge \frac{N^2}{2ak}-\frac N2.
\]
Taking the minimum over all colorings proves the claim. ∎

## Lemma 2.2: Balanced blow-ups preserve \(d_k\)

Let \(F(t)\) be the balanced independent blow-up of \(F\): every vertex \(v\) is replaced by an independent set of size \(t\), and every edge of \(F\) is replaced by a complete bipartite graph. Then
\[
d_k(F(t))=t^2d_k(F).
\]

### Proof

The upper bound follows by coloring each cluster monochromatically according to an optimal coloring of \(F\).

For the reverse bound, let \(p_{v,c}\) be the proportion of the cluster replacing \(v\) receiving color \(c\). The number of monochromatic edges, divided by \(t^2\), is
\[
Q=\sum_{uv\in E(F)}\sum_{c=1}^k p_{u,c}p_{v,c}.
\]
Independently color each base vertex \(v\) with distribution \((p_{v,1},\dots,p_{v,k})\). The expected number of monochromatic edges of \(F\) is exactly \(Q\). Every deterministic coloring has at least \(d_k(F)\) monochromatic edges, so \(Q\ge d_k(F)\). ∎

For \(F=K_4\)-free, every independent blow-up is again \(K_4\)-free: a \(K_4\) in the blow-up would project to four distinct pairwise adjacent vertices of \(F\).

# 3. A polylogarithmic approximation for \(r=1\)

We use the established off-diagonal Ramsey estimate
\[
R(4,t)=\Omega\!\left(\frac{t^3}{(\log t)^4}\right),
\]
proved by Mattheus and Verstraëte in *The asymptotics of \(r(4,t)\)*. Thus, for all sufficiently large \(t\), there is a \(K_4\)-free graph \(F\) on
\[
N\ge c_0\frac{t^3}{(\log t)^4}
\]
vertices with \(\alpha(F)<t\). We may take \(N\) of this order.

Choose
\[
t=\left\lceil A\sqrt{k}\,(\log k)^2\right\rceil,
\]
where \(A\) is a sufficiently large absolute constant. Since
\[
\log t=(1/2+o(1))\log k,
\]
the Ramsey construction gives
\[
N=\Theta\!\left(k^{3/2}(\log k)^2\right),
\]
and, after increasing \(A\),
\[
N\ge 2k(t-1)>2k\alpha(F).
\]
Lemma 2.1 therefore gives
\[
d_k(F)\ge \frac N2.
\]

Now take a balanced \(q\)-fold blow-up \(F(q)\). It remains \(K_4\)-free, and Lemma 2.2 gives
\[
d_k(F(q))\ge \frac{q^2N}{2}
          =\frac{|V(F(q))|^2}{2N}.
\]

For an arbitrary \(n\ge 2N\), take \(q=\lfloor n/N\rfloor\), use \(F(q)\), and add isolated vertices. The nonisolated part has at least \(n/2\) vertices. Hence
\[
h(n,k,K_4)
 \ge \frac{n^2}{8N}
 \ge c\,\frac{n^2}{k^{3/2}(\log k)^2}.
\]

We have therefore proved:

> **Proposition.** There are absolute constants \(c,C>0\) such that, for all sufficiently large \(k\) and all
> \[
> n\ge Ck^{3/2}(\log k)^2,
> \]
> \[
> h(n,k,W_3)=h(n,k,K_4)
> \ge c\,\frac{n^2}{k^{3/2}(\log k)^2}.
> \]

The conjectured lower bound for \(r=1\) is \(cn^2/k^{3/2}\), so this leaves only a factor \((\log k)^2\).

This Ramsey argument alone cannot remove the logarithm. Indeed, the standard upper bound
\[
R(4,t)=O\!\left(\frac{t^3}{(\log t)^2}\right)
\]
precludes a \(K_4\)-free graph of order \(O(k^{3/2})\) with independence number at most \(N/(2k)\). A constant-factor proof must therefore exploit a quantitatively robust obstruction to \(k\)-colorability, not merely a small independence number.

# 4. Why the same blow-up argument is delicate for longer wheels

For noncomplete forbidden graphs, blow-ups need not preserve freeness. The relevant obstruction can be described exactly.

Let \(\ell=2r+1\). If \(F(t)\) contains \(W_\ell\), projection onto the base graph sends the hub to some \(v\in V(F)\), while the rim projects to a closed walk of length \(\ell\) in \(F[N_F(v)]\). Thus a sufficient condition for every blow-up of \(F\) to be \(W_\ell\)-free is
\[
\operatorname{odd\,girth}(F[N_F(v)])>\ell
\qquad\text{for every }v\in V(F).
\]
Conversely, for \(t\ge \ell\), any closed walk of length \(\ell\) in a neighborhood can be lifted using distinct clones to a copy of \(W_\ell\). Since a closed odd walk of length \(\ell\) exists exactly when there is an odd cycle of length at most \(\ell\), this is the natural blow-up condition.

Consequently, the following finite construction would imply the conjectured lower bound.

> **Conditional finite criterion.** Suppose that for every sufficiently large \(k\) there is a graph \(F\) on
> \[
> N=O_r\!\left(k^{\,2-1/(r+1)}\right)
> \]
> vertices such that
> \[
> \alpha(F)\le \frac{N}{2k}
> \]
> and every neighborhood of \(F\) has odd girth greater than \(2r+1\). Then, for all sufficiently large \(n\),
> \[
> h(n,k,W_{2r+1})
> =\Omega_r\!\left(\frac{n^2}
> {k^{\,2-1/(r+1)}}\right).
> \]

The proof is exactly Lemmas 2.1 and 2.2 followed by the neighborhood odd-girth observation.

For \(r=1\), the neighborhood condition is equivalent to \(K_4\)-freeness, which is why the Ramsey construction applies. For \(r>1\), an arbitrary \(W_{2r+1}\)-free graph need not satisfy this stronger homomorphism-free condition, and its blow-up may create a wheel. Thus the \(r=1\) argument does not automatically extend.

# 5. Known baseline and remaining gap

Because \(W_{2r+1}\) contains its rim \(C_{2r+1}\),
\[
h(n,k,W_{2r+1})\ge h(n,k,C_{2r+1}).
\]
The odd-cycle lower bound from the source paper consequently gives, in its asymptotic range,
\[
h(n,k,W_{2r+1})
 =\Omega_r\!\left(\frac{n^2}{k^2}\right).
\]
The conjectured exponent improves this to
\[
2-\frac1{r+1}.
\]

The result above improves the \(k^{-2}\) baseline substantially for \(r=1\), reaching the conjectured power of \(k\) with only a logarithmic loss. I do not obtain a corresponding improvement for \(r\ge2\), nor a way to remove the logarithm for \(r=1\). Hence the conjecture remains unresolved.