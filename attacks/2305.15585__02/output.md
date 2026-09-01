```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved for k=2, while for general k there are universal fractional-chromatic and improved logarithmic bounds, but not the required constant bound.",
  "would_publish": false,
  "caveats": "The main unresolved issue is that G may be chosen after seeing T; the fixed-graph probability estimates are only exponentially small in N and cannot be union-bounded over all graphs."
}
```

## 1. Statement and notation

I interpret the intended conclusion as
\[
\chi\bigl(G[N_T^+(v)]\bigr)\ge k,
\]
as suggested in the catalog notes and by the source-paper abstract.

Fix \(k\ge2\), put \(q=k-1\), and call a pair \((T,G)\) **\(q\)-bad** if
\[
\chi\bigl(G[N_T^+(v)]\bigr)\le q
\qquad\text{for every }v\in V(T).
\tag{1}
\]

The conjecture asks whether, for fixed \(q\), the chromatic numbers of all \(q\)-bad graphs are bounded by a constant depending only on \(q\), with high probability for a random tournament.

The results below do not establish such a constant, but they give several rigorous restrictions on a possible counterexample.

---

## 2. An exact reformulation

For each \(v\), choose a map
\[
c_v:N_T^+(v)\longrightarrow [q].
\]
Given the collection \(c=(c_v)_v\), define a graph \(H_c\) on \(V(T)\) by declaring \(xy\in E(H_c)\) if and only if
\[
c_v(x)\ne c_v(y)
\]
for every \(v\) such that \(v\to x\) and \(v\to y\).

Then
\[
\max\left\{\chi(G):(T,G)\text{ is \(q\)-bad}\right\}
   =\max_c \chi(H_c).
\tag{2}
\]

Indeed, if \(G\) is \(q\)-bad, choose \(c_v\) to be a proper \(q\)-coloring of \(G[N_T^+(v)]\). Every edge of \(G\) then satisfies the defining condition of \(H_c\), so \(G\subseteq H_c\). Conversely, each \(c_v\) is a proper coloring of \(H_c[N_T^+(v)]\), so \(H_c\) itself is \(q\)-bad.

This also gives a fully specified exhaustive computation for small \(N\): enumerate the
\[
q^{\sum_v d_T^+(v)}=q^{\binom N2}
\]
local label systems \(c\), form \(H_c\), and compute the maximum of their chromatic numbers. I have not performed this computation.

---

## 3. The conjecture for \(k=1,2\)

### Proposition 3.1
The conjecture holds for \(k=2\), with the optimal choice \(\chi=2\).

### Proof

For a fixed pair \(\{x,y\}\), each \(v\notin\{x,y\}\) satisfies
\[
v\to x,\qquad v\to y
\]
with probability \(1/4\), independently over \(v\). Hence
\[
\Pr\bigl(\{x,y\}\text{ has no common dominator}\bigr)
  =\left(\frac34\right)^{N-2}.
\]
Therefore
\[
\Pr\bigl(\text{some pair has no common dominator}\bigr)
 \le \binom N2\left(\frac34\right)^{N-2}=o(1).
\tag{3}
\]

On the complementary event, if \(xy\in E(G)\), there is a vertex \(v\) with
\(\{x,y\}\subseteq N_T^+(v)\). Thus
\[
\chi\bigl(G[N_T^+(v)]\bigr)\ge2.
\]
Consequently, every \(1\)-bad graph is edgeless and has chromatic number at most \(1\).

The threshold \(2\) is optimal because an edgeless graph has chromatic number \(1\) and has no locally induced edge. ∎

For \(k=1\), \(\chi=1\) works trivially for \(N\ge2\), since some tournament out-neighborhood is nonempty.

---

## 4. A constant fractional-chromatic bound

Let \(\chi_f(G)\) denote the fractional chromatic number.

### Proposition 4.1
For every tournament \(T\) with minimum indegree \(\delta^-(T)>0\), every \(q\)-bad graph \(G\) satisfies
\[
\chi_f(G)\le \frac{qN}{\delta^-(T)}.
\tag{4}
\]

