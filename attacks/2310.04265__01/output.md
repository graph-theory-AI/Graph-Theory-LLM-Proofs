```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Polynomial boundedness is preserved for substitution expressions with bounded active ramification, including arbitrarily deep expressions having at most one nontransitive child at each nontransitive node.",
  "would_publish": false,
  "caveats": "There is no bound here on active ramification in terms of directed clique number; balanced cyclic substitutions remain unresolved."
}
```

# 1. Statement and notation

For a tournament \(T\) and an ordering \(\prec\) of \(V(T)\), let \(T^\prec\) be its backedge graph. Write

\[
\vec\omega(T)=\min_{\prec}\omega(T^\prec)
\]

and let \(\vec\chi(T)\) be the dichromatic number, namely the minimum number of transitive subtournaments partitioning \(V(T)\).

For a tournament \(S\) and nonempty tournaments \((H_v:v\in V(S))\), the substitution

\[
S(H_v:v\in V(S))
\]

is obtained by replacing each \(v\) by \(H_v\), with all arcs between \(H_u\) and \(H_v\) oriented as the arc \(uv\) of \(S\).

Suppose that \(\mathcal T\) has a nondecreasing binding function \(f\):

\[
\vec\chi(S)\le f(\vec\omega(S)) \qquad(S\in\mathcal T).
\]

There is no loss in taking \(f\ge1\) and nondecreasing, since a polynomial binding function can be replaced by a nondecreasing polynomial majorant.

I prove polynomial preservation for a substantial restricted family of substitution expressions.

---

# 2. Coloring lemmas for one substitution

Let

\[
T=S(H_v:v\in V(S)), \qquad d_v=\vec\chi(H_v), \qquad M=\max_v d_v.
\]

## Lemma 2.1: Crude product bound

\[
\vec\chi(T)\le \vec\chi(S)M.
\]

### Proof

Partition \(S\) into \(q=\vec\chi(S)\) transitive sets \(C_1,\dots,C_q\). For each \(v\), fix a partition of \(H_v\) into \(d_v\) transitive classes, padding with empty classes up to \(M\).

For every \(i\in[q]\) and \(j\in[M]\), take the union of the \(j\)-th classes in the modules \(H_v\) with \(v\in C_i\). This union is transitive because its quotient \(S[C_i]\) and all its constituent pieces are transitive. ∎

## Lemma 2.2: Transitive quotients cost nothing

If \(S\) is transitive, then

\[
\vec\chi(T)=\max_v\vec\chi(H_v).
\]

### Proof

The upper bound follows by aligning color classes across all modules in the transitive order of \(S\). The reverse inequality follows because every \(H_v\) is an induced subtournament of \(T\). ∎

The next lemma is the main useful observation.

## Lemma 2.3: One nontransitive child

Suppose that \(H_v\) is the only nontransitive child; thus \(H_x\) is transitive for every \(x\ne v\). Then

\[
\vec\chi(T)
 \le
\max\left\{
   \vec\chi(H_v),
   \vec\chi(S[N^+(v)])+\vec\chi(S[N^-(v)])
\right\}.
\]

Consequently,

\[
\vec\chi(T)\le \max\{\vec\chi(H_v),\,2\vec\chi(S)\}.
\]

### Proof

Put

\[
q^+=\vec\chi(S[N^+(v)]),\qquad
q^-=\vec\chi(S[N^-(v)]),\qquad q=q^++q^-.
\]

Partition \(N^+(v)\) and \(N^-(v)\) into altogether \(q\) transitive sets \(P_1,\dots,P_q\), with each \(P_i\) lying entirely on one side of \(v\). Then \(P_i\cup\{v\}\) is transitive: \(v\) is either a source or a sink in this subtournament.

Let \(A_1,\dots,A_d\) be a transitive coloring of \(H_v\), where \(d=\vec\chi(H_v)\). For each \(i\le q\), let

\[
U_i=\bigcup_{x\in P_i}V(H_x).
\]

Since \(P_i\) and all \(H_x\), \(x\ne v\), are transitive, \(U_i\) is transitive. Moreover, \(A_i\cup U_i\) is transitive whenever \(i\le d\), because its quotient is \(P_i\cup\{v\}\).

Thus use:

- \(A_i\cup U_i\) for \(i\le\min\{d,q\}\);
- \(A_i\) alone for \(q<i\le d\);
- \(U_i\) alone for \(d<i\le q\).

This gives \(\max\{d,q\}\) colors. Finally, restriction of a coloring of \(S\) to either \(N^+(v)\) or \(N^-(v)\) gives

\[
q^+,q^-\le\vec\chi(S),
\]

and hence \(q\le2\vec\chi(S)\). ∎

The important point is that an arbitrarily long chain of substitutions with just one nontransitive child need not multiply the binding function.

---

# 3. Active ramification of a substitution expression

Consider a fixed substitution expression over \(\mathcal T\). A child is called **active** if its represented tournament is nontransitive.

Call an internal node a **ramification node** if:

