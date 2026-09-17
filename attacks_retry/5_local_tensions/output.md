```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every embedded graph of girth at least four admits a 4-local-tension, settling the triangle-free special case but not the full conjecture.",
  "would_publish": false,
  "caveats": "No novelty claim; the stronger girth hypothesis excludes contractible triangles, which remain untreated."
}
```

## 1. A special case with unrestricted genus and degree

I do not resolve the conjecture. I use a different route from the previous attempt and do not rely on its special-case assertions.

The partial result is the following.

**Theorem.** Let \(G\) be a finite graph of girth at least \(4\), embedded in a surface. Then \(G\) has a \(4\)-local-tension.

The embedding need not be cellular or orientable. There is no restriction on the genus or the maximum degree.

Here girth is understood in the multigraph sense: loops and pairs of parallel edges are cycles of lengths \(1\) and \(2\). In particular, the theorem applies to every simple triangle-free embedded graph.

On a fixed orientation, I use the equivalent signed-value convention
\[
1\leq |\phi(e)|\leq k-1.
\]
Reorienting negatively valued edges gives the positive-value convention in the question.

The proof uses a signed-flow lemma, proved below using the standard matroid base-packing theorem. I make no claim that this lemma or its embedded-graph consequence is new.

## 2. A signed-flow lemma

A signed graph can be represented by an incidence matrix \(B\) in which each edge has two end-incidences, each equal to \(+1\) or \(-1\).

- An edge is **positive** if its two incidences have opposite signs.
- It is **negative** if they have the same sign.

Loops are allowed: their two incidences contribute to the same matrix entry. An integer flow is a vector \(z\in\mathbb Z^{E}\) satisfying
\[
Bz=0.
\]

Switching at a vertex means multiplying its row of \(B\) by \(-1\). A signed graph is **balanced** if switching can make every edge positive; equivalently, every cycle contains an even number of negative edges.

**Lemma.** Let \(H\) be a connected signed graph such that

1. every nonempty proper vertex set has an edge cut of size at least \(4\); and
2. \(H\) admits a nowhere-zero integer flow.

Then \(H\) admits a nowhere-zero integer flow \(z\) with
\[
1\leq |z(e)|\leq 3.
\]

### 2.1. A necessary consequence of flow-admissibility

No switching of \(H\) can have exactly one negative edge.

Indeed, sum all equations in \(Bz=0\). Positive edges contribute zero to this sum. If \(e\) were the unique negative edge, the resulting equation would be
\[
\pm 2z(e)=0,
\]
contradicting \(z(e)\neq0\).

Consequently, if \(H\) is unbalanced, every switching has at least two negative edges.

### 2.2. Packing two connected spanning bases

Write \(n=|V(H)|\). Over \(\mathbb F_2\), let

- \(D\) be the ordinary vertex-edge incidence matrix of the underlying graph;
- \(s\) be the row vector indicating the negative edges.

Consider the binary matrix
\[
A=\begin{pmatrix}D\\s\end{pmatrix}
\]
and its column matroid \(M\).

For \(F\subseteq E(H)\), let \(c(F)\) denote the number of components of \((V(H),F)\), including isolated vertices. Define
\[
\epsilon(F)=
\begin{cases}
0,&\text{if the signed subgraph on }F\text{ is balanced},\\
1,&\text{otherwise}.
\end{cases}
\]
Its rank is
\[
r(F)=n-c(F)+\epsilon(F). \tag{1}
\]

To verify (1), the incidence matrix \(D_F\) has rank \(n-c(F)\). The additional row \(s_F\) lies in its row space exactly when \(s_F\) has even intersection with every cycle—exactly the balanced condition.

We apply the **matroid base-packing theorem**: a matroid \(M\) has two disjoint bases if and only if
\[
|E(H)\setminus F|\geq 2\bigl(r(E(H))-r(F)\bigr)
\qquad\text{for every }F\subseteq E(H). \tag{2}
\]

Here is the verification of (2).

