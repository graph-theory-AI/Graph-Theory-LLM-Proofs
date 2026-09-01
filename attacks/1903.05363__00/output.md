```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every 2≤c≤12, D_c≥4c, and D_2 can exceed 8 only through a 2-connected 2-critical graph having no two edge-disjoint Kuratowski subdivisions.",
  "would_publish": false,
  "caveats": "The remaining low-Kuratowski-packing, single-block case is not bounded sharply, so none of D_2,\u2026,D_12 is determined exactly."
}
```

# Mathematical writeup

## 1. Definitions and results obtained

I use the standard threshold definition: \(G\) is \(c\)-crossing-critical if
\[
\operatorname{cr}(G)\ge c
\quad\text{and}\quad
\operatorname{cr}(G-e)<c\qquad\text{for every }e\in E(G).
\]
All arguments remain valid if one additionally requires \(\operatorname{cr}(G)=c\). Graphs are finite and loopless; the density and computational remarks below assume simplicity. Isolated vertices are irrelevant and will be discarded.

The following partial results are proved below.

### Theorem A
For every positive integer \(c\),
\[
D_c\ge 4c.
\]
Consequently, componentwise,
\[
(D_2,\ldots,D_{12})
\ge
(8,12,16,20,24,28,32,36,40,44,48).
\]

### Theorem B
Let \(\nu_K(G)\) be the maximum number of pairwise edge-disjoint subdivisions of \(K_5\) or \(K_{3,3}\) in \(G\). If \(G\) is \(c\)-crossing-critical, then
\[
\nu_K(G)\le c.
\]
Moreover, if \(\nu_K(G)=c\), then
\[
\Delta(G)\le 4c.
\]
Thus \(4c\) is the exact maximum degree among \(c\)-crossing-critical graphs with \(c\) edge-disjoint Kuratowski subdivisions. In particular, any graph witnessing \(D_c>4c\) must satisfy \(\nu_K(G)\le c-1\).

### Theorem C
After isolated vertices are discarded, every non-2-connected \(2\)-crossing-critical graph consists of exactly two \(1\)-crossing-critical blocks. Each block is a subdivision of \(K_5\) or \(K_{3,3}\), and hence
\[
\Delta(G)\le 8.
\]
Equality is attained by two copies of \(K_5\) identified at one vertex.

It follows that
\[
D_2=8
\]
would be proved once one establishes \(\Delta(G)\le8\) for the following residual class:

- \(G\) is 2-connected and 2-crossing-critical;
- \(G\) has no two edge-disjoint Kuratowski subdivisions.

No bound of \(8\) for this residual class is proved here.

---

## 2. Edge-disjoint nonplanar subgraphs

We begin with a basic but useful observation.

### Lemma 2.1
If \(H_1,\ldots,H_r\) are pairwise edge-disjoint subgraphs of \(G\), then
\[
\operatorname{cr}(G)\ge \sum_{i=1}^r \operatorname{cr}(H_i).
\]

#### Proof
Take a good drawing of \(G\), with no triple crossing points. Restrict it to \(H_i\). There must be at least \(\operatorname{cr}(H_i)\) crossings between pairs of edges both belonging to \(H_i\). Since the edge sets of the \(H_i\) are disjoint, a crossing internal to \(H_i\) cannot also be internal to \(H_j\) for \(i\ne j\). Summing these internal crossings gives the assertion. ∎

### Proof of Theorem B

Suppose first that \(G\) contains \(c+1\) pairwise edge-disjoint Kuratowski subdivisions
\[
S_1,\ldots,S_{c+1}.
\]
For any edge \(e\), at most one \(S_i\) contains \(e\). Thus \(G-e\) still contains at least \(c\) of the subdivisions. Lemma 2.1 gives
\[
\operatorname{cr}(G-e)\ge c,
\]
contrary to \(c\)-criticality. Hence \(\nu_K(G)\le c\).

Now suppose \(\nu_K(G)=c\), witnessed by \(S_1,\ldots,S_c\). If an edge \(e\) lay outside their union, then all \(c\) subdivisions would survive in \(G-e\), again implying
\[
\operatorname{cr}(G-e)\ge c.
\]
Therefore
\[
E(G)=\bigcup_{i=1}^c E(S_i).
\]
Every subdivision of \(K_5\) or \(K_{3,3}\) has maximum degree at most \(4\). Since the \(S_i\) are edge-disjoint,
\[
d_G(v)=\sum_{i=1}^c d_{S_i}(v)\le 4c
\]
for every vertex \(v\). Thus \(\Delta(G)\le4c\). ∎

---

## 3. The lower bound \(D_c\ge4c\)

Let \(W_c\) be obtained from \(c\) vertex-disjoint copies of \(K_5\) by identifying one chosen vertex from every copy to a common vertex \(v\).

