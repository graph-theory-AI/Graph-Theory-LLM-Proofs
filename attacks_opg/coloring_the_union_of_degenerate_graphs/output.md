```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for graphs on at most 11 vertices, and every smallest counterexample must avoid two explicit low-degree clique configurations.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of these reductions and the small-order bound has not been checked."
}
```

## 1. Partial result

All graphs below are finite and simple. Let \(\mathcal C\) be the class of graphs expressible as
\[
G=F\cup D,
\]
where \(F\) is a forest and \(D\) is \(2\)-degenerate.

I establish the following.

**Theorem.**
1. Every graph in \(\mathcal C\) on at most \(11\) vertices is \(5\)-colourable.
2. A counterexample of minimum order, chosen with the fewest edges subject to that, has neither of these configurations:
   - a \(K_5\) all of whose vertices have degree \(5\) in \(G\);
   - an induced \(K_6-xy\) whose four vertices other than \(x,y\) have degree \(5\) in \(G\).

The proof of the order bound uses the classical Gallai low-degree lemma for critical graphs, stated explicitly below. The configuration reductions are proved directly.

These results do not improve the general upper bound of \(6\).

## 2. Preliminaries

We may assume \(E(F)\cap E(D)=\varnothing\), by removing overlapping edges from \(D\). Both defining properties are preserved under taking subgraphs.

A \(2\)-degenerate graph admits an ordering in which every vertex has at most two later neighbours. Consequently, on \(n\ge2\) vertices it has at most \(2n-3\) edges. Thus every \(G\in\mathcal C\) satisfies
\[
|E(G)|\le (n-1)+(2n-3)=3n-4. \tag{1}
\]
This applies also to every subgraph of \(G\). In particular, no member of \(\mathcal C\) contains \(K_6\).

The product colouring gives \(\chi(G)\le6\). If the conjecture fails, choose a counterexample \(G\) first with minimum order and then with minimum size. It is \(6\)-critical: every proper subgraph is \(5\)-colourable. In particular,
\[
\delta(G)\ge5. \tag{2}
\]

We shall use two elementary list-colouring observations.

**Observation A.** Suppose \(T\) is connected, every vertex \(v\) has a list \(A(v)\) of size at least \(d_T(v)\), and one vertex has a strictly larger list. Then \(T\) is list-colourable.

Indeed, root a spanning tree at a vertex with a strictly larger list and colour in an order placing children before parents. Every non-root vertex has an uncoloured parent, and the root has the extra available colour.

**Observation B.** A clique \(K_r\) is list-colourable if every list has size at least \(r-1\) and the union of all lists has size at least \(r\).

This follows immediately from Hall’s theorem: a subfamily of at most \(r-1\) lists has a sufficiently large union, and the full family does by assumption.

In particular, suppose a \(K_5\) has exactly one external neighbour at each of its vertices. A colouring of the rest of the graph extends to the clique whenever the colours appearing on those external neighbours are not all the same. The five lists then have size four, with union of size five.

## 3. Reducing a degree-five \(K_5\)

**Lemma 1.** A minimum-order counterexample contains no \(K_5\) all of whose vertices have degree \(5\).

**Proof.**
Suppose \(Q\) is such a clique. Each \(q\in Q\) has exactly one neighbour outside \(Q\). Let \(N\) be the set of those external neighbours. Since \(G\) contains no \(K_6\), we have \(|N|\ge2\).

