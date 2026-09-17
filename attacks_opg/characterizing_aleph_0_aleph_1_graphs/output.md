```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a finite-separator characterization of binary type and a minor-stability theorem, but not a characterization of the whole intended class.",
  "would_publish": false,
  "caveats": "No novelty is claimed; an elementary counterexample below concerns only the degree-only wording, not the standard part-size definition."
}
```

## 1. A distinction in the formulation

There are two different definitions at issue.

The supplied statement prescribes **degrees**, but not the sizes of the parts. Write its bipartition as \((C,D)\), where
\[
\deg(c)=\aleph_1\quad(c\in C),\qquad
\deg(d)=\aleph_0\quad(d\in D). \tag{1}
\]
Thus \(C=B\) and \(D=A\) in the question’s notation.

The usual countable-part formulation instead prescribes
\[
|C|=\aleph_0,\qquad |D|=\aleph_1,
\]
with every vertex of \(D\) having infinite degree. The degree-only condition (1) does **not** imply that \(C\) is countable.

This distinction changes the concrete minor question. I first explain that issue, then give structural results for the intended countable-part setting. Throughout, graphs are nonempty and simple, and minors are defined by pairwise disjoint connected branch sets.

## 2. Under the degree-only definition, the concrete minor alternative is false

### Proposition 1
There is a graph satisfying (1) with no minor satisfying (1) that is either indivisible or of binary type.

### Proof

Construct a rooted tree \(T\) as follows:

- the root belongs to \(C\);
- every \(C\)-vertex has \(\aleph_1\) children in \(D\);
- every \(D\)-vertex has countably infinitely many children in \(C\).

More explicitly, its vertices are finite sequences whose coordinates alternate between elements of \(\omega_1\) and elements of \(\omega\), starting with an \(\omega_1\)-coordinate. Adjacency is immediate extension. Vertices of even length belong to \(C\), and those of odd length to \(D\).

Every \(C\)-vertex has degree \(\aleph_1\), and every \(D\)-vertex has degree \(\aleph_0\). Both parts have cardinality \(\aleph_1\).

Every minor of a tree is a forest. Indeed, a finite cycle in a minor model would lift, using finite paths inside its branch sets, to a cycle in the original tree.

Now observe two facts.

**Every forest satisfying (1) is divisible.**  
Choose a vertex \(v\) and two different components \(K_0,K_1\) of its component minus \(v\). Such components exist because \(v\) has infinite degree. Every vertex of either \(K_i\) loses at most the one neighbor \(v\); hence all its prescribed infinite degrees are unchanged. Consequently, both induced subgraphs \(T[V(K_i)]\) satisfy (1).

**No graph of binary type satisfying (1) is a forest.**  
In a binary-type representation, every \(C\)-vertex must map to a tree vertex: a ray vertex in the host has only countable degree. Thus \(C\) is countable, whereas \(D\) is uncountable. Choose two neighbors of each \(d\in D\). There are only countably many pairs of vertices of \(C\), so two different vertices of \(D\) choose the same pair. These four vertices form a \(4\)-cycle.

Therefore no minor of \(T\) satisfying (1) is indivisible or of binary type. ∎

This is a counterexample to the **literally worded** minor alternative, not a new counterexample to the intended Diestel–Leader question: \(T\) has an uncountable high-degree part.

The remaining results concern the countable-part setting.

## 3. An exact finite-separator characterization of binary type

For \(d,e\in D\), call a finite set \(S\subseteq C\) a **core separator** if \(d\) and \(e\) lie in different components of \(G-S\).

### Theorem 2
Let \(G\) satisfy (1). Then \(G\) is of binary type if and only if:

1. \(C\) is countable; and
2. every two distinct vertices of \(D\) have a finite core separator.

When \(C\) is countable, (1) automatically implies
\[
|C|=\aleph_0,\qquad |D|=\aleph_1.
\]

### Proof

#### Necessity

Represent the infinite binary tree by \(2^{<\omega}\) and its rooted rays by \(2^\omega\).

As observed above, all vertices of \(C\) must map to tree vertices, and all vertices of \(D\) to ray vertices. Thus \(C\) is countable.

Let \(d,e\) map to distinct rays \(x_d,x_e\). Choose a finite binary word \(q\) that is an initial segment of \(x_d\), but not of \(x_e\). Delete the vertices of \(C\) whose images are proper initial segments of \(q\). There are only finitely many.

After this deletion, no edge joins the following two regions:

- tree vertices extending \(q\), together with ray vertices extending \(q\);
- all remaining vertices.

Indeed, a ray extending \(q\) can meet the other region only at a proper initial segment of \(q\), and a tree vertex extending \(q\) can be adjacent only to rays extending \(q\). This separates \(d\) from \(e\).

#### Sufficiency: construct an abstract forest on \(C\)

