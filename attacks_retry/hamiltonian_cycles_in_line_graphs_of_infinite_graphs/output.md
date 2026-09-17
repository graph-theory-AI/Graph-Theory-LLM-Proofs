```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every infinite connected locally finite H, I prove that L(H □ K2) has a Hamilton circle, yielding exact-4-edge-connected special cases.",
  "would_publish": false,
  "caveats": "Neither general conjecture is resolved; novelty and an updated literature status are not claimed."
}
```

# A prism theorem and consequences at connectivity four

I do not resolve either conjecture. I establish the following sufficient condition.

**Theorem 1 (prisms).**  
Let \(H\) be an infinite connected locally finite graph. Then
\[
L(H\square K_2)
\]
has a Hamilton circle.

No connectivity assumption beyond connectedness is needed for this theorem. Its consequences include:

- exact-\(4\)-edge-connected, \(5\)-regular graphs \(T\square C_4\), where \(T\) is an infinite \(3\)-regular tree;
- one-ended, exact-\(4\)-edge-connected examples with infinitely many odd-degree vertices;
- examples for Part 2 whose underlying graphs have bridges.

The first family cannot satisfy the finite-bag, two-spanning-tree hypothesis in the supplied attempt: none of its finite subgraphs on at least two vertices contains two edge-disjoint spanning trees.

The proof uses the tree-of-cycles idea from that attempt, but the local construction is different, and the gluing—including its behavior at ends—is proved below. All graphs are simple.

## 1. A spanning tree that preserves the ends

We first give the spanning-tree fact needed in the construction.

**Lemma 2.**  
Every connected locally finite graph \(H\) has a rooted spanning tree \(T\) such that the endpoints of every edge of \(H\) are comparable in the ancestor order of \(T\). Moreover, the inclusion \(T\subseteq H\) induces a homeomorphism of end spaces.

**Proof.**  
A connected locally finite graph is countable. Enumerate its vertices and construct finite rooted tree subgraphs successively.

Maintain the following conditions:

1. endpoints of every \(H\)-edge with both endpoints in the current tree are comparable;
2. for every component \(D\) outside the current tree, its neighbors in the tree lie on one root-to-vertex path.

Start with a single root. Let \(v\) be the first enumerated vertex not yet included, and let \(D\) be its component outside the current tree. Let \(x\) be the deepest neighbor of \(D\) in the current tree. Add a finite \(x\)-\(v\) path whose other vertices lie in \(D\).

All old attachments of \(D\) are ancestors of \(x\). The added vertices form one chain below \(x\), so both conditions persist. The union is a spanning tree \(T\) with the asserted comparability property.

Because \(T\) is locally finite, its sets
\[
S_n=\{v:d_T(v,\text{root})\le n\}
\]
are finite. The components of \(H-S_n\) are exactly the vertex sets of the components of \(T-S_n\): different such tree components have incomparable vertices and hence no \(H\)-edge between them.

Nested components outside the \(S_n\) determine a unique rooted ray of \(T\), and conversely. These finite separators therefore give the claimed homeomorphism of end spaces. \(\square\)

Put
\[
P=H\square K_2,
\qquad V(P)=V(H)\times\{0,1\}.
\]
Fix a tree \(T\) supplied by Lemma 2.

For later use, define
\[
F_n=\{e\in E(P):e\text{ has an endpoint in }S_n\times\{0,1\}\}.
\]
Regard \(F_n\) as a finite vertex set of \(L(P)\). These sets exhaust \(V(L(P))\). The components of \(L(P)-F_n\) are precisely
\[
L(H[U]\square K_2),
\]
where \(U\) ranges over the components of \(T-S_n\). Each is connected, including when \(U\) is a singleton, because its prism contains a rung.

Consequently,
\[
\Omega(T)\cong\Omega(H)\cong\Omega(P)\cong\Omega(L(P)).
\tag{1}
\]

## 2. Finite local cycles

We now build a finite abstract cycle \(C_t\) for each \(t\in V(T)\). Its vertices will be edge-labels of \(P\), hence vertices of \(L(P)\). Some cycle edges will temporarily be *virtual*: they need not be edges of \(L(P)\).

Let the neighbors of \(t\) in \(T\) be
\[
u_1,\ldots,u_d.
\]
Here \(d\ge1\). Write
\[
a_j=(t,0)(u_j,0),\qquad
b_j=(t,1)(u_j,1),
\]
and let
\[
r_t=(t,0)(t,1)
\]
be the rung at \(t\).

