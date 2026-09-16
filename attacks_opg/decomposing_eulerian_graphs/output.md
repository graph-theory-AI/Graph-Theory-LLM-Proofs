```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every graph 3H+2J with H connected Eulerian and J arbitrary, as a consequence of a constructive parity criterion.",
  "would_publish": false,
  "caveats": "Special case only; no improvement of the general connectivity bound, and novelty has not been checked."
}
```

## 1. A sufficient condition

I do not settle the conjecture. I prove below a sufficient condition for multigraphs with no single-edge bundles. It includes a family of genuinely 6-edge-connected instances with arbitrary transition systems.

All graphs below are finite and loopless. As appropriate for the question’s multigraph formulation, two parallel edges may form a cycle of length two. All cycles are vertex-simple apart from their coinciding initial and terminal vertices.

Write
\[
E_{uv}=\{e\in E(G):e\text{ joins }u\text{ and }v\},
\qquad m_{uv}=|E_{uv}|.
\]
Call a nonempty bundle \(E_{uv}\) **blocked** if:

* \(m_{uv}=2\); and
* its two edges form a member of \(P(u)\) or \(P(v)\).

Thus a blocked bundle cannot itself be used as a compatible two-edge cycle.

Let \(B\) be the simple graph of blocked bundles, and let \(A\) be the simple graph of all other nonempty bundles. Both have vertex set \(V(G)\), including isolated vertices.

### Theorem
Let \(G\) be an Eulerian multigraph in which every nonempty bundle has size at least two, and let \(P\) be a 2-transition system. Suppose that, for every vertex set \(X\) of a connected component of \(A\),
\[
|\delta_B(X)|\equiv 0\pmod 2. \tag{1}
\]
Then \((G,P)\) has a compatible cycle decomposition.

Equivalently, after contracting the components of \(A\), the graph of blocked bundles has even degrees.

### Consequences

1. **Minimum multiplicity three.** Every Eulerian multigraph satisfying
   \[
   m_{uv}\ge 3\quad\text{whenever }m_{uv}>0
   \]
   has a compatible decomposition for every 2-transition system. Indeed, \(B\) is empty.

2. **A connected spanning subgraph of large bundles suffices.** Suppose every nonempty bundle has size at least two, and the vertex pairs with multiplicity at least three form a connected spanning graph. Then \(A\) is connected, so (1) is automatic.

3. **Tripled Eulerian graphs with arbitrary doubled edges added.** Let \(H\) be a connected Eulerian loopless multigraph on at least two vertices, and let \(J\) be any loopless multigraph on the same vertex set. Then
   \[
   G=3H+2J
   \]
   has a compatible decomposition for every 2-transition system.

   Here multiplication and addition refer to edge multiplicities. The bundles of multiplicity at least three contain the connected support of \(H\), so consequence 2 applies. Moreover,
   \[
   d_G(v)=3d_H(v)+2d_J(v)
   \]
   is even. Every nontrivial cut of the connected Eulerian graph \(H\) has size at least two, and hence
   \[
   |\delta_G(S)|
      =3|\delta_H(S)|+2|\delta_J(S)|
      \ge 6.
   \]
   Thus these graphs satisfy the hypotheses of the original conjecture.

The proof is self-contained.

## 2. Two elementary lemmas

### Lemma 1: pairing an even bundle

If a parallel-edge bundle has even size \(n\ge4\), its edges can be partitioned into compatible two-edge cycles.

#### Proof

Construct an auxiliary graph \(K\) whose vertices are the edges in the bundle. Two vertices of \(K\) are adjacent when the corresponding edges form a compatible two-edge cycle.

The forbidden pairs at either endpoint of the bundle form a matching. Therefore \(K\) is obtained from \(K_n\) by deleting the union of two matchings.

For \(n=4\), each forbidden matching is contained in one of the three perfect matchings of \(K_4\). At least one of those three perfect matchings consequently avoids both forbidden matchings.

