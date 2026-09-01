```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general finite problem remains open, but cubic graphs having a 2-factor with at most two cycles always contain a cycle with at least one seventh as many chords as vertices, and asymptotically one quarter as many.",
  "would_publish": false,
  "caveats": "Finite simple graphs are assumed; the argument does not handle graphs without a bounded-component 2-factor."
}
```

# Mathematical writeup

## 1. Statement and conventions

For a cycle \(C\) in a finite simple graph \(G\), write

\[
\operatorname{ch}_G(C)=|E(G[V(C)])|-|C|
\]

for its number of chords, and set

\[
\rho(G)=\max_C \frac{\operatorname{ch}_G(C)}{|C|}.
\]

The question asks whether

\[
\inf\{\rho(G):\delta(G)\ge 3\}>0.
\]

Finiteness is essential: if infinite graphs are allowed, the infinite \(3\)-regular tree has no cycle at all.

I do not resolve the general finite question. I prove a parameterized special case, with a stronger result when a cubic graph has a 2-factor with at most two components.

## 2. Preliminary facts

### 2.1 Hamiltonian graphs

If \(G\) has minimum degree at least \(3\) and has a Hamilton cycle \(C\) on \(n\) vertices, then every edge of \(G\) has both endpoints on \(C\), and hence

\[
\operatorname{ch}_G(C)=|E(G)|-n\ge \frac{3n}{2}-n=\frac n2.
\]

Thus Hamiltonian graphs satisfy the desired conclusion with \(c=1/2\).

### 2.2 The cubic boundary identity

If \(G\) is cubic, \(C\) is a cycle of length \(\ell\), and

\[
b=|\delta_G(V(C))|,
\]

then

\[
\boxed{\ell=2\operatorname{ch}_G(C)+b.} \tag{1}
\]

Indeed, at every vertex of \(C\), exactly one incident edge is not a cycle edge. A chord is counted at both ends, while an edge leaving \(C\) is counted once.

In particular, if \(G\) is an \(n\)-vertex cubic graph and \(C\) has length \(\ell\), then \(b\le 3(n-\ell)\), so

\[
\operatorname{ch}_G(C)\ge \frac{4\ell-3n}{2}. \tag{2}
\]

Consequently, if the circumference is at least \((3/4+\varepsilon)n\), then some cycle has chord ratio at least

\[
\frac{8\varepsilon}{3+4\varepsilon}.
\]

### 2.3 A constant two-chord input

I use the \(k=3\) case of the Gupta–Kahn–Robertson theorem quoted in the supplied source: every graph of minimum degree at least \(3\) has a cycle with at least two chords. Therefore every \(n\)-vertex such graph satisfies

\[
\rho(G)\ge \frac2n. \tag{3}
\]

This is only used to dispose of finitely many small orders.

---

## 3. Cubic graphs with a two-component 2-factor

### Theorem 1

Let \(G\) be a finite simple cubic graph possessing a 2-factor with at most two components. Then

\[
\boxed{\rho(G)\ge \frac17.}
\]

Moreover, if \(G\) has \(n\ge 8\) vertices, then

\[
\boxed{\rho(G)\ge \frac{n-6}{4(n+4)}.} \tag{4}
\]

Thus, for this class,

\[
\rho(G)\ge \frac14-o(1).
\]

If the 2-factor has one component, it is Hamiltonian, so only the case of two components needs proof.

### 3.1 The matching setup

Let the 2-factor be \(A\cup B\), where \(A,B\) are cycles of lengths \(a,b\), and let \(n=a+b\).

Since \(G\) is cubic,

\[
M=E(G)\setminus E(A\cup B)
\]

is a perfect matching. Let

- \(s_A\) be the number of edges of \(M\) with both ends in \(A\);
- \(s_B\) be the number with both ends in \(B\);
- \(s=s_A+s_B\);
- \(t\) be the number of matching edges between \(A\) and \(B\).

Then

\[
s+t=\frac n2. \tag{5}
\]

The cycles \(A\) and \(B\) themselves have respectively \(s_A\) and \(s_B\) chords. Hence

\[
\rho(G)\ge \max\left\{\frac{s_A}{a},\frac{s_B}{b}\right\}\ge \frac{s}{n}. \tag{6}
\]

### 3.2 Four cycles from two cross-edges

Assume \(t\ge2\), and choose two cross-edges

\[
e=x_1y_1,\qquad f=x_2y_2,
\]

where \(x_1,x_2\in V(A)\) and \(y_1,y_2\in V(B)\).

The vertices \(x_1,x_2\) split \(A\) into two arcs, and \(y_1,y_2\) split \(B\) into two arcs. Choosing one arc from each cycle and adding \(e,f\) gives four cycles. The sum of their lengths is

