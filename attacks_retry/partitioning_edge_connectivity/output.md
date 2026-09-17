```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture in a dense simple-graph regime and strengthen the order-dependent sufficient bound, but do not settle the general case.",
  "would_publish": false,
  "caveats": "The exact results require density or bounded order; the general bound depends on n, and no novelty is claimed."
}
```

# 1. Statements of the partial results

Let \(G\) be a finite undirected graph, let \(n=|V(G)|\ge 2\), and let \(a,b\ge 1\) be integers. Write
\[
m=\min(a,b),\qquad M=\max(a,b).
\]
Parallel edges are permitted except in the results explicitly concerning simple graphs. Loops can be discarded and assigned arbitrarily afterward.

I obtain three partial results.

### A. An exact dense-graph case

Let \(\varepsilon\in\{0,1\}\) be the parity of \(m\). The conjecture holds for simple graphs whenever
\[
\boxed{\quad n\le 2M+5-2\varepsilon.\quad} \tag{1}
\]
In fact, in this regime the weaker hypothesis
\[
\delta(G)\ge a+b+2
\]
suffices.

Thus, for example, a fixed smaller target and a larger target at least approximately \(n/2\) satisfy the conjectured additive-\(2\) threshold.

### B. Slightly stronger exact results for the smallest unresolved parameters

I prove the following minimum-degree statement:

> **If \(G\) is simple, \(\delta(G)\ge5\), and \(n\le2\delta(G)-1\), then \(E(G)\) can be partitioned into two \(2\)-edge-connected spanning subgraphs.**

Consequently, the original conjecture holds for:

- \((a,b)=(1,2)\), for every simple \(5\)-edge-connected graph of order at most \(9\);
- \((a,b)=(2,2)\), for every simple \(6\)-edge-connected graph of order at most \(11\).

These conclusions do not require Eulerian parity.

### C. A general order-dependent bound

All logarithms below are natural. Set
\[
h=2\log(2n),\qquad L=h+\log(h+1)+1,\qquad \mu=2m+1,
\]
and define
\[
r=r(n,m)=\min\left\{t\in\mathbb Z:
t\ge\mu,\quad
t\log(t/\mu)-t+\mu\ge L
\right\}.
\]
Then the desired partition exists whenever
\[
\boxed{\quad \lambda(G)\ge M+r(n,m).\quad} \tag{2}
\]
The smaller color can moreover be required to contain \(m\) edge-disjoint spanning trees.

For every fixed \(m\),
\[
\boxed{\quad
r(n,m)=(2+o(1))\frac{\log n}{\log\log n}.
\quad} \tag{3}
\]
For \(m=1\), this improves the leading constant \(4\) in the supplied attempt’s displayed bound to \(2\); it also extends that construction to arbitrary \(m\). It should of course be combined with the supplied \(2(a+b)\) bound by taking the better sufficient threshold.

The exchange-rounding idea from the previous attempt is reused, but proved below in the required generality. No computational checks or unverified literature claims are used.

# 2. The exact dense-graph case

We first record an elementary fact.

### Lemma 1

If a simple graph \(H\) on \(n\) vertices satisfies
\[
\delta(H)\ge \lfloor n/2\rfloor,
\]
then
\[
\lambda(H)=\delta(H).
\]

**Proof.** Put \(d=\delta(H)\). For any nontrivial cut, choose its smaller shore \(X\), and write \(q=|X|\). Then \(1\le q\le\lfloor n/2\rfloor\le d\), and
\[
|\delta_H(X)|
\ge q(d-q+1)
=d+(q-1)(d-q)
\ge d.
\]
The reverse inequality follows from a minimum-degree vertex. \(\square\)

### Proof of result A

Let
\[
\ell=\lceil m/2\rceil,\qquad 2\ell=m+\varepsilon.
\]
Condition (1) is equivalent to
\[
M+2-\varepsilon\ge\lfloor n/2\rfloor. \tag{4}
\]

We greedily remove \(\ell\) Hamilton cycles. Before removing the last one, the remaining minimum degree is at least
\[
m+M+2-2(\ell-1)
=M+4-\varepsilon
\ge \lfloor n/2\rfloor+2
\ge n/2.
\]
The same bound, or a stronger one, holds at each earlier step. Thus Dirac’s Hamilton-cycle theorem applies at every step.

Let \(A\) be the union of these \(\ell\) edge-disjoint Hamilton cycles, and put \(B=E(G)\setminus A\). Every nontrivial cut contains at least two edges of each Hamilton cycle, so
\[
\lambda(V,A)\ge2\ell\ge m.
\]
Also,
\[
\delta(V,B)\ge M+2-\varepsilon\ge\lfloor n/2\rfloor.
\]
Lemma 1 gives
\[
\lambda(V,B)=\delta(V,B)\ge M.
\]
Relabeling the colors if necessary proves the assertion. \(\square\)

