```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a uniform high-probability obstruction to low-defect random alterations, but do not close the Ramsey logarithmic gap.",
  "would_publish": false,
  "caveats": "No unrestricted Ramsey bound is improved; rare successful outcomes and the full random-greedy process are not ruled out."
}
```

# A partial result: low-defect random alterations cannot typically reach the conjectured scale

I do not prove or disprove the conjecture. The rigorous result below concerns a natural family of probabilistic constructions, without imposing the parity condition from the previous attempt.

In particular, consider sampling triples independently and then deleting **every triple belonging to an initially present** \(K_{4-e}^{(3)}\). I prove that, with high probability, the resulting hypergraph has a blue star with
\[
\Omega(\sqrt N\log N)
\]
leaves, **simultaneously for every choice of the sampling density**.

More generally, retaining only triples that initially belong to at most \(k\) forbidden four-sets cannot typically produce the conjectured construction when \(k=o(\log N)\).

This is a limitation on high-probability construction arguments of this particular type, not an existential obstruction to the conjecture.

Throughout, logarithms are natural.

## 1. Reformulation and the required density

Let \(H\) be the red hypergraph, and write
\[
L_H(v)=\{xy:vxy\in E(H)\},\qquad
A(H)=\max_{v\in V(H)}\alpha(L_H(v)).
\]

The following facts, also used in the previous attempt, are checked directly.

* \(H\) is \(K_{4-e}^{(3)}\)-free exactly when every link is triangle-free: three triples on four vertices have a common vertex.
* The blue complement contains \(S_n^{(3)}\) exactly when \(A(H)\ge n\).
* For every pair \(x,y\), its red neighborhood
  \[
  N_H(xy)=\{z:xyz\in E(H)\}
  \]
  is independent in \(L_H(x)\). Consequently,
  \[
  d_H(xy)\le A(H). \tag{1}
  \]

Thus the missing lower bound asks, up to constants, for \(K_{4-e}^{(3)}\)-free hypergraphs on \(N\) vertices with
\[
A(H)=O(\sqrt{N\log N}). \tag{2}
\]

I will need an elementary triangle-free independence bound. A proof is included to make the probabilistic obstruction self-contained.

### Lemma 1

If \(G\) is triangle-free, has \(m\) vertices, and has maximum degree at most \(D\ge2\), then
\[
\alpha(G)\ge \frac{m\log D}{8(\log 2)D}. \tag{3}
\]

#### Proof

Choose an independent set \(I\) uniformly from all independent sets of \(G\). Put
\[
\rho=\frac{\mathbb E|I|}{m}.
\]

For a vertex \(v\), condition on \(I\setminus N[v]\). Let \(K_v\) be the number of neighbors of \(v\) having no neighbor in this conditioned independent set.

Because \(G\) is triangle-free, \(N(v)\) is independent. Conditional on the outside configuration, the possibilities inside \(N[v]\) are:

* the singleton \(\{v\}\);
* any subset of the \(K_v\) available neighbors.

Hence
\[
\Pr(v\in I\mid I\setminus N[v])=\frac1{1+2^{K_v}}
\ge \frac12\,2^{-K_v},
\]
and
\[
\mathbb E(|I\cap N(v)|\mid I\setminus N[v])
=\frac{K_v2^{K_v-1}}{1+2^{K_v}}
\ge \frac{K_v}{4}.
\]

Averaging over vertices gives
\[
\frac1m\sum_v\mathbb E K_v
\le \frac4m\sum_u d(u)\Pr(u\in I)
\le4D\rho.
\]
Jensen's inequality therefore yields
\[
\rho\ge \frac12\exp(-4(\log2)D\rho). \tag{4}
\]

If \(\rho<\log D/(8(\log2)D)\), the right side of (4) exceeds
\(\tfrac12D^{-1/2}\), which is larger than
\(\log D/(8(\log2)D)\) for \(D\ge2\). This is a contradiction. Finally,
\(\alpha(G)\ge\mathbb E|I|=m\rho\). ∎

