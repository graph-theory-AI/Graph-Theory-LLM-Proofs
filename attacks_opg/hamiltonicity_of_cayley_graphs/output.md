```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A constructive subgroup-splicing argument proves Hamiltonicity for conjugacy-invariant connection sets and yields an additional central-generator criterion.",
  "would_publish": false,
  "caveats": "The arbitrary-connection-set case is not resolved; no novelty is claimed for these special cases."
}
```

# 1. Scope and partial result

I use the intended formulation: \(G\) is a finite group with \(|G|\ge 3\), and
\[
S=S^{-1}\subseteq G\setminus\{1\},\qquad \langle S\rangle=G.
\]
The undirected Cayley graph \(\Gamma=\operatorname{Cay}(G,S)\) has edges \(g\sim gs\). Thus disconnected graphs and the small-order exceptions are not being used as counterexamples.

I do not settle the unrestricted conjecture. The following special case admits a self-contained constructive proof.

**Theorem 1.** If \(S\) is invariant under conjugation by \(G\), then \(\operatorname{Cay}(G,S)\) has a Hamilton cycle.

This covers every abelian group and, for arbitrary finite groups, every inverse-closed generating set that is a union of conjugacy classes. The argument also gives a criterion for some connection sets that are not conjugacy-invariant.

The mechanism is to partition \(G\) into cosets carrying compatible Hamilton cycles, then splice those cycles along a bounded-degree spanning tree.

# 2. An exact cycle–tree product lemma

Write \(\square\) for the Cartesian product of graphs.

**Lemma 2.** Let \(m\ge 3\), and let \(T\) be a finite tree, possibly consisting of one vertex. Then
\[
C_m\square T\text{ is Hamiltonian}
\quad\Longleftrightarrow\quad
\Delta(T)\le m.
\]

**Proof: sufficiency.** Suppose \(\Delta(T)\le m\). Properly edge-colour \(T\) with \(m\) colours. This can be done greedily after rooting \(T\): at each nonroot vertex, assign its child edges distinct colours different from its parent-edge colour.

Identify the colours with the \(m\) edges of \(C_m\). Initially, take the disjoint cycle
\[
C_m\times\{v\}
\]
over each \(v\in V(T)\).

For an edge \(uv\in E(T)\) whose colour is the cycle edge \(xy\), perform the switch
\[
\begin{aligned}
&\text{delete }(x,u)(y,u),\ (x,v)(y,v),\\
&\text{insert }(x,u)(x,v),\ (y,u)(y,v).
\end{aligned}
\]
All inserted edges belong to the Cartesian product.

Process the tree edges in any order. At every stage, the current cycles correspond to the connected components of the forest of already processed tree edges. Consequently, the next tree edge joins two different current cycles. The two fibre edges required for its switch are still present: a fibre edge can previously have been deleted only by an incident tree edge of the same colour, and proper edge-colouring excludes that.

Deleting one edge from each of two disjoint cycles produces two paths; the two inserted edges join these paths into one cycle. Thus every switch merges two current cycles. After all \(|V(T)|-1\) switches, there is one spanning cycle.

**Proof: necessity.** In a Hamiltonian graph, deleting a nonempty vertex set \(X\) leaves at most \(|X|\) nonempty components: this holds already for the Hamilton cycle with \(X\) deleted.

Delete the \(m\)-vertex fibre over \(v\in V(T)\). The remaining product has exactly \(\deg_T(v)\) components, one for each component of \(T-v\). Hence \(\deg_T(v)\le m\). This holds for every \(v\). \(\square\)

The bound is therefore exact for this product construction, not merely an artefact of the proof.

# 3. Implementing the product inside a Cayley graph

For a subgroup \(H\le G\), use the right cosets
\[
H\backslash G=\{Hg:g\in G\}.
\]
The associated Schreier graph has edges
\[
Hg\sim Hgs\qquad(s\in S),
\]
with loops discarded.

**Lemma 3 — subgroup-splicing certificate.** Suppose \(H\le G\), with \(|H|=m\ge3\), has a Hamilton cycle \(D\) in \(\Gamma[H]\). Assume:

1. every right translate \(Dg\), \(g\in G\), is also a cycle in \(\Gamma\);
2. the Schreier graph on \(H\backslash G\) has a spanning tree \(T\) with \(\Delta(T)\le m\).

Then \(\Gamma\) is Hamiltonian.

**Proof.** Root \(T\) at the coset \(H\). Choose representatives recursively. Set \(g_H=1\). If \(q'\) is a child of \(q\), choose \(s\in S\) witnessing the Schreier edge \(q\sim q'\), so that \(q'=qs\), and put
\[
g_{q'}=g_qs.
\]

Identify the vertices of \(\Gamma\) with pairs \((h,q)\in H\times V(T)\) by
\[
(h,q)\longmapsto hg_q.
\]
This is a bijection.

Within the fibre over \(q\), the cycle \(Dg_q\) is available by assumption. Across a parent–child edge \(qq'\), all matching edges are available, because
\[
hg_{q'}=hg_qs\qquad(h\in H).
\]
These cycles and matchings form a spanning subgraph isomorphic to
\[
C_m\square T.
\]
Lemma 2 completes the proof. \(\square\)

The right-translation assumption is particularly transparent in terms of edge labels. If an edge of \(D\) is
\[
h\sim ht,\qquad t\in S\cap H,
\]
then its right translate by \(g\) is
\[
hg\sim htg=(hg)(g^{-1}tg).
\]
Thus it is enough that every label used by \(D\) has all its \(G\)-conjugates in \(S\). In particular, conjugacy-invariance of \(S\) guarantees the assumption.

## A bounded-degree Schreier tree

**Lemma 4.** If \(R\subseteq S\) generates \(G\), and \(|R|=r\), then every Schreier graph on \(H\backslash G\) has a spanning tree of maximum degree at most \(r+1\).

If \(H\trianglelefteq G\), it is enough that the images of \(R\) generate \(G/H\).

**Proof.** Consider the directed edges
\[
Hg\longrightarrow Hga\qquad(a\in R).
\]
Every coset is reachable from \(H\). Indeed, because the group is finite, inverses of elements of \(R\) can be expressed as positive powers, so group generation gives reachability by directed words.

Choose a directed breadth-first spanning tree rooted at \(H\). Each vertex has at most \(r\) children, and each nonroot vertex has one parent. Its underlying undirected tree therefore has maximum degree at most \(r+1\).

For normal \(H\), the same argument takes place in the finite quotient group \(G/H\). \(\square\)

Notice that \(R\) need not be inverse-closed. This is why the bound is \(r+1\), rather than the less useful bound \(2r\) obtained directly from undirected degrees.

# 4. Proof of Theorem 1

We use strong induction on \(|G|\). Choose an inclusion-minimal generating subset
\[
R=\{a_1,\ldots,a_r\}\subseteq S.
\]

### Case 1: \(r=1\)

Then \(G=\langle a_1\rangle\). Since \(|G|\ge3\), the edges labelled \(a_1^{\pm1}\) give the Hamilton cycle through the successive powers of \(a_1\).

### Case 2: \(r=2\), and both generators are involutions

The graph
\[
\operatorname{Cay}(G,\{a_1,a_2\})
\]
is connected and 2-regular: the two generators are distinct, nonidentity involutions. It is therefore a single cycle, necessarily spanning \(G\).

### Case 3: \(r=2\), and some generator has order at least \(3\)

Let \(a\in R\) have order \(m\ge3\), and put \(H=\langle a\rangle\). The cyclic ordering of \(H\) gives a Hamilton cycle \(D\) using labels \(a^{\pm1}\).

Conjugacy-invariance of \(S\) ensures that every right translate \(Dg\) is a cycle in \(\Gamma\). Lemma 4 supplies a Schreier spanning tree with maximum degree at most
\[
r+1=3\le m.
\]
Lemma 3 gives a Hamilton cycle in \(\Gamma\).

### Case 4: \(r\ge3\)

Put
\[
H=\langle a_1,\ldots,a_{r-1}\rangle.
\]
Minimality of \(R\) makes \(H\) a proper subgroup. Moreover, every inclusion in the chain
\[
\{1\}
<
\langle a_1\rangle
<
\langle a_1,a_2\rangle
<
\cdots
<
\langle a_1,\ldots,a_{r-1}\rangle
\]
is strict. Otherwise one of the \(a_i\) could be removed from \(R\). Each subgroup index in the chain is at least two, so
\[
|H|\ge 2^{r-1}\ge r+1
\qquad(r\ge3).
\]
In particular, \(|H|\ge4\).

The set \(S\cap H\) is inverse-closed, generates \(H\), and is invariant under conjugation by \(H\). Since \(H\) is proper, induction supplies a Hamilton cycle \(D\) in
\[
\operatorname{Cay}(H,S\cap H).
\]
Global conjugacy-invariance of \(S\) ensures that all right translates \(Dg\) are cycles in \(\Gamma\).

By Lemma 4, the Schreier graph has a spanning tree of maximum degree at most
\[
r+1\le |H|.
\]
Lemma 3 again applies.

These cases cover every possible \(r\). No induction call involves a group of order one or two, so there is no hidden small-order exception. \(\square\)

This proof is constructive: it recursively constructs the subgroup cycle, builds a Schreier tree, edge-colours that tree, and performs the switches from Lemma 2.

# 5. A criterion for arbitrary connection sets with a central generator

The same machinery applies without conjugacy-invariance of the whole connection set.

**Theorem 5.** Let \(\Gamma=\operatorname{Cay}(G,S)\) be finite, connected and undirected. Suppose
\[
z\in S\cap Z(G)
\]
has order \(m\ge3\). Let \(R\subseteq S\) have images generating \(G/\langle z\rangle\), and write \(r=|R|\). If
\[
m\ge r+1,
\]
then \(\Gamma\) is Hamiltonian.

**Proof.** Take \(H=\langle z\rangle\), with its cycle of successive powers of \(z\). Every right translate of this cycle remains in \(\Gamma\), since
\[
g^{-1}zg=z\in S.
\]
The normal-subgroup version of Lemma 4 gives a quotient spanning tree of maximum degree at most \(r+1\le m\). Apply Lemma 3. \(\square\)

No splitting assumption on the central extension is needed.

There is also an unconditional numerical version. If
\[
q=|G:\langle z\rangle|,
\]
one can select a generating subset of the projected connection set with at most \(\lfloor\log_2q\rfloor\) elements: in an irredundant generating sequence, each successive generated subgroup has at least twice the preceding order. Consequently,
\[
\boxed{\;
\operatorname{ord}(z)\ge
\max\{3,\,1+\lfloor\log_2|G:\langle z\rangle|\rfloor\}
\quad\Longrightarrow\quad
\operatorname{Cay}(G,S)\text{ is Hamiltonian}.
\;}
\]

For example, for any finite group \(Q=\langle a,b\rangle\),
\[
C_3\square
\operatorname{Cay}\bigl(Q,\{a^{\pm1},b^{\pm1}\}\setminus\{1\}\bigr)
\]
is Hamiltonian. This conclusion does not require a Hamilton path or cycle in the Cayley graph on \(Q\).

# 6. What prevents this from proving the full conjecture?

For an arbitrary connection set \(S\), right translations need not preserve Cayley edges:
\[
h\sim ht
\quad\not\Longrightarrow\quad
hg\sim htg,
\]
because the latter edge requires
\[
g^{-1}tg\in S.
\]
Thus an internally Hamiltonian subgroup need not provide compatible cycles on its cosets. The Schreier tree still exists, but the spanning product used in Lemma 3 may not.

Replacing \(S\) by its conjugacy closure does not repair the argument for the original graph. It adds edges, and the constructed Hamilton cycle may use those added edges.

Accordingly, the proofs above are complete for the stated special cases, but they provide neither a proof nor a counterexample for arbitrary generating sets. The unresolved step is finding a replacement for the compatible-fibre construction when conjugation sends the necessary edge labels outside \(S\).