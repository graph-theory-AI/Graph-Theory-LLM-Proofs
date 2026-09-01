```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem remains open for d at least 2, but failure forces the sharp bound χ_f(G)≤2d+1, the case d=1 has exact threshold 4, and a hypothetical d=2 counterexample must have very large girth and order.",
  "would_publish": false,
  "caveats": "No bound on ordinary chromatic number is obtained for d≥2, and some elementary observations may be implicit in the source paper."
}
```

# 1. Statement and notation

Fix \(d\geq 1\). Write \(\operatorname{deg}(H)\) for the degeneracy of a graph \(H\). Consider the negation of the desired conclusion:

\[
\tag{\(\mathcal P_d\)}
\operatorname{deg}\bigl(G[N_T^+(v)]\bigr)\le d-1
\qquad\text{for every }v\in V(G).
\]

The question is whether \((\mathcal P_d)\) forces \(\chi(G)\) to be bounded as a function of \(d\).

I do not resolve this for \(d\ge2\). The results below give:

1. a sharp fractional-chromatic version;
2. the exact answer for \(d=1\);
3. a domination-number reformulation and quantitative obstruction;
4. strong girth and order restrictions when \(d=2\);
5. an exact positive answer for perfect graphs.

# 2. A sharp fractional-chromatic bound

## Theorem 2.1

If \(G,T\) satisfy \((\mathcal P_d)\), then

\[
\chi_f(G)\le 2d+1.
\]

This is sharp for every \(d\ge1\).

### Proof

Let \(A\) be the skew-symmetric matrix of \(T\), indexed by \(V(T)\), with

\[
A_{xy}=
\begin{cases}
1,&x\to y,\\
-1,&y\to x,\\
0,&x=y.
\end{cases}
\]

By the finite minimax theorem, there is a probability distribution
\(p=(p_x:x\in V(T))\) such that

\[
p^{\mathsf T}A e_x\ge0
\qquad\text{for every }x.
\]

Indeed, the value of the zero-sum game with payoff matrix \(A\) is zero: for every probability vector \(q\),

\[
q^{\mathsf T}Aq=0
\]

by skew-symmetry.

For fixed \(x\), put

\[
a_x=\sum_{v:\,v\to x}p_v,
\qquad
b_x=\sum_{v:\,x\to v}p_v.
\]

Then \(a_x-b_x=p^{\mathsf T}Ae_x\ge0\), while

\[
a_x+b_x=1-p_x.
\]

Consequently,

\[
\tag{1}
a_x\ge \frac{1-p_x}{2}.
\]

By \((\mathcal P_d)\), each graph \(G[N_T^+(v)]\) is \(d\)-colorable. Fix a partition

\[
N_T^+(v)=I_{v,1}\cup\cdots\cup I_{v,d}
\]

into independent sets, allowing empty parts.

Give each \(I_{v,i}\) fractional weight \(2p_v\). In addition, give each singleton \(\{x\}\) weight \(p_x\). The total weight is

\[
\sum_v\sum_{i=1}^d 2p_v+\sum_xp_x
=2d+1.
\]

A vertex \(x\) receives weight \(2p_v\) once for every \(v\to x\), and receives singleton weight \(p_x\). Its total coverage is therefore

\[
2\sum_{v:\,v\to x}p_v+p_x
=2a_x+p_x
\overset{(1)}{\ge}1.
\]

Thus these weighted independent sets form a fractional coloring of total weight \(2d+1\). Hence

\[
\chi_f(G)\le2d+1.\qedhere
\]

## Sharpness

Let \(G=K_{2d+1}\), and let \(T\) be the cyclic regular tournament on
\(\mathbb Z/(2d+1)\mathbb Z\), where

\[
i\to j
\quad\Longleftrightarrow\quad
j-i\pmod{2d+1}\in\{1,\dots,d\}.
\]

Every vertex has exactly \(d\) out-neighbours. Therefore

\[
G[N_T^+(v)]\cong K_d,
\]

whose degeneracy is \(d-1\). Thus \((\mathcal P_d)\) holds, while

\[
\chi_f(G)=2d+1.
\]

Consequently,

\[
\sup\{\chi_f(G):(G,T)\text{ satisfies }(\mathcal P_d)\}=2d+1.
\]

In particular, the fractional analogue of the question is completely settled:

\[
\chi_f(G)>2d+1
\quad\Longrightarrow\quad
\exists v\ \operatorname{deg}(G[N_T^+(v)])\ge d.
\]

The same example shows that any integer threshold in the original question, if it exists, must satisfy

\[
\boxed{\chi(d)\ge2d+2.}
\]

# 3. Tournament domination and \(d\)-cores

Let \(\gamma(T)\) denote the domination number of \(T\): the minimum size of a set \(D\) such that every vertex outside \(D\) is beaten by some vertex of \(D\).

## Proposition 3.1

If \(G,T\) satisfy \((\mathcal P_d)\), then

\[
\boxed{\chi(G)\le d\,\gamma(T)+1.}
\]

