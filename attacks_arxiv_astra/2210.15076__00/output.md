```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact eventual finite-core reduction holds for general H, and a closed formula is obtained for K_{2,t} when s >= 12 and n is explicitly large.",
  "would_publish": false,
  "caveats": "This is not an all-parameter structural classification; overlap with the exact results in the listed follow-ups has not been verified."
}
```

## 1. Scope and notation

Write
\[
f_H(n,s)=\max\{e(G): |V(G)|=n,\ G\text{ is }H\text{-free},\ \nu(G)\le s\}.
\]
Graphs are simple, and forbidden copies are ordinary, not necessarily induced, subgraphs.

I give two rigorous partial results:

1. **For every fixed \(H,s\), an exact eventual affine formula**, with its constant term expressed as an explicitly bounded finite optimization.
2. **A closed formula for the non-color-critical family \(H=K_{2,t}\)**:
   \[
   \boxed{
   f_{K_{2,t}}(n,s)
   =n+(t-1)\binom{s}{2}-\left\lceil\frac s2\right\rceil
   }
   \]
   whenever \(t\ge2\), \(s\ge12\), and
   \[
   n\ge (2t-1)\binom{2s}{2}+2.
   \]

I have not verified whether the second result, or parts of the first, are among the exact results mentioned in the catalog. Thus no novelty claim is made.

Assume throughout that \(H\) has at least one edge. If \(H\) is edgeless on \(h\) vertices, there are no \(H\)-free graphs of order at least \(h\). Also, \(s=0\) gives \(f_H(n,0)=0\), so below \(s\ge1\).

---

## 2. An exact eventual finite-core theorem

Let \(h=|V(H)|\). Define
\[
q(H)=
\begin{cases}
\min\{|A|:(A,B)\text{ is a bipartition of }H\},&H\text{ bipartite},\\
\infty,&H\text{ nonbipartite}.
\end{cases}
\]
The minimum allows independent choices of orientation in different components. Set
\[
a=\min\{s,q(H)-1\},
\]
with \(a=s\) when \(q(H)=\infty\).

For a graph \(Q\) and \(S\subseteq V(Q)\), let \(Q^{S,h}\) be obtained by adjoining \(h\) independent vertices, each with neighborhood exactly \(S\).

### Theorem 1

Put
\[
k=2s-a,\qquad
B=k+(h-1)\binom{k}{a+1},
\]
where the binomial coefficient is zero when \(a+1>k\).

Let \(\mathcal C(H,s)\) consist of pairs \((Q,S)\) satisfying
\[
|S|=a,\qquad |V(Q)|\le B,
\]
\[
\nu(Q-S)\le s-a,
\qquad
Q^{S,h}\text{ is }H\text{-free}.
\]
Define
\[
\beta(H,s)=
\max_{(Q,S)\in\mathcal C(H,s)}
\bigl(e(Q)-a|V(Q)|\bigr).
\]

This is a nonempty finite optimization. Moreover, with
\[
L=\max\{h,s+1\},
\]
\[
D=\binom{2s}{2}+2s(L-1)2^{2s},
\]
and
\[
N=\max\left\{
B,\;
2s+(L-1)2^{2s}+1,\;
D+a^2+1
\right\},
\]
we have
\[
\boxed{f_H(n,s)=an+\beta(H,s)\qquad(n\ge N).}
\]

The important feature is that both the optimization and the threshold are bounded independently of \(n\).

### Proof

#### Step 1: A large repeated neighborhood in an extremal graph

The endpoints of a maximum matching form a vertex cover. Thus every graph with matching number at most \(s\) has a vertex cover of size at most \(2s\).

Take an extremal \(G\) of order \(n\ge N\), and extend such a cover to a set \(C\) of exactly \(2s\) vertices. Then \(I=V(G)\setminus C\) is independent. Partition \(I\) according to the neighborhood in \(C\).

A neighborhood class of size at least \(L\) cannot have degree greater than \(a\):

- If \(a=s\), a class with at least \(s+1\) vertices and at least \(s+1\) neighbors contains a matching of size \(s+1\).
- If \(a<s\), then \(H\) is bipartite and \(q(H)=a+1\). Since
  \[
  H\subseteq K_{a+1,h},
  \]
  a class with at least \(h\) vertices and at least \(a+1\) neighbors contains \(H\).

I claim that some class of degree exactly \(a\) has size at least \(L\).

