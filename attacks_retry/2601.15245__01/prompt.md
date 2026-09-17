Attack the following open graph-theory problem.

Catalog id: 2601.15245__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2601.15245__01/
Source paper: Coloring small locally sparse degenerate graphs and related problems (arXiv:2601.15245)

=== Catalog page (statement + literature review) ===
Sub-exponential vertex threshold for degenerate coloring — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 6.1 of arXiv:2601.15245 asks whether the upper bound $2^{cd}$ on the number of vertices in Theorems 1.1 and 1.2 can be weakened to $e^{\omega(d)}$, with a corresponding improvement of the chromatic number bound, and whether large constant girth additionally helps. The paper itself establishes $e^{\Omega(d)} \leq f(d) \leq e^{O(d^2 \log d)}$ for the minimum order of a $d$-degenerate triangle-free $(d+1)$-chromatic graph, showing an exponential gap between the lower bound on $f(d)$ and the vertex regime covered by the main theorems. No follow-up resolving or making partial progress on Problem 6.1 has been found in the literature as of May 2026, which is expected given the paper's January 2026 submission date.

 Reviewer notes. No follow-up found. The conjecture is very recent (January 2026). The key open gap is between the vertex regime $n \leq 2^{cd}$ covered by the main theorems and the sub-exponential regime $n = e^{\omega(d)}$; resolving it is noted by the authors as the most important open problem from their paper and would have implications for Erd\H{o}s's problem on graph Ramsey numbers for triangle-free graphs.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Can the upper bound $2^{cd}$ on the number of vertices assumed in Theorems 1.1 and 1.2 be weakened to $e^{\omega(d)}$ (with a corresponding improvement of the upper bound on $\chi$ when $n=e^{\omega(d)}$)? What if we additionally assume that the graph has large (constant) girth?

Context

The perhaps most important open problem left by the paper is whether the exponential requirement on the number of vertices in Theorems 1.1 and 1.2 can be further relaxed. Even improving the constant $c$ in Theorem 1.1 could resolve Erdős's problem on graph Ramsey numbers for all triangle-free graphs by combining with the trivial lower bound $r(G)\geq|V(G)|$.

Source paper

 Coloring small locally sparse degenerate graphs and related problems
 Domagoj Bradač, Jacob Fox, Raphael Steiner, Benny Sudakov, Shengtong Zhang · 2026-01-21
 https://arxiv.org/abs/2601.15245

