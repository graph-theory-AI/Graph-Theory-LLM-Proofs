```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it reduces to 5-colorable toroidal triangulations and holds when the maximum average degree is at most 5, in particular when each vertex lies in at most three triangles.",
  "would_publish": false,
  "caveats": "The argument does not handle triangle-dense critical cores or general toroidal triangulations, which contain the hard cases."
}
```

# Statement and outcome

Write \(\operatorname{ch}(G)\) for the list chromatic number and
\[
\operatorname{mad}(G)=\max_{\varnothing\ne H\subseteq G}\frac{2|E(H)|}{|V(H)|}.
\]

The implication
\[
\operatorname{ch}(G)\le 5\quad\Longrightarrow\quad \chi(G)\le 5
\]
is immediate by assigning the same list \(\{1,\dots ,5\}\) to every vertex. Thus only the converse is at issue.

I do not prove the full conjecture. I prove the following partial results.

## Partial theorem

Let \(G\) be a finite simple toroidal graph.

1. If \(\chi(G)\le5\) and \(\operatorname{mad}(G)\le5\), then \(G\) is \(5\)-choosable.

2. More generally, if \(t(H)\le |V(H)|\) for every subgraph \(H\subseteq G\), where \(t(H)\) denotes the number of distinct triangles of \(H\), then
   \[
   \chi(G)\le5\quad\Longrightarrow\quad \operatorname{ch}(G)\le5.
   \]

3. In particular, the conjecture holds for toroidal graphs in which each vertex belongs to at most three distinct triangles.

4. If each vertex belongs to at most two triangles, then \(G\) is \(4\)-degenerate and hence \(5\)-choosable, without assuming \(5\)-colorability.

5. It is enough to prove the conjecture for simple toroidal triangulations: every counterexample is a subgraph of a \(5\)-colorable, non-\(5\)-choosable toroidal triangulation.

There is also a useful structural consequence: in a list-critical subgraph of any counterexample, at least two vertices have degree at least six. Consequently, the conjecture holds if the \(5\)-core of \(G\) has at most one vertex of degree at least six.

No novelty claim is made for the standard ingredients or their elementary consequences below.

# 1. The maximum-average-degree criterion

I use the standard degree-choosability theorem:

> **Degree-choosability theorem.** A connected graph is degree-choosable unless every one of its blocks is a complete graph or an odd cycle.

A graph of the exceptional type is usually called a Gallai tree.

### Proposition 1

If \(G\) is \(5\)-colorable and \(\operatorname{mad}(G)\le5\), then \(G\) is \(5\)-choosable.

### Proof

Suppose that \(L\) is a bad list assignment with \(|L(v)|=5\) for every \(v\). Choose an induced subgraph \(H\) minimal such that \(H\) is not \(L\)-colorable.

Then \(H\) is connected and
\[
\delta(H)\ge5:
\]
indeed, if \(d_H(v)\le4\), an \(L\)-coloring of \(H-v\) extends greedily to \(v\).

On the other hand, \(\operatorname{mad}(G)\le5\) gives
\[
\frac{2|E(H)|}{|V(H)|}\le5.
\]
Hence every vertex of \(H\) has degree exactly five.

The degree-choosability theorem now says that \(H\) is \(L\)-colorable unless \(H\) is a Gallai tree. A connected \(5\)-regular Gallai tree must be \(K_6\). To see this, take a leaf block. An odd-cycle leaf block has non-cutvertices of degree two. A clique leaf block must be \(K_6\), but if it is attached through a cutvertex, that cutvertex has degree greater than five. Thus the whole graph is \(K_6\).

But \(H\subseteq G\), and a \(5\)-colorable graph cannot contain \(K_6\). This is a contradiction. ∎

In particular, every \(5\)-colorable graph of maximum degree at most five is \(5\)-choosable; this part does not use toroidality.

# 2. An edge bound in terms of triangles

