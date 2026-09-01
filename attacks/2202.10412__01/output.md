```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The auxiliary path can be removed at the cost of an explicit exponential chi-bound, and the conjectured polynomial bound follows under a local-neighborhood or one-exceptional-branch condition.",
  "would_publish": false,
  "caveats": "The general exponential factor remains; no proof or counterexample for branched brooms is obtained."
}
```

# Mathematical writeup

## 1. Setup and source-paper facts

All graphs are finite and simple, and all copies are induced. For an induced subgraph \(F\) and \(X\subseteq V(F)\), write
\[
A_F(X)=\{v\in V(F)\setminus X: N_F(v)\cap X=\varnothing\}
\]
for the antineighborhood of \(X\) in \(F\).

I use the following consequences of the definitions in the source paper.

1. If a copy \(X\) of \(H\) in \(G\) is not \(\sigma\)-nondominating, then, writing \(k=\omega(G)\),
   \[
   \chi(A_G(X))\leq \sigma(k). \tag{1}
   \]
   Indeed, under the source definition one has the sharper bound involving the clique number of the antineighborhood, and monotonicity of \(\sigma\) gives (1).

2. The absence of a \((\psi,q)\)-scattering is inherited by induced subgraphs. This follows directly because a scattering is witnessed by vertex subsets and their induced adjacencies, chromatic numbers and clique numbers.

3. We need only the following consequence of Theorem 2.2 of the source paper. Fix any auxiliary path \(J\) and any auxiliary nondomination polynomial. Ignoring the conclusion concerning \(J\), there is a nondecreasing polynomial
   \[
   \tau=\tau_{\psi,q,H}
   \]
   such that
   \[
   \chi(F)>\tau(\omega(F)),\quad
   F\text{ has no }(\psi,q)\text{-scattering}
   \quad\Longrightarrow\quad
   F\text{ contains a copy of }H. \tag{2}
   \]

Let
\[
h=|V(H)|,\qquad c=\chi(H)\leq 2.
\]

The issue in Conjecture 2.3 is therefore not obtaining an ordinary copy of \(H\), but obtaining one whose antineighborhood remains polynomially anomalous.

---

## 2. An exponential substitute for Conjecture 2.3

### Theorem 2.1

With \(\psi,\sigma,q,H\) fixed as in the conjecture, let \(\tau\) satisfy (2). Define
\[
C(k)=\tau(k)+\sigma(k)+c
\]
and
\[
\Phi_{\exp}(k)=C(k)\sum_{i=0}^{k-1}h^i.
\]
Thus, if \(h>1\),
\[
\Phi_{\exp}(k)
=
\bigl(\tau(k)+\sigma(k)+c\bigr)\frac{h^k-1}{h-1}.
\]

If \(G\) contains no \((\psi,q)\)-scattering and
\[
\chi(G)>\Phi_{\exp}(\omega(G)),
\]
then \(G\) contains a \(\sigma\)-nondominating copy of \(H\).

Consequently, the conjecture becomes true if “polynomial” is weakened to “an exponential function of the clique number.”

### Proof

Suppose that \(G\) has no \((\psi,q)\)-scattering and no \(\sigma\)-nondominating copy of \(H\). Put
\[
k=\omega(G),\qquad S=\sigma(k),\qquad C=C(k).
\]

Define
\[
U_0=0,\qquad U_r=C+hU_{r-1}\quad (1\leq r\leq k).
\]
Thus
\[
U_r=C\sum_{i=0}^{r-1}h^i.
\]

We prove by induction on \(r\) that every induced subgraph \(F\) of \(G\) with \(\omega(F)\leq r\) satisfies
\[
\chi(F)\leq U_r. \tag{3}
\]

The assertion is immediate for \(r=0\). Let \(r\geq1\).

If
\[
\chi(F)\leq\tau(\omega(F)),
\]
then
\[
\chi(F)\leq\tau(k)\leq C\leq U_r.
\]

Otherwise, (2), applied to \(F\), gives a copy \(X\) of \(H\) in \(F\). Since \(X\) is also a copy of \(H\) in \(G\), (1) gives
\[
\chi(A_F(X))
\leq \chi(A_G(X))
\leq S. \tag{4}
\]

