```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The logarithmic bound holds for bipartite graphs whose tree-partition width is bounded by a fixed polynomial in the maximum degree, with a sharper bound available in terms of bandwidth.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of these special-case results has not been checked."
}
```

## 1. Statements of the partial results

All graphs below are finite. Write \(\operatorname{ch}(G)\) for the list chromatic number. The conjecture is understood for \(\Delta\ge 2\), or with \(\log(\Delta+1)\) in place of \(\log\Delta\).

A **tree partition of width \(m\)** is a partition
\[
V(G)=\bigsqcup_{t\in V(T)}X_t,\qquad |X_t|\le m,
\]
where \(T\) is a forest and every edge of \(G\) has its endpoints either in one block or in blocks indexed by adjacent vertices of \(T\). This is a partition, not merely a tree decomposition.

### Theorem 1
If \(G\) is bipartite, has maximum degree \(\Delta\), and admits a tree partition of width \(m\), then
\[
\boxed{\displaystyle
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln\!\bigl(2m(\Delta+1)-1\bigr)}
{\ln(4/3)}
\right\rceil .}
\tag{1}
\]

Consequently, for fixed constants \(C\ge1\) and \(a\ge0\), the conjectured \(O(\log\Delta)\) bound holds whenever
\[
m\le C\Delta^a.
\]
More precisely, in this class,
\[
\operatorname{ch}(G)
\le \frac{a+1}{\ln(4/3)}\ln\Delta+O_{C,a}(1).
\]

There is no restriction on the number of blocks or on \(|V(G)|\).

For an ordering \(v_1,\ldots,v_n\), its **bandwidth** is the maximum of \(|i-j|\) over edges \(v_iv_j\). The bandwidth of \(G\) is the minimum over all orderings.

### Theorem 2
Every bipartite graph of bandwidth \(b\ge2\) satisfies
\[
\boxed{\displaystyle
\operatorname{ch}(G)
\le \log_2 b+\log_2\log_2 b+O(1),}
\tag{2}
\]
where the implicit constant is absolute.

Thus, for fixed \(C,a>0\), bandwidth at most \(C\Delta^a\) implies
\[
\operatorname{ch}(G)
\le a\log_2\Delta+\log_2\log_2\Delta+O_{C,a}(1).
\]

The proofs use *local palettes*: different regions may make independent decisions about which side of the bipartition receives a color, while vertices use only colors whose local decisions are consistent.

---

## 2. A local-cover lemma

### Lemma
Let \(G\) be bipartite. Suppose there is a family \(\mathcal S\) of vertex subsets such that:

1. every vertex belongs to at least one and at most \(r\) members of \(\mathcal S\);
2. every edge has both endpoints in some member of \(\mathcal S\);
3. every member of \(\mathcal S\) has size at most \(M\).

Then
\[
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln\!\bigl(r(M-1)+1\bigr)}
{-\ln(1-2^{-r})}
\right\rceil .
\tag{3}
\]

### Proof

Fix a bipartition \(A\cup B\) and an arbitrary assignment of lists of size \(k\). Larger lists can be trimmed.

For every color \(c\) and every \(S\in\mathcal S\), independently choose a fair bit
\[
\xi_{c,S}\in\{A,B\}.
\]
Call \(c\in L(v)\) **available at \(v\)** if
\[
\xi_{c,S}=\text{the side containing }v
\quad\text{for every }S\ni v.
\]

A vertex belongs to at most \(r\) sets, so each listed color is available with probability at least \(2^{-r}\). Different colors use independent random variables. Hence the bad event \(E_v\) that \(v\) has no available color satisfies
\[
\Pr(E_v)\le (1-2^{-r})^k.
\]

Connect two bad events in a dependency graph whenever their vertices belong to a common member of \(\mathcal S\). Events not connected in this graph have disjoint sets of underlying variables. Its maximum degree is at most
\[
D=r(M-1).
\]
In particular, this dependency bound has **no factor of \(k\)**.

