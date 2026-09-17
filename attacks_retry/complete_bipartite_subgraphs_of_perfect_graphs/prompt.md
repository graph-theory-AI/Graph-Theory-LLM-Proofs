Attack the following open graph-theory problem.

Catalog id: complete_bipartite_subgraphs_of_perfect_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/complete_bipartite_subgraphs_of_perfect_graphs/
Original entry: http://www.openproblemgarden.org/op/complete_bipartite_subgraphs_of_perfect_graphs
Problem attributed to: Fox, Jacob (posted 2008-06-17)

=== Problem statement (OpenProblemGarden) ===
Title: Complete bipartite subgraphs of perfect graphs
Problem Let $ G $ be a perfect graph on $ n $ vertices. Is it true that either $ G $ or $ \bar{G} $ contains a complete bipartite subgraph with bipartition $ (A,B) $ so that $ |A|, |B| \ge n^{1 - o(1)} $ ?

=== Discussion / context (OpenProblemGarden) ===
Every perfect graph on $ n $ vertices either has a clique or an independent set of size $ \ge n^{1/2} $ , so weakening the bound on $ |A| $ , $ |B| $ to $ \lfloor \frac{1}{2} n^{1/2} \rfloor $ gives a true statement. Jacob Fox [F] has proved that every comparability graph $ G $ on $ n $ vertices has a complete bipartite subgraph of size $ \ge c \frac{n}{\log n} $ , and (up to the constant) this is best possible.

=== References listed by OpenProblemGarden ===
- [F] J. Fox, A Bipartite Analogue of Dilworth’s Theorem, Order 23 (2006), 197-209.

=== Catalog page (statement + literature review) ===
Complete bipartite subgraphs of perfect graphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 Fox's 2008 problem asking whether every perfect graph $G$ on $n$ vertices has $G$ or $\bar{G}$ containing a complete bipartite subgraph $K_{A,B}$ with $|A|,|B|\ge n^{1-o(1)}$ appears to remain open. The best-known bound of $\Omega(n/\log n)$ for the special case of comparability graphs (Fox 2006) was extended to a multipartite setting for partial orders by Fox and Pham (2024), but no comparable advance for general perfect graphs has been found in the literature.

 Cited literature (1)

 
 
 
partial A multipartite analogue of Dilworth's Theorem
 (2024)
 

 
 Jacob Fox, Huy Tuan Pham · arXiv preprint · arXiv:2401.00827

Proves a multipartite extension of Fox's 2006 bipartite Dilworth result for partially ordered sets: every poset on $n$ elements contains $k$ subsets each of size $\Omega(n/k^5)$ forming a chain structure, or $\Omega(n/(k^2 \log n))$ that are pairwise incomparable. This advances the comparability-graph case (a subclass of perfect graphs) but does not address general perfect graphs.
 

 

 Reviewer notes. No paper was found that directly solves or makes progress on the perfect-graph problem as stated. The Fox–Pham 2024 paper (arXiv:2401.00827; the corresponding Springer Order 2025 publication at DOI 10.1007/s11083-025-09722-z could not be accessed due to a paywall redirect and is therefore not included in verified_urls) addresses a multipartite Dilworth theorem for posets — i.e., the comparability-graph subcase — and answers Fox's 2006 open question about multipartite generalisations, but leaves the general perfect-graph conjecture untouched. The Springer Combinatorica 2025 paper 'The Largest Subgraph Without A Forbidden Induced Subgraph' appeared in initial search results but was not verified by WebFetch and is therefore not cited. Confidence is medium rather than high because the problem is niche enough that a resolution in a specialised venue might not surface prominently in general web searches.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 162s.
 

Problem. Let $ G $ be a perfect graph on $ n $ vertices. Is it true that either $ G $ or $ \bar{G} $ contains a complete bipartite subgraph with bipartition $ (A,B) $ so that $ |A|, |B| \ge n^{1 - o(1)} $ ?

Keywords:
perfect graph

Discussion

