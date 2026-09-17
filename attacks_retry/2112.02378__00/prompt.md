Attack the following open graph-theory problem.

Catalog id: 2112.02378__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2112.02378__00/
Source paper: Quasiplanar Graphs, String Graphs, and the Erdos-Gallai Problem (arXiv:2112.02378)

=== Catalog page (statement + literature review) ===
Linear K_{r-1}-free subgraph in K_r-free segment graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 1.2 asks whether every K_r-free segment graph on n vertices contains an induced K_{r-1}-free subgraph on \Omega_r(n) vertices. The source paper (Fox–Pach–Suk 2022) establishes analogous results for string graphs with a log^2(n) factor loss (Theorems 1.5–1.6), but the segment-graph case with a linear guarantee remains explicitly unresolved. A wide search of the post-2022 literature found no paper resolving the segment-graph case; the conjecture is open with high confidence.

 Reviewer notes. The closest post-2022 work found is arXiv:2409.06650 ('Induced Subgraphs of K_r-Free Graphs and the Erdős–Rogers Problem', Combinatorica 2025), which studies the Erdős–Rogers problem for general (non-geometric) K_r-free graphs; it does not address segment graphs and does not cite 2112.02378. No paper specifically resolving Problem 1.2 for segment graphs was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Fix an integer $r \geq 4$. Is it true that every $K_r$-free segment graph on $n$ vertices has an induced subgraph on $\Omega_r(n)$ vertices which is $K_{r-1}$-free?

Context

Motivated by the approach of coloring $K_r$-free string graphs to prove Conjecture 1.1: if each color class could be made $K_4$-free, Ackerman's result would bound the edges per class by $O(n)$. Although Krawczyk–Walczak showed $K_r$-free string graphs can require $\Omega_r(\log\log n)$ colors with $K_{r-1}$-free classes, the question of finding a linearly large $K_{r-1}$-free induced subgraph in a $K_r$-free segment graph remains open. The paper's Theorems 1.5 and 1.6 address analogous questions for string graphs (with a $\log^2 n$ loss), but the segment-graph case with a linear guarantee is unresolved.

Source paper

 Quasiplanar Graphs, String Graphs, and the Erdos-Gallai Problem
 Jacob Fox, Janos Pach, Andrew Suk · 2022-10-25
 https://arxiv.org/abs/2112.02378
 PDF source

