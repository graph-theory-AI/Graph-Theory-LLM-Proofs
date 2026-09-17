```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I characterize all K4-minor-free graphs in the three classes and prove that every triangle-free 5- or 6-holed graph is K4-minor-free.",
  "would_publish": false,
  "caveats": "Graphs with K4 minors are not classified; novelty of the special-case characterization has not been checked."
}
```

# 1. The partial characterization

All graphs are finite and simple. Graphs without holes are allowed.

The unrestricted problem is not solved here. However, the low-attachment components left unresolved in the previous attempt can be classified completely when \(K_4\) minors are excluded. Moreover, for triangle-free \(5\)- and \(6\)-holed graphs, that exclusion is automatic.

The proof below is self-contained and does not assume the high-attachment characterization from the previous attempt.

For integers \(d,t\geq 2\), let \(\Theta_{d,t}\) be the graph consisting of two vertices \(u,v\) joined by \(t\) internally vertex-disjoint paths, each of length \(d\), with no additional edges. Thus
\[
\Theta_{d,2}=C_{2d},
\qquad
\Theta_{2,t}=K_{2,t}.
\]

A **vertex gluing** identifies one vertex of each of two otherwise disjoint graphs. An **edge gluing** identifies an edge of each graph, including its endpoints. The identified edge is retained, and no other edges are added.

## Theorem 1

Fix an integer \(\ell\geq 4\).

**(a)** A graph is both \(K_4\)-minor-free and \(\ell\)-holed if and only if it can be constructed by disjoint unions, vertex gluings, and edge gluings from the following building blocks:

- \(K_1,K_2,K_3\);
- \(C_\ell\), if \(\ell\) is odd;
- \(\Theta_{\ell/2,t}\) for arbitrary \(t\geq 2\), if \(\ell\) is even.

**(b)** If \(\ell\geq 5\), every triangle-free \(\ell\)-holed graph is \(K_4\)-minor-free.

Consequently, for the requested lengths, the nonclique building blocks in part (a) are
\[
\begin{array}{c|c}
\ell & \text{nonclique building blocks}\\ \hline
4 & K_{2,t}\quad(t\geq2),\\
5 & C_5,\\
6 & \Theta_{3,t}\quad(t\geq2).
\end{array}
\]

In particular:

- **Every triangle-free \(5\)-holed graph** is obtained from \(K_1,K_2,C_5\) by the three operations above.
- **Every triangle-free \(6\)-holed graph** is obtained from \(K_1,K_2\), and the graphs \(\Theta_{3,t}\), by those operations.

There is no degree restriction in these conclusions. For example, when \(t\geq3\), the two high-degree vertices of \(\Theta_{3,t}\) lie in opposite bipartition classes, so this family goes beyond the previous attempt’s one-sided degree-at-most-two case.

# 2. A modular obstruction to \(K_4\) subdivisions

We first prove the automatic exclusion asserted in part (b).

## Lemma 2

Let \(G\) be triangle-free and \(\ell\)-holed, where \(\ell\geq4\). Every cycle of \(G\), whether induced or not, has length congruent to \(2\) modulo \(\ell-2\).

### Proof

Induct on the cycle length.

An induced cycle has length \(\ell\), and
\[
\ell\equiv2\pmod{\ell-2}.
\]

If a cycle \(Q\) has a chord, that chord divides it into two shorter cycles \(Q_1,Q_2\), with
\[
|Q|=|Q_1|+|Q_2|-2.
\]
By induction, the right-hand side is congruent to \(2+2-2=2\).

Triangle-freeness ensures that every chordless cycle encountered in this induction is a hole and therefore has length \(\ell\). ∎

## Lemma 3

If \(\ell\geq5\), a triangle-free \(\ell\)-holed graph contains no subdivision of \(K_4\).

### Proof

Put \(r=\ell-2\), so \(r\geq3\). Suppose there is a subdivision of \(K_4\), with branch vertices labelled \(1,2,3,4\). Write \(a_{ij}\) for the length of its branch path corresponding to edge \(ij\).

Every cycle in this subdivision is also a cycle of \(G\), so Lemma 2 applies to it. In particular,
\[
a_{12}+a_{13}+a_{23}\equiv2\pmod r,
\]
\[
a_{12}+a_{14}+a_{24}\equiv2\pmod r,
\]
and
\[
a_{13}+a_{23}+a_{24}+a_{14}\equiv2\pmod r.
\]
Adding the first two congruences and subtracting the third gives
\[
2a_{12}\equiv2\pmod r.
\]
The same argument applies to every branch path:
\[
2a_{ij}\equiv2\pmod r. \tag{1}
\]

