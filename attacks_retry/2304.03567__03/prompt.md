Attack the following open graph-theory problem.

Catalog id: 2304.03567__03
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2304.03567__03/
Source paper: Temporalizing digraphs via linear-size balanced bi-trees (arXiv:2304.03567)

=== Catalog page (statement + literature review) ===
Constant-factor approximation for RFCPP — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 4 asks whether a polytime constant approximation algorithm exists for RFCPP (Request Forward Connected Pairs Problem), where only a specified set R of vertex pairs in a strongly connected digraph must be made forward-connected by an enumeration. The source paper (arXiv:2304.03567, STACS 2024) shows FCPP is in APX and proves (Proposition 4) that no constant c>0 can guarantee c|R| satisfied requests for worst-case instances in the undirected sense, but the question of a constant approximation ratio for directed RFCPP is posed explicitly as open. No follow-up paper resolving or substantially progressing Problem 4 was found in the indexed literature as of May 2026.

 Reviewer notes. The two internal references are identical false positives (arXiv:2206.12335, about 1-independent percolation), with no connection to the source paper or RFCPP. A topically related paper arXiv:2604.27227 ('Designing sparse temporal graphs satisfying connectivity requirements') appeared in search results but its abstract does not cite arXiv:2304.03567 and no progress on Problem 4 was found in it. No post-2024 resolution of Problem 4 was identified across all web queries.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is there a polytime constant approximation algorithm for RFCPP?

Context

RFCPP (Request Forward Connected Pairs Problem) is the variant of FCPP where only a specified set $R\subseteq\binom{V}{2}$ of pairs needs to be forward connected. Since FCPP (the case $R=\binom{V}{2}$) is in APX, the question is whether a constant-factor approximation also exists for RFCPP, and in particular whether a linear fraction of requests in $R$ can always be satisfied.

Source paper

 Temporalizing digraphs via linear-size balanced bi-trees
 Stéphane Bessy, Stéphan Thomassé, Laurent Viennot · 2024-01-11
 https://arxiv.org/abs/2304.03567