Every perfect graph on $ n $ vertices either has a clique or an independent set of size $ \ge n^{1/2} $ , so weakening the bound on $ |A| $ , $ |B| $ to $ \lfloor \frac{1}{2} n^{1/2} \rfloor $ gives a true statement. Jacob Fox [F] has proved that every comparability graph $ G $ on $ n $ vertices has a complete bipartite subgraph of size $ \ge c \frac{n}{\log n} $ , and (up to the constant) this is best possible.

Bibliography

 [F]
 J. Fox, A Bipartite Analogue of Dilworth’s Theorem , Order 23 (2006), 197-209.
 A Bipartite Analogue of Dilworth’s Theorem

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the desired near-linear bound for clique-sums of substitution-composites of comparability, cocomparability, and basic perfect graphs, but not for arbitrary perfect graphs.",
  "would_publish": false,
  "caveats": "This is a specified structural subclass, not a resolution of the conjecture; novelty of the closure results is not claimed."
}
```

## 1. Statement of the partial result

Call disjoint vertex sets \(A,B\) a **homogeneous pair** if either all edges between \(A\) and \(B\) are present or none are present. Put
\[
b(G)=\max\{\min(|A|,|B|):(A,B)\text{ is a homogeneous pair in }G\}.
\]
Thus \(b(G)=b(\overline G)\), and the question asks whether every perfect \(n\)-vertex graph satisfies
\[
b(G)\ge n^{1-o(1)}.
\]
Edges inside \(A\) and \(B\) are unrestricted.

Here is a structural special case. Both closure operations in its statement can be iterated arbitrarily many times.

### The base classes

Let \(\mathcal B\) consist of:

1. perfect graphs whose vertices can be partitioned into at most four sets, each inducing a clique or an independent set;
2. line graphs of bipartite multigraphs, and their complements.

In particular, \(\mathcal B\) contains all the usual basic perfect-graph types: bipartite graphs, their complements, bipartite line graphs, their complements, and double-split graphs. For the last assertion, a double-split graph has a partition into two independent sets and two cliques.

Let
\[
\mathcal C=\mathcal B\cup
\{\text{comparability graphs and cocomparability graphs}\}.
\]

For a class \(\mathcal X\), define:

- \(\operatorname{Sub}(\mathcal X)\): graphs given by finite substitution trees whose internal quotient graphs belong to \(\mathcal X\). In a substitution \(H(G_1,\dots,G_k)\), each vertex \(i\) of \(H\) is replaced by \(G_i\), and distinct replacement graphs are complete or anticomplete according to their corresponding vertices in \(H\).
- \(\operatorname{CS}(\mathcal X)\): graphs obtained by repeated **clique-sums** of members of \(\mathcal X\). A clique-sum takes two graphs with a common clique, retains both graphs, and adds no edges between their exclusive vertex sets.

The order here matters: the theorem concerns \(\operatorname{CS}(\operatorname{Sub}(\mathcal X))\), not arbitrary alternation of the two operations.

### Theorem

For every \(n\ge 1\):

1. If \(G\in\operatorname{CS}(\operatorname{Sub}(\mathcal B))\), then
   \[
   b(G)\ge \left\lfloor\frac n{256}\right\rfloor.
   \]
2. There is an absolute constant \(c_*>0\) such that, if
   \(G\in\operatorname{CS}(\operatorname{Sub}(\mathcal C))\), then
   \[
   b(G)\ge
   \left\lfloor c_*\frac n{\log_2(2n)}\right\rfloor.
   \]

The first part is proved below without using the comparability-graph result. The second uses precisely the homogeneous-pair consequence of the Fox theorem supplied in the question.

These are indeed perfect-graph subclasses. Perfection is preserved under substitution and clique-sums. For clique-sums, optimal colorings can be made to agree on the common clique by permuting colors. Substitution closure follows from the replication lemma: replace each quotient vertex \(i\) by a clique of size \(\chi(G_i)\), color the resulting perfect graph, and use the colors assigned to that clique to color \(G_i\). The same argument applies to every induced subgraph.

---

## 2. A weighted linear bound for the basic pieces

The important issue in substitution is that the replacement graphs can have very unequal orders. An unweighted bound for the quotient does not, by itself, handle this.

Give each vertex \(v\) a positive weight \(w(v)\), with total weight \(W\). Write \(w(S)=\sum_{v\in S}w(v)\).

### Lemma 1

For every weighted graph \(H\in\mathcal B\), either

- some vertex has weight at least \(W/32\), or
- \(H\) has a homogeneous pair \((A,B)\) with
  \[
  w(A),w(B)\ge W/32.
  \]

#### Proof

Assume every individual weight is less than \(W/32\).

**Four homogeneous parts.**  
If \(V(H)\) is partitioned into at most four cliques or independent sets, one part \(S\) has weight at least \(W/4\). Greedily select \(A\subseteq S\) until
\[
W/32\le w(A)<W/16.
\]
Then
\[
w(S\setminus A)>W/4-W/16=3W/16.
\]
Thus \((A,S\setminus A)\) is a suitable homogeneous pair.

**Line graphs.**  
Write \(H=L(F)\), where \(F\) is a loopless multigraph. In fact, this argument does not require \(F\) to be bipartite.

Regard the vertex weights of \(L(F)\) as edge weights of \(F\). Let
\[
d_w(x)=\sum_{e\ni x}w(e),\qquad
\Delta_w=\max_x d_w(x).
\]

If \(\Delta_w\ge W/4\), the edges incident with a vertex attaining \(\Delta_w\) form a clique of weight at least \(W/4\). Split it as above.

Suppose instead that \(\Delta_w<W/4\). Independently color the vertices of \(F\) red or blue, each with probability \(1/2\). Let \(X\) be the total weight of edges with two red endpoints, and \(Y\) the corresponding blue-edge weight.

For an ordered pair of vertex-disjoint edges, the probability that the first is red and the second blue is \(1/16\). Intersecting edges contribute zero. Consequently,
\[
\mathbb E[XY]
=\frac1{16}\sum_{e\cap f=\varnothing}w(e)w(f).
\]
Moreover,
\[
\begin{aligned}
\sum_{e\cap f=\varnothing}w(e)w(f)
&\ge W^2-\sum_x d_w(x)^2\\
&\ge W^2-\Delta_w\sum_xd_w(x)\\
&=W^2-2\Delta_wW\\
&>W^2/2.
\end{aligned}
\]
The first inequality is valid also for parallel edges: every ordered intersecting pair is counted at least once in \(\sum_xd_w(x)^2\).

Thus some coloring has \(XY>W^2/32\). Since \(X,Y\le W\), both \(X\) and \(Y\) exceed \(W/32\). The red-edge and blue-edge families are anticomplete in \(L(F)\).

Finally, complementation exchanges complete and anticomplete pairs. This proves the lemma. \(\square\)

---

## 3. Making the comparability bound weighted

I use the following form of the result quoted in the question: for some absolute \(c_F>0\), every comparability graph \(H\) on \(m\ge2\) vertices satisfies
\[
b(H)\ge c_F\frac m{\log_2(2m)}. \tag{1}
\]
The same holds for cocomparability graphs because \(b\) is complement-invariant.

The dichotomy is essential: the discussion's literal assertion about a biclique in \(G\) alone cannot hold for an edgeless comparability graph.

We first need a rounding observation.

### Lemma 2: rounding a pair in an independent blow-up

Replace each vertex \(i\) of a graph \(H\) by an independent set of integer size \(w_i\). Suppose the resulting graph has a homogeneous pair \((P,Q)\) with
\[
|P|,|Q|\ge t.
\]
If every \(w_i<t/2\), then the weighted graph \(H\) has a homogeneous pair with both weights at least \(t/2\).

#### Proof

If \(P,Q\) are complete to one another, they cannot meet the same replacement set. Their supports therefore give disjoint complete vertex sets in \(H\), each of weight at least \(t\).

Suppose \(P,Q\) are anticomplete. Let

- \(S\) be the indices meeting \(P\) but not \(Q\);
- \(T\) be the indices meeting \(Q\) but not \(P\);
- \(R\) be the indices meeting both.

The pairs \(S,T\), \(S,R\), and \(T,R\) are anticomplete, and \(R\) is independent. Hence vertices of \(R\) may be assigned arbitrarily to the two sides without destroying anticompleteness.

Also,
\[
w(S)+w(R)\ge t,\quad
w(T)+w(R)\ge t,\quad
w(S)+w(T)+w(R)\ge2t. \tag{2}
\]
The last inequality uses the disjointness of \(P\) and \(Q\).

If \(w(S),w(T)\ge t/2\), we are done. Otherwise, say \(w(S)<t/2\), greedily add vertices from \(R\) to \(S\) until the resulting weight first reaches \(t/2\). This is possible by (2). Since every added weight is less than \(t/2\), the resulting side has weight less than \(t\). All remaining vertices of \(T\cup R\) then have total weight greater than \(t\), again by (2). These are the required anticomplete sides. The case \(w(T)<t/2\) is symmetric. \(\square\)

Independent blow-ups preserve both comparability and cocomparability:

- for a comparability graph, replace each poset element by an antichain;
- for a cocomparability graph, replace each poset element by a chain.

Therefore (1) and Lemma 2 give a weighted version.

Set
\[
\lambda=\min\{1/32,c_F/2\},
\qquad
h(W)=\lambda\frac W{\log_2(2W)}.
\]

### Lemma 3

Give a graph \(H\in\mathcal C\) positive integer vertex weights totaling \(W\). Then either

- some vertex has weight at least \(h(W)\), or
- \(H\) has a homogeneous pair with both weights at least \(h(W)\).

#### Proof

Assume every weight is less than \(h(W)\).

If \(H\in\mathcal B\), Lemma 1 applies because \(h(W)\le W/32\).

Otherwise form the independent blow-up of order \(W\). Applying (1), it has a homogeneous pair with both sides at least
\[
t=c_F\frac W{\log_2(2W)}.
\]
Since every replacement size is less than \(h(W)\le t/2\), Lemma 2 gives a weighted pair with both weights at least \(t/2\ge h(W)\). The case \(W=1\) automatically satisfies the heavy-vertex alternative. \(\square\)

---

## 4. Substitution does not accumulate a loss with depth

A set \(M\subseteq V(G)\) is a module if every vertex outside \(M\) is either complete or anticomplete to \(M\). Every node of a substitution tree represents a module of the final graph.

### Lemma 4

For an \(n\)-vertex graph \(G\),

\[
G\in\operatorname{Sub}(\mathcal B)
\quad\Longrightarrow\quad
b(G)\ge\left\lfloor n/64\right\rfloor,
\]
and
\[
G\in\operatorname{Sub}(\mathcal C)
\quad\Longrightarrow\quad
b(G)\ge
\left\lfloor
\lambda\frac n{2\log_2(2n)}
\right\rfloor.
\]

#### Proof

The case \(n=1\) is immediate. Suppose \(n\ge2\).

Give each node of the substitution tree weight equal to its number of descendant leaves. Starting at the root, descend into a child of weight greater than \(n/2\) whenever one exists. Stop at a node of weight \(W>n/2\) all of whose children have weight at most \(n/2\). This node is internal.

Use the child weights as weights on its quotient graph. Apply either Lemma 1, with threshold \(W/32\), or Lemma 3, with threshold \(h(W)\).

There are two cases.

**A weighted homogeneous pair exists in the quotient.**  
Take the unions of the corresponding child modules. Their cross-adjacencies are uniform, so their orders are exactly the quotient-side weights.

**A child module \(M\) meets the heavy-vertex threshold.**  
Since \(|M|\le n/2\), at least \(n/2\) vertices lie outside \(M\). Partition them according to whether they are complete or anticomplete to \(M\). One part has order at least \(n/4\). Together with \(M\), it gives a homogeneous pair.

Both thresholds are at most \(W/32\le n/32\), so the latter outside set is sufficiently large.

In the first setting the resulting sides have size at least
\[
W/32>n/64.
\]
In the second they have size at least
\[
h(W)
=\lambda\frac W{\log_2(2W)}
\ge \lambda\frac n{2\log_2(2n)}.
\]
This proves both assertions. \(\square\)

The useful feature is that the loss is independent of the substitution-tree depth.

---

## 5. Clique-sums cost only another constant factor

We use a general tree-decomposition observation.

### Lemma 5

Given an \(n\)-vertex graph with a tree decomposition, either

- it has an anticomplete pair with both sides of order at least \(n/4\), or
- some bag has order at least \(n/4\).

Here the bag in the second alternative can be chosen by a centroid argument, enabling application of a bound for the graphs induced by bags.

#### Proof

Assign every graph vertex to one bag containing it, giving the decomposition tree total assigned weight \(n\). Choose a weighted centroid node \(x\): every component of the tree after deleting \(x\) has assigned weight at most \(n/2\). Write \(B_x\) for its bag.

Every vertex outside \(B_x\) has all its bags in a unique component of the tree minus \(x\). Let the corresponding vertex sets be \(U_1,\ldots,U_r\). They satisfy
\[
|U_i|\le n/2,
\]
and distinct \(U_i\) are anticomplete: an edge between them would have to occur in a common bag.

If \(|B_x|\ge n/4\), we have the second alternative. Otherwise
\[
\sum_i|U_i|>3n/4.
\]
If some \(U_i\) has size between \(n/4\) and \(n/2\), take it as one side and all other \(U_j\) as the other. Both sides have size at least \(n/4\).

If every \(U_i\) has size less than \(n/4\), greedily combine them until their union first reaches \(n/4\). This union has size less than \(n/2\), and the remaining union has size greater than \(n/4\). Again the two unions are anticomplete. \(\square\)

A graph formed by clique-sums has a tree decomposition whose bags induce the original pieces. This follows inductively: the common clique lies in a bag of each operand's decomposition, and those two bags can be joined by a tree edge. The fact that a clique lies in a bag follows from the Helly property for subtrees.

Now apply Lemma 5 with pieces in \(\operatorname{Sub}(\mathcal B)\) or \(\operatorname{Sub}(\mathcal C)\).

If the large anticomplete pair occurs, it is already stronger than needed. Otherwise a bag of order \(m\ge n/4\) gives, by Lemma 4,
\[
b(G)\ge \left\lfloor m/64\right\rfloor
\ge\left\lfloor n/256\right\rfloor
\]
in the first case, and
\[
\begin{aligned}
b(G)
&\ge
\left\lfloor
\lambda\frac m{2\log_2(2m)}
\right\rfloor\\
&\ge
\left\lfloor
\lambda\frac n{8\log_2(2n)}
\right\rfloor
\end{aligned}
\]
in the second. Thus the theorem holds with
\[
c_*=\lambda/8.
\]

---

## 6. What remains uncovered

This argument shows two things relevant to the conjecture:

- the basic perfect pieces have a **weighted linear** homogeneous-pair guarantee;
- highly unequal substitutions and repeated clique-sums do not destroy the near-linear guarantee, or introduce a loss depending on construction depth.

It does **not** show that an arbitrary perfect graph belongs to either constructed class. In particular, no argument above handles the full range of perfect graphs arising through more general decomposition phenomena, including balanced skew partitions and general 2-joins. A substitution tree is not a general perfect-graph decomposition.

Consequently, I obtain **no improved bound for unrestricted perfect graphs** here. For that class, the universally justified bound in this writeup remains
\[
b(G)\ge \left\lfloor\frac{\sqrt n}{2}\right\rfloor,
\]
coming from \(\alpha(G)\omega(G)\ge n\).

The theorem above is therefore a precise structural special case, rather than a proof of the catalog conjecture.
