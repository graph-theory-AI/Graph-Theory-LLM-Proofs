```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture when 5r >= 2n-3 and when every color class contains an r-edge matching, together with a quantitative reduction showing that long-target counterexamples must be dominated by monochromatic stars.",
  "would_publish": false,
  "caveats": "The bijectively centered all-star case is precisely the Caccetta-Haggkvist obstruction, so the full conjecture remains unresolved."
}
```

# Statement and status

Write the color classes as
\[
E_i=c^{-1}(i),\qquad i\in[n].
\]
A cycle is **properly colored** if its two incident edges at every vertex have different colors.

I do not obtain a proof or counterexample in full. I prove two special cases and a structural reduction:

1. If \(r\ge 2\) and
   \[
   5r\ge 2n-3,
   \]
   then there is in fact a rainbow triangle. In this range \(\lceil n/r\rceil=3\).

2. Let \(\nu_i\) be the matching number of the monochromatic graph \((V(G),E_i)\), and put \(S=\sum_i\nu_i\). Then there is a properly colored cycle of length at most
   \[
   \left\lceil \frac{n^2}{S}\right\rceil.
   \]
   Consequently, the conjecture holds whenever every color class contains a matching of size \(r\).

3. More sharply, if \(k=\lceil n/r\rceil\), \(t=\lfloor k/2\rfloor\), and \(q\) color classes contain two disjoint edges, then any counterexample must satisfy
   \[
   \left(1+\frac{2q}{n}\right)^t\le n.
   \]
   For \(r\ge4\), a color class contains no two disjoint edges exactly when it is a star. Thus a counterexample with \(t\ge\log n\) has fewer than \(4r\log n\) non-star color classes.

The supplied source already proves the conjecture, with a rainbow cycle, for \(r=2\). For \(r=1\), choosing one edge from each color gives \(n\) distinctly colored edges on \(n\) vertices, hence a rainbow cycle of length at most \(n\).

---

# 1. Preliminary reductions

We may delete edges until every color class has exactly \(r\) edges. Finding a desired cycle in the resulting subgraph suffices.

Henceforth, when convenient, assume
\[
|E_i|=r\quad\text{for every }i,
\qquad |E(G)|=nr.
\]
Feasibility gives
\[
nr\le \binom n2,
\qquad\text{so}\qquad
2r\le n-1.
\]
In particular \(n/r>2\), so the conjectured upper bound is always at least \(3\).

A properly colored triangle is the same thing as a rainbow triangle, since every pair of its edges is incident.

---

# 2. A dense-range theorem

## Theorem 2.1

Let \(r\ge2\). If
\[
5r\ge 2n-3,
\]
then \(G\) contains a rainbow triangle. Consequently, Conjecture 4 holds in this range.

## Proof

Trim every color class to exactly \(r\) edges, and suppose for contradiction that the resulting graph has no rainbow triangle.

For a color \(i\) and vertex \(v\), let
\[
d_i(v)=|\{e\in E_i:v\in e\}|.
\]
Define the number of monochromatic wedges by
\[
W=\sum_{i=1}^n\sum_{v\in V(G)}\binom{d_i(v)}2.
\]
For a fixed color \(i\), every wedge is an unordered pair of edges from \(E_i\). Therefore
\[
\sum_v\binom{d_i(v)}2\le \binom r2,
\]
and hence
\[
W\le n\binom r2. \tag{2.1}
\]

Let \(T\) be the number of triangles. Since there is no rainbow triangle, every triangle contains at least one monochromatic wedge. A fixed wedge lies in at most one triangle. Thus
\[
T\le W\le n\binom r2. \tag{2.2}
\]

