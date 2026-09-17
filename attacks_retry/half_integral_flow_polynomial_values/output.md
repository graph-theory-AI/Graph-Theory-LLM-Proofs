```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sum-of-squares identity proves the conjecture for every bridgeless graph formed from two identical halves joined by at most six corresponding edges.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; no novelty or current-literature-status claim is made."
}
```

# Positivity from a bounded-interface reflection

I do not obtain a proof or counterexample for arbitrary bridgeless graphs. I establish a different restricted-class result, including cubic graphs of girth six and cycle rank greater than eight.

The arithmetic nonvanishing observation in the previous attempt is correct; I verify it below. The rest of this argument is independent of its cycle reductions and Heawood-polynomial calculation.

## 1. Statement of the partial result

Let \(H\) be a finite graph with \(k\) distinct labelled vertices, called **terminals**. Define its **vertex-double** \(D(H)\) by taking two copies of \(H\) and identifying corresponding terminals.

**Edges are not identified:** if both copies have an edge between the same two terminals, both edges are retained.

### Theorem

For every such \(H\),
\[
\Phi(D(H),q)\ge 0
\qquad\text{whenever }q>\max\{0,k-1\}.
\tag{1}
\]
If \(D(H)\) is bridgeless and \(q\) is a nonintegral rational number in this range, then
\[
\Phi(D(H),q)>0.
\tag{2}
\]

In particular, the conjectured positivity at \(q=11/2\) holds for every bridgeless vertex-double with at most six terminals.

There is a useful version involving an edge cut rather than shared vertices.

### Corollary: identical halves joined by at most six edges

Take two disjoint copies \(H^+\) and \(H^-\) of a connected graph \(H\). For specified vertices \(u_1,\ldots,u_k\) of \(H\), add the edges
\[
u_i^+u_i^-\qquad(1\le i\le k).
\]
If the resulting graph \(G\) is bridgeless and \(k\le 6\), then
\[
\boxed{\Phi(G,11/2)>0.}
\tag{3}
\]

There is no bound on the order, cycle rank, or genus of \(H\).

The theorem follows from an explicit sum-of-squares identity. Its proof also explains exactly why six terminals are accessible at \(11/2\).

---

## 2. Arithmetic nonvanishing

Allow loops and parallel edges, and write
\[
r(G)=|E(G)|-|V(G)|+c(G).
\]
The standard inclusion–exclusion formula is
\[
\Phi(G,q)=
\sum_{A\subseteq E(G)}
(-1)^{|E(G)|-|A|}
q^{\,|A|-|V(G)|+c(V(G),A)}.
\tag{4}
\]

If \(G\) is bridgeless, this is a monic integer polynomial of degree \(r(G)\). Indeed, deleting any edge of a bridgeless graph lowers the cycle rank by one, and subsequent deletions cannot increase it. Thus the term \(A=E(G)\) is the unique term of degree \(r(G)\).

Consequently,
\[
2^{r(G)}\Phi(G,11/2)\equiv 11^{r(G)}\equiv1\pmod2.
\tag{5}
\]
In particular,
\[
\boxed{\Phi(G,11/2)\ne0\quad\text{for every bridgeless }G.}
\tag{6}
\]

More generally, a monic integer polynomial cannot have a nonintegral rational root. Thus it suffices, for any particular class of bridgeless graphs, to prove **nonnegativity** at \(11/2\).

---

## 3. The sum-of-squares identity

### 3.1 A subset-generating polynomial

For a graph \(K\), define
\[
Z_K(q,v)=\sum_{A\subseteq E(K)}q^{c(V(K),A)}v^{|A|}.
\tag{7}
\]
Equation (4) gives, for \(q\ne0\),
\[
\Phi(K,q)=(-1)^{|E(K)|}q^{-|V(K)|}Z_K(q,-q).
\tag{8}
\]

