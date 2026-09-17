```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained argument proves the Hamiltonian-path assertion for every connected vertex-transitive graph of order p, 2p, or 3p, where p is prime.",
  "would_publish": false,
  "caveats": "This is a restricted-order result with no novelty claim; the unrestricted conjecture is not resolved."
}
```

## Scope and partial result

Graphs below are finite, simple, and undirected. A graph is **traceable** if it has a Hamiltonian path.

I do not obtain a proof or counterexample for the full Lovász problem. I give a complete proof of the following special case, followed by a general restriction on a possible minimum-order counterexample. No recent literature claims from the catalog are needed.

**Theorem 1.** Let \(p\) be an odd prime. Suppose a connected regular graph \(G\) has an automorphism whose cycle decomposition consists of at most three cycles, all of length \(p\). Then \(G\) is traceable.

**Corollary 2.** Every connected vertex-transitive graph of order \(p\), \(2p\), or \(3p\), where \(p\) is prime, is traceable.

Theorem 1 does not require vertex-transitivity. Regularity and the specified cyclic symmetry suffice.

## 1. Facts about prime-sized cyclic orbits

Let \(\sigma\) be an automorphism of order \(p\), with no fixed vertices. Label two of its orbits
\[
X=\{x_i:i\in\mathbb Z_p\},\qquad
Y=\{y_i:i\in\mathbb Z_p\},
\]
so that \(\sigma\) adds \(1\) to every subscript.

### Internal edges

The edges within \(X\) are specified by a set
\[
S_X\subseteq\mathbb Z_p\setminus\{0\},\qquad S_X=-S_X:
\]
we have \(x_i x_{i+a}\in E(G)\) precisely when \(a\in S_X\).

Consequently:

* the internal degree of \(X\) is even, since \(p\) is odd;
* if \(X\) contains any edge, then \(G[X]\) has a Hamiltonian cycle.

Indeed, for any \(a\in S_X\), primality of \(p\) makes
\[
x_0,x_a,x_{2a},\ldots,x_{(p-1)a},x_0
\]
a Hamiltonian cycle.

### Edges between two orbits

The edges between \(X\) and \(Y\) are a union of perfect matchings
\[
M_t=\{x_i y_{i+t}:i\in\mathbb Z_p\},
\qquad t\in T_{XY}\subseteq\mathbb Z_p.
\]
Thus every vertex in either orbit has exactly \(|T_{XY}|\) neighbors in the other.

If \(|T_{XY}|\ge 2\), the graph on \(X\cup Y\) already contains a Hamiltonian cycle using only edges between the two orbits. To see this, choose distinct \(s,t\in T_{XY}\). Alternating between \(M_s\) and \(M_t\) gives
\[
x_i,\ y_{i+s},\ x_{i+s-t}.
\]
The resulting two-step displacement is \(s-t\ne0\), which generates \(\mathbb Z_p\). Hence \(M_s\cup M_t\) is a single cycle of length \(2p\).

### Joining spanning pieces

We will use two elementary observations.

1. **Two disjoint cycles joined by an edge have a spanning path.**  
   Delete one cycle edge incident with each endpoint of the joining edge, then concatenate the resulting paths.

2. **Cyclic orbits with internal Hamiltonian cycles can be traversed along a path of orbits.**  
   Suppose distinct orbits \(B_1,\ldots,B_k\) each have an internal Hamiltonian cycle, and there is an edge between \(B_i\) and \(B_{i+1}\). Every vertex of \(B_i\) then has a neighbor in \(B_{i+1}\). Traverse \(B_1\) by a Hamiltonian path, cross from its last vertex to \(B_2\), traverse \(B_2\) starting at the entry vertex, and continue. A cycle can be opened into a Hamiltonian path starting at any prescribed vertex.

The second observation does not prescribe both endpoints of a path inside an orbit; it only prescribes the entry vertex. This distinction is important.

## 2. Proof of Theorem 1

### One orbit

Connectedness guarantees an edge. The internal-edge observation therefore supplies a Hamiltonian cycle.

### Two orbits

Write the orbits as \(X,Y\). Let their internal degrees be \(r_X,r_Y\), and let \(t\) be the number of matchings between them.

Regularity gives
\[
r_X+t=r_Y+t,
\]
so \(r_X=r_Y\).

If this common internal degree is positive, each orbit contains a spanning cycle. Connectedness supplies an edge between the two cycles, and joining them gives a Hamiltonian path.

