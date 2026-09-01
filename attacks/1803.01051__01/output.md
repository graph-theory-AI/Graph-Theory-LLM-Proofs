```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "No general resolution is obtained, but matching and kernel-orientation arguments prove the bound for several substantial special classes and sharply constrain the first unresolved parameter case.",
  "would_publish": false,
  "caveats": "No general case is settled; the asymptotic and planar corollaries invoke established external theorems, and novelty is not claimed."
}
```

# Mathematical writeup

## 1. Statement and notation

Let \(G\) be a finite simple graph, and write
\[
d=\Delta(G),\qquad w=\omega(G),\qquad
R(G)=\left\lceil\frac{d+1+w}{2}\right\rceil .
\]
The proposed list-Reed inequality is
\[
\chi_\ell(G)\le R(G). \tag{LR}
\]

It is enough to work with the actual values \(d,w\), since the right-hand side is monotone in any advertised upper bounds on them. Also, the problem is componentwise: both \(\chi_\ell\) and the relevant local parameters are monotone under taking components.

I do not obtain a proof or counterexample in general. I prove the following special cases.

### Partial theorem

The inequality (LR) holds in each of the following situations.

1. \(w\ge d-2\). In particular, it holds for every graph with \(d\le4\).
2. \(G\) is bipartite; in fact,
   \[
   \chi_\ell(G)\le \left\lceil\frac d2\right\rceil+1.
   \]
3. More generally, \(G\) has an odd-cycle transversal of size at most \(w-1\).
4. \(|V(G)|\le d+2\). More generally, it suffices that
   \[
   \nu(\overline G)\ge |V(G)|-R(G),
   \]
   where \(\nu\) denotes matching number.
5. \(G\) is planar.
6. Under the sufficiently-large-degree hypothesis of the source paper, (LR) holds whenever
   \[
   d\ge (w+1)^{20736}.
   \]

In addition, any hypothetical counterexample with \(d=5,w=2\) has a list-critical induced subgraph on at least \(11\) vertices, of minimum degree \(4\), with further structure described below.

---

## 2. A matching bound for arbitrary graphs

We first prove a useful general list-coloring bound.

### Lemma 2.1

If \(G\) has \(n\) vertices and \(\overline G\) contains a matching of size \(p\), then
\[
\chi_\ell(G)\le n-p. \tag{1}
\]

#### Proof

Fix a matching
\[
M=\{u_1v_1,\ldots,u_pv_p\}
\]
in \(\overline G\). Thus each \(u_iv_i\) is a nonedge of \(G\).

We induct on \(n\). Let every vertex have a list of size
\[
k=n-p.
\]
If the family of lists has a system of distinct representatives, assigning distinct colors gives a proper coloring.

Otherwise, Hall's theorem gives \(X\subseteq V(G)\) such that
\[
\left|\bigcup_{x\in X}L(x)\right|<|X|.
\]
Since each individual list has size \(k\), we have
\[
|X|\ge k+1=n-p+1,
\]
and hence
\[
|V(G)\setminus X|\le p-1.
\]
Consequently, some matched pair \(u_iv_i\) lies entirely in \(X\), since otherwise the \(p\) matching edges would require at least \(p\) distinct vertices outside \(X\).

Let \(U=\bigcup_{x\in X}L(x)\). Then
\[
\begin{aligned}
|L(u_i)\cap L(v_i)|
&\ge |L(u_i)|+|L(v_i)|-|U|\\
&\ge 2(n-p)-(n-1)\\
&=n-2p+1\ge1.
\end{aligned}
\]
Choose \(c\in L(u_i)\cap L(v_i)\) and color both \(u_i,v_i\) with \(c\); this is proper because \(u_iv_i\notin E(G)\).

Delete \(u_i,v_i\), and delete \(c\) from all remaining lists. The resulting lists have size at least
\[
k-1=(n-2)-(p-1),
\]
and the remaining \(p-1\) pairs form a matching in the complement of the remaining graph. Induction completes the coloring. ∎

### Corollary 2.2

For every \(n\)-vertex graph,
\[
\chi_\ell(G)\le n-\nu(\overline G)
            \le \left\lfloor\frac{n+w}{2}\right\rfloor. \tag{2}
\]

#### Proof

Let \(p=\nu(\overline G)\). The vertices unmatched by a maximum matching form an independent set in \(\overline G\), hence a clique in \(G\). Therefore
\[
n-2p\le w,
\]
so \(p\ge\lceil(n-w)/2\rceil\). Apply Lemma 2.1. ∎

