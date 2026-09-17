```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with the stronger bound n^2/32 when G has no 5-cycle, and it also holds whenever G has at most n^5/224000 copies of C5.",
  "would_publish": false,
  "caveats": "Self-contained special cases only; no novelty claim, and the unrestricted conjecture is not settled."
}
```

# Partial results via distance-two cuts

For a graph \(G\), write
\[
b(G)=\min\{|F|:G-F\text{ is bipartite}\}.
\]
Equivalently,
\[
b(G)=\min_{V(G)=A\sqcup B}\bigl(e(G[A])+e(G[B])\bigr).
\]
Thus we seek a cut with at most \(n^{2}/25\) uncut edges.

I prove two special cases:

1. If \(G\) has neither a triangle nor a \(5\)-cycle, then
   \[
   \boxed{b(G)\le \frac{n^{2}}{32}.}
   \]
   In particular, the conjecture holds whenever the odd girth is at least \(7\).

2. Let \(t_5(G)\) denote the number of unoriented, unlabelled cycles of length five. If \(G\) is triangle-free and
   \[
   t_5(G)\le \frac{n^{5}}{224000},
   \]
   then
   \[
   \boxed{b(G)\le \frac{n^{2}}{25}.}
   \]

The neighborhood-averaging identity used in the previous attempt is valid and is reproved below. No Clebsch-graph or equality-classification claim from that attempt is needed. The main change is to use distance-two colorings rather than shortest-cycle peeling.

Assume \(n\ge1\); the empty graph is immediate. Put
\[
m=e(G),\qquad Q=\sum_{v\in V(G)}d(v)^2.
\]

## 1. Graphs with no triangles or pentagons

### Theorem 1
If \(G\) has no cycle of length three or five, then
\[
b(G)\le \frac m2-\frac{Q}{2n}
=\frac{n^2}{32}
-\frac1{2n}\sum_v\left(d(v)-\frac n4\right)^2.
\tag{1}
\]

### Proof

Fix a vertex \(v\), and let \(N_2(v)\) be the set of vertices at distance exactly two from \(v\).

Both \(N(v)\) and \(N_2(v)\) are independent. The first assertion follows from triangle-freeness. For the second, suppose \(xy\) is an edge with \(x,y\in N_2(v)\). Choose
\[
a\in N(v)\cap N(x),\qquad b\in N(v)\cap N(y).
\]
If \(a=b\), then \(a,x,y\) form a triangle. Otherwise
\[
v,a,x,y,b,v
\]
is a cycle of length five: these five vertices are distinct because \(x,y\notin N(v)\). Both possibilities are forbidden.

Consequently, the subgraph induced by
\[
\{v\}\cup N(v)\cup N_2(v)
\]
is bipartite, with parts
\[
N(v)\quad\text{and}\quad \{v\}\cup N_2(v).
\]
Its number of edges is exactly
\[
h_v:=\sum_{u\in N(v)}d(u),
\]
since every neighbor of a vertex in \(N(v)\) lies in this distance-two ball.

Color this ball according to its bipartition. Color every remaining vertex independently and uniformly with the two colors. All \(h_v\) edges inside the ball cross the resulting cut; every other edge is uncut with probability \(1/2\). Hence
\[
b(G)\le \frac{m-h_v}{2}.
\]

Averaging over \(v\), and observing that
\[
\sum_v h_v
=\sum_v\sum_{u\in N(v)}d(u)
=\sum_u d(u)^2
=Q,
\]
gives
\[
b(G)\le \frac m2-\frac{Q}{2n}.
\]
Finally,
\[
\sum_v\left(d(v)-\frac n4\right)^2
=Q-nm+\frac{n^3}{16},
\]
which proves (1). \(\square\)

This establishes the conjecture throughout the pentagon-free case. The constant \(1/32\) is not asserted to be sharp for that class.

## 2. A quantitative extension allowing pentagons

The obstruction to the preceding proof is an edge inside a second neighborhood. We can control such edges using common-neighbor counts, rather than merely counting their presence.

### Lemma 2
For every triangle-free graph \(G\) on \(n\ge1\) vertices and every real \(K>0\),
\[
\boxed{
b(G)\le
\frac m2-\frac{Q}{2n}
+\frac{K}{8n}\bigl(n(n-1)-2m\bigr)
+\frac{5t_5(G)}{2nK^2}.
}
\tag{2}
\]

### Proof

Fix \(v\), and put
\[
W_v=V(G)\setminus\bigl(N(v)\cup\{v\}\bigr).
\]
For \(x\in W_v\), define
\[
c_v(x)=|N(v)\cap N(x)|.
\]
Triangle-freeness gives
\[
h_v:=\sum_{u\in N(v)}d(u)
=d(v)+\sum_{x\in W_v}c_v(x).
\tag{3}
\]