# 3. Two bridgeless spanning subgraphs by a Hamilton-cycle switch

Here a connected graph is \(2\)-edge-connected precisely when every edge lies on a cycle.

### Proposition 2

Let \(G\) be simple, put \(D=\delta(G)\), and suppose
\[
D\ge5,\qquad n\le2D-1.
\]
Then \(G\) has an edge partition into two \(2\)-edge-connected spanning subgraphs.

**Proof.** Dirac’s theorem supplies a Hamilton cycle \(C\). Put
\[
H=G-E(C),\qquad d=D-2\ge3.
\]
Thus \(\delta(H)\ge d\).

If \(H\) is \(2\)-edge-connected, we are done. Otherwise there is a nontrivial cut
\[
|\delta_H(X)|\le1.
\]
Choose \(X\) to be its smaller shore and write \(Y=V(G)\setminus X\).

For a set of size \(q\le d\), the calculation in Lemma 1 gives
\[
|\delta_H(X)|\ge q(d-q+1)\ge d.
\]
Hence both shores of our cut have at least \(d+1\) vertices. Since
\[
n\le2D-1=2d+3,
\]
we must have
\[
|X|=d+1,\qquad d+1\le |Y|\le d+2. \tag{5}
\]

**The graph \(H[X]\) is complete.** Indeed, all but at most one vertex of \(X\) have no neighbor across the cut, so their degree condition forces adjacency to all other vertices of \(X\). This also forces all adjacencies at the possible exceptional vertex.

Moreover,
\[
\delta(H[Y])\ge d-1
\ge \left\lfloor\frac{|Y|}{2}\right\rfloor.
\]
By Lemma 1, \(H[Y]\) is \(2\)-edge-connected.

Because \(H[X]\) contains every possible edge within \(X\), the Hamilton cycle \(C\) has no edge within \(X\). Orient \(C\) cyclically. Its edges directed from \(X\) to \(Y\) define an injection
\[
f:X\longrightarrow Y.
\]
Put \(S=f(X)\). By (5), at most one vertex of \(Y\) lies outside \(S\). Since \(\delta(H[Y])\ge2\), there is an edge \(uv\in E(H[Y])\) with both endpoints in \(S\).

Let
\[
x=f^{-1}(u),\qquad x'=f^{-1}(v).
\]
The cycle \(C\) contains the directed edges \(xu\) and \(x'v\), while \(H\) contains \(xx'\) and \(uv\). Perform the switch
\[
C'=C-\{xu,x'v\}+\{xx',uv\}.
\]
Because the two removed edges have the same \(X\)-to-\(Y\) direction in the cyclic orientation, this reconnection produces one Hamilton cycle, not two cycles.

