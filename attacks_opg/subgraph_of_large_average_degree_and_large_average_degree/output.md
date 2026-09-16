```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The supplied C4-free theorem also settles g=5, and a self-contained sampling argument proves an all-g special case with explicit dependence on the number of degree scales.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; the partial bounds are not claimed to be new."
}
```

I work with finite simple graphs, ordinary—not necessarily induced—subgraphs, and girth \(+\infty\) for forests.

There are two outcomes: a correction to the stated unresolved range, and an elementary quantitative partial theorem. The latter allows arbitrarily large maximum-to-average degree ratios when only boundedly many degree scales occur.

## 1. The supplied result already covers \(g=5\)

Every graph has a bipartite spanning subgraph containing at least half its edges.

Using the \(C_4\)-free theorem supplied in the question, sufficiently large average degree therefore gives a \(C_4\)-free subgraph \(F\) of average degree at least \(2k\). A bipartite spanning subgraph of \(F\) with at least half its edges has average degree at least \(k\). It has no odd cycles and no \(C_4\), so its girth is at least \(6\), hence greater than \(5\).

More generally, an affirmative answer for \(g=2r\) implies one for \(g=2r+1\): first obtain average degree \(2k\) and girth greater than \(2r\), then take a bipartite subgraph.

Thus the supplied review should not list \(g=5\) as unresolved. This observation does not settle \(g=6\).

For completeness, \(g\le2\) is automatic for simple graphs, and \(g=3\) follows by taking a bipartite subgraph of a graph of average degree at least \(2k\).

## 2. A quantitative degree-scale theorem

Let \(G\) have positive average degree \(a\). Partition the vertices of degree at least \(a/4\) into the nonempty classes
\[
V_i=\left\{v:
  2^i\frac a4\le d_G(v)<2^{i+1}\frac a4
\right\},
\qquad i\ge0.
\]
Let \(t\) be the number of these nonempty classes. Gaps between their indices are allowed.

### Theorem
Fix integers \(g\ge4\) and \(k\ge1\), and put
\[
h=2\left\lfloor\frac g2\right\rfloor.
\]
If
\[
\boxed{\quad a\ge 2(16kt)^{h-1},\quad} \tag{1}
\]
then \(G\) contains a subgraph of average degree at least \(k\) and girth greater than \(g\).

Two consequences clarify the scope.

* If \(G\) has at most \(s\) distinct positive degree values, then \(t\le s\). Thus
  \[
  a\ge 2(16ks)^{h-1}
  \]
  suffices, independently of the sizes or ratios of those degree values.

* If \(\Delta=\Delta(G)\), then
  \[
  t\le 1+\left\lfloor\log_2\frac{4\Delta}{a}\right\rfloor.
  \]
  Consequently, the explicit condition
  \[
  a\ge
  2\left[
  16k\left(1+\left\lfloor\log_2\frac{4\Delta}{a}\right\rfloor\right)
  \right]^{h-1} \tag{2}
  \]
  suffices. The remaining dependence on \(\Delta\) is precisely why this is not a solution of the conjecture.

The proof uses a sampling lemma that balances the two sides of a bipartite graph before deleting short cycles.

## 3. Bipartite sampling lemma

### Lemma
Let \(h\ge4\) be even and \(k\ge1\). Let \(J\) be a bipartite graph with parts \(X,Y\) and \(m>0\) edges. Suppose
\[
d_J(x)\le A\quad(x\in X),\qquad
d_J(y)\le B\quad(y\in Y),
\]
where \(0<A\le B\), and suppose
\[
m\ge \rho\bigl(A|X|+B|Y|\bigr),
\qquad 0<\rho\le\frac12.
\]
If
\[
A\ge (k/\rho)^{h-1}, \tag{3}
\]
then \(J\) contains a subgraph of average degree at least \(k\) and girth at least \(h+2\).

### Proof

Set
\[
z=\frac{k}{\rho},\qquad p=\frac AB,\qquad q=\frac zA.
\]
Here \(z\ge2\). Condition (3) ensures \(q\le1\).

Independently retain each vertex of \(X\) with probability \(p\), and retain every vertex of \(Y\). Independently mark each edge with probability \(q\). Keep an edge exactly when it is marked and its endpoint in \(X\) was retained.

Let \(N,M\) be the resulting numbers of vertices and edges. Then
\[
\mathbb E M=mpq
\]
and
\[
\begin{aligned}
\mathbb E N
 &=p|X|+|Y|\\
 &=\frac{A|X|+B|Y|}{B}\\
 &\le \frac{m}{\rho B}
 =\frac{mp}{\rho A}.
\end{aligned}
\]
Therefore
\[
\frac{k}{2}\mathbb E N\le \frac12\mathbb E M. \tag{4}
\]

We next count short cycles. For \(j\ge2\), the number \(c_{2j}(J)\) of cycles of length \(2j\) satisfies
\[
c_{2j}(J)\le \frac{m(AB)^{j-1}}{2j}. \tag{5}
\]
Indeed, start with an edge directed from \(X\) to \(Y\), then choose the next \(2j-2\) edges. There are at most \((AB)^{j-1}\) choices, after which the closing edge is determined. Each simple \(2j\)-cycle is counted \(2j\) times.

