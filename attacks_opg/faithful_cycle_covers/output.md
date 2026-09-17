```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a bounded-weight reduction for counterexamples and an explicit graph-size-dependent additive buffer that makes every admissible weighting faithfully coverable.",
  "would_publish": false,
  "caveats": "The conjecture remains unresolved; novelty is not claimed, and the optional linear buffer bound uses the interval theorem exactly as quoted in the question."
}
```

## 1. Partial results

I work with finite undirected graphs. The proofs allow parallel edges if two parallel edges are regarded as a cycle. Loops, if allowed, can be covered separately.

An admissible weighting assigns weight zero to every bridge, so bridges may be deleted. Thus the substantive statements below concern a bridgeless graph \(G\), with \(m=|E(G)|\ge 1\). Write \(\mathbf 1\) for the all-one edge vector.

I establish the following.

**Theorem A — bounded-weight counterexamples.**  
If \(G\) admits an even admissible weighting having no faithful cover, then it admits such a weighting \(h\) satisfying
\[
0\le h(e)\le 2m-2\qquad(e\in E(G)).
\]

**Theorem B — an explicit additive buffer.**  
Put
\[
R=2^{\lceil\log_2(m+1)\rceil},\qquad
B=m\left\lfloor\frac{m-1}{2}\right\rfloor,\qquad
T=RB.
\]
For every admissible integer weighting \(p\), not necessarily coordinatewise even,
\[
(G,p+T\mathbf 1)
\]
has a faithful cover. In particular,
\[
T\le m^2(m-1).
\]

Theorem B does not use the numerical interval theorem quoted in the question. Using that theorem **as stated**, the buffer improves to
\[
T_{\mathrm{lin}}
 =32\left\lfloor\frac{m-1}{4}\right\rfloor+84
 \le 8m+76.
\]
The derivation appears in Section 5.

These results do not settle the conjecture: the buffer is generally positive, and Theorem A still includes the unresolved weighting \(p\equiv2\).

---

## 2. Rounding inside the cycle cone

For a cycle \(C\), let \(\chi_C\) denote its edge-incidence vector, and let
\[
\mathcal C(G)=
\left\{\sum_C\lambda_C\chi_C:\lambda_C\ge0\right\}.
\]

I use the cycle-cone characterization supplied in the question: nonnegativity and the cut inequalities characterize membership in \(\mathcal C(G)\).

### Rounding lemma

If \(q\in\mathcal C(G)\cap\mathbb Z^{E(G)}\), then
\[
q=\sum_{i=1}^{k} n_i\chi_{C_i}+r,
\]
where
\[
k\le m,\qquad n_i\in\mathbb Z_{\ge0},\qquad
r\in\mathcal C(G)\cap\mathbb Z^{E(G)},
\]
and
\[
0\le r(e)\le m-1.
\]
Moreover, if \(q(S)\) is even for every cut \(S\), the same holds for \(r\).

**Proof.** Conic Carathéodory, or elimination of linearly dependent used cycle vectors, gives
\[
q=\sum_{i=1}^{k}\alpha_i\chi_{C_i},
\qquad k\le m,\quad \alpha_i\ge0.
\]
Set \(n_i=\lfloor\alpha_i\rfloor\). Then
\[
r=\sum_{i=1}^{k}(\alpha_i-n_i)\chi_{C_i}
\]
is nonnegative and belongs to the cycle cone. It is integral because
\(r=q-\sum_i n_i\chi_{C_i}\), and
\[
r(e)<k\le m.
\]
Finally, every cycle meets every cut evenly, so subtracting integer multiples of cycle vectors preserves cut parity. \(\square\)

In particular, when \(q\) is admissible, the remainder \(r\) is also admissible.

### Proof of Theorem A

Let \(p\) be an even admissible weighting with no faithful cover. Since the cone inequalities are homogeneous, \(p/2\in\mathcal C(G)\). Choose
\[
\frac p2=\sum_{i=1}^{k}\alpha_i\chi_{C_i},\qquad k\le m.
\]
Define
\[
h=p-2\sum_{i=1}^{k}\lfloor\alpha_i\rfloor\chi_{C_i}
  =2\sum_{i=1}^{k}
       \bigl(\alpha_i-\lfloor\alpha_i\rfloor\bigr)\chi_{C_i}.
\]
Then \(h\) is integral, coordinatewise even, and lies in the cycle cone. Hence it is admissible. Also,
\[
0\le h(e)<2m,
\]
so its even coordinates satisfy \(h(e)\le2m-2\).

If \(h\) had a faithful cover, adding
\(2\lfloor\alpha_i\rfloor\) copies of each \(C_i\) would produce a faithful cover of \(p\), a contradiction. \(\square\)

---

## 3. Two elementary ingredients for the additive buffer

An **even edge set** is a subset of edges inducing even degree at every vertex. Every such set decomposes into edge-disjoint cycles.

### 3.1. A signed cycle identity for each series class

