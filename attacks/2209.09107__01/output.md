```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The question remains open, but any universal constant must satisfy C >= 3/2, this obstruction occurs for arbitrarily large maximum degree and is sharp for subcubic graphs, while bipartite graphs satisfy the bound with C = 1.",
  "would_publish": false,
  "caveats": "No uniform upper bound is obtained for arbitrary high-degree non-bipartite graphs; the standard AT normalization with outdegree at most k-1 is used."
}
```

# 1. Statement and normalization

All graphs below are finite and simple. I use the standard normalization: \(\operatorname{AT}(G)\) is the least \(k\) for which \(G\) has an orientation \(D\) satisfying

\[
d_D^+(v)\le k-1\qquad(v\in V(G))
\]

and for which the numbers of even and odd spanning Eulerian subdigraphs of \(D\) are unequal. Equivalently, the graph polynomial

\[
P_G(\mathbf x)=\prod_{uv\in E(G)}(x_u-x_v)
\]

has a nonzero monomial \(\prod_vx_v^{a_v}\) with every \(a_v\le k-1\).

I do not resolve the question. The main conclusions are:

1. A universal constant, if it exists, must satisfy
   \[
   C\ge \frac32.
   \]
   This occurs for connected regular graphs of arbitrarily large odd degree.
2. For graphs of maximum degree at most \(3\), \(C=3/2\) is sufficient and best possible.
3. For bipartite graphs, \(C=1\) is sufficient and best possible within that class.
4. The proposed bound with \(C=3/2\) also holds whenever every component has at most \(\Delta+2\) vertices.

Because \(\operatorname{AT}(G-M)\) is integral, the assertion with \(C=3/2\) is equivalent to the particularly natural bound

\[
\operatorname{AT}(G-M)\le \left\lceil\frac{\Delta}{2}\right\rceil+1.
\tag{1}
\]

# 2. Preliminary facts

## 2.1. Density obstruction

For every \(n\)-vertex graph \(H\),

\[
\operatorname{AT}(H)\ge
\left\lceil\frac{|E(H)|}{n}\right\rceil+1.
\tag{2}
\]

Indeed, in every orientation,

\[
\sum_{v\in V(H)}d^+(v)=|E(H)|.
\]

Thus an AT orientation with maximum outdegree at most \(k-1\) requires
\(|E(H)|\le n(k-1)\).

## 2.2. Monotonicity under taking subgraphs

If \(H\subseteq G\), then

\[
\operatorname{AT}(H)\le \operatorname{AT}(G).
\tag{3}
\]

For spanning subgraphs, write \(P_G=P_HP_{E(G)\setminus E(H)}\). If
\(\mathbf x^\alpha\) is a nonzero monomial of \(P_G\), then in the convolution giving its coefficient there is some nonzero product of a monomial \(\mathbf x^\beta\) of \(P_H\) and a monomial \(\mathbf x^\gamma\) of the other factor, with \(\beta+\gamma=\alpha\). Hence \(\beta\le\alpha\) coordinatewise. Vertex deletion follows by adding isolated vertices.

# 3. A stronger necessary lower bound: \(C\ge 3/2\)

The lower bound \(1/2\) quoted in the supplied context is not strongest under the standard normalization. In fact, odd complete graphs already give \(C\ge1\). More substantially, lack of a perfect matching in an odd-regular graph gives \(C\ge3/2\).

## Proposition 3.1

Let \(G\) be a \((2q+1)\)-regular graph on \(n\) vertices with no perfect matching. Then for every matching \(M\),

\[
\operatorname{AT}(G-M)\ge q+2.
\tag{4}
\]

### Proof

Since \(G\) has no perfect matching and \(n\) is even,

\[
|M|\le \frac n2-1.
\]

Therefore

\[
|E(G-M)|
\ge \frac{(2q+1)n}{2}-\left(\frac n2-1\right)
=qn+1.
\]

By (2),

\[
\operatorname{AT}(G-M)
\ge \left\lceil q+\frac1n\right\rceil+1
=q+2.
\]

This holds for every matching \(M\). \(\square\)

Such graphs exist in every odd degree.

## Explicit family

Fix an odd integer \(d\ge3\). Construct a graph \(L_d\) as follows.

