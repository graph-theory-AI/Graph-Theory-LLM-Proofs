```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every positive k, the clique blowup H[K_{2k}] is a union of k planar graphs if and only if H is a forest.",
  "would_publish": false,
  "caveats": "This is an exact special case, not a solution of the Earth–Moon problem; the general 9–12 gap is unchanged, and novelty is not claimed."
}
```

## 1. An exact special case

All graphs below are finite and simple. Write \(\theta(G)\) for the minimum number of planar graphs whose union is \(G\).

For a graph \(H\), let \(H[K_r]\) denote its **clique blowup**: replace each vertex \(x\) by a clique \(V_x\) of order \(r\), and put all edges between \(V_x\) and \(V_y\) whenever \(xy\in E(H)\). With the standard strong-product convention,
\[
H[K_r]=H\boxtimes K_r.
\]

I prove the following restricted result, including a constructive sufficiency proof.

**Theorem.** For every integer \(k\ge1\) and every graph \(H\),
\[
\boxed{\quad \theta\bigl(H[K_{2k}]\bigr)\le k
\quad\Longleftrightarrow\quad
H\text{ is a forest}.\quad}
\]

Consequently, the maximum chromatic number among biplanar graphs of the form \(H[K_4]\) is exactly \(8\). Thus uniform four-vertex clique blowups cannot supply even a nine-colour Earth–Moon example.

The proof also gives elementary obstructions to the literal strong-product graphs appearing in the supplied synopsis.

## 2. The density obstruction

We need both versions of Euler’s edge bound. A graph that is a union of \(k\) planar graphs has at most
\[
k(3n-6)
\]
edges when \(n\ge3\). More importantly:

**Lemma 1.** If a triangle-free graph \(F\) on \(n\ge3\) vertices is a union of \(k\) planar graphs, then
\[
|E(F)|\le k(2n-4).
\tag{1}
\]

**Proof.** Restrict each planar layer to the edges of \(F\). Every resulting layer is planar and triangle-free, so has at most \(2n-4\) edges. Summing proves (1). The planar bound also holds for disconnected graphs: one may first connect their components by bridges without creating triangles. \(\square\)

In particular, (1) applies to **every triangle-free subgraph** of a graph of thickness at most \(k\).

### Necessity in the theorem

Suppose \(H\) contains a cycle of length \(\ell\).

If \(\ell=3\), its three blown-up bags induce \(K_{6k}\). But
\[
|E(K_{6k})|
=\frac{6k(6k-1)}2
=18k^2-3k
>
18k^2-6k
=k\bigl(3(6k)-6\bigr).
\]
Thus \(K_{6k}\), and hence \(H[K_{2k}]\), cannot be a union of \(k\) planar graphs.

Now suppose \(\ell\ge4\). Keep the vertices in the cycle’s bags, but retain only the edges between consecutive bags of that cycle. Delete all within-bag edges and any edges corresponding to chords.

The resulting graph \(F\) is triangle-free and has
\[
|V(F)|=2k\ell,\qquad |E(F)|=(2k)^2\ell=4k^2\ell.
\]
However, (1) would require
\[
|E(F)|
\le k\bigl(2(2k\ell)-4\bigr)
=4k^2\ell-4k,
\]
a contradiction.

Every nonforest contains a cycle, so necessity follows.

## 3. A path decomposition with designated matching edges

The constructive direction uses an elementary decomposition of \(K_{2k}\).

**Lemma 2.** The edges of \(K_{2k}\) can be partitioned into Hamiltonian paths
\[
P_0,\ldots,P_{k-1}
\]
such that each \(P_j\) contains a designated edge \(e_j\), and
\[
\{e_0,\ldots,e_{k-1}\}
\]
is a perfect matching of \(K_{2k}\).

**Proof.** Label the vertices by \(\mathbb Z_{2k}\). For \(0\le j<k\), define the ordered vertices of \(P_j\) by
\[
v^{(j)}_{2r}=j+r,\qquad
v^{(j)}_{2r+1}=j-1-r
\qquad(0\le r<k),
\]
with arithmetic modulo \(2k\). Thus its order is
\[
j,\ j-1,\ j+1,\ j-2,\ \ldots,\ j+k-1,\ j-k.
\]
Each residue occurs exactly once.

The alternate edges
\[
v^{(j)}_{2r}v^{(j)}_{2r+1}
\]
have endpoint sum \(2j-1\), and they exhaust all unordered pairs with that sum. The other edges have endpoint sum \(2j\), and exhaust all non-loop unordered pairs with that sum.

As \(j\) ranges from \(0\) to \(k-1\), these two sum classes range over all residues modulo \(2k\). Hence the paths partition \(E(K_{2k})\).

Designate the central edge
\[
e_j=v^{(j)}_{k-1}v^{(j)}_k.
\]
Its two endpoints differ by \(k\) modulo \(2k\). Moreover, \(e_j\) is the translate of \(e_0\) by \(j\). These \(k\) edges are therefore precisely the antipodal perfect matching, in some order. \(\square\)

## 4. Constructing the planar layers for a forest