### Lemma 2

If \(H\) is a simple toroidal graph with \(n\) vertices, \(m\) edges, and \(t\) distinct triangles, then
\[
m\le 2n+\frac{t}{2}.
\tag{1}
\]

### Proof

It suffices to treat a connected component. Choose a cellular embedding of \(H\) in its minimum-genus orientable surface; its genus \(g\) is either \(0\) or \(1\).

Let \(f\) be the number of faces and \(f_3\) the number of facial walks of length three. Apart from the trivial graphs on at most two vertices, a simple connected graph has no facial walk of length one or two: a length-one walk would be a loop, while a length-two walk either uses parallel edges or forces the graph to be \(K_2\). Therefore
\[
2m\ge 3f_3+4(f-f_3)=4f-f_3.
\]
Euler's formula gives
\[
n-m+f=2-2g.
\]
Substitution yields
\[
m\le 2n-4+4g+\frac{f_3}{2}.
\tag{2}
\]

Each length-three facial walk is a triangle. Except when the whole connected graph is \(C_3\), the same triangle cannot be two distinct length-three faces: otherwise both sides of all three edges are already used by those faces, and connectedness leaves no place for an additional edge. Thus \(f_3\le t\), with \(C_3\) checked directly.

If \(g=1\), (2) gives \(m\le2n+t/2\). If \(g=0\), it gives the stronger bound \(m\le2n-4+t/2\). Summing over components proves (1). ∎

### Corollary 3

Suppose that
\[
t(H)\le |V(H)|
\tag{3}
\]
for every subgraph \(H\subseteq G\). Then \(\operatorname{mad}(G)\le5\).

Indeed, Lemma 2 gives
\[
|E(H)|\le2|V(H)|+\frac{t(H)}2
          \le\frac52|V(H)|.
\]
Proposition 1 now proves that every \(5\)-colorable such \(G\) is \(5\)-choosable.

If every vertex of \(G\) belongs to at most three triangles, then for every subgraph \(H\),
\[
3t(H)
 =\sum_{v\in V(H)}\#\{\text{triangles of \(H\) containing \(v\)}\}
 \le3|V(H)|,
\]
so (3) holds.

If every vertex belongs to at most two triangles, then \(t(H)\le 2|V(H)|/3\), and Lemma 2 gives
\[
\frac{2|E(H)|}{|V(H)|}\le 4+\frac{t(H)}{|V(H)|}
 \le\frac{14}{3}<5.
\]
Thus every nonempty subgraph has a vertex of degree at most four, so \(G\) is \(4\)-degenerate and hence \(5\)-choosable.

# 3. Reduction to toroidal triangulations

### Proposition 4

If a \(5\)-colorable non-\(5\)-choosable toroidal graph exists, then a \(5\)-colorable non-\(5\)-choosable simple toroidal triangulation exists.

### Proof

Let \(G\) be a counterexample and \(L\) a bad \(5\)-list assignment. Pass to a vertex-minimal induced subgraph \(H\) that is not \(L\)-colorable. As above, \(H\) is connected and \(\delta(H)\ge5\).

The classical planar \(5\)-choosability theorem implies that \(H\) is nonplanar. Since it is toroidal, its orientable genus is exactly one, and it has a cellular torus embedding. Because \(H\) is simple and has minimum degree at least five, every facial walk has length at least three.

Fix a proper ordinary \(5\)-coloring
\[
\varphi:V(H)\to\{1,\dots ,5\}.
\]
We describe how to triangulate each face while extending \(\varphi\).

Let a face have boundary occurrence sequence
\[
v_1v_2\cdots v_\ell v_1.
\]
Inside the face add distinct vertices \(w_1,\dots ,w_\ell\), one corresponding to each boundary edge \(v_iv_{i+1}\), and add the triangles
\[
v_iv_{i+1}w_i,\qquad v_{i+1}w_iw_{i+1}
\]
with indices modulo \(\ell\). This forms a triangulated annulus whose inner boundary is the cycle \(w_1\cdots w_\ell\).

