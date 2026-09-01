```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but the sharp 3^(2t/3) exponent is proved for complete multipartite pieces and, in another direction, for pieces whose complements have maximum degree at most two.",
  "would_publish": false,
  "caveats": "No improved bound is obtained for arbitrary graphs, and I have not verified whether these elementary special cases already appear in the literature."
}
```

## 1. Statement and notation

Write \(\tau(G)\) for the largest \(s\) such that \(G\) contains a subdivision of \(K_s\), and let \(\kappa(G)\) denote the number of cliques of \(G\), including the empty clique. Changing the convention about the empty clique only changes all estimates by one.

The catalogued conjecture is not proved here. I prove the following special cases.

### Partial theorem

Let \(t\ge 3\).

1. If \(\Delta(\overline G)\le 2\) and \(\tau(G)<t\), then
   \[
   \kappa(G)<3^{2(t+2)/3}.
   \]
   Consequently, if every connected component \(Q\) of an \(n\)-vertex graph satisfies \(\Delta(\overline Q)\le2\), then
   \[
   \kappa(G)\le 1+n\,3^{2(t+2)/3}.
   \]

2. If \(G\) is complete multipartite and \(\tau(G)<t\), then
   \[
   \kappa(G)<2|V(G)|\,3^{2t/3}.
   \]
   Consequently, if every connected component of an \(n\)-vertex graph is complete multipartite, then
   \[
   \kappa(G)\le 1+2n\,3^{2t/3}.
   \]

Both classes contain the standard cocktail-party lower-bound construction, so the exponent \(2t/3\) is sharp in both special cases.

## 2. Two elementary tools

### Routing observation

Let \(B\subseteq V(G)\). Suppose every nonedge \(uv\) of \(G[B]\) can be assigned a distinct vertex \(x_{uv}\in V(G)\setminus B\) adjacent in \(G\) to both \(u\) and \(v\). Then \(G\) contains a subdivision of \(K_{|B|}\): use the edge \(uv\) when it exists, and the path \(u x_{uv}v\) otherwise.

### Rounding lemma

Let \(d_1,\dots,d_m>0\) and \(0\le\theta_i<1\). There is a set \(J\subseteq[m]\) such that
\[
\sum_{i\in J}d_i\le \sum_i\theta_i d_i
\qquad\text{and}\qquad
|J|\ge \left\lfloor\sum_i\theta_i\right\rfloor.
\]

Indeed, maximize \(\sum x_i\) subject to \(0\le x_i\le1\) and
\[
\sum d_i x_i\le\sum d_i\theta_i.
\]
The given fractional vector is feasible. An extreme optimal solution has at most one fractional coordinate; rounding that coordinate down loses less than one in the objective.

## 3. Complements of maximum degree two

Let
\[
H=\overline G,\qquad \Delta(H)\le2.
\]
Then the components of \(H\) are paths and cycles, and
\[
\kappa(G)=i(H),
\]
where \(i(H)\) is the number of independent sets of \(H\).

### 3.1. Branch-set profiles

For a component \(D\) of \(H\), define
\[
c_D(b)=\min_{\substack{X\subseteq V(D)\\|X|=b}}
\bigl(|X|+e_D(X)\bigr).
\]
The term \(e_D(X)\) is the number of missing branch edges that would need internal routing vertices.

For a path \(P_\ell\), a binary-string/run argument gives
\[
\min_{|X|=b}e_{P_\ell}(X)
 =\max\{0,\,2b-\ell-1\},
\]
and hence
\[
c_{P_\ell}(b)=b+\max\{0,\,2b-\ell-1\}.             \tag{1}
\]
Indeed, if \(X\) has \(b\) vertices and \(\ell-b\) omitted vertices, the selected vertices form at most \(\ell-b+1\) runs, and each run of length \(s\) contributes \(s-1\) edges.

Similarly, for a cycle \(C_\ell\),
\[
\min_{|X|=b}e_{C_\ell}(X)
 =\max\{0,\,2b-\ell\},
\]
so
\[
c_{C_\ell}(b)=b+\max\{0,\,2b-\ell\}.               \tag{2}
\]

