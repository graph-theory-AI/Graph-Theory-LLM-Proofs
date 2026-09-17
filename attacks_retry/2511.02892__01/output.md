```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain the second-moment asymptotic for uniform simple graphs and prove that it is dominated by atypical graphs, but the probability of an exactly zero coefficient remains uncontrolled.",
  "would_publish": false,
  "caveats": "No anti-concentration at zero is proved; novelty of these partial results has not been checked."
}
```

# Partial result: the second moment is not a typical scale

I interpret the question as concerning the uniformly random labelled **simple** 4-regular graph.

The previous attempt’s pairing-model second-moment formula is correct; I independently rederive it below. I then resolve the conditioning-on-simplicity issue and obtain an additional conclusion: **the coefficient is smaller in probability than its root-mean-square scale**. Thus the large second moment is carried by atypical graphs, and a straightforward moment approach faces an additional obstacle.

This does not settle a.a.s. non-vanishing.

## 1. Statement of the partial results

For a 4-regular graph \(G\), orient its edges arbitrarily and put
\[
c(G)=
\left[\prod_{v\in V(G)}x_v^2\right]
\prod_{(u,v)\in\vec E(G)}(x_u-x_v).
\]
Changing the chosen orientations changes only the overall sign. In particular, \(c(G)^2\) and the event \(c(G)=0\) are graph invariants.

Let \(\mathbb P_n\) denote the uniform distribution on labelled simple 4-regular graphs on \(n\) vertices, and set
\[
a_n=\mathbb E_{\mathbb P_n}c(G)^2.
\]

### Theorem

The following statements hold.

1. **Second moment in the intended model:**
   \[
   \boxed{\displaystyle
   a_n\sim
   \frac23 e^{-3/4}\sqrt{2\pi n}
   \left(\frac32\right)^n.}
   \tag{1}
   \]

2. **Cycle counts under squared-coefficient weighting:** Define
   \[
   \mathbb Q_n(G)=\frac{c(G)^2}{a_n}\mathbb P_n(G).
   \tag{2}
   \]
   For any fixed finite collection of lengths \(\ell\ge3\), the corresponding cycle counts converge under \(\mathbb Q_n\) to independent Poisson random variables with means
   \[
   \boxed{\displaystyle
   \mu_\ell=
   \frac{3^\ell+1+2(-2)^\ell}{2\ell}.}
   \tag{3}
   \]
   By comparison, under \(\mathbb P_n\) the limiting means are
   \[
   \lambda_\ell=\frac{3^\ell}{2\ell}.
   \tag{4}
   \]

3. **The annealed scale is atypical:**
   \[
   \boxed{\displaystyle
   \frac{c(G)^2}{a_n}\xrightarrow{\mathbb P_n}0.}
   \tag{5}
   \]
   Equivalently,
   \[
   \boxed{\displaystyle
   |c(G)|=
   o_{\mathbb P_n}\!\left(
      n^{1/4}\left(\frac32\right)^{n/2}
   \right).}
   \tag{6}
   \]

Consequently,
\[
\boxed{\displaystyle
\frac{\mathbb E_{\mathbb P_n}c(G)^4}
     {(\mathbb E_{\mathbb P_n}c(G)^2)^2}
\longrightarrow\infty.}
\tag{7}
\]

The proofs are elementary pairing enumeration and endpoint asymptotics. In particular, no estimate for cycles of growing length is assumed.

---

## 2. Rechecking the pairing-model second moment

Give each of \(n\) vertices four distinguishable stubs. Let \(M\) be a uniformly random perfect matching of all \(4n\) stubs. Write \(C(M)\) for the central coefficient of its graph polynomial, choosing edge directions by any fixed stub-order convention.

Loops are permitted here and force \(C(M)=0\). This model is only an auxiliary device; simplicity will be imposed later.

Let
\[
b_n=\mathbb E C(M)^2.
\]

A term contributing to \(C(M)\) chooses one endpoint of each matched pair and exactly two stubs at each vertex. Encode that choice by a stub set \(S\). For two such sets \(S,T\), classify stubs by their membership bits:
\[
11,\quad 00,\quad 10,\quad 01.
\]

At each vertex, if there are \(k\) stubs of type \(11\), then there are also \(k\) of type \(00\), and \(2-k\) of each other type. Thus, globally,
\[
|11|=|00|=a,\qquad |10|=|01|=2n-a.
\]

A matching is compatible with both endpoint choices precisely when it pairs
\[
11\leftrightarrow00,\qquad 10\leftrightarrow01.
\]
There are
\[
a!(2n-a)!
\]
such matchings.

