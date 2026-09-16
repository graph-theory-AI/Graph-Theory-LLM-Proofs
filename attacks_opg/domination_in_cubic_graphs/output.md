```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the stronger floor(n/3) bound for bridgeless cubic graphs having a dominating family of vertex-disjoint triangles.",
  "would_publish": false,
  "caveats": "Special case only; novelty is not established, and triangle-free graphs are not covered."
}
```

## A partial result

I do not obtain a proof or counterexample for the full conjecture. The following is a self-contained special case. Its novelty would need a literature check.

All graphs below are finite and simple. A family of triangles is **dominating** if every vertex outside their union has a neighbor in that union.

**Theorem.** Let \(G\) be a connected bridgeless cubic graph. If \(G\) has a dominating family of vertex-disjoint triangles, then
\[
\gamma(G)\le \left\lfloor\frac{|V(G)|}{3}\right\rfloor .
\]

Thus the desired inequality holds, with a stronger rounding, for this class. There is no restriction on the number of triangles or on the number and lengths of the components outside them.

### Proof

Let \(\mathcal T\) be such a family, let \(t=|\mathcal T|\), and put
\[
R=G-\bigcup_{T\in\mathcal T}V(T).
\]
Because the triangles dominate \(G\), every vertex of \(R\) has a neighbor in a triangle. Hence
\[
\Delta(R)\le 2.
\]
The components of \(R\) are therefore paths, including isolated vertices, and cycles.

Each triangle has exactly three edges leaving it. We will select exactly one vertex from each triangle. Such a selection dominates the whole triangle and can also dominate one prescribed vertex of \(R\).

For the components of \(R\), define
\[
a=\#\{C:|V(C)|\equiv1\pmod3\},\qquad
b=\#\{C:|V(C)|\equiv2\pmod3\},
\]
and
\[
K=\sum_{C\text{ component of }R}\left\lfloor\frac{|V(C)|}{3}\right\rfloor.
\]
Consequently,
\[
|V(G)|=3t+3K+a+2b. \tag{1}
\]

The issue is to eliminate enough of the rounding costs in the usual path and cycle domination bound.

### 1. Local domination patterns

A path or cycle on \(m\) vertices has a dominating set of size at most \(\lceil m/3\rceil\). We use the following more specific patterns.

**Components of order \(3k+1\).**

- For a cycle, deleting any one vertex leaves a path on \(3k\) vertices, which can be dominated by \(k\) vertices.
- For a path
  \[
  v_1v_2\cdots v_{3k+1},
  \]
  deleting any vertex \(v_{3j+1}\), \(0\le j\le k\), leaves two paths whose orders are divisible by three. Together they can be dominated by \(k\) vertices.

Call these possible deleted vertices **eligible holes**. Thus such a component can be handled using \(k\) vertices internally if an eligible hole is dominated from a triangle.

**Components of order \(3k+2\).**

- In a cycle, deleting any two adjacent vertices leaves a path on \(3k\) vertices.
- In a path, any of the following pairs can be deleted:
  \[
  \{v_1,v_{3k+2}\},\qquad
  \{v_1,v_2\},\qquad
  \{v_{3k+1},v_{3k+2}\}.
  \]
  In each case the remaining graph is a path on \(3k\) vertices.

Call these **admissible pairs**. If both vertices of an admissible pair are dominated from triangles, only \(k\) internal vertices are needed.

Empty paths cause no difficulty in these statements.

### 2. Handle every \(1\bmod3\) component

Construct a bipartite incidence multigraph with:

- the \(a\) components of order \(1\bmod3\) on the left;
- the triangles of \(\mathcal T\) on the right;
- one incidence for each edge of \(G\) joining an eligible hole to a triangle.

Every left vertex has at least three incidences:

- an isolated vertex of \(R\) has three edges to triangles;
- a path on \(3k+1\) vertices, \(k\ge1\), has two eligible endpoints, each with two edges to triangles, and \(k-1\) eligible internal vertices, each with one;
- a cycle of order \(1\bmod3\) has at least four vertices, all eligible, each with one edge to a triangle.

Every right vertex has at most three incidences, since a triangle has only three outgoing edges.

For any set \(\mathcal X\) of left vertices, counting incidences gives
\[
3|\mathcal X|\le 3|N(\mathcal X)|.
\]
Hall’s theorem therefore gives a matching saturating all left vertices.

For each matched component, reserve its matched triangle to dominate the eligible hole at the matched edge. This uses \(a\) distinct triangles and lets us dominate each \(1\bmod3\) component internally with its floor bound.

Call these triangles **used**.

### 3. Greedily reduce some \(2\bmod3\) components

Repeatedly perform the following operation whenever possible:

- take a previously untreated component of order \(2\bmod3\);
- find an admissible pair whose two vertices have neighbors in two distinct unused triangles;
- reserve those triangles to dominate the pair.

Each operation uses two additional triangles and saves one internal dominating vertex.

Continue until no such operation is possible. Let \(s\) be the number of components treated this way. There are now
\[
a+2s
\]
used triangles and \(b-s\) untreated \(2\bmod3\) components.

