```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for the substitution-and-clique-sum closure of triangle-free graphs, and no polynomial degree in κ independent of ℓ can suffice in general.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; the upper bound uses the quoted triangle-free theorem, and no novelty is claimed for these partial results."
}
```

## 1. Statements of the partial results

Graphs are finite and simple. A **hole** is an induced cycle of length at least four.

I do not obtain a proof or counterexample for arbitrary bounded-clique graphs. The following restricted extension and quantitative lower bounds can, however, be proved rigorously.

For each integer \(\ell\ge1\), let \(b_\ell\ge2\) be an integer such that
\[
H\text{ triangle-free and containing no holes of }\ell
\text{ consecutive lengths}
\quad\Longrightarrow\quad
\chi(H)\le b_\ell.
\tag{1}
\]
Such an integer exists by the triangle-free theorem quoted in the question. Put
\[
d_\ell=\left\lceil\log_2 b_\ell\right\rceil.
\]

Recall two operations.

* **Substitution:** Given a graph \(H\) and nonempty graphs \(F_v\), \(v\in V(H)\), replace each \(v\) by \(F_v\), making \(F_u\) complete to \(F_v\) precisely when \(uv\in E(H)\).
* **Clique-sum:** Identify a clique of one graph with an equally sized clique of another, adding no edges between vertices outside the identified clique. The common clique may be empty.

Let \(\mathcal C\) be the smallest class containing all triangle-free graphs and closed under substitution and clique-sums.

### Theorem A — a restricted extension
If \(G\in\mathcal C\) contains no holes of \(\ell\) consecutive lengths, then
\[
\boxed{\chi(G)\le \omega(G)^{d_\ell}.}
\tag{2}
\]
Consequently, the conjecture holds within \(\mathcal C\), with
\[
c(\kappa,\ell)=(\kappa-1)^{d_\ell}
\qquad(\kappa\ge2,\ \ell\ge1).
\]

The class includes iterated lexicographic products and clique blow-ups of triangle-free graphs, as well as graphs assembled from these by clique-sums.

### Theorem B — necessary growth of a threshold
Any thresholds satisfying the original conjecture must satisfy
\[
\boxed{c(2^t+1,\ell)\ge (5/2)^t}
\qquad(t\ge1,\ \ell\ge3).
\tag{3}
\]
More generally, there is no absolute exponent \(D\) and finite-valued function \(A(\ell)\) for which
\[
c(\kappa,\ell)\le A(\ell)\kappa^D
\tag{4}
\]
can hold for all parameters.

In fact, an elementary probabilistic construction gives the following necessary condition: if, for a fixed sufficiently large \(\ell\),
\[
c(\kappa,\ell)\le A_\ell\kappa^{D_\ell},
\]
then
\[
\boxed{
D_\ell\ge
\frac13\log_2(\ell+2)
-\log_2\!\ln(\ell+2)-3.
}
\tag{5}
\]

The proofs follow.

---

## 2. A weighted coloring lemma

For positive integer demands \(q_v\), let \(\chi(H;\mathbf q)\) denote the minimum size of a palette from which each vertex \(v\) can receive \(q_v\) colors, with adjacent vertices receiving disjoint sets.

For positive integer weights \(w_v\), define
\[
W(H;\mathbf w)
=\max\left\{\sum_{v\in Q}w_v:Q\text{ is a clique of }H\right\}.
\]

### Lemma 1
Suppose \(\chi(H)\le b\), and \(d\ge1\) is an integer with \(2^d\ge b\). Then
\[
\chi(H;\mathbf w^d)\le W(H;\mathbf w)^d,
\tag{6}
\]
where \(\mathbf w^d\) denotes the demands \(w_v^d\).

### Proof

The empty graph is immediate. Write
\[
r=W(H;\mathbf w),\qquad h=\lfloor r/2\rfloor,
\]
and fix a proper coloring \(\varphi:V(H)\to\{1,\ldots,b\}\). We have
\[
w_v\le r,\qquad w_u+w_v\le r\quad\text{when }uv\in E(H).
\tag{7}
\]

Construct mutually disjoint palettes:

* for \(0\le t<h\) and \(1\le j\le b\), a palette \(P_{t,j}\) of size
  \[
  (t+1)^d-t^d;
  \]
* one extra palette \(P_*\) of size
  \[
  r^d-bh^d.
  \]

The latter size is nonnegative because \(b\le2^d\) and \(h\le r/2\). The total number of colors is \(r^d\).

At level \(t\), make the following colors available to \(v\):
\[
\begin{cases}
\varnothing, & w_v\le t,\\[2mm]
P_{t,\varphi(v)}, & t<w_v<r-t,\\[2mm]
\displaystyle\bigcup_{j=1}^bP_{t,j}, & w_v\ge r-t.
\end{cases}
\tag{8}
\]
Also make \(P_*\) available to every vertex of weight greater than \(h\).

