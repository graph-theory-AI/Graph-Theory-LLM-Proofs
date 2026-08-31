```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted extremal function remains undetermined, but finite-order and bounded-dual-scale upper bounds follow, and the quoted logarithmic lower bound is inconsistent with its claimed consequence under standard notation.",
  "would_publish": false,
  "caveats": "No matching upper bound for fixed r>=4; one argument uses the maximum-degree estimate quoted in the prompt, and the source's logarithmic notation needs verification."
}
```

## 1. Extremal formulation

For finite graphs, define
\[
F_r(d):=\sup\{\chi_f(G):G\text{ is }d\text{-degenerate and }K_r\text{-free}\}.
\]
Using a supremum is technically safer than “maximum,” since no attainment result is supplied. Throughout, \(r\) is fixed unless stated otherwise.

The immediate bounds are
\[
1\le F_r(d)\le d+1.
\]
The upper bound follows from greedy \((d+1)\)-colorability.

There are some exact regimes:

- \(F_2(d)=1\), since a \(K_2\)-free graph is edgeless.
- If \(d\le r-2\), then
  \[
  F_r(d)=d+1,
  \]
  attained by \(K_{d+1}\), which is \(K_r\)-free.
- In particular, \(F_r(1)=2\) for every \(r\ge3\).

Thus the asymptotic question only makes sense with \(r\) fixed and \(d\to\infty\).

The functions are nondecreasing in both parameters. Moreover, joining with a clique gives
\[
F_{r+s}(d+s)\ge F_r(d)+s. \tag{1}
\]
Indeed, if \(G\) is \(d\)-degenerate and \(K_r\)-free, then \(K_s\vee G\) is \(K_{r+s}\)-free, has degeneracy at most \(d+s\), and
\[
\chi_f(K_s\vee G)=s+\chi_f(G).
\]

## 2. A necessary correction to the quoted lower bound

Under standard notation,
\[
\log^{r-2}d=(\log d)^{r-2}.
\]
Read this way, the quoted lower bound
\[
\Omega_r\!\left(\frac d{(\log d)^{r-2}}\right)
\]
does **not** rule out
\[
O_r\!\left(\frac{d\log\log d}{\log d}\right).
\]
Indeed, for \(r\ge4\),
\[
\frac{d/(\log d)^{r-2}}{d\log\log d/\log d}
=
\frac1{(\log d)^{r-3}\log\log d}\longrightarrow0.
\]

There is a second inconsistency. The case \(r=3\) of the quoted theorem gives
\[
F_3(d)=\Omega(d/\log d).
\]
Since every triangle-free graph is \(K_r\)-free for every \(r\ge3\),
\[
F_r(d)\ge F_3(d)=\Omega(d/\log d). \tag{2}
\]
Thus, for \(r>3\), the literal bound \(d/(\log d)^{r-2}\) is weaker than the bound inherited from the triangle-free case.

Possibilities include that the intended notation was an iterated logarithm
\(\log^{\circ(r-2)}d\), or perhaps a power such as
\((\log d)^{1/(r-2)}\). Either could be compatible with the sentence about disproving the maximum-degree analogy. The actual statement of Theorem 1.6 must therefore be checked before its claimed consequence can be used.

The rest of this writeup does not assume a correction.

## 3. An elementary finite-order upper bound

The following bound is independent of degeneracy.

### Proposition 3.1

For every fixed \(r\ge3\), every \(n\)-vertex \(K_r\)-free graph satisfies
\[
\chi_f(G)\le C_r n^{(r-2)/(r-1)}. \tag{3}
\]

### Proof

The dual linear program for fractional chromatic number is
\[
\chi_f(G)=
\max\left\{
\sum_{v\in V(G)}w(v):
w(v)\ge0,\quad
\sum_{v\in I}w(v)\le1
\text{ for every independent }I
\right\}. \tag{4}
\]

Fix a feasible \(w\). In particular, \(w(v)\le1\) for every \(v\). For \(t\in(0,1]\), let
\[
S_t=\{v:w(v)\ge t\}
\quad\text{and}\quad
k(t)=\lfloor 1/t\rfloor+1.
\]
The graph \(G[S_t]\) cannot contain an independent set of size \(k(t)\), since such a set would have weight at least \(k(t)t>1\). It is also \(K_r\)-free. Hence
\[
|S_t|<R(r,k(t)).
\]
The elementary Ramsey recursion gives
\[
R(r,k)\le \binom{r+k-2}{r-1}=O_r(k^{r-1}),
\]
and consequently
\[
|S_t|\le \min\{n,C_r t^{-(r-1)}\}. \tag{5}
\]

