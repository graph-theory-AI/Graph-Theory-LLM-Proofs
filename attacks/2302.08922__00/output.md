```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is an optimal-order linear bound for every rooted tree of height at most two, together with depth-dependent polynomial lower bounds, but the general problem contains the polynomial χ-bounding problem for induced-path-free graphs.",
  "would_publish": false,
  "caveats": "No upper bound is obtained for arbitrary rooted trees of height at least three."
}
```

## 1. Formulation

For a fixed rooted tree \((T,r)\), let
\[
f_T(t)=\sup\{\chi(G):\omega(G)\le t,\ G\text{ has no path-induced copy of }(T,r)\}.
\]
The question is whether \(f_T(t)\le C_Tt^{d_T}\) for constants \(C_T,d_T\) depending only on \((T,r)\).

The height of \((T,r)\) is \(\max_{v\in V(T)}d_T(r,v)\).

I prove that \(f_T(t)=O_T(t)\) for every rooted tree of height two, with linear growth necessary whenever the height is exactly two.

## 2. A closed-neighborhood lemma

Write \(N_H[x]=N_H(x)\cup\{x\}\).

### Lemma 1

Let \(H\) be a graph such that, for every ordered adjacent pair \(x,y\),
\[
\bigl|N_H(y)\setminus N_H[x]\bigr|\le k.
\tag{1}
\]
Then
\[
\chi(H)\le (k+1)(\omega(H)-1)+1.
\tag{2}
\]

#### Proof

We first prove that every nonempty induced subgraph \(J\) of \(H\), with \(s=\omega(J)\), satisfies
\[
\delta(J)\le (k+1)(s-1).
\tag{3}
\]
Condition (1) is inherited by induced subgraphs.

For \(s=1\), the graph \(J\) is edgeless. Suppose \(s=2\) and, to the contrary, \(\delta(J)>k+1\). Choose an edge \(xy\). With
\[
C=N_J(x)\cap N_J(y),
\]
we have
\[
d_J(y)\le 1+|C|+k.
\]
Thus \(C\ne\varnothing\), producing a triangle, a contradiction.

Now let \(s\ge3\), and assume the assertion for smaller clique number. Suppose
\[
\delta(J)>(k+1)(s-1).
\]
Choose an edge \(xy\) and put \(C=N_J(x)\cap N_J(y)\). Again \(C\ne\varnothing\). For \(v\in C\), every neighbor of \(v\) outside \(C\), other than \(x,y\), is nonadjacent to at least one of \(x,y\). Consequently,
\[
\begin{aligned}
d_{J[C]}(v)
&\ge d_J(v)-2
-\bigl|N_J(v)\setminus N_J[x]\bigr|
-\bigl|N_J(v)\setminus N_J[y]\bigr|\\
&\ge \delta(J)-2(k+1)\\
&>(k+1)(s-3).
\end{aligned}
\]
On the other hand, \(\omega(J[C])\le s-2\), since a clique in \(C\), together with \(x,y\), is a clique in \(J\). Applying induction to \(J[C]\) gives
\[
\delta(J[C])\le (k+1)(\omega(J[C])-1)\le (k+1)(s-3),
\]
a contradiction. This proves (3).

Thus every induced subgraph of \(H\) has a vertex of degree at most
\[
(k+1)(\omega(H)-1).
\]
Hence \(H\) is that-degenerate, and greedy coloring proves (2). ∎

## 3. Linear bound for rooted trees of height at most two

### Theorem 2

Let \((T,r)\) have height at most two. Let the children of \(r\) be
\[
u_1,\dots,u_m,
\]
and let \(a_i\) be the number of children of \(u_i\). Put
\[
A=\sum_{i=1}^m a_i.
\]

If \(G\) has no path-induced copy of \((T,r)\) and \(\omega(G)\le t\), then:

1. if \(A=0\), then
   \[
   \chi(G)\le m;
   \tag{4}
   \]
2. if \(A>0\), then
   \[
   \chi(G)\le (2m-1)\bigl(A(t-1)+1\bigr).
   \tag{5}
   \]

#### Proof

