```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The intended fair-splitting conjecture is covered by Alishahi–Meunier's theorem, whereas the displayed integer-budget formulation is inequivalent and false.",
  "would_publish": false,
  "caveats": "Odd-sized parts require distinguishing half-integer deficits from their integer roundings; the affirmative result does not prove the literal wording."
}
```

## 1. Precise resolution

Two mathematically different assertions occur in the question:

- **The displayed statement, with integer \(b_i\), is false.** The supplied \(P_7\) counterexample is correct, as verified below.
- **The fair-splitting result associated with the intended conjecture is true and already known.** The relevant follow-up is Alishahi–Meunier, *Fair splitting of colored paths*, arXiv:1704.02921, listed in the question.

The `already_resolved` verdict refers to the latter research problem. It does **not** mean that the displayed integer formulation has an affirmative proof.

To make the resolution independent of the previous referee’s mathematical assertions, I give a complete proof of the relevant splitting theorem, followed by its precise consequences. I retain the earlier counterexample as a correction to the wording, not as a new disproof of the known fair-splitting theorem.

## 2. The fair-splitting theorem

**Theorem.** Let \(P_n\) have vertices \(1,\ldots,n\) in path order, partitioned into nonempty sets \(V_1,\ldots,V_m\). Write \(n_i=|V_i|\). There are disjoint independent sets \(S_1,S_2\) such that:

1. exactly one vertex of each \(V_i\) lies outside \(S_1\cup S_2\);
2. for each \(a\in\{1,2\}\) and each \(i\),
   \[
   |S_a\cap V_i|\in
   \left\{
   \left\lfloor\frac{n_i-1}{2}\right\rfloor,
   \left\lceil\frac{n_i-1}{2}\right\rceil
   \right\};
   \]
3. \(\bigl||S_1|-|S_2|\bigr|\le 1\).

In fact, the vertices of \(S_1\cup S_2\), read in path order, can be made to alternate between \(S_1\) and \(S_2\).

### Consequence: simultaneous bounds for actual deficits

Choose the larger of \(S_1,S_2\), and call it \(S\). Then
\[
|S|\ge \frac{n-m}{2}.
\]
Define the actual deficits
\[
b_i=\frac{n_i}{2}-|S\cap V_i|.
\]
The theorem gives
\[
b_i\in
\begin{cases}
\{0,1\},&n_i\text{ even},\\[2mm]
\{\tfrac12\},&n_i\text{ odd}.
\end{cases}
\]
Consequently,
\[
b_i\le1
\qquad\text{and}\qquad
\sum_{i=1}^m b_i
=\frac n2-|S|
\le\frac m2.
\]

Thus the simultaneous cap and global-budget requirements hold with **real, indeed half-integral, deficits**. Moreover, when all parts have even size, this proves the literal integer-\(b_i\) statement as well.

The theorem also implies the strict-inequality formulation described in the supplied referee report. Both sets satisfy
\[
|S_a\cap V_i|\ge\frac{n_i}{2}-1.
\]
For every \(i\), at least one of these two inequalities is strict, since
\[
|S_1\cap V_i|+|S_2\cap V_i|=n_i-1>n_i-2.
\]
Hence one of \(S_1,S_2\) has strict inequality on at least \(m/2\) classes. These are direct consequences of the splitting theorem; no equivalence between the different formulations is being assumed.

## 3. Proof of the splitting theorem

We use the standard octahedral Tucker lemma.

### Octahedral Tucker lemma

For nonzero vectors \(x,y\in\{-1,0,1\}^n\), write \(x\preceq y\) if every nonzero coordinate of \(x\) agrees with the corresponding coordinate of \(y\).

If
\[
\lambda:\{-1,0,1\}^n\setminus\{0\}
\longrightarrow \{\pm1,\ldots,\pm(n-1)\}
\]
satisfies \(\lambda(-x)=-\lambda(x)\), then there exist \(x\preceq y\) with
\[
\lambda(x)=-\lambda(y).
\]

