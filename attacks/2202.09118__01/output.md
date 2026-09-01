```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but a tight exponent log_3(7/2) is obtained for a natural perfect/odd-antihole decomposition subclass, and an explicit {P5,C5}-free family rules out every linear bound for all k.",
  "would_publish": false,
  "caveats": "The argument does not control arbitrary odd-hole-free prime atoms or graphs containing up to k-1 pairwise anticomplete odd holes."
}
```

## 1. Statement and scope

Let \(\mathcal C_k\) be the class of graphs with no \(k\) pairwise vertex-disjoint and pairwise anticomplete odd holes. The problem asks whether, for every fixed \(k\), there is a polynomial \(p_k\) such that
\[
\chi(G)\le p_k(\omega(G))\qquad(G\in\mathcal C_k).
\]

For \(k=1\), \(\mathcal C_1\) is exactly the class of odd-hole-free graphs. Thus the problem is already open in its first case.

I do not resolve the conjecture. I prove two related results:

1. For every \(k\), \(\mathcal C_k\) is not linearly \(\chi\)-bounded. More precisely, no estimate \(O(\omega^q)\) can hold with
   \[
   q<\beta:=\log_3(7/2)=1.1403\ldots.
   \]
   The examples are even \(\{P_5,C_5\}\)-free.

2. A recursively defined subclass of odd-hole-free graphs, built from perfect graphs and odd antiholes by substitution and clique sums, satisfies
   \[
   \chi(G)\le \frac65\,\omega(G)^\beta-\frac15.
   \]
   The exponent \(\beta\) is optimal for this subclass.

These results show both that a prospective polynomial cannot be linear and that iterated odd-antihole substitution by itself cannot produce a counterexample.

---

## 2. An explicit superlinear family

### 2.1 Substitution

For a graph \(F\) with vertex set \(\{1,\dots,s\}\) and nonempty graphs \(H_1,\dots,H_s\), write
\[
F(H_1,\dots,H_s)
\]
for the graph obtained by replacing vertex \(i\) with \(H_i\), making \(H_i\) complete to \(H_j\) when \(ij\in E(F)\), and anticomplete otherwise.

Let
\[
A=\overline{C_7}.
\]
Define
\[
G_0=K_1,\qquad G_{t+1}=A(G_t,\dots,G_t),
\]
with seven copies of \(G_t\).

### 2.2 The graphs are \(\{P_5,C_5\}\)-free

First, \(A\) has no induced \(C_5\): otherwise taking complements would give an induced \(C_5\) in \(C_7\), but every proper induced subgraph of a chordless cycle is a forest.

Also, \(A\) has no induced \(P_5\). If \(A[S]\cong P_5\), then
\[
C_7[S]\cong \overline{P_5}.
\]
But \(\overline{P_5}\) has six edges, whereas an induced five-vertex subgraph of \(C_7\) has at most four edges.

Both \(P_5\) and \(C_5\) are prime graphs: neither has a nontrivial homogeneous set. Consequently, if a prime graph \(J\) occurs as an induced subgraph of a substitution \(F(H_1,\dots,H_s)\), then it either lies wholly in one bag \(H_i\), or it uses at most one vertex from every bag and projects to an induced \(J\) in \(F\). Thus substitution preserves \(J\)-freeness when \(J\) is prime.

It follows inductively that every \(G_t\) is \(\{P_5,C_5\}\)-free. In particular, it is odd-hole-free: an odd hole of length at least seven contains an induced \(P_5\), while \(C_5\) is explicitly excluded. Hence
\[
G_t\in\mathcal C_1\subseteq\mathcal C_k
\]
for every \(k\).

### 2.3 Clique and chromatic numbers

Let
\[
w_t=\omega(G_t),\qquad c_t=\chi(G_t).
\]

Since \(\omega(A)=3\),
\[
w_{t+1}=3w_t,
\]
and hence
\[
w_t=3^t.
\]

I next calculate the chromatic recurrence exactly. Suppose \(\chi(H)=m\). In a coloring of \(A(H,\dots,H)\), each of the seven bags must use at least \(m\) colors. A global color can occur in at most two bags, and if it occurs in two, their indices must be consecutive on the underlying \(C_7\), since those are precisely the nonedges of \(A\). Therefore at least
\[
\left\lceil \frac{7m}{2}\right\rceil
\]
colors are needed.

This number is attainable:

- If \(m=2s\), assign \(s\) private colors to every edge of the underlying \(C_7\), shared by its two endpoint bags. Each bag then receives \(2s=m\) colors, using \(7s=7m/2\) colors in total.

