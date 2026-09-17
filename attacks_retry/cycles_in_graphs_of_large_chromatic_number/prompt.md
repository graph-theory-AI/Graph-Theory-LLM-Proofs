Attack the following open graph-theory problem.

Catalog id: cycles_in_graphs_of_large_chromatic_number
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/cycles_in_graphs_of_large_chromatic_number/
Original entry: http://www.openproblemgarden.org/op/cycles_in_graphs_of_large_chromatic_number
Problem attributed to: Brewster, Richard C., McGuinness, Sean, Moore, Benjamin, Noel, Jonathan A. (posted 2015-09-20)

=== Problem statement (OpenProblemGarden) ===
Title: Cycles in Graphs of Large Chromatic Number
Conjecture If $ \chi(G)>k $ , then $ G $ contains at least $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ .

=== Discussion / context (OpenProblemGarden) ===
Chudnovsky, Plumettaz, Scott and Seymour [CPSS] proved that every graph with chromatic number at least $ 4 $ contains a cycle of length $ 0\bmod 3 $ . A simpler proof was found by Wrochna [W]. Wrochna's argument was generalised by Brewster, McGuinness, Moore and Noel [BMMN] to the following: if $ \chi(G)>k $ , then $ G $ contains at least TeX Embedding failed! cycles of length $ 0\bmod k $ .} The compete graph on $ k+1 $ vertices has exactly $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ and so the conjecture above, if true, would be best possible.

=== References listed by OpenProblemGarden ===
- [BMMN] R. C. Brewster, S. McGuinness, B. Moore, J. A. Noel, A Dichotomy Theorem for Circular Colouring Reconfiguration, submitted, arXiv:1508.05573v1.
- [CPSS] M. Chudnovsky, M. Plumettaz, A. Scott, and P. Seymour, The Structure of Graphs with no Cycles of Length Divisible by Three, in preparation.
- [Wro] M. Wrochna, unpublished.

=== Catalog page (statement + literature review) ===
Cycles in Graphs of Large Chromatic Number — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The $k=3$ case of the conjecture — every graph with $\chi(G)>3$ contains at least $4$ cycles of length $0\bmod 3$ — was fully resolved by Kim and Picollelli (2024), who proved that every 4-critical graph contains at least 4 such cycles with equality only for $K_4$. They also showed that $(k+1)$-critical graphs with minimum degree $k$ contain at least as many cycles of length $0\bmod r$ as $K_{k+1}$ (provided $k+1\not\equiv 0\pmod{r}$), but the full conjecture for $k\ge 4$ remains open.

 Cited literature (1)

 
 
 
partial 4-Chromatic Graphs Have At Least Four Cycles of Length $0 \bmod 3$
 (2024)
 

 
 Sean Kim, Michael Picollelli · Electronic Journal of Combinatorics · arXiv:2312.05945 · doi:10.37236/12623

Proves the $k=3$ case of the BMMN conjecture in full (every 4-critical graph contains $\ge 4$ cycles of length $0\bmod 3$, uniquely minimised by $K_4$) and also establishes partial results toward the general conjecture for $(k+1)$-critical graphs with minimum degree $k$.
 

 

 Reviewer notes. The Gao–Huo–Ma (2023) result (that $(k+1)$-critical non-complete graphs contain cycles of all lengths mod $k$ for $k\ge 6$) is cited inside the Kim–Picollelli paper but was not independently verified here, so it is not listed in since_posted. The CPSS paper [Chudnovsky–Plumettaz–Scott–Seymour] was originally listed as 'in preparation'; it may have been published but was not found in searches. The 2026 paper arXiv:2605.02731 and arXiv:2601.13552 concern Dean's conjecture (minimum degree, not chromatic number) and are unrelated.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. If $ \chi(G)>k $ , then $ G $ contains at least $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ .

Keywords:
chromatic number · cycles

Discussion

Chudnovsky, Plumettaz, Scott and Seymour [CPSS] proved that every graph with chromatic number at least $ 4 $ contains a cycle of length $ 0\bmod 3 $ . A simpler proof was found by Wrochna [W]. Wrochna's argument was generalised by Brewster, McGuinness, Moore and Noel [BMMN] to the following: if $ \chi(G)>k $ , then $ G $ contains at least TeX Embedding failed! cycles of length $ 0\bmod k $ .} The compete graph on $ k+1 $ vertices has exactly $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ and so the conjecture above, if true, would be best possible.

