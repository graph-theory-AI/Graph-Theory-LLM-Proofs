```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove sharp local frequency bounds for members of size at most six, including that 19 is the minimum family size permitting a three-element member with no abundant element.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is unresolved here; these local results do not improve the general abundance bound, and novelty is not claimed."
}
```

# Sharp frequency bounds inside a specified small member

I do not obtain a proof or counterexample to Frankl’s conjecture. The results below concern the stronger requirement that an abundant element lie in a **specified member** of the family.

The injection underlying the supplied attempt is valid. I use its two-point special case below and reprove it. The rest of the argument uses a different construction and a decomposition into trace fibres.

Let \(\mathcal F\) be a finite union-closed family, and write
\[
m=|\mathcal F|,\qquad
d(x)=|\{B\in\mathcal F:x\in B\}|.
\]
An element is **abundant** if \(d(x)\ge m/2\). For a nonempty \(A\in\mathcal F\), put
\[
D_A=\max_{a\in A}d(a).
\]

## 1. Statements of the partial results

### Theorem 1 — Optimal local constants for members of size at most six

If \(A\in\mathcal F\) and \(1\le r=|A|\le6\), then
\[
D_A\ge c_r m,
\]
where
\[
\begin{array}{c|cccccc}
r&1&2&3&4&5&6\\ \hline
c_r&\frac12&\frac12&\frac49&\frac25&\frac9{25}&\frac13
\end{array}
\]

Each constant is optimal: for every \(\varepsilon>0\), there is such a pair \((\mathcal F,A)\) with
\[
\frac{D_A}{m}<c_r+\varepsilon.
\]
This remains true if \(A\) is required to be the unique nonempty member of minimum cardinality.

Thus even choosing a unique smallest member does not, in general, locate an abundant element.

### Theorem 2 — A sharp finite bound for a three-element member

Suppose \(A\in\mathcal F\), \(|A|=3\), and no element of \(A\) is abundant. Then
\[
\boxed{9D_A\ge 4m+5.}
\]

Consequently:

- if \(m\) is odd, then \(m\ge19\);
- if \(m\) is even, then \(m\ge28\).

Both thresholds are attained. More generally, for every integer \(t\ge1\), there is a union-closed family with a three-element member \(A\) such that
\[
m=9t+10,\qquad d(a)=4t+5\quad(a\in A).
\]
These examples satisfy
\[
2d(a)-m=-t,\qquad 9d(a)=4m+5.
\]

In particular, the smallest possible family containing a three-element member with no abundant element has exactly \(19\) members.

These are **not counterexamples to Frankl’s conjecture**: the constructions have abundant elements outside \(A\).

---

## 2. Decomposition into outside-trace fibres

Fix a nonempty \(A\in\mathcal F\), and set
\[
X=\bigcup\mathcal F,\qquad O=X\setminus A.
\]
For each outside part \(Y\subseteq O\) that occurs, define
\[
\mathcal U_Y=\{S\subseteq A:Y\cup S\in\mathcal F\}.
\]

Every nonempty fibre \(\mathcal U_Y\) is union-closed. Moreover,
\[
A\in\mathcal U_Y:
\]
if \(Y\cup S\in\mathcal F\), then union with the member \(A\) gives \(Y\cup A\in\mathcal F\).

The fibres partition \(\mathcal F\), so
\[
m=\sum_Y|\mathcal U_Y|
\]
and
\[
\sum_{a\in A}d(a)
=
\sum_Y\sum_{S\in\mathcal U_Y}|S|.
\tag{1}
\]

This turns a local frequency problem into an average-set-size problem on the fixed ground set \(A\).

## 3. Minimum average size on at most six points

Let \(|A|=r\), and let \(\mathcal U\subseteq2^A\) be union-closed with \(A\in\mathcal U\).

Adjoining \(\varnothing\), if necessary, only decreases the average set size. Thus assume \(\varnothing\in\mathcal U\).

Let
\[
I=\{a\in A:\{a\}\in\mathcal U\},\qquad j=|I|.
\]
Union-closure implies \(2^I\subseteq\mathcal U\).

If \(j=r\), then \(\mathcal U=2^A\), whose average set size is \(r/2\).

If \(j<r\), then \(\mathcal U\) contains
\[
2^I\cup\{A\},
\]
whose average set size is
\[
\frac{r+j2^{j-1}}{2^j+1}.
\tag{2}
\]
For \(j=0\), interpret \(j2^{j-1}\) as \(0\).

Every other member of \(\mathcal U\) has size at least two: the empty set and all singleton members are already in \(2^I\).

