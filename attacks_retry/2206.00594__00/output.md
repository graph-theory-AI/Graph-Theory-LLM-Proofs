```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain polynomial weighted MIS when Δ log(Δ+1)=O(log n), and separately on O_k-free graphs with bounded neighborhood independence.",
  "would_publish": false,
  "caveats": "The unrestricted dense case remains untreated; novelty of these special cases has not been checked."
}
```

# 1. Scope of the partial results

Throughout, graphs are finite and simple. Write
\[
p(G)=\max\{r:\text{\(G\) contains \(r\) pairwise vertex-disjoint, pairwise anticomplete cycles}\}.
\]
Thus \(G\) is \(\mathcal O_k\)-free exactly when \(p(G)<k\).

Let \(\tau(G)\) denote the minimum size of a feedback vertex set, and let \(\Delta(G)\) be the maximum degree.

I do **not** resolve the conjecture. Instead, I prove the following constructive bound:
\[
\boxed{\tau(G)=O\!\left(k\Delta\log(k\Delta+2)\right)
\quad\text{for every \(\mathcal O_k\)-free graph of maximum degree at most \(\Delta\).}}
\tag{1}
\]
Importantly, this bound has no dependence on \(n=|V(G)|\).

It yields:

1. an exact weighted MIS algorithm with running time
   \[
   2^{O(k\Delta\log(k\Delta+2))}\operatorname{poly}(n,L),
   \]
   where \(L\) is the bit length of the weights;
2. polynomial-time weighted MIS, for fixed \(k\), whenever
   \[
   \Delta\log(\Delta+1)=O(\log n);
   \]
3. polynomial-time weighted MIS for every fixed \(k,d\) on graphs that are both \(\mathcal O_k\)-free and \(K_{1,d+1}\)-free.

The third result allows arbitrarily large degrees and densities.

The argument is self-contained and does not use the previous attempt’s decomposition claims or its proposed dense family. I make no claim that these special cases are new in the literature.

# 2. A bounded-degree packing–transversal theorem

## Theorem 2.1

Let \(k\ge 2\) and \(\Delta\ge 3\). There is a polynomial-time algorithm which, given a graph \(G\) of maximum degree at most \(\Delta\), returns either:

- \(k\) pairwise vertex-disjoint and pairwise anticomplete cycles; or
- a feedback vertex set \(X\) satisfying
  \[
  |X|\le F(k,\Delta),
  \]
  where
  \[
  F(k,\Delta)=
  \left\lceil
  4(k-1)(\Delta-1)
  \log_2\!\left(16(k-1)(\Delta-1)^2\right)
  \right\rceil .
  \tag{2}
  \]

In particular, the second outcome is guaranteed on \(\mathcal O_k\)-free graphs.

For \(\Delta\le2\), a simpler algorithm returns either the requested packing or a feedback vertex set of size at most \(k-1\).

## 2.1. Safe reductions

We use two operations:

1. delete a vertex of degree at most one;
2. if \(x\) has degree two, with distinct nonadjacent neighbors \(a,b\), delete \(x\) and add \(ab\).

Call the second operation **suppression**. Vertex labels of \(a,b\) are retained, so every surviving vertex remains an original vertex.

Both operations preserve the following properties.

### Feedback vertex sets lift without increasing their size

For deletion of a degree-at-most-one vertex this is immediate.

For suppression, let
\[
H=G-x+ab.
\]
Every feedback vertex set \(Y\subseteq V(H)\) is also a feedback vertex set of \(G\). Indeed, a cycle of \(G-Y\) avoiding \(x\) remains a cycle in \(H-Y\). A cycle using \(x\) uses the path \(a x b\), which can be replaced by \(ab\). Since \(a,b\) were nonadjacent in \(G\), this replacement still produces a cycle of length at least three.

Moreover,
\[
\tau(H)=\tau(G).
\tag{3}
\]
For the other inequality, take a minimum feedback vertex set \(Y\) of \(G\). If \(x\notin Y\), then \(Y\) is also a feedback vertex set of \(H\). If \(x\in Y\), replace \(x\) by \(a\); the resulting set has size at most \(|Y|\) and is a feedback vertex set of \(H\).

