```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The worst-case exponent gap remains unresolved; I prove a quadratic bound for ordered sums of separated matchings and exact values for two canonical matching orders.",
  "would_publish": false,
  "caveats": "No bound on the worst-case function is improved, and the restricted lemmas may be folklore."
}
```

## 1. Precise formulation

Assume throughout that an ordered matching on \(n=2m\) vertices is perfect. Define
\[
R_{\mathrm{mat}}(2m)
 =\max\{r_<(M):M\text{ is an ordered perfect matching on }[2m]\}.
\]
This extremal formulation is necessary: \(r_<(M)\) is not determined by the number of vertices alone.

The bounds from the source paper are, for some absolute \(c>0\),
\[
(2m)^{\,c\log(2m)/\log\log(2m)}
 \le R_{\mathrm{mat}}(2m)
 \le (2m)^{\lceil\log_2(2m)\rceil}.
\]
I do not close or improve this worst-case gap.

I prove instead:

1. a quadratic upper bound for a class strictly larger than the matchings of interval chromatic number \(2\);
2. exact Ramsey numbers for the serial and completely nested matchings;
3. a sharp structural lemma about canonical submatchings;
4. an explicit explanation of why the quadratic construction does not extend directly to arbitrary matchings.

---

## 2. Separated matchings and an off-diagonal product bound

An ordered matching \(P\) with \(p\) edges is **separated** if there is a cut such that every edge has one endpoint on each side. Thus, after relabeling its vertices as
\[
1<\cdots<p<p+1<\cdots<2p,
\]
there is a permutation \(\pi\in S_p\) such that
\[
E(P)=\{\{i,p+\pi(i)\}:i\in[p]\}.
\]

Write \(r_<(P,Q)\) for the least \(N\) such that every red-blue coloring of \(K_N\) contains a red ordered copy of \(P\) or a blue ordered copy of \(Q\).

### Proposition 2.1
If \(P\) and \(Q\) are separated ordered matchings with \(p\) and \(q\) edges, respectively, then
\[
r_<(P,Q)\le 2pq.
\]

### Proof

Let \(\pi\in S_p\) and \(\tau\in S_q\) represent \(P\) and \(Q\). On \(2pq\) ordered vertices, take the following auxiliary separated matching \(U\) with \(pq\) edges. Its left endpoints are indexed lexicographically by pairs
\[
(i,a)\in[p]\times[q].
\]
Join the left endpoint \((i,a)\) to the right endpoint having rank
\[
(\pi(i)-1)q+\tau(a)
\]
among the \(pq\) right endpoints.

Consider any red-blue coloring of the edges of \(K_{2pq}\), restricted to these \(pq\) edges of \(U\). For each \(i\in[p]\), let
\[
G_i=\{(i,a):a\in[q]\}
\]
denote the corresponding group of \(q\) auxiliary edges.

- If every \(G_i\) contains a red edge, choose one red edge from each group. Their left groups occur in order \(1,\dots,p\), and their right groups occur in the order prescribed by \(\pi\). They therefore form a red copy of \(P\).
- Otherwise, some \(G_i\) is entirely blue. Within that group, the right endpoints occur according to \(\tau\), so its \(q\) edges form a blue copy of \(Q\).

Thus every coloring gives a red \(P\) or a blue \(Q\). ∎

In particular, every separated \(m\)-edge matching satisfies
\[
r_<(M)\le 2m^2=\frac{n^2}{2}.
\]

---

## 3. Closure under ordered sums

For ordered graphs \(H_1,\dots,H_s\), write
\[
H_1\oplus\cdots\oplus H_s
\]
for their ordered disjoint union, with every vertex of \(H_i\) preceding every vertex of \(H_{i+1}\).

### Lemma 3.1: Grid composition
For ordered graphs \(A_1,\dots,A_s\) and \(B_1,\dots,B_t\),
\[
r_<\!\left(\bigoplus_{i=1}^s A_i,\,
           \bigoplus_{j=1}^t B_j\right)
 \le
 \sum_{i=1}^s\sum_{j=1}^t r_<(A_i,B_j).
\]