We now lower-bound \(T\). Let \(d(v)\) denote the ordinary degree of \(v\), and put \(m=nr\). For every edge \(uv\),
\[
|N(u)\cap N(v)|\ge d(u)+d(v)-n.
\]
Summing over edges gives
\[
\begin{aligned}
3T
 &=\sum_{uv\in E(G)}|N(u)\cap N(v)|\\
 &\ge \sum_{uv\in E(G)}(d(u)+d(v)-n)\\
 &=\sum_v d(v)^2-nm\\
 &\ge \frac{(2m)^2}{n}-nm.
\end{aligned}
\]
Since \(m=nr\),
\[
T\ge \frac{nr(4r-n)}3. \tag{2.3}
\]

Combining (2.2) and (2.3),
\[
\frac{nr(4r-n)}3
   \le \frac{nr(r-1)}2.
\]
After cancellation,
\[
5r\le 2n-3. \tag{2.4}
\]
Thus strict inequality \(5r>2n-3\) already gives the theorem.

It remains to exclude equality
\[
5r=2n-3. \tag{2.5}
\]

Under (2.5), every inequality above must be equality. In particular:

1. \(G\) is \(2r\)-regular;
2. for every edge \(uv\),
   \[
   N(u)\cup N(v)=V(G);
   \]
3. every pair of edges in each color class intersects;
4. every monochromatic wedge closes to a triangle;
5. every triangle has exactly one monochromatic wedge.

Since (2.5) and \(r\ge2\) imply that \(r\) is odd, we have \(r\ge3\).

A pairwise intersecting family of at least four graph edges is a star. Indeed, if \(xy,xz\) belong to the family and an edge avoids \(x\), it must be \(yz\); no fourth distinct edge can then meet all three. For \(r=3\), the only additional possibility is a triangle, but a monochromatic triangle would have three monochromatic wedges, contradicting item 5. Thus every color class is a star.

By item 4, the \(r\) leaves of each monochromatic star form a clique in \(G\).

Now consider \(\overline G\). If \(x,y\in N_{\overline G}(w)\) and \(xy\in E(G)\), then \(w\notin N_G(x)\cup N_G(y)\), contradicting item 2. Hence every neighborhood in \(\overline G\) is a clique. It follows that every connected component of \(\overline G\) is complete.

Because \(G\) is \(2r\)-regular, \(\overline G\) is regular of degree
\[
n-1-2r.
\]
Thus \(\overline G\) is a disjoint union of equal cliques of order
\[
n-2r=\frac{r+3}{2}.
\]
Consequently \(G\) is a complete \(p\)-partite graph with equal parts, where
\[
p=\frac{n}{n-2r}
  =\frac{5r+3}{r+3}<5.
\]
Since \(p\) is an integer, \(p\le4\). The leaves of a monochromatic star centered in one part must lie in distinct other parts, so there can be at most \(p-1\le3\) leaves. If \(r\ge5\), this is impossible. If \(r=3\), the formula gives \(p=3\), allowing at most two leaves, again impossible.

Thus equality in (2.4) is also impossible. Therefore a rainbow triangle exists whenever \(5r\ge2n-3\). ∎

Finally, in every feasible instance \(n\ge2r+1\). Under the theorem's hypothesis, \(n\le3r\) for \(r\ge3\), and also for the feasible \(r=2\) cases. Hence
\[
2<\frac nr\le3,
\]
so \(\lceil n/r\rceil=3\), as required.

---

# 3. A matching-core bound

The next result extracts a globally proper subgraph by taking a maximum matching from each color.

## Lemma 3.1: Average-degree Moore bound

Let \(H\) be an \(N\)-vertex graph of average degree \(d\ge2\).

- If \(H\) has no cycle of length at most \(2t\), then
  \[
  N\ge 1+d\sum_{j=0}^{t-1}(d-1)^j. \tag{3.1}
  \]

- If \(H\) has no cycle of length at most \(2t+1\), then
  \[
  N\ge 2\sum_{j=0}^{t}(d-1)^j. \tag{3.2}
  \]

### Proof

Delete vertices of degree at most one until reaching the nonempty \(2\)-core. This does not decrease the average degree, so it is enough to prove the result when every degree is at least two.

