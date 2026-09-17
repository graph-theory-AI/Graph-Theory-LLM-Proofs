```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The cograph case has a sharp order bound of 2n-4, while random graphs force any general threshold to be at least n log n - 2n log log n - O(n).",
  "would_publish": false,
  "caveats": "No general upper threshold is proved for n >= 7; the cograph case is vacuous beyond its order bound, and novelty is not asserted."
}
```

## 1. Scope and results

All graphs below are finite and simple. Write
\[
\tau(G)=\min\{|X|:G-X\text{ is planar}\},
\]
and let \(h(G)\) denote the largest order of a complete minor of \(G\).

For \(n\ge5\), Thomas’s question asks whether there is a threshold \(M(n)\) such that
\[
|V(G)|\ge M(n),\qquad \kappa(G)\ge n,\qquad h(G)<n
\quad\Longrightarrow\quad
\tau(G)\le n-5.
\]
The threshold may depend on \(n\).

I do not resolve this assertion for unrestricted graphs. I prove two partial results:

1. **Sharp cograph case.** Every \(n\)-connected cograph without a \(K_n\) minor has at most \(2n-4\) vertices. For every \(n\ge8\), this bound is attained by a graph with \(\tau(G)=n-2\).

2. **Necessary growth of a general threshold.** With natural logarithms, put
   \[
   N_n=\left\lfloor n\bigl(\log n-2\log\log n-2\bigr)\right\rfloor.
   \]
   For every sufficiently large \(n\), there is an \(n\)-connected, \(K_n\)-minor-free graph on \(N_n\) vertices satisfying
   \[
   \tau(G)\ge N_n-6\left\lceil4(\log n)^2\right\rceil>n-5.
   \]
   Consequently, any valid general threshold must satisfy
   \[
   \boxed{M(n)>N_n}
   \]
   for all sufficiently large \(n. \)

These finite-order obstructions do **not** disprove the sufficiently-large formulation.

## 2. A sharp bounded-order theorem for cographs

Here a **cograph** means a graph obtainable from single vertices by disjoint unions and complete joins. The complete join of graphs adds every edge between different factors.

### Lemma 1: complete multipartite minors

Let
\[
H=K_{p_1,\ldots,p_k},\qquad
N=\sum_i p_i,\qquad P=\max_i p_i,
\]
where every \(p_i\ge1\). Then
\[
\boxed{
h(H)=
\min\left\{
\left\lfloor\frac{N+k}{2}\right\rfloor,\,
N-P+1
\right\}.
}
\tag{1}
\]

**Proof.** Consider a complete-minor model with \(t\) branch sets.

At most \(k\) branch sets can be singletons: two singleton branch sets in the same part would not be adjacent. Consequently,
\[
N\ge 2t-k,
\]
giving the first upper bound.

A connected branch set contained entirely in a largest part must be a singleton, and at most one branch set can have this property. All other branch sets use distinct vertices outside that part. Thus
\[
t\le N-P+1.
\]

For the lower bound, select one singleton branch set from each part. In the remaining complete multipartite graph, take a maximum matching and use its edges as two-vertex branch sets. Every such branch set is connected and adjacent to every other branch set.

A complete multipartite graph with \(R\) vertices and largest part of size \(Q\) has a matching of size
\[
\min\{\lfloor R/2\rfloor,R-Q\}.
\]
Indeed, if \(Q\ge R/2\), match every vertex outside a largest part into it. Otherwise, repeatedly match vertices from two largest parts; the largest part remains at most half the remaining order, rounded up, so at most one vertex is left unmatched.

Here \(R=N-k\) and \(Q=P-1\). Adding the \(k\) singleton branch sets gives exactly the right-hand side of (1). ∎

### Proposition 2: the cograph order bound

If \(n\ge5\), \(G\) is an \(n\)-connected cograph, and \(G\) has no \(K_n\) minor, then
\[
|V(G)|\le2n-4.
\tag{2}
\]

In fact, such a graph can exist only when \(n\ge8\).

**Proof.** Flattening the top join in a construction of the connected cograph \(G\), write
\[
G=G_1\vee\cdots\vee G_k,\qquad k\ge2,
\]
where each factor is either a singleton or disconnected. Set
\[
p_i=|V(G_i)|,\qquad N=|V(G)|,\qquad P=\max_i p_i.
\]

Then
\[
\kappa(G)=N-P.
\tag{3}
\]
To see the lower bound, deleting fewer than \(N-P\) vertices leaves vertices in at least two factors, and the complete join edges connect everything remaining. For the upper bound, delete all vertices outside a largest factor. If \(P\ge2\), that factor is disconnected. If \(P=1\), the graph is complete and the formula is again correct.