It remains to check the complement. It contains
\[
K=
\bigl(H[X]-xx'\bigr)
\cup
\bigl(H[Y]-uv\bigr)
\cup\{xu,x'v\}.
\]
Both \(H[X]\) and \(H[Y]\) are connected and bridgeless. Deleting one edge from each leaves them connected, and the two new cross-edges join them.

The graph \(K\) is also bridgeless. For example, a cycle in \(H[X]\) using the deleted edge \(xx'\) can have that edge replaced by a path through \(xu\), \(H[Y]-uv\), and \(vx'\). The analogous replacement works for edges of \(H[Y]\). The two new cross-edges themselves lie on a cycle obtained from paths in the two connected graphs after deletion.

Thus \(K\), and therefore \(G-E(C')\), is \(2\)-edge-connected. Together with \(C'\), this gives the partition. \(\square\)

The two bounded-order consequences in result B follow immediately from \(\delta(G)\ge\lambda(G)\).

# 4. A cut-counting estimate with leading exponent \(2\)

The order-dependent result uses a slightly sharper cut-union estimate than the one in the previous attempt.

### Lemma 3

If \(G\) has edge-connectivity \(\lambda>0\), then for every real \(\alpha\ge1\), the number of unordered nontrivial cuts of size at most \(\alpha\lambda\) is at most
\[
(2n)^{2\alpha}. \tag{6}
\]

**Proof.** Put \(\rho=2\alpha\) and \(q=\lceil\rho\rceil\). If \(q\ge n\), the total number of cuts gives the claimed bound.

Otherwise, repeatedly contract a uniformly random edge until \(q\) vertices remain, discarding loops. Fix a cut \(C\) of size at most \(\alpha\lambda\). Conditional on its survival to a stage with \(i\) vertices, the contracted graph has at least \(i\lambda/2\) edges. Therefore its probability of surviving the next contraction is at least
\[
1-\frac{\rho}{i}.
\]
For \(\rho\ge1\), Bernoulli’s inequality gives
\[
\frac{i-\rho}{i}
\ge
\left(\frac{i-\rho}{i-\rho+1}\right)^\rho.
\]
Consequently, the probability that \(C\) survives all contractions is at least
\[
\prod_{i=q+1}^{n}\left(1-\frac{\rho}{i}\right)
\ge
\left(\frac{q+1-\rho}{n+1-\rho}\right)^\rho
\ge n^{-\rho}.
\]
After contraction, choose uniformly one of the remaining nontrivial cuts. There are fewer than
\[
2^{q-1}\le2^\rho
\]
choices. Each fixed original cut under consideration is therefore output with probability at least \((2n)^{-\rho}\). Summing these probabilities proves (6). \(\square\)

Let \(\mathcal C\) denote the unordered nontrivial cuts, and put
\[
\alpha_C=\frac{|C|}{\lambda}.
\]
With \(h,L\) as defined in Section 1, Lemma 3 implies
\[
\begin{aligned}
\sum_{C\in\mathcal C}e^{-L\alpha_C}
&=
L\int_1^\infty
\#\{C:\alpha_C\le t\}\,e^{-Lt}\,dt\\
&\le
L\int_1^\infty e^{-(L-h)t}\,dt\\
&=
\frac{L}{L-h}e^{-(L-h)}
\le \frac1e. \tag{7}
\end{aligned}
\]
For the last inequality, use
\[
L-h=\log(h+1)+1\ge1,\qquad
\frac{L}{L-h}\le h+1.
\]

Thus, if each cut has failure probability at most \(e^{-L|C|/\lambda}\), the union bound leaves positive probability of no failure.

# 5. Negatively correlated rounding of spanning-tree packings

We need a version of the previous attempt’s tree-rounding lemma for unions of \(m\) spanning trees.

## 5.1 The relevant matroid

For \(F\subseteq E(G)\), let \(e_F(X)\) count the edges of \(F\) with both endpoints in \(X\). Define
\[
\mathcal I_m=
\left\{
F\subseteq E(G):
e_F(X)\le m(|X|-1)
\text{ for every nonempty }X\subseteq V(G)
\right\}. \tag{8}
\]
These are the independent sets of a matroid.

Here is a short verification of the augmentation axiom. For \(I\in\mathcal I_m\), call a nonempty set \(X\) tight if
\[
e_I(X)=m(|X|-1).
\]
Intersecting tight sets have tight union, by supermodularity of the internal-edge count. Since singletons are tight, the maximal tight sets form a partition of \(V(G)\).

Suppose \(I,J\in\mathcal I_m\), \(|I|<|J|\), and no edge of \(J\setminus I\) can be added to \(I\). Every such edge then has both endpoints in a tight set, hence in one part of the maximal-tight-set partition. Thus every edge of \(J\) crossing that partition belongs to \(I\), while within each part \(J\) has at most as many edges as \(I\). This gives \(|J|\le|I|\), a contradiction.

If \(G\) contains \(m\) edge-disjoint spanning trees, this matroid has rank \(m(n-1)\). Every base \(F\) is itself the union of \(m\) edge-disjoint spanning trees: for a partition into \(t\) nonempty parts,
\[
e_F(\text{between parts})
\ge m(n-1)-m(n-t)
=m(t-1),
\]
so the Nash–Williams/Tutte theorem applies, and the packed trees use all \(m(n-1)\) edges.

## 5.2 Rounding lemma

### Lemma 4

Let \(x\) be a convex combination of incidence vectors of bases of a matroid. There is a random base \(F\) such that, for every edge set \(S\),
\[
\Pr(S\subseteq F)\le\prod_{e\in S}x_e. \tag{9}
\]

**Proof.** Merge two bases \(B_1,B_2\), of positive weights \(\beta_1,\beta_2\), as follows.

Choose \(e\in B_1\setminus B_2\). Symmetric basis exchange supplies \(f\in B_2\setminus B_1\) such that both
\[
B_1-e+f,\qquad B_2-f+e
\]
are bases. Make one of the updates
\[
\begin{cases}
B_1\leftarrow B_1-e+f,
&\text{with probability }\beta_2/(\beta_1+\beta_2),\\
B_2\leftarrow B_2-f+e,
&\text{with probability }\beta_1/(\beta_1+\beta_2).
\end{cases}
\]
The current weighted incidence vector changes only in coordinates \(e,f\), by opposite amounts, and its conditional expectation is unchanged.

For fixed \(S\), the function
\[
\Phi_S(x)=\prod_{g\in S}x_g
\]
is concave along every such two-coordinate line: its restriction is constant, affine, or a quadratic with nonpositive leading coefficient. Therefore its conditional expectation does not increase.

Each update decreases the symmetric difference of the two bases. When they agree, merge their weights. Continue until one base remains. At termination,
\[
\Phi_S(\mathbf 1_F)=\mathbf 1_{\{S\subseteq F\}},
\]
which proves (9). \(\square\)

# 6. Proof of the general bound

Assume
\[
\lambda=\lambda(G)\ge M+r.
\]
Let
\[
k=\lfloor\lambda/2\rfloor.
\]
The definition of \(r\) ensures \(k\ge m\). By Nash–Williams/Tutte, \(G\) has \(k\) edge-disjoint spanning trees \(T_1,\dots,T_k\).

Take a convex combination of bases of the matroid in (8) in which each tree is used with frequency \(m/k\). For example, average the \(k\) unions of \(m\) cyclically consecutive trees. Its incidence vector satisfies
\[
x_e\le \frac{m}{k}.
\]
Apply Lemma 4 to obtain a random union \(F\) of \(m\) edge-disjoint spanning trees.

Fix a cut \(C\) of size \(c=\alpha\lambda\), where \(\alpha\ge1\), and let
\[
Z=|F\cap C|.
\]
For \(\theta\ge0\), expanding the product and using (9) gives
\[
\begin{aligned}
\mathbb E e^{\theta Z}
&=
\mathbb E\prod_{e\in C}
\left(1+(e^\theta-1)\mathbf 1_{\{e\in F\}}\right)\\
&\le
\prod_{e\in C}\left(1+(e^\theta-1)x_e\right)\\
&\le
\exp\left((e^\theta-1)\sum_{e\in C}x_e\right).
\end{aligned}
\]
Furthermore,
\[
\sum_{e\in C}x_e
\le \frac{cm}{k}
=\alpha\frac{\lambda m}{k}
\le\alpha(2m+1)
=\alpha\mu,
\]
where the penultimate inequality follows from
\[
\lambda\le2k+1,\qquad k\ge m.
\]

Since \(r>\mu\), choose \(\theta=\log(r/\mu)>0\). Exponential Markov yields
\[
\Pr(Z>\alpha r)
\le
\exp\left[-\alpha\left(r\log(r/\mu)-r+\mu\right)\right]
\le e^{-L\alpha}.
\]
By (7), with positive probability,
\[
|F\cap C|\le r\frac{|C|}{\lambda}
\qquad\text{for every cut }C. \tag{10}
\]

Choose such an \(F\), and set
\[
A=F,\qquad B=E(G)\setminus F.
\]
The graph \((V,A)\) contains \(m\) edge-disjoint spanning trees, so it is \(m\)-edge-connected. For every nontrivial cut,
\[
\begin{aligned}
|B\cap C|
&\ge |C|\left(1-\frac r\lambda\right)\\
&\ge \lambda-r\\
&\ge M.
\end{aligned}
\]
Thus \((V,B)\) is \(M\)-edge-connected, proving (2).

For fixed \(m\), \(\mu\) is fixed and
\[
t\log(t/\mu)-t+\mu\sim t\log t.
\]
Since
\[
L=2\log n+O(\log\log n),
\]
inverting this relation gives
\[
r\sim\frac{L}{\log L}
\sim 2\frac{\log n}{\log\log n},
\]
as claimed in (3).

# 7. Relation to the Eulerian lead, and remaining gaps

The previous attempt’s Eulerian \((2,2)\) conclusion checks out. Here is the short verification. In an Eulerian \(6\)-edge-connected graph, take three disjoint spanning trees \(T_1,T_2,T_3\). Choose a subset \(J\subseteq E(T_3)\) whose odd-degree vertices are exactly those of \(T_1\). Then
\[
A=E(T_1)\cup J
\]
is connected and even, while its complement is also even and contains \(T_2\). Both colors are therefore \(2\)-edge-connected. This argument genuinely needs the global parity assumption.

The new results above do **not** settle the unrestricted conjecture:

- The exact arguments require a simple graph and sufficient density.
- The general bound has a surplus growing with \(n\), not the required fixed additive \(2\).
- Requiring the smaller color to contain \(m\) spanning trees is intrinsically too expensive for some instances at the conjectured threshold. For example, with \(G=K_9\) and \(a=b=3\), three spanning trees would use \(24\) edges, while a \(3\)-edge-connected complement needs at least \(14\) edges; \(K_9\) has only \(36\) edges. Thus the stronger conclusion of the rounding method cannot cover even every instance of the original question.

In particular, the general-order \((1,2)\) case at connectivity \(5\), and the general non-Eulerian \((2,2)\) case at connectivity \(6\), remain unresolved by this work. No counterexample to the original additive-\(2\) assertion has been obtained.