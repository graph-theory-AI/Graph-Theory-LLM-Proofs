```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove that every q-dichromatic member of C3 has Omega(q^2 log q) vertices, but do not obtain a smaller construction.",
  "would_publish": false,
  "caveats": "This is an intrinsic lower-bound result, possibly already known; it does not improve the source construction's upper bound or verify its exact recurrence."
}
```

# A logarithmic strengthening of the order lower bound

Let \(\vec\chi(D)\) denote the dichromatic number of an oriented graph \(D\): the minimum number of parts in a partition of \(V(D)\) into acyclic sets. All logarithms below are natural.

The following partial result is unconditional and does not depend on the interpretation of Lemma 3 or of the size expression in the catalog.

## Theorem

Let \(D\) be an oriented graph with no transitive triangle, and let \(N=|V(D)|\ge 2\). Then
\[
\vec\chi(D)\le 1+64\sqrt{\frac{N}{\log N}}.
\tag{1}
\]
Consequently, if \(\vec\chi(D)\ge q\ge2\), then
\[
N\ge \frac{(q-1)^2\log q}{4096}.
\tag{2}
\]
One also has the finite bound
\[
N\ge q^2-1.
\tag{3}
\]

In particular, these statements hold for every member of \(\mathcal C_3\), giving
\[
\min\{|V(D)|:D\in\mathcal C_3,\ \vec\chi(D)\ge q\}
=\Omega(q^2\log q).
\tag{4}
\]

This improves the asymptotic quadratic lower bound in the previous attempt by a logarithmic factor. It does **not** improve the construction’s upper bound. I make no claim that (4) is new in the literature.

The proof is self-contained. Its principal ingredient is an independent-set estimate for locally bipartite graphs.

---

## 1. Local structure

### Lemma 1

If \(D\) has no transitive triangle, then, for every vertex \(v\),

* \(N^+(v)\) and \(N^-(v)\) are stable sets;
* every arc between these two sets is directed from \(N^+(v)\) to \(N^-(v)\).

Thus the underlying graph of \(D\) is locally bipartite, and \(D[N(v)]\) is acyclic.

### Proof

An edge between two out-neighbors of \(v\) would form a transitive triangle with source \(v\). The analogous argument applies to two in-neighbors.

Now take \(x\in N^+(v)\) and \(y\in N^-(v)\). If \(y\to x\), then
\[
y\to v\to x,\qquad y\to x
\]
is a transitive triangle. Therefore any edge between \(x\) and \(y\) must be directed \(x\to y\). ∎

This verifies and strengthens the relevant neighborhood observation from the previous attempt: the acyclicity of \(N(v)\) does not require the additional induced-cycle restriction defining \(\mathcal C_3\).

---

## 2. Independent sets in locally bipartite graphs

We will prove the following estimate without invoking an external coloring or Ramsey theorem.

### Lemma 2

Let \(G\) be a graph on \(M\) vertices such that every open neighborhood induces a bipartite graph. If its maximum degree is \(\Delta\ge2\), then
\[
\alpha(G)\ge \frac{M\log\Delta}{48\Delta}.
\tag{5}
\]

### 2.1. A calculation for bipartite graphs

For a graph \(F\), define its independent-set partition function by
\[
Z_F(t)=\sum_{\substack{J\subseteq V(F)\\J\text{ independent}}}t^{|J|}.
\]
Suppose that \(F\) is bipartite on \(m\) vertices. Let \(J\) be uniformly distributed over its independent sets, and put
\[
\mu_F=\mathbb E|J|.
\]

We claim that
\[
\mu_F\ge \frac m{12}
\quad\text{and hence}\quad
\mu_F\ge \frac{\log Z_F(1)}{12}.
\tag{6}
\]

Indeed, one side of a bipartition has at least \(m/2\) vertices, so
\[
Z_F(1)\ge 2^{m/2}.
\]
Also,
\[
Z_F(1/4)\le (5/4)^m,
\]
by summing over all subsets rather than only independent subsets. Jensen's inequality gives
\[
\frac{Z_F(1/4)}{Z_F(1)}
=\mathbb E\,4^{-|J|}
\ge 4^{-\mu_F}.
\]
Therefore
\[
\mu_F
\ge
\frac{\log Z_F(1)-\log Z_F(1/4)}{\log4}
\ge
m\frac{\frac12\log2-\log(5/4)}{\log4}
\ge \frac m{12}.
\]
The last numerical inequality is equivalent to \(2^7\ge5^3\). Finally,
\[
\log Z_F(1)\le m\log2\le m,
\]
which proves (6). The calculation also applies when \(m=0\).

