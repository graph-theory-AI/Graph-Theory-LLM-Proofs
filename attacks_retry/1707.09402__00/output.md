```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove polynomial-time solvability on rP3-free graphs for every fixed r, covering all forbidden linear forests whose components have at most three vertices.",
  "would_publish": false,
  "caveats": "The full dichotomy and unrestricted P6-free case remain unresolved here; novelty of this special-case result has not been independently checked."
}
```

# A partial classification: forbidden linear forests with components of order at most three

All graphs below are finite, simple, and undirected. An **independent feedback vertex set** of \(G\) is an independent set \(S\subseteq V(G)\) such that \(G-S\) is a forest. Write \(rP_3\) for the disjoint union of \(r\) three-vertex paths.

I use a different route from the previous attempt, based on reducing the retained forest to a matching after deleting a bounded-size set.

## Main partial result

**Theorem 1.** For every fixed integer \(r\geq 1\), a minimum independent feedback vertex set of an \(rP_3\)-free graph can be found in polynomial time. One running-time bound is
\[
2^{O(r)}(n+1)^{9(r-1)+O(1)}.
\]
The algorithm also determines when no independent feedback vertex set exists.

Consequently:

**Corollary 2.** Let \(H\) be a fixed nonempty linear forest, every component of which has at most three vertices. Independent Feedback Vertex Set is polynomial-time solvable on \(H\)-free graphs.

Indeed, if \(H\) has \(r\) components, then \(H\) is an induced subgraph of \(rP_3\). Hence every \(H\)-free graph is \(rP_3\)-free.

This does **not** resolve the full classification, in particular the unrestricted \(P_6\)-free case. The proof of the partial result follows.

---

# 1. An \(rP_3\)-free forest has a bounded deletion set to a matching

Here and below, “a matching plus isolated vertices” means a graph of maximum degree at most one.

**Lemma 3.** If \(F\) is an \(rP_3\)-free forest, there exists
\[
C\subseteq V(F),\qquad |C|\leq 2r-2,
\]
such that \(F-C\) is a matching plus isolated vertices.

### Proof

Root every component of \(F\). For each three-vertex path \(P\), let its **top** be its unique vertex closest to the root of its component.

Perform the following procedure on the family of all three-vertex paths of \(F\):

1. Choose a remaining path \(P\) whose top \(v\) has maximum depth.
2. Put \(v\) into \(C\), record \(P\), and remove all paths containing \(v\).
3. Repeat until no path remains.

Every remaining path that intersects \(P\) must contain \(v\). To see this, suppose a path \(Q\) intersects \(P\) but avoids \(v\). Since \(Q\) is connected, it lies in the descendant component of \(F-v\) containing a vertex of \(P-v\). Its top is therefore strictly deeper than \(v\), contradicting the choice of \(P\).

Thus the recorded paths are vertex-disjoint. Also, \(C\) meets every three-vertex path, so \(F-C\) has maximum degree at most one.

Let \(m\) be the number of recorded paths; then \(|C|=m\). Form their interaction graph: two recorded paths are adjacent when an edge of \(F\) joins their vertex sets. This interaction graph is a forest, as can be seen by contracting each recorded path in \(F\) and then deleting all other vertices.

It therefore has an independent set of size at least \(\lceil m/2\rceil\). The corresponding paths in \(F\) are pairwise anticomplete and hence induce \(\lceil m/2\rceil P_3\). Since \(F\) is \(rP_3\)-free,
\[
m\leq 2r-2.
\]
∎

The deletion set \(C\) in this lemma concerns the unknown retained forest, not necessarily the input graph. We will enumerate it.

---

# 2. An auxiliary partition problem

We first solve a constrained version of partitioning a graph into an independent set and a matching plus isolated vertices.

An instance consists of:

- a graph \(Q\);
- disjoint sets \(I_0,R_0\subseteq V(Q)\), whose vertices must respectively be selected and retained;
- a set \(L\subseteq E(Q)\) of edges permitted to have two retained endpoints.