Suppose \(H\) has \(n\) vertices and \(m\) edges, with terminal set \(W\), where \(|W|=k\). Its double has
\[
|V(D(H))|=2n-k,\qquad |E(D(H))|=2m.
\]
The sign in (8) therefore disappears:
\[
\Phi(D(H),q)=q^{-(2n-k)}Z_{D(H)}(q,-q).
\tag{9}
\]

### 3.2 Terminal partitions

Let \(\Pi_k\) denote the set of partitions of \(W\). Order partitions by refinement:
\[
\pi\le \sigma
\quad\Longleftrightarrow\quad
\text{every block of }\pi\text{ is contained in a block of }\sigma.
\]

For \(A\subseteq E(H)\), let:

- \(\pi(A)\in\Pi_k\) be the partition induced by connectivity in the spanning subgraph \((V(H),A)\);
- \(c_0(A)\) be the number of its components containing no terminal.

For \(\pi\in\Pi_k\), put
\[
a_\pi(q)=
\sum_{\substack{A\subseteq E(H)\\ \pi(A)=\pi}}
(-q)^{|A|}q^{c_0(A)}.
\tag{10}
\]

If edge subsets \(A\) and \(B\) are chosen in the two copies of \(H\), their union in the double has
\[
c_0(A)+c_0(B)+|\pi(A)\vee\pi(B)|
\]
components. Here \(\pi\vee\rho\) is the least common coarsening.

It follows that
\[
Z_{D(H)}(q,-q)
=
\sum_{\pi,\rho\in\Pi_k}
a_\pi(q)a_\rho(q)\,q^{|\pi\vee\rho|}.
\tag{11}
\]

### 3.3 Diagonalizing the partition matrix

Write
\[
(q)_j=q(q-1)\cdots(q-j+1),\qquad (q)_0=1.
\]

For every partition \(\tau\),
\[
q^{|\tau|}
=
\sum_{\substack{\sigma\in\Pi_k\\ \tau\le\sigma}}
(q)_{|\sigma|}.
\tag{12}
\]
For a positive integer \(q\), this counts assignments of colours to the blocks of \(\tau\), classified according to which blocks receive equal colours. It is therefore a polynomial identity.

Applying (12) to \(\tau=\pi\vee\rho\) in (11) gives
\[
Z_{D(H)}(q,-q)
=
\sum_{\sigma\in\Pi_k}
(q)_{|\sigma|}
\left(\sum_{\pi\le\sigma}a_\pi(q)\right)^2.
\tag{13}
\]

Combining (9), (10), and (13), we obtain the promised identity:
\[
\boxed{
\Phi(D(H),q)
=
q^{-(2n-k)}
\sum_{\sigma\in\Pi_k}
(q)_{|\sigma|}
\left[
\sum_{\substack{A\subseteq E(H)\\ \pi(A)\le\sigma}}
(-q)^{|A|}q^{c_0(A)}
\right]^2.
}
\tag{14}
\]

Every quantity here is explicitly defined by edge subsets of one half of the graph.

### 3.4 Positivity

If \(q>\max\{0,k-1\}\), then
\[
(q)_j>0\qquad(0\le j\le k).
\]
Also \(q^{-(2n-k)}>0\). Hence every summand in (14) is nonnegative, proving (1).

If \(D(H)\) is bridgeless and \(q\) is a nonintegral rational number, its flow polynomial cannot vanish there by Section 2. The nonnegative value is therefore strictly positive. This proves the theorem.

At the target value \(q=11/2\), all the weights are positive for \(k\le6\); in particular,
\[
(11/2)_6=\frac{10395}{64}>0.
\]

### 3.5 Proof of the edge-joining corollary

Subdivide each joining edge \(u_i^+u_i^-\) once, introducing a vertex \(w_i\).

The subdivided graph is the vertex-double of the graph obtained from \(H\) by adding \(k\) labelled leaves \(w_i\), with \(w_i\) adjacent to \(u_i\). Subdivision preserves the flow polynomial: conservation at a degree-two vertex uniquely equates the two edge values, after compatible orientations are chosen.

Thus the theorem with \(k\le6\) proves (3).

---

## 4. A cubic, girth-six example of cycle rank fifteen