- Start with \(K_{d+2}\).
- Choose three vertices \(u,a,b\).
- Delete \(ua\) and \(ub\).
- On the remaining \(d-1\) vertices, delete a perfect matching.

Then

\[
d_{L_d}(u)=d-1,
\]

while every other vertex of \(L_d\) has degree \(d\). Notice that
\(|V(L_d)|=d+2\) is odd.

Take \(d\) disjoint copies \(L_d^1,\dots,L_d^d\), with deficient vertices
\(u_1,\dots,u_d\), add a new vertex \(z\), and add the edges

\[
zu_1,\dots,zu_d.
\]

Call the resulting graph \(G_d\). It is connected and \(d\)-regular, with

\[
|V(G_d)|=1+d(d+2)=(d+1)^2.
\]

Each \(zu_i\) is a bridge separating an odd-order component \(L_d^i\). A perfect matching would therefore have to contain every one of the \(d\) bridges \(zu_i\), which is impossible because they all meet \(z\). Hence \(G_d\) has no perfect matching.

Writing \(d=2q+1\), Proposition 3.1 gives

\[
\operatorname{AT}(G_d-M)\ge q+2
\]

for every matching \(M\). Consequently, any universal \(C\) must satisfy

\[
q+2\le \frac{2q+1}{2}+C,
\]

and hence

\[
\boxed{C\ge\frac32}.
\]

This obstruction occurs for arbitrarily large \(\Delta=d\), not merely at a small exceptional degree.

# 4. The subcubic case is completely settled

## Theorem 4.1

Every graph \(G\) with maximum degree \(\Delta\le3\) has a matching \(M\) such that

\[
\operatorname{AT}(G-M)
\le \left\lceil\frac{\Delta}{2}\right\rceil+1.
\tag{5}
\]

Thus \(C=3/2\) is sufficient for all subcubic graphs. The graph \(G_3\) above shows that \(3/2\) is best possible for this class.

The only substantial case is \(\Delta=3\).

## Lemma 4.2

Every connected subcubic graph other than \(K_4\) has Alon–Tarsi number at most \(3\).

### Proof

If \(G\) is \(2\)-degenerate, orient its edges acyclically according to a degeneracy ordering. The maximum outdegree is at most \(2\), and an acyclic orientation has only the empty Eulerian subdigraph. Hence \(\operatorname{AT}(G)\le3\).

Suppose now that \(G\) is not \(2\)-degenerate. It contains a subgraph of minimum degree at least \(3\). Since \(G\) is subcubic, every vertex of this subgraph has all three neighbors inside it. Connectedness then implies that \(G\) itself is cubic.

Every cubic graph contains an even cycle. To see this, take a longest path
\(v_0\ldots v_\ell\). All three neighbors of \(v_\ell\) lie on the path. Two of their indices have the same parity, and those two edges together with the intervening subpath form an even cycle.

Choose a shortest even cycle \(C\). We claim that \(C\) has at most one chord unless \(G=K_4\).

Every chord of \(C\) joins vertices at even distance on \(C\), since otherwise the chord and one of the two arcs would give a shorter even cycle. Since \(G\) is cubic, distinct chords of \(C\) have disjoint endpoints.

If two chords do not cross, the two chords together with the two arcs lying between the chords form a shorter even cycle. If they cross, let the four intervening arc lengths be \(a,b,c,d\) cyclically. The parity condition on the chord endpoints implies that \(a,b,c,d\) have the same parity. The two cycles using both chords have lengths

\[
a+c+2,\qquad b+d+2.
\]

Both are even. Unless \(a=b=c=d=1\), one is shorter than \(C\). The exceptional case is a \(4\)-cycle with both diagonals, namely \(K_4\); since all four vertices are then saturated, connectedness gives \(G=K_4\). This proves the claim.

Let \(Q=G[V(C)]\), so \(Q\) is either \(C\) itself or \(C\) plus one chord. The graph \(G-V(C)\) is \(2\)-degenerate: otherwise it would contain a subgraph of minimum degree \(3\), which in a cubic graph would be closed off from \(C\), contradicting connectedness.

