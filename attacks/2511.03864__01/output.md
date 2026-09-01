```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The fixed-imtw question remains open, but it has a degree-(k+1) affirmative answer when the global induced-matching number is at most k, while no single polynomial jointly in imtw and induced biclique number can exist.",
  "would_publish": false,
  "caveats": "Bounded global induced-matching number is stronger than bounded imtw, and the probabilistic obstruction has imtw growing as Theta(log n)."
}
```

# Mathematical writeup

## 1. Formulation and notation

Write

- \(\operatorname{t\!-\!\alpha}(G)\) for the tree-independence number;
- \(\operatorname{imtw}(G)\) for induced matching treewidth;
- \(\nu_{\mathrm{ind}}(G)\) for the ordinary, global maximum size of an induced matching;
- \(\beta(G)\) for the induced biclique number.

A one-bag tree decomposition immediately gives

\[
\operatorname{imtw}(G)\leq \nu_{\mathrm{ind}}(G).
\tag{1}
\]

The class-wise interpretation of the question is:

> For every fixed \(K\), do there exist constants \(C_K,d_K\) such that
> \[
> \operatorname{t\!-\!\alpha}(G)
> \le C_K(\beta(G)+1)^{d_K}
> \]
> for every graph \(G\) with \(\operatorname{imtw}(G)\le K\)?

The results below do not settle this. They prove it under the stronger hypothesis \(\nu_{\mathrm{ind}}(G)\le K\), and they rule out the stronger interpretation asking for one polynomial in the two variables \(\operatorname{imtw}(G)\) and \(\beta(G)\).

---

## 2. Two elementary decomposition lemmas

### Lemma 2.1

If \(A\) is a maximum independent set of \(G\), then

\[
\operatorname{t\!-\!\alpha}(G)\le \alpha(G-A)+1.
\tag{2}
\]

#### Proof

Put \(H=G-A\). For every \(a\in A\), take the bag

\[
B_a=V(H)\cup\{a\},
\]

and connect these bags by an arbitrary tree. Every vertex of \(H\) occurs in every bag, while each \(a\in A\) occurs only in \(B_a\). All edges are covered because \(A\) is independent. Moreover,

\[
\alpha(G[B_a])\le \alpha(H)+1.
\]

This proves (2). \(\square\)

### Lemma 2.2

Let \(A\) be a maximum independent set of \(G\), and let \(X\) be an independent set in \(G-A\). Then the bipartite graph \(G[A,X]\) has a matching saturating \(X\).

#### Proof

For every \(Y\subseteq X\), the set

\[
(A\setminus N_A(Y))\cup Y
\]

is independent. Maximality of \(|A|\) therefore gives

\[
|A|-|N_A(Y)|+|Y|\le |A|,
\]

and hence \(|N_A(Y)|\ge |Y|\). Hall's theorem applies. \(\square\)

---

## 3. A dense bounded-VC-dimension lemma

The following standard consequence of Sauer–Shelah is the main quantitative ingredient.

### Lemma 3.1

For every integer \(d\ge1\) and every \(\delta>0\), there are constants
\(\gamma=\gamma(d,\delta)>0\) and \(m_0=m_0(d,\delta)\) such that the following holds.

Let \(H=(U,V;E)\) be bipartite with \(|U|=|V|=m\ge m_0\). Suppose

\[
|E|\ge \delta m^2
\]

and the set system \(\{N(u):u\in U\}\) has VC-dimension at most \(d\). Then \(H\) contains a \(K_{t,t}\) with

\[
t\ge \left\lfloor \gamma m^{1/(d+1)}\right\rfloor .
\tag{3}
\]

One may take, for sufficiently large \(m\),

\[
\gamma=\frac{\delta}{4(2e)^d}.
\]

#### Proof

At least \(\delta m/2\) vertices of \(U\) have degree at least \(\delta m/2\). Indeed, otherwise the total number of edges would be less than \(\delta m^2\).

Let

\[
s=\left\lceil m^{1/(d+1)}\right\rceil
\]

and choose a uniformly random \(s\)-subset \(S\subseteq V\). For any \(u\) of degree at least \(\delta m/2\), a hypergeometric Chernoff bound gives

\[
\Pr\left(|N(u)\cap S|<\frac{\delta s}{4}\right)
 \le \exp\left(-\frac{\delta s}{16}\right).
\]

For \(s\) sufficiently large, there is therefore a choice of \(S\) for which at least \(\delta m/4\) vertices \(u\in U\) satisfy

\[
|N(u)\cap S|\ge \frac{\delta s}{4}.
\tag{4}
\]