If the common internal degree is zero, all edges run between the two orbits. Connectedness forces \(t\ge2\): with \(t=0\) there are no edges, and with \(t=1\) the graph is a perfect matching. Two of the matchings give a Hamiltonian cycle.

### Three orbits

Write the orbits as \(X,Y,Z\). Let their internal degrees be
\[
r_X,r_Y,r_Z.
\]
Let \(a,b,c\) be the numbers of matchings between \(X,Y\), between \(X,Z\), and between \(Y,Z\), respectively. If the common degree of \(G\) is \(d\), then
\[
r_X+a+b=r_Y+a+c=r_Z+b+c=d. \tag{1}
\]
Each \(r_X,r_Y,r_Z\) is a nonnegative even integer.

We distinguish the four possible numbers of positive internal degrees.

#### Case 1: All three internal degrees are positive

Each orbit has an internal Hamiltonian cycle. The graph on the three orbits, with adjacency meaning that some edge runs between them, is connected. Every connected graph on three vertices has a spanning path.

Traverse the three orbits in that order using the joining observation above. This gives a Hamiltonian path of \(G\).

#### Case 2: Exactly two internal degrees are positive

Relabel so that
\[
r_X=0,\qquad r_Y,r_Z>0.
\]
Equation (1) gives
\[
r_Y=b-c,\qquad r_Z=a-c.
\]
Since both positive internal degrees are at least \(2\),
\[
a,b\ge c+2\ge2.
\]

Two matchings between \(X\) and \(Y\) give a spanning cycle on \(X\cup Y\). The orbit \(Z\) has an internal spanning cycle. Since \(b>0\), an edge joins these two cycles. They therefore yield a Hamiltonian path of \(G\).

#### Case 3: Exactly one internal degree is positive

Relabel so that
\[
r_X=r_Y=0,\qquad r_Z>0.
\]
Equation (1) gives
\[
b=c,\qquad r_Z=a-b.
\]
Connectedness forces \(b=c>0\), since otherwise \(Z\) is separated from \(X\cup Y\). Also \(r_Z\ge2\), so
\[
a=b+r_Z\ge3.
\]

Again, two matchings between \(X\) and \(Y\) give a spanning cycle on \(X\cup Y\), while \(Z\) has an internal spanning cycle. An edge between them yields a Hamiltonian path.

#### Case 4: All three internal degrees are zero

Equation (1) implies
\[
a=b=c=t.
\]
Connectedness gives \(t>0\).

Use matching-offset sets oriented from \(X\) to \(Y\), from \(Y\) to \(Z\), and from \(Z\) to \(X\). Choose offsets
\[
\alpha\in T_{XY},\qquad
\beta\in T_{YZ},\qquad
\gamma\in T_{ZX}.
\]
Their three matchings contain the walk pattern
\[
x_i,\ y_{i+\alpha},\ z_{i+\alpha+\beta},\
x_{i+\alpha+\beta+\gamma}.
\]
Put
\[
\delta=\alpha+\beta+\gamma\in\mathbb Z_p.
\]

If \(\delta\ne0\), repeating this pattern visits every index in each orbit and produces a Hamiltonian cycle of length \(3p\).

It remains to show that some choice has \(\delta\ne0\). Suppose instead that
\[
\alpha+\beta+\gamma=0
\]
for every choice of the three offsets. Fixing two offsets and varying the third shows that each offset set is a singleton. Thus \(t=1\), and the three unique offsets sum to zero.

But then these three matchings are all the edges of \(G\), and they form \(p\) disjoint triangles. This contradicts connectedness.

Thus a suitable choice exists, completing every case of Theorem 1. \(\square\)

## 3. Why the required automorphism exists in the stated orders

The following elementary permutation-group lemma supplies the symmetry used above.

**Lemma 3.** Let a finite group \(A\) act faithfully and transitively on a set of size \(kp\), where \(p\) is prime and \(1\le k\le p\). Then \(A\) contains a fixed-point-free element of order \(p\).

**Proof.**

First suppose \(k<p\). Let \(P\) be a Sylow \(p\)-subgroup of \(A\). For a point \(v\), orbit-stabilizer gives
\[
[A:A_v]=kp.
\]
Writing \(|H|_p\) for the largest power of \(p\) dividing \(|H|\), we obtain
\[
|P\cdot v|
=\frac{|P|}{|P_v|}
\ge \frac{|A|_p}{|A_v|_p}
=p.
\]
A \(P\)-orbit has prime-power size, and
\[
|P\cdot v|\le kp<p^2.
\]
Every \(P\)-orbit therefore has size exactly \(p\), giving \(k\) orbits.

