```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general conjecture remains open, but it holds for witnesses with bounded one-sided error, bounded score imbalance, and a learnable bounded multipartite-plus-one-sided-error structure.",
  "would_publish": false,
  "caveats": "The additional structural parameters need not be bounded in terms of k, and failure of the partial algorithms does not certify the original lower bound."
}
```

# 1. Statement and notation

For a vertex order \(\rho\) of a tournament \(T\), write \(B_\rho=T^\rho\) for its undirected backedge graph: \(uv\in E(B_\rho)\) when the arc between \(u,v\) points from the later vertex to the earlier vertex in \(\rho\). Thus
\[
\overrightarrow{\omega}(T)=\min_\rho \omega(B_\rho).
\]

Call an order \(\sigma\) a \(k\)-witness if
\[
\omega(B_\sigma)\le k-1.
\]
The conjecture asks for a polynomial-time gap algorithm which, whenever a \(k\)-witness exists, constructs an order whose backedge clique number is bounded solely in terms of \(k\).

The results below do not handle an arbitrary \(k\)-witness. They give several rigorous special cases and a useful reformulation as robust sorting.

---

# 2. Symmetric-difference reformulation

Given two orders \(\rho,\sigma\), let \(I(\rho,\sigma)\) be their inversion graph: \(uv\) is an edge when \(\rho\) and \(\sigma\) order \(u,v\) differently.

## Lemma 2.1
For every tournament \(T\) and orders \(\rho,\sigma\),
\[
E(B_\rho)\triangle E(B_\sigma)=E(I(\rho,\sigma)).
\]

### Proof
For a fixed pair \(u,v\), changing their relative order toggles whether the fixed tournament arc is backward. Their backward status is unchanged precisely when the two orders agree on the pair. \(\square\)

Consequently, after fixing an arbitrary reference order \(\tau\) and putting \(G=B_\tau\), the problem becomes:

> Given a graph \(G\), promised that
> \[
> G\triangle I(\tau,\sigma)
> \]
> is \(K_k\)-free for some permutation \(\sigma\), find a permutation \(\pi\) such that
> \[
> G\triangle I(\tau,\pi)
> \]
> has bounded clique number.

There is no hidden restriction on \(G\): every graph is the backedge graph of some tournament relative to a prescribed order. Thus the error graph of a witnessing order can be an arbitrary \(K_k\)-free graph.

---

# 3. Transferring closeness to a witnessing order

The following elementary lemma is useful throughout.

## Lemma 3.1
Let \(\sigma\) be a \(k\)-witness for \(T\), and let \(\pi\) be any order. Then
\[
\omega(B_\pi)\le (k-1)\,\omega\bigl(I(\sigma,\pi)\bigr).
\]

### Proof
Let \(C\) be a clique in \(B_\pi\), and list it as
\[
c_1<_{\sigma}c_2<_{\sigma}\cdots<_{\sigma}c_s.
\]
Write \(p_i\) for the position of \(c_i\) in \(\pi\).

On \(C\), Lemma 2.1 and the fact that \(B_\pi[C]\) is complete give
\[
\mathbf 1_{B_\sigma}(c_ic_j)=1-\mathbf 1_{I(\sigma,\pi)}(c_ic_j).
\]
Thus, for \(i<j\),
\[
c_ic_j\in E(B_\sigma)\quad\Longleftrightarrow\quad p_i<p_j.
\]
An increasing subsequence of \(p_1,\dots,p_s\) therefore gives a clique in \(B_\sigma\), and hence has length at most \(k-1\).

A sequence whose longest increasing subsequence has length at most \(k-1\) can be partitioned into at most \(k-1\) decreasing subsequences. For completeness, assign \(p_i\) the length of a longest increasing subsequence ending at \(p_i\); entries receiving the same value form a decreasing subsequence. Each decreasing subsequence is a clique in \(I(\sigma,\pi)\), and so has size at most \(\omega(I(\sigma,\pi))\). Therefore
\[
|C|\le (k-1)\omega(I(\sigma,\pi)).
\]
\(\square\)

Thus it suffices, in a number of special cases, to find an order at bounded longest-decreasing-subsequence distance from a witnessing order.

---

# 4. A Borda-order theorem

Let
\[
\sigma=(v_1,\dots,v_n),\qquad H=B_\sigma.
\]
For \(v_i\), define its signed error imbalance
\[
\delta_i=
  |N_H(v_i)\cap\{v_1,\dots,v_{i-1}\}|
 -
  |N_H(v_i)\cap\{v_{i+1},\dots,v_n\}|.
\]

