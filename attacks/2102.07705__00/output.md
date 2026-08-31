```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "For every orientation of the star K_{1,n} with n at least 3, I give a planarity-preserving reduction from signed Planar NAE-4-SAT to 2-F-PFC, but I do not extend it to all nontrivial leaf-extensions of the star.",
  "would_publish": false,
  "caveats": "The exact-star reduction is rigorous, but the precise NP-complete source variant should be checked against a primary citation; the gadgets are not necessarily acyclic."
}
```

# 1. Interpretation and partial result

I use the following formulation of \(2\)-\(F\)-PFC.

> **\(2\)-\(F\)-PFC.** For a fixed oriented graph \(F\), the input is an oriented planar graph \(D\). Decide whether \(V(D)\) has a 2-coloring with no monochromatic induced copy of \(F\).

Let \(S_{a,b}\) denote the orientation of \(K_{1,n}\), \(n=a+b\), in which the center has \(a\) outgoing and \(b\) incoming arcs. Every orientation of \(K_{1,n}\) is isomorphic to exactly one such \(S_{a,b}\).

The main partial result is:

> **Theorem.** Let \(a,b\geq 0\) and \(a+b=n\geq 3\). There is a polynomial-time, planarity-preserving reduction
> \[
> \text{signed Planar NAE-4-SAT}\ \leq_m\ 2\text{-}S_{a,b}\text{-PFC}.
> \]
> Consequently, under the standard NP-completeness of signed incidence-planar NAE-4-SAT, \(2\)-\(S_{a,b}\)-PFC is NP-complete for every orientation of \(K_{1,n}\), \(n\geq3\).

Membership in NP is immediate because \(F\) is fixed.

The reduction rests on clean equality and disequality gadgets for every oriented star.

# 2. A clean equality gadget

Write
\[
q_{\mathrm{out}}=a,\qquad q_{\mathrm{in}}=b.
\]
Directions with quota zero are omitted.

For two terminals \(x,y\), construct \(E_{a,b}(x,y)\) as follows. For every ordered pair
\[
(\sigma,\tau)\in\{\mathrm{out},\mathrm{in}\}^2
\]
with \(q_\sigma,q_\tau>0\), introduce an independent set
\[
Z_{\sigma,\tau}
\quad\text{of size}\quad
q_\sigma+q_\tau-1.
\]
Each \(z\in Z_{\sigma,\tau}\) is adjacent only to \(x\) and \(y\). Orient its edge at \(y\) according to \(\sigma\), and its edge at \(x\) according to \(\tau\). Thus, for example,

- if \(\sigma=\mathrm{out}\), put \(y\to z\);
- if \(\sigma=\mathrm{in}\), put \(z\to y\),

and analogously at \(x\). There is no arc between \(x\) and \(y\), and no arc between two internal vertices.

The underlying graph is \(K_{2,M}\), where
\[
M=\sum_{\sigma,\tau:q_\sigma q_\tau>0}(q_\sigma+q_\tau-1),
\]
so it is planar, with \(x,y\) on a common face.

## Lemma 2.1

Every \(S_{a,b}\)-free 2-coloring of \(E_{a,b}(x,y)\) satisfies
\[
\operatorname{col}(x)=\operatorname{col}(y).
\]
Conversely, either common terminal color extends to a coloring in which every arc of the gadget is bichromatic.

### Proof

Suppose, for a contradiction, that \(x\) has color \(0\) and \(y\) has color \(1\).

For each direction \(\sigma\), consider all internal vertices whose incidence with \(y\) has type \(\sigma\). If \(y\) had at least \(q_\sigma\) color-\(1\) internal neighbors in every direction \(\sigma\) with positive quota, then, because all internal vertices are pairwise nonadjacent, suitable choices of these vertices together with \(y\) would induce a monochromatic \(S_{a,b}\).

Therefore, for some \(\sigma\) with \(q_\sigma>0\), the total number of color-\(1\) vertices in
\[
\bigcup_{\tau:q_\tau>0} Z_{\sigma,\tau}
\]
is at most \(q_\sigma-1\).

