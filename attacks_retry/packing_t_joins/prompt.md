Attack the following open graph-theory problem.

Catalog id: packing_t_joins
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/packing_t_joins/
Original entry: http://www.openproblemgarden.org/op/packing_t_joins
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Packing T-joins
Conjecture There exists a fixed constant $ c $ (probably $ c=1 $ suffices) so that every graft with minimum $ T $ -cut size at least $ k $ contains a $ T $ -join packing of size at least $ (2/3)k-c $ .

=== Discussion / context (OpenProblemGarden) ===
Definitions: A graft consists of a graph $ G=(V,E) $ together with a distinguished set $ T \subseteq V $ of even cardinality. A $ T $ - cut is an edge-cut $ \delta(X) $ of $ G $ with the property that $ |X \cap T| $ is odd. A $ T $ - join is a set $ S \subseteq E $ with the property that a vertex of $ (V,S) $ has odd degree if and only if it is in $ T $ . A $ T $ -join packing is a set of pairwise disjoint T-joins. It is an easy fact that every $ T $ -join and every $ T $ -cut intersect in an odd number of elements. It follows easily from this that the maximum size of a $ T $ -join packing is always less than or equal to the minimum size of a $ T $ -cut. There is a simple example of a graft with $ |T|=4 $ with minimum $ T $ -cut size $ k $ which contains only $ (2/3)k $ disjoint T-joins. The above conjecture asserts that this is essentially the worst case. DeVos and Seymour [DS] have obtained a partial result toward the above conjecture, proving that every graft with minimum $ T $ -cut size $ k $ contains a $ T $ -join packing of size at least the floor of $ (1/3)k $ . Definition: We say that a graft $ G $ is an $ r $ - graph if $ G $ is $ r $ -regular, $ T=V $ , and every $ T $ -cut of G has size at least $ r $ . Conjecture (Rizzi) If $ G $ is an $ r $ -graph, then $ G $ contains a $ T $ -join packing of size at least $ r-2 $ . In an $ r $ -graph, every perfect matching is a $ T $ -join, so the above conjecture is true with room to spare for $ r $ -graphs which are $ r $ -edge-colorable. Indeed, Seymour had earlier conjectured that every $ r $ -graph contains $ r-2 $ disjoint perfect matchings. This however was disproved by Rizzi [R] who constructed for every $ r>2 $ an $ r $ -graph in which every two perfect matchings intersect. Rizzi suggested the above problem as a possible fix for Seymour's conjecture. DeVos and Seymour have proved that every $ r $ -graph has a $ T $ -join packing of size at least the floor of $ r/2 $ . Definition: Let $ G $ be a graph and let $ T $ be the set of vertices of $ G $ of odd degree. A $ T $ -join of $ (G,T) $ is defined to be a postman set . Note that when $ T $ is the set of vertices of odd degree, a cocycle of $ G $ is a $ T $ -cut if and only if it has odd size. Rizzi has shown that the following conjecture is equivalent to the above conjecture in the special case when $ r $ is odd. Conjecture (The packing postman sets conjecture (Rizzi)) If every odd edge-cut of $ G $ has size $ >2k+1 $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. The Petersen graph (or more generally any non $ (2k+1) $ -edge-colorable $ (2k+1) $ -graph) shows that the above conjecture would be false with the weaker assumption that every odd edge-cut has size $ >2k $ . The following conjecture asserts that odd edge-cut size $ >2k $ is enough (for the same conclusion) if we assume in addition that G has no Petersen minor. Conjecture (Conforti, Johnson) If $ G $ has no Petersen minor and every odd edge-cut of $ G $ has size $ >2k $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. Gerard Cornuejols [C] has kindly offered $5000 for a solution to this conjecture. However, it will be tough to find a quick proof since this conjecture does imply the 4-color theorem. Robertson, Seymour, Sanders, and Thomas [RSST] have proved the above conjecture for cubic graphs. Conforti and Johnson [CJ] proved it under the added hypothesis that G has no 4-wheel minor.