We deliberately do **not** suppress a degree-two vertex whose neighbors are adjacent: that operation could erase a triangle.

### Anticomplete cycle packings lift

A cycle packing in a graph obtained by deleting vertices is already a packing in the previous graph.

For suppression, take an anticomplete cycle packing in \(H=G-x+ab\). If one of its cycles uses \(ab\), replace that edge by \(a x b\). At most one cycle uses \(ab\), and the inserted vertex \(x\) has no neighbors other than \(a,b\). Thus the lifted cycles remain disjoint and anticomplete.

Consequently, neither reduction can increase \(p(G)\).

### Maximum degree does not increase

During suppression, \(a\) and \(b\) each lose neighbor \(x\) and gain each other. Their degrees are unchanged. All other surviving degrees are unchanged.

Exhaustively applying these reductions will be called **normalization**. A nonempty normalized graph has minimum degree at least two, and every degree-two vertex belongs to a triangle.

## 2.2. Finding a cycle short in terms of the feedback number

Fix a cyclic input graph \(G\), and put
\[
f=\tau(G)\ge1,\qquad d=\Delta-1.
\]

Consider any normalized graph \(H\) obtained during a sequence of reductions and vertex deletions. We have
\[
\Delta(H)\le\Delta,\qquad \tau(H)\le f.
\tag{4}
\]

If \(H\) has a degree-two vertex, it contains a triangle.

Otherwise \(\delta(H)\ge3\). Write \(h=|V(H)|\), and let \(Y\) be a minimum feedback vertex set of \(H\). Since \(H-Y\) is a forest,
\[
\frac32h
\le |E(H)|
\le |E(H-Y)|+\Delta|Y|
\le h-|Y|+\Delta|Y|.
\]
Therefore
\[
h\le2(\Delta-1)|Y|
\le2df.
\tag{5}
\]

A graph of minimum degree at least three on \(h\) vertices has a cycle of length at most
\[
2\log_2 h+2.
\tag{6}
\]
For completeness, if its girth is \(g\), breadth-first expansion to radius
\[
r=\left\lfloor\frac{g-1}{2}\right\rfloor
\]
gives at least \(1+3(2^r-1)>2^r\) vertices. Since \(g\le2r+2\), (6) follows.

Combining the triangle case with (5)–(6), every nonempty normalized \(H\) contains a cycle \(C\) of length at most
\[
\ell(C)\le 2\log_2(2df)+2.
\tag{7}
\]

Each vertex of \(C\) has at least two neighbors on \(C\). Hence
\[
|N_H[V(C)]|
\le (\Delta-1)\ell(C)
=d\ell(C).
\tag{8}
\]

The algorithm does not need to know \(f\). It simply uses a triangle through a degree-two vertex when one exists, and otherwise a shortest cycle.

## 2.3. The algorithm

Starting with \(G\), repeatedly:

1. normalize the current graph;
2. if it is empty, stop;
3. choose a cycle \(C\) as above;
4. record
   \[
   S=N_H[V(C)],
   \]
   and replace \(H\) by \(H-S\).

If \(k\) cycles have been chosen, stop and return an anticomplete packing of \(k\) cycles, obtained by reversing the reductions.

Why does this packing exist? At each step, all subsequent cycles are found in the antineighborhood of the cycle just chosen. In reverse order, lift the subsequent packing through the reductions, add the earlier cycle, and continue lifting. The preservation property proved above justifies every step.

Suppose instead that the process empties the graph after \(r<k\) cycle choices. Let \(X\) be the union of the recorded sets \(S\), using their original vertex labels. Reversing the reductions shows that
\[
G-X\text{ is a forest}.
\tag{9}
\]
Thus \(X\) is a feedback vertex set of the original graph.

It remains to bound its size.

## 2.4. Removing the dependence on \(n\)

