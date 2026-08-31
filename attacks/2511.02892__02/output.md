```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved for several structural classes, notably when the K4-interaction graph is a forest, or a cactus whose cyclic interactions are matchings apart from at most one light exception per cycle.",
  "would_publish": false,
  "caveats": "The unrestricted cyclic interaction case remains open, and novelty relative to the cited 2024 reduction has not been checked."
}
```

# 4-colourability of cycles plus \(K_4\)'s

## 1. Reformulation and outcome

Let \(\mathcal B\) be the set of components of \(H\), so each \(B\in\mathcal B\) has four vertices and induces a \(K_4\). A proper \(4\)-colouring of \(G\cup H\) is equivalently a colouring
\[
\varphi:V(G)\longrightarrow [4]
\]
such that:

1. \(\varphi(u)\ne\varphi(v)\) for every \(uv\in E(G)\);
2. \(\varphi|_B\) is a bijection \(B\to[4]\) for every \(B\in\mathcal B\).

Thus every \(K_4\)-block must be rainbow.

I do not prove the full conjecture. I establish:

- an exact Hall-type obstruction to extending a colouring over one block;
- a general greedy sufficient condition;
- the conjecture when the simple interaction graph of the \(K_4\)-blocks is a forest;
- a stronger cactus theorem, allowing one small nonmatching interaction on each cycle;
- a further sufficient condition in terms of a well-spaced independent transversal;
- structural restrictions on a minimal counterexample.

These arguments are constructive.

---

## 2. It is equivalent to allow paths as well as cycles

It is useful to replace “disjoint union of cycles” by “graph of maximum degree at most \(2\).”

### Proposition 2.1
The original conjecture is equivalent to the following formally stronger statement:

> If \(J\) has maximum degree at most \(2\), and \(H\) is a disjoint union of spanning \(K_4\)'s, then \(J\cup H\) is \(4\)-colourable.

### Proof
Only the reverse implication needs proof. Let \(J\) have maximum degree at most \(2\). Its components are paths, isolated vertices, and cycles.

For every path component \(P\) with at least two vertices and endpoints \(x,y\), add new vertices \(z_1,\dots,z_r\), where \(r\ge1\), and add the path
\[
y z_1 z_2\cdots z_r x.
\]
This turns \(P\) into a simple cycle. For an isolated vertex \(x\), add at least two new vertices and form a cycle through \(x\). The numbers of new vertices can be increased so that their total is divisible by \(4\). Partition the new vertices arbitrarily into \(4\)-sets and add a \(K_4\) on each such set.

The resulting degree-\(2\) graph is a disjoint union of cycles. Any \(4\)-colouring of the enlarged instance restricts to a \(4\)-colouring of the original instance. ∎

Hence deletion of an entire \(K_4\)-block is legitimate in a minimal-counterexample argument.

---

## 3. The exact one-block extension obstruction

Suppose all blocks except \(B\in\mathcal B\) have already been coloured properly and rainbow. For \(v\in B\), define
\[
F(v)=\{\varphi(u):u\in N_J(v)\setminus B\},\qquad
L(v)=[4]\setminus F(v).
\]
Since \(\Delta(J)\le2\),
\[
|F(v)|\le2,\qquad |L(v)|\ge2.
\]

Colouring \(B\) amounts to finding a system of distinct representatives for the four lists \(L(v)\).

### Lemma 3.1 — exact obstruction
The colouring extends over \(B\) unless at least one of the following occurs:

1. **Four-vertex obstruction:** there is a colour \(a\) such that
   \[
   a\in F(v)\qquad\text{for every }v\in B.
   \]
2. **Three-vertex obstruction:** there are three vertices \(v_1,v_2,v_3\in B\) and two colours \(a,b\) such that
   \[
   F(v_1)=F(v_2)=F(v_3)=\{a,b\}.
   \]

Conversely, either obstruction prevents an extension.

### Proof
Apply Hall's theorem to the bipartite graph between \(B\) and \([4]\), where \(v\) is adjacent to its available colours \(L(v)\).

Every list has size at least \(2\), so Hall cannot fail on a set of one or two vertices.

If Hall fails on three vertices, their union of lists has size at most \(2\). Since each individual list has size at least \(2\), the three lists are the same \(2\)-set. Their forbidden sets are therefore the same complementary pair, giving obstruction 2.

