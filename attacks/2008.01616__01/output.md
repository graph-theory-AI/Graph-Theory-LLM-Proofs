```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "No conditional superlinear lower bound is proved; I formalize the target and prove linear-time algorithms for rooted instances and for tuples admitting a short-word n-cycle, including one-vertex and one-face oriented maps.",
  "would_publish": false,
  "caveats": "The catalog item does not specify the conditioning hypothesis, machine model, encoding, or whether d is fixed."
}
```

# Mathematical writeup

## 1. A precise version of the problem

The catalog item is an open research direction rather than a truth-valued conjecture: a conditional lower bound requires a specified hypothesis, reduction notion, computational model, and input parameter. Without these, one could choose the hypothesis to be the desired conclusion.

A natural fixed-\(d\) formulation is the following.

### Simultaneous conjugacy

Given
\[
A=(a_1,\dots,a_d),\qquad B=(b_1,\dots,b_d)\in S_n^d,
\]
decide whether there is a permutation \(\pi\in S_n\) such that
\[
\pi a_i\pi^{-1}=b_i\qquad (1\leq i\leq d).
\tag{1}
\]
The inverse convention for \(\pi\) is immaterial.

For map isomorphism one takes \(d=2\), with a connected oriented combinatorial map represented by a dart rotation \(R\), an edge-reversing fixed-point-free involution \(L\), and the transitivity condition
\[
\langle R,L\rangle\curvearrowright D
\]
on the dart set \(D\). Orientation-preserving map isomorphism is simultaneous conjugacy of \((R,L)\).

The most meaningful complexity model here is an explicit-array word RAM with word size \(\Theta(\log n)\). The input has \(\Theta(dn)\) words, or \(\Theta(dn\log n)\) bits. Thus:

- if \(d\) is variable, the target should be \(\widetilde O(dn)\), not merely \(\widetilde O(n)\);
- if \(d=2\), an \(n^{1+\Omega(1)}\) conditional lower bound would rule out all \(\widetilde O(n)\) algorithms;
- in a bit model, an \(n\log n\) bound is already “superlinear in \(n\)” but only linear in the input length.

No such lower bound is proved below.

---

## 2. Rooted simultaneous conjugacy is linear-time

The first elementary observation isolates the source of the quadratic baseline.

### Proposition 2.1

Suppose \(\langle a_1,\dots,a_d\rangle\) is transitive on \([n]\). Given \(x,y\in[n]\), one can decide in \(O(dn)\) time whether there is a simultaneous conjugator \(\pi\) satisfying \(\pi(x)=y\). If it exists, it is unique and can be constructed in the same time.

#### Proof

Precompute all \(a_i^{-1}\) and \(b_i^{-1}\). Start with the partial assignment
\[
\pi(x)=y.
\]
Whenever \(\pi(u)=v\) has been assigned, for every \(i\) enforce
\[
\pi(a_i(u))=b_i(v),\qquad
\pi(a_i^{-1}(u))=b_i^{-1}(v).
\]
If a newly required value conflicts with an earlier assignment, or if two domain points are assigned the same image, reject.

Because \(\langle a_1,\dots,a_d\rangle\) is transitive, this propagation reaches every point of \([n]\). If no conflict occurs, the resulting map is an injection \([n]\to[n]\), hence a bijection, and it satisfies
\[
\pi a_i=b_i\pi
\]
for every \(i\). Thus it is a simultaneous conjugator.

For uniqueness, if \(\pi,\rho\) are two conjugators with \(\pi(x)=\rho(x)\), then
\[
h=\rho^{-1}\pi
\]
commutes with every \(a_i\) and fixes \(x\). For every \(u=w(a_1,\dots,a_d)x\),
\[
h(u)=w(a_1,\dots,a_d)h(x)=u.
\]
Transitivity gives \(h=1\), hence \(\pi=\rho\).

Each of the \(n\) points is processed along \(2d\) directed edges, giving \(O(dn)\) time. ∎

Consequently, unrooted transitive simultaneous conjugacy has the elementary \(O(dn^2)\) algorithm obtained by trying all possible images \(y\) of a fixed \(x\). A genuinely subquadratic algorithm must batch these \(n\) rooted tests.

For connected maps, this also proves that rooted map isomorphism is linear-time in the number of darts.

---

## 3. Linear time when a short word is an \(n\)-cycle

There is a substantial family in which all possible root images can be batched by cyclic string matching.

### Theorem 3.1 — cyclic-anchor algorithm