We seek a minimum-cardinality set \(I\) such that, writing \(R=V(Q)\setminus I\),

\[
\begin{aligned}
&I_0\subseteq I,\qquad R_0\subseteq R,\\
&I\text{ is independent},\\
&\Delta(Q[R])\leq 1,\\
&E(Q[R])\subseteq L.
\end{aligned} \tag{1}
\]

Allowing forbidden retained edges will be important in the final reduction.

**Lemma 4.** For every fixed \(r\), problem (1) is polynomial-time solvable on \(rP_3\)-free graphs, in time
\[
2^{O(r)}(n+1)^{3(r-1)+O(1)}.
\]

### Proof

## 2.1. A bounded seed leaves a union of cliques

Greedily find a maximal family of pairwise anticomplete induced three-vertex paths in \(Q\). Let \(X\) be the union of their vertex sets. Since \(Q\) is \(rP_3\)-free,
\[
|X|\leq 3(r-1).
\]

Put
\[
A=N_Q[X],\qquad B=V(Q)\setminus A.
\]
By maximality, \(Q[B]\) is \(P_3\)-free, and therefore is a disjoint union of cliques.

## 2.2. Guessing labels and mates determines all of \(A\)

Enumerate the selected/retained labels of vertices in \(X\).

For every vertex \(x\in X\) guessed retained, also guess its unique retained neighbor, or guess that it has none:
\[
\mu(x)\in N_Q(x)\cup\{\bot\}.
\]

Each branch forces labels as follows.

- If \(x\) is selected, every neighbor of \(x\) is retained.
- If \(x\) is retained and \(\mu(x)=\bot\), every neighbor of \(x\) is selected.
- If \(x\) is retained and \(\mu(x)=y\), then \(y\) is retained and every vertex of \(N_Q(x)\setminus\{y\}\) is selected.

Consequently, every vertex of \(A\) receives a label. Reject contradictory assignments, including contradictions with \(I_0,R_0\).

Let the resulting partition of \(A\) be \(I_A,R_A\). Check that

- \(I_A\) is independent;
- \(Q[R_A]\) has maximum degree at most one;
- every edge of \(Q[R_A]\) belongs to \(L\).

Reject the branch if any check fails.

Every feasible solution of (1) appears in one of these branches: use its labels on \(X\) and its actual retained mates.

## 2.3. The remaining choices form a bipartite matching problem

Consider a clique component \(K\) of \(Q[B]\). A feasible partition can select at most one vertex of \(K\), and can retain at most two. Hence a clique of order at least four makes the branch infeasible.

For each remaining clique \(K\), enumerate its local choices
\[
I_K\subseteq K,\qquad |I_K|\leq 1,\qquad R_K=K\setminus I_K,\qquad |R_K|\leq 2.
\]
There are at most four choices. Reject a choice unless:

1. it respects the prescribed labels \(I_0,R_0\);
2. no vertex of \(I_K\) is adjacent to a vertex of \(I_A\);
3. every retained edge within \(K\), or between \(R_K\) and \(R_A\), belongs to \(L\);
4. every vertex of \(Q[R_A\cup R_K]\) has retained degree at most one.

Assign the choice cost \(|I_K|\).

The key observation is that each surviving local choice uses **at most one** available retained vertex of \(A\):

- If \(|R_K|=2\), its two vertices are adjacent. Neither can have a neighbor in \(R_A\), so the choice uses no such vertex.
- If \(|R_K|=1\), its retained vertex has at most one neighbor in \(R_A\). If it has such a neighbor \(a\), then \(a\) must be isolated in \(Q[R_A]\), and this choice uses the sole available retained-degree slot at \(a\).
- If \(|R_K|=0\), no slot is used.

Thus the only possible conflict between choices for different clique components is that two of them use the same isolated vertex \(a\in R_A\). There are no edges between different clique components.

Construct a bipartite graph with:

- one left vertex for each clique component \(K\);
- one right vertex for each isolated vertex of \(Q[R_A]\);
- an additional private right vertex \(d_K\) for each clique \(K\).

