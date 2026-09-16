```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact rounding argument handles fractional covers with at most seven terms, and eight terms when every coefficient is at most one half.",
  "would_publish": false,
  "caveats": "No novelty claim; the general conjecture and the exceptional eight-term case are not settled here."
}
```

# Partial result: rounding sparse fractional covers

I do not obtain a proof or counterexample for arbitrary bridgeless cubic graphs. The result below is a precise rounding theorem, with unconditional special-case consequences:

- Berge–Fulkerson holds whenever the uniform fractional perfect-matching cover has a representation using at most seven perfect matchings.
- It also holds for an eight-term representation whose coefficients are all at most \(1/2\).
- Consequently, it holds for every bridgeless cubic graph with at most seven distinct perfect matchings, and for every bridgeless cubic graph on at most twelve vertices.

These special cases are not asserted to be new. The argument also identifies exactly which coefficient pattern escapes the eight-term rounding method.

Throughout, graphs are finite and loopless; parallel edges are permitted. Repetitions in the desired list of perfect matchings are permitted. The empty graph is trivial.

## 1. Fractional covers and normalization

Write \(\chi^M\) for the incidence vector of a perfect matching \(M\), and \(\mathbf 1\) for the all-one edge vector.

A **fractional uniform cover** is an identity
\[
\sum_{i=1}^{t} a_i\chi^{M_i}=\mathbf 1,
\qquad a_i>0.
\tag{1}
\]
In an \(r\)-regular graph, summing over the edges incident with any vertex gives
\[
\sum_{i=1}^{t}a_i=r.
\tag{2}
\]

For a cubic graph, Berge–Fulkerson asks for six perfect matchings satisfying
\[
\sum_{j=1}^{6}\chi^{N_j}=2\mathbf 1.
\tag{3}
\]

The distinction between (1) and (3) is precisely the rounding issue.

## 2. A balanced sparse-cover rounding theorem

The main lemma works for general regular graphs.

**Theorem 1.**  
Let \(G\) be an \(r\)-regular graph admitting (1), where
\[
t\le 2r+2
\quad\text{and}\quad
a_i\le \frac12\quad\text{for every }i.
\]
Then \(G\) has \(2r\) perfect matchings covering each edge exactly twice.

**Proof.** Define the unweighted multiplicity
\[
\mu(e)=\bigl|\{i:e\in M_i\}\bigr|.
\]
Since the coefficients on every edge sum to \(1\), and every coefficient is at most \(1/2\), we have
\[
\mu(e)\ge 2.
\tag{4}
\]
Also, at every vertex \(v\),
\[
\sum_{e\ni v}\mu(e)=t.
\]

If \(t=2r\), (4) forces \(\mu(e)=2\) for every edge, so the listed matchings already give the desired cover.

It remains to consider \(t=2r+1\) or \(2r+2\). Construct a multigraph \(D\) by retaining \(\mu(e)-2\) copies of each original edge \(e\). It is regular of degree
\[
s=t-2r\in\{1,2\}.
\]
Its multiplicity vector satisfies
\[
d:=\mu-2\mathbf 1
   =\sum_{i=1}^{t}(1-2a_i)\chi^{M_i}.
\tag{5}
\]
All coefficients on the right are nonnegative, and their sum is \(s>0\). Thus some \(M_i\) has \(1-2a_i>0\); every edge of that matching belongs to the support of \(D\). Choosing a copy of each such edge gives a perfect matching of \(D\).

Therefore \(D\) is bipartite:

- if \(s=1\), it is a disjoint union of single edges;
- if \(s=2\), it is a disjoint union of cycles, and the existence of a perfect matching forces every component cycle to be even.

Now let
\[
I=\{i:a_i=1/2\},\qquad q=|I|,
\]
and construct another multigraph \(R\), with edge multiplicities
\[
\rho(e)=2-\sum_{i\in I}\chi^{M_i}(e).
\tag{6}
\]
These multiplicities are nonnegative: three coefficient-\(1/2\) terms cannot contain the same edge. Moreover, \(R\) is \((2r-q)\)-regular.

