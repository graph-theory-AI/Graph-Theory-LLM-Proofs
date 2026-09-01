```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "NP-completeness follows when the bipartite symmetric part is connected, and more generally under explicit component-side, triangle-free-side, or circular-core orbit hypotheses.",
  "would_publish": false,
  "caveats": "The remaining case has disconnected symmetric part with cyclic obstructions distributed across several components; no claim of literature novelty is made."
}
```

# Partial resolution of Conjecture 2.16

## 1. Definitions and elementary facts

All digraphs below are finite and loopless, as in the source paper. Write
\[
D\to_\circ F
\]
when there is a circular homomorphism from \(D\) to \(F\).

For a digraph \(F\), let \(B(F)\) be its symmetric graph: \(V(B(F))=V(F)\), and \(xy\in E(B(F))\) precisely when both \(xy\) and \(yx\) are arcs of \(F\). Thus edges of \(B(F)\) correspond to digons of \(F\).

The following characterization is fundamental.

### Lemma 1: cycle-image characterization

A map \(f:V(D)\to V(F)\) is circular if and only if, for every directed cycle \(C\) of \(D\), the induced subdigraph
\[
F[f(V(C))]
\]
contains a directed cycle.

#### Proof

If \(F[f(V(C))]\) is acyclic, then the inverse image of this acyclic vertex set contains \(C\), contradicting circularity.

Conversely, if \(A\subseteq V(F)\) is acyclic but \(D[f^{-1}(A)]\) contains a directed cycle \(C\), then \(f(V(C))\subseteq A\), so \(F[f(V(C))]\) is acyclic. ∎

In particular, a source digon must map to a target digon: its two vertices cannot be identified, and their images must be adjacent in \(B(F)\).

Circular homomorphisms compose. Moreover,
\[
D_1\sqcup D_2\to_\circ F
\quad\Longleftrightarrow\quad
D_1\to_\circ F\ \text{and}\ D_2\to_\circ F.
\]

For fixed \(F\), the problem belongs to NP. Given \(f:V(D)\to V(F)\), precompute the finitely many acyclic subsets \(A\subseteq V(F)\) and test whether every \(D[f^{-1}(A)]\) is acyclic.

The only previously established result used below is the supplied part of Theorem 2.17:

> If a fixed target \(H\) is digon-free and contains a directed cycle, then Circular \(H\)-Colouring is NP-complete.

---

## 2. A finite-disjunction lemma

The reductions below naturally produce a finite disjunction of fixed-target problems.

### Lemma 2

Let \(H_1,\dots,H_m\) be fixed digraphs. Suppose at least one \(H_i\) is cyclic, and Circular \(H_i\)-Colouring is NP-hard for every cyclic member of the family. Then
\[
\mathcal L=\{D:\ D\to_\circ H_i\text{ for some }i\}
\]
is NP-hard.

#### Proof

Put a preorder on the \(H_i\) by
\[
H_i\preceq H_j\quad\Longleftrightarrow\quad H_i\to_\circ H_j.
\]
Start with a cyclic member and choose, among the equivalence classes reachable from it, a maximal class. Let \(H_*\) be a representative.

The target \(H_*\) is cyclic: a cyclic digraph cannot map circularly to an acyclic digraph. Moreover, if \(H_*\to_\circ H_i\), maximality implies \(H_i\to_\circ H_*\).

Given \(D\), form
\[
D'=D\sqcup H_*.
\]
If \(D\to_\circ H_*\), then \(D'\to_\circ H_*\). Conversely, if \(D'\to_\circ H_i\), then \(H_*\to_\circ H_i\), hence \(H_i\to_\circ H_*\), and therefore
\[
D\to_\circ H_i\to_\circ H_*.
\]
Thus
\[
D'\in\mathcal L\quad\Longleftrightarrow\quad D\to_\circ H_*.
\]
This is a many-one reduction from the NP-hard Circular \(H_*\)-Colouring problem. ∎

---

## 3. Synchronizing one component of the symmetric part

