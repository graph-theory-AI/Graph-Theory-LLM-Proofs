```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Minimum degree six suffices at girth at least five, and any counterexample to the original conjecture must have at least 20 degree-seven vertices contained in no K_5 subgraph.",
  "would_publish": false,
  "caveats": "These are special cases and structural restrictions, not a resolution of either conjecture; they use Mader's established extremal bound, and no novelty claim is made."
}
```

## Scope of the results

All graphs below are finite and simple. I do not resolve either unrestricted conjecture. I prove the following partial results.

**Theorem A.** Every graph of girth at least five and minimum degree at least six contains a \(K_6\)-minor.

**Theorem B.** Every bipartite graph with no \(4\)-cycle and minimum degree at least five contains a \(K_6\)-minor.

**Theorem C.** Suppose \(G\) is \(K_6\)-minor-free and \(\delta(G)\ge 7\). Then at least \(20\) vertices of \(G\) have degree exactly seven and belong to no \(K_5\) subgraph.

Theorem C gives another special case of the conjecture:

**Corollary.** Suppose \(\delta(G)\ge7\), and all but at most \(19\) degree-seven vertices have neighborhoods coverable by two cliques. Then \(G\) contains a \(K_6\)-minor.

In particular, the conjecture holds for **quasi-line graphs**, meaning graphs in which every vertex’s neighborhood is coverable by two cliques. This includes line graphs. The corollary places no restriction on the neighborhoods of vertices of degree at least eight.

## 1. The extremal input

I use the classical Mader bound
\[
|E(H)|\le 4|V(H)|-10
\tag{1}
\]
for every \(K_6\)-minor-free simple graph \(H\) with at least four vertices. The four-vertex case is immediate; the remaining cases are the standard extremal theorem for \(K_6\)-minors.

Consequently, finding a minor \(H\) with at least four vertices and
\[
|E(H)|>4|V(H)|-10
\]
certifies a \(K_6\)-minor.

## 2. Matching contraction: proof of Theorem A

Let \(G\) have girth at least five. Write
\[
n=|V(G)|,\qquad m=|E(G)|,
\]
and choose a maximum matching \(M\), of size \(k\).

Contract every edge of \(M\), and call the resulting graph \(J\). After removing the contracted edges, no parallel edges arise:

- Parallel edges between a contracted pair and an uncontracted vertex would give a triangle in \(G\).
- Parallel edges between two contracted pairs would give a triangle or a \(4\)-cycle in \(G\).

Therefore
\[
|V(J)|=n-k,\qquad |E(J)|=m-k.
\tag{2}
\]

The main point is that a maximum matching also gives useful degree information.

Let \(U\) be the unmatched vertices, and let \(W=V(G)\setminus U\). Thus
\[
|U|=n-2k,\qquad |W|=2k.
\]
The set \(U\) is independent.

Moreover, for each matched edge \(xy\), at most one of \(x,y\) has a neighbor in \(U\). Indeed, if both do, then either they have a common neighbor in \(U\), giving a triangle, or there are distinct \(u,v\in U\) with edges \(ux,yv\). In the latter case, replacing \(xy\) by \(ux,yv\) enlarges the matching.

We may consequently partition \(W=X\cup Y\), with \(|X|=|Y|=k\), so that:

- every matching edge joins \(X\) to \(Y\);
- no vertex of \(Y\) has a neighbor in \(U\).

If \(\delta(G)\ge d\), every vertex of \(Y\) has at least \(d\) neighbors in \(W\), while every vertex of \(X\) has at least its matching partner in \(W\). Hence
\[
2|E(G[W])|\ge (d+1)k.
\]
Also, since \(U\) is independent,
\[
|E(U,W)|\ge d(n-2k).
\]
It follows that
\[
m\ge dn-\frac{3d-1}{2}k.
\tag{3}
\]
Of course, the minimum-degree assumption also gives
\[
m\ge \frac{dn}{2}.
\tag{4}
\]

Now take \(d=6\). Equations (3) and (4) give
\[
m\ge 6n-\frac{17}{2}k,
\qquad
m\ge3n.
\]
Multiplying the latter inequality by seven and the former by four yields
\[
11m\ge45n-34k.
\]
Thus, by (2),
\[
11|E(J)|
=11(m-k)
\ge45(n-k)
=45|V(J)|.
\]
In particular,
\[
\frac{2|E(J)|}{|V(J)|}\ge\frac{90}{11}>8.
\tag{5}
\]

