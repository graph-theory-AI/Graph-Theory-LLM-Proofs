```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A matching-based sufficient condition gives six colours with arbitrarily long residual cycles, and every subcubic graph with a spanning 4-cycle factor admits a sharp five-colour bound.",
  "would_publish": false,
  "caveats": "These sufficient conditions are not universal; the original conjecture is unresolved here, and no novelty claim is made."
}
```

# A matching-based partial result

I do not obtain a proof or a counterexample for the unrestricted conjecture. I obtain two constructive sufficient conditions, including a five-colour theorem that bypasses the previous attempt’s obstruction on rainbow-labelled squares.

All graphs below are finite and simple. I reuse the previous attempt’s matching-protection idea, but prove the needed version independently. Its short-cycle lemma is not assumed.

## 1. Statements

For a matching \(M\) in \(G\), define its **conflict graph** \(H_M\) as follows:

- the vertices of \(H_M\) are the edges of \(M\);
- two distinct matching edges are adjacent when some edge of \(G\) joins an endpoint of one to an endpoint of the other.

Thus \(H_M\) records pairs of matching edges at distance two in the line graph. When \(M\) is perfect, \(H_M\) is the underlying simple graph of the multigraph obtained by contracting \(M\).

**Theorem 1.** Let \(G\) be subcubic, and let \(M\) be a matching covering every vertex of degree three. Put \(F=G-M\).

1. If \(H_M\) is 3-colourable, then
   \[
   \chi_s'(G)\le 6.
   \]
2. If \(H_M\) is bipartite and \(F\) has no component isomorphic to \(C_5\), then
   \[
   \chi_s'(G)\le 5.
   \]
   In particular, the five-colour conclusion holds whenever \(M\) is perfect and \(H_M\) is bipartite.

**Theorem 2.** If a subcubic graph \(G\) has a spanning union of vertex-disjoint 4-cycles, then
\[
\chi_s'(G)\le 5.
\]

Both numerical bounds are sharp within their respective classes: \(K_{3,3}\) witnesses six in Theorem 1, and \(K_4\) witnesses five in Theorem 2.

Theorem 1 does not restrict the lengths of the cycles of \(F\). For example, in the prism \(C_n\square K_2\), the matching of rungs has conflict graph \(C_n\), so the theorem applies for every \(n\ge3\).

## 2. Two elementary colouring lemmas

### 2.1 Paths and cycles

**Lemma 3.** Every path, and every cycle other than \(C_5\), has a star edge-colouring with three colours.

**Proof.** On a path, repeat the sequence \(1,2,3\).

Every integer \(n\ge3\), other than \(5\), can be written
\[
n=3a+4b
\]
with \(a,b\ge0\). Colour \(C_n\) by a cyclic concatenation of \(a\) copies of
\[
(1,2,3)
\]
and \(b\) copies of
\[
(1,2,1,3).
\]

The colouring is proper, including across block boundaries. In the resulting cyclic sequence, the gaps between successive occurrences of either colour \(2\) or colour \(3\) are three or four, while gaps between successive occurrences of colour \(1\) are at most three. Consequently every four consecutive entries contain all three colours. This excludes all forbidden paths and cycles. \(\square\)

We will colour \(C_5\) using the cyclic sequence
\[
p,4,5,4,6, \tag{1}
\]
where \(p\notin\{4,5,6\}\). This is proper and star: only one colour is repeated, whereas a bichromatic four-edge path or cycle would repeat both colours.

### 2.2 Protecting the matching

Suppose the matching edges have colours in a palette \(A\), and this is a proper vertex-colouring of \(H_M\). At every vertex \(v\) incident with \(M\), write \(\ell(v)\) for the colour of its matching edge. Leave \(\ell(v)\) undefined at unmatched vertices.

For \(e=xy\in E(F)\), put
\[
X_F(e)=\{x,y\}\cup N_F(x)\cup N_F(y).
\]
A colour \(p\in A\) is **available at \(e\)** if no vertex of \(X_F(e)\) has label \(p\).