Let \(M=|E(H)|\), and let \(W_\ell\) be the number of oriented non-backtracking walks of length \(\ell\). Start with a uniformly random oriented edge and, at every subsequent vertex, choose uniformly among all edges except the one just used. Uniform measure on oriented edges is stationary for this process.

If the successive internal vertices are \(V_1,\dots,V_{\ell-1}\), then
\[
\frac{W_\ell}{2M}
 =
\mathbb E\prod_{j=1}^{\ell-1}\bigl(d(V_j)-1\bigr).
\]
By Jensen's inequality,
\[
\frac{W_\ell}{2M}
 \ge
 \exp\left(
   \sum_{j=1}^{\ell-1}\mathbb E\log(d(V_j)-1)
 \right).
\]
The stationary vertex distribution is degree-biased. Moreover,
\[
x\longmapsto x\log(x-1)
\]
is convex on \([2,\infty)\). Therefore
\[
\frac1{2M}\sum_v d(v)\log(d(v)-1)\ge \log(d-1),
\]
and hence
\[
W_\ell\ge 2M(d-1)^{\ell-1}. \tag{3.3}
\]

Averaging (3.3) over starting vertices shows that some vertex starts at least
\[
1+d\sum_{j=0}^{t-1}(d-1)^j
\]
non-backtracking walks of lengths at most \(t\). If there is no cycle of length at most \(2t\), all their endpoints are distinct, proving (3.1).

Similarly, average over an initial unoriented edge and count non-backtracking continuations of lengths at most \(t\) from both endpoints, avoiding the initial edge. Some edge yields at least
\[
2\sum_{j=0}^{t}(d-1)^j
\]
distinct vertices unless a cycle of length at most \(2t+1\) occurs. This proves (3.2). ∎

## Proposition 3.2

For each color \(i\), let \(\nu_i\) be the matching number of \((V(G),E_i)\), and put
\[
S=\sum_{i=1}^n\nu_i.
\]
Then \(G\) has a properly colored cycle of length at most
\[
\boxed{\left\lceil\frac{n^2}{S}\right\rceil}. \tag{3.4}
\]

### Proof

Choose a maximum matching \(M_i\subseteq E_i\) for each color and let
\[
H=\bigcup_{i=1}^n M_i.
\]
Then \(|E(H)|=S\). Since the edges of each fixed color form a matching in \(H\), the restricted coloring of \(H\) is proper at every vertex. Thus every ordinary cycle in \(H\) is a properly colored cycle in \(G\).

Every color is nonempty, so \(\nu_i\ge1\) and \(S\ge n\). Put
\[
a=\frac Sn,\qquad
K=\left\lceil\frac na\right\rceil
 =\left\lceil\frac{n^2}{S}\right\rceil.
\]
The average degree of \(H\) is \(2a\).

Suppose first that \(K=2t\) and that \(H\) has no cycle of length at most \(K\). Lemma 3.1 gives
\[
n\ge1+2a\sum_{j=0}^{t-1}(2a-1)^j
  \ge1+2at
  =1+Ka.
\]
But \(n\le Ka\), a contradiction.

If \(K=2t+1\), Lemma 3.1 instead gives
\[
n\ge2\sum_{j=0}^{t}(2a-1)^j
 \ge2+2t(2a-1).
\]
The last expression exceeds \(Ka=(2t+1)a\), because
\[
2+2t(2a-1)-(2t+1)a
  =(2t-1)(a-1)+1>0.
\]
Again this contradicts \(n\le Ka\). Hence \(H\), and therefore \(G\), has the required cycle. ∎

## Corollary 3.3

If every color class contains a matching of size \(r\), then Conjecture 4 holds.

Indeed, \(S\ge nr\), so Proposition 3.2 gives a properly colored cycle of length at most
\[
\left\lceil\frac{n^2}{S}\right\rceil
 \le
\left\lceil\frac nr\right\rceil.
\]

