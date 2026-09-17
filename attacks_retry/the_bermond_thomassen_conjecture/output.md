```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For k≥4, I prove the conjecture when n=2k+s, s≤k+3, and s(s+1)≤28(k−2), extending the boundary cases of the supplied attempt.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved; this uses the established three-cycle and tournament cases, and novelty is unchecked."
}
```

# 1. Results and scope

All digraphs are finite and loopless, with no parallel arcs. Antiparallel arcs are allowed, and cycles are directed and vertex-disjoint. A **digon** is a directed cycle of length two.

The positive result is the following.

**Theorem 1.** Let \(k\ge4\), and let \(D\) satisfy
\[
|V(D)|=2k+s,\qquad \delta^+(D)\ge2k-1,
\]
where \(s\ge0\) is an integer. If
\[
\boxed{s\le k+3,\qquad s(s+1)\le28(k-2),}
\tag{1}
\]
then \(D\) contains \(k\) vertex-disjoint directed cycles.

This improves the supplied attempt’s conditions
\[
s\le k+2,\qquad s(s+1)<28(k-2).
\]
The improvement comes from resolving equality in the matching argument, not from improving its asymptotic range. I rederive the counting argument below rather than treating the previous attempt as an authority.

For example, Theorem 1 proves the conjecture whenever
\[
4\le k\le17,\qquad |V(D)|\le3k+3.
\]
Indeed, at \(s=k+3\), the second condition in (1) is equivalent to
\[
(k-4)(k-17)\le0.
\]
In particular, the four-cycle case holds for all digraphs of order at most \(15\).

I also give a **28-vertex** counterexample to the auxiliary question about outdegree six and no digons. This is smaller than the supplied attempt’s 49-vertex example, although its girth is three rather than four. It is not a counterexample to Bermond–Thomassen.

# 2. Established inputs and a semicomplete-core lemma

The proof uses two established results explicitly reported in the question:

1. Every digraph of minimum outdegree at least five contains three disjoint cycles.
2. Every tournament of minimum outdegree at least \(2h-1\) contains \(h\) disjoint cycles.

The outdegree version of the tournament theorem follows by reversing all arcs if it is stated with indegree. No additional literature claims are needed below.

A digraph is **semicomplete** if every pair of distinct vertices supports at least one of the two possible arcs.

**Lemma 2.** Every semicomplete digraph of minimum outdegree at least \(2h-1\) contains \(h\) disjoint cycles.

**Proof.** Induct on \(h\). For \(h=1\), positive minimum outdegree gives a cycle. If the digraph has no digon, it is a tournament, so the established tournament theorem applies. Otherwise, delete a digon. The remaining digraph is semicomplete and has minimum outdegree at least
\[
(2h-1)-2=2(h-1)-1.
\]
Apply induction and restore the deleted digon. \(\square\)

The following lemma handles the equality configurations in the counting argument.

**Lemma 3 — absorbing an exceptional set.** Suppose
\[
V(D)=S\mathbin{\dot\cup}R,\qquad |S|=a\le k-1,
\]
and that:

- \(\delta^+(D)\ge2k-1\);
- \(D[R]\) is semicomplete;
- every arc from \(R\) to \(S\) is present.

Then \(D\) contains \(k\) disjoint cycles.

**Proof.** Each \(x\in S\) has at least
\[
(2k-1)-(a-1)=2k-a
\]
outneighbors in \(R\). Each of these forms a digon with \(x\), because all arcs from \(R\) to \(S\) are present.

Since \(2k-a\ge a\), we can greedily choose distinct partners in \(R\) for all \(a\) vertices of \(S\). This gives \(a\) disjoint digons covering \(S\).

After deleting their \(2a\) vertices, the remaining digraph is semicomplete and has minimum outdegree at least
\[
2k-1-2a=2(k-a)-1.
\]
Lemma 2 supplies \(k-a\) additional cycles. \(\square\)

# 3. A Tutte–Berge count, including its equality case

For a digraph \(D\), let its **digon graph** \(G\) have vertex set \(V(D)\), with
\[
uv\in E(G)\quad\Longleftrightarrow\quad uv,vu\in A(D).
\]
Thus matchings in \(G\) are precisely packings of digons in \(D\).

Suppose that
\[
|V(D)|=n,\qquad \delta^+(D)\ge n-1-s,
\tag{2}
\]
and \(G\) has matching number at most \(r\), where \(n\ge2r+2\).

