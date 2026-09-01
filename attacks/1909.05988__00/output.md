```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The normalized link-Ramsey rate of a disconnected graph is, up to o(1), the maximum of the rates of its non-bipartite connected components, improving the quoted O(s) upper dependence to the order of the largest non-bipartite component.",
  "would_publish": false,
  "caveats": "The connected non-bipartite case and existence of a limiting constant remain unresolved; novelty of the reduction has not been literature-checked."
}
```

# Mathematical writeup

## 1. Setup

For a graph \(F\), let \(L(F)\) be the 3-uniform hypergraph obtained by adding a new apex \(z\) and taking the triples
\[
\{z,x,y\},\qquad xy\in E(F).
\]
Write
\[
R_F(n):=r(L(F),K_n^{(3)}),
\qquad
\rho_F(n):=\frac{\log R_F(n)}{n\log n}.
\]
The logarithm base is immaterial.

Equivalently, \(R_F(n)\) is the least \(N\) such that every \(L(F)\)-free 3-graph on \(N\) vertices has an independent set of order \(n\). A 3-graph \(\mathcal H\) is \(L(F)\)-free precisely when every link graph
\[
\operatorname{lk}_{\mathcal H}(v)
 =\{xy:vxy\in E(\mathcal H)\}
\]
is \(F\)-free.

The question does not state a specific candidate formula, and it is not presently known that \(\rho_F(n)\) has a limit. The following gives an exact reduction, on the \(n\log n\) scale, from arbitrary disconnected \(F\) to its connected components.

---

## 2. A component-reduction theorem

### Theorem 1

Let \(G\) have connected components \(G_1,\dots,G_t\), and put \(s=|V(G)|\). Then, for every \(n\),
\[
\boxed{
\max_{1\le i\le t}R_{G_i}(n)
\ \le\
R_G(n)
\ \le\
t(2s^2+1)\max_{1\le i\le t}R_{G_i}(n).
}
\tag{1}
\]

Consequently,
\[
0\le
\rho_G(n)-\max_{1\le i\le t}\rho_{G_i}(n)
\le
\frac{\log\!\bigl(t(2s^2+1)\bigr)}{n\log n}.
\tag{2}
\]
Thus
\[
\rho_G(n)=\max_i\rho_{G_i}(n)+o_G(1).
\tag{3}
\]

### Proof

We first need a graph-packing observation.

#### Packing lemma

If a graph \(Q\) is \(G\)-free, then there is an index \(i\in[t]\) and a set
\[
T\subseteq V(Q),\qquad |T|\le s^2,
\]
such that \(Q-T\) is \(G_i\)-free.

Indeed, let \(\nu_{G_i}(Q)\) denote the maximum number of pairwise vertex-disjoint copies of \(G_i\) in \(Q\). Suppose for contradiction that
\[
\nu_{G_i}(Q)\ge s+1
\]
for every \(i\). For each \(i\), fix a packing \(\mathcal P_i\) of \(s+1\) disjoint copies of \(G_i\).

Choose one copy from each \(\mathcal P_i\) successively. Before choosing the copy corresponding to \(G_i\), fewer than \(s\) vertices have already been used. Because the copies in \(\mathcal P_i\) are pairwise disjoint, at most \(s\) of them meet the previously used vertices. Hence one copy remains disjoint. The selected copies form a copy of the disjoint union
\[
G_1\sqcup\cdots\sqcup G_t=G,
\]
contrary to the assumption that \(Q\) is \(G\)-free.

Therefore \(\nu_{G_i}(Q)\le s\) for some \(i\). Take a maximal packing of copies of this \(G_i\), and let \(T\) be the union of its vertices. Then
\[
|T|\le s|V(G_i)|\le s^2.
\]
Maximality implies that \(Q-T\) is \(G_i\)-free. This proves the packing lemma.

#### Applying the packing lemma to all links

Let \(\mathcal H\) be an \(L(G)\)-free 3-graph on \(N\) vertices. For each \(v\in V(\mathcal H)\), its link \(Q_v=\operatorname{lk}_{\mathcal H}(v)\) is \(G\)-free. Apply the packing lemma to choose:

- an index \(i(v)\in[t]\);
- a set \(T_v\subseteq V(\mathcal H)\setminus\{v\}\), with \(|T_v|\le s^2\);

such that
\[
Q_v-T_v
\quad\text{is }G_{i(v)}\text{-free}.
\]

Partition \(V(\mathcal H)\) according to the value of \(i(v)\). Some class \(X\) has size at least \(N/t\); write \(i(v)=i\) for every \(v\in X\).

