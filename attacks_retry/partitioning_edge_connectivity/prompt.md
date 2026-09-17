Attack the following open graph-theory problem.

Catalog id: partitioning_edge_connectivity
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Connectivity
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partitioning_edge_connectivity/
Original entry: http://www.openproblemgarden.org/op/partitioning_edge_connectivity
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Partitioning edge-connectivity
Question Let $ G $ be an $ (a+b+2) $ - edge-connected graph. Does there exist a partition $ \{A,B\} $ of $ E(G) $ so that $ (V,A) $ is $ a $ -edge-connected and $ (V,B) $ is $ b $ -edge-connected?

=== Discussion / context (OpenProblemGarden) ===
By the Nash-Williams/Tutte theorem ([NW] or [T]) on disjoint spanning trees, the above conjecture is true if $ G $ is $ 2(a+b) $ -edge-connected. This is the only partial result I know of. Here is a related conjecture. Conjecture There exists a fixed integer $ k $ so that every $ k $ -edge-connected graph $ G=(V,E) $ has a subset of edges $ S $ with the property that every edge-cut of $ G $ has between $ \frac{1}{3} $ and $ \frac{2}{3} $ of its edges in $ S $ . The values $ \frac{1}{3} $ and $ \frac{2}{3} $ are of no special importance in the above conjecture. Indeed, an affirmative answer to the above problem with $ \frac{1}{3} $ and $ \frac{2}{3} $ replaced by $ \frac{1}{t} $ and $ 1 - \frac{1}{t} $ for any $ t > 0 $ would still be valuable - and in particular, would imply the 2+epsilon flow conjecture . Definition: Let $ G=(V,E) $ be a graph and let $ P=\{E_1,E_2,...,E_t\} $ be a partition of $ E $ . We say that $ P $ is $ k $ -courteous if $ G \setminus E_i $ is $ k $ -edge-connected for every $ 1 \le i \le t $ . Problem What is the smallest integer $ t $ so that every 3-edge-connected graph has a 2-courteous coloring of size $ t $ ? It is known (see [DJS]) that $ 4 \le t \le 10 $ . It would be quite interesting if the truth were in fact $ t=4 $ . An improvement on the current upper bound would have some consequences for certain flow problems and cycle-cover problems. In general, one may define a function $ H : {\mathbb Z}^2 \rightarrow {\mathbb Z} \cup \{\infty\} $ so that $ H(a,b) $ is the smallest integer $ t $ (or $ \infty $ if none exists) so that every $ a $ -edge-connected graph has a $ b $ -courteous coloring of size $ t $ . It is known (see [DJS]) that $ H(2k+2,2k+1) = \infty $ , and that $ 2k+1 < H(2k+1,2k) < C 100^k $ . Two special cases when better values are known are $ 2 < H(4,2) < 5 $ and $ 5 < H(5,4) < 31 $ .

=== References listed by OpenProblemGarden ===
- [DJS] M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
- [Ed] J. Edmonds, Minimum Partition of a Matriod into Independent Subsets, J. Res. Nat. Bur. Standards 69B (1965) 67-72. MathSciNet
- [NW] C.S.J.A. Nash-Williams, Edge Disjoint Spanning Trees of Finite Graphs, J. London Math. Soc. 36 (1961) 445-450. MathSciNet
- [T] W.T. Tutte, On the problem of decomposing a graph into n connected factors, J. London Math. Soc. 36 (1961), 221-230. MathSciNet

=== Catalog page (statement + literature review) ===
Partitioning edge-connectivity — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The question of whether every $(a+b+2)$-edge-connected graph can have its edges partitioned into an $a$-edge-connected and a $b$-edge-connected spanning subgraph remains open. The only known partial result is via the Nash-Williams/Tutte theorem: if $G$ is $2(a+b)$-edge-connected, one can pack $a+b$ edge-disjoint spanning trees and assign $a$ to one part and $b$ to the other. No published paper appears to have closed the gap between $a+b+2$ and $2(a+b)$.

 Reviewer notes. The DJS paper (DeVos-Johnson-Seymour 'Cut-coloring and circuit covering') predates the 2007 posting date and is background, not new progress. The Princeton PDF (DJS) could not be parsed as text. The OPG page itself was unreachable (ECONNREFUSED). No arXiv or journal paper post-2007 specifically advancing the (a+b+2) partition conjecture was found across four search queries; the problem is likely still open but a definitive survey or MathSciNet search could confirm.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Question. Let $ G $ be an $ (a+b+2) $ - edge-connected graph. Does there exist a partition $ \{A,B\} $ of $ E(G) $ so that $ (V,A) $ is $ a $ -edge-connected and $ (V,B) $ is $ b $ -edge-connected?