Form the cyclic list
\[
B_1B_2\cdots B_d\,r_t,
\qquad
B_j=
\begin{cases}
(a_j,b_j),&j\text{ odd},\\
(b_j,a_j),&j\text{ even}.
\end{cases}
\tag{2}
\]
Declare the adjacency within each block \(B_j\) virtual.

Every other adjacency in (2) is genuine in \(L(P)\):

- between consecutive blocks, the two labels meet at \((t,0)\) or at \((t,1)\);
- the last block and the first block are joined through the rung label \(r_t\).

This also handles \(d=1\): the local cycle is the abstract triangle on \(a_1,b_1,r_t\), with \(a_1b_1\) virtual.

There is a genuine transition through each of \((t,0)\) and \((t,1)\). For example, \(r_t,a_1\) meet at \((t,0)\). At \((t,1)\), use \(b_1,r_t\) if \(d=1\), and \(b_1,b_2\) otherwise.

### Incorporating all non-tree edges

For each edge of \(P\) arising from an edge of \(H-E(T)\), assign its label to one of its endpoints, once and for all. Each vertex receives finitely many assignments.

For \(i\in\{0,1\}\), insert all labels assigned to \((t,i)\) into a genuine transition of (2) through \((t,i)\). Every inserted label shares \((t,i)\) with its predecessor and successor. Thus all new adjacencies are genuine.

Denote the resulting finite abstract cycle by \(C_t\). It has the following properties.

1. Every nonvirtual edge of \(C_t\) is an edge of \(L(P)\).
2. Its virtual edges have pairwise disjoint endpoints.
3. If \(tu\in E(T)\), then \(C_t\) and \(C_u\) share exactly the two labels
   \[
   (t,0)(u,0),\quad (t,1)(u,1),
   \]
   which are the endpoints of the corresponding virtual edge in each cycle.
4. Cycles indexed by nonadjacent tree vertices are disjoint.
5. Every vertex of \(L(P)\) occurs: a tree-edge label occurs in its two endpoint cycles, while every other label occurs in exactly one cycle.

These properties are the entire combinatorial input to the gluing.

## 3. Gluing the cycles, with control at every end

For every \(tu\in E(T)\), identify the equally labelled vertices of \(C_t,C_u\), and delete their two copies of the corresponding virtual edge.

Over a finite subtree, this produces one abstract cycle. Indeed, adjoining a new local cycle replaces one virtual edge by the complementary path around that local cycle.

Performing all gluings produces a spanning \(2\)-regular subgraph \(Q\) of \(L(P)\):

- an unshared label retains its two genuine incident edges from its local cycle;
- a shared label receives one genuine incident edge from each endpoint cycle.

Those incident edges are distinct. More generally, genuine edges from different local cycles cannot coincide: two local cycles share only the endpoints of a virtual edge, and that edge is not genuine.

A spanning \(2\)-regular subgraph alone does **not** prove Hamiltonicity in an infinite graph. We next show directly that its closure is a circle.

### 3.1. A parameter circle

Root \(T\). Glue the local cycles at distance at most \(n\) from the root, leaving virtual edges toward unprocessed children. Call the resulting finite abstract cycle \(D_n\).

Parametrize \(D_0\) by \(S^1\), assigning a nondegenerate closed parameter interval to each cycle edge. When a virtual edge is replaced by a path, subdivide its parameter interval equally among the edges of that path.

The replacement path has at least two edges. Thus every new virtual interval has at most half the length of its parent interval. Furthermore, every new virtual interval lies strictly inside its parent interval: in the new local cycle, the child virtual edges have endpoints disjoint from those of the parent virtual edge.

It follows that:

- every genuine edge receives a fixed nondegenerate parameter interval;
- every vertex receives a unique parameter point at a finite stage;
- a parameter point not accounted for by genuine edges or vertices lies in a nested sequence of virtual intervals;
- such a nested sequence corresponds to a rooted ray of \(T\);
- its intervals have lengths tending to zero, so their intersection is one point.

Conversely, every rooted ray of \(T\) gives one such remaining point. Distinct rays eventually enter disjoint virtual intervals and hence give distinct points.

Using (1), map the point associated with a rooted ray to the corresponding end of \(L(P)\). Parametrize genuine edges by their assigned intervals. This defines a bijection
\[
f:S^1\longrightarrow Q\cup\Omega(L(P)).
\tag{3}
\]

