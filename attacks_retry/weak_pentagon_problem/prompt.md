Attack the following open graph-theory problem.

Catalog id: weak_pentagon_problem
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/weak_pentagon_problem/
Original entry: http://www.openproblemgarden.org/op/weak_pentagon_problem
Problem attributed to: Samal, Robert (posted 2007-07-13)

=== Problem statement (OpenProblemGarden) ===
Title: Weak pentagon problem
Conjecture If $ G $ is a cubic graph not containing a triangle, then it is possible to color the edges of $ G $ by five colors, so that the complement of every color class is a bipartite graph.

=== Discussion / context (OpenProblemGarden) ===
This conjecture has several reformulations: the conclusion of the conjecture can be replaced by either of the following: \item $ G $ has a homomorphism to the Clebsch graph . \item there is a cut-continuous mapping from $ G $ to $ C_5 $ . For the latter variant, few definitions are in place. A cut-continuous mapping from a graph~ $ G $ to a graph~ $ H $ is a mapping $ f : E(G) \to E(H) $ such that the preimage of every cut in~ $ H $ is a cut in~ $ G $ . Here, by a cut in~ $ H $ we mean the edge-set of a spanning bipartite subgraph of~ $ H $ ---less succinctly, it is the set of all edges leaving some subset of vertices of~ $ H $ . Cut-continuous mappings are closely related with graph homomorphisms (see [DNR], [S]). In particular, every homomorphism from~ $ G $ to~ $ H $ naturally induces a cut-continuous mapping from~ $ G $ to~ $ H $ ; thus, the presented conjecture can be thought of as a weaker version of Nesetril's Pentagon problem . We mention a generalization of the conjecture, that deals with longer cycles/larger number of colors. The $ n $ -dimensional projective cube , denoted $ PQ_n $ , is the simple graph obtained from the $ (n+1) $ -dimensional cube~ $ Q_{n+1} $ by identifying pairs of antipodal vertices (vertices that differ in all coordinates). Note that $ PQ_4 $ is the Clebsch graph . Question What is the largest integer $ k $ with the property that all cubic graphs of sufficiently high girth have a homomorphism to $ PQ_{2k} $ ? Again, the question has several reformulations due to the following simple proposition. Proposition For every graph $ G $ and nonnegative integer $ k $ , the following properties are equivalent. \item There exists a coloring of~ $ E(G) $ by $ 2k+1 $ colors so that the complement of every color class is a bipartite graph. \item $ G $ has a homomorphism to $ PQ_{2k} $ \item $ G $ has a cut-continuous mapping to~ $ C_{2k+1} $ There are high-girth cubic graphs with the largest cut of size less then $ 0.94\cdot |E| $ . Such graphs do not admit a homomorphism to $ PQ_{2k} $ for any $ k \ge 8 $ , so there is indeed some largest integer~ $ k $ in the above question. To bound this largest~ $ k $ from below, recall that every cubic graph maps homomorphically to $ K_4 = PQ_2 $ . Moreover, it is known [DS] that cubic graphs of girth at least 17 admit a homomorphism to $ PQ_4 $ (the Clebsch graph). This shows $ k\ge 2 $ (and also provides a support for the main conjecture).

=== References listed by OpenProblemGarden ===
- [DNR] Matt DeVos, Jaroslav Nesetril and Andre Raspaud: On edge-maps whose inverse preserves flows and tensions, \MRref{MR2279171}
- *[DS] Matt Devos, Robert Samal: \arXiv[High Girth Cubic Graphs Map to the Clebsch Graph}{math.CO/0602580}
- [S] Robert Samal, On XY mappings, PhD thesis, Charles University 2006, tech. report

=== Catalog page (statement + literature review) ===
Weak pentagon problem — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The weak pentagon conjecture — equivalently, that every triangle-free cubic graph admits a homomorphism to the Clebsch graph $PQ_4$ — remains open in full generality. The strongest verified positive evidence is still structural/special-class progress: DeVos–Šámal proved the high-girth case before the OPG posting, Naserasr proved the triangle-free planar case before the posting and later showed the Clebsch graph is the smallest triangle-free planar bound, and Naserasr–Nigussie–Škrekovski extended the Clebsch-homomorphism result to all triangle-free graphs with no $K_5$ minor.

 Cited literature (2)

 
 
 