Now double the length of the cycle on branch vertices \(1,2,3\). Equation (1) gives
\[
2(a_{12}+a_{13}+a_{23})\equiv6\pmod r.
\]
But Lemma 2 says that the same expression is congruent to \(4\). Thus \(r\mid2\), contradicting \(r\geq3\). ∎

For completeness, excluding a \(K_4\) subdivision is equivalent to excluding a \(K_4\) minor. The nontrivial direction is elementary: given four branch sets of a \(K_4\)-minor model, choose one connecting edge for each pair. Within each branch set, a tree joining its three connection points has a median vertex from which the three connections can be reached by paths meeting only at that vertex. Combining these paths with the six selected connecting edges produces a \(K_4\) subdivision. Coincident connection points simply give paths of length zero within the branch set.

Lemmas 2 and 3 therefore prove Theorem 1(b).

# 3. Attachments to a cycle without a \(K_4\) subdivision

The next observations concern arbitrary cycles, not just holes.

For a component \(D\) of \(G-V(C)\), write
\[
N_C(D)=N_G(D)\cap V(C).
\]

## Lemma 4

Suppose \(G\) contains no subdivision of \(K_4\).

1. If \(C\) is a cycle and \(D\) is a component of \(G-V(C)\), then
   \[
   |N_C(D)|\leq2.
   \]
2. There cannot be two paths with mutually disjoint interiors outside \(C\), whose four distinct ends occur alternately around \(C\).

### Proof

For the first assertion, suppose \(D\) has three distinct neighbors \(a,b,c\) on \(C\). Choose edges from \(a,b,c\) into \(D\). A minimal tree joining these three vertices through \(D\) consists of three paths from a common vertex in \(D\) to \(a,b,c\), meeting only at that common vertex. Together with the three \(a,b,c\)-arcs of \(C\), these paths form a subdivision of \(K_4\).

For the second assertion, the four arcs of \(C\) between the four ends, together with the two external paths, form a subdivision of \(K_4\). Extra edges of \(G\) are irrelevant: the subdivision need not be induced. ∎

# 4. Classification of the clique-cutset atoms

A clique cutset is a clique whose deletion leaves at least two nonempty components.

## Proposition 5

Let \(\ell\geq4\), and let \(G\) be a connected, \(K_4\)-subdivision-free, \(\ell\)-holed graph. Suppose \(G\) has no clique cutset of size one or two.

Then \(G\) is one of:

- \(K_1,K_2,K_3\);
- \(C_\ell\), if \(\ell\) is odd;
- \(\Theta_{\ell/2,t}\) for some \(t\geq2\), if \(\ell\) is even.

### Proof

### Step 1: Dispose of triangles and forests

Suppose \(G\) contains a triangle \(T\). If \(G\neq T\), take a component \(D\) of \(G-V(T)\). Connectivity and Lemma 4 give
\[
1\leq |N_T(D)|\leq2.
\]
Since \(T\) is a triangle, \(N_T(D)\) is a clique. Its deletion separates \(D\) from the nonempty set \(V(T)\setminus N_T(D)\), contradicting the hypothesis.

Thus any triangle-containing graph under consideration is \(K_3\).

We may therefore assume \(G\) is triangle-free. If it is acyclic, it is a tree. A tree on at least three vertices has a cut vertex, so in this case \(G\) is \(K_1\) or \(K_2\).

It remains to consider a triangle-free graph containing a hole
\[
C=c_0c_1\cdots c_{\ell-1}c_0.
\]

### Step 2: Every external component attaches antipodally

Let \(D\) be a component of \(G-V(C)\).

By connectivity and Lemma 4, \(N_C(D)\) has size one or two. Size one would give a cut vertex. Two adjacent neighbors would give a clique cutset of size two. Consequently,
\[
N_C(D)=\{a,b\},
\]
where \(a,b\) are nonadjacent on \(C\).

Choose a shortest \(a\)-\(b\) path \(P\) in \(G[D\cup\{a,b\}]\). Let its length be \(p\), and let the two \(a\)-\(b\) arcs of \(C\) have lengths \(d\) and \(\ell-d\).

Both unions of \(P\) with a rim arc are holes:

- \(P\) is induced by shortestness;
- its interior has no neighbor on \(C\setminus\{a,b\}\);
- \(a,b\) are nonadjacent;
- each rim arc is induced.

Hence
\[
p+d=\ell,\qquad p+\ell-d=\ell.
\]
It follows that
\[
p=d=\ell-d=\ell/2. \tag{2}
\]

If \(\ell\) is odd, this is impossible. There are then no vertices outside \(C\), and \(G=C_\ell\).

Assume henceforth that \(\ell=2h\).

### Step 3: All external components use the same antipodal pair

Equation (2) shows that every component outside \(C\) attaches to an antipodal pair.

Two distinct antipodal pairs on \(C_{2h}\) have four distinct ends occurring alternately around the cycle. Paths through their corresponding components would have disjoint interiors, contradicting Lemma 4(2).

Therefore, if \(G\neq C\), there is one antipodal pair \(\{u,v\}\) such that
\[
N_C(D)=\{u,v\}
\quad\text{for every component }D\text{ of }G-V(C). \tag{3}
\]

### Step 4: Every external component is one path

Fix a component \(D\), and choose a shortest \(u\)-\(v\) path \(P\) through \(D\). By (2), \(P\) has length \(h\).

Let \(R_1,R_2\) be the two \(u\)-\(v\) arcs of \(C\), each of length \(h\). The union
\[
C'=P\cup R_1
\]
is another \(2h\)-hole.

