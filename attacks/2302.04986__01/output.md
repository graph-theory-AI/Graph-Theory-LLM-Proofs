```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it reduces exactly to a weighted transversal problem on prime P_t-free graphs, with explicit bounds for perfect atoms and triangle-free atoms of bounded induced biclique number.",
  "would_publish": false,
  "caveats": "No bound is obtained for general non-perfect prime atoms containing arbitrarily large induced bicliques; literature novelty of the reductions was not checked."
}
```

# Statement and outcome

For a finite nonempty graph \(G\), let \(\mathcal M(G)\) be the family of its maximum stable sets, and let
\[
\eta(G)=\min\{|X|:X\cap S\neq\varnothing\text{ for every }S\in\mathcal M(G)\}.
\]
The conjecture asks whether, for every fixed \(t\ge 6\), there is a function \(h_t\) such that
\[
\eta(G)\le h_t(\omega(G))
\]
for every \(P_t\)-free graph \(G\).

I do not prove or disprove this. I give:

1. an exact reduction to the weighted problem on prime graphs;
2. a weighted bound for perfect graphs;
3. an explicit weighted bound for triangle-free \(P_t\)-free graphs with bounded induced \(K_{2,s}\);
4. consequent \(\eta\)-bounded subclasses, including a modularly closed one;
5. a separate bound in terms of induced odd-cycle packing.

All paths and forbidden subgraphs below are induced unless stated otherwise.

---

# 1. Basic facts about \(\eta\)

It is useful to observe that
\[
\eta(G)=\min\{|X|:\alpha(G-X)<\alpha(G)\}. \tag{1}
\]
Indeed, \(X\) misses some maximum stable set exactly when that set survives in \(G-X\).

Consequently, for every \(Z\subseteq V(G)\),
\[
\eta(G)\le |Z|+\eta(G-Z), \tag{2}
\]
with the following interpretation. If \(\alpha(G-Z)<\alpha(G)\), then \(Z\) itself is a transversal. Otherwise, a transversal of the maximum stable sets of \(G-Z\), together with \(Z\), hits every maximum stable set of \(G\).

Also, for every vertex \(v\),
\[
\eta(G)\le |N[v]|=\deg(v)+1. \tag{3}
\]
This is because every maximum stable set is maximal and hence meets \(N[v]\).

Two decomposition formulas will be used. If \(G\) is the disjoint union of nonempty graphs \(G_1,\dots,G_r\), then
\[
\eta(G)=\min_i\eta(G_i). \tag{4}
\]
A maximum stable set of \(G\) consists of a maximum stable set from every component.

If \(G=G_1\vee\cdots\vee G_r\) is the complete join, let
\[
I=\{i:\alpha(G_i)=\max_j\alpha(G_j)\}.
\]
Then
\[
\eta(G)=\sum_{i\in I}\eta(G_i), \qquad
\omega(G)=\sum_i\omega(G_i). \tag{5}
\]
Indeed, a maximum stable set is contained in exactly one \(G_i\) with \(i\in I\).

All these statements also have weighted analogues when vertex weights are strictly positive.

---

# 2. Weighted transversals in perfect graphs

For a positive integer weight function \(w\colon V(G)\to\mathbb N\), write
\[
\eta_w(G)
\]
for the minimum cardinality of a set meeting every maximum \(w\)-weight stable set.

## Proposition 2.1

If \(G\) is perfect, then for every positive integer weight function \(w\),
\[
\eta_w(G)\le \omega(G).
\]
Moreover, the transversal can be chosen to be a clique of \(G\).

### Proof

Put \(H=\overline G\), which is perfect. Replace each vertex \(v\in V(H)\) by a clique of \(w(v)\) true twins. By the replication lemma for perfect graphs, the resulting graph \(H^w\) is perfect.

Its clique number is
\[
W=\max\left\{\sum_{v\in K}w(v): K\text{ is a clique of }H\right\},
\]
which is the maximum weight of a stable set of \(G\). Since \(H^w\) is perfect, it has a proper \(W\)-coloring. Every \(W\)-clique uses all \(W\) colors, so any fixed color class \(C\) meets every maximum clique of \(H^w\).

