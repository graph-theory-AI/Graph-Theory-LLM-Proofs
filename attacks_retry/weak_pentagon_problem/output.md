```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured conclusion when some maximum cut omits at most six edges and all omitted edges lie on one side, extending the previous near-bipartite construction.",
  "would_publish": false,
  "caveats": "This is not a uniform result for edge-bipartization number at most six; the general conjecture remains unresolved here, and novelty is unchecked."
}
```

# A partial theorem via one-sided maximum cuts

I rechecked the Clebsch-graph model and the auxiliary-coloring construction in the previous attempt. Both are valid. The new step below is a structural reduction for an auxiliary \(K_6\), which allows the construction to handle a larger class.

Throughout, graphs are finite and simple.

For a maximum cut with parts \(A,B\), call an edge **omitted** if it does not cross the cut. A maximum cut in a cubic graph has its omitted edges forming a matching: moving a vertex incident with at least two omitted edges would increase the cut.

Here is the main partial result.

**Theorem.** Let \(G\) be a triangle-free cubic graph with a maximum cut \((A,B)\) such that \(B\) is independent. Put
\[
M=E(G[A]),\qquad
Z=\{b\in B:N_G(b)\subseteq V(M)\}.
\]
If
\[
|Z|\le 8,
\]
then \(G\) has a homomorphism to the Clebsch graph and hence has the required five-coloring.

Thus \(Z\) consists of the vertices of \(B\) whose three neighbors are all endpoints of omitted edges.

**Corollary.** The conclusion holds if some maximum cut has at most six omitted edges, all lying in one part.

Indeed, every endpoint of \(M\) has two neighbors in \(B\), so
\[
3|Z|\le 4|M|.
\tag{1}
\]

The theorem also extends the previous sufficient condition that every vertex of \(B\) has at most two neighbors in \(V(M)\): that condition is exactly \(Z=\varnothing\).

The maximum-cut hypothesis is essential to the argument below. In particular, I do **not** prove the conjecture for all graphs with edge-bipartization number at most six.

## 1. The Clebsch graph and the required edge-coloring

Let \(\mathbf1=(1,1,1,1,1)\in\mathbb F_2^5\), and set
\[
s_i=\mathbf1+e_i,\qquad 1\le i\le5.
\]
Use the following model \(\mathcal C\) of the Clebsch graph:

- vertices are the sixteen even-weight vectors in \(\mathbb F_2^5\);
- \(x\sim y\) precisely when \(x+y=s_i\) for some \(i\).

This is the antipodal quotient of \(Q_5\), using the unique even-weight representative of each antipodal pair.

We will use these elementary properties.

1. \(\mathcal C\) is triangle-free.
2. Two distinct nonadjacent vertices have exactly two common neighbors.
3. Its automorphisms are transitive on ordered adjacent pairs and on ordered distinct nonadjacent pairs.

For verification, translations by even-weight vectors and coordinate permutations are automorphisms. Two distinct nonadjacent vertices differ by \(e_i+e_j\); after translating one to \(0\), their common neighbors are exactly \(s_i,s_j\). Also, the sum of two distinct generators has weight two, proving triangle-freeness.

Given a homomorphism \(f:G\to\mathcal C\), color an edge \(uv\) with \(i\) when
\[
f(u)+f(v)=s_i.
\]
For fixed \(j\), every edge not colored \(j\) joins vertices with different \(j\)-th coordinates. Thus the complement of color class \(j\) is bipartite.

It remains to construct the homomorphism.

## 2. The auxiliary-coloring construction

We need a version that also applies to subcubic graphs produced by deleting a subgraph.

**Lemma 1.** Let \(H\) be triangle-free and subcubic, with a partition \(A_H,B_H\) such that \(B_H\) is independent and \(H[A_H]\) is a matching \(M_H\) together with isolated vertices.

For every endpoint \(u\) of \(M_H\), put
\[
N_u=N_H(u)\cap B_H.
\]
Construct a simple graph \(F_H\) on \(B_H\) by adding all edges between \(N_u\) and \(N_v\) for each \(uv\in M_H\). If \(F_H\) is five-colorable, then \(H\to\mathcal C\).