=== Source paper abstract / header ===
Abstract:An $r$-quasiplanar graph is a graph drawn in the plane with no $r$ pairwise crossing edges. Let $s \geq 3$ be an integer and $r=2^s$. We prove that there is a constant $C$ such that every $r$-quasiplanar graph with $n \geq r$ vertices has at most $n\left(Cs^{-1}\log n\right)^{2s-4}$ edges.
A graph whose vertices are continuous curves in the plane, two being connected by an edge if and only if they intersect, is called a string graph. We show that for every $\epsilon>0$, there exists $\delta>0$ such that every string graph with $n$ vertices, whose chromatic number is at least $n^{\epsilon}$ contains a clique of size at least $n^{\delta}$. A clique of this size or a coloring using fewer than $n^{\epsilon}$ colors can be found by a polynomial time algorithm in terms of the size of the geometric representation of the set of strings.
In the process, we use, generalize, and strengthen previous results of Lee, Tomon, and others. All of our theorems are related to geometric variants of the following classical graph-theoretic problem of Erdos, Gallai, and Rogers. Given a $K_r$-free graph on $n$ vertices and an integer $s<r$, at least how many vertices can we find such that the subgraph induced by them is $K_s$-free?
 

 
 
 
 Comments:
 Appears in the Proceedings of the 30th International Symposium on Graph Drawing and Network Visualization (GD 2022)
 

 Subjects:
 
 Combinatorics (math.CO); Computational Geometry (cs.CG)
 

 Cite as:
 arXiv:2112.02378 [math.CO]
 

 
  
 (or 
 arXiv:2112.02378v6 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2112.02378
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Andrew Suk [view email] 
 [v1]
 Sat, 4 Dec 2021 16:41:28 UTC (19 KB)

 [v2]
 Tue, 7 Dec 2021 02:54:48 UTC (19 KB)

 [v3]
 Mon, 13 Dec 2021 17:18:27 UTC (14 KB)

 [v4]
 Sat, 3 Sep 2022 01:56:20 UTC (14 KB)

 [v5]
 Fri, 9 Sep 2022 14:33:48 UTC (37 KB)

 [v6]
 Tue, 25 Oct 2022 13:54:32 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Quasiplanar Graphs, String Graphs, and the Erdos-Gallai Problem, by Jacob Fox and 2 other authors
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
 | 2021-12
 

 Change to browse by:
 
 cs
 cs.CG
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

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
  "one_line": "The conjecture remains open, but it holds under a summable hereditary separator condition, notably for K_{t,t}-free or bounded-direction segment graphs, and any counterexample sequence must have balanced biclique size tending to infinity but remaining sublinear.",
  "would_publish": false,
  "caveats": "The unrestricted argument only recovers the known n/log^2 n bound, and the unbounded sublinear-biclique regime remains untreated."
}
```

## 1. Statement and notation

For a graph \(G\), define
\[
a_s(G)=\max\{|X|:X\subseteq V(G),\ G[X]\text{ is }K_s\text{-free}\}.
\]
The problem asks whether, for every fixed \(r\ge 4\), there is \(c_r>0\) such that every \(K_r\)-free segment graph \(G\) satisfies
\[
a_{r-1}(G)\ge c_r |V(G)|.
\]

I do not prove or disprove this. Below are a separator criterion yielding several linear special cases, a structural restriction on any counterexample sequence, and a fractional reformulation for proper segment representations.

## 2. Elementary observations

### Lemma 2.1

Let \(G\) be \(K_r\)-free.

1. For every \(v\in V(G)\), the graph \(G[N(v)]\) is \(K_{r-1}\)-free. Consequently,
   \[
   a_{r-1}(G)\ge \Delta(G).
   \]
2. If \(A,B\subseteq V(G)\) are anticomplete, then
   \[
   a_{r-1}(G[A\cup B])
   \ge a_{r-1}(G[A])+a_{r-1}(G[B]).
   \]
3. If \(A,B\) are nonempty and complete to each other, then both \(G[A]\) and \(G[B]\) are \(K_{r-1}\)-free.

#### Proof

For (1), a \(K_{r-1}\) in \(N(v)\), together with \(v\), would form a \(K_r\).

For (2), take maximum \(K_{r-1}\)-free subsets of \(A\) and \(B\). Since there are no edges between them, every clique in their union lies in one side.

For (3), a \(K_{r-1}\) in \(A\), together with any vertex of \(B\), would form a \(K_r\), and symmetrically. ∎

In particular, a complete bipartite pair with one side of linear size immediately proves the desired conclusion.

## 3. The separator argument and its logarithmic barrier

I use the standard string-graph separator theorem in the following form.

> **String-graph separator theorem.** There is an absolute constant \(c_{\rm sep}\) such that every string graph with \(m\) edges has a partition
> \[
> V(G)=S\mathbin{\dot\cup}A\mathbin{\dot\cup}B
> \]
> satisfying:
> \[
> E(A,B)=\varnothing,\qquad |A|,|B|\le \frac23 |V(G)|,
> \qquad |S|\le c_{\rm sep}\sqrt m.
> \]

Since segment graphs are string graphs, it applies here.

### Proposition 3.1: recovery of the known \(n/\log^2 n\) bound

There is an absolute constant \(C\) such that, for every \(r\ge3\), every \(K_r\)-free string graph \(G\) on \(n\ge3\) vertices satisfies
\[
a_{r-1}(G)\ge \frac{n}{C(\log n)^2}.
\]

#### Proof

This is included to isolate precisely why the same induction does not give a linear bound.

Let
\[
\phi(x)=\frac{x}{(\log x)^2}
\]
for sufficiently large \(x\); finitely many smaller values can be absorbed by increasing \(C\).

Suppose first that
\[
\Delta(G)\ge \frac{\phi(n)}{C}.
\]
Then Lemma 2.1 gives the result.

Otherwise,
\[
m\le \frac{n\Delta(G)}2
   <\frac{n^2}{2C(\log n)^2}.
\]
The separator theorem gives a separator of size
\[
s\le \frac{c_{\rm sep}}{\sqrt{2C}}\frac{n}{\log n}.
\]
Write \(n_i=|A_i|\) for the two anticomplete sides. Thus
\[
n_1+n_2=n-s,\qquad n_i\le \frac{2n}{3}.
\]

The necessary calculus inequality is
\[
\phi(n_1)+\phi(n_2)\ge \phi(n),
\tag{3.1}
\]
provided \(s\le b n/\log n\), where \(b>0\) is a sufficiently small absolute constant.

Indeed, let \(L=\log n\), \(p_i=n_i/n\), and \(\eta=s/n\). For large \(n\), balance and \(\eta=O(1/L)\) imply \(p_i\in[1/4,2/3]\). Since \(u\mapsto(1+u)^{-2}\) lies above its tangent at \(0\),
\[
\begin{aligned}
\sum_i\phi(n_i)
&=\frac{n}{L^2}\sum_i p_i
 \left(1+\frac{\log p_i}{L}\right)^{-2}\\
&\ge \frac{n}{L^2}
 \left(1-\eta+\frac{2}{L}\sum_i -p_i\log p_i\right).
\end{aligned}
\]
On \(p_i\in[1/4,2/3]\), the entropy term
\[
\sum_i-p_i\log p_i
\]
is bounded below by a positive absolute constant. Thus (3.1) follows whenever \(\eta L\) is sufficiently small. Choosing \(C\) sufficiently large ensures this.

By induction and Lemma 2.1(2),
\[
\begin{aligned}
a_{r-1}(G)
&\ge a_{r-1}(G[A])+a_{r-1}(G[B])\\
&\ge \frac{\phi(n_1)+\phi(n_2)}C
 \ge \frac{\phi(n)}C.
\end{aligned}
\]
The finite induction base is handled by increasing \(C\). ∎

This is essentially the known logarithmic-loss argument from the source paper.

For a proposed linear induction \(a_{r-1}(H)\ge c|H|\), the same separator step gives only
\[
a_{r-1}(G)\ge c(|A|+|B|)=c(n-|S|),
\]
with no surplus to pay for \(S\). By contrast, \(x/\log^2x\) gains a small “entropy term” when a set is split into two balanced pieces, and that gain absorbs a separator of order \(n/\log n\). Thus a genuinely new ingredient is needed to recover vertices lying in separators or otherwise avoid paying for them at every scale.

## 4. A summable-separator criterion for a linear answer

The following criterion makes the preceding obstruction precise.

### Lemma 4.1

Fix \(s\ge2\), let \(\beta=2/3\), and let \(G\) be a string graph. Suppose that there are \(L\ge2\) and a nonincreasing function
\[
q:[L,\infty)\longrightarrow[0,\infty)
\]
such that every induced subgraph \(H\subseteq G\) with \(|H|>L\) which is not \(K_s\)-free has a balanced separator of size at most
\[
q(|H|)|H|.
\]
If
\[
Q_L:=\sum_{j=0}^{\infty}q(L\beta^{-j})<1,
\tag{4.1}
\]
then
\[
a_s(G)\ge \frac{1-Q_L}{L}|V(G)|.
\]
In particular, if \(Q_L\le 1/2\), then \(a_s(G)\ge |V(G)|/(2L)\).

#### Proof

Recursively process induced subgraphs as follows.

- Stop if the current graph is \(K_s\)-free.
- Stop if it has at most \(L\) vertices.
- Otherwise remove the asserted balanced separator and recurse on the two anticomplete sides.

Let \(\mathcal T\) be the recursion tree and let \(R\) be the union of all removed separators. At a recursion node \(X\), charge \(q(|X|)\) to every vertex of \(X\). This pays for its separator because
\[
|S_X|\le |X|q(|X|).
\]

Along any root-to-leaf path, the sizes of successive recursion nodes decrease by a factor at most \(\beta\). Reading the path backwards from its final internal node, its sizes are at least
\[
L,\ L\beta^{-1},\ L\beta^{-2},\ldots.
\]
Since \(q\) is nonincreasing, every original vertex receives total charge at most \(Q_L\). Hence
\[
|R|\le Q_L|V(G)|.
\]

The terminal sets are pairwise anticomplete. From a terminal \(K_s\)-free set, retain all vertices; from any other terminal set, which has at most \(L\) vertices, retain one vertex. Thus at least a \(1/L\) fraction of the nonseparator vertices are retained. Their union is \(K_s\)-free because distinct terminal sets are anticomplete. Therefore
\[
a_s(G)\ge \frac{|V(G)|-|R|}{L}
 \ge \frac{1-Q_L}{L}|V(G)|.
\]
∎

### Corollary 4.2: hereditary polynomial sparsity

Suppose there are constants \(D>0\) and \(\delta>0\) such that every induced subgraph \(H\subseteq G\) which is not \(K_s\)-free satisfies
\[
e(H)\le D|H|^{2-2\delta}.
\tag{4.2}
\]
Then
\[
a_s(G)\ge c(D,\delta)|V(G)|
\]
for some \(c(D,\delta)>0\).

#### Proof

The string-graph separator theorem and (4.2) give a separator of size at most
\[
c_{\rm sep}\sqrt D\,|H|^{1-\delta}.
\]
Thus \(q(x)=c_{\rm sep}\sqrt D\,x^{-\delta}\), and
\[
\sum_{j\ge0}q(L\beta^{-j})
=
\frac{c_{\rm sep}\sqrt D\,L^{-\delta}}
 {1-\beta^\delta}.
\]
This is at most \(1/2\) for a sufficiently large constant \(L=L(D,\delta)\). Apply Lemma 4.1. ∎

### Corollary 4.3: the summable logarithmic threshold

Suppose that for some \(D,\gamma>0\), every sufficiently large induced subgraph \(H\subseteq G\) which is not \(K_s\)-free satisfies
\[
e(H)\le
\frac{D|H|^2}{(\log |H|)^{2+\gamma}}.
\tag{4.3}
\]
Then \(a_s(G)\ge c(D,\gamma)|V(G)|\).

Indeed, the separator ratio is at most
\[
q(x)=\frac{c_{\rm sep}\sqrt D}
 {(\log x)^{1+\gamma/2}}.
\]
Since
\[
\sum_{j\ge0}
\frac{1}{(\log L+j\log(3/2))^{1+\gamma/2}}
\]
converges, its tail can be made at most \(1/(2c_{\rm sep}\sqrt D)\) by choosing \(L\) sufficiently large.

This identifies a natural threshold in the separator method: separator ratios of order \(1/\log^{1+\varepsilon}n\) are summable over geometric scales, whereas \(1/\log n\) is not.

## 5. A concrete consequence: the \(K_{t,t}\)-free case

### Theorem 5.1

For every fixed \(t\ge2\), there is \(c_t>0\) such that every \(K_{t,t}\)-free string graph \(G\) satisfies
\[
\alpha(G)\ge c_t|V(G)|.
\]
Consequently, for every \(r\ge4\), the conjecture holds for \(K_r\)-free segment graphs which are also \(K_{t,t}\)-free.

#### Proof

By the Kővári–Sós–Turán bound, there is \(D_t\) such that every \(K_{t,t}\)-free graph \(H\) on \(x\) vertices satisfies
\[
e(H)\le D_t x^{2-1/t}.
\]
Every induced subgraph remains \(K_{t,t}\)-free. Apply Corollary 4.2 with
\[
\delta=\frac1{2t}.
\]
This gives a linear independent set, which is certainly \(K_{r-1}\)-free.

More explicitly, it is enough to take an integer \(L_t\) satisfying
\[
L_t\ge
\left(
\frac{2c_{\rm sep}\sqrt{D_t}}
 {1-(2/3)^{1/(2t)}}
\right)^{2t},
\]
in which case the proof gives
\[
\alpha(G)\ge \frac{|V(G)|}{2L_t}.
\]
∎

This special case does not resolve the conjecture because \(K_r\)-freeness does not bound the balanced biclique number: \(K_{m,m}\) is itself a \(K_r\)-free segment graph for every \(r\ge3\).

## 6. Necessary structure of any counterexample sequence

Let
\[
b(G)=\max\{t:G\text{ contains a }K_{t,t}\}.
\]

### Proposition 6.1

Suppose \(G_n\) is a sequence of \(K_r\)-free segment graphs such that
\[
\frac{a_{r-1}(G_n)}{|V(G_n)|}\longrightarrow0.
\]
Then
\[
\Delta(G_n)=o(|V(G_n)|),
\]
and
\[
b(G_n)\longrightarrow\infty,
\qquad
b(G_n)=o(|V(G_n)|).
\]

#### Proof

Lemma 2.1 gives
\[
\Delta(G_n)\le a_{r-1}(G_n),
\]
so the maximum-degree assertion follows.

If \(G_n\) contains a \(K_{t,t}\) with sides \(A,B\), then each of \(A,B\) is \(K_{r-1}\)-free by Lemma 2.1(3). Therefore
\[
b(G_n)\le a_{r-1}(G_n)=o(|V(G_n)|).
\]

If \(b(G_n)\) did not tend to infinity, some infinite subsequence would be \(K_{T,T}\)-free for a fixed \(T\). Theorem 5.1 would then give
\[
a_{r-1}(G_n)\ge\alpha(G_n)\ge c_T|V(G_n)|,
\]
a contradiction. ∎

Thus any counterexample must inhabit a fairly specific regime: both maximum degree and largest balanced biclique are sublinear, but the balanced biclique size must nevertheless grow without bound.

## 7. Direct geometric special cases

### Boundedly many directions

Suppose the representing segments use at most \(q\) slopes. Choose a slope class containing at least \(n/q\) segments. Within one slope class, segments on distinct supporting lines are disjoint, while segments on the same supporting line form an interval graph. Hence the induced graph on this slope class is a disjoint union of interval graphs and is perfect.

If \(G\) is \(K_r\)-free, this slope class is properly colorable with at most \(r-1\) colors. The union of its largest \(r-2\) color classes is \(K_{r-1}\)-free and has size at least
\[
\frac{r-2}{r-1}\cdot\frac nq.
\]
Therefore
\[
a_{r-1}(G)\ge
\frac{r-2}{q(r-1)}\,n.
\]

This includes axis-parallel segment families with fixed \(q=2\).

More generally, if the segment graph is perfect—for example, a nondegenerate permutation graph—then
\[
a_{r-1}(G)\ge \frac{r-2}{r-1}n.
\]

## 8. Fractional reformulation for proper segment representations

Let \(\mathcal K_{r-1}(G)\) be the \((r-1)\)-uniform hypergraph whose hyperedges are the \((r-1)\)-cliques of \(G\). Then \(K_{r-1}\)-free induced subsets of \(G\) are precisely independent sets of \(\mathcal K_{r-1}(G)\).

Suppose \(G\) has a representation in which every adjacent pair of segments crosses transversely in their relative interiors. Such representations are closed under independent vertex blow-ups: replace a segment by any number of sufficiently close, distinct parallel translates. Copies of one segment are pairwise disjoint; copies corresponding to adjacent original segments all cross; and sufficiently small translations preserve all nonedges.

For this robust subclass, the conjecture is equivalent to a uniform bound on
\[
\chi_f(\mathcal K_{r-1}(G)),
\]
the fractional chromatic number of the clique hypergraph. Indeed, the linear assertion applied to all integer blow-ups gives the weighted statement
\[
\alpha_w(\mathcal K_{r-1}(G))
 \ge c_r\,w(V(G))
\]
for every nonnegative vertex weighting \(w\). Linear programming duality gives
\[
\chi_f(\mathcal K_{r-1}(G))
=
\sup_{w\ne0}
\frac{w(V(G))}
{\alpha_w(\mathcal K_{r-1}(G))}.
\]

This is potentially useful because the known examples requiring many integral \(K_{r-1}\)-free color classes do not by themselves rule out bounded fractional chromatic number.

I do not assert that every segment graph admits such a proper-crossing representation; collinear overlaps and forced tangencies make that robustness question nontrivial.

## 9. Remaining gap

The separator argument gives a complete explanation of the existing \(\Theta(\log^2 n)\) loss but does not remove it. The linear special cases above cover:

- hereditary edge density \(O(n^{2-\varepsilon})\);
- more generally, separator ratios summable over geometric scales;
- fixed \(K_{t,t}\)-free segment graphs;
- fixed-direction and perfect segment graphs;
- graphs containing a balanced biclique with a linear side.

They do not cover the essential remaining regime in which balanced bicliques grow with \(n\) but have size \(o(n)\). At a separator split, target subsets from the two anticomplete sides can be united, but there is presently no justified way to incorporate a positive fraction of the separator without creating an \((r-1)\)-clique across ancestor and descendant pieces. That is the unresolved step.