By the layer-cake identity,
\[
\sum_v w(v)=\int_0^1 |S_t|\,dt.
\]
Splitting the integral at \(t_0=(C_r/n)^{1/(r-1)}\), and adjusting constants when \(t_0>1\), gives
\[
\sum_vw(v)
\le nt_0+C_r\int_{t_0}^1t^{-(r-1)}\,dt
=O_r\!\left(n^{(r-2)/(r-1)}\right).
\]
Taking the maximum in (4) proves (3). ∎

Consequently, every \(n\)-vertex graph in the problem satisfies
\[
\chi_f(G)\le
\min\left\{d+1,\ C_r n^{(r-2)/(r-1)}\right\}. \tag{6}
\]
For example, if \(n=O(d)\), then
\[
\chi_f(G)=O_r\!\left(d^{(r-2)/(r-1)}\right)=o(d).
\]
More generally, a graph with \(\chi_f(G)\ge t\) must have
\[
n=\Omega_r\!\left(t^{(r-1)/(r-2)}\right). \tag{7}
\]
This does not control \(F_r(d)\), because the order is unrestricted.

## 4. Hall-ratio bound obtained by truncating high degrees

Define the Hall ratio
\[
\rho(G):=\max_{\varnothing\ne X\subseteq V(G)}
\frac{|X|}{\alpha(G[X])}.
\]
Always
\[
\rho(G)\le\chi_f(G),
\]
and the reverse inequality is false in general. This distinction is central here.

Using the maximum-degree \(K_r\)-free coloring bound quoted in the question gives the following.

### Proposition 4.1

For fixed \(r\) and sufficiently large \(d\), every \(d\)-degenerate \(K_r\)-free graph satisfies
\[
\rho(G)=O_r\!\left(\frac{d\log\log d}{\log d}\right). \tag{8}
\]

### Proof

Let \(H\) be any nonempty induced subgraph of \(G\), with \(m\) vertices. Degeneracy gives
\[
e(H)\le dm,
\]
so the average degree of \(H\) is at most \(2d\). Therefore at least \(m/2\) vertices of \(H\) have degree at most \(4d\). Let \(L\) be this set. Then
\[
|L|\ge m/2,\qquad \Delta(H[L])\le4d.
\]

The maximum-degree estimate quoted in the prompt gives
\[
\chi(H[L])
=O_r\!\left(\frac{d\log\log d}{\log d}\right).
\]
Thus \(H[L]\), and hence \(H\), has an independent set of size
\[
\Omega_r\!\left(\frac{m\log d}{d\log\log d}\right).
\]
Taking the maximum over induced subgraphs proves (8). ∎

This proves that the natural maximum-degree estimate controls all **uniformly weighted induced subgraphs**. It does not bound arbitrary dual weightings and therefore does not settle the fractional problem.

A standard quantitative form of this obstruction is useful.

### Lemma 4.2

Every \(n\)-vertex graph satisfies
\[
\chi_f(G)\le H_n\,\rho(G), \tag{9}
\]
where \(H_n=1+\frac12+\cdots+\frac1n\le1+\log n\).

### Proof

For an arbitrary nonnegative weighting, order the vertices so that
\[
w_1\ge w_2\ge\cdots\ge w_n.
\]
For each prefix \(X_i=\{v_1,\ldots,v_i\}\), there is an independent set of size at least \(i/\rho(G)\), and hence of weight at least
\[
\frac{i w_i}{\rho(G)}.
\]
Let \(M=\max_i iw_i\). Then
\[
\alpha_w(G)\ge\frac M{\rho(G)}
\]
and
\[
w(V)=\sum_{i=1}^nw_i\le M\sum_{i=1}^n\frac1i=M H_n.
\]
Therefore \(w(V)/\alpha_w(G)\le \rho(G)H_n\). Taking the dual maximum proves (9). ∎

Combining (8) and (9),
\[
\chi_f(G)
=
O_r\!\left(
\frac{d\log\log d}{\log d}(1+\log n)
\right). \tag{10}
\]
Together with (3) and the greedy bound, this gives the finite-order envelope
\[
\boxed{
\chi_f(G)\le
\min\left\{
d+1,\;
C_r n^{(r-2)/(r-1)},\;
C'_r\frac{d\log\log d}{\log d}(1+\log n)
\right\}.
} \tag{11}
\]

In particular, if \(t=\chi_f(G)\) substantially exceeds the maximum-degree scale, then
\[
\log n
\ge
\Omega_r\!\left(
\frac{t\log d}{d\log\log d}
\right)-O(1). \tag{12}
\]

## 5. Bounded-scale dual weightings obey the anticipated bound

The Hall-ratio argument can also isolate what a putative extremal dual weighting must look like.

