```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain an all-g partial theorem with a linear local degree-scale loss, and confirm that the supplied C4-free result already settles g=5.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; no novelty claim is made for the partial theorem."
}
```

Throughout, graphs are finite and simple, subgraphs need not be induced, and forests have girth \(+\infty\).

The main partial result below improves the degree-scale dependence in the previous attempt: the loss is **linear**, rather than a power depending on the girth. It also produces a subgraph whose maximum degree is at most \(32k\).

## 1. The supplied theorem covers \(g=5\)

The parity observation in the previous attempt is correct.

Every graph has a bipartite spanning subgraph containing at least half its edges. Apply the \(C_4\)-free theorem stated in the question with target average degree \(2k\), and then take such a bipartite subgraph. The result has average degree at least \(k\), no odd cycles, and no \(C_4\). Its girth is therefore at least \(6\), and hence greater than \(5\).

More generally, validity of the conjecture for \(g=2r\), for every \(k\), implies validity for \(g=2r+1\), by first using target average degree \(2k\).

Thus the supplied review's designation of \(g=5\) as unresolved is incorrect. This does not settle \(g=6\).

## 2. A partial theorem with linear degree-scale loss

Let \(G\) have \(n\) vertices, \(m>0\) edges, and average degree
\[
a=\frac{2m}{n}.
\]
Put
\[
U=\{v:d_G(v)\ge a/4\},
\qquad
V_i=\left\{v:2^i\frac a4\le d_G(v)<2^{i+1}\frac a4\right\}
\quad(i\ge0).
\]
For \(v\in U\), define
\[
s(v)=\bigl|\{i:N_G(v)\cap V_i\ne\varnothing\}\bigr|.
\]
Thus \(s(v)\) counts the degree scales occurring among the neighbors of \(v\) that belong to \(U\). Set
\[
S=\sum_{v\in U}s(v),
\qquad
\sigma=\frac Sn.
\]
We will see below that \(S>0\).

### Theorem
Let \(g\ge4\) and \(k\ge1\) be integers, and put
\[
h=2\left\lfloor\frac g2\right\rfloor.
\]
If
\[
\boxed{\qquad a\ge 2048\,\sigma\,(2k)^{h-1},\qquad} \tag{1}
\]
then \(G\) contains a subgraph \(F\) satisfying
\[
\overline d(F)>k,\qquad
\operatorname{girth}(F)>g,\qquad
\Delta(F)\le32k.
\]

In particular, if \(t\) is the number of nonempty classes \(V_i\), then \(\sigma\le t\), so
\[
\boxed{\qquad a\ge2048\,t\,(2k)^{h-1}\qquad} \tag{2}
\]
suffices.

This replaces the \(t^{h-1}\) dependence of the previous attempt by a linear dependence on \(t\). More strongly, the theorem uses the average *local* scale count \(\sigma\), not the total number of scales.

Some immediate special cases are:

* If \(G\) has at most \(s\) distinct positive degree values, then
  \[
  a\ge2048\,s\,(2k)^{h-1}
  \]
  suffices, with no restriction on the ratios of those degrees.
* The same bound holds if every vertex in \(U\) sees at most \(s\) of the classes \(V_i\), even when arbitrarily many classes occur globally.
* Since
  \[
  t\le1+\left\lfloor\log_2\frac{4\Delta(G)}a\right\rfloor,
  \]
  the explicit condition
  \[
  a\ge2048(2k)^{h-1}
  \left(1+\left\lfloor\log_2\frac{4\Delta(G)}a\right\rfloor\right) \tag{3}
  \]
  suffices.

The dependence on \(\Delta(G)\) in (3) is logarithmic, not a power of a logarithm depending on \(g\).

The proof consists of a degree-adapted sparsification lemma and a one-sided degree-scale extraction.

## 3. Degree-adapted sparsification

