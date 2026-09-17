```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove that every four-colouring of an induced seven-antihole extends over a 2-choosable remainder in a (K4,C5)-free graph, giving a restricted case that includes arbitrary forest remainders.",
  "would_publish": false,
  "caveats": "The full conjecture remains unresolved here; novelty of the extension theorem has not been checked, and the substantive statement excludes edgeless graphs."
}
```

# A precolouring-extension theorem for 2-choosable remainders

I do not resolve the full conjecture. I obtain a stronger extension result than the clique-remainder result in the previous attempt: **arbitrary forest remainders are allowed**, as are all 2-choosable remainders.

I reprove the attachment classification used in that attempt. The additional ingredient is a forcing procedure whose safety follows from the exclusion of \(K_4\) and induced \(C_5\)'s.

All graphs below are finite and simple. As in the previous attempt, “non-empty” is interpreted substantively as having an edge: an edgeless graph with vertices has singleton maximum cliques, so cannot satisfy the stated colouring conclusion.

## 1. Partial theorem

A graph is **2-choosable** if every assignment of a two-element list of colours to each vertex admits a proper colouring from those lists. In particular:

* forests are 2-choosable;
* a connected unicyclic graph is 2-choosable when its unique cycle is even;
* every 2-choosable graph is bipartite.

Here is the result.

**Theorem.** Let \(G\) be a graph with no \(K_4\) and no induced \(C_5\), and let \(A\subseteq V(G)\) induce \(\overline{C_7}\). Suppose that each component of \(G-A\) is either 2-choosable or a triangle. Then every proper four-colouring of \(G[A]\) extends to a proper four-colouring of \(G\).

Consequently, \(G\) admits a two-colouring with no monochromatic maximum clique.

Thus the theorem applies, for example, when every component of \(G-A\) is a tree, an even unicyclic graph, or a triangle. It includes the clique-remainder theorem in the previous attempt.

### Relation to the conjecture

For an odd-hole-free graph with clique number three, the requested two-division is equivalent to four-colourability.

Indeed, each part of a two-division is triangle-free and odd-hole-free, hence bipartite: a shortest odd cycle in a triangle-free non-bipartite graph is an induced odd cycle of length at least five. Conversely, grouping four proper colours into two pairs produces two triangle-free parts.

The theorem therefore proves the exact desired property in the stated restricted class, not merely an approximate colouring bound.

---

## 2. Attachments and colour lists

Label the antihole
\[
A=\{a_0,\ldots,a_6\},
\]
with indices modulo seven, so that distinct \(a_i,a_j\) are nonadjacent precisely when \(i,j\) are consecutive on the underlying seven-cycle.

For \(x\notin A\), write
\[
S(x)=\{i:a_i\in N(x)\}.
\]
Put
\[
T_i=\{i,i+1,i+2\},\qquad
D_i=\{i,i+1,i+2,i+3\}.
\]
In tables, a string such as \(16\) denotes the set \(\{1,6\}\).

### Lemma 1: possible neighbourhoods

Every \(S(x)\) is one of
\[
\varnothing,\quad
\{i\},\quad
\{i,j\}\text{ with }i,j\text{ nonconsecutive},\quad
T_i,\quad D_i.
\tag{1}
\]

**Proof.**
Let \(C\) be the underlying seven-cycle. Since \(G\) is \(K_4\)-free,
\[
\alpha(C[S(x)])\le 2.
\]
Otherwise three independent vertices of \(C[S(x)]\) form a triangle in \(G[A]\), which together with \(x\) is a \(K_4\).

In particular \(S(x)\ne V(C)\), so \(C[S(x)]\) is a union of paths. It cannot have a component consisting of exactly two vertices. If
\[
i,i+1\in S(x),\qquad i-1,i+2\notin S(x),
\]
then
\[
x,a_i,a_{i+2},a_{i-1},a_{i+1},x
\]
is an induced \(C_5\).

A path on at least five vertices has independence number at least three. A path on three or four vertices already has independence number two, so cannot accompany another component. What remains is exactly (1). ∎

### Normalizing the antihole colouring

Every proper four-colouring of \(A\) can be normalized, by rotating the indices and renaming colours, to
\[
\begin{array}{c|ccccccc}
 &a_0&a_1&a_2&a_3&a_4&a_5&a_6\\ \hline
\text{colour}&0&1&1&2&2&3&3.
\end{array}
\tag{2}
\]
Indeed, the colour-class sizes must be \(1,2,2,2\), and each two-vertex class is a consecutive pair on \(C\). Removing the singleton leaves a six-vertex path whose perfect matching is unique.

