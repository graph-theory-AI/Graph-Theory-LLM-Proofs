```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A local-lemma construction gives the necessary bound xi(c) < 1/ceil(1/c) for 0 < c < 1/2, but does not settle Possibility 1.6.",
  "would_publish": false,
  "caveats": "Necessary-condition improvement only; novelty of the probabilistic argument is not claimed."
}
```

# A stronger probabilistic obstruction

I obtain a partial negative result, not a counterexample to the quantified conjecture. In particular, any \(\xi(c)\) satisfying Possibility 1.6 would necessarily obey
\[
\boxed{\quad \xi(c)<\frac{1}{\lceil 1/c\rceil}\qquad(0<c<1/2).\quad}
\]
The witnesses can be chosen to be connected unicyclic forbidden graphs. For long cycles themselves, the argument also improves the negative range quoted in the prompt.

Throughout, graphs are finite and simple, and \(H\)-free means induced-\(H\)-free.

## 1. An auxiliary density parameter

Write \(\kappa(F)\) for the congestion of \(F\). Define
\[
\kappa_2(F)=
\max\left(
\{0\}\cup
\left\{
\frac{e(J)-v(J)+1}{e(J)-1}:
J\subseteq F,\ e(J)\ge2
\right\}
\right).
\]
This notation is auxiliary; the parameter in the question remains \(\kappa\).

Both parameters vanish on forests. If \(F\) contains a cycle, then
\[
\kappa_2(F)>\kappa(F).
\]
Indeed, choose \(J\) attaining the positive maximum defining congestion, and put \(r=e(J)-v(J)+1>0\). Then
\[
\kappa_2(F)\ge \frac{r}{e(J)-1}
>\frac{r}{e(J)}=\kappa(F).
\]

Here is the obstruction.

### Theorem
Let \(H\) be fixed, and suppose
\[
0<c<\min\{\kappa_2(H),\kappa_2(\overline H)\}.
\]
Then, for every sufficiently large integer \(n\), there is an \(n\)-vertex graph \(G_n\) that is \(H\)-free and \(\overline H\)-free and has no pure pair \(A,B\) with
\[
|A|\ge \left\lceil\frac{n}{\log n}\right\rceil,
\qquad
|B|\ge \left\lceil\frac{n^{1-c}}{\log n}\right\rceil.
\]
Consequently, no positive constant \(\varepsilon\) gives the conclusion of Possibility 1.6 for this particular \(H,c\).

### Proof

Choose subgraphs
\[
F_1\subseteq H,\qquad F_2\subseteq\overline H
\]
such that, writing \(v_i=v(F_i)\) and \(e_i=e(F_i)\),
\[
\beta_i:=\frac{e_i-v_i+1}{e_i-1}>c
\qquad(i=1,2).
\]
Choose
\[
c<\alpha<\min\{\beta_1,\beta_2\}.
\]
In particular, \(0<\alpha<1\).

Consider the binomial random graph \(G(n,p)\), where
\[
p=n^{\alpha-1}.
\]
Set
\[
a=\left\lceil\frac{n}{\log n}\right\rceil,\qquad
b=\left\lceil\frac{n^{1-c}}{\log n}\right\rceil,\qquad
q=pab.
\]
Since \(\alpha>c\),
\[
q=(1+o(1))\frac{n^{1+\alpha-c}}{(\log n)^2},
\qquad
\frac qn\longrightarrow\infty.
\]

We apply the asymmetric Lovász local lemma to two kinds of bad events.

* **Copy events:** for each injective map \(V(F_i)\to[n]\), all the corresponding edges of \(F_i\) are present. Its probability is \(p^{e_i}\). These concern ordinary, not necessarily induced, copies.
* **Rectangle events:** for each ordered pair of disjoint sets \(A,B\) with \(|A|=a\), \(|B|=b\), either all edges between them are absent or all are present. These are two separate events.

For sufficiently large \(n\), each rectangle event has probability at most
\[
e^{-pab}=e^{-q}.
\]
There are at most \(2\cdot3^n\) rectangle events.

Two events are joined in the dependency graph when they use a common edge variable. Events not joined to a given event are jointly independent of it.

Assign local-lemma weights
\[
x_E=2p^{e_i}
\]
to copy events of type \(i\), and
\[
x_E=e^{-q/2}
\]
to rectangle events.

#### Bounding the dependency contributions

A fixed edge of \(K_n\) belongs to at most
\[
2e_i n^{v_i-2}
\]
labelled copies of \(F_i\). Define
\[
\tau_n=4\sum_{i=1}^2 e_i n^{v_i-2}p^{e_i-1}.
\]
For each \(i\),
\[
n^{v_i-2}p^{e_i-1}
=n^{(e_i-1)(\alpha-\beta_i)}
\longrightarrow0,
\]
so \(\tau_n\to0\).

Thus, for an event depending on \(t\) edge variables, the total weight of adjacent copy events is at most
\[
tp\tau_n.
\]
The total weight of all rectangle events is at most
\[
R_n:=2\cdot3^n e^{-q/2}\longrightarrow0,
\]
because \(q/n\to\infty\).

