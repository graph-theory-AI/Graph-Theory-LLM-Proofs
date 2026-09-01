```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A Turán–Plotkin sandwich proves asymptotic equality from above the threshold in a broad regime and gives infinite exact families, while the principal below-threshold interpretation remains unresolved.",
  "would_publish": false,
  "caveats": "The words “close” and “near” are unquantified; no general comparison is proved when s/r approaches the threshold from below."
}
```

## 1. Precise formulation and a parameter correction

Let \(n=q+1\), where \(q\ge 2\), and put
\[
t_q=1-\frac1q.
\]
For an \((r,s)\)-coloring, write \(G_i\) for the graph formed by the edges receiving color \(i\).

Under the definitions in the prompt, the relevant \(q\)-ary code has minimum Hamming distance at least \(s\), not \(r-s\). Indeed, carried colors correspond to coordinates in which two codewords differ. A convention parametrized by maximum agreement would instead use \(r-s\).

Let \(A_q(r,s)\) denote the maximum size of a code in \([q]^r\) with minimum Hamming distance at least \(s\).

### Proposition 1
\[
R'(q+1;r,s)=A_q(r,s)+1.
\]

### Proof

Suppose an \((r,s)\)-coloring on vertex set \(V\) has \(\chi(G_i)\le q\) for every \(i\). Choose a proper coloring
\[
\phi_i:V\longrightarrow [q]
\]
of each \(G_i\), and associate to \(v\in V\) the word
\[
x_v=(\phi_1(v),\ldots,\phi_r(v)).
\]
If \(uv\) receives color \(i\), then \(\phi_i(u)\ne\phi_i(v)\). Since \(uv\) receives \(s\) colors, \(d_H(x_u,x_v)\ge s\). Thus \(\{x_v:v\in V\}\) is a \(q\)-ary code of size \(|V|\).

Conversely, given a code \(\{x_v:v\in V\}\subseteq[q]^r\) with minimum distance at least \(s\), assign to each edge \(uv\) any \(s\) coordinates on which \(x_u\) and \(x_v\) differ. For each coordinate \(i\), the resulting color graph is a subgraph of the complete \(q\)-partite graph whose parts are the sets \(\{v:x_v(i)=a\}\). Hence its chromatic number is at most \(q\). This proves the equality. \(\square\)

---

## 2. The Turán–Plotkin sandwich

Define
\[
\rho_q(N)=\frac{e(T_q(N))}{\binom N2},
\]
where \(T_q(N)\) is the balanced complete \(q\)-partite Turán graph, and, when \(s/r>t_q\), let
\[
P_q(r,s)=\max\left\{N\ge2:\frac sr\le \rho_q(N)\right\}.
\]

### Proposition 2
If \(s/r>t_q\), then
\[
A_q(r,s)+1=R'(q+1;r,s)
   \le R(q+1;r,s)
   \le P_q(r,s)+1.
\]

### Proof

Suppose an \((r,s)\)-coloring of \(K_N\) has no monochromatic \(K_{q+1}\). Every \(G_i\) is then \(K_{q+1}\)-free, so Turán's theorem gives
\[
s\binom N2=\sum_{i=1}^r e(G_i)
 \le r\,e(T_q(N)).
\]
Consequently \(s/r\le\rho_q(N)\), proving the upper bound.

The identical numerical inequality is the usual Plotkin bound for \(q\)-ary codes: in one coordinate, the number of separated pairs of codewords is at most \(e(T_q(N))\), and summing over all coordinates gives
\[
s\binom N2\le r\,e(T_q(N)).
\]
\(\square\)

Since
\[
e(T_q(N))\le \frac{t_qN^2}{2},
\]
we obtain a particularly simple bound.

### Corollary 3
If
\[
\frac sr=t_q+\varepsilon,\qquad \varepsilon>0,
\]
then
\[
R(q+1;r,s)\le \left\lfloor\frac{t_q}{\varepsilon}\right\rfloor+2.
\]

Indeed, an avoiding coloring on \(N\) vertices would satisfy
\[
t_q+\varepsilon
 \le\frac{t_qN}{N-1},
\]
and hence \(N\le1+t_q/\varepsilon\).

---

## 3. Asymptotic equality when the threshold is approached from above

The preceding upper bound is asymptotically attained by codes, provided the length is sufficiently large compared with the distance from the threshold.

### Theorem 4
Fix \(q\ge2\). Suppose
\[
\frac sr=t_q+\varepsilon<1,
\]
and let \(0<\eta<1\). Set
\[
m=q\left\lfloor \frac{(1-\eta)t_q}{q\varepsilon}\right\rfloor.
\]
Assume \(m\ge q\) and
\[
\binom m2 e^{-2\eta^2\varepsilon^2r}<1.
\]
Then
\[
m+1\le R'(q+1;r,s)\le R(q+1;r,s)
 \le \left\lfloor\frac{t_q}{\varepsilon}\right\rfloor+2.
\]

