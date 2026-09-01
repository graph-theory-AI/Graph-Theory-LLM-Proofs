```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but independent vertex-exchangeable query schemes require \u03a9(\u0394\u00b2 log \u0394) queries, so any optimal construction must use substantial correlation between its queries.",
  "would_publish": false,
  "caveats": "Assumes the standard adversarial oracle returning an arbitrary MIS of each queried induced subgraph."
}
```

# Mathematical writeup

## 1. Model and normalization

I use the standard model implicit in the source paper:

- The unknown graph is \(G=(V,E)\), with \(|V|=n\) and \(\Delta(G)\leq \Delta\).
- A query is a set \(Q\subseteq V\).
- The oracle returns an arbitrary maximal independent set of \(G[Q]\).
- All queries are chosen before any answers are received.
- Correctness is required for every valid choice of maximal independent sets by the oracle.

For ratios \(n/\Delta\) close to \(1\), the literal expression \(\log(n/\Delta)\) can be smaller than a constant. I therefore write
\[
L(r)=\max\{1,\log r\},\qquad r=\frac n\Delta.
\]
In the usual range \(n\ge 2\Delta\), this is equivalent up to constants to \(\log(n/\Delta)\).

I do not prove or disprove the proposed
\[
O\!\left(\Delta^2 L(n/\Delta)\right)
\]
bound.

---

## 2. The standard sufficient separation property

For a nonedge \(uv\notin E(G)\), suppose a query \(Q\) satisfies
\[
u,v\in Q,\qquad Q\cap\bigl(N_G(u)\cup N_G(v)\bigr)=\varnothing. \tag{1}
\]
Then \(u\) and \(v\) are isolated vertices of \(G[Q]\). Every maximal independent set of \(G[Q]\) must therefore contain both of them.

Consequently, a query family \(\mathcal Q\) reconstructs \(G\) if
\[
\forall uv\notin E(G)\quad
\exists Q\in\mathcal Q:
\{u,v\}\subseteq Q,\quad
Q\cap(N(u)\cup N(v))=\varnothing. \tag{2}
\]
Indeed, an edge can never occur as a pair in an oracle answer, while every nonedge occurs together in some answer under (2).

If each vertex is included independently with probability \(p=1/(2\Delta)\), then for a fixed nonedge \(uv\),
\[
\Pr[(1)]
=p^2(1-p)^{|N(u)\cup N(v)|}
\ge \frac{1}{16\Delta^2}.
\]
Thus \(O(\Delta^2\log n)\) independent queries suffice by a union bound over all pairs. This is the familiar upper-bound mechanism.

---

## 3. Easy ranges where the target is already attained

Two elementary upper bounds can be combined.

### 3.1 Existing randomized upper bound

The given upper bound is
\[
O(\Delta^2\log n).
\]
Hence the desired estimate already follows whenever
\[
\log \Delta=O\!\left(\log\frac n\Delta\right).
\]
For example, for every fixed \(\varepsilon>0\), if
\[
\Delta\le n^{1-\varepsilon},
\]
then
\[
\log(n/\Delta)\ge \varepsilon\log n,
\]
and therefore
\[
O(\Delta^2\log n)
=O_\varepsilon\!\left(\Delta^2\log(n/\Delta)\right).
\]

Equivalently, the question is only substantial when \(n/\Delta\) grows much more slowly than every relevant power of \(\Delta\).

### 3.2 Exact pair queries

Querying every two-element set reconstructs \(G\) deterministically:

- if \(uv\notin E(G)\), the unique maximal independent set of \(G[\{u,v\}]\) is \(\{u,v\}\);
- if \(uv\in E(G)\), every returned MIS is a singleton.

This uses \(\binom n2=O(n^2)\) queries. Therefore
\[
q(n,\Delta)
=O\!\left(\Delta^2
   \min\left\{\log n,\left(\frac n\Delta\right)^2\right\}\right). \tag{3}
\]
In particular, the target holds when \(n/\Delta=O(1)\).

Thus the genuinely unresolved window is roughly
\[
1\ll \frac n\Delta,\qquad
\log(n/\Delta)=o(\log\Delta),
\]
where neither branch of (3) has the conjectured order.

---

## 4. A hard family: cliques with optional matching edges

The following family isolates a structural obstruction.

Let \(s=\Delta\). Partition \(V\) into \(r\) disjoint sets
\[
C_1,\dots,C_r,\qquad |C_i|=s,
\]
and put a clique on each \(C_i\). Choose two of them,
\[
C=C_1=\{u_1,\dots,u_s\},\qquad
D=C_2=\{v_1,\dots,v_s\},
\]
and fix the perfect matching
\[
M=\{u_iv_i:1\le i\le s\}.
\]

