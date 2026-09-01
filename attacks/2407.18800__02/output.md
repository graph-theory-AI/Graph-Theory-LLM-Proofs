```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not settled, but any counterexample has an induced critical core of average degree greater than 21/4 with linearly many induced diamonds, proving the conjecture for induced-diamond-free and sufficiently sparse graphs.",
  "would_publish": false,
  "caveats": "Dense cores, notably 6-regular toroidal triangulations, remain; novelty of the partial lemmas was not literature-checked."
}
```

# 1. Statement and conventions

Graphs are finite and simple, and “drawn on the torus” means embedded without crossings. The conjecture is:

> **Conjecture.** Every graph with a torus embedding of edge-width at least four is 5-choosable.

I do not prove the conjecture. I prove a critical-core reduction and two concrete special cases.

Write \(K_4^-=K_4-e\), the diamond graph.

# 2. Main partial result

## Critical-core theorem

Let \(G\) be embedded in the torus with edge-width at least four. If \(G\) is not 5-choosable, then it contains an induced subgraph \(H\) with the following properties.

1. \(H\) is 2-connected, nonplanar, and its inherited torus embedding is cellular.
2. \(\delta(H)\ge 5\).
3. Every triangle of \(H\) bounds a face of \(H\).
4. \(H\) is \(K_4\)-free.
5. If
   \[
   S=\{v\in V(H):d_H(v)=5\},
   \]
   then every block of \(H[S]\) is \(K_2\), \(K_3\), or an odd cycle.
6. Put
   \[
   n=|V(H)|,\qquad m=|E(H)|,
   \]
   and let \(c\) be the number of components of \(H[S]\), with \(c=0\) when \(S=\varnothing\). Then
   \[
   2m\ge \frac{21}{4}n+\frac38c.
   \]
   In particular,
   \[
   \frac{2m}{n}>\frac{21}{4}.
   \]
7. If \(t\) is the number of triangular faces and \(x\) is the number of edges incident with triangular faces on both sides, then
   \[
   t\ge \frac54n+\frac38c
   \]
   and
   \[
   x\ge \frac98n+\frac{15}{16}c.
   \]
   Every one of these \(x\) edges is the central edge of an induced \(K_4^-\) in \(H\), and hence in \(G\).

Consequently:

> **Corollary 1.** If \(G\) has maximum average degree at most \(21/4\), then \(G\) is 5-choosable.

> **Corollary 2.** If \(G\) is induced-\(K_4^-\)-free, then \(G\) is 5-choosable.

In particular, Corollary 2 applies if no edge of \(G\) belongs to two triangles. It therefore includes the triangle-free case. Also, Corollary 1 includes all such graphs with maximum degree at most five.

# 3. Planar extension lemmas

I use the standard strengthened form of planar 5-choosability:

> **Outer-face list theorem.** Let \(P\) be a plane graph. Let \(Q\) be a path of length at most one on the outer face. Give the vertices of \(Q\) singleton lists, forming a proper coloring when \(Q\) is an edge. Give every other outer-face vertex a list of size at least three and every interior vertex a list of size at least five. Then \(P\) is list-colorable.

Two consequences will be used.

### Lemma 3.1: one prescribed planar vertex

Let \(P\) be planar, with lists of size at least five. For any vertex \(v\) and any prescribed color \(\alpha\in L(v)\), there is an \(L\)-coloring of \(P\) in which \(v\) receives \(\alpha\).

Indeed, choose a plane embedding with a face incident with \(v\) as the outer face and apply the outer-face theorem with \(Q=v\).

### Lemma 3.2: a prescribed facial triangle

Let \(P\) be drawn in a disk with boundary triangle \(abc\). If all internal vertices have lists of size at least five, then every proper prescribed coloring of \(a,b,c\) from their lists extends to an \(L\)-coloring of \(P\).

To see this, delete \(c\), remove the prescribed color of \(c\) from the lists of its remaining neighbors, and apply the outer-face theorem with the precolored edge \(ab\). All newly exposed outer-face vertices retain at least four colors.

# 4. Construction of the critical core

Assume \(G\) is not 5-choosable. Choose \(X\subseteq V(G)\) minimally such that
\[
H=G[X]
\]
is not 5-choosable. Choose a bad list assignment \(L\) with \(|L(v)|=5\) for all \(v\in V(H)\).

