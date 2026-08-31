```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The extremal value is determined for all k at most ell squared, all sufficiently large k, every k divisible by ell, and completely for ell at most 3, but a transition window remains for ell at least 4.",
  "would_publish": false,
  "caveats": "Assumes finite simple graphs of unrestricted order and the source definition of an unordered happy triple."
}
```

## 1. Statement and notation

Throughout, graphs are finite and simple. Following the source paper, a three-element vertex set is **happy** if it spans at least two edges. Thus a happy triple induces either \(P_3\) or \(K_3\).

Let
\[
M(k,\ell)=\max\{h(G): |E(G)|=k,\ \Delta(G)\le \ell\},
\]
where \(h(G)\) denotes the number of happy triples.

Isolated vertices are irrelevant. In particular, the unrestricted order of \(G\) causes no finiteness issue.

For later use, define two functions.

Write
\[
k=q\ell+s,\qquad 0\le s<\ell,
\]
and put
\[
\Phi_\ell(k)
=
q\binom{\ell}{2}
+\binom{s}{2}
+\ell\binom{q}{2}
+sq.
\tag{1}
\]

Also write
\[
2k=Q\ell+R,\qquad 0\le R<\ell,
\]
and put
\[
U_\ell(k)
=
Q\binom{\ell}{2}+\binom{R}{2}
=
k(\ell-1)-\frac{R(\ell-R)}2.
\tag{2}
\]

The main partial result is as follows.

### Theorem

Let \(\ell\ge1\).

1. If \(k\le \ell^2\), then
   \[
   \boxed{M(k,\ell)=\Phi_\ell(k).}
   \tag{3}
   \]

2. For all \(k,\ell\),
   \[
   \boxed{M(k,\ell)\le U_\ell(k).}
   \tag{4}
   \]

3. The bound in (4) is attained in either of the following cases:
   \[
   s=0,\ q\ge \ell,
   \tag{5}
   \]
   or
   \[
   1\le s<\ell,\qquad q\ge \ell+s-1.
   \tag{6}
   \]
   Consequently,
   \[
   \boxed{M(k,\ell)=U_\ell(k)\quad\text{whenever }k\ge2\ell(\ell-1).}
   \tag{7}
   \]

4. In particular, if \(k=q\ell\), then the problem is completely solved:
   \[
   \boxed{
   M(q\ell,\ell)=
   \begin{cases}
   \dfrac{q\ell}{2}\,(\ell+q-2),&q\le \ell,\\[2mm]
   q\ell(\ell-1),&q\ge \ell.
   \end{cases}}
   \tag{8}
   \]

Thus, in the requested regime \(\ell<k/2\), the problem is solved throughout
\[
2\ell<k\le \ell^2
\]
and throughout
\[
k\ge2\ell(\ell-1),
\]
as well as for every \(k\) divisible by \(\ell\).

The results also determine the whole problem for \(\ell\le3\).

---

## 2. The basic wedge identity and degree upper bound

Let \(t(G)\) be the number of triangles in \(G\). The number of unordered pairs of incident edges is
\[
P(G)=\sum_{v\in V(G)}\binom{d(v)}2.
\]
Every happy induced \(P_3\) contributes once to \(P(G)\), while every triangle contributes three times. Hence
\[
h(G)=P(G)-2t(G).
\tag{9}
\]
In particular,
\[
h(G)\le \sum_v\binom{d(v)}2.
\tag{10}
\]

Now maximize the right-hand side over integer degree vectors with sum \(2k\) and entries at most \(\ell\), ignoring graphicality. If
\[
0<a\le b<\ell,
\]
then replacing \(a,b\) by \(a-1,b+1\) increases the objective by
\[
\binom{a-1}{2}+\binom{b+1}{2}
-\binom a2-\binom b2
=b-a+1>0.
\]
Therefore the relaxed optimum has \(Q\) entries equal to \(\ell\), one entry equal to \(R\) if \(R>0\), and all remaining entries zero, where \(2k=Q\ell+R\). This proves
\[
h(G)\le U_\ell(k).
\]

It also gives an exact equality criterion:

> Equality \(h(G)=U_\ell(k)\) holds if and only if \(G\) is triangle-free and its positive degree sequence is
> \[
> (\ell,\ldots,\ell,R),
> \]
> omitting the last entry when \(R=0\).

