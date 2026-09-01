```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The class is determined through five vertices, a larger subgraph-closed family is proved positive via minimum-degree forcing, and strong separator-type necessary conditions are derived.",
  "would_publish": false,
  "caveats": "This does not characterize all connected graphs of order at least six and uses two standard minimum-degree theorems."
}
```

# 1. Statement of the partial results

Write \(F\preceq G\) when \(F\) is a minor of \(G\), and put

\[
f_\ell(F)=\max\{\chi_\ell(G):F\npreceq G\}.
\]

The following partial characterization can be proved.

### Theorem 1
For every graph \(H\) with \(1\le v(H)\le 5\),

\[
H\in\mathcal H
\quad\Longleftrightarrow\quad
H\not\cong K_5.
\]

Thus \(K_5\) is the unique obstruction through order five.

More generally, define \(\mathcal A\) to consist of the graphs every connected component of which is one of the following:

1. a tree;
2. a cycle;
3. a graph on at most four vertices;
4. a noncomplete graph on five vertices.

Then

\[
\mathcal A\subseteq \mathcal H.
\]

In particular, every graph of maximum degree at most two belongs to \(\mathcal H\), as do arbitrary disjoint unions of cycles, trees, and copies of graphs such as \(K_4\), \(K_5-e\), and \(K_{2,3}\).

On the negative side, the main theorem of the source paper yields the following necessary condition.

### Proposition 2
For every \(\alpha>0\), there is \(N_\alpha\) such that, if \(H\in\mathcal H\), then every subgraph \(J\subseteq H\) with \(v(J)\ge N_\alpha\) satisfies

\[
\kappa(J)<\alpha v(J).
\]

Thus every sufficiently large subgraph of a member of \(\mathcal H\) has a sublinear vertex separator.

This condition is far from sufficient: sufficiently large balanced complete bipartite graphs are not in \(\mathcal H\), and the second main theorem of the source paper gives excluded \(K_4\)-free graphs having only \(O(n\log n)\) edges.

---

# 2. A minimum-degree forcing criterion

Call a graph \(F\), of order \(r\), **degree-forced** if

\[
\delta(G)\ge r-1 \quad\Longrightarrow\quad F\preceq G
\tag{1}
\]

for every finite graph \(G\).

The relevance to list coloring is immediate.

### Lemma 3
If \(F\) is degree-forced, then

\[
f_\ell(F)=v(F)-1.
\]

#### Proof
Let \(r=v(F)\). The lower bound follows because \(K_{r-1}\) has list chromatic number \(r-1\) and cannot contain an \(r\)-vertex minor.

For the upper bound, suppose an \(F\)-minor-free graph \(G\) is not \((r-1)\)-choosable. Choose an uncolorable list assignment \(L\), with every list of size \(r-1\), and then a vertex-minimal induced subgraph \(Q\subseteq G\) that is not \(L\)-colorable.

For every \(x\in V(Q)\), the graph \(Q-x\) has an \(L\)-coloring. If \(d_Q(x)\le r-2\), at most \(r-2\) colors are used on its neighbors, so some color in the \((r-1)\)-element list \(L(x)\) remains available. This extends the coloring to \(Q\), a contradiction. Hence

\[
\delta(Q)\ge r-1.
\]

By degree-forcing, \(F\preceq Q\preceq G\), again a contradiction. Therefore every \(F\)-minor-free graph is \((r-1)\)-choosable. ∎

---

# 3. Closure under disjoint unions

We use the standard minimum-degree partition theorem:

> If \(d_1,\dots,d_s\) are nonnegative integers and
> \[
> \delta(G)\ge \sum_{i=1}^s d_i+s-1,
> \]
> then \(V(G)\) can be partitioned into sets \(V_1,\dots,V_s\) such that
> \[
> \delta(G[V_i])\ge d_i
> \]
> for every \(i\).

The two-part form is usually called the Stiebitz minimum-degree partition theorem; the displayed form follows by induction.

### Lemma 4
A disjoint union of degree-forced graphs is degree-forced.

#### Proof
Let

\[
F=F_1\dot\cup\cdots\dot\cup F_s,\qquad r_i=v(F_i),
\qquad r=\sum_i r_i,
\]

