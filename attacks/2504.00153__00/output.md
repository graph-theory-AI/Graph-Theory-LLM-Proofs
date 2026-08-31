```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove exact characterizations for edge-monotone classes, a bounded-adhesion closure theorem, and explicit shift-graph obstructions using interval, co-interval, complete multipartite, and line-graph factors, but not the general characterization.",
  "would_publish": false,
  "caveats": "Assumes finite simple graphs and the standard induced-subgraph meaning of χ-boundedness; overlap with the full source paper was not checked."
}
```

# Mathematical writeup

## 1. Conventions and summary

I use the standard robust definition: a class \(\mathcal D\) is \(\chi\)-bounded by \(f\) if
\[
 \chi(D[X])\le f(\omega(D[X]))
 \tag{1}
\]
for every \(D\in\mathcal D\) and every \(X\subseteq V(D)\). For hereditary classes this is the usual definition.

Thus, when factors have different vertex sets, they may be restricted to their common vertex set. All graphs below are finite and simple.

The main partial results are:

1. **Exact monotone classifications.**
   - A subgraph-closed class is intersectionwise \(\chi\)-guarding exactly when it has bounded chromatic number.
   - An induced-hereditary class closed under adding edges is guarding exactly when it has bounded independence number.

2. **A strong explicit obstruction.** There are interval graphs \(A_n\) and co-interval perfect graphs \(B_n\) such that
   \[
   A_n\cap B_n=S_n,
   \]
   where \(S_n\) is the triangle-free shift graph with \(\chi(S_n)\ge \lceil\log_2 n\rceil\). Consequently, neither the class of interval graphs nor the class of co-interval graphs is intersectionwise \(\chi\)-guarding.

3. Similar shift-graph representations use complete multipartite graphs and line graphs as the first factor. They imply several necessary conditions for finitely defined hereditary classes.

4. Classes admitting bounded-adhesion tree decompositions over guarding bags are guarding. In particular, chordal graphs whose clique trees have uniformly bounded adhesion form a guarding class.

These statements do not yield a converse for arbitrary hereditary classes.

---

## 2. Two elementary positive principles

### Lemma 2.1: bounded independence number

Let
\[
\mathcal A_a=\{A:\alpha(A)<a\}.
\]
Then \(\mathcal A_a\) is intersectionwise \(\chi\)-guarding.

#### Proof

Let \(\mathcal D\) be \(\chi\)-bounded by a nondecreasing function \(f\), and let
\[
G=A\cap B,\qquad A\in\mathcal A_a,\quad B\in\mathcal D,
\]
with \(\omega(G)\le q\).

If \(K\) is a clique of \(B\), then
\[
G[K]=A[K].
\]
Thus \(A[K]\) has no independent set of size \(a\) and no clique of size \(q+1\). With \(R(a,q+1)\) denoting the corresponding Ramsey number,
\[
|K|<R(a,q+1).
\]
Hence
\[
\omega(B)<R(a,q+1).
\]
Since \(G\subseteq B\),
\[
\chi(G)\le \chi(B)\le f(R(a,q+1)-1).
\]
This depends only on \(a,q\), and \(f\). \(\square\)

Classes of uniformly bounded chromatic number are even more directly guarding: if \(\chi(A)\le c\), then every \(A\cap B\) has chromatic number at most \(c\).

---

## 3. Exact characterizations for one-sided edge ideals

### Theorem 3.1

Let \(\mathcal C\) be an isomorphism-closed graph class.

1. If \(\mathcal C\) is closed under arbitrary subgraphs, the following are equivalent:
   \[
   \mathcal C\text{ is intersectionwise \(\chi\)-guarding};
   \]
   \[
   \mathcal C\text{ is \(\chi\)-bounded};
   \]
   \[
   \sup_{C\in\mathcal C}\chi(C)<\infty.
   \]

2. Suppose \(\mathcal C\) is induced-hereditary and closed under adding edges on a fixed vertex set. Then the following are equivalent:
   \[
   \mathcal C\text{ is intersectionwise \(\chi\)-guarding};
   \]
   \[
   \mathcal C\text{ is \(\chi\)-bounded};
   \]
   \[
   \sup_{C\in\mathcal C}\alpha(C)<\infty.
   \]

#### Proof

In either case, guarding implies \(\chi\)-boundedness: intersecting with the class of complete graphs returns every graph in \(\mathcal C\).

For part 1, suppose that a subgraph-closed \(\mathcal C\) is \(\chi\)-bounded. If \(\mathcal C\) had unbounded clique number, it would contain \(K_n\) for every \(n\). Since every \(n\)-vertex graph is a subgraph of \(K_n\), \(\mathcal C\) would contain every finite graph. This is not a \(\chi\)-bounded class, since triangle-free graphs can have arbitrarily large chromatic number. Hence \(\omega\) is uniformly bounded on \(\mathcal C\), and its \(\chi\)-bounding function gives a uniform bound on \(\chi\). The converse follows because
\[
\chi(A\cap B)\le \chi(A).
\]

