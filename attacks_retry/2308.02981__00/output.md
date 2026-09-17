```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove uniform Theta(log k) bounds for forbidden layered patterns whose layers have size at most two, and their symmetries, but do not obtain a worst-case polynomial bound.",
  "would_publish": false,
  "caveats": "No improvement to the general upper bound on F(k); novelty of these partial results has not been checked."
}
```

# 1. Statement of the partial result

Let \(\mathrm{Sep}\) denote the separable permutations. I use the equivalent descriptions
\[
\mathrm{Sep}=\operatorname{Av}(2413,3142)
\]
and “permutations obtainable from singletons by direct and skew sums.”

Write
\[
\operatorname{si}(\sigma)
=\min\{d\ge 1:\sigma=\alpha_1\circ\cdots\circ\alpha_d,\ \alpha_i\in\mathrm{Sep}\},
\qquad
I(\pi)=\sup_{\sigma\in\operatorname{Av}(\pi)}\operatorname{si}(\sigma).
\]
Thus the identity has index \(1\). Allowing an empty product changes only trivial boundary cases.

The question asks whether
\[
F(k)=\max_{\pi\in S_k}I(\pi)
\]
is polynomially bounded.

Define
\[
L_r=\underbrace{21\oplus21\oplus\cdots\oplus21}_{r\text{ summands}}.
\]

## Theorem 1

For \(r\ge2\), every \(L_r\)-avoiding permutation can be partitioned into at most \(2r-2\) separable induced subpermutations. Consequently,
\[
I(L_r)\le 1+2\left\lceil\log_2(2r-2)\right\rceil.
\]

More generally, suppose \(\pi\) is a direct sum of \(r\) blocks, each equal to \(1\) or \(21\), and let \(k=|\pi|\ge2\). If \(r\ge2\), then
\[
\boxed{
\frac{\log((k-1)!)}{(k-1)\log 8}
\le I(\pi)
\le 1+2\left\lceil\log_2(2r-2)\right\rceil.
}
\]
The same conclusion holds for every reverse, complement, or inverse of such a pattern. The exceptional case \(r=1,\ k\ge2\) is \(\pi=21\), for which \(I(\pi)=1\).

In particular, uniformly over this family,
\[
I(\pi)=\Theta(\log k).
\]

This extends the monotone-pattern special case in the previous attempt. I also sharpen its coloring-to-factorization lemma, replacing its overhead \(4\lceil\log_2r\rceil\) by \(2\lceil\log_2r\rceil\).

A limitation of this approach is particularly clear:

## Proposition 2

For every **nonseparable** pattern \(\pi\), there is no finite bound on the number of separable induced subpermutations needed to partition members of \(\operatorname{Av}(\pi)\).

This is not a counterexample to the conjecture: the explicit permutations establishing Proposition 2 all have separable index exactly \(2\).

---

# 2. A sharper coloring-to-factorization lemma

The elementary ideas in the previous attempt can be verified directly. The following modification—reversing one side of each binary grouping—improves the constants.

## 2.1. Binary folds are separable

Given a linearly ordered set whose elements are marked \(0\) or \(1\), form a new order by listing:

1. the \(0\)-marked elements in their old order;
2. the \(1\)-marked elements in reverse old order.

Call this a **fold**. As a permutation of the old positions, it is an increasing sequence followed by a decreasing sequence.

Every such permutation is separable. Indeed, its minimum is at one of its two ends. Removing that minimum leaves another permutation of the same form. Induction therefore constructs it by direct or skew sums with a singleton.

## 2.2. Grouping \(r\) colors using \(\lceil\log_2r\rceil\) folds

Let
\[
q=\lceil\log_2r\rceil,
\]
and pad the color palette with unused colors to obtain \(2^q\) colors, labeled by binary words of length \(q\).

First fold according to the first bit. Then, inside each resulting consecutive block, fold according to the second bit, and continue.

At each level, the folds on the different blocks form a direct sum of separable permutations, hence constitute one separable permutation. After \(q\) levels:

- colors occur in a fixed order;
- each individual color occurs either in its original order or in reverse;
- the orientation of a color depends only on its binary label.

In particular, the orientations do not depend on the particular colored ordered set.

## Lemma 3 — Parallelizing colored permutations

Suppose the entries of \(\sigma\) are colored with \(r\) colors, and each color-induced permutation has separable index at most \(d\), where \(d\ge1\). Then
\[
\boxed{\operatorname{si}(\sigma)\le d+2\lceil\log_2r\rceil.}
\]

If every color induces an increasing permutation, then
\[
\operatorname{si}(\sigma)\le
\max\{1,2\lceil\log_2r\rceil\}.
\]

