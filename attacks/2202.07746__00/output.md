```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved here for all connected simple cactus graphs, for generalized theta graphs, and deterministically whenever the cycle rank is at most n/3.",
  "would_publish": false,
  "caveats": "This assumes the intended connected-graph convention; literally allowing disconnected rotation systems gives the counterexample 2K_3, and the general non-cactus case remains open."
}
```

# 1. Statement and connectivity convention

A random orientable embedding of a graph is obtained by independently choosing a uniformly random cyclic order of the darts incident with each vertex. The faces are the cycles of the resulting face permutation.

The conjecture must be read for **connected** graphs. Indeed, if disconnected rotation systems are allowed and face counts are added over components, then \(2K_3\) has \(n=6\) and \(F=4>6/3+1=3\). Moreover, a cellular embedding in a connected surface necessarily has connected \(1\)-skeleton. I therefore use the intended formulation:

> **Conjecture.** Every connected simple graph \(G\) of order \(n\) satisfies
> \[
> \mathbb E F(G)\le \frac n3+1.
> \]

I prove this for two substantial classes, including all cactus graphs.

# 2. Preliminary reductions

Let
\[
\beta(G)=|E(G)|-|V(G)|+1
\]
be the cycle rank of a connected graph. For every orientable rotation system,
\[
|V|-|E|+F=2-2g,
\]
and hence
\[
F=\beta(G)+1-2g. \tag{2.1}
\]

## Proposition 2.1: the sparse range

If \(\beta(G)\le n/3\), then the conjecture holds deterministically.

Indeed, (2.1) gives
\[
F\le \beta(G)+1\le \frac n3+1.
\]

Thus only graphs satisfying
\[
|E(G)|>\frac{4n}{3}-1 \tag{2.2}
\]
can be counterexamples.

## Lemma 2.2: bridges

Suppose \(e\) is a bridge of \(G\), and \(G-e\) has components \(G_1,G_2\). Then
\[
\mathbb E F(G)=\mathbb E F(G_1)+\mathbb E F(G_2)-1. \tag{2.3}
\]

For a fixed rotation system, the ribbon corresponding to \(e\) joins one boundary component of the ribbon surface of \(G_1\) to one boundary component of that of \(G_2\), reducing the total number of boundary components by one. Deleting a specified dart from a uniformly random cyclic order leaves a uniformly random cyclic order on the remaining darts, so the induced rotations on \(G_1,G_2\) have the correct distributions.

Consequently, a vertex-minimal counterexample would be bridgeless.

# 3. An intersection-matrix formulation

Let a connected graph with a specified rotation system be cellularly embedded in an orientable surface \(S\). The embedding induces an alternating bilinear intersection form over \(\mathbb F_2\) on the cycle space of \(G\). If \(A\) is its matrix in any cycle-space basis, then
\[
\operatorname{rank}_{\mathbb F_2} A=2g. \tag{3.1}
\]

Indeed, \(H_1(G;\mathbb F_2)\to H_1(S;\mathbb F_2)\) is surjective, and the intersection form on \(H_1(S;\mathbb F_2)\) is nondegenerate of rank \(2g\).

Combining (2.1) and (3.1),
\[
F=\beta(G)+1-\operatorname{rank}_{\mathbb F_2} A. \tag{3.2}
\]

Thus the full conjecture is equivalent to
\[
\mathbb E\operatorname{rank}_{\mathbb F_2}A
   \ge \beta(G)-\frac n3. \tag{3.3}
\]

For cactus graphs the matrix \(A\) has enough tree structure to prove the required rank bound.

# 4. A local random-chord estimate

We first need an auxiliary lemma.

## Lemma 4.1

Place \(k\) fixed pairs of points in a uniformly random cyclic order, and let \(B_k\) be the \(k\times k\) matrix over \(\mathbb F_2\) whose \(ij\)-entry is \(1\) exactly when the endpoints of pairs \(i,j\) alternate around the circle. If \(k\ge2\), then
\[
\mathbb E\operatorname{rank} B_k\ge \frac k3. \tag{4.1}
\]

### Proof

This is the intersection matrix of a one-vertex orientable ribbon graph with \(k\) loops. Let \(f\) be its number of boundary components. Euler's formula and (3.1) give
\[
\operatorname{rank} B_k=k+1-f. \tag{4.2}
\]