If \(d(e)=0\), equation (5) shows that every listed matching containing \(e\) has coefficient \(1/2\). Since \(\mu(e)=2\), equation (6) gives \(\rho(e)=0\). Hence
\[
\operatorname{supp}(R)\subseteq \operatorname{supp}(D),
\]
so \(R\) is bipartite.

Every \(k\)-regular bipartite multigraph decomposes into \(k\) perfect matchings. Indeed, for \(k>0\), the degree count
\[
k|S|\le k|N(S)|
\]
verifies Hall’s condition; remove a perfect matching and proceed inductively. Apply this with \(k=2r-q\), with the degree-zero case requiring no matchings.

Take these \(2r-q\) perfect matchings of \(R\), viewed as perfect matchings of \(G\), together with the \(q\) matchings indexed by \(I\). Their total multiplicity on each original edge is
\[
\rho(e)+\sum_{i\in I}\chi^{M_i}(e)=2.
\]
There are exactly \(2r\) matchings. \(\square\)

For cubic graphs, this proves the claimed eight-term result under the coefficient bound \(a_i\le 1/2\).

## 3. Removing the coefficient bound for seven terms

**Theorem 2.**  
If a cubic graph admits a fractional uniform cover using at most seven terms, then it satisfies Berge–Fulkerson.

**Proof.** First suppose two listed perfect matchings \(M_i,M_j\) are edge-disjoint. Since \(G\) is cubic,
\[
E(G)\setminus(M_i\cup M_j)
\]
is a third perfect matching. Taking these three matchings twice proves the assertion.

We may therefore assume that every two listed perfect matchings intersect.

Every coefficient is then strictly less than \(1\). Indeed, an \(a_i=1\) would force every other listed matching to avoid every edge of \(M_i\), contrary to pairwise intersection. Consequently every edge belongs to at least two listed matchings:
\[
\mu(e)\ge 2.
\tag{7}
\]

If all coefficients are at most \(1/2\), Theorem 1 applies.

Otherwise let \(a_0>1/2\). Since every \(M_j\), \(j\ne0\), intersects \(M_0\), the edge equation at an intersection gives
\[
a_j\le 1-a_0<\frac12.
\tag{8}
\]
At any vertex, the edge belonging to \(M_0\) has multiplicity at least two by (7). Each of the other two edges must have multiplicity at least three, because its coefficients are all strictly below \(1/2\) and sum to \(1\). Thus
\[
t=\sum_{e\ni v}\mu(e)\ge 2+3+3=8,
\]
contradicting \(t\le7\). \(\square\)

### The exact eight-term configuration left over

The same argument yields a useful structural restriction.

Suppose \(t\le8\), the listed matchings are pairwise intersecting, and some coefficient \(a_0>1/2\). Then necessarily \(t=8\), with
\[
\mu(e)=
\begin{cases}
2,&e\in M_0,\\
3,&e\notin M_0.
\end{cases}
\tag{9}
\]
Every other \(M_j\) intersects \(M_0\), and an intersection edge belongs to exactly those two listed matchings. Therefore
\[
a_j=1-a_0\qquad(j=1,\ldots,7).
\]
Using \(\sum_i a_i=3\),
\[
a_0+7(1-a_0)=3,
\]
so
\[
a_0=\frac23,\qquad
a_1=\cdots=a_7=\frac13.
\tag{10}
\]
Equivalently,
\[
2\chi^{M_0}+\sum_{j=1}^{7}\chi^{M_j}=3\mathbf1.
\tag{11}
\]

Thus the only eight-term case not handled by this method is a very specific threefold cover: \(M_0\) occurs twice and seven other matchings occur once. This is **not** a counterexample to Berge–Fulkerson; it is a limitation of the rounding argument.

## 4. Unconditional special cases

### 4.1 Graphs with at most seven perfect matchings

**Corollary 3.**  
Every bridgeless cubic graph having at most seven distinct perfect matchings satisfies Berge–Fulkerson.

