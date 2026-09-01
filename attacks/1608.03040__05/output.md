```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Recognition is known to be NP-complete; below is an exact sparse-class characterization, but no unrestricted structural characterization is obtained.",
  "would_publish": false,
  "caveats": "The NP-hardness reduction is cited from arXiv:1911.01954 rather than reproduced, and the general structural question remains open."
}
```

# Mathematical writeup

## 1. Precise formulation and known complexity

Assume throughout that digraphs are finite, loopless, and have no parallel arcs. For a 2-colouring \(c:V(D)\to\{0,1\}\), put
\[
s_c(v)=|\{u\in N^+(v):c(u)=c(v)\}|.
\]
The colouring is a **majority 2-colouring** if
\[
s_c(v)\le \frac{d^+(v)}2
\qquad\text{for every }v\in V(D).
\]

Let \(\mathsf{M2C}\) denote the corresponding recognition problem.

**Known theorem.** Anastos, Lamaison, Steiner, and Szabó, *Majority Colorings of Sparse Digraphs*, arXiv:1911.01954, Theorem 9, prove that \(\mathsf{M2C}\) is NP-complete.

Membership in NP is immediate: given a colouring, all same-colour out-neighbour counts can be checked in \(O(|V|+|A|)\) time. The NP-hard direction is the cited result and is not independently reproduced here.

Consequently:

* a polynomial-time recognition algorithm exists only if \(\mathrm P=\mathrm{NP}\);
* the algorithmic alternative in Open Problem 5 therefore has the standard negative complexity-theoretic answer;
* NP-completeness does not preclude a descriptive structural characterization, unless that characterization is itself polynomial-time testable.

The structural request is not formally specified: the equivalent conditions below are literally “characterizations,” but are not the informative decomposition or obstruction theorem intended by the question.

---

## 2. Exact algebraic and Boolean formulations

Represent a colouring by signs \(x_v\in\{-1,1\}\). Then
\[
x_v\sum_{u\in N^+(v)}x_u
  =s_c(v)-\bigl(d^+(v)-s_c(v)\bigr)
  =2s_c(v)-d^+(v).
\]
Thus:

\[
\boxed{\quad D\text{ is majority 2-colourable }
\iff
\exists x\in\{-1,1\}^{V(D)}
\ \forall v,\quad
x_v\sum_{u\in N^+(v)}x_u\le 0.\quad}
\]

Equivalently, there is a bipartition for which every vertex has at least
\[
\left\lceil\frac{d^+(v)}2\right\rceil
\]
out-neighbours on the opposite side.

There is also a direct CNF formulation. Write colours as \(z_v\in\{0,1\}\), and put
\[
k_v=\left\lfloor\frac{d^+(v)}2\right\rfloor+1.
\]
For every \(k_v\)-subset \(S\subseteq N^+(v)\), impose
\[
\left(z_v\vee\bigvee_{u\in S}z_u\right)
\quad\wedge\quad
\left(\neg z_v\vee\bigvee_{u\in S}\neg z_u\right).
\]
These clauses forbid \(v\) and all vertices of \(S\) from receiving the same colour. The conjunction over all \(v,S\) is satisfiable exactly when \(D\) has a majority 2-colouring. This formulation may be exponentially large and does not yield an efficient algorithm.

---

## 3. Why induced-obstruction characterizations cannot work

Let \(D\) have vertices \(a,b,c,s\) and arcs
\[
a\to b,\qquad b\to c,\qquad c\to a,
\]
together with
\[
a\to s,\qquad b\to s,\qquad c\to s.
\]
Colour \(a,b,c\) alike and colour \(s\) oppositely. Each of \(a,b,c\) then has one same-colour and one opposite-colour out-neighbour, while \(s\) is a sink. Hence \(D\) is majority 2-colourable.

On the other hand, \(D[\{a,b,c\}]\) is a directed odd cycle of outdegree one. Its three arcs would each require differently coloured endpoints, which is impossible.

Thus majority 2-colourability is not hereditary. In particular, it cannot be characterized as the class of digraphs avoiding any family—finite or infinite—of induced subdigraphs.

---

## 4. Source deletion and acyclic digraphs

### Lemma 4.1
If \(v\) has indegree zero, then
\[
D\text{ is majority 2-colourable}
\iff
D-v\text{ is majority 2-colourable}.
\]

### Proof
If \(D\) has a majority colouring, restriction to \(D-v\) preserves every remaining vertex's out-neighbourhood, since no vertex sends an arc to \(v\).

Conversely, colour \(D-v\). Among the two colours, choose for \(v\) one occurring no more than \(d^+(v)/2\) times in \(N^+(v)\). This satisfies \(v\), and the colour of \(v\) affects no other condition because \(d^-(v)=0\). ∎

Repeatedly deleting indegree-zero vertices therefore preserves majority 2-colourability. Let \(K(D)\) denote the resulting directed \(1\)-in-core.

### Corollary 4.2
Every acyclic digraph has a majority 2-colouring, constructible in linear time.

