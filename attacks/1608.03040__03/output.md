```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every tournament of minimum out-degree at least 47 has a majority 3-colouring, and every tournament has a 3-colouring with at most four violating vertices.",
  "would_publish": false,
  "caveats": "Tournaments with minimum out-degree at most 46 remain, and there is no general way to repair the four exceptional vertices."
}
```

## 1. Statement and conventions

For a colouring \(\phi:V(T)\to\{1,2,3\}\), put
\[
m_\phi(v)=|\{u\in N^+(v):\phi(u)=\phi(v)\}|.
\]
The colouring is a majority colouring if
\[
m_\phi(v)\le \frac{d^+(v)}2
\]
for every \(v\), equivalently \(m_\phi(v)\le\lfloor d^+(v)/2\rfloor\).

The conjecture is not resolved here. I prove the following partial results.

### Theorem 1

Let \(T\) be a tournament.

1. If \(\delta^+(T)\ge 47\), then \(T\) has a majority \(3\)-colouring. In fact, it has one in which every colour class has size at most \(|V(T)|/2\).
2. Every tournament has a \(3\)-colouring for which at most four vertices violate the majority condition.

The constant \(47\) is only what the estimates below certify and is not claimed to be optimal.

---

## 2. The random-colouring reduction

Colour the vertices independently and uniformly from \(\{1,2,3\}\). For a vertex of out-degree \(d\), conditional on its own colour, the number of same-coloured out-neighbours is distributed as
\[
\operatorname{Bin}(d,1/3).
\]
Define
\[
p_d=\Pr\!\left(\operatorname{Bin}(d,1/3)>\frac d2\right)
   =3^{-d}\sum_{j=\lfloor d/2\rfloor+1}^d \binom dj2^{d-j}.
\]

Thus, if \(B(\phi)\) denotes the number of vertices violating the majority condition, then
\[
\mathbb E B(\phi)=\sum_{v\in V(T)}p_{d^+(v)}. \tag{2.1}
\]
In particular,
\[
\sum_{v\in V(T)}p_{d^+(v)}<1 \tag{2.2}
\]
is an exact sufficient score-sequence criterion for majority \(3\)-colourability.

No independence between the bad-vertex events is needed for this observation.

---

## 3. Tournament score majorization

Write the out-degrees in nondecreasing order:
\[
d_1\le d_2\le\cdots\le d_n.
\]

For every \(k\),
\[
\sum_{i=1}^k d_i\ge \binom{k}{2}. \tag{3.1}
\]
Indeed, the subtournament induced by the \(k\) vertices of smallest out-degree has \(\binom{k}{2}\) internal arcs, each contributing one to the out-degree sum of those vertices. Equality holds in (3.1) for \(k=n\).

Consequently, the vector
\[
(0,1,\ldots,n-1)
\]
majorizes \((d_1,\ldots,d_n)\). Hence, for every convex function \(h\),
\[
\sum_{i=1}^n h(d_i)\le \sum_{j=0}^{n-1}h(j). \tag{3.2}
\]

There is a useful refinement when \(d_i\ge\delta\) for all \(i\). Set
\[
m=2\delta+1
\]
and consider
\[
y=(\underbrace{\delta,\ldots,\delta}_{m\text{ times}},m,m+1,\ldots,n-1).
\]
Necessarily \(n\ge m\). For \(k\le m\), the first \(k\) entries of \(y\) sum to \(k\delta\), while for \(k>m\) they sum to \(\binom{k}{2}\). Therefore \(y\) majorizes the score vector, and
\[
\sum_{i=1}^n h(d_i)
 \le (2\delta+1)h(\delta)+\sum_{j=2\delta+1}^{n-1}h(j) \tag{3.3}
\]
for every convex \(h\).

---

## 4. Minimum out-degree at least \(47\)

Put
\[
\rho=\frac{2\sqrt2}{3}<1
\]
and define, for real \(x\ge0\),
\[
g(x)=\frac{2\rho^x}{\sqrt{\pi(x+1)}}.
\]

### Lemma 2

For every integer \(d\ge0\),
\[
p_d\le g(d). \tag{4.1}
\]
Moreover, \(g\) is decreasing and convex.

#### Proof

