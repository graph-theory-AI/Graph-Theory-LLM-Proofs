Attack the following open graph-theory problem.

Catalog id: 2103.08698__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2103.08698__01/
Source paper: Approximation metatheorems for classes with bounded expansion (arXiv:2103.08698)

=== Catalog page (statement + literature review) ===
FO minimization PTAS in treewidth-fragile classes — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 6 of arXiv:2103.08698 asks whether monotone minimization problems expressible in first-order logic admit constant-factor approximations in bounded-expansion classes and PTASes in efficiently fractionally treewidth-fragile classes. The source paper itself establishes these results only for maximization problems; the paper explicitly notes that for minimization the error is bounded only by a fraction of the total vertex weight rather than the optimum, leaving both parts of the problem open. No subsequent paper resolving either part was found in a targeted literature search spanning arXiv and conference proceedings through May 2026.

 Reviewer notes. No follow-up paper addressing the minimization side of Problem 6 was found. The source paper's own discussion identifies weighted vertex cover in fractionally treewidth-fragile classes as the simplest concrete open case. The related literature on PTAS for sparse general-valued CSPs (e.g. arXiv:2012.12607) works with Max-CSP frameworks and does not resolve the FO-minimization question in bounded-expansion classes.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Do monotone minimization problems expressible in the first order logic admit constant factor approximation in all classes with bounded expansion? And PTASes in all efficiently fractionally treewidth-fragile graph classes?

Context

The paper's techniques apply to minimization problems only with error bounded by a fraction of the total vertex weight rather than the optimal, so constant-factor approximation in bounded-expansion classes and PTASes in fractionally treewidth-fragile classes for minimization remain open. As a concrete simplest case, it is unknown whether a PTAS exists for weighted vertex cover in fractionally treewidth-fragile graph classes.

Source paper

 Approximation metatheorems for classes with bounded expansion
 Zdeněk Dvořák · 2021-10-09
 https://arxiv.org/abs/2103.08698
 PDF source

