```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove logarithmic stability under point deletion and slicewise polynomial-time exact computation at fixed deletion distance from separability, but not an FPT algorithm in separable index.",
  "would_publish": false,
  "caveats": "The slicewise exact algorithms are nonuniform in deletion distance; no general constant-factor approximation or hardness classification is obtained, and novelty has not been checked against the full paper."
}
```

# 1. Scope of the partial result

The parameterized complexity asked in the question remains unresolved here. In particular, I do not obtain an FPT or XP algorithm parameterized by \(\operatorname{sep}(\pi)\), nor a constant-factor FPT approximation.

There is, however, a useful additional parameter for which one can prove both constructive bounds and an exact, albeit nonuniform, complexity result.

Write
\[
d_{\mathcal S}(\pi)
=\min\{|D|:\pi-D\text{ is separable}\},
\qquad
\mathcal E_d=\{\pi:d_{\mathcal S}(\pi)\le d\}.
\]
Deletion means deletion of entries followed by standardization. In inversion-graph language, \(d_{\mathcal S}\) is vertex-deletion distance to a cograph.

I use the positive-length convention
\[
\operatorname{sep}(\pi)
=\min\{r\ge 1:\pi=\alpha_r\circ\cdots\circ\alpha_1,\ 
                  \alpha_i\text{ separable}\}.
\]
If the identity is assigned index zero, it can simply be handled separately.

## Partial theorem

The following statements hold.

1. **Logarithmic stability under deletion.** If a nonempty permutation \(\rho\) is obtained from \(\pi\) by deleting \(d\ge1\) entries, then
   \[
   \boxed{\operatorname{sep}(\rho)
   \le \operatorname{sep}(\pi)
   \le \operatorname{sep}(\rho)+1+\lceil\log_2 d\rceil.}
   \]
   For one deletion, the sharper formulation is
   \[
   \boxed{0\le \operatorname{sep}(\pi)-\operatorname{sep}(\rho)\le1.}
   \]

2. **Constructive bound near the separable class.** If a deletion set of size \(d\) making \(\pi\) separable is supplied, one can construct a factorization of length at most
   \[
   B(d)=
   \begin{cases}
   1,&d=0,\\
   2+\lceil\log_2 d\rceil,&d\ge1.
   \end{cases}
   \]
   A minimum such deletion set can be found in time
   \[
   O(4^{d_{\mathcal S}(\pi)}n^4).
   \]
   In particular, exact separable index is explicitly polynomial-time computable on \(\mathcal E_1\).

3. **Fixed deletion-distance slices are in P, nonuniformly in the distance.** For every fixed \(d\), there exists a polynomial-time algorithm computing exact separable index on \(\mathcal E_d\).

   This assertion uses finite obstruction sets whose existence is proved below. The proof does **not** provide a uniform procedure computing those sets from \(d\), or an effective bound on their sizes.

4. **The logarithmic dependence is optimal in the extremal sense.** If
   \[
   F(d)=\sup_{\pi\in\mathcal E_d}\operatorname{sep}(\pi),
   \]
   then
   \[
   \boxed{F(d)=\Theta(\log(d+2)).}
   \]

These are results about a different parameter. Section 7 gives simple permutations with separable index two and unbounded \(d_{\mathcal S}\), so the distinction cannot be removed by first passing to simple substitution quotients.

# 2. Order chains and elementary closure properties

A permutation can be represented by two total orders on the same ground set: its position order \(L_0\) and its value order \(L_\pi\).

A factorization into \(r\) separable permutations is equivalent to a chain
\[
L_0,L_1,\ldots,L_r=L_\pi
\]
such that the relative permutation between every two consecutive orders is separable. The relative permutations compose because each transition maps old ranks to new ranks.

The elementary facts needed from the previous attempt can be checked directly in this representation.

### Pattern monotonicity

