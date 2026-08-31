```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "On the inherited range n >= 4, K_4 has square energy 3 < 16/5, so the stated 4n/5 bound is false.",
  "would_publish": false,
  "caveats": "This only refutes the literal n >= 4 formulation; the natural repair n >= 5, or an asymptotic interpretation, remains unresolved."
}
```

## 1. Statement and its ambiguity

The preceding theorem in the source has the range \(n\ge 4\). Thus the literal interpretation of “the above bound can be improved to \(4n/5\)” is

\[
s(G)\ge \frac{4n}{5}
\tag{C}
\]

for every connected graph \(G\) of order \(n\ge4\).

Under that interpretation, (C) is false.

## 2. Counterexample

Take \(G=K_4\). Its adjacency matrix is \(J_4-I_4\), so its spectrum is

\[
3,-1,-1,-1.
\]

Consequently,

\[
s^+(K_4)=3^2=9,\qquad
s^-(K_4)=3\cdot(-1)^2=3,
\]

and hence

\[
s(K_4)=3<\frac{16}{5}=\frac{4|V(K_4)|}{5}.
\]

The same obstruction occurs for \(P_4\) and \(K_{1,3}\): every bipartite graph has symmetric adjacency spectrum, so for a tree \(T\),

\[
s^+(T)=s^-(T)=|E(T)|=|V(T)|-1.
\]

Thus every tree of order four has square energy \(3<16/5\).

More generally,

\[
s(K_n)=n-1,
\]

so \(K_n\) satisfies \(s(K_n)\ge4n/5\) exactly when \(n\ge5\). Therefore \(n=5\) is the earliest possible starting point for an exact \(4n/5\) theorem.

## 3. The natural repaired conjecture

The substantive version is presumably:

> **Repaired conjecture.** Every connected graph \(G\) of order \(n\ge5\) satisfies
> \[
> s(G)\ge\frac{4n}{5}.
> \tag{C\(_5\)}
> \]

The order-four counterexample says nothing about \((\mathrm C_5)\). I do not have a proof or a counterexample to this repaired statement. The following self-contained sufficient conditions cover several substantial classes.

---

## 4. A chromatic-density bound

### Proposition 1

For every nonempty graph \(G\) with \(m\) edges and chromatic number \(\chi(G)\),

\[
s(G)\ge \frac{2m}{\chi(G)}.
\tag{1}
\]

### Proof

Write the adjacency matrix spectrally as

\[
A=P-N,
\]

where \(P=A_+\succeq0\), \(N=(-A)_+\succeq0\), and \(PN=0\). Thus

\[
s^+(G)=\operatorname{tr}(P^2),\qquad
s^-(G)=\operatorname{tr}(N^2).
\]

Let \(c=\chi(G)\), fix a proper \(c\)-coloring, and let \(\mathcal E\) be the pinching map that retains only the diagonal blocks corresponding to the color classes. Since every color class is independent,

\[
\mathcal E(A)=0,
\]

and therefore

\[
\mathcal E(P)=\mathcal E(N)=B,
\]

say. Put

\[
P_0=P-B,\qquad N_0=N-B,\qquad \beta=\|B\|_F^2.
\]

Because block-diagonal and off-diagonal-block matrices are Frobenius orthogonal,

\[
s^+=\beta+\|P_0\|_F^2,\qquad
s^-=\beta+\|N_0\|_F^2.
\tag{2}
\]

Moreover, \(PN=0\) gives

\[
0=\operatorname{tr}(PN)
 =\beta+\operatorname{tr}(P_0N_0).
\]

Hence, by Cauchy–Schwarz,

\[
\|P_0\|_F\|N_0\|_F\ge\beta.
\tag{3}
\]

We also use the following pinching inequality: if \(X\succeq0\) is partitioned into \(c\) diagonal blocks, then

\[
\|X\|_F^2\le c\|\mathcal E(X)\|_F^2.
\tag{4}
\]

Indeed, write \(X=YY^*\), split \(Y\) into block rows \(Y_i\), and put \(Z_i=Y_i^*Y_i\). Then

\[
\|X\|_F^2
 =\sum_{i,j}\operatorname{tr}(Z_iZ_j)
 \le c\sum_i\operatorname{tr}(Z_i^2)
 =c\|\mathcal E(X)\|_F^2,
\]

where \(2\operatorname{tr}(Z_iZ_j)\le
\operatorname{tr}(Z_i^2)+\operatorname{tr}(Z_j^2)\).

Applying (4) to \(P\) and \(N\), and defining

