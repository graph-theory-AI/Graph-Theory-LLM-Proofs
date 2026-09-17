Attack the following open graph-theory problem.

Catalog id: 2604.13700__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2604.13700__01/
Source paper: Openly disjoint cycles and directed tree-width of regular digraphs (arXiv:2604.13700)

=== Catalog page (statement + literature review) ===
Directed tree-width linear constant in regular digraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The paper (arXiv:2604.13700) establishes that every r-regular digraph has directed tree-width Omega(r), resolving the existence of such a linear lower bound, and proves a specific constant of at least 3/22 via the connection to openly disjoint cycles. The optimal constant epsilon in the lower bound dtw >= epsilon*r remains unknown. The paper was posted 18 days before this review, and no follow-up addressing the optimal constant has been found.

 Reviewer notes. No follow-up found; the paper is fewer than 3 weeks old. The paper proves dtw >= (3/22)r as the current best lower bound on epsilon, leaving a gap to the true optimal constant. Steiner's own research page lists this paper as 'submitted' with no citing work yet.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Informal. What is the best-possible constant $\varepsilon>0$ such that every $r$-regular digraph $D$ has directed tree-width at least $\varepsilon r$?

Context

Motivated by Theorem 7 of the paper, which establishes that every $r$-regular digraph has directed tree-width growing with $r$, the authors pose this question about the optimal linear constant in such a lower bound.

Notes. Posed in the text as 'it would be interesting to determine' following Problem 2, without a formal labelled environment.

Source paper

 Openly disjoint cycles and directed tree-width of regular digraphs
 Raphael Steiner · 2026-04-26
 https://arxiv.org/abs/2604.13700