For part 2, suppose that \(\alpha\) is unbounded on \(\mathcal C\). By induced heredity, \(I_n\in\mathcal C\) for every \(n\). By closure under adding edges, every \(n\)-vertex graph then belongs to \(\mathcal C\). Again this contradicts \(\chi\)-boundedness. Thus \(\alpha\) is bounded, and Lemma 2.1 shows that \(\mathcal C\) is guarding. \(\square\)

This completely answers the question for these two natural categories of graph classes.

---

## 4. The shift graph

For \(n\ge 2\), define the shift graph \(S_n\) by
\[
V(S_n)=\{(i,j):1\le i<j\le n\},
\]
with
\[
(i,j)(j,k)\in E(S_n)\qquad\text{whenever }i<j<k.
\]

### Lemma 4.1

For \(n\ge3\),
\[
\omega(S_n)=2
\quad\text{and}\quad
\chi(S_n)\ge \lceil\log_2 n\rceil.
\]

#### Proof

Vertices with the same first coordinate are nonadjacent. If a triangle existed, order its three first coordinates as \(a<b<c\). Adjacency between the vertices with first coordinates \(a,b\) forces the former vertex to be \((a,b)\), while adjacency between the vertices with first coordinates \(a,c\) forces it to be \((a,c)\), a contradiction. Thus \(S_n\) is triangle-free.

Now suppose \(S_n\) has a proper coloring with colors in \([c]\). Set
\[
C_i=\{\text{colors of }(i,j):j>i\},\qquad C_n=\varnothing.
\]
For \(i<j\), the color of \((i,j)\) lies in \(C_i\). It does not lie in \(C_j\), because \((i,j)\) is adjacent to every \((j,k)\), \(k>j\). Therefore \(C_i\ne C_j\). The \(n\) sets \(C_1,\dots,C_n\) are distinct subsets of \([c]\), so
\[
n\le 2^c.
\]
Hence \(c\ge\lceil\log_2n\rceil\). \(\square\)

---

## 5. Interval and co-interval graphs are not guarding

For each \((i,j)\in V(S_n)\), let
\[
I_{i,j}=[i,j].
\]

Define \(A_n\) to be the intersection graph of these closed intervals. Thus \(A_n\) is an interval graph.

Define \(B_n\) by declaring \((i,j)\) and \((k,\ell)\) adjacent when
\[
j\le k\quad\text{or}\quad \ell\le i.
\tag{2}
\]
In other words, one interval lies wholly to the left of the other, with touching allowed.

### Proposition 5.1

For every \(n\),
\[
A_n\cap B_n=S_n,
\]
and the hereditary closure of \(\{B_n:n\ge1\}\) is perfect. Moreover, each \(B_n\) is co-interval.

#### Proof

A pair satisfying \(j<k\) is adjacent in \(B_n\) but not in \(A_n\). A pair with overlapping interiors is adjacent in \(A_n\) but not in \(B_n\). It is adjacent in both exactly when
\[
j=k
\]
or symmetrically \(\ell=i\). These are precisely the shift edges.

For perfectness, define a strict partial order by
\[
(i,j)\prec(k,\ell)\quad\Longleftrightarrow\quad j\le k.
\]
Then \(B_n\) is its comparability graph. For completeness, on any induced subposet, color an element \(x\) by the maximum length of a chain ending at \(x\). Comparable elements receive different colors, and the number of colors is at most the maximum chain length, which is exactly the clique number of the comparability graph. Thus every induced subgraph \(H\) of \(B_n\) satisfies
\[
\chi(H)=\omega(H).
\]

Finally, \(\overline{B_n}\) is an interval graph: represent \((i,j)\) by
\[
J_{i,j}=[i+\tfrac13,j-\tfrac13].
\]
Two such intervals meet exactly when neither inequality in (2) holds. Hence \(B_n\) is co-interval. \(\square\)

### Corollary 5.2

Neither the class of interval graphs nor the class of co-interval graphs is intersectionwise \(\chi\)-guarding.

#### Proof

The intersection of the interval graphs \(A_n\) with the perfect co-interval graphs \(B_n\) contains the triangle-free graphs \(S_n\) of unbounded chromatic number. Reversing the roles of the two factors gives the co-interval assertion. \(\square\)

In particular, the class of chordal graphs is not guarding, since it contains all interval graphs.

---

## 6. Two further shift-graph factorizations

These give useful obstructions for finitely defined hereditary classes.

### 6.1 Complete multipartite first factors

Partition \(V(S_n)\) into
\[
P_i=\{(i,j):j>i\}.
\]
Let \(M_n\) be the complete multipartite graph with parts \(P_i\). Let \(D_n\) have:

- all edges of \(S_n\), and
- all pairs within each \(P_i\).

Then
\[
M_n\cap D_n=S_n.
\]

For any \(X\subseteq V(D_n)\), put \(r=\omega(D_n[X])\). Since each \(P_i\cap X\) is a clique,
\[
|P_i\cap X|\le r.
\]
Order vertices by increasing first coordinate, arbitrarily inside each \(P_i\). A vertex \((i,j)\) has at most \(r-1\) later neighbors in \(P_i\), and at most \(r\) later shift-neighbors in \(P_j\). Thus every vertex has at most \(2r-1\) later neighbors. Consequently
\[
\chi(D_n[X])\le 2r.
\]
The hereditary closure of the \(D_n\) is therefore \(\chi\)-bounded by \(2r\).

Hence:

\[
\boxed{\text{The class of complete multipartite graphs is not guarding.}}
\]

### 6.2 Line-graph first factors

Let
\[
L_n=L(K_n),
\]
on the same vertex set \(\binom{[n]}2\). Every shift edge is an edge of \(L_n\).

Define \(E_n\) by making two \(2\)-subsets adjacent if either

1. they are disjoint, or
2. they form a shift pair \(\{i,j\},\{j,k\}\) with \(i<j<k\).

Then
\[
L_n\cap E_n=S_n.
\]

Let \(X\subseteq V(E_n)\), regard \(X\) as an edge set of a graph \(F\) on \([n]\), and put \(r=\omega(E_n[X])\). A matching in \(F\) is a clique in \(E_n[X]\), so \(\nu(F)\le r\). The endpoints \(U\) of a maximal matching form a vertex cover and satisfy
\[
|U|\le 2r.
\]
Assign each edge of \(F\) to one of its endpoints in \(U\). For fixed \(u\in U\), two assigned edges \(\{u,x\}\) and \(\{u,y\}\) are adjacent exactly when \(x<u<y\) or \(y<u<x\). Thus each assigned group induces a bipartite graph. Using separate two-color palettes for the elements of \(U\),
\[
\chi(E_n[X])\le 2|U|\le4r.
\]
Therefore the hereditary closure of the \(E_n\) is \(\chi\)-bounded.

Since line graphs are claw-free, this proves in particular:

\[
\boxed{\text{The class of claw-free graphs is not guarding.}}
\]

Indeed, the same conclusion holds for the class of \(K_{1,t}\)-free graphs for every \(t\ge3\).

---

## 7. Consequences for finite forbidden induced-subgraph sets

Let \(\mathcal H\) be finite, and let
\[
\operatorname{Forb}(\mathcal H)
\]
denote the class of graphs containing no member of \(\mathcal H\) as an induced subgraph.

### Theorem 7.1: necessary hitting conditions

If \(\operatorname{Forb}(\mathcal H)\) is intersectionwise \(\chi\)-guarding, then \(\mathcal H\) contains:

1. a forest;
2. a complete multipartite graph;
3. a line graph;
4. an interval graph;
5. a co-interval graph.

The five graphs need not be the same member of \(\mathcal H\).

#### Proof

For the first condition, guarding implies ordinary \(\chi\)-boundedness. If every \(H\in\mathcal H\) contains a cycle, let
\[
m=\max_{H\in\mathcal H}|V(H)|.
\]
Graphs of girth greater than \(m\) avoid every member of \(\mathcal H\). The standard high-girth/high-chromatic construction then shows that \(\operatorname{Forb}(\mathcal H)\) is not \(\chi\)-bounded.

For each remaining condition, use the corresponding hereditary host class from Sections 5 and 6. For example, if no member of \(\mathcal H\) is an interval graph, then every interval graph \(A_n\) is \(\mathcal H\)-free: an induced subgraph of an interval graph is again an interval graph. But \(A_n\cap B_n=S_n\), with the \(B_n\) belonging to a perfect class, contradicting guarding. The complete multipartite, line-graph, and co-interval cases are identical. \(\square\)

For \(|\mathcal H|=1\), these obstructions recover the announced single-forbidden characterization. A graph that is both a forest and complete multipartite is either:

- an independent set, or
- a star \(K_{1,t}\).

The line-graph condition excludes \(K_{1,t}\) for \(t\ge3\). Thus the only possibilities are
\[
I_t,\qquad K_2,\qquad P_3.
\]
They are indeed sufficient:

- \(\operatorname{Forb}(I_t)\) is guarding by Lemma 2.1.
- \(\operatorname{Forb}(K_2)\) consists of edgeless graphs.
- A \(P_3\)-free graph is a disjoint union of cliques. If \(G=A\cap B\) and \(C\) is a component of \(A\), then \(G[C]=B[C]\); different components are anticomplete in \(G\). Hence if \(\omega(G)\le q\),
  \[
  \chi(G)=\max_C\chi(B[C])\le f(q).
  \]

