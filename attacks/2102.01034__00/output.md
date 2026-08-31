```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "Although the full problem remains open, on the projective plane a digraph is 5-dicolourable exactly when it contains no bidirected K6, and both values admit a sparse-digon kernel on every fixed surface.",
  "would_publish": false,
  "caveats": "The unrestricted k=4 case and k=5 on other nonspherical surfaces remain unresolved; the projective-plane argument uses the standard theorem that K6 is the only 6-critical projective-planar graph."
}
```

## 1. Statement and conventions

I interpret \(\Sigma\)-\(k\)-DICOLOURABILITY as allowing digons. This is the interpretation consistent with the threshold \(k\ge 6\) in the source. For oriented inputs, the peeling argument below already gives a polynomial algorithm for \(k=4,5\).

For a loopless digraph \(D\), let:

- \(U(D)\) be its underlying simple graph;
- \(B(D)\) be its **digon graph**, where \(uv\in E(B(D))\) precisely when both \(uv\) and \(vu\) are arcs of \(D\);
- \(\vec\chi(D)\) be its dichromatic number.

Then
\[
\chi(B(D))\leq \vec\chi(D)\leq \chi(U(D)).
\tag{1}
\]
The first inequality holds because the ends of a digon must receive different colours; the second holds because every proper colouring of \(U(D)\) is a dicolouring of \(D\).

I establish two partial results.

### Theorem A: complete solution for \(k=5\) on the projective plane

Let \(\mathbb P^2\) denote the projective plane. If \(D\) is a loopless digraph whose underlying graph embeds in \(\mathbb P^2\), then
\[
\boxed{\quad \vec\chi(D)\leq 5
\quad\Longleftrightarrow\quad
B(D)\text{ contains no }K_6.\quad}
\]

Thus \(\mathbb P^2\)-5-DICOLOURABILITY is polynomial-time solvable: enumerate the six-vertex subsets and test whether every pair is a digon. The naive running time is \(O(n^6+n+m)\).

### Theorem B: a sparse-digon kernel on every fixed surface

Let \(k\in\{4,5\}\), and repeatedly delete a vertex whose current indegree or current outdegree is less than \(k\). Let \(H\) be the resulting \(k\)-core, so every vertex of \(H\) has indegree and outdegree at least \(k\).

Set
\[
t_k(H)=\bigl|\{v\in V(H):d_{B(H)}(v)\geq 2k-6\}\bigr|.
\]
If \(H\neq\varnothing\) and \(c=\chi(\Sigma)\), then
\[
|V(H)|\leq (7-k)t_k(H)-6c.
\tag{2}
\]
Moreover, \(D\) is \(k\)-dicolourable if and only if \(H\) is.

Consequently the problem is fixed-parameter tractable in \(t_k(H)\), with a kernel of at most
\[
\begin{cases}
3t_4(H)-6c,&k=4,\\
2t_5(H)-6c,&k=5
\end{cases}
\]
vertices.

In particular:

- \(k=4\) is polynomial-time solvable when every vertex is incident with at most one digon;
- \(k=5\) is polynomial-time solvable when every vertex is incident with at most three digons;
- for oriented graphs, both \(k=4\) and \(k=5\) are polynomial-time solvable on every fixed surface.

---

## 2. Proof of Theorem A

The only external graph-colouring ingredient is the following classical projective-plane theorem.

> **Projective-plane 5-colour theorem.**  
> If a simple graph embedded in the projective plane is not 5-colourable, then it contains \(K_6\) as a subgraph. Equivalently, \(K_6\) is the only 6-critical projective-planar graph.

This is an established theorem, not an open conjecture.

### 2.1. The easy obstruction

If \(B(D)\) contains \(K_6\), then the corresponding six vertices induce all fifteen digons. Any two vertices receiving the same colour form a monochromatic directed \(2\)-cycle. Therefore those six vertices require six colours, and \(D\) is not 5-dicolourable.

It remains to prove the converse.

### 2.2. The topology of an embedded \(K_6\)

Let \(Q\cong K_6\) be embedded in \(\mathbb P^2\).

The nonorientable Euler genus of \(K_6\) is one, so every projective-plane embedding of \(K_6\) is cellular: otherwise an essential curve disjoint from \(Q\) could be used to reduce the embedding to the sphere, contradicting nonplanarity.

