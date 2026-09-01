```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general conjecture remains open, but it holds for unions of copies of K_{d+1} with error 1, for K_{d,d}, and whenever d>=n-3, while sufficiently many identical copies of any regular graph admit an exact solution.",
  "would_publish": false,
  "caveats": "Assumes finite simple graphs; novelty of these elementary partial results has not been checked against the full literature."
}
```

# Statement and partial results

For a spanning subgraph \(H\) of a \(d\)-regular graph \(G\), write
\[
m(H,k)=|\{v\in V(G):d_H(v)=k\}|.
\]
The conjecture asks for
\[
\left|m(H,k)-\frac{n}{d+1}\right|\le 2
\qquad(0\le k\le d).
\]

I do not obtain the general conjecture. I prove the following special cases and auxiliary results.

1. For every \(d\)-regular \(G\), a sufficiently large disjoint union of identical copies of \(G\) has a spanning subgraph with the degree classes exactly uniform.
2. If \(G=tK_{d+1}\), then the conjectured error \(2\) can be replaced by \(1\).
3. If \(G\) is \(d\)-regular on \(n\) vertices and \(d\ge n-3\), then the conjecture holds.
4. The conjecture holds for \(K_{d,d}\).

All graphs below are finite and simple.

---

# 1. The uniform histogram lies in the convex hull

## Lemma 1

Let \(G\) be \(d\)-regular on \(N\) vertices, with \(M\) edges. There is a probability distribution on the spanning subgraphs \(S\subseteq E(G)\) such that
\[
\mathbb E\,m(S,k)=\frac{N}{d+1}
\qquad(0\le k\le d).
\]

### Proof

Choose \(p\) uniformly from \([0,1]\), and then retain each edge independently with probability \(p\). For a fixed edge set \(S\),
\[
\Pr(S)=\int_0^1p^{|S|}(1-p)^{M-|S|}\,dp
      =\frac{1}{(M+1)\binom{M}{|S|}}.
\]

For a fixed vertex \(v\),
\[
\begin{aligned}
\Pr(d_S(v)=k)
 &=\binom dk\int_0^1p^k(1-p)^{d-k}\,dp\\
 &=\binom dk\frac{k!(d-k)!}{(d+1)!}
 =\frac1{d+1}.
\end{aligned}
\]
Summing over the \(N\) vertices gives the assertion. \(\square\)

Thus the vector
\[
\left(\frac N{d+1},\ldots,\frac N{d+1}\right)
\]
lies in the convex hull of the attainable degree-histogram vectors. This alone does not prove the conjecture: a point may lie in the convex hull of integer vectors while being far from every individual vector.

## Corollary 2: exact stabilization

For every \(d\)-regular \(G\), there is an integer \(Q>0\) such that the disjoint union of \(Q\) copies of \(G\) has a spanning subgraph \(H\) satisfying
\[
m(H,k)=\frac{QN}{d+1}
\qquad(0\le k\le d).
\]

One explicit choice is
\[
Q=(M+1)!.
\]

### Proof

For every \(S\subseteq E(G)\), put \(s=|S|\) and assign the subgraph \(S\) to exactly
\[
s!(M-s)!
\]
copies of \(G\). The total number of copies used is
\[
\sum_{s=0}^M\binom Ms s!(M-s)!
=(M+1)M!
=(M+1)!.
\]
Moreover, \(s!(M-s)!=Q\Pr(S)\). Hence, for every \(k\),
\[
m(H,k)
 =Q\,\mathbb E\,m(S,k)
 =\frac{QN}{d+1}.
\]
\(\square\)