Let \(x=|X|\), and assume \(G\) is cyclic. Since \(X\) is a feedback vertex set,
\[
f\le x.
\tag{10}
\]
By (7)–(8), and because \(r\le k-1\),
\[
\begin{aligned}
x
&\le (k-1)d\bigl(2\log_2(2df)+2\bigr)\\
&=2(k-1)d\log_2(4df)\\
&\le2(k-1)d\log_2(4dx).
\end{aligned}
\tag{11}
\]

Set
\[
A=2(k-1)d,\qquad B=4d.
\]
Then
\[
x\le A\log_2(Bx).
\tag{12}
\]

Here \(AB\ge32\). Writing \(y=x/A\), we obtain
\[
y\le\log_2(AB)+\log_2 y.
\]
If \(y<4\), certainly \(y\le2\log_2(2AB)\). If \(y\ge4\), use
\[
\log_2 y\le y/2
\]
to get
\[
y\le2\log_2(AB)<2\log_2(2AB).
\]
Consequently,
\[
x\le2A\log_2(2AB)
=
4(k-1)d\log_2\!\left(16(k-1)d^2\right),
\]
which proves (2).

All operations are polynomial-time. For a fully specified shortest-cycle subroutine, for every edge \(uv\), find a shortest \(u\)-\(v\) path after deleting \(uv\), and take the shortest resulting cycle. There are at most \(n\) cycle-selection rounds and at most \(n\) normalization deletions or suppressions.

Finally, if \(\Delta\le2\), every component is a path, an isolated vertex, or a cycle. Either there are at least \(k\) cycle components, or deleting one vertex from each cycle component gives a feedback vertex set of size at most \(k-1\). This completes the proof. \(\square\)

# 3. Consequences for Maximum Weight Independent Set

Weights may be rational, and the empty independent set is allowed.

## Corollary 3.1

On \(\mathcal O_k\)-free graphs of maximum degree at most \(\Delta\), Maximum Weight Independent Set is solvable in
\[
2^{O(k\Delta\log(k\Delta+2))}\operatorname{poly}(n,L)
\tag{13}
\]
time.

### Proof

Use Theorem 2.1 to obtain a feedback vertex set \(X\).

Enumerate every independent subset \(I\subseteq X\). An independent set whose intersection with \(X\) is exactly \(I\) has optimum weight
\[
w(I)+
\alpha_w\!\left(G\bigl[V(G)\setminus(X\cup N_G(I))\bigr]\right).
\tag{14}
\]
The graph in the second term is a forest.

Weighted MIS on a rooted forest is solved by the standard two-state recurrence
\[
\begin{aligned}
\operatorname{in}(v)
&=w(v)+\sum_{u\text{ child of }v}\operatorname{out}(u),\\
\operatorname{out}(v)
&=\sum_{u\text{ child of }v}
\max\{\operatorname{in}(u),\operatorname{out}(u)\}.
\end{aligned}
\]
Taking the best value of (14) over all \(I\) is exact. There are at most \(2^{|X|}\) choices, giving (13). Witness independent sets can be recovered by storing the maximizing choices. \(\square\)

The case \(k=1\) is simply the forest case.

## Corollary 3.2: a growing-degree polynomial regime

For fixed \(k\), weighted MIS is polynomial-time solvable on every \(\mathcal O_k\)-free class satisfying
\[
\Delta(G)\log(\Delta(G)+1)=O(\log |V(G)|).
\tag{15}
\]

In particular, for any fixed constant \(c\), this holds under
\[
\Delta(G)\le c\,\frac{\log n}{\log\log n}
\]
for sufficiently large \(n\).

Indeed, (15) makes the exponent in (13) \(O(\log n)\). This is a uniform quantitative consequence allowing the degree bound—and the size of complete bipartite subgraphs—to grow with \(n\).

# 4. A dense subclass: bounded neighborhood independence

Define the neighborhood independence number by
\[
\iota(G)=\max_{v\in V(G)}\alpha(G[N_G(v)]).
\]
For \(d\ge1\), the condition \(\iota(G)\le d\) is equivalent to excluding an induced \(K_{1,d+1}\).

## Theorem 4.1

For every fixed \(k,d\), Maximum Weight Independent Set is polynomial-time solvable on graphs that are both \(\mathcal O_k\)-free and \(K_{1,d+1}\)-free.

