```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture when, in each weak component, at most five SCCs have external degree imbalance nonzero modulo k.",
  "would_publish": false,
  "caveats": "The general case is not resolved, and novelty of this arithmetic special case is not claimed."
}
```

## 1. A special case

All digraphs below are finite. Directed cuts are nonempty, and parallel arcs are allowed.

For a strongly connected component \(C\) of a digraph \(G\), define its **external imbalance** by
\[
b(C)=|\delta_G^+(C)|-|\delta_G^-(C)|.
\]

**Theorem.** Let \(G\) have minimum directed-cut size \(k\ge 1\). Suppose that, in each weak component of \(G\), at most five strongly connected components \(C\) satisfy
\[
b(C)\not\equiv 0\pmod k.
\]
Then \(G\) has \(k\) pairwise arc-disjoint dijoins.

The proof establishes a more general residue criterion. Its ingredients are integral circulation decomposition and an uncrossing argument.

### Reduction to weakly connected digraphs

Every directed cut is a union of directed cuts in weak components. Consequently, packings constructed independently in the weak components can be combined, using the same color labels.

Also, a directed cut cannot split a strongly connected component: a directed path from its outside portion to its inside portion would contain an arc entering the cut’s source shore. Thus contracting all strongly connected components, retaining parallel arcs, preserves the directed cuts and their sizes. Arcs internal to a strongly connected component belong to no directed cut.

It therefore suffices to prove the following criterion for a weakly connected digraph.

## 2. The residue criterion

For \(F\subseteq A(D)\), write
\[
b_F(v)=d_F^+(v)-d_F^-(v),\qquad
b_F(X)=\sum_{v\in X}b_F(v).
\]
Write \(b=b_{A(D)}\).

Fix a positive integer \(q\), and define
\[
a_v=\left\lfloor\frac{b(v)}q\right\rfloor,
\qquad
r_v=b(v)-qa_v\in\{0,\ldots,q-1\}.
\]
Put
\[
R=\{v:r_v>0\},\qquad m=|R|,\qquad
h=\frac1q\sum_{v\in R}r_v.
\]
Since \(\sum_v b(v)=0\),
\[
h=-\sum_v a_v
\]
is an integer. If \(R\ne\varnothing\), then
\[
1\le h\le m-1.
\]

**Residue criterion.** Suppose every directed cut of a weakly connected digraph \(D\) has size at least \(q\). If
\[
R=\varnothing
\quad\text{or}\quad
\min\{h,m-h\}\le 2,
\]
then \(A(D)\) can be partitioned into \(q\) dijoins.

For \(q=k\), the theorem follows from this criterion because \(m\le5\) implies
\[
\min\{h,m-h\}\le \lfloor m/2\rfloor\le2.
\]

## 3. A simultaneous rounding lemma

We need to round degree imbalances while also controlling their sums on disjoint vertex sets.

**Lemma.** Let \(D\) be a digraph, let \(q\ge1\), and let \(\mathcal P\) be a family of pairwise disjoint nonempty subsets of \(V(D)\). There is a partition
\[
A(D)=F_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}F_q
\]
such that, for every \(i\),
\[
b_{F_i}(X)\in
\left\{
\left\lfloor\frac{b(X)}q\right\rfloor,
\left\lceil\frac{b(X)}q\right\rceil
\right\}
\tag{1}
\]
whenever \(X\) is a singleton or belongs to \(\mathcal P\).

**Proof.** First recall an elementary integral-circulation decomposition fact. If \(z\) is an integer circulation and \(\ell,u\) are integer arc bounds satisfying
\[
q\ell\le z\le qu,
\]
then \(z\) is the sum of \(q\) integer circulations, each between \(\ell\) and \(u\).

Indeed, for \(q>1\), seek a circulation \(y\) with
\[
\max\{\ell,z-(q-1)u\}
\le y\le
\min\{u,z-(q-1)\ell\}.
\tag{2}
\]
The circulation \(z/q\) satisfies these bounds. Integral circulation feasibility—equivalently, total unimodularity of the vertex–arc incidence matrix—therefore supplies an integer \(y\). The residual \(z-y\) satisfies the corresponding \((q-1)\)-fold bounds, so induction applies. Integer lower bounds may be negative; shifting lower bounds gives the usual circulation formulation.