partial Homomorphisms of triangle-free graphs without a K5-minor
 (2009)
 

 
 Reza Naserasr, Yared Nigussie, Riste Škrekovski · Discrete Mathematics · doi:10.1016/j.disc.2009.04.032

Extends the Clebsch-graph homomorphism result from triangle-free planar graphs to all triangle-free graphs with no $K_5$ minor, giving a post-posting special class that includes cubic examples.
 

 
 
partial Mapping planar graphs into projective cubes
 (2013)
 

 
 Reza Naserasr · Journal of Graph Theory · doi:10.1002/jgt.21708

Shows that the Clebsch graph is the smallest triangle-free graph bounding all triangle-free planar graphs, strengthening the planar special case relevant to the weak pentagon conjecture.
 

 

 Reviewer notes. The core high-girth theorem of DeVos–Šámal (arXiv:math/0602580; author PDFs also verified) predates the 2007-07-13 OPG posting and is already cited in the OPG statement, so it is not listed in since_posted. Naserasr's 'Homomorphisms and edge-colourings of planar graphs' (JCTB 97(3), 2007; DOI 10.1016/j.jctb.2006.07.001) also predates the posting and proves the triangle-free planar case via the Clebsch graph. The post-posting 2009 Discrete Mathematics paper verifies a broader minor-closed special class, and the 2013 Journal of Graph Theory paper verifies optimality of the planar Clebsch bound; neither resolves arbitrary triangle-free cubic graphs. Targeted searches for a proof or counterexample to Šámal's full cubic triangle-free conjecture found no resolution.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. If $ G $ is a cubic graph not containing a triangle, then it is possible to color the edges of $ G $ by five colors, so that the complement of every color class is a bipartite graph.

Keywords:
Clebsch graph · cut-continuous mapping · edge-coloring · homomorphism · pentagon

Discussion

This conjecture has several reformulations: the conclusion of the conjecture can be replaced by either of the following: \item $ G $ has a homomorphism to the Clebsch graph . \item there is a cut-continuous mapping from $ G $ to $ C_5 $ . For the latter variant, few definitions are in place. A cut-continuous mapping from a graph~ $ G $ to a graph~ $ H $ is a mapping $ f : E(G) \to E(H) $ such that the preimage of every cut in~ $ H $ is a cut in~ $ G $ . Here, by a cut in~ $ H $ we mean the edge-set of a spanning bipartite subgraph of~ $ H $ ---less succinctly, it is the set of all edges leaving some subset of vertices of~ $ H $ . Cut-continuous mappings are closely related with graph homomorphisms (see [DNR], [S]). In particular, every homomorphism from~ $ G $ to~ $ H $ naturally induces a cut-continuous mapping from~ $ G $ to~ $ H $ ; thus, the presented conjecture can be thought of as a weaker version of Nesetril's Pentagon problem . We mention a generalization of the conjecture, that deals with longer cycles/larger number of colors. The $ n $ -dimensional projective cube , denoted $ PQ_n $ , is the simple graph obtained from the $ (n+1) $ -dimensional cube~ $ Q_{n+1} $ by identifying pairs of antipodal vertices (vertices that differ in all coordinates). Note that $ PQ_4 $ is the Clebsch graph . Question What is the largest integer $ k $ with the property that all cubic graphs of sufficiently high girth have a homomorphism to $ PQ_{2k} $ ? Again, the question has several reformulations due to the following simple proposition. Proposition For every graph $ G $ and nonnegative integer $ k $ , the following properties are equivalent. \item There exists a coloring of~ $ E(G) $ by $ 2k+1 $ colors so that the complement of every color class is a bipartite graph. \item $ G $ has a homomorphism to $ PQ_{2k} $ \item $ G $ has a cut-continuous mapping to~ $ C_{2k+1} $ There are high-girth cubic graphs with the largest cut of size less then $ 0.94\cdot |E| $ . Such graphs do not admit a homomorphism to $ PQ_{2k} $ for any $ k \ge 8 $ , so there is indeed some largest integer~ $ k $ in the above question. To bound this largest~ $ k $ from below, recall that every cubic graph maps homomorphically to $ K_4 = PQ_2 $ . Moreover, it is known [DS] that cubic graphs of girth at least 17 admit a homomorphism to $ PQ_4 $ (the Clebsch graph). This shows $ k\ge 2 $ (and also provides a support for the main conjecture).