This gives the strongest partial result.

### Theorem 3

Let \(F\) be a digraph whose symmetric graph \(B=B(F)\) is nonempty and bipartite. Let
\[
C_1,\dots,C_t
\]
be the nontrivial connected components of \(B\), with bipartitions
\[
V(C_i)=X_i\cup Y_i.
\]
If at least one of the induced digraphs
\[
F[X_i],\qquad F[Y_i]
\]
contains a directed cycle, then Circular \(F\)-Colouring is NP-complete.

#### Proof

Choose a fixed even integer \(L\) such that, in every \(C_i\), any two vertices in the same bipartition class are joined by a walk of length exactly \(L\).

Such an \(L\) exists. Same-side distances are even; choose a sufficiently large common even \(L\), and lengthen a shortest path by backtracking along edges.

Given an input digraph \(D\), construct \(T_L(D)\) as follows:

1. Add one new vertex \(z\).
2. For every \(v\in V(D)\), add an internally vertex-disjoint path of length \(L\) from \(z\) to \(v\).
3. Replace every edge of every added path by a digon.

We claim
\[
T_L(D)\to_\circ F
\quad\Longleftrightarrow\quad
D\to_\circ F[X_i]\ \text{or}\ D\to_\circ F[Y_i]
\quad\text{for some }i. \tag{1}
\]

Suppose first that \(g:T_L(D)\to_\circ F\). Every added source digon maps to an edge of \(B\). Hence every added path maps to a walk in one connected component \(C_i\). Since all paths start at \(z\), all vertices of \(D\) map into the same \(C_i\). As \(L\) is even, all \(g(v)\), \(v\in V(D)\), lie in the same bipartition class, say \(X_i\).

The restriction \(g|_{V(D)}\) is then a circular map
\[
D\to_\circ F[X_i],
\]
by Lemma 1.

Conversely, suppose \(h:D\to_\circ F[X_i]\). Choose any \(x\in X_i\) as the image of \(z\). For each \(v\in V(D)\), choose a length-\(L\) walk in \(C_i\) from \(x\) to \(h(v)\), and use it to colour the corresponding added path.

It remains to verify circularity. A directed cycle contained in \(D\) has cyclic image because \(h\) is circular. Any other directed cycle uses an arc from an added digon; its image contains the corresponding target digon and is therefore cyclic. Thus the extended map is circular. The argument for \(F[Y_i]\) is identical, proving (1).

Each \(F[X_i]\) and \(F[Y_i]\) is digon-free. Therefore every cyclic member of this finite family has an NP-complete circular-colouring problem by Theorem 2.17. If at least one is cyclic, Lemma 2 applied to (1) gives NP-hardness. Membership in NP was noted above. ∎

### Corollary 4: the connected symmetric-part case

Suppose \(B(F)\) is connected, bipartite, and nonempty, and \(F\) is not 2-dicolourable. Then Circular \(F\)-Colouring is NP-complete.

#### Proof

Let \(X\cup Y\) be the unique bipartition of \(B(F)\), up to swapping. If both \(F[X]\) and \(F[Y]\) were acyclic, then \(X,Y\) would be a 2-dicolouring of \(F\). Hence one of them is cyclic, and Theorem 3 applies. ∎

Thus the conjecture is settled for the entire residual case in which the symmetric graph is connected.

---

## 4. A second reduction using 3-uniform hypergraph 2-colourability

The preceding synchronization forces all input vertices into one component of \(B(F)\). The next argument permits different variables to use different components.

Let
\[
W=\{v\in V(F):d_{B(F)}(v)>0\}
\]
be the support of the symmetric graph. A coherent bipartition of \(W\) means a partition \(W=P\cup Q\) obtained by selecting a bipartition orientation independently in every nontrivial component of \(B(F)\).

### Theorem 5

Suppose \(B(F)\) is nonempty and bipartite. If there is a coherent bipartition \(W=P\cup Q\) such that neither \(F[P]\) nor \(F[Q]\) contains a directed triangle, then Circular \(F\)-Colouring is NP-complete.

