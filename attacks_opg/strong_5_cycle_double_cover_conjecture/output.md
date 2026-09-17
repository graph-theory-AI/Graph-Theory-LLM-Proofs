```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an exact-member criterion that yields the conjecture for non-3-edge-colourable cubic graphs whenever deleting the prescribed circuit leaves a 3-edge-colourable graph.",
  "would_publish": false,
  "caveats": "The general containment problem is not settled here; novelty of the criterion is not claimed."
}
```

## 1. Partial result

The distinction between **containing \(C\)** and **having \(C\) itself as a cover member** is important here. I obtain a complete criterion for the latter, more restrictive requirement.

Throughout, a 3-edge-colouring is a proper edge-colouring using at most three colours; it is applied to subcubic graphs as well as cubic ones.

**Theorem.** Let \(C\) be a circuit in a bridgeless cubic graph \(G\). The following are equivalent:

1. \(G\) has a cycle double cover with at most five members, one of which is exactly \(C\).
2. \(G-V(C)\) is 3-edge-colourable.

If \(G\) is not 3-edge-colourable, the cover in (1) necessarily consists of **exactly five distinct nonempty cycles**. Thus, in that case, it is a five-cycle double cover in the formulation of the question, without any empty-member convention.

In particular, this proves the requested conclusion for non-3-edge-colourable cubic graphs whenever:

- \(G-V(C)\) is bipartite; or
- \(G-V(C)\) has maximum degree at most two—for example, whenever every vertex outside \(C\) has a neighbour on \(C\).

The proof is self-contained. No claim of novelty is made.

---

## 2. A parity lemma

The main ingredient is an elementary existence lemma.

**Lemma.** Let \(A=\mathbb F_2^2\). For distinct \(i,j\in\{1,\dots,r\}\), let
\[
B_{ij}:A\times A\longrightarrow \mathbb F_2
\]
be bilinear, with
\[
B_{ij}(x,y)=B_{ji}(y,x).
\]
There exist \(x_1,\dots,x_r\in A\setminus\{0\}\) such that
\[
\sum_{j\ne i}B_{ij}(x_i,x_j)=0
\qquad\text{for every }i.
\]
Indeed, the number of such choices is odd.

**Proof.** Put
\[
d_i(x_1,\dots,x_r)=\sum_{j\ne i}B_{ij}(x_i,x_j).
\]
The number \(N\) of solutions, reduced modulo two, is
\[
N\equiv
\sum_{x_1,\dots,x_r\in A\setminus\{0\}}
\prod_{i=1}^r(1+d_i).
\tag{1}
\]

For any linear functional \(\ell:A\to\mathbb F_2\),
\[
\sum_{x\in A\setminus\{0\}}\ell(x)=0.
\tag{2}
\]

Expand the product in (1). A nonconstant term is obtained by choosing a nonempty set \(I\subseteq\{1,\dots,r\}\), and for each \(i\in I\) choosing one factor \(B_{i,j_i}\), where \(j_i\ne i\). Represent it by directed edges \(i\to j_i\).

If the underlying undirected multigraph has a vertex of degree one, summing over the variable at that vertex annihilates the term by (2).

Otherwise every active vertex has degree at least two. There are \(|I|\) edges and at least \(|I|\) active vertices, since all vertices of \(I\) are active. Consequently there are exactly \(|I|\) active vertices, all have degree two, and the directed graph is a disjoint union of directed cycles.

Terms having a directed cycle of length at least three cancel in pairs: reverse the long cycle containing the least-numbered vertex among all long cycles. The product is unchanged, by the symmetry of the \(B_{ij}\), but the selected directed edges change.

The remaining nonconstant terms consist solely of directed 2-cycles. A 2-cycle contributes
\[
B_{ij}(x_i,x_j)B_{ji}(x_j,x_i)
=B_{ij}(x_i,x_j)^2
=B_{ij}(x_i,x_j).
\]
Summing over one endpoint again gives zero by (2).

Thus only the constant term survives. Its sum is \(3^r\), which is odd. Hence \(N\) is odd and in particular positive. \(\square\)

