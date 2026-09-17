Attack the following open graph-theory problem.

Catalog id: partition_of_a_cubic_3_connected_graphs_into_paths_of_length_2
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Paths
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partition_of_a_cubic_3_connected_graphs_into_paths_of_length_2/
Original entry: http://www.openproblemgarden.org/op/partition_of_a_cubic_3_connected_graphs_into_paths_of_length_2
Problem attributed to: Kelmans, Alexander K. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Partition of a cubic 3-connected graphs into paths of length 2.
Problem Does every $ 3 $ -connected cubic graph on $ 3k $ vertices admit a partition into $ k $ paths of length $ 2 $ ?

=== Discussion / context (OpenProblemGarden) ===
More generally, the following question is posed. Problem Does every $ 3 $ -connected cubic graph on at least $ 3k $ vertices contain $ k $ pairwise vertex-disjoint paths of length $ 2 $ ? In [K1], Kelmans gave a construction that provided infinitely many 2-connected graphs for which the above statement is false.

=== References listed by OpenProblemGarden ===
- [K1] Alexander K. Kelmans, Packing 3-vertex paths in 2-connected graphs
- *[K2] Alexander K. Kelmans, On --Packing in 3--connected Graphs, RUTCOR Research Report 23--2005, Rutgers University. See also Packing 3-vertex Paths In Cubic 3-connected Graphs

=== Catalog page (statement + literature review) ===
Partition of a cubic 3-connected graphs into paths of length 2. — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture—that every 3-connected cubic graph on $3k$ vertices admits a partition into $k$ paths of length 2 (a $P_3$-factor)—remains open. Prior to the OPG posting, Kelmans established several equivalent reformulations and showed the conjecture implies Reed’s dominating conjecture for cubic 3-connected graphs, but no proof or disproof exists. Searches through 2026 found no post-2013 paper that resolves the problem.

 Reviewer notes. The problem is also attributed to Akiyama and Kano (1985 conjecture). All relevant arXiv papers found (0910.2766, 0801.1239, 0711.3871, 0712.4151, 0910.4681) predate the 2013 posting. Two possibly relevant post-2013 papers were identified — 'On maximum P3-packing in claw-free subcubic graphs' (J. Comb. Opt., 2021) and 'Packing 2- and 3-stars into cubic graphs' (ScienceDirect, 2023) — but both were behind paywalls (HTTP 403) and no arXiv versions were found; they also appear to address different graph classes (claw-free subcubic vs. stars). Confidence is medium rather than high because those inaccessible papers could in principle contain relevant partial results.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Problem. Does every $ 3 $ -connected cubic graph on $ 3k $ vertices admit a partition into $ k $ paths of length $ 2 $ ?

Discussion

More generally, the following question is posed. Problem Does every $ 3 $ -connected cubic graph on at least $ 3k $ vertices contain $ k $ pairwise vertex-disjoint paths of length $ 2 $ ? In [K1], Kelmans gave a construction that provided infinitely many 2-connected graphs for which the above statement is false.

Bibliography

 [K1]
 Alexander K. Kelmans, Packing 3-vertex paths in 2-connected graphs
 Packing 3-vertex paths in 2-connected graphs