### Proof

For each of the \(r\) coordinates, independently choose a uniformly random balanced map
\[
f_i:[m]\longrightarrow[q],
\]
with every fiber of size \(m/q\). For a fixed pair \(u,v\), the probability that \(f_i(u)\ne f_i(v)\) is
\[
p_m=\frac{e(T_q(m))}{\binom m2}
    =\frac{t_qm}{m-1}
    =t_q+\frac{t_q}{m-1}.
\]
Since
\[
m\le\frac{(1-\eta)t_q}{\varepsilon},
\]
we have
\[
p_m-\left(t_q+\varepsilon\right)
  =\frac{t_q}{m-1}-\varepsilon
  >\frac{t_q}{m}-\varepsilon
  \ge\frac{\varepsilon}{1-\eta}-\varepsilon
  \ge\eta\varepsilon.
\]
The distance between the words corresponding to \(u\) and \(v\) is distributed as \(\operatorname{Bin}(r,p_m)\). Hoeffding's inequality therefore gives
\[
\Pr\bigl(d_H(x_u,x_v)<s\bigr)
 \le e^{-2\eta^2\varepsilon^2r}.
\]
The union bound over the \(\binom m2\) pairs shows that a code of size \(m\) and minimum distance at least \(s\) exists. Proposition 1 gives the lower bound; Corollary 3 gives the upper bound. \(\square\)

### Asymptotic consequence

