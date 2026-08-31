```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound with c=0 holds when at most four clusters are active, and in particular diam PP(K,K,K,K)=ceil(4K/3), but the unrestricted case remains open.",
  "would_publish": false,
  "caveats": "The argument does not handle pairs involving five or more active clusters, including the general kappa_1=3 case."
}
```

## 1. Statement of the partial result

Write \(m=\sum_i\kappa_i\). A vertex of the partition polytope is a labelled partition
\[
P=(P_1,\dots,P_n),\qquad |P_i|=\kappa_i
\]
of an \(m\)-element ground set. For two vertices \(P,Q\), define
\[
d_i(P,Q)=|P_i\setminus Q_i|,\qquad d(P,Q)=\max_i d_i(P,Q),
\]
and call \(i\) active if \(P_i\ne Q_i\).

The following is proved below.

### Theorem
For any two vertices \(P,Q\) of \(\mathrm{PP}(\kappa_1,\dots,\kappa_n)\):

1. \(\operatorname{dist}(P,Q)\ge d(P,Q)\).
2. If at most three clusters are active, then
   \[
   \operatorname{dist}(P,Q)=d(P,Q).
   \]
3. If at most four clusters are active, then
   \[
   \operatorname{dist}(P,Q)\le
   \left\lceil\frac{4d(P,Q)}3\right\rceil.
   \]

Consequently, if \(n\le4\), then
\[
\operatorname{diam}\mathrm{PP}(\kappa_1,\dots,\kappa_n)
 \le \left\lceil\frac{4\kappa_1}{3}\right\rceil.
\]
Thus the conjecture holds with \(c=0\) for at most four clusters.

There are also two exact consequences:

- For \(n\le3\),
  \[
  \operatorname{diam}\mathrm{PP}(\kappa_1,\dots,\kappa_n)
  =\min\{\kappa_1,m-\kappa_1\}.
  \]
- For every \(K\ge1\),
  \[
  \operatorname{diam}\mathrm{PP}(K,K,K,K)
  =\left\lceil\frac{4K}{3}\right\rceil.
  \]

No claim of literature novelty is made for these special cases.

---

## 2. The discrepancy digraph and adjacency

Use the standard transportation realization
\[
\mathrm{PP}(\kappa_1,\dots,\kappa_n)
 =
 \left\{x\in\mathbb R_{\ge0}^{n\times m}:
 \sum_i x_{i,e}=1,\ 
 \sum_e x_{i,e}=\kappa_i
 \right\}.
\]
Its vertices are the incidence matrices of the labelled partitions.

Given \(P,Q\), form a directed multigraph \(D(P,Q)\) on the cluster set \([n]\): for every item
\[
e\in P_i\cap Q_j,\qquad i\ne j,
\]
put a labelled arc \(i\to j\). Items already in their final cluster are omitted. At every vertex \(i\),
\[
d_D^+(i)=|P_i\setminus Q_i|
        =|Q_i\setminus P_i|
        =d_D^-(i),
\]
so \(D(P,Q)\) is Eulerian.

### Adjacency lemma
Two partition vertices are adjacent precisely when their discrepancy digraph is one directed simple cycle, with a directed \(2\)-cycle allowed.

Indeed, consider the bipartite support graph of the two incidence matrices, with one side consisting of the clusters and the other of the items. The minimal face containing the two vertices is obtained by setting all coordinates outside the union of their supports to zero. Its dimension is
\[
|E|-|V|+c,
\]
the cycle rank of that support graph. Deleting unchanged-item leaves and contracting each changed-item vertex reduces this to the cycle rank of the underlying multigraph of \(D(P,Q)\).

Every nontrivial component of an Eulerian digraph has cycle rank at least one. Cycle rank one therefore means there is one nontrivial component and every active vertex has indegree and outdegree one, namely a directed cycle. This is exactly the adjacency condition.

Thus one polytope edge moves one item out of each cluster on a directed simple cycle.

It follows immediately that
\[
\operatorname{dist}(P,Q)\ge d_i(P,Q)
\]
for every \(i\): each of the \(d_i(P,Q)\) original items that must leave \(P_i\) has to be moved at least once, while one polytope edge moves at most one item out of cluster \(i\). This proves part 1 of the theorem.

---

## 3. Decomposition into permutation factors

Let
\[
d=\max_i d_i(P,Q).
\]
Add \(d-d_i(P,Q)\) formal loops at vertex \(i\). The resulting directed multigraph has indegree and outdegree exactly \(d\) at every active vertex.

