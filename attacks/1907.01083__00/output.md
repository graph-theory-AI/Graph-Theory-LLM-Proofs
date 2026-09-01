```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The intended unrestricted problem is not solved here, but K_{r+1}-free perfect graphs admit an elementary r(k-1)+1-vertex FPT kernel, while a literal ellipsoid-free reading is already handled by theta SDP with interior-point optimization.",
  "would_publish": false,
  "caveats": "The kernel assumes a clique-number bound, and interior-point SDP is not combinatorial in the customary sense."
}
```

## 1. Precise statement and interpretation

Let
\[
\textsc{Perfect-IS}=\{(G,k): G\text{ is perfect and }\alpha(G)\ge k\},
\]
where the input is promised to be perfect.

In the ordinary parameterized-complexity sense, this problem is already FPT: the known polynomial-time algorithm for maximum independent set on perfect graphs has running time \(n^{O(1)}\), which is an FPT running time with \(f(k)=1\). Thus the phrase “no combinatorial FPT algorithm is known” is a restriction on the type of algorithm, not an assertion that the problem's FPT status is unknown.

There is no generally accepted formal machine-model definition of “combinatorial algorithm.” The intended meaning is substantially stronger than merely “an implementation that does not invoke the ellipsoid method”: it normally excludes general LP/SDP or other continuous convex-optimization machinery.

I do not obtain an unrestricted algorithm satisfying that intended meaning.

## 2. A literal non-ellipsoid interpretation is not open

The distinction above is material. Let \(J\) be the all-ones matrix. Consider the standard theta SDP
\[
\vartheta(G)=
\max\left\{
  \langle J,X\rangle:
  \operatorname{Tr}(X)=1,\ 
  X_{uv}=0\ \text{for every }uv\in E(G),\
  X\succeq0
\right\}.
\]

### Lemma 2.1
For every graph \(G\),
\[
\alpha(G)\le \vartheta(G)\le \chi(\overline G).
\]

#### Proof

If \(S\) is an independent set of size \(s\), put
\[
x=\frac{1}{\sqrt{s}}\mathbf 1_S,\qquad X=xx^\mathsf T.
\]
Then \(X\) is feasible and
\[
\langle J,X\rangle=\left(\sum_v x_v\right)^2=s.
\]
This proves the lower bound.

For the upper bound, let \(C_1,\dots,C_q\) be a partition of \(V(G)\) into cliques, where \(q=\chi(\overline G)\). Write a feasible \(X\) as a Gram matrix
\[
X_{uv}=\langle p_u,p_v\rangle .
\]
Within each \(C_i\), the vectors \(p_v\) are mutually orthogonal because the corresponding pairs are edges of \(G\). Therefore, with \(z_i=\sum_{v\in C_i}p_v\),
\[
\|z_i\|^2=\sum_{v\in C_i}\|p_v\|^2.
\]
Consequently,
\[
\begin{aligned}
\langle J,X\rangle
 &=\left\|\sum_{v\in V(G)}p_v\right\|^2\\
 &=\left\|\sum_{i=1}^q z_i\right\|^2\\
 &\le q\sum_{i=1}^q\|z_i\|^2\\
 &=q\sum_v\|p_v\|^2
 =q\operatorname{Tr}(X)
 =q.
\end{aligned}
\]
This proves the upper bound. ∎

By the Weak Perfect Graph Theorem, the complement of a perfect graph is perfect. Hence, for perfect \(G\),
\[
\chi(\overline G)=\omega(\overline G)=\alpha(G),
\]
and Lemma 2.1 gives
\[
\vartheta(G)=\alpha(G).
\]

This SDP is particularly well conditioned:

- \(X=I/n\) is strictly primal feasible.
- Its feasible region is compact because \(X\succeq0\) and \(\operatorname{Tr}(X)=1\).
- In the dual, taking all edge multipliers to be zero and the trace multiplier to be \(n+1\) gives the strictly positive definite slack
  \[
  (n+1)I-J\succ0.
  \]

Thus a standard finite-precision primal-dual interior-point method approximates \(\vartheta(G)\) to additive error, say, \(1/4\), in polynomial time. Since \(\vartheta(G)=\alpha(G)\) is an integer, rounding recovers \(\alpha(G)\) exactly.

A maximum independent set can then be recovered by self-reduction. For an induced subgraph \(H\), let \(a=\alpha(H)\), choose \(v\in V(H)\), and compute \(b=\alpha(H-v)\). Since
\[
a-1\le b\le a,
\]
either:

- \(b=a\), in which case discard \(v\); or
- \(b=a-1\), in which case every maximum independent set contains \(v\), and
  \[
  \alpha(H-N_H[v])=a-1.
  \]
  Add \(v\) to the answer and recurse on \(H-N_H[v]\).

