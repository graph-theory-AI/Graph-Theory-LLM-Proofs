```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove 4-colourability whenever the K4-interaction graph has treewidth at most 2, including all cactus interaction graphs without restrictions on their edge bundles.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved here; novelty of the structural reduction has not been checked."
}
```

# A degree-preserving reduction and the treewidth-two case

I obtain a stronger structural result than the earlier cactus theorem: **all cactus interaction graphs are allowed, with arbitrarily many nonmatching or heavy interactions on their cycles**. More generally, the result holds whenever the interaction graph has treewidth at most two.

The main ingredient is a local reduction that eliminates a \(K_4\)-block having at most two neighbouring blocks. Its proof is self-contained and uses an explicit ten-case analysis of a four-edge auxiliary multigraph.

## 1. Statement and setup

Let \(J\) be a finite simple graph of maximum degree at most two, and let
\[
\mathcal B=\{B_1,\ldots,B_m\}
\]
partition \(V(J)\) into sets of size four. Let \(H\) consist of a \(K_4\) on every \(B_i\).

The **interaction graph** \(S\) has vertex set \(\mathcal B\), with \(A B\in E(S)\) when \(J\) has an edge between the distinct blocks \(A\) and \(B\). Multiplicities are ignored in \(S\).

A desired colouring assigns the four colours bijectively to every block and properly colours every edge of \(J\).

### Theorem 1
If \(S\) has treewidth at most two, then \(J\cup H\) is \(4\)-colourable.

Consequently, the original conjecture holds when:

- the interaction graph is a cactus, with no restrictions on its interactions;
- more generally, the interaction graph is a partial \(2\)-tree;
- there are at most three \(K_4\)-blocks.

The proof is constructive.

### Why allowing maximum degree two is legitimate

The cycle formulation is equivalent to the formulation with \(\Delta(J)\leq 2\).

Indeed, close each path component into a simple cycle using fresh vertices; an isolated vertex requires at least two fresh vertices. The numbers added can be chosen so that their total is divisible by four. Partition the fresh vertices into new \(K_4\)-blocks. A colouring of the enlarged cycle instance restricts to one of the original instance.

For Theorem 1, however, I prove the maximum-degree-two formulation directly.

## 2. The exact one-block obstruction

Suppose all blocks except \(B\) have been coloured. For \(b\in B\), put
\[
F(b)=\{\varphi(x):x\in N_J(b)\setminus B\},
\qquad
L(b)=[4]\setminus F(b).
\]
Every list has size at least two. Edges of \(J\) inside \(B\) cause no additional difficulty once \(B\) is rainbow.

### Lemma 2
The colouring fails to extend over \(B\) if and only if at least one of the following occurs:

1. some colour belongs to \(F(b)\) for all four \(b\in B\);
2. three vertices of \(B\) have the same forbidden set \(\{a,b\}\) of size two.

### Proof
Extension is equivalent to finding distinct representatives of the four lists.

Hall's condition cannot fail on one or two lists. Failure on three lists means that their union has size two, so all three are the same two-element set. Failure on all four lists means that some colour is absent from their union. These are exactly the two stated obstructions. ∎

In particular, if all outside neighbours of \(B\) lie in one coloured block, extension is always possible: each colour can then be forbidden at at most two vertices of \(B\).

## 3. Eliminating a block with two neighbouring blocks

Here is the main reduction.

### Lemma 3 — two-neighbour replacement
Suppose all outside neighbours of a block \(B\) lie in two other blocks \(A,C\). There is a simple graph \(P\), with edges only between \(A\) and \(C\), such that

\[
d_P(x)\leq e_J(x,B)\qquad(x\in A\cup C),
\tag{1}
\]

and every rainbow proper \(4\)-colouring of
\[
(J-B)\cup P\cup(H-B)
\]
extends, without changing any already assigned colour, to a rainbow proper \(4\)-colouring of \(J\cup H\).

In particular,
\[
J'=(J-B)\cup P
\]
still has maximum degree at most two.

The corresponding assertion with zero or one neighbouring block holds with \(P=\varnothing\).

### Proof