**Proof.** Triangle-freeness gives \(N_u\cap N_v=\varnothing\) whenever \(uv\in M_H\). Let
\[
c:B_H\to[5]
\]
be a proper coloring of \(F_H\). Then \(c(N_u)\) and \(c(N_v)\) are disjoint and each has size at most two.

Choose disjoint two-element sets \(P_u,P_v\subseteq[5]\) containing \(c(N_u)\) and \(c(N_v)\), respectively. This is possible because a total of only four distinct colors is required. Make the choices independently for the edges of \(M_H\).

Identifying subsets with characteristic vectors, define
\[
f(x)=
\begin{cases}
s_{c(x)},&x\in B_H,\\
0,&x\in A_H\setminus V(M_H),\\
\mathbf1_{P_x},&x\in V(M_H).
\end{cases}
\]
A cross edge incident with \(A_H\setminus V(M_H)\) is plainly respected. If \(xy\) is a cross edge with \(x\in V(M_H)\), then \(c(y)\in P_x\), so
\[
\mathbf1_{P_x}+s_{c(y)}
\]
is another generator \(s_i\). Finally, the labels at the ends of an edge of \(M_H\) are disjoint two-element sets and therefore differ in four coordinates. These are all edge types. \(\square\)

Notice also that
\[
d_{F_H}(b)\le
2\,|N_H(b)\cap V(M_H)|.
\tag{2}
\]

For the cubic graph in the theorem, write its auxiliary graph simply as \(F\). Each omitted edge contributes a copy of \(K_{2,2}\), which I will call a **block**. Blocks may share vertices and edges.

By (2),
\[
\Delta(F)\le6,
\qquad
\{b:d_F(b)\ge5\}\subseteq Z.
\tag{3}
\]

## 3. The only small high-degree obstruction is \(K_6\)

**Lemma 2.** Suppose a graph \(F\) has maximum degree at most six and at most eight vertices of degree at least five. If \(F\) is not five-colorable, it contains \(K_6\).

**Proof.** Take a vertex-minimal subgraph \(J\) that is not five-colorable. Every vertex of \(J\) has degree at least five, so \(|V(J)|\le8\).

If \(J\) has six vertices, it is \(K_6\). If it has seven vertices, its complement is a matching together with isolated vertices. Unless \(J\) contains \(K_6\), that matching has at least two edges, giving a five-coloring of \(J\).

If \(J\) has eight vertices, its complement has minimum degree at least one and maximum degree at most two. It is therefore a union of paths and cycles, each with at least two vertices. Such a graph has a matching of size at least three: a component of order \(t\ge2\) has a matching of size \(\lfloor t/2\rfloor\ge t/3\). Pairing the endpoints of three matching edges gives a five-coloring of \(J\), again a contradiction. \(\square\)

The next lemma explains why an auxiliary \(K_6\) is reducible in the maximum-cut setting.

## 4. Structure forced by an auxiliary \(K_6\)

**Lemma 3.** Let \(G,(A,B),M,F\) be as in the theorem, without assuming \(|Z|\le8\). If \(F[S]\cong K_6\), then \(G\) contains an induced subgraph \(H\) with the following properties:

- \(H\) has fourteen vertices;
- precisely two vertices \(u,v\) have degree two in \(H\), and all other vertices have degree three;
- \(u,v\in B\), and they are the only vertices of \(H\) incident with edges leaving \(H\);
- those two external edges are \(ux,vy\), where \(xy\in M\);
- the auxiliary graph of \(H\), using its inherited partition, is \(K_6-uv\).

### Two maximum-cut observations

For each \(a\in V(M)\), represent its two \(B\)-neighbors by an edge of a loopless multigraph \(R\) on \(B\). The two \(R\)-edges corresponding to the endpoints of an edge of \(M\) are paired. Triangle-freeness says that paired \(R\)-edges are vertex-disjoint.

First, **no parallel edges of \(R\) are incident with a vertex of \(Z\)**.

