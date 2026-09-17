```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a self-contained deterministic exact 2^{O_k(n^{2/3}(log n)^{2/3})}-time algorithm, improving the supplied subexponential bound but not proving polynomial-time tractability.",
  "would_publish": false,
  "caveats": "The polynomial-time conjecture is not resolved here, and the novelty of these refinements has not been checked."
}
```

## 1. Interpretation and results

All graphs below are finite and simple. Write \(\operatorname{iocp}(G)\) for the maximum number of pairwise vertex-disjoint, pairwise anticomplete induced odd cycles. An **odd-cycle transversal** is a set \(S\) such that \(G-S\) is bipartite; its minimum size is denoted by \(\tau_{\mathrm{odd}}(G)\).

I interpret the conjecture as asking for a polynomial-time MIS algorithm for every fixed upper bound on \(\operatorname{iocp}\). I do not settle that conjecture.

The main partial result is the following constructive bound.

> **Theorem 1.** Let \(G\) have \(n\) vertices and \(m\) edges, with \(\operatorname{iocp}(G)\le k\), where \(1\le k\le n\). In polynomial time one can construct an odd-cycle transversal of size
> \[
> O\!\left(\min\left\{n,\sqrt{k(n+m)\log(n+2)}\right\}\right).
> \]
> Consequently, MIS can be solved exactly in deterministic time
> \[
> 2^{O(\sqrt{k(n+m)\log(n+2)})}n^{O(1)}.
> \]

Combining this with high-degree branching gives:

> **Theorem 2.** MIS on graphs with \(\operatorname{iocp}(G)\le k\) admits a deterministic exact algorithm running in time
> \[
> 2^{O\!\left(k^{1/3}n^{2/3}(\log(n+2))^{2/3}\right)}n^{O(1)}.
> \]
> In particular, for fixed \(k\), the running time is
> \[
> 2^{O_k(n^{2/3}(\log n)^{2/3})}.
> \]

Both running times can of course be capped by \(2^n n^{O(1)}\). The case \(k=0\) is bipartite MIS.

These results improve the logarithmic factors in the supplied attempt. I replace its half-integral Erdős–Pósa and iterative-compression steps by an explicit polynomial-time transversal construction. I do not assert that the discarded steps are false; they are simply unnecessary here. The elementary branching and conflict-counting arguments reused below are proved again.

I also give two polynomial-time special cases in Section 6.

---

## 2. An elementary rounding lemma

The following lemma is the main tool. Its objective is the *cardinality* of the transversal, not a weighted deletion cost.

> **Lemma 2.1.** Suppose positive rational numbers \(x_v\), \(v\in V(H)\), satisfy
> \[
> \sum_{v\in V(C)}x_v\ge 1
> \tag{1}
> \]
> for every odd cycle \(C\) of an \(n\)-vertex graph \(H\). Put
> \[
> T=\sum_v x_v,\qquad h=\left\lceil\log_2(n+1)\right\rceil.
> \]
> An odd-cycle transversal of size at most \(40hT\) can be constructed in polynomial time.

The empty graph is handled separately.

### Proof

First delete
\[
Z=\{v:x_v\ge 1/8\}.
\]
Then
\[
|Z|\le 8T.
\tag{2}
\]
All remaining vertex values are less than \(1/8\).

Throughout the rest of the construction, the active graph is an induced subgraph of \(H-Z\). Give every active edge \(uv\) length
\[
\ell(uv)=\frac{x_u+x_v}{2}.
\]
The total length of a cycle is exactly the sum of its vertex values. Thus (1) says that every odd cycle has length at least \(1\).

### Small metric balls are bipartite

Choose an active vertex \(s\), and let \(d(v)\) be its shortest-path distance from \(s\) in these edge lengths. The ball
\[
B=\{v:d(v)\le 1/4\}
\]
is bipartite.

Indeed, take a shortest-path tree rooted at \(s\), and color vertices by the parity of their tree depth. If an edge \(uv\) inside \(B\) had equally colored ends, its union with the two root paths would give an odd closed walk of length at most
\[
d(u)+d(v)+\ell(uv)
<
\frac14+\frac14+\frac18
=
\frac58.
\]
Every odd closed walk contains an odd cycle of no greater length, contradicting (1).

### Choosing a cheap boundary

Set
\[
\beta=\frac{T}{n},
\]
using the original values of \(T,n\). For a radius \(r\in[1/8,1/4]\), avoiding the finitely many relevant endpoints, define
\[
A_r=\{v:d(v)+x_v/2<r\},
\]
and
\[
\partial_r=\{v:d(v)-x_v/2<r<d(v)+x_v/2\}.
\]
Unreachable vertices belong to neither set.

