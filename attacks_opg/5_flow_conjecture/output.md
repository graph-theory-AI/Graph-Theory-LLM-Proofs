```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A two-matching construction gives a rigorous oddness/connectivity bound and an exact polynomial-time search within this construction when a prescribed 2-factor has four odd cycles.",
  "would_publish": false,
  "caveats": "The conjecture remains unresolved here; no novelty is claimed, and the polynomial-time search covers only a restricted family of flows."
}
```

## 1. Scope and results

A **nowhere-zero integer \(5\)-flow** consists of an orientation and values in \(\{1,2,3,4\}\) on the oriented edges, with equal total incoming and outgoing value at every vertex.

I do not prove that every bridgeless graph has such a flow. The partial results below concern finite, connected, loopless cubic graphs; parallel edges are allowed.

The main construction gives:

**Theorem 1.** Let \(G\) be a bridgeless cubic graph with a specified \(2\)-factor \(F\) having \(2t\) odd cycles.

- If \(t=0\), then \(G\) has a nowhere-zero \(4\)-flow.
- If \(t\geq 1\), and every edge cut separating two whole odd cycles of \(F\) has size at least \(5t-3\), then \(G\) has a nowhere-zero \(5\)-flow.

Here “separating two whole odd cycles” means that one odd cycle is entirely on each side of the cut.

Consequently:

- A bridgeless cubic graph having a \(2\)-factor with at most two odd cycles has a nowhere-zero \(5\)-flow.
- A cyclically \((5t-3)\)-edge-connected cubic graph having a \(2\)-factor with \(2t\) odd cycles has a nowhere-zero \(5\)-flow.

For four odd cycles, this gives cyclic edge-connectivity \(7\), weaker than the threshold \(6\) reported in the supplied literature review. Thus this bound is not claimed as a literature advance.

The additional algorithmic result is:

**Theorem 2.** Suppose the specified \(2\)-factor has four odd cycles. Fix the auxiliary matching used in the construction below. One can determine in polynomial time whether *any* of the resulting component-wise bisections yields a nowhere-zero \(5\)-flow. The search reduces to two instances of \(2\)-SAT, followed, if successful, by an integral maximum-flow computation.

Crucially, failure of this restricted search would not show that \(G\) lacks a \(5\)-flow.

## 2. A cut criterion, with an integral construction

Write
\[
M=E(G)\setminus E(F);
\]
thus \(M\) is a perfect matching.

Suppose \(V(G)=A\mathbin{\dot\cup}B\) is a bisection in which every edge of \(M\) joins \(A\) to \(B\). For \(S\subseteq V(G)\), set
\[
d(S)=|S\cap A|-|S\cap B|,
\qquad
c(S)=|\delta_G(S)|.
\]

The relevant condition is
\[
5|d(S)|\leq 3c(S)
\quad\text{for every }S\subseteq V(G).
\tag{1}
\]

Here is a self-contained proof that (1) supplies an integer \(5\)-flow.

Orient each cycle of \(F\) cyclically, and orient every edge of \(M\) from \(A\) to \(B\). The resulting orientation has
\[
d^+(v)-d^-(v)=
\begin{cases}
1,&v\in A,\\
-1,&v\in B.
\end{cases}
\]
If \(p(S)\) and \(q(S)\) count the edges directed out of and into \(S\), respectively, then
\[
p(S)-q(S)=d(S),\qquad p(S)+q(S)=c(S).
\]
Consequently, (1) is equivalent to
\[
p(S)\leq 4q(S),\qquad q(S)\leq 4p(S)
\quad\text{for every }S.
\tag{2}
\]

Start with value \(1\) on every oriented edge. To correct its vertex imbalances, construct a network with:

- capacity \(3\) on each oriented edge of \(G\);
- an arc of capacity \(1\) from a new source to each vertex of \(B\);
- an arc of capacity \(1\) from each vertex of \(A\) to a new sink.

A source–sink cut whose graph vertices on the source side are \(S\) has capacity
\[
|B\setminus S|+3p(S)+|A\cap S|
 =|B|+3p(S)+d(S)
 =|B|+4p(S)-q(S).
\]
By (2), this is at least \(|B|\). The maximum-flow/minimum-cut theorem and integrality therefore give an integral flow \(x\) of value \(|B|\).

On graph edges, \(0\leq x(e)\leq 3\). All source and sink arcs are saturated, so
\[
f(e)=1+x(e)
\]
satisfies conservation at every graph vertex and belongs to \(\{1,2,3,4\}\).

Conversely, a flow with values in \([1,4]\) in this orientation necessarily satisfies (2), by summing flow conservation across a cut. Thus (1) is an exact criterion for the orientation just constructed.

## 3. The two-matchings construction

Choose a matching \(N\subseteq E(F)\) as follows:

- on each even cycle of \(F\), take an alternating perfect matching;
- on each odd cycle, take a matching missing exactly one vertex.

Let \(Z\) be the set of unmatched vertices. Then \(|Z|=2t\), with exactly one vertex of \(Z\) on each odd cycle of \(F\).