If \(A=0\), then \(T\) is a star rooted at its center. Any vertex of degree at least \(m\), together with \(m\) of its neighbors, gives a path-induced copy: all root paths have only one edge. Thus \(\Delta(G)\le m-1\), proving (4).

Assume now that \(A>0\), and let
\[
p=\bigl|\{i:a_i>0\}\bigr|.
\]
Thus \(1\le p\le m\).

For an ordered edge \(xy\), call \(x\to y\) bad if
\[
\bigl|N_G(y)\setminus N_G[x]\bigr|\ge A.
\tag{6}
\]

We first claim that every vertex \(x\) is the tail of at most \(m-1\) bad ordered edges. If \(d_G(x)<m\), this is immediate. Suppose \(d_G(x)\ge m\), and that there are \(p\) distinct bad neighbors
\[
y_1,\dots,y_p.
\]
Assign these vertices to the \(p\) children \(u_i\) for which \(a_i>0\). For each such \(i\), choose
\[
Z_i\subseteq N_G(y_i)\setminus N_G[x],
\qquad |Z_i|=a_i,
\]
with all the \(Z_i\)'s pairwise disjoint. This is possible greedily: every candidate set has size at least \(A\), while fewer than \(A\) vertices in total are required.

The vertices in the \(Z_i\)'s lie outside \(N_G[x]\), so they are distinct from all first-level vertices. Choose a further \(m-p\) neighbors of \(x\) for those children \(u_i\) with \(a_i=0\). This gives a copy of \(T\). Every root-to-level-two path has the form
\[
x-y_i-z,\qquad z\in Z_i,
\]
and \(xz\notin E(G)\), so this path is induced. Extra edges between different branches are irrelevant. Hence this is a path-induced copy, a contradiction. The claim follows.

Define an auxiliary graph \(B\) on \(V(G)\) by putting \(xy\in E(B)\) if \(xy\in E(G)\) and at least one of \(x\to y,y\to x\) is bad. For every \(S\subseteq V(G)\), each edge of \(B[S]\) can be assigned one of its bad orientations, and hence
\[
|E(B[S])|\le (m-1)|S|.
\]
Therefore every induced subgraph of \(B\) has average degree at most \(2m-2\), so \(B\) is \((2m-2)\)-degenerate and
\[
\chi(B)\le 2m-1.
\tag{7}
\]

Let \(S\) be a color class in a proper coloring of \(B\), and set \(H=G[S]\). If \(xy\in E(H)\), neither orientation of \(xy\) is bad. Consequently,
\[
|N_H(y)\setminus N_H[x]|
\le |N_G(y)\setminus N_G[x]|
\le A-1,
\]
and similarly with \(x,y\) interchanged. Lemma 1, with \(k=A-1\), gives
\[
\chi(H)\le A(\omega(H)-1)+1\le A(t-1)+1.
\]
Using disjoint palettes for the at most \(2m-1\) color classes of \(B\) proves (5). ∎

### Consequences

If the rooted height is exactly two, then \(A>0\). The complete graph \(K_t\) has no path-induced copy of \(T\), because any root-to-level-two path would have a chord between its ends. Thus
\[
t\le f_T(t)\le (2m-1)\bigl(A(t-1)+1\bigr).
\]
Therefore
\[
f_T(t)=\Theta_T(t)
\]
for every rooted tree of height exactly two.

For height one, the bound is independent of \(t\). Together with the standard fact that \(P_4\)-free graphs are perfect, this also settles every rooted tree on at most four vertices: the only case not covered directly by Theorem 2 is \(P_4\) rooted at an end, where a path-induced copy is exactly an induced \(P_4\).

## 4. The induced-path barrier

Let \(P_\ell\) be rooted at an endpoint. A path-induced copy of this rooted tree is exactly an induced \(P_\ell\): the full path from the root to the other endpoint must be induced. Hence
\[
f_{(P_\ell,\mathrm{end})}(t)
=
\sup\{\chi(G):\omega(G)\le t,\ G\text{ is induced-}P_\ell\text{-free}\}.
\tag{8}
\]