Define
\[
\begin{aligned}
\beta(P_1)&=1,\\
\beta(P_2)&=\frac32,\\
\beta(P_\ell)&=\frac{2\ell+1}{3}\quad(\ell\ge3),\\
\beta(C_\ell)&=\frac{2\ell}{3}\quad(\ell\ge3).
\end{aligned}                                      \tag{3}
\]

If \(r=\lfloor\beta(D)\rfloor\) and \(\theta=\beta(D)-r\), equations (1) and (2) imply
\[
|V(D)|=c_D(r)+\theta\bigl(c_D(r+1)-c_D(r)\bigr),    \tag{4}
\]
with the evident interpretation when \(\theta=0\).

Let
\[
S(H)=\sum_{D\in\operatorname{comp}(H)}\beta(D).
\]

Applying the rounding lemma to the possible upgrades \(r\to r+1\) in (4), and taking minimum-cost sets of the selected sizes, gives a set \(B_0\subseteq V(H)\) such that
\[
|B_0|\ge\lfloor S(H)\rfloor
\quad\text{and}\quad
|B_0|+e_H(B_0)\le |V(H)|.                           \tag{5}
\]

### 3.2. Independent-set count versus the profile

I claim that each path or cycle component satisfies
\[
i(D)\le 3^{2\beta(D)/3}.                            \tag{6}
\]

For \(P_1\) and \(P_2\), this is
\[
2\le3^{2/3},\qquad 3=3^{2(3/2)/3}.
\]

For \(\ell\ge3\),
\[
i(P_\ell)=F_{\ell+2},
\]
where \(F_0=0,F_1=1\). Set
\[
\rho=3^{4/9},\qquad A=3^{2/9}.
\]
Then the desired path bound is
\[
F_{\ell+2}\le A\rho^\ell.
\]
It holds for \(\ell=3\) because
\[
5<3^{14/9},
\]
and for \(\ell=4\) because \(8<9\). Moreover \(\rho>\varphi\), where \(\varphi^2=\varphi+1\): indeed
\[
\rho^9=81,
\qquad
\varphi^9=34\varphi+21<34\cdot\frac53+21<81.
\]
Thus \(\rho^2>\rho+1\), and the Fibonacci recurrence proves the estimate for all \(\ell\ge3\).

For cycles,
\[
i(C_\ell)=F_{\ell-1}+F_{\ell+1},
\]
and these numbers obey the same recurrence. The required estimate is
\[
i(C_\ell)\le \rho^\ell.
\]
The initial cases are
\[
i(C_3)=4<3^{4/3}=\rho^3
\]
and
\[
i(C_4)=7<3^{16/9}=\rho^4;
\]
the latter is equivalently
\[
7^9=40\,353\,607<43\,046\,721=3^{16}.
\]
The recurrence and \(\rho^2>\rho+1\) complete the proof of (6).

Since independent-set counts multiply over components,
\[
\kappa(G)=i(H)
 =\prod_D i(D)
 \le 3^{2S(H)/3}.                                  \tag{7}
\]

### 3.3. Routing the missing edges

Take \(B_0\) from (5), put \(b_0=|B_0|\), and let \(q_0=e_H(B_0)\). Thus
\[
b_0+q_0\le n.
\]

Remove two arbitrary vertices from \(B_0\), provided \(b_0\ge2\), and call the remaining set \(B\). Put
\[
b=|B|,\qquad q=e_H(B),\qquad R=V(H)\setminus B.
\]
Then
\[
|R|-q=n-b-q\ge2.                                   \tag{8}
\]

The missing branch pairs are the edges \(uv\in E(H[B])\). A router \(x\in R\) is unsuitable for \(uv\) only if \(xu\in E(H)\) or \(xv\in E(H)\). Since \(uv\in E(H)\) already uses one incident edge at each endpoint and \(\Delta(H)\le2\), at most two routers are unsuitable for any given pair \(uv\). By (8), each missing pair therefore has at least
\[
|R|-2\ge q
\]
eligible routers.

Hall's condition now follows immediately: for any nonempty collection \(X\) of missing pairs, the union of their eligible-router sets contains the eligible set of one member and hence has size at least \(q\ge|X|\). Thus all missing pairs have distinct routers, and the routing observation gives
\[
\tau(G)\ge \lfloor S(H)\rfloor-2.                   \tag{9}
\]