### 2.2. Conditioning on the exterior of a neighborhood

Choose an independent set \(I\) of \(G\) uniformly at random. Write
\[
p=\frac{\mathbb E|I|}{M}.
\]

Fix \(v\), and condition on \(I\setminus N[v]\). Let \(F_v\) be the graph induced by those vertices of \(N(v)\) having no neighbor in this conditioned exterior set. Since \(G[N(v)]\) is bipartite, so is \(F_v\).

The possible choices inside \(N[v]\) are precisely:

* the singleton \(\{v\}\); or
* an independent set of \(F_v\), with \(v\) omitted.

Put \(Z_v=Z_{F_v}(1)\). Conditional on the exterior,
\[
\Pr(v\in I)=\frac1{1+Z_v}
\tag{7}
\]
and
\[
\mathbb E\bigl[|I\cap N(v)|\bigr]
=\frac{Z_v}{1+Z_v}\mu_{F_v}
\ge \frac{\log Z_v}{24},
\tag{8}
\]
using \(Z_v\ge1\) and (6).

Let
\[
L=\frac1M\sum_{v\in V(G)}\mathbb E[\log Z_v].
\]
Averaging (7), and applying Jensen's inequality, yields
\[
p
\ge \frac12\cdot\frac1M\sum_v\mathbb E[Z_v^{-1}]
\ge \frac12 e^{-L}.
\tag{9}
\]
On the other hand, (8) and double counting give
\[
\frac L{24}
\le \frac1M\sum_v\mathbb E|I\cap N(v)|
=\frac1M\sum_u d(u)\Pr(u\in I)
\le \Delta p.
\]
Thus
\[
p\ge \frac12 e^{-24\Delta p}.
\tag{10}
\]

If \(p<\log\Delta/(48\Delta)\), then (10) implies
\[
p>\frac1{2\sqrt\Delta}
\ge \frac{\log\Delta}{48\Delta},
\]
a contradiction. Here the last inequality follows, for example, from
\(\log x\le\sqrt x\) for \(x\ge1\). Hence
\[
p\ge\frac{\log\Delta}{48\Delta}.
\]
Since a largest independent set is at least as large as the expected size of \(I\), this proves Lemma 2. ∎

---

## 3. A large acyclic set

### Lemma 3

Every transitive-triangle-free oriented graph \(D\) on \(n\ge2\) vertices has an acyclic vertex set of size at least
\[
\frac1{16}\sqrt{n\log n}.
\tag{11}
\]

### Proof

Let \(\Delta\) be the maximum degree of the underlying graph, and let \(A\) be the maximum size of an acyclic set in \(D\). By Lemma 1,
\[
A\ge\Delta.
\tag{12}
\]
Also \(A\ge\alpha(G)\), where \(G\) is the underlying graph.

If \(\Delta\le n^{1/4}\), the elementary greedy independent-set bound gives
\[
A\ge\frac n{\Delta+1}
\ge \frac12 n^{3/4}
\ge\frac1{16}\sqrt{n\log n}.
\]
The last inequality follows from \(\log n\le\sqrt n\).

Otherwise, \(\Delta>n^{1/4}\), so \(\Delta\ge2\). Lemma 2 gives
\[
A\ge\alpha(G)
\ge\frac{n\log\Delta}{48\Delta}
>\frac{n\log n}{192\Delta}.
\]
Together with (12), this implies
\[
A\ge
\max\left\{\Delta,\frac{n\log n}{192\Delta}\right\}
\ge\sqrt{\frac{n\log n}{192}}
\ge\frac1{16}\sqrt{n\log n}.
\]
This proves (11). ∎

---

## 4. Partitioning into acyclic sets

