```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds for hypergraphs with no 2-edges and no two vertex-disjoint independent triples.",
  "would_publish": false,
  "caveats": "This proves only a restricted dense case, not the general t=3 case; novelty of the special case has not been checked."
}
```

## 1. A precise partial result

Use weak hypergraph coloring: no hyperedge may be monochromatic. Vertex deletion discards incident hyperedges, and hyperedge contraction identifies all vertices of the contracted hyperedge. In particular, arbitrary shrinking of a hyperedge is not an allowed operation.

Write \(\eta(H)\) for the largest \(r\) such that \(K_r\) is a minor of \(H\). The conjectured upper bound is equivalent to
\[
\chi(H)\le \left\lceil \frac{3\eta(H)}2\right\rceil
\]
for every nonempty hypergraph \(H\).

I prove the following special case.

**Theorem.** Let \(H\) be a finite hypergraph whose hyperedges all have size at least \(3\). Suppose its independent triples are pairwise intersecting; equivalently, \(H\) has no two vertex-disjoint independent sets of size \(3\). Then
\[
\boxed{\chi(H)\le \left\lceil \frac{3\eta(H)}2\right\rceil.}
\]
Consequently, if such an \(H\) has no \(K_t\)-minor, then
\[
\chi(H)\le \left\lceil \frac32(t-1)\right\rceil.
\]

Within hypergraphs having no \(2\)-edges, this goes beyond the supplied independence-number-at-most-\(2\) case. It can even allow independence number \(5\): take all triples except those contained in a fixed five-vertex set. The independent triples are then the triples of that five-vertex set, which are pairwise intersecting.

The main ingredient is a sharp clique-minor bound for a dense class of \(3\)-uniform hypergraphs.

## 2. A sharp minor lemma

For a \(3\)-uniform hypergraph \(G\), let
\[
\mathcal F=\binom{V(G)}3\setminus E(G)
\]
be its family of missing triples.

**Lemma.** Suppose \(G\) has \(n\ge 6\) vertices and \(\mathcal F\) is intersecting. Then
\[
\boxed{\eta(G)\ge \left\lfloor\frac{n+1}{3}\right\rfloor.}
\]
This bound is sharp for every \(n\ge 6\).

### Minor models used in the proof

All our branch sets will be single vertices or pairwise disjoint hyperedges. To obtain a \(K_q\)-minor, it suffices that for every pair of branch sets there is a hyperedge contained in their union and meeting both. Contract the selected branch hyperedges; these witnessing hyperedges become ordinary edges. Delete everything else.

Thus none of the constructions below uses arbitrary hyperedge shrinking.

### Proof of the lemma

First consider \(n=6\). There are ten partitions of the vertex set into two triples. In each partition, at least one triple is a hyperedge, because two missing triples cannot be disjoint. Therefore \(G\) has at least ten hyperedges.

If every two hyperedges intersected in at most one vertex, their contained vertex-pairs would be disjoint, giving
\[
3|E(G)|\le \binom62=15,
\]
a contradiction. Hence two hyperedges intersect in exactly two vertices. Contracting one turns the other into a \(2\)-edge, yielding a \(K_2\)-minor. The case \(n=7\) follows by restricting to six vertices.

Now let \(n\ge 8\), and put
\[
q=\left\lfloor\frac{n+1}{3}\right\rfloor\ge 3.
\]
Since
\[
3q-1\le n,
\]
we may restrict to \(3q-1\) vertices. The missing triples remain intersecting. Thus assume
\[
n=3q-1.
\]

If \(\mathcal F=\varnothing\), take \(q-1\) disjoint triples and one additional vertex as branch sets. Every required adjacency is witnessed by a triple, so this gives a \(K_q\)-minor.

Suppose instead that \(A\in\mathcal F\), and put
\[
B=V(G)\setminus A.
\]
Every triple contained in \(B\) is a hyperedge: otherwise it would be a missing triple disjoint from \(A\). Also,
\[
|B|=3q-4\ge 5.
\]

There are two cases.

#### Case 1: Some missing triple meets \(A\) in exactly one vertex

Choose \(D\in\mathcal F\) with \(|D\cap A|=1\), and write
\[
A\setminus D=\{a,b\}.
\]
Choose distinct
\[
x,y\in B\setminus D;
\]
this is possible because \(D\) contains only two vertices of \(B\).

Use the branch sets
\[
S=\{a,b,x\},\qquad \{y\},
\]
together with a partition of \(B\setminus\{x,y\}\) into \(q-2\) triples
\[
T_1,\ldots,T_{q-2}.
\]

Both \(S\) and \(\{a,x,y\}\) are disjoint from \(D\), so both are hyperedges. The former makes \(S\) a valid branch set, and the latter witnesses adjacency between \(S\) and \(\{y\}\).

Every other required adjacency has a witnessing triple entirely in \(B\):

- between \(S\) and \(T_i\), use \(x\) and two vertices of \(T_i\);
- between \(\{y\}\) and \(T_i\), use \(y\) and two vertices of \(T_i\);
- between \(T_i\) and \(T_j\), use two vertices of one and one vertex of the other.

Each \(T_i\) is itself a hyperedge. These \(q\) branch sets therefore give a \(K_q\)-minor.

#### Case 2: No missing triple meets \(A\) in exactly one vertex