Let \(w\) be a word of length \(\ell\) in \(d\) generators and their inverses. Put
\[
p=w(a_1,\dots,a_d),\qquad q=w(b_1,\dots,b_d).
\]
If \(p\) and \(q\) are \(n\)-cycles, simultaneous conjugacy of \(A\) and \(B\), including the search version, can be solved deterministically in
\[
O((d+\ell)n)
\]
word-RAM time.

All simultaneous conjugators can also be represented by the matching cyclic shifts found in this time.

#### Proof

Choose \(x_0,y_0\in[n]\), and use the two \(n\)-cycles to coordinatize the point sets:
\[
x_t=p^t(x_0),\qquad y_t=q^t(y_0),
\qquad t\in\mathbb Z_n.
\]

Any \(\pi\) satisfying \(\pi p\pi^{-1}=q\) must have the form
\[
\pi(x_t)=y_{t+k}
\tag{2}
\]
for a unique \(k\in\mathbb Z_n\). Indeed, if \(\pi(x_0)=y_k\), then
\[
\pi(x_t)=\pi p^t(x_0)=q^t\pi(x_0)=y_{t+k}.
\]

For each generator \(a_i\), define its displacement relative to the \(p\)-cycle by
\[
a_i(x_t)=x_{t+\Delta^A_i(t)},
\qquad \Delta^A_i(t)\in\mathbb Z_n.
\]
Similarly define
\[
b_i(y_s)=y_{s+\Delta^B_i(s)}.
\]
For a map of the form (2),
\[
\begin{aligned}
\pi a_i(x_t)
  &=y_{t+\Delta^A_i(t)+k},\\
b_i\pi(x_t)
  &=y_{t+k+\Delta^B_i(t+k)}.
\end{aligned}
\]
Thus \(\pi a_i=b_i\pi\) for every \(i\) if and only if
\[
\Delta^A_i(t)=\Delta^B_i(t+k)
\quad\text{for all }i,t.
\tag{3}
\]

Form the length-\(n\) strings over the alphabet \((\mathbb Z_n)^d\)
\[
S_A[t]=\bigl(\Delta^A_1(t),\dots,\Delta^A_d(t)\bigr),
\quad
S_B[t]=\bigl(\Delta^B_1(t),\dots,\Delta^B_d(t)\bigr).
\]
Condition (3) says exactly that \(S_A\) is a cyclic shift of \(S_B\). This can be tested by searching for \(S_A\) in \(S_BS_B\), using KMP or any deterministic linear-time string-matching algorithm. There are \(O(n)\) symbol comparisons, each costing \(O(d)\), so this phase costs \(O(dn)\).

The cycles \(p,q\) can be evaluated in \(O(\ell n)\) time, and their cyclic coordinates and all displacement arrays in \(O(dn)\) time. A matching shift \(k\) explicitly gives the required conjugator through (2). ∎

### Remarks

1. The cyclic necklace represented by \(S_A\) is a complete invariant for tuples equipped with the cyclic anchor \(w(A)\).
2. When \(A=B\), valid shifts are precisely the automorphisms of the tuple lying in the cyclic centralizer of \(p\).
3. If only \(p\) is an \(n\)-cycle and \(q\) is not, the answer is immediately no, since conjugacy preserves cycle type.
4. The theorem applies whenever a suitable short word is supplied or is fixed by the problem structure. Finding such a word in an arbitrary generated permutation group is a different problem.

---

## 4. Consequences for maps

Let an oriented combinatorial map be given by \((R,L)\), where \(R\) rotates darts around vertices and \(L\) reverses each edge.

### Corollary 4.1

Orientation-preserving isomorphism of one-vertex oriented maps can be tested, and an isomorphism found, in \(O(n)\) time.

#### Proof

A one-vertex map has \(R\) as an \(n\)-cycle. Apply Theorem 3.1 with the anchor word \(w(R,L)=R\). ∎

### Corollary 4.2

Orientation-preserving isomorphism of one-face oriented maps can be tested in \(O(n)\) time.

#### Proof

In the standard dart encodings, the face permutation \(F\) is a fixed word of length two in \(R,L\), with the precise word depending on convention. A one-face map has \(F\) as an \(n\)-cycle. Apply Theorem 3.1 with \(w(R,L)=F\). ∎

If the map category also permits global orientation reversal, one runs the same algorithm against the appropriately reversed rotation tuple, adding only a constant factor.

These classes can have genus \(\Theta(n)\). Thus high genus alone cannot support a lower-bound construction: one-vertex and one-face high-genus instances remain linear-time. This does not address general maps with many vertices and faces.

---