Let \(t_5(v)\) be the number of pentagons containing \(v\). We have the exact identity
\[
t_5(v)
=\sum_{xy\in E(G[W_v])}c_v(x)c_v(y).
\tag{4}
\]
Indeed, for each edge \(xy\) in \(W_v\), choose
\[
a\in N(v)\cap N(x),\qquad b\in N(v)\cap N(y).
\]
The vertices \(a,b\) must be distinct, since otherwise \(a,x,y\) form a triangle. These choices therefore give the pentagon
\[
v,a,x,y,b,v.
\]
Conversely, every pentagon through \(v\) has a unique edge opposite \(v\), and is counted once in (4).

Now set
\[
p_x=\min\left\{\frac{c_v(x)}K,1\right\}.
\]
Construct a random cut as follows:

- give every vertex in \(N(v)\) color \(0\);
- give \(v\) color \(1\);
- independently give each \(x\in W_v\) color \(1\) with probability
  \[
  \frac{1+p_x}{2}.
  \]

Let \(U_v\) be the number of uncut edges. Since \(N(v)\) is independent and \(v\) has no neighbors in \(W_v\),
\[
\mathbb E U_v
=
\frac m2-\frac{d(v)}2
-\frac12\sum_{x\in W_v}c_v(x)p_x
+\frac12\sum_{xy\in E(G[W_v])}p_xp_y.
\tag{5}
\]
Here an edge from \(N(v)\) to \(x\) is uncut with probability \((1-p_x)/2\), while an edge \(xy\) inside \(W_v\) is uncut with probability \((1+p_xp_y)/2\).

For every \(c\ge0\),
\[
c\min\{c/K,1\}\ge c-\frac K4.
\tag{6}
\]
When \(c\le K\), this is the inequality
\[
\frac{c^2}{K}-c+\frac K4
=\frac{(c-K/2)^2}{K}\ge0;
\]
when \(c\ge K\), it is immediate. Also,
\[
p_xp_y\le \frac{c_v(x)c_v(y)}{K^2}.
\]
Using (3), (4), and (6) in (5), we obtain
\[
b(G)\le \mathbb E U_v
\le
\frac{m-h_v}{2}
+\frac{K|W_v|}{8}
+\frac{t_5(v)}{2K^2}.
\tag{7}
\]

Finally, average over all \(v\). The relevant identities are
\[
\sum_v h_v=Q,\qquad
\sum_v |W_v|=n(n-1)-2m,\qquad
\sum_v t_5(v)=5t_5(G).
\]
These give (2). \(\square\)

## 3. An explicit pentagon-density criterion

Set \(K=n/16\) in (2). Then
\[
b(G)\le
\frac{31m}{64}-\frac{Q}{2n}
+\frac{n^2-n}{128}
+\frac{640t_5(G)}{n^3}.
\tag{8}
\]
Completing the square gives the more informative form
\[
\boxed{
b(G)\le
\frac{1217n^2}{32768}-\frac n{128}
-\frac1{2n}\sum_v
 \left(d(v)-\frac{31n}{128}\right)^2
+\frac{640t_5(G)}{n^3}.
}
\tag{9}
\]

In particular, if
\[
t_5(G)\le \frac{n^5}{224000},
\]
then, after dropping the nonpositive degree-variance term,
\[
\begin{aligned}
b(G)
&\le
\left(\frac{1217}{32768}+\frac1{350}\right)n^2
-\frac n{128}\\
&<\frac{n^2}{25}.
\end{aligned}
\]
The last comparison is exact:
\[
\frac1{25}
-\left(\frac{1217}{32768}+\frac1{350}\right)
=\frac{17}{5734400}>0.
\]
This proves the second claimed special case. The numerical constant is not claimed to be optimal.

### Constructive aspect

These arguments produce cuts, not just existence bounds.

For Theorem 1, choose a vertex maximizing \(h_v\), properly color its distance-two ball, and assign the remaining colors by conditional expectations.

For (9), use \(K=n/16\), evaluate the expected cost in (5) for each \(v\), select a vertex whose expectation is at most the average bound, and again apply conditional expectations. All probabilities are rational, and the common-neighbor counts can be computed directly. No maximum-cut oracle or unreported computational search is involved.

## 4. What remains unresolved

Any counterexample to the original conjecture would necessarily have
\[
\boxed{t_5(G)>\frac{n^5}{224000}.}
\]
In particular, its odd girth would be exactly five—not merely one of \(5,7,9,11\), as allowed by the previous shortest-cycle argument.

However, this leaves the pentagon-rich regime untreated. It includes the extremal construction: if \(G\) is a balanced blow-up of \(C_5\), with five parts of size \(q\), then \(n=5q\) and
\[
b(G)=q^2=\frac{n^2}{25}.
\]
For completeness, deleting one complete edge class gives the upper bound. Conversely, the \(q^5\) pentagons selecting one vertex from each part must all be hit, and each edge lies in exactly \(q^3\) of these pentagons, forcing at least \(q^2\) deletions. This construction also has at least
\[
q^5=\frac{n^5}{3125}
\]
pentagons, well outside the density hypothesis above.

Thus the argument gives a stronger odd-girth special case and an explicit pentagon-density criterion, but it does **not** prove the unrestricted conjecture or improve the best quoted unconditional bound.