If \(c(F)\geq2\), each component vertex set \(V_i\) is nonempty and proper. Every edge between two such sets belongs to \(E(H)\setminus F\), and hence
\[
2|E(H)\setminus F|
   \geq \sum_{i=1}^{c(F)}|\delta_H(V_i)|
   \geq 4c(F).
\]
Thus
\[
|E(H)\setminus F|\geq2c(F).
\]
By (1),
\[
r(E(H))-r(F)\leq c(F),
\]
so (2) follows.

Suppose instead that \(c(F)=1\). If \(r(F)=r(E(H))\), there is nothing to prove. The only other possibility is that \(H\) is unbalanced and \(F\) is balanced. Switch so that every edge of \(F\) is positive. By Section 2.1, at least two edges of \(H\) are then negative, both outside \(F\). Therefore
\[
|E(H)\setminus F|\geq2
   =2\bigl(r(E(H))-r(F)\bigr).
\]

We obtain disjoint bases \(B_1,B_2\) of \(M\).

Importantly, **each basis spans a connected underlying subgraph**. If \(H\) is balanced, a basis is a spanning tree. If \(H\) is unbalanced, (1) shows that a basis is a connected spanning unicyclic graph whose unique cycle is unbalanced.

### 2.3. Two even signed Eulerian subgraphs covering all edges

For each \(i\in\{1,2\}\), prescribe a vector \(x_i\in\mathbb F_2^{E(H)}\) by setting
\[
x_i(e)=1\qquad(e\notin B_i)
\]
and choosing the coordinates on \(B_i\) so that
\[
Ax_i=0.
\]
This is possible because the columns indexed by \(B_i\) form a basis of the column space of \(A\).

Let
\[
F_i=\{e:x_i(e)=1\}.
\]
Then:

- \(Dx_i=0\), so every vertex has even degree in \(F_i\);
- \(sx_i=0\), so \(F_i\) contains an even number of negative edges;
- \(F_i\) contains \(B_{3-i}\), so it is connected and spanning;
- \(F_1\cup F_2=E(H)\), since \(B_1\cap B_2=\varnothing\).

A connected Eulerian signed graph with an even number of negative edges has a flow taking values in \(\{+1,-1\}\) on every edge. For completeness, follow an Euler tour, assigning signs successively so that the two incidence contributions at each passage through a vertex cancel. The consistency condition upon returning to the start is
\[
(-1)^{\text{number of negative edges}}=1,
\]
which holds.

Consequently, for \(i=1,2\), there is an integer flow \(\psi_i\) on \(H\) taking values in \(\{+1,-1\}\) on \(F_i\) and zero elsewhere. Set
\[
z=\psi_1+2\psi_2.
\]
This is an integer flow. Because \(F_1\cup F_2=E(H)\), its possible edge values are
\[
\pm1,\quad \pm2,\quad \pm1\pm2,
\]
all nonzero and of absolute value at most \(3\). This proves the lemma. \(\square\)

## 3. Application to cellular embeddings

First suppose \(G\) is cellularly embedded in a connected closed surface \(S\).

Choose an orientation of every primal edge and, independently, an orientation of every facial disk. Let \(B\) be the matrix whose \((f,e)\)-entry is the signed number of occurrences of \(e\) in the oriented boundary of \(f\). Each edge has two face incidences, so \(B\) is an incidence matrix of a signed dual graph \(H\).

For an integer edge assignment \(\phi\),
\[
B\phi=0 \tag{3}
\]
means precisely that every facial boundary has height zero. Equation (3) then makes \(\phi\) vanish on every null-homologous closed walk, and in particular on every contractible closed walk: the cellular boundary map is \(B^{\mathsf T}\).

Thus a nowhere-zero integer \(4\)-flow in this signed dual supplies a \(4\)-local-tension in \(G\).

We verify the two hypotheses of the lemma.

### 3.1. The underlying dual is 4-edge-connected

