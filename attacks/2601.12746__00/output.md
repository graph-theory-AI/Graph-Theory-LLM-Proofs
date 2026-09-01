```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The catalog item is a schematic research programme rather than a quantified conjecture, since neither the connectivity class, the containment relation, nor the permitted obstruction type is specified.",
  "would_publish": false,
  "caveats": "Under the standard crossing-free definition, an exact dual criterion and a complete strongly connected 3-connected special case are proved below."
}
```

# Mathematical writeup

## 1. Status of the extracted question

Even granting the intended definition of a circular drawing, a forbidden-structure assertion would have to specify data of the form
\[
\forall G\in\mathcal K,\qquad
G\text{ is circular}\iff
\text{there is no }X\in\mathcal X\text{ with }X\preceq G,
\]
where:

1. \(\mathcal K\) is the connectivity class;
2. \(\preceq\) is a containment relation—subdigraph, induced subdigraph, subdivision, directed topological minor, immersion, butterfly minor, etc.;
3. \(\mathcal X\) is required to be a single configuration, a finite family, a recursively enumerable family, or something else.

None of these is specified. Different choices give materially different answers. In particular:

- If arbitrary infinite families of ordinary subdigraph obstructions are allowed, a characterization exists tautologically.
- Under the natural crossing-free definition, no finite family of ordinary subdigraph obstructions can characterize all circular digraphs; this is proved in Section 4.
- A finite topological-obstruction theorem, or a theorem restricted to strongly connected digraphs, is a different and potentially substantive question.

Thus the catalog item is not a proposition with a definite truth value. The remainder gives precise results under the natural interpretation suggested by the abstract.

---

## 2. A fixed-embedding characterization by the directed dual

### 2.1 Definitions

Assume that a drawing is crossing-free. Work on an oriented sphere. For a directed simple cycle \(C\), its image is a Jordan curve, and its two sides will be denoted by \(L(C)\) and \(R(C)\), according to the local left and right sides when traversing \(C\).

A plane embedding is circular if there are two points \(p_\infty,p_0\) in the complement of the drawing such that, for every directed cycle \(C\),
\[
p_\infty\in L(C),\qquad p_0\in R(C).
\]
Deleting \(p_\infty\) from the sphere and sending \(p_0\) to the origin gives the usual plane formulation: every directed cycle surrounds the origin clockwise.

Let \(D\) be a connected plane digraph. Define its left-to-right directed dual \(D^*\) as follows:

- the vertices of \(D^*\) are the faces of \(D\);
- for each directed edge \(e\) of \(D\), add a dual edge
  \[
  e^*:L(e)\longrightarrow R(e),
  \]
  where \(L(e)\) and \(R(e)\) are the faces locally on the left and right of \(e\).

A source strongly connected component of \(D^*\) is an SCC with no incoming edge from another SCC; a sink SCC is defined dually.

### 2.2 The criterion

**Proposition 2.1.**  
Let \(D\) be a connected plane digraph, and let \(a,b\) be faces. The following are equivalent.

1. For every directed cycle \(C\),
   \[
   a\subseteq L(C),\qquad b\subseteq R(C).
   \]
2. In \(D^*\), the SCC containing \(a\) is the unique source SCC, and the SCC containing \(b\) is the unique sink SCC.

Consequently, the fixed embedding of \(D\) is circular if and only if \(D^*\) has exactly one source SCC and exactly one sink SCC.

#### Proof

We use the standard circuit-bond duality for plane graphs.

If \(C\) is a directed cycle of \(D\), then the dual edges corresponding to \(E(C)\) form a bond of the underlying graph of \(D^*\). Moreover, every such dual edge is directed from the faces in \(L(C)\) to the faces in \(R(C)\). Thus \(E(C)^*\) is a directed bond.

Conversely, every directed bond of \(D^*\) corresponds under planar duality to a directed cycle of \(D\), with the tail side of the bond equal to \(L(C)\) and the head side equal to \(R(C)\).

It remains to use the following elementary directed-graph lemma.

**Lemma 2.2.**  
Let \(H\) be a weakly connected digraph and let \(s,t\in V(H)\). The following are equivalent.

