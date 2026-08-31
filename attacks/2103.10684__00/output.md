```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact constant remains open, but the restricted problem in which every quasi-branch set has at most two components has asymptotic constant exactly 2/3, and the standard paired random construction has Hadwiger number 2t/3+O(log t).",
  "would_publish": false,
  "caveats": "The global bounds 1/2 <= c <= 2/3 are unchanged, and these refinements may already be implicit in the source construction."
}
```

# 1. Setup

Write \(h(G)\) for the Hadwiger number of \(G\). I use the standard definition that a quasi-\(K_t\)-model consists of pairwise disjoint nonempty sets
\[
X_1,\dots,X_t\subseteq V(G)
\]
such that \(G[X_i\cup X_j]\) is connected for every \(i\ne j\).

There is a useful normalization. Contract every connected component of each \(G[X_i]\) to one vertex, and discard all other vertices. The resulting graph \(H\) is a minor of \(G\) and has a partition
\[
C_1,\dots,C_t
\]
into stable sets such that every \(H[C_i\cup C_j]\) is connected. Thus lower bounds for this normalized graph lift to \(G\). The size of \(C_i\) is the number of components of the original quasi-branch set \(X_i\).

In particular, every vertex of \(C_i\) has a neighbor in every \(C_j\), \(j\ne i\).

Pairing the classes gives the familiar bound
\[
h(G)\ge \left\lfloor\frac t2\right\rfloor:
\]
each \(C_{2i-1}\cup C_{2i}\) is connected, and any two such unions are adjacent.

# 2. Exact asymptotic answer when every part has at most two components

## Theorem 2.1

Suppose \(G\) has a quasi-\(K_t\)-model \(X_1,\dots,X_t\), with every \(G[X_i]\) having at most two connected components. Then
\[
h(G)\ge \left\lceil\frac{2t}{3}\right\rceil .
\]

### Proof

Normalize as above, so \(C_1,\dots,C_t\) are stable, \(1\le |C_i|\le2\), and every bichromatic graph is connected.

We prove the assertion by induction on \(t\).

If some \(C_i=\{v\}\), then connectedness of \(H[C_i\cup C_j]\) implies that \(v\) is adjacent to every vertex of every other class \(C_j\). Apply induction after deleting \(C_i\), and add \(\{v\}\) as an additional branch set. Since
\[
1+\left\lceil\frac{2(t-1)}3\right\rceil
   \ge \left\lceil\frac{2t}3\right\rceil,
\]
this suffices.

We may therefore assume that every \(C_i\) has exactly two vertices. For each pair \(i\ne j\), delete edges from \(H[C_i\cup C_j]\) until it is a spanning tree. A bipartite tree with parts of size two is necessarily a \(P_4\). Consequently, for each ordered pair \(i\ne j\), exactly one vertex
\[
d_i(j)\in C_i
\]
is adjacent to both vertices of \(C_j\).

Suppose first that for some \(i\) there are distinct \(j,k\) with
\[
d_i(j)\ne d_i(k).
\]
Set
\[
B_j=C_j\cup\{d_i(j)\},
\qquad
B_k=C_k\cup\{d_i(k)\}.
\]
These are disjoint connected sets. They are adjacent because they contain all of \(C_j\) and \(C_k\), respectively.

Delete the three classes \(C_i,C_j,C_k\). By induction, the remaining classes contain a
\[
K_{\lceil 2(t-3)/3\rceil}
\]
minor. Each of its branch sets is adjacent to both \(B_j\) and \(B_k\): every vertex in a remaining class has a neighbor in the full class \(C_j\), and likewise in \(C_k\). Hence
\[
h(H)\ge 2+\left\lceil\frac{2(t-3)}3\right\rceil
      =\left\lceil\frac{2t}3\right\rceil.
\]

It remains that \(d_i(j)\) is independent of \(j\) for every \(i\). Let this common vertex be \(u_i\in C_i\). Then \(u_i\) is adjacent to both vertices of every \(C_j\), \(j\ne i\). Therefore
\[
\{u_1,\dots,u_t\}
\]
is a \(K_t\) subgraph, which is more than required. ∎

## Corollary 2.2: a component-sensitive lower bound

Let \(s\) of the \(t\) quasi-branch sets have at most two components. Then
\[
h(G)\ge
\left\lceil\frac{2s}{3}\right\rceil+
\left\lfloor\frac{t-s}{2}\right\rfloor
\ge \frac t2+\frac s6-1.
\]

Indeed, apply Theorem 2.1 to those \(s\) classes and pair the other \(t-s\) classes. Branch sets from the two constructions are adjacent because each paired branch set contains an entire color class.

Consequently, if
\[
h(G)\le \left(\frac12+\eta\right)t,
\]
then any displayed quasi-\(K_t\)-model must have
\[
s\le 6\eta t+6.
\]
Thus any construction approaching the lower endpoint \(1/2\) must have at least \(t-o(t)\) quasi-branch sets with three or more components. In particular, the two-vertex-per-color construction cannot be modified merely by changing its edge choices to obtain a constant below \(2/3\).

# 3. A sharp random construction in the two-component case

The preceding lower bound is asymptotically attained.

## Construction

For each \(q\), let
\[
C_i=\{x_i,y_i\},\qquad 1\le i\le q,
\]
be stable sets. Independently for every pair \(i<j\), choose uniformly one of the four possible edges between \(C_i\) and \(C_j\) and omit it; include the other three edges.

