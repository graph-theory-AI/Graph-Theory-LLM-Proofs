Attack the following open graph-theory problem.

Catalog id: arc_disjoint_out_branching_and_in_branching
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/arc_disjoint_out_branching_and_in_branching/
Original entry: http://www.openproblemgarden.org/op/arc_disjoint_out_branching_and_in_branching
Problem attributed to: Thomassen, Carsten (posted 2013-03-02)

=== Problem statement (OpenProblemGarden) ===
Title: Arc-disjoint out-branching and in-branching
Conjecture There exists an integer $ k $ such that every $ k $ -arc-strong digraph $ D $ with specified vertices $ u $ and $ v $ contains an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint.

=== Discussion / context (OpenProblemGarden) ===
Thomassen [T] showed that, given a digraph $ D $ and two vertices $ u $ and $ v $ , deciding whether there are an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint is NP-complete. In contrast, one can decide in polynomial time whether there are $ k $ arc-disjoint out-branchings with specified roots $ s_1, \dots , s_k $ (some of which may be identical). This is a consequence of Edmonds’ well known branching theorem [E] states that a digraph $ D $ has $ k $ arc-disjoint out-branchings rooted at some fixed vertex $ s $ if and only if there are $ k $ arc-disjoint paths from $ s $ to every other vertex of $ D $ . Bang-Jensen [B] proved this conjecture for tournaments. A similar question can be asked about arc-disjoint strongly connected spanning subdigraphs . Several related problems are mentioned in the survey of Bang-Jensen and Kriesell [BK].

=== References listed by OpenProblemGarden ===
- [B] J. Bang-Jensen, Edge-disjoint in- and out-branching in tournaments and related path problems. J. Combin. Theory Ser. B 51 (1991), 1-23.
- [BK] J. Bang-Jensen, M. Kriesell, Disjoint sub(di)graphs in digraphs, Electronic Notes in Discrete Mathematics 34 (2009), 179-183.
- [E] J. Edmonds, Edge-disjoint branchings. In Combinatorial Algorithms, B. Rustin, ed., Acad. Press, New York (1973), 91-96.
- *[T] C. Thomassen, Configurations in Graphs, Annals of The New York Acad. Sci. 555 (1989), 402-412.

=== Catalog page (statement + literature review) ===
Arc-disjoint out-branching and in-branching — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The general Thomassen conjecture — that some universal $k$ suffices for all digraphs — remains open. Since 2013, the conjecture has been verified for digraphs of independence number at most 2 (where $k=2$ suffices), for semicomplete digraphs (complete classification of which pairs of roots admit a good pair), and for semicomplete compositions; separately, extremal work showed the smallest 2-arc-strong digraph without a good pair has at least 10 vertices.

 Cited literature (5)

 
 
 
partial Arc-disjoint in- and out-branchings in digraphs of independence number at most 2
 (2022)
 

 
 Joergen Bang-Jensen, Stephane Bessy, Frederic Havet, Anders Yeo · Journal of Graph Theory · arXiv:2003.02107 · doi:10.1002/jgt.22779

Every digraph with independence number at most 2 and arc-connectivity at least 2 has an arc-disjoint out-branching and in-branching (i.e., $k=2$ suffices for this class), settling Thomassen's conjecture for digraphs of independence number 2.
 

 
 
partial The smallest number of vertices in a 2-arc-strong digraph which has no good pair
 (2022)
 

 
 Ran Gu, Gregory Gutin, Shasha Li, Yongtang Shi, Zhenyu Taoqiu · Theoretical Computer Science · arXiv:2012.03742

Every 2-arc-strong digraph on at most 9 vertices has a good pair (arc-disjoint out- and in-branching), so any 2-arc-strong counterexample to the conjecture with $k=2$ requires at least 10 vertices.
 

 
 
partial Arc-disjoint out-branchings and in-branchings in semicomplete digraphs
 (2024)
 

 
 Joergen Bang-Jensen, Yun Wang · Journal of Graph Theory · arXiv:2302.06177 · doi:10.1002/jgt.23072

Provides a complete polynomial-time decidable characterisation of which semicomplete digraphs contain a good $(u,v)$-pair for prescribed roots, generalising the 1991 tournament result of Bang-Jensen and confirming a conjecture of Bang-Jensen for semicomplete digraphs.
 

 
 
