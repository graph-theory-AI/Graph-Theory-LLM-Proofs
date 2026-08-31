```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every 2-connected graph with a universal vertex, with the stronger bound η(G) ≥ 3n−10, and also for every co-bipartite graph admitting a clique part of size two.",
  "would_publish": false,
  "caveats": "The argument does not cover arbitrary 2-connected graphs without a universal vertex or the stated co-bipartite structure."
}
```

# 1. Statement and notation

For a connected graph \(G\), let
\[
\eta(G)=Sz(G)-W(G).
\]
For an edge \(uv\), write \(n_{uv}(u)\) for the number of vertices closer to \(u\) than to \(v\). Then
\[
Sz(G)=\sum_{uv\in E(G)}n_{uv}(u)n_{uv}(v).
\]

As usual, an edge \(uv\) is **good** for an unordered pair \(\{a,b\}\) if, after possibly exchanging \(u,v\),
\[
d(a,u)<d(a,v),\qquad d(b,v)<d(b,u).
\]
Let \(g(a,b)\) be the number of good edges for \(\{a,b\}\). Double counting gives
\[
\eta(G)=\sum_{\{a,b\}\subseteq V(G)}\bigl(g(a,b)-d(a,b)\bigr).
\tag{1}
\]

The notation \(K_n^t\) denotes \(K_{n-1}\) together with one additional vertex adjacent to exactly \(t\) vertices of the clique.

I prove two partial results:

1. If \(G\) is 2-connected and has a universal vertex, then, apart from \(K_n,K_n^2,K_n^{n-2}\),
   \[
   \eta(G)\ge 3n-10.
   \tag{2}
   \]
   Hence the conjecture holds in this class for \(n\ge10\).

2. If \(V(G)\) can be partitioned into a clique of order \(2\) and a clique of order \(n-2\), then the conjecture also holds. This class contains an infinite family attaining \(\eta(G)=2n\).

# 2. An exact identity for diameter-two graphs

Let \(p_3(G),p_4(G),c_4(G)\) denote the numbers of induced copies of \(P_3,P_4,C_4\), respectively, and let \(\overline m(G)\) be the number of nonedges.

## Lemma 2.1
If \(\operatorname{diam}(G)\le2\), then
\[
\boxed{\eta(G)=2\bigl(p_3(G)-\overline m(G)\bigr)+p_4(G)+4c_4(G).}
\tag{3}
\]

### Proof

Consider first a nonedge \(xy\). Let \(r=|N(x)\cap N(y)|\). Every common neighbor produces the two good edges of a length-two \(x\)-\(y\) path. Every further good edge joins a vertex in
\[
N(x)\setminus N(y)
\quad\text{to a vertex in}\quad
N(y)\setminus N(x),
\]
and therefore produces an induced \(P_4\) with endpoints \(x,y\). Thus
\[
g(x,y)-d(x,y)=2r-2+\#\{\text{induced \(P_4\)'s with endpoints \(x,y\)}\}.
\]
Summing \(r\) over all nonedges counts every induced \(P_3\) once.

If \(xy\) is an edge, then \(xy\) itself accounts for the distance contribution \(1\). Every additional good edge is the edge opposite \(xy\) in an induced \(C_4\). Consequently, summing over adjacent pairs counts each induced \(C_4\) four times. This proves (3). \(\square\)

As a quick check, for \(K_n^t\), putting \(s=n-1-t\), there are \(s\) nonedges and \(st\) induced \(P_3\)'s, but no induced \(P_4\) or \(C_4\). Hence
\[
\eta(K_n^t)=2s(t-1)=2(n-1-t)(t-1).
\tag{4}
\]
In particular,
\[
\eta(K_n^2)=\eta(K_n^{n-2})=2n-6.
\]

# 3. Graphs with a universal vertex

Suppose \(G\) has a universal vertex \(u\), and put \(Q=G-u\). If \(G\) is 2-connected, then \(Q\) is connected. Conversely, if \(Q\) is connected, then the cone \(K_1\vee Q\) is 2-connected.

