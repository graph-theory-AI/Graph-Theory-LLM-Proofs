```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a uniform additive-two high-probability bound for shift graphs of order at least three, but do not resolve the conjecture for arbitrary graphs.",
  "would_publish": false,
  "caveats": "Special family only; novelty of the resulting bounds has not been checked."
}
```

# A uniform result for all orders of shift graphs

I do not obtain a proof or counterexample for arbitrary graphs. I do obtain a strengthening of the supplied special-family approach:

- the constants can be made **independent of the order of the shift graph**;
- for orders at least three, the logarithmic loss can be replaced by an **additive loss of two**, with an explicit high-probability bound, once the chromatic number is at least \(11\).

I checked and reuse the supplied attempt’s local-rectangle and sparse-orientation mechanism. The additional ingredient is to **retain the partial order on color types**, rather than treating the types as an unstructured palette. Iterated order-ideal posets then give exact deterministic chromatic thresholds.

All logarithms below are to base \(2\).

## 1. Statement of the partial result

For \(r\ge 1\) and \(N\ge r+1\), let \(S_r(N)\) have as vertices the increasing \(r\)-tuples from \([N]\), with an edge
\[
(a_1,\ldots,a_r)(a_2,\ldots,a_{r+1})
\]
for every \(a_1<\cdots<a_{r+1}\). Thus \(S_1(N)=K_N\).

### Theorem
Let \(r\ge3\), \(N\ge r+1\), and
\[
k=\chi(S_r(N)),\qquad
X=\chi((S_r(N))_{1/2}).
\]
If \(k\ge11\), then
\[
\boxed{\quad
\Pr(X\ge k-2)\ge 1-2^{-r^2}N^{-(r+1)}.
\quad}                                                     \tag{1}
\]
Consequently,
\[
\boxed{\quad
\mathbb E X\ge k-2-\frac{2^{-r^2}}{N}>k-3.
\quad}                                                     \tag{2}
\]

For ordinary shift graphs,
\[
\mathbb E\chi((S_2(N))_{1/2})
\ge k-2\log k-6,
\qquad k=\lceil\log N\rceil.                                \tag{3}
\]

In particular, for **all** \(r\ge2\) and \(N\ge r+1\),
\[
\boxed{\quad
\mathbb E\chi((S_r(N))_{1/2})
\ge \chi(S_r(N))-2\log\chi(S_r(N))-6.
\quad}                                                     \tag{4}
\]
Thus Bukh’s proposed lower bound holds with an absolute constant throughout this entire two-parameter family, even when \(r\) varies with \(N\).

The proof follows.

# 2. Exact chromatic thresholds via order ideals

Let \(D_j(N)\) be the canonical orientation of \(S_j(N)\), directed from
\[
(a_1,\ldots,a_j)\quad\text{to}\quad(a_2,\ldots,a_{j+1}).
\]
The vertices of \(D_j(N)\) are the arcs of \(D_{j-1}(N)\), and its arcs correspond to consecutive arcs of \(D_{j-1}(N)\).

For a finite poset \(P\), write \(J(P)\) for its poset of order ideals, ordered by inclusion.

Define
\[
P_0(q)=\text{an antichain of size }q,\qquad
P_{i+1}(q)=J(P_i(q)),\qquad
a_i(q)=|P_i(q)|.
\]
In particular,
\[
a_0(q)=q,\qquad a_1(q)=2^q.
\]

Call a labeling \(\phi:V(D)\to P\) **\(P\)-admissible** if every arc \(u\to v\) satisfies
\[
\phi(v)\not\le \phi(u).
\]

### Lemma 1: the order-ideal transfer
There is a \(P\)-admissible labeling of \(D_j(N)\) if and only if there is a \(J(P)\)-admissible labeling of \(D_{j-1}(N)\).

#### Proof

First suppose the arcs of \(D_{j-1}(N)\) have labels in \(P\) such that consecutive arcs have labels \(a,b\) satisfying \(b\not\le a\).

For a vertex \(v\) of \(D_{j-1}(N)\), let
\[
I_v=\downarrow\{\phi(e):e\text{ enters }v\}.
\]
For an arc \(e=u\to v\), its label belongs to \(I_v\). It does not belong to \(I_u\): otherwise some arc entering \(u\) would have label at least \(\phi(e)\), violating admissibility. Hence
\[
I_v\not\subseteq I_u.
\]

Conversely, suppose vertices of \(D_{j-1}(N)\) are assigned ideals \(I_v\) with
\[
I_v\not\subseteq I_u
\]
on every arc \(u\to v\). Assign that arc any label in \(I_v\setminus I_u\).

For consecutive arcs \(u\to v\) and \(v\to w\), their labels \(a,b\) satisfy
\[
a\in I_v,\qquad b\notin I_v.
\]
Since \(I_v\) is an ideal, \(b\le a\) is impossible. ∎

