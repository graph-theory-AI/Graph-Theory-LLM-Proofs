```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for k >= 4 and for additional broad classes of 3-uniform hypergraphs, leaving a specific five-vertex case and general mixed-twin cases unresolved.",
  "would_publish": false,
  "caveats": "Uses the intended H-free formulation and nonempty, vertex-locally finite perturbations; the full k=3 conjecture remains unresolved here."
}
```

# Partial resolution

I use the intended, nontrivial formulation from the supplied abstract:

> Find a countably infinite **induced-\(H\)-free** \(k\)-uniform hypergraph \(G\) such that \(G\triangle D\) contains an induced \(H\) whenever \(D\) is a nonempty family of \(k\)-sets and every vertex belongs to only finitely many members of \(D\).

The catalog’s displayed statement omits \(H\)-freeness and the exclusion of the empty perturbation. The argument below addresses the stronger intended formulation.

I checked the complete-shadow argument and the four-vertex construction in the supplied attempt; both are valid under this definition of local finiteness. The principal additional result is a rooted-amalgamation construction that handles many more 3-uniform hypergraphs.

## 1. Results obtained

For a 3-uniform hypergraph, call two vertices \(u,v\):

- **0-twins** if every triple containing both is a nonedge, and
  \[
  ux y\in E(H)\iff vx y\in E(H)
  \]
  for every pair \(x,y\notin\{u,v\}\);
- **1-twins** if every triple containing both is an edge, and the same equivalence holds.

Thus their transposition is an automorphism, with their common-pair triples uniformly absent or uniformly present.

The following cases of the conjecture are proved below.

### Theorem
Let \(H\) be a finite \(k\)-uniform hypergraph with an edge and a nonedge. The conjecture holds in each of the following cases.

1. **Every \(k\geq4\).**
2. **\(k=3\), and either \(H\) or \(\overline H\) has complete 2-shadow.**
3. **\(k=3\), \(|V(H)|\geq6\), and \(H\) does not have both a pair of 0-twins and a pair of 1-twins.**
4. **\(k=3\), \(|V(H)|\leq5\), except possibly the following five-vertex hypergraph and its complement:**
   \[
   V(C)=\{a,b,c,d,x\},\qquad
   E(C)=\{acd,bcd,cdx,acx\}.
   \]
   Here \(C\) is the cone over a triangle with a pendant edge.
5. **The pair-stars and their complements:** for every \(m\geq2\), the hypergraph
   \[
   V(S_m)=\{u,v,z_1,\ldots,z_m\},\qquad
   E(S_m)=\{uvz_i:1\leq i\leq m\}.
   \]

In particular, compared with the supplied attempt, the unresolved five-vertex class is reduced to two complementary examples. For orders at least six, any remaining example must have both kinds of twins, apart from additional families already covered by item 5.

These are partial results, not a proof of the full conjecture.

---

## 2. A rooted-witness construction

The following elementary device replaces the need for a homogeneous universal hypergraph.

### Lemma 2.1 — Rooted witnesses
Let \(H\) have \(n>k\) vertices. Suppose that, for each \(t\in\{0,1\}\), there is an \(H\)-free countable \(k\)-graph \(W_t\) with:

- a distinguished root \(Q_t\) of size \(k\), of edge status \(t\);
- a partition
  \[
  V(W_t)\setminus Q_t=P_1\sqcup\cdots\sqcup P_{n-k}
  \]
  into infinite parts;
- a \(k\)-set \(q_t\subseteq V(H)\), of status \(1-t\) in \(H\), such that every transversal
  \[
  Q_t\cup\{p_1,\ldots,p_{n-k}\},\qquad p_i\in P_i,
  \]
  induces \(H\triangle\{q_t\}\), with \(q_t\) corresponding to \(Q_t\).

Suppose also that whenever \(A\) is a countable \(H\)-free \(k\)-graph and \(e\in[V(A)]^k\) has status \(t\), one can amalgamate \(A\) and a fresh copy of \(W_t\) over \(e=Q_t\), preserving both as induced subhypergraphs and keeping the amalgam \(H\)-free.

Then the conjecture holds for \(H\).

#### Proof

Start with a countably infinite empty hypergraph. Repeatedly attach the appropriate rooted witness over every \(k\)-set.

