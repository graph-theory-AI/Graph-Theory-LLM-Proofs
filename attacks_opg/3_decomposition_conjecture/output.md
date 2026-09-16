```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A connected cubic graph has a 3-decomposition if it has an induced cycle family with connected complement and a cactus forest outside its closed neighborhood.",
  "would_publish": false,
  "caveats": "The required cycle family is not shown to exist in general; novelty of this sufficient condition is unverified."
}
```

## 1. A constructive special case

All original graphs below are finite and simple. Auxiliary graphs obtained by suppressing degree-two vertices may have loops and parallel edges.

Call a graph a **cactus forest** if each of its components is a cactus: every nontrivial block is an edge or a cycle. Isolated vertices and the empty graph are allowed.

### Theorem
Let \(G\) be a connected cubic graph. Suppose that a nonempty set \(S\subsetneq V(G)\) satisfies:

1. \(G[S]\) is \(2\)-regular;
2. \(G-S\) is connected;
3. \(G-N_G[S]\) is a cactus forest.

Then \(G\) has a decomposition into a spanning tree, the cycle family \(G[S]\), and a matching. Given \(S\), such a decomposition can be constructed in linear time.

In particular, this proves the conjecture for graphs having an induced cycle \(C\) such that
\[
G-V(C)\text{ is connected}
\quad\text{and}\quad
G-N_G[V(C)]\text{ is a cactus forest}.
\]

The main ingredient is an unconditional matching-decycling result for subcubic graphs.

## 2. A matching-decycling lemma

### Lemma
Let \(H\) be a connected subcubic graph, and put
\[
D=\{v\in V(H):d_H(v)=3\}.
\]
If \(H[D]\) is a cactus forest, then \(H\) has a matching \(M\) such that \(H-M\) is a spanning tree.

Thus the 2-Decomposition Conjecture holds whenever the degree-three vertices induce a cactus forest. In this special case, its hypothesis that every cycle is edge-separating is unnecessary.

### Proof

If \(H\) is a tree, take \(M=\varnothing\). If every vertex has degree two, then \(H\) is a cycle, and deleting one edge suffices. Assume henceforth that neither case applies.

#### Step 1: Suppress the degree-two paths

Let
\[
B=\{v\in V(H):d_H(v)\in\{1,3\}\}.
\]
Suppress all degree-two vertices, obtaining a connected multigraph \(K\) on \(B\). Every edge \(e\in E(K)\) represents a path \(P_e\) in \(H\), with internal vertices of degree two. A loop represents a path whose two ends are the same vertex of \(B\). These paths have pairwise disjoint interiors.

Degrees in \(K\), counting loops twice, are one or three. In particular, \(|B|\ge 2\).

Call \(e\) **short** if \(P_e\) has length one, and **long** otherwise. Let \(K_0\) be the spanning subgraph consisting of the short edges.

The short-edge graph is precisely \(H[B]\). Its degree-one vertices cannot lie on cycles, so the hypothesis on \(H[D]\) implies that \(K_0\) is a cactus forest. Since it is subcubic, its cycles are vertex-disjoint.

Contract each component of \(K_0\), and choose a spanning tree of the resulting connected multigraph. Let \(L\) be the corresponding set of long edges of \(K\). Then
\[
R=(B,E(K_0)\cup L)
\]
is a connected spanning cactus of \(K\), and its cycles are exactly those of \(K_0\).

Set
\[
Q=(B,E(K)\setminus E(R)).
\]
Every edge of \(Q\) is long. Also, \(R\) is connected and has at least two vertices, so
\[
d_Q(v)=d_K(v)-d_R(v)\le 2.
\]
Thus every nontrivial component of \(Q\) is a path or a cycle, allowing loops and two-edge cycles.

For a vertex \(v\) on a cycle of \(R\), we have \(d_Q(v)\le 1\). Moreover,
\[
v\text{ has an edge of }R\text{ outside that cycle}
\quad\Longrightarrow\quad d_Q(v)=0. \tag{1}
\]

#### Step 2: Choose compatible edges to break the cycles of \(R\)

We claim that one can choose a set \(A\), containing exactly one edge from every cycle of \(R\), such that, with
\[
Z=V(A),
\]
every nontrivial path component of \(Q\) has at most one endpoint in \(Z\).

