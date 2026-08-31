```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact Ramsey-theoretic characterization is proved for a natural family of monotone 3-degenerate classes, including a nonlinear example, but the general sparse monotone case remains open.",
  "would_publish": false,
  "caveats": "The missing step is whether exclusion of the canonical obstruction below is sufficient for arbitrary bounded-degeneracy classes; the construction may overlap examples in the source."
}
```

## 1. Setup and scope

All graphs are finite and simple. A set is **2-independent** if its vertices are pairwise at distance greater than \(2\); its maximum size is denoted by \(\alpha _2(G)\). Equivalently, the closed neighborhoods of vertices in a 2-independent set are pairwise disjoint.

The intended setting is that \(\mathcal G\) is monotone, meaning closed under taking arbitrary subgraphs, and has bounded average degree. For a monotone class, bounded average degree implies bounded degeneracy.

I do not obtain a characterization of all such classes. I prove:

1. an exact characterization for a broad canonical family of monotone \(3\)-degenerate classes;
2. an explicit sparse monotone class for which domination is tied to 2-independence but \(\gamma/\alpha _2\) is unbounded;
3. a general treewidth-based sufficient condition;
4. a necessary obstruction for every sparse monotone class.

The unresolved gap is isolated in Section 6.

---

## 2. The apex–incidence construction

For a graph \(Q\), define its **apex–incidence lift** \(A(Q)\) as follows. Its vertices are
\[
\{a\}\cup V(Q)\cup \{z_e:e\in E(Q)\}.
\]
For each edge \(e=uv\in E(Q)\), add precisely the three edges
\[
az_e,\qquad uz_e,\qquad vz_e.
\]

Thus \(A(Q)\) is bipartite, with bipartition
\[
\{a\}\cup V(Q),\qquad \{z_e:e\in E(Q)\}.
\]

For a family \(\mathcal Q\), let
\[
\mathcal A(\mathcal Q)
   =\{G:G\text{ is isomorphic to a subgraph of }A(Q)
            \text{ for some }Q\in\mathcal Q\}.
\]

Every graph in \(\mathcal A(\mathcal Q)\) is \(3\)-degenerate: every nonempty subgraph either has no \(z_e\)-vertex and is edgeless, or contains a \(z_e\)-vertex of degree at most \(3\). In particular, \(\mathcal A(\mathcal Q)\) is a sparse monotone class with maximum average degree less than \(6\).

### Theorem 2.1

For every family \(\mathcal Q\), the class \(\mathcal A(\mathcal Q)\) has domination tied to 2-independence if and only if
\[
\sup_{Q\in\mathcal Q}\omega(Q)<\infty.
\]

More precisely, if \(\omega(Q)\le s\) for every \(Q\in\mathcal Q\), then every \(G\in\mathcal A(\mathcal Q)\) satisfies
\[
\gamma(G)\le R(s+1,\alpha _2(G)+1)+\alpha _2(G),
\]
where \(R\) is the ordinary Ramsey number.

### Proof: bounded clique number implies tied domination

Fix \(G\subseteq A(Q)\), where \(\omega(Q)\le s\), and put
\[
k=\alpha _2(G).
\]
Use the inherited partition
\[
X=V(G)\cap V(Q),\qquad
Z=V(G)\cap\{z_e:e\in E(Q)\},
\]
together with the apex \(a\), if it is present.

Define an auxiliary graph \(H\) on \(X\) by declaring \(xy\in E(H)\) when some \(z\in Z\) is adjacent in \(G\) to both \(x\) and \(y\). Every such edge \(xy\) is an edge of \(Q\), so
\[
H\subseteq Q[X]
\quad\text{and hence}\quad
\omega(H)\le s.
\]

If \(S\subseteq X\) is independent in \(H\), then \(S\) is 2-independent in \(G\). Indeed, there are no edges inside \(X\), and a length-two path between two vertices of \(X\) would have a middle vertex \(z\in Z\) adjacent to both, producing an edge of \(H\). Consequently,
\[
\alpha(H)\le \alpha _2(G)=k.
\]