Bibliography

 [DNR]
 Matt DeVos, Jaroslav Nesetril and Andre Raspaud: On edge-maps whose inverse preserves flows and tensions, \MRref{MR2279171}

★ [DS]
 Matt Devos, Robert Samal: \arXiv[High Girth Cubic Graphs Map to the Clebsch Graph}{math.CO/0602580}

 [S]
 Robert Samal, On XY mappings, PhD thesis, Charles University 2006, tech. report
 tech. report

Related conjectures

 
 related to
 Pentagon problem
 open
 Conclusion-wise the Pentagon problem is stronger: a homomorphism G -> C5 induces a cut-continuous mapping G -> C5, which is exactly the Weak pentagon conclusion (equivalently, edge 5-coloring with bipartite color-class complements / homomorphism to the Clebsch graph); the OPG text calls the weak conjecture 'a weaker version' for this reason. But the hypothesis classes are not nested in the required direction: Pentagon assumes girth at least g for sufficiently large g, while Weak pentagon covers ALL triangle-free (girth >= 4) cubic graphs. A positive Pentagon answer would establish the weak conclusion only for high-girth graphs, leaving girths 4..g-1 unsettled, so the full statements do not stand in an implication; the connection is instance-wise on a subfamily. Hence related_only (Pentagon truth would settle the high-girth part and be strong evidence).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured conclusion for triangle-free cubic graphs that become bipartite after deleting at most three edges.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved, and novelty of this special case has not been checked."
}
```

## A proved special case

For a graph \(G\), define its **edge-bipartization number**
\[
\beta(G)=\min\{|D|:D\subseteq E(G),\ G-D\text{ is bipartite}\}.
\]

I establish the following partial result, using an explicit construction.

**Theorem.** Let \(G\) be a finite simple triangle-free cubic graph. If
\[
\beta(G)\le 3,
\]
then \(G\) admits a homomorphism to the Clebsch graph. Consequently, its edges can be colored with five colors so that the complement of every color class is bipartite.

The construction also gives an additional sufficient condition with no bound on \(\beta(G)\), stated below. It does not settle the full conjecture.

## 1. A useful model of the Clebsch graph

Work in \(\mathbb F_2^5\). Let \(\mathbf 1=(1,1,1,1,1)\), and put
\[
s_i=\mathbf 1+e_i\qquad(1\le i\le5).
\]
Thus \(s_i\) has a zero in coordinate \(i\) and ones elsewhere. In particular,
\[
s_1+s_2+s_3+s_4+s_5=0.
\]

Let \(\mathcal C\) have as vertices the sixteen even-weight vectors, with
\[
x\sim y\quad\Longleftrightarrow\quad x+y\in\{s_1,\ldots,s_5\}.
\]
This is \(PQ_4\), the Clebsch graph: each antipodal pair in \(Q_5\) has a unique even-weight representative, and flipping coordinate \(i\), followed by taking that representative, adds \(s_i\).

Here is also a direct verification of the required edge-coloring consequence. Given a homomorphism \(f:G\to\mathcal C\), color \(uv\) with the unique \(i\) satisfying
\[
f(u)+f(v)=s_i.
\]
For any fixed \(j\), every edge not colored \(j\) has endpoints whose \(j\)-th coordinates differ. Hence
\[
v\longmapsto f(v)_j
\]
is a bipartition of the complement of color class \(j\).

It therefore suffices to construct \(f\).

## 2. Maximum-cut structure with at most three defects

The number \(\beta(G)\) is also the minimum possible number of edges lying within the parts of a vertex bipartition. Indeed, deleting those edges makes the graph bipartite; conversely, a bipartition of \(G-D\) leaves at most \(|D|\) edges within its parts.

Choose a maximum cut with parts \(A,B\), and write
\[
M=E(G[A])\cup E(G[B]).
\]
Then \(|M|=\beta(G)\).

Because \(G\) is cubic, \(M\) is a matching. Otherwise, a vertex incident with at least two edges of \(M\) could be moved to the other part, increasing the cut.

Put
\[
a=|E(G[A])|,\qquad b=|E(G[B])|.
\]
Counting degrees on the two sides gives
\[
3|A|=2a+|\delta(A)|,\qquad
3|B|=2b+|\delta(A)|,
\]
and therefore
\[
3(|A|-|B|)=2(a-b).
\tag{1}
\]
In particular, \(a-b\) is divisible by three. Thus:

- \(\beta(G)=1\) is impossible;
- if \(\beta(G)=2\), then \(a=b=1\);
- if \(\beta(G)=3\), all three edges of \(M\) lie in the same part.

The case \(\beta(G)=0\) is immediate, since a bipartite graph maps to any edge of \(\mathcal C\). We handle the other two possibilities separately.

## 3. Two defects: an explicit eight-vertex construction

Suppose
\[
M=\{aa',bb'\},\qquad a,a'\in A,\quad b,b'\in B.
\]
Let
\[
D=G-M,
\]
which is bipartite with parts \(A,B\).

Triangle-freeness implies that the edges between \(\{a,a'\}\) and \(\{b,b'\}\) form a matching. After interchanging \(b,b'\) if necessary, we may therefore assume
\[
ab',\ a'b\notin E(G).
\]

Set
\[
L=\{a,b\},\qquad R=\{a',b'\}.
\]
Then
\[
\operatorname{dist}_D(L,R)\ge3.
\tag{2}
\]
To see this, \(a,a'\) lie in the same bipartition class, and a length-two \(a\)-\(a'\) path would form a triangle with \(aa'\). Thus their distance in \(D\) is at least four, or infinite. The same holds for \(b,b'\). The other two pairs are in opposite classes and are nonadjacent, so their distances are at least three.

Define
\[
h(v)=\min\{3,\operatorname{dist}_D(v,L)\},
\]
taking \(h(v)=3\) in components not meeting \(L\). Every edge \(uv\in E(D)\) satisfies
\[
|h(u)-h(v)|\le1.
\]
Moreover, \(h=0\) on \(L\) and \(h=3\) on \(R\).

Let \(p(v)=0\) on \(A\) and \(p(v)=1\) on \(B\), and put
\[
q(v)=p(v)+h(v)\pmod2.
\]
Define
\[
f(v)=q(v)s_4+\sum_{i=1}^{h(v)}s_i,
\tag{3}
\]
where an empty sum is zero.

We check every type of edge.

- If \(uv\in E(D)\) and \(h(u)=h(v)\), then \(p(u)\ne p(v)\), so
  \[
  f(u)+f(v)=s_4.
  \]

- If \(uv\in E(D)\) and the heights differ by one, then \(q(u)=q(v)\). Consequently,
  \[
  f(u)+f(v)=s_j
  \]
  for the appropriate \(j\in\{1,2,3\}\).

- Each edge of \(M\) joins a height-zero vertex to a height-three vertex in the same part. Its endpoint labels consequently differ by
  \[
  s_4+s_1+s_2+s_3=s_5.
  \]

Thus (3) is a homomorphism to \(\mathcal C\).

In fact, the eight possible labels in (3) support two four-vertex paths, their rungs, and the two crossed end-edges: the usual eight-vertex Wagner graph. So this case admits a smaller target than the full Clebsch graph.

## 4. Three defects: a small auxiliary coloring problem

Now suppose \(\beta(G)=3\). By (1), after exchanging the parts, we have
\[
G[B]\text{ edgeless},\qquad E(G[A])=M,
\]
where \(M\) is a three-edge matching.

For each endpoint \(u\) of \(M\), let
\[
N_u=N_G(u)\cap B.
\]
Each \(N_u\) has exactly two vertices. If \(uv\in M\), triangle-freeness gives
\[
N_u\cap N_v=\varnothing.
\]

Construct a simple auxiliary graph \(F\) on vertex set \(B\). For every \(uv\in M\), add all four edges between \(N_u\) and \(N_v\). Thus
\[
|E(F)|\le 12.
\]

The graph \(F\) is 4-degenerate. Indeed, a subgraph of minimum degree at least five would have at least six vertices and therefore at least fifteen edges. Hence \(F\) has a proper coloring
\[
c:B\longrightarrow[5].
\]

For \(uv\in M\), the two sets
\[
c(N_u),\qquad c(N_v)
\]
are disjoint, and each has size at most two. Choose disjoint two-element sets
\[
P_u,P_v\subseteq[5]
\]
such that
\[
c(N_u)\subseteq P_u,\qquad c(N_v)\subseteq P_v.
\tag{4}
\]
There are enough colors to do this: enlarging the two sets requires a total of four distinct colors, from a palette of five. Make these choices independently for the three edges of \(M\).

Identify subsets of \([5]\) with their characteristic vectors, and define
\[
f(x)=
\begin{cases}
s_{c(x)},&x\in B,\\[2mm]
0,&x\in A\setminus V(M),\\[2mm]
\mathbf 1_{P_x},&x\in V(M).
\end{cases}
\tag{5}
\]
All these vectors have even weight.

Again, every edge can be checked explicitly.

- If \(xy\) joins \(x\in A\setminus V(M)\) to \(y\in B\), its labels differ by \(s_{c(y)}\).

- Suppose \(x\in V(M)\), \(y\in B\), and \(xy\in E(G)\). By (4), write
  \[
  P_x=\{c(y),k\}.
  \]
  Then
  \[
  f(x)+f(y)
  =(e_{c(y)}+e_k)+(\mathbf1+e_{c(y)})
  =s_k.
  \]

- If \(uv\in M\), the sets \(P_u,P_v\) are disjoint and have size two. Their characteristic vectors differ in exactly four coordinates, so their difference is some \(s_i\).

There are no other edges. Therefore (5) is a homomorphism \(G\to\mathcal C\), completing the theorem. \(\square\)

## 5. A further sufficient condition

The auxiliary construction has a useful extension beyond bounded edge-bipartization.

**Corollary.** Suppose a triangle-free cubic graph \(G\) has a partition \(A,B\) such that:

1. \(B\) is independent;
2. \(G[A]\) consists of a matching \(M\) and isolated vertices;
3. every vertex of \(B\) has at most two neighbors in \(V(M)\).

Then \(G\) admits the conjectured five-coloring.

**Proof.** Form the same auxiliary graph \(F\). Each neighbor \(u\in V(M)\) of a vertex \(x\in B\) contributes at most two neighbors of \(x\) in \(F\), namely the two \(B\)-neighbors of the partner of \(u\) in \(M\). Thus
\[
\Delta(F)\le4.
\]
Greedy coloring gives a proper five-coloring of \(F\), and construction (4)–(5) applies unchanged. \(\square\)

More generally, the construction works whenever this explicitly defined auxiliary graph is five-colorable; no assertion that this always happens is needed for either proved result.

## 6. Algorithmic content and the remaining gap

The theorem is constructive. Given the relevant maximum cut, both homomorphism constructions take linear time.

One can also recognize and handle the case \(\beta(G)\le3\) without an unrestricted maximum-cut algorithm:

1. Enumerate \(D\subseteq E(G)\) in increasing size, up to size three.
2. Test the parity constraints
   \[
   p(u)+p(v)=
   \begin{cases}
   0,&uv\in D,\\
   1,&uv\notin D,
   \end{cases}
   \qquad\text{over }\mathbb F_2.
   \]
3. The first feasible \(D\) is a minimum cut-complement. Apply the appropriate construction above.

Each parity test is a graph traversal, giving total time
\[
O\!\left(m^3(n+m)\right).
\]
This is an algorithm specification, not a claim of computational experiments.

For arbitrary graphs with \(\beta(G)\ge4\), the argument gives no general conclusion. Already at \(\beta(G)=4\), equation (1) permits—and forces—a maximum-cut complement with two edges in each part. The one-sided auxiliary construction no longer applies, and the height construction above only handles one defect edge in each part.

Thus any counterexample to the original conjecture must have edge-bipartization number at least four, but its existence or nonexistence remains unresolved here. No novelty claim or improvement to the high-girth projective-cube question is asserted.
