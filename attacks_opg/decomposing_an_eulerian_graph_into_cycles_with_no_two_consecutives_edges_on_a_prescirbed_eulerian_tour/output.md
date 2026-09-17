```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a controlled-defect decomposition, reduce the conjecture to degrees 4 and 6, and prove a compatible-factorization theorem for regular bipartite graphs.",
  "would_publish": false,
  "caveats": "The general conjecture is not settled; these self-contained partial results may be known, and no novelty or current-literature claim is made."
}
```

# Constructive partial results

Work with finite undirected simple graphs. The arguments also apply to loopless multigraphs if cycles of length two are permitted. An Eulerian tour is regarded cyclically, so its last and first edges are consecutive.

For a vertex \(v\), the prescribed tour \(W\) partitions its incident edges into
\[
r(v):=\frac{d(v)}2
\]
pairs: the arrival and departure edges at each visit to \(v\). Call these the **forbidden transitions** at \(v\).

A cycle decomposition is compatible precisely when the two edges of every forbidden transition belong to different cycles.

The results below establish:

1. A cycle decomposition with at most one violated transition at each vertex of degree \(2\bmod 4\), and no violations elsewhere. The potentially violated transition at each such vertex can be prescribed in advance.
2. A reduction of the full conjecture to graphs whose degrees belong to \(\{4,6\}\).
3. The conjecture for every regular Eulerian bipartite graph, and more generally for bipartite graphs whose degrees have a common divisor \(2r\), where \(r\ge2\).

## 1. A decomposition with explicitly controlled defects

### Proposition 1

Let \(G\) be Eulerian, let \(W\) be an Eulerian tour, and put
\[
B=\{v\in V(G):d(v)\equiv2\pmod4\}.
\]
For each \(v\in B\), choose one forbidden transition \(P_v\) at \(v\).

Then \(G\) has a cycle decomposition in which every violated forbidden transition belongs to
\[
\{P_v:v\in B\}.
\]
In particular, the number of violated transitions is at most \(|B|\).

### Proof

Write \(m=|E(G)|\) and \(k=|B|\). Color the edges red and blue while following the cyclic tour \(W\), according to these rules:

- change color at every transition other than the chosen \(P_v\);
- retain the color at each chosen \(P_v\).

There are \(m-k\) color changes. This number is even, because
\[
m=\sum_{v\in V(G)}r(v)
\]
and exactly the \(k\) vertices in \(B\) have \(r(v)\) odd. Thus the rules give a consistent coloring around the entire cyclic tour.

Consider the color degrees at a vertex.

If \(v\notin B\), every visit pairs one red edge with one blue edge. Consequently,
\[
d_R(v)=d_B(v)=r(v),
\]
which is even.

If \(v\in B\), all but one visit pair different colors. If the chosen transition has two red edges, then
\[
d_R(v)=r(v)+1,\qquad d_B(v)=r(v)-1;
\]
if it has two blue edges, these quantities are interchanged. Both are again even.

Therefore the red and blue spanning subgraphs are even graphs. Decompose each into vertex-simple cycles.

Every resulting cycle is monochromatic. Every forbidden transition outside the chosen set has differently colored edges, so its two edges cannot lie in the same resulting cycle. This proves the proposition. \(\square\)

### Corollary 1

If every vertex of \(G\) has degree divisible by four, then the conjecture holds for every Eulerian tour of \(G\).

Indeed, \(B=\varnothing\), and the proof simply alternates red and blue around \(W\). Both color classes have even degree at every vertex.

This covers not just \(4\)-regular graphs but arbitrary Eulerian graphs with degrees in
\[
\{4,8,12,\ldots\}.
\]

### The remaining obstruction in this construction

The proposition does **not** show that the chosen defects can always be removed.

For example, suppose a chosen equal-colored pair forms a two-edge cut in its monochromatic component. Every cycle containing one edge of this cut must contain the other, since a cycle crosses every cut an even number of times. Thus no cycle decomposition of that particular color class can separate the pair.

So the parity construction gives a controlled bound, not a proof of compatibility.

## 2. Reduction to degrees \(4\) and \(6\)

The useful operation is to split vertices while keeping every tour transition intact.

### Lemma 2: Transition-preserving splitting

At each vertex \(v\), partition its \(r(v)\) tour visits into groups. Replace \(v\) by one new vertex for each group, attaching an edge-end to the new vertex containing its corresponding visit.

