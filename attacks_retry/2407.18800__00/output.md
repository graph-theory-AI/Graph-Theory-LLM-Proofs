```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The equivalence holds with at most 15 contractible triangles, and a separate argument proves 5-choosability for an infinite family of 6-regular toroidal triangulations.",
  "would_publish": false,
  "caveats": "The full conjecture is not settled; novelty of these partial results has not been checked against the literature."
}
```

# Partial results

All graphs are finite and simple. Criticality for 5-choosability means **global** criticality: the graph is not 5-choosable, but every proper subgraph is 5-choosable. In particular, \(K_7\) is not critical in this sense, since it contains \(K_6\).

I obtain two results.

### Theorem A
Let \(G\) have a fixed embedding in the torus with at most \(15\) distinct contractible triangles. Then
\[
G\text{ is 5-choosable}\quad\Longleftrightarrow\quad
G\text{ is 5-colorable}.
\]
Consequently, within this class, criticality for 5-choosability is equivalent to 6-criticality.

Here the hypothesis counts **all contractible 3-cycles**, not just facial triangles.

### Theorem B
Let \(T(r,s,t)\) be the twisted triangular torus grid defined in Section 5 below. If
\[
r\ge 3,\qquad s\ge 3,\qquad 3\mid s,
\]
then \(T(r,s,t)\) is 5-choosable, for every twist \(t\).

These graphs are 6-regular toroidal triangulations. The family includes graphs of arbitrarily large edge-width, so the argument does not require noncontractible triangles.

The minimal-counterexample, small-order, and cellularity reductions used in the previous attempt check out under the stated definition of criticality. The improvement in Theorem A comes from an additional reduction: **a minimal counterexample cannot have a \(K_5\) consisting of degree-5 vertices**.

## 1. Established coloring tools

I use the following proved results.

1. **Degree-choosability theorem.** A connected graph is colorable from every assignment satisfying
   \[
   |L(v)|\ge d(v)
   \]
   if and only if it is not a Gallai tree. A Gallai tree is a connected graph whose blocks are complete graphs or odd cycles.

2. **Thomassen’s planar list-coloring extension theorem**, in this standard consequence:

   > Let \(P\) be a plane graph. Give every interior vertex a list of size at least five and every vertex incident with the outer face a list of size at least three, except possibly one outer-face vertex whose list need only be nonempty. Then \(P\) is list-colorable.

   For a 2-connected graph, this follows from the usual precolored-outer-edge version by selecting a color at the exceptional vertex and a different color at an outer-face neighbor. The general version follows by block decomposition. It includes planar 5-choosability.

3. **Ohba’s theorem.** If
   \[
   |V(G)|\le 2\chi(G)+1,
   \]
   then \(\operatorname{ch}(G)=\chi(G)\).

The polynomial argument used for Theorem B is given explicitly.

## 2. A topological reduction and a reducible \(K_5\)

### Lemma 1
Every embedding of a connected nonplanar graph in the torus is cellular.

#### Proof
Let \(N\) be a connected regular neighborhood of the embedded graph. If \(N\) had genus zero, capping its boundary components would give a planar embedding. Thus \(N\) has genus one.

Write \(b\) for the number of boundary components of \(N\). Then
\[
\chi(N)=-b.
\]
Let \(F_1,\dots,F_a\) be the complementary surfaces, with genera \(g_i\) and numbers of boundary components \(b_i\). We have
\[
\sum_i b_i=b
\quad\text{and}\quad
0=\chi(N)+\sum_i\chi(F_i),
\]
so
\[
\sum_i\chi(F_i)=b.
\]
But
\[
\chi(F_i)=2-2g_i-b_i\le b_i,
\]
with equality precisely when \(F_i\) is a disk. Equality must hold for every \(i\). Thus every complementary component is a disk. ∎

### Proposition 2
Let \(G\) be a \(K_6\)-free toroidal graph containing a \(K_5\), denoted by \(K\), such that every vertex of \(K\) has degree at most five in \(G\). Then \(G\) is 5-choosable.

#### Proof
Fix an arbitrary 5-list assignment \(L\).

