```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for graphs with at most one odd cycle and for graphs with at most one positive adjacency eigenvalue, but the general multicyclic case remains open.",
  "would_publish": false,
  "caveats": "Graphs with at least two odd cycles and at least two positive eigenvalues are not resolved."
}
```

# 1. Statement and reformulation

Let \(G\) be a connected simple graph with \(n\) vertices, \(m\) edges, adjacency eigenvalues
\[
\lambda_1\ge \cdots\ge \lambda_n,
\]
and
\[
s^+(G)=\sum_{\lambda_i>0}\lambda_i^2,\qquad
s^-(G)=\sum_{\lambda_i<0}\lambda_i^2.
\]
Since \(\operatorname{tr}A^2=2m\),
\[
s^+(G)+s^-(G)=2m.
\]

Write
\[
c(G)=m-n+1
\]
for the cyclomatic number and set
\[
\delta(G)=s^+(G)-s^-(G)=\sum_i \lambda_i|\lambda_i|.
\]
Then
\[
s^+(G)=m+\frac{\delta(G)}2,\qquad
s^-(G)=m-\frac{\delta(G)}2,
\]
so
\[
s^+(G)-(n-1)=c(G)+\frac{\delta(G)}2,
\qquad
s^-(G)-(n-1)=c(G)-\frac{\delta(G)}2. \tag{1}
\]
Consequently,
\[
s^+(G)=n-1\iff \delta(G)=-2c(G),
\]
and
\[
s^-(G)=n-1\iff \delta(G)=2c(G). \tag{2}
\]

The easy directions are immediate:

- If \(G\) is a tree, then \(G\) is bipartite and its spectrum is symmetric, whence
  \[
  s^+(G)=s^-(G)=m=n-1.
  \]
- For \(K_n\), the spectrum is \(n-1,-1,\ldots,-1\), so
  \[
  s^-(K_n)=n-1.
  \]

The work below proves the converses for two substantial classes.

# 2. A phase integral for \(\delta(G)\)

Let
\[
\Psi_G(t)=\det(tI+iA)=\prod_{j=1}^n(t+i\lambda_j),\qquad t>0.
\]
Choose the continuous argument
\[
\theta_G(t)=\arg \Psi_G(t)
\]
with \(\theta_G(t)\to0\) as \(t\to\infty\).

## Lemma 2.1
For every graph \(G\),
\[
\delta(G)=-\frac4\pi\int_0^\infty t\,\theta_G(t)\,dt. \tag{3}
\]

### Proof

We have
\[
\theta_G'(t)
  =-\sum_{j=1}^n\frac{\lambda_j}{t^2+\lambda_j^2}.
\]
Also,
\[
\lambda|\lambda|
 =\frac2\pi\int_0^\infty\frac{\lambda^3}{t^2+\lambda^2}\,dt.
\]
Using \(\sum_j\lambda_j=\operatorname{tr}A=0\),
\[
\begin{aligned}
\delta(G)
 &=\frac2\pi\int_0^\infty
     \sum_j\frac{\lambda_j^3}{t^2+\lambda_j^2}\,dt\\
 &= -\frac2\pi\int_0^\infty
     t^2\sum_j\frac{\lambda_j}{t^2+\lambda_j^2}\,dt\\
 &=\frac2\pi\int_0^\infty t^2\theta_G'(t)\,dt.
\end{aligned}
\]
As \(t\to\infty\), the trace-zero condition gives
\(\theta_G(t)=O(t^{-3})\); as \(t\downarrow0\), \(\theta_G(t)\) is bounded. Integration by parts therefore gives (3). ∎

# 3. Graphs with exactly one odd cycle

Here “exactly one odd cycle” means exactly one odd simple cycle; the graph may have arbitrarily many even cycles attached through cut vertices.

## 3.1 Structural decomposition

Suppose \(C=v_1v_2\cdots v_\ell v_1\) is the unique odd cycle of \(G\).

There are no chords of \(C\): a chord divides \(C\) into two cycles of opposite parity, one of which is another odd cycle.

Moreover, every component of \(G-V(C)\) has neighbors in at most one vertex of \(C\). Indeed, if a component joined two distinct vertices of \(C\), a path through that component together with one of the two arcs of \(C\) would give another odd cycle.

