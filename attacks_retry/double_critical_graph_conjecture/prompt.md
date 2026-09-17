Attack the following open graph-theory problem.

Catalog id: double_critical_graph_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/double_critical_graph_conjecture/
Original entry: http://www.openproblemgarden.org/op/double_critical_graph_conjecture
Problem attributed to: Erdos, Paul, Lovasz, Laszlo (posted 2009-01-18)

=== Problem statement (OpenProblemGarden) ===
Title: Double-critical graph conjecture
A connected simple graph $ G $ is called double-critical, if removing any pair of adjacent vertexes lowers the chromatic number by two. Conjecture $ K_n $ is the only $ n $ -chromatic double-critical graph

=== Discussion / context (OpenProblemGarden) ===
This conjecture is a special case of a more general problem by Erdos and Lovasz proposed in 1966. It has been independently proven for the case where $ \chi(G) = 5 $ by Mozhan [3] and Stiebitz [4].

=== References listed by OpenProblemGarden ===
- *[1] P. Erdos, Problem 2, in: Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, New York, 1968, p. 361.
- [2] F. Chung, R. Graham, Erdos on graphs: His legacy of unsolved problems, A K Peters, Wellesley, Massachusetts, 1998.
- [3] N. N. Mozhan, On double critical graphs with the chromatic number five, Metody Diskretb. Anal. 46 (1987) 50-59.
- [4] M. Stiebitz, is the only double-critical -chromatic graph, Discrete Math. 64 (1987) 91-93.

=== Catalog page (statement + literature review) ===
Double-critical graph conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that $K_n$ is the only $n$-chromatic double-critical graph remains open for $n \geq 6$ in general. Substantial partial progress has been made since the OPG posting: the conjecture is now verified for claw-free graphs with chromatic number $t \leq 8$, and every double-critical $t$-chromatic graph is known to contain a $K_t$ minor for all $t \leq 9$.

 Cited literature (5)

 
 
 
partial Double-Critical Graphs and Complete Minors
 (2010)
 

 
 Ken-ichi Kawarabayashi, Anders Sune Pedersen, Bjarne Toft · Electronic Journal of Combinatorics · arXiv:0810.3133 · doi:10.37236/359

Proves that for $k=6$ and $k=7$, any non-complete double-critical $k$-chromatic graph is 6-connected and contains $K_k$ as a minor.
 

 
 
partial Complete and almost complete minors in double-critical 8-chromatic graphs
 (2010)
 

 
 Anders Sune Pedersen · arXiv preprint · arXiv:1007.5400

Proves every double-critical 8-chromatic graph contains a $K_8^-$ minor, and a full $K_8$ minor when the minimum degree is not 10 or 11.
 

 
 
partial A note on the double-critical graph conjecture
 (2016)
 

 
 Hao Huang, Alexander Yu · arXiv preprint · arXiv:1604.05262

Proves the conjecture for claw-free double-critical graphs of chromatic number 6.
 

 
 
partial Clique Minors in Double-critical Graphs
 (2016)
 

 
 Martin Rolek, Zi-Xia Song · arXiv preprint · arXiv:1603.06964

Proves every double-critical $t$-chromatic graph contains a $K_t$ minor for all $t \leq 9$.
 

 
 
partial Double-critical graph conjecture for claw-free graphs
 (2016)
 

 
 Martin Rolek, Zi-Xia Song · Discrete Mathematics · arXiv:1610.00636

Proves the Erdős–Lovász conjecture for claw-free double-critical graphs of chromatic number $t \leq 8$.
 

 

 Reviewer notes. A ResearchGate page (publication ID 362648627) titled 'On the double-critical graph conjecture' was inaccessible (HTTP 403); a search snippet suggested it might contain a complete proof via a universal-vertex argument, but this could not be verified and the paper is not cited. The arXiv preprint 0810.3133 was submitted in October 2008 (before the OPG posting date) but published in EJC in June 2010; it is included with year 2010. arXiv:1603.06964 was verified as submitted in 2016 but revised in 2017; year listed as 2016. The ScienceDirect page for arXiv:1610.00636 (Discrete Math., 2017) was not fetched; the arXiv URL is used instead.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. $ K_n $ is the only $ n $ -chromatic double-critical graph

Keywords:
coloring · complete graph

Discussion

This conjecture is a special case of a more general problem by Erdos and Lovasz proposed in 1966. It has been independently proven for the case where $ \chi(G) = 5 $ by Mozhan [3] and Stiebitz [4].

Bibliography

