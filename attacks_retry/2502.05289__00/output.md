```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A polynomial-time completion criterion extends the supplied partial result to four of the five two-branch topologies and all three-branch subcubic trees, but does not resolve the dichotomy.",
  "would_publish": false,
  "caveats": "Uses the established Three-in-a-Tree theorem; novelty is not claimed, and neither general direction of the dichotomy is proved."
}
```

# 1. Scope and main partial result

All graphs below are finite and simple. A subdivision may replace an edge by a path of length one. The target \(H\) is fixed; the input graph \(G\) is arbitrary and need not be subcubic.

A **branch vertex** of a subcubic graph means a vertex of degree \(3\).

I do not resolve the conjecture. The main result is the following sufficient condition for polynomial-time induced-subdivision detection.

## Theorem 1 — Single-center criterion

Let \(H\) be a fixed connected subcubic graph. Suppose there is a branch vertex \(v\) such that

1. \(H-v\) is a forest; and
2. every component of \(H-v\) contains at most one vertex having degree \(3\) **in \(H\)**.

Then \(H\)-\(\textsc{ISC}\) is polynomial-time solvable.

The distinction “degree \(3\) in \(H\)” is important: deleting \(v\) can lower the degree of another branch vertex.

This theorem gives, among other cases:

- every subcubic tree with at most three branch vertices;
- every four-branch subcubic tree whose branch-vertex skeleton is a star;
- four of the five connected two-branch topologies, including the cycle-with-fork case left untreated in the supplied attempt.

I reuse the previous attempt’s three-terminal completion idea, but prove the reduction and its applicability below. The useful additional observation is that, under the theorem’s hypotheses, all unbounded subdivision lengths can be concentrated on the three edges incident with one vertex.

I have not established whether these particular special cases are new in the literature.

# 2. A verified three-port completion lemma

I use the established **Three-in-a-Tree theorem**:

> Given a graph and three specified vertices, one can decide in polynomial time whether an induced tree contains all three.

No extension to four terminals is assumed.

## Lemma 2 — Three-port completion

Let \(Z\subseteq V(G)\), and let \(t_1,t_2,t_3\) be distinct vertices of \(Z\). There is a polynomial-time algorithm deciding whether some \(U\subseteq V(G)\setminus Z\) satisfies:

1. \(U\) is anticomplete to \(Z\setminus\{t_1,t_2,t_3\}\);
2. after deleting the edges between the three ports, the graph
   \[
   G[U\cup\{t_1,t_2,t_3\}]
   \]
   is a subdivided claw with leaves \(t_1,t_2,t_3\).

Thus the claw can be attached to the fixed induced configuration \(G[Z]\), with all existing edges between ports restored.

### Proof

Write \(T=\{t_1,t_2,t_3\}\), and set
\[
W=\{w\in V(G)\setminus Z:N_G(w)\cap(Z\setminus T)=\varnothing\}.
\]
Let
\[
A=G[W\cup T]-E(G[T]).
\]

Enumerate ordered triples
\[
(z_1,z_2,z_3)\in W^3
\]
such that \(t_i z_i\in E(G)\) for each \(i\). Coincidences among the \(z_i\) are allowed.

For each triple, retain only
\[
W_{\boldsymbol z}
=
\{w\in W:\text{ for every }i,\ t_iw\in E(G)\Longrightarrow w=z_i\}.
\]
Reject the triple if any chosen \(z_i\) was removed. Otherwise, in
\[
A_{\boldsymbol z}=A[T\cup W_{\boldsymbol z}],
\]
each \(t_i\) has exactly one neighbor.

Apply Three-in-a-Tree to the three ports. If it returns yes, take an induced tree containing them and repeatedly delete leaves not among the ports. The resulting induced tree has exactly three leaves: every port remains a leaf, and no other leaf remains.

For a tree with at least two vertices,
\[
|\{x:\deg(x)=1\}|
=
2+\sum_{\deg(x)\ge 3}(\deg(x)-2).
\]
Consequently, a tree with exactly three leaves has precisely one degree-\(3\) vertex and no vertex of higher degree. It is therefore a subdivided claw with the prescribed leaves.

Conversely, a valid claw completion determines the first neighbor \(z_i\) of each port. Its vertices lie in \(W\), and no completion vertex other than \(z_i\) is adjacent to \(t_i\). Thus the entire claw survives for that enumerated triple, and Three-in-a-Tree returns yes.

There are at most \(n^3\) triples. All other operations are polynomial. ∎

