```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I construct properly coloured regular graphs with arbitrarily large degree/log n and strong vanishing-profile robustness, but no colour-separated connected spanning pair.",
  "would_publish": false,
  "caveats": "The source's quantitative definition of robust sublinear expander is not supplied or verified; constant-fraction cut resilience instead gives an affirmative theorem."
}
```

## 1. Scope of the result

The quantitative meaning of **robust sublinear expander** is decisive here. I do not claim to have resolved the source question without verifying that definition.

There is, however, a substantially stronger obstruction than the one-colour cut in the previous attempt:

> Even properly coloured regular graphs with a fixed positive vertex-expansion constant, robust against deleting \(\Omega(\log n)|X|\) edges around every set \(X\), can have arbitrarily large average-degree-to-\(\log n\) ratio and still admit no two colour-disjoint spanning connected subgraphs.

Moreover, these examples satisfy every fixed, sufficiently small, **vanishing scale-dependent resilience profile**, as made precise below. The obstruction is a rank bottleneck, not a cut crossed by only one colour.

I also independently verify the previous attempt’s affirmative activation lemma. Thus the results distinguish two quantitatively different interpretations of robustness.

All logarithms below are natural unless a base is indicated.

---

## 2. A precise counterexample theorem

Let
\[
\rho:(0,\infty)\longrightarrow (0,1/10]
\]
be nonincreasing, with \(\rho(t)\to0\) as \(t\to\infty\).

Consider the following explicit robustness condition on a \(d\)-regular graph:
\[
\begin{split}
&\text{for every }X\subseteq V(G),\quad 1\le |X|\le 2|V(G)|/3,\\
&\text{and every }F\subseteq E(G)\text{ with }
 |F|\le d\,\rho(|X|/d)|X|,\\
&\hspace{35mm}|N_{G-F}(X)|\ge \rho(|X|/d)|X|.
\end{split}
\tag{\(\mathrm R_\rho\)}
\]
Here \(N\) denotes the external neighbourhood.

### Theorem 1
For every such fixed function \(\rho\) and every constant \(C>0\), there are arbitrarily large \(n\) and properly edge-coloured, simple, \(d\)-regular \(n\)-vertex graphs \(G\) such that:

1. \(d\ge C\log n\);
2. \(G\) satisfies \((\mathrm R_\rho)\);
3. under the same permitted deletions, the stronger bound
   \[
   |N_{G-F}(X)|\ge |X|/100
   \tag{1}
   \]
   holds;
4. \(G\) has no two colour-disjoint spanning connected subgraphs.

Importantly, \(\rho\) is fixed before \(C\) is chosen. For example, one may use the single profile
\[
\rho(t)=\frac{1}{100(1+\log(1+t))^2}
\]
for all \(C\).

### 2.1. Two sets of binary generators

Choose an integer
\[
K\ge \max\{32,\lceil 2C\log 2\rceil\}.
\]
For a sufficiently large integer \(r\), put
\[
a=Kr,\qquad b=2r-1.
\]

We need sets of distinct nonzero vectors
\[
A,B\subseteq \mathbb F_2^r,\qquad |A|=a,\quad |B|=b,
\]
with the following properties. For every nonzero \(u\in\mathbb F_2^r\),
\[
\bigl|\{x\in A:u\cdot x=1\}\bigr|\ge a/4,
\tag{2}
\]
and
\[
\bigl|\{y\in B:u\cdot y=1\}\bigr|\ge b/16.
\tag{3}
\]

Here is a self-contained existence argument.

Sample each list independently and uniformly from \(\mathbb F_2^r\), initially allowing repetitions. For fixed nonzero \(u\), the number of sampled vectors having dot product \(1\) with \(u\) is binomial with parameter \(1/2\).

For the list of length \(a\), a Chernoff bound gives
\[
\Pr\bigl(\operatorname{Bin}(a,1/2)\le a/4\bigr)
 \le e^{-a/16}.
\]
The union bound over nonzero \(u\) is therefore at most
\[
2^r e^{-a/16}
=\exp\bigl((\log 2-K/16)r\bigr)=o(1).
\]