Thus \(G\) is obtained from \(C\) by identifying each \(v_i\) with the root of a bipartite rooted graph \(H_i\). The graphs \(H_i-v_i\) are mutually disjoint. Bipartiteness of \(H_i\) follows because all neighbors of \(v_i\) in a fixed component must lie in the same side of its bipartition; otherwise a path between two such neighbors, together with \(v_i\), produces another odd cycle.

## 3.2 Eliminating the bipartite attachments

Fix \(t>0\). Put
\[
U_i=V(H_i)\setminus\{v_i\},\qquad
M_i=tI+iA_{H_i[U_i]}.
\]
Let \(b_i\) be the incidence vector of the neighbors of \(v_i\) in \(U_i\). Schur complementation gives
\[
\det(tI+iA_G)
 =\left(\prod_i\det M_i\right)
   \det(D(t)+iA_C), \tag{4}
\]
where
\[
D(t)=\operatorname{diag}(d_1(t),\ldots,d_\ell(t)),
\qquad
d_i(t)=t+b_i^{T}M_i^{-1}b_i. \tag{5}
\]

These numbers are real and satisfy
\[
d_i(t)\ge t, \tag{6}
\]
with strict inequality whenever \(H_i\ne\{v_i\}\).

Indeed, choose a bipartition of \(H_i\) in which \(v_i\) lies on the first side. In the induced graph on \(U_i\), \(b_i\) is supported on the second side. In bipartition order,
\[
M_i=
\begin{pmatrix}
tI&iB\\
iB^T&tI
\end{pmatrix}.
\]
The corresponding diagonal block of \(M_i^{-1}\) on the second side is
\[
\left(tI+t^{-1}B^TB\right)^{-1},
\]
which is real positive definite. This proves (6).

Furthermore, each \(\det M_i\) is positive: the spectrum of a bipartite graph is symmetric, so
\[
\det(tI+iA_{H_i[U_i]})
 =t^z\prod_{\mu>0}(t^2+\mu^2)>0. \tag{7}
\]
Thus the prefactor in (4) does not affect the argument.

## 3.3 The remaining odd-cycle determinant

For positive \(d_1,\ldots,d_\ell\), the determinant expansion on the chordless odd cycle gives
\[
\det(D+iA_C)
 =R_C(d_1,\ldots,d_\ell)+2i^\ell, \tag{8}
\]
where
\[
R_C(d_1,\ldots,d_\ell)
 =\sum_{M\text{ a matching of }C}
   \prod_{v_j\notin V(M)}d_j. \tag{9}
\]
The terms in (9) come from fixed points and disjoint transpositions; the two cyclic permutations give \(2i^\ell\).

Every coefficient in (9) is positive, and \(R_C\) is strictly increasing in each coordinate. Therefore, by (6),
\[
R_C(d_1(t),\ldots,d_\ell(t))
 \ge R_C(t,\ldots,t)=:\mathcal M_{C_\ell}(t), \tag{10}
\]
strictly if \(G\ne C_\ell\). Here
\[
\mathcal M_{C_\ell}(t)
 =\sum_k m_k(C_\ell)t^{\ell-2k}
\]
is the matching generating polynomial evaluated on the imaginary axis.

It follows from (4), (7), and (8) that
\[
|\theta_G(t)|
 =\arctan\!\left(
   \frac{2}{R_C(d_1(t),\ldots,d_\ell(t))}
   \right)
 \le
 \arctan\!\left(\frac{2}{\mathcal M_{C_\ell}(t)}\right)
 =|\theta_{C_\ell}(t)|. \tag{11}
\]
The signs also agree:

- if \(\ell\equiv1\pmod4\), then \(\theta_G(t)>0\) and \(\delta(G)<0\);
- if \(\ell\equiv3\pmod4\), then \(\theta_G(t)<0\) and \(\delta(G)>0\).

Combining (3) and (11) proves the following.

## Theorem 3.1
If \(G\) has a unique odd cycle \(C_\ell\), then
\[
|\delta(G)|\le |\delta(C_\ell)|,
\]
with strict inequality unless \(G=C_\ell\). Moreover, the sign of \(\delta(G)\) is positive for \(\ell\equiv3\pmod4\) and negative for \(\ell\equiv1\pmod4\).