### Proof

Let \(D\) be a dominating set of \(T\), and put

\[
U=\bigcup_{s\in D}N_T^+(s).
\]

Assign every vertex of \(U\) to one chosen \(s\in D\) which beats it. This partitions \(U\) into sets \(U_s\subseteq N_T^+(s)\). Each \(G[U_s]\) is \(d\)-colorable, so, using disjoint palettes for distinct \(s\), \(G[U]\) is \(d|D|\)-colorable.

Since \(D\) dominates every vertex outside \(D\), the set \(V(G)\setminus U\) is contained in \(D\). Moreover, a vertex of \(D\setminus U\) has no in-neighbour in \(T[D]\), so it is a source of \(T[D]\). A tournament has at most one source. Hence

\[
|V(G)\setminus U|\le1.
\]

One additional color proves

\[
\chi(G)\le d|D|+1.
\]

Minimizing over \(D\) gives the assertion. \(\square\)

As every \(n\)-vertex tournament has a dominating set of order at most
\(\lceil\log_2(n+1)\rceil\), this also gives the finite-order estimate

\[
\chi(G)\le d\lceil\log_2(|V(G)|+1)\rceil+1
\]

under \((\mathcal P_d)\).

## Proposition 3.2

Suppose \(S\subseteq V(G)\) satisfies

\[
\delta(G[S])\ge d.
\]

If \((G,T)\) satisfies \((\mathcal P_d)\), then \(S\) is a dominating set of \(T\).

### Proof

If \(S\) did not dominate \(T\), some \(v\notin S\) would beat every vertex of \(S\). Then

\[
S\subseteq N_T^+(v),
\]

and hence \(G[N_T^+(v)]\) would contain the subgraph \(G[S]\) of minimum degree at least \(d\). Its degeneracy would therefore be at least \(d\), contradicting \((\mathcal P_d)\). \(\square\)

Define the \(d\)-core order

\[
s_d(G)=\min\{|S|:\delta(G[S])\ge d\},
\]

when such a set exists. Combining Propositions 3.1 and 3.2 gives:

## Corollary 3.3

If \((G,T)\) satisfies \((\mathcal P_d)\) and \(k=\chi(G)\), then

\[
\gamma(T)\ge \left\lceil\frac{k-1}{d}\right\rceil
\]

and

\[
\boxed{s_d(G)\ge \left\lceil\frac{k-1}{d}\right\rceil.}
\]

Equivalently, if \(G\) contains a \(d\)-core on \(r\) vertices and

\[
\chi(G)\ge dr+2,
\]

then the desired out-neighbourhood necessarily exists.

Thus any counterexample sequence with unbounded chromatic number must simultaneously have linearly growing tournament domination number and linearly growing smallest \(d\)-core.

# 4. Exact solution for \(d=1\)

For \(d=1\), condition \((\mathcal P_1)\) says that every
\(G[N_T^+(v)]\) is edgeless.

## Theorem 4.1

The least threshold for \(d=1\) is

\[
\boxed{\chi(1)=4.}
\]

### Proof

Assume \((\mathcal P_1)\). If \(G\) has an edge \(xy\), then
\(\delta(G[\{x,y\}])=1\). Proposition 3.2 says that \(\{x,y\}\) dominates \(T\). Hence \(\gamma(T)\le2\), and Proposition 3.1 gives

\[
\chi(G)\le 1\cdot2+1=3.
\]

Thus every graph with \(\chi(G)\ge4\) has a vertex \(v\) for which
\(G[N_T^+(v)]\) contains an edge, i.e. has degeneracy at least \(1\).

Sharpness is given by \(G=K_3\) and a directed \(3\)-cycle \(T\). Every out-neighbourhood has one vertex and is edgeless, while \(\chi(G)=3\). \(\square\)

A direct version of the same argument is instructive. If \(x\to y\) and \(xy\in E(G)\), then no third vertex can beat both \(x\) and \(y\). Thus

\[
V(G)\setminus\{x\}\subseteq N_T^+(x)\cup N_T^+(y).
\]

Both out-neighbourhoods are independent in \(G\), so \(G-x\) is bipartite and \(G\) is \(3\)-colorable.

# 5. The case \(d=2\): girth and order restrictions

Under \((\mathcal P_2)\), every out-neighbourhood induces a forest.

Every cycle of \(G\) is a \(2\)-core. Proposition 3.2 therefore implies that every cycle is a dominating set of \(T\).

## Proposition 5.1

If \((G,T)\) satisfies \((\mathcal P_2)\) and \(\chi(G)=k\), then

\[
\boxed{\operatorname{girth}(G)\ge
\left\lceil\frac{k-1}{2}\right\rceil}
\]

whenever \(G\) contains a cycle.

### Proof

By Proposition 3.1,

\[
k\le2\gamma(T)+1,
\]

so

\[
\gamma(T)\ge\left\lceil\frac{k-1}{2}\right\rceil.
\]

