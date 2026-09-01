```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but a sharp random-orientation criterion reduces the upper bound to a one-scale local-density estimate, and exact bipartite and complexity side results are proved.",
  "would_publish": false,
  "caveats": "No triangle-free graph is shown to satisfy the required local-density estimate at the conjectured scale, so the logarithmic gap is not closed."
}
```

# 1. Statement and status

For an oriented graph \(D\), let \(\vec\alpha(D)\) be the maximum number of vertices in an induced acyclic subdigraph. Define
\[
\vec a(n)=\min\{\vec\alpha(D): |V(D)|=n,\ U(D)\text{ is triangle-free}\},
\]
where \(U(D)\) denotes the underlying undirected graph.

The conjecture is
\[
\vec a(n)=\Theta(\sqrt{n\log n}).
\]
The quoted lower bound already has this order, so the unresolved direction is the existence of an oriented triangle-free graph in which every acyclic set has \(O(\sqrt{n\log n})\) vertices.

All logarithms below are natural.

The main contribution here is a quantitative orientation lemma. It shows precisely what one-sided local-density estimate for a triangle-free-process graph would suffice, and improves the naive union bound over topological orders by a factor of two in the leading density threshold. I do not prove that the triangle-free process satisfies this estimate.

# 2. Counting acyclic orientations by indegree vectors

For a graph \(H\), write \(\operatorname{ao}(H)\) for its number of acyclic orientations.

## Lemma 2.1

For every finite simple graph \(H\),
\[
\operatorname{ao}(H)\leq \prod_{v\in V(H)}(d_H(v)+1).
\]

### Proof

Associate to each acyclic orientation \(Q\) its indegree vector
\[
\bigl(d_Q^-(v):v\in V(H)\bigr).
\]
I claim that this map is injective.

Suppose two acyclic orientations \(Q,Q'\) have the same indegree vector, and let \(F\) be the set of edges on which they differ. Orient \(F\) as in \(Q\). Since every edge of \(F\) is reversed in \(Q'\), equality of the two indegree vectors implies
\[
d^-_{Q[F]}(v)=d^+_{Q[F]}(v)
\]
at every vertex \(v\). If \(F\neq\varnothing\), the balanced digraph \(Q[F]\) contains a directed cycle, contradicting the acyclicity of \(Q\). Thus \(F=\varnothing\).

There are at most \(d_H(v)+1\) possible indegrees at \(v\), proving the result. \(\square\)

By the arithmetic-geometric mean inequality, if \(H\) has \(s\) vertices, \(m\) edges, and average degree \(\bar d=2m/s\), then
\[
\operatorname{ao}(H)
 \leq \prod_v(d_H(v)+1)
 \leq (1+\bar d)^s.
\]

# 3. A random-orientation criterion

## Theorem 3.1

Let \(G\) be any graph on \(n\) vertices and \(1\leq k\leq n\). If
\[
\sum_{\substack{S\subseteq V(G)\\ |S|=k}}
2^{-e(G[S])}\prod_{v\in S}\bigl(d_{G[S]}(v)+1\bigr)<1,
\tag{3.1}
\]
then \(G\) has an orientation \(D\) satisfying
\[
\vec\alpha(D)<k.
\]

### Proof

Orient every edge of \(G\) independently and uniformly. For a fixed \(k\)-set \(S\), the restriction to \(G[S]\) is uniformly distributed over its \(2^{e(G[S])}\) orientations. Hence
\[
\Pr(D[S]\text{ is acyclic})
 =\frac{\operatorname{ao}(G[S])}{2^{e(G[S])}}
 \leq
 2^{-e(G[S])}\prod_{v\in S}(d_{G[S]}(v)+1).
\]
Thus the left side of (3.1) bounds the expected number of acyclic \(k\)-sets. If it is less than one, some orientation has no acyclic \(k\)-set.

An acyclic set of more than \(k\) vertices would contain an acyclic \(k\)-set, so that orientation has \(\vec\alpha(D)<k\). \(\square\)

This is useful because condition (3.1) permits a small family of sparse exceptional sets. Requiring every \(k\)-set to be dense is stronger than necessary.

## Corollary 3.2: a uniform local-density version

Suppose every \(k\)-vertex set \(S\) satisfies
\[
\overline d(G[S])\geq d_0,
\]
where \(d_0>2/\log 2-1\), and
\[
\binom nk\left((1+d_0)2^{-d_0/2}\right)^k<1.
\tag{3.2}
\]
Then \(G\) has an orientation \(D\) with \(\vec\alpha(D)<k\).

### Proof

For \(d>2/\log 2-1\), the function
\[
(1+d)2^{-d/2}
\]
is decreasing. Lemma 2.1 and the arithmetic-geometric mean inequality therefore give, for every \(k\)-set \(S\),
\[
\Pr(D[S]\text{ acyclic})
 \leq (1+d_0)^k2^{-d_0k/2}.
\]
A union bound gives (3.2). \(\square\)

