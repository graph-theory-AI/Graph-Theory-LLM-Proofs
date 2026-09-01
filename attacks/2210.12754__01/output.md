```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For fixed p I prove sharp whp orders n log n for induced-star-free graphs and n^(3/2)(log n)^(1/2) for induced-K_{2,t}-free graphs with t at least 3, while the arbitrary hereditary case remains open.",
  "would_publish": false,
  "caveats": "Only special complete-bipartite exclusions are settled; induced C4 retains a logarithmic gap, general bipartite exclusions remain open, and novelty relative to arXiv:2405.09486 is unchecked."
}
```

## 1. Statement of the partial result

Throughout, \(p\in(0,1)\) and all other graph parameters are fixed as \(n\to\infty\). Hereditary means closed under taking induced subgraphs. Let

\[
\mathcal Q_{s,t}:=\operatorname{Forb}_{\mathrm{ind}}(K_{s,t}).
\]

Thus, if a hereditary property \(\mathcal P\) does not contain \(K_{s,t}\), then

\[
\mathcal P\subseteq \mathcal Q_{s,t}.
\]

The following gives sharp orders for two natural families in the bipartite-missing regime.

### Theorem 1

Let \(1\le s\le t\).

1. With high probability,
   \[
   \operatorname{ex}\bigl(G(n,p),\mathcal Q_{s,t}\bigr)
   =O_{p,s,t}\!\left(n^{2-1/s}(\log n)^{1/s}\right).
   \]
   Consequently, the same upper bound holds for every hereditary \(\mathcal P\) with \(K_{s,t}\notin\mathcal P\).

2. For every fixed \(t\ge2\),
   \[
   \operatorname{ex}\bigl(G(n,p),\mathcal Q_{1,t}\bigr)
   =\Theta_{p,t}(n\log n)
   \qquad\text{whp}.
   \]

3. For every fixed \(t\ge3\),
   \[
   \operatorname{ex}\bigl(G(n,p),\mathcal Q_{2,t}\bigr)
   =\Theta_{p,t}\!\left(n^{3/2}(\log n)^{1/2}\right)
   \qquad\text{whp}.
   \]

4. For induced \(C_4=K_{2,2}\), the argument leaves the gap
   \[
   \Omega_p(n^{3/2})
   \le
   \operatorname{ex}\bigl(G(n,p),\mathcal Q_{2,2}\bigr)
   \le
   O_p\!\left(n^{3/2}(\log n)^{1/2}\right)
   \qquad\text{whp}.
   \]

Part 1 is the complete-bipartite upper bound reported in the supplied literature review; a self-contained proof is included. Parts 2 and 3 show that the logarithmic factor is genuinely needed for the maximal induced-\(K_{s,t}\)-free properties when \(s=1\), and when \(s=2,t\ge3\).

---

## 2. A uniform random-graph lemma

For a graph \(J\), write \(i_k(J)\) for its number of independent \(k\)-sets.

### Lemma 2.1

For every fixed \(k\ge1\) and \(p\in(0,1)\), there are constants \(A,c>0\) such that, with high probability, every \(U\subseteq V(G(n,p))\) with

\[
|U|\ge A\log n
\]

satisfies

\[
i_k(G[U])\ge c|U|^k.
\]

#### Proof

The case \(k=1\) is immediate. Assume \(k\ge2\), and fix \(U\) with \(|U|=m\). Let \(X=i_k(G[U])\). Then

\[
\mu:=\mathbb E X
=(1-p)^{\binom{k}{2}}\binom{m}{k}
\ge c_0m^k
\]

for a constant \(c_0=c_0(p,k)>0\).

Expose the \(\binom m2\) edge indicators inside \(U\). Changing one edge changes \(X\) by at most

\[
\binom{m-2}{k-2}\le m^{k-2}.
\]

McDiarmid's bounded-difference inequality therefore gives

\[
\Pr(X\le\mu/2)
\le
\exp(-c_1m^2)
\]

for some \(c_1=c_1(p,k)>0\).

There are at most \((en/m)^m\) choices for \(U\). Hence, for \(m\ge A\log n\),

