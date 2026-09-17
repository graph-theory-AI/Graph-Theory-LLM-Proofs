```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The Janzer–Sudakov regular-subgraph theorem implies that constant multitasking capacity forces average degree O_alpha(log log n), ruling out the proposed logarithmic degree.",
  "would_publish": false,
  "caveats": "Uses an established regular-subgraph theorem as an external input; I have not checked whether this multitasking corollary was previously stated explicitly."
}
```

## 1. Statement

The decisive input is the **Janzer–Sudakov regular-subgraph theorem**, resolving the Erdős–Sauer regular-subgraph problem. Its density threshold is sufficiently strong to answer the question negatively.

In fact, we obtain the following.

**Theorem.** For every fixed \(\alpha>0\), there is a constant \(C_\alpha\) such that every sufficiently large bipartite \(\alpha\)-multitasker \(G=(A\cup B,E)\), with \(|A|=|B|=n\), satisfies
\[
d(G)=\frac{|E|}{n}\le C_\alpha\log\log n.
\]

Consequently, there is no family of multitaskers having both
\[
d(G)=\Theta(\log n)
\qquad\text{and}\qquad
\operatorname{mt}(G)\ge\alpha_0>0
\]
for a fixed \(\alpha_0\).

Taking the lower-bound construction supplied in the question as given, the largest possible average-degree **order of growth** for constant positive multitasking capacity is therefore \(\Theta(\log\log n)\).

The argument does not use the earlier attempt’s endpoint analysis.

## 2. The external regular-subgraph theorem

We use the following established theorem, in a weaker form than its quantitative statement.

**Regular-subgraph theorem — Janzer–Sudakov.** For every fixed integer \(r\ge3\), there exists a constant \(K_r\) such that every sufficiently large \(N\)-vertex graph of average degree at least
\[
K_r\log\log N
\]
contains a nonempty \(r\)-regular subgraph.

The subgraph is not required to be induced. That causes no difficulty here.

I use this named theorem as an external input; I do not assert an unchecked arXiv identifier or publication citation. The other outside input below is the classical van der Waerden permanent bound.

## 3. Multitasking capacity is monotone under taking subgraphs

For a matching \(M\) in \(G\), write
\[
\operatorname{im}_G(M)
=\max\{|I|:I\subseteq M,\ I\text{ is induced in }G\},
\]
and define
\[
\operatorname{mt}(G)
=\min_{\varnothing\ne M\text{ a matching in }G}
\frac{\operatorname{im}_G(M)}{|M|}.
\]

If \(H\) is any subgraph of \(G\), every matching of \(H\) is also a matching of \(G\). Moreover, an induced matching in \(G\) whose edges belong to \(H\) remains induced in \(H\). Thus
\[
\operatorname{mt}(G)\ge\alpha
\quad\Longrightarrow\quad
\operatorname{mt}(H)\ge\alpha.                         \tag{1}
\]

Equivalently,
\[
\operatorname{mt}(G)\le\operatorname{mt}(H).
\]

We will combine this observation with an elementary counting obstruction for regular bipartite graphs.

## 4. Regular bipartite graphs cannot have uniformly positive capacity as their degree grows

The following relatively weak bound suffices; sharper regular-graph bounds are unnecessary.

**Lemma.** If \(H\) is a nonempty \(r\)-regular bipartite graph, \(r\ge2\), then
\[
\operatorname{mt}(H)\le
\frac{\log(4e)}{\log r}.                              \tag{2}
\]

### Proof

Write the bipartition of \(H\) as \(X\cup Y\). Regularity and double-counting edges give
\[
|X|=|Y|=:q.
\]

Let \(P(H)\) denote the number of perfect matchings of \(H\). Dividing its bipartite adjacency matrix by \(r\) gives a doubly stochastic matrix. The van der Waerden permanent bound therefore yields
\[
P(H)\ge r^q\frac{q!}{q^q}
      \ge \left(\frac re\right)^q.                    \tag{3}
\]

Suppose \(H\) is a \(\beta\)-multitasker, and put
\[
k=\lceil\beta q\rceil.
\]
Every perfect matching of \(H\) contains an induced submatching of size \(k\).

There are at most
\[
\binom qk^2
\]
induced matchings of size \(k\): their two endpoint sets determine them uniquely. Indeed, if those endpoint sets support an induced matching, the entire graph between them consists precisely of its \(k\) edges.

A fixed induced matching of size \(k\) extends to at most
\[
r^{q-k}
\]
perfect matchings. To see this, assign a neighbor to each of the remaining \(q-k\) vertices of \(X\), ignoring the restrictions that these choices must be distinct and avoid the already occupied vertices.

Counting perfect matchings through their induced \(k\)-edge submatchings gives
\[
P(H)\le \binom qk^2r^{q-k}
     \le 4^q r^{q-k}.                                 \tag{4}
\]
Combining (3) and (4),
\[
\left(\frac re\right)^q\le4^q r^{q-k},
\]
and hence
\[
r^k\le(4e)^q.
\]
Therefore
\[
\beta\le\frac{k}{q}
      \le\frac{\log(4e)}{\log r}.
\]
Taking \(\beta=\operatorname{mt}(H)\) proves the lemma. \(\square\)

In particular, for every \(\alpha>0\), there is a fixed integer \(r\) such that **no \(r\)-regular bipartite graph is an \(\alpha\)-multitasker**.

## 5. Applying the regular-subgraph theorem

Fix \(0<\alpha\le1\), and choose an integer
\[
r\ge3
\quad\text{with}\quad
\log r\ge \frac{2\log(4e)}{\alpha}.
\]
By the lemma, every nonempty \(r\)-regular bipartite graph \(H\) satisfies
\[
\operatorname{mt}(H)\le\frac{\alpha}{2}<\alpha.         \tag{5}
\]

Now let \(G\) be an \(\alpha\)-multitasker on \(2n\) vertices. If
\[
d(G)\ge K_r\log\log(2n)
\]
and \(n\) is sufficiently large, the regular-subgraph theorem supplies a nonempty \(r\)-regular subgraph \(H\subseteq G\).

Because \(G\) is bipartite, so is \(H\). By the subgraph monotonicity (1), \(H\) must also be an \(\alpha\)-multitasker. This contradicts (5).

Thus
\[
d(G)<K_r\log\log(2n)
     =O_\alpha(\log\log n),
\]
as claimed. \(\square\)

An equivalent asymptotic formulation is
\[
\frac{d(G_n)}{\log\log n}\longrightarrow\infty
\quad\Longrightarrow\quad
\operatorname{mt}(G_n)\longrightarrow0.
\]

Since \(\log n/\log\log n\to\infty\), this directly excludes the proposed \(\Theta(\log n)\) construction.

## 6. Status and dependencies

The supplied review focuses on subsequent multitasking papers. The relevant additional development is instead the regular-subgraph theorem: sufficiently large average degree on the \(\log\log n\) scale forces regular subgraphs of any prescribed fixed degree.

The reduction above covers every fixed \(\alpha>0\), not merely \(\alpha\ge1/2\). It uses:

1. the established Janzer–Sudakov regular-subgraph theorem;
2. the classical van der Waerden permanent bound;
3. the elementary counting and monotonicity arguments proved above.

No unproved conjecture is substituted for the multitasking question. I have not checked whether this particular consequence is explicitly recorded in the multitasking literature, and make no novelty claim.