The graph \(G\) contains the spanning complete multipartite graph
\[
H=K_{p_1,\ldots,p_k}.
\]
Moreover,
\[
\kappa(H)=N-P=\kappa(G)\ge n.
\]
Since \(H\) also has no \(K_n\) minor, Lemma 1 implies
\[
\min\left\{
\left\lfloor\frac{N+k}{2}\right\rfloor,\,
N-P+1
\right\}\le n-1.
\]
The second entry is at least \(n+1\), so
\[
N+k\le2n-1.
\tag{4}
\]

We cannot have \(k=2\): then both parts of \(H\) have size at least \(n\), and \(H\) has a \(K_{n+1}\) minor. Hence \(k\ge3\), and (4) gives (2).

For the final assertion, \(P\le N-n\) and \(N\le kP\) yield
\[
kn\le(k-1)N\le(k-1)(2n-1-k).
\]
Thus
\[
n\ge\frac{k^2-1}{k-2}
=k+2+\frac3{k-2}.
\]
For every integer \(k\ge3\), the right-hand side is greater than \(7\). Therefore \(n\ge8\). ∎

### Sharpness, including the planar-deletion obstruction

For every \(n\ge8\), consider
\[
T_n=K_{n-4,n-4,4}.
\]
It has \(2n-4\) vertices, and
\[
\kappa(T_n)=(2n-4)-(n-4)=n.
\]
Lemma 1 gives
\[
h(T_n)=
\min\left\{
\left\lfloor\frac{2n-1}{2}\right\rfloor,n+1
\right\}
=n-1.
\]

Furthermore,
\[
\boxed{\tau(T_n)=n-2.}
\tag{5}
\]

To prove (5), consider a planar induced subgraph. If it contains at least three vertices from one part and at least three vertices altogether from the other two parts, it contains a \(K_{3,3}\) subgraph. Therefore, if one retained part has size at least three, the other retained parts have total size at most two. Its order is then at most
\[
(n-4)+2=n-2.
\]
If all three retained parts have size at most two, its order is at most \(6\le n-2\).

Conversely, retaining all vertices of a largest part and two vertices from another gives the planar graph \(K_{n-4,2}\), of order \(n-2\). Hence the largest planar induced subgraph has order \(n-2\), proving (5).

Thus, within cographs, the threshold \(2n-3\) is sufficient and is best possible for every \(n\ge8\). Sufficiency here is vacuous: above that order, no graph satisfies the connectivity and excluded-minor hypotheses.

## 3. A general lower bound of order \(n\log n\)

The following argument is self-contained and uses the binomial random graph \(G(N,p)\).

### Lemma 3: a first-moment bound for complete minors

Let \(0<p<1\), \(q=1-p\), and \(t\ge2\). Then
\[
\Pr\bigl(K_t\text{ is a minor of }G(N,p)\bigr)
\le
(t+1)^N
\exp\left(
-\binom t2 q^{(N/t)^2}
\right).
\tag{6}
\]

**Proof.** There are at most \((t+1)^N\) ordered collections of \(t\) pairwise disjoint nonempty vertex sets: label each vertex by a branch-set index or by “unused.”

Fix such a collection, with sizes \(b_1,\ldots,b_t\). Ignoring the requirement that branch sets be connected, the probability that every pair of branch sets has an edge between them is
\[
\prod_{i<j}(1-q^{b_i b_j})
\le
\exp\left(-\sum_{i<j}q^{b_i b_j}\right).
\tag{7}
\]
The events for different pairs use disjoint sets of random edges.

Writing \(B=\sum_i b_i\le N\), we have
\[
\frac1{\binom t2}\sum_{i<j}b_i b_j
=
\frac{B^2-\sum_i b_i^2}{t(t-1)}
\le\frac{B^2}{t^2}
\le\left(\frac Nt\right)^2.
\]
The function \(x\mapsto q^x\) is convex and decreasing. Jensen’s inequality therefore gives
\[
\sum_{i<j}q^{b_i b_j}
\ge
\binom t2 q^{(N/t)^2}.
\]
Substitute this into (7) and apply the union bound. ∎

### Proposition 4: large finite obstructions

For every sufficiently large integer \(n\), there is an \(n\)-connected, \(K_n\)-minor-free graph on
\[
N=\left\lfloor n\bigl(\log n-2\log\log n-2\bigr)\right\rfloor
\]
vertices with
\[
\tau(G)\ge N-6\left\lceil4(\log n)^2\right\rceil.
\tag{8}
\]

**Proof.** Put
\[
L=\log n,\qquad r=\frac Nn,\qquad
\lambda=1+\frac1{L^2},\qquad
p=\frac{\lambda}{r},
\]
and sample \(G\sim G(N,p)\). For sufficiently large \(n\), these parameters satisfy \(0<p<1\) and \(p\ge1/L\).

We show that all required properties hold with probability tending to one.