### 3.2. Continuity

Continuity at ordinary edge points and vertices follows from the finite-stage construction: eventually both genuine incident edges at a vertex are fixed.

Consider a remaining parameter point \(p\), associated with a rooted ray
\[
t_0t_1t_2\cdots
\]
and an end \(\omega\).

Fix \(F_m\), and let \(C_m\) be the component of \(L(P)-F_m\) containing \(\omega\). Let \(A_m\) be the finite set of projections to \(V(H)\) of all endpoints of edges in \(F_m\).

Choose \(k\) large enough that the descendant subtree \(U_k\) rooted at \(t_k\)

- is disjoint from \(A_m\), and
- lies in the component of \(T-S_m\) corresponding to \(\omega\).

Let \(I_k\) be the virtual interval toward \(U_k\). Every edge-label occurring in its eventual replacement has an endpoint in \(U_k\times\{0,1\}\), including the two boundary labels. Therefore none belongs to \(F_m\). All these labels lie in \(C_m\). The ends mapped from points of \(I_k\) are also ends belonging to that component.

Hence \(f(I_k)\) lies in the standard end-neighborhood determined by \(C_m\). Since the next virtual interval lies strictly inside \(I_k\), the point \(p\) lies in the interior of \(I_k\). This proves continuity at \(p\).

Thus (3) is continuous. Since \(S^1\) is compact and the Freudenthal compactification is Hausdorff, it is a homeomorphism onto its image. The image contains every vertex of \(L(P)\), proving Theorem 1. \(\square\)

For finite connected \(H\) with at least two vertices, the same construction terminates after finitely many gluings and gives a Hamilton cycle.

## 4. When the prism is \(4\)-edge-connected

The prism theorem supplies examples for the conjecture whenever its root graph meets the requisite connectivity. The following elementary criterion is useful.

**Lemma 3.**  
If \(H\) is infinite, \(2\)-edge-connected, and has minimum degree at least three, then \(H\square K_2\) is \(4\)-edge-connected.

**Proof.**  
For a nonempty proper subset \(X\subset V(H\square K_2)\), put
\[
A=\{v:(v,0)\in X\},\qquad
B=\{v:(v,1)\in X\}.
\]
Then
\[
|\delta_{H\square K_2}(X)|
=
|\delta_H(A)|+|\delta_H(B)|+|A\triangle B|,
\tag{4}
\]
with infinite cut sizes allowed.

If both \(A,B\) are nonempty and proper, the first two terms already total at least four.

If exactly one is nontrivial, taking complements and exchanging the two layers reduces to \(B=\varnothing\). The right side becomes
\[
|\delta_H(A)|+|A|.
\]
This is at least four if \(|A|\ge2\). If \(A\) is a singleton, it is at least \(3+1\).

If both are trivial, the only nontrivial choice for \(X\) separates the two complete layers and cuts infinitely many rungs. Thus every cut has size at least four. \(\square\)

There are two useful ways to obtain equality:

- if \(H\) has a vertex of degree three, the prism has a vertex of degree four;
- if \(H\) has a cut of size two, taking both copies of one shore in (4) gives a prism cut of size four.

### 4.1. Exact connectivity four with all degrees odd

Let \(T\) be an infinite locally finite tree. Every edge of \(T\square K_2\) lies on a \(4\)-cycle, so this graph is \(2\)-edge-connected. The two edges above any tree edge form a cut of size two.

If \(\delta(T)\ge2\), then
\[
\delta(T\square K_2)\ge3.
\]
Applying Lemma 3 to \(H=T\square K_2\), and using
\[
(T\square K_2)\square K_2\cong T\square C_4,
\]
gives the following.

**Corollary 4.**  
For every infinite locally finite tree \(T\),
\[
L(T\square C_4)
\]
has a Hamilton circle. If \(\delta(T)\ge2\), then \(T\square C_4\) is exactly \(4\)-edge-connected.

In particular, if \(T\) is an infinite \(3\)-regular tree, then \(T\square C_4\) is \(5\)-regular and exactly \(4\)-edge-connected.

This last family is outside both sufficient conditions stated in the supplied attempt. Its degrees are odd, and its finite subgraphs never contain two edge-disjoint spanning trees.

To verify the latter assertion, take a finite vertex set \(S\) of size \(n\ge2\) in \(T\square C_4\). Let