Consequently, for a uniformly random tournament,
\[
\chi_f(G)\le
2q\left(1+O\left(\sqrt{\frac{\log N}{N}}\right)\right)
\tag{5}
\]
simultaneously for every \(q\)-bad graph \(G\), with high probability.

### Proof

For each \(v\), let
\[
I_{v,1},\ldots,I_{v,q}
\]
be the color classes of a proper \(q\)-coloring of \(G[N_T^+(v)]\), padding with empty classes if necessary. Each \(I_{v,a}\) is an independent set of \(G\).

Put \(d=\delta^-(T)\), and assign weight \(1/d\) to every \(I_{v,a}\). A vertex \(x\) belongs to exactly \(d_T^-(x)\) of these independent sets, one for every \(v\to x\). Its total covering weight is therefore
\[
\frac{d_T^-(x)}d\ge1.
\]
The total weight is \(qN/d\), proving (4).

For a random tournament, Hoeffding's inequality gives
\[
\delta^-(T)\ge
\frac{N-1}{2}-\sqrt{(N-1)\log N}
\]
with probability \(1-o(1)\), which yields (5). ∎

Thus the following fractional version of the conjecture is proved:

> For every fixed \(k\) and every \(\varepsilon>0\), with high probability, every graph \(G\) with
> \[
> \chi_f(G)\ge 2(k-1)+\varepsilon
> \]
> has a vertex \(v\) for which
> \[
> \chi(G[N_T^+(v)])\ge k.
> \]

In particular, the integer threshold \(\chi_f(G)\ge2k-1\) works for all sufficiently large \(N\).

This does not settle the original conjecture: bounded fractional chromatic number does not bound ordinary chromatic number. For example,
\[
\chi\bigl(KG(2r+s,r)\bigr)=s+2,\qquad
\chi_f\bigl(KG(2r+s,r)\bigr)=2+\frac sr,
\]
so taking \(r=s^2\) gives unbounded ordinary chromatic number while the fractional chromatic number tends to \(2\).

A useful restricted consequence is immediate: if a graph class satisfies
\[
\chi(G)\le C\chi_f(G)
\]
for a fixed constant \(C\), then the conjecture holds in that class with threshold
\[
\left\lfloor 2C(k-1)\right\rfloor+1.
\]

---

## 5. Random tournaments dominate every sufficiently small set

All logarithms in this section are base \(2\). Define
\[
L_N=\left\lfloor
\log_2N-3\log_2\log_2N
\right\rfloor .
\tag{6}
\]

### Lemma 5.1
With high probability, every nonempty \(X\subseteq[N]\) with \(|X|\le L_N\) has a vertex \(v\notin X\) satisfying
\[
v\to x\qquad\text{for every }x\in X.
\tag{7}
\]

### Proof

For a fixed \(s\)-set \(X\), the probability that no outside vertex dominates all of \(X\) is
\[
(1-2^{-s})^{N-s}
 \le \exp\bigl(-(N-s)2^{-s}\bigr).
\]
For \(s\le L_N\),
\[
(N-s)2^{-s}\ge \frac12(\log_2N)^3
\]
for sufficiently large \(N\). Therefore
\[
\Pr(\text{some such }X)
 \le L_NN^{L_N}
       \exp\left(-\frac12(\log_2N)^3\right)=o(1),
\]
because \(\log(L_NN^{L_N})=O((\log N)^2)\). ∎

### Corollary 5.2
On the event in Lemma 5.1, every \(q\)-bad graph \(G\) satisfies
\[
\chi(G[X])\le q
\qquad\text{whenever }|X|\le L_N.
\tag{8}
\]

Indeed, otherwise a vertex \(v\) dominating \(X\) would have
\(X\subseteq N_T^+(v)\).

Thus every \(k\)-chromatic subgraph of a bad graph has more than
\[
\log_2N-3\log_2\log_2N
\]
vertices. In particular, for \(k=3\), every bad graph is either bipartite or has odd girth greater than \(L_N\).

---

## 6. An improved logarithmic upper bound

The preceding small-set property can be combined with a tournament elimination argument.

