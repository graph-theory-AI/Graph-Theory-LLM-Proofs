```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general question remains open, but radius-1 merge-width k forces hereditary 2(k-1)-near-twins, yielding explicit χ-bounds for induced-K_{2,t}-free graphs and a complete answer for k=1.",
  "would_publish": false,
  "caveats": "The argument uses the source convention that the centre's own part is counted in radius-1 width; under an open-ball normalization replace 2(k-1) by 2k."
}
```

# 1. Statement of the partial results

For distinct vertices \(u,v\) of a graph \(H\), put
\[
\Delta_H(u,v)
 =\bigl(N_H(u)\triangle N_H(v)\bigr)\setminus\{u,v\}.
\]
Thus \(\Delta_H(u,v)\) is the set of vertices which distinguish \(u\) from \(v\).

The following consequences of bounded radius-1 merge-width are proved below.

### Theorem A: hereditary near-twins

If \(\operatorname{mw}_1(G)\le k\), then every induced subgraph \(H\subseteq G\) with at least two vertices contains distinct \(u,v\) satisfying
\[
|\Delta_H(u,v)|\le 2(k-1).
\tag{1}
\]

Consequently,
\[
\operatorname{mw}_1(G)\ge
1+\left\lceil \frac12
 \max_{\substack{H\subseteq_i G\\ |H|\ge2}}
 \min_{u\ne v\in V(H)}|\Delta_H(u,v)|
\right\rceil.
\tag{2}
\]

### Theorem B: an induced-biclique-free special case

Suppose every induced subgraph of \(G\) with at least two vertices has a pair \(u,v\) with
\[
|\Delta_H(u,v)|\le d.
\tag{3}
\]
If \(G\) has no induced \(K_{2,t}\), then, writing \(s=\omega(G)\),
\[
\chi(G)\le
\prod_{r=2}^{s}\bigl(d+R(t,r)\bigr),
\tag{4}
\]
where \(R(t,r)\) is the Ramsey number for an independent set of size \(t\) or a clique of size \(r\).

Combining this with Theorem A gives
\[
\boxed{\quad
\chi(G)\le
\prod_{r=2}^{\omega(G)}
\bigl(2k-2+R(t,r)\bigr)
\quad}
\tag{5}
\]
for every induced-\(K_{2,t}\)-free graph with \(\operatorname{mw}_1(G)\le k\).

In particular, if \(G\) is triangle-free and has no \(K_{2,t}\), then
\[
\chi(G)\le 2k+t-2.
\tag{6}
\]

### Theorem C: the case \(k=1\)

Under the usual closed-ball normalization,
\[
\operatorname{mw}_1(G)=1
\quad\Longleftrightarrow\quad
G\text{ is a cograph}.
\tag{7}
\]
Hence graphs of radius-1 merge-width one satisfy
\[
\chi(G)=\omega(G).
\tag{8}
\]

I also give a modular-decomposition reduction showing that it is enough to settle the conjecture on prime graphs.

# 2. Near-twins forced by the first merge

I use only the following immediate feature of the definition of a merge sequence. At a stage whose current partition is \(\mathcal P\), adjacency is constant between two current parts except on pairs recorded in the resolver/error relation \(R\). The radius-1 width at that stage is
\[
\max_{x\in V(G)}
\bigl|\{P\in\mathcal P:P\cap N_R[x]\ne\varnothing\}\bigr|.
\]

Radius-1 merge-width is hereditary: restrict every current part and every resolver relation to an induced vertex set and delete ineffective merge steps.

Let \(H\) be an induced subgraph of \(G\). Consider the first effective merge in a width-\(k\) sequence for \(H\), merging singleton parts \(\{u\}\) and \(\{v\}\). Immediately after this merge all other vertices still form singleton parts.

If \(x\in\Delta_H(u,v)\), then \(ux\) and \(vx\) have different adjacency values. Therefore at least one of the pairs \(ux,vx\) must occur in the resolver relation at this stage; otherwise adjacency would not be constant between the new part \(\{u,v\}\) and \(\{x\}\).