For the list of length \(b\), the binary entropy bound gives
\[
\Pr\bigl(\operatorname{Bin}(b,1/2)\le b/16\bigr)
 \le 2^{-b(1-H_2(1/16))}.
\]
Since
\[
H_2(1/16)
=\frac14+\frac{15}{16}\log_2(16/15)
<\frac38,
\]
the union bound is at most
\[
2^{r-5b/8}=2^{-r/4+5/8}=o(1).
\]

The probability that either list contains zero or a repeated vector is at most
\[
\frac{a(a+1)+b(b+1)}{2^{r+1}}=o(1).
\]
Consequently, \(A\) and \(B\) satisfying (2)–(3) exist for every sufficiently large \(r\).

A fully specified deterministic choice is to take the lexicographically first sets satisfying (2)–(3). No computational check is being asserted.

### 2.2. The graph and its colouring

Let
\[
V(G)=\mathbb F_2^r\times\mathbb F_2^r.
\]
Use the Cayley generating set
\[
\{(x,0):x\in A\}\ \cup\ \{(0,y):y\in B\}.
\]
Colour each edge by its generating vector.

Every generator is a nonzero involution, so each colour class is a perfect matching. Distinct generators give distinct edges incident with each vertex. Thus the graph is simple, the colouring is proper, and
\[
n=2^{2r},\qquad d=a+b=(K+2)r-1.
\]
In particular,
\[
d\ge Kr\ge 2Cr\log 2=C\log n.
\]

### 2.3. Why the desired decomposition is impossible

Let \(H\) be any spanning connected subgraph of \(G\). Let \(B_H\subseteq B\) be the set of second-coordinate colours used by \(H\).

Project paths in \(H\) onto the second coordinate. Every projected displacement lies in the linear span of \(B_H\). Because \(H\) spans and is connected, all second-coordinate displacements must be possible. Hence
\[
\operatorname{span}(B_H)=\mathbb F_2^r,
\qquad\text{so}\qquad |B_H|\ge r.
\]

Two colour-disjoint spanning connected subgraphs would therefore require two disjoint subsets of \(B\), each of size at least \(r\). This is impossible because
\[
|B|=2r-1.
\]

This argument rules out even a pair of colour-disjoint spanning connected subgraphs that do not exhaust \(E(G)\), and therefore rules out the requested decomposition.

### 2.4. Expansion estimates

Write
\[
H_A=\operatorname{Cay}(\mathbb F_2^r,A),\qquad
H_B=\operatorname{Cay}(\mathbb F_2^r,B).
\]

For a binary Cayley graph with generator set \(D\), its Laplacian eigenvalue at the character indexed by \(u\) is
\[
2\bigl|\{z\in D:u\cdot z=1\}\bigr|.
\]
Thus (2)–(3) give
\[
\lambda_2(L_{H_A})\ge a/2,\qquad
\lambda_2(L_{H_B})\ge b/8.
\tag{4}
\]

We use two consequences.

#### Small sets: large unweighted edge boundary

Suppose \(X\subseteq V(G)\) has size \(s\le 2^{r-1}\). For each second coordinate \(y\), let
\[
X_y=\{x:(x,y)\in X\}.
\]
Then \(|X_y|\le 2^{r-1}\).

For a graph on \(N\) vertices with Laplacian gap \(\lambda\),
\[
e(S,V\setminus S)\ge \lambda |S|(1-|S|/N).
\tag{5}
\]
Applying this in each \(H_A\)-fibre and summing gives
\[
e_G(X,V(G)\setminus X)
\ge \frac a4\sum_y|X_y|
=\frac a4s
\ge \frac d5s,
\tag{6}
\]
where the last inequality follows from \(a\ge4b\).

#### All sets: a weighted expansion bound independent of \(K\)

Give each \(A\)-edge weight \(1/a\), and each \(B\)-edge weight \(1/b\). Every vertex now has weighted degree \(2\).

The weighted Laplacian is
\[
L_w=\frac1a L_{H_A}\otimes I
       +I\otimes\frac1b L_{H_B}.
\]
By (4),
\[
\lambda_2(L_w)\ge \min\{1/2,1/8\}=1/8.
\]
Therefore, whenever \(s=|X|\le2n/3\),
\[
w\bigl(\delta_G(X)\bigr)
\ge \frac18s(1-s/n)
\ge s/24.
\tag{7}
\]

