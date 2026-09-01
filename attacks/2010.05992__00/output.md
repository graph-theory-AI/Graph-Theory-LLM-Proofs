```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A rooted symmetric-difference lemma yields a sharper factorial upper bound, exponential bounds in two broad intersection regimes, and the exact value for rank two, but not the conjectured general exponential bound.",
  "would_publish": false,
  "caveats": "The general upper bound still contains a factor k!, and no claim of literature novelty is made."
}
```

# Mathematical writeup

## 1. Statement and notation

Let \(f_r(k)\) be the maximum size of a \(k\)-uniform family \(\mathcal F\) containing no \(r\) distinct sets \(A_1,\dots,A_r\) such that every ground-set element belongs to

\[
0,\ 1,\ r-1,\ \text{or }r
\]

of them. Such an \(r\)-tuple is an \(r\)-near-sunflower.

The conjecture is that, for each fixed \(r\),

\[
f_r(k)\le C_r^k.
\]

For \(r=3\), every three distinct sets form a near-sunflower, so \(f_3(k)=2\). Thus \(r\ge4\) is the substantive range.

I do not prove the conjecture. I give several rigorous partial results.

---

## 2. A rooted symmetric-difference lemma

The following observation appears to be the most useful structural reduction.

### Lemma 2.1

Let \(A_0,A_1,\dots,A_{r-1}\) be distinct sets, and put

\[
D_i=A_i\triangle A_0,\qquad 1\le i\le r-1.
\]

Then \(A_0,A_1,\dots,A_{r-1}\) form an \(r\)-near-sunflower if and only if
\(D_1,\dots,D_{r-1}\) form an ordinary sunflower.

### Proof

For every \(x\in A_0\), complement the membership bit of \(x\) in all \(r\) sets. This sends the multiplicity \(t\) of \(x\) to \(r-t\). The set

\[
\{0,1,r-1,r\}
\]

is invariant under \(t\mapsto r-t\), so this operation preserves the near-sunflower condition. After all these column-complementations, \(A_0\) becomes empty and \(A_i\) becomes \(A_i\triangle A_0=D_i\).

Since the first set is now empty, the possible multiplicities among the remaining \(r-1\) sets are

\[
0,\ 1,\ r-1.
\]

This is exactly the coordinatewise characterization of an ordinary sunflower of \(r-1\) sets. ∎

Consequently, if \(\mathcal F\) is \(r\)-near-sunflower-free and \(A_0\in\mathcal F\), then

\[
\{A\triangle A_0:A\in\mathcal F\setminus\{A_0\}\}
\]

contains no ordinary sunflower of size \(r-1\).

The difference sets are generally nonuniform, but they satisfy the balancing condition

\[
\bigl|(A\triangle A_0)\cap A_0\bigr|
 =
\bigl|(A\triangle A_0)\setminus A_0\bigr|.
\]

---

## 3. A sharper general factorial upper bound

I use the standard Erdős–Rado sunflower lemma in the following form.

### Lemma 3.1

If a \(t\)-uniform family contains no ordinary sunflower of size \(p\), then

\[
|\mathcal H|\le t!(p-1)^t.
\]

For completeness, this follows by induction on \(t\): a maximal matching has fewer than \(p\) members, its union has size at most \((p-1)t\), and some point lies in more than a \(1/((p-1)t)\)-fraction of the family. Passing to its link completes the induction.

### Proposition 3.2

For every \(r\ge4\) and \(k\ge1\),

\[
\boxed{
f_r(k)\le
\sum_{s=0}^k \binom{k}{s}s!(r-2)^s
=
\sum_{s=0}^k (k)_s(r-2)^s
}
\]

where \((k)_s=k!/(k-s)!\). In particular,

\[
\boxed{
f_r(k)\le
e^{1/(r-2)}(r-2)^k k!.
}
\]

### Proof

Fix \(A_0\in\mathcal F\). For \(X\subseteq A_0\), define

