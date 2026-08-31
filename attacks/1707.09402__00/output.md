```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every fixed linear forest H, IFVS on H-free graphs has a bounded-rank hitting-set formulation, an explicit FPT algorithm and polynomial compression, but neither a polynomial algorithm nor P_h-free hardness is obtained.",
  "would_publish": false,
  "caveats": "The unrestricted P6-free and general linear-forest classifications remain open; the hardness construction below has arbitrarily long induced paths."
}
```

# 1. Problem and scope

For a graph \(G\) and integer \(k\), **Independent Feedback Vertex Set** asks whether there is a set
\[
S\subseteq V(G),\qquad |S|\le k,
\]
such that \(S\) is independent and \(G-S\) is a forest.

The requested dichotomy for \(H\)-free graphs is not resolved below. In particular, I do not obtain either:

* a polynomial-time algorithm on unrestricted \(P_6\)-free graphs, or
* an NP-hardness reduction whose outputs are \(P_h\)-free for some fixed \(h\).

I give several rigorous partial results, including a direct parameterized reduction valid for every fixed linear forest, a polynomially solvable structural branch, and a hardness result explaining why domination-based extensions of the \(P_5\)-free method do not work without using the path-free hypothesis.

# 2. Linear-forest-free graphs have only bounded induced cycles

Let \(H\) be a fixed linear forest with \(p=|V(H)|\) and \(c=c(H)\) connected components. Define
\[
\tau(H):=p+c-1.
\]

## Lemma 2.1

Every \(H\)-free graph is \(P_{\tau(H)}\)-free.

### Proof

Write the component orders of \(H\) as \(p_1,\dots,p_c\). In a path on
\[
p_1+\cdots+p_c+(c-1)=\tau(H)
\]
vertices, select \(p_1\) consecutive vertices, omit one vertex, select the next \(p_2\), omit one vertex, and so on. The selected vertices induce precisely \(H\). Thus every induced \(P_{\tau(H)}\) contains an induced copy of \(H\). ∎

## Lemma 2.2

If \(G\) is \(P_t\)-free, every induced cycle of \(G\) has length at most \(t\).

### Proof

If \(C_\ell\) is induced and \(\ell\ge t+1\), then any \(t\) consecutive vertices of \(C_\ell\) induce \(P_t\). ∎

Consequently, in an \(H\)-free graph every induced cycle has at most \(\tau(H)\) vertices. In particular, for \(P_6\)-free graphs it is enough to consider induced cycles of lengths \(3,4,5,6\).

## Proposition 2.3: exact bounded-rank formulation

Let \(\mathcal C(G)\) be the family of vertex sets of induced cycles of \(G\). Then \(S\) is an independent feedback vertex set exactly when

1. \(S\) is independent, and
2. \(S\cap C\neq\varnothing\) for every \(C\in\mathcal C(G)\).

### Proof

The forward implication is immediate. Conversely, if \(G-S\) contains a cycle, a shortest cycle in \(G-S\) is chordless. Because \(G-S\) is induced, this is also an induced cycle of \(G\), contrary to condition 2. ∎

Thus on \(H\)-free graphs IFVS is a rank-\(\tau(H)\) **Independent Hitting Set** instance:

* universe \(V(G)\);
* hyperedges \(\mathcal C(G)\), all of size at most \(\tau(H)\);
* conflict graph \(G\), expressing that two adjacent vertices cannot both be selected.

Equivalently, with \(x_v=1\) meaning \(v\in S\), the constraints are
\[
\bigwedge_{uv\in E(G)}(\neg x_u\vee \neg x_v)
\quad\wedge\quad
\bigwedge_{C\in\mathcal C(G)}
\left(\bigvee_{v\in C}x_v\right),
\]
together with \(\sum_v x_v\le k\).

# 3. Parameterized consequences

## Theorem 3.1

For each fixed linear forest \(H\), IFVS on \(H\)-free graphs can be solved in
\[
\tau(H)^k\, n^{O(1)}
\]
time.

### Proof

