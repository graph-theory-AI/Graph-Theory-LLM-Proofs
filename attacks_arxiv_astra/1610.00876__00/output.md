```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Explicit quadratic obstructions and a sublinear, order-dependent sufficient degree bound are obtained, but not the conjectured absolute threshold.",
  "would_publish": false,
  "caveats": "No novelty or optimality is claimed; the order-independent conjecture remains unresolved here."
}
```

## 1. Scope of the partial results

All digraphs below are finite, loopless, and have no parallel arcs; opposite arcs are allowed. A subdivision uses directed replacement paths whose interiors are pairwise disjoint and avoid all branch vertices.

Write \(M(k)=\mathrm{mader}_{\delta^0}(TT_k)\), **if this threshold exists**. I establish two self-contained statements:

1. For \(k\ge 4\), any such threshold satisfies
   \[
   M(k)\ge
   \max\left\{
   \left\lceil\frac{k^2}{7}\right\rceil,\,
   \left\lceil\frac{7k^2-6k}{48}\right\rceil
   \right\}.
   \]
   The first bound also holds for \(k=3\).

2. For each fixed \(k\ge3\), putting \(t=\binom{k}{2}\), every sufficiently large \(n\)-vertex digraph satisfying
   \[
   \delta^+(D)\ge
   4\log t\,
   \frac{n\log\log\log n}{\log\log n}
   \tag{1}
   \]
   contains a subdivision of \(TT_k\). Thus the same holds under this minimum-semidegree hypothesis.

The second bound is \(o(n)\), but it still grows with \(n\). It does not prove the conjecture.

## 2. Explicit quadratic lower bounds

Let \(C_r[h]\) be the digraph with independent vertex classes
\[
V_0,\ldots,V_{r-1},
\qquad |V_i|=h,
\]
and all arcs from \(V_i\) to \(V_{i+1}\), with indices modulo \(r\). For \(r\ge3\), this is an oriented graph with
\[
\delta^0(C_r[h])=h.
\]

Suppose it contains a subdivision of \(TT_k\), with \(b_i\) branch vertices in \(V_i\). Order the branch vertices according to the transitive order of \(TT_k\).

Call a tournament arc between branches in consecutive classes **reversed** if its direction is opposite to \(V_i\to V_{i+1}\). Let \(R\) be the number of these reversed arcs. Then
\[
R\ge \min_i b_i b_{i+1}.
\tag{2}
\]

Indeed, if all \(b_i>0\), every selection of one branch vertex from each class must have a reversed consecutive-class arc: otherwise their transitive order would contain a directed \(r\)-cycle. There are \(P=\prod_i b_i\) selections, while a reversed arc between classes \(i,i+1\) belongs to
\[
\frac{P}{b_i b_{i+1}}
\le \frac{P}{\min_j b_jb_{j+1}}
\]
selections. Double-counting proves (2). If some \(b_i=0\), its right-hand side is zero.

### 2.1. A cyclic tripartite obstruction

Take \(r=3\), and write the branch counts as \(a,b,c\), with \(a+b+c=k\).

A replacement path joining branches in the same class has at least two internal vertices. A reversed cross-class arc requires at least one internal vertex. Consequently, the subdivision uses at least
\[
\begin{aligned}
k+2\left(\binom a2+\binom b2+\binom c2\right)+R
&\ge a^2+b^2+c^2+\min\{ab,bc,ca\}
\end{aligned}
\]
vertices.

Relabel cyclically so that the minimum product is \(ab\). The identity
\[
a^2+b^2+c^2+ab
=
\frac{3k^2}{7}
+\frac74\left(a+b-\frac{4k}{7}\right)^2
+\frac14(a-b)^2
\]
gives
\[
3h\ge \frac{3k^2}{7}.
\]
Thus
\[
C_3\!\left[\left\lceil k^2/7\right\rceil-1\right]
\]
has no \(TT_k\)-subdivision, proving
\[
M(k)\ge \left\lceil\frac{k^2}{7}\right\rceil
\qquad(k\ge3).
\tag{3}
\]

For example, \(C_3[5]\) has minimum semidegree \(5\) and no subdivision of \(TT_6\).

### 2.2. A slightly stronger asymptotic obstruction

Take \(r=4\), with branch counts \(a,b,c,d\).