It suffices to construct a graph
\[
G'=G-Q+ab\in\mathcal C
\]
for some distinct \(a,b\in N\). By minimality, \(G'\) has a \(5\)-colouring. The edge \(ab\) ensures that the external neighbours of \(Q\) are not monochromatic, so Observation B extends the colouring to \(Q\).

Fix the decomposition \(G=F\cup D\).

### Case 1: A component of \(F[Q]\) has at least two forest edges to \(V(G)\setminus Q\)

The external ends \(a,b\) of two such edges are distinct: otherwise these edges and a path in the component would make a cycle in \(F\).

There is an \(a\)-to-\(b\) path in \(F\) with all internal vertices in \(Q\). Hence \(a,b\) lie in different components of \(F-Q\). It follows that
\[
F-Q+ab
\]
is a forest. Together with \(D-Q\), it gives the required decomposition of \(G-Q+ab\).

### Case 2: Every component of \(F[Q]\) has at most one forest edge leaving \(Q\)

Write
\[
f=|E(F[Q])|,\qquad
t=|E_F(Q,V(G)\setminus Q)|.
\]
The forest \(F[Q]\) has \(5-f\) components, so
\[
t\le5-f.
\]
There are ten edges inside \(Q\) and five edges leaving \(Q\). Therefore the number of \(D\)-edges having at least one end in \(Q\) is
\[
(10-f)+(5-t)=15-f-t\ge10. \tag{3}
\]

Choose a \(2\)-degeneracy ordering of \(D\), and let \(z\) be the last vertex of \(N\) in this ordering.

Suppose some \(a\in N\setminus\{z\}\) has a later \(D\)-neighbour in \(Q\). Deleting \(Q\) frees at least one later-neighbour position at \(a\). Since \(z\) is later than \(a\), adding \(az\) leaves every vertex with at most two later neighbours. Thus
\[
D-Q+az
\]
is \(2\)-degenerate, giving the desired smaller graph.

It remains to show that such an \(a\) exists.

Suppose not. Construct a graph \(J\) on \(Q\cup\{z\}\) by retaining \(D[Q]\) and replacing every \(D\)-edge from \(q\in Q\) to \(N\) by \(qz\). Each \(q\) has only one external neighbour, so no two of these edges coalesce. By (3),
\[
|E(J)|\ge10. \tag{4}
\]

Nevertheless, \(J\) is \(2\)-degenerate. Use the original ordering restricted to \(Q\cup\{z\}\). If a replaced edge was \(qa\), with \(a\ne z\), our assumption implies
\[
q<a<z.
\]
Thus replacing \(qa\) by \(qz\) does not increase the number of later neighbours of \(q\). All newly acquired neighbours of \(z\) precede \(z\), so its number of later neighbours also does not increase.

This contradicts (4), because a \(2\)-degenerate graph on six vertices has at most nine edges. The required \(a\) therefore exists, completing the reduction. \(\square\)

## 4. Reducing a degree-five-interior \(K_6-e\)

**Lemma 2.** A minimum-order counterexample contains no induced \(K_6-xy\) whose four vertices other than \(x,y\) have degree \(5\) in \(G\).

**Proof.**
Let \(S\) induce this configuration, and put
\[
W=S\setminus\{x,y\}.
\]
Since \(G[S]\) has fourteen edges,
\[
|E(F[S])|\le5,\qquad |E(D[S])|\le9
\]
must both be equalities. Thus \(F[S]\) is a tree, and \(D[S]\) is an extremal \(2\)-degenerate graph on six vertices.

Take a \(2\)-degeneracy ordering of \(D\), and restrict it to \(S\). The successive numbers of later neighbours within \(S\) are bounded by
\[
2,2,2,2,1,0.
\]
Their sum is nine, so equality holds at every position. In particular, the last two vertices of \(S\) are adjacent in \(D\).

Assume \(x\) precedes \(y\). Since \(xy\notin E(D)\), \(x\) is among the first four vertices of \(S\), and it has exactly two later \(D\)-neighbours within \(S\). Hence \(x\) has no later \(D\)-neighbour outside \(S\).

Construct \(G'\) by deleting \(W\) and identifying \(x\) with \(y\), suppressing duplicate edges.

The images of the two parts still give a valid decomposition:

- **Forest part.** The tree \(F[S]\) contains an \(x\)-to-\(y\) path with internal vertices in \(W\). Therefore \(x,y\) are in different components of \(F-W\); otherwise \(F\) would contain a cycle. Identifying them preserves the forest property.
- **\(2\)-degenerate part.** Retain the position of \(y\) in the original ordering and delete \(x,W\). Every remaining \(D\)-neighbour of \(x\) precedes \(x\), and hence precedes \(y\). Moving its edge from \(x\) to \(y\) does not increase its number of later neighbours, and gives \(y\) no new later neighbour. Thus the image of \(D-W\) remains \(2\)-degenerate.

Consequently \(G'\in\mathcal C\), and it has five fewer vertices. A \(5\)-colouring of \(G'\) assigns the same colour to \(x,y\) when lifted back to \(G-W\). Colour the clique \(W\) with the other four colours. Its vertices have no neighbours outside \(S\), by their degree-five assumption, so this is a proper colouring of \(G\), a contradiction. \(\square\)

## 5. No counterexample on at most eleven vertices

Let \(G\) be a minimum counterexample as above. Define
\[
L=\{v:d_G(v)=5\},\qquad
R=V(G)\setminus L,
\]
and write
\[
\ell=|L|,\qquad h=|R|,\qquad
\eta=\sum_{v\in R}(d_G(v)-6).
\]
Every vertex of \(R\) has degree at least six. From (1),
\[
2|E(G)|=5\ell+6h+\eta
       =6|V(G)|-\ell+\eta
       \le6|V(G)|-8,
\]
so
\[
\ell\ge8+\eta. \tag{5}
\]

### 5.1 A Gallai-forest estimate

We use the following classical theorem.

> **Gallai’s low-degree lemma.** In a \(k\)-critical graph, the subgraph induced by the vertices of degree \(k-1\) has every block either a clique or an odd cycle.

Thus \(G[L]\) is a Gallai forest. Lemma 1 excludes a \(K_5\) in \(G[L]\), so its clique blocks have order at most four.

Let \(c\) be the number of components of \(G[L]\), and let \(b\) be its number of \(K_4\)-blocks. These \(K_4\)-blocks are vertex-disjoint: a vertex belonging to two would have at least six neighbours in \(L\), contrary to its degree being five. Hence
\[
b\le\ell/4.
\]

Every block other than a \(K_4\) has at most
\[
\frac32(|V(B)|-1)
\]
edges. A \(K_4\) exceeds this expression by \(3/2\). Using the block identity
\[
\sum_B(|V(B)|-1)=\ell-c,
\]
we obtain
\[
|E(G[L])|
 \le \frac32(\ell-c)+\frac32b
 \le \frac{15}{8}\ell-\frac32c. \tag{6}
\]

Set
\[
t=|E_G(L,R)|,\qquad r=|E(G[R])|.
\]
Since every vertex in \(L\) has degree five, (6) gives
\[
t=5\ell-2|E(G[L])|
 \ge \frac54\ell+3c. \tag{7}
\]
On the other hand,
\[
2|E(G)|=5\ell+t+2r\le6(\ell+h)-8.
\]
Combining this with (7),
\[
\boxed{\frac{\ell}{4}+3c\le6h-8-2r.} \tag{8}
\]

By (5), \(\ell\ge8\), and \(c\ge1\). The left side of (8) is therefore at least five. If \(h\le2\), its right side is at most four. Consequently,
\[
h\ge3. \tag{9}
\]

### 5.2 The only possible parameters below order twelve

Suppose now that \(|V(G)|\le11\). Equations (5) and (9) force
\[
\ell=8,\qquad h=3,\qquad \eta=0.
\]
Thus all three vertices of \(R\) have degree six, and
\[
|E(G[L])|=11+r. \tag{10}
\]
Equation (8) becomes
\[
2+3c\le10-2r. \tag{11}
\]
In particular, \(r\le2\).

Whenever \(R\) is properly coloured from five colours, give each \(v\in L\) the list of colours not used on its neighbours in \(R\). Then
\[
|A(v)|\ge5-d_R(v)=d_{G[L]}(v). \tag{12}
\]
Moreover, if two neighbours of \(v\) in \(R\) receive the same colour, the inequality in (12) is strict. Observation A then colours any component containing such a vertex.

We now cover all possibilities for \(G[R]\).

#### Case \(r=0\)

Colour all three vertices of \(R\) alike.

Every component of \(G[L]\) has a vertex of internal degree at most three: take a non-cutvertex in an endblock, or any suitable vertex if the component is a single block. Such a vertex has at least two neighbours in \(R\), so its list satisfies strict inequality in (12).

Observation A colours every component of \(G[L]\).

#### Case \(r=2\)

The graph \(G[R]\) is a path \(a-b-c\). Equation (11) implies that \(G[L]\) is connected.

Both endpoints \(a,c\) have five neighbours in \(L\). Since \(|L|=8\), they have a common neighbour in \(L\). Colour \(a,c\) alike and colour \(b\) differently. The common neighbour has a strictly larger list than its degree in \(G[L]\), so Observation A completes the colouring.

#### Case \(r=1\)

Write the edge of \(G[R]\) as \(uv\), with \(w\) isolated in \(G[R]\).

If \(G[L]\) is connected, then
\[
|N_L(u)|=5,\qquad |N_L(w)|=6.
\]
They have a common neighbour. Colour \(u,w\) alike and \(v\) differently, and apply Observation A.

It remains to consider disconnected \(G[L]\). Equation (11) gives \(c=2\). Also every vertex of \(L\) has at least two neighbours in \(L\), because it has degree five and there are only three vertices in \(R\). Thus the component orders are either \(3,5\) or \(4,4\).

The \(3,5\) possibility is incompatible with (10): the three-vertex component has at most three edges, and (6), applied to the five-vertex component, bounds its size by
\[
\left\lfloor\frac{15}{8}\cdot5-\frac32\right\rfloor=7.
\]
Their total is at most ten, whereas (10) requires twelve.

Therefore \(G[L]\) consists of two copies of \(K_4\). Each of their vertices has exactly two neighbours in \(R\).

Colour \(u,v,w\) with three distinct colours. On either \(K_4\), the four available lists have size three. They cannot all be identical. Otherwise all four vertices of that clique would have the same two neighbours in \(R\); the omitted vertex of \(R\) would have at most four neighbours in \(L\), all in the other clique. But the three vertices of \(R\) have respectively five, five and six neighbours in \(L\).

Thus the union of the four lists on each \(K_4\) has size at least four. Observation B colours both cliques.

Every case produces a \(5\)-colouring, contradicting the choice of \(G\). This proves that a counterexample must have at least twelve vertices. \(\square\)

## 6. What remains unresolved

The reductions impose genuine restrictions on a smallest counterexample:

- it is \(6\)-critical;
- it has at least eight degree-five vertices and at least three vertices of degree at least six;
- its degree-five vertices induce a Gallai forest with no \(K_5\)-block;
- it has no degree-five-interior \(K_6-e\);
- it satisfies the quantitative constraint (8).

However, these conditions do not exclude larger counterexamples. In particular, the argument does not provide reductions for all possible \(K_4\)-blocks and odd-cycle blocks in the degree-five subgraph.

Thus this is an analytic small-order result and a pair of structural reductions—not a proof of the full conjecture. No computational enumeration or claim of literature novelty is being made.