where every \(F_i\) is degree-forced. If \(\delta(G)\ge r-1\), then

\[
r-1=\sum_{i=1}^s(r_i-1)+(s-1).
\]

Apply the partition theorem with \(d_i=r_i-1\). We obtain disjoint vertex sets \(V_i\) satisfying

\[
\delta(G[V_i])\ge r_i-1.
\]

Thus \(G[V_i]\) contains an \(F_i\)-minor for each \(i\). These minor models are vertex-disjoint, and deleting edges between them produces an \(F\)-minor. ∎

This gives a useful sufficient framework: it is enough to identify connected degree-forced graphs.

---

# 4. Degree-forced building blocks

### Lemma 5
Every forest is degree-forced.

#### Proof
Let \(F\) be a forest on \(r\) vertices. Add edges between its components to obtain a tree \(T\) on the same vertex set.

Every graph of minimum degree at least \(r-1\) contains every \(r\)-vertex tree as a subgraph: root \(T\), expose its vertices in parent-before-child order, and embed greedily. When embedding a new vertex, at most \(r-2\) other host vertices have already been used, while the image of its parent has at least \(r-1\) neighbors.

Thus \(G\) contains \(T\), and hence \(F\), as a subgraph. ∎

### Lemma 6
Every cycle \(C_r\), \(r\ge3\), is degree-forced.

#### Proof
Let \(\delta(G)\ge r-1\), and take a longest path

\[
P=v_0v_1\cdots v_m.
\]

All neighbors of \(v_0\) lie on \(P\). Since \(v_0\) has at least \(r-1\) neighbors on \(P\), its neighbor of largest index has index at least \(r-1\). Consequently \(G\) has a cycle of length at least \(r\). Contracting edges on that cycle gives a \(C_r\)-minor. ∎

We also use the following standard small-minor facts:

\[
\begin{aligned}
\delta(G)&\ge2 &&\Longrightarrow K_3\preceq G,\\
\delta(G)&\ge3 &&\Longrightarrow K_4\preceq G,\\
\delta(G)&\ge4 &&\Longrightarrow K_5-e\preceq G.
\end{aligned}
\tag{2}
\]

The middle assertion is equivalent to the familiar fact that \(K_4\)-minor-free graphs are 2-degenerate. The last assertion is the standard degree-minor lemma equivalently stating that every \(K_5-e\)-minor-free graph is 3-degenerate.

### Lemma 7
Every graph \(F\) on at most four vertices is degree-forced. Every noncomplete graph \(F\) on five vertices is degree-forced.

#### Proof
For \(v(F)=r\le4\), the corresponding statement in (2) shows that every graph of minimum degree at least \(r-1\) contains a \(K_r\)-minor. Since \(F\) is a spanning subgraph of \(K_r\), it also contains an \(F\)-minor.

Now let \(v(F)=5\) and \(F\ne K_5\). Choose a nonedge \(xy\) of \(F\). Then \(F\) is a spanning subgraph of \(K_5-xy\). By (2), every graph of minimum degree at least four contains \(K_5-e\), and hence \(F\), as a minor. ∎

---

# 5. Proof of the positive family

