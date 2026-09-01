```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but it holds with polynomial bounds for graph expansions and loose forests, while component and pendant-edge reductions isolate the genuinely hard leafless cores.",
  "would_publish": false,
  "caveats": "No uniform exponent is obtained for linear cores of unbounded size or degree."
}
```

## 1. Statement and equivalent formulation

Write
\[
R_F(n)=r(F,K_n^{(3)}).
\]
A red-blue coloring of \(\binom{[N]}3\) can be identified with a red 3-graph \(H\); a blue \(K_n^{(3)}\) is then an independent set of order \(n\) in \(H\).

Consequently, the conjecture is equivalent to the following uniform Erdős-Hajnal-type statement:

> There is an absolute \(\delta>0\) such that, for every fixed linear 3-graph \(F\), there is \(c_F>0\) for which every \(F\)-free 3-graph \(H\) on \(N\) vertices satisfies
> \[
> \alpha(H)\ge c_F(\log N)^\delta .
> \]

Indeed, \(\delta=1/C\), up to changing the \(F\)-dependent constants.

I do not prove this uniform assertion. The results below establish it, in fact in polynomial form, for two substantial elementary classes and give reductions that identify where a counterexample would have to live.

---

## 2. Components do not create additional difficulty

### Lemma 2.1

If \(F=A\sqcup B\) is the vertex-disjoint union of two 3-graphs, then
\[
R_F(n)\le
\max\bigl\{R_A(n),\, |V(A)|+R_B(n)\bigr\}.
\]

#### Proof

Consider a coloring on
\[
N\ge \max\{R_A(n),|V(A)|+R_B(n)\}
\]
vertices with no blue \(K_n^{(3)}\). There is a red copy of \(A\). After deleting its vertices, at least \(R_B(n)\) vertices remain, so there is a disjoint red copy of \(B\). Their union is a red copy of \(F\). ∎

Iterating gives
\[
\max_i R_{F_i}(n)\le R_{\bigsqcup_i F_i}(n)
 \le \max_i R_{F_i}(n)+O_F(1).
\]
Thus it is enough to treat connected linear 3-graphs.

---

## 3. Adding a loose pendant edge preserves the asymptotic bound

### Lemma 3.1

Let \(F_0\) be a 3-graph with a distinguished vertex \(x\), and let \(F\) be obtained by adjoining two new vertices \(a,b\) and the single new edge \(\{x,a,b\}\). If \(f_0=|V(F_0)|\), then
\[
R_F(n)\le R_{F_0}(n)+(n-1)f_0.
\]

#### Proof

Suppose
\[
N\ge R_{F_0}(n)+(n-1)f_0
\]
and the coloring contains neither a red \(F\) nor a blue \(K_n^{(3)}\).

Greedily choose \(n\) vertex-disjoint red copies
\[
C_1,\dots,C_n
\]
of \(F_0\). This is possible because, before choosing \(C_i\), at least
\[
N-(i-1)f_0\ge R_{F_0}(n)
\]
vertices remain. Let \(x_i\) be the image of the distinguished vertex \(x\) in \(C_i\).

When \(C_i\) is selected, every triple \(\{x_i,u,v\}\) with \(u,v\) in the later reservoir must be blue: otherwise \(C_i\), together with \(u,v\), forms a red \(F\).

Hence for every \(i<j<k\), the triple
\[
\{x_i,x_j,x_k\}
\]
is blue. Thus \(\{x_1,\dots,x_n\}\) is a blue \(K_n^{(3)}\), a contradiction. ∎

### Corollary 3.2: loose forests have linear Ramsey numbers

Suppose a connected linear 3-graph \(F\) has an edge ordering
\[
e_1,\dots,e_k
\]
such that, for each \(i\ge2\),
\[
\left|e_i\cap\bigcup_{j<i}e_j\right|=1.
\]
Then, for \(n\ge3\),
\[
R_F(n)\le k^2 n.
\]

Indeed, after the first edge, every subsequent edge is a loose pendant edge. The intermediate graph with \(i-1\) edges has \(2(i-1)+1=2i-1\) vertices, so Lemma 3.1 gives
\[
R_F(n)
 \le n+(n-1)\sum_{i=2}^k(2i-1)
 =n+(n-1)(k^2-1)
 \le k^2n.
\]

Thus the conjecture holds very strongly for loose trees and, by Lemma 2.1, for loose forests.

---

## 4. Expansions of graphs have polynomial Ramsey numbers

For a simple graph \(G\), its 3-uniform expansion \(G^+\) is obtained by introducing a fresh vertex \(z_e\) for every \(e=uv\in E(G)\), with hyperedges
\[
\{u,v,z_e\},\qquad e\in E(G).
\]
Every \(G^+\) is linear.

### Theorem 4.1