Every nonedge of \(G\) lies in \(Q\). Moreover,
\[
p_3(G)=p_3(Q)+\overline m(Q),
\]
because each nonedge \(xy\) of \(Q\), together with \(u\), induces a \(P_3\). A universal vertex cannot lie in an induced \(P_4\) or \(C_4\). Therefore (3) gives
\[
\boxed{\eta(K_1\vee Q)=2p_3(Q)+p_4(Q)+4c_4(Q).}
\tag{5}
\]

The necessary extremal statement is the following.

## Lemma 3.1
Let \(Q\) be a connected, noncomplete graph of order \(m\). Unless

- \(Q\cong K_m-e\), or
- \(Q\) is \(K_{m-1}\) with one pendant vertex,

we have
\[
2p_3(Q)+p_4(Q)+4c_4(Q)\ge 3m-7.
\tag{6}
\]

For each of the two exceptional graphs, the left side equals \(2m-4\).

### Proof

Choose a maximum clique \(C\) of \(Q\), of order \(c\ge2\), and let \(L_i\) be the set of vertices at distance \(i\) from \(C\). Put
\[
\ell=|L_1|,\qquad r=\sum_{i\ge2}|L_i|,
\]
so that \(m=c+\ell+r\).

For \(x\in L_1\), put \(a_x=|N(x)\cap C|\). Maximality of \(C\) gives
\[
1\le a_x\le c-1.
\]
For every choice of
\[
v\in N(x)\cap C,\qquad w\in C\setminus N(x),
\]
the triple \(x,v,w\) induces a \(P_3\). Thus \(x\) lies in at least
\[
a_x(c-a_x)\ge c-1
\]
such induced \(P_3\)'s.

Every vertex \(x\in L_i\), \(i\ge2\), supplies another induced \(P_3\): take the first three vertices on a shortest path from \(x\) to \(C\). These copies are distinct for different \(x\). Therefore
\[
p_3(Q)\ge(c-1)\ell+r.
\tag{7}
\]

Similarly, each vertex at distance at least two from \(C\) supplies an induced \(P_4\). For \(i\ge3\), take the first four vertices of a shortest path. If \(x\in L_2\), take a shortest path \(x-y-v\), where \(v\in C\); since \(y\) is not complete to \(C\), choose \(w\in C\setminus N(y)\). Then \(x-y-v-w\) is induced. Hence
\[
p_4(Q)\ge r.
\tag{8}
\]

### Case 1: \(c\ge3\) and \(\ell\ge2\)

By (7) and (8),
\[
2p_3+p_4+4c_4\ge2(c-1)\ell+3r.
\]
The difference between this and \(3m-7\) is
\[
(2c-5)\ell-3c+7\ge c-3\ge0.
\]

### Case 2: \(c\ge3\) and \(\ell=1\)

Let \(L_1=\{x\}\), let \(a=|N(x)\cap C|\), and put
\[
A=a(c-a)\ge c-1.
\]

If \(r=0\), then \(Q\) consists of \(C\) and \(x\), and
\[
2p_3+p_4+4c_4=2A.
\]
If \(a=1\), this is \(K_c\) with a pendant vertex. If \(a=c-1\), this is \(K_{c+1}-e\). Otherwise \(2\le a\le c-2\), so
\[
2A\ge4(c-2)\ge3c-4=3m-7.
\]

Now suppose \(r>0\). Write
\[
s=|L_2|,\qquad t=\sum_{i\ge3}|L_i|,
\]
so \(s\ge1\) and \(r=s+t\). Every \(y\in L_2\) is adjacent to \(x\). For every
\[
v\in N(x)\cap C,\qquad w\in C\setminus N(x),
\]
the path \(y-x-v-w\) is induced. Thus
\[
p_3(Q)\ge A+r,\qquad p_4(Q)\ge As+t.
\]
Consequently,
\[
2p_3+p_4+4c_4
 \ge 2A+(A+2)s+3t.
\]
Subtracting \(3m-7=3c+3s+3t-4\), the difference is at least
\[
2(c-1)+(c-2)-3c+4=0.
\]

