```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open; it holds under bounded-degree, short-peeling, and almost-dominating-clique hypotheses, while any linear counterexample must recur at every degeneracy scale and have a long high-degree and dual-weight hierarchy.",
  "would_publish": false,
  "caveats": "The argument does not control unbounded peeling depth or arbitrarily many LP weight scales; one ingredient is the standard bounded-maximum-degree coloring theorem for fixed clique number."
}
```

## 1. Statement and notation

For fixed \(r\ge 4\), write
\[
F_r(d)=\sup\{\chi_f(G):G\text{ is }K_r\text{-free and }d\text{-degenerate}\}.
\]
The trivial greedy bound is \(F_r(d)\le d+1\). The problem asks whether
\[
\frac{F_r(d)}d\longrightarrow 0.
\]

I do not obtain a proof or a counterexample. I prove several reductions and special cases, including a sparsification lemma showing that failure at one large degeneracy scale propagates to every smaller scale with only a constant-factor loss.

I use two established inputs:

1. The triangle-free result quoted in the question:
   \[
   F_3(d)\le (4+o(1))\frac d{\log d}.
   \tag{TF}
   \]
2. For every fixed \(r\), the standard bounded-maximum-degree estimate
   \[
   \chi_f(H)\le \chi_\ell(H)
      \le C_r\frac{\Delta(H)\log\log \Delta(H)}{\log \Delta(H)}
   \tag{BD}
   \]
   for \(K_r\)-free \(H\) of sufficiently large maximum degree. A published source for this coarse form is Molloy, *The list chromatic number of graphs with small clique number*, JCTB 134 (2019).

All logarithms below are natural.

---

## 2. A fractional sparsification lemma

The fractional chromatic LP and its dual are
\[
\chi_f(G)=
 \min\left\{\sum_{I\in\mathcal I(G)}x_I:
 x_I\ge0,\ \sum_{I\ni v}x_I\ge1\ \forall v\right\},
\]
and
\[
\chi_f(G)=
 \max\left\{\sum_{v\in V(G)}w_v:
 w_v\ge0,\ \sum_{v\in I}w_v\le1\ \forall I\in\mathcal I(G)\right\}.
\tag{2.1}
\]

### Lemma 2.1 — sparsification

Let \(G\) be \(d\)-degenerate and put \(W=\chi_f(G)\). For every integer
\[
1\le k\le W
\]
there is an induced subgraph \(H\subseteq G\) such that
\[
\operatorname{dgn}(H)\le
 \left\lceil\frac{4dk}{W}\right\rceil
 \qquad\text{and}\qquad
\chi_f(H)\ge \frac{k}{4}.
\tag{2.2}
\]
Any hereditary property of \(G\), in particular \(K_r\)-freeness, is preserved.

#### Proof

Choose an optimal dual weighting \(w\). Let
\[
S=\{v:w_v>0\}.
\]
The restriction of \(w\) to \(G[S]\) is dual-feasible with total weight \(W\), while \(\chi_f(G[S])\le\chi_f(G)=W\). Hence
\[
\chi_f(G[S])=W.
\]
Replacing \(G\) by \(G[S]\), we may assume \(w_v>0\) for every \(v\).

Choose an optimal primal solution paired with \(w\). Complementary slackness implies that every vertex is covered with total primal weight exactly \(1\). After normalizing the primal solution by its total weight \(W\), we obtain a random independent set \(I\) satisfying
\[
\mathbb P(v\in I)=\frac1W
\qquad\text{for every }v.
\tag{2.3}
\]

Take \(k\) independent samples \(I_1,\dots,I_k\), and let
\[
U=I_1\cup\cdots\cup I_k.
\]
Since \(k\le W\),
\[
\mathbb P(v\in U)
 =1-\left(1-\frac1W\right)^k
 \ge \frac{k}{2W}.
\tag{2.4}
\]

Fix an acyclic orientation of \(G\) with outdegree at most \(d\). For \(v\), let
\[
Z_v=|N^+(v)\cap U|.
\]
If \(uv\in E(G)\), then \(u\) and \(v\) cannot occur in the same \(I_i\). Thus
\[
\mathbb P(u,v\in U)
 \le \frac{k(k-1)}{W^2}.
\]
Consequently,
\[
\begin{aligned}
\mathbb E[Z_v\mathbf 1_{\{v\in U\}}]
 &=\sum_{u\in N^+(v)}\mathbb P(u,v\in U)\\
 &\le \frac{dk(k-1)}{W^2}
 \le \frac{dk^2}{W^2}.
\end{aligned}
\]
Using (2.4),
\[
\mathbb E[Z_v\mid v\in U]\le \frac{2dk}{W}.
\]
Markov's inequality therefore gives
\[
\mathbb P\left(
 Z_v\le\frac{4dk}{W}\,\middle|\,v\in U
 \right)\ge\frac12.
\]
Define
\[
T=\left\{v\in U:Z_v\le\frac{4dk}{W}\right\}.
\]
Then, uniformly in \(v\),
\[
\mathbb P(v\in T)\ge\frac{k}{4W}.
\tag{2.5}
\]

