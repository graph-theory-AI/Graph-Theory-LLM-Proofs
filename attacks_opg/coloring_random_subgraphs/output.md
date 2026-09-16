```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every fixed-order shift-graph family, I prove the stronger estimate E[chi(G_{1/2})] >= chi(G) - O(log chi(G)), but the general conjecture remains unresolved.",
  "would_publish": false,
  "caveats": "The constants depend on the fixed order; novelty of this special-family estimate has not been verified."
}
```

## 1. A special-case result

I do not obtain a proof for arbitrary graphs. The partial result below concerns graphs with unbounded chromatic number but fractional chromatic number at most \(4\), so it addresses a family not handled by simply replacing \(\chi\) with \(\chi_f\).

All logarithms below are to base \(2\).

For integers \(r\ge 1\) and \(N\ge r+1\), define the **shift graph** \(S_r(N)\) as follows:

- its vertices are increasing \(r\)-tuples from \([N]\);
- for each \(a_1<\cdots<a_{r+1}\), there is an edge between
  \[
  (a_1,\ldots,a_r)
  \quad\text{and}\quad
  (a_2,\ldots,a_{r+1}).
  \]

Thus \(S_1(N)=K_N\), and \(S_2(N)\) is the ordinary shift graph.

### Theorem
For every fixed integer \(r\ge2\) and every fixed \(p\in(0,1]\), there is a constant \(C_{r,p}\) such that, writing \(k=\chi(S_r(N))\),
\[
\boxed{\quad
\mathbb E\!\left[\chi\bigl((S_r(N))_p\bigr)\right]
\ge k-C_{r,p}\log k .
\quad}
\]
In particular, for fixed \(r,p\),
\[
\mathbb E\!\left[\chi\bigl((S_r(N))_p\bigr)\right]
=(1-o(1))\chi(S_r(N))
\qquad(N\to\infty).
\]

For the ordinary shift graph at \(p=1/2\), the proof gives the explicit bound
\[
\boxed{\quad
\mathbb E\!\left[\chi\bigl((S_2(N))_{1/2}\bigr)\right]
\ge k-2\log k-6,
\qquad k=\lceil\log N\rceil .
\quad}
\]

The constants are not asserted to be uniform when the order \(r\) varies.

---

## 2. Deterministic chromatic estimates for shift graphs

Give \(S_j(N)\) its canonical orientation, from
\((a_1,\ldots,a_j)\) to \((a_2,\ldots,a_{j+1})\), and call the resulting digraph \(D_j(N)\).

The vertices of \(D_j(N)\) can be identified with the arcs of \(D_{j-1}(N)\). Two such vertices are adjacent when the corresponding arcs are consecutive.

Write
\[
k_j=\chi(S_j(N)),\qquad
L_0=N,\qquad L_{i+1}=\log L_i.
\]
Iterated logarithms are used only for sufficiently large \(N\).

### Lower bound

Suppose \(S_j(N)\) has a proper \(q\)-coloring. For a vertex \(v\) of \(D_{j-1}(N)\), let \(T_v\) be the set of colors appearing on arcs entering \(v\).

If \(u\to v\) is an arc with color \(c\), then \(c\in T_v\), while \(c\notin T_u\): an incoming arc of color \(c\) at \(u\) would be adjacent to \(u\to v\). Thus \(T_u\ne T_v\).

The sets \(T_v\subseteq[q]\) therefore give a proper coloring of \(S_{j-1}(N)\) with at most \(2^q\) colors. Consequently,
\[
k_{j-1}\le 2^{k_j},
\]
and iteration from \(k_1=N\) gives
\[
k_r\ge L_{r-1}.                                      \tag{1}
\]

### Upper bound

Let
\[
h(m)=\min\left\{s:\binom{s}{\lfloor s/2\rfloor}\ge m\right\}.
\]
A proper \(m\)-coloring of \(S_{j-1}(N)\) gives an \(h(m)\)-coloring of \(S_j(N)\):