A smaller existential multiplier follows from Carathéodory's theorem. Since all histogram vectors lie in the affine hyperplane whose coordinates sum to \(N\), at most \(d+1\) histogram vectors are needed in the convex representation. Clearing the barycentric denominators gives a multiplier satisfying, for \(d\ge1\),
\[
Q\le (d+1)d^{d/2}N^d.
\]
Indeed, after selecting an affinely independent representation of dimension \(a\le d\), Cramer's rule clears denominators using
\[
Q=(d+1)|\det C|,
\]
where \(C\) is an \(a\times a\) integer matrix with entries of absolute value at most \(N\); Hadamard's inequality gives
\[
|\det C|\le a^{a/2}N^a.
\]

As another useful special case, if \(G\) is \(1\)-factorizable, then \(d+1\) copies suffice: in copy \(k\), take a spanning \(k\)-factor. Every regular bipartite graph is \(1\)-factorizable by repeated application of Hall's theorem.

---

# 2. Disjoint unions of complete graphs

## Theorem 3

For all \(q\ge1\) and \(t\ge1\), the graph
\[
G=tK_q
\]
has a spanning subgraph \(H\) such that
\[
|m(H,k)-t|\le1
\qquad(0\le k\le q-1).
\]
Since \(d=q-1\) and \(n=tq\), this proves the conjecture for this family with error \(1\).

### Preliminary constructions

For \(q\ge2\), let \(A_q\) be the graph on vertices \(1,\ldots,q\) with
\[
ij\in E(A_q)\quad\Longleftrightarrow\quad i+j\ge q+1.
\]
A direct count gives
\[
d_{A_q}(i)=
\begin{cases}
i,&2i<q+1,\\
i-1,&2i\ge q+1.
\end{cases}
\]
Consequently, if \(c=\lfloor q/2\rfloor\), then
\[
m(A_q,0)=0,\qquad m(A_q,c)=2,
\]
and every other degree in \(\{1,\ldots,q-1\}\) occurs once. Thus its histogram differs from the all-ones vector by at most \(1\).

For \(r\ge1\), define the bipartite staircase graph \(B_r\) with parts
\[
X=\{x_0,\ldots,x_{r-1}\},\qquad
Y=\{y_0,\ldots,y_{r-1}\},
\]
and edges
\[
x_i y_j\in E(B_r)\quad\Longleftrightarrow\quad i+j\ge r.
\]
Then
\[
d(x_i)=i,\qquad d(y_j)=j,
\]
so every degree \(0,\ldots,r-1\) occurs exactly twice.

### Case 1: \(q=2r\)

Put \(B_r\) in one clique and its complement \(\overline{B_r}\) in a second clique. Since complementing a graph on \(q\) vertices changes degree \(k\) to \(q-1-k\),
\[
m(B_r,k)+m(\overline{B_r},k)=2
\qquad(0\le k\le q-1).
\]
Thus every pair of cliques can be handled exactly.

If \(t\) is odd, put \(A_q\) in the remaining clique. Its contribution differs from one vertex of each degree by at most \(1\). Hence the total error is at most \(1\).

### Case 2: \(q=2r+1\)

Let
\[
F_r=B_r\mathbin{\dot\cup}K_1.
\]
Its histogram is
\[
m(F_r,0)=3,\qquad
m(F_r,k)=2\quad(1\le k\le r-1),
\]
and \(m(F_r,k)=0\) for \(k\ge r\).

Let \(L_r\) be obtained from \(B_r\) by adding a new vertex \(z\) adjacent to every \(x_i\). Then
\[
m(L_r,0)=1,\qquad
m(L_r,k)=2\quad(1\le k\le r),
\]
and \(m(L_r,k)=0\) for \(k>r\).

Therefore
\[
m(F_r,k)+m(\overline{F_r},k)=
\begin{cases}
3,&k\in\{0,2r\},\\
0,&k=r,\\
2,&\text{otherwise},
\end{cases}
\]
while
\[
m(L_r,k)+m(\overline{L_r},k)=
\begin{cases}
1,&k\in\{0,2r\},\\
4,&k=r,\\
2,&\text{otherwise}.
\end{cases}
\]
Adding these identities shows that four cliques can be handled exactly:
\[
m(F_r,k)+m(\overline{F_r},k)
+m(L_r,k)+m(\overline{L_r},k)=4
\]
for every \(k\).

