Attack the following open graph-theory problem.

Catalog id: antidirected_trees_in_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/antidirected_trees_in_digraphs/
Original entry: http://www.openproblemgarden.org/op/antidirected_trees_in_digraphs
Problem attributed to: Addario-Berry, Louigi, Havet, Frédéric, Linhares Sales, Claudia, Reed, Bruce A., Thomassé, Stéphan (posted 2013-02-26)

=== Problem statement (OpenProblemGarden) ===
Title: Antidirected trees in digraphs
An antidirected tree is an orientation of a tree in which every vertex has either indegree 0 or outdergree 0. Conjecture Let $ D $ be a digraph. If $ |A(D)| > (k-2) |V(D)| $ , then $ D $ contains every antidirected tree of order $ k $ .

=== Discussion / context (OpenProblemGarden) ===
The value $ k-2 $ would be best possible, since the oriented tree consisting of a vertex dominating $ k-1 $ other vertices is not contained in any digraph in which every vertex has outdegree $ k-2 $ . The condition on the trees be antidirected cannot be suppressed. In a bipartite digraph $ D $ with bipartition $ (A,B) $ such that all arcs are directed from $ A $ to $ B $ , all the trees contained in $ D $ are antidirected. This conjecture for symmetric digraphs is equivalent to the celebrated Erdös-Sos conjecture for undirected graphs. (see [E]). Conjecture Let $ G $ be a graph. If $ |E(G)| > \frac{1}{2} (k-2) |V(G)| $ , then $ G $ contains every tree of order $ k $ . Addario-Berry et al. Conjecture also implies Burr's conjecture (see Oriented trees in n-chromatic digraphs ) for antidirected trees, since every digraph with chromatic number $ 2k-2 $ contains a colour-critical digraph has minimum degree at least $ 2k-3 $ , and so whose number of vertices is at least $ \frac{2k-3}{2}|V(D)| $ , which exceeds $ (k-2) |V(D)| $ . This conjecture has only been proved [AHL+] for antidirected trees of diameter at most $ 3 $ .

=== References listed by OpenProblemGarden ===
- *[AHL+] L. Addario-Berry, F. Havet, C. Linhares Sales, B. Reed, and S. Thomassé. Oriented trees in digraphs. Discrete Mathematics, 313(8):967-974, 2013.
- [E] P. Erdös, Some problems in graph theory, Theory of Graphs and Its Applications, M. Fielder, Editor, Academic Press, New York, 1965, pp. 29--36.

=== Catalog page (statement + literature review) ===
Antidirected trees in digraphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture remains open in general. The most significant post-2013 advances are: Stein and Trujillo-Negrete (2024) proved the conjecture for all antidirected caterpillars (achieving $|A(D)|>(k-1)|V(D)|$ implies every antidirected $k$-arc caterpillar is present) and for $K_{2,s}$-free digraphs with $s=\lceil k/12\rceil$; Stein and Zárate-Guerén (2022) showed the conjecture is asymptotically true in oriented graphs for all balanced antidirected trees of bounded maximum degree and of size linear in $n$. The full conjecture for arbitrary antidirected trees under pure arc-density conditions is still open.

 Cited literature (5)

 
 
 
partial Antidirected subgraphs of oriented graphs
 (2022)
 

 
 Maya Stein, Camila Zárate-Guerén · arXiv preprint · arXiv:2212.00769

Proves the Addario-Berry et al. conjecture is asymptotically true in $n$-vertex oriented graphs for all balanced antidirected trees of bounded maximum degree and of size linear in $n$, using minimum semidegree $>(1+\eta)(k-1)$ as density surrogate.
 

 
 
partial Semidegree, edge density and antidirected subgraphs
 (2023)
 

 
 Maya Stein, Camila Zárate-Guerén · European Conference on Combinatorics, Graph Theory and Applications (EuroComb 2023)

Conference version presenting asymptotic results for balanced antidirected trees of bounded degree in oriented graphs with high minimum semidegree, addressing the Addario-Berry et al. arc-density conjecture.
 

 
 