Let the resulting graph be \(G'\). Then:

1. the same cyclic edge sequence defines an Eulerian tour \(W'\) of \(G'\);
2. if \((G',W')\) has a compatible cycle decomposition, then so does \((G,W)\).

### Proof

At every visit of \(W\), the arrival and departure edges are attached to the same new vertex. Hence the original cyclic edge sequence remains a closed walk using every edge exactly once. In particular, \(G'\) is connected.

Now suppose \(\mathcal D'\) is a compatible cycle decomposition of \(G'\).

Take \(C'\in\mathcal D'\), and identify the split vertices back to their original vertices. Its edge set becomes an even subgraph \(H_{C'}\) of \(G\): the degree at an original vertex is the sum of the degrees contributed by its split copies, each contribution being zero or two.

Moreover, \(E(C')\), viewed as a set of original edges, contains no forbidden transition of \(W\). Every original forbidden transition was preserved as a transition of \(W'\), and compatibility of \(C'\) excludes both of its edges.

Decompose \(H_{C'}\) into simple cycles. Each resulting cycle uses a subset of \(E(C')\), so it still contains no forbidden transition.

Doing this separately for every \(C'\in\mathcal D'\) gives the required decomposition of \(G\). \(\square\)

The edge-set argument is important: projecting \(C'\) can produce a closed trail with repeated vertices, but it cannot introduce a forbidden pair into its edge set.

### Proposition 2

To prove the conjecture in full, it suffices to prove it for graphs whose degrees belong to \(\{4,6\}\).

Furthermore, the reduction produces exactly one degree-\(6\) vertex for each original vertex of degree \(2\bmod4\).

### Proof

Since \(d(v)\ge4\), we have \(r(v)\ge2\).

- If \(r(v)\) is even, partition its visits into groups of size two.
- If \(r(v)\) is odd, then \(r(v)\ge3\); use one group of size three and partition the remaining visits into groups of size two.

Apply transition-preserving splitting. A group of two visits produces a degree-\(4\) vertex, and a group of three produces a degree-\(6\) vertex. There is exactly one degree-\(6\) vertex for each original odd \(r(v)\).

Lemma 2 transfers a compatible decomposition back to the original graph. \(\square\)

For simple input graphs, splitting creates neither loops nor parallel edges. Thus this is also a reduction within the simple-graph formulation.

## 3. A stronger result for regular bipartite graphs

Here the prescribed transitions need not arise from a single Eulerian tour.

### Theorem 3

Let \(G\) be a bipartite \(2r\)-regular graph, where \(r\ge2\). At every vertex, prescribe an arbitrary partition of its incident edges into \(r\) pairs.

Then \(G\) has an edge partition
\[
E(G)=E(F_1)\,\dot\cup\cdots\dot\cup\,E(F_r)
\]
such that:

- every \(F_i\) is a spanning \(2\)-factor;
- the two edges of every prescribed pair belong to different factors.

Consequently, the cycles of these factors give a compatible cycle decomposition for every prescribed Eulerian tour.

### Proof

We construct an auxiliary \(r\)-regular bipartite graph \(H\).

For every \(v\in V(G)\), create \(r\) **port vertices**
\[
x_{v,1},\ldots,x_{v,r},
\]
one for each prescribed pair at \(v\). Attach the two original edge-ends in the \(i\)-th pair to \(x_{v,i}\). Thus each port is incident with exactly two original edges.

Also create \(r-2\) additional vertices
\[
y_{v,1},\ldots,y_{v,r-2},
\]
and add all edges between the \(r\) ports and these \(r-2\) additional vertices. For \(r=2\), there are no additional vertices or internal edges.

Every port now has degree
\[
2+(r-2)=r,
\]
and every additional vertex has degree \(r\). Hence \(H\) is \(r\)-regular.

Let \((A,B)\) be the bipartition of \(G\). Place:

- ports belonging to vertices of \(A\), and additional vertices belonging to vertices of \(B\), on one side;
- all remaining vertices on the other side.

Both original and internal edges cross this bipartition. Thus \(H\) is bipartite.

An \(r\)-regular bipartite graph has a proper edge-coloring with \(r\) colors. For completeness, for every subset \(S\) of one part,
\[
r|S|\le r|N(S)|,
\]
so Hall’s condition gives a perfect matching. Removing it and repeating partitions the edges into \(r\) perfect matchings.

Fix such an edge-coloring of \(H\), and restrict it to the original edges of \(G\).

Fix an original vertex \(v\) and a color \(i\). Across its \(r\) ports, color \(i\) occurs exactly \(r\) times, once at each port. Exactly \(r-2\) of these occurrences are on internal edges: each of the \(r-2\) additional vertices is incident with precisely one edge of color \(i\). Therefore exactly
\[
r-(r-2)=2
\]
original edges incident with \(v\) have color \(i\).

Thus every color class restricts to a spanning \(2\)-factor of \(G\).

Finally, the two edges of a prescribed pair meet at a common port in \(H\). Proper edge-coloring gives them different colors. Hence they belong to different factors. \(\square\)

### Corollary 3

Let \(G\) be bipartite and Eulerian. Suppose there is a fixed integer \(r\ge2\) such that
\[
2r\mid d(v)\qquad\text{for every }v\in V(G).
\]
Then the conjecture holds for \(G\).

### Proof

Write \(d(v)=2r q_v\). Partition the tour visits at \(v\) into \(q_v\) groups of size \(r\), and perform transition-preserving splitting.

The resulting graph is bipartite and \(2r\)-regular. Apply Theorem 3 and then Lemma 2. \(\square\)

In particular, **every regular Eulerian bipartite graph of degree at least four is covered**. The corollary also covers nonregular degree sets such as \(\{6,12,18,\ldots\}\).

## 4. Why these arguments do not settle the conjecture

The reduction leaves the general degree-\(\{4,6\}\) case. Proposition 1 then leaves at most one potentially violated transition at each degree-\(6\) vertex. The missing step is a method that eliminates all these defects simultaneously.

There is also a concrete reason not to discard the requirement that the forbidden transitions come from one Eulerian tour.

### An obstruction for arbitrary transition pairings

Partition \(K_5\) into the two \(5\)-cycles
\[
P=(0,1,2,3,4,0),\qquad
Q=(0,2,4,1,3,0).
\]
At each vertex, declare its two \(P\)-edges to be one forbidden pair and its two \(Q\)-edges to be the other.

Any compatible simple cycle would have to alternate between \(P\)-edges and \(Q\)-edges. It would therefore have even length. In \(K_5\), every even simple cycle has length four. But ten edges cannot be partitioned into \(4\)-cycles.

Thus arbitrary transition pairings need not admit a compatible cycle decomposition—even in a \(4\)-regular simple graph.

This is **not** a counterexample to the conjecture: these pairings describe two separate tour circuits, \(P\) and \(Q\), rather than one Eulerian tour. It shows why a proof must exploit the single-tour hypothesis, rather than only the local forbidden-pair structure.

Accordingly, the results above are constructive partial results, not a resolution of Sabidussi’s conjecture.