The symmetric Lovász local lemma guarantees that all bad events can be avoided if
\[
e(1-2^{-r})^k\bigl(r(M-1)+1\bigr)\le1.
\]
This is precisely the sufficient condition in (3).

Finally, choose any available color at each vertex. If adjacent vertices \(u\in A\) and \(v\in B\) both chose \(c\), take \(S\) containing both endpoints. Availability would require simultaneously
\[
\xi_{c,S}=A,\qquad \xi_{c,S}=B,
\]
a contradiction. Thus the coloring is proper. \(\square\)

---

## 3. Proof of Theorem 1

Root each component of the forest \(T\). For every node \(t\), define
\[
S_t=X_t\;\cup\!
\bigcup_{\substack{s\text{ a child}\\\text{of }t}}
\{v\in X_s:N_G(v)\cap X_t\ne\varnothing\}.
\]

These sets have the required properties:

- An edge inside \(X_t\) is covered by \(S_t\).
- An edge between \(X_t\) and a child block is covered by \(S_t\).
- A vertex in \(X_t\) belongs to \(S_t\), and possibly also to the set indexed by the parent of \(t\). Thus the load is at most \(2\).
- Finally,
  \[
  |S_t|
  \le |X_t|+\sum_{u\in X_t}d_G(u)
  \le m(\Delta+1).
  \]

Apply the lemma with
\[
r=2,\qquad M=m(\Delta+1).
\]
Since \(-\ln(1-2^{-2})=\ln(4/3)\), this gives (1). \(\square\)

**Extension.** The same argument works if the quotient graph of the partition admits an orientation of maximum indegree at most a fixed \(d\). Define \(S_t\) using the neighbors in blocks toward which edges are oriented. Each vertex then belongs to at most \(d+1\) sets, giving
\[
\operatorname{ch}(G)=O_d\!\left(\ln\bigl(m(\Delta+1)\bigr)\right).
\]
Thus the forest assumption can be replaced by a bounded-indegree orientation of the quotient.

---

## 4. A sharper localization argument for bandwidth

The preceding lemma uses each color at a vertex with probability at least \(1/4\). On a line, one can make that probability arbitrarily close to \(1/2\), while keeping dependencies local.

Fix an ordering \(v_1,\ldots,v_n\) of bandwidth at most \(b\), and let \(R\ge b\) be an integer. Include dummy integer positions outside \(\{1,\ldots,n\}\) so that all intervals below have their full lengths.

For every color \(c\) and position \(j\), independently choose:

- a continuous random label \(Z_{c,j}\), uniformly distributed on \([0,1]\);
- a fair bit \(\xi_{c,j}\in\{A,B\}\).

For each \(i\), put
\[
\begin{aligned}
U_i&=[i-R-b,i+R+b]\cap\mathbb Z,\\
W_i&=[i-R,i+R]\cap\mathbb Z,\\
I_i&=[i-R+b,i+R-b]\cap\mathbb Z.
\end{aligned}
\]
Let \(s_c(i)\) be the position of the minimum \(c\)-label in \(U_i\). Minima are unique with probability one.

Call \(c\in L(v_i)\) available if
\[
s_c(i)\in I_i
\quad\text{and}\quad
\xi_{c,s_c(i)}=\text{the side containing }v_i.
\tag{4}
\]

### Properness

Suppose \(v_iv_j\) is an edge. Since \(|i-j|\le b\),
\[
I_i\subseteq W_j\subseteq U_i.
\]
If \(c\) is available at \(v_i\), the minimum in \(U_i\) lies in \(I_i\), so it is also the minimum in \(W_j\).

If \(c\) is available at \(v_j\), its selected position is likewise the minimum in \(W_j\). Therefore
\[
s_c(i)=s_c(j).
\]
Because the endpoints lie on opposite sides of the bipartition, condition (4) cannot hold at both endpoints. Any choice of available colors is consequently proper.

### Availability probability