For \(X\subseteq[s]\), let \(G_X\) be the graph obtained by adding the matching edges \(u_iv_i\) for \(i\in X\). Since vertices of \(C\cup D\) initially have degree \(s-1\), every \(G_X\) has maximum degree at most \(s=\Delta\).

Call a query \(Q\) an exposure of \(i\) if
\[
Q\cap C=\{u_i\},\qquad Q\cap D=\{v_i\}. \tag{4}
\]

### Lemma 4.1

There is a valid adversarial MIS-answering rule under which the transcript depends on \(X\) only through those coordinates \(i\) exposed by at least one query.

#### Proof

Fix a query \(Q\), and write
\[
A=Q\cap C,\qquad B=Q\cap D.
\]

In every clique other than \(C,D\), choose one arbitrary queried vertex whenever the intersection is nonempty.

For \(C,D\):

1. If either \(A\) or \(B\) is empty, choose one vertex from each nonempty set.
2. If \(A=\{u_i\}\) and \(B=\{v_i\}\), then:
   - if \(i\notin X\), choose both \(u_i,v_i\);
   - if \(i\in X\), choose only \(u_i\).
3. In every other case with \(A,B\ne\varnothing\), choose
   \[
   a\in A,\qquad b\in B
   \]
   such that \(ab\notin M\). Such a pair exists unless \(A,B\) are the matching singletons in case 2.

The resulting set is independent in \(G_X[Q]\). It is maximal because every unselected queried vertex in an original clique is adjacent to the selected representative of that clique; in case 2 with \(i\in X\), the omitted \(v_i\) is adjacent to \(u_i\).

Outside case 2, this answer is independent of \(X\). In case 2, it reveals exactly the bit \(1_{i\in X}\). ∎

Thus, against adversarial MIS answers, nonadaptive reconstruction of this family contains a coupon-collection problem: all relevant matching coordinates must be exposed.

More precisely, if \(Z\) matching coordinates are never exposed, then under uniform random \(X\subseteq[s]\), any decoder has conditional success probability at most
\[
2^{-Z}. \tag{5}
\]

---

## 5. Independent exchangeable queries cannot close the gap

A random query is called vertex-exchangeable if its distribution is invariant under all permutations of \(V\). This includes:

- Bernoulli queries with a common inclusion probability;
- uniformly random fixed-size queries;
- independent mixtures of such distributions.

The rows may have different exchangeable distributions.

### Proposition 5.1

Let \(Q_1,\dots,Q_m\) be mutually independent, vertex-exchangeable random queries. For every fixed \(\varepsilon>0\), if
\[
m\le (1-\varepsilon)\Delta^2\log\Delta, \tag{6}
\]
then there is a graph of maximum degree at most \(\Delta\), and a valid MIS oracle for that graph, on which the reconstruction success probability tends to zero as \(\Delta\to\infty\).

#### Proof

Apply the preceding construction with \(s=\Delta\).

For query \(Q_t\), let
\[
E_{t,i}=\{Q_t\cap C=\{u_i\},\ Q_t\cap D=\{v_i\}\}.
\]
By exchangeability,
\[
\Pr(E_{t,i})=a_t
\]
is independent of \(i\). For fixed \(t\), the \(s^2\) events
\[
\{Q_t\cap C=\{u\},\ Q_t\cap D=\{v\}\},
\qquad (u,v)\in C\times D,
\]
are pairwise disjoint. Hence
\[
a_t\le \frac1{s^2}. \tag{7}
\]

Let \(Z_i\) be the indicator that coordinate \(i\) is never exposed, and set
\[
Z=\sum_{i=1}^s Z_i.
\]
Independence of the query rows gives
\[
\Pr(Z_i=1)=\prod_{t=1}^m(1-a_t)
\ge \left(1-\frac1{s^2}\right)^m.
\]
Therefore
\[
\mathbb E Z
\ge s\left(1-\frac1{s^2}\right)^m. \tag{8}
\]
Under (6),
\[
\mathbb E Z\ge s^{\varepsilon-o(1)}\longrightarrow\infty. \tag{9}
\]

For \(i\ne j\), events \(E_{t,i}\) and \(E_{t,j}\) are disjoint, so
\[
\Pr(Z_i=Z_j=1)=\prod_t(1-2a_t)
\le \prod_t(1-a_t)^2.
\]
Thus the indicators \(Z_i\) have nonpositive pairwise covariance and
\[
\operatorname{Var}Z\le \mathbb E Z. \tag{10}
\]
It follows that
\[
\Pr\left(Z<\frac12\mathbb E Z\right)
\le \frac{4}{\mathbb E Z}=o(1).
\]
Consequently,
\[
\mathbb E[2^{-Z}]
\le
\Pr\left(Z<\frac12\mathbb E Z\right)
+2^{-\mathbb E Z/2}
=o(1). \tag{11}
\]

