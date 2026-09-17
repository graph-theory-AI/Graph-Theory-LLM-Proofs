Attack the following open graph-theory problem.

Catalog id: 2603.17630__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2603.17630__01/
Source paper: Anticoncentration of random spanning trees in graphs with large minimum… (arXiv:2603.17630)

=== Catalog page (statement + literature review) ===
Non-isomorphic spanning trees count lower bound — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 4.2 from arXiv:2603.17630 (March 2026) asserts that Ω(n^{d-1}) is the correct lower bound for the number of non-isomorphic spanning trees in connected n-vertex graphs with minimum degree at least d, with K_{d,n-d} as the conjectured extremal example. The same paper establishes the weaker bound n^{Ω(d)} (tight only up to the constant in the exponent), which proves Lee's conjecture in strong form but falls short of the d-1 exponent claimed in Conjecture 4.2. No follow-up paper resolving or making partial progress on this specific conjecture was found in the indexed literature as of May 2026.

 Reviewer notes. The conjecture is very recent (March 2026). The source paper itself proves n^{Omega(d)} non-isomorphic spanning trees for graphs of minimum degree d, which is tight only up to the constant in the exponent; Conjecture 4.2 asks for the sharp exponent d-1, achieved by K_{d,n-d}. The predecessor paper arXiv:2601.07740 (Anticoncentration of random spanning trees in almost regular graphs) established a similar result for almost regular graphs and predates the source paper. No follow-up addressing Conjecture 4.2 was found after 5 web calls.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $d$ be sufficiently large, and let $n$ be sufficiently large relative to $d$. Suppose that $G$ is a connected graph with $n$ vertices and minimum degree at least $d$. Then, the number of non-isomorphic spanning trees of $G$ is at least $\Omega(n^{d-1})$.

Context

The anticoncentration property of Conjecture 4.1 would imply only $n^{(1/2-o_n(1))(d-1)}$ non-isomorphic spanning trees, but $K_{d,n-d}$ has $\Omega(n^{d-1})$ non-isomorphic spanning trees. The authors conjecture that this larger quantity gives an essentially optimal lower bound, with $K_{d,n-d}$ being an extremal example.

Source paper

 Anticoncentration of random spanning trees in graphs with large minimum degree
 Veronica Bitonti, Lukas Michel, Alex Scott · 2026-03-18
 https://arxiv.org/abs/2603.17630