If \(\tau(G)<t\), then (9) gives
\[
\lfloor S(H)\rfloor\le t+1,
\qquad\text{hence}\qquad
S(H)<t+2.
\]
Together with (7),
\[
\boxed{\kappa(G)<3^{2(t+2)/3}}.                     \tag{10}
\]

For a disjoint union \(G=G_1\cup\cdots\cup G_m\),
\[
\kappa(G)=1+\sum_{j=1}^m\bigl(\kappa(G_j)-1\bigr).
\]
Thus, if every connected component has complement of maximum degree at most two,
\[
\kappa(G)\le1+m\,3^{2(t+2)/3}
          \le1+n\,3^{2(t+2)/3}.
\]

## 4. Complete multipartite graphs

Let
\[
G=K_{a_1,\dots,a_m},
\qquad
a_1\ge a_2\ge\cdots\ge a_m\ge1,
\qquad
n=\sum_i a_i.
\]
Its clique count is
\[
\kappa(G)=\prod_{i=1}^m(a_i+1).                    \tag{11}
\]

Put
\[
T_r=\binom{r+1}{2}.
\]
For \(a\ge1\), let \(r\) be determined by
\[
T_r\le a<T_{r+1},
\]
and define
\[
\lambda(a)=r+\frac{a-T_r}{r+1}.                    \tag{12}
\]

### 4.1. The local numerical inequality

For every integer \(a\ge1\),
\[
a+1\le 3^{2\lambda(a)/3}.                           \tag{13}
\]

Equivalently, with
\[
\gamma=\frac{3}{2\log 3},
\]
we need
\[
\lambda(a)\ge\gamma\log(a+1).
\]

For \(a=1,\dots,5\), the values of \(\lambda(a)\) are
\[
1,\ \frac32,\ 2,\ \frac73,\ \frac83,
\]
and (13) becomes
\[
2\le3^{2/3},\quad
3=3,\quad
4\le3^{4/3},\quad
5\le3^{14/9},\quad
6\le3^{16/9},
\]
all immediate.

