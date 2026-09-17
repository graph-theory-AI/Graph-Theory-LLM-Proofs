```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a sharp four-color bound for recursively transitive/cyclically decomposable members of the class, using a stronger corner-support lemma, but do not settle the unrestricted conjecture.",
  "would_publish": false,
  "caveats": "The required decomposition is not established for arbitrary members of the class; novelty of these elementary partial results has not been checked."
}
```

## 1. Statement and conventions

Let
\[
H=\Delta(1,2,2).
\]
Thus \(H\) consists of a singleton \(A\) and two transitive pairs \(B,C\), with
\[
A\to B\to C\to A.
\]
The question asks whether there is an absolute constant \(C\) such that every induced-\(\{H,K_1+\vec P_2\}\)-free oriented graph \(D\) satisfies
\[
\vec\chi(D)\le C.
\]

I use the intended oriented-graph convention: no loops or digons.

The main partial result is a sharp bound of four for a recursively decomposable subclass. Its key ingredient strengthens the corner analysis in the supplied attempt:

> If three nonempty sets are cyclically oriented, their union is \(H\)-free, and their union meets at least five partite classes, then **two of the sets together meet at most two partite classes**.

This is considerably stronger than bounding the supports of the two smaller sets separately. It permits their colors to be absorbed into those of the remaining set, without an additive coloring cost.

All arguments below are self-contained; they do not use the tournament-hero theorem for \(H\).

## 2. Multipartite formulation

An oriented graph is induced-\((K_1+\vec P_2)\)-free if and only if its underlying graph is complete multipartite.

Indeed, define \(x\sim y\) if \(x=y\) or \(x,y\) are nonadjacent. If \(x\sim y\) and \(y\sim z\), but \(x,z\) are adjacent, then \(\{x,y,z\}\) induces one arc and an isolated vertex. Thus \(\sim\) is an equivalence relation. Its classes are independent, and vertices in different classes are adjacent.

Consequently, throughout the proof, \(D\) is an orientation of a complete multipartite graph, with parts
\[
P_1,\ldots,P_p.
\]
Every copy of \(H\) uses five distinct parts.

For \(S\subseteq V(D)\), write
\[
\pi(S)=\{i:S\cap P_i\ne\varnothing\},
\qquad
\sigma(S)=|\pi(S)|.
\]
In particular,
\[
\vec\chi(D[S])\le \sigma(S).
\]

For disjoint vertex sets \(X,Y\), write \(X\Rightarrow Y\) if every existing arc between them is directed from \(X\) to \(Y\). Vertices of \(X,Y\) lying in the same original part remain nonadjacent.

## 3. A five-representative lemma

The following elementary set-system fact is the source of the improvement.

### Lemma 3.1

Let \(A,B,C\) be nonempty finite sets. It is possible to select five distinct elements, two from each of two of these sets and one from the third, if and only if
\[
|A\cup B\cup C|\ge5
\tag{3.1}
\]
and
\[
|A\cup B|,\ |B\cup C|,\ |C\cup A|\ge3.
\tag{3.2}
\]

### Proof

Necessity is immediate: five distinct elements are selected in total, and at least three are selected from any two of the sets.

For sufficiency, first observe that two of the sets, say \(A,B\), satisfy
\[
|A|\ge2,\qquad |B|\ge2,\qquad |A\cup B|\ge4.
\tag{3.3}
\]

Here are all the cases establishing this observation.

* By (3.2), at most one of \(A,B,C\) is a singleton.
* If exactly one is a singleton, the union of the other two has size at least four by (3.1).
* Otherwise all three have size at least two. Suppose no pair has union of size at least four. If one set has size three, the other two are contained in it, contradicting (3.1). If all three have size two, they are pairwise intersecting; three pairwise-intersecting two-element sets have union of size at most four, again a contradiction.

Now apply Hall’s theorem to the five sets
\[
A,A,B,B,C.
\]
The Hall inequalities involving just one set type follow from (3.3) and \(C\ne\varnothing\). Those involving two types follow from
\[
|A\cup B|\ge4,\qquad |A\cup C|,|B\cup C|\ge3.
\]
The inequality involving all three types follows from (3.1). Hence these five sets have distinct representatives. ∎

## 4. Cyclic compositions do not accumulate colors

### Theorem 4.1 — cyclic support and coloring lemma

Suppose \(D\) is \(H\)-free and
\[
V(D)=X\mathbin{\dot\cup}Y\mathbin{\dot\cup}Z,
\qquad
X\Rightarrow Y,\quad Y\Rightarrow Z,\quad Z\Rightarrow X.
\tag{4.1}
\]

Then
\[
\vec\chi(D)\le
\max\{4,\vec\chi(D[X]),\vec\chi(D[Y]),\vec\chi(D[Z])\}.
\tag{4.2}
\]