There is no edge from \(A_r\) to a vertex outside \(A_r\cup\partial_r\). Otherwise, for such an edge \(uv\), with \(u\in A_r\),
\[
d(v)-d(u)>\frac{x_u+x_v}{2}=\ell(uv),
\]
contradicting the shortest-path inequality.

Also, \(A_r\subseteq B\), so \(H[A_r]\) is bipartite. The root belongs to \(A_r\), because \(x_s/2<1/16<r\).

Define the continuous, piecewise-linear function
\[
F(r)=\beta+
\sum_v
\min\!\left\{x_v,\,
\max\{0,r-d(v)+x_v/2\}\right\},
\]
where unreachable vertices contribute zero. Away from breakpoints,
\[
F'(r)=|\partial_r|.
\]
Moreover,
\[
F(1/8)\ge\beta,\qquad
F(1/4)\le\beta+T=(n+1)\beta.
\]
Consequently,
\[
\int_{1/8}^{1/4}\frac{|\partial_r|}{F(r)}\,dr
=
\log\frac{F(1/4)}{F(1/8)}
\le \log(n+1)\le h.
\]
Since the interval has length \(1/8\), some radius has
\[
|\partial_r|\le 8hF(r).
\tag{3}
\]

For a fully discrete polynomial-time choice, inspect the midpoints of the intervals between consecutive breakpoints. On each such interval, \(|\partial_r|\) is constant and \(F\) is affine and positive. The value of \(F\) at the midpoint is at least half its value at the right endpoint. Thus a midpoint exists satisfying the slightly weaker inequality
\[
|\partial_r|\le 16hF(r).
\tag{4}
\]
All these quantities are rational and polynomial-time computable.

Delete \(\partial_r\), set aside \(A_r\), and remove both from the active graph. Since
\[
F(r)\le
\beta+\sum_{v\in A_r\cup\partial_r}x_v,
\]
the boundary cost is at most
\[
16h\left(\beta+\sum_{v\in A_r\cup\partial_r}x_v\right).
\tag{5}
\]

Repeat until no active vertices remain. There are at most \(n\) iterations, because each set \(A_r\) contains its root. The sets removed from the active graph are disjoint, so summing (5) gives total boundary size at most
\[
16h(n\beta+T)=32hT.
\]
Together with (2), the total deletion size is at most \(40hT\).

Every set-aside block is bipartite, and no two such blocks have an edge between them after the boundary deletions. Hence the final remaining graph is bipartite. All operations use polynomially many shortest-path computations and rational arithmetic. ∎

---

## 3. A polynomial-time small-transversal construction

We now prove Theorem 1.

Let
\[
a(v)=d_G(v)+1,\qquad
W=\sum_v a(v)=n+2m,
\]
and let
\[
h=\left\lceil\log_2(n+1)\right\rceil,\qquad
R=\left\lceil\sqrt{\frac{Wh}{k}}\right\rceil.
\]

The vertex values \(a(v)\) remain fixed throughout the construction.

### Step 1: remove neighborhoods of cheap odd cycles

While the current induced subgraph contains an odd cycle \(C\) with
\[
\sum_{v\in V(C)}a(v)\le R,
\tag{6}
\]
choose one and delete its entire closed neighborhood. Add the deleted vertices to a set \(S_0\).

We may choose \(C\) induced: a chord of an odd cycle produces a shorter odd cycle on a proper subset of its vertices, and all values \(a(v)\) are positive.

The cycles chosen in different iterations are pairwise vertex-disjoint and anticomplete in the original graph. Indeed, after selecting a cycle, its whole closed neighborhood is removed. Therefore there are at most \(k\) iterations.

For each selected cycle,
\[
|N_{\mathrm{current}}[V(C)]|
\le
\sum_{v\in V(C)}(d_{\mathrm{current}}(v)+1)
\le
\sum_{v\in V(C)}a(v)
\le R.
\]
Thus
\[
|S_0|\le kR.
\tag{7}
\]

The required minimum-weight odd cycle is polynomial-time computable. One may give edge \(uv\) length \((a(u)+a(v))/2\) and use the parity double cover, with vertices \((v,0),(v,1)\) and edges joining opposite parity copies of adjacent vertices. A shortest path from \((v,0)\) to \((v,1)\) projects to an odd closed walk. Taking the minimum over \(v\), and extracting an odd cycle from the walk, finds a minimum-weight odd cycle. It can then be shortened to an induced one.

### Step 2: round a fractional transversal of the remainder