By Ramsey's theorem,
\[
|X|<R(s+1,k+1).
\]

Now let
\[
C=X\cup\bigl(\{a\}\cap V(G)\bigr).
\]
Every edge of \(G\) has an endpoint in \(C\), so \(C\) is a vertex cover and
\[
|C|\le R(s+1,k+1).
\]

Let \(I\) be the set of isolated vertices of \(G\) belonging to \(Z\). Then
\[
D=C\cup I
\]
is a dominating set: every nonisolated \(z\in Z\) has a neighbor in \(C\), every vertex of \(C\) is selected, and every isolated \(z\) is selected. Since all vertices of \(I\) are pairwise at infinite distance,
\[
|I|\le \alpha _2(G)=k.
\]
Therefore
\[
\gamma(G)\le |D|
 \le R(s+1,k+1)+k.
\]
This proves the positive direction.

### Proof: unbounded clique number prevents tied domination

Suppose \(\mathcal Q\) has unbounded clique number. Then \(\mathcal A(\mathcal Q)\) contains
\[
L_n:=A(K_n)
\]
for every \(n\): if \(Q\) contains \(K_n\), retain the apex, its \(n\) clique vertices, and the incidence vertices corresponding to the clique edges.

For \(n\ge3\),
\[
\alpha _2(L_n)=2.
\]
Indeed:

- every two vertices in \(\{a\}\cup V(K_n)\) are at distance at most \(2\);
- every two incidence vertices \(z_e,z_f\) are at distance \(2\) through \(a\);
- hence a 2-independent set has at most one vertex of each of these two parts;
- if \(e=x_2x_3\), then \(x_1\) and \(z_e\) have distance \(3\), giving a 2-independent set of size \(2\).

On the other hand,
\[
\gamma(L_n)\ge \left\lceil\frac n2\right\rceil.
\]
To see this, consider domination of the \(n\) vertices of \(K_n\). The apex dominates none of them, a selected original vertex dominates only itself among these \(n\) vertices, and a selected incidence vertex \(z_{ij}\) dominates only \(x_i,x_j\) among them. Thus every selected vertex accounts for at most two of the \(n\) original vertices.

Therefore \(\alpha _2(L_n)=2\) while \(\gamma(L_n)\to\infty\), so no function \(h\) exists. This proves Theorem 2.1. \(\square\)

---

## 3. A sparse monotone class with a genuinely nonlinear bound

The preceding theorem gives a transparent example showing that the relaxed property is strictly weaker than a bounded ratio.

Let \(\mathcal T\) be the family of all triangle-free graphs and put
\[
\mathcal C_\triangle=\mathcal A(\mathcal T).
\]
This is a monotone \(3\)-degenerate class. Theorem 2.1 gives
\[
\gamma(G)\le R(3,\alpha _2(G)+1)+\alpha _2(G)
\qquad
(G\in\mathcal C_\triangle).
\]

Nevertheless, no constant \(c\) satisfies
\[
\gamma(G)\le c\,\alpha _2(G)
\qquad
(G\in\mathcal C_\triangle).
\]

### Lemma 3.1

There is a sequence of triangle-free graphs \(Q_i\), with no isolated vertices, such that
\[
\frac{|V(Q_i)|}{\alpha(Q_i)}\longrightarrow\infty.
\]

### Proof

For large \(N\), take a random graph \(R\sim G(N,p)\) with
\[
p=N^{-2/3},
\qquad
t=\left\lceil2N^{2/3}\log N\right\rceil.
\]

The expected number of triangles is at most
\[
\binom N3p^3\le \frac N6.
\]
Thus, by Markov's inequality, the probability of more than \(N/2\) triangles is at most \(1/3\).

