```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Controlled metric growth gives a logarithmic list-colouring bound, with an optimal leading term under polynomial growth, but the unrestricted maximum-degree conjecture is not resolved.",
  "would_publish": false,
  "caveats": "The proof requires a growth hypothesis; novelty and current literature status have not been checked."
}
```

## 1. Partial result

All graphs below are finite and simple. Write \(\operatorname{ch}(G)\) for the list chromatic number, and put
\[
B_r(v)=\{w:\operatorname{dist}_G(v,w)\le r\},
\qquad
M_r=\max_{v\in V(G)}|B_r(v)|.
\]
Logarithms without a subscript are natural.

I verified the compatibility calculation in the previous attempt’s bandwidth argument. The construction below uses the same principle—locally consistent palettes—but replaces interval minima by **truncated exponential clocks on graph balls**. No bandwidth or tree partition is assumed.

### Theorem 1: polynomial growth

For every fixed \(d\ge0\), there is a constant \(C_d\) such that the following holds. If \(G\) is bipartite and
\[
|B_r(v)|\le K(r+1)^d
\qquad\text{for every vertex \(v\) and integer \(r\ge0\),}
\tag{1}
\]
where \(K\ge2\), then
\[
\boxed{\operatorname{ch}(G)
\le \log_2 K+2d\log_2\log_2 K+C_d.}
\tag{2}
\]

The leading coefficient \(1\) of \(\log_2 K\) is best possible, even for complete bipartite graphs.

Consequently, if \(C,a,d\) are fixed, \(a>0\), and
\[
|B_r(v)|\le C(\Delta+2)^a(r+1)^d
\tag{3}
\]
holds uniformly, then
\[
\operatorname{ch}(G)
\le a\log_2(\Delta+2)
   +2d\log_2\log_2(\Delta+2)
   +O_{C,a,d}(1).
\tag{4}
\]
Thus the conjectured order holds in this class, without a restriction on \(|V(G)|\).

The method also handles a broader, fixed-rate exponential-growth condition:

### Theorem 2: fixed-rate exponential growth

For every fixed \(\lambda\ge0\),
\[
M_r\le K e^{\lambda r}\quad(r\ge0),\qquad K\ge2,
\tag{5}
\]
implies
\[
\boxed{\operatorname{ch}(G)=O_\lambda(\log K).}
\tag{6}
\]
In particular, \(K\le C(\Delta+2)^a\), with \(C,a,\lambda\) fixed, again gives \(O(\log\Delta)\).

These are restricted results, not a resolution of the conjecture.

---

## 2. A finite-range colouring criterion

The main ingredient is the following explicit bound.

### Lemma

Let \(G\) be bipartite. Let \(R\) be a positive integer and \(\beta>0\), and suppose
\[
p:=\frac12\left(e^{-2\beta}-M_R e^{-\beta R}\right)>0.
\tag{7}
\]
Then
\[
\boxed{
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln M_{2R}}{-\ln(1-p)}
\right\rceil .
}
\tag{8}
\]

The significant feature is that the dependency bound will be \(M_{2R}-1\), with **no factor involving the list size or global colour frequency**.

### 2.1 An exponential-gap identity

Let \(W\) be a finite nonempty set. For \(w\in W\), let \(X_w\) be independent exponential random variables of rate \(\beta\). Let \(a_w\ge0\), with at least one \(a_w=0\).

Consider the scores \(X_w-a_w\), together with a dummy score \(0\). For \(t\ge0\),
\[
\Pr\!\left(
\text{some score exceeds every other score and \(0\) by more than \(t\)}
\right)
=e^{-\beta t}.
\tag{9}
\]

Indeed, condition on all variables other than \(X_w\), and write
\[
H_w=\max\left(\{0\}\cup\{X_z-a_z:z\ne w\}\right).
\]
Since \(a_w+H_w\ge0\),
\[
\begin{aligned}
\Pr(X_w-a_w>H_w+t\mid (X_z)_{z\ne w})
&=e^{-\beta(a_w+H_w+t)}\\
&=e^{-\beta t}
  \Pr(X_w-a_w>H_w\mid (X_z)_{z\ne w}).
\end{aligned}
\]
Summing over \(w\) proves (9): the maximum score is positive and unique almost surely, because some \(a_w=0\).

### 2.2 Construction and properness

Fix a bipartition \(A\cup B\) and an arbitrary assignment of lists of size \(k\). For every listed colour \(c\) and every graph vertex \(w\), independently choose

- an exponential random variable \(X_{c,w}\) of rate \(\beta\);
- a fair bit \(\eta_{c,w}\in\{A,B\}\).

Set
\[
Y_{c,w}=\min\{X_{c,w},R\}.
\]

At a vertex \(v\), examine the scores
\[
s_{c,v}(w)=Y_{c,w}-\operatorname{dist}(v,w),
\qquad w\in B_R(v),
\]
together with the dummy score \(0\).

