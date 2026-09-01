```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured dichotomy holds for every fixed bounded-treewidth class, hence for forests, bounded-degree chordal graphs, and all graphs with maximum degree at most two, with explicit constants whose dependence on d is essentially necessary.",
  "would_publish": false,
  "caveats": "The argument does not cover bounded-degree graphs of unbounded treewidth, and no claim of novelty is made."
}
```

## 1. Statement and conventions

All graphs are finite. For vertex sets \(A,B\subseteq V(G)\), write
\[
\operatorname{dist}_G(A,B)=\min\{\operatorname{dist}_G(a,b):a\in A,\ b\in B\},
\]
with distance \(+\infty\) between different components. An \(X\)-\(Y\) separator means a vertex set meeting every \(X\)-\(Y\) path.

The general conjecture remains unresolved here. I prove it for bounded-treewidth graphs, with an explicit dependence on the treewidth, and obtain genuine instances of the original conjecture for forests, chordal graphs of bounded degree, and \(\Delta\le 2\).

Define
\[
\beta_\Delta(r)=\max\{|B_H(v,r)|:\Delta(H)\le \Delta,\ v\in V(H)\}.
\]
The standard degree bound gives
\[
\beta_\Delta(0)=1,
\]
and, for \(r\ge1\),
\[
\beta_\Delta(r)\le
\begin{cases}
1,&\Delta=0,\\
2,&\Delta=1,\\
1+\Delta\displaystyle\sum_{i=0}^{r-1}(\Delta-1)^i,&\Delta\ge2.
\end{cases}
\]

## 2. A packing-covering lemma for subtrees

### Lemma 2.1
Let \(\mathcal F\) be a finite family of nonempty subtrees of a tree \(T\). Then the minimum number of vertices of \(T\) meeting every member of \(\mathcal F\) equals the maximum number of pairwise vertex-disjoint members of \(\mathcal F\).

#### Proof

Root \(T\). For a subtree \(F\), let \(t(F)\) be its unique vertex closest to the root.

While some subtree remains, choose \(F\) for which \(t(F)\) has maximum depth, put \(t(F)\) into a hitting set \(Z\), and discard all subtrees containing \(t(F)\).

The subtrees chosen during this procedure are pairwise disjoint. Indeed, suppose \(F\) is selected with \(z=t(F)\), and \(F'\) survives that step. If \(F'\) met \(F\), then, since the top of \(F'\) is no deeper than \(z\), the unique path in \(T\) from \(t(F')\) to a point of \(F\) would pass through \(z\). As \(F'\) is a subtree, this would imply \(z\in F'\), contrary to its survival.

Thus the number of selected vertices is at most the maximum number of disjoint subtrees. Conversely, every hitting set has size at least that maximum. ∎

The same statement holds for a forest, component by component.

## 3. The bounded-treewidth case

### Theorem 3.1
Let \(d,k\ge1\), let \(G\) satisfy
\[
\Delta(G)\le\Delta,\qquad \operatorname{tw}(G)\le t,
\]
and let \(X,Y\subseteq V(G)\). Put
\[
s=s(d):=\max\left\{0,\left\lceil\frac{d-2}{2}\right\rceil\right\}.
\]
Then either

1. \(G\) contains \(k\) \(X\)-\(Y\) paths pairwise at distance at least \(d\), or
2. \(G\) has an \(X\)-\(Y\) separator of size less than
   \[
   (t+1)\beta_\Delta(s)\,k.
   \]

#### Proof

Fix a tree decomposition \((T,\{B_q:q\in V(T)\})\) of width \(t\). Thus
\[
|B_q|\le t+1.
\]

For a connected subgraph \(A\subseteq G\), define its support in the decomposition by
\[
\tau(A):=\{q\in V(T):B_q\cap V(A)\ne\varnothing\}.
\]
This is a subtree of \(T\): for every vertex \(v\), the bags containing \(v\) induce a subtree, and the corresponding subtrees for adjacent vertices intersect.

For every \(X\)-\(Y\) path \(P\), let
\[
A_P=N_G^s[V(P)].
\]
The set \(A_P\) is connected, so \(\tau(A_P)\) is a subtree of \(T\).

We first record the spacing consequence of disjoint supports. If
\[
\tau(A_P)\cap\tau(A_Q)=\varnothing,
\]
then \(A_P\) and \(A_Q\) neither intersect nor have an edge between them. Indeed, a common vertex would occur in a common bag, and an edge between the two sets would have both endpoints in a common bag. Hence
\[
\operatorname{dist}_G(A_P,A_Q)\ge2.
\]
It follows that
\[
\operatorname{dist}_G(P,Q)\ge 2s+2.
\]
To see this directly, if a shortest \(P\)-\(Q\) path had length at most \(2s\), then \(N_s(P)\) and \(N_s(Q)\) would intersect; if it had length \(2s+1\), those two neighborhoods would have an edge between them.

