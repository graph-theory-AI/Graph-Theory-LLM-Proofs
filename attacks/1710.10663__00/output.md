```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Under the standard additive-gap definition, the case L=2 has maxcode_2(ε)=1/(4ε)+O(1), whereas the displayed formula gives c_2=1.",
  "would_publish": false,
  "caveats": "This almost certainly identifies a transcription error in the catalog constant; the correspondingly corrected conjecture for even L≥4 remains open."
}
```

## 1. Statement and normalization

Use the standard zero-rate parameter from the binary Hamming setting. For \(C\subseteq\{0,1\}^n\), put
\[
\operatorname{rad}_L(C)
 =\min_{\substack{S\subseteq C\\ |S|=L}}
   \min_{y\in\{0,1\}^n}\max_{x\in S}d_H(x,y),
\]
and let \(\tau_L(M)\) be the asymptotically maximal value of
\(\operatorname{rad}_L(C)/n\) among \(M\)-word codes. Thus
\[
\operatorname{maxcode}_L(\varepsilon)
 =\max\{M:\tau_L(M)\ge \tau_L+\varepsilon\},
\]
up to an immaterial choice of strict versus non-strict inequality.

Under this additive-gap normalization, the displayed constant
\[
c_L=2^{-\lfloor L/2\rfloor}\binom{L}{\lfloor L/2\rfloor}
\]
is already incompatible with the exactly solvable case \(L=2\).

## 2. Exact calculation for \(L=2\)

For two words \(x,y\),
\[
\min_z\max\{d_H(x,z),d_H(y,z)\}
 =\left\lceil\frac{d_H(x,y)}2\right\rceil.
\]
Consequently, in the asymptotic-in-blocklength definition, \(\tau_2(M)\) is one half of the largest possible relative minimum distance of an \(M\)-word binary code.

### Plotkin upper bound

Let \(C=\{x_1,\dots,x_M\}\subseteq\{0,1\}^n\), and let \(d\) be its minimum distance. If the \(j\)-th coordinate has \(a_j\) ones, then
\[
\sum_{1\le i<k\le M}d_H(x_i,x_k)
 =\sum_{j=1}^n a_j(M-a_j)
 \le n\left\lfloor\frac{M^2}{4}\right\rfloor.
\]
Since the left side is at least \(\binom M2d\),
\[
\frac dn\le
\frac{2\lfloor M^2/4\rfloor}{M(M-1)}.
\]
After dividing by \(2\),
\[
\tau_2(M)\le
\frac{\lfloor M^2/4\rfloor}{M(M-1)}
 =
 \begin{cases}
 \displaystyle\frac{M}{4(M-1)},&M\ \text{even},\\[6pt]
 \displaystyle\frac{M+1}{4M},&M\ \text{odd}.
 \end{cases}
\]

### Attainment

Let \(w=\lfloor M/2\rfloor\). Take one coordinate for every \(w\)-subset of \([M]\), with codeword \(i\) having a \(1\) in coordinate \(A\) exactly when \(i\in A\). Every pair of codewords then has relative distance
\[
\frac{2\binom{M-2}{w-1}}{\binom Mw}
 =\frac{2w(M-w)}{M(M-1)}.
\]
This equals
\[
\begin{cases}
\displaystyle\frac{M}{2(M-1)},&M\ \text{even},\\[6pt]
\displaystyle\frac{M+1}{2M},&M\ \text{odd}.
\end{cases}
\]
Repeating all coordinates removes the negligible ceiling in the two-point radius. Hence the Plotkin bound is attained asymptotically, and
\[
\boxed{\;
\tau_2(M)=
 \begin{cases}
 \displaystyle\frac{M}{4(M-1)},&M\ \text{even},\\[6pt]
 \displaystyle\frac{M+1}{4M},&M\ \text{odd}.
 \end{cases}}
\]

In particular, \(\tau_2=\lim_{M\to\infty}\tau_2(M)=1/4\), and
\[
\tau_2(M)-\frac14=
 \begin{cases}
 \displaystyle\frac1{4(M-1)},&M\ \text{even},\\[6pt]
 \displaystyle\frac1{4M},&M\ \text{odd}.
 \end{cases}
\]
Inverting this relation gives
\[
\boxed{\operatorname{maxcode}_2(\varepsilon)
      =\frac1{4\varepsilon}+O(1).}
\]

## 3. Contradiction with the extracted coefficient

The catalog’s displayed formula gives
\[
c_2=2^{-1}\binom21=1.
\]
It therefore predicts
\[
\operatorname{maxcode}_2(\varepsilon)
 =\frac1{\varepsilon}+O(1),
\]
whereas the exact calculation gives
\[
\operatorname{maxcode}_2(\varepsilon)
 =\frac1{4\varepsilon}+O(1).
\]
The difference \(3/(4\varepsilon)\) is unbounded and cannot be absorbed into \(O(1)\). Thus the conjecture as extracted is false.

## 4. Likely transcription error and remaining open problem

For the additive-radius normalization, the balanced-column construction for \(L=2m\) has first-order coefficient
\[
\widetilde c_L
 =\frac{m}{2^{2m+1}}\binom{2m}{m}
 =2^{-L-1}\left\lfloor\frac L2\right\rfloor
   \binom{L}{\lfloor L/2\rfloor}.
\]
For \(L=2\), this gives \(\widetilde c_2=1/4\), exactly as required.

Thus it is very plausible that an expression of the form
\[
2^{-L-1}\left\lfloor\frac L2\right\rfloor
\binom{L}{\lfloor L/2\rfloor}
\]
was mistranscribed as
\[
2^{-\lfloor L/2\rfloor}\binom{L}{\lfloor L/2\rfloor}.
\]
I have not independently checked the source TeX here, so this diagnosis should be verified against it. If the former is the intended constant, then the \(L=2\) case is correct, and the exact-leading-constant problem for even \(L\ge4\) is not resolved by the argument above.