Assign distinct subsets of \([h(m)]\), all of the same size, to the \(m\) colors. Denote the subset assigned to a vertex \(v\) by \(A_v\). Color the arc \(u\to v\) by any element of \(A_u\setminus A_v\). This difference is nonempty because adjacent vertices have different, equally sized subsets.

For consecutive arcs \(u\to v\) and \(v\to w\), the first assigned color lies outside \(A_v\), while the second lies inside \(A_v\). Hence the coloring is proper.

Since
\[
\binom{s}{\lfloor s/2\rfloor}\ge \frac{2^s}{s+1},
\]
we have
\[
h(m)=\log m+O(\log\log m).
\]
For every fixed \(r\), iteration yields
\[
L_{r-1}\le k_r\le L_{r-1}+O_r(L_r).                  \tag{2}
\]

For \(r=2\), the exact answer is
\[
k_2=\lceil\log N\rceil.                              \tag{3}
\]
The lower bound follows above. For the upper bound, label \([N]\) by the binary representations of \(0,\ldots,N-1\), and color \((a,b)\) by the most significant bit at which the two labels differ. Consecutive pairs \((a,b),(b,c)\), with \(a<b<c\), cannot receive the same color.

---

## 3. A color-type lemma

The main device turns a coloring of a shift graph into a coloring of the preceding shift graph, with a controlled set of exceptional edges.

Say that a graph is **\(d\)-orientable** if it admits an orientation with maximum outdegree at most \(d\). Such a graph satisfies
\[
e(F[U])\le d|U|                                      \tag{4}
\]
for every vertex set \(U\).

For a vertex \(v\) of \(D_{j-1}(N)\), the incoming and outgoing arcs form the two sides of a complete bipartite graph in \(S_j(N)\).

### Lemma
Suppose the vertices of \(S_j(N)\), equivalently the arcs of \(D_{j-1}(N)\), are assigned \(q\) colors. Suppose that for every vertex \(v\) of \(D_{j-1}(N)\) and every color \(c\), either

- fewer than \(t\) incoming arcs at \(v\) have color \(c\), or
- fewer than \(t\) outgoing arcs at \(v\) have color \(c\).

Then there is a subgraph \(F\subseteq S_{j-1}(N)\) such that

1. \(S_{j-1}(N)-F\) is \(2^q\)-colorable;
2. \(F\) is \(q(t-1)\)-orientable.

#### Proof

Let
\[
T_v=\{c:\text{at least \(t\) incoming arcs at \(v\) have color \(c\)}\}.
\]
Every color in \(T_v\) occurs on at most \(t-1\) outgoing arcs at \(v\). Every color outside \(T_v\) occurs on at most \(t-1\) incoming arcs.

Let \(F\) consist of the edges whose endpoints have the same set \(T_v\). The type assignment \(v\mapsto T_v\) properly colors \(S_{j-1}(N)-F\) with at most \(2^q\) colors.

Consider an edge of \(F\), canonically oriented \(u\to v\), and let \(c\) be its assigned color.

- If \(c\in T_u=T_v\), charge the edge to \(u\).
- If \(c\notin T_u=T_v\), charge it to \(v\).

At any vertex \(v\), at most
\[
|T_v|(t-1)+(q-|T_v|)(t-1)=q(t-1)
\]
edges are charged. Orient each edge of \(F\) away from its charged endpoint. This proves the second assertion. \(\square\)

The lemma is deterministic and holds for every coloring satisfying its hypothesis. This uniformity is important when the coloring is chosen after revealing the random graph.

---

## 4. Random rectangles and sparse deletions

Assume \(0<p<1\), and put
\[
b=-\log(1-p)>0,\qquad
L=\log N,\qquad
t=\left\lceil\frac{2L}{b}\right\rceil+r.
\]

### 4.1. The random graph has no large empty local rectangle

