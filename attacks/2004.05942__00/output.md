```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The local-update conjecture remains unresolved, but each fixed instance reduces to cycle detection on exponentially many five-color forests, yielding an exact exhaustive substitute and a PSPACE upper bound for termination testing.",
  "would_publish": false,
  "caveats": "No monotone potential or actual cycling triangulation is found; the reductions assume the paper's update is memoryless and its coefficients are given exactly."
}
```

# 1. Formalization of the termination question

Fix an internally triangulated plane graph \(G\) whose outer face is a pentagon, together with the pentagon data and normalization used in the source paper. Let

\[
\mathcal W(G)
\]

be the finite set of five-color forests of \(G\). For \(W\in\mathcal W(G)\), write the corresponding normalized linear system as

\[
A_Wx=b_W.
\]

The discussion below assumes, as in the algorithm, that solving this system gives a canonical vector \(x(W)\); in particular, after normalization the system is either nonsingular or the paper specifies a deterministic choice of solution.

Define the terminal set

\[
\mathcal T(G)=\{W\in\mathcal W(G):x(W)\geq 0
\text{ coordinatewise}\}.
\]

For \(W\notin\mathcal T(G)\), each negative coordinate to which the paper's local rule applies produces a new five-color forest. Thus there is a directed transition relation

\[
W\longrightarrow W'.
\]

If the paper fixes a tie-breaking rule, this relation is a partial function. If it says merely to choose a negative coordinate, it is genuinely nondeterministic. These two interpretations of “always terminates” are different.

The conjecture is that the trajectory from the prescribed initial forest eventually reaches \(\mathcal T(G)\).

# 2. Exact finite-state reduction

## Proposition 2.1

Let \(N(G)=|\mathcal W(G)|\).

1. For a deterministic memoryless update rule, either a terminal forest is reached within at most \(N(G)\) transitions, or the execution is eventually periodic.
2. If all legal choices are allowed, every execution reaches a terminal forest if and only if:
   - every reachable nonterminal state has an outgoing transition, and
   - the directed graph induced by the reachable nonterminal states is acyclic.
3. There exists a successful execution if and only if some terminal forest is reachable.

### Proof

For the deterministic statement, if no terminal state occurs among the first \(N(G)+1\) visited forests, two of them coincide. Because both the linear system and the tie-breaking rule depend only on the current forest, the subsequent trajectories also coincide. The execution is therefore periodic and never reaches a terminal state.

For the nondeterministic statement, a reachable directed cycle disjoint from the terminal set can be traversed indefinitely. Conversely, every infinite path in a finite directed graph repeats a vertex and therefore contains a directed cycle. If there are no nonterminal dead ends, every maximal path in the resulting finite acyclic graph ends in the terminal set. The last assertion is ordinary directed reachability. ∎

Thus a counterexample to deterministic termination always has a finite certificate: a repeated five-color forest together with the intervening legal updates. For adversarial nondeterminism, a reachable directed cycle is the corresponding certificate.

If choices are randomized with every legal transition having positive probability, the appropriate condition is weaker: almost-sure termination holds precisely when there is no reachable closed strongly connected component disjoint from \(\mathcal T(G)\). Merely having directed cycles would not disprove almost-sure termination.

# 3. Exponential bound from the \(\alpha\)-orientation correspondence

The source gives a bijection between five-color forests and certain \(\alpha\)-orientations of an auxiliary graph \(H_G\). Let

\[
M(G)=|E(H_G)|.
\]

An orientation is encoded by one bit per edge, so immediately

\[
N(G)\leq 2^{M(G)}.
\]

The auxiliary construction is local and of linear size in the plane graph, so in the source setting \(M(G)=O(|V(G)|)\). Consequently,

\[
N(G)=2^{O(|V(G)|)}.
\]

This gives the following unconditional finite bound, independent of any geometric monotonicity:

> If the deterministic local algorithm has not succeeded before repeating a forest, then it will never succeed; a repetition must occur within \(2^{M(G)}+1\) visited forests.

This does not prove that repetition is impossible.

## Exact fixed-instance termination test