Every cycle is a dominating set and consequently has length at least
\(\gamma(T)\). \(\square\)

Thus an unbounded-chromatic counterexample for \(d=2\) would necessarily be an unbounded-girth family.

There is also a substantial lower bound on its order.

## Proposition 5.2

Let \(k\ge6\). If a graph \(G\) of chromatic number \(k\), together with a tournament \(T\), satisfies \((\mathcal P_2)\), then, with

\[
r=\left\lfloor\frac{k-2}{4}\right\rfloor,
\]

one has

\[
\boxed{
|V(G)|
\ge
1+(k-1)\sum_{i=0}^{r-1}(k-2)^i
\ge (k-2)^r.
}
\]

In particular,

\[
|V(G)|\ge
\exp\!\left(\left(\frac14+o(1)\right)k\log k\right).
\]

### Proof

Take a \(k\)-critical subgraph \(H\subseteq G\). Then

\[
\delta(H)\ge k-1.
\]

The restricted pair \((H,T[V(H)])\) still satisfies \((\mathcal P_2)\), so Proposition 5.1 gives

\[
\operatorname{girth}(H)\ge
\left\lceil\frac{k-1}{2}\right\rceil.
\]

The choice of \(r\) ensures

\[
2r<
\left\lceil\frac{k-1}{2}\right\rceil.
\]

Consequently, a breadth-first search tree in \(H\), rooted at any vertex and continued to depth \(r\), has no collisions: any collision would create a cycle of length at most \(2r\). The root has at least \(k-1\) children, and every subsequent non-leaf vertex has at least \(k-2\) new children. Hence

\[
|V(H)|
\ge
1+(k-1)\sum_{i=0}^{r-1}(k-2)^i.
\]

Since \(H\subseteq G\), the same lower bound holds for \(G\). \(\square\)

This does not rule out counterexamples, since high-girth, high-chromatic graphs can have extremely large order, but it sharply constrains any finite search.

# 6. Perfect graphs and related special cases

## Corollary 6.1

For perfect graphs, the optimal threshold is

\[
\boxed{2d+2.}
\]

### Proof

If \(G\) is perfect and \((G,T)\) satisfies \((\mathcal P_d)\), then

\[
\chi(G)=\omega(G)\le\chi_f(G)\le2d+1.
\]

Thus \(\chi(G)\ge2d+2\) forces the desired out-neighbourhood. Sharpness follows from \(K_{2d+1}\) with the regular tournament used above. \(\square\)

More generally, the same conclusion holds for any individual graph satisfying \(\chi(G)=\chi_f(G)\).

# 7. Why the fractional bound does not settle the problem

The gap between \(\chi\) and \(\chi_f\) can be unbounded, even in a completely explicit family.

Let \(S_n\) be the shift graph with vertex set

\[
\{(i,j):1\le i<j\le n\},
\]

where \((i,j)\) is adjacent to \((j,k)\) whenever \(i<j<k\).

If \(S_n\) has a proper \(q\)-coloring \(c\), define

\[
C_i=\{c(i,j):j>i\}.
\]

For \(i<j\), the color \(c(i,j)\) belongs to \(C_i\), but it does not belong to \(C_j\), since \((i,j)\) is adjacent to every \((j,k)\). Thus the \(C_i\) are \(n\) distinct subsets of a \(q\)-element set, and therefore

\[
\chi(S_n)\ge\log_2 n.
\]

On the other hand, for each \(A\subseteq[n]\), let

\[
I_A=\{(i,j):i\in A,\ j\notin A\}.
\]

Each \(I_A\) is independent: two consecutive pairs \((i,j),(j,k)\) cannot both belong to \(I_A\). Every vertex belongs to exactly \(2^{n-2}\) of these independent sets. Giving every \(I_A\) weight \(2^{2-n}\) yields a fractional coloring of total weight \(4\). Hence

\[
\chi_f(S_n)\le4
\quad\text{while}\quad
\chi(S_n)\to\infty.
\]

This family is not asserted to admit a tournament satisfying
\((\mathcal P_d)\). It only shows that the sharp inequality
\(\chi_f(G)\le2d+1\) cannot by itself control ordinary chromatic number, already for \(d\ge2\).

# 8. Remaining gap

The original question is therefore settled here only for \(d=1\), and for classes such as perfect graphs. For \(d\ge2\), a counterexample with chromatic number \(k\) would have to satisfy all of the following:

\[
\chi_f(G)\le2d+1,
\]

\[
\gamma(T)\ge\left\lceil\frac{k-1}{d}\right\rceil,
\]

and

\[
s_d(G)\ge\left\lceil\frac{k-1}{d}\right\rceil.
\]

For \(d=2\), it would additionally have girth at least
\(\lceil(k-1)/2\rceil\) and order at least
\(\exp((1/4+o(1))k\log k)\).

These conditions are substantial but not contradictory. I have neither obtained a bounded coloring theorem from them nor constructed a tournament/graph family meeting them with unbounded chromatic number. Thus the case \(d\ge2\) remains open.