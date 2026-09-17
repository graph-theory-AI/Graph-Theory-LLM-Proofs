Attack the following open graph-theory problem.

Catalog id: bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree/
Original entry: http://www.openproblemgarden.org/op/bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree
Problem attributed to: Kostochka, Alexandr V., Reed, Bruce A. (posted 2009-04-17)

=== Problem statement (OpenProblemGarden) ===
Title: Bounding the chromatic number of triangle-free graphs with fixed maximum degree
Conjecture A triangle-free graph with maximum degree $ \Delta $ has chromatic number at most $ \ceil{\frac{\Delta}{2}}+2 $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is a special case of Reed's $ \omega $ , $ \Delta $ , and $ \chi $ conjecture, which posits that for any graph, $ \chi \leq \lceil\frac 12(\Delta+1+\omega)\rceil $ , where $ \omega $ , $ \Delta $ , and $ \chi $ are the clique number, maximum degree, and chromatic number of the graph respectively. Reed's conjecture is very easy to prove for complements of triangle-free graphs, but the triangle-free case seems challenging and interesting in its own right. This conjecture is very much true for large values of $ \Delta $ ; Johansson proved that triangle-free graphs have chromatic number at most $ \frac{9\Delta}{\ln \Delta} $ . Surprisingly, the question appears to be open for every value of $ \Delta $ greater than four, up until Johansson's result implies the conjecture. Kostochka previously proved that the chromatic number of a triangle-free graph is at most $ \frac{2\Delta}{3}+2 $ , and he proved that for every $ \Delta \geq 5 $ there is a $ g $ for which a graph of girth $ g $ has chromatic number at most $ \frac{\Delta}2+2 $ . Specifically, he showed that $ g \geq 4(\Delta+2)\ln \Delta $ is sufficient. In [K] he posed the general problem: "To find the best upper estimate for the chromatic number of the graph in terms of the maximal degree and density or girth." The conjecture is implied by Brooks' Theorem for $ \Delta\leq 5 $ . The three smallest open values of $ \Delta $ offer natural entry points to this problem. The easiest seems to be: Problem Does there exist a $ 6 $ -chromatic triangle-free graph of maximum degree 6? Perhaps looking at graphs of girth at least five would also be a good starting point.

=== References listed by OpenProblemGarden ===
- [K] Kostochka, A. V., Degree, girth and chromatic number. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, pp. 679--696, Colloq. Math. Soc. János Bolyai, 18, North-Holland, Amsterdam-New York, 1978.
- *[R] Reed, B.A., , and , J. Graph Theory 27 (1998) 177-212.

=== Catalog page (statement + literature review) ===
Bounding the chromatic number of triangle-free graphs with fixed maximum degree — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The Kostochka-Reed conjecture that every triangle-free graph with maximum degree $\Delta$ has chromatic number at most $\lceil \Delta/2 \rceil + 2$ remains open for finite values of $\Delta$ between 6 and the threshold above which Johansson's $O(\Delta/\log\Delta)$ bound (with Molloy's optimal constant) implies it. Computational work by Goedgebeur on minimal triangle-free 6-chromatic graphs has narrowed the smallest open case (whether a 6-chromatic triangle-free graph of maximum degree 6 exists) by showing such a graph would need between 32 and 40 vertices, but no proof or counterexample for the original conjecture has been published.

 Cited literature (1)

 
 
 
partial On minimal triangle-free 6-chromatic graphs
 (2017)
 

 
 Jan Goedgebeur · arXiv preprint · arXiv:1707.07581 · doi:10.1002/jgt.22467

Computationally shows that the smallest triangle-free 6-chromatic graphs have between 32 and 40 vertices and catalogues triangle-free 5-chromatic graphs up to 24 vertices, providing partial computational support for Reed's conjecture (and hence the Kostochka-Reed $\lceil\Delta/2\rceil+2$ bound) on triangle-free graphs of small order, directly relevant to the smallest open case ($\Delta=6$) of the conjecture.
 

 

 Reviewer notes. ScienceDirect paywalls (HTTP 403) prevented direct verification of 'A note on Reed's conjecture for triangle-free graphs' (Discrete Math. 2023, S0012365X23002959), so it is not cited despite being relevant. Several asymptotic results (Johansson 1996, Molloy 2019, Bonamy-Kelly-Nelson-Postle, Davies-Illingworth) confirm the conjecture for sufficiently large $\Delta$ but were already implied by Johansson's bound at the time of OPG posting; the conjecture's challenge is for fixed small $\Delta\geq 6$, and there no full proof or counterexample has been verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. A triangle-free graph with maximum degree $ \Delta $ has chromatic number at most $ \ceil{\frac{\Delta}{2}}+2 $ .

