Attack the following open graph-theory problem.

Catalog id: 2206.00594__02
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.00594__02/
Source paper: Sparse graphs with bounded induced cycle packing number have logarithmi… (arXiv:2206.00594)

=== Catalog page (statement + literature review) ===
MIS tractability in bounded-iocp graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that Maximum Independent Set is tractable in graphs with bounded induced odd cycle packing number (iocp) remains open. The source paper (arXiv:2206.00594) itself describes this as 'a surprising and formidable generalisation' of Conjecture 1.3 (MIS polynomial in Ok-free graphs) and of the known polynomial-time result for bounded ocp; no follow-up resolving it was found in a wide web search. The related prior work by Dvořák (arXiv:2001.02411, J. Graph Theory 2023) handles approximation in bounded-iocp graphs with additional VC-dimension constraints but does not settle exact tractability.

 Reviewer notes. No follow-up paper resolving or making partial progress on this conjecture was found across three targeted web searches and verification of the source paper's full HTML. The conjecture is informal and appears only in the discussion section of 2206.00594. Bounded iocp is strictly weaker than bounded icp, making this a harder graph class; even for bounded icp only quasi-polynomial time is known in general (with polynomial for sparse graphs). Dvořák's arXiv:2001.02411 (pre-dates conjecture) gives a QPTAS for independence number under bounded iocp, but exact polynomial time remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Maximum Independent Set could be tractable in graphs with bounded $\mathrm{iocp}$ (induced odd cycle packing number).

Context

The paper establishes tractability of MIS for graphs with bounded induced cycle packing number ($\mathrm{icp}$, i.e., $\mathcal{O}_k$-free graphs) in the sparse case, and quasipolynomial time in general. The authors remark that extending this to bounded $\mathrm{iocp}$ would be a surprising and formidable generalisation of Conjecture 1.3 and of the known polynomial-time result for bounded $\mathrm{ocp}$ (odd cycle packing number).

Notes. Stated as a speculative remark in prose ('As far as we can tell, MIS could even be tractable in graphs with bounded iocp'); authors treat it seriously as a potential generalisation.

Source paper

 Sparse graphs with bounded induced cycle packing number have logarithmic treewidth
 Marthe Bonamy, Édouard Bonnet, Hugues Déprés, Louis Esperet, Colin Geniet, Claire Hilaire, Stéphan Thomassé, Alexandra Wesolek · 2024-02-16
 https://arxiv.org/abs/2206.00594

