Attack the following open graph-theory problem.

Catalog id: intersecting_two_perfect_matchings
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Matchings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/intersecting_two_perfect_matchings/
Original entry: http://www.openproblemgarden.org/op/intersecting_two_perfect_matchings
Problem attributed to: Macajova, Edita, Skoviera, Martin (posted 2007-08-30)

=== Problem statement (OpenProblemGarden) ===
Title: The intersection of two perfect matchings
Conjecture Every bridgeless cubic graph has two perfect matchings $ M_1 $ , $ M_2 $ so that $ M_1 \cap M_2 $ does not contain an odd edge-cut.

=== Discussion / context (OpenProblemGarden) ===
Let $ G = (V,E) $ be a bridgeless cubic graph. A binary cycle (henceforth called cycle ) is a set $ C \subseteq E $ so that every vertex of $ (V,C) $ has even degree (equivalently, a cycle is any member of the binary cycle space). A postman join is a set $ J \subseteq E $ so that $ E \setminus J $ is a cycle. Note that since $ G $ is cubic, every perfect matching is a postman join. Next we state a well-known theorem of Jaeger in three equivalent forms. Theorem (Jaeger's 8-flow theorem) \item $ G $ has a nowhere-zero flow in the group $ {\mathbb Z}_2^3 $ . \item $ G $ has three cycles $ C_1,C_2,C_3 $ so that $ C_1 \cup C_2 \cup C_3 = E $ . \item $ G $ has three postman joins $ J_1,J_2,J_3 $ so that $ J_1 \cap J_2 \cap J_3 = \emptyset $ . The last of these statements is interesting, since The Berge Fulkerson Conjecture (if true) implies the following: Conjecture $ G $ has three perfect matchings $ M_1,M_2,M_3 $ so that $ M_1 \cap M_2 \cap M_3= \emptyset $ . So, we know that $ G $ has three postman joins $ J_1,J_2,J_3 $ with empty intersection, and it is conjectured that $ J_1,J_2,J_3 $ may be chosen so that each is a perfect matching, but now we see two statements in between the theorem and the conjecture. Namely, is it true that $ J_1,J_2,J_3 $ may be chosen so that one is a perfect matching? or two? The first of these was solved recently. Theorem (Macajova, Skoviera) $ G $ has two postman sets $ J_1,J_2 $ and one perfect matching $ M $ so that $ M \cap J_1 \cap J_2 = \emptyset $ The second of these asks for two perfect matchings $ M_1,M_2 $ and one postman join $ J $ so that $ M_1 \cap M_2 \cap J = \emptyset $ . It is an easy exercise to show that a set $ S \subseteq E $ contains a postman join if an only if $ S $ has nonempty intersection with every odd edge-cut. Therefore, finding two perfect matchings and one postman join with empty common intersection is precisely equivalent to the conjecture at the start of this page - find two perfect matchings whose intersection contains no odd edge-cut.

=== References listed by OpenProblemGarden ===
- * Edita Macajova, Martin Skoviera, Fano colourings of cubic graphs and the Fulkerson conjecture. Theoret. Comput. Sci. 349 (2005), no. 1, 112--120. MathSciNet

=== Catalog page (statement + literature review) ===
The intersection of two perfect matchings — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The Mácajová–Škoviera conjecture — that every bridgeless cubic graph has two perfect matchings $M_1, M_2$ with $M_1 \cap M_2$ containing no odd edge-cut — remains open. Fouquet and Vanherpe (2010) proved it for cubic graphs with few vertices and for traceable graphs. Related conjectures in the same research programme (notably Mazzuoccolo's conjecture that two perfect matchings whose deletion yields a bipartite subgraph, proved by Kardoš, Máčajová, and Zerafa in 2023) have since been resolved, but the original conjecture as stated is unresolved.

 Cited literature (2)

 
 
 
partial Mácajová and Škoviera Conjecture on Cubic Graphs
 (2010)
 

 
 Jean-Luc Fouquet, Jean-Marie Vanherpe · Discussiones Mathematicae Graph Theory · arXiv:0809.4839

Proves the conjecture for cubic graphs with a bounded number of vertices and gives a stronger result for traceable cubic graphs.
 

 
 
partial Disjoint odd circuits in a bridgeless cubic graph can be quelled by a single perfect matching
 (2023)
 

 
 František Kardoš, Edita Máčajová, Jean Paul Zerafa · Journal of Combinatorial Theory, Series B · arXiv:2204.10021

Proves Mazzuoccolo's conjecture that every bridgeless cubic graph admits two perfect matchings whose deletion yields a bipartite subgraph — a related result in the same research programme between Jaeger's 8-flow theorem and the Berge–Fulkerson conjecture, but distinct from the Mácajová–Škoviera conjecture about the intersection avoiding an odd edge-cut.
 

 

 Reviewer notes. The OPG page (openproblemgarden.org) was unreachable (ECONNREFUSED). The DMGT journal page for the Fouquet–Vanherpe article (dmgt.uz.zgora.pl) returned an SSL error and could not be verified. The Kardoš–Máčajová–Zerafa 2023 paper proves Mazzuoccolo's bipartite conjecture (G − M1 − M2 bipartite), which is at a different level in the hierarchy than the Mácajová–Škoviera conjecture (M1 ∩ M2 has no odd edge-cut). No post-2010 paper specifically resolving the Mácajová–Škoviera conjecture was found in 5 searches; it is assessed as still open with partial results.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Every bridgeless cubic graph has two perfect matchings $ M_1 $ , $ M_2 $ so that $ M_1 \cap M_2 $ does not contain an odd edge-cut.

Keywords:
cubic · nowhere-zero flow · perfect matching

Discussion

Let $ G = (V,E) $ be a bridgeless cubic graph. A binary cycle (henceforth called cycle ) is a set $ C \subseteq E $ so that every vertex of $ (V,C) $ has even degree (equivalently, a cycle is any member of the binary cycle space). A postman join is a set $ J \subseteq E $ so that $ E \setminus J $ is a cycle. Note that since $ G $ is cubic, every perfect matching is a postman join. Next we state a well-known theorem of Jaeger in three equivalent forms. Theorem (Jaeger's 8-flow theorem) \item $ G $ has a nowhere-zero flow in the group $ {\mathbb Z}_2^3 $ . \item $ G $ has three cycles $ C_1,C_2,C_3 $ so that $ C_1 \cup C_2 \cup C_3 = E $ . \item $ G $ has three postman joins $ J_1,J_2,J_3 $ so that $ J_1 \cap J_2 \cap J_3 = \emptyset $ . The last of these statements is interesting, since The Berge Fulkerson Conjecture (if true) implies the following: Conjecture $ G $ has three perfect matchings $ M_1,M_2,M_3 $ so that $ M_1 \cap M_2 \cap M_3= \emptyset $ . So, we know that $ G $ has three postman joins $ J_1,J_2,J_3 $ with empty intersection, and it is conjectured that $ J_1,J_2,J_3 $ may be chosen so that each is a perfect matching, but now we see two statements in between the theorem and the conjecture. Namely, is it true that $ J_1,J_2,J_3 $ may be chosen so that one is a perfect matching? or two? The first of these was solved recently. Theorem (Macajova, Skoviera) $ G $ has two postman sets $ J_1,J_2 $ and one perfect matching $ M $ so that $ M \cap J_1 \cap J_2 = \emptyset $ The second of these asks for two perfect matchings $ M_1,M_2 $ and one postman join $ J $ so that $ M_1 \cap M_2 \cap J = \emptyset $ . It is an easy exercise to show that a set $ S \subseteq E $ contains a postman join if an only if $ S $ has nonempty intersection with every odd edge-cut. Therefore, finding two perfect matchings and one postman join with empty common intersection is precisely equivalent to the conjecture at the start of this page - find two perfect matchings whose intersection contains no odd edge-cut.

Bibliography

★ [?]
 Edita Macajova, Martin Skoviera, Fano colourings of cubic graphs and the Fulkerson conjecture. Theoret. Comput. Sci. 349 (2005), no. 1, 112--120. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 The Berge-Fulkerson conjecture
 partial
 Rigorous: any perfect matching meets every odd edge-cut delta(X) in an odd (hence >=1) number of edges, since the odd set X cannot be perfectly matched internally. Given a Fulkerson cover M1..M6 with every edge in exactly two matchings, if an odd cut C were contained in M1 cap M2, every edge of C would already have both its memberships used by M1 and M2, forcing M3 cap C to be empty -- contradicting that the perfect matching M3 meets C. So M1 cap M2 contains no odd edge-cut, which is exactly the target. Direction correct: Berge-Fulkerson is the stronger statement.
 

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
  "one_line": "A fractional-matching argument proves the conjecture for fewer than 70 vertices and gives broader sufficient conditions, while a sharp construction shows that the first matching cannot be prescribed arbitrarily.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled, and novelty of the partial results is not claimed."
}
```

## 1. Results obtained

I do not obtain a proof or counterexample for the unrestricted conjecture. I prove:

1. Every bridgeless cubic graph with at most **68 vertices** satisfies the conjecture. In fact, such a graph has three perfect matchings with empty common intersection.
2. A parameterized sufficient condition involving odd cuts contained in a chosen perfect matching.
3. An order-independent sufficient condition involving the number of cycles in its complementary 2-factor.
4. For the variant in which the first perfect matching is prescribed:
   - every instance on at most **28 vertices** is positive;
   - this order bound is sharp, with an explicit **30-vertex** negative instance;
   - the decision problem is NP-complete.

The last item is **not** a counterexample to the original conjecture.

All graphs below are finite and loopless; parallel edges cause no difficulty. It suffices to work with connected graphs, since the conclusions combine componentwise.

## 2. A useful exact certificate

Write \(\delta(X)\) for the edges with exactly one endpoint in \(X\). Cubicity gives
\[
|\delta(X)|\equiv |X|\pmod 2.
\]

**Lemma 1.** For any \(I\subseteq E(G)\), the following are equivalent:

- \(I\) contains no odd edge-cut;
- every component of \(G-I\) has even order.

**Proof.** If \(K\) is an odd-order component of \(G-I\), then
\(\delta(V(K))\subseteq I\), and this cut has odd size.

Conversely, if an odd cut \(\delta(X)\) is contained in \(I\), then \(X\) is a union of components of \(G-I\). Since \(|X|\) is odd, at least one of those components has odd order. \(\square\)

Thus a proposed pair of perfect matchings can be checked in linear time: delete their intersection and inspect component orders.

## 3. A fractional-matching criterion

I use the standard perfect-matching polytope theorem: the convex hull of perfect-matching incidence vectors is
\[
\left\{
x\in\mathbb R_{\ge0}^{E(G)}:
x(\delta(v))=1\ \text{for all }v,\quad
x(\delta(X))\ge1\ \text{for every odd }X
\right\}.
\]

Recall also that every perfect matching meets an odd cut in a positive odd number of edges.

### Parameterized lemma

**Lemma 2.** Let \(P\) be a perfect matching of a bridgeless cubic graph \(G\), and let \(q\ge3\) be odd. Suppose that \(P\) contains no odd edge-cut of size less than \(q\).

Then there is a perfect matching \(Q\) such that
\[
|P\cap Q|\le \left\lfloor\frac{|V(G)|}{2q}\right\rfloor,
\]
and every \(q\)-edge-cut contained in \(P\) meets \(Q\) exactly once. Moreover, \(Q\) can be chosen to meet every 3-edge-cut exactly once.

Consequently, \(P\cap Q\) contains no odd cut of size at most \(q\).

**Proof.** Define
\[
x_e=
\begin{cases}
1/q,&e\in P,\\[2mm]
(q-1)/(2q),&e\notin P.
\end{cases}
\]
At each vertex the incident weights sum to \(1\).

Consider an odd cut \(C\). Put
\[
c=|C|,\qquad k=|C\setminus P|.
\]
Since \(|C\cap P|\) and \(c\) are odd, \(k\) is even. Furthermore,
\[
x(C)=\frac{c}{q}+\frac{q-3}{2q}k.
\]

If \(k=0\), the hypothesis gives \(c\ge q\), so \(x(C)\ge1\). If \(k\ge2\), bridgelessness gives \(c\ge3\), and hence
\[
x(C)\ge\frac{c+q-3}{q}\ge1.
\]
Thus \(x\) belongs to the perfect-matching polytope.

Take a convex decomposition of \(x\) into perfect matchings. For a random matching \(Q\) drawn according to this decomposition,
\[
\mathbb E|P\cap Q|
=\sum_{e\in P}x_e
=\frac{|V(G)|}{2q}.
\]

If \(C\subseteq P\) is a \(q\)-edge-cut, then \(x(C)=1\). Every perfect matching meets \(C\) at least once, so every matching occurring with positive coefficient in the decomposition meets \(C\) exactly once.

Every 3-edge-cut is also tight. For \(q=3\), \(x\) is the constant vector \(1/3\). For \(q>3\), the hypothesis forces \(P\) to meet each 3-edge-cut once, and its \(x\)-weight is again \(1\).

Choosing a matching from the decomposition with intersection size no larger than the average proves the assertions. \(\square\)

**Corollary 3.** Under the hypotheses of Lemma 2, the desired pair exists whenever
\[
|V(G)|<2q(q+2).
\]

Indeed, any odd cut contained in \(P\cap Q\) would have size at least \(q+2\), whereas
\[
|P\cap Q|<q+2.
\]

### Obtaining \(q=5\) unconditionally

The constant vector \(x_e=1/3\) belongs to the perfect-matching polytope of every bridgeless cubic graph. Every 3-edge-cut has weight exactly \(1\). Therefore every matching in a convex decomposition of this vector meets every 3-edge-cut exactly once.

Choose one such matching \(P\). It contains no 3-edge-cut, so Lemma 2 applies with \(q=5\). We obtain a perfect matching \(Q\) satisfying
\[
|P\cap Q|\le\left\lfloor\frac{|V(G)|}{10}\right\rfloor,
\]
such that \(P\cap Q\) contains neither a 3-edge-cut nor a 5-edge-cut.

This proves:

**Theorem 4.** Every bridgeless cubic graph with at most \(68\) vertices satisfies the conjecture.

At that order, the intersection has at most six edges, while any odd cut it contains would have at least seven.

### A stronger conclusion at the same order

For the pair \(P,Q\) just constructed, define
\[
y_e=\frac{3-\mathbf1_P(e)-\mathbf1_Q(e)}7.
\]
The vertex equations hold. For an odd cut \(C\):

- if \(|C|=3\), both matchings meet it once, so \(y(C)=1\);
- if \(|C|=5\), they cannot both contain all of \(C\), and therefore
  \[
  |P\cap C|+|Q\cap C|\le8,
  \qquad y(C)\ge\frac{15-8}{7}=1;
  \]
- if \(|C|\ge7\), every edge has \(y_e\ge1/7\), so \(y(C)\ge1\).

Thus \(y\) is another fractional perfect matching. Writing \(I=P\cap Q\), a perfect matching \(R\) drawn from its decomposition satisfies
\[
\mathbb E|R\cap I|=\frac{|I|}{7}.
\]
When \(|V(G)|\le68\), this is at most \(6/7\). Some \(R\) therefore has
\[
P\cap Q\cap R=\varnothing.
\]

This proves the stronger triple-intersection conclusion in that order range.

### A connectivity application

If an edge-cut is contained in a matching, every vertex on either side has internal degree at least two. Both sides therefore contain cycles.

Consequently, if \(G\) has no cyclic odd cut smaller than \(q\), the hypothesis of Lemma 2 holds for **every** perfect matching \(P\). For example, every cyclically 6-edge-connected cubic graph on at most \(124\) vertices satisfies the conjecture: use \(q=7\) and
\[
124<2\cdot7\cdot9.
\]

## 4. A sufficient condition with no order bound

The same fractional point gives another criterion.

**Theorem 5.** Under the hypotheses of Lemma 2, suppose that \(G-P\) has at most \(q+1\) cycles. Then there is a perfect matching \(Q\) such that \(P\cap Q\) contains no odd edge-cut.

**Proof.** Contract each cycle of \(G-P\) to a vertex, retaining the edges of \(P\). The resulting multigraph \(K\) is connected. Let \(B\subseteq P\) correspond to a spanning tree of \(K\).

Draw \(Q\) from the decomposition of the fractional matching in Lemma 2. Each edge of \(B\) belongs to \(Q\) with probability \(1/q\), so
\[
\mathbb E|B\cap Q|=\frac{|B|}{q}\le1.
\]

If \(|B|<q\), some \(Q\) avoids \(B\). Then \(G-(P\cap Q)\) contains \(G-P\) together with all of \(B\), and is connected. Its order is even, so Lemma 1 applies.

It remains to consider \(|B|=q\). Suppose, for contradiction, that every matching in the decomposition is unsuccessful. No such matching can avoid \(B\), and the expectation above is \(1\). Hence every one meets \(B\) in exactly one edge.

Fix \(e\in B\). Deleting \(e\) partitions the spanning tree into two parts. Let \(U_e\) be the union of the original cycles belonging to one part, and put
\[
D_e=\delta_G(U_e).
\]
All edges of \(D_e\) belong to \(P\).

Whenever \(e\in Q\), all other edges of \(B\) survive in \(G-(P\cap Q)\). Thus each side of \(D_e\) is connected in that graph. If any edge of \(D_e\) survived, the whole graph would be connected and the pair would succeed. Consequently, under our contradiction assumption,
\[
e\in Q\quad\Longrightarrow\quad D_e\subseteq Q.
\]
Moreover, the two resulting components must be odd, so \(D_e\) is an odd cut.

Write \(c_e=|D_e|\). Since \(\Pr(e\in Q)=1/q\), and every perfect matching meets \(D_e\) at least once,
\[
\mathbb E|Q\cap D_e|
\ge \frac{c_e}{q}+\left(1-\frac1q\right)
>\frac{c_e}{q}.
\]
But every edge of \(D_e\subseteq P\) has marginal probability \(1/q\), giving the contradictory equality
\[
\mathbb E|Q\cap D_e|=\frac{c_e}{q}.
\]
\(\square\)

In particular:

- any perfect matching whose complementary 2-factor has at most **four cycles** can serve as the first matching;
- a perfect matching meeting every 3-edge-cut once and having at most **six complementary cycles** is sufficient.

## 5. Why an arbitrary first matching cannot be fixed

Consider the prescribed-first-matching problem:

> Given a bridgeless cubic graph \(G\) and a specified perfect matching \(P\), does there exist a perfect matching \(Q\) such that \(P\cap Q\) contains no odd edge-cut?

Lemma 2 with \(q=3\) proves that every such instance with fewer than \(30\) vertices is positive. The following construction shows that this is sharp.

### Triangle expansion

Let \(H\) be a bridgeless cubic graph. Replace every vertex \(v\) by a triangle with one vertex for each edge incident with \(v\). For every original edge \(uv\), join its corresponding triangle vertices. Call the resulting cubic graph \(T(H)\).

Let \(P\) consist of all these edges joining different triangles. It is a perfect matching.

The graph \(T(H)\) is bridgeless: triangle edges lie on triangles, and every edge joining triangles lies on a lifted cycle of \(H\).

For any perfect matching \(Q\) of \(T(H)\), the number of its external edges at a triangle is either one or three. Define
\[
S=\{e\in E(H):\text{the corresponding external edge is not in }Q\}.
\]
Then every vertex has degree zero or two in \(H[S]\). Thus \(H[S]\) is a disjoint union of cycles and isolated vertices.

All triangle edges remain in \(T(H)-(P\cap Q)\). Contracting the triangles gives exactly \(H[S]\). A component with \(t\) vertices in \(H[S]\) lifts to a component with \(3t\) vertices. Therefore Lemma 1 gives
\[
\begin{aligned}
P\cap Q\text{ contains no odd cut}
&\iff H[S]\text{ has only even-order components}\\
&\iff S\text{ is a spanning union of even cycles}.
\end{aligned}
\]

A cubic graph has a spanning union of even cycles exactly when it is 3-edge-colourable. Conversely, any such even 2-factor \(S\) produces \(Q\): use the external edges corresponding to \(E(H)\setminus S\), and in each triangle match the other two vertices internally.

Hence
\[
\boxed{
(T(H),P)\text{ is a positive prescribed-matching instance}
\iff H\text{ is 3-edge-colourable}.
}
\]

### An explicit 30-vertex negative instance

Take \(H\) to be the Petersen graph, with vertices \(u_i,v_i\), \(i\in\mathbb Z_5\), and edges
\[
u_iu_{i+1},\qquad v_iv_{i+2},\qquad u_iv_i.
\]

For completeness, its non-3-edge-colourability can be checked directly through its perfect matchings. A perfect matching uses one, three, or five spokes \(u_iv_i\). Three spokes are impossible: the two remaining indices would have to be adjacent both on the outer pentagon and on the inner pentagram.

With one spoke, rotation lets us assume it is \(u_0v_0\), and the matching is necessarily
\[
\{u_0v_0,u_1u_2,u_3u_4,v_1v_3,v_2v_4\}.
\]
Its complement consists of the two 5-cycles
\[
u_0u_1v_1v_4u_4u_0,
\qquad
u_2u_3v_3v_0v_2u_2.
\]
The matching consisting of all five spokes also has two complementary 5-cycles. These cases cover every perfect matching, so there is no even 2-factor.

Thus \(T(H)\) has \(30\) vertices, and its prescribed external matching \(P\) has **no** suitable partner \(Q\).

This disproves only the prescribed-first-matching variant. Theorem 4 guarantees that this same 30-vertex graph has a suitable pair when both matchings may be chosen.

### Complexity consequence

Using the classical NP-completeness of cubic 3-edge-colourability, the triangle-expansion equivalence proves NP-hardness of the prescribed-first-matching problem.

The restriction to bridgeless inputs causes no problem: a cubic graph with a bridge is not 3-edge-colourable, so such inputs can be sent to the fixed Petersen-based negative instance above. Membership in NP follows from Lemma 1.

Therefore the prescribed-first-matching problem is **NP-complete**, even for simple bridgeless cubic graphs.

The reduction uses prescribed matchings containing many 3-edge-cuts. It does not establish hardness, or a counterexample, for the more restricted choice of \(P\) used in the \(q=5\) argument.

## 6. Remaining gap

The unconditional construction produces two perfect matchings with
\[
|P\cap Q|\le |V(G)|/10
\]
and excludes odd cuts of sizes three and five from their intersection.

At \(70\) vertices, this still permits an intersection of seven edges containing a 7-edge-cut. The argument does not exclude that possibility, nor does it control larger odd cuts at arbitrary order. The few-cycle criterion resolves some additional graphs, but not all bridgeless cubic graphs.

Thus the original conjecture remains unresolved by this attack. The proved conclusions are the quantitative and structural sufficient conditions above, together with the sharp obstruction and complexity classification for prescribing the first matching.
