```json
{
  "verdict": "no_progress",
  "confidence": "high",
  "one_line": "I could not settle termination; an explicit six-cycle shows that even strong algebraic and fan properties of the linear systems would not suffice without additional graph-specific structure.",
  "would_publish": false,
  "caveats": "The cycling system below is not realized by five-color forests and therefore is not a counterexample to the conjecture."
}
```

# 1. The question and the scope of this attack

The conjecture concerns the specific negative-variable updates in the pentagon representation algorithm: starting from an allowed five-color forest, must the algorithm eventually reach a forest whose normalized linear-system solution is coordinatewise nonnegative?

I obtain neither a proof nor a triangulation on which the algorithm cycles.

The finite-state observation in the previous attempt is correct under its stated memorylessness hypothesis: an infinite execution must eventually repeat a forest. But this detects what a counterexample would look like; it does not exclude one. I do not rely on the previous attempt’s unverified source-specific assumptions about the matrices or auxiliary graph.

I investigated a stronger potential-function approach: perhaps nonsingularity, sign-reversing local pivots, and geometric compatibility of the solution cones force termination. The rigorous result below shows that this approach needs a genuinely additional property. In particular, even a **complete simplicial fan**, together with strong monotonicity and unique-sink properties, does not suffice.

This is an obstruction to an abstract proof strategy, not a partial resolution for a class of triangulations.

# 2. An exact cycling model

Let
\[
\phi=\frac{1+\sqrt5}{2},\qquad
M=
\begin{pmatrix}
1&0&\phi\\
\phi&1&0\\
0&\phi&1
\end{pmatrix}.
\]
Consider
\[
w=Mz-\mathbf1.
\]

The states are the eight subsets \(B\subseteq\{1,2,3\}\). At state \(B\), impose
\[
w_i=0\quad(i\in B),\qquad z_i=0\quad(i\notin B),
\]
and solve the resulting linear system. Define the three basic values by
\[
u_i(B)=
\begin{cases}
z_i,&i\in B,\\
w_i,&i\notin B.
\end{cases}
\]

The local rule is:

> If \(u_i(B)<0\), permit the update \(B\longrightarrow B\triangle\{i\}\).

The algorithm stops when all three basic values are nonnegative.

Thus this model has the broad architecture relevant to the conjecture: a finite lattice of states, a canonical linear system at every state, and negative coordinates directing local changes. The use of \(\phi\) is an exact algebraic choice, not an assertion that these are pentagon contact equations.

## Proposition 2.1

This model has all of the following properties:

1. Every state has a unique linear-system solution.
2. Exactly one state is terminal.
3. Every permitted pivot changes the pivoted basic value from negative to positive.
4. Every face of the state cube has a unique sink.
5. Nevertheless, a deterministic, memoryless negative-coordinate selection rule can cycle.

### Proof

For a state \(B\), the variables \(z_B\) solve
\[
M_{BB}z_B=\mathbf1_B.
\]
All one-by-one and two-by-two principal minors of \(M\) are \(1\), while
\[
\det M=1+\phi^3>0.
\]
Thus every state is well defined and nonsingular.

Using \(\phi^2=\phi+1\), exact solution of the eight systems gives:

| State \(B\) | \(u_1(B)\) | \(u_2(B)\) | \(u_3(B)\) |
|---|---:|---:|---:|
| \(\varnothing\) | \(-1\) | \(-1\) | \(-1\) |
| \(\{1\}\) | \(1\) | \(\phi-1\) | \(-1\) |
| \(\{1,3\}\) | \(1-\phi\) | \(-2\) | \(1\) |
| \(\{3\}\) | \(\phi-1\) | \(-1\) | \(1\) |
| \(\{2,3\}\) | \(-2\) | \(1\) | \(1-\phi\) |
| \(\{2\}\) | \(-1\) | \(1\) | \(\phi-1\) |
| \(\{1,2\}\) | \(1\) | \(1-\phi\) | \(-2\) |
| \(\{1,2,3\}\) | \(2-\phi\) | \(2-\phi\) | \(2-\phi\) |

For example, at \(B=\{1,3\}\),
\[
z_3=1,\qquad z_1=1-\phi,
\]
and
\[
w_2=\phi(1-\phi)-1=-2.
\]

