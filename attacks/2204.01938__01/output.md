```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted wording has a bounded-extremal counterexample, but the conjectured high-probability bound holds for every finite forbidden family with unbounded Turán number, and for arbitrary families of connected forbidden graphs.",
  "would_publish": false,
  "caveats": "The catalog omits finiteness and nondegeneracy assumptions and may not reproduce the exact quantifiers of Remark 1.6."
}
```

# Mathematical writeup

## 1. Statement and outcome

For an orientation \(D\) of an \(m\)-edge graph, define its directed surplus by
\[
s(D):=\frac m2-\beta(D).
\]
The catalog asks whether, when \(H\) is an \(n\)-vertex \(\mathcal B\)-free graph with
\[
e(H)=m=\operatorname{ex}(n,\mathcal B),
\]
a uniformly random orientation \(D\) of \(H\) satisfies
\[
s(D)=\Omega_{\mathcal B}(\sqrt{mn})
\]
with high probability, without assuming a power law for \(\operatorname{ex}(n,\mathcal B)\).

There are two conclusions.

### Theorem

Let \(\mathcal B\) be a finite family of finite simple graphs, each having at least one edge, and let
\[
f(n)=\operatorname{ex}(n,\mathcal B).
\]
For every \(n\), let \(H\) be any \(n\)-vertex \(\mathcal B\)-free graph with \(m=f(n)\) edges, and orient its edges independently and uniformly to obtain \(D\). There is a constant \(c_{\mathcal B}>0\) such that
\[
\Pr\!\left(
s(D)\ge c_{\mathcal B}\min\{m,\sqrt{mn}\}
\right)
\ge
1-\exp\!\bigl(-c_{\mathcal B}\min\{m,n\}\bigr).
\tag{1}
\]

Consequently, if \(f(n)\) is unbounded, then in fact \(f(n)=\Omega_{\mathcal B}(n)\), and hence
\[
\Pr\!\left(
s(D)\ge c_{\mathcal B}\sqrt{mn}
\right)
\ge 1-e^{-c_{\mathcal B}n}.
\tag{2}
\]
Thus the conjectured conclusion holds for every finite, nondegenerate forbidden family, without any assumption of the form
\[
f(n)=\Theta(n^{2-\varepsilon}).
\]

The same conclusion holds, without finiteness of \(\mathcal B\), if every member of \(\mathcal B\) is connected.

On the other hand, the literal unrestricted catalog statement is false when \(f(n)\) is bounded; an explicit counterexample appears in Section 7.

---

## 2. Feedback arc sets and vertex orderings

For a vertex ordering \(\pi\), let \(F_\pi(D)\) be the number of arcs directed forward in \(\pi\). Then
\[
\beta(D)=m-\max_\pi F_\pi(D).
\tag{3}
\]
Indeed, the forward arcs of any ordering are acyclic, while every acyclic subgraph has a topological ordering.

Therefore
\[
s(D)=\max_\pi F_\pi(D)-\frac m2.
\tag{4}
\]

For a vertex \(v\), put
\[
b_D(v)=d_D^+(v)-d_D^-(v).
\]

### Lemma 2.1: imbalance gives surplus

For every orientation \(D\),
\[
s(D)\ge \frac14\sum_{v\in V(D)} |b_D(v)|.
\tag{5}
\]

#### Proof

Let
\[
P=\{v:b_D(v)\ge0\},\qquad N=V(D)\setminus P.
\]
The net number of arcs from \(P\) to \(N\) is
\[
e_D(P,N)-e_D(N,P)
 =\sum_{v\in P}b_D(v)
 =\frac12\sum_v |b_D(v)|.
\tag{6}
\]

Choose an ordering of \(P\) having at least half of the arcs inside \(P\) forward. Such an ordering exists because an arbitrary ordering and its reverse have complementary forward counts. Do the same inside \(N\), and put all of \(P\) before all of \(N\).

If \(m_\times\) is the number of crossing edges and \(\delta\) is the quantity in (6), then the number of forward crossing arcs is
\[
\frac{m_\times+\delta}{2}.
\]
Thus the resulting ordering has at least
\[
\frac{m-m_\times}{2}+\frac{m_\times+\delta}{2}
=\frac m2+\frac{\delta}{2}
=\frac m2+\frac14\sum_v|b_D(v)|
\]
forward arcs. Equation (4) proves the lemma. \(\square\)

---

## 3. Random orientations

Let \(d_H(v)=d_v\). Under a uniformly random orientation,
\[
b_D(v)\stackrel{d}{=}\xi_1+\cdots+\xi_{d_v},
\]
where the \(\xi_i\) are independent uniform signs.