The graph
\[
H=(V(G),M\cup N)
\]
has degree \(2\) outside \(Z\) and degree \(1\) at \(Z\). Its components are:

- even alternating cycles;
- \(t\) alternating paths, each starting and ending with an edge of \(M\).

Each such path has odd length. Hence every component of \(H\) is bipartite with equally sized colour classes.

Independently choose either bipartition of each component. This gives a bisection \(A,B\) of \(V(G)\), with both \(M\) and \(N\) joining opposite colours. Moreover, each path has one endpoint of each colour, so
\[
|Z\cap A|=|Z\cap B|=t.
\tag{3}
\]

Call these the **canonical bisections** associated with the fixed \(M,N\).

For an edge set \(X\), put
\[
c_X(S)=|\delta_G(S)\cap X|,
\]
and define the defect imbalance
\[
z(S)=|Z\cap A\cap S|-|Z\cap B\cap S|.
\]

Counting matching edges crossing the cut gives
\[
|d(S)|\leq c_M(S),
\tag{4}
\]
and
\[
|d(S)-z(S)|\leq c_N(S).
\tag{5}
\]
Indeed, internal matching edges pair one vertex of each colour, and only crossing matching edges contribute to the imbalance.

Since \(|z(S)|\leq t\), whenever \(d(S)\geq0\),
\[
c(S)\geq c_M(S)+c_N(S)
      \geq 2d(S)-z(S)
      \geq 2d(S)-t.
\tag{6}
\]

This elementary inequality is the starting point.

## 4. Every obstruction is small and separates odd cycles

Suppose a canonical bisection violates (1). Replacing \(S\) by its complement if necessary, write
\[
d=d(S)>0,\qquad c=c(S),\qquad 5d>3c.
\]

Because \(G\) is cubic,
\[
c\equiv |S|\equiv d\pmod 2.
\]
By (4), \(c\geq d\). Therefore
\[
j=\frac{c-d}{2}
\]
is a nonnegative integer.

The violating inequality becomes
\[
5d>3(d+2j),
\]
so
\[
d\geq 3j+1.
\tag{7}
\]
On the other hand, (6) gives
\[
d\leq 2j+t.
\tag{8}
\]
Combining these,
\[
j\leq t-1.
\]
In particular,
\[
d\leq 3t-2,\qquad
c=d+2j\leq 5t-4.
\tag{9}
\]

There is also a structural conclusion. Before replacing \(z(S)\) by \(t\), inequality (6) gives
\[
z(S)\geq d-2j\geq j+1.
\tag{10}
\]
Meanwhile, (4) implies
\[
c_{E(F)}(S)=c-c_M(S)\leq c-d=2j.
\tag{11}
\]

Every cycle of \(F\) having vertices on both sides of the cut contributes at least two edges to \(\delta_G(S)\). Thus at most \(j\) cycles of \(F\) are partially cut.

By (10), at least \(j+1\) vertices of \(Z\cap A\) lie in \(S\). They belong to distinct odd cycles of \(F\). Since at most \(j\) of those cycles can be partially cut, at least one odd cycle of \(F\) lies wholly in \(S\).

By (3), the defect imbalance of the complement is \(-z(S)\). The same argument shows that an odd cycle of \(F\) lies wholly in \(V(G)\setminus S\).

We have proved the following obstruction statement:

> **Every cut violating (1) has size at most \(5t-4\) and separates two whole odd cycles of \(F\).**

This proves Theorem 1 for \(t\geq1\).

If \(t=0\), then \(z(S)=0\), and (4)–(5) give
\[
c(S)\geq 2|d(S)|.
\]
The construction in Section 2, with capacity \(2\) instead of \(3\) on graph arcs, produces values in \(\{1,2,3\}\), proving the \(4\)-flow assertion.

For \(t=1\), an obstruction would have \(c\leq1\), impossible in a bridgeless graph.

The hypothesis of Theorem 1 is itself checkable by minimum-cut computations: for each pair of odd cycles of \(F\), contract one to a source and the other to a sink, and compute the minimum cut separating them.

## 5. Four odd cycles: the exact obstruction

Now let \(t=2\). There are precisely two path components of \(H\); call them \(P_1,P_2\).

Equations (7)–(8) leave only:

- \(j=0\), with \(d\in\{1,2\}\);
- \(j=1\), with \(d=4\).

Since \(G\) is bridgeless, \(d=c=1\) is excluded. Thus every violating cut has
\[
(c,d)=(2,2)\quad\text{or}\quad(c,d)=(6,4).
\tag{12}
\]

Put
\[
R=E(F)\setminus N.
\]
In both cases of (12), \(c=2d-2\). Equality throughout
\[
c\geq c_M+c_N\geq 2d-z(S)\geq 2d-2
\]
forces
\[
z(S)=2,\qquad
c_M=d,\qquad
c_N=d-2,\qquad
c_R=0.
\tag{13}
\]

