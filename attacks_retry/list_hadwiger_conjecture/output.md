```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For pure clique-sums of co-bipartite graphs, I obtain the sharp asymptotic extremal value 2t - (2+o(1))t log log t/log t, but the unrestricted conjecture is not resolved.",
  "would_publish": false,
  "caveats": "Restricted-class theorem; no claim of literature novelty and no general linear upper bound."
}
```

# A sharp second-order result for the class containing the pasted obstructions

I do not prove or disprove the unrestricted List Hadwiger Conjecture. I strengthen the previous attempt’s restricted-class result: its leading coefficient \(2\) can be supplemented by a sharp first lower-order term.

The clique-sum and list-amplification arguments in that attempt check out and are reproved below. The additional upper-bound ingredient is a matching argument that handles vertices in the pasting clique whose degrees need not be large.

All graphs are finite and simple, and all logarithms are natural. Write \(h(G)\) for the largest order of a complete minor and \(\operatorname{ch}(G)\) for the list chromatic number.

A graph is **co-bipartite** if its vertices can be partitioned into two cliques. Let \(\mathcal C\) consist of graphs constructed by starting with a co-bipartite graph and successively attaching co-bipartite graphs along cliques. All edges are retained, and an attachment creates no edges between its new vertices and old vertices outside the identified clique. These are the pure clique-sums considered in the previous attempt.

Define
\[
F(t)=\sup\{\operatorname{ch}(G):G\in\mathcal C,\ h(G)<t\}.
\]

## Theorem

For every integer \(t\ge2\),
\[
F(t)\le 2t-3.
\]
Moreover,
\[
\boxed{\displaystyle
F(t)=2t-(2+o(1))\,\frac{t\log\log t}{\log t}
\qquad(t\longrightarrow\infty).}
\tag{1}
\]

Thus the asymptotically optimal coefficient is \(2\) in this class, and the deficit from \(2t\) has an asymptotically determined leading term.

No claim of priority is made for this restricted-class theorem.

---

## 1. Basic clique-sum facts

### Complete minors are preserved under pure clique-sums

Suppose
\[
G=G_1\cup G_2,\qquad V(G_1)\cap V(G_2)=S,
\]
where \(S\) is a clique and there are no edges between the two sides outside \(S\). Then
\[
h(G)=\max\{h(G_1),h(G_2)\}.
\tag{2}
\]

To prove the upper bound, consider a \(K_k\)-minor model in \(G\). If every branch set meets \(S\), then \(k\le |S|\), and the clique \(S\) already supplies the required minor.

Otherwise, all branch sets disjoint from \(S\) lie in the same side, say \(G_1\): two on opposite sides could not be adjacent. Restrict each branch set meeting \(S\) to \(G_1\). Every component of its restriction meets \(S\), and the retained vertices of \(S\) form a clique, so the restriction is connected. Adjacencies to branch sets disjoint from \(S\) are retained; adjacencies between two branch sets meeting \(S\) are supplied by \(S\). This gives the model in \(G_1\).

### The elementary upper bound

Put \(p=t-1\). Every co-bipartite piece of a \(K_t\)-minor-free graph has at most \(2p\) vertices, since each of its two cliques has at most \(p\) vertices.

Consider the last attached piece \(H\), its pasting clique \(S\), and its new vertices \(U=V(H)\setminus S\). Once later attachments have been removed, vertices in \(U\) have all their neighbours in \(H\).

If \(|H|\le2p-1\), every vertex of \(U\) has degree at most \(2p-2\). If \(|H|=2p\), then \(H\) is not complete. Some nonedge has an endpoint outside \(S\), because \(S\) is a clique. Delete that endpoint first; it has degree at most \(2p-2\), and the remaining piece has at most \(2p-1\) vertices.

Removing pieces backwards therefore gives a \((2p-2)\)-degeneracy ordering. Consequently
\[
\operatorname{ch}(G)\le2p-1=2t-3.
\tag{3}
\]
In particular, \(F(t)\) is finite.

