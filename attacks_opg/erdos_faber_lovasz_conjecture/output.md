```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when the vertices belonging to at least three constituent cliques induce a bipartite graph.",
  "would_publish": false,
  "caveats": "Structural special case only; novelty has not been established."
}
```

# A structural partial result

I do not obtain a proof of the full conjecture. The following sufficient condition holds for every \(k\), independently of the sufficiently-large-\(k\) result described in the question.

Let \(C_1,\dots,C_k\) denote the vertex sets of the constituent \(K_k\)'s. For \(v\in V(G)\), define
\[
S(v)=\{i:v\in C_i\},\qquad r(v)=|S(v)|.
\]
Put
\[
B=\{v:r(v)\ge 3\},\qquad P=G[B].
\]

**Theorem.** If \(P\) is bipartite, then \(\chi(G)=k\).

In particular, this proves the conjecture whenever the vertices belonging to at least three constituent cliques induce a forest. A counterexample to the full conjecture would therefore have to contain an odd cycle entirely among those vertices.

The proof uses only ordinary graph edge-colouring results: Vizing’s theorem and its standard adjacency lemma.

## 1. The auxiliary graph and the private vertices

Pairwise edge-disjointness gives
\[
|C_i\cap C_j|\le 1\qquad(i\ne j).
\]
Consequently, for distinct vertices \(v,w\),
\[
|S(v)\cap S(w)|\le 1.
\]

Call a vertex **private** if \(r(v)=1\). It suffices to colour all nonprivate vertices properly with a palette of \(k\) colours. Indeed, if \(C_i\) contains \(s_i\) nonprivate vertices, their colours are distinct, leaving exactly \(k-s_i\) unused colours for its \(k-s_i\) private vertices. Each private vertex belongs to only this clique, so these extensions do not interfere.

Define a simple auxiliary graph \(F\) on vertex set \([k]\): a vertex \(v\) of multiplicity two, with
\[
S(v)=\{i,j\},
\]
corresponds to the edge \(ij\) of \(F\). There cannot be two such vertices for the same pair \(i,j\).

Thus:

- colouring the multiplicity-two vertices is edge-colouring \(F\);
- a colour assigned to \(b\in B\) must be avoided by every edge of \(F\) incident with an index in \(S(b)\).

For each \(i\), write
\[
h_i=|B\cap C_i|.
\]
For different \(b\in B\cap C_i\), the sets \(S(b)\setminus\{i\}\) are disjoint. They are also disjoint from the set of neighbours of \(i\) in \(F\). Hence
\[
d_F(i)+\sum_{b\in B\cap C_i}(r(b)-1)\le k-1.
\]
In particular,
\[
\boxed{d_F(i)\le k-1-2h_i.} \tag{1}
\]

If \(P\) is bipartite, then \(h_i\le 2\), since \(B\cap C_i\) is a clique in \(P\).

## 2. An ordinary edge-colouring lemma

We need a modest refinement of Vizing’s bound.

**Lemma.** Let \(J\) be a simple graph and \(D\ge 1\). If
\[
\Delta(J)\le D
\]
and at most two vertices of \(J\) have degree \(D\), then \(J\) has a proper edge-colouring with \(D\) colours.

**Proof.** The case \(D=1\) is immediate. If \(\Delta(J)<D\), Vizing’s theorem gives
\[
\chi'(J)\le \Delta(J)+1\le D.
\]

Suppose instead that \(J\) is not \(D\)-edge-colourable, and take an edge-minimal subgraph \(J_0\) with that property. Vizing’s theorem implies
\[
\Delta(J_0)=D,\qquad \chi'(J_0)=D+1.
\]
Moreover, deleting any edge makes \(J_0\) \(D\)-edge-colourable.

Vizing’s adjacency lemma says that, for every edge \(xy\) of such a critical graph, \(x\) has at least
\[
D-d_{J_0}(y)+1
\]
neighbours of degree \(D\), other than \(y\).

Choose a degree-\(D\) vertex \(x\) and a neighbour \(y\). If \(d_{J_0}(y)=D\), the lemma supplies another degree-\(D\) vertex besides \(x,y\). If \(d_{J_0}(y)<D\), it supplies at least two degree-\(D\) neighbours of \(x\). Either way, \(J_0\), and therefore \(J\), has at least three degree-\(D\) vertices—a contradiction. \(\square\)

## 3. Proof of the theorem

If \(B=\varnothing\), then \(\Delta(F)\le k-1\), so Vizing’s theorem edge-colours \(F\) with at most \(k\) colours. The private-vertex extension finishes the proof.

Assume henceforth that \(B\ne\varnothing\), so \(k\ge3\). Fix a proper colouring of \(P\) with two reserved colours, **red** and **blue**. Let
\[
D=k-2,\qquad
T=\{i\in[k]:d_F(i)\ge D\}.
\]

By (1), every index in \(T\) has \(h_i=0\): no vertex of \(B\) belongs to \(C_i\). Thus red and blue are both available at indices in \(T\).

Also, every vertex in \(T\) is nonadjacent in \(F\) to at most one other index, because
\[
d_F(i)\ge k-2.
\]
Therefore \(F[T]\) is a complete graph with a matching possibly deleted.