Keywords:
chromatic number · girth · maximum degree · triangle free

Discussion

This conjecture is a special case of Reed's $ \omega $ , $ \Delta $ , and $ \chi $ conjecture, which posits that for any graph, $ \chi \leq \lceil\frac 12(\Delta+1+\omega)\rceil $ , where $ \omega $ , $ \Delta $ , and $ \chi $ are the clique number, maximum degree, and chromatic number of the graph respectively. Reed's conjecture is very easy to prove for complements of triangle-free graphs, but the triangle-free case seems challenging and interesting in its own right. This conjecture is very much true for large values of $ \Delta $ ; Johansson proved that triangle-free graphs have chromatic number at most $ \frac{9\Delta}{\ln \Delta} $ . Surprisingly, the question appears to be open for every value of $ \Delta $ greater than four, up until Johansson's result implies the conjecture. Kostochka previously proved that the chromatic number of a triangle-free graph is at most $ \frac{2\Delta}{3}+2 $ , and he proved that for every $ \Delta \geq 5 $ there is a $ g $ for which a graph of girth $ g $ has chromatic number at most $ \frac{\Delta}2+2 $ . Specifically, he showed that $ g \geq 4(\Delta+2)\ln \Delta $ is sufficient. In [K] he posed the general problem: "To find the best upper estimate for the chromatic number of the graph in terms of the maximal degree and density or girth." The conjecture is implied by Brooks' Theorem for $ \Delta\leq 5 $ . The three smallest open values of $ \Delta $ offer natural entry points to this problem. The easiest seems to be: Problem Does there exist a $ 6 $ -chromatic triangle-free graph of maximum degree 6? Perhaps looking at graphs of girth at least five would also be a good starting point.

Bibliography

 [K]
 Kostochka, A. V., Degree, girth and chromatic number. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, pp. 679--696, Colloq. Math. Soc. János Bolyai, 18, North-Holland, Amsterdam-New York, 1978.

★ [R]
 Reed, B.A., $ \omega, \Delta $ , and $ \chi $ , J. Graph Theory 27 (1998) 177-212.