\[
\mathcal Y_X=
\left\{
A\setminus A_0:
A\in\mathcal F,\ A_0\setminus A=X
\right\}.
\]

If \(|X|=s\), then every member of \(\mathcal Y_X\) has size \(s\), since all members of \(\mathcal F\) have size \(k\).

Suppose \(Y_1,\dots,Y_{r-1}\in\mathcal Y_X\) formed an ordinary sunflower. The corresponding symmetric differences are

\[
D_i=X\cup Y_i.
\]

Since \(X\) is common to all of them and is disjoint from every \(Y_i\), the sets \(D_1,\dots,D_{r-1}\) would form an ordinary sunflower. Lemma 2.1 would then give an \(r\)-near-sunflower in \(\mathcal F\), a contradiction.

Thus \(\mathcal Y_X\) contains no \((r-1)\)-sunflower. Lemma 3.1 gives

\[
|\mathcal Y_X|\le s!(r-2)^s.
\]

There are \(\binom{k}{s}\) possible \(X\)'s of size \(s\). Summing over \(s\) proves the first bound.

Writing \(a=r-2\) and substituting \(j=k-s\),

\[
\sum_{s=0}^k (k)_s a^s
=
k!a^k\sum_{j=0}^k \frac{1}{j!a^j}
\le
e^{1/a}k!a^k.
\]

∎

This improves the direct classical estimate

\[
f_r(k)\le k!(r-1)^k,
\]

which follows merely because every ordinary \(r\)-sunflower is an \(r\)-near-sunflower. It does not, however, remove the factorial.

---

## 4. Two regimes where the conjectured exponential form holds

### 4.1 Families lying in a small Johnson ball

The proof of Proposition 3.2 gives a more precise local statement.

### Proposition 4.1

Suppose \(A_0\in\mathcal F\) and

\[
|A\setminus A_0|\le \lambda
\qquad\text{for every }A\in\mathcal F.
\]

If \(\mathcal F\) is \(r\)-near-sunflower-free, then

\[
\boxed{
|\mathcal F|
\le
\sum_{s=0}^{\lambda}(k)_s(r-2)^s.
}
\]

In particular, if

\[
\lambda\le \frac{k}{\log k},
\]

then

\[
|\mathcal F|\le C_r^k
\]

for a constant \(C_r\) depending only on \(r\).

### Proof

Only fibers with \(|X|\le\lambda\) occur in the proof of Proposition 3.2. Moreover,

\[
|\mathcal F|
\le
(\lambda+1)\bigl((r-2)k\bigr)^\lambda.
\]

For \(\lambda\le k/\log k\),

\[
\log |\mathcal F|
\le
\log(k+1)
+\frac{k}{\log k}\bigl(\log k+\log(r-2)\bigr)
=O_r(k).
\]

∎

Thus the conjecture holds for families of Johnson diameter \(O(k/\log k)\) around one of their members.

---

### 4.2 Families with uniformly small pairwise intersections

### Proposition 4.2

Let \(\mathcal F\) be \(k\)-uniform, \(r\)-near-sunflower-free, and suppose

\[
|A\cap B|\le\lambda
\qquad\text{for all distinct }A,B\in\mathcal F.
\]

Then

\[
\boxed{
|\mathcal F|
\le
(r-1)^{\lambda+1}(k)_\lambda.
}
\]

Consequently, if \(\lambda\le k/\log k\), then

\[
|\mathcal F|\le C_r^k.
\]

### Proof

It is enough to prove the assertion for an ordinary \(r\)-sunflower-free family, since an ordinary sunflower is a near-sunflower.

Let \(g_r(k,\lambda)\) denote the maximum size under these two conditions. For \(\lambda=0\), the sets are pairwise disjoint, so there can be at most \(r-1\) of them:

\[
g_r(k,0)\le r-1.
\]

For \(\lambda\ge1\), choose a maximal matching
\(M_1,\dots,M_t\subseteq\mathcal F\). Since \(r\) pairwise disjoint sets form a sunflower,

\[
t\le r-1.
\]

The union