Here:

- a same-class replacement path needs at least three internal vertices;
- a path between opposite classes needs at least one;
- a reversed consecutive-class arc needs at least two.

Hence the subdivision uses at least
\[
k+3\sum_{x\in\{a,b,c,d\}}\binom x2
+ac+bd+2\min\{ab,bc,cd,da\}
\tag{4}
\]
vertices.

Rotate the labels so that the minimum product is \(ab\), and put
\[
Q=\frac32(a^2+b^2+c^2+d^2)+ac+bd+2ab.
\]
Expression (4) is \(Q-k/2\). Since \(a+b+c+d=k\),
\[
\begin{aligned}
Q={}&\frac{7k^2}{12}
+\frac32\left(a+b-\frac{k}{3}\right)^2\\
&+\frac14(a-b+c-d)^2+\frac12(c-d)^2.
\end{aligned}
\]
It follows that
\[
4h\ge \frac{7k^2}{12}-\frac{k}{2},
\]
and therefore
\[
M(k)\ge
\left\lceil\frac{7k^2-6k}{48}\right\rceil
\qquad(k\ge4).
\tag{5}
\]

In particular, any threshold in the conjecture must be at least
\[
\frac{7}{48}k^2-O(k).
\]
These examples do not disprove the conjecture: for a fixed \(k\), they provide obstructions only at bounded semidegree.

## 3. A sufficient bound depending on the order

The upper-bound argument finds a complete blow-up of a directed cycle. Such a blow-up can route all arcs of \(TT_k\) using separate internal vertices.

### Lemma: a dense relation contains a Cartesian box

Let \(r\ge1\), \(s\ge2\), and \(0<\alpha\le1\). Suppose \(|X_i|=n\) for \(1\le i\le r\), and
\[
E\subseteq X_1\times\cdots\times X_r,
\qquad |E|\ge\alpha n^r.
\]
If
\[
n\ge s^2(2/\alpha)^{s^{r-1}},
\tag{6}
\]
then there are \(A_i\subseteq X_i\), each of size \(s\), such that
\[
A_1\times\cdots\times A_r\subseteq E.
\]

#### Proof

Induct on \(r\). The case \(r=1\) is immediate.

For \(r\ge2\), let \(d(x)\) be the number of extensions of
\(x\in X_1\times\cdots\times X_{r-1}\) into \(E\). Convexity gives
\[
\sum_x d(x)^s
\ge \alpha^s n^{r-1+s}.
\tag{7}
\]
This counts pairs consisting of \(x\) and an ordered \(s\)-tuple of common extensions, allowing repetitions.

There are at most \(\binom{s}{2}n^{s-1}\) ordered \(s\)-tuples with a repeated coordinate. Their contribution to (7) is at most
\[
\binom{s}{2}n^{r+s-2}.
\]
Condition (6) implies \(n\ge s^2\alpha^{-s}\), so at least
\[
\frac{\alpha^s}{2}n^{r+s-1}
\]
of the counted pairs use \(s\) distinct extensions. Thus some set of \(s\) distinct extensions has a common \((r-1)\)-coordinate relation of density at least
\[
\beta=\alpha^s/2.
\]

The induction hypothesis applies because
\[
s^2(2/\alpha)^{s^{r-1}}
\ge
s^2(2/\beta)^{s^{r-2}},
\]
using \(s\ge2\). It supplies the remaining \(r-1\) sets. ∎

### Theorem: an explicit dense-degree bound

Fix \(k\ge3\), \(0<\varepsilon<1\), and set \(t=\binom{k}{2}\). Choose an integer \(m\ge2\) satisfying
\[
m(1-\varepsilon)^{m-1}\le\frac12.
\tag{8}
\]
Define
\[
N=
\left\lceil
\max\left\{
m^2,\,
t^2(8m^{m+1})^{t^{m-1}}
\right\}
\right\rceil.
\tag{9}
\]

Every \(n\)-vertex digraph with
\[
n\ge N,\qquad \delta^+(D)\ge\varepsilon n
\]
contains a subdivision of \(TT_k\). All replacement paths can be chosen to have the same length, at most \(m\).

#### Proof

