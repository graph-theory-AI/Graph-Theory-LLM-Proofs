```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit connected planar family requires c(H) = Omega(|H| log |H|), and this order is tight for disjoint unions of triangles, but polynomial dependence remains unresolved.",
  "would_publish": false,
  "caveats": "This rules out linear dependence, not polynomial dependence; no novelty claim is made for the partial bounds."
}
```

# A superlinear lower bound, including for connected planar patterns

I do not resolve the polynomial-dependence question. I prove a stronger lower bound than the complete-graph example in the supplied attempt:

\[
c(H)=\Omega\bigl(|V(H)|\log |V(H)|\bigr)
\]

is necessary for an explicit family of **connected** planar graphs. For disjoint unions of triangles, the same order of growth is also an upper bound.

The connected example is useful: the extra logarithm in the pattern size is not merely an artifact of allowing disconnected patterns.

All logarithms below are natural. All final graphs are finite and simple; multigraphs occur only in an intermediate probabilistic construction.

## 1. Statement of the partial result

Write
\[
\nu_H(G)=\max\{\text{number of vertex-disjoint subgraphs containing an \(H\)-minor}\}
\]
and
\[
\tau_H(G)=\min\{|X|:G-X\text{ has no \(H\)-minor}\}.
\]
Define the optimal coefficient
\[
c_*(H)=
\sup_{\substack{G,\ k\ge1\\ \nu_H(G)<k}}
\frac{\tau_H(G)}{k\log(k+1)}.
\]

For \(t\ge1\), let:

* \(D_t\) be the disjoint union of \(t\) triangles;
* \(J_t\) be obtained from \(D_t\) by adding a vertex \(z\), adjacent to one vertex of each triangle.

Thus \(J_t\) is connected and planar, with
\[
|V(D_t)|=3t,\qquad |V(J_t)|=3t+1.
\]

### Partial theorem

There are absolute constants \(a,A>0\) such that, for every \(t\ge2\),
\[
a\,t\log(t+1)\le c_*(D_t)\le A\,t\log(t+1)
\tag{1}
\]
and
\[
c_*(J_t)\ge a\,t\log(t+1).
\tag{2}
\]

Moreover, the lower bounds can be witnessed, for all sufficiently large \(t\), using one fixed packing threshold \(k=K\), where \(K\) is independent of \(t\).

Consequently, a uniform bound \(c(H)=O(|V(H)|)\) is impossible, even when \(H\) is connected and planar.

The complete-graph lower bound from the earlier attempt is correct, but not sharp uniformly over planar patterns. The argument below does not use that attempt’s forest or separator assertions.

---

## 2. The host-graph lemma

The main ingredient is a robust supply of disjoint cycles adjacent to one connected set.

### Lemma

There are absolute constants \(\gamma,\delta,\alpha>0\) such that, for every sufficiently large integer \(N\), there is a simple graph \(G_N\) satisfying:

1. \(|V(G_N)|\le N\);
2. \(\operatorname{girth}(G_N)\ge\gamma\log N\);
3. for every \(X\subseteq V(G_N)\) with \(|X|\le\delta N\), and every positive integer
   \[
   t\le \frac{\alpha N}{\log N},
   \]
   the graph \(G_N-X\) contains \(J_t\) as a minor.

Here girth is infinite for a forest.

### Proof

We first construct a bounded-degree multigraph with expansion, remove its short cycles, and then prove the robustness assertion. Importantly, we do **not** assume that removing the short cycles preserves expansion: all expansion estimates will be made in the original multigraph.

### 2.1. A random regular multigraph with expansion and few short cycles

Fix \(d=64\). Let \(R\) be the random \(d\)-regular configuration multigraph on \(N\) vertices: each vertex has \(d\) labelled half-edges, and a uniformly random perfect matching of the \(dN\) half-edges determines the edges.

We claim that, with probability tending to one,
\[
e_R(S,V(R)\setminus S)>2|S|
\qquad
(1\le |S|\le N/2).
\tag{3}
\]

Fix \(S\) of size \(s\). If its edge boundary has size at most \(2s\), at least \((d-2)s\) half-edges at \(S\) are paired internally. Since \((d-2)s\) is even, some set of exactly \((d-2)s\) half-edges at \(S\) is paired entirely within itself.