1. its quotient tournament \(S\) is nontransitive, and
2. it has at least two active children.

Define \(b(E)\), the active ramification depth of an expression \(E\), recursively:

- a leaf has \(b(E)=0\);
- if the quotient is transitive, \(b(E)\) is the maximum \(b\) of its active children;
- if the quotient is nontransitive with at most one active child, \(b(E)\) is \(0\) or the \(b\)-value of that child;
- if the quotient is nontransitive with at least two active children, then
  \[
  b(E)=1+\max\{b(E_v):H_v\text{ is active}\}.
  \]

Thus \(b(E)\) counts ramification nodes along a worst root-to-leaf active path. Ordinary substitution depth can be unbounded while \(b(E)=0\).

## Theorem 3.1: Bound by active ramification

Let \(E\) be a substitution expression over \(\mathcal T\), representing a tournament \(T\), and put

\[
w=\vec\omega(T),\qquad b=b(E).
\]

Then

\[
\boxed{\quad \vec\chi(T)\le 2f(w)^{\,b+1}.\quad}
\]

### Proof

Directed clique number is induced-subtournament monotone: if \(U\) is induced in \(T\), restrict an ordering witnessing \(\vec\omega(T)\). In particular, at every node of the expression, its quotient and all its children have directed clique number at most \(w\). Thus every quotient \(S\in\mathcal T\) satisfies

\[
\vec\chi(S)\le f(w).
\]

We induct on the size of the expression.

### Case 1: The quotient \(S\) is transitive

By Lemma 2.2,

\[
\vec\chi(T)=\max_v\vec\chi(H_v).
\]

No ramification is added at this node, and the result follows from induction.

### Case 2: \(S\) is nontransitive and no child is active

All \(H_v\) are transitive, so

\[
\vec\chi(T)=\vec\chi(S)\le f(w)\le2f(w)^{b+1}.
\]

### Case 3: \(S\) is nontransitive and exactly one child \(H_v\) is active

By Lemma 2.3,

\[
\vec\chi(T)\le
\max\{\vec\chi(H_v),\,2f(w)\}.
\]

This node does not increase \(b\). By induction,

\[
\vec\chi(H_v)\le2f(w)^{b+1},
\]

and the desired bound follows.

### Case 4: \(S\) is nontransitive and has at least two active children

This is a ramification node. Every active child has ramification depth at most \(b-1\), and therefore, by induction,

\[
\vec\chi(H_v)\le2f(w)^b.
\]

Transitive children have dichromatic number \(1\), so

\[
M=\max_v\vec\chi(H_v)\le2f(w)^b.
\]

Lemma 2.1 now gives

\[
\vec\chi(T)
 \le \vec\chi(S)M
 \le f(w)\cdot2f(w)^b
 =2f(w)^{b+1}.
\]

This covers every case. ∎

## Corollary 3.2

If

\[
f(w)\le C(w+1)^a
\]

and a family of tournaments in \(\mathcal T^{\mathrm{subst}}\) has substitution expressions with \(b(E)\le B\), where \(B\) is fixed, then that family is polynomially \(\vec\chi\)-bounded:

\[
\vec\chi(T)
 \le
2C^{B+1}(w+1)^{a(B+1)}.
\]

In particular, if every nontransitive node has at most one nontransitive child, then

\[
\vec\chi(T)\le2f(\vec\omega(T)),
\]

regardless of the ordinary substitution depth.

For a base class with bounded dichromatic number \(f\equiv q\), Theorem 3.1 also gives a polynomial bound whenever \(b(E)=O(\log w)\):

\[
\vec\chi(T)\le 2q^{b(E)+1}=w^{O(1)}.
\]

---

# 4. The balanced cyclic test family

The obstruction not covered by Theorem 3.1 is repeated cyclic ramification. The simplest test family already lies in

\[
\{TT_1,TT_2,\overrightarrow C_3\}^{\mathrm{subst}}.
\]

Let

\[
R_0=TT_1,\qquad
R_{n+1}=\overrightarrow C_3(R_n,R_n,R_n).
\]

Write

\[
d_n=\vec\chi(R_n),\qquad w_n=\vec\omega(R_n).
\]

## Proposition 4.1: Exact dichromatic recurrence

\[
d_0=1,\qquad
d_{n+1}=\left\lceil\frac{3d_n}{2}\right\rceil.
\]

Hence

\[
d_n=\Theta((3/2)^n).
\]

### Proof

A transitive set in \(R_{n+1}\) can meet at most two of the three top-level modules: meeting all three would contain a directed triangle. If a coloring uses \(k\) colors, the restrictions to each of the three modules use at least \(d_n\) nonempty colors. Thus there are at least \(3d_n\) module-color incidences, while each global color has at most two such incidences. Hence

\[
k\ge\left\lceil\frac{3d_n}{2}\right\rceil.
\]

Conversely, one can choose \(\lceil3d_n/2\rceil\) supports, each being an edge or a vertex of \(\overrightarrow C_3\), so that every quotient vertex occurs in \(d_n\) supports.