### Case 3: \(c=2\)

Write \(C=\{u,v\}\). The graph is triangle-free. Partition \(L_1\) as
\[
A=N(u)\cap L_1,\qquad B=N(v)\cap L_1,
\]
and put \(\alpha=|A|\), \(\beta=|B|\), so \(\ell=\alpha+\beta\).

Besides the \(\ell+r\) induced \(P_3\)'s counted in (7), every pair in \(A\) forms an induced \(P_3\) through \(u\), and every pair in \(B\) forms one through \(v\). If \(e\) is the number of edges between \(A\) and \(B\), then each nonedge \(xy\), with \(x\in A,y\in B\), gives the induced \(P_4\)
\[
x-u-v-y,
\]
whereas each edge \(xy\) gives the induced \(C_4\)
\[
x-u-v-y-x.
\]
Together with (8), this gives
\[
\begin{aligned}
2p_3+p_4+4c_4
&\ge 2\left(\ell+r+\binom{\alpha}{2}+\binom{\beta}{2}\right)
   +r+(\alpha\beta-e)+4e\\
&=2\ell+3r+
 \alpha(\alpha-1)+\beta(\beta-1)+\alpha\beta+3e.
\end{aligned}
\]
Now
\[
\alpha(\alpha-1)+\beta(\beta-1)+\alpha\beta\ge\alpha+\beta-1=\ell-1.
\]
Therefore
\[
2p_3+p_4+4c_4\ge3\ell+3r-1=3m-7.
\]
This proves the lemma. \(\square\)

## Theorem 3.2
Let \(G\) be a 2-connected graph of order \(n\) with a universal vertex. If
\[
G\not\cong K_n,\ K_n^2,\ K_n^{n-2},
\]
then
\[
\boxed{\eta(G)\ge3n-10.}
\tag{9}
\]

### Proof

Write \(G=K_1\vee Q\), where \(Q\) is connected of order \(m=n-1\).

- If \(Q\) is complete, then \(G=K_n\).
- If \(Q\cong K_m-e\), then \(G\cong K_n^{n-2}\).
- If \(Q\) is \(K_{m-1}\) with a pendant vertex, then \(G\cong K_n^2\).
- Otherwise, (5) and Lemma 3.1 give
  \[
  \eta(G)\ge3m-7=3n-10.
  \]

For \(n\ge10\), \(3n-10\ge2n\). \(\square\)

The bound \(3n-10\) is sharp: if \(Q=P_{n-1}\), then
\[
p_3(Q)=n-3,\qquad p_4(Q)=n-4,\qquad c_4(Q)=0,
\]
so
\[
\eta(K_1\vee P_{n-1})=3n-10.
\]

# 4. A co-bipartite special case

We next consider graphs whose vertices can be partitioned as
\[
V(G)=\{a_1,a_2\}\mathbin{\dot\cup}B,
\]
where both \(G[\{a_1,a_2\}]\) and \(G[B]\) are complete. Put \(s=|B|=n-2\).

Partition \(B\) according to adjacency to \(a_1,a_2\):
\[
\begin{array}{c|c}
\text{class}&\text{size}\\ \hline
N(a_1)\cap N(a_2)\cap B & x\\
(N(a_1)\setminus N(a_2))\cap B & y\\
(N(a_2)\setminus N(a_1))\cap B & z\\
B\setminus(N(a_1)\cup N(a_2)) & w.
\end{array}
\]
Thus
\[
s=x+y+z+w.
\]

If \(G\) is 2-connected, then
\[
x+y>0,\qquad x+z>0,\qquad x+y+z\ge2.
\tag{10}
\]
Indeed, deleting \(a_2\) or \(a_1\) proves the first two inequalities, while if all cross edges met one vertex of \(B\), that vertex would be a cut vertex.

These conditions also imply \(\operatorname{diam}(G)\le2\).

## Proposition 4.1
For such a graph,
\[
\boxed{
\eta(G)=2x(y+z)+8yz+w\bigl(4x+3y+3z-4\bigr).
}
\tag{11}
\]

### Proof