For even \(n\ge6\),
\[
\delta(K)\ge n-3\ge n/2.
\]
Here is a short verification that this guarantees a perfect matching. If a maximum matching \(M\) leaves vertices \(x,y\) unmatched, all their neighbours are matched. Each edge of \(M\) receives at most two adjacencies from \(\{x,y\}\); otherwise there is an augmenting path of length three. Thus
\[
d_K(x)+d_K(y)\le2|M|\le n-2,
\]
contradicting \(d_K(x)+d_K(y)\ge n\).

A perfect matching of \(K\) gives the required partition. \(\square\)

### Lemma 2: doubling an Eulerian graph

If \(F\) is an Eulerian loopless multigraph, then \(2F\) has a compatible decomposition for every 2-transition system on \(2F\).

#### Proof

Fix an ordinary cycle decomposition of \(F\), and treat the doubled copies of each cycle separately.

Let \(C\) be one such cycle. For each edge \(e\in E(C)\), call its two copies a **copy pair**.

If every copy pair is compatible at both endpoints, use all these pairs as two-edge cycles.

Otherwise, some copy pair is forbidden at an endpoint \(v\). We show that the doubled \(C\) can be decomposed into two compatible cycles projecting bijectively onto \(C\).

At a vertex of \(C\), consider the two copy pairs belonging to its two incident cycle edges. There are two possible bijections between these pairs. At least one bijection avoids all forbidden cross-pairs: the forbidden cross-pairs form a matching in \(K_{2,2}\), so they can rule out at most one of its two perfect matchings.

At the chosen vertex \(v\), both bijections are allowed. Indeed, the two edges of the forbidden copy pair are paired with each other in \(P(v)\), so neither can be paired there with an edge of the other copy pair.

Cut \(C\) at \(v\). Label the two copies of its first edge \(0,1\), and propagate these labels along the resulting path, choosing an allowed bijection at every internal vertex. Closing at \(v\) imposes no restriction. The edges labelled \(0\), and those labelled \(1\), give two compatible cycles.

Doing this for every cycle of \(F\) proves the lemma. \(\square\)

## 3. Proof of the theorem

### Step 1: obtain an Eulerian graph of bundles to be doubled

Let
\[
U=\{v:d_B(v)\text{ is odd}\}.
\]
For each component vertex set \(X\) of \(A\), hypothesis (1) gives
\[
|U\cap X|
 \equiv \sum_{v\in X}d_B(v)
 \equiv |\delta_B(X)|
 \equiv0\pmod2.
\]
Consequently there is an edge set \(Q\subseteq E(A)\) with
\[
d_Q(v)\equiv d_B(v)\pmod2
\quad\text{for every }v. \tag{2}
\]

For completeness, \(Q\) can be constructed within a spanning tree of each component of \(A\): root the tree and include a parent–child edge precisely when the child’s subtree contains an odd number of vertices of \(U\). The evenness of \(|U\cap X|\) ensures the required parity also at the root.

Define the simple graph
\[
R=(V(G),\,E(B)\cup Q).
\]
The union is disjoint, and (2) says that \(R\) is Eulerian.

We will reserve exactly two physical edges from each bundle represented in \(R\). Lemma 2 will handle this reserved copy of \(2R\).

### Step 2: choose compatible representatives of odd bundles

Let \(O\) be the simple graph of odd-multiplicity bundles:
\[
E(O)=\{uv:m_{uv}\text{ is odd}\}.
\]
Because \(G\) is Eulerian,
\[
d_O(v)\equiv d_G(v)\equiv0\pmod2.
\]
Fix an ordinary cycle decomposition \(\mathcal D\) of \(O\).

We will choose one representative edge from each odd bundle, so that every cycle of \(\mathcal D\) lifts to a compatible cycle.

The representative lists are as follows.

