---
title: 'Geodesic cycles and Tutte''s Theorem'
subtitle: 'Unrefereed candidate disproof by GPT-6 Astra'
author:
  - 'Writeup: `gpt-6-astra` (single model pass)'
date: 'Catalog id `geodesic_cycles_and_tuttes_theorem` — generated 2026-09-16'
---

::: {.warning}
**UNREFEREED MODEL OUTPUT.** This document was selected solely because GPT-6 Astra labelled its own result `would_publish: true` and returned `proved` or `disproved`. It has not passed the adversarial LLM referee used for the earlier Sol campaign, has not been checked by a human mathematician, and has not been checked for novelty. Treat every mathematical and bibliographic claim below as unverified.
:::

# Summary and provenance

| | |
|:--|:--|
| Catalog id | `geodesic_cycles_and_tuttes_theorem` |
| Catalog entry | [Geodesic cycles and Tutte's Theorem](https://graph-theory-ai.github.io/graph-conjectures/op/geodesic_cycles_and_tuttes_theorem/) |
| Source corpus | opg |
| Campaign leg | OpenProblemGarden first pass (`attacks_opg`) |
| Source paper / entry | http://www.openproblemgarden.org/op/geodesic_cycles_and_tuttes_theorem |
| Model verdict | **disproved** (confidence: high) |
| Model's one-line claim | The eight-vertex graph obtained by inserting a degree-three vertex into every face of a tetrahedron is a counterexample. |
| Model | `gpt-6-astra`, reasoning effort `max`, `mode=pro`, flex service tier |
| Original artifact | `attacks_opg/geodesic_cycles_and_tuttes_theorem/output.md` |
| Independent review | **None** |
| Model's caveats | Peripheral has its standard induced, vertex-nonseparating meaning; bibliographical novelty has not been checked. |

# Problem statement

Problem If $G$ is a $3$ -connected finite graph, is there an assignment of lengths $\ell: E(G) \to \mathbb{R}^+$ to the edges of $G$ , such that every $\ell$ -geodesic cycle is peripheral ?

## Catalog context

A cycle $C$ is $\ell$ -geodesic if for every two vertices $x,y$ on $C$ there is no $x$ - $y$ ~path in $G$ shorter, with respect to $\ell$ , than both $x$ - $y$ ~arcs on $C$ . It is not hard to prove [GS] that for every finite graph $G$ and every assignment of edge lengths $\ell: E(G) \to \mathbb{R}^+$ the $\ell$ -geodesic cycles of $G$ generate its cycle space. Thus, a positive answer to the problem would imply a new proof of Tutte's classical theorem [T] that the peripheral cycles of a $3$ -connected finite graph generate its cycle space.

# Astra writeup

*The text below is the model output verbatim, apart from moving its machine-readable verdict block into the summary above and shifting Markdown heading levels for this document. Mechanical TeX defects and equation tags were normalized where needed for compilation.*

## An eight-vertex counterexample

A cycle is **peripheral** if it is induced and deleting its vertices leaves a connected graph.

Let
\[
B=\{b_1,b_2,b_3,b_4\},\qquad S=\{s_1,s_2,s_3,s_4\},
\]
and define \(G\) by
\[
V(G)=B\cup S,\qquad
E(G)=\{b_ib_j:i<j\}\ \cup\ \{s_i b_j:i\ne j\}.
\]
Thus \(B\) induces a \(K_4\), the set \(S\) is independent, and \(s_i\) is adjacent to the three vertices of \(B\setminus\{b_i\}\).

Equivalently, start with a tetrahedron embedded on the sphere and insert one vertex into each face, joining it to that face’s three vertices.

**Theorem.** For every assignment \(\ell:E(G)\to\mathbb R_{>0}\), some \(\ell\)-geodesic cycle of \(G\) is not peripheral.

### 1. Connectivity and peripheral cycles of \(G\)

The graph \(G\) is 3-connected. Indeed, after deleting at most two vertices, at least two vertices of \(B\) remain and induce a connected clique. Every surviving \(s_i\) retains at least one of its three neighbours in \(B\), so the remaining graph is connected.

There are eight vertices and eighteen edges, hence
\[
\dim_{\mathbb F_2}\mathcal C(G)=18-8+1=11.
\]

We next classify the peripheral cycles.

Every induced cycle of \(G\) is a triangle. To see this, an induced cycle of length at least four cannot contain \(s_i\): its two neighbours along the cycle would belong to \(B\), and the edge between them would be a chord. A cycle of length at least four entirely within \(B\) also has a chord.

The triangles are of two types:

* The four triangles
  \[
  T_i=G[B\setminus\{b_i\}]
  \]
  are **not peripheral**. In \(G-V(T_i)\), the vertex \(s_i\) is isolated, whereas the other remaining vertices form a nonempty connected component.

* The twelve triangles
  \[
  P_{i;jk}=s_i b_j b_k s_i,
  \qquad j<k,\quad i\notin\{j,k\},
  \]
  **are peripheral**. After deleting such a triangle, two adjacent vertices of \(B\) remain. Every other surviving vertex of \(S\) has a neighbour among these two vertices.

Consequently, \(G\) has exactly twelve peripheral cycles, all triangles. Each contains **exactly one edge of the core \(K_4\)**.

### 2. Two metric facts

We use two elementary facts, including their proofs to handle arbitrary positive lengths and possible ties.

#### Fact 1: Geodesic cycles generate the cycle space

Let \(H\) be any finite graph with positive edge lengths. If a cycle \(C\) is not geodesic, there is a path \(P\) between vertices \(x,y\in V(C)\) with
\[
\ell(P)<d_C(x,y),
\]
where \(d_C\) is distance measured within \(C\).

There is then a path \(Q\), with distinct endpoints \(u,v\in V(C)\) and all internal vertices outside \(C\), that is shorter than both \(u\)-\(v\) arcs of \(C\). Indeed, otherwise every excursion of \(P\) outside \(C\) could be replaced by a no-longer arc of \(C\). This would produce an \(x\)-\(y\) walk in \(C\) of length at most \(\ell(P)<d_C(x,y)\), a contradiction.

Write the two \(u\)-\(v\) arcs as \(A,B\). The cycles
\[
C_1=A\cup Q,\qquad C_2=B\cup Q
\]
satisfy
\[
E(C)=E(C_1)\mathbin{\triangle}E(C_2),
\qquad
\ell(C_1)<\ell(C),\quad \ell(C_2)<\ell(C).
\]
Induction through the finitely many cycle lengths proves that the geodesic cycles generate \(\mathcal C(H)\).

#### Fact 2: An admissible assignment can be perturbed to have unique shortest paths

Suppose an assignment has the property that every geodesic cycle is peripheral. For each nonperipheral cycle, choose one path witnessing its failure to be geodesic. Each witness gives two strict linear inequalities: the path is shorter than each of the two corresponding cycle arcs.

There are finitely many nonperipheral cycles. Thus these inequalities, and positivity of all edge lengths, persist throughout an open neighbourhood of the assignment.

Inside this neighbourhood, choose lengths avoiding all equalities
\[
\ell(P)=\ell(Q)
\]
between distinct simple paths with the same endpoints. These equalities form finitely many proper hyperplanes. The perturbed assignment still has no nonperipheral geodesic cycle, and every pair of vertices now has a unique shortest path.

Importantly, this argument preserves the strict shortcuts for nonperipheral cycles; it does **not** assume that particular peripheral cycles remain geodesic.

### 3. Contradiction

Suppose that \(G\) admits a positive length assignment for which every geodesic cycle is peripheral. By Fact 2, assume additionally that shortest paths between vertices are unique.

By Fact 1, the geodesic cycles generate the 11-dimensional cycle space. Since all of them belong to the twelve peripheral triangles listed above, at least eleven of those triangles must be geodesic. Therefore
\[
\boxed{\text{At most one peripheral triangle is not geodesic.}}
\qquad\text{(1)}
\]

Call an edge \(uv\) **tight** if
\[
\ell(uv)=d_\ell(u,v).
\]
Every edge satisfies \(\ell(uv)\ge d_\ell(u,v)\), so a non-tight edge has strictly greater length than the distance between its endpoints.

Consider a core edge \(e=b_jb_k\). Let \(\{p,q\}=\{1,2,3,4\}\setminus\{j,k\}\). Exactly two peripheral triangles contain \(e\):
\[
P_{p;jk}\quad\text{and}\quad P_{q;jk}.
\]

If \(e\) is non-tight, these two triangles cannot both be geodesic. Otherwise, geodesicity for the pair \(b_j,b_k\) would imply
\[
\ell(b_js_p)+\ell(s_pb_k)
=d_\ell(b_j,b_k)
=\ell(b_js_q)+\ell(s_qb_k).
\]
The two distinct paths \(b_js_pb_k\) and \(b_js_qb_k\) would both be shortest, contradicting uniqueness.

Thus every non-tight core edge belongs to a non-geodesic peripheral triangle. Different core edges require different such triangles, because each peripheral triangle contains exactly one core edge. By (1),
\[
\boxed{\text{At most one core edge is non-tight.}}
\qquad\text{(2)}
\]

There is consequently a core triangle \(T_i\) containing no non-tight edge: if the exceptional edge exists, choose a core triangle avoiding it.

All three edges of this \(T_i\) are tight. For every pair of vertices of \(T_i\), their joining edge therefore realizes their distance in \(G\). Hence \(T_i\) is geodesic.

But \(T_i\) is not peripheral, as established in Section 1. This is the required contradiction. \(\square\)

### Completeness and status

The perturbation argument covers assignments with tied shortest paths as well as generic assignments. Thus the counterexample rules out **every** positive edge-length assignment, not merely those in general position.

The graph is simple, planar, and 3-connected, so the assertion fails even within the planar subclass. The proof is self-contained; I have not checked whether this counterexample or argument has previously appeared in the literature.