Thus every \(G_q[C_i\cup C_j]\) is a \(P_4\), so the \(C_i\) form a frozen proper \(q\)-coloring and hence a quasi-\(K_q\)-model.

## Theorem 3.1

There is an absolute constant \(A\) such that, with probability tending to one,
\[
\left\lceil\frac{2q}{3}\right\rceil
\le h(G_q)
\le \frac{2q}{3}+A\log q.
\]

The lower bound is deterministic by Theorem 2.1. It remains to prove the upper bound.

### Small branch sets

Call a connected branch set small if it has at most two vertices. It is then either:

- a singleton, or
- an edge whose endpoints lie in distinct color classes.

Its color support has size at most two.

Consider a fixed family \(\mathcal F\) of \(\ell\) such sets whose color supports are pairwise disjoint. For distinct \(A,B\in\mathcal F\), the event that there is no edge between \(A\) and \(B\) has probability
\[
4^{-|A||B|}\ge 4^{-4}=\frac1{256}.
\]
Moreover, the adjacency events for the different pairs \(A,B\) are independent: each uses random choices belonging to a disjoint collection of unordered pairs of color classes. Therefore
\[
\Pr(\mathcal F\text{ is pairwise adjacent})
 \le \left(\frac{255}{256}\right)^{\binom{\ell}{2}}.
\]

There are exactly
\[
2q+4\binom q2=2q^2
\]
possible singleton or two-vertex shapes. Hence the probability that there is a pairwise adjacent, support-disjoint family of order \(\ell\) is at most
\[
(2q^2)^\ell
\left(\frac{255}{256}\right)^{\binom{\ell}{2}}.
\]
Taking
\[
\ell=L_q=
\left\lceil
\frac{6\log q}{\log(256/255)}
\right\rceil
\]
makes this expression tend to zero. Thus, with high probability, no such family has \(L_q\) members.

Now consider any clique-minor model and let \(s\) be its number of small branch sets. Form a conflict graph on these \(s\) sets, joining two when their color supports intersect. Since each color class has only two vertices and the branch sets are vertex-disjoint, every small branch set conflicts with at most two others. Hence the conflict graph has maximum degree at most two and has an independent set of size at least \(s/3\). Such an independent set is precisely a support-disjoint family.

It follows, with high probability, that
\[
s<3L_q.
\]

### Counting vertices

If the model has \(r\) branch sets, its \(s\) small branch sets use at least one vertex each, and all other branch sets use at least three vertices. Since \(G_q\) has \(2q\) vertices,
\[
2q\ge s+3(r-s)=3r-2s.
\]
Consequently,
\[
r\le \frac{2q}{3}+\frac{2s}{3}
 <\frac{2q}{3}+2L_q.
\]
This proves Theorem 3.1 with, for example,
\[
A=\frac{12}{\log(256/255)}+1.
\]
The constant is not optimized. ∎

## Consequence

If \(\gamma_2(t)\) denotes the minimum Hadwiger number among graphs having a quasi-\(K_t\)-model with at most two components in every part, then
\[
\lim_{t\to\infty}\frac{\gamma_2(t)}t=\frac23.
\]

Thus the known \(2/3\)-type construction is not concealing a substantially smaller Hadwiger number: in this natural paired model its Hadwiger number is
\[
\frac{2t}{3}+O(\log t).
\]

# 4. A small universal finite improvement

For completeness, the trivial lower bound can be improved additively without any restriction on component counts.

## Proposition 4.1

Every graph admitting a quasi-\(K_t\)-minor, \(t\ge4\), has a
\[
K_{\lfloor t/2\rfloor+2}
\]
minor.

### Proof

Normalize and take any four classes \(C_1,\dots,C_4\). Put \(n=\sum |C_i|\). Since each of the six bichromatic graphs is connected and their edge sets are disjoint,
\[
e\bigl(H[C_1\cup\cdots\cup C_4]\bigr)
 \ge \sum_{i<j}(|C_i|+|C_j|-1)
 =3n-6.
\]
A \(K_4\)-minor-free simple graph on \(n\) vertices has at most \(2n-3\) edges. Since \(n\ge4\), we have \(3n-6>2n-3\); hence these four classes contain a \(K_4\)-minor.

Pair the remaining \(t-4\) classes. Every branch set in the \(K_4\)-model is adjacent to each paired branch set because the latter contains a full color class. This gives
\[
4+\left\lfloor\frac{t-4}{2}\right\rfloor
=\left\lfloor\frac t2\right\rfloor+2.
\]
∎

This is only an additive improvement and does not affect the asymptotic constant.

# 5. What remains open

The argument does not improve the global interval
\[
\frac12\le c\le\frac23.
\]
It establishes instead:

1. the exact asymptotic value \(2/3\) when every quasi-branch set has at most two components;
2. an explicit structural obstruction to approaching \(1/2\): almost every part would need at least three components;
3. an \(O(\log t)\) quantitative sharpening for the paired random witness.

Resolving the original question still requires either:

- a construction with many three-or-more-component parts and Hadwiger number below \((2/3-o(1))t\), or
- a new conversion theorem extracting more than \(t/2\) ordinary branch sets from arbitrary multi-component quasi-branch sets.

No argument above covers those cases.