Here is a fully specified example showing that the result is not merely a small-cycle-rank statement.

Let \(J\) be the incidence graph of the seven points
\[
0,1,\ldots,6
\]
and the seven triples
\[
012,\quad034,\quad056,\quad135,\quad146,\quad236,\quad245.
\tag{15}
\]
An edge joins a point to a triple containing it.

Each point belongs to three triples, and each pair of points belongs to exactly one triple. Thus \(J\) is cubic and bipartite, with no \(4\)-cycle.

Delete the three edges
\[
(0,056),\qquad(1,146),\qquad(3,236)
\tag{16}
\]
to obtain \(H\). Its six degree-two vertices are
\[
W=\{0,1,3,056,146,236\}.
\tag{17}
\]
They form an independent set in \(H\).

The graph \(H\) is connected. For example, the path
\[
0,\ 012,\ 1,\ 135,\ 5,\ 056,\ 6,\ 236,\ 2,\ 245,\ 4,\ 034,\ 3
\]
contains every vertex except \(146\), which is adjacent to \(4\) and \(6\).

Now take two copies of \(H\) and add one corresponding joining edge for each vertex of \(W\). Call the result \(G\).

### Basic properties

The graph \(G\) is simple, connected, and cubic, with
\[
|V(G)|=28,\qquad |E(G)|=42,\qquad r(G)=15.
\]

It is bipartite: reverse the bipartition in the second copy before adding the joining edges. A connected cubic bipartite graph has no bridge. Indeed, if a bridge separated a vertex set \(S\), the difference between the degree sums over the two bipartition classes within \(S\) would give
\[
3\bigl(|S\cap X|-|S\cap Y|\bigr)=\pm1,
\]
which is impossible.

Finally, \(G\) has girth at least six:

- a cycle contained in one copy of \(H\) has length at least six;
- a cycle using joining edges uses a positive even number of them;
- consecutive joining edges on that cycle are separated inside a copy of \(H\) by a path between distinct vertices of \(W\), hence by at least two edges.

A cycle of the second kind consequently has length at least six.

The corollary proves, without computing its degree-fifteen flow polynomial,
\[
\boxed{\Phi(G,11/2)>0.}
\tag{18}
\]

---

## 5. What prevents this from proving the full conjecture?

There are two precise limitations.

### Different halves give products, not squares

For two unrelated halves with the same terminal set, formula (14) has products of two different terminal-state expressions in place of squares. Their signs need not agree.

Thus the argument does not establish positivity merely because a graph has an edge cut of size at most six. The matching symmetry between its two halves is essential to this proof.

### At seven terminals, the partition matrix is no longer positive semidefinite

Let
\[
M_k(q)_{\pi,\rho}=q^{|\pi\vee\rho|}.
\]
The calculation above gives
\[
M_k(q)=T^{\mathsf T}
\operatorname{diag}\bigl((q)_{|\sigma|}:\sigma\in\Pi_k\bigr)T,
\tag{19}
\]
where
\[
T_{\sigma,\pi}=\mathbf1_{\{\pi\le\sigma\}}.
\]
The matrix \(T\) is invertible: in a linear ordering extending refinement, it is triangular with diagonal entries one.

For \(k=7\) and \(q=11/2\),
\[
(11/2)_7=-\frac{10395}{128}<0.
\]
Therefore \(M_7(11/2)\) is not positive semidefinite. There are real coefficient vectors \(a\) for which
\[
a^{\mathsf T}M_7(11/2)a<0.
\]

**This is not a graph counterexample.** The vectors arising from actual half-graphs through (10) are highly constrained; no half-graph realizing such a negative vector has been constructed here. It only shows that the unrestricted positive-semidefinite-matrix argument stops at six terminals.

## Conclusion

The sum-of-squares identity proves the conjectured sign for a symmetry-defined class of unbounded order and cycle rank, including high-girth cubic examples. It does not control asymmetric graphs or arbitrary larger interfaces. The general positivity assertion at \(11/2\) remains unresolved by this argument.