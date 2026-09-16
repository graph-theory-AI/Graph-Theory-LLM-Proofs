```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The directed grid theorem resolves the conjecture, via a packing–transversal lemma for digraphs of bounded directed treewidth.",
  "would_publish": false,
  "caveats": "Uses the established directed grid theorem as a black box; no new or optimal quantitative bound is claimed."
}
```

# Statement and status

The updated catalog status is correct: this conjecture is a consequence of Kawarabayashi and Kreutzer’s **Directed Grid Theorem** (*The Directed Grid Theorem*, STOC 2015; arXiv:1411.5681).

Below is a complete deduction from that theorem. In particular, the conclusion does not depend merely on interpreting the paper’s abstract.

All digraphs are finite, “disjoint” means vertex-disjoint, and directed cycles are simple. Write
\[
\nu_\ell(D)=\max\{\text{number of vertex-disjoint directed cycles of length at least }\ell\}
\]
and
\[
\tau_\ell(D)=\min\{|T|:D-T\text{ has no directed cycle of length at least }\ell\}.
\]

Let \(g(r)\) be a directed-grid threshold, in the precise sense stated below. One valid bound is
\[
\boxed{
t_n(\ell)=(n-1)\left(g\!\left(\max\{n,\lceil\ell/2\rceil\}\right)+1\right)
\quad(n\ge2),
}
\]
with \(t_0(\ell)=t_1(\ell)=0\).

The two ingredients are:

1. a sufficiently large cylindrical directed grid forces many disjoint long directed cycles, even when present only as a butterfly minor;
2. bounded directed treewidth gives a bounded transversal whenever the cycle-packing number is bounded.

# 1. The directed grid theorem and long cycles

We use the following standard form of the established theorem.

**Directed Grid Theorem — Kawarabayashi–Kreutzer.**  
There is a function \(g:\mathbb N\to\mathbb N\) such that, for every positive integer \(r\), every digraph \(D\) with
\[
\operatorname{dtw}(D)>g(r)
\]
contains the cylindrical directed grid \(\Gamma_r\) of order \(r\) as a butterfly minor.

The grid \(\Gamma_r\) has \(r\) vertex-disjoint directed “rim” cycles, each of length \(2r\), joined by radial directed paths with alternating orientations.

We must check that these cycles lift to long, disjoint cycles in \(D\).

## Butterfly-minor lifting lemma

**Lemma 1.** Suppose \(H\) is a butterfly minor of \(D\). If \(H\) has vertex-disjoint directed cycles \(C_1,\ldots,C_k\), then \(D\) has vertex-disjoint directed cycles \(C'_1,\ldots,C'_k\) satisfying
\[
|C'_i|\ge |C_i| \qquad(1\le i\le k).
\]

**Proof.** A butterfly contraction contracts an arc \(uv\) for which either \(u\) has exactly one outgoing arc or \(v\) has exactly one incoming arc, with degrees taken at the time of contraction.

Reverse a sequence of deletions and butterfly contractions producing \(H\). Undoing a deletion is harmless. When undoing a contraction, at most one of the selected cycles contains the contracted vertex.

Suppose \(u\) has the unique outgoing arc \(uv\). The outgoing arc of a selected cycle at the contracted vertex must originally have left \(v\). Its incoming arc originally entered either \(u\) or \(v\). Accordingly, replace the contracted vertex by the directed path \(u v\), or just by \(v\). If instead \(v\) has the unique incoming arc \(uv\), the symmetric argument applies.

Thus the cycle remains simple and its length does not decrease. The newly restored vertices cannot lie on any of the other selected cycles, so disjointness is preserved. Repeating this proves the lemma. \(\square\)

Now set
\[
r=\max\{n,\lceil\ell/2\rceil\}.
\]
If \(D\) contains \(\Gamma_r\) as a butterfly minor, Lemma 1 gives \(r\) disjoint directed cycles, each of length at least \(2r\). Since \(r\ge n\) and \(2r\ge\ell\), this gives the required packing.

Consequently,
\[
\nu_\ell(D)<n
\quad\Longrightarrow\quad
\operatorname{dtw}(D)\le g(r).
\tag{1}
\]

# 2. A transversal lemma for bounded directed treewidth

The following lemma supplies the remaining step.

**Lemma 2.** Let \(D\) have directed treewidth at most \(w\), and let \(\mathcal C\) be any family of directed cycles in \(D\). If at most \(p\) members of \(\mathcal C\) can be pairwise vertex-disjoint, then some set of at most
\[
p(w+1)
\]
vertices meets every member of \(\mathcal C\).

## Directed-tree-decomposition conventions

We use the usual arboreal-decomposition definition of directed treewidth. A decomposition consists of:

- a rooted tree \(R\);
- bags \(W_t\), \(t\in V(R)\), partitioning \(V(D)\);
- a guard \(X_e\subseteq V(D)\) for every tree edge \(e\).