All edges of \(A\) will be short. Since the cycles of \(R\) are vertex-disjoint, \(A\) will be a matching. Also, every vertex of \(Z\) has \(Q\)-degree at most one.

There are two cases.

**Case 1: \(R\) is a single cycle.**

Every vertex of \(K\) then has degree three, and \(Q\) is a perfect matching on \(B\). Choose an edge \(xy\) of \(R\) whose endpoints are not joined by an edge of \(Q\). Such an edge exists: a vertex has two distinct neighbors on \(R\), but only one neighbor in \(Q\).

Taking \(A=\{xy\}\) gives the required property.

**Case 2: \(R\) is not a single cycle.**

For every cycle \(C\) of \(R\), connectedness supplies a vertex \(p_C\in V(C)\) incident with an edge of \(R\) outside \(C\). By (1), \(p_C\) is isolated in \(Q\).

Let \(a_C,b_C\) be the two neighbors of \(p_C\) on \(C\). We will choose either \(p_Ca_C\) or \(p_Cb_C\) for \(A\).

Put
\[
U=\{a_C,b_C:C\text{ is a cycle of }R\}.
\]
Construct an auxiliary multigraph \(J\) on \(U\) with two types of edges:

- a **choice edge** \(a_Cb_C\) for each cycle \(C\);
- a **conflict edge** \(xy\) whenever \(x,y\in U\) are the two endpoints of the same nontrivial path component of \(Q\).

The choice edges form a perfect matching on \(U\). The conflict edges also form a matching, because a vertex can be an endpoint of only one component of \(Q\).

Consequently, \(J\) is the union of two matchings. Its cycles alternate between the two edge types and therefore have even length. Hence \(J\) is bipartite.