Construct an auxiliary graph \(A\) on \(X\), where \(uv\in E(A)\) whenever
\[
u\in T_v\quad\text{or}\quad v\in T_u.
\]
For every \(Y\subseteq X\),
\[
e(A[Y])
 \le \sum_{v\in Y}|T_v\cap Y|
 \le s^2|Y|.
\]
Thus every induced subgraph of \(A\) has average degree at most \(2s^2\). Hence \(A\) is \(2s^2\)-degenerate and is \((2s^2+1)\)-colorable. It therefore has an independent set \(S\) satisfying
\[
|S|\ge \frac{|X|}{2s^2+1}
     \ge \frac{N}{t(2s^2+1)}.
\]

For \(v\in S\), independence in \(A\) gives
\[
T_v\cap(S\setminus\{v\})=\varnothing.
\]
It follows that
\[
\operatorname{lk}_{\mathcal H[S]}(v)
 \subseteq Q_v-T_v
\]
is \(G_i\)-free. This holds for every \(v\in S\), so \(\mathcal H[S]\) is \(L(G_i)\)-free.

Let
\[
M=\max_i R_{G_i}(n)
\]
and take
\[
N=t(2s^2+1)M.
\]
The construction gives \(|S|\ge M\ge R_{G_i}(n)\). Since \(\mathcal H[S]\) is \(L(G_i)\)-free, it contains an independent \(n\)-set. Therefore
\[
R_G(n)\le t(2s^2+1)M.
\]

For the lower bound in (1), each \(L(G_i)\) is a subhypergraph of \(L(G)\), so Ramsey monotonicity gives
\[
R_{G_i}(n)\le R_G(n).
\]
This proves (1), and (2)–(3) follow by taking logarithms. ∎

---

## 3. Bipartite components have only polynomial link-Ramsey numbers

To extract the consequence for non-bipartite \(G\), bipartite components must be shown negligible on the \(n\log n\) scale.

### Lemma 2

Let \(B\) be a fixed bipartite graph with a bipartition of sizes \(a,b\), where \(1\le a\le b\). Then
\[
R_B(n)\le C_B n^{2a}
\tag{4}
\]
for a constant \(C_B\). In particular,
\[
\rho_B(n)\longrightarrow 0.
\]

### Proof

The graph \(B\) is a subgraph of \(K_{a,b}\), so every \(B\)-free graph is \(K_{a,b}\)-free.

Let \(Q\) be a \(K_{a,b}\)-free graph on \(m\) vertices, with degrees \(d(x)\) and average degree \(\bar d\). Counting pairs consisting of an \(a\)-set and a common neighbor gives
\[
\sum_{x\in V(Q)}\binom{d(x)}a
 \le (b-1)\binom ma.
\tag{5}
\]
For \(d\ge a\),
\[
\binom da\ge \frac{(d-a+1)^a}{a!}.
\]
Convexity then yields
\[
\bar d
 \le a-1+(b-1)^{1/a}m^{1-1/a},
\]
and hence
\[
e(Q)\le C_{a,b}m^{2-1/a}.
\tag{6}
\]

Now let \(\mathcal H\) be an \(L(B)\)-free 3-graph on \(N\) vertices. Every link is \(B\)-free and therefore satisfies (6). Since each hyperedge contributes one edge to each of three links,
\[
3e(\mathcal H)
 =\sum_{v\in V(\mathcal H)}
   e\bigl(\operatorname{lk}_{\mathcal H}(v)\bigr)
 \le C_{a,b}N^{3-1/a}.
\]
Thus the average vertex degree \(d=3e(\mathcal H)/N\) satisfies
\[
d\le C_{a,b}N^{2-1/a}.
\tag{7}
\]

For completeness, random sampling gives the elementary 3-graph independence estimate
\[
\alpha(\mathcal H)\ge
\frac{2N}{3\sqrt{\max\{d,1\}}}.
\tag{8}
\]
Indeed, when \(d\ge1\), retain every vertex independently with probability \(p=d^{-1/2}\). The expected value of
\[
|X|-e(\mathcal H[X])
\]
is
\[
pN-p^3e(\mathcal H)
 =\frac{2N}{3\sqrt d}.
\]
Deleting one vertex from every surviving edge leaves an independent set of at least that order. The case \(d<1\) follows by taking all vertices and deleting one per edge.

Combining (7) and (8),
\[
\alpha(\mathcal H)\ge c_B N^{1/(2a)}.
\]
Taking \(N\ge C_B n^{2a}\) proves (4). ∎

The exponent \(2a\) is not asserted to be optimal; polynomial growth is all that is needed here.

