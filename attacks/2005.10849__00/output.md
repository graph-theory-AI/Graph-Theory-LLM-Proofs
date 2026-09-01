```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The asymptotic question remains open, but Clow's upper bound shows that any positive exponent improvement would force a corresponding exponential strengthening of the Moore bound, while any asymptotically Moore family would make the coefficient 1/4 exact.",
  "would_publish": false,
  "caveats": "No unbounded-girth asymptotically Moore family is known; bounded-girth examples only clarify the necessary quantifiers."
}
```

## 1. Precise formulation

Write
\[
D=\delta(G),\qquad d=D-1\ge 2,\qquad n=|V(G)|,\qquad g=g(G).
\]
The proven lower bound is
\[
c(G)\ge \frac1g\,d^{\lfloor (g-1)/4\rfloor}. \tag{1}
\]

Because of the floor, the informal expression \(d^{g/4}\) must be interpreted asymptotically as \(g\to\infty\). A convenient formalization is to define
\[
\alpha_*=\sup\left\{\alpha:\ \exists r(g)=o(g)\text{ such that }
c(G)\ge d^{\alpha g-r(g)}
\text{ for every sufficiently high-girth }G\right\}.
\]
Then (1) gives \(\alpha_*\ge 1/4\), while the Ramanujan examples from the source paper give \(\alpha_*\le 3/8\). The intended problem is whether
\[
\alpha_*=\frac14.
\]

I do not resolve this equality. The main rigorous conclusion below is that an improvement \(\alpha_*\ge 1/4+\varepsilon\) would imply a substantial new lower bound in the degree–girth problem.

---

## 2. Two bounds used

Besides (1), use the upper bound quoted in the catalog from Clow:
\[
c(G)\le \frac{6n\log n}{d^{\lfloor(g+1)/4\rfloor}}. \tag{2}
\]

The Moore bound says
\[
n\ge d^{g/2-O(1)}. \tag{3}
\]
More precisely, if \(g=2r+1\), then
\[
n\ge 1+D\sum_{j=0}^{r-1}d^j,
\]
and if \(g=2r\), then
\[
n\ge 2\sum_{j=0}^{r-1}d^j.
\]
Thus \(d^{g/2+o(g)}\) is the smallest possible order, on the exponential scale, for a graph of minimum degree \(d+1\) and girth \(g\).

---

## 3. Exact exponent for any asymptotically Moore family

### Proposition 1
Let \((G_i)\) be a sequence with \(g_i\to\infty\), and put
\[
d_i=\delta(G_i)-1,\qquad n_i=|V(G_i)|.
\]
Suppose
\[
\log_{d_i} n_i=\frac{g_i}{2}+o(g_i). \tag{4}
\]
Then
\[
\log_{d_i} c(G_i)=\frac{g_i}{4}+o(g_i). \tag{5}
\]

### Proof

The lower bound (1) gives
\[
\log_{d_i}c(G_i)
 \ge \left\lfloor\frac{g_i-1}{4}\right\rfloor-\log_{d_i}g_i
 =\frac{g_i}{4}-o(g_i),
\]
since \(d_i\ge2\) and hence \(\log_{d_i}g_i\le\log_2g_i=o(g_i)\).

For the upper bound, (2) and (4) give
\[
\begin{aligned}
\log_{d_i}c(G_i)
&\le \log_{d_i}n_i-\left\lfloor\frac{g_i+1}{4}\right\rfloor
   +\log_{d_i}(6\log n_i)\\
&=\frac{g_i}{4}+o(g_i)+\log_{d_i}(6\log n_i).
\end{aligned}
\]
The last logarithm is \(o(g_i)\). Indeed, writing
\[
x_i=\log_{d_i}n_i=O(g_i),
\]
we have
\[
\log_{d_i}(6\log n_i)
 =\log_{d_i}(6x_i\log d_i)
 \le C+\log_2 x_i
 =O(\log g_i)=o(g_i),
\]
where \((\log\log d)/\log d\) is uniformly bounded for \(d\ge2\).

This proves (5). ∎

### Consequence

If there exists any family with unbounded girth satisfying
\[
n=(\delta-1)^{g/2+o(g)},
\]
then that family has
\[
c(G)=(\delta-1)^{g/4+o(g)}.
\]
It would therefore disprove every proposed universal improvement to
\[
(\delta-1)^{(1/4+\varepsilon)g-o(g)}.
\]

Thus asymptotically Moore cages would settle the problem in favor of optimality of \(1/4\). Their existence for unbounded girth is itself an unresolved degree–girth problem.

---

## 4. Any improvement would strengthen the Moore bound

The converse implication is also informative.