★ [K2]
 Alexander K. Kelmans, On $ \Lambda $ --Packing in 3--connected Graphs, RUTCOR Research Report 23--2005, Rutgers University. See also Packing 3-vertex Paths In Cubic 3-connected Graphs
 Packing 3-vertex Paths In Cubic 3-connected Graphs

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I construct optimal P3-packings for every generalized Petersen graph and a larger periodically interleaved class, even after deleting any one outer-cycle edge.",
  "would_publish": false,
  "caveats": "The general conjecture is not settled here; no novelty claim is made for this elementary special case."
}
```

# A constructive special case

I do not obtain a proof or counterexample for arbitrary cubic 3-connected graphs. The result below settles both questions in the prompt for an explicit infinite class containing all generalized Petersen graphs.

Paths are not required to be induced. Write \(\nu_3(G)\) for the maximum number of pairwise vertex-disjoint three-vertex paths in \(G\).

## 1. The class and the theorem

Let \(N=d\ell\), where \(d\geq 1\) and \(\ell\geq 3\). Construct a graph \(G\) on
\[
\{u_i,v_i:i\in\mathbb Z_N\}
\]
as follows:

* the \(u_i\) form the **outer cycle**
  \[
  u_0u_1\cdots u_{N-1}u_0;
  \]
* add every spoke \(u_iv_i\);
* for each \(r\in\{0,\ldots,d-1\}\), put an arbitrary simple cycle on
  \[
  W_r=\{v_{r+td}:0\leq t<\ell\}.
  \]

There are no other edges. Thus the inner cycles all have length \(\ell\), and their spoke endpoints are periodically interleaved around the outer cycle. Their internal cyclic order is unrestricted.

**Theorem.** Every such graph is cubic and 3-connected. Moreover, for every outer-cycle edge \(e\),
\[
\boxed{\quad
\nu_3(G-e)=\nu_3(G)=\left\lfloor\frac{2N}{3}\right\rfloor.
\quad}
\]
Consequently, if \(3\mid N\), then \(G\) has a \(P_3\)-factor avoiding any prescribed outer-cycle edge.

The construction is linear-time when the displayed decomposition is supplied.

## 2. Packing construction

The upper bound \(\nu_3(G)\leq\lfloor 2N/3\rfloor\) is immediate. We construct a packing attaining it in \(G-e\).

Rotate the indexing so that
\[
e=u_{N-1}u_0.
\]
This preserves the residue-class description of the inner cycles. We will use outer edges only from the path
\[
u_0u_1\cdots u_{N-1}.
\]

Recall that a path whose order is divisible by three can be partitioned into consecutive three-vertex paths. The same holds for a cycle of order divisible by three, by first ignoring one cycle edge.

### Case A: \(\ell\equiv0\pmod3\)

Every inner cycle has order divisible by three, as does \(N=d\ell\). Partition each inner cycle into \(P_3\)'s, and partition the outer path into \(P_3\)'s.

This gives a \(P_3\)-factor of \(G-e\).

### Case B: \(\ell\equiv1\pmod3\)

Here \(\ell\geq4\). We will remove one vertex from each inner cycle, covering each removed vertex together with two adjacent outer vertices.

Consider the \(d\) disjoint outer pairs
\[
B_j=\{u_{2j},u_{2j+1}\},
\qquad 0\leq j<d.
\]
We need to choose
\[
a_j\in\{2j,2j+1\}
\]
so that the residues \(a_j\bmod d\) are all distinct.

Such a choice is explicit:

* if \(d\) is odd, take \(a_j=2j\);
* if \(d=2h\), take
  \[
  a_j=
  \begin{cases}
  2j,&0\leq j<h,\\
  2j+1,&h\leq j<2h.
  \end{cases}
  \]
  The first group represents the even residues modulo \(d\), and the second represents the odd residues.

Let \(b_j\) be the other member of \(\{2j,2j+1\}\). Select the paths
\[
v_{a_j}-u_{a_j}-u_{b_j},
\qquad 0\leq j<d.
\]
They are pairwise vertex-disjoint. They cover all outer vertices
\[
u_0,\ldots,u_{2d-1}
\]
and exactly one vertex of every inner cycle.

Each inner cycle now leaves a path of order \(\ell-1\), divisible by three, so tile all these paths. At this point we have covered all \(N\) inner vertices and \(2d\) outer vertices with
\[
\frac{N+2d}{3}
\]
paths. This is an integer because \(N+2d=d(\ell+2)\).

The remaining outer vertices form the path
\[
u_{2d}u_{2d+1}\cdots u_{N-1}.
\]
Tile it greedily, leaving at most two vertices. The total number of paths is
\[
\frac{N+2d}{3}
+\left\lfloor\frac{N-2d}{3}\right\rfloor
=
\left\lfloor\frac{2N}{3}\right\rfloor.
\]

### Case C: \(\ell\equiv2\pmod3\)

We instead remove two adjacent vertices from each inner cycle.

For each \(r\in\{0,\ldots,d-1\}\), choose an inner-cycle neighbor \(w_r\) of \(v_r\), and select
\[
u_r-v_r-w_r.
\]
These paths are vertex-disjoint: their outer vertices are distinct, and their inner vertices belong to distinct inner cycles.

Deleting \(v_r,w_r\) from their inner cycle leaves a path of order \(\ell-2\), divisible by three. Tile every such path.

We have now covered all inner vertices and the consecutive outer vertices
\[
u_0,\ldots,u_{d-1}
\]
with
\[
\frac{N+d}{3}
\]
paths. The remaining outer path has order \(N-d\), so the total becomes
\[
\frac{N+d}{3}
+\left\lfloor\frac{N-d}{3}\right\rfloor
=
\left\lfloor\frac{2N}{3}\right\rfloor.
\]

These three cases exhaust all possibilities. None uses \(e\), proving the packing assertion. Any uncovered vertices are the final one or two vertices of the remaining outer path.

## 3. Verification of 3-connectivity

Cubicity and connectedness follow directly from the construction. We first prove 3-edge-connectivity.

Suppose that a nonempty proper vertex set \(S\) satisfies
\[
|\delta(S)|\leq2,
\]
and put
\[
I=\{i:u_i\in S\}.
\]

### All outer vertices lie on one side

If \(I\) is empty or all of \(\mathbb Z_N\), replace \(S\) by its complement if necessary, so that \(S\) contains only inner vertices.

Every vertex of \(S\) contributes its spoke to \(\delta(S)\), hence \(|S|\leq2\). Since every inner cycle has at least three vertices, some inner cycle meets \(S\) properly and contributes at least two additional cut edges. Therefore
\[
|\delta(S)|\geq |S|+2\geq3,
\]
a contradiction.

### Outer vertices occur on both sides

The outer cycle contributes at least two cut edges. Thus it contributes exactly two, and no spoke or inner-cycle edge crosses the cut.

The absence of cut spokes gives
\[
u_i\in S\iff v_i\in S.
\]
The absence of cut inner edges means that each \(W_r\) lies entirely on one side. Hence \(I\) is a union of residue classes modulo \(d\).

Its nonconstant membership pattern therefore repeats \(\ell\) times around the outer cycle. Each period has at least two transitions, so the outer cycle contributes at least
\[
2\ell\geq6
\]
cut edges—a contradiction. For \(d=1\), a nonempty proper union of residue classes is already impossible.

Thus \(G\) is 3-edge-connected.

For completeness, a cubic 3-edge-connected graph is 3-vertex-connected. A cut vertex would leave a component with at most one incident cut edge. If \(\{x,y\}\) were a two-vertex separator, every component of \(G-\{x,y\}\) would have at least three boundary edges. Degree counting forces exactly two components, each with three boundary edges, and \(xy\notin E(G)\). Each component attaches to both \(x\) and \(y\), since there is no cut vertex. Adding to one component the separator vertex incident with two of its three boundary edges then produces a two-edge cut, again a contradiction.

This completes the theorem.

## 4. Application to generalized Petersen graphs

Define the generalized Petersen graph \(\operatorname{GP}(N,s)\), where
\[
1\leq s<N/2,
\]
by the edges
\[
u_i u_{i+1},\qquad u_iv_i,\qquad v_iv_{i+s},
\]
with subscripts modulo \(N\).

Set
\[
d=\gcd(N,s),\qquad \ell=N/d.
\]
The inner edges form \(d\) cycles of length \(\ell\), whose vertex sets are exactly the residue classes modulo \(d\). The parameter restriction ensures \(\ell\geq3\). Thus the theorem applies and gives
\[
\nu_3\bigl(\operatorname{GP}(N,s)\bigr)
=
\left\lfloor\frac{2N}{3}\right\rfloor.
\]

In particular:

* if \(3\mid N\), the graph has a \(P_3\)-factor;
* for every \(k\) with \(3k\leq2N\), it contains \(k\) vertex-disjoint \(P_3\)'s;
* an optimal packing can avoid any prescribed outer-cycle edge.

## 5. Where the argument stops

The proof depends on a particular spanning cycle-and-spoke decomposition and on the periodic placement of the inner cycles’ attachment vertices. The residue-transversal choice in Case B is the key feature supplied by this arrangement.

An arbitrary cubic 3-connected graph need not have this structure, and the argument does not handle a general 2-factor with irregular links between its cycles. Thus the original conjecture remains unsettled by this work. No literature novelty claim is made for the special-case construction above.
