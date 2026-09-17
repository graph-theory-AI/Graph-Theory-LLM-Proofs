```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Recognition lies in coNP, and a 6α−2 obstruction bound gives polynomial recognition at every fixed independence number.",
  "would_publish": false,
  "caveats": "Unrestricted polynomial-time recognition and hardness remain unresolved here; the novelty of these partial results has not been checked."
}
```

# A polynomial certificate and recognition at bounded independence number

I do not resolve the unrestricted recognition problem. I establish three partial results:

1. **Switchable recognition belongs to coNP.**
2. Every minimal forbidden induced subgraph \(H\) satisfies
   \[
   |V(H)|\le 6\alpha(H)-2,
   \]
   where \(\alpha(H)\) is its independence number. Consequently, recognition is polynomial-time on graphs of independence number at most \(r\), for each fixed \(r\).
3. For \(\alpha(G)\le2\), the bound improves to **six vertices**: testing all six-vertex induced subgraphs suffices, giving an \(O(n^6)\) algorithm.

The argument is self-contained and does not assume the previous attempt’s subclass equivalences. In particular, its PSPACE upper bound can be strengthened to coNP.

## 1. Definitions

Graphs are finite, simple, and undirected. For a graph \(H\), let \(\mathcal R(H)\) be the graph whose vertices are the perfect matchings of \(H\), where two matchings are adjacent if their symmetric difference is a cycle of length four.

I use the hereditary definition in the question:

> \(G\) is **Switchable** if, for every induced subgraph \(H\) of \(G\), every two perfect matchings of \(H\) are connected in \(\mathcal R(H)\).

The condition is vacuous when \(H\) has no perfect matching or only one.

A **minimal obstruction** is a graph that is not Switchable but whose proper induced subgraphs are Switchable. Such a graph \(H\) has disconnected \(\mathcal R(H)\): otherwise any failure would occur in a proper induced subgraph. Also, \(|V(H)|\) is even and at least six, since any two distinct perfect matchings on four vertices differ by one flip.

# 2. Replacing flips by edge-sharing on a minimal obstruction

For an even-order graph \(H\), define an auxiliary graph \(\Gamma(H)\).

- Its vertices are the **allowed edges** of \(H\), meaning edges belonging to at least one perfect matching.
- Two distinct allowed edges are adjacent in \(\Gamma(H)\) if some perfect matching contains both.

Every perfect matching induces a clique in \(\Gamma(H)\), so all its edges belong to a single component of \(\Gamma(H)\).

### Lemma 2.1 — Components of the auxiliary graph

Two perfect matchings have their edges in the same component of \(\Gamma(H)\) if and only if they can be joined by a sequence of perfect matchings in which consecutive matchings share an edge.

#### Proof

One direction is immediate: matchings sharing an edge belong to the same auxiliary component.

Conversely, suppose an edge of \(M\) and an edge of \(N\) are joined by an auxiliary path
\[
e_0,e_1,\ldots,e_s.
\]
For each \(i<s\), choose a perfect matching \(P_i\) containing \(e_i,e_{i+1}\). Then
\[
M,P_0,P_1,\ldots,P_{s-1},N
\]
is an edge-sharing sequence. ∎

### Lemma 2.2 — A hereditary auxiliary criterion

A graph \(G\) is Switchable if and only if, for every even-order induced subgraph \(H\) with \(|V(H)|\ge6\), the graph \(\Gamma(H)\) has at most one component.

Here an empty auxiliary graph is permitted.

#### Proof

Write \(|V(H)|=2k\), where \(k\ge3\). A flip changes two matching edges, so its two endpoint matchings share \(k-2\ge1\) edges. Therefore a flip sequence cannot move between different components of \(\Gamma(H)\). Thus, if \(\Gamma(H)\) has at least two components, \(\mathcal R(H)\) is disconnected.

For the converse, suppose \(G\) is not Switchable, and choose an induced subgraph \(H\) of minimum order such that \(\mathcal R(H)\) is disconnected.

If perfect matchings \(P,Q\) of \(H\) share an edge \(uv\), their restrictions to \(H-\{u,v\}\) can be reconfigured, by minimality. Restoring the fixed edge \(uv\) gives a reconfiguration from \(P\) to \(Q\).

Consequently, any edge-sharing sequence of perfect matchings of \(H\) can be replaced by a flip sequence. By Lemma 2.1, connectivity of \(\Gamma(H)\) would imply connectivity of \(\mathcal R(H)\), a contradiction. ∎

