```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Excluding one apex–incidence clique exactly characterizes tied domination for bounded-treewidth cores with bounded-degree peripheral vertices, and such classes can require exponentially growing tying functions.",
  "would_publish": false,
  "caveats": "The general bounded-degeneracy case remains unresolved; novelty relative to the full source paper has not been checked."
}
```

## 1. Scope and partial characterization

All graphs are finite and simple. Distances between different components are infinite. A set is **2-independent** if its vertices have pairwise distance greater than \(2\).

For \(t\ge 3\), let \(L_t\) have vertices
\[
\{a\}\cup\{x_1,\ldots,x_t\}
 \cup\{z_{ij}:1\le i<j\le t\},
\]
and edges
\[
az_{ij},\qquad x_i z_{ij},\qquad x_j z_{ij}.
\]
Thus \(L_t\) is the apex–incidence lift of \(K_t\) from the previous attempt.

I prove the proposed characterization for a larger setting than the lift classes considered there.

### Partial characterization theorem

Fix integers \(r\ge 3\) and \(w\ge 0\). Let \(\mathcal C\) be a monotone class such that every \(G\in\mathcal C\) admits a partition
\[
V(G)=X\mathbin{\dot\cup}Y
\]
satisfying
\[
\operatorname{tw}(G[X])\le w,
\qquad
\deg_G(y)\le r\quad(y\in Y).
\tag{1}
\]

Then the following are equivalent:

1. Domination is tied to 2-independence on \(\mathcal C\).
2. For some \(t\ge 3\), no graph in \(\mathcal C\) contains \(L_t\) as a subgraph.

For fixed \(r,w,t\), the positive direction admits a bound
\[
\gamma(G)\le \exp\!\bigl(O_{r,w,t}(k\log(k+1))\bigr),
\qquad k=\alpha_2(G).
\tag{2}
\]

These are sparse classes: every graph satisfying (1) is \(\max(r,w)\)-degenerate. Indeed, a subgraph containing a vertex of \(Y\) has a vertex of degree at most \(r\); a subgraph contained in \(X\) has a vertex of degree at most \(w\).

Condition (1) permits arbitrary edges inside \(Y\), subject to the degree bound. It includes bounded-treewidth classes, bounded-degree classes, and all bipartite graphs having bounded degree on one side.

I also give an explicit monotone, \(L_3\)-free, \(3\)-degenerate class satisfying this theorem for which **no polynomial tying function exists**.

The obstruction calculation and tree-decomposition argument suggested in the previous attempt are reproved below. General sufficiency of excluding \(L_t\) is not assumed.

---

## 2. The necessary obstruction

For every \(t\ge 3\),
\[
\alpha_2(L_t)=2,
\qquad
\gamma(L_t)\ge \left\lceil\frac t2\right\rceil.
\tag{3}
\]

To verify the first equality, both parts of the bipartition
\[
\{a,x_1,\ldots,x_t\},
\qquad
\{z_{ij}:i<j\}
\]
consist of vertices pairwise at distance at most \(2\). Thus a 2-independent set has at most two vertices. The pair \(x_1,z_{23}\) has distance \(3\), establishing equality.

For the domination bound, consider just the \(t\) vertices \(x_i\). A selected incidence vertex dominates two of them, a selected \(x_i\) dominates only itself among them, and \(a\) dominates none. Hence at least \(\lceil t/2\rceil\) selected vertices are necessary.

Consequently, if a monotone class satisfies
\[
\gamma(G)\le h(\alpha_2(G)),
\]
choose \(t\ge 3\) with \(\lceil t/2\rceil>h(2)\). Then \(L_t\) does not belong to the class. Monotonicity implies that no member contains \(L_t\) as a subgraph.

This proves necessity, without any sparsity assumption.

---

## 3. Two lemmas for sufficiency

### 3.1. Relative domination in bounded treewidth

For \(A\subseteq V(H)\), let
\[
\nu_H(A)=
\max\{|S|:S\subseteq A,\ S\text{ is 2-independent in }H\}.
\]

**Lemma 1.** If \(\operatorname{tw}(H)\le w\), then there is a set \(D\subseteq V(H)\) dominating \(A\) such that
\[
|D|\le (w+1)\nu_H(A).
\tag{4}
\]

**Proof.**
The empty case is immediate. Fix a width-\(w\) tree decomposition
\[
(T,\{B_t:t\in V(T)\}).
\]
For each graph vertex \(x\), its bag support
\[
T_x=\{t:x\in B_t\}
\]
is a nonempty subtree of \(T\).