---

## 2. A tool for constructing complete minors

We will repeatedly partition a clique into small sets that dominate another specified vertex set.

### Dominating-block lemma

Let \(X,Y\) be disjoint vertex sets, with \(|Y|=N\). Suppose every vertex of \(X\) has at most \(M\) non-neighbours in \(Y\). For a positive integer \(R\le N\), there are at least
\[
\left\lfloor\frac NR\right\rfloor
\left(1-|X|\left(\frac MN\right)^R\right)
\tag{4}
\]
pairwise disjoint \(R\)-subsets of \(Y\), each of which contains a neighbour of every vertex of \(X\).

**Proof.**
Randomly permute \(Y\), split the first \(R\lfloor N/R\rfloor\) vertices into \(R\)-element blocks, and discard the remainder. For a fixed block and \(x\in X\), the probability that all its vertices are non-neighbours of \(x\) is at most \((M/N)^R\), by sampling without replacement. A union bound over \(X\), followed by expectation over the blocks, proves (4). ∎

When \(X\) and \(Y\) are cliques, singleton branch sets from \(X\), together with such dominating blocks in \(Y\), form a complete minor.

---

## 3. The sharper upper bound

Set
\[
g(x)=\frac{x\log\log x}{\log x}
\qquad(x>e).
\]

The essential statement is a rooted version of a degeneracy bound.

### Rooted block lemma

Fix \(0<\alpha<2\). For all sufficiently large integers \(p\), the following holds:

If \(H\) is co-bipartite, \(h(H)\le p\), and \(S\) is a proper clique of \(H\), then some vertex outside \(S\) has degree at most
\[
2p-2-\lfloor\alpha g(p)\rfloor.
\tag{5}
\]

### Proof

Let
\[
s=\lfloor\alpha g(p)\rfloor,\qquad D=2p-s-1.
\]
Suppose, for a contradiction, that every vertex outside \(S\) has degree at least \(D\).

Partition \(V(H)=A\cup B\) into cliques, and put
\[
a=|A|,\qquad b=|B|.
\]
Since \(h(H)\le p\),
\[
a,b\le p.
\]
Because \(S\ne V(H)\), the degree assumption gives
\[
a+b\ge D+1=2p-s.
\]
In particular,
\[
a,b\ge p-s=(1-o(1))p.
\tag{6}
\]

Define
\[
m=a+b-2p+s.
\]
Then
\[
0\le m\le s,
\]
and every vertex outside \(S\) has at most \(m\) non-neighbours in the opposite clique.

Write
\[
A_0=A\cap S,\qquad B_0=B\cap S,\qquad
a_0=|A_0|,\quad b_0=|B_0|.
\]

### 3.1. Isolating the problematic vertices

Choose a fixed \(0<\eta<1\) such that
\[
\kappa:=\frac{1-\eta}{1+\eta}>\frac{\alpha}{2}.
\tag{7}
\]
Put
\[
L=\log p,\qquad l=\log\log p,\qquad
M=\frac{p}{L^{\,1-\eta}}.
\]

Let \(Z_A\) consist of vertices of \(A\) with more than \(M\) non-neighbours in \(B\), and define \(Z_B\) symmetrically.

Since
\[
m\le s\le\alpha\frac{pl}{L}=o(M),
\]
all vertices outside \(S\) have at most \(M\) non-neighbours. Hence
\[
Z_A\subseteq A_0,\qquad Z_B\subseteq B_0.
\]

There are no nonedges between \(A_0\) and \(B_0\). Counting nonedges from \(Z_A\) to \(B\setminus S\) therefore gives
\[
M|Z_A|
\le m|B\setminus S|
\le mp.
\]
Thus
\[
|Z_A|,\ |Z_B|
\le \frac{mp}{M}
\le \alpha\,\frac{pl}{L^\eta}
=o(p).
\tag{8}
\]

### 3.2. Repairing problematic vertices by matching

