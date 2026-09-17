```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every triangle-free graph with no induced 6-cycle and at most two vertices of degree at least four is 3-colourable.",
  "would_publish": false,
  "caveats": "This settles only a restricted case; novelty has not been checked, and the full ternary-graph conjecture is not resolved."
}
```

## 1. Statement of the partial result

All graphs below are finite and simple. A graph is **ternary** if it has no induced cycle whose length is divisible by three.

I do not obtain a proof or counterexample to the full conjecture. The following special case can, however, be proved using only the exclusion of triangles and induced 6-cycles.

**Theorem.** Let \(G\) be triangle-free and contain no induced \(C_6\). If at most two vertices of \(G\) have degree at least four, then \(G\) is 3-colourable.

Consequently, a vertex-minimal counterexample to the ternary-graph conjecture must have minimum degree at least three and **at least three vertices of degree at least four**.

The proof identifies a concrete obstruction: two endblocks of a suitable list-colouring obstruction produce an induced 6-cycle.

## 2. List-colouring preliminaries

For a graph \(Q\), a list assignment \(L\) assigns each vertex \(v\) a set \(L(v)\) of permitted colours. An \(L\)-colouring is a proper colouring choosing a colour from each list.

We need the following elementary form of the degree-list-colouring argument. Its proof uses only greedy colouring and the standard subcubic case of Brooks’ theorem.

**Lemma.** Suppose \(Q\) is connected and
\[
|L(v)|\ge d_Q(v)\qquad(v\in V(Q)).
\]

1. If the inequality is strict at some vertex, then \(Q\) is \(L\)-colourable.
2. If \(u\) is not a cutvertex, \(uv\in E(Q)\), and
   \[
   L(u)\setminus L(v)\ne\varnothing,
   \]
   then \(Q\) is \(L\)-colourable.
3. If \(Q\) is triangle-free, has maximum degree at most three, and is not \(L\)-colourable, then every block with at least two vertices is an edge or an odd cycle.

**Proof.**

For part 1, take a spanning tree rooted at a vertex \(r\) where the inequality is strict. Colour in reverse tree order. Every vertex other than \(r\) has an uncoloured parent when it is coloured; the root has more available colours initially than it has neighbours.

For part 2, colour \(u\) with a colour
\[
c\in L(u)\setminus L(v).
\]
Since \(Q-u\) is connected, take a spanning tree of \(Q-u\) rooted at \(v\), and again colour in reverse tree order. At the final vertex \(v\), the colour on its neighbour \(u\) does not belong to \(L(v)\), so at most \(d_Q(v)-1\) colours from \(L(v)\) are forbidden.

For part 3, suppose that \(Q\) has a block \(B\) that is neither an edge nor an odd cycle. Thus \(B\) is 2-connected.

First colour \(V(Q)\setminus V(B)\) greedily towards \(B\): order those vertices by nonincreasing distance from \(B\). Every vertex has an uncoloured neighbour closer to \(B\). After this, the residual lists \(M\) on \(B\) satisfy
\[
|M(v)|\ge d_B(v).
\]

If these residual lists are not all identical, there are adjacent vertices \(x,y\) such that, after exchanging their names if necessary,
\[
M(x)\setminus M(y)\ne\varnothing.
\]
Since \(B-x\) is connected, part 2 colours \(B\).

If the lists are all the same set \(A\), then \(|A|\ge\Delta(B)\). If \(\Delta(B)=2\), the block is an even cycle and is 2-colourable. If \(\Delta(B)=3\), Brooks’ theorem makes \(B\) 3-colourable: the exceptional graph \(K_4\) is excluded by triangle-freeness. Thus \(B\), and hence \(Q\), is \(L\)-colourable, a contradiction. \(\square\)

## 3. Proof of the theorem

Put
\[
S=\{v\in V(G):d_G(v)\ge4\},
\]
so \(|S|\le2\).

Precolour \(S\) as follows:

- if \(S\) is independent, give every vertex of \(S\) colour \(1\);
- if \(S=\{a,b\}\) and \(ab\in E(G)\), give \(a\) colour \(1\) and \(b\) colour \(2\).

Let \(H=G-S\), and give each \(v\in V(H)\) the list
\[
L(v)=\{1,2,3\}\setminus
\{\text{colours assigned to vertices in }N_G(v)\cap S\}.
\]
Since \(d_G(v)\le3\),
\[
|L(v)|\ge 3-|N_G(v)\cap S|
          \ge d_H(v).
\tag{1}
\]

Suppose some connected component \(Q\) of \(H\) is not \(L\)-colourable. By part 1 of the lemma, equality must hold in (1) at every vertex of \(Q\).

We claim that every \(v\in V(Q)\) satisfies
\[
d_G(v)=3,\qquad |N_G(v)\cap S|\le1,\qquad d_Q(v)\ge2.
\tag{2}
\]

Indeed:

- If \(S\) is independent and \(v\) has two neighbours in \(S\), then \(|L(v)|=2\), while \(d_Q(v)\le1\), giving a strict inequality.
- If \(S\) consists of an edge, no vertex has two neighbours in \(S\), by triangle-freeness.
- Once \(v\) has at most one neighbour in \(S\), equality in (1) forces \(d_G(v)=3\).

This proves (2).

By part 3 of the lemma, every block of \(Q\) is an edge or an odd cycle. Since \(\delta(Q)\ge2\), \(Q\) cannot be a single vertex or a single edge.

### The case in which \(Q\) is one block

Then \(Q\) is an odd cycle. Every vertex of \(Q\) has degree two in \(Q\), and therefore, by (2), has exactly one neighbour in \(S\).