If Hall fails on all four vertices, the union of the four lists omits some colour \(a\), so \(a\in F(v)\) for every \(v\in B\), giving obstruction 1.

The converse is immediate: obstruction 1 leaves only three colours for four vertices, while obstruction 2 leaves only two colours for three vertices. ∎

Two immediate consequences are useful.

### Corollary 3.2
A colouring extends over \(B\) if at most three \(J\)-edges join \(B\) to already coloured vertices.

### Proof
Obstruction 1 requires at least four such edges, one incident with each vertex of \(B\). Obstruction 2 requires at least six, two incident with each of three vertices. ∎

### Corollary 3.3
A colouring extends over \(B\) if all already coloured \(J\)-neighbours of \(B\) lie in a single \(K_4\)-block \(A\).

### Proof
For obstruction 1, the unique vertex of colour \(a\) in \(A\) would have to be adjacent to all four vertices of \(B\), contradicting its \(J\)-degree at most \(2\).

For obstruction 2, the unique \(a\)-coloured vertex of \(A\), and likewise the unique \(b\)-coloured vertex, would each have to be adjacent to three vertices of \(B\), again impossible. ∎

---

## 4. Greedy positive classes

Define the interaction multigraph \(Q\) on vertex set \(\mathcal B\): every \(J\)-edge whose endpoints lie in distinct blocks gives one edge of \(Q\). Parallel edges are retained. Let \(S\) be the underlying simple graph.

### Proposition 4.1 — ordering criterion
Suppose the blocks can be ordered \(B_1,\dots,B_m\) so that for every \(i\), either

\[
e_J\left(B_i,\bigcup_{j<i}B_j\right)\le3,
\]
or all earlier neighbours of \(B_i\) belong to a single block \(B_j\).

Then \(J\cup H\) is \(4\)-colourable.

### Proof
Colour the blocks in the given order. At step \(i\), apply Corollary 3.2 in the first case and Corollary 3.3 in the second case. Every edge to a later block will be handled when that later block is coloured. Edges of \(J\) internal to \(B_i\) are automatically proper because \(B_i\) is rainbow. ∎

This yields two useful corollaries.

### Corollary 4.2
If the interaction multigraph \(Q\), with multiplicities counted, is \(3\)-degenerate, then \(J\cup H\) is \(4\)-colourable.

Here \(3\)-degenerate means that every nonempty induced submultigraph has a vertex incident with at most three edges, counting multiplicity.

### Corollary 4.3 — forest case
If the simple interaction graph \(S\) is a forest, then \(J\cup H\) is \(4\)-colourable.

### Proof
Root every component of \(S\) and order blocks so that every parent precedes its children. Each nonroot block then has only its parent among the earlier neighbouring blocks, regardless of how many parallel \(J\)-edges join the two blocks. Apply Proposition 4.1. ∎

In particular, the conjecture holds when there are at most two \(K_4\)-blocks.

---

## 5. A cactus theorem

For adjacent blocks \(A,B\), let
\[
F_{AB}=J[A,B]
\]
be the bipartite graph consisting of the \(J\)-edges between them.

Call the interaction \(AB\):

- a **matching interaction** if \(F_{AB}\) is a matching;
- **light** if \(|E(F_{AB})|\le3\).

Recall that a cactus is a simple graph in which every edge belongs to at most one cycle.

### Theorem 5.1
Suppose the simple interaction graph \(S\) is a cactus. Assume that on each cycle of \(S\),

- all but at most one interaction are matching interactions; and
- if there is an exceptional nonmatching interaction, it is light.

Then \(J\cup H\) is \(4\)-colourable.

The forest result is the case in which \(S\) has no cycles.

The main point is the following cycle-extension lemma.

### Lemma 5.2 — prescribed-root cycle extension
Let
\[
B_0B_1\cdots B_{r-1}B_0,\qquad r\ge3,
\]
be a cycle of interacting blocks. Suppose one block has an arbitrarily prescribed rainbow colouring. If all but possibly one of the interactions on the cycle are matchings, and the exceptional interaction is either a matching or has at most three edges, then the prescribed colouring extends to all blocks on the cycle.

### Proof
Choose an edge \(e=XY\) of the block-cycle such that every interaction on the path
\[
P=C-e
\]
is a matching. If one interaction is exceptional, choose it as \(e\).

Regard the four colours as \(\mathbb Z_4\). Let \(R\) be the prescribed block. Define a bijection
\[
\lambda_R:R\longrightarrow \mathbb Z_4
\]
equal to its prescribed colouring.

