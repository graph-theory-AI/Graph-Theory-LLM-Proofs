```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Exact minimization is NP-complete even for every fixed t on VC-dimension-2, (t+1)-uniform instances, while the worst-case size is a Turán-system number that is explicit for t=1,2 and admits tight fixed-t order bounds.",
  "would_publish": false,
  "caveats": "The bounded-VC and geometric asymptotics in the source regime remain open; the elementary reductions may already be known."
}
```

# Mathematical writeup

## 1. Precise interpretation

The catalog item is an open-ended question rather than a proposition with a truth value. I address two precise versions.

Let \(H=(V,E)\), \(n=|V|\), and put
\[
m=\lceil \varepsilon n\rceil.
\]
Since \(\varepsilon>t/n\), we have
\[
t<m\le n.
\]
Write \(\tau_{\varepsilon,t}(H)\) for the minimum size of an \(\varepsilon\)-\(t\)-net.

The two questions considered below are:

1. Given an explicitly listed hypergraph, how hard is it to compute \(\tau_{\varepsilon,t}(H)\)?
2. What is
   \[
   \max_H \tau_{\varepsilon,t}(H)
   \]
   as a function of \(n,m,t\)?

The computational statements below use the explicit-input model; geometric and oracle representations can behave differently.

---

## 2. Exact formulation as Set Cover

Let
\[
E_{\ge m}=\{e\in E:|e|\ge m\}.
\]
For each \(s\in\binom Vt\), define
\[
D_s=\{e\in E_{\ge m}:s\subseteq e\}.
\]
Then \(S\subseteq\binom Vt\) is an \(\varepsilon\)-\(t\)-net precisely when
\[
\{D_s:s\in S\}
\]
covers the universe \(E_{\ge m}\). Equivalently,
\[
\tau_{\varepsilon,t}(H)=
\min \left\{
\sum_{s\in\binom Vt}x_s:
\sum_{s\in\binom et}x_s\ge 1\quad(e\in E_{\ge m}),\
x_s\in\{0,1\}
\right\}.
\]

Thus the optimization problem is exactly a Set Cover instance, albeit one with sets induced by containment of \(t\)-subsets.

### Consequence: a polynomial approximation for fixed \(t\)

If \(q=|E_{\ge m}|\) and \(t\) is fixed, all \(\binom nt=O(n^t)\) candidates can be enumerated. The usual greedy Set Cover algorithm therefore gives, in polynomial time, a net of size at most
\[
(1+\ln q)\,\tau_{\varepsilon,t}(H).
\]

Indeed, if \(k=\tau_{\varepsilon,t}(H)\) and \(r\) constraints remain uncovered, one of the \(k\) members of an optimum solution covers at least \(r/k\) of them. Greedy covers at least as many, giving the standard exponential-decay argument.

There is also the elementary bound
\[
\tau_{\varepsilon,t}(H)
\le
\min\left\{
q,\binom nt,
\left\lceil
\frac{\binom nt}{\binom mt}(\ln q+1)
\right\rceil
\right\}
\qquad(q\ge1).
\]
For the last bound, sample \(r\) uniformly random \(t\)-sets. A fixed large edge contains a sampled set with probability at least
\[
\frac{\binom mt}{\binom nt}.
\]
A union bound shows that the displayed value of \(r\) succeeds with positive probability.

---

## 3. Exact computation is NP-complete under severe restrictions

### Theorem 3.1

For every fixed \(t\ge1\), deciding whether an explicitly given hypergraph has an \(\varepsilon\)-\(t\)-net of size at most \(k\) is NP-complete. This remains true when:

- every hyperedge has size exactly \(t+1\);
- \(\varepsilon=(t+1)/|V|\);
- the hypergraph has VC-dimension at most \(2\).

### Proof

Membership in NP is immediate for fixed \(t\). More generally, if there are \(q\) large edges, choosing one \(t\)-subset from each gives a net of size at most \(q\), so polynomially sized certificates always suffice.

For hardness, reduce from Vertex Cover. Let \(G=(U,F)\) be a graph with \(|U|\ge3\). Introduce a set \(A\), disjoint from \(U\), of size \(t-1\), and define
\[
V=A\mathbin{\dot\cup} U,\qquad
e_{uv}=A\cup\{u,v\}\quad(uv\in F).
\]
Every hyperedge has size \(t+1\). Put
\[
\varepsilon=\frac{t+1}{|V|}.
\]
Then \(\varepsilon\in(t/|V|,1)\), and every hyperedge is large.