Keywords:
edge-coloring · edge-connectivity

Discussion

By the Nash-Williams/Tutte theorem ([NW] or [T]) on disjoint spanning trees, the above conjecture is true if $ G $ is $ 2(a+b) $ -edge-connected. This is the only partial result I know of. Here is a related conjecture. Conjecture There exists a fixed integer $ k $ so that every $ k $ -edge-connected graph $ G=(V,E) $ has a subset of edges $ S $ with the property that every edge-cut of $ G $ has between $ \frac{1}{3} $ and $ \frac{2}{3} $ of its edges in $ S $ . The values $ \frac{1}{3} $ and $ \frac{2}{3} $ are of no special importance in the above conjecture. Indeed, an affirmative answer to the above problem with $ \frac{1}{3} $ and $ \frac{2}{3} $ replaced by $ \frac{1}{t} $ and $ 1 - \frac{1}{t} $ for any $ t > 0 $ would still be valuable - and in particular, would imply the 2+epsilon flow conjecture . Definition: Let $ G=(V,E) $ be a graph and let $ P=\{E_1,E_2,...,E_t\} $ be a partition of $ E $ . We say that $ P $ is $ k $ -courteous if $ G \setminus E_i $ is $ k $ -edge-connected for every $ 1 \le i \le t $ . Problem What is the smallest integer $ t $ so that every 3-edge-connected graph has a 2-courteous coloring of size $ t $ ? It is known (see [DJS]) that $ 4 \le t \le 10 $ . It would be quite interesting if the truth were in fact $ t=4 $ . An improvement on the current upper bound would have some consequences for certain flow problems and cycle-cover problems. In general, one may define a function $ H : {\mathbb Z}^2 \rightarrow {\mathbb Z} \cup \{\infty\} $ so that $ H(a,b) $ is the smallest integer $ t $ (or $ \infty $ if none exists) so that every $ a $ -edge-connected graph has a $ b $ -courteous coloring of size $ t $ . It is known (see [DJS]) that $ H(2k+2,2k+1) = \infty $ , and that $ 2k+1 < H(2k+1,2k) < C 100^k $ . Two special cases when better values are known are $ 2 < H(4,2) < 5 $ and $ 5 < H(5,4) < 31 $ .

