```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for torus embeddings with at most 13 contractible triangles, while any counterexample contains a choice-critical subgraph on at least 12 vertices with at least 14 contractible facial triangles.",
  "would_publish": false,
  "caveats": "The dense triangulated regime, notably 6-regular toroidal triangulations, remains untreated; criticality is interpreted globally."
}
```

# Mathematical writeup

## 1. Definitions and partial result

All graphs are finite and simple. A graph is **critical for 5-choosability** if it is not 5-choosable but every proper subgraph is 5-choosable. This is global choice-criticality, not merely criticality for one particular list assignment. Under this definition, \(K_7\) is not choice-critical, since its proper subgraph \(K_6\) is already not 5-choosable.

A graph is **6-critical** if it is not 5-colorable but every proper subgraph is 5-colorable.

The main partial result obtained here is the following.

### Theorem 1
Let \(G\) be a graph with a fixed embedding in the torus. If the embedding contains at most \(13\) distinct contractible triangles, then
\[
G\text{ is 5-choosable}\quad\Longleftrightarrow\quad G\text{ is 5-colorable}.
\]
Consequently, in this class,
\[
G\text{ is critical for 5-choosability}
\quad\Longleftrightarrow\quad
G\text{ is 6-critical}.
\]

More generally, every 5-colorable non-5-choosable toroidal graph contains a choice-critical subgraph \(H\) satisfying:

1. \(|V(H)|\ge 12\);
2. \(\delta(H)\ge 5\), but \(H\) is not 5-regular;
3. the inherited torus embedding of \(H\) is cellular;
4. \(H\) has at least \(14\) distinct contractible facial triangles;
5. the subgraph induced by its degree-5 vertices is a Gallai forest whose clique blocks have order at most \(5\).

Thus any counterexample to the full conjecture lies in a rather dense, triangle-rich regime.

## 2. Established tools used

The proof uses three standard, proved results.

1. **Degree-choosability theorem.** A connected graph is colorable from every assignment satisfying
   \[
   |L(v)|\ge d(v)
   \]
   unless every block is a complete graph or an odd cycle. Such exceptional graphs are called Gallai trees.

2. **Planar 5-choosability.** Every planar graph is 5-choosable.

3. **Ohba's theorem.** If
   \[
   |V(G)|\le 2\chi(G)+1,
   \]
   then \(\operatorname{ch}(G)=\chi(G)\).

No unproved conjecture is used.

## 3. A density lemma

We first record a useful consequence of the degree-choosability theorem.

### Lemma 2
Let \(k\ge 3\). If
\[
\operatorname{mad}(G):=
\max_{\varnothing\ne J\subseteq G}\frac{2|E(J)|}{|V(J)|}\le k
\]
and \(G\) contains no \(K_{k+1}\), then \(G\) is \(k\)-choosable.

#### Proof
Suppose some \(k\)-list assignment \(L\) is not colorable, and let \(H\subseteq G\) be inclusion-minimal with this property. Then \(H\) is connected and
\[
\delta(H)\ge k,
\]
since a vertex of degree at most \(k-1\) could be colored after coloring \(H-v\).

On the other hand, \(\operatorname{mad}(G)\le k\), so the average degree of \(H\) is at most \(k\). Hence \(H\) is \(k\)-regular.

The lists now satisfy \(|L(v)|=d_H(v)\). By the degree-choosability theorem, \(H\) must be a Gallai tree. A finite connected \(k\)-regular Gallai tree with \(k\ge3\) is necessarily \(K_{k+1}\): if it has more than one block, take a leaf block. A non-cutvertex in an odd-cycle leaf block has degree \(2<k\); a non-cutvertex in a clique leaf block forces that block to be \(K_{k+1}\), whose cutvertex would then have degree greater than \(k\). Thus there is only one block, and it is \(K_{k+1}\).

This contradicts the hypothesis that \(G\) is \(K_{k+1}\)-free. ∎

For \(k=5\), this gives:

### Corollary 3
Every 5-colorable graph \(G\) with \(\operatorname{mad}(G)\le5\) is 5-choosable.

Indeed, a 5-colorable graph contains no \(K_6\).

This already proves the conjectured equivalence for the hereditary class \(\operatorname{mad}(G)\le5\).

## 4. Small-order exclusion

