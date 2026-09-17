Attack the following open graph-theory problem.

Catalog id: list_chromatic_number_and_maximum_degree_of_bipartite_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_chromatic_number_and_maximum_degree_of_bipartite_graphs/
Original entry: http://www.openproblemgarden.org/op/list_chromatic_number_and_maximum_degree_of_bipartite_graphs
Problem attributed to: Alon, Noga (posted 2013-03-12)

=== Problem statement (OpenProblemGarden) ===
Title: List chromatic number and maximum degree of bipartite graphs
Conjecture There is a constant $ c $ such that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ c \log \Delta $ .

=== Discussion / context (OpenProblemGarden) ===
For definitions and an introduction to list colouring, see the related Wikipedia page . Alon [A] showed that the list chromatic number of a graph (not necessarily bipartite) of maximum degree $ \Delta $ is at least $ \frac{1}{2}(1-o(1))\log_2\Delta $ . Random bipartite graphs show that this is tight up to a multiplicative factor $ (2+o(1)) $ . It is not diffcult to see that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ O(\Delta/\log \Delta) $ . It also follows a more general result of Johansson [J] on triangle-free graphs.

=== References listed by OpenProblemGarden ===
- *[A] N. Alon, Degrees and choice numbers, Random Structures Algorithms, 16 (2000), 364--368.
- [AK] N. Alon and M. Krivelevich, The choice number of random bipartite graphs, Annals of Combi- natorics 2 (1998), 291-297.
- [J] A. Johansson. Asymptotic choice number for triangle free graphs. Technical Report 91–95, DIMACS, 1996.

=== Catalog page (statement + literature review) ===
List chromatic number and maximum degree of bipartite graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Alon's conjecture that the list chromatic number of any bipartite graph of maximum degree $\Delta$ is at most $c\log\Delta$ remains open. The best known upper bound has been improved from $(1+o(1))\Delta/\log\Delta$ (Johansson's triangle-free bound) to $(4/5-\varepsilon)\Delta/\log\Delta$ for bipartite graphs specifically (Bradshaw, Mohar, Stacho 2024), but this is still $\Theta(\Delta/\log\Delta)$ rather than the conjectured $O(\log\Delta)$. Partial asymmetric progress was also made by Alon, Cambie, and Kang (2021), showing that in a bipartite graph with equal maximum degree $\Delta$ on both sides, one side can be coloured from lists of size $\log\Delta$ provided the other side uses lists of size $(1+o(1))\Delta/\log\Delta$.

 Cited literature (4)

 
 
 
partial Asymmetric list sizes in bipartite graphs
 (2021)
 

 
 Noga Alon, Stijn Cambie, Ross J. Kang · Annals of Combinatorics · arXiv:2004.07457 · doi:10.1007/s00026-021-00552-5

Proves that in a bipartite graph with $\Delta_A=\Delta_B=\Delta$, one part can be assigned lists of size $\log\Delta$ and the other $(1+o(1))\Delta/\log\Delta$ and a proper list colouring is guaranteed, giving asymmetric partial progress toward the Alon-Krivelevich conjecture.
 

 
 
partial Bipartite graphs are $(\frac{4}{5}-\varepsilon) \frac{\Delta}{\log \Delta}$-choosable
 (2024)
 

 
 Peter Bradshaw, Bojan Mohar, Ladislav Stacho · arXiv preprint · arXiv:2409.01513

Proves that every bipartite graph of sufficiently large maximum degree $\Delta$ satisfies $\chi_\ell(G) < (4/5-\varepsilon)\Delta/\log\Delta$ for $\varepsilon=10^{-3}$, improving Johansson's triangle-free bound and showing list colouring is fundamentally easier for bipartite graphs, but still far from the conjectured $O(\log\Delta)$.
 

 
 
partial Asymmetric list sizes in bipartite graphs
 (2021)
 

 
 Noga Alon, Stijn Cambie, Ross J. Kang · arXiv preprint · arXiv:2004.07457

Proves Corollary 10: for any $\varepsilon > 0$ and $\Delta$ large enough, every bipartite graph with maximum degree at most $\Delta$ is $((1+\varepsilon)\Delta/\log^4\Delta,\,2)$- and $((1+\varepsilon)\Delta/\log\Delta,\,\log\Delta)$-choosable, constituting the first asymmetric progress toward the conjecture.
 

 
 
partial Bipartite graphs are $(\frac{4}{5}-\varepsilon) \fracΔ{\log Δ}$-choosable
 (2024)
 

 
 Peter Bradshaw, Bojan Mohar, Ladislav Stacho · arXiv preprint · arXiv:2409.01513

