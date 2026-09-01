```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but every forest has a linear chromatic bound under the stronger exclusion of K_{2,t}, with explicit polynomial bounds for stars in the original setting.",
  "would_publish": false,
  "caveats": "K_{2,t}-free is strictly stronger than K_{t,t}-free for t>=3, so the balanced multipartite case is not resolved."
}
```

# 1. Statement and scope

All graphs below are finite and simple. “\(H\)-free” means having no induced copy of \(H\), whereas copies of \(K_d(t)\) are not required to be induced.

The conjecture asks whether, for every forest \(H\) and every fixed \(d\), there is a polynomial \(f_{H,d}(t)\) such that
\[
H\not\leq_{\mathrm{ind}}G,\qquad K_d(t)\not\leq G
   \quad\Longrightarrow\quad
\chi(G)\leq f_{H,d}(t).
\]

I do not prove or disprove this. I give:

1. a linear bound for every forest under the stronger exclusion of the unbalanced biclique \(K_{2,t}\);
2. explicit polynomial bounds for stars in the original balanced multipartite setting;
3. a precise identification of the smallest tree not covered by the positive results listed in the prompt;
4. a probabilistic obstruction to one natural attempt to pass from \(K_{2,t}\)-free graphs to \(K_{t,t}\)-free graphs.

# 2. Basic reductions

A clique on \(dt\) vertices contains \(K_d(t)\) as a subgraph, by partitioning its vertices into \(d\) sets of size \(t\) and deleting edges within the parts. Therefore
\[
K_d(t)\not\leq G \quad\Longrightarrow\quad \omega(G)\leq dt-1.
\tag{2.1}
\]

Also, multiboundedness is downward closed under taking induced subgraphs of the forbidden graph:

**Observation 2.1.** If \(F\leq_{\mathrm{ind}}H\) and \(H\) is multibounding, then \(F\) is multibounding.

Indeed, every \(F\)-free graph is \(H\)-free.

In particular, it is enough in principle to prove the conjecture for trees. If \(F\) is a forest with at least two components, choose one vertex in each component and add one new vertex adjacent to all the chosen vertices. The resulting graph \(T_F\) is a tree, and
\[
F\leq_{\mathrm{ind}}T_F.
\]
Thus multiboundedness of every tree would imply multiboundedness of every forest.

There is also an unavoidable linear lower bound in most cases. If \(F\) is any noncomplete forest, then \(K_{dt-1}\) is induced-\(F\)-free and contains no \(K_d(t)\), while
\[
\chi(K_{dt-1})=dt-1.
\tag{2.2}
\]

# 3. A codegree embedding lemma

For a graph \(G\), define
\[
\mu(G)=\max_{x\neq y}|N_G(x)\cap N_G(y)|.
\]

The following elementary lemma gives a useful quantitative statement for all trees.

**Lemma 3.1.**  
Let \(T\) be a tree on \(h\geq 2\) vertices, and let \(q\geq 0\). If
\[
\mu(G)\leq q
\quad\text{and}\quad
\delta(G)>(q+1)(h-2),
\]
then \(G\) contains an induced copy of \(T\).

**Proof.** Root \(T\), and order its vertices as
\[
v_1,v_2,\ldots,v_h
\]
so that, for every \(i>1\), \(v_i\) has exactly one neighbor among \(v_1,\ldots,v_{i-1}\), namely its parent.

Suppose inductively that \(v_1,\ldots,v_k\) have been embedded as an induced copy, where \(k<h\). Let \(p\) be the image of the parent of \(v_{k+1}\). We seek a vertex in \(N_G(p)\) that is outside the current copy and nonadjacent to every previously embedded vertex other than \(p\).

At most \(k-1\) vertices of \(N_G(p)\) belong to the current copy. For each previously embedded vertex \(z\neq p\), at most \(q\) vertices of \(N_G(p)\) are also adjacent to \(z\), since
\[
|N_G(p)\cap N_G(z)|\leq q.
\]
Thus the total number of forbidden candidates is at most
\[
(k-1)+q(k-1)=(q+1)(k-1)\leq(q+1)(h-2).
\]
The degree hypothesis leaves an available vertex. Adding it preserves inducedness. Iterating embeds all of \(T\). \(\square\)

Because the two hypotheses in Lemma 3.1 are inherited by induced subgraphs, it immediately yields a degeneracy bound.

**Corollary 3.2.**  
If \(T\) is a tree on \(h\geq2\) vertices, \(G\) is induced-\(T\)-free, and \(\mu(G)\leq q\), then \(G\) is \((q+1)(h-2)\)-degenerate. Consequently,
\[
\chi(G)\leq (q+1)(h-2)+1.
\tag{3.1}
\]

The same conclusion, with a slightly weaker constant, holds for arbitrary forests.