For completeness, nonzero sign vectors index the nonempty faces of the \(n\)-dimensional crosspolytope, and chains give its barycentric subdivision. If there were no complementary comparable pair, mapping a vertex \(x\) to
\(\operatorname{sgn}(\lambda(x))e_{|\lambda(x)|}\) would extend to an antipodal map
\[
S^{n-1}\longrightarrow S^{n-2}.
\]
Such a map is excluded by Borsuk–Ulam.

### Admissible sign vectors

Put
\[
d=n-m,\qquad h_i=\left\lfloor\frac{n_i}{2}\right\rfloor.
\]
If \(d=0\), every class is a singleton and \(S_1=S_2=\varnothing\) proves the theorem. Assume henceforth that \(d\ge1\).

For \(x\in\{-1,0,1\}^n\), define
\[
p_i(x)=|\{v\in V_i:x_v=1\}|,\qquad
q_i(x)=|\{v\in V_i:x_v=-1\}|.
\]
Call \(x\) **admissible** if, for every \(i\),
\[
p_i(x)\le h_i,\qquad
q_i(x)\le h_i,\qquad
p_i(x)+q_i(x)\le n_i-1. \tag{1}
\]
Every admissible vector therefore has at most
\[
\sum_i(n_i-1)=d
\]
nonzero coordinates.

Let \(\operatorname{alt}(x)\) be the maximum length of an alternating subsequence of the nonzero signs of \(x\), in coordinate order. For a nonzero vector, let \(\varepsilon(x)\) denote its first nonzero sign.

We will prove that there is an admissible \(x\) with
\[
\operatorname{alt}(x)\ge d. \tag{2}
\]

### Signing a violated class

Say that class \(i\) is **bad for \(x\)** if one of its conditions in (1) fails. Assign a sign \(\sigma_i(x)\) as follows:

- if \(p_i(x)>h_i\), set \(\sigma_i(x)=1\);
- if \(q_i(x)>h_i\), set \(\sigma_i(x)=-1\);
- otherwise, badness means that every vertex of \(V_i\) is nonzero. Necessarily \(n_i\) is even and
  \[
  p_i(x)=q_i(x)=n_i/2.
  \]
  Set \(\sigma_i(x)\) equal to the sign at the smallest vertex of \(V_i\).

The first two cases cannot occur simultaneously, because
\[
2(h_i+1)>n_i.
\]

This rule has two essential properties:

1. Negating \(x\) preserves badness and reverses \(\sigma_i(x)\).
2. If \(x\preceq y\) and \(i\) is bad for \(x\), then it remains bad for \(y\), with
   \[
   \sigma_i(y)=\sigma_i(x). \tag{3}
   \]

For the second property, a strict majority cannot disappear upon extending a sign vector. In the remaining case, all coordinates in \(V_i\) are already specified, so an extension cannot change its restriction to \(V_i\).

### Tucker labeling

Suppose, for a contradiction, that (2) fails. Define a labeling of all nonzero sign vectors.

If \(x\) is admissible, set
\[
\lambda(x)=\varepsilon(x)\operatorname{alt}(x).
\]
By our supposition, these labels have absolute values in \(\{1,\ldots,d-1\}\).

If \(x\) is not admissible, let \(i(x)\) be its smallest bad class, and set
\[
\lambda(x)=\sigma_{i(x)}(x)\bigl(d-1+i(x)\bigr).
\]
These labels have absolute values in
\[
\{d,\ldots,d+m-1\}=\{d,\ldots,n-1\}.
\]

The labeling is antipodal. We show it has no complementary comparable pair.

