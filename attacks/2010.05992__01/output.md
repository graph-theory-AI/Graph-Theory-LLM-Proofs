```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The displayed bound is never attained at finite length, and admits an exponentially large additive improvement, but the argument does not give a uniform multiplicative or exponential-rate improvement on lengths divisible by r-1.",
  "would_publish": false,
  "caveats": "The phrase “not tight” is ambiguous; this settles exact nonattainment, not the likely intended asymptotic binary conjecture."
}
```

## 1. Statement and interpretation

Write
\[
G_{r,q}(n)=g_r^{q\text{-ff}}(n),\qquad m=r-1.
\]
I use the standard definition from the source: distinct words
\[
x^{(0)},x^{(1)},\dots,x^{(m)}\in[q]^n
\]
form an \(r\)-focal family with focus \(x^{(0)}\) if, in every coordinate, at most one of the \(m\) other words differs from \(x^{(0)}\). Equivalently, the \(m\) nonempty difference supports
\[
\operatorname{supp}(x^{(j)}-x^{(0)}),\qquad 1\le j\le m,
\]
are pairwise disjoint.

The Alon–Holzman bound is
\[
G_{r,q}(n)\le m q^{\left\lceil (m-1)n/m\right\rceil}.
\tag{1}
\]

The phrase “not tight” has at least three possible meanings:

1. the right side of (1) is never attained exactly;
2. its multiplicative constant \(m\) can be replaced by \(m-\varepsilon_r\);
3. its exponential rate \((m-1)/m\) can be decreased for \(q=2\).

The argument below completely proves (1) is not attained exactly, and gives an exponentially large additive saving. It does not establish either of the stronger asymptotic interpretations.

---

## 2. A private-fiber refinement

### Lemma 1

Let \(B_1,\dots,B_m\) be a partition of the coordinate set into nonempty blocks of sizes
\[
t_1,\dots,t_m,\qquad \sum_j t_j=n.
\]
Put
\[
P=q^n,\qquad Q_j=q^{t_j},\qquad V_j=\frac{P}{Q_j},
\qquad
S=\sum_{j=1}^m\frac1{Q_j-1}.
\]
Then
\[
G_{r,q}(n)
\le
\left\lfloor \frac{PS}{1+S}\right\rfloor.
\tag{2}
\]
Independently,
\[
G_{r,q}(n)\le \sum_{j=1}^m V_j.
\tag{3}
\]

### Proof

Let \(C\subseteq[q]^n\) be \(r\)-focal-free, and write \(M=|C|\).

For each \(j\), partition \(C\) into fibers according to the projection onto the coordinates outside \(B_j\). Thus two words are in the same \(j\)-fiber precisely when they agree outside \(B_j\). There are \(V_j=q^{n-t_j}\) possible fibers, each of size at most \(Q_j=q^{t_j}\).

Call a word \(x\in C\) \(j\)-private if its \(j\)-fiber has size one. If \(x\) were not \(j\)-private for any \(j\), we could choose, for every \(j\), a word
\[
x^{(j)}\ne x
\]
which agrees with \(x\) outside \(B_j\). The difference support of \(x^{(j)}\) from \(x\) is then a nonempty subset of \(B_j\). These \(m\) supports are pairwise disjoint, and the \(x^{(j)}\) are distinct. Hence
\[
x,x^{(1)},\dots,x^{(m)}
\]
would be an \(r\)-focal family. Therefore every word of \(C\) is private in at least one direction.

Let \(v_j\) be the number of \(j\)-fibers of size exactly one. Since every singleton fiber contributes one private word,
\[
M\le \sum_{j=1}^m v_j.
\tag{4}
\]
As \(v_j\le V_j\), (3) follows.

For the sharper estimate, sum the sizes of all \(j\)-fibers. The \(v_j\) singleton fibers contribute \(v_j\), while every other fiber contributes at most \(Q_j\). Hence
\[
M\le v_j+Q_j(V_j-v_j)
   =P-(Q_j-1)v_j.
\]
Thus
\[
v_j\le \frac{P-M}{Q_j-1}.
\]
Summing this and using (4) gives
\[
M\le (P-M)\sum_{j=1}^m\frac1{Q_j-1}
   =(P-M)S.
\]
Therefore \(M(1+S)\le PS\), proving (2). ∎

---

## 3. Exact nonattainment of the displayed bound

Write
\[
n=mt+s,\qquad 0\le s<m,
\]
and assume \(n\ge m\), so \(t\ge1\). Also,
\[
\left\lceil\frac{(m-1)n}{m}\right\rceil
=n-\left\lfloor\frac nm\right\rfloor=n-t.
\tag{5}
\]

### Case 1: \(1\le s<m\)

Take \(m-s\) blocks of size \(t\) and \(s\) blocks of size \(t+1\). From (3),
\[
\begin{aligned}
G_{r,q}(n)
&\le (m-s)q^{n-t}+s q^{n-t-1}\\
&=\left(m-s+\frac{s}{q}\right)q^{n-t}\\
&<m q^{n-t}.
\end{aligned}
\tag{6}
\]
Using (5), this is strictly smaller than the right side of (1). In particular, for \(q=2\),
\[
G_{r,2}(n)
\le \left(m-\frac s2\right)2^{\lceil(m-1)n/m\rceil}.
\tag{7}
\]

### Case 2: \(s=0\)