Now let \(r\ge3\) and \(x\in[T_r,T_{r+1}]\). Define
\[
f_r(x)=r+\frac{x-T_r}{r+1}-\gamma\log(x+1).
\]
Since \(\gamma<3/2\) and
\[
\frac{T_r+1}{r+1}=\frac r2+\frac1{r+1}\ge\frac74,
\]
we have \(f_r'(x)>0\).

It remains to check \(f_r(T_r)\ge0\), equivalently
\[
T_r+1\le3^{2r/3}.                                   \tag{14}
\]
For \(r=3\), this is \(7\le9\). Moreover, for \(r\ge3\),
\[
T_{r+1}+1<2(T_r+1)
\]
and \(2<3^{2/3}\), so (14) follows by induction. This proves (13).

### 4.2. Constructing a large topological clique

Set
\[
S=\sum_{i=2}^m\lambda(a_i).
\]
We reserve the largest part \(V_1\) entirely for routing.

For each \(i\ge2\), write
\[
\lambda(a_i)=r_i+\theta_i,
\qquad
\theta_i=\frac{a_i-T_{r_i}}{r_i+1}.
\]
Choosing \(r_i\) branch vertices in part \(i\) has cost
\[
r_i+\binom{r_i}{2}=T_{r_i}.
\]
Upgrading to \(r_i+1\) branch vertices increases the cost by \(r_i+1\).

The fractional upgrades \(\theta_i\) use precisely the residual budget
\[
\sum_{i=2}^m(a_i-T_{r_i}).
\]
By the rounding lemma, we can choose integral upgrades so that the resulting integers \(b_i\in\{r_i,r_i+1\}\) satisfy
\[
B:=\sum_{i=2}^m b_i\ge\lfloor S\rfloor
\]
and
\[
\sum_{i=2}^m\left(b_i+\binom{b_i}{2}\right)
 \le\sum_{i=2}^m a_i=n-a_1.                        \tag{15}
\]

Let
\[
q_i=\binom{b_i}{2},
\qquad q=\sum_{i=2}^m q_i.
\]
The missing branch pairs are precisely the \(q_i\) pairs lying in the same multipartite part. By (15), the number \(U=n-B\) of unused vertices satisfies
\[
U\ge q+a_1.                                         \tag{16}
\]

Furthermore,
\[
q_i\le a_i\le a_1.                                  \tag{17}
\]
Indeed, if \(b_i=r_i\), then \(q_i=\binom{r_i}{2}\le a_i\); if \(b_i=r_i+1\), then \(q_i=T_{r_i}\le a_i\).

Construct a bipartite graph whose left side consists of the missing branch pairs, and whose right side consists of unused vertices; a pair in part \(i\) is adjacent to all unused vertices outside part \(i\). Hall's condition holds:

- for jobs all belonging to one part \(i\), there are at least \(a_1\ge q_i\) eligible vertices, by (17);
- if jobs from at least two different parts occur, their combined neighborhood is all \(U\) unused vertices, and \(U\ge q\) by (16).

Thus every missing pair receives a distinct router, and
\[
\tau(G)\ge\lfloor S\rfloor.                         \tag{18}
\]

If \(\tau(G)<t\), then \(S<t\). Using (13),
\[
\prod_{i=2}^m(a_i+1)
 \le 3^{2S/3}
 <3^{2t/3}.
\]
Since \(a_1+1\le2a_1\le2n\), equation (11) yields
\[
\boxed{\kappa(G)<2n\,3^{2t/3}}.                     \tag{19}
\]

Summing (19) over connected components proves the componentwise complete multipartite assertion.

## 5. Sharpness in both special classes

Let
\[
J_k=K_{\underbrace{2,\dots,2}_{k\text{ parts}}},
\]
the cocktail-party graph on \(2k\) vertices. It has
\[
\kappa(J_k)=3^k,
\]
because a clique chooses either no vertex or one of two vertices from each part.

I record its exact topological clique number:
\[
\tau(J_k)=\left\lfloor\frac{3k}{2}\right\rfloor.    \tag{20}
\]

For the upper bound, suppose a subdivision has \(b\) branch vertices, and let \(r\) be the number of parts containing both of their vertices as branch vertices. Those \(r\) nonadjacent branch pairs each require at least one distinct internal vertex, so
\[
r\le2k-b.
\]
Also \(b\le k+r\), since each of the \(k\) parts contributes at most one branch vertex before the \(r\) doubled contributions. Hence
\[
b\le k+r\le3k-b,
\]
so \(b\le\lfloor3k/2\rfloor\).

For the matching lower bound, double \(\lfloor k/2\rfloor\) parts and choose one branch vertex from every other part. The unused mates in the singly occupied parts route the doubled pairs.

Choose
\[
k=\left\lceil\frac{2t}{3}\right\rceil-1,
\]
so \(k<2t/3\) and \(\tau(J_k)<t\). A disjoint union of \(q\) copies has \(n=2kq\) vertices and
\[
\kappa(G)=1+q(3^k-1).
\]
Thus its number of nonempty cliques per vertex is
\[
\frac{3^k-1}{2k}
 =3^{2t/3-O(\log t)}
 =3^{2t/3+o(t)}.
\]
The graph \(J_k\) is complete multipartite and its complement is a matching, so the exponent in both partial theorems is best possible.

## 6. A minor extension by block decomposition

The same \(3^{2t/3+O(1)}n\) conclusion holds for graphs whose blocks are, in any mixture,

- complete multipartite graphs, or
- graphs whose complements have maximum degree at most two.

Indeed, a subdivision of \(K_t\), \(t\ge3\), is 2-connected and hence lies in one block. Every clique of size at least two also lies in one block. Finally,
\[
\sum_{\text{blocks }B}(|B|-1)\le n,
\]
so both the number of blocks and the sum of their orders are \(O(n)\). Summing the two bounds above therefore preserves the conjectured exponential constant.

## 7. Gap to the full conjecture

The argument does not extend directly to arbitrary graphs. Its essential feature is that a scalar budget
\[
|B|+e_{\overline G}(B)\le n
\]
can be converted into internally disjoint length-two routes.

For \(\Delta(\overline G)\le2\), each missing branch pair forbids at most two routers. For complete multipartite graphs, the missing pairs have a rigid type structure and Hall's condition can be checked exactly. In a general graph, a missing pair may have no common neighbor outside the branch set, even when the total number of unused vertices exceeds the number of missing pairs. Thus the numerical budget alone is insufficient.

Accordingly, this gives no improvement over the source paper's general \(2^{1.817t+o(t)}n\) upper bound and does not resolve the catalogued conjecture.