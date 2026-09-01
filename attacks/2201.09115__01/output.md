```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The universal conjecture is not resolved, but it holds sharply for s=1 and s=2, for the pair (3,3), and for chordal and complete multipartite graphs.",
  "would_publish": false,
  "caveats": "The arguments do not cover arbitrary graphs for s>=3 beyond (3,3), and the special cases are likely standard."
}
```

# 1. Statement

Write \(H\preceq G\) when \(H\) is a minor of \(G\). The question is whether, for every \(1\le s\le t\),
\[
K_{s,t}\npreceq G\quad\Longrightarrow\quad \chi_\ell(G)\le 2s+t.
\]

I do not obtain the general bound. I prove substantially stronger bounds for \(s\le2\), settle \((s,t)=(3,3)\), and give some structural restrictions on any counterexample.

Recall that a \(d\)-degenerate graph is \((d+1)\)-choosable.

# 2. The cases \(s=1\) and \(s=2\)

## Lemma 2.1

For every integer \(r\ge1\), every graph of minimum degree at least \(r+1\) contains a \(K_{2,r}\)-minor.

### Proof

Let
\[
P=v_0v_1\cdots v_m
\]
be a longest induced path. Since \(P\) is induced, \(v_0\) has only one neighbor on \(P\), namely \(v_1\). Thus \(v_0\) has at least \(r\) neighbors
\[
x_1,\dots,x_r\notin V(P).
\]

For each \(i\), the vertex \(x_i\) has another neighbor on \(P-v_0\). Otherwise
\[
x_i v_0v_1\cdots v_m
\]
would be a longer induced path.

Now take the following branch sets:
\[
\{v_0\},\qquad V(P)\setminus\{v_0\},\qquad \{x_1\},\dots,\{x_r\}.
\]
The first two are connected and disjoint. Each \(x_i\) is adjacent both to \(v_0\) and to \(P-v_0\). These branch sets therefore form a \(K_{2,r}\)-minor model. ∎

Equivalently, every graph of minimum degree \(\delta\ge2\) contains \(K_{2,\delta-1}\) as a minor.

## Theorem 2.2

For every \(t\ge1\),
\[
\max\{\chi_\ell(G):K_{1,t}\npreceq G\}=t.
\]

### Proof

If a graph has a vertex of degree at least \(t\), then it contains \(K_{1,t}\) as a subgraph. Hence a \(K_{1,t}\)-minor-free graph has maximum degree at most \(t-1\) and is \(t\)-choosable.

The complete graph \(K_t\) has list chromatic number \(t\), and it cannot contain \(K_{1,t}\), which has \(t+1\) vertices, as a minor. ∎

## Theorem 2.3

For every \(t\ge2\),
\[
\max\{\chi_\ell(G):K_{2,t}\npreceq G\}=t+1.
\]

### Proof

Every subgraph of a \(K_{2,t}\)-minor-free graph is again \(K_{2,t}\)-minor-free. By Lemma 2.1, no such subgraph can have minimum degree at least \(t+1\). Hence every \(K_{2,t}\)-minor-free graph is \(t\)-degenerate, and therefore
\[
\chi_\ell(G)\le t+1.
\]

This is sharp: \(K_{t+1}\) has list chromatic number \(t+1\), while it has fewer than the \(t+2\) vertices needed for a \(K_{2,t}\)-minor model. ∎

Thus the proposed inequality holds with considerable room for \(s=1,2\):
\[
\chi_\ell(G)\le
\begin{cases}
t,&s=1,\\
t+1,&s=2.
\end{cases}
\]

# 3. The pair \((s,t)=(3,3)\)

I use the standard extremal consequence of Wagner's decomposition:

> Every simple \(n\)-vertex graph with \(n\ge2\) and no \(K_{3,3}\)-minor has at most \(3n-5\) edges.

This follows from the characterization of \(K_{3,3}\)-minor-free graphs by \(0\)-, \(1\)-, and \(2\)-sums of planar graphs and copies of \(K_5\).

Every subgraph \(H\) of a \(K_{3,3}\)-minor-free graph is also \(K_{3,3}\)-minor-free. If \(|V(H)|\ge2\), then
\[
\frac{2|E(H)|}{|V(H)|}
   \le 6-\frac{10}{|V(H)|}<6.
\]
Thus \(H\) has a vertex of degree at most \(5\). Consequently:

## Proposition 3.1

Every \(K_{3,3}\)-minor-free graph is \(5\)-degenerate and hence \(6\)-choosable.

In particular,
\[
\chi_\ell(G)\le6<9=2\cdot3+3.
\]

# 4. Two broad restricted classes

## 4.1 Chordal graphs

## Proposition 4.1

If \(G\) is chordal and \(K_{s,t}\npreceq G\), then
\[
\chi_\ell(G)\le s+t-1.
\]

### Proof

A chordal graph has a perfect elimination ordering, so it is \(\omega(G)\)-choosable by greedy list coloring. If \(\omega(G)\ge s+t\), then \(G\) contains \(K_{s+t}\), and hence \(K_{s,t}\), as a subgraph. Therefore
\[
\omega(G)\le s+t-1.
\]
The bound is sharp within chordal graphs, as witnessed by \(K_{s+t-1}\). ∎

Thus Woodall's original stronger bound holds for chordal graphs.

## 4.2 Complete multipartite graphs

## Proposition 4.2

If \(G\) is complete multipartite and \(K_{s,t}\npreceq G\), then
\[
\chi_\ell(G)\le 2s+t-1.
\]

### Proof

Let \(n=|V(G)|\), let \(\alpha\) be the size of a largest part, and put \(q=n-\alpha\).

