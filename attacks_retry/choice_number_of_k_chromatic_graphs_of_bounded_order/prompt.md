Attack the following open graph-theory problem.

Catalog id: choice_number_of_k_chromatic_graphs_of_bounded_order
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/choice_number_of_k_chromatic_graphs_of_bounded_order/
Original entry: http://www.openproblemgarden.org/op/choice_number_of_k_chromatic_graphs_of_bounded_order
Problem attributed to: Noel, Jonathan A. (posted 2013-02-02)

=== Problem statement (OpenProblemGarden) ===
Title: Choice Number of k-Chromatic Graphs of Bounded Order
Conjecture If $ G $ is a $ k $ -chromatic graph on at most $ mk $ vertices, then $ \text{ch}(G)\leq \text{ch}(K_{m*k}) $ .

=== Discussion / context (OpenProblemGarden) ===
For integers $ m,k\geq1 $ , let $ K_{m*k} $ denote the complete $ k $ -partite graph in which every part has size $ m $ . In one of the original papers on choosability, Erdos, Rubin and Taylor [ERT] proved that $ \text{ch}(K_{2*k})=k $ . Later, Ohba [Ohba] conjectured the following generalization: if $ |V(G)|\leq 2\chi(G)+1 $ , then TeX Embedding failed! .} This was proved by Noel, Reed and Wu [NRW12]. Theorem (Noel, Reed and Wu 2012) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \text{ch}(G)=\chi(G) $ . The above theorem implies that the above conjecture holds for $ m=2 $ . That is, if $ G $ is a $ k $ -chromatic graph on at most $ 2k $ vertices (in fact, at most $ 2k+1 $ vertices), then $ \text{ch}(G)=k=\text{ch}(K_{2*k}) $ . Kierstead [Kie00] proved that $ \text{ch}(K_{3*k})=\left\lceil\frac{4k-1}{3}\right\rceil $ . This was generalized by Noel, West, Wu and Zhu [NWWZ13] to the following: Theorem (Noel, West, Wu and Zhu 2013) For every graph $ G $ , \[\text{ch}(G)\leq\max\left\{\chi(G),\left\lceil\frac{|V(G)|+\chi(G)-1}{3}\right\rceil\right\}.\] Therefore, if $ G $ is a $ k $ -chromatic graph on at most $ 3k $ vertices, then $ \text{ch}(G)\leq \left\lceil\frac{4k-1}{3}\right\rceil=\text{ch}(K_{3*k}) $ . This shows that the conjecture is true for $ m=3 $ . Recently, Kierstead, Salmon and Wang [KSW14] proved the following: Theorem (Kierstead, Salmon and Wang 2014) $ \text{ch}(K_{4*k})=\left\lceil\frac{3k-1}{2}\right\rceil $ . However, it is not known whether the upper bound of $ \left\lceil\frac{3k-1}{2}\right\rceil $ holds for all $ k $ -chromatic graphs on at most $ 4k $ vertices. If true, it would verify the conjecture for $ m=4 $ . The following is a refinement of the conjecture. Conjecture (Noel 2013) For $ n\geq k\geq 1 $ there is a graph $ G_{n,k} $ such that \item $ G_{n,k} $ is a complete $ k $ -partite graph on $ n $ vertices, \item the stability number of $ G_{n,k} $ is $ \left\lceil n/k\right\rceil $ , and \item every $ k $ -chromatic graph $ G $ on at most $ n $ vertices satisfies $ \text{ch}(G)\leq \text{ch}(G_{n,k}) $ .

