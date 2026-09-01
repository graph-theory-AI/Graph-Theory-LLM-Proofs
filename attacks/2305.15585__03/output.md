```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A bad pair has tournament domination number and odd girth at least half its chromatic number, fractional chromatic number at most 5 (at most 9/2 in the high-chromatic regime), and the conjecture follows in several substantial special cases.",
  "would_publish": false,
  "caveats": "No general o(log N) bound or counterexample is obtained; short even cycles obstruct the available Moore-bound argument."
}
```

# 1. Statement and reformulation

Call a pair \((G,T)\) **bad** if \(G\) and \(T\) have the same vertex set and
\[
\chi\bigl(G[N_T^+(v)]\bigr)\le 2
\qquad\text{for every }v.
\]
Let
\[
h(N)=\max\{\chi(G):(G,T)\text{ is a bad pair on }N\text{ vertices}\}.
\]
The conjecture is equivalent to
\[
h(N)=o(\log N).
\]

I do not prove this. I establish several structural restrictions on a bad pair. The main one is that every odd cycle is a dominating set in \(T\), which implies that the odd girth and the domination number of \(T\) are both at least approximately \(\chi(G)/2\).

# 2. Dominating sets and odd cycles

A set \(D\subseteq V(T)\) is dominating if every vertex outside \(D\) is beaten by some vertex of \(D\). Write \(\gamma(T)\) for the minimum size of such a set.

## Lemma 2.1: every non-bipartite set dominates

If \((G,T)\) is bad and \(S\subseteq V(G)\) induces a non-bipartite graph, then \(S\) is a dominating set of \(T\).

### Proof

Choose an odd cycle \(C\subseteq G[S]\). If some \(x\notin S\) beat every vertex of \(C\), then
\[
C\subseteq N_T^+(x),
\]
contradicting the bipartiteness of \(G[N_T^+(x)]\). Thus some vertex of \(C\), and hence of \(S\), beats \(x\). This holds for every \(x\notin S\). ∎

In particular, every odd cycle of \(G\) is a dominating set in \(T\).

## Lemma 2.2: coloring from a dominating set

If \(D\) is a dominating set of \(T\) and \(d=|D|\), then
\[
\chi(G)\le 2d+1.
\]

### Proof

Every vertex outside \(D\) belongs to \(N_T^+(u)\) for some \(u\in D\). Every vertex of \(D\), except possibly a source of \(T[D]\), also belongs to \(N_T^+(u)\) for some \(u\in D\). A tournament has at most one source.

Therefore all but at most one vertex of \(G\) can be partitioned into sets
\[
X_u\subseteq N_T^+(u),\qquad u\in D.
\]
Each \(G[X_u]\) is bipartite. Using a separate pair of colors for every \(u\in D\), and one additional color for the possible exceptional source, gives \(2d+1\) colors. ∎

Combining the two lemmas gives the following.

## Theorem 2.3: domination number and odd girth

Let \((G,T)\) be bad, and put \(k=\chi(G)\). Then
\[
\gamma(T)\ge \frac{k-1}{2}.
\]
If \(G\) is non-bipartite and \(g_{\mathrm{odd}}(G)\) denotes its odd girth, then
\[
g_{\mathrm{odd}}(G)\ge \gamma(T)\ge \frac{k-1}{2}.
\]

### Proof

Apply Lemma 2.2 to a minimum dominating set to get
\[
k\le 2\gamma(T)+1.
\]
Every shortest odd cycle is a dominating set by Lemma 2.1, so
\[
\gamma(T)\le g_{\mathrm{odd}}(G).
\]
∎

Thus any hypothetical sequence of bad pairs with \(\chi(G)=\Theta(\log N)\) must consist of graphs whose odd girth is itself \(\Theta(\log N)\).

## Corollary 2.4: the standard logarithmic upper bound

Every tournament on \(N\) vertices has a dominating set of size at most
\[
\lceil\log_2 N\rceil.
\]
Indeed, repeatedly choose a vertex of maximum out-degree in the remaining tournament and delete it together with its out-neighbors; the remaining order at least halves at each step.

Consequently every bad pair satisfies
\[
\boxed{\chi(G)\le 2\lceil\log_2 N\rceil+1.}
\]
Equivalently, if a bad pair has chromatic number \(k\), then
\[
N>2^{(k-3)/2}.
\]

This recovers the correct logarithmic scale but not the required little-\(o\) improvement.

# 3. Fractional chromatic restrictions

The local hypothesis has a strong weighted consequence.

## Theorem 3.1

Every bad graph \(G\) satisfies
\[
\boxed{\chi_f(G)\le 5.}
\]

### Proof

Let \(w:V(G)\to\mathbb R_{\ge0}\) be arbitrary. Put
\[
W=\sum_{v}w(v),
\qquad
\alpha=\max\{w(I):I\text{ is independent in }G\}.
\]
For every \(v\), the graph \(G[N_T^+(v)]\) is bipartite, so its two color classes are independent in \(G\). Hence
\[
w(N_T^+(v))\le 2\alpha.
\]
Moreover \(w(v)\le\alpha\) for every \(v\).

