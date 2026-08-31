```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general odd-order conjecture remains open, but I prove an exact sparse-overlap criterion, a universal near-stacking bound of (n-3)/2 conflicts, and the conjecture for affine midpoint colorings of every odd prime-power order.",
  "would_publish": false,
  "caveats": "No argument eliminates the remaining conflicts for arbitrary dense proper colorings, and the proposed exhaustive SAT search was not run."
}
```

# 1. Setup

Let \(\chi_1,\chi_2\) be proper edge-colorings of \(K_n\). After fixing the placement of \(\chi_1\), a stacking is determined by a permutation \(\pi\) of the vertices. Put
\[
X(\pi)=\bigl|\{e\in E(K_n):\chi_1(e)=\chi_2(\pi(e))\}\bigr|.
\]
Thus \(\pi\) is a rainbow stacking exactly when \(X(\pi)=0\).

For each color \(c\), write
\[
a_c=|\chi_1^{-1}(c)|,\qquad b_c=|\chi_2^{-1}(c)|.
\]
Colors absent from one coloring are assigned multiplicity zero there. Since both colorings are proper, every color class is a matching, so
\[
a_c,b_c\leq \left\lfloor\frac n2\right\rfloor.
\]
Let
\[
N=\binom n2,\qquad P=\sum_c a_cb_c.
\]

For a uniformly random vertex permutation \(\pi\), a fixed edge is mapped uniformly to one of the \(N\) edges. Consequently,
\[
\mathbb E X(\pi)=\frac{P}{N}. \tag{1}
\]

# 2. An exact sparse-overlap criterion

## Theorem 2.1

If \(n\geq 3\) and
\[
\sum_c a_cb_c\leq \binom n2,
\]
then \(\chi_1,\chi_2\) admit a rainbow stacking.

In particular, the conclusion holds if every color class of either coloring has size at most \(1\).

### Proof

If \(P<N\), then (1) gives \(\mathbb E X<1\). Since \(X\) is a nonnegative integer, some permutation has \(X=0\).

It remains to treat \(P=N\). Suppose, for contradiction, that every permutation has a conflict. Then \(X(\pi)\geq1\) for every \(\pi\), while \(\mathbb E X=1\). Hence
\[
X(\pi)=1\qquad\text{for every }\pi. \tag{2}
\]

Call a pair \((e,f)\), where
\[
\chi_1(e)=\chi_2(f),
\]
a bad event. Two distinct bad events \((e,f)\) and \((e',f')\) are jointly realizable if some vertex permutation maps \(e\) to \(f\) and \(e'\) to \(f'\). By (2), no two bad events can be jointly realizable.

For each vertex \(w\) in the target copy of \(K_n\), let
\[
\mathcal L_w=\{(e,f):\chi_1(e)=\chi_2(f),\ w\in f\}.
\]
I claim that the source edges appearing in \(\mathcal L_w\) are pairwise disjoint.

Indeed, take two distinct events \((e,f),(e',f')\in\mathcal L_w\).

* If \(f=f'\), then \(e,e'\) have the same color in \(\chi_1\), so properness makes them disjoint.
* If \(f\neq f'\), then \(f,f'\) meet at \(w\). Their colors are distinct by properness of \(\chi_2\). If \(e,e'\) also met, mapping their common endpoint to \(w\) and their other endpoints to the other endpoints of \(f,f'\) would realize both events simultaneously. This is impossible by (2).

Therefore
\[
|\mathcal L_w|\leq \left\lfloor\frac n2\right\rfloor.
\]
Every bad event is counted at the two endpoints of its target edge, so
\[
2P=\sum_w|\mathcal L_w|
   \leq n\left\lfloor\frac n2\right\rfloor
   <n(n-1)=2N
\]
for \(n\geq3\). Thus \(P<N\), contradicting \(P=N\). Hence a rainbow stacking exists. \(\square\)

The final assertion follows because, if \(b_c\leq1\) for every \(c\), then
\[
P=\sum_c a_cb_c\leq\sum_ca_c=N,
\]
and similarly with the two colorings interchanged.

# 3. A universal near-stacking bound

For odd \(n\), write
\[
q=\frac{n-1}{2},
\qquad N=nq.
\]
The trivial first-moment estimate gives a permutation with at most \(q\) conflicts. The next result saves one conflict uniformly.

## Theorem 3.1

For every pair of proper edge-colorings of \(K_n\), where \(n\geq3\) is odd, there is a permutation \(\pi\) satisfying
\[
X(\pi)\leq \frac{n-3}{2}.
\]

Thus every pair admits a stacking with at most \((n-3)/2\) non-rainbow superpositions.

### Extremal reduction

Because \(b_c\leq q\),
\[
P=\sum_c a_cb_c\leq q\sum_ca_c=qN. \tag{3}
\]
If the inequality is strict, then \(\mathbb E X<q\), and hence some integer value satisfies \(X\leq q-1\).