If \(n\le d+2\), then
\[
\chi_\ell(G)
 \le \left\lfloor\frac{n+w}{2}\right\rfloor
 \le \left\lfloor\frac{d+2+w}{2}\right\rfloor
 =\left\lceil\frac{d+1+w}{2}\right\rceil.
\]
Thus (LR) holds whenever \(n\le d+2\). The same calculation also covers \(n=d+3\) when \(d+w\) is even.

The direct matching condition
\[
\nu(\overline G)\ge n-R(G)
\]
is a polynomially checkable sufficient certificate for (LR), and can hold well beyond the order bound above.

---

## 3. Kernel orientations and the bipartite case

A kernel in a digraph \(D\) is an independent set \(K\) such that every vertex outside \(K\) has an outgoing arc to a vertex of \(K\). An orientation is kernel-perfect if every induced subdigraph has a kernel.

We use two standard facts:

- Richardson's kernel theorem: every digraph with no directed odd cycle has a kernel.
- Consequently, every orientation of a bipartite graph is kernel-perfect.

### Lemma 3.1 — Kernel lemma

Let \(D\) be a kernel-perfect orientation of \(G\). If
\[
|L(v)|\ge d_D^+(v)+1
\]
for every vertex \(v\), then \(G\) is \(L\)-colorable.

#### Proof

Choose a color \(c\) appearing in some list, and let
\[
X=\{v:c\in L(v)\}.
\]
Take a kernel \(K\) of \(D[X]\), and color every vertex of \(K\) with \(c\). This is proper because \(K\) is independent.

Delete \(K\), and delete \(c\) from all remaining lists. If \(v\in X\setminus K\), then \(v\) has an outgoing arc to \(K\), so its outdegree drops by at least one while its list loses one color. If \(v\notin X\), its list does not shrink. Thus the same list-size inequality holds in the remaining induced orientation. Induction on \(|V(G)|\) finishes the proof. ∎

### Lemma 3.2 — Balanced orientation

Every graph has an orientation satisfying
\[
d_D^+(v)\le \left\lceil\frac{d_G(v)}2\right\rceil
\]
at every vertex.

#### Proof

Add one auxiliary vertex adjacent to every odd-degree vertex. All degrees in the resulting graph are even. Orient each Eulerian component along an Euler tour, and then delete the auxiliary vertex. ∎

### Proposition 3.3 — Bipartite bound

If \(G\) is bipartite, then
\[
\chi_\ell(G)\le \left\lceil\frac d2\right\rceil+1. \tag{3}
\]

#### Proof

Use a balanced orientation. It is kernel-perfect because the underlying graph is bipartite. Lemma 3.1 applies. ∎

For a nonempty bipartite graph, \(w=2\). If \(d=2m\), the conjectured right-hand side is \(m+2\), while (3) gives \(m+1\). If \(d=2m+1\), both bounds equal \(m+2\). Thus every bipartite graph satisfies (LR).

---

## 4. An odd-cycle-transversal extension

The preceding argument extends beyond bipartite graphs.

### Proposition 4.1

Let \(S\subseteq V(G)\) be such that \(H=G-S\) is bipartite, and put
\[
\rho=\max_{x\in V(H)}|N_G(x)\cap S|.
\]
Then
\[
\chi_\ell(G)\le
\max\left\{\chi_\ell(G[S]),\,
1+\left\lceil\frac{d+\rho}{2}\right\rceil\right\}. \tag{4}
\]

#### Proof

Let
\[
q=\max\left\{\chi_\ell(G[S]),\,
1+\left\lceil\frac{d+\rho}{2}\right\rceil\right\},
\]
and give every vertex a list of size \(q\).

First color \(G[S]\). For \(x\in H\), let
\[
s_x=|N_G(x)\cap S|.
\]
After deleting from \(L(x)\) the colors used on its neighbors in \(S\), at least \(q-s_x\) colors remain.

Orient \(H\) in a balanced way. Since
\[
d_H(x)\le d-s_x
\]
and \(s_x\le\rho\),
\[
\begin{aligned}
s_x+\left\lceil\frac{d_H(x)}2\right\rceil
&\le s_x+\left\lceil\frac{d-s_x}{2}\right\rceil\\
&=\left\lceil\frac{d+s_x}{2}\right\rceil\\
&\le\left\lceil\frac{d+\rho}{2}\right\rceil.
\end{aligned}
\]
Therefore the residual list at \(x\) has size at least
\[
1+\left\lceil\frac{d_H(x)}2\right\rceil
\ge d_D^+(x)+1.
\]
The kernel lemma colors \(H\), completing the coloring of \(G\). ∎