The inherited acyclic orientation of \(G[T]\) has maximum outdegree at most
\[
D=\left\lceil\frac{4dk}{W}\right\rceil,
\]
so \(G[T]\) is \(D\)-degenerate. Moreover, by (2.5),
\[
\mathbb E\,w(T)
 \ge \frac{k}{4W}\sum_v w_v
 =\frac{k}{4}.
\]
Hence some realization \(T\) satisfies \(w(T)\ge k/4\). The restricted weighting is dual-feasible for \(G[T]\), and therefore
\[
\chi_f(G[T])\ge w(T)\ge k/4.
\]
Taking \(H=G[T]\) proves the lemma. \(\square\)

### Corollary 2.2 — asymptotic dichotomy

Let
\[
L^+=\limsup_{d\to\infty}\frac{F_r(d)}d,
\qquad
L^-=\liminf_{d\to\infty}\frac{F_r(d)}d.
\]
Then
\[
L^-\ge \frac{L^+}{16}.
\tag{2.6}
\]

In particular, either \(F_r(d)=o(d)\), or else there is \(c_r>0\) such that
\[
F_r(d)\ge c_r d
\]
for every sufficiently large \(d\).

#### Proof

Fix \(0<\delta<L^+\). There are arbitrarily large \(d\) and finite \(K_r\)-free \(d\)-degenerate graphs \(G\) with
\[
W=\chi_f(G)\ge\delta d.
\]
For a large target integer \(x\), choose such a \(d\ge x\) and put
\[
k=\left\lfloor\frac{\delta(x-1)}4\right\rfloor.
\]
Then \(k\le W\), and Lemma 2.1 produces \(H\) with
\[
\operatorname{dgn}(H)
 \le\left\lceil\frac{4dk}{W}\right\rceil
 \le\left\lceil\frac{4k}{\delta}\right\rceil
 \le x
\]
and
\[
\chi_f(H)\ge\frac{k}{4}
 =\left(\frac{\delta}{16}-o(1)\right)x.
\]
Thus \(F_r(x)/x\ge\delta/16-o(1)\). Letting first \(x\to\infty\) and then \(\delta\uparrow L^+\) gives (2.6). \(\square\)

A stronger finite formulation is useful: if a single graph satisfies
\[
\chi_f(G)\ge\varepsilon d,
\]
then for every sufficiently large \(x\le d\), it contains an induced \(K_r\)-free \(x\)-degenerate subgraph \(H_x\) with
\[
\chi_f(H_x)\ge \frac{\varepsilon x}{32}.
\tag{2.7}
\]
Thus a counterexample cannot live only at isolated degeneracy scales.

---

## 3. Bounded maximum degree and peeling depth

From (BD), every \(K_r\)-free graph \(G\) satisfies
\[
\chi_f(G)\le
 C_r\frac{\Delta(G)\log\log \Delta(G)}{\log\Delta(G)}.
\tag{3.1}
\]

Therefore the conjecture holds for every family satisfying
\[
\frac{\Delta(G)}d
 \frac{\log\log(\Delta(G)+3)}{\log(\Delta(G)+2)}
 \longrightarrow0.
\tag{3.2}
\]
In particular, it holds if
\[
\Delta(G)=o\!\left(\frac{d\log d}{\log\log d}\right).
\tag{3.3}
\]

Conversely, for every fixed \(\varepsilon>0\), a graph with
\[
\chi_f(G)\ge\varepsilon d
\]
must satisfy
\[
\Delta(G)\ge
 c_{r,\varepsilon}\frac{d\log d}{\log\log d}.
\tag{3.4}
\]
Indeed, \(\Delta(G)\ge\chi_f(G)-1=\Omega_\varepsilon(d)\), so \(\log\Delta\) and \(\log d\) are comparable in the range relevant to (3.4), and (3.1) then gives the assertion.

This can be extended from bounded maximum degree to graphs having a short high-degree peeling hierarchy.