## Corollary 3.3: calibration at the conjectured scale

Fix \(C,\varepsilon>0\), and put
\[
k=\left\lceil C\sqrt{n\log n}\right\rceil.
\]
Suppose a triangle-free graph \(G\) on \(n\) vertices satisfies
\[
\overline d(G[S])
 \geq \left(\frac1{\log 2}+\varepsilon\right)\log n
\tag{3.3}
\]
for every \(k\)-set \(S\). Then, for sufficiently large \(n\), \(G\) has an orientation \(D\) with
\[
\vec\alpha(D)<k.
\]

### Proof

Here
\[
\log\frac{en}{k}
 =\frac12\log n-\frac12\log\log n+O(1).
\]
The logarithm, divided by \(k\), of the right side in (3.2) is at most
\[
\log\frac{en}{k}+\log(1+d_0)-\frac{\log 2}{2}d_0.
\]
For \(d_0=(1/\log 2+\varepsilon)\log n\), this equals
\[
-\frac{\varepsilon\log 2}{2}\log n
 +\frac12\log\log n+O(1),
\]
which is negative for sufficiently large \(n\). \(\square\)

Equivalently, it suffices that every relevant \(S\) span at least
\[
\left(\frac{1}{2\log 2}+\Omega(1)\right)|S|\log n
\tag{3.4}
\]
edges.

# 4. What this asks from the triangle-free process

Suppose a triangle-free graph \(G\) has, uniformly over all \(k\)-sets,
\[
e(G[S])\geq (1-o(1))p\binom{k}{2},
\qquad
p=\rho\sqrt{\frac{\log n}{n}},
\tag{4.1}
\]
where
\[
k=C\sqrt{n\log n}.
\]
Then
\[
\overline d(G[S])\geq (1-o(1))pk
 =(1-o(1))\rho C\log n.
\]
Consequently, Corollary 3.3 applies whenever
\[
\rho C>\frac1{\log 2}.
\tag{4.2}
\]

For illustration, if the relevant process density has \(\rho=1/\sqrt2\), the resulting numerical threshold is
\[
C>\frac{\sqrt2}{\log 2}\approx 2.041.
\]
This is only a calibration, not a claim that (4.1) has been proved for the final triangle-free process.

The improvement over the most naive argument is worth recording. Counting a topological order separately gives
\[
\Pr(D[S]\text{ acyclic})\leq k!\,2^{-e(G[S])},
\]
and after union over \(S\) this effectively asks for average degree about
\[
\frac{2}{\log 2}\log n.
\]
Lemma 2.1 reduces the leading requirement to
\[
\frac{1}{\log 2}\log n.
\]

## The remaining gap

Neither the total edge count of a triangle-free-process graph nor its independence-number bound implies (3.3). Indeed, if \(\alpha(G)\leq A\), then Caro--Wei applied to \(G[S]\) gives only
\[
A\geq \alpha(G[S])
 \geq \frac{|S|}{1+\overline d(G[S])}.
\]
For \(|S|=CA\), this forces merely
\[
\overline d(G[S])\geq C-1,
\]
rather than \(\Theta(\log n)\).

There are also adaptively chosen sparse sets in every triangle-free graph: each neighborhood \(N(v)\) is independent. Thus a binomial calculation for a predetermined set does not establish a uniform statement over all sets selected after the process has run.

A proof of either

1. the uniform estimate (3.3), for some sufficiently large constant \(C\), or
2. the weaker weighted estimate (3.1),

for an appropriate triangle-free-process graph would prove the conjectured upper bound. Establishing either estimate is exactly the unfilled part of this approach.

# 5. An exact bipartite special case

Although bipartite graphs are far from extremal for the original problem, the restricted problem can be solved exactly.

## Theorem 5.1

For all sufficiently large \(m\),
\[
\min\{\vec\alpha(D): U(D)=K_{m,m}\}=m+1.
\]

Consequently, among orientations of bipartite graphs on \(2m\) vertices, the minimum possible acyclic number is \(m+1\) for sufficiently large \(m\).

### Proof

Let the two parts be \(L,R\), each of order \(m\). For every orientation, \(L\cup\{r\}\), with \(r\in R\), induces an oriented star together with isolated vertices. It is acyclic, so
\[
\vec\alpha(D)\geq m+1.
\]

For the reverse bound, orient every edge of \(K_{m,m}\) independently. For fixed sets \(A\subseteq L\), \(B\subseteq R\), with \(|A|=a\), \(|B|=b\), Lemma 2.1 gives
\[
\Pr(D[A\cup B]\text{ acyclic})
 \leq \frac{(b+1)^a(a+1)^b}{2^{ab}}.
\tag{5.1}
\]