On each orbit, \(P\) induces a transitive \(p\)-subgroup of \(S_p\). Such a subgroup has order \(p\), since \(p\) occurs only once in the prime factorization of \(p!\). Let \(K_i\) be the kernel of the action on the \(i\)-th orbit. Then
\[
[P:K_i]=p.
\]
Moreover,
\[
\left|\bigcup_{i=1}^kK_i\right|
\le \frac{k}{p}|P|<|P|.
\]
Choose \(\sigma\) outside this union. On each orbit, \(\sigma\) is a nonidentity element of a cyclic group of order \(p\), hence a \(p\)-cycle. Thus \(\sigma\) has order \(p\) and no fixed points.

Now suppose \(k=p\), so the degree is \(p^2\). The same orbit-stabilizer calculation gives
\[
|P\cdot v|\ge p^2,
\]
so \(P\) is transitive.

Choose a central element \(z\in Z(P)\) of order \(p\). If \(z\) fixed one point, centrality and transitivity of \(P\) would make it fix every point, contrary to faithfulness. Therefore \(z\) is fixed-point-free. \(\square\)

### Proof of Corollary 2

A vertex-transitive graph is regular.

For odd \(p\), each of the orders \(p,2p,3p\) has the form \(kp\) with \(k\le p\). Lemma 3 gives an automorphism consisting of exactly \(k\le3\) cycles of length \(p\). Theorem 1 applies.

For \(p=2\):

* order \(2\) gives \(K_2\);
* a connected vertex-transitive graph of order \(4\) is regular of degree \(2\) or \(3\), hence is \(C_4\) or \(K_4\);
* order \(6\) is already covered as \(2\cdot3\).

Every case is therefore covered. \(\square\)

## 4. A general restriction on a minimum counterexample

There is also a useful lifting statement that does not depend on prime orders.

**Lemma 4 — normal-orbit lifting.** Let \(A\le\operatorname{Aut}(G)\) be transitive, and let \(N\triangleleft A\). Form the simple quotient graph \(G/N\) whose vertices are the \(N\)-orbits, with two distinct orbits adjacent when an edge of \(G\) joins them.

If \(G/N\) and every induced orbit graph \(G[B]\) are traceable, then \(G\) is traceable.

**Proof.** The group \(N\) acts transitively on each orbit \(B\). Thus a Hamiltonian path in \(G[B]\) can be moved by an element of \(N\) to start at any prescribed vertex of \(B\).

Also, if two \(N\)-orbits \(B,C\) are adjacent, every vertex of \(B\) has a neighbor in \(C\). Indeed, apply elements of \(N\) to one edge between them.

Take a Hamiltonian path \(B_1,\ldots,B_t\) in the quotient. Traverse \(B_1\) by a Hamiltonian path, cross from its endpoint to \(B_2\), traverse \(B_2\) starting at that entry vertex, and continue. The resulting path visits every vertex exactly once. \(\square\)

Consequently, if a counterexample exists and \(G\) has minimum possible order, then:

> For every transitive \(A\le\operatorname{Aut}(G)\), every nontrivial intransitive normal subgroup \(N\triangleleft A\) has disconnected induced orbit graphs.

To verify this, suppose an induced orbit graph were connected. Normality and transitivity imply that all induced orbit graphs are isomorphic and vertex-transitive, and that \(G/N\) is connected and vertex-transitive. Both their orders are strictly smaller than \(|V(G)|\). Minimality would make them traceable, and Lemma 4 would contradict the choice of \(G\).

This is a necessary structural condition, not an assumption that a smaller unresolved conjecture is true.

## 5. What remains unresolved

The proof has identifiable limitations:

* **Primality is essential to the local argument.** For an orbit of composite size \(m\), a nonzero step need not traverse the entire orbit. Likewise, two cross-matchings with offsets \(s,t\) form \(\gcd(m,s-t)\) cycles, not necessarily one.
* **More orbits require new coordination.** A connected quotient on at least four vertices need not have a spanning path, and the three-orbit regularity equations no longer exhaust the possibilities.
* **Cyclic-orbit quotients need not be vertex-transitive.** The cyclic subgroup used in Theorem 1 need not be normal, so induction on its quotient is not justified.
* **Normal-orbit lifting requires traceable fibers.** Normal orbits can induce disconnected, even edgeless, subgraphs.

Thus the arguments establish the stated infinite special case and a minimum-counterexample restriction, but do not resolve the full Lovász Hamiltonian-path problem.