**Lemma 4.** Suppose \(F\) has a star edge-colouring using \(A\) and a disjoint palette \(B\). If every colour from \(A\) used on an \(F\)-edge is available there, then the combined colouring of \(G\) is a star edge-colouring.

**Proof.** The combined colouring is proper: availability excludes the matching-edge colours at the endpoints of every \(F\)-edge.

Furthermore, no matching edge has another edge of its colour at distance at most two in the line graph.

- For two matching edges at distance two, the intervening edge gives an adjacency in \(H_M\), so their colours differ.
- If a matching edge \(m\) is at distance at most two from an \(F\)-edge \(e\), an endpoint of \(m\) belongs to \(X_F(e)\). Indeed, any intervening edge must belong to \(F\), because \(M\) is a matching. Availability therefore excludes the colour of \(m\) from \(e\).

In a properly bichromatic four-edge path or cycle, every edge has another edge of its colour two positions away. Such a configuration cannot contain an edge of \(M\). It cannot lie entirely in \(F\), either, because the colouring of \(F\) is star. \(\square\)

## 3. Proof of Theorem 1

Because \(M\) covers every vertex of degree three,
\[
\Delta(F)\le2.
\]
Thus every component of \(F\) is a path or a cycle.

### The six-colour assertion

Properly colour \(H_M\) with
\[
A=\{1,2,3\},
\]
and transfer these colours to the matching edges. Use
\[
B=\{4,5,6\}
\]
on the remaining graph.

By Lemma 3, every component of \(F\) other than a 5-cycle can be star edge-coloured entirely from \(B\).

Consider a 5-cycle \(C\) of \(F\). Among the three possible matching labels, some label \(p\) occurs at most once on its five vertices.

- If \(p\) does not occur, it is available at every edge of \(C\).
- If \(p\) occurs only at \(v\), let \(e\) be the edge opposite \(v\). Then
  \[
  X_F(e)=V(C)\setminus\{v\},
  \]
  so \(p\) is available at \(e\).

Starting at this edge \(e\), colour \(C\) cyclically by
\[
p,4,5,4,6.
\]
As noted above, this is a star edge-colouring. Its sole use of a matching colour is available.

Perform this construction independently on every 5-cycle. Lemma 4 now gives a star edge-colouring of \(G\) with six colours.

### The five-colour assertion

If \(H_M\) is bipartite, colour the matching edges with \(4,5\). If \(F\) has no 5-cycle component, Lemma 3 colours all of \(F\) with \(1,2,3\). Lemma 4 applies, with no borrowing of matching colours, and gives five colours.

Finally, suppose \(M\) is perfect and \(H_M\) is bipartite. Label each vertex of \(G\) by the colour of its matching edge. For every \(xy\in E(F)\), the two matching edges at \(x,y\) are distinct and adjacent in \(H_M\), so
\[
\ell(x)\ne\ell(y).
\]
These labels give a proper two-colouring of \(F\). Hence every cycle of \(F\) is even, and in particular no component is \(C_5\). This proves the final assertion. \(\square\)

## 4. A five-colouring from a 4-cycle factor

We now prove Theorem 2. The important point is that we **change the protected matching**, instead of retaining the complement of the given factor.

Let \(F_0\) be a spanning union of 4-cycles, and put
\[
M_0=E(G)\setminus E(F_0).
\]
Since \(G\) is subcubic, \(M_0\) is a matching, possibly not perfect.

For each square
\[
v_0v_1v_2v_3v_0
\]
of \(F_0\), introduce the two auxiliary diagonal edges
\[
v_0v_2,\qquad v_1v_3.
\]
Together these auxiliary edges form a perfect matching \(D\) on \(V(G)\).

Consider the auxiliary multigraph
\[
T=(V(G),M_0\sqcup D).
\]
If an edge belongs to both \(M_0\) and \(D\), retain two copies. Every component of \(T\) is a path or an even cycle: any cycle alternates between the two matchings. Therefore \(T\) has a proper vertex-colouring
\[
b:V(G)\longrightarrow\{0,1\}.
\]