Enumerate
\[
C=\{c_0,c_1,\ldots\}.
\]

Construct a rooted forest \(F\) whose vertex set is \(C\). In each component \(K\) of \(G\), choose the least-indexed vertex of \(C\cap V(K)\) as a root. Delete that root. In each resulting component, choose its least-indexed \(C\)-vertex as a child, and continue recursively.

This construction is well-defined at every finite stage. Along any one recursive route, only finitely many vertices of \(C\) have been deleted. Every remaining vertex of \(D\) therefore still has infinitely many neighbors, so its component contains a vertex of \(C\).

Every \(c_i\) is eventually selected: while it remains in the component being processed, every vertex selected before it has index smaller than \(i\). Thus it can have at most \(i\) predecessors.

For every \(d\in D\), following the successive components containing \(d\) gives an infinite rooted ray \(R_d\) in \(F\). Moreover,
\[
N_G(d)\subseteq V(R_d). \tag{2}
\]
To see this, let \(c\in N_G(d)\). Until \(c\) is selected, the edge \(cd\) keeps \(c\) in the same component as \(d\). Hence \(c\) must eventually be selected on \(d\)'s route.

We claim that the rays \(R_d\) are distinct.

Suppose \(R_d=R_e\). Along this ray, the indices of the successively selected vertices strictly increase and hence tend to infinity. Therefore, for every finite \(S\subseteq C\), some component encountered along the common route contains both \(d,e\) and no vertex of \(S\). It supplies a \(d\)-\(e\) path in \(G-S\), contradicting condition 2.

#### Encode the forest in the binary tree

Adjoin a formal root above all roots of \(F\). Enumerate the children of every vertex by a finite initial segment of \(\omega\), or by \(\omega\).

Map the formal root to the empty word. If a vertex maps to \(s\), map its \(k\)-th child to
\[
s^\frown 1^k0.
\]
The words \(1^k0\) are pairwise incomparable under the initial-segment relation. Consequently this embeds the ancestor order of \(F\) into \(2^{<\omega}\), and distinct infinite rays of \(F\) yield distinct elements of \(2^\omega\).

Map \(c\in C\) to its corresponding tree vertex and \(d\in D\) to the binary ray corresponding to \(R_d\). By (2), every edge of \(G\) becomes an incidence between a tree vertex and a ray containing it.

This is a subgraph representation; additional incidences in the host may simply be omitted. Hence \(G\) is of binary type. ∎

This gives a purely graph-theoretic characterization of the binary-type subclass, without making reference to an embedding into a binary tree.

## 4. Arbitrary finite separators suffice after countably many deletions

The preceding theorem requires separators contained in \(C\). The next result allows arbitrary finite vertex separators.

First, an elementary normalization observation connects the exact-degree convention to the usual convention.

### Cleanup lemma
Suppose \(|C|=\aleph_0\), \(|D|=\aleph_1\), and every \(d\in D\) has infinite degree. Then \(G\) has an induced subgraph satisfying (1).

### Proof

Let
\[
C_{\mathrm{bad}}
=\{c\in C:|N(c)|\leq\aleph_0\},
\qquad
D_{\mathrm{bad}}
=\bigcup_{c\in C_{\mathrm{bad}}}N(c).
\]
The set \(D_{\mathrm{bad}}\) is countable.

Delete \(C_{\mathrm{bad}}\cup D_{\mathrm{bad}}\). Every surviving \(D\)-vertex retains all its neighbors, and hence infinitely many. Every surviving \(C\)-vertex originally had \(\aleph_1\) neighbors and loses only countably many. ∎

### Theorem 3
Let \(G\) have a countable part \(C\), an \(\aleph_1\)-sized part \(D\), and infinite degree at every vertex of \(D\).

Suppose there is an uncountable set \(D_0\subseteq D\) such that every two distinct vertices of \(D_0\) can be separated in \(G\) by a finite vertex set avoiding those two vertices.

Then \(G\) contains an **induced binary-type** graph satisfying (1).

If \(G\) already satisfies (1) and \(D_0=D\), it is enough to delete countably many vertices of \(D\).

### Proof

For every finite \(F\subseteq C\) and every pair of distinct vertices \(c,c'\in C\setminus F\), do the following:

> If some finite set \(W\subseteq D\) separates \(c,c'\) in \(G-F\), choose one such set \(W(F,c,c')\).

