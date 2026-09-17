```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the supplied rotation definition, I characterize all paths with at most two chords, prove that every noncrossing path is active, and obtain a linear kernel in the number of chords.",
  "would_publish": false,
  "caveats": "The unrestricted characterization remains unresolved; the full-paper definition and literature novelty were not independently checked."
}
```

# 1. Formulation and results

The catalog excerpt omits the formal definition of activity. I use the explicit fixed-cycle rotation formulation in the supplied attempt, restated below. I verify the rotation facts used; I do not rely on that attempt’s computational assertions.

Fix
\[
C=1\,2\,\cdots\,n\,1,\qquad n\ge 3,
\]
and root every Hamilton path at \(1\). For
\[
P=p_1p_2\cdots p_n,\qquad p_1=1,
\]
write
\[
F(P)=E(P)\setminus E(C),\qquad d(P)=|F(P)|.
\]
The edges in \(F(P)\) are its **chords**.

For \(1\le i\le n-2\), put
\[
\rho_i(P)=p_1\cdots p_i\,p_n p_{n-1}\cdots p_{i+1}.
\]
A forward flip is admissible when the broken edge \(p_ip_{i+1}\) lies in \(C\). A path is **active** if it can be obtained from \(12\cdots n\) by admissible forward flips.

I prove three partial results:

1. Every path whose chords are noncrossing in the cyclic order of \(C\) is active. It can be reduced to a cycle traversal using exactly \(d(P)\) reverse flips.
2. For \(d(P)=2\), an explicit table depending only on three cycle-strip lengths characterizes activity. In particular, for \(n\ge6\), the number of non-active rooted paths with exactly two chords is
   \[
   \boxed{3n^2-25n+48}.
   \]
3. A path with \(d\) chords can be reduced, preserving activity, to an instance on at most \(4d+2\) vertices. Consequently, recognition takes
   \[
   O\!\left(n+(d+1)^2 2^d\right)
   \]
   time.

The unrestricted “simple criterion” remains open in this answer.

# 2. Reverse flips

The elementary edge identity is
\[
E(\rho_i(P))
=
E(P)-\{p_ip_{i+1}\}+\{p_ip_n\}.
\tag{1}
\]
Thus forward flips never delete a chord.

Since \(\rho_i\) is an involution, a flip from
\[
Q=q_1\cdots q_n
\]
is a valid **reverse flip** precisely when
\[
q_iq_n\in E(C).
\tag{2}
\]
In words: choose a \(C\)-neighbor of the current endpoint, other than its predecessor, and reverse the suffix after that vertex.

A reverse flip either deletes one chord or preserves the chord set. Call the latter kind **neutral**. Neutral flips are reversible: they exchange two cycle edges.

There are exactly two chordless rooted Hamilton paths,
\[
12\cdots n,\qquad 1n(n-1)\cdots2,
\]
and the second is obtained from the first by one admissible flip at the root. Therefore
\[
P\text{ is active}
\quad\Longleftrightarrow\quad
P\text{ can reach a chordless path by reverse flips}.
\tag{3}
\]

In particular, changing the orientation used to label \(C\) does not change activity.

# 3. Noncrossing paths are active

Draw the vertices in the order of \(C\) on a circle and draw path edges as straight segments. “Noncrossing” means that no two edges with disjoint endpoints cross in their interiors.

## Theorem 3.1

If the chords of \(P\) are noncrossing, then \(P\) is active. Moreover, \(P\) has a reverse sequence consisting of exactly \(d(P)\) chord-deleting flips and no neutral flips.

### Proof

First recall a simple property of noncrossing Hamilton paths on vertices in convex position.

> Starting at an endpoint, the next vertex must be a cyclic neighbor of that endpoint among the vertices still present.

Indeed, if the first edge were a diagonal with unvisited vertices on both sides, the remaining path would have to pass between those two sides. Neither endpoint of the diagonal would be available for such a passage, so a later edge would cross the diagonal.