Let \(H\in\mathcal A\), and consider an arbitrary subgraph \(H'\subseteq H\).

A connected component of \(H'\) arising from:

- a tree component of \(H\) is again a tree;
- a cycle component of \(H\) is either that cycle or a tree;
- a component of order at most five still has order at most five, and if it has five vertices it cannot become \(K_5\) unless the original component was already \(K_5\).

Thus every connected component of \(H'\) is degree-forced by Lemmas 5–7. Lemma 4 then shows that \(H'\) itself is degree-forced. By Lemma 3,

\[
f_\ell(H')=v(H')-1.
\]

Therefore \(H\in\mathcal H\), proving

\[
\mathcal A\subseteq\mathcal H.
\]

The assertion for graphs of maximum degree at most two is the special case in which every component is a path or cycle.

---

# 6. Exact classification through five vertices

If \(H\) has at most five vertices and \(H\not\cong K_5\), then every subgraph \(H'\subseteq H\) is either:

- of order at most four, or
- a noncomplete graph on five vertices.

Lemma 7 and Lemma 3 therefore give

\[
f_\ell(H')=v(H')-1
\]

for all \(H'\subseteq H\). Hence \(H\in\mathcal H\).

It remains to exclude \(K_5\). There exists a planar graph that is not 4-choosable. Every planar graph is \(K_5\)-minor-free, so

\[
f_\ell(K_5)\ge5>4=v(K_5)-1.
\]

Therefore \(K_5\notin\mathcal H\), completing the proof of Theorem 1.

In particular,

\[
H\in\mathcal H\quad\Longrightarrow\quad K_5\not\subseteq H.
\tag{3}
\]

Condition (3), however, is nowhere near sufficient.

---

# 7. Necessary separator condition

Fix \(\alpha>0\), and let

\[
\varepsilon=\frac{\alpha}{2(1+\alpha)}.
\]

The first main theorem of the source paper gives an \(N_\alpha\) such that every graph \(J\) of order at least \(N_\alpha\) satisfies

\[
f_\ell(J)\ge (1-\varepsilon)\bigl(v(J)+\kappa(J)\bigr).
\]

If \(\kappa(J)\ge\alpha v(J)\), then, writing \(m=v(J)\),

\[
\begin{aligned}
f_\ell(J)
&\ge (1-\varepsilon)(1+\alpha)m\\
&=\left(1+\frac{\alpha}{2}\right)m\\
&>m-1.
\end{aligned}
\]

Such a \(J\) cannot be a subgraph of any member of \(\mathcal H\). This proves Proposition 2.

### Concrete consequence
For \(J=K_{q,q}\),

\[
v(J)=2q,\qquad \kappa(J)=q.
\]

Taking, for example, \(\varepsilon=\tfrac14\), the source theorem gives, for sufficiently large \(q\),

\[
f_\ell(K_{q,q})
\ge \frac34(3q)
=\frac94q
>2q-1.
\]

Hence sufficiently large balanced complete bipartite graphs are not in \(\mathcal H\). These obstructions are triangle-free, showing that even the absence of all small cliques does not characterize \(\mathcal H\).

---

# 8. Sparse \(K_4\)-free negative examples

The second theorem of the source paper gives another useful corollary. Fix \(\varepsilon=\tfrac12\), and let \(C=C(\varepsilon)\). For asymptotically almost every graph \(J\) chosen uniformly among the \(n\)-vertex graphs with

\[
m=\lceil Cn\log n\rceil
\]

edges,

\[
f_\ell(J)\ge\frac32n>n-1.
\]

At the same time such a random graph is asymptotically almost surely \(K_4\)-free. Indeed, with \(N=\binom n2\),

\[
\mathbb E[\#K_4]
=
\binom n4\frac{(m)_6}{(N)_6}
=
O\!\left(n^4\left(\frac{\log n}{n}\right)^6\right)
=
O\!\left(\frac{\log^6 n}{n^2}\right)
=o(1).
\]

Consequently, for arbitrarily large \(n\), there exist \(K_4\)-subgraph-free graphs \(J\) with only \(O(n\log n)\) edges such that

\[
f_\ell(J)>v(J)-1.
\]

Thus neither bounded clique number nor ordinary sparsity is sufficient.

---

# 9. What remains open

The arguments above give only a sufficient mechanism. Degree-forcing is stronger than the desired equality: it is conceivable that an \(F\)-minor-free graph of minimum degree at least \(v(F)-1\) exists but that all such graphs remain \((v(F)-1)\)-choosable.

The principal unresolved cases begin with connected graphs on at least six vertices not covered by the tree/cycle mechanism. In particular, this writeup does not characterize:

- general cactus graphs;
- general series-parallel graphs;
- graphs obtained by repeated vertex-sums of the positive small graphs;
- all connected bipartite graphs of bounded connectivity.

The source paper's two lower bounds show that any eventual characterization must accommodate both:

1. dense, linearly connected obstructions such as large \(K_{q,q}\); and
2. \(K_4\)-free obstructions of average degree only \(\Theta(\log n)\).

Accordingly, the full structural characterization remains open.