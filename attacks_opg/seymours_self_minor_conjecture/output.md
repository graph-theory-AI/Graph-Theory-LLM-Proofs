```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A finite-terminal pumping argument establishes proper contraction self-minors for graphs with a one-ended, locally finite, thin component behind a finite separator.",
  "would_publish": false,
  "caveats": "Special case only; no novelty claim, and the catalog's literature-status assertions were not independently verified."
}
```

## 1. Scope and statement

The supplied catalogue reports uncountable counterexamples to the literal formulation. I do not reconstruct or independently verify those counterexamples here. Instead, I prove a sufficient condition covering a class of graphs **containing rays**, including locally finite graphs with an isolated thin end.

All graphs below are simple and undirected. Write \(J\preccurlyeq K\) when \(J\) has a minor model in \(K\): pairwise disjoint nonempty connected vertex sets
\[
(B_v:v\in V(J))
\]
such that every edge \(uv\in E(J)\) is witnessed by an edge between \(B_u\) and \(B_v\).

For properness, I establish the concrete assertion
\[
G\preccurlyeq G/e
\]
for an edge \(e\in E(G)\). Thus the self-minor uses an actual contraction, rather than just the identity model.

### Theorem: a thin tail behind a finite separator

Let \(A\subseteq V(G)\) be finite, and let \(H\) be a component of \(G-A\). Suppose that:

1. \(H\) is infinite and locally finite;
2. \(H\) has exactly one end;
3. for some finite \(k\geq 1\), \(H\) contains \(k\), but not \(k+1\), pairwise vertex-disjoint rays.

Then, for every finite \(F\subseteq V(G)\), there is an edge \(e\in E(H)\), with neither endpoint in \(F\), such that
\[
G\preccurlyeq G/e.
\]
Moreover, the model can have finite branch sets and can fix every vertex in
\[
\bigl(V(G)\setminus V(H)\bigr)\cup F
\]
as a singleton branch set.

In particular:

> **Every locally finite graph with an isolated end of finite vertex-degree has a proper self-minor.**

Here an end is **thin** if the maximum number of pairwise vertex-disjoint rays belonging to it is finite. It is **isolated** if some finite vertex deletion leaves a component containing that end and no other end.

The proof uses the established finite Graph Minor Theorem, not any conjectural well-quasi-ordering of infinite graphs.

## 2. The finite comparison tools

### Finite rooted, labelled minors

I use the standard finite-label form of the Robertson–Seymour theorem:

> For a fixed finite poset \(Q\) and fixed integer \(t\), finite \(Q\)-labelled graphs with \(t\) ordered, distinct distinguished vertices are well-quasi-ordered by rooted, label-respecting minors.

The required minor models have these properties:

- the branch set of the \(i\)-th distinguished source vertex contains the \(i\)-th distinguished target vertex;
- for each source vertex \(v\), its branch set contains a target vertex \(w\) with
  \[
  \lambda(v)\leq_Q\lambda(w).
  \]

The rooted version follows from the finite-label version by adding distinct root markers to the labels.

We also need the following elementary strengthening of the usual “there is a comparable pair” formulation.

### Lemma 1: eventual upward recurrence

If \((x_n)_{n\geq 0}\) is a sequence in a well-quasi-order, then there are \(N\) and a strictly increasing function
\[
f:\{N,N+1,\ldots\}\longrightarrow\mathbb N
\]
such that, for every \(n\geq N\),
\[
f(n)>n
\qquad\text{and}\qquad
x_n\leq x_{f(n)}.
\]

#### Proof

Call \(n\) exceptional if
\[
\{m>n:x_n\leq x_m\}
\]
is finite.

There are only finitely many exceptional indices. Otherwise, recursively choose exceptional indices
\[
n_0<n_1<\cdots
\]
so that \(n_j\) lies beyond every index dominating any previously selected term. This gives
\[
x_{n_i}\not\leq x_{n_j}\qquad(i<j),
\]
contrary to well-quasi-ordering.