### Proof

For every state \((i,j)\), with \(0\le i<s\) and \(0\le j<t\), take a consecutive host block of
\[
r_<(A_{i+1},B_{j+1})
\]
vertices. Order these blocks by increasing \(i+j\), with arbitrary order inside each level.

Start at state \((0,0)\). When the block indexed by \((i,j)\) is reached, it contains either a red \(A_{i+1}\) or a blue \(B_{j+1}\).

- In the first case, move to state \((i+1,j)\).
- In the second, move to state \((i,j+1)\).

Each move increases \(i+j\), so the block corresponding to the new state lies later in the host order. After at most \(s+t-1\) moves, either \(i=s\) or \(j=t\). The accumulated red copies then form
\[
A_1\oplus\cdots\oplus A_s,
\]
or the accumulated blue copies form
\[
B_1\oplus\cdots\oplus B_t.
\]
Skipped blocks cause no problem because ordered copies need not use consecutive host vertices. ∎

Combining Lemma 3.1 with Proposition 2.1 gives the following.

### Theorem 3.2
Suppose
\[
A=A_1\oplus\cdots\oplus A_s,\qquad
B=B_1\oplus\cdots\oplus B_t,
\]
where every \(A_i\) and \(B_j\) is separated. If \(A\) has \(p\) edges and \(B\) has \(q\) edges, then
\[
r_<(A,B)\le 2pq.
\]

Indeed, writing \(p_i=e(A_i)\) and \(q_j=e(B_j)\),
\[
r_<(A,B)
 \le \sum_{i,j}2p_iq_j
 =2\left(\sum_i p_i\right)\left(\sum_jq_j\right)
 =2pq.
\]

### Corollary 3.3
If an \(m\)-edge ordered matching \(M\) is an ordered sum of separated matchings, then
\[
r_<(M)\le 2m^2.
\]

This class can have arbitrarily large interval chromatic number. For example, the matching
\[
\{(1,2),(3,4),\dots,(2m-1,2m)\}
\]
is an ordered sum of \(m\) one-edge separated matchings.

Equivalently, Corollary 3.3 applies whenever every indecomposable interval component of \(M\) has a cut crossed by all of its edges.

---

## 4. Exact values for two canonical orders

There are three canonical ways in which every pair of edges of a matching can have the same relative order:

\[
\begin{aligned}
S_m&=\{\{2i-1,2i\}:i\in[m]\}
&&\text{(serial)},\\
X_m&=\{\{i,m+i\}:i\in[m]\}
&&\text{(pairwise crossing)},\\
N_m&=\{\{i,2m+1-i\}:i\in[m]\}
&&\text{(pairwise nested)}.
\end{aligned}
\]

### Proposition 4.1
For all \(m\ge1\),
\[
r_<(S_m)=r_<(N_m)=4m-2.
\]
Moreover,
\[
3m-1\le r_<(X_m)\le4m-2.
\]

### Common upper bound

On \(4m-2\) vertices, exhibit \(2m-1\) edges of the relevant canonical type:

- serial:
  \[
  (1,2),(3,4),\dots,(4m-3,4m-2);
  \]
- crossing:
  \[
  (i,2m-1+i),\qquad i=1,\dots,2m-1;
  \]
- nested:
  \[
  (i,4m-1-i),\qquad i=1,\dots,2m-1.
  \]

Among these \(2m-1\) edges, at least \(m\) have the same color. Every \(m\)-edge subset has the same canonical order type, proving
\[
r_<(S_m),r_<(X_m),r_<(N_m)\le4m-2.
\]

### Lower bound for \(S_m\)

Color \(K_{4m-3}\) by declaring an edge \(xy\), \(x<y\), red if
\[
x\le2m-2,
\]
and blue otherwise.

In an ordered copy of \(S_m\), with selected vertices
\[
v_1<\cdots<v_{2m},
\]
the last edge is \(v_{2m-1}v_{2m}\). Since \(v_{2m-1}\ge2m-1\), this edge is blue, so there is no red \(S_m\).