Let \(G\) have \(b\) vertices and \(e\) edges, and put \(D=b+e\). Then
\[
R_{G^+}(n)
 \le r_2\!\left(G,K_{\lceil4Dn^2\rceil}\right),
\]
where the Ramsey number on the right is an ordinary graph Ramsey number. In particular,
\[
R_{G^+}(n)=O_G\!\left(n^{2(b-1)}\right).
\]

#### Proof

Let \(H\) be the red 3-graph in a coloring with no red \(G^+\). Define an auxiliary graph \(L\) on \(V(H)\) by declaring \(xy\in E(L)\) if the red codegree
\[
d_H(x,y)=|\{z:xyz\in E(H)\}|
\]
is at least \(D\).

The graph \(L\) is \(G\)-free. Indeed, if \(L\) contained a copy of \(G\), map the body vertices of \(G^+\) to this copy. For each \(uv\in E(G)\), the corresponding pair has at least \(D=b+e\) red neighbors. Greedily choose a distinct neighbor \(z_{uv}\) outside the body and outside the previously chosen expansion vertices. At every step fewer than \(b+e\) vertices are forbidden. This produces a red \(G^+\), contrary to assumption.

Set
\[
M=\lceil4Dn^2\rceil.
\]
If
\[
|V(H)|\ge r_2(G,K_M),
\]
then, because \(L\) is \(G\)-free, \(L\) has an independent set \(S\) of size \(M\). Every pair in \(S\) has red codegree less than \(D\). Therefore
\[
3e(H[S])
 =\sum_{\{x,y\}\in\binom S2}d_{H[S]}(x,y)
 <D\binom M2,
\]
so
\[
e(H[S])<\frac{DM^2}{6}.
\]

Choose each vertex of \(S\) independently with probability
\[
p=(DM)^{-1/2}.
\]
Let \(X\) be the number of selected vertices and \(Y\) the number of surviving red triples. Then
\[
\mathbb E(X-Y)
 \ge pM-p^3\frac{DM^2}{6}
 =\frac56\sqrt{\frac MD}
 \ge \frac53n.
\]
After the selection, delete one vertex from each surviving red triple. At most \(Y\) vertices are deleted, leaving an independent set of size at least \(X-Y\). Some outcome therefore leaves at least \(n\) vertices, giving a blue \(K_n^{(3)}\).

This proves the first bound. Finally,
\[
r_2(G,K_M)\le r_2(K_b,K_M)
 \le \binom{b+M-2}{b-1}
 =O_G(M^{b-1}),
\]
which yields the polynomial estimate. ∎

### Corollary 4.2

If \(F\) is linear and every edge of \(F\) contains a vertex of degree one, then \(R_F(n)\) is polynomial in \(n\).

To see this, choose one degree-one vertex \(z_e\) from every edge. These chosen vertices are automatically distinct. Removing them leaves two vertices from every hyperedge; these pairs form a simple graph \(G\), and \(F\cong G^+\), apart from irrelevant isolated vertices.

---

## 5. A pruning reduction

Repeatedly perform the following operation on a linear 3-graph:

* delete an edge which currently contains at least two degree-one vertices.

In reverse order, every deleted edge is either the first edge of a new component or is attached as a loose pendant edge. Lemmas 2.1 and 3.1 therefore give the following.

### Proposition 5.1

Let \(F^\circ\) be any terminal hypergraph obtained by the above pruning. Then, if \(F^\circ\) is nonempty,
\[
R_F(n)\le R_{F^\circ}(n)+O_F(n).
\]
If \(F^\circ\) is empty, then \(R_F(n)=O_F(n)\).

Consequently, if every edge of \(F^\circ\) has a degree-one vertex, then \(F^\circ\) is a graph expansion and \(R_F(n)\) is polynomial by Theorem 4.1.

Thus a genuinely difficult connected counterexample can be assumed to survive two-leaf pruning and to contain an edge with no degree-one vertex. In particular, all loose-forest appendages can be discarded without changing the conjectured exponent.

---

## 6. The standard canonical bound and its obstruction

Let \(\partial F\) denote the 2-shadow of \(F\): it is the graph on \(V(F)\) whose edges are all pairs contained in a hyperedge of \(F\).

### Proposition 6.1

For every fixed 3-graph \(F\),
\[
R_F(n)\le
 2^{\,O\!\left(r_2(\partial F,K_n)^2\right)}.
\]

#### Proof

The standard greedy Erdős-Rado selection gives the following canonical sequence statement: from any red-blue coloring of triples on \(2^{O(M^2)}\) vertices one can choose
\[
x_1<\cdots<x_M
\]
such that, for each \(i<j\), the color of
\[
\{x_i,x_j,x_k\}
\]
is independent of \(k>j\).

