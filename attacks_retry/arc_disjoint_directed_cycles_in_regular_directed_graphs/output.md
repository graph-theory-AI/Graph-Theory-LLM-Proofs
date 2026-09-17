```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds for k≤4 and, by an exact complementation identity, whenever n≤k+5.",
  "would_publish": false,
  "caveats": "Finite loopless digraphs; the unrestricted case k≥5 remains unresolved here, and novelty is not claimed."
}
```

# Partial result: the conjecture holds in degree four

I use the standard loopless convention: opposite arcs are permitted, but loops and parallel arcs are not. All digraphs are finite, and regular digraphs of positive degree are nonempty.

Write
\[
\nu(D)=\max\{|\mathcal C|:\mathcal C\text{ is a collection of arc-disjoint directed cycles in }D\},
\qquad
T(k)=\binom{k+1}{2}.
\]

The splitting approach in the supplied attempt can be pushed one degree further. All facts reused below are proved explicitly.

## Main theorem

**Theorem.** Let \(G\) be a \(k\)-regular digraph on \(n\) vertices. If
\[
\min\{k,n-1-k\}\le 4,
\]
then
\[
\nu(G)\ge T(k).
\]

Thus the conjecture holds for \(k\le4\), and also whenever \(n\le k+5\).

The proof also gives two further consequences:

- Every balanced simple digraph of minimum outdegree at least \(r\), for \(1\le r\le4\), contains at least \(T(r)\) arc-disjoint directed cycles.
- For arbitrary \(k=4q+r\), where \(0\le r<4\),
  \[
  \nu(G)\ge 10q+T(r).
  \]

These are partial results, not a resolution of the general conjecture. No claim of novelty or updated literature status is made.

---

## 1. Elementary packing tools

A digraph is **balanced** if every vertex has equal indegree and outdegree.

Every balanced digraph decomposes into directed cycles: a nonempty balanced digraph contains a directed cycle, and deleting the arcs of a cycle preserves balance. In particular,
\[
\nu(D)\ge \max_{v\in V(D)}d_D^+(v)
\qquad\text{when }D\text{ is balanced}.
\tag{1}
\]
Indeed, a cycle decomposition must use at least \(d_D^+(v)\) cycles to cover all arcs leaving \(v\).

Also, a digraph of minimum outdegree at least \(s\) contains \(s\) arc-disjoint directed cycles. After deleting fewer than \(s\) directed cycles, every vertex still has positive outdegree.

The following combination will be useful.

**Protected-vertex bound.** If \(D\) is balanced and \(D-v\) has minimum outdegree at least \(s\), then
\[
\nu(D)\ge d_D^+(v)+s.
\tag{2}
\]

**Proof.** Find \(s\) arc-disjoint cycles in \(D-v\), and delete their arcs from \(D\). The remaining digraph is balanced, and \(v\) retains its original outdegree. Apply (1). \(\square\)

Consequently, every \(k\)-regular digraph with \(k\ge1\) satisfies
\[
\nu(G)\ge 2k-1.
\tag{3}
\]
This proves the conjecture for \(k=1,2\); the case \(k=0\) is immediate.

---

## 2. Exact complementation

A pair of opposite arcs is a **digon**.