By the Tutte–Berge formula, there exists \(S\subseteq V(G)\) such that, writing
\[
a=|S|,\qquad R=V(G)\setminus S,\qquad m=n-a,\qquad q=o(G-S),
\]
we have
\[
q\ge n-2r+a.
\tag{3}
\]
Since \(q\le n-a\), this implies
\[
0\le a\le r.
\tag{4}
\]

## Counting cross-pairs

Let \(P\) be the number of unordered pairs lying in different components of \(G-S\). Then
\[
P\ge(q-1)\left(m-\frac q2\right).
\tag{5}
\]

To see this, merge any even components into one of the odd components. This leaves \(q\) nonempty groups and cannot increase the number of cross-pairs. Among partitions of \(m\) vertices into \(q\) nonempty groups, cross-pairs are minimized when \(q-1\) groups are singletons and one group has size \(m-q+1\), giving (5).

The function
\[
\phi(q)=(q-1)\left(m-\frac q2\right)
\]
is increasing for integers \(1\le q\le m\), since
\[
\phi(q+1)-\phi(q)=m-q.
\]
Using (3), we therefore obtain
\[
P\ge C(a):=
\frac{(n-2r+a-1)(n+2r-3a)}2.
\tag{6}
\]

## Counting missing arcs

Every pair counted by \(P\) is a nonedge of the digon graph, so at least one of its two directed arcs is missing.

Let \(M_{\mathrm{int}}\) be the number of missing arcs with both endpoints in \(R\), and let \(M_R\) be the number of missing arcs whose tail lies in \(R\), with head anywhere else in \(V(D)\). By (2), every vertex is missing at most \(s\) outgoing arcs. Consequently,
\[
C(a)\le P\le M_{\mathrm{int}}\le M_R\le sm.
\tag{7}
\]

In particular,
\[
C(a)\le s(n-a).
\tag{8}
\]

The equality case is essential.

**Equality conclusion.** If
\[
C(a)=s(n-a),
\tag{9}
\]
then \(D[R]\) is semicomplete and every arc from \(R\) to \(S\) is present.

Indeed, equality holds throughout (7). Equality \(M_{\mathrm{int}}=M_R\) means that no arc from \(R\) to \(S\) is missing. Equality \(P=M_{\mathrm{int}}\) means:

- exactly one arc is missing on each cross-pair;
- no arc is missing on a pair within a component of \(G-S\).

Thus every pair in \(R\) supports at least one arc, as asserted.

# 4. Proof of Theorem 1

Set
\[
n=2k+s,\qquad r=k-4.
\]

If the digon graph has a matching of size \(r+1=k-3\), delete those digons. The remaining induced digraph has minimum outdegree at least
\[
(2k-1)-2(k-3)=5.
\]
The established three-cycle theorem supplies three further cycles, completing the required packing.

It remains to consider the case in which the digon graph has matching number at most \(r\). Choose \(S\) as in Section 3.

Define
\[
F(a)=
\frac{(n-2r+a-1)(n+2r-3a)}2-s(n-a).
\]
The counting inequality gives
\[
F(a)\le0.
\tag{10}
\]

On the other hand, \(F\) is a concave quadratic in \(a\), with coefficient \(-3/2\) on \(a^2\). Its endpoint values simplify to
\[
F(0)=\frac{28(k-2)-s(s+1)}2
\tag{11}
\]
and
\[
F(r)=\frac{(n-r)(k+3-s)}2.
\tag{12}
\]

Under (1), both endpoint values are nonnegative. Concavity therefore gives
\[
F(a)\ge0\qquad(0\le a\le r).
\tag{13}
\]
When \(r=0\), this is simply the assertion at the single endpoint.

Combining (10) and (13), we obtain \(F(a)=0\). The equality conclusion from Section 3 now shows that:

- \(D[R]\) is semicomplete;
- all arcs from \(R\) to \(S\) are present.

Moreover,
\[
|S|=a\le r=k-4<k.
\]
Lemma 3 supplies \(k\) disjoint cycles.

This covers both the strict and boundary cases of (1), proving Theorem 1. \(\square\)

# 5. A 28-vertex obstruction to the auxiliary girth claim

The catalog already reports that the girth strengthening is false. Here is a small explicit construction for its stated four-cycle question.

More generally, fix \(k\ge2\), and put \(q=2k-1\). Let
\[
X=\{x_0,\ldots,x_{q-1}\}
\]
induce the regular cyclic tournament
\[
x_i\longrightarrow x_{i+j}
\qquad
(1\le j\le k-1),
\]
where subscripts are taken modulo \(q\).

