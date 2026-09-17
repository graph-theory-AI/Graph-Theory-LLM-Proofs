Attack the following open graph-theory problem.

Catalog id: 1903.04761__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1903.04761__01/
Source paper: On the Maximum Weight Independent Set Problem in graphs without induced… (arXiv:1903.04761)

=== Catalog page (statement + literature review) ===
FPT Algorithm for MWIS in (Long-Hole, k-Prism)-Free Graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 low confidence
 

 The source paper provides a polynomial-time n^{O(k)} algorithm for MWIS in (long-hole, k-prism)-free graphs and remarks that the authors do not see how to upgrade this to an FPT algorithm parameterized by k without invoking a structural result of Abrishami et al. Targeted searches across arXiv and related literature through 2026 found no follow-up paper that resolves this FPT question either positively or negatively. The problem is 6 years old, so absence of evidence may be indicative of genuine difficulty.

 Reviewer notes. No follow-up found. The open question is whether the n^{O(k)} algorithm of Theorem 1.1 can be made FPT in k for MWIS in (long-hole, k-prism)-free graphs. The authors note that invoking Abrishami et al. [1] (likely the series on induced subgraphs and tree decompositions of even-hole-free graphs) might be a path forward, but no paper appears to have completed this. Related progress exists on adjacent classes (no long claws, even-hole-free) but not on this specific class.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We do not see how to turn Theorem 1.1 into an FPT-algorithm (without using the result of [1]).

Context

Theorem 1.1 gives a polynomial-time algorithm running in time $n^{O(k)}$ for MWIS in (long-hole, $k$-prism)-free $n$-vertex graphs for any fixed integer $k > 0$. Immediately after stating the theorem the authors remark that extending this to a fixed-parameter tractable algorithm parameterized by $k$ appears to be out of reach with their techniques, unless the result of Abrishami et al. [1] is invoked.

Notes. Implicit open question stated in prose without a labelled environment. PDF source — math may be garbled.

Source paper

 On the Maximum Weight Independent Set Problem in graphs without induced cycles of length at least five
 Maria Chudnovsky, Marcin Pilipczuk, Michał Pilipczuk, Stéphan Thomassé · 2020-01-16
 https://arxiv.org/abs/1903.04761
 PDF source