The temporary deletion of port-to-port edges does not discard inducedness requirements. Those edges already belong to the fixed configuration \(G[Z]\); the final graph contains exactly the fixed edges together with the claw edges.

# 3. Concentrating subdivisions at one vertex

The following normalization is the structural part of Theorem 1.

## Lemma 3 — Normalization

Assume \(H,v\) satisfy Theorem 1. Every subdivision \(S\) of \(H\) has an induced subgraph \(S'\) admitting a subdivision model of \(H\) in which every edge not incident with \(v\) is unsubdivided.

### Proof

Consider the maximal threads of \(H\): paths with internal vertices of degree \(2\) and endpoints of degree \(1\) or \(3\), also allowing a thread that returns to the same branch vertex and forms a private cycle.

Because \(H\) is connected and has a branch vertex, these threads account for all its edges.

There are two restrictions on nonpendant threads.

- A thread between two distinct branch vertices different from \(v\) cannot exist: it would put two branch vertices of \(H\) in one component of \(H-v\).
- A private-cycle thread at a branch vertex different from \(v\) cannot exist: that cycle would survive in \(H-v\).

Hence every thread that is not a branch-to-leaf thread is either:

- a thread between \(v\) and another branch vertex; or
- a private-cycle thread at \(v\).

Fix a subdivision presentation of \(S\). Perform the following operations.

### Pendant threads

If a branch-to-leaf thread has length \(a\) in \(H\), retain only the first \(a\) edges of its corresponding thread in \(S\), starting at the branch vertex. Delete the remaining tail.

This is vertex deletion, and it leaves a pendant thread of exactly the required length.

### Threads between \(v\) and another branch vertex

Suppose such a thread has length \(d\) in \(H\) and length \(D\ge d\) in \(S\). Starting at its endpoint different from \(v\), use the first \(d-1\) consecutive internal vertices as the images of the internal vertices of the target thread.

All the excess length is then assigned to its final edge, which is incident with \(v\). No vertices of this thread need to be deleted.

### A private cycle at \(v\)

Suppose its length in \(H\) is \(q\). The corresponding cycle in \(S\) has length at least \(q\). On the path obtained by deleting \(v\) from that cycle, choose \(q-1\) consecutive vertices as the images of the target cycle’s other vertices.

All edges between these chosen vertices are unsubdivided. Any excess length is assigned to the two cycle edges incident with \(v\).

These choices are compatible because distinct threads have disjoint interiors. The resulting graph \(S'\), obtained only by truncating pendant tails, is induced in \(S\). With the new placement of the target’s degree-\(2\) vertices, only edges incident with \(v\) may be subdivided. ∎

This argument retains the length requirements of the fixed target. It does not replace \(H\) by an unconstrained homeomorphism type.

## Proof of Theorem 1

Let
\[
F=H-v,\qquad N_H(v)=\{t_1,t_2,t_3\}.
\]

Enumerate all injective maps
\[
\phi:V(F)\longrightarrow V(G)
\]
whose images induce a copy of \(F\). For each such copy, apply Lemma 2 with
\[
Z=\phi(V(F)),\qquad \text{ports } \phi(t_1),\phi(t_2),\phi(t_3).
\]

**Soundness.** A successful completion adds a new claw center and three internally disjoint paths to the images of the neighbors of \(v\). Together with the fixed copy of \(H-v\), this is precisely a subdivision of \(H\), with only edges incident with \(v\) possibly subdivided. Lemma 2 ensures that the union is induced in \(G\).

**Completeness.** Suppose \(G\) contains an induced subdivision \(S\) of \(H\). Apply Lemma 3 inside \(S\). The resulting induced subgraph contains an induced copy of \(F\), and everything outside that copy consists of the three subdivided edges incident with the image of \(v\). These form a valid claw completion, modulo any fixed edges between ports. The corresponding copy of \(F\) is enumerated, and Lemma 2 accepts.

There are at most \(n^{|V(H)|-1}\) embeddings to consider, followed by polynomial-time completion tests. ∎

# 4. Consequences for small branch topologies

## 4.1. Paths and cycles

Paths require no completion theorem: an induced subdivision of a fixed path contains an induced copy of that path by truncation.

For completeness, fixed cycle targets are also elementary.

### Proposition 4

For every fixed \(q\ge 3\), one can detect an induced cycle of length at least \(q\) in polynomial time.

### Proof

Enumerate every induced path
\[
P=(p_0,\ldots,p_{q-2}),
\]
having \(q-2\) edges. Put \(s=p_0\), \(t=p_{q-2}\), and
\[
M=V(P)\setminus\{s,t\}.
\]
Construct
\[
D=G\left[
\{s,t\}\cup
\{w\notin V(P):N_G(w)\cap M=\varnothing\}
\right],
\]
and delete \(st\) from \(D\), if present.

If \(s,t\) are connected, take a shortest path \(R\) between them in this auxiliary graph. It has at least two edges. Shortestness and the neighborhood deletion imply that \(P\cup R\) is an induced cycle, of length at least
\[
(q-2)+2=q.
\]

For \(q=3\), the deleted edge \(st\) is exactly the fixed path \(P\), and is restored when forming the cycle.

Conversely, from an induced cycle of length at least \(q\), choose \(q-2\) consecutive edges for \(P\). Its complementary path survives the auxiliary construction. ∎

Thus all connected targets with no branch vertex are covered.

## 4.2. Exactly two branch vertices

Let \(u,v\) be the two branch vertices of a connected subcubic graph. Suppress degree-\(2\) vertices while recording all thread lengths.

There is at least one \(u\)-\(v\) thread. If there are \(k\) such threads, then \(k\in\{1,2,3\}\). Each private cycle uses two incidences at its branch vertex; remaining incidences lead to pendant paths. This gives exactly the following five topologies.

| Topology | Suitable center for Theorem 1 |
|---|---|
| Three \(u\)-\(v\) threads: a theta | Either branch |
| Two \(u\)-\(v\) threads, with one pendant path at each branch | Either branch |
| One \(u\)-\(v\) thread, with two pendant paths at each branch | Either branch |
| A private cycle at \(u\), a \(u\)-\(v\) thread, and two pendant paths at \(v\) | \(u\) |
| A private cycle at each branch, joined by a thread: a barbell | Neither branch |

Consequently:

## Corollary 5

Every fixed connected subcubic target with exactly two branch vertices is covered by Theorem 1 except the two-private-cycle barbell topology.

This includes arbitrary prescribed thread lengths.

### The additional private-cycle case explicitly

Suppose \(H\) has:

- a cycle of length \(q\) through \(u\);
- a path of length \(d\) from \(u\) to \(v\);
- two pendant paths at \(v\), of lengths \(a,b\).

Deleting \(u\) leaves:

- a path of length \(q-2\), providing two ports;
- a component containing only the branch vertex \(v\), providing the third port.

One claw completion recreates the cycle branch \(u\), closes the cycle, and completes the handle to \(v\). Thus this case does not require two unrelated unbounded completions.

## 4.3. Trees with three or four branch vertices

For a subcubic tree \(T\), define its **branch-vertex skeleton** to have the branch vertices of \(T\) as vertices, with two adjacent when their connecting path in \(T\) contains no other branch vertex.

If this skeleton is a star, choose its center \(v\). Each component of \(T-v\) contains at most one branch vertex, so Theorem 1 applies.

## Corollary 6

The induced-subdivision problem is polynomial-time solvable for:

1. every fixed subcubic tree with at most three branch vertices;
2. every fixed four-branch subcubic tree whose branch-vertex skeleton is \(K_{1,3}\).

For three branch vertices, the skeleton is necessarily a path, so its middle vertex is a suitable center. For four branch vertices, the other possible skeleton is a four-vertex path; that case is not covered by this argument.

The criterion also covers a further unicyclic three-branch family: a cycle with a pendant path at one cycle branch and a path to a two-armed fork at the other cycle branch. Choose the latter cycle branch as the center.

## 4.4. Some disconnected targets

A path or subdivided claw has the following truncation property:
\[
G\text{ contains an induced subdivision of }B
\iff
G\text{ contains an induced copy of }B.
\]
For a subdivided claw, truncate its three arms to their target lengths.

Therefore let
\[
H=B\mathbin{\dot\cup}J,
\]
where every component of \(B\) is a path or subdivided claw, and \(J\) is one connected target covered above.

Enumerate an induced copy \(B'\) of \(B\), delete its closed neighborhood, and run the algorithm for \(J\) in the remaining graph. This is correct because distinct components of an induced subdivision are anticomplete, and the components assigned to \(B\) can be truncated independently.

This does not handle an arbitrary disjoint union of nontruncatable components.

# 5. A bounded-cycle result for the remaining barbell topology

The three-port lemma also gives a restricted algorithm for barbells.

Let
\[
B(q_1,q_2,d)
\]
denote two vertex-disjoint cycles of lengths \(q_1,q_2\ge 3\), joined by a path of length \(d\ge 1\).

## Proposition 7

For fixed \(q_1,q_2,d,L\), one can decide in polynomial time whether \(G\) contains an induced subdivision of \(B(q_1,q_2,d)\) in which at least one of the two model cycles has length at most \(L\).

In particular, every fixed barbell target is polynomial-time detectable on any input class with a fixed upper bound on induced-cycle length.

### Proof

First seek a model whose cycle corresponding to \(C_{q_1}\) has length at most \(L\).

Enumerate:

1. an induced cycle \(C\) of length
   \[
   q_1\le \ell\le L;
   \]
2. a vertex \(u\in V(C)\);
3. a path \(Q\) of length \(d-1\), starting at \(u\), otherwise disjoint from \(C\), with other endpoint \(z\);
4. a path \(P\) of length \(q_2-2\), disjoint from \(C\cup Q\), with endpoints \(x,y\).

When \(d=1\), \(Q\) is just \(u=z\).

Require the enumerated vertices to induce exactly the cycle with its attached prefix, together with the separate path \(P\). Apply Lemma 2 with ports \(x,y,z\).

If the completion has center \(v\), then:

- \(P\) and the two completion arms to \(x,y\) form an induced cycle of length at least \(q_2\);
- \(Q\) and the completion arm to \(z\) form a \(u\)-\(v\) path of length at least \(d\);
- this path joins the two induced cycles with no unwanted edges.

Thus a successful completion is a required barbell subdivision.

Conversely, take a qualifying model. Enumerate its bounded cycle, the first \(d-1\) edges of the handle from that cycle, and \(q_2-2\) consecutive edges of its other cycle avoiding that cycle’s attachment vertex. The remaining three paths form a valid claw completion.

Finally, interchange \(q_1,q_2\) to allow either model cycle to be the bounded one. All enumeration sizes are bounded by constants depending on the fixed parameters. ∎

This isolates the limitation of this approach: it does not decide whether there is a barbell model whose two cycles are both arbitrarily long.

# 6. Relation to planarity and the nonplanar direction

The targets in Theorem 1 are planar. Indeed, \(H-v\) has at most three components, and each contains at most one branch vertex of \(H\). Thus \(H\) has at most four branch vertices. The following elementary structural fact explains why that suffices.

## Proposition 8

Every nonplanar subcubic graph has at least six branch vertices. If it is connected and has exactly six, it is a subdivision of \(K_{3,3}\).

### Proof

By Kuratowski’s theorem, a nonplanar graph contains a subdivision of \(K_5\) or \(K_{3,3}\) as a subgraph. A subcubic graph cannot contain a subdivision of \(K_5\), so it contains a subdivision \(K\) of \(K_{3,3}\).

The six branch vertices of \(K\) have degree \(3\) in the ambient graph.

If these are the only degree-\(3\) vertices, each is saturated by its edges in \(K\). Every internal vertex of \(K\) has degree \(2\) in \(K\), and any additional incident edge would create another degree-\(3\) vertex. Hence no additional edge is incident with \(V(K)\). Thus \(K\) is a connected component, and connectedness makes it the whole graph. ∎

This is only a structural observation. It supplies no hardness reduction for \(K_{3,3}\) or its subdivisions. In particular, hardness for one fixed nonplanar target does not automatically transfer to every nonplanar target.

# 7. Remaining gaps

The full conjecture is not proved or disproved here.

What has been established is a polynomial-time algorithm for the precise single-center class of Theorem 1, its stated disconnected extensions, and the bounded-cycle barbell restriction. The algorithms work on unrestricted input graphs.

What remains beyond these arguments includes:

- the unrestricted two-private-cycle barbell case;
- planar branch structures not satisfying the single-center criterion;
- arbitrary combinations of nontruncatable connected components;
- a general NP-hardness theorem for nonplanar subcubic targets.

An omitted target is not thereby claimed to be open in the literature: for example, the question itself reports algorithms for \(K_4\) and the net, neither of which is subsumed by the criterion above.

Finally, every fixed \(H\)-\(\textsc{ISC}\) problem is in \(\mathsf{NP}\), using an explicit induced-subdivision model as certificate. The expected formal hard-side statement is therefore NP-completeness for every nonplanar subcubic \(H\); interpreting that as “not in \(\mathsf P\)” additionally requires \(\mathsf P\ne\mathsf{NP}\). No such general hardness statement is obtained here.