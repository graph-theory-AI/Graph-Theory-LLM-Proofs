```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A truncated-tail inequality for edge imbalances implies every Erdős–Gallai inequality and proves the conjecture.",
  "would_publish": true,
  "caveats": "The argument is self-contained apart from the standard Erdős–Gallai criterion; publication novelty has not been checked."
}
```

## Theorem

Let \(G\) be a finite simple undirected graph such that adjacent vertices have different degrees. Then
\[
M_G=\bigl\{|d(u)-d(v)|:uv\in E(G)\bigr\}
\]
is the degree multiset of a simple graph.

Write
\[
a_e=|d(u)-d(v)|\qquad(e=uv),\qquad
m=|E(G)|,\qquad D=\Delta(G).
\]
The hypothesis is \(a_e\ge 1\) for every edge.

The main ingredient is the following inequality.

## Truncated-tail lemma

If \(m>0\), then for every integer \(1\le k<D\) and every set \(S\subseteq E(G)\) of \(k\) edges,
\[
\boxed{\quad
\sum_{e\in E(G)\setminus S}\min\{k,a_e\}\ \ge\ k(D-k).
\quad} \tag{1}
\]

### Proof

First, \(m\ge D\), and the hypothesis implies \(D\ge2\).

For \(k=1\), positivity gives
\[
\sum_{e\notin S}\min\{1,a_e\}=m-1\ge D-1,
\]
as required.

We also dispose of \(D=3,\ k=2\). If \(m\ge4\), positivity gives a lower bound \(m-2\ge2\). If \(m=3\), the degree-three vertex is incident with every edge, so \(G\) consists of \(K_{1,3}\) and isolated vertices. All three imbalances are \(2\), and (1) again holds. These observations cover all cases with \(D\le3\).

Hence assume \(D\ge4\) and \(2\le k<D\).

Fix a vertex \(v\) of degree \(D\). Let
\[
q=m-D
\]
be the number of edges not incident with \(v\), and put
\[
s=|S\cap E(v)|,\qquad t=|S\setminus E(v)|=k-s.
\]
Define
\[
U=\{u\in N(v):vu\notin S\},\qquad r=|U|=D-s.
\]
Finally, put
\[
b=D-k.
\]
Thus \(b\ge1\), \(0\le t\le k\), and
\[
r=b+t. \tag{2}
\]

There are exactly \(q-t\) edges outside \(S\) that are not incident with \(v\). Each contributes at least \(1\) to the left side of (1). Moreover, since \(v\) has maximum degree,
\[
a_{vu}=D-d(u).
\]
Consequently,
\[
\begin{aligned}
\sum_{e\notin S}\min\{k,a_e\}
&\ge q-t+\sum_{u\in U}\min\{k,D-d(u)\}\\
&=q-t+kr-\sum_{u\in U}(d(u)-b)_+,
\end{aligned} \tag{3}
\]
where \(x_+=\max\{x,0\}\).

Let
\[
L=\{u\in U:d(u)>b\},\qquad \ell=|L|.
\]
Because every vertex of \(L\) is adjacent to \(v\),
\[
\sum_{u\in L}(d(u)-1)
\]
counts incidences of vertices in \(L\) with edges not incident with \(v\). Such an edge is counted at most once, except that an edge with both endpoints in \(L\) is counted twice. Simplicity therefore gives
\[
\sum_{u\in L}(d(u)-1)
\le q+|E(G[L])|
\le q+\binom{\ell}{2}.
\]
It follows that
\[
\sum_{u\in U}(d(u)-b)_+
=\sum_{u\in L}(d(u)-b)
\le q+\binom{\ell}{2}-(b-1)\ell. \tag{4}
\]

Set
\[
F_b(\ell)=\binom{\ell}{2}-(b-1)\ell.
\]
Combining (3) and (4), we obtain
\[
\sum_{e\notin S}\min\{k,a_e\}
\ge kr-t-F_b(\ell). \tag{5}
\]

We claim that
\[
F_b(\ell)\le (k-1)t. \tag{6}
\]
Indeed, \(0\le\ell\le r=b+t\), and \(F_b(x)\) is a convex quadratic. Its maximum on this interval is attained at an endpoint. Hence
\[
\begin{aligned}
F_b(\ell)
&\le \max\{F_b(0),F_b(b+t)\}\\
&=\max\left\{0,\binom{t+1}{2}-\binom b2\right\}. \tag{7}
\end{aligned}
\]

If \(k\ge3\), then
\[
\max\left\{0,\binom{t+1}{2}-\binom b2\right\}
\le \binom{t+1}{2}
\le \frac{t(k+1)}2
\le (k-1)t.
\]
If \(k=2\), then \(b=D-2\ge2\) and \(t\in\{0,1,2\}\). The last expression in (7) is respectively at most \(0,0,2\), and hence is at most \(t=(k-1)t\). This proves (6).

Using (6) in (5), and then (2), gives
\[
\sum_{e\notin S}\min\{k,a_e\}
\ge kr-t-(k-1)t
=k(r-t)
=kb
=k(D-k).
\]
This proves the lemma. \(\square\)

## Completion of the proof

If \(m=0\), the multiset is empty and is graphic. Assume \(m>0\).

First, the imbalance sum is even:
\[
\begin{aligned}
\sum_{uv\in E(G)}|d(u)-d(v)|
&\equiv \sum_{uv\in E(G)}(d(u)+d(v))\\
&=\sum_{v\in V(G)}d(v)^2\\
&\equiv\sum_{v\in V(G)}d(v)
=2m
\equiv0\pmod2.
\end{aligned} \tag{8}
\]

Also, both endpoints of an edge have positive degree, so
\[
1\le a_e\le D-1. \tag{9}
\]

Order the imbalances as
\[
a_1\ge a_2\ge\cdots\ge a_m.
\]
By the Erdős–Gallai criterion, it remains to prove, for every \(1\le k\le m\),
\[
\sum_{i=1}^{k}a_i
\le k(k-1)+\sum_{i=k+1}^{m}\min\{k,a_i\}. \tag{10}
\]

If \(k\ge D\), then (9) gives
\[
\sum_{i=1}^{k}a_i
\le k(D-1)
\le k(k-1),
\]
so (10) holds.

If \(1\le k<D\), apply the truncated-tail lemma to a set of edges carrying the \(k\) largest imbalances. It gives
\[
\sum_{i=k+1}^{m}\min\{k,a_i\}\ge k(D-k).
\]
Therefore,
\[
\begin{aligned}
k(k-1)+\sum_{i=k+1}^{m}\min\{k,a_i\}
&\ge k(k-1)+k(D-k)\\
&=k(D-1)\\
&\ge\sum_{i=1}^{k}a_i.
\end{aligned}
\]
Thus every Erdős–Gallai inequality holds. Together with (8), this proves that \(M_G\) is graphic. \(\square\)

## Scope and verification status

The argument covers disconnected graphs, isolated vertices, the empty graph, and all maximum degrees. Simplicity is used explicitly in the estimate
\[
|E(G[L])|\le\binom{|L|}{2},
\]
and positive imbalance is used to obtain one unit of tail contribution from every retained edge not incident with the chosen maximum-degree vertex.

No conjectural auxiliary assertion or computational check is needed. I have not independently checked whether this proof has appeared in the literature.