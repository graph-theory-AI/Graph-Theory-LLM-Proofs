```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every K_{a,b} with even a,b at least four, even for arbitrary forbidden transition pairings.",
  "would_publish": false,
  "caveats": "No general resolution; novelty and current literature status are unverified."
}
```

# Partial results: all even bicliques and a degree-six normal form

I work with finite undirected simple graphs. Cycles are vertex-simple, and Eulerian tours are regarded cyclically.

At each vertex \(v\), the prescribed tour partitions the incident edges into pairs. Write \(\mathcal F_v\) for this set of **forbidden pairs**. A cycle decomposition is compatible if no cycle contains both edges of any pair in any \(\mathcal F_v\).

For the principal special case below, the forbidden pairings need not come from one Eulerian tour.

I rechecked the regular-bipartite factorization and transition-preserving splitting arguments in the previous attempt; both are valid and are reproved below as needed. The new steps are:

* a peeling argument that removes the common-divisor restriction for complete bipartite graphs;
* an extension to independent even blow-ups of arbitrary graphs;
* a construction transforming any simple counterexample into a simple \(6\)-regular counterexample.

## 1. Main special-case theorem

### Theorem 1

Let \(a,b\ge 4\) be even integers. At every vertex of \(K_{a,b}\), prescribe an arbitrary partition of its incident edges into pairs.

Then \(K_{a,b}\) has a cycle decomposition containing no forbidden pair.

Moreover, if \(a\le b\), the construction produces a subgraph \(K_{a,a}\) such that:

* all edges outside this subgraph are decomposed into
  \[
  \frac{a(b-a)}4
  \]
  compatible \(4\)-cycles;
* the remaining \(K_{a,a}\) has a compatible decomposition into the cycles of \(a/2\) spanning \(2\)-factors.

Thus the original conjecture holds for every Eulerian complete bipartite graph of minimum degree at least four, including cases such as \(K_{4,6}\) that are not covered by the common-divisor condition in the previous attempt.

We first establish two lemmas.

### Lemma 1: Avoiding two perfect matchings

Let \(X\) have even cardinality \(2r\ge4\), and let \(M_1,M_2\) be perfect matchings on \(X\). There is a perfect matching of the complete graph on \(X\) disjoint from \(M_1\cup M_2\).

#### Proof

The simple graph with edge set \(M_1\cup M_2\) consists of even alternating cycles and isolated matching edges. It therefore has a bipartition
\[
X=A\mathbin{\dot\cup}B,\qquad |A|=|B|=r.
\]

If \(r\) is even, take arbitrary perfect matchings within \(A\) and within \(B\). Their union avoids \(M_1\cup M_2\), whose edges all run between \(A\) and \(B\).

If \(r\) is odd, then \(r\ge3\). Choose \(x\in A\). At most two vertices of \(B\) are joined to \(x\) by \(M_1\cup M_2\), so there is \(y\in B\) with
\[
xy\notin M_1\cup M_2.
\]
Take \(xy\), together with arbitrary perfect matchings within the even sets \(A\setminus\{x\}\) and \(B\setminus\{y\}\). This again avoids \(M_1\cup M_2\). \(\square\)

### Lemma 2: Regular bipartite graphs

Let \(G\) be bipartite and \(2r\)-regular, where \(r\ge2\). For arbitrary forbidden pairings at its vertices, \(G\) has a partition into \(r\) spanning \(2\)-factors such that the edges of every forbidden pair belong to different factors.

#### Proof

Construct an auxiliary bipartite graph \(H\).

For each vertex \(v\) of \(G\):

1. Create \(r\) port vertices, one for each forbidden pair at \(v\).
2. Attach each original edge-end to the port corresponding to its forbidden pair. Thus every port is incident with two original edges.
3. Create \(r-2\) additional vertices, and join each of them to all \(r\) ports belonging to \(v\).

Every vertex of \(H\) has degree \(r\). It is bipartite: ports inherit the side of their original vertex, while the additional vertices are placed on the opposite side.

By Hall’s theorem, an \(r\)-regular bipartite graph has a perfect matching. Repeatedly removing perfect matchings gives a proper edge-coloring of \(H\) with \(r\) colors.

Fix an original vertex \(v\) and a color \(i\). Across the \(r\) ports belonging to \(v\), there are exactly \(r\) incidences of color \(i\). Exactly \(r-2\) of these belong to internal edges, because each additional vertex has precisely one incident edge of color \(i\). Consequently, exactly two original edges at \(v\) have color \(i\).