=== References listed by OpenProblemGarden ===
- [CJ] M. Conforti and E.L. Johnson, Two min-max theorems for graphs noncontractible to a four wheel, preprint.
- [C] G. Cornuejols, Combinatorial Optimization, packing and covering, SIAM, Philadelphia (2001).
- [R] R. Rizzi, Indecomposable r-Graphs and Some Other Counterexamples, J. Graph Theory 32 (1999) 1-15. MathSciNet
- [RSST] N. Robertson, D.P. Sanders, P.D. Seymour, and R. Thomas, A New Proof of the Four-Color Theorem, Electron. Res. Announc., Am. Math. Soc. 02, no 1 (1996) 17-25.
- [S] P.D. Seymour, Some Unsolved Problems on One-Factorizations of Graphs, in Graph Theory and Related Topics, edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York 1979) 367-368.

=== Catalog page (statement + literature review) ===
Packing T-joins — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The main DeVos conjecture — that every graft with minimum $T$-cut size $k$ admits a $T$-join packing of size at least $(2/3)k - c$ — remains open; the best verified general lower bound is still $\lfloor k/3 \rfloor$ from DeVos–Seymour (pre-posting). Post-2007, Abdi and Guenin proved the packing result for the special class of clutters of odd $T$-joins with at most two terminals in the signed-graft setting, confirming the Cycling Conjecture in that case.

 Cited literature (1)

 
 
 
partial Packing odd $T$-joins with at most two terminals
 (2018)
 

 
 Ahmad Abdi, Bertrand Guenin · Journal of Graph Theory · arXiv:1410.7423 · doi:10.1002/jgt.22178

Proves that a signed graft packs if it is Eulerian and excludes two special non-packing minors, confirming the Cycling Conjecture for odd T-joins with at most two terminals; corollaries include T-join packing with at most four terminals.
 

 

 Reviewer notes. The Abdi–Guenin paper (arXiv:1410.7423, JGT 2018) works in the signed-graft / odd-T-join framework, which is related but not identical to the plain graft T-join packing of the DeVos conjecture; it is cited as a partial result for a special case. The Edwards 2011 McGill thesis ('Optimization and packings of T-joins and T-cuts') contains further planar-graph results but could not be fully read due to PDF encoding issues, so it is not cited. The 2025 paper arXiv:2510.26975 (Kita) concerns grafts with connected minimum joins and does not address the main packing bound. No post-2007 paper found that improves the general floor(k/3) bound toward the conjectured (2/3)k−c.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. There exists a fixed constant $ c $ (probably $ c=1 $ suffices) so that every graft with minimum $ T $ -cut size at least $ k $ contains a $ T $ -join packing of size at least $ (2/3)k-c $ .

Keywords:
packing · T-join

Discussion