Every blue edge has both endpoints in
\[
\{2m-1,\dots,4m-3\},
\]
which has only \(2m-1\) vertices. Hence there is no blue matching with \(m\) edges. Thus
\[
r_<(S_m)>4m-3.
\]

### Lower bound for \(N_m\)

Set \(N=4m-3\). For \(x<y\), define
\[
d(x,y)=\min\{x,N+1-y\}.
\]
Color \(xy\) red if \(d(x,y)\le m-1\), and blue otherwise.

Suppose there were a red nested matching with edges
\[
x_1y_1,\dots,x_my_m,
\]
ordered from outermost to innermost. Then
\[
x_1<\cdots<x_m<y_m<\cdots<y_1.
\]
Both sequences \(x_i\) and \(N+1-y_i\) increase strictly with \(i\). Therefore
\[
d(x_{i+1},y_{i+1})\ge d(x_i,y_i)+1.
\]
Since \(d(x_1,y_1)\ge1\), we obtain \(d(x_m,y_m)\ge m\), contradicting that all edges are red.

Every blue edge satisfies
\[
x\ge m,\qquad y\le N+1-m=3m-2.
\]
Thus every blue edge lies entirely inside the interval
\[
[m,3m-2],
\]
which has \(2m-1\) vertices. It cannot contain an \(m\)-edge matching. Hence
\[
r_<(N_m)>4m-3.
\]

This proves the exact values.

### Lower bound for \(X_m\)

The standard coloring on \(3m-2\) vertices also gives a lower bound for every ordered \(m\)-edge matching. Let \(A\) have \(2m-1\) vertices and \(B\) have \(m-1\) vertices. Color exactly the edges inside \(A\) red and all remaining edges blue.

The red matching number is at most \(m-1\), while every blue edge meets \(B\), so the blue matching number is also at most \(m-1\). Thus
\[
r_<(X_m)\ge3m-1.
\]

For \(m=2\), this is exact:
\[
r_<(X_2)=5.
\]
For the upper bound, in \(K_5\) consider the five host edges
\[
13,\ 24,\ 35,\ 14,\ 25
\]
cyclically in that order. Consecutive edges are disjoint and crossing. Since an odd cycle cannot be properly 2-colored, two consecutive edges have the same color and form \(X_2\).

Consequently, on four target vertices,
\[
r_<(X_2)=5,\qquad
r_<(S_2)=r_<(N_2)=6.
\]
Thus the Ramsey number already depends on the labeling for \(n=4\).

---

## 5. A sharp canonical-submatching lemma

For an ordered matching \(M\), let \(\kappa(M)\) be the largest number of edges in a submatching that is entirely serial, entirely crossing, or entirely nested.

### Proposition 5.1
Every \(m\)-edge ordered matching satisfies
\[
\kappa(M)\ge \left\lceil m^{1/3}\right\rceil.
\]
The exponent \(1/3\) is best possible.

### Proof of the lower bound

Associate to every edge \(ab\), \(a<b\), the interval \((a,b)\). Let \(s\) be the maximum number of pairwise disjoint such intervals. These \(s\) edges form a serial submatching, so \(s\le\kappa(M)\).

For intervals, the minimum number of points meeting every interval equals the maximum number of pairwise disjoint intervals. Thus the intervals can be pierced by \(s\) points. Assign every interval to one piercing point it contains.

Consider one class of \(L\) intervals containing a common point \(z\). Sort them by increasing left endpoint:
\[
a_1<\cdots<a_L<z.
\]
Their right endpoints are distinct and all exceed \(z\). An increasing subsequence of the right endpoints gives pairwise crossing edges; a decreasing subsequence gives pairwise nested edges.

If neither type has more than \(K=\kappa(M)\) edges, the Erdős–Szekeres product bound gives
\[
L\le K^2.
\]
There are at most \(s\le K\) piercing classes, so
\[
m\le sK^2\le K^3.
\]
Hence \(K\ge m^{1/3}\).

### Sharpness