Fix any \(\tau\) with \(q_\tau>0\). Since
\[
|Z_{\sigma,\tau}|=q_\sigma+q_\tau-1,
\]
at least
\[
(q_\sigma+q_\tau-1)-(q_\sigma-1)=q_\tau
\]
vertices of \(Z_{\sigma,\tau}\) have color \(0\). Selecting \(q_\tau\) such vertices for every \(\tau\) gives, together with \(x\), a monochromatic induced \(S_{a,b}\) centered at \(x\), again because all internal vertices are pairwise nonadjacent. This contradiction proves \(x=y\) in color.

Conversely, if \(x\) and \(y\) receive the same color, color every internal vertex with the other color. Every arc is then bichromatic, so the gadget contains no monochromatic copy of any connected graph with an arc. \(\square\)

The proof is unaffected by additional edges incident with \(x\) or \(y\), provided the internal vertices remain private. Thus the equality relation is robust under composition.

# 3. A clean disequality gadget

Construct \(I_{a,b}(x,y)\) as follows.

1. Take a fresh induced copy \(Q\) of \(S_{a,b}\), with center \(c\) and leaves
   \[
   u_1,\dots,u_n.
   \]
2. Join \(y\) to \(c\) through a fresh equality gadget \(E_{a,b}(y,c)\).
3. For every \(i\), join \(x\) to \(u_i\) through a fresh equality gadget \(E_{a,b}(x,u_i)\).

## Lemma 3.1

Every \(S_{a,b}\)-free 2-coloring of \(I_{a,b}(x,y)\) satisfies
\[
\operatorname{col}(x)\neq\operatorname{col}(y).
\]
Conversely, either assignment of opposite colors to \(x,y\) extends so that every arc in the gadget is bichromatic.

### Proof

By Lemma 2.1,
\[
\operatorname{col}(c)=\operatorname{col}(y),\qquad
\operatorname{col}(u_i)=\operatorname{col}(x)
\]
for every \(i\). If \(x\) and \(y\) had the same color, the fresh copy \(Q\) would be monochromatic, a contradiction.

If \(x\) and \(y\) have opposite colors, color \(c\) as \(y\), all \(u_i\) as \(x\), and extend every equality gadget by coloring its internal vertices opposite to its equal-colored terminals. All arcs of \(Q\) and all arcs of the equality gadgets are then bichromatic. \(\square\)

The gadget is planar. At the level of its blocks, its underlying graph is obtained from the planar graph consisting of \(K_{2,n}\) with poles \(x,c\), together with a pendant connection from \(y\) to \(c\), by replacing certain edges by planar two-terminal equality gadgets. The terminals \(x,y\) may be placed on the outer face.

# 4. Reduction from signed Planar NAE-4-SAT

The source problem used here is:

> **Signed Planar NAE-4-SAT.** Each clause consists of four signed literals. The variable-clause incidence graph, with signs ignored, is planar. Decide whether the variables can be assigned truth values so that every clause contains both a true and a false literal.

I use the standard NP-completeness of this problem as an external complexity fact. I have not independently checked, in this response, a primary citation establishing exactly the “four literals, signed, incidence-planar” formulation. The reduction below itself is independent of that bibliographic point.

Let
\[
F=S_{a,b},\qquad k=|V(F)|=n+1\geq4.
\]

Given a planar NAE-4-SAT instance \(\Phi\), construct an oriented planar graph \(D_\Phi\).

## Variables

For every Boolean variable \(X\), introduce a vertex \(h_X\). Its color will represent the truth value of \(X\).

## Clauses

For a clause
\[
C=(\ell_1,\ell_2,\ell_3,\ell_4),
\]
form a list \(L_C\) of length \(k\):

- if \(k=4\), use the four literals;
- if \(k>4\), append \(k-4\) further copies of \(\ell_1\).

Thus all entries of \(L_C\) have the same truth value if and only if the original four literals do.

Create \(k\) distinct vertices
\[
v_{C,1},\dots,v_{C,k}
\]
which induce a fresh copy of \(F\), with one vertex assigned the center role and the remaining \(n\) vertices the appropriate incoming and outgoing leaf roles.

If position \(j\) contains a positive occurrence of \(X\), connect \(h_X\) to \(v_{C,j}\) by a fresh equality gadget. If it contains a negative occurrence of \(X\), connect them by a fresh disequality gadget.