If \(\tau\) is a pattern of \(\pi\), then
\[
\operatorname{sep}(\tau)\le \operatorname{sep}(\pi).
\]
Indeed, restrict every order of a factorization chain to the entries inducing \(\tau\). Every transition becomes a pattern of a separable permutation.

Consequently
\[
\mathcal C_k=\{\pi:\operatorname{sep}(\pi)\le k\}
\]
is a permutation class.

### Substitution and parallel transitions

Separable permutations are generated from the singleton by direct and skew sums. It follows by induction that an inflation of a separable permutation by separable permutations is separable.

In particular:

- replacing an entry of a separable transition by two adjacent entries, adjacent in both orders, preserves separability;
- separable transitions on disjoint consecutive blocks can be performed simultaneously: their direct sum is separable.

More generally, if several consecutive blocks each have index at most \(r\), their factorizations can be padded with identities and executed in parallel in \(r\) steps.

### Reversal invariance

Reversing positions preserves the class of separable permutations. Therefore
\[
\operatorname{sep}(\pi^{\mathrm{rev}})
=\operatorname{sep}(\pi).
\]
For example, in a factorization of \(\pi\), absorb the position reversal into the first factor; that factor remains separable. Reversing again gives equality.

# 3. Inserting one point costs at most one factor

### Lemma 3.1

Suppose \(\rho\) is obtained from \(\pi\) by deleting one entry, and \(\rho\) is nonempty. Then
\[
\operatorname{sep}(\pi)\le \operatorname{sep}(\rho)+1.
\]

### Proof

Let \(x\) be the deleted entry. Choose an entry \(y\) adjacent to \(x\) in the original position order.

Take a factorization chain
\[
L_0,L_1,\ldots,L_r
\]
for \(\rho\), where \(r=\operatorname{sep}(\rho)\). Extend every order \(L_t\) by inserting \(x\) immediately beside \(y\), on the same side as in the original position order.

Each extended transition is an inflation of the old separable transition: the entry \(y\) is replaced by the adjacent pair \(\{x,y\}\), in the same internal order at both ends. Hence each extended transition remains separable.

After these \(r\) transitions, all entries other than \(x\) are in their required final order. It remains only to move \(x\) to its required place.

Moving a single entry is a separable transition. On the affected interval it is a permutation of one of the forms
\[
23\cdots t1
\qquad\text{or}\qquad
t12\cdots(t-1),
\]
both of which are skew sums of increasing permutations. Outside that interval the transition is the identity.

Thus one additional separable factor suffices. \(\square\)

Together with pattern monotonicity, this proves the one-deletion assertion. Iterating also gives the preliminary bound
\[
\operatorname{sep}(\pi)\le d_{\mathcal S}(\pi)+1.
\]

## An explicit exact algorithm on \(\mathcal E_1\)

On this class,
\[
\operatorname{sep}(\pi)=
\begin{cases}
1,&\pi\text{ is separable},\\
2,&\pi\text{ is not separable}.
\end{cases}
\]

The promise \(\pi\in\mathcal E_1\) can also be checked in polynomial time:

1. Test whether \(\pi\) avoids \(2413\) and \(3142\).
2. If not, find one forbidden occurrence \(Q\).
3. Test deletion of each of its four entries.

Any deletion making \(\pi\) separable must hit \(Q\), so these four tests suffice. Naive enumeration of quadruples gives \(O(n^4)\) time overall. In the successful nonseparable case, Lemma 3.1 constructs an optimal two-factor factorization.

## Finding a deletion set

The same observation gives a bounded-search-tree algorithm for \(d_{\mathcal S}\).

At a current permutation:

- if it is separable, succeed;
- otherwise find an occurrence of \(2413\) or \(3142\);
- branch on deleting one of its four entries.

With deletion budget \(d\), the search has \(O(4^d)\) nodes, each requiring \(O(n^4)\) time using naive pattern detection. Iterating budgets up to the optimum still takes
\[
O(4^{d_{\mathcal S}(\pi)}n^4).
\]

This is FPT in deletion distance, not in separable index.

# 4. Logarithmic stability under multiple deletions