1. Every directed bond of \(H\) is directed from a side containing \(s\) to a side containing \(t\).
2. The SCC condensation of \(H\) has a unique source containing \(s\) and a unique sink containing \(t\).

**Proof.**

Suppose first that the condensation \(Q\) has unique source \(q_s\) and unique sink \(q_t\). Every vertex of \(Q\) is reachable from \(q_s\), and every vertex reaches \(q_t\).

Let a directed bond be oriented from \(A\) to \(\overline A\). Since there is no edge from \(\overline A\) to \(A\), the set \(A\) is predecessor-closed in \(Q\). It is nonempty, so it contains \(q_s\). If it contained \(q_t\), then predecessor-closure and the fact that every vertex reaches \(q_t\) would imply \(A=V(Q)\), contrary to the bond being nontrivial. Hence \(q_t\in\overline A\).

Conversely, suppose every directed bond has the stated terminal placement. If \(Q\) had a source \(q\neq q_s\), remove \(q\) from the underlying undirected graph of \(Q\), and let \(K\) be the component containing \(q_s\). Then
\[
A=V(Q)\setminus V(K),\qquad B=V(K)
\]
are both connected in the underlying graph. All edges crossing from \(A\) to \(B\) are incident with \(q\), and, since \(q\) is a source, are directed from \(A\) to \(B\). This gives a directed bond whose tail side omits \(s\), a contradiction. Thus \(q_s\) is the unique source. The argument for the unique sink is symmetric. ∎

Applying Lemma 2.2 to \(H=D^*\), and using directed circuit-bond duality, proves the equivalence. ∎

### 2.3 Consequences

An abstract connected digraph \(D\) admits a circular drawing if and only if it has a planar embedding whose left-to-right dual has one source SCC and one sink SCC.

For a **given embedding**, this is testable in linear time:

1. enumerate the faces;
2. construct \(D^*\);
3. compute its SCCs;
4. count source and sink SCCs in the condensation.

This does not solve the embedding-selection problem when the underlying graph has cutvertices or 2-separations.

---

## 3. A complete strongly connected, 3-connected special case

Strong connectivity makes the dual criterion particularly simple.

**Lemma 3.1.**  
If \(D\) is strongly connected, then its left-to-right directed dual \(D^*\) is acyclic.

#### Proof

A directed cycle in \(D^*\) corresponds by planar circuit-bond duality to a bond of the underlying graph of \(D\) all of whose edges are directed consistently across the bond. There can then be no directed path across that cut in the opposite direction, contradicting strong connectivity. ∎

Suppose additionally that every facial boundary is a cycle, as happens when the underlying graph is 2-connected. A face is a source of \(D^*\) exactly when all edges on its boundary are directed consistently with the face on their left. Similarly, a face is a sink exactly when its boundary is directed consistently with the face on its right.

Because \(D^*\) is an acyclic connected digraph, it has at least one source and at least one sink. Proposition 2.1 therefore gives:

**Corollary 3.2.**  
Let \(D\) be a strongly connected plane orientation whose underlying graph is 2-connected. Then the fixed embedding is circular if and only if exactly two faces have directed boundary cycles—one corresponding to the unique source of \(D^*\), and one to its unique sink.

This produces an intrinsic characterization when the underlying graph is 3-connected.

Recall that a cycle of a graph is peripheral if it is induced and deleting its vertices leaves the remainder connected. In a 3-connected planar graph, the peripheral cycles are exactly the facial cycles in its unique spherical embedding.

**Theorem 3.3 — strong 3-connected special case.**  
Let \(D\) be a strongly connected orientation of a finite simple 3-connected graph \(G\). Then \(D\) admits a circular drawing if and only if:

1. \(G\) is planar; and
2. \(D\) has no three distinct directed peripheral cycles.

When these conditions hold, \(D\) has exactly two directed peripheral cycles.

#### Proof

If \(D\) is circular, then \(G\) is planar. By uniqueness of the spherical embedding of a 3-connected planar graph, its facial cycles are intrinsic and are precisely its peripheral cycles. By Proposition 2.1 and Lemma 3.1, the dual is an acyclic digraph with a unique source and a unique sink. Hence exactly two faces have directed boundaries, so exactly two peripheral cycles are directed.