The product of the two expansion signs is \(+1\) on a \(11\)-\(00\) pair and \(-1\) on a \(10\)-\(01\) pair. Its total is therefore
\[
(-1)^{2n-a}=(-1)^a.
\]

For a fixed local choice of \(S\), the numbers of choices of \(T\) with intersection size \(0,1,2\) are \(1,4,1\). Hence
\[
b_n=
\frac{6^n}{(4n-1)!!}
\sum_{a=0}^{2n}
[z^a](1+4z+z^2)^n
(-1)^a a!(2n-a)!.
\]

Using
\[
a!(2n-a)!
=(2n+1)!\int_0^1x^a(1-x)^{2n-a}\,dx,
\]
we obtain
\[
\boxed{\displaystyle
b_n=
\frac{6^n(2n+1)!}{(4n-1)!!}
\int_0^1 q(x)^n\,dx,
\qquad
q(x)=1-6x+6x^2.}
\tag{8}
\]

The absolute value of \(q\) is strictly below \(1\) away from \(0,1\), and
\[
q(x)=1-6x+O(x^2)
\]
near \(0\), with the symmetric expansion near \(1\). Therefore
\[
\int_0^1q(x)^n\,dx\sim\frac1{3n}.
\tag{9}
\]
This remains valid for odd \(n\); the negative interior contribution is exponentially smaller.

Since
\[
(4n-1)!!=\frac{(4n)!}{2^{2n}(2n)!},
\qquad
\binom{4n}{2n}\sim\frac{16^n}{\sqrt{2\pi n}},
\]
equation (8) gives
\[
\boxed{\displaystyle
b_n\sim
\frac23\sqrt{2\pi n}\left(\frac32\right)^n.}
\tag{10}
\]

---

## 3. A fixed-subgraph calculation

The following extension of (8) controls the effect of prescribing finitely many matched pairs.

Let \(F\) be a fixed partial matching consisting of \(r\) pairs and incident with \(s\) vertices. At those \(s\) vertices, consider ordered local endpoint selections \(S,T\), each containing two stubs per vertex, compatible with every pair of \(F\).

For such a selection, write

- \(a\) for the number of type-\(11\) stubs at these vertices;
- \(r_A\) for the number of prescribed \(11\)-\(00\) pairs;
- \(r_B=r-r_A\) for the number of prescribed \(10\)-\(01\) pairs.

Define
\[
R_F(x)=
\sum_{\text{compatible local }S,T}
(-1)^a
x^{a-r_A}(1-x)^{2s-a-r_B}.
\tag{11}
\]
The exponents are nonnegative: they count the remaining stubs of the relevant types after the prescribed pairs are removed.

The same matching enumeration as above gives the exact formula
\[
\boxed{\displaystyle
\mathbb E[C(M)^2\mid F\subseteq M]
=
\frac{6^{n-s}(2n-r+1)!}{(4n-2r-1)!!}
\int_0^1q(x)^{n-s}R_F(x)\,dx.}
\tag{12}
\]

Indeed, after removing \(F\), the two types of compatible residual pairs can be matched in
\[
(a_{\rm total}-r_A)!
(2n-a_{\rm total}-r_B)!
\]
ways. Applying the beta integral and summing over the unaffected vertices yields (12).

Replacing \(T\) by its complement at the \(s\) vertices exchanges the two exponents in (11) without changing the sign. Consequently,
\[
R_F(1-x)=R_F(x).
\tag{13}
\]

For every fixed polynomial \(R\),
\[
\int_0^1q(x)^{n-s}R(x)\,dx
=
\frac{R(0)+R(1)}{6n}+o(n^{-1}).
\tag{14}
\]
Combining (8), (12), and (13), we obtain
\[
\boxed{\displaystyle
\frac{\mathbb E[C(M)^2\mid F\subseteq M]}{b_n}
\longrightarrow
\frac{2^r}{6^s}R_F(0).}
\tag{15}
\]

We shall also use the weaker bound
\[
\frac{\mathbb E[C(M)^2\mid F\subseteq M]}{b_n}=O_F(1).
\tag{16}
\]
It follows directly from (12), since
\[
\int_0^1 |q(x)|^{n-s}|R_F(x)|\,dx=O_F(n^{-1}).
\]

### Prescribing a cycle

Suppose \(F\) is a cycle of length \(\ell\), where a loop is regarded as a 1-cycle and a pair of parallel edges as a 2-cycle. Then \(r=s=\ell\).

To evaluate \(R_F(0)\), the exponent \(a-r_A\) must vanish. Thus every stub outside the prescribed cycle is of type \(10\) or \(01\). At each cycle vertex, either:

1. the two cycle stubs are also of types \(10,01\); or
2. the cycle stubs are \(11\) and \(00\).

Compatibility along the prescribed edges forces the same alternative throughout the cycle.