Indeed, let \(b\in Z\). Switching \(b\) and its three neighbors to the other sides of the cut preserves the cut size: three omitted edges become crossing, and three crossing edges become omitted. The three neighbors of \(b\) belong to distinct edges of \(M\), by triangle-freeness. If two corresponding \(R\)-edges were parallel, the new omitted edges would include two edges incident with their other common \(B\)-endpoint. Switching that endpoint would increase the cut, a contradiction.

Second, there is a useful switching test. Let \(T\subseteq Z\), and switch precisely these \(B\)-vertices. For a paired pair of \(R\)-edges, let \(i,j\in\{0,1,2\}\) be their numbers of endpoints in \(T\). Optimizing the placements of the two corresponding \(A\)-vertices changes the number of omitted edges by
\[
\begin{array}{c|rrr}
\Phi(i,j)&j=0&j=1&j=2\\ \hline
i=0&0&0&-1\\
i=1&0&1&0\\
i=2&-1&0&0
\end{array}
\tag{4}
\]
relative to the original one omitted edge.

These choices are independent over \(M\). Moreover, no vertex of \(A\setminus V(M)\) is adjacent to \(T\). Consequently, maximum-cut optimality implies
\[
\sum_{uv\in M}\Phi\bigl(|N_u\cap T|,|N_v\cap T|\bigr)\ge0.
\tag{5}
\]

### Counting the blocks meeting \(S\)

Every vertex of the auxiliary \(K_6\) belongs to exactly three blocks: five auxiliary neighbors require three incident endpoints of \(M\).

A block meeting \(S\) cannot contain only one vertex of \(S\), or two vertices on the same side of its \(K_{2,2}\). Such an occurrence would contribute no internal auxiliary neighbor to one of its vertices, leaving that vertex with at most four neighbors in \(S\).

Thus a block meets \(S\) in:

- all four vertices;
- a three-vertex path;
- an edge.

Call a vertex a **leaf occurrence** when it has only one neighbor within the block’s intersection with \(S\). Each vertex of \(S\) can have at most one leaf occurrence.

Let \(n_4,n_3,n_2\) count these three block types. Then
\[
4n_4+3n_3+2n_2=18,
\qquad
n_2+n_3\le3.
\]
The only possibilities are
\[
(n_4,n_3,n_2)
=(4,0,1),\quad (3,2,0),\quad (3,0,3).
\tag{6}
\]

There is also a multiplicity constraint. A vertex with a leaf occurrence has exactly five internal neighbor incidences, all distinct. A vertex without a leaf occurrence has six incidences covering five neighbors, so exactly one is repeated. Hence the repeated auxiliary edges form a matching on the vertices without leaf occurrences.

We exclude the last two possibilities in (6).

### Excluding three full blocks and two partial paths

The four leaves of the two partial paths are distinct. Write \(x,y\) for the other two vertices. The unique repeated auxiliary edge is \(xy\).

The centers of the partial paths cannot both be leaves: they would have to be distinct and each would be a leaf of the other path, repeating an edge whose endpoints are leaves. If both centers are non-leaves, they must be distinct; otherwise their common center would occur in only one full block, whereas the two copies of \(xy\) require two full blocks.

Thus, up to names, the partial paths are either
\[
\text{I: }a-x-b,\quad c-y-d,
\qquad
\text{II: }a-x-b,\quad c-a-d.
\]

The full blocks are then forced up to relabeling. To display them economically, write \((ab,cd)\) for a block whose paired \(R\)-edges are \(ab\) and \(cd\). The letters \(X,Y\) below denote vertices outside \(S\), possibly equal.
\[
\begin{array}{c|c|c}
&\text{three full blocks}&\text{two partial blocks}\\ \hline
\mathrm{I}
 &(xa,yc),\ (xb,yd),\ (ac,bd)
 &(ab,xX),\ (cd,yY)\\[1mm]
\mathrm{II}
 &(xd,yc),\ (xb,yd),\ (yb,ac)
 &(ab,xX),\ (cd,aY)
\end{array}
\tag{7}
\]