### Proposition 6.1
With high probability, every \(q\)-bad graph satisfies
\[
\chi(G)\le
q\left(
\left\lceil
\log_2\frac{N+1}{L_N+1}
\right\rceil+2
\right).
\tag{9}
\]
Equivalently, for fixed \(k\),
\[
\chi(G)
 \le (k-1)\log_2N
 -(k-1)\log_2\log_2N
 +O_k(1).
\tag{10}
\]

### Proof

Assume the event in Lemma 5.1. Start with \(R_0=V(G)\). While
\(|R_i|>L_N\), choose \(v_i\in R_i\) with
\[
d^+_{T[R_i]}(v_i)\ge\frac{|R_i|-1}{2}.
\]
Such a vertex exists because the average outdegree in a tournament on \(R_i\) is \((|R_i|-1)/2\). Put
\[
A_i=N_T^+(v_i)\cap R_i,\qquad
R_{i+1}=N_T^-(v_i)\cap R_i.
\]
Then
\[
|R_{i+1}|\le \frac{|R_i|-1}{2},
\]
and hence
\[
|R_i|+1\le \frac{N+1}{2^i}.
\]
The process therefore stops after at most
\[
t=
\left\lceil
\log_2\frac{N+1}{L_N+1}
\right\rceil
\tag{11}
\]
iterations.

Each \(G[A_i]\) is \(q\)-colorable because
\(A_i\subseteq N_T^+(v_i)\).

Let \(P=\{v_0,\ldots,v_{t-1}\}\) be the pivot set. If \(j>i\), then
\(v_j\in R_{i+1}\), so \(v_j\to v_i\). Thus \(T[P]\) is transitive.

If the final residual set \(R_t\) is nonempty, every \(x\in R_t\) dominates every vertex of \(P\). Hence
\[
P\subseteq N_T^+(x),
\]
so \(G[P]\) is \(q\)-colorable. Moreover \(|R_t|\le L_N\), so \(G[R_t]\) is \(q\)-colorable by Corollary 5.2.

If \(R_t=\varnothing\), the last pivot dominates all earlier pivots. Hence \(P\) is colorable with at most \(q+1\le2q\) colors.

Using disjoint palettes for the sets \(A_i\), the pivots, and the residual set gives
\[
\chi(G)\le tq+2q,
\]
which is (9). Since \(L_N=(1+o(1))\log_2N\), equation (10) follows. ∎

For \(k=3\), a possible bad graph therefore has to satisfy simultaneously
\[
\chi_f(G)\le4+o(1),\qquad
\operatorname{odd\,girth}(G)>
\log_2N-3\log_2\log_2N,
\]
and
\[
\chi(G)\le
2\log_2N-2\log_2\log_2N+O(1).
\]

---

## 7. A strong estimate for graphs chosen independently of \(T\)

The adversarial dependence of \(G\) on \(T\) is essential. If \(G\) is fixed in advance, one obtains an exponentially small failure probability.

### Proposition 7.1
Let \(r\ge2q+2\) and put
\[
s=r-(2q+1).
\]
For every fixed graph \(G\) on \([N]\) with \(\chi(G)\ge r\),
\[
\Pr_T\bigl((T,G)\text{ is \(q\)-bad}\bigr)
 \le
2^{-\frac{s}{r}N}
=
2^{-\left(1-\frac{2q+1}{r}\right)N}.
\tag{12}
\]

### Proof

Choose an induced subgraph \(F\subseteq G\) minimal subject to
\(\chi(F)\ge r\). Then \(\chi(F)=r\) and \(F\) is vertex-critical.

Let \(m=|V(F)|\), and fix a proper \(r\)-coloring of \(F\), with color classes
\[
C_1,\ldots,C_r.
\]
Let \(C\) be the union of the \(s\) largest color classes and put
\[
U=V(F)\setminus C.
\]
Then
\[
|C|\ge\frac{sm}{r}.
\tag{13}
\]
The graph \(F[U]\) is colorable with \(r-s=2q+1\) colors. It cannot be \(2q\)-colorable, because then coloring each of the removed \(s\) independent classes with one fresh color would give an \((r-1)\)-coloring of \(F\). Hence
\[
\chi(F[U])=2q+1.
\tag{14}
\]

Let \(Z=[N]\setminus U\). From (13),
\[
|Z|=N-m+|C|
 \ge N-m+\frac{sm}{r}
 \ge \frac{sN}{r}.
\tag{15}
\]