These availability sets are disjoint on adjacent vertices. Indeed:

* if \(w_v\ge r-t\), every neighbor of \(v\) has weight at most \(t\), by (7);
* otherwise adjacent vertices receiving colors at level \(t\) receive different palettes according to \(\varphi\);
* vertices of weight greater than \(h\) form a stable set.

It remains to check the demands.

If \(w_v\le h\), the number of available colors is exactly
\[
\sum_{t=0}^{w_v-1}\big((t+1)^d-t^d\big)=w_v^d.
\]

If \(w_v>h\), put \(s=r-w_v\), so \(0\le s\le h\). The number available is
\[
s^d+b(h^d-s^d)+(r^d-bh^d)
=r^d-(b-1)s^d.
\]
This is at least \((r-s)^d=w_v^d\). To see this, the function
\[
f(x)=(r-x)^d+(b-1)x^d
\]
is convex on \([0,r/2]\), and
\[
f(0)=r^d,\qquad
f(r/2)=b(r/2)^d\le r^d.
\]
Thus \(f(s)\le r^d\).

Choose any \(w_v^d\) available colors at each vertex. This proves (6). \(\square\)

---

## 3. Preservation under substitution and clique-sums

Say that a graph \(F\) has property \(P_d\) if
\[
\chi(F;\mathbf w^d)\le W(F;\mathbf w)^d
\tag{9}
\]
for every assignment of positive integer weights.

### Lemma 2
Property \(P_d\) is preserved under substitution and clique-sums.

### Proof: substitution

Let
\[
F=H(F_v:v\in V(H)),
\]
where \(H\) and all the \(F_v\) have \(P_d\). Give the vertices of \(F\) weights \(w_x\), and set
\[
r_v=W(F_v;\mathbf w),\qquad r=W(F;\mathbf w).
\]
A clique in \(F\) projects to a clique in \(H\), and conversely maximum weighted cliques in modules corresponding to a clique of \(H\) can be combined. Hence
\[
r=\max_{Q\text{ clique in }H}\sum_{v\in Q}r_v.
\tag{10}
\]

Property \(P_d\) for \(H\) supplies sets of \(r_v^d\) colors from a common palette of size \(r^d\), disjoint for adjacent vertices of \(H\). Property \(P_d\) for \(F_v\) allows its demands \(w_x^d\) to be colored using its assigned set of \(r_v^d\) colors. These colorings combine to establish \(P_d\) for \(F\).

### Proof: clique-sums

Suppose \(F=F_1\cup F_2\), where \(F_1\cap F_2\) is a clique and there are no edges between the exclusive parts.

For any weights, both pieces admit the required weighted coloring from a palette of size \(W(F;\mathbf w)^d\). On the common clique, the color sets are pairwise disjoint, and each common vertex has the same prescribed number of colors in both colorings. A permutation of the palette in one piece therefore makes the two colorings agree on every common vertex.

The colorings then combine. \(\square\)

### Proof of Theorem A

Fix a finite construction of \(G\in\mathcal C\).

Every operand in this construction is isomorphic to an induced subgraph of \(G\). For substitution, the modules are induced subgraphs, and the quotient is realized by choosing one representative from each module. For clique-sums, both pieces remain induced subgraphs. Applying these observations recursively proves the assertion for all construction stages.

The property of containing no holes of \(\ell\) consecutive lengths is hereditary. Thus every triangle-free starting graph in the construction satisfies (1), and has chromatic number at most \(b_\ell\). Lemma 1 gives \(P_{d_\ell}\) for every such starting graph. Lemma 2 propagates that property through the construction.

Finally, setting all weights equal to one gives
\[
\chi(G)\le\omega(G)^{d_\ell}.
\]
This proves Theorem A. \(\square\)

---

## 4. Hole lengths under substitution

The lower bounds use a useful exact observation about long holes.

### Lemma 3
Let \(F=H(F_v:v\in V(H))\), with every module nonempty. Every hole of length at least five in \(F\) either:

1. lies inside one module \(F_v\); or
2. uses exactly one vertex from each of several modules and projects to a hole of the same length in \(H\).

Thus substitution introduces no new hole lengths greater than four.

### Proof

If an induced cycle \(C\) meets a module in a proper nonempty subset \(S\) of its vertices, then \(S\) is a module of the cycle: every vertex of \(C\setminus S\) is either complete or anticomplete to \(S\).

A cycle of length at least five has no proper module of size at least two. Indeed, an outside vertex adjacent to such a module would be adjacent to all its vertices, so the module has size two. Those two vertices cannot be adjacent, and must have the same two neighbors. This forces the entire cycle to have length four.