The zero- and one-neighbour cases follow from Lemma 2. Assume there are two possible neighbouring blocks \(A,C\).

#### 3.1. A four-edge auxiliary multigraph

Construct a loopless multigraph \(R\), with one edge for each vertex \(b\in B\):

- if \(b\) has two outside neighbours \(x,y\), add the edge \(xy\);
- if it has one outside neighbour \(x\), add \(xz_b\), where \(z_b\) is a private auxiliary vertex;
- if it has no outside neighbours, add an edge between two private auxiliary vertices.

Thus \(R\) has exactly four edges. Its real vertices lie in \(A\cup C\), and
\[
d_R(x)=e_J(x,B)\leq 2
\]
for each real vertex \(x\). Auxiliary vertices have degree one.

Hence \(\Delta(R)\leq 2\). Parallel edges are possible, but loops are not.

Call a pair of vertices **admissible** if one is a real vertex of \(A\) and the other a real vertex of \(C\). Only admissible pairs will become edges of \(P\).

Write \(P_k\) for a path on \(k\) vertices, and \(D\) for a component consisting of two parallel edges. Ignoring isolated vertices, the following ten forms exhaust all possibilities for \(R\).

#### 3.2. Construction of \(P\)

In the table, an indicated edge is added only when its pair is admissible.

| Form of \(R\) | Edges to put in \(P\) |
|---|---|
| \(P_5=x_1x_2x_3x_4x_5\) | \(x_2x_4\) |
| \(C_4=x_1x_2x_3x_4x_1\) | Both admissible opposite pairs \(x_1x_3,x_2x_4\) |
| \(P_4=x_1x_2x_3x_4\), together with \(P_2\) | If both \(x_1x_3\) and \(x_2x_4\) are admissible, add \(x_1x_3\); otherwise add nothing |
| \(C_3\), together with \(P_2\) | Nothing |
| Two \(P_3\)'s, with centres \(s,t\) | \(st\) |
| \(D\) on \(p,q\), together with \(P_3=rst\) | \(ps\) and \(qs\) |
| Two \(D\)'s, on \(p,q\) and \(r,s\) | All admissible pairs between \(\{p,q\}\) and \(\{r,s\}\) |
| \(P_3\), together with two \(P_2\)'s | Nothing |
| \(D\), together with two \(P_2\)'s | The rule immediately below |
| Four \(P_2\)'s | Nothing |

For the remaining rule, let the double-edge component have endpoints \(p,q\), and let the two single-edge components be \(e_1,e_2\). The vertices \(p,q\), having degree two in \(R\), are real.

- **If \(p,q\) lie in the same block:** consider those \(e_i\) whose two endpoints are real and lie in the other block. Assign these eligible edges injectively to \(p,q\). For each eligible edge, join its assigned vertex to both endpoints.
- **If \(p,q\) lie in different blocks:** rename them so that \(p\in A\), \(q\in C\). For each \(e_i\) having one endpoint in \(A\) and one in \(C\), join \(p\) to its endpoint in \(C\).

This completes the construction.

Every row satisfies
\[
d_P(x)\leq d_R(x).
\]
For example, in the last rule each degree-one endpoint receives at most one new edge, while \(p,q\) receive at most two each. In the two-double-edge case, each vertex receives at most two edges. The other rows are immediate.

