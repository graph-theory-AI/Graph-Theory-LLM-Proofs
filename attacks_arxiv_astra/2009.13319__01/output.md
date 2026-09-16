```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Randomly ordered line graphs of complete bipartite graphs refute the conjecture with H the directed triangle and F any orientation of the claw.",
  "would_publish": false,
  "caveats": "The proof is self-contained; no novelty claim is made relative to the recent counterexample reported in the supplied catalogue."
}
```

## 1. The counterexample instance

All forbidden-subdigraph conditions below are **induced**.

Let \(H=\vec C_3\), the directed triangle, and let \(F=S_3^+\), the oriented star with arcs
\[
x\to y_1,\qquad x\to y_2,\qquad x\to y_3.
\]
The tournament \(\vec C_3\) is a hero: every \(\vec C_3\)-free tournament is transitive, and therefore has dichromatic number \(1\). Also, \(F\) is an oriented star. Thus the conjecture asserts that
\[
\{\overleftrightarrow{K_2},\vec C_3,S_3^+\}
\]
is heroic.

We disprove this by proving the following quantitative statement.

**Theorem.** For every integer \(k\ge 1\), there is an oriented graph \(D_k\) on \(4096k^4\) vertices such that:

1. its underlying graph is claw-free;
2. it contains no directed triangle;
3. \(\vec\chi(D_k)>k\).

In particular, these graphs avoid **every** orientation of the claw, not merely \(S_3^+\).

## 2. The random construction

For a positive integer \(n\), let \(R_n\) be the graph with vertex set
\[
[n]\times[n],
\]
where two distinct vertices are adjacent exactly when they share a row or a column. Equivalently,
\[
R_n=L(K_{n,n}).
\]

Independently for each of the \(n\) rows and \(n\) columns, choose a uniformly random total order of its vertices. Orient each edge from the earlier to the later endpoint in the order of its unique common row or column. Denote the resulting oriented graph by \(D\).

Every realization has the following properties.

* **No digons:** every edge receives exactly one direction.
* **Claw-free underlying graph:** the neighborhood of any vertex is covered by two cliques, its row-neighbors and its column-neighbors. It cannot contain three pairwise nonadjacent vertices.
* **No directed triangle:** every triangle of \(R_n\) lies entirely in one row or entirely in one column, and each such clique is oriented transitively.

For completeness, the assertion about triangles follows because a vertex outside a given row cannot be adjacent to two distinct vertices in that row.

It remains to show that some choices of the orders have large dichromatic number.

## 3. Counting acyclic orientations

We use an elementary bound.

**Lemma.** If \(G\) is a finite simple graph and \(a(G)\) denotes its number of acyclic orientations, then
\[
a(G)\le \prod_{v\in V(G)}\bigl(d_G(v)+1\bigr).
\]

**Proof.** An acyclic orientation is uniquely determined by its indegree sequence. Indeed, suppose two acyclic orientations have the same indegrees. A source in the first is also a source in the second, so all its incident edges have the same directions. Delete that vertex and continue inductively; the remaining indegrees still agree.

There are at most \(d_G(v)+1\) possible indegrees at each vertex. \(\square\)

Now fix a set \(S\subseteq V(R_n)\) of size \(m\ge1\). Write
\[
r_i=|S\cap(\{i\}\times[n])|,
\qquad
c_j=|S\cap([n]\times\{j\})|.
\]
Thus
\[
\sum_i r_i=\sum_j c_j=m.
\]

The restrictions of our random orders to \(S\) are independent uniform orders. Consequently, the resulting orientations of \(R_n[S]\) are equiprobable, and their number is
\[
Q(S)=\prod_i r_i!\prod_j c_j!.
\]
Here distinct tuples of restricted orders give distinct orientations, since each row or column clique determines its order uniquely. Every acyclic orientation of \(R_n[S]\) occurs among these possibilities, because its restriction to every clique is transitive.

A vertex \((i,j)\in S\) has degree \(r_i+c_j-2\) in \(R_n[S]\). The lemma therefore gives
\[
\Pr(D[S]\text{ is acyclic})
\le
\frac{\displaystyle\prod_{(i,j)\in S}(r_i+c_j-1)}
     {\displaystyle\prod_i r_i!\prod_j c_j!}.
\tag{1}
\]

