```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For simple graphs, deferred exposure of the random rotations gives an O(log n) upper bound, while weighted simple facial cycles give a matching Omega(log n) lower bound.",
  "would_publish": true,
  "caveats": "The proof assumes finite loopless simple graphs; the corresponding multigraph statement is false."
}
```

# 1. Statement and result

Throughout, \(G=(V,E)\) is a finite simple graph, \(n=|V|\), \(m=|E|\), and
\[
\delta=\delta(G).
\]
At each vertex \(v\), independently choose a uniformly random cyclic permutation of the \(d_v\) incident darts. Let \(F(G)\) be the resulting number of faces.

The following proves the conjecture in the usual simple-graph interpretation.

## Theorem

For every fixed \(c>0\), uniformly over all simple graphs \(G\) on \(n\) vertices with \(\delta(G)\ge cn\),
\[
\frac12\log n-O_c(1)
\;\le\;
\mathbb E F(G)
\;\le\;
\left(\frac{2}{c^2}+o_c(1)\right)\log n .
\]
In particular,
\[
\mathbb E F(G)=\Theta_c(\log n).
\]

All logarithms are natural.

The upper bound in fact gives, writing \(N=2m\),
\[
\mathbb E F(G)
 \le (1+o(1))\frac{N}{\delta^2}H_N
       +O\!\left(\frac{N\sqrt{\log n}}{\delta^2}\right)+o(1),
\]
when \(\delta=\Omega(n)\). For \(K_n\), this specializes to
\[
\mathbb E F(K_n)\le (2+o(1))\log n.
\]

# 2. Permutation model and an exposure lemma

Let \(D\) be the set of \(2m\) darts. Let \(\iota\) reverse every dart, and let
\[
\rho=\prod_{v\in V}\rho_v,
\]
where \(\rho_v\) is a uniformly random \(d_v\)-cycle on the darts based at \(v\). The facial permutation is
\[
\Phi=\rho\iota,
\]
up to the immaterial choice of composition convention. Thus \(F(G)\) is the number of cycles of \(\Phi\).

We use the following standard deferred-decisions description.

## Lemma 2.1

Let \(\pi\) be a uniformly random \(d\)-cycle. Suppose \(k\le d-2\) values of \(\pi\) have been exposed and the exposed directed arcs are extendible to a \(d\)-cycle. If \(x\) is a point whose image has not yet been exposed, then \(\pi(x)\) is uniform among \(d-k-1\) admissible points.

### Proof

The exposed arcs form vertex-disjoint directed paths, isolated points being allowed. There are \(d-k\) path components. If \(x\) is the terminal point of one component, its image can be the initial point of any of the other \(d-k-1\) components. For each such choice, contracting the newly joined path leaves \(d-k-1\) components, which can be arranged into a directed cycle in exactly
\[
(d-k-2)!
\]
ways. Hence all admissible choices are equiprobable. ∎

When a face orbit is followed, every queried input of every \(\rho_v\) is new until the face closes. Indeed, the darts in a permutation orbit are distinct before the first return. Consequently Lemma 2.1 applies at every non-forced step of the face exploration.

Simplicity of \(G\) is used in the following crucial way: among the candidate darts at \(v\), at most one leads to any prescribed neighbor \(w\).

# 3. Upper bound

For a face \(C\), let
\[
r_C(v)
\]
denote the number of transitions of \(C\) occurring at \(v\), equivalently the number of darts of \(C\) based at \(v\). Thus
\[
|C|=\sum_v r_C(v).
\]

Set
\[
\theta=(\log n)^{-1/2}.
\]
For sufficiently large \(n\), \(\theta<1/2\) and \(\theta\delta\to\infty\).

Call a face \(C\) **light** if
\[
r_C(v)\le \theta d_v\qquad\text{for every }v,
\]
and heavy otherwise.

## 3.1. Light faces

Fix a dart \(a\), let \(C(a)\) be its facial cycle, and let \(L(a)=|C(a)|\).

### Lemma 3.1