\[
2a+2b+8=2n+8. \tag{7}
\]

Every other cross-edge between \(A\) and \(B\) is a chord of exactly one of these four cycles. Thus these edges contribute exactly \(t-2\) to the sum of the four chord counts.

We also average the contribution from the \(s\) internal matching edges. Fix an internal matching edge \(uv\) of \(A\). The two \(u\)-\(v\) arcs of \(A\) contain, say, \(r\) and \(t-r\) endpoints of cross-edges. For a uniformly random pair of cross-edges, the probability that their endpoints do not separate \(u\) and \(v\) cyclically is

\[
\frac{\binom r2+\binom{t-r}{2}}{\binom t2}
 \ge \frac{t-2}{2(t-1)}. \tag{8}
\]

Whenever they do not separate \(u,v\), the edge \(uv\) is a chord in two of the four cycles. Its expected contribution to the sum of the four chord counts is therefore at least

\[
\frac{t-2}{t-1}.
\]

The same holds for every internal matching edge in \(A\) or \(B\). Consequently, for some choice of \(e,f\), the sum \(S\) of the chord counts of the four cycles satisfies

\[
S\ge (t-2)+s\frac{t-2}{t-1}
   =\frac{(t-2)(n/2-1)}{t-1}, \tag{9}
\]

where (5) was used. Combining (7) and (9), at least one of the four cycles satisfies

\[
\rho(G)\ge
\frac{(t-2)(n-2)}
     {4(t-1)(n+4)}. \tag{10}
\]

Thus we have the useful bound

\[
\boxed{
\rho(G)\ge
\max\left\{
\frac{s}{n},
\frac{(t-2)(n-2)}{4(t-1)(n+4)}
\right\}.
} \tag{11}
\]

### 3.3 The asymptotic \(1/4\) bound

If \(s/n\ge1/4\), (6) gives \(\rho(G)\ge1/4\).

Otherwise \(t>n/4\). Since \(n\) is even and \(t\) is integral,

\[
t-1\ge\frac{n-2}{4}.
\]

Therefore

\[
\frac{t-2}{t-1}
=1-\frac1{t-1}
\ge 1-\frac4{n-2}
=\frac{n-6}{n-2}.
\]

Substituting this in (10) gives

\[
\rho(G)\ge \frac{n-6}{4(n+4)},
\]

proving (4).

### 3.4 The uniform constant \(1/7\)

The bound in (4) is greater than \(1/7\) for every even \(n\ge20\).

For \(n\le14\), (3) gives

\[
\rho(G)\ge\frac2n\ge\frac17.
\]

It remains to consider \(n=16,18\). Suppose neither factor cycle already has chord ratio at least \(1/7\). Then

\[
s=s_A+s_B<\frac n7.
\]

- If \(n=18\), then \(s\le2\), so \(t\ge7\). Equation (10) gives

  \[
  \rho(G)\ge
  \frac{5\cdot16}{4\cdot6\cdot22}
  =\frac5{33}>\frac17.
  \]

- Let \(n=16\). Then again \(s\le2\).

  * If \(s=0\), then \(t=8\), and (10) gives \(\rho(G)\ge3/20\).
  * If \(s=1\), then \(t=7\), and (10) gives \(\rho(G)\ge7/48\).
  * If \(s=2\), then \(t=6\). If the two internal matching edges lie in the same factor cycle, that factor has length \(10\) and two chords, giving ratio \(1/5\). Otherwise \(s_A=s_B=1\), and \(a=b=8\). In this last case, (9) gives an average total chord count of at least
    \[
    \frac{(6-2)(16/2-1)}{6-1}=\frac{28}{5}
    \]
    among the four lifted cycles. Since the total chord count is integral, some choice of the two cross-edges gives total chord count at least \(6\). Their total length is \(40\), so one cycle has ratio at least \(6/40=3/20\).

This completes the proof of Theorem 1.

---

## 4. A bounded-component 2-factor theorem

The preceding argument gives a weaker but more general parameterized result.

### Theorem 2

Let \(G\) be an \(n\)-vertex graph with

\[
3\le \delta(G)\le \Delta(G)\le d+2,
\]

and suppose \(G\) has a spanning 2-factor with at most \(k\ge2\) components. Put

\[
K=k(k-1).
\]

Then

\[
\rho(G)\ge
\max\left\{
\frac2n,\,
\max\left(0,
\frac{n/d-2K}{2n(K+1)+8K}
\right)
\right\}. \tag{12}
\]

In particular,

