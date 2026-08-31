```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is exactly equivalent to uniformly bounded rainbow-matching deficiency in equitable n-colourings of K_{2n}; I prove this reduction and the k=2 case, but not the required absolute bound.",
  "would_publish": false,
  "caveats": "I use f_c as the minimum number of matching edges recoloured; an L1 normalization changes bounds only by a factor of two."
}
```

# Mathematical writeup

## 1. Statement and normalization

Let \(N=2kt\), and let \(c:E(K_N)\to[k]\) be colour-balanced. Since

\[
|E(K_N)|=kt(N-1),
\]

each colour class has exactly

\[
t(N-1)
\]

edges. For a perfect matching \(M\), write

\[
m_i(M)=|\{e\in M:c(e)=i\}|.
\]

The target is \(m_i(M)=t\) for every \(i\).

I use the recolouring-distance interpretation

\[
f_c(M)=\min\{\text{number of edges of \(M\) recoloured to obtain \(t\) edges of each colour}\}.
\]

Equivalently,

\[
f_c(M)=\sum_{i=1}^k (m_i(M)-t)_+
      =\frac12\sum_{i=1}^k |m_i(M)-t|.
\tag{1}
\]

If the source defines \(f_c\) as the full \(L^1\)-quantity, all statements below acquire a factor of two.

---

## 2. Exact reduction to the case \(t=1\)

This is the main partial result.

### Proposition 2.1

Suppose there is a constant \(C\) such that every colour-balanced \(n\)-colouring of \(K_{2n}\), with every colour occurring \(2n-1\) times, has a perfect matching \(M\) satisfying \(f_c(M)<C\). Then the same constant works for every pair \(k,t\) in the original conjecture.

Consequently, the original conjecture is equivalent to its special case \(t=1\).

### Proof

Fix a colour-balanced \(k\)-colouring \(c\) of \(K_{2kt}\). Put \(n=kt\), so the graph is \(K_{2n}\).

Every original colour class has size

\[
t(2n-1).
\]

Partition the edges of original colour \(i\) arbitrarily into \(t\) classes

\[
E_{i,1},\ldots,E_{i,t},
\]

