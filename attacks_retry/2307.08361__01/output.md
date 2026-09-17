```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A finite-field construction gives quadratic bounds for sidewise almost-regular graphs and a stronger degree-scale-dependent estimate, but does not settle the unrestricted conjecture.",
  "would_publish": false,
  "caveats": "These are non-induced subgraphs; dependence on the number of degree scales remains, and novelty is not claimed."
}
```

## 1. Statement of the partial result

All graphs are finite and simple, and subgraphs need not be induced. Write
\[
h_4(G)=\max\{\overline d(H):H\subseteq G,\ H\text{ contains no }C_4\}.
\]

I do not obtain a polynomial threshold valid for arbitrary graphs. I improve the degree-dependent bounds in the supplied attempt, including replacing its cubic bound for sidewise almost-regular graphs by a quadratic one.

The change is to replace independent edge sampling and cycle deletion by a **locally injective random homomorphism into a finite-field incidence graph**. The balancing and degree-bucketing steps reused below have been checked and are proved again.

For a graph \(G\) with average degree \(D>0\) and maximum degree \(\Delta\), define
\[
L(G)=\left\lceil\log_2\left(1+\frac{4\Delta}{D}\right)\right\rceil
\]
and let
\[
s(G)=\left|\left\{\lfloor\log_2 d_G(v)\rfloor:d_G(v)>0\right\}\right|
\]
be the number of occupied dyadic degree classes. Put
\[
R(G)=\min\{L(G),\,2s(G)\}.
\]

### Theorem 1

With this notation,
\[
\boxed{
h_4(G)\ge
\max\left\{
\frac{D}{16\sqrt{\Delta}},
\frac{\sqrt D}{1024\sqrt{R(G)}\bigl(8+\log_2 R(G)\bigr)}
\right\}.
}
\tag{1}
\]

Thus, in asymptotic notation,
\[
h_4(G)=\Omega\!\left(
\frac{\sqrt{D/R(G)}}{\log(2+R(G))}
\right).
\tag{2}
\]

There is a stronger, cleaner bound under sidewise degree control.

### Theorem 2

Let \(B\) be bipartite, with parts \(A,T\), no isolated vertices, and \(m\) edges. Set
\[
x=\frac m{|A|},\qquad y=\frac m{|T|}.
\]
Suppose, for some \(K\ge1\),
\[
d(a)\le Kx\quad(a\in A),\qquad
d(t)\le Ky\quad(t\in T).
\tag{3}
\]
Then
\[
\boxed{
h_4(B)\ge \frac{\sqrt{\overline d(B)}}{32\sqrt K}.
}
\tag{4}
\]

Consequently, \(1024Kk^2\) average degree suffices in this class. In particular, a quadratic threshold suffices for all biregular bipartite graphs, regardless of the ratio between their two degrees.

No novelty claim is made for these elementary estimates.

---

## 2. A square-root sparsification lemma

The main ingredient is the following improvement over ordinary random alteration.

### Lemma 3

If \(B\) is bipartite, has average degree \(d>0\), and has maximum degree at most \(\Delta\), then
\[
h_4(B)\ge \frac{d}{8\sqrt\Delta}.
\tag{5}
\]
For an arbitrary graph \(G\),
\[
h_4(G)\ge \frac{\overline d(G)}{16\sqrt{\Delta(G)}}.
\tag{6}
\]

### Proof

Choose a power of two \(q\) satisfying
\[
2\sqrt\Delta\le q<4\sqrt\Delta.
\]
Over \(\mathbb F_q\), form a bipartite graph \(Q\) whose two parts are
\[
P=\mathbb F_q^2,\qquad \mathcal L=\mathbb F_q^2,
\]
where \((u,v)\in P\) is adjacent to \((a,b)\in\mathcal L\) precisely when
\[
v=au+b.
\]

Both parts have \(q^2\) vertices, and \(Q\) is \(q\)-regular. It is \(C_4\)-free: two distinct points lie on at most one of these lines.

Let \(X,T\) be the bipartition of \(B\). Independently label every vertex of \(X\) by a uniformly random element of \(P\), and every vertex of \(T\) by a uniformly random element of \(\mathcal L\).

Retain an edge \(xt\) only if:

1. its endpoint labels are adjacent in \(Q\);
2. no other neighbor of \(x\) has the same label as \(t\);
3. no other neighbor of \(t\) has the same label as \(x\).

Call the retained graph \(H\).

**First, \(H\) is always \(C_4\)-free.** Indeed, suppose
\[
x_1t_1x_2t_2x_1
\]
were a retained \(4\)-cycle. Conditions 2 and 3 imply that \(x_1,x_2\) have different labels and that \(t_1,t_2\) have different labels. Its four labels would therefore form a \(C_4\) in \(Q\), a contradiction.

