Attack the following open graph-theory problem.

Catalog id: weak_saturation_of_the_cube_in_the_clique
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/weak_saturation_of_the_cube_in_the_clique/
Original entry: http://www.openproblemgarden.org/op/weak_saturation_of_the_cube_in_the_clique
Problem attributed to: Morrison, Natasha, Noel, Jonathan A. (posted 2016-04-06)

=== Problem statement (OpenProblemGarden) ===
Title: Weak saturation of the cube in the clique
Problem Determine $ \text{wsat}(K_n,Q_3) $ .

=== Discussion / context (OpenProblemGarden) ===
Given graphs $ G $ and $ H $ , let $ \text{wsat}(G,H) $ denote the minimum number of edges in a subgraph $ F $ of $ G $ such that the edges of $ E(G)\setminus E(F) $ can be added to $ F $ , one edge at a time, so that each edge completes a copy of $ H $ when it is added. Of course, if one can solve the problem above, then a natural next step is to determine $ \text{wsat}(K_n,Q_m) $ for all $ n $ and $ m $ . Morrison, Noel and Scott [MNS] solved the related problem of determining $ \text{wsat}(Q_d,Q_m) $ for all $ d $ and $ m $ .

=== References listed by OpenProblemGarden ===
- [MNS] N. Morrison, J. A. Noel, A. Scott. Saturation in the hypercube and bootstrap percolation. To appear in Combin. Probab. Comput.

=== Catalog page (statement + literature review) ===
Weak saturation of the cube in the clique — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem of determining $\text{wsat}(K_n, Q_3)$ — the minimum number of edges in a weakly $Q_3$-saturated subgraph of $K_n$ — remains open. The related problem of $\text{wsat}(Q_d, Q_m)$ (hypercube host) was resolved by Morrison, Noel, and Scott, but no paper found addresses the complete-graph host case. Active research on weak saturation in the clique has focused on bipartite graphs and multipartite structures, leaving the hypercube case open.

 Reviewer notes. Searches found extensive recent literature on weak saturation in cliques (complete bipartite, tensor products, multipartite hypergraphs) but nothing specifically addressing wsat(K_n, Q_m) for any m. The MNS paper (arXiv:1408.5488) solved wsat(Q_d, Q_m) but that is for the hypercube host, not the complete graph host. The Springer Combinatorica 2025 paper on 'weak saturation rank' could not be fully accessed due to redirects. The problem likely remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Problem. Determine $ \text{wsat}(K_n,Q_3) $ .

Keywords:
bootstrap percolation · hypercube · Weak saturation

Discussion

Given graphs $ G $ and $ H $ , let $ \text{wsat}(G,H) $ denote the minimum number of edges in a subgraph $ F $ of $ G $ such that the edges of $ E(G)\setminus E(F) $ can be added to $ F $ , one edge at a time, so that each edge completes a copy of $ H $ when it is added. Of course, if one can solve the problem above, then a natural next step is to determine $ \text{wsat}(K_n,Q_m) $ for all $ n $ and $ m $ . Morrison, Noel and Scott [MNS] solved the related problem of determining $ \text{wsat}(Q_d,Q_m) $ for all $ d $ and $ m $ .