More explicitly, there is an algorithm with running time
\[
n^{3d(k-1)+O(1)}
\,2^{O(kd\log(kd+2))}
\operatorname{poly}(L).
\tag{16}
\]

### Proof

Starting with \(H_0=G\), repeatedly choose a triangle \(T_i\) in the current graph and delete
\[
S_i=N_{H_{i-1}}[V(T_i)].
\]
Stop when the remaining graph \(H\) is triangle-free.

The chosen triangles are pairwise anticomplete in \(G\). Therefore their number \(r\) satisfies
\[
r\le k-1.
\tag{17}
\]
Put
\[
S=S_1\cup\cdots\cup S_r,
\qquad H=G-S.
\]

### There are only polynomially many relevant choices inside \(S\)

For every vertex \(v\),
\[
\alpha(G[N_G[v]])\le d.
\tag{18}
\]
Indeed, an independent set in \(N_G[v]\) either consists of \(v\), or lies in \(N_G(v)\).

Each \(S_i\) is covered by the closed neighborhoods of the three vertices of \(T_i\). Hence
\[
\alpha(G[S_i])\le3d.
\]
It follows that
\[
\alpha(G[S])\le3dr\le3d(k-1).
\tag{19}
\]

Thus all independent subsets of \(S\) can be enumerated by inspecting subsets of size at most \(3d(k-1)\), in \(n^{3d(k-1)+O(1)}\) time.

### The remaining graph has bounded maximum degree

Because \(H\) is triangle-free, every neighborhood in \(H\) is independent. Consequently,
\[
\deg_H(v)
=\alpha(H[N_H(v)])
\le d,
\]
so
\[
\Delta(H)\le d.
\tag{20}
\]

For every enumerated independent set \(I\subseteq S\), compute
\[
w(I)+\alpha_w(H-N_G(I)).
\tag{21}
\]
The graph \(H-N_G(I)\) remains \(\mathcal O_k\)-free and has maximum degree at most \(d\). Corollary 3.1 therefore evaluates the second term in the time required by (16).

Every independent set of \(G\) has an intersection \(I\) with \(S\) among the enumerated choices. Conversely, combining \(I\) with an independent set of \(H-N_G(I)\) is valid. Maximizing (21) is therefore exact. \(\square\)

### Structural consequence

The same proof also gives a feedback vertex set with bounded independence number.

For \(d\ge3\), apply Theorem 2.1 to \(H\), obtaining a feedback vertex set \(Y\) of size at most \(F(k,d)\). Then
\[
G-(S\cup Y)\text{ is a forest}
\]
and
\[
\alpha(G[S\cup Y])
\le3d(k-1)+F(k,d).
\tag{22}
\]

Thus, even though the feedback vertex set may have arbitrarily many vertices in this dense subclass, the number of its vertices that an independent set can select is bounded in terms of \(k,d\).

# 5. What this does—and does not—settle

The arguments above establish two routes to polynomiality:

- **degree control:** obtain a logarithmic-size feedback vertex set when \(\Delta\log(\Delta+1)=O(\log n)\);
- **bounded induced stars:** remove triangle neighborhoods in which an independent set has only boundedly many choices, leaving a bounded-degree graph.

Neither controls arbitrary dense \(\mathcal O_k\)-free graphs.

For example, \(K_{m,m}\) is \(\mathcal O_2\)-free: every cycle meets both sides, so any two disjoint cycles have edges between them. Nevertheless,
\[
\Delta(K_{m,m})=\iota(K_{m,m})=m,
\qquad
\tau(K_{m,m})=m-1.
\]
Thus neither the degree bound nor the bounded-neighborhood-independence hypothesis can be uniformly bounded using \(k\) alone. This is an obstruction to these particular methods, **not** a counterexample to the MIS conjecture—MIS on bipartite graphs is polynomial.

The remaining issue is to handle unrestricted large independent neighborhoods in dense graphs without enumerating exponentially many choices inside them. No argument here supplies that step, and the full conjecture is not resolved.