Each middle \((r-1)\)-tuple indexes a complete bipartite graph in \(S_r(N)\): its left side consists of incoming extensions, and its right side of outgoing extensions. There are at most \(N^{r-1}\) such bipartite graphs, each having at most \(N\) vertices on either side.

For fixed sets of \(t\) vertices on each side, the probability that all \(t^2\) edges are absent from \((S_r(N))_p\) is
\[
(1-p)^{t^2}=2^{-bt^2}.
\]
A union bound shows that the probability of any empty local \(t\times t\) rectangle is at most
\[
N^{r-1+2t}2^{-bt^2}.
\]
Our choice of \(t\) gives
\[
bt^2-2tL=t(bt-2L)\ge 2rL+br^2.
\]
Thus the failure probability is at most
\[
\delta_{N,r,p}
=(1-p)^{r^2}N^{-(r+1)}.                             \tag{5}
\]

On the complementary event, every proper \(q\)-coloring of \((S_r(N))_p\) satisfies the color-type lemma: otherwise two monochromatic sets of size \(t\) would form an empty rectangle.

Consequently,
\[
S_{r-1}(N)-F_{r-1}
\]
has a coloring with at most \(2^q\) colors, where \(F_{r-1}\) is \(q(t-1)\)-orientable.

### 4.2. Iterating through sparse deletions

Suppose \(S_j(N)-F\) is \(q\)-colorable and \(F\) is \(d\)-orientable.

There cannot be \(2d+1\) incoming and \(2d+1\) outgoing arcs of the same color at a middle vertex. Otherwise all edges of a
\[
K_{2d+1,\,2d+1}
\]
would belong to \(F\), contradicting (4), because
\[
(2d+1)^2> d\cdot 2(2d+1).
\]

Applying the color-type lemma with \(t=2d+1\), we obtain:
\[
\begin{split}
&S_j(N)-F\text{ is \(q\)-colorable, and \(F\) is \(d\)-orientable}\\
&\qquad\Longrightarrow\\
&S_{j-1}(N)-F'\text{ is \(2^q\)-colorable, and \(F'\) is \(2qd\)-orientable}.
\end{split}                                                        \tag{6}
\]

At the bottom of the iteration, suppose \(K_N-F\) is \(m\)-colorable and \(F\) is \(d\)-orientable. Each color class of size \(s\) induces a clique in \(F\), so
\[
\binom{s}{2}\le ds.
\]
Hence \(s\le2d+1\), and therefore
\[
N\le m(2d+1).                                       \tag{7}
\]

### 4.3. The resulting numerical inequality

Define
\[
E_0(x)=x,\qquad E_{i+1}(x)=2^{E_i(x)}.
\]
Let
\[
q=\chi((S_r(N))_p).
\]

Starting from Section 4.1 and iterating (6), the final color palette has size
\[
E_{r-1}(q),
\]
and the final exceptional graph has an orientation with maximum outdegree at most
\[
2^{r-2}q(t-1)\prod_{i=1}^{r-2}E_i(q).
\]
The product is empty when \(r=2\).

By (7), on the event from Section 4.1,
\[
N\le
E_{r-1}(q)
\left(
2^{r-1}q(t-1)\prod_{i=1}^{r-2}E_i(q)+1
\right).                                           \tag{8}
\]

---

## 5. Extracting the chromatic lower bound

Taking logarithms in (8), and using \(A+1\le2A\) for \(A\ge1\), gives
\[
L\le
E_{r-2}(q)
+\sum_{i=0}^{r-3}E_i(q)
+\log q+\log(t-1)+r.                                \tag{9}
\]
Again, the sum is empty when \(r=2\).

### Ordinary shift graphs

For \(r=2\), we know \(q\le\lceil L\rceil\), while \(t=O_p(L)\). Equation (9) therefore gives
\[
q\ge L-2\log L-O_p(1).                              \tag{10}
\]
Together with (3), this is
\[
q\ge k_2-2\log k_2-O_p(1).
\]

