```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every admissible pair satisfies χ_f(G)≤5 and χ(G)≤(4+o(1))log n/log log n, while quasirandom or doubly regular tournaments force χ(G)≤5.",
  "would_publish": false,
  "caveats": "No absolute chromatic bound is obtained for arbitrary tournaments, and these elementary partial results may be implicit in existing work."
}
```

## 1. Statement and summary of the partial results

Call a pair \((G,T)\) **admissible** if \(G\) and \(T\) have the same vertex set and

\[
G[N_T^+(v)]\quad\text{is a forest for every }v\in V(G).
\tag{P}
\]

I prove the following.

### Partial theorem

Let \((G,T)\) be admissible, let \(n=|V(G)|\), and put \(k=\chi(G)\).

1. Every cycle of \(G\) is an out-dominating set in \(T\). More generally, if \(\gamma(T)\) is the minimum size of an out-dominating set in \(T\), then
   \[
   \chi(G)\le 2\gamma(T)+1.
   \tag{1}
   \]

2. If \(k\ge 3\), then
   \[
   n\ge (k-2)^{\left\lfloor (k-2)/4\right\rfloor}.
   \tag{2}
   \]
   Consequently,
   \[
   \chi(G)\le (4+o(1))\frac{\log n}{\log\log n}.
   \tag{3}
   \]

3. The fractional chromatic number satisfies
   \[
   \chi_f(G)\le 5,
   \tag{4}
   \]
   and the constant \(5\) is sharp.

4. Let
   \[
   a(T)=\min_{x\ne y}|N_T^-(x)\cap N_T^-(y)|,\qquad
   b(T)=\max_x d_T^-(x).
   \]
   If \(a(T)>0\), then
   \[
   \operatorname{degeneracy}(G)\le
   \left\lfloor\frac{2b(T)}{a(T)}\right\rfloor.
   \tag{5}
   \]
   In particular, if \(2b(T)/a(T)<5\), then \(\chi(G)\le5\). It follows that:
   - for a uniformly random tournament \(T\), with probability \(1-o(1)\), every admissible \(G\) is \(5\)-colorable;
   - if \(T\) is doubly regular of order at least \(11\), every admissible \(G\) is \(5\)-colorable.

5. Every admissible \(G\) is \(K_6\)-free and \(K_{6,6}\)-free.

These conclusions do not settle the conjecture because (2) still allows \(k\to\infty\) when \(n\) grows sufficiently quickly.

---

## 2. Cycles are tournament-dominating

Write \(x\to y\) when \(xy\) is oriented from \(x\) to \(y\) in \(T\).

### Lemma 2.1

Every cycle \(C\) of \(G\) is an out-dominating set of \(T\): for every \(x\notin V(C)\), there is \(c\in V(C)\) with \(c\to x\).

#### Proof

Otherwise \(x\to c\) for every \(c\in V(C)\). Hence

\[
V(C)\subseteq N_T^+(x),
\]

so \(G[N_T^+(x)]\) contains the cycle \(C\), contradicting (P). ∎

We use the following slightly more general coloring observation.

### Lemma 2.2

If \(D\) is an out-dominating set in \(T\), then

\[
\chi(G)\le 2|D|+1.
\]

#### Proof

For every \(x\in V(G)\setminus D\), choose \(d(x)\in D\) with \(d(x)\to x\).

If \(x\in D\) has an in-neighbor in \(T[D]\), choose such a \(d(x)\in D\). There is at most one vertex \(s\in D\) with no in-neighbor in \(T[D]\), namely a source of \(T[D]\).

For each \(d\in D\), let

\[
P_d=\{x:d(x)=d\}.
\]

Then \(P_d\subseteq N_T^+(d)\), so \(G[P_d]\) is a forest and is \(2\)-colorable. Give different pairs of colors to the sets \(P_d\). If the exceptional source \(s\) exists, give it one additional color. This uses at most \(2|D|+1\) colors. ∎

Taking \(D\) to be a minimum out-dominating set proves (1). Taking \(D=V(C)\) for any cycle \(C\) gives

\[
\chi(G)\le 2|C|+1.
\tag{6}
\]

Thus, if \(g(G)\) denotes the girth and \(\chi(G)=k\ge3\),

\[
g(G)\ge \left\lceil\frac{k-1}{2}\right\rceil.
\tag{7}
\]

In particular, an admissible graph of chromatic number at least \(8\) is triangle-free, and one of chromatic number at least \(10\) has no \(3\)- or \(4\)-cycle.

