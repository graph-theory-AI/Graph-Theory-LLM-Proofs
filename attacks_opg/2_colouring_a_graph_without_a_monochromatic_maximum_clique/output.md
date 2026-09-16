```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for odd-hole-free K4-free graphs whose deletion of some induced complement of C7 leaves a disjoint union of cliques.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of this special case has not been checked. Graphs with no edges are excluded."
}
```

# A precolouring-extension result around a seven-vertex antihole

I obtain a special case, with a self-contained proof. In fact, the result only needs the exclusion of \(K_4\) and induced \(C_5\), rather than all odd holes.

Graphs are finite and simple. For the substantive conjecture, assume \(\omega(G)\ge 2\): if “non-empty” permits an edgeless graph with vertices, its singleton maximum cliques are necessarily monochromatic.

## 1. Partial theorem

A **cluster graph** is a disjoint union of cliques, allowing isolated vertices and the empty graph.

**Theorem.** Let \(G\) contain no \(K_4\) and no induced \(C_5\). Suppose that \(A\subseteq V(G)\) induces \(\overline{C_7}\), and that \(G-A\) is a cluster graph. Then every proper four-colouring of \(G[A]\) extends to a proper four-colouring of \(G\).

Consequently, \(G\) has a two-colouring with no monochromatic maximum clique.

The edges between \(A\) and the outside clique components need not be uniform; those components are not assumed to be modules.

The proof establishes a slightly more general local fact: a four-colouring of the antihole extends over **each individual outside clique**, regardless of the structure of the rest of the graph.

### Why four-colouring is relevant

For an odd-hole-free graph with clique number three, the desired two-division is equivalent to four-colourability.

Indeed, each part of a two-division is triangle-free and odd-hole-free, and hence bipartite: a shortest odd cycle in a triangle-free non-bipartite graph would be an induced odd cycle of length at least five. Thus the two parts together use at most four proper colours. Conversely, grouping four proper colours into two pairs gives a two-division.

So the theorem addresses the exact desired property in this restricted clique-number-three setting.

## 2. Possible attachments to the antihole

Label
\[
A=\{a_0,a_1,\ldots,a_6\}
\]
cyclically, with indices modulo seven, so that
\[
a_i a_j\notin E(G[A])
\quad\Longleftrightarrow\quad
j=i\pm1
\qquad(i\ne j).
\]

For \(x\notin A\), put
\[
S(x)=\{i:a_i\in N(x)\}.
\]

**Lemma 1.** Every \(S(x)\) has one of the following forms:
\[
\begin{split}
&\varnothing;\\
&\{i\};\\
&\{i,j\},\quad i,j\text{ nonconsecutive on the seven-cycle};\\
&T_i:=\{i,i+1,i+2\};\\
&D_i:=\{i,i+1,i+2,i+3\}.
\end{split}
\]

**Proof.** Regard \(S(x)\) as a vertex subset of the underlying seven-cycle \(C\). Since \(G\) is \(K_4\)-free,
\[
\alpha(C[S(x)])\le 2:
\]
three independent vertices of \(C[S(x)]\) would be three pairwise adjacent neighbours of \(x\) in \(G\).

In particular, \(S(x)\ne V(C)\), so \(C[S(x)]\) is a disjoint union of paths.

No component of \(C[S(x)]\) can have exactly two vertices. Indeed, if
\[
i,i+1\in S(x),\qquad i-1,i+2\notin S(x),
\]
then
\[
x,a_i,a_{i+2},a_{i-1},a_{i+1},x
\]
is an induced five-cycle.

A path on at least five vertices has independence number at least three. A path on three or four vertices already has independence number two and therefore cannot occur together with another component. After excluding two-vertex components, the only remaining disconnected possibility is at most two isolated vertices. These are precisely the listed forms. \(\square\)

## 3. Lists induced by a four-colouring of the antihole

Normalize the given colouring of \(A\) as follows:
\[
\begin{array}{c|ccccccc}
\text{vertex}&a_0&a_1&a_2&a_3&a_4&a_5&a_6\\ \hline
\text{colour}&0&1&1&2&2&3&3 .
\end{array}
\tag{1}
\]

Every proper four-colouring of \(A\) can be put in this form by cyclically relabelling \(A\) and renaming colours. To see this, every colour class has size at most two, so the class sizes are \(2,2,2,1\). A two-vertex class consists of consecutive vertices of the underlying cycle. Once the singleton is removed, pairing the remaining six-vertex path is forced.

