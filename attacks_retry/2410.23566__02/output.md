```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the sharp asymptotic factor 2^k for trees with any fixed number of non-leaf vertices, but leave the unrestricted infimum undetermined.",
  "would_publish": false,
  "caveats": "Both k and the non-leaf core bound are fixed as n grows; novelty of this restricted result has not been checked."
}
```

# 1. A sharp bounded-core result

Containment below is **non-induced**. For an acyclic digraph \(D\), let \(u(D)\) be the smallest integer \(N\) such that every tournament on \(N\) vertices contains \(D\).

For an undirected tree \(T\), call its vertices of degree at least two its **non-leaf core**. Define
\[
U_{k,r}(n):=
\max\left\{
u(\vec T[k]):
|V(T)|=n,\ 
T\text{ has at most }r\text{ non-leaf vertices}
\right\},
\]
where the maximum includes all orientations of the eligible trees.

The following is the partial result.

## Theorem
For every fixed pair of positive integers \(k,r\),
\[
\boxed{\lim_{n\to\infty}\frac{U_{k,r}(n)}{kn}=2^k.}
\tag{1}
\]

Equivalently, for every \(\varepsilon>0\), every sufficiently large tournament of order at least
\[
(2^k+\varepsilon)kn
\]
contains the \(k\)-blow-up of every \(n\)-vertex oriented tree with at most \(r\) non-leaf vertices.

In particular:

- this covers **every orientation of a star**, not just out-stars and in-stars;
- it covers arbitrary orientations of any fixed-size core with arbitrarily many pendant leaves;
- the infimum of the base for each such restricted family is \(2\), with the large-\(n\) threshold allowed to depend on \(k,r\).

The unrestricted problem is not resolved. The proof below genuinely uses that the core size is fixed.

---

# 2. The lower bound: checking the out-star obstruction

The random-tournament obstruction from the supplied attempt is valid; here is an independent derivation.

Let \(\vec S_n^+\) be the out-star on \(n\) vertices, and put
\[
L=k(n-1).
\]
Its \(k\)-blow-up is contained in a tournament precisely when some \(k\)-set has at least \(L\) common out-neighbours.

Fix \(0<\theta<1\), and take a uniformly random tournament on
\[
N=\left\lfloor(1-\theta)2^kL\right\rfloor
\]
vertices. For each fixed \(k\)-set \(X\),
\[
|N^+(X)|\sim \operatorname{Bin}(N-k,2^{-k}),
\]
with mean at most \((1-\theta)L\). A Chernoff bound gives
\[
\Pr\bigl(|N^+(X)|\ge L\bigr)
\le \exp(-\theta^2L/2).
\]
Consequently,
\[
\Pr\bigl(\exists X:\ |N^+(X)|\ge L\bigr)
\le N^k\exp(-\theta^2L/2)=o(1)
\]
as \(L\to\infty\), with \(k,\theta\) fixed. Thus
\[
u(\vec S_n^+[k])\ge (2^k-o(1))k(n-1).
\tag{2}
\]

There is also a particularly simple matching upper bound:
\[
u(\vec S_n^+[k])\le 2^kL.
\tag{3}
\]
Indeed, in a tournament on \(M\) vertices some vertex has at least \(\lfloor M/2\rfloor\) out-neighbours. Starting with \(2^kL\) vertices, select a vertex and restrict to its out-neighbourhood, repeating \(k\) times. The \(k\) selected vertices have at least \(L\) common out-neighbours.

Since out-stars belong to the family defining \(U_{k,r}(n)\) for every \(r\ge1\), (2) proves the lower bound in (1). It also gives the unrestricted necessary condition
\[
\boxed{C\ge2.}
\]

The remainder proves the upper bound in (1).

---

# 3. A weighted tournament-density lemma

We first isolate the elementary inequality that selects a suitable location for the core.

## Lemma 1
Let \(w_1,\dots,w_t>0\), let \(W=\sum_iw_i\), and suppose
\[
d_{ij}\in[0,1],\qquad
d_{ij}+d_{ji}=1,\qquad d_{ii}=\frac12.
\]
Fix \(k\ge1\), and write \(\rho=2^{-k}\). Define
\[
f_i^+=\sum_jw_jd_{ij}^{\,k},
\qquad
f_i^-=\sum_jw_j(1-d_{ij})^{\,k}.
\]
If \(a,b\ge0\) and
\[
a+b<\rho W,
\tag{4}
\]
then some index \(i\) satisfies
\[
f_i^-\ge a,\qquad f_i^+\ge b.
\]