Orient \(G-V(C)\) acyclically with maximum outdegree at most \(2\). Orient all edges from \(C\) to \(G-V(C)\). Orient \(C\) as a directed cycle. If there is a chord, orient it arbitrarily.

Every vertex of \(C\) has one outgoing cycle edge and at most one additional incident edge, so its outdegree is at most \(2\). Vertices outside \(C\) also have outdegree at most \(2\).

It remains to verify the Alon–Tarsi parity condition.

- If \(Q=C\), its only Eulerian subdigraphs are the empty graph and the full directed even cycle. Both are even, so the difference is \(2\).
- If \(Q\) has one chord, the Eulerian subdigraphs are:
  \[
  \varnothing,\quad C,\quad\text{the directed cycle consisting of the chord and the directed head-to-tail path on \(C\)}.
  \]
  The last cycle is odd because the chord endpoints split the shortest even cycle into two odd cycles. Thus the even-minus-odd difference is \(2-1=1\).

No Eulerian subdigraph of the full orientation can use an edge from \(C\) to \(G-V(C)\): summing outdegree minus indegree over \(V(C)\) would give a positive number. The orientation outside \(C\) is acyclic. Therefore the full orientation has the same nonzero parity difference as \(Q\), and maximum outdegree at most \(2\). Hence \(\operatorname{AT}(G)\le3\). \(\square\)

### Completion of Theorem 4.1

If \(\Delta=3\), choose one edge from every component isomorphic to \(K_4\), and let \(M\) be the union of these edges. Then every \(K_4-e\) is \(2\)-degenerate, while Lemma 4.2 handles all other components. Thus

\[
\operatorname{AT}(G-M)\le3.
\]

If \(\Delta=2\), choose one edge from every odd-cycle component. The resulting graph is bipartite of maximum degree at most \(2\), and hence has an AT orientation with maximum outdegree at most \(1\). Thus \(\operatorname{AT}(G-M)\le2\).

If \(\Delta\le1\), remove all edges; they form a matching.

Finally, for the graph \(G_3\) from Section 3, every matching \(M\) satisfies
\(\operatorname{AT}(G_3-M)\ge3\). Lemma 4.2 and monotonicity give the reverse inequality. Hence

\[
\operatorname{AT}(G_3-M)=3
\]

for every matching \(M\). This proves sharpness of \(C=3/2\) in the subcubic class.

# 5. Bipartite graphs: \(C=1\)

## Theorem 5.1

Every bipartite graph \(B\) of maximum degree \(\Delta\) has a matching \(M\) such that

\[
\operatorname{AT}(B-M)
\le \left\lfloor\frac{\Delta}{2}\right\rfloor+1.
\tag{6}
\]

In particular, the original inequality holds for bipartite graphs with \(C=1\).

### Proof

First, every graph \(H\) admits a balanced orientation satisfying

\[
d^+(v)\le \left\lceil\frac{d_H(v)}2\right\rceil.
\tag{7}
\]

This follows by adjoining a new vertex to all odd-degree vertices, orienting Euler tours in the resulting even-degree graph, and then deleting the added edges.

For a bipartite graph, every directed cycle is even. Hence every Eulerian subdigraph, being a union of directed cycles, has an even number of edges. Thus every orientation of a bipartite graph is an AT orientation.

By the bipartite edge-colouring theorem, \(B\) has a proper \(\Delta\)-edge-colouring. Let \(M\) be any colour class. Every vertex of degree \(\Delta\) is incident with an edge of every colour, so

\[
\Delta(B-M)\le\Delta-1.
\]

Applying (7) to \(B-M\),

\[
\operatorname{AT}(B-M)
\le \left\lceil\frac{\Delta-1}{2}\right\rceil+1
=\left\lfloor\frac{\Delta}{2}\right\rfloor+1.
\]

\(\square\)

This is sharp within the bipartite class. If \(B\) is \(2q\)-regular on \(n\) vertices, then for every matching \(M\),

\[
|E(B-M)|\ge qn-\frac n2.
\]

By (2), \(\operatorname{AT}(B-M)\ge q+1\), and Theorem 5.1 attains equality. Thus even for bipartite graphs one cannot in general replace \(C=1\) by a smaller constant.

# 6. Two further positive regimes