For every local choice using the slot at \(a\), add the edge \(Ka\) with its cost. For a choice using no slot, add \(Kd_K\). If several choices produce the same edge, keep the cheapest and remember a corresponding choice.

A minimum-cost matching covering all left vertices gives exactly the best compatible collection of local choices. This is a standard polynomial-time min-cost flow computation: send one unit from each left vertex to a chosen right vertex, each right vertex having capacity one.

Add the fixed cost \(|I_A|\), and minimize over all branches.

All selected-set independence conditions have been checked locally, and the matching enforces every remaining retained-degree constraint. Thus the construction is both sound and complete.

## 2.4. Running time

There are at most
\[
2^{|X|}(n+1)^{|X|}
\leq 2^{3(r-1)}(n+1)^{3(r-1)}
\]
branches. Each is processed in polynomial time. ∎

---

# 3. Only boundedly many matching components can connect the forest core

The next observation will reduce acyclicity to the permitted-edge conditions in Lemma 4.

**Lemma 5.** Let \(F\) be a forest, and let \(C\subseteq V(F)\) be such that \(F-C\) has maximum degree at most one. For each component \(T\) of \(F-C\), put
\[
a(T)=|E_F(T,C)|.
\]

If \(C\neq\varnothing\), at most \(|C|-1\) components \(T\) satisfy \(a(T)\geq 2\). Their union therefore has at most \(2|C|-2\) vertices.

### Proof

Let \(F^+\) consist of \(C\) and all components \(T\) of \(F-C\) for which \(a(T)\geq 1\). It is a forest, and all its components meet \(C\).

Writing \(\kappa(F^+)\) for its number of components, an edge count gives
\[
|E(F[C])|
+\sum_{T:\,a(T)\geq 1}\bigl(a(T)-1\bigr)
=
|C|-\kappa(F^+)
\leq |C|-1.
\]
Indeed, each \(T\) contributes \(|V(T)|-1\) internal edges and \(a(T)\) attachment edges.

All summands are nonnegative, and each component with \(a(T)\geq 2\) contributes at least one. There are therefore at most \(|C|-1\) such components. Each has at most two vertices. ∎

If \(C=\varnothing\), no component has any attachment to \(C\), so the exceptional union is empty.

---

# 4. The IFVS algorithm

We now prove Theorem 1.

Let \(G\) be \(rP_3\)-free and put
\[
d=2r-2.
\]

Enumerate all disjoint sets \(C,Z\subseteq V(G)\) satisfying
\[
|C|\leq d,\qquad
|Z|\leq 2\max\{|C|-1,0\}. \tag{2}
\]

Their intended meanings are:

- \(C\) is a retained set whose deletion makes the retained forest a matching plus isolated vertices;
- \(Z\) is the union of matching components having at least two edges to \(C\).

For each pair, proceed as follows.

### Step 1: Check the retained core

Reject the pair unless
\[
G[C\cup Z]\text{ is a forest}
\]
and \(G[Z]\) has maximum degree at most one.

All vertices of \(C\cup Z\) are to be retained.

### Step 2: Specify the remaining partition instance

Put
\[
U=V(G)\setminus(C\cup Z),\qquad Q=G[U],
\]
and, for \(u\in U\), define
\[
b(u)=|N_G(u)\cap C|.
\]

Force the following vertices to be selected:
\[
I_0=
\{u\in U:N_G(u)\cap Z\neq\varnothing\}
\ \cup\
\{u\in U:b(u)\geq 2\}. \tag{3}
\]

Take no additional forced-retained vertices, and allow exactly these edges to have two retained endpoints:
\[
L=\{uv\in E(Q):b(u)+b(v)\leq 1\}. \tag{4}
\]

Use Lemma 4 to find a minimum solution \(I\) of this annotated partition instance.

Among all feasible pairs \(C,Z\), return a smallest such \(I\). If there is no feasible pair, report that \(G\) has no independent feedback vertex set.

---

## 4.1. Soundness