At \(p=1/2\), we have \(t=\lceil2L\rceil+2\). The \(r=2\) case of (8) gives
\[
q\ge L-\log\!\bigl(2q(t-1)+1\bigr).
\]
For \(N\ge4\), so \(L\ge2\),
\[
2q(t-1)+1
\le4(L+1)^2+1
\le16L^2.
\]
Thus
\[
q\ge L-2\log L-4
\ge k_2-2\log k_2-5                              \tag{11}
\]
with probability at least \(1-1/(16N^3)\).

Since always \(q\le k_2\), taking expectations in the loss \(k_2-q\) yields
\[
\mathbb E q\ge k_2-2\log k_2-6.
\]
The remaining case \(N=3\) satisfies this inequality trivially.

### Higher fixed orders

Now fix \(r\ge3\).

If \(E_{r-2}(q)\ge L\), then immediately
\[
q\ge L_{r-1}.
\]

Otherwise \(E_{r-2}(q)<L\). Every smaller tower in (9) is then at most \(\log L\). Also \(\log q\le\log L\), and, for fixed \(r,p\),
\[
\log(t-1)=\log L+O_{r,p}(1).
\]
Consequently,
\[
E_{r-2}(q)\ge L-O_{r,p}(\log L).
\]
Applying \(r-2\) logarithms gives
\[
q\ge L_{r-1}-o_{r,p}(1).                            \tag{12}
\]
Here the number of logarithms is fixed; replacing \(L\) by \(L-O(\log L)\) changes that iterated logarithm by \(o(1)\).

Combining (12) with the deterministic estimate (2),
\[
q\ge k_r-O_{r,p}(\log k_r)
\]
on an event of probability at least \(1-\delta_{N,r,p}\).

Finally, \(k_r\le |V(S_r(N))|\le N^r\), so
\[
\delta_{N,r,p}k_r=O(N^{-1}).
\]
Taking expectations proves
\[
\mathbb E q\ge k_r-O_{r,p}(\log k_r).
\]
Enlarging the constant covers the finitely many smaller \(N\). The case \(p=1\) is immediate. This proves the theorem.

---

## 6. Why this family is relevant—and what is still missing

For every \(r\ge2\),
\[
\chi_f(S_r(N))\le4.                                 \tag{13}
\]

Indeed, view its vertices as arcs of \(D_{r-1}(N)\). Choose a random subset \(A\) of the vertices of \(D_{r-1}(N)\), independently including each vertex with probability \(1/2\). The set
\[
I_A=\{u\to v:u\in A,\ v\notin A\}
\]
is independent in the arc graph: two consecutive arcs cannot both cross from \(A\) to its complement. Each arc belongs to \(I_A\) with probability \(1/4\). Multiplying this distribution of independent sets by \(4\) gives a fractional coloring of total weight \(4\).

The same averaging argument gives
\[
\alpha(S_r(N))\ge \frac{|V(S_r(N))|}{4}.
\]
Meanwhile \(\chi(S_r(N))\to\infty\) for every fixed \(r\). Thus these examples have an unbounded integral–fractional chromatic gap and do not satisfy an independence-number hypothesis of the form \(\alpha(G)=O(|V(G)|/\chi(G))\).

For ordinary shift graphs, \(|V(S_2(N))|=\binom N2\) and \(k\sim\log N\). A lower bound of order \(k/\log|V(G)|\) is only constant here, whereas the argument above gives \(k-O(\log k)\).

**The unresolved step for the original problem is structural.** The proof uses a specific chain of arc graphs, ending at a complete graph. Large local complete bipartite graphs turn random edge retention into a uniform restriction on every coloring; the color-type lemma then transfers the coloring down that chain with sparse errors. An arbitrary graph need not admit any such structure.

Accordingly, this is a complete special-family argument, not a proof or a counterexample to Bukh’s conjecture for general graphs.