We next compare all odd cycles with \(C_3\). We have
\[
\mathcal M_{C_3}(t)=t^3+3t.
\]
For every odd \(\ell\ge5\), the coefficient of \(t\) in
\(\mathcal M_{C_\ell}\) is \(\ell\), the coefficient of \(t^3\) is at least \(1\), and all remaining coefficients are nonnegative. Hence
\[
\mathcal M_{C_\ell}(t)>\mathcal M_{C_3}(t)
\qquad(t>0,\ \ell\ge5).
\]
Since \(C_3\) has spectrum \(2,-1,-1\),
\[
\delta(C_3)=2.
\]
The phase integral therefore yields:

## Corollary 3.2
If \(G\) has exactly one odd cycle, then
\[
|\delta(G)|\le2,
\]
and equality holds if and only if \(G=C_3\).

# 4. Equality characterization for graphs with at most one odd cycle

## Theorem 4.1
Let \(G\) be connected and suppose that \(G\) has at most one odd cycle. Then
\[
s^+(G)=n-1\iff G\text{ is a tree},
\]
and
\[
s^-(G)=n-1\iff G\text{ is a tree or }G=C_3.
\]

### Proof

If \(G\) is bipartite, then \(\delta(G)=0\), and hence
\[
s^+(G)=s^-(G)=m=n-1+c(G).
\]
Equality with \(n-1\) occurs exactly when \(c(G)=0\), namely when \(G\) is a tree.

Now suppose \(G\) has exactly one odd cycle. Then \(c(G)\ge1\) and Corollary 3.2 gives \(|\delta(G)|\le2\), with equality only for \(C_3\), where \(\delta=2\).

By (2), positive equality would require
\[
\delta(G)=-2c(G).
\]
If \(c(G)\ge2\), this contradicts \(|\delta(G)|\le2\). If \(c(G)=1\), it requires \(\delta=-2\), while the only graph with \(|\delta|=2\) is \(C_3\), for which \(\delta=2\). Thus positive equality never occurs here.

Likewise, negative equality requires \(\delta=2c(G)\). This is impossible for \(c(G)\ge2\), and for \(c(G)=1\) it occurs exactly for \(C_3\). ∎

In particular, this settles both assertions for all connected graphs with \(m\le n\), and also for graphs having one odd cycle together with arbitrarily complicated bipartite attachments.

# 5. Graphs with one positive adjacency eigenvalue

A second independent class can be settled completely.

## Lemma 5.1
A connected graph with at least two vertices has at most one positive adjacency eigenvalue if and only if it is complete multipartite.

### Proof

For a complete multipartite graph with parts \(V_1,\ldots,V_r\), put
\[
y_j=\sum_{v\in V_j}x_v.
\]
Then
\[
x^TAx=\left(\sum_jy_j\right)^2-\sum_jy_j^2,
\]
which is nonpositive on the codimension-one subspace
\(\sum_jy_j=0\). Thus there is at most one positive eigenvalue, and connectedness supplies one by Perron–Frobenius.

Conversely, a graph is complete multipartite exactly when it has no induced \(K_2\cup K_1\). If a connected non-complete-multipartite graph contains such a triple, a shortest path from the isolated vertex to the edge produces an induced \(P_4\) or an induced paw. Both have two positive eigenvalues: \(P_4\) has eigenvalues
\[
\frac{1+\sqrt5}{2},\quad \frac{\sqrt5-1}{2},
\quad-\frac{\sqrt5-1}{2},\quad-\frac{1+\sqrt5}{2},
\]
while the paw has characteristic polynomial
\[
x^4-4x^2-2x+1
\]
and has two positive roots. Interlacing then gives two positive eigenvalues in the original graph. ∎

We also need the following elementary spectral-radius bound, including its equality case.

## Lemma 5.2
If \(G\) is connected of order \(n\ge2\), size \(m\), and spectral radius \(\rho\), then
\[
\rho^2\le 2m-n+1. \tag{12}
\]
Equality holds if and only if \(G\) is a star or a complete graph.

### Proof

Let \(x>0\) be a Perron vector and choose \(v\) with \(x_v=\max_i x_i\). Then
\[
\begin{aligned}
\rho^2x_v
  &=(A^2x)_v\\
  &=\sum_{u\sim v}\sum_{w\sim u}x_w\\
  &\le x_v\sum_{u\sim v}d(u).
\end{aligned}
\]
Since every vertex outside \(N[v]\) has degree at least \(1\),
\[
\sum_{u\sim v}d(u)
 \le 2m-d(v)-(n-1-d(v))
 =2m-n+1.
\]
This proves (12).