The \(c\) copies remain edge-disjoint. In every drawing, the restriction to each copy of \(K_5\) has an internal crossing, so Lemma 2.1 yields
\[
\operatorname{cr}(W_c)\ge c.
\]
Conversely, draw the copies in pairwise disjoint small regions meeting only at \(v\), using one crossing in each copy. Hence
\[
\operatorname{cr}(W_c)=c.
\]

If \(e\) belongs to one copy of \(K_5\), then \(K_5-e\) is planar. Drawing that copy without crossings and each of the other \(c-1\) copies with one crossing gives
\[
\operatorname{cr}(W_c-e)\le c-1.
\]
The remaining \(c-1\) intact copies force the reverse inequality, so
\[
\operatorname{cr}(W_c-e)=c-1.
\]
Thus \(W_c\) is \(c\)-crossing-critical. Finally,
\[
d_{W_c}(v)=4c.
\]
This proves Theorem A.

---

## 4. Block decomposition

The crossing number is additive over blocks.

### Lemma 4.1
If \(B_1,\ldots,B_b\) are the edge-containing blocks of \(G\), then
\[
\operatorname{cr}(G)=\sum_{i=1}^b\operatorname{cr}(B_i).
\]

#### Proof
In any drawing of \(G\), restricting to \(B_i\) gives at least \(\operatorname{cr}(B_i)\) crossings internal to \(B_i\). These internal crossing sets are disjoint, proving the lower bound.

For the upper bound, root the block-cutvertex forest. Draw a root block optimally. At each cutvertex, place each descendant block, suitably scaled, in a separate sufficiently small sector incident with that cutvertex. Repeating recursively introduces no crossings between distinct blocks. ∎

The following form keeps track of the possibility that a threshold-critical graph has crossing number greater than its threshold.

### Proposition 4.2
Let \(G\) be \(c\)-crossing-critical, let
\[
K=\operatorname{cr}(G)=c+q,
\qquad q\ge0,
\]
and let its edge-containing blocks be \(B_1,\ldots,B_b\), with
\[
k_i=\operatorname{cr}(B_i).
\]
Then:

1. \(k_i\ge1\) for every \(i\);
2. for every \(e\in E(B_i)\),
   \[
   \operatorname{cr}(B_i-e)\le k_i-q-1;
   \]
3. in particular, \(k_i\ge q+1\);
4. and
   \[
   b(q+1)\le c+q.
   \]

Consequently \(b\le c\). If \(b=c\), then \(q=0\) and \(k_i=1\) for every \(i\).

#### Proof
If \(B_i\) were planar, deleting an edge of \(B_i\) would not change the sum of the crossing numbers of the other blocks, and hence would not lower the crossing number below \(c\). Thus \(k_i\ge1\).

For \(e\in E(B_i)\), block additivity gives
\[
\operatorname{cr}(G-e)
=
\operatorname{cr}(B_i-e)+K-k_i.
\]
Since this is at most \(c-1\),
\[
\operatorname{cr}(B_i-e)
\le c-1-K+k_i
= k_i-q-1.
\]
The left side is nonnegative, giving \(k_i\ge q+1\). Summing over all blocks,
\[
c+q=K=\sum_i k_i\ge b(q+1).
\]
If \(b\ge2\), this can be rewritten as
\[
(b-1)q\le c-b,
\]
which implies \(b\le c\). The case \(b=1\) is immediate. If \(b=c\), then \((c-1)q\le0\), so \(q=0\), and the \(c\) positive integers \(k_i\) sum to \(c\); hence all equal \(1\). ∎

### Corollary 4.3
If a \(c\)-crossing-critical graph has exactly \(c\) edge-containing blocks, then every block is a subdivision of \(K_5\) or \(K_{3,3}\), and
\[
\Delta(G)\le4c.
\]
This is sharp.

#### Proof
By Proposition 4.2, every block is \(1\)-crossing-critical. Let \(B\) be such a block. By Kuratowski's theorem, \(B\) contains a subdivision \(S\) of \(K_5\) or \(K_{3,3}\). If \(B\) had an edge outside \(S\), deleting that edge would leave the nonplanar subdivision \(S\), contradicting \(1\)-criticality. Hence \(B=S\), and \(\Delta(B)\le4\).

At a vertex, degrees contributed by incident blocks add. There are at most \(c\) blocks, so the total is at most \(4c\). The graphs \(W_c\) attain equality. ∎

Equality requires a vertex lying in all \(c\) blocks and having degree \(4\) in each; in particular, all these blocks must be \(K_5\)-subdivisions with that vertex as a degree-four branch vertex.

---

## 5. Complete analysis of the non-2-connected \(c=2\) case

Let \(G\) be 2-crossing-critical and have at least two edge-containing blocks. Proposition 4.2 gives
\[
b=2,\qquad q=0,\qquad k_1=k_2=1.
\]
Thus both blocks are subdivisions of \(K_5\) or \(K_{3,3}\).