The expected number of independent \(t\)-sets is at most
\[
\binom Nt(1-p)^{\binom t2}
 \le
 \exp\left(
 t\log\frac{eN}{t}
 -
 p\binom t2
 \right).
\]
For sufficiently large \(N\),
\[
\log\frac{eN}{t}\le\frac13\log N,
\qquad
\binom t2\ge\frac{t^2}{3},
\]
so this expectation tends to zero. Hence, with positive probability, \(R\) has at most \(N/2\) triangles and has no independent set of size \(t\).

Delete one vertex from each triangle. The resulting induced subgraph \(H\) is triangle-free, has at least \(N/2\) vertices, and still satisfies \(\alpha(H)<t\). The isolated vertices of \(H\) form an independent set, so fewer than \(t\) of them exist. Deleting them leaves a triangle-free graph \(Q\), with no isolated vertices, such that
\[
|V(Q)|\ge \frac N2-t\ge\frac N3
\]
for sufficiently large \(N\), while
\[
\alpha(Q)<2N^{2/3}\log N+1.
\]
Thus
\[
\frac{|V(Q)|}{\alpha(Q)}
 \ge
 \Omega\left(\frac{N^{1/3}}{\log N}\right)
 \longrightarrow\infty.
\]
\(\square\)

### Applying the lemma

For any graph \(Q\) with no isolated vertices,
\[
\alpha(Q)\le\alpha _2(A(Q))\le\alpha(Q)+1.
\]

The lower bound follows because an independent set in \(Q\), viewed among the original vertices of \(A(Q)\), is 2-independent. For the upper bound:

- at most one incidence vertex \(z_e\) can belong to a 2-independent set, since all such vertices are at distance \(2\) through the apex;
- the selected original vertices form an independent set in \(Q\);
- a 2-independent set containing the apex has size one, since every original vertex is at distance \(2\) from the apex when \(Q\) has no isolated vertices.

As in the proof for \(L_n\),
\[
\gamma(A(Q))\ge\frac{|V(Q)|}{2}.
\]
Therefore
\[
\frac{\gamma(A(Q))}
     {\alpha _2(A(Q))}
 \ge
 \frac{|V(Q)|}{2(\alpha(Q)+1)}.
\]
For the graphs supplied by Lemma 3.1, this tends to infinity. Thus \(\mathcal C_\triangle\) has domination tied to 2-independence, but its domination-to-2-independence ratio is unbounded.

This construction is likely of the same general flavor as the classes mentioned in the source; I do not claim novelty relative to those examples.

---

## 4. A general treewidth criterion

The following sufficient condition applies beyond the apex–incidence construction.

### Theorem 4.1

Every graph \(G\) satisfies
\[
\gamma(G)\le \bigl(\operatorname{tw}(G)+1\bigr)\alpha _2(G).
\]

Consequently, if a graph class \(\mathcal G\) has the property that
\[
t_{\mathcal G}(k):=
\sup\{\operatorname{tw}(G):
      G\in\mathcal G,\ \alpha _2(G)\le k\}<\infty
\]
for every \(k\), then domination is tied to 2-independence on \(\mathcal G\), with
\[
h(k)=k\bigl(t_{\mathcal G}(k)+1\bigr).
\]

### Proof

Fix a tree decomposition \((T,\{B_t:t\in V(T)\})\) of width \(w\). For a graph vertex \(x\), let
\[
T_x=\{t:x\in B_t\},
\]
which is a connected subtree of \(T\).

For each \(v\in V(G)\), define
\[
S_v=\bigcup_{x\in N[v]}T_x.
\]
This is connected: each \(T_x\), for \(x\in N(v)\), intersects \(T_v\), because some bag contains both ends of the edge \(vx\). Thus every \(S_v\) is a subtree of \(T\).

For a finite family of subtrees of a tree, the minimum number of tree vertices meeting every subtree equals the maximum number of pairwise disjoint subtrees. A short greedy proof is obtained by rooting \(T\), choosing a subtree whose highest vertex is deepest, selecting that highest vertex, and deleting all subtrees containing it. Every remaining subtree is disjoint from the chosen one.

