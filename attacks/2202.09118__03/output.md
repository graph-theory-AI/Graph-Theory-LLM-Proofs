```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full closure problem remains open, but there is an explicit exponential binding function, a direct quantitative proof when one component is K1 or K2, and a probabilistic lower bound on the degree of any possible polynomial.",
  "would_publish": false,
  "caveats": "No case with two general diameter-three trees is resolved; the qualitative K1/K2 cases follow already from the supplied P4 theorem, and the novelty of the lower bound has not been checked."
}
```

# Mathematical writeup

## 1. Statement and conventions

All graphs are finite and simple, and “\(H\)-free” means induced-\(H\)-free. Write \(H_1\dot\cup H_2\) for disjoint union with no edges between the two parts.

A graph \(H\) is **good** if there is a polynomial \(p_H\) such that every \(H\)-free graph \(G\) satisfies
\[
\chi(G)\le p_H(\omega(G)).
\]

The open problem asks whether \(H_1\dot\cup H_2\) is good whenever \(H_1,H_2\) are good trees.

I do not resolve this. I give three precise partial results.

---

## 2. A general explicit exponential bound

### Proposition 2.1

Suppose \(H_1,H_2\) have nondecreasing \(\chi\)-binding functions \(p_1,p_2\), respectively. Fix \(i\in\{1,2\}\), put \(j=3-i\), and let
\[
h=|V(H_i)|.
\]
Define
\[
F_i(0)=0,\qquad
F_i(w)=hF_i(w-1)+p_1(w)+p_2(w)+h
\quad (w\ge 1).
\]
Then every \((H_1\dot\cup H_2)\)-free graph \(G\) satisfies
\[
\chi(G)\le F_i(\omega(G)).
\]

Consequently, if \(p_1,p_2=O(w^d)\), then
\[
\chi(G)=
\begin{cases}
O(w^{d+1}),& h=1,\\[2mm]
O(h^w w^d),& h\ge 2.
\end{cases}
\]
One may choose the orientation with \(h=\min\{|H_1|,|H_2|\}\).

### Proof

Induct on \(w=\omega(G)\). If \(G\) is \(H_i\)-free, then
\[
\chi(G)\le p_i(w)\le F_i(w).
\]

Otherwise, fix an induced copy \(A=\{a_1,\dots,a_h\}\) of \(H_i\). Let
\[
Z=\{v\in V(G)\setminus A:N(v)\cap A=\varnothing\}.
\]
Then \(G[Z]\) is \(H_j\)-free: an induced \(H_j\) in \(Z\), together with \(A\), would induce \(H_1\dot\cup H_2\). Hence
\[
\chi(G[Z])\le p_j(w).
\]

Every remaining vertex outside \(A\cup Z\) has a neighbor in \(A\). Partition these vertices into \(R_1,\dots,R_h\), assigning a vertex to \(R_r\) when \(a_r\) is its first neighbor in the chosen ordering of \(A\). Then \(R_r\subseteq N(a_r)\). Therefore
\[
\omega(G[R_r])\le w-1,
\]
because any clique in \(R_r\), together with \(a_r\), is a larger clique. Each \(G[R_r]\) remains \((H_1\dot\cup H_2)\)-free, so induction gives
\[
\chi(G[R_r])\le F_i(w-1).
\]

Using disjoint palettes,
\[
\chi(G)
 \le h+p_j(w)+\sum_{r=1}^h\chi(G[R_r])
 \le h+p_j(w)+hF_i(w-1)
 \le F_i(w).
\]
This proves the recurrence. Its explicit solution is
\[
F_i(w)=\sum_{r=1}^w h^{\,w-r}
       \bigl(p_1(r)+p_2(r)+h\bigr),
\]
from which the asymptotic estimates follow. ∎

### Significance and limitation

Thus the disjoint union is always exponentially \(\chi\)-bounded under the hypotheses of the conjecture. However, for \(h\ge2\), this argument does not give a polynomial. Indeed, a proposed induction \(F(w)=Cw^D\) would require absorbing
\[
hC(w-1)^D,
\]
but
\[
\frac{h(w-1)^D}{w^D}\longrightarrow h>1.
\]
Increasing the fixed exponent \(D\) does not repair this obstruction.

---

## 3. Quantitative closure when one component is \(K_1\) or \(K_2\)

The maximum-clique argument below avoids the preceding multiplicative recurrence.

### Proposition 3.1: adding an isolated vertex

Let \(F\) be any graph whose \(F\)-free graphs satisfy
\[
\chi(G)\le p(\omega(G)).
\]
Then every \((F\dot\cup K_1)\)-free graph \(G\), with \(w=\omega(G)\), satisfies
\[
\boxed{\chi(G)\le w\,p(w)+w.}
\]