Choose \(X\subseteq[s]\) uniformly and use the valid answering rule from Lemma 4.1. By (5) and (11), the average reconstruction success probability over \(X\) is \(o(1)\). Hence some fixed \(X\) has success probability \(o(1)\). The corresponding \(G_X\) has maximum degree at most \(\Delta\). ∎

### Consequence

Take, for example,
\[
\frac n\Delta=r=\lceil\log\Delta\rceil.
\]
Then
\[
\Delta^2\log(n/\Delta)
=\Theta(\Delta^2\log\log\Delta)
=o(\Delta^2\log\Delta).
\]
Therefore no algorithm based on mutually independent, individually exchangeable random queries can attain the proposed bound uniformly in \(n,\Delta\).

In particular, merely changing the Bernoulli inclusion probability, using several independently sampled probabilities, or replacing Bernoulli rows by independent random fixed-size rows cannot solve the problem.

For ordinary Bernoulli-\(p\) rows, the probability of exposing a specified matching edge is exactly
\[
a(p)=p^2(1-p)^{2\Delta-2},
\]
maximized at \(p=1/\Delta\), where
\[
a(1/\Delta)
=\frac1{\Delta^2}\left(1-\frac1\Delta\right)^{2\Delta-2}
\sim \frac{e^{-2}}{\Delta^2}.
\]
Thus the usual coupon-collector threshold is explicitly
\[
\Theta(\Delta^2\log\Delta)
\]
even for this restricted graph family.

---

## 6. Why this is not a counterexample to the conjecture

The preceding lower bound depends essentially on independence between the query rows. Correlation can remove the coupon-collector loss.

Here is a self-contained benchmark illustrating this. Suppose the clique partition
\[
C_1,\dots,C_r,\qquad |C_i|\le s,
\]
were known to the query designer. Choose a power of two \(q\) with
\[
s\le q<2s
\]
and label the vertices of each \(C_i\) injectively by elements of \(\mathbb F_q\).

Let
\[
k=\lceil\log_q r\rceil
\]
and assign distinct vectors \(x_i\in\mathbb F_q^k\) to the cliques. For every coordinate \(\ell\in[k]\) and every \(A,B\in\mathbb F_q\), form a query that selects from \(C_i\) the vertex labelled
\[
A x_{i,\ell}+B,
\]
if that label is used in \(C_i\).

For distinct \(i,j\), choose a coordinate \(\ell\) with
\[
x_{i,\ell}\ne x_{j,\ell}.
\]
Given arbitrary labels \(\alpha,\beta\in\mathbb F_q\), the equations
\[
A x_{i,\ell}+B=\alpha,\qquad
A x_{j,\ell}+B=\beta
\]
have a unique solution \(A,B\). Hence every prescribed pair of vertices in different cliques is selected together, with at most one selected vertex from each clique.

The number of queries is
\[
kq^2
=O\!\left(s^2\left(1+\frac{\log r}{\log s}\right)\right)
=O(s^2(1+\log r)). \tag{12}
\]
Thus a highly correlated algebraic schedule avoids the \(\log s\) coupon-collector term when the relevant partition is known.

This does not solve reconstruction: in the actual problem, the clique partition—or, more generally, the neighborhoods that must be avoided—is itself hidden. It only shows why Proposition 5.1 cannot be promoted directly to a general lower bound.

---

## 7. Precise remaining gap

The clique-plus-matching family already imposes the following necessary test on any proposed algorithm:

> For every fixed partition into \(\Delta\)-cliques and every fixed perfect matching between two cliques, the random query family must, with high probability, expose every matching pair, while using only \(O(\Delta^2\log(n/\Delta))\) rows.

Independent exchangeable rows fail this test by Proposition 5.1. Partition-aware correlated arrays pass it, but depend on hidden graph structure.

For arbitrary graphs, the stronger direct route would be to construct a correlated random family satisfying
\[
\forall uv\notin E(G)\quad
\exists Q:\quad
u,v\in Q,\quad
Q\cap(N(u)\cup N(v))=\varnothing
\]
with only \(O(\Delta^2\log(n/\Delta))\) queries for every fixed \(G\). I do not have such a construction, nor a lower bound excluding one.

Hence the original problem remains open. The concrete partial conclusion is that an optimal algorithm, if it exists, cannot be a fresh-independent-sampling refinement of the known \(O(\Delta^2\log n)\) argument; it must use substantial correlation or a different decoding mechanism.