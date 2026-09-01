```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved; elementary Ramsey recurrences yield a weakened form, show that no k at most 33 is polite, and quantify the missing near-diagonal growth estimate.",
  "would_publish": false,
  "caveats": "There is no asymptotic proof or counterexample; the results below are self-contained but elementary."
}
```

# Mathematical writeup

## 1. Statement and notation

Let \(r(s,t)\) be the least \(n\) such that every red-blue coloring of \(K_n\) contains either a red \(K_s\) or a blue \(K_t\). Put
\[
\ell=\left\lceil\frac{k}{2}\right\rceil,\qquad
A_k=r(k,\ell),\qquad
S_k=r(k,k-1),\qquad
R_k=r(k,k),
\]
and
\[
q_k=\frac{A_k}{R_k}.
\]

According to the supplied definition, \(k\) is polite when

\[
q_k\le 2^{-31} \tag{P1}
\]
and
\[
\frac{R_k-1}{S_k}\ge 1+25q_k^{1/4}. \tag{P2}
\]

I do not prove or disprove that all sufficiently large \(k\) are polite.

---

## 2. A comparison between diagonal and half-diagonal Ramsey numbers

### Lemma 2.1
For \(2\le \ell\le k\), with \(d=k-\ell\),
\[
r(k,k)\le \binom{2d}{d}\,r(k,\ell).
\]

### Proof

Set \(A=r(k,\ell)=r(\ell,k)\). I claim that for all \(0\le i,j\le d\),
\[
r(\ell+i,\ell+j)\le \binom{i+j}{i}A. \tag{2.1}
\]

If \(i=0\), then by monotonicity,
\[
r(\ell,\ell+j)\le r(\ell,k)=A,
\]
and similarly when \(j=0\).

For \(i,j\ge1\), use the standard recurrence
\[
r(s,t)\le r(s-1,t)+r(s,t-1).
\]
Induction and Pascal's identity give
\[
\begin{aligned}
r(\ell+i,\ell+j)
&\le r(\ell+i-1,\ell+j)+r(\ell+i,\ell+j-1)\\
&\le \left[\binom{i+j-1}{i-1}+\binom{i+j-1}{i}\right]A\\
&=\binom{i+j}{i}A.
\end{aligned}
\]
Taking \(i=j=d\) proves the result. \(\square\)

For \(\ell=\lceil k/2\rceil\), we have \(d=\lfloor k/2\rfloor\), so
\[
\boxed{\quad
q_k=\frac{A_k}{R_k}\ge
\binom{2\lfloor k/2\rfloor}{\lfloor k/2\rfloor}^{-1}.
\quad} \tag{2.2}
\]

Asymptotically, this lower bound is of order
\[
\sqrt{k}\,2^{-k}.
\]

### Corollary 2.2
No integer \(k\le33\) is polite.

### Proof

If \(k\le33\), then \(d=\lfloor k/2\rfloor\le16\), and hence
\[
\binom{2d}{d}\le \binom{32}{16}
=601\,080\,390<2^{31}.
\]
By (2.2),
\[
q_k>\frac1{2^{31}},
\]
so (P1) fails. \(\square\)

Thus a necessary condition for politeness is
\[
k\ge34.
\]
This is only a finite exclusion and gives no asymptotic progress.

---

## 3. Lower-bound constructions

The following standard join construction is useful.

### Lemma 3.1
For \(s,t_1,\dots,t_m\ge2\), set
\[
T=1+\sum_{i=1}^m(t_i-1).
\]
Then
\[
r(s,T)\ge 1+\sum_{i=1}^m\bigl(r(s,t_i)-1\bigr). \tag{3.1}
\]

### Proof

For each \(i\), take a coloring on \(r(s,t_i)-1\) vertices containing neither a red \(K_s\) nor a blue \(K_{t_i}\). Color all edges between different blocks blue.

A red clique lies in one block and therefore has fewer than \(s\) vertices. A blue clique contains at most \(t_i-1\) vertices from block \(i\), hence has at most
\[
\sum_i(t_i-1)=T-1
\]
vertices. This gives the required coloring. \(\square\)

Two consequences are relevant.

### Consequence 3.2: a weak comparison for \(q_k\)

Taking two copies with \(t_1=t_2=\ell\), and noting that
\[
1+2(\ell-1)\le k,
\]
gives
\[
R_k\ge 2A_k-1.
\]
Consequently
\[
q_k\le \frac{A_k}{2A_k-1}
=\frac12+O(A_k^{-1}). \tag{3.2}
\]

Thus the elementary construction only places \(q_k\) between approximately \(2^{-k}\) and \(1/2\); it is very far from (P1).

### Consequence 3.3: strict growth from \(S_k\) to \(R_k\)

Taking \(m=2\), \(t_1=t\), \(t_2=2\), and using \(r(s,2)=s\), Lemma 3.1 gives
\[
r(s,t+1)\ge r(s,t)+s-1.
\]
In particular,
\[
R_k\ge S_k+k-1. \tag{3.3}
\]

If
\[
D_k=(R_k-1)-S_k,
\]
then
\[
\boxed{D_k\ge k-2.} \tag{3.4}
\]

Also, using the elementary upper bound
\[
S_k\le \binom{2k-3}{k-1},
\]
we obtain the unconditional weakened form
\[
\frac{R_k-1}{S_k}
\ge
1+\frac{k-2}{\binom{2k-3}{k-1}}
=
1+\Theta\!\left(k^{3/2}4^{-k}\right). \tag{3.5}
\]

