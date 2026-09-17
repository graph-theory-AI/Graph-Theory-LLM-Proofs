Attack the following open graph-theory problem.

Catalog id: friendly_partitions
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/friendly_partitions/
Original entry: http://www.openproblemgarden.org/op/friendly_partitions
Problem attributed to: DeVos, Matt (posted 2009-11-08)

=== Problem statement (OpenProblemGarden) ===
Title: Friendly partitions
A friendly partition of a graph is a partition of the vertices into two sets so that every vertex has at least as many neighbours in its own class as in the other. Problem Is it true that for every $ r $ , all but finitely many $ r $ -regular graphs have friendly partitions?

=== Discussion / context (OpenProblemGarden) ===
Let me say at the start, that I (M. DeVos) suspect this problem has been considered previously, so I await a more correct attribution. An unfriendly partition of a graph is a partition of the vertices into two sets so that every vertex has at least as many neighbours in the opposite class as its own. It is an easy fact that every (finite) graph has an unfriendly partition; for instance, any maximum size edge-cut gives a partition with this property. Finding friendly partitions appears to be considerably more difficult. Perhaps one reason why is that there exist graphs without unfriendly partitions. For instance, $ K_{2n} $ and $ K_{2n+1,2n+1} $ have no unfriendly partitions. However, it appears possible that the only graphs which fail to have friendly partitions are fairly dense. When $ r=3 $ , the above problem is fairly easy to solve, as it reduces to the problem of finding two vertex disjoint cycles. Every cubic graph other than $ K_4 $ or $ K_{3,3} $ has two disjoint cycles, and thus has a friendly partition. The case when $ r=4 $ is also not terribly complicated. However, the next step up, $ r=5 $ looks like a tricky problem which requires something new.

=== Catalog page (statement + literature review) ===
Friendly partitions — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 DeVos's question (equivalent to the internal-partition conjecture for $r$-regular graphs) remains open in full generality. Ban and Linial (2013) proved the conjecture for $r=6$ and exhibited new families of regular graphs without internal partitions; the cubic and 4-regular cases were already essentially known. The 5-regular case is still open as a deterministic statement, but Bärnkopf, Nagy and Paulovics (2024) settled it for 5-regular abelian Cayley graphs, and Csóka, Fekete, Nagy and Szemerédi (2025) showed that random 5-regular graphs a.a.s. admit an internal partition.

 Cited literature (4)

 
 
 
partial Internal Partitions of Regular Graphs
 (2013)
 

 
 Amir Ban, Nati Linial · arXiv preprint (later J. Graph Theory) · arXiv:1307.5246

Proves the internal/friendly partition conjecture for $r=6$ (all but finitely many 6-regular graphs have an internal partition), gives improved lower bounds on the threshold $N(d)$, and constructs new families of $d$-regular graphs without internal partitions, including $2k$-regular examples on $3k+2$ vertices.
 

 
 
partial A note on internal partitions: the 5-regular case and beyond
 (2021)
 

 
 Pál Bärnkopf, Zoltán Lóránt Nagy, Zoltán Paulovics · arXiv preprint (Graphs and Combinatorics, 2024) · arXiv:2109.14421 · doi:10.1007/s00373-024-02774-9

Studies the still-open 5-regular case, classifies all 5-regular abelian Cayley graphs without an internal partition, and obtains structural results on subgraphs of minimum degree 3 inside 5-regular graphs.
 

 
 
partial Bisection width, max-cut and internal partitions of 5-regular graphs
 (2025)
 

 
 Endre Csóka, Panna Tímea Fekete, Zoltán Lóránt Nagy, Levente Szemerédi · arXiv preprint · arXiv:2509.08531

Using a local-algorithm based factor with a recoloring phase, proves that random 5-regular graphs asymptotically almost surely admit an internal (friendly) partition, and derives new upper bounds on bisection width and max-cut of random $d$-regular graphs for $d>4$.
 

 
 