**Proof.** Use Edmonds’ perfect matching polytope theorem, as cited in the question.

The vector \(x_e=1/3\) satisfies every vertex equation. If \(S\) is odd, then
\[
|\delta(S)|\equiv |S|\pmod 2.
\]
Thus \(|\delta(S)|\) is odd. It cannot be one because the graph is bridgeless, so \(|\delta(S)|\ge3\). Consequently
\[
x(\delta(S))\ge1.
\]
Hence \(x\) belongs to the perfect matching polytope.

Writing \(x\) as a convex combination of perfect matchings and multiplying by three gives (1). If there are at most seven distinct perfect matchings in the graph, this representation uses at most seven terms after zero coefficients are discarded. Apply Theorem 2. \(\square\)

### 4.2 Graphs of order at most twelve

More generally, Theorem 2 applies whenever the perfect matching polytope has affine dimension at most six, by Carathéodory’s theorem.

**Corollary 4.**  
Every bridgeless cubic graph on at most twelve vertices satisfies Berge–Fulkerson.

**Proof.** First suppose \(G\) is connected, with \(n\) vertices.

If \(G\) is bipartite, its edges decompose into three perfect matchings, so the conclusion is immediate.

Suppose \(G\) is nonbipartite. Let \(B\) be its unsigned vertex-edge incidence matrix. Then
\[
\operatorname{rank}B=n.
\]
To see this, a row dependence gives numbers \(z_v\) satisfying \(z_u+z_v=0\) on every edge. Connectedness propagates these values with alternating signs, and an odd cycle forces every value to be zero.

All perfect matching vectors lie in the affine space
\[
Bx=\mathbf1_V.
\]
Since \(G\) has \(3n/2\) edges, this space has dimension
\[
\frac{3n}{2}-n=\frac n2.
\]
Edmonds’ theorem places the vector \(x_e=1/3\) in the perfect matching polytope. Carathéodory’s theorem therefore represents it using at most
\[
\frac n2+1\le7
\]
perfect matchings. Apply Theorem 2 after multiplying the coefficients by three.

For disconnected \(G\), apply the connected result to each component and take componentwise unions of the six matchings. \(\square\)

## 5. Additional restriction on the unrounded eight-term case

Equation (11) constrains the odd cycles of \(G-M_0\).

Let \(C\) be an odd cycle component of that 2-factor. Every edge leaving \(V(C)\) belongs to \(M_0\). By (9), each such edge belongs to exactly one of \(M_1,\ldots,M_7\). But each perfect matching meets an odd cut in an odd, positive number of edges. Hence
\[
|\delta(V(C))|
 =\sum_{j=1}^{7}|M_j\cap\delta(V(C))|
 \ge7.
\]
In particular,
\[
|C|\ge7.
\tag{12}
\]

If \(G-M_0\) has only even cycles, then \(M_0\), together with alternating matchings on those cycles, gives a 3-edge-coloring. Otherwise, because \(G\) has even order, its 2-factor has at least two odd components. Thus a genuinely unresolved instance of the eight-term configuration must have at least fourteen vertices, and all its odd \(G-M_0\) components have length at least seven.

## 6. Where the argument stops

The gap to the full conjecture is substantial and explicit.

1. **Edmonds’ theorem does not supply bounded support.**  
   The dimension argument above gives a number of terms growing with the graph’s order, not a bound of seven or eight.

2. **Splitting large coefficients does not fix this.**  
   Repeating a matching can make every coefficient at most \(1/2\), but may increase the number of terms beyond eight.

3. **The key bipartiteness step stops at surplus degree two.**  
   In Theorem 1, the auxiliary graph \(D\) has degree \(t-6\) in the cubic case. For nine or more terms, that degree may be at least three. Having a perfect matching then no longer forces \(D\) to be bipartite, so the final factorization argument fails.

Accordingly, the full Berge–Fulkerson conjecture is neither proved nor disproved here. What is proved is an exact sparse-cover rounding theorem, its stated special-case consequences, and the precise arithmetic form of the first case that this method does not round.