Let \(L(x)\) be the colours not used on \(N(x)\cap A\). These are the permissible colours for \(x\).

The singleton lists are exactly
\[
\begin{array}{c|c}
L(x)&S(x)\\ \hline
\{0\}&D_2\\
\{1\}&D_4\\
\{2\}&T_6,D_5,D_6\\
\{3\}&D_0.
\end{array}
\tag{3}
\]
The two-element lists are exactly
\[
\begin{array}{c|l}
L(x)&S(x)\\ \hline
\{0,1\}&35,36,46,T_3,T_4,D_3\\
\{0,2\}&15,16,25,26\\
\{0,3\}&13,14,24,T_1,T_2,D_1\\
\{1,2\}&05,T_5\\
\{1,3\}&03,04\\
\{2,3\}&02,T_0.
\end{array}
\tag{4}
\]
A singleton neighbourhood gives a three-element list, and the empty neighbourhood gives all four colours. In particular, every list is nonempty.

---

## 3. Two elementary compatibility tests

We will repeatedly use the following tests for adjacent vertices \(x,y\notin A\), with neighbourhood types \(S=S(x)\), \(T=S(y)\).

* **\(K_4\) test.** The intersection \(S\cap T\) cannot contain two nonconsecutive indices, since those two antihole vertices together with \(x,y\) would form a \(K_4\).

* **\(C_5\) test.** Suppose \(r\in S\setminus T\) and \(s\in T\setminus S\) are consecutive on \(C\). There cannot be
  \[
  t\notin S\cup T
  \]
  that is nonconsecutive to both \(r\) and \(s\). Otherwise
  \[
  x,a_r,a_t,a_s,y,x
  \]
  is an induced \(C_5\).

For \(s=r+1\), the possible \(t\)'s in the second test are exactly
\[
r+3,\ r+4,\ r+5 \pmod 7.
\tag{5}
\]

The finite tables below are obtained by applying these two tests to the complete list (4). Thus the enumeration is fully specified; no computational search or additional attachment assumption is being invoked.

We also use the reflection
\[
i\longmapsto -i,
\tag{6}
\]
which interchanges colours \(1,3\) and fixes colours \(0,2\).

---

## 4. Safe forcing when the remainder is triangle-free

For this section assume
\[
H=G-A
\]
is triangle-free. Later, 2-choosability will supply both this assumption and the final list-colouring step.

Initially assign every vertex with a singleton list its unique colour. We will then propagate assignments through vertices whose original lists have size two.

### 4.1 Possible forced states

Call the vertex responsible for a propagated assignment its **precursor**: if \(v\) has original list \(\{c,d\}\), an already assigned neighbour of colour \(c\) can force \(v\) to colour \(d\).

The only propagated states that will be needed are
\[
\begin{array}{c|c|c}
S(v)&\text{assigned colour}&\text{possible types of a precursor}\\ \hline
T_3&0&D_4,T_4\\
T_2&0&D_0,T_1\\
T_4&1&D_2,T_3\\
T_5&1&T_6,D_6\\
16&2&D_2\\
T_1&3&D_2,T_2\\
T_0&3&T_6,D_5.
\end{array}
\tag{7}
\]
Initial assignments are those in (3), and have no precursor.

For clarity, the complete families of types assigned each colour are therefore
\[
\begin{aligned}
\mathcal F_0&=\{D_2,T_3,T_2\},\\
\mathcal F_1&=\{D_4,T_4,T_5\},\\
\mathcal F_2&=\{T_6,D_5,D_6,16\},\\
\mathcal F_3&=\{D_0,T_1,T_0\}.
\end{aligned}
\tag{8}
\]

We prove three facts:

1. forcing preserves (7);
2. assignments satisfying (3), (7) are proper;
3. vertices whose original lists have size at least three retain at least two available colours.

These facts make the forcing procedure safe.

### 4.2 Closure under forcing

First suppose the assigned neighbour has a singleton original list. The compatibility tests give the following complete table. It lists adjacent types with a two-element original list containing the assigned colour.
\[
\begin{array}{c|c|l}
\text{assigned type}&\text{colour}&
(\text{neighbour type},\text{resulting colour})\\ \hline
D_2&0&(T_4,1),(16,2),(T_1,3)\\
D_4&1&(T_3,0)\\
D_0&3&(T_2,0)\\
T_6&2&(T_5,1),(T_0,3)\\
D_5&2&(T_0,3)\\
D_6&2&(T_5,1).
\end{array}
\tag{9}
\]
This gives the initial instances of (7).