If \(G\) is connected, the two blocks meet in exactly one cutvertex. At that vertex,
\[
d_G(v)=d_{B_1}(v)+d_{B_2}(v)\le4+4=8.
\]
Every other vertex has degree at most \(4\). If the blocks are in distinct components, the maximum degree is at most \(4\).

The upper bound \(8\) is attained by identifying one vertex of two copies of \(K_5\). Therefore:

> Among non-2-connected 2-crossing-critical graphs, the exact optimal maximum degree is \(8\).

Combining this with Theorem B gives the precise residual formulation
\[
D_2=8
\iff
\Delta(G)\le8
\]
for every 2-connected 2-crossing-critical graph \(G\) with \(\nu_K(G)=1\).

For such a residual graph, fix a Kuratowski subdivision \(S\). Then:

1. \(G-E(S)\) is planar, since otherwise it would contain a Kuratowski subdivision edge-disjoint from \(S\);
2. for every \(e\notin E(S)\), \(G-e\) has crossing number exactly \(1\);
3. in every at-most-one-crossing drawing of \(G-e\), the unique crossing is between two edges of \(S\).

The last assertion follows because the surviving nonplanar subdivision \(S\) itself requires an internal crossing. Thus the unresolved case can be viewed as a planar collection of \(S\)-bridges which is edge-minimal for preventing a one-crossing extension of \(S\).

---

## 6. Further general filters

### Planarizing sets

For every edge \(e\) of a \(c\)-crossing-critical graph, there is a set
\[
S_e\subseteq E(G),\qquad e\in S_e,\qquad |S_e|\le c,
\]
such that \(G-S_e\) is planar.

Indeed, take a drawing of \(G-e\) with at most \(c-1\) crossings and choose one participating edge from each crossing. Deleting those chosen edges together with \(e\) leaves the inherited drawing crossing-free.

For \(c=2\), every edge therefore belongs to a planarizing set of size at most two.

### Density

If \(G\) is simple, with \(n\ge3\) vertices and \(m\) edges, then
\[
m\le3n+c-6.
\]
To see this, fix \(e\) and a drawing of \(G-e\) with \(x\le c-1\) crossings. Deleting at most \(x\) edges removes all crossings, leaving a planar simple graph with at least \(m-1-x\) edges. Therefore
\[
m-1-x\le3n-6,
\]
which yields the claimed bound. In particular, every simple 2-crossing-critical graph satisfies
\[
m\le3n-4.
\]

These estimates do not control maximum degree by themselves, but they are useful for an exhaustive search.

---

## 7. An exact computational test for the residual \(c=2\) class

For a finite simple graph \(H\), the predicate \(\operatorname{cr}(H)\le1\) can be tested exactly as follows.

1. Test whether \(H\) is planar.
2. Otherwise, for every pair of independent edges
   \[
   e=ab,\qquad f=cd,
   \]
   delete \(e,f\), introduce a new vertex \(x\), and add
   \[
   ax,bx,cx,dx.
   \]
3. Test whether the resulting graph has a planar embedding in which the four darts at \(x\) alternate between the two original edges; for example, their cyclic order is
   \[
   a,c,b,d
   \]
   up to reversal and relabelling.

This criterion is necessary by planarizing the unique crossing of a good one-crossing drawing. It is sufficient because a small neighborhood of \(x\) can be replaced by one crossing joining \(a\) to \(b\) and \(c\) to \(d\).

The prescribed-rotation planarity test can be implemented either by a constrained-planarity algorithm or by brute-force enumeration of rotation systems and checking Euler characteristic. Hence, for any fixed \(N\), one can exhaustively enumerate all simple graphs on at most \(N\) vertices and retain precisely those satisfying
\[
\operatorname{cr}(G)>1,
\qquad
\operatorname{cr}(G-e)\le1\quad\text{for every }e.
\]

No such computation was performed here. Moreover, an order cutoff for all unresolved homeomorphically irreducible cores is still needed before a finite search proves \(D_2=8\). The supplied catalog mentions a characterization of large 2-crossing-critical graphs, but I have not verified a precise numerical cutoff or checked all exceptional and lower-connectivity cases, so I do not use it to claim an upper bound.

---

## 8. Gap and conclusion

The exact requested values remain undetermined. The main concrete conclusions are:

\[
D_c\ge4c\qquad(2\le c\le12),
\]
with equality proved within the class packing \(c\) edge-disjoint Kuratowski subdivisions, and the entire non-2-connected \(c=2\) case has exact maximum degree \(8\).

To settle \(D_2=8\), it remains to handle 2-connected 2-crossing-critical graphs whose Kuratowski subdivisions are pairwise edge-intersecting. For \(c=3,\ldots,12\), any example with degree greater than \(4c\) must similarly have Kuratowski edge-packing number at most \(c-1\). No valid argument here bounds those intertwined cases by \(4c\), and no counterexample is produced.