```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The worst-case exponent remains open, but the consecutive matching has exact Ramsey number 3n/2, while the crossing and nested matchings have linear Ramsey number with explicit bounds.",
  "would_publish": false,
  "caveats": "The general maximum is not improved, and novelty of the structured-case results was not checked exhaustively."
}
```

# Mathematical writeup

## 1. Formulation and scope

Write \(r_<(H,K_3)\) for the least \(N\) such that every red-blue coloring of the ordered complete graph on \([N]\) contains either a red order-preserving copy of \(H\) or a blue triangle.

For even \(n\), the natural worst-case quantity is
\[
R_{\mathrm{match}}(n)
 =\max\{r_<(M,K_3):M\text{ is an ordered perfect matching on }n\text{ vertices}\}.
\]
This distinction matters: there cannot be a single pointwise order of magnitude valid for every ordered matching. Some ordered matchings have linear Ramsey number, as proved below, whereas the lower bound quoted in the question gives matchings with Ramsey number
\[
\Omega\!\left((n/\log n)^{4/3}\right).
\]

The following partial results are self-contained.

### Theorem 1

Let \(m\geq 1\), and define ordered matchings on \(2m\) vertices by
\[
D_m=\{(1,2),(3,4),\ldots,(2m-1,2m)\},
\]
\[
X_m=\{(i,m+i):1\leq i\leq m\},
\]
and
\[
N_m=\{(i,2m+1-i):1\leq i\leq m\}.
\]
Thus \(D_m\) is the consecutive matching, \(X_m\) is the pairwise-crossing matching, and \(N_m\) is the fully nested matching. Then:

1. 
   \[
   r_<(D_m,K_3)=3m.
   \]

2. For \(X_m\) and \(N_m\),
   \[
   4m-1
   \leq r_<(X_m,K_3),\,r_<(N_m,K_3)
   \leq
   \left\lceil(3+\sqrt2)m\right\rceil
   +
   \left\lceil(1+\sqrt2)m\right\rceil.
   \]
   In terms of \(n=2m\),
   \[
   2n-1\leq r_<(X_m,K_3),\,r_<(N_m,K_3)
   \leq (2+\sqrt2)n+2.
   \]

The upper bound in part 2 follows from a more general reduction to forbidden permutation matrices.

---

## 2. Exact value for the consecutive matching

### Upper bound

Consider a red-blue coloring of \(K_{3m}\) with no blue triangle. Partition the ordered vertex set into \(m\) consecutive triples.

Every triple contains a red edge, since otherwise that triple would be a blue triangle. Choosing one red edge from each triple gives \(m\) red edges whose endpoint intervals are pairwise separated. They form an ordered copy of \(D_m\). Hence
\[
r_<(D_m,K_3)\leq 3m.
\]

### Lower bound

On \(3m-1\) ordered vertices, arrange
\[
G_0,\ s_1,\ G_1,\ s_2,\ldots,s_{m-1},G_{m-1},
\]
where every \(G_i\) consists of two consecutive vertices and each \(s_i\) is a single separator vertex. Thus there are \(2m+(m-1)=3m-1\) vertices.

Color the edge inside each \(G_i\) blue and color every other edge red. The blue graph is a matching, so it contains no blue triangle.

Let
\[
S=\{s_1,\ldots,s_{m-1}\}.
\]
For every red edge \(uv\), the closed order interval \([u,v]\) contains a vertex of \(S\): the only edge whose interval lies entirely inside one of the two-vertex gaps \(G_i\) is the blue edge of that gap.

In an ordered copy of \(D_m\), the \(m\) red edge-intervals are pairwise disjoint. Since each would have to contain a separator, they would require \(m\) distinct vertices of \(S\), but \(|S|=m-1\). Thus there is no red \(D_m\).

Therefore
\[
r_<(D_m,K_3)\geq 3m,
\]
proving the equality.

---

## 3. A forbidden-matrix reduction for interval-chromatic-two matchings

Let \(\pi\in S_m\). Define the ordered matching \(M_\pi\) on \([2m]\) by
\[
E(M_\pi)=\{\,i(m+\pi(i)):1\leq i\leq m\,\}.
\]
All left endpoints precede all right endpoints.

For positive integers \(p,q\), let \(\operatorname{ex}_\pi(p,q)\) denote the largest number of ones in a \(p\times q\) zero-one matrix which does not contain rows
\[
r_1<\cdots<r_m
\]
and columns
\[
c_1<\cdots<c_m
\]
such that all entries
\[
(r_i,c_{\pi(i)}),\qquad 1\leq i\leq m,
\]
are one.

### Proposition 2

