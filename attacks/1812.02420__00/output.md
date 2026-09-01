```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the intended loopless convention, NP-completeness follows for every cyclic target with connected symmetric part and for every two-clone blow-up of a digon-free circular core, including an infinite family outside all cases listed in Theorem 2.17.",
  "would_publish": false,
  "caveats": "The general case with disconnected bipartite symmetric part remains open; the proof uses the digon-free case of Theorem 2.17 and the known NP-completeness of 2-dicolourability."
}
```

# Circular \(F\)-colourability

Throughout, digraphs are finite and loopless, as is standard in the source. Parallel arcs do not affect the arguments.

Write \(D\to_\circ F\) if there is a circular homomorphism \(f:V(D)\to V(F)\), meaning that \(f^{-1}(A)\) induces an acyclic subdigraph of \(D\) whenever \(A\) induces an acyclic subdigraph of \(F\).

The conjectured dichotomy is:

- if \(F\) is acyclic, deciding \(D\to_\circ F\) is polynomial;
- if \(F\) contains a directed cycle, deciding \(D\to_\circ F\) is NP-complete.

I prove two additional NP-complete classes, both containing targets not covered by the three cases quoted from Theorem 2.17.

## 1. Preliminary facts

### Cycle criterion

A map \(f:V(D)\to V(F)\) is circular if and only if

\[
  F[f(V(C))]
\quad\text{contains a directed cycle for every directed cycle }C\subseteq D.
  \tag{1}
\]

Indeed, if \(f(V(C))\) is acyclic, then \(C\subseteq f^{-1}(f(V(C)))\), contradicting circularity. Conversely, if \(f^{-1}(A)\) is cyclic for some acyclic \(A\subseteq V(F)\), a directed cycle in \(D[f^{-1}(A)]\) violates (1).

Circular homomorphisms compose.

For fixed \(F\), the problem belongs to NP: after guessing \(f\), enumerate the constantly many acyclic subsets \(A\subseteq V(F)\) and test whether each \(D[f^{-1}(A)]\) is acyclic.

If \(F\) is acyclic and nonempty, then \(D\to_\circ F\) if and only if \(D\) is acyclic. Thus the acyclic side of the proposed dichotomy is polynomial.

### Symmetric part

Let \(S(F)\) be the undirected graph on \(V(F)\) in which \(xy\) is an edge exactly when both \(x\to y\) and \(y\to x\) are arcs of \(F\).

By (1), a source digon must map bijectively to a digon of \(F\). Consequently, the restriction of a circular map to a bidirected source graph is an ordinary graph homomorphism into \(S(F)\).

I use the following established part of Theorem 2.17 from the source:

> If \(H\) is a fixed digon-free digraph containing a directed cycle, then deciding \(D\to_\circ H\) is NP-complete.

## 2. Forcing a shore of a symmetric component

### Theorem 1

Let \(F\) be a fixed loopless digraph whose symmetric part \(S(F)\) is bipartite. For each nontrivial connected component \(K\) of \(S(F)\), fix its bipartition
\[
V(K)=X_K\mathbin{\dot\cup}Y_K.
\]
If at least one digraph among
\[
\mathcal H(F)=\{F[X_K],F[Y_K]: K\text{ a nontrivial component of }S(F)\}
\]
contains a directed cycle, then deciding \(D\to_\circ F\) is NP-complete.

### Proof

Each member of \(\mathcal H(F)\) is digon-free, since a bipartition shore is independent in \(S(F)\).

Order the cyclic members of \(\mathcal H(F)\) by circular homomorphism:
\[
H\preceq H' \quad\Longleftrightarrow\quad H\to_\circ H'.
\]
After identifying mutually homomorphic members, choose a maximal cyclic member \(H_0\).

Choose an even integer \(L\), depending only on \(F\), such that in every nontrivial component \(K\) of \(S(F)\), every two vertices in the same shore are joined by a walk of length exactly \(L\). Such an \(L\) exists: take an even integer at least every relevant distance and extend shorter walks by backtracking along an edge.

