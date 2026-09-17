```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A constructive Cartesian-product closure theorem gives Hamiltonian extensions for an infinite family of noncompletable matchings using every coordinate direction.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved, and novelty of the closure theorem has not been checked."
}
```

# 1. Partial result

I set aside the signed-minor strategy from the previous attempt. The result below applies to matchings that **cannot** be completed to perfect matchings. The only item reused from that attempt is its elementary \(Q_3\) example, which is verified directly below.

For a matching \(A\), let \(U(A)\) denote its set of uncovered vertices.

Identify
\[
Q_{a+b}=Q_a\square Q_b.
\]
For matchings \(A\subseteq E(Q_a)\) and \(B\subseteq E(Q_b)\), define the following ordered product:
\[
\begin{aligned}
A\star B={}&
\bigl\{(x,z)(y,z):xy\in A,\ z\in V(Q_b)\bigr\}\\
&\cup
\bigl\{(x,z)(x,w):x\in U(A),\ zw\in B\bigr\}.
\end{aligned} \tag{1}
\]
Thus we put a copy of \(A\) in every \(Q_a\)-layer, and put a copy of \(B\) in each remaining \(Q_b\)-fiber.

This is a matching, and
\[
U(A\star B)=U(A)\times U(B). \tag{2}
\]

**Theorem — Product closure.**  
Let \(a,b\ge 2\). Suppose \(A\) and \(B\) are contained in Hamiltonian cycles of \(Q_a\) and \(Q_b\), respectively. If \(B\) is not perfect, then \(A\star B\) is contained in a Hamiltonian cycle of \(Q_{a+b}\).

The proof of this case is self-contained and constructive. If \(B\) is perfect, then \(A\star B\) is perfect, so that case follows from Fink’s perfect-matching theorem quoted in the question.

One unconditional consequence will be:

**Corollary.** For every \(t\ge 1\), there is an explicitly specified matching \(M_t\) of \(Q_{3t}\) such that:

1. \(M_t\) extends to a Hamiltonian cycle;
2. \(M_t\) has no perfect-matching completion;
3. \(M_t\) uses all \(3t\) directions; and
4. 
   \[
   |M_t|=2^{3t-1}-2^{t-1}.
   \]

For \(t=2\), this gives a \(30\)-edge matching of \(Q_6\), using all six directions and having no perfect completion.

# 2. A cycle-product construction

Choose Hamiltonian cycles
\[
C\subseteq Q_a,\qquad D\subseteq Q_b
\]
containing \(A\) and \(B\), respectively. Write
\[
n=2^a,\qquad h=2^b,\qquad m=|A|.
\]
It is enough to work inside \(C\square D\).

Orient both cycles. Color the edges of \(D\) alternately with colors \(0\) and \(1\).

## 2.1. Partitioning the first cycle into blocks

Partition the vertices of \(C\), in cyclic order, as follows:

- each edge of \(A\), together with its two endpoints, is a two-vertex block;
- each vertex uncovered by \(A\) is a one-vertex block.

There are
\[
L=m+(n-2m)=n-m \tag{3}
\]
blocks.

Between consecutive blocks there is one edge of \(C\), necessarily outside \(A\). Call these the **boundary edges**.

We will associate an edge \(f_s\in E(D)\) with each boundary \(s\). Across that boundary, we initially use the two copies of the boundary edge situated at the two endpoints of \(f_s\).

The construction inside a block is determined by its incoming and outgoing boundary edges, say \(f,g\in E(D)\).

## 2.2. A one-vertex block

Here the block is one copy of \(D\), carrying the prescribed matching \(B\).

If \(f\ne g\) and \(f,g\notin B\), delete \(f\) and \(g\) from \(D\). This leaves two vertex-disjoint paths covering the block. One path is allowed to be a single vertex when \(f\) and \(g\) are adjacent.

Label the tail and head of every oriented edge of \(D\) by \(0\) and \(1\), respectively. The two paths pair the boundary ports as
\[
0\longleftrightarrow 1,\qquad
1\longleftrightarrow 0. \tag{4}
\]
Indeed, deleting oriented edges \(f=(x_0,x_1)\) and \(g=(y_0,y_1)\) leaves paths joining \(x_1\) to \(y_0\), and \(y_1\) to \(x_0\).

## 2.3. A two-vertex block

This block is a prism \(K_2\square D\). Its two columns correspond to the two endpoints of an edge of \(A\). Every rung of the prism is prescribed by \(A\star B\).

Suppose \(f\) and \(g\) have opposite alternating colors in \(D\). There is a Hamiltonian cycle of this prism containing:

- all rungs;
- the copy of \(f\) in the left column; and
- the copy of \(g\) in the right column.

To see this explicitly, put each edge of \(D\) into one column according to its alternating color, choosing the assignment so that \(f\) lies on the left. Add every rung. At each vertex of \(D\), its two incident cycle edges lie in opposite columns, so the resulting graph is one Hamiltonian cycle.

Orient this prism cycle so that its copies of edges of \(D\) follow the orientation of \(D\). Delete the specified copies of \(f\) and \(g\). Again, the resulting two spanning paths have the port pairing (4).

Consequently, every block in our construction acts as a swap of its two port labels. The edges connecting consecutive blocks preserve those labels.

# 3. Proof of product closure

Assume throughout this section that \(B\) is not perfect.

We treat the two possible parities of \(L\).

## 3.1. Even \(L\): construct two cycles, then merge them

Choose a vertex \(z\) uncovered by \(B\). Let
\[
p=z^-z,\qquad q=zz^+
\]
be its two incident edges in the oriented cycle \(D\). Both lie outside \(B\), and they have opposite alternating colors.

