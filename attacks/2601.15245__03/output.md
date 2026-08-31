```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but one obtains n >= d^{(r-1)/(r-2)} log d exp(Ω_r(log d/log log d)), and the desired exponential bound holds whenever the vertices are covered by O_r(1) triangle-free induced subgraphs.",
  "would_publish": false,
  "caveats": "The exponential bound is not proved in general; the quantitative partial result uses the standard fixed-clique maximum-degree coloring theorem and is not claimed to be new."
}
```

# 1. Statement and status

Fix \(r\ge 4\). The problem asks whether there is \(c_r>0\) such that every \(K_r\)-free \(d\)-degenerate graph \(G\) satisfying
\[
\chi(G)=d+1
\]
has
\[
|V(G)|\ge \exp(c_r d).
\]

I do not prove this. I give:

1. an unconditional lower bound stronger than the direct Ramsey lower bound by a subpolynomial factor;
2. a sufficient condition under which the desired exponential bound follows from the triangle-free theorem in the source paper;
3. structural constraints on a critical counterexample.

All logarithms below are natural, and \(r\) is fixed.

# 2. A high-degree peeling lemma

For a hereditary graph class \(\mathcal C\), define
\[
\Phi_{\mathcal C}(D)
  =\max\{\chi(H):H\in\mathcal C,\ \Delta(H)\le D\}
\]
and
\[
m_{\mathcal C}(k)
  =\min\{|V(H)|:H\in\mathcal C,\ \chi(H)\ge k\}.
\]

## Lemma 2.1

Let \(G\in\mathcal C\) be \(d\)-degenerate with \(\chi(G)=d+1\). For every fixed \(A>2\), put
\[
F=\Phi_{\mathcal C}(\lceil Ad\rceil),
\qquad
t=\left\lfloor\frac{d}{2F}\right\rfloor.
\]
Then
\[
|V(G)|\ge \left(\frac A2\right)^t
m_{\mathcal C}\!\left(\left\lceil\frac d2\right\rceil\right).
\]

### Proof

Set \(S_0=V(G)\). Recursively define
\[
L_i=\{v\in S_i:\deg_{G[S_i]}(v)\le Ad\},
\qquad
S_{i+1}=S_i\setminus L_i.
\]

Because every induced subgraph of \(G\) is \(d\)-degenerate,
\[
e(G[S_i])\le d|S_i|.
\]
Every vertex of \(S_{i+1}\) has degree greater than \(Ad\) in \(G[S_i]\), and hence
\[
Ad\,|S_{i+1}|
 <\sum_{v\in S_{i+1}}\deg_{G[S_i]}(v)
 \le 2e(G[S_i])
 \le 2d|S_i|.
\]
Therefore
\[
|S_{i+1}|<\frac2A|S_i|.
\]
Iterating,
\[
|V(G)|>\left(\frac A2\right)^t|S_t|.
\]

Moreover, \(G[L_i]\) has maximum degree at most \(Ad\), so
\[
\chi(G[L_i])\le F.
\]
Using disjoint palettes on \(L_0,\dots,L_{t-1},S_t\),
\[
\chi(G)\le \sum_{i=0}^{t-1}\chi(G[L_i])+\chi(G[S_t])
          \le tF+\chi(G[S_t]).
\]
Since \(tF\le d/2\) and \(\chi(G)=d+1\),
\[
\chi(G[S_t])\ge \frac d2+1.
\]
Thus
\[
|S_t|\ge m_{\mathcal C}\!\left(\left\lceil\frac d2\right\rceil\right),
\]
which proves the lemma. \(\square\)

# 3. Application to \(K_r\)-free graphs

I use the standard fixed-clique maximum-degree coloring theorem in the form
\[
\Phi_r(D)
 :=\max\{\chi(H):H\text{ is }K_r\text{-free},\ \Delta(H)\le D\}
 \le C_r\frac{D\log\log D}{\log D}
\]
for sufficiently large \(D\). The exact best constant is irrelevant.

Taking \(A=4\) in Lemma 2.1 gives
\[
t=\left\lfloor\frac{d}{2\Phi_r(4d)}\right\rfloor
  =\Omega_r\!\left(\frac{\log d}{\log\log d}\right),
\]
and hence
\[
|V(G)|\ge
\exp\!\left(\Omega_r\!\left(\frac{\log d}{\log\log d}\right)\right)
m_r(\lceil d/2\rceil).
\]

It remains to insert a general Ramsey lower bound on \(m_r(k)\).

## Lemma 3.1

For fixed \(r\ge3\),
\[
m_r(k)\ge c_r k^{(r-1)/(r-2)}\log k
\]
for sufficiently large \(k\).

### Justification

