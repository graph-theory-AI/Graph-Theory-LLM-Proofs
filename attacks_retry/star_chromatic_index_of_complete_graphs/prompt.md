Attack the following open graph-theory problem.

Catalog id: star_chromatic_index_of_complete_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/star_chromatic_index_of_complete_graphs/
Original entry: http://www.openproblemgarden.org/op/star_chromatic_index_of_complete_graphs
Problem attributed to: Dvorak, Zdenek, Mohar, Bojan, Samal, Robert (posted 2010-11-16)

=== Problem statement (OpenProblemGarden) ===
Title: Star chromatic index of complete graphs
Conjecture Is it possible to color edges of the complete graph $ K_n $ using $ O(n) $ colors, so that the coloring is proper and no 4-cycle and no 4-edge path is using only two colors? Equivalently: is the star chromatic index of $ K_n $ linear in $ n $ ?

=== Discussion / context (OpenProblemGarden) ===
The star chromatic index $ \chi_s'(G) $ of a graph $ G $ is the minimum number of colors needed to properly color the edges of $ G $ so that no path or cycle of length four is bi-colored. An equivalent definition is that $ \chi_s'(G) $ is the star chromatic number of the line graph $ L(G) $ . Dvořák, Mohar, and Šámal [DMS] show that $ \chi_s'(G) \ge (2+o(1))n $ . On the other hand, the best known upper bound (also in \cite{DMS]) is superlinear: $$ \chi_s'(K_n) \le n \cdot \frac{ 2^{ 2\sqrt2(1+o(1)) \sqrt{\log n} } }{(\log n)^{1/4}} \,. $$ It may be possible to decrease the upper bound by elementary methods.

=== References listed by OpenProblemGarden ===
- *[DMS] Dvořák, Zdeněk; Mohar, Bojan; Šámal, Robert: Star chromatic index, arXiv:1011.3376.

=== Catalog page (statement + literature review) ===
Star chromatic index of complete graphs — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The question of whether $\chi_s'(K_n) = O(n)$ remains open. The bounds established by Dvořák, Mohar, and Šámal in the original paper — a lower bound of $(2+o(1))n$ and a superlinear upper bound of $n \cdot 2^{2\sqrt{2}(1+o(1))\sqrt{\log n}}/(\log n)^{1/4}$ — still represent the state of the art. Multiple searches and the 2020 survey on star edge-coloring confirm that no resolution of the complete graph case has appeared in the literature.

 Reviewer notes. The survey arXiv:2009.08017 (Lei and Shi, 2020) on star edge-coloring was verified to exist but its PDF was not machine-readable; its abstract confirms it collects open problems in the area, suggesting the complete graph linearity question remains open. No citing paper found via four search rounds provided evidence of resolution. Research since 2010 has focused on specific graph classes (sparse graphs, subcubic, planar, multipartite) rather than on the complete graph linearity question.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Is it possible to color edges of the complete graph $ K_n $ using $ O(n) $ colors, so that the coloring is proper and no 4-cycle and no 4-edge path is using only two colors? Equivalently: is the star chromatic index of $ K_n $ linear in $ n $ ?

Keywords:
complete graph · edge coloring · star coloring

Discussion

The star chromatic index $ \chi_s'(G) $ of a graph $ G $ is the minimum number of colors needed to properly color the edges of $ G $ so that no path or cycle of length four is bi-colored. An equivalent definition is that $ \chi_s'(G) $ is the star chromatic number of the line graph $ L(G) $ . Dvořák, Mohar, and Šámal [DMS] show that $ \chi_s'(G) \ge (2+o(1))n $ . On the other hand, the best known upper bound (also in \cite{DMS]) is superlinear: $$ \chi_s'(K_n) \le n \cdot \frac{ 2^{ 2\sqrt2(1+o(1)) \sqrt{\log n} } }{(\log n)^{1/4}} \,. $$ It may be possible to decrease the upper bound by elementary methods.

Bibliography

