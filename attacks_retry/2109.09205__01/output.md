```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An elementary absorption argument extends regularity-free book goodness to exact goodness for bounded-separator, bounded-component targets, with a further transfer for linearly growing bounded-vertex-cover opponents.",
  "would_publish": false,
  "caveats": "The full Nikiforov–Rousseau theorem is not recovered; exact goodness uses the supplied book results, and novelty of these special-case extensions is not claimed."
}
```

# A regularity-free special-case extension

I do not obtain a regularity-free proof of the full Nikiforov–Rousseau theorem. I do, however, remove the additive error in the previous attempt for targets with a bounded separator and bounded remaining components.

The useful change is to **increase the book’s spine, rather than its order**. The additional spine vertices absorb every unused page vertex. A second argument shows that this approach also works when the opposite graph has bounded vertex-cover number and order up to a sufficiently small constant times the target order.

All containment below is ordinary, not induced, containment. The only substantial external input for the explicit \(p\)-goodness conclusion is the Fox–He–Wigderson theorem supplied in the question:
\[
n\ge 2^{k^{10p}}
\quad\Longrightarrow\quad
r(K_p,B_{k,n})=(p-1)(n-1)+1.
\tag{B}
\]

## 1. Absorption using a larger spine

Say that \(H\) has an **\((s,d)\)-separator** if there is a set \(S\subseteq V(H)\), with \(|S|\le s\), such that every component of \(H-S\) has at most \(d\) vertices.

### Lemma 1 — Same-order book transfer

Let \(G\) be a graph having at least one edge, let \(s,d\ge1\), and put
\[
R=r(G,K_d).
\]
Suppose
\[
k\ge s+(d-1)(R-1),\qquad n\ge k.
\tag{1}
\]
Then every \(n\)-vertex graph \(H\) with an \((s,d)\)-separator satisfies
\[
r(G,H)\le r(G,B_{k,n}).
\tag{2}
\]

#### Proof

Consider a red–blue coloring with no red \(G\) and containing a blue \(B_{k,n}\). Write \(X\) for its spine and \(P\) for its pages. Thus:

- \(X\) is a blue clique of order \(k\);
- every edge between \(X\) and \(P\) is blue;
- the coloring inside \(P\) is unrestricted.

Choose an \((s,d)\)-separator \(S\) of \(H\), and write \(s_0=|S|\). Reserve \(s_0\) vertices of \(X\) for \(S\), leaving
\[
a=k-s_0\ge (d-1)(R-1)
\tag{3}
\]
spine vertices.

Let \(Q_1,\ldots,Q_m\) be the components of \(H-S\), with orders \(q_i\le d\). While at least \(R\) unused pages remain, embed an unembedded \(Q_i\) into a blue clique in the unused pages. This is possible because those pages contain a blue \(K_d\); remove only the \(q_i\) vertices actually used.

There cannot be a shortage of unembedded components while unused pages remain: the total number of unembedded vertices outside \(S\) is always \(a\) plus the number of unused pages.

At termination, let \(u<R\) be the number of unused pages. The remaining components have total order \(a+u\). If their number is \(\ell\), then
\[
d\ell\ge a+u\ge (d-1)u+u=du,
\]
so \(\ell\ge u\).

Assign each unused page to one vertex in a different remaining component. Map all other vertices of those components bijectively to the \(a\) unused spine vertices. This works because each such component uses at most one page vertex: every required edge within it is either inside the blue spine or between spine and page.

Finally, map \(H[S]\) into the reserved spine vertices. Every required edge incident with \(S\) is blue, and there are no required edges between distinct components of \(H-S\). We have embedded a blue \(H\). ∎

This does not assert that \(H\) is a subgraph of the uncolored book \(B_{k,n}\). The proof also uses blue edges among the pages of the ambient coloring.

## 2. Exact \(p\)-goodness for bounded-component separators

### Theorem 2 — Explicit regularity-free goodness