Now suppose an assigned vertex \(u\) was itself propagated, with precursor \(p\), and \(v\) is an unassigned neighbour whose two-element original list contains the colour of \(u\). Since \(H\) is triangle-free, \(p,u,v\) is an induced path.

Up to reflection (6), the compatibility tests give:
\[
\begin{array}{c|c|l|l}
S(u)&\text{colour}&
\text{type retained for }v&
\text{other candidate types for }v\\ \hline
T_3&0&T_4&15,13,14,T_1,T_2,D_1\\
T_4&1&T_3&T_5\\
T_5&1&\text{none}&35,36,T_3,T_4,D_3,03\\
16&2&\text{none}&\text{none}.
\end{array}
\tag{10}
\]
Here “candidate” means surviving the two-vertex tests; the precursor eliminates the last column:

* If \(S(u)=T_3\), then \(S(p)\in\{D_4,T_4\}\). Every discarded type contains an index \(r\in\{1,2\}\). Neither \(u\) nor \(v\) sees \(a_6\), while \(p\) sees \(a_6\) and does not see \(a_r\). Hence
  \[
  p,u,v,a_r,a_6,p
  \]
  is an induced \(C_5\).

* If \(S(u)=T_4\), its discarded neighbour has type \(T_5\), and \(S(p)\in\{D_2,T_3\}\). Then
  \[
  p,u,v,a_0,a_3,p
  \]
  is an induced \(C_5\).

* If \(S(u)=T_5\), then \(S(p)\in\{T_6,D_6\}\). Every discarded type contains an index \(r\in\{3,4\}\), and
  \[
  p,u,v,a_r,a_1,p
  \]
  is an induced \(C_5\).

Reflection handles the other propagated states. Thus every new assignment has one of the types and precursors prescribed by (7).

### 4.3 The assigned vertices are properly coloured

Any two types in the same family \(\mathcal F_c\) have a common antihole edge, except for the three unordered pairs
\[
\{T_3,T_2\},\qquad
\{T_4,T_5\},\qquad
\{T_1,T_0\}.
\tag{11}
\]
A common antihole edge forbids adjacency by the \(K_4\) test.

The exceptional pairs cannot be adjacent either. The following table supplies an induced \(C_5\) if they are:
\[
\begin{array}{c|c|c|c}
S(u)&S(v)&S(p),\ p\text{ a precursor of }u&
\text{induced cycle}\\ \hline
T_3&T_2&D_4\text{ or }T_4&p,u,v,a_2,a_6,p\\
T_4&T_5&D_2\text{ or }T_3&p,u,v,a_0,a_3,p\\
T_1&T_0&D_2\text{ or }T_2&p,u,v,a_0,a_4,p.
\end{array}
\tag{12}
\]
The three outside vertices form an induced path because \(H\) is triangle-free.

Thus no adjacent assigned vertices receive the same colour. The assignments also respect \(A\), since every assigned colour belongs to the corresponding original list.

### 4.4 Larger original lists retain at least two colours

We need a small observation about types from different families.

Except for the two nested pairs
\[
T_5\subset D_5
\quad\text{with colours }1,2,
\qquad
T_0\subset D_6
\quad\text{with colours }3,2,
\tag{13}
\]
types \(S\in\mathcal F_c\), \(T\in\mathcal F_d\), \(c\ne d\), have indices
\[
r\in S\setminus T,\qquad s\in T\setminus S
\]
such that \(a_ra_s\) is an edge.

Here is a complete witness table; it also verifies the stated exceptions.
\[
\begin{array}{c|l|c}
(c,d)&\text{condition}&(r,s)\\ \hline
(0,1)&\text{always}&(3,6)\\
(0,2)&T=16&(4,1)\\
(0,2)&T\ne16&(3,0)\\
(0,3)&\text{always}&(4,1)\\
(1,2)&T\ne D_5&(5,1)\\
(1,2)&T=D_5,\ S\ne T_5&(4,1)\\
(1,3)&\text{always}&(5,1)\\
(2,3)&S\ne D_6&(6,2)\\
(2,3)&S=D_6,\ T\ne T_0&(6,3).
\end{array}
\tag{14}
\]

Let \(x\) be an unassigned vertex.

#### Empty neighbourhood in \(A\)

Suppose \(S(x)=\varnothing\), so \(|L(x)|=4\). Any two assigned neighbours of \(x\) are nonadjacent, because \(H\) is triangle-free.

