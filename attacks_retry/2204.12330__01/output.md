```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A fully specified finite-search construction gives a recursively presented finitely generated group of infinite twin-width, but not the natural or direct example sought by the question.",
  "would_publish": false,
  "caveats": "The construction still searches for high-twin-width witnesses and uses counting and the local lemma; no novelty claim or short finite presentation is made."
}
```

# An effective group construction, with a substantial explicitness caveat

The effectivity gap in the previous attempt can be closed. The important additional ingredients are:

1. the finite witnesses can be chosen with girth proportional to the logarithm of their order; and
2. the small-cancellation labeling problem has a **uniform finite-prefix extension property**.

The second point avoids the genuine, but in this instance unnecessary, problem of finding a computable branch through an arbitrary computable tree.

Here is the precise partial result.

> **Theorem.** There is a completely specified deterministic algorithm producing a presentation
> \[
> \Gamma=\langle S\mid R\rangle
> \]
> such that:
> - \(S\) is finite;
> - membership in the set of defining relator words \(R\) is decidable;
> - the Cayley graph \(\operatorname{Cay}(\Gamma,S)\) has infinite twin-width.
>
> One can take \(|S|=5\cdot 2^{4096}\).

The huge alphabet is merely convenient for making all estimates explicit.

This is an algorithmically explicit group, but it is **not** the kind of explicit example apparently intended by the source question: its finite graphs are selected by testing the desired twin-width lower bounds. I therefore regard this as an effectivization, not a resolution of the catalog problem. I do not claim that this effectivization is new in the literature.