For every \(\ell\ge3\),
\[
\Pr\bigl(L(a)=\ell\text{ and }C(a)\text{ is light}\bigr)
 \le \frac{1}{(1-\theta)^2\delta^2}.
\]

### Proof

Expose the orbit of \(a\) until the final two transitions needed to close it.

Let \(s\) be the base vertex of \(a\). For the face to close, the penultimate random rotation choice must choose a dart leading to \(s\). Since \(G\) is simple, there is at most one such candidate dart. The final rotation choice, at \(s\), must then choose the particular dart \(a\).

Suppose the resulting face is light. At either of these two vertices \(v\), immediately before its last transition on the face, at most \(r_C(v)-1\) images of \(\rho_v\) have been exposed. Lemma 2.1 therefore gives at least
\[
d_v-r_C(v)\ge(1-\theta)d_v\ge(1-\theta)\delta
\]
admissible choices.

The two required choices consequently have conditional probability at most
\[
\frac{1}{(1-\theta)\delta}\cdot
\frac{1}{(1-\theta)\delta}.
\]
If either required dart is inadmissible, the probability is zero, so the same bound remains valid. ∎

Faces of length one or two do not occur in a loopless simple graph of minimum degree greater than one. Using the cycle-rooting identity
\[
F_{\mathrm{light}}
 =\sum_{a\in D}\frac{\mathbf 1_{\{C(a)\text{ light}\}}}{L(a)},
\]
we obtain
\[
\begin{aligned}
\mathbb E F_{\mathrm{light}}
&\le
\sum_{a\in D}\sum_{\ell=3}^{N}
 \frac1\ell
 \Pr\bigl(L(a)=\ell,\ C(a)\text{ light}\bigr)\\
&\le
\frac{N}{(1-\theta)^2\delta^2}H_N,
\end{aligned}
\tag{3.1}
\]
where \(N=2m\).

## 3.2. A short face is very unlikely to be heavy

While exposing the orbit of a fixed dart, stop as soon as some vertex \(v\) has been queried
\[
\lfloor\theta d_v\rfloor+1
\]
times.

Before this stopping time, suppose the current query is at \(u\). Fewer than or equal to \(\lfloor\theta d_u\rfloor\) transitions have occurred at \(u\), so Lemma 2.1 leaves at least
\[
d_u-\lfloor\theta d_u\rfloor\ge(1-\theta)d_u
\]
candidate darts. Hence for every prescribed next vertex \(w\),
\[
\Pr(\text{next query is at }w\mid\text{past})
 \le \frac{1}{(1-\theta)\delta}
 \le \frac2\delta.
\tag{3.2}
\]

Let
\[
T=\left\lfloor\frac{\theta\delta^2}{100}\right\rfloor.
\]
For a fixed vertex \(w\) to become heavy, apart from possibly being the initial query vertex, it must be selected at least
\[
K_w=\lfloor\theta d_w\rfloor
 \ge \frac{\theta\delta}{2}
\]
times, for all sufficiently large \(n\).

The adaptive bound (3.2) implies
\[
\Pr(w\text{ receives at least }K_w\text{ selections in }T\text{ steps})
 \le \binom{T}{K_w}\left(\frac2\delta\right)^{K_w}.
\]
Indeed, for any fixed set of \(K_w\) selection times, the conditional probability that all select \(w\) is at most \((2/\delta)^{K_w}\). Therefore
\[
\begin{aligned}
\binom{T}{K_w}\left(\frac2\delta\right)^{K_w}
&\le
\left(\frac{2eT}{\delta K_w}\right)^{K_w}\\
&\le
\left(\frac e{25}\right)^{K_w}\\
&\le
\exp(-\gamma\theta\delta)
\end{aligned}
\tag{3.3}
\]
for an absolute constant \(\gamma>0\).

Taking a union bound over \(w\in V\), for every fixed root dart \(a\),
\[
\Pr\bigl(C(a)\text{ is heavy and }L(a)\le T\bigr)
 \le n\exp(-\gamma\theta\delta).
\tag{3.4}
\]

