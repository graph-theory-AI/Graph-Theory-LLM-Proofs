```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A complete-crossing block construction improves the general large-k lower-bound constant to 1/(2√2), leaving only a factor-two gap, and the k=1 case is settled exactly.",
  "would_publish": false,
  "caveats": "The general leading constant remains undetermined, and the literature novelty of the elementary improved bound has not been independently verified."
}
```

# Mathematical writeup

## 1. Formulation

Let \(\tau_k(n)\) denote the minimum number of \(k\)-planar straight-line subgraphs whose edge sets partition the edges of the complete geometric graph on \(n\) points in convex position. Here an edge is \(k\)-planar if it is crossed by at most \(k\) other edges of the same subgraph. Crossings are counted pairwise, as usual.

Because two chords of a convex polygon cross exactly when their endpoints alternate, \(\tau_k(n)\) depends only on \(n\), not on the particular convex point set.

I prove two partial results:

1. A general lower bound
   \[
   \tau_k(n)\ge
   \max_{a,b\ge1}
   \left\lceil
      \frac{ab\left\lfloor n/(a+b)\right\rfloor}
           {\max\{ab,2k\}}
   \right\rceil.
   \tag{1}
   \]
   Consequently,
   \[
   \tau_k(n)\ge
   \left(\frac{1}{2\sqrt2}-o(1)\right)\frac{n}{\sqrt{k}}
   \tag{2}
   \]
   as \(k\to\infty\) and \(n/\sqrt{k}\to\infty\). Compared with the quoted upper bound
   \[
   \tau_k(n)\le
   \left(\frac{1}{\sqrt2}+o(1)\right)\frac{n}{\sqrt{k}},
   \]
   this reduces the asymptotic multiplicative gap to \(2\).

2. For \(k=1\),
   \[
   \tau_1(n)=\left\lceil\frac n3\right\rceil
   \qquad(n\ge5).
   \tag{3}
   \]
   Thus the upper construction is tight, even without a lower-order error, in this special case.

The general conjecture for \(k\ge2\) remains unresolved.

---

## 2. A complete-crossing block lower bound

### Theorem 1

For all positive integers \(n,k,a,b\),
\[
\tau_k(n)\ge
\left\lceil
\frac{ab\left\lfloor n/(a+b)\right\rfloor}
     {\max\{ab,2k\}}
\right\rceil.
\]

### Proof

Set
\[
t=\left\lfloor\frac{n}{a+b}\right\rfloor.
\]
Choose \(t(a+b)\) vertices and divide them into cyclically consecutive blocks, in the order
\[
A_1,A_2,\ldots,A_t,B_1,B_2,\ldots,B_t,
\]
where \(|A_i|=a\) and \(|B_i|=b\).

For each \(i\), let
\[
\mathcal B_i=\{uv:u\in A_i,\ v\in B_i\}.
\]
Thus \(|\mathcal B_i|=ab\).

If \(i<j\), then the endpoints of any edge of \(\mathcal B_i\) and any edge of \(\mathcal B_j\) occur in the cyclic order
\[
A_i,\ A_j,\ B_i,\ B_j.
\]
They therefore alternate. Hence:

\[
\text{Every edge of }\mathcal B_i\text{ crosses every edge of }\mathcal B_j
\quad(i\ne j).
\tag{4}
\]

Consider one \(k\)-planar part \(H\) of a partition. Put
\[
x_i=|E(H)\cap\mathcal B_i|,
\qquad
S=\sum_{i=1}^t x_i,
\]
and let \(h\) be the number of indices with \(x_i>0\).

If \(h=1\), then plainly
\[
S\le ab.
\]

Suppose \(h\ge2\). For every occupied bundle \(i\), choose an edge
\(e_i\in E(H)\cap\mathcal B_i\). By (4), \(e_i\) crosses all the
\(S-x_i\) selected edges lying in the other bundles. Since \(H\) is
\(k\)-planar,
\[
S-x_i\le k
\qquad\text{for every occupied }i.
\]
Summing these \(h\) inequalities gives
\[
(h-1)S\le hk.
\]
Therefore
\[
S\le \frac{h}{h-1}k\le2k.
\]