Starting with the antichain \(P_0(q)\), admissibility is precisely proper \(q\)-coloring. At the bottom, \(D_1(N)\) is the transitive orientation of \(K_N\).

A finite poset \(P\) admits a \(P\)-admissible labeling of this transitive \(K_N\) exactly when \(|P|\ge N\). Necessity follows because the labels must be distinct. For sufficiency, list \(N\) elements in a linear extension: a later element is never below an earlier one.

We therefore have the exact identity
\[
\boxed{\quad
\chi(S_r(N))
=\min\{q\ge1:N\le a_{r-1}(q)\}.
\quad}                                                     \tag{5}
\]

For \(r=2\), this gives \(\chi(S_2(N))=\lceil\log N\rceil\). For larger \(r\), keeping these exact order-ideal capacities will be important.

# 3. An ordered color-type lemma

A graph \(F\) is \(d\)-orientable if it admits an orientation with maximum outdegree at most \(d\). Necessarily,
\[
e(F[U])\le d|U|                                             \tag{6}
\]
for every vertex set \(U\).

### Lemma 2: ordered types with sparse errors
Let \(D\) be one of the canonical digraphs above, and label its arcs by elements of a finite poset \(P\), where \(|P|=m\).

Suppose that, for every vertex \(v\) and every \(a,b\in P\) with \(b\le a\), it is not the case that both

- at least \(t\) arcs entering \(v\) have label \(a\);
- at least \(t\) arcs leaving \(v\) have label \(b\).

Then vertices of \(D\) can be labeled by ideals \(I_v\in J(P)\) so that all arcs violating
\[
I_v\not\subseteq I_u\qquad(u\to v)
\]
belong to an \(m(t-1)\)-orientable graph.

#### Proof

Let
\[
I_v=\downarrow\{a\in P:
   \text{at least }t\text{ arcs entering }v\text{ have label }a\}.
\]

Two facts follow from the hypothesis:

- if \(c\in I_v\), at most \(t-1\) arcs leaving \(v\) have label \(c\);
- if \(c\notin I_v\), at most \(t-1\) arcs entering \(v\) have label \(c\).

For the first fact, choose a frequent incoming label \(a\ge c\). The hypothesis bounds the number of outgoing arcs labeled \(c\). The second fact follows directly from the definition.

Let \(F\) consist of the arcs \(u\to v\) with \(I_v\subseteq I_u\), viewed as undirected edges. For such an arc with label \(c\):

- if \(c\in I_u\), charge it to \(u\);
- otherwise, \(c\notin I_v\), so charge it to \(v\).

At a vertex \(v\), the number of charged edges is at most
\[
|I_v|(t-1)+(m-|I_v|)(t-1)=m(t-1).
\]
Orient each edge away from the vertex to which it is charged. ∎

Here is the iteration mechanism.

Suppose the vertices of \(D_j(N)\) have labels in \(P\), and every arc violating \(P\)-admissibility belongs to a \(d\)-orientable graph \(F\).

At a vertex of \(D_{j-1}(N)\), there cannot be \(2d+1\) incoming arcs labeled \(a\) and \(2d+1\) outgoing arcs labeled \(b\le a\). All edges of the resulting
\[
K_{2d+1,\,2d+1}
\]
would belong to \(F\), contradicting (6).

Applying Lemma 2 with \(t=2d+1\) therefore gives
\[
\boxed{
\begin{aligned}
&\text{\(P\)-labels on \(D_j(N)\), with \(d\)-orientable violations}\\
&\qquad\Longrightarrow\\
&\text{\(J(P)\)-labels on \(D_{j-1}(N)\), with \(2|P|d\)-orientable violations.}
\end{aligned}}                                             \tag{7}
\]

# 4. Random rectangles and the resulting inequality

Put
\[
L=\log N,\qquad t=\lceil2L\rceil+r.
\]

At each vertex of \(D_{r-1}(N)\), its incoming and outgoing arcs form the two sides of a complete bipartite graph in \(S_r(N)\).

There are at most \(N^{r-1}\) such local bipartite graphs, with at most \(N\) vertices on either side. For fixed sets of \(t\) vertices on each side, the probability that all \(t^2\) corresponding edges are missing is \(2^{-t^2}\).

Thus the probability of any empty local \(t\times t\) rectangle is at most
\[
N^{r-1+2t}2^{-t^2}.
\]
Since \(t\ge2L+r\),
\[
t^2-2tL=t(t-2L)\ge r(2L+r).
\]
Consequently, the failure probability is at most
\[
\delta=2^{-r^2}N^{-(r+1)}.                                 \tag{8}
\]

Let \(\mathcal E\) be the event that there is no such empty rectangle.

