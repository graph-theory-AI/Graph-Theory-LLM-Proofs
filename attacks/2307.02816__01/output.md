```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with the optimal bound 2 for all excluded graphs of treedepth at most 2, and it also follows from the minor theorem for every subcubic excluded graph.",
  "would_publish": false,
  "caveats": "Patterns of treedepth at least 3 with several vertices of degree at least 4 remain untreated; the argument uses the standard bounded-degree tree-partition theorem."
}
```

# Mathematical writeup

## 1. Reformulation by graph partitions

An \(H\)-partition of a graph \(G\) is a partition
\[
V(G)=\bigcup_{x\in V(H)}B_x
\]
such that, for every edge \(uv\in E(G)\) with \(u\in B_x\) and \(v\in B_y\), either \(x=y\) or \(xy\in E(H)\). Its width is \(\max_x|B_x|\).

The following equivalence will be used repeatedly:

\[
G\subseteq H\boxtimes K_c
\quad\Longleftrightarrow\quad
G\text{ has an \(H\)-partition of width at most }c.
\]

Indeed, given the partition, assign distinct \(K_c\)-coordinates inside each bag. Conversely, projection onto the \(H\)-coordinate of an embedding gives such a partition.

I also use the standard bounded-degree tree-partition theorem:

> **Tree-partition lemma.**  
> For every pair \(k,\Delta\) there is an integer \(p(k,\Delta)\) such that every graph \(J\) with
> \[
> \operatorname{tw}(J)\le k,\qquad \Delta(J)\le\Delta
> \]
> has a tree-partition of width at most \(p(k,\Delta)\).

Only the finiteness of \(p(k,\Delta)\) is needed. In product language, \(J\subseteq F\boxtimes K_{p(k,\Delta)}\) for some forest \(F\).

---

## 2. The conjecture for \(\operatorname{td}(X)\le 2\)

### Theorem 1

For every graph \(X\) with \(\operatorname{td}(X)\le2\), every positive integer \(t\), and every \(X\)-topological-minor-free graph \(G\) with \(\operatorname{tw}(G)<t\), there is a graph \(H\) such that
\[
\operatorname{tw}(H)\le2
\quad\text{and}\quad
G\subseteq H\boxtimes K_{c_X(t)}
\]
for a suitable function \(c_X\).

Moreover, the uniform bound \(2\) is best possible.

### Proof: treedepth \(1\)

If \(\operatorname{td}(X)=1\), then \(X=qK_1\) for some \(q\). Every graph on at least \(q\) vertices contains \(qK_1\) as a subgraph, since unwanted edges may be deleted. Hence an \(X\)-topological-minor-free graph has at most \(q-1\) vertices. Put all vertices into one bag. Thus \(H=K_1\), and one may take
\[
\operatorname{tw}(H)=0,\qquad c_X(t)=\max\{1,q-1\}.
\]

### Proof: treedepth \(2\)

A graph has treedepth at most \(2\) if and only if it is a star forest. Write
\[
X=K_{1,d_1}\cup\cdots\cup K_{1,d_q},
\]
where \(d_i=0\) is allowed, representing an isolated vertex. Let
\[
D:=\max_i d_i.
\]

The case \(D=0\) was covered above, so assume \(D\ge1\).

If \(G\) contained \(q\) vertex-disjoint copies of \(K_{1,D}\) as ordinary subgraphs, then the \(i\)-th copy could be restricted to a copy of \(K_{1,d_i}\). Consequently, \(G\) would contain \(X\) as a subgraph, and hence as a topological minor.

Take a maximal collection of pairwise vertex-disjoint \(K_{1,D}\)-subgraphs of \(G\), and let \(S\) be the union of their vertex sets. There are at most \(q-1\) such stars, so
\[
|S|\le(q-1)(D+1).
\]
By maximality, \(G-S\) contains no \(K_{1,D}\) as a subgraph. Therefore
\[
\Delta(G-S)\le D-1.
\]

Since \(\operatorname{tw}(G-S)<t\), the tree-partition lemma gives a forest \(F\) and an \(F\)-partition
\[
\{B_x:x\in V(F)\}
\]
of \(G-S\), of width at most \(p(t-1,D-1)\).