Consequently,
\[
\begin{aligned}
\mathbb E F_{\mathrm{heavy,short}}
&=
\sum_{a\in D}
 \mathbb E\left[
 \frac{\mathbf 1_{\{C(a)\text{ heavy},\,L(a)\le T\}}}{L(a)}
 \right]\\
&\le
Nn\exp(-\gamma\theta\delta).
\end{aligned}
\tag{3.5}
\]

## 3.3. There are deterministically few long faces

Since the facial cycles partition the \(N\) darts, the number of faces of length greater than \(T\) is at most
\[
\frac NT.
\tag{3.6}
\]

Combining (3.1), (3.5), and (3.6),
\[
\mathbb E F(G)
\le
\frac{NH_N}{(1-\theta)^2\delta^2}
+\frac NT
+Nn\exp(-\gamma\theta\delta).
\tag{3.7}
\]

If \(\delta\ge cn\), then \(N\le n^2\), \(H_N\le2\log n+O(1)\), and
\[
\frac{N}{\delta^2}\le\frac1{c^2}.
\]
Moreover,
\[
\frac NT=O_c(\sqrt{\log n})=o(\log n),
\]
and the final term in (3.7) is \(o(1)\). Thus
\[
\mathbb E F(G)
\le
\left(\frac2{c^2}+o_c(1)\right)\log n.
\tag{3.8}
\]

# 4. Lower bound from simple facial cycles

Let \(X_\ell\) be the number of faces whose boundary is a vertex-simple cycle of length \(\ell\).

For every rooted oriented simple cycle
\[
(v_0,v_1,\dots,v_{\ell-1},v_0),
\]
the event that it is a facial cycle requires, independently at each \(v_i\), one prescribed dart to be followed by another prescribed dart in \(\rho_{v_i}\). Since the successor of a fixed dart in a uniformly random \(d_{v_i}\)-cycle is uniform among the other \(d_{v_i}-1\) darts,
\[
\Pr(\text{this oriented cycle is facial})
 =
\prod_{i=0}^{\ell-1}\frac1{d_{v_i}-1}.
\]
Each oriented facial cycle has \(\ell\) choices of root, so
\[
\mathbb E X_\ell
 =
\frac1\ell
\sum_{\substack{
v_0,\ldots,v_{\ell-1}\text{ distinct}\\
v_iv_{i+1}\in E
}}
\prod_{i=0}^{\ell-1}\frac1{d_{v_i}-1}.
\tag{4.1}
\]

It suffices to replace \(d_v-1\) by \(d_v\), thereby decreasing the right-hand side.

Let \(A\) be the adjacency matrix, \(D\) the diagonal degree matrix, and
\[
S=D^{-1/2}AD^{-1/2}.
\]
Then
\[
\operatorname{tr}S^\ell
 =
\sum_{v_0v_1\cdots v_{\ell-1}v_0}
 \prod_{i=0}^{\ell-1}\frac1{d_{v_i}},
\tag{4.2}
\]
where the sum is over all rooted closed walks of length \(\ell\).

Let \(W_\ell\) be the contribution in (4.2) from walks for which
\[
v_0,\dots,v_{\ell-1}
\]
are pairwise distinct. Equation (4.1) gives
\[
\mathbb E X_\ell\ge\frac{W_\ell}{\ell}.
\tag{4.3}
\]

## 4.1. Bounding the mass of non-simple closed walks

Put
\[
P=D^{-1}A.
\]
The matrices \(P\) and \(S\) are similar, and in particular
\[
(S^r)_{vv}=P^r(v,v).
\]

For every \(r\ge1\),
\[
P^r(v,v)
 =
\sum_{u}P^{r-1}(v,u)P(u,v)
 \le \frac1\delta,
\tag{4.4}
\]
because simplicity gives \(P(u,v)\le1/\delta\).

Also, for \(t\ge2\),
\[
\operatorname{tr}S^t
 \le \sum_j|\lambda_j(S)|^t
 \le \sum_j\lambda_j(S)^2
 =\operatorname{tr}S^2
 \le\frac n\delta.
\tag{4.5}
\]

