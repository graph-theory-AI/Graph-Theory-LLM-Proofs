```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For each fixed r, there is a division-free polynomial-time MWIS algorithm for C4-free perfect graphs whose triangles can be hit by the union of r cliques.",
  "would_publish": false,
  "caveats": "This is an elementary restricted result, with no novelty claim; the parameter is unbounded even in connected, clique-cutset-free examples of maximum degree three."
}
```

## 1. Restricted result

I do not obtain a combinatorial algorithm for all perfect graphs, or for all \(C_4\)-free perfect graphs. The following restricted algorithm is self-contained. Importantly, its exceptional cliques need not be supplied with the input.

Throughout, \(C_4\)-free means **having no induced cycle of length four**. Graphs are finite and simple, and vertex weights are nonnegative integers encoded in binary.

Define
\[
\kappa(G)=\min\left\{r:\begin{array}{l}
\text{there are cliques }K_1,\ldots,K_r\text{ such that}\\
G-\bigcup_{i=1}^rK_i\text{ is bipartite}
\end{array}\right\}.
\]
The cliques may overlap.

If \(G\) is perfect, then
\[
\kappa(G)=
\min\left\{r:\text{the union of }r\text{ cliques meets every triangle of }G\right\}.
\tag{1}
\]
Indeed, an induced subgraph of a perfect graph is perfect; if it is triangle-free, its clique number, and hence its chromatic number, is at most two. The converse is immediate.

### Theorem
For every fixed nonnegative integer \(r\), there is a combinatorial polynomial-time algorithm which, on a \(C_4\)-free graph \(G\),

1. determines whether \(\kappa(G)\le r\); and
2. if so, finds a maximum-weight independent set.

No collection \(K_1,\ldots,K_r\) needs to be given. For \(n\ge2\), one implementation uses
\[
O\!\left(n^5+n^{2r+2}+(n+1)^r n^5\right)
\tag{2}
\]
graph operations and integer additions, subtractions, and comparisons. Its bit complexity is polynomial in the input length for fixed \(r\).

Thus, by (1), the theorem applies to \(C_4\)-free perfect graphs whose triangles can be hit by a fixed number of cliques. The theorem actually holds without perfection when formulated using \(\kappa\).

## 2. Enumerating the maximal cliques

The useful consequence of excluding \(C_4\) is that all maximal cliques can be listed in polynomial time.

### Lemma
An \(n\)-vertex \(C_4\)-free graph, with \(n\ge1\), has at most
\[
1+\binom n2
\]
maximal cliques. They can be listed combinatorially in \(O(n^5)\) time.

### Proof

First observe that, whenever \(v,w\) are nonadjacent,
\[
N(v)\cap N(w)\quad\text{is a clique}.
\tag{3}
\]
Otherwise, two nonadjacent common neighbors, together with \(v,w\), induce a \(C_4\).

Fix a vertex \(v\), and put \(G'=G-v\). Every maximal clique \(K\) of \(G'\) produces a maximal clique of \(G\):
\[
K\longmapsto
\begin{cases}
K\cup\{v\},&K\subseteq N(v),\\
K,&K\not\subseteq N(v).
\end{cases}
\tag{4}
\]
The resulting cliques are distinct.

Consider a maximal clique \(L\) of \(G\) not obtained this way. It must contain \(v\), and
\[
S=L-\{v\}
\]
cannot be maximal in \(G'\). Thus some \(w\in V(G')\setminus S\) is complete to \(S\). Necessarily \(vw\notin E(G)\), since otherwise \(w\) would extend \(L\).

Now
\[
S\subseteq N(v)\cap N(w).
\]
By (3), the right-hand side is a clique. Its vertices, together with \(v\), form a clique containing \(L\). Maximality of \(L\) therefore gives
\[
L=\{v\}\cup\bigl(N(v)\cap N(w)\bigr).
\tag{5}
\]
There are at most \(n-1\) possible choices of \(w\). Consequently, if \(q(G)\) denotes the number of maximal cliques,
\[
q(G)\le q(G-v)+(n-1).
\]
Starting with \(q(K_1)=1\) proves the bound.

The proof gives an explicit listing algorithm. Insert the vertices one at a time. At each insertion of \(v\):

* update the old maximal cliques according to (4);
* for every earlier nonneighbor \(w\) of \(v\), form the candidate in (5);
* test each candidate for maximality and discard duplicates.

With an adjacency matrix and explicit vertex-set representations, the polynomial bound on the list size gives an \(O(n^5)\) implementation. For example, at a stage with \(i\) vertices, there are \(O(i^2)\) old cliques and at most \(i-1\) additional candidates. Comparing each additional candidate against the current list takes \(O(i^3)\) time, so the stage takes \(O(i^4)\) time. Summing over the stages gives the claimed bound. ∎