The main constructive ingredient is a separable binary grouping operation.

### Lemma 4.1 — binary grouping

Suppose entries in a current order are colored \(0\) and \(1\). There is a separable transition which puts all \(0\)-entries first, in their current relative order, followed by all \(1\)-entries in reverse of their current relative order.

### Proof

For a binary word \(w=c_1\cdots c_m\), recursively define
\[
q_w=
\begin{cases}
1\oplus q_{c_2\cdots c_m},&c_1=0,\\
1\ominus q_{c_2\cdots c_m},&c_1=1.
\end{cases}
\]
The empty word gives the empty permutation.

This is separable by construction. The values assigned to \(0\)-positions are the lowest ranks, in increasing order of position. The values assigned to \(1\)-positions are the highest ranks, in decreasing order of position. \(\square\)

### Theorem 4.2

Let \(\rho\) be obtained from \(\pi\) by deleting \(d\ge1\) entries. Then
\[
\operatorname{sep}(\pi)
\le \operatorname{sep}(\rho)+1+\lceil\log_2d\rceil.
\]
Given a factorization of \(\rho\), the proof constructs the claimed factorization of \(\pi\).

### Proof

Let \(D\) be the deleted set and \(r=\operatorname{sep}(\rho)\).

Partition the final value order into \(d\) consecutive, nonempty buckets
\[
I_1,\ldots,I_d,
\]
each containing exactly one member of \(D\). Such a partition is obtained by placing cuts between consecutive members of \(D\) in value order.

Take a balanced binary tree whose leaves, from left to right, are these buckets. Its height is
\[
h=\lceil\log_2d\rceil.
\]

Starting with the original position order, process this tree by depth. For every current block, color its entries according to which of its two child blocks they belong to and apply Lemma 4.1. At any one depth the operations are on disjoint consecutive blocks, so their direct sum is separable.

After \(h\) transitions, the buckets are consecutive and occur in their required final order.

Consider the relative order inside one bucket. Every grouping operation either preserves or reverses the relative order of all entries of that bucket. Hence its current order is either its original position order or the reverse of that order.

Delete the bucket’s unique member of \(D\). The remaining relative permutation is therefore a pattern of \(\rho\), possibly with positions reversed. Its index is at most \(r\). By Lemma 3.1, the whole bucket has index at most \(r+1\). A bucket consisting only of its exceptional entry is already separable.

Factor all buckets in parallel, using \(r+1\) further transitions. The total number is
\[
h+r+1.
\]
\(\square\)

Taking \(\rho\) separable gives
\[
\operatorname{sep}(\pi)
\le 2+\lceil\log_2 d_{\mathcal S}(\pi)\rceil
\]
when \(d_{\mathcal S}(\pi)\ge1\).

The grouping operations and the remaining local factorizations are all constructive. Combined with the branching algorithm, this gives a uniform
\[
4^{d_{\mathcal S}(\pi)}n^{O(1)}
\]
algorithm producing the stated factorization.

A useful class inclusion is
\[
\boxed{\mathcal E_{\,2^{k-2}}\subseteq\mathcal C_k
\qquad(k\ge2).}
\]
Thus an obstruction to index at most \(k\) must have deletion distance greater than \(2^{k-2}\).

# 5. Exact computation on every fixed deletion-distance slice

The next result is exact, but its nonuniformity is essential.

## 5.1 Finite-colored separable permutations are well-quasi-ordered

Recall that a quasi-order is a well-quasi-order if every infinite sequence contains an earlier term below a later term.

### Lemma 5.1

For any finite set of colors, the separable permutations whose entries carry those colors are well-quasi-ordered under color-preserving pattern containment.

### Proof

Encode each separable permutation by a rooted plane binary decomposition tree:

- internal vertices are labeled \(+\) or \(-\), for direct or skew sum;
- leaves carry the colors of the corresponding entries.

Use the ordered form of Kruskal’s tree theorem: finite rooted plane trees with labels in a finite alphabet are well-quasi-ordered under label-preserving homeomorphic embedding.

