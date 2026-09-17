Attack the following open graph-theory problem.

Catalog id: three_4_flows_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/three_4_flows_conjecture/
Original entry: http://www.openproblemgarden.org/op/three_4_flows_conjecture
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: The three 4-flows conjecture
Conjecture For every graph $ G $ with no bridge , there exist three disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G \setminus A_i $ has a nowhere-zero 4-flow for $ 1 \le i \le 3 $ .

=== Discussion / context (OpenProblemGarden) ===
A graph $ G $ has a nowhere-zero 4-flow if and only if there exist disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G\A_i $ has a nowhere-zero 2-flow for $ 1 \le i \le 3 $ . Thus, the above conjecture is true with room to spare for such graphs. Since every 4-edge-connected graph and every 3- edge-colorable cubic graph has a nowhere-zero 4-flow, this conjecture is automatically true for these families. As with the 5-flow conjecture or the cycle double cover conjecture , establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable. This conjecture is a consequence of the Petersen coloring conjecture , and it implies the Orientable cycle four cover conjecture . The latter implication follows immediately from the fact that every graph with a nowhere-zero 4-flow has an orientable cycle double cover. Actually, it is possible that for every graph $ G $ with no cut-edge, there exist disjoint sets $ A_B_1,B_2 \subseteq E(G) $ with $ A \cup B_1 \cup B_2 = E(G) $ and so that $ G\B_1 $ and $ G\B_2 $ have nowhere-zero 3-flows and $ G\A $ has a nowhere-zero 2-flow. The Petersen graph has such a decomposition ( $ B_1 $ and $ B_2 $ should be alternate edges of some 8-circuit) and so does every graph with a nowhere-zero 4-flow. If this stronger statement is true, then it would imply the oriented eight cycle four cover conjecture.

=== References listed by OpenProblemGarden ===
- [J] F. Jaeger, On circular flows in graphs. Finite and infinite sets, Vol. I, II (Eger, 1981), 391--402, Colloq. Math. Soc. János Bolyai, 37, North-Holland, Amsterdam, 1984.. MathSciNet

=== Catalog page (statement + literature review) ===
The three 4-flows conjecture — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The three 4-flows conjecture, which asks for a partition of the edge set of every bridgeless graph into three sets each of which can be removed to leave a graph with a nowhere-zero 4-flow, remains open. No post-2007 paper resolving or substantially partially resolving this conjecture was found; the problem reduces to cubic snarks and is implied by the Petersen coloring conjecture, itself still open.

 Reviewer notes. The OPG page (openproblemgarden.org) returned ECONNREFUSED. Five search queries were run; none returned a paper specifically addressing the three 4-flows conjecture. The arXiv paper 2511.01556 (Mattiolo, Nov 2025) on removable edge subsets in graphs with nowhere-zero 4-flows is related but does not address the conjecture directly. The Petersen coloring conjecture (which implies the three 4-flows conjecture) and the orientable cycle four cover conjecture (which is implied by it) are both still open, confirming the problem likely remains unresolved. Confidence is medium rather than high because the specific conjecture did not appear in any indexed paper by name, making it difficult to rule out niche partial results.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. For every graph $ G $ with no bridge , there exist three disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G \setminus A_i $ has a nowhere-zero 4-flow for $ 1 \le i \le 3 $ .

Keywords:
nowhere-zero flow

Discussion

A graph $ G $ has a nowhere-zero 4-flow if and only if there exist disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G\A_i $ has a nowhere-zero 2-flow for $ 1 \le i \le 3 $ . Thus, the above conjecture is true with room to spare for such graphs. Since every 4-edge-connected graph and every 3- edge-colorable cubic graph has a nowhere-zero 4-flow, this conjecture is automatically true for these families. As with the 5-flow conjecture or the cycle double cover conjecture , establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable. This conjecture is a consequence of the Petersen coloring conjecture , and it implies the Orientable cycle four cover conjecture . The latter implication follows immediately from the fact that every graph with a nowhere-zero 4-flow has an orientable cycle double cover. Actually, it is possible that for every graph $ G $ with no cut-edge, there exist disjoint sets $ A_B_1,B_2 \subseteq E(G) $ with $ A \cup B_1 \cup B_2 = E(G) $ and so that $ G\B_1 $ and $ G\B_2 $ have nowhere-zero 3-flows and $ G\A $ has a nowhere-zero 2-flow. The Petersen graph has such a decomposition ( $ B_1 $ and $ B_2 $ should be alternate edges of some 8-circuit) and so does every graph with a nowhere-zero 4-flow. If this stronger statement is true, then it would imply the oriented eight cycle four cover conjecture.