If \(C\subseteq U\) is a vertex cover, then
\[
S_C=\{A\cup\{u\}:u\in C\}
\]
is an \(\varepsilon\)-\(t\)-net.

Conversely, let \(S\) be a net. Delete any member of \(S\) contained in no hyperedge. For each remaining \(s\in S\), choose some
\[
u_s\in s\setminus A,
\]
which exists because \(|A|=t-1<|s|\), and replace \(s\) by \(A\cup\{u_s\}\). If a hyperedge contains \(s\), it contains both \(A\) and \(u_s\), so this replacement covers every hyperedge previously covered by \(s\). After all replacements and deletion of duplicates, we obtain a net no larger than \(S\) whose members all have the form \(A\cup\{u\}\).

Now \(A\cup\{u\}\subseteq e_{xy}\) exactly when \(u\in\{x,y\}\). Hence the corresponding vertices form a vertex cover of \(G\). Therefore
\[
\tau_{\varepsilon,t}(H_G)=\tau(G).
\]

It remains to check the VC-dimension. If a shattered set \(X\) meets \(A\), the empty trace cannot be realized because every hyperedge contains \(A\). Thus a shattered set lies in \(U\). But every hyperedge contains only two vertices of \(U\), so a set of three vertices cannot have its full trace realized. Hence
\[
\operatorname{VCdim}(H_G)\le2.
\]
The reduction preserves the optimum, proving the theorem. \(\square\)

Thus, in the explicit-input model, a minimum net cannot be computed in polynomial time unless \(P=NP\). This does not preclude efficient construction of nonminimum nets satisfying a proved asymptotic bound.

### Every Hitting Set instance embeds

The containment structure does not substantially restrict general Set Cover behavior. Given a Hitting Set instance \((U,\mathcal F)\) with nonempty members, replace \(U\) by
\[
W=U\times\{0,1\},
\]
take \(|A|=t-1\), and use hyperedges
\[
e_F=A\cup(F\times\{0,1\}),\qquad F\in\mathcal F.
\]
Set
\[
\varepsilon=\frac{t+1}{|A|+|W|}.
\]
Every hyperedge is large. The same normalization replaces every useful \(t\)-set \(s\) by \(A\cup\{w\}\) for some \(w\in s\setminus A\). Projecting \(w=(u,i)\) to \(u\) gives a hitting set of no greater size, while any hitting set gives a net of the same size. Hence this is an optimum-preserving reduction.

---

## 4. The worst case over all hypergraphs is a Turán-system number

Define
\[
T(n,m,t)=
\min\left\{
|S|:
S\subseteq\binom{[n]}t,\ 
\text{every }M\in\binom{[n]}m
\text{ contains some }s\in S
\right\}.
\]

### Proposition 4.1

For fixed \(n,m,t\),
\[
\max_H \tau_{\varepsilon,t}(H)=T(n,m,t),
\]
where the maximum ranges over all hypergraphs on \(n\) vertices with threshold \(m=\lceil\varepsilon n\rceil\).

### Proof

A family hitting every \(m\)-subset hits every set of size at least \(m\): choose an \(m\)-subset inside the larger set. Thus \(T(n,m,t)\) is an upper bound for every \(H\).

Equality is attained for
\[
H^*=\left([n],\binom{[n]}m\right).
\]
\(\square\)

There are two useful equivalent forms.

1. Viewing \(S\) as a \(t\)-uniform hypergraph, the condition is
   \[
   \alpha(S)\le m-1.
   \]

2. If \(K_m^{(t)}\) denotes the complete \(t\)-uniform hypergraph on \(m\) vertices, then
   \[
   T(n,m,t)
   =
   \binom nt-\operatorname{ex}_t(n,K_m^{(t)}).
   \]
   Indeed, the complement of \(S\) in \(\binom{[n]}t\) must be \(K_m^{(t)}\)-free.

There is also a covering-design duality:
\[
T(n,m,t)=\mathsf C(n,n-t,n-m),
\]
where \(\mathsf C(n,k,r)\) is the minimum number of \(k\)-subsets covering all \(r\)-subsets. This follows from
\[
s\subseteq M
\quad\Longleftrightarrow\quad
[n]\setminus M\subseteq[n]\setminus s.
\]

---

## 5. Exact worst-case values in some cases

### 5.1. The case \(t=1\)

A set of selected vertices meets every \(m\)-set exactly when its complement has size at most \(m-1\). Therefore
\[
T(n,m,1)=n-m+1.
\]

