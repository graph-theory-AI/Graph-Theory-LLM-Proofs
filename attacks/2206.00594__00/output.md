```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but polynomiality extends through modular and clique-cutset decompositions, and an explicit dense prime imperfect O2-free family is solved exactly.",
  "would_publish": false,
  "caveats": "General prime, clique-cutset-free, imperfect atoms with unrestricted large bicliques remain untreated."
}
```

# 1. Statement and interpretation

For a graph \(G\), let \(\operatorname{icp}(G)\) be the maximum number of cycles \(C_1,\dots,C_r\) such that

- the cycles are vertex-disjoint, and
- there is no edge between \(V(C_i)\) and \(V(C_j)\) for \(i\neq j\).

Thus \(G\) is \(\mathcal O_k\)-free when \(\operatorname{icp}(G)<k\). Whether the individual cycles are required to be induced is immaterial: every cycle contains a chordless cycle.

As usual, \(k\) is fixed. I do not obtain a proof or counterexample to the full conjecture. I give:

1. an induced-minor reformulation;
2. a polynomial-time subclass obtained by combining the source paper’s sparse case with modular and clique-cutset decompositions;
3. an explicit family of dense, prime, clique-cutset-free, imperfect \(\mathcal O_2\)-free graphs with arbitrarily large bicliques, together with a direct polynomial-time weighted MIS algorithm.

The third item shows that the unresolved dense atoms are genuine: they cannot all be eliminated merely by modular decomposition, clique-cutset decomposition, perfect-graph algorithms, or the source paper’s \(K_{t,t}\)-free theorem.

# 2. Induced-minor reformulation

## Proposition 2.1

A graph \(G\) contains \(k\) pairwise anticomplete cycles if and only if \(kK_3\) is an induced minor of \(G\).

### Proof

Suppose \(C_1,\dots,C_k\) are pairwise anticomplete cycles. Delete all other vertices and contract edges inside each \(C_i\) until it becomes a triangle. Since there were no edges between distinct cycles, the resulting graph is exactly \(kK_3\).

Conversely, suppose \(kK_3\) is an induced minor of \(G\). Consider an induced-minor model by pairwise disjoint connected branch sets. For each triangle component, its three branch sets are pairwise adjacent. Taking one edge between every pair and paths inside the branch sets joining the corresponding endpoints produces a cycle. Branch sets belonging to different triangle components are anticomplete, because induced-minor contractions cannot remove an edge between two final nonadjacent vertices. Hence these \(k\) cycles are pairwise anticomplete. ∎

Thus the conjecture can equivalently be stated as:

> For every fixed \(k\), Maximum Independent Set is polynomial-time solvable on graphs excluding \(kK_3\) as an induced minor.

This reformulation does not by itself yield an algorithm, but it makes clear that the class is induced-minor closed.

# 3. A polynomial decomposition subclass

A set \(M\subseteq V(G)\) is a module if every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is prime if it has no nontrivial module.

Fix \(k,t\ge 2\). Define \(\mathcal D_{k,t}\) to be the class of \(\mathcal O_k\)-free graphs \(G\) such that every prime induced subgraph \(H\) of \(G\) satisfies at least one of:

1. \(H\) is perfect;
2. \(H\) contains no \(K_{t,t}\) as a subgraph.

## Theorem 3.1

For fixed \(k,t\), Maximum Weight Independent Set with rational vertex weights is polynomial-time solvable on \(\mathcal D_{k,t}\).

### Proof

Use the modular decomposition tree of \(G\), processing it bottom-up.

At a node, let \(M_1,\dots,M_q\) be its maximal strong submodules and let \(Q\) be the quotient graph. The graph represented at that node is the substitution
\[
Q(G[M_1],\dots,G[M_q]).
\]

Suppose recursively that
\[
\beta_i=\alpha_w(G[M_i])
\]
has been computed, where the empty stable set is allowed. Then
\[
\alpha_w(G[M])
=
\max\left\{
\sum_{i\in I}\beta_i:
I\text{ is a stable set of }Q
\right\}.
\tag{3.1}
\]
Indeed, the modules met by a stable set form a stable set of \(Q\), and inside each selected module one may independently take an optimum stable set.