Proves that every bipartite graph $G$ of sufficiently large maximum degree $\Delta$ satisfies $\operatorname{ch}(G)<(\frac{4}{5}-\varepsilon)\frac{\Delta}{\log\Delta}$ for $\varepsilon=10^{-3}$, giving the first upper bound with leading constant strictly less than $1$ and showing that list coloring behaves fundamentally differently for bipartite graphs than for general triangle-free graphs.
 

 

 Reviewer notes. The Zhu (2023) paper on 'semi-small list size' for complete bipartite graphs was verified but focuses on asymmetric list sizes in complete bipartite graphs rather than the original conjecture, so it was omitted from since_posted. The conjecture's gap remains very large: the upper bound is $\Theta(\Delta/\log\Delta)$ and the lower bound from random bipartite graphs is $\Omega(\log\Delta)$. The 2024 Bradshaw-Mohar-Stacho paper is an arXiv preprint as of the review date; journal publication status unknown.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. There is a constant $ c $ such that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ c \log \Delta $ .

Discussion

For definitions and an introduction to list colouring, see the related Wikipedia page . Alon [A] showed that the list chromatic number of a graph (not necessarily bipartite) of maximum degree $ \Delta $ is at least $ \frac{1}{2}(1-o(1))\log_2\Delta $ . Random bipartite graphs show that this is tight up to a multiplicative factor $ (2+o(1)) $ . It is not diffcult to see that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ O(\Delta/\log \Delta) $ . It also follows a more general result of Johansson [J] on triangle-free graphs.

Bibliography

★ [A]
 N. Alon, Degrees and choice numbers , Random Structures Algorithms, 16 (2000), 364--368.
 Degrees and choice numbers

 [AK]
 N. Alon and M. Krivelevich, The choice number of random bipartite graphs, Annals of Combi- natorics 2 (1998), 291-297.

 [J]
 A. Johansson. Asymptotic choice number for triangle free graphs. Technical Report 91–95, DIMACS, 1996.