Such an embedding of decomposition trees induces a color-preserving pattern embedding of their leaf permutations. Indeed, the plane embedding preserves position order. For any two selected leaves, their value comparison is determined by the sign at their lowest common ancestor, which is preserved by the tree embedding.

Applying Kruskal’s theorem to any chosen sequence of decomposition trees gives the required comparable pair. \(\square\)

## 5.2 Bounded point extensions remain well-quasi-ordered

### Lemma 5.2

For every fixed \(d\), the class \(\mathcal E_d\) is well-quasi-ordered by pattern containment.

### Proof

Take an infinite sequence from \(\mathcal E_d\).

Bounded-length terms cause no difficulty, since there are only finitely many permutations of bounded length. We may therefore work with permutations of length greater than \(d\). For each permutation choose exactly \(d\) distinguished entries whose deletion leaves a separable permutation. A smaller deletion set can be enlarged, because separability is hereditary.

Pass to an infinite subsequence in which the distinguished entries induce the same permutation \(\delta\in S_d\).

Color every remaining entry \(x\) by
\[
\left(
\#\{\text{distinguished entries preceding }x\},
\#\{\text{distinguished entries below }x\}
\right).
\]
There are only \((d+1)^2\) colors.

By Lemma 5.1, an earlier colored separable remainder embeds in a later one. Map the distinguished entries according to their common pattern \(\delta\). The two color coordinates ensure that every comparison between a remaining entry and a distinguished entry is preserved, in both position and value order.

The two maps therefore combine into a pattern embedding of the whole earlier permutation into the later one. \(\square\)

## 5.3 Finite obstruction sets within each slice

Let \(\mathcal B_k\) be the set of minimal excluded permutations for \(\mathcal C_k\).

### Proposition 5.3

For all fixed \(d,k\),
\[
\boxed{\mathcal B_k\cap\mathcal E_d\text{ is finite}.}
\]

### Proof

Minimal excluded permutations form an antichain. Lemma 5.2 rules out an infinite antichain in \(\mathcal E_d\). \(\square\)

For a promised input \(\pi\in\mathcal E_d\), we have
\[
\operatorname{sep}(\pi)>k
\quad\Longleftrightarrow\quad
\pi\text{ contains a member of }\mathcal B_k\cap\mathcal E_d.
\]
For the forward implication, choose a shortest pattern of \(\pi\) outside \(\mathcal C_k\). It belongs to \(\mathcal E_d\), since \(\mathcal E_d\) is hereditary. The reverse implication is pattern monotonicity.

For fixed \(d,k\), the obstruction list is finite. Testing containment of each fixed pattern by enumerating position subsets is polynomial-time.

Moreover, Section 4 bounds the possible index on \(\mathcal E_d\) by the constant \(B(d)\). Hardwiring the finitely many obstruction lists for
\[
1\le k<B(d)
\]
therefore gives an exact polynomial-time algorithm on \(\mathcal E_d\).

**What is and is not proved:** for each fixed \(d\), there exists an ordinary polynomial-time algorithm; no advice depending on input length is needed. But this proof does not construct the family of algorithms uniformly from \(d\). In particular, it does not establish a uniform FPT or XP algorithm parameterized by \(d\).

There is also a useful criticality property.

### Proposition 5.4

If \(\beta\in\mathcal B_k\), where \(k\ge1\), then
\[
\operatorname{sep}(\beta)=k+1,
\]
and deleting any single entry of \(\beta\) gives a permutation of index exactly \(k\).

### Proof

Every one-entry deletion \(\tau\) belongs to \(\mathcal C_k\). Lemma 3.1 gives
\[
k<\operatorname{sep}(\beta)
\le \operatorname{sep}(\tau)+1
\le k+1.
\]
All inequalities force the asserted values. \(\square\)

Thus, if some \(\mathcal B_k\) is infinite, its members must have unbounded deletion distance from separability. The finite-slice argument cannot by itself prove that \(\mathcal B_k\) is finite.