Consider a feasible branch, and write
\[
R=U\setminus I.
\]

By Lemma 4, \(I\) is independent and \(Q[R]\) is a matching plus isolated vertices.

By (3):

- no vertex of \(R\) is adjacent to \(Z\);
- every vertex of \(R\) has at most one neighbor in \(C\).

By (4), if \(uv\) is a retained matching edge, then
\[
b(u)+b(v)\leq 1.
\]

Consequently, every component of \(Q[R]\) has at most one edge to \(C\cup Z\). Since \(G[C\cup Z]\) is a forest, adding these vertex-disjoint matching components cannot create a cycle.

Thus
\[
G-I=G[C\cup Z\cup R]
\]
is a forest, and \(I\) is a valid independent feedback vertex set of \(G\).

---

## 4.2. Completeness and optimality

Suppose \(S\) is any independent feedback vertex set, and put
\[
F=G-S.
\]

By Lemma 3, there exists \(C\subseteq V(F)\) with \(|C|\leq d\) such that \(F-C\) has maximum degree at most one.

Let \(Z\) be the union of components \(T\) of \(F-C\) satisfying
\[
|E_F(T,C)|\geq 2.
\]
Lemma 5 shows that \(C,Z\) satisfy (2), including the case \(C=\varnothing\). Hence this pair is enumerated.

For this pair:

- \(G[C\cup Z]\) is a forest;
- \(G[Z]\) has maximum degree at most one;
- no retained vertex outside \(C\cup Z\) is adjacent to \(Z\), since \(Z\) is a union of components of \(F-C\);
- every remaining component of \(F-C\) has at most one attachment edge to \(C\).

It follows that \(S\) contains every vertex forced selected in (3). Moreover, on \(Q=G-(C\cup Z)\), its retained vertices induce a matching plus isolated vertices, and every retained edge satisfies (4).

Therefore \(S\) is a feasible solution of the annotated instance in this branch.

Applying this to a minimum independent feedback vertex set \(S\), the algorithm returns a solution of size at most \(|S|\). Soundness shows that it cannot return a smaller invalid answer. Hence it returns the optimum.

This also covers graphs that are already forests and graphs having no independent feedback vertex set.

---

## 4.3. Running time

There are at most
\[
(n+1)^{3d}
\]
choices of \(C,Z\), using the slightly looser bound \(|Z|\leq 2d\).

Each annotated instance remains \(rP_3\)-free, so Lemma 4 solves it in
\[
2^{O(r)}(n+1)^{3(r-1)+O(1)}
\]
time. Since \(d=2r-2\), the total is
\[
2^{O(r)}(n+1)^{9(r-1)+O(1)}.
\]
This proves Theorem 1. ∎

---

# 5. Consequences and exact remaining gap

For every fixed choice of nonnegative integers \(s,t,u\), not all zero, the theorem gives a polynomial-time algorithm on
\[
(sP_1+tP_2+uP_3)\text{-free graphs}.
\]
Thus it covers, for example, all fixed \(rP_3\)-free classes, not just forbidden matchings or bounded-independence-number classes.

The essential ingredients are:

1. an \(rP_3\)-free forest becomes a matching after deleting at most \(2r-2\) vertices;
2. only boundedly many resulting matching components can attach more than once to that retained core;
3. the remaining constrained independent-set/matching partition problem is solvable by bounded enumeration followed by min-cost bipartite matching.

The unresolved scope is still substantial. In particular, no fixed \(r\) bounds the number of pairwise anticomplete \(P_3\)'s in a \(P_6\)-free graph. This remains true for connected graphs: add a universal vertex to \(mP_3\). The resulting graph is \(P_6\)-free and contains an induced \(mP_3\) for arbitrarily large \(m\).

Accordingly, the argument does not provide a polynomial-time algorithm for unrestricted \(P_6\)-free graphs, nor an NP-hardness construction for any fixed \(P_h\)-free class. It is a proved special-case classification, not a resolution of the full catalogued problem. I have not independently verified whether this particular special-case theorem already appears in the literature.