\[
\Pr\bigl(\exists U,\ |U|=m,\ X\le\mu/2\bigr)
\le
\exp\left(m\log\frac{en}{m}-c_1m^2\right).
\]

Choosing \(A\) sufficiently large makes the sum of these probabilities over all \(m\ge A\log n\) tend to zero. ∎

---

## 3. The complete-bipartite upper bound

We prove Theorem 1(1).

Work on the high-probability event of Lemma 2.1 simultaneously for \(k=s\) and \(k=t\). Let

\[
L=A\log n
\]

with \(A\) sufficiently large for both values.

Let \(H\subseteq G(n,p)\) be induced-\(K_{s,t}\)-free. For an \(s\)-set \(S\), let

\[
d_H(S):=\left|\bigcap_{x\in S}N_H(x)\right|.
\]

If \(S\) is independent in the host \(G\), then \(S\) is also independent in \(H\). We claim that

\[
d_H(S)<L. \tag{3.1}
\]

Indeed, if the common neighborhood had at least \(L\) vertices, Lemma 2.1 would give an independent \(t\)-set \(T\) in the host inside that common neighborhood. The sets \(S\) and \(T\) are independent in \(H\), and all \(st\) edges between them belong to \(H\), giving an induced \(K_{s,t}\), a contradiction.

Now double-count pairs \((v,S)\) where \(S\) is an independent \(s\)-set in \(G[N_H(v)]\). We obtain

\[
\sum_{v}i_s\bigl(G[N_H(v)]\bigr)
=
\sum_{\substack{S\subseteq V(G)\\ |S|=s,\ S\text{ independent in }G}}
d_H(S)
\le
L\binom ns. \tag{3.2}
\]

By Lemma 2.1, whenever \(d_H(v)\ge L\),

\[
i_s\bigl(G[N_H(v)]\bigr)\ge c\,d_H(v)^s.
\]

Thus (3.2), with the vertices of degree below \(L\) added trivially, yields

\[
\sum_v d_H(v)^s
\le
C\left(Ln^s+nL^s\right)
=
O(Ln^s). \tag{3.3}
\]

Hölder's inequality gives

\[
(2e(H))^s
=
\left(\sum_v d_H(v)\right)^s
\le
n^{s-1}\sum_vd_H(v)^s
=
O\!\left(Ln^{2s-1}\right).
\]

Therefore

\[
e(H)
=
O\!\left(n^{2-1/s}L^{1/s}\right)
=
O\!\left(n^{2-1/s}(\log n)^{1/s}\right).
\]

The estimate is uniform over every \(H\subseteq G\), proving the desired high-probability upper bound.

Finally, if \(\mathcal P\) is hereditary and \(K_{s,t}\notin\mathcal P\), no graph in \(\mathcal P\) can contain an induced \(K_{s,t}\). Hence \(\mathcal P\subseteq\mathcal Q_{s,t}\), proving the asserted consequence. ∎

---

## 4. Packing logarithmic cliques

The lower constructions use linearly many vertices partitioned into logarithmic host cliques.

### Lemma 4.1

For every fixed \(q\in(0,1)\), there is \(a=a(q)>0\) such that, with high probability, \(G(n,q)\) contains at least

\[
\frac{n}{3r}
\]

vertex-disjoint \(r\)-cliques, where \(r=\lfloor a\log n\rfloor\).

#### Proof

It suffices to prove that, with high probability, every set of \(\lfloor n/2\rfloor\) vertices contains an \(r\)-clique. Greedy removal then covers more than \(n/2\) vertices by disjoint \(r\)-cliques.

Fix a set \(U\) of size \(m=\lfloor n/2\rfloor\), and let \(X\) count its \(r\)-cliques. Put \(\beta=\log(1/q)\). Then

\[
\mu=\mathbb EX=\binom mr q^{\binom r2}.
\]

For \(a>0\) sufficiently small,

\[
\log\mu
\ge
r\log(m/r)-\frac{\beta r^2}{2}
\ge
c(\log n)^2. \tag{4.1}
\]