Indeed, a DAG is completely removed by source deletion. Equivalently, take a topological order and colour vertices in reverse order, always choosing a minority colour among the already coloured out-neighbours.

---

## 5. Maximum outdegree one

### Proposition 5.1
Suppose \(\Delta^+(D)\le 1\). Let \(G_D\) be the undirected graph with edge \(uv\) whenever \(v\) is the unique out-neighbour of \(u\). Then
\[
D\text{ is majority 2-colourable}
\iff
G_D\text{ is bipartite}.
\]

### Proof
If \(d^+(u)=1\), the majority condition requires its unique out-neighbour to have the opposite colour. Thus a majority colouring is exactly a proper 2-colouring of \(G_D\). ∎

This gives a linear-time exact characterization for \(\Delta^+\le1\). For arbitrary digraphs, bipartiteness of the graph formed by all outdegree-one constraints remains a necessary, but not sufficient, condition.

---

## 6. Maximum outdegree two and Property B

Suppose \(\Delta^+(D)\le2\). Define an indexed hypergraph \(H_D\) on \(V(D)\) by introducing, for every vertex \(v\) of positive outdegree, the hyperedge
\[
E_v=\{v\}\cup N^+(v).
\]
Thus \(E_v\) has size two or three.

### Proposition 6.1
For \(\Delta^+(D)\le2\),
\[
D\text{ has a majority 2-colouring}
\iff
H_D\text{ has Property B},
\]
that is, \(H_D\) has a vertex 2-colouring with no monochromatic hyperedge.

### Proof
If \(d^+(v)=1\), the condition is precisely that \(E_v\) is not monochromatic.

If \(d^+(v)=2\), the condition fails precisely when both out-neighbours have the same colour as \(v\), equivalently when the three-element edge \(E_v\) is monochromatic. ∎

Conversely, every rank-\(3\) hypergraph whose indexed edges admit distinct representatives \(r(E)\in E\) arises this way: make \(r(E)\) send arcs to the other one or two vertices of \(E\). Thus the natural sparse part of majority 2-colourability is exactly an oriented form of hypergraph Property B.

---

## 7. A complete sparse-class characterization

The following elementary hypergraph lemma gives a more structural result.

### Lemma 7.1
Let \(H\) be a hypergraph in which every edge has size at least two and every vertex belongs to at most two indexed edges. Then \(H\) has Property B unless one of its connected components is an odd cycle consisting entirely of two-element edges. Such an odd-cycle component is, of course, not 2-colourable.

### Proof

Assume \(H\) has no such component. We argue by induction on the number of hyperedges.

If some vertex \(x\) belongs to exactly one edge \(E\), consider \(H-E\). It still has no odd-cycle component: an odd cycle appearing as a component of \(H-E\) uses each of its vertices twice, so, under the degree-at-most-two hypothesis, \(E\) could not meet that component. By induction, colour \(H-E\). Choose any \(y\in E\setminus\{x\}\) and colour \(x\) oppositely to \(y\). Since \(x\) occurs nowhere in \(H-E\), this extends the colouring.

It remains to consider a component in which every vertex belongs to exactly two hyperedges. Construct a loopless multigraph \(G\) as follows:

* the vertices of \(G\) are the hyperedges of \(H\);
* every hypergraph vertex \(x\), lying in exactly two hyperedges \(E,F\), becomes an edge \(EF\) of \(G\).

A red-blue colouring of the edges of \(G\) is exactly a red-blue colouring of the vertices of \(H\). A hyperedge \(E\) of \(H\) is nonmonochromatic precisely when the corresponding vertex of \(G\) is incident with both edge colours.

We use the following fact.

> **Weak edge-colouring fact.** Every connected loopless multigraph \(G\) with minimum degree at least two has an edge 2-colouring in which every vertex sees both colours, unless \(G\) is an odd cycle.