Because \(\delta(G)\ge6\), we have \(n\ge7\), and therefore
\[
|V(J)|=n-k\ge\lceil n/2\rceil\ge4.
\]
Equation (5) contradicts (1) if \(J\), and hence \(G\), is \(K_6\)-minor-free. This proves Theorem A. \(\square\)

The argument gives an explicit density certificate: contracting a maximum matching produces a simple minor of average degree at least \(90/11\).

## 3. The bipartite improvement: proof of Theorem B

Let \(G\) be bipartite, contain no \(4\)-cycle, and satisfy \(\delta(G)\ge5\). Again choose a maximum matching \(M\) of size \(k\).

By König’s matching–vertex-cover theorem, \(G\) has a vertex cover \(Z\) with \(|Z|=k\). Since \(V(G)\setminus Z\) is independent,
\[
m\ge \sum_{v\notin Z}d_G(v)\ge5(n-k).
\tag{6}
\]

Bipartiteness excludes triangles, so the absence of \(4\)-cycles allows the same matching contraction as above:
\[
|V(J)|=n-k,\qquad |E(J)|=m-k.
\]
Using \(k\le n/2\), equation (6) gives
\[
\begin{aligned}
|E(J)|
&\ge5(n-k)-k\\
&=4(n-k)+(n-2k)\\
&\ge4|V(J)|.
\end{aligned}
\]
Here \(n\ge10\), so \(J\) has at least five vertices. This contradicts (1) if \(G\) is \(K_6\)-minor-free. Theorem B follows. \(\square\)

This proof does not use the recent minimum-degree-six theorem for general bipartite graphs quoted in the question; the additional exclusion of \(4\)-cycles makes the matching argument sufficient.

## 4. Localizing the degree-seven obstruction

The usual edge count already shows that a \(K_6\)-minor-free graph of minimum degree seven must have at least \(20\) degree-seven vertices. Theorem C strengthens this: at least \(20\) must lie in no \(K_5\) subgraph.

### 4.1 Clique separators and \(K_5\) subgraphs

A **clique separator** is a clique whose deletion leaves at least two nonempty components.

We first record an elementary fact.

**Lemma 1.** Let \(H\) be connected and \(K_6\)-minor-free, and suppose \(H\) has no clique separator. Then either \(H=K_5\) or \(\omega(H)\le4\).

**Proof.** Suppose \(Q\) is a \(5\)-clique and \(H\ne Q\). Choose a component \(R\) of \(H-Q\). Its neighborhood lies in \(Q\).

If \(N_H(R)=Q\), contracting the connected set \(R\) to one vertex produces a \(K_6\) on that vertex and \(Q\).

Otherwise, \(N_H(R)\) is a proper subset of \(Q\). It is a clique separator, separating \(R\) from the nonempty set \(Q\setminus N_H(R)\). Both alternatives are impossible. \(\square\)

### 4.2 Passing to an end piece without losing degrees

Suppose now that \(G\) is connected, \(K_6\)-minor-free, and \(\delta(G)\ge7\). Let \(S\) be a clique separator, and let \(A\) be a component of \(G-S\).

We can find an induced subgraph
\[
H=G[C\cup T]
\]
such that:

1. \(\varnothing\ne C\subseteq A\);
2. \(T\) is a clique;
3. every neighbor in \(G\) of a vertex of \(C\) lies in \(C\cup T\);
4. \(H\) is connected and has no clique separator.

Here is the reduction establishing this. Start with
\[
H=G[A\cup S],\qquad C=A,\qquad T=S.
\]
If the current \(H\) has a clique separator \(R\), the clique \(T\setminus R\) meets at most one component of \(H-R\). Choose another component \(D\), which is disjoint from \(T\), and replace
\[
(H,C,T)
\quad\text{by}\quad
\bigl(H[D\cup R],D,R\bigr).
\]
The new private set \(D\) is contained in the old private set \(C\). Since \(D\) is a component of \(H-R\), all its neighbors remain in the new graph. Thus properties 1–3 persist. The order strictly decreases, so the process terminates.

In particular,
\[
d_H(v)=d_G(v)\ge7\qquad(v\in C).
\tag{7}
\]
Therefore \(H\ne K_5\), and Lemma 1 gives
\[
\omega(H)\le4,\qquad |T|\le4.
\tag{8}
\]