For the Janson dependency term \(\Delta\), two clique indicators are dependent only when their vertex sets overlap in at least two vertices. Normalizing by \(\mu^2\),

\[
\frac{\Delta}{\mu^2}
\le
\sum_{j=2}^{r-1}
\frac{\binom rj\binom{m-r}{r-j}}{\binom mr}
q^{-\binom j2}.
\]

The hypergeometric factor is at most

\[
\left(\frac{C r^2}{m}\right)^j.
\]

The logarithm of the resulting summand is a convex function of \(j\), so its maximum occurs at \(j=2\) or \(j=r-1\). For \(a\) sufficiently small, the \(j=2\) term is \(O(r^4/n^2)\), while the \(j=r-1\) term is \(\exp(-c(\log n)^2)\). Consequently,

\[
\frac{\Delta}{\mu^2}=O\left(\frac{r^5}{n^2}\right).
\]

Janson's inequality and (4.1) now give

\[
\Pr(X=0)
\le
\exp\left(-\Omega\left(\frac{n^2}{r^5}\right)\right).
\]

A union bound over at most \(2^n\) choices of \(U\) proves that every \(n/2\)-set contains an \(r\)-clique. Greedily removing such cliques gives at least \(n/(3r)\) disjoint \(r\)-cliques. ∎

---

## 5. A general lower-bound transfer

Let

\[
z_{s,t}(m):=\operatorname{ex}(m,K_{s,t})
\]

denote the ordinary deterministic Turán number.

### Proposition 5.1

Fix \(2\le s\le t\), with \((s,t)\ne(2,2)\). There is \(a=a(p)>0\) such that, with

\[
r=\lfloor a\log n\rfloor,
\qquad
M=\left\lfloor\frac{n}{4r}\right\rfloor,
\]

we have, with high probability,

\[
\operatorname{ex}\bigl(G(n,p),\mathcal Q_{s,t}\bigr)
\ge
M\binom r2+c_pr^2z_{s,t}(M). \tag{5.1}
\]

#### Construction

Expose \(G(n,p)\) in two rounds. Let \(G_1,G_2\) be independent copies of \(G(n,p_*)\), where

\[
p_*=1-\sqrt{1-p}.
\]

Then \(G_1\cup G_2\) has distribution \(G(n,p)\).

Using \(G_1\) and Lemma 4.1, choose disjoint \(r\)-cliques

\[
Q_1,\dots,Q_M.
\]

Take an ordinary \(K_{s,t}\)-free graph on \(M\) vertices with \(z_{s,t}(M)\) edges. A random bipartition retains half its edges in expectation, so it has a bipartite \(K_{s,t}\)-free subgraph \(B\) satisfying

\[
e(B)\ge \frac12z_{s,t}(M). \tag{5.2}
\]

Define \(H\subseteq G_1\cup G_2\) by:

- making each \(Q_i\) a clique;
- for each \(ij\in E(B)\), including all \(G_2\)-edges between \(Q_i\) and \(Q_j\);
- including no other edges.

#### Verification that \(H\) is induced-\(K_{s,t}\)-free

Suppose that \(H\) contained an induced \(K_{s,t}\) with independent sides \(A\) and \(T\). Since every \(Q_i\) is a clique, each \(Q_i\) contains at most one vertex of \(A\) and at most one vertex of \(T\). Thus coincidences between cluster indices of vertices in \(A\) and \(T\) form a matching.

If there are no coincidences, the cluster indices support an ordinary \(K_{s,t}\) in \(B\), contradicting the choice of \(B\).

Suppose there is a coincidence, say \(a_1\in A\) and \(b_1\in T\) lie in the same cluster \(Q_x\).

- If \(t>s\), choose another \(a_i\in A\) and choose a vertex \(b_j\in T\) whose cluster is not paired with any vertex of \(A\). The three relevant cluster indices form a triangle in \(B\): the required edges are supported by \(a_i b_1\), \(a_1b_j\), and \(a_ib_j\). This contradicts bipartiteness of \(B\).

- If \(t=s\) and not all vertices are paired, the same argument uses an unpaired vertex of \(T\).

