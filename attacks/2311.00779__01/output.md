```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard quotient-lattice models the decision problem is in NP with quadratic-length certificates, and the distances between the extremal diagonal and generic rectangulations are exactly linear, but neither a polynomial-time algorithm nor NP-hardness is established.",
  "would_publish": false,
  "caveats": "This uses the standard combinatorial Baxter/diagonal and 2-clumped/generic flip graphs with fixed boundary and canonical labels; other notions of rectangulation or flip require separate treatment."
}
```

# 1. Formalization and results

The phrase “rectangulation flip distance” has several variants. I use the two standard finite combinatorial models arising as quotients of the weak order on \(S_n\):

- \(\mathcal D_n\): diagonal, equivalently weak/Baxter, rectangulations;
- \(\mathcal G_n\): generic/strong rectangulations, corresponding to the 2-clumped congruence.

In each case there is a surjection
\[
q:S_n\longrightarrow \mathcal R_n
\]
whose fibers are classes of a lattice congruence of the weak order, and the rectangulation flip graph is the cover graph of the quotient lattice. Rectangles carry the canonical labels from this construction. Geometric coordinates are not part of the input; a rectangulation is given by its combinatorial incidence data.

I prove the following partial results.

### Theorem A: complexity upper bounds

For either standard rectangulation flip graph on \(n\) rectangles:

1. Its diameter is at most
   \[
   \binom n2.
   \]
2. The decision problem
   \[
   \textsc{Rectangulation-Flip-Distance}
   =\{(R,S,k):d(R,S)\le k\}
   \]
   belongs to NP.
3. The numerical distance belongs to \(FP^{NP[\log n]}\).
4. With \(k\) as parameter, straightforward local search runs in
   \[
   n^{O(k)}
   \]
   time. Thus the problem is in XP parameterized by distance.
5. There is an exact exhaustive algorithm running in
   \[
   O(n!\,n^2)
   \]
   time, up to polynomial factors for encoding and hashing.

These statements do not establish polynomial-time solvability or NP-hardness.

### Theorem B: exact extremal distances

Let \(R^-_n=q(12\cdots n)\) and \(R^+_n=q(n\cdots21)\) be the bottom and top rectangulations of the quotient lattice.

For diagonal/Baxter rectangulations,
\[
d_{\mathcal D_n}(R^-_n,R^+_n)
 =\sum_{j=1}^{\min(2,n-1)}(n-j)
 =
 \begin{cases}
 0,&n=1,\\
 2n-3,&n\ge2.
 \end{cases}
\]

For generic/2-clumped rectangulations,
\[
d_{\mathcal G_n}(R^-_n,R^+_n)
 =\sum_{j=1}^{\min(3,n-1)}(n-j)
 =
 \begin{cases}
 0,&n=1,\\
 1,&n=2,\\
 3n-6,&n\ge3.
 \end{cases}
\]

More generally, if \(w\) is obtained from \(12\cdots n\) by reversing pairwise disjoint intervals of consecutive values of lengths \(m_1,\dots,m_s\), then
\[
d_{\mathcal D_n}(q(e),q(w))
 =\sum_{i=1}^s\sum_{j=1}^{\min(2,m_i-1)}(m_i-j),
\]
and
\[
d_{\mathcal G_n}(q(e),q(w))
 =\sum_{i=1}^s\sum_{j=1}^{\min(3,m_i-1)}(m_i-j).
\]

Consequently,
\[
2n-3\le \operatorname{diam}(\mathcal D_n)\le \binom n2
\]
for \(n\ge2\), and
\[
3n-6\le \operatorname{diam}(\mathcal G_n)\le \binom n2
\]
for \(n\ge3\).

# 2. Quotient graphs and the NP upper bound

Let \(L\) be a finite lattice, \(\Theta\) a lattice congruence, and
\[
p:L\longrightarrow L/\Theta
\]
the quotient map.

## Lemma 2.1

If \(x\lessdot y\) in \(L\), then either \(p(x)=p(y)\), or
\[
p(x)\lessdot p(y)
\]
in \(L/\Theta\).

### Proof

Suppose instead that
\[
p(x)<Z<p(y).
\]
Choose \(z\in L\) with \(p(z)=Z\), and put
\[
u=(x\vee z)\wedge y.
\]
Because \(x\le y\), one has \(x\le u\le y\). Moreover,
\[
p(u)
 =(p(x)\vee Z)\wedge p(y)
 =Z.
\]
This contradicts \(x\lessdot y\). ∎

Conversely, every cover in the quotient has a covering pair of representatives. Indeed, if \(A\lessdot B\), choose representatives \(a,b\), replace them by \(a\wedge b\) and \(a\vee b\), and take a saturated chain between these comparable representatives. Since there is no quotient class strictly between \(A\) and \(B\), some cover on that chain projects to \(A\lessdot B\).

Apply this to the weak order on \(S_n\). Its undirected cover graph is the permutahedron graph: two permutations are adjacent when they differ by swapping adjacent positions. Its diameter is \(\binom n2\), since the distance is Kendall tau distance.

