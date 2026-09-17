Attack the following open graph-theory problem.

Catalog id: 2502.05289__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2502.05289__00/
Source paper: Induced Disjoint Paths Without an Induced Minor (arXiv:2502.05289)

=== Catalog page (statement + literature review) ===
Subcubic H-ISC planarity dichotomy — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.5 from arXiv:2502.05289 proposes that for any subcubic graph $H$, the $H$-ISC problem (detecting $H$ as an induced subdivision) is in $\mathsf{P}$ if and only if $H$ is planar. The source paper provides the key hardness evidence: it exhibits a specific non-planar subcubic graph $H$ for which $H$-ISC is NP-complete (Theorem 3, also appearing as LIPIcs.ICALP.2025.4). No follow-up paper resolving or substantially advancing the full conjecture was found in the literature indexed as of May 2026.

 Reviewer notes. The conjecture is supported by the paper's own main result (NP-completeness for a specific non-planar subcubic H) and known polynomial algorithms for planar cases (net, K_4). The ICALP 2025 published version (LIPIcs vol. 334) numbers this as Conjecture 5.1 rather than 1.5. No follow-up resolving the full if-and-only-if characterization was found across three targeted searches.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any subcubic graph $H$, $H$-\textsc{ISC} is in $\mathsf{P}$ if and only if $H$ is planar.

Context

The conjecture is proposed by the paper's authors as a natural open question following their proof that a specific non-planar subcubic graph yields NP-complete induced subdivision containment. It complements known polynomial-time algorithms for planar induced subdivision detection (e.g., for the net and $K_{4}$) and the new hardness results of the paper.

Notes. The 'only if' direction (NP-hardness for non-planar subcubic $H$) implicitly assumes $\mathsf{P}\neq\mathsf{NP}$.

Source paper

 Induced Disjoint Paths Without an Induced Minor
 Pierre Aboulker, Édouard Bonnet, Timothé Picavet, Nicolas Trotignon · 2025-02-07
 https://arxiv.org/abs/2502.05289