- If \(t=s\ge3\) and all vertices are paired, the \(s\) occupied cluster indices support a \(K_s\) in \(B\), again impossible in a bipartite graph.

These cases cover every \(2\le s\le t\) except \(s=t=2\).

#### Edge count

Conditional on \(G_1\) and the selected cliques, the number \(Y\) of cross-edges is

\[
Y\sim\operatorname{Bin}\bigl(r^2e(B),p_*\bigr).
\]

By (5.2) and Chernoff's inequality,

\[
Y\ge c_pr^2z_{s,t}(M)
\]

with probability tending to one. Adding the \(M\binom r2\) internal clique edges proves (5.1). ∎

---

## 6. Sharpness for induced stars

Let \(t\ge2\). The upper bound in Theorem 1(1), with \(s=1\), gives

\[
\operatorname{ex}\bigl(G(n,p),\mathcal Q_{1,t}\bigr)
=O(n\log n).
\]

For the lower bound, use Lemma 4.1 to find \(M=\Theta(n/\log n)\) disjoint cliques of order \(r=\Theta(\log n)\), and take their disjoint union. This graph has

\[
M\binom r2=\Theta(n\log n)
\]

edges. A disjoint union of cliques has no induced \(K_{1,2}\), and hence no induced \(K_{1,t}\) for any \(t\ge2\). Therefore

\[
\operatorname{ex}\bigl(G(n,p),\mathcal Q_{1,t}\bigr)
=\Theta(n\log n)
\]

with high probability.

---

## 7. Sharpness for induced \(K_{2,t}\), \(t\ge3\)

We need a standard deterministic construction.

### Lemma 7.1

For every sufficiently large \(m\), there is a bipartite \(C_4\)-free graph \(B_m\) on \(m\) vertices with

\[
e(B_m)\ge c m^{3/2}.
\]

#### Proof

Choose a prime \(q=\Theta(\sqrt m)\) sufficiently small that

\[
2(q^2+q+1)\le m;
\]

such a prime exists by Bertrand's postulate. Take the incidence graph of the projective plane over \(\mathbb F_q\). It has

\[
2(q^2+q+1)
\]

vertices and

\[
(q+1)(q^2+q+1)=\Theta(q^3)=\Theta(m^{3/2})
\]

edges. It is \(C_4\)-free because two distinct points lie on a unique line. Add isolated vertices to reach order \(m\). ∎

In particular,

\[
z_{2,t}(m)\ge z_{2,2}(m)\ge c m^{3/2}
\qquad(t\ge2).
\]

For \(t\ge3\), Proposition 5.1 therefore gives

\[
\begin{aligned}
\operatorname{ex}\bigl(G(n,p),\mathcal Q_{2,t}\bigr)
&\ge
c r^2M^{3/2}\\
&=
\Omega\left(
(\log n)^2
\left(\frac{n}{\log n}\right)^{3/2}
\right)\\
&=
\Omega\left(n^{3/2}(\log n)^{1/2}\right).
\end{aligned}
\]

Together with the upper bound, this proves

\[
\boxed{
\operatorname{ex}\bigl(G(n,p),\operatorname{Forb}_{\mathrm{ind}}(K_{2,t})\bigr)
=
\Theta\left(n^{3/2}\sqrt{\log n}\right)
\quad\text{whp for every }t\ge3.
}
\]

For clarity, in this case the exclusion argument has a particularly simple form. If an induced \(K_{2,3}\) uses five distinct clusters, its cluster support contains a \(C_4\). If one opposite pair lies in the same cluster, the support contains a triangle. If two opposite pairs are identified, the remaining fifth vertex again creates a triangle. Thus a clique blow-up with arbitrary cross-edge subsets over a triangle- and \(C_4\)-free base remains induced-\(K_{2,3}\)-free.

---

## 8. The exceptional induced-\(C_4\) case

The upper bound gives

\[
\operatorname{ex}\bigl(G(n,p),\mathcal Q_{2,2}\bigr)
=
O\left(n^{3/2}\sqrt{\log n}\right).
\]