Given an instance \(D\) of circular \(H_0\)-colourability, first form the disjoint union
\[
G=D\mathbin{\dot\cup}H_0.
\]
Add a new vertex \(r\). For every \(x\in V(G)\), add an internally disjoint path of length \(L\) from \(r\) to \(x\), and replace every path edge by a digon. Call the resulting digraph \(B(D)\).

I claim
\[
B(D)\to_\circ F
\quad\Longleftrightarrow\quad
D\to_\circ H_0.
\tag{2}
\]

#### Forward implication

Let \(f:B(D)\to_\circ F\). Every digon in the added scaffold maps to an edge of \(S(F)\). Since the scaffold is connected, its image lies in one connected component \(K\) of \(S(F)\).

Every vertex of \(G\) is at even distance \(L\) from \(r\). Hence all vertices of \(G\) map into one shore, say \(X_K\). Thus
\[
f|_{V(G)}:G\to_\circ F[X_K].
\]
In particular,
\[
H_0\to_\circ F[X_K].
\]
A cyclic digraph cannot map circularly to an acyclic digraph, so \(F[X_K]\) is cyclic. Maximality of \(H_0\) now gives
\[
F[X_K]\to_\circ H_0.
\]
Composing the restriction \(D\to_\circ F[X_K]\) with this map yields \(D\to_\circ H_0\).

#### Reverse implication

Suppose \(g:D\to_\circ H_0\). Extend \(g\) to
\[
G=D\mathbin{\dot\cup}H_0\to_\circ H_0
\]
by using the identity on the fixed copy of \(H_0\).

Write \(H_0=F[X_{K_0}]\), and choose any \(a\in X_{K_0}\) as the image of \(r\). For every \(x\in V(G)\), the choice of \(L\) gives a length-\(L\) walk in \(S(F)\) from \(a\) to \(g(x)\). Use this walk to colour the corresponding bidirected path.

Every directed cycle of \(B(D)\) is of one of two kinds:

1. it lies entirely in \(G\), in which case its image is cyclic because \(g\) is circular; or
2. it uses an arc of the bidirected scaffold, in which case its image contains the target digon formed by the images of the endpoints of that scaffold edge.

Thus the extension is circular, proving (2).

Since \(H_0\) is cyclic and digon-free, circular \(H_0\)-colourability is NP-hard by Theorem 2.17. The construction is linear-size because \(F,L,H_0\) are fixed. Membership in NP proves NP-completeness. ∎

### Consequence: connected symmetric part

If \(S(F)\) is connected and bipartite, with shores \(X,Y\), and both \(F[X]\) and \(F[Y]\) are acyclic, then \(X,Y\) form a 2-dicolouring of \(F\).

Consequently:

### Corollary 2

The conjectured NP-completeness statement holds for every loopless cyclic \(F\) whose symmetric part is connected.

Indeed:

- if \(S(F)\) is non-bipartite, this is already Theorem 2.17;
- if \(F\) is 2-dicolourable, this is already Theorem 2.17;
- otherwise \(S(F)\) is connected and bipartite but one shore is cyclic, so Theorem 1 applies.

This genuinely extends the listed cases. For example, let
\[
V(F)=\{x_1,x_2,x_3,y\},
\]
put a digon between \(y\) and every \(x_i\), and put a directed triangle
\[
x_1\to x_2\to x_3\to x_1.
\]
Then \(S(F)=K_{1,3}\), so it is bipartite and connected. The target has digons and is not 2-dicolourable: every 2-dicolouring must put the three \(x_i\) opposite \(y\), making their directed triangle monochromatic. Thus none of the three previously listed cases applies, while Theorem 1 proves NP-completeness.

## 3. A residual family with disconnected symmetric part

The preceding shore argument does not apply when every shore of every individual symmetric component is acyclic. The following theorem nevertheless settles a broad infinite family of such targets.

### Two-clone blow-up

For a loopless digraph \(H\), define \(\widehat H\) as follows:
\[
V(\widehat H)=V(H)\times\{0,1\}.
\]
For every \(x\in V(H)\), put a digon between \((x,0)\) and \((x,1)\). For every arc \(x\to y\) of \(H\), put all four arcs
\[
(x,i)\to(y,j),\qquad i,j\in\{0,1\}.
\]