If \(Q\) is complete or edgeless, (3.1) is immediate. Otherwise \(Q\) is prime. Choosing one representative from each \(M_i\) realizes \(Q\) as an induced subgraph of \(G\). Therefore \(Q\) is itself \(\mathcal O_k\)-free and, by the definition of \(\mathcal D_{k,t}\), is either perfect or \(K_{t,t}\)-free.

- Weighted independent set is polynomial on perfect graphs.
- In the \(K_{t,t}\)-free case, the source theorem gives treewidth \(O_{k,t}(\log q)\). Standard treewidth dynamic programming solves weighted independent set in
  \[
  2^{O_{k,t}(\log q)}q^{O(1)}=q^{O_{k,t}(1)}
  \]
  time.

There are \(O(n)\) nodes in the modular decomposition tree. Hence the total running time is \(n^{O_{k,t}(1)}\). ∎

The condition defining \(\mathcal D_{k,t}\) is stronger than necessary: the algorithm only needs the prime quotients actually encountered in the modular decomposition to satisfy the dichotomy. The stronger formulation is useful because \(\mathcal D_{k,t}\) is hereditary.

## Clique-cutset extension

The preceding result also propagates through clique-cutset decompositions.

Suppose a graph is assembled from pieces in \(\mathcal D_{k,t}\) along clique adhesions. Root the decomposition tree. For a child side with adhesion clique \(K\), only \(|K|+1\) boundary states are possible:

- no vertex of \(K\) is selected;
- exactly \(v\in K\) is selected.

Let \(f(\bot)\) and \(f(v)\) denote the optimum contribution of the child side, excluding the weight of the adhesion vertices, in those states. The child contributes the constant \(f(\bot)\), and selecting \(v\) in the parent gives the additional bonus
\[
f(v)-f(\bot).
\]
Thus all child contributions can be incorporated into modified vertex weights in the parent piece. Conditioning on no adhesion vertex or on one prescribed adhesion vertex requires only weighted independent-set computations in induced subgraphs of that piece. Since \(\mathcal D_{k,t}\) is hereditary, Theorem 3.1 applies to all of them.

Consequently:

## Corollary 3.2

For fixed \(k,t\), weighted MIS is polynomial-time solvable on graphs admitting a clique-cutset decomposition whose pieces belong to \(\mathcal D_{k,t}\).

This already includes dense graphs outside the source paper’s sparse case.

# 4. A dense modular example

Let
\[
B_m=C_5[\overline K_m,\overline K_m,\overline K_m,\overline K_m,\overline K_m]
\]
be the complete independent blow-up of \(C_5\): its vertex set is partitioned into independent sets \(V_0,\dots,V_4\), each of size \(m\), with \(V_i\) complete to \(V_{i\pm1}\) and anticomplete to the other two parts.

## Proposition 4.1

For every \(m\), \(B_m\) is \(\mathcal O_2\)-free.

### Proof

Every cycle in \(B_m\) contains an edge between two consecutive bags, and hence determines an edge of the base \(C_5\).

Take one such base edge from each of two cycles. Any two edges of \(C_5\) either coincide, share an endpoint, or have adjacent endpoints. In each case, the completeness between consecutive bags gives an edge between the two cycles. Thus two cycles cannot be anticomplete. ∎

The graph \(B_m\) contains \(K_{m,m}\), so it is not covered by any fixed \(K_{t,t}\)-free hypothesis once \(m\ge t\). Nevertheless it belongs to \(\mathcal D_{2,2}\): two vertices in one bag are twins, so a prime induced subgraph uses at most one vertex per bag and is therefore an induced subgraph of \(C_5\), hence \(K_{2,2}\)-free.

This shows that modular decomposition gives a genuine extension of the sparse result. It also covers, for example, all split graphs: every cycle in a split graph contains at least two vertices of the clique, so split graphs are \(\mathcal O_2\)-free, and they are perfect.

# 5. A dense prime imperfect family

The previous example is highly modular. The following “punctured blow-up” removes that explanation.