Thus (1) holds, and
\[
d_{J'}(x)
\leq d_J(x)-e_J(x,B)+d_P(x)
\leq 2.
\tag{2}
\]

It remains to prove the extension property.

#### 3.3. Excluding the four-vertex obstruction

Fix a rainbow proper colouring of the reduced instance. Suppose a colour \(a\) is forbidden at all four vertices of \(B\).

There are at most two real outside vertices of colour \(a\): one in \(A\) and one in \(C\). Each has degree at most two in \(R\). To account for all four edges of \(R\), these two vertices must therefore:

- both have degree two;
- be nonadjacent in \(R\);
- together meet all four edges of \(R\).

Their pair is admissible.

The possible pairs of this kind are exactly:

- \(x_2,x_4\) in \(P_5\);
- an opposite pair in \(C_4\);
- the two centres in \(P_3\cup P_3\);
- the centre of \(P_3\) and either endpoint of \(D\), in \(D\cup P_3\);
- one endpoint from each component in \(D\cup D\).

There is no such pair in any other row of the table. In every listed case, the construction places the admissible pair in \(P\). Its two endpoints cannot therefore both have colour \(a\), a contradiction.

#### 3.4. Excluding the three-vertex obstruction

Suppose three vertices of \(B\) have forbidden set \(\{a,b\}\).

Their corresponding three edges of \(R\) have real endpoints, with each edge joining a vertex coloured \(a\) to one coloured \(b\). Since each colour occurs at most once in each of \(A,C\), these three edges use at most four vertices.

A loopless multigraph of maximum degree two, with three edges, at most four vertices, and a proper two-colouring must be either

\[
P_4
\qquad\text{or}\qquad
D\cup P_2.
\tag{3}
\]

We check these possibilities.

**A \(P_4\).** Along a path \(x_1x_2x_3x_4\) with colours alternating \(a,b\), the pairs
\[
x_1x_3,\qquad x_2x_4
\]
are monochromatic. Both pairs must be admissible, because colours are distinct within each block.

Such a three-edge path lies in a component \(P_4\), \(P_5\), or \(C_4\) of \(R\).

- In the \(P_4\cup P_2\) row, \(P\) contains \(x_1x_3\).
- In a \(P_5=x_1\cdots x_5\), either three-edge subpath makes \(x_2x_4\) monochromatic, and that edge is in \(P\).
- In a \(C_4\), the relevant opposite pairs are in \(P\).

Each case contradicts properness on \(P\).

**A \(D\cup P_2\).** Let \(p,q\) be the endpoints of the double edge. Their colours are \(a,b\), and the selected single edge also has endpoint colours \(a,b\).

- In \(D\cup P_3=rst\), the selected single edge contains the centre \(s\). Its colour agrees with that of \(p\) or \(q\). The corresponding admissible edge \(ps\) or \(qs\) is in \(P\).
- In \(D\cup D\), a monochromatic admissible pair between the two components is in \(P\).
- In \(D\cup P_2\cup P_2\), if \(p,q\) lie in the same block, the selected single edge lies entirely in the other block. The construction joins both its endpoints to its assigned vertex \(p\) or \(q\), so one added edge is monochromatic.
- In that same row, if \(p\in A,q\in C\), the selected single edge has one endpoint in each block. Its \(C\)-endpoint has the same colour as \(p\), and the construction joins them.

Again there is a contradiction.

Both obstructions of Lemma 2 have been excluded. The four lists consequently have distinct representatives, providing the required extension over \(B\). ∎

## 4. Proof of the treewidth-two theorem

I spell out why the reduction respects the structural hypothesis; mere \(2\)-degeneracy would not suffice for this argument.

A graph of treewidth at most two has a tree decomposition with bags of size at most three. Such a graph has a vertex \(B\) with at most two neighbours, and these neighbours can be joined after deleting \(B\) without increasing the treewidth above two.

Here is the standard decomposition argument. Repeatedly discard a leaf bag contained in its neighbouring bag. If only one bag remains, the assertion is immediate. Otherwise, take a leaf bag and a vertex \(B\) in it but not in its neighbouring bag. The running-intersection property implies that \(B\) occurs only in this leaf bag. Thus all neighbours of \(B\) lie in the same bag, and there are at most two. After deleting \(B\), adding the edge between those two neighbours is still covered by that bag.

Now prove Theorem 1 by induction on the number of blocks.

Choose such a block \(B\) in the interaction graph.

- If it has at most one neighbour, delete it and use the zero- or one-neighbour case of Lemma 3.
- If its neighbours are \(A,C\), apply Lemma 3 and form
  \[
  J'=(J-B)\cup P.
  \]

By (2), \(\Delta(J')\leq 2\). The new interaction graph is a subgraph of the graph obtained from \(S-B\) by adding \(AC\), so it still has treewidth at most two.

The induction hypothesis colours the reduced instance. Lemma 3 extends this colouring over \(B\). This proves the theorem. ∎

Every cactus has treewidth at most two: one may successively shorten an end-cycle by deleting a degree-two vertex and joining its neighbours, and remove leaves when no cycle remains. Thus the cactus conclusion has **no matching or lightness assumptions**.

With an appropriate elimination order supplied, the construction uses constant-size local operations at each block. During reconstruction, an extension can be found by checking the \(24\) bijections from the block to the four colours.

## 5. Consequences for a smallest counterexample

Suppose the conjecture fails, and choose a counterexample to the equivalent maximum-degree-two formulation having the minimum number of blocks.

### Corollary 4
Its interaction graph is \(2\)-connected and has minimum degree at least three.

### Proof
A block with at most two neighbouring blocks can be eliminated using Lemma 3. The resulting smaller maximum-degree-two instance is colourable by minimality, and its colouring extends back. Thus the interaction graph has minimum degree at least three.

Disconnected instances can be coloured componentwise, so the interaction graph is connected.

If a block \(B\) were a cutvertex, let \(D_1,\ldots,D_k\), \(k\geq2\), be the components after deleting \(B\). Each instance on \(D_i\cup\{B\}\) is smaller and hence colourable. Globally permute its four colours to agree with one prescribed rainbow colouring of \(B\). These colourings then combine, contradicting that the original instance was a counterexample. ∎

The minimum-degree assertion is stronger than the minimum-degree-two conclusion in the earlier attempt.

## 6. A precise limitation of the reduction

The two-neighbour hypothesis is genuinely relevant to this particular method. A universal degree-preserving replacement need not exist for a block with three neighbouring blocks.

Consider four blocks
\[
B=\{b_1,b_2,b_3,b_4\},\quad
A=\{a_1,a_2,a_3,a_4\},\quad
C=\{c_1,c_2,c_3,c_4\},\quad
D=\{d_1,d_2,d_3,d_4\},
\]
with
\[
\begin{aligned}
N_J(b_1)&=\{a_1,a_2\},&
N_J(b_2)&=\{c_1,c_2\},\\
N_J(b_3)&=\{d_1,d_2\},&
N_J(b_4)&=\{a_3,a_4\},
\end{aligned}
\]
and no other edges of \(J\).

Every outside neighbour has exactly one incident edge to \(B\). Therefore any replacement \(P\) satisfying the analogous budget
\[
d_P(x)\leq e_J(x,B)
\]
must be a matching on those eight outside neighbours.

For any such \(P\), put
\[
T=\{a_1,a_2,c_1,c_2,d_1,d_2\}.
\]
The graph on \(T\) consisting of \(P[T]\) and the three pair edges
\[
a_1a_2,\quad c_1c_2,\quad d_1d_2
\]
is a union of two matchings, hence bipartite. Colour it with colours \(1,2\). Each of the three displayed pairs then uses both colours.

Assign colours \(3,4\) to each remaining pair in \(A,C,D\). This is a rainbow colouring of the outside blocks and is proper on \(P\): any edge of \(P\) leaving \(T\) goes to \(a_3\) or \(a_4\), while an edge between those two vertices is also proper.

But now
\[
L(b_1)=L(b_2)=L(b_3)=\{3,4\},
\]
so this outside colouring does not extend over \(B\).

Thus no replacement satisfying the degree budget has the universal extension property here. **This is not a counterexample to the conjecture**—its interaction graph is a tree, so Theorem 1 colours it. It only shows why one cannot extend Lemma 3 to arbitrary three-neighbour blocks by the same argument.

## 7. Remaining gap

The unrestricted conjecture is not proved, and no counterexample is produced.

The established partial result is:

\[
\boxed{\text{Cycles plus }K_4\text{'s are 4-colourable whenever their block interaction graph has treewidth }\leq2.}
\]

The proof covers arbitrary edge bundles, including all cactus cases omitted by the earlier attempt. For general interaction graphs, the elimination process can reach a graph of minimum degree at least three; the local replacement lemma gives no further reduction there.

No computational result or unverified literature theorem is used in the argument. I have not checked whether this structural reduction already appears in the literature, so I make no novelty claim.