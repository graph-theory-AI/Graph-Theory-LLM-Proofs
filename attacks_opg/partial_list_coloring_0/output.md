```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The ratio inequality holds for every balanced complete tripartite graph and, for each fixed k, for all sufficiently large balanced complete k-partite graphs.",
  "would_publish": false,
  "caveats": "General graphs are not settled; novelty of these self-contained special-case results has not been checked."
}
```

# Partial results

All graphs below are finite. Write
\[
B_{k,m}=K_{\underbrace{m,\ldots,m}_{k\text{ parts}}}.
\]

I establish the following two special cases.

**Theorem 1.** For every \(m\ge 1\),
\[
\frac{\lambda_r(B_{3,m})}{r}\ge
\frac{\lambda_s(B_{3,m})}{s}
\qquad(1\le r\le s).
\]

**Theorem 2.** For each fixed \(k\ge2\), there is \(M(k)\) such that, whenever \(m\ge M(k)\),
\[
\frac{\lambda_r(B_{k,m})}{r}\ge
\frac{\lambda_s(B_{k,m})}{s}
\qquad(1\le r\le s).
\]

These statements allow all positive \(r\le s\), not just those at most the list chromatic number. No claim of novelty is made.

## 1. Palette partitions

Suppose \(G\) has a proper vertex partition \(V_1,\ldots,V_k\), and let \(\mathcal L\) be a \(t\)-list assignment. Independently assign each color appearing in the lists to one of \(k\) palette classes, uniformly at random.

Color a vertex \(v\in V_i\) whenever its list contains a color assigned to palette class \(i\). All such vertices can be colored simultaneously: each \(V_i\) is independent, and different vertex classes use disjoint palettes.

Put
\[
g_k(t)=1-\left(1-\frac1k\right)^t.
\]
Each vertex is colored with probability \(g_k(t)\). Consequently,
\[
\lambda_t(G)\ge \left\lceil |V(G)|g_k(t)\right\rceil. \tag{1}
\]

For \(B_{k,m}\), this can be slightly strengthened when \(k,t\ge2\):
\[
\boxed{\quad
\lambda_t(B_{k,m})\ge
\left\lfloor kmg_k(t)\right\rfloor+1.
\quad} \tag{2}
\]
Indeed, the outcome assigning every color to the first palette class colors exactly \(m\) vertices, whereas the expectation is
\[
kmg_k(t)>m.
\]
Thus the maximum number colored is strictly greater than the expectation.

For a **complete** multipartite graph, palette partitions also characterize the optimum for a fixed list assignment. A color used in a proper partial coloring cannot occur in two different parts. Assigning unused colors arbitrarily therefore extends the used colors to a partition of the whole palette. Conversely, any such palette partition permits coloring every vertex whose list meets the palette assigned to its part.

We will also use
\[
\lambda_t(B_{k,a+b})
\le \lambda_t(B_{k,a})+\lambda_t(B_{k,b}). \tag{3}
\]
To see this, split each part into sets of sizes \(a\) and \(b\), put extremal list assignments on the two resulting complete multipartite subgraphs, and use disjoint color palettes. A partial coloring restricts to a partial coloring of each subgraph, giving the bound. We interpret \(B_{k,0}\) as empty.

Finally, for every graph,
\[
\lambda_1(G)=\alpha(G),\qquad
\lambda_s(G)\le s\alpha(G). \tag{4}
\]
The second inequality follows by giving every vertex the same \(s\)-element list. Thus all pairs with \(r=1\) already satisfy the conjecture.

## 2. Proof of Theorem 1

Write \(T_m=B_{3,m}\). From (2),
\[
\lambda_2(T_m)\ge A(m):=\left\lfloor\frac{5m}{3}\right\rfloor+1, \tag{5}
\]
and
\[
\lambda_3(T_m)\ge B(m):=
\left\lfloor\frac{19m}{9}\right\rfloor+1
=2m+\left\lfloor\frac m9\right\rfloor+1. \tag{6}
\]

It is enough to prove the inequalities for adjacent indices.

### 2.1. All adjacent indices \(r\ge4\)

For \(r\ge4\),
\[
(r+1)\left(\frac23\right)^r\le1.
\]
At \(r=4\) the left side is \(80/81\), and its ratio at successive indices is
\[
\frac{2(r+2)}{3(r+1)}\le1.
\]
Hence (1) gives
\[
\lambda_r(T_m)\ge 3m\frac r{r+1}.
\]
Since \(\lambda_{r+1}(T_m)\le3m\),
\[
\frac{\lambda_r(T_m)}r
\ge\frac{3m}{r+1}
\ge\frac{\lambda_{r+1}(T_m)}{r+1}. \tag{7}
\]