Starting from \(R\), propagate bijections \(\lambda_B:B\to\mathbb Z_4\) along the two directions of the path \(P\). Across a matching interaction \(AB\), require
\[
\lambda_A(u)=\lambda_B(v)
\]
for every edge \(uv\in E(F_{AB})\).
Because \(F_{AB}\) is a matching, these requirements prescribe distinct labels at distinct vertices and therefore extend to a bijection on the whole next block.

Let the omitted edge \(e\) join the endpoint blocks \(X,Y\). Define
\[
D=\{\lambda_X(x)-\lambda_Y(y):xy\in E(F_{XY})\}\subseteq\mathbb Z_4.
\]
We claim that \(D\ne\mathbb Z_4\).

If \(|E(F_{XY})|\le3\), this is immediate. Otherwise \(F_{XY}\) is a matching of size \(4\), hence a perfect matching. If \(D=\mathbb Z_4\), then its four differences are all distinct and
\[
\sum_{xy\in E(F_{XY})}
\bigl(\lambda_X(x)-\lambda_Y(y)\bigr)
=
\sum_{z\in\mathbb Z_4} z
=2\pmod 4.
\]
On the other hand, both endpoint labels run through all of \(\mathbb Z_4\), so the left side is
\[
(0+1+2+3)-(0+1+2+3)=0\pmod4,
\]
a contradiction. Thus \(D\ne\mathbb Z_4\).

Choose \(t\in\mathbb Z_4\setminus D\). We now choose a shift \(s_B\in\mathbb Z_4\) for every block \(B\) on the path \(P\), with

- \(s_R=0\);
- adjacent blocks on \(P\) receiving distinct shifts;
- \(s_Y-s_X=t\), after orienting \(e\) consistently with the definition of \(D\).

Such shifts always exist. Indeed, at distance \(d\) from \(R\), the possible endpoint shifts of a sequence with adjacent unequal terms are
\[
A_d=
\begin{cases}
\{0\},&d=0,\\
\mathbb Z_4\setminus\{0\},&d=1,\\
\mathbb Z_4,&d\ge2.
\end{cases}
\]
If the distances from \(R\) to \(X,Y\) are \(a,b\), then \(a+b=r-1\ge2\). For every \(t\in\mathbb Z_4\), one can choose \(x\in A_a\), \(y\in A_b\) with \(y-x=t\). The only nontrivial case is \(a=b=1\), where
\[
(\mathbb Z_4\setminus\{0\})-(\mathbb Z_4\setminus\{0\})=\mathbb Z_4.
\]

Finally colour each vertex \(v\in B\) by
\[
\varphi(v)=\lambda_B(v)+s_B.
\]
Every block is rainbow. Along an edge of the path \(P\), the two endpoint labels are equal, but the two shifts are different, so the colours differ. Along the omitted interaction \(XY\), equality would imply
\[
s_Y-s_X\in D,
\]
contrary to the choice of \(t\). This proves the lemma. ∎

### Proof of Theorem 5.1
Process the block-cut tree of each connected component of the cactus \(S\).

Start with an arbitrary rainbow colouring of a root block.

- Across a bridge \(AB\), once \(A\) is coloured, colour \(B\) using Corollary 3.3; at that moment \(A\) is its only already coloured neighbouring block.
- When a cycle block of the cactus is encountered, exactly one of its vertices in the block-cut tree has already been coloured. Apply Lemma 5.2 with that block as the prescribed root.

Continue outward. Every interaction is handled either when crossing a bridge or when processing its unique cactus cycle. ∎

---

## 6. A sufficient independent-transversal condition

A set \(T\subseteq V(J)\) is a block transversal if \(|T\cap B|=1\) for every \(B\in\mathcal B\).

### Proposition 6.1
Suppose there is a block transversal \(T\) such that

1. \(T\) is independent in \(J\);
2. \(\Delta(J-T)\le1\).

Then \(J\cup H\) is \(4\)-colourable.

### Proof
Colour every vertex of \(T\) with colour \(4\). The graph \(H-T\) is a disjoint union of triangles, while \(J-T\) is a matching together with isolated vertices. Therefore
\[
K=(H-T)\cup(J-T)
\]
has maximum degree at most \(3\).

