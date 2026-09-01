```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted question remains open, but there is a 2^{O_Sigma(sqrt(n))} exact algorithm and an FPT algorithm parameterized by the number of degree-at-least-five vertices in the 4-core, giving polynomial time when that core has O(log n) triangles.",
  "would_publish": false,
  "caveats": "This gives neither an unrestricted polynomial algorithm nor an NP-hardness proof; novelty of the partial bounds is not claimed."
}
```

# Mathematical writeup

## 1. Interpretation and results obtained

I assume that graphs are finite and simple and that a crossing-free embedding in the fixed surface \(\Sigma\) is supplied. Loops can immediately be rejected and parallel edges suppressed. Let \(\gamma=\gamma(\Sigma)\) denote the Euler genus, so that
\[
\chi(\Sigma)=2-\gamma.
\]

I do not resolve the unrestricted polynomial-time question. I establish the following partial results.

### Theorem A: subexponential algorithm

For every fixed surface \(\Sigma\), 4-colorability of an \(n\)-vertex graph embedded in \(\Sigma\) can be decided in
\[
2^{O_\Sigma(\sqrt n)}n^{O(1)}
\]
time.

### Theorem B: an embedding-independent FPT algorithm

Let \(C_4(G)\) be the 4-core of \(G\), obtained by repeatedly deleting vertices of degree at most three, and put
\[
p(G)=\bigl|\{v\in V(C_4(G)):\deg_{C_4(G)}(v)\ge 5\}\bigr|.
\]
Then 4-colorability can be decided in
\[
O\!\left(4^{p(G)}(n+m)\right)
\]
time.

### Corollary C: few triangles

If the 4-core \(H=C_4(G)\) is embedded in a surface of Euler genus \(\gamma\) and contains \(t\) triangles, then
\[
p(G)\le 2t+4\gamma-8.
\]
Consequently, for every fixed surface:

* graphs whose 4-core has \(O(\log n)\) triangles have polynomial-time decidable 4-colorability;
* graphs whose 4-core has a bounded number of triangles have linear-time decidable 4-colorability, with a surface- and triangle-dependent constant;
* in particular, 4-colorability of triangle-free graphs on any fixed surface is decidable in linear time by this elementary method.

For Euler genus at most two one obtains more:

* every triangle-free projective-planar graph is 3-degenerate and hence 4-colorable;
* every triangle-free toroidal or Klein-bottle graph is 4-colorable.

The unrestricted problem remains precisely outside these sparse-triangle regimes.

---

## 2. Proof of Theorem A

A standard constructive surface-separator theorem says that an \(n\)-vertex graph of Euler genus \(\gamma\) has a balanced vertex separator of size
\[
O\!\left(\sqrt{(\gamma+1)n}\right),
\]
and such a separator can be found in polynomial time when the embedding is supplied. Each component after deletion has at most, say, \(2n/3\) vertices.

Applying this recursively gives a tree decomposition. If \(w(n)\) denotes its maximum bag size, then
\[
w(n)\le c\sqrt{(\gamma+1)n}+w(2n/3).
\]
Thus
\[
w(n)\le c\sqrt{(\gamma+1)n}
 \sum_{i\ge 0}(2/3)^{i/2}
 =O\!\left(\sqrt{(\gamma+1)n}\right).
\]

On a tree decomposition of width \(w\), ordinary 4-colorability is decided by storing, for each bag, the proper maps from the bag to \(\{1,2,3,4\}\) that extend to the processed part. The table has at most \(4^{w+1}\) entries per bag. Therefore the running time is
\[
4^{O(\sqrt{(\gamma+1)n})}n^{O(1)}
 =2^{O_\Sigma(\sqrt n)}n^{O(1)}
\]
for fixed \(\Sigma\).

This is an exact algorithm, but the \(\sqrt n\) in the exponent does not yield polynomial time.

---

## 3. Proof of Theorem B

### 3.1 Reduction to the 4-core

If \(v\) has degree at most three, then every 4-coloring of \(G-v\) extends to \(v\), because at most three colors are forbidden. Hence
\[
G\text{ is 4-colorable}
\quad\Longleftrightarrow\quad
C_4(G)\text{ is 4-colorable}.
\]

Let \(H=C_4(G)\). Every vertex of \(H\) has degree at least four. Define
\[
X=\{v\in V(H):\deg_H(v)\ge5\},\qquad J=H-X.
\]
Every vertex of \(J\) has degree exactly four in \(H\).