Choose representatives \(\sigma\in q^{-1}(R)\) and \(\tau\in q^{-1}(S)\). Project a shortest permutahedron path from \(\sigma\) to \(\tau\) and delete consecutive repetitions. Lemma 2.1 gives a rectangulation-flip walk of length at most
\[
d_{S_n}(\sigma,\tau)\le \binom n2.
\]
This proves the diameter bound.

For NP membership, a certificate can be either:

- a sequence of at most \(\binom n2\) combinatorial rectangulations, with each consecutive pair differing by one locally verifiable flip; or
- for each quotient edge, a pair of adjacent permutations witnessing that edge, together with the polynomial-time computable images under \(q\).

Thus even when \(k\) is written in binary, every yes-instance has a certificate of polynomial length. The exact numerical distance can then be found with \(O(\log n)\) threshold queries to the NP decision problem.

For the XP algorithm, a generalized permutohedron has edge directions among
\[
\{\mathbf e_i-\mathbf e_j:i\ne j\}.
\]
At a vertex there is at most one edge in any fixed oriented direction, so its degree is at most \(n(n-1)\). The standard combinatorial encodings permit all legal flips to be generated in polynomial time. Breadth-first search to depth \(k\) therefore takes
\[
O\!\left((n(n-1))^k\operatorname{poly}(n)\right)
\]
time.

# 3. Local descriptions of the two congruences

Let a permutation contain adjacent entries \(a,b\), where \(a<b\):
\[
\pi=U\,a\,b\,V.
\]
For every intermediate value \(x\in\{a+1,\dots,b-1\}\), write

- \(L\) if \(x\) occurs in \(U\);
- \(R\) if \(x\) occurs in \(V\).

This gives a side word
\[
W_{a,b}(\pi)\in\{L,R\}^{b-a-1}.
\]
Its number of clumps is its number of maximal constant runs.

The relevant generating moves are as follows.

- In the diagonal/Baxter congruence, swapping \(a,b\) is a zero move whenever \(W_{a,b}\) contains both \(L\) and \(R\). Indeed, choosing one intermediate witness on each side gives one of the two Baxter relations.
- In the generic/2-clumped congruence, swapping \(a,b\) is a zero move whenever \(W_{a,b}\) has at least three clumps.

It follows immediately that:

- no Baxter zero move swaps values whose difference is at most \(2\);
- no generic zero move swaps values whose difference is at most \(3\).

This yields useful class invariants.

## Proposition 3.1: short-pair signatures

For a Baxter class \(C\), define
\[
\chi_2(C)=
\left(
\mathbf 1[\pi^{-1}(a)<\pi^{-1}(b)]
\right)_{\substack{a<b\\b-a\le2}},
\qquad \pi\in C.
\]
This is independent of the chosen representative.

For a generic class, the analogous vector
\[
\chi_3(C)=
\left(
\mathbf 1[\pi^{-1}(a)<\pi^{-1}(b)]
\right)_{\substack{a<b\\b-a\le3}}
\]
is well-defined.