### Proof

For color \(c\), list its positions and values increasingly:
\[
x_{c,1}<\cdots<x_{c,m_c},
\qquad
y_{c,1}<\cdots<y_{c,m_c}.
\]

Apply the preceding \(q\)-fold procedure to the ordered positions, producing a permutation \(P\), and separately to the ordered values, producing \(Q\). Both are products of \(q\) separable permutations; when \(q=0\), these are empty routing stages.

The color blocks have the same order in \(P\) and \(Q\), and each color has the same orientation in both. Thus
\[
D=Q^{-1}\circ\sigma\circ P
\]
is a direct sum
\[
D=D_1\oplus\cdots\oplus D_r.
\]
If \(\sigma_c\) is the usual color-induced permutation, then
\[
D_c=\sigma_c
\quad\text{or}\quad
D_c=\rho_{m_c}\circ\sigma_c\circ\rho_{m_c},
\]
where \(\rho_m\) is reversal.

Conjugation by reversal preserves separability and preserves products of \(d\) separable permutations. Therefore every \(D_c\) has a factorization into \(d\) separable permutations, padding with identities when necessary. Taking direct sums of corresponding factors gives a \(d\)-factor decomposition of \(D\).

Finally,
\[
\sigma=Q\circ D\circ P^{-1},
\]
which uses at most \(q+d+q\) factors.

If all \(\sigma_c\) are increasing, then \(D\) is the identity and the middle stage can be omitted. \(\square\)

As another consequence of the fold construction, every permutation of length \(n\) has index at most
\[
\max\{1,\lceil\log_2n\rceil\}.
\]
Assign a distinct color to each value, with color order equal to the desired one-line order, and perform the grouping procedure.

---

# 3. Two splitting lemmas

Let
\[
c(\pi)=\sup_{\sigma\in\operatorname{Av}(\pi)}
\chi_{\mathrm{sep}}(\sigma),
\]
where \(\chi_{\mathrm{sep}}(\sigma)\) is the minimum number of separable induced subpermutations partitioning its entries. This supremum may be infinite.

## Lemma 4 — A southwest-quadrant split

For nonempty patterns \(\alpha,\beta\), every permutation avoiding \(\alpha\oplus\beta\) can be colored red and blue so that:

- red avoids \(\alpha\oplus1\);
- blue avoids \(1\oplus\beta\).

Consequently,
\[
c(\alpha\oplus\beta)
\le c(\alpha\oplus1)+c(1\oplus\beta)
\]
whenever the right-hand side is finite.

### Proof

Color an entry \(x\) blue if there is an occurrence of \(\alpha\) entirely southwest of \(x\): all its positions precede \(x\), and all its values are smaller than \(x\). Otherwise color \(x\) red.

A red occurrence of \(\alpha\oplus1\) is impossible because its final entry would be blue.

Suppose blue contains \(1\oplus\beta\), and let \(x\) be the first, smallest entry of that occurrence. Since \(x\) is blue, an occurrence of \(\alpha\) lies southwest of it. Combining that occurrence with the selected \(\beta\), and omitting \(x\), gives \(\alpha\oplus\beta\), a contradiction. \(\square\)

We also need a two-coloring of \(1324\)-avoiders. I give the proof rather than relying on its literature status.

## Lemma 5

Every \(1324\)-avoiding permutation is a merge of a \(132\)-avoiding permutation and a \(213\)-avoiding permutation. In particular,
\[
c(1324)\le2.
\]

### Proof

Process entries from left to right. Color the current entry blue if either:

1. coloring it red would create a red \(132\); or
2. an earlier blue entry is smaller than it.

Otherwise color it red. By construction, red avoids \(132\).

Suppose blue contains a \(213\), with entries \(b,c,d\), in that positional order, satisfying
\[
c<b<d.
\]
Choose such an occurrence with the position of \(c\) as early as possible.

There is no earlier blue entry \(e<c\). Indeed:

- if \(e\) precedes \(b\), then \(e,b,c,d\) forms \(1324\);
- if \(e\) lies between \(b\) and \(c\), then \(b,e,d\) is a blue \(213\) whose middle entry occurs earlier.

Thus condition 2 did not force \(c\) to be blue. Condition 1 did, so there are red entries \(a,h\), in that order before \(c\), with
\[
a<c<h.
\]

If \(a\) precedes \(b\), then \(a,b,c,d\) forms \(1324\).

Otherwise both \(a\) and \(h\) follow the blue entry \(b\). Since \(h\) was colored red, condition 2 implies \(h<b\). Hence
\[
a<c<h<b<d,
\]
and \(a,h,c,d\) forms \(1324\), again a contradiction.