We now prove (1). Define
\[
f(x)=\frac1{16}\sqrt{x\log x}\qquad(x>1).
\]
Repeatedly remove an acyclic set supplied by Lemma 3 and assign it a new color. The absence of transitive triangles is hereditary, so the lemma remains applicable.

The function \(f\) is increasing. If a removal reduces the number of remaining vertices from \(m\) to \(m'\ge1\), then
\[
\int_{m'}^m\frac{dx}{f(x)}
\ge \frac{m-m'}{f(m)}
\ge1.
\]
Charging all but the final color in this way gives
\[
\vec\chi(D)
\le 1+16\int_1^N\frac{dx}{\sqrt{x\log x}}.
\tag{13}
\]
The integral is finite at its lower endpoint.

Set \(a=\sqrt{\log N}\), and substitute \(x=e^{t^2}\). Then
\[
16\int_1^N\frac{dx}{\sqrt{x\log x}}
=32\int_0^a e^{t^2/2}\,dt.
\]
For \(0\le t\le a\),
\[
a^2-t^2\ge a(a-t).
\]
Consequently,
\[
\begin{aligned}
\int_0^a e^{t^2/2}\,dt
&\le e^{a^2/2}\int_0^a e^{-a(a-t)/2}\,dt\\
&\le \frac{2e^{a^2/2}}a.
\end{aligned}
\]
Substituting into (13) proves
\[
\vec\chi(D)\le1+64\sqrt{\frac N{\log N}}.
\]

If \(\vec\chi(D)\ge q\ge2\), it follows that
\[
N\ge \frac{(q-1)^2\log N}{4096}
\ge \frac{(q-1)^2\log q}{4096},
\]
where the final inequality uses \(N\ge q\). This proves (2).

---

## 5. The finite quadratic estimate

For completeness, the same local observation also improves the constant in the previous attempt's elementary quadratic bound.

We prove \(N\ge q^2-1\) by induction on \(q\). For \(q=2\), an oriented graph containing a directed cycle has at least three vertices.

For \(q\ge3\), pass to an induced subdigraph minimal with dichromatic number at least \(q\). It has dichromatic number exactly \(q\). Every vertex \(v\) satisfies
\[
d^+(v)\ge q-1,\qquad d^-(v)\ge q-1.
\tag{14}
\]
Indeed, color \(D-v\) acyclically with \(q-1\) colors. If some color is absent from \(N^+(v)\), assigning that color to \(v\) cannot create a monochromatic directed cycle. This proves the out-degree assertion; the in-degree assertion is symmetric.

By Lemma 1, \(N(v)\) is acyclic. Moreover, \(v\) is isolated in \(D-N(v)\). Therefore
\[
q\le 1+\max\{1,\vec\chi(D-N[v])\}.
\]
Since \(q\ge3\), the graph \(D-N[v]\) has dichromatic number at least \(q-1\). By induction and (14),
\[
\begin{aligned}
|V(D)|
&\ge |N(v)|+1+|V(D-N[v])|\\
&\ge 2(q-1)+1+\bigl((q-1)^2-1\bigr)\\
&=q^2-1.
\end{aligned}
\]
This proves (3).

---

## 6. Consequences for the catalog problem, and the remaining gap

Writing
\[
s_{\mathcal C_3}(q)
=\min\{|V(D)|:D\in\mathcal C_3,\ \vec\chi(D)\ge q\},
\]
the proved estimates give
\[
s_{\mathcal C_3}(q)\ge
\max\left\{
q^2-1,\,
\frac{(q-1)^2\log q}{4096}
\right\}.
\]
In particular, every \((k+1)\)-dichromatic example in \(\mathcal C_3\) has at least
\[
\frac{k^2\log(k+1)}{4096}
\]
vertices.

The distinction from the requested improvement is important:

* This is a lower bound in the **target dichromatic number**.
* It is not an improved upper-bound recurrence from \(|G_k|\) to \(|G_{k+1}|\).
* No smaller \((k+1)\)-dichromatic construction in \(\mathcal C_3\) is produced.
* The conditional high-girth interpretation of the source's Lemma 3 is not used.

Thus the construction-size question remains unresolved here. The completed partial result is the self-contained logarithmic strengthening of the intrinsic order lower bound, valid even without the induced-directed-cycle restriction.