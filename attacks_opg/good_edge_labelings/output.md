```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An increasing-walk potential gives a sharp logarithmic density bound, and local extension arguments establish the critical-graph finiteness assertion for c <= 5/2.",
  "would_publish": false,
  "caveats": "Novelty has not been verified; the full critical-graph conjecture and exact extremal values for general orders are not resolved here."
}
```

## 1. Results obtained

I use precisely the distinct-label definition in the question. Write
\[
f(n)=\max\{|E(G)|:|V(G)|=n,\ G\text{ has a good edge labeling}\}.
\]

The following are self-contained consequences of that definition.

**Theorem 1.** For every \(n\ge1\),
\[
\frac n2\log_2 n-\frac n2
\;\le\; f(n)\;\le\;\frac n2\log_2 n.
\]
Moreover,
\[
f(2^k)=k2^{k-1}\qquad(k\ge1).
\]

Thus the extremal average degree is \(\log_2 n+O(1)\). In particular, without a restriction on the number of vertices, the average degree of good graphs is unbounded.

**Theorem 2.** If \(G\) is good-edge-labeling critical and
\[
G\not\cong K_3,K_{2,3},
\]
then
\[
\overline d(G)\ge\frac52.
\]
Consequently, the finiteness conjecture holds for every \(c\le5/2\).

I have not checked whether these arguments or bounds already appear in the listed literature, so I make no novelty claim. In particular, the density argument below should be checked directly rather than inferred from the supplied literature summary.

## 2. The increasing-walk potential

### 2.1. Why walks can be counted

Fix a good labeling, and replace its labels by \(1,\dots,m\), preserving their order.

An **increasing walk** is a walk whose successive edge labels strictly increase. Allow a length-zero walk at each vertex.

Every increasing walk in a good labeling is a path. Indeed, if such a walk repeated a vertex, a shortest nonempty closed segment would be a simple cycle. Its edge labels, in the order traversed, would strictly increase. Its largest-labeled edge would therefore be its only local maximum, contrary to goodness.

Consequently, for every vertex \(v\), there are at most \(n\) increasing walks ending at \(v\): the trivial walk, and at most one increasing path from each other vertex.

### 2.2. An exact recurrence

Let \(G_i\) consist of the edges with labels at most \(i\). Let
\[
a_i(v)=\#\{\text{increasing walks in }G_i\text{ ending at }v\},
\]
including the trivial walk. Initially, \(a_0(v)=1\).

Suppose edge \(i\) is \(uv\), and put
\[
a=a_{i-1}(u),\qquad b=a_{i-1}(v).
\]
Any increasing walk using edge \(i\) must use it last. Appending \(uv\) to a walk ending at \(u\), or appending \(vu\) to a walk ending at \(v\), therefore gives the exact simultaneous update
\[
a_i(u)=a+b,\qquad a_i(v)=a+b.
\]
All other values remain unchanged.

Counting **walks** here makes the recurrence unconditional: appending an edge always gives a walk. Goodness is used separately to bound the resulting counts.

Set
\[
P_i=\prod_{v\in V(G)}a_i(v).
\]
At this update,
\[
\frac{P_i}{P_{i-1}}
=\frac{(a+b)^2}{ab}\ge4.
\]
Since \(P_0=1\), we obtain \(P_m\ge4^m\). On the other hand, goodness gives \(a_m(v)\le n\), so \(P_m\le n^n\). Thus
\[
4^m\le n^n,
\]
or
\[
\boxed{m\le\frac n2\log_2 n.}
\]

This proves the upper bound in Theorem 1.

### 2.3. Hypercubes attain the bound

Let \(Q_k\) be the \(k\)-dimensional hypercube. Label its edges distinctly, with every edge in coordinate direction \(i\) preceding every edge in direction \(j\) whenever \(i<j\).

Along an increasing path, coordinate directions strictly increase. Consecutive edges cannot have the same direction, since that would immediately traverse the same edge backwards. Thus every coordinate is changed at most once.

For any ordered pair \(x,y\), an increasing path must change exactly the coordinates on which \(x\) and \(y\) differ, in increasing coordinate order. There is exactly one such path. The labeling is therefore good.

Since
\[
|V(Q_k)|=2^k,\qquad |E(Q_k)|=k2^{k-1},
\]
the upper bound is attained.

### 2.4. A lower bound for every order

For an arbitrary \(n\), take the subgraph of a sufficiently large hypercube induced by binary representations of
\[
0,1,\dots,n-1.
\]
It is good by inheritance. Its number of edges is
\[
F(n)=\sum_{j=0}^{n-1}\operatorname{wt}(j),
\]
where \(\operatorname{wt}(j)\) is the number of \(1\)-bits of \(j\).

Writing \(n=N+r\), where \(N=2^k\) and \(0\le r<N\), gives
\[
F(n)=\frac{kN}{2}+F(r)+r.
\]
The last term counts the matching edges between the two binary blocks.