Therefore blue avoids \(213\).

Finally,
\[
\operatorname{Av}(132)\subseteq\mathrm{Sep},
\qquad
\operatorname{Av}(213)\subseteq\mathrm{Sep},
\]
because both \(2413\) and \(3142\) contain both of these three-point patterns. \(\square\)

Together with Lemma 3, this already gives
\[
I(1324)\le3.
\]

---

# 4. Layered forbidden patterns with layers of size at most two

Set
\[
P_t=1\oplus L_t,
\qquad
Q_t=1\oplus L_t\oplus1.
\]

I claim
\[
c(Q_t)\le2t,
\qquad
c(P_t)\le2t-1.
\]

The initial cases are
\[
Q_1=1324,\qquad P_1=132,
\]
so Lemma 5 gives \(c(Q_1)\le2\), while \(c(P_1)=1\).

For \(t\ge2\), write
\[
Q_t=(1\oplus L_{t-1})\oplus(21\oplus1).
\]
Lemma 4 gives a split into
\[
\operatorname{Av}(Q_{t-1})
\quad\text{and}\quad
\operatorname{Av}(1324).
\]
Thus
\[
c(Q_t)\le c(Q_{t-1})+2\le2t.
\]

Similarly,
\[
P_t=(1\oplus L_{t-1})\oplus21
\]
splits into \(\operatorname{Av}(Q_{t-1})\) and \(\operatorname{Av}(132)\), yielding
\[
c(P_t)\le2(t-1)+1=2t-1.
\]

Finally, for \(r\ge2\),
\[
L_r=21\oplus L_{r-1}.
\]
Another application of Lemma 4 splits \(\operatorname{Av}(L_r)\) into
\[
\operatorname{Av}(213)
\quad\text{and}\quad
\operatorname{Av}(P_{r-1}).
\]
Therefore
\[
\boxed{c(L_r)\le1+(2r-3)=2r-2.}
\]

Lemma 3 now proves
\[
I(L_r)\le1+2\lceil\log_2(2r-2)\rceil.
\]

Suppose \(\pi\) is a direct sum of \(r\) blocks, each \(1\) or \(21\). It is a pattern of \(L_r\), obtained by selecting one or both entries from each \(21\)-block. Hence
\[
\operatorname{Av}(\pi)\subseteq\operatorname{Av}(L_r),
\]
and the same upper bound holds for \(I(\pi)\).

For completeness, separable index is invariant under inverse, reverse, and complement with the convention used here. Inversion reverses and inverts the factors. A reversal or complement can be absorbed into an end factor, since these operations preserve separability. Applying the operation twice gives equality of indices. Pattern avoidance transforms equivariantly, establishing the symmetry assertion in Theorem 1.

In particular,
\[
I(2143)\le3,\qquad I(3412)\le3.
\]

---

# 5. The logarithmic lower bound is universal

The counting argument from the previous attempt admits a simpler formulation: its elementary lower bound holds for **every** forbidden pattern of size \(k\).

Let \(s_n=|\mathrm{Sep}\cap S_n|\). Representing a separable permutation by a plane full binary tree with direct/skew labels gives
\[
s_n\le 2^{n-1}C_{n-1}<8^n.
\]
Consequently, at most
\[
s_n^D<8^{Dn}
\]
permutations of length \(n\) have separable index at most \(D\). Shorter factorizations can be padded with identities.

Now let \(|\pi|=k\) and put \(n=k-1\). Every member of \(S_n\) avoids \(\pi\). Thus, if every \(\pi\)-avoider has index at most \(D\), then
\[
n!\le8^{Dn},
\]
and therefore
\[
\boxed{I(\pi)\ge\frac{\log((k-1)!)}{(k-1)\log8}.}
\]

Since
\[
\frac{\log((k-1)!)}{k-1}=\log k-1+o(1),
\]
this is \(\Omega(\log k)\).

For the family in Theorem 1, \(r\le k\), so the upper bound is \(O(\log k)\). This proves the asserted uniform \(\Theta(\log k)\) result.

## Sharper monotone special case

Lemma 3 also improves the previous attempt’s monotone upper bound to
\[
\boxed{
I(12\cdots k)=I(k\cdots21)
\le \max\{1,2\lceil\log_2(k-1)\rceil\}.
}
\]

Indeed, if \(\sigma\) avoids a decreasing subsequence of length \(k\), color an entry by the maximum length of a decreasing subsequence ending there. There are at most \(k-1\) colors, and each color is increasing. Apply the increasing-color case of Lemma 3. Complementation handles the other monotone pattern.

---