### 5.2. The case \(t=2\)

Put
\[
p=m-1,\qquad n=pa+b,\qquad 0\le b<p.
\]
Then
\[
\boxed{
T(n,m,2)
=
(p-b)\binom a2+b\binom{a+1}2.
}
\]

To see this, regard the selected pairs as the edges of a graph \(G\). Every \(m\)-set contains a selected pair exactly when
\[
\alpha(G)\le m-1.
\]
Equivalently, \(\overline G\) is \(K_m\)-free. Turán's theorem says that the maximum \(K_m\)-free graph is the balanced complete \((m-1)\)-partite graph. Consequently, \(G\) is optimally the disjoint union of \(m-1\) balanced cliques, yielding the displayed formula.

For example,
\[
T(n,3,2)
=
\binom{\lfloor n/2\rfloor}{2}
+
\binom{\lceil n/2\rceil}{2}
=
\frac{n^2}{4}+O(n).
\]

### 5.3. Boundary cases for arbitrary \(t\)

Clearly
\[
T(n,n,t)=1.
\]

Also,
\[
T(n,n-1,t)=\left\lceil\frac{n}{n-t}\right\rceil.
\]
Indeed, the complements of the selected \(t\)-sets have size \(n-t\), and the condition is exactly that these complements cover all vertices.

---

## 6. General elementary bounds and the correct fixed-\(t\) order

Assume \(2\le t<m\le n\). Put
\[
N=\binom nt,\qquad K=\binom mt.
\]

### Lower bounds

Double counting pairs \((s,M)\), where \(s\in S\), \(M\in\binom{[n]}m\), and \(s\subseteq M\), gives
\[
T(n,m,t)\ge
\left\lceil
\frac{\binom nt}{\binom mt}
\right\rceil.
\]

A stronger bound in many ranges follows by an alteration argument. Let \(S\) have \(r\) members and choose each vertex independently with probability \(x\). If \(R\) is the chosen vertex set and \(Z\) is the number of members of \(S\) contained in \(R\), deleting one vertex from each such member leaves an independent set of size at least \(|R|-Z\). Hence
\[
\alpha(S)\ge nx-rx^t.
\]
Since \(\alpha(S)\le m-1\),
\[
r\ge
\frac{nx-(m-1)}{x^t}
\quad(0<x\le1).
\]
Thus
\[
T(n,m,t)\ge
\left\lceil
\Phi(n,m,t)
\right\rceil,
\qquad
\Phi(n,m,t)=
\max_{0<x\le1}
\frac{nx-(m-1)}{x^t}.
\]

Writing
\[
\beta=\frac{m-1}{n},
\]
elementary differentiation gives
\[
\Phi(n,m,t)=
\begin{cases}
\displaystyle
\frac{n(t-1)^{t-1}}{t^t\beta^{t-1}}
=
\frac{(t-1)^{t-1}}{t^t}
\frac{n^t}{(m-1)^{t-1}},
&
\beta\le\frac{t-1}{t},\\[1.2em]
n-m+1,
&
\beta\ge\frac{t-1}{t}.
\end{cases}
\]

### An explicit partition upper bound

Put
\[
p=\left\lfloor\frac{m-1}{t-1}\right\rfloor
\]
and partition the \(n\) vertices into \(p\) classes as equally as possible. Write
\[
n=pa+b,\qquad 0\le b<p.
\]
Select all \(t\)-sets contained in one class. This gives
\[
T(n,m,t)
\le
U(n,m,t):=
(p-b)\binom at+b\binom{a+1}t.
\]

Indeed, an \(m\)-set avoiding all selected \(t\)-sets would contain at most \(t-1\) vertices in each class and therefore at most
\[
p(t-1)\le m-1
\]
vertices, a contradiction.

For \(t=2\), this construction is exactly optimal by Turán's theorem.

### Corollary 6.1: tight order for fixed \(t\)

For every fixed \(t\ge2\),
\[
T(n,m,t)=
\begin{cases}
\displaystyle
\Theta_t\!\left(\frac{n^t}{(m-1)^{t-1}}\right),
&
m-1\le\frac{t-1}{t}n,\\[1.2em]
\Theta_t(n-m+1),
&
m-1\ge\frac{t-1}{t}n.
\end{cases}
\]

The lower bounds are those above. For the upper bound in the first range,
\[
p\ge\frac{m-1}{2(t-1)}
\]
and every class has size at most \(3n/(2p)\), so the partition construction has size
\[
O_t\!\left(\frac{n^t}{(m-1)^{t-1}}\right).
\]

