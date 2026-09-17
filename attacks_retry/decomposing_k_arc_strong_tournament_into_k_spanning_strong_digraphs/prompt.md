Attack the following open graph-theory problem.

Catalog id: decomposing_k_arc_strong_tournament_into_k_spanning_strong_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs » Tournaments
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/decomposing_k_arc_strong_tournament_into_k_spanning_strong_digraphs/
Original entry: http://www.openproblemgarden.org/op/decomposing_k_arc_strong_tournament_into_k_spanning_strong_digraphs
Problem attributed to: Bang-Jensen, Joergen, Yeo, Anders (posted 2013-03-15)

=== Problem statement (OpenProblemGarden) ===
Title: Decomposing k-arc-strong tournament into k spanning strong digraphs
Conjecture Every k-arc-strong tournament decomposes into k spanning strong digraphs.

=== Discussion / context (OpenProblemGarden) ===
Conjecture 8 implies Kelly's conjecture ( Every regular tournament of order $ n $ can be decomposed into $ (n-1)/2 $ Hamilton directed cycles. ) which has been proved for tournaments of sufficiently large order by Kühn and Osthus [KO]. Bang-Jensen and Yeo [BY] gave several results supporting this conjecture. For example they proved it for $ k $ -arc-strong tournaments with minimum in- and out-degree at least $ 37k $ .

=== References listed by OpenProblemGarden ===
- *[BY] J. Bang-Jensen, A. Yeo, Decomposing k-arc-strong tournaments into strong spanning subdigraphs, Combinatorica 24 (2004) 331–349.
- [KO] Daniela Kühn and Deryk Osthus, Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments, Advances in Mathematics 237 (2013), 62-146.

=== Catalog page (statement + literature review) ===
Decomposing k-arc-strong tournament into k spanning strong digraphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture that every $k$-arc-strong tournament decomposes into $k$ spanning strong digraphs remains open. The best known partial result from Bang-Jensen and Yeo (2004) covers $k$-arc-strong tournaments with minimum in- and out-degree at least $37k$. Post-2013 work has extended arc-disjoint strong spanning subdigraph results to broader classes (semicomplete compositions) but has not resolved the original conjecture for tournaments.

 Cited literature (1)

 
 
 
partial Arc-disjoint Strong Spanning Subdigraphs of Semicomplete Compositions
 (2019)
 

 
 Joergen Bang-Jensen, Gregory Gutin, Anders Yeo · arXiv preprint · arXiv:1903.12225

Characterizes digraph compositions (with a semicomplete base digraph) that admit a strong arc decomposition, extending the framework of Bang-Jensen–Yeo to a broader class than tournaments.
 

 

 Reviewer notes. The Wiley Online Library pages for 'Strong arc decompositions of split digraphs' (JGT 2025) and 'Making a tournament k-strong' (JGT 2023) and 'Arc-disjoint strong spanning subdigraphs of semicomplete compositions' (JGT 2020) returned HTTP 403 and could not be verified. The 2024 arXiv paper 2408.02260 on split digraphs is related but does not address the tournament conjecture directly. No post-2013 paper resolving the original conjecture was found in 4 search rounds. Kelly's conjecture (implied by this conjecture) was proved for large tournaments by Kühn–Osthus (2013), but that does not resolve the stronger Bang-Jensen–Yeo conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Every k-arc-strong tournament decomposes into k spanning strong digraphs.

Discussion

Conjecture 8 implies Kelly's conjecture ( Every regular tournament of order $ n $ can be decomposed into $ (n-1)/2 $ Hamilton directed cycles. ) which has been proved for tournaments of sufficiently large order by Kühn and Osthus [KO]. Bang-Jensen and Yeo [BY] gave several results supporting this conjecture. For example they proved it for $ k $ -arc-strong tournaments with minimum in- and out-degree at least $ 37k $ .

Bibliography