Adjacent vertices of \(Q\) cannot have the same neighbour in \(S\), because that would create a triangle. Thus assigning to each vertex of \(Q\) its unique neighbour in \(S\) gives a proper colouring of an odd cycle with at most two labels. This is impossible.

Hence \(Q\) has more than one block.

### Endblocks of \(Q\)

The block-cutvertex tree of \(Q\) has at least two endblocks. An endblock cannot be an edge, since its non-cutvertex endpoint would have degree one in \(Q\). Therefore every endblock is an odd cycle, of length at least five.

Let \(B\) be an endblock and \(z\) its unique cutvertex. Every vertex of \(B-z\) has exactly one neighbour in \(S\). Along the path \(B-z\), consecutive vertices have different neighbours in \(S\), again by triangle-freeness.

It follows that \(S=\{a,b\}\), and these neighbours alternate between \(a\) and \(b\).

We now distinguish whether \(a\) and \(b\) are adjacent.

### Case 1: \(ab\in E(G)\)

Choose adjacent vertices \(u,v\) of \(B-z\) whose neighbours in \(S\) are \(a,b\), respectively. Their lists are
\[
L(u)=\{2,3\},\qquad L(v)=\{1,3\}.
\]
The vertex \(u\) is not a cutvertex of \(Q\), and
\[
2\in L(u)\setminus L(v).
\]
Part 2 of the lemma makes \(Q\) \(L\)-colourable, a contradiction.

### Case 2: \(ab\notin E(G)\)

Take two distinct endblocks \(B,B'\). Choose adjacent non-cutvertices \(u,v\) in \(B\) and \(u',v'\) in \(B'\) such that
\[
N_G(u)\cap S=N_G(u')\cap S=\{a\},
\]
and
\[
N_G(v)\cap S=N_G(v')\cap S=\{b\}.
\]

There are no edges between the selected non-cutvertices of distinct endblocks. Consequently,
\[
a-u-v-b-v'-u'-a
\]
is an induced 6-cycle:

- its six displayed edges exist;
- \(ab\) is absent;
- each of \(u,v,u',v'\) has only its specified neighbour in \(S\);
- among these four vertices, the only edges are \(uv\) and \(u'v'\).

This contradicts the hypothesis that \(G\) has no induced \(C_6\).

Both cases are impossible. Every component of \(H\) is therefore \(L\)-colourable, and these colourings extend the precolouring of \(S\). Thus \(G\) is 3-colourable. \(\square\)

## 4. Consequences for a counterexample search

### A restriction on a minimal counterexample

Let \(G\) be vertex-minimal among ternary graphs that are not 3-colourable. Then:

1. Every \(G-v\) is 3-colourable, so \(\chi(G)=4\).
2. Every vertex has degree at least three; otherwise a colouring of \(G-v\) extends to \(v\).
3. By the theorem, at least three vertices have degree at least four.

Here vertex deletion is important: ternarity is inherited by induced subgraphs, but not necessarily by edge-deleted subgraphs.

### A slightly broader applicable class

Repeatedly delete vertices of current degree at most two, obtaining the 3-core \(K\). If \(K\) has at most two vertices of degree at least four, then every ternary \(G\) is 3-colourable: colour \(K\) by the theorem and restore the deleted vertices in reverse order.

Thus the theorem also applies when the original graph has many high-degree vertices that disappear during this peeling process.

## 5. A separate obstruction to Mycielski constructions

Another natural source of triangle-free graphs of chromatic number four can be excluded explicitly.

Define the generalized Mycielski graph \(M_r(F)\), for \(r\ge2\), to have vertices
\[
(x,i)\quad(x\in V(F),\ 0\le i<r)
\]
and an apex \(w\). Keep the edges of \(F\) in layer \(0\); between consecutive layers join copies whose original vertices are adjacent in \(F\); and join \(w\) to every vertex in layer \(r-1\).

**Proposition.** If \(F\) is triangle-free and non-bipartite, then \(M_r(F)\) contains an induced \(C_6\).

**Proof.** Choose an induced odd cycle in \(F\), and let
\[
x_0,x_1,x_2,x_3,x_4
\]
be five consecutive vertices on it.

For \(r=2\), the vertices
\[
w,\ (x_0,1),\ (x_1,0),\ (x_2,0),\ (x_3,0),\ (x_4,1)
\]
in that order form an induced 6-cycle.

For \(r\ge3\), use
\[
w,\ (x_0,r-1),\ (x_1,r-2),\ (x_2,r-3),\
(x_3,r-2),\ (x_4,r-1).
\]
The only possible additional cross-layer edges would require \(x_0x_3\) or \(x_1x_4\), both absent. Same-layer edges cannot add a chord: all relevant layers are independent, except possibly layer \(0\), which contains only one selected vertex in this construction. \(\square\)

If \(F\) has a triangle, \(M_r(F)\) retains it. Hence a ternary graph of the form \(M_r(F)\) must have bipartite \(F\); colouring all copies according to a bipartition of \(F\), and the apex with a third colour, then gives a 3-colouring.

## 6. Remaining gap

The main proof relies on there being at most two high-degree vertices. In a bad list-colouring component, the non-cutvertices of each end odd cycle must then attach alternately to the same two vertices. Two such endblocks force an induced \(C_6\).

With three or more high-degree vertices, those attachment labels need not alternate between a fixed pair, so the induced-6-cycle conclusion does not follow. Nothing above rules out such configurations in a vertex-minimal ternary counterexample.

Thus these arguments settle restricted classes and exclude a standard construction, but do not establish a general 3-colouring theorem for ternary graphs.