Let \(H=G-S_0\). By termination, every odd cycle in \(H\) has \(a\)-weight greater than \(R\). Therefore
\[
x_v=\frac{a(v)}{R},\qquad v\in V(H),
\]
satisfies the hypothesis of Lemma 2.1, and
\[
\sum_{v\in V(H)}x_v\le\frac WR.
\]
The lemma constructs an odd-cycle transversal \(S_1\) of \(H\) with
\[
|S_1|\le \frac{40hW}{R}.
\tag{8}
\]

Combining (7) and (8),
\[
|S_0\cup S_1|
\le kR+\frac{40hW}{R}.
\]
Since \(k\le n\le Wh\),
\[
kR
\le \sqrt{kWh}+k
\le 2\sqrt{kWh},
\]
and
\[
\frac{40hW}{R}\le 40\sqrt{kWh}.
\]
Thus the construction returns a transversal of size at most
\[
42\sqrt{kWh}
=
O\!\left(\sqrt{k(n+m)\log(n+2)}\right).
\]
It is also, trivially, at most \(n\). This proves the structural and algorithmic assertions of Theorem 1. ∎

No recognition algorithm for bounded \(\operatorname{iocp}\) is used. On arbitrary inputs, the construction still returns a transversal; the size guarantee uses the promise.

---

## 4. Exact MIS from a transversal

Given an odd-cycle transversal \(S\),
\[
\alpha(G)=
\max_{\substack{X\subseteq S\\X\text{ independent}}}
\left(
|X|+
\alpha\bigl(G-(S\cup N_G(X))\bigr)
\right).
\tag{9}
\]
The graph in the final term is bipartite, so its independence number is computable in polynomial time by maximum matching and König’s theorem.

Enumerating the subsets of \(S\) therefore takes
\[
2^{|S|}n^{O(1)}
\]
time. Theorem 1 now gives the edge-sensitive running time
\[
2^{O(\sqrt{k(n+m)\log(n+2)})}n^{O(1)}.
\]

In particular, for bounded-average-degree graphs and fixed \(k\), this is
\[
2^{O_k(\sqrt{n\log n})}.
\]

The same reasoning works for nonnegative, polynomially encoded vertex weights: replace \(|X|\) in (9) by its weight and solve weighted bipartite MIS by a minimum-cut computation.

---

## 5. Optimized high-degree branching

Fix an integer threshold \(D\ge2\). On a current induced subgraph \(H\), if some vertex \(v\) has degree at least \(D\), branch using
\[
\alpha(H)=
\max\{\alpha(H-v),\,1+\alpha(H-N_H[v])\}.
\tag{10}
\]
Otherwise, apply the algorithm from Theorem 1 and Section 4.

The \(\operatorname{iocp}\) bound is hereditary.

### Number of leaves

Along any root-to-leaf path, an inclusion branch removes at least \(D+1\) vertices, whereas an exclusion branch removes at least one. Thus there are at most
\[
\left\lfloor\frac{n}{D+1}\right\rfloor
\]
inclusion branches.

Encode each path by its binary branch sequence and pad it with zeros to length \(n\). This encoding is injective because leaf sequences are prefix-free. Hence the number of leaves is at most
\[
\sum_{j=0}^{\lfloor n/(D+1)\rfloor}\binom nj
=
2^{O(n\log(D+1)/D)}.
\tag{11}
\]

### Cost at a leaf

A leaf graph has at most \(n\) vertices and maximum degree less than \(D\), hence at most \(nD/2\) edges. Theorem 1 and (9) solve it in time
\[
2^{O(\sqrt{k nD\log(n+2)})}n^{O(1)}.
\tag{12}
\]

Multiplying (11) and (12), the total running time is
\[
2^{O\left(
\frac{n\log(D+1)}{D}
+
\sqrt{k nD\log(n+2)}
\right)}n^{O(1)}.
\tag{13}
\]

Choose
\[
D=\left\lceil
\left(\frac{n\log(n+2)}{k}\right)^{1/3}
\right\rceil,
\]
provided the quantity inside the ceiling is at least \(2\). Both terms in the exponent of (13) are then
\[
O\!\left(k^{1/3}n^{2/3}(\log(n+2))^{2/3}\right).
\]
If that quantity is smaller than \(2\), the claimed exponent is already \(\Omega(n)\), so brute force satisfies the stated bound.

This proves Theorem 2. ∎

---

## 6. Two polynomial-time special cases

### 6.1 Sparse graphs with bounded induced odd-cycle length

Here is an elementary proof of the polynomial special case proposed in the supplied attempt; it does not need half-integral packing.