Let \(m=k^3\). Take \(k\) ordered, mutually serial blocks. Inside each block put a separated matching with \(k^2\) edges corresponding to the permutation
\[
k,k-1,\dots,1,\ 
2k,2k-1,\dots,k+1,\ 
\dots,\ 
k^2,k^2-1,\dots,k^2-k+1.
\]
This permutation has longest increasing and decreasing subsequences both of length \(k\).

Within one block:

- crossing submatchings correspond to increasing subsequences;
- nested submatchings correspond to decreasing subsequences;
- no two edges are serial because all cross the same cut.

Between different blocks, every pair of edges is serial. Therefore:

- a serial canonical submatching uses at most one edge from each of the \(k\) blocks;
- a crossing or nested canonical submatching lies inside a single block and has at most \(k\) edges.

Thus \(\kappa(M)=k=m^{1/3}\).

This lemma is structurally sharp, but it does not improve the ordered Ramsey upper bound: if \(C\subseteq M\), then
\[
r_<(C)\le r_<(M),
\]
which is the wrong direction for reconstructing all of \(M\).

---

## 6. Why the quadratic construction does not extend directly

The proof of Proposition 2.1 depends crucially on separation. Each outer group has two properties:

1. choosing one edge from every group always reproduces the outer permutation;
2. a single group itself reproduces the inner permutation.

For an arbitrary ordered matching, replacing one edge by a group confined between its two endpoint intervals can only produce a separated matching inside that group. It cannot reproduce an arbitrary double-occurrence pattern.

There is also an immediate color-coherence obstruction. Consider
\[
M^\star=\{\{1,3\},\{2,5\},\{4,6\}\}.
\]
It is indecomposable: every cut is crossed by some edge. It is not separated: no cut is crossed by all three edges.

Color \(K_6\) by making all edges inside \(\{1,2,3\}\) and inside \(\{4,5,6\}\) blue, and every edge between the two triples red. The only order-preserving embedding of \(M^\star\) into these six vertices has edge colors
\[
\text{blue},\ \text{red},\ \text{blue}.
\]
Thus complete red structure across a cut and blue structure inside the two sides do not glue into a monochromatic matching.

This is the fundamental difficulty in a multiscale proof: internal and crossing portions of the target may be forced in opposite colors. According to the supplied literature review, separated matchings can themselves have nearly quadratic ordered Ramsey number, so one also cannot simply replace the quadratic separated gadget by a uniformly linear one at every scale.

---

## 7. Exact SAT formulation for small cases

For a fixed matching \(M\) on \([2m]\) and host size \(N\), introduce one Boolean variable \(x_{ab}\) for every \(1\le a<b\le N\), with \(x_{ab}=1\) meaning red.

For every increasing tuple
\[
v_1<\cdots<v_{2m},
\]
add the two clauses
\[
\bigvee_{\{i,j\}\in E(M)}\neg x_{v_iv_j},
\qquad
\bigvee_{\{i,j\}\in E(M)}x_{v_iv_j}.
\]
The first forbids an all-red copy on that tuple, and the second forbids an all-blue copy.

The resulting formula has
\[
\binom N2
\]
variables and
\[
2\binom N{2m}
\]
clauses, each of length \(m\). It is satisfiable exactly when
\[
r_<(M)>N.
\]
Thus exhaustive small-case calculations can be made certifiable by retaining SAT assignments and unsatisfiability certificates. No computational result beyond the hand-checked \(n=4\) cases above is claimed here.

---

## 8. Remaining gap

The new restricted estimate is
\[
r_<(M)\le \frac{n^2}{2}
\]
when every indecomposable ordered-sum component of \(M\) is separated. This includes matchings of unbounded interval chromatic number, but excludes genuinely mixed indecomposable patterns such as \(M^\star\).

Nothing here improves
\[
R_{\mathrm{mat}}(n)\le n^{\lceil\log_2 n\rceil}
\]
or the known superpolynomial lower bound. Resolving the catalog problem still requires either:

- a construction coordinating hard behavior over substantially more scales, to raise the lower bound toward \(n^{\Theta(\log n)}\); or
- a high-arity or otherwise color-coherent decomposition of every ordered matching, to lower the universal exponent to \(O(\log n/\log\log n)\).

I do not have such an argument.