First observe that if
\[
n\ge 2s+t\quad\text{and}\quad q\ge s,
\]
then \(G\) contains a \(K_{s,t}\)-minor. Indeed, under \(n\ge2s\) and \(q\ge s\), a complete multipartite graph has a matching of size \(s\). Let its edges be \(e_1,\dots,e_s\). At least \(t\) vertices remain outside these edges.

Every edge of a complete multipartite graph is a dominating connected set: if its endpoints lie in two different parts, every other vertex is adjacent to at least one endpoint. Hence the \(s\) edge-branch-sets \(e_i\), together with any \(t\) remaining singleton branch sets, form a \(K_{s,t}\)-minor.

It follows that a \(K_{s,t}\)-minor-free complete multipartite graph satisfies one of:

1. \(n\le2s+t-1\), in which case
   \[
   \chi_\ell(G)\le n\le2s+t-1;
   \]
2. \(q\le s-1\).

In the second case, order the vertices of a largest part first. Each has at most \(q\) later neighbors, and after that at most \(q-1\) vertices remain. Thus \(G\) is \(q\)-degenerate and
\[
\chi_\ell(G)\le q+1\le s.
\]
This proves the assertion. ∎

# 5. A finite-order result

Put
\[
k=2s+t.
\]

## Lemma 5.1

Let \(s\ge2\), and suppose a graph \(G\) has
\[
|V(G)|=k+r,\qquad \delta(G)\ge k.
\]
If
\[
r(s-1)\le2s,
\]
then \(G\) contains \(K_{s,t}\) as a subgraph.

### Proof

In the complement \(\overline G\),
\[
\Delta(\overline G)\le |V(G)|-1-k=r-1.
\]
Fix any set \(A\) of \(s\) vertices. The number of vertices outside \(A\) that fail to be adjacent in \(G\) to at least one member of \(A\) is at most \(s(r-1)\). Hence the number of vertices adjacent to every member of \(A\) is at least
\[
(k+r)-s-s(r-1)
 =t+2s-r(s-1)
 \ge t.
\]
Choosing \(t\) such vertices gives a \(K_{s,t}\)-subgraph. ∎

Define
\[
R_s=\left\lfloor\frac{2s}{s-1}\right\rfloor
=
\begin{cases}
4,&s=2,\\
3,&s=3,\\
2,&s\ge4.
\end{cases}
\]

## Corollary 5.2

Every \(K_{s,t}\)-minor-free graph \(G\) with
\[
|V(G)|\le 2s+t+R_s
\]
is \((2s+t-1)\)-degenerate and hence \((2s+t)\)-choosable.

### Proof

If some subgraph \(H\subseteq G\) had minimum degree at least \(k\), then
\[
|V(H)|=k+r
\]
for some \(1\le r\le R_s\). Lemma 5.1 would give a \(K_{s,t}\)-subgraph of \(H\), a contradiction. ∎

Thus a counterexample with \(s=3\) would need at least \(2s+t+4=t+10\) vertices; for \(s\ge4\), it would need at least \(2s+t+3\) vertices.

# 6. Structure of a minimal counterexample

Suppose the conjecture fails, set \(k=2s+t\), and choose an uncolorable \(k\)-list assignment on a vertex-minimal graph \(H\).

Then:

1. \(H\) is connected.
2. \(\delta(H)\ge k\).  
   Indeed, color \(H-v\). If \(d_H(v)\le k-1\), at most \(k-1\) colors are forbidden at \(v\), so the coloring extends.
3. By Theorems 2.2 and 2.3 and Proposition 3.1, necessarily
   \[
   s\ge3,\qquad (s,t)\ne(3,3).
   \]

There is also a useful recursive local restriction.

## Lemma 6.1

Let \(s\ge3\), let \(G\) be \(K_{s,t}\)-minor-free, and let
\[
P=v_0v_1\cdots v_m
\]
be a longest induced path. Put
\[
X=N_G(v_0)\setminus V(P).
\]
Then
\[
K_{s-2,t}\npreceq G[X].
\]

### Proof

As in Lemma 2.1, every \(x\in X\) has a neighbor in \(P-v_0\).

Suppose \(G[X]\) contained a \(K_{s-2,t}\)-minor. Add the two connected branch sets
\[
\{v_0\},\qquad V(P)\setminus\{v_0\}
\]
to its side of size \(s-2\). Every branch set on the side of size \(t\) lies in \(X\), and hence is adjacent both to \(v_0\) and to \(P-v_0\). This produces a \(K_{s,t}\)-minor in \(G\), a contradiction. ∎

For a minimal counterexample, \(v_0\) has only one neighbor on \(P\), so
\[
|X|\ge\delta(H)-1\ge2s+t-1.
\]
Nevertheless \(G[X]\) excludes the smaller minor \(K_{s-2,t}\). In particular:

- if \(s=3\), then \(G[X]\) is \(K_{1,t}\)-minor-free, so it has maximum degree at most \(t-1\);
- if \(s=4\), then \(G[X]\) is \(K_{2,t}\)-minor-free, so it is \(t\)-degenerate.

This gives a fairly rigid local picture, but it does not yet yield a global list coloring.

# 7. Remaining gap

For \(s=2\), the longest-induced-path argument constructs both branch sets on the side of size \(2\), and the minimum-degree condition finishes the problem.

For \(s\ge3\), the same argument only constructs two universally adjacent branch sets. Completing them to \(s\) branch sets would require a suitable \(K_{s-2,t}\)-minor inside the large set \(X\); Lemma 6.1 says precisely that this minor is absent. Large cardinality of \(X\) alone gives no useful list-chromatic or minimum-degree lower bound inside \(X\).

Thus the central unresolved step is to exploit the full critical list assignment, rather than only its consequence \(\delta(H)\ge2s+t\). No such argument is supplied here, so the universal conjecture remains unresolved.