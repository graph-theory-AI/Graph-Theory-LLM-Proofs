```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a uniform lower bound, including 500 ≤ r_{K_3}^{(3)}(K_3) ≤ 680, and prove the conjectured lower bound whenever an R_q(t)-critical core has independence number at most two.",
  "would_publish": false,
  "caveats": "The full conjecture remains unresolved; no exhaustive search was run, and novelty of these partial bounds has not been checked."
}
```

# 1. Statement and results obtained

All graphs below are finite and simple. Write
\[
L_q(t)=r_{K_3}^{(q)}(K_t),\qquad R=R_q(t),
\]
where \(G\longrightarrow_q K_t\) means that every \(q\)-coloring of \(E(G)\) contains a monochromatic \(K_t\). Let \(T(G)\) and \(m(G)\) denote the numbers of triangles and edges.

The conjecture is
\[
L_q(t)=\binom R3.
\tag{1}
\]
The upper bound follows from \(K_R\longrightarrow_q K_t\). The cases \(q=1\) and \(t=2\) are immediate, so the substantive discussion concerns \(q\ge2\), \(t\ge3\).

Put
\[
d=q(t-2),\qquad
S(r)=\sum_{i=1}^{r-1}i^2
=\frac{r(r-1)(2r-1)}6.
\]

I prove the following uniform bound:
\[
\boxed{\quad
L_q(t)\ge
\left\lceil\frac{dS(R)}{2d+3}\right\rceil .
\quad}
\tag{2}
\]
In particular,
\[
L_q(t)\ge
\frac{d(2R-1)}{(2d+3)(R-2)}\binom R3
\ge
\frac{2d}{2d+3}\binom R3.
\tag{3}
\]

A small but useful strengthening is
\[
\boxed{\quad
L_q(t)\ge
\min\left\{
\binom R3,\;
\left\lceil\frac{d\bigl(S(R)+2\bigr)}{2d+3}\right\rceil
\right\}.
\quad}
\tag{4}
\]

For the first genuinely multicolor case, this gives
\[
\boxed{500\le L_3(3)\le680.}
\tag{5}
\]

There is also a structural exclusion:

> **Independence-number exclusion.** If \(G\longrightarrow_q K_t\) contains an \(R\)-chromatic subgraph \(H\) with \(\alpha(H)\le2\), then
> \[
> T(G)\ge\binom R3.
> \]
> Consequently, every \(R\)-critical core of a counterexample must have independence number at least three.

The principal new ingredient relative to the supplied attempt is the chromatic inequality
\[
m(G)+2T(G)\ge S(\chi(G)).
\tag{6}
\]
Its proof is elementary. The structural refinement uses the classical Gallai decomposition theorem for critical graphs and Brooks’ theorem, in the precise forms stated below.

I do not claim that these bounds improve the best bounds in the literature; I have not independently checked that question.

# 2. The elementary Ramsey reductions

I reprove the two reductions from edge-minimality that I use.

## Lemma 2.1: local triangle multiplicity

If \(G\) is edge-minimal subject to \(G\longrightarrow_q K_t\), then every edge belongs to at least \(d=q(t-2)\) triangles. Consequently,
\[
d\,m(G)\le3T(G).
\tag{7}
\]

**Proof.** Fix an edge \(xy\). There is a \(q\)-coloring of \(G-xy\) with no monochromatic \(K_t\).

For each color \(c\), giving \(xy\) color \(c\) must create a monochromatic \(K_t\) containing \(xy\). Thus there is a set \(A_c\) of \(t-2\) common neighbors of \(x,y\) such that all edges of this \(K_t\), other than \(xy\), have color \(c\).

