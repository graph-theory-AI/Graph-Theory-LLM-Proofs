```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Iterated-edge embeddability has an exact linear-algebraic recognition criterion, and the conjecture extends from the known two-tight-component case to arbitrary one-vertex amalgams of such hypergraphs.",
  "would_publish": false,
  "caveats": "The Ramsey argument uses the source paper's proved case; cyclic cores with at least three tight components remain unresolved."
}
```

# Mathematical writeup

## 1. Setup and partial result

Let \(\mathcal I\) denote the class of finite \(3\)-graphs that are subgraphs of iterated blowups of one edge. I use the result stated in the supplied source paper:

> **Known theorem.** If a \(3\)-graph has at most two tight components, then its Ramsey number against \(K_n^{(3)}\) is polynomial in \(n\) if and only if it belongs to \(\mathcal I\).

I prove the following extensions and reductions.

### Partial theorem

1. Membership in \(\mathcal I\) has an exact characterization in terms of incidence-matrix ranks over \(\mathbb F_3\), and hence is recognizable in polynomial time.

2. The conjecture holds for every \(3\)-graph obtained by repeatedly taking disjoint unions or identifying one vertex of \(3\)-graphs having at most two tight components.

3. In particular, the conjecture holds when the tight components \(C_1,\dots,C_t\) can be ordered so that
   \[
   \left|V(C_i)\cap \bigcup_{j<i}V(C_j)\right|\le 1
   \qquad(i=2,\dots,t).
   \]

4. Any remaining counterexample to the only-if direction can be reduced to an induced subgraph \(F\) satisfying
   \[
   \operatorname{rank}_{\mathbb F_3} M_F=|V(F)|-1,
   \]
   having at least three tight components, with every one- or two-component subgraph belonging to \(\mathcal I\), and with cyclic overlap among its tight components.

The Ramsey conjecture is not settled for these residual cyclic cores.

---

## 2. A word model for iterated blowups

A convenient universal iterated blowup has vertices labelled by ternary words. For words
\[
x,y,z\in\{0,1,2\}^d,
\]
declare \(\{x,y,z\}\) to be an edge if, at the first coordinate at which the three symbols are not all equal, the three symbols are \(0,1,2\) in some order.

Every finite iterated blowup of an edge embeds in such a word construction after padding branches to a common depth. Conversely, a finite \(3\)-graph \(H\) belongs to \(\mathcal I\) precisely when its vertices admit ternary labels such that every edge satisfies this first-difference condition. Labels can be made injective by appending private suffixes after all edges have already been resolved.

Thus a top-level partition of an iterated blowup has the property that each edge is either:

- contained in one part, or
- meets all three parts once.

No edge has a \(2+1\) distribution across the top-level parts.

---

## 3. The \(\mathbb F_3\) splitting criterion

For a \(3\)-graph \(J\), let \(M_J\) be its edge-vertex incidence matrix over \(\mathbb F_3\). Thus a vector
\[
c\in\mathbb F_3^{V(J)}
\]
lies in \(\ker M_J\) exactly when
\[
c(x)+c(y)+c(z)=0
\]
for every edge \(xyz\).

For three elements of \(\mathbb F_3\), their sum is zero precisely when they are either all equal or all distinct. Indeed, if two are equal, say \(a,a,b\), then
\[
2a+b=0 \quad\Longrightarrow\quad b=-2a=a.
\]

Hence:

> **Splitting lemma.** A vector \(c\in\ker M_J\) is exactly a vertex \(3\)-coloring under which every edge is monochromatic or rainbow.

The constant vectors always lie in \(\ker M_J\).

### Recursive characterization

For an edge-containing \(J\),
\[
J\in\mathcal I
\]
if and only if there is a nonconstant \(c\in\ker M_J\) such that each of
\[
J[c^{-1}(0)],\quad J[c^{-1}(1)],\quad J[c^{-1}(2)]
\]
belongs to \(\mathcal I\).

The reverse implication follows by putting the three recursive representations into the three top-level branches. For the forward implication, take the first level of a word representation at which not all vertices have the same symbol. Every edge is monochromatic or rainbow there, and the monochromatic pieces inherit recursive representations.

---

## 4. Exact rank characterization

### Theorem 4.1

For a finite \(3\)-graph \(H\), the following are equivalent.

1. \(H\in\mathcal I\).

2. For every \(S\subseteq V(H)\) with \(E(H[S])\neq\varnothing\),
   \[
   \dim_{\mathbb F_3}\ker M_{H[S]}\ge 2.
   \]

3. For every such \(S\),
   \[
   \operatorname{rank}_{\mathbb F_3} M_{H[S]}\le |S|-2.
   \]

#### Proof

The equivalence of (2) and (3) is rank-nullity.

Suppose \(H\in\mathcal I\). The class \(\mathcal I\) is hereditary under taking vertices or deleting edges, so every \(H[S]\) also belongs to \(\mathcal I\). If it has an edge, the recursive characterization gives a nonconstant vector in its incidence kernel. Together with the constant vectors, its kernel has dimension at least two.