Furthermore, **every vertex of \(C\) belongs to no \(K_5\) subgraph of \(G\)**. If such a clique contained \(v\in C\), all its vertices would be neighbors of \(v\) or \(v\) itself, and hence would lie in \(H\), contradicting (8).

### 4.3 Each end piece supplies at least ten such vertices

Put
\[
c=|C|,\qquad s=|T|\le4,
\]
and let \(a\) be the number of vertices in \(C\) whose degree in \(G\) is seven.

By (7), all other vertices of \(C\) have degree at least eight, so
\[
\sum_{v\in C}d_H(v)\ge8c-a.
\tag{9}
\]
Also, a vertex of \(C\) has degree at least seven in a graph of order \(c+s\), giving
\[
c\ge8-s\ge4.
\]
Thus (1) applies both to \(H\) and to \(G[C]\).

Because \(T\) is a clique,
\[
\sum_{v\in C}d_H(v)
=|E(H)|+|E(G[C])|-\binom{s}{2}.
\]
Using (1),
\[
\sum_{v\in C}d_H(v)
\le8c+4s-20-\binom{s}{2}.
\]
Together with (9), this implies
\[
a\ge20-4s+\binom{s}{2}.
\tag{10}
\]
For \(s=0,1,2,3,4\), the right side is respectively
\[
20,\ 16,\ 13,\ 11,\ 10.
\]
Consequently, each such end piece supplies at least ten degree-seven vertices that belong to no \(K_5\) subgraph of \(G\).

### 4.4 Completing the proof of Theorem C

We may assume \(G\) is connected: otherwise, work in any component, where degrees and membership in \(K_5\) subgraphs are unchanged.

There are two cases.

**Case 1: \(G\) has no clique separator.**  
Lemma 1 and \(\delta(G)\ge7\) give \(\omega(G)\le4\). Let \(a\) be the number of degree-seven vertices. Then
\[
8|V(G)|-a
\le2|E(G)|
\le8|V(G)|-20.
\]
Hence \(a\ge20\), and every one of these vertices belongs to no \(K_5\).

**Case 2: \(G\) has a clique separator \(S\).**  
Choose two distinct components \(A,B\) of \(G-S\). Apply the end-piece reduction separately inside \(A\cup S\) and \(B\cup S\). Equation (10) supplies at least ten qualifying vertices in each component.

The two sets are disjoint, so there are at least twenty altogether. In fact, they are **anticomplete** to each other, since they lie in different components of \(G-S\).

This proves Theorem C. \(\square\)

## 5. The locally clique-covered special case

Suppose \(v\) has degree seven and \(N_G(v)\) is covered by two cliques. At least one of those cliques has at least four vertices. Adding \(v\) to four of them gives a \(K_5\) subgraph containing \(v\).

Thus every degree-seven vertex that belongs to no \(K_5\) must be among the vertices whose neighborhoods are not coverable by two cliques. If there are at most nineteen such exceptions, Theorem C excludes a \(K_6\)-minor-free graph of minimum degree seven.

This proves the stated corollary, including the quasi-line and line-graph cases. It also proves the seven-connected conjecture within those classes, since seven-connectivity implies minimum degree at least seven.

## 6. What remains unresolved

The arguments cover two different local regimes:

- With no triangles or \(4\)-cycles, matching contraction raises density enough to force the minor.
- When degree-seven neighborhoods contain sufficiently large cliques, clique-separator reduction and the extremal bound force the minor.

Neither regime covers all graphs of minimum degree seven.

The precise failure of the matching argument in general is that triangles and \(4\)-cycles can produce parallel edges after contraction. Simplifying the resulting minor then loses additional edges, invalidating the density calculation. Theorem C, meanwhile, supplies a necessary configuration—twenty degree-seven vertices outside all \(K_5\) subgraphs—but does not rule that configuration out.

For comparison, degree six cannot suffice without additional hypotheses: adjoining a universal vertex to the planar, \(5\)-regular icosahedral graph gives an apex graph of minimum degree six. It is \(K_6\)-minor-free, since apex graphs are minor-closed and \(K_6\) is not apex.

Accordingly, these are rigorous special cases and counterexample restrictions, not a proof or disproof of either unrestricted conjecture. No claim is made that these deductions are new in the literature.