- If \(d_n=2r\), use \(r\) copies of each of the three two-vertex supports.
- If \(d_n=2r+1\), use \(r\) copies of each two-vertex support, one additional two-vertex support, and the remaining singleton.

Assign the \(d_n\) color classes in each module injectively to supports containing its quotient vertex. This gives the upper bound.

Finally,

\[
\frac32d_n\le d_{n+1}\le\frac32d_n+\frac12,
\]

which gives the stated asymptotic. ∎

## Proposition 4.2: Elementary bounds on \(w_n\)

\[
\boxed{\quad n+1\le w_n\le2^n.\quad}
\]

### Lower bound

More generally, if

\[
T=\overrightarrow C_3(A,B,C),
\]

then

\[
\vec\omega(T)\ge
\min\{\vec\omega(A),\vec\omega(B),\vec\omega(C)\}+1.
\]

Indeed, let \(q\) be the minimum on the right and fix any ordering of \(T\). In each module choose a backedge clique \(K_A,K_B,K_C\) of size \(q\). Orient the quotient as

\[
A\to B\to C\to A.
\]

If no \((q+1)\)-clique exists, then no vertex of \(B\) can occur before every vertex of \(K_A\), since it could then be adjoined to \(K_A\). Therefore

\[
\min K_A<\min K_B.
\]

Similarly,

\[
\min K_B<\min K_C<\min K_A,
\]

a contradiction. Thus \(w_{n+1}\ge w_n+1\), giving \(w_n\ge n+1\).

### Upper bound

Order the three top modules as consecutive blocks \(A,B,C\), where \(A\to B\to C\to A\), and recursively use the chosen block order inside each copy of \(R_n\). The quotient backedge graph has one edge, between \(A\) and \(C\). Consequently a backedge clique uses at most two child modules, and

\[
w_{n+1}\le2w_n.
\]

Since \(w_0=1\), this yields \(w_n\le2^n\). ∎

For reference, \(w_0=1,w_1=2,w_2=3\). For \(R_2\), the upper bound \(3\) is witnessed by ordering vertices \((i,j)\in\{0,1,2\}^2\) as

\[
(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2).
\]

A four-vertex backedge clique would have to use two vertices from each of two top modules. In each module the unique backward pair has second coordinates \(\{0,2\}\), and two such pairs cannot have the required complete separation in this interleaved order.

## Why this family is decisive

The base class \(\{TT_1,TT_2,\overrightarrow C_3\}\) has the constant binding function \(f\equiv2\). Therefore:

- If one could construct orders with
  \[
  w_n=\exp(o(n)),
  \]
  then
  \[
  d_n=\exp(\Theta(n))
  \]
  would not be bounded by any polynomial in \(w_n\), disproving the catalog question.
- Conversely, a positive answer to the catalog question would force
  \[
  w_n\ge \exp(\Omega(n))
  \]
  for this family.

The elementary bounds \(n+1\le w_n\le2^n\) leave both possibilities open. The active ramification depth of \(R_n\) is \(n-1\), so Theorem 3.1 deliberately does not settle this example.

---

# 5. Fully specified computation for \(w_n\)

The exact values of \(w_n\) can be attacked by SAT.

Represent \(V(R_n)\) as \(\{0,1,2\}^n\). For distinct words \(x,y\), let \(i\) be their first differing coordinate and orient

\[
x\to y
\quad\Longleftrightarrow\quad
y_i-x_i\equiv1\pmod 3.
\]

To test whether \(\vec\omega(R_n)\le k\):

1. Introduce Boolean variables \(x_{uv}\), meaning \(u\prec v\), with \(x_{uv}=\neg x_{vu}\).
2. Enforce transitivity of the order by
   \[
   (\neg x_{uv}\lor\neg x_{vz}\lor x_{uz})
   \]
   for all distinct \(u,v,z\).
3. For every \((k+1)\)-set \(Q\) inducing a transitive tournament, find its unique orientation order
   \[
   q_1\to q_2\to\cdots\to q_{k+1}.
   \]
   It is a backedge clique exactly when
   \[
   q_{k+1}\prec q_k\prec\cdots\prec q_1.
   \]
   Add the clause
   \[
   \bigvee_{i=1}^{k}\neg x_{q_{i+1},q_i}.
   \]

The resulting instance is satisfiable exactly when an ordering with no \((k+1)\)-vertex backedge clique exists. For larger instances the final family of clauses can be generated lazily: obtain a candidate order, find a maximum clique in its backedge graph, and add the corresponding violated clause.

---

# 6. Remaining gap

The partial theorem shows that ordinary substitution depth is not itself the obstruction: arbitrarily deep unary active substitutions preserve essentially the original binding function. What remains uncontrolled is repeated ramification by two or more nontransitive children at a nontransitive quotient.

No argument above bounds active ramification in terms of \(\vec\omega(T)\), and the balanced cyclic family \(R_n\) shows exactly why such a bound would have to be quantitatively strong. Thus the original polynomial-preservation question remains open.