Conversely, assume (2), and induct on \(|V(H)|\). There is nothing to prove if \(H\) has no edges. Otherwise choose a nonconstant
\[
c\in\ker M_H.
\]
Every nonempty color class has fewer than \(|V(H)|\) vertices. Moreover, each induced color-class subgraph still satisfies (2), since every one of its induced subgraphs is also an induced subgraph of \(H\). By induction all three color-class subgraphs belong to \(\mathcal I\). The recursive characterization then gives \(H\in\mathcal I\). \(\square\)

### Consequences

If \(H\notin\mathcal I\), then \(H\) contains an induced subgraph \(F\) with
\[
\ker M_F=\langle \mathbf 1\rangle,
\qquad
\operatorname{rank}_{\mathbb F_3}M_F=|V(F)|-1.
\]
Call such an \(F\) **\(\mathbb F_3\)-rigid**.

In particular,
\[
|E(F)|\ge |V(F)|-1.
\]
Thus every non-iterated \(3\)-graph has an induced subgraph of this density.

### Certifying recognition algorithm

The characterization gives the following algorithm.

- If the current induced subgraph \(J\) has no edges, accept it.
- Compute \(\ker M_J\).
- If this kernel consists only of constant vectors, reject and output \(J\).
- Otherwise choose any nonconstant \(c\in\ker M_J\) and recurse on the three color classes.

If all recursive calls accept, concatenate their ternary representations. If one rejects, its output is an induced \(\mathbb F_3\)-rigid obstruction.

Every nonconstant split has at least two nonempty classes, so the recursion tree has \(O(|V(H)|)\) nodes. Naive Gaussian elimination gives a polynomial-time algorithm; for example \(O(v^6)\) field operations is an immediate coarse bound. Importantly, **any** nonconstant kernel vector may be chosen: if all three resulting pieces belonged to \(\mathcal I\), then their composition would put \(J\) in \(\mathcal I\).

---

## 5. Closure under one-vertex amalgamation

Call \(H\) a **one-sum** of \(H_1,H_2\) if
\[
E(H)=E(H_1)\cup E(H_2),
\qquad
|V(H_1)\cap V(H_2)|\le 1.
\]

### Lemma 5.1

\[
H_1,H_2\in\mathcal I
\quad\Longrightarrow\quad
H_1\cup H_2\in\mathcal I.
\]

#### Proof

Suppose first that \(V(H_1)\cap V(H_2)=\{v\}\). Let
\[
w_i:V(H_i)\longrightarrow\{0,1,2\}^{d_i}
\]
be valid word representations.

Assign
\[
x\in V(H_1)\setminus\{v\}
  \longmapsto (w_1(x),w_2(v)),
\]
\[
y\in V(H_2)\setminus\{v\}
  \longmapsto (w_1(v),w_2(y)),
\]
and
\[
v\longmapsto (w_1(v),w_2(v)).
\]

Every edge of \(H_1\) is resolved in the first block, while every edge of \(H_2\) is monochromatic throughout the first block and is resolved in the second. Private suffixes make the labels injective if necessary.

For a disjoint union, use arbitrary constant words in place of \(w_1(v)\) and \(w_2(v)\). \(\square\)

Since \(\mathcal I\) is hereditary, the converse is automatic:

\[
H_1\cup H_2\in\mathcal I
\quad\Longleftrightarrow\quad
H_1,H_2\in\mathcal I
\]
for a one-sum.

---

## 6. Ramsey consequence of the one-sum lemma

For subgraphs \(F\subseteq H\),
\[
r(F,K_n^{(3)})\le r(H,K_n^{(3)}).
\]
Thus a superpolynomial Ramsey lower bound for \(F\) transfers to \(H\).

Suppose \(H\) is a one-sum of \(H_1,H_2\), and the conjectural classification is already known for each \(H_i\). If \(H\notin\mathcal I\), then by Lemma 5.1 at least one \(H_i\notin\mathcal I\). That \(H_i\) has superpolynomial Ramsey number, and hence so does \(H\). If \(H\in\mathcal I\), the known Erdős–Hajnal upper bound applies.

Iterating gives:

### Theorem 6.1

The conjecture holds for every \(3\)-graph obtainable by repeated disjoint unions and one-vertex identifications of \(3\)-graphs having at most two tight components.

This is a genuine extension of the supplied source theorem to hypergraphs with arbitrarily many tight components.

### Tight-component forest corollary

Let \(C_1,\dots,C_t\) be the tight components of \(H\), viewed as edge-subgraphs with their supporting vertices. If they admit an ordering satisfying
\[
\left|V(C_i)\cap\bigcup_{j<i}V(C_j)\right|\le1,
\]
then \(H\) is a repeated one-sum of tightly connected \(3\)-graphs. Therefore the conjecture holds for \(H\).

A sufficient equivalent-looking formulation is that the bipartite incidence graph whose left vertices are tight components and whose right vertices are vertices belonging to at least two component supports is a forest. Rooting that forest gives the required ordering.

