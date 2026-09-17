```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove Ryser's inequality when nonisolated degrees lie in {d,d+1} with d <= r-2, or when maximum vertex degree is at most three and r >= 6.",
  "would_publish": false,
  "caveats": "Only degree-restricted families are treated; novelty has not been checked, and the general conjecture is not resolved."
}
```

# A local-degree bound and two special cases

Throughout, \(H\) is a finite \(r\)-uniform \(r\)-partite hypergraph, with \(r\ge 2\). Write
\[
d(v)=|\{e\in E(H):v\in e\}|
\]
for its vertex degrees. Isolated vertices can be discarded.

The following are the partial results established here.

**Theorem.**
1. If every nonisolated vertex has degree \(d\) or \(d+1\), for some integer \(d\ge1\), then
   \[
   \boxed{\tau(H)\le \frac{rd+1}{d+1}\,\nu(H).}
   \]
   Consequently, Ryser’s inequality holds in this class whenever \(d\le r-2\).

2. If \(H\) has maximum vertex degree at most three, then Ryser’s inequality holds for every \(r\ge6\). For the two preceding values of \(r\), the same argument gives
   \[
   r=4:\quad \tau(H)\le \frac72\nu(H),
   \qquad
   r=5:\quad \tau(H)\le \frac{21}{5}\nu(H).
   \]

In particular, the first assertion proves Ryser’s inequality for \(r\ge4\) when all nonisolated degrees belong to \(\{2,3\}\).

The proof is self-contained and uses a random-ordering matching bound together with a degree-weighted count of the vertices.

## 1. A local certificate for Ryser’s inequality

For an edge \(e\), put
\[
s(e)=\sum_{v\in e}(d(v)-1),
\qquad
w(e)=\sum_{v\in e}\frac1{d(v)}.
\]

**Lemma.** If \(H\) is nonempty, then
\[
\boxed{
\tau(H)\le
\frac1r\max_{e\in E(H)}
\bigl[(s(e)+1)w(e)\bigr]\,\nu(H).
}
\tag{1}
\]

Thus the explicitly checkable condition
\[
(s(e)+1)w(e)\le r(r-1)
\qquad\text{for every }e\in E(H)
\tag{2}
\]
is sufficient for Ryser’s inequality.

**Proof.** Let \(G\) be the edge-intersection graph of \(H\): its vertices are the edges of \(H\), and two vertices are adjacent when the corresponding hyperedges intersect. Independent sets of \(G\) are exactly matchings of \(H\).

For every edge \(e\),
\[
d_G(e)\le \sum_{v\in e}(d(v)-1)=s(e).
\tag{3}
\]
Repeated intersections only make this inequality stronger.

Order the vertices of \(G\) uniformly at random, and select each vertex that precedes all its neighbors. The selected vertices form an independent set, and a vertex \(e\) is selected with probability \(1/(d_G(e)+1)\). Therefore
\[
\nu(H)\ge
\sum_{e\in E(H)}\frac1{d_G(e)+1}
\ge
\sum_{e\in E(H)}\frac1{s(e)+1}.
\tag{4}
\]

On the other hand, if \(n\) is the number of nonisolated vertices of \(H\), then
\[
n
=\sum_{e\in E(H)}\sum_{v\in e}\frac1{d(v)}
=\sum_{e\in E(H)}w(e).
\tag{5}
\]
Each part of \(H\) is a vertex cover, so
\[
\tau(H)\le \min_i|V_i|\le \frac nr.
\tag{6}
\]

Set
\[
K=\frac1r\max_e (s(e)+1)w(e).
\]
Combining (4)–(6) gives
\[
\tau(H)
\le \frac1r\sum_e w(e)
\le K\sum_e\frac1{s(e)+1}
\le K\nu(H),
\]
as required. \(\square\)

The empty hypergraph satisfies all the asserted bounds trivially.

## 2. Two consecutive vertex degrees

Suppose every nonisolated degree belongs to \(\{d,d+1\}\).

For an edge \(e\), let \(b\) be the number of its vertices having degree \(d\). Thus its remaining \(r-b\) vertices have degree \(d+1\). We obtain
\[
w(e)=\frac b d+\frac{r-b}{d+1}
=\frac{rd+b}{d(d+1)}
\]
and
\[
s(e)=b(d-1)+(r-b)d=rd-b.
\]
Consequently,
\[
\begin{aligned}
(s(e)+1)w(e)
&=\frac{(rd+b)(rd-b+1)}{d(d+1)}\\
&=\frac{rd(rd+1)+b-b^2}{d(d+1)}\\
&\le \frac{r(rd+1)}{d+1}.
\end{aligned}
\tag{7}
\]
The last inequality uses the fact that \(b\) is an integer, so \(b-b^2\le0\).

Applying (1) proves
\[
\tau(H)\le \frac{rd+1}{d+1}\nu(H).
\]

Finally,
\[
\frac{rd+1}{d+1}\le r-1
\quad\Longleftrightarrow\quad
d\le r-2.
\]
This proves the first assertion.