We first record the elementary planar building block.

The graph
\[
K_2\vee P_{2k},
\]
where \(\vee\) denotes join, is planar. To see this, write the \(K_2\) vertices as \(u,v\) and the path vertices as \(p_1,\ldots,p_{2k}\). Start with the triangle \(uvp_1\). Successively insert \(p_{i+1}\) in the triangular face \(uvp_i\), joining it to \(u,v,p_i\).

This constructs exactly the desired graph. In this embedding, \(uv\) lies on the outer face. Consequently, the block can be attached to any plane graph along an existing edge \(uv\), with all its other vertices new. Such an attachment preserves planarity.

Now let \(H\) be a forest and root each component. In every bag \(V_x\), use the same labelled copy of the decomposition from Lemma 2. Denote its paths and designated edges by
\[
P_j(x),\qquad e_j(x).
\]

Define layer \(L_j\), for \(0\le j<k\), as follows:

1. In each bag \(V_x\), include the path \(P_j(x)\).
2. For every parent–child edge \(x\to y\) of the rooted forest, include all edges from the two endpoints of \(e_j(x)\) to every vertex of \(V_y\).

### These layers partition all edges

The within-bag edges are partitioned by Lemma 2.

For a parent–child pair \(x\to y\), the designated edges
\[
e_0(x),\ldots,e_{k-1}(x)
\]
partition \(V_x\) into pairs. Thus every edge between \(V_x\) and \(V_y\) belongs to exactly one layer: the layer whose designated pair contains its endpoint in \(V_x\).

Therefore,
\[
E\bigl(H[K_{2k}]\bigr)
=\dot\bigcup_{j=0}^{k-1}E(L_j).
\]

### Every layer is planar

Fix \(j\). Begin with the paths in the root bags, embedded as disjoint components.

Process the remaining bags in parent-before-child order. When adding a child bag \(V_y\) of \(x\), the new portion of \(L_j\), together with the already present edge \(e_j(x)\), is exactly
\[
K_2\vee P_{2k}.
\]
Its intersection with the graph constructed so far is precisely that edge and its endpoints.

Thus each step is an edge attachment of the planar building block described above. Induction proves that \(L_j\) is planar.

This proves sufficiency and completes the theorem. \(\square\)

## 5. The chromatic consequence is sharp

Suppose \(H\) is a forest with at least one edge. Its bipartition gives a colouring of \(H[K_{2k}]\) with \(4k\) colours: use one palette of \(2k\) colours on one side and a disjoint palette on the other.

Conversely, the bags at the ends of any edge of \(H\) induce \(K_{4k}\). Hence
\[
\chi\bigl(H[K_{2k}]\bigr)=4k.
\]

If \(H\) is nonempty and edgeless, the chromatic number is \(2k\). Therefore,
\[
\max\left\{
\chi\bigl(H[K_{2k}]\bigr):
\theta\bigl(H[K_{2k}]\bigr)\le k
\right\}=4k.
\]
Equality is attained by \(H=K_2\), whose blowup is \(K_{4k}\); the construction above supplies the required \(k\) planar layers.

For \(k=2\), this gives the claimed exact maximum \(8\) within the uniform four-clique blowup family.

## 6. Consequences for the displayed cycle-product candidates

Under the standard strong-product definition,
\[
C_\ell\boxtimes K_4=C_\ell[K_4].
\]
The theorem therefore excludes every such graph from being biplanar.

For \(\ell\ge4\), the obstruction remains after deleting **one arbitrary vertex**. Indeed, retain only edges between consecutive cycle bags. After the deletion, this triangle-free subgraph has
\[
N=4\ell-1,\qquad M=16\ell-8.
\]
Biplanarity would require
\[
M\le4N-8=16\ell-12,
\]
which fails by four edges.

In particular, the literal graphs in the synopsis have the following certificates:

| Graph | Vertices of triangle-free subgraph | Edges | Biplanar upper bound |
|---|---:|---:|---:|
| \(C_7\boxtimes K_4\) | \(28\) | \(112\) | \(104\) |
| \((C_5\boxtimes K_4)-v\) | \(19\) | \(72\) | \(68\) |

These are direct Euler-based certificates, not computational conclusions. Any biplanar spanning subgraph of the first graph must omit at least eight inter-bag edges; for the second, at least four more inter-bag edges must be omitted.

**Literature caveat.** This does not identify the precise candidates actually studied in the cited papers, whose definitions I have not independently checked. Additional edge-deletion variants, or a different convention for “blowup,” must be distinguished from these literal strong products. I am not claiming a new refutation of a previously unresolved published candidate.

## 7. What remains unresolved

The special-case classification above is complete and uses only Euler’s bounds and an explicit construction. It does **not** produce a ten-chromatic biplanar graph, nor improve the general twelve-colour upper bound.

There is no reduction here from arbitrary biplanar graphs to uniform clique blowups. Thus the general Earth–Moon interval quoted in the question,
\[
9\le M_2\le12,
\]
is unchanged by this argument. The result supplies an exact restricted classification and rules out this particular blowup route to a stronger lower bound; I have not checked its novelty.