Properly color \(J\) black and white. For each \(C\), let \(q_C\) be the unique black vertex of \(\{a_C,b_C\}\), and choose
\[
A=\{p_Cq_C:C\text{ is a cycle of }R\}.
\]
The vertices \(p_C\) are isolated in \(Q\). If a path component of \(Q\) had both endpoints in \(Z\), those endpoints would therefore be two selected black vertices \(q_C,q_{C'}\). They would be joined by a conflict edge, contradicting the proper coloring.

This proves the claim. If \(R\) has no cycles, the construction simply gives \(A=\varnothing\).

#### Step 3: Orient the remaining long edges

Orient each cycle component of \(Q\) cyclically. Orient each nontrivial path component as a directed path, starting at its endpoint in \(Z\) if it has one; otherwise choose either direction.

The claim ensures that these orientations satisfy
\[
d_Q^-(v)\le 1\quad\text{for every }v,
\qquad
d_Q^-(z)=0\quad\text{for every }z\in Z. \tag{2}
\]
Marked vertices cannot lie on cycle components because their \(Q\)-degree is at most one.

For every oriented edge \(e\in E(Q)\), with head \(v\), select the edge \(f_e\) of its represented path \(P_e\) incident with \(v\). For a loop, choose the end-incidence corresponding to its orientation. Define
\[
M=A\cup\{f_e:e\in E(Q)\},
\]
identifying each short edge of \(A\) with its original edge in \(H\).

We verify that \(M\) is a matching.

- The edges of \(A\) are vertex-disjoint.
- Every \(P_e\), for \(e\in E(Q)\), has length at least two. Thus \(f_e\) has one endpoint in \(B\) and one internal vertex of \(P_e\).
- Distinct represented paths have disjoint interiors.
- By (2), the selected edges \(f_e\) have distinct endpoints in \(B\), and none of those endpoints lies in \(Z\).

Therefore no two edges of \(M\) meet.

#### Step 4: Verify that the complement is a spanning tree

Deleting one edge from every cycle of the connected cactus \(R\) leaves a spanning tree:
\[
R-A\text{ is a spanning tree of }K.
\]
Expand its edges back into their represented paths in \(H\). This gives a connected tree containing every vertex of \(B\).

For each \(e\in E(Q)\), exactly one edge of \(P_e\) was deleted. All its internal vertices remain connected to an endpoint of \(P_e\), and hence to the expanded tree. This also holds when \(e\) is a loop. Thus \(H-M\) is connected.

Finally,
\[
\begin{aligned}
|M|
&=|A|+|E(Q)|\\
&=|E(K)|-(|B|-1)\\
&=|E(H)|-|V(H)|+1,
\end{aligned}
\]
where the last equality uses invariance of the cycle rank under subdivision. Hence
\[
|E(H-M)|=|V(H)|-1.
\]
A connected graph with this many edges is a tree. This proves the lemma. \(\square\)

All steps are constructive. Suppression, finding \(R\), identifying the components of \(Q\), two-coloring \(J\), and lifting the selected edges can be implemented in linear time.

## 3. Applying the lemma to the cubic graph

We now prove the theorem.

Let
\[
H=G-S.
\]
For \(v\in V(H)\), cubicity gives
\[
d_H(v)=3
\quad\Longleftrightarrow\quad
v\text{ has no neighbor in }S.
\]
Therefore, if \(D\) denotes the degree-three vertices of \(H\),
\[
H[D]=G-N_G[S].
\]
By hypothesis this is a cactus forest, so the lemma gives a spanning tree \(T_H\) and a matching \(M\) partitioning \(E(H)\).

Every vertex of \(S\) has exactly two incident edges in \(G[S]\), and therefore exactly one incident edge joining it to \(H\). Let \(\delta_G(S)\) be this set of joining edges, and put
\[
T=T_H\cup\delta_G(S).
\]
This attaches every vertex of \(S\) as a leaf to \(T_H\). Thus \(T\) is a spanning tree of \(G\).

Consequently,
\[
E(G)=E(T)\,\dot\cup\,E(G[S])\,\dot\cup\,M.
\]
The middle part is a nonempty \(2\)-regular subgraph, exactly as required. \(\square\)

## 4. An explicit infinite family covered by the theorem

The sufficient condition permits arbitrary cubic graphs to occur as minors.

Start with any connected cubic graph \(F\). For every \(e\in E(F)\):

1. subdivide \(e\) once, introducing a vertex \(x_e\);
2. introduce a vertex \(y_e\);
3. join \(x_e\) to \(y_e\).

Finally, arrange all the vertices \(y_e\) into a cycle \(C\), in any cyclic order. Call the resulting graph \(G\).

Every vertex of \(G\) has degree three. Moreover:

- \(C\) is induced;
- \(G-V(C)\) is the once-subdivided copy of \(F\), hence connected;
- \(G-N_G[V(C)]\) consists of the original vertices of \(F\), with no edges.

The theorem therefore gives a 3-decomposition for every choice of \(F\) and every cyclic order of the vertices \(y_e\).

If \(F\) has \(b\) vertices, then \(G\) has \(4b\) vertices, and this construction uses
\[
|E(C)|=\frac{3b}{2},
\qquad
|M|=\frac b2+1.
\]
Also, \(F\) is a minor of \(G\); in particular, choosing nonplanar \(F\) produces nonplanar examples.

## 5. What remains unresolved

The result does **not** establish that every connected cubic graph has a set \(S\) satisfying the theorem. The uncontrolled cases are those in which, after selecting an induced cycle family with connected complement, the remaining degree-three core has overlapping cycles rather than cactus structure. The auxiliary two-matching argument relies essentially on the vertex-disjointness of the cactus cycles.

Nor can the matching-decycling lemma simply be extended to arbitrary subcubic graphs. Subdividing one edge of \(K_4\) gives a graph with five vertices and seven edges. A tree–matching decomposition would require a matching of size
\[
7-(5-1)=3,
\]
which is impossible on five vertices. Its degree-three core is \(K_4\) minus an edge, which is not a cactus. This is not a counterexample to the stated 2-Decomposition Conjecture: it has a triangle whose edge deletion leaves a connected graph.

Thus the conclusions established here are:

- an unconditional tree–matching decomposition theorem for subcubic graphs with cactus degree-three core;
- the resulting constructive cycle-neighborhood criterion for the 3-Decomposition Conjecture.

No proof or counterexample for the general conjecture is obtained, and I have not verified whether these sufficient conditions are already present in the literature.