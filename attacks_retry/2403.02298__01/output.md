```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A random-priority triangle filter gives t_vec(n) >= (sqrt(pi)/4-o(1))sqrt(n)/ln(n), improving the lower-bound constant but leaving the logarithmic gap open.",
  "would_publish": false,
  "caveats": "Only the constant improves, not the order; novelty beyond the bounds supplied in the prompt is not asserted."
}
```

## 1. Partial result

All logarithms below are natural. I prove
\[
\boxed{\displaystyle
\vec a(n)\leq \left(\frac{4}{\sqrt{\pi}}+o(1)\right)\sqrt n\,\ln n
}
\tag{1}
\]
and consequently
\[
\boxed{\displaystyle
\vec t(n)\geq
\left(\frac{\sqrt{\pi}}4-o(1)\right)\frac{\sqrt n}{\ln n}.
}
\tag{2}
\]

The constants are
\[
\frac4{\sqrt\pi}\approx 2.256758,
\qquad
\frac{\sqrt\pi}{4}\approx 0.443113.
\]
Thus (2) improves the constants in both the source bound and the supplied previous attempt, under natural-log normalization. It does **not** improve the logarithmic exponent and does not settle the conjecture.

I use and reprove the previous attempt’s elementary block certificate, but replace its local-lemma construction by a random-priority triangle filter.

---

## 2. The triangle filter

Fix positive constants \(c,C\), and write
\[
I_c=\int_0^c e^{-t^2}\,dt.
\]
We will prove that
\[
CI_c>2
\tag{3}
\]
is sufficient to construct, for all sufficiently large \(n\), an oriented triangle-free graph \(D\) satisfying
\[
\vec\alpha(D)<(C+o(1))\sqrt n\,\ln n.
\tag{4}
\]

Independently for every unordered pair \(e=\{u,v\}\), choose:

* a priority \(U_e\), uniformly distributed on \([0,1]\);
* one of its two orientations, with equal probabilities.

Put
\[
p=\frac c{\sqrt n},
\]
and let \(G_p\) contain the pairs with \(U_e\leq p\). Thus \(G_p\) has distribution \(G(n,p)\).

Retain \(e=\{u,v\}\) precisely when
\[
U_e\leq p
\quad\text{and}\quad
\text{there is no }w\notin\{u,v\}
\text{ with }U_{uw}<U_e,\ U_{vw}<U_e.
\tag{5}
\]
Give each retained edge its previously chosen orientation.

With probability one, all priorities are distinct. In every triangle of \(G_p\), its largest-priority edge fails (5). Therefore the retained underlying graph is triangle-free.

This filter deletes the largest-priority edge of every original triangle; it does not involve an iterative process.

---

## 3. Block certificates and their number

Set
\[
\ell=\lceil\ln n\rceil,\qquad
b=\lceil C\sqrt n\rceil,\qquad
k=\ell b.
\]
Then
\[
k=(C+o(1))\sqrt n\,\ln n.
\tag{6}
\]

Consider all ordered collections
\[
\mathcal V=(V_1,\ldots,V_\ell)
\]
of pairwise disjoint \(b\)-element sets. Write
\[
S=V_1\cup\cdots\cup V_\ell,
\]
and let \(P_{\mathcal V}\) be the unordered pairs joining different blocks. Its size is
\[
R=\binom{\ell}{2}b^2
  =\frac{1-1/\ell}{2}k^2.
\tag{7}
\]

An arc from \(V_j\) to \(V_i\), where \(i<j\), is called **backward** for \(\mathcal V\).

### Block certificate

If every such \(\mathcal V\) has a backward arc, then
\[
\vec\alpha(D)<k.
\tag{8}
\]

Indeed, an acyclic induced subdigraph on \(k\) vertices has a topological ordering. Its \(\ell\) consecutive blocks of size \(b\) have no backward arc.

Let \(N_B\) be the number of ordered block collections. We have
\[
N_B=\frac{(n)_k}{(b!)^\ell}
    \leq \left(\frac{en}{b}\right)^k,
\]
and hence
\[
\ln N_B\leq
\left(\frac12+o(1)\right)k\ln n.
\tag{9}
\]

The rest of the proof shows that the filtered orientation has a backward arc in every block collection with probability tending to one.

---

## 4. Uniformly few triangles inside a \(k\)-set

The first auxiliary estimate controls deletions caused entirely inside a certificate’s support.

### Lemma 1