=== Source paper abstract / header ===
Abstract:A hole in a graph is an induced cycle of length at least $4$, and an antihole is the complement of an induced cycle of length at least $4$. A hole or antihole is long if its length is at least $5$. For an integer $k$, the $k$-prism is the graph consisting of two cliques of size $k$ joined by a matching. The complexity of Maximum (Weight) Independent Set (MWIS) in long-hole-free graphs remains an important open problem. In this paper we give a polynomial time algorithm to solve MWIS in long-hole-free graphs with no $k$-prism (for any fixed integer $k$), and a subexponential algorithm for MWIS in long-hole-free graphs in general. As a special case this gives a polynomial time algorithm to find a maximum weight clique in perfect graphs with no long antihole, and no hole of length $6$. The algorithms use the framework of minimal chordal completions and potential maximal cliques.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1903.04761 [cs.DM]
 

 
  
 (or 
 arXiv:1903.04761v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1903.04761
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Marcin Pilipczuk [view email] 
 [v1]
 Tue, 12 Mar 2019 07:37:40 UTC (271 KB)

 [v2]
 Thu, 16 Jan 2020 08:49:20 UTC (402 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the Maximum Weight Independent Set Problem in graphs without induced cycles of length at least five, by Maria Chudnovsky and 3 other authors
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
 | 2019-03
 

 Change to browse by:
 
 cs
 cs.DS
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Maria Chudnovsky
Marcin Pilipczuk
Michal Pilipczuk
Stéphan Thomassé 

 

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
  "one_line": "The FPT question remains unresolved, but there are long-hole-free k-prism-free graphs with n^{Omega(k)} minimal separators and potential maximal cliques, ruling out any FPT upgrade that explicitly enumerates all of them.",
  "would_publish": false,
  "caveats": "No FPT algorithm or parameterized hardness proof is obtained; the lower bound only obstructs explicit separator/PMC enumeration, and the precise theorem cited as [1] was not supplied."
}
```

# 1. Formal statement

Write \(\mathsf{Pr}_k\) for the \(k\)-prism: two \(k\)-cliques joined by exactly a perfect matching. I interpret the question as asking for an algorithm with running time
\[
f(k)\,n^{O(1)}
\]
for MWIS on the promise class
\[
\{G:\ G\text{ has no induced hole of length at least }5
       \text{ and no induced }\mathsf{Pr}_k\}.
\]

I do not obtain such an algorithm or a hardness proof. I do obtain an explicit obstruction showing that the \(n^{O(k)}\) potential-maximal-clique approach cannot in general be made FPT merely by speeding up the enumeration.

# 2. The first two parameter values

These are completely tractable.

- \(\mathsf{Pr}_1=K_2\). Thus a \(\mathsf{Pr}_1\)-free graph is edgeless.
- \(\mathsf{Pr}_2=C_4\). A graph with neither an induced \(C_4\) nor an induced cycle of length at least \(5\) is chordal. MWIS is polynomial-time solvable on chordal graphs, for example by dynamic programming over a clique tree.

Thus \(k=3\) is the first nontrivial case.

Also, every chordal graph is \(\mathsf{Pr}_k\)-free for every \(k\geq 2\), since every \(\mathsf{Pr}_k\) contains an induced \(\mathsf{Pr}_2=C_4\).

# 3. An \(n^{\Omega(k)}\) lower bound for explicit separator/PMC enumeration

## Theorem

For all integers \(r,q\geq 2\), there is a graph \(G_{r,q}\) on
\[
n=2rq
\]
vertices such that:

1. \(G_{r,q}\) is long-hole-free;
2. \(G_{r,q}\) is \(\mathsf{Pr}_{r+1}\)-free;
3. \(G_{r,q}\) has at least \((q-1)^r\) distinct minimal separators;
4. \(G_{r,q}\) has at least \((q-1)^r\) distinct potential maximal cliques;
5. nevertheless, MWIS on \(G_{r,q}\) is solvable in \(O(n^2)\) time.

Consequently, with \(k=r+1\),
\[
(q-1)^r\geq \left(\frac{n}{4(k-1)}\right)^{k-1}.
\]
Therefore no algorithm that explicitly lists all minimal separators, or all potential maximal cliques, can run in time \(f(k)n^c\) for a universal constant \(c\).

## Construction

Let
\[
A_i=\{a_i^1,\dots,a_i^q\},\qquad
B_i=\{b_i^1,\dots,b_i^q\}
\]
for \(i=1,\dots,r\), and put
\[
A=\bigcup_{i=1}^r A_i,\qquad B=\bigcup_{i=1}^r B_i.
\]

Make both \(A\) and \(B\) cliques. Between \(A\) and \(B\), put
\[
a_i^p b_j^s\in E(G_{r,q})
\quad\Longleftrightarrow\quad
i=j\ \text{ and }\ p\leq s.
\]

Thus the bipartite graph of cross-edges is the disjoint union of \(r\) chain graphs.

## Long-hole-freeness

Every co-bipartite graph is long-hole-free. Indeed, in an induced cycle of length at least \(5\), one of the two clique parts contains at least three cycle vertices. Two of these are nonconsecutive on the cycle, and their clique edge is a chord.

Hence \(G_{r,q}\) has no induced cycle of length at least \(5\).

## Exclusion of \(\mathsf{Pr}_{r+1}\)

Let \(H\) be the bipartite graph consisting of the cross-edges between \(A\) and \(B\).

For \(s\geq3\), an induced \(\mathsf{Pr}_s\) in a co-bipartite graph corresponds to an induced matching of size \(s\) in \(H\). To justify the possible choice of co-bipartition, observe that the complement of \(\mathsf{Pr}_s\) is the connected crown graph \(K_{s,s}\) minus a perfect matching. Its bipartition is unique up to reversal, so its two parts must agree with the fixed bipartition \(A,B\) in \(\overline{G_{r,q}}\).

Within one block \(H[A_i,B_i]\), there is no induced matching of size two. Indeed, if
\[
a_i^p b_i^s,\quad a_i^{p'}b_i^{s'}
\]
are two disjoint edges and \(p\leq p'\), then \(p'\leq s'\), hence \(p\leq s'\), so \(a_i^p b_i^{s'}\) is an additional cross-edge.

Thus an induced matching in \(H\) uses at most one edge from each block. Its size is at most \(r\), and therefore \(G_{r,q}\) is \(\mathsf{Pr}_{r+1}\)-free. In fact, choosing one edge from each block gives an induced \(\mathsf{Pr}_r\), so the parameter is tight.

## Many minimal separators

For a vector
\[
t=(t_1,\dots,t_r)\in\{1,\dots,q-1\}^r,
\]
define
\[
\begin{aligned}
A_t^-&=\{a_i^p:p\leq t_i\},&
A_t^+&=\{a_i^p:p>t_i\},\\
B_t^-&=\{b_i^s:s\leq t_i\},&
B_t^+&=\{b_i^s:s>t_i\},
\end{aligned}
\]
and set
\[
S_t=A_t^-\cup B_t^+.
\]

Then
\[
G_{r,q}-S_t=G[A_t^+\cup B_t^-].
\]
Both \(A_t^+\) and \(B_t^-\) are nonempty cliques, and there are no edges between them: in the same block one has \(p>t_i\geq s\), and distinct blocks have no cross-edges.

Moreover, every vertex of \(S_t\) has a neighbor in each component:

- If \(a_i^p\in A_t^-\), it is adjacent to all of \(A_t^+\) and to \(b_i^{t_i}\in B_t^-\).
- If \(b_i^s\in B_t^+\), it is adjacent to all of \(B_t^-\) and to \(a_i^{t_i+1}\in A_t^+\).

Thus \(A_t^+\) and \(B_t^-\) are two full components associated with \(S_t\), so \(S_t\) is a minimal separator. Distinct vectors \(t\) give distinct separators. Hence there are at least
\[
(q-1)^r
\]
minimal separators.

## Many potential maximal cliques

Fix \(t\), put
\[
x_t=a_1^{t_1+1},
\qquad
\Omega_t=S_t\cup\{x_t\}.
\]

I construct a minimal chordal completion in which \(\Omega_t\) is a maximal clique.

Order the vertices of \(A\) as
\[
u_1,\dots,u_{rq}
\]
so that:

1. within each \(A_i\), the order is
   \[
   a_i^1,a_i^2,\dots,a_i^q;
   \]
2. all vertices of \(A_t^-\) occur first;
3. \(x_t\) occurs immediately afterward;
4. all remaining vertices occur after \(x_t\).

For a vertex \(u_j\), define its new cross-neighborhood by
\[
N_{\widehat H}(u_j)
   =\bigcup_{\ell\geq j}N_H(u_\ell),
\]
and let \(\widehat G\) be obtained from \(G_{r,q}\) by adding these cross-edges.

The neighborhoods in \(\widehat H\) are nested:
\[
N_{\widehat H}(u_1)\supseteq
N_{\widehat H}(u_2)\supseteq\cdots.
\]
Hence \(\widehat H\) has no induced \(2K_2\). A co-bipartite graph is chordal exactly when its cross-edge graph has no induced \(2K_2\), so \(\widehat G\) is chordal.

The completion is inclusion-minimal. Let \(u_jb\) be an added edge, with \(u_j=a_i^p\). There is some \(\ell>j\) such that \(u_\ell b\) was an original edge. Necessarily \(u_\ell\) belongs to a block different from \(i\); otherwise the order inside \(A_i\) would imply that \(u_jb\) was already present. Let
\[
c=b_i^p.
\]
Then \(u_jc\) and \(u_\ell b\) are original edges, while \(u_\ell c\notin E(\widehat G)\). If the fill edge \(u_jb\) is removed, the four vertices
\[
u_j,u_\ell,b,c
\]
induce a \(C_4\). Its cycle edges are original edges, so removing additional fill edges cannot destroy this \(C_4\). Hence every fill edge is necessary.

If \(x_t=u_j\), then by construction
\[
N_{\widehat H}(x_t)=B_t^+.
\]
Every vertex preceding \(x_t\) is adjacent to all of \(B_t^+\), so \(\Omega_t\) is a clique in \(\widehat G\).

It is maximal:

- A vertex of \(B_t^-\) is not adjacent to \(x_t\).
- Every \(A\)-vertex appearing after \(x_t\) misses a private \(B_t^+\)-neighbor lost at some preceding step of the nested-neighborhood order.

Thus \(\Omega_t\) is a maximal clique in a minimal chordal completion, i.e. a potential maximal clique. Again \(B_i\cap\Omega_t=\{b_i^{t_i+1},\dots,b_i^q\}\) recovers \(t_i\), so the \(\Omega_t\) are distinct.

Therefore \(G_{r,q}\) has at least \((q-1)^r\) potential maximal cliques.

## Consequence for FPT enumeration

Set \(k=r+1\). Since \(q-1\geq q/2\),
\[
(q-1)^r\geq\left(\frac q2\right)^r
 =\left(\frac{n}{4r}\right)^r
 =\left(\frac{n}{4(k-1)}\right)^{k-1}.
\]

Suppose all minimal separators or all PMCs could be explicitly listed in time \(f(k)n^c\). Choose \(r>c\) and then let \(q\) tend to infinity. The number of output objects grows as \(q^r\), while \(f(r+1)n^c=O_{r,f}(q^c)\), a contradiction.

This is an unconditional output-size obstruction.

## Why this is not a hardness result for MWIS

The graph \(G_{r,q}\) is co-bipartite, so every independent set has size at most two. Therefore
\[
\alpha_w(G_{r,q})
 =
 \max\left\{
 0,\ \max_v w(v),\
 \max_{\substack{a\in A,\ b\in B\\ab\notin E}}
 \bigl(w(a)+w(b)\bigr)
 \right\},
\]
which is computable in \(O(n^2)\).

Thus the large number of PMCs reflects redundancy of the explicit triangulation framework, not intrinsic hardness of MWIS.

# 4. Further structural obstructions and reductions

## Ordinary treewidth cannot be bounded by \(k\)

For every fixed \(k\geq3\), the graph \(K_{m,m}\) is:

- long-hole-free, since every cycle of length at least six has chords;
- \(\mathsf{Pr}_k\)-free, since it is triangle-free while \(\mathsf{Pr}_k\) contains a triangle;
- of treewidth \(m\).

The equality \(\operatorname{tw}(K_{m,m})=m\) follows from the standard width-\(m\) decomposition and a \(K_{m+1}\)-minor obtained from \(m-1\) paired branch sets together with one unpaired vertex on each side.

Therefore a direct theorem asserting ordinary treewidth bounded solely by \(k\) is impossible, even with clique number two. Any use of a tree-decomposition theorem must allow tractable large biclique or chordal torsos, or use a different width measure.

## Clique cutsets are not the main difficulty

At a clique adhesion \(S\), an independent set meets \(S\) in either no vertex or exactly one vertex. Thus a dynamic program needs only \(|S|+1\) boundary states.

More explicitly, if a child contribution is \(M(\bot)\) when no vertex of \(S\) is chosen and \(M(s)\) when \(s\in S\) is chosen, then one may use \(M(\bot)\) as a baseline and add
\[
M(s)-M(\bot)
\]
to the effective weight of \(s\). Because \(S\) is a clique, at most one such adjustment is selected. Consequently, an FPT routine for induced subgraphs of clique-cutset atoms lifts through a clique-cutset decomposition with only polynomial overhead.

Thus a structural attack can focus on clique-cutset-free atoms.

## Perfect atoms are already tractable

The target graphs have no odd hole. By the Strong Perfect Graph Theorem, every nonperfect target graph therefore contains an odd antihole; a \(5\)-antihole is a \(C_5\), so its length is at least seven. Weighted independent set is polynomial-time solvable on perfect graphs.

Hence the unresolved atom routine may be restricted to nonperfect, clique-cutset-free graphs containing an odd antihole of length at least seven.

This does not bound the antihole length in terms of \(k\). Indeed, for every odd \(\ell\geq7\), \(\overline{C_\ell}\) is long-hole-free and \(\mathsf{Pr}_3\)-free:

- An induced cycle of length \(m\geq6\) would require each cycle vertex to have at least three nonneighbors inside the cycle, whereas every vertex of \(\overline{C_\ell}\) has only two nonneighbors.
- An induced \(C_5\) would force the chosen set to be closed under both neighbors in \(C_\ell\), which is impossible unless \(\ell=5\).
- An induced \(\mathsf{Pr}_3\) would complement to an induced \(C_6\) in \(C_\ell\), but a proper induced subgraph of a cycle is a disjoint union of paths.

# 5. What remains open

The construction proves that the \(n^{O(k)}\) exponent is unavoidable for any algorithm that individually enumerates every minimal separator or every potential maximal clique. It does not rule out:

- selecting only a small set of PMCs relevant to an optimal independent set;
- representing the \(n^{\Theta(k)}\) PMCs implicitly;
- a decomposition into chordal, bipartite, or otherwise tractable torsos;
- a completely different FPT algorithm.

Finally, the catalog excerpt does not state the precise theorem of Abrishami et al. The qualification “without using [1]” is methodological rather than an algorithmic property. If that theorem already gives a constructive \(f(k)n^{O(1)}\) decomposition and an MWIS dynamic program, then the existential FPT question would already be resolved. Without its exact statement and running-time consequences, I cannot responsibly make that claim.