Take a maximum matching from \(Z_A\) into \(B\), using edges of \(H\), and let \(d_A\) be the number of unmatched vertices of \(Z_A\). Define \(d_B\) symmetrically for a maximum matching from \(Z_B\) into \(A\).

We claim that
\[
d_A\le\min\{a_0,(m-b_0)_+\},
\qquad
d_B\le\min\{b_0,(m-a_0)_+\},
\tag{9}
\]
where \(x_+=\max\{x,0\}\).

For the first inequality, consider a nonempty \(X\subseteq Z_A\). Every vertex of \(B_0\) is adjacent to every vertex of \(X\). If \(|X|>m\), every vertex of \(B\setminus S\) also has a neighbour in \(X\), since it has at most \(m\) non-neighbours in \(A\). Thus \(N(X)=B\). By (6) and (8), \(|Z_A|<b\) for large \(p\), so such an \(X\) has no Hall deficiency.

If \(|X|\le m\), then
\[
|X|-|N(X)|\le m-b_0.
\]
The deficiency form of Hall’s theorem gives
\[
d_A\le(m-b_0)_+.
\]
Also \(d_A\le |Z_A|\le a_0\). This proves the first inequality in (9), and the other is symmetric.

The bounds imply the useful budget
\[
d_A+d_B\le m.
\tag{10}
\]
Indeed, if \(a_0+b_0\le m\), use \(d_A+d_B\le a_0+b_0\). Otherwise, if both \(a_0,b_0\le m\), use
\[
d_A+d_B\le 2m-a_0-b_0\le m.
\]
If either \(a_0\) or \(b_0\) is at least \(m\), one deficiency is zero and the other is at most \(m\).

### 3.3. Many additional branch sets

Use the matching from \(Z_A\) into \(B\). For each matched \(z\in Z_A\), make the edge joining \(z\) to its matched vertex a branch set. Every vertex of \(A\setminus Z_A\) is a singleton branch set. Discard the unmatched vertices of \(Z_A\).

This gives \(a-d_A\) pairwise adjacent branch sets. Each two-vertex branch set contains a vertex of \(B\), so it is adjacent to every unused vertex of \(B\).

Let \(Y\) be the unused part of \(B\). By (6) and (8),
\[
N:=|Y|=(1-o(1))p.
\]
Every vertex of \(A\setminus Z_A\) has at most \(M\) non-neighbours in \(Y\).

Set
\[
R=\left\lceil
\frac{1+\eta}{1-\eta}\,\frac{L}{l}
\right\rceil.
\]
Then
\[
p\left(\frac MN\right)^R
=\exp(-\eta L+o(L))
=o(1),
\tag{11}
\]
and
\[
\left\lfloor\frac NR\right\rfloor
=(\kappa+o(1))g(p).
\tag{12}
\]
The dominating-block lemma therefore supplies
\[
(\kappa-o(1))g(p)
\]
disjoint blocks in \(Y\) that dominate \(A\setminus Z_A\).

Each block is connected because \(B\) is a clique. The blocks are pairwise adjacent, adjacent to all singleton branch sets, and adjacent to all two-vertex branch sets. Hence
\[
h(H)\ge a-d_A+(\kappa-o(1))g(p).
\tag{13}
\]
Interchanging \(A\) and \(B\) gives
\[
h(H)\ge b-d_B+(\kappa-o(1))g(p).
\tag{14}
\]

All error terms here are uniform over \(H,S\): the explicit bound (8) makes \(N/p\to1\) uniformly.

Using (10), we obtain
\[
\begin{aligned}
h(H)
&\ge \max\{a-d_A,b-d_B\}+(\kappa-o(1))g(p)\\
&\ge \frac{a+b-m}{2}+(\kappa-o(1))g(p)\\
&=p-\frac{s}{2}+(\kappa-o(1))g(p)\\
&\ge p+\left(\kappa-\frac{\alpha}{2}-o(1)\right)g(p).
\end{aligned}
\]
By (7), this exceeds \(p\) for sufficiently large \(p\), a contradiction. The rooted block lemma follows. ∎