Moreover, one quotient edge changes at most one coordinate. Consequently,
\[
d_{\mathcal D_n}(C,C')
 \ge d_H(\chi_2(C),\chi_2(C')),
\]
and
\[
d_{\mathcal G_n}(C,C')
 \ge d_H(\chi_3(C),\chi_3(C')),
\]
where \(d_H\) is Hamming distance.

### Proof

Every defining zero move swaps a pair of value difference at least \(3\), respectively at least \(4\), so the indicated comparisons are constant throughout every congruence class.

Every quotient edge has representatives differing by a single adjacent transposition. Such a transposition reverses only the relative order of the two swapped values. Thus at most one short-pair coordinate changes. ∎

For \(e=12\cdots n\) and \(w_0=n\cdots21\), all short-pair coordinates are reversed. This gives the lower bounds
\[
d_{\mathcal D_n}(q(e),q(w_0))
 \ge \sum_{j=1}^{\min(2,n-1)}(n-j),
\]
and
\[
d_{\mathcal G_n}(q(e),q(w_0))
 \ge \sum_{j=1}^{\min(3,n-1)}(n-j).
\]

It remains to construct matching paths.

# 4. An alternating reduced word for the reverse permutation

## Lemma 4.1

For every \(n\), there is a reduced adjacent-transposition sequence from
\[
12\cdots n
\quad\text{to}\quad
n\cdots21
\]
with the following property:

When values \(a<b\) are swapped, the intermediate values
\[
a+1,a+2,\dots,b-1
\]
lie alternately to the left and to the right of the adjacent pair. Hence the side word has exactly \(b-a-1\) clumps.

### Proof

First let \(n=2m\) be even. Use the brick-wall sorting network with \(2m\) rounds:

- in odd rounds swap positions
  \[
  (1,2),(3,4),\dots,(2m-1,2m);
  \]
- in even rounds swap positions
  \[
  (2,3),(4,5),\dots,(2m-2,2m-1).
  \]

All indicated swaps are performed unconditionally.

Write
\[
O_i=2i-1,\qquad E_j=2j.
\]
A direct induction on the rounds gives the crossing times
\[
T(O_i,E_j)=\langle j-i+1\rangle_{2m},
\]
where the residue lies in \(\{1,\dots,2m\}\), and, for \(i<j\),
\[
T(O_i,O_j)=2m+2-i-j,\qquad
T(E_i,E_j)=i+j.
\]

Equivalently, these formulas follow by tracking the reflecting trajectories of the labels through the two alternating matchings. They show that every pair crosses exactly once, so the resulting word is reduced and ends at \(w_0\).

Now fix \(a<c<b\). Substitution into the displayed crossing-time formulas, considering the four possible parity combinations of \(a,b\), gives:

- if \(c\) is even, then \(a\) and \(c\) cross before \(a\) and \(b\);
- if \(c\) is odd, then \(c\) and \(b\) cross before \(a\) and \(b\).

Immediately before \(a,b\) cross, an even intermediate value is therefore to their left, while an odd intermediate value is to their right. As the values \(a+1,\dots,b-1\) alternate in parity, their side word alternates between \(L\) and \(R\).

For odd \(n\), construct the network on \(n+1\) labels and delete the wire carrying \(n+1\). Deleting a wire from a wiring diagram leaves a valid adjacent-transposition sequence on the remaining wires. Since the deleted label is larger than all remaining labels, it is never an intermediate value between \(a\) and \(b\), so the alternating-side property is preserved. ∎

# 5. Proof of the exact extremal formulas

Project the reduced word from Lemma 4.1 to the appropriate quotient.

## Diagonal/Baxter case

When \(b-a\ge3\), there are at least two intermediate values. Their side word alternates, so both \(L\) and \(R\) occur. The corresponding adjacent transposition is therefore a Baxter zero move.

When \(b-a\le2\), Proposition 3.1 shows that the edge cannot be contracted.

Thus the projected path has exactly one paid flip for each pair of values of difference \(1\) or \(2\). Its length is
\[
\sum_{j=1}^{\min(2,n-1)}(n-j).
\]
This matches the signature lower bound.

## Generic/2-clumped case

When \(b-a\ge4\), the alternating side word has at least three clumps, so the adjacent transposition is a generic zero move.

When \(b-a\le3\), its orientation is part of the invariant \(\chi_3\), so the transition is noncontracted.

Thus the projected path has exactly one paid flip for each pair of values of difference at most \(3\), giving
\[
\sum_{j=1}^{\min(3,n-1)}(n-j).
\]
Again this meets the lower bound.

The same construction can be run independently inside any interval of consecutive values. For disjoint intervals, concatenate the corresponding networks. The short-pair signature gives the sum of the individual lower bounds, proving the stated block-reversal formulas.

# 6. Small sanity check

For \(n=4\), the brick-wall sequence can be linearized as
\[
1234\to2134\to2143\to2413\to4213\to4231\to4321.
\]

In the Baxter quotient,
\[
2143\equiv2413,
\]
because the intermediate values \(2,3\) lie on opposite sides of the adjacent pair \(1,4\). Hence the projected path has length \(5=2\cdot4-3\).

In the generic quotient, that side word has only two clumps, so the same transition is not contracted. Thus the distance is \(6=3\cdot4-6\), equal to the full Kendall distance.

At \(n=4\), the two Baxter zero edges are
\[
2143\leftrightarrow2413,\qquad
3142\leftrightarrow3412,
\]
giving \(22\) quotient classes. There are no generic zero edges for \(n=4\), giving \(24\) classes. At \(n=5\), the only possible generic zero moves swap \(1,5\) with side word \(LRL\) or \(RLR\); there are four such edges, yielding \(120-4=116\) classes.

# 7. Fully specified exhaustive algorithm

For small \(n\), the quotient graph can be constructed directly.

1. Enumerate all \(\pi\in S_n\).
2. Initialize a union-find structure on \(S_n\).
3. For every adjacent-position swap in every \(\pi\), form its side word:
   - in the diagonal model, union the two permutations if both \(L\) and \(R\) occur;
   - in the generic model, union them if the side word has at least three clumps.
4. The union-find components are the rectangulation congruence classes.
5. For every adjacent-position swap, add an edge between the two components if they are distinct.
6. Run breadth-first search between the two input components.

With inverse-position arrays, testing one potential move takes \(O(n)\). There are \(n!(n-1)\) directed adjacent-position swaps, so the construction takes
\[
O(n!\,n^2)
\]
time and \(O(n!\,\operatorname{poly}(n))\) memory. Every quotient edge is found because every quotient cover has a weak-order cover witness.

# 8. Remaining gap

The main complexity question is not settled here. In particular:

- there is no polynomial-time algorithm for arbitrary pairs of rectangulations;
- there is no NP-hardness reduction;
- the \(n^{O(k)}\) search is XP, not an FPT algorithm;
- the short-pair signatures have only \(O(n)\) coordinates and need not determine distance for arbitrary pairs, because swaps of widely separated labels can be either contracted or paid depending on their context.

Thus, under the standard combinatorial model, the problem is narrowed to an NP shortest-path problem of polynomial diameter, with exact formulas for a nontrivial family of pairs, but its P-versus-NP-hard status remains open.