A fixed \(2j\)-cycle survives with probability \(p^j q^{2j}\). Let \(C\) count all surviving cycles of lengths \(4,6,\ldots,h\). By (5),
\[
\begin{aligned}
\mathbb E C
&\le
\sum_{j=2}^{h/2}
\frac{m(AB)^{j-1}}{2j}\,p^j q^{2j}\\
&=
\frac{mpq}{A}
\sum_{j=2}^{h/2}\frac{z^{2j-1}}{2j}.
\end{aligned}
\]
Since \(z\ge2\),
\[
\begin{aligned}
\sum_{j=2}^{h/2}\frac{z^{2j-1}}{2j}
&\le
\frac{z^{h-1}}4\sum_{\ell\ge0}z^{-2\ell}\\
&\le \frac{z^{h-1}}3.
\end{aligned}
\]
Using (3),
\[
\mathbb E C\le \frac13\mathbb E M. \tag{6}
\]

Combining (4) and (6) gives
\[
\mathbb E\!\left(M-C-\frac{kN}{2}\right)
\ge \frac16\mathbb E M>0.
\]
Hence some realization satisfies
\[
M-C>\frac{kN}{2}.
\]

Choose one edge from each short cycle in that realization and delete the union of the chosen edges. At most \(C\) edges are deleted. Every original short cycle is broken, and edge deletion cannot create a cycle.

The resulting graph therefore has average degree greater than \(k\). It remains bipartite and has no even cycle of length at most \(h\), so its girth is at least \(h+2\). ∎

For example, in an \((r,s)\)-biregular bipartite graph, the lemma applies with \(\rho=1/2\). Thus
\[
\min(r,s)\ge(2k)^{h-1}
\]
suffices, with no restriction on \(\max(r,s)/\min(r,s)\).

## 4. Extracting a weighted-dense pair of degree classes

We now prove the theorem.

Write \(n=|V(G)|\), \(m=|E(G)|\), so \(a=2m/n\). Let
\[
U=\{v:d_G(v)\ge a/4\}.
\]
Deleting \(V(G)\setminus U\) removes at most
\[
\sum_{v\notin U}d_G(v)\le \frac{an}{4}=\frac m2
\]
edges. Thus
\[
e(G[U])\ge \frac m2.
\]
Choose a bipartition \(U=X\cup Y\) whose crossing graph \(B\) has at least half these edges. Then
\[
e(B)\ge \frac m4. \tag{7}
\]

For every occupied degree class, put
\[
D_i=2^{i+1}\frac a4,\qquad
X_i=X\cap V_i,\qquad Y_i=Y\cap V_i,
\]
and define
\[
w_i^X=D_i|X_i|,\qquad w_i^Y=D_i|Y_i|.
\]
Because \(D_i\le2d_G(v)\) for \(v\in V_i\),
\[
S:=\sum_i(w_i^X+w_i^Y)
\le 2\sum_{v\in U}d_G(v)
\le4m. \tag{8}
\]

Let \(e_{ij}\) count the edges between \(X_i\) and \(Y_j\). These edge sets partition \(E(B)\), and
\[
\sum_{i,j}(w_i^X+w_j^Y)=tS.
\]
Consequently, (7)–(8) imply that some pair \(i,j\) satisfies
\[
e_{ij}\ge \frac{w_i^X+w_j^Y}{16t}. \tag{9}
\]
This is simply weighted averaging; pairs of zero weight can be omitted.

Let \(J\) consist of the edges between this \(X_i\) and \(Y_j\). Its degree upper bounds on the two sides are \(D_i,D_j\), and (9) is exactly the density hypothesis of the sampling lemma with
\[
\rho=\frac1{16t}.
\]
Moreover,
\[
\min(D_i,D_j)\ge \frac a2
\ge (16kt)^{h-1}
=(k/\rho)^{h-1}.
\]
After interchanging the two sides if necessary, all hypotheses of the lemma hold.

We obtain a subgraph of average degree at least \(k\) and girth at least \(h+2\). Since \(g\in\{h,h+1\}\), its girth is greater than \(g\). ∎

## 5. The exact limitation of this approach

The unresolved step is removing the dependence on the number \(t\) of degree scales. The averaging argument pays a factor \(1/t\), and selecting just one pair of original degree classes cannot generally retain large average degree.

Here is an explicit obstruction to that particular strategy.

Fix \(r\ge2\), let
\[
N=r2^r,\qquad D_j=r2^j\quad(1\le j\le r),
\]
and take a set \(X\) of \(N\) vertices. For each \(j\), partition \(X\) into consecutive blocks of size \(D_j\). Create one vertex for each block and join it to all vertices in that block. Let \(Y_j\) be the set of vertices created at level \(j\).

Then:

* every vertex of \(X\) has degree \(r\);
* every vertex of \(Y_j\) has degree \(D_j\);
* the average degree is
  \[
  \frac{2r}{1+\sum_{j=1}^r D_j^{-1}}
  =
  \frac{2r^2}{r+1-2^{-r}}
  \sim 2r;
  \]
* the graph between \(X\) and any single \(Y_j\) is a disjoint union of stars.

Thus the average degree tends to infinity, but every subgraph using only one pair of original degree classes is a forest and has average degree strictly less than \(2\).

This is **not** a counterexample to Thomassen’s conjecture. The nested partitions even give a \(K_{r,2r}\). It shows only that a uniform proof must sometimes combine several original degree scales rather than extract a single pair.

**Conclusion.** The \(g=5\) boundary in the supplied review is incorrect, and the theorem above gives a fully proved all-\(g\) result under an explicit degree-scale condition. I have neither a proof nor a counterexample for unrestricted graphs in the first remaining case \(g=6\).