More precisely, if all three sets are nonempty and \(D\) meets at least five parts, then, after cyclically relabeling \(X,Y,Z\),
\[
\sigma(Y\cup Z)\le2
\tag{4.3}
\]
and
\[
\vec\chi(D)\le \max\{2,\vec\chi(D[X])\}.
\tag{4.4}
\]

### Proof

If one of \(X,Y,Z\) is empty, all arcs between the other two sets point in one direction. Their acyclic colorings can therefore use the same palette.

If \(D\) meets at most four parts, coloring by part proves (4.2).

Assume henceforth that the three sets are nonempty and
\[
|\pi(X)\cup\pi(Y)\cup\pi(Z)|\ge5.
\]
If each pairwise union of these three support sets had size at least three, Lemma 3.1 would select five distinct parts, with two represented in each of two bags and one in the third.

Choose corresponding vertices. Each selected pair is adjacent, hence is a transitive pair. By (4.1), the selected vertices induce a cyclic composition with bag sizes \(2,2,1\), which is isomorphic to \(H\). This contradicts \(H\)-freeness.

Thus two bags together meet at most two parts. Cyclically relabel so that these bags are \(Y,Z\), proving (4.3).

Let
\[
k=\max\{2,\vec\chi(D[X])\},
\]
and take an acyclic \(k\)-coloring of \(D[X]\). Assign different colors to the at most two original parts meeting \(Y\cup Z\), using colors from the same palette.

Consider any color \(i\). Its vertices in \(Y\cup Z\) lie in one original part, so there are no arcs between its vertices in \(Y\) and \(Z\). Its remaining inter-bag arcs have the form
\[
Z_i\Rightarrow X_i\Rightarrow Y_i.
\]
Thus \(Z_i\) contributes only sources relative to \(X_i\), and \(Y_i\) contributes only sinks. Since \(D[X_i]\) is acyclic, the whole color class is acyclic. This proves (4.4), and hence (4.2). ∎

### Corollary 4.2 — a bounded recursive subclass

Suppose an \(H\)-free multipartite tournament \(D\) admits a recursive vertex decomposition with the following node types:

1. **Leaf:** the induced subgraph meets at most four original parts.
2. **Transitive node:** its vertices partition into \(X,Y\) with \(X\Rightarrow Y\).
3. **Cyclic node:** its vertices partition into \(X,Y,Z\) satisfying (4.1).

Then
\[
\boxed{\vec\chi(D)\le4.}
\]

### Proof

Induct up the decomposition tree. A leaf is four-colorable by its parts. At a transitive node, the two children reuse the same palette. At a cyclic node, Theorem 4.1 applies. Every node induces an \(H\)-free graph because \(H\)-freeness is hereditary. ∎

More generally, if all leaves have dichromatic number at most \(b\), the same argument gives
\[
\vec\chi(D)\le\max\{4,b\}.
\]

The hypothesis is not that these operations automatically preserve \(H\)-freeness. Rather, the resulting graph is assumed \(H\)-free. Subject to that assumption, arbitrarily deep cyclic decompositions incur no cumulative coloring cost.

## 5. The bound four is sharp

Here is a fully specified probabilistic construction verifying sharpness for the subclass in Corollary 4.2.

Take four independent parts, each of size \(48\), and orient every inter-part edge independently and uniformly. The resulting graph \(D\) has \(192\) vertices. It is automatically \(H\)-free, since it has only four parts, and
\[
\vec\chi(D)\le4.
\]

Fix a set \(S\) of \(64\) vertices and put \(s_i=|S\cap P_i|\). The number of edges in its underlying graph is
\[
e(S)=\sum_{i<j}s_is_j
=\frac{64^2-\sum_i s_i^2}{2}.
\]
Under \(0\le s_i\le48\) and \(\sum_i s_i=64\), the sum of squares is maximized by the profile \(48,16,0,0\). Hence
\[
e(S)\ge48\cdot16=768.
\]

For any fixed linear order of \(S\), the probability that it is a topological order of \(D[S]\) is \(2^{-e(S)}\). Therefore
\[
\begin{aligned}
\Pr(\text{some acyclic set has size }64)
&\le \binom{192}{64}\,64!\,2^{-768}\\
&<2^{192}\,2^{384}\,2^{-768}\\
&=2^{-192}<1.
\end{aligned}
\]
Thus there exists such an orientation with no acyclic set of size \(64\). A three-color acyclic coloring of its \(192\) vertices would have a color class of size at least \(64\), which is impossible.

Consequently, this orientation satisfies
\[
\vec\chi(D)=4.
\]
It is a leaf of the decomposition class above, so the bound in Corollary 4.2 is optimal.

No computational experiment is being claimed here.

## 6. Stronger structure around a directed triangle

The preceding theorem applies directly to the corner sets in the supplied attempt. I verify the relevant orientation argument.