=== Source paper abstract / header ===
Abstract:The classic upper bound on the chromatic number of $d$-degenerate graphs is $d+1$, shown to be tight by complete graphs. A natural question is whether this bound remains tight if one forbids large cliques. Classic constructions of Tutte and Zykov from the early 50s show that there exist $d$-degenerate $(d+1)$-chromatic graphs that are triangle-free, however these constructions grow rapidly with $d$. Motivated by this and addressing a problem posed by the second author at the Oberwolfach Graph Theory workshop, we prove that the minimum order $f(d)$ of a $d$-degenerate triangle-free graph of chromatic number $d+1$ satisfies $e^{\Omega(d)}\le f(d)\le e^{O(d^2\log d)}.$ The lower bound follows from a novel upper bound on the chromatic number of triangle-free graphs: Every triangle-free $d$-degenerate graph $G$ on $n \le e^{O(d)}$ vertices satisfies $$\chi(G)\le O\left(\frac{d}{\log\left(d/\log n\right)}\right).$$ We extend this to a more general result about degenerate graphs with sparse neighborhoods, which has applications to many graph coloring problems: For example, we prove that every counterexample to Hadwiger's conjecture with parameter $t$ must have a complete bipartite subgraph with one exponentially large side ($K_{a,b}$ where $a=(\log t)^{1/2-o(1)}$ and $b=e^{t^{1-o(1)}}$) or a small and very dense subgraph (of order $\le t$ with $t^{2-o(1)}$ edges) in some neighborhood.
For the upper bound on $f(d)$ we establish a surprising connection between $f(d)$ and the on-line-chromatic number $g(n)$ of $n$-vertex triangle-free graphs. We also give an asymptotic improvement of the previous best upper bound for $g(n)$ due to Lovász, Saks and Trotter from 1989.
Along the way we disprove a generalization of Harris' fractional coloring conjecture to graphs of bounded clique number and raise numerous problems which open up interesting directions to explore for future research.
 

 
 
 
 Comments:
 24 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15, 05C83
 

 Cite as:
 arXiv:2601.15245 [math.CO]
 

 
  
 (or 
 arXiv:2601.15245v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2601.15245
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 21 Jan 2026 18:26:40 UTC (37 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Coloring small locally sparse degenerate graphs and related problems, by Domagoj Brada\v{c} and 4 other authors
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
 | 2026-01
 

 Change to browse by:
 
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
  "one_line": "The conjecture remains open, but girth growing faster than d/log d suffices for a super-exponential vertex threshold via an explicit chromatic Moore-type bound.",
  "would_publish": false,
  "caveats": "The argument gives no improvement for any fixed constant girth and does not settle the triangle-free case."
}
```

## 1. Formal interpretation of the question

Let
\[
f_\triangle(d)=\min\{|V(G)|:\ G\text{ is triangle-free, \(d\)-degenerate, and }\chi(G)=d+1\}.
\]
Since every \(d\)-degenerate graph is \((d+1)\)-colorable, the qualitative endpoint of the problem is naturally

\[
\boxed{\frac{\log f_\triangle(d)}d\longrightarrow\infty.}
\tag{Q}
\]

Equivalently, one asks whether there is some function \(h(d)\to\infty\) such that every triangle-free \(d\)-degenerate graph with at most
\[
\exp(dh(d))
\]
vertices is \(d\)-colorable.

There is a quantifier issue in the notation \(n=e^{\omega(d)}\). If it is read as saying that the conclusion should hold for every order sequence satisfying \(\log n/d\to\infty\), then it is already false. Indeed, the supplied upper construction gives counterexamples of order at most \(\exp(O(d^2\log d))\); adding isolated vertices produces counterexamples whose order is exactly \(e^{\omega(d)}\). Thus (Q), namely the existence of some super-exponential threshold, is the meaningful interpretation.

I do not resolve (Q). I give below a complete growing-girth special case.

---

## 2. A chromatic Moore-type bound

For an integer \(g\ge4\), put
\[
t=\left\lfloor\frac g2\right\rfloor.
\]

### Theorem

Every \(n\)-vertex graph \(G\) of girth at least \(g\) satisfies
\[
\boxed{\chi(G)\le 2+(2tn)^{1/t}.}
\tag{1}
\]

Consequently, if \(G\) is \(d\)-degenerate, has girth at least \(g\), and
\[
|V(G)|<\frac{(d-1)^t}{2t},
\tag{2}
\]
then \(G\) is \(d\)-colorable.

This theorem does not use degeneracy until the last implication.

### Proof

Set
\[
R=t-1=\left\lfloor\frac{g-2}{2}\right\rfloor.
\]
Thus
\[
2R+1<g.
\tag{3}
\]

For \(D\ge2\), define
\[
B_R(D)=1+D\sum_{j=0}^{R-1}(D-1)^j.
\tag{4}
\]

#### Claim 1: tree balls

If \(H\) has minimum degree at least \(D\) and girth at least \(g\), then every radius-\(R\) ball in \(H\) contains at least \(B_R(D)\) vertices and induces a tree.

Indeed, a non-tree edge in such a ball, together with paths in a breadth-first search tree, would create a cycle of length at most \(2R+1<g\). Hence the ball is a tree. Its root has at least \(D\) children, and every non-root vertex at distance less than \(R\) has at least \(D-1\) children. This gives (4).

#### Claim 2: iterated removal of large independent sets

Let \(q=\chi(G)\). Starting with \(G_0=G\), suppose that \(q_i=\chi(G_i)\ge3\). Choose an induced, vertex-minimal \(q_i\)-chromatic subgraph \(H_i\subseteq G_i\). The standard criticality argument gives
\[
\delta(H_i)\ge q_i-1.
\tag{5}
\]

Take a radius-\(R\) ball in \(H_i\). By Claim 1 it is a tree with at least
\[
B_R(q_i-1)
\]
vertices. One of its two bipartition classes is an independent set \(I_i\) of size at least
\[
|I_i|\ge \frac12 B_R(q_i-1).
\tag{6}
\]
Because \(H_i\) is induced in \(G_i\), this set is also independent in \(G_i\).

Removing an independent set lowers chromatic number by at most one:
\[
\chi(G_i-I_i)\ge \chi(G_i)-1.
\tag{7}
\]
Set \(G_{i+1}=G_i-I_i\). Starting from \(q_0=q\), we may perform this for \(i=0,\ldots,q-3\), and induction from (7) gives
\[
q_i\ge q-i.
\]

The independent sets \(I_i\) are pairwise disjoint. Since \(B_R(D)\) is increasing in \(D\), equations (6) and (7) give
\[
n\ge \frac12\sum_{D=2}^{q-1}B_R(D).
\tag{8}
\]
The last level of the tree ball gives
\[
B_R(D)\ge D(D-1)^{R-1}\ge (D-1)^R.
\]
Therefore
\[
\begin{aligned}
n
&\ge \frac12\sum_{u=1}^{q-2}u^R\\
&\ge \frac12\int_0^{q-2}x^R\,dx\\
&=\frac{(q-2)^{R+1}}{2(R+1)}
 =\frac{(q-2)^t}{2t}.
\end{aligned}
\tag{9}
\]
Inverting (9) proves (1).

Finally, if \(G\) is \(d\)-degenerate, then \(\chi(G)\le d+1\). If it were not \(d\)-colorable, it would have \(\chi(G)=d+1\), and (9) would imply
\[
n\ge\frac{(d-1)^t}{2t},
\]
contrary to (2). ∎

---

## 3. Consequence for growing girth

Define
\[
f_{\ge g}(d)=
\min\{|V(G)|:\operatorname{girth}(G)\ge g,\ G\text{ is \(d\)-degenerate},\
\chi(G)=d+1\},
\]
with value \(+\infty\) if no such graph exists.

The theorem gives
\[
\boxed{
f_{\ge g}(d)\ge
\frac{(d-1)^{\lfloor g/2\rfloor}}
     {2\lfloor g/2\rfloor}.
}
\tag{10}
\]

Combining this with the exponential lower bound from the source paper, for \(g\ge4\) one has
\[
f_{\ge g}(d)\ge
\max\left\{
e^{c d},
\frac{(d-1)^{\lfloor g/2\rfloor}}
     {2\lfloor g/2\rfloor}
\right\}
\tag{11}
\]
for some absolute \(c>0\).

If \(g=g(d)\) satisfies
\[
g(d)=\omega\!\left(\frac d{\log d}\right),
\tag{12}
\]
then (10) yields
\[
\log f_{\ge g(d)}(d)
\ge
\left\lfloor\frac{g(d)}2\right\rfloor\log(d-1)
-O(\log g(d))
=\omega(d).
\]
Thus:

\[
\boxed{
g(d)=\omega(d/\log d)
\quad\Longrightarrow\quad
f_{\ge g(d)}(d)=e^{\omega(d)}
\text{ in the lower-bound sense.}
}
\tag{13}
\]

This completely proves the desired super-exponential threshold when the girth is allowed to grow slightly faster than \(d/\log d\).

More quantitatively, if
\[
n=e^{d h(d)}
\]
and \(t=\lfloor g/2\rfloor\), then (1) gives
\[
\chi(G)\le
\min\left\{
d+1,\,
2+\exp\left(\frac{d h(d)+\log(2t)}t\right)
\right\}.
\tag{14}
\]
For example, if for some fixed \(\varepsilon>0\),
\[
t\ge(1+\varepsilon)\frac{d h(d)}{\log d},
\]
then
\[
\chi(G)\le d^{1/(1+\varepsilon)+o(1)}.
\tag{15}
\]

---

## 4. A necessary critical-graph configuration

There is another elementary structural constraint which indicates where a stronger argument would have to enter.

### Lemma

Let \(H\) be a \((d+1)\)-vertex-critical, \(d\)-degenerate graph. Then:

1. \(H\) has a vertex \(v\) of degree exactly \(d\).
2. In every proper \(d\)-coloring of \(H-v\), the \(d\) neighbors of \(v\) receive all \(d\) colors exactly once.
3. For every two colors \(i,j\), the corresponding neighbors \(x_i,x_j\) belong to the same \(i,j\)-Kempe component.

#### Proof

Criticality gives \(\delta(H)\ge d\), while \(d\)-degeneracy gives a vertex of degree at most \(d\), proving the first assertion.

If two neighbors of \(v\) had the same color in a \(d\)-coloring of \(H-v\), some color would be absent from \(N(v)\), allowing \(v\) to be colored. Hence the neighbor colors are all distinct.

If \(x_i,x_j\) were in different components of the subgraph induced by colors \(i,j\), swapping \(i\) and \(j\) on the component containing \(x_i\) would eliminate color \(i\) from \(N(v)\), again allowing \(v\) to be colored. ∎

If \(H\) has girth at least \(g\), each such bichromatic connection contains a path of length at least \(g-2\), because adjoining its two edges to \(v\) creates a cycle. Paths belonging to different unordered color pairs are edge-disjoint, since every edge has a unique pair of endpoint colors. Hence
\[
e(H)\ge d+(g-2)\binom d2.
\tag{16}
\]
On the other hand, an \(m\)-vertex \(d\)-degenerate graph has
\[
e(H)\le dm-\binom{d+1}{2}.
\tag{17}
\]
Together these imply only
\[
m\ge \frac{(g-1)d+5-g}{2},
\]
which is weaker than the tree-ball bound. Thus merely counting one family of Kempe paths cannot produce a super-exponential threshold.

---

## 5. What remains open

For every fixed constant \(g\), equation (10) is only polynomial in \(d\):
\[
f_{\ge g}(d)=\Omega_g\!\left(d^{\lfloor g/2\rfloor}\right).
\]
This is asymptotically weaker than the paper's \(e^{\Omega(d)}\) lower bound, which already applies to all triangle-free graphs. Therefore the argument gives no improvement for “large constant girth” in the intended fixed-\(g\) sense.

The unresolved tasks remain:

1. Prove or disprove
   \[
   \log f_\triangle(d)/d\to\infty.
   \]
2. Even under any fixed girth condition \(g\ge5\), improve the existing exponential lower bound to \(e^{\omega(d)}\), or construct \(e^{O(d)}\)-order counterexamples.
3. Obtain the corresponding quantitative chromatic bound in the regime \(\log n/d\to\infty\).

The local obstruction naturally occurs on an exponential scale: if the colors on the \(d\) independent neighbors of the critical vertex were independent and uniform, the probability that they were all distinct would be
\[
\frac{d!}{d^d}=e^{-d+O(\log d)}.
\]
This is only a heuristic, but it explains why a union-bound or bounded-depth local argument tends to stop at \(e^{O(d)}\). A resolution of the fixed-girth problem appears to require a genuinely global use of the Kempe-linkage constraints or a comparably strong structural idea.
