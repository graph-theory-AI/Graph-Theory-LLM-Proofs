```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The sharp bound holds for K_{2k+1}-F with k missing edges whenever F has at most k+1 nonisolated vertices or is a linear forest.",
  "would_publish": false,
  "caveats": "The general question is not resolved here; novelty and the latest literature status have not been independently verified."
}
```

# A sharp partial result at the counting threshold

All graphs below are finite and simple, unless explicitly described as multigraphs. Paths have no repeated vertices. Write \(p(G)\) for the minimum number of paths partitioning \(E(G)\).

I prove a prescribed-endpoint version of the desired bound for two infinite families at the maximum edge count permitted by the question. The proof is constructive and self-contained. I also give a short extension to graphs obtained by adding one vertex to an even clique.

## 1. Statement of the partial result

For a graph on \(2k+1\) vertices, every path has at most \(2k\) edges. Hence
\[
p(G)\ge \left\lceil\frac{|E(G)|}{2k}\right\rceil.
\]
In particular, deleting at most \(k-1\) edges from \(K_{2k+1}\) leaves more than \(2k^2\) edges, explaining the odd semi-clique obstruction.

The first case beyond that obstruction is
\[
G=K_{2k+1}-E(F),\qquad |E(F)|=k.
\]
Here \(|E(G)|=2k^2\), so a decomposition into \(k\) paths must consist entirely of Hamilton paths.

**Theorem 1.**  
Let \(k\ge 1\), and let \(F\) be a graph consisting of \(k\) edges on a subset of the vertices of \(K_{2k+1}\). Suppose either

1. \(F\) has at most \(k+1\) nonisolated vertices; or
2. \(F\) is a linear forest, meaning that every nontrivial component is a path.

Then \(K_{2k+1}-E(F)\) has a decomposition
\[
\{P_e:e\in E(F)\}
\]
into \(k\) Hamilton paths, where the endpoints of \(P_{uv}\) are \(u\) and \(v\). Consequently,
\[
p(K_{2k+1}-E(F))=k.
\]

Condition 1 includes **every missing-edge graph whose nonisolated part is connected**: a connected graph with \(k\) edges has at most \(k+1\) vertices. It allows arbitrary degrees and arbitrary cycles in that connected missing-edge graph.

These graphs are connected: disconnecting \(K_{2k+1}\) requires deleting at least \(2k\) edges, whereas only \(k\) are deleted.

The strategy is to construct a Hamilton-cycle decomposition of \(K_{2k+1}\) in which the edges of \(F\) lie in distinct cycles. Deleting the designated edge from each cycle then gives the required paths.

# 2. A Hamilton-cycle completion lemma

The following lemma supplies the first part of Theorem 1.

**Lemma 2.**  
Let \(n=2k+1\), and let \(1\le t<n\). Suppose the edges of \(K_t\) are colored with \(k\) colors such that:

- every color class is a linear forest, with isolated vertices included;
- if color \(i\) has \(e_i\) edges, then
  \[
  e_i\ge 2t-n.
  \]

Then this coloring extends to a Hamilton-cycle decomposition of \(K_n\).

### Proof

Put
\[
r=n-t.
\]
The color-\(i\) forest has
\[
c_i=t-e_i
\]
components, counting isolated vertices. The hypothesis says \(c_i\le r\).

Let \(U=V(K_t)\). Introduce a vertex \(z\), which initially represents all \(r\) vertices outside \(U\). Construct a multigraph \(H\) with:

- the original \(K_t\) on \(U\);
- \(r\) parallel edges between \(z\) and each \(u\in U\);
- \(\binom r2\) loops at \(z\).

For each \(u\in U\), color exactly
\[
2-d_i(u)
\]
of the \(zu\)-edges with color \(i\), where \(d_i(u)\) is its degree in the color-\(i\) forest. This uses exactly the required \(r\) parallel edges, since
\[
\sum_{i=1}^k(2-d_i(u))
=2k-(t-1)
=r.
\]

Give color \(i\) exactly \(r-c_i\) loops at \(z\). These numbers are nonnegative, and
\[
\begin{aligned}
\sum_{i=1}^k(r-c_i)
&=k(r-t)+\binom t2\\
&=\binom r2,
\end{aligned}
\]
using \(2k=t+r-1\).

For every color:

- each vertex of \(U\) has degree \(2\);
- \(z\) has degree \(2r\);
- the colored graph is connected.

Indeed, every component of the original linear forest has exactly two degree deficits, so it is attached to \(z\) at both ends. An isolated vertex receives two parallel edges to \(z\).

It remains to split \(z\) into \(r\) vertices while preserving the colored degrees and connectivity.

## The splitting step

More generally, suppose that \(z\) currently represents \(r\ge2\) vertices and that the underlying multigraph has:

- a complete graph on a set \(U\) of \(n-r\) individual vertices;
- \(r\) parallel edges from \(z\) to each vertex of \(U\);
- \(\binom r2\) loops at \(z\).