Here is a direct check of exhaustion. In case I, the two full cycles using the doubled edge \(xy\) are, after relabeling,
\[
x-y-a-c-x,\qquad x-y-b-d-x,
\]
and the remaining one is \(a-b-c-d-a\). In case II, \(a\) has only two incident full-block edges, \(ay,ab\). Its full cycle must be \(y-a-b-c-y\), after possibly exchanging \(c,d\); the remaining cycles are \(x-y-d-c-x\) and \(x-y-b-d-x\). These give (7).

Now use (5):

- In case I, take \(T=\{x,a,b\}\). The five contributions in (7) are
  \[
  -1,-1,+1,0,0.
  \]
- In case II, take \(T=\{y,c,d\}\). They are
  \[
  0,-1,+1,0,-1.
  \]

Both sums are \(-1\), contradicting maximum-cut optimality.

### Excluding three full blocks and three partial edges

The three partial edges form a perfect matching \(P\) on \(S\). There are no repeated internal auxiliary edges, so the full blocks edge-decompose \(K_6-P\).

Every full four-cycle contains some pair of \(P\) as a diagonal. Repeating such a diagonal would repeat an \(R\)-edge incident with \(S\subseteq Z\), which was excluded above. Therefore the three full cycles each contain exactly one \(P\)-pair as a diagonal, and use all three pairs.

Consider the cycles whose \(P\)-diagonals are \(\{a,a'\}\) and \(\{b,b'\}\). The first has, as its other diagonal, one vertex \(b_0\in\{b,b'\}\) and a vertex of the third pair. The second similarly uses some \(a_0\in\{a,a'\}\). Both cycles contain the auxiliary edge \(a_0b_0\), contradicting edge-disjointness.

### The remaining case

We must have four full blocks and one partial edge, say \(uv\).

The vertices \(u,v\) each occur in two full blocks; the other four vertices of \(S\) occur in three. Let \(H\) consist of \(S\) and the eight \(A\)-vertices belonging to the four full blocks.

Every one of those eight \(A\)-vertices has all its neighbors in \(H\). Within \(S\), only \(u,v\) have a neighbor outside \(H\). Since they lie on opposite sides of the unique partial block, their external neighbors are the endpoints of the same edge of \(M\). Finally, \(uv\) occurs only in the partial block, so the auxiliary graph of \(H\) is exactly \(K_6-uv\).

This proves Lemma 3. \(\square\)

## 5. Completing the main theorem

By (3) and Lemma 2, either \(F\) is five-colorable, or \(F\) contains \(K_6\).

In the first case, Lemma 1 gives the desired homomorphism.

In the second case, take the fourteen-vertex subgraph \(H\) from Lemma 3, with ports \(u,v\) and external neighbors \(x,y\).

### Mapping the fourteen-vertex subgraph

Its auxiliary graph is \(K_6-uv\). Color \(u,v\) alike, and give the other four vertices distinct colors. Lemma 1 gives a homomorphism \(H\to\mathcal C\) with equal port images.

We can change the image of \(u\) alone to make the port images distinct and nonadjacent. Indeed, \(u\) has only two neighbors in \(H\). Their images either coincide or are distinct nonadjacent vertices. In both cases they have at least two common neighbors in \(\mathcal C\), so there is a choice other than the current image of \(u\). The new image and the old image are nonadjacent because they share a neighbor in the triangle-free graph \(\mathcal C\).

Thus \(H\) has a homomorphism whose port images are distinct and nonadjacent.

### Mapping the rest and joining the maps