\[
x=\frac{\|P_0\|_F^2}{\beta},\qquad
y=\frac{\|N_0\|_F^2}{\beta},
\]

we obtain

\[
x,y\le c-1,\qquad xy\ge1
\]

by (3). Consequently,

\[
\max\left\{\frac{s^+}{s^-},\frac{s^-}{s^+}\right\}\le c-1.
\tag{5}
\]

For example, if \(x\ge y\), then \(y\ge1/x\), and hence

\[
\frac{s^+}{s^-}
 =\frac{1+x}{1+y}
 \le\frac{1+x}{1+1/x}
 =x\le c-1.
\]

Let \(a=\min\{s^+,s^-\}\). Equation (5) gives

\[
2m=s^++s^-\le ca,
\]

which proves (1). ∎

### Consequences

1. If
   \[
   m\ge \frac{2}{5}\chi(G)n,
   \]
   then \(s(G)\ge4n/5\).

2. Every connected bipartite graph of order \(n\ge5\) satisfies \((\mathrm C_5)\), since \(\chi=2\) and \(m\ge n-1\). In fact,
   \[
   s^+(G)=s^-(G)=m\ge n-1.
   \]

3. Every vertex-\(c\)-critical graph with \(c\ge5\) satisfies \((\mathrm C_5)\). Indeed, its minimum degree is at least \(c-1\), so
   \[
   m\ge\frac{(c-1)n}{2},
   \]
   and Proposition 1 gives
   \[
   s(G)\ge\frac{c-1}{c}n\ge\frac45n.
   \]

4. Using Brooks' theorem, every connected \(d\)-regular graph of order at least five satisfies \((\mathrm C_5)\). For \(d\ge3\), unless the graph is complete, \(\chi\le d\), giving
   \[
   s(G)\ge \frac{nd}{\chi}\ge n.
   \]
   Complete graphs have \(s(K_n)=n-1\). Even cycles are bipartite. For odd cycles, deleting one vertex gives an induced \(P_{n-1}\), hence \(s(C_n)\ge n-2\), which suffices for odd \(n\ge11\); the cases \(C_5,C_7,C_9\) follow directly from the eigenvalues \(2\cos(2\pi j/n)\).

More generally, if \(\bar d=2m/n\) and

\[
\bar d\ge\frac45\Delta(G),
\]

then Brooks' theorem and Proposition 1 prove \((\mathrm C_5)\), apart from the complete-graph and odd-cycle exceptions, which were just handled.

---

## 5. A degree-sequence sufficient condition

There is also a direct matrix bound independent of coloring.

### Proposition 2

For every graph with degree sequence \(d_1,\dots,d_n\) and \(m>0\),

\[
s(G)\ge
\frac{4m^2}{\,2m+\sum_i d_i^2\,}.
\tag{6}
\]

### Proof

For any positive semidefinite matrix \(X\),

\[
s^+(A)\ge
\frac{\bigl(\operatorname{tr}(AX)\bigr)_+^2}
     {\operatorname{tr}(X^2)}.
\tag{7}
\]

Indeed, with \(A=P-N\) as above,

\[
\operatorname{tr}(AX)
 \le \operatorname{tr}(PX)
 \le \|P\|_F\|X\|_F.
\]

Apply (7) with the signless Laplacian \(Q=D+A\succeq0\). We have

\[
\operatorname{tr}(AQ)=2m,\qquad
\operatorname{tr}(Q^2)=\sum_i d_i^2+2m.
\]

This gives (6) for \(s^+\). Applying the same argument to \(-A\) with the Laplacian \(L=D-A\succeq0\) gives the identical lower bound for \(s^-\). ∎

Writing

\[
\bar d=\frac{2m}{n},\qquad
\sigma^2=\frac1n\sum_i(d_i-\bar d)^2,
\]

(6) becomes

\[
s(G)\ge
\frac{n\bar d^2}{\bar d^2+\bar d+\sigma^2}.
\]

Thus \((\mathrm C_5)\) holds whenever

\[
\sigma^2\le \frac{\bar d(\bar d-4)}4.
\]

This includes, for example, every regular graph of degree at least four, although Proposition 1 gives a stronger result for regular graphs.

## 6. Remaining gap

The exact statement inherited from the source's range \(n\ge4\) is disproved by \(K_4\). If the intended conjecture starts at \(n=5\), the difficult uncovered regime consists primarily of sparse, irregular, non-bipartite graphs not meeting the chromatic-density or degree-variance criteria above. No argument here resolves that repaired conjecture.