Suppose also that each color is connected, has degree \(2\) at every vertex of \(U\), and degree \(2r\) at \(z\).

For each color, its edges split into exactly \(r\) **excursions from \(z\) back to \(z\)**. An excursion is either a loop or a path whose internal vertices lie in \(U\). To see this, delete \(z\). Every resulting component is a path or an isolated vertex; a cycle component would contradict colored connectivity.

We will select two incidences at \(z\) from each color, belonging to different excursions. We also require:

- exactly one selected incidence among the \(r\) edges \(zu\), for each \(u\in U\);
- exactly \(r-1\) selected incidences from loops.

The selection follows from integral maximum flow. Use the following network:

| Arcs | Capacity |
|---|---:|
| source to each color | \(2\) |
| a color to each of its excursions | \(1\) |
| an excursion to the bin of each of its two incidences at \(z\) | \(1\) per incidence |
| each \(u\)-bin to the sink | \(1\) |
| the loop-bin to the sink | \(r-1\) |

A nonloop incidence has bin \(u\) if its edge is \(zu\); a loop incidence has the loop-bin.

There is a fractional flow of value \(2k\): send \(1/r\) through each incidence arc. Each excursion then carries \(2/r\le1\), each color carries \(2\), every \(u\)-bin receives \(1\), and the loop-bin receives
\[
\frac{2\binom r2}{r}=r-1.
\]
The total sink capacity is
\[
|U|+r-1=n-1=2k.
\]
By maximum-flow integrality, an integral flow of value \(2k\) exists. It gives exactly the required selection.

Create a new vertex \(x\), and move all selected incidences from \(z\) to \(x\). Thus:

- each \(u\in U\) becomes adjacent to \(x\) by exactly one edge;
- exactly \(r-1\) loops become \(xz\)-edges;
- no loop has both incidences selected, because an excursion has capacity \(1\).

The underlying multigraph now has the same form with \(U\cup\{x\}\) and \(r-1\) in place of \(U\) and \(r\). In particular, the number of remaining loops is
\[
\binom r2-(r-1)=\binom{r-1}{2}.
\]

In each color, \(x\) has degree \(2\) and \(z\) has degree \(2(r-1)\). Connectivity is preserved: the two selected, distinct excursions are joined through \(x\) into one excursion through \(z\).

Repeat until \(r=1\). The underlying graph is then \(K_n\), and every color is a connected spanning \(2\)-regular graph, hence a Hamilton cycle. No edge originally inside \(U\) has changed color. ∎

# 3. Missing edges supported on at most \(k+1\) vertices

We now prove condition 1 of Theorem 1.

Let \(U\) be the set of nonisolated vertices of \(F\), and put \(t=|U|\le k+1\). Give the \(k\) edges of \(F\) distinct colors.

We first extend this to a coloring of all of \(K_t\), maintaining that every color class is a linear forest.

Consider an uncolored edge \(uv\). A color is forbidden if adding \(uv\) would:

- give \(u\) or \(v\) degree \(3\) in that color; or
- create a monochromatic cycle.

Every forbidden color contributes at least two to
\[
d_{\mathrm{col}}(u)+d_{\mathrm{col}}(v),
\]
where these are the total degrees in already colored edges. Indeed, the first obstruction uses two incidences at one endpoint; the second, if the first is absent, uses one incidence at each endpoint.

Since \(uv\) is uncolored,
\[
d_{\mathrm{col}}(u)+d_{\mathrm{col}}(v)\le2(t-2).
\]
Thus at most \(t-2\) colors are forbidden. Because \(k\ge t-1\), an available color always exists.

Continuing greedily gives a coloring of \(K_t\) into \(k\) nonempty linear forests. Each color contains its original edge of \(F\), so
\[
e_i\ge1\ge 2t-(2k+1).
\]
Lemma 2 extends this coloring to a Hamilton-cycle decomposition of \(K_{2k+1}\).

Each Hamilton cycle contains exactly one edge of \(F\), because the edges of \(F\) have distinct colors. Delete that edge from each cycle. The result is the prescribed-endpoint Hamilton-path decomposition asserted in Theorem 1. ∎

The proof also gives a polynomial-time construction: greedy coloring, followed by the integral-flow splitting steps.

# 4. Missing edges forming a linear forest

This second construction handles disconnected missing-edge graphs with as many as \(2k\) nonisolated vertices.

Use vertex set
\[
\{\infty\}\cup\mathbb Z_{2k}.
\]
For \(i=0,\ldots,k-1\), define
\[
C_i=
\bigl(
\infty,\,
i,\,
i-1,\,
i+1,\,
i-2,\,
i+2,\,
\ldots,\,
i-(k-1),\,
i+(k-1),\,
i-k,\,
\infty
\bigr),
\]
with arithmetic modulo \(2k\). When \(k=1\), the interleaved list is empty.