Each color class restricted to \(G\) is therefore a spanning \(2\)-factor. The two edges of a forbidden pair meet at a common port in \(H\), so they receive different colors. \(\square\)

### Proof of Theorem 1

By symmetry, assume \(a\le b\). We induct on \(b-a\).

If \(a=b\), Lemma 2 applies to \(K_{a,a}\).

Suppose \(b>a\), so \(b\ge a+2\). Write the bipartition as
\[
X\mathbin{\dot\cup}Y,\qquad |X|=a,\quad |Y|=b.
\]

Fix \(y\in Y\). For each \(x\in X\), the edge \(xy\) has exactly one mate in the forbidden pairing at \(x\), say \(xz_x\). Hence at most \(a\) vertices of \(Y\setminus\{y\}\) are excluded as possible choices of a second vertex \(z\).

But
\[
|Y\setminus\{y\}|=b-1\ge a+1.
\]
We can therefore choose \(z\ne y\) such that
\[
\{xy,xz\}\notin\mathcal F_x
\qquad\text{for every }x\in X. \tag{1}
\]

The forbidden pairings at \(y\) and \(z\) induce two perfect matchings \(M_y,M_z\) on \(X\). By Lemma 1, choose a perfect matching \(P\) on \(X\) avoiding both.

For each \(xx'\in P\), take the \(4\)-cycle
\[
x\,y\,x'\,z\,x.
\]

These cycles decompose all edges between \(X\) and \(\{y,z\}\). They are compatible:

* at \(x\) and \(x'\), compatibility follows from (1);
* at \(y\) and \(z\), it follows from \(xx'\notin M_y\cup M_z\).

Now delete \(y,z\), leaving \(K_{a,b-2}\). Restrict the original forbidden pairings to the remaining edges. At each vertex, this restriction is a partial matching on an even number of edges, so it can be completed to a perfect matching.

Apply the induction hypothesis to these completed pairings. The resulting decomposition avoids every original forbidden pair whose two edges remain in \(K_{a,b-2}\). Any forbidden pair split between the removed subgraph and the remaining graph automatically has its edges in different cycles.

Together with the newly constructed \(4\)-cycles, this gives the required decomposition.

The completion of the remaining pairings need not describe a single Eulerian tour. This is exactly why we prove the stronger arbitrary-pairing statement.

Each peeling step removes two vertices of \(Y\) and produces \(a/2\) four-cycles. There are \((b-a)/2\) steps, giving
\[
\frac{a}{2}\frac{b-a}{2}=\frac{a(b-a)}4
\]
designated four-cycles outside the final \(K_{a,a}\). \(\square\)

## 2. Extension beyond bipartite graphs

The arbitrary-pairing formulation has a useful closure property.

### Lemma 3: Closure under even edge partitions

Suppose
\[
E(G)=E(G_1)\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}E(G_t),
\]
where every \(G_i\) is even and admits a compatible cycle decomposition for every system of forbidden pairings.

Then \(G\) also admits a compatible cycle decomposition for every system of forbidden pairings.

#### Proof

Fix forbidden pairings on \(G\). Within each \(G_i\), retain every forbidden pair whose two edges both belong to \(G_i\). At each vertex this gives a partial matching on an even set of incident edges, so complete it to a perfect matching.

Apply the assumed property to each \(G_i\). A forbidden pair of \(G\) either lies entirely within one piece, where it is avoided, or has its edges in different pieces, hence in different cycles. \(\square\)

### Corollary 4: Independent even blow-ups

Let \(H\) be a connected simple graph with at least one edge. Replace each vertex \(v\) by an independent set \(S_v\) of even size at least four, and replace each edge \(uv\) by all edges between \(S_u\) and \(S_v\).

The resulting graph admits a compatible cycle decomposition for arbitrary forbidden pairings.

#### Proof

Its edges are partitioned by the complete bipartite graphs
\[
K_{|S_u|,|S_v|},\qquad uv\in E(H).
\]
Apply Theorem 1 and Lemma 3. \(\square\)

These graphs are connected and Eulerian, with minimum degree at least four. The corollary includes nonbipartite graphs. In particular:

> Every complete multipartite graph whose parts all have even size at least four satisfies the conjecture, even for arbitrary forbidden pairings.

## 3. Any simple counterexample yields a simple \(6\)-regular counterexample

The following strengthens the degree-\(\{4,6\}\) reduction from the previous attempt. It is a structural result about possible counterexamples, not a solution of the remaining regular case.

### Proposition 5

If the conjecture has a simple counterexample, then it has a simple \(6\)-regular counterexample.

More precisely, an instance \((G,W)\) with \(m\) edges can be transformed into a simple \(6\)-regular instance \((H,W_H)\) with at most \(12m\) edges such that a compatible decomposition of \((H,W_H)\) would give one of \((G,W)\).

### Step 1: Split vertices into degrees four and six

At a vertex \(v\), regard each arrival–departure pair of \(W\) as one visit. There are \(d(v)/2\ge2\) visits.

Partition these visits into groups of size two and three:

* if the number of visits is even, use only groups of size two;
* if it is odd, use one group of size three and groups of size two for the remainder.

Replace \(v\) by one vertex for each group, attaching the edge-ends of each visit to its group vertex. Let the resulting graph be \(G_1\).

The same cyclic edge sequence is an Eulerian tour \(W_1\): every original transition was kept intact. Thus \(G_1\) is connected, remains simple, and has only degrees four and six.

Suppose \((G_1,W_1)\) has a compatible cycle decomposition. Project one of its cycles back to \(G\). Its edge set becomes an even subgraph, although it need not remain a vertex-simple cycle.

Crucially, that edge set contains no forbidden pair of \(W\), since every such pair was preserved as a forbidden pair of \(W_1\). Decompose the projected even subgraph into simple cycles. Taking subsets of its edge set cannot introduce a forbidden pair.

Doing this for every cycle transfers a compatible decomposition from \(G_1\) to \(G\).

### Step 2: Pad each degree-four vertex to degree six

Let \(v\) be a degree-four vertex of \(G_1\), with forbidden pairs
\[
\{a,b\},\qquad \{c,d\}.
\]

Take a fresh copy of \(K_7\), select an edge \(xy\), delete \(xy\), and add the two edges \(vx,vy\).

Every fresh vertex now has degree six:

* \(x,y\) had degree five after deletion and each receives one new edge;
* the other five vertices retain degree six.

The degree of \(v\) also becomes six. Call the attached subgraph, including \(v\), a balloon.

The graph \(K_7-xy\) has an Eulerian trail from \(x\) to \(y\). Consequently, the balloon has an Eulerian excursion starting and ending at \(v\). Insert this excursion into \(W_1\) between the consecutive edges \(a,b\).

Thus the forbidden pair \(\{a,b\}\) is broken in the new tour, while \(\{c,d\}\) remains consecutive.

Do this independently at every degree-four vertex. The resulting graph \(H\) is simple, connected, and \(6\)-regular, with the explicitly constructed Eulerian tour \(W_H\).

### Why a compatible decomposition transfers back

Every balloon meets the rest of the graph only at its attachment vertex. A simple cycle therefore cannot contain both a balloon edge and an original edge of \(G_1\).

Hence a cycle decomposition of \(H\), restricted to the original edges, gives a cycle decomposition of \(G_1\).

At an original degree-six vertex, all forbidden pairs were preserved. At a padded degree-four vertex, the pair \(\{c,d\}\) was preserved and is therefore avoided.

The other original pair \(\{a,b\}\) must also be avoided. Indeed, if one cycle in the restricted decomposition used \(a,b\), then the only remaining original edges at \(v\) would be \(c,d\). They would necessarily occur together in another cycle, contradicting compatibility with the preserved pair \(\{c,d\}\).

Thus the restricted decomposition is compatible with \(W_1\), and Step 1 transfers it to \((G,W)\).

### Size bound

Splitting does not change the number \(m\) of edges. If \(G_1\) has \(n_4\) degree-four vertices and \(n_6\) degree-six vertices, then
\[
m=2n_4+3n_6,
\]
so \(n_4\le m/2\).

Each balloon adds
\[
|E(K_7)|-1+2=22
\]
edges. Therefore
\[
|E(H)|=m+22n_4\le12m.
\]
This proves Proposition 5. \(\square\)

## 4. What remains unresolved

These arguments do not prove or disprove the general conjecture.

The biclique theorem is a complete special-case result: it covers all even part sizes at least four, not merely regular bicliques or part sizes with a common divisor greater than two. Its extension requires an edge partition into suitable even pieces; an arbitrary Eulerian graph need not have such a partition.

The degree-six construction only restricts the form of a possible counterexample. It does not provide a compatible decomposition for an arbitrary \(6\)-regular graph. In particular, its \(K_7-xy\) balloons contain triangles, so the resulting instance is not generally bipartite and Lemma 2 cannot finish the argument.

No computational enumeration or unverified literature assertion is used here. The partial theorems above have complete proofs, but I do not claim their novelty or a resolution of the conjecture’s current literature status.