Deleting vertices of degree greater than twice the average degree gives the useful corollary
\[
\alpha(G)\ge
\frac{m\log(2d)}{32(\log2)d}
\qquad(d\ge1), \tag{5}
\]
where \(d\) is the average degree of a triangle-free graph. For \(d<1\), the simpler bound \(\alpha(G)\ge m/2\) suffices.

As a check, (1) and Lemma 1 immediately recover
\[
r(K_{4-e}^{(3)},S_n^{(3)})=O(n^2/\log n).
\]

There is also a necessary global density condition.

### Proposition 2

For every fixed \(C>0\), any \(K_{4-e}^{(3)}\)-free \(H\) on \(N\) vertices satisfying
\[
A(H)\le C\sqrt{N\log N}
\]
must, for sufficiently large \(N\), satisfy
\[
c_C N^{5/2}\sqrt{\log N}
\le |E(H)|
\le \frac C6 N^{5/2}\sqrt{\log N}. \tag{6}
\]

#### Proof

The upper bound follows from (1):
\[
3|E(H)|=\sum_{xy}d_H(xy)
\le \binom N2 A(H).
\]

For the lower bound, put
\[
d=\frac{6|E(H)|}{N(N-1)}.
\]
Some link has average degree at most \(d\).

If \(d\le\sqrt N\), delete from that link the vertices of degree greater than \(2\sqrt N\). At least half remain, and Lemma 1 gives
\[
A(H)\ge c\sqrt N\log N,
\]
contrary to the assumed bound for sufficiently large \(N\).

Thus \(d>\sqrt N\). Deleting vertices of degree greater than \(2d\) and applying Lemma 1 now gives
\[
A(H)\ge
\frac{(N-1)\log(2d)}{32(\log2)d}
\ge
\frac{(N-1)\log N}{64(\log2)d}.
\]
The assumed upper bound on \(A(H)\) forces
\(d\ge c_C\sqrt{N\log N}\), proving (6). ∎

Thus a conjecture-scale construction needs red density of order
\(\sqrt{\log N/N}\), not merely \(N^{-1/2}\).

## 2. The random alteration model

Assign independent uniform labels \(T_e\in[0,1]\) to all triples \(e\in\binom{[N]}3\), and set
\[
G_p=\{e:T_e\le p\},\qquad 0\le p\le1.
\]

For \(e=\{a,b,c\}\), define its **initial defect**
\[
D_p(e)=
\left|\left\{x\notin e:
\text{at least two of }abx,acx,bcx\text{ belong to }G_p
\right\}\right|.
\]
If \(e\in G_p\), this counts the four-sets on which \(e\) belongs to an initially present \(K_{4-e}^{(3)}\). A four-set with all four triples present is counted once.

Define
\[
F_{p,k}=\{e\in G_p:D_p(e)\le k\}. \tag{7}
\]

For \(k=0\), \(F_{p,0}\) is exactly the result of deleting every triple belonging to any initial forbidden configuration. It is automatically \(K_{4-e}^{(3)}\)-free.

For \(k>0\), \(F_{p,k}\) need not be \(K_{4-e}^{(3)}\)-free; we allow any \(K_{4-e}^{(3)}\)-free subhypergraph of it.

### Theorem 3: uniform low-defect bound

There are absolute constants \(c,C_1>0\) such that, with probability at least
\[
1-C_1\frac{(\log N)^2}{N},
\]
the following holds simultaneously for every \(p\in[0,1]\), every integer \(0\le k\le N-3\), and every \(K_{4-e}^{(3)}\)-free \(H\subseteq F_{p,k}\):
\[
A(H)\ge
c\sqrt{\frac{N}{k+1}}\log N. \tag{8}
\]

The uniformity includes choosing \(p\) after seeing all the random labels.

### 2.1. A binomial estimate

