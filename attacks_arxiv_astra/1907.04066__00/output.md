```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "After degree-three peeling, there is an O(4^k n)-time algorithm, where k counts interior vertices of degree at least five, and every instance reduces to an alternating two-color boundary instance.",
  "would_publish": false,
  "caveats": "The unrestricted polynomial-time question is not settled; no novelty claim is made for these elementary partial results."
}
```

## 1. Results obtained

I do not obtain a polynomial-time algorithm for unrestricted near-triangulations, or a hardness result. I establish the following partial results.

1. **Boundary normalization:** every instance reduces, by adding at most two vertices, to one whose prescribed outer coloring is \(1,2,1,2\).
2. **A parameterized algorithm:** repeatedly delete interior vertices of degree at most three, obtaining \(G_0\). Put
   \[
   k=\bigl|\{v\in V(G_0)\setminus V(C):\deg_{G_0}(v)\ge 5\}\bigr|.
   \]
   Extension can be decided in time
   \[
   O(4^k|V(G)|).
   \]
   In particular, this is linear time when every interior vertex of the original graph has degree at most four.
3. **An explicit description of the \(k=0\) case:** when the outer cycle is chordless, the remaining graph \(G_0\) is a double fan over a path. Extension is governed by a simple parity condition.
4. **An unrestricted structural observation:** for a chordless outer 4-cycle, at least three of the four boundary-coloring types extend. Determining whether the fourth extends is the unresolved part.

I use the standard convention that a near-triangulation is a simple plane graph whose outer face is bounded by a cycle and whose bounded faces are triangles. The only classical coloring theorems invoked below are the Four Color Theorem and Brooks’ theorem.

---

## 2. Boundary types and a two-vertex normalization

Write the outer cycle as \(C=abcd\). Up to permutation of the four colors, its proper colorings have exactly four types:
\[
\begin{array}{c|c|c}
\text{type}&(\psi(a),\psi(b),\psi(c),\psi(d))&
\text{equal opposite pairs}\\ \hline
A&(1,2,1,2)&a=c,\ b=d\\
B&(1,2,1,3)&a=c\\
C&(1,2,3,2)&b=d\\
D&(1,2,3,4)&\text{none}.
\end{array}
\]
Let \(E_A(G),E_B(G),E_C(G),E_D(G)\) be the corresponding extension predicates. Color permutations ensure that these predicates depend only on the indicated type.

### A boundary move

Define \(T_bG\) by adding a new vertex \(x\) outside \(C\), adjacent to \(a,b,c\). Its outer cycle is
\[
axcd,
\]
and the two newly bounded faces are \(abx\) and \(bcx\). Thus \(T_bG\) is again a near-triangulation with outer boundary of length four.

The extension predicates satisfy
\[
\boxed{
(E_A,E_B,E_C,E_D)(T_bG)
=
(E_B,\ E_A\lor E_B,\ E_D,\ E_C)(G).
}
\tag{1}
\]

To verify this, first suppose \(a\) and \(c\) have the same color. Then \(b,x,d\) use the other three colors, subject to \(b\ne x\).

- If the new boundary has type \(A\), then \(x=d\), so \(b\ne d\): the old boundary has type \(B\). Conversely, an old type-\(B\) coloring extends by giving \(x\) the color of \(d\).
- If the new boundary has type \(B\), then \(x\ne d\), and the old boundary can have either type \(A\) or type \(B\). Conversely, either old type permits a suitable choice for \(x\).

If \(a\ne c\), both \(b\) and \(x\) must use the two colors absent from \(\{a,c\}\). Since \(b\ne x\), they use these colors oppositely. Consequently, \(b=d\) holds exactly when \(x\ne d\), interchanging types \(C\) and \(D\). This proves (1), including both directions of every equivalence.

Similarly, let \(T_a\) add a vertex adjacent to \(d,a,b\), replacing \(a\) on the outer boundary. By cyclic symmetry,
\[
E_A(T_aG)=E_C(G).
\tag{2}
\]

It follows that the original instance reduces to type \(A\) as follows:
\[
\begin{array}{c|c}
\text{original type}&\text{graph on which to request type }A\\ \hline
A&G\\
B&T_bG\\
C&T_aG\\
D&T_a(T_bG).
\end{array}
\tag{3}
\]
For the last row,
\[
E_A(T_a(T_bG))=E_C(T_bG)=E_D(G).
\]