The restriction to at least six vertices is essential: on four vertices, a flip need not preserve any matching edge.

## 2.1. Consequence: recognition is in coNP

The graph \(\Gamma(H)\) is computable in polynomial time using general-graph perfect-matching tests:

- An edge \(uv\) is allowed exactly when \(H-\{u,v\}\) has a perfect matching.
- Two vertex-disjoint edges \(uv,xy\) can coexist exactly when
  \[
  H-\{u,v,x,y\}
  \]
  has a perfect matching.

There are at most \(|E(H)|^2\) such pair tests.

Thus a certificate that \(G\) is not Switchable is simply a vertex set \(S\) such that

- \(|S|\) is even and at least six; and
- \(\Gamma(G[S])\) has at least two components.

This certificate is polynomially verifiable. Lemma 2.2 guarantees that a certificate exists for every non-Switchable graph.

> **Theorem 2.3.** Switchable recognition belongs to coNP.

This does **not** justify testing only \(\Gamma(G)\). For example, \(G=C_6\dot\cup K_2\) has connected \(\Gamma(G)\), since every perfect matching contains the \(K_2\)-edge. Nevertheless, \(\mathcal R(G)\) is disconnected.

# 3. Structure forced by a disconnected auxiliary graph

The next arguments apply to any graph \(H\) of even order at least six for which \(\Gamma(H)\) is disconnected; minimality is not needed.

Choose perfect matchings \(M,N\) belonging to different auxiliary components.

No perfect matching can contain both an edge of \(M\) and an edge of \(N\). Moreover, \(M,N\) share no edge.

Their union must be a single Hamiltonian cycle. Otherwise, switching from \(M\) to \(N\) on just one component of \(M\triangle N\) would produce a perfect matching containing edges from both.

We may therefore write
\[
C=a_0b_0a_1b_1\cdots a_{k-1}b_{k-1}a_0,
\qquad k\ge3,
\]
with
\[
M=\{a_ib_i:0\le i<k\},
\qquad
N=\{b_ia_{i+1}:0\le i<k\},
\]
where indices are modulo \(k\). Set
\[
A=\{a_0,\ldots,a_{k-1}\},\qquad
B=\{b_0,\ldots,b_{k-1}\}.
\]

### Lemma 3.1 — No splitting chord

Every \(A\)-\(B\) edge of \(H\) belongs to \(C\).

#### Proof

Suppose a non-rim edge joins opposite parities of \(C\). Its endpoints divide the rim into two odd-length paths, each of length at least three.

Use this chord, and match the internal vertices of both paths along the rim. The resulting perfect matching contains at least one edge of \(M\) and at least one edge of \(N\), which is impossible. ∎

Hence every non-rim edge lies entirely in \(A\) or entirely in \(B\).

Draw \(C\) on a circle. An \(A\)-chord and a \(B\)-chord **cross** if their four endpoints alternate around the circle.

### Lemma 3.2 — Bichromatic crossings form a matching

Every \(A\)-chord crosses at most one \(B\)-chord, and every \(B\)-chord crosses at most one \(A\)-chord.

#### Proof

Fix a \(B\)-chord
\[
f=b_i b_j
\]
and an \(A\)-chord \(e\) crossing it.

The four endpoints of \(e,f\) alternate in parity around the rim. Deleting these endpoints leaves four rim paths, each with an even number of vertices. Match these paths along the rim and add \(e,f\). This gives a perfect matching \(P(e,f)\).

Its remaining \(k-2\ge1\) edges are rim edges. They cannot include both \(M\)-edges and \(N\)-edges.

- If all are \(M\)-edges, the four deleted vertices must be the endpoints of two edges of \(M\). Thus
  \[
  e=a_i a_j.
  \]
  Moreover, \(f\) belongs to the auxiliary component of \(M\).

- If all are \(N\)-edges, similarly
  \[
  e=a_{i+1}a_{j+1},
  \]
  and \(f\) belongs to the auxiliary component of \(N\).

For fixed \(f\), each case permits at most one \(A\)-chord. Both cases cannot occur, since they would put \(f\) in the components of both \(M\) and \(N\).

Thus \(f\) crosses at most one \(A\)-chord. The other assertion follows symmetrically. ∎

These are necessary conditions, not a claimed complete structural characterization.