Conversely, suppose \(G\) is planar and \(D\) has at most two directed peripheral cycles. Use the unique spherical embedding of \(G\). By Lemma 3.1, \(D^*\) is acyclic. Therefore \(D^*\) has at least one source and one sink, and the corresponding facial boundaries are directed. Thus \(D\) has at least two directed peripheral cycles. By hypothesis it has exactly two, so \(D^*\) has exactly one source and exactly one sink. Proposition 2.1 now gives a circular drawing. ∎

Using Kuratowski’s theorem, this can be phrased as a genuine, though restricted and global, forbidden-configuration statement:

> A strongly connected orientation of a simple 3-connected graph is circular if and only if its underlying graph contains no subdivision of \(K_5\) or \(K_{3,3}\), and it contains no triple of directed peripheral cycles.

The second obstruction is global rather than a fixed subdigraph, so this is unlikely to be the Thomassen-style characterization sought in the source paper. It is nevertheless a complete special case.

---

## 4. Why the meaning of “type \(X\)” matters

### 4.1 A tautological infinite characterization

Under the crossing-free definition, circularity is hereditary under taking subdigraphs: delete vertices or edges from a circular drawing and retain the same origin.

Let \(\mathcal M\) be the family of subdigraph-minimal noncircular finite digraphs. Finiteness ensures that every noncircular digraph contains some member of \(\mathcal M\). Hence
\[
D\text{ is circular}
\quad\Longleftrightarrow\quad
D\text{ contains no member of }\mathcal M
\]
as an ordinary subdigraph.

Thus, if arbitrary infinite obstruction families are allowed, the requested theorem exists for formal reasons and carries no structural information.

### 4.2 No finite ordinary-subdigraph obstruction family

**Proposition 4.1.**  
Under the standard crossing-free definition, the class of all finite circular digraphs is not characterized by any finite family of forbidden ordinary subdigraphs.

#### Proof

For \(n\geq 1\), let \(U_n\) be obtained from \(K_{3,3}\) by subdividing every edge exactly \(n\) times. Orient every replacement path consistently from one part of the bipartition to the other, and call the resulting acyclic digraph \(D_n\).

The underlying graph \(U_n\) is nonplanar, so \(D_n\) is not circular. On the other hand, every proper subgraph of \(U_n\) is planar. Indeed, deleting any edge breaks one subdivided \(K_{3,3}\)-edge; what remains is a subgraph of a subdivision of \(K_{3,3}-e\), together with pendant path segments. The graph \(K_{3,3}-e\) is planar.

Every proper subdigraph of \(D_n\) is therefore both planar and acyclic. It consequently has a circular drawing vacuously, since it has no directed cycles. Thus every \(D_n\) is subdigraph-minimal noncircular.

The \(D_n\) are pairwise nonisomorphic. If a finite family \(\mathcal F\) characterized circularity, some \(F\in\mathcal F\) would occur in every noncircular \(D_n\). Since every proper subdigraph of \(D_n\) is circular, such an \(F\) would have to be isomorphic to \(D_n\). A finite family cannot contain all \(D_n\), a contradiction. ∎

This argument does not rule out finite obstruction families under subdivision or directed-topological-minor containment: all the \(U_n\) have the same underlying topological type. Nor does it address a restriction to strongly connected digraphs.

---

## 5. Remaining gap

The results above do not settle the intended open direction. They leave open the substantive problem of finding a useful primal obstruction theory for a specified class such as strongly connected or strongly 2-connected digraphs, under a specified containment relation.

In particular:

- Proposition 2.1 is embedding-dependent.
- Theorem 3.3 relies on uniqueness of the embedding and therefore bypasses precisely the 2-separator phenomena highlighted in the source.
- No characterization is given for choosing among the generally many embeddings of a graph with 2-separations.
- Nothing here establishes a finite topological-minor, immersion, or directed-minor obstruction set.

Thus the original catalog item remains unanswerable as written, while the strongly connected 3-connected case has the exact characterization above.