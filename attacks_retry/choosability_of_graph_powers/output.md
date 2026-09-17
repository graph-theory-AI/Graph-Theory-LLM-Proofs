```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A local-palette argument gives O(k log k) for a bounded-fibre quotient class containing arbitrarily large regular roots with square degree (k-1)^2, but does not settle the unrestricted question.",
  "would_publish": false,
  "caveats": "The quotient hypothesis is additional; no universal o(k^2) bound or claim of novelty is obtained."
}
```

## 1. A partial result using bounded-fibre quotients

All graphs are finite and simple, and logarithms are natural.

A graph homomorphism \(\phi:G\to B\) is **locally injective** if its restriction to \(N_G(v)\) is injective for every vertex \(v\). In particular, graph covering maps are locally injective.

The following gives a sufficient condition different from the degeneracy and block-order conditions in the previous attempt.

**Theorem.** Suppose that \(G\) admits a locally injective homomorphism
\[
\phi:G\longrightarrow B
\]
such that every fibre \(\phi^{-1}(x)\) has at most \(s\) vertices. Put
\[
D=\Delta(B^2).
\]
Then
\[
\boxed{\displaystyle
\operatorname{ch}(G^2)
\le
\left\lceil
(D+1)\bigl(1+\ln(s(D^2+1))\bigr)
\right\rceil .
} \tag{1}
\]

Consequently, writing \(k=\chi(G^2)\):

* if \(D=O(k)\) and \(\ln s=o(k)\), then
  \[
  \operatorname{ch}(G^2)=o(k^2);
  \]
* if \(D\le Ck\) and \(s\le k^A\), for fixed \(A,C\), then
  \[
  \operatorname{ch}(G^2)=O_{A,C}(k\log k).
  \]

There is **no restriction on the order of \(B\)**. Below I construct examples covered by this theorem in which
\[
\chi(G^2)=k,\qquad
\Delta(G)=\operatorname{degeneracy}(G)=k-1,\qquad
\Delta(G^2)=(k-1)^2,
\]
and \(G\) is Hamiltonian of arbitrarily large order. Thus the result is not merely exploiting small root degree, small square degree, or small blocks.

## 2. Proof: local palettes indexed by quotient vertices

The key is a list-colouring lemma for bounded-fibre homomorphisms.

**Lemma.** Let \(\psi:H\to J\) be a graph homomorphism. Suppose
\[
|\psi^{-1}(x)|\le s\quad\text{for every }x\in V(J),
\qquad
\Delta(J)\le D.
\]
Then
\[
\operatorname{ch}(H)
\le
\left\lceil
(D+1)\bigl(1+\ln(s(D^2+1))\bigr)
\right\rceil . \tag{2}
\]

**Proof.** The case \(D=0\) is immediate, since \(H\) is edgeless. Assume \(D\ge1\), and put
\[
L=\left\lceil
(D+1)\bigl(1+\ln(s(D^2+1))\bigr)
\right\rceil .
\]
Consider any assignment of lists of size \(L\) to \(V(H)\), and let \(\mathcal C\) be their union.

Independently for every pair
\[
(x,c)\in V(J)\times\mathcal C,
\]
choose a uniform random variable \(U_{x,c}\in[0,1]\).

Say that \(x\) **owns** \(c\) when
\[
U_{x,c}<U_{y,c}\qquad\text{for every }y\in N_J(x).
\]
Adjacent vertices of \(J\) cannot own the same colour.

For \(v\in V(H)\), let \(E_v\) be the event that \(\psi(v)\) owns no colour in \(L(v)\). For a fixed colour \(c\),
\[
\Pr(\psi(v)\text{ owns }c)
=\frac{1}{\deg_J(\psi(v))+1}
\ge\frac1{D+1}.
\]
The ownership tests for distinct colours use disjoint random variables. Hence
\[
\Pr(E_v)
\le
\left(1-\frac1{D+1}\right)^L
\le e^{-L/(D+1)}
\le \frac{1}{e\,s(D^2+1)}. \tag{3}
\]