Choose \(m\) distinct vertices uniformly at random. Conditional on one selected vertex being \(v\), the probability that none of the other selected vertices is an out-neighbour of \(v\) is at most
\[
\left(1-\frac{d^+(v)}{n-1}\right)^{m-1}
\le (1-\varepsilon)^{m-1}.
\]
By a union bound and (8), the induced sample has minimum outdegree at least one with probability at least \(1/2\). Such a sample contains a directed cycle.

For \(2\le\ell\le m\), let \(p_\ell\) be the probability that a uniformly chosen ordered \(\ell\)-tuple of distinct vertices forms a directed cycle in its listed order. A union bound over ordered choices of positions in the sample gives
\[
\frac12
\le \sum_{\ell=2}^{m}m^\ell p_\ell
\le m^{m+1}\max_{\ell}p_\ell.
\]
Therefore some \(\ell\in\{2,\ldots,m\}\) satisfies
\[
p_\ell\ge\frac1{2m^{m+1}}.
\tag{10}
\]

Let \(E\subseteq V(D)^\ell\) consist of the ordered, distinct-vertex directed cycles of length \(\ell\). Since \(n\ge m^2\),
\[
(n)_\ell
=n^\ell\prod_{j=0}^{\ell-1}(1-j/n)
\ge \frac12n^\ell.
\]
Together with (10), this gives
\[
|E|\ge \frac{n^\ell}{4m^{m+1}}.
\]

Apply the lemma with
\[
r=\ell,\qquad s=t,\qquad
\alpha=\frac1{4m^{m+1}}.
\]
Condition (9) is sufficient. We obtain sets
\[
A_1,\ldots,A_\ell,\qquad |A_i|=t,
\]
such that every tuple in their Cartesian product is a distinct-vertex directed cycle.

The sets \(A_i\) are pairwise disjoint: an element in two of them would give a tuple with a repeated vertex. Moreover, every possible arc from \(A_i\) to \(A_{i+1}\), cyclically, is present.

Choose branch vertices \(b_1,\ldots,b_k\) in \(A_1\). For each pair \(i<j\), and in each class \(A_q\) with \(2\le q\le\ell\), choose a distinct vertex \(x_q^{ij}\). This is possible because there are exactly \(t\) pairs. Use
\[
b_i,x_2^{ij},x_3^{ij},\ldots,x_\ell^{ij},b_j
\]
as the replacement path for \(i\to j\).

These paths have pairwise disjoint interiors, avoid every branch vertex internally, and all have length \(\ell\). They form the required subdivision. ∎

## 4. Extracting the sublinear bound

All logarithms in this section are natural. Fix \(k\ge3\), let \(t=\binom{k}{2}\), and put
\[
L=\log\log n,\qquad
\varepsilon_n=4\log t\,\frac{\log L}{L}.
\]
For sufficiently large \(n\), choose
\[
m=\left\lceil
\frac{2}{\varepsilon_n}\log\frac{2}{\varepsilon_n}
\right\rceil.
\]
Then
\[
m(1-\varepsilon_n)^{m-1}
\le m e^{-\varepsilon_n(m-1)}
\longrightarrow0,
\]
so (8) holds eventually. Also,
\[
m=\left(\frac{1}{2\log t}+o(1)\right)L.
\]
For the bound \(N\) in (9), this yields
\[
\log N
=
\exp\bigl((1/2+o(1))L\bigr)
=
(\log n)^{1/2+o(1)}
=o(\log n).
\]
Consequently \(N\le n\) for all sufficiently large \(n\). Applying the theorem with \(\varepsilon=\varepsilon_n\) proves (1).

The argument actually works for any fixed loopless target digraph: replace \(t\) by the maximum of its number of vertices, its number of arcs, and \(2\).

## 5. The remaining gap

The subdivision arguments above are complete under their stated hypotheses. The unresolved issue is precisely the dependence on \(n\).

The sufficient degree in (1) tends to infinity with \(n\). For a fixed proposed threshold \(d\), digraphs with \(\delta^0(D)\ge d\) can have arbitrarily large order and need not satisfy (1). Thus neither the dense-cycle argument nor the explicit obstructions supplies a function of \(k\) alone.

In particular, this does **not** establish the existence of \(\mathrm{mader}_{\delta^0}(TT_5)\), nor resolve Conjecture 3.