Every vertex of \(F\setminus(X\cup A_F(X))\) has a neighbor in \(X\), and hence
\[
V(F)\subseteq X\cup A_F(X)\cup\bigcup_{x\in X}N_F(x).
\]
For each \(x\in X\),
\[
\omega(F[N_F(x)])\leq r-1,
\]
since a clique in \(N_F(x)\), together with \(x\), is a larger clique. Therefore the induction hypothesis gives
\[
\chi(F[N_F(x)])\leq U_{r-1}.
\]
Using disjoint color palettes,
\[
\begin{aligned}
\chi(F)
&\leq \chi(F[X])+\chi(A_F(X))
   +\sum_{x\in X}\chi(F[N_F(x)])\\
&\leq c+S+hU_{r-1}\\
&\leq C+hU_{r-1}=U_r.
\end{aligned}
\]
This proves (3). Taking \(F=G\) and \(r=k\) yields
\[
\chi(G)\leq U_k=\Phi_{\exp}(k),
\]
as required. \(\square\)

### Significance and limitation

This proves that, in the no-scattering regime, graphs with no \(\sigma\)-nondominating broom are still \(\chi\)-bounded. The bound is
\[
O\!\left(h^{\omega(G)}
       \bigl(\tau(\omega(G))+\sigma(\omega(G))\bigr)\right).
\]

The exponential factor comes from coloring as many as \(h\) neighborhood branches at every one-unit decrease of the clique number. Eliminating this repeated \(h\)-fold branching is exactly the missing polynomial step.

---

## 3. A polynomial special case: locally polynomial neighborhoods

The exponential branching disappears if individual neighborhoods already have a polynomial chromatic bound.

### Proposition 3.1

Let \(\rho\colon\mathbb N\to\mathbb N\) be a nondecreasing polynomial. Under the hypotheses of Conjecture 2.3, additionally assume that
\[
\chi(G[N_G(v)])\leq \rho(\omega(G))
\qquad\text{for every }v\in V(G). \tag{5}
\]
Then \(G\) contains a \(\sigma\)-nondominating copy of \(H\) whenever
\[
\chi(G)>
\phi_\rho(\omega(G)),
\]
where
\[
\phi_\rho(k)=\tau(k)+\sigma(k)+c+h\rho(k).
\]
In particular, \(\phi_\rho\) is a nondecreasing polynomial.

### Proof

Put \(k=\omega(G)\). If \(\chi(G)>\phi_\rho(k)\), then in particular \(\chi(G)>\tau(k)\), so (2) supplies a copy \(X\) of \(H\).

If \(X\) were not \(\sigma\)-nondominating, then
\[
\chi(A_G(X))\leq\sigma(k).
\]
As before,
\[
V(G)\subseteq X\cup A_G(X)\cup\bigcup_{x\in X}N_G(x).
\]
Using (5),
\[
\chi(G)
\leq c+\sigma(k)+h\rho(k)
<\phi_\rho(k),
\]
a contradiction. \(\square\)

This covers, for example, graphs with uniformly bounded local chromatic number. In particular, for triangle-free graphs every open neighborhood is stable, so one may take \(\rho\equiv1\).

---

## 4. Explicit unconditional bounds for the two smallest path targets

These cases are already encompassed qualitatively by the path result in the source paper, but the following bounds do not require the no-scattering hypothesis.

### 4.1. A single vertex

If \(H=K_1\), then
\[
\chi(G)\leq \omega(G)\bigl(\sigma(\omega(G))+1\bigr)
\]
whenever \(G\) has no \(\sigma\)-nondominating vertex.

Indeed, put \(k=\omega(G)\) and \(S=\sigma(k)\). For every vertex \(v\),
\[
\chi(A_G(v))\leq S.
\]
Inducting on the clique number of induced subgraphs and using
\[
V(F)=\{v\}\cup N_F(v)\cup A_F(v)
\]
gives the recurrence
\[
W_r\leq W_{r-1}+S+1,
\]
and hence \(W_k\leq k(S+1)\).

### 4.2. An edge

If \(H=K_2\), then every graph \(G\) with no \(\sigma\)-nondominating edge satisfies
\[
\chi(G)\leq
2k+\binom{k}{2}\sigma(k),
\qquad k=\omega(G). \tag{6}
\]

To prove this, let \(C\) be a maximum clique of size \(k\), and put \(S=\sigma(k)\). For \(v\notin C\), let
\[
M(v)=\{a\in C: av\notin E(G)\}.
\]
This set is nonempty by maximality of \(C\).

If \(|M(v)|=1\), assign \(v\) to the unique member \(a\in M(v)\). For each fixed \(a\), the assigned vertices form a stable set: two adjacent such vertices, together with \(C\setminus\{a\}\), would form a clique of size \(k+1\). These vertices therefore require at most \(k\) colors.