A simple fourth-moment argument gives a uniform lower bound. If
\[
Z=\xi_1+\cdots+\xi_d,
\]
then
\[
\mathbb E Z^2=d,\qquad
\mathbb E Z^4=3d^2-2d\le3d^2.
\]
Applying Paley–Zygmund to \(Z^2\),
\[
\Pr\left(|Z|\ge\sqrt{d/2}\right)\ge\frac1{12}.
\]
Hence
\[
\mathbb E|Z|\ge \frac{\sqrt d}{12\sqrt2}.
\tag{7}
\]

Writing
\[
Y(D)=\sum_v |b_D(v)|,
\]
we therefore have
\[
\mathbb E Y(D)\ge \frac1{12\sqrt2}\sum_v\sqrt{d_v}.
\tag{8}
\]

There is also strong concentration. Reversing one edge changes the imbalances of its two endpoints by \(2\), so it changes \(Y\) by at most \(4\). The bounded-differences inequality gives
\[
\Pr\bigl(Y\le \mathbb EY-t\bigr)
\le \exp\left(-\frac{t^2}{8m}\right).
\tag{9}
\]

It remains to prove that extremality forces
\[
\sum_v\sqrt{d_v}
\]
to have the required order.

---

## 4. Approximate replication for finite forbidden families

We first remove isolated vertices from every forbidden graph. For all sufficiently large host orders this does not change the forbidden condition: if a host contains the nonisolated part of a forbidden graph, arbitrary additional vertices can represent its isolated vertices. Thus we may suppose that every component of every \(B\in\mathcal B\) contains an edge.

### Lemma 4.1: approximate superadditivity

For every finite family \(\mathcal B\), there is a constant \(L=L(\mathcal B)\) such that, for all \(1\le k\le n\),
\[
f(k)\le Lk+\frac{2k}{n}f(n).
\tag{10}
\]

#### Proof

Fix an extremal \(k\)-vertex \(\mathcal B\)-free graph \(G\).

For \(B\in\mathcal B\), write its connected components as
\[
C_1,\ldots,C_r
\]
and put \(h=|V(B)|\). Since \(G\) is \(B\)-free, at least one component \(C_i\) has fewer than \(h\) pairwise vertex-disjoint copies in \(G\). Otherwise, choose copies of \(C_1,\ldots,C_r\) greedily: before selecting the next component fewer than \(h\) vertices have been used, while a packing of \(h\) disjoint copies has at most one member meeting each previously used vertex. This would produce vertex-disjoint copies of all components of \(B\), hence a copy of \(B\).

Choose such a component \(C_B\), take a maximal packing of copies of \(C_B\), and let \(X_B\) be the union of its vertices. Then
\[
|X_B|<|V(B)|^2
\]
and \(G-X_B\) is \(C_B\)-free.

Doing this for every \(B\in\mathcal B\), let
\[
X=\bigcup_{B\in\mathcal B}X_B.
\]
There is a constant \(L=L(\mathcal B)\) such that \(|X|\le L\), and \(G-X\) avoids one connected component \(C_B\) of every forbidden graph \(B\). Hence a disjoint union of arbitrarily many copies of \(G-X\) is \(\mathcal B\)-free: a connected copy of \(C_B\) would have to lie in one copy of \(G-X\), where none exists.

Moreover,
\[
e(G-X)\ge f(k)-Lk.
\]
Taking \(q=\lfloor n/k\rfloor\) disjoint copies of \(G-X\), together with isolated vertices, gives
\[
f(n)\ge q\bigl(f(k)-Lk\bigr).
\]
Since
\[
q=\left\lfloor\frac nk\right\rfloor\ge\frac{n}{2k},
\]
we obtain
\[
f(k)\le Lk+\frac{f(n)}q
\le Lk+\frac{2k}{n}f(n).
\]
This proves (10). \(\square\)

For connected forbidden graphs, no deletion is needed: disjoint unions of \(\mathcal B\)-free graphs remain \(\mathcal B\)-free. Thus in that case one may take \(L=0\), even for an infinite family \(\mathcal B\).

---

## 5. Degree spread in an extremal graph

Let \(H\) be \(n\)-vertex extremal, with \(m=f(n)\), and put
\[
x=\frac mn.
\]
For every \(S\subseteq V(H)\), Lemma 4.1 gives
\[
e_H(S)\le f(|S|)
\le \left(L+2x\right)|S|.
\tag{11}
\]
Thus every subgraph of \(H\) has average degree at most
\[
2L+4x.
\]

Repeatedly delete a vertex of degree at most \(2L+4x\). If \(q_v\) denotes the number of neighbors remaining when \(v\) is deleted, then
\[
q_v\le 2L+4x,\qquad q_v\le d_v,
\qquad \sum_vq_v=m.
\]
Consequently
\[
q_v^2\le (2L+4x)d_v,
\]
and hence
\[
m=\sum_vq_v
\le \sqrt{2L+4x}\sum_v\sqrt{d_v}.
\]
Therefore
\[
\sum_v\sqrt{d_v}
\ge
\frac{m}{\sqrt{2L+4m/n}}.
\tag{12}
\]