### Definition 3.1

For \(D\ge d\), put \(S_0=V(G)\), and recursively define
\[
L_i=\{v\in S_i:\deg_{G[S_i]}(v)\le D\},
\qquad
S_{i+1}=S_i\setminus L_i.
\]
Because \(G\) is \(d\)-degenerate and \(D\ge d\), the process terminates. Let
\[
\tau_D(G)
\]
be the number of nonempty layers \(L_i\).

### Proposition 3.2

For fixed \(r\),
\[
\chi_f(G)\le
 C_r\,\tau_D(G)\,
 \frac{D\log\log D}{\log D}.
\tag{3.5}
\]

#### Proof

For every \(i\),
\[
\Delta(G[L_i])\le D,
\]
because \(L_i\subseteq S_i\). The graph \(G[L_i]\) is \(K_r\)-free, so (BD) gives
\[
\chi_f(G[L_i])
 \le C_r\frac{D\log\log D}{\log D}.
\]
Fractional chromatic number is subadditive over a vertex partition: use disjoint color spaces for the different induced parts. Summing over the layers proves (3.5). \(\square\)

Taking \(D=Ad\) for fixed \(A>1\), we obtain:

> If
> \[
> \tau_{Ad}(G)=o\!\left(\frac{\log d}{\log\log d}\right),
> \]
> then \(\chi_f(G)=o(d)\).

Hence a linear counterexample must satisfy
\[
\tau_{Ad}(G)
 =\Omega_{r,A,\varepsilon}\!\left(
 \frac{\log d}{\log\log d}
 \right)
\tag{3.6}
\]
for every fixed \(A>1\).

There is also an order-dependent bound. If \(D>2d\), then
\[
|S_{i+1}|<\frac{2d}{D}|S_i|.
\]
Indeed, every vertex of \(S_{i+1}\) has more than \(D\) neighbors in \(S_i\), while
\[
\sum_{v\in S_i}\deg_{G[S_i]}(v)
 \le 2d|S_i|.
\]
Thus, for \(n=|V(G)|\),
\[
\tau_D(G)
 \le 1+\frac{\log n}{\log(D/(2d))},
\]
and consequently
\[
\chi_f(G)
 \le C_r\frac{D\log\log D}{\log D}
 \left(
 1+\frac{\log n}{\log(D/(2d))}
 \right).
\tag{3.7}
\]
Because \(n\) is unrestricted, (3.7) does not settle the problem.

Combining Lemma 2.1 with (3.4) and (3.6) gives a multiscale obstruction: if one graph satisfies \(\chi_f(G)\ge\varepsilon d\), then for every large \(x\le d\) it contains an induced \(H_x\) satisfying (2.7), and necessarily
\[
\Delta(H_x)
 =\Omega_{r,\varepsilon}\!\left(
 \frac{x\log x}{\log\log x}
 \right)
\]
and
\[
\tau_{Ax}(H_x)
 =\Omega_{r,A,\varepsilon}\!\left(
 \frac{\log x}{\log\log x}
 \right).
\]

---

## 4. An obstruction in the dual weight scales

The preceding high-degree obstruction has a dual analogue.

For a positive weighting \(w\), let \(q(w)\) denote the number of nonempty dyadic weight classes
\[
\left(2^{-j-1}M,2^{-j}M\right],
\qquad M=\max_v w_v.
\]

### Proposition 4.1

Let \(G\) be \(K_r\)-free and \(d\)-degenerate, and let \(w\) be any feasible dual weighting. Then
\[
\sum_v w_v
 \le
 C'_r\,q(w)\,
 \frac{d\log\log d}{\log d}.
\tag{4.1}
\]

#### Proof

Fix one dyadic class \(S\), so all its weights lie in \((a,2a]\). Since \(G[S]\) is \(d\)-degenerate,
\[
e(G[S])\le d|S|.
\]
At least \(|S|/2\) vertices of \(S\) have degree at most \(4d\) in \(G[S]\). Let \(L\) be this set. Then
\[
\Delta(G[L])\le4d.
\]
By (BD), \(G[L]\) can be colored using
\[
B=O_r\!\left(\frac{d\log\log d}{\log d}\right)
\]
colors. One color class \(I\) therefore has
\[
|I|\ge\frac{|S|}{2B}.
\]
Since every vertex of \(I\) has weight greater than \(a\), while
\[
w(S)\le2a|S|,
\]
we obtain
\[
w(I)\ge \frac{w(S)}{4B}.
\]
Dual feasibility gives \(w(I)\le1\), and hence \(w(S)\le4B\). Summing over the \(q(w)\) classes proves (4.1). \(\square\)