The cruder consequence
\[
h(G)\le k(\ell-1)
\tag{11}
\]
follows directly from
\[
\binom d2\le \frac{\ell-1}{2}d.
\]

---

## 3. Exact solution for \(k\le\ell^2\)

We first record two elementary facts about \(\Phi_\ell\).

### Lemma 1: Recurrence

For \(k\ge\ell\),
\[
\Phi_\ell(k)
=
\binom{\ell}{2}+(k-\ell)+\Phi_\ell(k-\ell).
\tag{12}
\]

#### Proof

Writing \(k=q\ell+s\), one has \(k-\ell=(q-1)\ell+s\). Substitution into (1) gives
\[
\begin{aligned}
\Phi_\ell(k)-\Phi_\ell(k-\ell)
&=\binom{\ell}{2}
+\ell\left[\binom q2-\binom{q-1}2\right]+s\\
&=\binom{\ell}{2}+\ell(q-1)+s\\
&=\binom{\ell}{2}+k-\ell.
\end{aligned}
\]
\(\square\)

### Lemma 2: Monotonicity in the degree cap

If \(m\le L^2\), then
\[
\Phi_L(m)\le \Phi_{L+1}(m).
\tag{13}
\]

#### Proof

Write \(m=aL+b\), with \(0\le b<L\). Since \(m\le L^2\), we have \(a\le L\).

If \(b\ge a\), then
\[
m=a(L+1)+(b-a),
\]
and direct substitution gives
\[
\Phi_{L+1}(m)-\Phi_L(m)=a(L-b)\ge0.
\]

If \(b<a\), then
\[
m=(a-1)(L+1)+(L+b-a+1),
\]
and substitution gives
\[
\Phi_{L+1}(m)-\Phi_L(m)=b(L-a)\ge0.
\]
\(\square\)

We also need the following estimate near the square threshold.

### Lemma 3

If
\[
(\ell-1)^2<k\le \ell^2,
\]
then
\[
\Phi_\ell(k)\ge k(\ell-2).
\tag{14}
\]

#### Proof

Write \(k=q\ell+s\).

The relevant possibilities are:

- \(q=\ell-2\) and \(2\le s<\ell\), in which case
  \[
  \Phi_\ell(k)-k(\ell-2)=\binom{s}{2};
  \]

- \(q=\ell-1\), in which case
  \[
  \Phi_\ell(k)-k(\ell-2)
  =\frac{\ell(\ell-1)+s(s+1)}2;
  \]

- \(q=\ell,s=0\), in which case the difference is \(\ell^2\).

All are nonnegative. \(\square\)

### Proof of Theorem, part 1

We prove by induction on \(\ell\), with an inner induction on \(k\), that
\[
h(G)\le\Phi_\ell(k)
\]
whenever \(k\le\ell^2\) and \(\Delta(G)\le\ell\).

Let \(d=\Delta(G)\).

#### Case 1: \(d\le\ell-1\)

If \(k\le(\ell-1)^2\), the induction hypothesis and Lemma 2 give
\[
h(G)\le\Phi_{\ell-1}(k)\le\Phi_\ell(k).
\]

If \(k>(\ell-1)^2\), then by (10),
\[
h(G)
\le\sum_v\binom{d(v)}2
\le k(\ell-2)
\le\Phi_\ell(k),
\]
where the last inequality is Lemma 3.

#### Case 2: \(d=\ell\)

Choose \(v\) with \(d(v)=\ell\), and set
\[
A=N(v),\qquad
B=V(G)\setminus(A\cup\{v\}).
\]
Let \(c=e(A,B)\).

A happy triple containing \(v\) is either:

- \(v\) together with two vertices of \(A\), giving \(\binom{\ell}{2}\) triples; or
- \(v,a,b\) with \(a\in A,b\in B\) and \(ab\in E(G)\), giving \(c\) triples.

Therefore
\[
h(G)=h(G-v)+\binom{\ell}{2}+c.
\tag{15}
\]
Since all \(c\) edges are among the \(k-\ell\) edges not incident with \(v\),
\[
c\le k-\ell.
\]
The inner induction and Lemma 1 now give
\[
\begin{aligned}
h(G)
&\le \Phi_\ell(k-\ell)+\binom{\ell}{2}+k-\ell\\
&=\Phi_\ell(k).
\end{aligned}
\]

