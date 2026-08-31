```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A linear extension of an S_t-free poset gives its incomparability graph linear mim-width at most t-1, and bounded linear mim-width admits a polynomial-time minimal-dominating-set extension oracle, hence polynomial-delay enumeration.",
  "would_publish": false,
  "caveats": "This assumes S_t is the standard example poset; the argument is self-contained, but novelty and overlap with existing mim-width metatheorems were not externally checked."
}
```

# Statement

Let \(S_t\) denote the standard example on

\[
\{a_1,\dots ,a_t,b_1,\dots ,b_t\},
\]

where \(a_i<b_j\) exactly when \(i\neq j\). Thus each of
\(\{a_1,\dots ,a_t\}\) and \(\{b_1,\dots ,b_t\}\) is an antichain, while \(a_i\)
and \(b_i\) are incomparable.

I prove the following stronger form of the conjecture.

## Theorem

For every fixed \(t\), given an \(S_t\)-free poset \(P\), the minimal dominating sets of its incomparability graph \(G=\operatorname{Inc}(P)\) can be enumerated with delay \(n^{O(t)}\) and polynomial space.

The proof has three ingredients:

1. every linear extension of \(P\) is a linear mim-width layout of \(G\) of width at most \(t-1\);
2. on a graph supplied with a bounded linear mim-width layout, the existence of a minimal dominating set respecting prescribed inclusions and exclusions is decidable in polynomial time;
3. the usual binary flashlight search using this extension oracle has polynomial delay.

No unproved conjecture is used.

---

# 1. \(S_t\)-freeness gives bounded linear mim-width

For disjoint \(A,B\subseteq V(G)\), let

\[
\operatorname{mim}_G(A,B)
\]

be the maximum size of an induced matching in the bipartite graph consisting of the edges of \(G\) between \(A\) and \(B\). Edges internal to \(A\) or \(B\) are ignored.

Let

\[
v_1,\dots ,v_n
\]

be a linear extension of \(P\), and put

\[
A_k=\{v_1,\dots ,v_k\},\qquad B_k=V(P)\setminus A_k.
\]

## Lemma 1

For every \(k\),

\[
\operatorname{mim}_G(A_k,B_k)\le t-1.
\]

### Proof

Suppose that the bipartite graph \(G[A_k,B_k]\) has an induced matching

\[
a_1b_1,\dots ,a_mb_m,
\]

where every \(a_i\in A_k\) and every \(b_i\in B_k\).

Because \(a_ib_i\in E(G)\), the elements \(a_i,b_i\) are incomparable in \(P\). For \(i\neq j\), inducedness of the matching says that \(a_i b_j\notin E(G)\), so \(a_i\) and \(b_j\) are comparable in \(P\). Since every \(a_i\) precedes every \(b_j\) in the chosen linear extension, necessarily

\[
a_i<_P b_j\qquad(i\neq j).
\]

It remains to show that the \(a_i\)'s and the \(b_i\)'s are antichains.

If, for instance, \(a_i<_P a_j\), then \(a_j<_P b_i\) because \(i\neq j\), and hence

\[
a_i<_P a_j<_P b_i,
\]

contradicting \(a_i\parallel b_i\). Thus the \(a_i\)'s form an antichain.

Similarly, if \(b_i<_P b_j\), then \(a_j<_P b_i\), giving

\[
a_j<_P b_i<_P b_j,
\]

contradicting \(a_j\parallel b_j\). Thus the \(b_i\)'s form an antichain.

Consequently, the restriction of \(P\) to these \(2m\) elements is exactly \(S_m\). If \(m\ge t\), it contains \(S_t\), contrary to the hypothesis. Hence \(m\le t-1\). ∎

Thus the given linear extension has linear mim-width at most \(t-1\), and it is computable by a topological sort.

---

# 2. A bounded-mim-width local-labeling algorithm

I give the required dynamic program explicitly rather than invoking a metatheorem.

Fix constants \(q,d,w\). Suppose that a graph \(G\) is supplied with an ordering

\[
v_1,\dots ,v_n
\]

such that every prefix cut has induced-matching size at most \(w\).

Consider a labeling problem with labels \(1,\dots ,q\). Each vertex \(v\) has a set \(L(v)\) of allowed labels. Whether \(v\) accepts a labeling is determined by:

- its own label, and
- for every label \(j\), the truncated number
  \[
  \min\{d,\lvert N(v)\cap V_j\rvert\},
  \]
  where \(V_j\) is the set of vertices receiving label \(j\).

## Lemma 2

For fixed \(q,d,w\), feasibility of such a labeling can be decided in time

\[
n^{O(qdw)}
\]

and polynomial space.

The predicates may be vertex-dependent.

## Proof

