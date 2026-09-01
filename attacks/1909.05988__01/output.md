```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard definition, the entire linear regime is determined, with exact formulas near s=kt and general exponent bounds outside it, but the nonlinear cases and Ramsey endpoint remain open.",
  "would_publish": false,
  "caveats": "Assumes fixed k,s,t and fewer than t edges on every s-set; no claim of novelty or of resolving the nonlinear regime."
}
```

## 1. Definition and scope

I use the standard definition
\[
f_k(N;s,t)=\min\{\alpha(H): |V(H)|=N,\ e_H(S)<t
\text{ for every }S\in {V(H)\choose s}\},
\]
where \(H\) is a simple \(k\)-uniform hypergraph and \(k,s,t\) are fixed while \(N\to\infty\).

For \(N\ge s\), the local condition has the useful equivalent form
\[
H\text{ is admissible}
\quad\Longleftrightarrow\quad
\left|\bigcup_{e\in\mathcal F}e\right|\ge s+1
\quad\text{for every }\mathcal F\in {E(H)\choose t}.
\tag{1}
\]

Indeed, a collection of \(t\) edges whose union has at most \(s\) vertices can be padded to an \(s\)-set, and the converse is immediate.

All implicit constants below may depend on \(k,s,t\).

---

## 2. Partial classification

### Theorem

Let \(k\ge3\), \(s\ge k+1\), and \(1\le t\le\binom{s}{k}\).

1. **Very sparse regime.** If \(s\ge kt\), then for every \(N\ge s\),
   \[
   f_k(N;s,t)=N-t+1.
   \tag{2}
   \]

2. **An exact matching regime.** Put \(d=kt-s\). If
   \[
   1\le d\le \min\{t-1,k+1\},
   \tag{3}
   \]
   then for every \(N\ge s\),
   \[
   f_k(N;s,t)=N-\left\lfloor\frac Nk\right\rfloor.
   \tag{4}
   \]
   In particular,
   \[
   f_k(N;kt-1,t)=N-\left\lfloor\frac Nk\right\rfloor.
   \]

3. **Complete linear regime.** If
   \[
   (k-1)t+1\le s<kt,
   \tag{5}
   \]
   then there is an effectively computable rational number
   \(\rho=\rho(k,s,t)\in(0,1)\) such that
   \[
   f_k(N;s,t)=\rho N+O_{k,s,t}(1).
   \tag{6}
   \]
   Thus, for fixed parameters,
   \[
   f_k(N;s,t)=\Theta(N)
   \quad\Longleftrightarrow\quad
   s\ge (k-1)t+1.
   \tag{7}
   \]

4. **General nonlinear bounds.** Suppose
   \[
   s<(k-1)t+1,
   \]
   and set
   \[
   r=\left\lceil\frac{kt-s}{t-1}\right\rceil,\qquad
   \gamma=\frac{k-r}{k-1},\qquad
   \beta=\frac{s-1}{t(k-1)}.
   \tag{8}
   \]
   Then \(2\le r\le k\), \(0\le\gamma<1\), and \(\beta<1\). For sufficiently large \(N\),
   \[
   \max\left\{
      cN^\gamma,\,
      c\log_{(k-1)}N
   \right\}
   \le f_k(N;s,t)
   \le
   C N^\beta(\log N)^{1/(k-1)},
   \tag{9}
   \]
   where \(\log_{(j)}\) denotes \(j\)-fold iterated logarithm.

The bounds in (9) are generally far apart and are not presented as the expected final answer.

---

## 3. Proof of the exact sparse formula

Assume \(s\ge kt\). Any \(t\) distinct \(k\)-edges have union of size at most \(kt\le s\), so by (1) every admissible \(H\) has at most \(t-1\) edges.

Choosing one vertex from each edge gives a vertex cover of size at most \(t-1\), hence
\[
\alpha(H)\ge N-(t-1).
\]
Conversely, take \(t-1\) pairwise disjoint edges and all remaining vertices isolated. Its independence number is \(N-(t-1)\), and it is admissible because it has fewer than \(t\) edges in total. This proves (2).