Together with (4), this leaves only the adjacent pairs \((2,3)\) and \((3,4)\).

### 2.2. The pair \((2,3)\)

We first construct an upper bound for \(\lambda_3(T_m)\).

Use the palette \([4]\). In each part, assign the four possible lists
\[
[4]\setminus\{i\},\qquad i\in[4],
\]
with multiplicities \(x_1,\ldots,x_4\) as equal as possible, totaling \(m\).

If all three parts receive nonempty palettes, their palette sizes are \(2,1,1\). A part receiving two colors can color all its vertices. A part receiving only color \(i\) misses exactly \(x_i\) vertices. Thus the optimum is bounded by \(3m\) minus the sum of the two smallest multiplicities. A palette partition with an empty class colors at most \(2m\), which does not exceed that bound.

Writing \(m=4a+b\), \(0\le b<4\), gives
\[
\lambda_3(T_m)\le
U_3(m):=3m-2a-\mathbf1_{\{b=3\}}.
\]
Equivalently,
\[
U_3(m)=\frac52m+\varepsilon_m,
\]
where
\[
\begin{array}{c|cccc}
m\bmod4&0&1&2&3\\ \hline
\varepsilon_m&0&\tfrac12&1&\tfrac12
\end{array}
\]
while
\[
\frac32A(m)=\frac52m+\eta_m,
\qquad
\begin{array}{c|ccc}
m\bmod3&0&1&2\\ \hline
\eta_m&\tfrac32&\tfrac12&1.
\end{array}
\]
Therefore
\[
U_3(m)\le\frac32A(m)
\]
except possibly when
\[
m\equiv10\pmod{12}. \tag{8}
\]

For that residue class, use one additional construction. On \(T_{10}\), give the vertices in each part the ten distinct 3-subsets of a five-color palette.

A partition of the palette into three nonempty classes has sizes either \(2,2,1\) or \(3,1,1\). These allow respectively
\[
9+9+6=24
\quad\text{or}\quad
10+6+6=22
\]
colored vertices. If a palette class is empty, at most \(20\) vertices are colored. Hence
\[
\lambda_3(T_{10})\le24. \tag{9}
\]

Now let \(m=10+12q\), where \(q\ge0\). By (3), (9), and the four-color construction on \(T_{12q}\),
\[
\lambda_3(T_m)
\le24+30q
=\frac52m-1
\le\frac32A(m).
\]
Thus every \(m\ge1\) satisfies
\[
\lambda_3(T_m)\le\frac32\lambda_2(T_m),
\]
which proves the pair \((2,3)\).

### 2.3. The pair \((3,4)\)

Use a five-color palette, and in each part give the five lists
\[
[5]\setminus\{i\},\qquad i\in[5],
\]
multiplicities as equal as possible.

In any partition of five colors among three parts, some part receives at most one color. If it receives one color, at least \(\lfloor m/5\rfloor\) vertices in that part miss it; if it receives no color, all \(m\) vertices are missed. Therefore
\[
\lambda_4(T_m)\le
U_4(m):=3m-\left\lfloor\frac m5\right\rfloor. \tag{10}
\]

By (6), the desired inequality follows whenever
\[
3U_4(m)\le4B(m).
\]
After rearrangement, this is
\[
F(m):=
m-3\left\lfloor\frac m5\right\rfloor
 -4\left\lfloor\frac m9\right\rfloor
\le4. \tag{11}
\]

Here
\[
F(45q+h)=F(h)-2q,\qquad 0\le h<45.
\]
The required finite arithmetic is summarized by
\[
\begin{array}{c|rrrrrr}
\text{range of }h&0\!:\!7&8&9\!:\!17&18\!:\!26&27\!:\!35&36\!:\!44\\ \hline
\max F(h)&4&5&4&4&4&4.
\end{array}
\]
Thus (11) holds for every positive \(m\) except \(m=8\).

#### The exceptional value \(m=8\)

We construct a 4-list assignment on \(T_7\) that permits coloring at most \(19\) vertices.

Use the palette \(\mathbb Z_7\), and let
\[
\mathcal F=
\bigl\{\{i,i+1,i+3\}:i\in\mathbb Z_7\bigr\},
\]
with addition modulo \(7\). Each color belongs to three members of \(\mathcal F\), and each pair of colors belongs to exactly one member. The latter follows because the six ordered nonzero differences between elements of \(\{0,1,3\}\) are precisely the six nonzero residues modulo \(7\).

In each part of \(T_7\), use the seven lists
\[
\mathbb Z_7\setminus F,\qquad F\in\mathcal F.
\]

Consider any partition of the seven colors among the three parts.