All gadget interiors are mutually disjoint.

# 5. Planarity

Start with a fixed planar embedding of the incidence graph of \(\Phi\). When a literal is repeated to pad a clause, draw the additional incidence edges parallel to the original edge for that literal.

Replace each incidence edge by the corresponding two-terminal equality or disequality gadget in a narrow strip around that edge. Both gadgets have embeddings with their terminals on a common face.

Inside a small disk around a clause vertex, put the \(k\) occurrence vertices on the boundary in their incidence order. Choose one as the center of the star and draw all star arcs from it to the other occurrence vertices inside the disk. These arcs can be drawn pairwise disjoint except at their common center.

At a variable vertex, all incident gadget terminals are identified with the single vertex \(h_X\); the planar blocks can be arranged in separate angular sectors. Thus \(D_\Phi\) is planar. It is also oriented: no pair receives arcs in both directions.

# 6. Correctness

## Soundness

Suppose \(D_\Phi\) has an \(F\)-free 2-coloring.

Assign \(X\) the Boolean value given by the color of \(h_X\). By Lemmas 2.1 and 3.1, every positive occurrence vertex has the color of its variable, and every negative occurrence vertex has the opposite color.

For each clause \(C\), its \(k\) occurrence vertices induce a copy of \(F\). They therefore cannot all have the same color. Because every original literal occurs at least once in \(L_C\), the original four literal values are not all equal. Thus every clause is NAE-satisfied.

Hence \(\Phi\) is satisfiable.

## Completeness

Conversely, suppose \(\Phi\) has an NAE assignment.

Color every \(h_X\) according to the value of \(X\), and every occurrence vertex according to its literal value. Extend:

- each equality gadget by its clean extension from Lemma 2.1;
- each disequality gadget by its clean extension from Lemma 3.1.

Every arc lying in a wire gadget is bichromatic. Therefore the only potentially monochromatic arcs are arcs inside the clause copies of \(F\).

In a clause copy:

- a leaf has only one clause neighbor, so it cannot center a copy of \(K_{1,n}\) because \(n\geq3\);
- the clause center has precisely its \(n\) clause leaves as possible same-colored neighbors outside the bichromatic wire gadgets;
- since the clause is NAE-satisfied, at least one of the \(n+1\) clause vertices differs in color from another. In particular, the center has at most \(n-1\) same-colored clause leaves.

Thus no clause center has \(n\) same-colored neighbors, and no monochromatic induced \(F\) occurs. Hence \(D_\Phi\) has an \(F\)-free 2-coloring.

This completes the reduction.

# 7. What this resolves

Subject to the standard source-problem lemma, the argument proves:

\[
\boxed{\text{\(2\)-\(F\)-PFC is NP-complete for every orientation \(F\) of \(K_{1,n}\), \(n\geq3\).}}
\]

This includes all orientations of the claw \(K_{1,3}\), not merely the all-in or all-out orientations.

The construction also gives, unconditionally, explicit planar equality and disequality senders for exact oriented stars.

# 8. Gap to the catalog problem

The argument does not automatically extend to a larger oriented tree \(T\) whose iterated leaf-pruning core is a star. Avoiding a monochromatic \(T\) is weaker than avoiding a monochromatic copy of its star core. In particular, the equality proof above uses the fact that sufficiently many appropriately oriented, pairwise independent same-colored neighbors already constitute the entire forbidden graph. If each “leaf” must carry a nontrivial branch, those branches can be colored nonmonochromatically, and the counting argument no longer forces equality.

Thus one still needs either:

1. a clean equality sender for every such larger oriented tree \(T\); or
2. a verified planarity-preserving inheritance theorem showing that NP-hardness for a pruned core transfers to every permitted leaf extension.

The catalog description suggests that the source paper has machinery for path-pruned trees, but I have not verified an exact proposition broad enough to combine automatically with the star theorem above. I therefore do not claim the full catalog problem is resolved.

Finally, for mixed orientations \(a,b>0\), the equality gadget generally contains directed 4-cycles, so this proof does not establish hardness under the stronger restriction that the input orientation be acyclic.