#### Proof

Let \(Q=\{q_1,\dots,q_w\}\) be a maximum clique. Every vertex \(v\notin Q\) has a nonneighbor in \(Q\), since otherwise \(Q\cup\{v\}\) would be a larger clique. Assign \(v\) to one such nonneighbor \(q_i\), obtaining sets \(Y_1,\dots,Y_w\).

Every vertex of \(Y_i\) is nonadjacent to \(q_i\). Thus \(G[Y_i]\) is \(F\)-free: an induced copy of \(F\) in \(Y_i\), together with \(q_i\), would induce \(F\dot\cup K_1\). Hence each \(Y_i\) is \(p(w)\)-colorable. Coloring the \(Y_i\)'s with disjoint palettes and \(Q\) with \(w\) further colors proves the bound. ∎

### Proposition 3.2: adding an edge

Under the same hypothesis on \(F\), every \((F\dot\cup K_2)\)-free graph \(G\), with \(w=\omega(G)\), satisfies
\[
\boxed{\chi(G)\le \binom{w}{2}p(w)+w.}
\]

#### Proof

Again let \(Q=\{q_1,\dots,q_w\}\) be a maximum clique. For \(v\notin Q\), put
\[
M(v)=\{i:vq_i\notin E(G)\}.
\]
This set is nonempty.

First consider vertices with \(M(v)=\{i\}\); call their set \(X_i\). The set \(X_i\) is stable. Indeed, if \(x,y\in X_i\) were adjacent, then both would be complete to \(Q\setminus\{q_i\}\), and
\[
(Q\setminus\{q_i\})\cup\{x,y\}
\]
would be a clique of size \(w+1\). Moreover, \(q_i\) is anticomplete to \(X_i\). Thus \(Q\cup\bigcup_iX_i\) is colorable with \(w\) colors by giving \(q_i\cup X_i\) color \(i\).

For every remaining vertex \(v\), choose a pair \(\{i,j\}\subseteq M(v)\), and let \(Y_{ij}\) be the vertices assigned to that pair. The edge \(q_iq_j\) is anticomplete to \(Y_{ij}\). Consequently \(G[Y_{ij}]\) is \(F\)-free, since an induced \(F\) there would combine with \(q_iq_j\) to give \(F\dot\cup K_2\). Hence
\[
\chi(G[Y_{ij}])\le p(w).
\]
There are \(\binom w2\) such classes, proving the claim. ∎

### Corollary 3.3: \(2K_2\)-free graphs

Taking \(F=K_2\), for which \(p(w)=1\), gives
\[
\boxed{\chi(G)\le \binom{w+1}{2}}
\]
for every \(2K_2\)-free graph \(G\).

Qualitatively, Propositions 3.1 and 3.2 are subsumed by the supplied result that \(F\dot\cup P_4\) is good whenever \(F\) is a good forest, since both \(K_1\) and \(K_2\) occur as induced subgraphs of \(P_4\). The displayed bounds are direct and quantitative.

The same propositions can also be iterated to add any fixed number of isolated vertices or independent edges, with a controlled increase in polynomial degree.

---

## 4. A probabilistic lower bound on any binding polynomial

The following shows that a prospective proof cannot generally produce a low-degree polynomial.

For a graph \(J\), define its maximum \(1\)-density by
\[
\rho(J)=
\max_{\substack{J_0\subseteq J\\ |V(J_0)|\ge2,\ e(J_0)>0}}
\frac{e(J_0)}{|V(J_0)|-1},
\]
where \(J_0\) need not be induced.

### Proposition 4.1

Let \(L\) be a fixed graph, put \(J=\overline L\), and suppose \(\rho(J)>1\). If every induced-\(L\)-free graph satisfies a bound
\[
\chi(G)=O(\omega(G)^D),
\]
then
\[
\boxed{D\ge \rho(J).}
\]

More explicitly, for every
\[
\frac1{\rho(J)}<a<1
\]
there are arbitrarily large induced-\(L\)-free graphs \(G\) with
\[
\chi(G)\ge c_a|V(G)|
\quad\text{and}\quad
\omega(G)\le C_a |V(G)|^a\log |V(G)|.
\]

### Proof

Choose \(J_0\subseteq J\) attaining \(\rho(J)\), and write
\[
k=|V(J_0)|,\qquad e=e(J_0).
\]
Let \(a\) satisfy
\[
\frac{k-1}{e}<a<1,
\]
and take
\[
R\sim G(n,q),\qquad q=n^{-a}.
\]

We use three standard first-moment estimates.