---

## 3. Necessity of the colouring condition

Set
\[
H=G-E(C),
\]
retaining all vertices. Vertices on \(C\) have degree one in \(H\), and all other vertices have degree three.

First observe that
\[
H\text{ is 3-edge-colourable}
\quad\Longleftrightarrow\quad
G-V(C)\text{ is 3-edge-colourable}.
\tag{3}
\]
One direction is restriction. For the other, extend a colouring of \(G-V(C)\) by assigning its missing colours to the edges from each outside vertex to \(C\). There is no conflict at a vertex on \(C\), which has only one incident edge in \(H\). Chords of \(C\) are isolated-edge components of \(H\) and can be coloured arbitrarily.

Suppose now that
\[
C,D_x\quad(x\in A=\mathbb F_2^2)
\]
is a cycle double cover, padding with empty \(D_x\)'s if necessary.

An edge of \(H\) belongs to precisely two of the \(D_x\)'s. If those indices are \(x,y\), colour the edge by
\[
\kappa(e)=x+y\in A\setminus\{0\}.
\]

At a vertex outside \(C\), the sum of the three incident edge colours is zero: each index \(x\) contributes either zero or twice, because \(D_x\) is even at that vertex. Three nonzero elements of \(\mathbb F_2^2\) with sum zero must be the three distinct nonzero elements. Thus \(\kappa\) is a proper 3-edge-colouring of \(H\).

Together with (3), this proves necessity.

---

## 4. Sufficiency: eliminating the component obstructions

Assume that \(H\) has a proper 3-edge-colouring
\[
\kappa:E(H)\longrightarrow A\setminus\{0\}.
\]
Identify the additive group \(A\) with the field \(\mathbb F_4\).

Write
\[
C=v_1v_2\cdots v_m v_1.
\]
Let \(b_i\) be the colour of the unique edge of \(H\) incident with \(v_i\).

For a component \(K\) of \(H\), put
\[
I_K=\{i:v_i\in V(K)\}.
\]
Summing incident colours over the vertices of \(K\) gives
\[
\sum_{i\in I_K}b_i=0.
\tag{4}
\]
Indeed, every edge is counted twice, and at each degree-three vertex the three colours sum to zero.

### 4.1 Independent recolouring of the components

For each component \(K\), choose a scalar
\[
t_K\in\mathbb F_4\setminus\{0\}
\]
and multiply every colour in \(K\) by \(t_K\). This preserves proper 3-edge-colouring.

Let
\[
a_i=t_Kb_i\quad(i\in I_K),\qquad
s_0=0,\qquad
s_i=\sum_{j=1}^i a_j.
\]
By (4), \(s_m=0=s_0\).

We will choose the scalars so that a certain parity obstruction vanishes in every component.

Let
\[
W=\mathbb F_2^{A},
\]
with unit vectors \(u_x\), indexed by \(x\in A\), and put
\[
h=\sum_{x\in A}u_x.
\]
Define
\[
\pi:W\longrightarrow\mathbb F_2\oplus A,
\qquad
\pi(u_x)=(1,x).
\]
This map has kernel \(\{0,h\}\).

For each component \(K\), define its boundary vector
\[
w_K=\sum_{i\in I_K}\bigl(u_{s_{i-1}}+u_{s_i}\bigr).
\tag{5}
\]
Since
\[
\pi(w_K)=\left(0,\sum_{i\in I_K}a_i\right)=0,
\]
we can write
\[
w_K=\delta_K h,\qquad \delta_K\in\mathbb F_2.
\]

We claim that the \(t_K\)'s can be chosen nonzero so that every \(\delta_K\) is zero.

### 4.2 The obstructions are symmetric bilinear interactions

Choose coordinates \(A=\mathbb F_2^2\), and define
\[
q(x_1,x_2)=x_1x_2,
\qquad
\beta(x,y)=x_1y_2+x_2y_1.
\]
Thus
\[
q(x+y)=q(x)+q(y)+\beta(x,y).
\]