First let \(d=2k+1\). The first term in the relevant binomial tail is
\[
b_k=\binom{2k+1}{k+1}
       \left(\frac13\right)^{k+1}
       \left(\frac23\right)^k.
\]
The ratio of each subsequent term to its predecessor is less than \(1/2\), so
\[
p_{2k+1}\le 2b_k.
\]
Using
\[
\binom{2k+1}{k+1}
 =\frac12\binom{2k+2}{k+1}
 \le \frac{4^{k+1}}{2\sqrt{\pi(k+1)}},
\]
we obtain
\[
b_k\le \frac{\rho^{2k+1}}{\sqrt{\pi(2k+2)}}.
\]
Therefore
\[
p_{2k+1}\le
\frac{2\rho^{2k+1}}{\sqrt{\pi(2k+2)}}=g(2k+1).
\]

Also,
\[
p_{2k}<p_{2k+1},
\]
since after appending one Bernoulli trial the event gains the case of exactly \(k\) successes followed by a success. Since \(g\) is decreasing, this gives
\[
p_{2k}<p_{2k+1}\le g(2k+1)<g(2k).
\]
The case \(d=0\) is immediate.

Finally,
\[
\log g(x)=\text{constant}+x\log\rho-\frac12\log(x+1).
\]
Its first derivative is negative, and
\[
\frac{g''(x)}{g(x)}
 =
\left(\log\rho-\frac{1}{2(x+1)}\right)^2
 +\frac{1}{2(x+1)^2}>0.
\]
Thus \(g\) is decreasing and convex. \(\square\)

Now suppose \(\delta^+(T)\ge47\). Applying (3.3) to \(g\), with \(m=95\), gives
\[
\sum_{v\in V(T)}p_{d^+(v)}
 \le 95g(47)+\sum_{j=95}^{\infty}g(j).
\]
Since \(j+1\ge96\) in the tail,
\[
\sum_{j=95}^{\infty}g(j)
 \le
 \frac{2\rho^{95}}{(1-\rho)\sqrt{96\pi}}.
\]
Consequently,
\[
\sum_{v\in V(T)}p_{d^+(v)}
 \le
 \frac{190\rho^{47}}{\sqrt{48\pi}}
 +\frac{2\rho^{95}}{(1-\rho)\sqrt{96\pi}}
 =0.9791\ldots<1. \tag{4.2}
\]
By (2.1), some random colouring has no violating vertex.

### Balanced strengthening

For any fixed colour, its class size is \(\operatorname{Bin}(n,1/3)\). Hence the probability that some colour is used on more than \(n/2\) vertices is at most
\[
3p_n\le3g(n)\le3g(95)<0.0013.
\]
Combining this with (4.2), the probability that either a majority condition fails or some colour class has size greater than \(n/2\) is less than \(0.981\). Thus a balanced majority \(3\)-colouring exists.

This also gives a simple Las Vegas algorithm: repeatedly sample a uniform random \(3\)-colouring and verify it. For \(\delta^+(T)\ge47\), the displayed estimates give a positive success probability bounded away from zero.

---

## 5. Four exceptional vertices in an arbitrary tournament

A sharper score-majorization argument gives a universal constant bound on the number of bad vertices.

Set
\[
a_k=p_{2k+1}\qquad(k\ge0).
\]

### Lemma 3

The sequence \((a_k)\) is decreasing and convex, and
\[
\sum_{k=0}^{\infty}a_k=2. \tag{5.1}
\]

#### Convexity

Let \(X_k\sim\operatorname{Bin}(2k+1,1/3)\), and put
\[
b_k=\Pr(X_k=k).
\]
Comparing \(2k+1\) trials with \(2k+3\) trials gives
\[
a_k-a_{k+1}
 =\frac19 b_k. \tag{5.2}
\]
Moreover,
\[
\frac{b_{k+1}}{b_k}
 =\frac{4(2k+3)}{9(k+2)}<1. \tag{5.3}
\]
Thus the positive differences \(a_k-a_{k+1}\) decrease, proving that \(a_k\) is decreasing and convex.

#### Evaluation of the sum

Let \(S_t\) be the random walk starting at zero with increments \(+1\) with probability \(1/3\) and \(-1\) with probability \(2/3\). Then
\[
p_t=\Pr(S_t>0).
\]
For a positive integer \(j\), the probability that the walk ever reaches \(j\) is
\[
\left(\frac{1/3}{2/3}\right)^j=2^{-j}.
\]
Once the walk first reaches \(j\), its return probability after leaving is
\[
\frac13\cdot1+\frac23\cdot\frac12=\frac23.
\]
Hence the expected total number of visits to \(j\), starting at zero, is
\[
3\cdot2^{-j}.
\]
At odd times the walk can visit only odd states. Therefore, by summing expected occupation times,
\[
\sum_{k=0}^{\infty}a_k
 =3\sum_{\substack{j\ge1\\j\text{ odd}}}2^{-j}
 =3\frac{1/2}{1-1/4}=2.
\]
This proves (5.1). \(\square\)