If they have different colours and are not one of the exceptional pairs (13), the edge supplied by (14) gives an induced cycle
\[
x,y,a_r,a_s,z,x.
\]
Consequently, three distinct colours cannot occur among assigned neighbours of \(x\): among any three colours, at least one pair is not an exception in (13). At most two colours are removed from \(L(x)\), leaving at least two.

#### Singleton neighbourhood in \(A\)

Suppose \(S(x)=\{i\}\), so \(|L(x)|=3\).

First, every assigned neighbour \(y\) whose colour belongs to \(L(x)\) must itself see \(a_i\). Here are the details.

For a type \(T_j\), a singleton type \(\{i\}\) with \(i\notin T_j\) can survive the \(C_5\) compatibility test only for
\[
i=j+4\quad\text{or}\quad i=j+5.
\]
For \(D_j\), only \(i=j+5\) survives. For type \(16\), only \(i=3,4\) survive.

Using the assigned colours in (3), (7), the only surviving cases with \(i\notin S(y)\) and the colour of \(y\) in \(L(x)\) are
\[
\begin{array}{c|c|c}
S(y)&i&q\\ \hline
T_3&1&6\\
T_2&6&1\\
T_5&3&1\\
T_0&4&6.
\end{array}
\tag{15}
\]
If \(p\) is the precursor of \(y\), its prescribed type in (7) sees \(a_q\) and does not see \(a_i\). In each row,
\[
p,y,x,a_i,a_q,p
\]
is an induced \(C_5\), again because \(p,y,x\) is an induced path. This proves the assertion.

Now suppose assigned neighbours \(y,z\) remove two distinct colours from \(L(x)\). Both see \(a_i\). Unless their types form one of (13), table (14) supplies an exclusive edge \(a_ra_s\). Since \(i\) belongs to both types, \(r,s\ne i\), and
\[
x,y,a_r,a_s,z,x
\]
is an induced \(C_5\).

It remains to exclude (13). Suppose \(S(y)=T_5\), with colour \(1\), and \(S(z)=D_5\), with colour \(2\). The precursor \(p\) of \(y\) has type \(T_6\) or \(D_6\). The four vertices \(p,y,x,z\) form an induced path:

* \(px\) and \(yz\) are absent because \(H\) is triangle-free;
* \(pz\) is absent because both \(p,z\) see the antihole edge \(a_1a_6\), so \(pz\) would create a \(K_4\).

Also \(i\in T_5=\{0,5,6\}\). Therefore
\[
p,y,x,z,a_1,p
\]
is an induced \(C_5\). The other exceptional pair follows by reflection.

Thus at most one colour is removed from a three-element original list. It retains at least two colours.

This proves the required larger-list assertion.

---

## 5. Completing the extension over a 2-choosable remainder

Suppose now that \(H=G-A\) is 2-choosable. In particular it is triangle-free.

Start with all singleton-list assignments. Repeatedly do the following:

> If an unassigned vertex \(v\) has an original two-element list and an assigned neighbour whose colour belongs to that list, assign \(v\) the other colour.

Section 4.2 shows that every assignment satisfies the prescribed forced-state rules. Section 4.3 shows that it is proper, including with respect to previously assigned neighbours. Thus a two-element list is never exhausted by conflicting assignments.

The procedure terminates after at most \(|V(H)|\) assignments. At termination:

* every unassigned vertex with an original two-element list still has both colours available;
* every unassigned vertex with an original list of size at least three has at least two colours available, by Section 4.4.

Induced subgraphs of 2-choosable graphs are 2-choosable. Restrict each remaining available list to any two colours and colour the remaining induced subgraph from those lists.

This completes the extension over a 2-choosable remainder. ∎

Notice that the forcing argument itself used only triangle-freeness of the remainder. The 2-choosability assumption is used for the final completion.

---

## 6. Triangular components

For completeness, here is a verification of the additional triangle case, rather than an appeal to the previous attempt.

Let \(Q\) be an outside triangle. Its lists admit distinct representatives.

The one-vertex Hall condition follows from nonempty lists. A two-vertex Hall failure would require adjacent vertices with the same singleton list. For each colour, all types in (3) producing that singleton list contain a common antihole edge; hence such adjacency would produce a \(K_4\).

Suppose the three-vertex Hall condition fails. The union of the three lists is then a two-element set \(B\).