Equality in (3) is very rigid. It implies \(b_c=q\) for every color used by \(\chi_1\). Since a proper coloring of \(K_n\) needs at least \(n\) color classes of size at most \(q\), equality is possible only when:

1. both colorings use exactly \(n\) colors;
2. they use the same color palette; and
3. every color class in both colorings has exactly \(q\) edges.

It therefore remains only to treat this optimal common-palette case.

## Lemma 3.2: the second moment in the optimal case

Suppose both colorings use the same \(n\) colors and every color class has \(q=(n-1)/2\) edges. For uniform \(\pi\),
\[
\mathbb E X=q
\]
and
\[
\operatorname{Var}(X)
 =q+\frac{q-1}{2q-1}>0. \tag{4}
\]

### Proof

Each color class is a matching covering \(n-1\) vertices and therefore misses a unique vertex. Moreover, distinct colors miss distinct vertices: every vertex is incident with \(n-1\) distinct colors and hence misses exactly one of the \(n\) colors.

Write
\[
X=\sum_{e\in E(K_n)} I_e,
\qquad
I_e=\mathbf 1_{\{\chi_1(e)=\chi_2(\pi(e))\}}.
\]
Each \(I_e\) has expectation \(q/N=1/n\), giving \(\mathbb E X=q\).

We calculate \(\mathbb E\binom X2\) by classifying unordered pairs of source edges. Let \((n)_k=n(n-1)\cdots(n-k+1)\).

### Adjacent source edges