Let \(\tau_{\rm odd}(G)\) be the minimum size of an odd-cycle transversal. Taking \(|S|=\tau\), using \(\chi_\ell(G[S])\le\tau\) and \(\rho\le\tau\), gives
\[
\chi_\ell(G)\le
\max\left\{\tau,\,
1+\left\lceil\frac{d+\tau}{2}\right\rceil\right\}. \tag{5}
\]

### Corollary 4.2

If
\[
\tau_{\rm odd}(G)\le w-1,
\]
then \(G\) satisfies (LR).

#### Proof

Since \(d\ge w-1\), we have \(R(G)\ge w\), so the first term in (5) is at most \(R(G)\). Moreover,
\[
1+\left\lceil\frac{d+\tau}{2}\right\rceil
=\left\lceil\frac{d+\tau+2}{2}\right\rceil
\le\left\lceil\frac{d+w+1}{2}\right\rceil=R(G).
\]
∎

The ceiling also permits the boundary case \(\tau_{\rm odd}(G)=w\) when \(d+w\) is even.

A stronger useful formulation follows directly from Proposition 4.1: it suffices to find an odd-cycle transversal \(S\) such that
\[
\chi_\ell(G[S])\le R(G)
\quad\text{and}\quad
\max_{x\notin S}|N(x)\cap S|\le w-1.
\]

---

## 5. The near-clique range

We use the standard list version of Brooks' theorem: a connected graph of maximum degree \(d\) is \(d\)-choosable unless it is \(K_{d+1}\), or \(d=2\) and it is an odd cycle.

If \(w\ge d-2\), then
\[
R(G)=\left\lceil\frac{d+1+w}{2}\right\rceil\ge d.
\]
Thus list Brooks proves (LR), apart from its two exceptional configurations. They also satisfy the desired bound exactly:

- \(K_{d+1}\) has \(w=d+1\) and \(\chi_\ell=d+1=R(G)\);
- an odd cycle has \(d=w=2\) and \(\chi_\ell=3=R(G)\).

Hence (LR) holds whenever \(w\ge d-2\). Since every nonempty graph with \(d\le4\) has \(w\ge2\ge d-2\), this proves all maximum degrees at most four.

---

## 6. Planar graphs

Every planar graph satisfies (LR).

Indeed, invoke the classical theorem that every planar graph is \(5\)-choosable.

- If \(d\ge6\), then \(w\ge2\) and
  \[
  R(G)\ge\left\lceil\frac{d+3}{2}\right\rceil\ge5.
  \]
- If \(d=5\) and \(w\ge3\), then \(R(G)\ge5\).
- If \(d=5,w=2\), then \(G\) is triangle-free planar. Every subgraph \(F\) with at least three vertices satisfies
  \[
  |E(F)|\le2|V(F)|-4,
  \]
  so \(F\) has a vertex of degree at most three. Thus \(G\) is \(3\)-degenerate and hence \(4\)-choosable. Here \(R(G)=4\).
- The cases \(d\le4\) were handled above.

This planar consequence is standard rather than a new resolution mechanism.

---

## 7. The low-clique asymptotic region from the source paper

The source paper proves, for sufficiently large \(d\), a correspondence-coloring bound that implies
\[
\chi_\ell(G)
 \le 72d\sqrt{\frac{\ln(w+1)}{\ln d}}. \tag{6}
\]
I have used \(w+1\) as the forbidden-clique parameter, avoiding any convention issue between “clique number at most \(w\)” and “\(K_{w+1}\)-free.”

If
\[
d\ge (w+1)^{20736},
\]
then
\[
\sqrt{\frac{\ln(w+1)}{\ln d}}\le\frac1{144},
\]
and (6) gives
\[
\chi_\ell(G)\le \frac d2<R(G).
\]
Thus, subject to the source theorem's unspecified sufficiently-large threshold, the conjecture holds throughout this explicit low-clique region. This is a direct consequence of the source paper, not a new theorem.

---

## 8. Structure of a hypothetical counterexample

Let \(k=R(G)\), and suppose \(G\) is not \(k\)-choosable. Choose a bad \(k\)-list assignment and an inclusion-minimal induced subgraph \(H\) that is not colorable from the restricted assignment.

Then:

1. \(H\) is connected.
2. Every vertex of \(H\) has degree at least \(k\), since a vertex of degree at most \(k-1\) could be colored after coloring \(H-v\).
3. Let
   \[
   B=\{v\in V(H):d_H(v)=k\}.
   \]
   Every component of \(H[B]\) is a Gallai tree: each of its blocks is a clique or an odd cycle.

