```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The directed-cycle and two-length-2-path orientations are Eulerian-avoidable with explicit polynomial bounds, and all four orientations are avoidable in Eulerian hosts of bounded degree spread, but the unrestricted anti-directed and one-reversal orientations remain unresolved.",
  "would_publish": false,
  "caveats": "The argument does not control arbitrarily irregular Eulerian hosts for two of the four orientation types."
}
```

# 1. Statement of the partial results

Throughout, digraphs are finite, loopless, and have no parallel arcs; antiparallel pairs are harmless. Copies are not required to be induced. Write
\[
d(v)=d_D^+(v).
\]
In an Eulerian digraph, \(d_D^-(v)=d(v)\) for every \(v\).

Up to isomorphism, there are four orientations of \(C_4\):

1. The directed cycle
   \[
   F_{\rm cyc}: \quad v_0\to v_1\to v_2\to v_3\to v_0.
   \]

2. The anti-directed orientation
   \[
   F_{\rm alt}=\vec K_{2,2},
   \]
   with two sources and two sinks.

3. The orientation consisting of two directed length-two paths with common source and sink:
   \[
   F_\theta:\quad s\to x\to t,\qquad s\to y\to t.
   \]

4. The one-reversal, or shortcut, orientation:
   \[
   F_{\rm sh}:\quad s\to x\to y\to t,\qquad s\to t.
   \]

I prove the following.

**Theorem A.**

1. Every digraph of minimum out-degree at least \(64k^4\) contains an \(F_{\rm cyc}\)-free spanning subdigraph of minimum out-degree \(k\).

2. Every Eulerian digraph of minimum out-degree at least \(36k^4\) contains an \(F_\theta\)-free spanning subdigraph of minimum out-degree \(k\).

3. More generally, suppose \(D\) is Eulerian and
   \[
   \delta\le d(v)\le M\qquad\text{for every }v,
   \]
   where \(M/\delta\le R\). Then every orientation \(F\) of \(C_4\) is avoidable in this class. One valid sufficient condition is
   \[
   \delta\ge
   \max\{64,\;36,\;12(R+2),\;16R\}\,k^4.
   \]

Thus the original question is proved for two of the four orientation types, and for all four types in every bounded-degree-spread subclass of Eulerian digraphs.

I also give an explicit construction showing that the most obvious highly irregular Eulerian candidate is not a counterexample to \(F_{\rm alt}\).

# 2. A local-lemma sparsification

For every vertex \(v\), independently choose a uniformly random \(k\)-element subset
\[
X_v\subseteq E_D^+(v).
\]
Let \(H\) be the spanning subdigraph whose arcs are \(\bigcup_vX_v\). Then
\[
d_H^+(v)=k
\]
for every vertex.

For a copy \(Q\) of a fixed orientation \(F\) of \(C_4\), let \(A_Q\) be the event that all four arcs of \(Q\) are selected. If a vertex \(z\) has \(r_z\in\{0,1,2\}\) outgoing arcs in \(Q\), then
\[
\Pr(A_Q)
 =\prod_z\frac{(k)_{r_z}}{(d(z))_{r_z}}
 \le k^4\prod_zd(z)^{-r_z}.
\tag{2.1}
\]
Here \((a)_r=a(a-1)\cdots(a-r+1)\).

The event \(A_Q\) depends only on \(X_v\) for vertices which are tails of arcs of \(Q\). Consequently, two bad events are independent whenever their sets of tail vertices are disjoint.

We use the following convenient form of the asymmetric Lovász local lemma.

**Lemma 2.1.**  
Suppose a dependency graph for events \(\{A_i\}\) satisfies
\[
\sum_{j\sim i}\Pr(A_j)\le\frac14
\tag{2.2}
\]
for every \(i\), and \(\Pr(A_i)<1/2\). Then with positive probability none of the events occurs.

**Proof.** Set \(x_i=2\Pr(A_i)\). By (2.2),
\[
\sum_{j\sim i}x_j\le\frac12.
\]
Therefore
\[
\prod_{j\sim i}(1-x_j)
 \ge 1-\sum_{j\sim i}x_j
 \ge\frac12,
\]
and hence
\[
x_i\prod_{j\sim i}(1-x_j)\ge \Pr(A_i).
\]
The asymmetric local lemma applies. ∎