Split every vertex into a source copy and a target copy. The arcs then form a \(d\)-regular bipartite multigraph. By repeated application of Hall's theorem, its edges decompose into \(d\) perfect matchings. Equivalently,
\[
D(P,Q)\ \text{together with formal loops}
\]
decomposes into \(d\) permutations
\[
\pi_1,\dots,\pi_d
\]
of the active clusters. Every non-loop arc is an actual labelled item and occurs in exactly one permutation factor. Formal loops merely represent fixed points and are never moved.

If a permutation factor has only one nontrivial cycle, all its actual items can be sent directly to their targets in one polytope edge.

For at most three active clusters, every permutation has at most one nontrivial cycle. Hence all factors can be executed in at most \(d\) moves. Together with the lower bound, this gives
\[
\operatorname{dist}(P,Q)=d
\]
when at most three clusters are active.

---

## 4. Routing permutation factors on four clusters

On four clusters, the only permutation with two nontrivial cycles is a double transposition. Up to relabelling, the three possible types are
\[
A=(12)(34),\qquad
B=(13)(24),\qquad
C=(14)(23).
\]
For example, a factor of type \(A\) consists of the four demanded token moves
\[
1\to2,\quad 2\to1,\quad 3\to4,\quad 4\to3.
\]

A cyclic word such as \((1243)\) denotes the move
\[
1\to2\to4\to3\to1.
\]

The following finite routing lemma is the key point.

### Four-cluster routing lemma

- One double-transposition factor can be routed in two moves.
- Two such factors can be routed in at most three moves.
- Any three such factors can be routed in four moves.

For completeness, explicit certificates follow. In the listed two-step routes, the two transitions are made by the same token. Every transition not listed as part of such a route is traversed directly by a token whose target is the head of that transition.

#### One factor \(A\)

Moves:
\[
C_1=(1234),\qquad C_2=(13).
\]
Two-step routes:
\[
2\xrightarrow{C_1}3\xrightarrow{C_2}1,\qquad
4\xrightarrow{C_1}1\xrightarrow{C_2}3.
\]
The remaining transitions are \(1\to2\) and \(3\to4\).

#### Two equal factors \(AA\)

Moves:
\[
C_1=(1234),\qquad C_2=(1243),\qquad C_3=(134).
\]
Two-step routes:
\[
2\xrightarrow{C_1}3\xrightarrow{C_2}1,
\]
\[
2\xrightarrow{C_2}4\xrightarrow{C_3}1,
\]
\[
4\xrightarrow{C_1}1\xrightarrow{C_3}3.
\]
The remaining transitions, together with these three endpoint demands, are exactly two copies of \(A\).

#### Two distinct factors \(AB\)

They can in fact be routed directly in two moves:
\[
C_1=(1243),\qquad C_2=(1342).
\]
The transitions in these two cycles are precisely the arcs of \(A+B\).

#### Three equal factors \(AAA\)

Moves:
\[
C_1=(1243),\quad
C_2=(1342),\quad
C_3=(1234),\quad
C_4=(1432).
\]
Two-step routes:
\[
2\xrightarrow{C_1}4\xrightarrow{C_3}1,
\qquad
3\xrightarrow{C_1}1\xrightarrow{C_4}4,
\]
\[
1\xrightarrow{C_2}3\xrightarrow{C_4}2,
\qquad
4\xrightarrow{C_2}2\xrightarrow{C_3}3.
\]
These routes contribute one full copy of \(A\); all unpaired transitions contribute two further copies.

#### Two equal and one distinct factor \(AAB\)

Moves:
\[
C_1=(1243),\quad
C_2=(1342),\quad
C_3=(1324),\quad
C_4=(1423).
\]
Two-step routes:
\[
2\xrightarrow{C_1}4\xrightarrow{C_3}1,
\qquad
3\xrightarrow{C_1}1\xrightarrow{C_4}4,
\]
\[
1\xrightarrow{C_2}3\xrightarrow{C_3}2,
\qquad
4\xrightarrow{C_2}2\xrightarrow{C_4}3.
\]
The paired routes form one \(A\), while the unpaired transitions form \(A+B\).

#### Three distinct factors \(ABC\)

Moves:
\[
C_1=(1324),\quad
C_2=(1423),\quad
C_3=(1324),\quad
C_4=(1423).
\]
Two-step routes:
\[
1\xrightarrow{C_1}3\xrightarrow{C_3}2,
\qquad
2\xrightarrow{C_1}4\xrightarrow{C_3}1,
\]
\[
3\xrightarrow{C_2}1\xrightarrow{C_4}4,
\qquad
4\xrightarrow{C_2}2\xrightarrow{C_4}3.
\]
The paired routes form \(A\), and the unpaired transitions form \(B+C\).