Because the transitive tournament following \(\sigma\) gives \(v_i\) outdegree \(n-i\), flipping the edges of \(H\) gives
\[
d_T^+(v_i)=n-i+\delta_i. \tag{4.1}
\]

## Theorem 4.1
Suppose \(\sigma\) is a \(k\)-witness and
\[
|\delta_i|\le b\qquad\text{for every }i.
\]
Let \(\pi\) order the vertices by nonincreasing tournament outdegree, with arbitrary deterministic tie-breaking. Then
\[
\omega(B_\pi)\le (k-1)(2b+1).
\]

### Proof
Let \(v_{i_1},\dots,v_{i_t}\), with \(i_1<\cdots<i_t\), form a clique in \(I(\sigma,\pi)\). Their order in \(\pi\) is the reverse of their order in \(\sigma\). Since \(\pi\) is nonincreasing by outdegree,
\[
d_T^+(v_{i_1})\le d_T^+(v_{i_2})\le\cdots\le d_T^+(v_{i_t}).
\]
Using (4.1),
\[
\delta_{i_{j+1}}-\delta_{i_j}
 \ge i_{j+1}-i_j
 \ge 1.
\]
Hence the selected \(\delta\)-values are separated by at least one. As all lie in \([-b,b]\), one has \(t\le 2b+1\). Therefore
\[
\omega(I(\sigma,\pi))\le 2b+1.
\]
Lemma 3.1 completes the proof. \(\square\)

In particular, if \(H\) has maximum degree at most \(\Delta\), then \(b\le\Delta\), giving
\[
\omega(B_\pi)\le (k-1)(2\Delta+1).
\]

There is also a quantitative sparse-error version.

## Corollary 4.2
If \(\sigma\) is a \(k\)-witness and \(m=|E(B_\sigma)|\), then the same Borda order satisfies
\[
\omega(B_\pi)
 \le
 (k-1)\left\lfloor\sqrt{8m+1}\right\rfloor .
\]

### Proof
For a clique of size \(t\) in \(I(\sigma,\pi)\), the corresponding \(\delta\)-values are separated by at least one. The minimum possible sum of their absolute values is
\[
\left\lfloor\frac{t^2}{4}\right\rfloor.
\]
On the other hand,
\[
\sum_{i=1}^n |\delta_i|
 \le \sum_{i=1}^n d_H(v_i)=2m.
\]
Thus
\[
\left\lfloor\frac{t^2}{4}\right\rfloor\le2m,
\]
which implies \(t^2\le8m+1\). Apply Lemma 3.1. \(\square\)

This proves the conjectured conclusion, with a function of \(k\), whenever \(b\) or \(m\) is itself bounded by a function of \(k\).

## A sharp obstruction to the Borda approach

The dependence on \(m^{1/2}\) cannot be replaced by a constant even when the witnessing backedge graph is a forest.

For \(t\ge1\), let
\[
C=\{c_1,\dots,c_t\},
\qquad
L=\{\ell_{i,j}:1\le i\le t,\ 1\le j\le2i\}.
\]
Order all vertices of \(L\) first, followed by
\[
c_1<_{\sigma}\cdots<_{\sigma}c_t.
\]
Let \(H\) have exactly the edges
\[
c_i\ell_{i,j}\qquad(1\le j\le2i).
\]
Thus \(H\) is a disjoint union of stars, hence a forest. Construct \(T\) by reversing precisely the edges of \(H\) relative to \(\sigma\). Then
\[
\overrightarrow{\omega}(T)\le\omega(H)=2.
\]

There are \(t(t+1)\) vertices in \(L\), and
\[
d_T^+(c_i)
   = (t-i)+2i
   = t+i.
\]
Consequently every nonincreasing-outdegree order lists
\[
c_t,c_{t-1},\dots,c_1
\]
in that relative order. Since
\[
c_1\to c_2\to\cdots\to c_t
\]
inside \(T[C]\), the set \(C\) is a \(K_t\) in the resulting backedge graph.

Here \(m=t(t+1)\), so the \(\sqrt m\) exponent in Corollary 4.2 is asymptotically sharp for the Borda algorithm. This does not contradict the stated \(k=3\) result, which must use a different algorithm.

---

# 5. A one-sided-error special case

The preceding forest example is nevertheless handled by a different elementary algorithm.