For an edge \(e\), let \(U_e\) be the union of the bags on the side of \(R-e\) not containing the root. The condition is that \(U_e\) is \(X_e\)-normal: it is disjoint from \(X_e\), and there is no directed walk in \(D-X_e\) whose endpoints lie in \(U_e\) but which visits a vertex outside \(U_e\).

Define the expanded bag
\[
B_t=W_t\cup\bigcup_{\substack{e\in E(R)\\ e\text{ incident with }t}}X_e.
\]
The width is
\[
\max_{t\in V(R)}|B_t|-1.
\]
Thus we may choose a decomposition with \(|B_t|\le w+1\) for every \(t\).

## Proof of Lemma 2

For each \(C\in\mathcal C\), let
\[
A_C=\{t\in V(R):W_t\cap V(C)\ne\varnothing\},
\]
and let \(R_C\) be the minimal subtree of \(R\) containing \(A_C\).

The important property is
\[
t\in V(R_C)\quad\Longrightarrow\quad B_t\cap V(C)\ne\varnothing.
\tag{2}
\]

To prove this, if \(t\in A_C\), the assertion follows from \(W_t\subseteq B_t\). Otherwise, choose an edge \(e\) of \(R_C\) incident with \(t\). By minimality of \(R_C\), both components of \(R-e\) contain a vertex of \(A_C\). Hence \(C\) meets both \(U_e\) and its complement.

If \(C\) avoided \(X_e\), following \(C\) from a vertex in \(U_e\) back to itself would give a directed walk in \(D-X_e\) that leaves and returns to \(U_e\), contradicting normality. Therefore
\[
V(C)\cap X_e\ne\varnothing.
\]
Since \(X_e\subseteq B_t\), this proves (2).

Next, vertex-disjoint subtrees
\[
R_{C_1},\ldots,R_{C_q}
\]
correspond to vertex-disjoint cycles \(C_1,\ldots,C_q\). Indeed, a common vertex of two cycles belongs to a unique bag \(W_t\), and that node \(t\) belongs to both corresponding subtrees. Thus the family
\[
\{R_C:C\in\mathcal C\}
\]
has no \(p+1\) pairwise vertex-disjoint members.

We use the elementary subtree packing–transversal fact:

> For a finite family of subtrees of a tree, the minimum number of tree vertices meeting every subtree equals the maximum number of pairwise vertex-disjoint subtrees.

For completeness, root the tree and call the vertex of a subtree nearest the root its top. Choose a subtree \(S\) whose top \(x\) has maximum depth. Every subtree intersecting \(S\) contains \(x\): if it intersects \(S\) at \(y\), its top and \(x\) are both ancestors of \(y\), and its top is no deeper than \(x\), so its path to \(y\) passes through \(x\). Select \(x\), discard all subtrees containing it, and repeat. The chosen witness subtrees are pairwise disjoint, and the selected vertices hit every subtree. This proves the fact.

It follows that there is a set \(Z\subseteq V(R)\), with \(|Z|\le p\), meeting every \(R_C\). Set
\[
T=\bigcup_{t\in Z}B_t.
\]
By (2), \(T\) meets every cycle in \(\mathcal C\), and
\[
|T|\le\sum_{t\in Z}|B_t|
\le p(w+1).
\]
This proves Lemma 2. \(\square\)

In particular,
\[
\tau_\ell(D)\le
\bigl(\operatorname{dtw}(D)+1\bigr)\nu_\ell(D)
\tag{3}
\]
for nonempty \(D\); the empty digraph is trivial.

# 3. Completion of the Erdős–Pósa argument

Fix \(\ell\ge2\) and \(n\ge2\), and put
\[
r=\max\{n,\lceil\ell/2\rceil\}.
\]

Let \(D\) be any digraph. If \(\nu_\ell(D)\ge n\), the packing alternative holds. Otherwise, (1) gives
\[
\operatorname{dtw}(D)\le g(r).
\]
Apply Lemma 2 to the family of all directed cycles of length at least \(\ell\). Its packing number is at most \(n-1\), so there is a set \(T\) meeting every such cycle with
\[
|T|\le(n-1)(g(r)+1).
\]
Equivalently, \(D-T\) has no directed cycle of length at least \(\ell\).

The boundary cases are immediate:

- For \(n=0\), the empty collection is a packing of zero cycles.
- For \(n=1\), either a qualifying cycle exists, or \(T=\varnothing\) works.

This establishes exactly the stated conjecture.

# Scope and gaps

The sole substantial imported result is the **proved directed grid theorem**; its proof is not reproduced here. The deduction above covers all parameters and finite digraphs, and explicitly checks the two potentially delicate points: preservation of cycle lengths under butterfly-minor lifting, and the transversal argument for directed—not undirected—treewidth.

This is an explanation of an already established consequence, not a new research result. The displayed bound is in terms of a directed-grid threshold; no claim is made about its optimality or the best currently available quantitative growth rate.