For each \(i\), add a set \(Y_i\) of \(k-1\) new vertices. Add precisely these further arcs:
\[
x_i\longrightarrow y\quad(y\in Y_i),
\]
and
\[
y\longrightarrow x_h\quad(y\in Y_i,\ h\ne i).
\]
There are no arcs between vertices in \(\bigcup_iY_i\).

Call the resulting digraph \(H_k\).

## Degree and absence of digons

Each \(x_i\) has \(k-1\) outneighbors in \(X\) and \(k-1\) in \(Y_i\). Each \(y\in Y_i\) has all \(2k-2\) vertices of \(X\setminus\{x_i\}\) as outneighbors. Therefore
\[
\delta^+(H_k)=2k-2.
\]

There are no digons:

- \(H_k[X]\) is a tournament;
- \(x_i\to Y_i\), but no vertex of \(Y_i\) sends an arc to \(x_i\);
- for \(h\ne i\), the only arc between \(x_h\) and \(y\in Y_i\) is \(y\to x_h\).

## Exact cycle-packing number

Every cycle contains at least two vertices of \(X\). A cycle cannot lie entirely outside \(X\), since that set is independent. A cycle containing exactly one distinguished vertex would have to be
\[
x_i\to y\to x_i,
\]
which is impossible.

Consequently,
\[
\nu_{\mathrm{cyc}}(H_k)\le
\left\lfloor\frac{|X|}{2}\right\rfloor=k-1.
\]

Equality holds. Pair any \(2k-2\) vertices of \(X\). For a pair with tournament arc \(x_h\to x_i\), choose \(y\in Y_i\); then
\[
x_i\to y\to x_h\to x_i
\]
is a triangle. Different pairs yield vertex-disjoint triangles. Thus
\[
\boxed{
|V(H_k)|=k(2k-1),\qquad
\delta^+(H_k)=2k-2,\qquad
g(H_k)=3,\qquad
\nu_{\mathrm{cyc}}(H_k)=k-1.
}
\tag{14}
\]

For \(k=4\), this is an explicitly specified oriented graph on
\[
4\cdot7=28
\]
vertices, with minimum outdegree six and no four disjoint cycles.

Its degree is **one below** the Bermond–Thomassen threshold of seven.

## Optimality within this bottleneck mechanism

The order in (14) is optimal among oriented digraphs using the same type of obstruction.

**Proposition 4.** Suppose \(D\) is oriented, \(\delta^+(D)\ge2k-2\), and there is a set \(X\) of \(2k-1\) vertices such that every directed cycle contains at least two vertices of \(X\). Then
\[
|V(D)|\ge k(2k-1).
\]

**Proof.** Put \(Y=V(D)\setminus X\). The digraph \(D[Y]\) is acyclic.

No vertex \(y\in Y\) can be an outneighbor of two distinct vertices \(x,x'\in X\). Otherwise, follow a directed path in \(D[Y]\) from \(y\) to a sink \(z\) of \(D[Y]\). All outneighbors of \(z\) lie in \(X\), and there are at least \(2k-2\) of them. Since \(|X|=2k-1\), at least one of \(z\to x,z\to x'\) is present. This produces a directed cycle containing exactly one vertex of \(X\), a contradiction.

Thus the sets \(N^+(x)\cap Y\), for \(x\in X\), are pairwise disjoint. Since \(D[X]\) is oriented,
\[
\begin{aligned}
|Y|
&\ge \sum_{x\in X}d_Y^+(x)\\
&=\sum_{x\in X}d_D^+(x)-e(D[X])\\
&\ge (2k-1)(2k-2)-\binom{2k-1}{2}\\
&=(2k-1)(k-1).
\end{aligned}
\]
Adding \(|X|=2k-1\) proves the claim. \(\square\)

This is only a restricted optimality statement. It does **not** establish that 28 is the minimum possible order of a counterexample to the auxiliary question.

# 6. Remaining gap

Theorem 1 is an order-restricted result, with surplus
\[
s=O(\sqrt{k}).
\]
It does not improve the unrestricted minimum-outdegree bound.

The matching argument works because either sufficiently many digons exist, or equality forces a semicomplete core. Outside the stated inequalities, the count need not force either outcome. In particular, general oriented digraphs of large order remain outside its reach.

The auxiliary construction has minimum outdegree \(2k-2\), not \(2k-1\), so it establishes sharpness and refutes the girth strengthening—not Bermond–Thomassen itself.

Thus the main conjecture remains unresolved by this attack. The rigorous progress is the boundary extension in Theorem 1 and the explicit, restricted-optimal bottleneck construction above; their novelty has not been checked.