Related conjectures

 
 implied by
 Reed's omega, delta, and chi conjecture
 partial
 Triangle-free means omega(G) <= 2. Reed's conjectured bound then gives chi <= ceil((Delta+1)/2 + 1) = ceil((Delta+3)/2). For even Delta this equals Delta/2 + 2 = ceil(Delta/2)+2; for odd Delta it equals (Delta+3)/2 = ceil(Delta/2)+1 <= ceil(Delta/2)+2. So Reed's conjecture (source) implies the triangle-free conjecture (target) by restriction to omega <= 2, with the correct rounding check. The target's own Open Problem Garden context states explicitly: 'This conjecture is a special case of Reed's omega, Delta, and chi conjecture.' Direction as claimed.
 

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
  "one_line": "For maximum degree 6, the conjecture holds if deleting at most two vertices makes the degree-6 subgraph bipartite, and hence if there are at most nine degree-6 vertices.",
  "would_publish": false,
  "caveats": "This is a structural special case, not a resolution of the conjecture; no novelty or independent literature-status claim is made."
}
```

## 1. Result obtained

All graphs below are finite and simple. For a graph \(G\), let
\[
H_k(G)=G[\{v:d_G(v)=k\}].
\]

I prove the following sufficient condition.

**Theorem.** Let \(q\ge 3\), and let \(G\) be triangle-free with maximum degree at most \(q+1\). Put \(H=H_{q+1}(G)\). If there is a set \(S\subseteq V(H)\) such that
\[
|S|\le 2
\qquad\text{and}\qquad
\chi(H-S)\le q-3,
\]
then \(G\) is \(q\)-colorable.

In particular, taking \(q=5\) gives:

**Corollary 1.** A triangle-free graph of maximum degree at most \(6\) is \(5\)-colorable whenever its degree-\(6\) subgraph can be made bipartite by deleting at most two vertices.

I also prove the following small-order consequence without computational enumeration.

**Corollary 2.** A triangle-free graph of maximum degree at most \(6\) with at most nine vertices of degree \(6\) is \(5\)-colorable.

Thus any counterexample at \(\Delta=6\) must have at least ten degree-\(6\) vertices, and its degree-\(6\) subgraph must have odd-cycle transversal number at least three.

The proof uses only Brooks’ theorem and elementary list-coloring arguments.

## 2. Degree-list coloring facts

An \(A\)-coloring of a graph \(F\), where \(A(v)\) is a list of colors at each vertex, is a proper coloring assigning to each \(v\) a color in \(A(v)\).

We need the following standard obstruction, for which I include a proof.

**Lemma 1.** Let \(F\) be connected and triangle-free, with
\[
|A(v)|\ge d_F(v)\qquad(v\in V(F)).
\]
If \(F\) is not \(A\)-colorable, then:

1. \(|A(v)|=d_F(v)\) for every vertex;
2. every block of \(F\) is an edge or an odd cycle, apart from the possible one-vertex graph;
3. if additionally every list has size at least two, then every leaf block is an odd cycle of length at least five. The non-cutvertices of each leaf block have identical lists of size two. If \(F\) consists of a single block, it is an odd cycle and all its lists are identical two-element sets.

**Proof.** Two greedy observations are useful.

First, if some vertex \(z\) has \(|A(z)|>d_F(z)\), root a spanning tree at \(z\) and color vertices in an order in which children precede parents. Every vertex other than \(z\) has an uncolored neighbor when it is colored; \(z\) has a spare color at the end. This proves assertion 1.

Second, suppose \(uv\in E(F)\), \(F-u\) is connected, and
\[
A(u)\setminus A(v)\ne\varnothing.
\]
Color \(u\) with a color \(c\) in this difference. Then greedily color \(F-u\) toward root \(v\). At the last vertex \(v\), the color on \(u\) does not belong to \(A(v)\), so at most \(d_F(v)-1\) colors from its list are forbidden. Thus this also produces an \(A\)-coloring.

Now suppose \(F\) has a block \(B\) that is neither complete nor an odd cycle. Greedily color \(F-V(B)\) in decreasing order of distance from \(B\). The residual lists on \(B\) have size at least the corresponding degrees in \(B\).

If these residual lists are not all identical, some adjacent pair has different lists. Since \(B\) is 2-connected, the second greedy observation colors \(B\). If all residual lists are identical, their common size is at least \(\Delta(B)\), and Brooks’ theorem colors \(B\). Either way, the coloring extends to all of \(F\).

Consequently, every block of an uncolorable \(F\) is complete or an odd cycle. Triangle-freeness gives assertion 2.

Finally, suppose every list has size at least two. Assertion 1 gives \(\delta(F)\ge2\). A leaf block cannot be an edge, because its non-cutvertex would have degree one. Hence it is an odd cycle of length at least five.

Its non-cutvertices have degree two and therefore two-element lists. If two consecutive non-cutvertices had different lists, the second greedy observation would color \(F\). Their lists are consequently identical along the path of non-cutvertices. The same argument applies around the whole cycle when \(F\) has only one block. ∎

## 3. A precoloring extension lemma

The next lemma allows a small exceptional set to receive distinct reserved colors.

**Lemma 2.** Let \(G\) be triangle-free, let \(q\ge3\), and put
\[
H=G[\{v:d_G(v)\ge q+1\}],
\qquad
L=V(G)\setminus V(H).
\]
Suppose \(S\subseteq V(H)\) satisfies
\[
|S|\le3,\qquad \chi(H-S)\le q-3,
\]
and every vertex in \(L\) has at most one neighbor in \(S\). Then \(G\) is \(q\)-colorable.

**Proof.** Use a palette of \(q\) colors. Color \(H-S\) using \(q-3\) ordinary colors, and give the vertices of \(S\) distinct colors from the three reserved colors.

For \(v\in L\), remove the colors appearing on its neighbors in \(H\), leaving a list \(A(v)\). Since \(d_G(v)\le q\),
\[
|A(v)|\ge q-d_H(v)\ge d_{G[L]}(v).
\]
Moreover, \(v\) sees at most \(q-3\) ordinary colors and at most one reserved color. Hence
\[
|A(v)|\ge2.
\]

Suppose some component \(F\) of \(G[L]\) is not list-colorable. By Lemma 1, it has adjacent non-cutvertices \(u,v\) in a leaf odd cycle with
\[
A(u)=A(v),\qquad |A(u)|=2.
\]

For a list to have size two, its vertex must see all \(q-3\) ordinary colors and one reserved color. Equality of the two lists means that \(u\) and \(v\) see the same reserved color. That reserved color was assigned to a unique vertex \(s\in S\). Thus \(s,u,v\) form a triangle, a contradiction.

Every component of \(G[L]\) can therefore be colored. ∎

For example, the neighborhood condition in Lemma 2 is automatic when \(S\) is a clique. The main theorem strengthens this, under the maximum-degree hypothesis, to an arbitrary set of two exceptional vertices.

## 4. Proof of the theorem

Let
\[
r=q-3,
\qquad
H=H_{q+1}(G),
\qquad
L=V(G)\setminus V(H).
\]
Choose \(S\) inclusion-minimal among sets of size at most two for which \(H-S\) is \(r\)-colorable.

If \(|S|\le1\), Lemma 2 applies immediately. If \(S\) consists of two adjacent vertices, triangle-freeness ensures that every vertex in \(L\) has at most one neighbor in \(S\), so Lemma 2 again applies.

It remains to consider
\[
S=\{s,t\},\qquad st\notin E(G).
\]

### 4.1. Each exceptional vertex has at most four low-degree neighbors

Minimality gives
\[
\chi(H-s)>r,\qquad \chi(H-t)>r.
\]
If \(r\ge1\) and \(d_H(s)<r\), an \(r\)-coloring of \(H-S\) could be extended to \(s\), contradicting \(\chi(H-t)>r\). Thus \(d_H(s)\ge r\), and similarly \(d_H(t)\ge r\). For \(r=0\), these inequalities are automatic.

Since \(\Delta(G)\le q+1=r+4\),
\[
d_L(s)\le4,\qquad d_L(t)\le4. \tag{1}
\]

### 4.2. Color \(s,t\) alike initially

Color \(H-S\) with the \(r\) ordinary colors, and give both \(s\) and \(t\) one new color \(\alpha\). This is proper because \(s,t\) are nonadjacent. Let \(\beta,\gamma\) be the other two colors in the \(q\)-color palette.

For each \(v\in L\), form its residual list \(A(v)\). As before,
\[
|A(v)|\ge d_{G[L]}(v),
\qquad
\{\beta,\gamma\}\subseteq A(v).
\]

If this precoloring extends, we are done. Otherwise, let \(F\) be an uncolorable component of \(G[L]\).

By Lemma 1, all lists in \(F\) are tight, \(\delta(F)\ge2\), and its blocks are edges or odd cycles.

Consider a degree-two non-cutvertex \(v\) of a leaf cycle. Tightness gives
\[
A(v)=\{\beta,\gamma\}.
\]
Thus its neighbors in \(H\) use all \(r\) ordinary colors and \(\alpha\), totaling \(r+1=q-2\) distinct colors.

But \(v\) already has two neighbors in \(F\) and has total degree at most \(q\). Therefore it has exactly \(q-2\) neighbors in \(H\), with distinct colors. In particular,
\[
|N_G(v)\cap\{s,t\}|=1. \tag{2}
\]
Label \(v\) by its unique neighbor in \(\{s,t\}\).

Adjacent labeled vertices cannot have the same label, since that would create a triangle.

### 4.3. An obstruction exhausts both four-neighbor budgets

If \(F\) consists of a single block, it is an odd cycle. Every vertex on it satisfies (2), and the labels \(s,t\) would properly 2-color this odd cycle—a contradiction.

Hence \(F\) has at least two blocks and therefore at least two leaf blocks. Every leaf block is an odd cycle of length at least five. Its non-cutvertices form a path on at least four vertices. Their labels alternate, so each leaf block contributes at least two distinct neighbors of \(s\) and at least two distinct neighbors of \(t\).

Non-cutvertices from different leaf blocks are distinct. Consequently,
\[
d_L(s)\ge4,\qquad d_L(t)\ge4.
\]
Together with (1), this exhausts both neighbor budgets. All neighbors of \(s\) and \(t\) in \(L\) are among these labeled non-cutvertices, each of which has exactly one neighbor in \(S\). Therefore
\[
N_G(s)\cap N_G(t)\cap L=\varnothing.
\]

The hypothesis of Lemma 2 now holds for \(S=\{s,t\}\). Recoloring \(s,t\) with distinct reserved colors and applying that lemma yields a \(q\)-coloring of \(G\).

This completes the proof. ∎

## 5. Why nine degree-\(6\) vertices suffice

The following elementary fact supplies the numerical corollary.

**Lemma 3.** Every triangle-free graph on at most nine vertices can be made bipartite by deleting at most two vertices.

**Proof.** Adding isolated vertices reduces the claim to graphs \(J\) on exactly nine vertices.

First, \(J\) has an independent set of size four:

- A vertex of degree at least four has four independent neighbors.
- A vertex of degree at most two has at least six nonneighbors. Every triangle-free graph on six vertices has an independent set of size three, which together with the original vertex gives four.
- If neither case occurs, every vertex has degree three, impossible on nine vertices by the handshaking lemma.

For completeness, the six-vertex fact follows immediately: a vertex with at least three neighbors gives an independent triple; otherwise, among three nonneighbors of a vertex there is a nonadjacent pair, which together with that vertex is independent.

If \(J\) has an independent set \(I\) of size five, its remaining four vertices contain an independent pair. Their union with \(I\) induces a bipartite graph on seven vertices, as required.

We may therefore assume \(\alpha(J)=4\). Choose an independent set \(I\) of size four and put
\[
R=J-I.
\]
If \(R\) has an independent triple, we again obtain an induced bipartite graph on seven vertices.

Otherwise \(R\cong C_5\). Indeed, a triangle-free graph on five vertices with no independent triple has maximum degree at most two and minimum degree at least two, and is therefore \(C_5\).

Each vertex of \(I\) has at most two neighbors on this \(C_5\), so there are at most eight edges between \(I\) and \(R\). Some vertex \(c\in R\) consequently has at most one neighbor in \(I\). It cannot have none, since then \(I\cup\{c\}\) would be independent. Let its unique neighbor in \(I\) be \(u\).

Now
\[
I'=(I-\{u\})\cup\{c\}
\]
is another independent four-set. Its complement is
\[
R'=(R-\{c\})\cup\{u\}.
\]
The vertex \(u\) has degree at most one in \(R'\): it had at most two neighbors on \(R\), one of which was \(c\). Hence \(R'\not\cong C_5\), so \(R'\) has an independent triple. Combining it with \(I'\) gives an induced bipartite graph on seven vertices.

Deleting the other two vertices proves the lemma. ∎

Apply Lemma 3 to \(H_6(G)\), and then apply the main theorem with \(q=5\). This proves Corollary 2.

## 6. What remains unresolved

The established necessary conditions for a \(\Delta=6\) counterexample are
\[
|V(H_6(G))|\ge10,
\qquad
\text{odd-cycle transversal number of }H_6(G)\ge3.
\]

There is no argument here forcing either condition to fail. The hypothesis is genuinely restrictive: three disjoint \(5\)-cycles already require three vertex deletions to become bipartite. Such a graph can occur as the degree-\(6\) subgraph of an easily 3-colorable graph, by attaching four leaves to each cycle vertex. Thus failure of the sufficient condition is not itself evidence of a counterexample.

The key counting step also explains a limitation of this method: two leaf cycles force four low-degree neighbors at each exceptional vertex, and the maximum-degree hypothesis makes four the entire available budget. At larger degree bounds this need not exhaust the budget.

I have not performed a computational search or established novelty of these structural lemmas. The full conjecture—including the remaining \(\Delta=6\) case—is not resolved here.

Finally, the catalog’s order bounds for *unrestricted* triangle-free \(6\)-chromatic graphs should not be interpreted as an upper bound of \(40\) vertices for a maximum-degree-\(6\) witness. That additional degree restriction changes the existence question; none of those numerical literature claims is used above.