**Corollary 3.3.**  
Let \(F\) be a nonempty forest on \(h\) vertices. If \(G\) is induced-\(F\)-free and \(\mu(G)\leq q\), then
\[
\chi(G)\leq(q+1)(h-1)+1.
\tag{3.2}
\]

**Proof.** If \(F\) is connected, use Corollary 3.2. Otherwise form the tree \(T_F\) on \(h+1\) vertices described in Section 2. Since \(F\leq_{\mathrm{ind}}T_F\), an induced-\(F\)-free graph is induced-\(T_F\)-free. Corollary 3.2 applied to \(T_F\) gives
\[
\chi(G)\leq(q+1)((h+1)-2)+1=(q+1)(h-1)+1.
\]
\(\square\)

These are also list-chromatic bounds, since a \(k\)-degenerate graph is \((k+1)\)-choosable.

## 3.1. An unbalanced-biclique version of the conjecture

If \(G\) contains no \(K_{2,t}\) as a subgraph, then every pair of vertices has at most \(t-1\) common neighbors. Hence Corollary 3.3 gives:

**Theorem 3.4.**  
For every nonempty forest \(F\) on \(h\) vertices, every induced-\(F\)-free, \(K_{2,t}\)-free graph satisfies
\[
\boxed{\chi(G)\leq t(h-1)+1.}
\tag{3.3}
\]
If \(F\) is a tree on \(h\geq2\) vertices, the sharper bound
\[
\boxed{\chi(G)\leq t(h-2)+1}
\tag{3.4}
\]
holds.

Thus every forest satisfies a linear analogue of the multibounding conjecture when the forbidden balanced graph \(K_{t,t}\) is replaced by the smaller unbalanced graph \(K_{2,t}\).

For the seven-vertex spider \(S_{1,2,3}\) discussed below, (3.4) gives
\[
\chi(G)\leq 5t+1
\]
under the stronger \(K_{2,t}\)-free hypothesis.

This does not settle the original \(d=2\) problem: for \(t\geq3\), a \(K_{t,t}\)-free graph can have arbitrarily large pairwise codegree. For example, \(K_{2,N}\) is \(K_{t,t}\)-free when \(t\geq3\), regardless of \(N\).

# 4. Explicit original bounds for stars

The original conjecture has a short direct proof for stars, with an explicit polynomial.

**Proposition 4.1.**  
Let \(H=K_{1,r}\), where \(r\geq1\). If \(G\) is induced-\(H\)-free and contains no \(K_d(t)\), then
\[
\chi(G)\leq R(r,dt)
   \leq \binom{dt+r-2}{r-1}.
\tag{4.1}
\]

Here \(R(r,s)\) denotes the least integer such that every graph on \(R(r,s)\) vertices contains either a stable set of size \(r\) or a clique of size \(s\).

**Proof.** For every \(v\in V(G)\), the neighborhood \(G[N(v)]\) contains no stable set of size \(r\), since such a set together with \(v\) would induce \(K_{1,r}\). It also contains no clique of size \(dt\), by (2.1). Ramsey's theorem therefore gives
\[
|N(v)|<R(r,dt)
\]
for every \(v\). Hence
\[
\chi(G)\leq\Delta(G)+1\leq R(r,dt).
\]
The standard Ramsey recurrence gives
\[
R(r,dt)\leq \binom{dt+r-2}{r-1},
\]
which is a polynomial in \(t\) of degree \(r-1\) for fixed \(r,d\). \(\square\)

A parallel global argument handles edgeless forbidden forests. If \(H=rK_1\), then \(\alpha(G)<r\), while (2.1) gives \(\omega(G)<dt\). Consequently
\[
|V(G)|<R(r,dt)
\quad\text{and hence}\quad
\chi(G)<R(r,dt).
\]

These cases are subsumed qualitatively by the known radius-two and disjoint-union results, but (4.1) gives a completely explicit bound.

# 5. The smallest tree not covered by the listed positive results

Using only the results quoted in the prompt—paths, brooms, radius-two trees, and closure under disjoint unions—one obtains a precise small-order frontier.

Let \(S_{1,2,3}\) denote the subdivided claw whose three arms, measured from its unique degree-three vertex, have lengths \(1,2,3\). It has seven vertices and diameter five.

**Proposition 5.1.**  
The results listed in the prompt establish multiboundedness for:

1. every forest all of whose components have at most six vertices;
2. every forest all of whose components have at most seven vertices and none of whose components is \(S_{1,2,3}\).

In particular, among forests with at most seven total vertices, the only tree not covered by the listed classes is \(S_{1,2,3}\).

**Proof.**

Let \(T\) be a tree with at most six vertices.