- **One vector admissible, the other inadmissible:** their label magnitudes lie in disjoint ranges.
- **Both inadmissible:** equal label magnitudes mean that the selected bad class is the same. Equation (3) then rules out opposite signs.
- **Both admissible:** if \(x\preceq y\) and their label magnitudes agree, then
  \[
  \operatorname{alt}(x)=\operatorname{alt}(y).
  \]
  Their first nonzero signs must agree. Indeed, if the first sign of \(y\) were opposite to the first sign of \(x\), it would occur earlier, and could be prepended to a longest alternating subsequence of \(x\) starting at its first nonzero coordinate. This would give
  \(\operatorname{alt}(y)\ge\operatorname{alt}(x)+1\), a contradiction.

This contradicts the octahedral Tucker lemma, establishing (2).

### Recovering the independent sets

For the admissible vector supplied by (2),
\[
d\le\operatorname{alt}(x)
\le|\operatorname{supp}(x)|
\le d.
\]
Thus all three quantities equal \(d\), and the entire nonzero sign sequence alternates.

Set
\[
S_1=\{v:x_v=1\},\qquad S_2=\{v:x_v=-1\}.
\]
They are independent: two adjacent vertices belonging to the same set would be consecutive equal signs in the nonzero sign sequence. Alternation also gives
\[
\bigl||S_1|-|S_2|\bigr|\le1.
\]

Since
\[
p_i(x)+q_i(x)\le n_i-1
\quad\text{and}\quad
\sum_i(p_i(x)+q_i(x))=\sum_i(n_i-1),
\]
equality holds for every class. Exactly one vertex of each class is omitted.

Finally:

- if \(n_i=2k\), the two counts sum to \(2k-1\) and are both at most \(k\), so they are \(k-1,k\);
- if \(n_i=2k+1\), they sum to \(2k\) and are both at most \(k\), so they are \(k,k\).

This proves the theorem. \(\square\)

## 4. Why the literal integer formulation is false

The rounding discrepancy is exact. For a fixed independent set \(S\), the smallest permissible integer \(b_i\) is
\[
b_i^{\min}
=\left\lceil\frac{n_i}{2}\right\rceil-|S\cap V_i|.
\]
If \(o\) classes have odd size, then
\[
\sum_i b_i^{\min}
=\frac{n+o}{2}-|S|,
\]
whereas the sum of the actual, possibly half-integral deficits is
\[
\frac n2-|S|.
\]
Integer rounding therefore adds \(o/2\) to the budget.

### Explicit obstruction

Take
\[
P_7=1-2-3-4-5-6-7
\]
with
\[
V_1=\{2,4,6\},\qquad
V_2=\{1\},\qquad
V_3=\{3,5,7\}.
\]

If integer \(b_i\) satisfy the displayed inequalities, then
\[
\sum_i b_i\ge (2+1+2)-|S|=5-|S|.
\]
But their integer sum must satisfy
\[
\sum_i b_i\le\frac32,
\]
hence \(\sum_i b_i\le1\). Thus \(|S|\ge4\).

The unique independent set of size \(4\) in \(P_7\) is
\[
\{1,3,5,7\}.
\]
Indeed, four selected vertices \(x_1<x_2<x_3<x_4\) satisfy
\[
x_4\ge x_1+6\ge7,
\]
forcing the positions \(1,3,5,7\). Larger independent sets are impossible.

This set misses \(V_1\), contradicting
\[
|S\cap V_1|\ge\frac32-b_1\ge\frac12.
\]
So the literal integer statement is false.

There is no contradiction with fair splitting: for example,
\[
S_1=\{2,5\},\qquad S_2=\{3,6\}
\]
satisfy the splitting theorem, omitting vertices \(1,4,7\). Either set has actual deficit \(1/2\) in every class.

## 5. Status and gaps

The mathematical conclusions above require no computation and have no unresolved case; the topological input is the standard Tucker/Borsuk–Ulam theorem.

The catalog should distinguish the **known affirmative fair-splitting result** from the **false literal integer-budget formula**. Neither should be presented as the same still-open assertion. No new research result is claimed here.