In particular, this proves the conjecture whenever every monochromatic class itself is a matching.

More generally, if every class contains an \(s\)-edge matching, then there is a properly colored cycle of length at most \(\lceil n/s\rceil\). For \(s\ge2\), Lemma 3.1 also gives the logarithmic bound
\[
g_{\rm pc}(G,c)
 \le
 2\left\lceil\log_{2s-1}n\right\rceil+1. \tag{3.5}
\]

---

# 4. Quantitative reduction to monochromatic stars

Let
\[
k=\left\lceil\frac nr\right\rceil,
\qquad
t=\left\lfloor\frac k2\right\rfloor,
\]
and let \(q\) be the number of color classes with matching number at least two. Then
\[
S\ge n+q,
\]
so the matching-core graph has average degree at least
\[
2+\frac{2q}{n}.
\]

If there were no properly colored cycle of length at most \(k\), Lemma 3.1 would imply, in either parity of \(k\),
\[
n\ge \left(1+\frac{2q}{n}\right)^t.
\]
Thus every counterexample must satisfy
\[
\boxed{
q\le \frac n2\left(n^{1/t}-1\right).
} \tag{4.1}
\]

For \(r\ge4\), a monochromatic class has matching number one if and only if it is a star. To see this, a matching-number-one class is a pairwise intersecting family of graph edges. As in the equality argument above, a pairwise intersecting family which is not a star has at most three edges.

Consequently, for \(r\ge4\), \(q\) is precisely the number of non-star color classes. In particular:

- If every color class is non-star, then a counterexample would require
  \[
  3^t\le n.
  \]
  Hence the conjecture holds whenever
  \[
  3^{\lfloor\lceil n/r\rceil/2\rfloor}>n.
  \]

- If \(t\ge\log n\), then using \(e^x-1\le2x\) for \(0\le x\le1\), (4.1) gives
  \[
  q\le \frac{n\log n}{t}.
  \]
  Since
  \[
  t\ge\frac{n/r-1}{2}
  \]
  and feasibility gives \(r\le(n-1)/2\),
  \[
  q<4r\log n. \tag{4.2}
  \]

Thus, when the target length is at least logarithmic and \(r\log n=o(n)\), any counterexample must have all but \(O(r\log n)\) color classes equal to stars.

---

# 5. The remaining hard core

The star case cannot be dismissed: it contains the Caccetta–Häggkvist conjecture exactly.

Let \(D\) be an oriented graph on \(n\) vertices with minimum outdegree at least \(r\). Form its underlying graph and color every edge \(uv\), corresponding to an arc \(u\to v\), by its tail \(u\). Then:

- there are \(n\) colors;
- every color class is a star centered at the corresponding vertex;
- every color class has size at least \(r\).

For a cycle in the underlying graph, the two incident edges at a vertex \(v\) have the same color precisely when both cycle edges are oriented out of \(v\). Hence a properly colored cycle has no source in its cyclic orientation. Since a cycle has as many arcs as vertices, absence of a source forces every vertex to have one incoming and one outgoing cycle edge. Therefore the cycle is directed.

Conversely, every directed cycle is properly colored. Thus, on these bijectively centered star colorings, the conjectured bound is exactly the Caccetta–Häggkvist bound.

This explains the limitation of the matching argument: in this hard subclass every \(\nu_i=1\), so \(S=n\), and Proposition 3.2 only returns the trivial upper bound \(n\).

---

# 6. What remains open

The principal unresolved cases include:

- the triangle range
  \[
  \frac n3\lesssim r<\frac{2n-3}{5},
  \]
  where the desired cycle has length three;

- configurations in which almost every color class is a star, especially when the star centers are in bijection with the vertices;

- more generally, any proof improving the star-centered case to the exact \(\lceil n/r\rceil\) bound would have to overcome the Caccetta–Häggkvist obstruction.

No computational verification is claimed here, and I have not checked whether the two partial lemmas above already occur in the literature in this precise formulation.