For \(t=1\), this simply says that the only admissible hypergraph is empty and \(f_k(N;s,1)=N\).

---

## 4. Proof of the exact matching regime

Assume \(d=kt-s\) satisfies (3). For a family \(\mathcal A\) of edges define its deficiency by
\[
\delta(\mathcal A)=k|\mathcal A|-\left|\bigcup_{e\in\mathcal A}e\right|.
\]
Deficiency is monotone under adding edges, since
\[
\delta(\mathcal A\cup\{e\})-\delta(\mathcal A)
=
\left|e\cap\bigcup_{f\in\mathcal A}f\right|\ge0.
\tag{10}
\]

For any \(t\) edges of an admissible \(H\), condition (1) gives
\[
\delta(\mathcal A)\le kt-(s+1)=d-1.
\tag{11}
\]

Suppose first that \(e(H)\ge t\). Form the edge-intersection graph whose vertices are the edges of \(H\), with two adjacent when they intersect.

If an edge-component contained \(d+1\) edges, it would contain a connected set \(e_1,\dots,e_{d+1}\) ordered so that each \(e_i\), \(i>1\), intersects an earlier edge. Therefore
\[
\left|\bigcup_{i=1}^{d+1}e_i\right|
\le k+d(k-1),
\]
and consequently their deficiency is at least \(d\). Since \(d+1\le t\), these edges can be extended to \(t\) edges, contradicting (10)–(11). Thus every edge-component contains at most \(d\) edges.

Let \(C\) be such a component, with \(m\) edges and \(v\) vertices. Extending all its edges to a collection of \(t\) edges shows
\[
km-v=\delta(C)\le d-1\le k.
\tag{12}
\]
If \(m=1\), one vertex covers \(C\), and \(v=k\). If \(m\ge2\), root a spanning tree of the edge-intersection graph of \(C\). For each nonroot edge choose one vertex in its intersection with its parent. These at most \(m-1\) vertices meet every edge of \(C\), including the root. Hence
\[
\tau(C)\le m-1.
\]
By (12),
\[
v\ge km-k=k(m-1),
\]
so
\[
\tau(C)\le \frac vk.
\]
Summing over the vertex-disjoint edge-components gives
\[
\tau(H)\le \left\lfloor\frac Nk\right\rfloor,
\]
and therefore
\[
\alpha(H)\ge N-\left\lfloor\frac Nk\right\rfloor.
\tag{13}
\]

If \(e(H)<t\), then \(\tau(H)\le t-1\). Usually \(N\ge s\ge k(t-1)\), so this again gives \(\tau(H)\le\lfloor N/k\rfloor\). The only exceptional possibility is \(d=k+1\) and \(N=s=k(t-1)-1\). If \(H\) has \(t-1\) edges, they cannot all be disjoint; two intersecting edges can be covered by one common vertex, and one vertex from each remaining edge gives a cover of size at most \(t-2=\lfloor N/k\rfloor\). Thus (13) holds in every case.

For the reverse inequality, take a maximum matching of \(\lfloor N/k\rfloor\) edges. Every \(t\) of its edges have union \(kt>s\), so it is admissible. Its independence number is
\[
N-\left\lfloor\frac Nk\right\rfloor.
\]
This proves (4).

---

## 5. The entire linear regime and its finite reduction

Assume
\[
(k-1)t+1\le s<kt.
\]

### 5.1 Bounded edge-components

If an edge-intersection component contained at least \(t\) edges, it would contain a connected set \(e_1,\dots,e_t\). Ordering them so that each new edge meets the preceding union gives
\[
\left|\bigcup_{i=1}^t e_i\right|
\le k+(t-1)(k-1)
=(k-1)t+1
\le s,
\]
contrary to (1). Thus every edge-component has at most \(t-1\) edges and at most \(k(t-1)\) nonisolated vertices.

There are therefore only finitely many possible isomorphism types of nontrivial edge-components.

### 5.2 Repeatable components

Call such a component \(C\) **repeatable** if the disjoint union of \(t\) copies of \(C\) satisfies (1). Equivalently, every choice of \(t\) edges from these \(t\) copies has union of size at least \(s+1\).