More explicitly, in each round enumerate all \(k\)-sets of the hypergraph present at the beginning of that round and attach one witness over each, using fresh vertices outside its root. Take the union, and repeat for countably many rounds. The resulting hypergraph \(G\) is countable and infinite. Every finite set of vertices occurs at some stage, so every \(k\)-set eventually receives a witness. Every stage, and hence \(G\), is \(H\)-free.

Let \(D\neq\varnothing\) be vertex-locally finite, and choose \(e\in D\). Consider the witness attached over \(e\).

Choose its transversal one vertex at a time. If the currently selected set is \(S\), define
\[
F_D(S)=\bigcup\{d\in D:d\cap S\neq\varnothing\}.
\]
This set is finite. Choose the next vertex from its required infinite part outside \(F_D(S)\cup S\).

No newly contained member of \(D\) can use this new vertex: such a changed \(k\)-set would also meet \(S\), placing the new vertex in \(F_D(S)\). Consequently, the completed transversal \(T\) satisfies
\[
D\cap[T]^k=\{e\}.
\]
Before perturbation it induces \(H\triangle\{q_t\}\); afterwards it induces \(H\). ∎

Complementation preserves the required property, since
\[
\overline{G\triangle D}=\overline G\triangle D.
\]

### Free and cofree amalgamation

For hypergraphs \(A,B\) with common induced subhypergraph \(R\):

- their **free amalgam** adds no hyperedge meeting both \(A\setminus R\) and \(B\setminus R\);
- their **cofree amalgam** declares every \(k\)-set meeting both exclusive sides to be an edge.

A useful observation is:

> In an induced copy of \(H\) spanning a free amalgam, every pair represented on opposite exclusive sides is a null pair of \(H\). In a cofree amalgam, every such pair is a full pair of \(H\).

Here a null pair lies in no edge, while a full pair lies in no nonedge.

---

## 3. Blowups and complete shadows

Given a finite \(k\)-graph \(B\), its **0-blowup** replaces each vertex by a part and declares a \(k\)-set to be an edge exactly when it meets \(k\) distinct parts whose labels form an edge of \(B\). Thus every \(k\)-set repeating a part is a nonedge.

The **1-blowup** instead declares every \(k\)-set repeating a part to be an edge, while retaining \(B\)'s statuses on transversals.

Parts may be singletons. For rooted witnesses, the root parts will be singletons and all other parts infinite.

### Lemma 3.1
The following hold.

1. If the 2-shadow of \(H\) is complete, a 0-blowup of an \(H\)-free \(B\) is \(H\)-free.
2. For 3-uniform \(H\), if \(H\) has no 0-twins, a 0-blowup of an \(H\)-free \(B\) is \(H\)-free.
3. For 3-uniform \(H\), if \(H\) has no 1-twins, a 1-blowup of an \(H\)-free \(B\) is \(H\)-free.

#### Proof

For item 1, two vertices of a putative induced \(H\) cannot lie in one part: that pair would lie in no edge of the copy, contradicting the complete 2-shadow. The projection onto \(B\) would therefore be an induced embedding.

For item 2, two vertices of a putative copy lying in the same part would be 0-twins in that copy. Again, the projection must be injective.

Item 3 is the complementary argument. ∎

### Proposition 3.2 — Complete-shadow case
If either \(H\) or \(\overline H\) has complete 2-shadow, the conjecture holds for \(H\).

#### Proof

Suppose first that \(H\) has complete 2-shadow. Free amalgamation preserves induced-\(H\)-freeness: a spanning copy would have a null pair represented on opposite sides.

To construct \(W_0\), choose an edge \(q_0\) of \(H\), put
\[
B_0=H-q_0,
\]
and take its 0-blowup with the vertices of \(q_0\) singleton and all other parts infinite.

For \(W_1\), choose a nonedge \(q_1\) and use the analogous rooted 0-blowup of
\[
B_1=H+q_1.
\]

Both \(B_0\) and \(B_1\) are \(H\)-free: they have \(n\) vertices and respectively one fewer or one more edge than \(H\). Their blowups are \(H\)-free by Lemma 3.1. They satisfy Lemma 2.1, using free amalgamation.

The complementary case follows by complementation. ∎

### Corollary 3.3 — Every \(k\geq4\)

If neither \(H\) nor \(\overline H\) had complete 2-shadow, \(H\) would have a null pair \(P\) and a full pair \(Q\). For \(k\geq4\),
\[
|P\cup Q|\leq4\leq k.
\]
There is therefore a \(k\)-set \(T\subseteq V(H)\) containing both pairs. It would have to be simultaneously a nonedge and an edge.