The established theorems used below are the Marcus–Tardos permutation-matrix theorem, the finite asymmetric Lovász local lemma, and the graphical \(C'(1/6)\) embedding theorem. A final, optional corollary uses Higman’s embedding theorem. No unproved conjecture is used.

## 1. Elementary facts about contraction sequences

For a partition \(\mathcal P\) of \(V(G)\), two distinct parts are:

- complete if every possible edge between them is present;
- anticomplete if none is present;
- mixed otherwise.

The mixed pairs are precisely the red edges in the trigraph associated with \(\mathcal P\). Thus the trigraph depends only on the partition, not on how that partition was reached.

Consequently, for fixed finite \(G\) and integer \(d\), the assertion
\[
\operatorname{tww}(G)\le d
\]
is decidable: enumerate all chains from the singleton partition to the one-part partition, each step merging two parts, and test whether every partition has maximum red degree at most \(d\). A dynamic program over partitions is an equivalent finite procedure.

We will also use the **contact quotient**
\[
Q_G(\mathcal P),
\]
in which distinct parts are adjacent whenever at least one original edge joins them.

If \(\Delta(G)\le D\) and \(\mathcal P\) occurs in a width-\(d\) contraction sequence, then
\[
\Delta\bigl(Q_G(\mathcal P)\bigr)\le d+D. \tag{1}
\]
Indeed, each part has at most \(d\) mixed neighbors. It has at most \(D\) complete neighbors: fix a vertex in the part and choose one of its neighbors from every complete-neighboring part.

Finally,
\[
\operatorname{tww}(G_1\mathbin{\dot\cup}G_2)
=\max\{\operatorname{tww}(G_1),\operatorname{tww}(G_2)\}. \tag{2}
\]
For the upper bound, contract the components separately and then merge the resulting isolated bags. The lower bound is induced-subgraph monotonicity.

## 2. High-girth subcubic witnesses

We need a slightly stronger existence statement than unbounded twin-width at bounded degree.

> **Lemma 1.** For every integer \(k\) and every prescribed girth threshold, there is a connected graph \(F\) such that
> \[
> 2\le \delta(F)\le\Delta(F)\le3,\qquad
> \operatorname{tww}(F)>k,
> \]
> and, for some integer \(h\) above the prescribed threshold,
> \[
> \operatorname{girth}(F)\ge h,
> \qquad
> |V(F)|\le e^{40h}. \tag{3}
> \]
> Moreover, such a graph can be found by finite exhaustive search.

Here is a proof, including the counting input.

### 2.1 Counting bounded-twin-width subcubic graphs

For each fixed \(d\), there is a constant \(C_d\) such that the number of labeled \(n\)-vertex graphs satisfying
\[
\Delta(G)\le3,\qquad \operatorname{tww}(G)\le d
\]
is at most
\[
n!C_d^n. \tag{4}
\]

For completeness, this special case follows from Marcus–Tardos as follows.

Put \(q=d+3\). By (1), a width-\(d\) contraction sequence has contact-quotient maximum degree at most \(q\). Order the vertices by a left-to-right ordering of the leaves of its binary contraction tree. Every bag in the sequence is then an interval.

The adjacency matrix in this order has no division into
\[
r=2q+5
\]
row intervals and \(r\) column intervals with every rectangle nonempty. To see this, suppose such a division exists.

If a division interval is a singleton, its vertex has degree at least \(r>q\), a contradiction. Otherwise, consider the first contraction at which a bag \(A\) contains a whole division interval. Before this contraction, every bag meets at most two row intervals and at most two column intervals: an interval meeting three would contain the middle one. Hence \(A\) meets at most four intervals of either division, and every other bag still meets at most two.

Suppose \(A\) contains a row interval. It has an edge into every column interval. Outside the at most four column intervals meeting \(A\), these edges meet at least
\[
\left\lceil\frac{r-4}{2}\right\rceil=q+1
\]
other bags, contradicting the contact-degree bound. The column-interval case is symmetric.

Now take the permutation of length \(r^2\) whose permutation matrix has one entry in each cell of an \(r\times r\) grid: index its rows by \((a,b)\) in lexicographic order and its columns by \((b,a)\). Containing this permutation matrix would give the forbidden division. Thus the ordered adjacency matrix avoids a fixed permutation matrix.

Marcus–Tardos gives a linear bound \(cN\) on the number of ones in every \(N\times N\) matrix avoiding that permutation. There are only exponentially many such matrices: for \(N\) a power of two, replace each \(2\times2\) block by its Boolean OR. The resulting matrix still avoids the permutation and has at most \(cN/2\) occupied cells. Each occupied cell has at most \(15\) preimages. Iterating gives \(2^{O(N)}\) matrices. Padding handles general \(N\).

Finally, allow all \(n!\) vertex orders. This proves (4).

### 2.2 Counting high-girth subcubic graphs

Let the two sides of a bipartition each have \(m\) vertices. Choose three permutations independently and take the simple union of their three perfect matchings. This produces a simple bipartite graph of maximum degree at most three.

Define
\[
h=h(m):=\max\{a\in\mathbb N:6^{10a}\le m\}
=\left\lfloor\frac{\log m}{10\log6}\right\rfloor.
\]

The expected number of cycles of length less than \(h\) is at most \(6^h\), for all sufficiently large \(m\). Indeed, for a possible cycle of length \(j\):

- there are at most \(m^j\) choices of its alternating vertex sequence;
- there are at most \(3^j\) assignments of its edges to the three permutations;
- a feasible assignment occurs with probability at most \((m-j)^{-j}\).

For \(j\le m/2\), their product is at most \(6^j\). Summing over \(j<h\) proves the assertion. In particular, the expectation is at most \(m^{1/10}\).

Therefore at least half of the \((m!)^3\) permutation triples have at most
\[
t=\lceil 2m^{1/10}\rceil
\]
short cycles. Delete an edge from a short cycle repeatedly until none remains. At most \(t\) edges are deleted.

For a fixed resulting graph \(H\), the original simple graph is obtained by adding at most \(t\) edges, so there are at most
\[
\sum_{j=0}^{t}\binom{m^2}{j}
\]
possibilities. Each original simple graph arises from at most \(6^m\) permutation triples: at any left vertex, the three ordered matching neighbors must map onto its neighborhood, and there are at most six such assignments.

Thus the number of resulting labeled high-girth graphs is at least
\[
\frac{(m!)^3}
{2\cdot6^m\displaystyle\sum_{j=0}^{t}\binom{m^2}{j}}
=
\exp\bigl(3m\log m-O(m)\bigr). \tag{5}
\]

On \(n=2m\) vertices, this is
\[
\exp\bigl(\tfrac32 n\log n-O(n)\bigr).
\]
For any fixed \(d\), it eventually exceeds the bound (4). Hence, for every sufficiently large \(m\), some such high-girth graph has twin-width greater than \(d\).

### 2.3 Removing trees

We can additionally require minimum degree at least two.

Let \(K\) be the \(2\)-core of a subcubic graph \(H\). Then
\[
\operatorname{tww}(H)\le \max\{3,\operatorname{tww}(K)+3\}, \tag{6}
\]
with the evident interpretation if \(K\) is empty.

To prove this, contract leaf edges until each tree attached to the core has been absorbed into its attachment vertex, and each tree component has become an isolated bag. During these contractions the contact quotient has maximum degree at most three. Now follow an optimal contraction sequence of \(K\). Its contact quotients have maximum degree at most \(\operatorname{tww}(K)+3\), by (1), and they are also the contact quotients between the expanded core bags. Finally merge isolated bags.

Choose \(H\) in the preceding count with
\[
\operatorname{tww}(H)>k+3.
\]
Its \(2\)-core has twin-width greater than \(k\), and by (2), so does some connected component \(F\).

Deletion preserves the girth lower bound. Moreover,
\[
\log |V(F)|\le \log(2m)
<\log2+10(h+1)\log6
\le40h
\]
for \(h\ge1\). This proves (3) and Lemma 1. All the predicates used are finite and decidable, so exhaustive search finds such a graph.

## 3. A canonical sequence of finite graphs

We now specify the graph sequence without any oracle.

Set \(\ell_0=0\). At stage \(i\ge1\):

1. Enumerate integers \(m\) increasingly, subject to
   \[
   h(m)\ge12(\ell_{i-1}+1).
   \]
2. For each \(m\), enumerate all simple bipartite graphs \(H\) on the prescribed two parts of size \(m\), in adjacency-word order.
3. Find the first satisfying
   \[
   \Delta(H)\le3,\qquad
   \operatorname{girth}(H)\ge h(m),\qquad
   \operatorname{tww}(H)>i+3.
   \]
4. Take the first component of its \(2\)-core having twin-width greater than \(i\), and relabel it increasingly. Call it \(F_i\).
5. Put
   \[
   h_i=h(m),\qquad \ell_i=\left\lceil h_i/12\right\rceil.
   \]

Lemma 1 and its proof establish termination. The resulting sequence satisfies
\[
\operatorname{tww}(F_i)>i,\qquad
\ell_1<\ell_2<\cdots, \tag{7}
\]
and
\[
|V(F_i)|\le e^{40h_i}\le e^{480\ell_i},
\qquad
6\ell_i\le h_i\le\operatorname{girth}(F_i). \tag{8}
\]

The \(h_i\) increase effectively to infinity.

## 4. Effective small-cancellation labels

This is the step that goes beyond the previous attempt.

Let
\[
q=2^{4096},
\qquad
S=\{a_{c,z}:1\le c\le5,\ 1\le z\le q\}.
\]

Greedily give each \(F_i\) a proper edge-coloring with colors \(1,\dots,5\), using its prescribed edge order. Five colors suffice because an edge is incident with at most four other edges. Orient every edge from its smaller to its larger endpoint.

For an edge of color \(c\), its label in the prescribed orientation will be
\[
a_{c,z_e},
\]
where \(z_e\in\{1,\dots,q\}\). Its reverse has the inverse label.

Proper edge-coloring ensures that this labeling is locally injective, independently of the choices of \(z_e\).

We will arrange:

- **internal uniqueness:** distinct oriented paths of length \(\ell_i\) in \(F_i\) have distinct label words;
- **avoidance of earlier words:** for \(j<i\), no path of length \(\ell_j\) in \(F_i\) has a word occurring on a path of length \(\ell_j\) in \(F_j\).

Paths here are nonbacktracking. At these lengths they are simple, by (8).

### 4.1 Finite-prefix extension lemma

> **Lemma 2.** Any labels on \(F_1,\dots,F_{i-1}\) satisfying these requirements extend to labels on \(F_i\). Such an extension can be found by exhaustive search through the \(q^{|E(F_i)|}\) assignments.

Fix the earlier labels and choose the variables \(z_e\) in \(F_i\) independently and uniformly.

For \(j<i\), let \(W_j\) be the set of words on oriented paths of length \(\ell_j\) in \(F_j\). Then
\[
|W_j|\le |V(F_j)|3^{\ell_j}
\le (3e^{480})^{\ell_j}. \tag{9}
\]

There are two kinds of bad event.

**Earlier-word events.** A specified path \(P\) of length \(\ell_j\) in \(F_i\) receives a word in \(W_j\). Because its edges are distinct,
\[
\Pr(A_{P,j})\le
(3e^{480}/q)^{\ell_j}. \tag{10}
\]

**Internal collision events.** Distinct paths \(P,Q\) of length \(\ell_i\) receive the same word.

Only pairs with the same sequence of base colors and orientation signs need be considered. For such a pair,
\[
\Pr(B_{P,Q})\le q^{-\ell_i/2}. \tag{11}
\]

Here is the overlap justification for (11). The proper base labeling means that a path is determined by its initial vertex and its base word. If \(P\) and \(Q\) use the same oriented edge in the same position, following the base word backwards and forwards forces \(P=Q\). Using the same edge in opposite directions in the same position is incompatible with matching orientation signs.

Thus, for distinct eligible \(P,Q\), the equations asserting equality of their random coordinates form a loopless multigraph on the edge variables, of maximum degree two, with \(\ell_i\) edges. Its components are paths and cycles, and its equality constraints have rank at least \(\ell_i/2\). This proves (11).

Assign local-lemma parameters
\[
x(A_{P,j})=q^{-\ell_j/2},
\qquad
x(B_{P,Q})=q^{-\ell_i/4}.
\]

For a fixed edge \(e\) of \(F_i\):

- the number of oriented length-\(\ell\) paths containing \(e\) is at most \(2\ell3^\ell\);
- the number of ordered length-\(\ell_i\) path pairs with \(e\) in at least one path is at most
  \[
  4\ell_i |V(F_i)|3^{2\ell_i}.
  \]

Hence the sum of the \(x\)-parameters of events using \(e\) is at most
\[
2\sum_{\ell\ge1}\ell(3q^{-1/2})^\ell
+
4\ell_i(9e^{480}q^{-1/4})^{\ell_i}
<\frac1{10}. \tag{12}
\]
The strict increase of the \(\ell_j\) justifies bounding the earlier-event sum by the sum over all positive integers. The displayed numerical inequality follows immediately from \(\log q>2800\).

Every \(x\) is at most \(1/2\). Thus, for an event depending on \(s\) edge variables, (12) gives
\[
\prod_{\text{dependent events }E}(1-x(E))
\ge \exp(-s/5). \tag{13}
\]

The chosen \(q\) also gives
\[
(3e^{480}/q)^\ell
\le q^{-\ell/2}e^{-\ell/5},
\qquad
q^{-\ell/2}
\le q^{-\ell/4}e^{-2\ell/5}.
\]
Together with (10), (11), and (13), these are precisely the asymmetric local-lemma inequalities. Therefore an assignment avoiding all bad events exists.

There are only finitely many assignments, and the conditions are decidable. Taking the lexicographically first successful assignment proves Lemma 2. ∎

### 4.2 Why this is an effective infinite construction

At stage \(i\), compute \(F_i\), then enumerate the finitely many label assignments until the first valid one is found. Lemma 2 proves termination **for every previously chosen valid prefix**.

Thus no compactness choice or noncomputable infinite branch is being used.

The resulting labeled disjoint union
\[
\mathcal F=\bigsqcup_{i\ge1}F_i
\]
has the following property: if a word has two distinct path occurrences and one occurrence lies in \(F_i\), then its length is less than \(\ell_i\). For occurrences in different components, apply the avoidance requirement at the later stage; for occurrences in one component, use internal uniqueness and local injectivity.

By (8), every such repeated path in \(F_i\) has length
\[
<\ell_i\le \frac16\operatorname{girth}(F_i). \tag{14}
\]

## 5. The group presentation

Define
\[
\Gamma=
\left\langle
S\ \middle|\
\text{labels of all oriented simple cycles in every }F_i
\right\rangle. \tag{15}
\]

I use the following standard graphical small-cancellation embedding theorem:

> Let a disjoint union of connected graphs be locally injectively labeled over a finite alphabet. Suppose every path with two distinct label-preserving occurrences has length less than one sixth of the girth of each component in which it occurs. Then, in the group presented by the cycle labels, each component maps isometrically into the Cayley graph.

This is a **graphical** small-cancellation statement. Overlaps which are literally the same path in a component are not two distinct occurrences; ordinary small cancellation applied separately to the list of cycle words would not be the appropriate theorem.

Our labels satisfy this theorem by (14). Therefore each \(F_i\) embeds isometrically into \(\operatorname{Cay}(\Gamma,S)\). Its image is induced: an extra Cayley edge between two image vertices would contradict preservation of distance.

Consequently,
\[
\operatorname{tww}\bigl(\operatorname{Cay}(\Gamma,S)\bigr)
\ge \operatorname{tww}(F_i)>i
\]
for every \(i\), where infinite-graph twin-width is measured by finite induced subgraphs. Thus the Cayley graph has infinite twin-width.

### Decidability of the defining relator set

The presentation is more than recursively enumerable.

Every defining cycle word from \(F_i\) is cyclically reduced and has length at least \(h_i\). Given a word of length \(L\), compute the construction until the first stage with \(h_i>L\). No later graph can contribute a defining cycle word of that length.

Only finitely many earlier graphs remain to be checked, and their simple cycles can be enumerated. Therefore membership in the defining relator set in (15) is decidable.

This completes the proof of the stated partial theorem.

## 6. A finitely presented existence corollary

For clarity, the preceding effectivity also has a group-theoretic consequence. No novelty is claimed for it.

> **Corollary.** Some finitely presented group has infinite twin-width.

The needed subgroup permanence has a short proof.

### A locality estimate

Let \(H,J\) be finite graphs on the same vertex set, with
\[
E(J)\subseteq E(H^r),\qquad \Delta(H)\le D.
\]
Then
\[
\operatorname{tww}(J)
\le \bigl(\operatorname{tww}(H)+D+1\bigr)^r-1. \tag{16}
\]

Indeed, use a width-\(d\) sequence for \(H\). Its contact quotients have degree at most \(d+D\), by (1). An edge of \(J\) gives a walk of length at most \(r\) between the corresponding bags in the contact quotient. Hence every red neighbor for \(J\) lies in a radius-\(r\) ball of that quotient. The number of other bags in such a ball is at most
\[
\sum_{a=1}^r(d+D)^a
\le(d+D+1)^r-1.
\]

Now let \(A\) be a finitely generated subgroup of a finitely generated group \(B\). Each generator of \(A\) has bounded word length, say at most \(r\), in a fixed generating set of \(B\).

For any finite vertex set of the Cayley graph of \(A\), include in the Cayley graph of \(B\) the finitely many length-\(\le r\) paths representing its edges. Applying (16) to the resulting finite induced graph shows:

\[
B\text{ has finite twin-width}
\quad\Longrightarrow\quad
A\text{ has finite twin-width}. \tag{17}
\]

The group \(\Gamma\) in (15) is finitely generated and recursively presented. Higman’s embedding theorem embeds it in a finitely presented group \(B\). By (17), \(B\) must have infinite twin-width.

This corollary does **not** supply a short finite presentation.

## 7. What remains unresolved

The mathematical construction above is complete, but its limitation is fundamental to the meaning of the question.

- The graphs \(F_i\) are selected by the predicate
  \[
  \operatorname{tww}(F_i)>i.
  \]
  Their lower bounds are not explained by a natural combinatorial structure.
- Termination of that search comes from counting.
- The labeling algorithm is finite exhaustive search, justified by the local lemma.
- The resulting group is specified algorithmically, not by a recognizable short presentation or a familiar geometric construction.
- The finitely presented corollary is an embedding-based existence statement, not a displayed presentation with a direct twin-width analysis.

Thus this closes the **computability and compatible-labeling gap** left by the previous attempt. It does not remove the probabilistic/combinatorial existence machinery or identify a natural group with a direct infinite-twin-width proof. In that stronger and intended sense, the original problem remains open here.