=== References listed by OpenProblemGarden ===
- [Alo92] N. Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.
- [ERT80] P. Erdos, A. L. Rubin, and H. Taylor. Choosability in graphs. Congress. Numer., XXVI, pages 125–157, 1980.
- [Kie00] H. A. Kierstead. On the choosability of complete multipartite graphs with part size three. Discrete Math., 211(1-3):255–259, 2000.
- [KSW14] H. A. Kierstead, A. Salmon and R. Wang. On the Choice Number of Complete Multipartite Graphs With Part Size Four.
- *[Noe13] J. A. Noel. Choosability of Graphs With Bounded Order: Ohba's Conjecture and Beyond. Master's thesis, McGill University, Montreal. pdf
- [NRW12] J. A. Noel, B. A. Reed, and H. Wu. A Proof of a Conjecture of Ohba. Preprint, arXiv:1211.1999v1, November 2012. Webpage
- [NWWZ13] J. A. Noel, D. B. West, H. Wu, and X. Zhu. Beyond Ohba's Conjecture: A bound on the choice number of -chromatic graphs with vertices. Preprint, arXiv:1308.6739v1, August 2013. pdf
- [Ohb02] K. Ohba. On chromatic-choosable graphs. J. Graph Theory, 40(2):130–135, 2002.
- [Yan03] D. Yang. Extension of the game coloring number and some results on the choosability of complete multipartite graphs. PhD thesis, Arizona State University, Tempe, Arizona, 2003.

=== Catalog page (statement + literature review) ===
Choice Number of k-Chromatic Graphs of Bounded Order — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture has been verified for $m = 2$ (before posting) and $m = 3$ (proved by Noel, West, Wu, and Zhu in 2013, published 2015). Kierstead, Salmon, and Wang determined $\text{ch}(K_{4*k}) = \lceil(3k-1)/2\rceil$ in 2014, establishing what the bound should be for $m = 4$, but the general upper bound $\text{ch}(G) \leq \lceil(3k-1)/2\rceil$ for all $k$-chromatic graphs on at most $4k$ vertices (and the full conjecture for $m \geq 4$) remains open.

 Cited literature (2)

 
 
 
partial Beyond Ohba's Conjecture: A bound on the choice number of k-chromatic graphs with n vertices
 (2015)
 

 
 Jonathan A. Noel, Douglas B. West, Hehui Wu, Xuding Zhu · European Journal of Combinatorics · arXiv:1308.6739 · doi:10.1016/j.ejc.2014.08.032

Proves that ch(G) ≤ max{χ(G), ⌈(|V(G)|+χ(G)-1)/3⌉} for every graph G, which implies the conjecture for m=3: every k-chromatic graph on at most 3k vertices satisfies ch(G) ≤ ⌈(4k-1)/3⌉ = ch(K_{3*k}).
 

 
 
partial On the choice number of complete multipartite graphs with part size four
 (2014)
 

 
 H. A. Kierstead, Andrew Salmon, Ran Wang · arXiv preprint · arXiv:1407.3817