- If \(m=2s+1\), first do the same with \(s\) colors per cycle edge. This gives \(2s\) colors to every bag. Use three further colors on a matching covering six cycle vertices, and one singleton color on the remaining vertex. This uses
  \[
  7s+4=\left\lceil\frac{7(2s+1)}2\right\rceil
  \]
  colors.

Thus
\[
c_{t+1}=\left\lceil\frac{7c_t}{2}\right\rceil,\qquad c_0=1.
\]
In particular,
\[
c_t\ge \left(\frac72\right)^t.
\]

Set
\[
\beta=\log_3(7/2).
\]
Then
\[
\chi(G_t)=c_t\ge \left(\frac72\right)^t
=(3^t)^\beta
=\omega(G_t)^\beta.
\]

Consequently:

> **Proposition 1.** For every \(k\ge1\), no bound
> \[
> \chi(G)=O(\omega(G)^q)\qquad(G\in\mathcal C_k)
> \]
> is possible when \(q<\log_3(7/2)\). In particular, \(\mathcal C_k\) is not linearly \(\chi\)-bounded.

Since an ordinary polynomial has integral degree, any polynomial \(\chi\)-bound for \(\mathcal C_k\) must have degree at least two.

---

## 3. A tightly bounded substitution subclass

I now describe a subclass on which the preceding lower exponent is optimal.

Call a graph **perfect–antihole decomposable** if it can be obtained recursively by the following operations:

1. Every perfect graph belongs to the class.
2. If \(F\) is either perfect or an odd antihole
   \[
   \overline{C_{2r+1}},\qquad r\ge3,
   \]
   and every bag \(H_v\) is already in the class, then
   \[
   F(H_v:v\in V(F))
   \]
   belongs to the class.
3. The class is closed under clique sums: if two such graphs intersect in a clique and have no other cross-edges, their union belongs to the class.

The next theorem gives a tight power-law bound for this class.

### 3.1 Weighted coloring of a template

For a graph \(F\) and integer demands \(d_v\ge0\), let \(\chi_d(F)\) denote the minimum number of colors with which one can assign each vertex \(v\) a set of \(d_v\) colors, with adjacent vertices receiving disjoint sets.

For a substitution
\[
G=F(H_v:v\in V(F)),
\]
put \(d_v=\chi(H_v)\). Then
\[
\chi(G)=\chi_d(F).
\]
Indeed, a coloring of \(G\) induces a palette on every bag, and palettes of complete bags are disjoint. Conversely, an appropriate family of palettes together with optimal colorings of the bags colors \(G\).

Likewise, if \(w_v=\omega(H_v)\), then
\[
\omega(G)=
\max_{Q\text{ clique in }F}\sum_{v\in Q}w_v.
\tag{1}
\]

If \(F\) is perfect, then
\[
\chi_d(F)=\max_{Q\text{ clique in }F}\sum_{v\in Q}d_v.
\tag{2}
\]
To see this, replace every vertex \(v\) by a clique of size \(d_v\). Repeated vertex replication preserves perfection, and coloring the resulting blow-up is exactly weighted coloring of \(F\).