### Proposition 2
Suppose there are \(\varepsilon>0\) and \(r(g)=o(g)\) such that every sufficiently high-girth graph of minimum degree at least \(3\) satisfies
\[
c(G)\ge d^{(1/4+\varepsilon)g-r(g)}. \tag{6}
\]
Then every such graph satisfies
\[
\log_d n\ge \left(\frac12+\varepsilon\right)g-o(g). \tag{7}
\]
Equivalently,
\[
n\ge d^{(1/2+\varepsilon)g-o(g)}. \tag{8}
\]

### Proof

Combining (6) with (2),
\[
d^{(1/4+\varepsilon)g-r(g)}
\le \frac{6n\log n}{d^{\lfloor(g+1)/4\rfloor}}.
\]
Therefore
\[
n\log n
\ge \frac16d^{(1/4+\varepsilon)g-r(g)+\lfloor(g+1)/4\rfloor}
=d^{(1/2+\varepsilon)g-o(g)}. \tag{9}
\]

Set \(x=\log_d n\). Taking logarithms in (9) gives
\[
x+\log_d(6\log n)\ge
\left(\frac12+\varepsilon\right)g-o(g). \tag{10}
\]
If \(x\ge g^2\), then (7) is immediate. Otherwise \(x<g^2\), and
\[
\log_d(6\log n)
=\log_d(6x\log d)
\le C+\log_2x
=O(\log g)=o(g).
\]
Substituting into (10) proves (7). ∎

### Interpretation

The ordinary Moore bound only gives
\[
n\ge d^{g/2-O(1)}.
\]
Consequently, an improvement of the cop-number coefficient from \(1/4\) to \(1/4+\varepsilon\) would force a uniform positive exponential gap over the Moore bound:
\[
n\ge d^{(1/2+\varepsilon)g-o(g)}.
\]

This is a strong obstruction to a “lean” proof of the improvement. On the other hand, proving such a degree–girth gap would not by itself prove the cop-number improvement; Proposition 2 is only a necessary condition.

---

## 5. Why the floors and the limit \(g\to\infty\) are essential

Taken literally and without an \(O(1)\) loss in the exponent, even the shorthand \(c(G)=\Omega(d^{g/4})\) is false when \(g\) is fixed.

Let \(P_q\) be the incidence graph of the projective plane of order \(q\), where \(q\) is a prime power. Then
\[
|V(P_q)|=2(q^2+q+1),\qquad \delta(P_q)=q+1,\qquad g(P_q)=6.
\]

Moreover,
\[
c(P_q)=q+1. \tag{11}
\]

Here is a self-contained proof.

### Lower bound in (11)

Suppose at most \(q\) cops are used. Every closed neighborhood has \(q+2\) vertices, so the cops' closed neighborhoods cover at most
\[
q(q+2)<2(q^2+q+1)
\]
vertices. The robber can therefore start at distance at least two from every cop.

After any cop move, one cop can control at most one neighbor of the robber's current vertex: if a cop were equal or adjacent to two distinct neighbors, the resulting configuration would create a triangle or a 4-cycle. Since the graph has girth \(6\), this is impossible. The robber has \(q+1\) neighbors and there are at most \(q\) cops, so an uncontrolled neighbor always exists. Moving there restores distance at least two from every cop. Thus \(q\) cops do not suffice.

### Upper bound in (11)

Fix a line \(L\) and put one cop on each of its \(q+1\) points.

- If the robber starts on a line \(M\), then \(M\cap L\) is occupied, and that cop captures the robber on the first move.
- Otherwise the robber starts at a point \(P\notin L\). For each point \(Q\in L\), move the cop at \(Q\) to the line \(PQ\). These are exactly all \(q+1\) lines through \(P\). The robber cannot move to any incident line, and if the robber stays at \(P\), capture occurs on the next cop move.

Hence \(c(P_q)=q+1\).

For this family, \(d=q\) and \(g=6\), so
\[
c(P_q)\asymp d,
\qquad
d^{g/4}=d^{3/2}.
\]
Thus the informal \(g/4\) exponent cannot be interpreted as a floor-free, uniform assertion with fixed \(g\) and \(d\to\infty\). This does not address the intended asymptotic coefficient, because \(g\) remains bounded.

---

## 6. Status and remaining gap

The rigorous picture is therefore:

\[
\frac14\le \alpha_*\le\frac38.
\]

In addition:

1. An unbounded-girth asymptotically Moore family would imply \(\alpha_*=1/4\), by Proposition 1.
2. Any proof that \(\alpha_*>1/4\) would imply a positive exponential improvement over the Moore bound, by Proposition 2.
3. The projective-plane family shows that floors and \(o(g)\) terms cannot be omitted.
4. Neither implication resolves the central existence question. In particular, no suitable asymptotically Moore family is presently available from the information supplied, and the Ramanujan construction only yields the coefficient \(3/8\).

Accordingly, I do not have a complete proof or counterexample to the intended unbounded-girth conjecture.