There are only countably many triples \((F,c,c')\). Thus
\[
Z=\bigcup W(F,c,c')
\]
is countable.

We claim that every two distinct vertices of \(D_0\setminus Z\) have a finite core separator in \(G-Z\).

Take such vertices \(d,e\). By hypothesis, they have a finite separator \(S\), avoiding \(d,e\). Write
\[
F=S\cap C,\qquad W=S\cap D.
\]
Choose
\[
c\in N(d)\setminus F,\qquad c'\in N(e)\setminus F.
\]
These vertices exist because \(d,e\) have infinite degree. They are distinct, and they are separated by \(W\) in \(G-F\): otherwise the edges \(dc\) and \(ec'\), together with a \(c\)-\(c'\) path avoiding \(S\), would connect \(d\) to \(e\) in \(G-S\).

Consequently the chosen separator \(W(F,c,c')\subseteq Z\) exists. In \(G-(F\cup Z)\), the vertices \(c,c'\) are separated, while \(d,e\) remain adjacent to them respectively. Hence \(F\) separates \(d,e\) in \(G-Z\), proving the claim.

Now restrict to
\[
G[C\cup(D_0\setminus Z)].
\]
Every vertex on its uncountable side still has infinite degree, and distinct vertices on that side have finite core separators. Apply the cleanup lemma. Core separability persists under these vertex deletions, so Theorem 2 makes the resulting induced graph binary type.

If \(G\) satisfies (1) and \(D_0=D\), no cleanup is necessary: deleting the countable set \(Z\subseteq D\) preserves all prescribed degrees. ∎

Thus the concrete minor question has an affirmative answer, using the binary alternative, whenever there is an uncountable pairwise finitely separable set on the uncountable side. In fact, no contractions or edge deletions are needed in this case.

## 5. Binary type is stable under minors, modulo countably many vertices

The finite-separator characterization also gives a useful restriction on minors of binary-type graphs.

### Theorem 4
Let \(G\) be of binary type and satisfy (1). Let \(H\) be a minor of \(G\) satisfying (1), with bipartition \((C_H,D_H)\).

Then \(C_H\) is countable, and there is a countable set \(Z\subseteq D_H\) such that \(H-Z\) is of binary type.

### Proof

Fix a minor model \((V_h:h\in V(H))\) in \(G\), and write the bipartition of \(G\) as \((C_G,D_G)\).

A connected branch set avoiding \(C_G\) must be a singleton, because \(D_G\) is independent. Such a singleton has only countable degree in \(G\), so it cannot model a vertex of degree \(\aleph_1\).

Therefore every branch set corresponding to \(C_H\) meets \(C_G\). Since \(C_G\) is countable and branch sets are disjoint, \(C_H\) is countable.

Let
\[
Z=\{d\in D_H:V_d\cap C_G\neq\varnothing\}.
\]
Again \(Z\) is countable. Every remaining \(d\in D_H\setminus Z\) has a singleton branch set
\[
V_d=\{x_d\},\qquad x_d\in D_G.
\]

Take distinct \(d,e\in D_H\setminus Z\). By Theorem 2, some finite \(S\subseteq C_G\) separates \(x_d,x_e\) in \(G\). Let
\[
F=\{h\in V(H-Z):V_h\cap S\neq\varnothing\}.
\]
The set \(F\) is finite. Moreover \(F\subseteq C_H\), because all surviving \(D_H\)-branch sets avoid \(C_G\).

A \(d\)-\(e\) path in \(H-Z-F\) would lift through its branch sets to a connected subgraph of \(G-S\) containing \(x_d,x_e\). This is impossible. Hence \(F\) is a finite core separator in \(H-Z\).

Deleting countably many vertices from \(D_H\) preserves all the degrees in (1). Theorem 2 therefore applies to \(H-Z\). ∎

### Corollary 5
A binary-type graph has no indivisible minor satisfying (1).

### Proof

First, every binary-type graph satisfying (1) is divisible. Choose two vertices of its uncountable side and a finite core separator between them. Every component remaining after deleting that separator still satisfies (1): a vertex loses only finitely many neighbors, and all other neighbors lie in its component. Two such components give the required disjoint induced graphs.

In fact, repeating this splitting inside one of the retained components produces countably many pairwise anticomplete induced graphs satisfying (1).

Now apply Theorem 4. If \(H\) is a minor satisfying (1), then \(H-Z\) is binary type and hence divisible. Its two witnessing induced subgraphs are also induced subgraphs of \(H\), so \(H\) is divisible. ∎

## 6. What remains unresolved

These results establish:

- an exact characterization of **binary type** by countability of the high-degree side and finite core separability;
- a sufficient condition for a binary-type **induced subgraph**, using arbitrary finite separators;
- stability of binary type under relevant minors after deleting countably many low-degree vertices;
- the absence of indivisible minors inside binary-type graphs.

They do **not** characterize the entire intended class. In the forest construction from Theorem 2, many vertices of the uncountable side may follow the same ray. The argument neither separates such large fibers into binary-type minors nor converts them into indivisible minors.

Accordingly, the tree construction resolves only the concrete question under the supplied **degree-only** wording. The intended countable-part characterization problem is not resolved here.