Attack the following open graph-theory problem.

Catalog id: unit_vector_flows
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/unit_vector_flows/
Original entry: http://www.openproblemgarden.org/op/unit_vector_flows
Problem attributed to: Jain, Kamal (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Unit vector flows
Conjecture For every graph $ G $ without a bridge , there is a flow $ \phi : E(G) \rightarrow S^2 = \{ x \in {\mathbb R}^3 : |x| = 1 \} $ . Conjecture There exists a map $ q:S^2 \rightarrow \{-4,-3,-2,-1,1,2,3,4\} $ so that antipodal points of $ S^2 $ receive opposite values, and so that any three points which are equidistant on a great circle have values which sum to zero.

=== Discussion / context (OpenProblemGarden) ===
The main interest in these two conjectures is that together they imply Tutte's 5-flow conjecture . This follows easily from the fact that the 5-flow conjecture can be reduced to cubic graphs without bridges, and for such a graph $ G $ , the composition of the maps $ \phi $ and $ q $ (given by the above conjectures) is a nowhere-zero 5-flow. There are a couple of easy partial results toward the first conjecture which follow from well-known flow/cycle-cover results. First, Tutte showed that every graph with a nowhere-zero 4-flow has a list of three 2-flows $ f_1,f_2,f_3 : E(G) \to \{-1,0,1\} $ so that every edge is in the support of exactly two of these flows. Combining these flows and normalizing appropriately gives an $ S^2 $ -flow. Bermond, Jackson, and Jaeger [BJJ] showed that every graph with no bridge has a list of seven 2-flows so that every edge is in the support of exactly four of these flows. Combining these and normalizing appropriately gives an $ S^6 $ -flow. It seems likely that a graph has an $ S^1 $ -flow if and only if it has a nowhere-zero 3-flow. The "if" direction of this implication isn't hard to show and the "only if" direction looks quite possible. A dual concept to that of a flow is that of a tension. Observe that a graph $ G $ has a $ S^n $ tension if and only if can be embedded in $ {\mathbb R}^{n+1} $ so that all edges are unit length line segments. Such embeddings have received some attention over the years. In particular, there is considerable interest in finding the best possible upper bound on the chromatic number of graphs which embed in $ {\mathbb R}^2 $ in this manner. This is Hadwinger-Nelson problem on coloring the plane.

=== References listed by OpenProblemGarden ===
- [BJJ] J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MRhref{0735197}
- [T54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
- [T66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet

=== Catalog page (statement + literature review) ===
Unit vector flows — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Jain's second conjecture—that a map $q:S^2\to\{-4,-3,-2,-1,1,2,3,4\}$ with the required properties exists—was disproved in March 2026 by Ulyanov, who exhibited explicit point sets on $S^2$ that force the additional values $\pm 5$. The first conjecture (every bridgeless graph admits a flow $\phi:E(G)\to S^2$) remains open, though partial results since 2023 establish geometric characterisations and bounds on related $d$-dimensional flow numbers.

 Cited literature (4)

 
 
 
partial On $d$-dimensional nowhere-zero $r$-flows on a graph
 (2023)
 

 
 Davide Mattiolo, Giuseppe Mazzuoccolo, Jozef Rajník, Gloria Tabarelli · arXiv preprint · arXiv:2304.14231

Proves $\phi_2(G)\le 1+\sqrt{5}$ for all bridgeless graphs and shows the oriented 5-cycle double cover conjecture would imply the bound $\phi_2(G)\le\tau^2$ (golden ratio squared), giving the first quantitative upper bounds for 2-dimensional unit-vector flows.
 

 
 
partial Geometric description of $d$-dimensional flows of a graph
 (2025)
 

 
 Davide Mattiolo, Giuseppe Mazzuoccolo, Jozef Rajník, Gloria Tabarelli · arXiv preprint · arXiv:2510.19411

Establishes that existence of a suitable cycle double cover is equivalent to the graph admitting a geometrically constructed $(r,d)$-nowhere-zero flow, linking the first unit-vector flows conjecture to the cycle double cover programme.
 

 
 
partial 2-dimensional unit vector flows
 (2026)
 

 
 Hussein Houdrouge, Bobby Miraftab, Pat Morin · arXiv preprint · arXiv:2602.21526 · doi:10.48550/arXiv.2602.21526

Gives a geometric characterisation of cubic graphs that admit an $S^2$-flow (i.e., satisfy Jain's first conjecture) and shows this class is closed under specific composition operations, extending algebraic rank methods from $S^1$-flows to $S^2$-flows.
 

 
 
counterexample Graph Puzzles II.1: Counterexamples to Jain's Second Unit Vector Flows Conjecture
 (2026)
 

 
 Nikolay Ulyanov · arXiv preprint · arXiv:2603.23328

Constructs explicit point sets on $S^2$ (including one derived from the icosidodecahedron) that are counterexamples to Jain's second conjecture: these sets require the additional values $\pm 5$, so no map $q:S^2\to\{-4,-3,-2,-1,1,2,3,4\}$ with the required antipodal and great-circle-sum properties exists.
 

 

 Reviewer notes. Jain's second conjecture is definitively refuted (Ulyanov 2026), closing off the specific two-conjecture route to Tutte's 5-flow conjecture. Jain's first conjecture (S²-flows for all bridgeless graphs) remains open and is the active focus of the 2026 Houdrouge–Miraftab–Morin preprint. The 2023 and 2025 Mattiolo et al. papers work in the more general (r,d)-nowhere-zero flow setting rather than targeting the S² conjecture directly. No journal-published versions of the 2023–2026 arXiv papers were confirmed.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For every graph $ G $ without a bridge , there is a flow $ \phi : E(G) \rightarrow S^2 = \{ x \in {\mathbb R}^3 : |x| = 1 \} $ .

Conjecture. There exists a map $ q:S^2 \rightarrow \{-4,-3,-2,-1,1,2,3,4\} $ so that antipodal points of $ S^2 $ receive opposite values, and so that any three points which are equidistant on a great circle have values which sum to zero.

Keywords:
nowhere-zero flow

Discussion

The main interest in these two conjectures is that together they imply Tutte's 5-flow conjecture . This follows easily from the fact that the 5-flow conjecture can be reduced to cubic graphs without bridges, and for such a graph $ G $ , the composition of the maps $ \phi $ and $ q $ (given by the above conjectures) is a nowhere-zero 5-flow. There are a couple of easy partial results toward the first conjecture which follow from well-known flow/cycle-cover results. First, Tutte showed that every graph with a nowhere-zero 4-flow has a list of three 2-flows $ f_1,f_2,f_3 : E(G) \to \{-1,0,1\} $ so that every edge is in the support of exactly two of these flows. Combining these flows and normalizing appropriately gives an $ S^2 $ -flow. Bermond, Jackson, and Jaeger [BJJ] showed that every graph with no bridge has a list of seven 2-flows so that every edge is in the support of exactly four of these flows. Combining these and normalizing appropriately gives an $ S^6 $ -flow. It seems likely that a graph has an $ S^1 $ -flow if and only if it has a nowhere-zero 3-flow. The "if" direction of this implication isn't hard to show and the "only if" direction looks quite possible. A dual concept to that of a flow is that of a tension. Observe that a graph $ G $ has a $ S^n $ tension if and only if can be embedded in $ {\mathbb R}^{n+1} $ so that all edges are unit length line segments. Such embeddings have received some attention over the years. In particular, there is considerable interest in finding the best possible upper bound on the chromatic number of graphs which embed in $ {\mathbb R}^2 $ in this manner. This is Hadwinger-Nelson problem on coloring the plane.

Bibliography

 [BJJ]
 J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MRhref{0735197}

 [T54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
 MathSciNet

 [T66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 5-flow conjecture
 partial
 The source node contains both conjectures of the OPG entry, whose context states verbatim that 'together they imply Tutte's 5-flow conjecture.' The reduction is standard: the 5-flow conjecture reduces to bridgeless cubic graphs; for such G, an S²-flow φ gives at each vertex three unit vectors summing to zero, hence coplanar at mutual 120° angles, i.e., equidistant on a great circle. Composing φ with the map q of the second conjecture yields values in {±1,...,±4} summing to zero at every vertex (antipodality makes this orientation-consistent), i.e., a nowhere-zero 5-flow. Note the implication needs both conjectures of the entry, which the source node bundles.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit construction gives an S^2-flow for every generalized Petersen graph and for a larger family of two-layer cubic graphs over finite abelian groups.",
  "would_publish": false,
  "caveats": "The unrestricted first conjecture is not resolved; novelty and the catalog's reported 2026 results have not been independently verified."
}
```

## 1. Scope

I focus on the first conjecture. The supplied catalog reports a refutation of the second conjecture, but I have not independently verified that report.

The result below is a self-contained special case of the first conjecture. It includes all generalized Petersen graphs, including the Petersen graph itself. I also give an explicit bridgeless graph showing that a natural symmetry-based extension of the construction cannot work universally.

Identify \(\mathbb R^3\) with \(\mathbb C\times\mathbb R\). An \(S^2\)-flow on an oriented graph assigns each edge a vector of Euclidean norm one, with
\[
\sum_{e\text{ leaving }v}\phi(e)
-
\sum_{e\text{ entering }v}\phi(e)=0
\]
at every vertex.

## 2. A family admitting explicit unit-vector flows

Let \(A\) be a finite abelian group, written additively, and let \(s,t\in A\setminus\{0\}\).

Define \(G(A;s,t)\) with vertices
\[
\{u_g,v_g:g\in A\}
\]
and the following indexed, oriented edges:
\[
e_g:u_g\longrightarrow u_{g+s},\qquad
f_g:v_g\longrightarrow v_{g+t},\qquad
m_g:u_g\longrightarrow v_g.
\]

Edges with different indices are distinct. Thus an element of order two produces parallel edges in its layer. When both \(s\) and \(t\) have order at least three, this is a simple cubic graph.

### Theorem
For every finite abelian group \(A\) and every nonzero \(s,t\in A\), the graph \(G(A;s,t)\) admits an \(S^2\)-flow.

The key is to choose a character that moves both \(s\) and \(t\) sufficiently far around the unit circle.

### Lemma
There is a character
\[
\chi:A\longrightarrow \{z\in\mathbb C:|z|=1\}
\]
such that
\[
|1-\chi(s)|\ge 1,\qquad |1-\chi(t)|\ge 1.
\]

#### Proof

For an element \(x\in A\) of order \(q\), the values \(\chi(x)\), as \(\chi\) ranges over the character group \(\widehat A\), are uniformly distributed among the \(q\)-th roots of unity. This follows from the elementary fact that every character of the cyclic subgroup \(\langle x\rangle\) extends to \(A\).

A \(q\)-th root \(e^{2\pi i j/q}\) satisfies
\[
|1-e^{2\pi i j/q}|\ge 1
\]
exactly when
\[
\frac q6\le j\le\frac{5q}{6},
\qquad 0\le j<q.
\]
Consequently, the number of acceptable roots is
\[
N(q)=q+1-2\left\lceil\frac q6\right\rceil.
\]
Here
\[
N(2)=1,\qquad N(q)>\frac q2\quad(q\ge3).
\]
For \(q=3,4,5,6\), the latter assertion is immediate; for \(q>6\), it follows from
\[
N(q)>\frac{2q}{3}-1>\frac q2.
\]

Thus each of the two sets
\[
X_s=\{\chi:|1-\chi(s)|\ge1\},\qquad
X_t=\{\chi:|1-\chi(t)|\ge1\}
\]
contains at least half the characters, and contains strictly more than half unless the corresponding element has order two. If at least one of \(s,t\) has order greater than two, their intersection is nonempty.

It remains to consider the case in which both have order two. We need a character with
\[
\chi(s)=\chi(t)=-1.
\]
Choose \(\chi_s\) with \(\chi_s(s)=-1\). If \(\chi_s(t)=-1\), we are done. Otherwise choose \(\chi_t\) with \(\chi_t(t)=-1\). Either \(\chi_t(s)=-1\), or the product \(\chi_s\chi_t\) has value \(-1\) on both elements. \(\square\)

### Proof of the theorem

Choose \(\chi\) as in the lemma, and put
\[
\alpha=-\frac{1}{1-\chi(s)^{-1}},
\qquad
\beta=\frac{1}{1-\chi(t)^{-1}}.
\]
The lemma implies
\[
|\alpha|\le1,\qquad |\beta|\le1.
\]
Therefore the real numbers
\[
h_s=\sqrt{1-|\alpha|^2},
\qquad
h_t=\sqrt{1-|\beta|^2}
\]
are well defined.

Assign
\[
\boxed{
\begin{aligned}
\phi(e_g)&=(\alpha\chi(g),h_s),\\
\phi(f_g)&=(\beta\chi(g),h_t),\\
\phi(m_g)&=(\chi(g),0).
\end{aligned}}
\]

Every assigned vector has norm one. For example,
\[
\|\phi(e_g)\|^2
=|\alpha\chi(g)|^2+h_s^2
=|\alpha|^2+1-|\alpha|^2=1.
\]

At \(u_g\), the outgoing-minus-incoming sum is
\[
\begin{aligned}
\phi(e_g)-\phi(e_{g-s})+\phi(m_g)
&=\left(
\chi(g)\bigl[\alpha(1-\chi(s)^{-1})+1\bigr],\,0
\right)\\
&=(0,0).
\end{aligned}
\]
At \(v_g\), it is
\[
\begin{aligned}
\phi(f_g)-\phi(f_{g-t})-\phi(m_g)
&=\left(
\chi(g)\bigl[\beta(1-\chi(t)^{-1})-1\bigr],\,0
\right)\\
&=(0,0).
\end{aligned}
\]
Thus \(\phi\) is an \(S^2\)-flow. This also covers the order-two cases with parallel edges. \(\square\)

## 3. Consequences and an effective construction

### Generalized Petersen graphs

With the usual notation,
\[
GP(n,k)=G(\mathbb Z_n;1,k),
\qquad n\ge3,\quad 1\le k<n/2.
\]
Hence:

### Corollary
Every generalized Petersen graph admits an \(S^2\)-flow.

More generally, the same holds for every graph \(G(\mathbb Z_n;a,b)\) with nonzero steps \(a,b\), using the indexed-edge convention above.

The construction is effective without numerical feasibility testing. Write \([x]_n\) for the representative of \(x\bmod n\) in \(\{0,\ldots,n-1\}\). Scan \(r=0,\ldots,n-1\) until
\[
n\le 6[ra]_n\le5n,
\qquad
n\le 6[rb]_n\le5n.
\]
The lemma guarantees such an \(r\). Then use
\[
\chi(g)=e^{2\pi i rg/n}
\]
in the displayed flow formula. All resulting coordinates are algebraic.

For example, for the Petersen graph \(GP(5,2)\), take
\[
z=e^{2\pi i/5},\qquad \chi(g)=z^g.
\]
The formula uses
\[
\alpha=-\frac1{1-z^{-1}},
\qquad
\beta=\frac1{1-z^{-2}},
\]
and
\[
h_s=\sqrt{\frac{5-\sqrt5}{10}},
\qquad
h_t=\sqrt{\frac{5+\sqrt5}{10}}.
\]
Together with the indexed formula above, these specify all fifteen edge vectors exactly.

### Covers

The result also extends immediately to every finite graph cover of any graph in this family. Indeed, orient each lifted edge according to its image and pull back the flow. The local bijection defining a graph cover preserves the conservation equation at every vertex.

## 4. A genuine obstruction to extending the symmetry method

The construction above is equivariant: translation in the group acts on the flow vectors by rotations about a fixed axis. That feature cannot be imposed on arbitrary bridgeless cubic graphs.

Here is a fully explicit obstruction.

### Proposition
There is a simple bridgeless cubic graph on \(28\) vertices, with a specified automorphism of order seven, that admits no \(S^2\)-flow equivariant under that automorphism.

#### Construction

Use vertices
\[
c_i,\quad a_i^{(1)},\quad a_i^{(2)},\quad a_i^{(3)}
\qquad(i\in\mathbb Z_7).
\]
Add the edges
\[
m_i^{(j)}:c_i\longrightarrow a_i^{(j)}
\]
and
\[
e_i^{(j)}:a_i^{(j)}\longrightarrow a_{i+j}^{(j)},
\qquad j=1,2,3.
\]
Thus there are three disjoint \(7\)-cycles, together with seven vertices each joined to one vertex of each cycle.

The graph is simple and cubic. It is bridgeless: the cycle edges lie on their respective \(7\)-cycles, and every spoke lies on a cycle obtained by going through another layer and returning through its own layer.

Let \(T\) be the automorphism increasing every subscript by one.

By an equivariant flow, mean one for which there is an orthogonal matrix \(Q\) satisfying
\[
Q^7=I,\qquad \phi(T e)=Q\phi(e)
\]
for every oriented edge.

#### Proof of nonexistence

Suppose such a flow exists, and set
\[
x_j=\phi(e_0^{(j)}),\qquad
w_j=\phi(m_0^{(j)}).
\]
Conservation at \(a_0^{(j)}\) gives
\[
w_j=x_j-Q^{-j}x_j.
\]
Since both \(x_j\) and \(w_j\) have norm one,
\[
1\le \|I-Q^{-j}\|_{\mathrm{op}}
\qquad(j=1,2,3).
\]

An orthogonal matrix of order dividing seven is either the identity or a rotation through angle \(2\pi r/7\), for some \(r\in\{1,\ldots,6\}\). The identity is immediately impossible. In the rotation case,
\[
\|I-Q^{-j}\|_{\mathrm{op}}
=2\left|\sin\frac{\pi rj}{7}\right|.
\]
Thus all three residues
\[
r,\quad 2r,\quad 3r \pmod7
\]
must belong to
\[
\{2,3,4,5\}.
\]

No \(r\) works:

- \(r=1,6\) fails for \(j=1\);
- \(r=2,5\) fails for \(j=3\);
- \(r=3,4\) fails for \(j=2\).

This is a contradiction. \(\square\)

**This does not establish a counterexample to Jain’s conjecture.** It excludes only flows respecting the specified symmetry. In particular, one cannot average an arbitrary flow over the automorphism group and expect the unit-length conditions to survive.

## 5. What remains unresolved

The positive result covers a structured infinite family, and its finite covers, but there is no reduction here from arbitrary bridgeless graphs to that family.

The \(28\)-vertex example identifies a specific limitation of the method: even when a graph has a useful cyclic automorphism, an \(S^2\)-flow need not be obtainable equivariantly. It does not rule out unrestricted \(S^2\)-flows on that graph.

Accordingly, this is a **partial result**, not a proof or disproof of the universal first conjecture.