Construct \(H\) from \(F\) by adding one vertex \(a\) adjacent to every vertex of \(F\). Use the additional bag
\[
B_a:=S.
\]
Every edge internal to \(G-S\) is respected by the \(F\)-partition, while every edge with an endpoint in \(S\) is represented by an edge incident with \(a\). Thus this is an \(H\)-partition of \(G\) of width at most
\[
c_X(t):=
\max\bigl\{1,(q-1)(D+1),p(t-1,D-1)\bigr\}.
\]

Finally, \(H\) is a cone over a forest, so
\[
\operatorname{tw}(H)\le \operatorname{tw}(F)+1\le2.
\]
This proves the upper bound.

---

## 3. Optimality of the bound at treedepth \(2\)

Let
\[
X_0:=2K_{1,4}.
\]
Then \(\operatorname{td}(X_0)=2\).

For \(n\ge4\), let \(G_n\) be the fan
\[
G_n=K_1\vee P_n.
\]
Write \(a\) for its apex and \(v_1,\dots,v_n\) for the path in order. The only vertex of degree at least \(4\) in \(G_n\) is \(a\). In every subdivision of \(K_{1,4}\), the image of the centre has degree at least \(4\) in the host graph. Hence \(G_n\) cannot contain two vertex-disjoint subdivisions of \(K_{1,4}\). Thus \(G_n\) is \(X_0\)-topological-minor-free.

Also,
\[
\operatorname{tw}(G_n)=2<3.
\]

Suppose, for contradiction, that for some fixed \(c\) every \(G_n\) embedded in \(H_n\boxtimes K_c\) with \(\operatorname{tw}(H_n)\le1\). Thus \(H_n\) is a forest. Let
\[
\pi:V(G_n)\to V(H_n)
\]
be projection onto the first coordinate, and put \(x=\pi(a)\).

Since \(av_i\in E(G_n)\), every \(\pi(v_i)\) belongs to the closed neighbourhood \(N_{H_n}[x]\). Distinct neighbours of \(x\) are nonadjacent because \(H_n\) is a forest. Hence, in the sequence
\[
\pi(v_1),\ldots,\pi(v_n),
\]
any maximal interval avoiding \(x\) is constant: consecutive path vertices cannot project to two distinct neighbours of \(x\).

At most \(c-1\) path vertices project to \(x\), since the same fibre already contains \(a\). If \(r\le c-1\) path vertices project to \(x\), there are at most \(r+1\) intervals avoiding \(x\), and each contains at most \(c\) vertices. Therefore
\[
n\le r+c(r+1)\le(c-1)+c^2=c^2+c-1.
\]
This is impossible for arbitrarily large \(n\).

Consequently, no uniform representation over graphs of treewidth at most \(1\) exists. Thus the optimal uniform quotient-treewidth for all excluded graphs of treedepth \(2\) is exactly
\[
2.
\]

---

## 4. All subcubic excluded graphs

Let \(F_{\mathrm{minor}}\) denote the universal function supplied by the excluded-minor version of the theorem described in the question.

### Proposition 2

If \(\Delta(X)\le3\), then the conjectured conclusion holds for \(X\), with quotient-treewidth at most
\[
F_{\mathrm{minor}}(\operatorname{td}(X)).
\]

### Proof

For a subcubic graph \(X\), the following standard equivalence holds:
\[
X\preccurlyeq_{\mathrm m}G
\quad\Longleftrightarrow\quad
X\preccurlyeq_{\mathrm{top}}G.
\]
Only the forward implication needs justification.

Take an \(X\)-minor model \(\{B_v:v\in V(X)\}\). For each edge \(uv\in E(X)\), choose one edge between \(B_u\) and \(B_v\). For a fixed \(v\), there are at most three selected attachment vertices in the connected graph \(G[B_v]\), counted with repetitions.

For at most three terminals in a connected graph, there is a vertex \(b_v\) and paths from \(b_v\) to the terminals whose only common vertex is \(b_v\). For three distinct terminals, take a minimal connecting tree: it is either a path, in which case the middle terminal can be used as \(b_v\), or a subdivided claw, whose branch vertex can be used. Repeated terminals are handled by choosing the repeated terminal as \(b_v\).