Definitions: A graft consists of a graph $ G=(V,E) $ together with a distinguished set $ T \subseteq V $ of even cardinality. A $ T $ - cut is an edge-cut $ \delta(X) $ of $ G $ with the property that $ |X \cap T| $ is odd. A $ T $ - join is a set $ S \subseteq E $ with the property that a vertex of $ (V,S) $ has odd degree if and only if it is in $ T $ . A $ T $ -join packing is a set of pairwise disjoint T-joins. It is an easy fact that every $ T $ -join and every $ T $ -cut intersect in an odd number of elements. It follows easily from this that the maximum size of a $ T $ -join packing is always less than or equal to the minimum size of a $ T $ -cut. There is a simple example of a graft with $ |T|=4 $ with minimum $ T $ -cut size $ k $ which contains only $ (2/3)k $ disjoint T-joins. The above conjecture asserts that this is essentially the worst case. DeVos and Seymour [DS] have obtained a partial result toward the above conjecture, proving that every graft with minimum $ T $ -cut size $ k $ contains a $ T $ -join packing of size at least the floor of $ (1/3)k $ . Definition: We say that a graft $ G $ is an $ r $ - graph if $ G $ is $ r $ -regular, $ T=V $ , and every $ T $ -cut of G has size at least $ r $ . Conjecture (Rizzi) If $ G $ is an $ r $ -graph, then $ G $ contains a $ T $ -join packing of size at least $ r-2 $ . In an $ r $ -graph, every perfect matching is a $ T $ -join, so the above conjecture is true with room to spare for $ r $ -graphs which are $ r $ -edge-colorable. Indeed, Seymour had earlier conjectured that every $ r $ -graph contains $ r-2 $ disjoint perfect matchings. This however was disproved by Rizzi [R] who constructed for every $ r>2 $ an $ r $ -graph in which every two perfect matchings intersect. Rizzi suggested the above problem as a possible fix for Seymour's conjecture. DeVos and Seymour have proved that every $ r $ -graph has a $ T $ -join packing of size at least the floor of $ r/2 $ . Definition: Let $ G $ be a graph and let $ T $ be the set of vertices of $ G $ of odd degree. A $ T $ -join of $ (G,T) $ is defined to be a postman set . Note that when $ T $ is the set of vertices of odd degree, a cocycle of $ G $ is a $ T $ -cut if and only if it has odd size. Rizzi has shown that the following conjecture is equivalent to the above conjecture in the special case when $ r $ is odd. Conjecture (The packing postman sets conjecture (Rizzi)) If every odd edge-cut of $ G $ has size $ >2k+1 $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. The Petersen graph (or more generally any non $ (2k+1) $ -edge-colorable $ (2k+1) $ -graph) shows that the above conjecture would be false with the weaker assumption that every odd edge-cut has size $ >2k $ . The following conjecture asserts that odd edge-cut size $ >2k $ is enough (for the same conclusion) if we assume in addition that G has no Petersen minor. Conjecture (Conforti, Johnson) If $ G $ has no Petersen minor and every odd edge-cut of $ G $ has size $ >2k $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. Gerard Cornuejols [C] has kindly offered $5000 for a solution to this conjecture. However, it will be tough to find a quick proof since this conjecture does imply the 4-color theorem. Robertson, Seymour, Sanders, and Thomas [RSST] have proved the above conjecture for cubic graphs. Conforti and Johnson [CJ] proved it under the added hypothesis that G has no 4-wheel minor.

Bibliography

 [CJ]
 M. Conforti and E.L. Johnson, Two min-max theorems for graphs noncontractible to a four wheel, preprint.

 [C]
 G. Cornuejols, Combinatorial Optimization, packing and covering, SIAM, Philadelphia (2001).

 [R]
 R. Rizzi, Indecomposable r-Graphs and Some Other Counterexamples, J. Graph Theory 32 (1999) 1-15. MathSciNet
 MathSciNet

 [RSST]
 N. Robertson, D.P. Sanders, P.D. Seymour, and R. Thomas, A New Proof of the Four-Color Theorem, Electron. Res. Announc., Am. Math. Soc. 02, no 1 (1996) 17-25.

 [S]
 P.D. Seymour, Some Unsolved Problems on One-Factorizations of Graphs, in Graph Theory and Related Topics, edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York 1979) 367-368.