Reading the coordinate indexed by \((1,1)\) in (5) gives
\[
\begin{aligned}
\delta_K
&=\sum_{i\in I_K}\bigl(q(s_{i-1})+q(s_i)\bigr)\\
&=\sum_{i\in I_K}q(a_i)
  +\sum_{i\in I_K}\sum_{j<i}\beta(a_j,a_i).
\end{aligned}
\tag{6}
\]
The terms involving only indices in \(I_K\) sum to
\[
q\left(\sum_{i\in I_K}a_i\right)=0.
\]
Consequently
\[
\delta_K=\sum_{L\ne K}B_{KL}(t_K,t_L),
\tag{7}
\]
where
\[
B_{KL}(t,u)=
\sum_{\substack{i\in I_K,\ j\in I_L\\j<i}}
\beta(ub_j,tb_i).
\]
These are bilinear over \(\mathbb F_2\).

Moreover,
\[
\begin{aligned}
B_{KL}(t,u)+B_{LK}(u,t)
&=\sum_{i\in I_K,\ j\in I_L}\beta(tb_i,ub_j)\\
&=\beta\left(t\sum_{i\in I_K}b_i,\,
             u\sum_{j\in I_L}b_j\right)\\
&=0
\end{aligned}
\]
by (4). Thus they satisfy the symmetry hypothesis of the parity lemma.

The lemma supplies nonzero scalars \(t_K\) for which
\[
\delta_K=0\quad\text{for all }K,
\qquad\text{hence}\qquad
w_K=0\quad\text{for all }K.
\tag{8}
\]

---

## 5. Lifting the colouring to four cycles