> **Proposition 6.1.** Fix \(k,L,c\) and \(0<\varepsilon\le1\). MIS is polynomial-time solvable on graphs satisfying:
> 1. \(\operatorname{iocp}(G)\le k\);
> 2. every induced odd cycle has length at most \(L\);
> 3. every induced subgraph \(F\) satisfies
>    \[
>    e(F)\le c|V(F)|^{2-\varepsilon}.
>    \]

**Proof.** Greedily choose vertex-disjoint induced odd cycles, deleting only their vertices, until the remaining graph is bipartite. Let the selected cycles be \(C_1,\ldots,C_q\), and put
\[
U=\bigcup_i V(C_i).
\]
Each cycle has at most \(L\) vertices, so \(|U|\le qL\). Moreover, \(U\) is an odd-cycle transversal.

Form a graph \(J\) on the selected cycles, joining two when an edge of \(G\) connects them. Since the cycles are vertex-disjoint,
\[
\alpha(J)\le k.
\]
Turán’s theorem applied to \(\overline J\) gives
\[
e(J)\ge\frac{q(q-k)}{2k}.
\]
Every edge of \(J\) requires a distinct pair of cycles joined by an edge in \(G[U]\), so
\[
e(J)\le e(G[U])\le c(qL)^{2-\varepsilon}.
\]
For \(q\ge2k\), it follows that
\[
\frac{q^2}{4k}\le c(qL)^{2-\varepsilon},
\]
and hence
\[
q\le
\left(4kcL^{2-\varepsilon}\right)^{1/\varepsilon}.
\]
Otherwise \(q<2k\). Thus
\[
|U|
\le
L\max\left\{
2k,\,
\left(4kcL^{2-\varepsilon}\right)^{1/\varepsilon}
\right\},
\]
a constant independent of \(n\). Apply (9). ∎

This includes fixed \(K_{s,s}\)-subgraph-free classes: the usual common-neighbor counting bound gives
\[
e(F)=O_s(|V(F)|^{2-1/s}).
\]

### 6.2 A dense special case: bounded neighborhood independence

A different restriction permits polynomial time without requiring a small transversal.

> **Proposition 6.2.** Fix \(k,L,a\), with \(a\ge1\). MIS is polynomial-time solvable on graphs satisfying:
> \[
> \operatorname{iocp}(G)\le k,\qquad
> \alpha(G[N(v)])\le a\quad\text{for every }v,
> \]
> and having no induced odd cycle longer than \(L\).
> A running-time bound is \(n^{aLk+O(1)}\).

**Proof.** If the graph is bipartite, solve it directly. Otherwise choose an induced odd cycle \(C\), necessarily of length at most \(L\), and set
\[
B=N[V(C)].
\]
Every independent set in a closed neighborhood \(N[v]\) has size at most \(a\). Therefore
\[
\alpha(G[B])\le aL.
\]
Enumerate all independent subsets \(X\subseteq B\), of which there are \(O_{a,L}(n^{aL})\), and use
\[
\alpha(G)=
\max_{\substack{X\subseteq B\\X\text{ independent}}}
\left(
|X|+
\alpha\bigl(G-(B\cup N(X))\bigr)
\right).
\tag{14}
\]

Because \(C\) is anticomplete to \(G-B\),
\[
\operatorname{iocp}(G-B)\le k-1.
\]
Thus every recursive instance in (14) has its packing bound reduced by one. The other hypotheses are hereditary. Recursion depth is at most \(k\), giving the claimed polynomial bound. ∎

Equivalently, the neighborhood condition excludes an induced \(K_{1,a+1}\). Unlike Proposition 6.1, this case allows arbitrarily large cliques and arbitrarily large odd-cycle transversals.

---

## 7. What remains unresolved

The unrestricted conjecture is not proved. The general exponent obtained here is
\[
O_k\!\left(n^{2/3}(\log n)^{2/3}\right),
\]
not \(O_k(\log n)\).

The new ingredient is a polynomial-time construction of a transversal of size
\[
O\!\left(\sqrt{k(n+m)\log n}\right).
\]
This improves the supplied approach but still leaves too many transversal vertices to enumerate.

Bounded \(\operatorname{iocp}\) alone cannot force a small odd-cycle transversal: \(K_n\) has \(\operatorname{iocp}=1\) but \(\tau_{\mathrm{odd}}(K_n)=n-2\). Thus a full polynomial-time algorithm must exploit more than uniformly small transversals. The high-degree branching above handles some dense configurations cheaply, but its worst-case analysis remains subexponential rather than polynomial.

The two polynomial cases impose additional hypotheses that do not follow from bounded \(\operatorname{iocp}\). No hardness construction or counterexample to the original tractability conjecture is obtained.