\[
T=M_1\cup\cdots\cup M_t
\]

has size at most \((r-1)k\) and meets every member of \(\mathcal F\).

For \(x\in T\), the link

\[
\mathcal F_x=\{A\setminus\{x\}:A\in\mathcal F,\ x\in A\}
\]

is \((k-1)\)-uniform, contains no \(r\)-sunflower, and has pairwise intersections at most \(\lambda-1\). Therefore

\[
|\mathcal F|
\le
\sum_{x\in T}|\mathcal F_x|
\le
(r-1)k\,g_r(k-1,\lambda-1).
\]

Induction gives

\[
g_r(k,\lambda)
\le
(r-1)^{\lambda+1}(k)_\lambda.
\]

The exponential corollary follows from

\[
\log |\mathcal F|
\le
(\lambda+1)\log(r-1)+\lambda\log k
=O_r(k)
\]

when \(\lambda\le k/\log k\). ∎

For fixed \(\lambda\), this is the polynomial bound

\[
|\mathcal F|=O_{r,\lambda}(k^\lambda).
\]

---

## 5. Exact determination in rank two

The conjecture can be solved exactly for \(k=2\).

### Theorem 5.1

For every \(r\ge4\),

\[
\boxed{f_r(2)=(r-1)^2.}
\]

Also \(f_3(2)=2\).

### Proof

A \(2\)-uniform family is the edge set of a finite simple graph \(G\). Consider \(r\) selected edges and let \(d(v)\) be the degree of \(v\) in the selected subgraph. They form a near-sunflower precisely when every positive degree belongs to

\[
\{1,r-1,r\}.
\]

Since the degree sum is \(2r\), for \(r\ge4\) the possible selected subgraphs are exactly:

1. a matching of size \(r\);
2. a star \(K_{1,r}\);
3. a disjoint union \(K_{1,r-1}\sqcup K_2\).

Indeed, if \(a,b,c\) are the numbers of vertices of degrees \(r,r-1,1\), then

\[
ar+b(r-1)+c=2r.
\]

A degree-\(r\) vertex is incident with all selected edges, so no second vertex can have degree \(r-1\). If there is no degree-\(r\) vertex, then \(b\le2\). The cases \(b=0,1\) give the matching and \(K_{1,r-1}\sqcup K_2\), respectively. If \(b=2\), the two high-degree vertices require \(2r-2\) incidences, but \(r\) simple edges can supply at most \(r+1\) such incidences; this is impossible for \(r\ge4\).

It follows that a near-sunflower-free graph satisfies

\[
\nu(G)\le r-1,\qquad \Delta(G)\le r-1,
\]

and whenever \(d(v)=r-1\), the closed neighborhood \(N[v]\) is a vertex cover: otherwise the \(r-1\) edges at \(v\), together with an edge disjoint from \(N[v]\), give configuration 3.

If \(\Delta(G)\le r-2\), Vizing's edge-colouring theorem gives

\[
\chi'(G)\le \Delta(G)+1\le r-1.
\]

Every color class is a matching of size at most \(r-1\), and hence

\[
|E(G)|\le(r-1)^2.
\]

If \(\Delta(G)=r-1\), choose \(v\) with \(d(v)=r-1\), and put \(S=N[v]\), so \(|S|=r\). As \(S\) is a vertex cover,

\[
|E(G)|=\sum_{u\in S}d(u)-e(G[S]).
\]

Now \(\sum_{u\in S}d(u)\le r(r-1)\), while \(e(G[S])\ge r-1\), because all edges incident with \(v\) lie in \(G[S]\). Therefore

\[
|E(G)|\le r(r-1)-(r-1)=(r-1)^2.
\]

For equality, take \(G=K_{r-1,r-1}\). It has matching number and maximum degree \(r-1\), and every edge meets the closed neighborhood of any vertex. Hence none of the three listed configurations occurs. Thus it is near-sunflower-free and has \((r-1)^2\) edges.