The closed \(R\)-neighborhood of \(u\) already meets its own current part \(\{u,v\}\), so it can meet at most \(k-1\) other current parts. Since all these other parts are singletons, at most \(k-1\) distinguishing vertices can be charged to \(u\). The same holds for \(v\). Hence
\[
|\Delta_H(u,v)|\le 2(k-1),
\]
proving Theorem A.

This argument is insensitive to whether the resolver records exceptional edges, exceptional nonedges, or both: a disagreement between the two adjacency values must be charged to at least one of its two pairs.

# 3. Coloring graphs with hereditary near-twins

We now prove Theorem B.

Let \(G\) satisfy (3), contain no induced \(K_{2,t}\), and have clique number at most \(s\). Repeatedly choose a near-twin pair in the current induced graph. This gives an ordering
\[
v_1,v_2,\dots,v_n
\]
and, for every \(i<n\), a parent \(p_i=v_j\) with \(j>i\), such that
\[
S_i:=\Delta_{G[\{v_i,\dots,v_n\}]}(v_i,p_i)
\]
has size at most \(d\).

Call \(i\) a **false step** if \(v_ip_i\notin E(G)\), and a **true step** if \(v_ip_i\in E(G)\).

## 3.1. False steps have bounded forward degree

Suppose \(i\) is a false step and let
\[
C_i=N(v_i)\cap N(p_i)\cap\{v_{i+1},\dots,v_n\}.
\]

Because \(v_i,p_i\) are nonadjacent, an independent \(t\)-set in \(C_i\), together with \(v_i,p_i\), would induce a \(K_{2,t}\). Thus
\[
\alpha(G[C_i])<t.
\]
Moreover, a clique of size \(s\) in \(C_i\), together with \(v_i\), would be a clique of size \(s+1\). Hence
\[
\omega(G[C_i])<s.
\]
By the definition of \(R(t,s)\),
\[
|C_i|\le R(t,s)-1.
\]

Every forward neighbor of \(v_i\) either lies in \(C_i\) or belongs to the one-sided difference between the neighborhoods of \(v_i\) and \(p_i\). Therefore
\[
|N(v_i)\cap\{v_{i+1},\dots,v_n\}|
   \le d+R(t,s)-1.
\tag{9}
\]

## 3.2. An auxiliary sparse graph

Construct an auxiliary graph \(J\) on \(V(G)\) as follows.

* At a false step \(i\), join \(v_i\) in \(J\) to every forward \(G\)-neighbor of \(v_i\).
* At a true step \(i\), join \(v_i\) in \(J\) to \(p_i\), and also to every vertex of \(S_i\). These latter pairs are added to \(J\) whether or not they are edges of \(G\).

By (9), a false-step vertex has at most
\[
d+R(t,s)-1
\]
forward neighbors in \(J\). A true-step vertex has at most \(d+1\) forward neighbors in \(J\). Since \(R(t,s)\ge2\), the ordering above witnesses that \(J\) is
\[
\bigl(d+R(t,s)-1\bigr)\text{-degenerate}.
\]
Thus \(J\) has a proper coloring with
\[
L_s:=d+R(t,s)
\tag{10}
\]
colors.

## 3.3. Each auxiliary color class has smaller clique number

Let \(X\) be one color class of this proper coloring of \(J\). I claim
\[
\omega(G[X])\le s-1.
\tag{11}
\]

Suppose instead that \(K\subseteq X\) is an \(s\)-clique, and let \(v_i\) be the earliest vertex of \(K\).

The step \(i\) cannot be false: every forward \(G\)-neighbor of \(v_i\), in particular every other vertex of \(K\), was joined to \(v_i\) in \(J\).

