Attack the following open graph-theory problem.

Catalog id: 1611.02400__01
Catalog status: open (triage tier 2, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1611.02400__01/
Source paper: A Graph-Theoretic Approach to Multitasking (arXiv:1611.02400)

=== Catalog page (statement + literature review) ===
Multitasker threshold at average degree log n — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No paper resolving the open problem has been found. The follow-up work arXiv:1809.02835 (Multitasking Capacity: Hardness Results and Improved Constructions, published in SIAM J. Discrete Math.) proves hardness of approximation results and provides improved constructions achieving $\alpha = 1/2 - \varepsilon$ for matchings of size $n/\mathrm{poly}(d)$, but does not construct multitaskers with $\alpha > 0$ independent of $n$ at average degree $\Theta(\log n)$. The specific threshold question — whether $\Theta(\log n)$ average degree suffices for constant $\alpha$ — remains open as of the search date.

 Cited literature (1)

 
 
 
partial Multitasking Capacity: Hardness Results and Improved Constructions
 (2018)
 

 
 Noga Alon, Jonathan D. Cohen, Biswadip Dey, Tom Griffiths, Sebastian Musslick, Kayhan Ozcimder, Daniel Reichman, Igor Shinkar, Tal Wagner · arXiv preprint (published in SIAM Journal on Discrete Mathematics) · arXiv:1809.02835

Proves computational hardness for approximating multitasking capacity and gives improved constructions achieving $\alpha = 1/2 - \varepsilon$ for matchings of size $n/\mathrm{poly}(d)$, but does not resolve the $\Theta(\log n)$ average-degree threshold question.
 

 

 Reviewer notes. The main follow-up paper arXiv:1809.02835 was verified via WebFetch; it improves constructions and proves hardness but does not address the specific open problem about $\Theta(\log n)$ average degree. No other paper specifically resolving this threshold question was found in the search.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. It is an interesting question whether there exists a multitasker with $\alpha > 0$ independent of $n$, for average degree $\Theta(\log n)$, which, if true is the largest average degree possible. This is left as an open problem.

Context

The paper shows there exist multitaskers of average degree $\Omega(\log\log n)$ with $\alpha > 1/3 - \varepsilon$, and that for the multitasking capacity to decay with average degree $d$ one must assume $d$ grows faster than $\log\log n$. The question is whether the threshold can be pushed up to $\Theta(\log n)$.

Notes. Statement appears in running prose without a labelled environment; PDF source.

Source paper

 A Graph-Theoretic Approach to Multitasking
 Noga Alon, Jonathan D. Cohen, Biswadip Dey, Tom Griffiths, Sebastian Musslick, Kayhan Ozcimder, Daniel Reichman, Igor Shinkar, Tal Wagner · 2017-06-09
 https://arxiv.org/abs/1611.02400
 PDF source

=== Source paper abstract / header ===
Abstract:A key feature of neural network architectures is their ability to support the simultaneous interaction among large numbers of units in the learning and processing of representations. However, how the richness of such interactions trades off against the ability of a network to simultaneously carry out multiple independent processes -- a salient limitation in many domains of human cognition -- remains largely unexplored. In this paper we use a graph-theoretic analysis of network architecture to address this question, where tasks are represented as edges in a bipartite graph $G=(A \cup B, E)$. We define a new measure of multitasking capacity of such networks, based on the assumptions that tasks that \emph{need} to be multitasked rely on independent resources, i.e., form a matching, and that tasks \emph{can} be multitasked without interference if they form an induced matching. Our main result is an inherent tradeoff between the multitasking capacity and the average degree of the network that holds \emph{regardless of the network architecture}. These results are also extended to networks of depth greater than $2$. On the positive side, we demonstrate that networks that are random-like (e.g., locally sparse) can have desirable multitasking properties. Our results shed light into the parallel-processing limitations of neural systems and provide insights that may be useful for the analysis and design of parallel architectures.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1611.02400 [cs.DM]
 

 
  
 (or 
 arXiv:1611.02400v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1611.02400
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Reichman [view email] 
 [v1]
 Tue, 8 Nov 2016 06:06:36 UTC (35 KB)

 [v2]
 Fri, 9 Jun 2017 15:57:19 UTC (35 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A Graph-Theoretic Approach to Multitasking, by Noga Alon and Jonathan D. Cohen and Biswadip Dey and Tom Griffiths and Sebastian Musslick and Kayhan Ozcimder and Daniel Reichman and Igor Shinkar and Tal Wagner
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
 | 2016-11
 

 Change to browse by:
 
 cs
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Jonathan D. Cohen
Biswadip Dey
Tom Griffiths
Sebastian Musslick
Kayhan Özcimder …

 

 

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
  "one_line": "The logarithmic-degree question remains open, but the endpoint alpha=1/2 has a sharp constant threshold: every balanced 1/2-multitasker has average degree below 4, and examples approach 4.",
  "would_publish": false,
  "caveats": "This does not decide any fixed alpha below 1/2, including the approximately 1/3 regime, and novelty relative to implicit observations in the source was not verified."
}
```

# 1. Statement and notation

Let \(G=(A\cup B,E)\) be a finite simple bipartite graph. For a matching \(M\), let
\[
\operatorname{im}(M)
 =\max\{|M'|:M'\subseteq M\text{ is an induced matching in }G\}.
\]
Define the multitasking capacity
\[
\operatorname{mt}(G)
 =\min_{\varnothing\ne M\subseteq E\atop M\text{ a matching}}
   \frac{\operatorname{im}(M)}{|M|}.
\]
Thus \(G\) is an \(\alpha\)-multitasker exactly when
\(\operatorname{mt}(G)\ge \alpha\).

In the balanced convention \(|A|=|B|=n\), the average degree is
\[
d(G)=\frac{|E|}{n},
\]
which is also the ordinary average degree because \(G\) has \(2n\) vertices.

The catalogued problem asks whether there are graphs with
\[
d(G)=\Theta(\log n)
\quad\text{and}\quad
\operatorname{mt}(G)\ge \alpha_0>0
\]
for an absolute constant \(\alpha_0\).

I do not resolve this. I prove a sharp endpoint result for
\(\alpha_0=1/2\), together with a general structural obstruction for arbitrary fixed \(\alpha_0\).

---

# 2. Conflict graphs

Given a matching
\[
M=\{e_i=a_i b_i:i\in I\},
\]
define its conflict graph \(C_G(M)\) on vertex set \(M\) by joining
\(e_i\) and \(e_j\) when at least one cross-edge
\[
a_i b_j,\qquad a_j b_i
\]
belongs to \(G\).

Then
\[
M'\subseteq M\text{ is induced in }G
\quad\Longleftrightarrow\quad
M'\text{ is independent in }C_G(M).
\]
Moreover, for every \(M'\subseteq M\),
\[
C_G(M')[M']=C_G(M)[M'].
\]

Consequently, \(G\) is a \(1/2\)-multitasker if and only if every conflict graph \(C_G(M)\) is bipartite. Indeed, if a conflict graph is bipartite, one of its two color classes has at least half its vertices. Conversely, if some conflict graph is nonbipartite, take a shortest odd cycle in it. This cycle is induced, and on \(2k+1\) vertices it has independence number \(k<(2k+1)/2\).

---

# 3. A sharp theorem at \(\alpha=1/2\)

## Theorem 1

Let \(G\) be a bipartite graph on \(N\ge3\) vertices. If
\[
\operatorname{mt}(G)\ge\frac12,
\]
then:

1. \(G\) contains no cycle whose length is congruent to \(2\pmod 4\);
2. \(G\) is \(2\)-degenerate;
3. consequently,
   \[
   |E(G)|\le 2N-4.
   \]

In particular, if \(|A|=|B|=n\), then
\[
d(G)=\frac{|E(G)|}{n}\le 4-\frac4n.
\]

The constant \(4\) is asymptotically best possible.

### Proof

#### Step 1: cycles of length \(2\bmod 4\) are forbidden

Suppose \(G\) contains a cycle \(C\) of length
\[
4k+2=2(2k+1).
\]
Take every other edge of \(C\). This gives a matching \(M\) of size
\(2k+1\).

The unused cycle edges make the corresponding vertices of \(C_G(M)\)
span an odd cycle of length \(2k+1\). Chords of \(C\), if present, only
add further conflict edges. Therefore
\[
\operatorname{im}(M)
 \le \alpha(C_{2k+1})
 =k
 <\frac{2k+1}{2}.
\]
This contradicts \(\operatorname{mt}(G)\ge1/2\). Hence no such cycle exists.

#### Step 2: absence of these cycles implies \(2\)-degeneracy

We prove the following elementary lemma.

**Lemma.** Every bipartite graph with no cycle of length \(2\bmod4\)
has a vertex of degree at most \(2\).

Suppose otherwise that a bipartite graph \(H\) has minimum degree at
least \(3\). Let
\[
P=v_0v_1\cdots v_\ell
\]
be a longest path. Every neighbor of \(v_0\) lies on \(P\). Since
\(\deg(v_0)\ge3\), besides \(v_1\) there are two neighbors
\(v_i,v_j\), where
\[
3\le i<j.
\]
Bipartiteness implies that \(i\) and \(j\) are odd.

The edge \(v_0v_i\), together with
\(v_0v_1\cdots v_i\), forms a cycle of length \(i+1\). Since this
length is even but not \(2\bmod4\), we must have
\[
i+1\equiv0\pmod4,
\qquad\text{so}\qquad
i\equiv3\pmod4.
\]
Likewise \(j\equiv3\pmod4\).

But the two edges \(v_0v_i,v_0v_j\), together with the section of
\(P\) from \(v_i\) to \(v_j\), form a cycle of length
\[
(j-i)+2\equiv2\pmod4,
\]
a contradiction. This proves the lemma.

Every subgraph of \(G\) also has no cycle of length \(2\bmod4\), so the
lemma applies to every subgraph. Thus \(G\) is \(2\)-degenerate.

#### Step 3: edge count

A \(2\)-degenerate graph has an ordering in which each vertex has at
most two later neighbors. This gives the preliminary bound
\[
|E(G)|\le 2N-3.
\]
Equality would require the third-last vertex to be adjacent to both of
the final two vertices and the final two vertices to be adjacent to
each other. Those three vertices would form a triangle. Since \(G\)
is bipartite, equality is impossible, and hence
\[
|E(G)|\le2N-4.
\]
For \(N=2n\), this becomes
\[
d(G)=\frac{|E(G)|}{n}\le4-\frac4n.
\]
This proves the upper bound. \(\square\)

---

# 4. Asymptotic sharpness

For \(m\ge2\), let
\[
G_m=K_{2,m}\ \dot\cup\ K_{m,2},
\]
where the \(2\)-vertex side of the first component and the \(m\)-vertex
side of the second component are placed in \(A\). Then
\[
|A|=|B|=m+2=:n
\]
and
\[
|E(G_m)|=4m.
\]
Thus
\[
d(G_m)=\frac{4m}{m+2}
      =4-\frac8n.
\]

Every matching in either component has size at most \(2\). From a
two-edge matching in \(K_{2,m}\), either one edge is an induced
matching, while the two edges together are not induced. Choosing
independently in the two components therefore gives an induced
submatching of at least half of every matching.

Conversely, a two-edge matching inside one \(K_{2,m}\) component has
no induced two-edge submatching. Hence
\[
\operatorname{mt}(G_m)=\frac12.
\]

Therefore the constant \(4\) in Theorem 1 is asymptotically sharp.

---

# 5. The stricter regime \(\alpha>1/2\)

There is a further rigidity phenomenon.

## Proposition 2

If
\[
\operatorname{mt}(G)>\frac12,
\]
then every connected component of \(G\) is a star or an isolated
vertex. In particular, every matching of \(G\) is already induced, so
\[
\operatorname{mt}(G)=1.
\]

### Proof

If two disjoint edges have a cross-edge between their endpoints, they
form a two-edge matching whose largest induced submatching has size
\(1\). Its ratio is exactly \(1/2\).

Thus \(\operatorname{mt}(G)>1/2\) implies that no such pair exists.
In particular, \(G\) contains no three-edge path \(P_4\), since the
first and last edges of that path would be a conflicting matching.
A connected bipartite graph with no \(P_4\) as a subgraph is a star.
The conclusion follows. \(\square\)

For balanced graphs this gives \(d(G)<2\). This is also asymptotically
sharp, using
\[
K_{1,m}\ \dot\cup\ K_{m,1}.
\]

Thus there is no growing-degree construction with capacity at least
\(1/2\), and capacity strictly above \(1/2\) collapses all the way to
star forests.

---

# 6. A general obstruction for arbitrary fixed \(\alpha\)

The following does not settle the conjecture, but rules out
constructions in which the edge set is supported by a very small
vertex cover.

Let
\[
s=\min\{t\in\mathbb N:\alpha t>1\}
  =\left\lfloor\frac1\alpha\right\rfloor+1.
\]

## Proposition 3

If \(G\) is an \(\alpha\)-multitasker, then \(G\) is \(K_{s,s}\)-free.

If additionally \(|A|=|B|=n\), \(d=|E(G)|/n\), and \(\nu(G)\) is the
maximum matching size, then
\[
d\le (s-1)+[2(s-1)]^{1/s}\nu(G)^{\,1-1/s}.
\]
Consequently, for \(d>s-1\),
\[
\nu(G)\ge
\left(
 \frac{d-(s-1)}{[2(s-1)]^{1/s}}
\right)^{s/(s-1)}.
\]

In particular, if \(d=\Theta(\log n)\) and \(\alpha\) is fixed, then
\[
\nu(G)=\Omega_\alpha\!\left(
(\log n)^{s/(s-1)}
\right).
\]

### Proof

A perfect matching of a \(K_{s,s}\) has size \(s\), while any two of
its edges conflict. Its largest induced submatching therefore has size
\(1\). Since \(1/s<\alpha\), an \(\alpha\)-multitasker cannot contain
\(K_{s,s}\).

We use the following elementary asymmetric Zarankiewicz estimate. If
\(H=(X,Y)\) is \(K_{s,s}\)-free with \(|X|=r\), \(|Y|=n\), then
\[
|E(H)|
 \le (s-1)r+(s-1)^{1/s}nr^{1-1/s}.                 \tag{1}
\]
Indeed, writing \(d_x=\deg_H(x)\), every \(s\)-subset of \(Y\) has at
most \(s-1\) common neighbors, so
\[
\sum_{x\in X}\binom{d_x}{s}
 \le (s-1)\binom ns.
\]
Putting \(z_x=\max\{d_x-s+1,0\}\), one has
\[
\binom{d_x}{s}\ge \frac{z_x^s}{s!}.
\]
Hölder's inequality then gives (1).

By König's theorem, \(G\) has a vertex cover \(C\) of size
\(\nu(G)\). Write
\[
C_A=C\cap A,\qquad C_B=C\cap B,
\]
with sizes \(r_A,r_B\). Assign every edge incident with \(C_A\) to one
subgraph and all remaining edges to a second subgraph; every edge in
the second subgraph is incident with \(C_B\). Applying (1) twice gives
\[
|E(G)|
 \le (s-1)(r_A+r_B)
 +(s-1)^{1/s}n
 \left(r_A^{1-1/s}+r_B^{1-1/s}\right).
\]
Since \(r_A+r_B=\nu(G)\) and
\[
r_A^{1-1/s}+r_B^{1-1/s}
 \le 2^{1/s}\nu(G)^{1-1/s},
\]
the claimed inequality follows. \(\square\)

---

# 7. Remaining gap

The main logarithmic-degree problem remains untouched in its essential
range. Theorem 1 only rules out the endpoint
\(\alpha\ge1/2\); the conjecture asks for any positive constant, and
the known constructions discussed in the prompt operate near
\(\alpha=1/3\).

Proposition 3 shows that a putative construction cannot obtain
average degree \(\Theta(\log n)\) merely by placing all edges around
\(O(\log n)\) hub vertices: its maximum matching, equivalently its
minimum vertex-cover size, must be superlogarithmic. This is far from
an impossibility result, since it still permits matchings of size
\(n^{\Omega(1)}\) or linear size.

Thus no construction with constant \(\alpha<1/2\), and no upper bound
excluding such a construction at average degree \(\Theta(\log n)\),
is obtained here.
