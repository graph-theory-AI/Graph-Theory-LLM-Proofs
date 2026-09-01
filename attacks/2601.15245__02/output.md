```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but it holds when every block has diameter at most \(d^{\varepsilon/2}\), and the relevant coupon-collector statistic can be localized by the Lovász Local Lemma at the conjectured maximum-degree scale.",
  "would_publish": false,
  "caveats": "The LLL construction is not a proper coloring; making the locally available color choices consistent remains the central gap."
}
```

# Mathematical writeup

## 1. Problem and conventions

Fix \(0<\varepsilon<1\). The question is whether there is a constant \(C_\varepsilon\) such that every finite triangle-free, \(d\)-degenerate graph \(G\) satisfying
\[
\Delta(G)\le \exp\bigl(d^{1-\varepsilon}\bigr)
\]
has
\[
\chi(G)\le C_\varepsilon\frac d{\log d}.
\]

All logarithms below are natural. The cases \(\varepsilon\ge1\) are trivial asymptotically, since then the maximum-degree hypothesis is bounded.

I do not obtain a proper coloring in the general case. I give:

1. an affirmative result when the blocks of \(G\) have moderately bounded diameter;
2. a necessary large-diameter structure for any counterexample family;
3. an LLL lemma showing that the coupon-collector estimates suggested by the source theorem can indeed be made simultaneous under the stated maximum-degree hypothesis;
4. the precise consistency obstruction preventing this lemma from completing the proof.

---

## 2. Consequence of the source paper's order-dependent theorem

I use the theorem quoted in the problem statement:

> If \(H\) is an \(n\)-vertex, triangle-free, \(d\)-degenerate graph in the relevant range, then
> \[
> \chi(H)=O\left(\frac d{\log(d/\log n)}\right).
> \tag{2.1}
> \]

An immediate useful specialization is the following.

### Lemma 2.1

For every fixed \(\eta>0\), every triangle-free, \(d\)-degenerate graph \(H\) on
\[
|V(H)|\le \exp\bigl(d^{1-\eta}\bigr)
\]
vertices satisfies
\[
\chi(H)=O_\eta\left(\frac d{\log d}\right).
\]

### Proof

Since \(\log |V(H)|\le d^{1-\eta}\),
\[
\log\left(\frac d{\log |V(H)|}\right)
 \ge \log(d^\eta)
 =\eta\log d.
\]
Substitution into (2.1) gives the assertion. \(\square\)

This can be applied blockwise, which removes the irrelevant obstruction coming from a graph being a long chain of small pieces.

### Proposition 2.2: bounded-block-diameter case

Fix \(0<\gamma<\varepsilon<1\). Suppose \(G\) is triangle-free and \(d\)-degenerate, satisfies
\[
\Delta(G)\le \exp\bigl(d^{1-\varepsilon}\bigr),
\]
and every block \(B\) of \(G\) has
\[
\operatorname{diam}(B)\le d^{\varepsilon-\gamma}.
\]
Then
\[
\chi(G)=O_\gamma\left(\frac d{\log d}\right).
\]

In particular, the conjectured conclusion holds if every block has diameter at most \(d^{\varepsilon/2}\).

### Proof

Let \(B\) be a block and put \(R=\operatorname{diam}(B)\). The elementary breadth-first-search bound gives
\[
|V(B)|\le \bigl(\Delta(G)+1\bigr)^{R+1}.
\]
Therefore
\[
\log |V(B)|
 \le (R+1)\log(\Delta(G)+1)
 =O\left(d^{\varepsilon-\gamma}d^{1-\varepsilon}\right)
 =O\left(d^{1-\gamma}\right).
\]
For sufficiently large \(d\), the constant in the last \(O\)-term can be absorbed to give
\[
|V(B)|\le \exp\bigl(d^{1-\gamma/2}\bigr).
\]
Lemma 2.1 therefore gives
\[
\chi(B)=O_\gamma\left(\frac d{\log d}\right).
\]

Finally,
\[
\chi(G)=\max_B\chi(B),
\]
where the maximum is over the blocks of \(G\). Indeed, after rooting the block-cutvertex forest, color the blocks successively; when a new block meets the already colored graph at a cutvertex, permute its color names so that the two colors at that cutvertex agree. Thus one common palette suffices. \(\square\)

As another standard special case, if \(\Delta(G)\le A d\) for fixed \(A\), the classical triangle-free maximum-degree bound
\[
\chi(G)=O\left(\frac{\Delta(G)}{\log\Delta(G)}\right)
\]
already gives \(\chi(G)=O_A(d/\log d)\). The unresolved regime is therefore genuinely the one in which \(\Delta/d\) is unbounded and the chromatic obstruction lives in a large 2-connected piece.

