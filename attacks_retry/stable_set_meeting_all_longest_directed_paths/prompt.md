Attack the following open graph-theory problem.

Catalog id: stable_set_meeting_all_longest_directed_paths
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/stable_set_meeting_all_longest_directed_paths/
Original entry: http://www.openproblemgarden.org/op/stable_set_meeting_all_longest_directed_paths
Problem attributed to: Laborde, Jean-Marie, Payan, Charles, Xuong N.H. (posted 2013-03-01)

=== Problem statement (OpenProblemGarden) ===
Title: Stable set meeting all longest directed paths.
Conjecture Every digraph has a stable set meeting all longest directed paths

=== Discussion / context (OpenProblemGarden) ===
If the stability number is 1, that is if the digraph is a tournament, it follows Redei's Theorem stating that every tournament has a directed hamiltonian path. The conjecture has been proved by Havet [H] for digraphs having stability number 2. The conjecture would give an easy inductive proof of Gallai-Roy Theorem: every digraph with chromatic number $ k $ contains a directed path on $ k $ vertices. Hahn and Jackson [HJ] conjectured that in contrast there is no directed path meeting every maximum stable set. In fact, they conjectured the following: For each positive integer $ k $ , there is a digraph $ D $ with stability number $ k $ such that deleting the vertices of any $ k-1 $ directed paths in $ D $ leaves a digraph with stability number $ k $ . This was proved by Fox and Sudakov [FS] by a probabilistic argument.

=== References listed by OpenProblemGarden ===
- [FS] J. Fox and B. Sudakov, Paths and stability number in digraphs, Electronic Journal of Combiantorics, 16 (2009), no.1, N23.
- [HJ] G. Hahn and B. Jackson, A note concerning paths and independence number in digraphs, Discrete Math. 82 (1990), 327–329.
- [H] F. Havet. Stable set meeting every longest path. Discrete Mathematics, 289 (2004), no. 1-3, 169-173.
- *[LPX] J.M. Laborde, C. Payan, and N.H. Xuong, Independent sets and longest directed paths in digraphs. In Graphs and other Combinatorial Topics (Prague, 1982)}, Teubner-Texte Math., Vol. 59 (1983), 173-177, Teubner, Leipzig.

