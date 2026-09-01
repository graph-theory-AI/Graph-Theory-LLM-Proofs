```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard normalization one has R(n) ≤ 2G(n), and a weak converse can be proved only after a very large change of the star parameter; the same-parameter reverse bound remains open.",
  "would_publish": false,
  "caveats": "\"Roughly the same order\" is undefined, and the unretrieved 2025 citation is not used."
}
```

# Mathematical writeup

## 1. Formalization

Write
\[
R(n)=r(K_4^{(3)},S_n^{(3)}).
\]

Let \(G(n)=\operatorname{gr}(G_{2\times2},K_n)\) denote the least \(N\) such that every red-blue coloring of \(K_N\square K_N\) contains either

* a red canonical rectangle, or
* a blue \(K_n\), necessarily contained in a row or column.

Index the rows and columns by \([N]\). Write

* \(h_i(j,k)\) for the color of the horizontal edge in row \(i\) between columns \(j,k\);
* \(v_j(i,k)\) for the color of the vertical edge in column \(j\) between rows \(i,k\).

Thus a red rectangle on rows \(i,i'\) and columns \(j,j'\) means that
\[
h_i(j,j'),\quad h_{i'}(j,j'),\quad
v_j(i,i'),\quad v_{j'}(i,i')
\]
are all red.

The phrase “roughly the same order” has no formal truth value. The strongest natural interpretation is
\[
R(n)=\Theta(G(n)).
\tag{1}
\]
A weaker possible interpretation is polynomial equivalence,
\[
G(n)\le R(n)^{O(1)}
\quad\text{and}\quad
R(n)\le G(n)^{O(1)}.
\tag{2}
\]
The arguments below address (1), while also identifying what is missing for (2).

---

## 2. The elementary one-sided comparison

### Proposition 1
For every \(n\ge2\),
\[
R(n)\le 2G(n).
\tag{3}
\]

### Proof

Suppose, toward a contradiction, that there is a red-blue coloring of the triples of a set \(X\cup Y\), where
\[
|X|=|Y|=G(n),
\]
containing neither a red \(K_4^{(3)}\) nor a blue \(S_n^{(3)}\).

Construct a grid coloring with rows indexed by \(X\) and columns indexed by \(Y\) as follows:

* color the horizontal edge in row \(x\), between columns \(y,y'\), by the color of the triple \(\{x,y,y'\}\);
* color the vertical edge in column \(y\), between rows \(x,x'\), by the color of the triple \(\{x,x',y\}\).