Every proper induced subgraph of \(H\) is 5-choosable.

## Minimum degree

If \(d_H(v)\le4\), color \(H-v\) and then color \(v\), since at most four colors are forbidden. Hence
\[
\delta(H)\ge5.
\]

The graph \(H\) is connected and nonplanar, since planar graphs are 5-choosable.

## Reduction to one nonplanar block

The orientable genus is additive over the blocks of a graph. Since \(H\) is nonplanar and toroidal, exactly one of its blocks can be nonplanar.

Suppose \(H\) had more than one block, and let \(B\) be its unique nonplanar block. By minimality, the proper induced subgraph \(H[V(B)]\) is 5-choosable, so color it from \(L\). Every branch of the block-cutvertex tree outside \(B\), together with its attachment vertex in \(B\), is planar. By Lemma 3.1, its coloring extends for the already prescribed color of the attachment vertex. Coloring all branches gives an \(L\)-coloring of \(H\), a contradiction.

Thus \(H\) is 2-connected.

Since \(H\) has orientable genus exactly one, its inherited torus embedding is a minimum-genus embedding and hence is cellular. Equivalently, a non-disc face would allow compression along a curve disjoint from \(H\), producing a plane embedding.

# 5. Every triangle is facial

Let \(T\) be a triangle of \(H\). Edge-width at least four implies that \(T\) is contractible, so it bounds a disk \(D\).

Suppose the interior of \(D\) contains a vertex of \(H\). Not all of \(H\) lies in \(D\), since otherwise \(H\) would be planar. Color the proper induced subgraph consisting of \(T\) and everything outside \(D\). The three vertices of \(T\) receive distinct colors. Lemma 3.2 then extends this coloring through the planar subgraph inside \(D\), contradicting the choice of \(L\).

Therefore the disk bounded by every triangle contains no part of \(H\), and hence every triangle is facial.

## Exclusion of \(K_4\)

Suppose \(abcd\) spans a \(K_4\). Each of its four triangles is facial. At vertex \(a\), each pair among the three incident edges \(ab,ac,ad\) must be consecutive in the cyclic order around \(a\), because each such pair bounds one of the triangular faces. Three specified incident edges can be pairwise consecutive only if there is no fourth incident edge. Thus \(d_H(a)=3\), contradicting \(\delta(H)\ge5\).

Hence
\[
K_4\not\subseteq H.
\]

# 6. The degree-five subgraph

Let
\[
S=\{v:d_H(v)=5\},\qquad R=V(H)\setminus S,
\]
and put
\[
l=|S|,\qquad h=|R|.
\]

I use the standard degree-choosability characterization: a 2-connected graph which is neither a complete graph nor an odd cycle is colorable from every list assignment satisfying \(|L(v)|\ge d(v)\).

Consider a block \(B\) of \(H[S]\). Color \(H-V(B)\), which is possible by minimality. For \(v\in V(B)\), at most
\[
d_H(v)-d_B(v)=5-d_B(v)
\]
colors are lost to already colored outside neighbors. Thus \(v\) retains at least \(d_B(v)\) colors. If \(B\) were neither complete nor an odd cycle, degree-choosability would color \(B\), contradicting the badness of \(L\).

Therefore every block of \(H[S]\) is complete or an odd cycle. Since \(H\) is \(K_4\)-free, the complete blocks are only \(K_2\) and \(K_3\).

Let \(c\) be the number of components of \(H[S]\). For each component \(C\), the block identity
\[
\sum_{B\text{ block of }C}(|V(B)|-1)=|V(C)|-1
\]
holds. Every permitted block satisfies
\[
|E(B)|\le\frac32(|V(B)|-1).
\]
Indeed, equality is possible for \(K_3\), while it is immediate for \(K_2\) and odd cycles. Summing over all components gives
\[
e(H[S])\le\frac32(l-c).
\]

Let \(e(S,R)\) be the number of edges between \(S\) and \(R\). Since every vertex of \(S\) has degree five,
\[
5l=2e(H[S])+e(S,R),
\]
and consequently
\[
e(S,R)\ge 5l-3(l-c)=2l+3c. \tag{1}
\]

Write
\[
\sigma=\sum_{v\in R}(d_H(v)-6)\ge0.
\]
Then
\[
2m=5l+6h+\sigma. \tag{2}
\]
Since the total degree in \(R\) is at least \(e(S,R)\), (1) implies
\[
\sigma\ge \max\{0,\,2l+3c-6h\}. \tag{3}
\]