Now define a sequence \(f\) on the nonnegative integers by
\[
f(0)=\frac{10}{27},
\]
\[
f(2k+1)=a_k,
\]
and
\[
f(2k+2)=\frac{a_k+a_{k+1}}2.
\]
Extend \(f\) linearly between consecutive integers.

Since
\[
a_0=p_1=\frac13,\qquad a_1=p_3=\frac7{27},
\]
the choice \(f(0)=10/27\) continues the initial slope between \(a_0\) and \(a_1\). The convexity of \((a_k)\) then shows that \(f\) is convex.

Also \(f(d)\ge p_d\) for every integer \(d\). Equality holds at odd \(d\). At an even integer \(d=2k+2\),
\[
p_{2k+2}<p_{2k+3}=a_{k+1}
 \le \frac{a_k+a_{k+1}}2=f(2k+2).
\]

Using score majorization (3.2),
\[
\sum_{v\in V(T)}p_{d^+(v)}
 \le \sum_{i=1}^n f(d_i)
 \le \sum_{j=0}^{n-1}f(j).
\]
By Lemma 3,
\[
\begin{aligned}
\sum_{j=0}^{\infty}f(j)
&=\frac{10}{27}
  +\sum_{k\ge0}a_k
  +\frac12\sum_{k\ge0}(a_k+a_{k+1})\\
&=\frac{10}{27}+4-\frac16\\
&=\frac{227}{54}<5.
\end{aligned}
\]
Thus
\[
\mathbb E B(\phi)<5.
\]
Since \(B(\phi)\) is integer-valued, some \(3\)-colouring has
\[
B(\phi)\le4.
\]

This proves Theorem 1(2).

---

## 6. A closure observation

Call a majority colouring of a tournament \(H\) balanced if every colour class has size at most \(|V(H)|/2\).

Suppose \(V(T)\) is partitioned into \(V_1,\ldots,V_s\) such that all arcs between each pair \(V_i,V_j\) have the same direction. If every \(T[V_i]\) has a balanced majority \(3\)-colouring, then their colourings combine to give a balanced majority \(3\)-colouring of \(T\).

Indeed, for \(v\in V_i\), each out-neighbour block \(V_j\) contributes at most \(|V_j|/2\) same-coloured out-neighbours, while the internal contribution is at most half of the internal out-degree.

Consequently, the minimum-out-degree result applies bagwise to arbitrary tournament substitutions. Transitive bags of size at least two also admit balanced majority colourings: order them transitively and use the periodic colour pattern \(1,2,3,1,2,3,\ldots\).

---

## 7. Limitation of the first-moment approach

The bound by four exceptional vertices is close to the integer barrier of this particular method.

Let \(T_r\) be the ordinal sum, from source to sink,
\[
s_{r-1},C_{r-1},s_{r-2},C_{r-2},\ldots,s_0,C_0,
\]
where each \(s_i\) is a singleton and each \(C_i\) is a directed triangle. Then the score multiset is
\[
\{\,4i+1,4i+1,4i+1,4i+3:0\le i<r\,\}.
\]
Hence the expected number of bad vertices under uniform independent colouring is
\[
\sum_{i=0}^{r-1}\bigl(3p_{4i+1}+p_{4i+3}\bigr).
\]
Writing
\[
A=\sum_{i\ge0}p_{4i+1},
\qquad
B=\sum_{i\ge0}p_{4i+3},
\]
Lemma 3 gives \(A+B=2\). Since \(a_k\) is strictly decreasing,
\[
A-B=a_0-a_1+a_2-a_3+\cdots>0,
\]
so \(A>1\). Therefore the preceding expectations tend to
\[
3A+B=2+2A>4.
\]
Thus independent uniform colouring together with a score-sum estimate cannot uniformly force the expected number of violations below four.

These tournaments are not counterexamples: each four-vertex block \(s_i\to C_i\) has a balanced majority colouring, and the closure observation applies.

---

## 8. Remaining gap

The full conjecture remains open after these arguments.

Any counterexample must have
\[
\delta^+(T)\le46,
\]
but this does not bound its order. The four exceptional vertices in Theorem 1(2) also cannot simply be recoloured independently: recolouring a vertex can make arbitrarily many tight in-neighbours newly violate their majority conditions. Deleting the exceptional vertices is likewise invalid, since deleting differently coloured out-neighbours lowers the relevant denominator.

Thus the missing ingredient is a structural or recolouring argument for tournaments with a low-out-degree vertex; the probabilistic score estimates alone do not provide it.