---

## 3. A superexponential lower bound on the order

Choose an induced subgraph \(H\subseteq G\) minimal subject to \(\chi(H)=k\). Then \(H\) is vertex-critical, so

\[
\delta(H)\ge k-1.
\tag{8}
\]

The restricted pair \((H,T[V(H)])\) remains admissible. Let \(g=g(H)\). By (7),

\[
g\ge \left\lceil\frac{k-1}{2}\right\rceil.
\tag{9}
\]

Set

\[
r=\left\lfloor\frac{g-1}{2}\right\rfloor.
\]

A breadth-first search tree in \(H\), rooted at any vertex and continued to depth \(r\), has no collision: a collision between two nonbacktracking paths of length at most \(r\) would give a cycle of length at most \(2r<g\). Therefore, using (8),

\[
|V(H)|\ge (k-2)^r.
\]

From (9),

\[
r\ge
\left\lfloor
\frac{\left\lceil(k-1)/2\right\rceil-1}{2}
\right\rfloor
=
\left\lfloor\frac{k-2}{4}\right\rfloor.
\]

Hence

\[
n\ge |V(H)|
\ge
(k-2)^{\left\lfloor(k-2)/4\right\rfloor},
\]

which proves (2).

Taking logarithms gives

\[
\log n
\ge
\left(\frac{k}{4}+O(1)\right)\log k,
\]

and inversion yields

\[
k\le (4+o(1))\frac{\log n}{\log\log n}.
\]

Thus any counterexample sequence with chromatic number tending to infinity must have order at least

\[
\exp\!\left((1/4+o(1))k\log k\right).
\]

---

## 4. A sharp fractional chromatic bound

For a nonnegative vertex weighting \(w\), write

\[
W=\sum_{x}w(x),\qquad
Q=\sum_x w(x)^2,\qquad
M=\max_x w(x),
\]

and let \(\alpha_w(G)\) denote the maximum weight of an independent set.

We have the tournament identity

\[
\begin{aligned}
\sum_{v}w(v)\,w(N_T^+(v))
 &=\sum_{v\to x}w(v)w(x)\\
 &=\sum_{\{v,x\}}w(v)w(x)\\
 &=\frac{W^2-Q}{2}.
\end{aligned}
\tag{10}
\]

Therefore some \(v\) satisfies

\[
w(N_T^+(v))\ge \frac{W^2-Q}{2W}.
\tag{11}
\]

Since \(G[N_T^+(v)]\) is a forest, it has an independent set of weight at least half its total weight. Hence

\[
\alpha_w(G)\ge \frac{W^2-Q}{4W}.
\tag{12}
\]

Also \(\alpha_w(G)\ge M\), while \(Q\le MW\). Consequently,

\[
\alpha_w(G)\ge
\max\left\{M,\frac{W-M}{4}\right\}
\ge \frac W5.
\tag{13}
\]

The weighted dual characterization of fractional chromatic number now gives

\[
\chi_f(G)
=
\sup_{w\ge0,\ w\ne0}\frac{W}{\alpha_w(G)}
\le5.
\]

This is sharp. Let \(G=K_5\), and let \(T\) be the regular tournament on \(\mathbb Z_5\), with

\[
i\to j\quad\Longleftrightarrow\quad j-i\in\{1,2\}\pmod 5.
\]

Every out-neighborhood has two vertices, so its induced \(K_2\) is a forest, while

\[
\chi_f(G)=\chi(G)=5.
\]

Thus no universal bound below \(5\) is possible.

---

## 5. Tournaments with robust pair-codegrees

For distinct \(x,y\), put

\[
c^-(x,y)=|N_T^-(x)\cap N_T^-(y)|.
\]

### Lemma 5.1

If

\[
a=\min_{x\ne y}c^-(x,y)>0,\qquad
b=\max_x d_T^-(x),
\]

then every \(X\subseteq V(G)\) satisfies

\[
e(G[X])\le \frac ba |X|.
\tag{14}
\]

#### Proof

For every \(v\), the graph \(G[X\cap N_T^+(v)]\) is a forest, so

\[
e\bigl(G[X\cap N_T^+(v)]\bigr)
\le |X\cap N_T^+(v)|.
\]

Summing over \(v\), the left side counts an edge \(xy\in E(G[X])\) exactly \(c^-(x,y)\) times. Therefore

\[
a\,e(G[X])
\le
\sum_v e\bigl(G[X\cap N_T^+(v)]\bigr).
\]