Euler's formula gives
\[
6-15+f=1,
\]
so \(f=10\). Since
\[
\sum_F |\partial F|=2|E(K_6)|=30
\]
and every facial boundary has length at least three, all ten faces are triangles.

Consequently, if a graph \(G\) containing this embedded \(K_6\) is also embedded in \(\mathbb P^2\), every component of \(G-V(Q)\) lies in one of the ten triangular faces of \(Q\), and it can be adjacent only to the three vertices on that facial triangle.

### 2.3. Colouring around a non-bidirected edge

Assume now that \(B(D)\) contains no \(K_6\).

If \(U(D)\) is 5-colourable, a proper 5-colouring of \(U(D)\) is already a 5-dicolouring of \(D\). We may therefore suppose that \(U(D)\) is not 5-colourable. By the projective-plane theorem, \(U(D)\) contains a subgraph
\[
Q\cong K_6.
\]

Since \(B(D)\) has no \(K_6\), there are vertices \(x,y\in V(Q)\) such that \(xy\) is not a digon. Because \(xy\in E(U(D))\), there is exactly one direction of arc between \(x\) and \(y\).

Colour \(x\) and \(y\) with colour \(1\), and colour the other four vertices of \(Q\) bijectively with \(2,3,4,5\). This is a dicolouring of \(D[Q]\): its only nonsingleton colour class is \(\{x,y\}\), and that class contains at most one arc.

We now extend this colouring independently inside every triangular face of \(Q\).

#### Faces not incident with \(xy\)

The three boundary vertices have three distinct prescribed colours. Let \(G_F\) be the graph drawn in the closure of such a face, including its boundary triangle. By the Four Colour Theorem, \(G_F\) has a proper colouring using at most four abstract colours. Its boundary triangle receives three distinct abstract colours, so a permutation and injection of those colours into \(\{1,\dots,5\}\) makes the colouring agree with the prescribed boundary colours.

Thus \(G_F\) can be coloured properly while retaining the colours on its boundary.

#### The two faces incident with \(xy\)

Such a face has boundary \(xyz\), where \(x,y\) have colour \(1\) and \(z\) has some colour \(j\in\{2,3,4,5\}\).

Delete \(x\) and \(y\) from the graph drawn in this face. The remaining graph is planar, so it has a proper 4-colouring. Relabel its colours using the palette
\[
\{2,3,4,5\}
\]
so that \(z\) receives its prescribed colour \(j\). Reinsert \(x\) and \(y\) with colour \(1\).

Every edge in this face is now properly coloured except \(xy\).

### 2.4. Combining the face colourings

Different face interiors are disjoint and there are no edges between them. Every component outside \(Q\) attaches only to the boundary triangle of its face. The preceding colourings therefore combine into a colouring of all of \(U(D)\).

In the resulting colouring, the only possible monochromatic underlying edge is \(xy\). Since \(xy\) is not a digon, this single arc cannot form a directed cycle. Hence every colour class is acyclic.

This proves that \(D\) is 5-dicolourable and completes the proof of Theorem A.

---

## 3. The sparse-digon kernel

### 3.1. Peeling low-semidegree vertices

Suppose \(v\) has \(d^+(v)<k\), and \(D-v\) has a \(k\)-dicolouring. Some colour is absent from \(N^+(v)\); give \(v\) that colour. A newly created monochromatic directed cycle would have to contain \(v\), and hence would have to leave \(v\) along a same-coloured out-arc, which is impossible.

The argument is symmetric when \(d^-(v)<k\). Therefore
\[
D\text{ is \(k\)-dicolourable}
\quad\Longleftrightarrow\quad
D-v\text{ is \(k\)-dicolourable}
\]
whenever \(d^+(v)<k\) or \(d^-(v)<k\).

Deleting such vertices repeatedly and then reinserting them in reverse order proves that \(D\) is \(k\)-dicolourable exactly when its resulting core \(H\) is.

### 3.2. A necessary digon density

Let

- \(n=|V(H)|\);
- \(m=|E(U(H))|\);
- \(q=|E(B(H))|\);
- \(a=|A(H)|\).

Each underlying edge contributes one arc, and each digon contributes one additional arc, so
\[
a=m+q.
\]
Since every vertex has outdegree at least \(k\),
\[
a=\sum_v d^+(v)\geq kn.
\]
For a simple graph embedded in a surface of Euler characteristic \(c\),
\[
m\leq 3n-3c.
\]
It follows that
\[
q=a-m\geq kn-(3n-3c)
   =(k-3)n+3c.
\tag{3}
\]

