```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For digraphs allowing digons, the p=2 problem is NP-complete via a two-layer construction in which matching digons force every weight-2 fractional colouring to encode an ordinary acyclic 2-colouring.",
  "would_publish": true,
  "caveats": "The reduction uses antiparallel pairs; it does not settle a variant restricted to oriented digraphs."
}
```

# Statement

Let \(\mathrm{FDC}(2)\) denote the decision problem

\[
\text{Instance: a digraph }H,\qquad
\text{Question: is }\vec\chi_f(H)\le 2?
\]

Under the standard convention that a pair of opposite arcs is a directed \(2\)-cycle, \(\mathrm{FDC}(2)\) is NP-complete.

In fact, NP-hardness holds for digraphs whose vertices are arranged in two layers, with corresponding vertices joined by digons and with no other arcs between the layers.

# Fractional dichromatic colourings

Let \(\mathcal A(H)\) be the family of vertex sets inducing acyclic subdigraphs of \(H\). The fractional dichromatic number is the optimum of

\[
\begin{aligned}
\min \quad &\sum_{A\in\mathcal A(H)}x_A\\
\text{subject to}\quad
&\sum_{\substack{A\in\mathcal A(H)\\v\in A}}x_A\ge 1
&&\text{for every }v\in V(H),\\
&x_A\ge 0
&&\text{for every }A\in\mathcal A(H).
\end{aligned}
\]

## Membership in NP

Although this LP has exponentially many variables, every yes-instance has a polynomially encoded certificate.

If \(N=|V(H)|\), an optimal basic feasible solution has at most \(N\) positive variables. The relevant constraint matrices have entries in \(\{0,1\}\), so Cramer's rule and Hadamard's determinant bound give numerators and denominators with \(O(N\log N)\) bits. A certificate lists the at most \(N\) acyclic sets and their rational weights. One can verify in polynomial time that each listed set is acyclic, that every vertex receives weight at least \(1\), and that the total weight is at most \(2\). Hence \(\mathrm{FDC}(2)\in\mathrm{NP}\).

# Reduction

We reduce from the established NP-complete problem of deciding whether a digraph has dichromatic number at most \(2\), i.e. whether its vertex set can be partitioned into two acyclic sets. This NP-completeness is also part of the supplied source-paper premise.

Given a nonempty digraph \(D\), construct a digraph \(H=R(D)\) as follows. For each \(v\in V(D)\), introduce two vertices

\[
v_0=(v,0),\qquad v_1=(v,1).
\]

For every arc \(uv\in A(D)\) and each \(i\in\{0,1\}\), add the arc

\[
u_i v_i.
\]

Thus each layer induces a copy of \(D\). Finally, for every \(v\in V(D)\), add both arcs

\[
v_0v_1,\qquad v_1v_0.
\]

There are no other cross-layer arcs. The construction has \(2|V(D)|\) vertices and \(2|A(D)|+2|V(D)|\) arcs.

We prove

\[
\boxed{\ \vec\chi_f(R(D))\le 2
\quad\Longleftrightarrow\quad
\vec\chi(D)\le 2.\ }
\]

## Forcing lemma

Suppose \((x_A)_{A\in\mathcal A(H)}\) is a fractional acyclic colouring of \(H\) with total weight

\[
W=\sum_A x_A\le 2.
\]

Fix \(v\in V(D)\). Since \(v_0,v_1\) form a digon, no acyclic set \(A\) contains both. Therefore

\[
\begin{aligned}
2
&\le
\sum_{A\ni v_0}x_A+\sum_{A\ni v_1}x_A\\
&=
\sum_A x_A\,|A\cap\{v_0,v_1\}|\\
&\le
\sum_A x_A
=W
\le 2.
\end{aligned}
\]

All inequalities are consequently equalities. In particular,

\[
\sum_A x_A\bigl(1-|A\cap\{v_0,v_1\}|\bigr)=0.
\]

Every summand is nonnegative. Hence for every \(A\) with \(x_A>0\),

\[
|A\cap\{v_0,v_1\}|=1.
\]

Thus every acyclic set in the positive support of a weight-\(2\) fractional colouring chooses exactly one copy of every original vertex.

## Forward implication

Assume \(\vec\chi_f(H)\le2\), and choose any acyclic set \(A\) having positive weight in a feasible fractional colouring of total weight at most \(2\).

By the forcing lemma, the sets

\[
C_i=\{v\in V(D):v_i\in A\},\qquad i\in\{0,1\},
\]

partition \(V(D)\).

For each \(i\), the copy of \(D[C_i]\) in layer \(i\) is an induced subdigraph of \(H[A]\). Since \(H[A]\) is acyclic, both \(D[C_0]\) and \(D[C_1]\) are acyclic. Hence \(C_0,C_1\) form an acyclic \(2\)-colouring of \(D\), and therefore

\[
\vec\chi(D)\le2.
\]

## Reverse implication

Conversely, suppose

\[
V(D)=C_0\mathbin{\dot\cup}C_1
\]

with both \(D[C_0]\) and \(D[C_1]\) acyclic. Define

\[
A=(C_0\times\{0\})\cup(C_1\times\{1\})
\]

and

\[
B=(C_0\times\{1\})\cup(C_1\times\{0\})=V(H)\setminus A.
\]

Each matching digon has one endpoint in \(A\) and one in \(B\), so neither \(H[A]\) nor \(H[B]\) contains a matching arc. Moreover,

\[
H[A]\cong D[C_0]\mathbin{\dot\cup}D[C_1],
\]

with the two terms lying in different layers. Thus \(H[A]\) is acyclic. The same argument, with the layers exchanged, shows that \(H[B]\) is acyclic.

Assigning weight \(1\) to each of \(A\) and \(B\) gives every vertex total coverage \(1\), with total weight \(2\). Therefore

\[
\vec\chi_f(H)\le2.
\]

This proves the equivalence.

# Complexity conclusion

The map \(D\mapsto R(D)\) is a polynomial-time many-one reduction from acyclic \(2\)-colourability of digraphs to \(\mathrm{FDC}(2)\). Therefore \(\mathrm{FDC}(2)\) is NP-hard. Together with membership in NP:

\[
\boxed{\text{Deciding whether }\vec\chi_f(D)\le2\text{ is NP-complete}.}
\]

Combined with the results quoted from the source paper, this closes the sole missing threshold \(p=2\).

# Scope and gaps

The proof uses digons essentially: the two opposite arcs force an acyclic set to contain at most one of \(v_0,v_1\). Consequently, the argument settles the stated digraph/multidigraph problem but does not settle a potentially stronger version in which the input is required to be an oriented graph. No other gap is present in the reduction.