```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "An exact phase-integral formula derived from the matching-polynomial decomposition of the characteristic polynomial determines the sign of s+(G)-s-(G).",
  "would_publish": true,
  "caveats": "This uses the standard convention that a unicyclic graph is connected; publication priority was not independently checked."
}
```

# Theorem

Let \(G\) be a connected simple unicyclic graph of order \(n\), and let its unique cycle \(C\) have odd length \(k\). Then

\[
\begin{cases}
s^+(G)>n>s^-(G),&k\equiv 3\pmod 4,\\[2mm]
s^+(G)<n<s^-(G),&k\equiv 1\pmod 4.
\end{cases}
\]

In fact, there is an explicit integral formula whose integrand has a fixed sign.

## 1. Matching-polynomial decomposition

For a graph \(H\) of order \(h\), let \(m_j(H)\) denote its number of \(j\)-edge matchings and write

\[
\mu_H(x)=\sum_{j\geq 0}(-1)^j m_j(H)x^{h-2j}.
\]

Let

\[
F=G-V(C).
\]

We claim that the adjacency characteristic polynomial \(p_G(x)=\det(xI-A(G))\) satisfies

\[
p_G(x)=\mu_G(x)-2\mu_F(x). \tag{1}
\]

Indeed, in the determinant expansion, terms having no permutation cycle of length at least three correspond precisely to matchings of \(G\), and their sum is \(\mu_G(x)\). Since \(G\) has a unique cycle, every remaining nonzero term contains the whole cycle \(C\), in one of its two orientations, together with a matching in \(F\).

If such a matching has \(j\) edges, each orientation contributes
\[
-(-1)^j x^{|V(F)|-2j}.
\]
The two orientations therefore contribute
\[
-2(-1)^j x^{|V(F)|-2j}.
\]
Summing over all matchings in \(F\) proves (1).

For a graph \(H\) of order \(h\), define the positive-coefficient polynomial

\[
M_H(t)=\sum_{j\geq 0}m_j(H)t^{h-2j}.
\]

For every \(t>0\),

\[
\mu_H(it)=i^h M_H(t), \tag{2}
\]
because
\[
(-1)^j(it)^{h-2j}=i^h t^{h-2j}.
\]

Combining (1) and (2), and recalling that \(|V(F)|=n-k\), gives

\[
i^{-n}p_G(it)
  =M_G(t)-2i^{-k}M_F(t).
\]

Set

\[
\eta=(-1)^{(k-1)/2}.
\]

For odd \(k\), one has \(i^{-k}=-\eta i\), and hence

\[
i^{-n}p_G(it)=M_G(t)+2\eta i\,M_F(t). \tag{3}
\]

Both \(M_G(t)\) and \(M_F(t)\) are strictly positive for \(t>0\). Consequently the continuous argument of the right-hand side of (3), chosen to tend to zero as \(t\to\infty\), is

\[
\phi(t)
 =\eta\arctan\!\left(\frac{2M_F(t)}{M_G(t)}\right). \tag{4}
\]

## 2. A phase formula for the square-energy imbalance

Let the adjacency eigenvalues be \(\lambda_1,\dots,\lambda_n\), and put

\[
D(G)=s^+(G)-s^-(G)
     =\sum_{j=1}^n \operatorname{sgn}(\lambda_j)\lambda_j^2.
\]

For every real \(\lambda\),

\[
\operatorname{sgn}(\lambda)\lambda^2
 =\frac{2}{\pi}\int_0^\infty
       \frac{\lambda^3}{\lambda^2+t^2}\,dt,
\]
with both sides zero when \(\lambda=0\). Thus

\[
D(G)=\frac{2}{\pi}\int_0^\infty
       \sum_{j=1}^n\frac{\lambda_j^3}{\lambda_j^2+t^2}\,dt. \tag{5}
\]

Since \(A(G)\) has zero diagonal,

\[
\sum_j\lambda_j=\operatorname{tr}A(G)=0.
\]

Therefore

\[
\sum_j\frac{\lambda_j^3}{\lambda_j^2+t^2}
 =-t^2\sum_j\frac{\lambda_j}{\lambda_j^2+t^2}. \tag{6}
\]

On the other hand, from \(p_G(it)=\prod_j(it-\lambda_j)\),

\[
\begin{aligned}
\phi'(t)
 &=\frac{d}{dt}\arg\!\big(i^{-n}p_G(it)\big)\\
 &=\operatorname{Im}\sum_j\frac{i}{it-\lambda_j}\\
 &=-\sum_j\frac{\lambda_j}{\lambda_j^2+t^2}.
\end{aligned}
\]

Equations (5) and (6) now give

\[
D(G)=\frac{2}{\pi}\int_0^\infty t^2\phi'(t)\,dt. \tag{7}
\]

Integration by parts is legitimate. Indeed, \(\phi(t)\) is bounded near zero, while

\[
\frac{M_F(t)}{M_G(t)}=O(t^{-k})
\qquad (t\to\infty),
\]
so \(\phi(t)=O(t^{-k})\). Since \(k\geq 3\),

\[
\lim_{t\to0}t^2\phi(t)
 =\lim_{t\to\infty}t^2\phi(t)=0,
\]
and \(\int_0^\infty t|\phi(t)|\,dt\) converges. Hence (7) and (4) yield the exact identity

\[
\boxed{
D(G)
 =-\frac{4\eta}{\pi}
   \int_0^\infty
   t\arctan\!\left(\frac{2M_F(t)}{M_G(t)}\right)\,dt
}. \tag{8}
\]

The integral in (8) is strictly positive.

## 3. Determination of the sign

If \(k\equiv3\pmod4\), then \(\eta=-1\), so (8) gives

\[
s^+(G)-s^-(G)>0.
\]

If \(k\equiv1\pmod4\), then \(\eta=1\), so

\[
s^+(G)-s^-(G)<0.
\]

Finally, because a connected unicyclic graph has \(|E(G)|=n\),

\[
s^+(G)+s^-(G)
 =\sum_j\lambda_j^2
 =\operatorname{tr}A(G)^2
 =2|E(G)|=2n.
\]

Thus

\[
s^+(G)=n+\frac{D(G)}2,\qquad
s^-(G)=n-\frac{D(G)}2,
\]
which proves exactly the two asserted strict chains of inequalities.

## Scope and gaps

No mathematical cases remain under the standard definition that “unicyclic” means connected with exactly one cycle. If disconnected graphs having exactly one cyclic component were allowed, the statement would be false as written; for example, \(C_3\cup K_1\) has \(s^+=4=n\). Literature priority for the integral argument has not been independently verified.