For each \(i\), permit \(w_i\) any ordinary color in
\[
P_i=\{1,\dots ,5\}\setminus
   \{\varphi(v_i),\varphi(v_{i+1})\}.
\]
Each \(P_i\) has size at least three. A cycle is colorable from lists of size three: color \(w_1,\ldots,w_{\ell-1}\) successively, and choose the color of \(w_\ell\) avoiding the colors of \(w_{\ell-1}\) and \(w_1\). Thus the annulus receives a proper \(5\)-coloring.

It remains to triangulate the disk bounded by \(w_1\cdots w_\ell\). The following elementary ear procedure preserves its boundary coloring.

- If three consecutive boundary vertices \(x,y,z\) satisfy \(\varphi(x)\ne\varphi(z)\), add the diagonal \(xz\), remove the ear \(xyz\), and continue.
- If no such vertex exists, then \(\varphi(w_i)=\varphi(w_{i+2})\) for every \(i\). The remaining boundary is therefore an even cycle alternating between two colors. Add one central vertex adjacent to the whole boundary and color it with any third color.

This gives a properly \(5\)-colored triangulated disk. Since all ring vertices are new and face-specific, no loops or parallel edges are introduced, even when the original facial walk repeats an old vertex.

Applying this construction independently in every nontriangular face yields a simple toroidal triangulation \(T\) containing \(H\), and \(\varphi\) extends to a proper \(5\)-coloring of \(T\).

Finally, give the old vertices their lists from \(L\), and give each new vertex any list of five colors. Any list-coloring of \(T\) would restrict to an \(L\)-coloring of \(H\), which is impossible. Thus \(T\) is not \(5\)-choosable. ∎

Hence the conjecture for all toroidal graphs is equivalent to its restriction to toroidal triangulations. The important limitation is that the triangulation \(T\) need not itself be list-critical.

# 4. Necessary structure of a counterexample

Let \(H\) again be a vertex-minimal subgraph uncolorable from some lists of size five. Write
\[
n=|V(H)|,\qquad m=|E(H)|.
\]

## 4.1 Density and triangular faces

We have \(\delta(H)\ge5\). Equality \(2m=5n\) would make \(H\) \(5\)-regular, and Proposition 1's argument would color it. Therefore
\[
\frac{2m}{n}>5.
\tag{4}
\]

On the other hand, toroidality gives \(2m/n\le6\). Thus
\[
5<\frac{2m}{n}\le6.
\]

By Lemma 2, (4) implies
\[
t(H)>n.
\tag{5}
\]
Thus some vertex belongs to at least four distinct triangles.

There is an embedding version of the same conclusion. Since \(H\) is nonplanar, take a cellular torus embedding and let \(f_3\) be its number of triangular faces. Euler's formula gives \(f=m-n\), and
\[
2m\ge3f_3+4(f-f_3)=4(m-n)-f_3.
\]
Consequently
\[
f_3\ge2m-4n>n.
\tag{6}
\]
So every critical counterexample lies in the strongly triangle-dense regime: a cellular embedding has more triangular faces than vertices.

## 4.2 The degree-five vertices form a Gallai forest

Let
\[
A=\{v\in V(H):d_H(v)=5\},\qquad
B=V(H)\setminus A.
\]
Thus every vertex of \(B\) has degree at least six.

Consider a component \(C\) of \(H[A]\). By minimality, \(H-C\) has an \(L\)-coloring. Delete from \(L(v)\), for \(v\in C\), the colors used on neighbors outside \(C\). The residual list satisfies
\[
|L_C(v)|\ge 5-d_{H-C}(v)=d_C(v).
\]
If \(C\) were degree-choosable, this coloring would extend to \(C\), contradicting the choice of \(H\). Hence each component of \(H[A]\) is a Gallai tree: every block is a clique or an odd cycle.