For \(B\sim\operatorname{Bin}(m,t)\), integration of its probability-generating function gives
\[
\mathbb E\frac1{B+1}
=\frac{1-(1-t)^{m+1}}{(m+1)t}
\le\frac1{(m+1)t}.
\]
Therefore
\[
\Pr(B\le k)
\le
\min\left\{1,\frac{k+1}{(m+1)t}\right\}. \tag{9}
\]

For a fixed triple \(e\),
\[
D_q(e)\sim\operatorname{Bin}(N-3,t(q)),
\qquad
t(q)=3q^2-2q^3\ge q^2.
\]
In particular, (9) implies
\[
q\,\Pr\bigl(\operatorname{Bin}(m,t(q))\le k\bigr)
\le \sqrt{\frac{k+1}{m+1}}. \tag{10}
\]

### 2.2. Counting low-defect triples

For \(0<q\le1/2\), let
\[
Y(q,k)=
\left|\{e:T_e\le2q,\ D_q(e)\le k\}\right|.
\]
The label \(T_e\) is independent of \(D_q(e)\), so (10) gives
\[
\mathbb E Y(q,k)
\le
2\binom N3\sqrt{\frac{k+1}{N-2}}
\le \sqrt{k+1}\,N^{5/2} \tag{11}
\]
for \(N\ge10\).

We next establish
\[
\operatorname{Var}Y(q,k)\le3(k+1)N^4. \tag{12}
\]

Write \(Y(q,k)=\sum_e X_e\).

* If \(e\cap f=\varnothing\), then \(X_e,X_f\) are independent. Indeed, \(X_e\) depends only on labels of triples meeting \(e\) in at least two vertices, and no triple can meet two disjoint triples in at least two vertices each.

* Suppose \(|e\cap f|=1\). Restrict the defect counts to extension vertices outside \(e\cup f\). These two restricted counts are independent copies of
  \(\operatorname{Bin}(N-5,t(q))\), and are independent of \(T_e,T_f\). Consequently,
  \[
  \mathbb E(X_eX_f)
  \le
  (2q)^2
  \Pr\bigl(\operatorname{Bin}(N-5,t(q))\le k\bigr)^2
  \le\frac{4(k+1)}{N-4}. \tag{13}
  \]

* If \(|e\cap f|=2\), use the bound \(\mathbb E(X_eX_f)\le1\).

There are at most \(N^5/4\) ordered pairs of distinct triples intersecting in one vertex, and at most \(N^4/2\) intersecting in two vertices. Adding the diagonal terms proves (12).

By (11), (12), and Chebyshev's inequality,
\[
\Pr\left(Y(q,k)>2\sqrt{k+1}\,N^{5/2}\right)
\le\frac3N. \tag{14}
\]

To make this uniform, take
\[
q_j=2^{-j},
\qquad
1\le j\le \left\lceil4\log_2N\right\rceil,
\]
and
\[
k_\ell=2^\ell-1,
\qquad
0\le\ell\le\left\lceil\log_2(N-2)\right\rceil.
\]
There are \(O((\log N)^2)\) pairs of grid parameters, so a union bound applies to (14).

At the smallest density \(q_{\min}\le N^{-4}\),
\[
\Pr(G_{q_{\min}}\ne\varnothing)
\le\binom N3q_{\min}=O(N^{-1}).
\]

Now let \(p\ge q_{\min}\), and choose \(q_j\le p\le2q_j\). Choose \(k_\ell\ge k\) with \(k_\ell+1\le2(k+1)\). Monotonicity of the defect counts gives
\[
F_{p,k}\subseteq
\{e:T_e\le2q_j,\ D_{q_j}(e)\le k_\ell\}.
\]
It follows that, on the common high-probability event,
\[
|F_{p,k}|
\le 2\sqrt{2(k+1)}\,N^{5/2}
\le3\sqrt{k+1}\,N^{5/2} \tag{15}
\]
for every \(p,k\). For \(p<q_{\min}\), the same assertion follows from \(G_{q_{\min}}=\varnothing\).