Delete the first vertex and apply the same argument repeatedly. Since the root is \(1\), the vertices remaining after deleting it form the interval
\[
2,3,\ldots,n.
\]
The path successively removes either the smallest or the largest vertex of the remaining interval.

Let the final vertex be \(j\). If \(j=2\), all earlier choices are forced to be
\[
n,n-1,\ldots,3,
\]
so \(P=1n(n-1)\cdots2\). Likewise, if \(j=n\), then \(P=12\cdots n\). These are chordless.

Suppose now that \(P\) has a chord. Then
\[
3\le j\le n-1.
\]
The penultimate vertex is either \(j-1\) or \(j+1\). By symmetry, suppose it is \(j+1\).

Consider the earlier occurrence of \(j-1\). At the time it was visited, it was the smaller endpoint of the remaining interval. Consequently, \(j-2\) had already been visited. Its successor in \(P\) is not \(j\), because \(j\) is the final vertex and its predecessor is \(j+1\). Thus neither \(C\)-neighbor of \(j-1\) is its successor in \(P\). Its outgoing path edge is therefore a chord.

Since \(j-1\) is a \(C\)-neighbor of the current endpoint \(j\), the reverse flip at \(j-1\) deletes that chord and adds the cycle edge \((j-1)j\).

The resulting path is still noncrossing: its edge set is obtained by deleting a chord and adding a boundary edge. Induction on \(d(P)\) completes the proof. ∎

### Consequence

Every rooted Hamilton path with at most one chord is active.

This also gives a sufficient condition allowing arbitrarily many chords—for example, the familiar alternating-end paths
\[
1,2,n,3,n-1,4,n-2,\ldots
\]
are noncrossing and hence active.

# 4. An explicit characterization for two chords

For a word \(W\), write \(\overline W\) for its reversal.

If \(P\) has exactly two chords, deleting those chords leaves three cycle-edge paths. After choosing the appropriate orientation of \(C\), the component containing the root can be written as
\[
A=1\,2\,\cdots\,a.
\]
The other two cycle intervals, in cyclic order, are
\[
B=(a+1)(a+2)\cdots b,\qquad
Z=(b+1)(b+2)\cdots n.
\]
Put
\[
\alpha=a,\qquad \beta=b-a,\qquad \gamma=n-b.
\]
All three lengths are positive.

The path begins with \(A\), and then traverses \(B,Z\) in some order and orientations.

## Theorem 4.1 — Two-chord criterion

The following table contains every possible two-chord path. The conditions in the middle column are exactly those making both displayed joins chords.

| Form of \(P\) | Conditions for exactly two chords | Active precisely when |
|---|---|---|
| \(A\overline B Z\) | \(\beta\ge2\) | \(\alpha=1\), or \(\beta=2\) and \((\alpha=2\text{ or }\gamma=1)\) |
| \(A\overline B\overline Z\) | \(\beta\ge2\) | \(\beta=2\), or \(\alpha=\gamma=1\) |
| \(AZB\) | \(\gamma\ge2\), or \(\gamma=1,\ \alpha,\beta\ge2\) | \(\beta=1\), or \(\gamma=1\), or \(\alpha=1,\gamma=2\) |
| \(AZ\overline B\) | \(\gamma\ge2\) | Always |
| \(A\overline ZB\) | \(\alpha,\beta\ge2\) | Always |

When a block is a singleton, two displayed forms can coincide; their classifications agree.

### Why these forms are exhaustive

There are eight choices of the order and orientations of \(B,Z\). In
\[
ABZ,\qquad AB\overline Z,
\]
the first join is a cycle edge. In
\[
A\overline Z\overline B,
\]
the second join is a cycle edge. These cannot be the three maximal cycle strips of a two-chord path.

The other five choices give the table. Checking whether their joins are cycle edges gives its middle column.

### Principle used in the proof

A two-chord path is active if and only if some sequence of neutral reverse flips exposes a chord that can be deleted.

Indeed, a deletion leaves a one-chord path, which is active by Theorem 3.1. Conversely, a successful reverse sequence must eventually make its first chord deletion.