### Proof
Suppose otherwise. Partition the indices into
\[
I_-=\{i:f_i^-<a\},
\qquad I_+=\{1,\dots,t\}\setminus I_-.
\]
Every index in \(I_+\) then satisfies \(f_i^+<b\).

Put \(W_-=\sum_{i\in I_-}w_i\). If \(W_->0\), convexity gives
\[
\begin{aligned}
\sum_{i\in I_-}w_if_i^-
&\ge
\sum_{i,j\in I_-}w_iw_j(1-d_{ij})^k\\
&\ge
W_-^2
\left(
\frac{\sum_{i,j\in I_-}w_iw_j(1-d_{ij})}{W_-^2}
\right)^k\\
&=\rho W_-^2.
\end{aligned}
\]
The last equality follows from \(d_{ij}+d_{ji}=1\), including the diagonal convention. On the other hand, the same sum is less than \(aW_-\). Hence \(W_-\le a/\rho\), also valid when \(W_-=0\).

Similarly, \(W_+\le b/\rho\). Therefore
\[
W=W_-+W_+\le\frac{a+b}{\rho}<W,
\]
a contradiction. ∎

---

# 4. Approximating a fixed set of vertices by “clones”

The next lemma is a standard regularity-and-sampling consequence, but its details matter here. In particular, we need simultaneous control of both common neighbourhoods and their intersections.

For disjoint sets \(A,B\) in a tournament, write
\[
d(A,B)=\frac{e(A,B)}{|A||B|},
\]
where \(e(A,B)\) counts arcs from \(A\) to \(B\).

## Lemma 2
Fix \(q\ge1\) and \(\eta>0\). Every sufficiently large \(N\)-vertex tournament has disjoint vertex sets
\[
V_1,\dots,V_t
\]
with the following properties. Put
\[
U=\bigcup_iV_i,\qquad w_i=|V_i|,\qquad W=|U|.
\]

1. \(W\ge(1-\eta)N\), and every \(w_i\) tends to infinity with \(N\).
2. There are numbers \(d_{ij}\) satisfying
   \[
   d_{ij}+d_{ji}=1,\qquad d_{ii}=\frac12.
   \]
3. For each \(i\), at least a \(1-\eta\) proportion of the \(q\)-subsets \(S\subseteq V_i\) satisfy the following simultaneously for every pair of disjoint subsets \(E,F\subseteq S\):
   \[
   \left|
   |\{v\in U\setminus S:E\to v\to F\}|
   -
   \sum_j w_jd_{ij}^{\,|E|}(1-d_{ij})^{\,|F|}
   \right|
   \le\eta N.
   \tag{5}
   \]

Here \(E\to v\to F\) imposes no condition on a side that is empty.

### Proof
We use the finite regularity lemma for the arc relation of a tournament. Its usual energy-increment proof gives an equitable partition
\[
V_0,V_1,\dots,V_s
\]
with \(|V_0|\le\delta N\), with \(t_0\le s\le M(\delta,t_0)\), and with at most \(\delta s^2\) irregular unordered pairs. A pair \((A,B)\) is \(\delta\)-regular when all subsets of relative size at least \(\delta\) have arc density within \(\delta\) of \(d(A,B)\).

Delete \(V_0\) and every cluster having more than \(\sqrt\delta\,s\) irregular partners. At most \(2\sqrt\delta\,s\) clusters are deleted. Thus the surviving union has size at least
\[
(1-\delta-2\sqrt\delta)N.
\tag{6}
\]
Relabel the surviving clusters. For \(i\ne j\), set \(d_{ij}=d(V_i,V_j)\), and set \(d_{ii}=1/2\).

We justify the sampling assertion.

### Sampling in one regular pair
Consider a \(\delta\)-regular pair \((A,B)\) of density \(d\), and choose \(q\) distinct vertices of \(A\) uniformly. Fix a pattern prescribing, for some of these vertices, either the direction \(x\to v\) or \(v\to x\).

Expose the relevant vertices one at a time, maintaining the set of compatible vertices in \(B\). Whenever that set has size at least \(\delta|B|\), regularity implies that all but at most \(2\delta|A|\) choices for the next vertex have the prescribed neighbourhood size within
\[
\delta\cdot |\text{current compatible set}|
\]
of its expected density multiple.