Equality in the signed matching counts also forces every endpoint in \(S\) of a crossing \(M\)- or \(N\)-edge to belong to \(A\).

Consequently, a canonical bisection violates (1) exactly when some cut has one of these profiles and all its endpoints on one side have the same colour:
\[
\begin{array}{c|ccc|c}
|\delta_G(S)| & c_M(S)&c_N(S)&c_R(S)&|d(S)|\\ \hline
2&2&0&0&2\\
6&4&2&0&4
\end{array}
\tag{14}
\]

The converse is immediate from the matching count: a monochromatic \(S\)-side boundary gives \(|d(S)|=c_M(S)\), which violates (1) in either row.

Furthermore, (13) implies that \(S\) contains exactly one endpoint of each of \(P_1,P_2\); these two endpoints have the same colour.

If \(G\) is \(3\)-edge-connected, only the second row is possible. By Section 4, such a cut is cyclic and separates whole odd cycles of \(F\). Thus, for this construction:

> In a \(3\)-edge-connected cubic graph with a specified \(2\)-factor having four odd cycles, the only possible failures are precisely the indicated cyclic six-edge cuts.

For example, it suffices that every cyclic six-edge cut meet \(R\).

## 6. Searching all canonical bisections by \(2\)-SAT

There may be many cycle components of \(H\), so naïvely there are exponentially many canonical bisections. Nevertheless, at \(t=2\) the search is polynomial.

Choose a reference bipartition on every component of \(H\). Each component has one Boolean variable indicating whether its colours are flipped.

A global colour swap does not affect (1), so fix the colouring of \(P_1\). There are only two choices for the colouring of \(P_2\). Consider each choice separately.

### Relevant cuts

List cuts having one of the two profiles in (14). Discard a cut unless it separates the endpoints of both \(P_1\) and \(P_2\): Section 5 proves that a discarded cut cannot violate (1) under any canonical bisection.

Each path contributes at least one boundary edge. Every cycle component of \(H\) meeting the cut contributes at least two boundary edges. Therefore:

- for a relevant two-edge cut, no cycle component of \(H\) meets the cut;
- for a relevant six-edge cut, at most two cycle components of \(H\) meet the cut.

This is what makes \(2\)-SAT possible.

### The clause for a cut

For a relevant cut \(\delta_G(S)\), examine the \(S\)-side boundary endpoints lying on \(P_1\) or \(P_2\). Their colours are already fixed.

- If both colours occur, the boundary cannot be monochromatic, so no constraint is needed.
- Otherwise, all these fixed endpoints have some common colour \(a\).

In the latter case, avoiding a violation means that at least one remaining boundary endpoint has colour different from \(a\).

Those remaining endpoints lie on at most two cycle components of \(H\). Their colours are Boolean literals in the corresponding flip variables.

If a cycle supplies boundary endpoints of both reference colours, the cut is automatically safe under either flip. Otherwise it contributes one literal. Hence the requirement is a clause with at most two literals:
\[
\ell_1\lor\ell_2,
\]
possibly a unit clause or an empty, unsatisfiable clause.

Taking all relevant cuts gives a \(2\)-CNF formula.

If either choice for \(P_2\) gives a satisfiable formula, its assignment produces a canonical bisection satisfying (1) for every cut. Section 2 then constructs an integral nowhere-zero \(5\)-flow.

If both formulas are unsatisfiable, no canonical bisection for this fixed pair \(M,N\) satisfies (1).

### Polynomial bound

Let \(n=|V(G)|\) and \(m=|E(G)|\).

All cuts of size \(2\) or \(6\) can be enumerated in
\[
O\!\left(m^6(n+m)\right)
\]
time by the following fully specified procedure:

1. Choose an edge set \(X\) of size \(2\) or \(6\).
2. Compute the components of \(G-X\).
3. Inspect their unions \(S\), retaining those for which \(\delta_G(S)=X\).

Deleting at most six edges from a connected graph creates at most seven components, so step 3 examines at most \(2^7\) unions. Every cut of the required size is found.

The resulting formulas have polynomially many clauses. Standard implication-graph \(2\)-SAT algorithms and the final integral maximum-flow computation are polynomial. This proves Theorem 2. No computational experiments are being asserted.

## 7. What remains unproved

The obstruction analysis does **not** finish Tutte’s conjecture.

1. A general bridgeless cubic graph need not come with a \(2\)-factor satisfying the odd-cycle separation bound of Theorem 1.
2. With four odd cycles, I have not proved that one of the two \(2\)-SAT formulas must always be satisfiable.
3. The auxiliary matching \(N\) is fixed in Theorem 2. Different choices may behave differently.
4. A general \(5\)-flow need not arise from a canonical bisection for the chosen \(M,N\). Thus failure of this search is not a counterexample.

The rigorous output is therefore a constructive special-case bound, an exact description of the cut obstructions at four odd cycles, and a polynomial-time search within that construction—not a proof or disproof of the full conjecture. I have not verified whether the precise \(2\)-SAT formulation is already in the literature, and I make no novelty claim.