On \(\mathcal E\), every proper \(q\)-coloring of the random graph satisfies Lemma 2 with the antichain \(P_0(q)\): otherwise two monochromatic \(t\)-sets would form an empty rectangle. This yields \(P_1(q)\)-labels on \(D_{r-1}(N)\), with violations forming a \(q(t-1)\)-orientable graph.

Now iterate (7). At the bottom, \(D_1(N)\) has labels in \(P_{r-1}(q)\), with violations forming a graph orientable with maximum outdegree at most
\[
d_{\mathrm{final}}
=
2^{r-2}q(t-1)\prod_{i=1}^{r-2}a_i(q).
\]

Every set of vertices with the same final label induces a clique in the violation graph. If its size is \(s\), then
\[
\binom{s}{2}\le d_{\mathrm{final}}s,
\]
so \(s\le2d_{\mathrm{final}}+1\).

Hence, on \(\mathcal E\), the existence of a proper \(q\)-coloring implies
\[
\boxed{\quad
N\le a_{r-1}(q)
\left(
2^{r-1}q(t-1)\prod_{i=1}^{r-2}a_i(q)+1
\right).
\quad}                                                     \tag{9}
\]
The product is empty when \(r=2\).

Importantly, \(\mathcal E\) is independent of the choice of coloring. Thus (9) applies to an optimal coloring chosen after revealing the random graph.

# 5. Two elementary bounds for the ideal capacities

We need growth in the iteration index and growth when two colors are added.

## 5.1. Growth along the iteration

For every \(q\ge8\),
\[
\boxed{\quad
a_{i+1}(q)\ge a_i(q)^4\qquad(i\ge1).
\quad}                                                     \tag{10}
\]

For the first step, the middle level of the Boolean lattice \(P_1(q)\) is an antichain, so
\[
a_2(q)\ge 2^{\binom q{\lfloor q/2\rfloor}}.
\]
For \(q=8\), the exponent is \(70\ge4q\). For \(q\ge9\),
\[
\binom q{\lfloor q/2\rfloor}
\ge \binom q2\ge4q.
\]
Thus \(a_2(q)\ge a_1(q)^4\).

For the induction, abbreviate \(a_i=a_i(q)\). Elements of \(P_i=J(P_{i-1})\) have \(a_{i-1}+1\) possible cardinalities. One cardinality level is therefore an antichain of size at least
\[
\frac{a_i}{a_{i-1}+1}.
\]
Every subset of an antichain generates a different ideal, giving
\[
a_{i+1}\ge 2^{a_i/(a_{i-1}+1)}.
\]
If \(a_i\ge a_{i-1}^4\), then
\[
\frac{a_i}{a_{i-1}+1}\ge \frac12a_i^{3/4}.
\]
Here \(a_i\ge2^{32}\), and the elementary inequality
\[
\frac12x^{3/4}\ge4\log x\qquad(x\ge2^{32})
\]
completes the induction.

We also always have
\[
a_{i+1}(q)\le2^{a_i(q)}.                                  \tag{11}
\]

## 5.2. Adding two colors squares every later capacity

For every \(q\ge2\) and \(i\ge2\),
\[
\boxed{\quad
a_i(q+2)\ge a_i(q)^2.
\quad}                                                     \tag{12}
\]

We prove a stronger order-embedding statement.

First, if \(R\) is an induced subposet of \(P\), then
\[
I\longmapsto\downarrow_P I
\]
is an order embedding \(J(R)\hookrightarrow J(P)\): intersecting the image with \(R\) recovers \(I\).

Now \(P_1(q+2)\), the Boolean lattice on \(q+2\) elements, contains two mutually incomparable copies of \(P_1(q)\). Use the subsets containing exactly one of the two new elements. Taking ideals gives an embedding
\[
P_2(q)\times P_2(q)\hookrightarrow P_2(q+2).
\]

Suppose inductively that
\[
P_i(q)\times P_i(q)\hookrightarrow P_i(q+2).
\]
The poset \(P_i(q)\) has two incomparable elements, since \(q\ge2\), and this property is preserved under taking ideals. Fixing these two elements in the second coordinate produces two mutually incomparable copies of \(P_i(q)\). Taking ideals again gives
\[
P_{i+1}(q)\times P_{i+1}(q)\hookrightarrow P_{i+1}(q+2).
\]
This proves (12).

# 6. Extracting an additive-two bound

Assume \(r\ge3\), \(q\ge8\), and that a proper \(q\)-coloring exists on \(\mathcal E\).

Write
\[
A=a_{r-2}(q),\qquad
M=a_{r-1}(q),\qquad
\mu=\log M,
\]
and
\[
B=2^{r-1}q\prod_{i=1}^{r-2}a_i(q).
\]