If rows \(x,x'\) and columns \(y,y'\) form a red rectangle, then the four triples
\[
\{x,y,y'\},\quad
\{x',y,y'\},\quad
\{x,x',y\},\quad
\{x,x',y'\}
\]
are all red. These are precisely the four triples on
\(\{x,x',y,y'\}\), giving a red \(K_4^{(3)}\), a contradiction.

If a row \(x\) contains a blue \(K_n\) on columns \(y_1,\dots,y_n\), then all triples
\[
\{x,y_i,y_j\},\qquad 1\le i<j\le n,
\]
are blue. They form a blue \(S_n^{(3)}\) centered at \(x\). The argument for a blue \(K_n\) in a column is identical.

Thus the induced \(G(n)\times G(n)\) grid coloring contains neither target, contradicting the definition of \(G(n)\). ∎

Consequently, under interpretation (1), the entire unresolved direction is
\[
G(n)=O(R(n)).
\tag{4}
\]

In particular, the relation \(R(n)\le 2^{G(n)}\) stated in the prompt is far weaker than what follows directly from the standard definitions. It is possible that \(2\,\operatorname{gr}\) was transcribed as \(2^{\operatorname{gr}}\); in any event, (3) is self-contained.

The factor \(2\) in (3) cannot be uniformly reduced without an additive term: for \(n=2\),
\[
G(2)=2,\qquad R(2)=4.
\]
Indeed, avoiding a blue \(K_2\) forces every grid edge red, and \(K_2\square K_2\) is then a red rectangle. Also, \(S_2^{(3)}\) is a single triple, so on four vertices either some triple is blue or all four triples form a red \(K_4^{(3)}\).

---

## 3. Reformulation as a completion problem

A grid coloring is equivalently a coloring of all triples in \(X\cup Y\) that meet both \(X\) and \(Y\):

* triples of type \(XYY\) encode horizontal edges;
* triples of type \(XXY\) encode vertical edges.

The absence of a red rectangle says that there is no red \(K_4^{(3)}\) with two vertices in each part. The absence of a blue grid \(K_n\) says that there is no blue star whose center is in one part and whose leaves all lie in the other part.

Thus the missing implication (4) is essentially a completion problem:

> Given a large coloring of the mixed triples with these two properties, can one pass to a linear-sized subconfiguration and color the triples internal to \(X\) and \(Y\) so as to avoid every red \(K_4^{(3)}\) and every blue \(S_n^{(3)}\)?

There are two genuine additional obstructions:

1. A red \(K_4^{(3)}\) of type \(3+1\), which is not visible as a grid rectangle.
2. A blue star whose leaves meet both parts, or whose leaves largely lie in the same part.

These are exactly the cases not controlled by the grid hypotheses.

---

## 4. A simple converse with a parameter shift

Although same-parameter completion is not obtained, there is a universal completion if the star parameter is allowed to grow with the grid dimension.

### Proposition 2
If there is a \(q\times q\) grid coloring containing neither a red rectangle nor a blue \(K_n\), then
\[
R(q+n-1)>2q.
\tag{5}
\]
In particular,
\[
R\bigl(G(n)+n-2\bigr)\ge 2G(n)-1.
\tag{6}
\]

### Proof

Let \(X,Y\) be disjoint sets of size \(q\). Color all mixed triples according to the grid coloring, as in Proposition 1, and color every triple wholly contained in \(X\) or wholly contained in \(Y\) blue.

There is no red \(K_4^{(3)}\):

* a \(4+0\) configuration has all its triples blue;
* a \(3+1\) configuration contains a same-part triple, which is blue;
* a \(2+2\) red configuration would be a red rectangle.

Now consider a blue star centered at \(x\in X\). If its leaf set is \(A\cup B\), with
\[
A\subseteq X\setminus\{x\},\qquad B\subseteq Y,
\]
then \(|A|\le q-1\). Moreover, \(B\) must be a blue clique in grid row \(x\), so \(|B|\le n-1\). Hence such a star has at most
\[
(q-1)+(n-1)=q+n-2
\]
leaves. The same argument applies to centers in \(Y\). Thus there is no blue \(S_{q+n-1}^{(3)}\).

Taking \(q=G(n)-1\) gives (6). ∎

This does not approach (4), because the new star parameter is approximately \(G(n)\), not \(n\). It nevertheless isolates the same-part leaves as the principal loss in the naive completion.

---

## 5. A fully explicit but very weak parameter-changing converse

One can also obtain a structural implication in the direction from grids to ordinary hypergraphs, at the cost of an enormous change in \(n\).

Let \(\mathcal R(a,b)\) be the ordinary two-color graph Ramsey number for a red \(K_a\) versus a blue \(K_b\), and let \(\mathcal R_6(t)\) be the diagonal six-color graph Ramsey number.

For \(n\ge3\), set
\[
s=n+\binom n2+1.
\]
Define recursively
\[
t_1=1,\qquad
t_{j+1}=1+\mathcal R(t_j,n-1)
\quad(1\le j<s),
\]
and put
\[
T=t_s,\qquad M(n)=\mathcal R_6(T).
\]

All these numbers are finite by the elementary graph Ramsey theorem.

### Proposition 3
For \(n\ge3\),
\[
G(n)\le R(M(n)).
\tag{7}
\]

This is far too weak to imply any same-parameter comparison, but it is a direct, completely explicit implication.

### A half-graph lemma

Suppose a target-free grid contains distinct matched row-column labels
\[
z,x_1,\dots,x_T
\]
such that
\[
h_{x_i}(z,x_j)\text{ is blue whenever }i<j.
\tag{8}
\]
This is impossible.

Indeed, for fixed \(i\), the horizontal graph in row \(x_i\) induced by
\(\{x_{i+1},\dots,x_T\}\) has no blue \(K_{n-1}\): together with column \(z\), such a clique would form a blue \(K_n\) in row \(x_i\).

The recursion defining \(t_j\) therefore gives a subsequence
\[
y_1,\dots,y_s
\]
such that
\[
h_{y_i}(y_j,y_k)\text{ is red whenever }i<j<k.
\tag{9}
\]
This follows by induction: choose the first term, use
\(\mathcal R(t_{j-1},n-1)\) to find a red clique of the required size in its row, and continue inside that clique.

Consider the first \(n\) labels \(y_1,\dots,y_n\) as rows and the remaining
\[
\binom n2+1
\]
labels as possible columns. For each pair \(1\le i<j\le n\), at most one of those later columns \(y_k\) can satisfy
\[
v_{y_k}(y_i,y_j)=\text{red}.
\]
Otherwise, if two later columns \(y_k,y_\ell\) had this vertical edge red, then (9) would give the two red horizontal sides
\[
h_{y_i}(y_k,y_\ell),\qquad h_{y_j}(y_k,y_\ell),
\]
producing a red rectangle.

There are only \(\binom n2\) row-pairs but \(\binom n2+1\) candidate columns. Hence one candidate column has every edge among rows \(y_1,\dots,y_n\) blue, yielding a blue \(K_n\), a contradiction.

The same conclusion holds with the sequence order reversed, and also after interchanging rows and columns.

### Construction of the auxiliary hypergraph

Now suppose that a \(q\times q\) grid avoids both targets. Identify its row and column index sets by an arbitrary bijection. Define a red-blue coloring of triples of \([q]\) by declaring \(\{a,b,c\}\) red exactly when all six edges
\[
\begin{aligned}
&h_a(b,c),\ h_b(a,c),\ h_c(a,b),\\
&v_a(b,c),\ v_b(a,c),\ v_c(a,b)
\end{aligned}
\tag{10}
\]
are red.

This auxiliary hypergraph has no red \(K_4^{(3)}\). Indeed, if
\(\{a,b,c,d\}\) were red, then rows \(a,b\) and columns \(c,d\) would have red sides
\[
h_a(c,d),\quad h_b(c,d),\quad v_c(a,b),\quad v_d(a,b),
\]
forming a red rectangle.

Suppose instead that it has a blue \(S_{M(n)}^{(3)}\), centered at \(z\), with leaf set \(L\). For every pair \(x,y\in L\), at least one of the six edges in (10), applied to \(\{z,x,y\}\), is blue. Fix an order on \(L\), and assign each pair one of the following six witness types:

1. \(h_z(x,y)\) is blue;
2. \(v_z(x,y)\) is blue;
3. the horizontal witness at the earlier leaf is blue;
4. the horizontal witness at the later leaf is blue;
5. the vertical witness at the earlier leaf is blue;
6. the vertical witness at the later leaf is blue.

If several witnesses are available, select one by a fixed priority rule. Since
\[
|L|=\mathcal R_6(T),
\]
there is a \(T\)-element subset whose pairs all receive the same witness type.

* Type 1 gives a blue \(K_T\), hence a blue \(K_n\), in row \(z\).
* Type 2 gives one in column \(z\).
* Type 3 is precisely the forbidden half-graph configuration (8).
* Type 4 reduces to type 3 by reversing the order.
* Types 5 and 6 are the row-column transposes of types 3 and 4.

Every case is impossible. Thus the auxiliary hypergraph has neither a red \(K_4^{(3)}\) nor a blue \(S_{M(n)}^{(3)}\), so
\[
q<R(M(n)).
\]
Taking \(q=G(n)-1\) proves (7). ∎

---

## 6. What remains open

Under the natural formalization \(R(n)=\Theta(G(n))\), Proposition 1 proves one direction with the sharp elementary constant \(2\). The unresolved assertion is
\[
G(n)\le C\,R(n)
\]
for an absolute constant \(C\).

Even the weaker same-parameter polynomial bound
\[
G(n)\le R(n)^C
\]
does not follow from the arguments above. Proposition 2 changes the star parameter from \(n\) to approximately \(G(n)\), while Proposition 3 changes it to the enormous Ramsey-theoretic function \(M(n)\).

Thus I obtain neither a proof nor a counterexample. The precise gap is a same-parameter completion or extraction theorem for the mixed-triple coloring encoded by a grid. The reported 2025 preprint was not available for verification and was not used here.