Thus every color class contains at most
\[
\max\{ab,2k\}
\]
edges from \(\bigcup_i\mathcal B_i\). There are \(tab\) such edges in
total, so any partition into \(q\) classes satisfies
\[
q\max\{ab,2k\}\ge tab.
\]
This proves (1). \(\square\)

### Asymptotic consequence

Define
\[
s_k=\min\{a+b:a,b\in\mathbb N,\ ab\ge2k\}.
\]
Taking a minimizing pair in Theorem 1 gives
\[
\tau_k(n)\ge \left\lfloor\frac{n}{s_k}\right\rfloor.
\tag{5}
\]

By AM–GM,
\[
s_k\ge2\sqrt{2k}.
\]
Conversely, taking
\[
a=b=\left\lceil\sqrt{2k}\right\rceil
\]
shows
\[
s_k\le2\sqrt{2k}+2.
\]
Hence
\[
\tau_k(n)\ge
\frac{n}{2\sqrt{2k}+2}-1.
\tag{6}
\]

In particular,
\[
\tau_k(n)\ge
\left(\frac{1}{2\sqrt2}-o(1)\right)\frac n{\sqrt{k}}
\]
when \(k\to\infty\) and \(n/\sqrt{k}\to\infty\).

The quoted lower bound has asymptotic coefficient \(1/4.93\), whereas
(2) has coefficient
\[
\frac1{2\sqrt2}\approx0.35355.
\]
The quoted upper coefficient is \(1/\sqrt2\approx0.70711\), so this argument leaves precisely a factor-two gap at the level of large-\(k\) constants.

For \(k=2\), Theorem 1 only gives \(\tau_2(n)\ge\lfloor n/4\rfloor\), so the specialized \(3n/10\) lower bound mentioned by the source is stronger in that case.

---

## 3. Exact resolution for \(k=1\)

### Theorem 2

For every \(n\ge5\),
\[
\tau_1(n)=\left\lceil\frac n3\right\rceil.
\]

The proof has an upper and a lower part.

### 3.1 Upper bound by direction classes

Label the vertices cyclically by \(v_0,\ldots,v_{n-1}\). For an edge
\(v_iv_j\), define its direction
\[
d(v_iv_j)=i+j\pmod n.
\]
Let \(D_r\) be the set of edges of direction \(r\).

I claim that the union of any three consecutive direction classes
\[
D_r\cup D_{r+1}\cup D_{r+2}
\tag{7}
\]
is \(1\)-planar.

Indeed, suppose that \(v_iv_j\) and \(v_pv_q\) cross, with integer
representatives ordered as
\[
i<p<j<q<i+n.
\]
Then
\[
d(v_pv_q)-d(v_iv_j)
 \equiv (p-i)+(q-j)\pmod n.
\]
Put
\[
\delta=(p-i)+(q-j).
\]
Both summands are positive, and
\[
n-\delta=(j-p)+(n-q+i)
\]
is also the sum of two positive integers. Hence
\[
2\le\delta\le n-2.
\tag{8}
\]
Thus crossing edges never have equal or consecutive directions.

Within three consecutive direction classes, crossings can therefore
occur only between the two extreme classes. Moreover, if
\(\delta=2\), then necessarily
\[
p=i+1,\qquad q=j+1,
\]
so for a fixed edge there is at most one crossing edge whose direction
is two larger. The analogous assertion holds for direction difference
\(-2\). Consequently every edge in (7) has at most one crossing.

Partition the \(n\) direction classes into consecutive groups of size at
most three. This gives
\[
\tau_1(n)\le\left\lceil\frac n3\right\rceil.
\tag{9}
\]

### 3.2 Density bound for convex \(1\)-planar graphs

We need the following self-contained extremal lemma.

#### Lemma 3

A straight-line \(1\)-planar graph on \(n\) vertices in convex position has at most
\[
\frac{5n}{2}-4
\tag{10}
\]
edges.

#### Proof