To prove the fact, add a new vertex \(z\) adjacent once to every odd-degree vertex of \(G\). The resulting graph \(G'\) is Eulerian. Take an Euler circuit and colour its edges alternately.

If the circuit length is even, each arrival-departure pair at every vertex receives opposite colours. After deleting the added edges, an originally odd-degree vertex still has at least one untouched opposite-coloured pair because its original degree was at least three.

If the circuit length is odd and \(z\) was added, choose the beginning of the Euler circuit at \(z\), so the unique failure of cyclic alternation occurs only at \(z\). If no \(z\) was needed, all degrees of \(G\) are even. Unless \(G\) is an odd cycle, some vertex has degree at least four; start the circuit there. Its non-boundary arrival-departure pair supplies both colours, while every other vertex has only opposite-coloured pairs.

This proves the fact. Applying it to the dual multigraph \(G\) gives Property B unless \(G\) is an odd cycle. The latter case corresponds exactly to an odd cycle of two-element hyperedges in \(H\). ∎

This immediately yields the promised digraph characterization.

### Theorem 7.2
If
\[
\Delta^+(D)\le2
\qquad\text{and}\qquad
\Delta^-(D)\le1,
\]
then \(D\) is majority 2-colourable if and only if no weak component of \(D\) is a directed odd cycle.

### Proof
For the hypergraph \(H_D\),
\[
\deg_{H_D}(x)
=
\mathbf 1_{\{d^+(x)>0\}}+d^-(x)
\le2.
\]
Lemma 7.1 therefore applies.

It remains to identify its obstruction. Suppose a component of \(H_D\) is an odd cycle of two-element edges. Each such edge is \(E_v=\{v,u\}\) for a vertex \(v\) of outdegree one. An odd cycle has equally many vertex-nodes and hyperedge-nodes. Since different indexed hyperedges have different tails, every vertex in the component is the tail of exactly one edge and the head of exactly one edge. Hence the corresponding weak component of \(D\) is a directed odd cycle. Its indegrees and outdegrees are saturated, so no arc joins it to the rest of \(D\).

Conversely, on a directed odd-cycle component every vertex has outdegree one, so every arc requires opposite colours at its endpoints. This is impossible around an odd cycle. ∎

The proof is constructive and yields a linear-time recognition and colouring algorithm for this sparse class.

Combining this with source deletion gives a somewhat wider exact result:

### Corollary 7.3
Let \(K(D)\) be obtained by repeatedly deleting indegree-zero vertices. If
\[
\Delta^+(K(D))\le2,\qquad \Delta^-(K(D))\le1,
\]
then \(D\) is majority 2-colourable exactly when no weak component of \(K(D)\) is a directed odd cycle.

---

## 8. Why the indegree-two case is already richer

The indegree bound in Theorem 7.2 cannot simply be removed.

Let \(V(D)=\mathbb Z_7\), and put
\[
i\to i+1,\qquad i\to i+3
\quad\text{for every }i\in\mathbb Z_7.
\]
This is a \(2\)-in, \(2\)-out regular digraph. Its constraint triples are
\[
L_i=\{i,i+1,i+3\},
\]
namely
\[
013,\ 124,\ 235,\ 346,\ 045,\ 156,\ 026.
\]
These are the seven lines of the Fano plane: every pair of vertices lies in exactly one listed triple.

Every red-blue colouring of the Fano plane has a monochromatic line. To see this, let \(B\) be the smaller colour class.

* If \(|B|\le2\), choose a vertex \(r\) of the other colour. The three lines through \(r\) partition the other six vertices into three pairs. At most two pairs meet \(B\), so one line through \(r\) is monochromatic.
* If \(|B|=3\) and \(B\) is a line, it is monochromatic.
* If \(|B|=3\) and is not a line, the three lines determined by its three pairs are distinct and account for six of the nine incidences between \(B\) and the seven lines. The remaining four lines contain only three such incidences in total, so one of them misses \(B\) and is monochromatic in the other colour.

By Proposition 6.1, this digraph has no majority 2-colouring. Thus new obstructions already occur at \(\Delta^+=\Delta^-=2\).

---

## 9. A broad positive class: symmetric digraphs

### Proposition 9.1
Every symmetric digraph—one in which \(uv\) is an arc exactly when \(vu\) is an arc—has a majority 2-colouring.

### Proof
Let \(G\) be its underlying undirected graph. Start with any bipartition and repeatedly flip a vertex having more neighbours on its own side than on the opposite side. If \(s\) incident edges currently stay inside its side and \(o\) cross the cut, flipping the vertex increases the number of crossing edges by \(s-o>0\).

The process terminates after at most \(|E(G)|\) flips. At termination, every vertex has at least as many neighbours across the cut as on its own side. Since \(N_D^+(v)=N_G(v)\), this is a majority 2-colouring of \(D\). ∎

This is a polynomial constructive argument; it does not require computing a maximum cut.

---

## 10. Complexity barriers and remaining gap

The conclusions are:

1. **Algorithmic half:** \(\mathsf{M2C}\) is NP-complete. Hence a polynomial-time recognition algorithm would imply \(\mathrm P=\mathrm{NP}\).

2. **Hereditary characterization:** impossible, even with an infinite forbidden-induced-subdigraph family, because the class is not hereditary.

3. **Exact restricted characterizations:**
   * for \(\Delta^+\le1\), bipartiteness of the forced-edge graph;
   * for \(\Delta^+\le2,\Delta^-\le1\), the only obstructions are weak components that are directed odd cycles;
   * more generally for \(\Delta^+\le2\), the problem is exactly Property B for the associated rank-\(3\) hypergraph;
   * DAGs and symmetric digraphs are always majority 2-colourable.

4. **Unresolved part:** no informative structural characterization for arbitrary digraphs is obtained. The hypergraph reformulation becomes substantially more complicated once vertices occur in three or more local constraints, as the Fano example demonstrates.

Finally, any general characterization whose conditions could be tested in polynomial time would contradict NP-completeness unless \(\mathrm P=\mathrm{NP}\). A polynomially bounded, polynomially verifiable obstruction certificate for every non-colourable digraph would put \(\mathsf{M2C}\) in coNP and hence, by NP-completeness, imply \(\mathrm{NP}=\mathrm{coNP}\). These are barriers to certain kinds of characterization, not proofs that no useful structural theorem exists.