We have
\[
A\ge256,\qquad M\ge A^4,\qquad \mu\le A.                    \tag{13}
\]

Repeated use of (10) gives
\[
\prod_{i=1}^{r-2}a_i(q)
\le A^{1+1/4+1/16+\cdots}\le A^2
\]
and
\[
\log A\ge q\,4^{r-3}.
\]
Therefore
\[
2^{r-1}q\le4\log A.
\]
Also \(r\le A\). Since \(4\log A\le A/8\) for \(A\ge256\), it follows that
\[
B\le4(\log A)A^2\le\frac{A^3}{8}.                         \tag{14}
\]

Combining (13) and (14),
\[
B(4\mu+r)+1
\le \frac{A^3}{8}(5A)+1
< A^4
\le M.                                                     \tag{15}
\]

On the other hand, \(t-1\le2L+r\), so (9) gives
\[
2^L\le M\bigl(B(2L+r)+1\bigr).                            \tag{16}
\]

The function
\[
x\longmapsto\frac{2^x}{B(2x+r)+1}
\]
is strictly increasing for \(x\ge2\). At \(x=2\mu\), (15) gives
\[
\frac{2^{2\mu}}{B(4\mu+r)+1}>M.
\]
Thus (16) forces
\[
L<2\mu,
\qquad\text{and hence}\qquad
N<M^2.
\]

By (12),
\[
N<M^2\le a_{r-1}(q+2).
\]
The exact chromatic characterization (5) now implies
\[
\boxed{\quad
\chi(S_r(N))\le q+2.
\quad}                                                     \tag{17}
\]

Let \(X\) be the actual chromatic number of the random graph. Apply the argument with
\[
q=\max\{X,8\}.
\]
On \(\mathcal E\),
\[
k\le\max\{X,8\}+2.
\]
If \(k\ge11\), this forces \(X\ge k-2\). Together with (8), this proves (1).

Finally, \(k\le |V(S_r(N))|\le N^r\), so
\[
\mathbb E X
\ge (1-\delta)(k-2)
\ge k-2-\delta k
\ge k-2-\frac{2^{-r^2}}N.
\]
This proves (2).

# 7. Ordinary shift graphs and the uniform corollary

For \(r=2\), identity (5) gives
\[
k=\lceil L\rceil.
\]
Equation (9) becomes
\[
N\le2^q\bigl(2q(t-1)+1\bigr),
\qquad t=\lceil2L\rceil+2.
\]

For \(N\ge4\), we have \(L\ge2\), \(q\le L+1\), and \(t-1\le2L+2\). Hence
\[
2q(t-1)+1
\le4(L+1)^2+1
\le16L^2.
\]
On \(\mathcal E\),
\[
q\ge L-2\log L-4
\ge k-2\log k-5.
\]

Here \(\Pr(\mathcal E^c)\le1/(16N^3)\). Since \(q\le k\),
\[
\mathbb E(k-q)
\le2\log k+5+\frac{k}{16N^3}
\le2\log k+6.
\]
The remaining case \(N=3\) satisfies the asserted bound trivially. This proves (3).

For \(r\ge3\) and \(k\ge11\), (2) is stronger than (4). For \(2\le k\le10\), the right-hand side of (4) is nonpositive, so (4) is automatic. Thus (4) holds for every order \(r\ge2\).

In particular,
\[
\mathbb E\chi((S_r(N))_{1/2})
=(1-o(1))\chi(S_r(N))
\]
as the chromatic number tends to infinity, **uniformly in \(r\)**.

# 8. Relevance to the original conjecture, and the remaining gap

These are examples with a large integral–fractional chromatic gap. Indeed, for every \(r\ge2\),
\[
\chi_f(S_r(N))\le4.
\]

To see this, view the vertices of \(S_r(N)\) as arcs of \(D_{r-1}(N)\). Choose a random subset \(W\) of the vertices of that digraph, including each vertex independently with probability \(1/2\). The arcs directed from \(W\) to its complement form an independent set in the arc graph: two consecutive arcs cannot both cross in this direction. Each arc belongs to this independent set with probability \(1/4\). Multiplying this distribution by \(4\) gives a fractional coloring of total weight \(4\).

Meanwhile, for every fixed \(r\), equation (5) shows that \(\chi(S_r(N))\to\infty\). Thus the result is not obtainable merely from a lower bound in terms of the fractional chromatic number.

**What remains unresolved:** the argument requires the chain of arc graphs
\[
D_r(N),D_{r-1}(N),\ldots,D_1(N),
\]
the corresponding order-ideal transfer, and the complete graph at the bottom. An arbitrary graph supplies none of this structure. I have not established the desired \(\Omega(\chi(G)/\log\chi(G))\) bound for general \(G\), nor found a counterexample.