Write \(t=4a+s\), \(0\le s\le3\), and use exact four-clique blocks. For the remainder:

- \(s=1\): use \(A_q\);
- \(s=2\): use \(A_q\) and \(F_r\);
- \(s=3\): use \(F_r,\overline{F_r},A_q\).

For \(s=2\), the resulting counts are
\[
3\text{ at }k=0,\quad
3\text{ for }1\le k\le r-1,\quad
2\text{ at }k=r,\quad
1\text{ for }r+1\le k\le2r,
\]
all within \(1\) of \(2\).

For \(s=3\), the counts are \(3\) except that they are \(4\) at \(k=2r\) and \(2\) at \(k=r\), again all within \(1\) of \(3\).

The case \(q=1\) is immediate. This completes the proof. \(\square\)

---

# 3. A codensity bound

The following threshold construction proves the conjecture for the three densest possible orders \(n=d+1,d+2,d+3\).

## Lemma 4

Let \(G\) be a graph on \(n\) vertices and put
\[
F=\overline G,\qquad r=\Delta(F).
\]
If \(F\) is nonempty, then \(G\) has a spanning subgraph \(H\) satisfying
\[
\max_k m(H,k)\le r+1.
\]
If \(F\) is empty, then \(G=K_n\) has a spanning subgraph with maximum degree multiplicity at most \(2\).

### Proof

The case \(F=K_n\) is trivial: take \(H\) empty, for which the maximum multiplicity is \(n=r+1\). Assume now that \(F\) is nonempty and noncomplete.

We first choose two vertices \(u,v\) such that
\[
N_F(u)\setminus\{v\}\ne N_F(v)\setminus\{u\}.
\]
Such a pair exists. Otherwise, for every three distinct vertices \(u,v,w\),
\[
uw\in E(F)\quad\Longleftrightarrow\quad vw\in E(F).
\]
It would follow that every vertex is either adjacent to every other vertex or to none, forcing \(F\) to be complete or empty.

Put \(c=\lfloor n/2\rfloor\), and let \(W=V(F)\setminus\{u,v\}\). We will label \(u\) by \(c\), \(v\) by \(c+1\), and choose which vertices get the high labels \(c+2,\ldots,n\).

For \(w\in W\), define
\[
a_w=\mathbf 1_{\{uw\in E(F)\}}
     -\mathbf 1_{\{vw\in E(F)\}}.
\]
This vector is nonzero. Let
\[
h=n-c-1,
\]
the number of labels in \(\{c+2,\ldots,n\}\). There is a subset \(X\subseteq W\) of size \(h\) such that
\[
\sum_{w\in X}a_w\ne0.
\]
For \(n\ge4\), this follows from the elementary fixed-cardinality argument: if every \(h\)-subset had sum zero, comparing two such subsets differing in one element would force all \(a_w\) equal, and then equal to zero. The \(n=3\) noncomplete cases are checked directly.

Assign the labels \(c+2,\ldots,n\) to \(X\), and the labels \(1,\ldots,c-1\) to \(W\setminus X\). On these labels define the threshold graph \(T\) by
\[
ij\in E(T)\quad\Longleftrightarrow\quad i+j\ge n+1.
\]
Finally, take
\[
H=T-E(F).
\]
Then \(H\subseteq G\).

The vertices labeled \(c\) and \(c+1\) have the same degree \(c\) in \(T\). Moreover, apart from a possible common contribution of the edge \(uv\), their incident edges of \(F\) that belong to \(T\) are exactly their edges to \(X\). Hence, if
\[
\ell(x)=|\{e\in E(F)\cap E(T):e\text{ is incident with }x\}|,
\]
then
\[
\ell(u)-\ell(v)
=|N_F(u)\cap X|-|N_F(v)\cap X|
\ne0.
\]
Thus the two vertices having the duplicated degree \(c\) in \(T\) acquire distinct degrees in \(H\).