Choose \(N\) beyond all exceptional indices. For each \(n\geq N\), infinitely many later terms dominate \(x_n\). We may therefore choose \(f(n)\) recursively, larger than \(n\) and all previously chosen values. \(\square\)

The point is that, after retaining a finite prefix, **every** remaining term can be moved forward—not just the terms of one favourable subsequence.

## 3. Decomposing the thin end into finite slabs

We first work entirely inside \(H\). Fix \(k\) pairwise vertex-disjoint rays
\[
R_1,\ldots,R_k.
\]

### Lemma 2: separators of size at most \(k\)

For every finite \(X\subseteq V(H)\), there is a set
\[
S\subseteq V(H)\setminus X,\qquad |S|\leq k,
\]
such that every component of \(H-S\) meeting \(X\) is finite.

#### Proof

The assertion is trivial for \(X=\varnothing\), so suppose \(X\ne\varnothing\). Its external neighbourhood
\[
P=N_H(X)\setminus X
\]
is finite by local finiteness.

Take successively larger finite balls \(W_m\) containing \(X\cup P\), and let \(\partial W_m\) be their inner vertex boundaries. Apply finite Menger in
\[
H[W_m\setminus X]
\]
between \(P\) and \(\partial W_m\), allowing a separator to meet these two sets.

A separator \(S\) of size at most \(k\) would have the desired property. Indeed, an infinite component of \(H-S\) meeting \(X\) would, by local finiteness, contain a ray starting in \(X\). After its last visit to \(X\), that ray would give a \(P\)-to-\(\partial W_m\) path avoiding \(S\), a contradiction.

Consequently, if the desired \(S\) did not exist, finite Menger would give \(k+1\) vertex-disjoint \(P\)-to-\(\partial W_m\) paths for every sufficiently large \(m\). Their lengths tend to infinity. Since \(P\) is finite and \(H\) is locally finite, the usual finitely branching compactness argument—König’s infinity lemma applied to tuples of path prefixes—produces \(k+1\) pairwise vertex-disjoint rays. This contradicts the choice of \(k\). \(\square\)

For any finite nonempty \(S\), the graph \(H-S\) has finitely many components: each component has an edge to \(S\), and only finitely many edges meet \(S\). Since \(H\) is one-ended, exactly one of those components is infinite. Thus its complement in \(V(H)\) is finite.

Let
\[
F_H=F\cap V(H),
\]
and fix an increasing exhaustion of \(H\) by finite balls. Repeatedly applying Lemma 2 gives separators
\[
S_0,S_1,\ldots
\]
and infinite components \(C_n\) of \(H-S_n\), with
\[
D_n:=V(H)\setminus V(C_n),
\]
such that:

- \(D_n\) is finite;
- \(D_n\subseteq D_{n+1}\) and \(\bigcup_nD_n=V(H)\);
- \(S_{n+1}\subseteq C_n\);
- \(F_H\subseteq D_0\setminus S_0\);
- each \(S_n\) has size exactly \(k\) and meets each \(R_i\) exactly once.

Here is the recursion explicitly. At step \(n\), take the finite set \(X\) in Lemma 2 to contain \(F_H\), the initial vertex of every \(R_i\), the \(n\)-th ball, and \(D_{n-1}\) when \(n>0\). Every \(R_i\) must meet the resulting separator. Since the rays are disjoint and the separator has size at most \(k\), it has exactly one vertex on each ray and no other vertices.

Write
\[
S_n=\{s_1(n),\ldots,s_k(n)\},\qquad s_i(n)\in V(R_i).
\]
Along \(R_i\), these vertices occur in increasing order.

Define the finite slab
\[
P_n:=H\bigl[S_n\cup(D_{n+1}\setminus D_n)\bigr].
\]
Its ordered left and right boundary vertices are
\[
s_1(n),\ldots,s_k(n)
\quad\text{and}\quad
s_1(n+1),\ldots,s_k(n+1).
\]

These slabs satisfy:

1. \(P_n\cap P_{n+1}=H[S_{n+1}]\) at the level of their common vertices and induced edges;
2. nonconsecutive slabs have disjoint vertex sets;
3. for every \(N\),
   \[
   H=H[D_N]\;\cup\!\bigcup_{n\geq N}P_n;
   \]
4. the segment of \(R_i\) between \(s_i(n)\) and \(s_i(n+1)\) lies in \(P_n\).

For item 3, no edge can jump over a separator: because \(C_n\) is a component of \(H-S_n\), an edge from \(C_n\) to its complement must end in \(S_n\).

Thus \(H\) is a chain of finite, arbitrarily complicated slabs with a fixed number of boundary vertices and fixed disjoint rails connecting successive boundaries.

## 4. Pumping the slabs while preserving the rest of \(G\)

Vertices of \(H\) may have neighbours in \(A\), including infinitely many such incidences overall. We must preserve these adjacencies when moving the slabs.

Give each \(v\in V(H)\) the label
\[
\lambda(v)=N_G(v)\cap A.
\]
These labels lie in the finite poset
\[
Q=(2^A,\subseteq).
\]
A label-respecting minor model ensures that every original adjacency to \(A\) is retained.

Regard each \(P_n\) as a \(Q\)-labelled graph with its \(2k\) ordered boundary vertices distinguished. By the finite rooted, labelled Graph Minor Theorem and Lemma 1, there exist \(N\) and a strictly increasing \(f\) such that
\[
f(n)>n,\qquad P_n\preccurlyeq_* P_{f(n)}
\quad(n\geq N),
\]
where \(\preccurlyeq_*\) denotes the rooted, label-respecting relation.

For each \(n\geq N\), choose such a model
\[
(M_v^n:v\in V(P_n))
\]
inside \(P_{f(n)}\). In particular,
\[
s_i(f(n))\in M^n_{s_i(n)}
\quad\text{and}\quad
s_i(f(n)+1)\in M^n_{s_i(n+1)}.
\]

We now glue these finite models.

### Construction of the branch sets in \(H\)

For vertices in the retained prefix, put
\[
B_v=\{v\}\qquad(v\in D_N\setminus S_N).
\]

For a vertex \(v\) in the interior of a source slab \(P_n\), put
\[
B_v=M_v^n.
\]

For the first source boundary, put
\[
B_{s_i(N)}
=
V\!\left(R_i[s_i(N),s_i(f(N))]\right)
\;\cup\;
M^N_{s_i(N)}.
\]

For subsequent source boundaries, \(n>N\), put
\[
\begin{split}
B_{s_i(n)}
={}&M^{n-1}_{s_i(n)}\\
&\cup V\!\left(
 R_i[s_i(f(n-1)+1),s_i(f(n))]
 \right)\\
&\cup M^n_{s_i(n)}.
\end{split}
\]
A segment whose endpoints coincide is interpreted as a single vertex.

The connecting segments run through the gaps between the selected target slabs. They join the right-root branch set from one selected model to the corresponding left-root branch set from the next.

### Verification

**Every source vertex receives a branch set.**  
The \(D_n\) exhaust \(H\), the separators are pairwise disjoint, and the remaining vertices are slab interiors. Thus the cases above cover every vertex exactly once.

**The branch sets are finite and connected.**  
Every \(M_v^n\) is finite and connected. Each added rail segment is finite and meets the relevant model branch sets at the required distinguished target vertices. A separator branch set uses at most two finite model branch sets and one finite segment.

**Distinct branch sets are disjoint.**  
Within a selected target slab, this follows from its minor model. Different selected target slabs have disjoint interiors.

When selected slabs are consecutive, their common separator vertices belong to the corresponding rooted branch sets and are glued only for the same source vertex. The interiors of the added connecting segments lie in unselected slabs. Different rails are disjoint, and distinct connecting intervals on the same rail are separated by a selected slab.

Finally, the initial connecting segments meet the retained prefix only at their respective vertices of \(S_N\). These observations account for every possible overlap.