Related conjectures

 
 implied by
 Asymmetric Krivelevich–Alon choosability for bipartite graphs
 open
 Take any bipartite G with maximum degree Delta; both parts then have maximum degree at most Delta, so apply the source's case (ii) with Delta_A = Delta_B = Delta and k_A = k_B = ceil(C log Delta), which satisfies k_A >= C log Delta_B and k_B >= C log Delta_A. The conclusion is that G is (k, k)-choosable with k = ceil(C log Delta), and (k,k)-choosability (both parts get lists of size k) is exactly k-choosability, so chi_l(G) <= C log Delta + 1 = O(log Delta) — the Alon (Krivelevich–Alon) conjecture. The source's own context confirms the hypothesis-strength ordering: 'conditions (ii) and (iii) are stronger than Conjecture 2' (the symmetric log-Delta conjecture). Direction correct: source is the stronger asymmetric refinement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The logarithmic bound holds for bipartite graphs whose tree-partition width is bounded by a fixed polynomial in the maximum degree, with a sharper bound available in terms of bandwidth.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of these special-case results has not been checked."
}
```

## 1. Statements of the partial results

All graphs below are finite. Write \(\operatorname{ch}(G)\) for the list chromatic number. The conjecture is understood for \(\Delta\ge 2\), or with \(\log(\Delta+1)\) in place of \(\log\Delta\).

A **tree partition of width \(m\)** is a partition
\[
V(G)=\bigsqcup_{t\in V(T)}X_t,\qquad |X_t|\le m,
\]
where \(T\) is a forest and every edge of \(G\) has its endpoints either in one block or in blocks indexed by adjacent vertices of \(T\). This is a partition, not merely a tree decomposition.

### Theorem 1
If \(G\) is bipartite, has maximum degree \(\Delta\), and admits a tree partition of width \(m\), then
\[
\boxed{\displaystyle
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln\!\bigl(2m(\Delta+1)-1\bigr)}
{\ln(4/3)}
\right\rceil .}
\tag{1}
\]

Consequently, for fixed constants \(C\ge1\) and \(a\ge0\), the conjectured \(O(\log\Delta)\) bound holds whenever
\[
m\le C\Delta^a.
\]
More precisely, in this class,
\[
\operatorname{ch}(G)
\le \frac{a+1}{\ln(4/3)}\ln\Delta+O_{C,a}(1).
\]

There is no restriction on the number of blocks or on \(|V(G)|\).

For an ordering \(v_1,\ldots,v_n\), its **bandwidth** is the maximum of \(|i-j|\) over edges \(v_iv_j\). The bandwidth of \(G\) is the minimum over all orderings.

### Theorem 2
Every bipartite graph of bandwidth \(b\ge2\) satisfies
\[
\boxed{\displaystyle
\operatorname{ch}(G)
\le \log_2 b+\log_2\log_2 b+O(1),}
\tag{2}
\]
where the implicit constant is absolute.

Thus, for fixed \(C,a>0\), bandwidth at most \(C\Delta^a\) implies
\[
\operatorname{ch}(G)
\le a\log_2\Delta+\log_2\log_2\Delta+O_{C,a}(1).
\]

The proofs use *local palettes*: different regions may make independent decisions about which side of the bipartition receives a color, while vertices use only colors whose local decisions are consistent.

---

## 2. A local-cover lemma

### Lemma
Let \(G\) be bipartite. Suppose there is a family \(\mathcal S\) of vertex subsets such that:

1. every vertex belongs to at least one and at most \(r\) members of \(\mathcal S\);
2. every edge has both endpoints in some member of \(\mathcal S\);
3. every member of \(\mathcal S\) has size at most \(M\).

Then
\[
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln\!\bigl(r(M-1)+1\bigr)}
{-\ln(1-2^{-r})}
\right\rceil .
\tag{3}
\]

### Proof

Fix a bipartition \(A\cup B\) and an arbitrary assignment of lists of size \(k\). Larger lists can be trimmed.

For every color \(c\) and every \(S\in\mathcal S\), independently choose a fair bit
\[
\xi_{c,S}\in\{A,B\}.
\]
Call \(c\in L(v)\) **available at \(v\)** if
\[
\xi_{c,S}=\text{the side containing }v
\quad\text{for every }S\ni v.
\]

A vertex belongs to at most \(r\) sets, so each listed color is available with probability at least \(2^{-r}\). Different colors use independent random variables. Hence the bad event \(E_v\) that \(v\) has no available color satisfies
\[
\Pr(E_v)\le (1-2^{-r})^k.
\]

Connect two bad events in a dependency graph whenever their vertices belong to a common member of \(\mathcal S\). Events not connected in this graph have disjoint sets of underlying variables. Its maximum degree is at most
\[
D=r(M-1).
\]
In particular, this dependency bound has **no factor of \(k\)**.

The symmetric Lovász local lemma guarantees that all bad events can be avoided if
\[
e(1-2^{-r})^k\bigl(r(M-1)+1\bigr)\le1.
\]
This is precisely the sufficient condition in (3).

Finally, choose any available color at each vertex. If adjacent vertices \(u\in A\) and \(v\in B\) both chose \(c\), take \(S\) containing both endpoints. Availability would require simultaneously
\[
\xi_{c,S}=A,\qquad \xi_{c,S}=B,
\]
a contradiction. Thus the coloring is proper. \(\square\)

---

## 3. Proof of Theorem 1

Root each component of the forest \(T\). For every node \(t\), define
\[
S_t=X_t\;\cup\!
\bigcup_{\substack{s\text{ a child}\\\text{of }t}}
\{v\in X_s:N_G(v)\cap X_t\ne\varnothing\}.
\]

These sets have the required properties:

- An edge inside \(X_t\) is covered by \(S_t\).
- An edge between \(X_t\) and a child block is covered by \(S_t\).
- A vertex in \(X_t\) belongs to \(S_t\), and possibly also to the set indexed by the parent of \(t\). Thus the load is at most \(2\).
- Finally,
  \[
  |S_t|
  \le |X_t|+\sum_{u\in X_t}d_G(u)
  \le m(\Delta+1).
  \]

Apply the lemma with
\[
r=2,\qquad M=m(\Delta+1).
\]
Since \(-\ln(1-2^{-2})=\ln(4/3)\), this gives (1). \(\square\)

**Extension.** The same argument works if the quotient graph of the partition admits an orientation of maximum indegree at most a fixed \(d\). Define \(S_t\) using the neighbors in blocks toward which edges are oriented. Each vertex then belongs to at most \(d+1\) sets, giving
\[
\operatorname{ch}(G)=O_d\!\left(\ln\bigl(m(\Delta+1)\bigr)\right).
\]
Thus the forest assumption can be replaced by a bounded-indegree orientation of the quotient.

---

## 4. A sharper localization argument for bandwidth

The preceding lemma uses each color at a vertex with probability at least \(1/4\). On a line, one can make that probability arbitrarily close to \(1/2\), while keeping dependencies local.

Fix an ordering \(v_1,\ldots,v_n\) of bandwidth at most \(b\), and let \(R\ge b\) be an integer. Include dummy integer positions outside \(\{1,\ldots,n\}\) so that all intervals below have their full lengths.

For every color \(c\) and position \(j\), independently choose:

- a continuous random label \(Z_{c,j}\), uniformly distributed on \([0,1]\);
- a fair bit \(\xi_{c,j}\in\{A,B\}\).

For each \(i\), put
\[
\begin{aligned}
U_i&=[i-R-b,i+R+b]\cap\mathbb Z,\\
W_i&=[i-R,i+R]\cap\mathbb Z,\\
I_i&=[i-R+b,i+R-b]\cap\mathbb Z.
\end{aligned}
\]
Let \(s_c(i)\) be the position of the minimum \(c\)-label in \(U_i\). Minima are unique with probability one.

Call \(c\in L(v_i)\) available if
\[
s_c(i)\in I_i
\quad\text{and}\quad
\xi_{c,s_c(i)}=\text{the side containing }v_i.
\tag{4}
\]

### Properness

Suppose \(v_iv_j\) is an edge. Since \(|i-j|\le b\),
\[
I_i\subseteq W_j\subseteq U_i.
\]
If \(c\) is available at \(v_i\), the minimum in \(U_i\) lies in \(I_i\), so it is also the minimum in \(W_j\).

If \(c\) is available at \(v_j\), its selected position is likewise the minimum in \(W_j\). Therefore
\[
s_c(i)=s_c(j).
\]
Because the endpoints lie on opposite sides of the bipartition, condition (4) cannot hold at both endpoints. Any choice of available colors is consequently proper.

### Availability probability

The minimum position is uniform in \(U_i\), and its bit is independent of the labels. Therefore
\[
\Pr(c\text{ is available at }v_i)
=
\frac{2(R-b)+1}{2\bigl(2(R+b)+1\bigr)}.
\]
Writing
\[
q=\frac12+\frac{2b}{2(R+b)+1},
\]
the probability that a vertex with \(k\) listed colors has none available is exactly \(q^k\).

The bad event at \(v_i\) uses variables only at positions in \(U_i\). Thus it is independent of all bad events outside index distance \(2(R+b)\), and a dependency graph has maximum degree at most \(4(R+b)\).

The local lemma now gives the explicit bound
\[
\boxed{\displaystyle
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln\!\bigl(4(R+b)+1\bigr)}
{-\ln\!\left(\frac12+\frac{2b}{2(R+b)+1}\right)}
\right\rceil
\qquad(R\ge b).}
\tag{5}
\]

For sufficiently large \(b\), choose
\[
R=\lceil b\ln b\rceil.
\]
Then
\[
\begin{aligned}
1+\ln\!\bigl(4(R+b)+1\bigr)
   &=\ln b+\ln\ln b+O(1),\\
-\ln\!\left(\frac12+\frac{2b}{2(R+b)+1}\right)
   &=\ln2-\frac{2}{\ln b}
     +O\!\left(\frac1{(\ln b)^2}\right).
\end{aligned}
\]
Substituting in (5) yields
\[
\operatorname{ch}(G)
\le \frac{\ln b+\ln\ln b}{\ln2}+O(1),
\]
which is (2). The finitely many smaller integer values of \(b\ge2\) are absorbed into the absolute constant using (5). \(\square\)

---

## 5. Why this does not settle the conjecture

The unresolved step is not an estimate inside these proofs. It is that arbitrary bounded-degree bipartite graphs need not possess the required bounded-load, small-set covers.

There is a direct obstruction. Suppose \(G\) has girth greater than \(M\), and \(\mathcal S\) covers its edges with sets of size at most \(M\) and vertex load at most \(r\). Every \(G[S]\) is a forest, so
\[
|E(G)|
\le \sum_{S\in\mathcal S}|E(G[S])|
\le \sum_{S\in\mathcal S}(|S|-1)
\le r|V(G)|.
\tag{6}
\]
Thus such a cover is impossible when the average degree exceeds \(2r\).

For completeness, bounded-degree bipartite graphs realizing this obstruction exist with arbitrarily large prescribed girth. Fix \(d\) and \(g\), and take the union of \(d\) independent uniformly random perfect matchings between two \(n\)-vertex sets. For \(n\ge2g\), the expected number of parallel pairs and cycles of length at most \(g\) is at most
\[
\binom d2+
\sum_{\ell=2}^{\lfloor g/2\rfloor}(2d)^{2\ell}.
\]
Indeed, for a cycle of length \(2\ell\), there are at most \(n^{2\ell}d^{2\ell}\) choices of vertices and matching labels, and any consistent specification has probability at most \((n-2\ell)^{-2\ell}\).

Hence some outcome has only \(O_{d,g}(1)\) such obstructions. Deleting one edge from each leaves a simple bipartite graph with:

- maximum degree at most \(d\);
- girth greater than \(g\);
- average degree \(d-O_{d,g}(1/n)\).

Taking \(d=5\) and \(n\) sufficiently large gives average degree greater than \(4\). By (6), these graphs cannot have two-fold edge covers with uniformly bounded set size. In particular, their tree-partition widths are unbounded despite maximum degree \(5\). Bandwidth is also unbounded, since bandwidth at most \(b\) gives a tree partition of width at most \(b\) by consecutive blocks.

This is an obstruction to the **method**, not a counterexample to the conjecture. The general problem still requires a way to handle high-expansion instances without paying for long-range color dependencies. The arguments above establish the stated special cases but supply no uniform \(c\) for all bipartite graphs.