Maintain a current independent set \(S\). If \(G-S\) is a forest, accept. Otherwise find a shortest cycle \(C\) in \(G-S\). It is induced, and by Lemmas 2.1–2.2,
\[
|C|\le \tau(H).
\]
Every extension of \(S\) to a feedback vertex set must contain a vertex of \(C\). Branch over all \(v\in C\) that have no neighbor in \(S\), replacing \(S\) by \(S\cup\{v\}\). The depth is at most \(k\), and the branching factor is at most \(\tau(H)\). ∎

For \(P_6\)-free graphs this gives a direct \(6^k n^{O(1)}\) algorithm. This does not imply polynomial time when \(k\) is part of the input and may be linear in \(n\).

## Theorem 3.2: polynomial compression

For fixed \(H\), an \(H\)-free IFVS instance \((G,k)\) has a polynomial-time compression to an Independent Hitting Set instance with
\[
O_H(k^{\tau(H)})
\]
vertices and \(O_H(k^{\tau(H)})\) hyperedges.

### Proof

Set \(d=\tau(H)\). Enumerate all induced cycles of lengths at most \(d\), in \(n^{O(d)}\) time, obtaining a rank-\(d\) hypergraph \(\mathcal F\).

Use the following sunflower reduction. If
\[
F_1,\dots,F_{k+2}
\]
form a sunflower with core \(C\), delete \(F_{k+2}\). This preserves every hitting set of size at most \(k\): a set of at most \(k\) vertices hitting \(F_1,\dots,F_{k+1}\) must meet \(C\), since otherwise it needs distinct vertices in the \(k+1\) pairwise disjoint petals. It therefore also hits \(F_{k+2}\).

