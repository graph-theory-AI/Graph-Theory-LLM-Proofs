Attack the following open graph-theory problem.

Catalog id: choosability_of_graph_powers
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/choosability_of_graph_powers/
Original entry: http://www.openproblemgarden.org/op/choosability_of_graph_powers
Problem attributed to: Noel, Jonathan A. (posted 2013-07-13)

=== Problem statement (OpenProblemGarden) ===
Title: Choosability of Graph Powers
Question (Noel, 2013) Does there exist a function $ f(k)=o(k^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^2\right)\leq f\left(\chi\left(G^2\right)\right)?\]

=== Discussion / context (OpenProblemGarden) ===
For a survey of choosability, including relevant definitions, see [Noe] or click here . The List Square Colouring Conjecture, due to Kostochka and Woodall [KW], states that $ \text{ch}\left(G^2\right) = \chi\left(G^2\right) $ for every graph $ G $ . This was disproved by Kim and Park [KP], who proved that there is a sequence $ \{G_n\}_n $ of graphs and a constant $ c_1 $ such that $ \chi\left(G^2_n\right)\to\infty $ and $ \text{ch}\left(G_n^2\right) \geq c_1 \chi\left(G_n^2\right)\log\left(\chi\left(G_n^2\right)\right) $ for all $ n $ . To obtain this lower bound from the construction of Kim and Park, one can apply the well-known result of Alon [Alo]. It may be the case that the correct upper bound for all graphs is of the same order of magnitude as the example in the result of Kim and Park. Question (Noel, 2013) Does there exist a positive constant $ c_2 $ such that every graph $ G $ satisfies $ \text{ch}\left(G^2\right) \leq c_2\chi\left(G^2\right)\log{\chi\left(G^2\right)} $ ? By calculating the clique number and maximum degree of $ G^2 $ , one can easily show that $ \text{ch}\left(G^2\right)\leq\chi\left(G^2\right)^2 $ (this observation is due to Young Soo Kwon), but it seems that no significantly better bound is known. Proposition If $ G $ contains an edge, then \[\text{ch}\left(G^2\right)< \chi\left(G^2\right)^2.\] Proof We observe the following bounds: \[\chi\left(G^2\right) \geq \omega\left(G^2\right) \geq \Delta(G)+1,\] \[\text{ch}\left(G^2\right) \leq \Delta\left(G^2\right)+1 \leq \Delta(G)\left(\Delta(G)-1\right) + \Delta(G)+1 = \Delta(G)^2+1.\] Therefore, since $ \Delta(G)>0 $ , we have \[\text{ch}\left(G^2\right)\leq \Delta(G)^2+1 < \left(\Delta(G)+1\right)^2 \leq \chi\left(G^2\right)^2.\] This completes the proof. These questions are related to a problem of Zhu (see Doug West's webpage for more info) who asked whether there exists an integer $ k $ such that for every graph $ G $ , we have that $ G^k $ has choice number equal to chromatic number. This conjecture has been disproved independently by Kim, Kwon and Park [KKP] and Kosar, Petrickova, Reigniger and Yeager [KPRY]. The example of [KPRY] also yields, for every $ k $ , a sequence $ \{G_n\}_n $ of graphs and a constant $ c $ such that $ \chi\left(G^k_n\right)\to\infty $ and $ \text{ch}\left(G_n^k\right) \geq c \chi\left(G_n^k\right)\log\left(\chi\left(G_n^k\right)\right) $ for all $ n $ . They ask the following, more general, questions: Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a function $ f_k(x)=o(x^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^k\right)\leq f_k\left(\chi\left(G^k\right)\right)?\] To our knowledge, it is not known whether there exists a function $ f_k(x) = o(x^k) $ such that the same conclusion holds. (Intuitively, it seems that higher values of $ k $ should yield a smaller separation between $ \text{ch}(G^k) $ and $ \chi(G^k) $ ; however, there seems to be no hard evidence to support this.) Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a positive constant $ c_k $ such that every graph $ G $ satisfies $ \text{ch}\left(G^k\right) \leq c_k\chi\left(G^k\right)\log{\chi\left(G^k\right)} $ ? Moreover, can the constant $ c_k $ be made independent of $ k $ ? These questions are also related to the so-called List Total Colouring Conjecture of Borodin, Kostochka and Woodall [BKW], which says that the total graph of a multigraph always satisfies $ \text{ch}=\chi $ . Given a multigraph $ G $ , the total graph of $ G $ can be obtained by subdividing every edge of $ G $ and then taking the square of the resulting graph.

=== References listed by OpenProblemGarden ===
- [Alo] Noga Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.
- [BKW] Oleg V. Borodin, Alexandr V. Kostochka, and Douglas R. Woodall. List edge and list total colourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.
- [KP] Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture, submitted.
- [KKP] Seog-Jin Kim, Young Soo Kwon and Boram Park: Chromatic-choosability of the power of graphs.
- [KPRY] Nicholas Kosar, Sarka Petrickova, Benjamin Reiniger, Elyse Yeager: A note on list-coloring powers of graphs.
- [KW] Alexandr V. Kostochka and Douglas R. Woodall. Choosability conjectures and multicircuits, Discrete Math., 240 (2001), 123--143.
- [Noe] Jonathan A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond, Master's thesis. McGill University (2013). pdf.

=== Catalog page (statement + literature review) ===
Choosability of Graph Powers — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The question of whether $\text{ch}(G^2) \le f(\chi(G^2))$ for some $f = o(k^2)$ remains open. Shortly after the OPG posting, two independent papers (Kim–Kwon–Park and Kosar–Petrickova–Reiniger–Yeager) confirmed that Zhu's related conjecture fails for all powers $k \ge 2$ and that the logarithmic lower bound $\text{ch}(G^k) \ge c\,\chi(G^k)\log\chi(G^k)$ extends to every $k$; KPRY also established $\text{ch}(G^k) < \chi(G^k)^3$ for $k > 1$, but no subquadratic improvement over the quadratic upper bound $\text{ch}(G^2) \le \chi(G^2)^2$ has been established for squares.

 Cited literature (2)

 
 
 
partial Chromatic-choosability of the power of graphs
 (2013)
 

 
 Seog-Jin Kim, Young Soo Kwon, Boram Park · arXiv preprint · arXiv:1309.0888

Independently disproves Zhu's conjecture by showing that for every integer $k \ge 2$ there exists a graph $G$ such that $G^k$ is not chromatic-choosable and the gap $\chi_\ell(G^k)-\chi(G^k)$ can be arbitrarily large.
 

 
 
partial A note on list-coloring powers of graphs
 (2013)
 

 
 Nicholas Kosar, Sarka Petrickova, Benjamin Reiniger, Elyse Yeager · arXiv preprint · arXiv:1309.7705

Extends the logarithmic lower bound to all powers ($\text{ch}(G^k) \ge c\,\chi(G^k)\log\chi(G^k)$ for all $k \ge 2$) and proves the upper bound $\text{ch}(G^k) < \chi(G^k)^3$ for $k > 1$, but does not yield a subquadratic upper bound for squares.
 

 

 Reviewer notes. The Kim–Park arXiv preprint (1305.2566) was submitted May 12 2013, before the OPG posting of July 13 2013, so it is not counted as a post-posting result even though its journal publication (J. Graph Theory, 2015) is later. Both the KKP and KPRY papers appear in the OPG bibliography, indicating the OPG page was updated after initial posting to incorporate them. Six searches were conducted with no evidence of a paper proving a subquadratic upper bound for $\text{ch}(G^2)$; the problem thus appears genuinely open. The 2022 Hasanvand paper (arXiv:2211.00622) addresses the planar/bipartite versions of the List Square Coloring Conjecture but does not establish any bound of the form $\text{ch}(G^2) \le f(\chi(G^2))$ with $f = o(k^2)$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 269s.
 

Question (Noel, 2013). Does there exist a function $ f(k)=o(k^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^2\right)\leq f\left(\chi\left(G^2\right)\right)?\]