partial Arc-disjoint out- and in-branchings in compositions of digraphs
 (2024)
 

 
 Joergen Bang-Jensen, Yun Wang · European Journal of Combinatorics · arXiv:2302.08283

Completely solves (in polynomial time) the good-pair problem for semicomplete compositions, extending the semicomplete-digraph classification to a broader class.
 

 
 
partial Strong arc decompositions of split digraphs
 (2025)
 

 
 Joergen Bang-Jensen, Yun Wang · Journal of Graph Theory · arXiv:2309.06904 · doi:10.1002/jgt.23157

Proves that every 3-arc-strong split digraph has a strong arc decomposition (partition of arcs into two strong spanning subdigraphs), which implies good pairs exist in this class; also shows 2-arc-strong is insufficient in general for split digraphs.
 

 

 Reviewer notes. The Wiley (JGT) and ScienceDirect pages returned HTTP 403 and could not be fetched directly; DOIs 10.1002/jgt.22779 and 10.1002/jgt.23072 are taken from Wiley URL patterns visible in search results and are reported with medium confidence. The DOI for arXiv:2302.08283 (European J. Combinatorics) and arXiv:2012.03742 (Theoretical Computer Science) could not be confirmed and are set to null. The conjecture for general digraphs remains open as of all verified sources. The 2019 paper arXiv:1906.08052 (Gutin, Sun) addresses the same-root variant (u=v) and was not included in since_posted as it is tangential to Thomassen's conjecture. No paper was found that resolves the general conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 183s.
 

Conjecture. There exists an integer $ k $ such that every $ k $ -arc-strong digraph $ D $ with specified vertices $ u $ and $ v $ contains an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint.

Discussion

Thomassen [T] showed that, given a digraph $ D $ and two vertices $ u $ and $ v $ , deciding whether there are an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint is NP-complete. In contrast, one can decide in polynomial time whether there are $ k $ arc-disjoint out-branchings with specified roots $ s_1, \dots , s_k $ (some of which may be identical). This is a consequence of Edmonds’ well known branching theorem [E] states that a digraph $ D $ has $ k $ arc-disjoint out-branchings rooted at some fixed vertex $ s $ if and only if there are $ k $ arc-disjoint paths from $ s $ to every other vertex of $ D $ . Bang-Jensen [B] proved this conjecture for tournaments. A similar question can be asked about arc-disjoint strongly connected spanning subdigraphs . Several related problems are mentioned in the survey of Bang-Jensen and Kriesell [BK].

Bibliography

 [B]
 J. Bang-Jensen, Edge-disjoint in- and out-branching in tournaments and related path problems. J. Combin. Theory Ser. B 51 (1991), 1-23.

 [BK]
 J. Bang-Jensen, M. Kriesell, Disjoint sub(di)graphs in digraphs, Electronic Notes in Discrete Mathematics 34 (2009), 179-183.

 [E]
 J. Edmonds, Edge-disjoint branchings. In Combinatorial Algorithms, B. Rustin, ed., Acad. Press, New York (1973), 91-96.

★ [T]
 C. Thomassen, Configurations in Graphs, Annals of The New York Acad. Sci. 555 (1989), 402-412.