It remains to show that the expected number of acyclic sets with at least \(m+2\) vertices tends to zero. Such a set has \(a,b\geq2\). By symmetry assume \(2\leq b\leq a\).

For \(b=2\), necessarily \(a=m\), and the total contribution is at most
\[
\binom m2\left(\frac34\right)^m(m+1)^2=o(1).
\]

For \(b=3\), one has \(a\in\{m-1,m\}\), and the contribution is
\[
\operatorname{poly}(m)\,2^{-m}=o(1).
\]

Suppose \(4\leq b<m/4\). Since \(a+b\geq m+2\), one has \(m-a\leq b-2\). Put
\[
q_b=\frac{b+1}{2^b}.
\]
For each pair \((a,b)\), its contribution is at most
\[
(2m^3)^b q_b^{m-b}.
\]
For \(b\geq4\),
\[
q_b\leq 2^{-b/3}.
\]
As \(m-b\geq3m/4\),
\[
(2m^3)^b q_b^{m-b}
 \leq (2m^3)^b2^{-bm/4}=o(m^{-2}),
\]
uniformly in this range.

Finally, if \(b\geq m/4\), then \(a\geq m/2\) and \(ab\geq m^2/8\). Summing crudely over all choices of \(A,B\), the contribution is at most
\[
2^{2m}(m+1)^{2m}2^{-m^2/8}=o(1).
\]

Thus with positive probability there is no acyclic set of order at least \(m+2\), while every orientation has one of order \(m+1\). \(\square\)

This confirms that even very dense triangle-free underlying graphs need not have acyclic sets substantially larger than their largest independent side. However, bipartiteness itself forces a linear-sized acyclic set and therefore does not approach the conjectured extremal regime.

# 6. Complexity of finding a maximum acyclic set

The optimization problem remains hard even under the stronger restriction that the underlying graph is bipartite.

## Theorem 6.1

The following problem is NP-complete:

> Given an oriented bipartite graph \(D\) and an integer \(q\), decide whether \(\vec\alpha(D)\geq q\).

### Proof

Membership in NP is immediate. We reduce from Vertex Cover.

Let \(G=(V,E)\) be a simple graph, let \(r=|V|\), and set \(M=r+1\). Create one vertex \(x_v\) for each \(v\in V\). For every edge \(e=\{u,v\}\), choose an arbitrary ordering \((u,v)\), and for every \(i\in[M]\) create two new vertices \(a_{e,i},b_{e,i}\) and the directed 4-cycle
\[
x_u\longrightarrow a_{e,i}\longrightarrow x_v
\longrightarrow b_{e,i}\longrightarrow x_u.
\tag{6.1}
\]
There are no other arcs.

The underlying graph is bipartite, with all \(x_v\) in one part and all \(a_{e,i},b_{e,i}\) in the other.

Let \(\tau_{\rm DFVS}(D)\) be the minimum order of a directed feedback vertex set. I claim
\[
\tau_{\rm DFVS}(D)=\tau(G),
\tag{6.2}
\]
where \(\tau(G)\) is the vertex-cover number of \(G\).

If \(C\) is a vertex cover of \(G\), deleting \(\{x_v:v\in C\}\) destroys every directed cycle: each gadget (6.1) then has at most one original endpoint remaining, and all its new vertices have residual undirected degree at most one. Hence
\[
\tau_{\rm DFVS}(D)\leq\tau(G).
\]

Conversely, deleting all \(r\) original vertices is a feedback vertex set, so a minimum feedback vertex set \(F\) has
\[
|F|\leq r<M.
\]
If an edge \(uv\in E(G)\) had both \(x_u,x_v\notin F\), then for each \(i\in[M]\), at least one of \(a_{e,i},b_{e,i}\) would have to lie in \(F\) to break the corresponding directed 4-cycle. This would give \(|F|\geq M\), a contradiction. Therefore
\[
\{v:x_v\in F\}
\]
is a vertex cover of \(G\), so \(|F|\geq\tau(G)\). This proves (6.2).

Since
\[
\vec\alpha(D)=|V(D)|-\tau_{\rm DFVS}(D),
\]
the reduction is complete. \(\square\)

I have not checked whether this auxiliary complexity statement has appeared previously, so no novelty claim is made for it.

# 7. Conclusion

The conjecture is not proved or disproved. The sharpest rigorous reduction obtained here is:

> It is enough to find, for some \(C\), a triangle-free graph \(G\) on \(n\) vertices such that either the weighted sum (3.1) is less than one for \(k=C\sqrt{n\log n}\), or every such \(k\)-set has average degree at least \((1/\log 2+\varepsilon)\log n\).

A random orientation would then complete the construction. What remains unproved is precisely the required local or weighted density estimate for a suitable triangle-free-process graph.