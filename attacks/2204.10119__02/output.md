```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any counterexample must have both bipartition classes of size at least seven and must contain at least 63 distinct four-cycles, with stronger quantitative restrictions proved below.",
  "would_publish": false,
  "caveats": "The argument does not control the remaining C4-rich configurations and therefore neither proves nor disproves the conjecture."
}
```

## 1. Statement and scope

All graphs below are finite and simple. The question is whether every bipartite graph \(G\) with
\[
\delta(G)\ge 5
\]
contains a \(K_6\) minor.

I do not settle the question. I prove the following partial results.

1. If \(G\) has at most \(62\) distinct \(4\)-cycles, then \(G\) has a \(K_6\) minor. In particular, the conjecture holds for \(C_4\)-free bipartite graphs.
2. If either bipartition class has size at most \(6\), then \(G\) has a \(K_6\) minor. Thus a counterexample has at least \(14\) vertices.
3. More generally, if the bipartition classes have sizes \(a\le b\), then a counterexample must satisfy
   \[
   7\le a\le b\le \frac56\binom a5.
   \]
   In particular, if \(a=7\), then \(b\le17\).
4. No bipartite graph of minimum degree at least five is apex: deleting one vertex never leaves a planar graph.

The first result is obtained by random star contractions and the sharp \(K_6\) case of Mader's extremal theorem.

---

## 2. The contraction inequality and four-cycles

I use the following standard sharp form of Mader's theorem:

> **Mader's \(K_6\) extremal theorem.**  
> If a simple \(n\)-vertex graph has no \(K_6\) minor, then
> \[
> |E|\le 4n-10.
> \]
> Equivalently, \(4n-9\) edges force a \(K_6\) minor.

Let \(G=(X,Y;E)\) be bipartite, with \(|X|=a\). For every \(y\in Y\), choose a root
\[
\rho(y)\in N(y).
\]
For each \(x\in X\), form the connected branch set
\[
B_x=\{x\}\cup\{y\in Y:\rho(y)=x\}.
\]
Contracting every \(B_x\) produces a simple minor \(H_\rho\) on vertex set \(X\), after parallel edges are suppressed.

