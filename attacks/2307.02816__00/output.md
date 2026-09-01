```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general planar conjecture remains open, but the desired linear dependence is exact for the canonical trivially-perfect path-exclusion witnesses, and polynomial bounds follow when the excluded planar graph has polynomial-size core.",
  "would_publish": false,
  "caveats": "No polynomial bound is obtained for all planar X; in particular, the full class of P_m-minor-free graphs remains unresolved."
}
```

## 1. Statement and conventions

For a graph class \(\mathcal C\), let \(\operatorname{utw}(\mathcal C)\) be the least \(k\) for which there is a constant \(c\) such that every \(G\in\mathcal C\) is a subgraph of
\[
H\boxtimes K_c
\]
for some graph \(H\) with \(\operatorname{tw}(H)\le k\). Equivalently, \(G\) has an \(H\)-partition
\[
V(G)=\bigcup_{x\in V(H)}P_x,\qquad |P_x|\le c,
\]
such that every edge of \(G\) has both ends in one part or in parts indexed by adjacent vertices of \(H\).

For a planar graph \(X\), write
\[
\mathcal G_X=\{G:X\not\preccurlyeq G\}.
\]
The source proves, with \(h=\operatorname{td}(X)\),
\[
h-2\le \operatorname{utw}(\mathcal G_X)\le 2^{h+1}-4.
\]
The question is whether the upper bound can be replaced by a universal polynomial in \(h\).

I do not resolve this. I give one exact special case, two reductions covering genuine families of excluded planar graphs, and an obstruction to a natural induction.

### Planarity is essential

If the question is read without the implicit assumption that \(X\) is planar, it is false. Indeed, if \(X\) is nonplanar, then every planar graph is \(X\)-minor-free. On the other hand,
\[
G\subseteq H\boxtimes K_c,\quad \operatorname{tw}(H)\le k
\]
implies
\[
\operatorname{tw}(G)\le c(k+1)-1,
\]
by replacing every bag \(B\) of a tree-decomposition of \(H\) by \(B\times[c]\). Since planar grids have unbounded treewidth, \(\operatorname{utw}(\mathcal G_X)=\infty\) for nonplanar \(X\).

Thus everything below concerns the intended planar formulation.

---

## 2. Exact result for the canonical path-exclusion witnesses

Let \(\mathcal{TP}\) denote the class of trivially perfect graphs, equivalently graphs of the form \(\operatorname{cl}(T)\), where \(T\) is a rooted forest and two vertices are adjacent precisely when one is an ancestor of the other.

### Theorem 2.1

For every \(m\ge2\),
\[
\boxed{\;
\operatorname{utw}\bigl(\mathcal{TP}\cap\mathcal G_{P_m}\bigr)
   =\lfloor\log_2 m\rfloor-1
   =\operatorname{td}(P_m)-2.
\;}
\]

Thus the desired polynomial dependence is not only true but linear, and sharp, on the standard trivially-perfect family used to obtain the general lower bound.

### Preliminary observation

A graph has \(P_m\) as a minor if and only if it contains a path on at least \(m\) vertices. The reverse implication is immediate. For the forward implication, concatenate paths inside the consecutive branch sets of a \(P_m\)-model.

### Upper bound

Let \(G=\operatorname{cl}(T)\) have no \(P_m\)-minor. For a vertex \(v\in V(T)\), let \(T_v\) be its rooted descendant subtree and define
\[
\lambda(v):=\text{maximum order of a path in }\operatorname{cl}(T_v).
\]

If the children of \(v\) have \(\lambda\)-values
\[
\lambda_1\ge\lambda_2\ge\cdots,
\]
where \(\lambda_2=0\) when \(v\) has at most one child, then
\[
\lambda(v)=1+\lambda_1+\lambda_2. \tag{2.1}
\]
Indeed, a path avoiding \(v\) lies in one child subtree, while a path using \(v\) can meet at most two child subtrees, and \(v\) is adjacent to every vertex in each such subtree.

At every non-leaf \(v\), designate a child with maximum \(\lambda\)-value as heavy; all other child edges are light. The heavy edges partition \(T\) into vertex-disjoint directed paths. Contract each heavy path to one vertex, obtaining a rooted forest \(R\).

For every light child \(u\) of \(v\), (2.1) gives
\[
\lambda(v)\ge 1+2\lambda(u). \tag{2.2}
\]
Consequently, along a root-to-leaf path \(Q_1,\ldots,Q_s\) in \(R\), where \(q_i\) is the top vertex of the heavy path \(Q_i\),
\[
\lambda(q_i)\ge 1+2\lambda(q_{i+1}).
\]
Induction yields
\[
\lambda(q_1)\ge 2^s-1.
\]
Since \(G\) has no path on \(m\) vertices, \(\lambda(q_1)\le m-1\). Hence
\[
s\le \lfloor\log_2 m\rfloor. \tag{2.3}
\]