If \(|M(v)|\geq2\), assign \(v\) to some pair \(\{a,b\}\subseteq M(v)\). Since \(a,b\in C\), they form an edge, and every vertex assigned to \(\{a,b\}\) lies in \(A_G(\{a,b\})\). As that edge is not \(\sigma\)-nondominating, each such class has chromatic number at most \(S\). There are at most \(\binom{k}{2}\) classes.

Finally, color \(C\) with \(k\) colors. This proves (6).

---

## 5. A precise structural reduction: the two-branch obstruction

The proof of Theorem 2.1 shows that a polynomial bound would follow if one could prevent two or more anomalous neighborhood branches at every copy of \(H\).

### Proposition 5.1

Let \(\rho\) be a nondecreasing polynomial. Suppose that \(G\) has no \((\psi,q)\)-scattering and satisfies the following condition:

> For every induced subgraph \(F\subseteq G\) with  
> \(\chi(F)>\tau(\omega(F))\), there is a copy \(X\) of \(H\) in \(F\) such that, for all but at most one \(x\in X\),
> \[
> \chi(F[N_F(x)])
> \leq
> \rho\bigl(\omega(F[N_F(x)])\bigr). \tag{7}
> \]

Then \(G\) contains a \(\sigma\)-nondominating copy of \(H\) whenever
\[
\chi(G)>
\omega(G)\Bigl(
\tau(\omega(G))+\sigma(\omega(G))+c+(h-1)\rho(\omega(G))
\Bigr). \tag{8}
\]

### Proof

Assume there is no \(\sigma\)-nondominating copy. Put
\[
k=\omega(G),\qquad
D=\tau(k)+\sigma(k)+c+(h-1)\rho(k).
\]

We prove by induction on \(r\) that every induced \(F\subseteq G\) with \(\omega(F)\leq r\) satisfies
\[
\chi(F)\leq rD.
\]

If \(\chi(F)\leq\tau(\omega(F))\), this follows from \(\tau(\omega(F))\leq D\).

Otherwise choose \(X\) as in (7), and let \(x_0\) be the possible exceptional vertex. The antineighborhood of \(X\) in \(F\) has chromatic number at most \(\sigma(k)\). The \(h-1\) nonexceptional neighborhoods require at most
\[
(h-1)\rho(k)
\]
colors in total. The exceptional neighborhood has clique number at most \(r-1\), and hence has chromatic number at most \((r-1)D\) by induction. Therefore
\[
\chi(F)
\leq
\sigma(k)+c+(h-1)\rho(k)+(r-1)D
\leq rD.
\]
Taking \(F=G\) proves the assertion. \(\square\)

### Corollary 5.2: structure of any hypothetical counterexample

Fix any polynomial \(\rho\). If a graph \(G\) violates the polynomial bound in (8), has no scattering, and has no \(\sigma\)-nondominating \(H\), then it contains an induced subgraph \(F\) such that

- \(\chi(F)>\tau(\omega(F))\), and
- for every copy \(X\) of \(H\) in \(F\), at least two vertices \(x\in X\) satisfy
  \[
  \chi(F[N_F(x)])
  >
  \rho\bigl(\omega(F[N_F(x)])\bigr). \tag{9}
  \]

Thus every sufficiently large counterexample must have a core in which every broom copy has at least two polynomially anomalous neighborhood branches.

---

## 6. The unresolved step

Taking \(\rho=\psi\), condition (9) seems close to the definition of a scattering, but it is not enough.

For two anomalous vertices \(x,y\in X\), the sets \(N_F(x)\) and \(N_F(y)\)

1. need not be disjoint;
2. may have a chromatically anomalous intersection;
3. may lose most of their chromatic number when made disjoint; and
4. even when disjoint anomalous private parts remain, their cross-adjacency need not satisfy the sparse-neighborhood condition required for a \((\psi,q)\)-scattering.

If \(x\) and \(y\) are adjacent, their common neighborhood has clique number at most \(\omega(F)-2\), which is potentially useful. For nonadjacent vertices—especially distinct leaves of a broom—there is only a one-unit clique decrease. Rich adjacency between the two private neighborhood branches is also compatible with the absence of a scattering, and I do not see a valid argument converting that rich adjacency into a broom with a polynomially anomalous antineighborhood.

Accordingly, Theorem 2.1 gives a complete exponential bound, Propositions 3.1 and 5.1 give polynomial special cases and a structural reduction, but the multi-branch case for a genuinely branched broom remains open.