These are Hamilton cycles partitioning the edges of \(K_{2k+1}\). In fact, their edge-coloring can be written as
\[
\operatorname{col}(\infty x)=x\pmod k
\]
and, for finite vertices,
\[
\operatorname{col}(xy)
=\left\lceil\frac{x+y}{2}\right\rceil\pmod k.
\]
To check the partition, the finite edges of \(C_i\) are exactly those with
\[
x+y\equiv 2i-1\quad\text{or}\quad 2i\pmod{2k}.
\]
These two sum classes contain \(k\) and \(k-1\) edges respectively, and the displayed cycle contains all of them.

We will embed \(F\) so that its \(k\) edges have distinct colors.

Let the nontrivial components of \(F\) have lengths
\[
\ell_1,\ldots,\ell_c,\qquad \sum_{j=1}^c\ell_j=k.
\]
Put
\[
s_0=0,\qquad s_j=\ell_1+\cdots+\ell_j.
\]

For component \(j\), initially use the consecutive finite labels
\[
s_{j-1},s_{j-1}+1,\ldots,s_j,
\]
and add \(k\) to every label if \(j\) is even. Labels are taken modulo \(2k\).

The edge colors in component \(j\) are
\[
s_{j-1}+1,\ldots,s_j\pmod k.
\]
Adding \(k\) to both endpoints does not change an edge color. Thus all \(k\) colors occur exactly once.

It remains to check vertex-disjointness.

- Intervals belonging to two odd-indexed components are disjoint.
- The same holds for two even-indexed components.
- Odd-indexed components use labels in \([0,k]\), while shifted even-indexed components use labels in \([k+1,2k]\).

The only possible collision is label \(0\): it occurs twice precisely when \(c\) is even, once at the start of the first component and once at the end of the last component. In that case, replace the first component’s initial \(0\) by \(\infty\). Its first edge changes from \(01\) to \(\infty1\), preserving color \(1\).

We therefore obtain a vertex-disjoint embedding of all components of \(F\), with one missing edge in each \(C_i\). Removing those edges proves condition 2 of Theorem 1. ∎

# 5. An extension below the counting threshold

The same explicit cycles settle another family without requiring exactly \(k\) missing edges.

**Corollary 3.**  
Let \(G\) be obtained from \(K_{2k}\) by adding one vertex \(x\) adjacent to a nonempty set \(A\) of clique vertices. Then \(G\) admits a decomposition into \(k\) paths if and only if
\[
|A|\le k.
\]
Thus Question 1.1 holds for every graph in this family.

### Proof

Put \(d=|A|\). If \(d>k\), then
\[
|E(G)|=k(2k-1)+d>2k^2,
\]
so \(k\) paths are impossible. Equivalently, \(G\) is an odd semi-clique.

Suppose \(1\le d\le k\). Choose a perfect matching \(M\) on the clique vertices such that every vertex of \(A\) is matched to a vertex outside \(A\).

Deleting \(\infty\) from the cycles in Section 4 decomposes \(K_{2k}\) into \(k\) Hamilton paths whose endpoint pairs form a perfect matching. Relabeling shows that this endpoint matching can be any prescribed \(M\).

Consequently, no path has both endpoints in \(A\). For each \(a\in A\), extend the unique path ending at \(a\) by the edge \(ax\). Each path is extended at most once, so this produces a decomposition of \(G\) into \(k\) simple paths. ∎

# 6. What remains unresolved

These arguments do **not** prove the general conjecture.

They do give a restriction on a counterexample at the extremal edge count. Suppose
\[
|V(G)|=2k+1,\qquad |E(G)|=2k^2,\qquad p(G)>k,
\]
and let \(F=K_{2k+1}-E(G)\). Then necessarily:

- \(F\) has at least \(k+2\) nonisolated vertices;
- its nonisolated part is disconnected;
- it is not a linear forest.

In fact, \(F\) must have at least two nontrivial tree components. To see this, discard its isolated vertices and write its components as \(F_1,\ldots,F_c\). Then
\[
|V(F)|-|E(F)|
=\sum_{j=1}^c\bigl(|V(F_j)|-|E(F_j)|\bigr)\ge2.
\]
A tree component contributes \(1\), and a component containing a cycle contributes at most \(0\).

There are two specific barriers to extending the proof as written:

1. **Large missing-edge support.**  
   The greedy coloring argument guarantees an available color only when \(t\le k+1\). For larger \(t\), neither the needed linear-forest coloring nor the completion lemma’s component bounds have been established here.

2. **More than \(k\) missing edges.**  
   Deleting several edges from a Hamilton cycle generally leaves several paths. Thus the threshold result is not monotone under further edge deletion and does not automatically extend to sparser graphs.

No result above is claimed to be new in the literature. The mathematical conclusions proved here are the prescribed-endpoint decompositions in Theorem 1 and the clique-plus-one-vertex case in Corollary 3; the full question remains unresolved by this attack.