Inductively,
\[
F(n)\ge\frac n2\log_2 n-\frac n2.
\]
For completeness, using \(0\log_2 0=0\), the induction step is
\[
\begin{aligned}
F(n)
&\ge \frac12\bigl(N\log_2 N+r\log_2 r\bigr)+\frac r2\\
&\ge \frac n2\log_2 n-\frac n2+\frac r2\\
&\ge \frac n2\log_2 n-\frac n2.
\end{aligned}
\]
The middle inequality follows from convexity of \(x\log_2 x\):
\[
N\log_2 N+r\log_2 r\ge n\log_2(n/2).
\]
This completes Theorem 1.

## 3. A special case of the critical-graph conjecture

The proof uses explicit extensions of good labelings.

First, \(K_3\) is bad because its cycle cannot have two local maxima. Also \(K_{2,3}\) is bad: its three length-two paths between the two degree-three vertices each increase in one of the two directions, so two increase in the same direction.

Both graphs are critical. An edge-deletion from \(K_3\) is a forest; an edge-deletion from \(K_{2,3}\) is a four-cycle with a pendant edge, which is good.

Henceforth let \(G\) be critical and different from these two graphs. It contains neither as a subgraph.

### 3.1. Minimum degree and adjacent degree-two vertices

We have \(\delta(G)\ge2\): a good labeling extends over an isolated vertex or a pendant edge, since no new cycle is created.

There cannot be adjacent degree-two vertices \(x,y\). Write their other neighbors as \(a,b\). If \(a=b\), there is a triangle. Otherwise, take a good labeling of \(G-\{x,y\}\), rescaled into \((0,1)\), and set
\[
\lambda(ax)=-2,\qquad
\lambda(yb)=-1,\qquad
\lambda(xy)=2.
\]

Every cycle meeting \(x\) or \(y\) contains the path \(a x y b\). It has a local maximum at \(xy\), and another at the largest-labeled edge of its nonempty complementary path in \(G-\{x,y\}\). This extends the labeling, a contradiction.

Thus degree-two vertices form an independent set.

### 3.2. A degree-three vertex cannot have three degree-two neighbors

Suppose \(v\) has degree three and its neighbors \(x_1,x_2,x_3\) all have degree two. Let \(u_i\) be the other neighbor of \(x_i\). By the preceding observation, all \(u_i\) lie outside
\[
\{v,x_1,x_2,x_3\}.
\]
Take a good labeling of
\[
H=G-\{v,x_1,x_2,x_3\}.
\]

There are three cases.

**All \(u_i\) coincide.** Then these vertices contain a \(K_{2,3}\), which is excluded.

**The \(u_i\) are pairwise distinct.** Rescale the labels of \(H\) into \((0,1)\). Give all three edges \(u_ix_i\) distinct negative labels and all three edges \(x_iv\) distinct labels greater than \(1\).

Every new cycle uses two arms \(u_ix_iv\) and \(vx_ju_j\), together with a nonempty path in \(H\). The larger of the two edges incident with \(v\) is a local maximum. The largest edge of the \(H\)-path is another, because its boundary edges have negative labels.

**Exactly two \(u_i\) coincide.** Write \(u_1=u_2=u\) and \(u_3=w\ne u\). Rescale the labels of \(H\) into \((10,20)\), and assign
\[
\begin{array}{c|rrrrrr}
e&ux_1&x_1v&vx_2&x_2u&wx_3&x_3v\\ \hline
\lambda(e)&2&0&3&1&-1&30.
\end{array}
\]

The four-cycle \(ux_1vx_2u\) has local maxima \(2\) and \(3\). Every other new cycle uses the third arm and one of the first two arms, together with a nonempty \(u\)-\(w\) path in \(H\). Such a cycle has a local maximum at the edge labeled \(30\), and another at the largest edge of its \(H\)-path.

These descriptions cover every new simple cycle, since a cycle through \(v\) uses exactly two of its incident edges. In both extension cases the resulting labeling is good, contradicting criticality.

We conclude:

> Every degree-three vertex of \(G\) has at most two degree-two neighbors.

### 3.3. Discharging

Give each vertex initial charge
\[
d(v)-\frac52.
\]
Every vertex of degree at least three sends charge \(1/4\) to each degree-two neighbor.

- A degree-two vertex receives \(1/4\) from each neighbor and finishes with charge \(0\).
- A degree-three vertex sends at most \(2(1/4)\), so finishes with nonnegative charge.
- A vertex of degree \(d\ge4\) finishes with charge at least
  \[
  d-\frac52-\frac d4
  =\frac{3d}{4}-\frac52\ge\frac12.
  \]

Thus the total charge is nonnegative:
\[
2|E(G)|-\frac52|V(G)|\ge0.
\]
Therefore
\[
\boxed{\overline d(G)\ge\frac52.}
\]

This proves Theorem 2, including finiteness for every \(c\le5/2\).

## 4. What remains unresolved

These arguments do **not** prove the conjecture for
\[
\frac52<c<4.
\]
In particular, the local reductions give no bound on the order of critical graphs whose average degree lies in that interval.

For density, the argument determines the leading asymptotic term and the exact answer at powers of two. It does not determine \(f(n)\) for every \(n\).

Finally, I have supplied proofs rather than a literature-status claim: whether either partial result is new requires checking the original papers.