Thus one of the two shadows is complete, proving the conjecture for every \(k\geq4\). ∎

For \(k=3\), the same observation shows that a null pair and a full pair must be disjoint.

---

## 4. The new general result for 3-graphs of order at least six

For a 3-graph \(H\), define
\[
Z(H)=\{v:v\text{ belongs to a null pair of }H\},
\]
\[
O(H)=\{v:v\text{ belongs to a full pair of }H\}.
\]

These sets are disjoint. Indeed, if \(uv\) were null and \(vw\) full, the triple \(uvw\) would have conflicting statuses.

### Lemma 4.1 — Amalgamation over triples
Let \(H\) have \(n\) vertices.

1. If \(|Z(H)|\leq n-4\), free amalgamation over a triple preserves induced-\(H\)-freeness.
2. If \(|O(H)|\leq n-4\), cofree amalgamation over a triple preserves induced-\(H\)-freeness.
3. If \(n=6\) and \(Z(H),O(H)\) partition \(V(H)\) into two three-element sets, then:
   - free amalgamation over a **nonedge** preserves induced-\(H\)-freeness;
   - cofree amalgamation over an **edge** preserves induced-\(H\)-freeness.

#### Proof

In a spanning copy in a free amalgam, every vertex represented outside the intersection has an opposite-side partner forming a null pair. Thus every vertex of \(V(H)\setminus Z(H)\) must be represented in the intersection.

If \(|Z(H)|\leq n-4\), this requires at least four vertices in an intersection of size three. This proves item 1. Item 2 is complementary.

For item 3, a spanning copy in a free amalgam must place all three vertices of \(O(H)\) in the root. But \(H[O(H)]\) is an edge, because \(O(H)\) contains a full pair. It cannot be identified with a nonedge root.

Similarly, a spanning copy in a cofree amalgam must place \(Z(H)\) in the root. Its triple is a nonedge, because it contains a null pair. It cannot be identified with an edge root. ∎

### Theorem 4.2
If \(H\) is a 3-graph on \(n\geq6\) vertices and has no 0-twins or has no 1-twins, the conjecture holds for \(H\).

#### Proof

Choose \(c\in\{0,1\}\) such that \(H\) has no \(c\)-twins. Construct rooted witnesses for both root statuses using \(c\)-blowups of \(H-q\) and \(H+q\), as in Proposition 3.2. They are \(H\)-free by Lemma 3.1.

It remains to justify their attachment.

If \(n\geq7\), disjointness of \(Z(H)\) and \(O(H)\) gives
\[
\min\{|Z(H)|,|O(H)|\}
 \leq \lfloor n/2\rfloor
 \leq n-4.
\]
Thus one of free or cofree amalgamation over every triple is available.

For \(n=6\), the same conclusion holds if one of the two sets has size at most two. Otherwise both have size three and partition \(V(H)\). In that case use free amalgamation for nonedge roots and cofree amalgamation for edge roots, by Lemma 4.1.

Lemma 2.1 now applies. ∎

This proof is independent of the graph-case theorem from the source paper.

---

## 5. Pair-stars

The preceding blowup argument does not handle hypergraphs with both kinds of twins. Pair-stars give an infinite family in that residual class for which suitable witnesses can nevertheless be constructed.

Recall
\[
E(S_m)=\{uvz_i:1\leq i\leq m\}.
\]

We first handle \(m\geq3\).

### 5.1. A witness for adding a nonedge

Take root
\[
Q_0=\{u,v,z\},
\]
with \(z\) isolated. Let \(C_1,\ldots,C_{m-1}\) be disjoint countably infinite sets.

Make each
\[
\{u,v\}\cup C_i
\]
a complete 3-graph, and add no other edges. Call the result \(W_0\).

Every choice of one vertex \(w_i\in C_i\) gives, together with the root, an induced \(S_m\) missing the edge \(uvz\).

Moreover, \(W_0\) is \(S_m\)-free. To see this, consider the core pair of a putative \(S_m\).

- If the core pair is \(\{u,v\}\), its leaves must lie in distinct \(C_i\)'s, since two leaves in one \(C_i\) create an unwanted edge with \(u\). There are only \(m-1\) parts.
- Otherwise, any edges containing that core pair lie in a single complete block \(\{u,v\}\cup C_i\). Two leaves then already create an unwanted edge with one core vertex.

Thus no induced \(S_m\) exists.

