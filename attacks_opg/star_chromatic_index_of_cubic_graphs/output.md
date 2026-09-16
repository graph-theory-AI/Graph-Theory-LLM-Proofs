```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp six-colour bound is proved for simple cubic graphs having a 2-factor consisting of 3-, 5-, and 6-cycles, but the general conjecture is not resolved.",
  "would_publish": false,
  "caveats": "No novelty claim is made; the required short-cycle 2-factor need not exist."
}
```

## A restricted six-colouring theorem

I do not obtain a proof or a counterexample for arbitrary subcubic graphs. I can prove the following constructive sufficient condition.

**Theorem.** Let \(G\) be a finite simple cubic graph. If \(G\) has a spanning \(2\)-factor whose cycles all have lengths in
\[
\{3,5,6\},
\]
then
\[
\chi_s'(G)\le 6.
\]
The bound is sharp within this class.

In particular, this covers every graph obtained by replacing each vertex of a cubic graph by a triangle, with its three incident edges attached to distinct vertices of that triangle. It also applies to subgraphs of the cubic graphs covered by the theorem.

The only standard external ingredient in the proof is Brooks’s vertex-colouring theorem.

## 1. Protecting the matching edges

Let \(M\) be a perfect matching of a cubic graph \(G\), and put
\[
F=G-M.
\]
Thus \(F\) is a spanning union of cycles. Use the palettes
\[
A=\{1,2,3,4\},\qquad B=\{5,6\}.
\]

Suppose the edges of \(M\) have been assigned colours in \(A\). For each vertex \(v\), let \(\ell(v)\) denote the colour of its incident matching edge. Assume that
\[
\ell(x)\ne \ell(y)\qquad\text{for every }xy\in E(F). \tag{1}
\]

For \(e=xy\in E(F)\), define
\[
X(e)=\{x,y\}\cup N_F(x)\cup N_F(y).
\]
Call a colour \(a\in A\) **available at \(e\)** if
\[
a\notin \{\ell(z):z\in X(e)\}. \tag{2}
\]

**Matching-protection lemma.** Suppose \(F\) has a star edge-colouring with colours in \(A\cup B\), and every use of a colour from \(A\) satisfies (2). Together with the prescribed colouring of \(M\), this is a star edge-colouring of \(G\).

**Proof.** The combined colouring is proper: condition (2) excludes the colours of the matching edges incident with either endpoint of an \(F\)-edge.

Moreover, no matching edge has another edge of its colour at distance at most two in the line graph:

- Two matching edges at distance two are joined by an \(F\)-edge, so their colours differ by (1).
- If an \(F\)-edge \(e\) is at distance at most two from a matching edge \(m\), then an endpoint of \(m\) belongs to \(X(e)\). Consequently, (2) excludes the colour of \(m\) from \(e\).

In any properly bichromatic four-edge path or cycle, each edge has another edge of its colour two positions away. Such a configuration therefore cannot contain a matching edge. Nor can it lie entirely in \(F\), whose colouring is a star edge-colouring. \(\square\)

The advantage is that, once the matching colours are chosen, the cycles of \(F\) can be coloured independently.

## 2. A local cycle-colouring lemma

For this section, neighbourhoods in the definition of \(X(e)\) are taken within the cycle under consideration.

**Cycle lemma.** Let \(C\) be a cycle of length \(3\), \(5\), or \(6\), with a proper vertex-labelling
\[
\ell:V(C)\longrightarrow A.
\]
Then \(C\) has a star edge-colouring with colours in \(A\cup B\) such that every colour from \(A\) is used only where it is available.

All edge-colour sequences below are written in cyclic order.

### A triangle

The three vertex labels are distinct. Choose \(p\in A\) absent from the triangle and colour its edges
\[
p,5,6.
\]
This satisfies all requirements.

### A 5-cycle

If a label \(p\) occurs at a unique vertex \(v\), then \(p\) is available at the edge opposite \(v\): the set \(X(e)\) for that edge consists of precisely the other four vertices.

A proper labelling of \(C_5\) uses either three or four labels.

- If it uses three, their multiplicities are \(2,2,1\). Let \(p\) be the uniquely occurring label, and let \(q\in A\) be the unused label. Use \(p\) on the edge opposite its vertex, and \(q\) on an adjacent edge.
- If it uses four, three labels occur uniquely. Their three opposite edges contain two adjacent edges, since a matching in \(C_5\) has at most two edges. Choose those two edges and use their corresponding, distinct available labels \(p,q\).

In either case, complete the edge-colouring in cyclic order as
\[
p,q,5,6,5.
\]
It is proper, and any four cyclically consecutive edges have at least three colours.

### A 6-cycle

Write its vertices as \(v_0,\ldots,v_5\), and let
\[
e_i=v_iv_{i+1},
\]
with indices modulo \(6\). Call an edge available if at least one colour in \(A\) is available there.

First observe that **two opposite available edges suffice**. Choose available colours \(p,q\) on them and use
\[
p,5,6,q,5,6.
\]
This is a star edge-colouring even if \(p=q\).

If at most three vertex labels are used, every edge is available. If four labels are used, their multiplicities are either
\[
3,1,1,1\quad\text{or}\quad 2,2,1,1.
\]

In the first case, the label occurring three times occupies alternating vertices. Every four consecutive vertices therefore contain a repeated label, so again every edge is available.

Consider the second case, with repeated labels \(a,b\).

- If a repeated label occurs at opposite vertices, say \(v_0,v_3\), then \(e_1,e_4\) are opposite available edges.
- Otherwise, both repeated pairs have cyclic distance two. Normalize the \(a\)-vertices to \(v_0,v_2\). The \(b\)-vertices can then be
  \[
  \{v_1,v_3\},\quad \{v_1,v_5\},\quad\text{or}\quad \{v_3,v_5\}.
  \]
  The last possibility makes \(e_0,e_3\) opposite available edges.

