```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved for several substantial special cases, including all instances with at most three tournament vertices and all instances without asymmetric arcs from the stable part to the tournament part.",
  "would_publish": false,
  "caveats": "The mixed case with asymmetric S-to-T arcs and at least four tournament vertices remains unresolved."
}
```

# 1. Statement and notation

Fix a split partition
\[
V(G)=T\mathbin{\dot\cup}S,
\]
where \(G[T]\) is a tournament and \(S\) is stable. A set \(K\) is a strong \(2\)-kernel if it is stable, \(2\)-covers every vertex, and every \(t\in T\) is either \(1\)-covered by \(K\), or \(2\)-covered by \(K\cap T\).

Write
\[
m=|T|,\qquad r=|S|.
\]
Since \(K\) is stable and \(T\) is a tournament, \(|K\cap T|\leq 1\).

All distances below are directed distances, with a vertex covering itself at distance zero.

I do not settle the conjecture in full. I prove:

1. Every source-free split digraph has a strong \(2\)-kernel, with an explicit bound at most \(r+1\).
2. The conjectured bound holds if every tournament vertex has an in-neighbour in \(S\).
3. It holds whenever \(m\ge r+2\).
4. It holds if every arc \(s\to t\), with \(s\in S,t\in T\), is accompanied by \(t\to s\). In particular, for oriented digraphs this covers the case with no arcs from \(S\) to \(T\).
5. It holds whenever \(m\le 3\).
6. A further quantitative bound is obtained in terms of the tournament vertices having no in-neighbour in \(S\).

# 2. A weighted tournament lemma

We first record the basic tool.

## Lemma 2.1

Let \(Q\) be a tournament and let \(w:V(Q)\to\mathbb Z_{\ge 0}\) have total weight \(W>0\). There is a vertex \(q\) which \(2\)-covers all of \(Q\) and satisfies
\[
w(N_Q^-(q))<\frac W2.
\]

### Proof

For \(v\in V(Q)\), put
\[
F(v)=w(\{v\}\cup N_Q^+(v)).
\]
Choose \(q\) lexicographically maximizing
\[
\bigl(F(q),\,|\{q\}\cup N_Q^+(q)|\bigr).
\]

First, \(q\) is a \(2\)-king. Otherwise there is some \(u\) not reachable from \(q\) in at most two steps. Then \(u\to q\), and \(u\to x\) for every \(x\in N_Q^+(q)\), since otherwise \(q\to x\to u\). Hence
\[
\{q\}\cup N_Q^+(q)\subseteq N_Q^+(u).
\]
Thus \(F(u)\ge F(q)\), and if equality holds, the closed out-neighbourhood of \(u\) is strictly larger. This contradicts the choice of \(q\).

It remains to bound \(F(q)\). Choose a random vertex \(v\) with probability \(w(v)/W\). Then
\[
\begin{aligned}
\mathbb E F(v)
&=\frac1W\left(\sum_x w(x)^2+
   \sum_{x\to y}w(x)w(y)\right)\\
&=\frac1W\left(\sum_x w(x)^2+
   \sum_{\{x,y\}}w(x)w(y)\right)\\
&=\frac W2+\frac{\sum_xw(x)^2}{2W}>\frac W2.
\end{aligned}
\]
Therefore \(F(q)>W/2\). Since
\[
W=F(q)+w(N_Q^-(q)),
\]
the claimed inequality follows. ∎

# 3. Two elementary constructions

Define
\[
A=\{t\in T:N_G^-(t)\cap S=\varnothing\}.
\]
Thus \(A\) consists of tournament vertices that cannot be directly covered from \(S\).

## Proposition 3.1

If \(A=\varnothing\), then \(G\) has a strong \(2\)-kernel of size at most
\[
\min\{m,r\}\le \frac{m+r}{2}.
\]

### Proof

For each \(t\in T\), choose \(s_t\in S\) with \(s_t\to t\), and let
\[
K=\{s_t:t\in T\}.
\]
This is stable and has size at most both \(m\) and \(r\). Every tournament vertex is \(1\)-covered by \(K\).