For \(|A|\ge2q\), the probability that one of these tests fails is at most \(4q\delta\). If no test fails, the final compatible set has size within \(q\delta|B|\) of
\[
d^{e}(1-d)^f|B|,
\]
where \(e,f\) are the numbers of the two prescribed directions.

This conclusion also holds if an intermediate compatible set becomes smaller than \(\delta|B|\): from that point its actual size remains small, and its predicted size is at most \(q\delta|B|\).

There are at most \(3^q\) patterns. Therefore, if \(Z_{A,B}\) is the largest normalized error over all patterns, then
\[
\mathbb E Z_{A,B}\le C_q\delta
\tag{7}
\]
for a constant \(C_q\) depending only on \(q\).

### Summing over clusters
For a fixed surviving cluster \(V_i\), sum these errors over its regular partner clusters, weighted by their sizes. By (7), the expected total error is at most \(C_q\delta N\). Markov's inequality shows that, for all but an \(\eta\) proportion of the \(q\)-subsets of \(V_i\), this total error is at most \(\eta N/2\), provided \(\delta\) is sufficiently small in terms of \(q,\eta\).

The irregular partners have total size at most \(\sqrt\delta N\). The contribution from \(V_i\) itself introduces an error of at most
\[
|V_i|\le N/t_0.
\]
Choose \(t_0\) large enough and then \(\delta\) small enough that
\[
\sqrt\delta+1/t_0\le\eta/2,
\qquad
\delta+2\sqrt\delta\le\eta.
\]
This proves (5) and the mass assertion. The regularity bound on the number of clusters ensures that each surviving cluster has size at least a positive constant times \(N\). ∎

---

# 5. Embedding a bounded core and all its leaves

Fix \(k,r,\varepsilon\), and put
\[
\rho=2^{-k},\qquad q=kr.
\]
Let \(\vec T\) be an \(n\)-vertex oriented tree with at most \(r\) non-leaf vertices, and set
\[
m=kn.
\]
We may assume \(n\ge3\). Let \(F\) be its non-leaf core, and write \(r_0=|V(F)|\le r\).

Let

- \(A\) be the number of blow-up vertices belonging to leaves whose tree arc is directed **towards** the core;
- \(B\) be the corresponding number for leaves whose arc is directed **away from** the core.

Thus
\[
A+B=L=m-kr_0.
\tag{8}
\]

Consider any tournament \(R\) on
\[
N\ge(\rho^{-1}+\varepsilon)m
\tag{9}
\]
vertices.

## 5.1 Choosing the approximation parameters

Set
\[
\zeta=\rho-\frac1{\rho^{-1}+\varepsilon}>0,
\]
so that
\[
m\le(\rho-\zeta)N.
\tag{10}
\]

Every tournament on
\[
h=2^{q-1}
\]
vertices has a transitive \(q\)-vertex subtournament, by the usual induction using an in- or out-neighbourhood. Consequently, in any sufficiently large tournament, at least the proportion
\[
\tau_q=\binom hq^{-1}
\tag{11}
\]
of its \(q\)-subsets are transitive: double-count pairs consisting of an \(h\)-set and a transitive \(q\)-set inside it.

Choose
\[
0<\eta<
\min\{\zeta/10,\rho/16,\tau_q/2\}.
\tag{12}
\]
Apply Lemma 2 with \(q,\eta\).

For its density matrix, define \(f_i^\pm\) as in Lemma 1. Since
\[
\begin{aligned}
(A+2\eta N)+(B+2\eta N)
&\le m+4\eta N\\
&\le(\rho-\zeta+4\eta)N\\
&<\rho(1-\eta)N\\
&\le\rho W,
\end{aligned}
\]
Lemma 1 gives a cluster \(V_i\) with
\[
f_i^-\ge A+2\eta N,\qquad
f_i^+\ge B+2\eta N.
\tag{13}
\]

## 5.2 Embedding the core

At least a \(\tau_q\) proportion of the \(q\)-sets in \(V_i\) are transitive, while at most an \(\eta\) proportion fail (5). Hence there exists a transitive \(q\)-set \(S\subseteq V_i\) satisfying (5).

