Attack the following open graph-theory problem.

Catalog id: colouring_the_square_of_a_planar_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/colouring_the_square_of_a_planar_graph/
Original entry: http://www.openproblemgarden.org/op/colouring_the_square_of_a_planar_graph
Problem attributed to: Wegner (posted 2013-03-13)

=== Problem statement (OpenProblemGarden) ===
Title: Colouring the square of a planar graph
Conjecture Let $ G $ be a planar graph of maximum degree $ \Delta $ . The chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ .

=== Discussion / context (OpenProblemGarden) ===
The square of a graph $ G $ is the graph $ G^2 $ on the same set of vertices, in which two vertices are adjacent when their distance in $ G $ is at most 2. Wegner [W] also gave examples showing that these bounds would be tight. For $ \Delta\geq 8 $ , they are the following. For $ 4\leq \Delta \leq 9 $ , the examples are planar graphs on $ \Delta+5 $ with maximum degree $ \Delta $ whose square is a complete graph. This conjecture has also been generalized to the list chromatic number . Conjecture Let $ G $ be a planar graph of maximum degree $ \Delta $ . The list chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ . Cranston and Kim [CK] showed that the square of every connected graph (non necessarily planar) which is subcubic (i.e., with $ \Delta\le3 $ ) is 8-choosable, except for the Petersen graph. However, the 7-choosability of the square of subcubic planar graphs is still open. Havet et al. [HHMR] proved the conjecture asymptotically: Theorem The square of every planar graph $ G $ of maximum degree $ \Delta $ has list chromatic number at most $ (1+o(1))\,\frac32\,\Delta $ . In fact, they proved this results for more general classes of graph. This led them to pose the following problem. Problem Is it true that for every minor-closed family $ {\cal F} $ of graphs (with $ {\cal F} $ not the set of all graphs), we have $ \chi(G^2)\le \bigl(\frac32+o(1)\bigr) \Delta(G) $ for all $ G\in{\cal F} $ ?

=== References listed by OpenProblemGarden ===
- [HHMR] F. Havet, J. van den Heuvel, C. McDiarmid, and B. Reed. List Colouring Squares of Planar Graphs. Research Report RR-6586, INRIA, July 2008.
- [CK] D. W. Cranston and S.-J. Kim. List-coloring the square of a subcubic graph, J. Graph Theory, 57(1):65--87, 2008.
- *[W] G. Wegner. Graphs with given diameter and a coloring problem. Technical report, 1977.

=== Catalog page (statement + literature review) ===
Colouring the square of a planar graph — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Significant partial progress has been made since the 2013 OPG posting. The $\Delta=3$ case of Wegner's conjecture ($\chi(G^2)\le 7$) has been fully proved — independently by Hartke, Jahanbekam, and Thomas (2016) and by Thomassen (2018). For larger $\Delta$ the conjecture remains open: improved general upper bounds such as $2\Delta+7$ (for $\Delta\ge 6$) and $3\Delta+4$ have been established, and the clique bound $\omega(G^2)\le\lfloor\frac{3}{2}\Delta\rfloor+1$ has been verified for $\Delta\ge 36$, but the full conjecture (all three cases) is still unresolved.

 Cited literature (8)

 
 
 
proof The chromatic number of the square of subcubic planar graphs
 (2016)
 

 
 Stephen G. Hartke, Sogol Jahanbekam, Brent Thomas · arXiv preprint · arXiv:1604.06504

Proves Wegner's conjecture for $\Delta=3$: the square of every subcubic planar graph is 7-colorable, using the discharging method and computational verification of reducible configurations.
 

 
 
proof The square of a planar cubic graph is 7-colorable
 (2018)
 

 
 Carsten Thomassen · Journal of Combinatorial Theory, Series B · doi:10.1016/j.jctb.2017.08.010

Independent proof of Wegner's conjecture for $\Delta=3$ (cubic planar graphs): $\chi(G^2)\le 7$; published in JCTB 128 (2018) 192–218.
 

 
 