Define
\[
\alpha_r=
\min\left\{
\frac r2,\
\min_{0\le j<r}
\frac{r+j2^{j-1}}{2^j+1}
\right\}.
\]
Whenever \(\alpha_r\le2\), the preceding observations imply
\[
\frac1{|\mathcal U|}\sum_{S\in\mathcal U}|S|\ge\alpha_r.
\tag{3}
\]
Indeed, the indicated subfamily has average at least \(\alpha_r\), and every additional member has size at least \(2\ge\alpha_r\).

Evaluating the finite minimum gives
\[
\begin{array}{c|cccccc}
r&1&2&3&4&5&6\\ \hline
\alpha_r&\frac12&1&\frac43&\frac85&\frac95&2
\end{array}
\]
so (3) applies in all six cases.

Applying (3) to every fibre in (1) yields
\[
\sum_{a\in A}d(a)\ge\alpha_r m.
\]
Therefore
\[
D_A\ge\frac{\alpha_r}{r}m=c_rm.
\]
This proves the lower bounds in Theorem 1.

The argument does not assert the same formula for larger \(r\): already for \(r=7\), the displayed minimum exceeds \(2\), and additional two-element members can no longer be discarded in this averaging argument.

---

## 4. The stronger finite bound for a three-element member

Let \(A=\{a,b,c\}\).

### 4.1. An excess associated with a fibre

For a union-closed \(\mathcal U\subseteq2^A\) containing \(A\), define
\[
e(\mathcal U)=3\sum_{S\in\mathcal U}|S|-4|\mathcal U|.
\]
Let \(u_i\) denote the number of \(i\)-element members of \(\mathcal U\). Since \(u_3=1\),
\[
e(\mathcal U)=5-4u_0-u_1+2u_2.
\]
The unions of distinct singleton members are distinct pairs, so
\[
u_2\ge\binom{u_1}{2}.
\]
Consequently,
\[
e(\mathcal U)
\ge (u_1-1)^2+4(1-u_0).
\tag{4}
\]

We will use four consequences:

1. \(e(\mathcal U)\ge0\);
2. if \(\varnothing\notin\mathcal U\), then \(e(\mathcal U)\ge4\);
3. if \(\mathcal U\) has no singleton member, then \(e(\mathcal U)\ge1\);
4. \(e(2^A)=4\).

### 4.2. What local nonabundance forces

Assume no element of \(A\) is abundant.

First, no singleton \(\{a\}\), \(\{b\}\), or \(\{c\}\) belongs to \(\mathcal F\). For example, if \(\{a\}\in\mathcal F\), the map
\[
B\longmapsto B\cup\{a\}
\]
injects members avoiding \(a\) into members containing \(a\), proving that \(a\) is abundant.

Second, **all three singleton traces on \(A\) must occur**.

To prove this, suppose, for example, that \(\{a\}\) is not a trace. Then \(\{b,c\}\) meets every nonempty trace on \(A\). Partition \(\mathcal F\) into:

- \(p\) members disjoint from \(A\);
- \(q\) members containing \(A\);
- \(t\) remaining members.

The map \(B\mapsto A\cup B\) injects the first class into the second, so \(q\ge p\). Hence
\[
d(b)+d(c)\ge2q+t\ge p+q+t=m,
\]
contradicting the assumption that both \(b\) and \(c\) are nonabundant.

This is the two-point injection argument reused from the supplied lead.

### 4.3. Two fibres contribute at least five units of excess

Return to the fibres \(\mathcal U_Y\).

The bottom fibre \(\mathcal U_{\varnothing}\) contains \(A\) but has no singleton member. Thus
\[
e(\mathcal U_{\varnothing})\ge1.
\tag{5}
\]

The top outside part \(O=X\setminus A\) also occurs, because \(X\in\mathcal F\). Consider \(\mathcal U_O\).

- If \(\varnothing\notin\mathcal U_O\), then (4) gives
  \[
  e(\mathcal U_O)\ge4.
  \]
- If \(\varnothing\in\mathcal U_O\), then \(O\in\mathcal F\). For each \(x\in A\), choose a member whose trace on \(A\) is \(\{x\}\). Union with \(O\) shows that \(\{x\}\in\mathcal U_O\). Thus
  \[
  \mathcal U_O=2^A,
  \]
  and again \(e(\mathcal U_O)=4\).

These are distinct fibres. Indeed, \(O=\varnothing\) would make every singleton trace a singleton member, contrary to the preceding subsection.

All other fibres have nonnegative excess. Summing therefore gives
\[
\begin{aligned}
3\sum_{x\in A}d(x)-4m
&=\sum_Y e(\mathcal U_Y)\\
&\ge1+4=5.
\end{aligned}
\]
Since \(\sum_{x\in A}d(x)\le3D_A\),
\[
9D_A\ge4m+5.
\]