The classical off-diagonal Ramsey estimate
\[
R(r,s)\le C_r\frac{s^{r-1}}{(\log s)^{r-2}}
\]
implies that every \(K_r\)-free graph on \(N\) vertices contains an independent set of size at least
\[
c_r N^{1/(r-1)}
(\log N)^{(r-2)/(r-1)}.
\]
Applying this estimate successively to induced subgraphs gives
\[
\chi(H)\le
C_r\left(\frac{|V(H)|}{\log |V(H)|}\right)^{(r-2)/(r-1)}.
\]
Inverting this inequality yields the displayed lower bound for \(m_r(k)\).

If one wants to avoid the logarithmically improved Ramsey estimate, the elementary bound
\[
R(r,s)\le \binom{r+s-2}{r-1}
\]
still gives \(m_r(k)=\Omega_r(k^{(r-1)/(r-2)})\).

Combining Lemmas 2.1 and 3.1 gives the following partial result.

## Theorem 3.2

For every fixed \(r\ge4\), every \(K_r\)-free \(d\)-degenerate graph \(G\) with \(\chi(G)=d+1\) satisfies
\[
\boxed{
|V(G)|
 \ge
 c_r d^{(r-1)/(r-2)}\log d\,
 \exp\!\left(
   c'_r\frac{\log d}{\log\log d}
 \right)
}
\]
for sufficiently large \(d\).

This is still \(e^{o(d)}\), so it is far from the conjectured bound.

The proof also gives a structural conclusion: a putative small counterexample contains a nested sequence
\[
V(G)=S_0\supset S_1\supset\cdots\supset S_t,
\qquad
t=\Omega_r\!\left(\frac{\log d}{\log\log d}\right),
\]
such that every vertex of \(S_{i+1}\) has more than \(4d\) neighbors in \(S_i\), while
\[
\chi(G[S_t])\ge d/2.
\]

# 4. A special case giving the conjectured exponential bound

The quantitative triangle-free result from the source paper has the following immediate consequence.

## Lemma 4.1

For every \(\eta>0\), there is \(c_\eta>0\) such that any triangle-free \(D\)-degenerate graph \(T\) satisfying
\[
\chi(T)\ge \eta D
\]
has
\[
|V(T)|\ge \exp(c_\eta D).
\]

### Proof

The source theorem gives, in the relevant range,
\[
\chi(T)\le
C\frac{D}{\log(D/\log |V(T)|)}.
\]
If \(\log |V(T)|\le cD\), then
\[
\log\!\left(\frac{D}{\log |V(T)|}\right)
 \ge \log(1/c).
\]
Choosing \(c>0\) sufficiently small in terms of \(\eta\) makes the right-hand side of the coloring bound strictly less than \(\eta D\), a contradiction. \(\square\)

This yields a useful sufficient condition.

## Proposition 4.2

Let \(G\) be \(d\)-degenerate with \(\chi(G)=d+1\). If \(G\) contains a triangle-free subgraph \(T\) with
\[
\chi(T)\ge \varepsilon d
\]
for some fixed \(\varepsilon>0\), then
\[
|V(G)|\ge \exp(c_\varepsilon d).
\]

### Proof

