```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A prescribed-circuit extension criterion proves the conjecture for cubic graphs having a cycle that dominates all vertices.",
  "would_publish": false,
  "caveats": "The universal conjecture is not resolved; no novelty relative to existing extension theorems is claimed."
}
```

## 1. A precise partial result

I do not resolve the conjecture. I give a self-contained prescribed-circuit criterion and derive unconditional special cases.

Throughout, graphs are finite. The argument below is for simple cubic graphs; it also works for loopless cubic multigraphs with the usual cycle conventions.

### Theorem
Let \(G\) be a cubic graph, and let \(C\) be an ordinary cycle of \(G\). The following are equivalent:

1. \(G\) has a \((5,2)\)-cycle-cover in which **one entire binary-cycle member is exactly \(E(C)\)**.
2. \(G-V(C)\) has a proper edge-colouring with three colours.

The qualification “one entire member” matters: this is stronger than asking that \(C\) be a component of one member of a five-cycle cover.

Two immediate consequences are:

- If every vertex outside \(C\) has a neighbour on \(C\), then \(G\) has a \((5,2)\)-cycle-cover containing \(E(C)\) as a member. Indeed, \(G-V(C)\) then has maximum degree at most two.
- If \(G-V(C)\) is a forest, the same conclusion holds.

In particular, this proves the conjecture for **cycle-permutation graphs**: two vertex-disjoint cycles joined by an arbitrary perfect matching.

I prove the criterion below. No external theorem is needed.

---

## 2. Encoding covers by pairs of labels

Let \(\Omega\) be a set of five labels. Assign to each edge \(e\) a two-element set
\[
P(e)\in\binom{\Omega}{2}.
\]
For \(\omega\in\Omega\), put
\[
Z_\omega=\{e:\omega\in P(e)\}.
\]

Every edge belongs to exactly two of the sets \(Z_\omega\). In a cubic graph, all five sets are binary cycles precisely when the three edge-labels at every vertex form the three edges of a triangle on three labels of \(\Omega\).

To see necessity, form the multigraph on \(\Omega\) whose three edges are the labels on the three incident edges of \(G\). Every degree in this multigraph must be even. A loopless, three-edge multigraph with all degrees even must be a triangle. Sufficiency is immediate.

We shall use
\[
\Omega=\{\star\}\sqcup Q,\qquad Q=\mathbb F_2^2.
\]
Write
\[
[x,y]=x_1y_2+x_2y_1.
\]
For \(a\ne0\), the linear functional \(x\mapsto[a,x]\) has kernel \(\{0,a\}\). Thus the two pairs of elements of \(Q\) whose difference is \(a\) are distinguished by the value of this functional.

### Necessity in the theorem

Suppose \(Z_\star=E(C)\). At every vertex outside \(C\), the incident pair-labels form a triangle on three elements of \(Q\).

Colour an edge outside \(C\), labelled \(\{x,y\}\subset Q\), by \(x+y\). The three edge-colours at a vertex outside \(C\) are the three distinct nonzero elements of \(Q\). Restricting this colouring to \(G-V(C)\) gives a proper three-edge-colouring.

The substantive direction is sufficiency.

---

## 3. Two elementary lemmas

### Lemma 1: lifting a coloured graph with terminals

Let \(D\) be a connected graph whose vertices have degree one or three. Suppose its edges are properly coloured by \(Q\setminus\{0\}\).

At each degree-one vertex \(z\), prescribe a pair
\[
P_z=x_z+\{0,a_z\},
\]
where \(a_z\) is the colour of its incident edge.

There is an assignment of pairs from \(\binom Q2\) to the edges of \(D\), having:

- difference equal to the given edge-colour;
- prescribed pair \(P_z\) at every degree-one vertex;
- a triangle of pair-labels at every degree-three vertex,

if and only if
\[
\sum_{\deg(z)=1}\bigl(1+[a_z,x_z]\bigr)=0
\quad\text{in }\mathbb F_2. \tag{1}
\]