=== Source paper abstract / header ===
Abstract:A graph is $\mathcal{O}_k$-free if it does not contain $k$ pairwise vertex-disjoint and non-adjacent cycles. We prove that "sparse" (here, not containing large complete bipartite graphs as subgraphs) $\mathcal{O}_k$-free graphs have treewidth (even, feedback vertex set number) at most logarithmic in the number of vertices. This is optimal, as there is an infinite family of $\mathcal{O}_2$-free graphs without $K_{2,3}$ as a subgraph and whose treewidth is (at least) logarithmic.
Using our result, we show that Maximum Independent Set and 3-Coloring in $\mathcal{O}_k$-free graphs can be solved in quasi-polynomial time. Other consequences include that most of the central NP-complete problems (such as Maximum Independent Set, Minimum Vertex Cover, Minimum Dominating Set, Minimum Coloring) can be solved in polynomial time in sparse $\mathcal{O}_k$-free graphs, and that deciding the $\mathcal{O}_k$-freeness of sparse graphs is polynomial time solvable.
 

 
 
 
 Comments:
 30 pages, 6 figures. v5: revised version
 

 Subjects:
 
 Combinatorics (math.CO); Data Structures and Algorithms (cs.DS)
 

 Cite as:
 arXiv:2206.00594 [math.CO]
 

 
  
 (or 
 arXiv:2206.00594v5 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.00594
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B 167 (2024), 215-249
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2024.03.003

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Louis Esperet [view email] 
 [v1]
 Wed, 1 Jun 2022 16:06:38 UTC (138 KB)

 [v2]
 Tue, 14 Jun 2022 10:57:46 UTC (138 KB)

 [v3]
 Mon, 18 Jul 2022 08:18:18 UTC (140 KB)

 [v4]
 Tue, 11 Apr 2023 12:12:39 UTC (141 KB)

 [v5]
 Fri, 16 Feb 2024 09:36:29 UTC (143 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Sparse graphs with bounded induced cycle packing number have logarithmic treewidth, by Marthe Bonamy and 7 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2022-06
 

 Change to browse by:
 
 cs
 cs.DS
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

 export BibTeX citation
 Loading...

 
 
 BibTeX formatted citation

 ×
 

 
 loading...
 

 
 Data provided by: 
 
 

 

 Bookmark

 
 
 
 
 

 

 

 
 Bibliographic Tools
 
 Bibliographic and Citation Tools

 
 
 
 
 
 
 Bibliographic Explorer Toggle
 
 

 
 Bibliographic Explorer (What is the Explorer?)
 

 

 
 
 
 
 
 Connected Papers Toggle
 
 

 
 Connected Papers (What is Connected Papers?)
 

 

 
 
 
 
 Litmaps Toggle
 
 

 
 Litmaps (What is Litmaps?)
 

 

 
 
 
 
 
 scite.ai Toggle
 
 

 
 scite Smart Citations (What are Smart Citations?)
 

 

 

 

 

 

 

 

 
 Code, Data, Media
 
 Code, Data and Media Associated with this Article

 
 
 
 
 
 
 alphaXiv Toggle
 
 

 
 alphaXiv (What is alphaXiv?)
 

 

 
 
 
 
 
 Links to Code Toggle
 
 

 
 CatalyzeX Code Finder for Papers (What is CatalyzeX?)
 

 

 
 
 
 
 
 DagsHub Toggle
 
 

 
 DagsHub (What is DagsHub?)
 

 

 
 
 
 
 
 
 GotitPub Toggle
 
 

 
 Gotit.pub (What is GotitPub?)
 

 

 
 
 
 
 
 Huggingface Toggle
 
 

 
 Hugging Face (What is Huggingface?)
 

 

 
 
 
 
 
 ScienceCast Toggle
 
 

 
 ScienceCast (What is ScienceCast?)
 

 

 

 

 

 

 

 

 

 

 
 Demos
 
 Demos

 
 
 
 
 
 
 Replicate Toggle
 
 

 
 Replicate (What is Replicate?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 Hugging Face Spaces (What is Spaces?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 TXYZ.AI (What is TXYZ.AI?)
 

 

 

 

 

 

 

 
 Related Papers
 
 Recommenders and Search Tools

 
 
 
 
 
 
 Link to Influence Flower
 
 

 
 Influence Flower (What are Influence Flowers?)
 

 

 
 
 
 
 
 Core recommender toggle
 
 

 
 CORE Recommender (What is CORE?)
 

 

 

 
 
 Author

 Venue

 Institution

 Topic

 
 
 

 

 

 

 

 

 

 

 

 
 
 About arXivLabs
 
 
 
 
 arXivLabs: experimental projects with community collaborators

 arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

 Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

 Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

 

 
 

 

 

 

 

 
 Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-5.6-sol`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For each fixed k, MIS on n-vertex graphs with iocp at most k has a deterministic exact 2^{O_k(n^{2/3} log n)}-time algorithm, and becomes polynomial under an additional sparse bounded-odd-cycle-length hypothesis.",
  "would_publish": false,
  "caveats": "This does not give polynomial time in general; it uses the established quantitative half-integral odd-cycle Erdos-Posa theorem, and the literature novelty of the combination was not checked."
}
```

## 1. Interpretation and partial result

I interpret the conjecture as follows.

> **Conjecture.** For every fixed \(k\), Maximum Independent Set is polynomial-time solvable on graphs \(G\) with
> \[
> \operatorname{iocp}(G)\le k,
> \]
> where \(\operatorname{iocp}(G)\) is the largest number of pairwise vertex-disjoint, pairwise anticomplete induced odd cycles in \(G\).

I do not prove the conjecture. I prove two partial results.

### Theorem A: general exact subexponential algorithm

For every fixed \(k\), Maximum Independent Set on \(n\)-vertex graphs with \(\operatorname{iocp}(G)\le k\) can be solved exactly in deterministic time
\[
2^{O_k(n^{2/3}\log n)}.
\]

More generally, if \(G\) has \(n\) vertices and \(m\) edges, there is an exact algorithm with running time
\[
2^{O(P\log(P+2))}n^{O(1)},\qquad
P:=k+\sqrt{k(n+m)}.
\]
Thus, for example, bounded-average-degree graphs with fixed iocp admit an exact
\[
2^{O_k(\sqrt n\log n)}
\]
algorithm.

### Theorem B: a polynomial special case

Fix \(k,L\), and suppose a hereditary graph class satisfies
\[
|E(H)|\le c|V(H)|^{2-\varepsilon}
\]
for constants \(c,\varepsilon>0\) and every induced subgraph \(H\). Then MIS is polynomial-time solvable on members \(G\) of this class satisfying:

1. \(\operatorname{iocp}(G)\le k\), and
2. every induced odd cycle of \(G\) has length at most \(L\).

In particular, for every fixed \(k,s,L\), MIS is polynomial-time solvable on \(K_{s,s}\)-subgraph-free graphs of iocp at most \(k\) whose induced odd cycles have length at most \(L\).

The unrestricted case with arbitrarily long induced odd cycles remains open.

---

## 2. A congestion-two odd-cycle packing

A **half-integral odd-cycle packing** will mean a collection
\[
\mathcal C=(C_1,\dots,C_q)
\]
of odd cycles such that every vertex of \(G\) belongs to at most two members of \(\mathcal C\). The terminology refers to congestion at most two, not to the fractional cycle-packing LP.

Every odd cycle contains an induced odd cycle: take a shortest odd cycle contained in its vertex set; a chord would produce a shorter odd cycle. Consequently, replacing each \(C_i\) by an induced odd cycle contained in it does not increase congestion. We may therefore assume all \(C_i\) are induced.

The key observation is that bounded iocp forces a congestion-two packing to generate many distinct vertices or edges.

### Lemma 2.1: conflict counting

Let \(G\) have \(\operatorname{iocp}(G)\le k\), where \(k\ge1\). Let
\(\mathcal C=(C_1,\dots,C_q)\) be a half-integral packing of induced odd cycles, and let
\[
U=\bigcup_{i=1}^q V(C_i).
\]
Then
\[
\frac{q(q-k)}{2k}\le |U|+4|E(G[U])|.
\]
In particular, if \(G\) has \(n\) vertices and \(m\) edges, then
\[
q\le \frac{k+\sqrt{k^2+8k(n+4m)}}2.
\]

#### Proof

Define a conflict graph \(J\) on \(\{1,\dots,q\}\), joining \(i\) and \(j\) when either

- \(C_i\) and \(C_j\) intersect, or
- there is an edge of \(G\) between \(V(C_i)\) and \(V(C_j)\).

An independent set in \(J\) corresponds to pairwise vertex-disjoint, pairwise anticomplete induced odd cycles. Hence
\[
\alpha(J)\le k.
\]

By Turán's theorem applied to \(\overline J\),
\[
e(J)\ge \binom q2-\left(1-\frac1k\right)\frac{q^2}{2}
      =\frac{q(q-k)}{2k}.
\]

We now upper-bound \(e(J)\).

For each intersecting pair \(C_i,C_j\), choose a common vertex. Since every vertex belongs to at most two cycles of \(\mathcal C\), one vertex can witness at most one unordered intersecting pair. Thus the number of intersecting pairs is at most \(|U|\).

For each remaining adjacent pair, choose an edge \(xy\in E(G[U])\) with
\(x\in C_i\) and \(y\in C_j\). Since \(x\) belongs to at most two cycles and \(y\) belongs to at most two cycles, a fixed edge \(xy\) can witness at most four pairs of cycles. Thus the number of nonintersecting adjacent pairs is at most \(4e(G[U])\).

Consequently,
\[
e(J)\le |U|+4e(G[U]),
\]
which proves the first assertion. Since \(|U|\le n\) and \(e(G[U])\le m\), solving the resulting quadratic inequality gives the second. ∎

---

## 3. From the packing bound to a small odd-cycle transversal

I use the following established form of the half-integral odd-cycle Erdős–Pósa theorem.

> **Half-integral odd-cycle Erdős–Pósa theorem.** There is an absolute constant \(c\) such that every graph \(H\) has an odd-cycle transversal of size at most
> \[
> c\bigl(\nu_{1/2}(H)+1\bigr)\log\bigl(\nu_{1/2}(H)+2\bigr),
> \]
> where \(\nu_{1/2}(H)\) is the maximum cardinality of a half-integral odd-cycle packing.

Here an odd-cycle transversal is a vertex set \(S\) such that \(H-S\) is bipartite.

Combining this theorem with Lemma 2.1 gives:

### Corollary 3.1

If \(G\) has \(n\) vertices, \(m\) edges, and \(\operatorname{iocp}(G)\le k\), then \(G\) has an odd-cycle transversal of size
\[
O\!\left(
 \bigl(k+\sqrt{k(n+m)}\bigr)
 \log\bigl(k+n+m+2\bigr)
\right).
\]

This is useful only when \(G\) is sufficiently sparse; for dense graphs the bound can be linear. The high-degree branching in Section 5 deals with that issue.

---

## 4. Algorithmic use of an odd-cycle transversal

Two standard facts are needed.

### 4.1 Finding a bounded odd-cycle transversal

Given an integer \(t\), Odd Cycle Transversal can be solved in
\[
2^{O(t)}n^{O(1)}
\]
time by iterative compression. For completeness, the compression step can be summarized as follows.

Suppose \(S\) is an odd-cycle transversal of size \(t+1\), and seek one of size at most \(t\). For each vertex of \(S\), guess one of three states:

1. deleted by the new transversal;
2. retained and colored \(0\);
3. retained and colored \(1\).

For a fixed proper coloring of the retained part of \(S\), the graph \(G-S\) is bipartite. Fix a bipartition of it. Neighbors of retained vertices in \(S\) impose one of two possible orientations on components of \(G-S\). A minimum set of vertices outside \(S\) whose deletion separates incompatible orientation demands is a minimum vertex-capacitated cut and is computable by a standard max-flow construction. There are at most \(3^{t+1}\) guesses.

Processing vertices one at a time gives the claimed \(2^{O(t)}n^{O(1)}\) algorithm.

### 4.2 MIS after deleting an odd-cycle transversal

If \(S\) is an odd-cycle transversal, then
\[
\alpha(G)=
\max_{\substack{X\subseteq S\\X\text{ independent}}}
\left(
 |X|+\alpha\bigl(G-(S\cup N_G(X))\bigr)
\right).
\]
The graph inside the final \(\alpha\) is an induced subgraph of \(G-S\), hence bipartite. Its maximum independent set can be found in polynomial time using maximum matching and König's theorem.

Thus MIS can be solved in
\[
2^{|S|}n^{O(1)}
\]
time once \(S\) is known.

Combining this with Corollary 3.1 proves the edge-sensitive part of Theorem A.

---

## 5. The general \(2^{O_k(n^{2/3}\log n)}\) algorithm

Let \(N\) be the number of vertices of the original input and set
\[
D=\lceil N^{1/3}\rceil.
\]

On a current induced subgraph \(H\):

- if \(H\) has a vertex \(v\) of degree at least \(D\), branch using
  \[
  \alpha(H)=
  \max\bigl\{\alpha(H-v),\,1+\alpha(H-N_H[v])\bigr\};
  \]
- otherwise, solve \(H\) using the odd-cycle-transversal algorithm above.

The property \(\operatorname{iocp}(H)\le k\) is hereditary, so it holds at every recursive subproblem.

### Size of the branching tree

A high-degree branch removes respectively at least \(1\) and \(D+1\) vertices. If \(B(r)\) denotes the maximum number of leaves starting from \(r\) vertices, then
\[
B(r)\le B(r-1)+B(r-D-1).
\]
The standard branching-number estimate gives
\[
B(N)=2^{O(N\log D/D)}.
\]
For example, with
\[
\rho=\exp(2\log D/D),
\]
one has \(\rho^{-1}+\rho^{-(D+1)}\le1\) for sufficiently large \(D\), giving \(B(N)\le\rho^N\). Therefore
\[
B(N)=2^{O(N^{2/3}\log N)}.
\]

### Cost at a leaf

Let a leaf graph \(H\) have \(r\le N\) vertices. Since \(\Delta(H)<D\),
\[
|E(H)|\le \frac{rD}{2}.
\]
Lemma 2.1 therefore bounds its maximum half-integral odd-cycle packing by
\[
O\bigl(k+\sqrt{krD}\bigr)
 =O_k(N^{2/3}).
\]
The half-integral Erdős–Pósa theorem gives an odd-cycle transversal of size
\[
O_k(N^{2/3}\log N).
\]
Finding that transversal and solving MIS from it both take
\[
2^{O_k(N^{2/3}\log N)}
\]
time.

Multiplying by the number of leaves proves
\[
T(N)=2^{O_k(N^{2/3}\log N)}.
\]

The algorithm can be made correct on arbitrary inputs, not merely promised ones: at a leaf, increase the odd-cycle-transversal parameter until a transversal is found, eventually reaching \(S=V(H)\). The claimed running-time bound uses the promise \(\operatorname{iocp}(G)\le k\).

---

## 6. Polynomial time when induced odd cycles have bounded length

We now prove Theorem B.

Assume every induced odd cycle has at most \(L\) vertices and every induced subgraph \(F\) satisfies
\[
e(F)\le c|V(F)|^{2-\varepsilon}.
\]

Let \(\mathcal C=(C_1,\dots,C_q)\) be a maximum half-integral packing, shortened so that all cycles are induced. Let \(U\) be their union. Then
\[
|U|\le qL.
\]
Lemma 2.1 gives
\[
\frac{q(q-k)}{2k}
 \le |U|+4e(G[U])
 \le qL+4c(qL)^{2-\varepsilon}.
\]

For \(q\ge2k\), the left side is at least \(q^2/(4k)\). If also \(q\ge8kL\), then \(qL\le q^2/(8k)\), and consequently
\[
\frac{q^2}{8k}
 \le 4cL^{2-\varepsilon}q^{2-\varepsilon}.
\]
Hence
\[
q^\varepsilon\le 32kcL^{2-\varepsilon}.
\]
Thus \(q\) is bounded by a function of \(k,L,c,\varepsilon\), independently of \(|V(G)|\).

The half-integral Erdős–Pósa theorem now supplies an odd-cycle transversal of constant size. Enumerating its intersection with an independent set and solving the remaining bipartite instances gives a polynomial-time algorithm.

For \(K_{s,s}\)-subgraph-free graphs, the Kővári–Sós–Turán bound gives
\[
e(F)=O_s\bigl(|V(F)|^{2-1/s}\bigr),
\]
so one may take \(\varepsilon=1/s\). Bounded-degree and bounded-degeneracy classes are covered as the special case \(\varepsilon=1\).

---

## 7. What remains open

The argument does not yield polynomial time for unrestricted bounded-iocp graphs. Its weak point is exactly the presence of arbitrarily long induced odd cycles. In a half-integral packing, long cycles can distribute the quadratically many required conflicts over a growing number of vertices and edges. The counting argument then gives only a sublinear, rather than constant or polylogarithmic, odd-cycle transversal.

Thus the missing step would need to exploit the cyclic order and parity structure of long induced odd cycles, not merely count their intersections and joining edges.

No NP-hardness construction or counterexample to the conjecture is obtained here. I also have not verified whether the subexponential combination above is already implicit in the algorithmic literature, so I would not submit it without a dedicated novelty search.