survey Oriented trees and paths in digraphs
 (2024)
 

 
 Maya Stein · Surveys in Combinatorics 2024, Cambridge University Press · arXiv:2310.18719

Comprehensive survey covering all known results on oriented tree containment in digraphs; confirms the Addario-Berry et al. conjecture remains open, with the caterpillar case and diameter-$\leq 3$ case as the main resolved classes.
 

 
 
partial Antidirected trees in dense digraphs
 (2024)
 

 
 Maya Stein, Ana Trujillo-Negrete · arXiv preprint · arXiv:2404.10750

Proves the conjecture fully for antidirected caterpillars (every digraph with $>\!(k-1)n$ arcs contains every antidirected $k$-arc caterpillar), and for $K_{2,\lceil k/12\rceil}$-free digraphs under the same arc-density threshold.
 

 
 
partial Antidirected trees in directed graphs
 (2025)
 

 
 George Kontogeorgiou, Giovanne Santos, Maya Stein · arXiv preprint · arXiv:2501.11726

Establishes minimum semidegree and maximum degree conditions (replacing arc-density conditions) that guarantee containment of balanced antidirected trees of bounded maximum degree, extending prior asymptotic results.
 

 

 Reviewer notes. All verified papers use the edge convention 'k arcs in the tree' (i.e., tree order k+1), which is consistent with the OPG formulation after shifting k by 1. The EuroComb 2023 entry (Stein–Zárate-Guerén) may be a conference version of arXiv:2212.00769; if so, only the arXiv paper need be cited. No paper fully resolves the conjecture for all antidirected trees under arc-density conditions. The Klimošová–Stein 2023 result on antidirected paths in oriented graphs was mentioned in the survey but could not be independently verified within the search budget.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 164s.
 

Conjecture. Let $ D $ be a digraph. If $ |A(D)| > (k-2) |V(D)| $ , then $ D $ contains every antidirected tree of order $ k $ .

Discussion

The value $ k-2 $ would be best possible, since the oriented tree consisting of a vertex dominating $ k-1 $ other vertices is not contained in any digraph in which every vertex has outdegree $ k-2 $ . The condition on the trees be antidirected cannot be suppressed. In a bipartite digraph $ D $ with bipartition $ (A,B) $ such that all arcs are directed from $ A $ to $ B $ , all the trees contained in $ D $ are antidirected. This conjecture for symmetric digraphs is equivalent to the celebrated Erdös-Sos conjecture for undirected graphs. (see [E]). Conjecture Let $ G $ be a graph. If $ |E(G)| > \frac{1}{2} (k-2) |V(G)| $ , then $ G $ contains every tree of order $ k $ . Addario-Berry et al. Conjecture also implies Burr's conjecture (see Oriented trees in n-chromatic digraphs ) for antidirected trees, since every digraph with chromatic number $ 2k-2 $ contains a colour-critical digraph has minimum degree at least $ 2k-3 $ , and so whose number of vertices is at least $ \frac{2k-3}{2}|V(D)| $ , which exceeds $ (k-2) |V(D)| $ . This conjecture has only been proved [AHL+] for antidirected trees of diameter at most $ 3 $ .

Bibliography

★ [AHL+]
 L. Addario-Berry, F. Havet, C. Linhares Sales, B. Reed, and S. Thomassé. Oriented trees in digraphs. Discrete Mathematics, 313(8):967-974, 2013.

 [E]
 P. Erdös, Some problems in graph theory, Theory of Graphs and Its Applications, M. Fielder, Editor, Academic Press, New York, 1965, pp. 29--36.