Some immediate instances are:
\[
\begin{array}{c|c|c}
\text{allowed nonisolated degrees}&\text{bound}&\text{Ryser follows for}\\
\hline
\{1,2\}&\tau\le \frac{r+1}{2}\nu&r\ge3\\[2mm]
\{2,3\}&\tau\le \frac{2r+1}{3}\nu&r\ge4\\[2mm]
\{r-2,r-1\}&\tau\le (r-1)\nu&r\ge3.
\end{array}
\]

## 3. Maximum vertex degree three

Now allow degrees \(1,2,3\) simultaneously.

For an edge \(e\), let \(a,b,c\) be the numbers of its vertices of degrees \(1,2,3\), respectively. Then
\[
a+b+c=r
\]
and
\[
(s(e)+1)w(e)
=(1+b+2c)\left(a+\frac b2+\frac c3\right).
\tag{8}
\]

We optimize this expression over all such integer triples.

If \(b\ge2\), replacing
\[
(a,b,c)\quad\text{by}\quad(a+1,b-2,c+1)
\]
leaves \(1+b+2c\) unchanged and increases the second factor by \(1/3\). Thus a maximizing numerical pattern can be taken to have \(b=0\) or \(b=1\).

For \(b=0\), define
\[
F_r(c)=\left(r-\frac{2c}{3}\right)(2c+1),
\qquad 0\le c\le r.
\]
For \(b=1\), the expression in (8) is
\[
G_r(c)=\left(r-\frac12-\frac{2c}{3}\right)(2c+2),
\qquad 0\le c\le r-1.
\]
A direct calculation gives
\[
G_r(c)=\frac{F_r(c)+F_r(c+1)}2-\frac c3
\le \max\{F_r(c),F_r(c+1)\}.
\]
Hence (1) yields
\[
\boxed{
\tau(H)\le \beta_r\nu(H),\qquad
\beta_r=
\frac1{3r}
\max_{\substack{0\le c\le r\\c\in\mathbb Z}}
(3r-2c)(2c+1).
}
\tag{9}
\]
This is the optimized constant from the local certificate; it is not asserted to be the optimal matching-cover ratio for this class.

Completing the square,
\[
(3r-2c)(2c+1)
=
\frac{(3r+1)^2}{4}
-4\left(c-\frac{3r-1}{4}\right)^2.
\tag{10}
\]
Thus
\[
\beta_r\le \frac{(3r+1)^2}{12r}.
\tag{11}
\]
For \(r\ge7\),
\[
r-1-\frac{(3r+1)^2}{12r}
=
\frac{3r(r-6)-1}{12r}>0.
\]
For \(r=6\), the integer maximum in (9) occurs at \(c=4\), giving
\[
\beta_6=\frac{(18-8)\cdot9}{18}=5=r-1.
\]
This proves Ryser’s inequality for maximum vertex degree at most three whenever \(r\ge6\).

The same calculation gives
\[
\beta_4=\frac{(12-6)\cdot7}{12}=\frac72,
\qquad
\beta_5=\frac{(15-6)\cdot7}{15}=\frac{21}{5},
\]
proving the remaining quantitative assertions.

## 4. Equality examples for the consecutive-degree result

The coefficient \(r-1\) in the first family cannot generally be improved.

Let \(q\ge2\) be a prime power and put \(r=q+1\). Index the parts by
\[
\mathbb F_q\cup\{\infty\},
\qquad
V_t=\{t\}\times\mathbb F_q.
\]
For each \((a,b)\in\mathbb F_q^2\), take the edge
\[
e_{a,b}
=
\{(\infty,a)\}
\cup
\{(t,b+ta):t\in\mathbb F_q\}.
\tag{12}
\]
This is an \(r\)-uniform \(r\)-partite hypergraph with \(q^2\) edges, and every vertex has degree \(q=r-1\).

Any two distinct edges intersect:

- If \(a=a'\), they share \((\infty,a)\).
- If \(a\ne a'\), the equation
  \[
  b+ta=b'+ta'
  \]
  has a unique solution \(t\in\mathbb F_q\).

Therefore \(\nu=1\). Since each vertex meets exactly \(q\) of the \(q^2\) edges, every cover has at least \(q\) vertices. Each part is a cover of size \(q\), so
\[
\tau=q=(r-1)\nu.
\]
These examples belong to the first family with \(d=r-2\). In particular, \(q=3\) gives a degree-three, \(4\)-partite equality example.

## 5. What remains unproved

The local certificate does not control arbitrary degree patterns. It already fails to imply the desired constant for certain maximum-degree-three patterns when \(r=4,5\):

- For \(r=4\), an edge with incident degrees \(1,3,3,3\) has
  \[
  (s+1)w=7\cdot2=14>12=r(r-1).
  \]
- For \(r=5\), incident degrees \(1,1,3,3,3\) give
  \[
  (s+1)w=7\cdot3=21>20=r(r-1).
  \]

These are limitations of the certificate, **not counterexamples to Ryser’s conjecture**. Likewise, no reduction has been established that transforms an arbitrary potential counterexample into one of the degree-restricted families above.

Thus the results are complete proofs of special cases and quantitative bounds, but not a proof or disproof of the unrestricted conjecture. I make no claim that these elementary consequences are new.