Define
\[
s_n=\frac{k\ln n}{\sqrt{\ln\ln n}}.
\tag{10}
\]
With probability tending to one,
\[
3\,T(G_p[S])\leq s_n
\qquad\text{for every }S\subseteq[n],\quad |S|=k,
\tag{11}
\]
where \(T(H)\) denotes the number of triangles of \(H\).

#### Proof

Put
\[
L=\left\lceil\frac{4\ln n}{\ln\ln n}\right\rceil.
\]
For each pair of vertices, its number of common neighbors in \(G_p\) has distribution
\[
\operatorname{Bin}(n-2,p^2).
\]
The usual binomial tail bound gives
\[
\Pr\bigl(\text{some pair has at least }L
\text{ common neighbors}\bigr)
\leq n^2\left(\frac{ec^2}{L}\right)^L
=n^{-2+o(1)}=o(1).
\tag{12}
\]

On the complementary event, every edge belongs to at most \(L\) triangles. Greedily selecting triangles and discarding all triangles sharing a selected edge therefore finds at least
\[
\frac{T(H)}{3L}
\]
edge-disjoint triangles in every subgraph \(H\subseteq G_p\).

Consequently, if (11) fails for some \(S\), then \(G_p[S]\) contains
\[
q=\left\lfloor\frac{s_n}{9L}\right\rfloor
  =\left(\frac1{36}+o(1)\right)
     k\sqrt{\ln\ln n}
\tag{13}
\]
edge-disjoint triangles.

For a fixed \(S\), a union bound over collections of \(q\) edge-disjoint triangles gives
\[
\Pr\bigl(G_p[S]\text{ contains }q
\text{ edge-disjoint triangles}\bigr)
\leq
\binom{\binom{k}{3}}q p^{3q}
\leq
\left(\frac{e\binom{k}{3}p^3}{q}\right)^q.
\tag{14}
\]
Here edge-disjointness ensures that each specified collection requires exactly \(3q\) distinct edges.

Now
\[
\binom{k}{3}p^3=\Theta((\ln n)^3),
\]
whereas (13) gives
\[
\ln\left(\frac{q}{e\binom{k}{3}p^3}\right)
=\left(\frac12+o(1)\right)\ln n.
\]
Thus the right-hand side of (14) is
\[
\exp\!\left(-\Omega\!\left(
 k\ln n\sqrt{\ln\ln n}\right)\right).
\]
This permits a union bound over all \(\binom nk\leq n^k\) choices of \(S\). Combining with (12) proves the lemma. \(\square\)

---

## 5. External survival thresholds

Fix a block collection \(\mathcal V\), with support \(S\). For a cross-block pair \(e=\{u,v\}\), define
\[
\tau_e=
\min\left\{
p,\ 
\min_{w\notin S}\max(U_{uw},U_{vw})
\right\}.
\tag{15}
\]

If \(U_e<\tau_e\), no triangle with third vertex outside \(S\) causes the filter to delete \(e\). Importantly, the thresholds \((\tau_e)_{e\in P_{\mathcal V}}\) depend only on priorities of edges joining \(S\) to its complement. They are independent of the priorities and orientations of pairs inside \(S\).

For \(0\leq t\leq p\),
\[
\Pr(\tau_e>t)=(1-t^2)^{n-k},
\]
so
\[
\begin{aligned}
\mathbb E\tau_e
&=\int_0^p(1-t^2)^{n-k}\,dt\\
&=\frac1{\sqrt n}\int_0^c
  \left(1-\frac{x^2}{n}\right)^{n-k}\,dx\\
&=\frac{I_c+o(1)}{\sqrt n}.
\end{aligned}
\tag{16}
\]

We need this expected mass to hold approximately for **every** block collection.

### Lemma 2

For every fixed \(\eta>0\), with probability tending to one,
\[
\sum_{e\in P_{\mathcal V}}\tau_e
\geq \frac{I_c-\eta}{\sqrt n}R
\qquad\text{for every }\mathcal V.
\tag{17}
\]

#### Proof

For a fixed \(\mathcal V\), put
\[
F=\frac1p\sum_{e\in P_{\mathcal V}}\tau_e.
\]
By (16),
\[
\mathbb EF=\left(\frac{I_c}{c}+o(1)\right)R.
\tag{18}
\]

The independent random inputs to \(F\) can be organized as the rows
\[
(U_{uw}:u\in S),\qquad w\notin S.
\]
Let
\[
X_w=\bigl|\{u\in S:U_{uw}\leq p\}\bigr|.
\]
The \(X_w\) are independent and distributed as \(\operatorname{Bin}(k,p)\), with
\[
kp=\Theta(\ln n).
\tag{19}
\]