By the choice of \(s\),
\[
2s+2\ge d.
\]
Consequently, \(k\) pairwise disjoint subtrees among
\[
\{\tau(A_P):P\text{ is an }X\text{-}Y\text{ path}\}
\]
would yield \(k\) \(X\)-\(Y\) paths pairwise at distance at least \(d\).

Suppose outcome 1 does not hold. Lemma 2.1 gives a set
\[
Z\subseteq V(T),\qquad |Z|\le k-1,
\]
meeting every subtree \(\tau(A_P)\).

Define
\[
S:=\bigcup_{q\in Z}N_G^s[B_q].
\]
For every \(X\)-\(Y\) path \(P\), some \(q\in Z\) lies in \(\tau(A_P)\). Thus \(B_q\) contains a vertex at distance at most \(s\) from \(P\), and therefore \(S\) meets \(P\). Hence \(S\) separates \(X\) and \(Y\).

Finally,
\[
|N_G^s[B_q]|\le |B_q|\beta_\Delta(s)
 \le (t+1)\beta_\Delta(s),
\]
so
\[
|S|\le (k-1)(t+1)\beta_\Delta(s)
 < k(t+1)\beta_\Delta(s).
\]
This is outcome 2. ∎

### Consequences

1. **Maximum degree at most two.**  
   Every graph of maximum degree at most two has treewidth at most two. Thus the original conjecture holds for all \(d\) when \(\Delta\le2\). Since
   \[
   \beta_2(s)=1+2s,
   \]
   one may take, for example,
   \[
   C(d,2)=3d.
   \]

2. **Forests.**  
   Since forests have treewidth at most one, Theorem 3.1 gives
   \[
   C(d,\Delta)=2\beta_\Delta\!\left(
   \max\left\{0,\left\lceil\frac{d-2}{2}\right\rceil\right\}\right).
   \]

3. **Chordal graphs.**  
   A chordal graph has treewidth \(\omega(G)-1\), while
   \(\omega(G)\le\Delta(G)+1\). Hence the original conjecture holds for chordal graphs with
   \[
   C(d,\Delta)=(\Delta+1)\beta_\Delta(s(d)).
   \]

More generally, the conjecture holds on any class whose treewidth is bounded by a function of \(\Delta\).

## 4. A sharper result for forests

The parity loss in Theorem 3.1 can be reduced for forests.

### Proposition 4.1
Let \(F\) be a forest with \(\Delta(F)\le\Delta\). The conjectured conclusion holds with
\[
C_{\mathrm{forest}}(d,\Delta)=
\begin{cases}
\beta_\Delta\!\left(\dfrac{d-1}{2}\right),
   &d\text{ odd},\\[2mm]
2\beta_\Delta\!\left(\dfrac d2-1\right),
   &d\text{ even}.
\end{cases}
\]

#### Proof for odd \(d\)

Write \(d=2a+1\). For every \(X\)-\(Y\) path \(P\), let
\[
E_P=N_F^a[V(P)].
\]
Each \(E_P\) is a subtree of \(F\), and
\[
E_P\cap E_Q=\varnothing
\quad\Longleftrightarrow\quad
\operatorname{dist}_F(P,Q)\ge2a+1=d.
\]
Thus, if there are no \(k\) distance-\(d\) paths, Lemma 2.1 gives at most \(k-1\) vertices \(Z\) meeting every \(E_P\). Then \(N_F^a(Z)\) meets every \(X\)-\(Y\) path, and
\[
|N_F^a(Z)|\le(k-1)\beta_\Delta(a)
 <k\beta_\Delta(a).
\]

#### Proof for even \(d\)

Write \(d=2a\), and let \(F^\ast\) be obtained by subdividing every edge of \(F\) once. For a path \(P\subseteq F\), let \(P^\ast\) be its subdivision in \(F^\ast\). For two paths,
\[
\operatorname{dist}_{F^\ast}(P^\ast,Q^\ast)
   =2\operatorname{dist}_{F}(P,Q).
\]

Set
\[
E_P=N_{F^\ast}^{2a-1}[V(P^\ast)].
\]
Since distances between lifted paths are even,
\[
E_P\cap E_Q=\varnothing
\quad\Longleftrightarrow\quad
\operatorname{dist}_{F}(P,Q)\ge2a=d.
\]
Again obtain a transversal \(Z\subseteq V(F^\ast)\) of size at most \(k-1\).