Project \(C\) back to \(V(H)\), obtaining \(J\). Since the copies of each original vertex form a clique, \(C\) contains at most one copy of each vertex. Thus \(J\) is stable in \(H\), hence a clique in \(G\), and
\[
|J|\le \alpha(H)=\omega(G).
\]
Every maximum-weight clique of \(H\), and hence every maximum-weight stable set of \(G\), meets \(J\). ∎

In particular:

\[
\boxed{\eta(G)\le \omega(G)\quad\text{for every perfect graph }G.} \tag{6}
\]

Thus the conjecture is already true, with the optimal natural bound \(h(k)=k\), on all perfect \(P_t\)-free graphs. It also follows from (2) that if \(Z\) is such that \(G-Z\) is perfect, then
\[
\eta(G)\le |Z|+\omega(G). \tag{7}
\]

---

# 3. Exact reduction to weighted prime graphs

A set \(M\subseteq V(G)\) is a module if every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is prime if it has no nontrivial module.

For \(t\ge4\), the path \(P_t\) is prime. Indeed, if a proper module \(M\) of a path has at least two vertices, choose an edge \(xy\) with \(x\in M\) and \(y\notin M\). Then \(y\) must be adjacent to all of \(M\). Since \(y\) has degree at most two, \(M\) must consist of the two path-neighbors of \(y\); for \(t\ge4\), an additional path-neighbor distinguishes these two vertices, a contradiction.

## Theorem 3.1 — weighted-prime reduction

Fix \(t\ge4\). The following are equivalent.

1. The class of all \(P_t\)-free graphs is \(\eta\)-bounded.
2. There is a function \(q\colon\mathbb N\to\mathbb N\) such that, for every prime \(P_t\)-free graph \(Q\), every positive integer weight function \(w\), and every \(k=\omega(Q)\),
   \[
   \eta_w(Q)\le q(k). \tag{8}
   \]

Moreover, if (8) holds, one may take
\[
B(k)=\max\bigl(\{2,k\}\cup\{q(j):1\le j\le k\}\bigr),
\qquad
h_t(k)=B(k)^k. \tag{9}
\]

### Proof that 1 implies 2

Let \(Q\) be prime and \(P_t\)-free, with weights \(w(v)\). Replace every \(v\in V(Q)\) by an independent set \(V_v\) of size \(w(v)\), with complete or anticomplete adjacency between bags according to adjacency in \(Q\). Call the resulting independent blow-up \(Q^w\).

Because \(P_t\) is prime, \(Q^w\) is still \(P_t\)-free. Indeed, if an induced \(P_t\) used at least two vertices of one bag and at least one vertex outside it, those vertices of the bag would form a nontrivial module of the induced \(P_t\). An induced \(P_t\) cannot lie entirely in one independent bag.

Also,
\[
\omega(Q^w)=\omega(Q).
\]
The maximum stable sets of \(Q^w\) are precisely the unions
\[
\bigcup_{v\in I}V_v,
\]
where \(I\) is a maximum-weight stable set of \((Q,w)\).

If \(X\) hits all maximum stable sets of \(Q^w\), let
\[
J=\{v:X\cap V_v\neq\varnothing\}.
\]
Then \(J\) meets every maximum-weight stable set of \(Q\), and \(|J|\le |X|\). An \(\eta\)-bound for all \(P_t\)-free graphs therefore gives (8).

### Proof that 2 implies 1

Use the standard modular decomposition. Every internal node is one of:

- a disjoint-union node;
- a complete-join node;
- a substitution \(Q(G_1,\dots,G_m)\), where \(Q\) is prime.

We prove by induction on the decomposition tree that a graph \(G\) of clique number \(k\) satisfies
\[
\eta(G)\le B(k)^k. \tag{10}
\]

The disjoint-union case follows from (4).