By Sauer–Shelah, the number of distinct traces \(N(u)\cap S\) is at most

\[
\sum_{i=0}^{d}\binom{s}{i}\le (es)^d.
\]

Consequently, at least

\[
\frac{\delta m}{4(es)^d}
\]

of the vertices satisfying (4) have the same trace \(T\subseteq S\). These vertices and \(T\) induce a complete bipartite graph. Since \(s\le 2m^{1/(d+1)}\),

\[
|T|\ge \frac{\delta}{4}m^{1/(d+1)}
\]

and

\[
\frac{\delta m}{4(es)^d}
 \ge \frac{\delta}{4(2e)^d}m^{1/(d+1)}.
\]

This proves the lemma. \(\square\)

---

## 4. Matching versus biclique under bounded induced-matching number

### Proposition 4.1

For every fixed \(k\ge1\), there is a constant \(D_k\) such that every bipartite graph \(H\) with

\[
\nu_{\mathrm{ind}}(H)\le k
\]

and an ordinary matching of size \(m\) satisfies

\[
m\le D_k\bigl(\beta(H)+1\bigr)^{k+1}.
\tag{5}
\]

#### Proof

Restrict \(H\) to the endpoints of a matching

\[
M=\{x_i a_i:1\le i\le m\}.
\]

Thus the two parts are \(X=\{x_1,\dots,x_m\}\) and
\(A=\{a_1,\dots,a_m\}\).

Define a graph \(Q\) on \([m]\) by

\[
ij\in E(Q)
\quad\Longleftrightarrow\quad
x_i a_j\in E(H)\ \text{or}\ x_j a_i\in E(H).
\tag{6}
\]

An independent set of size \(k+1\) in \(Q\) would make the corresponding \(k+1\) matching edges an induced matching in \(H\). Hence

\[
\alpha(Q)\le k.
\]

Equivalently, \(\overline Q\) is \(K_{k+1}\)-free. By Turán's theorem,

\[
e(Q)
\ge \binom m2-\left(1-\frac1k\right)\frac{m^2}{2}
=\frac{m(m-k)}{2k}.
\]

Thus, when \(m\ge2k\),

\[
e(Q)\ge \frac{m^2}{4k}.
\tag{7}
\]

Every edge of \(Q\) accounts for at least one edge of \(H[X,A]\), so (7) shows that \(H[X,A]\) has edge density at least \(1/(4k)\).

Moreover, the neighborhood set system of \(H[X,A]\) has VC-dimension at most \(k\). Indeed, if \(k+1\) columns were shattered, then choosing a row whose trace on these columns is each prescribed singleton would produce an induced matching of size \(k+1\).

Lemma 3.1, with \(d=k\) and \(\delta=1/(4k)\), therefore yields a complete bipartite graph of order

\[
t\ge c_km^{1/(k+1)}-1
\]

for a constant \(c_k>0\). Hence

\[
\beta(H)+1\ge c_km^{1/(k+1)},
\]

which is equivalent to (5), after enlarging the constant to cover \(m<2k\) and the finite threshold in Lemma 3.1. \(\square\)

---

## 5. Polynomial bound for bounded global induced-matching number

### Theorem 5.1

For every fixed \(k\ge1\), there is a constant \(C_k\) such that every graph \(G\) with

\[
\nu_{\mathrm{ind}}(G)\le k
\]

satisfies

\[
\boxed{\operatorname{t\!-\!\alpha}(G)
 \le C_k\bigl(\beta(G)+1\bigr)^{k+1}.}
\tag{8}
\]

Thus the catalog question has an affirmative answer for every class with bounded global induced-matching number.

#### Proof

Let \(A\) be a maximum independent set of \(G\), let \(H=G-A\), and let \(X\) be a maximum independent set of \(H\). Put

\[
m=|X|=\alpha(H).
\]

By Lemma 2.2, the bipartite graph \(G[A,X]\) contains a matching saturating \(X\), hence a matching of size \(m\). Since both \(A\) and \(X\) are independent, \(G[A,X]\) is an induced bipartite subgraph of \(G\). Therefore

\[
\nu_{\mathrm{ind}}(G[A,X])\le k,
\qquad
\beta(G[A,X])\le\beta(G).
\]

Proposition 4.1 gives

\[
m\le D_k(\beta(G)+1)^{k+1}.
\]

Finally, Lemma 2.1 gives

\[
\operatorname{t\!-\!\alpha}(G)\le m+1,
\]

which proves (8) after adjusting the constant. \(\square\)

A completely explicit, though very non-optimal, value follows from the proof. For example, constants of order

\[
C_k=2\bigl(128k(2e)^k\bigr)^{k+1}
\]