The oriented core \(F\) is acyclic. List its vertices in a topological order and assign consecutive disjoint \(k\)-sets of the transitive order on \(S\) to them. This embeds \(F[k]\). Denote these core bags by \(X_u\), for \(u\in V(F)\).

We will place all leaf vertices outside \(S\).

For every core bag \(X\), define
\[
P_X^-=\{v\in U\setminus S:v\to X\},
\qquad
P_X^+=\{v\in U\setminus S:X\to v\}.
\]
By (5) and (13),
\[
|P_X^-|\ge A+\eta N\ge A,
\qquad
|P_X^+|\ge B+\eta N\ge B.
\tag{14}
\]

We also need a union bound for pools of opposite signs.

## 5.3 Opposite-sign pools have enough combined capacity

For two distinct core bags \(X,Y\), (5) gives
\[
\begin{aligned}
|P_X^-\cup P_Y^+|
&\ge
\sum_jw_j\left[
(1-d_{ij})^k+d_{ij}^k
-d_{ij}^k(1-d_{ij})^k
\right]-3\eta N.
\end{aligned}
\tag{15}
\]
For every \(d\in[0,1]\),
\[
d^k+(1-d)^k\ge2\rho,
\qquad
d^k(1-d)^k\le\rho^2.
\]
Therefore
\[
|P_X^-\cup P_Y^+|
\ge(2\rho-\rho^2)W-3\eta N.
\tag{16}
\]

If \(X=Y\), the two pools are disjoint, and the same lower bound follows from the two individual estimates in (5). Thus (16) holds in all cases.

Since \(\rho\le1/2\), \(W\ge(1-\eta)N\), and \(\eta<\rho/16\),
\[
\begin{aligned}
(2\rho-\rho^2)W-3\eta N
&\ge\left(\frac32\rho-4\eta\right)N\\
&\ge\rho N\\
&\ge m.
\end{aligned}
\]
In particular,
\[
\boxed{|P_X^-\cup P_Y^+|\ge L}
\quad\text{for all core bags }X,Y.
\tag{17}
\]

## 5.4 Hall's theorem assigns every leaf vertex

Form a bipartite graph whose left side consists of all \(L\) leaf vertices of \(\vec T[k]\), and whose right side is \(U\setminus S\). A leaf vertex adjacent towards a core bag \(X\) has candidate set \(P_X^-\); one adjacent away from \(X\) has candidate set \(P_X^+\).

Consider any nonempty set \(Z\) of left-side vertices.

- If all vertices of \(Z\) have incoming leaf arcs, then \(|Z|\le A\), and their candidate union contains a pool of size at least \(A\), by (14).
- If all have outgoing leaf arcs, the analogous argument uses \(B\).
- If both signs occur, the candidate union contains one incoming pool and one outgoing pool, whose union has size at least \(L\ge|Z|\), by (17).

Thus Hall's condition holds. A matching assigns all leaf vertices injectively to their candidate vertices.

All core arcs were already embedded, and every remaining required arc joins a leaf bag to its core bag. Hence the matching completes an embedding of \(\vec T[k]\).

This proves the upper bound in (1). Together with the out-star lower bound, the theorem follows. ∎

---

# 6. Consequences and the remaining gap

The restricted theorem gives
\[
\boxed{
U_{k,r}(n)=(2^k+o(1))kn
\qquad(k,r\text{ fixed}).
}
\]
It improves the supplied partial attempt in two directions: arbitrary star orientations are covered, and the center can be replaced by any fixed-size oriented tree core with arbitrarily distributed incoming and outgoing leaves.

It does **not** establish the claimed bound for arbitrary trees. The crucial fixed-core step embeds the entire core inside a transitive \(kr\)-set. For a path, the core has \(n-2\) vertices; forcing a transitive set of that size would require far more than a linear-order host tournament. The regularity parameters and the sufficiently-large-\(n\) threshold also depend on \(r\).

For the unrestricted normalization
\[
a_k=
\limsup_{n\to\infty}
\max_{|V(T)|=n}
\frac{u(\vec T[k])}{kn},
\]
the bounds established or supplied here remain
\[
2^k\le a_k\le2^{10+18k}.
\]
Thus no improved unrestricted upper bound is claimed. In particular, a proof that the general infimum is \(2\), or a construction forcing it above \(2\), is still missing.

The bounded-core theorem above is proved independently, but I have not checked whether it is already implicit in the literature on tournament embeddings with bounded vertex cover.