### Lemma 1
If \(u\to v\) and \(v\to u\) are arcs of \(D\), and
\[
D'=D-\{u\to v,v\to u\},
\]
then
\[
\nu(D)=1+\nu(D').
\tag{4}
\]

**Proof.** Adding the digon to a packing in \(D'\) proves one inequality.

For the other, take a maximum packing in \(D\). If at most one of the two arcs is used, discard at most one cycle. If both arcs belong to the same cycle, that cycle is the digon, which can be discarded.

Otherwise, the two arcs belong to distinct cycles. Removing them leaves a directed \(v\)-to-\(u\) path and a directed \(u\)-to-\(v\) path. Their concatenation is a nonempty closed directed trail, and therefore contains a directed cycle. Replace the two original cycles by such a cycle. This loses only one cycle and avoids both deleted arcs. \(\square\)

Let \(b(D)\) be the number of digons in \(D\), and let \(R(D)\) be obtained by deleting all their arcs. Repeated application of (4) gives
\[
\nu(D)=b(D)+\nu(R(D)).
\tag{5}
\]

Let \(\overline D\) denote the directed complement on the same vertex set, excluding loops. For each unordered pair of vertices:

- a digon of \(D\) becomes an empty pair in \(\overline D\);
- an empty pair becomes a digon;
- a single arc becomes its reverse.

Hence \(R(\overline D)\) is the reversal of \(R(D)\), so these residual digraphs have equal packing numbers. If \(D\) has \(n\) vertices and \(m\) arcs, counting the three types of unordered pairs gives
\[
b(D)-b(\overline D)=m-\binom n2.
\]
Thus
\[
\boxed{\nu(D)-\nu(\overline D)=|A(D)|-\binom n2.}
\tag{6}
\]

For a \(k\)-regular \(G\), put
\[
t=n-1-k.
\]
Its complement is \(t\)-regular, and (6) becomes
\[
\boxed{\nu(G)-T(k)=\nu(\overline G)-T(t).}
\tag{7}
\]

The conjectured inequality is therefore equivalent for a regular digraph and its complement.

Since degrees at most two are already settled, (7) settles all 3-regular digraphs on at most six vertices.

---

## 3. Admissible splitting

Let \(v\) have indegree and outdegree \(r\). Pair its incoming arcs bijectively with its outgoing arcs. Replace each paired path
\[
a\to v\to b
\]
by \(a\to b\), and delete \(v\).

The split is **admissible** if every new arc is a nonloop and was absent before the split. An admissible split of an \(r\)-regular digraph produces another simple loopless \(r\)-regular digraph, on one fewer vertex.

If \(H\) is obtained from \(G\) by an admissible split, then
\[
\nu(G)\ge \nu(H).
\tag{8}
\]
To see this, lift each new arc in a packing of \(H\) to its paired two-arc path through \(v\). The resulting closed directed trails are arc-disjoint. Selecting a directed cycle from each trail proves (8).

The same lifting argument applies to a **single-pair split**, in which just one path \(a\to v\to b\) is replaced and \(v\) is retained.

Existence of a full admissible split is a matching question. Its bipartite graph has parts
\[
N^-(v),\qquad N^+(v),
\]
with \(a\) adjacent to \(b\) precisely when
\[
a\ne b\quad\text{and}\quad a\to b\notin A(G).
\tag{9}
\]

### Lemma 2: the degree-three and degree-four splitting lemma
Let \(r\in\{3,4\}\), and let \(G\) be \(r\)-regular. If some vertex \(v\) belongs to no digon, then some vertex of \(G\) admits an admissible split.

**Proof.** Put
\[
A=N^-(v),\qquad B=N^+(v).
\]
The absence of a digon at \(v\) means that \(A\cap B=\varnothing\).

Every row and every column of the allowed-pair graph (9) has a neighbor. For example, \(a\in A\) already sends an arc to \(v\), so it cannot send arcs to all \(r\) vertices of \(B\). The column argument uses indegrees.

If there is a perfect matching, split \(v\). Otherwise, Hall’s theorem gives a complete directed bipartite block of forbidden pairs. For \(r=3\), it has two tails and two heads. For \(r=4\), it can be chosen with sizes \(2,3\) or \(3,2\). Reversing every arc if necessary, we may therefore label vertices so that
\[
a_1,a_2\in A,\qquad b_1,\ldots,b_{r-1}\in B,
\]
and all arcs
\[
a_i\to b_j
\qquad
(i=1,2,\;1\le j\le r-1)
\]
are present.

Regularity forces
\[
N^+(a_1)=N^+(a_2)=S:=\{v,b_1,\ldots,b_{r-1}\}.
\tag{10}
\]

Consider splitting \(a_1\), and put \(U=N^-(a_1)\). We have
\[
U\cap\{a_1,a_2,v\}=\varnothing.
\tag{11}
\]
Here loops exclude \(a_1\), equation (10) excludes \(a_2\), and the absence of a digon at \(v\) excludes \(v\).

We examine the forbidden pairs from \(U\) to \(S\).

- With head \(v\), a forbidden pair must have its tail in
  \[
  A\setminus\{a_1,a_2\},
  \]
  so there are at most \(r-2\) such tails.
- With head \(b_j\), the already known inneighbors are \(v,a_1,a_2\). There are only \(r-3\) additional inneighbors. Together with the possible loop pair \((b_j,b_j)\), this gives at most \(r-2\) forbidden tails.

Also, every row has an allowed pair. If \(u\notin A\), then \(u\to v\) is an allowed replacement. If \(u\in A\), then \(u\notin S\); forbidding all \(r\) pairs from \(u\) to \(S\), together with the existing arc \(u\to a_1\), would give \(d^+(u)\ge r+1\).

For \(r=3\), each column has at most one forbidden tail. Every set of at least two rows therefore meets all columns, while singleton sets have a neighbor. Hall’s condition follows.

For \(r=4\), every column has at most two forbidden tails. Every set of at least three rows meets all four columns, so the only possible Hall obstruction is a pair \(Q\subseteq U\) whose allowed neighborhood has size at most one. At least three columns would then forbid both tails of \(Q\).

At least two of those columns have heads among \(b_1,b_2,b_3\). A two-element forbidden set for column \(b_j\) must contain \(b_j\), since there is only one possible additional existing-arc obstruction besides the loop. Thus, for two distinct such columns,
\[
Q=\{b_j,b_\ell\}\subseteq B.
\]
Column \(v\) cannot forbid these tails, because its forbidden tails lie in \(A\). Therefore all three columns \(b_1,b_2,b_3\) would have to forbid \(Q\), forcing \(Q\) to contain all three distinct heads—a contradiction.

The allowed-pair graph for splitting \(a_1\) consequently has a perfect matching. \(\square\)

The degree-four part is the additional ingredient beyond the supplied attempt.

---

## 4. Degree three

### Proposition 3
Every 3-regular digraph contains six arc-disjoint directed cycles.

**Proof.** Suppose otherwise, and choose a counterexample \(G\) with the fewest vertices. By Section 2,
\[
n\ge7.
\]

Let \(b\) be the number of digons. If \(b\ge6\), we are done. If \(b=4\) or \(5\), delete all digons to obtain a balanced digraph \(R\). It has
\[
|A(R)|=3n-2b\ge3n-10>n,
\]
so some vertex has outdegree at least two. By (1), \(R\) has at least two arc-disjoint cycles, giving at least six cycles together with the digons.

Thus a counterexample has \(b\le3\). At most six vertices belong to digons, so some vertex belongs to no digon. Lemma 2 supplies an admissible split. The resulting 3-regular digraph has one fewer vertex and, by minimality, has six arc-disjoint cycles. Equation (8) gives the same conclusion for \(G\), a contradiction. \(\square\)

Using complementation, the conjecture now holds whenever \(n-1-k\le3\). In particular, every 4-regular digraph on at most eight vertices is settled.

---

## 5. Degree four

### Proposition 4
Every 4-regular digraph contains ten arc-disjoint directed cycles.

**Proof.** Suppose otherwise, and choose a counterexample \(G\) with the fewest vertices. Then
\[
n\ge9,\qquad \nu(G)\le9.
\tag{12}
\]

No vertex admits an admissible split, since such a split would produce a smaller counterexample. Lemma 2 therefore implies that **every vertex belongs to a digon**.

Let \(b\) be the number of digons, and let \(h(v)\) be the number of digons incident with \(v\). Thus
\[
h(v)\ge1,\qquad \sum_v h(v)=2b,\qquad n\le2b.
\tag{13}
\]

Delete all digons, obtaining a balanced digraph \(R\). Its degrees satisfy
\[
d_R^+(v)=4-h(v)\le3.
\tag{14}
\]
By (5) and (12),
\[
\nu(R)\le9-b.
\]
Applying (1) and summing the outdegrees gives
\[
4n-2b=|A(R)|\le n(9-b),
\]
or
\[
(b-5)n\le2b.
\tag{15}
\]

Equations (12) and (13) imply \(b\ge5\). Hence \(b-5\ge0\), and (15) yields
\[
9(b-5)\le2b.
\]
Therefore \(b\le6\). Only two cases remain.

Define the total degree deficit of \(R\) from degree three by
\[
\varepsilon
 :=\sum_v\bigl(3-d_R^+(v)\bigr)
 =2b-n.
\tag{16}
\]

### Case 1: \(b=5\)

Here \(9\le n\le10\), so \(\varepsilon\le1\). Thus all vertices of \(R\) have outdegree three, except possibly one vertex \(u\) of outdegree two.

Choose a degree-three vertex \(w\) which is not an outneighbor of \(u\), if \(u\) exists. There are at least eight degree-three vertices and at most two forbidden choices, so this is possible.

Every vertex of \(R-w\) has outdegree at least two. The protected-vertex bound gives
\[
\nu(R)\ge3+2=5.
\]
Together with the five digons, this gives ten cycles, a contradiction.

### Case 2: \(b=6\)

Now \(9\le n\le12\), so \(\varepsilon\le3\). Consequently:

- at least \(n-3\ge6\) vertices have outdegree three;
- at most one vertex has outdegree one.

Delete any isolated vertices from \(R\), obtaining \(R_0\); this changes neither degrees of the remaining vertices nor the packing number. Choose a degree-three vertex \(w\) that is not the unique outneighbor of the degree-one vertex, if such a vertex exists.

Every vertex of \(R_0-w\) has positive outdegree: vertices of degree at least two lose at most one outgoing arc, and the possible degree-one vertex loses none. By (2),
\[
\nu(R)=\nu(R_0)\ge3+1=4.
\]
Together with the six digons, this again gives ten cycles.

Both cases contradict (12). \(\square\)

Combining Propositions 3 and 4 with the elementary cases proves the conjecture for \(k\le4\). Equation (7) then proves it whenever
\[
n-1-k\le4,
\]
which completes the main theorem.

---

## 6. Further consequences

### 6.1 Balance and minimum degree suffice for \(r\le4\)

**Corollary 5.** Let \(1\le r\le4\). Every balanced simple loopless digraph \(D\) with minimum outdegree at least \(r\) satisfies
\[
\nu(D)\ge T(r).
\]

**Proof.** We reduce to the \(r\)-regular case by single-pair splits.

Suppose \(D\) is not \(r\)-regular, and let \(v\) have maximum outdegree \(M>r\). Put
\[
A=N^-(v),\qquad B=N^+(v),
\]
so \(|A|=|B|=M\).

If there is a pair \(a\in A,b\in B\) with \(a\ne b\) and \(a\to b\) absent, perform the single-pair split
\[
a\to v\to b\quad\longmapsto\quad a\to b.
\]
This preserves balance and all degrees except that of \(v\), which decreases by one and remains at least \(r\). Packing numbers do not increase under this reduction, by the lifting argument.

If no such pair exists, then \(A=B\). Indeed, a vertex \(a\in A\setminus B\) would send arcs to all \(M\) vertices of \(B\), as well as to \(v\), contradicting maximality of \(M\). Moreover, every ordered pair of distinct vertices in \(A\) is an arc. Thus \(A\cup\{v\}\) induces a complete symmetric digraph on \(M+1\) vertices, supplying
\[
T(M)\ge T(r)
\]
digons.

Otherwise, continue splitting. The nonnegative integer
\[
\sum_x(d_D^+(x)-r)
\]
decreases by one at every step. The process reaches an \(r\)-regular digraph, or encounters the complete symmetric subdigraph just described. The proved regular cases and lifting finish the argument. \(\square\)

### 6.2 An elementary bound for every degree

Every \(k\)-regular digraph decomposes into \(k\) directed 1-factors. To see this, form the bipartite incidence graph with a tail-copy and a head-copy of each vertex. It is \(k\)-regular, so Hall’s theorem gives a perfect matching; remove it and repeat.

Write \(k=4q+r\), with \(0\le r<4\). Group the 1-factors into \(q\) groups of four and one remaining group of \(r\). Applying the proved cases to these arc-disjoint regular subdigraphs gives
\[
\boxed{\nu(G)\ge10q+T(r).}
\tag{17}
\]
This is only a linear bound and does not improve the quoted quadratic bound asymptotically.

### 6.3 Degree four is sharp at every order

For \(n\ge5\), let \(P(n,4)\) have vertices \(\mathbb Z_n\) and arcs
\[
x\to x+j,\qquad 1\le j\le4.
\]
Assign weight \(j\) to such an arc. Every directed cycle has total weight a positive multiple of \(n\), hence at least \(n\). The total weight of all arcs is
\[
n(1+2+3+4)=10n.
\]
Thus any arc-disjoint packing has at most ten cycles. Proposition 4 supplies ten, so
\[
\nu(P(n,4))=10
\qquad(n\ge5).
\]

---

## 7. What remains unresolved

No general proof or counterexample is obtained.

The local splitting argument above is complete for degrees three and four. In degree five, a failed Hall condition can produce a \(3\times3\) complete directed block between the in- and outneighborhoods of a digon-free vertex. Unlike the blocks used above, this need not saturate either side’s degrees, so the reduction no longer follows.

By complementation and the proved cases, any counterexample could be replaced by one satisfying
\[
5\le k\le\frac{n-1}{2}.
\]
The unrestricted conjecture in this range remains untreated here.