For \(\{x,x'\}\in\binom X2\), let
\[
Z_{x,x'}=
\bigl|\{y\in N(x)\cap N(x'):\rho(y)\in\{x,x'\}\}\bigr|.
\]
Then \(xx'\in E(H_\rho)\) exactly when \(Z_{x,x'}\ge1\). Moreover,
\[
\sum_{\{x,x'\}\in\binom X2} Z_{x,x'}
   =\sum_{y\in Y}(d(y)-1)=:R_Y,
\]
because a vertex \(y\), once rooted, creates one potential quotient edge from its root to each of its other \(d(y)-1\) neighbors.

Choose the roots independently and uniformly. For every nonnegative integer \(z\),
\[
\mathbf 1_{\{z\ge1\}}\ge z-\binom z2.
\]
Consequently,
\[
\mathbb E|E(H_\rho)|
 \ge R_Y-W_Y,
\]
where
\[
W_Y=
\sum_{\{x,x'\}\in\binom X2}
\ \sum_{\{y,z\}\in\binom{N(x)\cap N(x')}2}
\frac{4}{d(y)d(z)}.
\tag{2.1}
\]
Indeed, for fixed \(x,x',y,z\), the probability that both \(y\) and \(z\) produce the quotient edge \(xx'\) is
\[
\frac{2}{d(y)}\frac{2}{d(z)}.
\]

Every summand in \(W_Y\) corresponds to one \(4\)-cycle
\[
x-y-x'-z-x.
\]

### Proposition 2.1

If \(G\) has no \(K_6\) minor and \(a\ge6\), then
\[
W_Y\ge R_Y-4a+10.
\tag{2.2}
\]

#### Proof

Every \(H_\rho\) is a minor of \(G\), and hence is \(K_6\)-minor-free. Mader's theorem gives
\[
|E(H_\rho)|\le4a-10
\]
for every choice of \(\rho\). Taking expectations and using the preceding lower bound gives
\[
R_Y-W_Y\le\mathbb E|E(H_\rho)|\le4a-10.
\]
This is exactly (2.2). \(\square\)

There is also an exact, rather than Bonferroni, version:
\[
\mathbb E|E(H_\rho)|
=
\sum_{\{x,x'\}\in\binom X2}
\left(
1-\prod_{y\in N(x)\cap N(x')}
\left(1-\frac2{d(y)}\right)
\right).
\tag{2.3}
\]
Thus if the right-hand side of (2.3) exceeds \(4a-10\), then some \(H_\rho\) has at least \(4a-9\) edges and hence contains a \(K_6\) minor.

### Corollary 2.2: every counterexample has at least \(63\) four-cycles

Let the bipartition classes have sizes
\[
a=|X|\le |Y|=b,
\]
and put
\[
\sigma_Y=\sum_{y\in Y}(d(y)-5).
\]
Then
\[
R_Y=4b+\sigma_Y.
\]
If \(G\) is \(K_6\)-minor-free, Proposition 2.1 gives
\[
W_Y\ge 10+4(b-a)+\sigma_Y.
\tag{2.4}
\]
Since \(d(y),d(z)\ge5\), every \(4\)-cycle contributes at most \(4/25\) to \(W_Y\). Hence, writing \(c_4(G)\) for the number of distinct \(4\)-cycles,
\[
\boxed{
c_4(G)\ge
\left\lceil
\frac{25}{4}\left(10+4(b-a)+\sigma_Y\right)
\right\rceil .
}
\tag{2.5}
\]

In particular,
\[
c_4(G)\ge \left\lceil\frac{25}{4}\cdot10\right\rceil=63.
\]

Thus:

> **Theorem 2.3.**  
> Every bipartite graph of minimum degree at least five with at most \(62\) four-cycles contains a \(K_6\) minor.

In particular, every \(C_4\)-free bipartite graph of minimum degree at least five contains a \(K_6\) minor. For a balanced \(5\)-regular hypothetical counterexample, (2.5) says that at least \(63\) four-cycles are necessary.

---

## 3. A \(6\times6\) lemma

The next lemma handles small bipartition classes.

### Lemma 3.1

Let \(H=(X,Y;E)\), where
\[
|X|=|Y|=6,
\]
and suppose every vertex of \(Y\) has degree at least five. Then \(H\) contains a \(K_6\) minor.

#### Proof

Delete edges if necessary so that every \(y\in Y\) has degree exactly five. Let \(f(y)\in X\) be the unique nonneighbor of \(y\).

Choose \(x_0\in X\) for which \(|f^{-1}(x_0)|\) is maximum, and choose
\[
y_0\in f^{-1}(x_0).
\]
Put
\[
X'=X\setminus\{x_0\},\qquad Y'=Y\setminus\{y_0\}.
\]

We claim that the vertices of \(Y'\) can be bijectively assigned to the vertices of \(X'\), say \(x\mapsto y_x\), so that

1. \(f(y_x)\ne x\); and
2. there are no distinct \(x,x'\in X'\) with
   \[
   f(y_x)=x'\quad\text{and}\quad f(y_{x'})=x.
   \tag{3.1}
   \]

To verify the claim, regard each \(y\in Y'\) as a token labelled \(f(y)\). Tokens labelled \(x_0\) impose no restriction on \(X'\); call them null tokens. Placing a non-null token labelled \(j\) at a source \(i\) is denoted by the arrow \(i\to j\). We need no loop and no directed \(2\)-cycle.

Because \(x_0\) belongs to a largest fiber of \(f\), the possible multiplicities of the non-null labels, after deleting \(y_0\), are precisely those in the left column below. Null tokens occupy all unmentioned sources.

\[
\begin{array}{c|l}
\text{non-null multiplicities}&\text{placement}\\ \hline
()&\text{no arrows}\\
(1)&u\to1\\
(2)&u\to1,\ v\to1\\
(1,1)&u\to1,\ v\to2\\
(3)&u\to1,\ v\to1,\ w\to1\\
(2,1)&u\to1,\ v\to1,\ w\to2\\
(1,1,1)&1\to2,\ 2\to3,\ 3\to1\\
(2,2)&2\to1,\ 3\to1,\ 4\to2,\ 5\to2\\
(2,1,1)&2\to1,\ 3\to1,\ 4\to2,\ 5\to3\\
(1,1,1,1)&1\to2,\ 2\to3,\ 3\to4,\ 4\to1\\
(1,1,1,1,1)&1\to2,\ 2\to3,\ 3\to4,\ 4\to5,\ 5\to1.
\end{array}
\]
Here \(u,v,w\) are distinct sources outside the displayed target labels. Each row has neither a loop nor a \(2\)-cycle, proving the assignment claim.

Now define six branch sets:
\[
Q=\{y_0\},\qquad P_x=\{x,y_x\}\quad(x\in X').
\]
Each \(P_x\) is connected because \(f(y_x)\ne x\). The singleton \(Q\) is adjacent to every \(P_x\), since \(y_0\) is adjacent to every vertex of \(X'\).

Finally, for distinct \(x,x'\), the only way \(P_x\) and \(P_{x'}\) could fail to be adjacent is if both cross-edges were absent:
\[
xy_{x'}\notin E(H),\qquad x'y_x\notin E(H).
\]
This is equivalent to
\[
f(y_{x'})=x,\qquad f(y_x)=x',
\]
which is excluded by (3.1). Thus the six branch sets are pairwise adjacent and form a \(K_6\) model. \(\square\)

### Corollary 3.2

If a bipartite graph \(G\) has minimum degree at least five and one bipartition class has size at most six, then \(G\) contains a \(K_6\) minor.

#### Proof

A bipartition class has size at least five.

If one class has size five, every vertex in the other class is adjacent to all five of its vertices, so \(G\) contains \(K_{5,5}\). A \(K_6\) model in \(K_{5,5}\), with parts
\[
\{x_1,\dots,x_5\},\quad \{y_1,\dots,y_5\},
\]
is
\[
\{x_i,y_i\}\ (1\le i\le4),\qquad \{x_5\},\qquad \{y_5\}.
\]

If the smaller class \(X\) has size six, choose any six vertices in the other class. Each has at least five neighbors in \(X\), and Lemma 3.1 applies. \(\square\)

Hence every counterexample has both bipartition classes of size at least seven, and consequently has at least fourteen vertices.

---

## 4. A stronger fixed-side counting obstruction

Lemma 3.1 also gives a useful finite bound when one bipartition class is fixed.

### Proposition 4.1

Let \(G=(X,Y;E)\), where \(|X|=a\ge6\). If \(G\) has no \(K_6\) minor, then
\[
\boxed{
\sum_{y\in Y}
\left[
\binom{d(y)}6+(a-d(y))\binom{d(y)}5
\right]
\le 5\binom a6.
}
\tag{4.1}
\]

#### Proof

For \(y\in Y\), the quantity
\[
\binom{d(y)}6+(a-d(y))\binom{d(y)}5
\]
counts the six-element subsets \(S\subseteq X\) for which
\[
|N(y)\cap S|\ge5.
\]
Indeed, either all six vertices of \(S\) are neighbors of \(y\), or exactly five are neighbors and the sixth is a nonneighbor.

If (4.1) failed, double counting pairs \((y,S)\) would give a six-element set \(S\subseteq X\) for which at least six vertices \(y\in Y\) have at least five neighbors in \(S\). Choosing six such vertices produces a \(6\times6\) bipartite subgraph satisfying Lemma 3.1, and hence a \(K_6\) minor. \(\square\)

Since \(d(y)\ge5\), each vertex \(y\) is counted for at least \(a-5\) six-subsets: fix five of its neighbors and adjoin any one of the remaining \(a-5\) vertices of \(X\). Therefore, if \(|Y|=b\),
\[
b(a-5)\le5\binom a6.
\]
Using
\[
\binom a6=\frac{a-5}{6}\binom a5
\]
gives:

> **Corollary 4.2.**  
> If a bipartite graph with \(\delta(G)\ge5\) and bipartition sizes \(a\le b\) is \(K_6\)-minor-free, then
> \[
> \boxed{b\le\frac56\binom a5.}
> \]

For example:

- \(a=6\) would give \(b\le5\), another proof that this case is impossible;
- \(a=7\) gives \(b\le17\);
- \(a=8\) gives \(b\le46\).

Thus the first bipartition-size range not settled by these arguments is
\[
7\le a\le b\le17.
\]

---

## 5. Apex graphs cannot occur

The familiar general \(K_6\)-minor-free constructions obtained by adjoining an apex to a planar graph cannot yield a counterexample here.

### Proposition 5.1

No bipartite graph of minimum degree at least five becomes planar after deleting one vertex.

#### Proof

Suppose \(G=(A,B;E)\), \(v\in A\), and \(H=G-v\) is planar. Put
\[
a=|A|-1,\qquad b=|B|,\qquad m=|E(H)|.
\]
Every vertex of \(A\setminus\{v\}\) retains all its neighbors, so
\[
m\ge5a.
\]
Every vertex of \(B\) loses at most the edge to \(v\), so
\[
m\ge4b.
\]

The graph \(H\) is planar and bipartite. Applying the planar bipartite edge bound componentwise gives
\[
m\le2(a+b)-4.
\]
Consequently,
\[
5a\le2a+2b-4,
\]
and hence
\[
b\ge\frac32a+2.
\]
On the other hand,
\[
4b\le2a+2b-4,
\]
so
\[
b\le a-2.
\]
These inequalities are incompatible. The case \(v\in B\) is symmetric. \(\square\)

---

## 6. What remains open

The results above leave a genuine gap. A hypothetical counterexample \(G=(X,Y)\), with \(|X|=a\le b=|Y|\), must satisfy all of the following:

\[
7\le a\le b\le\frac56\binom a5,
\]
\[
c_4(G)\ge
\left\lceil
\frac{25}{4}
\left(
10+4(b-a)+\sum_{y\in Y}(d(y)-5)
\right)
\right\rceil,
\]
and \(G\) is not apex.

The random-contraction argument is exact in identifying the obstruction: numerous \(4\)-cycles cause different contracted stars to create parallel copies of the same quotient edge. The estimates above force that phenomenon to be substantial, but they do not show that a sufficiently \(C_4\)-rich configuration itself contains a \(K_6\) minor. No complete proof or counterexample follows from the present argument.