Related conjectures

 
 implied by
 Arc-disjoint strongly connected spanning subdigraphs
 partial
 Suppose k witnesses the source conjecture, and let D be a k-arc-strong digraph with specified vertices u, v. Then D contains arc-disjoint strongly connected spanning subdigraphs D1 and D2. Any strong spanning subdigraph contains, for every choice of root, both an out-branching and an in-branching (take a BFS out-tree from the root, resp. an in-tree to the root, which exist by strong connectivity and spanning-ness). Take an out-branching rooted at u inside D1 and an in-branching rooted at v inside D2; they are arc-disjoint because D1 and D2 are. Hence the same k witnesses the target conjecture. Both OPG pages cross-reference each other as similar questions but the implication in this direction is rigorous and self-contained.
 

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
  "one_line": "For complete independent blow-ups with every part of size at least two, k=3 suffices and is sharp for prescribed roots.",
  "would_publish": false,
  "caveats": "This is a structural special case, not a resolution for arbitrary digraphs; novelty is not claimed."
}
```

# A sharp special case

I do not resolve the general conjecture. I prove a sufficient condition for a structured class, together with an explicit six-vertex obstruction to \(k=2\) when the roots are prescribed.

For a digraph \(D\), write
\[
\delta_D^+(X)=\{xy\in A(D):x\in X,\ y\notin X\}.
\]
Thus \(D\) is \(k\)-arc-strong if every nonempty proper \(X\subset V(D)\) satisfies \(|\delta_D^+(X)|\ge k\).

A **complete independent blow-up** of a loopless simple digraph \(H\) is obtained by replacing each vertex \(x\) by a nonempty independent set \(V_x\), and replacing every arc \(xy\) by all arcs from \(V_x\) to \(V_y\). There are no other arcs.

## Theorem

Let \(H\) be a strongly connected loopless simple digraph with at least two vertices. Let \(D\) be a complete independent blow-up of \(H\), with
\[
|V_x|\ge 2\qquad\text{for every }x\in V(H).
\]

If \(D\) is \(3\)-arc-strong, then \(D\) contains two arc-disjoint strongly connected spanning subdigraphs. Consequently, for every prescribed \(u,v\in V(D)\), it contains an out-branching rooted at \(u\) and an arc-disjoint in-branching rooted at \(v\).

The constant \(3\) is best possible for this class. The obstruction at \(2\) can be chosen to have six vertices, to be Eulerian and Hamiltonian, and to have independence number \(2\).

The proof is self-contained.

# 1. A construction using two or three copies of each vertex

## 1.1 A lifting lemma

Let \(q\in\{2,3\}\), and select \(q\) vertices
\[
x_0,\ldots,x_{q-1}
\]
from each part \(V_x\), with subscripts interpreted in \(\mathbb Z_q\).

For a function
\[
a:A(H)\longrightarrow \mathbb Z_q,
\]
define a spanning subdigraph \(L(a)\) on these selected vertices by including
\[
x_i y_{i+a(xy)}
\qquad
(xy\in A(H),\ i\in\mathbb Z_q).
\]

**Lemma.** If \(H\) has a directed cycle \(C\) such that
\[
\sum_{e\in A(C)}a(e)\ne 0\pmod q,
\]
then \(L(a)\) is strongly connected.

**Proof.** Fix \(c\in V(C)\). Traversing a lift of \(C\) changes the subscript at \(c\) by
\[
s=\sum_{e\in A(C)}a(e).
\]
Because \(q\) is prime and \(s\ne0\), repeated traversals reach all \(q\) copies of \(c\). Those copies therefore lie in one strong component.

For any \(x\in V(H)\), choose directed paths from \(c\) to \(x\) and from \(x\) to \(c\). Lifting the first path from the different copies of \(c\) reaches every copy of \(x\), while lifting the second takes every copy of \(x\) to a copy of \(c\). Hence all selected vertices lie in one strong component. \(\square\)

Also, if
\[
a(e)\ne b(e)\quad\text{for every }e\in A(H),
\]
then \(L(a)\) and \(L(b)\) are arc-disjoint.

## 1.2 Two copies suffice unless the base is an odd directed cycle

Suppose \(H\) is not itself a directed odd cycle. I construct two arc-disjoint strong spanning subdigraphs using two selected vertices per part.

All arithmetic here is in \(\mathbb Z_2\).

### Case A: \(H\) contains an even directed cycle

Choose such a cycle \(C\) and an arc \(e\in A(C)\). Set
\[
a(e)=1,\qquad a(f)=0\quad(f\ne e),
\]
and set \(b(f)=1-a(f)\) for every arc \(f\).

Then
\[
\sum_C a=1,\qquad
\sum_C b=|A(C)|-1=1\pmod2.
\]
The lifting lemma makes both \(L(a)\) and \(L(b)\) strong, and they are arc-disjoint.

### Case B: every directed cycle of \(H\) is odd

Since \(H\) is strong but is not itself a directed cycle, it has two distinct simple directed cycles \(C_1,C_2\). Indeed, every arc of a strong digraph belongs to a directed cycle, so a strong digraph with only one directed cycle is exactly that cycle.

Choose
\[
e\in A(C_1)\setminus A(C_2).
\]
Such an arc exists because distinct simple directed cycles cannot have one arc set properly contained in the other.

Again set \(a(e)=1\), set \(a=0\) elsewhere, and let \(b=1-a\). Then
\[
\sum_{C_1}a=1,\qquad
\sum_{C_2}b=|A(C_2)|=1\pmod2.
\]
Thus both lifts are strong and arc-disjoint.

This proves:

> If \(H\) is not a directed odd cycle, two selected vertices per part support two arc-disjoint strong spanning subdigraphs.

## 1.3 Three copies always suffice

Now use \(\mathbb Z_3\), and let \(H\) be any strongly connected base of order at least two.

Choose a simple directed cycle \(C\), of length \(\ell\), and an arc \(e\in A(C)\). Define
\[
a(e)=1,\qquad a(f)=0\quad(f\ne e).
\]
Initially define
\[
b(e)=0,\qquad b(f)=1\quad(f\ne e).
\]

We have
\[
\sum_C a=1,\qquad \sum_C b=\ell-1\pmod3.
\]
If the second sum is zero, choose another arc \(f\in A(C)\setminus\{e\}\) and change \(b(f)\) from \(1\) to \(2\). The sum on \(C\) then becomes \(1\).

In either case both cycle sums are nonzero, and
\[
a(g)\ne b(g)\qquad\text{for every }g\in A(H).
\]
The lifting lemma gives two arc-disjoint strong spanning subdigraphs on the three selected vertices per part.

# 2. Extending the construction to all vertices

Suppose two arc-disjoint strong spanning subdigraphs \(F_1,F_2\) have been constructed on two or three selected vertices per part.

For every base vertex \(x\), choose an in-neighbor \(p(x)\) and an out-neighbor \(t(x)\) in \(H\). These exist because \(H\) is strong and has at least two vertices.

For each unselected vertex \(z\in V_x\), add
\[
p(x)_0z,\quad zt(x)_0
\]
to \(F_1\), and add
\[
p(x)_1z,\quad zt(x)_1
\]
to \(F_2\).

All these arcs exist by the definition of the blow-up. They are arc-disjoint:

- the added arcs have an unselected endpoint, so are not core arcs;
- for a fixed \(z\), the two incoming arcs have different tails and the two outgoing arcs have different heads;
- arcs associated with different unselected vertices cannot coincide.

Each added vertex can be reached from, and can reach, the corresponding strong core. Both enlarged subdigraphs are therefore strongly connected and spanning.

We have proved the following sufficient conditions:
\[
\boxed{
\begin{aligned}
&H\text{ not a directed odd cycle},\quad \min_x|V_x|\ge2;\\
&\text{or simply}\quad \min_x|V_x|\ge3.
\end{aligned}}
\]
Either condition guarantees two arc-disjoint strong spanning subdigraphs.

# 3. Applying the construction under \(3\)-arc-connectivity

Let \(D\) satisfy the theorem’s hypotheses.

If \(H\) is not a directed odd cycle, the two-copy construction applies immediately.

Suppose instead that \(H\) is a directed odd cycle. For every part \(V_x\), each vertex in its predecessor part has out-degree exactly \(|V_x|\). Since \(D\) is \(3\)-arc-strong, every vertex has out-degree at least \(3\). Therefore
\[
|V_x|\ge3\qquad\text{for every }x,
\]
and the three-copy construction applies.

Thus \(D\) contains arc-disjoint strong spanning subdigraphs \(F_1,F_2\). Choose an out-branching rooted at the prescribed \(u\) inside \(F_1\), and an in-branching rooted at the prescribed \(v\) inside \(F_2\). Strong connectivity guarantees both exist, and their arc sets are disjoint.

This also covers \(u=v\). If a partition of all arcs into two strong spanning subdigraphs is desired, assign every unused arc to either part. \(\square\)

# 4. A six-vertex obstruction to \(k=2\)

Let \(D_0\) have independent parts
\[
A=\{u,v\},\qquad B=\{b_1,b_2\},\qquad C=\{c_1,c_2\},
\]
with all arcs
\[
A\longrightarrow B,\qquad B\longrightarrow C,\qquad C\longrightarrow A,
\]
and no others. Thus \(D_0\) is the complete independent blow-up of a directed triangle, with two vertices per part.

Every vertex has in-degree and out-degree \(2\).

## 4.1 Arc-connectivity

The arcs of \(D_0\) partition into the Hamilton cycle
\[
K=u\,b_1\,c_1\,v\,b_2\,c_2\,u
\]
and the two directed triangles
\[
Q_1=u\,b_2\,c_1\,u,\qquad
Q_2=v\,b_1\,c_2\,v.
\]

Let \(X\) be nonempty and proper. The Hamilton cycle contributes at least one arc to \(\delta^+(X)\).

If \(Q_1\cup Q_2\) contributes an outgoing arc, then \(|\delta^+(X)|\ge2\). Otherwise \(X\) must be exactly the vertex set of one of the two triangles. The Hamilton cycle alternates between those vertex sets, so it contributes three outgoing arcs.

Hence \(D_0\) is \(2\)-arc-strong. Its arc-connectivity is exactly \(2\), since every vertex has out-degree \(2\).

The graph is Eulerian and Hamiltonian. Its independence number is \(2\): vertices in different parts are adjacent in one direction, and each part has size two.

## 4.2 No good pair for the prescribed roots \(u,v\)

Suppose there were arc-disjoint branchings \(T,S\), where \(T\) is an out-branching rooted at \(u\), and \(S\) is an in-branching rooted at \(v\).

For every \(z\ne v\), the in-branching \(S\) uses one outgoing arc of \(z\). Since \(d_{D_0}^+(z)=2\),
\[
d_T^+(z)\le1\qquad(z\ne v).
\]

Moreover, \(d_T^+(v)\le1\). Otherwise \(T\) would contain both \(vb_1\) and \(vb_2\). But its root \(u\) must also have an outgoing arc, necessarily to one of \(b_1,b_2\). That vertex would then have in-degree at least two in \(T\), impossible.

Thus every vertex has out-degree at most one in \(T\). A spanning out-branching with this property is a Hamilton path starting at its root. The cyclic arrangement of the parts forces
\[
T=u\,b_i\,c_j\,v\,b_{3-i}\,c_{3-j}
\]
for some \(i,j\in\{1,2\}\).

In \(D_0-A(T)\), the vertices
\[
u,\quad b_{3-i},\quad c_j
\]
form the directed triangle
\[
u\longrightarrow b_{3-i}\longrightarrow c_j\longrightarrow u.
\]
Each has exactly one remaining outgoing arc, namely the displayed arc. Therefore this set has no outgoing arc in \(D_0-A(T)\).

It does not contain \(v\). Consequently \(D_0-A(T)\) has no directed path from \(u\) to \(v\), and cannot contain the alleged in-branching \(S\). This contradiction proves the obstruction.

Hence any universal constant in the original conjecture must satisfy
\[
k\ge3.
\]

## 4.3 Why prescribed roots matter

This six-vertex graph does have good pairs when the roots may be chosen. For example, both roots can be \(u\), using
\[
T_0=\{ub_1,ub_2,b_1c_1,b_2c_2,c_1v\}
\]
and
\[
S_0=\{vb_1,b_1c_2,c_2u,b_2c_1,c_1u\}.
\]
These are arc-disjoint out- and in-branchings rooted at \(u\).

Thus the example does not contradict statements guaranteeing an unspecified-root good pair on small digraphs or on digraphs of independence number at most two.

# 5. What remains unresolved

The theorem requires a substantial additional hypothesis: a partition into independent parts of size at least two, with complete adjacency between every ordered pair of adjacent parts.

Allowing singleton parts would remove that restriction, but the proof would no longer apply. Nor can one solve the general problem by first blowing up an arbitrary digraph and then contracting the parts: the two lifted subdigraphs use different copies of the same base arcs, so contraction destroys arc-disjointness.

Therefore the argument supplies:

- a sharp \(k=3\) result for the stated blow-up class;
- an explicit prescribed-root obstruction at \(k=2\);
- no universal upper bound for arbitrary digraphs.

No novelty claim is made for these special-case constructions.