Write

\[
A_i=\{v_1,\dots ,v_i\},\qquad B_i=V(G)\setminus A_i.
\]

For \(X\subseteq A_i\), define its \(d\)-signature toward \(B_i\) by

\[
\sigma_i(X)(b)=\min\{d,\lvert N(b)\cap X\rvert\}
\quad(b\in B_i).
\]

Define signatures from \(B_i\) toward \(A_i\) analogously.

### Signature bound

For any cut \((A,B)\) with \(\operatorname{mim}_G(A,B)\le w\), the number of different \(d\)-signatures of subsets of \(A\) toward \(B\) is at most

\[
K:=\sum_{r=0}^{dw}\binom nr=n^{O(dw)}.
\]

Indeed, given \(X\subseteq A\), repeatedly delete vertices while preserving its signature, obtaining an inclusion-minimal representative \(R\subseteq X\).

For each \(x\in R\), minimality gives a vertex \(b\in B\) such that deleting \(x\) changes the truncated count at \(b\). Necessarily

\[
1\le |N(b)\cap R|\le d.
\]

Thus the sets \(N(b)\cap R\) of size at most \(d\) cover \(R\). Choose an inclusion-minimal subcover

\[
N(b_1)\cap R,\dots ,N(b_s)\cap R.
\]

For each \(j\), minimality of the cover gives

\[
x_j\in N(b_j)\cap R
\]

which belongs to none of the other selected neighborhoods. Then

\[
x_1b_1,\dots ,x_sb_s
\]

is an induced matching across the cut. Hence \(s\le w\), and therefore

\[
|R|\le ds\le dw.
\]

Every signature consequently has a representative of size at most \(dw\), proving the claimed bound.

The same bound holds in the other direction across the cut.

### Suffix signatures

For each \(i\), let \(\mathcal U_i\) be the set of \(q\)-tuples of signatures toward \(A_i\) arising from allowable labelings of \(B_i\). There are at most \(K^q\) such tuples.

These sets can be computed from right to left. Initially \(\mathcal U_n\) consists of the all-zero tuple. When \(v_{i+1}\) is added to the suffix, try every allowed label for \(v_{i+1}\), add its contribution to the corresponding signature, truncate at \(d\), and deduplicate. This recurrence generates exactly \(\mathcal U_i\), without enumerating all suffix labelings.

### Main states

A state at cut \(i\) is a pair

\[
(s,u),
\]

where:

- \(s\) is the \(q\)-tuple of signatures toward \(B_i\) of an allowable labeling of \(A_i\);
- \(u\in\mathcal U_i\) is a possible tuple of signatures of the suffix toward \(A_i\).

The state is declared true if there is an allowable labeling of \(A_i\) with signature \(s\) under which every vertex of \(A_i\) satisfies its local predicate when the contribution from \(B_i\) is given by \(u\).

There are at most \(K^{2q}\) states.

At \(i=0\), the prefix is empty, so the unique zero prefix signature is compatible with every member of \(\mathcal U_0\).