### Lemma 1
Let \(J\) be a nonempty bipartite graph. Write
\[
D=\Delta(J),\qquad
P=\min_{uv\in E(J)}d_J(u)d_J(v).
\]
Let \(h\ge4\) be even and \(k\ge1\). If
\[
\frac PD\ge(2k)^{h-1}, \tag{4}
\]
then \(J\) contains a subgraph \(F\) with
\[
\overline d(F)>k,\qquad
\operatorname{girth}(F)\ge h+2,\qquad
\Delta(F)\le32k.
\]

### Proof

Delete isolated vertices of \(J\), and abbreviate \(d_J(v)\) to \(d_v\). Let \(m_J=|E(J)|\) and set
\[
z=2k.
\]

Independently retain each vertex \(v\) with probability
\[
p_v=\frac{d_v}{D}.
\]
Independently of these choices, mark each edge \(uv\) with probability
\[
q_{uv}=\frac{zD}{d_ud_v}.
\]
Keep a marked edge precisely when both endpoints were retained. These are valid probabilities: by (4),
\[
q_{uv}\le \frac{zD}{P}\le z^{2-h}\le1.
\]

Let \(N,M\) denote the numbers of retained vertices and edges. Then
\[
\mathbb E N=\frac{2m_J}{D},
\qquad
\mathbb E M=\frac{m_Jz}{D}.
\]
Consequently,
\[
\frac{k}{2}\mathbb E N=\frac12\mathbb E M. \tag{5}
\]

#### Counting short cycles

Let \(T\) be the normalized adjacency matrix of \(J\):
\[
T_{uv}=
\begin{cases}
(d_ud_v)^{-1/2},&uv\in E(J),\\
0,&\text{otherwise}.
\end{cases}
\]
All eigenvalues of \(T\) belong to \([-1,1]\). Indeed, for every real vector \(x\),
\[
|x^{\mathsf T}Tx|
\le
\sum_{uv\in E(J)}
\left(\frac{x_u^2}{d_u}+\frac{x_v^2}{d_v}\right)
=\sum_vx_v^2.
\]
It follows that, for \(j\ge1\),
\[
\operatorname{tr}(T^{2j})
\le\operatorname{tr}(T^2)
=2\sum_{uv\in E(J)}\frac1{d_ud_v}
\le\frac{2m_J}{P}. \tag{6}
\]

A fixed cycle \(C\) of length \(2j\) survives with probability
\[
\prod_{v\in V(C)}p_v\prod_{uv\in E(C)}q_{uv}
=\frac{z^{2j}}{\prod_{v\in V(C)}d_v}.
\]
Moreover, that cycle contributes
\[
\frac{4j}{\prod_{v\in V(C)}d_v}
\]
to \(\operatorname{tr}(T^{2j})\). Thus, if \(C_{\rm short}\) counts the surviving cycles of lengths \(4,6,\ldots,h\), then
\[
\begin{aligned}
\mathbb E C_{\rm short}
&\le
\sum_{j=2}^{h/2}\frac{z^{2j}}{4j}\operatorname{tr}(T^{2j})\\
&\le
\frac{m_J}{P}\sum_{j=2}^{h/2}\frac{z^{2j}}{2j}.
\end{aligned}
\]
Since \(z\ge2\),
\[
\sum_{j=2}^{h/2}\frac{z^{2j-1}}{2j}
\le
\frac{z^{h-1}}4\sum_{\ell\ge0}z^{-2\ell}
\le\frac{z^{h-1}}3.
\]
Using (4),
\[
\mathbb E C_{\rm short}
\le \frac13\mathbb E M. \tag{7}
\]

#### Controlling maximum degree

Conditioned on a vertex \(v\) being retained, its incident edges survive independently, each with probability
\[
p_uq_{uv}=\frac{z}{d_v}.
\]
Thus its conditional expected degree is exactly \(z\).