Call \(w\) a **clear winner** for \(c\) at \(v\) if
\[
s_{c,v}(w)>
2+\max\left(
\{0\}\cup
\{s_{c,v}(z):z\in B_R(v),\ z\ne w\}
\right).
\tag{10}
\]
There is at most one clear winner. Declare \(c\in L(v)\) **available** if a clear winner exists and its bit is the side containing \(v\).

Any choice of available colours is proper. To see this, first observe that vertices outside \(B_R(v)\), in the same connected component, have scores at most
\[
R-(R+1)=-1.
\]
Thus a clear winner beats *every* other vertex’s score by more than \(2\), not just those in \(B_R(v)\).

If \(u\) and \(v\) are adjacent, each score changes by at most \(1\) when moving from \(v\) to \(u\). Consequently, a clear winner at \(v\) is the unique maximum-score vertex at \(u\) as well. Its score at \(u\) is positive, so it belongs to \(B_R(u)\).

Therefore, if the same colour \(c\) were available at both endpoints of an edge, their clear winners would coincide. Availability would then require the same bit to equal both \(A\) and \(B\), which is impossible.

### 2.3 Availability probability

Fix \(v\) and \(c\). First use the uncapped clocks \(X_{c,w}\) for \(w\in B_R(v)\), with offsets
\[
a_w=\operatorname{dist}(v,w).
\]
The offset at \(v\) is zero. By (9), the probability of a gap greater than \(2\), also above the dummy score, is exactly \(e^{-2\beta}\).

Capping changes none of these clocks unless some \(X_{c,w}>R\). A union bound gives
\[
\Pr(\exists w\in B_R(v):X_{c,w}>R)
\le |B_R(v)|e^{-\beta R}.
\]
Hence
\[
\Pr(c\text{ has a clear winner at }v)
\ge e^{-2\beta}-M_R e^{-\beta R}.
\]
The winner’s bit is independent of the clocks, so
\[
\Pr(c\text{ is available at }v)\ge p.
\tag{11}
\]

Different colours use independent random variables. Thus the bad event \(E_v\), that \(v\) has no available colour, satisfies
\[
\Pr(E_v)\le(1-p)^k.
\tag{12}
\]

### 2.4 Local lemma

The event \(E_v\) uses variables only at centres in \(B_R(v)\). It is therefore independent of the collection of all events \(E_u\) with
\[
\operatorname{dist}(u,v)>2R.
\]
A dependency graph has maximum degree at most \(M_{2R}-1\).

The symmetric Lovász local lemma applies when
\[
e(1-p)^k M_{2R}\le1.
\]
This is precisely the sufficient condition in (8). Avoiding all bad events and choosing an available colour at each vertex gives a proper list colouring. \(\square\)

---

## 3. Proof of the polynomial-growth bound

Assume (1). Put
\[
L=\ln K,\qquad
\beta=\frac1L,\qquad
R=\left\lceil 2L^2\right\rceil.
\]
For now let \(K\to\infty\), with \(d\) fixed.

The error caused by truncation is small:
\[
\begin{aligned}
M_R e^{-\beta R}
&\le K(R+1)^d e^{-R/L}\\
&\le (2L^2+2)^d e^{-L}\\
&=o_d(L^{-2}).
\end{aligned}
\tag{13}
\]
Consequently, the parameter in (7) satisfies
\[
p=\frac12-\frac1L+O_d(L^{-2}),
\]
and hence
\[
-\ln(1-p)=\ln2-\frac2L+O_d(L^{-2}).
\tag{14}
\]

Meanwhile,
\[
\begin{aligned}
1+\ln M_{2R}
&\le 1+\ln K+d\ln(2R+1)\\
&=L+2d\ln L+O_d(1).
\end{aligned}
\tag{15}
\]
Substitution into (8) gives
\[
\begin{aligned}
\operatorname{ch}(G)
&\le
\frac{L+2d\ln L+O_d(1)}
{\ln2-2/L+O_d(L^{-2})}\\
&=
\frac{L+2d\ln L}{\ln2}+O_d(1)\\
&=\log_2K+2d\log_2\log_2K+O_d(1).
\end{aligned}
\]

This proves the estimate for all sufficiently large \(K\), depending on \(d\). The remaining bounded range is absorbed into \(C_d\): from (1) at radius \(1\),
\[
\Delta+1\le 2^dK,
\]
and the elementary greedy bound is
\(\operatorname{ch}(G)\le\Delta+1\).
Thus every \(K\ge2\) is covered. This proves Theorem 1 and its consequence (4). \(\square\)

Only the estimates on \(M_R\) and \(M_{2R}\) were used. Thus the full growth hypothesis can be weakened to appropriate volume bounds at these two scales.

---

## 4. Proof for fixed-rate exponential growth

