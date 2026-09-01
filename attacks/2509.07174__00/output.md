```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full surface conjecture remains open, but it holds for forests with the optimal uniform radius ceil(c/2) and, more generally, for every class of uniformly bounded tree-breadth.",
  "would_publish": false,
  "caveats": "Finite graphs and the source convention distance > c are assumed; the argument does not control arbitrary surface graphs."
}
```

# Partial results on coarse Menger for surfaces

## 1. Conventions and reformulation

All graphs are finite. For vertex sets \(A,B\subseteq V(G)\), write
\[
d(A,B)=\min\{d_G(a,b):a\in A,\ b\in B\},
\qquad
N_r(A)=\{v:d_G(v,A)\le r\}.
\]
The source abstract defines \(c\)-distant paths to mean paths at distance **more than** \(c\).

For a family \(\mathcal A\) of connected vertex sets, define
\[
\nu_c(\mathcal A)
 =\max\{|\mathcal B|:\mathcal B\subseteq\mathcal A,\ 
 d(A,A')>c\text{ for distinct }A,A'\in\mathcal B\},
\]
and
\[
\tau_r(\mathcal A)
 =\min\{|X|:X\subseteq V(G),\ d(X,A)\le r
 \text{ for every }A\in\mathcal A\}.
\]

For the family \(\mathcal P(S,T)\) of all \(S\)-\(T\) paths, the conjecture asks for an \(\ell=\ell(\mathcal S,k,c)\) such that
\[
\nu_c(\mathcal P(S,T))\le k
\quad\Longrightarrow\quad
\tau_\ell(\mathcal P(S,T))\le k.
\]

Two elementary cases hold for all graphs:

- If \(k=0\), either there is an \(S\)-\(T\) path or the empty set satisfies the second alternative.
- If \(c=0\), paths at distance more than zero are vertex-disjoint, so ordinary Menger gives \(\ell=0\).

The results below concern \(c>0\).

---

## 2. The packing–transversal lemma for subtrees

### Lemma 2.1
Let \(D\) be a finite forest and let \(\mathcal F\) be a family of nonempty subtrees of \(D\). Then
\[
\min\{|Z|:Z\subseteq V(D),\ Z\cap F\ne\varnothing
\text{ for every }F\in\mathcal F\}
=
\max\{|\mathcal F'|:\mathcal F'\subseteq\mathcal F
\text{ is pairwise vertex-disjoint}\}.
\]

### Proof
It suffices to consider one component of \(D\), rooted arbitrarily.

For a subtree \(F\), let \(h(F)\) be its unique vertex closest to the root. Choose \(F\in\mathcal F\) for which \(h(F)\) has maximum depth. Put \(h(F)\) into a transversal, put \(F\) into a packing, and delete all members of \(\mathcal F\) containing \(h(F)\).

We claim that \(F\) is disjoint from every undeleted subtree \(F'\). Suppose instead that \(x\in F\cap F'\). Since \(h(F)\) is the highest vertex of \(F\), the vertex \(x\) is a descendant of \(h(F)\). Let \(h'=h(F')\). By maximality of the depth of \(h(F)\),
\[
\operatorname{depth}(h')\le \operatorname{depth}(h(F)).
\]
Thus \(h'\) is not a strict descendant of \(h(F)\). The unique \(h'\)-\(x\) path consequently contains \(h(F)\). Since \(F'\) is connected, \(h(F)\in F'\), contrary to \(F'\) being undeleted.

Iterating, the chosen subtrees are pairwise disjoint, while the chosen vertices hit every member of \(\mathcal F\). The packing and transversal produced have equal size. Since every transversal must use distinct vertices for pairwise disjoint subtrees, this size is optimal. ∎

---

## 3. The conjecture for forests

### Theorem 3.1
Let \(G\) be a forest and let \(\mathcal A\) be any family of connected subgraphs of \(G\). Put
\[
r=\left\lceil\frac c2\right\rceil.
\]
Then
\[
\tau_r(\mathcal A)\le \nu_c(\mathcal A).
\]

In particular, for every \(k,c\ge0\), every forest \(G\), and every \(S,T\subseteq V(G)\), either there are \(k+1\) pairwise \(c\)-distant \(S\)-\(T\) paths, or there is a set \(X\) of at most \(k\) vertices such that every \(S\)-\(T\) path comes within distance
\[
\left\lceil\frac c2\right\rceil
\]
of \(X\).

### Proof
For each \(A\in\mathcal A\), let
\[
A^+=N_r(A).
\]
Since \(G\) is a forest and \(A\) is connected, \(A^+\) is a subtree of the relevant component of \(G\).

If \(A^+\) and \(B^+\) are disjoint, then
\[
d(A,B)>2r.
\]
Indeed, if a shortest \(A\)-\(B\) path had length at most \(2r\), it would contain a vertex at distance at most \(r\) from both \(A\) and \(B\). Since \(2r\ge c\), disjointness therefore implies
\[
d(A,B)>c.
\]

Consequently, every pairwise disjoint subfamily of \(\{A^+:A\in\mathcal A\}\) corresponds to a pairwise \(c\)-distant subfamily of \(\mathcal A\). Its size is at most \(\nu_c(\mathcal A)\).

Apply Lemma 2.1 to the family of subtrees \(A^+\). There is a set \(X\) of at most \(\nu_c(\mathcal A)\) vertices meeting every \(A^+\). Equivalently, \(d(X,A)\le r\) for every \(A\in\mathcal A\). ∎

This proof applies to all connected-subgraph families, not only to path families.

---

## 4. Sharpness of the forest bound

The radius in Theorem 3.1 is best possible, even for planar trees and for every \(k\ge1\).

### Proposition 4.1
For every \(k\ge1\) and \(c\ge1\), there is a tree \(G\) and disjoint sets \(S,T\subseteq V(G)\) such that

1. there are no \(k+1\) pairwise \(c\)-distant \(S\)-\(T\) paths; but
2. no set of at most \(k\) vertices coarsely meets every \(S\)-\(T\) path at any radius smaller than
   \[
   \left\lceil\frac c2\right\rceil.
   \]

### Construction and proof
Let \(n=k+1\). Start with a subdivided star with centre \(o\) and branch endpoints
\[
z_1,\ldots,z_n.
\]
Choose branch lengths
\[
d(o,z_1)=\left\lfloor\frac c2\right\rfloor,\qquad
d(o,z_2)=\left\lceil\frac c2\right\rceil,
\]
and, for \(i\ge3\),
\[
d(o,z_i)=c+1.
\]
If the first branch has length zero, identify \(z_1\) with \(o\).

Attach a new leaf \(u_i\) to each \(z_i\), and put
\[
S=\{z_1,\ldots,z_n\},\qquad
T=\{u_1,\ldots,u_n\}.
\]
Let \(L_i=z_iu_i\) denote the local \(S\)-\(T\) path.

The distances between the local paths satisfy
\[
d(L_1,L_2)=c,
\]
while every other pair of local paths is at distance more than \(c\). Hence the local paths contain a \(c\)-distant family of size \(n-1=k\), but not of size \(n\).

Every nonlocal \(S\)-\(T\) path has endpoints \(z_i,u_j\) with \(i\ne j\). It contains the centre \(o\), so two nonlocal paths intersect. Moreover, the \(z_i\)-\(u_j\) path intersects both \(L_i\) and \(L_j\). Thus a pairwise \(c\)-distant family containing a nonlocal path contains at most \(n-2\) local paths and hence has size at most \(n-1=k\). Therefore no \(k+1\) pairwise \(c\)-distant paths exist.

Now put
\[
r=\left\lceil\frac c2\right\rceil,\qquad q=r-1.
\]
For all distinct \(i,j\),
\[
d(L_i,L_j)>2q.
\]
Indeed, \(d(L_1,L_2)=c>2q\), and all other distances exceed \(c\). A radius-\(q\) ball can therefore meet at most one of the \(n=k+1\) local paths. Hence \(k\) such balls cannot meet every \(S\)-\(T\) path.

Since graph distances are integral, the same argument excludes every real radius \(\ell<r\). Combined with Theorem 3.1, this proves optimality. ∎

Because every tree embeds on every surface, this also gives the universal lower bound
\[
\ell(\mathcal S,k,c)\ge \left\lceil\frac c2\right\rceil
\]
for any prospective surface theorem, when \(k,c\ge1\).

---

## 5. A tree-decomposition extension

The subtree argument extends to graphs whose tree-decomposition bags can themselves be covered by a bounded number of bounded-radius balls.

### Theorem 5.1
Let \(G\) have a tree decomposition
\[
(D,\{B_t:t\in V(D)\}).
\]
Suppose that for every \(t\in V(D)\) there is a set \(C_t\subseteq V(G)\) such that
\[
|C_t|\le p
\quad\text{and}\quad
B_t\subseteq N_\rho(C_t).
\]
Then, for every family \(\mathcal A\) of connected subgraphs of \(G\),
\[
\tau_{\lceil c/2\rceil+\rho}(\mathcal A)
\le p\,\nu_c(\mathcal A).
\]

### Proof
Again put \(r=\lceil c/2\rceil\), and for each \(A\in\mathcal A\) define
\[
H_A=N_r(A).
\]
The subgraph \(H_A\) is connected.

Define its trace in the decomposition tree by
\[
Q_A=\{t\in V(D):B_t\cap H_A\ne\varnothing\}.
\]
This trace is a subtree of \(D\). To see this, for each \(v\in H_A\), the nodes whose bags contain \(v\) form a subtree \(D_v\). Whenever \(uv\) is an edge of \(H_A\), some bag contains both \(u\) and \(v\), so \(D_u\cap D_v\ne\varnothing\). As \(H_A\) is connected,
\[
Q_A=\bigcup_{v\in H_A}D_v
\]
is connected.

If \(Q_A\) and \(Q_{A'}\) are disjoint, then \(H_A\) and \(H_{A'}\) are vertex-disjoint: a common vertex would belong to some bag lying in both traces. As in Theorem 3.1, disjointness of \(H_A,H_{A'}\) implies
\[
d(A,A')>2r\ge c.
\]
Therefore a pairwise disjoint collection of traces \(Q_A\) has size at most \(\nu_c(\mathcal A)\).

By Lemma 2.1, there is a set \(Z\subseteq V(D)\), with
\[
|Z|\le \nu_c(\mathcal A),
\]
meeting every trace \(Q_A\). Let
\[
X=\bigcup_{t\in Z} C_t.
\]
Then \(|X|\le p\,\nu_c(\mathcal A)\).

For any \(A\in\mathcal A\), choose \(t\in Z\cap Q_A\) and
\[
y\in B_t\cap H_A.
\]
There is \(x\in C_t\) with \(d(x,y)\le\rho\), while \(d(y,A)\le r\). Hence
\[
d(x,A)\le r+\rho.
\]
Thus \(X\) has the asserted property. ∎

### Corollary 5.2: bounded tree-breadth
Suppose \(G\) has a tree decomposition such that every bag \(B_t\) lies in a ball \(N_\rho(x_t)\). Then
\[
\tau_{\lceil c/2\rceil+\rho}(\mathcal A)
\le \nu_c(\mathcal A).
\]
Consequently, the strong coarse Menger conclusion with exactly \(k\) centres holds on every class of uniformly bounded tree-breadth.

In particular, if \(G\) is embeddable on a fixed surface and has tree-breadth at most \(\rho\), one can take
\[
\ell=\left\lceil\frac c2\right\rceil+\rho.
\]

### Corollary 5.3: bounded tree-length and chordal graphs
If \(G\) has a tree decomposition in which every bag has weak \(G\)-diameter at most \(\lambda\), choose an arbitrary vertex of each bag as its centre. Then
\[
\tau_{\lceil c/2\rceil+\lambda}(\mathcal A)
\le \nu_c(\mathcal A).
\]

Every chordal graph has a clique-tree decomposition. Each clique lies in a radius-one ball centred at any of its vertices. Therefore chordal graphs satisfy the strong coarse Menger conclusion with
\[
\ell=\left\lceil\frac c2\right\rceil+1.
\]

### Corollary 5.4: a bounded-treewidth weak form
If \(G\) has treewidth at most \(w\), take \(C_t=B_t\), \(p=w+1\), and \(\rho=0\). Then
\[
\tau_{\lceil c/2\rceil}(\mathcal A)
\le (w+1)\nu_c(\mathcal A).
\]
Hence, if there are no \(k+1\) pairwise \(c\)-distant \(S\)-\(T\) paths, there is a set \(X\) with
\[
|X|\le (w+1)k
\]
such that every \(S\)-\(T\) path comes within distance \(\lceil c/2\rceil\) of \(X\).

This does not have the conjectured coefficient \(1\), but the number of centres is linear in \(k\) and independent of \(c\).

---

## 6. Why this does not prove the surface conjecture

The trace argument works for any tree decomposition and produces at most \(k\) decomposition bags meeting the traces of all expanded paths. The unresolved step is converting each selected bag into one bounded-radius graph ball.

- Bounded tree-breadth permits this conversion and gives exactly \(k\) centres.
- Bounded treewidth only bounds the number of vertices in a bag, yielding up to \((w+1)k\) centres.
- A surface embedding alone supplies neither uniformly bounded tree-breadth nor uniformly bounded treewidth.

Thus the surface-specific difficulty is precisely to replace a metrically large selected region by one coarse centre, or else extract an additional distant path using the embedding. No such argument is supplied here.

The source paper’s outer-face-terminal theorem, as quoted in the prompt, handles a different substantial planar case. The reported later weak surface theorem is not used or independently verified here.

## 7. Conclusion

The full conjecture is neither proved nor disproved. The self-contained progress is:

1. the strong conjecture holds for forests with the optimal radius
   \[
   \ell=\left\lceil\frac c2\right\rceil;
   \]
2. the same exact-\(k\) conclusion holds for every uniformly bounded-tree-breadth class, with
   \[
   \ell=\left\lceil\frac c2\right\rceil+\rho;
   \]
3. bounded-treewidth graphs admit the weak bound \((w+1)k\) on the number of centres.

The principal gap is that arbitrary graphs on a fixed surface need not satisfy the metric decomposition hypothesis used above.