### Lemma 4
Every 5-colorable graph on at most \(11\) vertices is 5-choosable.

#### Proof
The claim is immediate when \(|V(G)|<5\). Otherwise, refine a proper coloring of \(G\) into exactly five nonempty independent sets, and add every edge joining different sets. This produces a complete 5-partite supergraph \(K\) on the same vertex set. It has
\[
\chi(K)=5,\qquad |V(K)|\le11=2\chi(K)+1.
\]
By Ohba's theorem, \(K\) is 5-choosable. Since choosability is preserved under deleting edges, \(G\) is 5-choosable. ∎

Thus a 5-colorable non-5-choosable graph has at least \(12\) vertices.

## 5. Minimal toroidal obstructions

Let \(G\) be a 5-colorable, non-5-choosable toroidal graph. Choose an inclusion-minimal non-5-choosable subgraph \(H\). Write
\[
n=|V(H)|,\qquad m=|E(H)|.
\]

Then:

- \(H\) is connected;
- \(H\) is choice-critical;
- \(H\) remains 5-colorable;
- \(\delta(H)\ge5\);
- by Lemma 4, \(n\ge12\).

Moreover, \(H\) is not 5-regular. If it were, then \(\operatorname{mad}(H)\le5\), and since \(H\) is 5-colorable it contains no \(K_6\). Lemma 2 would imply that \(H\) is 5-choosable, a contradiction.

Define the positive degree excess
\[
E:=\sum_{v\in V(H)}(d(v)-5)=2m-5n>0.
\]
Its parity is the parity of \(n\). Hence
\[
E\ge
\begin{cases}
2,&n\text{ even},\\
1,&n\text{ odd}.
\end{cases}
\]

## 6. Cellularity of the inherited embedding

The graph \(H\) is nonplanar, since every planar graph is 5-choosable. Therefore its orientable genus is exactly one.

For completeness, the inherited torus embedding is cellular. Let \(N\) be a connected regular neighborhood of \(H\). Capping the boundary components of \(N\) gives a closed orientable surface containing \(H\). Since \(H\) is nonplanar but toroidal, \(N\) has genus one.

Let \(b\) be the number of boundary components of \(N\), and let \(F_1,\dots,F_r\) be the closures of the complementary components, with \(b_i\) boundary components and genus \(g_i\). Since
\[
\chi(N)=-b
\]
and Euler characteristic is additive along boundary circles,
\[
\sum_i \chi(F_i)=b.
\]
But
\[
\chi(F_i)=2-2g_i-b_i\le b_i,
\]
with equality only when \(F_i\) is a disk. Since \(\sum_i b_i=b\), equality must hold for every \(i\). Thus every complementary component is a disk.

Hence the embedding of \(H\) is cellular.

## 7. Counting facial triangles

Let \(f\) be the number of faces and \(f_3\) the number of faces whose boundary walk has length three.

Because \(H\) is simple and has minimum degree at least five, no face has boundary length one or two. A length-one face would require a loop. A length-two facial walk would require parallel edges or a single edge whose two endpoints both have degree one.

Euler's formula on the torus gives
\[
f=m-n.
\]

Let
\[
R:=\sum_{\substack{F\text{ a face}\\ |F|\ge4}}(|F|-4)\ge0.
\]
Counting edge-sides gives
\[
2m=3f_3+4(f-f_3)+R,
\]
and hence
\[
f_3=4f+R-2m
    =2m-4n+R
    =n+E+R.
\]
Therefore
\[
f_3\ge n+E.
\]

Every length-three facial walk is a genuine triangle. Moreover, two different triangular faces cannot have the same boundary triangle: if both sides of a triangle were faces, then at each of its vertices the two triangle edges would be consecutive in both cyclic directions, forcing degree two. Thus these \(f_3\) faces give \(f_3\) distinct triangles.

Each facial triangle is contractible. Consequently,
\[
\#\{\text{contractible triangles of }H\}\ge n+E.
\]

Since \(n\ge12\), this is at least \(14\):

- if \(n=12\), then \(E\ge2\);
- if \(n\ge13\), then \(n+E\ge14\).

Thus:

### Proposition 5
Every 5-colorable non-5-choosable toroidal graph contains at least \(14\) distinct contractible triangles.

More precisely, its minimal non-5-choosable subgraph has at least \(14\) contractible facial triangles.