#### Proof

At a degree-three vertex \(v\), let \(t_v\in Q\) be the label missing from its triangle. The incident edge of colour \(a\) must receive
\[
Q\setminus\{t_v,t_v+a\}. \tag{2}
\]
As \(a\) ranges over the three nonzero elements, these are exactly the edges of the triangle on \(Q\setminus\{t_v\}\).

For an edge \(uv\) between degree-three vertices, agreement of the two endpoint prescriptions is equivalent to
\[
[a,t_u+t_v]=0. \tag{3}
\]
For an edge joining a degree-three vertex \(v\) to a degree-one vertex \(z\), it is equivalent to
\[
[a_z,t_v]=1+[a_z,x_z]. \tag{4}
\]

These are linear equations in the two coordinates of each \(t_v\).

Suppose \(D\) has a degree-three vertex. A linear dependence among the equation rows assigns coefficients \(r_e\in\mathbb F_2\) to edges such that, at every degree-three vertex,
\[
\sum_{e\ni v}r_e\,a(e)=0.
\]
Its three incident colours are the three nonzero vectors of \(Q\); their only nonempty zero-sum subset is the full set. Consequently the three coefficients \(r_e\) at \(v\) are equal.

Connectivity now forces every coefficient \(r_e\) to be equal. Hence the only nonzero row dependence is the sum of all rows. The system is therefore consistent exactly when the sum of its right-hand sides is zero, which is (1).