Bibliography

 [BMMN]
 R. C. Brewster, S. McGuinness, B. Moore, J. A. Noel, A Dichotomy Theorem for Circular Colouring Reconfiguration, submitted, arXiv:1508.05573v1.

 [CPSS]
 M. Chudnovsky, M. Plumettaz, A. Scott, and P. Seymour, The Structure of Graphs with no Cycles of Length Divisible by Three, in preparation.

 [Wro]
 M. Wrochna, unpublished.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every nontrivial join, using only cycles of length exactly k; this also settles graphs of order at most 2k.",
  "would_publish": false,
  "caveats": "Intended range k≥3; no novelty claim for these partial results, and the general case k≥4 remains unresolved."
}
```

# A partial result: joins satisfy the conjecture

Throughout, graphs are finite and simple, and cycles are unoriented and need not be induced. Write
\[
T_k=\frac{(k+1)(k-1)!}{2}.
\]
I use the intended range \(k\ge3\). If \(k=2\) were allowed, an odd cycle would trivially contradict the statement.

The principal result proved below is:

> **Theorem 1.** Suppose \(k\ge3\), \(\chi(G)>k\), and \(G\) is a nontrivial join. Then \(G\) contains at least \(T_k\) cycles of length **exactly \(k\)**.
>
> Consequently, the conjecture holds whenever \(G\) contains a \((k+1)\)-critical subgraph whose complement is disconnected.

Here \(A\vee B\), the **join** of two vertex-disjoint graphs, is obtained by adding every edge between \(V(A)\) and \(V(B)\).

The counting argument is self-contained. A small-order corollary uses the classical Gallai decomposition theorem, stated explicitly below. I do not claim that these partial results are new.

## 1. A quantitative cycle-counting lemma for joins

For \(p,q\ge1\), let \(c_{p,q}(A\vee B)\) denote the number of cycles with exactly \(p\) vertices in \(A\) and \(q\) vertices in \(B\).

> **Lemma 2.** Suppose
> \[
> |A|=n_A,\quad |B|=n_B,\qquad
> \delta(A)\ge a-1,\quad \delta(B)\ge b-1.
> \]
> If \(1\le p\le a\), \(1\le q\le b\), and \(m=p+q\ge3\), then
> \[
> c_{p,q}(A\vee B)\ge
> \frac{1}{2m}\binom{m}{p}\,
> n_A n_B
> \frac{(a-1)!}{(a-p)!}
> \frac{(b-1)!}{(b-q)!}.
> \tag{1}
> \]

### Proof

Consider a word \(w\) of length \(m\) containing \(p\) letters \(A\) and \(q\) letters \(B\), with first letter \(A\) and last letter \(B\). Let \(r(w)\) be its number of \(A\)-runs, which also equals its number of \(B\)-runs.

We assign distinct vertices to the positions of \(w\), in order, so that consecutive positions are adjacent. The closing edge is automatic because the first and last positions lie in different parts.

The first \(A\)-position has \(n_A\) choices. At the \(j\)-th \(A\)-position, for \(j\ge2\):

* if the preceding position is an \(A\)-position, there are at least
  \[
  (a-1)-(j-2)=a-j+1
  \]
  unused neighbors available;
* otherwise, there are at least \(n_A-j+1\ge a-j+1\) choices.

The same argument applies to the \(B\)-positions. Thus every such word has at least
\[
P=
n_A n_B
\frac{(a-1)!}{(a-p)!}
\frac{(b-1)!}{(b-q)!}
\tag{2}
\]
realizations as an oriented cycle with a distinguished starting vertex.

An unoriented cycle having \(r\) runs in each part has exactly \(2r\) representations of this kind: two orientations, and in each orientation \(r\) possible starting vertices immediately after a \(B\)-to-\(A\) crossing. Consequently,
\[
c_{p,q}(A\vee B)
\ge \frac P2\sum_w\frac1{r(w)}.
\tag{3}
\]

There are
\[
\binom{p-1}{r-1}\binom{q-1}{r-1}
\]
words with \(r\) runs in each part, by choosing the positive run lengths. Hence
\[
\begin{aligned}
\sum_w\frac1{r(w)}
&=\sum_{r\ge1}\frac1r
  \binom{p-1}{r-1}\binom{q-1}{r-1}\\
&=\frac1p\sum_{r\ge1}
  \binom pr\binom{q-1}{q-r}\\
&=\frac1p\binom{m-1}{q}
=\frac1m\binom mp,
\end{aligned}
\]
where the penultimate equality is Vandermonde’s identity. Substitution into (3) proves (1). \(\square\)

The weighted count above avoids any assumption that the cyclic \(A,B\)-patterns are aperiodic.

## 2. Applying the lemma at the chromatic threshold

First suppose \(a,b\ge2\) and
\[
a+b=k+1.
\]
Apply Lemma 2 to the two disjoint types
\[
(p,q)=(a,b-1)
\quad\text{and}\quad
(p,q)=(a-1,b).
\]
In both applications, the factorial factor in (2) is
\[
n_A n_B(a-1)!(b-1)!.
\]
Therefore
\[
\begin{aligned}
c_k(A\vee B)
&\ge
\frac{n_A n_B(a-1)!(b-1)!}{2k}
\left[\binom ka+\binom k{a-1}\right]\\
&=
\frac{n_A n_B(a-1)!(b-1)!}{2k}
\binom{k+1}{a}\\
&=
\frac{n_A n_B}{ab}\,T_k.
\end{aligned}
\tag{4}
\]
Here \(c_k\) counts cycles of length exactly \(k\). Since \(n_A\ge a\) and \(n_B\ge b\), this proves the desired bound.

Thus we have the stronger quantitative statement
\[
\boxed{\quad
c_k(A\vee B)\ge \frac{|A||B|}{ab}\,T_k
\quad}
\tag{5}
\]
whenever \(a,b\ge2\), \(a+b=k+1\), and the two minimum-degree hypotheses hold.

### The case of a one-vertex factor

Suppose \(B\) is \(k\)-critical and \(u\) is adjacent to every vertex of \(B\). Then \(\delta(B)\ge k-1\).

If \(|B|=k\), then \(B=K_k\), so \(B+u=K_{k+1}\), which has exactly \(T_k\) cycles of length \(k\).

Otherwise \(|B|\ge k+1\). The number of ordered simple paths on \(k-1\) vertices in \(B\) is at least
\[
|B|(k-1)(k-2)\cdots2=|B|(k-1)!.
\tag{6}
\]
Adding \(u\) closes each such path to a \(k\)-cycle, with each unoriented cycle counted twice. Consequently,
\[
c_k(B+u)\ge \frac{|B|(k-1)!}{2}\ge T_k.
\tag{7}
\]

### Proof of Theorem 1

Write \(G=G_1\vee G_2\), where both parts are nonempty. Since
\[
\chi(G)=\chi(G_1)+\chi(G_2)\ge k+1,
\]
choose positive integers
\[
a\le\chi(G_1),\qquad b\le\chi(G_2),\qquad a+b=k+1.
\]
Take an \(a\)-critical subgraph \(A\subseteq G_1\) and a \(b\)-critical subgraph \(B\subseteq G_2\). Criticality gives
\[
\delta(A)\ge a-1,\qquad \delta(B)\ge b-1.
\]

If \(a,b\ge2\), use (4). If one of \(a,b\) equals \(1\), its critical subgraph is a single vertex, and (7) applies. All these cycles lie in \(G\). \(\square\)

### A family beyond the degree-\(k\) special case

Let
\[
G=C_{2s+1}\vee C_{2t+1},\qquad s,t\ge2.
\]
Then \(\chi(G)=6\), so \(k=5\). Taking \(a=b=3\), (5) gives
\[
c_5(G)\ge
\frac{(2s+1)(2t+1)}9\,T_5
=8(2s+1)(2t+1)\ge200,
\]
whereas \(T_5=72\).

These graphs have clique number \(4\) and minimum degree at least \(7\). They are also \(6\)-critical. For example, after deleting a cross-edge \(xy\), use disjoint two-color palettes on the two odd cycles minus \(x\) and \(y\), and give \(x,y\) a fifth common color. Deleting an internal edge or a vertex also makes the join \(5\)-colorable.

Thus the join result covers critical graphs with minimum degree strictly greater than \(k\), not merely graphs containing \(K_{k+1}\).

## 3. The small-order corollary

For this corollary, use the following classical, proved theorem.

> **Gallai’s decomposition theorem.** An \(r\)-critical graph on at most \(2r-2\) vertices is a nontrivial join.

Here “critical” means that every proper subgraph has smaller chromatic number.

> **Corollary 3.** If \(k\ge3\), \(\chi(G)>k\), and
> \[
> |V(G)|\le2k,
> \]
> then \(G\) contains at least \(T_k\) cycles of length exactly \(k\).

Indeed, choose a \((k+1)\)-critical subgraph \(H\subseteq G\). It has at most
\[
2k=2(k+1)-2
\]
vertices, so Gallai’s theorem makes it a nontrivial join. Theorem 1 applies.

The same conclusion holds when a larger graph \(G\) contains such a small critical subgraph.

## 4. Further necessary conditions on a counterexample

Two additional elementary reductions help identify what remains.

### 4.1 Every neighborhood must have small degeneracy

> **Proposition 4.** If some neighborhood \(N_G(v)\) contains a subgraph \(F\) with
> \[
> \delta(F)\ge k-1,
> \]
> then \(G\) contains at least \(T_k\) cycles of length exactly \(k\).

The minimum-degree condition implies \(|F|\ge k\). If \(|F|=k\), then \(F=K_k\), and adding \(v\) gives \(K_{k+1}\). If \(|F|\ge k+1\), the path count (6), followed by closing through \(v\), gives the result.

Consequently, in any counterexample every neighborhood is \((k-2)\)-degenerate:
\[
\boxed{\qquad G[N_G(v)]\text{ is }(k-2)\text{-degenerate for every }v.\qquad}
\tag{8}
\]

This condition is stronger than merely forbidding a \(k\)-chromatic neighborhood.

### 4.2 The degree-\(k\) critical case

For completeness, here is a self-contained proof of the degree-\(k\) special case mentioned in the question, for the particular modulus \(k\).

> **Proposition 5.** If a \((k+1)\)-critical graph \(H\) has a vertex of degree \(k\), then \(H\) has at least \(T_k\) cycles whose lengths are divisible by \(k\).

**Proof.** Let \(v\) have degree \(k\), and fix a proper \(k\)-coloring of \(H-v\). Every color occurs exactly once in \(N_H(v)\), since a missing color would extend the coloring to \(H\).

Fix a cyclic order of the colors, and temporarily label them by \(\mathbb Z_k\) in that order. Let \(x_i\) be the neighbor of \(v\) colored \(i\). Form a digraph \(D\) on \(H-v\) by directing an edge from color \(i\) to color \(i+1\), and omitting edges between nonconsecutive colors.

For every \(i\), there is a directed path
\[
x_i\longrightarrow x_{i-1}.
\tag{9}
\]
Otherwise, let \(R\) be the set reachable from \(x_i\). Increase the color of every vertex of \(R\) by \(1\), modulo \(k\). This remains proper: a newly monochromatic crossing edge would be an arc leaving \(R\), contrary to reachability closure. Since \(x_{i-1}\notin R\), color \(i\) disappears from \(N_H(v)\), allowing \(v\) to receive color \(i\), a contradiction.

It follows from (9) that all \(x_i\) lie in one strongly connected component. In particular:

* \(D\) contains a directed cycle, whose length is divisible by \(k\);
* for each \(i\), choose a simple directed path \(P_i\) from \(x_i\) to \(x_{i-2}\).

The path \(P_i\) has length congruent to \(k-2\pmod k\), so adjoining \(v\) makes a cycle of length divisible by \(k\). These \(k\) cycles through \(v\) are distinct: after deleting \(v\), each has a unique direction compatible with \(D\), and hence a unique starting neighbor \(x_i\). Together with the cycle avoiding \(v\), this gives \(k+1\) cycles for the chosen cyclic color order.

There are
\[
\frac{(k-1)!}{2}
\]
cyclic color orders up to reversal. Cycles obtained for distinct such orders cannot coincide:

* a directed cycle avoiding \(v\) displays the entire cyclic order of the \(k\) colors;
* a path \(P_i\) displays at least \(k-1\) consecutive distinct colors. If exactly \(k-1\) colors occur, the single missing color has a unique position completing the cyclic order; if all \(k\) occur, the order is already determined.

Thus the underlying unoriented cycle determines the color order up to reversal. We obtain at least
\[
(k+1)\frac{(k-1)!}{2}=T_k
\]
distinct cycles. \(\square\)

## 5. What remains unresolved

If the conjecture fails, choose a \((k+1)\)-critical subgraph \(H\) of a counterexample. The preceding results force all of the following:
\[
\begin{array}{ll}
\text{(i)}&\delta(H)\ge k+1,\\[2mm]
\text{(ii)}&\overline H\text{ is connected},\\[2mm]
\text{(iii)}&|V(H)|\ge2k+1,\\[2mm]
\text{(iv)}&H[N_H(v)]\text{ is }(k-2)\text{-degenerate for every }v.
\end{array}
\]

These are necessary conditions, not a contradiction. In particular, the join-counting argument does not address general complement-connected critical graphs, and the neighborhood criterion gives no leverage in triangle-free graphs. In such graphs, the required cycles may have lengths \(2k,3k,\ldots\), rather than \(k\).

Accordingly, this does **not** settle the conjecture for general \(k\ge4\). The concrete partial advance is the quantitative join bound (5), its small-order consequence, and the resulting restrictions on a possible counterexample.