### 5.2. A witness for deleting an edge

Take root
\[
Q_1=\{u,x,y\}.
\]
Let \(D,C_1,\ldots,C_{m-2}\) be disjoint infinite sets.

Define a graph \(L\) on
\[
D\cup\{x,y\}\cup C_1\cup\cdots\cup C_{m-2}
\]
as follows:

- \(D\) is a clique and is joined completely to all other vertices;
- each \(C_i\) and \(\{x,y\}\) is a clique;
- there are no edges between distinct members of the collection
  \[
  \{x,y\},C_1,\ldots,C_{m-2}.
  \]

Let \(W_1\) be the 3-uniform cone over \(L\), with apex \(u\):
\[
uab\in E(W_1)\iff ab\in E(L),
\]
and no triples avoiding \(u\) are edges.

Choose \(d\in D\) and \(c_i\in C_i\). On
\[
\{u,d,x,y,c_1,\ldots,c_{m-2}\}
\]
the edges are exactly those of \(S_m\), with core \(\{u,d\}\), together with the extra edge \(uxy\).

The hypergraph \(W_1\) is \(S_m\)-free. Any induced \(S_m\) in a cone must use the apex as one of its two core vertices. It would therefore give an induced \(K_{1,m}\) in \(L\). But:

- a vertex of \(D\) has no independent \(m\)-set in its neighborhood: at most one vertex can be taken from each of the \(m-1\) peripheral cliques;
- a vertex outside \(D\) has a clique as its neighborhood.

Hence \(L\) is induced-\(K_{1,m}\)-free.

### 5.3. Attaching these witnesses

Use cofree amalgamation over the root.

In \(S_m\), all \(m\) leaves belong to null pairs. Consequently, a spanning induced \(S_m\) in a cofree amalgam must place every leaf in the intersection.

For \(m\geq4\), this is impossible over a three-vertex root.

For \(m=3\):

- an edge root cannot represent the independent triple of leaves, so attachment of \(W_1\) is safe;
- for attachment of \(W_0\), a spanning \(S_3\) would have the root as its three leaves and one core vertex on each exclusive side. Its new-side core vertex would form no edge with any pair of root vertices. But every new vertex of \(W_0\) forms an edge with the root pair \(\{u,v\}\).

Thus both attachments are safe also for \(m=3\).

Lemma 2.1 proves the conjecture for every \(S_m\), \(m\geq3\), and complementation gives the complementary family.

---

## 6. The four-vertex two-edge hypergraph

The remaining pair-star \(S_2\) is the unique four-vertex 3-graph \(F\) with exactly two edges.

Let
\[
V=\{x\in\{0,1\}^{\mathbb N}:x\text{ has finite support}\}.
\]
For distinct \(x,y,z\), let
\[
\ell(x,y,z)=\min\{i:x_i,y_i,z_i\text{ are not all equal}\}.
\]
Declare \(xyz\) an edge exactly when \(\ell(x,y,z)\) is odd.

### \(F\)-freeness

Given four vertices, consider their first nonconstant coordinate.

- For a \(2+2\) split, all four triples have the same status.
- For a \(1+3\) split, the three triples containing the singleton have the same status, while the remaining triple is arbitrary.

The four-set therefore has \(0,1,3\), or \(4\) edges, never two.

### Robustness

Let \(D\neq\varnothing\) be locally finite, and choose a changed triple \(e=\{a,b,c\}\). Put \(n=\ell(a,b,c)\), with \(a,b\) the majority pair at coordinate \(n\).

There are infinitely many \(w\in V\) such that
\[
\ell(a,b,w)=n+1,
\qquad
\ell(a,c,w)=\ell(b,c,w)=n.
\]
Indeed, prescribe the common prefix through coordinate \(n-1\), give \(w\) the majority bit at \(n\), and arrange a split among \(a,b,w\) at \(n+1\). Infinitely many finite-support tails remain available.

On \(\{a,b,c,w\}\), three triples, including \(e\), have status \(n\bmod2\), and the fourth has the opposite status. Toggling \(e\) changes its edge count from one to two, or from three to two.

Only finitely many candidate \(w\)'s occur in changed triples meeting \(\{a,b,c\}\). Choose an unspoiled one. Then \(e\) is the only changed triple on the four-set, which becomes an induced \(F\).

This also completes the pair-star family and, together with Proposition 3.2, settles every mixed 3-graph on four vertices.