Bibliography

 [DJS]
 M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
 Cut-coloring and circuit covering

 [Ed]
 J. Edmonds, Minimum Partition of a Matriod into Independent Subsets, J. Res. Nat. Bur. Standards 69B (1965) 67-72. MathSciNet
 MathSciNet

 [NW]
 C.S.J.A. Nash-Williams, Edge Disjoint Spanning Trees of Finite Graphs, J. London Math. Soc. 36 (1961) 445-450. MathSciNet
 MathSciNet

 [T]
 W.T. Tutte, On the problem of decomposing a graph into n connected factors, J. London Math. Soc. 36 (1961), 221-230. MathSciNet
 MathSciNet

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove two order-dependent sufficient bounds and the Eulerian case a=b=2, but do not settle the full additive-2 conjecture.",
  "would_publish": false,
  "caveats": "The general bounds depend on the number of vertices; the exact special case requires Eulerian parity, and no novelty is claimed."
}
```

## 1. Partial results

Let \(G\) be a finite undirected graph, with parallel edges permitted, and let \(n=|V(G)|\ge 2\). Loops can be discarded and assigned arbitrarily afterward. Write
\[
\delta_G(X)=\{uv\in E(G):u\in X,\ v\notin X\},
\qquad
\lambda(G)=\min_{\varnothing\ne X\subsetneq V(G)}|\delta_G(X)|.
\]
Assume \(a,b\) are positive integers.

The desired partition is equivalent to finding \(A\subseteq E(G)\) such that, for every nontrivial \(X\subset V(G)\),
\[
a\le |A\cap\delta_G(X)|\le |\delta_G(X)|-b.
\]

I obtain the following partial results.

### A. A general bound approaching \(a+b\) when \(a+b\gg\log n\)

Put
\[
s=a+b,\qquad
\rho=\frac{ab}{a+b},\qquad
L=\log(4n^4),
\]
where logarithms are natural. The required partition exists if
\[
\boxed{\quad
\lambda(G)\ge
s+\left\lceil \sqrt{8\rho L}+\frac{16}{3}L\right\rceil .
\quad} \tag{1}
\]

Thus a sufficient connectivity is
\[
a+b+O\!\left(\sqrt{\min(a,b)\log n}+\log n\right).
\]
In particular, if \((a+b)/\log n\to\infty\), this is an \((a+b)+o(a+b)\) bound.

### B. A smaller order-dependent surplus when one target is \(1\)

Define
\[
r_n=\min\left\{r\in\mathbb Z:
r\ge9,\quad r\log\frac{r}{3e}\ge \log(4n^4)\right\}.
\]
If
\[
\boxed{\quad \lambda(G)\ge b+r_n,\quad} \tag{2}
\]
then \(G\) has a spanning tree \(T\) such that \(G-E(T)\) is \(b\)-edge-connected. Moreover,
\[
r_n=(4+o(1))\frac{\log n}{\log\log n}.
\]
The symmetric assertion holds when \(b=1\).

### C. An Eulerian improvement, including an exact conjectured case

If \(G\) is Eulerian and \(a,b\) are positive even integers, then the required partition exists whenever
\[
\boxed{\quad \lambda(G)\ge 2(a+b)-2.\quad} \tag{3}
\]

In particular:

> **Every Eulerian \(6\)-edge-connected graph has an edge partition into two \(2\)-edge-connected spanning subgraphs.**

This proves the conjectured threshold for the Eulerian case \(a=b=2\).

Each sufficient bound can, of course, be combined with the supplied Nash–Williams/Tutte bound by taking the better of it and \(2(a+b)\). I do not claim these elementary partial results are new.

---

## 2. A cut-counting lemma

The probabilistic arguments use the following fact, for which a proof is included.

### Lemma 1

If \(G\) has edge-connectivity \(\lambda>0\), then, for every integer \(j\ge1\), the number of unordered nontrivial vertex cuts of size at most \(j\lambda\) is at most
\[
n^{2j}.
\]

### Proof

If \(2j\ge n\), the total number of cuts is at most \(2^{n-1}-1\le n^{2j}\).

Suppose \(2j<n\). Repeatedly contract a uniformly random edge, discarding loops, until \(2j\) vertices remain. Fix a cut \(C\) with \(|C|\le j\lambda\).

Conditional on \(C\) surviving to a stage with \(i\) vertices, the contracted graph still has edge-connectivity at least \(\lambda\), so it has at least \(i\lambda/2\) edges. Consequently, the conditional probability of contracting an edge of \(C\) is at most \(2j/i\). Thus \(C\) survives with probability at least
\[
\prod_{i=2j+1}^{n}\left(1-\frac{2j}{i}\right)
=\binom{n}{2j}^{-1}.
\]

After contraction, choose uniformly one of the \(2^{2j-1}-1\) nontrivial cuts. Each fixed cut of size at most \(j\lambda\) is therefore output with probability at least
\[
\frac{1}{\binom{n}{2j}(2^{2j-1}-1)}.
\]
Summing these probabilities gives
\[
\#\{C:|C|\le j\lambda\}
\le \binom{n}{2j}(2^{2j-1}-1)
\le n^{2j}.
\]
\(\square\)

Here is a convenient consequence. Suppose a random construction assigns a bad event \(\mathcal B_C\) to each cut, with
\[
\Pr(\mathcal B_C)\le 2\exp\left(-L\frac{|C|}{\lambda}\right),
\qquad L=\log(4n^4).
\]
Group the cuts according to
\[
j\lambda\le |C|<(j+1)\lambda,\qquad j\ge1.
\]
Lemma 1 and the union bound give
\[
\begin{aligned}
\Pr(\text{some bad cut})
&\le 2\sum_{j\ge1}n^{2(j+1)}e^{-Lj}\\
&=\frac{2n^4e^{-L}}{1-n^2e^{-L}}\\
&=\frac{1/2}{1-1/(4n^2)}
\le \frac{8}{15}<1.
\end{aligned} \tag{4}
\]
No independence between different cuts is needed.

---

## 3. Proof of the general bound

Let
\[
\lambda=\lambda(G),\qquad d=\lambda-a-b.
\]
Independently put each edge into \(A\) with probability
\[
p=\frac{a+d/2}{\lambda},
\]
and put all other edges into \(B\).

Consider a cut \(C\) of size
\[
c=\alpha\lambda,\qquad \alpha\ge1.
\]
Let \(Z=|A\cap C|\). Its mean and variance are
\[
\mathbb EZ=\alpha(a+d/2),
\qquad
\operatorname{Var}(Z)=\alpha v,
\]
where
\[
v=\lambda p(1-p)
=\frac{(a+d/2)(b+d/2)}{a+b+d}.
\]

It suffices to ensure
\[
\alpha a\le Z\le\alpha(a+d). \tag{5}
\]
Indeed, the lower bound implies \(Z\ge a\), while the upper bound implies
\[
|B\cap C|=c-Z\ge\alpha b\ge b.
\]

The two endpoints in (5) are at distance \(\alpha d/2\) from the mean. Bernstein’s inequality for sums of independent Bernoulli variables gives
\[
\begin{aligned}
\Pr(\text{(5) fails})
&\le
2\exp\left(
-\frac{(\alpha d/2)^2}
{2(\alpha v+\alpha d/6)}
\right)\\
&=
2\exp\left(
-\alpha\frac{d^2}{8v+4d/3}
\right). \tag{6}
\end{aligned}
\]

With \(\rho=ab/(a+b)\), a direct calculation gives
\[
v
=\rho+\frac d2-
\frac{\rho d+d^2/4}{a+b+d}
\le \rho+\frac d2.
\]
Therefore
\[
8v+\frac43d\le 8\rho+\frac{16}{3}d. \tag{7}
\]

Under (1),
\[
d\ge \sqrt{8\rho L}+\frac{16}{3}L,
\]
which implies
\[
d^2\ge L\left(8\rho+\frac{16}{3}d\right). \tag{8}
\]
For example, put \(u=\sqrt{8\rho L}\) and \(w=16L/3\). Then \(d\ge u+w\) gives
\[
d(d-w)\ge u^2,
\]
which is exactly (8).

Combining (6)–(8), every cut has failure probability at most
\[
2e^{-\alpha L}
=2\exp\left(-L\frac{|C|}{\lambda}\right).
\]
By (4), with positive probability no cut fails. Such a coloring gives the required partition. \(\square\)

---

## 4. Proof of the improved bound when \(a=1\)

Independent edge sampling pays for making the first color connected. Here it is better to sample a spanning tree directly. The required rounding fact can be proved using elementary exchanges between trees.

### Lemma 2: negatively correlated tree rounding

Suppose
\[
x=\sum_{i=1}^{k}\beta_i\mathbf 1_{T_i},
\qquad
\beta_i>0,\quad \sum_i\beta_i=1,
\]
is a convex combination of spanning-tree incidence vectors. There is a random spanning tree \(T\) such that, for every \(F\subseteq E(G)\),
\[
\Pr(F\subseteq T)\le\prod_{e\in F}x_e. \tag{9}
\]

### Proof

We describe a procedure that repeatedly merges two weighted trees.

Take trees \(T_1,T_2\) of weights \(\beta_1,\beta_2\). If they differ, choose \(e\in T_1\setminus T_2\). There is an edge \(f\in T_2\setminus T_1\) such that both
\[
T_1-e+f,\qquad T_2-f+e
\]
are spanning trees: choose \(f\) on the \(T_2\)-path between the endpoints of \(e\), crossing the cut created by deleting \(e\) from \(T_1\).

Now perform one of the following updates:
\[
\begin{cases}
T_1\leftarrow T_1-e+f,
&\text{with probability }\dfrac{\beta_2}{\beta_1+\beta_2},\\[6pt]
T_2\leftarrow T_2-f+e,
&\text{with probability }\dfrac{\beta_1}{\beta_1+\beta_2}.
\end{cases}
\]
The current weighted incidence vector changes only in coordinates \(e,f\), by opposite amounts, and its conditional expectation is unchanged.

For fixed \(F\), the function
\[
\Phi_F(x)=\prod_{g\in F}x_g
\]
is concave along every line on which two coordinates change by opposite amounts and all others remain fixed. Indeed, its restriction is constant, affine, or a quadratic with nonpositive leading coefficient. Hence the conditional expectation of \(\Phi_F\) does not increase.

Each update reduces the symmetric difference of the two trees. When they agree, replace them by their common tree with weight \(\beta_1+\beta_2\). Continue until one tree remains. At termination,
\[
\Phi_F(\mathbf 1_T)=\mathbf 1_{\{F\subseteq T\}},
\]
so the preceding conditional-expectation inequalities imply (9). \(\square\)

### Applying the lemma

Let \(\lambda=\lambda(G)\) and
\[
k=\lfloor\lambda/2\rfloor.
\]
By Nash–Williams/Tutte, \(G\) has \(k\) edge-disjoint spanning trees. Apply Lemma 2 to their uniform average. Then
\[
x_e\le \frac1k
\]
for every edge.

Fix a cut \(C\) of size \(c=\alpha\lambda\), and set \(Z=|T\cap C|\). For \(\theta\ge0\), expanding the product and using (9) yields
\[
\begin{aligned}
\mathbb E e^{\theta Z}
&=\mathbb E\prod_{e\in C}
\left(1+(e^\theta-1)\mathbf 1_{\{e\in T\}}\right)\\
&\le\prod_{e\in C}\left(1+(e^\theta-1)x_e\right)\\
&\le \exp\left((e^\theta-1)\sum_{e\in C}x_e\right).
\end{aligned}
\]
Since \(\lambda\ge3\),
\[
\sum_{e\in C}x_e\le\frac ck\le 3\alpha.
\]

Let \(r=r_n\) and choose \(\theta=\log(r/3)>0\). Exponential Markov gives
\[
\begin{aligned}
\Pr(Z>r\alpha)
&\le
\exp\left[-\alpha\left(r\log(r/3)-r+3\right)\right]\\
&\le
\exp\left[-\alpha r\log\frac r{3e}\right]\\
&\le e^{-L\alpha}.
\end{aligned}
\]
The cut-union estimate (4) therefore shows that some spanning tree \(T\) satisfies
\[
|T\cap C|\le r\frac{|C|}{\lambda}
\qquad\text{for every cut }C. \tag{10}
\]

If \(\lambda\ge b+r\), then for every cut,
\[
\begin{aligned}
|\delta_{G-E(T)}(X)|
&\ge |\delta_G(X)|\left(1-\frac r\lambda\right)\\
&\ge \lambda-r\\
&\ge b.
\end{aligned}
\]
Thus \(A=E(T)\), \(B=E(G)\setminus E(T)\) is the desired partition for \(a=1\).

Finally, the definition of \(r_n\), with \(L=4\log n+O(1)\), gives
\[
r_n=(4+o(1))\frac{\log n}{\log\log n}.
\]
\(\square\)

---

## 5. Proof of the Eulerian result

The following slightly stronger formulation isolates the mechanism.

### Proposition

Let \(a,b\ge2\) be even. If an Eulerian graph \(G\) contains \(a+b-1\) edge-disjoint spanning trees, then \(G\) admits the required partition.

### Proof

Separate the packed trees into:

- \(a-1\) trees whose union is \(F_A\);
- \(b-1\) trees whose union is \(F_B\);
- one remaining tree \(T_0\).

Let \(Q\) be the set of odd-degree vertices of \(F_A\). By the handshaking lemma, \(|Q|\) is even. There is a subset \(J\subseteq E(T_0)\) whose odd-degree vertex set is exactly \(Q\).

For completeness, root \(T_0\). Include the edge from a nonroot vertex to its parent precisely when that vertex’s rooted subtree contains an odd number of vertices of \(Q\). This gives the stated parity at every vertex.

Set
\[
A=E(F_A)\cup J,\qquad B=E(G)\setminus A.
\]
Every degree in \((V,A)\) is even. Since \(G\) is Eulerian, every degree in \((V,B)\) is also even.

The graph \((V,A)\) contains \(a-1\) edge-disjoint spanning trees, so every nontrivial cut has at least \(a-1\) edges. But every cut in an even-degree graph has even size. As \(a-1\) is odd, every such cut has at least \(a\) edges.

Similarly, \((V,B)\) contains the \(b-1\) trees of \(F_B\), and all its cuts are even. Thus every nontrivial cut has at least \(b\) edges. \(\square\)

If \(\lambda(G)\ge2(a+b)-2\), Nash–Williams/Tutte supplies the required \(a+b-1\) trees. This proves (3). For \(a=b=2\), the threshold is \(6=a+b+2\).

---

## 6. What remains unresolved

These arguments do **not** prove the full conjecture.

- Bounds (1) and (2) have surplus terms that grow with \(n\); neither yields a fixed additive \(2\).
- The Eulerian proof uses parity twice. Without the assumption that \(G\) is Eulerian, making \(A\) even does not make \(B\) even, so the \(b-1\) packed trees in \(B\) need not provide \(b\)-edge-connectivity.
- In particular, these arguments do not settle the general \((a,b)=(1,2)\) case at edge-connectivity \(5\), or the non-Eulerian \((2,2)\) case at edge-connectivity \(6\).

The constant \(2\) cannot be decreased uniformly to \(1\): for \(a=b=1\), the \(3\)-edge-connected graph \(K_{3,3}\) has only \(9\) edges, whereas two edge-disjoint connected spanning subgraphs would require at least \(2(6-1)=10\).

Thus the original additive-\(2\) assertion is neither proved nor disproved here. The concrete progress is an order-dependent near-sum bound, a smaller surplus for the spanning-tree case, and the exact Eulerian \((2,2)\) case.