# 6. Why finite separable colorings cannot handle the general problem

Here is a rigorous obstruction to extending this particular approach to arbitrary forbidden patterns.

## 6.1. Inflation has no additional factorization cost

For nonempty permutations \(\sigma_1,\ldots,\sigma_m\), write
\[
\tau[\sigma_1,\ldots,\sigma_m]
\]
for their inflation into the entries of \(\tau\).

### Lemma 6
\[
\boxed{
\operatorname{si}\bigl(\tau[\sigma_1,\ldots,\sigma_m]\bigr)
=
\max\bigl\{\operatorname{si}(\tau),
          \operatorname{si}(\sigma_1),\ldots,
          \operatorname{si}(\sigma_m)\bigr\}.
}
\]

### Proof

First, separable index does not increase on taking a pattern. Restrict a factorization to the chosen positions and to their successive images under the factors. Standardizing these intermediate ordered sets gives a factorization of the induced pattern by patterns of the original separable factors. This proves the lower bound, since the skeleton and each block occur as patterns of the inflation.

For the upper bound, the relevant composition identity is
\[
a[\gamma_{b^{-1}(1)},\ldots,\gamma_{b^{-1}(m)}]
\circ b[\eta_1,\ldots,\eta_m]
=
(a\circ b)[\gamma_1\circ\eta_1,\ldots,\gamma_m\circ\eta_m],
\]
where \(|\gamma_i|=|\eta_i|\). The reindexing accounts for the intermediate order of the blocks.

Let \(d\) be the displayed maximum, and pad all skeleton and block factorizations to length \(d\). Iterating this identity constructs \(d\) global factors. Each is an inflation of a separable skeleton by separable blocks, and hence is separable. \(\square\)

In particular, repeated inflation cannot itself increase the index beyond the largest index of one of its constituent skeletons.

## 6.2. Index two, but unbounded separable coloring number

Let
\[
\tau=3142,\qquad \sigma_0=1,
\qquad
\sigma_t=\tau[\sigma_{t-1},\sigma_{t-1},\sigma_{t-1},\sigma_{t-1}].
\]
Then \(|\sigma_t|=4^t\).

### Claim 1: \(\sigma_t\) avoids \(2413\)

The pattern \(2413\) is simple: it has no proper nontrivial interval.

In any occurrence inside an inflation, selected entries belonging to one block form an interval of the selected pattern. Therefore an occurrence of \(2413\) either:

- lies wholly in one block; or
- uses at most one entry from each block.

The first possibility is excluded inductively. In the second, all four blocks must be used, producing \(3142\), not \(2413\). This proves the claim.

### Claim 2: Every separable induced subpermutation of \(\sigma_t\) has at most \(3^t\) entries

Such a subpermutation cannot meet all four top-level blocks: selecting one point from each would give \(3142\). Hence it meets at most three blocks. Its restriction to each is separable, so induction bounds its size by
\[
3\cdot3^{t-1}=3^t.
\]
Consequently,
\[
\chi_{\mathrm{sep}}(\sigma_t)
\ge
\left\lceil\frac{4^t}{3^t}\right\rceil
\longrightarrow\infty.
\]

### Claim 3: \(\operatorname{si}(\sigma_t)=2\) for \(t\ge1\)

Explicitly,
\[
3142=1243\circ4132,
\]
and both factors are separable. Since \(3142\) is not separable, its index is exactly \(2\). Lemma 6 gives the assertion for every \(\sigma_t\).

Thus
\[
c(2413)=\infty
\]
even though the witnessing family has constant index \(2\). By inversion, \(c(3142)=\infty\) as well.

Finally, every nonseparable pattern \(\pi\) contains \(2413\) or \(3142\). If, for example, it contains \(2413\), then
\[
\operatorname{Av}(2413)\subseteq\operatorname{Av}(\pi).
\]
The other case is symmetric. Hence
\[
\boxed{c(\pi)=\infty\quad\text{for every nonseparable }\pi,}
\]
proving Proposition 2.

---

# 7. Remaining gap

The results above prove logarithmic bounds for a family of non-monotone forbidden patterns and improve the elementary monotone bound. They do **not** improve the upper bound on
\[
F(k)=\max_{\pi\in S_k}I(\pi).
\]

Moreover, the coloring route has an intrinsic limitation: for every nonseparable forbidden pattern, its avoidance class has unbounded separable coloring number. A general proof must therefore exploit factorizations that cannot be obtained merely by partitioning the entries into boundedly many separable pieces.

Inflation parallelization explains one way that factorization can outperform coloring, but it does not control arbitrary permutation skeletons. No general polynomial bound, and no counterexample to one, is established here.