```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For k=2 the unresolved information is exactly a prescribed 'third pairing', which remains NP-complete even when the other two pairings have explicit solutions, while no separation is possible on chordal graph classes.",
  "would_publish": false,
  "caveats": "No hereditary separating class is constructed; the hardness mask is not hereditary and deleting it exposes the original instance."
}
```

## 1. Formalization

I use the standard convention that an induced linkage is a collection of vertex-disjoint induced paths with no edge joining two different paths. All terminals are distinct.

For a perfect matching \(M\) on a terminal set \(Z\), write
\[
\mathsf L(G,M)
\]
when \(G\) contains an induced linkage whose terminal pairs are the edges of \(M\).

For \(k=2\), let the four terminals be \(a_1,a_2,a_3,a_4\), and denote the three possible pairings by
\[
\begin{aligned}
M_0&=\{\{a_1,a_2\},\{a_3,a_4\}\},\\
M_1&=\{\{a_2,a_3\},\{a_4,a_1\}\},\\
M_*&=\{\{a_1,a_3\},\{a_2,a_4\}\}.
\end{aligned}
\]

The prescribed-pair problem asks for one specified \(M_i\). A flow instance with a \(2\)-\(2\) partition \(S,T\) accepts exactly when at least one of the two pairings crossing the cut \((S,T)\) is feasible.

---

## 2. Exactly what information three flow queries provide

There are three \(2\)-\(2\) partitions of four terminals, up to exchanging \(S\) and \(T\). Each partition excludes exactly one of \(M_0,M_1,M_*\), namely the pairing whose two edges lie within the two sides.

Let \(q_i\) be the answer to the flow query whose partition excludes \(M_i\). Then
\[
q_i=\bigvee_{j\ne i}\mathsf L(G,M_j).
\]

Consequently:

- if no pairing is feasible, \((q_0,q_1,q_*)=(0,0,0)\);
- if exactly one pairing is feasible, the answer vector has exactly two \(1\)'s and identifies that pairing;
- if at least two pairings are feasible, then
  \[
  (q_0,q_1,q_*)=(1,1,1).
  \]

Thus a polynomial algorithm for the flow problem already decides the prescribed problem on all instances having at most one feasible terminal pairing. Any separation for \(k=2\) must hide its hardness among instances having at least two feasible pairings.

The next theorem shows that this residual case is genuinely NP-hard in general graphs.

---

## 3. The “third pairing” remains NP-complete

### Theorem 3.1

The following problem is NP-complete:

> Given a graph \(H\) with ordered terminals \(a_1,a_2,a_3,a_4\), decide whether all three pairings \(M_0,M_1,M_*\) admit induced linkages.

Moreover, NP-hardness holds on instances in which \(M_0\) and \(M_1\) have explicit length-two linkage solutions. Equivalently, it is NP-hard, under the promise that \(M_0\) and \(M_1\) are feasible, to decide whether \(M_*\) is feasible.

### Proof

Membership in NP is immediate: since there are only three pairings, one may provide three linkage certificates.

We reduce from Induced \(2\)-Disjoint Paths, which is NP-complete by the source result and hence is NP-complete on unrestricted graphs.

Start with an instance
\[
(G;(s_1,t_1),(s_2,t_2)).
\]

Add four new independent vertices \(a_1,a_2,a_3,a_4\), with
\[
N(a_1)\cap V(G)=\{s_1\},\quad
N(a_3)\cap V(G)=\{t_1\},
\]
and
\[
N(a_2)\cap V(G)=\{s_2\},\quad
N(a_4)\cap V(G)=\{t_2\}.
\]
Call the resulting graph \(K\). Then
\[
\mathsf L(K,M_*) \quad\Longleftrightarrow\quad
(G;(s_1,t_1),(s_2,t_2))\text{ is a yes-instance}.
\tag{1}
\]
Indeed, the new terminals are leaves in \(K\), so their incident edges must be the first and last edges of the corresponding paths.

Now add four further vertices
\[
U=\{u_1,u_2,u_3,u_4\}.
\]
Make \(U\) independent and add the edges of the induced cycle
\[
a_1u_1a_2u_2a_3u_3a_4u_4a_1.
\tag{2}
\]
Finally, make every \(u_i\) adjacent to every vertex of \(G\). Let the resulting graph be \(H\).

#### The two easy pairings

The paths
\[
a_1u_1a_2,\qquad a_3u_3a_4
\]
form an induced \(M_0\)-linkage. Similarly,
\[
a_2u_2a_3,\qquad a_4u_4a_1
\]
form an induced \(M_1\)-linkage.

Thus \(M_0\) and \(M_1\) are always feasible.

#### The hard pairing is preserved

We claim
\[
\mathsf L(H,M_*)\quad\Longleftrightarrow\quad \mathsf L(K,M_*).
\tag{3}
\]