★ [DMS]
 Dvořák, Zdeněk; Mohar, Bojan; Šámal, Robert: Star chromatic index, arXiv:1011.3376 .
 arXiv:1011.3376

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An indexed-block packing argument gives chi_s'(K_n) >= 3n - O(1), but does not resolve whether O(n) colors suffice.",
  "would_publish": false,
  "caveats": "Linearity remains unresolved; novelty of the lower bound has not been checked."
}
```

## A lower bound with leading constant \(3\)

I obtain the following self-contained partial result:
\[
\boxed{
\chi_s'(K_n)\ge
\left\lceil
\frac{3\binom n2}{\lfloor n/2\rfloor+2}
\right\rceil
\qquad(n\ge2).
}
\]
Equivalently,
\[
\chi_s'(K_n)\ge
\begin{cases}
\displaystyle\left\lceil\frac{3n(n-1)}{n+4}\right\rceil,
& n\text{ even},\\[1.2ex]
\displaystyle\left\lceil\frac{3n(n-1)}{n+3}\right\rceil,
& n\text{ odd}.
\end{cases}
\]
In particular,
\[
\chi_s'(K_n)\ge 3n-O(1).
\]

This is stronger than the leading-constant-\(2\) bound quoted in the question. I have not independently checked whether this observation is already known or whether the supplied literature summary is incomplete.

### 1. The packing lemma

Consider a proper edge-coloring of a simple graph on vertex set \(V\). Its color classes \(M_1,\dots,M_k\) are matchings.

For every unordered pair of edges \(e,f\) belonging to the same color class, form the four-element set
\[
B(e,f)=V(e)\cup V(f).
\]
Keep these sets as an **indexed collection**: different pairs of edges give different members, even if their four-element supports coincide.

**Lemma.** The coloring is a star edge-coloring if and only if every three-element subset of \(V\) is contained in at most one member of this indexed collection.

**Proof.** Suppose two distinct members contain the same triple.

They cannot come from the same color class. Indeed, two distinct pairs of edges from a matching have supports intersecting in either zero or two vertices.

Thus they arise from two edges of color \(a\) and two edges of another color \(b\). The four selected edges are distinct, and their union has either four or five vertices.

- If it has four vertices, every vertex has degree two, so the union is a bichromatic \(4\)-cycle.
- If it has five vertices, three vertices have degree two and two have degree one. Since the union is properly two-colored, it has no odd cycle; it cannot have an even cycle either, because only three vertices have degree two. Consequently, the union is a bichromatic four-edge path.

Both are forbidden.

Conversely, a bichromatic four-edge path supplies two same-colored pairs of edges whose four-vertex supports share the three internal vertices. A bichromatic \(4\)-cycle supplies two such pairs with identical supports. Either violates the stated packing property. ∎

The indexing is essential: it is what detects a bichromatic \(4\)-cycle.

### 2. Counting the blocks

Now let the coloring be a star edge-coloring of \(K_n\), and write
\[
N=\binom n2,\qquad m_i=|M_i|.
\]
Then
\[
\sum_{i=1}^k m_i=N.
\]
The number of indexed blocks is
\[
B=\sum_{i=1}^k\binom{m_i}{2}.
\]

The lemma immediately gives
\[
4B\le \binom n3,
\]
because each block contains four triples and no triple is counted twice. A pair-incidence count slightly strengthens this when \(n\) is odd.

Fix a pair \(\{x,y\}\). Distinct blocks containing this pair must have disjoint sets of remaining vertices: otherwise they would share a triple. Hence the number \(d(x,y)\) of blocks containing \(\{x,y\}\) satisfies
\[
d(x,y)\le \left\lfloor\frac{n-2}{2}\right\rfloor.
\]
Every block contains six pairs, so
\[
6B=\sum_{\{x,y\}\subseteq V}d(x,y)
\le N\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
Therefore
\[
\begin{aligned}
\sum_{i=1}^k m_i^2
&=N+2B\\
&\le N\left(1+\frac13\left\lfloor\frac{n-2}{2}\right\rfloor\right)\\
&=\frac N3\bigl(\lfloor n/2\rfloor+2\bigr).
\end{aligned}
\]
By Cauchy–Schwarz,
\[
N^2=\left(\sum_{i=1}^k m_i\right)^2
\le k\sum_{i=1}^k m_i^2
\le \frac{kN}{3}\bigl(\lfloor n/2\rfloor+2\bigr).
\]
Dividing by \(N>0\) proves the claimed bound.

The underlying necessary condition, which retains more information than the final Cauchy–Schwarz step, is
\[
\boxed{
\sum_{i=1}^k\binom{m_i}{2}
\le
\left\lfloor
\frac{\binom n2}{6}
\left\lfloor\frac{n-2}{2}\right\rfloor
\right\rfloor.
}
\]

## A sharp finite check: \(K_8\)

The displayed lower bound gives
\[
\chi_s'(K_8)\ge14.
\]
Here is an explicit coloring attaining \(14\), also illustrating the packing lemma.

Use vertices \(0,1,\dots,7\). Each brace below is a separate color class; \(ij\) denotes the edge \(\{i,j\}\).
\[
\begin{array}{c|c}
\{01,23\}&\{45,67\}\\
\{04,15\}&\{26,37\}\\
\{06,17\}&\{24,35\}\\
\{02,46\}&\{13,57\}\\
\{05,27\}&\{14,36\}\\
\{07,34\}&\{16,25\}\\
\{03,56\}&\{12,47\}
\end{array}
\]
These are fourteen matchings partitioning all \(28\) edges.

Identify the vertex labels with their binary vectors in \(\mathbb F_2^3\). The four vertices supporting each color class sum to zero. Moreover, the fourteen supports in the table are distinct. Two distinct zero-sum four-element sets cannot share three vertices, because those three vertices uniquely determine the fourth.

Thus their supports satisfy the packing lemma, and the coloring is a star edge-coloring. Consequently,
\[
\boxed{\chi_s'(K_8)=14.}
\]
This is a directly checkable construction, not a claim based on an unspecified computational search.

## What remains unresolved

The argument establishes a stronger necessary linear coefficient:
\[
\liminf_{n\to\infty}\frac{\chi_s'(K_n)}n\ge3.
\]
It does **not** distinguish between
\[
\chi_s'(K_n)=O(n)
\quad\text{and}\quad
\frac{\chi_s'(K_n)}n\longrightarrow\infty
\]
—or other unbounded-ratio behavior.

The packing count controls the second moment of color-class sizes, but supplies neither a linear-size construction nor an obstruction forcing the number of colors to be superlinear. Thus the original conjecture is not resolved here. The mathematical lower-bound argument is complete; its novelty requires a literature check.