## 8. Proof of Theorem 1

Suppose \(G\) has at most \(13\) contractible triangles and is 5-colorable. If it were not 5-choosable, choose a minimal non-5-choosable subgraph \(H\). Proposition 5 gives at least \(14\) distinct contractible triangles in \(H\), hence in \(G\), a contradiction.

Thus every such 5-colorable \(G\) is 5-choosable. The reverse implication is immediate by assigning the same five colors to every vertex.

The class of torus-embedded graphs with at most \(13\) contractible triangles is hereditary. Therefore:

- If \(G\) is choice-critical, it cannot be 5-colorable, while every proper subgraph is 5-colorable. Hence \(G\) is 6-critical.
- If \(G\) is 6-critical, then it is not 5-choosable under the constant five-color list assignment. Every proper subgraph is 5-colorable and still has at most \(13\) contractible triangles, so every proper subgraph is 5-choosable. Hence \(G\) is choice-critical.

This proves the asserted special case.

In particular, the conclusion holds if \(G\) has at most \(13\) triangles in total.

## 9. Structure of the degree-5 vertices

Let \(H\) be a minimal 5-colorable non-5-choosable toroidal graph, and let
\[
S=\{v\in V(H):d(v)=5\}.
\]

### Proposition 6
Every block of \(H[S]\) is a complete graph or an odd cycle. Its complete blocks have order at most five.

#### Proof
Choose a bad list assignment \(L\) with \(|L(v)|=5\) for every vertex. Since \(H\) is choice-critical, every proper subgraph is colorable from the restricted lists.

Suppose a block \(B\) of \(H[S]\) is neither complete nor an odd cycle. Color \(H-V(B)\). For \(x\in V(B)\), delete from \(L(x)\) the colors used on neighbors outside \(B\). Since \(d_H(x)=5\),
\[
|L_B(x)|\ge 5-(5-d_B(x))=d_B(x).
\]
By the degree-choosability theorem, \(B\) is colorable from these residual lists. This extends the coloring of \(H-V(B)\), contradicting the choice of \(L\).

Thus \(H[S]\) is a Gallai forest. A clique block has order at most six from the degree bound, and \(K_6\) is excluded because \(H\) is 5-colorable. ∎

There is also an exact curvature identity. Put
\[
Q:=\sum_F(|F|-3)=3n-m.
\]
Then
\[
\sum_v(6-d(v))=6n-2m=2Q,
\]
so
\[
|S|-\sum_{d(v)\ge7}(d(v)-6)=2Q.
\]

Consequently, every minimal counterexample falls into one of two branches:

1. \(S=\varnothing\), in which case every vertex has degree six and every face is triangular; thus \(H\) is a 6-regular toroidal triangulation.
2. \(S\ne\varnothing\), in which case the degree-5 vertices form the constrained Gallai forest above and balance all higher-degree curvature and nontriangular faces.

The first branch appears to be a central unresolved case.

## 10. A further easy special case

### Proposition 7
Every triangle-free toroidal graph is 4-choosable.

#### Proof
Every subgraph of a triangle-free toroidal graph satisfies the Euler bound
\[
|E(J)|\le 2|V(J)|,
\]
so its maximum average degree is at most four. It contains no \(K_5\). Lemma 2 with \(k=4\) therefore gives 4-choosability. ∎

## 11. Remaining gap

The argument does not control toroidal graphs with many contractible triangles. In particular, it leaves untouched 6-regular toroidal triangulations: these have no degree-5 vertices, and the Gallai-forest reduction gives no local reducible configuration.

Also, the facial triangles produced above are contractible. Their abundance does not imply the cyclic system of nearby noncontractible triangles required by the source paper's theorem; triangular-lattice quotients can have many facial triangles while having large noncontractible edge-width.

For a finite computational attack, a candidate on \(n\) vertices only requires colors from a universe of size at most \(5n\). Non-5-choosability can therefore be tested by the exact finite quantified condition
\[
\exists\bigl(L(v)\in {[5n]\choose5}\bigr)_{v\in V}
\ \forall(c_v\in[5n])_{v\in V}:
\left[
\exists v,\ c_v\notin L(v)
\right]
\lor
\left[
\exists uv\in E,\ c_u=c_v
\right].
\]
The structural restrictions above substantially reduce the candidates, but no such enumeration was performed here.