The reverse implication is immediate: a linkage lying in \(K\) remains induced in \(H\), since vertices outside a chosen linkage do not affect inducedness.

For the forward implication, let \(P,Q\) be an induced \(M_*\)-linkage in \(H\). Suppose that \(P\) contains a vertex of \(U\). Since every vertex of \(U\) is complete to \(V(G)\), anticompleteness of \(P\) and \(Q\) implies
\[
V(Q)\cap V(G)=\varnothing.
\]
The endpoints of \(Q\) are nonadjacent, so \(Q\) has an internal vertex. Its internal vertices cannot be any of the other terminals, since those are endpoints of \(P\), and hence \(Q\) must also contain a vertex of \(U\). By symmetry, \(P\) then contains no vertex of \(G\).

It follows that both \(P\) and \(Q\) lie in the induced \(8\)-cycle (2). But this cycle has no pair of vertex-disjoint paths connecting the opposite pairing
\[
a_1-a_3,\qquad a_2-a_4:
\]
the four terminals occur alternately around the cycle. This is a contradiction.

Therefore neither path uses \(U\), and the linkage lies in \(K\), proving (3).

Combining (1) and (3), \(M_*\) is feasible in \(H\) exactly when the original Induced \(2\)-Disjoint Paths instance is positive. Since \(M_0,M_1\) are always feasible, all three pairings are feasible exactly in the positive case. The reduction is polynomial. ∎

### Consequence

On the constructed instances, every possible \(2\)-\(2\) flow query on the terminal set \(\{a_1,a_2,a_3,a_4\}\) has answer YES, regardless of the answer to the original NP-complete instance. Indeed, every \(2\)-\(2\) cut allows at least one of \(M_0,M_1\).

Thus the simple strategy “try all terminal bipartitions” loses precisely an NP-hard bit of information.

This is only a local separation, not the requested hereditary complexity separation. The mask vertices \(U\) can be deleted, and
\[
H-U=K,\qquad H-(U\cup\{a_1,a_2,a_3,a_4\})=G.
\]
Therefore the hereditary closure of these masked graphs exposes the original hard cores.

---

## 4. No gap on chordal graph classes

There is nevertheless a broad hereditary setting in which the pairing ambiguity cannot occur.

### Lemma 4.1: uniqueness of disjoint pairings in a tree

Let \(T\) be a tree, and let \(\{A_z:z\in Z\}\) be pairwise disjoint nonempty subtrees of \(T\). There is at most one perfect matching \(M\) on \(Z\) such that the minimal subtrees joining \(A_x\) to \(A_y\), for \(xy\in M\), are pairwise vertex-disjoint.

#### Proof

Contract each \(A_z\) to a marked vertex \(z\), obtaining another tree \(T'\). A permissible matching is represented by pairwise vertex-disjoint paths in \(T'\), one joining each matched pair.