Let \(D\) be the degeneracy of \(T\). Then
\[
D\le d
\]
and
\[
D\ge \chi(T)-1\ge \varepsilon d-1.
\]
Moreover,
\[
\chi(T)\ge\varepsilon d\ge\varepsilon D.
\]
Lemma 4.1 therefore gives
\[
|V(G)|\ge |V(T)|\ge \exp(c_\varepsilon D)
          \ge \exp(c'_\varepsilon d).
\]
\(\square\)

Two concrete consequences are worth recording.

### Corollary 4.3: bounded triangle-free partition number

Suppose \(V(G)\) can be covered by \(s\) sets, each inducing a triangle-free graph, where \(s\) is fixed. Then
\[
|V(G)|\ge \exp(c_s d).
\]

Indeed, after assigning every vertex to one of the covering sets, obtain a partition
\[
V(G)=V_1\cup\cdots\cup V_s
\]
with every \(G[V_i]\) triangle-free. Since disjoint palettes give
\[
\chi(G)\le\sum_{i=1}^s\chi(G[V_i]),
\]
some part satisfies
\[
\chi(G[V_i])\ge\frac{d+1}{s}.
\]
Proposition 4.2 applies with \(\varepsilon=1/s\).

Thus the original conjecture holds for every family of \(K_r\)-free graphs whose vertices can be covered by \(O_r(1)\) triangle-free induced subgraphs.

### Corollary 4.4: small triangle transversal

Suppose there is \(X\subseteq V(G)\) meeting every triangle and
\[
\chi(G[X])\le(1-\varepsilon)d.
\]
Then \(G-X\) is triangle-free and
\[
\chi(G-X)
 \ge\chi(G)-\chi(G[X])
 \ge\varepsilon d+1.
\]
Consequently,
\[
|V(G)|\ge\exp(c_\varepsilon d).
\]

In particular, it suffices that every triangle can be hit by at most \((1-\varepsilon)d\) vertices.

# 5. Structure of a critical obstruction

The exact equality \(\chi=d+1\) and degeneracy \(d\) imposes a strong color-forcing condition.

## Lemma 5.1: rainbow neighborhood

Let \(H\) be a \((d+1)\)-critical subgraph of \(G\). Then \(H\) contains a vertex \(v\) of degree exactly \(d\). For every proper \(d\)-coloring \(\varphi\) of \(H-v\), the \(d\) vertices of \(N_H(v)\) receive all \(d\) colors exactly once.

### Proof

Criticality gives \(\delta(H)\ge d\). Since \(H\) is \(d\)-degenerate, it has a vertex of degree at most \(d\), hence exactly \(d\).

Also \(\chi(H-v)=d\): it is at most \(d\) by criticality, while if it were at most \(d-1\), one could color \(v\) with one additional color and obtain a \(d\)-coloring of \(H\).

If a color were absent from \(N(v)\), it could be assigned to \(v\). Thus all \(d\) colors occur in \(N(v)\), and because \(|N(v)|=d\), each occurs once. \(\square\)

Write \(x_i\) for the neighbor of \(v\) receiving color \(i\).

## Lemma 5.2: multicolor connectivity

For every set \(I\subseteq[d]\) with \(|I|\ge2\), the vertices
\[
\{x_i:i\in I\}
\]
all lie in one connected component of
\[
(H-v)[\varphi^{-1}(I)].
\]

### Proof

Suppose a component \(C\) contains a nonempty proper subset of these distinguished vertices. Choose \(a\in I\) with \(x_a\in C\) and \(b\in I\) with \(x_b\notin C\). Interchange colors \(a\) and \(b\) on every vertex of \(C\).

This remains a proper coloring: no vertex of \(C\) has a neighbor outside \(C\) whose color lies in \(I\), since \(C\) is a component of the subgraph induced by colors \(I\). After the interchange, both \(x_a\) and \(x_b\) have color \(b\), and no neighbor of \(v\) has color \(a\). Hence \(v\) can be colored \(a\), contradicting \(\chi(H)=d+1\). \(\square\)

Taking \(|I|=2\), every pair \(x_i,x_j\) is connected by an \(i,j\)-bichromatic path.

## Corollary 5.3: a local edge count

If \(H\) is also \(K_r\)-free, then
\[
|V(H)|\ge d\left(1+\frac1{r-2}\right).
\]

### Proof

The graph \(H[N(v)]\) is \(K_{r-1}\)-free. Let \(M\) denote the number of nonedges in \(N(v)\). Turán's theorem gives
\[
M
 \ge \binom d2-
 \left(1-\frac1{r-2}\right)\frac{d^2}{2}.
\]

For each pair \(i<j\), the bichromatic graph on colors \(i,j\) connects \(x_i\) to \(x_j\). It contains at least one edge if \(x_ix_j\in E(H)\), and at least three edges otherwise. Edges belonging to different color pairs are disjoint. Consequently,
\[
e(H-v)\ge \binom d2+2M,
\]
and therefore
\[
e(H)\ge d+\binom d2+2M
       \ge \binom d2+\frac{d^2}{r-2}.
\]

If \(h=|V(H)|\), the exact extremal edge bound for a \(d\)-degenerate graph is
\[
e(H)\le dh-\binom{d+1}{2}.
\]
Combining the two estimates,
\[
dh
 \ge \binom{d+1}{2}+\binom d2+\frac{d^2}{r-2}
 =d^2+\frac{d^2}{r-2}.
\]
Division by \(d\) proves the claim. \(\square\)

This local bound is asymptotically weaker than the Ramsey lower bound, but it records a genuine constraint: a low-degree vertex of a critical obstruction has a \(K_{r-1}\)-free neighborhood which is forced to be rainbow in every \(d\)-coloring of the rest of the graph.

# 6. Why these arguments stop short of the conjecture

The peeling lemma loses a separate palette on every low-degree layer. The best general fixed-clique maximum-degree bound colors such a layer with roughly
\[
d\frac{\log\log d}{\log d}
\]
colors. Thus only
\[
O_r\!\left(\frac{\log d}{\log\log d}\right)
\]
multiplicative shrinking steps can be taken before \(d\) colors are exhausted. This inherently produces only the factor
\[
\exp\!\left(
 O_r\!\left(\frac{\log d}{\log\log d}\right)
\right),
\]
not \(\exp(\Omega_r(d))\).

The triangle-free carrier proposition would settle the problem if every such \(K_r\)-free critical graph had a triangle-free subgraph of chromatic number \(\Omega_r(d)\), or a bounded partition into triangle-free induced subgraphs. I do not know how to derive either conclusion from \(K_r\)-freeness and degeneracy, and no such assertion is used as an unproved step.

Finally, the rainbow-neighborhood condition yields pairwise bichromatic connectivity, but this alone requires only \(O(d^2)\) witness edges. It does not provide the exponentially many essentially disjoint witnesses needed for the conjectured order bound.

Thus the general \(r\ge4\) problem remains unresolved.