Now use the heavy paths as the parts of a partition of \(G\). Each heavy path has at most \(m-1\) vertices, because it is an ancestor chain and hence induces a clique, in particular a path, in \(G\). If two vertices in distinct heavy paths are adjacent in \(G\), their heavy paths are ancestor-related in \(R\). Therefore
\[
G\subseteq \operatorname{cl}(R)\boxtimes K_{m-1}.
\]
By (2.3), \(R\) has height at most \(\lfloor\log_2m\rfloor\), and the ancestor-path bags give
\[
\operatorname{tw}(\operatorname{cl}(R))
   \le \lfloor\log_2m\rfloor-1.
\]
This proves the upper bound.

### Lower bound

Put
\[
r=\lfloor\log_2m\rfloor.
\]
For \(N\ge2\), let \(T_{r,N}\) be the complete \(N\)-ary rooted tree of height \(r\), where height counts vertices, and let
\[
F_{r,N}:=\operatorname{cl}(T_{r,N}).
\]
By (2.1), the maximum path order in \(F_{r,N}\) is \(2^r-1<m\), so
\[
F_{r,N}\in\mathcal{TP}\cap\mathcal G_{P_m}.
\]

Suppose \(F_{r,N}\subseteq H\boxtimes K_c\). Map each vertex of \(F_{r,N}\) to its first coordinate in \(H\). Every fiber has size at most \(c\). If \(N>rc\), one can select a root-to-leaf chain
\[
v_1,\ldots,v_r
\]
whose vertices have pairwise distinct first coordinates: after choosing \(v_1,\ldots,v_i\), the union of their \(i\) fibers contains at most \(ic\) vertices and consequently meets at most \(ic\) child subtrees of \(v_i\); choose an untouched child subtree.

The selected vertices are pairwise adjacent in \(F_{r,N}\), being ancestor-related. Their distinct first coordinates therefore induce a \(K_r\) in \(H\). Hence
\[
\operatorname{tw}(H)\ge r-1.
\]
Since \(N\) can be chosen after \(c\), this proves the lower bound.

Finally,
\[
\operatorname{td}(P_m)=\lceil\log_2(m+1)\rceil
\]
and, for integral \(m\ge2\),
\[
\lfloor\log_2m\rfloor
   =\lceil\log_2(m+1)\rceil-1.
\]
The theorem follows.

---

## 3. What this says about the full path-exclusion case

Since
\[
\mathcal{TP}\cap\mathcal G_{P_m}\subseteq\mathcal G_{P_m},
\]
Theorem 2.1 gives
\[
\operatorname{utw}(\mathcal G_{P_m})
   \ge \lfloor\log_2m\rfloor-1. \tag{3.1}
\]

There is also the elementary upper bound
\[
\operatorname{utw}(\mathcal G_{P_m})\le m-2. \tag{3.2}
\]
Indeed, run depth-first search in each component of a \(P_m\)-minor-free graph. Every root-to-leaf path in the DFS forest has at most \(m-1\) vertices, and every non-tree edge joins ancestor-related vertices. Taking the ancestor path of each DFS vertex as a bag gives a tree-decomposition of width at most \(m-2\).

Writing \(h=\operatorname{td}(P_m)\), this yields
\[
h-2\le\operatorname{utw}(\mathcal G_{P_m})
   \le m-2\le 2^h-3. \tag{3.3}
\]
Thus even the connected excluded minor \(X=P_m\) already contains the essential unresolved gap: the conjecture would require replacing the upper bound \(m=2^{\Theta(h)}\) by \((\log m)^{O(1)}\).

---

## 4. A genuine polynomial regime for the full class \(\mathcal G_X\)

### Proposition 4.1

There are absolute constants \(C,D\) such that every planar \(n\)-vertex graph \(X\) satisfies
\[
\operatorname{utw}(\mathcal G_X)\le Cn^D. \tag{4.1}
\]

#### Proof

Two established quantitative facts suffice.

1. There are absolute \(A,a\) such that every graph of treewidth at least \(Ar^a\) contains the \(r\times r\) grid as a minor. Polylogarithmic factors in a particular formulation can be absorbed by increasing \(a\).

2. Every planar \(n\)-vertex graph is a minor of an \(r\times r\) grid for some \(r=n^{O(1)}\). This follows, for example, from a polynomial-area planar grid drawing after replacing high-degree vertices by contractible planar gadgets.

Choose such an \(r\) for \(X\). If
\[
\operatorname{tw}(G)\ge Ar^a,
\]
then \(G\) contains the \(r\times r\) grid and therefore contains \(X\). Hence every \(X\)-minor-free graph has treewidth \(n^{O(1)}\). Taking \(H=G\) and \(c=1\) proves (4.1). \(\square\)

Consequently, for every fixed \(s\), the desired conclusion holds for the family of planar graphs satisfying
\[
|V(X)|\le \operatorname{td}(X)^s:
\qquad
\operatorname{utw}(\mathcal G_X)
   \le C\,\operatorname{td}(X)^{sD}. \tag{4.2}
\]