For a fixed edge \(xt\), the probability of condition 1 is \(1/q\). Conditional on its endpoint labels being adjacent, a union bound gives
\[
\Pr(\text{condition 2 or 3 fails})
 \le \frac{d(x)+d(t)-2}{q^2}
 \le \frac{2\Delta}{q^2}
 \le \frac12.
\]
Hence
\[
\Pr(xt\in E(H))\ge \frac1{2q}\ge\frac1{8\sqrt\Delta}.
\]
By linearity of expectation, some outcome has at least
\[
\frac{e(B)}{8\sqrt\Delta}
\]
edges. Keeping the original vertex set proves (5); deleting isolated vertices can only help.

Finally, every graph has a bipartite spanning subgraph containing at least half its edges. Applying (5) to such a subgraph proves (6). \(\square\)

In particular, if \(\Delta(G)\le KD\), then
\[
h_4(G)\ge \frac{\sqrt D}{16\sqrt K}.
\tag{7}
\]
This already gives a quadratic threshold for graphs whose maximum degree is a bounded multiple of their average degree.

---

## 3. Balancing the two sides

We need a structural version of the balancing argument.

### Lemma 4

Under the hypotheses of Theorem 2, \(B\) contains a bipartite subgraph \(F\) such that
\[
\overline d(F)\ge \frac{\overline d(B)}4,
\qquad
\Delta(F)\le 4K\,\overline d(F).
\tag{8}
\]

### Proof

Write \(a=|A|\), \(b=|T|\), and interchange the parts if necessary so that \(a\le b\). Thus \(x\ge y\). Set
\[
p=\frac ab=\frac yx.
\]
Select every vertex of \(T\) independently with probability \(p\), and let \(Z\) be the number selected. Then \(\mathbb EZ=a\).

For \(u\in A\), let \(X_u\) count its selected neighbors. Its mean satisfies
\[
\mu_u=pd(u)\le pKx=Ky.
\]
Since there are no isolated vertices, \(y\ge1\). Put
\[
M=\lceil Ky\rceil,
\]
so
\[
\mu_u\le M\le 2Ky.
\]

After the selection, retain at most \(M\) selected edges at each vertex of \(A\). Let \(Y\) be the number retained.

For integers \(z\ge0\) and \(M\ge1\),
\[
\min\{z,M\}\ge z-\frac{\binom z2}{M}.
\tag{9}
\]
For \(z\le M\) this is immediate. For \(z=M+t\), \(t\ge0\), it follows from
\[
\binom z2-M(z-M)=\binom M2+\binom t2\ge0.
\]
Since \(X_u\) is binomial,
\[
\mathbb E\binom{X_u}{2}\le\frac{\mu_u^2}{2}.
\]
Therefore
\[
\mathbb E\min\{X_u,M\}
 \ge \mu_u-\frac{\mu_u^2}{2M}
 \ge \frac{\mu_u}{2}.
\]
Summing gives
\[
\mathbb EY\ge\frac{pm}{2}=\frac{ay}{2}.
\]
Consequently,
\[
\mathbb E\left[Y-\frac y4(a+Z)\right]\ge0.
\]
Some outcome therefore satisfies
\[
Y\ge \frac y4(a+Z).
\]
Its retained graph \(F\) has
\[
\overline d(F)\ge\frac y2,\qquad
\Delta(F)\le2Ky.
\tag{10}
\]

Also,
\[
\overline d(B)=\frac{2xy}{x+y}\le2y.
\]
Thus (10) implies both inequalities in (8). \(\square\)

Applying Lemma 3 directly to the graph in (10),
\[
\begin{aligned}
h_4(B)
&\ge \frac{y/2}{8\sqrt{2Ky}}\\
&=\frac{\sqrt y}{16\sqrt{2K}}\\
&\ge\frac{\sqrt{\overline d(B)}}{32\sqrt K}.
\end{aligned}
\]
This proves Theorem 2.

---

## 4. Extracting a graph with controlled degree spread

The next lemma only counts degree classes; it does not care how far apart they are.

### Lemma 5

Let \(J\) be a bipartite graph of positive average degree. Suppose each side can be partitioned into at most \(r\) classes, with the degrees within each class lying in an interval \([t,2t)\), where \(t>0\) may depend on the class.

Then \(J\) contains a bipartite subgraph \(F\) satisfying
\[
\overline d(F)\ge\frac{\overline d(J)}{12r},
\qquad
\Delta(F)\le24r\,\overline d(F).
\tag{11}
\]

### Proof