First suppose \(a\ge1\), and no such class exists. Every class of degree at least \(a\) then has at most \(L-1\) vertices. There are at most \(2^{2s}\) classes, so
\[
\begin{aligned}
e(G)
&\le \binom{2s}{2}+(a-1)|I|
       +2s(L-1)2^{2s}\\
&\le (a-1)n+D.
\end{aligned}
\]
On the other hand, \(K_{a,n-a}\) is feasible: it has matching number at most \(a\le s\), and it cannot contain \(H\), by the definition of \(q(H)\). Consequently
\[
e(G)\ge a(n-a)=an-a^2.
\]
These inequalities contradict \(n\ge D+a^2+1\).

If \(a=0\), absence of a degree-zero class of size at least \(L\) would mean that every class has size at most \(L-1\), giving
\[
n\le 2s+(L-1)2^{2s},
\]
again a contradiction.

We have therefore found an independent set \(U\), with
\[
|U|\ge L,\qquad N_G(u)=S\quad(u\in U),\qquad |S|=a.
\]

#### Step 2: The repeated neighborhood uses exactly \(a\) units of matching budget

All vertices of \(U\) are isolated in \(G-S\). Since \(|U|\ge a\), matching \(S\) to distinct vertices of \(U\) shows that
\[
\nu(G)\ge a+\nu(G-S).
\]
Thus
\[
\nu(G-S)\le s-a. \tag{1}
\]