---

## 4. Consequences for the stated problem

Let \(G_1,\dots,G_t\) be the connected components of a fixed non-bipartite graph \(G\), and let
\[
\mathcal N(G)=\{G_i:G_i\text{ is non-bipartite}\}.
\]
At least one such component exists. By the quoted Fox–He lower bound, every \(C\in\mathcal N(G)\) satisfies
\[
R_C(n)\ge 2^{c_C n\log n}
\]
for sufficiently large \(n\). Lemma 2 says that every bipartite component has only polynomial \(R_{G_i}(n)\). Therefore Theorem 1 gives

\[
\boxed{
R_G(n)
 =\Theta_G\!\left(
   \max_{C\in\mathcal N(G)}R_C(n)
   \right).
}
\tag{9}
\]

Equivalently,
\[
\boxed{
\rho_G(n)
 =
 \max_{C\in\mathcal N(G)}\rho_C(n)+o_G(1).
}
\tag{10}
\]

In particular:

1. If the normalized limits exist for the connected non-bipartite components, then
   \[
   \lim_{n\to\infty}\rho_G(n)
   =
   \max_{C\in\mathcal N(G)}
   \lim_{n\to\infty}\rho_C(n).
   \]

2. Without assuming limits,
   \[
   \limsup_{n\to\infty}\rho_G(n)
   =
   \max_{C\in\mathcal N(G)}
   \limsup_{n\to\infty}\rho_C(n).
   \]

3. Let
   \[
   h(G)=\max\{|V(C)|:C\in\mathcal N(G)\}.
   \]
   Applying the quoted Fox–He upper bound to each connected component yields the refinement
   \[
   \limsup_{n\to\infty}\rho_G(n)=O(h(G)),
   \tag{11}
   \]
   replacing \(O(s)\) by the order of the largest non-bipartite connected component.

Thus, if \(g\) is the odd girth of \(G\),
\[
\Omega(1/g)
\le
\liminf_{n\to\infty}\rho_G(n)
\le
\limsup_{n\to\infty}\rho_G(n)
\le
O(h(G)).
\tag{12}
\]
For connected \(G\), of course, \(h(G)=s\), so this does not improve the central connected case.

---

## 5. Repeated components and isolated vertices

There is a sharper statement when all components are copies of one graph.

### Proposition 3

For every fixed graph \(F\), integer \(k\ge1\), and \(f=|V(F)|\),
\[
\boxed{
R_F(n)
\le R_{kF}(n)
\le \bigl(2(k-1)f+1\bigr)R_F(n),
}
\tag{13}
\]
where \(kF\) denotes the disjoint union of \(k\) copies of \(F\).

Indeed, a \(kF\)-free graph has no \(k\) vertex-disjoint copies of \(F\). The union of a maximal \(F\)-packing therefore has at most \((k-1)f\) vertices and meets every copy of \(F\). Applying the same auxiliary-graph selection argument as above gives (13).

Consequently,
\[
\rho_{kF}(n)=\rho_F(n)+o_{F,k}(1).
\tag{14}
\]

For example, for an odd cycle \(C_g\),
\[
R_{C_g}(n)
\le R_{kC_g}(n)
\le \bigl(2(k-1)g+1\bigr)R_{C_g}(n).
\]
Hence the quoted \(O(s)=O(kg)\) upper dependence for \(G=kC_g\) can be replaced by \(O(g)\); in fact its entire normalized rate agrees asymptotically with that of one \(C_g\).

Isolated vertices are even more harmless. If \(F'=F\sqcup qK_1\), then \(L(F')\) is \(L(F)\) together with \(q\) isolated hypergraph vertices. Whenever
\[
R_F(n)\ge |V(F)|+1+q,
\]
one has the exact equality
\[
R_{F'}(n)=R_F(n):
\]
a red copy of \(L(F)\) has enough unused host vertices to supply the \(q\) isolated vertices. Thus isolated padding can increase the displayed parameter \(s\) arbitrarily without changing the eventual Ramsey number.

---

## 6. Remaining gap

The reduction above completely removes component multiplicities and bipartite connected components from the \(n\log n\) rate. It does not address the essential case of a connected non-bipartite graph \(G\). In that case the original gap remains
\[
\Omega(1/g)\le \rho_G(n)\le O(s),
\]
and the argument gives neither:

- an exact dependence on the internal structure of connected \(G\);
- equality of the lower and upper dependences on \(g\) or \(s\);
- nor existence of \(\lim_{n\to\infty}\rho_G(n)\).

Thus this is a structural partial result rather than a solution of the stated open problem.