For \(m\ge5\), define \(P_m\) with
\[
V(P_m)=\{v_i^a:i\in\mathbb Z_5,\ a\in[m]\}.
\]
The five sets
\[
V_i=\{v_i^a:a\in[m]\}
\]
are independent, there are no edges between nonconsecutive parts, and
\[
v_i^a v_{i+1}^b\in E(P_m)
\quad\Longleftrightarrow\quad
a\neq b.
\tag{5.1}
\]
Thus every consecutive pair induces \(K_{m,m}\) minus a perfect matching.

## Proposition 5.1

For every \(m\ge5\), \(P_m\) has all of the following properties:

1. \(P_m\) is \(\mathcal O_2\)-free;
2. \(P_m\) is prime;
3. \(P_m\) has no clique cutset;
4. \(P_m\) is imperfect;
5. \(P_m\) contains \(K_{t,t}\) whenever \(m\ge2t\);
6. \(\alpha(P_m)=2m\);
7. Maximum Weight Independent Set with nonnegative weights is polynomial-time solvable on the family \(\{P_m:m\ge5\}\).

### Proof of \(\mathcal O_2\)-freeness

For a cycle \(C\), put
\[
A_i=V(C)\cap V_i
\]
and let \(S(C)=\{i:A_i\neq\varnothing\}\). Since \(C\) is connected, \(S(C)\) is connected in the base \(C_5\), and it contains an edge.

A basic consequence of (5.1) is:

\[
X\subseteq V_i,\quad Y\subseteq V_{i+1},\quad
X,Y\neq\varnothing,\quad E(X,Y)=\varnothing
\]
implies that \(X\) and \(Y\) are singletons with the same label.
\(\tag{5.2}\)

Suppose cycles \(C,D\) are anticomplete, and write \(B_i=V(D)\cap V_i\).

First suppose \(S(C)\) is a proper connected subset of \(C_5\), hence a path.

- If \(|S(C)|=2\), both bags contain at least two vertices of \(C\). By (5.2), \(D\) avoids all four base vertices neighboring these two bags, leaving only one possible bag, which cannot support a cycle.
- If \(|S(C)|=3\), the middle bag contains at least two vertices of \(C\). Indeed, otherwise its unique vertex would separate the two end bags on the cycle. Hence \(D\) avoids the two end bags. Its only possible cyclic support is the opposite base edge, on which it has at least two vertices in each bag. This contradicts (5.2) with either end bag of \(C\).
- If \(|S(C)|=4\), each of the two internal bags contains at least two vertices of \(C\). Consequently \(D\) is confined to the remaining single bag, again impossible.

Thus both cycles must meet all five bags. By (5.2), every \(A_i\) and \(B_i\) is a singleton. Let their labels be \(a_i,b_i\). Anticompleteness gives
\[
a_i=b_{i+1}=b_{i-1}
\]
for every \(i\). Hence \(b_{i+1}=b_{i-1}\); because addition by \(2\) generates \(\mathbb Z_5\), all \(b_i\), and therefore all \(a_i\), are equal. But then consecutive vertices of \(C\) are nonadjacent by (5.1), a contradiction. Therefore \(P_m\) is \(\mathcal O_2\)-free.

### Proof that \(P_m\) is prime

Let \(M\) be a module.

Suppose \(M\) contains \(v_i^a,v_i^b\) with \(a\neq b\). The vertex \(v_{i+1}^a\) distinguishes them, so it also lies in \(M\). Now \(v_i^a,v_{i+1}^a\in M\). For every \(c\neq a\), the vertex \(v_{i+1}^c\) is adjacent to \(v_i^a\) and nonadjacent to \(v_{i+1}^a\), so \(V_{i+1}\subseteq M\). Every vertex in either neighboring part has mixed adjacency to \(V_{i+1}\), and therefore must also belong to \(M\). Propagating around the \(5\)-cycle gives \(M=V(P_m)\).

Now suppose \(M\) contains vertices from distinct parts \(V_i,V_j\). The open neighborhoods of \(i\) and \(j\) in the base \(C_5\) are distinct, so choose
\[
r\in N_{C_5}(i)\setminus N_{C_5}(j).
\]
All but at most one vertex of \(V_r\) distinguish the two chosen vertices. Since \(m\ge5\), at least two vertices of \(V_r\) belong to \(M\), and the previous paragraph again gives \(M=V(P_m)\).