For \(r=3\), all multiplicities \(0,1,2,3\) are allowed, so every three distinct sets form a near-sunflower and \(f_3(2)=2\). ∎

---

## 6. An exponential lower bound

The conjectured exponential scale is necessary. The following standard random-deletion argument gives explicit constants.

Fix \(q\ge2\), and represent a word \(w\in[q]^k\) by the transversal

\[
A_w=\{(i,w_i):1\le i\le k\}.
\]

These are \(k\)-uniform sets on \([k]\times[q]\).

For one coordinate, an ordered \(r\)-tuple of symbols is compatible with a near-sunflower precisely when its multiplicity partition is one of

\[
(r),\qquad (r-1,1),\qquad (1,1,\dots,1).
\]

Thus the number of allowed ordered coordinate patterns is

\[
L_r(q)=q+r q(q-1)+(q)_r,
\]

where \((q)_r=q(q-1)\cdots(q-r+1)\), interpreted as zero when \(q<r\).

### Proposition 6.1

For every fixed \(r\ge4\) and \(q\ge2\),

\[
\liminf_{k\to\infty} f_r(k)^{1/k}
\ge
\left(\frac{q^r}{L_r(q)}\right)^{1/(r-1)}
>1.
\]

### Proof

Choose each word of \([q]^k\) independently with probability \((c/q)^k\), where

\[
1<c<
\left(\frac{q^r}{L_r(q)}\right)^{1/(r-1)}.
\]

The expected number of selected words is \(c^k\). There are at most \(L_r(q)^k\) ordered near-sunflower \(r\)-tuples. Restricting to tuples of distinct words, the expected number retained is at most

\[
L_r(q)^k\left(\frac cq\right)^{kr}
=
(ca)^k,
\qquad
a=\frac{L_r(q)c^{r-1}}{q^r}<1.
\]

Deleting one word from every surviving forbidden tuple leaves a near-sunflower-free family of expected-size lower bound

\[
c^k-(ca)^k=c^k(1-a^k).
\]

Taking \(k\)-th roots and then letting \(c\) approach the displayed threshold proves the result. ∎

For example, when \(r=4\) and \(q=4\),

\[
L_4(4)=4+4\cdot4\cdot3+4!=76,
\]

so

\[
\liminf_{k\to\infty} f_4(k)^{1/k}
\ge
\left(\frac{256}{76}\right)^{1/3}
=
\left(\frac{64}{19}\right)^{1/3}
\approx1.499.
\]

No optimality is asserted.

---

## 7. Where the full argument fails

Lemma 2.1 might suggest applying an exponential ordinary sunflower bound to the difference family

\[
\{A\triangle A_0:A\in\mathcal F\setminus\{A_0\}\}.
\]

That would indeed prove the conjecture, since these differences have size at most \(2k\). However, the required exponential ordinary sunflower bound is itself the unresolved Erdős–Rado sunflower conjecture and cannot be used.

The balancing condition on the differences is not by itself enough to avoid this obstacle. If \(A_0\) is a fixed \(k\)-set and \(\mathcal G\) is any \(k\)-uniform family on a disjoint ground set, then

\[
\{A_0\cup G:G\in\mathcal G\}
\]

is balanced relative to \(A_0\), and it contains a \(p\)-sunflower exactly when \(\mathcal G\) does. Thus a proof using only “balanced and ordinary-sunflower-free” difference families would settle the ordinary sunflower conjecture.

A straightforward link induction also retains the factorial loss. Indeed, every link of a near-sunflower-free \(k\)-uniform family is near-sunflower-free of rank \(k-1\), and the family has matching number at most \(r-1\). Greedy coloring of its intersection graph therefore gives only

\[
f_r(k)
\le
(r-1)\bigl(k(f_r(k-1)-1)+1\bigr),
\]

which is of factorial rather than constant-base exponential size.

Hence the unresolved case is genuinely the heterogeneous-intersection regime: neither all sets lie in a small Johnson ball nor are all pairwise intersections \(O(k/\log k)\). The arguments above do not control that regime, so the conjecture remains open.