An edge from \(R\) to a used triangle will be called **blocked**.

We need the following claim.

**Claim.** Every untreated \(2\bmod3\) component has at least two blocked edges.

#### Cycle case

Let \(C\) be such a cycle, and suppose it has at most one blocked edge. Every vertex of \(C\) has exactly one edge to a triangle.

Delete the vertex incident with the blocked edge, if one exists. The remaining vertices form a connected path or cycle on at least four vertices, and all their triangle neighbors lie in unused triangles.

If two consecutive remaining vertices have neighbors in distinct triangles, they form an admissible pair, contradicting termination. Otherwise, connectedness forces all remaining vertices to have neighbors in the same triangle. That would require at least four outgoing edges from that triangle, which is impossible.

#### Path case

Let
\[
P=v_1v_2\cdots v_m,\qquad m\equiv2\pmod3,
\]
and again suppose there is at most one blocked edge.

Each endpoint has two edges to triangles. Among these four endpoint edges, at least three go to unused triangles, and each endpoint has at least one such edge.

If the two endpoints can be assigned distinct unused triangles, the endpoint pair is admissible and we could perform another operation. Hence all unused endpoint edges must go to one unused triangle \(A\).

Since \(A\) has only three outgoing edges, exactly three endpoint edges go to \(A\), and the fourth endpoint edge is blocked. Reverse the path if necessary so that this blocked edge is incident with \(v_1\). Thus \(v_1\) has one edge to \(A\), while \(v_m\) has two.

If \(m\ge5\), the internal vertex \(v_2\) has one edge to a triangle \(B\). This edge is unblocked, because the only blocked edge of the component is already at \(v_1\). Also \(B\ne A\), since all three outgoing edges of \(A\) are accounted for at the endpoints. Therefore \(\{v_1,v_2\}\) can be assigned the two distinct unused triangles \(A,B\), again contradicting termination.

It remains to consider \(m=2\). In that case the set
\[
V(A)\cup\{v_1,v_2\}
\]
has exactly one outgoing edge: the blocked endpoint edge. That edge is a bridge, contrary to the hypothesis.

This proves the claim. Notice that the last case is the only place where bridgelessness is used. \(\square\)

### 4. Count the savings

Each used triangle has one outgoing edge reserved for a hole in an already treated component. It therefore has at most two edges to untreated \(2\bmod3\) components.

The claim consequently gives
\[
2(b-s)\le 2(a+2s),
\]
or equivalently,
\[
b\le a+3s. \tag{2}
\]

Now construct the dominating set:

- in each used triangle, choose the vertex prescribed by its reserved edge;
- in each unused triangle, choose any vertex;
- use the floor-size internal sets in all \(1\bmod3\) components and in the \(s\) treated \(2\bmod3\) components;
- use an ordinary \(\lceil |C|/3\rceil\)-vertex dominating set in every remaining component.

Every triangle is dominated. Every designated hole is dominated by its reserved triangle, and all other vertices of \(R\) are dominated internally.

The resulting set \(D\) satisfies
\[
|D|\le t+K+b-s.
\]
Using (1) and (2),
\[
\begin{aligned}
|V(G)|-3(t+K+b-s)
 &=a-b+3s\\
 &\ge0.
\end{aligned}
\]
Thus
\[
\gamma(G)\le |D|\le \frac{|V(G)|}{3},
\]
and integrality gives the asserted floor bound. \(\square\)

## A formulation directly for 3-connected cubic graphs

**Corollary.** Let \(G\) be a 3-connected cubic graph. If every vertex lies in a triangle or has a neighbor lying in a triangle, then
\[
\gamma(G)\le \left\lfloor\frac{|V(G)|}{3}\right\rfloor.
\]

**Proof.** First, in a 3-connected cubic graph other than \(K_4\), distinct triangles are vertex-disjoint.

Indeed, two triangles meeting at a vertex must share an edge, since that vertex has degree three. Write them as \(abc\) and \(abd\). If \(cd\) is an edge, these four vertices form a \(K_4\) component, so connectedness gives \(G=K_4\). Otherwise, deleting \(c,d\) separates \(a,b\) from the rest of the graph, contradicting 3-connectivity.

For \(G\ne K_4\), take all its triangles. They are vertex-disjoint and, by the hypothesis, dominating. Since \(G\) is bridgeless, the theorem applies. For \(K_4\), the conclusion is \(\gamma(K_4)=1\). \(\square\)

## What this does—and does not—settle

The proof is constructive: given the triangle family, it uses a bipartite matching, a finite greedy procedure, and explicit path/cycle dominating sets. It therefore also gives a polynomial-time construction of the promised dominating set.

The missing hypothesis is substantial. Three-connectivity does **not** ensure a dominating triangle family; in particular, triangle-free cubic graphs are completely outside this argument. More generally, a vertex having no neighbor in the chosen triangles has degree three in \(R\), so the path/cycle decomposition on which the proof depends disappears.

Accordingly, this proves a triangle-rich special case, not the original conjecture. No counterexample to the original statement is obtained.