Thus any surviving core must have many digons:

- for \(k=4\), approximately at least \(n\) digons;
- for \(k=5\), approximately at least \(2n\) digons.

This quantifies why the oriented case is much easier.

### 3.3. Bounding the kernel by high-digon vertices

For \(v\in V(H)\), let \(b(v)=d_{B(H)}(v)\). Since a digon-neighbour is counted in both \(N^+(v)\) and \(N^-(v)\),
\[
d_{U(H)}(v)
 =d^+(v)+d^-(v)-b(v)
 \geq 2k-b(v).
\tag{4}
\]
Also, trivially,
\[
d_{U(H)}(v)\geq k.
\tag{5}
\]

Call \(v\) low if \(b(v)\leq 2k-7\), and high otherwise. Every low vertex has underlying degree at least seven by (4); every high vertex has degree at least \(k\) by (5).

Let \(\ell\) and \(t\) denote the numbers of low and high vertices. Then
\[
2m=\sum_v d_{U(H)}(v)\geq 7\ell+kt.
\]
On the other hand,
\[
2m\leq 6(\ell+t)-6c.
\]
Hence
\[
7\ell+kt\leq 6\ell+6t-6c,
\]
and therefore
\[
\ell\leq (6-k)t-6c.
\]
Adding \(t\) gives
\[
n=\ell+t\leq (7-k)t-6c,
\]
which is (2).

One may now test all \(k^{|V(H)|}\) colour assignments, check each colour class for acyclicity, and then reinsert the peeled vertices. For fixed \(\Sigma\), this is fixed-parameter tractable in \(t\).

For \(k=4\), high means incident with at least two digons. For \(k=5\), high means incident with at least four digons. This proves all the stated corollaries.

---

## 4. Why a bounded-obstruction proof cannot settle \(k=4\)

There are arbitrarily large vertex-minimal non-4-dicolourable toroidal digraphs.

Let
\[
G_r=K_2\vee C_r,
\]
where \(r\geq3\) is odd and \(\vee\) denotes graph join. Then
\[
\chi(G_r)=\chi(K_2)+\chi(C_r)=2+3=5.
\]
Deleting either hub leaves \(K_1\vee C_r\), which is 4-colourable, and deleting a cycle vertex leaves \(K_2\vee P_{r-1}\), also 4-colourable.

Moreover, if \(ab\) is the edge joining the two hubs, then \(G_r-ab\) is planar: draw the cycle as an equator, one hub inside and one outside. Adding the single edge \(ab\) can be routed through one handle, so \(G_r\) is toroidal.

Replace every edge of \(G_r\) by a digon. The resulting digraph \(\overleftrightarrow{G_r}\) satisfies
\[
\vec\chi(\overleftrightarrow{G_r})=\chi(G_r)=5,
\]
but deleting any vertex makes it 4-dicolourable. Hence the orders of vertex-minimal toroidal NO-instances for \(k=4\) are unbounded.

Thus the finite-critical-core argument used for larger \(k\) cannot extend directly to unrestricted \(k=4\).

---

## 5. Additional complexity observation

For every graph \(G\), replacing each edge by a digon gives
\[
\vec\chi(\overleftrightarrow G)=\chi(G),
\]
without changing surface embeddability. Therefore ordinary \(\Sigma\)-\(k\)-COLOURABILITY many-one reduces to \(\Sigma\)-\(k\)-DICOLOURABILITY. Any verified hardness result for the former transfers immediately to the latter.

I do not invoke any unverified surface-colouring complexity classification here.

---

## 6. Remaining gaps

The original problem is not fully resolved.

1. The unrestricted \(k=4\) problem remains open here, already for the torus.
2. For \(k=5\), the argument resolves the projective plane but not the torus, Klein bottle, or higher-genus surfaces.
3. The sparse-digon kernel does not yield a polynomial algorithm when the number of vertices incident with many digons is linear.
4. The projective-plane proof uses two established external results: the Four Colour Theorem and the theorem that every non-5-colourable projective-planar graph contains \(K_6\). No unproved conjecture is used.
5. If the catalog intended **oriented** rather than general digraph inputs, then the peeling/kernel argument gives a complete polynomial-time classification for both \(k=4\) and \(k=5\); the genuinely open interpretation is the one allowing digons.