### A direct consequence

Maximum Clique and Maximum Weight Clique have combinatorial polynomial-time algorithms on **all** \(C_4\)-free graphs: enumerate the maximal cliques and choose the best one.

This does not solve MIS on \(C_4\)-free perfect graphs. The restricted class is not closed under complementation; for example,
\[
\overline{2K_2}=C_4.
\]

## 3. Finding the exceptional cliques

Let \(\mathcal C\) be the list of maximal cliques from the lemma. Add the empty set as a dummy choice.

Enumerate all ordered \(r\)-tuples
\[
(K_1,\ldots,K_r)\in(\mathcal C\cup\{\varnothing\})^r.
\]
For each tuple, set
\[
U=\bigcup_{i=1}^rK_i
\]
and test whether \(G-U\) is bipartite.

This search is complete. If arbitrary cliques \(K'_1,\ldots,K'_s\), with \(s\le r\), witness \(\kappa(G)\le r\), enlarge every nonempty \(K'_i\) to a maximal clique \(K_i\). Removing more vertices preserves bipartiteness. The resulting collection, padded with empty choices, occurs in the enumeration.

Since \(|\mathcal C|=O(n^2)\), the search takes
\[
O(n^{2r+2})
\]
time for fixed \(r\), using an \(O(n^2)\) bipartiteness test.

Once one suitable tuple is found, the search stops. We do **not** need to run the optimization algorithm for every tuple.

For \(r=0\), this step is simply a bipartiteness test. Empty graphs are handled separately.

## 4. Optimizing after the cliques have been found

Suppose that cliques \(K_1,\ldots,K_r\) have been found such that
\[
B=G-U,\qquad U=\bigcup_iK_i,
\]
is bipartite.

Every independent set contains at most one vertex of each \(K_i\). Enumerate the tuples
\[
a_i\in K_i\cup\{\bot\},\qquad i=1,\ldots,r.
\]
For a tuple, let \(T\) be the set of its non-\(\bot\) entries; repeated entries are included only once. Discard the tuple unless \(T\) is independent.

For every surviving \(T\), solve MWIS in
\[
H_T=G-\bigl(U\cup N_G(T)\bigr).
\tag{6}
\]
This is an induced subgraph of \(B\), so it is bipartite. The candidate value is
\[
w(T)+\alpha_w(H_T).
\tag{7}
\]

There are at most
\[
\prod_{i=1}^r(|K_i|+1)\le(n+1)^r
\]
tuples.

### Correctness

Every candidate in (7) is feasible: an independent set of \(H_T\) is disjoint from and anticomplete to \(T\).

Conversely, let \(I\) be any independent set of \(G\), and put \(T=I\cap U\). For each \(i\), the intersection \(I\cap K_i\) is either empty or a singleton. Choosing those singleton vertices, and \(\bot\) otherwise, produces exactly \(T\), even when the cliques overlap.

Moreover,
\[
I-U\subseteq V(H_T).
\]
It follows that
\[
w(I)\le w(T)+\alpha_w(H_T).
\]
Thus maximizing (7) over the enumeration gives precisely \(\alpha_w(G)\), and retaining the corresponding sets recovers an optimum independent set.

## 5. The bipartite subroutine uses no division

For completeness, the required weighted bipartite optimization is a minimum-cut computation.

Let \(H\) have bipartition \((A,B)\), and put
\[
W=\sum_{v\in V(H)}w(v),\qquad M=W+1.
\]
Construct the directed network with arcs

* \(s\to a\), of capacity \(w(a)\), for \(a\in A\);
* \(b\to t\), of capacity \(w(b)\), for \(b\in B\);
* \(a\to b\), of capacity \(M\), for every edge \(ab\in E(H)\).

There is a cut of capacity at most \(W\), so no minimum cut crosses an arc of capacity \(M\).

If \(X\) is the source side of a minimum cut, then
\[
C=(A\setminus X)\cup(B\cap X)
\]
is a vertex cover: if \(a\in A\cap X\) and \(ab\) is an edge, then \(b\in X\), since otherwise the cut would cross an \(M\)-capacity arc. The cut capacity equals \(w(C)\).

Conversely, a vertex cover \(C\) gives the cut with source side
\[
\{s\}\cup(A\setminus C)\cup(B\cap C),
\]
of capacity \(w(C)\). Therefore
\[
\alpha_w(H)=W-\operatorname{mincut}.
\]

A shortest-augmenting-path maximum-flow algorithm uses
\[
O(|V|\,|E|^2)=O(n^5)
\]
arithmetic operations here, independently of the numerical capacity values. It uses only integer addition, subtraction, comparison, and graph traversal.

If the input weights have at most \(b\) bits, the capacities and residual capacities have \(O(b+\log n)\) bits. Thus this is polynomial in the binary input length, rather than merely pseudopolynomial.

Combining this subroutine with Sections 2–4 proves the theorem and the bound (2).

## 6. Why this does not cover the full \(C_4\)-free perfect class

The obstruction is not just that disconnected graphs can contain arbitrarily many triangles. The parameter \(\kappa\) is unbounded even after excluding clique cutsets and bounding the maximum degree by three.

### Proposition
There are connected, \(C_4\)-free perfect graphs \(G\) of maximum degree three, with no clique cutset, for which \(\kappa(G)\) is arbitrarily large.

### Construction and proof

Take a two-connected cubic bipartite graph \(Q\). Such graphs have arbitrarily many vertices; one explicit family is
\[
Q=C_{2t}\mathbin{\square}K_2,\qquad t\ge2.
\]
Replace every edge of \(Q\) by a path of length three, obtaining \(H\), and let
\[
G=L(H)
\]
be its line graph.

#### The graph is \(C_4\)-free and perfect

The graph \(H\) is bipartite and has girth at least twelve. An induced four-cycle in \(L(H)\) would correspond to a four-cycle in \(H\): its four edge-vertices represent consecutively incident edges, while opposite edges are disjoint. Thus \(G\) is \(C_4\)-free.

For every edge set \(F\subseteq E(H)\),
\[
G[F]=L(H_F),
\]
where \(H_F=(V(H),F)\) is bipartite. By the bipartite edge-coloring theorem,
\[
\chi(L(H_F))=\chi'(H_F)=\Delta(H_F).
\]
Since \(H_F\) is triangle-free, a clique in its line graph consists of edges sharing an endpoint, so
\[
\omega(L(H_F))=\Delta(H_F).
\]
Hence every induced subgraph of \(G\) satisfies \(\chi=\omega\), proving perfection.

Also, an edge of \(H\) has endpoint degrees either \(3,2\) or \(2,2\). Its corresponding vertex in \(G\) consequently has degree three or two.

#### The parameter is large

For each original vertex \(v\in V(Q)\), the three edges of \(H\) incident with \(v\) give a triangle \(T_v\) in \(G\).

The triangles \(T_v\) are pairwise anticomplete. Indeed, the two subdivisions on every original edge ensure that edges incident with different original vertices do not share an endpoint in \(H\). Consequently, a clique of \(G\) can meet at most one of these triangles.

By (1), every collection witnessing \(\kappa(G)\) must meet each \(T_v\). Therefore
\[
\kappa(G)\ge |V(Q)|.
\]
Conversely, delete the union of all the \(T_v\). What remains consists of the vertices of \(L(H)\) corresponding to the middle edges of the subdivided paths. Those edges form a matching in \(H\), so the remaining graph is independent. Thus
\[
\boxed{\kappa(G)=|V(Q)|.}
\tag{8}
\]

#### There is no clique cutset

Subdividing edges preserves two-connectivity, so \(H\) is two-connected.

Because \(H\) is triangle-free, every clique \(K\) of \(L(H)\) corresponds to an edge set contained in the star of some vertex \(u\in V(H)\). The edges of \(H-u\) induce a connected subgraph of \(G-K\). Every remaining edge incident with \(u\) attaches to this subgraph: its other endpoint has another incident edge because \(H\) has minimum degree two.

Hence \(G-K\) is connected for every clique \(K\), proving that \(G\) has no clique cutset. ∎

These examples are not hard instances of MWIS: being line graphs, they can be handled through maximum-weight matching. Their purpose is narrower—they show that the parameter in the theorem cannot be bounded throughout the target class, even after elementary clique-cutset decomposition.

## 7. The remaining gap

The algorithm has running time \(n^{O(r)}\). It is polynomial for every fixed \(r\), but not a polynomial-time algorithm when \(r=\kappa(G)\) is unrestricted.

The maximal-clique enumeration also does not finish the problem. It makes all clique inequalities explicitly available, but it does not supply a combinatorial optimizer for their associated packing problem. Invoking a general linear-programming algorithm at that point would abandon the requested approach.

Thus the results established here are:

* combinatorial polynomial-time MC and MWC on all induced-\(C_4\)-free graphs;
* combinatorial polynomial-time MWIS when a fixed number of cliques can be deleted to leave a bipartite graph, with those cliques found automatically;
* an explicit demonstration that this restriction remains substantial within \(C_4\)-free perfect graphs.

No algorithm for unrestricted MIS/MWIS on \(C_4\)-free perfect graphs, or for the full perfect-graph problem, is obtained.