## 6.1. Components of order at most \(\Delta+2\)

Let the components of \(G\) have orders \(n_1,\dots,n_s\). In each component, pair its vertices arbitrarily, leaving one unpaired vertex if its order is odd. Let \(N_i\) be this maximum matching in the ambient complete graph, and put

\[
M_i=N_i\cap E(G).
\]

Then

\[
G_i-M_i\subseteq K_{n_i}-N_i.
\]

Using the formula quoted in the question,

\[
\operatorname{AT}(K_{n_i}-N_i)=\left\lceil\frac{n_i}{2}\right\rceil,
\]

and monotonicity gives

\[
\operatorname{AT}(G-M)\le
\max_i\left\lceil\frac{n_i}{2}\right\rceil,
\qquad M=\bigcup_iM_i.
\tag{8}
\]

Consequently, if every component has order at most \(\Delta+2\), then

\[
\operatorname{AT}(G-M)
\le\left\lceil\frac{\Delta+2}{2}\right\rceil
=\left\lceil\frac{\Delta}{2}\right\rceil+1.
\]

Thus the candidate \(C=3/2\) holds for this dense-component regime.

## 6.2. Bounded odd-cycle transversal

Suppose \(X\subseteq V(G)\), \(|X|=t\), and \(G-X\) is bipartite. Then, even with the empty matching,

\[
\operatorname{AT}(G)
\le
1+\max\left\{
\left\lceil\frac{\Delta+t}{2}\right\rceil,\,
t-1
\right\}.
\tag{9}
\]

Indeed, orient \(G-X\) in a balanced way, orient \(G[X]\) acyclically, and orient all edges between \(G-X\) and \(X\) towards \(X\). If \(v\in G-X\) has \(s\) neighbors in \(X\), then

\[
d^+(v)
\le \left\lceil\frac{d_{G-X}(v)}2\right\rceil+s
\le \left\lceil\frac{\Delta+t}{2}\right\rceil.
\]

Vertices in \(X\) have outdegree at most \(t-1\). No Eulerian subdigraph uses a cut edge directed from \(G-X\) to \(X\), so the parity difference factors into the nonzero differences on the two sides. Thus every class with bounded odd-cycle-transversal number satisfies the original question with a constant depending only on that bound.

# 7. Why ordinary colouring does not yield a counterexample

There is an elementary ordinary-colouring analogue at essentially the desired threshold.

## Proposition 7.1

Every graph of maximum degree \(\Delta\) has a matching \(M\) such that

\[
\chi(G-M)\le
\left\lceil\frac{\Delta+1}{2}\right\rceil.
\tag{10}
\]

### Proof

Let \(k=\lceil(\Delta+1)/2\rceil\), so \(2k>\Delta\). Partition \(V(G)\) into \(k\) classes minimizing the total number of edges lying inside classes.

If some vertex \(v\) has at least two neighbors in its own class, then not every class can contain at least two neighbors of \(v\), since that would give \(d(v)\ge2k>\Delta\). Moving \(v\) to a class containing at most one of its neighbors strictly decreases the number of intraclass edges, a contradiction.

Thus each class induces maximum degree at most \(1\). The union \(M\) of all intraclass edges is a matching, and after deleting \(M\) the classes are independent. \(\square\)

Therefore a counterexample to the AT question cannot arise merely from chromatic-number resilience: for a suitable matching, the ordinary chromatic number is already at the half-degree threshold. It would have to exploit genuine Alon–Tarsi coefficient cancellation or list-colouring phenomena.

# 8. Remaining gap

The strongest natural target consistent with the examples above is

\[
\boxed{\operatorname{AT}(G-M)\le
\left\lceil\frac{\Delta}{2}\right\rceil+1,}
\]

equivalently \(C=3/2\). The lower-bound family shows this would be optimal.

The arguments here establish this bound for:

- all graphs of maximum degree at most \(3\);
- all bipartite graphs, with the stronger constant \(C=1\);
- graphs whose components have order at most \(\Delta+2\).

They do not control general high-degree non-bipartite graphs with large components. In particular, the cubic proof relies on a shortest even cycle having at most one chord; this fails badly in higher degree. No complete proof or counterexample to the existence of a universal constant is obtained.