If
\[
p-\frac{\operatorname{ex}_\pi(p,q)}q\geq 2m,
\]
then
\[
r_<(M_\pi,K_3)\leq p+q.
\]

#### Proof

Consider a coloring on \(p+q\) ordered vertices with no blue triangle. Let \(L\) be the first \(p\) vertices and \(R\) the last \(q\) vertices.

Form the \(p\times q\) matrix whose one-entries are the red edges between \(L\) and \(R\). If this matrix contains the permutation pattern \(\pi\), it gives a red ordered copy of \(M_\pi\).

Otherwise, there are at most \(\operatorname{ex}_\pi(p,q)\) red edges between \(L\) and \(R\). Hence some \(z\in R\) has at most
\[
\frac{\operatorname{ex}_\pi(p,q)}q
\]
red neighbors in \(L\), and therefore at least \(2m\) blue neighbors in \(L\).

The blue neighborhood of \(z\) is a red clique: two blue-adjacent vertices in that neighborhood, together with \(z\), would form a blue triangle. Thus \(L\) contains a red \(K_{2m}\), which contains an order-preserving copy of every ordered matching on \(2m\) vertices, including \(M_\pi\). ∎

In particular,
\[
r_<(M_\pi,K_3)\leq
2\min\left\{t:
t-\frac{\operatorname{ex}_\pi(t,t)}t\geq 2m
\right\}.
\]
The usefulness of this statement depends on controlling the forbidden-matrix coefficient uniformly as \(\pi\) and \(m\) vary.

---

## 4. Exact matrix extremal number for monotone permutations

For the identity permutation, a copy is a chain of \(m\) cells under
\[
(i,j)\prec(i',j')
\quad\Longleftrightarrow\quad
i<i'\ \text{ and }\ j<j'.
\]

### Lemma 3

If \(h\leq \min\{p,q\}\), the largest subset of \([p]\times[q]\) containing no chain of length \(h+1\) is
\[
h(p+q-h).
\]

#### Proof

First, an antichain in a \(P\times Q\) grid has size at most \(P+Q-1\). Indeed, suppose its nonempty rows are
\[
i_1<\cdots<i_s.
\]
In row \(i_\ell\), let \(a_\ell\) and \(b_\ell\) be the minimum and maximum occupied columns. The antichain condition gives
\[
b_{\ell+1}\leq a_\ell.
\]
Consequently,
\[
\begin{aligned}
|A|
&\leq \sum_{\ell=1}^s(b_\ell-a_\ell+1)\\
&=b_1-a_s+s+\sum_{\ell=2}^s(b_\ell-a_{\ell-1})\\
&\leq Q-1+s\\
&\leq P+Q-1.
\end{aligned}
\]

Now let \(F\subseteq[p]\times[q]\) have no chain of length \(h+1\). Give each cell \(x\in F\) the rank \(\rho(x)\), the maximum length of a chain ending at \(x\). Cells of any fixed rank \(k\) form an antichain. Moreover, a rank-\(k\) cell has both coordinates at least \(k\). Hence the rank-\(k\) cells lie in a
\[
(p-k+1)\times(q-k+1)
\]
subgrid and number at most
\[
p+q-2k+1.
\]
Therefore
\[
|F|
\leq\sum_{k=1}^h(p+q-2k+1)
=h(p+q-h).
\]

Equality is attained by
\[
F=\{(i,j):i\leq h\text{ or }j\leq h\}.
\]
It has \(h(p+q-h)\) cells, and the last cell of any chain of length \(h+1\) would have both coordinates at least \(h+1\), so it could not belong to \(F\). ∎

Taking \(h=m-1\), this gives
\[
\operatorname{ex}_{\mathrm{id}}(p,q)
=(m-1)(p+q-m+1).
\]
Reflecting the columns gives the same formula for the reversal permutation.

The identity and reversal permutation matchings are exactly \(X_m\) and \(N_m\).

### Applying Proposition 2

Put
\[
h=m-1,\qquad
p=\left\lceil(3+\sqrt2)m\right\rceil,\qquad
q=\left\lceil(1+\sqrt2)m\right\rceil.
\]
Then
\[
p-\frac{\operatorname{ex}_{\mathrm{id}}(p,q)}q
=
p-\frac{h(p+q-h)}q
=
\frac{(p-h)(q-h)}q.
\]
The last expression is nondecreasing in both \(p\) and \(q\). Set
\[
A=3+\sqrt2,\qquad B=1+\sqrt2.
\]
At the unrounded values \(p=Am\), \(q=Bm\),
\[
\begin{aligned}
\frac{(p-h)(q-h)}q
&=
\frac{((2+\sqrt2)m+1)(\sqrt2\,m+1)}
     {(1+\sqrt2)m}\\
&=2m+2+\frac{1}{(1+\sqrt2)m}\\
&>2m.
\end{aligned}
\]
Thus Proposition 2 applies to both the identity and reversal patterns. This proves
\[
r_<(X_m,K_3),\,r_<(N_m,K_3)
\leq
\left\lceil(3+\sqrt2)m\right\rceil
+
\left\lceil(1+\sqrt2)m\right\rceil.
\]