Assume the pentagon data are rational or real algebraic numbers given exactly. This includes the usual fixed regular-pentagon setting, whose coefficients lie in a fixed finite algebraic extension of \(\mathbb Q\).

For a fixed \(G\), one can:

1. enumerate all \(2^{M(G)}\) orientations of \(H_G\);
2. retain those satisfying the prescribed \(\alpha\)-outdegree conditions;
3. decode them as five-color forests;
4. construct and solve \(A_Wx=b_W\) using exact algebraic arithmetic;
5. construct every legal negative-variable transition;
6. test the reachable subgraph for directed cycles or terminal reachability.

The systems have size \(O(|V(G)|)\), and determinant bit lengths remain polynomial in the input size. Hence each state and its outgoing transitions are computable in polynomial space.

## Proposition 3.1

For algebraic pentagon data and a memoryless update rule, each of the following fixed-input questions belongs to PSPACE:

- does the deterministic execution terminate?
- do all legal executions terminate?
- is there a legal execution reaching a nonnegative solution?

### Proof

A five-color forest has a polynomial-size encoding. For the nondeterministic version, the existence of a reachable nonterminal cycle can be checked by guessing a state reachable in at most \(N(G)\) steps and then a nonempty return path of length at most \(N(G)\), storing only the current state and binary step counters. Each transition is checked using exact linear algebra in polynomial space. Thus nontermination is in NPSPACE, which equals PSPACE; PSPACE is closed under complement. Reachability is similar. The deterministic case can also be tested by orbit iteration or cycle-finding in polynomial space. ∎

Explicit enumeration gives a \(2^{O(n)}\)-time, exponential-space test when the auxiliary graph has \(O(n)\) edges. No matching hardness result is established here.

If the pentagon coefficients are arbitrary unspecified real numbers, a Turing complexity statement is not meaningful without an oracle or an exact representation of those numbers.

# 4. A guaranteed exhaustive substitute for the local rule

There is a simple terminating algorithm which ignores the proposed negative-variable dynamics.

The representation-to-forest correspondence used in deriving the systems has the following consequence. Given a pentagon contact representation \(R\), read off its five-color forest \(W_R\), and let \(d_R\) be its vector of side distances. Then

\[
d_R\geq 0,\qquad A_{W_R}d_R=b_{W_R}.
\]

After applying the prescribed normalization, if the system has a unique solution then \(x(W_R)=d_R\). Zero coordinates account for allowable degeneracies.

The main theorem of the source paper, proved using the Monster Packing Theorem, supplies such a representation. Therefore, under the representation-to-forest correspondence established in the source,

\[
\mathcal T(G)\neq\varnothing.
\]

This yields the following algorithm.

```text
For every admissible α-orientation of H_G:
    decode it as a five-color forest W;
    construct A_W x = b_W;
    solve it exactly;
    if x is coordinatewise nonnegative:
        apply the paper's construction and return the representation.
```

If the normalized system is not unique, replace “solve it” by the linear feasibility test

\[
A_Wx=b_W,\qquad x\geq 0.
\]

This exhaustive algorithm tries at most \(2^{M(G)}\) systems and is guaranteed to find a representation. It is therefore a finite, generally exponential substitute for the conjectured local algorithm.

This does **not** provide the desired independent existence proof: its guarantee that some system succeeds uses the already-proved contact-representation theorem, whose proof invokes Monster Packing. It also says nothing about whether the negative-guided walk reaches a successful forest.

## A small rigorous special case

If \(G\) has exactly one five-color forest, then the conjectured algorithm succeeds immediately, assuming the normalized system is unique.

Indeed, the existence/correspondence argument above shows that at least one forest is terminal, and there is only one forest.

