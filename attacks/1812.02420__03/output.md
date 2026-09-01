```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For positive integers, such a digraph exists exactly when b is at most 2 or k is at most b+1; in particular, (k,b)=(5,3) is impossible.",
  "would_publish": true,
  "caveats": "Assumes loopless digraphs may contain digons; literature priority has not been independently checked."
}
```

# Complete classification

Throughout, digraphs are finite and loopless, but antiparallel arcs are allowed. A directed \(2\)-cycle therefore counts as a directed cycle.

## Theorem

For positive integers \(k\ge b\), a digraph \(\vec K(k,b)\) satisfying
\[
\vec K(k,b)[\mathcal F]\text{ is acyclic}
\quad\Longleftrightarrow\quad
\bigcap_{B\in\mathcal F}B\ne\varnothing
\]
for every \(\mathcal F\subseteq\binom{[k]}b\) exists if and only if
\[
b\le 2\qquad\text{or}\qquad k\le b+1.
\]

Thus, for every \(b\ge3\), solutions exist only for \(k=b\) and \(k=b+1\). In particular, \((k,b)=(5,3)\) is a counterexample to general existence.

---

## 1. Minimal empty-intersection families must induce chordless cycles

We first record the main structural observation.

### Lemma

Suppose \(D\) has the required property, and let
\[
\mathcal M\subseteq\binom{[k]}b
\]
be inclusion-minimal subject to
\[
\bigcap_{B\in\mathcal M}B=\varnothing.
\]
If \(|\mathcal M|\ge3\), then \(D[\mathcal M]\) consists exactly of the arcs of a directed Hamilton cycle.

### Proof

