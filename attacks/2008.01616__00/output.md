```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A birthday-sampling argument gives a one-sided-error randomized O(n^(3/2) log n) algorithm, but the deterministic conjecture remains unresolved.",
  "would_publish": false,
  "caveats": "This disproves the statement only if bounded-error randomized algorithms are included; no deterministic truly subquadratic algorithm or lower bound is proved."
}
```

# 1. Statement and interpretation

Let \(N\) denote the size of the standard flag representation of a map; this is within a constant factor of the usual combinatorial encoding size. I obtain:

**Proposition.** Isomorphism of connected maps has a one-sided-error randomized algorithm running in
\[
O(N^{3/2}\log N)
\]
time and \(O(N^{3/2})\) space. It never declares two nonisomorphic maps isomorphic, and accepts isomorphic maps with probability at least \(2/3\).

Thus, if “algorithm” in Conjecture 1.2 includes bounded-error randomized algorithms, the conjecture as written is false. Under the likely intended interpretation—deterministic algorithms—the proposition is only partial progress.

I also give a deterministic truly subquadratic algorithm for maps possessing a sufficiently rare, isomorphism-invariant class of flags.

# 2. Maps as bounded-arity transition systems

A map can be represented by its flag set \(F\), together with the three flag involutions
\[
\rho_0,\rho_1,\rho_2:F\to F,
\]
where \(\rho_i\) changes the \(i\)-dimensional member of a flag. The corresponding edge-colored flag graph is connected. A map isomorphism is precisely a bijection
\[
\varphi:F(M)\longrightarrow F(M')
\]
satisfying
\[
\varphi\rho_i=\rho_i'\varphi,\qquad i=0,1,2.
\]

This representation covers orientable and nonorientable maps uniformly. Other standard permutation representations convert to it with only constant-factor overhead.

The argument below applies more generally to every connected transition system
\[
X=(\Omega;s_1,\ldots,s_d)
\]
with fixed \(d\), where the \(s_i\) are permutations and generate a transitive action.

## Lemma 2.1: Linear-time rooted canonical code

For every flag \(x\in F(M)\), one can compute in \(O(N)\) time a word \(C_M(x)\) of length \(O(N)\) such that
\[
C_M(x)=C_{M'}(y)
\]
if and only if there is a map isomorphism \(M\to M'\) sending \(x\) to \(y\).

### Proof

Starting at \(x\), perform breadth-first search in the flag graph, considering colors \(0,1,2\) in a fixed order. Number flags in their order of discovery:
\[
x=x_1,x_2,\ldots,x_N.
\]
Output the table
\[
C_M(x)=\bigl(a_{j,i}:1\leq j\leq N,\ 0\leq i\leq2\bigr),
\qquad
\rho_i(x_j)=x_{a_{j,i}}.
\]

The flag graph is connected, so every flag is numbered. An isomorphism sending \(x\) to \(y\) preserves the BFS discovery order, by induction, and hence gives identical tables.

Conversely, equality of the two tables makes the bijection \(x_j\mapsto y_j\) intertwine all three involutions, and therefore it is a map isomorphism. The search and construction inspect only constantly many transitions at each flag, so they take \(O(N)\) time. ∎

This is the usual reason that map isomorphism becomes easy once the image of one flag is prescribed.

# 3. A randomized truly subquadratic algorithm

Let \(M,M'\) be two maps with \(N\) flags each; unequal sizes can be rejected immediately. Put
\[
k=\left\lceil\sqrt{N\log 3}\right\rceil,
\]
capped at \(N\) for the finitely many small cases.

Choose independently and uniformly random \(k\)-element subsets
\[
S\subseteq F(M),\qquad T\subseteq F(M').
\]

Compute
\[
\{C_M(x):x\in S\}
\quad\text{and}\quad
\{C_{M'}(y):y\in T\}.
\]
Sort the \(2k\) codes lexicographically, retaining which input map each code came from. Return YES if some code occurs for both maps, and return NO otherwise.

## Correctness on nonisomorphic maps

By Lemma 2.1, equality \(C_M(x)=C_{M'}(y)\) certifies an isomorphism carrying \(x\) to \(y\). Consequently, if \(M\not\cong M'\), no cross-map code equality is possible. The algorithm therefore never produces a false positive.

## Success probability on isomorphic maps

Suppose \(M\cong M'\), and fix one isomorphism
\[
\varphi:F(M)\to F(M').
\]
If
\[
\varphi(S)\cap T\neq\varnothing,
\]
then some \(x\in S\) satisfies \(\varphi(x)\in T\), and Lemma 2.1 gives
\[
C_M(x)=C_{M'}(\varphi(x)).
\]
Thus the algorithm returns YES.

Conditional on \(S\), the set \(\varphi(S)\) is a fixed \(k\)-element subset of \(F(M')\). Hence
\[
\Pr\bigl[T\cap\varphi(S)=\varnothing\bigr]
 =\frac{\binom{N-k}{k}}{\binom Nk}
 \leq \left(1-\frac{k}{N}\right)^k
 \leq e^{-k^2/N}
 \leq \frac13.
\]
Therefore an isomorphic pair is accepted with probability at least \(2/3\). Repetition amplifies this probability in the usual way.

## Running time

There are \(2k=O(\sqrt N)\) rooted codes, each computable in \(O(N)\) time. Generating all codes costs
\[
O(kN)=O(N^{3/2}).
\]

A direct comparison sort uses \(O(k\log k)\) comparisons, each involving strings of length \(O(N)\), and therefore costs
\[
O(kN\log k)=O(N^{3/2}\log N).
\]
The same bound covers exact comparison, so no hashing error is needed. In particular,
\[
N^{3/2}\log N=O(N^{7/4}),
\]
which is truly subquadratic.

The space bound from storing all codes is \(O(N^{3/2})\).

# 4. A deterministic special case

There is also a simple deterministic reduction whenever flags admit a rare invariant type.

Let
\[
c_M:F(M)\to\Sigma
\]
be an isomorphism-invariant coloring computable in linear or near-linear time, with canonically comparable color names. Thus every isomorphism \(\varphi:M\to M'\) satisfies
\[
c_{M'}(\varphi(x))=c_M(x).
\]

Examples include
\[
c_M(x)=\bigl(\deg(v_x),\,\deg(f_x)\bigr),
\]
where \(v_x\) and \(f_x\) are the vertex and face incident with \(x\), possibly augmented by further local incidence data.

Compare the two color histograms. If they differ, reject. Otherwise choose a nonempty color class of minimum cardinality, say of size \(r\). Fix one flag \(x\) of that color in \(M\), compute \(C_M(x)\), and compare it with \(C_{M'}(y)\) for every flag \(y\) of the same color in \(M'\).

If the maps are isomorphic, the image of \(x\) is among these \(r\) flags. Conversely, equality of one rooted code certifies an isomorphism. The running time is
\[
O(rN).
\]

Consequently:

**Corollary.** If an isomorphism-invariant flag coloring has a nonempty class of size at most \(N^{1-\delta}\), then map isomorphism is deterministically decidable in
\[
O(N^{2-\delta})
\]
time on that class of instances.

In particular, if the coloring takes at least \(N^\delta\) distinct values, its smallest class has size at most \(N^{1-\delta}\).

# 5. Remaining gap

The randomized algorithm relies essentially on birthday intersection between two independently sampled sets of possible root images. It is not a zero-error or deterministic algorithm: on an isomorphic pair it can miss every corresponding pair of sampled flags.

No argument above computes all relevant rooted codes in deterministically subquadratic time, nor does it establish any classical lower bound. Thus:

- under a bounded-error randomized interpretation, the stated conjecture is disproved;
- under the standard deterministic interpretation apparently intended by the source paper, Conjecture 1.2 remains open;
- the statement should explicitly specify the computational model and whether randomization is excluded.