Through the \(\alpha\)-orientation bijection, uniqueness can sometimes be checked directly. For ordinary \(\alpha\)-orientations with some edges possibly fixed, an admissible orientation \(O\) is unique if and only if the subdigraph of nonfixed edges contains no directed cycle. One direction follows by reversing a directed cycle. Conversely, if \(O'\neq O\) is another \(\alpha\)-orientation, orient the symmetric difference as in \(O\). Equal outdegrees imply that this nonempty directed subgraph is balanced at every vertex, hence it contains a directed cycle.

# 5. Why the distributive lattice alone does not prove termination

The set of \(\alpha\)-orientations, and hence the set of five-color forests, carries a finite distributive lattice structure. Let \(\rho\) be its rank function.

A sufficient condition for termination would be

\[
W\longrightarrow W' \quad\Longrightarrow\quad
\rho(W')>\rho(W)
\]

for every nonterminal transition, or the same inequality with the direction reversed. In that case no state repeats, and termination occurs within the lattice height, provided every nonterminal state has a legal successor.

The existence of the lattice and of at least one terminal forest is not enough. For example, on the three-element chain

\[
W_0<W_1<W_2,
\]

declare \(W_2\) terminal and allow transitions \(W_0\to W_1\) and \(W_1\to W_0\). The state space remains a connected finite lattice containing a terminal state, but the prescribed walk from \(W_0\) cycles.

Thus the missing assertion must concern the signs produced by the linear systems, not merely connectivity or finiteness of the flip lattice.

## A more geometric potential criterion

Let \(p_W\) be the incidence vector of the \(\alpha\)-orientation corresponding to \(W\). If one could find a vector \(c\), depending only on the fixed input, such that

\[
c\cdot(p_{W'}-p_W)>0
\]

for every legal negative-variable update \(W\to W'\), termination would follow immediately.

A natural place to seek such a vector is the orientation polytope

\[
Q_\alpha=\operatorname{conv}\{p_W:W\in\mathcal W(G)\}.
\]

For adjacent vertices \(p_W,p_{W'}\), their normal cones meet in the hyperplane

\[
y\cdot(p_{W'}-p_W)=0.
\]

If the sign of the negative variable triggering \(W\to W'\) were exactly the assertion that a fixed vector \(y\) lies on the \(W'\)-side of this hyperplane, then

\[
y\cdot p_{W'}>y\cdot p_W
\]

would be a strict potential. This would prove termination.

I do not see, from the systems described in the supplied material, an identity equating the relevant Cramer-rule sign with such a fixed normal-fan sign. Establishing that identity, or showing that the cones determined by the systems form a polytopal fan, appears to be a concrete route to a proof rather than a consequence of the known lattice structure.

# 6. Exact computational counterexample search

Assume \(A_W\) is nonsingular. For coordinate \(j\), Cramer's rule gives

\[
x_j(W)=
\frac{\det A_W^{(j)}}{\det A_W},
\]

where \(A_W^{(j)}\) is obtained by replacing column \(j\) by \(b_W\). Thus

\[
x_j(W)<0
\quad\Longleftrightarrow\quad
\det A_W^{(j)}\,\det A_W<0.
\]

A completely checkable cycle certificate consists of

\[
W_0,j_0,W_1,j_1,\ldots,W_{k-1},j_{k-1},W_k=W_0
\]

such that, for each \(i\),

1. \(W_i\) is a valid five-color forest;
2. \(x_{j_i}(W_i)<0\), verified by exact determinant signs;
3. the source's local rule applied at \(j_i\) permits \(W_i\to W_{i+1}\);
4. for a deterministic rule, \(j_i\) is exactly the coordinate selected by its tie-breaking rule.

For small graphs, a reliable computation should therefore use exact rational/algebraic arithmetic, enumerate the \(\alpha\)-orientations, construct the full transition digraph, and compute reachable strongly connected components. Floating-point signs are not adequate near zero.

I have not carried out this computation and therefore report no small-case verification.

# 7. Remaining gap

The original conjecture is neither proved nor disproved here. The precise unresolved point is:

\[
\text{Can the sign-directed transition graph contain a reachable
nonterminal directed cycle?}
\]

Finiteness, lattice connectivity, and the known existence of a successful forest do not rule such a cycle out. A proof requires a strict potential or an equivalent structural sign theorem for the actual matrices. A disproof requires an explicit triangulation and an exact legal cycle of forests. Neither is obtained above.