Let \(p\ge2\) and \(s,d\ge1\). Define
\[
R_{p,d}=r(K_p,K_d),\qquad
k=s+(d-1)(R_{p,d}-1).
\tag{4}
\]
Every connected \(n\)-vertex graph \(H\) having an \((s,d)\)-separator is \(p\)-good whenever
\[
n\ge 2^{k^{10p}}.
\tag{5}
\]
In other words,
\[
r(K_p,H)=(p-1)(n-1)+1.
\tag{6}
\]

#### Proof

Lemma 1 and (B) give
\[
r(K_p,H)\le r(K_p,B_{k,n})
=(p-1)(n-1)+1.
\]

For the reverse inequality, partition \((p-1)(n-1)\) vertices into \(p-1\) sets of size \(n-1\), color all within-set edges blue and all cross-edges red. There is no red \(K_p\). Every blue component has fewer than \(n\) vertices, so there is no blue copy of the connected graph \(H\). ∎

### Fully explicit parameters

The elementary clique-Ramsey bound
\[
r(K_a,K_b)\le \binom{a+b-2}{a-1}
\tag{7}
\]
follows from the usual Ramsey recurrence. Consequently, in Theorem 2 one may replace \(k\) by
\[
\widehat k
=
s+(d-1)\left(\binom{p+d-2}{p-1}-1\right).
\tag{8}
\]

Thus a sufficient condition, allowing \(s,d\) to grow with \(n\), is
\[
s+(d-1)\left(\binom{p+d-2}{p-1}-1\right)
\le (\log_2 n)^{1/(10p)}.
\tag{9}
\]
For fixed \(p\), the left side is \(O_p(s+d^p)\).

The case \(d=1\) recovers the bounded-vertex-cover consequence of the book theorem. The new point is that \(d>1\) incurs **no additive error in the Ramsey number**.

For example, for any fixed nonempty graphs \(F,J\), every sufficiently large graph
\[
H_t=F\vee(tJ)
\]
is \(p\)-good by this argument: take \(S=V(F)\) and \(d=|V(J)|\). The same conclusion holds for arbitrary mixtures of bounded components attached to a bounded separator, with arbitrary attachment patterns.

## 3. Keeping the spine bounded when the red graph grows

Applying Lemma 1 directly to a growing graph \(G\) can require a growing spine, because \(r(G,K_d)\) grows with \(v(G)\). The following packing argument avoids that problem when \(G\) has bounded vertex-cover number.

Write \(\tau(G)\) for the vertex-cover number of \(G\).

Fix \(A\ge1\) and \(d\ge2\), and define constants
\[
\begin{aligned}
R_*&=r(K_{A+1},K_d),\\
D&=\binom{R_*}{A+1},\\
\lambda&=\max\{R_*,D\},\\
L&=Ad,\\
T&=r(K_L,K_d),\\
C&=(d+1)\lambda+d\binom LA.
\end{aligned}
\tag{10}
\]
All these constants depend only on \(A,d\). They can be bounded explicitly using (7), without regularity.

### Lemma 3 — A linear Ramsey bound

If \(G\) has \(g\) vertices and \(\tau(G)\le A\), then
\[
r(G,K_d)\le \lambda g.
\tag{11}
\]

#### Proof

If \(g<A\), then \(G\subseteq K_{A+1}\), so the assertion follows immediately.

Suppose \(g\ge A\). Enlarging a vertex cover to size \(A\) shows that
\[
G\subseteq B_{A,g}.
\tag{12}
\]
Indeed, map the cover into the spine; all remaining vertices form an independent set in \(G\).

Set
\[
N=\max\{R_*,\,A+D(g-A)\}.
\]
Consider a coloring of \(K_N\) with no blue \(K_d\). Every \(R_*\)-vertex set contains a red \(K_{A+1}\). If \(t_{A+1}\) denotes the number of these red cliques, double-counting gives
\[
t_{A+1}\ge
\frac{\binom N{A+1}}{\binom{R_*}{A+1}}
=\frac{\binom N{A+1}}D.
\tag{13}
\]

Summing common red-neighborhood sizes over all red \(K_A\)'s counts each red \(K_{A+1}\) exactly \(A+1\) times. Thus some red \(K_A\) has at least
\[
\frac{(A+1)t_{A+1}}{\binom NA}
\ge \frac{N-A}{D}
\ge g-A
\tag{14}
\]
common red neighbors. This gives a red \(B_{A,g}\), hence a red \(G\).