### 2.5. Verification of every robustness case

Take \(r\) sufficiently large that, in addition to the generator-set requirements,
\[
\rho(2^{r-1}/d)\le \frac{1}{48(K+2)}.
\tag{8}
\]
This is possible because \(2^{r-1}/d\to\infty\).

Fix \(X\) with \(1\le s=|X|\le2n/3\), and suppose
\[
|F|\le d\rho(s/d)s.
\]

**Case 1: \(s\le2^{r-1}\).**

By (6) and \(\rho\le1/10\),
\[
e_{G-F}(X,V(G)\setminus X)
\ge \frac d5s-\frac d{10}s
=\frac d{10}s.
\]
Every external neighbour is incident with at most \(d\) of these edges, so
\[
|N_{G-F}(X)|\ge s/10.
\]
This is at least both \(\rho(s/d)s\) and \(s/100\).

**Case 2: \(s>2^{r-1}\).**

By monotonicity and (8),
\[
\rho(s/d)\le\frac1{48(K+2)}.
\]
Since \(a\ge b\), every edge has weight at most \(1/b\). Also \(d/b\le K+2\). Hence
\[
w(F\cap\delta_G(X))
\le \frac{|F|}{b}
\le \frac db\,\rho(s/d)s
\le s/48.
\]
Together with (7), this yields
\[
w\bigl(\delta_{G-F}(X)\bigr)\ge s/48.
\]
An external vertex is incident with total edge weight at most \(2\). Consequently,
\[
|N_{G-F}(X)|\ge s/96.
\]
Since \(K\ge32\),
\[
\rho(s/d)\le\frac1{48(K+2)}<\frac1{100}<\frac1{96}.
\]
Thus both required neighbourhood bounds hold in this case too.

This proves Theorem 1. \(\square\)

---

## 3. Additional strength of these counterexamples

The construction has two useful features that distinguish it from a graph with a one-colour bottleneck.

### 3.1. Uniform robustness against \(\Omega(\log n)|X|\) edge deletions

The weighted argument immediately gives, for every \(1\le|X|\le2n/3\),
\[
|F|\le \frac b{48}|X|
\quad\Longrightarrow\quad
|N_{G-F}(X)|\ge |X|/96.
\tag{9}
\]
Here
\[
b=2r-1=\log_2 n-1.
\]

In particular, let \(\omega(n)\to\infty\) be any fixed function. For each fixed \(C\), sufficiently large members of the construction satisfy
\[
|F|\le \frac d{\omega(n)}|X|
\quad\Longrightarrow\quad
|N_{G-F}(X)|\ge |X|/100.
\tag{10}
\]
Indeed, \(d/b\le K+2\), so eventually \(d/\omega(n)\le b/48\).

Thus uniform resilience of order \(d/(\log n)^\alpha\), for any fixed \(\alpha>0\), does not suffice—even with a fixed linear vertex-expansion conclusion.

### 3.2. Every cut uses \(\Omega(\log n)\) colours

For \(|X|\le n/2\), the weighted spectral estimate improves to
\[
w(\delta_G(X))\ge |X|/16.
\]
Since every edge has weight at most \(1/b\),
\[
e_G(X,V(G)\setminus X)\ge \frac b{16}|X|.
\]
Properness implies that a single colour contributes at most \(|X|\) crossing edges. Therefore every nontrivial cut is crossed by at least
\[
b/16=\frac{\log_2 n-1}{16}
\tag{11}
\]
colours.

The obstruction is therefore genuinely global: the \(2r-1\) second-coordinate generators cannot supply two spanning sets of an \(r\)-dimensional quotient.

---

## 4. The affirmative cut-resilience theorem is valid

For completeness, here is an independent verification of the activation lemma in the previous attempt.

For any edge-coloured graph, let
\[
\kappa_{\mathrm{col}}(G)
=\min_{\varnothing\ne X\subsetneq V(G)}
 \bigl|\{\text{colours on }\delta_G(X)\}\bigr|.
\]