# 4. A linear obstruction bound in the independence number

We now prove the main quantitative result.

> **Theorem 4.1.** If \(|V(H)|\ge6\) and \(\Gamma(H)\) has at least two components, then
> \[
> |V(H)|\le 6\alpha(H)-2.
> \]

Continue with the Hamiltonian cycle and its parity classes from Section 3. Write
\[
F_A=H[A],\qquad F_B=H[B],
\]
and let \(c_A,c_B\) be their numbers of connected components, including isolated vertices.

Let \(t\) be the number of crossing pairs consisting of one \(A\)-chord and one \(B\)-chord. By Lemma 3.2, these pairs use \(t\) distinct edges from each chord family.

## 4.1. Every crossed chord is a bridge

Suppose \(e\in E(F_A)\) crosses \(f\in E(F_B)\). One of the circular arcs between the endpoints of \(f\) determines a nonempty proper subset \(S\subset A\).

An \(A\)-edge crosses \(f\) precisely when it has one endpoint in \(S\) and one in \(A\setminus S\). By Lemma 3.2,
\[
\delta_{F_A}(S)=\{e\}.
\]
Therefore \(e\) is a bridge of \(F_A\).

Symmetrically, every crossed edge of \(F_B\) is a bridge.

## 4.2. A circular component inequality

We need
\[
\boxed{k+1\le c_A+c_B+t.} \tag{1}
\]

Here is a linear-algebra proof over \(\mathbb F_2\).

Let
\[
W=\left\{x\in\mathbb F_2^k:\sum_i x_i=0\right\},
\qquad
Q=\mathbb F_2^k/\langle\mathbf1\rangle.
\]
The dot product induces a nondegenerate pairing between \(W\) and \(Q\); both spaces have dimension \(k-1\).

For an \(A\)-edge \(e=a_pa_q\), let
\[
u_e=\mathbf e_p+\mathbf e_q\in W.
\]
The space \(U\) spanned by these vectors has dimension
\[
\dim U=k-c_A,
\]
by the usual incidence-rank formula.

For a \(B\)-edge \(f=b_i b_j\), let \(w_f\) be the indicator vector of the \(A\)-vertices on one circular arc from \(b_i\) to \(b_j\). Choosing the other arc adds \(\mathbf1\), so \([w_f]\in Q\) is well-defined.

The circular difference map
\[
D:Q\longrightarrow W,\qquad
(Dw)_i=w_i+w_{i+1},
\]
is an isomorphism and maps \([w_f]\) to \(\mathbf e_i+\mathbf e_j\). Hence the space \(V\) spanned by the \([w_f]\) has dimension
\[
\dim V=k-c_B.
\]

Furthermore,
\[
\langle u_e,[w_f]\rangle=
\begin{cases}
1,&e\text{ crosses }f,\\
0,&\text{otherwise}.
\end{cases}
\]
By Lemma 3.2, this matrix has exactly \(t\) nonzero entries, in distinct rows and columns. Its rank is therefore \(t\).

The rank of the pairing restricted to \(U\times V\) is at least
\[
\dim U+\dim V-(k-1).
\]
Consequently,
\[
t\ge(k-c_A)+(k-c_B)-(k-1)
  =k+1-c_A-c_B,
\]
proving (1).

## 4.3. Bounding the component counts

Set \(a=\alpha(H)\). Choosing one vertex from each component gives
\[
c_A\le a,\qquad c_B\le a. \tag{2}
\]

Delete the \(t\) crossed edges from \(F_A\). Since all are bridges, the resulting graph has \(c_A+t\) components.

Choose one vertex from each of these components. The graph induced by the selected vertices is a forest: all its edges come from the deleted bridges, whose quotient graph is a forest. It therefore has an independent set of size at least \((c_A+t)/2\). Thus
\[
c_A+t\le2a.
\]
Similarly,
\[
c_B+t\le2a. \tag{3}
\]

Combining (1)–(3), we obtain
\[
k+1\le c_A+c_B+t\le a+2a=3a.
\]
Since \(|V(H)|=2k\),
\[
|V(H)|\le6a-2.
\]
This proves Theorem 4.1. ∎

## 4.4. Minimal obstructions and recognition

By Lemma 2.2, every minimal obstruction \(H\) has disconnected \(\Gamma(H)\). Hence:

> **Corollary 4.2.** Every minimal obstruction to Switchability satisfies
> \[
> |V(H)|\le6\alpha(H)-2.
> \]
> In particular, every non-Switchable graph \(G\) contains a non-Switchable induced subgraph of order at most
> \[
> 6\alpha(G)-2.
> \]

This gives an exact recognition algorithm at bounded independence number.

### Algorithm for \(\alpha(G)\le r\)

Enumerate every even-order vertex set
\[
S\subseteq V(G),\qquad 6\le |S|\le6r-2.
\]
For each \(S\), construct \(\Gamma(G[S])\). Reject if it has at least two components; otherwise accept.

- Rejection is sound by Lemma 2.2.
- If \(G\) is not Switchable, Corollary 4.2 supplies a minimal obstruction among the enumerated sets.

For fixed \(r\), this takes
\[
f(r)n^{6r-2}
\]
time, with \(f(r)\) polynomially bounded using the auxiliary-graph construction. This is an **XP algorithm parameterized by independence number**, not an FPT algorithm.

The promise \(\alpha(G)\le r\), if needed, can itself be checked in polynomial time for fixed \(r\) by enumerating all \((r+1)\)-vertex sets.

# 5. Independence number at most two: six vertices suffice

The preceding bound can be sharpened substantially for \(r=2\).

> **Theorem 5.1.** If \(\alpha(G)\le2\), then \(G\) is Switchable if and only if \(\mathcal R(G[S])\) is connected, in the pairwise/vacuous sense, for every six-element set \(S\subseteq V(G)\).

#### Proof

Only sufficiency needs proof.

Suppose \(G\) is not Switchable, and choose a minimal obstruction \(H\). Use the Hamiltonian cycle
\[
a_0b_0a_1b_1\cdots a_{k-1}b_{k-1}a_0
\]
and distinct auxiliary components from Section 3.

Suppose \(k\ge4\). By Lemma 3.1, the combined \(B\)-neighborhood of \(a_i,a_{i+1}\) is exactly
\[
\{b_{i-1},b_i,b_{i+1}\}.
\]
Since \(k\ge4\), some \(B\)-vertex is adjacent to neither. Therefore, if \(a_i a_{i+1}\) were absent, these three vertices would form an independent set. As \(\alpha(H)\le2\), we must have
\[
a_i a_{i+1}\in E(H)
\quad\text{for every }i.
\]
Symmetrically,
\[
b_i b_{i+1}\in E(H)
\quad\text{for every }i.
\]

But the \(A\)-chord \(a_0a_1\) crosses both \(B\)-chords
\[
b_{k-1}b_0,\qquad b_0b_1.
\]
This contradicts Lemma 3.2.

Thus \(k=3\), and \(H\) has six vertices. ∎

### Explicit \(O(n^6)\) algorithm

For every six-element set \(S\):

1. Enumerate the \(15\) pair partitions of \(S\).
2. Retain those whose pairs are edges of \(G\).
3. Join two retained matchings if their symmetric difference is a four-cycle.
4. Test connectivity, accepting automatically when there are at most one retained matching.

Each test takes constant time, so the total is \(O(n^6)\).

This applies to **all** graphs of independence number at most two, not just co-bipartite graphs.

### Sharpness of the six-vertex bound

Take the cycle
\[
0123450
\]
and add the chords \(02\) and \(35\). This consists of two triangles, on \(\{0,1,2\}\) and \(\{3,4,5\}\), joined by the edges \(23\) and \(50\). Its independence number is two.

It has exactly two perfect matchings:
\[
\{01,23,45\},
\qquad
\{12,34,50\}.
\]
They differ on all six vertices and hence are not adjacent. Thus its reconfiguration graph is disconnected.

Every proper induced subgraph with a perfect matching has at most four vertices, so the graph is a minimal obstruction.

# 6. What remains unresolved

These arguments give a polynomial verifier for non-Switchability and exact recognition on every class of bounded independence number. They do not give unrestricted polynomial-time recognition.

The unresolved algorithmic step is:

> Find an induced vertex set \(S\) with disconnected \(\Gamma(G[S])\), without enumerating vertex subsets.

The obstruction bound does not settle this when \(\alpha(G)\) grows with \(n\). The necessary crossing restrictions in Section 3 are also not asserted to be sufficient.

Accordingly, I establish neither a polynomial-time recognition algorithm for arbitrary graphs nor a hardness result. I also make no novelty claim without a literature check.