### 3.4. Applying the lemma to the clique-sum construction

Fix \(0<\alpha<2\), let \(p=t-1\), and suppose \(p\) is sufficiently large.

Remove attachments in reverse order. In the current last piece, the rooted block lemma supplies a low-degree vertex outside its pasting clique. After deleting that vertex, the remaining piece is still co-bipartite and still has Hadwiger number at most \(p\), so the lemma can be applied repeatedly.

This gives a degeneracy bound
\[
2p-2-\lfloor\alpha g(p)\rfloor.
\]
Therefore
\[
F(t)\le
2t-3-\lfloor\alpha g(t-1)\rfloor.
\tag{15}
\]
Since \(g(t-1)/g(t)\to1\),
\[
\liminf_{t\to\infty}
\frac{2t-F(t)}{g(t)}
\ge\alpha.
\]
Letting \(\alpha\uparrow2\) yields
\[
\liminf_{t\to\infty}
\frac{2t-F(t)}{g(t)}
\ge2.
\tag{16}
\]

---

## 4. A matching lower bound

The lower construction uses the previous attempt’s pasting mechanism, with an optimized minor estimate.

### 4.1. List amplification

Suppose \(H\) is partitioned into two \(n\)-vertex cliques \(A,B\), and every vertex of \(B\) has at least \(d\ge1\) neighbours in \(A\). Then there is a graph \(G\in\mathcal C\) with
\[
h(G)=h(H),\qquad \operatorname{ch}(G)\ge n+d.
\tag{17}
\]

To see this, put
\[
\ell=n+d-1.
\]
Choose disjoint colour sets \(T,P\) with
\[
|T|=\ell,\qquad |P|=n-1,
\]
and fix \(D_b\subseteq N_H(b)\cap A\) of size \(d\) for each \(b\in B\).

For every injection \(f:A\to T\), attach a fresh copy \(B_f\) of \(B\) to the common clique \(A\), with adjacencies prescribed by \(H\). Give the lists
\[
L(a)=T \quad(a\in A),\qquad
L(b_f)=P\cup f(D_b).
\]
All lists have size \(\ell\).

A proper colouring of \(A\) is an injection \(f:A\to T\). In its corresponding copy \(B_f\), every colour in \(f(D_b)\) is forbidden at \(b_f\). Thus the \(n\)-vertex clique \(B_f\) would have to use only the \(n-1\) colours of \(P\), which is impossible.

Equation (2) gives preservation of the Hadwiger number. The construction is finite: it has
\[
n\bigl(1+(\ell)_n\bigr)\le n\bigl(1+(2n)^n\bigr)
\]
vertices.

### 4.2. Random co-bipartite blocks

Take two \(n\)-vertex cliques \(A,B\), and include each cross-edge independently with probability \(1-q\), where \(0<q<1/2\).

Fix \(\varepsilon\in(0,1)\) and \(\theta>0\), and set
\[
k=\lceil(1+\varepsilon)n\rceil,\qquad
r=\left\lceil\frac{1+\theta}{\varepsilon}\right\rceil.
\]

The probability that either some vertex has fewer than \((1-2q)n\) cross-neighbours or the graph contains a \(K_k\) minor is at most
\[
2n e^{-qn/3}
+
\exp\left(
2n\log(2n+1)
-\frac{\theta}{1+\theta}\varepsilon^2q^r n^2
\right).
\tag{18}
\]

Here is a proof.

For a vertex, its number \(X\) of missing cross-edges is \(\operatorname{Bin}(n,q)\), and
\[
\Pr(X>2qn)
\le 2^{-2qn}(1+q)^n
\le e^{-(2\log2-1)qn}
\le e^{-qn/3}.
\]
A union bound proves the first term.