Fix scalars satisfying (8), and let \(\kappa'\) denote the resulting colouring of \(H\).

We assign a vector \(L(e)\in W\) to every edge.

For a circuit edge \(e_i=v_iv_{i+1}\), set
\[
L(e_i)=u_{s_i}.
\]
For an edge \(e\in E(H)\), initially set
\[
L(e)=u_0+u_{\kappa'(e)}.
\]

Thus circuit edges have labels of weight one, and edges of \(H\) have labels of weight two.

At every vertex \(v\),
\[
\pi\left(\sum_{e\ni v}L(e)\right)=0.
\]
Outside \(C\), this follows from proper 3-edge-colouring. At \(v_i\in C\), it follows from
\[
s_{i-1}+s_i=a_i.
\]
Hence the vertex defect
\[
d(v)=\sum_{e\ni v}L(e)
\]
is either \(0\) or \(h\).

For a component \(K\) of \(H\), summing these defects gives
\[
\sum_{v\in V(K)}d(v)=w_K=0:
\]
labels on edges of \(H\) cancel twice, leaving exactly the boundary expression (5). Therefore \(K\) contains an even number of vertices with defect \(h\).

In each component \(K\), choose an edge set \(J_K\subseteq E(K)\) whose odd-degree vertices are precisely the vertices with defect \(h\). Such an edge set exists for every even vertex subset of a connected graph; it can be found on a spanning tree.

For every edge in \(J_K\), replace its label \(L(e)\) by
\[
L(e)+h.
\]
This corrects all vertex defects. It also preserves weight two on \(H\), since adding \(h\) replaces a two-element subset of the four coordinates by its complementary pair. No label on \(C\) is changed.

We now have
\[
\sum_{e\ni v}L(e)=0
\qquad\text{at every vertex }v.
\tag{9}
\]

For \(x\in A\), let \(D_x\) consist of the edges whose \(x\)-coordinate in \(L(e)\) is one. By (9), every vertex has even degree in \(D_x\). Since \(G\) is cubic, every nonisolated vertex of \(D_x\) has degree two. Thus each \(D_x\) is a cycle in the problem's sense.

Every edge of \(C\) belongs to exactly one \(D_x\), and every edge outside \(C\) belongs to exactly two. Therefore
\[
\boxed{\quad C,\ D_x\ (x\in A)\quad}
\]
is a cycle double cover with at most five members, containing \(C\) as an entire member. This proves sufficiency.

### Why there are exactly five members in the non-colourable case

Any cycle double cover of a cubic graph with at most four members yields a proper 3-edge-colouring: index four members by \(A=\mathbb F_2^2\), and colour an edge by the sum of its two member-indices. The same argument used in Section 3 proves properness.

Thus, if \(G\) is not 3-edge-colourable, none of the five constructed members can be empty.

Also, two nonempty members of a cubic cycle double cover cannot coincide. At a vertex of two identical members, two incident edges would already be covered twice. The third incident edge could then belong to no even cover member, since such a member would need another incident edge at that vertex.

Hence the five members are distinct and nonempty. \(\square\)

---

## 6. Concrete consequences and an explicit construction bound

### Easily checked sufficient conditions

For a non-3-edge-colourable bridgeless cubic graph, the theorem proves the conjecture for the prescribed \(C\) in either of the following situations.

1. **\(G-V(C)\) is bipartite.**  
   A bipartite graph of maximum degree at most three has a proper 3-edge-colouring. This follows, for example, by embedding it in a 3-regular bipartite multigraph and successively removing perfect matchings using Hall's theorem.

2. **\(\Delta(G-V(C))\le 2\).**  
   Its components are paths and circuits, all properly edge-colourable with at most three colours.

Another consequence is the following graph-wide special case:

> If \(G\) is not 3-edge-colourable, but \(G-\{u,v\}\) is 3-edge-colourable for every edge \(uv\), then the strong five-cycle double cover conclusion holds for every circuit of \(G\).

Indeed, choose an edge \(uv\) of the prescribed circuit \(C\). Then \(G-V(C)\) is a subgraph of \(G-\{u,v\}\).

### Explicit search algorithm

Given a proper 3-edge-colouring of \(H=G-E(C)\), let \(r\) be the number of components of \(H\).

The proof gives an algorithm:

1. Enumerate the \(3^r\) nonzero scalar choices \((t_K)\).
2. For each choice, compute the prefix values \(s_i\) and boundary vectors \(w_K\).
3. Stop at a choice with every \(w_K=0\); the parity lemma guarantees that one exists.
4. Correct vertex defects on spanning trees of the components of \(H\).
5. Output \(C\) and the four coordinate supports.

The running time, **given the initial colouring**, is
\[
O\!\left(3^r\bigl(|V(G)|+|E(G)|\bigr)\right).
\]
This is a specified construction, not a claim of executed computational checks.

---

## 7. The precise gap: \(C\) may need additional components

The theorem does not cover every prescribed circuit. In fact, insisting that \(C\) itself be a member is genuinely too strong.

Let \(Q\) be a simple bridgeless cubic graph that is not 3-edge-colourable, such as the Petersen graph. Replace a vertex \(v\) of \(Q\) by a triangle, attaching its three vertices to the three former neighbours of \(v\). Call the resulting graph \(G\), and let \(C\) be the new triangle. The graph \(G\) is cubic and bridgeless.

Here
\[
G-V(C)=Q-v
\]
is not 3-edge-colourable. To see this, suppose it had such a colouring, using the nonzero elements of \(\mathbb F_2^2\). Let \(d_1,d_2,d_3\) be the missing colours at the three former neighbours of \(v\). Summing incident colours over \(Q-v\) gives
\[
d_1+d_2+d_3=0.
\]
Since all three are nonzero, they are distinct. Assigning these colours to the three edges incident with a restored vertex \(v\) would 3-edge-colour \(Q\), a contradiction.

By the theorem, this \(G\) has **no** cycle double cover with at most five members having the triangle \(C\) itself as a member.

This is **not** a counterexample to the stated conjecture. The conjecture allows the relevant member to be
\[
C\cup D,
\]
where \(D\) is a nonempty union of circuits vertex-disjoint from \(C\).

That is the unresolved part of this attack: when \(G-V(C)\) is not 3-edge-colourable, the argument provides no method for choosing the necessary additional circuits \(D\). The partial result establishes the colourable-complement case, but does not settle that extension problem.