#### Proof

Reduce from 2-colourability of 3-uniform hypergraphs, equivalently the classical Property B problem.

Let \(\mathcal H=(U,\mathcal E)\) be a 3-uniform hypergraph, with isolated vertices removed. Construct a digraph \(D_{\mathcal H}\).

For each \(u\in U\), introduce a root \(r_u\). For every incidence \(u\in e\), introduce vertices \(s_{u,e}\) and \(t_{u,e}\), and add the two digons
\[
r_u\leftrightarrow s_{u,e}\leftrightarrow t_{u,e}.
\]
For every hyperedge \(e=\{u,v,w\}\), add the directed triangle
\[
t_{u,e}\to t_{v,e}\to t_{w,e}\to t_{u,e}.
\]

We prove
\[
\mathcal H\text{ is 2-colourable}
\quad\Longleftrightarrow\quad
D_{\mathcal H}\to_\circ F. \tag{2}
\]

Choose a fixed target digon \(a\leftrightarrow b\), with \(a\in P\) and \(b\in Q\).

If \(c:U\to\{0,1\}\) is a proper hypergraph 2-colouring, map \(r_u\) and all \(t_{u,e}\) to \(a\) when \(c(u)=0\), and to \(b\) when \(c(u)=1\). Map every intermediate \(s_{u,e}\) to the opposite endpoint. Every source digon maps to \(a\leftrightarrow b\). Every clause triangle has nonmonochromatic image, hence its image contains both \(a\) and \(b\).

The subdigraph consisting only of non-digon arcs is a disjoint union of the clause triangles. Consequently, every other directed cycle uses an arc belonging to a source digon and its image contains \(a\leftrightarrow b\). The resulting map is circular.

Conversely, let \(f:D_{\mathcal H}\to_\circ F\). Every source digon maps to an edge of \(B(F)\). Hence, along the even path
\[
r_u-s_{u,e}-t_{u,e},
\]
the images \(f(r_u)\) and \(f(t_{u,e})\) lie in the same side \(P\) or \(Q\). All occurrence terminals of \(u\) therefore lie on the same side. Colour \(u\) by \(0\) or \(1\) according to that side.

Consider \(e=\{u,v,w\}\). If all three hypergraph colours were the same, the image of its directed triangle would be a set of at most three vertices wholly contained in \(P\), or wholly contained in \(Q\). Such a set contains no digon because \(P,Q\) are independent in \(B(F)\), and by hypothesis contains no directed triangle. It is therefore acyclic, contradicting Lemma 1. Thus every hyperedge is nonmonochromatic, proving (2).

The construction is polynomial, so NP-hardness follows. ∎

### Consequence

In particular, Theorem 5 applies whenever the subdigraph induced by the non-isolated vertices of \(B(F)\) has no directed triangle at all. Thus a further substantial portion of the disconnected residual case is settled.

---

## 5. A circular-core pinning lemma

There is also a useful target-specific forcing mechanism.

A circular core of \(F\) is an induced subdigraph \(C\subseteq F\) of minimum order such that
\[
F\to_\circ C\to_\circ F.
\]
Such a core exists by taking the image of a circular endomorphism of minimum image size. Every circular endomorphism of \(C\) is bijective; since its inverse is a positive power of the same permutation, its inverse is also circular. Thus these endomorphisms form a group \(\Gamma\) of circular automorphisms.

### Proposition 6

Let \(C\) be a circular core of \(F\), let \(c\in V(C)\), and let
\[
O=\Gamma c
\]
be its orbit. Then
\[
\text{Circular }C[O]\text{-Colouring}\ \leq_m\ \text{Circular }F\text{-Colouring}.
\]

#### Proof

Given \(D\), attach to each vertex \(v\in V(D)\) a fresh copy \(C_v\) of \(C\), identifying \(v\) with the vertex corresponding to \(c\). Different copies otherwise have disjoint vertex sets. Call the resulting digraph \(D^\bullet\).