are sufficient.

### The case \(k=1\)

For induced-matching number at most one, the exponent can be improved to one.

### Theorem 5.2

If \(G\) has no induced \(2K_2\), then

\[
\boxed{\operatorname{t\!-\!\alpha}(G)\le 2\beta(G)+1.}
\tag{9}
\]

#### Proof

Continue with \(A,H,X\) as above, and write \(m=|X|\). Hall's theorem gives matching edges \(x_i a_i\), \(1\le i\le m\), between \(X\) and \(A\).

Because \(G[A,X]\) contains no induced \(2K_2\), the neighborhoods of vertices of \(X\) in \(A\) are linearly ordered by inclusion. Relabel so that

\[
N_A(x_1)\subseteq N_A(x_2)\subseteq\cdots\subseteq N_A(x_m).
\]

Let \(p=\lceil m/2\rceil\). For every \(i\le p\) and every \(j\ge p\),

\[
a_i\in N_A(x_i)\subseteq N_A(x_j).
\]

Thus the sets

\[
\{a_1,\dots,a_p\}
\quad\text{and}\quad
\{x_p,\dots,x_m\}
\]

contain a balanced biclique of order \(\lceil m/2\rceil\). Both sides are independent, so this biclique is induced. Hence

\[
\left\lceil\frac m2\right\rceil\le\beta(G),
\qquad\text{and therefore}\qquad
m\le2\beta(G).
\]

Lemma 2.1 now gives (9). \(\square\)

The auxiliary inequality \(m\le2\beta\) is sharp: the Ferrers graph with parts
\(\{x_1,\dots,x_{2b}\}\), \(\{a_1,\dots,a_{2b}\}\), and

\[
x_i a_j\in E \quad\Longleftrightarrow\quad j\le i
\]

has an ordinary matching of size \(2b\), induced-matching number one, and biclique number exactly \(b\).

This theorem concerns the stronger condition \(\nu_{\mathrm{ind}}(G)\le1\), not the full case \(\operatorname{imtw}(G)\le1\).

---

## 6. No uniform polynomial in both parameters

The wording “polynomial in both induced matching treewidth and induced biclique number” could be read as asking for one bivariate polynomial \(P\) satisfying

\[
\operatorname{t\!-\!\alpha}(G)
\le P(\operatorname{imtw}(G),\beta(G))
\tag{10}
\]

for all graphs \(G\). That stronger statement is false.

### Theorem 6.1

For arbitrarily large \(n\), there is a bipartite graph \(G_n\) on \(2n\) vertices such that

\[
\operatorname{t\!-\!\alpha}(G_n)\ge \frac n8,
\tag{11}
\]

\[
\frac12\log_2 n-O(1)
\le\operatorname{imtw}(G_n)
\le5\log_2 n+1,
\tag{12}
\]

and

\[
\beta(G_n)\le3\log_2 n+1.
\tag{13}
\]

Consequently, no universal bivariate polynomial \(P\) can satisfy (10).

#### Proof

Take the binomial random bipartite graph \(G\sim G(n,n,1/2)\), with parts \(L,R\), and put \(L_n=\log_2 n\).

### Upper bound on induced matchings

Let \(r=\lceil5L_n\rceil\). The expected number of induced matchings of size \(r\) is at most

\[
\binom nr^2r!\,2^{-r^2}
\le n^{3r}2^{-r^2}
=2^{3rL_n-r^2}
=o(1).
\]

Thus, with high probability,

\[
\nu_{\mathrm{ind}}(G)<r.
\]

The one-bag decomposition then gives

\[
\operatorname{imtw}(G)<5L_n+1.
\]

### Upper bound on bicliques

Let \(s=\lceil3L_n\rceil\). The expected number of \(K_{s,s}\)'s is at most

\[
\binom ns^2 2^{-s^2}
\le n^{2s}2^{-s^2}
=2^{2sL_n-s^2}
=o(1).
\]

Since every biclique in a bipartite graph is induced, with high probability

\[
\beta(G)<s.
\]

### No small balanced separator

With high probability there is no partition

\[
V(G)=X\mathbin{\dot\cup}Y\mathbin{\dot\cup}Z
\]

such that

\[
|Z|<\frac n4,\qquad |X|,|Y|\ge\frac n4,
\]

and there are no edges between \(X\) and \(Y\).

Indeed, write

\[
a=|X\cap L|,\quad b=|X\cap R|,
\quad c=|Y\cap L|,\quad d=|Y\cap R|.
\]

Then

\[
a+c>\frac{3n}{4},\qquad b+d>\frac{3n}{4},
\qquad a+b,c+d\ge\frac n4.
\]

