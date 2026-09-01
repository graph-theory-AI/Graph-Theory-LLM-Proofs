```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general conjecture remains open, but frozen k-colourings force a K_{ceil(k/2)} minor, while bipartite graphs are Kempe-connected for every k at least 2 and quasi-line K_t-minor-free graphs for k at least 2t-3.",
  "would_publish": false,
  "caveats": "The argument does not control surjective, non-frozen Kempe classes in general minor-free graphs."
}
```

# Mathematical writeup

## 1. Conventions and status

A proper \(k\)-colouring is a map \(\alpha:V(G)\to [k]\); colours need not all be used. A Kempe change interchanges two colours on one connected component of the subgraph induced by those two colours. Write \(h(G)\) for the largest \(r\) such that \(G\) contains a \(K_r\)-minor.

For a real constant \(c'\), the expression \(c't\) should be read with an innocuous rounding, such as \(\lceil c't\rceil\).

I do not resolve the general question. I prove:

1. A frozen \(k\)-colouring forces \(h(G)\ge \lceil k/2\rceil\). Consequently, a \(K_t\)-minor-free graph has no frozen \(k\)-colouring for \(k\ge 2t-1\).
2. Every proper \(k\)-colouring of a bipartite graph, for every \(k\ge2\), lies in one Kempe class; in fact the Kempe diameter is at most \(2|V(G)|\).
3. If every neighbourhood of a \(K_t\)-minor-free graph is covered by \(p\) cliques, then all its \(k\)-colourings are Kempe equivalent for
   \[
   k\ge p(t-2)+1.
   \]
   In particular this gives \(k\ge2t-3\) for line graphs and, more generally, quasi-line graphs.
4. A general disjoint-palette lemma shows that any obstruction at a large palette must remain nearly surjective throughout its Kempe class.

The unresolved issue is precisely that a disconnected Kempe class need not contain a frozen colouring.

---

## 2. The degeneracy lemma, with proof

We use the standard fact quoted in the problem.

### Lemma 2.1
If \(G\) is \(d\)-degenerate and \(k>d\), then all proper \(k\)-colourings of \(G\) are Kempe equivalent.

### Proof
Induct on \(|V(G)|\). Choose \(v\) with \(\deg(v)\le d<k\). Let \(\alpha,\beta\) be two \(k\)-colourings. By induction, their restrictions to \(G-v\) are joined by a sequence of Kempe changes.

It remains to lift one change in \(G-v\). Suppose it interchanges colours \(a,b\) on a component \(C\) of \((G-v)[a,b]\).

If the current colour of \(v\) is not \(a\) or \(b\), or if \(v\) has no neighbour in \(C\) of the opposite colour, then \(C\) is also a component of \(G[a,b]\), and the same change can be made in \(G\).

Otherwise suppose \(v\) currently has colour \(a\) and has a \(b\)-neighbour in \(C\). If some colour \(c\ne a\) is absent from \(N(v)\), then \(v\) is a singleton component of \(G[a,c]\), so first recolour \(v\) from \(a\) to \(c\), and then perform the desired change on \(C\). Here \(c\ne b\), since \(v\) has a \(b\)-neighbour.

The remaining case is that every one of the \(k-1\) colours other than \(a\) occurs in \(N(v)\). Since \(\deg(v)\le k-1\), each occurs exactly once. In particular, \(v\) has exactly one \(b\)-neighbour, so \(C\cup\{v\}\) is a component of \(G[a,b]\). Swapping that component induces exactly the desired change on \(G-v\).

After lifting the whole sequence, the restriction to \(G-v\) equals \(\beta|_{G-v}\). Since \(\beta(v)\) is absent from the now correctly coloured neighbourhood of \(v\), a final singleton Kempe change gives \(v\) its target colour. ∎

Thus any counterexample at palette size \(k\) must have degeneracy at least \(k\), and hence contains an induced subgraph of minimum degree at least \(k\).

---

## 3. Bipartite graphs have only one Kempe class

This is a substantial special case because bipartite graphs can have arbitrarily large degeneracy.

### Theorem 3.1
Let \(G\) be bipartite and \(k\ge2\). Then all proper \(k\)-colourings of \(G\) are Kempe equivalent. Moreover, fixing a bipartition \(V(G)=X\cup Y\), every \(k\)-colouring can be transformed in at most \(|V(G)|\) Kempe changes into the colouring
\[
\tau(x)=1\quad(x\in X),\qquad \tau(y)=2\quad(y\in Y).
\]

### Proof
Let \(\alpha\) be an arbitrary \(k\)-colouring.

For each colour \(c\ne1\), consider the components of \(G[\{1,c\}]\). Every nontrivial such component has one of two orientations with respect to the fixed bipartition:

\[
X\text{-vertices have colour }c,\quad Y\text{-vertices have colour }1,
\]
or
\[
X\text{-vertices have colour }1,\quad Y\text{-vertices have colour }c.
\]

Indeed, both the graph bipartition and the two colours alternate along every path in the component.

For the current value of \(c\), perform a Kempe change on every component of the first orientation, including isolated vertices of \(X\) coloured \(c\). This changes all its \(X\)-vertices from \(c\) to \(1\), and it changes no \(X\)-vertex already coloured \(1\). Consequently, after processing all \(c\ne1\), every vertex of \(X\) has colour \(1\). Once fixed, such a vertex is never changed again.

Now let \(y\in Y\) have colour \(c\ne2\). If \(c\ne1\), then all vertices coloured \(c\) or \(2\) lie in \(Y\), apart from vertices of \(X\), which all have colour \(1\). Since \(Y\) is independent, \(y\) is an isolated component of the \((c,2)\)-subgraph and can be recoloured to \(2\). If \(c=1\), properness and the fact that all neighbours of \(y\) lie in \(X\) and have colour \(1\) imply that \(y\) is isolated in \(G\); it can again be recoloured to \(2\) by a singleton Kempe change.

This reaches \(\tau\).

Each Kempe component changed in the first phase contains a previously unfixed vertex of \(X\), which becomes permanently fixed, so there are at most \(|X|\) such changes. The second phase uses at most \(|Y|\) singleton changes. Thus the distance from \(\alpha\) to \(\tau\) is at most \(|V(G)|\), and the distance between any two colourings is at most \(2|V(G)|\). ∎

### Consequence
On the subclass of bipartite \(K_t\)-minor-free graphs, the catalog question has a much stronger affirmative answer: every palette of size at least \(2\) works, independently of \(t\). Thus the large degeneracy of bipartite minor-extremal graphs is not by itself a Kempe obstruction.

---

## 4. Frozen colourings force a linear clique minor

Call a surjective \(q\)-colouring with classes \(V_1,\dots,V_q\) frozen if every \(G[V_i\cup V_j]\) is connected. Then every Kempe change merely globally exchanges two colour labels, so the underlying partition cannot change.

### Theorem 4.1
If \(G\) has a frozen \(q\)-colouring, then
\[
h(G)\ge \left\lceil\frac q2\right\rceil .
\]

### Proof
If \(q=2r\), form the \(r\) branch sets
\[
B_i=V_{2i-1}\cup V_{2i}\qquad(1\le i\le r).
\]
Each \(B_i\) is connected by frozeness. They are pairwise disjoint. For \(i\ne j\), the connected graph
\[
G[V_{2i-1}\cup V_{2j-1}]
\]
contains an edge between \(V_{2i-1}\subseteq B_i\) and \(V_{2j-1}\subseteq B_j\). Hence the branch sets are pairwise adjacent and give a \(K_r\)-minor.

If \(q=2r+1\), use the same \(r\) paired branch sets and choose an arbitrary vertex \(x\in V_{2r+1}\) as one further branch set. For every \(i\), connectedness of
\[
G[V_{2r+1}\cup V_{2i-1}]
\]
implies that \(x\) has a neighbour in \(V_{2i-1}\), since \(V_{2r+1}\) is independent. Thus \(\{x\}\) is adjacent to every paired branch set. This gives a \(K_{r+1}\)-minor. ∎

### Corollary 4.2
If \(G\) has no \(K_t\)-minor, then every frozen colouring of \(G\) has at most \(2t-2\) colours. In particular, there is no frozen \(k\)-colouring for
\[
k\ge2t-1.
\]

This brackets the role of the construction from the source paper:

- frozen examples exist with approximately \(\frac32t\) colours;
- no frozen construction can obstruct a constant larger than \(2\).

It emphatically does **not** prove that \(c'=2\) works, because a disconnected Kempe class need not contain a frozen colouring.

Two further elementary consequences of frozeness are
\[
\delta(G)\ge q-1
\]
and, writing \(n=|V(G)|\),
\[
|E(G)|
 \ge \sum_{i<j}\bigl(|V_i|+|V_j|-1\bigr)
 = (q-1)n-\binom q2.
\]
The minor bound above is stronger than what follows from this density estimate alone.

---

## 5. A linear result for line and quasi-line graphs

### Theorem 5.1
Let \(G\) have no \(K_t\)-minor, and suppose that for every \(v\in V(G)\), the neighbourhood \(N(v)\) can be covered by \(p\) cliques. Then all proper \(k\)-colourings of \(G\) are Kempe equivalent whenever
\[
k\ge p(t-2)+1.
\]

### Proof
Since \(G\) has no \(K_t\)-minor, it has no \(K_t\) subgraph. If \(Q\subseteq N(v)\) is a clique, then \(Q\cup\{v\}\) is a clique, so
\[
|Q|\le t-2.
\]
As \(N(v)\) is covered by \(p\) such cliques,
\[
\deg(v)\le p(t-2).
\]
Thus \(G\) is \(p(t-2)\)-degenerate. Lemma 2.1 applies for every
\[
k>p(t-2).
\]
∎

A quasi-line graph is, by definition here, a graph whose every neighbourhood is covered by two cliques. Hence:

### Corollary 5.2
If \(G\) is quasi-line and has no \(K_t\)-minor, then all its \(k\)-colourings are Kempe equivalent for
\[
k\ge2t-3.
\]

Every line graph is quasi-line: if \(e=uv\) is an edge of the underlying graph, then the neighbours of \(e\) in the line graph are covered by the clique of edges incident with \(u\) and the clique of edges incident with \(v\). Thus the same \(2t-3\) bound holds for line graphs.

Similarly, if \(G\) is chordal and has no \(K_t\)-minor, every induced subgraph has a simplicial vertex of degree at most \(t-2\). Hence \(G\) is \((t-2)\)-degenerate, and all \(k\)-colourings are Kempe equivalent for \(k\ge t-1\).

---

## 6. A general disjoint-palette lemma

The following gives a useful description of what a genuinely bad class must look like.

### Lemma 6.1
Let \(\alpha,\beta\) be proper \(k\)-colourings using respectively \(p\) and \(q\) nonempty colours. If
\[
p+q\le k,
\]
then \(\alpha\) and \(\beta\) are Kempe equivalent.

### Proof
Any global permutation of colour labels is a Kempe sequence: for a transposition of colours \(a,b\), swap \(a,b\) successively on every component of the \((a,b)\)-subgraph.

Therefore relabel \(\alpha\) and \(\beta\) so that their used palettes \(A,B\subseteq[k]\) are disjoint, with \(|A|=p\) and \(|B|=q\).

For each \(b\in B\), let
\[
T_b=\beta^{-1}(b).
\]
Process these target classes one at a time. For each \(v\in T_b\), recolour \(v\) from its current colour \(a\in A\) to \(b\). At that moment all vertices currently coloured \(b\) already lie in \(T_b\). Since \(T_b\) is independent, \(v\) has no \(b\)-coloured neighbour. It also has no \(a\)-coloured neighbour because the current colouring is proper. Hence \(v\) is a singleton component of the \((a,b)\)-subgraph, and this recolouring is a Kempe change.

At the end the colouring is \(\beta\), up to the initial relabelling. ∎

### Corollary 6.2
Let \(r=\chi(G)\) and \(k\ge2r\). Fix an \(r\)-colouring \(\beta\). Every \(k\)-colouring using at most \(k-r\) colours is Kempe equivalent to \(\beta\). Consequently, every Kempe class other than this “low-colour” class consists entirely of colourings using at least
\[
k-r+1
\]
colours.

Thus, when \(k\) is substantially larger than \(\chi(G)\), any exceptional Kempe class must remain almost surjective under every sequence of Kempe changes. Frozen classes are the extreme example, but near-surjectivity does not imply frozeness.

---

## 7. Why the general argument stops

The frozen proof pairs colour classes and uses each union as a connected branch set. For a general colouring in a nontrivial Kempe class, a two-colour subgraph may have many components. Then:

- \(V_i\cup V_j\) is not a valid branch set;
- selecting one component may discard all edges needed to meet another selected component;
- even if every pair of colour classes has at least one edge between them, contracting the colour classes is invalid because individual colour classes are independent and generally disconnected.

Hence neither a complete colour-adjacency quotient nor the necessary condition \(\operatorname{degeneracy}(G)\ge k\) produces a linear clique minor.

A complete proof would need a new statement of roughly one of the following forms:

- every sufficiently large Kempe class can be changed to a colouring using only \(O(t)\) colours; or
- every non-reducible, possibly non-frozen \(k\)-colouring forces a \(K_{\Omega(k)}\)-minor.

No such statement is proved here. Therefore the general \(O(t\sqrt{\log t})\) upper bound from degeneracy is not improved.