---

## 3. What a counterexample family would have to look like

Suppose the conjecture is false for some fixed \(0<\varepsilon<1\). Then there is a sequence \(G_i\), with parameters \(d_i\to\infty\), such that
\[
\Delta(G_i)\le \exp\bigl(d_i^{1-\varepsilon}\bigr)
\quad\text{and}\quad
\frac{\chi(G_i)\log d_i}{d_i}\longrightarrow\infty.
\tag{3.1}
\]

Choose an induced vertex-critical subgraph \(H_i\subseteq G_i\) with
\[
\chi(H_i)=\chi(G_i).
\]
Then:

- \(H_i\) is triangle-free and \(d_i\)-degenerate;
- \(\Delta(H_i)\le \exp(d_i^{1-\varepsilon})\);
- \(H_i\) is 2-connected for all sufficiently large \(i\);
- \(\delta(H_i)\ge \chi(H_i)-1\).

The last two facts are standard critical-graph arguments. A cutvertex would allow colorings of the two sides to be combined after permuting color names, and a vertex of degree at most \(\chi(H_i)-2\) could be colored after coloring its deletion.

More significantly, for every fixed \(\eta>0\), eventually
\[
|V(H_i)|>\exp\bigl(d_i^{1-\eta}\bigr).
\tag{3.2}
\]
Otherwise Lemma 2.1 would bound the ratio in (3.1) by a constant depending only on \(\eta\).

Let \(R_i=\operatorname{diam}(H_i)\). Since a connected graph of maximum degree \(\Delta\) and diameter \(R\) has at most \((\Delta+1)^{R+1}\) vertices,
\[
R_i+1
 \ge \frac{\log |V(H_i)|}{\log(\Delta(H_i)+1)}.
\]
Combining (3.2) with \(\log(\Delta(H_i)+1)\le 2d_i^{1-\varepsilon}\), for every fixed \(0<\eta<\varepsilon\) one gets
\[
R_i\ge \frac12 d_i^{\varepsilon-\eta}-1
\]
for all sufficiently large \(i\).

Thus any counterexample family must contain 2-connected, vertex-critical graphs satisfying
\[
\delta(H_i)\ge\chi(H_i)-1
\quad\text{and}\quad
\operatorname{diam}(H_i)=d_i^{\varepsilon-o(1)}.
\]
In particular, counterexamples cannot be manufactured merely by joining small chromatic obstructions through cutvertices.

---

## 4. A localized coupon-collector lemma

A \(d\)-degeneracy ordering gives an acyclic orientation in which every vertex has outdegree at most \(d\). For an orientation \(D\), write \(N^+(v)\) for the outneighborhood and \(r_v=|N^+(v)|\).

The following lemma shows that the basic coupon-collector statistic can be controlled simultaneously by the LLL under precisely the relevant maximum-degree condition.

### Lemma 4.1

Fix \(0<\varepsilon<1\), and put
\[
K=\frac8\varepsilon,
\qquad
q=\left\lceil K\frac d{\log d}\right\rceil.
\]
For all sufficiently large \(d=d(\varepsilon)\), let \(D\) be any orientation of a graph \(G\) such that
\[
d_D^+(v)\le d
\quad\text{and}\quad
\Delta(G)\le \exp\bigl(d^{1-\varepsilon}\bigr).
\]
Then there is a labeling
\[
X:V(G)\longrightarrow [q]
\]
such that, for every \(v\), the number \(M_v\) of labels absent from \(X(N^+(v))\) satisfies
\[
\frac12q\left(1-\frac1q\right)^{r_v}
 \le M_v\le
\frac32q\left(1-\frac1q\right)^{r_v}.
\tag{4.1}
\]

The lemma does not require triangle-freeness.

### Proof

Initially choose the labels \(X_u\), \(u\in V(G)\), independently and uniformly from \([q]\). For a fixed vertex \(v\),
\[
M_v=\left|[q]\setminus\{X_u:u\in N^+(v)\}\right|.
\]
By linearity of expectation,
\[
\mu_v:=\mathbb E M_v
 =q\left(1-\frac1q\right)^{r_v}.
\tag{4.2}
\]

Changing one variable \(X_u\), for \(u\in N^+(v)\), changes \(M_v\) by at most one. Hence the bounded-differences inequality gives, when \(r_v>0\),
\[
\Pr\left(\left|M_v-\mu_v\right|>\frac{\mu_v}{2}\right)
 \le 2\exp\left(-\frac{\mu_v^2}{2r_v}\right).
\tag{4.3}
\]