Thus the full problem is polynomial-time equivalent to the problem with the fixed alternating boundary pattern \(1,2,1,2\). This is a normalization, not a solution: the alternating case itself can fail.

### Chords are easy

If \(C\) has a chord, say \(ac\), then extension is possible exactly when \(\psi(a)\ne\psi(c)\).

Necessity is immediate. For sufficiency, the chord splits the disk into two near-triangulations with triangular boundaries \(abc\) and \(acd\). Each prescribed boundary triangle uses three distinct colors. Apply the Four Color Theorem on each side and permute its colors to match the prescribed triangle. The resulting colorings agree on \(a,c\) and combine.

Hence only chordless outer cycles need further consideration.

---

## 3. An \(O(4^k n)\)-time algorithm

### 3.1. Peeling low-degree interior vertices

If an unprecolored vertex has degree at most three, every proper 4-coloring of the graph with that vertex deleted extends to it. Therefore repeatedly deleting such interior vertices preserves the answer.

For a simple near-triangulation, an interior vertex has degree at least three. Deleting an interior degree-three vertex replaces its three incident triangular faces by one triangular face, so the intermediate graphs remain near-triangulations with the same outer cycle.

The peeling can be performed in linear time using a queue. Let \(G_0\) be the result, and let
\[
X=\{v\in V(G_0)\setminus V(C):\deg_{G_0}(v)\ge5\},
\qquad k=|X|.
\]

The algorithm will enumerate the colors on \(X\). The remaining problem is handled by the following lemma.

### 3.2. A degree-feasible list-coloring lemma

**Lemma.** Let \(H\) have maximum degree at most four, and let
\[
L(v)\subseteq\{1,2,3,4\}
\]
satisfy
\[
|L(v)|\ge\deg_H(v)
\quad\text{for every }v.
\tag{4}
\]
Whether \(H\) has a proper \(L\)-coloring can be decided in linear time.

**Proof.** We treat connected components separately.

First, a useful greedy observation: if a connected graph \(Q\) satisfies (4) and some vertex \(r\) satisfies
\[
|L(r)|>\deg_Q(r),
\]
then \(Q\) is \(L\)-colorable. Root a spanning tree at \(r\) and color in reverse tree order. Every vertex other than \(r\) has an uncolored parent when processed, and \(r\) has the extra available color.

Now consider a 2-connected graph \(B\) that is neither complete nor an odd cycle, with lists satisfying (4).

- If some list is larger than the corresponding degree, use the greedy observation.
- Otherwise all lists have size equal to degree. If adjacent vertices \(u,v\) have different lists, orient the pair so that some color
  \[
  \gamma\in L(u)\setminus L(v)
  \]
  exists. Color \(u\) with \(\gamma\). Since \(B-u\) is connected, and \(v\) now has a list larger than its remaining degree, the greedy observation colors \(B-u\).
- If no adjacent lists differ, connectedness implies that all lists are the same set \(S\). Tightness then makes \(B\) \(|S|\)-regular. Brooks’ theorem gives a coloring using \(S\), because \(B\) is neither complete nor an odd cycle.

Consequently, if a connected component of \(H\) has a block \(B\) that is neither complete nor an odd cycle, that entire component is list-colorable. Indeed, first greedily color the vertices outside \(B\), in decreasing order of distance from \(B\). Each has an uncolored neighbor closer to \(B\). The remaining lists on \(B\) have size at least their degrees in \(B\), so the preceding argument applies.

It remains to handle components whose blocks are all complete graphs or odd cycles. Use dynamic programming on the block-cutvertex tree:

- A message from a block to its parent cutvertex records which of the four colors at that cutvertex extend through the block’s subtree.
- At a vertex, intersect its original list with the messages from its child blocks.
- A complete block has at most five vertices, since \(\Delta(H)\le4\), so all its assignments can be tested in constant time.
- For an odd-cycle block, fix the parent cutvertex’s color and run a four-state path dynamic program around the cycle. For allowed sets \(A_i\), the transition is
  \[
  D_i=\{t\in A_i:\text{ some }s\in D_{i-1}\text{ satisfies }s\ne t\},
  \]
  with the last color also required to differ from the fixed first color.