Proves that ch(K_{4*k}) = ⌈(3k-1)/2⌉, determining the target bound for the m=4 case of the conjecture, but does not establish this upper bound for all k-chromatic graphs on at most 4k vertices.
 

 

 Reviewer notes. The m=2 and m=3 cases of the conjecture are settled (m=2 follows from the proof of Ohba's conjecture; m=3 from NWWZ13/2015). The m=4 case reduces to showing ch(G) ≤ ⌈(3k-1)/2⌉ for all k-chromatic G on ≤4k vertices, which is explicitly stated as open in the OPG discussion. No papers resolving m=4 or any m≥5 case were found in exhaustive searching through 2025. Jonathan Noel's recent arXiv profile returned only unrelated work (bootstrap percolation), and his university homepage was unreachable. The KSW14 paper's journal publication venue could not be confirmed from verified sources (ADS shows only arXiv preprint).

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 231s.
 

Conjecture. If $ G $ is a $ k $ -chromatic graph on at most $ mk $ vertices, then $ \text{ch}(G)\leq \text{ch}(K_{m*k}) $ .

Keywords:
choosability · complete multipartite graph · list coloring

Discussion

For integers $ m,k\geq1 $ , let $ K_{m*k} $ denote the complete $ k $ -partite graph in which every part has size $ m $ . In one of the original papers on choosability, Erdos, Rubin and Taylor [ERT] proved that $ \text{ch}(K_{2*k})=k $ . Later, Ohba [Ohba] conjectured the following generalization: if $ |V(G)|\leq 2\chi(G)+1 $ , then TeX Embedding failed! .} This was proved by Noel, Reed and Wu [NRW12]. Theorem (Noel, Reed and Wu 2012) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \text{ch}(G)=\chi(G) $ . The above theorem implies that the above conjecture holds for $ m=2 $ . That is, if $ G $ is a $ k $ -chromatic graph on at most $ 2k $ vertices (in fact, at most $ 2k+1 $ vertices), then $ \text{ch}(G)=k=\text{ch}(K_{2*k}) $ . Kierstead [Kie00] proved that $ \text{ch}(K_{3*k})=\left\lceil\frac{4k-1}{3}\right\rceil $ . This was generalized by Noel, West, Wu and Zhu [NWWZ13] to the following: Theorem (Noel, West, Wu and Zhu 2013) For every graph $ G $ , \[\text{ch}(G)\leq\max\left\{\chi(G),\left\lceil\frac{|V(G)|+\chi(G)-1}{3}\right\rceil\right\}.\] Therefore, if $ G $ is a $ k $ -chromatic graph on at most $ 3k $ vertices, then $ \text{ch}(G)\leq \left\lceil\frac{4k-1}{3}\right\rceil=\text{ch}(K_{3*k}) $ . This shows that the conjecture is true for $ m=3 $ . Recently, Kierstead, Salmon and Wang [KSW14] proved the following: Theorem (Kierstead, Salmon and Wang 2014) $ \text{ch}(K_{4*k})=\left\lceil\frac{3k-1}{2}\right\rceil $ . However, it is not known whether the upper bound of $ \left\lceil\frac{3k-1}{2}\right\rceil $ holds for all $ k $ -chromatic graphs on at most $ 4k $ vertices. If true, it would verify the conjecture for $ m=4 $ . The following is a refinement of the conjecture. Conjecture (Noel 2013) For $ n\geq k\geq 1 $ there is a graph $ G_{n,k} $ such that \item $ G_{n,k} $ is a complete $ k $ -partite graph on $ n $ vertices, \item the stability number of $ G_{n,k} $ is $ \left\lceil n/k\right\rceil $ , and \item every $ k $ -chromatic graph $ G $ on at most $ n $ vertices satisfies $ \text{ch}(G)\leq \text{ch}(G_{n,k}) $ .

Bibliography

 [Alo92]
 N. Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.

 [ERT80]
 P. Erdos, A. L. Rubin, and H. Taylor. Choosability in graphs. Congress. Numer., XXVI, pages 125–157, 1980.

 [Kie00]
 H. A. Kierstead. On the choosability of complete multipartite graphs with part size three. Discrete Math., 211(1-3):255–259, 2000.

 [KSW14]
 H. A. Kierstead, A. Salmon and R. Wang. On the Choice Number of Complete Multipartite Graphs With Part Size Four .
 On the Choice Number of Complete Multipartite Graphs With Part Size Four

