```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I bound two-block cyclic-shift distances in the generic rectangulation graph to within one flip and prove an exact common-block factorization, but do not resolve the unrestricted complexity question.",
  "would_publish": false,
  "caveats": "Uses the standard clumped-quotient flip conventions; no general polynomial-time algorithm or NP-hardness result is established, and novelty has not been checked."
}
```

# 1. Model and results

I use the finite combinatorial flip graphs, not geometric drawings with arbitrary real coordinates or independently assigned rectangle labels.

Here is the precise permutation-quotient convention used below. Suppose two permutations differ by swapping adjacent entries \(a<b\). For each intermediate value
\[
a+1,\ldots,b-1,
\]
record \(L\) or \(R\) according as it lies to the left or right of the adjacent pair. Read these letters in increasing **value** order. Call the resulting word \(W_{a,b}\), and call its maximal constant runs its *clumps*.

The two models considered are:

- **Diagonal rectangulations:** contract an adjacent-transposition edge when \(W_{a,b}\) contains both \(L\) and \(R\).
- **Generic rectangulations:** contract it when \(W_{a,b}\) has at least three clumps.

These are, respectively, the usual diagonal/twisted-Baxter and generic/2-clumped weak-order quotient models. Write their quotient maps as \(q_D,q_G\), and their graph distances as \(d_D,d_G\). A permutation representative is a finite encoding of a vertex.

The arguments below use these explicit local rules. They do not depend on the extremal-distance formulas or sorting-network assertions in the preceding attempt.

The main partial results are:

### Theorem 1: a nearly exact family of generic distances

Let \(a,b\geq 1\), \(n=a+b\), and set
\[
e=12\cdots n,\qquad
w_{a,b}=(a+1)(a+2)\cdots n\,12\cdots a.
\]
Then
\[
d_G(q_G(e),q_G(w_{a,b}))=
\begin{cases}
n-1,&\min(a,b)=1,\\[2mm]
2n-4,&\min(a,b)=2,
\end{cases}
\]
and, if \(a,b\geq3\),
\[
\boxed{\quad
2n-4\ \leq\ d_G(q_G(e),q_G(w_{a,b}))\ \leq\ 2n-3.
\quad}
\]

Thus the distance is determined to within one flip throughout this family.

Moreover, every increasing path in the quotient lattice between these endpoints has length \(ab\). For balanced blocks, therefore, every increasing path has quadratic length, while unrestricted shortest paths have linear length.

### Theorem 2: isometric common-block factorization

For either model, fix a partition of the values into consecutive intervals. The subgraph obtained by concatenating independently chosen quotient vertices on these intervals, in a fixed block order, is an isometric Cartesian product of the smaller quotient graphs.

Consequently, exact distance is fixed-parameter tractable in the largest block size of a displayed common consecutive-block decomposition. This computes the **ambient** flip distance, not merely distance restricted to the block-preserving subgraph.

Neither theorem decides the unrestricted P-versus-NP-hardness question.

# 2. A polynomial-time lower bound for generic rectangulations

The lower bound in Theorem 1 comes from a class invariant that is different from the short-pair signatures in the previous attempt.

Let
\[
\mathcal F_n=
\{I:\ I\text{ is a nonempty proper interval of consecutive values in }[n]\}
\;\cup\;
\{[n]\setminus I:\ I\text{ is such an interval}\}.
\]
Thus \(\mathcal F_n\) consists of intervals and complements of intervals.

For a permutation \(\pi\), let
\[
P_k(\pi)=\{\pi_1,\ldots,\pi_k\},\qquad 1\leq k<n.
\]
Define
\[
\lambda_k(\pi)=
\begin{cases}
P_k(\pi),&P_k(\pi)\in\mathcal F_n,\\
\bot,&P_k(\pi)\notin\mathcal F_n.
\end{cases}
\]

## Lemma 2.1

Each \(\lambda_k\) is constant on every generic rectangulation class.

### Proof

An adjacent swap at positions \(j,j+1\) changes only the prefix set \(P_j\). Suppose that, before the swap, this set is \(S\in\mathcal F_n\).

Write the swapped values as \(a<b\). Exactly one of \(a,b\) belongs to \(S\). For an intermediate value \(x\in(a,b)\), its side letter is \(L\) exactly when \(x\in S\).

Membership in an interval has the form
\[
R^*L^*R^*
\]
when read in value order; membership in the complement of an interval has the form
\[
L^*R^*L^*.
\]
Because \(a,b\) have opposite membership, the word strictly between them has at most two clumps. The swap therefore cannot be a generic zero move.

