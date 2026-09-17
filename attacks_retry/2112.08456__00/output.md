```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained bound gives tau_k(n) = n/sqrt(2k) + O(n/k + 1), settling the large-k leading constant but not fixed-k tightness.",
  "would_publish": false,
  "caveats": "The exact leading coefficient for each fixed k remains undetermined; literature novelty has not been independently checked."
}
```

# A matching large-\(k\) asymptotic

Let \(\tau_k(n)\) be the minimum number of \(k\)-planar subgraphs partitioning the complete straight-line graph on \(n\) points in convex position. Crossings are counted pairwise: each edge may cross at most \(k\) other edges in its own part.

I prove the following bounds, with absolute constants:
\[
\boxed{
\frac{n}{8+\sqrt{2k+64}}-13
\;\le\;
\tau_k(n)
\;\le\;
\frac{n}{\sqrt{2k}}+1
}
\qquad(n\ge3,\ k\ge1).
\tag{1}
\]
In particular,
\[
\boxed{
\tau_k(n)=\frac{n}{\sqrt{2k}}
+O\!\left(\frac{n}{k}+1\right).
}
\tag{2}
\]
Consequently, whenever \(k\to\infty\) and \(\sqrt{k}=o(n)\),
\[
\tau_k(n)
=
\left(\frac1{\sqrt2}+o(1)\right)\frac{n}{\sqrt{k}}.
\tag{3}
\]

Thus the catalog’s large-\(k\) leading constant \(1/\sqrt2\) is optimal. This does **not** establish that the exact direction-class bound is asymptotically optimal in \(n\) for every fixed \(k\), so I retain the verdict “partial.”

The new ingredient is an edge-ordering bound for two-layer drawings. The previous attempt’s \(k=1\) extremal lemma is not used. The direction-class upper construction is checked independently below.

---

## 1. A density bound for two-layer \(k\)-planar graphs

A **two-layer drawing** has two ordered vertex classes; two edges with distinct endpoints cross exactly when their endpoint orders are reversed. Straight chords between two disjoint boundary arcs of a convex polygon have this crossing relation, after reversing one of the orders.

### Lemma 1
Every simple two-layer \(k\)-planar graph on \(N\) vertices has at most
\[
B_kN
\quad\text{edges},\qquad
B_k:=4+\sqrt{16+\frac{k}{2}}.
\tag{4}
\]

### Proof

We first establish two inequalities for any such graph with \(M>0\) edges. Write \(d_v\) for its vertex degrees, and put
\[
T:=\sum_{uv\in E}d_ud_v,
\qquad
S:=\sum_v d_v^2.
\]

#### Edge orders and displacement

Order the edges in two ways:

- first by their left endpoint, breaking ties by the right endpoint;
- first by their right endpoint, breaking ties by the left endpoint.

Use the specified vertex orders in both cases. Let \(p(e)\) and \(q(e)\) be the positions of \(e\) in these two edge orders.

Two edges disagree in the two orders exactly when they cross. Edges sharing an endpoint agree, by the tie-breaking conventions. For any two total orders,
\[
|p(e)-q(e)|
\le
\#\{\text{elements whose relative order with }e\text{ changes}\}.
\]
Hence \(k\)-planarity gives
\[
|p(e)-q(e)|\le k.
\tag{5}
\]

Partition \([0,M]\) into intervals \(I_u\), one for each left vertex, of lengths \(d_u\), in the first edge order. Similarly, partition \([0,M]\) into intervals \(J_v\), of lengths \(d_v\), in the second order.

For every edge \(uv\), mark the rectangle \(I_u\times J_v\). These rectangles have disjoint interiors, because the graph is simple. Their union \(U\) therefore has area
\[
\operatorname{area}(U)=T.
\]

The rank point
\[
\bigl(p(uv)-\tfrac12,q(uv)-\tfrac12\bigr)
\]
lies in \(I_u\times J_v\). Thus every \((x,y)\) in that rectangle satisfies
\[
|x-y|\le k+d_u+d_v.
\tag{6}
\]

The central band \(\{|x-y|\le k\}\cap[0,M]^2\) has area at most \(2kM\).

Outside that band, set \(\delta=|x-y|-k>0\). By (6), either
\[
\delta\le2d_u
\qquad\text{or}\qquad
\delta\le2d_v.
\]
For fixed \(x\in I_u\), the first condition permits a set of \(y\)-values of total length at most \(4d_u\). Its total area is therefore at most
\[
4\sum_{\text{left }u}d_u^2.
\]
The second condition contributes at most
\[
4\sum_{\text{right }v}d_v^2.
\]
Consequently,
\[
T\le2kM+4S.
\tag{7}
\]

#### A degree-product inequality