=== Source paper abstract / header ===
Abstract:In a directed graph $D$ on vertex set $v_1,\dots ,v_n$, a \emph{forward arc} is an arc $v_iv_j$ where $i<j$. A pair $v_i,v_j$ is \emph{forward connected} if there is a directed path from $v_i$ to $v_j$ consisting of forward arcs. In the {\tt Forward Connected Pairs Problem} ({\tt FCPP}), the input is a strongly connected digraph $D$, and the output is the maximum number of forward connected pairs in some vertex enumeration of $D$. We show that {\tt FCPP} is in APX, as one can efficiently enumerate the vertices of $D$ in order to achieve a quadratic number of forward connected pairs. For this, we construct a linear size balanced bi-tree $T$ (an out-tree and an in-tree with same size which roots are identified). The existence of such a $T$ was left as an open problem motivated by the study of temporal paths in temporal networks. More precisely, $T$ can be constructed in quadratic time (in the number of vertices) and has size at least $n/3$. The algorithm involves a particular depth-first search tree (Left-DFS) of independent interest, and shows that every strongly connected directed graph has a balanced separator which is a circuit. Remarkably, in the request version {\tt RFCPP} of {\tt FCPP}, where the input is a strong digraph $D$ and a set of requests $R$ consisting of pairs $\{x_i,y_i\}$, there is no constant $c>0$ such that one can always find an enumeration realizing $c.|R|$ forward connected pairs $\{x_i,y_i\}$ (in either direction).
 

 
 
 
 Comments:
 11 pages, 2 figure
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS)
 
 
 MSC classes:
 05C20, 05C85, 68R10
 

 
 ACM classes:
 F.2.2; G.2.2
 

 Cite as:
 arXiv:2304.03567 [math.CO]
 

 
  
 (or 
 arXiv:2304.03567v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2304.03567
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Stéphane Bessy [view email] 
 [v1]
 Fri, 7 Apr 2023 10:02:30 UTC (361 KB)

 [v2]
 Thu, 11 Jan 2024 09:30:34 UTC (48 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Temporalizing digraphs via linear-size balanced bi-trees, by St\'ephane Bessy and 1 other authors
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
 | 2023-04
 

 Change to browse by:
 
 cs
 cs.DM
 cs.DS
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
  "one_line": "RFCPP is APX-complete already on bidirected stars, admits a deterministic constant approximation when requested directed distances are bounded, and has an O(log |R|)-approximation on symmetric digraphs.",
  "would_publish": false,
  "caveats": "These results neither give a constant approximation nor prove constant-factor hardness for unrestricted directed RFCPP."
}
```

# Mathematical writeup

## 1. Problem and an exact reformulation

Let \(D=(V,A)\) be strongly connected and let \(R\subseteq \binom V2\). For an enumeration \(\pi\), let

\[
A_\pi=\{uv\in A:\pi(u)<\pi(v)\}.
\]

A request \(\{x,y\}\) is realized if \(A_\pi\) contains an \(x\)-to-\(y\) path or a \(y\)-to-\(x\) path.

### Lemma 1
The RFCPP optimum is

\[
\max_{H\subseteq D\text{ acyclic}}
\left|\left\{\{x,y\}\in R:
x\leadsto_H y\text{ or }y\leadsto_H x\right\}\right|.
\]

#### Proof
For every enumeration \(\pi\), \(D_\pi=(V,A_\pi)\) is acyclic, and its requested comparable pairs are exactly those realized by \(\pi\).

Conversely, if \(H\subseteq D\) is acyclic, take a topological ordering of \(H\). Every arc of \(H\) is then forward, so every request connected in one direction in \(H\) is realized. ∎

This emphasizes the source of difficulty: the objective is a reachability objective on an acyclic subgraph, rather than an additive objective on its arcs.

---

## 2. Bounded request distance gives a constant approximation

For a request \(r=\{x,y\}\), write \(d(x,y)\) for directed distance in \(D\). Since \(D\) is strong, both directed distances are finite.

### Theorem 2
There is a deterministic polynomial-time algorithm producing an enumeration realizing at least

\[
\sum_{\{x,y\}\in R}
\left(
\frac{1}{(d(x,y)+1)!}
+
\frac{1}{(d(y,x)+1)!}
\right)
\tag{1}
\]

requests.

Consequently, if

\[
L=\max_{\{x,y\}\in R}\min\{d(x,y),d(y,x)\},
\]

then RFCPP has a deterministic \((L+1)!\)-approximation on this class of instances. In particular, RFCPP is in APX whenever \(L\) is bounded by a constant.

### Proof
For every request \(r=\{x,y\}\), choose shortest directed paths

\[
P_r^+=(x=v_0,v_1,\dots,v_a=y),
\qquad
P_r^-=(y=w_0,w_1,\dots,w_b=x).
\]

In a uniformly random enumeration, the vertices of \(P_r^+\) occur in their prescribed order with probability \(1/(a+1)!\). On that event, \(P_r^+\) is a forward path. Similarly, \(P_r^-\) is forward with probability \(1/(b+1)!\).

The two events are disjoint: the first requires \(x\) before \(y\), while the second requires \(y\) before \(x\). Hence the expected number of requests realized through one of these chosen paths is exactly the quantity in (1). Thus some enumeration attains at least (1).

This can be derandomized by conditional expectation. Given a prefix of the enumeration, the conditional probability that a prescribed sequence \(z_1,\dots,z_k\) will occur in order is:

- zero if the sequence vertices already chosen are not an initial segment \(z_1,\dots,z_j\) in the correct order;
- \(1/(k-j)!\) otherwise.

At each position, test every remaining vertex as the next choice and select one maximizing the resulting conditional expectation. All chosen paths have at most \(n\) vertices, so this is polynomial time.

Finally, if every request has one direction of distance at most \(L\), then each summand in (1) is at least \(1/(L+1)!\). Hence the algorithm realizes at least

\[
\frac{|R|}{(L+1)!}\geq \frac{\operatorname{OPT}}{(L+1)!}.
\]

∎

The factorial dependence is only a restricted-case result. For example, on a directed Hamiltonian cycle all requests can be realized by cutting the cycle into a Hamiltonian path, while a fixed long witness path is monotone in only a factorially small proportion of random orders.

---

## 3. Exact equivalence with MAX-CUT on bidirected stars

The following gives a sharp complexity classification for a very restricted class.

### Theorem 3
RFCPP restricted to bidirected stars, with all requests between leaves, is exactly unweighted MAX-CUT. Consequently this restricted RFCPP is APX-complete and has no PTAS unless \(P=NP\).

### Proof
Given a simple graph \(G=(U,E)\), construct a digraph \(D\) with vertex set \(U\cup\{c\}\), where for every \(u\in U\) both arcs \(uc\) and \(cu\) are present. Thus \(D\) is a strongly connected bidirected star. Set

\[
R=\{\{u,v\}:uv\in E\}.
\]

Consider an enumeration \(\pi\). The unique simple path in the underlying star between distinct leaves \(u,v\) is \(u,c,v\). Thus \(\{u,v\}\) is forward-connected exactly when

\[
\pi(u)<\pi(c)<\pi(v)
\quad\text{or}\quad
\pi(v)<\pi(c)<\pi(u).
\]

Let

\[
S=\{u\in U:\pi(u)<\pi(c)\}.
\]

The realized requests are therefore exactly the edges of \(G\) crossing the cut \((S,U\setminus S)\).

Conversely, every cut \(S\subseteq U\) is represented by placing all vertices of \(S\) before \(c\) and all vertices of \(U\setminus S\) after \(c\). Hence

\[
\operatorname{OPT}_{\mathrm{RFCPP}}(D,R)
=
\operatorname{MAXCUT}(G).
\]

The transformations between solutions preserve objective values exactly. Since unweighted MAX-CUT is APX-hard, this restriction of RFCPP is APX-hard. It belongs to APX because a random cut, derandomized by conditional expectation, cuts at least \(|E|/2\) edges and hence is a \(2\)-approximation. ∎

Thus RFCPP is already NP-hard and APX-hard on symmetric strong digraphs of directed diameter two. This rules out a PTAS but does not rule out a constant approximation for general RFCPP.

---

## 4. An \(O(\log |R|)\)-approximation for symmetric digraphs

Call \(D\) symmetric if \(uv\in A(D)\) implies \(vu\in A(D)\). The proof actually only needs \(D\) to contain a bidirected spanning tree.

### Theorem 4
Let \(D\) contain a bidirected spanning tree, and let \(m=|R|\geq1\). There is a deterministic polynomial-time enumeration realizing at least

\[
\frac{m}{2(1+\lfloor\log_2 m\rfloor)}
\]

requests. Consequently this class has a deterministic

\[
2(1+\lfloor\log_2 m\rfloor)
\]

approximation.

### Proof

Fix a bidirected spanning tree \(T\).

#### Request-weighted centroid decomposition

For a connected subtree \(U\subseteq T\), let \(Q\) be the requests whose two endpoints are in \(U\) and which have not yet been assigned. Give each vertex \(v\in U\) weight equal to the number of endpoints of requests in \(Q\) located at \(v\). The total weight is \(2|Q|\).

Choose a weighted centroid \(c\), so that every component \(B\) of \(U-c\) has endpoint weight at most \(|Q|\). Assign to \(c\) all requests in \(Q\) whose \(T\)-path contains \(c\). Every remaining request has both endpoints in one component \(B\), and we recurse there.

If \(Q_B\) is the set passed to \(B\), then

\[
2|Q_B|
\leq \text{endpoint weight of }B
\leq |Q|,
\]

so \(|Q_B|\leq |Q|/2\). Thus the recursion has at most

\[
h=1+\lfloor\log_2 m\rfloor
\]

nonempty levels. Every request is assigned exactly once.

#### Satisfying half the requests assigned to one centroid

Fix a recursion node with subtree \(U\), centroid \(c\), and assigned request set \(Q_c\). The components of \(U-c\) will be called branches.

For each branch \(B\), choose one of two states:

- orient every edge of \(B\cup\{c\}\) toward \(c\);
- orient every such edge away from \(c\).

If a request has one endpoint equal to \(c\), its tree path is directed in one of the two directions regardless of the branch state.

Otherwise its endpoints lie in distinct branches \(B_1,B_2\). Its path is directed exactly when \(B_1\) and \(B_2\) receive opposite states. Therefore these requests define a multigraph on the branches, and choosing the branch states is precisely a cut problem. A random choice cuts half its edges in expectation, so a deterministic greedy conditional-expectation procedure satisfies at least half of \(Q_c\).

#### Combining one recursion level

At any fixed recursion depth, the corresponding subtrees \(U\) are vertex-disjoint. Hence their edge orientations can be chosen independently, satisfying at least half the requests assigned at that depth. Orient all remaining tree edges arbitrarily.

Every orientation of a tree is acyclic, so take a topological ordering of the oriented tree. Since both directed versions of every tree edge belong to \(D\), each consistently oriented request path is a forward path in \(D\).

Let \(m_i\) be the number of requests assigned at depth \(i\). Since

\[
\sum_{i=0}^{h-1}m_i=m,
\]

some depth has \(m_i\geq m/h\). The corresponding enumeration realizes at least \(m_i/2\geq m/(2h)\) requests. Since \(\operatorname{OPT}\leq m\), this is also a \(2h\)-approximation. ∎

The same argument works for nonnegative request weights, with the decomposition depth controlled by the number of positive-weight requests.

---

## 5. What remains open

The unrestricted directed problem is not resolved here.

1. The bounded-distance approximation deteriorates factorially with the maximum requested distance.
2. The symmetric-digraph algorithm has a logarithmic, not constant, approximation factor.
3. The MAX-CUT reduction proves only APX-hardness. It excludes a PTAS under \(P\neq NP\), but is fully compatible with the existence of a constant-factor approximation.
4. The bidirected-tree argument relies crucially on independently orienting tree edges and then topologically sorting. A general strong digraph need not contain a bidirected spanning tree, and replacing tree edges by directed paths can introduce incompatible overlaps and directed cycles.
5. Proposition 4 from the source, asserting that \(\operatorname{OPT}/|R|\) can tend to zero, is consistent with the \(O(\log |R|)\) symmetric guarantee and does not by itself imply hardness relative to \(\operatorname{OPT}\).

Thus the central dichotomy—constant approximation versus constant-factor inapproximability for unrestricted directed RFCPP—remains open.