For completeness, the replication lemma has a short proof. Add to a perfect graph a true twin \(v'\) of \(v\). Consider an induced subgraph \(J\) containing both twins and put \(J_0=J-v'\), \(q=\omega(J_0)\). If \(\omega(J)=q+1\), color \(J_0\) with \(q\) colors and give \(v'\) a new color. Otherwise no \(q\)-clique of \(J_0\) contains \(v\). In a \(q\)-coloring of \(J_0\), let \(S\) be the color class containing \(v\). Then \(S\setminus\{v\}\) meets every \(q\)-clique, so
\[
\omega\bigl(J_0-(S\setminus\{v\})\bigr)\le q-1.
\]
The graph \(J-S\) is isomorphic to this induced subgraph, with \(v'\) replacing \(v\), and hence is \((q-1)\)-colorable. Giving \(S\) the final color produces a \(q\)-coloring of \(J\).

### 3.2 Weighted coloring of an odd antihole

Let \(A_n=\overline{C_n}\), where \(n\) is odd, and let \(d_0,\dots,d_{n-1}\) be nonnegative integer demands. Put
\[
D=\sum_i d_i,\qquad
W=\max\left\{\sum_{i\in I}d_i:I\text{ stable in }C_n\right\}.
\]

> **Lemma 2.**
> \[
> \chi_d(A_n)=\max\left\{W,\left\lceil\frac D2\right\rceil\right\}.
> \tag{3}
> \]

#### Proof

An independent set in \(A_n\) has at most two vertices, and a two-vertex independent set consists of consecutive vertices of \(C_n\). Thus every color either serves one demand unit or pairs demand units at two consecutive cycle vertices.

Construct a graph \(B\) by replacing vertex \(i\) of \(C_n\) with an independent set \(X_i\) of size \(d_i\), with consecutive bags complete to one another. A matching edge in \(B\) represents two demand units sharing one color. Hence
\[
\chi_d(A_n)=D-\nu(B),
\]
where \(\nu(B)\) is the maximum matching size.

Also,
\[
\alpha(B)=W.
\]

Let
\[
\delta=D-2\nu(B)
\]
be the number of unmatched vertices in a maximum matching. The Tutte–Berge formula gives
\[
\delta=\max_{S\subseteq V(B)}\bigl(o(B-S)-|S|\bigr),
\]
where \(o(X)\) is the number of odd-order components of \(X\).

For any matching, parity gives
\[
\delta\ge D\bmod 2,
\]
and a stable set of size \(W\) forces at least \(2W-D\) unmatched vertices. Thus
\[
\delta\ge \max\{D\bmod 2,\,2W-D\}.
\tag{4}
\]

For the reverse inequality, fix \(S\subseteq V(B)\).

- If every residual bag \(X_i\setminus S\) is nonempty, then \(B-S\) is connected. Hence
  \[
  o(B-S)-|S|\le 1.
  \]
  Since this quantity has the same parity as \(D\), it is at most \(D\bmod2\).

- If some residual bag is empty, every component of \(B-S\) is a blow-up of a path and hence bipartite. Taking the larger bipartition class in every component produces an independent set of size at least
  \[
  \frac{D-|S|+o(B-S)}2.
  \]
  Therefore
  \[
  W\ge\frac{D-|S|+o(B-S)}2,
  \]
  or
  \[
  o(B-S)-|S|\le2W-D.
  \]

Together with (4), this gives
\[
\delta=\max\{D\bmod2,\,2W-D\}.
\]
Therefore
\[
D-\nu(B)=\frac{D+\delta}{2}
=\max\left\{\left\lceil\frac D2\right\rceil,W\right\}.
\]
This proves the lemma. \(\square\)

### 3.3 A power inequality on odd cycles

Let
\[
\beta=\log_3(7/2),
\qquad\text{so that}\qquad 3^\beta=\frac72.
\]

> **Lemma 3.** Let \(n=2r+1\) with \(r\ge3\), and let \(x_0,\dots,x_{n-1}\ge0\). If
> \[
> \Omega=\max\left\{\sum_{i\in I}x_i:I\text{ stable in }C_n\right\},
> \]
> then
> \[
> \sum_{i=0}^{n-1}x_i^\beta\le2\Omega^\beta.
> \tag{5}
> \]

#### Proof

Relabel so that \(x_0=m=\min_i x_i\). The two sets
\[
E=\{1,3,\dots,2r-1\},\qquad
O=\{2,4,\dots,2r\}
\]
are stable in \(C_n\), so
\[
\sum_{i\in E}x_i\le\Omega,\qquad
\sum_{i\in O}x_i\le\Omega.
\]

For \(r\) numbers \(y_1,\dots,y_r\ge m\), the function
\[
\left(\sum_jy_j\right)^\beta-\sum_jy_j^\beta
\]
is nondecreasing in every coordinate because \(\beta>1\). Hence
\[
\left(\sum_jy_j\right)^\beta-\sum_jy_j^\beta
\ge (r^\beta-r)m^\beta.
\]
Applying this to \(E\) and \(O\),
\[
\sum_i x_i^\beta
\le
2\Omega^\beta+
\bigl(1-2(r^\beta-r)\bigr)m^\beta.
\]

Now
\[
3^\beta-3=\frac12,
\]
and \(r^\beta-r\) is increasing for \(r\ge3\). Thus
\[
r^\beta-r\ge\frac12,
\]
making the final coefficient nonpositive. This proves (5). \(\square\)

### 3.4 The special-case theorem

> **Theorem 4.** Every nonempty perfect–antihole decomposable graph \(G\) is odd-hole-free and satisfies
> \[
> \chi(G)\le f(\omega(G)),
> \qquad
> f(x)=\frac65x^\beta-\frac15,
> \qquad
> \beta=\log_3(7/2).
> \tag{6}
> \]

#### Proof of the chromatic bound

Proceed by induction on a construction tree.

If \(G\) is perfect and \(w=\omega(G)\), then
\[
\chi(G)=w\le\frac65w^\beta-\frac15,
\]
since \(w^\beta\ge w\) for \(w\ge1\).

Now let
\[
G=F(H_v:v\in V(F)),
\]
put
\[
w_v=\omega(H_v),\qquad d_v=\chi(H_v),
\]
and let \(\Omega=\omega(G)\). By induction,
\[
d_v\le\frac65w_v^\beta-\frac15.
\tag{7}
\]

If \(F\) is perfect, then by (2), for every clique \(Q\) of \(F\),
\[
\begin{aligned}
\sum_{v\in Q}d_v
&\le \frac65\sum_{v\in Q}w_v^\beta-\frac{|Q|}{5}\\
&\le \frac65\left(\sum_{v\in Q}w_v\right)^\beta-\frac15\\
&\le \frac65\Omega^\beta-\frac15.
\end{aligned}
\]
Thus (6) follows.

Suppose next that \(F=\overline{C_n}\), with \(n\ge7\) odd. Cliques of \(F\) correspond to stable sets of \(C_n\). For every such nonempty stable set \(I\),
\[
\sum_{i\in I}d_i
\le
\frac65\left(\sum_{i\in I}w_i\right)^\beta-\frac15
\le f(\Omega).
\tag{8}
\]

Also, by Lemma 3,
\[
\begin{aligned}
D:=\sum_i d_i
&\le \frac65\sum_iw_i^\beta-\frac n5\\
&\le \frac{12}{5}\Omega^\beta-\frac n5\\
&=2f(\Omega)-\frac{n-2}{5}\\
&\le2f(\Omega)-1,
\end{aligned}
\]
because \(n\ge7\). Hence
\[
\left\lceil\frac D2\right\rceil
\le \frac{D+1}{2}
\le f(\Omega).
\tag{9}
\]
Equations (8), (9), and Lemma 2 prove the desired bound.

Finally, if \(G\) is a clique sum of \(G_1,G_2\), then
\[
\omega(G)=\max\{\omega(G_1),\omega(G_2)\},
\qquad
\chi(G)=\max\{\chi(G_1),\chi(G_2)\}.
\]
For the coloring equality, permute the colors in each summand so that the common clique receives the same colors. Since \(f\) is increasing, the induction closes.

#### Proof that the class is odd-hole-free

A perfect graph has no odd hole, since an odd hole has clique number \(2\) and chromatic number \(3\).

Also, \(\overline{C_n}\) is odd-hole-free for odd \(n\ge7\). If it contained an induced \(C_m\), then \(C_n\) would contain an induced \(\overline{C_m}\). For a proper vertex subset, \(C_n\) induces a forest with at most \(m-1\) edges, while
\[
|E(\overline{C_m})|=\frac{m(m-3)}2>m-1
\]
for \(m\ge5\). If all vertices were used, the degree sequences of \(C_n\) and \(\overline{C_n}\) differ.

Substitution preserves odd-hole-freeness. Indeed, every cycle \(C_m\), \(m\ge5\), is prime. If an induced \(C_m\) in a substitution meets a bag in more than one vertex and also meets another bag, that intersection is a nontrivial homogeneous set in the cycle, impossible. Thus the cycle either lies in one bag or uses one vertex per bag and projects to an odd hole in the template.

An induced hole cannot cross a clique sum: it would need two nonconsecutive vertices of the common clique, producing a chord.

This completes the proof. \(\square\)

### 3.5 Tightness within this subclass

Every \(G_t\) from Section 2 is perfect–antihole decomposable, since it is obtained by repeated substitution into \(\overline{C_7}\). We have
\[
\chi(G_t)\ge\omega(G_t)^\beta,
\]
while Theorem 4 gives
\[
\chi(G_t)\le\frac65\omega(G_t)^\beta-\frac15.
\]

Thus \(\beta=\log_3(7/2)\) is the optimal power-law exponent for this recursively decomposable subclass.

---

## 4. Why this does not settle the conjecture

The missing point is a decomposition theorem. An arbitrary odd-hole-free graph need not come equipped with a clique cutset or with a substitution whose template is perfect or an odd antihole. Merely containing an induced odd antihole does not make that antihole a homogeneous set and therefore does not permit the weighted substitution induction above.

Moreover, for \(k\ge2\), graphs in \(\mathcal C_k\) may contain odd holes; they merely cannot contain \(k\) pairwise anticomplete ones. Nothing in the present argument bounds the chromatic contribution of neighborhoods of those holes.

Accordingly:

- the construction proves a genuine lower bound for every \(k\);
- Theorem 4 handles a nontrivial, substitution-closed portion of the \(k=1\) class;
- no polynomial upper bound is obtained for all odd-hole-free graphs, and hence the catalog problem remains open.