Delete isolated vertices first if necessary. Denote the classes on the two sides by \(A_i,T_j\), adding empty classes so that there are \(r\) on each side. Write
\[
e_{ij}=e(A_i,T_j),\qquad
U_i=\sum_j e_{ij},\qquad
V_j=\sum_i e_{ij}.
\]

Call a cell \((i,j)\) good if
\[
e_{ij}\ge\frac{U_i}{3r}
\quad\text{and}\quad
e_{ij}\ge\frac{V_j}{3r}.
\tag{12}
\]
The cells failing the first condition contain less than one-third of all edges; the same holds for the second condition. Thus good cells contain at least one-third of all edges.

Moreover,
\[
\sum_{i,j}(|A_i|+|T_j|)=r\,v(J).
\]
Weighted averaging therefore gives a good cell with
\[
\frac{2e_{ij}}{|A_i|+|T_j|}
 \ge \frac{\overline d(J)}{3r}.
\tag{13}
\]

Let \(P=J[A_i,T_j]\). Suppose the degrees in \(A_i\) lie in \([t,2t)\). The first inequality in (12) gives
\[
\frac{e_{ij}}{|A_i|}
 \ge\frac{U_i}{3r|A_i|}
 \ge\frac{t}{3r}.
\]
Every degree on that side of \(P\) is less than \(2t\), and hence at most
\[
6r\,\frac{e_{ij}}{|A_i|}.
\]
The analogous bound holds on the other side.

Delete isolated vertices from \(P\). Its side-average degrees only increase, so Lemma 4 applies with \(K=6r\). By (13), the resulting graph \(F\) satisfies
\[
\overline d(F)\ge\frac{\overline d(P)}4
 \ge\frac{\overline d(J)}{12r},
\]
and
\[
\Delta(F)\le4(6r)\overline d(F).
\]
This is (11). \(\square\)

### Applying the extraction lemma to an arbitrary graph

We now show that every \(G\) contains a bipartite \(F\) with
\[
\boxed{
\overline d(F)\ge\frac{D}{24R(G)},
\qquad
\Delta(F)\le24R(G)\,\overline d(F).
}
\tag{14}
\]

There are two ways to obtain the required classes.

#### Using \(L(G)\)

Take a bipartite spanning subgraph of average degree at least \(D/2\). Repeatedly delete vertices of degree less than \(D/4\). The current average degree cannot decrease, and the process leaves a nonempty graph \(J\) with
\[
\overline d(J)\ge D/2,\qquad \delta(J)\ge D/4.
\]

The intervals
\[
\left[\frac D4\,2^{i-1},\,\frac D4\,2^i\right),
\qquad 1\le i\le L(G),
\]
cover all its degrees, since
\[
2^{L(G)}D/4>\Delta.
\]
Lemma 5 therefore gives (14) with \(L(G)\) in place of \(R(G)\).

#### Using \(s(G)\)

Choose a maximum cut of \(G\), and let \(J\) be its bipartite spanning subgraph. At each vertex,
\[
\frac{d_G(v)}2\le d_J(v)\le d_G(v);
\tag{15}
\]
otherwise moving that vertex across the cut would increase the number of crossing edges.

A degree in the original interval \([2^i,2^{i+1})\) therefore becomes a degree in
\[
[2^{i-1},2^{i+1}),
\]
which meets at most two standard dyadic classes. Thus \(J\) has at most \(2s(G)\) occupied dyadic classes in total. Also \(\overline d(J)\ge D/2\).

After deleting isolated vertices, Lemma 5 gives (14) with \(2s(G)\) in place of \(R(G)\).

Choosing the better construction proves (14).

---

## 5. A second extraction improves the logarithmic loss

First apply Lemma 3 to the graph \(F\) from (14). Writing \(d_F=\overline d(F)\),
\[
\begin{aligned}
h_4(G)
&\ge \frac{d_F}{8\sqrt{\Delta(F)}}\\
&\ge \frac{\sqrt{d_F}}{8\sqrt{24R(G)}}\\
&\ge \frac{\sqrt D}{192R(G)}.
\end{aligned}
\tag{16}
\]
In particular, every graph \(X\) satisfies
\[
h_4(X)\ge
\frac{\sqrt{\overline d(X)}}{192L(X)}.
\tag{17}
\]