---

## 7. Five vertices: all but one complementary pair

Suppose a five-vertex 3-graph has both a null pair and a full pair. Label them \(ab\) and \(cd\), with remaining vertex \(x\).

Six triple statuses are forced:
\[
abc=abd=abx=0,\qquad
acd=bcd=cdx=1.
\]
The other four are recorded by
\[
M=
\begin{pmatrix}
acx&adx\\
bcx&bdx
\end{pmatrix}.
\]

Up to swapping rows, swapping columns, isomorphism, and complementation, the possibilities are:

1. \(M\) has no ones: \(S_3\);
2. \(M\) has one one:
   \[
   E(C)=\{acd,bcd,cdx,acx\};
   \]
3. \(M\) has two ones in one row:
   \[
   E(R)=\{acd,bcd,cdx,acx,adx\};
   \]
4. \(M\) has two diagonal ones:
   \[
   E(T)=\{acd,bcd,cdx,acx,bdx\}.
   \]

The zero-one count handles the other possibilities: three or four ones reduce by complementation, and a full column is complementary, up to relabelling, to a full row.

The pair-star case was settled above. I now settle \(R\) and \(T\).

### Lemma 7.1
The conjecture holds for \(R\) and \(T\).

#### Proof

Directly from their displayed edge sets:

| Hypergraph | Null pairs | Full pairs |
|---|---|---|
| \(R\) | \(ab,bx\) | \(cd\) |
| \(T\) | \(ab\) | \(cd\) |

Neither hypergraph has 0-twins. For example, \(a,b\) are distinguished by the pair \(c,x\); in \(R\), \(b,x\) are distinguished by \(a,c\).

Thus 0-blowups of their \(H\)-free finite subtemplates are \(H\)-free.

Use cofree amalgamation. Since the only full pair is \(cd\), any spanning induced \(H\), for \(H\in\{R,T\}\), must have exactly one exclusive vertex on each side, corresponding to \(c,d\). Its other three vertices, \(a,b,x\), must be the whole root.

Two features follow:

1. the root must be a nonedge;
2. each exclusive vertex must form exactly one edge with the three pairs of root vertices.

The second assertion follows by inspecting the links of \(c,d\) on \(\{a,b,x\}\).

Consequently, attachment over an edge root is always safe. For this root status, use a rooted 0-blowup of \(H+q\), for any nonedge \(q\).

For nonedge roots, choose the following witnesses:

| \(H\) | Removed edge \(q\) | Vertices outside \(q\) | Number of edges each forms with root pairs |
|---|---|---|---|
| \(R\) | \(acx\) | \(b,d\) | \(0,3\) |
| \(T\) | \(cdx\) | \(a,b\) | \(2,2\) |

Take the rooted 0-blowup of \(H-q\). Every new vertex retains the listed root profile, so no new vertex forms exactly one edge with root pairs. A spanning induced \(H\) in the cofree amalgam is therefore impossible.

These are the witnesses and safe attachments required by Lemma 2.1. ∎

If a five-vertex \(H\) has no null pair or no full pair, Proposition 3.2 already applies. The classification above therefore proves:

### Corollary 7.2
Every mixed five-vertex 3-graph satisfies the conjecture, except possibly
\[
E(C)=\{acd,bcd,cdx,acx\}
\]
and its complement.

No claim is made here that either exceptional hypergraph is a counterexample.

---

## 8. What remains unresolved

The arguments establish the full conjecture for every uniformity \(k\geq4\).

For \(k=3\), the unresolved cases after these results are confined to:

- the specific five-vertex hypergraph
  \[
  E(C)=\{acd,bcd,cdx,acx\}
  \]
  and its complement;
- hypergraphs on at least six vertices having **both** a pair of 0-twins and a pair of 1-twins, excluding families such as the pair-stars and their complements already handled above.

There are two distinct limitations.

First, the order-at-least-six amalgamation argument does not cover the five-vertex \(C\), even though \(C\) has neither kind of twin. Its null/full pair structure permits spanning copies over small roots in both amalgamation directions.

Second, if \(H\) has both kinds of twins, neither uniform blowup operation is automatically safe: a copy of \(H\) can use multiple vertices from a single part. The pair-star constructions overcome this through specially designed rooted witnesses, but no construction for arbitrary mixed-twin \(H\) is supplied.

Accordingly, this is a rigorous enlargement of the partial resolution, not a proof of the remaining ternary conjecture.