If \(D\) has no degree-three vertex, it is a single edge with two degree-one endpoints. Its two prescribed pairs agree exactly when
\[
[a,x_z]=[a,x_{z'}],
\]
again equivalent to (1). This covers the remaining case. ∎

### Lemma 2: an even-transversal lemma

Let \(X\) be a graph partitioned into sets
\[
W_1,\ldots,W_k
\]
of odd cardinality. Suppose every vertex has an even number of neighbours in each other part.

Then the number of transversals—one vertex from each \(W_i\)—whose induced subgraph has all degrees even is odd. In particular, such a transversal exists.

#### Proof

All counting in this proof is modulo two. For choices \(w_i\in W_i\), let
\[
b_{ij}(w_i,w_j)
\]
be their adjacency indicator, and let
\[
d_i=\sum_{j\ne i}b_{ij}(w_i,w_j).
\]
Since \(\sum_i d_i=0\), the selected subgraph is even precisely when \(d_1,\ldots,d_{k-1}\) vanish. Thus the parity of the number in question is
\[
\sum_{w_1,\ldots,w_k}\prod_{i=1}^{k-1}(1+d_i). \tag{5}
\]

Expand the product. A term is described by a directed graph on \(\{1,\ldots,k\}\): each vertex has outdegree at most one, vertex \(k\) has outdegree zero, and an arc \(i\to j\) contributes \(b_{ij}\).

If a vertex is incident with exactly one arc, summing over its choice \(w_i\) makes the term vanish, by the even-neighbour hypothesis.

A nonempty directed graph of this kind with no vertex incident with exactly one arc must be a disjoint union of directed cycles:

- A directed two-cycle contributes \(b_{ij}^2=b_{ij}\); summing over one endpoint again makes its contribution vanish.
- Terms containing only directed cycles of length at least three cancel in pairs by reversing the cycle containing the least-indexed nonisolated vertex. Reversal preserves the product of adjacency indicators and changes the directed graph.

Only the empty term remains. Its contribution is
\[
\prod_i |W_i|=1\pmod2.
\]
Therefore the desired number is odd. ∎

---

## 4. Proof of sufficiency

Assume \(H=G-V(C)\) is properly three-edge-coloured. Identify its colours with \(Q\setminus\{0\}\).

Write
\[
C=v_1v_2\cdots v_\ell v_1,
\]
and let
\[
D=G-E(C).
\]
Every vertex of \(C\) has degree one in \(D\), and every other vertex has degree three.

Extend the colouring of \(H\) to \(D\): at each vertex outside \(C\), assign the unused colours to its edges joining \(C\). A chord of \(C\), which is a single-edge component of \(D\), can receive any nonzero colour.

Let the components of \(D\) be \(D_1,\ldots,D_k\), and define
\[
I_i=\{r:v_r\in V(D_i)\}.
\]
Let \(A_r\ne0\) be the colour of the unique edge of \(D\) incident with \(v_r\).

Summing the edge-colours over the vertices of \(D_i\) gives
\[
\sum_{r\in I_i}A_r=0. \tag{6}
\]
Indeed, each degree-three vertex contributes the sum of the three nonzero elements of \(Q\), namely zero, while every edge is counted twice.

### 4.1 Independent colour rotations

Let \(R\) cyclically permute the three nonzero elements of \(Q\). This is a linear map and satisfies
\[
I+R+R^2=0. \tag{7}
\]

We may independently rotate the colours of each component \(D_i\), choosing an exponent
\[
s_i\in\{0,1,2\}.
\]
After doing so, put
\[
a_r=R^{s_i}A_r\qquad(r\in I_i).
\]

Define
\[
p_0=0,\qquad p_r=\sum_{q=1}^r a_q.
\]
Equation (6) implies \(p_\ell=0\). Also,
\[
p_r+p_{r-1}=a_r\ne0.
\]

Give the cycle edge \(v_rv_{r+1}\) the pair-label
\[
\{\star,p_r\}.
\]
At \(v_r\), the required pair on its edge outside \(C\) is then
\[
\{p_{r-1},p_r\}. \tag{8}
\]
The three pairs at \(v_r\) will form a triangle.

By Lemma 1, these boundary prescriptions extend through \(D_i\) precisely when
\[
\sigma_i
=
|I_i|+\sum_{r\in I_i}[a_r,p_{r-1}]
=0. \tag{9}
\]

It remains to choose the rotations so that all these conditions hold.

### 4.2 The obstruction is an interaction parity

We use the following identity. If \(b_1,\ldots,b_t\) are nonzero elements of \(Q\) with sum zero, then
\[
\sum_{r=1}^t
\left[b_r,\sum_{q<r}b_q\right]
=t\pmod2. \tag{10}
\]

For proof, let \(N_1,N_2,N_3\) be their three multiplicities. Zero sum means these multiplicities have the same parity, say \(\varepsilon\). The left side counts pairs with different labels, so it equals
\[
N_1N_2+N_1N_3+N_2N_3
=\varepsilon
=t\pmod2.
\]

Apply (10) to the subsequence indexed by \(I_i\). The interactions internal to \(I_i\) cancel the term \(|I_i|\) in (9). Hence
\[
\sigma_i=\sum_{j\ne i}B_{ij}(s_i,s_j), \tag{11}
\]
where
\[
B_{ij}(s,t)
=
\sum_{\substack{r\in I_i,\ q\in I_j\\q<r}}
[R^sA_r,R^tA_q]. \tag{12}
\]

These interaction functions have two crucial properties.

First,
\[
B_{ij}(s,t)=B_{ji}(t,s). \tag{13}
\]
Their sum is
\[
\left[\sum_{r\in I_i}R^sA_r,\,
      \sum_{q\in I_j}R^tA_q\right]=0
\]
by (6).

Second,
\[
\sum_{t=0}^2 B_{ij}(s,t)=0, \tag{14}
\]
by linearity and (7).

### 4.3 Eliminate all obstructions simultaneously

Construct a graph with parts
\[
W_i=\{(i,0),(i,1),(i,2)\},
\]
joining \((i,s)\) to \((j,t)\) exactly when \(B_{ij}(s,t)=1\).

Equation (13) makes this an undirected graph. Equation (14) says that every vertex has an even number of neighbours in each other part.

Lemma 2 supplies choices \((i,s_i)\) whose induced subgraph has all degrees even. By (11), these choices satisfy
\[
\sigma_i=0\qquad\text{for every }i.
\]

Lemma 1 now extends the prescribed pairs through every component of \(D\). Together with the pairs already assigned to \(C\), all incident triples are triangles. Therefore
\[
Z_\omega=\{e:\omega\in P(e)\},
\qquad \omega\in\{\star\}\sqcup Q,
\]
are five binary cycles covering every edge exactly twice.

Only the edges of \(C\) have labels containing \(\star\), so
\[
Z_\star=E(C).
\]

This proves sufficiency and the theorem. Notice that the single-edge case in Lemma 1 explicitly handles chords of \(C\), including the case \(H\) is empty. ∎

---

## 5. Consequences and an explicit example

### Vertex-dominating cycles

Suppose every vertex outside \(C\) has at least one neighbour on \(C\). Since \(G\) is cubic,
\[
\Delta(G-V(C))\le2.
\]
Every component of \(G-V(C)\) is a path, a cycle, or an isolated vertex, and therefore is properly three-edge-colourable. The theorem gives the required \((5,2)\)-cover.

In particular, the conclusion holds if \(C\) is edge-dominating, meaning that no edge has both endpoints outside \(C\).

### Cycle-permutation graphs

Suppose \(G\) consists of two disjoint cycles of equal length and a perfect matching between them. Taking either cycle as \(C\), its vertex-deleted complement is the other cycle. Thus every such graph has a \((5,2)\)-cover.

This family includes the Petersen graph, so the result is not confined to three-edge-colourable cubic graphs.

For an explicit check, write the Petersen graph with edges
\[
u_i u_{i+1},\qquad u_i v_i,\qquad v_i v_{i+2},
\]
with indices modulo five. The following five ordinary circuits give a \((5,2)\)-cover:
\[
\begin{aligned}
&u_0u_1u_2u_3u_4u_0,\\
&u_0u_4v_4v_1v_3v_0u_0,\\
&u_1u_2v_2v_4v_1u_1,\\
&u_0u_1v_1v_3u_3u_2v_2v_0u_0,\\
&u_3u_4v_4v_2v_0v_3u_3.
\end{aligned}
\]
Their lengths are \(5,6,5,8,6\), summing to \(30=2|E(G)|\), and direct inspection shows that each edge occurs exactly twice.

### A fully specified construction

Given a three-edge-colouring of \(G-V(C)\), the proof is algorithmic:

1. Extend it to \(D=G-E(C)\).
2. Compute the nine values \(B_{ij}(s,t)\) for each pair of components.
3. Enumerate the \(3^k\) rotation choices until all equations (11) vanish; Lemma 2 guarantees success.
4. Solve the linear systems in Lemma 1 by Gaussian elimination.
5. Read off the five edge sets from the resulting pair-labels.

With the initial colouring supplied, a direct implementation takes
\[
O(3^k k^2+|V(G)|^3)
\]
operations. In particular, when \(C\) is induced and \(G-V(C)\) is connected, \(k=1\), so no exponential search is needed.

---

## 6. What remains unresolved

This does **not** establish that an arbitrary bridgeless cubic graph has a cycle \(C\) whose vertex-deleted complement is three-edge-colourable.

Moreover, a member of a general five-cycle cover may be a disjoint union of several ordinary cycles. The proof above relies on arranging the terminal labels around **one** cyclic order; it does not automatically establish the analogous criterion for an arbitrary disconnected binary cycle.

If \(G-V(C)\) is not three-edge-colourable, the necessity argument rules out using that particular \(C\) as an entire cover member. It does not rule out a cover using different or disconnected members.

Finally, the supplied catalog already mentions prescribed-subgraph extension results. I have not independently established whether the criterion above duplicates one of them. It should be regarded as a proved, self-contained partial result—not a novelty claim or a resolution of the universal conjecture.