Fixing the cyclic order and randomizing the pairing gives the same distribution. Let \(N=2k\), let
\[
\gamma=(1\,2\,\dots\,N),
\]
and let \(\alpha\) be a uniformly random perfect matching, viewed as a fixed-point-free involution. Then
\[
f=c(\gamma\alpha),
\]
the number of cycles of \(\gamma\alpha\).

Let \(Z_1,Z_2\) denote the numbers of \(1\)- and \(2\)-cycles of \(\gamma\alpha\). For every permutation of \(N\) points,
\[
c(\gamma\alpha)
 \le \frac N3+\frac23Z_1+\frac13Z_2. \tag{4.3}
\]

For \(N\ge6\),
\[
\mathbb EZ_1=\frac{N}{N-1}.
\]
Also, an unordered pair \(\{i,j\}\) forms a \(2\)-cycle precisely when
\[
\alpha(i)=\gamma^{-1}(j),\qquad
\alpha(j)=\gamma^{-1}(i).
\]
This is impossible when \(i,j\) are cyclically adjacent. For each of the \(N(N-3)/2\) nonadjacent pairs, it prescribes two disjoint matching edges and therefore has probability
\[
\frac1{(N-1)(N-3)}.
\]
Hence
\[
\mathbb EZ_2=\frac{N}{2(N-1)}.
\]
It follows that
\[
2\mathbb EZ_1+\mathbb EZ_2
 =\frac{5N}{2(N-1)}
 \le3
\]
for \(N\ge6\). By (4.3),
\[
\mathbb Ef\le \frac N3+1=\frac{2k}{3}+1.
\]
Equation (4.2) now gives
\[
\mathbb E\operatorname{rank}B_k
 \ge k+1-\left(\frac{2k}{3}+1\right)
 =\frac k3.
\]

For \(k=2\), among the three matchings of four cyclically ordered points, exactly one is crossing. Thus the rank is \(2\) with probability \(1/3\) and \(0\) otherwise, giving expected rank \(2/3=k/3\). ∎

# 5. The conjecture for cactus graphs

Recall that a cactus is a graph in which every edge lies in at most one cycle.

## Theorem 5.1

Every connected simple cactus graph \(G\) of order \(n\) satisfies
\[
\mathbb EF(G)\le \frac n3+1.
\]

### 5.1. Reduction to a bridgeless cactus

By Lemma 2.2, it suffices to prove the result for each component left after deleting all bridges. Components consisting of a single vertex contribute nothing to \(F-1\). Thus assume that \(G\) is connected, bridgeless, and has \(t\ge1\) cycle blocks
\[
C_1,\dots,C_t.
\]

Let \(\ell_i=|C_i|\). Form the bipartite incidence graph \(\mathcal T\) whose two classes are:

- the cycles \(C_i\);
- vertices of \(G\) lying on at least two cycles,

with incidence given by containment. Since \(G\) is a cactus, \(\mathcal T\) is a tree.

Let \(q_i\) be the degree of the cycle node \(C_i\) in \(\mathcal T\), and put
\[
Q=\sum_{i=1}^t (q_i-3)_+.
\]

Because \(\mathcal T\) is a tree,
\[
\sum_x (r_x-1)=t-1, \tag{5.1}
\]
where \(r_x\) is the number of cycles through a shared vertex \(x\). Hence
\[
n=\sum_{i=1}^t\ell_i-(t-1). \tag{5.2}
\]
Moreover,
\[
\ell_i\ge \max\{3,q_i\}=3+(q_i-3)_+,
\]
so
\[
n\ge 3t+Q-(t-1)=2t+1+Q. \tag{5.3}
\]

### 5.2. The cactus intersection matrix

The cycles \(C_1,\dots,C_t\) form a basis of the cycle space. Two such cycles intersect mod \(2\) precisely when, at their common vertex, their four incident darts alternate in the local cyclic order. Let \(A\) be this \(t\times t\) intersection matrix.

By (3.2),
\[
F=t+1-\operatorname{rank}A. \tag{5.4}
\]

It remains to prove the following rank estimate.

## Lemma 5.2

For the random rotations of a bridgeless cactus,
\[
\mathbb E\operatorname{rank} A\ge \frac{t-1-Q}{3}. \tag{5.5}
\]

### Proof

Root the incidence tree \(\mathcal T\) at a cycle node. We induct on \(t\). The case \(t=1\) is immediate.

Choose a deepest cycle node \(Y\) having at least one child shared-vertex node. Every cycle below such a child node is then a leaf of \(\mathcal T\).

There are two cases.

#### Case 1: a child shared vertex contains at least two child cycles