Let \(W\) be the endpoints of a maximum matching in \(G-S\), and put
\[
C'=S\cup W.
\]
Then \(C'\) is a vertex cover of \(G\), and
\[
|C'|\le a+2(s-a)=k.
\]
The set \(U\) is disjoint from \(C'\).

Let
\[
X=\{x\in V(G)\setminus C':d_G(x)\ge a+1\},
\qquad
Q=G[C'\cup X].
\]

We next bound \(|V(Q)|\). If \(a=s\), then \(|C'|\le a\), so \(X=\varnothing\).

If \(a<s\), every \((a+1)\)-subset of \(C'\) has at most \(h-1\) common neighbors outside \(C'\), since otherwise \(G\) contains \(K_{a+1,h}\), and hence \(H\). Double-counting gives
\[
\sum_{x\notin C'}\binom{d_G(x)}{a+1}
\le (h-1)\binom{|C'|}{a+1}.
\]
Every member of \(X\) contributes at least one, whence
\[
|V(Q)|
\le k+(h-1)\binom{k}{a+1}
=B. \tag{2}
\]

By (1),
\[
\nu(Q-S)\le s-a.
\]
Also, choosing \(h\) vertices from \(U\) shows that \(Q^{S,h}\) occurs as an induced subgraph of \(G\). Hence \((Q,S)\in\mathcal C(H,s)\).

All vertices outside \(Q\) form an independent set and have degree at most \(a\). Therefore
\[
\begin{aligned}
e(G)
&\le e(Q)+a(n-|V(Q)|)\\
&\le an+\beta(H,s). \tag{3}
\end{aligned}
\]

#### Step 3: Every feasible core can be extended to arbitrary order

Conversely, choose \((Q,S)\) attaining \(\beta(H,s)\), and add \(n-|V(Q)|\) independent vertices, all with neighborhood \(S\).

The resulting graph has matching number at most
\[
|S|+\nu(Q-S)\le s.
\]
It is \(H\)-free: any copy of \(H\) uses at most \(h\) added vertices and could therefore be reproduced in \(Q^{S,h}\).

Its edge count is
\[
e(Q)+a(n-|V(Q)|)=an+\beta(H,s).
\]
This proves equality in (3).

Finally, the finite family is nonempty: take \(Q\) to be an independent set \(S\) of size \(a\). Then \(Q^{S,h}=K_{a,h}\) is \(H\)-free. ∎

### Consequence when the leading coefficient is \(s\)

When \(a=s\), the bound above becomes \(B=s\). Thus Theorem 1 simplifies to
\[
\boxed{
f_H(n,s)
=s(n-s)+
\max\{e(J):|V(J)|=s,\ J\vee I_h\text{ is }H\text{-free}\}
}
\]
for \(n\ge N\).

In particular, this applies to **every nonbipartite \(H\)**. It gives an exact eventual reduction to a graph on only \(s\) vertices, rather than merely an \(O(1)\)-error estimate.

---

## 3. A closed formula for \(K_{2,t}\)

Here the finite-core constant can be evaluated in a substantial uniform range.

### Theorem 2

Let \(t\ge2\), \(s\ge12\), and
\[
n\ge (2t-1)\binom{2s}{2}+2.
\]
Then
\[
\boxed{
f_{K_{2,t}}(n,s)
=n+(t-1)\binom{s}{2}
-\left\lceil\frac s2\right\rceil.
}
\]

Put
\[
b=t-1,\qquad
\psi_b(r)=b\binom r2-\left\lceil\frac r2\right\rceil.
\]

### Lower bound

Take a set \(A\) of \(s\) vertices and put a matching of size \(\lfloor s/2\rfloor\) on \(A\). For every unordered pair \(\{x,y\}\subseteq A\), add \(b\) new vertices, each adjacent exactly to \(x,y\). Add all remaining vertices as leaves at one fixed vertex of \(A\).

The set \(A\) is a vertex cover, so the matching number is at most \(s\).

The graph is \(K_{2,t}\)-free. Equivalently, every pair of vertices has at most \(b\) common neighbors:

- Two vertices of \(A\) have exactly \(b\) common neighbors, because the graph inside \(A\) is a matching.
- A vertex of \(A\) and a vertex outside \(A\) have at most one common neighbor.
- Two vertices outside \(A\) have at most two common neighbors. This is sufficient when \(b\ge2\). When \(b=1\), there is only one added vertex for each pair, so distinct outside vertices have at most one common neighbor.

The edge count is
\[
\begin{aligned}
e(G)
&=\left\lfloor\frac s2\right\rfloor
  +2b\binom s2
  +n-s-b\binom s2\\
&=n+b\binom s2-\left\lceil\frac s2\right\rceil\\
&=n+\psi_b(s).
\end{aligned}
\]

The stated lower bound on \(n\) is more than sufficient for the construction to fit.

### Upper bound, part I: an extremal graph has a leaf

Let \(G\) be extremal. The \(n\)-vertex star is feasible, so
\[
e(G)\ge n-1.
\]

Choose a vertex cover \(C\) of size exactly \(2s\), and put \(I=V(G)\setminus C\). Since \(G\) is \(K_{2,t}\)-free,
\[
\sum_{x\in I}\binom{d_G(x)}2
\le b\binom{2s}{2}. \tag{4}
\]
If no vertex of \(I\) has degree one, then \(d\le2\binom d2\) for every positive degree occurring in \(I\), and hence
\[
\begin{aligned}
e(G)
&\le \binom{2s}{2}
   +2b\binom{2s}{2}\\
&=(2b+1)\binom{2s}{2}\\
&\le n-2,
\end{aligned}
\]
a contradiction.

Thus \(G\) has a leaf \(w\), with neighbor \(v\). As \(w\) is isolated in \(G-v\),
\[
\nu(G-v)\le s-1. \tag{5}
\]

### Upper bound, part II: use a Tutte–Berge barrier

Apply the Tutte–Berge formula to \(R=G-v\), in the form
\[
\nu(R)=
\min_{T\subseteq V(R)}
\left(
|T|+\sum_{C\text{ component of }R-T}
\left\lfloor\frac{|C|}{2}\right\rfloor
\right).
\]
Choose a minimizing \(T\), and set
\[
A=T\cup\{v\},\qquad r=|A|.
\]

Let \(C_1,\dots,C_m\) be the nontrivial components of \(G-A\), and let \(I_0\) be its isolated vertices. Write
\[
u_i=\left\lfloor\frac{|C_i|}{2}\right\rfloor.
\]
By (5),
\[
r+\sum_i u_i\le s. \tag{6}
\]

For a vertex \(x\), write \(d_A(x)=|N(x)\cap A|\). Counting common neighbors of pairs in \(A\) gives
\[
\sum_{x\in I_0}\binom{d_A(x)}2
\le
b\binom r2
-\sum_{x\in A}\binom{d_A(x)}2
-\sum_i\sum_{x\in C_i}\binom{d_A(x)}2. \tag{7}
\]

Use the elementary inequality
\[
d-1-\binom d2\le0\qquad(d\ge0).
\]
Splitting the edges according to \(A,C_1,\ldots,C_m,I_0\), and applying (7), yields
\[
\begin{aligned}
e(G)-n
\le\;&b\binom r2-r
+e(G[A])-\sum_{x\in A}\binom{d_A(x)}2\\
&+\sum_i e(C_i).
\end{aligned}
\]
Furthermore,
\[
\begin{aligned}
e(G[A])-\sum_{x\in A}\binom{d_A(x)}2
&=\frac12\sum_{x\in A}d_A(x)(2-d_A(x))\\
&\le \left\lfloor\frac r2\right\rfloor.
\end{aligned}
\]
Consequently,
\[
\boxed{e(G)-n\le \psi_b(r)+\sum_i e(C_i).} \tag{8}
\]

It remains to show that the nontrivial components cannot compensate for the reduction from \(s\) to \(r\).

### Upper bound, part III: control the nontrivial components

For a \(K_{2,t}\)-free graph \(F\) on \(m\) vertices, counting length-two paths and using Cauchy–Schwarz gives
\[
e(F)\le
\frac m4\left(1+\sqrt{1+4b(m-1)}\right). \tag{9}
\]
Indeed,
\[
\sum_x\binom{d_F(x)}2\le b\binom m2,
\]
and solving the resulting quadratic inequality gives (9).

Since \(|C_i|\le2u_i+1\), we get
\[
e(C_i)
\le \frac{2u_i+1}{4}
       \left(1+\sqrt{1+8bu_i}\right)
\le b\,u_i\,g(u_i), \tag{10}
\]
where
\[
g(u)=\frac{2u+1}{4u}\left(1+\sqrt{8u+1}\right).
\]
The last inequality uses \(b\ge1\).

Two elementary properties of \(g\) suffice:

1. \(g\) is nondecreasing for \(u\ge1\). To see this, put \(y=\sqrt{8u+1}\ge3\); then
   \[
   g(u)=\frac{y+1}{2}+\frac2{y-1},
   \]
   whose derivative with respect to \(y\) is
   \[
   \frac12-\frac2{(y-1)^2}\ge0.
   \]

2. For \(u\ge11\),
   \[
   g(u)\le\frac u2.
   \]
   In fact,
   \[
   (u-\tfrac32)^2-(8u+1)
   =u(u-11)+\tfrac54\ge0,
   \]
   so
   \[
   \frac{2u+1}{4}(1+\sqrt{8u+1})
   \le \frac{u^2}{2}-\frac18.
   \]

As \(s\ge12\), equations (6) and (10) imply
\[
\sum_i e(C_i)
\le b(s-r)g(s-1)
\le \frac{b(s-r)(s-1)}2. \tag{11}
\]

Finally, \(\psi_b\) is discretely convex on the positive integers: its successive differences are
\[
\psi_b(j+1)-\psi_b(j)
=bj-\mathbf 1_{\{j\text{ even}\}},
\]
which are nondecreasing. Also \(\psi_b(1)=-1\), and
\[
\psi_b(s)+1\ge \frac{b(s-1)^2}{2}.
\]
Therefore, for \(1\le r<s\),
\[
\frac{\psi_b(s)-\psi_b(r)}{s-r}
\ge
\frac{\psi_b(s)+1}{s-1}
\ge \frac{b(s-1)}2.
\]
Together with (11), this gives
\[
\psi_b(r)+\sum_i e(C_i)\le\psi_b(s).
\]
The case \(r=s\) follows directly from (6), since then there are no nontrivial components.

Substituting into (8),
\[
e(G)\le n+\psi_b(s),
\]
matching the construction. ∎

For example, the \(C_4\) specialization is
\[
f_{C_4}(n,s)
=n+\binom s2-\left\lceil\frac s2\right\rceil
\]
for
\[
s\ge12,\qquad n\ge6s^2-3s+2.
\]

---

## 4. Effective computation and the remaining gap

Theorem 1 gives a fully specified exact algorithm for fixed \(H,s\):

1. Enumerate every labeled graph \(Q\) on at most \(B\) vertices and every \(a\)-subset \(S\).
2. Test \(\nu(Q-S)\le s-a\), for example by enumerating possible matchings of size \(s-a+1\).
3. Test whether \(Q^{S,h}\) contains \(H\), by enumerating injections of \(V(H)\).
4. Compute the maximum \(e(Q)-a|V(Q)|\).

This determines \(f_H(n,s)\) for every \(n\ge N\). For \(n<N\), exhaustive enumeration involves only a number of vertices bounded in terms of \(h,s\). Consequently the value problem has an exact algorithm taking
\[
F(h,s)+\operatorname{poly}(\log n)
\]
time when \(n\) is given in binary, for some explicit finite function \(F\). This is an effective parameterized determination, not a practical algorithm. No computational experiments are being claimed here.

The unresolved part of the requested research direction remains substantial:

- For general bipartite \(H\) with \(q(H)\le s\), the finite constant \(\beta(H,s)\) has not been evaluated in closed form here.
- The small-\(n\) range is treated only by enumeration, not by an extremal classification.
- The restrictions \(s\ge12\) and large \(n\) in Theorem 2 are sufficient conditions, not claimed to be optimal.

Thus the broad all-\(H,n,s\) problem is not solved, but the arguments give exact eventual structure in general and a closed formula for an entire non-color-critical forbidden family.