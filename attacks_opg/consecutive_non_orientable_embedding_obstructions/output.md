```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I rule out overlap involving the projective plane and derive degree, girth, edge-count, and Euler-genus restrictions on any common obstruction.",
  "would_publish": false,
  "caveats": "Existence for higher non-orientable surfaces is not settled here; no claim of novelty for these restrictions."
}
```

## 1. A classification-free partial result

Write \(N_k\) for the closed non-orientable surface of genus \(k\), and let \(\mathcal O_k\) be its set of minor-minimal embedding obstructions. Write \(\widetilde\gamma(G)\) for non-orientable genus, with value \(0\) for planar graphs.

All graphs below are finite and simple. This loses nothing for surface-embedding forbidden minors: loops and additional parallel edges can always be restored to an embedding locally.

**Theorem.** Suppose
\[
G\in\mathcal O_k\cap\mathcal O_\ell,\qquad 1\le k<\ell.
\]
Put \(n=|V(G)|\) and \(q=|E(G)|\). Then:

1. \(\ell=k+1\) and \(\widetilde\gamma(G)=k+2\).
2. \(G\) is triangle-free and \(\delta(G)\ge4\).
3. 
   \[
   2n\le q\le 2n+2k-3.
   \]
   In particular, \(k\ge2\), and
   \[
   \sum_{v\in V(G)}(d(v)-4)\le4k-6.
   \]

Consequently, **every minor-minimal obstruction for the projective plane embeds in the Klein bottle**, and
\[
\mathcal O_1\cap\mathcal O_\ell=\varnothing
\qquad(\ell\ge2).
\]

The proof does not use a list of projective-plane obstructions.

## 2. Edge insertion forces consecutivity

An embedding of \(G-e\) in \(N_k\) can be extended to an embedding of \(G\) in \(N_{k+2}\): attach a handle between small complementary discs near the two endpoints of \(e\), and draw \(e\) through it. Since \(N_k\) is already non-orientable, the resulting surface is \(N_{k+2}\).

For the graph in the theorem, every proper minor embeds in \(N_k\). Hence
\[
\widetilde\gamma(G)\le k+2.
\]
But \(G\) does not embed in \(N_\ell\), so
\[
\widetilde\gamma(G)\ge\ell+1.
\]
Together with \(\ell>k\), this gives
\[
\ell=k+1,\qquad \widetilde\gamma(G)=k+2.
\]

Thus the question is exactly whether there is a graph of non-orientable genus \(k+2\) all of whose proper minors embed in \(N_k\).

## 3. Two local one-crosscap surgeries

The following elementary construction is useful.

Replace a vertex-disc of an embedded graph by a Möbius band with the same boundary. Given two distinct prescribed boundary points, choose an essential properly embedded arc \(\alpha\) joining them. Cutting the Möbius band along \(\alpha\) produces a disc.

Inside that cut-open disc, a star can be drawn joining its centre to any prescribed collection of boundary points. This gives two surgeries.

### 3.1 Adding an edge that completes a triangle

**Lemma 1.** If \(xy\notin E(H)\), but \(H\) contains a path \(xzy\), then
\[
H\text{ embeds in }N_h
\quad\Longrightarrow\quad
H+xy\text{ embeds in }N_{h+1}.
\]

**Proof.** Take a small vertex-disc around \(z\). On its boundary choose two new points, respectively adjacent to the ports of \(zx\) and \(zy\). Replace the disc by a Möbius band and choose an essential arc \(\alpha\) joining those new points.

After cutting along \(\alpha\), redraw the original star at \(z\) in the resulting disc, with all its old boundary ports unchanged. The star is disjoint from the interior of \(\alpha\).

Draw the new edge \(xy\) parallel to \(xz\) outside the replaced disc, then along \(\alpha\), then parallel to \(zy\). This adds precisely one crosscap. ∎

### 3.2 Undoing a contraction at a degree-three vertex

**Lemma 2.** Suppose \(G\) is triangle-free, \(v\) has degree three, and \(e=uv\). Then
\[
G/e\text{ embeds in }N_h
\quad\Longrightarrow\quad
G\text{ embeds in }N_{h+1}.
\]

**Proof.** Triangle-freeness ensures that contracting \(uv\) creates no parallel edges. Let \(w\) be the contracted vertex. Two of the boundary ports at \(w\) correspond to the other two edges formerly incident with \(v\).

Replace the vertex-disc at \(w\) by a Möbius band. Choose an essential arc \(\alpha\) between these two ports, and put \(v\) at an interior point of \(\alpha\). Its two subarcs provide the two corresponding edge segments at \(v\).

Cutting along \(\alpha\) leaves a disc. Put \(u\) inside that disc, and draw a star joining \(u\) to all remaining old boundary ports and to one copy of \(v\) on the cut boundary. The latter connection is \(uv\). Regluing gives the desired embedding of \(G\). ∎

These arguments work for arbitrary embeddings; cellularity is not required.

## 4. Triangle-freeness and minimum degree

Return to a hypothetical common obstruction \(G\), with
\[
\widetilde\gamma(G)=k+2
\]
and every proper minor embeddable in \(N_k\).

If \(G\) contains a triangle \(xyz\), then \(G-xy\) embeds in \(N_k\). Lemma 1 gives an embedding of \(G\) in \(N_{k+1}\), a contradiction. Thus \(G\) is triangle-free.

Minor-minimality excludes vertices of degree zero or one: they can be restored locally to an embedding after deletion. It also excludes a degree-two vertex. Indeed, in a triangle-free graph, suppressing such a vertex is an edge contraction, and the original graph is recovered by subdividing an edge.