- \(p\) be the number of its nonempty \(T\)-layers, so \(1\le p\le4\);
- \(q\) be the number of nonempty \(C_4\)-fibres that \(S\) meets without containing the entire fibre.

The edges in the \(T\)-direction form four forests, contributing at most \(n-p\) edges. A proper nonempty induced subgraph of \(C_4\) is a forest, so the edges in the \(C_4\)-direction contribute at most \(n-q\). Hence
\[
|E((T\square C_4)[S])|\le 2n-p-q.
\]
For \(n\ge2\), one has \(p+q\ge3\):

- if \(p\ge3\), this is immediate;
- if \(p=2\), at least one fibre is partial;
- if \(p=1\), every occupied fibre is partial, and \(q=n\ge2\).

Consequently,
\[
|E((T\square C_4)[S])|\le 2n-3.
\tag{5}
\]
Two edge-disjoint spanning trees would require \(2n-2\) edges, contradicting (5).

Thus the prism construction handles a threshold-four family for which the earlier finite-piece tree-packing hypothesis is impossible, regardless of how finite bags are chosen.

### 4.2. A one-ended example with infinitely many odd-degree vertices

Let \(H\) be the square grid on \(\mathbb Z^2\) with one edge deleted.

The square grid is \(4\)-edge-connected. Indeed, after deleting finitely many edges, all vertices outside a sufficiently large box remain connected; any other component is finite, and every nonempty finite vertex set has at least four boundary edges, in the four coordinate directions.

Therefore \(H\) is \(3\)-edge-connected. Its two vertices incident with the deleted edge have degree three, and all other vertices have degree four. It is also one-ended.

It follows that
\[
P=H\square K_2
\]
is one-ended and exactly \(4\)-edge-connected. Four vertices of \(P\) have degree four, and all others have degree five. Nevertheless, \(L(P)\) has a Hamilton circle by Theorem 1; equivalently in this one-ended case, it has a spanning double ray.

## 5. Consequences for Part 2, including underlying graphs with bridges

If an infinite graph \(P\) is \(4\)-edge-connected, then \(L(P)\) is \(4\)-connected: deleting at most three vertices of \(L(P)\) means deleting at most three edges of \(P\), leaving a connected graph and hence a connected line graph.

For the family \(P=T\square C_4\) with \(T\) an infinite \(3\)-regular tree, the line graph is **exactly** \(4\)-connected. The four labels corresponding to edges above a tree edge form a vertex cut of \(L(P)\).

There is also a direct extension beyond Part 1.

**Corollary 5.**  
Let \(P=H\square K_2\) satisfy Lemma 3. Attach finitely many new leaves at each vertex of \(P\), and call the resulting graph \(G\). Then \(L(G)\) is \(4\)-connected and has a Hamilton circle.

**Proof.**  
For Hamiltonicity, insert each pendant-edge label into a local transition through its attachment vertex in the construction of \(C_t\). Every such transition exists, and local finiteness ensures that each local cycle remains finite. Perform these insertions before gluing.

The pendant attachments create no new ends. Equivalently, the finite cuts used in the proof can be enlarged to include pendant labels attached to the corresponding finite sets of core vertices. The same parametrization and continuity argument therefore gives a Hamilton circle in \(L(G)\).

For connectivity, delete at most three edge-labels. The surviving core edges form a connected line graph because \(P\) is \(4\)-edge-connected. Every surviving pendant edge is adjacent to a surviving core edge at its attachment vertex: that vertex originally had at least four core edges. Thus the whole remaining line graph is connected. \(\square\)

If any leaf is attached, \(G\) has a bridge. These are therefore genuine special cases of Part 2 not covered by its implication from Part 1.

## 6. What remains unproved

The construction relies on a specific resource: two vertices in each fibre, a rung joining them, and two compatible tree-edge copies. These provide paired virtual ports whose nested intervals visit every end exactly once.

Neither \(4\)-edge-connectivity of an arbitrary graph nor \(4\)-connectivity of its line graph has been shown here to supply that structure. In particular:

- the proof does not produce the required end-controlled scaffold in an arbitrary \(4\)-edge-connected locally finite graph;
- it does not settle arbitrary one-ended graphs at connectivity four;
- it leaves general finite \(4\)-connected line graphs untouched.

Accordingly, this is a self-contained sufficient-condition result, not a resolution of either conjecture. I do not claim novelty for the prism theorem or an independently verified update of the literature status.