- If \(\operatorname{diam}(T)\leq4\), then \(T\) has radius at most two.
- If \(\operatorname{diam}(T)\geq5\), then \(T\) has exactly six vertices, all lying on a diametral path, and hence \(T=P_6\).

Thus every such tree is either a path or has radius at most two.

Now let \(T\) have seven vertices.

- If its diameter is at most four, it has radius at most two.
- If its diameter is six, it is \(P_7\).
- Suppose its diameter is five. Fix a diametral path
  \[
  x_0x_1x_2x_3x_4x_5.
  \]
  The seventh vertex is a leaf attached to one of \(x_1,x_2,x_3,x_4\). Attachment at \(x_1\) or \(x_4\) gives a broom: at the unique branching vertex, all but one branches have length one. Attachment at \(x_2\) or \(x_3\) gives \(S_{1,2,3}\).

Closure under disjoint unions now gives the forest assertions. \(\square\)

This does not prove that \(S_{1,2,3}\) is not multibounding; it only identifies the first case not reached by the positive results stated in the prompt.

# 6. A blind partition reduction from \(K_{t,t}\) to \(K_{2,t}\) fails

A tempting strategy would be to partition every \(K_{t,t}\)-free graph into a bounded number of induced \(K_{2,t}\)-free graphs and then apply Theorem 3.4. Such a partition theorem is false without using the \(F\)-free hypothesis.

**Proposition 6.1.**  
For every fixed \(t\geq5\), there are \(K_{t,t}\)-free graphs requiring arbitrarily many parts in any vertex partition into induced \(K_{2,t}\)-free graphs.

**Proof.** Fix real numbers
\[
\frac{2}{t}<\alpha<\frac12,
\qquad
2\alpha<\gamma<1.
\]
Let \(G\sim G(n,p)\), where \(p=n^{-\alpha}\), and put \(m=\lceil n^\gamma\rceil\).

The expected number of copies of \(K_{t,t}\) is at most
\[
n^{2t}p^{t^2}
 =n^{2t-\alpha t^2}=o(1),
\]
since \(\alpha>2/t\). Thus \(G\) is \(K_{t,t}\)-free with probability tending to one.

We also use the elementary extremal estimate
\[
\operatorname{ex}(m,K_{2,t})=O_t(m^{3/2}).
\tag{6.1}
\]
Indeed, in a \(K_{2,t}\)-free graph,
\[
\sum_v \binom{d(v)}2
 =\sum_{\{x,y\}}|N(x)\cap N(y)|
 \leq (t-1)\binom m2,
\]
and convexity gives (6.1).

For a fixed \(m\)-vertex set \(X\), the random variable \(e(G[X])\) has mean
\[
\mu=\binom m2p=\Theta(n^{2\gamma-\alpha}).
\]
Since \(\gamma>2\alpha\),
\[
m^{3/2}=o(\mu).
\]
Hence, for sufficiently large \(n\), the event that \(G[X]\) is \(K_{2,t}\)-free implies \(e(G[X])\leq\mu/2\). A Chernoff bound gives
\[
\Pr\big(e(G[X])\leq\mu/2\big)\leq e^{-\mu/8}.
\]
There are at most
\[
\binom nm\leq \exp(O(n^\gamma\log n))
\]
choices for \(X\), while
\[
\mu=\Theta(n^{2\gamma-\alpha})
\]
and \(2\gamma-\alpha>\gamma\). A union bound therefore shows that, with probability tending to one, every \(m\)-vertex subset contains \(K_{2,t}\).

We may consequently choose \(G\) which is \(K_{t,t}\)-free and in which every \(m\)-vertex set contains \(K_{2,t}\). Every induced \(K_{2,t}\)-free subgraph then has fewer than \(m\) vertices, so any partition into such subgraphs requires at least
\[
\frac{n}{m}=n^{1-\gamma-o(1)}
\]
parts. This tends to infinity. \(\square\)

This is not a counterexample to the forest conjecture: the construction imposes no induced-\(F\)-free condition. It only shows that an extension of Theorem 3.4 must use the forbidden-forest hypothesis essentially.

# 7. Remaining gap

The principal unresolved step is the passage from bounded pairwise codegree to exclusion of a balanced complete multipartite graph. The condition
\[
K_d(t)\not\leq G
\]
allows very large common neighborhoods of fewer than \(t\) vertices; these can resemble large complete bipartite pieces and have small chromatic number individually, but there is presently no argument here that decomposes all such pieces while preserving a polynomial number of colors.

In particular, for the first tree outside the listed known classes,
\[
S_{1,2,3},
\]
the argument above proves only
\[
\chi(G)\leq5t+1
\]
under the stronger \(K_{2,t}\)-free condition. It gives no polynomial bound under the desired \(K_{t,t}\)-free condition, let alone for general \(K_d(t)\).

Thus the full conjecture remains open; no counterexample is produced.