Let \(X\) be a nonempty proper set of faces. Over \(\mathbb F_2\), the boundary of their sum is exactly the primal edge set corresponding to the dual cut:
\[
\operatorname{supp}\left(\partial_2\sum_{f\in X}f\right)
   =\delta_H(X).
\]
Since \(\partial_1\partial_2=0\), this nonempty primal edge set has even degree at every vertex. It therefore contains a cycle.

Every cycle of \(G\) has length at least \(4\), so
\[
|\delta_H(X)|\geq4.
\]
The dual is connected, so this proves the required cut condition.

### 3.2. The signed dual is flow-admissible

Choose an injective map
\[
a:V(G)\longrightarrow\mathbb Z
\]
and assign to an oriented edge \(uv\) the value
\[
t(uv)=a(v)-a(u).
\]
As \(G\) is loopless, every value is nonzero. Every facial height telescopes to zero, so
\[
Bt=0.
\]
Thus the signed dual admits a nowhere-zero integer flow, without any bound yet imposed on its values.

The lemma now produces a flow \(\phi\) satisfying
\[
B\phi=0,\qquad 1\leq|\phi(e)|\leq3.
\]
This is the desired \(4\)-local-tension.

## 4. Removing the cellularity assumption

The following argument ensures that the theorem applies to the embedding in the question, not merely to cellular embeddings.

Let \(N\) be a closed regular neighborhood of \(G\) in its original surface \(S\). Cap every boundary component of \(N\) by a disk. Componentwise, this gives a closed surface in which the same graph \(G\) is cellularly embedded.

Apply the cellular result. The resulting edge assignment \(\phi\) has height zero on every boundary component of \(N\), because each such component bounds one of the newly added facial disks.

We must check that \(\phi\) vanishes on a closed walk \(W\) that is contractible in the original surface \(S\).

Since \(N\) deformation-retracts onto \(G\), edge-height evaluation defines a homomorphism
\[
\ell_\phi:H_1(N;\mathbb Z)\longrightarrow\mathbb Z.
\]
This homomorphism vanishes on the image of \(H_1(\partial N;\mathbb Z)\).

Put \(M=\overline{S\setminus N}\). The Mayer–Vietoris sequence for \(S=N\cup M\) gives
\[
\ker\!\left(H_1(N;\mathbb Z)\longrightarrow H_1(S;\mathbb Z)\right)
 \subseteq
\operatorname{im}\!\left(H_1(\partial N;\mathbb Z)
                 \longrightarrow H_1(N;\mathbb Z)\right).
\]
Since \(W\) is contractible in \(S\), its homology class lies in this kernel. Therefore
\[
\ell_\phi([W])=0.
\]
So \(\phi\) is a local tension in the original embedding as well. Disconnected graphs are handled by the same argument with disconnected \(N\). This completes the theorem. \(\square\)

## 5. Consequence for triangle-free multigraphs

There is also a formulation matching the problem's allowance of parallel edges.

**Corollary.** Let \(G\) be a loopless embedded graph whose underlying simple graph is triangle-free. If its edge-width is at least \(4\), then \(G\) has a \(4\)-local-tension.

Delete all but one edge between each adjacent pair of vertices and apply the theorem to the resulting simple graph. Every deleted edge and its retained parallel edge form a contractible \(2\)-cycle, by the edge-width assumption. Assign them the same value when oriented consistently.

Replacing a deleted edge by its retained parallel edge preserves both height and the homotopy class of a walk. Thus the extended assignment remains a local tension.

## 6. The remaining gap

The distinction between **girth** and **edge-width** is essential here.

Large edge-width permits arbitrarily many contractible triangles. A triangular face of the primal graph creates a degree-\(3\) vertex in the dual, so the \(4\)-edge-connectivity argument fails immediately.

Moreover, this is not just a technical omission in the packing proof. For a large triangulation the dual is cubic and has too few edges to contain the two spanning bases used above. This remains true no matter how large the primal edge-width becomes.

Thus the result handles arbitrary genus and degree, but not the triangulated regime central to the conjecture. It establishes neither a universal constant \(c\) for unrestricted embedded graphs nor a counterexample of unbounded edge-width.