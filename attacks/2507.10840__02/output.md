```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "Under the standard transversal-line definition of zig-zag, ceil(n/2) <= z(n) <= n^2/6 + O(n), convex configurations have exact value ceil(n/2), and z(4)=2.",
  "would_publish": false,
  "caveats": "The excerpt omits the formal definition; the quadratic upper bound uses non-spanning zig-zag paths and does not apply if every covering path is required to be Hamiltonian."
}
```

# 1. Definitions and results

For a point set \(S\), write \(z(S)\) for the minimum number of plane zig-zag paths covering \(E(K[S])\), and
\[
z(n)=\max_{|S|=n}z(S).
\]

The catalog excerpt does not reproduce the definition of a zig-zag path. I use the standard transversal-line formulation:

> A path \(v_0v_1\cdots v_t\) is a zig-zag path if there is a line \(\ell\), avoiding the vertices, such that consecutive vertices lie in opposite open halfplanes bounded by \(\ell\). Equivalently, every edge of the path intersects \(\ell\).

All paths constructed below are plane as well. In fact, their odd- and even-indexed vertex sets have disjoint, linearly separable convex hulls.

Under this convention, the following bounds hold for \(n\ge2\):
\[
\boxed{
\left\lceil\frac n2\right\rceil
\le z(n)
\le
\min\left\{
\left\lceil\frac{n(n-1)}4\right\rceil,\,
\frac{N(N-1)}6
\right\},
}
\]
where \(N\ge n\) is the least integer satisfying
\[
N\equiv1\ \text{or}\ 4\pmod {12}.
\]
Since \(N-n\le8\),
\[
\boxed{z(n)\le \frac{n^2}{6}+O(n).}
\]

I also prove:

1. Every four-point complete geometric graph is covered by two plane zig-zag paths. Consequently,
   \[
   z(1)=0,\qquad z(2)=1,\qquad z(3)=2,\qquad z(4)=2.
   \]
2. If the \(n\) points are in strictly convex position, the exact answer is
   \[
   \boxed{z(S)=\left\lceil\frac n2\right\rceil.}
   \]

The main worst-case asymptotic problem remains open: the bounds are still linear versus quadratic.

---

# 2. Universal lower bound

Every path on \(n\) vertices contains at most \(n-1\) edges. Therefore, if \(k\) paths cover all \(\binom n2\) edges, then
\[
k(n-1)\ge \binom n2.
\]
Thus
\[
z(n)\ge \left\lceil \frac{\binom n2}{n-1}\right\rceil
=\left\lceil\frac n2\right\rceil.
\]

This argument does not use planarity or the zig-zag condition.

---

# 3. A self-contained quadratic upper bound

We first show
\[
z(n)\le \left\lceil\frac{\binom n2}{2}\right\rceil
=\left\lceil\frac{n(n-1)}4\right\rceil.
\]

## Lemma 3.1
The edges of \(K_n\) can be partitioned into pairs of adjacent edges, with at most one edge left over.

### Proof

Let \(M=\binom n2\). We orient the edges of \(K_n\) so that every vertex has even indegree when \(M\) is even, and exactly one vertex has odd indegree when \(M\) is odd.

Such an orientation exists. Starting from any orientation, reversing an edge toggles the indegree parity at both endpoints. Hence, by reversing edges along paths pairing the vertices whose current parities are incorrect, any prescribed parity vector whose coordinate sum is congruent to \(M\pmod2\) can be obtained.

At each vertex, pair the edges directed into that vertex. If \(M\) is odd, leave one incoming edge unpaired at the unique odd-indegree vertex. Every edge is directed into exactly one endpoint, so this partitions \(E(K_n)\) into adjacent pairs and at most one singleton. ∎

Each adjacent pair \(uv,vw\) forms the path \(u-v-w\), which is automatically plane. It is also a zig-zag: in the triangle \(uvw\), a line parallel to \(uw\) and sufficiently close to \(v\) intersects the relative interiors of both \(uv\) and \(vw\), separating \(v\) from \(u,w\). A singleton edge is trivially a zig-zag path.

Thus each pair is covered by one path, proving the stated bound.

---

# 4. Four points require only two paths

## Lemma 4.1
For every four-point set \(S\) in general position,
\[
z(S)=2.
\]

### Convex case

Let the points be \(a,b,c,d\) in cyclic order. Take
\[
P_1=(a,d,b,c),\qquad P_2=(b,a,c,d).
\]
Their edge sets are
\[
E(P_1)=\{ad,db,bc\},\qquad
E(P_2)=\{ab,ac,cd\},
\]
so they partition \(E(K_4)\).

The only nonadjacent edge pair in \(P_1\) is \(ad,bc\), and in \(P_2\) it is \(ab,cd\); these are pairs of disjoint hull edges. Hence both paths are plane.

For \(P_1\), the parity classes are \(\{a,b\}\) and \(\{c,d\}\), whose convex hulls are disjoint. For \(P_2\), they are \(\{b,c\}\) and \(\{a,d\}\). Thus both paths are zig-zags.

### One interior point

Let \(x\) lie inside triangle \(abc\). Take
\[
P_1=(a,b,x,c),\qquad P_2=(b,c,a,x).
\]
These paths cover respectively
\[
\{ab,bx,cx\},\qquad \{bc,ac,ax\},
\]
again partitioning \(E(K_4)\).

The only nonadjacent pairs are \(ab,cx\) and \(bc,ax\), respectively. An interior-to-vertex segment cannot meet the opposite side of the containing triangle, so both paths are plane.