Keywords:
choosability · chromatic number · list coloring · square of a graph

Discussion

For a survey of choosability, including relevant definitions, see [Noe] or click here . The List Square Colouring Conjecture, due to Kostochka and Woodall [KW], states that $ \text{ch}\left(G^2\right) = \chi\left(G^2\right) $ for every graph $ G $ . This was disproved by Kim and Park [KP], who proved that there is a sequence $ \{G_n\}_n $ of graphs and a constant $ c_1 $ such that $ \chi\left(G^2_n\right)\to\infty $ and $ \text{ch}\left(G_n^2\right) \geq c_1 \chi\left(G_n^2\right)\log\left(\chi\left(G_n^2\right)\right) $ for all $ n $ . To obtain this lower bound from the construction of Kim and Park, one can apply the well-known result of Alon [Alo]. It may be the case that the correct upper bound for all graphs is of the same order of magnitude as the example in the result of Kim and Park. Question (Noel, 2013) Does there exist a positive constant $ c_2 $ such that every graph $ G $ satisfies $ \text{ch}\left(G^2\right) \leq c_2\chi\left(G^2\right)\log{\chi\left(G^2\right)} $ ? By calculating the clique number and maximum degree of $ G^2 $ , one can easily show that $ \text{ch}\left(G^2\right)\leq\chi\left(G^2\right)^2 $ (this observation is due to Young Soo Kwon), but it seems that no significantly better bound is known. Proposition If $ G $ contains an edge, then \[\text{ch}\left(G^2\right)< \chi\left(G^2\right)^2.\] Proof We observe the following bounds: \[\chi\left(G^2\right) \geq \omega\left(G^2\right) \geq \Delta(G)+1,\] \[\text{ch}\left(G^2\right) \leq \Delta\left(G^2\right)+1 \leq \Delta(G)\left(\Delta(G)-1\right) + \Delta(G)+1 = \Delta(G)^2+1.\] Therefore, since $ \Delta(G)>0 $ , we have \[\text{ch}\left(G^2\right)\leq \Delta(G)^2+1 < \left(\Delta(G)+1\right)^2 \leq \chi\left(G^2\right)^2.\] This completes the proof. These questions are related to a problem of Zhu (see Doug West's webpage for more info) who asked whether there exists an integer $ k $ such that for every graph $ G $ , we have that $ G^k $ has choice number equal to chromatic number. This conjecture has been disproved independently by Kim, Kwon and Park [KKP] and Kosar, Petrickova, Reigniger and Yeager [KPRY]. The example of [KPRY] also yields, for every $ k $ , a sequence $ \{G_n\}_n $ of graphs and a constant $ c $ such that $ \chi\left(G^k_n\right)\to\infty $ and $ \text{ch}\left(G_n^k\right) \geq c \chi\left(G_n^k\right)\log\left(\chi\left(G_n^k\right)\right) $ for all $ n $ . They ask the following, more general, questions: Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a function $ f_k(x)=o(x^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^k\right)\leq f_k\left(\chi\left(G^k\right)\right)?\] To our knowledge, it is not known whether there exists a function $ f_k(x) = o(x^k) $ such that the same conclusion holds. (Intuitively, it seems that higher values of $ k $ should yield a smaller separation between $ \text{ch}(G^k) $ and $ \chi(G^k) $ ; however, there seems to be no hard evidence to support this.) Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a positive constant $ c_k $ such that every graph $ G $ satisfies $ \text{ch}\left(G^k\right) \leq c_k\chi\left(G^k\right)\log{\chi\left(G^k\right)} $ ? Moreover, can the constant $ c_k $ be made independent of $ k $ ? These questions are also related to the so-called List Total Colouring Conjecture of Borodin, Kostochka and Woodall [BKW], which says that the total graph of a multigraph always satisfies $ \text{ch}=\chi $ . Given a multigraph $ G $ , the total graph of $ G $ can be obtained by subdividing every edge of $ G $ and then taking the square of the resulting graph.

Bibliography

 [Alo]
 Noga Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.

 [BKW]
 Oleg V. Borodin, Alexandr V. Kostochka, and Douglas R. Woodall. List edge and list total colourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.

 [KP]
 Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture , submitted.
 Counterexamples to the List Square Coloring Conjecture

 [KKP]
 Seog-Jin Kim, Young Soo Kwon and Boram Park: Chromatic-choosability of the power of graphs .
 Chromatic-choosability of the power of graphs

 [KPRY]
 Nicholas Kosar, Sarka Petrickova, Benjamin Reiniger, Elyse Yeager: A note on list-coloring powers of graphs .
 A note on list-coloring powers of graphs

 [KW]
 Alexandr V. Kostochka and Douglas R. Woodall. Choosability conjectures and multicircuits, Discrete Math., 240 (2001), 123--143.

 [Noe]
 Jonathan A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond, Master's thesis. McGill University (2013). pdf .
 pdf

Related conjectures

 
 related to
 List Total Colouring Conjecture
 open
 The source page explicitly says these questions 'are also related to the so-called List Total Colouring Conjecture'. Both descend from the disproved List Square Colouring Conjecture ch(G^2)=chi(G^2): LTCC is its special case on squares of subdivisions (total graphs), Noel's question is a weakened o(k^2)-bound version for all graphs. No implication either way: a positive answer to Noel's question allows a superlinear gap, far weaker than the exact equality LTCC demands on total graphs; and LTCC, restricted to total graphs, cannot bound ch(G^2) for general G. Explicitly stated relatedness, no derivable implication: related_only.
 

 
 related to
 Total Colouring Conjecture
 partial
 The mention in the source page is actually to the List Total Colouring Conjecture of Borodin, Kostochka and Woodall, not to Behzad's Total Colouring Conjecture; the match to Behzad's page is a name near-miss. A thematic link survives (total graphs are squares of subdivided graphs, so choosability-of-squares questions bear on total colouring), but there is no implication either way: Noel's question asks for an o(k^2) bound on ch(G^2) in terms of chi(G^2), while Behzad's conjecture bounds the chromatic number (not choosability) of total graphs by Delta+2. Neither statement's truth forces the other's.
 

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
  "one_line": "Explicit bounds give subquadratic results for roots of sublinear degeneracy or with subexponential-size blocks, but do not settle the unrestricted question.",
  "would_publish": false,
  "caveats": "These elementary special cases and the logarithmic-gap example are not claimed to be new; no universal subquadratic bound is obtained."
}
```

## 1. A quantitative partial result

All graphs below are finite and simple. Write
\[
k=\chi(G^2),\qquad \Delta=\Delta(G),\qquad d=\operatorname{degeneracy}(G).
\]
Count bridges as two-vertex blocks, and let \(M\) be the maximum number of vertices in a block of \(G\).

The following gives two complementary regimes in which Noel’s question has a positive answer.

**Theorem.** If \(G\) contains an edge, then
\[
\boxed{\quad
\operatorname{ch}(G^2)
\le
\min\left\{
(2d-1)\Delta-d(d-1)+1,\;
\Delta+\left\lceil k\ln M\right\rceil
\right\}.
\quad} \tag{1}
\]

Since \(N_G[v]\) is a clique in \(G^2\), we have \(\Delta\le k-1\). Consequently:

* If \(d=o(k)\), then \(\operatorname{ch}(G^2)=o(k^2)\).
* If \(\ln M=o(k)\), then \(\operatorname{ch}(G^2)=o(k^2)\).
* If \(M\le k^A\), for a fixed constant \(A>0\), then
  \[
  \operatorname{ch}(G^2)\le A k\ln k+k.
  \tag{2}
  \]
  Thus the stronger, conjectured \(O(k\log k)\) estimate holds for roots with polynomial-size blocks, even if the entire graph has arbitrarily many vertices.

The order in (2) is necessary when blocks of quadratic size are allowed; a self-contained example appears in Section 3.

Edgeless nonempty graphs have \(k=\operatorname{ch}(G^2)=1\) and can be handled separately.

## 2. Proof of the upper bounds

### 2.1. The degeneracy bound

Choose an ordering of \(V(G)\) in which every vertex has at most \(d\) later neighbors in \(G\). Fix a vertex \(v\), and let \(p\le d\) be its number of later neighbors in \(G\).

We count vertices later than \(v\) that are adjacent to \(v\) in \(G^2\).

* Direct later neighbors contribute at most \(p\).
* Two-edge paths through a later neighbor of \(v\) contribute at most \(p(\Delta-1)\).
* If a two-edge path \(vwu\) goes through an earlier neighbor \(w\), then \(u\), being later than \(v\), is also later than \(w\). Since \(v\) is one of the at most \(d\) later neighbors of \(w\), there are at most \(d-1\) possible such \(u\).

Hence the number of later neighbors of \(v\) in \(G^2\) is at most
\[
\begin{aligned}
p+p(\Delta-1)+(\deg_G(v)-p)(d-1)
&\le p\Delta+(\Delta-p)(d-1)\\
&\le d\Delta+(\Delta-d)(d-1)\\
&=(2d-1)\Delta-d(d-1).
\end{aligned}
\]
The second inequality uses \(\Delta-d+1>0\).

Greedy list coloring in reverse order therefore gives
\[
\operatorname{ch}(G^2)
\le (2d-1)\Delta-d(d-1)+1.
\tag{3}
\]

Equivalently, the right-hand side is
\[
\Delta^2-(\Delta-d)(\Delta-d+1)+1.
\]
For forests, \(d=1\), and this recovers the exact bound
\(\operatorname{ch}(G^2)=\Delta+1\).

### 2.2. A bounded-order list-coloring lemma

**Lemma.** Every \(k\)-colorable graph \(H\) on \(n\ge1\) vertices satisfies
\[
\operatorname{ch}(H)\le \left\lceil k\ln n\right\rceil+1.
\tag{4}
\]

**Proof.** Fix a proper coloring with color classes \(V_1,\ldots,V_k\), and give each vertex a list of
\[
\ell=\left\lceil k\ln n\right\rceil+1
\]
colors.

Independently assign every color appearing in the lists to one of \(k\) palettes, uniformly at random. A vertex in \(V_i\) has no listed color in palette \(i\) with probability
\[
(1-1/k)^\ell\le e^{-\ell/k}.
\]
The probability that any vertex fails is at most
\[
n e^{-\ell/k}<1.
\]
Thus some palette assignment gives each vertex of \(V_i\) a listed color in palette \(i\). Choosing one such color at every vertex gives a proper coloring. \(\square\)

### 2.3. Localizing the problem to blocks

The useful point is that the bounded-order lemma need only be applied to individual blocks, not to the entire graph.

**Block lemma.** If \(G\) contains an edge, then
\[
\operatorname{ch}(G^2)
\le
\Delta(G)-1+
\max_{B\text{ a block of }G}\operatorname{ch}(B^2).
\tag{5}
\]

**Proof.** Put
\[
b=\max_B\operatorname{ch}(B^2).
\]
In particular, \(b\ge2\). If \(\Delta=1\), the assertion is immediate. Assume \(\Delta\ge2\), and consider lists of size
\[
L=\Delta-1+b.
\]

Work component by component. Root the block-cut tree of a component at a block and process blocks with parents before children. Color the root block first.

A subsequent block \(B\) meets the previously colored part in exactly its parent articulation vertex \(a\). Moreover:

1. every path from \(B-\{a\}\) to the previously colored part passes through \(a\);
2. \(G^2[V(B)]=B^2\), since a path outside \(B\) cannot connect two distinct vertices of \(B\).

Suppose first that \(B\) is not a bridge. Then \(\deg_B(a)\ge2\). For a new vertex \(v\in B-\{a\}\):

* If \(v\) is adjacent to \(a\), its previously colored square-neighbors are among \(a\) and the previously colored neighbors of \(a\). Their number is at most
  \[
  1+\Delta-\deg_B(a)\le\Delta-1.
  \]
* If \(v\) is not adjacent to \(a\), its only possible previously colored square-neighbor is \(a\), again giving at most \(\Delta-1\).

Delete the colors on these previously colored square-neighbors. Every new vertex retains at least \(b\) colors, so \(B^2-\{a\}\) can be list-colored.

If \(B\) is a bridge \(av\), only \(v\) is new. It has at most \(\Delta\) previously colored square-neighbors. Since \(L\ge\Delta+1\), at least one color remains for \(v\).

Continuing in this way colors \(G^2\). \(\square\)

For every block \(B\), the graph \(B^2\) is \(k\)-colorable and has at most \(M\) vertices. Applying (4) and then (5) gives
\[
\operatorname{ch}(G^2)
\le \Delta-1+\left(\left\lceil k\ln M\right\rceil+1\right)
=\Delta+\left\lceil k\ln M\right\rceil.
\]
Together with (3), this proves (1).

## 3. The polynomial-block-size result is order-sharp

Here is a self-contained construction exhibiting
\[
|V(G)|=O(k^2),
\qquad
\chi(G^2)=k,
\qquad
\operatorname{ch}(G^2)=\Omega(k\log k).
\]
This reproduces the logarithmic-gap phenomenon in the question; it does **not** disprove the requested subquadratic bound.

### 3.1. A complete multipartite list lower bound

Let \(K_{r\times r}\) denote the complete \(r\)-partite graph with \(r\) vertices in each part. For all sufficiently large \(r\),
\[
\operatorname{ch}(K_{r\times r})
>
\frac{r\log_2 r}{16}.
\tag{6}
\]

To prove this, set
\[
\ell=\left\lfloor\frac{r\log_2 r}{16}\right\rfloor,
\qquad m=2\ell.
\]
Independently give each vertex a uniformly random \(\ell\)-element list from a common \(m\)-color set.

In a proper coloring, no color can be used in two different parts. Thus any proper list coloring determines a partition
\[
S_1,\ldots,S_r
\]
of the color set such that every list in part \(i\) meets \(S_i\). Unused colors can be assigned arbitrarily to complete the partition.

Fix such a partition. At least \(r/2\) of its sets have size at most \(2m/r\). For one of these sets, of size \(s\), and \(r\ge8\),
\[
\begin{aligned}
\Pr(L(v)\cap S_i=\varnothing)
&=\frac{\binom{m-s}{\ell}}{\binom m\ell}\\
&=\prod_{j=0}^{s-1}\frac{m/2-j}{m-j}\\
&\ge 4^{-s}\\
&\ge 4^{-2m/r}
\ge r^{-1/2}.
\end{aligned}
\]
The product estimate uses \(s\le m/4\).

There are at least \(r^2/2\) vertices in these small-palette parts. Consequently, the probability that this fixed partition meets all their lists is at most
\[
(1-r^{-1/2})^{r^2/2}
\le e^{-r^{3/2}/2}.
\]
There are at most \(r^m\) partitions. Therefore the probability that any partition works is at most
\[
\exp\left(
\frac{r(\ln r)^2}{8\ln2}-\frac{r^{3/2}}2
\right)<1
\]
for all sufficiently large \(r\). Some \(\ell\)-list assignment is therefore uncolorable, proving (6).

### 3.2. A square containing \(K_{q\times q}\)

Let \(q\) be a prime. Construct a bipartite graph \(G_q\) with parts
\[
P=\{(x,y):x,y\in\mathbb F_q\},
\qquad
\mathcal L=\{[a,b]:a,b\in\mathbb F_q\},
\]
where
\[
(x,y)\sim[a,b]\quad\Longleftrightarrow\quad y=ax+b.
\]
Thus \(P\) consists of affine points and \(\mathcal L\) of nonvertical affine lines. The graph has \(2q^2\) vertices and is \(q\)-regular.

Put \(H_q=G_q^2\).

* Two points are adjacent in \(H_q\) exactly when their \(x\)-coordinates differ. Hence
  \[
  H_q[P]\cong K_{q\times q}.
  \]
* Two line vertices are adjacent exactly when their slopes differ.
* Between \(P\) and \(\mathcal L\), the edges of \(H_q\) are precisely the original incidence edges.

Coloring points by \(x\)-coordinate and lines by slope, using disjoint palettes, gives
\[
\chi(H_q)\le2q.
\]

Conversely, an independent set contains points from at most one vertical column and lines from at most one parallel class. Between any such column and parallel class, incidence is a perfect matching. Thus every independent set has size at most \(q\). Since \(H_q\) has \(2q^2\) vertices,
\[
\chi(H_q)\ge2q.
\]
Therefore
\[
\chi(H_q)=2q.
\tag{7}
\]

By (6),
\[
\operatorname{ch}(H_q)
\ge \operatorname{ch}(K_{q\times q})
=\Omega(q\log q).
\]
Writing \(k=2q\), we obtain
\[
|V(G_q)|=\frac{k^2}{2},
\qquad
\operatorname{ch}(G_q^2)=\Omega(k\log k).
\]
Together with (2), this establishes the sharp order \(k\log k\) in the class allowing blocks of order \(O(k^2)\).

## 4. What an unresolved obstruction must look like

The upper bounds impose quantitative conditions on any putative quadratic-gap sequence.

Suppose, for a fixed \(\varepsilon>0\),
\[
\operatorname{ch}(G^2)\ge\varepsilon k^2.
\]
From (1),
\[
\operatorname{ch}(G^2)\le 2d(k-1)+1,
\]
so
\[
d\ge \frac{\varepsilon k^2-1}{2(k-1)}.
\tag{8}
\]
Also,
\[
\operatorname{ch}(G^2)
\le \Delta+\lceil k\ln M\rceil
\le k\ln M+k,
\]
and consequently
\[
M\ge \exp(\varepsilon k-1).
\tag{9}
\]
Thus a quadratic-gap sequence would require both linear-in-\(k\) degeneracy and exponentially large blocks.

There is also a useful normalization showing that regular roots cannot simply be avoided.

**Regular-completion lemma.** Every \(G\) with \(\chi(G^2)=k\ge2\) is a subgraph of a graph \(F\) such that
\[
F\text{ is }(k-1)\text{-regular},
\qquad
\chi(F^2)=k,
\qquad
\operatorname{ch}(G^2)\le\operatorname{ch}(F^2).
\tag{10}
\]

**Proof.** Fix a proper \(k\)-coloring of \(G^2\), with classes \(V_1,\ldots,V_k\). Between any two classes, the edges of \(G\) form a matching: otherwise two vertices of one class would have a common neighbor.

Add isolated vertices to make all classes the same size. For every pair of classes, complete the existing matching to a perfect matching.

The resulting graph \(F\) has exactly one neighbor in every other class at each vertex, so it is \((k-1)\)-regular. The same classes properly color \(F^2\): no vertex has two neighbors in one class. Every closed neighborhood in \(F\) is a \(k\)-clique in \(F^2\), so \(\chi(F^2)=k\). Finally, \(G^2\) is a subgraph of \(F^2\), giving the choice-number inequality. \(\square\)

These \(F\) are finite covers of \(K_k\). In this normalized family, \(d=k-1\), and the degeneracy estimate returns exactly the original quadratic scale. The block-size estimate helps only when the blocks are not too large.

**Remaining gap.** I do not obtain an \(o(k^2)\) estimate for arbitrarily large regular covers of \(K_k\). The small-block palette argument cannot simply be made local: its random variables are colors, and lists at vertices arbitrarily far apart may share those colors. No bounded-dependency argument has been established here. Thus neither Noel’s unrestricted question nor its \(O(k\log k)\) strengthening is settled by these results.