For an order \(\sigma=(v_1,\dots,v_n)\) and graph \(H\), define
\[
d_{\sigma}^{\rightarrow}(H)
 =
 \max_i
 |N_H(v_i)\cap\{v_{i+1},\dots,v_n\}|.
\]

## Theorem 5.1
Suppose \(T\) has an order \(\sigma\) such that
\[
d_{\sigma}^{\rightarrow}(B_\sigma)\le D.
\]
The following polynomial-time algorithm finds an order \(\pi\) with
\[
\omega(B_\pi)\le D+1:
\]

1. In the current induced subtournament, choose a vertex of minimum indegree.
2. Append it to \(\pi\) and delete it.
3. Repeat.

### Proof
Let \(U\) be the current vertex set, and let \(u\) be the first vertex of \(U\) in the witnessing order \(\sigma\). Every other vertex of \(U\) is later than \(u\) in \(\sigma\). Hence
\[
d^-_{T[U]}(u)
 =
 |N_{B_\sigma}(u)\cap U|
 \le D.
\]
Therefore the minimum indegree in \(T[U]\) is at most \(D\), so the algorithm always selects a vertex of indegree at most \(D\).

In the final order \(\pi\), those current inneighbors are exactly the selected vertex's later neighbors in \(B_\pi\). Thus every vertex has at most \(D\) later neighbors in \(B_\pi\). In a clique, the earliest vertex has all other clique vertices as later neighbors, so the clique has size at most \(D+1\). \(\square\)

The algorithm also correctly detects failure of this stronger premise: if at some stage the minimum indegree exceeds \(D\), no order with the stated one-sided property can exist. This is not, however, a certificate that \(\overrightarrow{\omega}(T)\ge k\).

The forest construction above has \(d_\sigma^\rightarrow(H)=1\), so Theorem 5.1 produces an order with backedge clique number at most \(2\), despite the failure of the Borda order.

---

# 6. A learnable multipartite-plus-one-sided-error case

The next theorem handles some dense witnesses, including complete multipartite backedge graphs.

For a partition
\[
\mathcal P=\{P_1,\dots,P_q\}
\]
of \(V(T)\), let \(K_{\mathcal P}\) be the complete multipartite graph whose edges are precisely the pairs in different parts.

## Theorem 6.1
Fix \(k\ge2\) and \(D\ge0\). Suppose there are an order \(\sigma\) and a partition \(\mathcal P\) such that, with
\[
H=B_\sigma,\qquad J=H\triangle K_{\mathcal P},
\]
one has
\[
\omega(H)\le k-1
\quad\text{and}\quad
d_\sigma^\rightarrow(J)\le D. \tag{6.1}
\]
Then a polynomial-time algorithm, for fixed \(k,D\), finds an order \(\pi\) satisfying
\[
\omega(B_\pi)\le (k-1)(D+1)^2. \tag{6.2}
\]

The running time of the algorithm below is
\[
n^{(k-1)(D+1)^2+O(1)}.
\]

### Bounding the number of parts

Choose one representative from each part of \(\mathcal P\). The graph \(J\) on those representatives is \((D+1)\)-colorable: process them in reverse \(\sigma\)-order, when each vertex has at most \(D\) already-colored \(J\)-neighbors.

Thus \(J\) has an independent set of representatives of size at least
\[
\left\lceil \frac q{D+1}\right\rceil.
\]
For representatives from distinct parts, every pair belongs to \(K_{\mathcal P}\). Hence a \(J\)-independent set of representatives is a clique in
\[
H=J\triangle K_{\mathcal P}.
\]
By \(\omega(H)\le k-1\),
\[
q\le Q:=(k-1)(D+1). \tag{6.3}
\]

### Enumerating the correct partition

The following bounded-depth search generates the true partition among its candidates.

Suppose \(U\) is the union of the parts not yet extracted. Choose a vertex \(a\in U\), and put
\[
S(a,U)=\{a\}\cup\bigl(N_T^+(a)\cap U\bigr).
\]
Enumerate every \(E\subseteq U\setminus\{a\}\) with \(|E|\le D\), declare
\[
P=S(a,U)\triangle E
\]
to be the next part, and recurse on \(U\setminus P\). Stop after at most \(Q\) parts.