Related conjectures

 
 related to
 Seymour's r-graph conjecture
 solved
 The mention says Seymour's r-graph conjecture 'is also closely related to Rizzi's packing postman sets conjecture (see packing T-joins)'. The target page's headline conjecture is about general grafts ((2/3)k - c disjoint T-joins), which Seymour's conjecture (chi' <= r+1 for r-graphs) cannot imply: it concerns arbitrary grafts, not r-regular graphs with T=V. Even for Rizzi's r-graph subcase (r-2 disjoint T-joins), an (r+1)-edge-coloring yields matchings that need not be perfect, hence not T-joins, so no direct implication follows; the pages assert closeness 'in nature' only. Both live in the same circle of ideas (Goldberg, r-graphs, matching/T-join decompositions) without a proven implication either way.
 

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
  "one_line": "An exact formula yields the sharp bound floor((2k+1)/3) for four-terminal grafts with independent nonterminals, but does not resolve the general conjecture.",
  "would_publish": false,
  "caveats": "Restricted special case; no claim of novelty or improvement of the general bound."
}
```

# 1. A sharp special case

Write
\[
\lambda(G,T)=\min\{|\delta(X)|:|X\cap T|\text{ is odd}\}
\]
and let \(\nu(G,T)\) be the maximum number of pairwise edge-disjoint \(T\)-joins.

I obtain an exact solution for the following class. The proof is self-contained; I do not claim that this special case is new.

**Theorem.** Let \(G\) be a finite loopless multigraph, let
\[
T=\{t_1,t_2,t_3,t_4\},
\]
and suppose \(V(G)\setminus T\) is independent. Then
\[
\boxed{\displaystyle
\nu(G,T)\ge
\left\lfloor\frac{2\lambda(G,T)+1}{3}\right\rfloor .}
\tag{1}
\]
For every positive integer value of \(\lambda\), equality is attained by a simple bipartite graph in this class.

Thus the conjectured inequality holds in this class with \(c=1/3\), and that constant is best possible **within this class**. An exact formula for \(\nu\) is proved below.

Subdividing an edge with a new nonterminal preserves both \(\lambda\) and \(\nu\): a join must use both subdivision edges or neither, and minimum cuts have the same value. Consequently, the theorem also covers subdivisions of graphs in the stated class.

## A four-vertex lemma

**Lemma 1.** If \(H\) is a loopless multigraph on four vertices and \(T=V(H)\), then
\[
\nu(H,T)=\delta(H).
\]

**Proof.** The upper bound follows from the four singleton \(T\)-cuts. For the lower bound, prove by induction on \(d\) that minimum degree at least \(d\) guarantees \(d\) disjoint \(T\)-joins.

If \(H\) has a perfect matching, delete it and apply induction.

Otherwise, if \(d>0\), the underlying simple graph is a spanning star. Indeed, a graph on four vertices with no isolated vertex and no perfect matching must be a star: after choosing an edge \(ab\), the other two vertices cannot be adjacent, and the absence of a perfect matching forces both to have the same sole neighbour among \(a,b\).

Choose one edge to each leaf. These three edges form a \(T\)-join. Each leaf loses one incident edge. The centre originally has degree at least \(3d\), so afterward its degree is at least
\[
3d-3\ge d-1.
\]
Induction completes the proof. \(\square\)

We will also use the following elementary pairing fact.

**Lemma 2.** Suppose objects of four types have multiplicities \(b_1,\ldots,b_4\). They can be partitioned into pairs of different types if and only if
\[
\sum_i b_i\text{ is even},
\qquad
b_i\le \sum_{j\ne i}b_j\quad\text{for every }i.
\]

**Proof.** Necessity is immediate. For sufficiency, repeatedly pair objects from the two currently largest nonempty types. If the current total is \(2s\) and every multiplicity is at most \(s\), then after this operation every multiplicity is at most \(s-1\). Induction applies. \(\square\)

# 2. An exact formula

Put \(N=V(G)\setminus T\). For \(v\in N\), define
\[
a_{vi}=|E(v,t_i)|,\qquad d_v=\sum_{i=1}^4 a_{vi},
\]
and
\[
b_{vi}=\min\{a_{vi},d_v-a_{vi}\}.
\]
Let \(d_i^0\) be the degree of \(t_i\) in \(G[T]\), and set
\[
u_i=d_i^0+\sum_{v\in N}b_{vi},
\qquad
S=\sum_{i=1}^4u_i.
\]

Call a nonterminal \(v\) **defective** if
\[
d_v\text{ is odd}
\quad\text{and}\quad
2a_{vi}<d_v\quad\text{for every }i.
\]
Let \(D\) be the set of defective vertices, and write
\[
h=|D|,
\qquad
h_i=|\{v\in D:a_{vi}=0\}|.
\]
Every defective vertex has at least three distinct terminal neighbours.

**Proposition.** Under the hypotheses of the theorem,
\[
\lambda(G,T)=\min_i u_i
\tag{2}
\]
and
\[
\boxed{\displaystyle
\nu(G,T)=
\min\left\{
\min_i u_i,\;
\left\lfloor\frac{S-h}{4}\right\rfloor,\;
\min_i\left\lfloor\frac{S-u_i-h_i}{3}\right\rfloor
\right\}.}
\tag{3}
\]

For simple graphs, the defective vertices are exactly the degree-three nonterminals. Formula (3) therefore has particularly simple data in that case.

## 2.1. Computing the minimum \(T\)-cut

A \(T\)-cut has either one or three terminals on one side. Complementing the shore, it suffices to consider cuts with
\[
X\cap T=\{t_i\}.
\]

Since \(N\) is independent, each \(v\in N\) can independently be placed inside or outside \(X\). Its contribution is respectively \(d_v-a_{vi}\) or \(a_{vi}\), with minimum \(b_{vi}\). Hence the minimum such cut has size \(u_i\), proving (2).

## 2.2. Local pairings at nonterminals

The vectors \(b_v=(b_{v1},\ldots,b_{v4})\) have the following useful properties.

* If some \(a_{vi}>d_v/2\), this index is unique, and
  \[
  b_{vi}=\sum_{j\ne i}a_{vj},\qquad b_{vj}=a_{vj}\quad(j\ne i).
  \]
  Thus \(b_v\) has even total and satisfies Lemma 2.

* If no \(a_{vi}>d_v/2\) and \(d_v\) is even, then \(b_v=a_v\), again satisfying Lemma 2.

* If \(v\) is defective, then \(b_v=a_v\). For **any** terminal neighbour \(t_i\), the vector
  \[
  b_v-\mathbf e_i
  \]
  has even total \(d_v-1\), and every entry is at most \((d_v-1)/2\). It therefore satisfies Lemma 2.

Consequently, at a nondefective vertex we can retain and pair arms with terminal multiplicities \(b_v\). At a defective vertex we can do the same after choosing one terminal neighbour at which to lose one arm.

Replace each pair of arms by an auxiliary edge between its two distinct terminals. Together with \(G[T]\), these edges form a multigraph \(H\) on the four terminals.

If \(\ell_i\) defective vertices choose to lose an arm at \(t_i\), then
\[
d_H(t_i)=u_i-\ell_i.
\tag{4}
\]
Every \(T\)-join packing in \(H\) lifts to one in \(G\): replace each auxiliary edge by its two-edge path. The paths use distinct original edges, and every nonterminal receives even degree.

## 2.3. Choosing where to lose the arms

Fix an integer \(q\ge0\). We want to assign each defective vertex \(v\) to one of its terminal neighbours, with at most
\[
u_i-q
\]
vertices assigned to \(t_i\).

This is a capacitated bipartite matching problem. Hall's condition says that, for every \(U\subseteq T\),
\[
|\{v\in D:N_G(v)\subseteq U\}|
\le \sum_{t_i\in U}(u_i-q).
\tag{5}
\]
Here the capacities must also be nonnegative.

Because every defective vertex has at least three terminal neighbours, only sets \(U\) of size three or four can give nontrivial conditions. Thus the complete list is
\[
q\le u_i\quad(1\le i\le4),
\tag{6}
\]
\[
h\le S-4q,
\tag{7}
\]
and
\[
h_i\le S-u_i-3q\quad(1\le i\le4).
\tag{8}
\]

Whenever these inequalities hold, the resulting \(H\) has minimum degree at least \(q\). Lemma 1 and lifting then produce \(q\) disjoint \(T\)-joins in \(G\). This proves the lower bound in (3).

## 2.4. Why every packing satisfies the same conditions

Let \(J_1,\ldots,J_p\) be disjoint \(T\)-joins.

Within each \(J_r\), delete pairs of parallel edges joining a nonterminal to the same terminal until at most one such edge remains. Each deletion changes two vertex degrees by two, so all joins remain \(T\)-joins and remain disjoint.

Let \(c_{vi}\) count the remaining used edges between \(v\) and \(t_i\), over all joins. Since each join has even degree at \(v\) and at most one edge there to each terminal,
\[
c_{vi}\le\sum_{j\ne i}c_{vj}.
\]
Together with the edge capacities, this gives
\[
c_{vi}\le \min\{a_{vi},d_v-a_{vi}\}=b_{vi}.
\tag{9}
\]

If \(v\) is defective, the total number of used arms at \(v\) is even, whereas \(d_v\) is odd. Some arm is therefore unused. Choose a terminal neighbour \(\sigma(v)\) with such an unused arm. Then
\[
c_{vi}\le b_{vi}-\mathbf 1_{\{\sigma(v)=i\}}.
\tag{10}
\]

Each of the \(p\) joins has positive odd degree at every terminal. Hence, writing \(\ell_i=|\sigma^{-1}(i)|\),
\[
p
\le \sum_{r=1}^p d_{J_r}(t_i)
\le d_i^0+\sum_v c_{vi}
\le u_i-\ell_i.
\]
Thus the choices \(\sigma(v)\) provide an assignment with capacities \(u_i-p\). Conditions (6)–(8) must hold for \(q=p\). This proves the reverse inequality in (3). \(\square\)

The proof is constructive: a capacitated matching, local pairings, and the decomposition in Lemma 1 find an optimal packing.

# 3. Deriving the sharp \(2/3\) bound

Let
\[
\lambda=\min_i u_i,
\qquad
q=\left\lfloor\frac{2\lambda+1}{3}\right\rfloor.
\]
We verify that all terms in (3) are at least \(q\).

## 3.1. The total-capacity term

Each defective vertex contributes at least three to \(S\), so
\[
3h\le S.
\tag{11}
\]
Also,
\[
S-h\quad\text{is even}.
\tag{12}
\]
Indeed, terminal-terminal edges contribute an even total to \(S\); every nondefective \(b_v\) has even total; and every defective \(b_v\) has odd total.

Therefore the integer \(L=(S-h)/2\) satisfies
\[
L\ge \frac S3\ge\frac{4\lambda}{3}.
\]
It follows that
\[
\left\lfloor\frac{S-h}{4}\right\rfloor
=\left\lfloor\frac L2\right\rfloor
\ge
\left\lfloor\frac{\lceil4\lambda/3\rceil}{2}\right\rfloor
=
\left\lfloor\frac{2\lambda+1}{3}\right\rfloor.
\tag{13}
\]
The last equality follows by considering \(\lambda\bmod3\).

## 3.2. The three-terminal terms

Every vector \(b_v\) satisfies
\[
b_{vi}\le\sum_{j\ne i}b_{vj}.
\]
A defective vertex missing \(t_i\) contributes at least three to
\[
\sum_{j\ne i}b_{vj}-b_{vi}.
\]
Terminal-terminal edges also contribute nonnegatively to the analogous difference. Consequently,
\[
S-2u_i\ge3h_i.
\tag{14}
\]

Writing \(A_i=S-u_i=\sum_{j\ne i}u_j\), we get
\[
\frac{S-u_i-h_i}{3}
\ge \frac{2A_i+u_i}{9}
\ge \frac{7\lambda}{9}.
\tag{15}
\]
For \(\lambda\ge3\),
\[
\frac{7\lambda}{9}\ge\frac{2\lambda+1}{3}\ge q.
\]
Also \(u_i\ge\lambda\ge q\). Formula (3) now proves (1).

For \(\lambda=0\), the assertion is trivial. For \(\lambda=1,2\), its right-hand side is one. Positive minimum \(T\)-cut size ensures that every component meets \(T\) evenly, which guarantees a \(T\)-join: in a rooted spanning tree of each component, include a parent edge precisely when its descendant subtree contains an odd number of terminals. This covers the remaining cases. \(\square\)

A further consequence of (3) is worth recording:

**Corollary.** If there are no defective vertices, then
\[
\nu(G,T)=\lambda(G,T).
\]
In particular, this holds in the stated class whenever every nonterminal has even degree.

# 4. Sharp examples for every minimum cut value

For nonnegative integers \(a_1,a_2,a_3,a_4\), construct a simple bipartite graph as follows:

* one side is \(T=\{t_1,t_2,t_3,t_4\}\);
* for each \(i\), add \(a_i\) nonterminals adjacent to exactly \(T\setminus\{t_i\}\).

Put \(A=\sum_i a_i\). All nonterminals are defective, and
\[
u_i=A-a_i,\qquad S=3A,\qquad h=A,\qquad h_i=a_i.
\]
Thus (2)–(3) give
\[
\boxed{\displaystyle
\lambda=A-\max_i a_i,\qquad
\nu=\min\left\{A-\max_i a_i,\left\lfloor\frac A2\right\rfloor\right\}.}
\tag{16}
\]

The packing obstruction has a direct interpretation. A degree-three nonterminal can be used by at most one join in a packing, because every join uses an even number of its incident edges. Every join needs at least two nonterminals to give all four terminals odd degree. Therefore \(\nu\le\lfloor A/2\rfloor\).

The following choices attain (1) for every positive \(\lambda\):
\[
\begin{array}{c|c|c}
\lambda &(a_1,a_2,a_3,a_4)&\nu\\ \hline
3r &(r,r,r,r)&2r\\
3r+1 &(r+1,r+1,r,r)&2r+1\\
3r+2 &(r+1,r+1,r+1,r)&2r+1.
\end{array}
\]
In particular, \(a_i=r\) gives
\[
\lambda=3r,\qquad \nu=2r,
\]
while the last row shows that \(c<1/3\) is impossible for this subclass.

# 5. For the general conjecture, \(c\ge1\) is necessary

The better additive constant above cannot extend to all grafts. The Petersen graph gives a short, fully checkable obstruction.

Use vertices \(a_i,b_i\), indexed modulo five, and edges
\[
a_i a_{i+1},\qquad b_i b_{i+2},\qquad a_i b_i,
\]
and take \(T=V(G)\).

The graph is cubic and bridgeless. Every odd-vertex cut therefore has odd size at least three, and singleton cuts have size three. Hence
\[
\lambda(G,T)=3.
\]

If there were two disjoint \(T\)-joins, each would have degree one at every vertex: two positive odd degrees must sum to at most three. Thus they would be disjoint perfect matchings.

The Petersen graph has no two disjoint perfect matchings, as follows directly from its construction. A perfect matching has an odd number of spokes \(a_i b_i\). It cannot have three: the two indices without spokes would have to be adjacent both in the outer cycle and in the inner cycle, requiring their difference to be both \(\pm1\) and \(\pm2\) modulo five. Thus it has one or five spokes.

There is one matching with five spokes, and exactly one for each choice of a single spoke. The five-spoke matching meets all the others. Among single-spoke matchings, choices at cyclic distance one share an inner edge, while choices at distance two share an outer edge. For example, choices \(0,1\) share \(b_2b_4\), and choices \(0,2\) share \(a_3a_4\); rotation and reflection cover all pairs.

Consequently,
\[
\nu(G,T)=1.
\]
Any universal inequality
\[
\nu(G,T)\ge \frac23\lambda(G,T)-c
\]
must therefore have
\[
\boxed{c\ge1.}
\]
So the proposed value \(c=1\), if valid, is best possible.

# 6. What remains unresolved

The exact formula depends essentially on two restrictions:

1. **Independent nonterminals.** Their arms can be paired independently, and minimum \(T\)-cuts are computed by four sums of local contributions. General nonterminal components couple these decisions.
2. **Exactly four terminals.** Lemma 1 makes minimum degree sufficient for packing joins in the auxiliary graph. This is false for larger terminal sets; the Petersen example already demonstrates that failure.

No extension of either step to arbitrary grafts is established here. In particular, this argument does **not** improve the general \(\lfloor k/3\rfloor\) guarantee stated in the question.

The partial result determines the exact packing number in an extremal subclass and identifies the one-unused-arm loss at cubic nonterminals as its \(2/3\) obstruction. It does not prove the uniform conjecture.