If \(s\in S\setminus K\), then, because \(s\) is not a source and \(S\) is stable, there is \(t\in T\) with \(t\to s\). Thus
\[
s_t\to t\to s.
\]
Hence \(K\) is a strong \(2\)-kernel. ∎

## Proposition 3.2

Suppose \(A\ne\varnothing\), and let \(q\) be a \(2\)-king of the tournament \(G[A]\). Then
\[
K_q=\{q\}\cup\bigl(S\setminus N_G^+(q)\bigr)
\]
is a strong \(2\)-kernel. Consequently,
\[
|K_q|=1+r-|N_G^+(q)\cap S|\le r+1.
\]

### Proof

Since \(q\in A\), there is no arc from \(S\) to \(q\). Every member of \(S\setminus N_G^+(q)\) is therefore nonadjacent to \(q\), so \(K_q\) is stable.

Every \(s\in S\) is either in \(K_q\), or is directly covered by \(q\).

Every \(a\in A\) is \(2\)-covered by \(q\) inside the tournament \(G[A]\). Now let \(t\in T\setminus A\). Choose \(s\in S\) with \(s\to t\). If \(q\to s\), then
\[
q\to s\to t.
\]
Otherwise \(s\in K_q\), and \(s\) directly covers \(t\). Thus the required strong condition holds for every tournament vertex. ∎

This gives the following immediate partial result.

## Corollary 3.3

The conjectured bound holds whenever
\[
m\ge r+2.
\]

Indeed, Proposition 3.2 gives \(|K_q|\le r+1\le(m+r)/2\), while Proposition 3.1 handles \(A=\varnothing\).

More precisely, Proposition 3.2 proves the conjecture whenever some \(2\)-king \(q\) of \(G[A]\) satisfies
\[
|N_G^+(q)\cap S|
\ge r+1-\left\lfloor\frac{m+r}{2}\right\rfloor
=\left\lceil\frac{r-m+2}{2}\right\rceil.
\]

A further easy case is useful.

## Proposition 3.4

If the tournament \(G[T]\) has a source \(q\), then \(\{q\}\) is a strong \(2\)-kernel.

### Proof

The vertex \(q\) directly covers every tournament vertex. For any \(s\in S\), choose \(t\in T\) with \(t\to s\). Then either \(t=q\), or \(q\to t\to s\). ∎

# 4. The case without asymmetric backward cross-arcs

The main obstruction to simply choosing a weighted tournament king is stability: a stable vertex \(s\) not \(2\)-covered by \(q\) may still have an arc \(s\to q\). If such asymmetric arcs are excluded, the weighted argument works.

## Theorem 4.1

Assume that
\[
s\to t\quad\Longrightarrow\quad t\to s
\tag{4.1}
\]
for every \(s\in S,t\in T\). Then \(G\) has a strong \(2\)-kernel of size at most \(|G|/2\).

If \(r>0\), it in fact has one of size at most \(\lceil r/2\rceil\).

### Proof

For every \(s\in S\), choose \(p(s)\in T\) with \(p(s)\to s\). Such a vertex exists because \(G\) has no sources. Give \(t\in T\) weight
\[
w(t)=|\{s\in S:p(s)=t\}|.
\]
The total weight is \(r\).

Assume first that \(r>0\). By Lemma 2.1, there is a tournament \(2\)-king \(q\) such that
\[
w(N_T^-(q))<\frac r2.
\]
Let
\[
U=\{s\in S:\operatorname{dist}_G(q,s)>2\}.
\]
If \(s\in U\), then necessarily \(p(s)\to q\): if \(p(s)=q\), or \(q\to p(s)\), then \(q\to p(s)\to s\) has length at most two. Therefore
\[
|U|\le w(N_T^-(q))<\frac r2.
\]

For \(s\in U\), there is no arc \(q\to s\). By (4.1), there cannot be an arc \(s\to q\) either. Hence
\[
K=\{q\}\cup U
\]
is stable. The vertex \(q\) \(2\)-covers all of \(T\), every vertex of \(S\setminus U\) is \(2\)-covered by \(q\), and the vertices in \(U\) belong to \(K\). Thus \(K\) is strong.