Then every triple consisting of one vertex of \(A\) and two vertices of \(B\) is a hyperedge.

Choose distinct \(a,b\in A\) and distinct \(x,y\in B\). Use
\[
S=\{a,x,y\},\qquad \{b\},
\]
and partition \(B\setminus\{x,y\}\) into \(q-2\) triples \(T_1,\ldots,T_{q-2}\).

Here:

- \(S\) is a hyperedge;
- \(\{b,x,y\}\) witnesses adjacency between \(S\) and \(\{b\}\);
- \(b\) together with two vertices of \(T_i\) witnesses adjacency between \(\{b\}\) and \(T_i\);
- all remaining adjacencies have witnesses entirely in \(B\), as in Case 1.

Again we obtain a \(K_q\)-minor. This proves the lower bound. \(\square\)

### Sharpness

Let \(G\) consist of the complete \(3\)-uniform hypergraph on \(n-1\) vertices and one isolated vertex. Its missing triples are precisely the triples containing the isolated vertex, so they are intersecting.

For the complete \(3\)-uniform hypergraph on \(m\ge 1\) vertices,
\[
\eta\!\left(K_m^{(3)}\right)=\left\lfloor\frac{m+2}{3}\right\rfloor.
\]

For the lower bound, use disjoint triple branch sets and at most one singleton, as above. For the upper bound, every nonsingleton branch set must contain at least three original vertices. Moreover, two singleton branch sets cannot be adjacent, since there are no original \(2\)-edges. Thus a \(K_r\)-model requires at least
\[
3(r-1)+1=3r-2
\]
vertices.

The isolated vertex cannot participate in a clique minor of order at least two. Consequently,
\[
\eta(G)=\left\lfloor\frac{n+1}{3}\right\rfloor,
\]
establishing sharpness.

## 3. Proof of the coloring theorem

The empty vertex set is trivial, so assume \(n=|V(H)|\ge 1\). Let
\[
\mathcal F=\{A\in\textstyle\binom{V(H)}3:A\text{ is independent in }H\}.
\]
Because \(H\) has no edges of size \(1\) or \(2\), a triple is independent precisely when it is not a \(3\)-edge.

Let \(G\) be obtained from \(H\) by deleting every hyperedge of size greater than \(3\). Then \(G\) has missing-triple family \(\mathcal F\), and
\[
\eta(H)\ge \eta(G).
\]

We distinguish whether \(\mathcal F\) is empty.

### No independent triple

If \(\mathcal F=\varnothing\), all triples are hyperedges. Put
\[
q_0=\left\lfloor\frac{n+2}{3}\right\rfloor.
\]
The complete \(3\)-uniform subhypergraph gives \(\eta(H)\ge q_0\).

Every pair is independent, so partitioning the vertices into pairs and possibly one singleton gives
\[
\chi(H)\le \left\lceil\frac n2\right\rceil.
\]
Since \(n\le 3q_0\),
\[
\chi(H)
 \le \left\lceil\frac{3q_0}{2}\right\rceil
 \le \left\lceil\frac{3\eta(H)}2\right\rceil.
\]

### At least one independent triple

Choose \(A\in\mathcal F\). Give \(A\) one color and partition the remaining vertices into pairs and possibly one singleton, using one color for each part. This proves
\[
\chi(H)
 \le 1+\left\lceil\frac{n-3}{2}\right\rceil
 =\left\lceil\frac{n-1}{2}\right\rceil.
\]
Hyperedges larger than three cause no problem: all color classes have size at most three, and the only size-three class is independent.

If \(n\le 5\), this is at most \(2\), while \(\eta(H)\ge1\), proving the required inequality.

If \(n\ge6\), the lemma gives
\[
\eta(H)\ge q:=\left\lfloor\frac{n+1}{3}\right\rfloor.
\]
The definition of \(q\) implies \(n-1\le3q\). Hence
\[
\chi(H)
 \le \left\lceil\frac{n-1}{2}\right\rceil
 \le \left\lceil\frac{3q}{2}\right\rceil
 \le \left\lceil\frac{3\eta(H)}2\right\rceil.
\]
This completes the proof of the theorem. \(\square\)

## 4. Consequences and the remaining gap

A concrete consequence for the smallest open case is:

**Corollary.** Every \(K_3\)-minor-free hypergraph on at most eight vertices whose hyperedges all have size at least three is \(3\)-colorable.

**Proof.** If its independent triples are pairwise intersecting, apply the theorem and \(\eta(H)\le2\). Otherwise, color two disjoint independent triples separately and give the at-most-two remaining vertices a third color. \(\square\)

More generally, the theorem supplies a necessary condition for a counterexample:

> Any counterexample to the conjecture having no \(2\)-edges must contain two vertex-disjoint independent triples.

The special-case proof is complete. The gap to the full conjecture is substantial, however. It does not treat general mixtures of \(2\)-edges and larger hyperedges, nor hypergraphs without \(2\)-edges that have disjoint independent triples. The key density inference—that the complement of an independent triple induces a complete \(3\)-uniform hypergraph—fails outside the intersecting-family hypothesis.

Thus this does **not** determine \(h(3)\), or give a new general upper bound on \(h(t)\). I have also not verified whether this particular dense special case or its sharp minor lemma already appears in the literature.