The unique terminal state is \(\{1,2,3\}\). Nevertheless, the table gives the legal cycle
\[
\begin{aligned}
\{1\}
&\xrightarrow{\,3\,}\{1,3\}
\xrightarrow{\,1\,}\{3\}
\xrightarrow{\,2\,}\{2,3\}\\
&\xrightarrow{\,3\,}\{2\}
\xrightarrow{\,1\,}\{1,2\}
\xrightarrow{\,2\,}\{1\}.
\end{aligned}
\]
The labels indicate the toggled coordinates. The triggering values alternate between
\[
-1\quad\text{and}\quad 1-\phi,
\]
so every step is strictly permitted.

Here is a deterministic memoryless selection rule producing this cycle:

- if a negative \(z_i\) is basic, pivot such a coordinate out;
- otherwise pivot a negative basic \(w_i\) in;
- resolve any remaining tie by the smallest index.

Starting at \(\varnothing\), this rule first reaches \(\{1\}\) and then follows the displayed cycle indefinitely.

The table also verifies that each cube edge is directed in exactly one direction, and that its pivoted value becomes positive at the destination. Hence there is no immediate reversal.

For completeness, the unique-sink assertion can be checked without invoking any general theorem about complementarity systems. The three square faces with one coordinate fixed absent have respective sinks
\[
\begin{array}{c|c}
\text{Coordinate fixed absent}&\text{Sink}\\ \hline
1&\{2\}\\
2&\{3\}\\
3&\{1\}.
\end{array}
\]
Each of the three square faces with one coordinate fixed present has sink \(\{1,2,3\}\). Each edge has one sink, and the whole cube has the unique sink \(\{1,2,3\}\). This covers every face. ∎

There is no degeneracy in the tested coordinates: every entry in the table is nonzero. Consequently the cycling sign pattern persists under sufficiently small perturbations of \(M\) and the right-hand side. It is not a floating-point or zero-length phenomenon.

# 3. Strong monotonicity does not prevent this cycle

The preceding matrix satisfies a substantially stronger condition than positivity of its principal minors.

## Proposition 3.1

There is a constant \(\mu>0\) such that
\[
x^{\mathsf T}Mx\geq \mu\|x\|^2
\qquad\text{for all }x\in\mathbb R^3.
\]

### Proof

Writing \(J\) for the all-ones matrix,
\[
\frac{M+M^{\mathsf T}}2
=
\left(1-\frac{\phi}{2}\right)I+\frac{\phi}{2}J.
\]
Therefore
\[
x^{\mathsf T}Mx
=
\left(1-\frac{\phi}{2}\right)\|x\|^2
+\frac{\phi}{2}\left(\sum_i x_i\right)^2.
\]
Since \(1<\phi<2\), one may take
\[
\mu=1-\frac{\phi}{2}>0.
\]
∎

Thus even a strongly monotone linear operator can produce a cycling negative-coordinate pivot walk. Strong monotonicity controls the underlying feasibility problem; it does not make every discrete pivot sequence monotone.

# 4. Even a complete solution fan is insufficient

The previous attempt suggested seeking a normal-fan interpretation. There is an important distinction here: proving that the solution cones form a complete fan would not, by itself, prove the needed normal-fan property.

The same example demonstrates this distinction explicitly.

Let \(m_i\) denote column \(i\) of \(M\), and define
\[
C_B=\operatorname{cone}\bigl(
\{-m_i:i\in B\}\cup\{e_i:i\notin B\}
\bigr).
\]
These are precisely the right-hand sides \(q\) for which the basis \(B\) gives a nonnegative solution to
\[
w=Mz+q.
\]

## Proposition 4.1

The cones \(C_B\), together with their faces, form a complete simplicial fan. This fan is not the normal fan of a convex polytope.

### Proof: completeness and the intersection property

First, for every \(q\in\mathbb R^3\), the complementarity conditions
\[
z\geq0,\qquad w=Mz+q\geq0,\qquad z_iw_i=0
\]
have a unique solution.

Here is a direct proof. Put
\[
\mu=1-\frac{\phi}{2},\qquad L=1+\phi.
\]
Since \(M=I+\phi P\), where \(P\) is a permutation matrix, \(\|M\|\leq L\). For
\[
\tau=\frac{\mu}{L^2},
\]
consider the map on the nonnegative orthant
\[
T_q(z)=\bigl(z-\tau(Mz+q)\bigr)_+,
\]
where positive part is taken coordinatewise.