For \(x\notin A\), let
\[
L(x)=\{0,1,2,3\}\setminus
\{\text{colours appearing on }N(x)\cap A\}.
\]
These are exactly the colours that can be assigned to \(x\) without conflicting with (1).

If \(|S(x)|\le2\), then \(|L(x)|\ge2\). For the other possibilities in Lemma 1, direct inspection gives:
\[
\begin{array}{c|c|c}
i&L(x)\text{ when }S(x)=T_i&
L(x)\text{ when }S(x)=D_i\\ \hline
0&\{2,3\}&\{3\}\\
1&\{0,3\}&\{0,3\}\\
2&\{0,3\}&\{0\}\\
3&\{0,1\}&\{0,1\}\\
4&\{0,1\}&\{1\}\\
5&\{1,2\}&\{2\}\\
6&\{2\}&\{2\}
\end{array}
\tag{2}
\]
In particular, every outside vertex has a nonempty list.

## 4. Every outside clique can be coloured from its lists

**Lemma 2.** If \(Q\subseteq V(G)\setminus A\) is a clique, then its vertices can be assigned distinct colours from their lists \(L(x)\).

**Proof.** Since \(G\) is \(K_4\)-free, \(|Q|\le3\). By Hall’s theorem, it is enough to verify its condition for subsets of \(Q\) of sizes one, two and three.

The one-vertex condition follows from (2).

### Two vertices

A two-vertex Hall violation would consist of adjacent vertices \(x,y\) with
\[
L(x)=L(y)=\{c\}.
\]
For each \(c\), all neighbourhood types producing the singleton list \(\{c\}\) contain a common edge of \(A\):
\[
\begin{array}{c|c|c}
c&\text{possible neighbourhood types}&\text{common edge}\\ \hline
0&D_2&a_2a_4\\
1&D_4&a_4a_6\\
2&T_6,D_5,D_6&a_1a_6\\
3&D_0&a_0a_2 .
\end{array}
\]
That edge together with \(x,y\) would induce a \(K_4\), a contradiction.

### Three vertices

Suppose \(Q\) has three vertices and violates Hall’s condition. By the preceding paragraph,
\[
\bigcup_{x\in Q}L(x)=T
\]
for some two-element colour set \(T\).

If \(0\notin T\), every vertex of \(Q\) is adjacent to \(a_0\), the unique vertex of colour zero. Then \(Q\cup\{a_0\}\) is a \(K_4\). Hence
\[
T=\{0,c\},\qquad c\in\{1,2,3\}.
\]
Reversing the cyclic indexing interchanges colours \(1\) and \(3\), so it suffices to consider \(c=1,2\).

For compactness, write \(035\) for \(\{0,3,5\}\), and similarly for other index sets.

#### Case \(T=\{0,1\}\)

Lemma 1 and (2) show that
\[
S(x)\in
\{35,36,46,345,456,2345,3456,0456\}
\qquad(x\in Q).
\tag{3}
\]
Thus every \(x\in Q\) is nonadjacent to \(a_1\) and has a neighbour in \(\{a_3,a_4\}\).

For adjacent \(x,y\in Q\), the nonempty sets
\[
S(x)\cap\{3,4\},\qquad S(y)\cap\{3,4\}
\]
must intersect. Otherwise, after exchanging \(x,y\) if necessary,
\[
x,a_3,a_1,a_4,y,x
\]
would be an induced five-cycle.

The three nonempty subsets \(S(x)\cap\{3,4\}\), for \(x\in Q\), are therefore pairwise intersecting. A pairwise-intersecting family of nonempty subsets of a two-element set has a common element. Hence either \(a_3\) or \(a_4\) is adjacent to all three vertices of \(Q\), producing a \(K_4\).

#### Case \(T=\{0,2\}\)

This time the possible types are
\[
S(x)\in
\{15,16,25,26,016,0156,0126,2345\}.
\tag{4}
\]
At most one vertex of \(Q\) has type \(2345\): two such adjacent vertices, together with \(a_2,a_4\), would form a \(K_4\).