For each \(z\in Z\), the set
\[
R_z=U\cap N_T^+(z)
\]
is a uniformly random subset of \(U\), and the sets \(R_z\), \(z\in Z\), are mutually independent because they depend on disjoint sets of tournament arcs.

For a uniformly random \(R\subseteq U\), let
\[
p=\Pr\bigl(\chi(F[R])\le q\bigr).
\]
At most one of \(R\) and \(U\setminus R\) can induce a \(q\)-colorable graph: otherwise \(F[U]\) would be \(2q\)-colorable using disjoint palettes, contrary to (14). Pairing every subset with its complement gives
\[
p\le\frac12.
\]
If \((T,G)\) is \(q\)-bad, then \(F[R_z]\) is \(q\)-colorable for every \(z\in Z\). Therefore
\[
\Pr_T\bigl((T,G)\text{ is \(q\)-bad}\bigr)
 \le p^{|Z|}
 \le 2^{-|Z|}
 \le 2^{-sN/r}.
\]
∎

Consequently, the conjectured conclusion holds uniformly for any predetermined family of at most
\[
2^{\left(1-\frac{2q+1}{r}-\varepsilon\right)N}
\]
graphs of chromatic number at least \(r\).

This still falls far short of the adaptive problem: the collection of all labeled graphs, or even all local labeling systems in (2), has size exponential in \(N^2\), while (12) only gives an exponential-in-\(N\) estimate.

---

## 8. Restricted graph classes

The common-dominator property for fixed-size sets immediately proves the conjecture for every fixed \(\chi\)-bounded class.

Suppose a graph class satisfies
\[
\chi(G)\le f(\omega(G))
\]
for a fixed nondecreasing function \(f\). If
\[
\chi(G)\ge f(k-1)+1,
\]
then \(G\) contains a \(K_k\). With high probability every \(k\)-set \(X\) has a vertex dominating all of \(X\), since
\[
\Pr(\text{some \(k\)-set has no common dominator})
 \le
\binom Nk(1-2^{-k})^{N-k}=o(1).
\]
That out-neighborhood contains a \(K_k\), and hence has chromatic number at least \(k\).

In particular, for perfect graphs the sharp natural threshold \(\chi=k\) works.

---

## 9. A necessary lower bound on the conjectured constant

For \(k\ge3\), any valid constant in the original conjecture must be at least \(k+1\).

Indeed, for infinitely many \(N\), let
\[
G=K_{k-3}\vee C_m,
\qquad m=N-k+3
\]
where \(m\) is odd. Here \(\vee\) denotes the graph join. Then
\[
\chi(G)=(k-3)+3=k.
\]
Moreover \(G\) is vertex-critical:

- deleting a vertex of the clique leaves chromatic number \(k-1\);
- deleting a cycle vertex turns \(C_m\) into a bipartite path, again leaving chromatic number \(k-1\).

Thus every proper induced subgraph of \(G\) is \((k-1)\)-colorable. For every tournament \(T\) and every vertex \(v\),
\[
N_T^+(v)\subseteq V(G)\setminus\{v\},
\]
so
\[
\chi\bigl(G[N_T^+(v)]\bigr)\le k-1.
\]
Hence no choice \(\chi\le k\) can satisfy the conjecture for \(k\ge3\).

---

## 10. Remaining gap

The unresolved task can be stated precisely using (2): prove that, with high probability,
\[
\max_c\chi(H_c)
\]
is bounded solely as a function of \(q\).

The arguments above establish only
\[
\max_c\chi_f(H_c)\le2q+o(1)
\]
and
\[
\max_c\chi(H_c)
 \le q\log_2N-q\log_2\log_2N+O_q(1).
\]
They also show that every \(k\)-chromatic obstruction in a bad graph has order greater than approximately \(\log_2N\).

Neither bounded fractional chromatic number nor absence of bounded-order chromatic obstructions alone forces bounded ordinary chromatic number. The fixed-graph estimate cannot simply be union-bounded, because the graph and all its local colorings may be selected after the entire random tournament is exposed. This adaptivity is the substantive gap, and none of the arguments above removes it.