# 3. The directed \(C_4\)

Let \(\delta=\delta^+(D)\). For a vertex \(v\), let
\[
\Sigma(v)=\sum_{Q:\,A_Q\text{ depends on }X_v}\Pr(A_Q).
\]

Fix one prescribed role of \(v\) on a directed \(4\)-cycle. Dropping injectivity only increases the sum, so by (2.1) the corresponding contribution is at most
\[
k^4
\sum_{\substack{v\to x_1\to x_2\to x_3\\x_3\to v}}
 \frac1{d(v)d(x_1)d(x_2)d(x_3)}.
\]
The first three factors are the transition probabilities of a three-step random walk which chooses an out-neighbor uniformly at every step. The final factor satisfies \(1/d(x_3)\le1/\delta\). Thus this sum is at most \(k^4/\delta\).

There are four possible roles for \(v\), so
\[
\Sigma(v)\le \frac{4k^4}{\delta}.
\]
A directed \(C_4\)-event depends on four vertex variables. Hence the total probability of all events adjacent to a given event is at most
\[
\frac{16k^4}{\delta}.
\]
If \(\delta\ge64k^4\), this is at most \(1/4\). Lemma 2.1 gives a choice of the \(X_v\) for which no directed \(C_4\) is selected. The resulting spanning subdigraph has out-degree exactly \(k\) at every vertex.

This proves Theorem A(1); Eulerianity was not used.

# 4. The two-length-two-path orientation

Let
\[
F_\theta:\quad s\to x,\ s\to y,\ x\to t,\ y\to t.
\]
For vertices \(a,b\), write
\[
c(a,b)=|N_D^+(a)\cap N_D^+(b)|.
\]

Assume now that \(D\) is Eulerian and \(d(v)\ge\delta\) for every \(v\).

A copy with images \(s,x,y,t\) has probability at most
\[
\frac{k^4}{d(s)^2d(x)d(y)}.
\tag{4.1}
\]

## 4.1. A fixed vertex in the source role

Fix \(s=v\). Summing (4.1) over possible \(x,y,t\) gives at most
\[
k^4\sum_{x,y\in N^+(v)}
 \frac{c(x,y)}{d(v)^2d(x)d(y)}.
\]
Since
\[
c(x,y)\le\min\{d(x),d(y)\},
\]
we have
\[
\frac{c(x,y)}{d(x)d(y)}
 \le \frac1{\max\{d(x),d(y)\}}
 \le\frac1\delta.
\]
There are \(d(v)^2\) ordered choices of \(x,y\), and therefore the source-role contribution is at most
\[
\frac{k^4}{\delta}.
\tag{4.2}
\]

## 4.2. A fixed vertex in a middle role

Fix \(x=v\). The corresponding total weight is at most
\[
k^4
\sum_{s\to v}\sum_{y\in N^+(s)}
 \frac{c(v,y)}{d(s)^2d(v)d(y)}.
\]
Using \(c(v,y)\le d(y)\),
\[
\begin{aligned}
&\sum_{s\to v}\sum_{y\in N^+(s)}
 \frac{c(v,y)}{d(s)^2d(v)d(y)}
\\
&\qquad\le
\sum_{s\to v}\sum_{y\in N^+(s)}
 \frac1{d(s)^2d(v)}
\\
&\qquad=
\frac1{d(v)}\sum_{s\to v}\frac1{d(s)}
\\
&\qquad\le
\frac{d_D^-(v)}{d(v)\delta}
=\frac1\delta,
\end{aligned}
\tag{4.3}
\]
where the last equality is precisely the Eulerian hypothesis. The same bound holds for the role \(y\).

The sink \(t\) contributes no random variable. Combining (4.2) and (4.3),
\[
\Sigma(v)\le \frac{3k^4}{\delta}.
\]
Each bad event depends on three variables, so the sum of probabilities over its dependency neighborhood is at most
\[
\frac{9k^4}{\delta}.
\]
For \(\delta\ge36k^4\), Lemma 2.1 applies. Thus there is a spanning \(F_\theta\)-free subdigraph of out-degree exactly \(k\).

This proves Theorem A(2).

# 5. Conditional treatment of the shortcut orientation