Combining these paths with the selected inter-branch-set edges produces a subdivision of \(X\). Different branch sets are disjoint, and within each branch set the paths meet only at the corresponding branch vertex \(b_v\).

Therefore, if \(G\) excludes \(X\) as a topological minor, it also excludes \(X\) as a minor. The excluded-minor theorem from the source paper then gives the required product representation with quotient-treewidth bounded by
\[
F_{\mathrm{minor}}(\operatorname{td}(X)).
\]

This covers disconnected subcubic \(X\) as well.

---

## 5. A non-subcubic family of treedepth \(3\)

There is a useful general criterion.

### Lemma 3

Let \(X\) be connected. Suppose there are integers \(D,r\) such that every connected \(X\)-topological-minor-free graph has at most \(r\) vertices of degree at least \(D\). Then the desired conclusion holds for \(X\) with
\[
\operatorname{tw}(H)\le2.
\]

### Proof

In each component \(C\) of \(G\), put
\[
S_C:=\{v\in V(C):\deg_C(v)\ge D\}.
\]
Then \(|S_C|\le r\). The graph \(C-S_C\) has maximum degree at most \(D-1\), so it has a bounded-width forest partition by the tree-partition lemma. Add one quotient vertex \(a_C\), place all of \(S_C\) in its bag, and make \(a_C\) adjacent to every forest bag belonging to \(C-S_C\). The resulting quotient is a disjoint union of cones over forests and therefore has treewidth at most \(2\). Its partition width is at most
\[
\max\{r,p(t-1,D-1)\}.
\]

### Application to double-stars

Let \(D_{a,b}\) be the tree consisting of adjacent vertices \(u,v\), with \(a\) additional leaves at \(u\) and \(b\) additional leaves at \(v\).

If a connected graph \(C\) contains two vertices \(x,y\) of degree at least
\[
a+b+1,
\]
take a shortest \(x\)-\(y\) path \(P\). Each of \(x,y\) has at least \(a+b\) neighbours outside \(P\). Choose \(a\) neighbours of \(x\), and then \(b\) neighbours of \(y\) disjoint from those already chosen. Together with \(P\), these edges form a subdivision of \(D_{a,b}\).

Thus a \(D_{a,b}\)-topological-minor-free connected graph has at most one vertex of degree at least \(a+b+1\). Lemma 3 gives
\[
\operatorname{tw}(H)\le2.
\]

When \(a,b\ge1\), one has \(\operatorname{td}(D_{a,b})=3\). In particular, \(D_{3,3}\) is non-subcubic and has treedepth \(3\). The fan graphs used above exclude \(D_{3,3}\), since they have only one vertex of degree at least \(4\), and they rule out quotient-treewidth \(1\). Hence the optimal quotient-treewidth for excluding \(D_{3,3}\) is exactly \(2\).

---

## 6. Why this does not settle the general problem

The simple route of replacing topological-minor exclusion by exclusion of another ordinary minor cannot work once \(\Delta(X)\ge4\). Indeed, for every finite graph \(Y\), replace each high-degree vertex of \(Y\) by a subcubic tree with one leaf for every incident edge. The resulting subcubic graph \(Q_Y\) contains \(Y\) as a minor. On the other hand, \(Q_Y\) cannot contain any graph \(X\) with \(\Delta(X)\ge4\) as a topological minor. Thus there is no graph \(Y\) satisfying
\[
Y\preccurlyeq_{\mathrm m}G
\ \Longrightarrow\
X\preccurlyeq_{\mathrm{top}}G
\]
for all \(G\).

The treedepth-\(2\) proof succeeds because star models can be taken with a bounded number of vertices, so a maximal disjoint packing gives a bounded exceptional set. For a general \(X\), a minimal topological model may contain arbitrarily long subdivided edges, and the union of even one model cannot be put into a bounded-width exceptional bag. Controlling the arrangement of several high-degree branch vertices, rather than merely their number, is the unresolved part.

Thus the full conjecture remains open, but the shallow case \(\operatorname{td}(X)\le2\) is completely resolved, including the optimal constant, and the subcubic and double-star cases follow as above.