If \(m\le n\), this is at least
\[
\frac{m}{\sqrt{2L+4}},
\]
while if \(m\ge n\), it is at least
\[
\frac{\sqrt{mn}}{\sqrt{2L+4}}.
\]
Thus
\[
\sum_v\sqrt{d_v}
\ge c_{\mathcal B}\min\{m,\sqrt{mn}\}.
\tag{13}
\]

For connected forbidden families, \(L=0\), and (12) directly gives the sharper estimate
\[
\sum_v\sqrt{d_v}\ge \frac12\sqrt{mn}.
\tag{14}
\]

---

## 6. Completion of the probabilistic bound

Combining (8) and (13), there is \(a_{\mathcal B}>0\) such that
\[
\mu:=\mathbb EY(D)
\ge a_{\mathcal B}\min\{m,\sqrt{mn}\}.
\tag{15}
\]
Taking \(t=\mu/2\) in (9),
\[
\Pr\left(Y(D)<\frac\mu2\right)
\le
\exp\left(-\frac{\mu^2}{32m}\right).
\]
Since
\[
\frac{\min\{m,\sqrt{mn}\}^2}{m}
=\min\{m,n\},
\]
we get
\[
\Pr\left(Y(D)<\frac\mu2\right)
\le
\exp\bigl(-c_{\mathcal B}\min\{m,n\}\bigr).
\tag{16}
\]

On the complementary event, Lemma 2.1 gives
\[
s(D)\ge\frac14Y(D)
\ge\frac18\mu
\ge c_{\mathcal B}\min\{m,\sqrt{mn}\}.
\]
This proves (1).

---

## 7. Why unbounded finite-family Turán numbers are automatically linear

For completeness, the condition \(f(n)=\Omega(n)\) need not be separately assumed when \(\mathcal B\) is finite and \(f\) is unbounded.

After removing isolated vertices from forbidden graphs:

* A graph embeds in a matching if and only if it is itself a matching.
* A graph embeds in a star if and only if it is itself a star.

If no matching belongs to \(\mathcal B\), then an \(n\)-vertex matching is \(\mathcal B\)-free, so
\[
f(n)\ge \lfloor n/2\rfloor.
\]

Suppose instead that \(M_s\in\mathcal B\). Then every \(\mathcal B\)-free graph has matching number at most \(s-1\). If no star belongs to \(\mathcal B\), then \(K_{1,n-1}\) is \(\mathcal B\)-free and
\[
f(n)\ge n-1.
\]

Finally, if both \(M_s\) and \(K_{1,t}\) belong to \(\mathcal B\), then every \(\mathcal B\)-free graph has
\[
\nu(G)\le s-1,\qquad \Delta(G)\le t-1.
\]
The endpoints of a maximal matching form a vertex cover of size at most \(2(s-1)\), whence
\[
e(G)\le 2(s-1)(t-1).
\]
Thus \(f(n)\) is bounded.

It follows that a finite-family Turán number is either bounded or at least linear. In the unbounded case, \(m\ge c_{\mathcal B}n\), and (1) becomes exactly
\[
s(D)=\Omega_{\mathcal B}(\sqrt{mn})
\]
with failure probability \(e^{-\Omega_{\mathcal B}(n)}\).

---

## 8. Literal counterexample when bounded Turán numbers are allowed

Let
\[
\mathcal B=\{P_3,\,2K_2\}.
\]
A \(P_3\)-free graph has maximum degree at most \(1\), hence is a matching. Being also \(2K_2\)-free forces it to have at most one edge. Therefore
\[
\operatorname{ex}(n,\mathcal B)=1
\]
for every \(n\ge2\).

An orientation of the unique edge is acyclic, so
\[
\beta(D)=0,\qquad
s(D)=\frac12.
\]
But
\[
\sqrt{mn}=\sqrt n.
\]
Hence no fixed positive constant \(c_{\mathcal B}\) can satisfy
\[
s(D)\ge c_{\mathcal B}\sqrt{mn}
\]
as \(n\to\infty\).

Thus the unrestricted catalog wording is false. The correct finite-family scale is
\[
\boxed{\min\{m,\sqrt{mn}\}},
\]
and the conjectured \(\sqrt{mn}\) scale follows whenever the Turán number is unbounded, as is the case in the usual applications involving cycle-containing forbidden graphs.

## 9. Remaining scope issue

The proof covers:

1. every finite forbidden family with unbounded Turán number;
2. every family, finite or infinite, whose forbidden graphs are connected.

It does not cover an arbitrary infinite family of disconnected forbidden graphs. The finite-family proof uses a uniform bound on the total number and sizes of forbidden components. Also, if Remark 1.6 in the source asks for an upper bound \(s(D)=O(\sqrt{mn})\), rather than the lower bound stated in the catalog, the argument above addresses only the cataloged lower-bound formulation.