Assign \(p,q,p,q,\ldots\) to the boundaries in cyclic order. Since \(L\) is even, every block has one incident boundary assigned \(p\) and the other assigned \(q\). Thus all the local constructions in Section 2 apply.

In each block, one of the two local paths consists exactly of the block’s vertices at the \(D\)-coordinate \(z\):

- in a one-vertex block, it is a single vertex;
- in a two-vertex block, it is the rung at \(z\).

These short paths, joined across the boundaries, form precisely
\[
C\square\{z\}.
\]
The other path in every block joins to the corresponding paths in the neighboring blocks, forming one further cycle through all remaining vertices. We have therefore constructed a spanning two-factor with exactly two cycles, containing \(A\star B\).

Now choose any boundary. Suppose its assigned edge of \(D\) is \(zz'\), and its edge of \(C\) is \(xy\). The two-factor contains
\[
(x,z)(y,z)
\quad\text{and}\quad
(x,z')(y,z'),
\]
one on each of its two cycles.

Neither edge is prescribed: \(xy\) is a boundary edge and hence is outside \(A\). Replace them by
\[
(x,z)(x,z')
\quad\text{and}\quad
(y,z)(y,z').
\]
These latter edges were deleted in the local block constructions, so they are not already present.

This square switch joins the two cycles into one Hamiltonian cycle and removes no edge of \(A\star B\).

## 3.2. Odd \(L\): arrange one connected system of paths

Because \(n\) is divisible by \(4\), a perfect matching of \(C\) has even size. From \(L=n-m\), odd \(L\) implies odd \(m\), so \(A\) is not perfect. Hence there is a one-vertex block. Index the blocks cyclically so that this is block \(0\).

The free edges \(E(D)\setminus B\) meet both alternating color classes. Otherwise \(B\) would contain an entire color class, making \(B\) perfect.

Moreover,
\[
|E(D)\setminus B|
=h-|B|
\ge \frac h2+1
\ge 3.
\]
We can therefore choose distinct free edges \(p,p'\) of one color, say color \(0\), and a free edge \(q\) of color \(1\).

For boundaries \(0,\ldots,L-2\), assign
\[
f_s=
\begin{cases}
p,&s\text{ even},\\
q,&s\text{ odd},
\end{cases}
\]
and assign
\[
f_{L-1}=p'.
\]
Because \(L\) is odd, every block other than block \(0\) has incident boundary edges of opposite colors. Block \(0\) has the distinct free edges \(p'\) and \(p\).

Thus every block admits the two-path construction of Section 2. Each block swaps the port labels, and each boundary preserves them. Going once around all \(L\) blocks therefore swaps the labels, since \(L\) is odd.

It follows that a traversal goes through both local paths of every block before returning to its starting point. The resulting spanning two-regular graph is consequently connected: it is one Hamiltonian cycle.

No prescribed edge was removed. This proves the theorem. \(\square\)

# 4. An explicit family with no perfect completions

Let
\[
N=\{001\,011,\;010\,110,\;100\,101\}\subseteq E(Q_3).
\]
This matching leaves exactly
\[
U=\{000,111\}
\]
uncovered. These two vertices are nonadjacent, so \(N\) has no perfect-matching completion.

Nevertheless,
\[
000,\ 001,\ 011,\ 010,\ 110,\ 111,\ 101,\ 100,\ 000 \tag{5}
\]
is a Hamiltonian cycle containing \(N\): consecutive strings differ in one coordinate, every vertex occurs once, and all three displayed matching edges occur.

Define
\[
M_1=N,\qquad M_t=N\star M_{t-1}\quad(t\ge2). \tag{6}
\]
By product closure and induction, every \(M_t\) extends to a Hamiltonian cycle. This application uses only the self-contained, nonperfect case of the theorem.

## 4.1. An explicit description without recursion

Write a vertex of \(Q_{3t}\) as \(t\) consecutive three-bit blocks.

For a vertex not in \(U^t\), find its first block that is not \(000\) or \(111\). Match it by applying \(N\) in that block and leaving all other blocks unchanged.

Vertices of \(U^t\) remain uncovered. Thus
\[
U(M_t)=U^t,\qquad |U(M_t)|=2^t,
\]
and
\[
|M_t|
=\frac{2^{3t}-2^t}{2}
=2^{3t-1}-2^{t-1}. \tag{7}
\]

Any two distinct vertices of \(U^t\) differ in at least one entire three-bit block, so their Hamming distance is at least \(3\). The uncovered vertices therefore induce an edgeless graph. A perfect matching containing \(M_t\) would have to match these vertices among themselves, which is impossible.

Finally, \(N\) uses each of the three directions exactly once. For a direction in block \(j\), its number of occurrences in \(M_t\) is
\[
2^{j-1}8^{t-j}>0. \tag{8}
\]
Hence \(M_t\) uses all \(3t\) directions.

For example, \(M_2\subseteq Q_6\) consists of:

- a copy of \(N\) in each of the eight first-factor layers; and
- a copy of \(N\) in each second-factor fiber whose first coordinate is \(000\) or \(111\).

It has \(30\) edges and leaves
\[
000000,\quad 000111,\quad 111000,\quad 111111
\]
uncovered. It uses the first three directions eight times each and the last three directions twice each.

# 5. What remains unresolved

The product-closure theorem is a genuine special-case result, not a proof of the full conjecture. It requires the strong structure in (1).

An arbitrary matching need not admit that structure: edges lying in different layers can project to edges sharing an endpoint, and edges in the other factor can occur at incompatible first-factor vertices. The construction does not handle those interactions.

Thus the general Ruskey–Savage question remains unresolved by this argument. The progress here is a complete constructive closure theorem and an explicit infinite family beyond both perfect-matching completion and a bounded number of directions. No novelty claim is made.