This includes grid-like excluded minors and other families whose order is polynomial in their treedepth. It does not address paths, heavily subdivided graphs, or graphs with very large repeated branches.

---

## 5. Repeated connected components cost at most one unit of underlying treewidth

The following transfer lemma separates component multiplicity—which treedepth does not see—from the difficult connected case.

### Lemma 5.1: bounded-deletion transfer

Suppose every graph \(G\in\mathcal C\) has a set \(A\), with \(|A|\le a\), such that \(G-A\in\mathcal D\). Then
\[
\operatorname{utw}(\mathcal C)
   \le \operatorname{utw}(\mathcal D)+1. \tag{5.1}
\]

#### Proof

Let \(G-A\subseteq H\boxtimes K_c\) with \(\operatorname{tw}(H)\le k\). Add a new universal vertex \(z\) to \(H\), obtaining \(H^+\). Map all vertices of \(A\) into the fiber over \(z\), using a clique factor of size at least \(a\). All edges incident with \(A\) are then present in \(H^+\boxtimes K_{\max\{a,c\}}\), and
\[
\operatorname{tw}(H^+)\le k+1
\]
by adding \(z\) to every bag of a tree-decomposition of \(H\). \(\square\)

### Corollary 5.2

Let \(Y\) be a connected planar graph and let \(rY\) be the disjoint union of \(r\) copies of \(Y\). Then
\[
\boxed{\;
\operatorname{utw}(\mathcal G_Y)
 \le \operatorname{utw}(\mathcal G_{rY})
 \le \operatorname{utw}(\mathcal G_Y)+1.
\;} \tag{5.2}
\]

#### Proof

The first inequality follows from
\[
\mathcal G_Y\subseteq\mathcal G_{rY}.
\]

For the second, if \(G\) has no \(rY\)-minor, then it has no \(r\) vertex-disjoint \(Y\)-minor models. The vertex Erdős–Pósa theorem for models of a fixed planar graph gives a set \(A\), of size bounded in terms of \(Y,r\), meeting every \(Y\)-minor model. Thus \(G-A\in\mathcal G_Y\), and Lemma 5.1 applies. \(\square\)

Since
\[
\operatorname{td}(rY)=\operatorname{td}(Y),
\]
arbitrarily large repetition does not fundamentally worsen the problem. Combining Corollary 5.2 with Proposition 4.1 gives, for example, a polynomial bound for every \(X=rY\) where
\[
|V(Y)|\le \operatorname{td}(Y)^s,
\]
independently of \(r\), even though \(|V(X)|\) can be arbitrarily large relative to \(\operatorname{td}(X)\).

---

## 6. Failure of a natural separator induction

A tempting approach to \(P_m\)-exclusion is to seek a bounded set \(S\) whose deletion reduces the longest-path bound by a fixed factor and then recurse. This is false.

Let \(\ell=2s\), set \(m=\ell+4\), and construct \(A_{\ell,N}\) from \(N\) disjoint copies of \(P_\ell\) by adding one vertex \(z\) adjacent to a central vertex of each copy. A path avoiding \(z\) has at most \(\ell\) vertices. A path using \(z\) meets at most two arms and has at most
\[
s+1+1+s
\]
edges, hence at most \(\ell+3=m-1\) vertices. Thus \(A_{\ell,N}\) is \(P_m\)-minor-free.

However, for every set \(S\) of at most \(b\) vertices, choosing \(N>b\) leaves some entire \(P_\ell\)-arm disjoint from \(S\). Hence some component of \(A_{\ell,N}-S\) still contains \(P_\ell=P_{m-4}\). For any fixed \(\alpha<1\), taking \(\ell\) sufficiently large gives \(\ell>\alpha m\). Thus no bounded global deletion set can uniformly reduce the path threshold by a fixed factor.

This example is itself a tree and has underlying treewidth \(1\), so it does not contradict the conjecture. It shows that a successful recursion must handle many local separators in parallel; a single bounded “central cluster” induction cannot work.

---

## 7. Conclusion and remaining gap

The results above establish:

- the intended statement must be restricted to planar \(X\);
- the lower-bound witnesses based on complete branching closures admit an exact matching upper bound:
  \[
  \operatorname{utw}(\mathcal{TP}\cap\mathcal G_{P_m})
    =\operatorname{td}(P_m)-2;
  \]
- the conjecture holds for excluded planar graphs whose order is polynomial in their treedepth;
- arbitrary repetition of a connected excluded planar component costs at most \(1\) in underlying treewidth.

They do not yield a polynomial bound for all planar \(X\). In particular, no argument above improves
\[
\operatorname{utw}(\mathcal G_{P_m})\le m-2
\]
to a polylogarithmic function of \(m\), which is already necessary to settle the original question.