For the lower bound, fix the \(C_4\)-free graph \(B_n\) from Lemma 7.1 and retain its edges that occur in \(G(n,p)\). The resulting graph is still ordinary \(C_4\)-free and has, by Chernoff concentration,

\[
\Theta_p(n^{3/2})
\]

edges with high probability. Hence

\[
\operatorname{ex}\bigl(G(n,p),\mathcal Q_{2,2}\bigr)
=\Omega(n^{3/2}).
\]

The clique-blow-up transfer fails exactly here. An induced \(C_4\) can use one internal edge in each of two clique clusters and a two-edge matching between those clusters. After identifying the two opposite pairs, its cluster support is only a single base edge, so neither triangle-freeness nor \(C_4\)-freeness of the base prevents it. Thus the remaining factor \(\sqrt{\log n}\) is a genuine gap in this argument.

---

## 9. The monotone subcase

There is a simple general answer when \(\mathcal P\) is also closed under deleting edges. Put

\[
m_{\mathcal P}(n)=\max\{e(F): |V(F)|=n,\ F\in\mathcal P\}.
\]

If \(m_{\mathcal P}(n)\to\infty\), then

\[
(p-o(1))m_{\mathcal P}(n)
\le
\operatorname{ex}(G(n,p),\mathcal P)
\le
m_{\mathcal P}(n)
\qquad\text{whp}. \tag{9.1}
\]

Indeed, the upper bound is deterministic. For the lower bound, fix an extremal \(F_n\in\mathcal P\) and intersect its edge set with \(G(n,p)\). Edge-deletion closure keeps the resulting graph in \(\mathcal P\), and its number of edges is

\[
\operatorname{Bin}(m_{\mathcal P}(n),p)
=(p+o(1))m_{\mathcal P}(n)
\]

with high probability.

Thus every monotone bipartite-forbidden problem has the same order as its deterministic extremal number. The principal difficulty in the original question lies in genuinely induced-hereditary, non-monotone properties.

---

## 10. Why no property-independent order is possible

Even among hereditary properties missing a bipartite graph, the possible scales vary substantially:

- Edgeless graphs: \(\operatorname{ex}(G,\mathcal P)=0\).
- Graphs of maximum degree at most a fixed \(d\ge1\):
  \[
  \operatorname{ex}(G,\mathcal P)=\Theta(n).
  \]
  The upper bound is \(dn/2\); a fixed partition into pairs supplies \(\Theta(n)\) present matching edges whp.
- Induced-\(K_{1,2}\)-free graphs:
  \[
  \Theta(n\log n).
  \]
- Ordinary \(C_4\)-free graphs:
  \[
  \Theta(n^{3/2}).
  \]
  The deterministic upper bound follows from
  \[
  \sum_v\binom{d(v)}2\le\binom n2,
  \]
  and the lower bound follows from Lemma 7.1 and random intersection.
- Induced-\(K_{2,3}\)-free graphs:
  \[
  \Theta(n^{3/2}\sqrt{\log n}).
  \]

Therefore the hypothesis “\(\mathcal P\) misses a bipartite graph” alone cannot determine a universal order; finer structural information about \(\mathcal P\) is indispensable.

---

## 11. Remaining gaps

This does not settle the catalog problem in full.

1. For an arbitrary excluded bipartite graph \(F\) that is not complete bipartite, the independent-set double count above does not encode the missing cross-edges of \(F\).

2. Even when \(K_{s,t}\notin\mathcal P\), the sharp lower constructions apply to the maximal property \(\operatorname{Forb}_{\mathrm{ind}}(K_{s,t})\), not to an arbitrary strict hereditary subclass.

3. The maximal induced-\(C_4\)-free property still has the unresolved gap
   \[
   n^{3/2}
   \quad\text{versus}\quad
   n^{3/2}\sqrt{\log n}.
   \]

4. The supplied catalog reports that arXiv:2405.09486 proves a polynomial upper bound for every hereditary property missing a bipartite graph. I have not independently checked whether the sharp lower constructions above already appear there, so no novelty claim is made.