To pass from \(i\) to \(i+1\), put \(v=v_{i+1}\). For every true state \((s,u)\), every allowed label \(\ell\) for \(v\), and every \(u'\in\mathcal U_{i+1}\):

1. add \(v\), with label \(\ell\), to the suffix represented by \(u'\), and compute its signature toward \(A_i\);
2. require that this signature equal \(u\);
3. calculate the truncated number of neighbors of \(v\) of each label:
   - its neighbors in \(A_i\) are read from the coordinate of \(s\) indexed by \(v\);
   - its neighbors in \(B_{i+1}\) are read from the coordinate of \(u'\) indexed by \(v\);
4. test the local predicate of \(v\);
5. if it holds, add \(v\) with label \(\ell\) to \(s\), delete the coordinate indexed by \(v\), and insert the resulting state \((s',u')\).

Old prefix vertices need not be retested: moving \(v\) from suffix to prefix does not change their total label-neighbor counts.

Conversely, every feasible labeling induces precisely such a sequence of transitions. Hence the final table is nonempty exactly when a feasible labeling exists.

There are \(n\) cuts, at most \(K^{2q}\) states, and at most \(qK^q\) transitions considered per state. The running time is therefore \(n^{O(qdw)}\), and all stored tables have polynomial size for fixed \(q,d,w\). ∎

---

# 3. Minimal dominating sets as a four-label local problem

For a dominating set \(D\), a vertex \(p\) is a private neighbor of \(d\in D\) if

\[
N[p]\cap D=\{d\}.
\]

The standard private-neighbor criterion says:

\[
D\text{ is a minimal dominating set}
\iff
D\text{ dominates and every }d\in D\text{ has a private neighbor}.
\]

Introduce a second set \(W\), intended to contain private-neighbor witnesses. Give each vertex a label

\[
(\delta,\omega)\in\{0,1\}^2,
\]

where

\[
\delta=1\iff v\in D,\qquad \omega=1\iff v\in W.
\]

Thus \(q=4\). Use truncation threshold \(d=2\).

For a vertex \(v\), let

\[
c_D(v)=\min\{2,\lvert N[v]\cap D\rvert\},
\qquad
c_W(v)=\min\{2,\lvert N[v]\cap W\rvert\}.
\]

Impose the following local conditions:

\[
\begin{aligned}
&c_D(v)\ge 1 &&\text{for every }v,\\
&\omega(v)=1\Longrightarrow c_D(v)=1,\\
&\delta(v)=1\Longrightarrow c_W(v)\ge 1.
\end{aligned}
\tag{1}
\]

These are local predicates of the type covered by Lemma 2; the contribution of \(v\) itself to its closed neighborhood is determined by its own label.

## Lemma 3

A set \(D\) is a minimal dominating set if and only if there is a set \(W\) such that the four-label assignment satisfies (1).

### Proof

If (1) holds, the first condition says that \(D\) dominates. For every \(d\in D\), the third condition gives some \(w\in N[d]\cap W\). Since \(w\in W\), the second condition says that \(w\) has exactly one member of \(D\) in its closed neighborhood. That member must be \(d\), so \(w\) is a private neighbor of \(d\). Hence \(D\) is minimal.

Conversely, if \(D\) is minimal, choose one private neighbor \(p_d\) for every \(d\in D\), and put

\[
W=\{p_d:d\in D\}.
\]

Every member of \(W\) has exactly one member of \(D\) in its closed neighborhood, and every member of \(D\) has an adjacent witness in \(W\). Thus (1) holds. ∎

Now let \(I,O\subseteq V(G)\) be disjoint sets of vertices required to be respectively inside and outside \(D\). Restrict the allowed labels by requiring:

\[
\delta(v)=1\quad(v\in I),\qquad
\delta(v)=0\quad(v\in O),
\]

while leaving \(\omega(v)\) unrestricted.

By Lemmas 2 and 3, on a graph of linear mim-width at most \(w\), one can decide in time \(n^{O(w)}\) whether there exists a minimal dominating set \(D\) with

\[
I\subseteq D\subseteq V(G)\setminus O.
\]

This is the required extension oracle.

For \(G=\operatorname{Inc}(P)\) with \(P\) \(S_t\)-free, Lemma 1 gives \(w\le t-1\). Therefore each extension query takes \(n^{O(t)}\) time.

---

# 4. Polynomial-delay enumeration

Use the same vertex order \(v_1,\dots ,v_n\). At a node of a binary search tree, the membership of an initial segment in \(D\) has been fixed.

Before descending into a child, call the extension oracle:

- one child forces the next vertex into \(D\);
- the other forces it outside \(D\);
- prune a child if the oracle answers no.

At a leaf, all membership decisions are fixed. The oracle answers yes exactly when that set is a minimal dominating set, and it is output once.

Between two consecutive output leaves, depth-first traversal visits \(O(n)\) nodes and hence makes \(O(n)\) oracle calls. Thus the delay is

\[
n^{O(t)}.
\]

The recursion stack and the dynamic-programming tables use polynomial space. This proves the conjecture, in fact with polynomial delay.

---

# 5. Input representation

If the poset \(P\) is supplied, a linear extension is obtained by topological sorting.

If only the incomparability graph \(G\) is supplied, one can compute a transitive orientation of \(\overline G\) in polynomial time and then take a topological ordering. The \(S_t\)-free property is independent of which transitive orientation is chosen:

- an occurrence of \(S_t\) corresponds in \(G\) to two \(t\)-cliques joined by exactly a perfect matching;
- in \(\overline G\), the corresponding induced graph is \(K_{t,t}\) minus a perfect matching;
- for \(t\ge3\), every transitive orientation of this connected bipartite graph orients all edges from one shore to the other, since a vertex with both an incoming and an outgoing edge would create a forbidden directed two-edge path between nonadjacent vertices;
- for \(t=2\), every orientation gives two disjoint two-element chains, which is \(S_2\).

Thus any transitive orientation of the complement remains \(S_t\)-free when the graph belongs to the promised class.

---

# Gaps and status

Under the standard-example meaning of \(S_t\), there is no remaining mathematical gap in the argument. The main new observation is Lemma 1, while Lemma 2 supplies a self-contained bounded-mim-width dynamic program rather than relying on an external enumeration theorem.

The exponent depends on fixed \(t\), as required; the argument does not claim a polynomial whose exponent is independent of \(t\).