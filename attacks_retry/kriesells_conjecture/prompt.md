Attack the following open graph-theory problem.

Catalog id: kriesells_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Connectivity
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/kriesells_conjecture/
Original entry: http://www.openproblemgarden.org/op/kriesells_conjecture
Problem attributed to: Kriesell, Matthias (posted 2013-08-25)

=== Problem statement (OpenProblemGarden) ===
Title: Kriesell's Conjecture
Conjecture Let $ G $ be a graph and let $ T\subseteq V(G) $ such that for any pair $ u,v\in T $ there are $ 2k $ edge-disjoint paths from $ u $ to $ v $ in $ G $ . Then $ G $ contains $ k $ edge-disjoint trees, each of which contains $ T $ .

=== Discussion / context (OpenProblemGarden) ===
This problem was featured as unsolved problem #22 in Bondy and Murty's book "Graph Theory" [BM]. See also a posting on the open problem forum of the Egerváry Research Group on Combinatorial Optimization.

=== References listed by OpenProblemGarden ===
- [BM] J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.

=== Catalog page (statement + literature review) ===
Kriesell's Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Kriesell's conjecture that 2k-edge-connectivity of $T$ in $G$ guarantees $k$ edge-disjoint $T$-Steiner trees remains open in full generality. The best known result (DeVos, McDonald, Pivotto, 2016) shows that edge-cuts separating $T$ of size at least $5k+4$ suffice, improving earlier bounds of $6.5k$ (West–Wu) and $24k$ (Lau). Special cases are settled: the conjecture holds when $|T| \leq 5$, when $V\setminus T$ is a stable set in a $3k$-edge-connected graph, and when every vertex in $V\setminus T$ has even degree.

 Cited literature (1)

 
 
 
partial Packing Steiner Trees
 (2016)
 

 
 Matt DeVos, Jessica McDonald, Irene Pivotto · Journal of Combinatorial Theory, Series B · arXiv:1307.7621

Proves that $k$ edge-disjoint $T$-Steiner trees exist when every edge-cut separating $T$ has size at least $5k+4$, giving the best known constant-factor relaxation of Kriesell's conjecture and improving earlier bounds of $6.5k$ and $24k$.
 

 

 Reviewer notes. The DeVos–McDonald–Pivotto arXiv preprint (1307.7621) was submitted July 29, 2013, slightly before the OPG posting date of August 25, 2013; it is included here by its journal publication year of 2016. A 2023 paper in Graphs and Combinatorics (DOI: 10.1007/s00373-023-02621-3) titled 'Edge-Disjoint Steiner Trees and Connectors in Graphs' appeared in search results but could not be verified due to Springer paywall restrictions; it may contain further progress. The West–Wu 6.5k result was cited in multiple sources but no specific verified arXiv URL was found. Lau's 24k bound dates from around 2004, predating the OPG posting.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. Let $ G $ be a graph and let $ T\subseteq V(G) $ such that for any pair $ u,v\in T $ there are $ 2k $ edge-disjoint paths from $ u $ to $ v $ in $ G $ . Then $ G $ contains $ k $ edge-disjoint trees, each of which contains $ T $ .

Keywords:
Disjoint paths · edge-connectivity · spanning trees

Discussion

This problem was featured as unsolved problem #22 in Bondy and Murty's book "Graph Theory" [BM]. See also a posting on the open problem forum of the Egerváry Research Group on Combinatorial Optimization.