For the second range, put \(\delta=n-m+1\). Then \(\delta\le n/t\) and \(p\ge\delta\). Writing
\[
n=p(t-1)+h,
\]
one has
\[
h\le\delta+t-2\le(t-1)\delta.
\]
Only at most \(h\) classes have size at least \(t\), and every class has size at most \(2t-2\). Hence
\[
U(n,m,t)
\le
(t-1)\binom{2t-2}{t}\delta.
\]

In particular, for fixed \(t\) and fixed \(0<\varepsilon<1\),
\[
T(n,\lceil\varepsilon n\rceil,t)=\Theta_{t,\varepsilon}(n).
\]
Thus arbitrary hypergraphs do not admit a bound depending only on \(t\) and \(\varepsilon\), independently of \(n\).

---

## 7. Two bounded-VC lower-bound constructions

### 7.1. A near-threshold obstruction

Fix \(t\ge2\), let
\[
H=\left([n],\binom{[n]}{t+1}\right),
\qquad
\varepsilon=\frac{t+1}{n},
\]
and suppose \(n\ge2(t+1)\).

The VC-dimension of \(H\) is exactly \(t+1\): every \((t+1)\)-set is shattered by completing each of its subsets with vertices outside it, while no larger set can have its full trace realized.

Each selected \(t\)-set lies in exactly \(n-t\) hyperedges. Therefore
\[
\tau_{\varepsilon,t}(H)
\ge
\frac{\binom n{t+1}}{n-t}
=
\frac{1}{t+1}\binom nt
=
\Omega_t(n^t)
=
\Omega_t(\varepsilon^{-t}).
\]

Consequently, under only the displayed assumption \(\varepsilon>t/n\), no uniform bound of the form
\[
O\!\left(
\frac{(1+\log t)d}{\varepsilon}\log\frac1\varepsilon
\right)
\]
can hold for all admissible \((n,\varepsilon)\): for fixed \(t\ge2\), the displayed expression is \(O_t(n\log n)\), while this example requires \(\Omega_t(n^t)\).

This is not asserted to contradict the source theorem. The source abstract says “sufficiently large,” and its precise quantifier is not included in the prompt. The example shows that the largeness requirement must depend nonuniformly on \(t\) and \(\varepsilon\), or equivalently must exclude the regime \(\varepsilon n-t=O(1)\).

### 7.2. VC-dimension one sunflowers

For arbitrary \(n,m,t\), put
\[
L=m-t+1,\qquad
r=\left\lfloor\frac{n-t+1}{L}\right\rfloor.
\]
Take a common core \(A\) of size \(t-1\), disjoint petals
\[
P_1,\dots,P_r,\qquad |P_i|=L,
\]
and hyperedges
\[
e_i=A\cup P_i.
\]
Unused vertices may be added to reach \(n\).

Every edge has size \(m\), and distinct edges intersect in the \((t-1)\)-set \(A\). Hence no \(t\)-set can be contained in two different edges, so
\[
\tau_{\varepsilon,t}(H)=r.
\]
The hypergraph has VC-dimension at most \(1\): a two-element set meeting the core cannot realize the empty trace; two elements in one petal cannot realize singleton traces; and two elements in different petals cannot realize the full trace.

Thus even VC-dimension-one examples can require
\[
\left\lfloor
\frac{n-t+1}{m-t+1}
\right\rfloor
\]
members. Near the threshold \(m=t+1\), this is approximately \((n-t)/2\); when \(m\sim\varepsilon n\) and \(n\gg t/\varepsilon\), it is of order \(1/\varepsilon\).

---

## 8. Remaining gaps

1. For \(t\ge3\), an exact formula for \(T(n,m,t)\) contains difficult classical hypergraph Turán problems. For example,
   \[
   T(n,4,3)=\binom n3-\operatorname{ex}_3(n,K_4^{(3)}).
   \]
   Determining the leading constant here is the classical tetrahedron Turán problem and, to my knowledge, remains open.

2. The NP-completeness result concerns exact optimization for explicitly listed hypergraphs. It does not rule out efficient algorithms constructing nets meeting a prescribed nonoptimal asymptotic bound.

3. The source paper's tight bounded-VC estimates in the regime where \(n\) is sufficiently large relative to \(t\) and \(\varepsilon\), and the corresponding geometric questions, are not resolved here.

4. The near-threshold examples show that the exact quantifiers in any proposed VC-dimension bound are essential.