We will usually precolour a few edges of \(F\) red and blue, then apply the lemma to the remaining graph using \(D\) fresh colours. There is one exceptional configuration, handled separately with three reserved colours.

### Case 1: \(T=\varnothing\)

Here \(\Delta(F)\le D-1\), so \(F\) has a \(D\)-edge-colouring. Use colours disjoint from red and blue.

Together with the colouring of \(B\), this uses at most
\[
D+2=k
\]
colours.

### Case 2: \(|T|\ge2\)

First suppose \(T\) consists of two nonadjacent vertices. Each has degree exactly \(k-2=D\): neither can have degree \(k-1\), since they are nonadjacent. All other vertices have degree at most \(D-1\). The lemma therefore colours \(F\) with \(D\) fresh colours.

In every other instance of this case, \(F[T]\) has a Hamilton path. For completeness, when \(|T|\ge3\), this follows directly from its description as a complete graph minus a matching: start with a spanning path on any three vertices, and append each further vertex at an endpoint to which it is adjacent. Such an endpoint always exists because the new vertex has at most one nonneighbour.

Precolour this Hamilton path alternately red and blue. This is compatible with \(B\), since all its vertices lie in \(T\), where no high-multiplicity vertex occurs.

Remove the path edges, obtaining \(F_0\). An internal path vertex loses two incident edges, and an endpoint loses one. Thus:

- every internal path vertex has degree at most \(k-3=D-1\) in \(F_0\);
- each endpoint has degree at most \(k-2=D\);
- every vertex outside \(T\) still has degree at most \(D-1\).

Consequently, \(\Delta(F_0)\le D\), with at most two vertices of degree \(D\). The lemma colours \(F_0\) with \(D\) fresh colours. Again the total is \(k\).

### Case 3: \(T=\{u\}\)

If \(d_F(u)=D\), the lemma directly colours \(F\) with \(D\) fresh colours.

It remains to consider
\[
d_F(u)=D+1=k-1.
\]
Thus \(u\) is universal in \(F\), and no vertex of \(B\) belongs to \(C_u\).

Suppose there is an index \(j\ne u\) at which at least one of red or blue does not occur on \(B\cap C_j\). Give \(uj\) that available colour.

After deleting \(uj\), vertex \(u\) has degree \(D\), while every other vertex has degree at most \(D-1\), since \(T=\{u\}\). The lemma colours the remaining graph with \(D\) fresh colours, completing this subcase.

The only remaining configuration is therefore:

\[
\begin{gathered}
u\text{ is universal in }F,\qquad h_u=0,\\
\text{every }C_i,\ i\ne u,\text{ contains two vertices of }B,
\text{ one red and one blue.}
\end{gathered} \tag{2}
\]

### Case 4: The exceptional configuration (2)

Introduce a third reserved colour, **green**.

Choose a red vertex \(x\in B\) and an index \(p\in S(x)\). Let \(y\) be the blue vertex in \(B\cap C_p\). Because \(r(y)\ge3\) and
\[
S(x)\cap S(y)=\{p\},
\]
we can choose
\[
q\in S(y)\setminus\{p\}.
\]
Then \(q\notin S(x)\), and \(q\ne u\).

Recolour \(x\) green. This remains a proper colouring of \(P\), since green is used on no other vertex.

Now precolour the two edges
\[
up\text{ red},\qquad uq\text{ green}.
\]
These assignments are valid:

- at \(u\), no high-multiplicity vertex occurs;
- at \(p\), the high-multiplicity colours are now green and blue, so red is available;
- at \(q\), \(x\) does not occur, so green is available.

Let \(F_1\) be obtained by removing \(up\) and \(uq\). Then
\[
d_{F_1}(u)=k-3.
\]
For every \(i\ne u\), condition (2) gives \(h_i=2\), so (1) yields
\[
d_{F_1}(i)\le d_F(i)\le k-5.
\]
Thus \(u\) is the unique vertex of maximum degree \(k-3\).

Here \(k\ge6\) automatically: \(S(x)\cup S(y)\) contains at least five indices and does not contain \(u\). The lemma therefore applies with \(D'=k-3\), colouring \(F_1\) with \(k-3\) fresh colours.

Including red, blue and green, the total number of colours is
\[
(k-3)+3=k.
\]

### Completing the colouring

In every case:

1. the vertices of \(B\) are properly coloured;
2. the corresponding edge-colouring of \(F\) properly colours all multiplicity-two vertices;
3. whenever such a vertex meets a vertex of \(B\), their colours differ.

Hence all nonprivate vertices are properly coloured with \(k\) colours. Extend to the private vertices as in Section 1.

Finally, \(G\) contains a \(K_k\), so \(\chi(G)\ge k\). Therefore
\[
\boxed{\chi(G)=k.}
\]
This proves the stated special case. \(\square\)

## 4. What remains unresolved

The argument establishes the concrete necessary condition
\[
\boxed{\text{Every counterexample must have an odd cycle in }G[B].}
\]
This applies to the high-multiplicity set \(B\) arising from any witnessing clique decomposition.

However, pairwise edge-disjointness does not force \(G[B]\) to be bipartite. The proof gives no general treatment of nonbipartite high-overlap configurations, so it neither settles the full conjecture nor closes the finite gap left by a sufficiently-large-\(k\) theorem.

No computational verification is claimed, and I have not established whether this structural theorem is new.