Let
\[
a\to b\to c\to a
\]
be a directed triangle. Remove temporarily all vertices in the three parts containing \(a,b,c\), and define
\[
\begin{aligned}
X_a&=\{x:c\to x\to b\},\\
X_b&=\{x:a\to x\to c\},\\
X_c&=\{x:b\to x\to a\}.
\end{aligned}
\]
These sets are pairwise disjoint.

### Proposition 6.1

If \(D\) is \(H\)-free, then
\[
X_b\Rightarrow X_a\Rightarrow X_c\Rightarrow X_b.
\tag{6.1}
\]

### Proof

Take \(x\in X_b\) and \(y\in X_c\) in different parts. If \(x\to y\), then
\[
a\to\{b,x\}\to\{c,y\}\to a
\]
is a copy of \(H\). All five vertices lie in distinct parts: \(x,y\) avoid the three base parts by definition. Therefore \(y\to x\), giving \(X_c\Rightarrow X_b\). The other two relations follow by cyclically permuting \(a,b,c\). ∎

### Corollary 6.2 — strengthened corner conclusion

Write
\[
K=X_a\cup X_b\cup X_c.
\]
Then
\[
\boxed{
\vec\chi(D[K])
\le
\max\{4,\vec\chi(D[X_a]),\vec\chi(D[X_b]),\vec\chi(D[X_c])\}.
}
\tag{6.2}
\]

Moreover, if all three corner sets are nonempty and \(\sigma(K)\ge5\), then two of them together meet at most two original parts. If \(X\) is the remaining corner set, then
\[
\vec\chi(D[K])\le\max\{2,\vec\chi(D[X])\}.
\tag{6.3}
\]

### Proof

Apply Theorem 4.1 to (6.1). ∎

This replaces the supplied attempt’s bound of eight for the corner union by four. More importantly, in the large-support case, it identifies a common two-part support for both smaller corners, allowing their colors to be absorbed into the larger corner.

## 7. A restriction on the remaining uniform sets

The vertices outside the three base parts partition into the three corner sets and
\[
U=\{v:v\to a,b,c\},
\qquad
W=\{v:a,b,c\to v\}.
\]
The cyclic support lemma does not control \(U\) and \(W\). There is, however, a useful restriction on arcs directed from \(W\) back to \(U\).

### Lemma 7.1 — reverse interfaces occur in two-part components

Fix any arc \(x\to y\), and set
\[
S=N^-(x)\cap N^-(y),\qquad
T=N^+(x)\cap N^+(y).
\]
Form a bipartite graph \(B\) with sides \(S,T\), where \(st\) is an edge when \(t\to s\) in \(D\).

If \(D\) is \(H\)-free, every nontrivial connected component of \(B\) has all its \(S\)-vertices in one original part and all its \(T\)-vertices in another original part.

### Proof

For \(s\in S\), its neighbors in \(B\) lie in one original part. Otherwise, two such neighbors \(t_1,t_2\) from distinct parts give
\[
s\to\{x,y\}\to\{t_1,t_2\}\to s,
\]
a copy of \(H\).

Similarly, for \(t\in T\), its neighbors in \(B\) lie in one original part. Otherwise,
\[
t\to\{s_1,s_2\}\to\{x,y\}\to t
\]
is a copy of \(H\).

Along a path in \(B\), consecutive vertices on the same side therefore lie in the same original part. This propagates through each connected component. The two parts are distinct because every edge of \(B\) represents an arc of \(D\). ∎

Taking \(x=a,y=b\), we have \(U\subseteq S\) and \(W\subseteq T\). Thus the reverse arcs \(W\to U\) satisfy this component restriction.

This is a structural constraint, not yet a bounded-color argument: there can be arbitrarily many components and part-pairs, and no global palette assignment handling all of them is proved here.

## 8. The remaining gap

The unrestricted conjecture is not proved by these results.

The precise missing step is a decomposition theorem. I have not shown that every \(H\)-free multipartite tournament admits the recursive transitive/cyclic decomposition of Corollary 4.2.

The triangle analysis explains the obstruction to a direct induction. Even when \(U=W=\varnothing\), coloring the three base parts separately only gives
\[
\vec\chi(D)
\le
3+\max\{4,\vec\chi(D[X_a]),\vec\chi(D[X_b]),\vec\chi(D[X_c])\}.
\]
The cyclic-composition coloring cost has been eliminated, but the cost of the base parts can still accumulate. In general, the two uniform sets also remain, with the nonuniform reverse interface described in Lemma 7.1.

Thus the established progress is:

* a sharp four-color theorem for a recursively decomposable subclass;
* an exact support obstruction for three cyclically oriented bags;
* a strengthened corner bound, reducing eight to four and localizing both small corners to two common parts in the large-support case;
* a two-part component restriction on reverse arcs between common in- and out-neighborhoods.

None of these arguments supplies an order-independent dichromatic bound for all \(H\)-free multipartite tournaments, nor an unbounded counterexample family.