More generally, if \((T,r)\) has height \(h\), every path-induced copy of \(T\) contains an induced \(P_{h+1}\), namely a deepest root-to-leaf path. Therefore every induced-\(P_{h+1}\)-free graph is path-induced-\(T\)-free, and
\[
f_T(t)\ge f_{P_{h+1}}(t).
\tag{9}
\]

Thus the general question genuinely contains the polynomial χ-bounding problem for induced-path-free graphs; it is not merely superficially related to it.

## 5. Depth-dependent lower bounds

The following elementary probabilistic construction shows that the degree of a possible polynomial must grow with the rooted height.

### Proposition 3

Let \((T,r)\) have height \(h\ge4\), and set
\[
q=\left\lceil\frac{h+1}{2}\right\rceil.
\]
Then
\[
f_T(t)\ne O(t^d)
\qquad\text{for every }d<q/2.
\tag{10}
\]
More quantitatively, along an unbounded sequence of \(t\),
\[
f_T(t)=\Omega_q\!\left(\left(\frac{t}{\log t}\right)^{q/2}\right).
\tag{11}
\]

#### Proof

Fix sufficiently large \(n\), put \(p=n^{-2/q}\), and take \(R\sim G(n,p)\). Let \(X\) be the number of copies of \(K_q\). Then
\[
\mathbb E X
\le \binom nq p^{\binom q2}
\le \frac{n}{q!}.
\]
Thus with probability at least \(1-2/q!\), one has \(X\le n/2\).

Set
\[
a=\left\lceil 8n^{2/q}\log n\right\rceil.
\]
A union bound gives
\[
\begin{aligned}
\Pr(\alpha(R)\ge a)
&\le \binom na(1-p)^{\binom a2}\\
&\le
\exp\left(a\log(en/a)-\frac{p\,a(a-1)}2\right)
=o(1).
\end{aligned}
\]
Indeed, the positive term is at most \(8n^{2/q}(\log n)^2+o(n^{2/q}(\log n)^2)\), while the negative term has magnitude at least \(16n^{2/q}(\log n)^2\) for large \(n\).

Hence there exists an \(R\) with at most \(n/2\) copies of \(K_q\) and with \(\alpha(R)<a\). Delete one vertex from each remaining \(K_q\) until none remains. The resulting induced subgraph \(J\) has
\[
|V(J)|\ge n/2,\qquad \omega(J)\le q-1,\qquad \alpha(J)<a.
\]

Let \(G=\overline J\). Then
\[
\omega(G)=\alpha(J)<a
\]
and, since every independent set of \(G\) is a clique of \(J\),
\[
\chi(G)\ge \frac{|V(G)|}{q-1}\ge \frac{n}{2(q-1)}.
\tag{12}
\]

Put \(\ell=h+1\). The graph \(\overline{P_\ell}\) contains a \(K_q\): take the odd-indexed vertices of the path. Since \(J\) is \(K_q\)-free, \(G=\overline J\) is induced-\(P_\ell\)-free. By (9), \(G\) has no path-induced copy of \(T\).

Taking \(t=a=O(n^{2/q}\log n)\), inequality (12) proves (11). If an upper bound \(f_T(t)=O(t^d)\) held with \(d<q/2\), then
\[
n=O\!\left(n^{2d/q}(\log n)^d\right),
\]
which is impossible as \(n\to\infty\). ∎

For example, rooted height at least four already rules out a linear χ-bound: the construction gives growth at least \(t^{3/2-o(1)}\).

## 6. Remaining gap

The upper-bound argument relies essentially on the cardinal estimate
\[
|N(y)\setminus N[x]|\le A-1.
\]
It allows passage to common neighborhoods while losing only a bounded number of neighbors, which is exactly what drives Lemma 1.

For height three, failure of an extension naturally gives only structural or chromatic control over the relevant sets, rather than bounded cardinality. Replacing cardinality in Lemma 1 by bounded chromatic number is invalid: in a triangle-free graph, for every edge \(xy\), the set \(N(y)\setminus N[x]\) is stable, yet triangle-free graphs can have arbitrarily large chromatic number.

Thus the argument does not iterate to arbitrary height. The general conjecture, including endpoint-rooted paths of unrestricted length, remains unresolved here.