Let
\[
F_{\rm sh}:\quad s\to x\to y\to t,\qquad s\to t.
\]
Define
\[
\rho(v)=\sum_{u\to v}\frac1{d(u)^2},
\qquad
\rho=\max_v\rho(v).
\tag{5.1}
\]

A copy with images \(s,x,y,t\) has probability at most
\[
\frac{k^4}{d(s)^2d(x)d(y)}.
\tag{5.2}
\]

The three tail roles have the following bounds.

- For \(s=v\), summing first over the common endpoint \(t\) gives
  \[
  \sum_{\substack{x\in N^+(v),\,y\in N^+(x)}}
  \frac{c(v,y)}{d(v)^2d(x)d(y)}
  \le \frac1\delta.
  \tag{5.3}
  \]

- For \(x=v\),
  \[
  \sum_{s\to v}\sum_{y\in N^+(v)}
  \frac{c(s,y)}{d(s)^2d(v)d(y)}
  \le
  \sum_{s\to v}\frac1{d(s)^2}
  =\rho(v).
  \tag{5.4}
  \]

- For \(y=v\), using Eulerianity twice,
  \[
  \begin{aligned}
  &\sum_{x\to v}\sum_{s\to x}
  \frac{c(s,v)}{d(s)^2d(x)d(v)}
  \\
  &\qquad\le
  \frac1{d(v)}
  \sum_{x\to v}\frac1{d(x)}
  \sum_{s\to x}\frac1{d(s)}
  \le\frac1\delta.
  \end{aligned}
  \tag{5.5}
  \]

Consequently,
\[
\Sigma(v)\le k^4\left(\frac2\delta+\rho\right).
\]
Each event depends on three variables. Therefore:

**Proposition 5.1.**  
An Eulerian digraph contains a spanning \(F_{\rm sh}\)-free subdigraph of out-degree \(k\) whenever
\[
k^4\left(\frac2\delta+\rho\right)\le\frac1{12}.
\tag{5.6}
\]

The obstruction to making this unconditional is the term \(\rho(v)\): an Eulerian vertex of very large degree may have arbitrarily many in-neighbors of degree close to the minimum degree.

# 6. Conditional treatment of the anti-directed orientation

Let \(F_{\rm alt}=\vec K_{2,2}\). Define
\[
\tau(v)=
\sum_{u\ne v}
 \frac{c(v,u)(c(v,u)-1)}{d(v)^2d(u)^2},
\qquad
\tau=\max_v\tau(v).
\tag{6.1}
\]

For a fixed source role occupied by \(v\), the weighted sum of all labelled copies is at most \(k^4\tau(v)\). Allowing for the two source roles gives the safe bound
\[
\Sigma(v)\le 2k^4\tau.
\]
An anti-directed \(C_4\)-event depends on only its two source variables. Thus the total probability in the dependency neighborhood of any event is at most
\[
4k^4\tau.
\]

Hence:

**Proposition 6.1.**  
An Eulerian digraph contains a spanning \(F_{\rm alt}\)-free subdigraph of out-degree \(k\) whenever
\[
\tau\le\frac1{16k^4}.
\tag{6.2}
\]

Unlike the preceding two orientations, this criterion genuinely fails in natural highly irregular Eulerian examples; see Section 8 below.

# 7. Eulerian hosts of bounded degree spread

Assume
\[
\delta\le d(v)\le M=R\delta.
\]

For the shortcut orientation,
\[
\rho(v)
 =\sum_{u\to v}\frac1{d(u)^2}
 \le\frac{d_D^-(v)}{\delta^2}
 =\frac{d(v)}{\delta^2}
 \le\frac R\delta.
\]
Thus Proposition 5.1 applies if
\[
\delta\ge12(R+2)k^4.
\tag{7.1}
\]

For the anti-directed orientation, observe that
\[
\sum_u c(v,u)(c(v,u)-1)
\]
counts ordered triples \((u,a,b)\) where \(a\ne b\) are both out-neighbors of \(v\) and also both out-neighbors of \(u\). For each ordered pair \(a,b\in N^+(v)\), the number of possible \(u\) is at most
\[
|N^-(a)\cap N^-(b)|\le M.
\]
Therefore
\[
\sum_u c(v,u)(c(v,u)-1)\le d(v)^2M.
\]
Since \(d(u)\ge\delta\),
\[
\tau(v)\le
\frac{d(v)^2M}{d(v)^2\delta^2}
=\frac{M}{\delta^2}
=\frac R\delta.
\]
Proposition 6.1 applies if
\[
\delta\ge16Rk^4.
\tag{7.2}
\]