Since \(\mathcal M\) has empty intersection, \(D[\mathcal M]\) is not acyclic and hence contains a directed cycle \(C\). If the vertex set of \(C\) were a proper subset \(\mathcal M'\subsetneq\mathcal M\), then \(D[\mathcal M']\) would not be acyclic, forcing
\[
\bigcap_{B\in\mathcal M'}B=\varnothing,
\]
contrary to the minimality of \(\mathcal M\). Thus \(C\) uses every vertex of \(\mathcal M\).

There can be no additional arc. Indeed, let \(X\to Y\) be an arc not belonging to this Hamilton cycle. Following the Hamilton cycle from \(Y\) to \(X\), and then using \(X\to Y\), gives a directed cycle on a proper subset of \(\mathcal M\). This again contradicts minimality. The reverse of a Hamilton-cycle arc would similarly give a directed \(2\)-cycle on a proper subset.

Hence \(D[\mathcal M]\) is exactly a directed cycle. \(\square\)

Consequently, if \(H\) denotes the undirected graph in which two vertices are adjacent whenever at least one arc of \(D\) joins them, then every minimal empty-intersection family induces an ordinary chordless cycle in \(H\).

---

## 2. Nonexistence for \(b\ge3\) and \(k=b+2\)

Put
\[
n=b+2.
\]
Every \(b\)-subset of \([n]\) is the complement of a unique edge of \(K_n\). For \(e\in\binom{[n]}2\), write
\[
B_e=[n]\setminus e.
\]
For every edge family \(\mathcal E\subseteq E(K_n)\),
\[
\bigcap_{e\in\mathcal E} B_e
=
[n]\setminus\bigcup_{e\in\mathcal E}e.
\]
Thus the corresponding family of \(b\)-sets has empty intersection exactly when \(\mathcal E\) is an edge cover of \(K_n\).

Fix \(v\in[n]\) and consider the full star
\[
\mathcal S_v=\{vx:x\in[n]\setminus\{v\}\}.
\]
It is an inclusion-minimal edge cover: deleting \(vx\) leaves \(x\) uncovered. Therefore, by the lemma, the corresponding \(n-1\) vertices
\[
\{B_{vx}:x\ne v\}
\]
induce a chordless cycle \(C_{n-1}\) in \(H\).

Since \(b\ge3\), we have \(n-1\ge4\). Hence this cycle contains two nonadjacent vertices, say \(B_{vp}\) and \(B_{vq}\), where \(p,q\ne v\).

Now define
\[
\mathcal T=
\{vx:x\in[n]\setminus\{v,p,q\}\}\cup\{pq\}.
\]
This is another inclusion-minimal edge cover:

- deleting \(vx\) leaves \(x\) uncovered;
- deleting \(pq\) leaves both \(p\) and \(q\) uncovered.

It has \(n-2\) edges, so its corresponding vertices must induce a chordless cycle \(C_{n-2}\) in \(H\).

Let
\[
\mathcal R=\mathcal S_v\setminus\{vp,vq\}.
\]
We can now compute \(H[\mathcal R]\) in two incompatible ways.

1. In the cycle \(H[\mathcal S_v]\cong C_{n-1}\), the deleted vertices \(B_{vp}\) and \(B_{vq}\) were chosen nonadjacent. Deleting two nonadjacent vertices from \(C_{n-1}\) leaves
   \[
   (n-1)-4=n-5
   \]
   edges.

2. In the cycle \(H[\mathcal T]\cong C_{n-2}\), deleting the single vertex \(B_{pq}\) leaves a path, with
   \[
   (n-2)-2=n-4
   \]
   edges.

Both induced graphs are the same graph \(H[\{B_e:e\in\mathcal R\}]\), but they would have different numbers of edges. This is a contradiction.

Therefore no required digraph exists for
\[
b\ge3,\qquad k=b+2.
\]

### Extension to every \(k\ge b+2\)

If a solution existed for some \(k>b+2\), choose a set \(U\subseteq[k]\) of size \(b+2\) and restrict the digraph to the vertices \(\binom Ub\). Intersections of these sets are unchanged, so this induced subdigraph would be a solution for \((b+2,b)\), which has just been proved impossible.

Hence
\[
\boxed{\text{No solution exists whenever }b\ge3\text{ and }k\ge b+2.}
\]

For the smallest instance \((k,b)=(5,3)\), the first minimal cover is a \(4\)-edge star and must induce a chordless \(C_4\); choosing two opposite vertices and replacing their star edges by the edge joining their leaves gives a minimal \(3\)-edge cover that would have to induce a triangle, contradicting the absence of the required chord in the \(C_4\).

---

## 3. Positive cases

### 3.1. The cases \(k=b\) and \(k=b+1\)

If \(k=b\), there is only one vertex, namely \([k]\), and the edgeless one-vertex digraph works.

If \(k=b+1\), write
\[
B_i=[k]\setminus\{i\},\qquad i\in[k].
\]
For \(I\subseteq[k]\),
\[
\bigcap_{i\in I}B_i=[k]\setminus I,
\]
which is empty exactly when \(I=[k]\). Therefore a directed cycle
\[
B_1\to B_2\to\cdots\to B_k\to B_1
\]
works: its full vertex set is cyclic, while every proper induced subdigraph is acyclic.

### 3.2. The case \(b=1\)

The vertices are the singletons \(\{i\}\). A family of distinct singleton sets has nonempty intersection exactly when it has at most one member. The complete bidirected digraph works: every induced subdigraph on at least two vertices contains a directed \(2\)-cycle.

### 3.3. The case \(b=2\)

Fix a cyclic order on \([k]\). For each \(x\in[k]\), let \(<_{x}\) be the linear order on \([k]\setminus\{x\}\) obtained by starting immediately after \(x\) and reading around the cyclic order.

Define a digraph on \(\binom{[k]}2\) as follows.

- If \(A\cap B=\varnothing\), put both arcs \(A\to B\) and \(B\to A\).
- If
  \[
  A=\{x,a\},\qquad B=\{x,c\},
  \]
  put
  \[
  A\to B\quad\Longleftrightarrow\quad a<_{x}c.
  \]

This is unambiguous because two distinct intersecting \(2\)-sets have a unique common element.

If a family \(\mathcal F\) has common element \(x\), all its members are of the form \(\{x,a\}\), and every arc between them increases in the order \(<_{x}\). Hence \(D[\mathcal F]\) is acyclic.

Conversely, suppose \(\mathcal F\) has empty intersection.

- If it contains two disjoint sets, those two vertices form a directed \(2\)-cycle.
- Otherwise \(\mathcal F\) is pairwise intersecting. A pairwise-intersecting family of \(2\)-sets with no common element contains a triangle: from
  \[
  \{x,a\},\{x,c\}
  \]
  and a member not containing \(x\), one obtains \(\{a,c\}\).

If \(x,a,c\) occur in that cyclic order, the three corresponding vertices are oriented as
\[
\{x,a\}\to\{x,c\}\to\{a,c\}\to\{x,a\}.
\]
Thus they form a directed \(3\)-cycle. Hence every empty-intersection family is cyclic.

This proves existence for every \(k\ge2\) when \(b=2\).

---

## Conclusion

For positive integers \(k\ge b\),
\[
\boxed{
\vec K(k,b)\text{ exists }
\Longleftrightarrow
b\le2\ \text{or}\ k-b\le1.
}
\]

Thus the proposed directed Kneser graphs do not exist in the generality requested. The first impossible parameter pair is \((5,3)\). There are no remaining mathematical cases under the stated digraph conventions.