Put \(h=y+z\). For a cross nonedge \(a_1b\):

- if \(b\) belongs to the \(z\)-class, it has \(x+y+1\) common neighbors with \(a_1\);
- if \(b\) belongs to the \(w\)-class, it has \(x+y\) common neighbors with \(a_1\).

The analogous statement holds for \(a_2\). Hence
\[
p_3(G)-\overline m(G)
=xh+2yz+w(2x+h-2).
\tag{12}
\]

An induced \(P_4\) must use both \(a_1,a_2\), one vertex from the \(w\)-class, and one vertex from the \(y\)- or \(z\)-class. Thus
\[
p_4(G)=w(y+z)=wh.
\tag{13}
\]

An induced \(C_4\) arises from one vertex in the \(y\)-class and one in the \(z\)-class, so
\[
c_4(G)=yz.
\tag{14}
\]
Substitution in (3) gives (11). \(\square\)

## Theorem 4.2
Let \(n\ge10\), and suppose \(G\) is 2-connected and admits a partition into cliques \(K_2\) and \(K_{n-2}\). If
\[
G\not\cong K_n,\ K_n^2,\ K_n^{n-2},
\]
then
\[
\boxed{\eta(G)\ge2n.}
\tag{15}
\]

### Proof

Here \(s=n-2\ge8\), so the target is \(\eta(G)\ge2s+4\).

If \(x=0\), (10) gives \(y,z\ge1\). From (11),
\[
\eta-(2s+4)
=8yz-2(y+z)-4+3w(y+z-2)\ge0.
\]
Equality occurs when \(y=z=1\).

If \(y=z=0\), then \(x\ge2\). Unless \(w=0\), which gives \(K_n\),
\[
\eta=4w(x-1)\ge2(x+w)+4=2s+4,
\]
using \(x+w=s\ge8\).

It remains to assume \(x\ge1\) and \(h=y+z\ge1\). From (11),
\[
\eta-(2s+4)
=2(x-1)(h-1)-6+8yz+w(4x+3h-6).
\tag{16}
\]

If \(w\ge1\), the right side is nonnegative. Indeed, its only potentially small parameter triples are
\[
(x,h)=(1,1),(1,2),(2,1),
\]
and \(x+h+w\ge8\) gives respectively \(w\ge6,5,5\), which makes (16) nonnegative.

Suppose \(w=0\). If \(yz>0\), then (16) is again positive. If \(yz=0\), one of \(a_1,a_2\) is adjacent to all of \(B\), while the other is adjacent to exactly \(x\) vertices of \(B\). Thus
\[
G\cong K_n^{x+1}.
\]
The cases \(x=1\) and \(h=1\) are precisely \(K_n^2\) and \(K_n^{n-2}\). Otherwise \(x,h\ge2\) and \(x+h=s\ge8\), so
\[
(x-1)(h-1)\ge5,
\]
and (16) is at least \(4\). This proves (15). \(\square\)

There is an infinite admissible equality family. Take a clique
\[
A=\{a_1,a_2\}
\]
and a clique \(B\) of order \(n-2\), and put exactly two edges between them, forming a matching \(a_1b_1,a_2b_2\). Then
\[
x=0,\qquad y=z=1,\qquad w=n-4,
\]
and (11) gives
\[
\eta(G)=8+2(n-4)=2n.
\]
Thus the conjectured constant \(2n\) is best possible even outside the three excluded families.

# 5. What remains open

The above gives a complete proof of the conjecture in two substantial classes:

- all 2-connected graphs with domination number \(1\);
- all 2-connected co-bipartite graphs with a clique part of order \(2\).

The unresolved case consists of general 2-connected graphs with no universal vertex and without the second clique-partition structure. In particular, identity (3) is only directly available for diameter-two graphs, and even there a general lower bound on
\[
2\bigl(p_3-\overline m\bigr)+p_4+4c_4
\]
under 2-connectivity remains to be established. No step above proves that a graph with \(\eta(G)<2n\) must belong to either treated class, so this is a genuine gap rather than a reduction of the full conjecture.