Call \(\{(x,0),(x,1)\}\) the fibre above \(x\).

A digraph \(H\) is a circular core if every circular endomorphism \(H\to_\circ H\) is bijective.

### Lemma 3

Suppose \(H\) is digon-free. A set \(U\subseteq V(\widehat H)\) is cyclic if and only if at least one of the following holds:

1. \(U\) contains both vertices of some fibre;
2. the projection
   \[
   \pi(U)=\{x:(x,i)\in U\text{ for some }i\}
   \]
   induces a cyclic subdigraph of \(H\).

#### Proof

The first condition gives a digon. If no fibre is fully contained in \(U\), the projection is injective on \(U\), and \(\widehat H[U]\) is isomorphic to \(H[\pi(U)]\). ∎

### Lemma 4

If \(H\) is digon-free and \(\varphi:\widehat H\to_\circ\widehat H\), then \(\varphi\) induces a circular endomorphism \(g:H\to_\circ H\) on the fibres.

#### Proof

Because the symmetric part of \(\widehat H\) is a matching, every source fibre digon maps bijectively onto one target fibre. Define \(g(x)\) to be the target fibre receiving the fibre above \(x\).

Let \(C\) be a directed cycle of \(H\). For every \(x\in V(C)\), choose the unique clone above \(x\) which \(\varphi\) sends to the \(0\)-clone of the fibre above \(g(x)\). The chosen source clones contain a directed cycle in \(\widehat H\). Their image contains at most one clone from each target fibre. Circularity of \(\varphi\), together with Lemma 3, therefore implies that \(H[g(V(C))]\) is cyclic. Thus \(g\) is circular. ∎

### Theorem 5

Let \(H\) be a fixed nonempty digon-free circular core. Then deciding
\[
D\to_\circ\widehat H
\]
is NP-complete.

In particular, if \(H\) is cyclic, then \(\widehat H\) belongs to the previously unresolved class: its symmetric part is a disjoint union of edges, and it is not 2-dicolourable.

### Proof

Reduce from the known NP-complete problem of deciding whether \(D\) is 2-dicolourable.

Fix \(p\in V(H)\). Construct \(T(D)\) as follows.

Take one common copy of all fibres of \(\widehat H\) above \(V(H)\setminus\{p\}\); call this common part the anchor. For each \(v\in V(D)\), add a private pair
\[
p_v^0,p_v^1
\]
and all arcs needed so that the anchor together with this pair is a copy \(\widehat H_v\) of \(\widehat H\), with \(p_v^0,p_v^1\) as the fibre above \(p\).

Finally, for each arc \(u\to v\) of \(D\), add
\[
p_u^0\to p_v^0.
\]

We prove
\[
T(D)\to_\circ\widehat H
\quad\Longleftrightarrow\quad
D\text{ is 2-dicolourable}.
\tag{3}
\]

#### Forward implication

Let \(\varphi:T(D)\to_\circ\widehat H\). Its restriction to each \(\widehat H_v\) is a circular endomorphism of \(\widehat H\). By Lemma 4, it induces a circular endomorphism
\[
g_v:H\to_\circ H.
\]
Since \(H\) is a circular core, every \(g_v\) is a permutation.

All copies agree pointwise on the anchor. Hence the permutations \(g_v\) agree on every element of \(V(H)\setminus\{p\}\). As they are permutations, all \(g_v(p)\) equal the same remaining vertex \(q\in V(H)\).

It follows that every distinguished vertex \(p_v^0\) maps to one of the two clones in the fibre above \(q\). Use those two target vertices as colours \(0,1\) of \(v\).

If \(C\) were a monochromatic directed cycle of \(D\), the corresponding cycle on the vertices \(p_v^0\) would have image contained in one target vertex. This is acyclic, contradicting circularity. Thus the two colour classes are acyclic, and \(D\) is 2-dicolourable.

#### Reverse implication