each of size \(2n-1\). Regard these \(kt=n\) classes as distinct “shades.” This produces a colour-balanced \(n\)-colouring \(\widetilde c\) of \(K_{2n}\) with parameter \(t'=1\).

For any perfect matching \(M\), let \(m_{i,j}\) be its number of edges of shade \((i,j)\). By (1),

\[
\begin{aligned}
f_c(M)
&=\frac12\sum_{i=1}^k
  \left|\sum_{j=1}^t(m_{i,j}-1)\right|\\
&\le
\frac12\sum_{i=1}^k\sum_{j=1}^t |m_{i,j}-1|
=f_{\widetilde c}(M).
\end{aligned}
\tag{2}
\]

Equivalently, if \(r\) edges of \(M\) can be recoloured so that every shade occurs once, then after forgetting the shade indices, at most the same \(r\) recolourings make every original colour occur \(t\) times.

Thus a constant bound for \(t=1\) gives the same bound for arbitrary \(t\). The converse is immediate, since \(t=1\) is a special case. ∎

### Quantitative formulation

Let

\[
F(k,t)=\max_c\min_M f_c(M),
\]

where \(c\) ranges over all colour-balanced \(k\)-colourings of \(K_{2kt}\). If \(D(n)=F(n,1)\), Proposition 2.1 gives

\[
F(k,t)\le D(kt),
\qquad
\sup_{k,t}F(k,t)=\sup_n D(n).
\tag{3}
\]

Thus any unbounded counterexample can also be realized with \(t=1\).

---

## 3. Rainbow-matching reformulation

For a colouring \(c\) of \(K_{2n}\), let \(\rho(c)\) be the maximum size of a rainbow matching, i.e. a matching whose edges have pairwise distinct colours.

### Proposition 3.1

For a colour-balanced \(n\)-colouring of \(K_{2n}\) with \(t=1\),

\[
\min_{M\text{ perfect}} f_c(M)=n-\rho(c).
\tag{4}
\]

Hence the conjecture is equivalent to the following purely rainbow statement:

> There is an absolute constant \(C\) such that every edge-colouring of \(K_{2n}\) with \(n\) colours, each occurring exactly \(2n-1\) times, contains a rainbow matching of size at least \(n-C\).

### Proof

For a perfect matching \(M\), let \(d(M)\) denote the number of colours represented in \(M\). Since \(M\) has \(n\) edges and the target is one edge of every colour,

\[
f_c(M)=n-d(M).
\tag{5}
\]

Choosing one edge of every represented colour gives a rainbow submatching of \(M\) of size \(d(M)\). Conversely, every rainbow matching of size \(r\) extends to a perfect matching of \(K_{2n}\), because the remaining \(2(n-r)\) vertices can be paired arbitrarily. The resulting perfect matching represents at least those \(r\) colours. Therefore

\[
\max_{M\text{ perfect}}d(M)=\rho(c),
\]

and (4) follows. ∎

This reformulation removes the parameter \(t\) entirely. It also shows exactly what a counterexample must provide: equitable colourings of \(K_{2n}\) whose largest rainbow matching misses an unbounded number of colours.

---

## 4. A binary balancing lemma

Although it does not synchronize different colour subsets, every single binary coarsening can be balanced to within one edge.

### Lemma 4.1

Let the edges of \(K_{2m}\) be coloured red/blue, and suppose the number of red edges is

\[
a(2m-1)
\]

for an integer \(a\). Then there is a perfect matching containing \(a-1\), \(a\), or \(a+1\) red edges.

### Proof

In a uniformly random perfect matching, every edge is present with probability \(1/(2m-1)\). Hence, if \(X(M)\) is the number of red edges in \(M\),

\[
\mathbb E X=\frac{a(2m-1)}{2m-1}=a.
\]

Thus some perfect matching has at most \(a\) red edges and some has at least \(a\).

The graph whose vertices are the perfect matchings of \(K_{2m}\), with two matchings adjacent when one is obtained from the other by replacing two matched edges \(xx',yy'\) with \(xy,x'y'\), is connected. Indeed, given perfect matchings \(P,Q\), choose \(xy\in Q\setminus P\), where \(x\) and \(y\) are paired in \(P\) with \(x'\) and \(y'\); the indicated switch adds \(xy\) and increases the number of common edges with \(Q\).

A switch removes two edges and adds two, so the red count changes by at most two. Along a path from a matching with red count at most \(a\) to one with count at least \(a\), the first count at least \(a\) is at most \(a+1\). ∎

### Corollary 4.2: the conjecture for \(k=2\)

For every \(t\), every balanced two-colouring of \(K_{4t}\) has a perfect matching \(M\) with

\[
f_c(M)\le 1.
\]

Thus the conjecture holds for \(k=2\), for example with the strict constant \(C=2\).

Indeed, one colour has \(t(4t-1)\) edges, so Lemma 4.1 gives a perfect matching with \(t-1,t\), or \(t+1\) edges of that colour. The other colour has the complementary discrepancy.

More generally, in an arbitrary \(k\)-colouring, for every subset \(I\) of colours there is a perfect matching \(M_I\) such that

\[
\left|
\sum_{i\in I}m_i(M_I)-|I|t
\right|\le 1.
\tag{6}
\]

The obstruction is that the matching \(M_I\) depends on \(I\).

### Parity addendum

If all perfect matchings have red counts of the same parity, then Lemma 4.1 gives an exactly balanced matching.

Indeed, \(K_{2m}\) has \((2m-1)!!\) perfect matchings, and each edge belongs to \((2m-3)!!\) of them; both numbers are odd. Thus the common parity of the red count equals the parity of the total number \(a(2m-1)\) of red edges, namely \(a\). A path of perfect matchings with all counts congruent to \(a\pmod 2\) and jumps of size at most two must hit \(a\) when crossing it.

---

## 5. A Hall-type property forced by equitability

Return to the rainbow formulation. Let \(c\) be an equitable \(n\)-colouring of \(K_{2n}\), and for \(I\subseteq[n]\) let \(G_I\) be the graph consisting of all edges whose colours lie in \(I\).

### Proposition 5.1

For every set \(I\) of \(r\) colours,

\[
\nu(G_I)\ge r,
\tag{7}
\]

where \(\nu\) denotes ordinary matching number.

### Proof

We use the standard extremal matching bound: a graph on \(N\) vertices with matching number at most \(s\) has at most

\[
\max\left\{
\binom{2s+1}{2},
\binom{s}{2}+s(N-s)
\right\}
\tag{8}
\]

edges.

For completeness, (8) follows from the Tutte–Berge theorem. If \(\nu(G)\le s\), there is \(S\subseteq V(G)\), with \(a=|S|\le s\), such that \(G-S\) has at least \(N-2s+a\) odd components. Adding all allowable edges and concentrating all but one of those odd components into isolated vertices gives

\[
e(G)\le
\binom a2+a(N-a)+\binom{2s-2a+1}{2}.
\]

This is a convex quadratic in \(a\in[0,s]\), so its maximum occurs at \(a=0\) or \(a=s\), yielding (8).

Now \(G_I\) has exactly

\[
r(2n-1)
\]

edges. If \(\nu(G_I)\le r-1\), (8), with \(N=2n\) and \(s=r-1\), would give

\[
e(G_I)\le
\max\left\{
\binom{2r-1}{2},
\frac{(r-1)(4n-r)}2
\right\}.
\]

But

\[
r(2n-1)-\binom{2r-1}{2}
=2r(n-r+1)-1>0,
\]

and

\[
2r(2n-1)-(r-1)(4n-r)
=r^2-3r+4n>0
\]

for \(1\le r\le n\). This is a contradiction. ∎

Thus every colour subfamily satisfies the natural Hall-type condition that its union contains an ordinary matching as large as the number of colours. The missing step is that graph matchings do not form a matroid, so this condition does not automatically produce a matching using one edge from each colour.

---

## 6. Limitation of a direct maximal-matching count

Let \(R\) be an inclusion-maximal rainbow matching in the \(t=1\) formulation. Write

\[
|R|=n-q.
\]

There are \(q\) unused colours and \(2q\) unmatched vertices, forming a set \(U\). No edge inside \(U\) can have an unused colour, since such an edge could be appended to \(R\).

The \(q\) unused colour classes therefore place all their \(q(2n-1)\) edges outside \(E(K_U)\). Consequently,

\[
q(2n-1)
\le
\binom{2n}{2}-\binom{2q}{2}.
\tag{9}
\]

Solving gives

\[
q\le
\frac{-(n-1)+\sqrt{5n^2-4n+1}}2,
\]

and therefore

\[
|R|\ge
\frac{3n-1-\sqrt{5n^2-4n+1}}2
=
\left(\frac{3-\sqrt5}{2}+o(1)\right)n.
\tag{10}
\]

This is only a weak linear bound. More importantly, (9) still permits \(q\) to be linear in \(n\). Thus counting the locations of unused colours, without exploiting alternating switches between colours, cannot prove the conjectured constant deficiency.

---

## 7. Small case \(n=2\)

For completeness, every equitable two-colouring of \(K_4\), with three edges of each colour, has a rainbow perfect matching.

The six edges of \(K_4\) split into its three perfect matchings. If none were rainbow, every one of these three two-edge blocks would be monochromatic. Each colour class would then be a union of two-edge blocks and hence have even size, contradicting that both have size three.

Thus the rainbow deficiency is zero for \(n\le2\).

---

## 8. Exact finite counterexample search

For fixed \(n\) and \(q\), the existence of an equitable colouring with rainbow deficiency at least \(q\) can be formulated as a finite \(0\)-\(1\) feasibility problem.

Let \(r=n-q+1\), and introduce variables

\[
x_{e,i}\in\{0,1\},
\qquad
e\in E(K_{2n}),\ i\in[n].
\]

Impose

\[
\sum_{i=1}^n x_{e,i}=1
\quad\text{for every edge }e,
\]

and

\[
\sum_e x_{e,i}=2n-1
\quad\text{for every colour }i.
\]

To forbid a rainbow matching of size \(r\), for every matching
\(F=\{e_1,\ldots,e_r\}\) and every injection
\(\phi:[r]\to[n]\), impose

\[
\sum_{j=1}^r x_{e_j,\phi(j)}\le r-1.
\tag{11}
\]

These constraints are exact: a violated constraint is precisely a matching whose \(r\) edges receive \(r\) distinct colours.

The number of size-\(r\) matchings to be considered is

\[
\frac{(2n)!}{(2n-2r)!\,2^r r!}.
\]

A proposed colouring can independently be checked by dynamic programming on states \((S,T)\), where \(S\subseteq V(K_{2n})\) is the set of used vertices and \(T\subseteq[n]\) is the set of used colours. From \((S,T)\), add an edge \(uv\) with \(u,v\notin S\) and \(c(uv)\notin T\). The maximum attained \(|T|\) is exactly \(\rho(c)\). No computational run is claimed here.

---

## 9. Remaining gap

The conjecture is reduced exactly to proving

\[
\sup_n\ \max_c\bigl(n-\rho(c)\bigr)<\infty
\]

over equitable \(n\)-colourings of \(K_{2n}\).

The results above show:

1. the parameter \(t\) is unnecessary for the qualitative conjecture;
2. every individual binary aggregation of the colours can be balanced within one edge;
3. every set of \(r\) colours has a union containing an ordinary \(r\)-matching;
4. the conjecture holds for \(k=2\).

What is missing is a simultaneous alternating-switch argument converting these separate matching witnesses into a single matching using all but \(O(1)\) colours. I do not have such an argument, nor an unbounded-deficiency construction.