The constants are asymptotically optimal for this particular one-cut argument. If \(p\sim xm\) and \(q\sim ym\), the condition becomes
\[
\frac{(x-1)(y-1)}y\geq 2.
\]
Minimizing \(x+y\) under this constraint gives
\[
y=1+\sqrt2,\qquad x=3+\sqrt2.
\]

---

## 5. Linear lower bound for interval-indecomposable matchings

Call a cut \(k\in\{1,\ldots,n-1\}\) of an ordered matching \(M\) free if no edge of \(M\) has one endpoint at most \(k\) and the other greater than \(k\). Call \(M\) interval-indecomposable if it has no free cut.

### Lemma 4

If \(M\) is an interval-indecomposable ordered matching on \(n\) vertices, then
\[
r_<(M,K_3)\geq 2n-1.
\]

#### Proof

On \(2n-2\) vertices, take two consecutive intervals \(A<B\), each of size \(n-1\). Color all edges inside \(A\) and inside \(B\) red and all edges between \(A\) and \(B\) blue.

The blue graph is complete bipartite and hence triangle-free. A red copy of \(M\) cannot lie wholly inside \(A\) or \(B\), since each has only \(n-1\) vertices. If a copy used both intervals, the source vertices mapped into \(A\) would form a nonempty proper initial segment of \(V(M)\). Since every red edge lies within one host interval, no matching edge could cross the corresponding source cut. That would be a free cut, contrary to interval-indecomposability. ∎

Both \(X_m\) and \(N_m\) are interval-indecomposable, so Lemma 4 yields
\[
r_<(X_m,K_3),\,r_<(N_m,K_3)\geq 4m-1.
\]

---

## 6. Additivity and a parameterized improvement for decomposable matchings

If \(H_1,\ldots,H_k\) are ordered graphs, let
\[
H_1\oplus\cdots\oplus H_k
\]
denote their ordered concatenation: all vertices of \(H_i\) precede all vertices of \(H_{i+1}\), with no edges between distinct summands.

### Lemma 5

\[
r_<(H_1\oplus\cdots\oplus H_k,K_3)
\leq
\sum_{i=1}^k r_<(H_i,K_3).
\]

#### Proof

Partition a host interval of the stated size into consecutive blocks of sizes \(r_<(H_i,K_3)\). In a coloring with no blue triangle, each block contains a red copy of its corresponding \(H_i\). Their union is a red ordered copy of the concatenation. ∎

Split an ordered matching \(M\) at all its free cuts, obtaining interval-indecomposable components
\[
M=M_1\oplus\cdots\oplus M_k.
\]
Let \(n_i=|V(M_i)|\), \(n=\sum_i n_i\), and \(q=\max_i n_i\). Using the classical estimate quoted in the question,
\[
r_<(M_i,K_3)
\leq r(K_{n_i},K_3)
\leq C\frac{n_i^2}{\log(2+n_i)}.
\]
Therefore
\[
r_<(M,K_3)
\leq
C\sum_i\frac{n_i^2}{\log(2+n_i)}
\leq
C\frac{nq}{\log(2+q)}.
\]
Thus the classical \(O(n^2/\log n)\) bound improves whenever the largest interval-indecomposable component has \(q=o(n)\). In particular, bounded-size interval components give a linear bound.

---

## 7. What remains open

These results do not improve the general worst-case bounds
\[
\Omega\!\left((n/\log n)^{4/3}\right)
\leq R_{\mathrm{match}}(n)
\leq O(n^2/\log n).
\]

The matrix reduction identifies one concrete obstruction. For an arbitrary interval-chromatic-two matching \(M_\pi\), one needs useful uniform control of
\[
\operatorname{ex}_\pi(p,q)
\]
where the forbidden permutation \(\pi\) itself has size \(m\). Bounds treating \(\pi\) as fixed are insufficient because their constants may grow rapidly with \(m\). For matchings of interval chromatic number greater than two, even this single-matrix representation is unavailable.

Likewise, the component bound gives no improvement for interval-indecomposable matchings, where \(q=n\); these include the difficult permutation-matchings. Thus the exponent gap in the catalog problem remains unresolved.