Thus \(i\) is a true step. Since \(v_ip_i\in E(J)\), the parent \(p_i\) is not in \(K\). For every \(y\in K\setminus\{v_i\}\), the fact that \(v_i,y\) have the same \(J\)-color implies \(y\notin S_i\). Therefore
\[
p_iy\in E(G)\quad\Longleftrightarrow\quad v_iy\in E(G).
\]
The right side holds because \(K\) is a clique. Also \(v_ip_i\in E(G)\). Hence
\[
K\cup\{p_i\}
\]
is an \((s+1)\)-clique, a contradiction. This proves (11).

## 3.4. Induction on the clique number

Let \(F_{d,t}(1)=1\), and for \(s\ge2\) let
\[
F_{d,t}(s)=\bigl(d+R(t,s)\bigr)F_{d,t}(s-1).
\]
Every \(G[X]\) again satisfies the hereditary near-twin condition and excludes induced \(K_{2,t}\), while (11) gives \(\omega(G[X])\le s-1\). By induction,
\[
\chi(G[X])\le F_{d,t}(s-1).
\]
There are at most \(L_s=d+R(t,s)\) auxiliary color classes, so
\[
\chi(G)\le
\bigl(d+R(t,s)\bigr)F_{d,t}(s-1)
=
\prod_{r=2}^{s}\bigl(d+R(t,r)\bigr).
\]
This proves Theorem B.

For a triangle-free graph, \(s=2\) and \(R(t,2)=t\), giving
\[
\chi(G)\le d+t.
\]
Substituting \(d=2(k-1)\) proves (6).

# 4. A simpler ordinary-biclique bound

If \(G\) has no \(K_{2,t}\) even as a non-induced subgraph, then every two vertices have at most \(t-1\) common neighbors. For a near-twin pair \(u,v\),
\[
\deg(u)\le (t-1)+d+\mathbf 1_{uv\in E(G)}
\le d+t.
\]
Every induced subgraph has such a pair, so \(G\) is \((d+t)\)-degenerate. Consequently,
\[
\chi(G)\le d+t+1.
\]
For \(\operatorname{mw}_1(G)\le k\), this gives
\[
\chi(G)\le 2k+t-1.
\tag{12}
\]

The induced-\(K_{2,t}\)-free result is different: it allows arbitrarily large cliques and many large non-induced bicliques.

# 5. Exact treatment of width one

Suppose \(\operatorname{mw}_1(G)\le1\). Theorem A implies that every induced subgraph with at least two vertices contains \(u,v\) with
\[
\Delta_H(u,v)=\varnothing.
\]
Thus \(u,v\) are true or false twins in \(H\).

The four-vertex path \(P_4\) has no pair of twins. Hence \(G\) has no induced \(P_4\), and therefore \(G\) is a cograph.

Conversely, a cograph is built recursively from single vertices by disjoint union and complete join. Merge the two child modules at each node of a cotree. Their vertices have identical adjacency to every current part outside the node, so no resolver pair ever needs to connect two distinct current parts. All resolver pairs already internal to a current part remain internal after later merges. Hence every radius-1 ball meets only its own current part, and the width is one.

Finally, induction over the cotree gives
\[
\chi(G_1\mathbin{\dot\cup}G_2)
 =\max\{\chi(G_1),\chi(G_2)\},
\qquad
\chi(G_1\vee G_2)=\chi(G_1)+\chi(G_2),
\]
with identical formulas for the clique number. Thus \(\chi(G)=\omega(G)\).

# 6. Reduction to prime graphs

A module of \(G\) is a vertex set \(M\) such that every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is prime if it has no nontrivial module.

The open problem is equivalent to its restriction to prime graphs, quantitatively as follows.

### Proposition

Fix \(k,s\), and suppose every prime graph \(Q\) satisfying
\[
\operatorname{mw}_1(Q)\le k,\qquad \omega(Q)\le s
\]
has \(\chi(Q)\le q\), where \(q\ge2\). Then every graph \(G\) satisfying the same two inequalities obeys
\[
\chi(G)\le q^{\omega(G)-1}.
\tag{13}
\]

### Proof