Since \(r_v\le d\),
\[
\mu_v\ge \mu_*:=q\left(1-\frac1q\right)^d.
\]
For sufficiently large \(d\),
\[
q-1\ge \frac{Kd}{2\log d}.
\]
Using
\[
\log(1-x)\ge-\frac{x}{1-x},
\]
we obtain
\[
\left(1-\frac1q\right)^d
 \ge \exp\left(-\frac d{q-1}\right)
 \ge d^{-2/K}.
\]
Consequently,
\[
\mu_*\ge qd^{-2/K}
 \ge K\frac{d^{1-2/K}}{\log d}.
\]
Thus every bad event
\[
B_v=\left\{\left|M_v-\mu_v\right|>\frac{\mu_v}{2}\right\}
\]
has probability at most
\[
p\le
2\exp\left(
-\frac{K^2}{2}\frac{d^{1-4/K}}{(\log d)^2}
\right).
\tag{4.4}
\]
Because \(K=8/\varepsilon\), one has \(4/K=\varepsilon/2\), so the negative exponent in (4.4) is
\[
\Omega_\varepsilon\left(
\frac{d^{1-\varepsilon/2}}{(\log d)^2}
\right).
\tag{4.5}
\]

The event \(B_v\) depends only on variables indexed by \(N^+(v)\). A variable \(X_u\) occurs in at most \(\deg_G(u)\le\Delta(G)\) such events. Hence each \(B_v\) is dependent on at most
\[
D_0\le d\Delta(G)
\]
other bad events. Now
\[
\log(D_0+1)
 \le O(\log d)+d^{1-\varepsilon},
\]
whereas the exponent in (4.5) is
\[
\frac{d^{1-\varepsilon/2}}{(\log d)^2}
 \gg d^{1-\varepsilon}.
\]
Therefore, for sufficiently large \(d\),
\[
ep(D_0+1)\le1.
\]
The symmetric Lovász Local Lemma gives positive probability that no \(B_v\) occurs, which is precisely (4.1). Vertices with \(r_v=0\) satisfy (4.1) deterministically. \(\square\)

This lemma replaces a union bound over all vertices by a dependency bound of order \(d\Delta\). Numerically, therefore, the hypothesis
\[
\log\Delta\le d^{1-\varepsilon}
\]
is more than strong enough for the coupon-collector concentration at
\[
q=\Theta_\varepsilon(d/\log d).
\]

---

## 5. Why Lemma 4.1 does not give a coloring

For a labeling \(x:V(G)\to[q]\), define
\[
A_x(v)=[q]\setminus x(N^+(v)).
\]
A proper coloring \(c\) is exactly a fixed point satisfying
\[
c(v)\in A_c(v)\qquad\text{for every }v.
\tag{5.1}
\]

Lemma 4.1 gives a labeling \(x\) for which every \(A_x(v)\) has the expected coupon-collector size, but it does not give
\[
x(v)\in A_x(v).
\]
Choosing a new color \(c(v)\in A_x(v)\) is not enough: once \(x(v)\) is replaced by \(c(v)\), the available sets of all in-neighbors of \(v\) change. In a degeneracy orientation these changes can propagate along directed paths of arbitrary length.

The direct random-coloring bad event is also unsuitable for the LLL. For a vertex of outdegree \(d\),
\[
\Pr\bigl(X_v\notin A_X(v)\bigr)
 =1-\left(1-\frac1q\right)^d
 =1-d^{-\Theta_\varepsilon(1)},
\]
which tends to one when \(q=\Theta_\varepsilon(d/\log d)\). Thus the properness violations themselves are not rare local events.

Triangle-freeness says that \(N^+(v)\) is an independent set, but it does not make the eventual colors of those vertices independent: their choices can be coupled through common distance-two vertices and through arbitrarily long chains. This is exactly where the desired localization of the random greedy process is still missing.

---

## 6. Conclusion

The general conjecture is neither proved nor disproved here. The unconditional progress is:

- the conjectured bound holds when every block has diameter at most \(d^{\varepsilon/2}\), more generally \(d^{\varepsilon-\gamma}\) for fixed \(\gamma>0\);
- any counterexample family must contain 2-connected vertex-critical graphs of diameter \(d^{\varepsilon-o(1)}\) and minimum degree at least \(\chi-1\);
- the coupon-collector concentration underlying the \(d/\log d\) scale can be made simultaneous by the LLL under \(\Delta\le e^{d^{1-\varepsilon}}\).

The unresolved step is a consistency or fixed-point problem: converting locally large sets \(A_x(v)\) into one labeling \(c\) satisfying \(c(v)\in A_c(v)\) everywhere without introducing unbounded-range dependencies.