Thus it suffices to determine the neutral component and whether it has an exit deleting a chord.

## Proof of the table

### Case I: \(P=A\overline B Z\), with \(\beta\ge2\)

The endpoint is \(n\).

If \(\alpha=1\), the reverse flip at the root immediately deletes the first chord.

Suppose \(\alpha\ge2\). A neutral flip at the root gives
\[
R=1\,\overline Z\,B\,a(a-1)\cdots2,
\]
whose endpoint is \(2\).

There are just two possible further branches to consider:

- If \(\gamma=1\), the original endpoint \(n=b+1\) also permits a neutral flip at \(b\), giving
  \[
  U=A\,b\,n\,(a+1)(a+2)\cdots(b-1).
  \]
  Its endpoint is \(b-1\).

- If \(\alpha=2\), the endpoint \(2\) of \(R\) permits a neutral flip at \(3\), giving
  \[
  T=1\,\overline Z\,3\,2\,b(b-1)\cdots4.
  \]
  Its endpoint is \(4\).

The active cases are:

- \(\beta=2,\gamma=1\): in \(U\), the endpoint is \(a+1\), and the flip at \(a\) deletes the chord \(ab\).
- \(\beta=2,\alpha=2\): after the neutral flips at \(1\) and \(3\), the endpoint is \(4\), and the flip at \(5\) deletes a chord.

It remains to verify that all other cases are blocked.

If \(\beta\ge3\), then \(U\), when present, ends in the cycle edge
\[
(b-2)(b-1),
\]
and \(T\), when present, ends in the cycle edge \(54\). Their only nontrivial reverse moves go back along the listed neutral transitions. Likewise, \(R\) either ends in \(32\), or has exactly the listed transition to \(T\). The original path either ends in \((n-1)n\), or has exactly the listed transition to \(U\).

Thus these listed paths form a closed neutral component.

The remaining inactive case is
\[
\beta=2,\qquad \alpha\ge3,\qquad \gamma\ge2.
\]
Here only \(P,R\) occur, and their endpoints have predecessors \(n-1,3\), respectively. They form a closed two-state neutral component.

This proves the first row.

### Case II: \(P=A\overline B\overline Z\), with \(\beta\ge2\)

If \(\gamma=1\), this is Case I.

Suppose \(\gamma\ge2\). The endpoint is \(b+1\), its predecessor is \(b+2\), and its only nontrivial reverse move is the neutral flip at \(b\). This produces
\[
R=A\,b\,Z\,(a+1)(a+2)\cdots(b-1).
\]

If \(\beta=2\), its endpoint is \(a+1\), and the flip at \(a\) deletes a chord.

If \(\beta\ge3\), its endpoint \(b-1\) has predecessor \(b-2\), and its only reverse move returns to \(P\). Hence \(P,R\) form a closed neutral component.

This proves the second row.

### Case III: \(P=AZB\)

If \(\beta=1\), the endpoint is \(a+1\), and the flip at \(a\) deletes the first chord.

If \(\gamma=1\), the flip at \(n=b+1\) deletes the second chord.

It remains to consider \(\beta,\gamma\ge2\). The endpoint is \(b\), with predecessor \(b-1\), so its only nontrivial reverse move is the neutral flip at \(b+1\). The result is
\[
R=A\,(b+1)\,\overline B\,n(n-1)\cdots(b+2).
\]

If \(\gamma\ge3\), the endpoint \(b+2\) has predecessor \(b+3\), and its only reverse move returns to \(P\). This is a closed two-state component.

Suppose \(\gamma=2\). Then \(R\) ends at \(n=b+2\).

- If \(\alpha=1\), the reverse flip at the root deletes a chord.
- If \(\alpha\ge2\), the flip at the root is neutral and produces
  \[
  S=1\,n\,B\,(b+1)\,a(a-1)\cdots2.
  \]

For \(\alpha\ge3\), the endpoint \(2\) of \(S\) has predecessor \(3\), so its only reverse move goes back.