=== Source paper abstract / header ===
Abstract:We give a number of approximation metatheorems for monotone maximization problems expressible in the first-order logic, in substantially more general settings than the previously known. We obtain * constant-factor approximation algorithm in any class of graphs with bounded expansion, * a QPTAS in any class with strongly sublinear separators, and * a PTAS in any fractionally treewidth-fragile class (which includes all common classes with strongly sublinear separators. Moreover, our tools also give an exact subexponential-time algorithm in any class with strongly sublinear separators.
 

 
 
 
 Comments:
 35 pages, no figures; revised the presentation
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2103.08698 [cs.DM]
 

 
  
 (or 
 arXiv:2103.08698v3 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2103.08698
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdeněk Dvořák [view email] 
 [v1]
 Mon, 15 Mar 2021 20:26:05 UTC (16 KB)

 [v2]
 Sat, 11 Sep 2021 16:12:58 UTC (17 KB)

 [v3]
 Sat, 9 Oct 2021 23:06:38 UTC (24 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Approximation metatheorems for classes with bounded expansion, by Zden\v{e}k Dvo\v{r}\'ak
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2021-03
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Zdenek Dvorák 

 

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
  "one_line": "The full metatheorem remains open, but weighted vertex cover has a PTAS on every efficiently fractionally treewidth-fragile class via a half-integral LP core.",
  "would_publish": false,
  "caveats": "Only weighted vertex cover and a bounded-rank syntactic fragment are covered; the general monotone FO claims remain open."
}
```

## 1. Statement of the partial result

I use the following standard formulation of efficient fractional treewidth fragility. For every fixed integer \(k\), an algorithm produces a polynomial-size multiset
\[
Z_1,\ldots,Z_m\subseteq V(G)
\]
such that

1. \(\operatorname{tw}(G-Z_i)\le t(k)\) for every \(i\), where \(t(k)\) is independent of \(|G|\); and
2. every vertex belongs to at most \(m/k\) of the sets \(Z_i\).

The equivalent probabilistic formulation is that \(Z\) is sampled from a finite distribution with
\[
\Pr(v\in Z)\le \frac1k
\]
for every vertex, and \(G-Z\) always has treewidth at most \(t(k)\).

The following settles the concrete weighted-vertex-cover case highlighted in the question.

### Theorem 1

Let \(\mathcal C\) be an efficiently fractionally treewidth-fragile graph class. Then minimum-weight vertex cover, with nonnegative rational vertex weights, has a deterministic PTAS on \(\mathcal C\) under the explicit-support definition above.

More precisely, for every integer \(k\), the algorithm returns a vertex cover of weight at most
\[
\left(1+\frac{2}{k}\right)\operatorname{OPT}.
\]

No hereditary assumption on \(\mathcal C\) is needed.

The proof consists of applying the fractional treewidth deletion only after a weighted Nemhauser–Trotter reduction. The resulting residual graph has total vertex weight at most twice its optimum vertex-cover weight, exactly eliminating the “error relative to total weight” obstruction.

---

## 2. A weighted half-integral core lemma

For a weighted graph \((G,w)\), consider the vertex-cover LP
\[
\begin{aligned}
\min\quad &\sum_{v\in V(G)}w(v)x_v,\\
\text{subject to}\quad &x_u+x_v\ge 1 &&(uv\in E(G)),\\
&0\le x_v\le 1 &&(v\in V(G)).
\end{aligned}
\tag{VC-LP}
\]

An optimal basic solution can be chosen half-integral:
\[
x_v\in\left\{0,\frac12,1\right\}.
\]
For completeness, this follows by considering the graph of tight edge constraints on the strictly fractional variables. A bipartite component admits a nonzero alternating perturbation in both directions, contradicting extremality, while an odd cycle of tight equations \(x_u+x_v=1\) forces all values in its component to equal \(1/2\).

Set
\[
V_0=\{v:x_v=0\},\qquad
R=\{v:x_v=1/2\},\qquad
V_1=\{v:x_v=1\},
\]
and let \(H=G[R]\).

### Lemma 2

The partition above satisfies

\[
\tau_w(G)=w(V_1)+\tau_w(H)
\tag{1}
\]
and
\[
w(R)\le 2\tau_w(H),
\tag{2}
\]
where \(\tau_w\) denotes minimum vertex-cover weight.

#### Proof

First, there is no edge from \(V_0\) to \(V_0\cup R\), since such an edge would violate its LP constraint. Thus every neighbor of a vertex in \(V_0\) belongs to \(V_1\).

We prove the persistence assertion underlying (1). Let \(C\) be a minimum-weight vertex cover of \(G\), and put
\[
A=V_1\setminus C,\qquad B=V_0\cap C.
\]
Let
\[
N_0(A)=N(A)\cap V_0.
\]
Since \(C\) omits every vertex of \(A\), it must contain every vertex of \(N_0(A)\), so
\[
N_0(A)\subseteq B.
\tag{3}
\]

Modify \(x\) by lowering every variable in \(A\) from \(1\) to \(1/2\), and raising every variable in \(N_0(A)\) from \(0\) to \(1/2\). This remains LP-feasible:

- an edge from \(A\) to \(V_0\) has both endpoint values \(1/2\);
- an edge from \(A\) to \(R\) has both endpoint values \(1/2\);
- an edge with both endpoints in \(A\) also has sum \(1\);
- all other affected constraints remain satisfied.

Optimality of \(x\) therefore gives
\[
\frac12 w(N_0(A))-\frac12 w(A)\ge 0,
\]
and hence, using (3),
\[
w(A)\le w(N_0(A))\le w(B).
\tag{4}
\]

Now define
\[
C'=(C\setminus B)\cup A.
\]
The set \(C'\) contains all of \(V_1\) and none of \(V_0\). It is still a vertex cover: every edge incident with \(V_0\) has its other endpoint in \(V_1\), and no other edge can be uncovered by removing \(B\). By (4),
\[
w(C')\le w(C).
\]
Thus there is a minimum vertex cover containing \(V_1\) and avoiding \(V_0\).

Consequently, its intersection with \(R\) covers \(H\), proving
\[
\tau_w(G)\ge w(V_1)+\tau_w(H).
\]
Conversely, \(V_1\) together with any vertex cover of \(H\) covers all of \(G\), proving equality (1).

Finally, the all-\(1/2\) solution on \(H\) is optimal for the vertex-cover LP of \(H\). Otherwise, a better fractional solution on \(H\), combined with values \(0\) on \(V_0\) and \(1\) on \(V_1\), would improve the original LP solution. Therefore
\[
\operatorname{LP}(H)=\frac12 w(R).
\]
Since the LP is a lower bound on the integral optimum,
\[
\frac12 w(R)\le \tau_w(H),
\]
which is (2). ∎

---

## 3. PTAS algorithm

Fix \(\varepsilon>0\) and choose
\[
k=\left\lceil\frac{2}{\varepsilon}\right\rceil.
\]

Given \((G,w)\), perform the following steps.

1. Compute an optimal basic solution of (VC-LP), and obtain \(V_0,R,V_1\) and \(H=G[R]\).
2. Run the fractional treewidth-fragility algorithm on the original graph \(G\), obtaining \(Z_1,\ldots,Z_m\).
3. Put
   \[
   X_i=Z_i\cap R.
   \]
   Because every vertex lies in at most \(m/k\) deletion sets,
   \[
   \frac1m\sum_{i=1}^m w(X_i)
   \le \frac{w(R)}{k}.
   \]
   Hence an index \(i\) minimizing \(w(X_i)\) satisfies
   \[
   w(X_i)\le \frac{w(R)}{k}.
   \tag{5}
   \]
4. Since
   \[
   H-X_i=G[R\setminus Z_i]
   \]
   is an induced subgraph of \(G-Z_i\), it has treewidth at most \(t(k)\).
5. Compute an exact minimum-weight vertex cover \(D_i\) of \(H-X_i\) by dynamic programming on a bounded-width tree decomposition.
6. Return
   \[
   K=V_1\cup X_i\cup D_i.
   \]

### Feasibility

All edges incident with \(V_0\) have their other endpoint in \(V_1\). All other edges outside \(H\) are also covered by \(V_1\). Within \(H\), every edge incident with \(X_i\) is covered by \(X_i\), and every remaining edge is covered by \(D_i\). Thus \(K\) is a vertex cover of \(G\).

### Approximation guarantee

Let \(C_H^\star\) be a minimum-weight vertex cover of \(H\). Then
\[
C_H^\star\setminus X_i
\]
is a vertex cover of \(H-X_i\). Therefore
\[
w(D_i)\le w(C_H^\star\setminus X_i)\le \tau_w(H).
\]
Using (5) and Lemma 2,
\[
\begin{aligned}
w(X_i)+w(D_i)
&\le \frac{w(R)}{k}+\tau_w(H)\\
&\le \left(1+\frac{2}{k}\right)\tau_w(H).
\end{aligned}
\]
Together with the exact decomposition (1),
\[
\begin{aligned}
w(K)
&\le w(V_1)+\left(1+\frac{2}{k}\right)\tau_w(H)\\
&\le \left(1+\frac{2}{k}\right)
   \bigl(w(V_1)+\tau_w(H)\bigr)\\
&=\left(1+\frac{2}{k}\right)\tau_w(G)\\
&\le (1+\varepsilon)\tau_w(G).
\end{aligned}
\]

For fixed \(\varepsilon\), the number \(t(k)\) is constant. Weighted vertex cover on a graph of treewidth \(t(k)\) is solvable exactly in polynomial time, for example with \(2^{O(t(k))}\) states per bag. Thus the overall algorithm is a PTAS.

If efficient fractional fragility is supplied only by a sampler rather than an explicit polynomial-size support, the same proof gives a randomized PTAS by sampling repeatedly and taking the best candidate.

---

## 4. A constant-factor fragment of the first question

There is also a straightforward positive answer for a substantial syntactic subclass of monotone FO minimization formulas.

### Proposition 3

Suppose the feasibility formula is a fixed conjunction of formulas of the form
\[
\forall x_1\cdots x_q\,
\left(
\theta(x_1,\ldots,x_q)
\longrightarrow
\bigvee_{i\in I} S(x_i)
\right),
\tag{6}
\]
where \(\theta\) does not use the solution predicate \(S\), and every set \(I\) has size at most \(r\). Then the corresponding weighted minimization problem has an \(r\)-approximation on arbitrary graphs.

#### Proof

For every tuple satisfying \(\theta\), form the hyperedge
\[
e=\{x_i:i\in I\}.
\]
The feasible sets \(S\) are exactly the hitting sets of this rank-\(r\) hypergraph. There are polynomially many tuples because the formula and its arity are fixed.

Solve the standard hitting-set LP
\[
\min \sum_v w(v)x_v,\qquad
\sum_{v\in e}x_v\ge1\quad(e\in\mathcal E),\qquad x_v\ge0.
\]
Return
\[
S=\{v:x_v\ge1/r\}.
\]
Every hyperedge of size at most \(r\) contains such a vertex, and
\[
w(S)\le r\sum_v w(v)x_v\le r\,\operatorname{OPT}.
\]
∎

This covers vertex cover, fixed-pattern vertex transversals, and other bounded-rank universal covering formulas. It does not use bounded expansion.

---

## 5. What remains open

The proof does not establish either full metatheorem.

1. General semantically monotone FO formulas need not have the bounded-rank universal form (6). Dominating set, for example, has an existential selected witness ranging over an unbounded neighborhood.
2. The weighted vertex-cover PTAS relies crucially on the exact persistence identity
   \[
   \tau_w(G)=w(V_1)+\tau_w(H)
   \]
   and the balanced-core bound
   \[
   w(V(H))\le2\tau_w(H).
   \]
   No comparable lossless balanced-core theorem is proved here for arbitrary monotone FO minimization.
3. Fractional treewidth deletion by itself only yields an additive loss of order \(w(V)/k\). The LP core is precisely what converts that loss into \(O(\operatorname{OPT}/k)\); without such a core, the original obstruction remains.
4. Thus the constant-factor question for all monotone FO minimization problems on bounded-expansion classes, and the PTAS question for all such problems on efficiently fractionally treewidth-fragile classes, remain unresolved.

The argument is self-contained, but I have not independently verified whether this short weighted-vertex-cover observation has appeared elsewhere. Under the catalog's stated literature status, it would settle the highlighted concrete special case.