This is a rederivation, not an improvement, of the single-forbidden result stated in the catalog.

### A simple sufficient finite-family case

If
\[
K_s,\ K_{1,t}\in\mathcal H,
\]
then \(\operatorname{Forb}(\mathcal H)\) has uniformly bounded chromatic number and is therefore guarding.

Indeed, in a \(K_s\)-free, \(K_{1,t}\)-free graph, the neighborhood of any vertex contains neither a clique of size \(s-1\) nor an independent set of size \(t\). Hence
\[
\Delta(G)<R(s-1,t),
\]
and so
\[
\chi(G)\le R(s-1,t).
\]
For example, the class of triangle-free claw-free graphs has maximum degree at most \(2\), even though neither the class of triangle-free graphs nor the class of claw-free graphs is guarding by itself.

---

## 8. A bounded-adhesion closure theorem

The following gives a positive decomposition principle.

### Lemma 8.1: coloring through bounded adhesion

Suppose \(G\) has a tree decomposition \((T,\{X_t\}_{t\in V(T)})\) of adhesion at most \(s\), and
\[
\chi(G[X_t])\le c
\]
for every bag. Then
\[
\chi(G)\le c(s+1).
\]

#### Proof

Root \(T\). For each vertex \(v\), the bags containing \(v\) form a subtree; assign \(v\) to its highest bag \(t(v)\). Process bags from the root downwards.

Fix a proper coloring
\[
\lambda_t:G[X_t]\to[c]
\]
for each bag. When processing a vertex \(v\) assigned to \(t\), use a color
\[
(\lambda_t(v),a(v)),\qquad a(v)\in\{0,\dots,s\}.
\]
All previously colored neighbors of \(v\) lie in the adhesion set between \(t\) and its parent, which has size at most \(s\). Therefore one can choose \(a(v)\) avoiding the second coordinates of all previously colored neighbors having first coordinate \(\lambda_t(v)\). Edges between vertices assigned to the same bag are distinguished by their first coordinates. This yields a proper \(c(s+1)\)-coloring. \(\square\)

### Theorem 8.2

Let \(\mathcal C_0\) be intersectionwise \(\chi\)-guarding. Fix \(s\). Suppose every \(A\in\mathcal C\) has a tree decomposition of adhesion at most \(s\) such that
\[
A[X_t]\in\mathcal C_0
\]
for every bag \(X_t\). Then \(\mathcal C\) is intersectionwise \(\chi\)-guarding.

#### Proof

Let \(\mathcal D\) be \(\chi\)-bounded and let \(G=A\cap B\) with \(\omega(G)\le q\). Since \(\mathcal C_0\) is guarding, there is a bound \(c(q)\) such that
\[
\chi(G[X_t])
 =\chi(A[X_t]\cap B[X_t])
 \le c(q)
\]
for every bag. The same bags form a tree decomposition of \(G\), so Lemma 8.1 gives
\[
\chi(G)\le (s+1)c(q).
\]
\(\square\)

### Corollary 8.3

Fix \(s\). The class of chordal graphs admitting a clique tree in which adjacent maximal cliques intersect in at most \(s\) vertices is intersectionwise \(\chi\)-guarding.

Indeed, every bag is a clique in the chordal factor, so on that bag the intersection equals the corresponding induced subgraph of the other factor. If the latter is \(\chi\)-bounded by \(f\), the explicit bound is
\[
\chi(A\cap B)\le (s+1)f(\omega(A\cap B)).
\]

The unrestricted class of chordal graphs is not guarding by Corollary 5.2, so some restriction of this kind is genuinely needed.

---

## 9. Remaining gap

The results above leave a substantial gap:

- The finite-forbidden hitting conditions in Theorem 7.1 are only necessary.
- The bounded-partition and bounded-adhesion constructions are only sufficient.
- No argument here shows that every guarding hereditary class admits either type of decomposition.
- In particular, I do not obtain a structural converse encompassing arbitrary hereditary classes.

There is also a definitional caveat. If “\(\chi\)-bounded” were interpreted as bounding only whole members of a possibly nonhereditary class, while factors were allowed to have extraneous vertices, the question would behave pathologically. For example, take triangle-free \(H_n\) with \(\chi(H_n)\to\infty\), let
\[
B_n=H_n\mathbin{\dot\cup}K_{m_n}
\]
with \(m_n\ge\chi(H_n)\) strictly increasing, and intersect \(B_n\) with a complete graph whose vertex set is only \(V(H_n)\). The weakly \(\chi\)-bounded class \(\{B_n\}\) would then produce the \(H_n\). Thus the induced-subgraph convention (1), or an equivalent hereditary convention, is essential.