Let \(x\) be such a shared vertex. Besides \(Y\), suppose \(x\) lies on \(k\ge2\) leaf cycles. Delete \(x\) and those \(k\) leaf cycles, obtaining a smaller incidence tree and matrix \(A'\).

Let \(B\) be the intersection matrix restricted to those \(k\) leaf cycles. Omitting the two darts belonging to \(Y\) from the uniformly random cyclic order at \(x\) leaves a uniformly random cyclic order of the \(2k\) remaining darts. Thus Lemma 4.1 gives
\[
\mathbb E\operatorname{rank}B\ge \frac k3. \tag{5.6}
\]

In suitable order the full matrix has the form
\[
A=
\begin{pmatrix}
 B&b&0\\
 b^{T}&0&c^{T}\\
 0&c&C
\end{pmatrix},
\qquad
A'=
\begin{pmatrix}
0&c^{T}\\
c&C
\end{pmatrix}. \tag{5.7}
\]

An alternating matrix is congruent to a direct sum of hyperbolic \(2\times2\) blocks and a zero matrix. Applying such a congruence to \(B\), eliminating the coupling of its nonsingular part with the \(Y\)-coordinate, and then deleting its null coordinates gives
\[
\operatorname{rank}A\ge \operatorname{rank}A'
                            +\operatorname{rank}B. \tag{5.8}
\]
No nonzero diagonal term is created because the inverse of a nonsingular alternating matrix is alternating.

When \(x\) is deleted, \(q_Y\) decreases by one. Therefore
\[
Q-Q'=\varepsilon,
\qquad \varepsilon\in\{0,1\},
\]
and
\[
(t-1-Q)-(t'-1-Q')=k-\varepsilon\le k.
\]
The induction hypothesis, (5.6), and (5.8) yield (5.5).

#### Case 2: every child shared vertex of \(Y\) contains exactly one child cycle

Suppose there are \(s\ge1\) such child cycles. The corresponding \(s\) shared vertices each lie on exactly two cycles. At each such vertex, the two cycles alternate with probability \(1/3\): among the six cyclic orders of four labeled darts, exactly two are alternating. These \(s\) events are independent.

Let \(X_j\in\{0,1\}\) be the intersection entry between \(Y\) and the \(j\)-th child cycle. Thus
\[
\Pr(X_1=\cdots=X_s=0)=\left(\frac23\right)^s. \tag{5.9}
\]

Delete \(Y\), these \(s\) leaf cycles, and their shared vertices; also delete \(Y\) from its parent shared vertex if \(Y\) is not the root. Let \(A'\) be the matrix on the remaining cycle nodes. The full matrix has the block form
\[
A=
\begin{pmatrix}
0_{s\times s}&X&0\\
X^{T}&0&c^{T}\\
0&c&C
\end{pmatrix},
\qquad A'=C. \tag{5.10}
\]

If \(X\ne0\), choose a coordinate with \(X_j=1\). The principal submatrix on that child cycle, \(Y\), and the remaining coordinates is congruent to
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}\oplus C.
\]
Therefore
\[
\operatorname{rank}A
 \ge \operatorname{rank}A'
      +2\mathbf 1_{\{X\ne0\}}.
\]
Taking expectations,
\[
\mathbb E\operatorname{rank}A
 \ge \mathbb E\operatorname{rank}A'
      +2\left(1-\left(\frac23\right)^s\right). \tag{5.11}
\]

If \(Y\) is not the root, then \(q_Y=s+1\), and deleting \(Y\) changes \(Q\) by
\[
(s-2)_++\delta,
\qquad \delta\in\{0,1\};
\]
the possible \(\delta\) accounts for the parent shared vertex disappearing and lowering the incidence degree of the remaining parent cycle. Hence the change in \(t-1-Q\) is at most
\[
s+1-(s-2)_+
 =
 \begin{cases}
 2,&s=1,\\
 3,&s\ge2.
 \end{cases}
\]
On the other hand,
\[
2\left(1-\left(\frac23\right)^s\right)
 \ge
 \begin{cases}
 2/3,&s=1,\\
 10/9,&s\ge2,
 \end{cases}
\]
which is at least one third of the preceding change.

If \(Y\) is the root, the whole remaining tree consists of \(Y\) and these \(s\) leaf cycles. Then
\[
t-1-Q=s-(s-3)_+\le3,
\]
while the right side of (5.11) is at least \(2/3,10/9,\) or \(38/27\) according as \(s=1,2,\) or \(s\ge3\). This again proves (5.5).

The induction is complete. ∎