Together with Sections 3 and 4, this proves Theorem A(3).

In particular, for an Eulerian regular host, \(\delta\ge64k^4\) suffices simultaneously for every orientation of \(C_4\).

# 8. Why a spanning argument cannot settle the anti-directed case

Consider the following Eulerian oriented graph \(D_{a,b}\). Its vertex classes, in cyclic order, have sizes
\[
|A_0|=a,\quad |B_0|=b,\quad |A_1|=a,\quad |B_1|=b,
\]
and all possible arcs are present in the directions
\[
A_0\to B_0\to A_1\to B_1\to A_0.
\]
Every \(A_i\)-vertex has in- and out-degree \(b\), while every \(B_i\)-vertex has in- and out-degree \(a\). Thus \(D_{a,b}\) is Eulerian with minimum out-degree \(\min\{a,b\}\).

Suppose \(H\) were a **spanning** \(F_{\rm alt}\)-free subdigraph with minimum out-degree at least \(k\), where \(k\ge2\). For every \(x\in A_0\), choose a \(k\)-set
\[
S_x\subseteq N_H^+(x)\cap B_0.
\]
If two distinct vertices \(x,x'\in A_0\) had
\[
|S_x\cap S_{x'}|\ge2,
\]
then \(x,x'\), together with two common heads, would form an anti-directed \(C_4\). Hence the family \(\{S_x:x\in A_0\}\) is linear: no unordered pair of \(B_0\) occurs in two of its members. Consequently,
\[
a\binom{k}{2}\le\binom b2.
\tag{8.1}
\]
Taking \(a>\binom b2/\binom k2\) shows that no spanning sparsification can work, even though \(b\) can be arbitrarily large.

This does not produce a counterexample to avoidability, because vertices may be deleted. Indeed, the same family has an explicit small anti-directed-\(C_4\)-free core.

Choose a power of two \(q\) with
\[
k\le q\le2k
\]
(take \(q=2\) when \(k=1\)). Suppose every class has at least \(q^2\) vertices. Select \(q^2\) vertices from each class. Between every consecutive pair of selected classes, identify the source class with the affine lines
\[
\{(m,c):m,c\in\mathbb F_q\}
\]
and the target class with the points
\[
\{(x,y):x,y\in\mathbb F_q\}.
\]
Retain the arc
\[
(m,c)\to(x,y)
\quad\Longleftrightarrow\quad
y=mx+c.
\]
Every selected vertex has out-degree \(q\), and two distinct lines have at most one common point. Thus no two sources in the same class have two common heads. Sources in different classes have heads in different next classes. The resulting subdigraph is therefore \(F_{\rm alt}\)-free and has minimum out-degree \(q\ge k\).

Hence complete cyclic blow-ups, including those with arbitrarily large degree ratio \(a/b\), are not counterexamples. What fails is only the spanning random-selection method.

# 9. Remaining gap

The unrestricted problem is not resolved here.

- \(F_{\rm cyc}\) is handled in arbitrary hosts.
- \(F_\theta\) is handled in arbitrary Eulerian hosts.
- \(F_{\rm sh}\) is handled when the inverse-square in-neighbor load \(\rho\) is small; in particular, it is handled under bounded degree spread.
- \(F_{\rm alt}\) is handled when the normalized common-out-neighborhood load \(\tau\) is small; again, bounded degree spread suffices.

For highly irregular Eulerian digraphs, \(\rho\) and \(\tau\) can be arbitrarily large compared with the minimum degree. In the anti-directed case, Section 8 shows that this is not merely a defect in the estimates: a spanning \(k\)-out selection can genuinely be impossible. A full proof would therefore need a vertex-deleting structural argument that extracts a suitably balanced Eulerian or nearly Eulerian core before applying sparsification. No such extraction lemma is established here.

Accordingly, this is a rigorous partial resolution, not a proof that every orientation of \(C_4\) is Eulerian-avoidable.