Thus every proper module is a singleton.

### No clique cutset

The graph is triangle-free, so every clique has size at most two. After deleting at most two vertices, each \(V_i\) still has at least three vertices. Between every two consecutive surviving parts the graph is a complete bipartite graph minus a partial matching and is connected. These five connected bipartite graphs overlap cyclically in nonempty parts, so the remaining graph is connected. Hence there is no clique cutset.

### Imperfection and large bicliques

Choosing five distinct labels, one in each part, gives an induced \(C_5\), so \(P_m\) is not perfect.

For consecutive parts \(V_i,V_{i+1}\), choose disjoint label sets \(A,B\subseteq[m]\) with \(|A|=|B|=t\). The corresponding vertices induce a \(K_{t,t}\). Thus \(P_m\) contains \(K_{t,t}\) whenever \(m\ge2t\).

### Independence number

For an independent set \(I\), let \(I_i=I\cap V_i\). If \(|I_i|\ge2\), then \(I_{i-1}=I_{i+1}=\varnothing\), since a vertex in an adjacent part is nonadjacent to at most one vertex of \(V_i\).

Call \(i\) large when \(|I_i|\ge2\). The large indices form a stable set of the base \(C_5\), so there are at most two.

- With two large parts, all other parts are empty, giving at most \(2m\) vertices.
- With one large part, the two remaining possible parts are consecutive and each contributes at most one vertex, giving at most \(m+2\le2m\).
- With no large part, \(|I|\le5\le2m\).

Conversely, the union of any two nonconsecutive parts is independent and has size \(2m\). Hence
\[
\alpha(P_m)=2m.
\]

### Weighted algorithm

The five parts can be recovered in polynomial time from the graph. For distinct nonadjacent vertices \(x,y\), in a promised \(P_m\),

\[
|N(x)\cap N(y)|=
\begin{cases}
2m-4,&x,y\text{ lie in the same }V_i,\\
m-1\text{ or }m-2,&\text{their base positions have distance }2,\\
0,&\text{they are the matched nonedge in consecutive parts}.
\end{cases}
\]

For \(m\ge5\), these values distinguish the first case. Thus the equivalence classes determined by
\[
x\equiv y
\quad\Longleftrightarrow\quad
x=y\ \text{or}\ 
\bigl(xy\notin E,\ |N(x)\cap N(y)|=2m-4\bigr)
\]
are exactly \(V_0,\dots,V_4\). One can then verify the cyclic order and the five missing perfect matchings in polynomial time.

For optimization, enumerate the set \(L\subseteq\mathbb Z_5\) of parts containing at least two selected vertices. It is an independent set of \(C_5\), so there are only eleven possibilities. For \(i\in L\), both neighboring parts are empty; with nonnegative weights it is optimal to take all of \(V_i\). In every remaining part, enumerate either no vertex or one vertex. There are at most
\[
11(m+1)^5=n^{O(1)}
\]
possibilities, and each can be checked directly. This gives a polynomial-time weighted algorithm. ∎

For \(m\ge2t\), the graph \(P_m\) is itself a prime induced subgraph that is neither perfect nor \(K_{t,t}\)-free. It is also clique-cutset-free. Thus Theorem 3.1 and its clique-cutset extension do not cover \(P_m\); its direct algorithm uses the much more rigid “complete minus a matching” structure.

# 6. Remaining gap

The conjecture would follow from a polynomial-time treatment of arbitrary prime, clique-cutset-free, imperfect \(\mathcal O_k\)-free graphs containing large \(K_{t,t}\)'s. The family \(P_m\) shows that these atoms exist already for \(k=2\), can have linear treewidth-type density, and need not be modular blow-ups.

What is missing is a structural theorem saying that every such dense atom admits a tractable description generalizing the co-matching structure of \(P_m\), or an algorithm that handles large bicliques without exponential branching over their two sides. Nothing above establishes such a theorem. Therefore the full conjecture remains unresolved.