Choose two vertices \(x,y\in Q\) whose types are not \(2345\). Both are nonadjacent to \(a_3,a_4\), and both have neighbours in each of
\[
\{a_1,a_2\},\qquad \{a_5,a_6\}.
\]
Put
\[
U_z=S(z)\cap\{1,2\},\qquad
W_z=S(z)\cap\{5,6\}
\quad(z=x,y).
\]

If both
\[
U_x\cap U_y\ne\varnothing,\qquad
W_x\cap W_y\ne\varnothing,
\]
choose a common neighbour from each pair. Every vertex of \(\{a_1,a_2\}\) is adjacent to every vertex of \(\{a_5,a_6\}\); the two chosen vertices together with \(x,y\) form a \(K_4\).

Otherwise one intersection is empty.

* If \(U_x\cap U_y=\varnothing\), orient the names so that \(U_x=\{1\}\), \(U_y=\{2\}\). Then
  \[
  x,a_1,a_4,a_2,y,x
  \]
  is an induced \(C_5\).
* If \(W_x\cap W_y=\varnothing\), orient the names so that \(W_x=\{5\}\), \(W_y=\{6\}\). Then
  \[
  x,a_5,a_3,a_6,y,x
  \]
  is an induced \(C_5\).

Every possibility contradicts a hypothesis. This completes the three-vertex Hall check, and hence the proof. \(\square\)

## 5. Completion of the theorem

Each component \(Q\) of \(G-A\) is a clique of size at most three. By Lemma 2, colour \(Q\) properly from the lists \(L(x)\).

Different components have no edges between them, so these choices combine to extend the prescribed colouring of \(A\) to all of \(G\).

Since \(A\) contains a triangle and \(G\) is \(K_4\)-free,
\[
\omega(G)=3.
\]
Grouping colours \(0,1\) into one part and colours \(2,3\) into the other gives two induced subgraphs of clique number at most two. Thus no maximum clique is monochromatic. \(\square\)

The construction is explicit: once \(A\) is supplied, use (1), compute the lists, and for each outside clique inspect at most \(4^3=64\) assignments.

## 6. Consequences for the conjecture

### A necessary configuration in a clique-number-three counterexample

Suppose \(G\) is an odd-hole-free counterexample with \(\omega(G)=3\).

The Strong Perfect Graph Theorem implies that \(G\) contains an odd antihole, since perfect graphs with an edge admit a two-division. An odd antihole of length at least nine contains a \(K_4\), while a five-vertex antihole is a \(C_5\). Therefore \(G\) contains an induced \(\overline{C_7}\).

The theorem now gives the following necessary condition:

> For every induced \(\overline{C_7}\) with vertex set \(A\), the graph \(G-A\) contains an induced \(P_3\).

Indeed, graphs with no induced \(P_3\) are exactly cluster graphs.

### A fully proved small-order consequence

**Corollary.** Every odd-hole-free graph with at least one edge and at most nine vertices has the desired two-division.

**Proof.** Write \(n=|V(G)|\) and \(k=\omega(G)\).

* If \(k=2\), the graph is bipartite, as observed above.
* If \(k=3\), either \(G\) is perfect or it contains an induced \(\overline{C_7}\). In the latter case, at most two vertices remain outside that antihole, so the theorem applies.
* Suppose \(k\ge4\). For every graph,
  \[
  \chi(G)\le \left\lfloor\frac{n+\omega(G)}2\right\rfloor.
  \tag{5}
  \]
  To prove (5), repeatedly remove pairs of nonadjacent vertices until the remaining vertices form a clique. Give each removed pair its own colour and each remaining vertex its own colour. If \(s\le\omega(G)\) vertices remain, this uses \((n+s)/2\) colours.

  Here \(n\le9\le3k-3\), so
  \[
  \chi(G)\le
  \left\lfloor\frac{n+k}{2}\right\rfloor
  \le 2k-2.
  \]
  Partition these proper colours into two groups of at most \(k-1\) colours each. Neither group can contain a \(k\)-clique.

All cases are covered. \(\square\)

This corollary is a hand-proved finite verification, not a claim of a best known small-order bound.

## 7. What remains unproved

The extension lemma establishes all Hall conditions **on cliques** outside the antihole. When an outside component is not a clique, those local conditions do not by themselves yield a proper list-colouring of that component. The proof supplies no general extension argument in that situation.

Thus the unrestricted clique-number-three case remains unproved here, as does the full conjecture. The result above is a special-case theorem, not a resolution; I have not checked whether this particular extension lemma is already implicit in the literature.