For \(v\in A\), put
\[
S_v=\bigcup_{x\in N_H[v]}T_x.
\]
This is a subtree: for every neighbor \(x\) of \(v\), some bag contains both \(x\) and \(v\), so \(T_x\) intersects \(T_v\).

For a finite family of subtrees of a tree, the minimum size of a vertex transversal equals the maximum size of a pairwise disjoint subfamily. Here is the relevant greedy proof. Root the tree and choose a subtree whose vertex closest to the root is as deep as possible. Select that vertex and delete all subtrees containing it. Any subtree intersecting the chosen subtree contains the selected vertex: their highest vertices are comparable along the path to an intersection point, and the maximal-depth choice forces the required containment. Thus the retained, chosen subtrees are pairwise disjoint, while the selected vertices hit the entire family.

If \(S_u,S_v\) are disjoint, then
\[
N_H[u]\cap N_H[v]=\varnothing,
\]
since a common graph vertex would have its bag support in both subtrees. Therefore \(u,v\) have distance greater than \(2\) in \(H\).

It follows that at most \(\nu_H(A)\) tree vertices suffice to meet every \(S_v\). The union of their bags dominates \(A\): a bag meeting \(S_v\) contains a vertex of \(N_H[v]\). Its size is at most \((w+1)\nu_H(A)\). ∎

### 3.2. Cleaning repeated witnesses

We will use ordinary multicolor Ramsey numbers, denoted by
\[
R(s_0,\ldots,s_q).
\]

The following elementary observation handles the possibility that one common neighbor witnesses several pairs.

**Lemma 2.** Suppose the edges of \(K_M\) are labelled so that each label occurs on at most \(b\) edges. If
\[
M\ge b t^3,
\]
then some \(K_t\) has all its edge labels distinct. If \(b=1\), \(M=t\) suffices.

**Proof.**
The assertion for \(b=1\) is immediate. Otherwise choose a uniformly random \(t\)-subset of the vertices.

The number of unordered pairs of distinct edges with the same label is at most
\[
\frac{b-1}{2}\binom M2.
\]
Such a pair uses either three or four vertices, so the probability that all its endpoints are selected is at most \((t/M)^3\). Thus the expected number of repeated-label pairs in the selected \(K_t\) is less than
\[
\frac{(b-1)t^3}{4M}<1.
\]
Some choice has none. ∎

Set
\[
M=M(r,t)=
\begin{cases}
t,&r=3,\\[2mm]
\displaystyle\binom{r-1}{2}t^3,&r\ge4.
\end{cases}
\tag{5}
\]

**Lemma 3.** Suppose:

- \(V(G)=X\dot\cup Y\);
- every \(y\in Y\) has degree at most \(r\);
- \(D\subseteq V(G)\) dominates \(Y\);
- \(G\) is \(L_t\)-subgraph-free and \(\alpha_2(G)\le k\).

If
\[
S\subseteq X\setminus N_G[D]
\]
is 2-independent in \(G[X]\), then, for every integer \(q\ge |D|\) with \(q\ge1\),
\[
|S|<
R\bigl(k+1,\underbrace{M,\ldots,M}_{q\text{ copies}}\bigr).
\tag{6}
\]

**Proof.**
Color the pairs of \(S\) as follows.

- A pair at distance greater than \(2\) in \(G\) receives color \(0\).
- Otherwise, its endpoints have a common neighbor \(y\in Y\): a path of length at most \(2\) contained in \(G[X]\) is excluded by the choice of \(S\).

For a pair of the second type, choose one such witness \(y\). Since the endpoints lie outside \(N_G[D]\), we have \(y\notin D\). As \(D\) dominates \(Y\), choose
\[
a\in D\cap N_G(y)
\]
and color the pair by \(a\). Pad with unused colors if \(|D|<q\).

There is no color-\(0\) clique of order \(k+1\), since it would be 2-independent in \(G\).

Suppose there is a monochromatic clique \(S_0\) of order \(M\), of color \(a\in D\). Label each edge by its chosen witness \(y\). Such a witness is adjacent to \(a\) and to the endpoints of every edge bearing its label. Since \(a\notin S_0\) and \(\deg(y)\le r\), its label occurs at most
\[
b=\binom{r-1}{2}
\]
times.