partial Coloring squares of planar graphs with small maximum degree
 (2021)
 

 
 Mateusz Krzyżyński, Paweł Rzążewski, Szymon Tur · arXiv preprint · arXiv:2105.11235

Proves $\chi(G^2)\le 3\Delta+4$ for every planar graph $G$, giving the best-known bound for $6\le\Delta\le 14$.
 

 
 
partial Improved square coloring of planar graphs
 (2021)
 

 
 Nicolas Bousquet, Quentin Deschamps, Lucas de Meyer, Théo Pierron · arXiv preprint · arXiv:2112.12512

Shows that $2\Delta+7$ colors suffice to square-color any planar graph, improving the best-known bounds for $6\le\Delta\le 31$.
 

 
 
partial Relaxation of Wegner's Planar Graph Conjecture for maximum degree 4
 (2022)
 

 
 Eun-Kyung Cho, Ilkyoo Choi, Bernard Lidický · arXiv preprint · arXiv:2212.10643

Shows that a relaxation of $G^2$-coloring for planar $G$ with $\Delta=4$ is achievable with 9 colors (the conjectured bound), by allowing at most one repeated color in neighborhoods of degree-4 vertices.
 

 
 
partial The square of every subcubic planar graph of girth at least 6 is 7-choosable
 (2023)
 

 
 Seog-Jin Kim, Xiaopan Lian · arXiv preprint · arXiv:2305.05194

Proves the list-chromatic version of Wegner's conjecture ($\chi_\ell(G^2)\le 7$) for subcubic planar graphs of girth at least 6.
 

 
 
partial Bounding Clique Size in Squares of Planar Graphs
 (2023)
 

 
 Daniel W. Cranston · European Journal of Combinatorics · arXiv:2308.09585

Proves that $\omega(G^2)\le\lfloor\frac{3}{2}\Delta(G)\rfloor+1$ for plane graphs with $\Delta(G)\ge 36$, confirming the clique-number analogue of Wegner's conjecture for large degree.
 

 
 
partial Squares of subcubic planar graphs without cycles of length 4-8 are 6-choosable
 (2025)
 

 
 Seog-Jin Kim, Rong Luo · arXiv preprint · arXiv:2512.10175

Shows $\chi_\ell(G^2)\le 6$ for subcubic planar graphs containing no cycles of length 4 through 8, improving the 7-choosable bound under additional girth/cycle restrictions.
 

 

 Reviewer notes. The Thomassen 2018 paper (doi:10.1016/j.jctb.2017.08.010) was verified via Wikidata and DTU Orbit since ScienceDirect returned HTTP 403. The Hartke–Jahanbekam–Thomas paper (arXiv:1604.06504) appears to remain a preprint (not yet found in a peer-reviewed journal page that was accessible). The Δ=4 case of the original conjecture (χ(G²)≤9) remains open with best known upper bound of 12. The list-chromatic version of the conjecture for subcubic planar graphs (7-choosability without girth restriction) also remains open. The paper on Δ=5 square coloring (Graphs and Combinatorics 2023, doi:10.1007/s00373-023-02615-1) was found in search but could not be fetched due to authentication redirect and was therefore not included.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 166s.
 

Conjecture. Let $ G $ be a planar graph of maximum degree $ \Delta $ . The chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ .

Discussion

The square of a graph $ G $ is the graph $ G^2 $ on the same set of vertices, in which two vertices are adjacent when their distance in $ G $ is at most 2. Wegner [W] also gave examples showing that these bounds would be tight. For $ \Delta\geq 8 $ , they are the following. For $ 4\leq \Delta \leq 9 $ , the examples are planar graphs on $ \Delta+5 $ with maximum degree $ \Delta $ whose square is a complete graph. This conjecture has also been generalized to the list chromatic number . Conjecture Let $ G $ be a planar graph of maximum degree $ \Delta $ . The list chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ . Cranston and Kim [CK] showed that the square of every connected graph (non necessarily planar) which is subcubic (i.e., with $ \Delta\le3 $ ) is 8-choosable, except for the Petersen graph. However, the 7-choosability of the square of subcubic planar graphs is still open. Havet et al. [HHMR] proved the conjecture asymptotically: Theorem The square of every planar graph $ G $ of maximum degree $ \Delta $ has list chromatic number at most $ (1+o(1))\,\frac32\,\Delta $ . In fact, they proved this results for more general classes of graph. This led them to pose the following problem. Problem Is it true that for every minor-closed family $ {\cal F} $ of graphs (with $ {\cal F} $ not the set of all graphs), we have $ \chi(G^2)\le \bigl(\frac32+o(1)\bigr) \Delta(G) $ for all $ G\in{\cal F} $ ?

