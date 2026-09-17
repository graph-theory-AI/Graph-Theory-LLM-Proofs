```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A stronger transversal theorem holds when each strongly connected component is Hamiltonian or becomes acyclic after deleting one vertex.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of these special cases has not been verified."
}
```

## 1. Partial result

All digraphs below are finite and loopless; antiparallel arcs are allowed. Directed paths have distinct vertices, and stability prohibits arcs in either direction.

I obtain an SCC-based extension of the feedback-one case. The proof is independent of the previous attempt. It does **not** require the resulting stable set to contain a prescribed feedback vertex, but it allows arbitrarily many cyclic strong components and gives a transversal independent of vertex weights.

### Theorem
Suppose every strongly connected component \(C\) of a digraph \(D\) satisfies at least one of the following:

- **(F)** There is a vertex \(x_C\in C\) such that \(D[C]-x_C\) is acyclic.
- **(H)** \(D[C]\) contains a directed Hamiltonian cycle.

Then \(D\) has a stable set \(S\) with the following property:
\[
\boxed{\quad
V(P)\cap S=\varnothing
\quad\Longrightarrow\quad
V(P)\subsetneq V(Q)
\text{ for some directed path }Q.
\quad} \tag{1}
\]

Consequently:

1. \(S\) meets every longest directed path.
2. The **same** \(S\) meets every maximum-weight directed path for **every** assignment of positive vertex weights.
3. If every component satisfies (F), then \(S\) meets every **right-maximal** directed path: every path avoiding \(S\) can actually be extended by appending one new vertex.

Here, right-maximal means that no vertex outside the path can be appended at its terminal end. A singleton component satisfies (F), using its unique vertex.

Thus the theorem includes all digraphs whose individual strong components have directed feedback vertex number at most one. Their *total* feedback vertex number need not be bounded. No uniformity assumption is imposed on arcs between components.

---

## 2. An elementary tool: kernels of DAGs

A **kernel** of a digraph \(H\) is a stable set \(K\) such that every vertex outside \(K\) sends an arc to a vertex of \(K\).

### Lemma
Every finite acyclic digraph has a kernel.

### Proof
Process the vertices in reverse topological order. Select a vertex precisely when it has no out-neighbour already selected.

The selected vertices are stable: all arcs run forward in topological order, and an earlier vertex is rejected if it sends an arc to a selected later vertex. Every rejected vertex has an out-neighbour that was selected and remains selected. ∎

This construction takes linear time. The kernel of the empty digraph is the empty set.

---

## 3. Construction of the stable set

Let
\[
C_1,C_2,\ldots,C_r
\]
be a topological ordering of the strong components, so every intercomponent arc goes from \(C_i\) to \(C_j\) with \(i<j\).

Process the components in reverse order. When processing \(C_i\), let \(S_{>i}\) be the vertices already selected in later components, and define
\[
B_i=\{u\in C_i:\ u\to s\text{ for some }s\in S_{>i}\}.
\]

There are no arcs from \(S_{>i}\) into \(C_i\). Thus a vertex of \(C_i\) is nonadjacent to all of \(S_{>i}\) exactly when it lies outside \(B_i\).

Choose a set \(T_i\subseteq C_i\setminus B_i\) as follows.

### Components of type (F)

Fix a witness \(x=x_{C_i}\).

- If \(x\notin B_i\), put
  \[
  T_i=\{x\}.
  \]
- If \(x\in B_i\), then \(D[C_i\setminus B_i]\) is acyclic, since it is an induced subdigraph of \(D[C_i]-x\). Let
  \[
  T_i
  \]
  be a kernel of \(D[C_i\setminus B_i]\).

If a component satisfies both conditions, we may use this rule.

### Remaining components, of type (H)

- If \(C_i\setminus B_i=\varnothing\), put \(T_i=\varnothing\).
- Otherwise choose any \(z_i\in C_i\setminus B_i\) and put
  \[
  T_i=\{z_i\}.
  \]

Finally, set
\[
S=\bigcup_{i=1}^r T_i.
\]

### Stability

Each \(T_i\) is stable. Since \(T_i\subseteq C_i\setminus B_i\), no vertex of \(T_i\) sends an arc to \(S_{>i}\). No arc goes in the opposite direction, by the component ordering. Inductively, \(S\) is stable.

---

## 4. Proof of the transversal property

Let \(P\) be a directed path avoiding \(S\), and let its last vertex \(u\) lie in \(C_i\).

A directed path visits each strong component in one contiguous segment. Indeed, leaving and subsequently returning to a component would produce a directed cycle in the condensation. We consider the rule used at \(C_i\).

### Case A: Type (F), with \(x_{C_i}\in B_i\)

Here \(T_i\) is a kernel of \(D[C_i\setminus B_i]\).

If \(u\in B_i\), then \(u\to s\) for some \(s\in S_{>i}\). Since \(P\) avoids \(S\), appending \(s\) extends \(P\).

If \(u\notin B_i\), then \(u\notin T_i\), again because \(P\) avoids \(S\). The kernel property gives an arc
\[
u\to t,\qquad t\in T_i.
\]
Appending \(t\) extends \(P\).

Thus in this case \(P\) has a one-vertex extension.

### Case B: Type (F), with \(x=x_{C_i}\notin B_i\)

Here \(T_i=\{x\}\), so \(P\) avoids \(x\).