We separate rows of moderate size from unusually large rows.

### 5.1 Capping the rows

Let
\[
D_0=\lceil n^{1/16}\rceil.
\]
Replace every row with \(X_w>D_0\) by a row whose entries are all \(1\), and let \(F_0\) be the resulting value of \(F\). Deleting these constraints can only increase the thresholds, so
\[
F_0\geq F,\qquad \mathbb EF_0\geq\mathbb EF.
\tag{20}
\]

Changing one capped row can affect only pairs contained in its old or new sets of entries at most \(p\). Therefore it changes \(F_0\) by at most
\[
2\binom{D_0}{2}\leq D_0^2.
\]
The bounded-differences inequality gives, for fixed \(\varepsilon>0\),
\[
\Pr(F_0<\mathbb EF-\varepsilon R)
\leq
\exp\left(-\frac{2\varepsilon^2R^2}{(n-k)D_0^4}\right)
=
\exp\left(-\Omega(n^{3/4}(\ln n)^4)\right).
\tag{21}
\]

### 5.2 Controlling the discarded rows

Let
\[
M=\lceil 2c\sqrt n\rceil,
\qquad
\mathcal M=\{\Delta(G_p)\leq M\}.
\]
A Chernoff bound and a union bound give
\[
\Pr(\mathcal M^c)=o(1).
\tag{22}
\]

On \(\mathcal M\), every \(X_w\leq M\), and restoring the discarded rows decreases \(F_0\) by at most
\[
\sum_{\substack{w\notin S\\X_w>D_0}}\binom{X_w}{2}
\leq
\sum_{w\notin S} h(X_w),
\tag{23}
\]
where
\[
h(r)=r^2\,\mathbf 1_{\{D_0<r\leq M\}}.
\]
We do **not** condition the independent rows on \(\mathcal M\); we use only implication (23).

Set
\[
A=\ln\left(\frac{D_0}{e kp}\right),
\qquad
\theta=\frac{A}{2M}.
\]
For sufficiently large \(n\), \(A>0\), and
\[
A=\left(\frac1{16}+o(1)\right)\ln n,
\qquad
\theta=\Theta\left(\frac{\ln n}{\sqrt n}\right).
\tag{24}
\]

For \(D_0<r\leq M\),
\[
\Pr(X_w=r)\leq\left(\frac{e kp}{r}\right)^r
\]
and
\[
\theta r^2-r\ln\left(\frac r{e kp}\right)
\leq \frac{Ar}{2}-Ar
=-\frac{Ar}{2}.
\]
Consequently,
\[
\mathbb E e^{\theta h(X_w)}
\leq
1+\sum_{r>D_0}e^{-Ar/2}
=
1+\exp(-\Omega(n^{1/16}\ln n)).
\]
Independence of the rows now gives
\[
\begin{aligned}
\Pr\left(\sum_{w\notin S}h(X_w)>\varepsilon R\right)
&\leq
e^{-\theta\varepsilon R}
\prod_{w\notin S}\mathbb E e^{\theta h(X_w)}\\
&\leq
\exp(-\theta\varepsilon R+o(1))\\
&=
\exp\left(-\Omega(\sqrt n(\ln n)^3)\right).
\end{aligned}
\tag{25}
\]

### 5.3 Uniformity over the certificates

Combining (21), (23), and (25), for a fixed \(\mathcal V\) we obtain
\[
\begin{aligned}
&\Pr\bigl(\mathcal M
\text{ and }F<\mathbb EF-2\varepsilon R\bigr)\\
&\quad\leq
\exp\left(-\Omega(n^{3/4}(\ln n)^4)\right)
+
\exp\left(-\Omega(\sqrt n(\ln n)^3)\right).
\end{aligned}
\tag{26}
\]

Both terms are \(\exp(-\omega(k\ln n))\). Thus (9) permits a union bound over all block collections. Using (18), choosing \(\varepsilon>0\) sufficiently small in terms of \(c,\eta\), and finally adding (22), we obtain
\[
F\geq\frac{I_c-\eta}{c}R
\]
simultaneously for every \(\mathcal V\), with probability tending to one. Multiplication by \(p=c/\sqrt n\) proves (17). \(\square\)

---

## 6. Every certificate has a surviving backward arc

Assume (3), and fix \(\eta>0\) small enough that
\[
C(I_c-\eta)>2.
\tag{27}
\]

For a block collection \(\mathcal V\), let \(X_{\mathcal V}\) count cross-block pairs \(e\) such that

1. \(U_e<\tau_e\);
2. the chosen orientation of \(e\) is backward.