There are
\[
n\binom{n-1}{2}=\frac{n(n-1)(n-2)}2
\]
such pairs. Their colors \(c,d\) are distinct. In the target coloring, exactly \(n-2\) vertices are incident with both a \(c\)-edge and a \(d\)-edge. Hence
\[
\Pr(I_e=I_{e'}=1)=\frac{n-2}{(n)_3}
=\frac1{n(n-1)}.
\]

### Disjoint source edges of the same color

There are
\[
n\binom q2=\frac{n(n-1)(n-3)}8
\]
such pairs. Their images must be two distinct edges in the same \(q\)-edge matching, giving
\[
\Pr(I_e=I_{e'}=1)
=\frac{4q(q-1)}{(n)_4}
=\frac1{n(n-2)}.
\]

### Disjoint source edges of different colors

There are
\[
3\binom n4-n\binom q2
=\frac{n(n-1)(n-3)^2}{8}
\]
such pairs. For two distinct target colors \(c,d\), their near-perfect matchings have exactly \(n-2\) adjacent pairs of edges. Thus the number of disjoint ordered pairs, one edge of each color, is
\[
q^2-(n-2)=\frac{(n-3)^2}{4}.
\]
It follows that
\[
\Pr(I_e=I_{e'}=1)
 =\frac{(n-3)^2}{(n)_4}
 =\frac{n-3}{n(n-1)(n-2)}.
\]

Summing the three contributions gives
\[
\mathbb E\binom X2
 =\frac{(n-1)^2}{8}
  +\frac{n-3}{4(n-2)}.
\]
Equivalently,
\[
\mathbb E[X(X-1)]
 =q^2+\frac{q-1}{2q-1}.
\]
Therefore
\[
\operatorname{Var}(X)
 =\mathbb E[X(X-1)]+\mathbb E X-(\mathbb E X)^2
 =q+\frac{q-1}{2q-1},
\]
proving (4). \(\square\)

### Completion of Theorem 3.1

In the extremal case, \(X\) has mean \(q\) and positive variance, so it is not constantly equal to \(q\). If every permutation had \(X\geq q\), its mean \(q\) would force \(X\equiv q\), contradicting (4). Hence some permutation has \(X<q\), and integrality gives \(X\leq q-1=(n-3)/2\). \(\square\)

For \(n=3\), this already gives a genuine rainbow stacking. For \(n=5\), it gives a permutation with at most one conflict, but does not by itself eliminate that final conflict.

# 4. The conjecture for affine midpoint colorings

There is also a dense, optimal infinite family for which the full conjecture holds.

Let \(Q\) be an odd prime power and identify the vertices with \(\mathbb F_Q\). Define the midpoint coloring
\[
\kappa(\{x,y\})=\frac{x+y}{2}.
\]
It is proper: for fixed \(x\), the map \(y\mapsto(x+y)/2\) is injective. Each color class has \((Q-1)/2\) edges and misses its midpoint vertex.

An affine midpoint coloring means any coloring obtained from \(\kappa\) by arbitrary vertex and color relabelings.

## Lemma 4.1: relative derangements in a 2-transitive group

Let a finite group \(G\) act 2-transitively on a set \(\Omega\) of size at least \(2\). For every permutation \(\sigma\in S_\Omega\), there is \(g\in G\) such that
\[
g(x)\neq\sigma(x)\qquad\text{for every }x\in\Omega.
\]

### Proof

For \(g\in G\), put
\[
A(g)=|\{x:g(x)=\sigma(x)\}|.
\]
By transitivity, for each fixed \(x\), exactly \(|G|/|\Omega|\) elements of \(G\) send \(x\) to \(\sigma(x)\). Hence
\[
\frac1{|G|}\sum_{g\in G}A(g)=1.
\]
If every \(g\) had at least one agreement with \(\sigma\), then every \(g\) would have exactly one agreement. But for distinct \(x,y\), 2-transitivity supplies \(g\) satisfying
\[
g(x)=\sigma(x),\qquad g(y)=\sigma(y),
\]
giving at least two agreements. Contradiction. \(\square\)

## Theorem 4.2

Every pair of affine midpoint colorings of \(K_Q\), for \(Q\) an odd prime power, admits a rainbow stacking. The two colorings may use arbitrary color names, and their palettes need not coincide.

### Proof

After choosing vertex coordinates, write
\[
\chi_1(\{x,y\})=\alpha\!\left(\frac{x+y}{2}\right),
\qquad
\chi_2(\{x,y\})=\beta\!\left(\frac{x+y}{2}\right),
\]
where \(\alpha,\beta\) are injective relabelings of \(\mathbb F_Q\) into the global color set.

Equality of a source color \(\alpha(c)\) with a target color \(\beta(d)\) defines a partial bijection \(c\mapsto d\) between subsets of \(\mathbb F_Q\). Extend it arbitrarily to a permutation \(\sigma\) of \(\mathbb F_Q\).

The affine group
\[
\operatorname{AGL}(1,Q)=\{T(x)=ax+b:a\neq0\}
\]
is 2-transitive. By Lemma 4.1, choose \(T\) such that
\[
T(c)\neq\sigma(c)\qquad\text{for every }c.
\]
Use \(T\) as the relative vertex placement. Since affine maps preserve midpoints,
\[
\frac{T(x)+T(y)}2=T\!\left(\frac{x+y}{2}\right).
\]
Thus, if an edge has source midpoint \(c\), its target color is \(\beta(T(c))\). Equality
\[
\alpha(c)=\beta(T(c))
\]
would imply \(T(c)=\sigma(c)\), contrary to the choice of \(T\). Therefore no edge conflict occurs. \(\square\)

This handles arbitrary pairs inside the affine near-one-factorization class, but not arbitrary optimal \(Q\)-edge-colorings.

# 5. A complete SAT formulation for fixed \(n\)

Although I did not run it, the following encoding searches all possible counterexamples for a fixed \(n\), including arbitrary numbers of colors.

Let \(E=E(K_n)\), \(|E|=N\), and take \(N\) potential common color labels \(c\in[N]\). This is sufficient because every color occurring in both colorings must occur on at least one of the \(N\) edges in each coloring.

Introduce Boolean variables
\[
A_{e,c},\qquad B_{e,c}.
\]
They mean that edge \(e\) receives common color \(c\) in the first or second coloring. Impose:

1. For every edge \(e\), at most one \(A_{e,c}\) and at most one \(B_{e,c}\) is true.
2. For every vertex \(v\), color \(c\), and two distinct edges \(e,e'\) incident with \(v\),
   \[
   \neg A_{e,c}\vee\neg A_{e',c},
   \qquad
   \neg B_{e,c}\vee\neg B_{e',c}.
   \]

Unassigned edges can subsequently be given fresh, side-private colors.

For each vertex permutation \(\pi\), edge \(e\), and color \(c\), introduce \(Z_{\pi,e,c}\), with clauses
\[
\neg Z_{\pi,e,c}\vee A_{e,c},
\qquad
\neg Z_{\pi,e,c}\vee B_{\pi(e),c}.
\]
Finally, for each \(\pi\), impose
\[
\bigvee_{e\in E,\ c\in[N]} Z_{\pi,e,c}.
\]
Thus every permutation is forced to have a common-colored superimposed edge.

This SAT instance is satisfiable if and only if a counterexample exists for that \(n\). For \(n=7\), it has
\[
2N^2=882
\]
basic coloring variables and
\[
7!\,N^2=5040\cdot441=2{,}222{,}640
\]
witness variables before symmetry reductions. An UNSAT conclusion should be accompanied by a checkable proof certificate; no such computation is claimed here.

# 6. Remaining gap

The general conjecture is not resolved by these arguments. In the worst odd-order case,
\[
P=\frac{n-1}{2}\binom n2,
\]
whereas Theorem 2.1 only handles \(P\leq\binom n2\). The second-moment argument saves exactly one conflict over averaging but gives no mechanism for eliminating the remaining \((n-3)/2\) conflicts. The affine argument relies essentially on a 2-transitive automorphism group and does not extend to arbitrary near-one-factorizations.

Thus no counterexample is produced, and no complete proof for arbitrary odd \(n\) is claimed.