- If some part receives at most one color, at least three vertices are missed.
- Otherwise the palette sizes are \(3,2,2\). Each two-color palette is contained in one member of \(\mathcal F\), so each corresponding part has an uncolored vertex.

Every partial coloring therefore misses at least two vertices, giving
\[
\lambda_4(T_7)\le19.
\]
Using (3),
\[
\lambda_4(T_8)\le19+3=22.
\]
On the other hand, (6) gives \(\lambda_3(T_8)\ge17\), and consequently
\[
3\lambda_4(T_8)\le66<68\le4\lambda_3(T_8).
\]

This completes the pair \((3,4)\). All adjacent inequalities have now been proved, and chaining them proves Theorem 1.

## 3. Proof of Theorem 2

The key asymptotic formula is
\[
\boxed{\qquad
\lim_{m\to\infty}
\frac{\lambda_t(B_{k,m})}{km}
=
1-\left(1-\frac1k\right)^t
\qquad} \tag{12}
\]
for each fixed \(k\ge2\) and \(t\ge1\).

The lower bound follows from (1). For the upper bound, let \(q\ge t\) be divisible by \(k\), and put
\[
N=\binom qt.
\]
On \(B_{k,N}\), give each part exactly one copy of every \(t\)-subset of a \(q\)-color palette.

If the palette classes have sizes \(a_1,\ldots,a_k\), the number of vertices that cannot be colored is
\[
\sum_{i=1}^k\binom{q-a_i}{t}.
\]
We use the convention \(\binom bt=0\) for \(0\le b<t\). The sequence \(b\mapsto\binom bt\) is discretely convex: its first differences are \(\binom b{t-1}\), which are nondecreasing. Since \(\sum_i a_i=q\), balancing the \(a_i\)'s minimizes the displayed sum. Consequently,
\[
\lambda_t(B_{k,N})
\le
k\left[
\binom qt-\binom{q-q/k}{t}
\right]. \tag{13}
\]

For arbitrary \(m=dN+u\), \(0\le u<N\), apply (3) and the trivial bound on the remaining \(ku\) vertices. This yields the explicit estimate
\[
\frac{\lambda_t(B_{k,m})}{km}
\le
1-\frac{\binom{q-q/k}{t}}{\binom qt}
+\frac{\binom qt}{m}. \tag{14}
\]
First let \(m\to\infty\) with \(q\) fixed, and then let \(q\to\infty\) through multiples of \(k\). Since
\[
\frac{\binom{q-q/k}{t}}{\binom qt}
\longrightarrow
\left(1-\frac1k\right)^t,
\]
equation (12) follows.

### Uniformity over all list sizes

Pointwise convergence in (12) alone would not suffice, because the conjecture involves a range of indices growing with \(m\). A uniform cutoff handles this issue.

Set \(a=1-1/k\). Then
\[
\frac{g_k(t)}t
=
\frac1{kt}\sum_{j=0}^{t-1}a^j
\]
is strictly decreasing in \(t\): it is the average of the first \(t\) terms of a strictly decreasing positive sequence, divided by \(k\).

Choose \(R=R(k)\) such that
\[
(r+1)a^r\le1\qquad(r\ge R).
\]
Such an \(R\) exists because \((r+1)a^r\to0\). For every \(m\) and \(r\ge R\), (1) gives
\[
\frac{\lambda_r(B_{k,m})}{r}
\ge\frac{km}{r+1}
\ge\frac{\lambda_{r+1}(B_{k,m})}{r+1}. \tag{15}
\]

There are only finitely many remaining adjacent pairs, namely \(1\le r<R\). For each such \(r\), (12) and strict decrease give
\[
\begin{aligned}
\lim_{m\to\infty}\frac1{km}
\left(
\frac{\lambda_r(B_{k,m})}{r}
-\frac{\lambda_{r+1}(B_{k,m})}{r+1}
\right)
&=
\frac{g_k(r)}r-\frac{g_k(r+1)}{r+1}\\
&>0.
\end{aligned}
\]
Thus all these finitely many inequalities hold once \(m\) exceeds a common threshold \(M(k)\). Together with (15), this proves every adjacent inequality, and hence Theorem 2.

The argument is effective: after choosing \(R\), estimate (14) can be used to obtain a numerical threshold for the finitely many smaller indices.

## 4. Scope and remaining gap

The proofs above establish genuine special cases of the stronger ratio conjecture, rather than merely its \(s=\chi_\ell\) specialization.

They do **not** settle arbitrary graphs. In particular, the upper-bound constructions rely on the fact that a color cannot be reused in different parts of a complete multipartite graph. That property is lost for general multipartite graphs, so the exact tripartite proof cannot simply be transferred to their subgraphs.

No general proof or counterexample is established here, and the prior literature status of these particular special cases has not been verified.