The event \(E_v\) depends only on variables whose first coordinate lies in
\[
N_J[\psi(v)].
\]
Thus it is independent of the collection of events \(E_w\) for which
\[
\operatorname{dist}_J(\psi(v),\psi(w))>2.
\]
A radius-two ball in \(J\) has at most
\[
1+D+D(D-1)=D^2+1
\]
vertices. Therefore each bad event has at most
\[
s(D^2+1)-1
\]
other events in this dependency graph.

The symmetric Lovász local lemma, using (3), gives a positive probability that no \(E_v\) occurs. For such an outcome, choose at every \(v\) a listed colour owned by \(\psi(v)\). If \(vw\in E(H)\), then \(\psi(v)\psi(w)\in E(J)\), so these two quotient vertices cannot own the same colour. The resulting list colouring is proper. \(\square\)

The locality here is genuine: variables are indexed by **both a quotient vertex and a colour**. A colour occurring far away need not use the same random decision.

### Applying the lemma to squares

If \(\phi:G\to B\) is locally injective, then it induces a graph homomorphism
\[
G^2\longrightarrow B^2. \tag{4}
\]

Indeed, the only potential difficulty is a two-edge path \(u v w\) with \(\phi(u)=\phi(w)\). Local injectivity at \(v\) excludes this when \(u\ne w\). Thus distinct vertices at distance at most two in \(G\) map to distinct vertices at distance at most two in \(B\).

Apply the lemma with \(H=G^2\), \(J=B^2\), and the same fibres. This proves (1).

For example, under \(D\le Ck\) and \(s\le k^A\),
\[
\operatorname{ch}(G^2)
\le
(Ck+1)\bigl((A+2)\ln k+O_C(1)\bigr)+1.
\]

## 3. Arbitrarily large regular roots covered by the bound

Here is a concrete family demonstrating that the quotient condition can help even when the elementary quadratic degree bound is fully saturated.

### 3.1. The quotient graphs

Fix \(k\ge4\) and \(n\ge3\). Define \(B_{k,n}\) on
\[
\mathbb Z_n\times[k]
\]
as follows:

* within each cell \(\{a\}\times[k]\), put a copy of \(K_k\) with the edge \(12\) deleted;
* add the edges
  \[
  (a,1)(a+1,2)\qquad(a\in\mathbb Z_n).
  \]

Every vertex has exactly one neighbour of each other second coordinate. Consequently \(B_{k,n}\) is \((k-1)\)-regular, and colouring \((a,i)\) by \(i\) properly colours its square.

A direct count gives
\[
\deg_{B_{k,n}^2}(a,i)=
\begin{cases}
2k-2,&i\in\{1,2\},\\
k+1,&i\notin\{1,2\}.
\end{cases}
\]
Thus
\[
\Delta(B_{k,n}^2)=2k-2. \tag{5}
\]

Let \(F\) be any \(s\)-sheet cover of \(B_{k,n}\). It is again \((k-1)\)-regular, and the second-coordinate colouring pulls back to a proper \(k\)-colouring of \(F^2\). Every closed neighbourhood in \(F\) is a \(k\)-clique in \(F^2\), so
\[
\chi(F^2)=k. \tag{6}
\]

The theorem now yields
\[
\boxed{\displaystyle
\operatorname{ch}(F^2)
\le
\left\lceil
(2k-1)\left(1+\ln\!\left(s\bigl((2k-2)^2+1\bigr)\right)\right)
\right\rceil .
} \tag{7}
\]

In particular, polynomial-sheet covers satisfy \(O(k\log k)\), independently of \(n\).

### 3.2. Covers with girth at least five and one arbitrarily large block

I next show that, with \(s=k^4\), such covers can simultaneously be Hamiltonian and have girth at least five.

Use the additive group
\[
\Gamma=\mathbb Z_s.
\]
For each oriented internal edge \(ij\) of \(K_k-12\), assign a voltage \(a_{ij}\in\Gamma\), with \(a_{ji}=-a_{ij}\). Use the same internal voltages in every cell.