Suppose equality holds. Equality in the last estimate says that every vertex outside \(N[v]\) has degree \(1\). Such a vertex \(z\), if present, must be joined to some \(u\in N(v)\). Equality in the Perron-vector estimate then gives \(x_z=x_v\), whereas
\[
\rho x_z=x_u\le x_v=x_z,
\]
so \(\rho\le1\). But \(v,u,z\) induce a \(P_3\), forcing
\(\rho\ge\sqrt2\), a contradiction. Thus \(v\) is universal.

Let \(H=G-v\). If \(H\) is edgeless, \(G\) is a star. Otherwise, equality forces both endpoints of every edge of \(H\) to have Perron coordinate \(x_v\). Hence the nonisolated part \(U\) of \(H\) is \(d\)-regular with
\[
d=\rho-1.
\]
Writing \(h=|U|\) and letting \(k\) be the number of isolated vertices of \(H\), the eigenvalue equation at \(v\) gives
\[
\rho=h+\frac{k}{\rho}.
\]
On the other hand, a \(d\)-regular graph has at least \(d+1=\rho\) vertices, so \(h\ge\rho\). Therefore \(h=\rho\), \(k=0\), and \(U\) is \((h-1)\)-regular on \(h\) vertices, hence complete. Thus \(G\) itself is complete. The converse equality checks are immediate. ∎

## Theorem 5.3
If \(G\) is connected and has at most one positive adjacency eigenvalue, then
\[
s^+(G)=n-1\iff G\text{ is a tree},
\]
and
\[
s^-(G)=n-1\iff G\text{ is a tree or complete}.
\]

### Proof

By Lemma 5.1, \(G=K_{a_1,\ldots,a_r}\).

There is exactly one positive eigenvalue, namely \(\rho\), so
\[
s^+(G)=\rho^2,\qquad s^-(G)=2m-\rho^2.
\]

For \(s^+\), if \(r=2\), then
\[
\rho^2=a_1a_2,
\]
and
\[
a_1a_2-(a_1+a_2-1)=(a_1-1)(a_2-1).
\]
Thus \(\rho^2=n-1\) exactly when one part has size \(1\), i.e. \(G\) is a star.

If \(r\ge3\), fix a part of size \(a\). The graph contains the spanning complete bipartite graph \(K_{a,n-a}\) as a proper subgraph. Perron–Frobenius monotonicity gives
\[
\rho(G)^2>a(n-a)\ge n-1.
\]
Thus no additional positive equality occurs.

For the negative square energy, Lemma 5.2 gives
\[
s^-(G)=2m-\rho^2\ge n-1.
\]
Equality holds exactly in the equality cases of Lemma 5.2, namely stars and complete graphs. ∎

# 6. Remaining gap

The arguments prove the conjecture for:

1. every bipartite graph;
2. every graph with exactly one odd cycle, even if it has many additional even cycles;
3. every complete multipartite graph, equivalently every connected graph with at most one positive adjacency eigenvalue.

Thus any additional equality example would necessarily have:

- cyclomatic number at least \(2\);
- at least two distinct odd cycles;
- \(\lambda_2(G)>0\).

For the positive equality, the elementary inequalities
\[
\rho^2\le s^+(G)=n-1,\qquad \rho\ge\frac{2m}{n}
\]
also imply
\[
m\le \frac n2\sqrt{n-1}.
\]

The phase method does not presently extend to general multicyclic graphs. With one odd cycle, all bipartite attachments can be eliminated into real diagonal terms \(d_i(t)\ge t\), leaving a single expression
\[
R(t)+2i^\ell
\]
whose argument has a fixed sign and admits a pointwise comparison with \(C_3\). With several interacting odd cycles, Schur complementation produces complex effective terms, while the Sachs expansion contains contributions from several odd cycles and from vertex-disjoint collections of cycles. Their phases can reinforce or cancel, and no bound strong enough to force
\[
-2c(G)<\delta(G)<2c(G)
\]
has been established here.

Using the strengthened result quoted in the supplied source abstract, an additional counterexample to the \(s^+\) assertion would also have to contain an induced claw and have diameter at least \(3\): once \(c(G)\ge2\), one has \(m\ge n+1\), and the source theorem gives \(s^+(G)\ge n\) for claw-free graphs and for graphs of diameter \(2\).