Add all \(n\) hull edges; this preserves \(1\)-planarity. Let \(H\) be
the subgraph consisting of all uncrossed edges. It is an outerplane
graph containing the hull cycle.

Every crossed edge has exactly one crossing mate, so the crossed edges
split into \(c\) pairs, with two edges in each pair. Each pair lies
inside a single bounded face of \(H\).

We first establish a face bound. Suppose a face has boundary length
\(\ell\), and contains \(c_F\) crossing pairs. No chord belonging to one
pair crosses a chord belonging to another pair. Then
\[
c_F\le\frac{\ell-2}{2}.
\tag{11}
\]

To see this, choose one crossing pair. Its two chords divide the face
into four sectors. Every remaining crossing pair must lie wholly in one
of these sectors; otherwise one of its chords would cross a chosen
chord. If the four open boundary arcs contain respectively
\(q_1,\ldots,q_4\) other boundary vertices, then
\[
q_1+\cdots+q_4=\ell-4.
\]
Induction applied in the four sectors gives
\[
c_F
 \le 1+\frac{q_1+\cdots+q_4}{2}
 =\frac{\ell-2}{2}.
\]

Let \(f\) be the number of bounded faces of \(H\), and for a bounded face
\(F\) let
\[
d_F=\ell_F-2.
\]
The standard outerplane identities give
\[
|E(H)|=n+f-1
\tag{12}
\]
and
\[
\sum_F d_F=n-2.
\tag{13}
\]

If \(c_F=0\), then
\[
1+2c_F=1\le\frac32d_F.
\]
If \(c_F>0\), then \(\ell_F\ge4\), so \(d_F\ge2\), and by (11),
\[
1+2c_F\le1+d_F\le\frac32d_F.
\]
Summing over the bounded faces,
\[
f+2c
 =\sum_F(1+2c_F)
 \le\frac32\sum_F d_F
 =\frac32(n-2).
\tag{14}
\]

There are \(2c\) crossed edges. Hence, using (12) and (14),
\[
|E(G)|
 =|E(H)|+2c
 =n+f-1+2c
 \le n-1+\frac32(n-2)
 =\frac{5n}{2}-4.
\]
This proves the lemma. \(\square\)

### 3.3 Applying the density bound to a partition

A convex \(1\)-planar graph contains at most
\[
\frac{3n}{2}-4
\tag{15}
\]
diagonals: add all \(n\) hull edges and apply Lemma 3.

The complete convex graph has
\[
\binom n2-n=\frac{n(n-3)}2
\]
diagonals. If these are partitioned into \(q\) \(1\)-planar graphs,
then
\[
q\left(\frac{3n}{2}-4\right)
 \ge \frac{n(n-3)}2,
\]
and therefore
\[
q\ge \frac{n(n-3)}{3n-8}.
\tag{16}
\]

For \(n\ge5\), the right side of (16) is strictly larger than
\(\lceil n/3\rceil-1\). This can be checked by writing \(n\) modulo
three:
\[
n(n-3)-\left(\left\lceil\frac n3\right\rceil-1\right)(3n-8)
=
\begin{cases}
8(m-1),&n=3m,\\
2(m-1),&n=3m+1,\\
5m-2,&n=3m+2,
\end{cases}
\]
which is positive in the relevant ranges \(n\ge5\). Since \(q\) is an
integer,
\[
q\ge\left\lceil\frac n3\right\rceil.
\]
Together with (9), this proves Theorem 2.

For completeness, \(\tau_1(4)=1\), since the whole convex \(K_4\) is
\(1\)-planar.

---

## 4. Remaining gap

The complete-crossing block argument gives
\[
\left(\frac{1}{2\sqrt2}-o(1)\right)\frac n{\sqrt{k}}
\le \tau_k(n)
\le
\left(\frac{1}{\sqrt2}+o(1)\right)\frac n{\sqrt{k}}.
\]
Thus it reduces the quoted general constant-factor gap to \(2\), but it
does not determine whether the upper coefficient \(1/\sqrt2\) is
correct. Nor does it provide an improved upper construction or a
counterexample to the proposed tightness.

The general \(k\ge2\) question therefore remains open.