The minimum position is uniform in \(U_i\), and its bit is independent of the labels. Therefore
\[
\Pr(c\text{ is available at }v_i)
=
\frac{2(R-b)+1}{2\bigl(2(R+b)+1\bigr)}.
\]
Writing
\[
q=\frac12+\frac{2b}{2(R+b)+1},
\]
the probability that a vertex with \(k\) listed colors has none available is exactly \(q^k\).

The bad event at \(v_i\) uses variables only at positions in \(U_i\). Thus it is independent of all bad events outside index distance \(2(R+b)\), and a dependency graph has maximum degree at most \(4(R+b)\).

The local lemma now gives the explicit bound
\[
\boxed{\displaystyle
\operatorname{ch}(G)\le
\left\lceil
\frac{1+\ln\!\bigl(4(R+b)+1\bigr)}
{-\ln\!\left(\frac12+\frac{2b}{2(R+b)+1}\right)}
\right\rceil
\qquad(R\ge b).}
\tag{5}
\]

For sufficiently large \(b\), choose
\[
R=\lceil b\ln b\rceil.
\]
Then
\[
\begin{aligned}
1+\ln\!\bigl(4(R+b)+1\bigr)
   &=\ln b+\ln\ln b+O(1),\\
-\ln\!\left(\frac12+\frac{2b}{2(R+b)+1}\right)
   &=\ln2-\frac{2}{\ln b}
     +O\!\left(\frac1{(\ln b)^2}\right).
\end{aligned}
\]
Substituting in (5) yields
\[
\operatorname{ch}(G)
\le \frac{\ln b+\ln\ln b}{\ln2}+O(1),
\]
which is (2). The finitely many smaller integer values of \(b\ge2\) are absorbed into the absolute constant using (5). \(\square\)

---

## 5. Why this does not settle the conjecture

The unresolved step is not an estimate inside these proofs. It is that arbitrary bounded-degree bipartite graphs need not possess the required bounded-load, small-set covers.

There is a direct obstruction. Suppose \(G\) has girth greater than \(M\), and \(\mathcal S\) covers its edges with sets of size at most \(M\) and vertex load at most \(r\). Every \(G[S]\) is a forest, so
\[
|E(G)|
\le \sum_{S\in\mathcal S}|E(G[S])|
\le \sum_{S\in\mathcal S}(|S|-1)
\le r|V(G)|.
\tag{6}
\]
Thus such a cover is impossible when the average degree exceeds \(2r\).

For completeness, bounded-degree bipartite graphs realizing this obstruction exist with arbitrarily large prescribed girth. Fix \(d\) and \(g\), and take the union of \(d\) independent uniformly random perfect matchings between two \(n\)-vertex sets. For \(n\ge2g\), the expected number of parallel pairs and cycles of length at most \(g\) is at most
\[
\binom d2+
\sum_{\ell=2}^{\lfloor g/2\rfloor}(2d)^{2\ell}.
\]
Indeed, for a cycle of length \(2\ell\), there are at most \(n^{2\ell}d^{2\ell}\) choices of vertices and matching labels, and any consistent specification has probability at most \((n-2\ell)^{-2\ell}\).

Hence some outcome has only \(O_{d,g}(1)\) such obstructions. Deleting one edge from each leaves a simple bipartite graph with:

- maximum degree at most \(d\);
- girth greater than \(g\);
- average degree \(d-O_{d,g}(1/n)\).

Taking \(d=5\) and \(n\) sufficiently large gives average degree greater than \(4\). By (6), these graphs cannot have two-fold edge covers with uniformly bounded set size. In particular, their tree-partition widths are unbounded despite maximum degree \(5\). Bandwidth is also unbounded, since bandwidth at most \(b\) gives a tree partition of width at most \(b\) by consecutive blocks.

This is an obstruction to the **method**, not a counterexample to the conjecture. The general problem still requires a way to handle high-expansion instances without paying for long-range color dependencies. The arguments above establish the stated special cases but supply no uniform \(c\) for all bipartite graphs.