For a fixed set of \(m\) half-edges, where \(m\) is even, the probability that all its half-edges are paired internally is
\[
\prod_{j=0}^{m/2-1}
\frac{m-2j-1}{dN-2j-1}
\le \left(\frac{m}{dN}\right)^{m/2}.
\]
It follows that
\[
\Pr\bigl(e_R(S,V(R)\setminus S)\le2s\bigr)
\le
\binom{ds}{2s}
\left(\frac{s}{N}\right)^{(d-2)s/2}.
\]
Taking a union bound over \(S\) gives
\[
\Pr\bigl(\text{(3) fails}\bigr)
\le
\sum_{s=1}^{\lfloor N/2\rfloor}
\left[
B\left(\frac{s}{N}\right)^{30}
\right]^s,
\qquad
B=e(ed/2)^2.
\tag{4}
\]
For \(d=64\), \(B2^{-30}<1\). Splitting the sum at \(\sqrt N\) shows that (4) tends to zero.

Now put
\[
g_N=\left\lfloor\frac{\log N}{4\log d}\right\rfloor.
\]
Count loops as cycles of length one and pairs of parallel edges as cycles of length two. For \(1\le\ell<g_N\), the expected number \(C_\ell\) of cycles of length \(\ell\) is
\[
\mathbb E C_\ell
=
\frac{(N)_\ell[d(d-1)]^\ell}
{2\ell\prod_{j=0}^{\ell-1}(dN-2j-1)}
\le d^\ell
\tag{5}
\]
for sufficiently large \(N\). Thus
\[
\mathbb E\sum_{\ell<g_N}C_\ell=O(N^{1/4}).
\]
By Markov’s inequality, with probability tending to one there are at most \(\sqrt N\) cycles of length less than \(g_N\).

Hence, for every sufficiently large \(N\), we can choose \(R\) satisfying (3) and having at most \(\sqrt N\) such short cycles. Choose one vertex from each short cycle, and let \(Z_0\) be the union of the chosen vertices. Then
\[
|Z_0|\le\sqrt N.
\]
The graph
\[
G_N=R-Z_0
\]
is simple and has girth at least \(g_N\). In particular, for sufficiently large \(N\),
\[
\operatorname{girth}(G_N)\ge\gamma\log N,
\qquad
\gamma=\frac1{8\log d}.
\tag{6}
\]

### 2.2. A giant-component observation

Suppose \(U\subseteq V(R)\), with
\[
u:=|U|<\frac{N}{2d}.
\]
Then \(R-U\) has a unique component \(Q\) with more than \(N/2\) vertices.

Indeed, if no component had more than \(N/2\) vertices, a union \(W\) of components could be chosen with
\[
N/4\le |W|\le N/2.
\]
All edges leaving \(W\) would go to \(U\), so
\[
e_R(W,V(R)\setminus W)\le du<N/2,
\]
contrary to (3).

Let \(B\) denote the union of all components of \(R-U\) other than \(Q\). Since \(|B|<N/2\), expansion also gives
\[
2|B|\le e_R(B,U)\le du,
\]
and therefore
\[
|B|\le \frac d2u.
\tag{7}
\]

### 2.3. Greedily extracting short cycles

Set
\[
\varepsilon=\frac1{100d},\qquad
\eta=\frac{\varepsilon\gamma}{16},\qquad
\delta=\frac{\eta}{4d},\qquad
\alpha=\frac{\eta}{8d}.
\tag{8}
\]

Take an arbitrary \(X\subseteq V(G_N)\) with \(|X|\le\delta N\), and put
\[
Z=Z_0\cup X.
\]
For sufficiently large \(N\),
\[
|Z|\le2\delta N.
\tag{9}
\]

We will select
\[
q=\left\lfloor\frac{\varepsilon N}{8\log N}\right\rfloor
\tag{10}
\]
pairwise vertex-disjoint cycles in \(G_N-X\), each of length at most \(8\log N\).

