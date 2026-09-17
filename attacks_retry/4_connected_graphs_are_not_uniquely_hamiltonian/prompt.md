Attack the following open graph-theory problem.

Catalog id: 4_connected_graphs_are_not_uniquely_hamiltonian
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/4_connected_graphs_are_not_uniquely_hamiltonian/
Original entry: http://www.openproblemgarden.org/op/4_connected_graphs_are_not_uniquely_hamiltonian
Problem attributed to: Fleischner, Herbert (posted 2013-03-11)

=== Problem statement (OpenProblemGarden) ===
Title: 4-connected graphs are not uniquely hamiltonian
Conjecture Every $ 4 $ -connected graph with a Hamilton cycle has a second Hamilton cycle.

=== References listed by OpenProblemGarden ===
- *[F] H. Fleischner, Uniquely Hamiltonian graphs of minimum degree four,, J. Graph Theory, to appear.

=== Catalog page (statement + literature review) ===
4-connected graphs are not uniquely hamiltonian — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that every 4-connected Hamiltonian graph has a second Hamilton cycle remains open. Fleischner's companion paper (already cited in the OPG bibliography as 'to appear,' published 2014) constructs uniquely Hamiltonian graphs of minimum degree 4 but with connectivity only 2 or 3, confirming that 4-connectivity is the essential barrier. A 2023–2024 extension by Brinkmann and De Pauw further develops such constructions for many degree sequences while still not surpassing 3-connectivity.

 Cited literature (1)

 
 
 
partial Uniquely hamiltonian graphs for many sets of degrees
 (2023)
 

 
 Gunnar Brinkmann, Matthias De Pauw · arXiv preprint · arXiv:2304.08946

For all degree sets $M$ with minimum 4, except possibly $\{4\}$, $\{4,5\}$, and $\{4,6\}$, uniquely Hamiltonian graphs with exactly those vertex degrees exist; the best connectivity achieved is 3, leaving the 4-connected case of the conjecture untouched.
 

 

 Reviewer notes. The Fleischner 2014 J. Graph Theory paper (DOI 10.1002/jgt.21729) is the OPG-cited 'to appear' reference and is treated as background, not new progress. Wiley and Springer journal pages returned 403/redirect errors, preventing direct verification. The related Sheehan conjecture (second Hamilton cycle in 4-regular graphs) is also open. Brinkmann–De Pauw (arXiv:2304.08946) was published in a journal in December 2024 but the journal name was not visible from the abstract page. Eppstein (arXiv:2510.18359, 2025) and Lancia et al. (arXiv:2112.05087, 2021) were verified but are not directly relevant to the 4-connected conjecture.

 
 Auto-reviewed 2026-05-07 with claude-sonnet-4-6 (web search enabled) · 237s.
 

Conjecture. Every $ 4 $ -connected graph with a Hamilton cycle has a second Hamilton cycle.

Bibliography