Color the graph pair \(x_ix_j\) by this stabilized color. Take
\[
M=r_2(\partial F,K_n).
\]
If the resulting graph contains a blue \(K_n\), the same vertices form a blue \(K_n^{(3)}\). If it contains a red copy of \(\partial F\), then every hyperedge of \(F\) maps to a red triple: among its three image vertices, the two earliest form an edge of \(\partial F\), hence have stabilized red color. ∎

If \(f=|V(F)|\), this gives the completely explicit but nonuniform estimate
\[
R_F(n)\le 2^{O_f(n^{2f-2})}.
\]
Equivalently, every \(F\)-free 3-graph on \(N\) vertices has an independent set of size at least
\[
c_F(\log N)^{1/(2f-2)}.
\]
The conjecture asks that the exponent \(1/(2f-2)\) be replaced by an absolute positive constant for linear \(F\).

Linearity does not make the shadows uniformly sparse. For example, let
\[
V=\mathbb F_2^d\setminus\{0\}
\]
and take the triples
\[
\{x,y,x+y\},\qquad x\ne y.
\]
This is a linear 3-graph on \(2^d-1\) vertices in which every pair belongs to exactly one hyperedge. Its shadow is therefore \(K_{2^d-1}\).

Moreover, a direct random-graph alteration shows that, for fixed \(s\),
\[
r_2(K_s,K_n)\ge c_s\left(\frac n{\log n}\right)^{s/2}.
\]
Indeed, take
\[
N=c_s(n/\log n)^{s/2},\qquad
p=A_s\log n/n.
\]
For \(A_s>s-2\), the expected number of independent \(n\)-sets in \(G(N,p)\) is \(o(1)\); choosing \(c_s\) sufficiently small makes the expected number of \(K_s\)'s at most \(N/4\). Deleting one vertex from every \(K_s\) gives the assertion.

Hence the canonical-shadow argument necessarily has an exponent growing with \(F\), even inside the class of linear 3-graphs. This is only a limitation of the argument, not a lower bound for \(R_F(n)\).

---

## 7. Why fixed finite pair-template constructions do not disprove the conjecture

A common source of hypergraph Ramsey lower bounds is to color graph pairs from a fixed finite alphabet and let the color of a triple depend on the colors of its three pairs. Such constructions cannot give a counterexample here.

Suppose
\[
\phi:\binom{[N]}2\to[q]
\]
and, for \(x<y<z\), declare \(xyz\) red according to whether
\[
(\phi(xy),\phi(xz),\phi(yz))
\]
lies in some fixed set \(\mathcal A\subseteq[q]^3\).

Let \(f=|V(F)|\) and \(T=\max\{f,n\}\). Every \(q\)-coloring of the pairs of a sufficiently large complete graph has a pair-monochromatic \(K_T\); a greedy majority argument gives the crude bound
\[
r_q(T)\le q^{O(qT)}.
\]
On such a pair-monochromatic set of color \(a\), all triples have pair-pattern \((a,a,a)\). They are therefore either all red, yielding a red \(F\), or all blue, yielding a blue \(K_n^{(3)}\). Thus every fixed-\(q\) pair-template satisfies
\[
N\le 2^{O_{F,q}(n)}
\]
whenever it avoids both objects.

There is an additional use of linearity. If \(\mathcal A\ne\varnothing\) and \(\phi\) is an independent random \(q\)-coloring of the pairs, then the resulting hypergraph contains every fixed linear \(F\) with probability tending to one. Fix an ordering of \(V(F)\) and choose one allowed pair-color pattern for each hyperedge. Because \(F\) is linear, no pair belongs to two hyperedges, so all these prescriptions are consistent. Extend them arbitrarily to a coloring of all \(\binom f2\) pairs. Each disjoint ordered \(f\)-tuple realizes this prescribed pattern with probability \(q^{-\binom f2}\), independently across disjoint tuples.

Thus a prospective counterexample cannot come from a fixed finite-state random pair construction. It would need either a number of pair states growing with \(N\), or genuinely nonlocal structure.

---

## 8. Remaining gap

The preceding arguments prove the conjecture, with the stronger choice \(C=1\), for:

1. loose forests;
2. expansions \(G^+\) of arbitrary fixed graphs;
3. linear 3-graphs which reduce to such an expansion after repeatedly pruning edges with two current degree-one vertices;
4. disjoint unions of the above.

They do not control linear cores with no useful degree-one structure, such as finite projective Steiner triple systems. The canonical bound only yields a polylogarithmic independent set with an exponent tending to zero as \(|V(F)|\) grows.

To disprove the conjecture one would need, for arbitrarily large \(D\), a fixed linear \(F_D\) and \(F_D\)-free 3-graphs with
\[
\alpha(H)<n
\quad\text{and}\quad
\log |V(H)|\gg n^D.
\]
No such construction is provided here. Conversely, none of the arguments establishes an absolute lower exponent in
\[
\alpha(H)\ge(\log |V(H)|)^\delta
\]
for the remaining leafless cores. That is the unresolved step.