Since every unordered pair is oriented exactly once,
\[
\sum_v w(v)w(N_T^+(v))
 =\sum_{\{u,v\}}w(u)w(v)
 =\frac{W^2-\sum_v w(v)^2}{2}.
\]
Therefore
\[
\frac{W^2-\sum_v w(v)^2}{2}\le 2\alpha W.
\]
Using
\[
\sum_v w(v)^2\le \alpha W
\]
gives
\[
W^2\le 5\alpha W,
\]
and hence \(W/\alpha\le5\). The weighted dual characterization of fractional chromatic number now gives \(\chi_f(G)\le5\). ∎

The constant \(5\) is sharp: take \(G=K_5\) and let \(T\) be the regular cyclic tournament on five vertices. Every out-neighborhood has two vertices and hence induces \(K_2\), while \(\chi_f(K_5)=5\).

For chromatic number at least \(8\), Theorem 2.3 implies that \(G\) is triangle-free. In that regime the fractional bound improves.

## Theorem 3.2

If \((G,T)\) is bad and \(G\) is triangle-free, then
\[
\boxed{\chi_f(G)\le \frac92.}
\]

### Proof

Retain the notation \(W,\alpha,w\) from Theorem 3.1. For each \(v\), choose a bipartition
\[
N_T^+(v)=A_v\cup B_v.
\]
Write \(x=w(v)\). Split \(A_v\) and \(B_v\) according to adjacency to \(v\):
\[
a_1=w(A_v\cap N_G(v)),\quad a_0=w(A_v\setminus N_G(v)),
\]
and similarly \(b_1,b_0\).

Since \(G\) is triangle-free, \(N_G(v)\) is independent, so
\[
a_1+b_1\le\alpha.
\]
Also \(A_v,B_v\) are independent, and
\[
\{v\}\cup(A_v\setminus N_G(v)),\qquad
\{v\}\cup(B_v\setminus N_G(v))
\]
are independent. Thus
\[
a_0,b_0\le\alpha-x.
\]
It follows that
\[
w(N_T^+(v))
 \le
 \begin{cases}
 2\alpha,&x\le\alpha/2,\\
 3\alpha-2x,&x>\alpha/2.
 \end{cases}
\]
Equivalently,
\[
w(N_T^+(v))
 \le 2\alpha-(2x-\alpha)_+.
\]
Consequently,
\[
\frac{W^2-\sum_vw(v)^2}{2}
 \le 2\alpha W-\sum_v w(v)(2w(v)-\alpha)_+.
\]
For every \(0\le x\le\alpha\),
\[
x^2-2x(2x-\alpha)_+\le \frac{\alpha x}{2}.
\]
Summing this pointwise inequality yields
\[
W^2\le 4\alpha W+\frac{\alpha W}{2}
 =\frac92\alpha W.
\]
Hence \(W/\alpha\le9/2\), proving the claim by LP duality. ∎

Thus every bad pair with \(\chi(G)\ge8\) satisfies simultaneously
\[
g_{\mathrm{odd}}(G)\ge\frac{\chi(G)-1}{2},
\qquad
\chi_f(G)\le\frac92.
\]
A counterexample to the conjecture would therefore require a logarithmic integrality gap between ordinary and fractional chromatic number while also having logarithmic odd girth.

# 4. Further structural consequences

## Clique number

For every bad pair,
\[
\omega(G)\le5.
\]
Indeed, if \(Q\) is a clique, then every vertex of \(T[Q]\) has out-degree at most \(2\), since its out-neighbors in \(Q\) induce a clique inside a bipartite graph. Hence
\[
\frac{|Q|(|Q|-1)}2\le2|Q|,
\]
so \(|Q|\le5\). The \(K_5\) example above shows sharpness.

## Optimal coloring classes

Fix an optimal \(k\)-coloring
\[
V(G)=V_1\cup\cdots\cup V_k.
\]
For every \(I\subseteq[k]\),
\[
\chi\left(G\left[\bigcup_{i\in I}V_i\right]\right)=|I|;
\]
otherwise one could recolor that union with fewer than \(|I|\) colors and improve the original coloring.

In particular, the union of every three color classes is non-bipartite and therefore contains an odd cycle of length at least \(g_{\mathrm{odd}}(G)\). Double-counting over triples gives
\[
\binom{k-1}{2}N
 \ge \binom{k}{3}g_{\mathrm{odd}}(G),
\]
and hence
\[
N\ge \frac{k}{3}g_{\mathrm{odd}}(G)
 \ge \frac{k(k-1)}6.
\]
This polynomial bound is weaker than the domination-number exponential bound, but it shows that every triple of classes already carries a global tournament-dominating obstruction.

## The local-independent case is completely bounded

If the stronger hypothesis
\[
G[N_T^+(v)]\text{ is independent for every }v
\]
holds, then \(\chi(G)\le3\).

Indeed, the endpoints of every edge of \(G\) form a dominating set of \(T\); otherwise some vertex would beat both endpoints. Applying the analogue of Lemma 2.2 with one color per out-neighborhood gives at most \(2+1=3\) colors. This explains why local chromatic number \(2\), rather than \(1\), is the first genuinely unbounded case.