All the weights are at most \(1/2\) for large \(n\). Therefore, using
\(\log(1-x)\ge-2x\) for \(0\le x\le1/2\), every event \(E\) depending on \(t\) edge variables satisfies
\[
\prod_{D\sim E}(1-x_D)
\ge
\exp\bigl(-2tp\tau_n-2R_n\bigr).
\]

#### Checking the local-lemma inequalities

For a copy event of type \(i\), \(t=e_i\) is fixed. Hence
\[
\prod_{D\sim E}(1-x_D)=1-o(1)\ge \frac12
\]
for large \(n\), and therefore
\[
\mathbb P(E)=p^{e_i}
\le
x_E\prod_{D\sim E}(1-x_D).
\]

For a rectangle event, \(t=ab\), so
\[
x_E\prod_{D\sim E}(1-x_D)
\ge
\exp\bigl(-q/2-2q\tau_n-2R_n\bigr).
\]
Since \(\tau_n\to0\) and \(R_n/q\to0\), this is at least \(e^{-q}\) for sufficiently large \(n\). Thus the local-lemma inequality also holds for every rectangle event.

The Lovász local lemma now gives positive probability that none of the bad events occurs.

The resulting graph contains neither \(F_1\) nor \(F_2\) as an ordinary subgraph. It is consequently induced-\(H\)-free and induced-\(\overline H\)-free. It has no pure pair of sizes exactly \(a,b\), and hence none with both sizes at least \(a,b\).

Finally, for every fixed \(\varepsilon>0\), sufficiently large \(n\) satisfies
\[
a\le\varepsilon n,\qquad
b\le\varepsilon n^{1-c}.
\]
So these graphs rule out every fixed \(\varepsilon\) in the claimed conclusion. \(\square\)

## 2. Consequences for unicyclic forbidden graphs

For an integer \(\ell\ge3\), let \(H_\ell\) be obtained from \(C_\ell\) by attaching two leaves to the same cycle vertex.

Its only cycle is \(C_\ell\). Every cyclic subgraph has at least \(\ell\) edges and has \(e-v+1\le1\). The cycle itself attains equality in the relevant bounds, giving
\[
\kappa(H_\ell)=\frac1\ell,
\qquad
\kappa_2(H_\ell)=\frac1{\ell-1}.
\]

The two leaves, together with any cycle vertex other than their common neighbour, form an independent set of size three in \(H_\ell\). Thus \(\overline{H_\ell}\) contains a triangle, and
\[
\kappa_2(\overline{H_\ell})\ge\kappa_2(K_3)=\frac12.
\]
It follows that
\[
\min\{\kappa_2(H_\ell),\kappa_2(\overline{H_\ell})\}
=\frac1{\ell-1}.
\]

The theorem therefore proves:

### Corollary
For every integer \(\ell\ge3\) and every
\[
0<c<\frac1{\ell-1},
\]
there is no \(\varepsilon>0\) such that all \(H_\ell\)-free and \(\overline{H_\ell}\)-free graphs satisfy the conclusion of Possibility 1.6.

For this family, the smaller congestion of \(H_\ell,\overline{H_\ell}\) is \(1/\ell\). Thus the obstruction quoted in the prompt covers \(c<1/\ell\), while the argument above extends it to
\[
c<\frac1{\ell-1}.
\]
In particular, failure can occur even when \(\kappa(H_\ell)<c\).

### Necessary bound on \(\xi(c)\)

Fix \(0<c<1/2\), and put
\[
L=\lceil1/c\rceil.
\]
Then \(L\ge3\), and
\[
L-1<1/c,
\qquad\text{so}\qquad
c<\frac1{L-1}.
\]
The corollary applies to \(H_L\), whose congestion is \(1/L\).

If an admissible value of \(\xi(c)\) were at least \(1/L\), then \(H_L\) would be among the forbidden graphs covered by Possibility 1.6, contradicting the corollary. Hence necessarily
\[
\boxed{\xi(c)<\frac1{\lceil1/c\rceil}\qquad(0<c<1/2).}
\]

For bare cycles, the same negative range holds when \(\ell\ge5\): \(\overline{C_5}\cong C_5\), and \(\overline{C_\ell}\) contains a triangle for \(\ell\ge6\). Thus \(H=C_\ell\) already gives failure for every \(c<1/(\ell-1)\) in that range.

## 3. The unresolved gap

The bound above does **not** disprove Possibility 1.6: the conjecture permits choosing a smaller positive \(\xi(c)\).

Indeed, the density criterion used here cannot reach arbitrarily small congestion for a fixed \(c\). Put \(L=\lceil1/c\rceil\). If
\[
\kappa(F)<\frac1L,
\]
then
\[
\kappa_2(F)\le\frac1L\le c.
\]
To see this, consider a subgraph \(J\) with positive integer
\[
r=e(J)-v(J)+1.
\]
The congestion assumption gives \(r/e(J)<1/L\), so integrality yields
\[
e(J)\ge rL+1.
\]
Consequently,
\[
\frac{r}{e(J)-1}\le\frac1L.
\]
Subgraphs with nonpositive numerator do not affect the maximum.

Thus the probabilistic criterion cannot produce counterexamples below the displayed congestion threshold. Nor does the argument establish any positive sufficient value of \(\xi(c)\).

The partial theorem is proved above; the central question—whether sufficiently small positive congestion always forces a pure pair with one linear side—remains unresolved here.