Suppose some of these cycles have already been selected, and let \(A'\) be their vertex union. Throughout the process,
\[
|A'|\le\varepsilon N.
\]
Set \(U=Z\cup A'\). The constants satisfy \(2\delta\le\varepsilon\), so
\[
|U|\le2\varepsilon N<\frac{N}{2d}.
\]
Let \(Q\) be the giant component of \(R-U\), and let \(B\) be the union of the remaining components. By (7),
\[
|U|+|B|
\le \left(1+\frac d2\right)|U|
\le \varepsilon(d+2)N.
\]
Since \(R\) has \(dN/2\) edges and deleting a vertex removes at most \(d\) edges,
\[
|E(R[Q])|
\ge
\frac{dN}{2}-d\varepsilon(d+2)N
=
\left(\frac d2-\frac{d+2}{100}\right)N
>2N.
\tag{11}
\]
Also, \(R[Q]\) is simple, because \(U\) contains \(Z_0\).

A simple graph with more than twice as many edges as vertices has a nonempty subgraph of minimum degree at least three: otherwise repeatedly deleting vertices of degree at most two would account for at most twice as many edges as vertices.

The usual breadth-first-search argument shows that a graph of minimum degree at least three on at most \(N\) vertices has a cycle of length at most \(8\log N\), for sufficiently large \(N\). For example, a ball of radius \(r\) is a tree if the girth exceeds \(2r+1\), and then has at least \(1+3(2^r-1)\) vertices.

Thus (11) supplies the next cycle. Repeating this constructs all \(q\) cycles.

Let \(A\) be their vertex union. By (6), each selected cycle has length at least \(\gamma\log N\). For sufficiently large \(N\), (10) gives
\[
q\ge\frac{\varepsilon N}{16\log N}.
\]
Consequently,
\[
\eta N\le |A|\le\varepsilon N.
\tag{12}
\]

### 2.4. Many selected cycles meet one connected remainder

Consider the giant component \(Q\) of \(R-(Z\cup A)\), and let \(B\) be the union of the other components. Put
\[
W=A\cup B.
\]
Using (7),
\[
|W|\le \varepsilon N+d\varepsilon N<N/2.
\]
There are no edges between \(B\) and \(Q\). Since \(V(R)\) is partitioned into \(W,Z,Q\), expansion and (9)–(12) give
\[
\begin{aligned}
e_R(A,Q)
&=e_R(W,Q)\\
&\ge 2|W|-d|Z|\\
&\ge 2\eta N-2d\delta N\\
&\ge \eta N.
\end{aligned}
\tag{13}
\]
Each selected cycle has at most \(8\log N\) vertices and hence at most \(8d\log N\) edges to \(Q\). Therefore at least
\[
\frac{\eta N}{8d\log N}
=
\frac{\alpha N}{\log N}
\tag{14}
\]
of the selected cycles have an edge to \(Q\).

Take any \(t\) of these cycles. Contract the connected graph \(Q\) to the hub vertex \(z\). Contract each selected cycle to a triangle, keeping an endpoint of its edge to \(Q\) in one of the triangle’s branch sets. The cycles are mutually vertex-disjoint and avoid \(Q\), so these contractions give a \(J_t\)-minor in \(G_N-X\).

This proves the lemma. ∎

---

## 3. Applying the lemma to the coefficient

Choose an absolute constant
\[
D\ge \max\{2,4/\alpha\},
\]
and, for each sufficiently large \(t\), set
\[
N=\left\lceil D\,t\log(t+1)\right\rceil.
\tag{15}
\]
Since \(D\) is fixed, for sufficiently large \(t\),
\[
\log(t+1)\le\log N\le2\log(t+1)
\]
and
\[
N\le(D+1)t\log(t+1).
\tag{16}
\]
In particular,
\[
\frac{\alpha N}{\log N}\ge\frac{\alpha D}{2}\,t\ge t.
\]
The host-graph lemma therefore implies
\[
\tau_{J_t}(G_N)\ge\delta N.
\tag{17}
\]
Since \(D_t\) is a minor of \(J_t\), it also implies
\[
\tau_{D_t}(G_N)\ge\delta N.
\tag{18}
\]

On the other hand, every subgraph containing either \(D_t\) or \(J_t\) as a minor contains \(t\) vertex-disjoint cycles. Indeed, both patterns contain \(D_t\) as a minor, and a triangle minor is equivalent to the presence of a cycle.

By the girth bound, every such subgraph uses at least
\[
t\gamma\log N
\]
vertices. Thus, for \(H\in\{D_t,J_t\}\),
\[
\nu_H(G_N)
\le
\frac{N}{t\gamma\log N}
\le \frac{D+1}{\gamma}.
\tag{19}
\]

Fix
\[
K=\left\lceil\frac{D+1}{\gamma}\right\rceil+1.
\]
This is an absolute integer, independent of \(t\), and (19) gives \(\nu_H(G_N)<K\). Combining (15), (17), and (18),
\[
\begin{aligned}
c_*(H)
&\ge \frac{\tau_H(G_N)}{K\log(K+1)}\\
&\ge
\frac{\delta D}{K\log(K+1)}
\,t\log(t+1),
\qquad H\in\{D_t,J_t\}.
\end{aligned}
\tag{20}
\]
This proves the asserted lower bounds for all sufficiently large \(t\).

For completeness, the finitely many smaller values can be absorbed by decreasing the absolute constant. If \(H\) has \(h\ge1\) vertices, then
\[
G=K_{2h-1}
\]
satisfies
\[
\nu_H(G)=1,\qquad \tau_H(G)=h.
\]
The first equality follows from the vertex requirement for a minor model; the second follows because any \(h\) vertices of the clique contain \(H\) as a subgraph. Hence
\[
c_*(H)\ge \frac{h}{2\log3}>0.
\]
This also directly verifies the complete-graph construction reused from the previous attempt.

---

## 4. Matching upper bound for disjoint triangles

Here only the classical cycle Erdős–Pósa theorem is needed. It is also the \(H=K_3\) instance of the theorem supplied in the question.

Fix an absolute constant \(A_0\) such that
\[
\nu_{K_3}(G)<q
\quad\Longrightarrow\quad
\tau_{K_3}(G)\le A_0q\log(q+1).
\tag{21}
\]

Grouping cycles into sets of \(t\) gives the exact identity
\[
\nu_{D_t}(G)=
\left\lfloor\frac{\nu_{K_3}(G)}{t}\right\rfloor.
\tag{22}
\]
Thus, if \(\nu_{D_t}(G)<k\), then \(\nu_{K_3}(G)<tk\). A feedback vertex set also hits all \(D_t\)-models, so (21) yields
\[
\tau_{D_t}(G)
\le A_0tk\log(tk+1).
\tag{23}
\]
For \(k,t\ge2\),
\[
\log(tk+1)\le\log(t+1)+\log(k+1),
\]
and consequently
\[
\begin{aligned}
\frac{\tau_{D_t}(G)}{k\log(k+1)}
&\le
A_0t\left(1+\frac{\log(t+1)}{\log(k+1)}\right)\\
&\le
\frac{2A_0}{\log3}\,t\log(t+1).
\end{aligned}
\]
The case \(k=1\) has \(\tau_{D_t}(G)=0\). Taking the supremum proves the upper bound in (1).

We have therefore established
\[
\boxed{c_*(tK_3)=\Theta(t\log(t+1))}
\]
with absolute implied constants.

---

## 5. What this settles, and what remains open

For the connected planar family \(J_t\), with \(h=3t+1\), (20) gives
\[
\boxed{c_*(J_t)=\Omega(h\log h).}
\]

The mechanism is worth distinguishing from the usual lower bound in the packing parameter:

* each model must contain \(t\) disjoint cycles;
* logarithmic girth makes each model consume \(\Omega(t\log N)\) vertices;
* in a host with \(N=\Theta(t\log t)\), only a constant number of models can be packed;
* nevertheless, expansion makes the pattern survive deletion of a positive fraction of the host.

Thus the \(\log t\) cannot be absorbed into \(\log(k+1)\): in these witnesses, \(k=K\) is fixed.

This rules out a uniform linear coefficient, including for connected planar patterns. It does **not** disprove polynomial dependence. In particular, an \(O(h^{1+\varepsilon})\) bound for any fixed \(\varepsilon>0\), or an \(O(h^2)\) bound, is fully compatible with these examples.

The unresolved gap is still a uniform polynomial upper bound for arbitrary planar \(H\), or a family requiring a superpolynomial coefficient. Neither is obtained here.