Now extend \(\mathcal P\) to a partition \(\mathcal B\) of \(V(D)\) by adding singleton blocks for uncovered vertices. Add a vertex \(w_B\) for each \(B\in\mathcal B\), a root \(\rho\), and arcs
\[
v\longrightarrow w_B\quad(v\in B),\qquad
w_B\longrightarrow\rho.
\]
Define an integer circulation \(z\) on this augmented network by assigning:

- value \(1\) to every original arc;
- value \(-b(v)\) to \(v\to w_B\);
- value \(-b(B)\) to \(w_B\to\rho\).

Flow conservation follows directly from the definitions.

Apply the decomposition fact with
\[
\ell_e=\lfloor z_e/q\rfloor,\qquad
u_e=\lceil z_e/q\rceil.
\]
On an original arc, the resulting \(q\) integer values are nonnegative and sum to \(1\), so they define an arc partition \(F_1,\ldots,F_q\). Conservation at the auxiliary vertices identifies the other arc values with \(-b_{F_i}(v)\) and \(-b_{F_i}(B)\). Their rounding bounds give (1). \(\square\)

## 4. Proof of the residue criterion

For a vertex set \(X\), use the notation
\[
a(X)=\sum_{v\in X}a_v,\qquad r(X)=\sum_{v\in X}r_v.
\]

Whenever a partition satisfies the singleton conclusions of the lemma, put
\[
t_i(v)=b_{F_i}(v)-a_v.
\]
Then
\[
t_i(v)=0\quad(v\notin R),\qquad
t_i(v)\in\{0,1\}\quad(v\in R).
\]
Moreover,
\[
t_i(R)=h,
\tag{3}
\]
because every arc set has total imbalance zero and \(a(V)=-h\).

Call a nonempty proper set \(X\) a **source shore** if \(\delta_D^-(X)=\varnothing\). Weak connectivity ensures its cut is nonempty. For such an \(X\),
\[
|\delta_D^+(X)|=b(X)=qa(X)+r(X),
\tag{4}
\]
and
\[
|F_i\cap\delta_D^+(X)|
=b_{F_i}(X)
=a(X)+t_i(X\cap R).
\tag{5}
\]

Reversing every arc preserves the directed-cut edge sets. It replaces each nonzero residue \(r_v\) by \(q-r_v\), and hence replaces \(h\) by \(m-h\). It is therefore enough to consider \(h=0,1,2\).

### Case \(h=0\)

Here \(R=\varnothing\). Apply the rounding lemma with no additional groups. Equation (5) gives
\[
|F_i\cap\delta_D^+(X)|
=\frac{|\delta_D^+(X)|}{q}\ge1.
\]
Thus every \(F_i\) is a dijoin.

### Case \(h=1\)

Again apply the lemma with no additional groups. Let \(X\) be a source shore and put \(T=X\cap R\).

If \(T\ne R\), then \(r(T)<q\). From (4) and the minimum-cut hypothesis, \(a(X)\ge1\). Equation (5) is therefore positive.

If \(T=R\), then \(r(T)=q\), so (4) gives \(a(X)\ge0\). Equation (3) now yields
\[
a(X)+t_i(T)=a(X)+1\ge1.
\]

### Case \(h=2\)

Here \(r(R)=2q\). If a source shore \(X\) has \(X\cap R\ne R\), then \(r(X)<2q\), and (4) implies
\[
a(X)\ge0.
\tag{6}
\]
The potentially troublesome cuts are precisely those with \(a(X)=0\): they require at least one rounded-up vertex on their source shore.

Define
\[
\mathcal T=
\left\{
T\subsetneq R:
\begin{array}{l}
\text{there is a source shore }X\text{ with}\\
X\cap R=T\text{ and }a(X)=0
\end{array}
\right\}.
\]
Every \(T\in\mathcal T\) satisfies
\[
r(T)\ge q,
\tag{7}
\]
by (4). In particular, \(T\ne\varnothing\).

Let \(\mathcal F\) consist of the inclusion-minimal members of \(\mathcal T\).

#### Claim: the sets \(R\setminus T\), for \(T\in\mathcal F\), are pairwise disjoint

Take distinct \(T_1,T_2\in\mathcal F\), with witnessing source shores \(X_1,X_2\). Suppose
\[
T_1\cup T_2\ne R.
\]
Since both \(r(T_j)\ge q\), while \(r(T_1\cup T_2)<2q\), we have
\[
r(T_1\cap T_2)>0.
\]
Thus \(X_1\cap X_2\) is nonempty, and \(X_1\cup X_2\) is proper.