- An isolated vertex is feasible exactly when its list is nonempty.

These messages are exact by induction on the block-cutvertex tree. There are only four states per attachment, and the total size of all blocks is linear. Thus the procedure runs in linear time. \(\square\)

### 3.3. Enumerating the high-degree vertices

For each of the at most \(4^k\) assignments of colors to \(X\):

1. Combine it with \(\psi\), obtaining a coloring \(\chi\) of
   \[
   S=V(C)\cup X.
   \]
2. Discard the assignment if \(\chi\) is not proper on \(G_0[S]\). This also checks any chord of \(C\).
3. Let
   \[
   H=G_0-S.
   \]
   For \(v\in V(H)\), define
   \[
   L(v)=\{1,2,3,4\}\setminus
   \{\chi(w):w\in N_{G_0}(v)\cap S\}.
   \]

Every vertex of \(H\) has degree at most four in \(G_0\). Hence
\[
\begin{aligned}
|L(v)|
&\ge 4-|N_{G_0}(v)\cap S|\\
&=4-\deg_{G_0}(v)+\deg_H(v)\\
&\ge\deg_H(v).
\end{aligned}
\tag{5}
\]
The lemma therefore decides the remaining list-coloring instance in linear time.

An extension of \(\psi\) determines one enumerated coloring of \(X\), and its restriction to \(H\) is precisely a coloring from these lists. Conversely, a successful list-coloring combines with \(\chi\), and then extends back through all peeled vertices. Thus the algorithm is correct in both directions.

Since a near-triangulation has linearly many edges, the total running time is
\[
\boxed{O(4^k n).}
\]

This is polynomial when \(k=O(\log n)\), and linear when \(k=0\). In particular, if every original interior vertex has degree at most four, then \(k=0\).

---

## 4. An explicit parity criterion when \(k=0\)

The low-degree case admits a particularly simple geometric description.

**Proposition.** Suppose \(C\) is chordless and \(k=0\). Then, after peeling, \(G_0\) has the following form:

- its interior vertices form a path \(x_1,\ldots,x_t\), with \(t\ge1\);
- for a suitable cyclic ordering \(C=rpsq\), both \(p\) and \(q\) are adjacent to every vertex of the path
  \[
  r,x_1,\ldots,x_t,s;
  \]
- these are all the edges, apart from the edges of that path.

Thus \(G_0\) is a double fan over a path.

**Proof.** Every remaining interior vertex has degree four. Put
\[
H=G_0-V(C),\qquad |V(H)|=t.
\]

The graph \(H\) is connected. To see this, every bounded face contains an interior vertex, because \(C\) is a chordless 4-cycle. Two bounded faces sharing an internal edge share an interior endpoint. The adjacency graph of the bounded faces is connected, as follows by drawing curves inside the disk between face interiors. Hence all interior vertices belong to one component of \(H\).

Euler’s formula gives
\[
|E(G_0)|=3(t+4)-7=3t+5.
\]
Writing \(e_I=|E(H)|\) and \(e_B=|E(C,H)|\), we obtain
\[
e_I+e_B=3t+1,
\qquad
2e_I+e_B=4t.
\]
Therefore \(e_I=t-1\), so \(H\) is a tree.

At an interior degree-four vertex, consecutive neighbors in the cyclic order are adjacent. If three of its neighbors belonged to \(H\), two would be consecutive and would form a triangle with it in \(H\), contradicting that \(H\) is a tree. Thus \(\Delta(H)\le2\), and \(H\) is a path.

For \(t=1\), the graph is the 4-wheel, which has the asserted form.

For \(t\ge2\), the two triangular faces incident with each path edge have their third vertices on \(C\). At an internal path vertex, its two interior neighbors alternate in the cyclic order with its two boundary neighbors. Consequently, the same pair of boundary vertices, say \(p,q\), occurs along every path edge.