★ [BY]
 J. Bang-Jensen, A. Yeo, Decomposing k-arc-strong tournaments into strong spanning subdigraphs, Combinatorica 24 (2004) 331–349.

 [KO]
 Daniela Kühn and Deryk Osthus, Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments, Advances in Mathematics 237 (2013), 62-146.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every k-arc-strong tournament having a directed cut of size k with both sides non-singleton admits the required decomposition.",
  "would_publish": false,
  "caveats": "The singleton-minimum-cut case remains untreated; novelty of this sufficient condition has not been checked."
}
```

# A partial theorem: nontrivial minimum cuts suffice

I do not obtain a proof or counterexample to the full conjecture. I prove a structural special case, together with a restriction on possible counterexamples. I do not claim this sufficient condition is new; it may already occur in the literature supplied in the question.

For a digraph \(D\), write
\[
d_D^+(X)=|E_D(X,V(D)\setminus X)|,\qquad
d_D^-(X)=|E_D(V(D)\setminus X,X)|.
\]
Thus \(D\) is \(k\)-arc-strong precisely when every nonempty proper vertex set \(X\) satisfies \(d_D^+(X)\ge k\). Equivalently, every such set satisfies \(d_D^-(X)\ge k\).

Producing \(k\) pairwise arc-disjoint spanning strong subdigraphs is sufficient: any unused arcs can be assigned arbitrarily to those subdigraphs.

## 1. The partial result

**Theorem.** Let \(T\) be a \(k\)-arc-strong tournament, where \(k\ge1\). Suppose
\[
V(T)=A\mathbin{\dot\cup}B,\qquad |A|,|B|\ge2,
\]
and exactly \(k\) arcs are directed from \(B\) to \(A\). Then \(T\) decomposes into \(k\) spanning strong digraphs.

In particular, if a tournament has a minimum directed cut with both sides non-singleton, then it decomposes into as many spanning strong digraphs as its arc-connectivity.

The proof uses rooted arborescence packing within the two sides, and a bipartite edge-colouring argument to join the resulting structures.

## 2. A bipartite edge-cover lemma

**Lemma 1.** Let \(G\) be a finite bipartite graph with minimum degree at least \(k\). Its edges can be partitioned into \(k\) sets
\[
F_1,\ldots,F_k
\]
such that every vertex is incident with an edge of every \(F_i\).

Here the \(F_i\) are edge covers, not necessarily matchings.

**Proof.** At each vertex, partition its incident edges into groups of size \(k\), together with at most one residual group of size less than \(k\). Split the vertex into one new vertex for each group, retaining the corresponding incidences. Do this on both sides of the bipartition.

The resulting bipartite graph has maximum degree at most \(k\). Moreover, every original vertex has at least one corresponding split vertex of degree exactly \(k\).

The split graph has a proper edge-colouring with \(k\) colours. For completeness, this follows by completing it to a \(k\)-regular bipartite multigraph and repeatedly removing perfect matchings. Such a completion is obtained by first equalizing the two part sizes with isolated vertices and then joining deficient vertices, allowing parallel edges. Hall’s condition holds in every regular bipartite multigraph.

Project the colouring back to the original graph. At a degree-\(k\) split vertex all \(k\) colours occur, so every original vertex is incident with every colour. The colour classes give the required partition. \(\square\)

## 3. A tight-cut gluing lemma

The following statement applies more generally than to tournaments.

**Lemma 2.** Let \(D\) be a \(k\)-arc-strong digraph with a partition
\[
V(D)=A\mathbin{\dot\cup}B
\]
into nonempty sets. Suppose:

1. exactly \(k\) arcs go from \(B\) to \(A\);
2. every vertex of \(A\) has at least \(k\) outgoing arcs to \(B\);
3. every vertex of \(B\) has at least \(k\) incoming arcs from \(A\).

Then \(D\) decomposes into \(k\) spanning strong digraphs.

**Proof.** Label the arcs from \(B\) to \(A\) as
\[
e_i=b_i a_i,\qquad 1\le i\le k.
\]
The vertices \(a_i\), or the vertices \(b_i\), need not be distinct.

We use the standard **rooted arborescence-packing theorem**:

> A digraph with distinguished root \(r\) contains \(k\) pairwise arc-disjoint spanning out-arborescences rooted at \(r\) if and only if every nonempty set not containing \(r\) has at least \(k\) entering arcs.

This theorem also holds for directed multigraphs, which is relevant to the auxiliary constructions below.

### Out-arborescences on \(A\)

Form \(D_A\) from \(D[A]\) by adding a new source \(r\) and the \(k\) labelled arcs
\[
ra_1,\ldots,ra_k.
\]
These may include parallel arcs. For every nonempty \(X\subseteq A\),
\[
\begin{aligned}
d_{D_A}^-(X)
&=d_{D[A]}^-(X)+|\{i:a_i\in X\}|\\
&=d_D^-(X)\\
&\ge k.
\end{aligned}
\]
The second equality holds because \(e_1,\ldots,e_k\) are all the arcs from \(B\) to \(A\).

Consequently, \(D_A\) contains \(k\) arc-disjoint spanning out-arborescences rooted at \(r\). Each uses at least one arc leaving \(r\); there are exactly \(k\) such arcs altogether. Therefore each arborescence uses exactly one, and all these arcs are used.

After deleting \(r\), and indexing by the labelled arc \(ra_i\), we obtain pairwise arc-disjoint spanning out-arborescences
\[
O_i\subseteq D[A]
\]
rooted at \(a_i\).

### In-arborescences on \(B\)

Dually, add a new sink \(s\) to \(D[B]\), with labelled arcs
\[
b_1s,\ldots,b_ks.
\]
For every nonempty \(Y\subseteq B\), its outgoing cut in this auxiliary digraph has size
\[
d_{D[B]}^+(Y)+|\{i:b_i\in Y\}|=d_D^+(Y)\ge k.
\]
Applying the arborescence-packing theorem to the reversed digraph and then deleting \(s\) gives pairwise arc-disjoint spanning in-arborescences
\[
I_i\subseteq D[B]
\]
rooted at \(b_i\).

Thus every vertex of \(B\) can reach \(b_i\) in \(I_i\).

### Joining the two sides

Let \(G\) be the bipartite graph whose edges correspond to the arcs from \(A\) to \(B\). Conditions 2 and 3 give \(\delta(G)\ge k\). By Lemma 1, partition these arcs into sets
\[
F_1,\ldots,F_k
\]
such that, for each \(i\),

- every \(a\in A\) has an outgoing arc in \(F_i\);
- every \(b\in B\) has an incoming arc in \(F_i\).

Define
\[
H_i=O_i\cup I_i\cup\{b_i a_i\}\cup F_i
\]
on the full vertex set \(V(D)\).

To verify strong connectivity, use \(a_i\) as a reference vertex.

- It reaches every vertex of \(A\) through \(O_i\).
- It reaches every \(b\in B\): choose an arc \(ab\in F_i\), first reach \(a\) through \(O_i\), and then traverse \(ab\).
- Every vertex of \(B\) reaches \(b_i\) through \(I_i\), and then reaches \(a_i\) through \(b_i a_i\).
- Every \(a\in A\) has an arc \(ab\in F_i\), and hence reaches \(a_i\) through \(b\), \(I_i\), and \(b_i a_i\).

Therefore \(H_i\) is strongly connected.

The \(H_i\) are pairwise arc-disjoint: the two arborescence packings are arc-disjoint within their respective sides, the \(e_i\) are distinct, and the \(F_i\) partition the forward crossing arcs. Assign any remaining internal arcs arbitrarily to the \(H_i\). This gives a decomposition of all of \(D\). \(\square\)

## 4. Why a nontrivial tight cut in a tournament satisfies the lemma

We now prove the theorem.

Let
\[
a=|A|,\qquad b=|B|.
\]
Since \(T\) is \(k\)-arc-strong, every vertex has indegree and outdegree at least \(k\).

Summing indegrees over \(A\), and using the fact that exactly \(k\) arcs enter \(A\) from \(B\), gives
\[
ka
\le \sum_{v\in A}d_T^-(v)
=\binom a2+k.
\]
Equivalently,
\[
(a-1)(a-2k)\ge0.
\]
Because \(a\ge2\), this forces
\[
a\ge2k.
\]

Similarly, summing outdegrees over \(B\) gives
\[
kb\le \binom b2+k,
\]
and therefore
\[
b\ge2k.
\]

Now consider the bipartite graph of arcs from \(A\) to \(B\). Every vertex of \(A\) has at least
\[
b-k\ge k
\]
outgoing arcs to \(B\), since at most \(k\) of its pairs with \(B\) can be oriented backwards. Likewise, every vertex of \(B\) has at least
\[
a-k\ge k
\]
incoming arcs from \(A\).

All hypotheses of Lemma 2 hold. This proves the theorem. \(\square\)

Notice the useful accompanying fact:

> In a \(k\)-arc-strong tournament, a directed cut of size exactly \(k\) has each side either a singleton or of order at least \(2k\).

## 5. Consequences

Let
\[
\lambda(T)=\min_{\varnothing\ne X\subsetneq V(T)}d_T^+(X)
\]
be the arc-connectivity, and let
\[
\delta^0(T)=\min_{v\in V(T)}\min\{d_T^+(v),d_T^-(v)\}.
\]

### A restriction on counterexamples

**Corollary.** If
\[
\lambda(T)<\delta^0(T),
\]
then \(T\) decomposes into \(\lambda(T)\) spanning strong digraphs. Consequently, it has the required decomposition for every \(k\le\lambda(T)\).

**Proof.** A cut with a singleton side has size equal to some vertex’s indegree or outdegree, and hence at least \(\delta^0(T)\). Thus a minimum cut cannot have a singleton side. Apply the theorem with \(k=\lambda(T)\).

To obtain fewer than \(\lambda(T)\) parts, merge parts of this decomposition. A union containing a spanning strong digraph remains spanning and strong. \(\square\)

More generally, any counterexample to the original conjecture must satisfy both
\[
\lambda(T)=\delta^0(T)
\]
and

\[
\text{every minimum directed cut has a singleton side.}
\]

### Closure under balanced vertex additions

There is also a simple extension principle. Suppose a tournament already has \(k\) arc-disjoint spanning strong subdigraphs. Add a vertex \(v\) having at least \(k\) in-neighbours and at least \(k\) out-neighbours in the existing tournament. Choose distinct arcs
\[
x_i v,\quad vy_i,\qquad 1\le i\le k,
\]
and add the pair \(x_iv,vy_i\) to part \(i\). Each part becomes strong on the enlarged vertex set.

Thus the class proved above can be enlarged by any sequence of such vertex additions, even if the resulting tournament no longer has a nontrivial minimum cut.

## 6. An explicit family with minimum semi-degree exactly \(k\)

The theorem applies well below the supplied sufficient hypothesis \(\delta^0(T)\ge37k\).

Take two disjoint regular tournaments \(R_A,R_B\), each of order
\[
m=2k+1.
\]
Such tournaments exist, for example by orienting \(i\to i+j\) modulo \(m\) for \(1\le j\le k\).

Initially orient every crossing pair from \(A\) to \(B\), and then reverse any \(k\) distinct crossing arcs.

The resulting tournament \(T\) has exactly \(k\) arcs from \(B\) to \(A\). It is \(k\)-arc-strong. Indeed, in a regular tournament of order \(2k+1\), a set of \(s\) vertices has outgoing cut size
\[
ks-\binom s2
=\frac{s(2k+1-s)}2
\ge k
\qquad(1\le s\le2k).
\]
Any cut of \(T\) that splits either block therefore has at least \(k\) outgoing arcs within that block. The only other nonempty proper cuts separate the two whole blocks, and their sizes are \(k\) and \(m^2-k\).

Hence
\[
\lambda(T)=k.
\]
Also \(\delta^0(T)=k\): internal degrees are already \(k\), and some vertex of \(A\) receives no reversed crossing arc. The theorem therefore gives the desired decomposition for every tournament in this family.

This example does not establish novelty relative to other results of Bang-Jensen–Yeo; it simply exhibits the scope of the proved criterion.

## 7. The remaining gap

The proof does not handle a minimum cut with a singleton side. In that situation, the forward bipartite graph has degree at most one at every vertex on the opposite side, so the \(k\)-fold edge-cover construction cannot work for \(k\ge2\).

This gap includes the regular tournaments central to the problem. If \(T\) is regular of order \(2k+1\), then
\[
d_T^+(X)=\frac{|X|(2k+1-|X|)}2.
\]
Its minimum cuts have size \(k\), attained only when one side is a singleton.

Moreover, such a tournament has exactly \(k|V(T)|\) arcs. Every spanning strong subdigraph has at least \(|V(T)|\) arcs. Consequently, any decomposition into \(k\) spanning strong subdigraphs would have exactly \(|V(T)|\) arcs in each part, forcing every part to be a directed Hamilton cycle.

Thus the argument settles a structurally defined subclass and rules out nontrivial minimum cuts in any counterexample, but it does not resolve the full conjecture.