Every other degree in \(T\) occurs at most once. Also,
\[
0\le \ell(x)\le r.
\]
If \(d_H(x)=k\), then
\[
d_T(x)\in\{k,k+1,\ldots,k+r\}.
\]
This interval contains \(r+1\) degree values. Each has at most one vertex that can finish with degree \(k\), because the only duplicated \(T\)-degree is \(c\), and its two vertices have distinct final degrees. Therefore
\[
m(H,k)\le r+1.
\]

If \(F\) is empty, simply use \(T\); its degree multiplicity is at most \(2\). \(\square\)

## Corollary 5

Let \(G\) be \(d\)-regular on \(n\) vertices, and put
\[
r=n-1-d.
\]
Then:

- if \(r=0\), there is an \(H\) with
  \[
  \left|m(H,k)-\frac{n}{d+1}\right|\le1;
  \]
- if \(r=1\), there is an \(H\) satisfying the conjectured bound \(2\);
- if \(r\ge2\) and \(d\ge1\), there is an \(H\) with
  \[
  \left|m(H,k)-\frac{n}{d+1}\right|\le r.
  \]

In particular, the conjecture holds whenever
\[
r\le2,
\qquad\text{equivalently}\qquad d\ge n-3.
\]

### Proof

When \(r=0\), \(G=K_n\), the target is \(1\), and Lemma 4 gives multiplicity at most \(2\).

When \(r\ge1\), Lemma 4 gives
\[
0\le m(H,k)\le r+1.
\]
Let
\[
\mu=\frac{n}{d+1}.
\]

If \(r=1\), then \(1\le\mu<2\), and every number in \([0,2]\) is within \(2\) of \(\mu\).

Suppose \(r\ge2\) and \(d\ge1\). Since \(n=d+r+1\),
\[
r(d+1)-n=(r-1)d-1\ge0.
\]
Thus \(1\le\mu\le r\). Hence
\[
|m(H,k)-\mu|
\le\max\{\mu,r+1-\mu\}
\le r.
\]
For \(r=2\), this is precisely the conjectured error \(2\). If \(d=0\), the graph is empty and the assertion is immediate. \(\square\)

---

# 4. Complete bipartite graphs

## Proposition 6

The conjecture holds for \(G=K_{d,d}\).

### Proof

Label the two parts
\[
X=\{x_0,\ldots,x_{d-1}\},\qquad
Y=\{y_0,\ldots,y_{d-1}\},
\]
and retain the edge \(x_i y_j\) exactly when
\[
i+j\ge d.
\]
Then
\[
d_H(x_i)=i,\qquad d_H(y_j)=j.
\]
Thus
\[
m(H,k)=
\begin{cases}
2,&0\le k\le d-1,\\
0,&k=d.
\end{cases}
\]
Here \(n=2d\), so
\[
\frac{n}{d+1}=\frac{2d}{d+1}=2-\frac2{d+1}.
\]
For \(k<d\), the error is \(2/(d+1)\), while for \(k=d\) it is
\[
\frac{2d}{d+1}<2.
\]
\(\square\)

---

# What remains open

These arguments do not settle a general \(d\)-regular graph with \(d\ge4\).

The convex-hull lemma gives the correct average histogram but does not imply that one attainable histogram is close to the average. The exact stabilization result uses different spanning subgraphs in different connected components, and there is no valid procedure for “dividing by the number of copies.”

The codensity argument reaches the conjectured constant only when the complement has degree at most \(2\). For complement degree \(r=3\), it gives additive error \(3\), not \(2\). The clique and complete-bipartite constructions rely heavily on the freedom to realize specially designed threshold or staircase graphs inside those hosts.

Thus the general conjecture remains unresolved.