This proves the upper bound.

For equality, write \(k=q\ell+s\). Construct a bipartite graph with one part consisting of \(q\) vertices adjacent to all \(\ell\) vertices in the other part, together, when \(s>0\), with one further vertex adjacent to \(s\) vertices in the \(\ell\)-vertex part. Its degree multisets on the two sides are
\[
(\ell^q,s)
\quad\text{and}\quad
((q+1)^s,q^{\ell-s}),
\]
respectively. Since \(k\le\ell^2\), its maximum degree is at most \(\ell\). It is triangle-free and has
\[
q\binom{\ell}{2}+\binom{s}{2}
+s\binom{q+1}{2}+(\ell-s)\binom q2
=\Phi_\ell(k)
\]
happy triples.

Thus \(M(k,\ell)=\Phi_\ell(k)\). \(\square\)

### Relation to Lemma 2 of the source

When \(\ell\ge k/2\) and \(\ell\le k<2\ell\), one has \(q=1\) and \(s=k-\ell\). Formula (3) becomes
\[
M(k,\ell)
=
\binom{\ell}{2}+\binom{k-\ell+1}{2},
\]
which is the source-paper bound. Thus (3) extends that result from \(k\le2\ell\) all the way to \(k\le\ell^2\).

---

## 4. Attaining the degree upper bound for large \(k\)

It remains to construct triangle-free graphs with the degree sequences required for equality in (4).

### Auxiliary construction lemma

Let \(r\ge1\), \(1\le s\le r\), and \(q\ge r+s\). Let \(A_0,B_0\) be disjoint \(q\)-element sets, with distinguished subsets
\[
Y\subseteq A_0,\qquad X\subseteq B_0,\qquad |X|=|Y|=s.
\]
There is a bipartite graph \(J\) on \(A_0\cup B_0\) such that

- vertices of \(X\cup Y\) have degree \(r\);
- every other vertex has degree \(r+1\);
- there is no edge between \(X\) and \(Y\).

#### Proof

We first construct an \(r\)-regular bipartite graph \(F\) avoiding \(X\)-\(Y\) edges, together with a perfect matching \(M\) between \(A_0\setminus Y\) and \(B_0\setminus X\), disjoint from \(F\).

For the base case \(q=r+s\), write
\[
A_0=Y\dot\cup A_1,\qquad
B_0=X\dot\cup B_1,
\]
where \(|A_1|=|B_1|=r\). Put into \(F\):

- all edges between \(Y\) and \(B_1\);
- all edges between \(A_1\) and \(X\);
- an \((r-s)\)-regular bipartite graph between \(A_1\) and \(B_1\), disjoint from a fixed perfect matching \(M\).

Such an \((r-s)\)-regular graph exists because \(K_{r,r}-M\) is \((r-1)\)-regular and decomposes into perfect matchings. Every vertex has degree \(r\) in \(F\).

To pass from \(q\) to \(q+1\), add new vertices \(a^\ast,b^\ast\). An \(r\)-regular bipartite graph has a perfect matching, so choose \(r\) independent edges
\[
a_i b_i,\qquad 1\le i\le r,
\]
of \(F\). Delete these edges and add
\[
a^\ast b_i,\qquad a_i b^\ast,\qquad 1\le i\le r.
\]
The new graph is again \(r\)-regular, avoids \(X\)-\(Y\) edges, and remains disjoint from the enlarged matching
\[
M\cup\{a^\ast b^\ast\}.
\]
This proves the assertion for all \(q\ge r+s\).

Finally set \(J=F\cup M\). The matching raises the degree of every vertex outside \(X\cup Y\) by one and does not meet \(X\cup Y\). \(\square\)

### Applying the lemma

Write
\[
k=q\ell+s,\qquad 1\le s<\ell,
\]
and suppose
\[
q\ge\ell+s-1.
\]
Apply the auxiliary lemma with \(r=\ell-1\). Thus \(J\) has degree \(\ell-1\) on \(X\cup Y\), degree \(\ell\) elsewhere, and no \(X\)-\(Y\) edges.

Add two new vertices \(x,y\), placing \(x\) on the \(A\)-side and \(y\) on the \(B\)-side, and add all edges
\[
xX,\qquad yY.
\]
The resulting bipartite graph has:

- \(2q\) vertices of degree \(\ell\);
- two vertices \(x,y\) of degree \(s\);
- no edge between \(N(x)=X\) and \(N(y)=Y\).

Now perform one of the following surgeries.

#### Case \(2s<\ell\)

Identify \(x\) and \(y\) into one vertex \(z\). Then
\[
d(z)=2s.
\]
No triangle is created, since a triangle through \(z\) would require an edge between \(X\) and \(Y\). The degree sequence is
\[
(\ell^{\,2q},2s),
\]
which is exactly the degree sequence prescribed by \(2k=2q\ell+2s\).

#### Case \(2s=\ell\)

Again identify \(x\) and \(y\). The new vertex has degree \(\ell\), yielding an \(\ell\)-regular triangle-free graph on \(2q+1\) vertices.

#### Case \(2s>\ell\)

Choose \(Y_0\subseteq Y\) with
\[
|Y_0|=\ell-s.
\]
Delete \(x,y\), and introduce vertices \(u,v\) with
\[
N(u)=X\cup Y_0,\qquad
N(v)=Y\setminus Y_0.
\]
Then
\[
d(u)=\ell,\qquad d(v)=2s-\ell.
\]
Again the graph is triangle-free: \(N(u)\) is independent because there are no \(X\)-\(Y\) edges, while \(N(v)\) lies in one side of the original bipartition.

Thus in all cases we obtain a triangle-free graph whose degree sequence is precisely
\[
(\ell^Q,R),
\]
where \(2k=Q\ell+R\). It therefore has \(U_\ell(k)\) happy triples.

If \(s=0\) and \(q\ge\ell\), simply take an \(\ell\)-regular bipartite graph with \(q\) vertices in each part; for example, label both parts by \(\mathbb Z_q\) and join \(i\) to
\[
i,i+1,\ldots,i+\ell-1.
\]
This completes the proof of parts 2 and 3 of the theorem.

Since \(s\le\ell-1\), the condition
\[
q\ge2\ell-2
\]
implies \(q\ge\ell+s-1\). Hence \(k\ge2\ell(\ell-1)\) is sufficient for equality in (4).

---

## 5. The divisible case

Let \(k=q\ell\).

If \(q\le\ell\), then \(k\le\ell^2\), and (3) gives
\[
M(k,\ell)
=
q\binom{\ell}{2}+\ell\binom q2
=
\frac{q\ell}{2}(\ell+q-2).
\]
The extremal graph is \(K_{q,\ell}\).

If \(q\ge\ell\), take an \(\ell\)-regular bipartite graph with \(q\) vertices in each part. It has
\[
q\ell=k
\]
edges and
\[
2q\binom{\ell}{2}=k(\ell-1)
\]
happy triples, matching (11).

This proves (8). In particular, the example mentioned on the catalog page is completely resolved:

> If \(\ell=3\) and \(k=3t\) with \(t\ge3\), then
> \[
> M(3t,3)=6t.
> \]
> An extremal graph is any cubic bipartite graph on \(t+t\) vertices, for example the cyclic graph joining \(i\) to \(i,i+1,i+2\pmod t\).

Unlike \(K_{t,3}\), this graph really has maximum degree \(3\).

---

## 6. Complete solution for \(\ell\le3\)

For \(\ell=1\), every graph is a matching, so
\[
M(k,1)=0.
\]

For \(\ell=2\) and \(k\ge5\), (11) gives \(M(k,2)\le k\), while the cycle \(C_k\) has exactly \(k\) happy triples. Hence
\[
M(k,2)=k.
\]

For \(\ell=3\), the whole requested range \(k>6\) is determined:

\[
\boxed{
M(k,3)=
\begin{cases}
11,&k=7,\\
14,&k=8,\\
2k,&k\ge9\text{ and }3\mid k,\\
2k-1,&k\ge9\text{ and }3\nmid k.
\end{cases}}
\tag{16}
\]

The values at \(k=7,8\) follow from (3).

For \(k\ge9\), the upper bound is (2). It remains only to give constructions.

- If \(k=3t\), use a cubic bipartite graph on \(t+t\) vertices.