AM–GM, followed by convexity of \(x\log x\), gives
\[
\begin{aligned}
\frac{T}{M}
&\ge
\exp\!\left(
\frac1M\sum_{uv\in E}\log(d_ud_v)
\right)\\
&=
\exp\!\left(
\frac1M\sum_v d_v\log d_v
\right)\\
&\ge
\left(\frac{2M}{N}\right)^2.
\end{aligned}
\]
Thus
\[
T\ge \frac{4M^3}{N^2}.
\tag{8}
\]
Zero degrees may be included using \(0\log0=0\).

#### Passing to a densest subgraph

Choose a nonempty subgraph maximizing its edge-to-vertex ratio, and apply (7)–(8) to it. Continue to write \(M,N\) for its parameters and set
\[
\rho=\frac MN.
\]
Every vertex has degree at least \(\rho\): deleting a vertex of smaller degree would increase the ratio.

If \(\rho\le8\), then \(\rho\le B_k\). Otherwise,
\[
S
=\sum_{uv\in E}(d_u+d_v)
\le \frac2\rho\sum_{uv\in E}d_ud_v
=\frac{2T}{\rho}.
\]
Together with (7),
\[
\left(1-\frac8\rho\right)T\le2kM.
\]
Since \(\rho>8\), we may use (8) to obtain
\[
4\rho^2\left(1-\frac8\rho\right)\le2k.
\]
Equivalently,
\[
\rho^2-8\rho\le\frac{k}{2},
\]
and hence
\[
\rho\le4+\sqrt{16+\frac{k}{2}}=B_k.
\]

The original graph has no larger edge-to-vertex ratio. This proves the lemma. \(\square\)

The important feature is
\[
B_k=\sqrt{\frac{k}{2}}+O(1),
\tag{9}
\]
rather than merely an unspecified constant times \(\sqrt{k}\).

---

## 2. Long edges localize after two crossing deletions

Let \(n=2m\). The **cyclic length** of an edge is the smaller number of polygon sides on the two boundary arcs between its endpoints.

For an integer \(t\) with
\[
0\le t<\frac m3,
\]
call an edge **long** if its cyclic length is at least \(m-t\).

### Lemma 2
A \(k\)-planar subgraph contains at most
\[
2k+(2t+2)B_k
\tag{10}
\]
long edges.

### Proof

Let \(F\) be its set of long edges. The assertion is immediate if \(F\) is empty.

Choose \(e\in F\) of minimum cyclic length, say
\[
\ell(e)=m-d,\qquad 0\le d\le t.
\]
Delete from \(F\) all edges crossing \(e\), at most \(k\) edges.

Every remaining edge lies in the closed longer boundary arc between the endpoints of \(e\), whose length is \(m+d\). Indeed:

- an edge joining the interiors of the two arcs would cross \(e\);
- an edge other than \(e\) lying entirely in the shorter arc would have cyclic length less than \(m-d\), contradicting the choice of \(e\).

Index the vertices of the longer arc by
\[
0,1,\ldots,a,\qquad a=m+d.
\]
For a remaining edge with endpoints \(i<j\), put
\[
x=i,\qquad y=a-j.
\]
Its cyclic length is at least \(m-d\), so \(j-i\ge m-d\). Therefore
\[
x+y=a-(j-i)\le2d.
\tag{11}
\]

All these edges join two disjoint endpoint blocks: \(x\le2d\) at one end and \(y\le2d\) at the other. The blocks are disjoint because
\[
3d<m.
\]
For two such edges, crossing is equivalent to reversal of the \(x\)- and \(y\)-orders.

Choose a remaining edge \(f\) maximizing \(x_f+y_f\), and delete all remaining edges crossing \(f\), again at most \(k\) edges.

Every edge \(g\) now satisfies
\[
x_g\le x_f,\qquad y_g\le y_f.
\tag{12}
\]
To see this, if one coordinate were larger and the other smaller, \(g\) would cross \(f\). If one were larger and the other at least as large, then \(x_g+y_g>x_f+y_f\), contrary to maximality.

Thus all edges left after the two deletions form a two-layer \(k\)-planar graph supported on at most
\[
(x_f+1)+(y_f+1)\le2d+2\le2t+2
\]
vertices. Lemma 1 bounds their number by \((2t+2)B_k\). Restoring the at most \(2k\) deleted edges proves (10). \(\square\)

---

## 3. Counting long edges gives the lower bound

In the complete convex graph on \(n=2m\) vertices, there are \(n\) edges of each cyclic length \(1,\ldots,m-1\), and \(n/2\) edges of cyclic length \(m\).