Now \(n=mt\). Take all blocks of size \(t\), and set \(Q=q^t\). Lemma 1 gives
\[
G_{r,q}(mt)
\le
\left\lfloor
\frac{mQ^m}{Q+m-1}
\right\rfloor.
\tag{8}
\]
On the other hand, the right side of (1) is
\[
m q^{(m-1)t}=mQ^{m-1}.
\]
The ratio of the real quantity in (8) to this bound is
\[
\frac{Q}{Q+m-1}<1.
\]
Consequently,
\[
G_{r,q}(mt)<m q^{(m-1)t}.
\tag{9}
\]

Combining the two cases proves:

### Corollary 2

For every \(r\ge3\), \(q\ge2\), and \(n\ge r-1\),
\[
G_{r,q}(n)
<
(r-1)q^{\left\lceil (r-2)n/(r-1)\right\rceil}.
\tag{10}
\]

Thus, under the literal “equality” interpretation, the catalog statement is proved, and in fact binaryity is unnecessary.

---

## 4. A recursive, exponentially additive improvement

The preceding counting can use the focal-free condition inside each fiber.

For a block \(B_j\) of size \(t_j\), every \(j\)-fiber induces an \(r\)-focal-free code of length \(t_j\). Hence its size is at most
\[
D_j:=G_{r,q}(t_j).
\]
Repeating the proof of Lemma 1 gives
\[
M\le D_jV_j-(D_j-1)v_j,
\]
and hence
\[
v_j\le \frac{D_jV_j-M}{D_j-1}.
\]
Together with \(M\le\sum_jv_j\), this yields
\[
G_{r,q}(n)
\le
\left\lfloor
\frac{\displaystyle\sum_{j=1}^m
 \frac{D_jV_j}{D_j-1}}
{\displaystyle 1+\sum_{j=1}^m\frac1{D_j-1}}
\right\rfloor.
\tag{11}
\]

For \(n=mt\), all blocks equal, so with \(D_t=G_{r,q}(t)\),
\[
G_{r,q}(mt)
\le
\left\lfloor
\frac{mD_t}{D_t+m-1}\,q^{(m-1)t}
\right\rfloor.
\tag{12}
\]

For \(q=2\), apply the original bound at the shorter length \(t\):
\[
D_t\le \widehat D_t
:=m2^{\left\lceil (m-1)t/m\right\rceil}.
\]
Since \(D/(D+m-1)\) is increasing in \(D\), (12) implies
\[
G_{r,2}(mt)
\le
\frac{m\widehat D_t}{\widehat D_t+m-1}\,2^{(m-1)t}.
\tag{13}
\]
Thus the saving from the catalog bound \(m2^{(m-1)t}\) is at least
\[
\frac{m(m-1)2^{(m-1)t}}
{m2^{\lceil(m-1)t/m\rceil}+m-1}.
\tag{14}
\]
In particular,
\[
G_{r,2}(mt)
\le
m2^{(m-1)t}
-\frac{m-1}{4}\,
 2^{(m-1)^2t/m}.
\tag{15}
\]
If \(\alpha=(m-1)/m=(r-2)/(r-1)\) and \(n=mt\), this has the form
\[
G_{r,2}(n)
\le m2^{\alpha n}-2^{\alpha^2n-O_r(1)}.
\tag{16}
\]

So even on the difficult divisible lengths, the numerical gap is exponentially large, though exponentially smaller than the main term.

---

## 5. The case \(r=3\)

Here \(m=2\). Splitting the coordinates into blocks of sizes \(a,b\), regard a codeword as an edge of a bipartite graph with parts of sizes \(2^a\) and \(2^b\).

If an edge had degree at least two at both endpoints, choosing one other edge at each endpoint would produce two words whose difference supports from the original word lie in the two disjoint blocks. Thus every edge has a degree-one endpoint. Such a bipartite graph is a disjoint union of stars, and has at most
\[
2^a+2^b-2
\]
edges. Consequently,
\[
G_{3,2}(2t)\le 2^{t+1}-2,
\qquad
G_{3,2}(2t+1)\le 3\cdot2^t-2.
\tag{17}
\]

For example, the second bound is exact at \(n=3\): the four words
\[
000,\quad 011,\quad 101,\quad 110
\]
are 3-focal-free.

The recursive form of (12) becomes
\[
G_{3,2}(2t)
\le
\left\lfloor
\frac{2^{t+1}G_{3,2}(t)}
{G_{3,2}(t)+1}
\right\rfloor.
\tag{18}
\]

---

## 6. What remains open

The estimates above do not prove either of the likely intended asymptotic statements.

For \(n=mt\), the elementary bound (8) has ratio
\[
\frac{2^t}{2^t+m-1}\longrightarrow1
\]
to the Alon–Holzman upper bound. Even (16) has the same exponential rate:
\[
\limsup_{n\to\infty}\frac1n\log_2 G_{r,2}(n)
\le \frac{r-2}{r-1},
\]
with no strict improvement obtained here.

Thus the following stronger assertions remain unproved by this argument:

- there exists \(\varepsilon_r>0\) such that
  \[
  G_{r,2}(n)\le (r-1-\varepsilon_r)
  2^{\lceil(r-2)n/(r-1)\rceil}
  \quad\text{for all large }n;
  \]
- or, more strongly,
  \[
  \limsup_{n\to\infty}\frac1n\log_2G_{r,2}(n)
  <\frac{r-2}{r-1}.
  \]

Given the source’s comparison with Reed–Solomon constructions and its emphasis on the linear binary case, one of these asymptotic meanings is probably what was intended. I therefore classify the result as partial rather than claiming resolution of the substantive binary conjecture.