---

## 7. Normal form for a genuinely unresolved instance

Let \(H\notin\mathcal I\). The rank algorithm produces an induced \(\mathbb F_3\)-rigid subgraph \(F\subseteq H\).

If \(F\) has at most two tight components, the supplied source theorem already implies that \(r(F,K_n^{(3)})\), and hence \(r(H,K_n^{(3)})\), is superpolynomial.

Likewise, if one tight component \(C\) of \(F\) is itself outside \(\mathcal I\), then the tightly connected case applies to \(C\).

Consequently, a residual unresolved core may be assumed to satisfy all of the following:

1. \(\operatorname{rank}_{\mathbb F_3}M_F=|V(F)|-1\);
2. \(F\) has at least three tight components;
3. every tight component belongs to \(\mathcal I\);
4. more strongly, every subgraph formed from at most two tight components belongs to \(\mathcal I\);
5. the component-support incidence graph contains a cycle.

Thus the remaining difficulty is genuinely a cyclic compatibility phenomenon between at least three individually harmless tight components.

---

## 8. A smallest cyclic rigid obstruction

The following six-vertex example exhibits the residual phenomenon.

Let \(Q\) have vertex set \(\{1,\dots,6\}\) and edge set
\[
E(Q)=\{123,\;345,\;346,\;156,\;256\}.
\]

Its incidence equations over \(\mathbb F_3\) are
\[
x_1+x_2+x_3=0,
\]
\[
x_3+x_4+x_5=0,\qquad x_3+x_4+x_6=0,
\]
\[
x_1+x_5+x_6=0,\qquad x_2+x_5+x_6=0.
\]

Subtracting the middle two equations gives \(x_5=x_6\), while subtracting the final two gives \(x_1=x_2\). Put
\[
x_1=x_2=a,\qquad x_5=x_6=c.
\]
Then \(x_1+x_5+x_6=0\) gives
\[
a+2c=0,
\]
hence \(a=c\) in \(\mathbb F_3\). The first equation gives \(x_3=a\), and then the second gives \(x_4=a\). Thus every kernel vector is constant:
\[
\ker M_Q=\langle\mathbf1\rangle.
\]
Therefore
\[
\operatorname{rank}_{\mathbb F_3}M_Q=5
\]
and \(Q\notin\mathcal I\).

Its tight components are
\[
\{123\},\qquad \{345,346\},\qquad \{156,256\}.
\]
Each belongs to \(\mathcal I\): the latter two are two-edge books, with the common pair placed in two top-level parts and both tips in the third part. Thus \(Q\) is globally non-iterated although every tight component is iterated.

Moreover, \(Q\) is subgraph-minimal outside \(\mathcal I\). A direct count gives
\[
\max_{|S|=3}e_Q(S)=1,\qquad
\max_{|S|=4}e_Q(S)=2,\qquad
\max_{|S|=5}e_Q(S)=3.
\]
After deleting any edge, the full six-vertex graph has at most four edges. Hence every edge-containing induced subgraph \(J\) of every proper subgraph of \(Q\) satisfies
\[
|E(J)|\le |V(J)|-2,
\]
so
\[
\operatorname{rank}M_J\le |V(J)|-2.
\]
Theorem 4.1 then puts every proper subgraph of \(Q\) in \(\mathcal I\).

Finally, six vertices are the minimum possible for a \(3\)-graph with three tight components: choosing one edge from each component gives three triples that pairwise intersect in at most one vertex, whose union has size at least
\[
9-3=6.
\]

Thus \(Q\) is a smallest possible three-component obstruction not accessible through one-sum closure.

---

## 9. Why the rank obstruction alone does not finish the Ramsey argument

For an \(\mathbb F_3\)-rigid \(F\), there is an immediate \(F\)-free construction. Let \(G_d\) have vertex set \(\mathbb F_3^d\), with distinct \(x,y,z\) forming an edge when
\[
x+y+z=0.
\]
A copy of \(F\) would, in every coordinate, give a vector in \(\ker M_F\), hence a constant vector. All vertices of the alleged copy would therefore receive the same element of \(\mathbb F_3^d\), a contradiction.

However, this construction is insufficient for superpolynomial Ramsey growth. The set
\[
\{0,1\}^d\subseteq\mathbb F_3^d
\]
is independent: a zero-sum triple using only \(0,1\) in each coordinate would have to be coordinatewise constant, so its three vectors would coincide. Consequently,
\[
\alpha(G_d)\ge 2^d
   =|V(G_d)|^{\log_3 2}.
\]
This is a fixed power of the number of vertices, whereas proving superpolynomial Ramsey growth requires \(F\)-free examples with independence number \(N^{o(1)}\).

That is the unresolved Ramsey-theoretic step. The structural and algorithmic reductions above isolate it to cyclic, multi-component, \(\mathbb F_3\)-rigid cores such as \(Q\); they do not prove the conjecture for those cores.