★ [F]
 H. Fleischner, Uniquely Hamiltonian graphs of minimum degree four,, J. Graph Theory, to appear.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any counterexample must satisfy n ≥ 3δ ≥ 12 and Δ ≤ n − 2δ + 3, and deleting its unique Hamilton cycle must leave at least three components.",
  "would_publish": false,
  "caveats": "The conjecture is not resolved; these self-contained partial bounds are not claimed to be new or best known."
}
```

## 1. Partial result

All graphs below are finite and simple, and Hamilton cycles are distinguished by their edge sets.

I obtain the following necessary conditions for a counterexample. The argument uses minimum degree, rather than the full force of 4-connectivity.

**Theorem.** Let \(G\) be uniquely Hamiltonian, with unique Hamilton cycle \(C\), minimum degree \(\delta\ge 4\), maximum degree \(\Delta\), and \(n\) vertices. Put
\[
H=(V(G),E(G)\setminus E(C)).
\]
Then:

1. \(H\) has at least three connected components.
2. If \(H\) has exactly two odd-order components, there is no edge of \(G\) between those two components.
3. \(\displaystyle \Delta\le n-2\delta+3\).
4. \(\displaystyle n\ge 3\delta\).

Consequently, the proposed conjecture holds for a 4-connected Hamiltonian graph satisfying either
\[
n<3\delta
\qquad\text{or}\qquad
\Delta\ge n-2\delta+4.
\]
In particular, it holds when \(n\le 11\), or when the graph has a vertex of degree at least \(n-4\).

I give complete proofs, but make no claim that these bounds improve existing literature or computational bounds.

---

## 2. A rotation-parity lemma

**Lemma 1.** Let \(J\) be a graph with an edge \(uv\). If every vertex outside \(\{u,v\}\) has odd degree, then the number of Hamilton cycles containing \(uv\) is even.

**Proof.** Form an auxiliary graph whose vertices are the oriented Hamilton paths
\[
P=(p_1,p_2,\ldots,p_n),\qquad p_1=u,\quad p_2=v.
\]
Whenever \(p_np_i\in E(J)\), with \(2\le i\le n-2\), join \(P\) to
\[
(p_1,\ldots,p_i,p_n,p_{n-1},\ldots,p_{i+1}).
\]
These rotations are reversible, and different choices of \(i\) give different paths. Thus
\[
d_{\mathrm{aux}}(P)
=d_J(p_n)-1-\mathbf 1_{\{up_n\in E(J)\}}.
\]
Because \(p_n\notin\{u,v\}\), its degree in \(J\) is odd. Therefore \(P\) has odd auxiliary degree precisely when \(up_n\in E(J)\).

The latter paths correspond bijectively to Hamilton cycles containing \(uv\): orient such a cycle to start with \(u,v\), and delete its final edge back to \(u\). The handshaking lemma now gives the required evenness. \(\square\)

We also need a basic parity-subgraph fact.

**Lemma 2.** If \(Q\) is connected and \(T\subseteq V(Q)\) has even cardinality, then \(Q\) has a spanning subgraph whose odd-degree vertices are exactly \(T\).

**Proof.** Root a spanning tree of \(Q\). Include a parent–child edge precisely when the subtree rooted at the child contains an odd number of vertices of \(T\). The resulting degrees have the prescribed parity. \(\square\)

---

## 3. Restrictions on the chord components

The next criterion does not require a minimum-degree assumption.

**Proposition 3.** Let \(C\) be a Hamilton cycle of \(G\), and let \(H=G-E(C)\). Then \(G\) has a second Hamilton cycle in any of the following situations:

- \(H\) has no odd-order component;
- \(H\) has exactly one odd-order component;
- \(H\) has exactly two odd-order components, and some edge of \(C\) joins them.

**Proof.** Choose an exceptional set \(S\) as follows:

- \(S=\varnothing\) in the first case;
- \(S=\{x\}\), with \(x\) in the unique odd-order component, in the second;
- \(S=\{x,y\}\), where \(xy\in E(C)\) joins the two odd-order components, in the third.

For every component \(Q\) of \(H\), the set
\[
V(Q)\setminus S
\]
has even cardinality. By Lemma 2, choose \(F\subseteq H\) so that its odd-degree vertices are exactly \(V(G)\setminus S\).

The graph
\[
J=C\cup F
\]
has odd degree at every vertex outside \(S\). In the three cases, apply Lemma 1 respectively to an arbitrary edge of \(C\), an edge of \(C\) incident with \(x\), or the edge \(xy\). Since \(C\) is counted, there must be another Hamilton cycle. It also belongs to \(G\). \(\square\)

If \(H\) had at most two components, Proposition 3 would always apply: when both components have odd order, \(C\) necessarily has an edge between them. This proves conclusion 1 of the theorem.

For conclusion 2, suppose there are exactly two odd-order components. Proposition 3 forbids a \(C\)-edge between them. By definition there is no \(H\)-edge between distinct components either. Thus there is no \(G\)-edge between them.

### The maximum-degree bound

Every vertex has exactly two incident edges in \(C\), so
\[
\delta(H)=\delta-2.
\]
Consequently, every component of \(H\) has at least \(\delta-1\) vertices.

Let \(Q\) contain a vertex of maximum degree in \(G\). There are at least two other components, whence
\[
|Q|\le n-2(\delta-1).
\]
It follows that
\[
\Delta
\le (|Q|-1)+2
\le n-2\delta+3.
\]
This proves conclusion 3.

---

## 4. A useful consecutive-block observation

The following lets us handle certain configurations with three odd-order chord components.

**Lemma 4.** Suppose a Hamiltonian graph \(J\) has a nonempty proper block \(S\) of consecutive vertices on a Hamilton cycle \(C\), with at least two vertices outside \(S\). If

- every vertex of \(S\) has degree two in \(J\), and
- every vertex outside \(S\) has odd degree in \(J\),

then \(J\) has a second Hamilton cycle.

**Proof.** Write the corresponding segment of \(C\) as
\[
a,s_1,\ldots,s_t,b.
\]
Replace this segment, including its internal vertices, by
\[
a,x,y,b,
\]
where \(x,y\) are new vertices. Call the resulting graph \(J'\).

Every vertex of \(J'\) outside \(\{x,y\}\) has odd degree. Lemma 1 shows that \(J'\) has an even number of Hamilton cycles containing \(xy\), and at least one exists.

Since \(x\) and \(y\) have degree two, every such cycle uses the entire path \(a,x,y,b\). Replacing that path by the original segment gives a bijection with the Hamilton cycles of \(J\). Hence \(J\) has at least two. \(\square\)

In particular, suppose \(H\) has exactly three components, all of odd order. If three consecutive vertices of \(C\) lie one in each component, and deleting each chosen vertex leaves its component connected, then \(G\) has a second Hamilton cycle.

Indeed, after those three deletions, each remaining component is connected and has even order. Use Lemma 2 to choose a chord subgraph with odd degree at every remaining vertex and no edges incident with the three chosen vertices. Adding \(C\) produces exactly the situation of Lemma 4.

---

## 5. Proof that \(n\ge 3\delta\)

Suppose, for a contradiction, that \(G\) is uniquely Hamiltonian and
\[
n\le 3\delta-1.
\]
Set
\[
r=\delta-1\ge 3.
\]
Every component of \(H\) has order at least \(r\), and there are at least three components. Since
\[
4r>3r+2,
\]
there are exactly three components. Up to permutation, their orders must be one of
\[
(r,r,r),\qquad
(r,r,r+1),\qquad
(r,r+1,r+1),\qquad
(r,r,r+2).
\tag{1}
\]

Any component of order \(r\) is \(K_r\), because its minimum degree in \(H\) is at least \(r-1\).

### Case A: \(r\) is even

Proposition 3 immediately excludes every list in (1) except
\[
(r,r+1,r+1).
\]
Let \(A\) be the component of order \(r\), and \(B,D\) the two odd-order components.

There is no \(C\)-edge between \(B\) and \(D\). Moreover, a vertex of \(B\) has at most one nonneighbor within \(B\) in \(H\), since
\[
d_{H[B]}(v)\ge r-1=|B|-2.
\]
An internal \(C\)-neighbor must be such a nonneighbor in \(H\). Thus every vertex of \(B\) has at least one incident \(C\)-edge leaving \(B\). The same holds for \(D\).

All these edges go to \(A\), giving at least
\[
2(r+1)
\]
edges of \(C\) incident with \(A\). But \(C\) has total degree \(2r\) on \(A\), a contradiction.

### Case B: \(r\) is odd

The list \((r,r+1,r+1)\) has only one odd-order component, so Proposition 3 excludes it.

For the list \((r,r,r+1)\), the two order-\(r\) components \(A,B\) are odd cliques. There is no \(C\)-edge between them. Nor can \(C\) have an edge within either clique, because all such edges already belong to \(H\).

Hence all \(4r\) cycle-edge incidences at \(A\cup B\) go to the remaining component, which has only \(2(r+1)\) available cycle-edge incidences. This is impossible.

It remains to consider
\[
(r,r,s),\qquad s\in\{r,r+2\}.
\]
All three orders are odd. Let \(A,B\) be the order-\(r\) cliques and \(D\) the remaining component.

There must be a \(C\)-edge between \(A\) and \(B\). Otherwise all \(4r\) cycle-edge incidences at \(A\cup B\) would go to \(D\), whereas
\[
2s\le 2r+4<4r.
\]

Choose a maximal consecutive block of \(C\) contained in \(A\cup B\) that contains such an edge. Its vertices alternate between \(A\) and \(B\), and its length is at least two. Its two boundary vertices lie in \(D\) and are distinct.

I claim that at least one of these boundary vertices is not a cut vertex of \(H[D]\).

- If \(s=r\), then \(H[D]=K_r\), so every vertex works.
- Suppose \(s=r+2\). If \(z\) is a cut vertex, every component of \(H[D]-z\) has at least \(r-1\) vertices: a vertex in such a component has neighbors only within that component and possibly at \(z\). Therefore
  \[
  r+1=|D|-1\ge 2(r-1),
  \]
  forcing \(r\le3\).
- Since \(r\ge3\) is odd, the only remaining possibility is \(r=3\), \(s=5\). A connected five-vertex graph of minimum degree at least two with a cut vertex must consist of two triangles sharing that cut vertex. In particular, it has only one cut vertex.

Thus one of the two distinct boundary vertices, say \(d\), is not a cut vertex. At that end of the block, we obtain three consecutive vertices of \(C\), one each in \(D,A,B\). Deleting the selected vertices from \(A\) and \(B\) leaves even-order cliques; deleting \(d\) from \(D\) leaves a connected even-order graph.

The consequence of Lemma 4 established above now supplies a second Hamilton cycle—a final contradiction.

All possibilities in (1) have been excluded. Hence
\[
n\ge 3r+3=3\delta.
\]
This proves conclusion 4 and completes the partial theorem. \(\square\)

---

## 6. The remaining gap

These arguments do **not** establish that a uniquely Hamiltonian graph must have a vertex cut of size at most three.

There is a precise limitation to the basic parity construction. For any \(F\subseteq H\) and any component \(Q\) of \(H\),
\[
\bigl|\{v\in Q:d_{C\cup F}(v)\text{ is even}\}\bigr|
\equiv |Q|\pmod 2.
\]
Thus every odd-order chord component necessarily contributes an even-degree vertex to \(C\cup F\). With three or more such components, one cannot simply arrange that all vertices outside the endpoints of one cycle edge have odd degree. The consecutive-block argument overcomes this only in particular configurations.

The unresolved part of this attack therefore includes sparse 4-connected graphs with sufficiently many vertices and several odd-order chord components. The proof above supplies necessary conditions on a counterexample, but neither produces one nor rules out that remaining class.