Bibliography

 [HHMR]
 F. Havet, J. van den Heuvel, C. McDiarmid, and B. Reed. List Colouring Squares of Planar Graphs . Research Report RR-6586, INRIA, July 2008.
 List Colouring Squares of Planar Graphs

 [CK]
 D. W. Cranston and S.-J. Kim. List-coloring the square of a subcubic graph, J. Graph Theory, 57(1):65--87, 2008.

★ [W]
 G. Wegner. Graphs with given diameter and a coloring problem. Technical report, 1977.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured list bounds for planar graphs with vertex cover at most four, and disprove the separately stated minor-closed extension as worded.",
  "would_publish": false,
  "caveats": "The unrestricted planar conjecture is not resolved; the auxiliary counterexample is nonplanar, and novelty of the restricted-class result is not claimed."
}
```

# 1. Results and scope

Write
\[
W(D)=
\begin{cases}
7,&D=3,\\
D+5,&4\le D\le7,\\
\lfloor 3D/2\rfloor+1,&D\ge8.
\end{cases}
\]

I prove the following restricted version, including list colouring.

**Theorem 1.** Let \(D\ge3\). If \(G\) is a finite simple planar graph of maximum degree at most \(D\), and \(G\) has a vertex cover of size at most four, then
\[
\chi_\ell(G^2)\le W(D).
\]

Here a vertex cover is a set meeting every edge. The large-degree bound in Theorem 1 is sharp within this class.

There is also an extension to graphs with arbitrarily large vertex-cover number.

**Corollary 2.** Wegner’s ordinary colouring bounds hold for every planar graph in which each block has a vertex cover of size at most four.

The list-colouring assertion is not claimed for the block extension.

Finally, the auxiliary assertion about **every proper minor-closed family**, literally as stated in the question, is false: I give \(K_5\)-minor-free graphs \(X_r\) satisfying
\[
\chi(X_r^2)=\chi_\ell(X_r^2)=\frac53\Delta(X_r),
\qquad \Delta(X_r)\longrightarrow\infty.
\]
This is not a counterexample to the planar conjecture.

I make no claim that these restricted-class observations are new.

# 2. A list-colouring certificate

The following elementary lemma is useful because it converts a matching of nonedges into a list-colouring bound.

**Lemma 3.** If a graph \(H\) has \(n\) vertices and its complement contains a matching of size \(r\), then
\[
\chi_\ell(H)\le n-r.
\]

**Proof.** Add edges to \(H\) until the only nonedges are the \(r\) matched pairs. The resulting graph is complete multipartite, with \(k=n-r\) parts, each of size one or two. It suffices to prove that such a graph is \(k\)-choosable.

Proceed by induction on \(k\). If the lists of the two vertices in some two-vertex part share a colour, give both that colour, delete their part, and delete that colour from all remaining lists. Induction applies.

Otherwise the two lists in every two-vertex part are disjoint. Hall’s condition holds for the family of vertex lists: a set of at most \(k\) vertices has at least \(k\) colours in its union; a larger set contains both vertices of some part, whose disjoint lists together contain at least \(2k\) colours. There are at most \(2k\) vertices altogether. Thus distinct representatives give a proper list colouring. ∎

# 3. Proof of Theorem 1

## 3.1. Reduction and notation

Graphs on fewer than four vertices are immediate. Otherwise enlarge a vertex cover, if necessary, to
\[
C=\{1,2,3,4\}.
\]
Consequently \(V(G)\setminus C\) is independent.

Delete all vertices outside \(C\) having degree at most one, obtaining \(G_0\). Such a deleted vertex cannot be internal to a path of length two between retained vertices, so
\[
G_0^2=G^2[V(G_0)].
\]
A deleted leaf has at most \(D\) neighbours in \(G^2\). Since \(W(D)\ge D+1\), every \(W(D)\)-list colouring of \(G_0^2\) extends greedily to the deleted vertices.

It therefore suffices to colour \(G_0^2\). Put
\[
U=V(G_0)\setminus C.
\]
Every vertex of \(U\) has two, three, or four neighbours, all in \(C\).

Use the following notation:

- \(F=G_0[C]\), and \(f_i=d_F(i)\);
- \(d_i=d_{G_0}(i)\le D\);
- \(x_{ij}\) is the number of vertices of \(U\) with neighbourhood \(\{i,j\}\);
- \(t_i\) is the number with neighbourhood \(C\setminus\{i\}\);
- \(z\) is the number with neighbourhood \(C\);
- \(p=t_1+t_2+t_3+t_4+z\).

Planarity gives
\[
t_i\le2 \qquad(i=1,2,3,4),                         \tag{1}
\]
because three vertices counted by \(t_i\), together with \(C\setminus\{i\}\), would form a \(K_{3,3}\).

Two vertices of \(U\) are adjacent in \(G_0^2\) precisely when their neighbourhoods intersect. Thus nonedges within \(U\) occur exactly between opposite pair-types:
\[
(12,34),\qquad(13,24),\qquad(14,23).
\]
Choose a matching \(M_0\) of these nonedges of size
\[
r_0=\min(x_{12},x_{34})+
    \min(x_{13},x_{24})+
    \min(x_{14},x_{23}).
\]
Define
\[
q=p+\max(x_{12},x_{34})+
       \max(x_{13},x_{24})+
       \max(x_{14},x_{23}).
\]
Then
\[
|V(G_0)|=q+r_0+4.
\]

All \(p\) vertices of degree three or four are unmatched by \(M_0\). If we can add \(s\) disjoint nonedges between cover vertices and currently unmatched vertices of \(U\), Lemma 3 gives
\[
\chi_\ell(G_0^2)\le q+4-s.                         \tag{2}
\]

For later use, if \(u\in U\) has neighbourhood \(S\subseteq C\), then \(i\in C\) is nonadjacent to \(u\) in \(G_0^2\) exactly when
\[
i\notin S
\quad\text{and}\quad
N_F(i)\cap S=\varnothing.                         \tag{3}
\]

## 3.2. The star–triangle alternative

From each opposite pair of pair-types choose one attaining the maximum in the definition of \(q\). The three chosen edges of the abstract \(K_4\) are pairwise intersecting, so they form either a star or a triangle.

For any \(i\in C\), define its star weight
\[
q_i=p+\sum_{j\ne i}x_{ij}.
\]
Counting neighbours of \(i\) gives
\[
q_i=d_i-f_i+t_i\le D+2.                           \tag{4}
\]

If the chosen types form a star centred at \(i\), then \(q=q_i\). Moreover, equality \(q=D+2\) forces
\[
d_i=D,\qquad f_i=0,\qquad t_i=2.                 \tag{5}
\]
In that situation, \(i\) can be matched to an unmatched vertex counted by \(t_i\), using (3).

Now suppose the chosen types form a triangle, relabelled as \(T=\{1,2,3\}\). Then
\[
q=p+x_{12}+x_{13}+x_{23}.
\]
For \(i\in T\), let \(\{j,k\}=T\setminus\{i\}\), and put
\[
a_i=x_{jk}-x_{i4}\ge0.
\]
Exactly \(a_i\) vertices of type \(\{j,k\}\) remain unmatched by \(M_0\). Also,
\[
a_i=q-q_i=q-d_i+f_i-t_i
       \ge q-D+f_i-t_i.                           \tag{6}
\]

Let
\[
m=|E(F[T])|,
\qquad
g=|E_F(\{4\},T)|.
\]
A degree count gives
\[
d_1+d_2+d_3
=
2q+(x_{14}+x_{24}+x_{34})+t_4+z+2m+g.
\]
Consequently
\[
q\le\lfloor3D/2\rfloor,
\qquad
2m+g\le3D-2q.                                    \tag{7}
\]

The following ways to enlarge \(M_0\) follow directly from (3):

- If \(i\in T\) is isolated in \(F[T]\) and \(a_i>0\), match \(i\) to a free vertex of type \(T\setminus\{i\}\).
- If \(f_i=0\) and \(t_i>0\), match \(i\) to a free vertex counted by \(t_i\).
- If \(g\le1\), vertex \(4\) has an eligible triangle pair-type: any pair in \(T\) avoiding its possible neighbour in \(F\).

We now cover all degree ranges.

## 3.3. The case \(D\ge8\)

Set
\[
Q=\lfloor3D/2\rfloor,\qquad k=Q+1.
\]

### Star case

If \(D\ge10\), then
\[
q+4\le D+6\le Q+1=k,
\]
so no enlargement of \(M_0\) is needed.

If \(D=8\) or \(9\), then \(k=D+5\). Again no enlargement is needed unless \(q=D+2\). In that event (5) supplies one additional matching edge, and (2) gives
\[
\chi_\ell(G_0^2)\le q+3=D+5=k.
\]

### Triangle case

Write
\[
\delta=Q-q\ge0.
\]
If \(\delta\ge3\), then \(q+4\le k\). Hence assume \(\delta\in\{0,1,2\}\). We need \(3-\delta\) additional matching edges.

Equations (1), (6), and (7) imply
\[
a_i\ge \lfloor D/2\rfloor-\delta-2+f_i
       \ge2-\delta+f_i,                           \tag{8}
\]
and
\[
2m+g\le2\delta+1.                                 \tag{9}
\]

**If \(\delta=0\):** Equation (9) gives \(m=0\), and (8) gives \(a_i\ge2\) for all \(i\in T\). Match each of the three vertices \(i\in T\) to a free vertex of its opposite triangle type. These are three disjoint additional matching edges.

**If \(\delta=1\):** Here \(m\le1\), and every \(a_i\ge1+f_i\).

If \(m=0\), match any two vertices of \(T\) to their respective opposite types.

Suppose \(m=1\), and let \(i\) be the isolated vertex of \(F[T]\). Equation (9) gives \(g\le1\). We match both \(i\) and \(4\) to eligible free triangle-type vertices. If their chosen types are different, the positive \(a_j\)'s suffice. The only forced coincidence occurs when \(g=1\) and the edge from \(4\) goes to \(i\). Then \(f_i=1\), so (8) gives \(a_i\ge2\), allowing two distinct free vertices of the same type.

Thus two additional matching edges exist.

**If \(\delta=2\):** Now \(m\le2\).

If \(m\le1\), choose an isolated vertex \(i\) of \(F[T]\). If \(a_i>0\), use its opposite pair-type. If \(a_i=0\), then (6) and \(q-D\ge2\) give
\[
0\ge2+f_i-t_i.
\]
Together with \(t_i\le2\), this forces \(f_i=0\) and \(t_i=2\). A vertex counted by \(t_i\) supplies the required matching edge.

If \(m=2\), every vertex of \(T\) has \(f_i\ge1\), so (8) gives \(a_i\ge1\) for all \(i\in T\). Also (9) gives \(g\le1\). Match vertex \(4\) to a free vertex of an eligible triangle type.

In all three subcases, (2) gives
\[
\chi_\ell(G_0^2)\le q+4-(3-\delta)=Q+1.
\]

## 3.4. The cases \(4\le D\le7\)

Here \(k=D+5\). If \(q\le D+1\), no extra matching edge is needed.

In the star case, the only remaining possibility is \(q=D+2\). Equation (5) supplies one additional edge, giving \(q+3=k\).

In the triangle case, (7) shows that the remaining possibilities are
\[
q=D+2\quad\text{or}\quad q=D+3.
\]

If \(q=D+2\), then
\[
2m+g\le D-4\le3,
\]
so \(F[T]\) has an isolated vertex \(i\). Equation (6) gives
\[
a_i\ge2+f_i-t_i.
\]
If \(a_i>0\), use the opposite pair-type. Otherwise \(f_i=0,t_i=2\), and use a triple-type vertex. One additional edge gives \(q+3=D+5\).

If \(q=D+3\), necessarily \(D\in\{6,7\}\), and
\[
2m+g\le D-6\le1.
\]
Thus \(m=0\). Moreover,
\[
a_i\ge3+f_i-t_i\ge1.
\]
Match two vertices of \(T\) to their distinct opposite types. Equation (2) gives
\[
\chi_\ell(G_0^2)\le q+2=D+5.
\]

## 3.5. The case \(D=3\)

We need one additional planar observation.

**Claim.** If \(t_i=2\), then \(d_i\le2\).

To prove it, let \(x,y\in U\) both have neighbourhood \(J=C\setminus\{i\}\). Each vertex of \(J\) has at most one incident edge other than its edges to \(x,y\).

Suppose \(d_i=3\). Each neighbour of \(i\) either belongs to \(J\), or is a vertex of \(U\) having a further neighbour in \(J\). These produce three paths of length one or two from \(i\) to \(J\). Their endpoints must be distinct: otherwise some vertex of \(J\) would have two incident edges in addition to its edges to \(x,y\). Their internal vertices are also distinct.

Together with the edges from \(x,y\) to \(J\), these paths form a subdivision of \(K_{3,3}\), contradicting planarity. This proves the claim.

It follows from the claim and (4) that every star weight satisfies
\[
q_i\le4,
\]
and equality \(q_i=4\) implies
\[
f_i=0,\qquad t_i>0.                               \tag{10}
\]
The triangle bound (7) also gives \(q\le4\).

If \(q\le3\), then (2) already gives seven-choosability. Suppose \(q=4\).

- In the star case, (10) supplies one additional matching edge.
- In the triangle case, (7) gives \(2m+g\le1\), so \(F[T]\) is edgeless. Choose \(i\in T\). If \(a_i>0\), use its opposite pair-type. If \(a_i=0\), then \(q_i=q=4\), and (10) supplies a triple-type vertex.

Thus one additional edge always exists, and
\[
\chi_\ell(G_0^2)\le4+4-1=7.
\]

This completes every case of Theorem 1, including extension to the previously deleted leaves. ∎

# 4. Blocks and sharpness

## 4.1. Proof of Corollary 2

For completeness, the relevant gluing fact is
\[
\chi(G^2)=
\max\left\{\Delta(G)+1,\ \max_B\chi(B^2)\right\},   \tag{11}
\]
where blocks include bridges and isolated vertices.

The lower bounds are immediate. For the upper bound, let the right-hand side be \(K\), and add blocks in a rooted block-tree order. Suppose a new block \(B\) meets the already coloured graph only at a cutvertex \(v\).

Take a \(K\)-colouring of \(B^2\). Permute its colours to agree at \(v\), and to give the \(d_B(v)\) neighbours of \(v\) colours unused on its previously coloured neighbours. This is possible because
\[
K-1\ge\Delta(G)
\]
and the old and new neighbours together number at most \(\Delta(G)\). The neighbours of \(v\) in \(B\) have distinct colours in every colouring of \(B^2\).

The only square-edges crossing between the old and new portions join old and new neighbours of \(v\). Hence the resulting colouring is proper. Continuing proves (11).

Apply Theorem 1 separately to the blocks, using the global degree bound \(D=\Delta(G)\). Since \(W(D)\ge D+1\), equation (11) proves Corollary 2. ∎

## 4.2. Sharpness for every \(D\ge8\)

Take three vertices \(a,b,c\), with edges \(ab,bc\). Add independent sets of degree-two vertices with neighbourhoods and sizes
\[
\begin{array}{c|c}
\text{neighbourhood}&\text{number of vertices}\\ \hline
\{a,b\}&\lfloor D/2\rfloor-1\\
\{b,c\}&\lceil D/2\rceil-1\\
\{a,c\}&\lfloor D/2\rfloor.
\end{array}
\]

This graph is planar: draw the length-two paths in parallel bundles along the sides of a triangle, retaining the direct edges \(ab,bc\). Its maximum degree is \(D\), and \(\{a,b,c\}\) is a vertex cover.

Every two added vertices share a neighbour. The path \(a-b-c\) also puts every hub within distance two of every added vertex. Thus the graph has diameter two and order
\[
3+\bigl(\lfloor D/2\rfloor-1\bigr)
 +\bigl(\lceil D/2\rceil-1\bigr)
 +\lfloor D/2\rfloor
=
\lfloor3D/2\rfloor+1.
\]
Its square is therefore
\[
K_{\lfloor3D/2\rfloor+1}.
\]
So the high-degree bound cannot be improved even for planar graphs with a three-vertex cover.

# 5. Counterexample to the auxiliary minor-closed assertion

This section concerns only the final auxiliary question in the supplied context, not Wegner’s planar conjecture.

For an integer \(r\ge1\), construct \(X_r\) as follows.

- Start with four independent vertices \(a,b,c,d\).
- For each \(u\in\{b,c,d\}\), add a set \(A_u\) of \(r\) vertices, each with neighbourhood \(\{a,u\}\).
- Add a set \(T\) of \(2r\) vertices, each with neighbourhood \(\{b,c,d\}\).
- Add no other edges.

Every one of \(a,b,c,d\) has degree \(3r\), while the other vertices have degree two or three. Hence
\[
\Delta(X_r)=3r.
\]

The set
\[
A_b\cup A_c\cup A_d\cup T
\]
is a clique in \(X_r^2\):

- vertices in the \(A\)-sets share \(a\);
- vertices in \(T\) share \(b,c,d\);
- a vertex in \(A_u\) and a vertex in \(T\) share \(u\).

Consequently
\[
\chi(X_r^2)\ge5r=\frac53\Delta(X_r).               \tag{12}
\]

In fact equality holds even for list colouring. Pair \(a\) with a vertex of \(T\), and pair \(b,c,d\), respectively, with vertices of \(A_c,A_d,A_b\). These are four disjoint nonedges of \(X_r^2\). Since \(X_r\) has \(5r+4\) vertices, Lemma 3 gives
\[
\chi_\ell(X_r^2)\le5r.
\]

It remains to verify membership in a fixed proper minor-closed class.

**Claim.** \(X_r\) has no \(K_5\) minor.

Indeed, consider five disjoint connected branch sets for a hypothetical \(K_5\) minor. At most four contain a vertex of \(\{a,b,c,d\}\). A branch set containing none of these vertices lies in an independent set, so must be a singleton. That singleton has degree at most three, and therefore cannot be adjacent to all four other branch sets. Contradiction.

Thus all \(X_r\) belong to the proper minor-closed family of \(K_5\)-minor-free graphs. Equation (12) disproves
\[
\chi(G^2)\le\bigl(\tfrac32+o(1)\bigr)\Delta(G)
\]
for that family.

These graphs are nonplanar; for \(r\ge2\), three vertices of \(T\), together with \(b,c,d\), already form a \(K_{3,3}\).

Because this counterexample is elementary, the catalog’s auxiliary question may have omitted a hypothesis. I have not checked its formulation against the original source, so the conclusion here is specifically about the assertion **as quoted**.

# 6. What remains unresolved

The planar argument relies on the special intersection structure of neighbourhoods inside a four-vertex cover. It does not cover arbitrary planar blocks with larger vertex-cover number, and therefore does not resolve Wegner’s conjecture.

The established partial conclusions are:

- the full conjectured **list** bounds for planar graphs with vertex cover at most four;
- the ordinary bounds when every block has such a cover;
- sharpness of the large-degree estimate within that restricted planar class;
- a negative answer to the separately quoted minor-closed-family assertion.