This proves the inequality in Theorem 2.

If \(m=2h+1\), nonabundance gives \(D_A\le h\), whence
\[
9h\ge8h+9,
\]
so \(h\ge9\) and \(m\ge19\).

If \(m=2h\), nonabundance gives \(D_A\le h-1\), whence
\[
9(h-1)\ge8h+5,
\]
so \(h\ge14\) and \(m\ge28\).

---

## 5. Explicit constructions proving sharpness

The following construction proves all the sharpness assertions.

Fix a set \(A\) of size \(r\ge3\), and choose an integer \(k\) with \(1\le k<r\). List every \(k\)-subset of \(A\) exactly \(t\) times:
\[
B_1,\ldots,B_N,\qquad N=t\binom rk.
\]
Introduce distinct markers
\[
M=\{z_1,\ldots,z_N\},\qquad V_i=M\setminus\{z_i\}.
\]
Set
\[
\mathcal L_i=2^{B_i}\cup\{A\}
\]
and define
\[
\boxed{
\mathcal F=
\{\varnothing,A\}
\;\cup\;
\bigcup_{i=1}^N\{V_i\cup S:S\in\mathcal L_i\}
\;\cup\;
\{M\cup S:S\subseteq A\}.
}
\tag{6}
\]

### Union-closure

Each \(\mathcal L_i\) is union-closed. Thus unions within one \(V_i\)-layer remain there.

For \(i\ne j\),
\[
V_i\cup V_j=M,
\]
so unions between different layers belong to the top layer. Unions involving the top layer remain there.

Finally, union with \(A\) replaces the trace by \(A\), which is allowed in every layer; union with \(\varnothing\) changes nothing. These cases cover all pairs of members.

### Counts

The outside parts \(\varnothing,V_1,\ldots,V_N,M\) are distinct, so
\[
m=2+N(2^k+1)+2^r.
\tag{7}
\]

For any \(a\in A\),
\[
d(a)
=
1+N+
t\binom{r-1}{k-1}2^{k-1}
+2^{r-1}.
\tag{8}
\]
Indeed, each middle layer contributes its trace \(A\), and a layer whose \(B_i\) contains \(a\) contributes another \(2^{k-1}\) occurrences.

Every element of \(A\) has the same frequency. From (7)–(8),
\[
\lim_{t\to\infty}\frac{d(a)}m
=
\frac{r+k2^{k-1}}{r(2^k+1)}.
\tag{9}
\]

Choose
\[
(r,k)=(3,1),(4,2),(5,2),(6,2).
\]
The limits in (9) are respectively
\[
\frac49,\qquad\frac25,\qquad\frac9{25},\qquad\frac13.
\]
For \(r=1,2\), the family \(\{\varnothing,A\}\) attains frequency \(1/2\). This proves optimality of every constant in Theorem 1.

### Exact three-element examples

For \(r=3\) and \(k=1\), equations (7)–(8) become
\[
m=9t+10,\qquad d(a)=4t+5\quad(a\in A).
\]
Therefore
\[
2d(a)-m=-t<0
\]
and
\[
9d(a)=4m+5.
\]

Taking \(t=1\) gives \(19\) sets, with each of the three designated elements occurring \(9\) times. Taking \(t=2\) gives \(28\) sets, with each occurring \(13\) times. Thus both parity thresholds in Theorem 2 are sharp.

### Making \(A\) uniquely smallest by cardinality

Replace each marker \(z_i\) by a disjoint block of \(q\) new elements, always included or excluded together. This replacement is injective and preserves unions, family size, and all frequencies of elements of \(A\).

Every nonempty member other than \(A\) then has at least \(q(N-1)\) outside elements. Choosing
\[
q(N-1)>r
\]
makes \(A\) the unique nonempty member of minimum cardinality.

For the \(19\)-set example, blocks of size two suffice.

### Why these are not counterexamples to Frankl

A marker \(z_i\) is absent precisely from the two bottom sets and its own layer. Hence
\[
d(z_i)=m-(2^k+3)>\frac m2
\]
for the parameters above. After block replacement, every element of the corresponding block has the same abundant frequency.

---

## 6. Scope and remaining gap

The results give a complete answer to the optimal **specified-member** frequency question for member sizes at most six, together with a sharp finite obstruction at size three.

They also show precisely why a natural strategy fails:

> Even a unique nonempty member of minimum cardinality need not contain an abundant element.

The constructions defeat that strengthening while leaving abundant marker elements outside the designated member. What is not proved is a general mechanism forcing an abundant outside element whenever local abundance fails. Consequently, these results neither resolve Frankl’s conjecture nor improve its best general abundance bound. No claim of originality is made.