Conditional on the external priorities defining the thresholds, these are independent Bernoulli events, with respective probabilities \(\tau_e/2\). Their conditional mean is
\[
\mu_{\mathcal V}
=\frac12\sum_{e\in P_{\mathcal V}}\tau_e.
\]

Whenever (17) holds for this collection,
\[
\mu_{\mathcal V}\geq
\mu_0:=\frac{I_c-\eta}{2\sqrt n}R.
\tag{28}
\]
By (6) and (7),
\[
\mu_0
=
\left(\frac{C(I_c-\eta)}4+o(1)\right)k\ln n.
\tag{29}
\]
In particular, the number \(s_n\) from Lemma 1 satisfies \(s_n=o(\mu_0)\).

For completeness, if \(X\) is a sum of independent Bernoulli variables of mean \(\mu\geq\mu_0\), the exponential-moment bound with
\[
\lambda=\ln(\mu_0/s_n)
\]
gives
\[
\begin{aligned}
\Pr(X\leq s_n)
&\leq
\exp\bigl(\lambda s_n-(1-e^{-\lambda})\mu\bigr)\\
&\leq
\exp\left(-\mu_0+s_n+s_n\ln\frac{\mu_0}{s_n}\right)\\
&=
\exp(-(1-o(1))\mu_0).
\end{aligned}
\tag{30}
\]

Applying this conditionally and then averaging,
\[
\Pr\bigl(
X_{\mathcal V}\leq s_n
\text{ and (17) holds for }\mathcal V
\bigr)
\leq \exp(-(1-o(1))\mu_0).
\]
A union bound over all \(\mathcal V\), using (9), (27), and (29), yields
\[
\begin{aligned}
N_B\exp(-(1-o(1))\mu_0)
&\leq
\exp\left[
\left(
\frac12-\frac{C(I_c-\eta)}4+o(1)
\right)k\ln n
\right]\\
&=o(1).
\end{aligned}
\tag{31}
\]

Together with Lemma 2, this shows that, with probability tending to one,
\[
X_{\mathcal V}>s_n
\qquad\text{for every }\mathcal V.
\tag{32}
\]

Now also impose the event in Lemma 1.

Every arc counted by \(X_{\mathcal V}\) is protected from deletion by triangles whose third vertex lies outside \(S\). If such an arc is nevertheless deleted by the filter, it belongs to a triangle of \(G_p[S]\). Thus at most
\[
3T(G_p[S])\leq s_n
\]
of these arcs can be deleted.

Since \(X_{\mathcal V}>s_n\), at least one backward arc survives for every \(\mathcal V\). The block certificate therefore gives
\[
\vec\alpha(D)<k.
\]

All the required events hold simultaneously with probability tending to one. The construction hence proves (4) for every fixed \(c,C>0\) satisfying \(CI_c>2\).

---

## 7. Optimizing the constant

We have
\[
I_c\uparrow\int_0^\infty e^{-t^2}\,dt
=\frac{\sqrt\pi}{2}
\qquad(c\to\infty).
\]

Therefore, for every
\[
C>\frac4{\sqrt\pi},
\]
one can choose a fixed \(c\) satisfying \(CI_c>2\). The preceding construction works for all sufficiently large \(n\), giving
\[
\limsup_{n\to\infty}
\frac{\vec a(n)}{\sqrt n\,\ln n}
\leq\frac4{\sqrt\pi}.
\]
This is (1).

Every dichromatic color class is acyclic, so the constructed graph satisfies
\[
\vec\chi(D)\geq\frac{n}{\vec\alpha(D)}.
\]
Taking reciprocals in the asymptotic bound gives (2).

---

## 8. What remains unresolved

The proved lower bound and the upper bound supplied in the question are now
\[
\left(\frac{\sqrt\pi}{4}-o(1)\right)
\frac{\sqrt n}{\ln n}
\leq
\vec t(n)
\leq
(\sqrt2+o(1))
\sqrt{\frac n{\ln n}}.
\]
The factor \(\sqrt{\ln n}\) gap remains.

The limitation of this particular filter is visible directly. A fixed pair survives with probability
\[
\int_0^{c/\sqrt n}(1-t^2)^{n-2}\,dt
=\frac{I_c+o(1)}{\sqrt n},
\]
and \(I_c\leq\sqrt\pi/2\). Thus increasing the candidate density does not increase the retained-density scale beyond \(n^{-1/2}\).

The argument establishes the stated constant improvement without relying on another conjecture. It does not provide the denser triangle-free construction, or a different orientation argument, needed to reach the conjectured order.