On each square,
\[
b(v_2)=1-b(v_0),\qquad b(v_3)=1-b(v_1). \tag{2}
\]
Consequently every vertex has exactly one square-neighbour with the same bit and exactly one with the opposite bit. Indeed, its two square-neighbours are opposite vertices of that square, so their bits differ by (2).

Let
\[
S=\{xy\in E(F_0):b(x)=b(y)\}.
\]
It follows that \(S\) is a perfect matching. In each square, \(S\) consists of two opposite edges.

Moreover, **every edge outside \(S\) joins vertices with different bits**:

- this holds for \(F_0-S\) by definition;
- it holds for \(M_0\) because \(b\) properly colours \(T\).

Assign to each edge of \(S\) its common endpoint bit. This is a proper two-colouring of its conflict graph \(H_S\): an edge witnessing a conflict lies outside \(S\), and hence joins opposite bits.

Thus \(S\) is a perfect matching with bipartite conflict graph. Theorem 1 gives
\[
\chi_s'(G)\le5.
\]
This proves Theorem 2. \(\square\)

This construction bypasses the earlier rainbow-square obstruction. That obstruction concerned protecting a fixed complementary matching with four colours. Here a new matching is selected *inside* the squares, and only two colours are needed to protect it.

Given the 4-cycle factor, all steps above can be performed in linear time. Likewise, Theorem 1 is a linear-time construction once its matching and conflict-graph colouring are supplied.

## 5. Sharpness

### Five colours are necessary for \(K_4\)

The graph \(K_4\) has a spanning 4-cycle, so Theorem 2 gives five colours.

In any proper edge-colouring of \(K_4\), a colour class has at most two edges. Every two-edge colour class is a perfect matching. Two such classes together form a bichromatic 4-cycle, so a star edge-colouring can have at most one two-edge colour class.

Four colours could therefore cover at most
\[
2+1+1+1=5
\]
edges, fewer than the six edges of \(K_4\). Hence
\[
\chi_s'(K_4)=5.
\]

### Six colours are necessary for \(K_{3,3}\)

For any perfect matching \(M\) of \(K_{3,3}\), its conflict graph is \(K_3\). Theorem 1 therefore gives six colours.

Suppose there were a star edge-colouring using at most five colours.

If a colour class contained three edges, it would be a perfect matching. Its union with any two edges of another colour is either a five-edge alternating path or a 4-cycle together with a disjoint edge. Either contains a forbidden configuration. Thus every other colour class would have size at most one, covering at most
\[
3+4=7
\]
edges altogether.

Consequently every colour class has size at most two. To cover all nine edges with at most five colours, at least four colour classes must have size two.

Fix one side \(X\) of the bipartition. Each two-edge colour class omits exactly one vertex of \(X\). Two of the four classes omit the same vertex. Their union has four edges, maximum degree two, and degree two at both vertices of the remaining two-element subset of \(X\). It must be a four-edge path or a 4-cycle, again forbidden.

Therefore
\[
\chi_s'(K_{3,3})=6.
\]

## 6. Why this does not settle the conjecture

The missing hypothesis is genuinely restrictive, not merely an unproved existence statement that can safely be assumed.

For example, the Petersen graph has ten vertices and girth five. For **every** perfect matching \(M\), contracting \(M\) produces a 4-regular multigraph on five vertices. This quotient has:

- no loops, because the original graph is simple;
- no parallel edges, because two parallel quotient edges would lift to a triangle or a 4-cycle in the original graph.

Hence the quotient is \(K_5\), and
\[
H_M\cong K_5.
\]
Thus no choice of perfect matching makes Theorem 1 applicable to the Petersen graph. Since a matching covering all degree-three vertices of a cubic graph must be perfect, allowing the more general formulation of Theorem 1 does not help here.

This is an obstruction to the sufficient condition, **not** a counterexample to six-colourability. Other constructions are needed outside the stated classes.

Accordingly, the results above supply complete proofs for their hypotheses—including the sharp five-colour theorem for a 4-cycle factor—but leave the unrestricted six-versus-seven problem unanswered.