There are at most five edges between \(K\) and \(G-V(K)\), since each vertex of \(K\) already has four neighbors in \(K\). Color \(K\) from its lists; this is possible because \(K_5\) is 5-choosable.

By Lemma 1, the embedding of \(K\) is cellular. Consequently, each component \(D\) of \(G-V(K)\) lies in a disk face of \(K\). Viewed as a plane graph in that disk, every vertex of \(D\) adjacent to \(K\) is incident with the outer face of \(D\).

For \(v\in V(D)\), delete the colors used on its neighbors in \(K\), obtaining a residual list \(L'(v)\). Put
\[
r(v)=|N_G(v)\cap V(K)|.
\]
Then
\[
|L'(v)|\ge 5-r(v).
\]

Since there are at most five edges leaving \(K\), at most one vertex outside \(K\) has \(r(v)\ge3\). Moreover, \(r(v)\le4\), because a vertex adjacent to all five vertices of \(K\) would give a \(K_6\).

Thus:

- interior vertices of \(D\) retain five colors;
- outer-face vertices have at least three colors, except possibly one;
- that exceptional vertex still has a nonempty list.

The planar extension theorem colors \(D\). Doing this for every component extends the coloring of \(K\) to \(G\).

Since \(L\) was arbitrary, \(G\) is 5-choosable. ∎

This is the additional reduction missing from the previous attempt.

## 3. A stronger density restriction on a minimal counterexample

Suppose \(G\) is toroidal, 5-colorable, and not 5-choosable. Choose an inclusion-minimal non-5-choosable subgraph \(H\). Set
\[
n=|V(H)|,\qquad m=|E(H)|,\qquad
E=2m-5n.
\]

The graph \(H\) is connected, remains 5-colorable, and satisfies
\[
\delta(H)\ge5.
\]
The last assertion follows by coloring \(H-v\) and then extending to a vertex of degree at most four.

Also, \(H\) is nonplanar by planar 5-choosability, so its inherited torus embedding is cellular by Lemma 1.

### Small-order exclusion

We have
\[
n\ge12.
\]

Indeed, every 5-colorable graph on at most eleven vertices is 5-choosable. For orders between five and eleven, refine a proper coloring into exactly five nonempty independent sets and complete the graph to a complete 5-partite graph \(J\). Then
\[
\chi(J)=5,\qquad |V(J)|\le11,
\]
so Ohba’s theorem gives \(\operatorname{ch}(J)=5\). Graphs of smaller order are immediate.

### The low-degree subgraph

Define
\[
S=\{v\in V(H):d_H(v)=5\},\qquad
T=V(H)\setminus S,
\]
and write
\[
s=|S|,\qquad t=|T|.
\]
If \(S\ne\varnothing\), let \(c\) be the number of components of \(H[S]\).

### Lemma 3
Every component of \(H[S]\) is a Gallai tree, and its complete blocks have order at most four.

#### Proof
Choose a bad list assignment \(L\) on \(H\), with every list of size five.

Let \(C\) be a component of \(H[S]\). Color \(H-V(C)\), which is possible by minimality. After deleting colors used on neighbors outside \(C\), each \(v\in V(C)\) has at least
\[
5-\bigl(5-d_C(v)\bigr)=d_C(v)
\]
available colors. If \(C\) were not a Gallai tree, the degree-choosability theorem would extend the coloring, a contradiction.

A complete block cannot have order at least six, since \(H\) is 5-colorable. A \(K_5\) block would consist of five vertices having degree five in \(H\), and Proposition 2 would make \(H\) 5-choosable. Thus complete blocks have order at most four. ∎

### Lemma 4
If \(S\ne\varnothing\), then
\[
\boxed{\quad E\ge \frac{5n+12c}{29}.\quad}
\]

#### Proof
Let \(b_4\) be the number of \(K_4\) blocks of \(H[S]\).

Two \(K_4\) blocks cannot share a vertex: such a vertex would have at least six neighbors in \(H[S]\), whereas its degree in \(H\) is five. Hence
\[
4b_4\le s.
\]

For a block \(B\) other than \(K_4\),
\[
|E(B)|\le \frac32\bigl(|V(B)|-1\bigr).
\]
This holds for \(K_2\), \(K_3\), and odd cycles. For \(K_4\), the excess over this bound is \(3/2\).

Using the block identity
\[
\sum_B\bigl(|V(B)|-1\bigr)=s-c,
\]
we obtain
\[
\begin{aligned}
|E(H[S])|
&\le \frac32(s-c)+\frac32b_4\\
&\le \frac{15}{8}s-\frac32c.
\end{aligned}
\]
Therefore
\[
e(S,T)=5s-2|E(H[S])|
   \ge \frac54s+3c.
\]

On the other hand,
\[
e(S,T)\le \sum_{v\in T}d_H(v)=5t+E.
\]
Since every vertex of \(T\) has degree at least six,
\[
t\le E.
\]
Combining these inequalities gives
\[
5(n-t)+12c\le20t+4E,
\]
and consequently
\[
5n+12c\le25t+4E\le29E.
\]
This proves the claim. ∎

If \(S=\varnothing\), then directly
\[
E=\sum_v(d_H(v)-5)\ge n.
\]
In fact, Euler’s inequality forces equality in this case: \(H\) is a 6-regular triangulation.

Thus a minimal counterexample has the following strengthened structure:

- \(n\ge12\);
- the degree-5 vertices induce a Gallai forest with clique blocks of order at most four;
- if that forest has \(c\ge1\) components, then
  \[
  2m-5n\ge\frac{5n+12c}{29}.
  \]

## 4. At least sixteen contractible facial triangles

Let \(f\) be the number of faces of \(H\), and let \(f_3\) count the triangular faces.

Because \(H\) is simple and has minimum degree at least five, every face boundary has length at least three. Euler’s formula gives
\[
f=m-n.
\]
Counting edge-sides,
\[
2m\ge3f_3+4(f-f_3),
\]
and therefore
\[
f_3\ge4f-2m
     =2m-4n
     =n+E.
\]

We now show that \(n+E\ge16\).

If \(S=\varnothing\), then
\[
n+E\ge2n\ge24.
\]

Otherwise, Lemma 4 and \(n\ge12\), \(c\ge1\) give
\[
n+E\ge\frac{34n+12c}{29}
       \ge\frac{420}{29}>14.
\]
But
\[
n+E=2m-4n
\]
is even. Hence \(n+E\ge16\), as required.

Every triangular face is bounded by a genuine contractible 3-cycle. Different triangular faces have different boundary triangles: if both sides of one triangle were faces, each of its vertices would have degree two, contrary to \(\delta(H)\ge5\).

We have proved:

### Proposition 5
Every 5-colorable, non-5-choosable toroidal graph contains a minimal non-5-choosable subgraph whose inherited embedding has at least sixteen distinct contractible facial triangles.

In particular, the original embedded graph contains at least sixteen distinct contractible triangles.

### Proof of Theorem A

If \(G\) had at most fifteen contractible triangles and were 5-colorable but not 5-choosable, Proposition 5 would be a contradiction. The reverse implication follows by assigning the same five colors to every vertex.

The class of embedded graphs with at most fifteen contractible triangles is hereditary under taking subgraphs. Therefore the equivalence also yields the criticality formulation:

- a choice-critical graph in this class is not 5-colorable, while every proper subgraph is 5-colorable;
- a 6-critical graph in this class is not 5-choosable, while every proper subgraph is 5-choosable.

Thus choice-criticality and 6-criticality coincide in this class. ∎

## 5. An infinite family in the 6-regular case

Here is a separate argument treating some dense triangulations left untouched by the counting method.

### Definition of \(T(r,s,t)\)

For \(r,s\ge3\) and \(t\in\mathbb Z_s\), let
\[
V(T(r,s,t))=\{0,\ldots,r-1\}\times\mathbb Z_s.
\]
Its edges are:

1. horizontal edges
   \[
   (i,j)(i,j+1);
   \]
2. for \(0\le i<r-1\), edges
   \[
   (i,j)(i+1,j),\qquad (i,j)(i+1,j+1);
   \]
3. seam edges
   \[
   (r-1,j)(0,j+t),\qquad
   (r-1,j)(0,j+t+1).
   \]

This is a quotient of the triangular lattice. It is simple, 6-regular, and has its natural triangular embedding in the torus.

The key coloring fact is the following.

### Lemma 6
If \(\ell\ge6\) and \(3\mid\ell\), then the square \(C_\ell^2\) is 3-choosable.

#### Proof
Index the vertices cyclically by \(0,\ldots,\ell-1\), and consider
\[
P(x_0,\ldots,x_{\ell-1})
 =\prod_{i=0}^{\ell-1}
   (x_i-x_{i+1})(x_i-x_{i+2}),
\]
with subscripts modulo \(\ell\). This is a graph-coloring polynomial for \(C_\ell^2\), of total degree \(2\ell\).

We calculate the coefficient
\[
a=[x_0^2\cdots x_{\ell-1}^2]P.
\]
Put \(A=\{0,1,2\}\) and
\[
F(x)=\prod_{a\in A}(x-a).
\]
The multivariate Lagrange coefficient identity gives
\[
a=
\sum_{\phi\in A^\ell}
\frac{P(\phi)}
     {\prod_i F'(\phi_i)}.
\]

Only proper 3-colorings of \(C_\ell^2\) contribute. Such a coloring must repeat a permutation of \(0,1,2\) with period three, so there are exactly six of them.

For each such coloring, the colors \(\phi_{i+1}\) and \(\phi_{i+2}\) are the two elements of \(A\setminus\{\phi_i\}\). Consequently,
\[
(\phi_i-\phi_{i+1})(\phi_i-\phi_{i+2})
   =F'(\phi_i).
\]
Every nonzero summand is therefore \(1\), and
\[
a=6\ne0.
\]

Now take arbitrary lists of size three, identifying their colors with distinct real numbers. Apply the same coefficient identity using these three-element sets in place of \(A\) at the respective vertices. If \(P\) vanished on every choice from the lists, its displayed coefficient would be zero, contrary to \(a=6\).

Thus some choice from the lists makes \(P\ne0\), which is a proper coloring. ∎

The coefficient identity used here follows from univariate Lagrange interpolation in each variable; the total-degree bound \(2\ell\) ensures that it extracts the indicated coefficient.

### Proof of Theorem B

Fix an arbitrary 5-list assignment on \(T(r,s,t)\), where \(3\mid s\).

First color rows
\[
0,1,\ldots,r-3
\]
in this order. When coloring a row other than the first, each vertex has at most two already colored neighbors outside that row. Hence every vertex retains at least three available colors. The row is a cycle, so it can be colored from these residual lists.

Two consecutive rows remain, numbered \(r-2\) and \(r-1\). Write
\[
a_j=(r-2,j),\qquad b_j=(r-1,j).
\]
Their induced subgraph is \(C_{2s}^2\), in the cyclic order
\[
b_0,a_0,b_1,a_1,\ldots,b_{s-1},a_{s-1}.
\]

Each vertex in these two rows has exactly two neighbors outside them. It therefore retains at least three available colors. Since
\[
3\mid 2s,
\]
Lemma 6 colors the remaining induced subgraph.

This completes an arbitrary 5-list coloring. ∎

For example, \(T(3q,3q,0)\), with \(q\ge2\), has edge-width \(3q\): in the triangular-lattice cover, a noncontractible closed walk must accumulate a nonzero period displacement, requiring at least \(3q\) steps, and a horizontal row realizes that length. Thus these examples have no noncontractible triangles and have arbitrarily large edge-width.

## 6. What remains open in this attack

Neither argument proves the full conjecture.

The density restriction
\[
2m-5n\ge\frac{5n+12c}{29}
\]
is compatible with the toroidal upper bound \(m\le3n\). It does not force a forbidden subgraph or a list coloring when there are many contractible triangles.

The grid argument also has a genuine limitation. When \(3\nmid s\), the remaining graph \(C_{2s}^2\) is not even 3-colorable from a common three-color list, so this particular two-row completion cannot be used unchanged. This is a limitation of the argument, not evidence that the corresponding toroidal grid fails to be 5-choosable.

Accordingly, the rigorous conclusions are the improved sixteen-triangle obstruction bound, Theorem A, and the explicit 6-regular family in Theorem B. No counterexample to the full conjecture is produced, and no computational enumeration is claimed.