=== Source paper abstract / header ===
Abstract:A classical result by Otter shows that the complete graph has an exponential number of non-isomorphic spanning trees. This was recently extended by Lee to every almost regular graph of sufficiently large degree.
In this paper, we consider graphs of large minimum degree. We show that every connected graph $G$ with $n$ vertices and minimum degree $d$ has at least $n^{\Omega(d)}$ non-isomorphic spanning trees. This is tight up to the constant factor in the exponent. In fact, we prove the following anticoncentration result: if $\mathcal{T}$ is a uniformly random spanning tree of $G$, then for every tree $T$, the probability that $\mathcal{T}$ is isomorphic to $T$ is at most $n^{-\Omega(d)}$. This proves a conjecture of Lee in a strong form.
 

 
 
 
 Comments:
 16 pages
 

 Subjects:
 
 Combinatorics (math.CO); Probability (math.PR)
 

 Cite as:
 arXiv:2603.17630 [math.CO]
 

 
  
 (or 
 arXiv:2603.17630v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2603.17630
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Lukas Michel [view email] 
 [v1]
 Wed, 18 Mar 2026 11:51:31 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Anticoncentration of random spanning trees in graphs with large minimum degree, by Veronica Bitonti and 2 other authors
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
 | 2026-03
 

 Change to browse by:
 
 math
 math.PR
 

 

 

 
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
  "one_line": "The sharp exponent is proved for graphs with a linear deletable common-neighborhood class, including bounded-vertex-cover and complete multipartite graphs, and for bounded-block bouquets.",
  "would_publish": false,
  "caveats": "Constants depend on d and auxiliary structural bounds; arbitrary large 2-connected graphs remain untreated."
}
```

# Mathematical writeup

Let \(s(G)\) denote the number of isomorphism classes of spanning trees of \(G\). All asymptotic constants below may depend on \(d\); thus \(\Omega_d(n^{d-1})\) is intended. The arguments do not resolve the conjecture for arbitrary graphs.

## 1. A common-neighborhood lemma

The following gives the conjectured exponent whenever linearly many vertices can independently be made leaves adjacent to the same \(d\) vertices.

### Lemma 1
Let \(G\) be a connected graph. Suppose there are disjoint sets
\[
X=\{x_1,\dots,x_d\},\qquad Y\subseteq V(G),
\]
such that

1. every \(y\in Y\) is adjacent to every \(x_i\), and
2. \(G-Y\) is connected.

Writing \(m=|Y|\), one has
\[
s(G)\ge \frac1{d!}\binom{m+d-1}{d-1}.
\]
In particular,
\[
s(G)\ge \frac{m^{d-1}}{d!(d-1)!}.
\]

### Proof
Fix a spanning tree \(S\) of \(G-Y\), and put \(b_i=\deg_S(x_i)\).

For every weak composition
\[
\mathbf a=(a_1,\dots,a_d),\qquad a_i\ge0,\qquad \sum_i a_i=m,
\]
partition \(Y\) into sets \(Y_i\) with \(|Y_i|=a_i\), and add the edge \(yx_i\) for each \(y\in Y_i\). The resulting graph \(T_{\mathbf a}\) is a spanning tree: it is obtained from \(S\) by attaching every vertex of \(Y\) as a leaf.

Let \(D_0\) be the fixed multiset consisting of the degrees in \(T_{\mathbf a}\) of all vertices outside \(X\). Thus \(D_0\) includes \(m\) copies of \(1\). The full degree multiset is
\[
D(T_{\mathbf a})
 =D_0\uplus\{b_1+a_1,\dots,b_d+a_d\}.
\]
If \(D(T_{\mathbf a})=D(T_{\mathbf a'})\), cancellation of the common multiset \(D_0\) gives
\[
\{b_1+a_1,\dots,b_d+a_d\}
 =
\{b_1+a'_1,\dots,b_d+a'_d\}.
\]
For a fixed multiset on the right, there are at most \(d!\) ways to assign its entries to the indices \(1,\dots,d\), and each such assignment determines \(\mathbf a\). Hence every degree multiset arises from at most \(d!\) compositions. There are
\(\binom{m+d-1}{d-1}\) compositions, and distinct degree multisets give non-isomorphic trees. ∎

Thus the conjecture holds whenever \(m=\Omega_d(n)\).

---

## 2. Bounded vertex cover

### Corollary 2
Let \(G\) be connected, let \(\delta(G)\ge d\), and suppose \(G\) has a vertex cover of size at most \(k\). Then, with
\[
m=\left\lceil\frac{n-k}{2^k}\right\rceil-1,
\]
one has
\[
s(G)\ge \frac1{d!}\binom{m+d-1}{d-1}.
\]
Consequently, for every fixed \(d,k\),
\[
s(G)=\Omega_{d,k}(n^{d-1}).
\]

### Proof
Let \(C\) be a vertex cover with \(|C|\le k\), and put \(I=V(G)\setminus C\). The set \(I\) is independent. Vertices of \(I\) fall into at most \(2^k\) classes according to their neighborhood in \(C\). Hence one class \(Y_0\) has size at least
\[
\left\lceil\frac{n-k}{2^k}\right\rceil.
\]
Every vertex of \(Y_0\) has at least \(d\) neighbors, all in \(C\). Choose \(X\) to be any \(d\) of these common neighbors.

Retain one vertex \(y_0\in Y_0\), and set \(Y=Y_0\setminus\{y_0\}\). Then \(G-Y\) is connected: any path using a deleted vertex \(y\in Y\) can have each passage \(c-y-c'\) rerouted as \(c-y_0-c'\), since \(y\) and \(y_0\) have the same neighborhood. Lemma 1 applies. ∎

This covers, in particular, all families whose vertex-cover number is bounded by a function of \(d\).

---

## 3. Complete multipartite graphs

### Corollary 3
For every fixed \(d\), every sufficiently large complete multipartite graph \(G\) on \(n\) vertices with minimum degree at least \(d\) satisfies
\[
s(G)=\Omega_d(n^{d-1}).
\]

### Proof
Let the largest part have size \(M\). Since
\[
\delta(G)=n-M\ge d,
\]
there are at least \(d\) vertices outside the largest part.

We find sets as in Lemma 1 with \(|Y|\ge n/2-1\), apart from an \(O(d^2)\) loss in one case.

* If \(M\ge n/2\), choose \(d\) vertices \(X\) outside the largest part. Keep one vertex \(y_0\) in the largest part and take the other \(M-1\) vertices as \(Y\). Every vertex of \(Y\) is adjacent to every vertex of \(X\), and \(y_0\) connects all vertices of \(G-Y\).

* If \(M<n/2\) and \(M\ge d\), choose \(X\) inside the largest part. Keep one vertex \(y_0\) outside that part and take all other outside vertices as \(Y\). Then
  \[
  |Y|=n-M-1>n/2-1,
  \]
  and \(G-Y\) is a star-like connected graph with center \(y_0\).

* If \(M<d\), choose any \(d\) vertices as \(X\), and let \(Q\) be the union of the multipartite classes meeting \(X\). Since at most \(d\) classes are used and each has size at most \(d-1\),
  \[
  |Q|\le d(d-1).
  \]
  Every vertex outside \(Q\) is adjacent to all of \(X\). Keep one such vertex \(y_0\) and use all the others as \(Y\). Then
  \[
  |Y|\ge n-d(d-1)-1,
  \]
  and \(G-Y=G[Q\cup\{y_0\}]\) is connected because \(y_0\) is adjacent to all of \(Q\).

Lemma 1 now gives the result. ∎

This includes complete graphs as well as all complete bipartite graphs.

---

## 4. The conjectured example \(K_{d,N}\) has exactly the claimed order

The lower bound from Lemma 1 can be paired with a short upper bound.

### Proposition 4
For fixed \(d\) and \(N\to\infty\),
\[
s(K_{d,N})=\Theta_d(N^{d-1}).
\]
More explicitly,
\[
s(K_{d,N})\ge
\frac1{d!}\binom{N+d-2}{d-1}.
\]

### Proof
For the lower bound, let \(A\) be the part of size \(d\), retain one vertex of the other part, and use the remaining \(N-1\) vertices as \(Y\) in Lemma 1.

For the upper bound, let \(T\) be any spanning tree and let \(B\) be the part of size \(N\). Since every edge has one endpoint in \(B\),
\[
\sum_{b\in B}\bigl(\deg_T(b)-1\bigr)
  =|E(T)|-|B|
  =(d+N-1)-N
  =d-1.
\]
Therefore at most \(d-1\) vertices of \(B\) have degree at least \(2\). Delete all degree-one vertices of \(B\). What remains is a bipartite tree on the \(d\) vertices of \(A\) and at most \(d-1\) vertices of \(B\). For fixed \(d\), there are only finitely many possibilities for this core.

Once the core is fixed, every deleted vertex is a leaf attached to one of the \(d\) vertices in \(A\). The possible ordered leaf-multiplicity vectors number at most
\[
\binom{N+d-1}{d-1}.
\]
Thus \(s(K_{d,N})\le C_dN^{d-1}\) for a constant \(C_d\). ∎

This confirms the claimed order for the proposed extremal family, but of course does not establish its extremality among all graphs.

---

## 5. Highly symmetric bouquets of dense blocks

A possible counterexample mechanism is to take many identical dense blocks meeting at one cutvertex. Isomorphism then forgets the order of the blocks, potentially reducing exponentially many local choices to only polynomially many multisets. The following shows that this natural mechanism still gives exponent at least \(d-1\).

For a tree \(T\) rooted at \(r\), define its branch profile
\[
\beta(T,r)
\]
to be the vector indexed by rooted-tree isomorphism types which counts the components of \(T-r\), each rooted at its unique neighbor of \(r\).

### Lemma 5
Let \(H\) be a 2-connected graph rooted at \(r\), and suppose
\[
\deg_H(v)\ge d\qquad\text{for every }v\ne r.
\]
Then \(H\) has spanning trees \(T_1,\dots,T_d\) such that
\[
\beta(T_1,r),\dots,\beta(T_d,r)
\]
are affinely independent.

### Proof
Put \(J=H-r\), which is connected.

First, there is a vertex \(v\in N_H(r)\) which is not a cutvertex of \(J\). Indeed, if \(J\) has no cutvertex, any neighbor works. Otherwise choose an end block \(B\) of \(J\), with its unique cutvertex \(c\). Since \(H-c\) is connected, some vertex of \(B\setminus\{c\}\) must be adjacent to \(r\); such a vertex is not a cutvertex of \(J\).

Now
\[
\deg_J(v)=\deg_H(v)-1\ge d-1,
\]
and \(J-v\) is connected. A standard spanning-tree exchange argument shows that, for every
\[
i=1,\dots,d-1,
\]
there is a spanning tree \(S_i\) of \(J\) with \(\deg_{S_i}(v)=i\):

* degree \(1\) is obtained from a spanning tree of \(J-v\) plus one edge incident with \(v\);
* degree \(\deg_J(v)\) is obtained by extending the star of all edges incident with \(v\) to a spanning tree;
* the basis-exchange graph of spanning trees is connected, and a single exchange changes the degree of \(v\) by at most one.

Set
\[
T_i=S_i+rv,\qquad 1\le i\le d-1.
\]
Here \(r\) is a leaf, so \(\beta(T_i,r)\) is a unit vector corresponding to the rooted tree \((S_i,v)\). These \(d-1\) rooted types are distinct because their root degrees are \(1,\dots,d-1\).

Finally, extend any two edges incident with \(r\) to a spanning tree \(T_d\) of \(H\). Then \(T_d-r\) has at least two components. If \(h=|V(H)|-1\), every branch of \(T_d-r\) has fewer than \(h\) vertices, whereas each branch in \(T_i-r\), \(i<d\), has exactly \(h\) vertices. Thus \(\beta(T_d,r)\) has no support on any of the \(d-1\) coordinates used by the first profiles.

It follows immediately that the \(d\) profile vectors are affinely independent. ∎

### Theorem 6
Let \(G_m\) be obtained from \(m\) rooted copies of a fixed 2-connected graph \((H,r)\) by identifying all copies of \(r\), with no other intersections. Suppose every non-root vertex of \(H\) has degree at least \(d\). If
\[
m>|V(H)|-1,
\]
then
\[
s(G_m)\ge \binom{m+d-1}{d-1}.
\]
Since \(|V(G_m)|=1+m(|V(H)|-1)\), this is
\[
s(G_m)=\Omega_{d,H}(|V(G_m)|^{d-1}).
\]

### Proof
Use the \(d\) local spanning trees from Lemma 5. For each weak composition
\[
(c_1,\dots,c_d),\qquad \sum_i c_i=m,
\]
choose local tree \(T_i\) in exactly \(c_i\) of the petals. Their union is a spanning tree of \(G_m\), and its branch profile at the common root is
\[
\sum_{i=1}^d c_i\beta(T_i,r).
\]
Affine independence shows that different compositions give different profiles.

Every constructed tree has degree at least \(m\) at the common root, while every other vertex has degree at most \(|V(H)|-1\). Thus the common root is the unique maximum-degree vertex and is preserved by every unrooted tree isomorphism. Consequently distinct profiles give non-isomorphic unrooted trees. ∎

### Corollary 7
Fix \(d\) and \(B\). Suppose \(G\) is a block bouquet: every block contains the same cutvertex \(r\), distinct blocks meet only at \(r\), every block has at most \(B\) vertices, and \(\delta(G)\ge d\ge2\). Then
\[
s(G)=\Omega_{d,B}(n^{d-1}).
\]

### Proof
There are only finitely many rooted isomorphism types of blocks on at most \(B\) vertices. If \(G\) has \(M\) blocks, one rooted block type therefore occurs \(\Omega_B(M)\) times. Moreover,
\[
n-1=\sum_{\text{blocks }Q}(|V(Q)|-1)\le M(B-1),
\]
so this type occurs \(\Omega_B(n)\) times.

No block is a bridge: in a bouquet, the non-root endpoint of such a bridge would have degree one. Thus the repeated blocks are 2-connected, and Lemma 5 applies. Fix spanning trees in all other blocks and vary the repeated blocks as in Theorem 6.

For \(M>B-1\), the common cutvertex has degree at least \(M\) in every constructed tree, while every other vertex has degree at most \(B-1\), so it is again uniquely identifiable. ∎

This rules out generalized windmills with bounded petals as counterexamples.

---

## 6. Remaining gap

The argument does not handle a general minimum-degree-\(d\) graph. In particular, a graph may simultaneously have

* no linear set \(Y\) with \(d\) common neighbors and connected complement,
* vertex-cover number linear in \(n\),
* no cutvertex or repeated bounded blocks, and
* one large 2-connected block.

Lemma 5 supplies \(d\) affinely independent local spanning-tree states in a fixed block, but by itself gives only \(d\) trees, not \(n^{d-1}\) trees. A full proof would need to obtain \(d-1\) parameters each ranging over order \(n\), or an alternative source of at least \(n^{d-1}\) abstract tree shapes, inside an arbitrary large 2-connected graph.

Thus the conjecture remains unresolved, but its sharp exponent is verified for several structural classes containing both the proposed extremal example and the most obvious highly symmetric cutvertex constructions.