1. **Few copies of \(J_0\).**  
   The expected number \(X\) of copies of \(J_0\) is at most
   \[
   \mathbb E X\le n^kq^e=n^{k-ae}=o(n),
   \]
   because \(ae>k-1\).

2. **Bounded clique number.**  
   Choose a fixed integer \(r\) satisfying \(a(r-1)>2\). Then
   \[
   \mathbb E[\#K_r]
   \le n^r q^{\binom r2}
   =n^{\,r-a\binom r2}=o(1).
   \]
   Thus with probability tending to one, \(\omega(R)\le r-1\).

3. **Small independence number.**  
   Put
   \[
   \ell=\left\lceil 8q^{-1}\log n\right\rceil.
   \]
   Then
   \[
   \Pr(\alpha(R)\ge\ell)
   \le \binom n\ell(1-q)^{\binom\ell2}
   \le \left(\frac{en}{\ell}\right)^\ell
      \exp\!\left(-q\binom\ell2\right)
   =o(1).
   \]
   Hence \(\alpha(R)\le 8n^a\log n+1\) with high probability.

Choose a realization satisfying all three properties and with \(X\le n/4\). Delete one selected vertex from every copy of \(J_0\). The resulting induced subgraph \(R'\) has at least \(3n/4\) vertices, is \(J_0\)-free, and still satisfies
\[
\omega(R')\le r-1,\qquad
\alpha(R')\le 8n^a\log n+1.
\]

Let
\[
G=\overline{R'}.
\]
If \(G\) contained an induced copy of \(L\), then \(R'\) would contain an induced copy of \(J=\overline L\), and hence a subgraph isomorphic to \(J_0\), a contradiction. Thus \(G\) is induced-\(L\)-free.

Moreover,
\[
\omega(G)=\alpha(R')\le 8n^a\log n+1.
\]
Every stable set of \(G\) is a clique of \(R'\), and therefore has size at most \(r-1\). Hence
\[
\chi(G)\ge \frac{|V(G)|}{r-1}=\Omega(n).
\]

If \(D<\rho(J)\), choose \(a\) with
\[
\frac1{\rho(J)}<a<\frac1D.
\]
Then a putative \(O(\omega^D)\) bound would give
\[
\chi(G)=O\!\left(n^{aD}(\log n)^D\right)=o(n),
\]
contradicting the lower bound above. Therefore \(D\ge\rho(J)\). ∎

---

## 5. Consequence for a disjoint union of two trees

Let
\[
L=H_1\dot\cup H_2,\qquad
v=|V(H_1)|+|V(H_2)|.
\]
Since \(H_1,H_2\) are trees,
\[
e(L)=(|H_1|-1)+(|H_2|-1)=v-2.
\]
Thus
\[
e(\overline L)=\binom v2-v+2.
\]
Using the whole graph \(\overline L\) in the definition of \(\rho\) gives
\[
\rho(\overline L)
\ge
\frac{\binom v2-v+2}{v-1}
=
\frac{v-2}{2}+\frac1{v-1}.
\]

Therefore any binding polynomial for \(H_1\dot\cup H_2\) must have degree at least
\[
\boxed{\left\lfloor\frac v2\right\rfloor}
\qquad (v\ge4).
\]

In particular:

- every polynomial binding function for \(2K_2\)-free graphs must have degree at least \(2\); combined with Corollary 3.3, the minimum ordinary polynomial degree is exactly \(2\);
- if both trees have diameter exactly three, then each has at least four vertices, so \(v\ge8\);
- consequently, no cubic polynomial can bind the chromatic number for the disjoint union of two diameter-three trees. For \(2P_4\), for example,
  \[
  \rho(\overline{2P_4})\ge\frac{22}{7}>3.
  \]

The invariant \(\rho(\overline L)\) can be larger than the displayed whole-graph lower bound for some tree shapes.

---

## 6. Remaining gap

The unresolved case begins when neither component can be supplied by a maximum clique. For \(K_1\) and \(K_2\), grouping vertices by common nonneighbors in a maximum clique produces classes that are immediately \(H\)-free. A tree on at least three vertices is not a clique, so the same partition does not produce an induced copy of that tree anticomplete to a class.

Anchoring an actual induced copy of \(H_1\) instead gives Proposition 2.1, but creates \(|H_1|\) recursively colored neighborhoods of clique number \(w-1\). The resulting coefficient greater than one yields an exponential recurrence, and no argument above permits those palettes to be reused.

Thus none of these arguments settles the case of two arbitrary good trees, or even two arbitrary diameter-three trees. The probabilistic construction only supplies a necessary polynomial degree; it does not give a superpolynomial counterexample.