Let \(q\) be fixed and suppose
\[
\varepsilon\to0^+,
\qquad
\frac{r\varepsilon^2}{\log(1/\varepsilon)}\longrightarrow\infty.
\]
Then
\[
\frac{R(q+1;r,s)}{R'(q+1;r,s)}\longrightarrow1
\qquad
\left(\frac sr=t_q+\varepsilon\right).
\]

To see this, choose \(\eta\to0\) slowly enough that
\[
\eta^2r\varepsilon^2\gg\log(1/\varepsilon).
\]
Theorem 4 then gives
\[
R'\ge (1-o(1))\frac{t_q}{\varepsilon},
\qquad
R\le (1+o(1))\frac{t_q}{\varepsilon}.
\]

Thus a natural ratio formulation of the conjecture is true on a substantial one-sided neighborhood above the Turán density.

---

## 4. Infinite exact families approaching the threshold

There are also infinitely many parameter sets for which \(R=R'\) exactly.

### Theorem 5
Fix \(q\ge2\), let \(M=qa\) with \(a\ge2\), and let
\[
L=\frac{M!}{(a!)^q}.
\]
For any positive integer \(k\), set
\[
r=kL,\qquad
s=kL\,\frac{M-a}{M-1}.
\]
Then \(s\) is an integer and
\[
R(q+1;r,s)=R'(q+1;r,s)=M+1.
\]

Moreover,
\[
\frac sr=\frac{t_qM}{M-1}\longrightarrow t_q
\]
as \(a\to\infty\).

### Proof

Take as coordinates all balanced maps \(f:[M]\to[q]\), each repeated \(k\) times. For any pair \(u,v\), the proportion of these maps separating \(u\) and \(v\) is
\[
1-\frac{a-1}{M-1}
 =\frac{M-a}{M-1}
 =\frac{t_qM}{M-1}.
\]
Thus the \(M\) resulting codewords have pairwise distance exactly \(s\), proving \(R'>M\).

On the other hand, for every \(N>M\),
\[
\rho_q(N)
 \le\frac{t_qN}{N-1}
 <\frac{t_qM}{M-1}
 =\frac sr.
\]
Proposition 2 therefore gives \(R\le M+1\), and all three quantities are equal. \(\square\)

This gives exact equality along ratios converging to the Turán density from above, although the lengths \(r\) in this construction are highly divisible.

---

## 5. The exact threshold for triangles

The boundary case \(n=3\), \(s/r=1/2\), admits a separate linear upper bound.

### Theorem 6
For every even \(r\),
\[
R(3;r,r/2)\le4r+1.
\]
Furthermore,
\[
A_2(r,r/2)\le2r.
\]
If \(r=2^m\), then
\[
R'(3;r,r/2)=2r+1
\]
and consequently
\[
2r+1\le R(3;r,r/2)\le4r+1,
\qquad
\frac{R(3;r,r/2)}{R'(3;r,r/2)}<2.
\]

### Proof

We need two lemmas.

#### Triangle-free graphs are close to a cut

If \(G\) is triangle-free on \(N\) vertices with \(e\) edges, then \(G\) has a bipartition with at most
\[
\frac{N^2}{4}-e
\]
internal edges.

For a vertex \(v\), its neighborhood is independent. Hence the cut
\[
\bigl(N(v),V(G)\setminus N(v)\bigr)
\]
contains \(\sum_{u\in N(v)}d(u)\) crossing edges. Averaging over \(v\), some such cut has at least
\[
\frac1N\sum_u d(u)^2
 \ge\frac{4e^2}{N^2}
\]
crossing edges. Thus the number of internal edges is at most
\[
e-\frac{4e^2}{N^2}
 =\frac{4e}{N^2}\left(\frac{N^2}{4}-e\right)
 \le\frac{N^2}{4}-e.
\]

#### A Gram-matrix estimate

Let \(z_1,\ldots,z_N\) be unit vectors in \(\mathbb R^r\), and put
\[
P=\sum_{u\ne v}\max\{\langle z_u,z_v\rangle,0\}.
\]
If \(P\le N\), then \(N\le4r\).

Indeed, let \(H\) be their Gram matrix and let
\[
Q=\sum_{u\ne v}\max\{-H_{uv},0\}.
\]
Since \(H\) is positive semidefinite,
\[
0\le\mathbf1^TH\mathbf1=N+P-Q,
\]
so \(Q\le N+P\). Since \(|H_{uv}|\le1\),
\[
\operatorname{tr}(H^2)
 \le N+P+Q
 \le2(N+P)\le4N.
\]
Therefore
\[
\operatorname{rank}H
 \ge\frac{(\operatorname{tr}H)^2}{\operatorname{tr}(H^2)}
 \ge\frac N4.
\]
As \(\operatorname{rank}H\le r\), this gives \(N\le4r\).

Now suppose an \((r,r/2)\)-coloring of \(K_N\) has no monochromatic triangle. Every \(G_i\) is triangle-free. Choose for each \(G_i\) a bipartition with \(b_i\) internal edges, where
\[
b_i\le\frac{N^2}{4}-e(G_i).
\]
Since every edge lies in \(r/2\) color graphs,
\[
\sum_i e(G_i)=\frac r2\binom N2=\frac{rN(N-1)}4.
\]
Consequently
\[
\sum_i b_i
 \le\frac{rN^2}{4}-\frac{rN(N-1)}4
 =\frac{rN}{4}.
\]

Represent the two sides of the \(i\)-th bipartition by signs \(\pm1\). Each vertex \(v\) thereby gives a unit vector
\[
z_v\in\{\pm r^{-1/2}\}^r.
\]
For a pair \(u,v\), let \(b_{uv}\) be the number of carried colors whose chosen bipartition puts \(u,v\) on the same side. At least \(r/2-b_{uv}\) coordinates separate them, so
\[
\langle z_u,z_v\rangle\le\frac{2b_{uv}}r.
\]
It follows that
\[
P
 \le\frac4r\sum_{\{u,v\}}b_{uv}
 =\frac4r\sum_i b_i
 \le N.
\]
The Gram-matrix estimate gives \(N\le4r\), proving \(R(3;r,r/2)\le4r+1\).

For a binary code of minimum distance at least \(r/2\), the corresponding sign vectors have pairwise nonpositive inner products. Applying the same Gram argument with \(P=0\) gives \(A_2(r,r/2)\le2r\).

Finally, when \(r=2^m\), index the coordinates by \(x\in\mathbb F_2^m\) and take all affine functions
\[
x\longmapsto a\cdot x+b,
\qquad a\in\mathbb F_2^m,\ b\in\mathbb F_2.
\]
There are \(2r\) such words. Two distinct affine functions differ either everywhere or on exactly half the coordinates. Hence this is a code of size \(2r\) and minimum distance \(r/2\), proving
\[
A_2(r,r/2)=2r.
\]
Proposition 1 completes the proof. \(\square\)

Exact equality cannot be expected for every individual parameter set: for example,
\[
R(3;2,1)=6,\qquad R'(3;2,1)=A_2(2,1)+1=5.
\]

---

## 6. What remains open

The principal unresolved case is
\[
\frac sr=t_q-\varepsilon,
\qquad \varepsilon\to0^+,
\]
especially if “close” is intended in the sense \(R/R'\to1\), or even equality of logarithmic asymptotics.

A random \(q\)-ary code gives the elementary lower bound
\[
R'(q+1;r,s)\ge \exp(\Omega(r\varepsilon^2)):
\]
for \(M\) random words, a fixed pair has distance \(\operatorname{Bin}(r,t_q)\), so
\[
\Pr(d_H<s)\le e^{-2\varepsilon^2r},
\]
and the union bound works for \(M=\exp(c\varepsilon^2r)\). Since \(R\ge R'\), this is also a lower bound for \(R\). The Turán–Plotkin upper bound, however, becomes infinite at or below \(t_q\), and the arguments above provide no matching upper bound in that regime.

Thus the informal conjecture is not resolved as stated. What is proved here is:

1. ratio asymptotic equality from above under  
   \(r\varepsilon^2\gg\log(1/\varepsilon)\);
2. infinitely many exact equality families approaching the threshold from above;
3. a linear upper bound at the exact threshold for \(n=3\), yielding a factor-\(2\) comparison along \(r=2^m\).

The below-threshold fixed-\(n\) regime remains the substantive gap.