Applying the same argument in reverse shows that a generic zero move cannot create a prefix set in \(\mathcal F_n\), either. Hence it preserves every \(\lambda_k\). ∎

This invariant is specific to the generic rule. It need not be invariant under diagonal zero moves.

For each \(k\), introduce an auxiliary graph \(H_k\):

- its vertices are \(\bot\) and all \(k\)-element members of \(\mathcal F_n\);
- \(\bot\) is adjacent to every other vertex;
- two recognized sets \(S,T\) are adjacent when \(|S\setminus T|=1\).

Its distance between distinct recognized sets is
\[
\delta_k(S,T)=\min\{2,|S\setminus T|\}.
\]
Also \(\delta_k(S,\bot)=1\), and equal states have distance zero.

## Proposition 2.2

For generic rectangulations \(R,S\),
\[
\boxed{\qquad
d_G(R,S)\ \geq\
L(R,S):=\sum_{k=1}^{n-1}
\delta_k\bigl(\lambda_k(R),\lambda_k(S)\bigr).
\qquad}
\]

### Proof

A quotient edge has representatives differing by one adjacent swap, say at positions \(j,j+1\). All signature coordinates except \(j\) remain unchanged.

At coordinate \(j\), either one of the two states is \(\bot\), or the two recognized prefix sets differ by replacing one element. Thus this coordinate moves by distance at most one in \(H_j\).

The signature map is therefore 1-Lipschitz into the Cartesian product of the \(H_k\). The product distance is the displayed sum. ∎

Given permutation representatives, this lower bound can be evaluated in \(O(n^2)\) time by directly maintaining and comparing prefix sets. It requires no enumeration of rectangulations.

# 3. Lower bounds for two-block cyclic shifts

Consider \(e,w_{a,b}\) from Theorem 1.

For \(e\),
\[
P_k(e)=[1,k].
\]
For \(w_{a,b}\),
\[
P_k(w_{a,b})=
\begin{cases}
[a+1,a+k],&k\leq b,\\[1mm]
[a+1,n]\cup[1,k-b],&k>b.
\end{cases}
\]
Every one of these sets belongs to \(\mathcal F_n\): the first kind is an interval, and the second kind has interval complement.

A direct calculation gives
\[
\bigl|P_k(e)\setminus P_k(w_{a,b})\bigr|
   =\min\{k,n-k,a,b\}.
\]
Consequently,
\[
L(q_G(e),q_G(w_{a,b}))
=
\sum_{k=1}^{n-1}
\min\bigl\{2,k,n-k,a,b\bigr\}.
\]

If \(\min(a,b)=1\), every summand is one, giving \(n-1\).

If \(a,b\geq2\), the first and last summands are one, and each of the \(n-3\) intervening summands is two. Hence
\[
L(q_G(e),q_G(w_{a,b}))=2n-4.
\]

This proves all the lower bounds in Theorem 1.

# 4. A linear-length path

There is always the ordinary adjacent-transposition path which interchanges the two increasing blocks. It has length \(ab\), so
\[
d_G(q_G(e),q_G(w_{a,b}))\leq ab.
\]
Combined with the preceding lower bound, this already proves the exact formulas when \(\min(a,b)\) is one or two.

Assume now that \(a,b\geq3\). Put
\[
A'=(a-1),1,2,\ldots,a-2,a,
\qquad
B=(a+1),(a+2),\ldots,n.
\]

We construct a path in three stages.

## Stage 1: create one temporary internal inversion pattern

Starting from \(e\), move \(a-1\) to the beginning of the first block. This takes \(a-2\) adjacent swaps and produces
\[
A'B.
\]
Its projected cost is at most \(a-2\).

## Stage 2: interchange the blocks while preserving their internal orders