* If \(m_{uv}\ge5\), every edge of \(E_{uv}\) is a candidate.
* If \(m_{uv}=3\) and \(uv\in Q\), all three edges are candidates.
* If \(m_{uv}=3\) and \(uv\notin Q\), an edge is a candidate precisely when the other two edges form a compatible two-edge cycle.

We need to verify that these lists permit a simultaneous choice.

Consider the last case, and let \(\mathcal F_{uv}\) be the set of distinct forbidden pairs lying entirely inside the three-edge bundle. Each endpoint contributes at most one such pair, so
\[
|\mathcal F_{uv}|\in\{0,1,2\}.
\]
The candidate lists have the following properties:

| Distinct internal forbidden pairs | Number of candidates | Endpoints at which candidates cannot conflict with an outside edge |
|---:|---:|---:|
| \(0\) | \(3\) | \(0\) guaranteed |
| \(1\) | \(2\) | at least \(1\) |
| \(2\) | \(1\) | both |

To justify the last column:

* With one forbidden pair, the candidates are its two members. At an endpoint where this pair is forbidden, both candidates already have their forbidden partner inside the bundle.
* With two distinct forbidden pairs, they occur at different endpoints. Their common edge is the unique candidate, and its forbidden partner lies inside the bundle at both endpoints.

Call an endpoint having the stated property **protected**.

Now process the odd bundles in any order. For the representative being chosen, only its two neighbours in its fixed cycle of \(\mathcal D\) matter. At an unprotected endpoint, an already chosen neighbouring representative excludes at most one candidate, because \(P\) is a 2-transition system. At a protected endpoint it excludes none.

The table shows that the candidate list is larger than the number of potentially excluding endpoints. In the other cases the list has at least three members, while there are only two endpoints. Thus the greedy choice always succeeds.

We have obtained edge-disjoint compatible cycles using exactly one edge from every odd bundle.

### Step 3: pair the remaining edges and reserve \(2R\)

After removing the chosen representatives, every bundle has positive even size.

If its remaining size is at least four, apply Lemma 1. If its support edge belongs to \(R\), reserve one pair from this pairing and use all other pairs as compatible two-edge cycles. If it does not belong to \(R\), use every pair as such a cycle.

It remains to check bundles whose remaining size is two.

* **Original multiplicity two.** If the support edge belongs to \(R\), reserve both edges. Otherwise it is not in \(B\), since \(B\subseteq R\), so the two edges form a compatible cycle.
* **Original multiplicity three.** If its support edge belongs to \(Q\), reserve both remaining edges. Otherwise the definition of its representative list guarantees that these two edges form a compatible cycle.

This covers every case. The reserved edges form exactly two copies of the Eulerian graph \(R\). Restrict \(P\) to those edges and apply Lemma 2.

Every original edge now belongs to exactly one of:

1. a lifted cycle from \(\mathcal D\);
2. a compatible two-edge cycle constructed from a remaining bundle;
3. a cycle in the compatible decomposition of the reserved \(2R\).

Their union is the required compatible decomposition. \(\square\)

The construction is polynomial-time: it uses spanning trees, ordinary cycle decompositions, greedy representative choices, and the matchings in Lemma 1.

## 4. What remains unresolved

The parity condition is sufficient, not necessary. Crucially, it does not handle the doubled-cubic instances appearing in the cycle-double-cover connection.

Indeed, let \(K\) be a simple 3-edge-connected cubic graph, put \(G=2K\), and let \(P\) pair the two copies of every edge at both endpoints. Then \(G\) is 6-edge-connected and Eulerian, but every bundle is blocked. Consequently
\[
A\text{ is edgeless},\qquad B=K.
\]
Every singleton component of \(A\) has three edges leaving it in \(B\), so condition (1) fails at every vertex.

Graphs with single-edge bundles are also outside the theorem. Thus the argument establishes the stated special cases but neither proves the original conjecture nor improves its general connectivity threshold. I have not established whether this sufficient condition is already recorded in the literature.