Fix two positions \(0\le i<j\le\ell-1\), and let \(r=j-i\). The total weight of closed walks satisfying \(v_i=v_j\) is
\[
\sum_v(S^r)_{vv}(S^{\ell-r})_{vv}
 \le \frac n{\delta^2},
\tag{4.6}
\]
unless one segment has length one, in which case it is zero because \(G\) has no loops.

A union bound over pairs of positions therefore shows
\[
W_\ell
 \ge
\operatorname{tr}S^\ell-B_\ell,
\qquad
B_\ell:=\binom{\ell}{2}\frac n{\delta^2}.
\tag{4.7}
\]

## 4.2. Pairing even and odd lengths

All eigenvalues of \(S\) lie in \([-1,1]\). Each connected component contributes an eigenvalue \(1\). Hence, for every \(k\ge1\),
\[
\begin{aligned}
\operatorname{tr}S^{2k}+\operatorname{tr}S^{2k+1}
&=\sum_j\lambda_j^{2k}(1+\lambda_j)\\
&\ge2.
\end{aligned}
\tag{4.8}
\]
This pairing automatically handles bipartite components: their \(-1\) eigenvalues contribute zero to (4.8), while their \(+1\) eigenvalues contribute two.

Set
\[
K=\left\lfloor\frac{\delta}{4\sqrt n}\right\rfloor.
\]
Since \(\delta\ge cn\), we have \(K=\Theta_c(\sqrt n)\). From (4.3), (4.7), and (4.8),
\[
\begin{aligned}
\mathbb E F(G)
&\ge
\sum_{k=2}^{K}\bigl(\mathbb E X_{2k}+\mathbb E X_{2k+1}\bigr)\\
&\ge
\sum_{k=2}^{K}
 \left(
 \frac{\operatorname{tr}S^{2k}}{2k}
 +
 \frac{\operatorname{tr}S^{2k+1}}{2k+1}
 \right)\\
&\qquad-
\sum_{k=2}^{K}
 \left(
 \frac{B_{2k}}{2k}
 +
 \frac{B_{2k+1}}{2k+1}
 \right)\\
&\ge
\sum_{k=2}^{K}\frac2{2k+1}-O(1).
\end{aligned}
\tag{4.9}
\]
Indeed,
\[
\sum_{k=2}^{K}
 \left(
 \frac{B_{2k}}{2k}
 +
 \frac{B_{2k+1}}{2k+1}
 \right)
<
\frac{n}{\delta^2}\sum_{k=2}^{K}2k
=O\!\left(\frac{nK^2}{\delta^2}\right)
=O(1).
\]

Finally,
\[
\sum_{k=2}^{K}\frac2{2k+1}
 =\log K+O(1)
 =\frac12\log n-O_c(1).
\]
Therefore
\[
\mathbb E F(G)\ge\frac12\log n-O_c(1).
\tag{4.10}
\]

Together, (3.8) and (4.10) prove the conjecture.

# 5. Why simplicity is essential

If “graph” permits parallel edges, the statement is false even for connected multigraphs.

Let \(n=2k\) be even. Take \(k\) disjoint dipoles, each consisting of two vertices joined by \(M=n\) parallel edges, and connect consecutive dipoles by single bridge edges. The resulting connected multigraph has \(n\) vertices and minimum degree at least \(n\).

For any orientable embedding of an \(M\)-edge dipole,
\[
F=M-2g.
\]
Since \(M\) is even and \(F>0\), necessarily \(F\ge2\).

Deleting a bridge from a rotation system separates one face into one face in each component, so joining two embedded graphs by a bridge changes the number of faces from \(F_1+F_2\) to \(F_1+F_2-1\). Consequently every rotation system of the chained multigraph satisfies
\[
F\ge 2k-(k-1)=k+1=\frac n2+1.
\]
Thus the multigraph version has \(\mathbb E F=\Omega(n)\), not \(O(\log n)\).

Hence the proof resolves the conjecture under the standard dense-simple-graph interpretation. The only remaining nonmathematical caveat is that the exact simple-graph convention in Conjecture 9.3 should be checked directly in the source text.