### 2.3. From edge count to a blue star

Let \(H\subseteq F_{p,k}\) be \(K_{4-e}^{(3)}\)-free. By (15),
\[
\frac1N\sum_v
\frac{2|E(L_H(v))|}{N-1}
=
\frac{6|E(H)|}{N(N-1)}
\le C_2\sqrt{(k+1)N}.
\]
Choose a link whose average degree is at most the right-hand side.

Delete from that link all vertices of degree greater than
\(2C_2\sqrt{(k+1)N}\). At least half its vertices remain. Applying Lemma 1 to the remaining triangle-free graph yields
\[
\alpha(L_H(v))
\ge
c\frac{N\log N}{\sqrt{(k+1)N}},
\]
which is (8). This proves Theorem 3. ∎

## 3. Consequences for the conjecture

### 3.1. One-round cleaning has a logarithmic-square ceiling in probability

Taking \(k=0\) in Theorem 3 gives, with high probability,
\[
A(F_{p,0})\ge c\sqrt N\log N
\qquad\text{for every }p\in[0,1]. \tag{16}
\]

Thus this particular sampling-and-cleaning procedure cannot typically avoid a blue \(S_n^{(3)}\) once
\[
N\ge C\frac{n^2}{\log^2 n}
\]
for a sufficiently large absolute \(C\).

The elementary first-moment calculation already points toward this obstruction:
\[
\mathbb E|F_{p,0}|
=
\binom N3 p(1-3p^2+2p^3)^{N-3}. \tag{17}
\]
The maximum retained density in (17) is
\[
(1+o(1))(6eN)^{-1/2}.
\]
Indeed, its interior maximizer satisfies
\[
(6N-16)p^2-p-1=0.
\]
The variance and discretization argument above supplies the uniform high-probability statement that the first moment alone does not provide.

### 3.2. Allowing \(o(\log N)\) initial defects still does not suffice

If \(k=o(\log N)\), then (8) gives
\[
A(H)\ge
c\sqrt{N\log N}
\sqrt{\frac{\log N}{k+1}}
=
\omega(\sqrt{N\log N}).
\]
Therefore no \(K_{4-e}^{(3)}\)-free subgraph formed solely from these low-defect triples can typically satisfy the conjecture-scale requirement (2).

There is also a quantitative version. Suppose a successful subgraph
\(H\subseteq G_p\) satisfies
\[
A(H)\le C\sqrt{N\log N}.
\]
Combining Proposition 2 with (15) gives
\[
\frac{|\{e\in E(H):D_p(e)\le k\}|}{|E(H)|}
\le
O_C\left(\sqrt{\frac{k+1}{\log N}}\right). \tag{18}
\]
Thus, for every \(k=o(\log N)\), only an \(o(1)\) proportion of the red triples of such a successful subgraph can have initial defect at most \(k\).

In other words, a successful alteration at the conjectured scale must generally **retain triples involved in many initial forbidden configurations and eliminate their conflicting partners**, rather than simply discard the initially troublesome triples.

## 4. What is still missing

The argument does **not** rule out the \(K_{4-e}^{(3)}\)-free process. That process may retain a triple with many potential initial conflicts because the conflicting triples are never selected. Theorem 3 does not control this adaptive mechanism.

Nor is a high-probability failure an existential impossibility: exceptionally rare samples can evade the estimates above. Hence this result cannot disprove the Ramsey conjecture or exclude a rare-event existence argument.

The unrestricted bounds quoted in the question remain unchanged by this work:
\[
c\frac{n^2}{\log^2 n}
\le r(K_{4-e}^{(3)},S_n^{(3)})
\le c'\frac{n^2}{\log n}.
\]
What remains unproved here is the simultaneous construction of triangle-free links with independence number \(O(\sqrt{N\log N})\), subject to triple consistency. The result above rigorously identifies one limitation of simpler random alterations, but does not supply the uniform star-hitting estimate needed for the full conjectured lower bound.