Let \(c:V(D)\to\{0,1\}\) be a 2-dicolouring. Map every anchor clone identically, and set
\[
p_v^0\longmapsto (p,c(v)),\qquad
p_v^1\longmapsto (p,1-c(v)).
\tag{4}
\]
On every copy \(\widehat H_v\), this is the identity except possibly for swapping the two clones above \(p\). Since the two clones of a fibre have identical external in- and out-neighbourhoods, it is a digraph automorphism of that copy.

Consider a directed cycle \(C\) of \(T(D)\).

- If \(C\) contains both vertices of any anchor or private fibre, its image contains a target digon.
- Otherwise, \(C\) uses at most one vertex from each fibre. Every gadget arc between distinct fibres projects to an arc of \(H\), while every added \(D\)-arc projects to a stationary step \(p\to p\).

If \(C\) uses at least one gadget arc between distinct fibres, delete the stationary \(p\to p\) steps from its projected type sequence. The result is a nonempty directed closed walk in \(H\), whose vertex set contains a directed cycle. The image of \(C\) is therefore cyclic by Lemma 3.

If \(C\) uses no such gadget arc, then—because it uses no complete fibre—it consists entirely of the distinguished vertices \(p_v^0\) and added arcs corresponding to a directed cycle of \(D\). Since \(c\) is a 2-dicolouring, this cycle contains both colours. Its image under (4) therefore contains the target digon above \(p\).

Thus every directed cycle has cyclic image, and the map is circular. This proves (3), and hence NP-hardness. Membership in NP completes the proof. ∎

### A concrete infinite residual family

Take \(H=\vec C_q\), the chordless directed \(q\)-cycle, for any \(q\ge 3\). It is a circular core: the image of its directed cycle under a circular endomorphism must contain all \(q\) vertices, so the endomorphism is surjective and hence bijective.

The target
\[
F_q=\widehat{\vec C_q}
\]
has \(q\) disjoint digons as its symmetric part, with all arcs from fibre \(i\) to fibre \(i+1\pmod q\). It satisfies:

- \(S(F_q)=qK_2\), nonempty and bipartite;
- \(F_q\) has digons;
- \(F_q\) is not 2-dicolourable;
- every shore of every symmetric component is a singleton, so Theorem 1 does not apply.

Thus \(F_q\) lies squarely in the residual class identified by the catalog, and Theorem 5 proves circular \(F_q\)-colourability NP-complete for every \(q\ge3\).

To verify non-2-dicolourability directly, every digon fibre must be split between the two colours. Each colour class consequently contains one vertex from every fibre, and those vertices induce a directed \(q\)-cycle.

## 4. What remains open

Combining the source results with Theorem 1, a still-unresolved target may be assumed to satisfy all of the following:

1. \(F\) is loopless and cyclic;
2. \(S(F)\) is nonempty, bipartite, and disconnected;
3. \(F\) is not 2-dicolourable;
4. each individual shore of each nontrivial component of \(S(F)\) is acyclic;
5. \(F\) need not possess the uniform two-clone structure of Theorem 5.

The obstruction is that directed cycles of \(F\) may use vertices from several distinct components of \(S(F)\). A connected bidirected forcing scaffold can synchronize bipartition parity inside one symmetric component, but cannot force colours simultaneously into prescribed shores of several disconnected components.

There is also a useful, but presently insufficient, sandwich. If \(F\) contains a digon and \(m=|V(F)|\), then
\[
\chi_d(D)\le 2
\quad\Longrightarrow\quad
D\to_\circ F
\quad\Longrightarrow\quad
\chi_d(D)\le m.
\]
The first implication maps the two acyclic classes to the endpoints of a target digon. The second follows because each fibre of a circular map is acyclic. Thus a hardness theorem distinguishing \(\chi_d(D)\le2\) from \(\chi_d(D)>m\) would settle every target containing a digon, but no such gap theorem is proved here; ordinary NP-completeness of exact 2-dicolourability alone is not enough.

Finally, if loops are allowed, the blanket conjecture requires amendment: if \(F\) has a looped vertex \(v\), the constant map to \(v\) is circular for every \(D\), since no acyclic subset of \(F\) contains \(v\). Under that convention the problem is trivially all-YES for such a target.