### 3.2 Branching on \(X\)

Enumerate all maps
\[
\varphi:X\longrightarrow\{1,2,3,4\}.
\]
Discard \(\varphi\) if it is not proper on \(H[X]\). For \(v\in V(J)\), define
\[
L_\varphi(v)
 =
 \{1,2,3,4\}\setminus
 \{\varphi(x):x\in N_H(v)\cap X\}.
\]

Then \(\varphi\) extends to a 4-coloring of \(H\) if and only if \(J\) is colorable from the lists \(L_\varphi\).

Since \(\deg_H(v)=4\),
\[
\deg_J(v)=4-|N_H(v)\cap X|.
\]
The number of distinct colors forbidden by \(N_H(v)\cap X\) is at most the number of those neighbors. Therefore
\[
|L_\varphi(v)|
 \ge 4-|N_H(v)\cap X|
 =\deg_J(v).
\tag{1}
\]

Thus every branch produces a degree-list-coloring instance.

### 3.3 Solving the resulting degree-list instances

I use the standard degree-choosability theorem:

> **Degree-list lemma.**  
> Let \(K\) be a connected graph and suppose that \(|L(v)|\ge\deg_K(v)\) for every \(v\). If \(K\) is not \(L\)-colorable, then every block of \(K\) is either a complete graph or an odd cycle.

Graphs whose blocks are all complete graphs or odd cycles are often called Gallai trees. This is the list version of the Brooks-type degree-coloring theorem.

For each connected component \(K\) of \(J\):

1. If \(K\) is not a Gallai tree, the degree-list lemma and (1) guarantee that \(K\) is \(L_\varphi\)-colorable.
2. If \(K\) is a Gallai tree, its list-colorability can be tested directly in linear time:
   * every complete block has at most five vertices because \(\Delta(J)\le4\);
   * every odd-cycle block has treewidth two;
   * gluing such blocks at cutvertices produces a tree decomposition of width at most four.

A standard list-coloring dynamic program over this width-four decomposition decides the component in constant-state linear time. Isolated vertices with empty lists are rejected separately.

Hence each branch \(\varphi\) can be tested in \(O(n+m)\) time. There are at most \(4^{|X|}=4^{p(G)}\) branches, proving
\[
T(G)=O\!\left(4^{p(G)}(n+m)\right).
\]

If a branch succeeds, the deleted vertices outside the 4-core can be reinserted in reverse deletion order and colored greedily.

---

## 4. Bounding the parameter by the number of triangles

Let \(H=C_4(G)\), let \(n_H=|V(H)|\), and suppose \(H\) is embedded in a surface of Euler genus \(\gamma\).

More generally, let \(F\subseteq E(H)\) meet every triangle of \(H\), and write \(\tau=|F|\). Then \(H-F\) is triangle-free. The standard Euler bound for a simple triangle-free graph \(Q\) embedded in Euler genus \(\gamma\) is
\[
|E(Q)|\le 2|V(Q)|-4+2\gamma.
\tag{2}
\]
It follows that
\[
|E(H)|
 \le 2n_H-4+2\gamma+\tau.
\]
Because \(H\) has minimum degree at least four,
\[
\begin{aligned}
\sum_{v\in V(H)}(\deg_H(v)-4)
 &=2|E(H)|-4n_H\\
 &\le 2\tau+4\gamma-8.
\end{aligned}
\tag{3}
\]
Every vertex of \(X\) contributes at least one to the left side, while no vertex contributes negatively. Therefore
\[
p(G)=|X|\le 2\tau+4\gamma-8.
\tag{4}
\]

If \(H\) has \(t\) triangles, selecting one edge from each triangle gives a triangle edge-transversal of size at most \(t\). Hence
\[
p(G)\le 2t+4\gamma-8.
\]

Combining this with Theorem B gives
\[
T(G)
 \le
4^{\max\{0,\,2t+4\gamma-8\}}\,O(n+m).
\]

For fixed \(\gamma\), this is polynomial whenever \(t=O(\log n)\).

### Triangle-free consequences

Taking \(t=0\) gives
\[
p(G)\le 4\gamma-8.
\]

Thus the number of degree-at-least-five vertices in the 4-core of a triangle-free graph is bounded solely in terms of the surface.