Interchange \(A'\) and \(B\) by adjacent swaps, preserving the internal order of each block. Every pair
\[
u\in[1,a],\qquad v\in[a+1,n]
\]
is swapped exactly once.

The side word of such a crossing depends only on these fixed internal orders.

If \(u\leq a-2\), it is
\[
W_{u,v}
=
R^{\,a-u-2}\,L\,R\,L^{\,v-a-1}.
\]
Indeed:

- values \(u+1,\ldots,a-2\) are after \(u\);
- \(a-1\) is before \(u\);
- \(a\) is after \(u\);
- values \(a+1,\ldots,v-1\) are before \(v\).

It follows that the crossing is a generic zero move whenever

- \(u\leq a-3\), for any \(v\); or
- \(u=a-2\) and \(v\geq a+2\).

The only crossings not covered by this zero-move argument are
\[
u\in\{a-1,a\},\quad v\in[a+1,n],
\]
and the one additional pair
\[
(u,v)=(a-2,a+1).
\]
There are \(2b+1\) such pairs. Thus Stage 2 projects to a walk of length at most \(2b+1\), ending at
\[
BA'.
\]

## Stage 3: restore the first block's internal order

Inside \(A'\), move \(a-1\) back to its increasing-order position. This costs at most \(a-2\) more flips and produces \(w_{a,b}\).

The total projected length is at most
\[
(a-2)+(2b+1)+(a-2)=2n-3.
\]
This proves Theorem 1. ∎

For example, with \(a=4,b=3\), the construction starts
\[
1234567\longrightarrow1324567\longrightarrow3124567.
\]
The middle stage interchanges \(3124\) and \(567\), with at most seven paid flips, reaching \(5673124\). Two further adjacent swaps give \(5671234\). Thus
\[
10\leq d_G(q_G(1234567),q_G(5671234))\leq11,
\]
whereas every increasing path has length \(12\).

No computational experiment is needed for this example: the middle-stage zero moves are certified by the displayed side-word calculation.

# 5. Why monotone paths can be far from optimal

Let \(T_{a,b}\) be the permutations whose restrictions to
\[
A=[1,a],\qquad B=[a+1,n]
\]
are both increasing. These are precisely the shuffles of two increasing chains.

## Lemma 5.1

Every permutation in \(T_{a,b}\) is a singleton generic congruence class.

### Proof

Consider any adjacent pair.

If its two values lie in the same block, they must be consecutive values: otherwise an intermediate value of that increasing chain would have to occur between them. The side word is empty.

For a cross-block pair \(u\in A,v\in B\), all intermediate values in \(A\) lie to the right of the pair, and all intermediate values in \(B\) lie to its left. Therefore
\[
W_{u,v}=R^{\,a-u}L^{\,v-a-1},
\]
which has at most two clumps.

Thus no incident adjacent-transposition edge is a generic zero edge. The zero-move component is a singleton. ∎

Any path that maintains the two within-block increasing orders therefore consists of ordinary adjacent transpositions between these singleton vertices. Between \(e\) and \(w_{a,b}\), the number of cross-block inversions changes from zero to \(ab\), and one step changes it by at most one. Such a path has length at least \(ab\).

This also describes all increasing quotient-lattice paths between these endpoints. In weak order,
\[
[e,w_{a,b}]=T_{a,b}.
\]
Moreover, if \(q_G(x)\leq q_G(w_{a,b})\), then
\[
q_G(x\vee w_{a,b})=q_G(w_{a,b}).
\]
The class of \(w_{a,b}\) is a singleton, so \(x\vee w_{a,b}=w_{a,b}\), and hence \(x\leq w_{a,b}\). Thus the quotient order interval contains exactly these singleton classes. Every increasing path has \(ab\) edges.

For \(a=b=m\geq4\), we have
\[
d_G(q_G(e),q_G(w_{m,m}))
\in\{4m-4,4m-3\},
\]
while every increasing path has length \(m^2\).

Therefore:

> Restricting to increasing paths, or requiring the path to preserve the two initially agreeing within-block orders, can lose a factor \(\Theta(n)\).

In particular, an unrestricted shortest path can be forced to reverse and later restore a relative order on which the two endpoints agree. This rules out a natural class of monotonicity-based algorithms.

# 6. Isometric common-block factorization

The next result applies to **both** diagonal and generic rectangulations.

Partition the value set into consecutive intervals
\[
I_1,\ldots,I_t,
\qquad |I_i|=m_i.
\]
Fix a block order, initially taken to be \(I_1,I_2,\ldots,I_t\). Concatenating permutation representatives on these blocks defines a map
\[
E:\prod_{i=1}^t\mathcal R_{m_i}\longrightarrow\mathcal R_n,
\]
where \(\mathcal R\) is either model. Labels in each factor are shifted to the corresponding interval.

## Lemma 6.1: restriction is well-defined and nonexpansive

For a quotient class \(C=q(\pi)\), define
\[
P_i(C)=q\bigl(\operatorname{std}(\pi|_{I_i})\bigr),
\]
where restriction deletes the other values and standardization relabels the interval increasingly.

Then \(P_i\) is well-defined. Moreover, a quotient edge changes at most one coordinate of
\[
P=(P_1,\ldots,P_t),
\]
and changes that coordinate by at most one graph edge.

### Proof

Consider a zero move swapping adjacent values \(a,b\).

If both values lie in \(I_i\), every value strictly between them also lies in \(I_i\). Restriction preserves adjacency of the pair and preserves its entire side word. The restricted swap is therefore a zero move in the same model.

If the two values do not both lie in \(I_i\), restriction leaves the relative order on \(I_i\) unchanged.

This proves independence of the representative.

The same argument for an arbitrary adjacent swap shows that at most one factor changes, and that its images are equal or adjacent. ∎

## Lemma 6.2: concatenation is well-defined

The map \(E\) is well-defined, and
\[
P\circ E=\mathrm{id}.
\]
Furthermore, an edge in one factor lifts to an edge in the full quotient graph.

### Proof

A zero move inside a block retains its side word after concatenation, because every intermediate value belongs to that same consecutive-value interval. Thus changing representatives in a factor does not change the concatenated quotient class.

Restriction clearly recovers each factor.

An edge in a factor has adjacent-transposition representatives. Concatenating them gives adjacent permutations in \(S_n\). Their full quotient images cannot coincide, since restriction recovers the distinct factor endpoints. Hence they define a quotient edge. ∎

## Proof of Theorem 2

For factor vertices \(C_i,D_i\), Lemma 6.1 gives
\[
d\bigl(E(C_1,\ldots,C_t),E(D_1,\ldots,D_t)\bigr)
\geq
\sum_{i=1}^t d(C_i,D_i).
\]
Conversely, perform a shortest path in each factor successively and lift it using Lemma 6.2. This gives the opposite inequality. Therefore
\[
\boxed{\quad
d\bigl(E(C_1,\ldots,C_t),E(D_1,\ldots,D_t)\bigr)
=
\sum_{i=1}^t d(C_i,D_i).
\quad}
\]

The same proof works for any other fixed order of the blocks. ∎

The lower-bound direction is essential: a path that mixes or interleaves blocks cannot beat the sum of the factor distances.

# 7. An exact algorithm for bounded common-block width

Suppose the input permutation representatives \(\pi,\tau\) display a common consecutive-block decomposition.

For the increasing block order, such a decomposition can be found by taking all common cuts \(j\) satisfying
\[
\{\pi_1,\ldots,\pi_j\}
=
\{\tau_1,\ldots,\tau_j\}
=[1,j].
\]
Together with \(0,n\), these cuts partition both words into the same consecutive-value blocks.

Let \(w\) be the largest resulting block size. For each block of size \(m\), construct its quotient graph as follows:

1. Enumerate the \(m!\) permutations.
2. Union the endpoints of every zero adjacent-transposition edge, using the appropriate clump test.
3. Add an edge between distinct components whenever an ordinary adjacent-transposition edge joins them.
4. Run breadth-first search between the two input components.

The clump test is polynomial-time, so a factor can be solved in
\[
m!\,m^{O(1)}
\]
time and space. Theorem 2 then gives the exact ambient distance by summing the answers.

The total running time is
\[
\operatorname{poly}(n)+
\sum_i m_i!\,m_i^{O(1)}
\leq
w!\,w^{O(1)}\operatorname{poly}(n).
\]

Thus the problem is FPT in this common-block-width parameter. Identical blocks can, of course, be skipped. In particular, the algorithm is polynomial-time when
\[
w=O\!\left(\frac{\log n}{\log\log n}\right).
\]

This parameter is structural and can equal \(n\). The result is **not** an FPT algorithm parameterized by the requested flip distance.

# 8. Remaining gaps

The unrestricted complexity question remains open in this attack.

The concrete contributions are:

- a polynomial-time computable prefix-signature lower bound for generic rectangulations;
- exact distances for two-block cyclic shifts when the smaller block has size at most two;
- a one-flip uncertainty bound for every larger two-block cyclic shift;
- a family showing a \(\Theta(n)\) gap between increasing-path length and unrestricted distance;
- an exact isometric block decomposition and its parameterized algorithm.

The prefix signature does not itself solve arbitrary instances. For example,
\[
152346,\qquad153246
\]
have identical signatures \((\lambda_k)\): their only different prefix sets are
\[
\{1,2,5\},\qquad\{1,3,5\},
\]
both unrecognized. Nevertheless, their generic quotient vertices have distance one. They differ by swapping \(2,3\), and the order of consecutive values is invariant under all zero moves.

Nor does the block algorithm handle arbitrary pairs efficiently when no useful common decomposition is present.

Accordingly, I have neither a polynomial-time algorithm nor an NP-hardness reduction for general rectangulation flip distance. The partial theorems above are proved in the stated models, but I would not present them as a resolution of the catalog problem.