Bibliography

 [MNS]
 N. Morrison, J. A. Noel, A. Scott. Saturation in the hypercube and bootstrap percolation. To appear in Combin. Probab. Comput.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove ceil((5n-7)/3) <= wsat(K_n,Q_3) <= ceil((7n-1)/4) for n >= 11, and determine wsat(K_8,Q_3) = 15.",
  "would_publish": false,
  "caveats": "The exact function is not determined; novelty of these bounds and current literature status have not been verified."
}
```

# Partial results

Write \(w(n)=\operatorname{wsat}(K_n,Q_3)\). The following bounds and small-host value admit self-contained proofs:
\[
\boxed{\left\lceil\frac{5n-7}{3}\right\rceil
\le w(n)\le
\left\lceil\frac{7n-1}{4}\right\rceil
\qquad(n\ge 11).}
\]
Also,
\[
\boxed{w(n)=\binom n2\quad(n<8),\qquad w(8)=15,}
\]
and the constructions below give
\[
w(9)\le16,\qquad w(10)\le18.
\]

Thus the asymptotic bounds obtained here are
\[
\frac53n-O(1)\le w(n)\le\frac74n+O(1).
\]
They do not determine the requested function. I make no claim that these bounds are new.

Throughout, copies are **not required to be induced**. We repeatedly use the description
\[
Q_3=K_{4,4}-M,
\]
where \(M\) is a perfect matching.

## 1. A lower bound by merging edge blocks

### 1.1. A density inequality for proper subgraphs of the cube

Every nonempty proper edge-subgraph \(J\subsetneq Q_3\), with isolated vertices discarded, satisfies
\[
3e(J)\le 5v(J)-7. \tag{1}
\]

Indeed, the following are upper bounds on its number of edges:
\[
\begin{array}{c|rrrrrrr}
v(J)&2&3&4&5&6&7&8\\ \hline
e(J)&1&2&4&5&7&9&11.
\end{array}
\]
Each entry implies (1). For the entries on five, six and seven vertices, one can equivalently delete three, two or one vertices from the cubic graph \(Q_3\).

### 1.2. The block invariant

Let \(F\) be weakly \(Q_3\)-saturated in \(K_n\), where \(n\ge8\). Initially give each edge of \(F\) its own block.

During a valid saturation sequence, when an edge is added using a witnessing cube, merge all blocks containing the other eleven edges of that cube, and put the new edge in the merged block.

For a block \(B\), let

- \(V(B)\) be the set of vertices incident with its current edges;
- \(m(B)\) be the number of original edges of \(F\) assigned to it.

I claim that every block satisfies
\[
m(B)\ge \frac{5|V(B)|-7}{3}. \tag{2}
\]
A singleton original edge satisfies this with equality.

Suppose an addition merges \(k\) blocks \(B_1,\ldots,B_k\). Put
\[
v_i=|V(B_i)|,\qquad
v=\left|\bigcup_i V(B_i)\right|,\qquad
t=\sum_i v_i-v.
\]
Partition the eleven old edges of the witnessing cube according to their blocks. Let \(J_i\) be the nonempty subgraph in block \(B_i\), and put \(s_i=v(J_i)\).

By (1),
\[
5\sum_i s_i\ge 3\cdot11+7k.
\]
These subgraphs cover all eight vertices of the witnessing cube. Consequently,
\[
t\ge \sum_i s_i-8\ge \frac{7(k-1)}5. \tag{3}
\]
The first inequality follows by counting vertex multiplicities in the blocks; overlaps outside the witnessing cube only increase \(t\).

Using the induction hypothesis and (3),
\[
\begin{aligned}
m(B)
  &=\sum_i m(B_i)\\
  &\ge \frac{5\sum_i v_i-7k}{3}\\
  &=\frac{5v+5t-7k}{3}\\
  &\ge \frac{5v-7}{3}.
\end{aligned}
\]
The endpoints of the new edge already occur among the eleven old edges, so the new edge does not enlarge this vertex union. This proves the invariant.

### 1.3. Merging after saturation

After reaching \(K_n\), allow the following additional operation: merge all blocks meeting a complete copy of \(Q_3\).

The invariant still holds. If such a cube meets \(k\ge2\) blocks, its twelve edges are partitioned into nonempty **proper** subgraphs \(J_i\). Thus
\[
5\sum_i s_i\ge36+7k,
\qquad
t\ge\frac{7k-4}{5},
\]
which is stronger than needed in the preceding calculation.

Any two edges of \(K_n\), whether adjacent or disjoint, lie together in a cube when \(n\ge8\). Hence these operations can merge all blocks into one. The final block has vertex set \([n]\) and weight \(e(F)\). Applying (2) gives
\[
\boxed{e(F)\ge \left\lceil\frac{5n-7}{3}\right\rceil.} \tag{4}
\]

## 2. Three useful addition rules

These elementary rules will certify the upper-bound constructions.

### Rule A: absorbing a vertex into a clique

Suppose \(C\) is a clique of order at least seven, and \(x\notin C\) already has two distinct neighbours in \(C\). Then all remaining edges from \(x\) to \(C\) can be added.

For a desired edge \(xr\), use \(x\), its two old neighbours, \(r\), and four further vertices of \(C\). Embed a cube with \(x\) adjacent to precisely those three selected neighbours. Every required edge except \(xr\) is present.

In particular, once a clique of order at least seven has been obtained, a new vertex costs only two initial edges.

### Rule B: a vertex with two neighbours on one side

Suppose all edges between disjoint sets \(A,B\) are present, with
\[
|A|\ge4,\qquad |B|\ge3.
\]
If \(x\notin A\cup B\) has two neighbours in \(A\), then all edges from \(x\) to \(A\) can be added.

For a missing edge \(xa\), choose four vertices of \(A\), including \(a\) and the two old neighbours, and three vertices of \(B\). These support a cube with bipartition
\[
A_0,\quad \{x\}\cup B_0
\]
in which the three neighbours of \(x\) are the two old neighbours and \(a\).

### Rule C: two internal stars

Suppose all edges between \(A,B\) are present, where \(|A|,|B|\ge4\). Suppose that

- \(up,uq\) are present inside \(A\);
- \(br\) is present inside \(B\).

Then, for any missing edge \(bs\) inside \(B\), it can be added.

Choose
\[
a\in A\setminus\{u,p,q\},\qquad
t\in B\setminus\{b,r,s\}.
\]
Use the two squares
\[
(u,p,r,b),\qquad(q,t,a,s),
\]
with matching edges
\[
uq,\quad pt,\quad ra,\quad bs.
\]
Together they form a cube, and only \(bs\) is missing.

It follows that
\[
\boxed{K_{A,B}+\text{a }P_3\text{ inside }A
+\text{an edge inside }B
\text{ is weakly }Q_3\text{-saturated in }K_{A\cup B}.} \tag{5}
\]
Indeed, first grow a spanning star in \(B\), then a spanning star in \(A\). Once both internal graphs have no isolated vertices, repeated applications of the rule fill both sides completely.

## 3. A 13-edge seed for \(K_{5,4}\)

Let
\[
A_0=\{a_0,a_1,a_2,a_3\},\qquad
B=\{b_0,b_1,b_2,b_3\},
\]
and let
\[
Q=\{a_i b_j:i\ne j\}.
\]
This is a cube. Put \(e=a_0b_1\), and introduce a fifth vertex \(z\) on the \(A\)-side.

Start with
\[
(Q-e)\cup\{zb_0,zb_1\}. \tag{6}
\]
There are thirteen edges.

First add \(e\), completing \(Q\). Then:

- add \(zb_2\), using the cube obtained by replacing \(a_3\) by \(z\);
- add \(zb_3\), using the cube obtained by replacing \(a_2\) by \(z\).

Now add \(a_0b_0\). A witnessing cube has bipartition
\[
\{a_0,a_2,a_3,z\},\quad B,
\]
and is obtained from their \(K_{4,4}\) by deleting the matching
\[
\{a_2b_2,\ a_3b_3,\ a_0b_1,\ zb_0\}.
\]

Finally, for each \(i=1,2,3\), add \(a_i b_i\) using the cube
\[
Q-\{a_0b_i,a_i b_0\}+\{a_0b_0,a_i b_i\}.
\]
Thus (6) generates every edge of \(K_{A,B}\), where
\[
A=A_0\cup\{z\}.
\]

Adding a \(P_3\) inside \(A\) and one edge inside \(B\), then applying (5), proves
\[
w(9)\le13+3=16.
\]
Rule A consequently gives \(w(10)\le18\).

## 4. A 19-edge seed for \(K_{11}\)

Take the thirteen-edge seed (6), and introduce two more vertices \(x,y\). Add the six initial edges
\[
a_0a_1,\quad b_1b_2,\quad
xa_0,\quad xb_0,\quad
yb_1,\quad ya_2. \tag{7}
\]
This gives nineteen edges on eleven vertices.

First generate the complete \(K_{A,B}\) as in Section 3. The following three additions are then legal.

### Add \(xy\)

Use the squares
\[
(x,a_0,b_1,y),\qquad (b_0,a_1,b_2,a_2),
\]
with matching edges
\[
xb_0,\quad a_0a_1,\quad b_1b_2,\quad ya_2.
\]
Only \(xy\) is missing.

### Add \(ya_3\)

Use the squares
\[
(x,a_0,b_1,y),\qquad (b_0,a_1,b_2,a_3),
\]
with matching edges
\[
xb_0,\quad a_0a_1,\quad b_1b_2,\quad ya_3.
\]

### Add \(xb_3\)

Use the squares
\[
(x,a_0,b_1,y),\qquad (b_3,a_1,b_2,a_2),
\]
with matching edges
\[
xb_3,\quad a_0a_1,\quad b_1b_2,\quad ya_2.
\]

Now \(y\) has two neighbours \(a_2,a_3\) in \(A\), and \(x\) has two neighbours \(b_0,b_3\) in \(B\). Rule B fills all edges from \(y\) to \(A\) and from \(x\) to \(B\).

Consequently, all edges are present between
\[
A'=A\cup\{x\},\qquad B'=B\cup\{y\}.
\]
Inside these parts we have the paths
\[
a_1-a_0-x,\qquad b_2-b_1-y.
\]
Rule C completes the clique. Therefore
\[
\boxed{w(11)\le19.} \tag{8}
\]

## 5. Four new vertices for seven initial edges

Suppose a current seed can generate a clique \(C\) of order at least seven.

Introduce four new vertices \(u_0,u_1,u_2,u_3\), and initially put in:

- the path \(u_0u_1u_2u_3\), costing three edges;
- four edges \(u_i c_i\), where \(c_0,c_1,c_2,c_3\) are distinct vertices of \(C\).

Thus the cost is seven edges.

Once \(C\) is complete, add \(u_3u_0\). A witnessing cube consists of the two squares
\[
(u_0,u_1,u_2,u_3),\qquad(c_0,c_1,c_2,c_3),
\]
and their matching.

Choose
\[
z\in C\setminus\{c_0,c_1,c_2,c_3\}.
\]
For each \(i\), add \(u_i z\), using the outer square \(u_0u_1u_2u_3\), and a square in \(C\) obtained by replacing \(c_i\) by \(z\). Every other matching edge is already present.

Each new vertex now has two neighbours in \(C\). Rule A absorbs the four vertices, one at a time, into the clique.

Therefore
\[
w(n+4)\le w(n)+7 \tag{9}
\]
whenever the chosen seed generates a clique of order at least seven.

Starting from the nineteen-edge seed on eleven vertices, write
\[
n=11+4q+r,\qquad 0\le r\le3.
\]
Use \(q\) four-vertex gadgets and \(r\) two-edge single-vertex extensions. This gives
\[
w(n)\le19+7q+2r
=\left\lceil\frac{7n-1}{4}\right\rceil,
\]
proving the advertised upper bound.

## 6. The exact value on eight vertices

Here every witnessing cube is spanning. This permits a sharper argument:
\[
\boxed{w(8)=15.}
\]

### 6.1. Upper bound

Start with \(Q-e\), as above, and add
\[
a_0b_0,\qquad a_0a_1,\quad a_0a_2,\qquad b_0b_1.
\]
The edge count is \(11+4=15\).

Restore \(e\). The edge \(a_0b_0\) allows all other missing matching edges to be added by the two-edge-switch construction in Section 3. We now have \(K_{4,4}\), together with a \(P_3\) in one part and an edge in the other. Rule C finishes.

### 6.2. Two facts about balanced cuts of a cube

For any partition of a cube's vertices into two sets of size four:

1. either it is the cube's bipartition, with all twelve edges crossing;
2. or at least four cube edges lie inside the parts.

Moreover, when exactly four edges lie inside the parts, their internal graphs are either

- a two-edge matching in each part; or
- a \(P_3\) and an isolated vertex in each part.

These statements follow directly from \(Q_3=K_{4,4}-M\). For example, a four-set meeting one cube bipartition class in one vertex induces at least two edges; one meeting it in two vertices also induces at least two edges.

In the \(P_3\) case, the two path centres are adjacent. To see this explicitly, a representative four-set is
\[
\{000,001,010,111\};
\]
its path centre is \(000\), while the complementary four-set has path centre \(100\).

### 6.3. Reduction from fourteen edges

Suppose a weakly saturated graph had at most fourteen edges. Immediately after its first addition, the graph contains a spanning cube \(Q\), together with at most three extra edges.

Fix the bipartition \(L,R\) of \(Q\).

If at most two extra edges lie inside \(L\) or \(R\), then no further internal edge can ever be added: its witnessing cube would have between one and three internal edges, contrary to the balanced-cut fact. Thus such a graph cannot generate \(K_8\).

The only remaining case is
\[
Q+\text{three internal edges},
\]
with no extra crossing edge.

A crossing edge cannot be the next addition. Any witnessing cube would have no internal edges, but a spanning cubic graph plus one extra edge has no different spanning cubic subgraph containing that extra edge.

Thus, if any addition is possible, it is a fourth internal edge, completing another cube \(Q'\). The resulting graph is exactly
\[
G=Q\cup Q'.
\]
I show that \(G\) is closed under further cube additions.

### 6.4. Matching case

Suppose the four internal edges form a perfect matching in each of \(L,R\). Then \(G\) is 4-regular, and its complement \(M\) is a triangle-free cubic graph.

Triangle-freeness follows because \(G\) has independence number at most two:

- three vertices in one original part contain an edge of its added matching;
- two vertices in one part and one in the other cannot be independent, since a vertex of the crown graph \(Q\) misses only one vertex in the other part.

Suppose a missing edge could be added, completing a cube with bipartition \(X,Y\), \(|X|=|Y|=4\). The crossing edges of \(M\), except possibly the added edge, must fit inside a perfect matching. Hence their number is at most five.

On the other hand, each four-set spans at most four edges of the triangle-free graph \(M\). Thus \(M\) has at least four crossing edges. Since \(M\) is cubic, this cut has even size, so it has exactly four edges. Both sides therefore induce 4-cycles, and the crossing edges form a perfect matching.

Deleting one edge from a perfect matching leaves three edges whose extension to a perfect matching is unique. Consequently, the purported new cube would also have to omit the added edge—a contradiction.

### 6.5. Path case

Suppose instead that the internal graphs are two \(P_3\)'s. Relabel the original crown graph as
\[
Q=\{a_i b_j:i\ne j\}
\]
so that the four internal edges are
\[
a_0a_2,\quad a_0a_3,\qquad
b_1b_2,\quad b_1b_3. \tag{10}
\]

Here is why this normal form covers the case. The two path centres are adjacent in \(Q'\), so their joining edge belongs to \(Q\). Removing the two centres leaves exactly seven crossing edges in both cubes; hence these edge sets coincide. The internal leaves are then forced by degree three.

The vertices
\[
u=a_1,\qquad v=b_0
\]
have degree three in \(G\), with
\[
N_G(u)=\{v,b_2,b_3\},\qquad
N_G(v)=\{u,a_2,a_3\}.
\]

Consider a purported next edge and its spanning witnessing cube.

If the new edge meets neither \(u\) nor \(v\), all their incident edges must be used. The cube's bipartition is therefore one of just two possibilities:
\[
\{a_0,a_1,a_2,a_3\}\mid\{b_0,b_1,b_2,b_3\},
\]
or
\[
\{b_1,a_1,a_2,a_3\}\mid\{b_0,a_0,b_2,b_3\}.
\]
In either cut, the existing crossing graph is already a cube. Adding one edge cannot produce a different spanning cubic graph containing it.

If the new edge meets \(u\), it does not meet \(v\), since \(uv\) is already present. The unchanged neighbourhood of \(v\) forces one bipartition class to be
\[
\{u,a_2,a_3,t\},
\qquad t\in\{a_0,b_1,b_2,b_3\}.
\]
The choices \(t=a_0,b_1\) give the preceding two cuts. If \(t=b_2\), both \(u\) and \(b_2\) have only two existing crossing neighbours. One new crossing edge cannot raise both degrees to three, because they lie in the same part. The case \(t=b_3\) is identical.

The case where the new edge meets \(v\) is symmetric. Thus \(G\) is closed.

Both cases are impossible for a weakly saturated graph, proving \(w(8)\ge15\).

## 7. What remains unresolved

The argument leaves a genuine asymptotic gap:
\[
\frac53\le
\liminf_{n\to\infty}\frac{w(n)}n
\le
\limsup_{n\to\infty}\frac{w(n)}n
\le\frac74.
\]
It also does not determine \(w(9)\), \(w(10)\), or the exact values for larger \(n\).

The constructions and lower bound above use no unproved conjecture and no computational assertion. They constitute partial progress, not a resolution of the catalog problem.