Given a nonzero weighting \(w\), let \(L(w)\) be the number of nonempty dyadic classes
\[
S_j=\{v:2^{-j-1}M<w(v)\le2^{-j}M\},
\qquad M=\max_vw(v).
\]

### Proposition 5.1

For every weighting \(w\),
\[
\frac{w(V)}{\alpha_w(G)}
\le 2\,\rho(G)\,L(w). \tag{13}
\]

### Proof

For every nonempty \(S_j\), choose an independent set
\(I_j\subseteq S_j\) of size at least \(|S_j|/\rho(G)\). Then
\[
w(I_j)
\ge
2^{-j-1}M\frac{|S_j|}{\rho(G)}
\ge
\frac{w(S_j)}{2\rho(G)}.
\]
Some dyadic class has weight at least \(w(V)/L(w)\), proving (13). ∎

Therefore, if an optimal dual weighting has only \(L=O_r(1)\) occupied scales, then
\[
\chi_f(G)
=O_r\!\left(\frac{d\log\log d}{\log d}\right). \tag{14}
\]
More generally, if its positive weights have ratio at most \(Q\), then
\[
\chi_f(G)
=
O_r\!\left(
\frac{d\log\log d}{\log d}(1+\log Q)
\right). \tag{15}
\]

Conversely, if \(t=\chi_f(G)\), every optimal dual weighting must satisfy
\[
L(w)
\ge
\Omega_r\!\left(
\frac{t\log d}{d\log\log d}
\right). \tag{16}
\]
Thus any example genuinely exceeding the maximum-degree analogy must use a highly multiscale dual obstruction, not merely an induced subgraph with small ordinary independence ratio.

As another immediate special case, if \(\Delta(G)=O(d)\), then the maximum-degree theorem quoted in the prompt directly gives
\[
\chi_f(G)\le\chi(G)
=O_r\!\left(\frac{d\log\log d}{\log d}\right).
\]
This includes regular and vertex-transitive examples: a regular \(d\)-degenerate graph has degree at most \(d\).

## 6. Local constraints on an extremal dual weighting

There is also a direct consequence of the degeneracy orientation and \(K_r\)-freeness.

Choose an ordering in which every vertex has at most \(d\) later neighbors, denoted \(N^+(v)\). Let \(w\) be dual-feasible as in (4). Then \(G[N^+(v)]\) is \(K_{r-1}\)-free and has at most \(d\) vertices.

Applying Proposition 3.1 inside \(N^+(v)\) gives
\[
w(N^+(v))\le
\begin{cases}
1, & r=3,\\[2mm]
C_r d^{(r-3)/(r-2)}, & r\ge4.
\end{cases} \tag{17}
\]
For \(r=3\), the forward neighborhood is itself independent.

More precisely, for \(r\ge4\) and \(t\in(0,1]\),
\[
\big|\{u\in N^+(v):w(u)\ge t\}\big|
\le
\min\{d,C_r t^{-(r-2)}\}. \tag{18}
\]
Indeed, otherwise the elementary Ramsey bound would produce either a
\(K_{r-1}\) or an independent set of weight greater than one.

Orienting every edge forward and summing (17), one obtains the weighted edge-energy bound
\[
\sum_{uv\in E(G)}w(u)w(v)
\le
\begin{cases}
w(V), & r=3,\\[2mm]
C_r d^{(r-3)/(r-2)}w(V), & r\ge4.
\end{cases} \tag{19}
\]

Equations (17)–(19) are genuine restrictions on any dual witness for large fractional chromatic number. The missing step is a global argument converting these local, multiscale restrictions into a bound on \(w(V)\). I do not have such an argument; asserting one would amount to solving the open problem.

## 7. Status and remaining gap

The full asymptotic behavior of \(F_r(d)\) for fixed \(r\ge4\) is not resolved here. The established partial conclusions are:

1. The problem is exact when \(d\le r-2\).
2. For bounded order,
   \[
   \chi_f(G)\le C_r n^{(r-2)/(r-1)}.
   \]
3. The Hall ratio always satisfies the maximum-degree-scale bound
   \[
   \rho(G)=O_r(d\log\log d/\log d).
   \]
4. Graphs with bounded maximum degree relative to degeneracy, or with a bounded-scale optimal dual weighting, also satisfy that bound.
5. Any larger fractional chromatic number requires both large order and a strongly multiscale dual weighting.
6. Under the conventional meaning of \(\log^{r-2}d\), the catalog’s displayed lower bound and its claimed implication are incompatible. The actual source notation must be checked before a sharper lower-bound comparison can be made.

No unrestricted \(o(d)\) upper bound for fixed \(r\ge4\), and no matching construction or counterexample, is proved here.