In the first case, the choices are counted by the transfer matrix
\[
T=\begin{pmatrix}2&1\\1&2\end{pmatrix},
\]
so their contribution is
\[
\operatorname{tr}(T^\ell)=3^\ell+1.
\]

In the second case, there are two consistent directions for the \(11\)-\(00\) assignments around the cycle. At each vertex, the remaining \(10,01\) stubs can be assigned in two ways. The sign is \((-1)^\ell\). This contributes
\[
2^{\ell+1}(-1)^\ell=2(-2)^\ell.
\]

Therefore
\[
\boxed{\displaystyle
R_F(0)=\rho_\ell,
\qquad
\rho_\ell=3^\ell+1+2(-2)^\ell.}
\tag{17}
\]
In particular,
\[
\rho_1=0,\qquad \rho_2=18,\qquad \rho_3=12.
\]

Equations (15) and (17) give
\[
\boxed{\displaystyle
\frac{\mathbb E[C(M)^2\mid F\subseteq M]}{b_n}
\longrightarrow\frac{\rho_\ell}{3^\ell}.}
\tag{18}
\]

For vertex-disjoint prescribed cycles, the polynomials \(R_F\) factor, so the limits in (18) multiply.

---

## 4. Cycle counts under squared-coefficient weighting

Let \(X_\ell(M)\) count cycles of length \(\ell\) in the pairing multigraph, with the conventions above. Define the tilted pairing law
\[
\widehat{\mathbb P}^{\,\mathrm{pair}}_n(M)
=
\frac{C(M)^2}{b_n}\,
\mathbb P^{\mathrm{pair}}_n(M).
\tag{19}
\]

Under the ordinary pairing law, a direct enumeration gives
\[
\mathbb E X_\ell
=
\frac{(n)_\ell\,12^\ell}{2\ell}
\frac{(4n-2\ell-1)!!}{(4n-1)!!}
\longrightarrow
\frac{3^\ell}{2\ell}=\lambda_\ell.
\tag{20}
\]

The same enumeration of vertex-disjoint cycles, now using (18), gives their joint factorial moments under the tilted law. For fixed nonnegative integers \(k_1,\dots,k_L\),
\[
\widehat{\mathbb E}^{\,\mathrm{pair}}_n
\prod_{\ell=1}^L(X_\ell)_{k_\ell}
\longrightarrow
\prod_{\ell=1}^L
\left(\frac{\rho_\ell}{2\ell}\right)^{k_\ell}.
\tag{21}
\]

Here is the required check that overlapping cycles do not contribute to the limit. If a collection of distinct cycles overlaps, its union has \(s\) vertices and \(r>s\) edges in at least one component. There are \(O(n^s)\) possible placements of each fixed overlap pattern, and its prescribed pairs occur with probability \(O(n^{-r})\). By (16), the squared-coefficient tilt changes this by at most a pattern-dependent constant. Thus every such contribution is \(O(n^{-1})\). There are only finitely many patterns when \(L\) and the \(k_\ell\) are fixed.

The factorial moments in (21) characterize a product of Poisson laws. Consequently, under the tilted pairing law,
\[
(X_1,\dots,X_L)
\ \xrightarrow{d}\
\bigotimes_{\ell=1}^L
\operatorname{Poisson}(\mu_\ell),
\qquad
\mu_\ell=\frac{\rho_\ell}{2\ell}.
\tag{22}
\]
The corresponding ordinary pairing limit has means \(\lambda_\ell\).

Notice that \(\mu_1=0\), consistently with the fact that loops force \(C(M)=0\).

---

## 5. Conditioning on simplicity

Let \(\mathcal S_n\) be the event that the pairing graph is simple. Exactly,
\[
\mathcal S_n=\{X_1=X_2=0\}.
\]

Under the ordinary pairing law, (20) and the joint factorial-moment calculation give
\[
\mathbb P^{\mathrm{pair}}_n(\mathcal S_n)
\longrightarrow
e^{-\lambda_1-\lambda_2}
=e^{-15/4}.
\tag{23}
\]

Under the squared-coefficient tilt,
\[
\widehat{\mathbb P}^{\,\mathrm{pair}}_n(\mathcal S_n)
\longrightarrow
e^{-\mu_1-\mu_2}
=e^{-9/2},
\tag{24}
\]
because \(\mu_1=0\) and \(\mu_2=18/4=9/2\).

Every labelled simple 4-regular graph is represented by the same number, \((4!)^n\), of pairings. Therefore conditioning the ordinary pairing model on \(\mathcal S_n\) gives precisely \(\mathbb P_n\). Hence
\[
a_n
=
b_n\,
\frac{\widehat{\mathbb P}^{\,\mathrm{pair}}_n(\mathcal S_n)}
     {\mathbb P^{\mathrm{pair}}_n(\mathcal S_n)}
\sim e^{-3/4}b_n.
\]
Together with (10), this proves (1).