Lemma 2, with (5), gives \(t\) branch vertices whose pairs have distinct witnesses. Together with \(a\), these vertices and witnesses contain \(L_t\) as a subgraph. All vertices are distinct: the branches lie in \(X\setminus N[D]\), the witnesses lie in \(Y\setminus D\), and \(a\in D\).

Both Ramsey alternatives are impossible, proving (6). ∎

---

## 4. Proof of the sufficient direction

Fix a graph \(G\) satisfying (1), assume that it contains no \(L_t\), and put
\[
k=\alpha_2(G).
\]
The empty graph is harmless, so assume \(k\ge1\).

Choose an inclusion-maximal 2-independent set \(P\subseteq Y\), with distances measured in \(G\), and let
\[
D=\bigcup_{p\in P}N_G[p].
\]
Then
\[
|D|\le(r+1)|P|\le(r+1)k.
\tag{7}
\]

Moreover, \(D\) dominates \(Y\). Indeed, by maximality every \(y\in Y\) has distance at most \(2\) from some \(p\in P\), and \(N_G[p]\) dominates every vertex at distance at most \(2\) from \(p\).

Write
\[
H=G[X],
\qquad
U=X\setminus N_G[D],
\qquad
q=(r+1)k,
\]
and set
\[
B=
R\bigl(k+1,\underbrace{M,\ldots,M}_{q\text{ copies}}\bigr).
\]

By Lemma 3,
\[
\nu_H(U)\le B-1.
\]
Lemma 1 supplies a set \(E\subseteq X\) dominating \(U\) in \(H\), with
\[
|E|\le(w+1)(B-1).
\]

Now \(D\cup E\) dominates \(G\): \(D\) dominates \(Y\) and \(X\setminus U\), while \(E\) dominates \(U\). Hence an explicit tying function is
\[
\boxed{
h(k)=
(r+1)k+
(w+1)\left[
R\bigl(k+1,\underbrace{M(r,t),\ldots,M(r,t)}_{(r+1)k\text{ copies}}\bigr)-1
\right].
}
\tag{8}
\]
Set \(h(0)=0\).

For completeness, the growth claim (2) follows from an elementary multicolor Ramsey bound. With
\[
N=k+q(M-1)=\bigl(1+(r+1)(M-1)\bigr)k,
\]
the standard Ramsey recursion gives
\[
R(k+1,M,\ldots,M)
\le
\frac{N!}{k!\,((M-1)!)^q}
\le N!.
\]
Thus (8) is at most \(\exp(O_{r,w,t}(k\log(k+1)))\).

This completes the partial characterization theorem.

---

## 5. An explicit class requiring exponential tying functions

The preceding result is not merely a route to polynomial bounds. The following construction gives exponential lower bounds even when \(r=3\), \(w=0\), and \(L_3\) is excluded.

### Construction

For \(m\ge4\), let
\[
X_m=\{0,1\}^m,
\qquad
A_m=\{a_1,\ldots,a_m\}.
\]
For distinct bit strings \(x,y\), define
\[
c(x,y)=\min\{i:x_i\ne y_i\}.
\]

Construct the bipartite graph \(G_m\) with parts
\[
X_m\cup A_m,
\qquad
Z_m=\{z_{xy}:\{x,y\}\in\binom{X_m}{2}\},
\]
where
\[
N(z_{xy})=\{x,y,a_{c(x,y)}\}.
\tag{9}
\]

Every vertex of \(Z_m\) has degree \(3\), and \(X_m\cup A_m\) is independent.

### 5.1. Domination is exponential

Every selected vertex dominates at most two vertices of \(X_m\):

- a vertex of \(Z_m\) dominates its two endpoints;
- a vertex of \(X_m\) dominates only itself within \(X_m\);
- a hub \(a_i\) dominates none of \(X_m\).

Therefore
\[
\boxed{\gamma(G_m)\ge 2^{m-1}.}
\tag{10}
\]

### 5.2. The 2-independence number is exactly \(m+1\)

Every two vertices of \(X_m\) have a common incidence neighbor. Thus a 2-independent set contains at most one vertex of \(X_m\).

For each \(i\), at most one incidence vertex of color \(i\) can be selected, because all such vertices have common neighbor \(a_i\). Also \(a_i\) cannot be selected together with an incidence vertex of color \(i\).

Finally, every \(x\in X_m\) has distance \(2\) from every \(a_i\), by taking \(y\) obtained from \(x\) by flipping bit \(i\). Consequently:

- without a selected vertex of \(X_m\), the set has size at most \(m\);
- with one selected vertex of \(X_m\), it has no hubs and at most \(m\) incidence vertices.

Hence
\[
\alpha_2(G_m)\le m+1.
\tag{11}
\]

For equality, fix \(x^0\in X_m\). For each \(i\), the pairs obtained by flipping only bit \(i\) form a perfect matching of \(X_m\), all of color \(i\), of size \(2^{m-1}\).

Greedily choose one edge from each of these \(m\) matchings, avoiding \(x^0\) and all previously used endpoints. At every step at most \(2m-1\) vertices are forbidden, and
\[
2^{m-1}>2m-1\qquad(m\ge4),
\]
so a choice is available. The corresponding \(m\) incidence vertices have disjoint endpoint pairs and distinct hubs. They, together with \(x^0\), form a 2-independent set.

Thus
\[
\boxed{\alpha_2(G_m)=m+1.}
\tag{12}
\]

### 5.3. No \(G_m\) contains \(L_3\)

Because \(L_3\) is connected and bipartite, an embedding into \(G_m\) preserves the bipartition up to swapping. Consider the location of its apex.

**Case 1: the apex maps into \(X_m\cup A_m\).**

Its three incidence witnesses map into \(Z_m\). By (9), each has exactly three neighbors. The three required pairs of branch vertices therefore form a triangle in the link graph at the apex.

- At \(a_i\), this link graph consists of pairs \(xy\) with \(c(x,y)=i\). Every such pair crosses the \(i\)-th-bit bipartition, so this link graph is bipartite.
- At \(x\in X_m\), each link edge joins a bit string \(y\) to a hub \(a_{c(x,y)}\), again giving a bipartite graph.

Neither link graph contains a triangle.

**Case 2: the apex maps to \(z_{xy}\in Z_m\).**

Its three incidence witnesses must map to the three neighbors
\[
x,\ y,\ a_{c(x,y)}.
\]
In \(L_3\), every pair of incidence witnesses has a common branch neighbor distinct from the apex. But \(x\) and \(y\) have exactly one common neighbor in \(G_m\), namely \(z_{xy}\). This is impossible.

Thus \(G_m\) is \(L_3\)-subgraph-free.

### 5.4. Taking the monotone closure

Let
\[
\mathcal E=
\{G:G\text{ is isomorphic to a subgraph of some }G_m,\ m\ge4\}.
\]
This is a monotone, \(L_3\)-free, \(3\)-degenerate class. It satisfies (1) with \(r=3,w=0\), so the partial characterization theorem proves that domination is tied to 2-independence on \(\mathcal E\).

Nevertheless, every tying function for \(\mathcal E\) must satisfy, by (10) and (12),
\[
\boxed{h(k)\ge 2^{k-2}\qquad(k\ge5).}
\tag{13}
\]

In particular, domination tied to 2-independence need not admit a polynomial bound, even in this restricted sparse monotone setting.

---

## 6. What remains unresolved

The theorem above does **not** cover arbitrary bounded-degeneracy classes. Its essential additional hypothesis is that, after separating off globally bounded-degree peripheral vertices, the remaining core has bounded treewidth.

The precise use of that hypothesis is Lemma 1: a bound on the relative packing number \(\nu_H(U)\) is converted into a bounded set dominating \(U\).

One cannot simply replace treewidth by degeneracy in that lemma. Let \(H\) be the once-subdivided \(K_n\), and let \(U\) be its original branch vertices. Then
\[
\nu_H(U)=1,
\]
because every two branch vertices have distance \(2\), but every set dominating \(U\) has size at least \(\lceil n/2\rceil\). This happens in a \(2\)-degenerate graph. It does not contradict a bound using \(\alpha_2(H)\), since the subdivision vertices themselves contain large 2-independent sets; rather, it identifies what the relative argument loses.

Thus I have not proved or disproved the general assertion
\[
\forall d,t,k\ \exists M(d,t,k):
\quad
\begin{cases}
G\text{ is }d\text{-degenerate},\\
G\text{ is }L_t\text{-subgraph-free},\\
\alpha_2(G)\le k
\end{cases}
\Longrightarrow
\gamma(G)\le M(d,t,k).
\]
Nor have I obtained an alternative characterization for all sparse monotone classes.

The rigorous progress is the exact characterization under (1), together with the explicit exponential lower-bound class. Novelty of these special-case results relative to the full cited source has not been checked.