Bibliography

 [J]
 F. Jaeger, On circular flows in graphs. Finite and infinite sets, Vol. I, II (Eger, 1981), 391--402, Colloq. Math. Soc. János Bolyai, 37, North-Holland, Amsterdam, 1984.. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 Petersen coloring conjecture
 partial
 The implication is stated explicitly in the target's OPG context: 'This conjecture is a consequence of the Petersen coloring conjecture.' The mechanism is standard: the Petersen coloring conjecture is equivalent to every bridgeless graph having a cycle-continuous map f to the Petersen graph; the Petersen graph's edge set partitions into three sets P_1,P_2,P_3 whose complements have nowhere-zero 4-flows, and the pullbacks A_i = f^{-1}(P_i) partition E(G) with G\A_i inheriting a nowhere-zero 4-flow (4-flows are a cycle-space property preserved under cycle-continuous preimages). Direction is correct: Petersen coloring is the stronger statement.
 

 
 related to
 5-flow conjecture
 partial
 The mention is a methodological analogy only: 'As with the 5-flow conjecture or the cycle double cover conjecture, establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable.' No implication is stated or derivable. Combining the 4-flows on G\A1 and G\A2 (which cover all of E(G) since A1,A2 are disjoint) yields only a nowhere-zero Z4xZ4-flow, i.e. a 16-flow, weaker than Seymour's unconditional 6-flow theorem, so the three-4-flows conjecture does not yield a 5-flow; conversely a nowhere-zero 5-flow gives no decomposition into three sets whose complements carry 4-flows. Both reduce to snarks and share the flow framework, so related_only.
 

 
 related to
 Cycle double cover conjecture
 partial
 The truncated mention is misleading: fetching the full CDC page shows 'the above conjecture would follow from The three 4-flows conjecture' refers to the ORIENTED CYCLE FOUR COVER conjecture, a separate weaker statement hosted on the same page, not the CDC node's statement. The three 4-flows page confirms: 'it implies the Orientable cycle four cover conjecture' (each edge lies in exactly two of the graphs G\A_i, each having an orientable CDC via its nowhere-zero 4-flow, summing to a 4-cover). A cycle four cover does not give a double cover, and no implication between three 4-flows and CDC proper is known in either direction; both reduce to non-3-edge-colorable cubic graphs and both follow from Petersen coloring, but that makes them related family members only.
 

 
 related to
 Cycle double cover conjecture
 partial
 The mention is the same analogy sentence (both reduce to non-3-edge-colorable cubic graphs). The genuine implication stated in the context goes from three-4-flows to the Orientable cycle FOUR cover conjecture, not to CDC: each G\A_i has a nowhere-zero 4-flow, hence an orientable cycle double cover, and since each edge lies in exactly two of the three subgraphs G\A_i, the union covers every edge exactly four times. A cycle 4-cover is already known unconditionally (Bermond-Jackson-Jaeger via Jaeger's 8-flow theorem), so this route does not give a double cover, and no implication between three-4-flows and CDC is stated or standard in either direction. Hence related_only.
 

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
  "one_line": "A cycle-doubling construction gives the required partition for every flower snark and a larger explicit class, with one complement even admitting a 2-flow.",
  "would_publish": false,
  "caveats": "No general proof or counterexample; novelty of this special case has not been checked."
}
```

## 1. Partial result

I prove a construction theorem and apply it to the entire flower-snark family. The result is stronger than the requested conclusion on this class: the three complements admit nowhere-zero \(2\)-, \(4\)-, and \(4\)-flows, respectively.

The construction does not cover arbitrary bridgeless graphs.

Throughout, a nowhere-zero integer \(k\)-flow means an integer circulation whose edge values, relative to a fixed orientation, satisfy
\[
0<|f(e)|<k.
\]
Subdividing an edge preserves such a flow: orient the replacement path consistently and give all its edges the original value. Isolated vertices cause no difficulty.

### Theorem 1: Doubling a collection of circuits

Let \(H\) be a finite graph having a nowhere-zero \(4\)-flow, and let \(F\) be a union of vertex-disjoint cycles in \(H\). Orient each component of \(F\) cyclically.

Construct \(D(H,F)\) as follows:

* retain every vertex of \(H\);
* retain every edge of \(E(H)\setminus E(F)\);
* for each \(v\in V(F)\), introduce vertices \(v^+\), \(v^-\) and edges \(vv^+\), \(vv^-\);
* for each directed edge \(u\to v\) of \(F\), introduce edges
  \[
  u^+v^-,\qquad u^-v^+.
  \]

Then \(D(H,F)\) has an edge partition \(A_1,A_2,A_3\) such that
\[
D(H,F)\setminus A_1
\]
has a nowhere-zero \(2\)-flow, while both other complements have nowhere-zero \(4\)-flows.

If \(H\) is cubic, then \(D(H,F)\) is cubic.

#### Proof

Put
\[
\begin{aligned}
A_1&=(E(H)\setminus E(F))
       \cup\{vv^+,vv^-:v\in V(F)\},\\
A_2&=\{u^+v^-:u\to v\in E(F)\},\\
A_3&=\{u^-v^+:u\to v\in E(F)\}.
\end{aligned}
\]
These are disjoint and exhaust the edge set by construction.

Each of \(A_2,A_3\) is a perfect matching on the newly introduced vertices. Indeed, every vertex of the oriented \(F\) has exactly one incoming and one outgoing edge. Consequently,
\[
D(H,F)\setminus A_1=A_2\cup A_3
\]
is a disjoint union of even cycles, together with isolated original vertices. Orienting each cycle cyclically and assigning value \(1\) gives a nowhere-zero \(2\)-flow.

Now consider \(D(H,F)\setminus A_2\). For every directed edge \(u\to v\) of \(F\), this graph contains the replacement path
\[
u\,u^-\,v^+\,v.
\]
These paths are internally vertex-disjoint and use every newly introduced vertex exactly once. Thus \(D(H,F)\setminus A_2\) is precisely a subdivision of \(H\), with each edge of \(F\) subdivided twice. It inherits a nowhere-zero \(4\)-flow from \(H\).

Similarly, \(D(H,F)\setminus A_3\) is a subdivision of \(H\), using the paths
\[
u\,u^+\,v^-\,v.
\]
It also inherits a nowhere-zero \(4\)-flow.

Finally, if \(H\) is cubic, an original vertex on \(F\) loses two edges and gains two, and every new vertex has degree three. Hence the constructed graph is cubic. \(\square\)

The constructed graph is automatically bridgeless: every edge belongs to a complement carrying a nowhere-zero flow, whereas a bridge cannot carry a nonzero value in any circulation.

The useful feature of this construction is that **both alternating smoothings of the doubled circuits recover the same known \(4\)-flow graph \(H\)**.

## 2. Application to all flower snarks

For odd \(n\geq 5\), define \(J_n\) on vertices
\[
\{a_i,b_i,c_i,d_i:0\leq i<n\}.
\]
Its edges are:

* the three spokes
  \[
  a_ib_i,\quad a_ic_i,\quad a_id_i
  \qquad(0\leq i<n);
  \]
* the cycle
  \[
  b_0b_1\cdots b_{n-1}b_0;
  \]
* the cycle
  \[
  C=c_0c_1\cdots c_{n-1}d_0d_1\cdots d_{n-1}c_0.
  \]

This is the usual flower graph \(J_n\).

### Corollary 2

For every odd \(n\geq5\), \(J_n\) has an edge partition \(A_1,A_2,A_3\) such that
\[
J_n\setminus A_1
\]
has a nowhere-zero \(2\)-flow and
\[
J_n\setminus A_2,\qquad J_n\setminus A_3
\]
have nowhere-zero \(4\)-flows.

#### Explicit partition

Take
\[
A_1=\{a_ib_i,a_ic_i,a_id_i,b_ib_{i+1}:0\leq i<n\},
\]
where subscripts on \(b\) are cyclic. Let \(A_2,A_3\) be the two alternating perfect matchings of the even cycle \(C\).

Thus the certificate consists simply of the \(b\)-cycle and all spokes in one part, and alternating edges of the \(2n\)-cycle in the other two parts.

#### Proof

Let \(H_n\) be the prism with vertex set
\[
\{a_i,b_i:0\leq i<n\}
\]
and edges
\[
a_ia_{i+1},\qquad b_ib_{i+1},\qquad a_ib_i.
\]

First, \(H_n\) has a nowhere-zero \(4\)-flow. It has the even Hamiltonian cycle
\[
a_0a_1\cdots a_{n-1}b_{n-1}b_{n-2}\cdots b_0a_0.
\]
Colour this cycle alternately \(1,2\), and colour the remaining perfect matching \(3\). This gives a proper \(3\)-edge-colouring.

For an explicit conversion to an integer \(4\)-flow, orient the cycles formed by colours \(1,2\), obtaining a circulation \(f\) with values in \(\{-1,0,1\}\). Independently orient the cycles formed by colours \(1,3\), obtaining another such circulation \(g\). Then
\[
f+2g
\]
is a circulation, and its values are:

* \(\pm1\) on colour \(2\);
* \(\pm2\) on colour \(3\);
* one of \(\pm1,\pm3\) on colour \(1\).

It is therefore a nowhere-zero \(4\)-flow.

Now \(J_n\setminus A_1=C\), apart from isolated vertices, so it has a nowhere-zero \(2\)-flow.

In either of the other complements, every \(c_i,d_i\) has degree two. Suppress these vertices. For each \(i\), the two edges of \(C\) connecting the fibre \(\{c_i,d_i\}\) to the next fibre occur \(n\) positions apart around \(C\). Since \(n\) is odd, each alternating matching contains exactly one of those two edges.

Consequently, in either complement the suppression produces exactly one edge \(a_ia_{i+1}\), in addition to the unchanged \(b\)-cycle and edges \(a_ib_i\). Both suppressed graphs are therefore \(H_n\).

Thus both complements are subdivisions of a graph having a nowhere-zero \(4\)-flow. \(\square\)

Equivalently, \(J_n\) is \(D(H_n,F)\), where \(F\) is the \(a\)-cycle, after exchanging the names of the two copied vertices at alternating positions.

## 3. These examples genuinely go beyond graphs already having a \(4\)-flow

For completeness, here is a self-contained proof that \(J_n\) is not \(3\)-edge-colourable when \(n\) is odd.

Identify the three colours with the nonzero elements
\[
\alpha,\beta,\gamma
\]
of \(\mathbb F_2^2\), so that \(\alpha+\beta+\gamma=0\).

At each claw centred at \(a_i\), record the colours of the incoming and outgoing track edges in branch order \(b,c,d\):
\[
x=(x_1,x_2,x_3),\qquad y=(y_1,y_2,y_3).
\]
Proper colouring at the three branch vertices requires
\[
x_j\ne y_j\qquad(j=1,2,3).
\]
The spoke at branch \(j\) has colour \(x_j+y_j\). Since the three spokes have distinct colours,
\[
(x_1+y_1)+(x_2+y_2)+(x_3+y_3)=0.
\]
Hence
\[
x_1+x_2+x_3=y_1+y_2+y_3. \tag{1}
\]

Between successive claws, the outgoing tuple becomes the next incoming tuple. At the wrap-around, the last two coordinates are exchanged because the \(c,d\) tracks are twisted. This exchange preserves the sum, so (1) gives a common sum \(s\in\mathbb F_2^2\) for all boundary tuples.

### Case 1: \(s=0\)

Every boundary tuple contains the three distinct colours. Passing through a claw changes every coordinate. Thus the outgoing tuple is obtained from the incoming tuple by a derangement of three symbols, necessarily a \(3\)-cycle. Its permutation parity is unchanged.

It follows that tuple parity is preserved through all claws. But the wrap-around transposes the last two coordinates, reversing parity. This is impossible.

### Case 2: \(s\ne0\)

Relabel the colours so that \(s=\alpha\). A triple of nonzero elements summing to \(\alpha\) is either
\[
(\alpha,\alpha,\alpha),
\]
or a permutation of
\[
(\alpha,\beta,\beta),\qquad
(\alpha,\gamma,\gamma).
\]

The all-\(\alpha\) tuple cannot occur: any adjacent tuple with sum \(\alpha\) contains an \(\alpha\), violating coordinatewise inequality.

Every tuple therefore has a repeated colour, either \(\beta\) or \(\gamma\). Two consecutive tuples cannot have the same repeated colour, because two two-element subsets of three coordinate positions intersect. At an intersecting position, the incoming and outgoing colours would coincide.

Thus the repeated colour switches between \(\beta\) and \(\gamma\) at every claw. The wrap-around merely permutes coordinates and does not change the repeated colour. Returning to the starting tuple therefore requires an even number of claws, contradicting odd \(n\).

This proves that \(J_n\) is not \(3\)-edge-colourable.

For cubic graphs, nowhere-zero \(4\)-flows and proper \(3\)-edge-colourings are equivalent. The direction used earlier was proved explicitly above. For the reverse direction, reduce an integer \(4\)-flow modulo \(4\). At every cubic vertex the signed incident residues must be
\[
(1,1,2)\quad\text{or}\quad(3,3,2),
\]
up to permutation. The residue-\(2\) edges form a perfect matching. The remaining cycles are even: their odd half-edge residues agree at a vertex and change sign across an edge, forcing even length. Alternately colouring those cycles supplies the other two colours.

Therefore the flower graphs in Corollary 2 do **not** themselves have nowhere-zero \(4\)-flows. The partial result is not just an application of the easy \(4\)-flow case already mentioned in the question.

## 4. What remains missing

The construction supplies complete certificates for:

* every graph \(D(H,F)\) with \(H\) admitting a nowhere-zero \(4\)-flow;
* in particular, every flower snark \(J_n\), \(n\geq5\) odd.

For a general cubic snark, there is no reason established here that one can find an even circuit system whose two alternating smoothings both admit \(4\)-flows. In the construction, that obstacle is eliminated by design: both smoothings are subdivisions of the same graph \(H\).

I have neither established such a structure for arbitrary bridgeless graphs nor found a counterexample. The full conjecture, and the stronger \(2,3,3\) version in the discussion, remain unresolved by this argument.