Likewise, conditioning the tilted pairing law on simplicity gives the law \(\mathbb Q_n\) defined in (2). The limiting cycle counts of lengths at least three remain independent of the limiting counts of lengths one and two. Thus (22) proves the asserted simple-model cycle law (3).

This completes the conditioning step that was missing from the previous attempt.

---

## 6. Why the normalized square tends to zero

Set
\[
W_n(G)=\frac{c(G)^2}{a_n}.
\]
Then
\[
\mathbb E_{\mathbb P_n}W_n=1,
\qquad
\mathbb Q_n(A)=\mathbb E_{\mathbb P_n}[W_n\mathbf1_A].
\tag{25}
\]

Fix an even integer \(\ell\ge4\). Write
\[
\Delta_\ell=\mu_\ell-\lambda_\ell
=\frac{1+2^{\ell+1}}{2\ell}>0,
\]
and define
\[
A_{n,\ell}
=
\left\{
X_\ell\ge\lambda_\ell+\frac{\Delta_\ell}{2}
\right\}.
\]

The two Poisson limits and Chebyshev’s inequality imply
\[
\limsup_{n\to\infty}\mathbb P_n(A_{n,\ell})
\le \frac{4\lambda_\ell}{\Delta_\ell^2},
\tag{26}
\]
and
\[
\limsup_{n\to\infty}\mathbb Q_n(A_{n,\ell}^{\,c})
\le \frac{4\mu_\ell}{\Delta_\ell^2}.
\tag{27}
\]

For every \(\varepsilon>0\), equation (25) gives
\[
\begin{aligned}
\mathbb P_n(W_n>\varepsilon)
&\le
\mathbb P_n(A_{n,\ell})
+
\mathbb P_n(W_n>\varepsilon,\ A_{n,\ell}^{\,c})\\
&\le
\mathbb P_n(A_{n,\ell})
+\varepsilon^{-1}\mathbb Q_n(A_{n,\ell}^{\,c}).
\end{aligned}
\]
Consequently,
\[
\limsup_{n\to\infty}\mathbb P_n(W_n>\varepsilon)
\le
\frac{4\lambda_\ell+4\varepsilon^{-1}\mu_\ell}
     {\Delta_\ell^2}.
\tag{28}
\]

As \(\ell\to\infty\) through even integers,
\[
\frac{\lambda_\ell}{\Delta_\ell^2}
=O\!\left(\ell\left(\frac34\right)^\ell\right)
\longrightarrow0,
\]
and the same holds with \(\mu_\ell\) in place of \(\lambda_\ell\). Thus (28) proves
\[
W_n\xrightarrow{\mathbb P_n}0.
\]

The order of limits is important: first \(n\to\infty\) with \(\ell\) fixed, and only then \(\ell\to\infty\). No uniform approximation for growing cycle lengths is needed.

Combining this with (1) proves (6).

Finally, for \(0<\varepsilon<1\),
\[
1=\mathbb E W_n
\le
\varepsilon+
\sqrt{\mathbb E W_n^2\,
      \mathbb P_n(W_n>\varepsilon)}.
\]
Since the probability tends to zero,
\[
\mathbb E W_n^2\longrightarrow\infty,
\]
which is (7).

---

## 7. What this establishes—and the remaining gap

The partial results give a fairly specific description of the obstruction to a naive second-moment strategy.

- The exact asymptotic survives conditioning on simplicity, with multiplier \(e^{-3/4}\).
- Squared-coefficient weighting favours even cycles and suppresses odd cycles.
- Although the relative change in the mean number of long fixed-length cycles is small, it is large compared with their Poisson fluctuations:
  \[
  \frac{(\mu_\ell-\lambda_\ell)^2}{\lambda_\ell}
  \asymp \frac1\ell\left(\frac43\right)^\ell.
  \]
- Consequently, the unweighted and squared-coefficient-weighted graph laws become distinguishable, and the second moment is carried by a vanishing-probability set of graphs.

In particular, a bounded-fourth-moment argument at this annealed normalization is impossible.

However, none of this bounds the atom at zero. The conclusion
\[
c(G)^2/a_n\to0
\]
is compatible both with a.a.s. non-vanishing at a smaller scale and with a substantial probability of exact cancellation.

The original unresolved step is still
\[
\boxed{\displaystyle
\mathbb P_n(c(G)=0)\longrightarrow0.}
\]
No proof of that assertion, or asymptotically relevant counterexample to it, is obtained here.