=== Catalog page (statement + literature review) ===
Stable set meeting all longest directed paths. — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that every digraph has a stable set meeting all longest directed paths remains open. The only verified partial result—Havet's 2004 proof for digraphs with stability number at most 2—predates the OPG posting, as does Fox and Sudakov's 2009 proof of the complementary Hahn-Jackson conjecture. No post-2013 papers extending the conjecture to stability number $\geq 3$ or to the general case were found in multiple targeted searches.

 Reviewer notes. The DMGT article at dmgt.uz.zgora.pl/publish/article.php?doi=1650 appeared repeatedly in searches but was inaccessible due to SSL certificate errors. The AJC 2014 paper (ajc.maths.uq.edu.au/pdf/59/ajc_v59_p311.pdf) was a binary PDF that could not be read; it is possible this contains a partial result on this conjecture. All clearly post-2013 arXiv papers found (arXiv:2402.16776 on Thomassé's conjecture; arXiv:2302.04986 on P5-free graphs) are unrelated to the LPX conjecture. Confidence is medium rather than high due to these two inaccessible sources.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. Every digraph has a stable set meeting all longest directed paths

Discussion

If the stability number is 1, that is if the digraph is a tournament, it follows Redei's Theorem stating that every tournament has a directed hamiltonian path. The conjecture has been proved by Havet [H] for digraphs having stability number 2. The conjecture would give an easy inductive proof of Gallai-Roy Theorem: every digraph with chromatic number $ k $ contains a directed path on $ k $ vertices. Hahn and Jackson [HJ] conjectured that in contrast there is no directed path meeting every maximum stable set. In fact, they conjectured the following: For each positive integer $ k $ , there is a digraph $ D $ with stability number $ k $ such that deleting the vertices of any $ k-1 $ directed paths in $ D $ leaves a digraph with stability number $ k $ . This was proved by Fox and Sudakov [FS] by a probabilistic argument.

Bibliography

 [FS]
 J. Fox and B. Sudakov, Paths and stability number in digraphs, Electronic Journal of Combiantorics, 16 (2009), no.1, N23.

 [HJ]
 G. Hahn and B. Jackson, A note concerning paths and independence number in digraphs, Discrete Math. 82 (1990), 327–329.

 [H]
 F. Havet. Stable set meeting every longest path. Discrete Mathematics, 289 (2004), no. 1-3, 169-173.

★ [LPX]
 J.M. Laborde, C. Payan, and N.H. Xuong, Independent sets and longest directed paths in digraphs. In Graphs and other Combinatorial Topics (Prague, 1982)}, Teubner-Texte Math., Vol. 59 (1983), 173-177, Teubner, Leipzig.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for digraphs made acyclic by deleting one vertex, even for maximum-weight paths with arbitrary positive vertex weights.",
  "would_publish": false,
  "caveats": "The general case is not resolved; novelty of this special case has not been verified."
}
```

## 1. A constructive special case

I obtain the following self-contained partial result. I do not claim that this special case is new.

All digraphs below are finite and loopless; antiparallel arcs are allowed. Paths have distinct vertices. A set is **stable** if no arc joins two of its vertices in either direction.

### Theorem
Let \(D\) be a digraph and let \(x\in V(D)\) satisfy that \(D-x\) is acyclic. Give every vertex \(v\) a positive weight \(w(v)\).

Then there is a stable set \(S\) **containing \(x\)** that meets every maximum-weight directed path of \(D\).

For unit weights, such a set can be constructed in \(O(|V(D)|+|A(D)|)\) time when \(x\) is supplied.

Thus the conjecture holds for digraphs with directed feedback vertex number at most one. The requirement that \(S\) contain the specified feedback vertex is an additional conclusion.

The proof gives a useful dichotomy: either deleting \(x\) strictly decreases the maximum path weight, or a suitable longest-path layer of \(D-x\) is entirely nonadjacent to \(x\).

## 2. Critical layers in a weighted DAG

Let \(H\) be a nonempty acyclic digraph with positive vertex weights, and let
\[
L=\max\{w(P):P\text{ is a directed path of }H\}.
\]
For \(v\in V(H)\), define
\[
p(v)=\max\{w(P):P\text{ ends at }v\},\qquad
q(v)=\max\{w(P):P\text{ starts at }v\}.
\]

A maximum-weight path ending at \(v\) and one starting at \(v\) have no other vertex in common: otherwise their union would contain a directed cycle. Consequently,
\[
p(v)+q(v)-w(v)\le L. \tag{1}
\]

Call \(v\) **critical** when equality holds in (1), and write \(\mathcal C\) for the critical vertices. For \(v\in\mathcal C\), put
\[
J_v=(p(v)-w(v),\,p(v)].
\]
For \(0<t\le L\), define
\[
F_t=\{v\in\mathcal C:t\in J_v\}.
\]

These sets have two important properties.

### Lemma
For every \(t\in(0,L]\), the set \(F_t\) is stable and meets every maximum-weight path of \(H\).

#### Proof
If \(u\to v\) is an arc of \(H\), acyclicity allows a maximum-weight path ending at \(u\) to be extended to \(v\). Thus
\[
p(v)\ge p(u)+w(v),
\]
and hence
\[
p(v)-w(v)\ge p(u).
\]
The intervals \(J_u\) and \(J_v\), when both are defined, are therefore disjoint. In particular, no arc has both endpoints in \(F_t\).

Now let \(P=v_1\cdots v_k\) have weight \(L\), and put
\[
W_i=\sum_{j=1}^{i}w(v_j),\qquad W_0=0.
\]
The prefix and suffix of \(P\) at \(v_i\) give
\[
p(v_i)\ge W_i,\qquad
q(v_i)\ge L-W_{i-1}.
\]
Together with (1), these inequalities force equality in both. Thus every \(v_i\) is critical and
\[
J_{v_i}=(W_{i-1},W_i].
\]
These intervals partition \((0,L]\). Therefore \(P\) contains exactly one vertex of \(F_t\). ∎

For unit weights, these are ordinary critical rank layers:
\[
F_i=\{v:p(v)=i,\ p(v)+q(v)-1=L\}.
\]

## 3. Adding the feedback vertex

We now prove the theorem.

Set \(H=D-x\). If \(H\) is empty, take \(S=\{x\}\). Otherwise construct \(L,\mathcal C,J_v,F_t\) as above.

Let
\[
A=\{u\in\mathcal C:u\to x\},\qquad
B=\{v\in\mathcal C:x\to v\}.
\]

We will find either:

1. a directed path in \(D\) of weight greater than \(L\); or
2. a value \(t\in(0,L]\) such that \(F_t\) is entirely nonadjacent to \(x\).

### Case 1: \(B=\varnothing\)

Consider \(t=L\).

If some \(u\in A\) satisfies \(L\in J_u\), then \(p(u)=L\), since \(p(u)\le L\). Appending \(x\) to a maximum-weight path ending at \(u\) gives a path of weight
\[
L+w(x)>L.
\]

Otherwise, no vertex of \(F_L\) sends an arc to \(x\). Since \(B=\varnothing\), no vertex of \(F_L\) receives an arc from \(x\) either. Thus \(F_L\) is entirely nonadjacent to \(x\).

### Case 2: \(B\ne\varnothing\)

Choose \(v\in B\) minimizing
\[
s=p(v)-w(v).
\]
Because \(v\) is critical,
\[
q(v)=L-s. \tag{2}
\]

If \(s=0\), prepend \(x\) to a maximum-weight path starting at \(v\). By (2), the resulting path has weight \(w(x)+L>L\).

Suppose now that \(s>0\). Then \(0<s<L\). By the minimal choice of \(s\), no interval \(J_z\) with \(z\in B\) contains \(s\): its left endpoint is at least \(s\), and the intervals are open on the left.

If no \(u\in A\) has \(s\in J_u\), it follows that \(F_s\) is entirely nonadjacent to \(x\), as required.

It remains to handle a vertex \(u\in A\) with
\[
p(u)-w(u)<s\le p(u). \tag{3}
\]
Notice that \(u\ne v\), because \(s\notin J_v\).

Take a maximum-weight path \(P\) ending at \(u\), and a maximum-weight path \(Q\) starting at \(v\). These paths are vertex-disjoint. Indeed, an intersection would give a directed path from \(v\) to \(u\) in \(H\). Along such a path, the rank inequality used in the lemma gives
\[
p(u)-w(u)\ge p(v)=s+w(v)>s,
\]
contrary to (3).

Consequently,
\[
P\,x\,Q
\]
is a simple directed path: the joining arcs are \(u\to x\) and \(x\to v\). Using (2) and (3), its weight is
\[
p(u)+w(x)+q(v)
\ge s+w(x)+(L-s)
=L+w(x)>L.
\]

This completes the dichotomy.

### Concluding the proof

If the first outcome occurs, every maximum-weight path of \(D\) contains \(x\), since every path avoiding \(x\) lies in \(H\) and has weight at most \(L\). Take
\[
S=\{x\}.
\]

In the second outcome, take
\[
S=\{x\}\cup F_t.
\]
This is stable by the lemma and the nonadjacency condition.

A maximum-weight path containing \(x\) meets \(S\). A maximum-weight path avoiding \(x\) must have weight exactly \(L\): it lies in \(H\), while \(H\) itself supplies a path of weight \(L\) in \(D\). It therefore meets \(F_t\), again by the lemma. Thus \(S\) meets every maximum-weight path. ∎

## 4. Algorithmic content

The proof does not require solving the longest-path problem in the cyclic digraph \(D\).

Given \(x\):

1. Topologically order \(H=D-x\).
2. Compute \(p\), \(q\), and \(L\) by forward and backward dynamic programming.
3. Identify the critical vertices and the sets \(A,B\).
4. Follow the two cases above.
   - In a “longer path” case, output \(\{x\}\).
   - Otherwise, output \(\{x\}\cup F_t\).

With unit weights, all these operations take \(O(n+m)\) time. Predecessor and successor pointers in the dynamic programs also recover the longer path whenever that outcome is used.

For positive rational weights, the construction uses \(O(n+m)\) exact additions and comparisons, and hence has polynomial bit complexity.

## 5. A broader stable-set version

The same argument permits an extension beyond feedback vertex number one.

### Corollary
Suppose \(X\) is a nonempty stable set, \(D-X\) is acyclic, and all vertices of \(X\) have the same out-neighbourhood in \(D-X\). Then, for every positive vertex weighting, \(D\) has a stable set containing \(X\) that meets every maximum-weight path.

The same conclusion holds if the in-neighbourhoods, rather than the out-neighbourhoods, are identical.

#### Proof
Use the critical layers of \(H=D-X\), and replace \(A,B\) by
\[
A=\{u\in\mathcal C:u\to a\text{ for some }a\in X\},
\]
\[
B=\{v\in\mathcal C:b\to v\text{ for some }b\in X\}.
\]

The only additional point is the joining step. If \(u\in A\) and \(v\in B\), choose \(a\in X\) with \(u\to a\). Since some vertex of \(X\) sends an arc to \(v\), the common-out-neighbourhood hypothesis gives \(a\to v\). Thus the same disjoint prefix and suffix can be joined through \(a\), producing a path of weight greater than \(L\).

All other steps are unchanged. The output is either \(X\), when a path heavier than \(L\) is obtained, or \(X\cup F_t\), where \(F_t\) is nonadjacent to all of \(X\). If \(H\) is empty, simply use \(X\).

The in-neighbourhood version follows by reversing every arc. ∎

## 6. What remains unresolved

The central use of acyclicity is not cosmetic. It provides:

- stable critical layers;
- consistent prefix ranks on maximum paths;
- disjointness of the prefix and suffix joined through \(x\).

For a general cyclic \(D-x\), the proposed prefix and suffix can overlap. Their concatenation would then be a walk, not necessarily a path, so the argument does not establish the required contradiction.

Also, one cannot simply require an arbitrary stable feedback set to be contained in the desired transversal. For example, take vertices
\[
a,b,c,x,y
\]
and arcs
\[
a\to b,\quad b\to c,\quad a\to x,\quad b\to x,\quad y\to c.
\]
This digraph is acyclic. The stable set \(X=\{x,y\}\) is maximal, but it misses the longest path \(abc\). Hence no stable superset of \(X\) is a longest-path transversal. This is not a counterexample to the original conjecture—\(\{b\}\) works—but it obstructs that stronger extension strategy.

Thus the result above supplies a constructive cyclic special case, including a weighted strengthening, but does not settle the general Laborde–Payan–Xuong conjecture.