By (3), no vertex outside \(C\) has a neighbor in the interior of \(R_2\). Since \(C\) is induced, the interior of \(R_2\) is therefore a component of \(G-V(C')\), attached to \(C'\) precisely at \(u,v\).

Steps 2 and 3 apply to the hole \(C'\) as well. Since one component outside \(C'\) attaches at \(u,v\), every component outside \(C'\) attaches precisely at \(u,v\).

Suppose \(D\) contained a vertex outside the interior of \(P\). Because \(D\) is connected, some edge would join a vertex of \(P\setminus\{u,v\}\) to a vertex of \(D\setminus V(P)\). The latter vertex belongs to a component outside \(C'\), giving that component a neighbor on \(C'\) different from \(u,v\), a contradiction.

Thus
\[
D=V(P)\setminus\{u,v\}.
\]

This holds for every component outside \(C\). Accordingly, \(G\) consists of \(R_1,R_2\), and one additional length-\(h\) path for each such component, with no edges between their interiors. Hence
\[
G=\Theta_{h,t}
\]
for some \(t\geq2\). ∎

This proposition resolves all low-attachment components in the minor-free setting: in an atom, they are absent for odd \(\ell\), and are single half-length paths with common ends for even \(\ell\).

# 5. Gluing and completion of the characterization

We check both preservation properties required by Theorem 1(a).

## Lemma 6

Let \(G\) be obtained by gluing \(G_1,G_2\) along a clique \(S\) of size at most two, with no edges between their vertices outside \(S\).

1. Every hole of \(G\) lies entirely in \(G_1\) or entirely in \(G_2\).
2. If \(G_1,G_2\) contain no \(K_4\) subdivision, neither does \(G\).

### Proof

For the first assertion, a cycle meeting both sides must pass through two distinct vertices of \(S\). These vertices cannot be consecutive on the cycle, because both arcs between them must contain vertices outside \(S\). Their adjacency in the clique \(S\) is therefore a chord. If \(|S|\leq1\), no cycle can meet both sides in the first place.

For the second assertion, suppose \(T\) is a \(K_4\) subdivision in \(G\). Any two branch vertices of \(T\) are joined in \(T\) by three internally vertex-disjoint paths. Thus branch vertices cannot lie on opposite sides of the separator \(S\). All four branch vertices lie in one summand, say \(G_1\).

Every vertex of \(T\) outside \(G_1\) has degree two in \(T\). Such vertices can only form excursions between vertices of \(S\). Every cycle of a \(K_4\) subdivision contains at least three branch vertices. Consequently, an excursion cannot have the same end twice; there cannot be two excursions between the two vertices of \(S\); and the edge joining those vertices cannot already belong to \(T\) if an excursion is present.

Thus there is at most one excursion, and replacing it by the edge of \(S\) produces a \(K_4\) subdivision wholly in \(G_1\), a contradiction. ∎

### Necessity in Theorem 1(a)

Proceed by induction on \(|V(G)|\), handling disconnected graphs componentwise.

If \(G\) has a clique cutset \(S\) of size one or two, split \(G\) into two proper induced subgraphs whose intersection is \(S\), with no edges between their vertices outside \(S\). Both pieces remain \(\ell\)-holed and \(K_4\)-minor-free. By induction they have the claimed construction, and gluing them reconstructs \(G\).

If there is no such cutset, Proposition 5 gives one of the stated building blocks.

The empty graph is obtained by an empty disjoint union.

### Sufficiency in Theorem 1(a)

Every building block is \(\ell\)-holed:

- \(K_1,K_2,K_3\) have no holes;
- the cycle block has length \(\ell\);
- every cycle of \(\Theta_{\ell/2,t}\) uses exactly two of its branches and therefore has length \(\ell\).

Every building block is also \(K_4\)-subdivision-free. For a theta block, only its two end vertices can have degree at least three, whereas a \(K_4\) subdivision requires four such vertices.

Lemma 6 preserves both properties under the allowed gluings. Disjoint unions also preserve them. This proves part (a).

Finally, a triangle cannot straddle the two sides of a vertex or edge gluing. Thus omitting \(K_3\) produces triangle-free graphs. Conversely, every induced piece in the decomposition of a triangle-free graph is triangle-free, so no \(K_3\) block occurs. Together with Lemma 3, this proves the claimed unconditional descriptions for triangle-free \(5\)- and \(6\)-holed graphs.

# 6. Why this does not solve the unrestricted problem

The restrictions are substantive, including after clique-cutset decomposition.

## 6.1 Length four

The graph \(K_{3,3}\) is triangle-free and \(4\)-holed, and has no clique cutset. It nevertheless contains a \(K_4\) subdivision.

Explicitly, with bipartition
\[
\{a_1,a_2,a_3\},\qquad \{b_1,b_2,b_3\},
\]
take branch vertices \(a_1,a_2,b_1,b_2\), the four edges between these two pairs, and the paths
\[
a_1-b_3-a_2,\qquad b_1-a_3-b_2.
\]
These form the required subdivision.

Thus the automatic minor exclusion cannot extend to \(\ell=4\). In the modular proof, the obstruction disappears exactly because \(\ell-2=2\).

## 6.2 Triangle-containing atoms for lengths five and six

Here are small atoms outside the characterization.

### A \(5\)-holed atom

Take a triangle on \(a_1,a_2,a_3\), a vertex \(u\), and three additional vertices \(x_1,x_2,x_3\). Add precisely the paths
\[
u-x_i-a_i\qquad(i=1,2,3)
\]
besides the triangle edges.

Its holes are exactly
\[
u-x_i-a_i-a_j-x_j-u
\qquad(i\neq j),
\]
all of length five. Indeed, deleting \(u\) leaves a triangle with pendant vertices, and an induced cycle through \(u\) must use two of the displayed paths and the edge joining their triangle ends.

This graph is itself a subdivision of \(K_4\).

### A \(6\)-holed atom

Take disjoint triangles on \(a_1,a_2,a_3\) and \(b_1,b_2,b_3\). Join corresponding vertices by the paths
\[
a_i-x_i-b_i\qquad(i=1,2,3),
\]
with no additional edges.

Its holes are exactly
\[
a_i-x_i-b_i-b_j-x_j-a_j-a_i
\qquad(i\neq j),
\]
all of length six. A hole must cross between the two triangles, and it can use at most two vertices of either triangle, forcing exactly this form.

It also contains a \(K_4\) subdivision: the second triangle together with the three \(x_i\)'s is a connected set attached to all three vertices of the first triangle, so the construction in Lemma 4 applies.

Both graphs have no clique cutset. Every clique is contained in one of the displayed triangles or in an edge of a displayed two-edge path; deleting any such clique leaves a connected graph.

Therefore, triangles create additional genuine atoms, not merely pieces that disappear under clique-cutset decomposition.

# 7. Remaining gap

The proved result gives:

- a complete characterization inside the \(K_4\)-minor-free class for all three requested lengths;
- an unconditional complete characterization of the triangle-free subclasses for lengths five and six.

It does **not** describe the general \(K_4\)-minor-containing atoms. For lengths five and six, every such graph necessarily contains a triangle, but the examples above show that this is not enough to force a clique cutset.

That is the unresolved part of this attack. I have not verified the literature status or novelty of the special-case theorem, and make no claim that the unrestricted catalog problem is settled.