If \(2l+3c\le6h\), then
\[
2m-\frac{21}{4}n
 =\frac{3h-l}{4}
 \ge\frac38c.
\]
If \(2l+3c\ge6h\), then by (2)–(3),
\[
2m\ge7l+3c,
\]
and hence
\[
2m-\frac{21}{4}n
 \ge \frac{7(l-3h)+12c}{4}
 \ge\frac38c.
\]
Thus in all cases
\[
\boxed{2m\ge\frac{21}{4}n+\frac38c.} \tag{4}
\]

If \(l>0\), then \(c\ge1\), so the average degree is strictly greater than \(21/4\). If \(l=0\), every vertex has degree at least six; the toroidal Euler bound below forces every degree to equal six, so the average degree is six. Thus it is again strictly greater than \(21/4\).

# 7. Face and diamond counts

Let \(f\) be the number of faces and \(t\) the number of triangular faces. Since the embedding is cellular on the torus,
\[
f=m-n.
\]
All facial walks have length at least three, and every nontriangular face has length at least four. Therefore
\[
2m\ge3t+4(f-t)=4f-t,
\]
so
\[
t\ge4f-2m=2m-4n.
\]
Using (4),
\[
\boxed{t\ge\frac54n+\frac38c.} \tag{5}
\]

Let \(x,y,z\) denote respectively the number of edges incident with two, one, or zero triangular face-sides. Then
\[
x+y+z=m,\qquad 2x+y=3t.
\]
Consequently,
\[
x-z=3t-m,
\]
and hence
\[
x\ge3t-m.
\]
Using \(t\ge2m-4n\),
\[
x\ge5m-12n=\frac52(2m)-12n.
\]
Applying (4) gives
\[
\boxed{x\ge\frac98n+\frac{15}{16}c.} \tag{6}
\]

If an edge \(uv\) is incident with triangular faces \(uvp\) and \(uvq\), then \(p\ne q\). Moreover, \(pq\notin E(H)\), since otherwise \(u,v,p,q\) span a \(K_4\). Thus these four vertices induce a \(K_4^-\), with central edge \(uv\). Because \(H\) was chosen as an induced subgraph of \(G\), this \(K_4^-\) is also induced in \(G\).

This proves the critical-core theorem.

For completeness, Euler's inequality also gives
\[
m\le3n.
\]
Combining this with (1)–(2) yields
\[
l+3c\le6h,
\]
and therefore
\[
h\ge\frac{n+3c}{7}.
\]
Thus a critical core has a linear number of vertices of degree at least six.

# 8. Consequences

## Maximum-average-degree case

If \(G\) were not 5-choosable, its critical core \(H\) would have average degree greater than \(21/4\). Hence:

\[
\operatorname{mad}(G)\le\frac{21}{4}
\quad\Longrightarrow\quad
G\text{ is 5-choosable}.
\]

## Induced-diamond-free case

Equation (6) forces at least one induced \(K_4^-\) in any critical core. Therefore:

\[
G\text{ induced-}K_4^-\text{-free}
\quad\Longrightarrow\quad
G\text{ is 5-choosable}.
\]

In particular, this applies whenever no edge lies in two triangles.

# 9. Remaining gap

The argument is compatible with dense toroidal triangulations. If the critical core has no degree-five vertices, then Euler's formula forces:

- every vertex to have degree six;
- every face to be triangular;
- every edge to be incident with two triangular faces.

Thus the unresolved extremal case already contains 6-regular toroidal triangulations with every triangle facial.

For example, for \(p,q\ge4\), let
\[
V(T_{p,q})=\mathbb Z_p\times\mathbb Z_q
\]
and join vertices whose difference is one of
\[
\pm(1,0),\quad \pm(0,1),\quad \pm(1,-1).
\]
This is a 6-regular toroidal triangulation. Its standard embedding has edge-width
\[
\min\{p,q\}\ge4:
\]
a lifted noncontractible cycle ends at a nonzero deck translation \((ap,bq)\), and each edge changes either coordinate by at most one. These graphs satisfy all the structural inequalities above, with
\[
m=3n,\qquad t=2n,\qquad x=3n.
\]

The present argument gives no list-coloring mechanism for this family or for more general dense critical cores. Hence it does not settle the conjecture.