Since \(|U|\) is an integer strictly smaller than \(r/2\),
\[
|K|\le \left\lceil\frac r2\right\rceil
\le \left\lfloor\frac{m+r}{2}\right\rfloor.
\]

If \(r=0\), then \(G\) is a source-free tournament, so \(m\ge3\); any tournament \(2\)-king is a strong \(2\)-kernel of size one. ∎

If the ambient convention forbids digons, condition (4.1) simply says that there are no arcs from \(S\) to \(T\). In particular, the conjecture holds for that one-way oriented case.

# 5. The conjecture for \(\boldsymbol{|T|\le3}\)

## Theorem 5.1

Every source-free split digraph with \(|T|\le3\) has a strong \(2\)-kernel of size at most \(|G|/2\).

### Proof

For \(|T|\le2\), the tournament has a source, so Proposition 3.4 applies. The same is true for a transitive tournament on three vertices.

It remains to consider a directed triangle. Write
\[
a\to b\to c\to a.
\]
If \(A=\varnothing\), Proposition 3.1 applies. Thus suppose \(A\ne\varnothing\), and relabel so that \(a\in A\).

For \(v\in T\), define
\[
U_v=\{s\in S:\operatorname{dist}_G(v,s)>2\}.
\]
Because \(a\in A\), no vertex of \(U_a\) is adjacent to \(a\): the arc \(a\to s\) is excluded by the definition of \(U_a\), while \(s\to a\) is excluded by \(a\in A\). Hence
\[
K_a=\{a\}\cup U_a
\]
is a strong \(2\)-kernel.

Put
\[
B=\left\lfloor\frac{r+3}{2}\right\rfloor.
\]
If \(1+|U_a|\le B\), we are done. Suppose instead that
\[
|U_a|\ge B.
\tag{5.1}
\]

A directed path of length at most two from \(a\) to a vertex of \(S\) can only use \(b\) as its intermediate tournament vertex. Thus, for every \(s\in U_a\),
\[
a\nrightarrow s,\qquad b\nrightarrow s.
\]
Since \(s\) is not a source, it follows that
\[
c\to s.
\tag{5.2}
\]

Similarly, if \(s\in U_c\), then
\[
c\nrightarrow s,\qquad a\nrightarrow s,
\]
and hence \(b\to s\). In particular, (5.2) implies
\[
U_a\cap U_c=\varnothing.
\tag{5.3}
\]

There are now two cases.

### Case 1: no vertex of \(U_c\) sends an arc to \(c\)

Then every member of \(U_c\) is nonadjacent to \(c\), so
\[
K_c=\{c\}\cup U_c
\]
is a strong \(2\)-kernel. By (5.1) and (5.3),
\[
|U_c|\le r-|U_a|\le r-B.
\]
Consequently,
\[
|K_c|\le1+r-B\le B.
\]

### Case 2: some \(x\in U_c\) satisfies \(x\to c\)

The set \(\{a,x\}\) is stable. Indeed, \(x\to a\) is impossible because \(a\in A\), while \(a\to x\) would give the path \(c\to a\to x\), contrary to \(x\in U_c\).

The vertex \(a\) \(2\)-covers the whole tournament. It also \(2\)-covers every vertex of \(S\setminus U_a\). Finally, for every \(s\in U_a\), (5.2) gives
\[
x\to c\to s.
\]
Thus \(\{a,x\}\) is a strong \(2\)-kernel. Since this case has \(r\ge1\), we have \(2\le B\).

This completes all cases. ∎

# 6. A quantitative bound for the mixed case

The following gives an additional family of instances satisfying the conjecture.

Let
\[
A=\{t\in T:N_G^-(t)\cap S=\varnothing\},\qquad
B=T\setminus A,
\]
and write \(a=|A|\), \(b=|B|\). Define
\[
C=\{s\in S:N_G^-(s)\cap A=\varnothing\},
\qquad c=|C|.
\]
Thus \(C\) consists of the stable vertices receiving no arc from \(A\).