partial Majority Dynamics and Internal Partitions of Random Regular Graphs: Experimental Results
 (2024)
 

 
 Pavel Arkhipov · arXiv preprint · arXiv:2406.07026

Investigates majority dynamics on random odd-regular graphs as a heuristic for producing internal partitions, shows the standard dynamics fails to yield parts with the required $\lceil d/2\rceil$-cores, and proposes a modified dynamics that does so with high probability.
 

 

 Reviewer notes. DeVos's 'friendly partition' problem is exactly the internal-partition conjecture studied in the literature (vertex partition into two nonempty parts where every vertex has at least as many neighbours in its own part as in the other). The cases $r\in\{3,4\}$ are folklore/easy (cubic case reduces to two disjoint cycles, excluding $K_4$ and $K_{3,3}$). The Ban-Linial paper resolves $r=6$; $r=5$ and all $r\geq 7$ remain open in the deterministic sense, with progress only for random graphs and special families (Cayley graphs). The DOI 10.1007/s00373-024-02774-9 for the Graphs and Combinatorics version was found via search but the Springer page required authentication; the arXiv abstract page was verified directly.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Problem. Is it true that for every $ r $ , all but finitely many $ r $ -regular graphs have friendly partitions?

Keywords:
edge-cut · partition · regular

Discussion

Let me say at the start, that I (M. DeVos) suspect this problem has been considered previously, so I await a more correct attribution. An unfriendly partition of a graph is a partition of the vertices into two sets so that every vertex has at least as many neighbours in the opposite class as its own. It is an easy fact that every (finite) graph has an unfriendly partition; for instance, any maximum size edge-cut gives a partition with this property. Finding friendly partitions appears to be considerably more difficult. Perhaps one reason why is that there exist graphs without unfriendly partitions. For instance, $ K_{2n} $ and $ K_{2n+1,2n+1} $ have no unfriendly partitions. However, it appears possible that the only graphs which fail to have friendly partitions are fairly dense. When $ r=3 $ , the above problem is fairly easy to solve, as it reduces to the problem of finding two vertex disjoint cycles. Every cubic graph other than $ K_4 $ or $ K_{3,3} $ has two disjoint cycles, and thus has a friendly partition. The case when $ r=4 $ is also not terribly complicated. However, the next step up, $ r=5 $ looks like a tricky problem which requires something new.