To see that the true partition occurs, at a true branch choose \(a\) to be the first vertex of \(U\) in \(\sigma\). For every \(v\in U\setminus\{a\}\), the vertex \(a\) precedes \(v\) in \(\sigma\). A direct check from
\[
J=H\triangle K_{\mathcal P}
\]
gives
\[
P(a)\cap U
 =
 S(a,U)\triangle\bigl(N_J(a)\cap U\bigr). \tag{6.4}
\]
All vertices of \(U\setminus\{a\}\) are later than \(a\), so (6.1) gives
\[
|N_J(a)\cap U|\le D.
\]
Thus the correction set in (6.4) is among those enumerated. Repeating this extracts every true part. By (6.3), the recursion has depth at most \(Q\).

### Testing a candidate partition

For each generated partition \(\mathcal P'\), form the tournament \(T'\) obtained by reversing all arcs joining distinct parts of \(\mathcal P'\). Run the minimum-indegree elimination algorithm of Theorem 5.1 on \(T'\).

Reject \(\mathcal P'\) if at some stage the current minimum indegree exceeds \(D\). Otherwise return the resulting order \(\pi\).

For the true partition,
\[
B(T',\sigma)=H\triangle K_{\mathcal P}=J.
\]
The proof of Theorem 5.1 therefore shows that the minimum indegree never exceeds \(D\). Hence the true partition passes.

For any passing candidate partition with \(q'\le Q\), its output satisfies
\[
\omega(B(T',\pi))\le D+1.
\]
Inside each part, \(T\) and \(T'\) are identical. Therefore any clique \(C\) of \(B(T,\pi)\) has
\[
|C\cap P_i'|\le D+1
\]
for every part \(P_i'\). It follows that
\[
|C|\le q'(D+1)\le Q(D+1)=(k-1)(D+1)^2,
\]
which proves (6.2). \(\square\)

For \(D=0\), this handles every witnessing backedge graph that is complete multipartite, and obtains the exact bound \(k-1\).

The extra structure is genuine. For example, a balanced blow-up of the \(5\)-cycle is triangle-free but cannot, for fixed \(q,D\), always be written as
\[
K_{\mathcal P}\triangle J
\]
with at most \(q\) parts and \(J\) of one-sided degree at most \(D\). Indeed, take five independent sets of size \(t\), with complete edges exactly between cyclically consecutive sets. For any partition into at most \(q\) parts, choose a most frequent part label in each of the five sets. Each corresponding label class has size at least \(t/q\). Some pair of these five labels must disagree with the \(C_5\) adjacency pattern: otherwise nonadjacent pairs would force all five labels equal, while adjacent pairs would force them unequal. The residual graph then contains \(K_{t/q,t/q}\), and hence has degeneracy at least \(t/q\). Taking \(t>qD\) rules out one-sided degree \(D\). Thus a general \(K_k\)-free error graph does not admit the decomposition used in Theorem 6.1.

---

# 7. Exact finite formulation

For computational experiments, the condition \(\overrightarrow{\omega}(T)\le r\) has the following explicit \(0\)-\(1\) formulation.

Use variables \(x_{uv}\), for ordered distinct pairs, with \(x_{uv}=1\) meaning \(u\) precedes \(v\). Impose
\[
x_{uv}+x_{vu}=1
\]
and, for all distinct \(u,v,w\),
\[
x_{uv}+x_{vw}+x_{wu}\le2.
\]
These constraints make \(x\) a total order.

For every \((r+1)\)-set \(S\), impose
\[
\sum_{u\to v\in A(T[S])} x_{uv}\ge1. \tag{7.1}
\]
Constraint (7.1) says that at least one tournament arc in \(S\) is forward. It fails exactly when every pair of \(S\) is a backedge, i.e. when \(S\) is a \(K_{r+1}\) in the backedge graph. Thus feasibility is equivalent to
\[
\overrightarrow{\omega}(T)\le r.
\]

This gives a fully specified exhaustive test for small tournaments, although I have not run such a computation here.

---

# 8. What remains open

The positive results above depend on an additional parameter:

- bounded signed error imbalance \(b\);
- bounded one-sided error degree \(D\); or
- bounded one-sided error after removing a learnable complete multipartite template.

None of these bounds follows from the sole condition that \(B_\sigma\) is \(K_k\)-free. By the symmetric-difference reformulation, an arbitrary \(K_k\)-free graph can occur as the backedge graph of a witnessing order.

Moreover, the negative outcome of the structured algorithms is only:

> no witness with the specified additional structure exists,

not the required conclusion
\[
\overrightarrow{\omega}(T)\ge k.
\]

Thus these arguments do not prove Conjecture 4.2. They isolate two polynomially tractable robust-sorting regimes and one learnable dense regime, but the general case of irregular \(K_k\)-free comparison errors remains untreated.