Let \(G'=G-V(H)\), retaining its inherited partition. It is triangle-free and subcubic, with an independent \(B\)-part and a matching in its \(A\)-part.

All six vertices of \(S\) belonged to \(Z\). By (2), the auxiliary graph of \(G'\) therefore has at most
\[
|Z|-6\le2
\]
vertices of degree at least five. It is consequently 4-degenerate and five-colorable. Lemma 1 gives a homomorphism \(f':G'\to\mathcal C\).

The vertices \(x,y\) remain adjacent in \(G'\). Apply a target automorphism so that
\[
f'(x)=0,\qquad f'(y)=s_5.
\]
Set
\[
p=s_1,\qquad q=s_5+s_2.
\]
Then
\[
p\sim f'(x),\qquad q\sim f'(y),
\]
while
\[
p+q=s_1+s_5+s_2=e_3+e_4.
\]
Thus \(p,q\) are distinct and nonadjacent.

By transitivity on ordered distinct nonadjacent pairs, an automorphism takes the port images of the homomorphism of \(H\) to \(p,q\). The resulting map of \(H\) combines with \(f'\), since \(ux,vy\) are the only edges between the two pieces.

This completes the theorem. \(\square\)

## 6. Relation to edge-bipartization

Let
\[
\beta(G)=\min\{|D|:G-D\text{ is bipartite}\}.
\]
This is the number of omitted edges in a maximum cut.

If a maximum cut has \(a\) omitted edges in \(A\) and \(b\) in \(B\), degree counting gives
\[
3(|A|-|B|)=2(a-b).
\tag{8}
\]
Hence \(a-b\) is divisible by three.

In particular:

- \(\beta(G)=1\) is impossible;
- if \(\beta(G)=2\), the distribution is \(1+1\);
- if \(\beta(G)=3\), all omitted edges lie on one side;
- if \(\beta(G)=6\), the possible distributions are \(6+0\), \(3+3\), and \(0+6\).

The new theorem handles the one-sided distributions at six.

For completeness, here is a short verification of the remaining case needed to recover the previous uniform result \(\beta(G)\le3\).

### Two omitted edges

Write them as \(aa'\) and \(bb'\), with \(a,a'\in A\) and \(b,b'\in B\), and let \(D=G-\{aa',bb'\}\).

Triangle-freeness implies that the edges between \(\{a,a'\}\) and \(\{b,b'\}\) form a matching. Orient the names so that
\[
ab',a'b\notin E(G).
\]
Then, for
\[
L=\{a,b\},\qquad R=\{a',b'\},
\]
we have \(\operatorname{dist}_D(L,R)\ge3\): a length-two path between the endpoints of either omitted edge would create a triangle, and the other relevant pairs are in opposite parts and nonadjacent.

Define
\[
h(v)=\min\{3,\operatorname{dist}_D(v,L)\},
\]
with height three in components not meeting \(L\). Let \(p=0\) on \(A\), \(p=1\) on \(B\), and put
\[
f(v)=\bigl(p(v)+h(v)\bmod2\bigr)s_4
      +\sum_{i=1}^{h(v)}s_i.
\tag{9}
\]

For a \(D\)-edge, heights differ by at most one. Equal heights give label difference \(s_4\); heights differing by one give one of \(s_1,s_2,s_3\). Each omitted edge joins heights zero and three within one part, giving difference
\[
s_4+s_1+s_2+s_3=s_5.
\]
Thus (9) is a homomorphism.

Consequently the previous \(\beta(G)\le3\) result is valid, and the present argument adds the one-sided maximum-cut case at \(\beta(G)=6\), as well as the more general \(|Z|\le8\) theorem with no bound on \(\beta(G)\).

## 7. Scope and remaining gap

The proof is constructive once a qualifying maximum cut is supplied. One can peel auxiliary vertices of degree at most four, leaving at most eight vertices; the remaining coloring check and search for an auxiliary \(K_6\) are bounded-size tasks. The subsequent constructions are explicit. This does not provide a polynomial-time method for finding the required maximum cut, and no computational experiment is being claimed.

The full conjecture is not settled:

- maximum-cut complements split between both sides are generally outside this auxiliary construction;
- in particular, no general conclusion is obtained here for \(\beta(G)=4\) or \(5\);
- with more than eight vertices in \(Z\), non-five-colorability of the auxiliary graph need not be witnessed by the small-obstruction argument used above.

Thus the new result is a proved special case and a reducibility lemma, not a proof of the weak pentagon conjecture.