The first two remaining possibilities are equivalent by reflection. After renaming the two unique labels, their cyclic vertex-label sequence is
\[
a,b,a,c,d,b.
\]
Use the edge-colour sequence
\[
6,d,5,6,5,c. \tag{3}
\]
Here \(d\) is available at \(e_1\), because \(X(e_1)\) has labels \(a,b,a,c\); and \(c\) is available at \(e_5\), because \(X(e_5)\) has labels \(d,b,a,b\). The other edges use \(B\).

Sequence (3) is proper, and each of its six cyclic blocks of four entries has at least three colours. This completes every case of the cycle lemma. \(\square\)

## 3. Proof of the theorem

It suffices to treat connected \(G\). Let \(F\) be the assumed \(2\)-factor and let
\[
M=E(G)\setminus E(F).
\]
Since \(G\) is cubic, \(M\) is a perfect matching.

Contract every edge of \(M\), retaining parallel edges, to obtain a multigraph \(Q\). Because \(G\) is simple, \(Q\) has no loops. Each contracted vertex has degree four, counting multiplicity. Thus the underlying simple graph of \(Q\) is connected and has maximum degree at most four.

By Brooks’s theorem, this underlying graph has a proper vertex-colouring with \(A\), unless it is \(K_5\).

### The ordinary case: \(Q\) is 4-colourable

Give each matching edge the colour of its corresponding vertex in \(Q\). Let \(\ell(v)\) be the resulting matching-edge label at \(v\).

Every \(F\)-edge becomes an edge of \(Q\), so its endpoint labels differ. Thus (1) holds. Apply the cycle lemma independently to every component of \(F\), and then apply the matching-protection lemma. This gives a star edge-colouring of \(G\) with six colours.

### The exceptional case: the underlying graph of \(Q\) is \(K_5\)

Since \(Q\) is 4-regular counting multiplicity, it must actually be the simple graph \(K_5\). In particular, \(G\) has ten vertices.

The only way to partition ten vertices into cycles of lengths \(3,5,6\) is
\[
10=5+5.
\]
Hence \(F\) consists of two 5-cycles.

No matching edge can have both endpoints on one of these cycles. Such an edge would be a chord of a 5-cycle, whose endpoints have a common cycle neighbour. Contracting the chord would produce parallel edges in \(Q\), a contradiction. Thus all matching edges join the two cycles.

Label the first cycle
\[
u_0u_1u_2u_3u_4u_0,
\]
and denote the matching partner of \(u_i\) by \(v_i\), with indices modulo \(5\). Because the quotient is \(K_5\), the second cycle has edges
\[
v_iv_{i+2}\qquad(i\in\mathbb Z_5).
\]

Colour every matching edge with \(6\). For an \(F\)-edge whose endpoint indices are \(i,j\), use
\[
c(ij)=1+\bigl((i+j)\bmod 5\bigr). \tag{4}
\]

Formula (4) is a proper five-edge-colouring of the quotient \(K_5\): at a fixed vertex \(i\), distinct neighbours give distinct sums. Also, each of the two \(F\)-cycles is rainbow, since its edge sums are respectively
\[
2i+1\quad\text{and}\quad 2i+2 \pmod 5.
\]

A forbidden bichromatic four-edge path or cycle cannot lie entirely in \(F\). If it contains a matching edge, its two colours must be \(6\) and some \(a\in\{1,\ldots,5\}\). Its two \(F\)-edges of colour \(a\) are separated by a matching edge. Those two edges become incident in \(Q\), contradicting the proper edge-colouring (4).

So the exceptional case also admits six colours. Colouring connected components separately proves the theorem. \(\square\)

## 4. Sharpness within the class

The graph \(K_{3,3}\) has a spanning 6-cycle, so the theorem gives its six-colour upper bound. For completeness, here is a short proof that five colours are impossible.

Suppose \(K_{3,3}\) had a star edge-colouring using at most five colours. Every colour class is a matching.

If some colour class had three edges, it would be a perfect matching. Its union with any two edges of another colour contains either a 4-cycle or a five-edge alternating path. Both violate the star condition. Thus all other colour classes would have size at most one, giving at most
\[
3+4=7
\]
edges, rather than nine.

Consequently, every colour class has size at most two. There must therefore be four colour classes of size two. Fix one side \(X\) of the bipartition. Each two-edge colour class omits exactly one of the three vertices of \(X\). Two such classes omit the same vertex.

Their union is a four-edge subgraph of \(K_{2,3}\), with degree two at both vertices on its two-vertex side and maximum degree two everywhere. It is therefore either a four-edge path or a 4-cycle. Again it is forbidden.

Hence
\[
\chi_s'(K_{3,3})=6,
\]
and the restricted theorem is sharp.

## 5. What remains unresolved

The argument does not produce the required \(2\)-factor in an arbitrary cubic graph. In particular, it says nothing about cubic graphs of girth at least seven.

There is also a concrete obstruction to extending the local construction indiscriminately. On a 4-cycle whose matching-edge labels are, cyclically,
\[
1,2,3,4,
\]
every set \(X(e)\) contains all four labels. No colour from \(A\) is available on any edge. Using only \(5,6\) would force a forbidden bichromatic 4-cycle.

That is an obstruction to this **matching-protection method**, not a counterexample to the conjecture: different matching colours, a different decomposition, or a colouring that does not protect every matching edge could overcome it.

Thus the six-colour theorem above is complete for its stated class, but the unrestricted six-versus-seven question remains unanswered by this argument.