Call a retained vertex bad if its degree exceeds \(16z\), and let
\[
W=\sum_{\substack{v\text{ retained}\\d(v)>16z}}d(v).
\]
Conditioned on a particular edge incident with \(v\) surviving, the expected number of other surviving incident edges is at most \(z\). Markov's inequality gives
\[
\Pr\bigl(d(v)>16z\mid uv\text{ survives}\bigr)\le\frac1{16}.
\]
Summing over edge-endpoint incidences,
\[
\mathbb E W\le\frac18\mathbb E M. \tag{8}
\]

Combining (5), (7), and (8),
\[
\mathbb E\left(M-C_{\rm short}-W-\frac{kN}{2}\right)
\ge
\left(1-\frac13-\frac18-\frac12\right)\mathbb E M
=\frac1{24}\mathbb E M>0.
\]
Choose a realization for which this expression is positive. Delete all edges incident with bad vertices, and choose and delete one edge from every short cycle present in that realization. At most \(W+C_{\rm short}\) edges are deleted.

The resulting graph has average degree greater than \(k\), maximum degree at most \(16z=32k\), and no cycle of length at most \(h\). Being bipartite, its girth is at least \(h+2\). ∎

## 4. Extracting a suitable bipartite graph

The next lemma is the source of the linear scale loss.

### Lemma 2
With \(a,U,S,\sigma\) defined in Section 2, \(G\) contains a nonempty bipartite subgraph \(J\) such that
\[
\frac{\min_{uv\in E(J)}d_J(u)d_J(v)}{\Delta(J)}
\ge \frac{m}{1024S}
=\frac{a}{2048\sigma}. \tag{9}
\]

### Proof

Deleting vertices outside \(U\) removes at most
\[
\sum_{v\notin U}d_G(v)\le\frac{an}{4}=\frac m2
\]
edges. Hence
\[
e(G[U])\ge\frac m2.
\]
Take a bipartite spanning subgraph \(B\) of \(G[U]\) with
\[
e(B)\ge\frac m4.
\]
In particular, \(S>0\).

Orient every edge of \(B\) toward an endpoint of larger original degree \(d_G\), breaking ties arbitrarily. Call \(v\) good if
\[
d_B^-(v)\ge\frac{d_G(v)}{16}.
\]
The number of edges directed into vertices that are not good is at most
\[
\sum_{v\text{ not good}}d_B^-(v)
\le \frac1{16}\sum_{v\in U}d_G(v)
\le\frac m8.
\]
Therefore at least \(m/8\) edges are directed into good vertices.

For every degree class \(V_i\) and each side of the bipartition of \(B\), form a cell consisting of all edges directed into good vertices of \(V_i\) on that side. Its targets lie on that side, and its sources lie on the opposite side.

For a nonempty cell, let \(e\) be its number of edges and \(x\) its number of distinct sources. A vertex \(v\) occurs as a source in at most \(s(v)\) cells. Consequently,
\[
\sum_{\text{cells}}x\le S,
\qquad
\sum_{\text{cells}}e\ge\frac m8.
\]
Some cell therefore satisfies
\[
\frac ex\ge\frac{m}{8S}. \tag{10}
\]

Fix that cell. Write
\[
D_i=2^{i+1}\frac a4
\]
for the upper degree bound of its target class, and let \(y\) be the number of targets.

Every target \(w\) has all its incoming edges in this cell, so its cell degree is at least
\[
\frac{d_G(w)}{16}\ge\frac{D_i}{32}.
\]
Thus
\[
e\ge\frac{D_i y}{32}. \tag{11}
\]
Also, both targets and sources have original degree less than \(D_i\): for a source this follows from the orientation toward an endpoint of at least as large original degree. Hence the cell has maximum degree at most \(D_i\).

Set
\[
\alpha=\frac{e}{2x},
\qquad
\beta=\frac{D_i}{64}.
\]
By (11),
\[
\alpha x+\beta y\le e.
\]