Intersections and unions of source shores are source shores. Their residue sets are proper subsets of \(R\), so (6) applies:
\[
a(X_1\cap X_2)\ge0,\qquad
a(X_1\cup X_2)\ge0.
\]
But modularity of \(a\) gives
\[
a(X_1\cap X_2)+a(X_1\cup X_2)
=a(X_1)+a(X_2)=0.
\]
Consequently \(a(X_1\cap X_2)=0\), and
\[
T_1\cap T_2\in\mathcal T.
\]
This contradicts the minimality of \(T_1,T_2\). Therefore \(T_1\cup T_2=R\), proving the claim.

Now set
\[
\mathcal P=\{R\setminus T:T\in\mathcal F\}.
\]
These are pairwise disjoint. For \(P=R\setminus T\in\mathcal P\), (7) gives
\[
0<r(P)=2q-r(T)\le q.
\tag{8}
\]

Apply the rounding lemma with these groups. Its upper bound on \(b_{F_i}(P)\), together with (8), gives
\[
b_{F_i}(P)
\le
\left\lceil\frac{b(P)}q\right\rceil
=a(P)+1.
\]
Hence \(t_i(P)\le1\). Using \(t_i(R)=2\),
\[
t_i(T)=2-t_i(P)\ge1
\qquad(T\in\mathcal F).
\tag{9}
\]
Every member of \(\mathcal T\) contains a member of \(\mathcal F\). Since all \(t_i(v)\) are nonnegative, (9) holds for every \(T\in\mathcal T\).

It remains to check an arbitrary source shore \(X\), with \(T=X\cap R\).

- If \(T=R\), then (4) gives \(a(X)\ge-1\), and therefore
  \[
  a(X)+t_i(T)\ge-1+2=1.
  \]
- If \(T\ne R\) and \(a(X)\ge1\), equation (5) is positive.
- If \(T\ne R\) and \(a(X)=0\), then \(T\in\mathcal T\), so (9) makes equation (5) positive.

These exhaust the possibilities by (6). Thus every color class meets every directed cut. This proves the residue criterion and, by the SCC reduction, the theorem. \(\square\)

## 5. Constructivity and a capacitated extension

### Polynomial construction for the five-exception case

The proof gives a polynomial-time construction under the stated five-exception hypothesis.

Only the \(h=2\) case requires finding \(\mathcal T\). There are at most
\[
2^5-2=30
\]
nonempty proper subsets \(T\subset R\). For each, minimize the directed-cut size over source shores satisfying \(X\cap R=T\). Membership in \(\mathcal T\) is equivalent to that minimum being \(r(T)\).

This constrained minimization is an ordinary minimum-cut computation:

- give each original arc capacity \(1\);
- add its reverse with capacity \(M>|A(D)|\);
- force vertices of \(T\) onto the source side and vertices of \(R\setminus T\) onto the sink side using capacity-\(M\) arcs.

Cuts of value below \(M\) correspond exactly to admissible source shores. After identifying the minimal members of \(\mathcal T\), the rounding construction uses integral circulation computations.

No computational experiments are asserted here.

### Capacitated version

The same residue criterion also holds for nonnegative integer arc capacities \(c\), with
\[
b(v)=\sum_{e\in\delta^+(v)}c(e)-\sum_{e\in\delta^-(v)}c(e),
\]
and with every directed cut having capacity at least \(q\).

In the rounding lemma, start with value \(c(e)\), rather than \(1\), on each original arc. The resulting color flows are nonnegative integers. Their positive supports are dijoins, and each arc belongs to at most \(c(e)\) supports because its total color-flow value is \(c(e)\).

Thus the argument proves a restricted capacitated statement as well; it does **not** assert the false general weighted conjecture.

## 6. What remains unresolved

The argument does not cover the residue range
\[
h\ge3,\qquad m-h\ge3.
\]
For instance, with \(q=3\), six exceptional vertices having residues
\[
1,1,1,2,2,2
\]
give \(h=3\), outside the criterion.

The precise obstruction to extending this proof is that, for \(h\ge3\), a proper source shore can have \(a(X)=-1\) while its directed cut still has size at least \(q\). The nonnegativity used in the uncrossing claim then fails. No replacement for that step is established here.

Finally, two cautions about the supplied catalog:

- The displayed bound \(\lfloor\tau/6\rfloor\) alone yields three dijoins at \(\tau\ge18\), not at \(\tau\ge3\). Any stronger assertion needs separate verification.
- The quoted Steiner summary concerns list coloring and excluded minors, not this dijoin-packing conjecture.

I have not independently verified the recent bibliography or whether the special case proved above is already known.