# 6. Sharpness of the logarithmic distance bound

We prove
\[
F(d)=\Theta(\log(d+2)).
\]

The upper bound was established in Section 4.

For the lower bound, every separable permutation of length \(n\) has a signed plane binary decomposition tree with \(n\) leaves. There are at most
\[
4^{n-1}\cdot2^{n-1}=8^{n-1}
\]
such trees. Hence there are at most \(8^{n-1}\) separable permutations of length \(n\), and at most
\[
8^{r(n-1)}
\]
products of \(r\) of them.

Every permutation of length \(d+1\) belongs to \(\mathcal E_d\). Padding factorizations by identities therefore gives
\[
(d+1)!\le 8^{dF(d)}
\]
for \(d\ge1\), and consequently
\[
F(d)\ge
\frac{\log((d+1)!)}{d\log8}
=\Omega(\log(d+2)).
\]

This is an **extremal** sharpness statement. It does not say that the constructed factorization is a constant-factor approximation on each individual input.

# 7. Why this does not give FPT in separable index

The mismatch between the parameters persists even on simple permutations.

For \(m\ge2\), consider the parallel alternation
\[
\lambda_m=2,4,\ldots,2m,1,3,\ldots,2m-1.
\]

It has separable index exactly two. Indeed, let
\[
a_m=1,2,\ldots,m,2m,2m-1,\ldots,m+1
\]
and
\[
b_m=2,4,\ldots,2m,2m-1,2m-3,\ldots,1.
\]
Then
\[
\lambda_m=b_m\circ a_m.
\]
The permutation \(a_m\) is a direct sum of an increasing and a decreasing permutation. Also,
\[
b_1=21,\qquad
b_m=(1\oplus b_{m-1})\ominus1,
\]
so every \(b_m\) is separable. Thus \(\operatorname{sep}(\lambda_m)\le2\), while its first two even entries and first two odd entries induce \(2413\), giving equality.

The permutation \(\lambda_m\) is simple:

- an interval of positions contained wholly in either half has values of one parity, so cannot be a nontrivial permutation interval;
- an interval crossing the boundary between the halves contains both \(2m\) and \(1\), so it can be a permutation interval only if it contains every entry.

Finally, for
\[
j=1,3,5,\ldots,\qquad j+1\le m,
\]
the positions
\[
j,\ j+1,\ m+j,\ m+j+1
\]
induce \(2413\). These occurrences are pairwise disjoint. Every deletion set making \(\lambda_m\) separable must hit all of them, so
\[
d_{\mathcal S}(\lambda_m)\ge\lfloor m/2\rfloor.
\]

Therefore
\[
\operatorname{sep}(\lambda_m)=2,
\qquad
d_{\mathcal S}(\lambda_m)\longrightarrow\infty,
\]
even though every \(\lambda_m\) is simple.

Consequently:

- a running time exponential in \(d_{\mathcal S}\) is not an FPT running time in separable index;
- a logarithmic bound in \(d_{\mathcal S}\) does not certify any constant approximation ratio in separable index;
- substitution decomposition does not remove this obstruction.

# 8. Remaining gaps

The original questions remain open in this attack:

1. No FPT or XP algorithm parameterized by \(k=\operatorname{sep}(\pi)\) is obtained.
2. No fixed-\(k\) NP-hardness result is obtained, including for \(k=2\).
3. No constant-factor FPT approximation in \(k\) is obtained.
4. The exact polynomial-time algorithms on fixed deletion-distance slices are nonuniform: the proof supplies neither their obstruction lists nor an effective bound on those lists.
5. Finite obstruction sets in each \(\mathcal E_d\) do not establish finite baseness of \(\mathcal C_k\).

The concrete progress is the logarithmic deletion-stability theorem, the explicit exact algorithm at deletion distance one, and the finite-obstruction/slicewise-P result for every fixed deletion distance. None is presented as a resolution of Question 1.3.