=== Source paper abstract / header ===
Abstract:We exhibit a new obstacle to the nascent algorithmic theory for classes excluding an induced minor. We indeed show that on the class of string graphs -- which avoids the 1-subdivision of, say, $K_5$ as an induced minor -- Induced 2-Disjoint Paths is NP-complete. So, while $k$-Disjoint Paths, for a fixed $k$, is polynomial-time solvable in general graphs, the absence of a graph as an induced minor does not make its induced variant tractable, even for $k=2$. This answers a question of Korhonen and Lokshtanov [SODA '24], and complements a polynomial-time algorithm for Induced $k$-Disjoint Paths in classes of bounded genus by Kobayashi and Kawarabayashi [SODA '09]. In addition to being string graphs, our produced hard instances are subgraphs of a constant power of bounded-degree planar graphs, hence have bounded twin-width and bounded maximum degree.
We also leverage our new result to show that there is a fixed subcubic graph $H$ such that deciding if an input graph contains $H$ as an induced subdivision is NP-complete. Until now, all the graphs $H$ for which such a statement was known had a vertex of degree at least 4. This answers a question by Chudnovsky, Seymour, and the fourth author [JCTB '13], and by Le [JGT '19]. Finally we resolve another question of Korhonen and Lokshtanov by exhibiting a subcubic graph $H$ without two adjacent degree-3 vertices and such that deciding if an input $n$-vertex graph contains $H$ as an induced minor is NP-complete, and unless the Exponential-Time Hypothesis fails, requires time $2^{\Omega(\sqrt n)}$. This complements an algorithm running in subexponential time $2^{O(n^{2/3} \log n)}$ by these authors [SODA '24] under the same technical condition.
 

 
 
 
 Comments:
 14 pages, 5 figures
 

 Subjects:
 
 Computational Complexity (cs.CC); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 68Q25
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2502.05289 [cs.CC]
 

 
  
 (or 
 arXiv:2502.05289v1 [cs.CC] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2502.05289
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Fri, 7 Feb 2025 19:45:26 UTC (108 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced Disjoint Paths Without an Induced Minor, by Pierre Aboulker and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.CC

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2025-02
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 

 

 

 
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
  "one_line": "The full dichotomy remains unresolved, but polynomial algorithms are given for all connected targets with at most one degree-3 vertex and for three of the five possible two-degree-3 branch topologies.",
  "would_publish": false,
  "caveats": "The two private-cycle topologies and the minimal nonplanar case K_{3,3} remain untreated; strict nonmembership in P is conditional on P != NP."
}
```

## 1. Statement and conventions

For a fixed finite simple graph \(H\), the \(H\)-ISC problem asks whether an input graph \(G\) has an induced subgraph isomorphic to a subdivision of \(H\). Subdivision is understood in the standard sense: every edge is replaced by a path of positive length, so \(H\) itself is a subdivision of \(H\).

I do not resolve the full conjecture. I prove the planar direction for a reasonably broad elementary class and isolate \(K_{3,3}\) subdivisions as the precise nonplanar frontier with the minimum possible number of degree-\(3\) vertices.

Call a degree-\(3\) vertex of \(H\) a branch vertex.

## 2. Partial algorithmic theorem

Let \(\mathcal B\) be the class consisting of paths, isolated vertices, and subdivisions of \(K_{1,3}\). Let \(\mathcal J\) consist of the following connected subcubic graphs:

1. a cycle;
2. a cycle with one pendant path attached at one cycle vertex;
3. a tree with exactly two branch vertices;
4. a theta graph, meaning three internally vertex-disjoint paths with common distinct ends;
5. a cycle with one pendant path attached at each of two distinct cycle vertices.

### Theorem 2.1

If \(H\) is the disjoint union of any number of graphs from \(\mathcal B\) and at most one graph from \(\mathcal J\), then \(H\)-ISC is polynomial-time solvable.

In particular:

- every connected subcubic \(H\) with at most one branch vertex satisfies the polynomial side of the conjecture;
- every subcubic tree with at most two branch vertices does so;
- among connected graphs with exactly two branch vertices, theta graphs and cycles with a pendant path at each branch vertex are also covered.

All exponents below depend on the fixed target \(H\).

---

## 3. Truncatable components

### Lemma 3.1

If \(H\) is a path or a subdivision of \(K_{1,3}\), then \(G\) contains an induced subdivision of \(H\) if and only if \(G\) contains \(H\) as an induced subgraph.

#### Proof

For a path of length \(a\), an induced subdivision is an induced path of length at least \(a\). Taking any \(a\) consecutive edges gives an induced copy of \(H\).

Now let \(H\) be a subdivision of \(K_{1,3}\), with arm lengths \(a_1,a_2,a_3\). In any subdivision of \(H\), the three corresponding arms have lengths at least \(a_1,a_2,a_3\), after a suitable permutation. Retaining the first \(a_i\) edges on each arm produces an induced copy of \(H\). The converse is immediate. ∎

Thus a disjoint union \(B\) of such components can be detected by enumerating injective maps \(V(B)\to V(G)\) and checking all adjacencies and nonadjacencies, in time \(n^{O(|V(B)|)}\).

---

## 4. A rooted long-cycle algorithm

An induced cycle below may have length \(3\).

### Lemma 4.1

For every fixed \(q\geq 3\), there is a polynomial algorithm that, given \(G\) and \(r\in V(G)\), decides whether \(G\) contains an induced cycle of length at least \(q\) through \(r\).

#### Algorithm

Enumerate every ordered induced path

\[
P=(p_0=r,p_1,\ldots,p_{q-2}).
\]

Put \(s=p_0\), \(t=p_{q-2}\), and

\[
M=V(P)\setminus\{s,t\}.
\]

Let \(D\) be the induced graph on

\[
\{s,t\}\cup
\{z\in V(G)\setminus V(P):N_G(z)\cap M=\varnothing\}.
\]

Delete the edge \(st\) from \(D\), if present, and test by breadth-first search whether \(s\) and \(t\) remain connected.

#### Correctness

If a path \(R\) exists, choose a shortest \(s\)-\(t\) path in \(D-st\). It is induced. Its internal vertices have no neighbor in \(M\), and shortestness excludes chords from \(s\) or \(t\) to nonconsecutive vertices of \(R\). Consequently \(P\cup R\) is an induced cycle. Since \(st\) was deleted during the search, \(R\) has at least two edges, so the cycle has length at least

\[
(q-2)+2=q.
\]

Conversely, suppose \(C\) is an induced cycle of length at least \(q\) through \(r\). Take \(P\) to be \(q-2\) consecutive edges of \(C\) starting at \(r\). The complementary \(s\)-\(t\) path of \(C\) has at least two edges and survives in \(D-st\), because \(C\) has no chord. ∎

For fixed \(r\), the crude running time is

\[
O\bigl(n^{q-2}(n+m)\bigr).
\]

Iterating over \(r\) recognizes induced subdivisions of \(C_q\).

---

## 5. One branch vertex

A connected subcubic graph with exactly one branch vertex is of one of the following two forms:

- a subdivision of \(K_{1,3}\);
- a cycle with one pendant path.

Indeed, after deleting the branch vertex, every component is a path. Its three incident edges are distributed either as \(1+1+1\), giving three arms, or as \(2+1\), giving a cycle and one pendant arm.

The tree case was handled by Lemma 3.1.

### Proposition 5.1

Let \(H\) consist of a cycle of length \(q\) and a pendant path of length \(a\) attached at a cycle vertex. Then \(H\)-ISC is polynomial-time solvable.

#### Proof

Enumerate an ordered induced path

\[
Q=(r=q_0,q_1,\ldots,q_a)
\]

of length \(a\). It is intended to be the first \(a\) edges of the pendant arm.

Form the graph

\[
F_Q=G\left[
\{r\}\cup
\{z\in V(G)\setminus V(Q):
N_G(z)\cap\{q_1,\ldots,q_a\}=\varnothing\}
\right].
\]

Apply Lemma 4.1 to \((F_Q,r,q)\).

If the algorithm finds a cycle \(C\), then \(C\cup Q\) induces a cycle of length at least \(q\) with a pendant path of length \(a\), and hence a subdivision of \(H\).

Conversely, from any induced subdivision of \(H\), truncate its pendant arm after \(a\) edges. The resulting \(Q\) is enumerated, and the cycle survives in \(F_Q\). ∎

A crude running time is \(O(n^{a+q-1}(n+m))\).

This proves the conjectured polynomial side for every connected subcubic target with at most one branch vertex.

---

## 6. Trees with two branch vertices

Every tree with exactly two branch vertices \(u,v\) consists of:

- a \(u\)-\(v\) path of some length \(d\geq1\);
- two pendant arms at \(u\), of lengths \(a_1,a_2\);
- two pendant arms at \(v\), of lengths \(b_1,b_2\).

Call this a double claw.

### Proposition 6.1

The induced-subdivision problem for every fixed double claw is polynomial-time solvable.

#### Proof

Enumerate:

- vertices \(u,v\);
- two induced paths of lengths \(a_1,a_2\) starting at \(u\);
- two induced paths of lengths \(b_1,b_2\) starting at \(v\);
- an induced path
  \[
  P=(p_0=u,p_1,\ldots,p_d=x)
  \]
  of length \(d\).

All these paths are required to have precisely the intersections prescribed by the target.

If \(x=v\), check whether their union is induced and accept if so.

Suppose \(x\neq v\), and let \(Z\) be the set of all enumerated vertices. Require that the only edges of \(G[Z]\) are the prescribed path edges, with the possible exception of the edge \(xv\), which is allowed as a one-edge completion of the central path.

Construct the induced graph \(D\) on

\[
\{x,v\}\cup
\{w\in V(G)\setminus Z:
N_G(w)\cap(Z\setminus\{x,v\})=\varnothing\}.
\]

Test whether \(x\) and \(v\) are connected in \(D\). If so, take a shortest \(x\)-\(v\) path \(R\).

Shortestness makes \(R\) induced, and the definition of \(D\) excludes every unwanted edge from its internal vertices to the fixed arms or to the fixed prefix of the central path. Thus \(Z\cup V(R)\) induces a double claw whose central path has length at least \(d\).

Conversely, in an induced subdivision of the target, truncate all four pendant arms to their prescribed lengths and take the first \(d\) edges of the central path starting at \(u\). The remaining suffix of the central path survives in \(D\). ∎

The straightforward implementation runs in \(n^{O(|V(H)|)}\) time.

---

## 7. A three-terminal completion lemma

For the next two target classes, I use the established **Three-in-a-Tree theorem**:

> Given a graph and three specified vertices, one can decide in polynomial time whether there is an induced tree containing all three vertices.

This is a proved algorithmic theorem, not an additional conjectural assumption.

The following consequence will be useful.

### Lemma 7.1 — claw completion

Suppose a fixed induced partial configuration \(G[Z]\) has three distinct designated ports \(t_1,t_2,t_3\in Z\). One can decide in polynomial time whether it can be completed, using vertices outside \(Z\), by an induced subdivided claw whose leaves are \(t_1,t_2,t_3\), with no completion vertex adjacent to \(Z\setminus\{t_1,t_2,t_3\}\).

Edges among the ports that already belong to the fixed configuration are ignored by the completion subproblem.

#### Proof

Let

\[
W=\{w\in V(G)\setminus Z:
N_G(w)\cap(Z\setminus\{t_1,t_2,t_3\})=\varnothing\}.
\]

Construct an auxiliary graph on \(\{t_1,t_2,t_3\}\cup W\), deleting the already prescribed edges among the ports.

Enumerate the first completion-neighbor \(z_i\in W\) of each \(t_i\), allowing some \(z_i\)'s to coincide. Delete every vertex \(w\in W\) that is adjacent to \(t_i\) without being \(z_i\). Reject a tuple if one of the chosen \(z_i\)'s is thereby inconsistent.

In the resulting graph every \(t_i\) has exactly one possible neighbor. Apply Three-in-a-Tree. If an induced tree exists, repeatedly prune leaves not among the three ports. The resulting induced tree has exactly three leaves, hence exactly one degree-\(3\) vertex, and is a subdivided claw with the desired leaves.

Conversely, any valid claw completion supplies one enumerated triple of first neighbors and survives the deletions. ∎

---

## 8. Theta targets

Let \(H\) be a theta graph with branch vertices \(u,v\) and three internally disjoint \(u\)-\(v\) threads of lengths

\[
\ell_1,\ell_2,\ell_3.
\]

Because \(H\) is simple, at most one \(\ell_i\) equals \(1\).

### Proposition 8.1

For every fixed theta graph \(H\), \(H\)-ISC is polynomial-time solvable.

#### Proof

First suppose all \(\ell_i\geq2\). Enumerate a vertex \(u'\) and three paths \(Q_i\), sharing only \(u'\), where \(Q_i\) has length \(\ell_i-1\). Let \(x_i\) be its other endpoint. Require that their union is induced.

Use Lemma 7.1 with ports \(x_1,x_2,x_3\). If the completion has center \(v'\), then the three paths

\[
u'Q_i x_i \;+\; x_iTv'
\]

are internally vertex-disjoint induced \(u'\)-\(v'\) paths. Their lengths are at least

\[
(\ell_i-1)+1=\ell_i.
\]

Their union is therefore an induced subdivision of \(H\).

Conversely, from a subdivision model of \(H\), take the first \(\ell_i-1\) edges of each thread starting at one branch vertex. The three remaining suffixes form a valid claw completion.

Now suppose, say, \(\ell_1=1\). Use \(u'\) itself as the first port and enumerate prefixes of lengths \(\ell_2-1,\ell_3-1\) on the other two threads. Apply Lemma 7.1 with ports \(u',x_2,x_3\), deleting from the auxiliary completion graph any fixed port-to-port edges already belonging to the two prefixes. The completion arm starting at \(u'\) has length at least \(1\), while the other two completed threads have lengths at least \(\ell_2,\ell_3\). The same converse argument applies. ∎

In particular, \(K_{2,3}\)-ISC is polynomial-time solvable.

---

## 9. A cycle with two pendant paths

Let \(H\) consist of a cycle with pendant paths of lengths \(a,b\) attached at distinct cycle vertices \(u,v\). Let the two \(u\)-\(v\) arcs of the cycle have lengths \(p,q\); at most one of \(p,q\) is \(1\).

### Proposition 9.1

For every such fixed \(H\), \(H\)-ISC is polynomial-time solvable.

#### Proof

Anchor the construction at the branch corresponding to \(u\).

1. Enumerate an induced pendant path of length \(a\) starting at \(u'\).
2. For each cycle arc of target length at least \(2\), enumerate a prefix from \(u'\) of length one less than that target length. Let its endpoint be \(x_i\).
3. If one cycle arc has target length \(1\), use \(u'\) itself as the corresponding port.
4. To encode the other pendant arm without first guessing its branch vertex, enumerate a path of length \(b-1\) from its prospective leaf towards the cycle. Let \(y\) be its endpoint nearest the prospective cycle branch. For \(b=1\), this is just the single vertex \(y\).

Require the fixed pieces to induce precisely their prescribed disjoint union. Apply Lemma 7.1 to the three ports \(x_1,x_2,y\), where \(x_i=u'\) for a target arc of length \(1\).

If the completing claw has center \(v'\), its first two arms complete two internally disjoint \(u'\)-\(v'\) paths of lengths at least \(p,q\). Together they form the required subdivided cycle. Its third arm followed by the fixed \((b-1)\)-edge path gives a pendant path at \(v'\) of length at least \(b\). The fixed arm at \(u'\) has length \(a\).

Conversely, in any subdivision model, truncate the two pendant arms at lengths \(a,b\), retain the first \(p-1\) and \(q-1\) edges of the two cycle arcs when appropriate, and view the remaining three paths incident with the second branch vertex as the claw completion. ∎

---

## 10. Disconnected targets

Let

\[
H=B\mathbin{\dot\cup}J,
\]

where every component of \(B\) is a path or subdivided claw, and \(J\) is one of the connected targets handled above.

Enumerate an induced copy \(B'\) of \(B\). Delete \(B'\) and every outside vertex having a neighbor in \(B'\), and run the algorithm for \(J\) in the remaining graph.

This is correct because:

- any subdivision model of \(B\) can be truncated componentwise to an induced copy of \(B\);
- different components of an induced subdivision are pairwise anticomplete;
- conversely, an induced copy of \(B\) together with a \(J\)-model in the anticomplete residual graph forms an \(H\)-model.

This proves Theorem 2.1.

---

## 11. Which two-branch targets remain?

Suppressing degree-\(2\) vertices, a connected subcubic graph with exactly two branch vertices \(u,v\) has one of five topological forms:

1. three \(u\)-\(v\) threads: a theta — covered;
2. two \(u\)-\(v\) threads and one pendant arm at each branch: covered;
3. one \(u\)-\(v\) thread and two pendant arms at each branch: a double claw — covered;
4. one \(u\)-\(v\) thread, a private cycle at one branch, and two pendant arms at the other;
5. one \(u\)-\(v\) thread and a private cycle at each branch, i.e. a barbell-type graph.

Cases 4 and 5 are not resolved here. The difficulty is that at least two unbounded induced paths must be chosen simultaneously. Replacing either by an arbitrary shortest path can destroy the anticompleteness needed by the other.

---

## 12. The minimal nonplanar frontier

### Proposition 12.1

Every nonplanar subcubic graph has at least six branch vertices.

If a connected nonplanar subcubic graph has exactly six branch vertices, then it is a subdivision of \(K_{3,3}\).

#### Proof

By Kuratowski's theorem, a nonplanar graph contains a subdivision of \(K_5\) or \(K_{3,3}\) as a subgraph. A subcubic graph cannot contain a subdivision of \(K_5\), because its five branch vertices would have degree \(4\). Hence it contains a subdivision \(K\) of \(K_{3,3}\).

The six branch vertices of \(K\) all have degree \(3\) in the ambient graph, proving the lower bound.

Suppose there are exactly six such vertices. Then they are precisely the branch vertices of \(K\). Each is saturated by its three edges in \(K\). Every internal vertex of \(K\) has degree \(2\) in \(K\); if it had an additional incident edge in the ambient graph, it would be a seventh degree-\(3\) vertex. Thus no edge leaves \(K\), and there is no additional edge among its vertices. Hence \(K\) is a connected component. If the ambient graph is connected, it equals \(K\). ∎

Thus the first genuinely nonplanar connected targets are exactly subdivisions of \(K_{3,3}\). For such a target, \(H\)-ISC is a length-constrained induced linkage problem involving six branch vertices and nine mutually compatible paths.

This structural fact does **not** prove hardness. In particular, induced-subdivision complexity is not monotone under taking target subgraphs or further subdividing target edges. Subdividing every edge of the input is also not a valid transfer: an original chord \(xy\) becomes a length-two path whose internal vertex can simply be omitted, potentially turning a non-induced model into an induced one.

---

## 13. Remaining gap

The two central unresolved fronts are therefore:

1. the planar side for more complicated branch topologies, already including the two private-cycle forms above and graphs with at least three branch vertices;
2. the nonplanar side for \(K_{3,3}\) and its subdivisions.

Finally, every fixed \(H\)-ISC language lies in \(\mathsf{NP}\). Therefore the literal assertion “in \(\mathsf P\) iff \(H\) is planar” necessarily presupposes \(\mathsf P\neq\mathsf{NP}\); the expected formal hard-side theorem would be NP-completeness for every nonplanar subcubic \(H\). No such hardness result is proved here.