Their parity classes are respectively
\[
\{a,x\}\mid\{b,c\},
\qquad
\{a,b\}\mid\{c,x\}.
\]
The two convex hulls in each partition are disjoint segments, hence strictly linearly separable. Thus both paths are zig-zags.

Finally, two paths are necessary because one path has at most three edges while \(K_4\) has six. ∎

---

# 5. Design amplification: \(z(n)\le n^2/6+O(n)\)

I use the settled design-theoretic fact that a \(2\!-\!(N,4,1)\) design exists whenever
\[
N\equiv1\ \text{or}\ 4\pmod {12}.
\]
Such a design is a collection \(\mathcal B\) of four-element blocks in which every pair of vertices belongs to exactly one block. Counting pairs gives
\[
|\mathcal B|=\frac{\binom N2}{\binom42}
=\frac{N(N-1)}{12}.
\]

Given the \(n\)-point set \(S\), add \(N-n\) abstract dummy labels and take such a design on the resulting \(N\)-element label set. No geometric positions for the dummy labels are needed.

For every block \(B\), consider \(B\cap S\):

- if \(|B\cap S|\le1\), nothing is needed;
- if \(|B\cap S|=2\), its single edge is one zig-zag path;
- if \(|B\cap S|=3\), two paths cover its three edges;
- if \(|B\cap S|=4\), Lemma 4.1 gives two paths.

Thus every block contributes at most two paths. Every pair of genuine vertices belongs to exactly one block, so all edges of \(K_n[S]\) are covered. Therefore
\[
z(n)\le 2|\mathcal B|
=\frac{N(N-1)}6.
\]

The admissible residue classes \(1,4\pmod {12}\) have gaps at most \(9\), so \(N-n\le8\). Hence
\[
z(n)\le\frac{(n+8)(n+7)}6
=\frac{n^2}{6}+O(n).
\]

---

# 6. Exact answer for points in convex position

Let \(S=\{0,1,\dots,n-1\}\) be cyclically labeled, with arithmetic modulo \(n\). For \(a\in\mathbb Z_n\), define
\[
Z_a=
\bigl(
a,\ a-1,\ a+1,\ a-2,\ a+2,\ldots
\bigr),
\]
continuing until every vertex occurs. More explicitly,
\[
z_{a,0}=a,\qquad
z_{a,2r-1}=a-r,\qquad
z_{a,2r}=a+r
\]
whenever the index is at most \(n-1\).

These are the standard alternating-end, or Walecki-type, zig-zag paths.

## 6.1 Planarity and the zig-zag property

It suffices to take \(a=0\). The edges have the two forms
\[
A_r=\{r-1,-r\},
\qquad
B_r=\{-r,r\}.
\]
In the cyclic order cut between the extreme positive and negative indices, the endpoint intervals of every two such chords are nested or share an endpoint. They never alternate around the convex hull. Since two chords of a convex polygon cross exactly when their endpoints alternate, \(Z_a\) is plane.

The even-positioned vertices form one consecutive block of the cyclic order, and the odd-positioned vertices form the complementary consecutive block. Their convex hulls are disjoint and therefore strictly linearly separable. Every path edge joins the two blocks, so the separating line meets every edge. Hence \(Z_a\) is a zig-zag path.

## 6.2 Edge coverage

For \(s\in\mathbb Z_n\), set
\[
M_s=\bigl\{\{i,j\}: i\ne j,\ i+j\equiv s\pmod n\bigr\}.
\]
Every edge belongs to exactly one \(M_s\).

The odd-indexed edges of \(Z_a\) satisfy
\[
(a+r-1)+(a-r)\equiv 2a-1\pmod n,
\]
while its even-indexed edges satisfy
\[
(a-r)+(a+r)\equiv2a\pmod n.
\]
Thus
\[
E(Z_a)=M_{2a-1}\cup M_{2a}.
\]

### Even \(n=2m\)

If \(s\) is odd, then \(|M_s|=m\); if \(s\) is even, then \(|M_s|=m-1\). The path \(Z_a\) contains exactly these numbers of odd- and even-indexed edges, so it contains all edges in the two indicated classes.

For
\[
a=0,1,\dots,m-1,
\]
the residues \(2a-1\) run through all odd residues and \(2a\) through all even residues. Consequently,
\[
Z_0,Z_1,\dots,Z_{m-1}
\]
partition \(E(K_{2m})\). Hence \(m=n/2\) paths suffice.

### Odd \(n=2m+1\)

Here every \(M_s\) has \(m\) edges. Taking
\[
a=0,1,\dots,m
\]
covers all residue classes \(s\in\mathbb Z_n\); precisely one class, \(M_{2m}\), is covered twice. Therefore \(m+1=(n+1)/2\) paths suffice.

Together with the universal edge-counting lower bound,
\[
z(S)=\left\lceil\frac n2\right\rceil
\]
for every strictly convex \(S\).

---

# 7. What remains open

The resulting worst-case bracket is
\[
\left\lceil\frac n2\right\rceil
\le z(n)
\le \frac{n^2}{6}+O(n).
\]
Thus the argument improves the elementary quadratic upper bound but does not determine whether \(z(n)\) is linear, genuinely quadratic, or intermediate.

The convex case is extremal only for the elementary edge-counting lower bound; there is no justification here that convex configurations maximize \(z(S)\).

Finally, if Problem 5.2 requires every covering path to be spanning Hamiltonian, then the short-path and block-design upper bounds do not apply. Under that interpretation, the supplied existence theorem gives only
\[
z_H(n)\le 1+\binom n2-(n-1)
=\binom n2-n+2,
\]
by taking one Hamiltonian zig-zag path and then one covering path for each edge it misses. The convex construction remains valid because all \(Z_a\) are Hamiltonian.