All induced subgraphs remain perfect, and at most \(n\) theta computations are needed.

Therefore, if “combinatorial” were defined literally as “does not use the ellipsoid method,” an ellipsoid-free polynomial algorithm already follows from theta plus a path-following SDP method. This is not considered a solution to the intended problem, because it merely replaces one general convex-optimization technique by another.

## 3. A discrete min-max formulation

For a perfect graph \(G\), the clique-cover number satisfies
\[
\overline\chi(G)=\chi(\overline G)
=\omega(\overline G)
=\alpha(G).
\]
Consequently, for every \(k\), exactly one of the following holds:

1. \(G\) contains an independent set of size \(k\);
2. \(V(G)\) can be partitioned into at most \(k-1\) cliques.

Indeed, the second alternative prevents an independent set from taking \(k\) vertices, while if \(\alpha(G)<k\), perfection of \(\overline G\) supplies such a clique partition.

Thus a natural fully discrete version of the FPT challenge is:

> Given a perfect graph \(G\) and \(k\), find either an independent set of size \(k\) or a partition of \(V(G)\) into at most \(k-1\) cliques, in time \(f(k)n^{O(1)}\), without LP/SDP machinery.

I do not solve this total-search problem.

## 4. A bounded-clique combinatorial FPT result

The following elementary special case gives a genuine combinatorial FPT algorithm.

### Theorem 4.1
Let \(r,k\ge1\). On the promise class of perfect graphs satisfying
\[
\omega(G)\le r,
\]
the problem of finding an independent set of size \(k\) has a kernel with at most
\[
N=r(k-1)+1
\]
vertices. A witness can be found in time
\[
O\!\left(n+m+N^2+k^2\binom Nk\right)
 =O\!\left(n+m+(er)^k\operatorname{poly}(k,r)\right).
\]

#### Proof

Every induced subgraph \(H\) of \(G\) is perfect and satisfies
\[
\chi(H)=\omega(H)\le r.
\]
Hence every such \(H\) has an independent set of size at least
\[
\left\lceil\frac{|V(H)|}{r}\right\rceil.
\]

If \(n\ge N\), choose an arbitrary set \(U\subseteq V(G)\) of exactly \(N\) vertices. Then
\[
\alpha(G[U])
 \ge \left\lceil\frac{r(k-1)+1}{r}\right\rceil
 =k.
\]
Thus both \(G\) and \(G[U]\) are yes-instances.

If \(n<N\), take \(U=V(G)\). Therefore, in all cases the induced graph \(G[U]\), with \(|U|\le N\), is an equivalent instance under the promise.

Finally, enumerate the \(k\)-subsets of \(U\), checking each in \(O(k^2)\) time. Since \(N\le rk\),
\[
\binom Nk\le \left(\frac{eN}{k}\right)^k\le (er)^k.
\]
The enumeration finds a witness whenever one exists. ∎

### Corollary 4.2
For every computable function \(g\), independent set is combinatorially FPT, parameterized by \(k\), on perfect graphs satisfying
\[
\omega(G)\le g(k).
\]

No coloring algorithm is required: perfection is used only to prove that the exhaustive search on the small induced subgraph must succeed.

## 5. Why this does not extend immediately

The bounded-clique assumption cannot simply be dropped. For example, let
\[
G_n=\overline{P_n}.
\]
Since paths are bipartite and hence perfect, \(G_n\) is perfect. Moreover,
\[
\alpha(G_n)=\omega(P_n)=2,
\qquad
\omega(G_n)=\alpha(P_n)=\left\lceil\frac n2\right\rceil.
\]
Thus, for every fixed \(k\ge3\), the graphs \(G_n\) form arbitrarily large no-instances with unbounded clique number. They also show that the inequality
\[
n\le \alpha(G)\omega(G)
\]
for perfect graphs is asymptotically tight in the relevant regime.

Furthermore, certifying the hypothesis \(\omega(G)\le r\) is itself a maximum-clique problem on perfect graphs, equivalent under complementation to the original optimization problem. The theorem is therefore a promise-class result, not an unrestricted branching rule.

## 6. Gaps and conclusion

The rigorous conclusions are:

- In the ordinary complexity sense, perfect-graph independent set is already polynomial-time and therefore FPT.
- If “non-ellipsoid” is interpreted literally, theta plus an interior-point SDP algorithm already supplies a polynomial non-ellipsoid solution.
- Under the customary, stronger meaning of “combinatorial,” the unrestricted polynomial and FPT questions remain unresolved here.
- A genuinely combinatorial FPT kernel exists when the clique number is bounded by a function of the target size.

The missing step is an entirely discrete way to handle perfect graphs with arbitrarily large clique number, such as the family above, without invoking theta, LP/SDP optimization, or an equivalent maximum-clique subroutine.