For a complete join, put \(k_i=\omega(G_i)\), so \(\sum_i k_i=k\). By (5) and induction,
\[
\eta(G)\le \sum_i B(k_i)^{k_i}
 \le \sum_i B(k)^{k_i}
 \le B(k)^k.
\]
The last inequality follows by repeatedly using
\[
b^a+b^c\le b^{a+c}\qquad(a,c\ge1,\ b\ge2).
\]

Now suppose \(G=Q(G_1,\dots,G_m)\), where \(Q\) is prime. Set
\[
a_i=\alpha(G_i),\qquad k_i=\omega(G_i).
\]
A maximum stable set of \(G\) is obtained by choosing a maximum \(a\)-weight stable set \(I\) of \(Q\), and then choosing a maximum stable set of \(G_i\) for every \(i\in I\).

By (8), there is a set \(J\subseteq V(Q)\) of size at most
\[
q(\omega(Q))\le B(k)
\]
meeting every maximum \(a\)-weight stable set of \(Q\). For each \(j\in J\), let \(X_j\) hit all maximum stable sets of \(G_j\). Then
\[
X=\bigcup_{j\in J}X_j
\]
hits every maximum stable set of \(G\).

A prime quotient at such a node is connected, so every \(j\in V(Q)\) has a neighbor. Consequently,
\[
k_j\le k-1,
\]
because a maximum clique of \(G_j\), together with one vertex from a neighboring module, forms a clique of size at least \(k_j+1\). Therefore
\[
|X|
 \le |J|\,B(k)^{k-1}
 \le B(k)^k.
\]
This completes the induction. ∎

### Significance of the reduction

It is not enough merely to prove the unweighted statement for prime graphs. Substitution turns the quantities \(\alpha(G_i)\) into arbitrary positive weights on the prime quotient. The genuinely necessary atom-level assertion is the weighted one in (8).

---

# 4. A weakly sparse triangle-free case

The following gives an explicit bound for a substantial part of the \(\omega=2\) case.

## Theorem 4.1

Let \(t\ge4\) and \(s\ge2\). If \(G\) is triangle-free, \(P_t\)-free, and induced-\(K_{2,s}\)-free, then, for every positive weight function \(w\),
\[
\eta_w(G)\le 1+(t-3)(s-1). \tag{11}
\]

In fact, every such graph has degeneracy at most
\[
(t-3)(s-1).
\]

### Proof

It suffices to find a vertex of degree at most
\[
D=(t-3)(s-1),
\]
because \(N[v]\) hits every maximum-weight stable set.

Work in a nontrivial connected component and let
\[
P=v_1v_2\cdots v_\ell
\]
be a longest induced path. Since \(G\) is \(P_t\)-free,
\[
\ell\le t-1.
\]

For \(1\le j\le \ell-2\), put
\[
C_j=N(v_j)\cap N(v_\ell).
\]
The vertices \(v_j\) and \(v_\ell\) are nonadjacent. Moreover, \(C_j\) is stable, since two adjacent vertices of \(C_j\), together with \(v_\ell\), would form a triangle. Hence, if \(|C_j|\ge s\), then
\[
G[\{v_j,v_\ell\}\cup C_j]\cong K_{2,s},
\]
contrary to the hypothesis. Therefore
\[
|C_j|\le s-1. \tag{12}
\]

We claim that, when \(\ell\ge3\),
\[
N(v_\ell)\subseteq \bigcup_{j=1}^{\ell-2}C_j. \tag{13}
\]
The predecessor \(v_{\ell-1}\) belongs to \(C_{\ell-2}\). If \(x\notin V(P)\) is adjacent to \(v_\ell\), triangle-freeness gives \(xv_{\ell-1}\notin E(G)\). If \(x\) had no neighbor among \(v_1,\dots,v_{\ell-2}\), then
\[
v_1v_2\cdots v_\ell x
\]
would be a longer induced path. Thus \(x\in C_j\) for some \(j\le\ell-2\).

It follows from (12) and (13) that
\[
\deg(v_\ell)
 \le (\ell-2)(s-1)
 \le (t-3)(s-1).
\]
The cases \(\ell=1,2\) satisfy the same bound directly. Since the hypotheses are hereditary, the same argument applies to every induced subgraph, proving the degeneracy assertion. Finally,
\[
\eta_w(G)\le |N[v_\ell]|\le D+1.
\]
∎