The constructive sunflower lemma for rank \(d\) implies that a family with more than
\[
d!(k+1)^d
\]
members contains such a sunflower. Repeating the rule leaves a family \(\mathcal F'\) of at most \(d!(k+1)^d\) hyperedges. The constructive proof is polynomial for fixed \(d\): greedily find a maximal family of disjoint sets; if it has fewer than \(k+2\) members, recurse on a high-frequency element, reducing the rank by one.

Let
\[
U'=\bigcup_{F\in\mathcal F'}F.
\]
Then
\[
|U'|\le d\cdot d!(k+1)^d.
\]
Restrict the conflict graph to \(G[U']\). If an independent size-\(k\) hitting set uses vertices outside \(U'\), deleting those vertices from the set preserves the property of hitting \(\mathcal F'\); the sunflower reductions then imply that it still hits every original cycle. Hence the restriction is equivalent.

This is a compression to Independent Hitting Set, rather than necessarily a graph-instance kernel, because the retained hyperedges need not be exactly the induced cycles of \(G[U']\). ∎

## Corollary 3.3: bounded degree

For every fixed linear forest \(H\) and fixed \(\Delta\), IFVS is polynomial-time solvable on \(H\)-free graphs of maximum degree at most \(\Delta\).

### Proof

Put \(t=\tau(H)\). Every connected \(P_t\)-free graph has diameter at most \(t-2\), since every shortest path is induced. A connected graph of maximum degree \(\Delta\) and diameter at most \(t-2\) has at most
\[
B(t,\Delta)=1+\Delta\sum_{i=0}^{t-3}(\Delta-1)^i
\]
vertices, with the usual interpretation for \(\Delta\le1\). Thus every connected component has constant order. Enumerate all vertex subsets in each component, find its minimum independent feedback vertex set, and add the componentwise optima. ∎

# 4. A polynomial domination branch

The following is useful when a structural decomposition produces a small dominating set known to be retained.

## Theorem 4.1

Let \(D\) be a specified dominating set of order \(d\). In time
\[
n^{3d+O(1)}
\]
one can find a minimum independent feedback vertex set \(S\) subject to
\[
S\cap D=\varnothing.
\]

### Proof

Put \(U=V(G)\setminus D\), and let \(x_u=1\) mean \(u\in S\). Since \(D\) dominates \(G\),
\[
a(u):=|N(u)\cap D|\ge1
\]
for every \(u\in U\).

Suppose \(S\) is feasible and put \(R=U\setminus S\). Let
\[
A=\sum_{u\in R}(a(u)-1),
\qquad
m=|E(G[R])|.
\]
Every component of the forest \(G[D\cup R]\) contains a vertex of \(D\), so it has at most \(d\) components. Counting edges gives
\[
|E(G[D\cup R])|
 =|E(G[D])|+|R|+A+m.
\]
Since this graph is a forest,
\[
|E(G[D])|+A+m=d-c(G[D\cup R])\le d-1.
\]
In particular,
\[
A\le d-1,\qquad m\le d-1. \tag{1}
\]

Therefore:

* at most \(d-1\) retained vertices \(u\) have \(a(u)\ge2\);
* at most \(d-1\) edges have both endpoints retained.

Enumerate:

* a set \(Z\subseteq\{u:a(u)\ge2\}\), of size at most \(d-1\), intended to be exactly the retained vertices having at least two neighbors in \(D\);
* a set \(M\subseteq E(G[U])\), of size at most \(d-1\), intended to be exactly \(E(G[R])\).

For a fixed pair \((Z,M)\), impose:

1. \(x_u=0\) for \(u\in Z\cup V(M)\);
2. \(x_u=1\) for every \(u\notin Z\) with \(a(u)\ge2\);
3. \(x_u\ne x_v\) for every \(uv\in E(G[U])\setminus M\).

Condition 3 is necessary because such an edge may have neither two retained endpoints, by the definition of \(M\), nor two selected endpoints, by independence. These are parity constraints and can be solved componentwise by testing bipartiteness, with fixed values propagated through each component.

Let
\[
C=D\cup Z\cup V(M).
\]
Every retained vertex outside \(C\) has exactly one neighbor in \(D\) and no retained neighbor in \(U\); it is therefore a leaf of \(G-S\). Hence \(G-S\) is a forest exactly when the parity system is consistent and \(G[C]\) is a forest.

In a parity component with no fixed value, the two possible orientations may be considered independently; choose the one selecting fewer vertices. Taking the best result over all \((Z,M)\) gives the optimum. The number of choices is at most
\[
n^{d-1}\cdot n^{2d-2}=n^{3d-3}.
\]
∎

## Corollary 4.2: universal vertex

IFVS is solvable in linear time on graphs with a universal vertex \(u\).

Indeed:

* If \(u\in S\), then \(S=\{u\}\), and this is feasible exactly when \(G-u\) is a forest.
* If \(u\notin S\), then no edge of \(G-u\) can have both endpoints retained, since together with \(u\) it would form a triangle. Every edge of \(G-u\) must therefore have exactly one endpoint in \(S\). Thus \(G-u\) must be bipartite, and in each connected component one chooses one bipartition class for \(S\), taking the smaller class for optimization.

# 5. Why domination alone does not extend the result

The restriction \(S\cap D=\varnothing\) in Theorem 4.1 is essential. In fact, IFVS is already NP-complete on graphs with a specified dominating edge.

## Theorem 5.1

Independent Feedback Vertex Set is NP-complete on \(K_4\)-free graphs having a dominating edge \(xy\). Moreover, the construction can ensure that every solution of size at most \(k\) contains \(x\).

### Proof

Reduce from **3-Set Packing**. Let
\[
\mathcal A=\{A_1,\dots,A_m\}
\]
be a family of 3-element subsets of a universe \(W\), and let \(q\) be the desired packing size. Set
\[
K=1+m-q,\qquad L=K+1.
\]

Construct \(G\) with vertices:

* \(x,y\);
* an element vertex \(f_w\) for every \(w\in W\);
* a set vertex \(u_i\) for every \(A_i\);
* vertices \(a_j,b_j\) for \(1\le j\le L\).

Add the following edges:

1. \(xy\);
2. \(xf_w\) for all \(w\in W\);
3. \(yu_i\) for all \(i\);
4. \(u_if_w\) exactly when \(w\in A_i\);
5. for every \(j\), the triangle \(xa_jb_jx\).

There are no other edges. The edge \(xy\) is dominating: every element or forcing-gadget vertex is adjacent to \(x\), while every set vertex is adjacent to \(y\). The only triangles are the \(xa_jb_j\), so the graph is \(K_4\)-free.

Every feedback vertex set must hit each triangle \(xa_jb_j\). If \(x\notin S\), at least one of \(a_j,b_j\) must be selected for every \(j\), giving
\[
|S|\ge L=K+1.
\]
Thus every solution of size at most \(K\) contains \(x\).

Since \(S\) is independent, once \(x\in S\), none of
\[
y,\quad f_w,\quad a_j,\quad b_j
\]
can belong to \(S\). Hence
\[
S=\{x\}\cup\{u_i:i\notin I\}
\]
for some index set \(I\).

If \(i,j\in I\) and \(A_i\cap A_j\) contains \(w\), then
\[
y-u_i-f_w-u_j-y
\]
is a surviving 4-cycle. Therefore the sets \(A_i\), \(i\in I\), must be pairwise disjoint.

Conversely, if they are pairwise disjoint, then after deleting \(S\):

* each \(a_jb_j\) is an isolated edge;
* the component containing \(y\) consists of edges \(yu_i\), with the corresponding element vertices as leaves adjacent to their unique retained \(u_i\);
* unused element vertices are isolated.

Thus \(G-S\) is a forest. Finally,
\[
|S|=1+m-|I|\le K
\quad\Longleftrightarrow\quad
|I|\ge q.
\]
Hence \(G\) has an IFVS of size at most \(K\) exactly when \(\mathcal A\) has a packing of size at least \(q\). ∎

This does not settle any \(P_h\)-free case. The incidence subgraph on the vertices \(u_i,f_w\) can contain arbitrarily long induced paths. For example, with
\[
A_i=\{e_{i-1},e_i,z_i\},
\]
the sequence
\[
z_1,u_1,e_1,u_2,e_2,\ldots,e_{r-1},u_r,z_r
\]
is an induced path of unbounded order.

# 6. A fully solvable orthogonal subclass: chordal graphs

For completeness, IFVS has a particularly simple description on chordal graphs.

## Proposition 6.1

A chordal graph has an independent feedback vertex set if and only if it is \(K_4\)-free. The minimum size can be found in polynomial, in fact linear, time.

### Proof

A graph containing \(K_4\) has no IFVS: an independent set contains at most one vertex of the \(K_4\), leaving a triangle.

Conversely, a \(K_4\)-free chordal graph has clique number at most three and is properly 3-colourable. For any proper 3-colouring, deleting one colour class leaves an induced chordal bipartite graph. A chordal triangle-free graph is a forest, so each colour class is an IFVS.

Moreover, there is an exact optimization correspondence:

* an IFVS \(S\) yields a proper 3-colouring by 2-colouring the forest \(G-S\) and giving \(S\) the third colour;
* the third colour class of any proper 3-colouring is an IFVS.

Thus the optimum is the minimum possible size of a designated colour class in a proper 3-colouring. Since a \(K_4\)-free chordal graph has treewidth at most two, this is found by the standard constant-state dynamic program over its clique tree. ∎

# 7. Exact remaining gap

For \(P_6\)-free graphs, Proposition 2.3 reduces the problem to selecting an independent set meeting every induced \(C_3,C_4,C_5,C_6\). Bounded arity alone is not enough: abstract rank-3 Independent Hitting Set is already NP-hard. Given a positive 1-in-3-SAT instance, use its variables as the universe, its clauses as 3-hyperedges, and join two variables in the conflict graph whenever they occur in a common clause. An independent hitting set then selects exactly one variable from every clause.

What remains special, and unexploited here, is that in the graph problem the hyperedges must be actual induced cycles of the same \(P_6\)-free conflict graph. A resolution therefore requires either:

1. a structural algorithm exploiting this realizability condition, or
2. an NP-hardness construction realizing sufficiently rich exact-one constraints while forbidding induced \(P_6\)'s.

The domination-edge reduction shows that a small dominating structure by itself is insufficient, but its long incidence paths prevent it from addressing the catalogued open cases.