Because \(H\) is \(5\)-colorable, no clique block is larger than \(K_5\). Moreover, \(H[A]\) contains at most one \(K_5\)-block. Indeed, orientable genus is additive over blocks, and each \(K_5\)-block has genus one; two such blocks cannot occur in a toroidal subgraph.

Let \(a=|A|\), and suppose \(a>0\). If \(F=H[A]\) has \(c\) components, its block decomposition gives
\[
|E(F)|
 =2(a-c)+
 \sum_Q\bigl(|E(Q)|-2(|V(Q)|-1)\bigr),
\]
where \(Q\) ranges over the blocks. For clique blocks \(K_r\), \(2\le r\le5\), the summand is respectively
\[
-1,\ -1,\ 0,\ 2,
\]
and for an odd cycle of length \(\ell\ge5\) it is \(2-\ell<0\). Since at most one block is \(K_5\),
\[
|E(H[A])|\le2a.
\tag{7}
\]

Counting degrees in \(A\), (7) gives
\[
e(A,B)=5a-2|E(H[A])|\ge a.
\tag{8}
\]

In particular, \(B\) contains at least two vertices. For if \(B=\{b\}\), simplicity gives \(e(A,B)\le a\), so equality holds throughout (8) and \(|E(H[A])|=2a\). Equality in the block estimate forces a \(K_5\)-block, while equality \(e(A,B)=a\) says that \(b\) is adjacent to every vertex of \(A\). The vertex \(b\) together with that \(K_5\) forms a \(K_6\), contrary to \(5\)-colorability.

Thus every critical counterexample satisfies
\[
\bigl|\{v:d_H(v)\ge6\}\bigr|\ge2.
\tag{9}
\]

### Core consequence

Let \(C_5(G)\) be the \(5\)-core of \(G\), obtained by repeatedly deleting vertices of degree at most four.

Any subgraph of minimum degree at least five is contained in \(C_5(G)\). Therefore (9) proves:

> If \(G\) is a \(5\)-colorable toroidal graph and \(C_5(G)\) has at most one vertex of degree at least six, measured inside \(C_5(G)\), then \(G\) is \(5\)-choosable.

In particular, the conjecture holds for toroidal graphs having at most one vertex of degree at least six.

## 4.3 A small-order bound

Using the proved theorem commonly known as Ohba's theorem,
\[
|V(X)|\le2\chi(X)+1\quad\Longrightarrow\quad
\operatorname{ch}(X)=\chi(X),
\]
one obtains that every \(5\)-colorable graph on at most eleven vertices is \(5\)-choosable.

Indeed, for \(5\le n\le11\), refine a proper coloring into five nonempty independent sets and add all edges between different sets. This produces a complete \(5\)-partite supergraph \(X\) on the same vertex set, with \(\chi(X)=5\). Ohba's theorem gives \(\operatorname{ch}(X)=5\), and hence the original subgraph is \(5\)-choosable. Graphs on fewer than five vertices are trivially \(5\)-choosable.

Consequently, any counterexample has at least twelve vertices.

# 5. What remains unresolved

The preceding reductions leave precisely the dense regime:

- a critical subgraph has average degree strictly between \(5\) and \(6\);
- it has more triangular faces than vertices;
- its degree-five vertices induce a Gallai forest;
- it has at least two vertices of degree at least six;
- and a counterexample can be enlarged to a \(5\)-colorable toroidal triangulation.

The main gap is that the triangulation produced in Proposition 4 is not necessarily list-critical. Passing to a critical subgraph destroys the triangulation, while retaining the triangulation loses the minimum-degree and Gallai-forest conclusions. Nothing above controls the interaction of the degree-at-least-six vertices with the many triangular faces strongly enough to complete the coloring argument.

Thus this is a rigorous partial result and structural reduction, not a proof or counterexample to the full conjecture.