Attack the following open graph-theory problem.

Catalog id: 2506.08810__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2506.08810__01/
Source paper: Infinite induced-saturated graphs (arXiv:2506.08810)

=== Catalog page (statement + literature review) ===
Disconnectedness of H-free graphs adjacency structure — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 22 from arXiv:2506.08810 asks for which finite graphs H the flip graph G_{H,n} (whose vertices are H-free graphs on [n] and whose edges connect graphs differing by exactly one edge) is disconnected for all sufficiently large n. The paper itself establishes that G_{P_4,n} is connected for all n≥1, ruling out universal disconnectedness. No follow-up paper addressing this problem was found in the indexed literature as of May 2026.

 Reviewer notes. No follow-up work found. Semantic Scholar returns zero citations for arXiv:2506.08810 as of May 2026. The paper appeared in the Canadian Journal of Mathematics. The problem is recent (posted June 2025) and is a weaker relaxation of H-induced-saturation: an H-induced-saturated graph on n vertices corresponds to an isolated vertex in G_{H,n}, so disconnectedness of G_{H,n} is strictly weaker. The only known case mentioned in the paper is that G_{P_4,n} is connected for all n≥1.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. For a finite graph $H$ and integer $n$, let $G_{H,n}$ denote the graph with the $H$-free graphs on vertex set $[n]$ as vertices, and with an edge between $G,G^{\prime}\in V(G_{H,n})$ if and only if $|E(G)\triangle E(G^{\prime})|=1$. For which $H$ is $G_{H,n}$ disconnected for all sufficiently large $n$?

Context

An $H$-induced-saturated graph on $n$ vertices corresponds to an isolated vertex in $G_{H,n}$; disconnectedness is a weaker but potentially more tractable property. The authors note that $G_{P_4,n}$ is connected for all $n\geq 1$, so disconnectedness is not universal.

Source paper

 Infinite induced-saturated graphs
 Marthe Bonamy, Carla Groenland, Tom Johnston, Natasha Morrison, Alex Scott · 2025-09-01
 https://arxiv.org/abs/2506.08810