All second transitions occur after their corresponding first transitions, so the certificates give genuine token routings. Other items remain untouched.

### Completing the four-cluster bound

Suppose that, among the \(d\) permutation factors, exactly \(r\) are double transpositions. Execute each of the other \(d-r\) factors in one move.

Partition the \(r\) bad factors into triples, with at most two left over. The routing lemma gives a total of
\[
h(r)=\left\lceil\frac{4r}{3}\right\rceil
\]
moves for the bad factors. Hence
\[
\operatorname{dist}(P,Q)
 \le d-r+\left\lceil\frac{4r}{3}\right\rceil
 =d+\left\lceil\frac r3\right\rceil.
\]
Since \(r\le d\),
\[
\operatorname{dist}(P,Q)
 \le d+\left\lceil\frac d3\right\rceil
 =\left\lceil\frac{4d}{3}\right\rceil.
\]
This proves part 3 of the theorem.

Because \(d\le\kappa_1\), for \(n\le4\) this yields
\[
\operatorname{diam}\mathrm{PP}(\kappa_1,\dots,\kappa_n)
 \le \left\lceil\frac{4\kappa_1}{3}\right\rceil.
\]

---

## 5. Exact diameter for at most three clusters

For \(n\le3\), the pairwise formula is
\[
\operatorname{dist}(P,Q)=\max_i|P_i\setminus Q_i|.
\]

For a fixed cluster \(i\), two subsets of size \(\kappa_i\) can differ in at most
\[
\min\{\kappa_i,m-\kappa_i\}
\]
elements. Conversely, this maximum is attained by choosing the two subsets with intersection of minimum possible size and then extending their complements to partitions with the prescribed remaining sizes.

Since \(\kappa_1\ge\kappa_i\),
\[
\max_i\min\{\kappa_i,m-\kappa_i\}
 =\min\{\kappa_1,m-\kappa_1\}.
\]
Therefore
\[
\operatorname{diam}\mathrm{PP}(\kappa_1,\dots,\kappa_n)
 =\min\{\kappa_1,m-\kappa_1\},
 \qquad n\le3.
\]

---

## 6. Exact diameter of \(\mathrm{PP}(K,K,K,K)\)

The four-cluster upper bound gives
\[
\operatorname{diam}\mathrm{PP}(K,K,K,K)
 \le \left\lceil\frac{4K}{3}\right\rceil.
\]

For the reverse inequality, choose \(P,Q\) so that \(Q\) exchanges clusters \(1,2\) and independently exchanges clusters \(3,4\). Thus the discrepancy digraph consists of \(K\) copies of
\[
A=(12)(34).
\]
All \(4K\) items are initially misplaced.

Consider a path of \(q\) polytope edges from \(P\) to \(Q\). Let:

- \(L\) be the total number of item-movements over all \(q\) moves;
- \(s\) be the number of items moved exactly once;
- \(T\) be the number of transitions made between \(1,2\) or between \(3,4\).

Every move is a simple cycle on at most four clusters, so
\[
L\le4q.
\]
Each of the \(4K-s\) other items is moved at least twice, whence
\[
L\ge s+2(4K-s)=8K-s.
\]

An item moved exactly once must move directly from its initial cluster to its target. Hence its transition is one of
\[
1\leftrightarrow2,\qquad 3\leftrightarrow4,
\]
so
\[
s\le T.
\]
A simple cycle on four vertices contains at most two directed transitions belonging to these two disjoint pairs. Therefore
\[
T\le2q.
\]
Combining the inequalities,
\[
4q\ge L\ge8K-s\ge8K-2q,
\]
and consequently
\[
q\ge\frac{4K}{3}.
\]
Thus
\[
\operatorname{dist}(P,Q)\ge
\left\lceil\frac{4K}{3}\right\rceil.
\]
Together with the upper bound,
\[
\boxed{\operatorname{diam}\mathrm{PP}(K,K,K,K)
=\left\lceil\frac{4K}{3}\right\rceil.}
\]

---

## 7. Remaining gap

The argument depends crucially on the fact that a permutation of at most four clusters has either one nontrivial cycle or is a double transposition. With five or more active clusters, a permutation factor may contain more complicated collections of disjoint cycles, and the finite routing lemma above no longer applies.

In particular, this does not prove that arbitrary instances with \(\kappa_1=3\) have diameter at most \(4\), nor does it provide an absolute additive constant for unboundedly many clusters. The original conjecture therefore remains open.