Related conjectures

 
 related to
 Unfriendly partitions
 partial
 Dual notions in disjoint settings with no logical link. Friendly partitions (DeVos) asks whether all but finitely many finite r-regular graphs admit a partition where every vertex has at least as many neighbours in its own class; the unfriendly-partition problem (Cowan-Emerson) asks whether every countably infinite graph has a partition where every vertex has at least as many neighbours in the other class. The source page mentions unfriendly partitions only as contrast/motivation ('every finite graph has an unfriendly partition ... finding friendly partitions appears to be considerably more difficult'). One statement is about finite regular graphs with the 'friendly' inequality, the other about countably infinite graphs with the opposite inequality; truth of either has no bearing on the other. Thematically linked, no implication: related_only.
 

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
  "one_line": "Every odd-regular graph of degree at least 3 and girth at least 5 has a friendly partition, as shown by the self-contained argument below.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of this special case and its algorithmic proof is not claimed."
}
```

## 1. Scope of the result

Graphs are finite, simple and undirected, and both classes of a friendly partition must be **nonempty**.

I do not resolve the full conjecture. I prove the following deterministic special case, including a polynomial-time construction.

**Theorem.** Let \(k\ge 2\). Every \((2k-1)\)-regular graph containing neither a triangle nor a cycle of length four has a friendly partition.

Thus, in particular, every 5-regular graph of girth at least five has a friendly partition. The proof also gives a structural restriction on potential counterexamples without a girth assumption.

No literature result is needed for the argument below, and I am not claiming that this special case is new.

## 2. Friendly partitions and disjoint cores

Call a nonempty vertex set \(X\) a **\(k\)-core set** if
\[
\delta(G[X])\ge k.
\]
Here, a core set need not be maximal. A graph is \((k-1)\)-degenerate precisely when it contains no \(k\)-core set.

### Lemma 1: extending two cores

In a \((2k-1)\)-regular graph, a friendly partition exists if and only if there are two disjoint \(k\)-core sets.

**Proof.** The forward implication is immediate.

Conversely, let \(X,Y\) be disjoint \(k\)-core sets. Among all partitions
\[
V(G)=A\mathbin{\dot\cup}B,\qquad X\subseteq A,\quad Y\subseteq B,
\]
choose one minimizing the number of crossing edges.

Every vertex of \(X\cup Y\) already has at least \(k\) neighbours in its own class. If a vertex outside \(X\cup Y\) had more neighbours across the partition than within its class, moving it would strictly decrease the cut. This move preserves the prescribed cores and the nonemptiness of both classes, contradicting minimality. ∎

We also need an intersection observation.

### Lemma 2: intersections cannot be singletons

If \(P,Q\) are \(k\)-core sets in a graph of maximum degree at most \(2k-1\), then either \(P\cap Q=\varnothing\), or
\[
\delta(G[P\cap Q])\ge 1.
\]

**Proof.** For \(v\in P\cap Q\),
\[
\begin{aligned}
d_{P\cap Q}(v)
&=d_P(v)+d_Q(v)-d_{P\cup Q}(v)\\
&\ge 2k-(2k-1)=1.
\end{aligned}
\]
∎

In particular, if \(P\cap Q\subseteq\{x,y\}\), then a nonempty intersection must be exactly \(\{x,y\}\), with \(xy\in E(G)\).

## 3. A structural restriction on any counterexample

Suppose, for this section, that \(G\) is \((2k-1)\)-regular and has **no** friendly partition.

There exists a partition
\[
V(G)=A\mathbin{\dot\cup}B
\]
such that both induced graphs are \((k-1)\)-degenerate: take a maximum cut. Every vertex then has at most \(k-1\) neighbours in its own class.

Among all such degenerate partitions, choose one maximizing
\[
F(A,B)=e(G[A])+e(G[B]).
\]
Both classes are automatically nonempty, since \(G\) itself is not \((k-1)\)-degenerate.

Define the low-degree sets
\[
L_A=\{x\in A:d_A(x)\le k-1\},\qquad
L_B=\{y\in B:d_B(y)\le k-1\}.
\]
Both are nonempty by degeneracy.

### Lemma 3: the low-degree sets are completely joined

For this extremal partition:

1. every vertex of \(L_A\) has degree exactly \(k-1\) in \(A\);
2. every vertex of \(L_B\) has degree exactly \(k-1\) in \(B\);
3. every vertex of \(L_A\) is adjacent to every vertex of \(L_B\).

Consequently,
\[
1\le |L_A|,|L_B|\le k.
\]

**Proof.** Fix \(x\in L_A\). Moving \(x\) to \(B\) would increase \(F\) by
\[
(2k-1)-2d_A(x)\ge 1.
\]
Removing \(x\) preserves degeneracy of \(A\), so extremality implies that \(G[B\cup\{x\}]\) contains a \(k\)-core set \(Q_x\). Necessarily \(x\in Q_x\), since \(G[B]\) is degenerate.

Similarly, for every \(y\in L_B\), there is a \(k\)-core set
\[
P_y\subseteq A\cup\{y\},\qquad y\in P_y.
\]

By Lemma 1, \(P_y\) and \(Q_x\) cannot be disjoint. But
\[
P_y\cap Q_x\subseteq\{x,y\}.
\]
Lemma 2 therefore forces
\[
P_y\cap Q_x=\{x,y\},\qquad xy\in E(G).
\]

Since \(x\in P_y\subseteq A\cup\{y\}\), its degree in \(P_y\) is at most \(d_A(x)+1\). Hence
\[
k\le d_A(x)+1\le k,
\]
so \(d_A(x)=k-1\). The argument for \(y\) is symmetric.

Finally, every low-degree vertex has exactly \(k\) crossing neighbours, giving the asserted size bounds. ∎

For the 5-regular case, this says that an extremal partition into two 2-degenerate induced subgraphs has minimum degree two in both classes, and its degree-two sets form a complete bipartite graph \(K_{p,q}\), where \(1\le p,q\le3\).

## 4. Proof of the girth-five theorem

Assume now that \(G\) has no triangles and no four-cycles. Suppose for contradiction that it has no friendly partition, and choose the extremal degenerate partition above.

### 4.1. Finding degree-\(k\) neighbours

Because \(L_A\) and \(L_B\) are completely joined, triangle-freeness implies that each of \(L_A,L_B\) is independent.

Furthermore, every vertex of \(A\) has at most one neighbour in \(L_A\). Indeed, if \(w\in A\) had distinct neighbours \(x,x'\in L_A\), then any \(y\in L_B\) would give the four-cycle
\[
w,x,y,x',w.
\]
The symmetric assertion holds in \(B\).

I claim that there are vertices
\[
x\in L_A,\quad a\in A\setminus L_A
\]
such that
\[
xa\in E(G),\qquad d_A(a)=k.
\]

Otherwise, consider \(G[A\setminus L_A]\). This graph is nonempty: each vertex of \(L_A\) has \(k-1\ge1\) neighbours in \(A\), and \(L_A\) is independent.

A vertex of degree \(k\) in \(A\) would lose no neighbours when \(L_A\) is removed, by the supposition. A vertex of degree at least \(k+1\) would lose at most one. Thus
\[
\delta(G[A\setminus L_A])\ge k,
\]
contradicting degeneracy.

Symmetrically, choose
\[
y\in L_B,\quad b\in B\setminus L_B
\]
such that
\[
yb\in E(G),\qquad d_B(b)=k.
\]

By Lemma 3, \(xy\in E(G)\). Triangle-freeness gives
\[
ay\notin E(G),\qquad bx\notin E(G).
\]

### 4.2. A zero-cost exchange creates a four-cycle

Swap \(x\) and \(y\):
\[
A'=(A\setminus\{x\})\cup\{y\},\qquad
B'=(B\setminus\{y\})\cup\{x\}.
\]

Since \(y\) originally had \(k\) neighbours across the partition, one of which was \(x\),
\[
d_{A'}(y)=k-1.
\]
Likewise \(d_{B'}(x)=k-1\).

Adding a vertex with at most \(k-1\) neighbours to a \((k-1)\)-degenerate graph preserves degeneracy. Hence \((A',B')\) is admissible.

Moreover, each class loses \(k-1\) internal edges and gains \(k-1\), so
\[
F(A',B')=F(A,B).
\]
The new partition is therefore also extremal.

Now
\[
d_{A'}(a)=k-1,\qquad d_{B'}(b)=k-1,
\]
because \(a\) loses \(x\) and does not gain \(y\), while \(b\) loses \(y\) and does not gain \(x\).

Applying Lemma 3 to the new extremal partition forces \(ab\in E(G)\). But then
\[
x,a,b,y,x
\]
is a four-cycle, a contradiction. This proves the theorem. ∎

## 5. The proof can be implemented in polynomial time

The global optimization in the proof is not necessary for a construction.

Start from a cut that is locally maximum under single-vertex moves; both classes then have maximum internal degree at most \(k-1\). Maintain a partition into two \((k-1)\)-degenerate induced subgraphs.

Use the following procedure.

1. **Strict improvement.** If a low-degree vertex can be transferred while preserving degeneracy of the receiving class, transfer it. This increases \(F\) by at least one.

2. **Inspect a stalled partition.** If no such transfer is possible, every blocked transfer supplies a \(k\)-core set in the receiving class plus the transferred vertex.
   - If some low-degree vertex has internal degree below \(k-1\), the corresponding two blocked-transfer cores are disjoint.
   - If some opposite pair of low-degree vertices is nonadjacent, their blocked-transfer cores are disjoint.

   These assertions follow from exactly the intersection argument in Lemma 3. In either event, finish using Lemma 1.

3. **Exchange.** Otherwise, all the structural conclusions of Lemma 3 hold. Find \(x,a,y,b\) as in Section 4 and swap \(x,y\). The resulting low-degree vertices \(a,b\) are nonadjacent, since an edge \(ab\) would make a four-cycle.
   - If both transfers of \(a,b\) are blocked, their cores are disjoint.
   - Otherwise, perform an available transfer, strictly increasing \(F\).

Thus there is at most one zero-cost exchange between successive strict improvements. Since \(0\le F\le |E(G)|\), there are at most \(|E(G)|\) strict improvements.

Degeneracy and the existence of a \(k\)-core can be tested by repeatedly deleting vertices of degree below \(k\), in \(O(n+m)\) time. Testing all potential transfers gives, for example, an
\[
O\bigl(mn(n+m)\bigr)
\]
implementation, which is \(O(n^3)\) for each fixed degree. Finally, the core-extension step is also implemented by cut-decreasing single-vertex moves.

## 6. A complementary small-core criterion

The following bound applies **without any girth assumption**.

**Proposition.** Suppose a \((2k-1)\)-regular graph on \(n\) vertices contains a \(k\)-core set of size \(a\). If
\[
n>ka-k(k-1),
\]
then it has a friendly partition.

**Proof.** Let \(X\) be the given core, and put \(B=V(G)\setminus X\), \(b=|B|\). Since \(G[X]\) has minimum degree at least \(k\),
\[
e(X,B)\le (k-1)a.
\]

A \((k-1)\)-degenerate graph on \(b\ge k-1\) vertices has at most
\[
(k-1)b-\binom{k}{2}
\]
edges, by a degeneracy ordering. The size hypothesis ensures \(b\ge k-1\): indeed, \(a\ge k+1\), and
\[
b>(k-1)(a-k)\ge k-1.
\]

If \(G[B]\) were \((k-1)\)-degenerate, regularity would give
\[
e(X,B)
=(2k-1)b-2e(G[B])
\ge b+k(k-1).
\]
Consequently,
\[
n=a+b\le ka-k(k-1),
\]
a contradiction. Thus \(B\) contains another \(k\)-core, and Lemma 1 applies. ∎

In particular:

- A 5-regular graph containing a 3-core on \(a\) vertices has a friendly partition whenever \(n>3a-6\).
- Every 5-regular graph containing \(K_4\), other than \(K_6\), has a friendly partition.
- More generally, a \((2k-1)\)-regular graph containing \(K_{k+1}\) has a friendly partition whenever \(n>2k\).

The same edge count gives another sufficient condition in degree five: a bisection with fewer than
\[
\frac n2+6
\]
crossing edges forces both sides to contain 3-cores. By parity, this condition can equivalently be written as a cut size at most \(n/2+4\).

## 7. What remains unresolved

The argument does **not** bound the order of all counterexamples for any unresolved degree.

For example, a 5-regular counterexample on more than six vertices would have to:

- be \(K_4\)-free;
- contain a triangle or a four-cycle;
- exhibit the complete-bipartite low-degree pattern from Lemma 3 in every extremal partition into two 2-degenerate induced subgraphs.

These conditions still permit graphs of arbitrarily large order. When short cycles are allowed, the independence and distinct-neighbour arguments in Section 4 fail, and the final exchange can produce a four-cycle without contradiction. I have not shown that this remaining configuration forces a bound on \(n\), which is the missing step toward the original conjecture.