Positive part is nonexpansive. Consequently, for \(h=z-z'\),
\[
\begin{aligned}
\|T_q(z)-T_q(z')\|^2
&\leq \|h-\tau Mh\|^2\\
&\leq
\left(1-2\tau\mu+\tau^2L^2\right)\|h\|^2\\
&=
\left(1-\frac{\mu^2}{L^2}\right)\|h\|^2.
\end{aligned}
\]
Thus \(T_q\) is a contraction of a complete metric space into itself. Its unique fixed point is exactly the unique complementary solution.

Every complementary solution belongs to at least one basis: include the positive coordinates of \(z\) in \(B\), exclude the positive coordinates of \(w\), and assign coordinates with \(z_i=w_i=0\) arbitrarily. Therefore
\[
\bigcup_B C_B=\mathbb R^3.
\]

Each \(C_B\) is simplicial because its generating matrix is nonsingular. If \(q\in C_B\cap C_D\), uniqueness of the complementary solution implies
\[
z_i=w_i=0\qquad(i\in B\triangle D).
\]
It follows that \(C_B\cap C_D\) is exactly the cone generated by their common rays, hence a face of both. This proves the fan assertion.

### Proof: failure of polytopality

Suppose a polytope had this normal fan. The cone
\[
C_\varnothing=\operatorname{cone}(e_1,e_2,e_3)
\]
would be the normal cone of a vertex. Translate that vertex to the origin. The corresponding three supporting inequalities are then
\[
x_i\leq0\qquad(i=1,2,3).
\]

The other facet normals are \(-m_1,-m_2,-m_3\), so write their inequalities as
\[
\begin{aligned}
-x_1-\phi x_2&\leq h_1,\\
-x_2-\phi x_3&\leq h_2,\\
-\phi x_1-x_3&\leq h_3.
\end{aligned}
\]
Here \(h_1,h_2,h_3>0\), because these facets do not contain the translated vertex.

The vertex with normal cone \(C_{\{1\}}\) must be
\[
(-h_1,0,0).
\]
Its feasibility gives
\[
\phi h_1\leq h_3.
\]
Similarly, the vertices with normal cones \(C_{\{2\}}\) and \(C_{\{3\}}\) give
\[
\phi h_2\leq h_1,\qquad
\phi h_3\leq h_2.
\]
Multiplication yields
\[
\phi^3 h_1h_2h_3\leq h_1h_2h_3,
\]
contradicting \(\phi>1\). ∎

For a complete fan, a negative basic coordinate means that the target right-hand side lies across the corresponding facet. Thus the six-cycle above is also a cycle of such facet-directed moves in a complete fan.

If the fan were a normal fan, the corresponding moves would strictly increase a fixed linear functional on the vertices of its polytope. The example shows exactly why obtaining a complete fan is weaker than obtaining that potential.

# 5. What this says—and does not say—about pentagons

The construction rules out the following general inference:

> A finite distributive lattice of nonsingular linear-system states, with negative-coordinate local updates and a unique feasible state, must have terminating update dynamics.

It remains false even after adding all of these conditions:

- the pivoted negative value becomes positive;
- every cube face has a unique sink;
- the underlying linear operator is strongly monotone;
- the solution cones form a complete simplicial fan;
- all relevant signs are strict.

Accordingly, a proof of the pentagon conjecture cannot rest on those properties alone. It must exploit further restrictions imposed by the actual contact equations and five-color-forest structure, or use a different termination argument.

The obstruction also gives a focused counterexample-search target: look for three commuting forest changes whose six middle states support the displayed cyclic sign pattern. But turning that target into a counterexample would require all of the following:

1. an explicit allowed plane triangulation;
2. actual five-color forests realizing the states;
3. exact solutions of the paper’s linear systems;
4. verification that each displayed move is permitted by its update rule;
5. compatibility with any prescribed tie-breaking;
6. reachability from the prescribed initial forest, if initialization is restricted.

**None of those graph-realization steps has been established here.** In particular, the occurrence of the golden ratio in this algebraic example is not evidence that it embeds in pentagon contact equations.

The remaining issue is therefore still the original one: can the specific sign-directed forest dynamics cycle? I have not excluded that possibility and have not produced a realizing graph.