On the other hand,

\[
\sum_v |X\cap N_T^+(v)|
=
\sum_{x\in X}d_T^-(x)
\le b|X|.
\]

Combining the inequalities proves (14). ∎

It follows that every induced subgraph has average degree at most \(2b/a\), and hence

\[
\operatorname{degeneracy}(G)
\le \left\lfloor\frac{2b}{a}\right\rfloor.
\]

### Random tournaments

For a uniformly random tournament,

\[
d_T^-(x)\sim \operatorname{Bin}(n-1,1/2)
\]

and, for each fixed pair \(x,y\),

\[
c^-(x,y)\sim \operatorname{Bin}(n-2,1/4).
\]

Chernoff bounds followed by a union bound over all vertices and pairs show that, with probability \(1-o(1)\),

\[
b(T)\le 0.51n,\qquad a(T)\ge0.24n.
\]

On this event,

\[
\frac{2b(T)}{a(T)}
\le
\frac{1.02}{0.24}
=4.25<5.
\]

Thus every admissible \(G\) is \(4\)-degenerate and therefore \(5\)-colorable. This statement is simultaneous over all graphs \(G\) on the vertex set.

### Doubly regular tournaments

In a doubly regular tournament of order \(n\),

\[
b(T)=\frac{n-1}{2},\qquad
a(T)=\frac{n-3}{4}.
\]

Hence

\[
\frac{2b(T)}{a(T)}
=
\frac{4(n-1)}{n-3}.
\]

For \(n>11\), this is less than \(5\), so \(\chi(G)\le5\).

For \(n=11\), the ratio is exactly \(5\), but the forest inequality is strict whenever \(X\ne\varnothing\): at least one set \(X\cap N_T^+(v)\) is nonempty, and a nonempty forest on \(s\) vertices has at most \(s-1\) edges. Thus every nonempty \(G[X]\) has average degree strictly less than \(5\), again making \(G\) \(4\)-degenerate. Therefore doubly regular tournaments of order at least \(11\) satisfy the conjectured conclusion with the optimal bound \(5\).

---

## 6. Two forbidden subgraphs

### No \(K_6\)

If \(Q\subseteq V(G)\) induces a \(K_6\), then \(T[Q]\) has a vertex with at least three out-neighbors in \(Q\). Those three vertices induce a triangle in the corresponding out-neighborhood, contradicting (P). Hence

\[
\omega(G)\le5.
\]

In particular, the conjecture holds with threshold \(6\) for perfect graphs and, more generally, for any graph class whose chromatic number is bounded in terms of its clique number.

### No \(K_{6,6}\)

Suppose \(G\) contains a \(K_{6,6}\) with parts \(A,B\). If a vertex \(v\) dominates two vertices of \(A\) and two vertices of \(B\), those four vertices contain a \(4\)-cycle in \(G[N_T^+(v)]\). Therefore, for every \(v\),

\[
\min\{|N_T^+(v)\cap A|,\ |N_T^+(v)\cap B|\}\le1.
\tag{15}
\]

Let

\[
A_0=\{a\in A:d_{T[A]}^+(a)\le1\}.
\]

If \(r=|A_0|\), then

\[
\binom r2
=e(T[A_0])
\le r,
\]

so \(r\le3\). Hence \(A'=A\setminus A_0\) has size at least \(3\), and every \(a\in A'\) has at most one out-neighbor in \(B\), by (15). Define \(B'\) analogously; then \(|B'|\ge3\), and every \(b\in B'\) has at most one out-neighbor in \(A'\).

Counting the arcs between \(A'\) and \(B'\) gives

\[
|A'||B'|
\le |A'|+|B'|,
\]

which is impossible when both sizes are at least \(3\). Thus \(G\) contains no \(K_{6,6}\), even as a non-induced subgraph.

---

## 7. Remaining gap

The main unresolved case is an extremely structured tournament with small pair-codegrees on selected pairs. The fractional bound cannot simply be rounded: ordinary chromatic number can in general be much larger than fractional chromatic number. Likewise, the girth argument only forces a hypothetical counterexample to have at least \(k^{k/4+o(k)}\) vertices; it does not rule out such graphs.

Thus the argument proves the conjecture for quasirandom tournaments, tournaments of bounded domination number, doubly regular tournaments, perfect graphs, and several other restricted settings, but it neither proves an absolute bound for arbitrary tournaments nor produces a counterexample.