We next bound this expression uniformly over **all** shapes of \(S\). Using
\[
d!\ge (d/e)^d\qquad(d\ge1),
\]
and omitting zero row and column counts, we obtain
\[
\prod_i r_i!\prod_j c_j!
\ge
e^{-2m}\prod_i r_i^{r_i}\prod_j c_j^{c_j}
=
e^{-2m}\prod_{(i,j)\in S}r_i c_j.
\]
Hence (1) implies
\[
\Pr(D[S]\text{ is acyclic})
\le
e^{2m}
\prod_{(i,j)\in S}
\left(\frac1{r_i}+\frac1{c_j}\right).
\tag{2}
\]

Crucially,
\[
\begin{aligned}
\sum_{(i,j)\in S}\left(\frac1{r_i}+\frac1{c_j}\right)
&=
|\{i:r_i>0\}|+|\{j:c_j>0\}|\\
&\le 2n.
\end{aligned}
\]
Applying arithmetic–geometric mean to (2) yields
\[
\boxed{\displaystyle
\Pr(D[S]\text{ is acyclic})
\le
\left(\frac{2e^2n}{m}\right)^m.}
\tag{3}
\]

No regularity assumption on \(S\) is involved.

## 4. Excluding every large acyclic set

Fix \(k\ge1\), and set
\[
n=64k^2,
\qquad
m=\frac{n^2}{k}=4096k^3.
\]
Both are integers, and \(1\le m\le n^2\).

By the union bound, (3), and the standard estimate
\(\binom{N}{m}\le(eN/m)^m\),
\[
\begin{aligned}
\Pr\bigl(\exists S\subseteq V(R_n),\ |S|=m,\ D[S]\text{ acyclic}\bigr)
&\le
\binom{n^2}{m}
\left(\frac{2e^2n}{m}\right)^m\\
&\le
\left(\frac{2e^3n^3}{m^2}\right)^m\\
&=
\left(\frac{2e^3k^2}{n}\right)^m\\
&=
\left(\frac{e^3}{32}\right)^m
<1.
\end{aligned}
\]
The last inequality follows, for example, from \(e<3\).

Therefore there is a realization \(D_k\) with **no acyclic vertex set of size \(m\)**. Since acyclicity is hereditary, every acyclic vertex set has fewer than \(m\) vertices.

A coloring of \(D_k\) with \(k\) acyclic color classes would have a class of size at least
\[
\frac{|V(D_k)|}{k}=\frac{n^2}{k}=m,
\]
a contradiction. Thus
\[
\vec\chi(D_k)>k.
\]
The graph has
\[
|V(D_k)|=n^2=4096k^4,
\]
and the construction already guarantees the other two properties. This proves the theorem. \(\square\)

### Deterministic specification

The probabilistic proof can also be made into a fully specified, though inefficient, finite construction. Order the tuples of \(2n\) permutations lexicographically, and take the first tuple whose orientation has no acyclic \(m\)-vertex induced subgraph. Test each \(m\)-subset by topological sorting. The estimate above guarantees that this search terminates.

No computational experiment is needed for the proof.

## 5. Contradiction to Conjecture 4.2

For every \(k\), the graph \(D_k\) is
\[
\{\overleftrightarrow{K_2},\vec C_3,S_3^+\}\text{-free},
\]
but \(\vec\chi(D_k)>k\). Consequently,
\[
\boxed{\{\overleftrightarrow{K_2},\vec C_3,S_3^+\}\text{ is not heroic}.}
\]

Nevertheless, \(\vec C_3\) is a hero and \(S_3^+\) is an oriented star. This directly contradicts the claimed “if” direction.

The same construction gives a broader consequence: if \(H\) is any nontransitive tournament and \(F\) is any oriented forest having a vertex of underlying degree at least \(3\), then
\[
\{\overleftrightarrow{K_2},H,F\}
\]
is not heroic. Indeed, every nontransitive tournament contains a directed triangle, and every such forest contains an induced orientation of the claw.

This refutation leaves the **transitive-tournament branch** untouched: our graphs contain arbitrarily large transitive tournaments in their rows.

## 6. Scope and literature caveat

The logical connection left uncertain in the catalogue is direct: claw-free, directed-triangle-free oriented graphs of unbounded dichromatic number refute Conjecture 4.2 with \(H=\vec C_3\) and \(F\) an oriented claw.

The proof above establishes that family independently of any external citation. I have not verified the recent bibliographic claim in the supplied catalogue and make no claim that this construction or argument is new.