For \(\alpha=2\), there is one more neutral move, at \(3\), producing
\[
T=1\,n\,3\,2\,(b+1)\,b(b-1)\cdots4.
\]
For every \(\beta\ge2\), the predecessor of its endpoint \(4\) is \(5\). Its only nontrivial reverse move returns to \(S\).

These checks give a closed neutral component in every remaining case, proving the third row.

### Cases IV and V

For
\[
P=AZ\overline B,
\]
the endpoint is \(a+1\). The reverse flip at \(a\) immediately deletes the first chord.

For
\[
P=A\overline ZB,
\]
the endpoint is \(b\). The reverse flip at \(b+1\) immediately deletes the second chord.

Both resulting paths have one chord, so both are active. This completes the proof. ∎

## Corollary 4.2 — Exact count of two-chord obstructions

For \(n\le5\), every rooted path with exactly two chords is active. For \(n\ge6\), the number of non-active rooted paths with exactly two chords is
\[
3n^2-25n+48.
\]

### Proof

First consider paths whose root strip has \(\alpha\ge2\), and fix its orientation. The inactive contributions are:

- Case I with \(\beta\ge3\):
  \[
  \binom{n-4}{2}.
  \]
- Case I with \(\beta=2,\alpha\ge3,\gamma\ge2\):
  \[
  n-6.
  \]
- Case II with \(\beta\ge3,\gamma\ge2\):
  \[
  \binom{n-5}{2}.
  \]
  Here \(\gamma=1\) was already counted in Case I.
- Case III with \(\beta,\gamma\ge2\):
  \[
  \binom{n-4}{2}.
  \]

There are two possible orientations of the root strip.

For \(\alpha=1\), keep the original orientation of \(C\) fixed. Cases II and III contribute \(n-5\) paths each. Hence the total is
\[
2\left[
2\binom{n-4}{2}+\binom{n-5}{2}+n-6
\right]+2(n-5)
=
3n^2-25n+48.
\]
The table shows directly that no inactive case occurs before \(n=6\). ∎

At \(n=6\), the six two-chord obstructions are
\[
125436,\quad125634,\quad143265,\quad145623,\quad163254,\quad163452.
\]
Thus these six obstructions, including the paper’s displayed example, follow analytically from the table rather than from exhaustive search.

# 5. A linear kernel

The previous attempt’s dependence on \(n\) can be substantially reduced.

## Theorem 5.1

Given \(P\) with \(d=d(P)>0\), one can construct in \(O(n)\) time a rooted Hamilton path \(P^\ast\), relative to a cycle \(C^\ast\), such that:

1. \(P^\ast\) has exactly \(d\) chords;
2. \(P^\ast\) has at most \(4d+2\) vertices;
3. \(P\) is active if and only if \(P^\ast\) is active.

### Proof

Mark the vertices
\[
T=\{1\}\cup V(F(P)).
\]
Thus
\[
|T|\le2d+1.
\]

In the cyclic order of \(C\), replace each nonempty maximal run of unmarked vertices by a single unmarked vertex. Keep every marked vertex. This produces \(C^\ast\).

There are at most \(|T|\) nonempty unmarked runs, so
\[
|V(C^\ast)|\le2|T|\le4d+2.
\tag{4}
\]

The key observation is the following.

> Every cycle edge with both endpoints outside \(T\) belongs to every rooted Hamilton path \(Q\) satisfying \(F(Q)\subseteq F(P)\).

To see this, let \(uv\) be such an edge. At most one of \(u,v\) is the free endpoint of \(Q\), and neither is the root. The other vertex has degree two in \(Q\) and is incident with no chord. Hence both of its cycle edges, including \(uv\), belong to \(Q\).

Consequently, every unmarked run is traversed as an indivisible chain in every such \(Q\). Contracting these chains gives a rooted Hamilton path \(Q^\ast\). Conversely, a path in the reduced instance using only the allowed chords has a unique expansion: the orientation of each chain is determined by its incident path edge or edges.