For the third assertion, color \(H-C\), where \(C\) is a component of \(H[B]\). Each \(v\in C\) retains at least
\[
k-(k-d_C(v))=d_C(v)
\]
colors. The degree-choosability characterization says that \(C\) would be colorable unless it were a Gallai tree.

Combining the established special cases, a general counterexample must in particular have
\[
d\ge5,\qquad 2\le w\le d-3,
\]
and cannot satisfy the complement-matching or odd-cycle-transversal criteria above.

---

## 9. The first untreated parameter pair: \(d=5,w=2\)

Here the conjectured bound is \(k=4\). If a triangle-free graph of maximum degree at most five is not \(4\)-choosable, take a minimal bad induced subgraph \(H\). Then:

- every degree in \(H\) is \(4\) or \(5\);
- the subgraph induced by the degree-four vertices is a Gallai forest whose blocks are edges or odd cycles of length at least five;
- \(H\) is nonbipartite;
- \(H\) has odd-cycle transversal number at least two;
- \(H\) is nonplanar.

There is also a small-order exclusion.

### Proposition 9.1

Every triangle-free graph of maximum degree at most five on at most ten vertices is \(4\)-choosable.

#### Proof

Suppose otherwise and take a minimal bad subgraph \(H\). It has minimum degree at least four. It cannot be bipartite by Proposition 3.3.

Let \(C\) be a shortest odd cycle in \(H\), of length \(\ell\ge5\). It is induced. Any vertex outside \(C\) has at most two neighbors on \(C\): with three neighbors, the three intervening arcs of \(C\) all have length at least two, and one has odd length at most \(\ell-4\); together with the outside vertex it would give a shorter odd cycle.

Every vertex of \(C\) has at least two neighbors outside \(C\), while each outside vertex has at most two neighbors on \(C\). Hence
\[
2\ell\le e(C,V(H)\setminus C)\le2(|V(H)|-\ell),
\]
so \(|V(H)|\ge2\ell\ge10\). With \(|V(H)|\le10\), equality holds throughout: \(|V(H)|=10\) and \(\ell=5\).

Thus every vertex of \(C\) has exactly two outside neighbors, and every outside vertex has exactly two neighbors on \(C\). Indexing \(C=c_0c_1\cdots c_4c_0\), the five possible pairs of nonconsecutive cycle vertices are
\[
\{c_{i-1},c_{i+1}\},\qquad i\in\mathbb Z_5.
\]
The cross-degree equations force exactly one outside vertex \(x_i\) with each such pair. Triangle-freeness permits edges among the \(x_i\)'s only between consecutive indices. Since every \(x_i\) has degree at least four and already has two neighbors on \(C\), the \(x_i\)'s induce a \(5\)-cycle.

Therefore \(H\) is the graph obtained by replacing each vertex of \(C_5\) by an independent pair and each edge by \(K_{2,2}\). It is \(4\)-regular and \(2\)-connected, but is neither a clique nor an odd cycle. Hence it is not a Gallai tree, contradicting the structural property of the degree-four vertices. ∎

A further counting restriction is available. Let \(a\) and \(b\) be the numbers of degree-five and degree-four vertices of a minimal obstruction, and let \(t\) be the number of components induced by the degree-four vertices. Each such component \(T\) satisfies
\[
e(T)\le\frac54(|V(T)|-1),
\]
because every odd-cycle block has length at least five. Consequently,
\[
e(A,B)=4b-2e(B)\ge \frac{3b+5t}{2}.
\]
Since \(e(A,B)\le5a\),
\[
3b+5t\le10a.
\]
In particular,
\[
\overline d(H)>4+\frac3{13}=\frac{55}{13}.
\]
This is a genuine restriction, but it does not yield a contradiction for arbitrary nonplanar triangle-free graphs.

---

## 10. Remaining gap

The kernel argument succeeds for bipartite graphs because every orientation is kernel-perfect. For a general nonbipartite graph, a balanced orientation may contain directed odd cycles, so Richardson's theorem no longer applies. The Gallai-tree structure of the degree-\(k\) vertices in a minimal list obstruction is not by itself strong enough to exclude such graphs.

Thus the argument leaves a substantial intermediate regime:
\[
d\ge5,\qquad 2\le w\le d-3,
\]
with no suitably small odd-cycle transversal or complement matching, and outside the very-low-clique asymptotic range of the source theorem. No counterexample or complete proof for that regime is obtained, and no computational enumeration is claimed.