For \(z\in Z\), define a set \(S_z\subseteq V(F)\) as follows:

- if \(z\in V(F)\), let \(S_z=B_F(z,a-1)\);
- if \(z\) subdivides an edge \(uv\), let
  \[
  S_z=B_F(u,a-1)\cup B_F(v,a-1).
  \]

If \(z\in E_P\), then \(S_z\) meets \(P\). For an original vertex \(z\), subdivision distances to \(P^\ast\) are twice the corresponding distances to \(P\). For a subdivision vertex on \(uv\), either \(uv\) belongs to \(P\), or
\[
\operatorname{dist}_{F^\ast}(z,P^\ast)
 =1+2\min\{\operatorname{dist}_F(u,P),
            \operatorname{dist}_F(v,P)\}.
\]
In either case the assertion follows from
\(\operatorname{dist}_{F^\ast}(z,P^\ast)\le2a-1\).

Therefore
\[
S=\bigcup_{z\in Z}S_z
\]
separates \(X\) and \(Y\), and
\[
|S|\le 2(k-1)\beta_\Delta(a-1)
 <2k\beta_\Delta(a-1).
\]
∎

## 5. Necessary dependence of the constant

The dependence of \(C(d,\Delta)\) on \(d\) cannot be polynomial for fixed \(\Delta\ge3\). This is already forced by trees and \(k=2\).

### Proposition 5.1
Let \(\Delta\ge3\).

- If \(d=2a+1\ge3\), every valid constant must satisfy
  \[
  C(d,\Delta)>
  \frac{\Delta(\Delta-1)^{a-1}}2.
  \]
- If \(d=2a\ge2\), every valid constant must satisfy
  \[
  C(d,\Delta)>(\Delta-1)^{a-1}.
  \]

#### Construction and proof

First suppose \(d=2a+1\). Let \(H\) be the rooted tree of depth \(a\) in which the root has \(\Delta\) children and every other non-leaf vertex has \(\Delta-1\) children. Its leaf set \(L\) has size
\[
n=\Delta(\Delta-1)^{a-1},
\]
and its diameter is \(2a=d-1\).

For each \(v\in L\), add two leaves \(x_v,y_v\) adjacent to \(v\). Let
\[
X=\{x_v:v\in L\},\qquad Y=\{y_v:v\in L\}.
\]
The resulting graph is a tree of maximum degree \(\Delta\).

The \(n\) paths
\[
x_v-v-y_v,\qquad v\in L,
\]
are pairwise vertex-disjoint, so every \(X\)-\(Y\) separator has size at least \(n\). On the other hand, every \(X\)-\(Y\) path contains the core vertex adjacent to its \(X\)-endpoint. Any two such core vertices are at distance at most
\[
\operatorname{diam}(H)=d-1.
\]
Thus no two \(X\)-\(Y\) paths are at distance at least \(d\).

Taking \(k=2\), the conjectured separator would have size less than \(2C(d,\Delta)\), forcing
\[
2C(d,\Delta)>n.
\]

For even \(d=2a\), use a tree with a central edge and grow a complete \((\Delta-1)\)-ary tree to depth \(a-1\) from each endpoint. There are
\[
n=2(\Delta-1)^{a-1}
\]
outer leaves, and the diameter is \(2a-1=d-1\). Adding the same pairs \(x_v,y_v\) gives the claimed bound.

For \(\Delta=2\), a path on \(d\) vertices with its vertices alternately assigned to \(X\) and \(Y\) has \(\lfloor d/2\rfloor\) vertex-disjoint \(X\)-\(Y\) edges, diameter \(d-1\), and no two distance-\(d\) \(X\)-\(Y\) paths. Hence
\[
C(d,2)>\frac12\left\lfloor\frac d2\right\rfloor.
\]
Thus linear dependence on \(d\) is necessary when \(\Delta=2\), while exponential dependence of order \((\Delta-1)^{d/2}\) is necessary for every fixed \(\Delta\ge3\).

## 6. Remaining gap

The proof of Theorem 3.1 turns each path into a subtree of a decomposition tree and then replaces each selected decomposition bag by its bounded-radius neighborhood. In a general bounded-degree graph, tree-decomposition bags can have arbitrarily large size: bounded-degree expanders already show that treewidth is not controlled by \(\Delta\). Consequently, the argument only gives a constant depending on \(\operatorname{tw}(G)\), which is not permitted in Conjecture 1.4.

Thus the unbounded-treewidth case for \(d\ge3\) remains open here. The lower-bound trees show that any complete proof must in any event tolerate constants exponential in \(d\); they do not provide a counterexample to linearity in \(k\).