Repeatedly delete a source of current degree less than \(\alpha\), or a target of current degree less than \(\beta\). A nonempty graph remains. Otherwise, summing the degrees at deletion would give
\[
e<\alpha x+\beta y\le e,
\]
a contradiction.

Call the remaining graph \(J\). Every edge of \(J\) has endpoint-degree product at least \(\alpha\beta\), while \(\Delta(J)\le D_i\). Therefore, by (10),
\[
\begin{aligned}
\frac{\min_{uv\in E(J)}d_J(u)d_J(v)}{\Delta(J)}
&\ge\frac{\alpha\beta}{D_i}\\
&=\frac{e}{128x}\\
&\ge\frac{m}{1024S}.
\end{aligned}
\]
This proves (9). ∎

### Completion of the theorem

Under (1), Lemma 2 supplies a bipartite \(J\) satisfying
\[
\frac{\min_{uv\in E(J)}d_J(u)d_J(v)}{\Delta(J)}
\ge(2k)^{h-1}.
\]
Apply Lemma 1. Its output has girth at least \(h+2\), which is greater than \(g\), since \(g\in\{h,h+1\}\).

All the stated degree-scale consequences follow from \(\sigma\le t\). ∎

One can strengthen the minimum-degree conclusion as well. Applying the theorem with \(2k\) in place of \(k\), then repeatedly deleting vertices of degree less than \(k\), gives a nonempty subgraph with
\[
\delta\ge k,\qquad \Delta\le64k,\qquad \operatorname{girth}>g.
\]
The pruning cannot empty a graph of average degree greater than \(2k\).

## 5. A further all-\(g\) special case

Suppose that, for every \(v\in U\), the degrees of its neighbors in \(U\) differ by a factor of at most \(R\). Then those neighbors occupy at most
\[
1+\lceil\log_2 R\rceil
\]
dyadic classes. Thus
\[
a\ge2048\bigl(1+\lceil\log_2R\rceil\bigr)(2k)^{h-1}
\]
suffices.

This allows arbitrarily many global degree scales and arbitrarily large maximum-to-average degree ratios. In particular, it does not require global almost-regularity.

## 6. What remains unresolved

The essential missing step is removing the local scale factor. Large average degree alone does not force \(a/\sigma\) to be large.

Here is a fully specified example, also validating the obstruction used in the previous attempt. Fix \(r\ge2\), let
\[
N=r2^r,
\]
and take a set \(X\) of \(N\) vertices. For each \(j=1,\ldots,r\), partition \(X\) into consecutive blocks of size \(r2^j\). Introduce one vertex for each block and join it to all vertices in that block; call these vertices \(Y_j\).

Then every \(x\in X\) has degree \(r\), while every vertex in \(Y_j\) has degree \(r2^j\). Writing
\[
b=\sum_j|Y_j|=2^r-1,
\]
we have
\[
n=N+b,\qquad m=rN,\qquad a=\frac{2rN}{N+b}\sim2r.
\]
All vertices belong to \(U\). Each \(x\in X\) sees \(r\) degree scales, and every vertex in the \(Y_j\)'s sees one. Consequently,
\[
S=rN+b,
\qquad
\frac a\sigma=\frac{2m}{S}
=\frac{2rN}{rN+b}<2.
\]
Thus the average degree tends to infinity, while the quantity controlled by the partial theorem stays bounded.

This is **not** a counterexample to Thomassen's conjecture. The nested blocks contain a \(K_{2r,r}\); for every fixed \(g,k\), Lemma 1 applies to that biclique once \(r\) is sufficiently large. Rather, the example shows that the present extraction criterion cannot establish the unrestricted conjecture merely by increasing the average-degree threshold.

**Conclusion.** The supplied \(C_4\)-free theorem settles \(g=5\). For all \(g\), the argument above proves a quantitative special case with linear local degree-scale dependence and bounded maximum degree in the resulting subgraph. It does not prove or disprove the unrestricted conjecture, including the first remaining case \(g=6\).