If \(C_i=\{x\}\), this case cannot contain the terminal vertex of \(P\). Otherwise, strong connectivity implies that \(u\) has an out-neighbour \(v\) inside \(C_i\).

I claim that \(v\notin V(P)\). If \(v\) were on \(P\), the subpath from \(v\) to \(u\) would lie entirely in \(C_i-x\). Together with \(u\to v\), it would form a directed cycle in \(D[C_i]-x\), contradicting acyclicity.

Therefore \(Pv\) is a directed path extending \(P\).

This proves, in particular, the right-maximal-path conclusion when all components are treated by (F).

### Case C: Type (H), with \(C_i=B_i\)

The terminal vertex \(u\) has an out-neighbour in \(S_{>i}\). Appending that vertex extends \(P\).

### Case D: Type (H), with \(T_i=\{z_i\}\)

Write
\[
P=P_0R,
\]
where \(R\) is the terminal segment of \(P\) lying in \(C_i\), and let \(a\) be the first vertex of \(R\). The prefix \(P_0\) contains no vertex of \(C_i\).

A Hamiltonian cycle of \(D[C_i]\), traversed starting at \(a\) and stopped immediately before returning to \(a\), gives a directed Hamiltonian path \(R'\) of \(D[C_i]\) starting at \(a\).

Replace \(R\) by \(R'\). The resulting sequence
\[
Q=P_0R'
\]
is a directed path:

- the incoming arc to \(a\), if present, is unchanged;
- \(P_0\) is disjoint from \(C_i\);
- \(R'\) visits every vertex of \(C_i\) exactly once.

Moreover,
\[
V(Q)=V(P_0)\cup C_i\supsetneq V(P),
\]
because \(P\) avoids \(z_i\in C_i\).

These four cases establish (1). ∎

### Why this handles all positive weightings simultaneously

If \(w(v)>0\) for every vertex and \(V(P)\subsetneq V(Q)\), then
\[
w(Q)-w(P)=\sum_{v\in V(Q)\setminus V(P)}w(v)>0.
\]
Hence no maximum-weight path can avoid \(S\).

The construction of \(S\) never used the weights.

---

## 5. A further stable-feedback-set extension

The singleton feedback set in condition (F) can be replaced by a larger stable set under a local, one-sided compatibility condition.

### Proposition
The theorem remains valid if a component of type (F) is instead equipped with a nonempty stable set \(X_C\subseteq C\) such that:

1. \(D[C]-X_C\) is acyclic; and
2. all vertices of \(X_C\) have the same out-neighbourhood outside \(C\):
   \[
   N_D^+(x)\setminus C=N_D^+(y)\setminus C
   \qquad(x,y\in X_C).
   \]

If every component is of this generalized type, the resulting stable set meets every right-maximal directed path.

### Proof
At the stage when \(C=C_i\) is processed, the common exterior out-neighbourhood condition implies that either
\[
X_C\cap B_i=\varnothing
\quad\text{or}\quad
X_C\subseteq B_i.
\]

In the first case, select \(T_i=X_C\). This is stable and nonadjacent to the previously selected vertices. Any path ending in a nontrivial \(C\) and avoiding \(X_C\) can be extended by exactly the argument of Case B: an arc from its terminal vertex back into the path would create a cycle in \(D[C]-X_C\).

In the second case, \(D[C\setminus B_i]\) is acyclic. Select a kernel of this DAG and apply Case A.

The remaining arguments are unchanged. ∎

For a strongly connected digraph, the exterior-neighbourhood condition is vacuous. We therefore obtain the particularly simple consequence:

> If a nontrivial strongly connected digraph has a stable feedback vertex set \(X\), then \(X\) itself meets every right-maximal directed path.

This follows directly from the terminal-extension argument.

---

## 6. Algorithmic content

For the main theorem, suppose each component is supplied with either:

- a vertex whose deletion makes that component acyclic; or
- a directed Hamiltonian cycle.

Then the stable set can be constructed in
\[
O(|V(D)|+|A(D)|)
\]
time:

1. compute and topologically order the strong components;
2. process them backwards, scanning outgoing arcs to determine \(B_i\);
3. construct a DAG kernel whenever the feedback vertex belongs to \(B_i\).

The DAGs used for kernel computations lie in distinct components, so their total size is linear. The supplied component witnesses can also be verified in linear total time.

In particular, this does not require solving a longest-path problem, nor does it require knowing a vertex weighting.

---

## 7. What remains unresolved

The construction does not apply to arbitrary strong components.

The main difficulty is not merely finding a stable transversal of the longest paths *inside* a component. A longest path of the whole digraph may enter that component at an externally determined vertex. Its terminal segment need not be an unrestricted longest path of the component.

The two proved mechanisms avoid that difficulty:

- a stable feedback set supplies a one-step terminal extension;
- a Hamiltonian cycle supplies a spanning path beginning at **every possible entry vertex**.

Likewise, in the stable-feedback-set extension, dropping the exterior-neighbourhood condition may leave
\[
\varnothing\ne X_C\cap B_i\ne X_C.
\]
Then one cannot select all of \(X_C\), while deleting \(B_i\) need not leave an acyclic digraph. The construction provides no rule for that situation.

Thus this is a self-contained partial result, not a proof of the general Laborde–Payan–Xuong conjecture. No claim of novelty is made.