\[
\boxed{\rho(G)\ge \frac{1}{4d(K+1)}
       =\frac{1}{4(\Delta(G)-2)(k(k-1)+1)}.} \tag{13}
\]

For fixed \(d,k\), the second term in (12) tends to

\[
\frac{1}{2d(K+1)}
\]

as \(n\to\infty\).

### Proof

Let the factor cycles be \(C_1,\dots,C_r\), with \(r\le k\), and put

\[
H=G-E(C_1\cup\cdots\cup C_r).
\]

Every vertex has degree at least \(1\) and at most \(d\) in \(H\). A maximal matching \(M\) of \(H\) has size at least \(n/(2d)\): every unmatched vertex is adjacent to a matched endpoint, and each matching edge accounts for at most \(2d\) vertices.

Let \(s_i\) be the number of matching edges having both endpoints on \(C_i\), and set

\[
s=\sum_i s_i,\qquad x=\frac{s}{n}.
\]

Some factor cycle has chord ratio at least \(x\).

There are at least

\[
\frac n{2d}-s
\]

matching edges joining distinct factor cycles. These are distributed among at most \(K/2\) unordered pairs of factor cycles. Hence some pair is joined by at least

\[
\frac{(1/d-2x)n}{K}
\]

matching edges.

Choose two such edges. As before, the four cycles obtained from the two factor cycles have total length at most \(2n+8\), and every other matching edge between this pair is a chord in one of them. Therefore

\[
\rho(G)\ge
\max\left\{
x,\,
\frac{(1/d-2x)n/K-2}{2n+8}
\right\}. \tag{14}
\]

The first expression increases with \(x\), while the second decreases. Their intersection is

\[
x_0=\frac{n/d-2K}{2n(K+1)+8K},
\]

which proves the second term in (12). The first term follows from the two-chord theorem.

Finally, if \(n\ge4dK+4\), elementary rearrangement gives \(x_0\ge1/[4d(K+1)]\). If \(n<4dK+4\), then

\[
\frac2n>\frac1{2(dK+1)}
       \ge \frac1{4d(K+1)}.
\]

This proves (13).

For cubic graphs \(d=1\). Theorem 1 improves the \(k=2\) conclusion substantially by also averaging the internal matching edges through the four lifted cycles.

---

## 5. An upper bound on any possible universal constant

The Petersen graph shows that any universal constant must satisfy

\[
\boxed{c\le\frac13.}
\]

Write the Petersen graph with outer cycle \(u_0u_1\cdots u_4u_0\), inner edges \(v_iv_{i+2}\), and spokes \(u_iv_i\), with indices modulo \(5\).

It is non-Hamiltonian. For completeness: a Hamilton cycle would use an even positive number of spokes, hence either two or four. With two spokes, their indices would have to be adjacent in both the outer cyclic order (difference \(1\)) and the inner cyclic order (difference \(2\)), which is impossible. With four spokes, after rotation the missing spoke can be taken as \(u_0v_0\); the forced remaining edges split into the two 5-cycles

\[
u_0u_1v_1v_4u_4u_0
\]

and

\[
u_2u_3v_3v_0v_2u_2.
\]

The Petersen graph is also \(3\)-edge-connected. Hence, for every cycle \(C\), its vertex set is proper and

\[
|\delta(V(C))|\ge3.
\]

Since every cycle has length \(\ell\le9\), the cubic identity (1) gives

\[
\operatorname{ch}(C)
\le\frac{\ell-3}{2}
\le\frac{\ell}{3}.
\]

Equality is attained by the 9-cycle

\[
u_0u_1v_1v_3u_3u_2v_2v_4u_4u_0,
\]

which has exactly three chords. Thus \(\rho(\text{Petersen})=1/3\).

---

## 6. What remains open

The arguments above do not yield an absolute constant for arbitrary minimum-degree-\(3\) graphs.

The essential limitations are:

1. A minimum-degree-\(3\) graph need not have a spanning 2-factor.
2. Even a cubic graph with a 2-factor may require an unbounded number of factor cycles.
3. In Theorem 2, cross-edges are distributed among \(\Theta(k^2)\) pairs of factor cycles, so the resulting constant deteriorates with \(k\).
4. Combining many factor cycles at once requires controlling the lengths of the chosen arcs inside each factor cycle. A cycle in the quotient graph of factor components does not automatically lift to a cycle retaining a linear fraction of the quotient chords.

Thus the full conjecture is neither proved nor disproved here. The concrete progress is the \(1/7\) theorem, the asymptotic \(1/4\) bound for cubic graphs with a two-component 2-factor, and the bounded-\(\Delta\), bounded-factor-component estimate (13).