**Every edge of \(H\) is represented.**  
An edge in \(H[D_N]\) is represented by its original edge, since each endpoint’s branch set contains that endpoint. Every other edge lies in some source slab \(P_n\), where it is represented by \(M^n\). Enlarging the branch sets during gluing preserves these witnessing edges.

**Labels are respected.**  
For a prefix vertex, its original copy witnesses its label. Every other source vertex retains a branch set from at least one label-respecting slab model. Hence
\[
\forall v\in V(H)\quad
\exists w\in B_v
\quad\text{such that}\quad
\lambda(v)\subseteq\lambda(w).
\]

**The prescribed vertices are fixed.**  
Since
\[
F_H\subseteq D_0\setminus S_0
\subseteq D_N\setminus S_N,
\]
we have \(B_v=\{v\}\) for every \(v\in F_H\).

We have therefore constructed a label-respecting self-minor model of \(H\) with finite branch sets.

### Extending the model to all of \(G\)

For every vertex outside \(H\), use the singleton branch set
\[
B_v=\{v\}.
\]

Edges entirely outside \(H\) are retained unchanged. Since \(H\) is a component of \(G-A\), every edge between \(H\) and its complement has the form
\[
va,\qquad v\in V(H),\ a\in A.
\]
Here \(a\in\lambda(v)\). Choose \(w\in B_v\) with
\(\lambda(v)\subseteq\lambda(w)\). Then \(wa\in E(G)\), witnessing the required adjacency between \(B_v\) and \(B_a=\{a\}\).

This proves that the assembled family is a minor model of \(G\) in \(G\), with all vertices outside \(H\), and all vertices of \(F\), fixed as singletons.

### The model is genuinely proper

Because \(f(N)>N\), the initial rail segment
\[
R_1[s_1(N),s_1(f(N))]
\]
contains an edge \(e\). The entire segment lies in \(B_{s_1(N)}\). Moreover, it avoids \(F\): its vertices lie in \(S_N\cup C_N\), whereas
\[
F_H\subseteq D_N\setminus S_N.
\]

Contract \(e\). Since both endpoints of \(e\) lie in the same branch set, this contraction merges no two distinct branch sets. Their images remain connected and pairwise disjoint, and every required adjacency remains represented. Hence
\[
G\preccurlyeq G/e.
\]
All specified singleton branch sets remain unchanged. This proves the theorem. \(\square\)

## 5. The isolated-thin-end corollary

Let \(G\) be locally finite and let \(\omega\) be an isolated thin end. Choose a finite set \(A\) such that the component \(H\) of \(G-A\) containing tails of \(\omega\) contains no other end.

Then \(H\) is connected, locally finite and one-ended. Indeed, two different ends of \(H\) would remain different in \(G\) after deleting \(A\) and a suitable finite separator inside \(H\).

Taking tails shows that the maximum number of disjoint rays in \(H\) equals the vertex-degree of \(\omega\), which is finite. The theorem applies.

Consequently, the result includes:

- every locally finite one-ended graph with a thin end;
- every locally finite graph with finitely many ends, at least one of them thin;
- graphs obtained by adding finitely many arbitrarily adjacent vertices to a locally finite, one-ended, thin graph;
- graphs with an otherwise unrestricted exterior attached through the finite set \(A\) in the theorem.

No bound is imposed on the sizes, degrees within individual slabs, or treewidths of the finite slabs.

## 6. What remains unresolved

The essential resources in this proof are:

1. **finite slabs**, so the proved finite Graph Minor Theorem applies;
2. a **fixed finite number \(2k\) of terminals**;
3. disjoint rails through the skipped slabs, allowing independently chosen minor models to be glued.

For a thick end, there need not be separators of a fixed finite size. For a non-isolated thin end, finite separators may leave additional infinite pieces, so the slab sequence above need not consist of finite graphs.

Thus this argument does not settle the unrestricted countable case, and it supplies no explicit uncountable counterexample. The established claim is the displayed special-case theorem; I do not assert that this sufficient condition or its proof is new.