For \(\gamma=1\), inequality (3) rules out any nonempty 4-core, so every triangle-free projective-planar graph is 3-degenerate.

For \(\gamma=2\), the 4-core, if nonempty, is 4-regular. By Brooks' theorem each connected component is 4-colorable unless it is \(K_5\); triangle-freeness excludes \(K_5\). Thus every triangle-free graph on the torus or Klein bottle is 4-colorable.

For larger fixed Euler genus, triangle-free 5-chromatic examples can exist, but Theorem B tests them using only a surface-dependent constant number of branches.

---

## 5. A small but genuine toroidal bottleneck

Consider the following planar relation problem.

> **\(\textsc{Planar-Separate}_4\).**  
> Input: a plane graph \(P\) and two nonadjacent vertices \(a,b\).  
> Question: does \(P\) have a 4-coloring in which \(a\) and \(b\) receive different colors?

Set
\[
G=P+ab.
\]
Then
\[
G\text{ is 4-colorable}
\quad\Longleftrightarrow\quad
(P,a,b)\in\textsc{Planar-Separate}_4.
\tag{5}
\]

Moreover, \(G\) always embeds in the torus. Starting from the spherical embedding of \(P\), attach a handle between small face-neighborhoods incident with \(a\) and \(b\), and draw the new edge through the handle. This construction also supplies the embedding in polynomial time.

Consequently:

> A polynomial-time algorithm for toroidal 4-colorability would, already on graphs made planar by deleting one edge, decide whether two vertices of a planar graph can be separated by a 4-coloring.

This subproblem is nontrivial. For example, in \(K_5-ab\), the other three vertices form a triangle and are adjacent to both \(a\) and \(b\), so every 4-coloring gives \(a\) and \(b\) the same fourth color. On the other hand, if \(a\) and \(b\) are cofacial in a plane embedding, then \(ab\) can be added planarly, and the Four Color Theorem gives a separating coloring.

I do not prove that \(\textsc{Planar-Separate}_4\) is hard or polynomial-time solvable; (5) is a bottleneck reduction, not a hardness result.

---

## 6. Exact reformulation for triangulations

There is also a useful algebraic formulation for cellular triangulations.

Let \(T\) be a cellular triangulation of \(\Sigma\), let \(T^*\) be its cubic dual, and identify the four vertex colors with
\[
A=\mathbb F_2^2.
\]
Given a proper vertex coloring \(c:V(T)\to A\), label each edge \(uv\) by
\[
\ell(uv)=c(u)+c(v)\in A\setminus\{0\}.
\]
Around every triangular face, the three labels are precisely the three nonzero elements of \(A\). Hence \(\ell\) is a proper 3-edge-coloring of the cubic dual \(T^*\).

Conversely, a proper 3-edge-coloring of \(T^*\) labels the three sides of every primal triangle by the three nonzero elements of \(A\), whose sum is zero. Thus \(\ell\) is an \(A\)-valued cellular 1-cocycle on \(T\). It comes from a vertex coloring exactly when it is a coboundary, equivalently when
\[
[\ell]=0\in H^1(\Sigma;A).
\]

Therefore
\[
T\text{ is 4-colorable}
\quad\Longleftrightarrow\quad
T^*\text{ has a proper 3-edge-coloring of zero }A\text{-cohomology class}.
\tag{6}
\]

For fixed \(\Sigma\), the group \(H^1(\Sigma;A)\) has only \(4^\gamma\) elements. Nevertheless, this does not itself yield a polynomial algorithm: finding a proper 3-edge-coloring in a prescribed cohomology class remains a global constrained nowhere-zero-flow problem.

---

## 7. Remaining gap

The FPT argument becomes ineffective on triangle-rich 4-cores. A surface triangulation can have \(\Theta(n)\) triangles and \(\Theta(n)\) vertices of degree at least five, even though large planar triangulations are automatically 4-colorable. Thus the parameter \(p(G)\) can be linear for exactly the locally planar, globally constrained instances on which the Four Color Theorem would need to be used algorithmically.

Likewise:

* the separator algorithm remains exponential in \(\sqrt n\);
* the one-added-edge reduction does not classify the planar forced-equality problem;
* the constant number of homology classes in (6) does not make prescribed-class cubic edge-coloring tractable.

Hence no case covering unrestricted graphs on any fixed nonspherical surface has been proved here, and no NP-hardness construction has been obtained.