Finally, if \(v\) has degree three, contract an incident edge. The resulting proper minor embeds in \(N_k\), and Lemma 2 embeds \(G\) in \(N_{k+1}\), again a contradiction.

Therefore
\[
\delta(G)\ge4,
\qquad\text{so}\qquad q\ge2n.
\]

## 5. Euler counting, including noncellular embeddings

We need a version of the usual girth bound that does not silently assume connectivity or cellularity.

**Lemma 3.** Let \(H\) be a simple graph of minimum degree at least two and girth at least \(r\ge3\). If \(H\) embeds in \(N_k\), then
\[
|E(H)|\le \frac{r}{r-2}\bigl(|V(H)|-2+k\bigr).
\]

**Proof.** Take a closed regular neighbourhood \(R\) of the embedded graph, and let \(b\) be its number of boundary components.

Each boundary component traces a closed walk in \(H\). Because the minimum degree is at least two, such a walk has no immediate reversal. It therefore contains a cycle and has length at least \(r\). Each edge contributes two sides, so
\[
rb\le2|E(H)|.
\]

Every component of the complementary surface has nonempty boundary, and its Euler characteristic is at most its number of boundary components. Since \(R\) deformation retracts onto \(H\),
\[
2-k
\le |V(H)|-|E(H)|+b
\le |V(H)|-\frac{r-2}{r}|E(H)|.
\]
Rearranging proves the claim. ∎

Apply this to \(H=G-e\), for any edge \(e\). We have \(\delta(H)\ge3\), and \(H\) is triangle-free. Thus
\[
q-1\le2n-4+2k,
\]
or
\[
q\le2n+2k-3.
\]
Together with \(q\ge2n\), this yields
\[
2k\ge3,
\]
hence \(k\ge2\). Also,
\[
\sum_v(d(v)-4)=2q-4n\le4k-6.
\]

This completes the theorem.

In particular, if a projective-plane obstruction failed to embed in the Klein bottle, it would be a common obstruction for \(N_1\) and \(N_2\), which the theorem excludes.

## 6. Further restrictions on the remaining cases

### 6.1 The first remaining index is nearly four-regular

For a possible overlap between \(N_2\) and \(N_3\),
\[
\sum_v(d(v)-4)\le2.
\]
This sum is nonnegative and even. Therefore the degree sequence must have one of these forms:

- every vertex has degree \(4\);
- one vertex has degree \(6\), and all others have degree \(4\);
- two vertices have degree \(5\), and all others have degree \(4\).

More generally, a common obstruction for \(N_k,N_{k+1}\) has at most \(4k-6\) vertices of degree greater than four, and
\[
\Delta(G)\le4k-2.
\]

### 6.2 Higher girth forces a larger surface index

If \(G\) has girth at least \(r\ge5\), Lemma 3 applied to \(G-e\), together with \(q-1\ge2n-1\), gives
\[
2n-1\le\frac{r}{r-2}(n-2+k).
\]
Equivalently,
\[
\boxed{(r-4)n+r+2\le rk.}
\]

For girth at least five, this becomes
\[
n+7\le5k.
\]
Minimum degree four and girth at least five imply \(n\ge17\): a vertex, four of its neighbours, and three further neighbours of each are all distinct. Consequently,
\[
k\ge5.
\]

Thus, for \(k=2,3,4\), any common obstruction must contain a \(4\)-cycle, although it cannot contain a triangle.

### 6.3 Every edge deletion must lower non-orientable genus exactly two

For any remaining possible example, \(k\ge2\). For every edge \(e\),
\[
\widetilde\gamma(G-e)=k.
\]
Indeed, if \(G-e\) embedded in \(N_{k-1}\), adding a handle would embed \(G\) in \(N_{k+1}\), contrary to the required genus \(k+2\).

This statement concerns edge deletions. Contractions may lower genus further.

### 6.4 An Euler-genus dichotomy

Let \(\operatorname{eg}(G)\) denote minimum Euler genus over orientable and non-orientable surfaces. The elementary inequalities
\[
\operatorname{eg}(G)\le\widetilde\gamma(G)
\le\operatorname{eg}(G)+1
\]
follow because an orientable minimum-Euler-genus embedding can be made non-orientable by adding one crosscap.

Hence a common obstruction satisfies
\[
\operatorname{eg}(G)\in\{k+1,k+2\}.
\]

There are two possibilities:

- **Euler genus \(k+2\).** Every proper minor has Euler genus at most \(k\), so every proper minor lowers Euler genus by at least two.
- **Euler genus \(k+1\).** Minimum-Euler-genus embeddings must be orientable, since \(G\) does not embed in \(N_{k+1}\). Therefore \(k+1\) is even, so \(k\) is odd.

In particular, when \(k\) is even, necessarily
\[
\operatorname{eg}(G)=\widetilde\gamma(G)=k+2.
\]

## 7. What remains unresolved

These arguments do **not** decide whether a common obstruction exists.

The first case not excluded by this proof is \(k=2\): a triangle-free graph of Euler genus and non-orientable genus \(4\), with one of the three degree patterns above, all of whose proper minors embed in the Klein bottle.

The counting argument leaves arbitrarily many degree-four vertices unconstrained. Eliminating—or constructing—graphs satisfying the remaining minor-embedding conditions requires information beyond these local surgeries and Euler inequalities. No such graph, and no general impossibility proof, is established here.