=== Source paper abstract / header ===
Abstract:A graph $G$ is $H$-induced-saturated if $G$ is $H$-free but deleting any edge or adding any edge creates an induced copy of $H$. There are non-trivial graphs $H$, such as $P_4$, for which no finite $H$-induced-saturated graph $G$ exists. We show that for every finite graph $H$ that is not a clique or an independent set, there always exists a countable $H$-induced-saturated graph. In fact, we show that a far stronger property can be achieved: there is a countably infinite $H$-free graph $G$ such that any graph $G'\ne G$ obtained by making a locally finite set of changes to $G$ contains a copy of $H$.
 

 
 
 
 Comments:
 26 pages, 13 figures
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2506.08810 [math.CO]
 

 
  
 (or 
 arXiv:2506.08810v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2506.08810
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Carla Groenland [view email] 
 [v1]
 Tue, 10 Jun 2025 14:00:59 UTC (34 KB)

 [v2]
 Wed, 20 Aug 2025 10:44:56 UTC (36 KB)

 [v3]
 Mon, 1 Sep 2025 10:23:31 UTC (36 KB)

 

 
 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Infinite induced-saturated graphs, by Marthe Bonamy and Carla Groenland and Tom Johnston and Natasha Morrison and Alex Scott
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Ancillary-file links:
 Ancillary files (details):

 small_graphs.py
 theorem_10.py

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2025-06
 

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
  "one_line": "I prove upward persistence of disconnectedness, completely classify graphs H with at most four vertices, and give induced-saturated constructions for all induced stars and a multipartite family.",
  "would_publish": false,
  "caveats": "The characterization for arbitrary H remains open; H-free is interpreted as induced-H-free, and the one-vertex H is convention-dependent."
}
```

# 1. Statement of the partial results

Throughout, “\(H\)-free” means **induced-\(H\)-free**, as required by the induced-saturation context. Write \(\mathcal G_{H,n}\) for the flip graph in the question.

I prove the following.

### Theorem A: persistence in \(n\)

Let \(|V(H)|\ge 2\). If \(\mathcal G_{H,n}\) is disconnected for some \(n\), then \(\mathcal G_{H,m}\) is disconnected for every \(m\ge n\).

Thus the phrase “for all sufficiently large \(n\)” can equivalently be replaced by “for at least one \(n\).”

### Theorem B: the first possible order

Let \(h=|V(H)|\ge 3\). Then
\[
\mathcal G_{H,h}\text{ is disconnected}
\quad\Longleftrightarrow\quad
|E(H)|\in\left\{1,\binom h2-1\right\}.
\]

In particular, if \(H\) is neither a one-edge graph nor the complement of a one-edge graph, then any disconnection must first occur at some \(n>h\).

### Theorem C: complete classification for \(|V(H)|\le 4\)

For every graph \(H\) with \(2\le |V(H)|\le4\),
\[
\mathcal G_{H,n}\text{ is connected for every }n
\]
if and only if \(H\) is one of:

- a complete graph;
- an independent graph;
- \(P_4\).

Every other \(H\) on at most four vertices has \(\mathcal G_{H,n}\) disconnected for all sufficiently large \(n\).

Concrete sufficient thresholds are given below.

### Further infinite families

1. For every \(r\ge2\), both \(K_{1,r}\) and \(K_r+K_1\) have eventually disconnected flip graphs.
2. A general “two complete-multipartite perturbations” criterion gives further infinite families, including the paw and its complement.

No claim is made that the numerical thresholds below are optimal.

---

# 2. Upward persistence of disconnectedness

We first record two elementary observations.

## 2.1 Complementation

The map
\[
G\longmapsto \overline G
\]
is an isomorphism
\[
\mathcal G_{H,n}\cong \mathcal G_{\overline H,n},
\]
because complementation preserves one-edge flips and transforms induced copies of \(H\) into induced copies of \(\overline H\).

## 2.2 Safe one-vertex extensions

Let \(H\) have at least two vertices.

- If \(H\) has no isolated vertex, then adjoining an isolated vertex to any \(H\)-free graph preserves \(H\)-freeness.
- If \(H\) has an isolated vertex, then \(H\) has no universal vertex. In that case, adjoining a universal vertex preserves \(H\)-freeness.

Indeed, an induced copy of \(H\) containing the new vertex would make that vertex isolated or universal, respectively.

## Proposition 2.1

If \(\mathcal G_{H,n}\) is disconnected, then \(\mathcal G_{H,n+1}\) is disconnected.

### Proof

Choose \(H\)-free graphs \(A,B\) in different components of \(\mathcal G_{H,n}\). Extend both safely to \(H\)-free graphs \(A^+,B^+\) on \([n+1]\), using an isolated or universal vertex as above.

Suppose there were a path
\[
A^+=G_0,G_1,\dots,G_t=B^+
\]
in \(\mathcal G_{H,n+1}\). Restrict every \(G_i\) to \([n]\). Each restriction remains \(H\)-free. A flip involving \(n+1\) becomes a repeated term after restriction, while a flip inside \([n]\) remains a one-edge flip. Removing consecutive repetitions would therefore give a path in \(\mathcal G_{H,n}\) from \(A\) to \(B\), a contradiction. ∎

Iteration proves Theorem A.

---

# 3. The flip graph at \(n=|V(H)|\)

Let \(h=|V(H)|\), \(q=\binom h2\), and \(e=|E(H)|\). On exactly \(h\) vertices, the forbidden graphs are precisely the labeled copies of \(H\), all lying in edge layer \(e\) of the \(q\)-dimensional hypercube.

## Proposition 3.1

For \(h\ge3\), \(\mathcal G_{H,h}\) is disconnected if and only if \(e=1\) or \(e=q-1\).

### Proof

All graphs with fewer than \(e\) edges form a connected subgraph: delete edges to reach the empty graph. Similarly, all graphs with more than \(e\) edges form a connected subgraph by adding edges to reach the complete graph.

If there is an \(e\)-edge graph \(F\) on \(h\) vertices not isomorphic to \(H\), then \(F\) is allowed. Since \(0<e<q\), it has a deletion neighbor in the lower region and an addition neighbor in the upper region. Hence these two regions, and therefore the entire flip graph, are connected.

Thus disconnection occurs exactly when every \(e\)-edge graph on \(h\) vertices is isomorphic to \(H\). For \(h\ge3\), this happens only for
\[
e\in\{0,1,q-1,q\}.
\]
The cases \(e=0,q\) leave only one extreme layer forbidden, and the remaining hypercube is connected. Hence only \(e=1,q-1\) yield disconnection.

For completeness, when \(h\ge4\) and \(2\le e\le q-2\), there are always two nonisomorphic \(e\)-edge graphs. By complementation, assume \(e\le q/2\).

- If \(2\le e\le h-1\), compare \(K_{1,e}\) with \(2K_2\) when \(e=2\), or with \(P_{e+1}\) when \(e\ge3\).
- If \(e\ge h\), then \(e\le q/2\le\binom{h-1}{2}\). There is an \(e\)-edge graph with an isolated vertex, while starting with \(C_h\) and adding \(e-h\) edges gives an \(e\)-edge graph with no isolated vertex.

Thus the two graphs are nonisomorphic. ∎

### Corollary 3.2

For \(h\ge3\):

- if \(H=K_2+(h-2)K_1\), the empty graph on \(h\) vertices is isolated in \(\mathcal G_{H,h}\);
- if \(H=K_h-e\), the complete graph on \(h\) vertices is isolated.

In fact, these remain isolated for every \(n\ge h\).

---

# 4. The connected benchmark cases

## 4.1 Cliques and independent graphs

If \(H=K_h\), deleting edges cannot create an induced \(K_h\). Hence every \(H\)-free graph can be connected to the empty graph by successive edge deletions.

Dually, if \(H=\overline K_h\), every \(H\)-free graph can be connected to the complete graph by successive edge additions.

Thus these flip graphs are connected for every \(n\).

## 4.2 The case \(H=P_4\)

I include a self-contained proof.

We use the elementary cograph decomposition:

> If a \(P_4\)-free graph \(F\) has at least two vertices, then either \(F\) is disconnected or \(\overline F\) is disconnected.

Here is a proof. Assume \(F\) is connected and induct on \(|V(F)|\). Fix \(v\).

- If \(F-v\) is disconnected, then \(v\) must be complete to every component. Otherwise, in one component take an edge \(pq\) across a transition from a neighbor \(p\) of \(v\) to a nonneighbor \(q\), and take a neighbor \(z\) of \(v\) in another component. Then
  \[
  q-p-v-z
  \]
  is an induced \(P_4\). Hence \(v\) is universal and \(\overline F\) is disconnected.

- Suppose \(F-v\) is connected. By induction, \(\overline{F-v}\) has components \(C_1,\dots,C_t\), \(t\ge2\). Distinct \(C_i\)'s are completely joined in \(F\). If \(v\) is complete to some \(C_i\), then \(C_i\) is completely joined to its complement, so \(\overline F\) is disconnected. Otherwise \(v\) has a nonneighbor in every \(C_i\). Since \(F\) is connected, \(v\) has a neighbor in some \(C_1\). Along a path in \(\overline F[C_1]\), choose consecutive vertices \(p,q\) with \(vp\in E(F)\) and \(vq\notin E(F)\). Choose a nonneighbor \(z\) of \(v\) in \(C_2\). Then
  \[
  v-p-z-q
  \]
  is an induced \(P_4\), a contradiction.

Now induct on \(n\) to show that every \(P_4\)-free graph on \(n\) vertices is connected in the flip graph to the empty graph.

- If \(G\) is disconnected, independently transform each component to an empty graph. Disjoint unions of \(P_4\)-free graphs are \(P_4\)-free.
- If \(G\) is connected, then
  \[
  G=G_1\vee\cdots\vee G_t
  \]
  is the join of smaller \(P_4\)-free graphs. By applying the induction hypothesis to \(\overline{G_i}\) and complementing the corresponding paths, each \(G_i\) can be transformed to a clique. Thus \(G\) can be transformed to \(K_n\).

Finally, \(K_n\) can be transformed to the empty graph while remaining \(P_4\)-free: isolate one vertex at a time, deleting its incident edges in arbitrary order. At every intermediate stage, all nonisolated vertices except possibly the current vertex form a clique. Such a graph cannot contain an induced \(P_4\).

Therefore \(\mathcal G_{P_4,n}\) is connected for every \(n\).

---

# 5. Induced-saturated witnesses

An \(H\)-free graph \(S\) for which every one-edge flip creates an induced \(H\) is an isolated vertex of \(\mathcal G_{H,|S|}\). By Theorem A, one such graph proves eventual disconnectedness.

## 5.1 All induced stars

### Proposition 5.1

For every \(r\ge3\), there is a finite \(K_{1,r}\)-induced-saturated graph.

### Construction

Put
\[
k=r-1,\qquad m=k^2+k=r(r-1).
\]
Let \(X_{k,m}\) have the \(k\)-subsets of \([m]\) as vertices, with
\[
AB\in E(X_{k,m})\quad\Longleftrightarrow\quad A\cap B\ne\varnothing.
\]

Thus \(|V(X_{k,m})|=\binom{r(r-1)}{r-1}\).

### \(K_{1,r}\)-freeness

Suppose an induced \(K_{1,r}\) were centered at a \(k\)-set \(A\). Its \(r=k+1\) leaves would be pairwise nonadjacent, hence pairwise disjoint \(k\)-sets, and each would intersect \(A\). Their intersections with \(A\) would be pairwise disjoint nonempty subsets of the \(k\)-element set \(A\), which is impossible for \(k+1\) leaves.

### Adding a nonedge

Let \(A,B\) be disjoint \(k\)-sets. Write
\[
A=\{a_1,\dots,a_k\}.
\]
Choose pairwise disjoint \((k-1)\)-sets \(P_1,\dots,P_k\), all outside \(A\cup B\), and set
\[
D_i=\{a_i\}\cup P_i.
\]
There are enough ground elements because
\[
|A\cup B|+k(k-1)=2k+k(k-1)=k^2+k=m.
\]

The sets \(B,D_1,\dots,D_k\) are pairwise disjoint. After adding \(AB\), the vertex \(A\) is therefore the center of an induced \(K_{1,k+1}\) with these leaves.

### Deleting an edge

Let \(A,B\) intersect and choose \(c\in A\cap B\). Choose new elements
\[
t_1,\dots,t_{k-1}\notin A\cup B
\]
and put
\[
C=\{c,t_1,\dots,t_{k-1}\}.
\]
For each \(i\), choose a private \((k-1)\)-set \(P_i\), with all these sets mutually disjoint and outside everything chosen so far, and put
\[
D_i=\{t_i\}\cup P_i.
\]

After deleting \(AB\), the vertex \(C\) is adjacent to
\[
A,B,D_1,\dots,D_{k-1}.
\]
These \(k+1=r\) vertices are pairwise nonadjacent in the toggled graph. Hence they form the leaves of an induced \(K_{1,r}\).

Thus \(X_{k,m}\) is \(K_{1,r}\)-induced-saturated. ∎

For \(r=2\), \(K_{1,2}=P_3=K_3-e\), and the complete graph \(K_n\) is isolated for every \(n\ge3\).

By complementation, \(K_r+K_1=\overline{K_{1,r}}\) also has eventually disconnected flip graphs.

For \(r=3\), the construction is
\[
X_{2,6}=L(K_6),
\]
on \(15\) vertices.

---

## 5.2 A complete-multipartite perturbation criterion

### Proposition 5.2

Suppose \(H\) is not complete multipartite and has both of the following representations:

1. \(H=A+e\), where \(A\) is complete multipartite and \(e\) is a nonedge of \(A\);
2. \(H=B-f\), where \(B\) is complete multipartite and \(f\) is an edge of \(B\).

Then \(H\) has a finite induced-saturated graph.

### Proof

Take a complete \(R\)-partite graph \(M\) with all parts of the same size \(s\), where:

- \(R\) is at least the number of parts of both \(A\) and \(B\);
- \(s\) is at least every part size occurring in \(A\) or \(B\).

Every induced subgraph of \(M\) is complete multipartite, so \(M\) is \(H\)-free.

A nonedge of \(M\) lies inside one part. Embed \(A\) into \(M\), mapping the endpoints of \(e\) to this pair. Adding the nonedge creates an induced \(H\).

An edge of \(M\) joins two different parts. Embed \(B\) into \(M\), mapping the endpoints of \(f\) to this edge. Deleting it creates an induced \(H\).

Thus every flip creates \(H\). ∎

### Corollary 5.3

Let \(Q\) be any complete multipartite graph having a part exactly
\[
\{u,v,z\}
\]
of size \(3\), and let \(H=Q+uv\). Then \(H\) has eventually disconnected flip graphs.

Indeed, take \(A=Q\). For the second representation, split the distinguished part into \(\{u,z\}\) and \(\{v\}\), obtaining a complete multipartite graph \(B\), and delete the edge \(vz\). Then \(B-vz=H\).

The paw is the smallest nontrivial example: it is obtained from \(K_{3,1}\) by adding an edge inside the part of size \(3\).

### Explicit paw witness

Let \(H\) be the paw. Then \(K_{3,3,3}\) is \(H\)-induced-saturated.

- It is paw-free because every induced subgraph is complete multipartite, while the paw is not.
- Adding an edge \(uv\) inside a part: choose \(w\) in another part and \(z\) in the same part as \(u,v\). Then \(u,v,w\) form a triangle and \(z\) is pendant at \(w\).
- Deleting an edge \(uv\) between two parts: choose \(x\ne u\) in \(u\)'s part and \(y\) in the third part. Then \(v,x,y\) form a triangle, while \(u\) is adjacent only to \(y\) among those three.

Hence the paw is disconnected from \(n=9\) onward. Its complement \(P_3+K_1\) has the same conclusion.

---

# 6. A \(C_4\)-induced-saturated graph

The remaining nontrivial four-vertex case is \(C_4\). A convenient witness is the icosahedral graph.

Let indices lie in \(\mathbb Z_5\), and define a graph \(I\) on
\[
\{x,y\}\cup\{a_i,b_i:i\in\mathbb Z_5\}
\]
by the edges

\[
xa_i,\qquad yb_i,
\]
\[
a_i a_{i+1},\qquad b_i b_{i+1},
\]
\[
a_i b_i,\qquad a_i b_{i-1}.
\]

This is the usual 12-vertex icosahedral graph.

## 6.1 \(I\) is induced-\(C_4\)-free

An induced \(C_4\) exists exactly when some nonadjacent pair has two nonadjacent common neighbors.

The nonedge types, up to the symmetry
\[
x\leftrightarrow y,\qquad a_i\leftrightarrow b_{-i},
\]
are as follows:

\[
\begin{array}{c|c}
\text{nonedge} & \text{common neighborhood}\\ \hline
xy & \varnothing\\
xb_i & \{a_i,a_{i+1}\}\\
a_i a_{i+2} & \{x,a_{i+1}\}\\
a_i b_{i+1} & \{a_{i+1},b_i\}\\
a_i b_{i+2} & \varnothing\\
a_i b_{i+3} & \{a_{i-1},b_{i-1}\}.
\end{array}
\]

Every displayed two-vertex common neighborhood is an edge. Hence no nonedge has two nonadjacent common neighbors, so \(I\) has no induced \(C_4\).

## 6.2 Every edge deletion creates a \(C_4\)

For every edge type, the table below gives two nonadjacent common neighbors:

\[
\begin{array}{c|c}
\text{edge} & \text{two nonadjacent common neighbors}\\ \hline
xa_i & a_{i-1},a_{i+1}\\
a_i a_{i+1} & x,b_i\\
a_i b_i & a_{i+1},b_{i-1}\\
a_i b_{i-1} & a_{i-1},b_i.
\end{array}
\]

The symmetric edge types are covered by the same argument. If \(uv\) is deleted and \(p,q\) are the indicated common neighbors, then the four vertices \(u,p,v,q\) induce a \(C_4\).

## 6.3 Every nonedge addition creates a \(C_4\)

It suffices to exhibit an induced three-edge path between every nonadjacent pair:

\[
\begin{array}{c|c}
\text{nonedge} & \text{induced path}\\ \hline
xy & x-a_i-b_i-y\\
xb_i & x-a_{i+2}-b_{i+1}-b_i\\
a_i a_{i+2} & a_i-b_i-b_{i+1}-a_{i+2}\\
a_i b_{i+1} & a_i-x-a_{i+2}-b_{i+1}\\
a_i b_{i+2} & a_i-b_i-b_{i+1}-b_{i+2}\\
a_i b_{i+3} & a_i-x-a_{i-2}-b_{i-2}.
\end{array}
\]

Again the remaining cases follow from symmetry. Adding an edge between the endpoints of an induced \(P_4\) creates an induced \(C_4\).

Therefore \(I\) is \(C_4\)-induced-saturated. Consequently,
\[
\mathcal G_{C_4,n}\text{ is disconnected for every }n\ge12.
\]
By complementation, the same holds for \(2K_2\), using \(\overline I\).

---

# 7. Classification for graphs on at most four vertices

For \(n<|V(H)|\), the flip graph is the full hypercube and is connected. The preceding constructions give the following exhaustive list.

\[
\begin{array}{c|c|c}
H\text{ up to complementation} & \text{isolated }H\text{-free graph} & \text{sufficient }n_0\\ \hline
K_2+K_1 & \overline K_3 & 3\\
K_2+2K_1 & \overline K_4 & 4\\
K_{1,3} & L(K_6) & 15\\
\text{paw} & K_{3,3,3} & 9\\
C_4 & I\text{ (icosahedral graph)} & 12.
\end{array}
\]

Taking complements covers, respectively,

- \(P_3\);
- \(K_4-e\);
- \(K_3+K_1\);
- \(P_3+K_1\);
- \(2K_2\).

The only remaining four-vertex graph is \(P_4\), whose flip graph is connected for every \(n\). Together with the clique and independent-set cases, this proves Theorem C.

---

# 8. What remains open

The argument does not classify arbitrary \(H\) with at least five vertices. In particular:

1. Existence of an induced-saturated graph is only a sufficient condition for disconnection; disconnected flip graphs need not contain isolated vertices.
2. The constructions above do not address general paths, cycles, prime graphs, or arbitrary modular compositions.
3. The numerical thresholds \(9,12,15\) are only explicit upper bounds.
4. The results are consistent with the possible classification
   \[
   \mathcal G_{H,n}\text{ connected for every }n
   \quad\Longleftrightarrow\quad
   H\in\{K_h,\overline K_h,P_4\},
   \]
   but no proof of this general statement is supplied.

For \(H=K_1\), there are no \(H\)-free graphs on a nonempty vertex set, so whether the resulting empty flip graph is called connected is a matter of convention.