Now apply (17), rather than the maximum-degree estimate, to \(F\). From (14),
\[
\begin{aligned}
L(F)
&=\left\lceil\log_2\left(1+\frac{4\Delta(F)}{d_F}\right)\right\rceil\\
&\le\left\lceil\log_2(1+96R(G))\right\rceil\\
&\le 8+\log_2 R(G).
\end{aligned}
\]
Consequently,
\[
\begin{aligned}
h_4(G)
&\ge \frac{\sqrt{d_F}}{192L(F)}\\
&\ge
\frac{\sqrt D}
{192\sqrt{24R(G)}\bigl(8+\log_2 R(G)\bigr)}\\
&\ge
\frac{\sqrt D}
{1024\sqrt{R(G)}\bigl(8+\log_2 R(G)\bigr)}.
\end{aligned}
\]
Together with (6), this proves Theorem 1.

The second extraction is useful because the first one reduces the maximum-to-average degree ratio from an unrestricted value to \(O(R(G))\). Degree bucketing inside that extracted graph then costs only \(O(\log R(G))\).

---

## 6. Consequences

### 6.1 Quadratic bounds in controlled-degree classes

The results give the following sufficient thresholds:

- If \(\Delta(G)\le KD\), then
  \[
  D\ge256Kk^2
  \quad\Longrightarrow\quad h_4(G)\ge k.
  \]
- Under the sidewise hypothesis (3),
  \[
  D\ge1024Kk^2
  \quad\Longrightarrow\quad h_4(G)\ge k.
  \]
- If \(s(G)\le s\), then
  \[
  D=O\!\left(s\log^2(s+2)\,k^2\right)
  \]
  suffices, with an absolute implied constant. In particular, a fixed number of occupied degree scales gives a quadratic threshold, even when those scales are arbitrarily far apart.

The quadratic order is optimal already for biregular graphs. Indeed, in any \(C_4\)-free graph \(H\), every pair of vertices has at most one common neighbor, so
\[
\sum_{v\in V(H)}\binom{d_H(v)}2
 \le \binom{v(H)}2.
\]
By convexity,
\[
\overline d(H)\bigl(\overline d(H)-1\bigr)\le v(H)-1.
\]
Every subgraph of \(K_{t,t}\) has at most \(2t\) vertices, and hence
\[
h_4(K_{t,t})\le 1+\sqrt{2t}.
\]
Thus no subquadratic threshold can hold even within the biregular class.

### 6.2 Polynomial maximum degree

For every fixed \(A\ge1\), if \(\Delta\le D^A\), then
\[
R(G)\le L(G)=O_A(\log D).
\]
Therefore
\[
h_4(G)
=\Omega_A\!\left(
\frac{\sqrt D}{\sqrt{\log D}\,\log\log D}
\right)
\qquad(D\to\infty).
\tag{18}
\]
Inverting this bound shows that, in this class,
\[
O_A\!\left(k^2\log k\,(\log\log k)^2\right)
\tag{19}
\]
average degree suffices for sufficiently large \(k\); increasing the constant covers the remaining values.

This improves the cubic-with-logarithms conclusion in the supplied attempt.

### 6.3 A stronger necessary profile for a counterexample family

Suppose \(D\to\infty\) along a sequence of graphs satisfying
\[
h_4(G)=D^{o(1)}.
\]
Theorem 1 implies
\[
R(G)\bigl(8+\log_2R(G)\bigr)^2
 \ge \frac{D}{2^{20}h_4(G)^2}.
\tag{20}
\]
If \(R(G)\ge D\), there is nothing further to show. Otherwise, replacing \(\log R(G)\) by \(\log D\) in (20) gives
\[
R(G)\ge D^{1-o(1)}.
\]
Since \(R(G)\le2s(G)\) and
\[
s(G)\le1+\lfloor\log_2\Delta\rfloor,
\]
such a sequence must satisfy
\[
\boxed{
s(G)\ge D^{1-o(1)},\qquad
\log\Delta\ge D^{1-o(1)},\qquad
|V(G)|\ge 2^{D^{1-o(1)}}.
}
\tag{21}
\]

Thus a diagonal family defeating every power-law lower bound must have nearly \(D\) occupied dyadic degree scales, in this asymptotic sense—not merely one exceptionally large maximum degree.

---

## 7. The unresolved gap

The argument still depends on \(R(G)\), which is not bounded by a function small enough in \(D\) for arbitrary graphs. When the number of relevant degree scales is comparable to or larger than \(D\), the estimate need not give any growing lower bound.

The precise missing step is an order-independent way to combine contributions from arbitrarily many degree scales without losing essentially their number during extraction. The finite-field construction handles an extracted, degree-controlled graph efficiently, but it does not supply that combination.

Accordingly:

- no unrestricted polynomial \(p(k)\) is proved;
- no counterexample to its existence is constructed;
- the quoted unrestricted \(k^{Ck^2}\) threshold is not improved by these arguments.

I have not independently checked whether these formulations already occur in the literature or whether later work resolves the original problem. The claims proved here are the self-contained partial results above.