Finally,
\[
A+D(g-A)\le Dg,\qquad R_*\le R_*g,
\]
so \(N\le\lambda g\). ∎

### Lemma 4 — Prescribed clique packing with constant remainder

Let \(G\) have \(g\) vertices and \(\tau(G)\le A\). Consider a red–blue coloring on \(M\) vertices with no red \(G\), where
\[
M\ge Cg.
\tag{15}
\]
Let \(q_1,\ldots,q_m\) be positive integers satisfying
\[
q_i\le d,\qquad \sum_i q_i\ge M.
\tag{16}
\]
Then one can choose some distinct indices \(i\) and vertex-disjoint blue cliques of their prescribed orders \(q_i\), leaving fewer than \(T\) vertices uncovered.

#### Proof

Choose such a packing maximizing the number of covered vertices, and let \(U\) be the uncovered set.

Suppose for a contradiction that \(|U|\ge T\). Not all prescribed indices have been used: otherwise (16) would force every vertex to be covered. Choose an unused index of order \(q\le d\).

Maximality implies that \(U\) contains no blue \(K_q\). By Lemma 3,
\[
|U|<r(G,K_q)\le r(G,K_d)\le\lambda g.
\tag{17}
\]
In particular, \(U\) contains no blue \(K_d\). Since \(|U|\ge T\), it contains a red clique \(I\) of order
\[
|I|=L=Ad.
\]
If \(g\le L\), this clique already contains \(G\), a contradiction. Hence assume \(g>L\).

Call a packed clique \(Q\) **bad** if some vertex of \(Q\) has at least \(A\) red neighbors in \(I\), and **good** otherwise.

**Good cliques.** For a good clique \(Q\), each of its at most \(d\) vertices has at most \(A-1\) red neighbors in \(I\). Consequently at least
\[
L-d(A-1)=d
\tag{18}
\]
vertices of \(I\) are blue-adjacent to every vertex of \(Q\).

Choose one representative vertex from each good clique. If there were at least \(r(G,K_q)\) good cliques, their representatives would contain a blue \(K_q\). Let its vertices come from \(Q_1,\ldots,Q_q\).

By (18), choose distinct vertices \(u_1,\ldots,u_q\in I\), with \(u_j\) blue-complete to \(Q_j\). In each \(Q_j\), replace its representative by \(u_j\). The removed representatives form a new blue \(K_q\), realizing the unused prescribed index. All old prescribed orders remain realized, and the packing covers \(q\) additional vertices. This contradicts maximality.

Therefore
\[
\#\{\text{good cliques}\}<r(G,K_q)\le\lambda g.
\tag{19}
\]

**Bad cliques.** For each bad clique \(Q\), choose a vertex \(v_Q\in Q\) and an \(A\)-element set \(X_Q\subseteq I\) to which \(v_Q\) is red-complete. For any fixed \(X\subseteq I\) of order \(A\), fewer than \(g-A\) chosen vertices can correspond to \(X\): otherwise \(X\), together with those vertices, gives a red \(B_{A,g}\), and hence a red \(G\). Thus
\[
\#\{\text{bad cliques}\}
\le \binom LA(g-A-1)
<\binom LA g.
\tag{20}
\]

Every packed clique has at most \(d\) vertices. Combining (17), (19), and (20),
\[
\begin{aligned}
M
&=|U|+\sum_{\text{packed }Q}|Q|\\
&<\lambda g+d\left(\lambda g+\binom LA g\right)\\
&=Cg,
\end{aligned}
\]
contrary to (15). Hence \(|U|<T\). ∎

The packing need not be found efficiently for this proof: a maximum packing exists because the host graph is finite. No counting, removal, or regularity theorem is hidden in the argument.

## 4. A same-order transfer for linear-sized bounded-cover opponents

### Theorem 5