#### 3.1. Absence of a \(K_n\) minor

We have
\[
r=L-2\log L-2+O(1/n).
\]
Writing \(q=1-p\), Taylor expansion gives
\[
\begin{aligned}
r^2\log q
&=r^2\log(1-\lambda/r)\\
&=-\lambda r-\frac{\lambda^2}{2}+O(1/r)\\
&=-L+2\log L+\frac32+o(1).
\end{aligned}
\]
Consequently,
\[
q^{r^2}
=(e^{3/2}+o(1))\frac{L^2}{n}.
\]
Also,
\[
N\log(n+1)=(1+o(1))nL^2.
\]
Applying Lemma 3 with \(t=n\),
\[
\Pr(K_n\text{ minor})
\le
\exp\left(
\left(1-\frac{e^{3/2}}2+o(1)\right)nL^2
\right)
=o(1),
\tag{9}
\]
because \(e^{3/2}/2>1\).

#### 3.2. \(n\)-connectivity

Set
\[
a=\frac{n}{2L^2}.
\]
The expected degree of a vertex is
\[
\mu=(N-1)p
=n+\frac n{L^2}-p.
\]
For large \(n\),
\[
\mu-(n+a)\ge\frac n{3L^2},
\qquad \mu\le2n.
\]
The elementary binomial lower-tail bound
\[
\Pr(X\le\mu-u)\le \exp(-u^2/(2\mu))
\]
and a union bound imply
\[
\Pr\bigl(\delta(G)<n+a\bigr)
\le
N\exp\left(-\frac{n}{36L^4}\right)
=o(1).
\tag{10}
\]

There are at most \(3^N\) ordered pairs of disjoint vertex sets \(A,B\). Therefore
\[
\begin{aligned}
&\Pr\bigl(\exists A,B:\ |A|,|B|\ge a,\ E(A,B)=\varnothing\bigr)\\
&\qquad\le 3^N e^{-pa^2}\\
&\qquad\le
\exp\left(N\log3-\frac{n^2}{4L^5}\right)
=o(1).
\end{aligned}
\tag{11}
\]

Suppose neither exceptional event occurs. If deleting a set \(S\), with \(|S|\le n-1\), disconnects \(G\), then every component \(C\) of \(G-S\) satisfies
\[
|C|\ge\delta(G)-|S|+1\ge a+2.
\]
One component and the union of the others would therefore be disjoint anticomplete sets, each of size at least \(a\), contradicting (11). Thus \(\kappa(G)\ge n\).

#### 3.3. Almost every vertex must be deleted to obtain planarity

Let
\[
u=\lceil4L^2\rceil.
\]
A union bound over independent sets gives
\[
\Pr(\alpha(G)\ge u)
\le
\binom Nu q^{\binom u2}
\le
\exp\left(u\log N-\frac{pu(u-1)}2\right).
\]
Using \(N\le nL\) and \(p\ge1/L\), the exponent is at most
\[
u(L+\log L)-\frac{u(u-1)}{2L}
=-(4+o(1))L^3.
\]
Hence
\[
\Pr(\alpha(G)\ge u)=o(1).
\tag{12}
\]

Every planar graph is \(6\)-colorable: Euler’s inequality gives a vertex of degree at most five in every nonempty subgraph, and greedy coloring applies. Thus every planar induced subgraph \(H\) of \(G\) satisfies
\[
|V(H)|\le6\alpha(H)\le6\alpha(G)<6u.
\]
It follows that
\[
\tau(G)\ge N-6u.
\]

By (9)–(12), the desired properties hold simultaneously with probability \(1-o(1)\), and in particular with positive probability for every sufficiently large \(n\). This proves (8). ∎

### Consequence for Thomas’s threshold

Since \(N\sim n\log n\),
\[
N-6\lceil4(\log n)^2\rceil>n-5
\]
for all sufficiently large \(n\). The graph in Proposition 4 therefore violates the desired conclusion at order \(N\).

Accordingly, any threshold having the required property must satisfy
\[
\boxed{
M(n)>
\left\lfloor n\bigl(\log n-2\log\log n-2\bigr)\right\rfloor.
}
\]
In particular, no threshold \(M(n)=o(n\log n)\) can work.

## 4. Gap to the original problem

The partial results have two different limitations:

- The cograph argument exploits a spanning complete multipartite graph with the same connectivity. Arbitrary graphs need not admit such a structure.
- The probabilistic construction gives one large finite obstruction for each growing \(n\). It gives no unbounded family for any **fixed** \(n\), which would be needed to disprove Thomas’s statement.

Thus I have neither proved a general upper bound on the order of non-\((n-5)\)-apex obstructions nor produced a counterexample to the sufficiently-large conjecture. In particular, the unrestricted fixed case \(n=7\) is not settled by these arguments.