Choose the voltages independently and uniformly on one orientation of each internal edge. For each fixed triangle or four-cycle of \(K_k-12\), its voltage sum is uniform in \(\Gamma\), so it is zero with probability \(1/s\). There are at most
\[
\binom{k}{3}+3\binom{k}{4}<k^4=s
\]
such cycles. By the union bound, an assignment exists for which every triangle and four-cycle has nonzero voltage. Fix one.

The graph \(B_{k,n}\) has a Hamiltonian cycle that traverses each cell along
\[
2,3,\ldots,k,1
\]
and then uses the cross-edge to the next cell. Assign voltages to the cross-edges so that this Hamiltonian cycle has total voltage \(1\in\Gamma\): set all but one cross-edge voltage to zero and choose the remaining one accordingly.

Form the voltage cover \(F\): an oriented base edge \(x\to y\) with voltage \(a\) gives the edges
\[
(x,z)(y,z+a)\qquad(z\in\Gamma).
\]
This is an \(s\)-sheet cover.

The base Hamiltonian cycle lifts to a Hamiltonian cycle of \(F\). Indeed, one traversal increases the sheet coordinate by \(1\), and \(1\) generates \(\mathbb Z_s\).

Also, \(F\) has no triangle or four-cycle. To see this:

1. A triangle or four-cycle in a cover projects to a closed nonbacktracking walk of the same length.
2. In a simple graph, such a walk of length three or four is a triangle or four-cycle.
3. Every triangle or four-cycle of \(B_{k,n}\) lies inside a cell. A cycle using cross-edges must traverse the cyclic arrangement of cells; its length is at least \(3n\ge9\).
4. The internal voltage choices prevent these short base cycles from lifting to closed cycles of the same length.

Therefore \(F\) is \((k-1)\)-regular of girth at least five. The vertices reached by one- and two-edge paths from a given vertex are all distinct except for the prescribed path origins, giving
\[
\Delta(F^2)
=(k-1)+(k-1)(k-2)
=(k-1)^2. \tag{8}
\]

Combining the properties,
\[
\begin{aligned}
|V(F)|&=nk^5,\\
\operatorname{degeneracy}(F)&=k-1,\\
\chi(F^2)&=k,\\
\Delta(F^2)&=(k-1)^2.
\end{aligned}
\]
Since \(F\) is Hamiltonian, it is one block. Nevertheless, (7) gives
\[
\operatorname{ch}(F^2)
\le
(2k-1)\bigl(6\ln k+1+\ln4\bigr)+1
=O(k\log k). \tag{9}
\]

Taking, for example, \(n\ge e^{k^2}\), neither sublinear degeneracy nor subexponential block order applies. The quotient argument still does.

## 4. What remains unresolved

I checked the regular-completion lemma in the supplied attempt; it is valid and explains precisely where the unrestricted difficulty remains.

Suppose \(\chi(G^2)=k\ge2\), and fix a proper \(k\)-colouring with classes \(V_1,\ldots,V_k\). Between two classes, the edges of \(G\) form a matching: two vertices of one class cannot have a common neighbour.

Add isolated vertices to equalize the class sizes, and complete every matching between two classes to a perfect matching. The resulting graph \(F\) is \((k-1)\)-regular, with exactly one neighbour in every other class at each vertex. Thus
\[
F\longrightarrow K_k
\]
is a covering map,
\[
\chi(F^2)=k,
\qquad
\operatorname{ch}(G^2)\le\operatorname{ch}(F^2).
\]

So arbitrary finite covers of \(K_k\) must still be handled.

For the always-available quotient \(F\to K_k\), the fibre size is
\[
s=\frac{|V(F)|}{k},
\]
which is unrestricted. The local-palette theorem then gives only
\[
\operatorname{ch}(F^2)
\le
k\ln s+O(k\ln k).
\]
When \(\ln s\) is comparable to or larger than \(k\), this does not give the required subquadratic bound.

Nothing above guarantees that an arbitrary cover admits a **different** quotient with small fibres and square degree \(O(k)\). That is the missing hypothesis, not an established structural property of all covers.

Thus the argument proves a substantial special-case criterion, including the large regular examples above, but establishes neither Noel’s unrestricted \(o(k^2)\) bound nor the proposed universal \(O(k\log k)\) strengthening.