★ [Noe13]
 J. A. Noel. Choosability of Graphs With Bounded Order: Ohba's Conjecture and Beyond. Master's thesis, McGill University, Montreal. pdf
 pdf

 [NRW12]
 J. A. Noel, B. A. Reed, and H. Wu. A Proof of a Conjecture of Ohba. Preprint, arXiv:1211.1999v1, November 2012. Webpage
 Webpage

 [NWWZ13]
 J. A. Noel, D. B. West, H. Wu, and X. Zhu. Beyond Ohba's Conjecture: A bound on the choice number of $ k $ -chromatic graphs with $ n $ vertices. Preprint, arXiv:1308.6739v1, August 2013. pdf
 pdf

 [Ohb02]
 K. Ohba. On chromatic-choosable graphs. J. Graph Theory, 40(2):130–135, 2002.

 [Yan03]
 D. Yang. Extension of the game coloring number and some results on the choosability of complete multipartite graphs. PhD thesis, Arizona State University, Tempe, Arizona, 2003.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained argument establishes the conjecture up to a factor 1+O(log log m/log m), uniformly in k, but does not prove the exact inequality.",
  "would_publish": false,
  "caveats": "No resolution for fixed m≥4; no novelty claim is made for the asymptotic result."
}
```

## 1. A uniform asymptotic version

Write
\[
M(m,k)=\max\{\operatorname{ch}(G):\chi(G)=k,\ |V(G)|\le mk\}.
\]
The conjecture is precisely
\[
M(m,k)=\operatorname{ch}(K_{m*k}).
\]

I obtain the following partial result. All logarithms below are natural.

**Theorem.** Let \(m\ge1\) and \(k\ge2\) be integers, and put
\[
\lambda_k=\log\frac{k}{k-1}.
\]
Then
\[
M(m,k)\le
\left\lceil\frac{\log m+3}{\lambda_k}\right\rceil. \tag{1}
\]
Moreover, if \(L=\log m\ge20\), then
\[
\operatorname{ch}(K_{m*k})
>
\frac{L-2\log L-\log\log L-8}{\lambda_k}. \tag{2}
\]

Consequently,
\[
1\le
\frac{M(m,k)}{\operatorname{ch}(K_{m*k})}
\le
\frac{L+4}{L-2\log L-\log\log L-8}
=
1+O\!\left(\frac{\log\log m}{\log m}\right), \tag{3}
\]
where the implicit constant is independent of \(k\).

Thus, for every \(\varepsilon>0\), the conjectured inequality holds with a multiplicative factor \(1+\varepsilon\) for all sufficiently large \(m\), **simultaneously for every \(k\)**. The case \(k=1\) holds exactly.

The proof is self-contained. I do not claim that this asymptotic statement is new.

## 2. The exact extremal reduction

Given a proper \(k\)-coloring of \(G\), add all edges between different color classes. If necessary, add vertices to the classes until the order is \(mk\). This produces a complete \(k\)-partite supergraph, without decreasing the choice number.

Hence
\[
M(m,k)=
\max_{\substack{n_1,\dots,n_k\ge1\\n_1+\cdots+n_k=mk}}
\operatorname{ch}(K_{n_1,\dots,n_k}).
\]
The unresolved issue is therefore genuinely one of balancing the part sizes. The upper bound below does not assume that the color classes are balanced.

## 3. Proof of the upper bound

Fix a \(k\)-chromatic graph \(G\) of order at most \(mk\), together with a proper coloring
\[
V(G)=V_1\cup\cdots\cup V_k.
\]
Set
\[
q=\left\lceil\frac{\log m+3}{\lambda_k}\right\rceil.
\]
Consider an arbitrary list assignment in which every list has exactly \(q\) colors.

We use
\[
k-1\le \frac1{\lambda_k}\le k. \tag{4}
\]
In particular, \(q\ge k\).

### The cases \(k=2,3\)

Independently assign every color appearing in the lists to one of \(k\) bins, uniformly. Call a vertex \(v\in V_i\) bad if its list contains no color from bin \(i\).

The expected number of bad vertices is at most
\[
mk\left(1-\frac1k\right)^q
\le k e^{-3}<1.
\]
Thus there is an assignment with no bad vertices. Color every vertex of \(V_i\) using a color from bin \(i\). This is proper.

### The cases \(k\ge4\)

Introduce a reserve bin. Independently assign each color to:

- the reserve bin with probability \(\rho=k/q\);
- each of the \(k\) ordinary bins with probability \((1-\rho)/k\).

Again, \(v\in V_i\) is bad if its list misses ordinary bin \(i\). Write
\[
\beta=1-\frac{1-\rho}{k}.
\]
If \(B\) is the number of bad vertices, then
\[
\mathbb E B\le mk\beta^q.
\]
Since
\[
\log\beta
=
-\lambda_k+\log\left(1+\frac{\rho}{k-1}\right)
\le-\lambda_k+\frac{\rho}{k-1},
\]
we have
\[
q\log\beta
\le-(\log m+3)+\frac{k}{k-1}
\le-\log m-\frac53.
\]
Therefore
\[
\mathbb E B\le k e^{-5/3}. \tag{5}
\]

For a vertex \(v\), let \(R_v\) count the reserve colors in its list. Conditional on \(v\) being bad, its list colors remain independent, and
\[
R_v\sim\operatorname{Bin}\left(q,\frac{\rho}{\beta}\right).
\]
The conditional mean is
\[
\mu=\frac{q\rho}{\beta}=\frac{k}{\beta}\ge k.
\]
The elementary binomial lower-tail bound gives
\[
\Pr(R_v<k/2\mid v\text{ is bad})
\le e^{-k/8}.
\]
Consequently,
\[
\Pr(\exists\text{ bad }v\text{ with }R_v<k/2)
\le k e^{-5/3-k/8}. \tag{6}
\]
Also, by Markov's inequality,
\[
\Pr(B>k/2)\le2e^{-5/3}. \tag{7}
\]
Combining (6) and (7), the probability that either undesirable event occurs is at most
\[
e^{-5/3}\left(2+k e^{-k/8}\right)
\le
e^{-5/3}\left(2+\frac8e\right)
<1.
\]

Choose an outcome avoiding both events. Color all nonbad vertices from their respective ordinary bins. There are at most \(\lfloor k/2\rfloor\) bad vertices, and each has at least \(\lceil k/2\rceil\) reserve colors. They can therefore be given pairwise distinct reserve colors greedily.

Ordinary-bin colors do not conflict across color classes, and reserve colors were not used on nonbad vertices. This proves (1).

## 4. A list obstruction from hitting sets

We next construct lower bounds for the balanced graph.

Suppose that \(\mathcal F=(A_1,\dots,A_m)\) is a family of \(q\)-element subsets of a palette of \(N\) colors, and every set meeting all members of \(\mathcal F\) has size at least \(r\).

Assign the lists \(A_1,\dots,A_m\) to the \(m\) vertices in each part of \(K_{m*k}\). In any proper list coloring:

- the colors used in each part meet every member of \(\mathcal F\), so there are at least \(r\) of them;
- different parts use disjoint sets of colors.

It follows that this assignment is uncolorable whenever
\[
kr>N. \tag{8}
\]

We will also use a scaling observation. Replace each palette color by \(\ell\) distinct clones, and replace each list by all clones of its colors. List sizes and palette size are multiplied by \(\ell\), but the minimum size of a hitting set remains at least \(r\): projecting a hitting set onto the original colors gives a hitting set for \(\mathcal F\).

## 5. Constructing the obstruction

Assume \(L=\log m\ge20\), and define
\[
r=\lceil L^2\rceil,\qquad b=\lceil L\rceil,\qquad
T=L-2\log L-\log\log L-6.
\]
Here \(T>2\).

We first prove that, for every integer \(2\le j\le b^2\), there are \(m\) lists of size
\[
q=\left\lfloor\frac{T}{\lambda_j}\right\rfloor
\]
on a palette of
\[
N=jr-1
\]
colors, with no hitting set of size \(r-1\).

Choose the \(m\) lists independently and uniformly from the \(q\)-subsets of the palette. Repeated lists are allowed.

Fix an \((r-1)\)-subset \(S\). The probability that one random list avoids \(S\) is
\[
p=
\frac{\binom{(j-1)r}{q}}{\binom{jr-1}{q}}
=
\prod_{i=0}^{q-1}\frac{(j-1)r-i}{jr-1-i}. \tag{9}
\]
The binomial coefficients are well-defined: by (4),
\[
q\le jL\le (j-1)r.
\]

Put \(a=(j-1)/j\). Each factor in (9) satisfies
\[
\frac{(j-1)r-i}{jr-1-i}
=
a\left(1+\frac{j-1-i}{(j-1)(N-i)}\right)
\ge
a\left(1-\frac{i}{(j-1)(N-i)}\right).
\]
Also,
\[
N-q\ge \frac{jL^2}{2},
\qquad
\frac{i}{(j-1)(N-i)}
\le\frac{2}{(j-1)L}\le\frac12.
\]
Using \(\log(1-x)\ge-2x\) for \(0\le x\le1/2\), we obtain
\[
\begin{aligned}
\log p
&\ge q\log a
-\frac{q(q-1)}{(j-1)(N-q)}\\
&\ge-q\lambda_j-4.
\end{aligned}
\]
Since \(q\lambda_j\le T\),
\[
mp\ge m e^{-T-4}=e^2L^2\log L. \tag{10}
\]

On the other hand, the number of candidate hitting sets satisfies
\[
\log\binom{N}{r-1}
\le r\log(2ej)
\le6L^2\log L. \tag{11}
\]
For the last inequality, use \(r\le2L^2\), \(j\le\lceil L\rceil^2\), and
\(\log(2e\lceil L\rceil^2)\le3\log L\) for \(L\ge20\).

A fixed \(S\) meets all \(m\) lists with probability
\[
(1-p)^m\le e^{-mp}.
\]
Thus (10), (11), and the union bound show that the probability of any hitting set of size \(r-1\) is at most
\[
\exp\left((6-e^2)L^2\log L\right)<1.
\]
The required family therefore exists.

By (8), this immediately yields
\[
\operatorname{ch}(K_{m*j})
\ge q+1
>
\frac{T}{\lambda_j},
\qquad 2\le j\le b^2. \tag{12}
\]

## 6. Extending the lower bound to every \(k\)

It remains to cover \(k>b^2\).

Use the family just constructed for \(j=b\). Its lists have size
\[
q_0=\left\lfloor\frac{T}{\lambda_b}\right\rfloor,
\]
its palette has \(br-1\) colors, and every hitting set has size at least \(r\).

Let
\[
\ell=\left\lfloor\frac{k}{b}\right\rfloor.
\]
Clone each color \(\ell\) times. The resulting lists have size \(\ell q_0\), and the palette has
\[
\ell(br-1)\le kr-1
\]
colors. The hitting-set obstruction gives
\[
\operatorname{ch}(K_{m*k})\ge\ell q_0+1. \tag{13}
\]

By (4),
\[
q_0\ge(b-1)T-1,
\qquad
\ell\ge k/b-1.
\]
Using \(k>b^2\), expansion of these inequalities gives
\[
\ell q_0+1
>
k\left(T-\frac{2T+1}{b}\right).
\]
Since \(T\le L-6\) and \(b\ge L\), we have \(2T+1<2b\). Hence
\[
\operatorname{ch}(K_{m*k})
>
k(T-2)
\ge\frac{T-2}{\lambda_k}.
\]
Together with (12), this proves, for every \(k\ge2\),
\[
\operatorname{ch}(K_{m*k})
>
\frac{L-2\log L-\log\log L-8}{\lambda_k},
\]
which is (2).

Finally, \(\lambda_k\le\log2<1\), so (1) implies
\[
M(m,k)\le\frac{L+4}{\lambda_k}.
\]
Dividing by (2) proves (3).

## 7. What remains unresolved

The partial result gives the explicit additive estimate
\[
0\le M(m,k)-\operatorname{ch}(K_{m*k})
<
\frac{2\log L+\log\log L+11}{\lambda_k}+1,
\qquad L=\log m\ge20.
\]
Since \(1/\lambda_k=\Theta(k)\), the possible gap here is still of order
\(k\log\log m\).

That gap cannot be discarded when the desired statement is an exact integer inequality. In particular, this argument provides **no resolution of the \(m=4\) case**. It establishes asymptotic extremality of the balanced graph, not the required exact balancing principle.