Bibliography

 [BM]
 J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when at most 2k+1 vertices outside T have odd degree, by a splitting-off and hypergraph-packing argument.",
  "would_publish": false,
  "caveats": "The full conjecture is not resolved here, and novelty of this special case has not been checked."
}
```

# A parity-defect bound

I obtain a parameterized sufficient condition, and give a complete argument below. I have not verified whether this condition already appears in the literature, so I do not claim novelty or an improvement over every known special case.

Graphs are finite and undirected. Parallel edges are allowed; loops may be discarded. Write
\[
q(G,T)=|\{v\in V(G)\setminus T:\deg_G(v)\text{ is odd}\}|.
\]
A **\(T\)-cut** is an edge cut with terminals on both sides. By the edge version of Menger’s theorem, the hypothesis in the question is equivalent to every \(T\)-cut having size at least \(2k\).

## 1. Partial result

**Theorem.** Let \(k\ge1\), let \(|T|\ge2\), and put \(q=q(G,T)\). If every \(T\)-cut has size at least
\[
\boxed{\max\left\{2k,\ k+\left\lfloor\frac q2\right\rfloor\right\},}
\]
then \(G\) contains \(k\) edge-disjoint trees containing \(T\).

In particular, under the original \(2k\)-connectivity hypothesis, the conjecture holds whenever
\[
\boxed{q(G,T)\le 2k+1.}
\]

The proof uses established splitting-off and matroid min–max theorems, not another conjecture.

## 2. Reduction to at most \(q\) cubic nonterminals

Splitting off two edges \(vx,vy\) means deleting them and inserting an edge \(xy\). If \(x=y\), the resulting loop can be discarded.

We use the following standard form of **Mader’s local splitting-off theorem**:

> If a vertex \(v\) has degree at least two, has degree different from three, and is incident with no bridge, then some pair of edges at \(v\) can be split off without decreasing the local edge-connectivity between any two vertices other than \(v\).

Here and below, edges are kept individually labeled, including parallel edges.

**Reduction lemma.** Suppose every \(T\)-cut of \(G\) has size at least \(\lambda\ge2\). There is a connected loopless multigraph \(H\), containing the same terminal set \(T\), such that:

1. every \(T\)-cut of \(H\) has size at least \(\lambda\);
2. every vertex of \(V(H)\setminus T\) has degree three;
3. \(|V(H)\setminus T|\le q(G,T)\);
4. any packing of edge-disjoint \(T\)-trees in \(H\) lifts to one of the same size in \(G\).

### Proof

First discard components not containing \(T\). All terminals lie in one component.

We need a pruning observation. Delete all bridges and let \(B\) be the resulting component containing \(T\). Such a component contains all terminals, since a bridge separating terminals would be a \(T\)-cut of size one.

Replacing the current graph by its induced subgraph on \(B\) preserves terminal connectivity: a simple path between terminals cannot make an excursion across a bridge into a terminal-free branch.

This pruning also cannot increase the number of odd-degree nonterminals. Indeed, each component \(D\) outside \(B\) is attached to \(B\) by exactly one bridge. Consequently,
\[
\sum_{v\in D}\deg(v)=2|E(D)|+1.
\]
Thus \(D\) contains an odd-degree vertex, necessarily a nonterminal. If there are \(b\) such branches, they contain at least \(b\) odd-degree nonterminals. Deleting their attachment edges can create at most \(b\) new odd-degree nonterminals inside \(B\). Hence the total number does not increase.

We may therefore repeatedly perform the following operations:

* prune to the bridgeless component containing \(T\);
* if a nonterminal \(v\) has degree different from three, apply Mader’s theorem at \(v\) and split off an admissible pair;
* remove isolated vertices and discard loops.

After pruning, every vertex has degree at least two. Thus Mader’s theorem applies whenever the second operation is needed.

A splitting changes every affected degree by an even number, so it preserves degree parity. Removing an isolated vertex does not remove an odd-degree vertex. Terminal connectivity is preserved because the split vertex is not a terminal.

Each splitting strictly decreases the edge count. The process terminates with all remaining nonterminals cubic. Each is therefore odd, and the parity-count observation gives
\[
|V(H)\setminus T|\le q(G,T).
\]

Finally, reverse the splittings. Each used replacement edge is expanded into its two predecessor edges. Distinct retained edges expand into edge-disjoint sets of original edges. Expansion preserves connectedness, although it can create cycles when several expansions pass through the same eliminated vertex. After all expansions, take a spanning tree of each connected subgraph. This produces edge-disjoint trees containing \(T\) in the original graph. ∎

## 3. A hypergraph packing lemma

The following lemma is a standard hypergraphic analogue of spanning-tree packing. I include its matroid proof to specify exactly what it supplies.

**Lemma.** Let \(\mathcal H=(X,\mathcal E)\) be a finite hypergraph, allowing repeated hyperedges, with every hyperedge of size at least two. Suppose that for every partition \(\mathcal P\) of \(X\),
\[
d_{\mathcal H}(\mathcal P)\ge k(|\mathcal P|-1),                 \tag{1}
\]
where \(d_{\mathcal H}(\mathcal P)\) counts hyperedges meeting at least two parts.

Then one can select pairs of vertices from some hyperedges, using each hyperedge at most once in total, so that the selected pairs form \(k\) edge-disjoint spanning trees on \(X\).

### Proof

For each labeled hyperedge \(e\), create all graph edges \(xy\) with \(x,y\in e\), \(x\ne y\), retaining the label \(e\). Let \(\Omega\) be this set of candidate edges and \(n=|X|\).

Consider two matroids on \(\Omega\):

* \(M_k\), the union of \(k\) copies of the graphic matroid; its independent sets are unions of \(k\) forests;
* \(N\), the partition matroid allowing at most one candidate edge with each hyperedge label.

The matroid-union rank formula gives, for \(A\subseteq\Omega\),
\[
r_{M_k}(A)
=
\min_{\mathcal P}
\left[
k(n-|\mathcal P|)+|A\cap\delta(\mathcal P)|
\right],                                                    \tag{2}
\]
where \(\delta(\mathcal P)\) denotes the candidate edges crossing the partition.

For completeness, this is the graphic specialization of
\[
r_{M_k}(A)=
\min_{B\subseteq A}\bigl(|A\setminus B|+k(n-c(B))\bigr),
\]
with \(c(B)\) the number of components of \((X,B)\). Taking the component partition of \(B\), and conversely taking all \(A\)-edges internal to a partition, gives (2).

Fix \(A\subseteq\Omega\) and a partition \(\mathcal P\). Every hyperedge crossing \(\mathcal P\) either:

* has a candidate edge outside \(A\), so its label is counted by \(r_N(\Omega\setminus A)\); or
* has all its candidate edges in \(A\), including a crossing one.

Therefore
\[
|A\cap\delta(\mathcal P)|+r_N(\Omega\setminus A)
\ge d_{\mathcal H}(\mathcal P).
\]
Using (1) and (2),
\[
\begin{aligned}
r_{M_k}(A)+r_N(\Omega\setminus A)
&\ge
\min_{\mathcal P}
\left[k(n-|\mathcal P|)+d_{\mathcal H}(\mathcal P)\right]\\
&\ge k(n-1).
\end{aligned}
\]

The matroid-intersection theorem now supplies a common independent set of size \(k(n-1)\). Its decomposition into \(k\) forests must consist of \(k\) spanning trees, since each forest has at most \(n-1\) edges. Independence in \(N\) ensures that each hyperedge label is used at most once. ∎

## 4. Proof of the parity-defect bound

Let every \(T\)-cut have size at least \(\lambda\), where
\[
\lambda\ge 2k,
\qquad
\lambda\ge k+\left\lfloor\frac q2\right\rfloor.                \tag{3}
\]
Apply the reduction lemma. We obtain \(H\) with at most \(q\) nonterminals, all cubic.

Let \(\mathcal C\) be the components of \(H-T\). For \(C\in\mathcal C\), write
\[
n_C=|V(C)|,\qquad m_C=|E(C)|,\qquad d_C=|\delta_H(C)|.
\]
Since every vertex of \(C\) has degree three,
\[
d_C=3n_C-2m_C.
\]
Since \(C\) is connected, \(m_C\ge n_C-1\), and hence
\[
d_C\le n_C+2.                                               \tag{4}
\]

Construct a hypergraph \(\mathcal H\) on vertex set \(T\):

* every edge of \(H[T]\) becomes a labeled two-element hyperedge;
* every component \(C\) having at least two distinct terminal neighbors contributes one labeled hyperedge
  \[
  N_T(C).
  \]

Components with just one terminal neighbor are omitted.

Fix a partition
\[
\mathcal P=\{P_1,\ldots,P_r\}
\]
of \(T\), with \(r\ge2\). Let

* \(a\) be the number of \(H[T]\)-edges crossing \(\mathcal P\);
* \(\mathcal C_\times\) be the components whose terminal neighborhoods meet at least two parts;
* \(c=|\mathcal C_\times|\).

Then
\[
d_{\mathcal H}(\mathcal P)=a+c.                              \tag{5}
\]

For each \(i\), define
\[
U_i=P_i\ \cup
\bigcup_{\substack{C\in\mathcal C\\N_T(C)\subseteq P_i}}V(C).
\]
Each \(U_i\) separates terminals, so
\[
|\delta_H(U_i)|\ge\lambda.
\]
Summing these \(r\) inequalities gives the exact counting relation
\[
\lambda r
\le
\sum_{i=1}^r|\delta_H(U_i)|
=
2a+\sum_{C\in\mathcal C_\times}d_C.                          \tag{6}
\]
Terminal-terminal crossing edges are counted twice; edges from crossing nonterminal components to terminals are counted once.

By (4),
\[
\sum_{C\in\mathcal C_\times}(d_C-2)
\le
\sum_{C\in\mathcal C_\times}n_C
\le q.
\]
Together with (5) and (6), this yields
\[
d_{\mathcal H}(\mathcal P)
=a+c
\ge \frac{\lambda r-q}{2}.                                  \tag{7}
\]

Conditions (3) imply
\[
\begin{aligned}
\lambda r-q-2k(r-1)
&=(\lambda-2k)(r-2)+(2\lambda-2k-q)\\
&\ge -1.
\end{aligned}
\]
Since the left side of (7) is an integer,
\[
d_{\mathcal H}(\mathcal P)\ge k(r-1).
\]
Thus the hypergraph packing lemma applies.

Realize its selected pairs in \(H\). A pair coming from a terminal-terminal edge uses that edge. A pair \(u,v\in N_T(C)\) is realized by a \(u\)-\(v\) path whose internal vertices lie in \(C\). Because each component-hyperedge is used at most once across the entire packing, these paths are mutually edge-disjoint. Expanding the spanning trees therefore gives \(k\) edge-disjoint \(T\)-trees in \(H\).

The reduction lemma lifts them to \(G\), proving the theorem. ∎

### A slightly finer structural criterion

The proof actually uses only
\[
\sum_{\substack{C\in\mathcal C\\|N_T(C)|\ge2}}(d_C-2)
\le 2\lambda-2k+1,
\qquad \lambda\ge2k.
\]
The odd-nonterminal count is a convenient upper bound on this boundary-excess sum after splitting off. Thus some graphs with more than \(2k+1\) odd nonterminals are also covered.

## 5. The precise obstruction to extending this argument

The restrictive step is replacing an entire component of \(H-T\) by **one selectable pair**. A Steiner tree can instead use a component to join three or more terminal regions at once.

The method can fail immediately beyond the stated parity budget.

Take \(k=3\) and
\[
T=\{a,b,c,d\}.
\]
For each \(t\in T\), introduce two nonterminals \(x_t^1,x_t^2\), each adjacent to all three terminals in \(T\setminus\{t\}\). There are no other edges.

All eight nonterminals are cubic, so
\[
q=8=2k+2.
\]
Every \(T\)-cut has size at least six:

* a one-versus-three terminal split has minimum cut size six;
* a two-versus-two split has minimum cut size eight.

Indeed, each nonterminal can be placed independently on whichever side minimizes its contribution.

But the auxiliary hypergraph has only eight hyperedges. For the partition into four singleton terminals,
\[
d_{\mathcal H}(\mathcal P)=8<3(4-1)=9.
\]
Consequently, the one-pair-per-component reduction cannot produce three spanning trees.

This graph is **not** a counterexample to Kriesell’s conjecture. Three edge-disjoint Steiner trees can be formed using the following disjoint pairs of stars:
\[
(x_a^1,x_b^1),\qquad
(x_a^2,x_c^1),\qquad
(x_b^2,x_d^1).
\]
In each pair, use the first star in full, and use two edges of the second star to attach the missing terminal to a terminal already in the first star.

Thus the gap is genuine and explicit: the cut argument controls a packing model that permits only one connection per nonterminal component, whereas Steiner trees can exploit branching. No argument above handles that additional freedom in general, and the full conjecture remains unresolved by this attack.