For an edge \(e\in E(T')\), let \(Z_e\) be the marked vertices on one side of \(T'-e\). Let \(c_e\) be the number of matched paths crossing \(e\). Since the paths are vertex-disjoint,
\[
c_e\le 1.
\]
On the other hand,
\[
c_e\equiv |Z_e|\pmod 2,
\]
because pairs with both ends on the same side contribute an even number of endpoints, while each crossing pair contributes one. Hence
\[
c_e=
\begin{cases}
1,& |Z_e|\text{ odd},\\
0,& |Z_e|\text{ even}.
\end{cases}
\]
Thus the union of all matched paths is uniquely determined by the marked vertices. Its components are paths, and each such component has exactly two marked endpoints, uniquely determining the matching. ∎

### Theorem 4.2: chordal graphs have a unique feasible terminal pairing

Let \(G\) be chordal and let \(Z\) be an even terminal set. There is at most one perfect matching \(M\) on \(Z\) for which \(G\) has an induced \(M\)-linkage.

#### Proof

Use the standard clique-tree representation of a chordal graph: there is a tree \(T\) and, for each \(v\in V(G)\), a subtree \(T_v\subseteq T\) such that
\[
uv\in E(G)\quad\Longleftrightarrow\quad T_u\cap T_v\ne\varnothing.
\]

Suppose two distinct perfect matchings \(M,M'\) both admit induced linkages. Their symmetric difference contains a nontrivial alternating cycle on a terminal subset \(Z_0\).

For any two distinct terminals \(x,y\in Z_0\), they are on different paths in at least one of the two linkages: if \(xy\in M\), then \(xy\notin M'\), and otherwise they are already on different \(M\)-paths. Hence \(x,y\) are nonadjacent in \(G\), and so the terminal subtrees
\[
\{T_z:z\in Z_0\}
\]
are pairwise disjoint.

For each pair \(xy\in M\) on the alternating cycle, the union of the subtrees corresponding to the vertices of the \(x\)-\(y\) linkage path is connected and contains \(T_x\cup T_y\). Since distinct linkage paths are anticomplete, these connected unions are pairwise disjoint. Thus \(M|_{Z_0}\) gives a permissible matching of the terminal subtrees in the sense of Lemma 4.1. The same is true of \(M'|_{Z_0}\).

Lemma 4.1 says these two matchings must be equal, contradicting the choice of a nontrivial symmetric-difference cycle. ∎

### Corollary 4.3: flow determines linkage on chordal graphs

Fix \(k\). Given desired pairs
\[
(s_1,t_1),\ldots,(s_k,t_k)
\]
in a chordal graph, choose independently, for each \(i\), which one of \(s_i,t_i\) is placed in \(S\), putting the other in \(T\). Query the flow problem for every such orientation.

The desired linkage exists if and only if all these flow queries return YES.

Indeed, the desired matching crosses every such cut. Conversely, by Theorem 4.2 there is at most one feasible perfect matching. If that matching crossed every orientation of the desired pairs, it could not contain an edge joining terminals from two different desired pairs: one can orient those two pairs so that both endpoints of that edge lie on the same side. Hence the unique matching must be the desired one.

There are \(2^{k-1}\) distinct queries up to exchanging \(S,T\), which is constant for fixed \(k\).

For \(k=2\), only the following two queries are needed:
\[
S=\{s_1,s_2\},\quad T=\{t_1,t_2\},
\]
and
\[
S=\{s_1,t_2\},\quad T=\{t_1,s_2\}.
\]

Consequently, on every subclass of chordal graphs, polynomial-time solvability of the flow variant implies polynomial-time solvability of the linkage variant.

### Direct chordal algorithm

In fact, both problems are polynomial-time solvable on chordal graphs for every fixed \(k\).

In the subtree representation, an induced linkage path \(P_i\) gives a connected host-tree set
\[
B_i=\bigcup_{v\in V(P_i)}T_v.
\]
The sets \(B_1,\ldots,B_k\) are pairwise disjoint. Any \(k\) pairwise disjoint connected sets in a tree can be placed in distinct components by deleting \(k-1\) tree edges.

Thus one may enumerate all sets \(F\subseteq E(T)\) with \(|F|=k-1\). For each component \(C\) of \(T-F\), let
\[
V_C=\{v\in V(G):T_v\subseteq C\}.
\]
Accept a choice of \(F\) if the two terminals of each prescribed pair lie in one component, different pairs lie in different components, and each pair is connected in the corresponding graph \(G[V_C]\).

Necessity follows by choosing the cut edges between the actual connected sets \(B_i\). For sufficiency, choose a shortest terminal path in each \(G[V_C]\). Shortest paths are induced, and vertices assigned to different host-tree components are anticomplete because their representing subtrees are disjoint.

This gives an \(n^{O(k)}\) algorithm, hence polynomial time for fixed \(k\).

---

## 5. Rooted-hole reformulation for \(k=2\)

There is a useful equivalent formulation of the flow problem.

Given
\[
S=\{s_1,s_2\},\qquad T=\{t_1,t_2\},
\]
form \(\widehat G\) by adding two nonadjacent vertices \(x,y\) with
\[
N(x)=S,\qquad N(y)=T.
\]

Then
\[
(G,S,T)\text{ has two induced disjoint }S\text{--}T\text{ paths}
\]
if and only if
\[
\widehat G\text{ has an induced cycle containing both }x\text{ and }y.
\]

Indeed, two mutually induced \(S\)-\(T\) paths, together with \(x,y\), form such a hole. Conversely, since \(x\) and \(y\) both have degree two, deleting them from a hole containing them leaves exactly two mutually induced \(S\)-\(T\) paths.

The prescribed-pair problem asks for a specified cyclic pairing of the four neighbors of \(x,y\), whereas the flow problem accepts either possible cyclic pairing. This reformulation captures the ordered-versus-unordered nature of the conjectured gap. It is conceptual only: adding \(x,y\) need not preserve an arbitrary hereditary class.

---

## 6. What has and has not been resolved

The results above establish:

1. For \(k=2\), flow queries determine the prescribed answer unless at least two terminal pairings are feasible.
2. Distinguishing “exactly the two easy pairings” from “all three pairings” is NP-complete, even when the two easy linkages are explicit paths of length two.
3. Chordal graphs cannot exhibit the desired complexity gap; in fact, fixed-\(k\) induced linkage is polynomial there.
4. A potential separating class must support substantial multiple-pairing ambiguity, necessarily beyond the tree-like behavior of chordal graphs.

The catalog question remains open. The masking reduction does not yield a hereditary class with polynomial flow: deleting the mask exposes the arbitrary original graph, and no polynomial flow algorithm for that hereditary closure is obtained.