Each path end has one additional boundary neighbor, say \(r\) and \(s\). Every vertex of a chordless outer cycle has an interior neighbor: otherwise its two boundary edges would lie on a triangular face requiring an outer chord. Thus \(p,q,r,s\) are all four boundary vertices. The faces around the path ends give the boundary order \(rpsq\), and the claimed edge set follows from the degrees. \(\square\)

The extension criterion is now immediate.

- If \(\psi(p)=\psi(q)\), all vertices of the displayed path may use the other three colors. A path of length at least two can be colored from three colors with arbitrary prescribed endpoint colors, so extension always exists.
- If \(\psi(p)\ne\psi(q)\), the path must use the other two colors alternately. Its length is \(t+1\), so extension exists exactly when
  \[
  \boxed{\psi(r)=\psi(s)\quad\Longleftrightarrow\quad t\text{ is odd}.}
  \tag{6}
  \]

In particular, an alternating two-color boundary always extends in this class.

---

## 5. What is still difficult in the unrestricted case?

### At least three boundary types always extend

For a chordless outer 4-cycle, the Four Color Theorem gives
\[
A\lor B,\qquad A\lor C,\qquad C\lor D,\qquad B\lor D.
\tag{7}
\]

For example:

- identifying \(a,c\) through the outer face gives a loopless planar graph, so some coloring with \(a=c\) exists;
- adding the edge \(ac\) through the outer face gives a planar graph, so some coloring with \(a\ne c\) exists.

The other two statements follow similarly using \(b,d\).

There is also a Kempe-chain relation between the two groups
\[
\{A,D\}\quad\text{and}\quad\{B,C\}.
\tag{8}
\]
An extension of any type in either group can be changed to an extension of some type in the other group.

For types \(A\) and \(D\), consider the \(\{1,3\}\)-components containing \(a,c\) and the \(\{2,4\}\)-components containing \(b,d\). Both opposite pairs cannot be connected: this would give vertex-disjoint paths joining alternating boundary pairs in a disk. Swapping colors in a component belonging to a disconnected pair changes the boundary to type \(B\) or \(C\).

For type \(B=(1,2,1,3)\), use the color pairs \(\{2,3\}\) on \(b,d\) and \(\{1,4\}\) on \(a,c\). Again, both pairs cannot be connected. A swap on a disconnected pair gives type \(A\) or \(D\). Type \(C\) is symmetric.

The only pairs of simultaneously absent types not already excluded by (7) are \(\{A,D\}\) and \(\{B,C\}\). Relation (8) excludes these too. Therefore:

\[
\boxed{\text{For chordless }C,\text{ at least three of }A,B,C,D\text{ extend}.}
\tag{9}
\]

This guarantee does not identify whether the fourth type extends.

### A smallest alternating-boundary obstruction

Here is an explicit seven-vertex example showing that type \(A\) is genuinely nontrivial.

Take outer cycle \(abcd\), interior triangle \(pqr\), and additional edges
\[
ap,\ bp,\ bq,\ cq,\ cr,\ dr,\ ar.
\]
A plane embedding has bounded faces
\[
abp,\quad bpq,\quad bcq,\quad cqr,\quad
cdr,\quad dar,\quad arp,\quad pqr.
\]
Thus this is a near-triangulation with chordless outer cycle.

Prescribe
\[
\psi(a)=\psi(c)=1,\qquad
\psi(b)=\psi(d)=2.
\]
Each of \(p,q,r\) has boundary neighbors of both colors \(1\) and \(2\). Hence all three must use colors \(3,4\), which cannot properly color the triangle \(pqr\). The precoloring does not extend.

The interior degrees are \(4,4,5\), so this obstruction already occurs with \(k=1\). Seven vertices are minimal for a chordless alternating-boundary obstruction: with at most two interior vertices, their induced graph can be colored using the two colors absent from the boundary.

---

## 6. Remaining gap

The normalization shows that the alternating boundary problem contains the full difficulty. The parameterized algorithm handles a substantial restriction, but \(k\) can be linear in \(n\), even after peeling. Its running time therefore does not yield the requested general polynomial bound.

Likewise, the Four Color Theorem and Kempe changes ensure that at least three boundary types extend, but provide no criterion for deciding whether the remaining type does.

Thus the arguments above give exact reductions, a fully specified parameterized algorithm, and a structural special-case solution—not a resolution of the unrestricted problem.