Every directed cycle of \(D^\bullet\) is contained either in \(D\) or in one of the attached copies, since each copy meets the rest at a single cut vertex.

Suppose \(D^\bullet\to_\circ C\). Its restriction to \(C_v\) is a circular endomorphism of \(C\), hence a circular automorphism. Therefore the image of \(v\) lies in \(O\). Restriction to \(D\) gives
\[
D\to_\circ C[O].
\]

Conversely, suppose \(h:D\to_\circ C[O]\). For each \(v\), choose \(\gamma_v\in\Gamma\) with \(\gamma_v(c)=h(v)\), and colour \(C_v\) by \(\gamma_v\). Since all cycles lie within one block, this extends \(h\) to a circular map \(D^\bullet\to_\circ C\).

Finally, \(F\) and \(C\) have exactly the same circular-colourability language because they map circularly to one another. ∎

### Corollary 7

If some circular-automorphism orbit \(O\) of the circular core induces a digon-free subdigraph \(C[O]\) containing a directed cycle, then Circular \(F\)-Colouring is NP-complete.

This follows from Proposition 6 and the digon-free case of Theorem 2.17.

---

## 6. Why these arguments do not yet cover every residual target

The hypotheses of Theorems 3 and 5 are not automatic. For example, consider the six-vertex digraph with vertices
\[
a_0,a_1,b_0,b_1,c_0,c_1,
\]
digons
\[
a_0\leftrightarrow a_1,\qquad
b_0\leftrightarrow b_1,\qquad
c_0\leftrightarrow c_1,
\]
and, for every \(j,k\in\{0,1\}\), the directed triangle
\[
a_0\to b_j\to c_k\to a_0.
\]

Its symmetric graph is \(3K_2\), hence nonempty and bipartite. Every 2-dicolouring would have to split each of the three digons. The colour class containing \(a_0\) also contains one \(b_j\) and one \(c_k\), and those three vertices form a directed triangle. Thus the digraph is not 2-dicolourable.

On the other hand:

- each side of each individual component of \(B(F)\) is a singleton, so Theorem 3 does not apply;
- every coherent bipartition has a side containing one of the displayed directed triangles, so Theorem 5 does not apply.

This example is only meant to show that the first two sufficient conditions are not forced by the residual assumptions. Proposition 6 may settle particular targets after their circular core and orbit structure are determined.

The genuinely untreated configuration is therefore one where:

1. \(B(F)\) is disconnected and bipartite;
2. every individual component-side induces an acyclic digraph;
3. every coherent bipartition of the non-isolated support has a monochromatic directed triangle on at least one side; and
4. no cyclic digon-free circular-core orbit is available for the pinning reduction.

The obstruction is that a connected source digon scaffold forces all its vertices into one target component and fixes their relative bipartition parity. Allowing vertices to choose different target components permits a monochromatic source clause to map onto a directed triangle spread across those components. I do not have a gadget excluding this behavior in full generality.

---

## 7. Fully specified computational formulation

For small fixed targets, circular maps can be tested exactly as follows.

Introduce variables \(x_{v,a}\) for \(v\in V(D)\), \(a\in V(F)\), with exactly one \(x_{v,a}\) true for each \(v\). For every simple directed cycle \(Z\) of \(D\) and every acyclic subset \(A\subseteq V(F)\), impose
\[
\bigvee_{v\in V(Z)}\ \bigvee_{a\notin A} x_{v,a}.
\]
These clauses say that no source directed cycle has all its images in an acyclic target set. By Lemma 1, the resulting SAT instance is satisfiable exactly when \(D\to_\circ F\).

The same formulation with \(D=F\) enumerates circular endomorphisms and hence permits exact computation of circular cores and their circular-automorphism orbits. I have not run or claimed any enumeration here.

## Conclusion

The conjecture remains unresolved in full. The main concrete advance is Corollary 4: the entire residual case with connected bipartite symmetric part is NP-complete. Theorems 3 and 5 and Proposition 6 also settle additional disconnected families, but a distributed-triangle case remains.