Related conjectures

 
 related to
 Oriented trees in n-chromatic digraphs
 partial
 The OPG page explicitly states and proves that the Addario-Berry et al. conjecture implies Burr's conjecture ONLY for antidirected trees: chi(D) >= 2k-2 yields a colour-critical subdigraph of min degree >= 2k-3, hence arc density > (k-2)|V|, triggering the source conjecture. But Burr's conjecture concerns ALL oriented trees, so the source does not imply the full target (subfamily-only implication). The converse also fails: high arc density does not force high chromatic number (bipartite digraphs with all arcs one way have chi=2 and arbitrary density, as the source context notes). Genuine partial-implication link, but no full implication in either direction, so related_only.
 

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
  "one_line": "I prove the conjectured threshold under a short almost-antidirected odd-cycle exclusion, and obtain an asymptotically sharp density bound for highly unbalanced trees.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of these elementary partial results is not claimed."
}
```

## 1. Results obtained

Throughout, digraphs are finite and loopless, with no parallel arcs; opposite arcs are allowed. Copies need not be induced. The case \(k=1\) is trivial, so assume \(k\ge 2\).

Let \(T\) be an antidirected tree, with source class \(S\) and sink class \(R\). Write
\[
s=|S|,\qquad t=|R|,\qquad s+t=k,
\]
and define
\[
\lambda(T)=\max\{\operatorname{dist}_T(x,y):x\in S,\ y\in R\}.
\]
Thus \(\lambda(T)\) is odd and at most \(\operatorname{diam}(T)\).

Call an orientation of an odd cycle **almost antidirected** if, within the chosen cycle, exactly one vertex has both positive indegree and positive outdegree, while every other vertex is a source or a sink. For length three this is precisely a transitive triangle. Extra arcs in the ambient digraph are irrelevant to this definition.

### Theorem 1: an explicit obstruction dichotomy

If
\[
|A(D)|>(k-2)|V(D)|,
\]
then \(D\) contains either

1. a copy of \(T\), or
2. an almost-antidirected odd cycle of some length \(\ell\) satisfying
   \[
   3\le \ell\le \lambda(T).
   \]

Consequently, the conjectured threshold is valid whenever the second possibility is excluded. In particular:

- **Bipartite hosts:** the conjecture holds if the underlying undirected graph of \(D\) is bipartite. Arcs in both directions across its bipartition are allowed.
- **Large odd girth:** it holds if the underlying graph has odd girth greater than \(\operatorname{diam}(T)\).
- **Small-diameter targets:** every transitive-triangle-free digraph satisfying the conjectured density contains every antidirected tree of order \(k\) and diameter at most \(4\).

I also obtain the following bound without any restriction on the host.

### Theorem 2: a leaf-sensitive density bound

Let
\[
\ell(T)=\max\bigl\{
|\{v\in S:\deg_T(v)=1\}|,
|\{v\in R:\deg_T(v)=1\}|
\bigr\},
\qquad h=k-\ell(T).
\]
Then
\[
|A(D)|>
\bigl(k-2+\max\{h-2,0\}\bigr)|V(D)|
\tag{1}
\]
guarantees a copy of \(T\).

In particular, if \(r=\min\{s,t\}\ge2\), then the simpler condition
\[
|A(D)|>(k+2r-5)|V(D)|
\tag{2}
\]
suffices. The ratio of this sufficient coefficient to \(k-2\) tends to \(1\) whenever \(r=o(k)\).

These are partial results only. Here are complete proofs.

## 2. A weighted bipartite embedding lemma

**Lemma.** Let \(H\) be a bipartite graph with specified parts \(L,R'\). If
\[
e(H)>(t-1)|L|+(s-1)|R'|,
\tag{3}
\]
then \(H\) contains the underlying tree of \(T\), with \(S\) mapped into \(L\) and \(R\) mapped into \(R'\).

**Proof.** Repeatedly delete a vertex of \(L\) whose current degree is at most \(t-1\), or a vertex of \(R'\) whose current degree is at most \(s-1\).

If this procedure deleted every edge, charging each edge to the first of its endpoints deleted would give
\[
e(H)\le (t-1)|L|+(s-1)|R'|,
\]
contrary to (3). Thus a nonempty subgraph \(H_0\) remains, satisfying
\[
d_{H_0}(x)\ge t\quad(x\in L\cap V(H_0)),
\qquad
d_{H_0}(y)\ge s\quad(y\in R'\cap V(H_0)).
\]

Root \(T\) at a vertex of \(S\) and embed it greedily. When a new sink is required, at most \(t-1\) vertices of the right part have already been used, whereas its parent has at least \(t\) neighbors. When a new source is required, the corresponding bounds are \(s-1\) and \(s\). Hence the role-respecting embedding can be completed. \(\square\)

## 3. Proof of Theorem 1

### 3.1. Split each vertex into its two possible roles

Construct a bipartite graph \(B(D)\) with parts
\[
V^+=\{v^+:v\in V(D)\},\qquad
V^-=\{v^-:v\in V(D)\},
\]
putting an edge \(u^+v^-\) exactly when \(u\to v\) is an arc of \(D\).

Writing \(n=|V(D)|\), we have
\[
e(B(D))=|A(D)|>(k-2)n
=(t-1)|V^+|+(s-1)|V^-|.
\]
The lemma therefore gives an embedding of \(T\) into \(B(D)\), with sources in \(V^+\) and sinks in \(V^-\).

Project this embedding back to \(D\), identifying \(v^+\) and \(v^-\) with \(v\). The resulting map
\[
f:V(T)\longrightarrow V(D)
\]
preserves every arc and is injective separately on \(S\) and on \(R\).

The sole possible obstruction is a **cross-role collision**:
\[
f(x)=f(y),\qquad x\in S,\ y\in R.
\]

### 3.2. A shortest collision gives the claimed cycle

If there is no collision, \(f\) is a copy of \(T\).

Otherwise choose a colliding pair \(x,y\) minimizing
\[
\ell=\operatorname{dist}_T(x,y),
\]
and write its tree path as
\[
x=x_0,x_1,\ldots,x_\ell=y.
\]
Because \(x,y\) lie in opposite bipartition classes, \(\ell\) is odd. Also \(\ell\ne1\), since an adjacent colliding pair would map an arc to a loop.

By minimality, no two vertices of this path have the same image except its endpoints. Indeed, any other repetition would give a colliding pair at smaller tree distance. Hence
\[
f(x_0),f(x_1),\ldots,f(x_{\ell-1})
\]
are the distinct vertices of a cycle in \(D\).

Along the tree path, every internal vertex is a source or a sink. Identifying the source endpoint \(x_0\) with the sink endpoint \(x_\ell\) creates exactly one vertex having one incoming and one outgoing cycle arc. The resulting cycle is therefore almost antidirected.

Finally,
\[
3\le\ell\le\lambda(T),
\]
as required. \(\square\)

### Consequences

Every almost-antidirected odd cycle is, after forgetting orientations, an odd cycle. Thus underlying odd girth greater than \(\operatorname{diam}(T)\) excludes every obstruction from Theorem 1.

If \(\operatorname{diam}(T)\le4\), the only possible obstruction length is \(3\), namely a transitive triangle.

Notice that this last condition is weaker than requiring the underlying graph to be triangle-free: directed cyclic triangles are allowed.

## 4. Proof of Theorem 2

By reversing every arc of both \(D\) and \(T\), if necessary, assume that \(T\) has \(\ell(T)\) sink leaves. Remove all those leaves, obtaining a tree \(T_0\) of order
\[
h=k-\ell(T).
\]

Set
\[
p=k-1,\qquad q=\max\{1,h-1\}.
\]
The coefficient in (1) is exactly
\[
p+q-2=k-2+\max\{h-2,0\}.
\]

Apply the deletion argument from the preceding lemma to \(B(D)\), now deleting left vertices of degree at most \(p-1\) and right vertices of degree at most \(q-1\). The assumed density leaves a nonempty arc-subdigraph \(D_0\) such that
\[
d^+_{D_0}(v)>0\implies d^+_{D_0}(v)\ge k-1,
\tag{4}
\]
and
\[
d^-_{D_0}(v)>0\implies d^-_{D_0}(v)\ge \max\{1,h-1\}.
\tag{5}
\]

Here a vertex need not have both kinds of degree positive. This causes no problem because every vertex of an antidirected tree needs only one of the two roles.

### Embed \(T_0\)

If \(h=1\), its remaining vertex is a source; map it to the tail of any arc of \(D_0\).

If \(h\ge2\), first map an edge of \(T_0\) to an arc of \(D_0\), then extend greedily. Every newly embedded source has positive outdegree, and every newly embedded sink has positive indegree. Both relevant degree bounds are at least \(h-1\).

When adding another vertex of \(T_0\), at most \(h-1\) vertices have been used. Since the host is loopless, at most \(h-2\) of them can be neighbors of the parent in the required direction. Thus an unused neighbor is available.

This gives an injective copy of \(T_0\) in the original digraph, not merely in its split graph.

### Attach the removed leaves

All removed vertices are sink leaves. Add them one at a time.

Their parents are already embedded sources, each having outdegree at least \(k-1\) by (4). Before any addition, at most \(k-1\) vertices have been used; at most \(k-2\) of them can be outneighbors of the parent. Hence an unused outneighbor always exists.

This completes a copy of \(T\). \(\square\)

### Derivation of the unbalanced-tree bound

Let \(r=\min\{s,t\}\), and consider the larger bipartition class, of size \(k-r\). Since every edge has exactly one endpoint in that class,
\[
\sum_{v\text{ in the larger class}}(\deg_T(v)-1)
=(k-1)-(k-r)=r-1.
\]
Every nonleaf contributes at least one. Therefore the larger class has at most \(r-1\) nonleaves and at least
\[
(k-r)-(r-1)=k-2r+1
\]
leaves. Consequently,
\[
h=k-\ell(T)\le 2r-1.
\]
For \(r\ge2\), Theorem 2 now gives
\[
k-2+\max\{h-2,0\}\le k+2r-5,
\]
proving (2). When \(r=1\), the tree is a directed star, and Theorem 2 gives the exact coefficient \(k-2\).

## 5. A non-caterpillar illustration

Let \(T_r\) be the tree obtained by subdividing every edge of \(K_{1,r}\), with each subdivision vertex a source and the original center and leaves sinks. For \(r\ge3\), this is not a caterpillar.

It has
\[
k=2r+1,\qquad \operatorname{diam}(T_r)=4,\qquad \ell(T_r)=r.
\]
Thus the two results give:

- If \(D\) is transitive-triangle-free, then
  \[
  |A(D)|>(2r-1)|V(D)|
  \quad\Longrightarrow\quad T_r\subseteq D.
  \]
  This is the conjectured threshold.
- Without any host restriction,
  \[
  |A(D)|>(3r-2)|V(D)|
  \quad\Longrightarrow\quad T_r\subseteq D.
  \]

Both statements also hold for the reversed orientation.

## 6. Sharpness and the remaining gap

For any fixed tree \(T\) of order \(k\), disjoint unions of bidirected copies of \(K_{k-1}\) have
\[
|A(D)|=(k-2)|V(D)|
\]
and contain no copy of \(T\), because every connected component has only \(k-1\) vertices. Thus the coefficient in the unrestricted conjecture is necessary even for each individual target tree. In particular, the bound above is asymptotically sharp when \(\min\{s,t\}=o(k)\).

The exact coefficient is also necessary uniformly over all target trees even within bipartite hosts: the bidirected \(K_{k-2,k-2}\) has arc density \(k-2\) and contains no out-star of order \(k\).

The unresolved issue is precisely the projection collision. The split-graph argument always produces a role-injective homomorphic image at the conjectured density, but it need not produce an injective image in \(D\). For example, a bidirected triangle has a split graph of minimum degree \(2\), containing a role-correct four-vertex antidirected path, while the original digraph has only three vertices. This example is at equality, not above the conjectured threshold, so it is **not** a counterexample.

Theorem 1 excludes collisions by forbidding their short odd-cycle witnesses. Theorem 2 instead pays additional density to avoid used original vertices directly. Neither argument removes that additional assumption or density cost in general. No proof or counterexample to the unrestricted conjecture is obtained here.