On a bridgeless graph, define
\[
e\sim f
\quad\Longleftrightarrow\quad
e=f\ \text{ or }\ \{e,f\}\text{ is an edge-cut}.
\]
This is an equivalence relation: transitivity follows from
\[
\delta(X)\mathbin{\triangle}\delta(Y)=\delta(X\mathbin{\triangle}Y).
\]
Call its equivalence classes **series classes**.

Every cycle contains either both edges of a two-edge cut or neither. Also, every admissible weighting is constant on a series class, since the inequalities for a cut \(\{e,f\}\) give
\[
p(e)\le p(f)\quad\text{and}\quad p(f)\le p(e).
\]

**Lemma 1.** For every series class \(A\), there are cycles \(C_A,C'_A\), possibly equal, whose edge intersection is exactly \(A\). Consequently, with
\[
D_A=C_A\mathbin{\triangle}C'_A,
\]
the set \(D_A\) is even and
\[
2\chi_A=\chi_{C_A}+\chi_{C'_A}-\chi_{D_A}. \tag{1}
\]

**Proof.** Fix \(e=uv\in A\). In \(G-e\), give capacity \(2\) to edges of \(A-\{e\}\), and capacity \(1\) to every other edge.

Every \(u\)-\(v\) cut has capacity at least \(2\). Indeed:

- capacity \(0\) would make \(e\) a bridge of \(G\);
- capacity \(1\) would mean that the cut consists of a single capacity-one edge \(f\), making \(\{e,f\}\) a cut of \(G\), contrary to \(f\notin A\).

The integral edge version of max-flow/min-cut therefore supplies two \(u\)-\(v\) paths \(P,Q\) sharing no edge outside \(A-\{e\}\).

For every \(f\in A-\{e\}\), the cut \(\{e,f\}\) shows that every \(u\)-\(v\) path in \(G-e\) must use \(f\). Thus
\[
E(P)\cap E(Q)=A-\{e\}.
\]
Take \(C_A=P+e\) and \(C'_A=Q+e\). Their intersection is \(A\), proving (1). \(\square\)

### 3.2. A uniform cycle cover containing a prescribed even edge set

**Lemma 2.** For the integer
\[
R=2^{\lceil\log_2(m+1)\rceil},
\]
and every even edge set \(D\), the vector
\[
R\mathbf1-\chi_D
\]
has a faithful cover.

**Proof.** Let \(k=\lceil\log_2(m+1)\rceil\), so \(R=2^k>m\).

Choose independently \(k\) uniformly random members
\(Z_1,\dots,Z_k\) of the binary cycle space. Because \(G\) is bridgeless, every edge belongs to a cycle. Consequently, for every edge \(e\), exactly half of the cycle-space members contain \(e\). Hence
\[
\Pr(e\notin Z_1\cup\cdots\cup Z_k)=2^{-k}.
\]
The union bound gives
\[
\Pr(Z_1\cup\cdots\cup Z_k\ne E(G))
   \le \frac mR<1.
\]
Fix a choice whose union is all of \(E(G)\).

For \(\varepsilon\in\mathbb F_2^k\), put
\[
Z(\varepsilon)=
\mathop{\triangle}_{i:\,\varepsilon_i=1} Z_i.
\]
Each edge belongs to exactly \(R/2\) of these \(R\) even edge sets.

Now consider the list of \(2R\) even edge sets
\[
Z(\varepsilon),\qquad Z(\varepsilon)\mathbin{\triangle}D
\qquad(\varepsilon\in\mathbb F_2^k).
\]
Every edge occurs exactly \(R\) times in this list. The second list contains \(D\), namely at \(\varepsilon=0\). Delete that occurrence of \(D\), and decompose all remaining even edge sets into cycles. The resulting list has incidence vector
\[
R\mathbf1-\chi_D.
\]
This includes \(D=\varnothing\), which gives a faithful cover of \(R\mathbf1\). \(\square\)

---

## 4. Proof of the additive-buffer theorem

Apply the rounding lemma to an admissible weighting \(p\):
\[
p=\sum_i n_i\chi_{C_i}+r,\qquad 0\le r(e)\le m-1.
\]
The vector \(r\) is admissible and is constant on each series class.

Let
\[
F=\{e:r(e)\text{ is odd}\}.
\]
Cut parity at singleton vertex cuts shows that \(F\) is an even edge set.

For a series class \(A\), define
\[
a_A=\left\lfloor\frac{r(e)}2\right\rfloor
\qquad(e\in A).
\]
Then
\[
r=\chi_F+2\sum_A a_A\chi_A,
\]
and, writing \(N=\sum_A a_A\),
\[
N\le
m\left\lfloor\frac{m-1}{2}\right\rfloor=B.
\]

Use the cycles and even edge sets supplied by Lemma 1. Identity (1) gives
\[
\begin{aligned}
p+RB\mathbf1
={}&\sum_i n_i\chi_{C_i}+\chi_F\\
&+\sum_A a_A
 \left[
   \chi_{C_A}+\chi_{C'_A}
   +(R\mathbf1-\chi_{D_A})
 \right]\\
&+(B-N)R\mathbf1. \tag{2}
\end{aligned}
\]

Every term on the right of (2) has a faithful cover:

- the first terms are integer multiples of cycles;
- \(F\) is an even edge set;
- Lemma 2 covers each \(R\mathbf1-\chi_{D_A}\);
- Lemma 2 with \(D=\varnothing\) covers \(R\mathbf1\).

All displayed coefficients are nonnegative integers. Concatenating these covers proves Theorem B.

Finally, \(R\le2m\), so
\[
T=Rm\left\lfloor\frac{m-1}{2}\right\rfloor
 \le m^2(m-1).
\]
Also, \(T\) is even. \(\square\)

### A graph-specific sharpening

Every occurrence of \(m\) in these bounds can be replaced by the number \(d\) of series classes.

Indeed, cycle vectors are constant on series classes, while (1) shows that each class indicator belongs to their real span. Thus the real span of cycle vectors has dimension exactly \(d\). Conic rounding therefore needs at most \(d\) cycles, and the probabilistic construction need only hit one representative from each series class.

The resulting bounds are
\[
h(e)\le2d-2
\]
and
\[
T=
2^{\lceil\log_2(d+1)\rceil}
d\left\lfloor\frac{d-1}{2}\right\rfloor
\le d^2(d-1).
\]

---

## 5. Linear refinement from the interval theorem quoted in the question

This section takes the numerical interval-cover theorem in the prompt **exactly as stated**. I have not independently checked its constants against the original publication; the preceding proofs do not depend on it.

Set
\[
k=\left\lfloor\frac{m-1}{4}\right\rfloor,
\qquad T_{\mathrm{lin}}=32k+84.
\]
Again write
\[
p=\sum_i n_i\chi_{C_i}+r,
\qquad 0\le r(e)\le m-1,
\]
with \(r\) admissible.

The constant weighting \(T_{\mathrm{lin}}\mathbf1\) is admissible: \(T_{\mathrm{lin}}\) is even, and every nonempty cut of a bridgeless graph has at least two edges. Therefore
\[
q=r+T_{\mathrm{lin}}\mathbf1
\]
is admissible.

Write \(m-1=4k+s\), where \(0\le s\le3\). For every edge,
\[
32k+83<q(e)
\le32k+84+(m-1)
=36k+84+s
\le36k+87<36k+88.
\]
The quoted interval theorem gives a faithful cover of \(q\). Adding the rounded integer copies of the \(C_i\) gives a faithful cover of
\[
p+T_{\mathrm{lin}}\mathbf1.
\]
Moreover,
\[
T_{\mathrm{lin}}\le8m+76.
\]

Thus the rounding argument amplifies the quoted near-uniform result into a uniform additive bound independent of the magnitude or disparity of the original weights.

---

## 6. Consequences and a finite verification procedure

### An explicit sufficient condition for an unshifted instance

Let \(T\) be the buffer from Theorem B, or the linear buffer when using the quoted interval theorem.

An even weighting \(p\) has a faithful cover whenever
\[
p(e)\ge T\qquad(e\in E)
\]
and
\[
p(S)-2p(e)\ge T(|S|-2)
\qquad
\text{for every cut }S\text{ and }e\in S. \tag{3}
\]
Indeed, (3) says exactly that \(p-T\mathbf1\) satisfies the cut inequalities. It is nonnegative and even, hence admissible; applying the buffer theorem recovers \(p\).

For example, if \(G\) is 3-edge-connected, every even weighting satisfying
\[
T\le b\le p(e)\le2b-T\qquad(e\in E)
\]
has a faithful cover. After subtracting \(T\), the largest edge weight is at most twice the smallest, while every nonempty cut has at least three edges.

These are genuine positive instances, including graphs with Petersen minors, but the threshold depends on the graph size.

### Finite verification for a fixed graph

Theorem A gives a fully specified exhaustive test for the conjecture on one fixed graph:

1. Enumerate all simple cycles of \(G\).
2. On the integer box
   \[
   \{0,1,\ldots,2m-2\}^{E(G)},
   \]
   mark vectors reachable from \(0\) by repeatedly adding a cycle-incidence vector without leaving the box.
3. Test every coordinatewise even vector in the box for admissibility.
4. Check that every admissible vector tested in step 3 was marked in step 2.

Reachability is exactly faithful coverability within the box: partial sums of a cycle cover never exceed its final incidence vector. Passing this finite test proves the conjecture for **all** even admissible weightings on that graph, not just the bounded ones.

There are at most \((2m-1)^m\) dynamic-programming states. This is an exact but exponential procedure. **No computational run is claimed here.**

---

## 7. What remains unresolved

The missing step is eliminating the additive buffer, particularly near tight cut inequalities. Subtracting \(T\mathbf1\) can destroy admissibility, so the buffer theorem cannot simply be applied to an arbitrary original instance.

Likewise, the bounded-weight reduction does not bypass the cycle double cover problem: \(p\equiv2\) remains among the bounded instances.

Thus I obtain quantitative partial results and a finite verification reduction, but neither a proof nor a counterexample to Seymour’s conjecture. I have not established novelty for these deductions and would not presently submit them as a research paper.