Assume (5). Choose
\[
\beta=\lambda+1,
\qquad
R=\left\lceil\ln(2K)+2\beta\right\rceil.
\]
Then
\[
M_R e^{-\beta R}
\le K e^{-(\beta-\lambda)R}
=K e^{-R}
\le \frac12e^{-2\beta}.
\]
Therefore
\[
p\ge p_\lambda:=\frac14e^{-2(\lambda+1)}>0.
\tag{16}
\]
Also,
\[
\begin{aligned}
1+\ln M_{2R}
&\le 1+\ln K+2\lambda R\\
&\le (1+2\lambda)\ln K+O_\lambda(1).
\end{aligned}
\]
The finite-range lemma now gives
\[
\operatorname{ch}(G)
\le
\frac{(1+2\lambda)\ln K+O_\lambda(1)}
{-\ln(1-p_\lambda)}
=O_\lambda(\log K),
\]
as asserted. \(\square\)

Here \(\lambda\) must be fixed across the graph class. Allowing it to grow with \(\Delta\) would not establish the original conjecture.

---

## 5. Sharpness of the polynomial-growth leading term

For completeness, here is a self-contained lower-bound construction. It is not a counterexample to the conjecture.

For every integer \(k\ge2\), set
\[
r=2k^2,\qquad m=r\,2^{k+1}=4k^2 2^k.
\]
There is a sequence of \(m\) \(k\)-subsets of an \(r\)-element colour set with no property B: under every two-colouring of the colour set, at least one of the \(k\)-subsets is monochromatic.

To prove this, choose the \(m\) subsets independently and uniformly. Under any fixed two-colouring, one colour class has size at least \(k^2\). Therefore the probability that a random \(k\)-subset is monochromatic is at least
\[
\begin{aligned}
\frac{\binom{k^2}{k}}{\binom{2k^2}{k}}
&=
2^{-k}\prod_{i=0}^{k-1}
\frac{1-i/k^2}{1-i/(2k^2)}\\
&\ge
2^{-k}\prod_{i=0}^{k-1}(1-i/k^2)\\
&\ge
2^{-k}\left(1-\sum_{i=0}^{k-1}i/k^2\right)\\
&\ge 2^{-k-1}.
\end{aligned}
\]
The probability that a fixed two-colouring makes none of the \(m\) subsets monochromatic is at most
\[
e^{-m2^{-k-1}}=e^{-r}.
\]
A union bound over all \(2^r\) two-colourings gives
\[
2^r e^{-r}<1.
\]
The required sequence therefore exists; repeated subsets cause no difficulty.

Assign these \(m\) lists to each side of \(K_{m,m}\), using the same list sequence on both sides. A proper list colouring would yield a property-B partition: let \(S\) be the set of colours used on the first side. No colour in \(S\) can be used on the other side, so every list must meet both \(S\) and its complement. This is a contradiction.

Thus
\[
\operatorname{ch}(K_{m,m})>k,
\qquad
\log_2 m=k+2\log_2 k+2.
\]
In particular,
\[
\operatorname{ch}(K_{m,m})
\ge \log_2 m-2\log_2\log_2 m-O(1).
\tag{17}
\]

For \(K_{m,m}\), every ball has at most \(2m\) vertices. Consequently, (1) holds with \(K=2m\) for every fixed \(d\ge0\). Equation (17) shows that the coefficient \(1\) of \(\log_2K\) in Theorem 1 cannot be decreased.

---

## 6. What remains unresolved

The missing step is removal of the growth hypothesis.

For example, at the root of a sufficiently deep finite tree whose internal vertices have degree \(\Delta\),
\[
|B_r(v)|
=
1+\Delta\sum_{j=0}^{r-1}(\Delta-1)^j.
\tag{18}
\]
For fixed \(r>a\), this exceeds
\[
C(\Delta+2)^a(r+1)^d
\]
as \(\Delta\to\infty\), for any fixed \(C,a,d\). Thus controlled polynomial growth with a polynomial-in-\(\Delta\) prefactor is not automatic even for bipartite graphs. These trees are themselves \(2\)-choosable; they illustrate a limitation of the hypothesis, not a counterexample.

The finite-range criterion also identifies the quantitative obstruction. When \(M_R\) behaves like \((\Delta-1)^R\), making
\[
e^{-2\beta}-M_Re^{-\beta R}>0
\]
forces \(\beta\) to be of order \(\ln\Delta\). The resulting availability guarantee is then no longer a positive absolute constant. Taking a radius large enough to encompass an entire component instead recovers a bound in terms of its order, not its maximum degree.

Hence this argument establishes logarithmic choosability for controlled-growth classes, including an asymptotically sharp polynomial-growth estimate, but supplies neither a universal constant \(c\) nor a counterexample to the original conjecture.

Finally, the supplied discussion’s claim of a lower bound for **every** graph solely from its maximum degree is false as written: stars have arbitrarily large maximum degree and choice number \(2\). Nothing above uses that assertion.