Use the modular decomposition of \(G\). At an internal node, \(G\) is obtained by substituting child graphs \(G_i\) into a quotient \(Q\), where \(Q\) is complete, edgeless, or prime.

Each quotient \(Q\) is an induced subgraph of \(G\): choose one representative from each child module. Hence \(\operatorname{mw}_1(Q)\le k\).

Proceed by induction over the modular decomposition.

* If \(Q\) is edgeless, then
  \[
  \chi(G)=\max_i\chi(G_i).
  \]

* If \(Q\) is complete, then
  \[
  \chi(G)=\sum_i\chi(G_i),
  \qquad
  \omega(G)=\sum_i\omega(G_i).
  \]
  For positive integers \(a_i\) and \(q\ge2\),
  \[
  \sum_i q^{a_i-1}\le q^{\sum_i a_i-1}.
  \]

* If \(Q\) is prime, color \(Q\) with at most \(q\) colors. Modules whose quotient vertices receive the same color are pairwise anticomplete and may share a palette. Thus
  \[
  \chi(G)\le q\max_i\chi(G_i).
  \]
  A nontrivial prime quotient has no isolated vertex. If \(G_i\) maximizes the right side and \(a=\omega(G_i)\), a neighboring quotient module gives
  \[
  \omega(G)\ge a+1.
  \]
  Hence
  \[
  q\chi(G_i)\le q\cdot q^{a-1}=q^a
  \le q^{\omega(G)-1}.
  \]

This proves (13).

As a consequence, Theorem B also proves χ-boundedness for graphs whose prime modular quotients exclude some fixed induced \(K_{2,t}\), even when the original graphs themselves contain arbitrarily large bicliques generated by substitution or join operations.

# 7. The shift-graph test case

A natural prospective counterexample remains the shift graph
\[
S_n:\quad
V(S_n)=\{(i,j):1\le i<j\le n\},
\]
where
\[
(i,j)\sim(j,\ell)
\qquad (i<j<\ell).
\]

It has the three properties required of a counterexample family:

1. \(S_n\) is triangle-free.
2. It contains arbitrarily large bicliques: for a fixed middle coordinate \(m\),
   \[
   \{(i,m):i<m\}
   \quad\text{is complete to}\quad
   \{(m,j):m<j\}.
   \]
3. Its chromatic number is
   \[
   \chi(S_n)=\lceil\log_2 n\rceil.
   \]

For completeness, if \(S_n\) has a proper \(q\)-coloring, let \(A_j\subseteq[q]\) be the set of colors appearing on arcs \((i,j)\) entering \(j\). The color of \((i,j)\) lies in \(A_j\setminus A_i\), so \(A_j\nsubseteq A_i\) whenever \(i<j\). Hence the \(A_i\) are distinct and \(n\le2^q\).

Conversely, order \(n\) distinct subsets \(A_1,\dots,A_n\subseteq[q]\) by nondecreasing cardinality, where \(2^q\ge n\), and color \((i,j)\) by any element of \(A_j\setminus A_i\). Consecutive arcs receive different colors.

Thus a uniform bound on \(\operatorname{mw}_1(S_n)\) would disprove the conjecture. I do not have such a merge sequence, nor a proof that \(\operatorname{mw}_1(S_n)\) is unbounded.

# 8. Remaining gap

The auxiliary-coloring proof identifies the unresolved obstruction precisely. For a nonadjacent near-twin pair \(u,v\), almost all neighbors of \(u\) may also be neighbors of \(v\). If this common neighborhood is unbounded, one cannot add all forward edges of \(u\) to the sparse auxiliary graph. Long chains of such “false” near-twin merges are exactly where large bicliques can occur.

Radius-2 control prevents a neighboring part from concealing arbitrarily many further interactions; radius-1 control alone does not provide such a bound. The argument above handles the case where those common neighborhoods cannot contain large independent sets, but it does not control the arbitrary-biclique case. Therefore it does not resolve the original question.