★ [1]
 P. Erdos, Problem 2, in: Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, New York, 1968, p. 361.

 [2]
 F. Chung, R. Graham, Erdos on graphs: His legacy of unsolved problems, A K Peters, Wellesley, Massachusetts, 1998.

 [3]
 N. N. Mozhan, On double critical graphs with the chromatic number five, Metody Diskretb. Anal. 46 (1987) 50-59.

 [4]
 M. Stiebitz, $ K_5 $ is the only double-critical $ 5 $ -chromatic graph, Discrete Math. 64 (1987) 91-93.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds if deleting the endpoints of some edge leaves independence number at most two; consequently, any noncomplete counterexample has at least χ(G)+6 vertices.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; novelty is not claimed for these restricted results."
}
```

# A restricted case and an order bound

All graphs below are finite and simple, and \(\chi(\varnothing)=0\). Deletions such as \(G-\{x,y\}\) mean **vertex deletions**.

I prove the following restricted form of the conjecture.

**Theorem 1.** Let \(G\) be a connected double-critical graph with \(\chi(G)=t\). If some edge \(xy\in E(G)\) satisfies
\[
\alpha\bigl(G-\{x,y\}\bigr)\le 2,
\]
then \(G\cong K_t\).

Thus every noncomplete counterexample must satisfy
\[
\alpha\bigl(G-\{x,y\}\bigr)\ge 3
\qquad\text{for every }xy\in E(G).
\tag{1}
\]

Combining this with elementary degree restrictions gives:

**Corollary 2.** Every noncomplete connected double-critical \(t\)-chromatic graph has at least \(t+6\) vertices.

The proofs use the classical Gallai–Edmonds matching decomposition. No claim of novelty is made.

## 1. Vertex-criticality and a complementary formulation

A connected double-critical graph with at least two vertices is vertex-critical:
\[
\chi(G-v)=t-1 \qquad(v\in V(G)).
\tag{2}
\]
Indeed, choose a neighbor \(w\) of \(v\). Then
\[
t-1\le \chi(G-v)
\le \chi(G-\{v,w\})+1=t-1.
\]
In particular, if \(G\) contains a \(K_t\), then \(G=K_t\): deleting any vertex outside that clique would contradict (2).

For a graph \(J\), define its **clique-packing savings**
\[
p(J)=\max_{\mathcal P}\sum_{Q\in\mathcal P}(|Q|-1),
\]
where \(\mathcal P\) ranges over collections of pairwise vertex-disjoint cliques of order at least two. Uncovered vertices may be regarded as singleton cliques.

A coloring of \(\overline J\) is a partition into cliques of \(J\), so
\[
p(J)=|V(J)|-\chi(\overline J).
\tag{3}
\]
Writing \(\nu(J)\) for the maximum matching size, we have
\[
p(J)\ge \nu(J),
\]
with equality whenever \(J\) is triangle-free.

We will also use two elementary properties:
\[
p(J_1\mathbin{\dot\cup}J_2)=p(J_1)+p(J_2)
\tag{4}
\]
and
\[
p(J)\le p(J-X)+|X|.
\tag{5}
\]
For (5), remove \(X\) from a clique packing. Each removed vertex decreases its savings by at most one.

Now put
\[
H=\overline G,\qquad n=|V(G)|,\qquad r=n-t.
\]
Equations (2), (3), and double-criticality give
\[
\begin{aligned}
p(H)&=r,\\
p(H-v)&=r &&(v\in V(H)),\\
p(H-\{u,v\})&=r &&(uv\in E(G)).
\end{aligned}
\tag{6}
\]

## 2. A matching lemma

Here is the precise matching-theoretic ingredient.

For a graph \(J\), let:

- \(D\) be the set of vertices exposed by at least one maximum matching;
- \(A=N_J(D)\setminus D\);
- \(C=V(J)\setminus(D\cup A)\).

The Gallai–Edmonds theorem states that the components \(Q_1,\ldots,Q_m\) of \(J[D]\) are factor-critical, while \(J[C]\) has a perfect matching. Every maximum matching:

- has a near-perfect matching inside each \(Q_i\);
- matches every vertex of \(A\) into a distinct \(Q_i\);
- has a perfect matching inside \(C\).

In particular, a maximum matching exposes at most one vertex in each \(Q_i\). If
\[
b_i=\frac{|V(Q_i)|-1}{2},
\]
then
\[
\nu(J)=\sum_i b_i+|A|+\frac{|C|}{2}.
\tag{7}
\]

**Lemma 3.** Suppose
\[
p(J)=\nu(J)
\quad\text{and}\quad
p(J-v)=p(J)\quad\text{for every }v\in V(J).
\tag{8}
\]
Then \(A=\varnothing\) in the Gallai–Edmonds decomposition. Moreover,
\[
p(Q_i)=b_i
\quad\text{and}\quad
p(J[C])=\frac{|C|}{2}.
\tag{9}
\]

**Proof.** Fix a component \(Q_i\). Since its vertices belong to \(D\), some maximum matching exposes a vertex of \(Q_i\). Such a matching has exactly \(b_i\) edges inside \(Q_i\) and no matching edge from \(Q_i\) to \(A\).

If \(p(Q_i)>b_i\), replacing those \(b_i\) matching edges by a clique packing of \(Q_i\) would produce a clique packing of \(J\) with savings greater than \(\nu(J)\), contradicting \(p(J)=\nu(J)\). Thus \(p(Q_i)=b_i\).

Likewise, replacing the perfect matching on \(C\) shows
\[
p(J[C])=\frac{|C|}{2}.
\]
There are no edges between distinct \(Q_i\), or between \(D\) and \(C\). Hence, by (7),
\[
p(J-A)=\sum_i b_i+\frac{|C|}{2}
=\nu(J)-|A|.
\tag{10}
\]
If \(a\in A\), inequality (5), applied to \(J-a\), gives
\[
p(J-a)
\le p(J-A)+|A|-1
=\nu(J)-1,
\]
contrary to (8). Therefore \(A=\varnothing\). \(\square\)

## 3. Proof of Theorem 1

Let \(xy\in E(G)\) satisfy
\[
\alpha(G-\{x,y\})\le2,
\]
and put \(S=\{x,y\}\). Thus \(H-S\) is triangle-free. By (6),
\[
r=p(H-S)=\nu(H-S)\le \nu(H)\le p(H)=r.
\]
Consequently,
\[
p(H)=\nu(H)=\nu(H-S)=r.
\tag{11}
\]

Apply Lemma 3 to \(H\). Its Gallai–Edmonds set \(A\) is empty.

Choose a maximum matching of \(H-S\), viewed as a maximum matching of \(H\). It exposes both vertices of \(S\). Therefore:

- \(S\subseteq D\);
- each factor-critical component \(Q_i\) contains at most one vertex of \(S\).

### Eliminating \(C\)

Since \(S\subseteq D\), the graph \(H[C]\) is triangle-free. It also has a perfect matching. If \(C\ne\varnothing\), choose \(c\in C\). Because \(A=\varnothing\), \(H\) is the disjoint union of the \(Q_i\) and \(H[C]\). Thus
\[
\begin{aligned}
p(H-c)
&=\sum_i p(Q_i)+p(H[C]-c)\\
&=\sum_i b_i+\nu(H[C]-c)\\
&\le \sum_i b_i+\frac{|C|}{2}-1\\
&=r-1.
\end{aligned}
\]
This contradicts (6). Hence \(C=\varnothing\).

We have now shown that every component \(Q\) of \(H\) is factor-critical, has odd order \(2b+1\), and satisfies
\[
p(Q)=b.
\tag{12}
\]
Moreover, each \(Q\) contains at most one vertex of \(S\).

By additivity and (6), whenever \(a,b'\in V(Q)\) are nonadjacent in \(H\), so that \(ab'\in E(G)\), we have
\[
p(Q-\{a,b'\})=p(Q).
\tag{13}
\]

### Components avoiding \(S\)

Suppose \(V(Q)\cap S=\varnothing\). Then \(Q\) is triangle-free.

If \(Q\) is nontrivial, its odd order is at least three, so it cannot be a complete triangle-free graph. Choose nonadjacent vertices \(a,b'\in V(Q)\). Since \(Q-\{a,b'\}\) is triangle-free and has \(2b-1\) vertices,
\[
p(Q-\{a,b'\})
=\nu(Q-\{a,b'\})
\le b-1,
\]
contradicting (12) and (13). Thus \(Q\) is a singleton.

### Components meeting \(S\)

Suppose \(V(Q)\cap S=\{z\}\). Then \(Q-z\) is triangle-free.

If \(z\) has a nonneighbor \(u\) inside \(Q\), then \(Q-\{z,u\}\) is triangle-free on \(2b-1\) vertices. Again,
\[
p(Q-\{z,u\})\le b-1,
\]
contradicting (12) and (13). Therefore \(z\) is adjacent in \(H\) to every other vertex of \(Q\).

If \(b\ge1\), factor-criticality supplies a perfect matching of \(Q-z\). Take one matching edge \(ab'\). The vertices \(z,a,b'\) form a triangle. Using this triangle and the other \(b-1\) matching edges gives a clique packing with savings
\[
2+(b-1)=b+1,
\]
contrary to (12). Hence \(b=0\), and \(Q\) is again a singleton.

Every component of \(H\) is therefore a singleton. Thus \(H\) is edgeless and
\[
G\cong K_n=K_t.
\]
This proves Theorem 1. \(\square\)

## 4. A minimum-degree restriction

We next establish the degree bound needed for Corollary 2.

**Lemma 4.** If \(G\) is a noncomplete connected double-critical \(t\)-chromatic graph, then
\[
\delta(G)\ge t+1.
\tag{14}
\]

**Proof.** The cases \(t\le2\) admit no noncomplete connected double-critical graph, so assume \(t\ge3\).

First observe that, for every edge \(uv\), every color class in every \((t-2)\)-coloring of \(G-\{u,v\}\) contains a common neighbor of \(u\) and \(v\). Otherwise, if a color class \(I\) contained no common neighbor, then \(G[I\cup\{u,v\}]\) would be bipartite: \(I\) is independent, and no vertex of \(I\) is adjacent to both \(u\) and \(v\). Replacing that one color class by a two-coloring including \(u,v\) would give a \((t-1)\)-coloring of \(G\).

Consequently,
\[
|N(u)\cap N(v)|\ge t-2
\qquad(uv\in E(G)).
\tag{15}
\]
This implies \(\delta(G)\ge t-1\).

If \(d(v)=t-1\), then (15) forces every two vertices in \(N(v)\) to be adjacent. Thus \(G[N[v]]\cong K_t\), forcing \(G=K_t\), a contradiction.

Suppose \(d(v)=t\). Equation (15) says that every vertex of \(N(v)\) has at most one nonneighbor within \(N(v)\). The neighborhood cannot be complete, since together with \(v\) it would form a \(K_{t+1}\). Choose nonadjacent \(a,b\in N(v)\). Then
\[
N(v)\cap N(a)=N(v)\setminus\{a,b\},
\]
a set of exactly \(t-2\) vertices.

In any \((t-2)\)-coloring of \(G-\{v,a\}\), these common neighbors represent all \(t-2\) colors. But \(b\) is adjacent to every one of them, because its only nonneighbor within \(N(v)\) is \(a\). No color is available for \(b\), a contradiction.

Therefore \(\delta(G)\ge t+1\). \(\square\)

## 5. Proof of Corollary 2

Suppose, for a contradiction, that \(G\) is noncomplete and
\[
n\le t+5.
\]
By Lemma 4, its complement \(H\) satisfies
\[
\Delta(H)\le n-1-(t+1)\le3.
\tag{16}
\]
Also,
\[
p(H)=n-t\le5.
\tag{17}
\]

Vertex-criticality prohibits two nonadjacent vertices of \(G\) from having identical neighborhoods: after deleting one, it could be given the other’s color. Equivalently, \(H\) cannot contain adjacent vertices with identical closed neighborhoods.

It follows that distinct triangles of \(H\) are vertex-disjoint:

- Two triangles sharing exactly one vertex would give that vertex degree at least four, contradicting (16).
- If triangles \(abc\) and \(abd\) shared an edge, then the subcubic bound would give
  \[
  N_H[a]=N_H[b]=\{a,b,c,d\},
  \]
  contradicting the preceding prohibition.

Each triangle contributes two to a clique packing. By (17), \(H\) therefore has at most two triangles.

We can now find an edge of \(G\) whose endpoint deletion destroys all triangles of \(H\):

- If \(H\) has no triangles, take any edge of \(G\).
- If \(H\) has one triangle, choose a vertex of it and any incident edge in \(G\).
- If \(H\) has two triangles, choose a vertex \(a\) of the first. It already has two neighbors within its triangle, so by (16) it cannot be adjacent in \(H\) to all three vertices of the second. Choose a nonneighbor \(b\) there. Then \(ab\in E(G)\).

For the resulting edge \(ab\), the graph \(H-\{a,b\}\) is triangle-free. Equivalently,
\[
\alpha(G-\{a,b\})\le2.
\]
Theorem 1 now forces \(G=K_t\), a contradiction. Hence \(n\ge t+6\). \(\square\)

## 6. What remains unresolved

The argument does not handle a graph satisfying (1): every edge deletion may leave an independent triple.

The essential limitation is the equality
\[
p(J)=\nu(J)
\]
for triangle-free \(J\). Once triangles are present, clique-packing savings can exceed matching size—for example,
\[
p(K_3)=2,\qquad \nu(K_3)=1.
\]
Thus the matching parity obstructions used above need not control chromatic number in the remaining cases.

In particular, no universal vertex has been established for an arbitrary double-critical graph, and the general conjecture is not proved here.