Consequently, a hole of length at least five that crosses modules uses at most one vertex from each. Its projection is then an induced cycle of the same length in \(H\). \(\square\)

---

## 5. Explicit lower bounds

Let \(H\) be a triangle-free graph on \(N\ge5\) vertices containing an edge, and write
\[
a=\alpha(H).
\]
Define its lexicographic powers by
\[
G_1=H,\qquad
G_{t+1}=H(G_t,\ldots,G_t).
\]

Projecting cliques and stable sets to the outer copy of \(H\) gives
\[
|V(G_t)|=N^t,\qquad
\omega(G_t)=2^t,\qquad
\alpha(G_t)=a^t.
\tag{11}
\]
Therefore
\[
\chi(G_t)\ge\frac{|V(G_t)|}{\alpha(G_t)}
=\left(\frac Na\right)^t.
\tag{12}
\]

By Lemma 3, every hole of \(G_t\) has length at most \(N\). Consequently, whenever
\[
N\le\ell+2,
\tag{13}
\]
\(G_t\) cannot contain holes of \(\ell\) consecutive lengths: any such run starts at least at four and ends at least at \(\ell+3>N\).

Since \(G_t\) has no \(K_{2^t+1}\), every admissible threshold satisfies
\[
c(2^t+1,\ell)\ge \left(\frac Na\right)^t.
\tag{14}
\]

### 5.1 The five-cycle

Take \(H=C_5\). Then \(N=5\), \(a=2\), and every hole in its lexicographic powers has length four or five. Thus, for every \(\ell\ge3\),
\[
c(2^t+1,\ell)\ge (5/2)^t.
\]

In particular, along \(\kappa=2^t+1\),
\[
c(\kappa,3)\ge
(\kappa-1)^{\log_2(5/2)}.
\tag{15}
\]
So even for three consecutive lengths, a linear dependence on the forbidden clique size is impossible.

### 5.2 The necessary degree grows with \(\ell\)

Here is a self-contained construction of triangle-free graphs with large \(N/\alpha\).

For a sufficiently large integer \(M\), take
\[
J\sim G(M,p),\qquad p=M^{-2/3},
\]
and put
\[
s=\left\lceil3M^{2/3}\ln M\right\rceil.
\]

The expected number \(T\) of triangles satisfies
\[
\mathbb E T=\binom M3p^3\le M/6.
\]
Hence
\[
\Pr(T>M/2)\le1/3.
\tag{16}
\]

Also,
\[
\begin{aligned}
\Pr(\alpha(J)\ge s)
&\le \binom Ms(1-p)^{\binom s2}\\
&\le
\exp\left(s\ln M-\frac{p\,s(s-1)}2\right)
=o(1).
\end{aligned}
\tag{17}
\]
Thus there exists \(J\) with at most \(M/2\) triangles and independence number less than \(s\).

Delete one chosen vertex from each triangle, taking the union of these choices. At most \(M/2\) vertices are deleted, and the resulting graph \(H\) is triangle-free. It satisfies
\[
M/2\le N:=|V(H)|\le M,\qquad \alpha(H)<s.
\]
For sufficiently large \(M\), \(s\le4M^{2/3}\ln M\), so
\[
\frac{N}{\alpha(H)}
\ge \frac{M^{1/3}}{8\ln M}.
\tag{18}
\]

Now take \(M=\ell+2\). Equations (13)–(14) give, for every sufficiently large \(\ell\) and every \(t\ge1\),
\[
c(2^t+1,\ell)
\ge
\left(
\frac{(\ell+2)^{1/3}}{8\ln(\ell+2)}
\right)^t.
\tag{19}
\]

If \(c(\kappa,\ell)\le A_\ell\kappa^{D_\ell}\), taking logarithms in (19), dividing by \(t\), and letting \(t\to\infty\) yields
\[
D_\ell\ge
\frac13\log_2(\ell+2)
-\log_2\!\ln(\ell+2)-3.
\]
This proves (5), and in particular rules out an exponent independent of \(\ell\). \(\square\)

---

## 6. What remains unresolved

The upper-bound argument only propagates a chromatic bound through substitution and clique-sums. For a general bounded-clique graph, a quotient or indecomposable piece can contain triangles, and the quoted triangle-free theorem then supplies no chromatic bound for that piece. No argument overcoming this obstruction is provided here.

The lower-bound examples are **not counterexamples** to the conjecture: their clique numbers grow as \(2^t\). They constrain the dependence on \(\kappa\), rather than producing unbounded chromatic number at a fixed clique bound.

Thus these results give a proved structural special case and necessary quantitative growth, but do not settle the unrestricted conjecture—even the general \(K_4\)-free, three-consecutive-lengths case.