The number of possible bipartite edges between \(X\) and \(Y\) is

\[
ad+bc\ge\frac{3n^2}{64}.
\tag{14}
\]

To see (14), one of \(a,c\) and one of \(b,d\) is at least \(3n/8\). If these large entries belong to opposite sets, the lower bound is \(9n^2/64\). If they both belong, say, to \(X\), then one of \(c,d\) is at least \(n/8\), giving at least \(3n^2/64\). The case where both large entries belong to \(Y\) is symmetric.

For a fixed partition, the probability that all these edges are absent is at most \(2^{-3n^2/64}\). There are at most \(3^{2n}\) partitions, so a union bound gives probability

\[
3^{2n}2^{-3n^2/64}=o(1).
\]

Every tree decomposition has a bag \(B\) such that every component of \(G-B\) has at most half the vertices. This follows by assigning each graph vertex to one node of its bag-subtree and taking a weighted centroid of the decomposition tree.

If every bag had size less than \(n/4\), the components of \(G-B\), each of size at most \(n\), could be grouped into two sets \(X,Y\), each of size at least \(n/4\), with no edges between them. This contradicts the preceding property. Hence every tree decomposition has some bag of size at least \(n/4\).

Since \(G\) is bipartite, every bag \(B\) contains an independent set of size at least \(|B|/2\). Therefore

\[
\operatorname{t\!-\!\alpha}(G)\ge\frac n8.
\]

### Lower bound on induced matching treewidth

Put

\[
q=\left\lfloor\frac12L_n\right\rfloor.
\]

For a fixed \(q\)-set \(I\subseteq L\) and a fixed \(x\in I\), a vertex \(y\in R\) satisfies

\[
N(y)\cap I=\{x\}
\]

with probability \(2^{-q}\). Hence the probability that no such \(y\) exists is at most

\[
e^{-n2^{-q}}.
\]

A union bound over every \(q\)-set \(I\), every \(x\in I\), and both bipartition sides gives

\[
2\binom nq q\,e^{-n2^{-q}}
\le 2n^q q\,e^{-\sqrt n}
=o(1).
\]

Thus, with high probability, every \(q\)-set in either bipartition class is the set of one endpoint from each edge of an induced matching of size \(q\).

Every tree decomposition has a bag of size at least \(n/4\), hence containing at least \(n/8\) vertices from one bipartition class. It therefore hits an induced matching of size \(q\). Consequently,

\[
\operatorname{imtw}(G)\ge q.
\]

All the required properties hold simultaneously with probability tending to one. This proves (11)–(13).

If \(P\) were a fixed bivariate polynomial, then

\[
P(\operatorname{imtw}(G_n),\beta(G_n))
=(\log n)^{O(1)},
\]

whereas \(\operatorname{t\!-\!\alpha}(G_n)=\Omega(n)\), a contradiction. \(\square\)

---

## 7. What remains missing

Theorem 5.1 does not extend directly from global induced-matching number to induced matching treewidth.

The obstruction is local-to-global. Given a maximum independent set \(A\) and a maximum independent set \(X\subseteq G-A\), the Hall matching between \(A\) and \(X\) can be spread across many distant bags. Bounded \(\operatorname{imtw}\) does not bound the induced-matching number of \(G[A,X]\).

This distinction is genuine even when the bound is one. Long paths have arbitrarily large global induced matchings, but their standard edge-bag decompositions have induced matching width one.

Nor can one simply bound the independence number of every bag in an arbitrary optimal induced-matching-width decomposition. For example, \(K_{2,n}\) has a one-bag induced-matching-width-one decomposition whose bag contains an independent set of size \(n\), although a different decomposition has tree-independence number at most two.

A plausible route to the full problem would be a localization lemma showing that a stable set which cannot be removed by refining an \(\operatorname{imtw}\)-\(K\) decomposition yields a dense bipartite incidence graph of VC-dimension at most \(K\). Lemma 3.1 would then give a polynomial biclique bound. I do not have such a localization lemma: component-incidence graphs arising from minimal triangulations do not immediately suffice, because a component adjacent to many bag vertices need not contain one vertex adjacent to all of them.

Thus the original fixed-\(\operatorname{imtw}\) question remains open. The arguments above establish:

1. the conjectured polynomial bound for the substantial special case of bounded global induced-matching number;
2. a linear bound when that global number is one;
3. a proof that any formulation using one universal polynomial in both parameters is false.

I have not independently verified whether the global-induced-matching special case already appears in the cited preprints; the argument here is self-contained, and no novelty claim is made.