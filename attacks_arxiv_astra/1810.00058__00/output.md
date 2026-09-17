```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "The displayed linear-linear statement is false already for H = K_3, by a sparse random-graph construction followed by vertex deletion.",
  "would_publish": false,
  "caveats": "This refutes the displayed formula, not the polynomial-linear conjecture in the supplied source abstract; the catalog appears to have lost an exponent."
}
```

## 1. The displayed statement is false

I address the exact requirement that **both** anticomplete sets have size at least \(\varepsilon |G|\).

**Proposition.** For every \(\varepsilon>0\), there are arbitrarily large triangle-free graphs \(G\) such that
\[
\Delta(G)<\varepsilon |G|
\]
and every anticomplete pair \(A,B\) satisfies
\[
\min\{|A|,|B|\}<\varepsilon |G|.
\]
Moreover, these counterexamples can have maximum degree bounded by \(64\varepsilon^{-2}\), independently of their order.

Thus no choice of \(\varepsilon\) works for \(H=K_3\).

### Proof

Fix \(\varepsilon>0\), and put
\[
c=\frac{8}{\varepsilon^2}.
\]
Choose an integer
\[
N>\max\left\{4,c,\frac{4c^3}{3},\frac{16c}{\varepsilon}\right\}.
\]
Let \(R\) be the random graph on \([N]\) in which each edge is present independently with probability
\[
p=\frac cN.
\]

We establish two properties that hold simultaneously with positive probability.

#### Property 1: no moderately large anticomplete pair

Set
\[
t=\left\lceil\frac{\varepsilon N}{2}\right\rceil.
\]
There are at most \(3^N\) ordered pairs of disjoint vertex sets: each vertex belongs to the first set, the second set, or neither.

For fixed disjoint sets \(A,B\) of size \(t\), the probability that they are anticomplete is
\[
(1-p)^{t^2}\le e^{-pt^2}.
\]
Consequently, by the union bound,
\[
\begin{aligned}
\Pr\bigl(R\text{ has an anticomplete }(t,t)\text{-pair}\bigr)
&\le 3^N e^{-pt^2}\\
&\le 3^N
 \exp\left(-\frac cN\frac{\varepsilon^2N^2}{4}\right)\\
&=(3e^{-2})^N
<\frac12.
\end{aligned}
\tag{1}
\]
If \(2t>N\), there are no such pairs, and the bound remains valid.

#### Property 2: triangles and high-degree vertices can be removed cheaply

Let \(T\) be the number of triangles in \(R\), and define
\[
D=\{v\in V(R):d_R(v)\ge 8c\}.
\]
We have
\[
\mathbb E T=\binom N3p^3\le \frac{c^3}{6}<\frac N8.
\]
For each vertex \(v\), Markov's inequality gives
\[
\Pr(v\in D)
\le \frac{\mathbb E d_R(v)}{8c}
\le \frac18,
\]
so
\[
\mathbb E|D|\le \frac N8.
\]
Therefore
\[
\mathbb E(T+|D|)<\frac N4,
\]
and another application of Markov's inequality yields
\[
\Pr(T+|D|\ge N/2)<\frac12.
\tag{2}
\]

By (1) and (2), some realization \(R\) simultaneously has no anticomplete \((t,t)\)-pair and satisfies
\[
T+|D|<N/2.
\]

#### Delete vertices and check the normalization

From this realization, delete every vertex in \(D\), together with one selected vertex from each triangle. Let \(G\) be the resulting induced subgraph, and write \(n=|G|\). The total number of deleted vertices is at most \(T+|D|\), so
\[
n>N/2>1.
\]

Every original triangle was hit by a deletion, hence \(G\) is triangle-free. Every retained vertex had degree less than \(8c\) in \(R\), so
\[
\Delta(G)<8c=\frac{64}{\varepsilon^2}
<\frac{\varepsilon N}{2}
<\varepsilon n.
\]

Finally, suppose that \(G\) had disjoint anticomplete sets \(A,B\) with
\[
|A|,|B|\ge\varepsilon n.
\]
Since \(n>N/2\), each set has at least \(t\) vertices. Taking \(t\)-vertex subsets would give an anticomplete \((t,t)\)-pair in \(R\), because \(G\) is an induced subgraph of \(R\). This contradicts Property 1.

The integer \(N\) can be arbitrarily large, proving the proposition. \(\square\)

## 2. In fact, every cyclic forbidden graph is an obstruction

The same argument proves that a necessary condition for a fixed graph \(H\) to satisfy the displayed property is that \(H\) be a forest.

Indeed, suppose \(H\) contains a cycle, and put \(h=|H|\). Replace the triangle count \(T\) above by the number \(T_h\) of cycles of lengths \(3,\ldots,h\). In \(R=G(N,c/N)\),
\[
\mathbb E T_h
\le \sum_{\ell=3}^{h}\frac{c^\ell}{2\ell},
\]
which is independent of \(N\). For sufficiently large \(N\), it is less than \(N/8\), so the same deletion argument applies.

Delete one vertex from every cycle of length at most \(h\), as well as the high-degree vertices. The remaining graph has girth greater than \(h\), and therefore contains no copy of \(H\), even as a non-induced subgraph. The maximum-degree and anticomplete-pair conclusions are unchanged.

Thus the universal linear–linear assertion fails for every \(H\) containing a cycle.

## 3. The discrepancy with the supplied source

The supplied abstract asks for an anticomplete pair of sizes
\[
s n^{s}\qquad\text{and}\qquad s n,
\]
not two sets of size \(s n\). These are materially different statements.

The counterexamples above do **not** refute that polynomial–linear conclusion. For example, in a graph of fixed maximum degree \(d\), any set \(A\) of size \(o(n)\) has an anticomplete set
\[
B=V(G)\setminus\bigl(A\cup N(A)\bigr)
\]
of size at least
\[
n-(d+1)|A|=n-o(n).
\]

Accordingly, this is a complete disproof of the **displayed catalog formulation**, not a claimed resolution of the different conjecture described in the source abstract.