Thus, for fixed \(t\), any sequence of triangle-free \(P_t\)-free graphs with unbounded \(\eta\) must contain induced \(K_{2,s}\)'s with \(s\to\infty\).

Combining Theorems 3.1, 4.1 and Proposition 2.1 gives a modularly closed special case.

## Corollary 4.2

Fix \(t\ge4\) and \(s\ge2\). Let \(G\) be \(P_t\)-free and suppose every non-perfect prime quotient appearing in its modular decomposition is triangle-free and induced-\(K_{2,s}\)-free. If \(k=\omega(G)\), then
\[
\eta(G)\le
\left(\max\{2,k,1+(t-3)(s-1)\}\right)^k. \tag{14}
\]

Indeed, a perfect prime quotient has weighted transversal number at most its clique number, while every other prime quotient has weighted transversal number bounded by (11). Theorem 3.1 then applies.

---

# 5. A bound from induced odd-cycle packing

Let \(p_{\mathrm{odd}}(G)\) denote the maximum number of pairwise vertex-disjoint induced odd cycles in \(G\), with triangles included.

## Proposition 5.1

If \(G\) is \(P_t\)-free for \(t\ge4\), then
\[
\eta_w(G)\le t\,p_{\mathrm{odd}}(G)+2 \tag{15}
\]
for every positive integer weight function \(w\).

### Proof

Every induced odd cycle in \(G\) has at most \(t\) vertices: an induced cycle of length greater than \(t\) contains an induced \(P_t\) on \(t\) consecutive vertices.

Choose a maximum collection of \(p=p_{\mathrm{odd}}(G)\) pairwise vertex-disjoint induced odd cycles and let \(Z\) be their union. Then
\[
|Z|\le tp.
\]
By maximality, \(G-Z\) has no induced odd cycle. If \(G-Z\) were non-bipartite, a shortest odd cycle in it would be induced, a contradiction. Thus \(G-Z\) is bipartite and therefore perfect, so Proposition 2.1 gives
\[
\eta_w(G-Z)\le2.
\]
The deletion inequality (2) now yields (15). ∎

Consequently, any subclass in which \(p_{\mathrm{odd}}(G)\) is bounded by a function of \(\omega(G)\) is \(\eta\)-bounded. In particular, \(P_t\)-free graphs with no two vertex-disjoint induced odd cycles satisfy
\[
\eta(G)\le t+2.
\]

This condition is not sufficient for the full conjecture because induced odd-cycle packing can be unbounded even at clique number two.

---

# 6. Why these results do not settle the conjecture

Consider the independent blow-up of \(C_5\) in which every bag has size \(m\). This graph is:

- triangle-free;
- \(P_5\)-free, hence \(P_t\)-free for every \(t\ge5\);
- of clique number \(2\);
- containing an induced \(K_{m,m}\);
- containing \(m\) vertex-disjoint induced \(C_5\)'s.

Nevertheless,
\[
\eta(G)=3.
\]
Indeed, its maximum stable sets are the unions of two nonadjacent bags. These pairs form the edge set of another \(C_5\), whose minimum vertex cover has size three.

Thus neither large induced bicliques nor large odd-cycle packing alone forces large \(\eta\). In this example the large bags are modules, and the weighted-prime reduction compresses the graph to the quotient \(C_5\).

The unresolved case is therefore more precise than the original formulation suggests:

> One must bound the transversals of maximum-weight stable sets in non-perfect prime \(P_t\)-free graphs.

For \(\omega=2\), Theorem 4.1 handles those prime atoms with bounded induced \(K_{2,s}\). What remains is the possibility of non-bipartite prime triangle-free \(P_t\)-free atoms containing arbitrarily large induced bicliques. No argument above controls the weighted maximum stable sets in such atoms.

Accordingly, there is no complete proof or counterexample here. The reductions and special cases are self-contained, but I have not verified whether some or all already occur in the literature.