Therefore the number of long edges is
\[
nt+\frac n2=n\left(t+\frac12\right).
\]
Applying Lemma 2 to every part of a partition gives the finite bound
\[
\boxed{
\tau_k(n)\ge
\left\lceil
\frac{n(t+\tfrac12)}
     {2k+(2t+2)B_k}
\right\rceil
}
\qquad
\left(n=2m,\ 0\le t<\frac m3\right).
\tag{13}
\]

Choose
\[
t=\left\lfloor\frac{m-1}{3}\right\rfloor.
\]
Then
\[
t+\frac12\ge\frac n{12}.
\]
Writing \(B=B_k\), equation (13) consequently implies
\[
\tau_k(n)
\ge
\frac{n}
{2B+\dfrac{B+2k}{t+1/2}}
\ge
\frac{n}{2B+\dfrac{12(B+2k)}n}.
\]
Using \(1/(a+x)\ge1/a-x/a^2\),
\[
\tau_k(n)
\ge
\frac{n}{2B}
-\frac{3(B+2k)}{B^2}.
\tag{14}
\]

The defining equation for \(B\) is
\[
B^2-8B=\frac{k}{2}.
\]
Hence
\[
\frac{3(B+2k)}{B^2}
=
12-\frac{93}{B}
<12.
\]
For even \(n\),
\[
\tau_k(n)\ge\frac{n}{2B_k}-12.
\tag{15}
\]

For odd \(n\), restriction to \(n-1\) vertices gives
\[
\tau_k(n)\ge\tau_k(n-1)
\ge\frac{n-1}{2B_k}-12
\ge\frac{n}{2B_k}-13.
\]
The smallest values, if needed, satisfy this negative lower bound trivially. Since
\[
2B_k=8+\sqrt{2k+64},
\]
this establishes the lower half of (1).

---

## 4. Rechecking the upper construction

Label the vertices cyclically by \(0,\ldots,n-1\), and assign edge \(ij\) the direction
\[
i+j\pmod n.
\]
Let \(D_r\) consist of all edges of direction \(r\).

For two crossing edges, choose integer representatives
\[
i<p<j<q<i+n.
\]
Their direction difference is congruent to
\[
\delta=(p-i)+(q-j).
\]
Both summands are positive, and
\[
n-\delta=(j-p)+(i+n-q)
\]
is also a sum of two positive integers. Thus
\[
2\le\delta\le n-2.
\tag{16}
\]

For a fixed edge, the number of crossing edges whose direction differs by \(d\), in either specified cyclic direction, is at most \(d-1\). For positive difference this follows by counting positive solutions of
\[
(p-i)+(q-j)=d;
\]
for negative difference use the complementary two gaps.

Consider \(h\) consecutive direction classes. An edge in position \(j\), where \(0\le j\le h-1\), consequently has at most
\[
\binom j2+\binom{h-1-j}{2}
\le
\binom{h-1}{2}
\tag{17}
\]
crossings inside their union.

Put
\[
s_k=
\left\lfloor\frac{3+\sqrt{1+8k}}2\right\rfloor.
\]
Then
\[
\binom{s_k-1}{2}\le k.
\]
Partitioning the direction classes into consecutive groups of size at most \(s_k\) therefore gives
\[
\tau_k(n)\le\left\lceil\frac n{s_k}\right\rceil.
\tag{18}
\]
Also \(s_k\ge\sqrt{2k}\), so
\[
\tau_k(n)\le\frac n{\sqrt{2k}}+1.
\]
This proves the upper half of (1).

---

## 5. The asymptotic consequence and the remaining question

For \(a=\sqrt{2k}\),
\[
8+\sqrt{a^2+64}\le a+16.
\]
Thus (1) even yields the explicit, uniform estimate
\[
\frac n{\sqrt{2k}}-\frac{8n}{k}-13
\le
\tau_k(n)
\le
\frac n{\sqrt{2k}}+1.
\tag{19}
\]
This proves (2), and in relative form gives
\[
\frac{\tau_k(n)}{n/\sqrt{2k}}
=
1+O\!\left(\frac1{\sqrt{k}}+\frac{\sqrt{k}}n\right).
\tag{20}
\]

Therefore **no fixed-factor improvement of the coefficient \(1/\sqrt2\) is possible** in the regime \(k\to\infty\), \(\sqrt{k}=o(n)\).

The distinction concerning the original question is important:

- **Large-\(k\) leading constant:** determined by the argument above.
- **Every fixed \(k\), with \(n\to\infty\):** not determined. In that regime the error \(O(n/k)\) is still linear in \(n\), so this does not prove
  \[
  \tau_k(n)=\frac{n}{s_k}+o(n).
  \]

All auxiliary statements used to prove (1)–(2) have been proved here. The remaining mathematical gap is fixed-\(k\) tightness of the more precise upper construction, not the large-\(k\) constant. I have not independently verified whether the new bounds already occur elsewhere in the literature.