# 5. Two special cases where the conjectured conclusion follows

## 5.1 Tournaments of sublogarithmic domination number

If a family of tournaments satisfies
\[
\gamma(T)\le a(N)=o(\log N),
\]
then every bad pair with such a tournament satisfies
\[
\chi(G)\le2a(N)+1=o(\log N).
\]
Thus the conjecture holds on this class with threshold
\[
f(N)=2a(N)+2.
\]

This does not settle the general case: tournaments can have domination number
\[
\log_2 N-2\log_2\log_2 N-O(1).
\]
A direct probabilistic verification is as follows. Let \(L=\log_2N\) and
\[
s=\left\lfloor L-2\log_2L-3\right\rfloor.
\]
In a random tournament, a fixed \(s\)-set dominates with probability
\[
(1-2^{-s})^{N-s}.
\]
Hence the expected number of dominating \(s\)-sets is at most
\[
\binom Ns\exp(-(N-s)2^{-s})=o(1).
\]
Therefore some tournaments have no dominating set of size \(s\). The domination-set argument is consequently tight to first order.

## 5.2 When short even cycles are also excluded

Suppose in addition that, for some fixed \(c>0\),
\[
\operatorname{girth}(G)\ge c\,g_{\mathrm{odd}}(G).
\]
This includes the case where a shortest cycle of \(G\) is odd, for which \(c=1\).

Let \(k=\chi(G)\), and take a \(k\)-critical subgraph \(H\). Then
\[
\delta(H)\ge k-1
\]
and, under the bad-pair hypothesis,
\[
\operatorname{girth}(H)\ge\operatorname{girth}(G)
 \ge \frac{c(k-1)}2.
\]
Put
\[
r=\left\lfloor\frac{\operatorname{girth}(H)-1}{2}\right\rfloor.
\]
The standard breadth-first Moore argument gives
\[
N\ge
1+(k-1)\sum_{i=0}^{r-1}(k-2)^i
\ge (k-2)^r.
\]
Since \(r\ge ck/4-O(1)\),
\[
\log N\ge \left(\frac c4+o(1)\right)k\log k,
\]
and therefore
\[
\boxed{
k\le
\left(\frac4c+o(1)\right)\frac{\log N}{\log\log N}.
}
\]
This is \(o(\log N)\), so the conjectured conclusion holds in this special case.

The obstruction to applying this generally is the possible abundance of short even cycles. Odd girth and large minimum degree alone do not give a Moore bound: replacing every vertex of a long odd cycle by an independent set and every cycle edge by a complete bipartite graph gives arbitrarily large minimum degree and the same odd girth, but only linearly many vertices in the degree parameter.

# 6. Fully specified finite search

Small cases can be searched exactly by SAT.

For vertices \([N]\), introduce:

- \(e_{xy}\) for every \(x<y\), indicating \(xy\in E(G)\);
- tournament variables \(a_{xy}\) for \(x<y\), where \(a_{xy}=1\) means \(x\to y\);
- local color variables \(b_{v,x}\in\{0,1\}\) for every \(v\ne x\).

For every distinct \(v,x,y\), impose
\[
\bigl(v\to x\bigr)\wedge\bigl(v\to y\bigr)\wedge e_{xy}
\quad\Longrightarrow\quad
b_{v,x}\ne b_{v,y}.
\]
These constraints are equivalent to the existence, for each \(v\), of a proper 2-coloring of \(G[N_T^+(v)]\).

To impose \(\chi(G)\ge k\), for every map
\[
c:[N]\to[k-1]
\]
add the clause
\[
\bigvee_{\substack{x<y\\c(x)=c(y)}} e_{xy}.
\]
Thus every proposed \((k-1)\)-coloring has a monochromatic edge. This encoding is exponential in \(N\), but it is exact and suitable for small orders or a QBF reformulation.

As a sanity check, for \(N=5\), \(G=K_5\) and the cyclic regular tournament satisfy all local constraints. For every \(N>5\), one may add isolated vertices to \(G\), orient every \(K_5\) vertex toward every isolate, and orient the isolates arbitrarily; this gives bad pairs with chromatic number \(5\).

No computational enumeration beyond this explicit construction was performed here.

# 7. Remaining gap

The results reduce a potential counterexample sequence with
\[
\chi(G)=\Omega(\log N)
\]
to a very constrained regime:

\[
\gamma(T)=\Omega(\log N),\qquad
g_{\mathrm{odd}}(G)=\Omega(\log N),\qquad
\chi_f(G)\le\frac92,
\]
with \(G\) triangle-free.

Neither the domination-number bound nor the fractional bound by itself excludes \(\chi(G)=\Theta(\log N)\). The ordinary-girth argument would prove the conjecture, but short even cycles invalidate its breadth-first expansion. I do not have an argument combining the tournament constraints, bounded fractional chromatic number, and large odd girth strongly enough to obtain \(o(\log N)\), nor do I have a construction attaining \(\Theta(\log N)\).