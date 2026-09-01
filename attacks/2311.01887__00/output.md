```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with r(G_n)=(1+o(1))f(n) whenever log(f(n)/n)=o(sqrt(n)), and uniformly throughout that range.",
  "would_publish": false,
  "caveats": "The exponential-scale regime remains open; the construction uses isolated vertices, as allowed by the stated problem."
}
```

## 1. Statement and partial result

Write \(r(H)\) for the diagonal two-colour Ramsey number of \(H\), with copies understood to be non-induced.

The full conjecture is not resolved here. The following establishes multiplicative \(1+o(1)\)-density over a substantial initial segment of the Ramsey spectrum.

### Theorem

Let \(L_n\ge 0\) satisfy \(L_n=o(\sqrt n)\). Uniformly for every integer
\[
n\le y\le n e^{L_n},
\]
there is an \(n\)-vertex graph \(G=G(n,y)\) such that
\[
\frac{r(G)}{y}=1+O\!\left(
\sqrt{\frac{(L_n+1)(L_n+\log n+1)}{n}}
\right).
\]
In particular, if
\[
n\le f(n)\le r(K_n)
\qquad\text{and}\qquad
\log\frac{f(n)}n=o(\sqrt n),
\]
then there are \(n\)-vertex graphs \(G_n\) satisfying
\[
r(G_n)=(1+o(1))f(n).
\]
Thus Conjecture 10 holds for all polynomially bounded \(f\), and more generally for all
\[
f(n)=n\exp(o(\sqrt n)).
\]

The proof uses complete bipartite graphs with one relatively small part.

---

## 2. Two elementary lemmas

### Lemma 1: Padding by isolated vertices

If \(F\) has \(h\le n\) vertices and
\[
F^{[n]}=F\mathbin{\dot\cup}(n-h)K_1,
\]
then
\[
r(F^{[n]})=\max\{n,r(F)\}.
\]

#### Proof

The lower bound follows because \(F^{[n]}\) has \(n\) vertices and contains \(F\).

Conversely, let \(N=\max\{n,r(F)\}\). Every colouring of \(K_N\) contains a monochromatic copy of \(F\). Since \(N\ge n\), one can add \(n-h\) unused vertices to this copy; their incident edges are irrelevant because the added vertices are isolated in \(F^{[n]}\). Hence \(r(F^{[n]})\le N\). ∎

### Lemma 2: An asymptotic Ramsey number for \(K_{s,t}\)

Let \(s,t\ge1\), and put
\[
M=2^s t,\qquad h=s\log(eM),\qquad
\delta=4\sqrt{\frac ht}.
\]
Whenever \(\delta\le \tfrac12\),
\[
(1-\delta)M<r(K_{s,t})\le M+4s^2. \tag{1}
\]

Consequently, if \(t\to\infty\) and
\[
s\log(2^s t)=o(t), \tag{2}
\]
then
\[
r(K_{s,t})=(1+o(1))\,2^s t. \tag{3}
\]

#### Lower bound in Lemma 2

Set
\[
N=\left\lfloor(1-\delta)M\right\rfloor
\]
and colour \(E(K_N)\) independently red or blue with probability \(1/2\).

For an \(s\)-set \(S\) and a colour \(c\), let \(X_c(S)\) be the number of common \(c\)-neighbours of all vertices of \(S\). Then
\[
X_c(S)\sim \operatorname{Bin}(N-s,2^{-s})
\]
and its mean satisfies
\[
\mu\le N2^{-s}\le(1-\delta)t.
\]
A standard additive Chernoff bound gives
\[
\Pr(X_c(S)\ge t)
 \le \exp\left(-\frac{\delta^2t}{2}\right).
\]
There are at most
\[
2\binom Ns\le 2(eM)^s=2e^h
\]
choices of \((S,c)\). Hence the probability that some \(S\) has at least \(t\) common neighbours in one colour is at most
\[
2\exp\left(h-\frac{\delta^2t}{2}\right)
 =2e^{-7h}<1,
\]
because \(\delta^2t=16h\).

Thus there is a colouring of \(K_N\) without a monochromatic \(K_{s,t}\), proving
\[
r(K_{s,t})\ge N+1>(1-\delta)M.
\]

#### Upper bound in Lemma 2

Let
\[
N=M+4s^2
\]
and consider an arbitrary red-blue colouring of \(K_N\). For a vertex \(v\), write \(d_R(v)\) and \(d_B(v)\) for its red and blue degrees. Since
\[
d_R(v)+d_B(v)=N-1,
\]
discrete convexity of \(x\mapsto\binom xs\) gives
\[
\binom{d_R(v)}s+\binom{d_B(v)}s
 \ge 2\binom ms,
\qquad
m=\left\lfloor\frac{N-1}{2}\right\rfloor .
\]

For an \(s\)-set \(S\), let \(d_R(S)\) and \(d_B(S)\) denote its numbers of common red and blue neighbours. Double-counting pairs \((S,v)\) gives
\[
\sum_{S\in\binom{V}{s}}\bigl(d_R(S)+d_B(S)\bigr)
 \ge 2N\binom ms.
\]
Therefore some \(S\) satisfies
\[
\max\{d_R(S),d_B(S)\}
 \ge N\frac{\binom ms}{\binom Ns}. \tag{4}
\]