Fix \(A,s\ge1\) and \(d\ge2\), and use the constants \(T,C\) from (10). Put
\[
k=s+(d-1)(T-1).
\tag{21}
\]
Let \(G\) have \(g\) vertices and \(\tau(G)\le A\). Let \(H\) have \(n\) vertices and an \((s,d)\)-separator. If
\[
n-k\ge Cg,
\tag{22}
\]
then
\[
r(G,H)\le r(G,B_{k,n}).
\tag{23}
\]

#### Proof

Take a coloring with no red \(G\) and a blue \(B_{k,n}\), with spine \(X\) and page set \(P\). Choose a separator \(S\) of order \(s_0\le s\), reserve \(s_0\) spine vertices for it, and put
\[
a=k-s_0\ge(d-1)(T-1).
\]

List the orders \(q_i\le d\) of the components of \(H-S\). Their sum is
\[
n-s_0=|P|+a\ge |P|.
\]
By (22), Lemma 4 applies to the coloring on \(P\). Embed the selected components into its prescribed blue cliques. Fewer than \(T\) page vertices remain unused; write their number as \(u\).

The unembedded components have total order \(a+u\), and their number \(\ell\) satisfies
\[
d\ell\ge a+u\ge du.
\]
Assign the \(u\) unused pages to distinct remaining components, one vertex per component. Embed every other unembedded vertex outside \(S\) in the remaining spine. As in Lemma 1, all required edges are blue. ∎

For \(d=1\), the simpler assertion follows directly from
\[
H\subseteq B_{s,n},
\]
without condition (22).

### Consequence for exact book equalities

Let \(\chi(G)=p\), and let \(\sigma(G)\) denote the smallest color-class size appearing in a proper \(p\)-coloring of \(G\). Under the hypotheses of Theorem 5, if a regularity-free book result gives
\[
r(G,B_{k,n})=(p-1)(n-1)+\sigma(G),
\tag{24}
\]
then every connected target \(H\) in Theorem 5 satisfies
\[
r(G,H)=(p-1)(n-1)+\sigma(G).
\tag{25}
\]

The upper bound is Theorem 5. For the lower bound, take \(p-1\) blue cliques of order \(n-1\) and one of order \(\sigma(G)-1\), with every cross-edge red. There is no blue connected \(n\)-vertex graph. A red copy of \(G\) would induce a proper \(p\)-coloring with a class smaller than \(\sigma(G)\), which is impossible. Here \(\sigma(G)\le n\) follows from (22).

This transfer remains applicable when \(g\) grows linearly with \(n\): it suffices to require
\[
g\le \frac{n}{2C},\qquad n\ge2k.
\tag{26}
\]
In particular, the complete multipartite opponents described in the question have bounded vertex cover when the first \(p-1\) parts have fixed total size. In every parameter range where their regularity-free book equality is available, Theorem 5 transfers that equality to the present target class after decreasing the allowed linear-size constant.

This last statement does **not** assert a book equality for every bounded-cover graph \(G\); such an assertion would be false. It transfers book equalities already established for particular opponent families.

## 5. What this resolves, and what remains

The previous attempt’s additive-constant bound is unnecessary for \((s,d)\)-separator targets. Its page-only packing leaves a constant remainder, but increasing the spine by a suitable constant lets every remaining page participate in the embedding. The order of the book stays exactly \(n\), preserving the sharp Ramsey bound.

The proved conclusions are:

1. **Exact \(p\)-goodness**, with explicit regularity-free bounds, for all connected targets with a bounded separator and bounded remaining components.
2. A quantitative version permitting slowly growing separator and component bounds, as in (9).
3. A same-order book transfer that still works for opponents of bounded vertex-cover number and sufficiently small linear order.

The gap to the catalog question is scope. These arguments do not supply an embedding theorem for all targets allowed by the full Nikiforov–Rousseau theorem. In particular, the fixed-spine argument is not uniform when the separator or remaining component sizes grow beyond the displayed bounds, and the stronger packing argument assumes bounded vertex-cover number on the opposite side.

Thus this is a proved regularity-free special-case extension, not a complete elimination of regularity from Nikiforov–Rousseau Theorem 2.1. I have not verified whether this extension already appears elsewhere in the literature.