The sets \(A_c\) are pairwise disjoint: a vertex belonging to both \(A_c\) and \(A_{c'}\) would make its edge to \(x\) have two different colors. Hence \(xy\) has at least \(q(t-2)\) common neighbors. Summing over edges proves (7). ∎

## Lemma 2.2: chromatic obstruction

If \(G\longrightarrow_q K_t\), then
\[
\chi(G)\ge R_q(t).
\tag{8}
\]

**Proof.** Otherwise, properly color \(V(G)\) with \(R-1\) labels. Fix a \(q\)-coloring of \(K_{R-1}\) with no monochromatic \(K_t\), and give an edge of \(G\) the color of the pair of its endpoint labels.

Every clique in \(G\) has distinct labels. A monochromatic \(K_t\) would therefore project to one in the coloring of \(K_{R-1}\), a contradiction. ∎

# 3. A chromatic inequality involving edges and triangles

Define
\[
F(G)=m(G)+2T(G).
\]

## Theorem 3.1
Every graph of chromatic number \(r\) satisfies
\[
F(G)\ge S(r)=\frac{r(r-1)(2r-1)}6.
\tag{9}
\]

Equality holds for complete graphs; it also holds for \(C_5\).

### Proof

We first use the elementary independence bound
\[
\alpha(H)\ge \frac{|V(H)|^2}{|V(H)|+2m(H)}.
\tag{10}
\]
For completeness, a uniformly random vertex ordering gives an independent set consisting of the vertices preceding all their neighbors. Its expected size is
\[
\sum_{v\in V(H)}\frac1{d_H(v)+1}
\ge \frac{|V(H)|^2}{|V(H)|+2m(H)}.
\]

Now induct on \(r\). The result is immediate for \(r=1\). Because \(F\) is monotone under taking subgraphs, we may replace \(G\) by a vertex-critical induced subgraph of chromatic number \(r\). Thus
\[
\delta(G)\ge r-1.
\]

Let \(I\) be a maximum independent set, of size \(a=\alpha(G)\). For \(v\in V(G)\), let \(\tau(v)\) be the number of triangles containing \(v\). Applying (10) to \(G[N(v)]\), whose independence number is at most \(a\), gives
\[
d(v)+2\tau(v)\ge \frac{d(v)^2}{a}.
\tag{11}
\]

Since \(I\) is independent, each edge or triangle meeting \(I\) meets it in exactly one vertex. Therefore
\[
\begin{aligned}
F(G)-F(G-I)
&=\sum_{v\in I}\bigl(d(v)+2\tau(v)\bigr)\\
&\ge \frac1a\sum_{v\in I}d(v)^2\\
&\ge (r-1)^2.
\end{aligned}
\tag{12}
\]

Also \(\chi(G-I)=r-1\): it is at least \(r-1\) because \(I\) can receive one new color, and at most \(r-1\) by vertex-criticality. Induction now yields
\[
F(G)\ge S(r-1)+(r-1)^2=S(r).
\]
∎

## Deduction of the uniform bound

Let \(G\longrightarrow_q K_t\), and pass to an edge-minimal Ramsey subgraph \(G_0\). By Lemmas 2.1–2.2 and Theorem 3.1,
\[
S(R)\le m(G_0)+2T(G_0)
\le \left(\frac3d+2\right)T(G_0).
\]
Since \(T(G_0)\le T(G)\), this proves (2).

Unlike the incidence bound \(T(G)\ge d\binom R2/3\), this retains a positive fraction approaching one as \(d\) grows, independently of the size of \(R\).

# 4. Graphs of independence number at most two

Here I use the following classical form of Gallai’s decomposition theorem:

> If a \(k\)-critical graph has at most \(2k-2\) vertices, its complement is disconnected.

The statement also applies to vertex-critical graphs. Indeed, a vertex-critical graph has an edge-critical spanning subgraph of the same chromatic number; disconnectedness of the complement of that spanning subgraph implies disconnectedness of the original complement.

## Theorem 4.1
If \(\chi(H)=r\ge4\) and \(\alpha(H)\le2\), then
\[
T(H)\ge\binom r3.
\tag{13}
\]

### Proof

Replace \(H\) by an induced vertex-critical subgraph of chromatic number \(r\). Decompose it according to the connected components of its complement:
\[
H=H_1\vee\cdots\vee H_s.
\]
Here \(\vee\) denotes the join. Each \(H_i\) is vertex-critical, and its complement is connected. Write
\[
r_i=\chi(H_i),\qquad n_i=|V(H_i)|,\qquad m_i=m(H_i).
\]
Then \(\sum_i r_i=r\).

### Step 1: the possible factor orders

Gallai’s theorem gives
\[
n_i\ge2r_i-1.
\tag{14}
\]
On the other hand, deleting any vertex of \(H_i\) leaves an \((r_i-1)\)-colorable graph. All its color classes have size at most two, so
\[
n_i-1\le2(r_i-1).
\tag{15}
\]
Consequently,
\[
n_i=2r_i-1.
\tag{16}
\]

A factor with \(r_i=1\) is \(K_1\). There is no factor with \(r_i=2\), since the only vertex-critical 2-chromatic graph is \(K_2\), whose complement is disconnected. A factor with \(r_i=3\) is \(C_5\).

### Step 2: factors of chromatic number at least four

If \(J\) has \(n\) vertices and \(\alpha(J)\le2\), then its complement is triangle-free. Counting mixed triples gives
\[
T(J)
=
\binom n3-\frac12\sum_{v\in V(J)}
d_J(v)\bigl(n-1-d_J(v)\bigr).
\]
Using \(x(n-1-x)\le(n-1)^2/4\),
\[
T(J)\ge \frac{n(n-1)(n-5)}{24}.
\tag{17}
\]

For a factor with \(r_i=k\ge4\), substitute \(n_i=2k-1\):
\[
T(H_i)\ge
\frac{(2k-1)(k-1)(k-3)}6.
\tag{18}
\]
For \(k=4\), the right side is \(7/2\), so integrality gives \(T(H_i)\ge4=\binom43\). For \(k\ge5\), its difference from \(\binom k3\) is
\[
\frac{(k-1)(k^2-5k+3)}6\ge0.
\]
Thus every factor except \(C_5\) satisfies
\[
T(H_i)\ge\binom{r_i}3.
\tag{19}
\]
A \(C_5\) factor falls short by exactly one triangle.

### Step 3: joins compensate for the \(C_5\) deficit

For every factor,
\[
n_i\ge r_i,\qquad m_i\ge\binom{r_i}2.
\]
For a \(C_5\) factor specifically,
\[
n_i=5,\qquad r_i=3,\qquad
m_i=\binom32+2.
\]

The triangle count in a join is
\[
T(H)=
\sum_i T(H_i)
+\sum_{i\ne j}m_i n_j
+\sum_{i<j<k}n_i n_j n_k.
\tag{20}
\]
Replacing \(n_i,m_i,T(H_i)\) by the complete-graph baselines gives \(\binom r3\), except for a deficit of one for each \(C_5\) factor.

Let \(h\) be the number of \(C_5\) factors. The two excess edges in each such factor contribute at least
\[
2\sum_{j\ne i}r_j=2(r-3)
\]
additional cross-part triangles. Hence
\[
T(H)\ge\binom r3-h+2h(r-3)\ge\binom r3,
\]
because \(r\ge4\). ∎

It follows immediately that a counterexample to (1) cannot have an \(R\)-critical core of independence number at most two.

# 5. A strictness refinement of the chromatic inequality

The preceding structural result can be combined with a small stability statement for Theorem 3.1.

## Lemma 5.1
Let \(H\) be vertex-critical, with
\[
\chi(H)=r\ge4,\qquad \alpha(H)\ge3.
\]
Then
\[
F(H)\ge S(r)+2.
\tag{21}
\]

### Proof

Suppose instead that
\[
F(H)\le S(r)+1.
\tag{22}
\]
Put \(k=r-1\) and \(a=\alpha(H)\). For every maximum independent set \(I\), the proof of Theorem 3.1 gives
\[
F(H)-F(H-I)\le k^2+1.
\tag{23}
\]

Since all degrees are at least \(k\), the left side is at least \(ak\). Thus \(a\le k\).

If some \(v\in I\) had degree at least \(k+1\), then (11) would give
\[
F(H)-F(H-I)
\ge k^2+\frac{2k+1}{a}
>k^2+2,
\]
contradicting (23). Therefore every vertex belonging to a maximum independent set has degree exactly \(k\).

Write
\[
k=a\ell+s,\qquad 0\le s<a.
\]
By Turán’s theorem applied to the complement, a graph on \(k\) vertices with independence number at most \(a\) has at least
\[
b=a\binom{\ell}{2}+s\ell
\tag{24}
\]
edges. Consequently, for a maximum independent set \(I\),
\[
F(H)-F(H-I)
\ge a(k+2b)
=k^2+s(a-s).
\tag{25}
\]

Since \(a\ge3\), a nonzero remainder \(s\) would give
\[
s(a-s)\ge a-1\ge2,
\]
again contradicting (23). Hence \(a\mid k\).

Now (23) and parity force equality in (24) for every neighborhood of a vertex in \(I\): otherwise the left side of (23) increases by at least two. The equality case of Turán’s theorem therefore says that, for every vertex belonging to a maximum independent set, its neighborhood is a disjoint union of \(a\) cliques, each of order \(k/a\).

Let \(D\) be the set of vertices belonging to some maximum independent set. If \(v\in D\), every neighbor \(u\) of \(v\) belongs to an independent set of size \(a\) inside \(N(v)\): select \(u\) and one vertex from each of the other neighborhood cliques. Thus \(N(v)\subseteq D\).

Therefore \(D\) is nonempty and closed under taking neighbors. A vertex-critical graph is connected, so \(D=V(H)\). It follows that \(H\) is \(k\)-regular and has chromatic number \(k+1\).

Brooks’ theorem now forces \(H=K_{k+1}\), since \(k\ge3\). This contradicts \(\alpha(H)\ge3\). ∎

## Deduction of the strengthened Ramsey bound

Let \(C=\binom R3\), and suppose that a Ramsey graph \(G\) has \(T(G)<C\). Choose an edge-minimal Ramsey subgraph \(G_0\), and an \(R\)-critical subgraph \(H\subseteq G_0\).

Theorem 4.1 implies \(\alpha(H)\ge3\). Since \(R\ge6\), Lemma 5.1 applies and gives
\[
S(R)+2\le F(H)\le F(G_0)
\le\left(2+\frac3d\right)T(G_0).
\]
Thus either \(T(G)\ge C\), or
\[
T(G)\ge
\left\lceil\frac{d\bigl(S(R)+2\bigr)}{2d+3}\right\rceil.
\]
This proves (4).

# 6. The three-color triangle case

Here \(R_3(3)=17\), \(d=3\), and
\[
S(17)=\frac{17\cdot16\cdot33}{6}=1496.
\]
Therefore (4) gives
\[
L_3(3)\ge
\min\left\{680,\left\lceil\frac{3(1496+2)}9\right\rceil\right\}
=500.
\]

The Ramsey value \(R_3(3)=17\) can be verified explicitly as follows.

* For the upper bound, in a coloring of \(K_{17}\), some vertex has six neighbors joined to it in one color. An edge of that color among those neighbors gives a monochromatic triangle; otherwise the \(K_6\) on those neighbors uses only the other two colors and contains a monochromatic triangle.
* For the lower bound, use vertices \(0,\ldots,15\), viewed as four-bit vectors, and partition the nonzero vectors into
  \[
  A=\{1,8,10,12,15\},\quad
  B=\{2,3,7,11,13\},\quad
  C=\{4,5,6,9,14\}.
  \]
  Color \(xy\) according to the part containing \(x\mathbin{\mathrm{xor}}y\). Each displayed part is sum-free under XOR, as is checked directly. A monochromatic triangle would give distinct \(a,b,a\mathbin{\mathrm{xor}}b\) in one part, which is impossible.

Thus the numerical conclusion (5) uses no unexecuted search.

## A smaller critical-core range

Suppose a counterexample in this case has at most \(679\) triangles. Its edge-minimal Ramsey subgraph \(G_0\) satisfies
\[
m(G_0)\le679.
\]
Let \(H\subseteq G_0\) be 17-critical. Since \(\delta(H)\ge16\),
\[
|V(H)|\le
\left\lfloor\frac{2\cdot679}{16}\right\rfloor=84.
\tag{26}
\]

Moreover, \(\alpha(H)\ge3\) by Theorem 4.1. This excludes orders at most \(19\). Indeed, Gallai decomposition shows that a 17-critical graph on at most \(19\) vertices is either \(K_{17}\), or
\[
K_{14}\vee C_5.
\]
To see this, decompose maximally into complement-connected critical factors. Each nontrivial factor of chromatic number \(k\) has \(k\ge3\) and order at least \(2k-1\), so contributes at least \(k-1\ge2\) to the excess \(|V(H)|-\chi(H)\). With total excess at most two, the only possible nontrivial factor is \(C_5\). Both resulting graphs have independence number at most two.

Hence every counterexample must contain a critical core satisfying
\[
\boxed{
20\le |V(H)|\le84,\qquad
\chi(H)=17,\qquad
\alpha(H)\ge3.
}
\tag{27}
\]

# 7. What remains unresolved

These arguments do not exclude the cores in (27), nor do they produce a three-color Ramsey graph with fewer than \(680\) triangles. In particular, the interval
\[
500\le L_3(3)\le680
\]
remains open in this writeup.

The quoted absolute-\(K\) coloring theorem from the source already gives equality when \(q(t-2)\ge K\). The estimates here do not replace that theorem or settle all of the remaining parameters. Their contribution is an elementary, substantially stronger uniform counting bound than the direct edge–triangle incidence estimate, together with an exact exclusion of low-independence critical cores.

No exhaustive enumeration or SAT computation was performed.