For \(0\le i<s\),
\[
\frac{m-i}{N-i}
 \ge \frac12\left(1-\frac{i+2}{N-i}\right).
\]
Since \(N>4s^2\),
\[
\frac{\binom ms}{\binom Ns}
 \ge 2^{-s}\prod_{i=0}^{s-1}
 \left(1-\frac{i+2}{N-i}\right)
 \ge 2^{-s}\left(1-\frac{4s^2}{N}\right).
\]
Substituting in (4),
\[
\max\{d_R(S),d_B(S)\}
 \ge \frac{N-4s^2}{2^s}
 =\frac M{2^s}=t.
\]
Thus \(S\), together with \(t\) common neighbours in the relevant colour, gives a monochromatic \(K_{s,t}\). This proves the upper bound in (1).

Finally, condition (2) makes \(\delta=o(1)\). It also implies \(s^2=o(t)\), since
\[
s\log(2^s t)\ge (\log 2)s^2.
\]
Thus \(4s^2/M=o(1)\), and (3) follows. ∎

---

## 3. Construction for prescribed \(y\)

Fix \(n\) and an integer \(y\) satisfying
\[
n\le y\le ne^{L_n}.
\]
Define
\[
k=\left\lceil\log_2\frac yn\right\rceil,
\qquad s=k+1,
\qquad
t=\left\lfloor\frac{y}{2^s}\right\rfloor.
\]
Because
\[
2^{k-1}<\frac yn\le2^k,
\]
we have
\[
\frac n4<\frac{y}{2^s}\le\frac n2.
\]
Consequently,
\[
\frac n4-1\le t\le\frac n2.
\]
Moreover,
\[
s=O(L_n+1)=o(\sqrt n),
\]
so \(s+t\le n\) for all sufficiently large \(n\).

Put
\[
F=K_{s,t},\qquad M=2^s t.
\]
Rounding \(t\) down gives
\[
0\le y-M<2^s,
\]
and since \(y/2^s>n/4\),
\[
1-\frac4n<\frac My\le1. \tag{5}
\]

Also,
\[
s\log(eM)
 \le C(L_n+1)(L_n+\log n+1).
\]
Since \(t\ge n/5\) for large \(n\), Lemma 2 gives
\[
r(F)=(1+O(\rho_n))M,
\]
where
\[
\rho_n=
\sqrt{\frac{(L_n+1)(L_n+\log n+1)}n}.
\]
The hypothesis \(L_n=o(\sqrt n)\) implies \(\rho_n=o(1)\).

More explicitly, the upper part of Lemma 2 and (5) give
\[
\frac{r(F)}y
 \le 1+\frac{4s^2}{y}
 \le1+O(\rho_n),
\]
while the random-colouring lower bound gives
\[
\frac{r(F)}y\ge1-O(\rho_n).
\]

Finally, set
\[
G=F\mathbin{\dot\cup}(n-s-t)K_1.
\]
By Lemma 1,
\[
r(G)=\max\{n,r(F)\}.
\]
Since \(n/y\le1\), taking this maximum does not spoil either estimate, and hence
\[
\frac{r(G)}y=1+O(\rho_n).
\]
This proves the theorem.

Taking \(y=f(n)\) and \(L_n=\log(f(n)/n)=o(\sqrt n)\) yields
\[
r(G_n)=(1+o(1))f(n),
\]
which is stronger than the fixed-\(\varepsilon\) conclusion in this range.

---

## 4. Why this does not settle the full conjecture

The construction takes
\[
s\asymp \log\frac yn,\qquad t\asymp n.
\]
The matching random-colouring lower bound for \(K_{s,t}\) requires
\[
s\log(2^st)=o(t).
\]
Its dominant restriction is \(s^2=o(n)\), exactly leading to
\[
\log(y/n)=o(\sqrt n).
\]
When \(\log(y/n)\) is of order \(\sqrt n\) or larger, the union bound no longer gives a \(1-o(1)\) estimate. This is a limitation of the argument, not evidence against the conjecture.

There is also a sharp obstruction at the top of the spectrum. Every noncomplete \(n\)-vertex graph is a subgraph of \(K_n-e\), so
\[
\max\{r(G):|V(G)|=n,\ G\ne K_n\}=r(K_n-e).
\]
Therefore the full conjecture necessarily implies
\[
\frac{r(K_n-e)}{r(K_n)}\longrightarrow1. \tag{6}
\]
No proof of (6) is supplied here.

More generally, list the distinct elements of the \(n\)-vertex Ramsey spectrum as
\[
n=a_{n,0}<a_{n,1}<\cdots<a_{n,m_n}=r(K_n).
\]
The conjecture is equivalent to
\[
\max_i\frac{a_{n,i+1}}{a_{n,i}}\longrightarrow1.
\]
Indeed, if the ratios tend to \(1\), choose the first spectrum value at least \(f(n)\). Conversely, a fixed multiplicative gap on infinitely many \(n\) gives a counterexample function by choosing an integer near the geometric mean of the two endpoints.

A sufficient, but presently unproved, edge-stability statement would be
\[
\sup_{\substack{|V(H)|=n\\e\notin E(H)}}
\frac{r(H+e)}{r(H)}=1+o(1).
\]
Adding the edges of \(K_n\) one at a time would then produce a chain whose Ramsey values have no substantial multiplicative jump. The bipartite argument above does not establish such stability for graphs with exponential Ramsey number, which is the remaining gap.