## 5. What a successful conditional lower bound would require

For fixed \(d\), simultaneous conjugacy is an isomorphism problem for a bounded-degree relational structure: relation \(i\) contains the arcs
\[
(x,a_i(x)).
\]
The associated Gaifman graph has degree at most \(2d\). Directions and the fixed number of colors can be encoded by bounded-size gadgets. Hence, for fixed \(d\), polynomial-time solvability follows from the bounded-valence graph-isomorphism theorem of Luks. Map isomorphism similarly becomes color-preserving isomorphism of a trivalent flag graph.

Therefore an ordinary polynomial-time Karp reduction from SAT to fixed-\(d\) simultaneous conjugacy or map isomorphism would imply \(P=NP\). A SETH/ETH lower bound must instead use a genuinely fine-grained construction—typically an exponential split-and-list reduction from SAT, or a reduction from a polynomial-time problem such as Orthogonal Vectors.

Here is the quantitative target.

### Reduction target

Assume the Orthogonal Vectors Conjecture in the form that, for suitable \(d=\Theta(\log N)\), OV on two sets of \(N\) vectors has no \(N^{2-\varepsilon}\)-time algorithm for any fixed \(\varepsilon>0\).

Suppose one could reduce OV, in \(N^{\alpha+o(1)}\) time for some \(\alpha<2\), to \(O(1)\) map-isomorphism or fixed-\(d\) simultaneous-conjugacy instances, each of size \(N^{\alpha+o(1)}\). Then an \(m^{p+o(1)}\)-time target algorithm would give an
\[
N^{\alpha p+o(1)}
\]
OV algorithm. Consequently OVC would rule out every
\[
p<\frac{2}{\alpha}.
\]
Since \(\alpha<2\), this would be a truly superlinear target lower bound.

The missing ingredient is exactly such a subquadratic-size reduction. No such reduction is constructed here.

---

## 6. Two structural obstacles to straightforward OV reductions

These observations do not rule out sophisticated reductions, but they exclude two tempting approaches.

### 6.1 Independent coordinate gadgets cannot express orthogonality

There do not exist four objects \(P_0,P_1,Q_0,Q_1\) in any isomorphism category satisfying
\[
P_x\cong Q_y\quad\Longleftrightarrow\quad xy=0.
\tag{4}
\]

Indeed, (4) would give
\[
P_0\cong Q_0,\qquad P_0\cong Q_1,\qquad P_1\cong Q_0.
\]
By symmetry and transitivity of isomorphism, all four objects would then be isomorphic, contradicting the required \(P_1\not\cong Q_1\).

Thus an OV reduction cannot merely place one color-separated component per coordinate and ask for coordinatewise component isomorphism. It must use nonlocal coupling, boundary permutations, or another mechanism that is not simple equality of gadget types.

### 6.2 Isomorphisms of connected tuples form a small coset

Let
\[
C(A)=\{c\in S_n:ca_i=a_ic\text{ for all }i\}.
\]
If \(\pi_0\) is one simultaneous conjugator, then
\[
\operatorname{Iso}(A,B)=\pi_0C(A)=C(B)\pi_0.
\tag{5}
\]
This follows by comparing any solution with \(\pi_0\).

If \(\langle A\rangle\) is transitive, \(C(A)\) acts semiregularly: an element of \(C(A)\) fixing one point fixes its entire orbit and hence is the identity. Therefore
\[
|C(A)|\leq n,\qquad |\operatorname{Iso}(A,B)|\leq n.
\tag{6}
\]

In particular, a connected map on \(n\) darts has at most \(n\) orientation-preserving isomorphisms to another fixed map. A subquadratic-size parsimonious reduction cannot represent all \(N^2\) possible OV witnesses as distinct map isomorphisms. A successful reduction would have to collapse many source witnesses into one target isomorphism. This is not impossible, but it is a genuine design constraint.

---

## 7. Gaps and conclusion

The requested conditional lower bound remains unproved here. In particular:

1. no SETH-, ETH-, or OVC-preserving reduction to map isomorphism or simultaneous conjugacy is supplied;
2. the gadget and coset observations only obstruct simple or parsimonious reductions, not general nonlocal constructions;
3. no argument excludes a general \(\widetilde O(n)\) algorithm;
4. the linear-time results cover rooted instances and instances with a cyclic anchor, but not tuples lacking such an anchor.

The concrete partial result is that any prospective hard family must avoid rootedness and short-word \(n\)-cycles; in the map setting it must in particular use maps with more than one vertex and more than one face, despite possibly having unbounded genus.