=== Source paper abstract / header ===
Abstract:Given a digraph $D$, let $c(D)$ denote the largest integer $k$ such that there are $k$ openly disjoint cycles through a vertex, i.e., a collection of directed cycles $C_1,\ldots,C_k$ through a common vertex $v$ such that $C_1-v,\ldots,C_k-v$ are pairwise vertex-disjoint. The famous Caccetta-Häggkvist conjecture and its regular variant due to Behzad, Chartrand and Wall from 1970, have motivated the study of degree conditions forcing $c(D)$ to be large.
In 1985 Thomassen constructed digraphs of arbitrarily high minimum out- and in-degree such that $c(D)\le 2$. In 2005, Seymour asked whether in contrast every $r$-regular digraph satisfies $c(D)=r$, which would have implied the Behzad-Chartrand-Wall conjecture. In 2008, Mader answered this negatively for every $r\ge 8$, but conjectured that nevertheless the minimum value $c_r$ of $c(D)$ over all $r$-regular digraphs grows with $r$, i.e. $\lim_{r\rightarrow\infty}c_r=\infty$.
As the first main result of our paper, we prove Mader's conjecture in a strong form by showing $c_r\ge \lceil\frac{3}{22} r\rceil$ for every $r\in \mathbb{N}$. We also show $c_r\le 7\left\lceil \frac{r}{8}\right\rceil$, improving the previous best upper bound $c_r\le r-\Theta(\sqrt{r})$ due to Mader.
In our second main result we show that every $r$-regular digraph has directed tree-width $\Omega(r)$. This is tight up to the implied constant and cannot be extended to digraphs of minimum out- and in-degree at least $r$. As a corollary we obtain the existence of a function $f:\mathbb{N}\rightarrow \mathbb{N}$ such that every regular digraph with degree at least $f(k)$ contains a subdivision of the cylindrical wall of order $k$, and hence of a large class of planar digraphs. This makes progress on the notoriously difficult problem of finding degree conditions guaranteeing subdivisions of digraphs, related to a well-known conjecture of Mader from 1985.
 

 
 
 
 Comments:
 16 pages, added new result
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C07, 05C20, 05C38, 05C40
 

 Cite as:
 arXiv:2604.13700 [math.CO]
 

 
  
 (or 
 arXiv:2604.13700v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2604.13700
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 15 Apr 2026 10:28:27 UTC (13 KB)

 [v2]
 Sun, 26 Apr 2026 15:04:32 UTC (29 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Openly disjoint cycles and directed tree-width of regular digraphs, by Raphael Steiner
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
 | 2026-04
 

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
  "one_line": "Under the finite simple loopless convention, 3/22 ≤ ε* ≤ 1; the optimal constant is 1 for symmetric regular digraphs, while semicomplete digraphs and regular tournaments admit stronger 1/3 and asymptotic 2/3 lower bounds, respectively.",
  "would_publish": false,
  "caveats": "The global optimum remains open; allowing parallel arcs makes the optimal constant zero."
}
```

# Mathematical writeup

## 1. Formalization and global bounds

Throughout, an \(r\)-regular digraph means a finite loopless simple digraph \(D\) satisfying
\[
d_D^+(v)=d_D^-(v)=r\qquad\text{for every }v\in V(D),
\]
with digons permitted. Directed tree-width is normalized so that a one-bag decomposition on \(n\) vertices has width \(n-1\).

Define
\[
\varepsilon_*=
 \inf_{r\ge 1}\ \inf_{\substack{D\text{ simple}\\D\text{ is }r\text{-regular}}}
 \frac{\operatorname{dtw}(D)}r.
\]
Thus \(\varepsilon_*\) is the largest constant valid for every \(r\) and every \(r\)-regular \(D\).

Taking the theorem quoted in the catalog as given,
\[
\varepsilon_*\ge \frac3{22}.
\]

For the upper bound, let \(D=\overleftrightarrow{K}_{r+1}\), the complete bidirected graph on \(r+1\) vertices. It is \(r\)-regular and, as proved below,
\[
\operatorname{dtw}(\overleftrightarrow{K}_{r+1})=r.
\]
Consequently
\[
\boxed{\frac3{22}\le \varepsilon_*\le 1.}
\]
The results below do not narrow this global interval, but they settle substantial special classes.

---

## 2. A leaf lemma for arboreal decompositions

For \(v\in V(D)\), let \(\nu_D(v)\) be the maximum number of openly disjoint directed cycles through \(v\). Equivalently, let
\[
\tau_D(v)=\min\bigl\{|Z|:Z\subseteq V(D)\setminus\{v\},\ 
 Z\text{ meets every directed cycle through }v\bigr\}.
\]

By directed Menger applied after splitting \(v\) into a source and a sink,
\[
\nu_D(v)=\tau_D(v).
\]

### Lemma 2.1
For every loopless digraph \(D\),
\[
\boxed{\operatorname{dtw}(D)\ge \min_{v\in V(D)}\nu_D(v).}
\]

#### Proof

Let \((R,\mathcal W,\mathcal X)\) be an arboreal decomposition of width \(k\). We use the standard definition in which \(X_e\) is disjoint from the set it guards.

If \(R\) has one node, then \(k=|V(D)|-1\), while \(\nu_D(v)\le |V(D)|-1\) for every \(v\).

Otherwise, choose an out-leaf \(t\) of \(R\), and let \(e\) be its parent edge. Put
\[
S=W_t,\qquad X=X_e.
\]
Then \(X\) guards \(S\), and the width condition at \(t\) gives
\[
|S|+|X|-1\le k.
\]

Fix \(v\in S\). The set
\[
Z=(S\setminus\{v\})\cup X
\]
meets every directed cycle through \(v\). Indeed, a cycle contained in \(S\) meets \(S\setminus\{v\}\), while a cycle which leaves \(S\) must meet \(X\), by \(X\)-normality of \(S\). Therefore
\[
\nu_D(v)=\tau_D(v)\le |Z|=|S|+|X|-1\le k.
\]
Hence \(\min_v\nu_D(v)\le k\). Minimizing over all decompositions proves the claim. \(\square\)

This lemma involves the minimum local packing, not the paper's parameter
\[
c(D)=\max_v\nu_D(v).
\]
One cannot replace the minimum by \(c(D)\): a bidirected star with \(q\) leaves has directed tree-width \(1\), but its center lies on \(q\) openly disjoint digons.

---

## 3. Symmetric and almost-symmetric digraphs

Let
\[
b_D(v)=|N_D^+(v)\cap N_D^-(v)|
\]
be the number of bidirected neighbors of \(v\). The corresponding \(b_D(v)\) digons through \(v\) are openly disjoint, so Lemma 2.1 gives:

### Corollary 3.1
For every digraph \(D\),
\[
\boxed{\operatorname{dtw}(D)\ge \min_v b_D(v).}
\]

In particular, every symmetric \(r\)-regular digraph satisfies
\[
\operatorname{dtw}(D)\ge r.
\]
Since \(\overleftrightarrow{K}_{r+1}\) has a one-bag decomposition of width \(r\),
\[
\operatorname{dtw}(\overleftrightarrow{K}_{r+1})=r.
\]

Thus the optimal constant restricted to symmetric regular digraphs is exactly

\[
\boxed{\varepsilon_{\mathrm{sym}}=1.}
\]

More generally, if every vertex has at most \(s\) asymmetric out-neighbors, then
\[
\operatorname{dtw}(D)\ge r-s.
\]

There is also an order-dependent bound. If \(D\) has \(n\) vertices, then
\[
2r-b_D(v)=|N^+(v)\cup N^-(v)|\le n-1,
\]
and hence

\[
\boxed{\operatorname{dtw}(D)\ge \max\{0,\,2r-n+1\}.}
\]

This is useful for regular digraphs whose order is substantially below \(2r\).

---

## 4. Semicomplete regular digraphs

A digraph is semicomplete if every pair of distinct vertices is joined by at least one arc.

### Theorem 4.1
If \(D\) is an \(r\)-regular semicomplete digraph, then
\[
\boxed{\operatorname{dtw}(D)\ge \left\lceil\frac{r+1}{3}\right\rceil.}
\]

A sharper form is available. Put
\[
b=2r-|V(D)|+1.
\]
Then
\[
\operatorname{dtw}(D)\ge
\min\left\{
r,\,
\max\left\{
b,\,
\left\lceil\frac{2r-3b+2}{3}\right\rceil
\right\}
\right\}.
\]

#### Proof

Fix \(v\). Partition \(V(D)\setminus\{v\}\) as
\[
M=N^+(v)\cap N^-(v),\qquad
O=N^+(v)\setminus N^-(v),\qquad
I=N^-(v)\setminus N^+(v).
\]
Semicompleteness makes this a partition. If \(b=|M|\), then
\[
|O|=|I|=r-b
\]
and
\[
|V(D)|-1=b+2(r-b)=2r-b.
\]
Thus \(b=2r-|V(D)|+1\), independently of \(v\).

Let \(Z\) be a minimum vertex set meeting every directed cycle through \(v\), and put \(k=|Z|=\nu_D(v)\). Every vertex of \(M\) belongs to \(Z\), because each \(u\in M\) forms the digon \(vuv\). Hence
\[
b\le k.
\]

Assume \(k<r\), since otherwise the result is immediate. Define
\[
P=O\setminus Z,\qquad Q=I\setminus Z,
\]
with \(p=|P|\) and \(q=|Q|\). Neither set is empty: if, for example, \(P=\varnothing\), then \(Z\) contains \(M\cup O\), so \(k\ge r\).

There can be no arc from \(P\) to \(Q\), since such an arc would give a directed triangle
\[
v\to P\to Q\to v
\]
avoiding \(Z\). By semicompleteness, every pair in \(Q\times P\) is therefore oriented from \(Q\) to \(P\).

Sum the outdegrees of vertices in \(Q\). There are at least

* \(\binom q2\) arcs internal to \(Q\);
* \(pq\) arcs from \(Q\) to \(P\);
* \(q\) arcs from \(Q\) to \(v\).

Consequently
\[
qr\ge \binom q2+pq+q,
\]
which gives
\[
2r\ge 2p+q+1.
\]
Similarly, summing the indegrees of vertices in \(P\) gives
\[
2r\ge p+2q+1.
\]

Moreover,
\[
p+q=2r-b-k.
\]
Substitution yields
\[
p\le b+k-1,\qquad q\le b+k-1.
\]
Therefore
\[
2r-b-k=p+q\le 2b+2k-2,
\]
or equivalently
\[
3k\ge 2r-3b+2.
\]

Together with \(k\ge b\), this proves the sharper bound. Finally,
\[
3k+3b\ge 2r+2
\]
and \(b\le k\), so \(6k\ge2r+2\), giving
\[
k\ge\frac{r+1}{3}.
\]
This holds for every \(v\), so Lemma 2.1 completes the proof. \(\square\)

---

## 5. Regular tournaments

A regular tournament has \(2r+1\) vertices and is \(r\)-regular. The preceding proof with \(b=0\) gives a stronger estimate.

### Corollary 5.1
If \(T\) is an \(r\)-regular tournament, then
\[
\boxed{\operatorname{dtw}(T)\ge
\min\left\{r,\left\lceil\frac{2(r+1)}3\right\rceil\right\}.}
\]
In particular, for \(r\ge2\),
\[
\operatorname{dtw}(T)\ge \left\lceil\frac{2(r+1)}3\right\rceil.
\]

The local cycle-packing estimate is asymptotically sharp. For \(m\ge2\), set
\[
r=3m-1.
\]
Take disjoint sets \(A,B,X\) of sizes
\[
|A|=|B|=2m-1,\qquad |X|=2m,
\]
and an additional vertex \(v\). Orient \(A\) and \(B\) as regular tournaments. Orient \(X\) as an almost-regular tournament, with \(m\) vertices \(X^+\) of internal outdegree \(m\) and \(m\) vertices \(X^-\) of internal outdegree \(m-1\). Such a tournament is obtained by deleting one vertex from a regular tournament on \(2m+1\) vertices.

Orient the cross-arcs as
\[
B\to A,\qquad A\to X,\qquad X\to B,
\]
and
\[
B\to v\to A,\qquad v\to X^+,\qquad X^-\to v.
\]
A direct degree check shows that this is a regular tournament of degree \(3m-1\). Deleting \(X\) leaves
\[
B\to v\to A,\qquad B\to A,
\]
so \(X\) meets every directed cycle through \(v\). Hence
\[
\nu_T(v)\le 2m.
\]
Corollary 5.1 gives the reverse inequality, so
\[
\min_u\nu_T(u)=2m
\quad\text{and}\quad
\frac{\min_u\nu_T(u)}r=\frac{2m}{3m-1}\longrightarrow\frac23.
\]
This only proves sharpness of the local packing argument, not that these tournaments have directed tree-width \(2m\).

For comparison, the cyclic tournament \(C_{2r+1}\) has directed tree-width exactly \(r\). Indeed, writing its vertices modulo \(2r+1\) and orienting
\[
i\to i+1,\ldots,i+r,
\]
the \(r\) triangles
\[
0\to i\to r+i\to0,\qquad 1\le i\le r,
\]
are openly disjoint. Thus Lemma 2.1 gives \(\operatorname{dtw}\ge r\). On the other hand, deleting \(r\) consecutive vertices leaves a transitive tournament. A feedback vertex set of size \(r\) gives an arboreal decomposition of width at most \(r\), so equality follows.

---

## 6. Why the local lemma does not settle the general problem

The minimum local packing \(\min_v\nu_D(v)\) can be constant even in regular digraphs.

For every \(r\), take vertices \(v,x\) and two sets \(A,B\) of size \(r\). Let \(A\) and \(B\) each induce a complete bidirected graph, and add all arcs
\[
v\to A,\qquad A\to x,\qquad x\to B,\qquad B\to v.
\]
This is a simple \(r\)-regular digraph. Every directed cycle through \(v\) contains \(x\), so
\[
\nu_D(v)=1.
\]
Thus no linear global bound can follow solely from Lemma 2.1. The large directed tree-width is forced elsewhere in the decomposition—here, in particular, by the bidirected \(K_r\)'s.

Likewise, the quoted upper bound
\[
c_r\le 7\left\lceil\frac r8\right\rceil
\]
for openly disjoint cycles does not by itself imply an upper bound of \(7/8\) for directed tree-width. An explicit arboreal decomposition of the corresponding constructions would be needed.

The unresolved step is therefore genuinely global: one must either

1. improve the use of regularity across the entire arboreal decomposition, raising \(3/22\), or
2. construct simple \(r\)-regular digraphs with a certified decomposition of width strictly below \(r\).

This writeup achieves neither, so the optimal \(\varepsilon_*\) remains undetermined.

---

## 7. Convention caveat

If parallel arcs are allowed and counted in the degree, no positive constant exists. Take two vertices \(u,v\) with \(r\) parallel arcs in each direction. This is \(r\)-regular as a directed multigraph, but its directed tree-width is \(1\), independently of \(r\). Hence
\[
\inf_r\frac{\operatorname{dtw}(D_r)}r=0.
\]
Thus the positive-constant problem necessarily uses the source paper's simple-digraph convention.