Checking \(t\) copies is enough: any \(t\) edges in an arbitrary number of disjoint copies occupy at most \(t\) copies.

Let \(\mathcal R=\mathcal R(k,s,t)\) be the finite set of repeatable component types and define
\[
\rho(k,s,t)=
\min_{C\in\mathcal R}\frac{\alpha(C)}{|V(C)|}.
\tag{14}
\]
This family is nonempty: a single \(k\)-edge is repeatable because \(t\) disjoint edges have union \(kt>s\). Thus
\[
0<\rho\le \frac{k-1}{k}.
\]

If a nonrepeatable component type occurred \(t\) times in an admissible \(H\), the forbidden choice of \(t\) edges in the corresponding \(t\) copies would violate (1). Hence every nonrepeatable type occurs at most \(t-1\) times. Since there are finitely many types, all nonrepeatable components together contain only \(O_{k,s,t}(1)\) vertices.

Independence number is additive over edge-components. Therefore
\[
\alpha(H)\ge \rho N-O_{k,s,t}(1).
\tag{15}
\]

Conversely, choose \(C\in\mathcal R\) attaining (14), take as many disjoint copies of \(C\) as fit, and make the remaining \(O(1)\) vertices isolated. Repeatability makes this hypergraph admissible, and its independence number is
\[
\rho N+O_{k,s,t}(1).
\tag{16}
\]
Together, (15) and (16) prove (6).

The constant \(\rho\) is computable by a finite exhaustive procedure:

1. enumerate all simple \(k\)-graphs with at most \(t-1\) edges, no isolated vertices, and connected edge-intersection graph;
2. form \(t\) disjoint copies;
3. test every \(t\)-element selection of edges for union size greater than \(s\);
4. compute \(\alpha(C)\) by exhaustive search over vertex subsets;
5. minimize \(\alpha(C)/|V(C)|\).

No claim of practical efficiency is intended.

Finally, if \(s<(k-1)t+1\), the random construction proved below gives \(f_k(N;s,t)=o(N)\). This establishes the equivalence (7).

---

## 6. General lower bound in the nonlinear regime

Assume \(s<(k-1)t+1\), and define \(r\) by (8). Then
\[
r+t(k-r)=kt-(t-1)r\le s.
\tag{17}
\]

If an \(r\)-set \(R\) belonged to \(t\) distinct edges, those edges would have union of size at most
\[
r+t(k-r)\le s,
\]
contrary to (1). Thus every \(r\)-degree is at most \(t-1\). Double-counting pairs \((R,e)\) with \(R\subset e\) gives
\[
\binom{k}{r}e(H)
=
\sum_{R\in{V(H)\choose r}} d_H(R)
\le
(t-1)\binom Nr,
\]
and hence
\[
e(H)\le A N^r
\tag{18}
\]
for a constant \(A=A(k,t)\).

Choose each vertex independently with probability
\[
p=\eta N^{-(r-1)/(k-1)},
\]
where \(\eta>0\) is a sufficiently small constant. For the resulting random set \(W\),
\[
\mathbb E\bigl[|W|-e(H[W])\bigr]
=
pN-p^k e(H).
\]
Using (18),
\[
\mathbb E\bigl[|W|-e(H[W])\bigr]
\ge
\left(\eta-A\eta^k\right)
N^{(k-r)/(k-1)}.
\]
Taking \(\eta\) so that \(A\eta^{k-1}\le1/2\), some \(W\) satisfies
\[
|W|-e(H[W])
\ge cN^{(k-r)/(k-1)}.
\]
Choosing one vertex from each edge of \(H[W]\) and deleting the resulting vertex cover leaves an independent set of at least this size. Therefore
\[
f_k(N;s,t)\ge cN^\gamma.
\tag{19}
\]