### 5.3. Completion of the cactus proof

Using (5.4), Lemma 5.2, and (5.3),
\[
\begin{aligned}
\mathbb EF
&\le t+1-\frac{t-1-Q}{3}\\
&=\frac{2t+4+Q}{3}\\
&\le \frac n3+1.
\end{aligned}
\]

Finally, restore the bridges. If the cyclic components after deleting all bridges are \(B_1,\dots,B_r\), then repeated use of (2.3) gives
\[
\mathbb EF(G)
 =1+\sum_{i=1}^r\bigl(\mathbb EF(B_i)-1\bigr)
 \le1+\frac13\sum_{i=1}^r|V(B_i)|
 \le1+\frac n3.
\]
This proves Theorem 5.1. ∎

In particular, the conjectured extremal construction is recovered: \(t\) vertex-disjoint triangles connected by bridges has
\[
F=1+t=\frac n3+1.
\]

# 6. Generalized theta graphs

A generalized theta graph consists of two branch vertices joined by \(k\) internally vertex-disjoint paths.

## Proposition 6.1

Every simple generalized theta graph satisfies the conjecture.

### Proof

All internal vertices have degree two. Label the \(k\) paths. Traversing a face from one branch vertex to the other and back shows that the faces are the cycles of the product of the two local \(k\)-cycles. Thus it suffices to bound the number of cycles of
\[
\pi=\gamma\sigma,
\]
where \(\gamma\) is a fixed \(k\)-cycle and \(\sigma\) is a uniformly random \(k\)-cycle.

For \(k\ge3\), let \(Z_1,Z_2\) denote the numbers of \(1\)- and \(2\)-cycles of \(\pi\). Again,
\[
c(\pi)\le \frac k3+\frac23Z_1+\frac13Z_2. \tag{6.1}
\]

A prescribed point is fixed with probability \(1/(k-1)\), so
\[
\mathbb EZ_1=\frac{k}{k-1}. \tag{6.2}
\]

For a nonadjacent unordered pair \(\{i,j\}\), being a \(2\)-cycle prescribes two disjoint directed arcs of \(\sigma\). The probability that a uniformly random \(k\)-cycle contains them is
\[
\frac{(k-3)!}{(k-1)!}
 =\frac1{(k-1)(k-2)}.
\]
Adjacent pairs are impossible. Hence
\[
\mathbb EZ_2
 =\frac{k(k-3)}{2(k-1)(k-2)}. \tag{6.3}
\]

A calculation gives
\[
3-\left(2\mathbb EZ_1+\mathbb EZ_2\right)
 =\frac{(k-3)(k-4)}{2(k-1)(k-2)}
 \ge0.
\]
Therefore (6.1) yields
\[
\mathbb EF\le \frac k3+1. \tag{6.4}
\]

In a simple generalized theta graph at most one of the \(k\) paths has length one, so \(n\ge k+1\). Thus (6.4) is stronger than
\[
\mathbb EF\le \frac n3+1.
\]

For \(k=2\), the graph is a cycle, has \(F=2\), and \(n\ge3\). ∎

The bridge lemma consequently also handles graphs whose components after deleting all bridges are cacti or generalized theta graphs.

# 7. Restrictions on a minimal counterexample

The preceding arguments imply that a vertex-minimal counterexample, if one exists, must satisfy all of the following:

1. It is connected and bridgeless.
2. Its cycle rank satisfies
   \[
   \beta(G)>\frac n3.
   \]
3. It is not a cactus, so some edge lies in at least two cycles.
4. It is not a generalized theta graph.
5. Every degree-two vertex lies in a triangle.

For the last assertion, if a degree-two vertex \(v\) has nonadjacent neighbors \(u,w\), suppressing \(v\) and replacing \(uv,vw\) by \(uw\) produces a smaller simple graph. Subdivision does not alter any face count, and the random rotations correspond bijectively. This would contradict vertex-minimality.

# 8. Remaining gap

For an arbitrary graph, equation (3.3) is the central unresolved inequality:
\[
\mathbb E\operatorname{rank}_{\mathbb F_2}A
 \ge \beta(G)-\frac n3.
\]

In a cactus, the natural cycle basis is edge-disjoint, and its incidence structure is a tree. This gives leaf rows and local random chord matrices that can be eliminated without rank cancellation. In a general bridgeless graph, basis cycles may share paths and multiple vertices, and the support structure of the intersection matrix need not be tree-like. The rank induction above does not survive those overlaps. Thus the full conjecture is not proved here.