Now fix a candidate family of \(k\) disjoint nonempty branch sets. At least
\[
2k-2n\ge2\varepsilon n
\]
are singletons, so one clique, say \(A\), contains at least \(\varepsilon n\) singleton branch sets.

At least \(k-n\ge\varepsilon n\) branch sets lie entirely in \(B\). Fewer than
\[
\frac{n}{r+1}<\frac{\varepsilon n}{1+\theta}
\]
of them have more than \(r\) vertices. Consequently at least
\[
\frac{\theta}{1+\theta}\varepsilon n
\]
are contained in \(B\) and have size at most \(r\).

Every singleton just selected in \(A\) must have a neighbour in every such small branch set in \(B\). Each test succeeds with probability at most \(1-q^r\). The tests involve disjoint sets of random edges, so they are independent. The probability that this fixed candidate is a model is therefore at most
\[
\exp\left(
-\frac{\theta}{1+\theta}\varepsilon^2q^r n^2
\right).
\]
There are at most \((k+1)^{2n}\le(2n+1)^{2n}\) labelled candidate families, including invalid assignments. A union bound proves (18).

### 4.3. Choosing the parameters

Fix any constant \(\rho>1\), and choose
\[
0<\theta<\rho-1.
\]
For large integer \(t\), put
\[
L=\log t,\qquad l=\log\log t,
\]
\[
q=\frac1L,\qquad
\varepsilon=\rho\frac lL,\qquad
n=\left\lfloor\frac{t}{1+\varepsilon}\right\rfloor.
\]
Then
\[
k=\lceil(1+\varepsilon)n\rceil\le t.
\]

Let
\[
\lambda=\frac{1+\theta}{\rho}<1.
\]
Since
\[
r\le \lambda\frac Ll+1,
\]
we have
\[
q^r\ge \frac{t^{-\lambda}}L.
\]
Also \(n\ge t/2\) for sufficiently large \(t\). Therefore the negative term in the second exponent of (18) is at least a positive constant times
\[
\frac{t^{2-\lambda}l^2}{L^3}.
\]
This dominates \(t\log t\), because \(1-\lambda>0\). The first term of (18) also tends to zero. Thus, for every sufficiently large \(t\), there exists a block \(H\) with

* \(h(H)<k\le t\);
* every vertex having at least \((1-2q)n\) cross-neighbours.

Apply list amplification with
\[
d=\lfloor(1-2q)n\rfloor.
\]
The resulting \(K_t\)-minor-free graph \(G\in\mathcal C\) satisfies
\[
\begin{aligned}
\operatorname{ch}(G)
&\ge n+d\\
&\ge (2-2q)n-1\\
&\ge \frac{2-2q}{1+\varepsilon}\,t-3\\
&\ge 2t-2(\varepsilon+q)t-3\\
&=2t-(2\rho+o(1))g(t).
\end{aligned}
\tag{19}
\]
Consequently
\[
\limsup_{t\to\infty}
\frac{2t-F(t)}{g(t)}
\le2\rho.
\]
Since \(\rho>1\) was arbitrary,
\[
\limsup_{t\to\infty}
\frac{2t-F(t)}{g(t)}
\le2.
\tag{20}
\]

Combining (16) and (20) proves (1).

---

## 5. What this does—and does not—settle

This proves a sharp quantitative result for the class containing the pasted co-bipartite obstructions:

\[
F(t)=2t-(2+o(1))\frac{t\log\log t}{\log t}.
\]

The leading-constant lower bound \(2\) is not being claimed as new; it is already present in the supplied context. The refinement here is the matching second-order analysis for \(\mathcal C\).

The argument does **not** extend automatically to arbitrary \(K_t\)-minor-free graphs. Its upper bound uses two specific structural facts:

1. every block consists of two cliques, each of order at most \(t-1\);
2. at a pasting clique, problematic vertices can be repaired by matchings whose two deficiencies have a controlled total.

An arbitrary minor-free graph need not admit this decomposition. Thus no universal linear upper bound for the original problem, and no counterexample to the existence of such a bound, has been established.