No original chord becomes a cycle edge. If two marked vertices had a nonempty gap between them, the reduced cycle still retains one vertex in that gap. Thus the chord set is preserved.

It remains to check flips. A nontrivial reverse pivot must be marked. Indeed, if an unmarked vertex \(y\) were a pivot, then the inserted cycle edge from the free endpoint to \(y\) would be absent from \(Q\). But \(y\), being neither endpoint, has both cycle edges in \(Q\), a contradiction.

Thus reverse flips never cut the interior of an unmarked chain. They commute with the contraction and expansion above. A cycle neighbor created at the other end of a contracted endpoint-chain is its predecessor in the reduced path and therefore does not create an additional nontrivial flip.

We obtain an isomorphism between the reverse transition systems restricted to chord subsets of \(F(P)\). By chord monotonicity, these systems contain all reverse sequences relevant to activity. Chordless paths correspond under expansion, proving the equivalence. ∎

Informally, the general problem only needs to retain:

- the root;
- the chord endpoints;
- one representative from each nonempty gap between consecutive marked vertices.

Long chord-free gaps carry no additional information about activity.

# 6. Recognition and certificates after kernelization

For completeness, the fixed-chord-set bound from the supplied attempt is valid.

Let \(C^\ast\) have \(m\) vertices, and fix a chord subset \(S\). For a rooted Hamilton path \(Q\) with chord set \(S\) and free endpoint \(x\), put
\[
D=E(C^\ast)\setminus E(Q).
\]
Then, at every vertex,
\[
\deg_D(v)=\deg_S(v)+\mathbf1_{v=1}+\mathbf1_{v=x}.
\tag{5}
\]

Writing the cycle edges in order and their membership indicators in \(D\) as \(\delta_1,\ldots,\delta_m\), these equations have the form
\[
\delta_{j-1}+\delta_j
=
\deg_S(c_j)+\mathbf1_{c_j=1}+\mathbf1_{c_j=x}.
\tag{6}
\]
Once one bit \(\delta_1\) is chosen, all other bits are forced. Thus, for each endpoint \(x\), there are at most two possible omitted-edge sets. Each connected resulting edge set determines a unique rooted Hamilton path. Therefore
\[
|\{Q:F(Q)=S\}|\le2(m-1).
\tag{7}
\]

A reverse search has at most two outgoing transitions per state, and only visits chord subsets of the queried path. It consequently visits at most
\[
2(m-1)2^d
\]
states. Constructing a flipped path takes \(O(m)\) time.

Combining this with Theorem 5.1 yields
\[
\boxed{O\!\left(n+(d+1)^2 2^d\right)}
\]
recognition time. States may be indexed by \((S,x,\delta_1)\), so the bound does not require identifying paths by a factorial-size permutation index.

There is also a certificate bound independent of the original gap lengths. In a successful reverse sequence, each chord deletion starts a new fixed-chord-set phase. Removing repeated states within each phase bounds the total number of flips by
\[
(d+1)(2m-3)+d
=
2(m-1)(d+1)-1
=
O(d^2).
\]
These flips lift one-for-one to the original instance.

# 7. The remaining gap: deletion choices matter

The preceding results do not justify greedily deleting an arbitrary exposed chord.

For example,
\[
Q=125463
\]
is active, as witnessed by the reverse sequence
\[
125463
\longrightarrow123645
\longrightarrow123654
\longrightarrow123456.
\]
Each displayed step deletes one chord.

However, another legal reverse flip from the same \(Q\), at vertex \(4\), gives
\[
125463\longrightarrow125436,
\]
and the latter is non-active by the first row of Theorem 4.1.

Thus even an active path can have a chord-deleting move into a closed obstruction. The noncrossing theorem avoids this problem because every resulting path remains noncrossing; unrestricted paths do not have that protection.

What remains unproved is a polynomial-time or comparably simple structural criterion for arbitrary chord sets. The two-chord table, the noncrossing theorem, and the linear kernel are complete results within their stated scopes, but they do not settle Question 4.1.