Consequently, if \(w\) has total weight at least \(\varepsilon d\), then
\[
q(w)
 =\Omega_{r,\varepsilon}\!\left(
 \frac{\log d}{\log\log d}
 \right).
\tag{4.2}
\]
In particular,
\[
\frac{\max_v w_v}{\min\{w_v:w_v>0\}}
 \ge
 \exp\!\left(
 \Omega_{r,\varepsilon}
 \left(\frac{\log d}{\log\log d}\right)
 \right).
\tag{4.3}
\]

Thus any dual witness to a linear counterexample must have an enormous dynamic range. The conjecture is true for every family for which some optimal dual solution has
\[
q(w)=o\!\left(\frac{\log d}{\log\log d}\right).
\]

---

## 5. A high-degree special case using the triangle-free theorem

The following special case is not covered by bounded maximum degree.

Let \(Q\) be an \((r-3)\)-clique of a \(K_r\)-free graph \(G\), and define its common neighborhood
\[
X=N(Q)=\{v\notin Q:vq\in E(G)\text{ for every }q\in Q\}.
\]
Then \(G[X]\) is triangle-free: a triangle in \(X\), together with \(Q\), would form a \(K_r\).

Let
\[
R=V(G)\setminus X,
\qquad
d_R=\operatorname{dgn}(G[R]).
\]
By subadditivity and (TF),
\[
\begin{aligned}
\chi_f(G)
 &\le \chi_f(G[X])+\chi_f(G[R])\\
 &\le F_3(d)+d_R+1\\
 &\le (4+o(1))\frac d{\log d}+d_R+1.
\end{aligned}
\tag{5.1}
\]

Therefore the conjecture holds whenever \(G\) has an \((r-3)\)-clique \(Q\) for which
\[
\operatorname{dgn}(G[V\setminus N(Q)])=o(d).
\tag{5.2}
\]
In particular, it holds if all but \(o(d)\) vertices lie in \(N(Q)\).

A concrete extreme case is a dominating \((r-3)\)-clique. Then \(G-Q\) is triangle-free, so
\[
\chi_f(G)=O_r\!\left(\frac d{\log d}\right).
\]
For \(r=4\), this says that every \(K_4\)-free \(d\)-degenerate graph with a dominating vertex satisfies the desired sublinear bound, even though that vertex may have arbitrarily large degree.

More generally, if \(V(G)\) can be partitioned into \(t=o(\log d)\) triangle-free induced subgraphs and a remainder of degeneracy \(o(d)\), then repeated use of (TF) gives \(\chi_f(G)=o(d)\).

---

## 6. The remaining local-to-global gap

Let \(w\) be dual-feasible, and let \(Q\) be a \(q\)-clique, \(q\le r-3\). Since \(G[N(Q)]\) is \(K_{r-q}\)-free and \(d\)-degenerate,
\[
w(N(Q))
 \le \chi_f(G[N(Q)])
 \le F_{r-q}(d).
\tag{6.1}
\]
For \(q=r-3\), the triangle-free theorem gives
\[
w(N(Q))
 \le (4+o(1))\frac d{\log d}.
\tag{6.2}
\]
In particular, for \(r=4\), every dual-feasible weighting satisfies
\[
w(N(v))=O\!\left(\frac d{\log d}\right)
\qquad\text{for every }v.
\]

This is exactly the tempting induction point, but it does not control the total dual weight. Numerically small neighborhood mass alone is insufficient. For example, take \(m\) disjoint copies of a graph \(H\), and put \(w_0/m\) on each copy, where \(w_0\) is dual-feasible on \(H\). The resulting weighting remains dual-feasible, has the same total weight as \(w_0\), but every weighted neighborhood has mass \(O(1/m)\). Thus a successful argument must use more than the separate inequalities (6.1); it must coordinate the neighborhood fractional colorings or exploit an irreducible global structure.

The unresolved case is therefore a graph with all of the following features:

- maximum degree at least on the order of \(d\log d/\log\log d\);
- a high-degree peeling hierarchy of length \(\Omega(\log d/\log\log d)\);
- optimal dual weights occupying \(\Omega(\log d/\log\log d)\) dyadic scales;
- no \((r-3)\)-clique with a low-degeneracy residual outside its common neighborhood;
- the same obstruction recurring in induced subgraphs at every intermediate degeneracy scale.

The arguments above do not rule out such graphs, and hence do not resolve the conjecture.