- If \(k=3t+1\), where \(t\ge3\), start with the cycle
  \[
  C_{2t+1}=0,1,\ldots,2t,0
  \]
  and add the matching
  \[
  \{\,i(i+t):1\le i\le t\,\}.
  \]
  Every vertex except \(0\) has degree \(3\), while \(0\) has degree \(2\). The graph is triangle-free: the added edges form a matching, and each joins vertices at cyclic distance at least \(3\). Thus it has
  \[
  2t\binom32+\binom22=6t+1=2k-1
  \]
  happy triples.

- If \(k=3t+2\), add a new leaf adjacent to \(0\) in the preceding construction. The resulting degree sequence is
  \[
  (3^{2t+1},1),
  \]
  and it has \(6t+3=2k-1\) happy triples.

---

## 7. One exact value in the remaining transition window

The degree upper bound need not always be attained immediately above \(\ell^2\). For example,
\[
\boxed{M(18,4)=51.}
\tag{17}
\]

Indeed, \(U_4(18)=54\). Equality would require a triangle-free \(4\)-regular graph on nine vertices.

More strongly, every \(4\)-regular graph on nine vertices has at least two triangles.

- If it were triangle-free, choose \(v\), put \(A=N(v)\) and let \(B\) be the remaining four vertices. Then \(A\) is independent and \(e(A,B)=12\), so \(e(B)=2\). For every edge \(xy\in E(B)\), triangle-freeness gives
  \[
  d_A(x)+d_A(y)\le4,
  \]
  hence
  \[
  d_B(x)+d_B(y)\ge4.
  \]
  This is impossible in a four-vertex graph with only two edges.

- Suppose there were exactly one triangle \(abc\). Each of \(a,b,c\) has two neighbors outside the triangle. No outside vertex can have two neighbors in \(\{a,b,c\}\), so the six outside vertices each have exactly one such neighbor. Their induced graph is therefore cubic and triangle-free on six vertices, hence is \(K_{3,3}\). For each of \(a,b,c\), its two outside neighbors must be nonadjacent and hence lie in the same side of this \(K_{3,3}\). But the three resulting disjoint pairs cannot partition two odd-sized parts of size three. Contradiction.

Thus a \(4\)-regular nine-vertex graph has
\[
h(G)=54-2t(G)\le50.
\]
If the degree sequence is not \(4^9\), convexity shows
\[
\sum_v\binom{d(v)}2\le
8\binom42+\binom32=51.
\]
Therefore \(M(18,4)\le51\).

For equality, take \(K_{4,4}\), subdivide one edge, and attach a leaf to the subdivision vertex. The resulting triangle-free graph has degree sequence
\[
(4^8,3,1)
\]
and hence exactly
\[
8\binom42+\binom32=51
\]
happy triples.

---

## 8. What remains open

For \(\ell\ge4\), the arguments above leave only a transition region. Writing
\[
k=q\ell+s,\qquad 0\le s<\ell,
\]
the potentially unresolved pairs satisfy
\[
\ell^2<k<2\ell(\ell-1),\qquad
s>0,\qquad
q<\ell+s-1,
\tag{18}
\]
apart from sporadic values such as \((18,4)\) settled above.

The universal upper bound there is \(U_\ell(k)\). It is attained exactly when there exists a triangle-free graph with positive degree sequence
\[
(\ell^Q,R),\qquad 2k=Q\ell+R.
\]
When no such realization exists, one must balance a loss in the convex degree sum against the triangle penalty in (9); this is the remaining difficulty.

For completely reproducible finite checks, \(M(k,\ell)\) is the optimum of the following binary integer program on \(n=2k\) vertices. Use edge variables \(x_{ij}\) and triple variables \(y_{abc}\):
\[
\sum_{i<j}x_{ij}=k,
\]
\[
\sum_{j\ne i}x_{\min\{i,j\},\max\{i,j\}}\le\ell
\quad\text{for every }i,
\]
\[
2y_{abc}\le x_{ab}+x_{ac}+x_{bc}
\quad\text{for every }a<b<c,
\]
and maximize
\[
\sum_{a<b<c}y_{abc}.
\]
Every graph with \(k\) edges has at most \(2k\) non-isolated vertices and can be padded with isolated vertices, so this formulation is exact.

I have not independently verified whether the elementary extensions above have appeared after the source paper; the mathematical claims here are proved directly, but they do not settle the entire two-parameter problem.