This is exponentially weaker than what politeness may demand.

---

## 4. Exact scale of the second condition

The standard upper recurrence gives
\[
R_k\le r(k-1,k)+r(k,k-1)=2S_k,
\]
and monotonicity gives \(S_k\le R_k\). Hence
\[
\frac{R_k}{2}\le S_k\le R_k. \tag{4.1}
\]

Condition (P2) is exactly
\[
D_k\ge25S_k\left(\frac{A_k}{R_k}\right)^{1/4}. \tag{4.2}
\]

Using (4.1), a necessary consequence is
\[
D_k\ge \frac{25}{2}R_k^{3/4}A_k^{1/4}, \tag{4.3}
\]
while
\[
D_k\ge25R_k^{3/4}A_k^{1/4} \tag{4.4}
\]
would be sufficient.

Thus (P2), up to a factor of two, asks for the additive gap \(R_k-1-S_k\) to have the geometric-mean scale
\[
R_k^{3/4}A_k^{1/4}.
\]

In particular, since \(R_k\ge A_k\), politeness implies
\[
D_k\ge \frac{25}{2}A_k. \tag{4.5}
\]
This is already much stronger than the unconditional \(D_k\ge k-2\).

Combining (2.2) with (P2), any polite \(k\) must satisfy
\[
\frac{R_k-1}{S_k}-1
\ge
25\binom{2d}{d}^{-1/4},
\qquad d=\left\lfloor\frac{k}{2}\right\rfloor. \tag{4.6}
\]
Asymptotically the right side has order
\[
k^{1/8}2^{-k/4}. \tag{4.7}
\]

By contrast, (3.5) only gives order \(k^{3/2}4^{-k}\). The exponential gap between \(2^{-k/4}\) and \(4^{-k}\) is the main obstruction in this elementary approach.

---

## 5. What separation from the half-diagonal gives by averaging

For fixed \(k\), write \(x_t=r(k,t)\). Then
\[
\prod_{t=\ell+1}^{k}\frac{x_t}{x_{t-1}}
=
\frac{R_k}{A_k}
=q_k^{-1}.
\]
Therefore some \(t\in\{\ell+1,\dots,k\}\) satisfies
\[
\frac{r(k,t)}{r(k,t-1)}
\ge q_k^{-1/(k-\ell)}. \tag{5.1}
\]

In particular, if (P1) holds, then some intermediate increment satisfies
\[
\frac{r(k,t)}{r(k,t-1)}
\ge 2^{31/\lfloor k/2\rfloor}. \tag{5.2}
\]

This only locates a relatively large increment somewhere between \(r(k,\lceil k/2\rceil)\) and \(r(k,k)\). The conjecture needs control of the final increment
\[
r(k,k)-r(k,k-1).
\]
No valid monotonicity or convexity principle transferring (5.1) to the final increment is known from the arguments above.

---

## 6. A quantitative sufficient criterion

The following records exactly how much weaker than a constant consecutive-Ramsey gap would suffice.

### Proposition 6.1
Suppose there are constants \(c,d>0\) with \(d<c/4\) such that, for all sufficiently large \(k\),
\[
q_k\le e^{-ck}
\]
and
\[
\frac{R_k-1}{S_k}-1\ge e^{-dk}.
\]
Then every sufficiently large \(k\) is polite.

### Proof

The first condition implies (P1) once
\[
k\ge \frac{31\log 2}{c}.
\]
Moreover,
\[
25q_k^{1/4}\le25e^{-ck/4}.
\]
Since \(d<c/4\),
\[
e^{-dk}\ge25e^{-ck/4}
\]
for all
\[
k\ge\frac{\log25}{c/4-d}.
\]
Thus (P2) also holds eventually. \(\square\)

This is only a conditional rate-matching observation. Neither required estimate is proved here.

---

## 7. Why the standard numerical bounds do not settle (P1)

For comparison, the recurrence gives
\[
A_k\le \binom{k+\ell-2}{k-1}
=
\left(\frac{3\sqrt3}{2}+o(1)\right)^k,
\]
whereas the elementary random-coloring argument gives
\[
R_k\ge \left(\frac{1}{e\sqrt2}-o(1)\right)k\,2^{k/2}.
\]
Their quotient has an exponentially growing upper estimate, since
\[
\frac{3\sqrt3/2}{\sqrt2}\approx1.837.
\]
Thus these standard self-contained bounds do not even imply \(q_k=o(1)\), let alone \(q_k\le2^{-31}\).

## Conclusion and gap

The following unconditional weakened estimates have been established:
\[
\binom{2\lfloor k/2\rfloor}{\lfloor k/2\rfloor}^{-1}
\le
\frac{r(k,\lceil k/2\rceil)}{r(k,k)}
\le
\frac{A_k}{2A_k-1},
\]
and
\[
\frac{r(k,k)-1}{r(k,k-1)}
\ge
1+\frac{k-2}{\binom{2k-3}{k-1}}.
\]

They imply that no \(k\le33\) is polite and clarify the quantitative strength of (P2). They do not establish either politeness condition asymptotically. A complete proof would require both a substantially stronger diagonal-versus-half-diagonal comparison and a genuinely new lower bound on the final near-diagonal Ramsey increment.