There is also a universal iterated-logarithmic lower bound. Every admissible \(H\) is \(K_s^{(k)}\)-free. The elementary Erdős–Rado exposure recurrence gives
\[
R_k(q,q)\le T_k(C_kq),
\]
where \(T_1(x)=x\) and \(T_{j+1}(x)=2^{T_j(x)}\). Consequently every two-coloring of the \(k\)-sets of an \(N\)-set has a homogeneous set of size
\[
c_k\log_{(k-1)}N.
\]
For large \(N\) this size exceeds \(s\), so the homogeneous set cannot be an \(H\)-clique and must be independent. Hence
\[
f_k(N;s,t)\ge c_{k,s}\log_{(k-1)}N.
\tag{20}
\]

Combining (19) and (20) gives the lower half of (9).

---

## 7. General probabilistic upper bound

Again assume
\[
s<(k-1)t+1,
\qquad
\beta=\frac{s-1}{t(k-1)}<1.
\]

Start with \(M=2N\) vertices and let \(G\sim G^{(k)}(M,p)\), where
\[
p=cM^{-(s-1)/t},
\tag{21}
\]
and \(c>0\) will be chosen sufficiently small.

Let \(Y\) denote the number of \(s\)-sets spanning at least \(t\) edges. By a union bound,
\[
\begin{aligned}
\mathbb EY
&\le
\binom Ms
\binom{\binom{s}{k}}{t}p^t\\
&\le A_{k,s,t}c^t M.
\end{aligned}
\tag{22}
\]
Choose \(c\) so that the last quantity is at most \(M/16\). Markov's inequality then gives
\[
\Pr(Y\le M/4)\ge\frac34.
\tag{23}
\]

On the other hand, let
\[
q=
\left\lceil
D\bigl(p^{-1}\log M\bigr)^{1/(k-1)}
\right\rceil
=
O\!\left(
M^\beta(\log M)^{1/(k-1)}
\right),
\tag{24}
\]
where \(D\) is a sufficiently large constant. Since \(\beta<1\), we have \(q=o(M)\). A union bound over \(q\)-sets gives
\[
\Pr(\alpha(G)\ge q)
\le
\binom Mq(1-p)^{\binom qk}
\le
\exp\left(
q\log\frac{eM}{q}
-p\binom qk
\right)
=o(1),
\tag{25}
\]
because \(p q^{k-1}=D^{k-1}\log M\).

Thus with positive probability both \(Y\le M/4\) and \(\alpha(G)<q\).

For each bad \(s\)-set choose one of its vertices, and delete the union of the chosen vertices. At most \(Y\le M/4\) vertices are deleted. The remaining induced hypergraph has no bad \(s\)-set and has at least \(3M/4>N\) vertices. Taking any \(N\) of them produces an admissible \(k\)-graph whose independence number is still less than \(q\). Therefore
\[
f_k(N;s,t)
\le
C N^\beta(\log N)^{1/(k-1)}.
\]
This proves the upper half of (9) and, since \(\beta<1\), proves \(f_k(N;s,t)=o(N)\) throughout the nonlinear regime.

---

## 8. Why this does not settle the catalog problem

At the endpoint
\[
t=\binom{s}{k},
\]
admissibility is exactly \(K_s^{(k)}\)-freeness. If \(R_k(s,n)\) denotes the usual two-color hypergraph Ramsey number, then there is the exact inverse relation
\[
f_k\!\left(N;s,\binom{s}{k}\right)
=
\max\{n:R_k(s,n)\le N\}.
\tag{26}
\]
Indeed, every \(K_s^{(k)}\)-free \(k\)-graph on \(N\) vertices has an independent \(n\)-set precisely when \(N\ge R_k(s,n)\).

Thus the catalog problem includes the general off-diagonal hypergraph Ramsey problem as a special endpoint. The exponent interval in (9) is also usually wide. For example, for \((k,s,t)=(3,4,3)\), (9) gives only an iterated-logarithmic lower bound and a polynomial upper bound, whereas the supplied Fox–He theorem gives the much sharper
\[
f_3(N;4,3)=\Theta\!\left(\frac{\log N}{\log\log N}\right).
\]

Accordingly, the results above completely determine the linear-growth phase and give some exact formulas and baseline nonlinear bounds, but they do not determine the order of \(f_k(N;s,t)\) in general.