If \(0\notin B\), every vertex of \(Q\) sees \(a_0\), giving a \(K_4\). Thus \(B=\{0,c\}\). By reflection, it suffices to consider \(c=1,2\).

### Case \(B=\{0,1\}\)

Tables (3), (4) give the possible types
\[
35,36,46,T_3,T_4,D_3,D_2,D_4.
\]
Every such vertex misses \(a_1\) and has a neighbour in \(\{a_3,a_4\}\).

For adjacent \(x,y\in Q\), their nonempty neighbourhoods in \(\{a_3,a_4\}\) must intersect. Otherwise
\[
x,a_3,a_1,a_4,y,x
\]
is an induced \(C_5\), after interchanging \(x,y\) if necessary.

Three pairwise-intersecting nonempty subsets of a two-element set have a common element. Hence \(Q\) has a common neighbour in \(\{a_3,a_4\}\), producing a \(K_4\).

### Case \(B=\{0,2\}\)

The possible types are
\[
15,16,25,26,T_6,D_5,D_6,D_2.
\]
At most one vertex of \(Q\) has type \(D_2\), since two adjacent such vertices have a common antihole edge.

Choose two vertices \(x,y\) not of type \(D_2\). Both miss \(a_3,a_4\), and both have neighbours in each of
\[
U=\{a_1,a_2\},\qquad W=\{a_5,a_6\}.
\]
If they have a common neighbour in each of \(U,W\), those two common neighbours together with \(x,y\) form a \(K_4\).

Otherwise their neighbourhoods in one of the two pairs are disjoint. In the first pair this gives an induced cycle
\[
x,a_1,a_4,a_2,y,x;
\]
in the second it gives
\[
x,a_5,a_3,a_6,y,x.
\]
Both contradict \(C_5\)-freeness.

Hall’s condition therefore holds, so \(Q\) can be properly coloured from its lists.

Different components of \(G-A\) have no edges between them. We may consequently colour each 2-choosable component by Section 5 and each triangular component by the argument above. This proves the theorem in its stated form.

Since \(A\) contains a triangle and \(G\) is \(K_4\)-free, \(\omega(G)=3\). Grouping the four proper colours into two pairs gives the required two-division. ∎

---

## 7. Explicit consequences

### Forest and even-unicyclic remainders

Every forest is 2-choosable by leaf removal.

For an even cycle with two-element lists, if all lists agree, use the two colours alternately. Otherwise choose adjacent vertices with different lists, colour one with a colour absent from the other’s list, and greedily colour around the cycle toward the latter vertex. The last vertex then has at most one forbidden colour from its list. Trees attached to the cycle can subsequently be coloured outward.

Hence the theorem gives, in particular:

**Corollary.** Let \(G\) be odd-hole-free with \(\omega(G)=3\), and suppose \(G\) contains an induced \(\overline{C_7}\) with vertex set \(A\). If every component of \(G-A\) is a tree, an even unicyclic graph, or a triangle, then \(G\) has the required two-division.

This includes arbitrarily large trees and arbitrarily large even cycles outside the antihole, rather than only outside cliques.

### Necessary structure of a clique-number-three counterexample

Suppose an odd-hole-free graph \(G\) with \(\omega(G)=3\) is a counterexample.

It is not perfect. By the Strong Perfect Graph Theorem, it contains an odd antihole. A five-antihole is a forbidden \(C_5\), and an odd antihole of length at least nine contains a \(K_4\). Thus \(G\) contains an induced \(\overline{C_7}\).

The theorem implies:

> For every induced seven-antihole \(A\), some component of \(G-A\) is neither 2-choosable nor a triangle.

In particular, deleting a seven-antihole cannot leave a forest. This strengthens the previous attempt’s necessary condition that the remainder contain an induced \(P_3\).

The proof is constructive once \(A\) is supplied: compute the lists, run the forcing procedure, and finish the residual two-list instance. For forest or even-unicyclic remainders, the final colouring has the explicit greedy construction just described.

---

## 8. What remains unresolved

The unrestricted conjecture is not proved.

The principal limitation is the final list-colouring step. The forcing argument leaves at least two available colours at every remaining vertex, but a general bipartite graph need not be 2-choosable. I have not proved that the particular residual lists arising here avoid all such list-colouring obstructions.

Moreover, the safe forcing argument relies on a triangle-free outside component; the separate Hall argument handles an isolated triangular component, not arbitrary components containing triangles.

Thus this is a proved special case and a structural restriction on possible clique-number-three counterexamples. I have not checked whether the extension theorem, or an equivalent formulation of it, already appears in the literature.