## Proposition 6.1

Suppose \(A\ne\varnothing\) and \(r-c>0\). Then \(G\) has a strong \(2\)-kernel of size at most
\[
\min\left\{r+1,\;
b+c+\left\lceil\frac{r-c}{2}\right\rceil\right\}.
\tag{6.1}
\]

### Proof

For each \(s\in S\setminus C\), choose \(p(s)\in A\) with \(p(s)\to s\), and put
\[
w(a_0)=|\{s\in S\setminus C:p(s)=a_0\}|.
\]
The total weight on \(A\) is \(W=r-c>0\).

Apply Lemma 2.1 to \(G[A]\). We obtain a \(2\)-king \(q\in A\) with
\[
w(N_A^-(q))<\frac W2.
\]
Let
\[
H=\{s\in S\setminus C:\operatorname{dist}_G(q,s)>2\}.
\]
For \(s\in H\), the chosen parent satisfies \(p(s)\to q\); hence
\[
|H|\le w(N_A^-(q))
\le \left\lfloor\frac{W-1}{2}\right\rfloor.
\tag{6.2}
\]

For every \(t\in B\) not \(2\)-covered by \(q\), choose \(x_t\in S\) with \(x_t\to t\), and let \(R\) be the set of chosen vertices. Then \(|R|\le b\). Moreover, every \(x_t\) is nonadjacent to \(q\): the arc \(x_t\to q\) is impossible because \(q\in A\), and \(q\to x_t\) would give \(q\to x_t\to t\).

Every vertex of \(C\) is also nonadjacent to \(q\): neither direction is possible by the definitions of \(A\) and \(C\). The same holds for every vertex of \(H\). Therefore
\[
K=\{q\}\cup C\cup H\cup R
\]
is stable.

The vertex \(q\) \(2\)-covers \(A\); each vertex of \(B\) is either \(2\)-covered by \(q\), or directly covered by \(R\). Every vertex of \(C\cup H\) belongs to \(K\), and every vertex of \(S\setminus(C\cup H)\) is \(2\)-covered by \(q\). Thus \(K\) is strong.

Using (6.2),
\[
\begin{aligned}
|K|
&\le 1+c+b+\left\lfloor\frac{W-1}{2}\right\rfloor\\
&=b+c+\left\lceil\frac W2\right\rceil.
\end{aligned}
\]
Combining this with Proposition 3.2 proves (6.1). ∎

For example, if
\[
\delta\equiv r-c\pmod 2,\qquad
\varepsilon\equiv m+r\pmod2,
\]
then the second bound in (6.1) is at most \(\lfloor(m+r)/2\rfloor\) whenever
\[
a\ge b+c+\delta+\varepsilon.
\]

# 7. What remains

The arguments above leave only a genuinely mixed regime. Any counterexample must satisfy at least all of the following:

- \(A\ne\varnothing\), since \(A=\varnothing\) is Proposition 3.1;
- \(A\ne T\), since \(A=T\) is covered by Theorem 4.1;
- \(G[T]\) has no source;
- \(m\ge4\);
- \(m\le r+1\);
- there is an asymmetric cross-arc \(s\to t\) with no reverse arc \(t\to s\);
- every \(2\)-king \(q\) of \(G[A]\) has too few out-neighbours in \(S\) to satisfy the threshold after Proposition 3.2;
- the quantitative bound in Proposition 6.1 must also exceed \(\lfloor(m+r)/2\rfloor\).

The precise obstruction to extending Theorem 4.1 is the following. The weighted tournament lemma still produces a tournament \(2\)-king \(q\) for which fewer than \(r/2\) stable vertices fail to be \(2\)-covered by \(q\). However, such an uncovered vertex may have an asymmetric arc \(s\to q\). Then it cannot be added to a stable set containing \(q\). The constructions through \(A\) avoid this stability problem, but currently lose too much in the residual vertices \(T\setminus A\).

Thus the general asymmetric mixed case is not resolved by the present argument.