Moreover, \(K\) contains no \(K_4\). Indeed, if a \(K_4\) used at most two vertices from every \(H-T\) triangle, each of its vertices would have at most one triangle-neighbour and at most one matching-neighbour inside the \(K_4\). If it used an entire triangle, the fourth vertex would need three incident matching edges, impossible.

By Brooks' theorem, every component of \(K\) is \(3\)-colourable; components of maximum degree at most \(2\) are also trivially \(3\)-colourable. In any proper \(3\)-colouring, each triangle of \(H-T\) receives all three colours. Together with colour \(4\) on \(T\), every original \(K_4\)-block is rainbow.

Edges incident with \(T\) are proper because the other endpoint receives one of the first three colours, and edges inside \(T\) do not exist. ∎

When \(J\) is a union of cycles, the hypotheses mean that consecutive vertices of \(T\) on each cycle occur at cyclic distance \(2\) or \(3\). Thus any independent block transversal with these spacing constraints settles the instance.

---

## 7. Restrictions on a minimal counterexample

Assume that a counterexample exists to the maximum-degree-\(2\) formulation, and choose one with the minimum number of \(K_4\)-blocks.

### Proposition 7.1
For such a minimal counterexample:

1. the simple interaction graph \(S\) is connected;
2. every block has at least four incident crossing \(J\)-edges, counted with multiplicity;
3. every block is adjacent in \(S\) to at least two other blocks;
4. for every block \(B\) and every colouring of the instance obtained by deleting \(B\), one of the two obstructions of Lemma 3.1 occurs.

Consequently, \(S\) has minimum degree at least \(2\). If \(S\) is a cactus, then some cycle either has at least two nonmatching interactions or has a nonmatching interaction containing at least four edges.

### Proof
Deleting a block leaves a smaller maximum-degree-\(2\) instance, which is colourable by minimality.

If a deleted block had at most three crossing edges, Corollary 3.2 would extend the colouring. If all its outside neighbours lay in one block, Corollary 3.3 would extend it. This proves assertions 2 and 3. Lemma 3.1 gives assertion 4.

If \(S\) were disconnected, each component would give a smaller instance; colour the components independently and combine the colourings. Thus \(S\) is connected.

The final cactus assertion follows from Theorem 5.1. ∎

The local obstruction is genuinely feasible under the degree bound. For example, if \(A,C\) are coloured blocks and their colour-\(1\) vertices respectively send two \(J\)-edges to \(\{b_1,b_2\}\subset B\) and two to \(\{b_3,b_4\}\subset B\), then colour \(1\) is forbidden at every vertex of \(B\). This respects maximum degree \(2\) but blocks extension of that particular outside colouring. Recolouring \(A\) and \(C\) might remove the obstruction, which is exactly where a global argument is needed.

---

## 8. Exact finite-domain formulation

Fix an ordering \(b_1,\dots,b_4\) of each block \(B\). Introduce one variable
\[
\pi_B\in S_4,
\]
where \(b_i\) receives colour \(\pi_B(i)\). For every crossing edge \(b_i c_j\in E(J)\), impose
\[
\pi_B(i)\ne \pi_C(j).
\]

This is a binary constraint satisfaction problem with domain size \(24\). Given a tree decomposition of the simple interaction graph \(S\) of width \(t\), standard bag dynamic programming decides the instance in time
\[
O\!\left(24^{\,t+1}\bigl(|V(S)|+|E(J)|\bigr)\right),
\]
up to the usual polynomial dependence on \(t\). A table entry records one permutation for every block in the bag and is retained exactly when all constraints whose endpoints have been processed are satisfied.

I did not run an exhaustive computation, so I make no small-order claim beyond the analytically proved two-block case.

---

## 9. Remaining gap

The unrestricted problem remains open in this analysis. The exact Hall lemma isolates the difficulty:

- four vertices of an uncoloured block may all see the same colour coming from at least two previously coloured blocks;
- or three vertices may each see the same pair of colours.

Both patterns are compatible with degree \(2\). The cactus argument avoids them by coordinating colourings through matching interactions. It does not handle, for example, a block-interaction cycle with two nonmatching edge bundles, nor a single nonmatching bundle of four or more edges. General interaction graphs can also contain overlapping cycles, where the \(\mathbb Z_4\)-shift construction no longer separates the constraints.

Thus no complete proof or counterexample is obtained. The cited Dalal–McDonald–Shan reduction may subsume some of these special cases; I have not verified its detailed contents, so no novelty claim is made.