### Theorem 2
Suppose an \(n\)-vertex edge-coloured graph has
\[
\kappa_{\mathrm{col}}(G)\ge k.
\]
Retain each colour independently with probability \(p\), retaining all its edges. Then
\[
\Pr(G_p\text{ is disconnected})
\le (n-1)(1-p)^{k/2}.
\tag{12}
\]
Consequently, the desired colour-separated decomposition exists if
\[
k>2\log_2(2(n-1)).
\tag{13}
\]

Properness is not needed for this theorem.

### Proof

Give every colour an independent exponential activation time of rate \(1\). Let \(c(t)\) be the number of components formed by the activated colours.

Consider a state with \(c\ge2\) components. Every colour crossing the cut of a current component is inactive. Thus each component is incident with at least \(k\) inactive crossing colours.

For an inactive colour \(\gamma\), let \(a_\gamma\) be the number of current components incident with an edge of that colour joining different components. If \(\gamma\) activates, the decrease in the component count is at least \(a_\gamma/2\): every nontrivial component in the auxiliary graph on current components has at least two vertices.

Counting component–colour incidences gives
\[
\sum_\gamma a_\gamma\ge kc.
\]
As each inactive colour activates at rate \(1\), the conditional drift of \(c(t)-1\) is at most
\[
-\frac12\sum_\gamma a_\gamma
\le-\frac k2c
\le-\frac k2(c-1).
\]
The same drift inequality holds when \(c=1\). Taking expectations and solving the differential inequality,
\[
\mathbb E[c(t)-1]\le(n-1)e^{-kt/2}.
\]
At time \(t=-\log(1-p)\), the activated colours are independent with retention probability \(p\). Markov’s inequality proves (12).

For a uniformly random red/blue partition of the colours, both marginal subgraphs have \(p=1/2\). They need not be independent: a union bound suffices to give
\[
\Pr(G_{\rm red}\text{ or }G_{\rm blue}\text{ disconnected})
\le2(n-1)2^{-k/2}.
\]
This is less than \(1\) under (13). \(\square\)

### Consequence for constant-fraction resilience

Suppose \(G\) is properly coloured, has average degree \(d\), and there is a fixed \(\eta>0\) such that for every \(0<|X|\le n/2\), deleting at most
\[
\eta d|X|
\]
edges cannot eliminate all edges between \(X\) and its complement.

If that cut uses \(q\) colours, properness gives
\[
e_G(X,V(G)\setminus X)\le q|X|.
\]
Thus \(q\le\eta d\) would make the entire cut deletable, a contradiction. Hence
\[
\kappa_{\mathrm{col}}(G)>\eta d.
\]
Theorem 2 proves the desired conclusion for \(d\ge C_\eta\log n\); for example,
\[
C_\eta=\frac4{\eta\log2}
\]
suffices for every \(n\ge2\). The one-vertex case is trivial.

So the previous attempt’s positive mathematical core is sound.

---

## 5. What remains unresolved about Question 10.2

The two proved results lead to opposite answers under different quantitative hypotheses:

- **Fixed vanishing resilience profile:** If the intended definition is \((\mathrm R_\rho)\), or a weaker condition covered by Theorem 1, then the proposed universal \(C\) does **not** exist. The same fixed profile works throughout the counterexample family.
- **Uniform \(o(d)\)-per-vertex edge-deletion resilience:** Even a fixed linear vertex-expansion conclusion does not suffice, by (10).
- **Constant-fraction cut resilience:** If the definition guarantees resilience against \(\eta d|X|\) edge deletions at every scale for a fixed \(\eta>0\), the answer is **yes**, by Theorem 2.

There is no contradiction between the construction and the last item. In the constructed graph, the set
\[
X=\mathbb F_2^r\times\{0\}
\]
has exactly \(b|X|\) boundary edges, whereas \(d/b\) can be made arbitrarily large by increasing \(K\). It therefore fails constant-fraction edge resilience once \(K\) is sufficiently large relative to \(1/\eta\).

The remaining source-specific task is to check the exact robustness parameters, and any additional hypotheses, used in Question 10.2. I have not verified those from the supplied excerpt, so neither quantitative theorem is being presented as an unconditional resolution of the catalogued question.