If \(S_u\) and \(S_v\) are disjoint, then
\[
N[u]\cap N[v]=\varnothing,
\]
since any common graph vertex \(x\) would make \(T_x\subseteq S_u\cap S_v\). Hence \(u\) and \(v\) are at distance greater than \(2\). It follows that the maximum number of pairwise disjoint members of \(\{S_v\}\) is at most \(\alpha _2(G)\).

We may therefore choose at most \(\alpha _2(G)\) nodes \(t_1,\dots,t_m\) of \(T\) meeting every \(S_v\). Let
\[
D=B_{t_1}\cup\cdots\cup B_{t_m}.
\]
If \(t_i\in S_v\), then \(B_{t_i}\) contains some vertex of \(N[v]\). Thus \(D\) meets every closed neighborhood and is a dominating set. Finally,
\[
|D|\le m(w+1)\le (w+1)\alpha _2(G).
\]
\(\square\)

This criterion is only sufficient: even dense cliques have \(\gamma=\alpha _2=1\) and unbounded treewidth.

---

## 5. A necessary canonical obstruction in every monotone class

The graphs
\[
L_n=A(K_n)
\]
give a necessary condition for every monotone class, not just lift classes.

### Proposition 5.1

If a monotone class \(\mathcal G\) has domination tied to 2-independence, then there exists \(n_0\) such that no graph in \(\mathcal G\) contains \(L_{n_0}\) as a subgraph.

### Proof

If \(\gamma(G)\le h(\alpha _2(G))\) on \(\mathcal G\), choose \(n_0\) with
\[
\left\lceil\frac{n_0}{2}\right\rceil>h(2).
\]
Since
\[
\alpha _2(L_{n_0})=2,
\qquad
\gamma(L_{n_0})\ge\left\lceil\frac{n_0}{2}\right\rceil,
\]
we have \(L_{n_0}\notin\mathcal G\). Monotonicity then implies that no member of \(\mathcal G\) contains \(L_{n_0}\) as a subgraph. \(\square\)

For the apex–incidence classes of Theorem 2.1, this necessary condition is also sufficient: excluding some \(L_n\) is equivalent to bounded clique number in the base family.

---

## 6. The precise remaining gap

A natural possible route to the full sparse monotone problem is the following statement.

> **Canonical-obstruction assertion.** For all integers \(d,t,k\), there is a number \(M(d,t,k)\) such that every \(d\)-degenerate, \(L_t\)-subgraph-free graph \(G\) with \(\alpha _2(G)\le k\) satisfies
> \[
> \gamma(G)\le M(d,t,k).
> \]

If this assertion were true, then it would solve the sparse monotone problem:

- bounded average degree plus monotonicity gives a uniform degeneracy bound \(d\);
- Proposition 5.1 gives exclusion of some \(L_t\);
- the asserted bound would then provide \(h(k)=M(d,t,k)\).

I have not proved this assertion, nor found a counterexample.

Two supporting cases are covered above:

1. it holds for the apex–incidence classes;
2. it holds whenever treewidth is bounded as a function of \(\alpha _2\).

There is also a simple endpoint case. If \(G\) is \(d\)-degenerate and \(\alpha _2(G)=1\), then \(G\) is connected and has diameter at most \(2\). Choose a vertex \(v\) of degree at most \(d\). Unless \(G\) is a single vertex, the open neighborhood \(N(v)\) dominates \(G\), so
\[
\gamma(G)\le d.
\]
Thus any obstruction in a bounded-degeneracy class must begin at \(\alpha _2\ge2\), and \(L_n\) realizes failure already at \(\alpha _2=2\).

The unresolved issue is whether bounded degeneracy permits qualitatively different fixed-\(\alpha _2\), unbounded-domination obstructions that avoid every fixed \(L_t\). The arguments above do not rule out such recursive or multi-apex configurations, so the general characterization remains open.