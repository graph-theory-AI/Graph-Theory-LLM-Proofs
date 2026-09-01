```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A power bound follows under a polynomial cross-defect hypothesis, and for edge maximization in the complete host one unconditionally obtains an explicit O_H(n^2/(log^* n)^{c_H}) bound.",
  "would_publish": false,
  "caveats": "The original dense-host problem remains open because no polynomial bound is obtained for vertices incident with linearly many omitted cross-edges."
}
```

## 1. Formulation

Write \(k=\chi(H)\), \(r=k-1\), and let \(K_m(t)\) denote the balanced \(t\)-blow-up of \(K_m\). The conjecture asks for a constant \(\delta(H)>0\) such that an \(H\)-free, \(K_m(t)\)-maximizing subgraph \(F\) of a sufficiently dense \(n\)-vertex host can be made \(r\)-partite by deleting \(O(n^{2-\delta(H)})\) edges.

I do not prove this. I give:

1. a power-saving theorem reducing the problem to polynomial control of omitted cross-edges; and  
2. an unconditional explicit quantitative improvement in the special case \(G=K_n\) and \(K_m(t)=K_2\).

The first result applies to all objectives because it only uses \(H\)-freeness once the appropriate approximate partition is known.

---

## 2. A power bound under polynomial cross-defect

### Proposition 2.1

Let \(H\) be fixed with \(\chi(H)=k\), put \(r=k-1\), and let \(h=v(H)\). Fix \(c,\gamma>0\). There is an \(\varepsilon_0=\varepsilon_0(H,c)>0\) with the following property.

Let \(G\) be an \(n\)-vertex graph with
\[
\delta(G)\ge (1-\varepsilon_0)n,
\]
let \(F\subseteq G\) be \(H\)-free, and suppose
\[
V(F)=V_1\cup\cdots\cup V_r,\qquad |V_i|\ge cn
\]
is a partition. Let
\[
D=\{xy\in E(G)\setminus E(F):x\in V_i,\ y\in V_j,\ i\ne j\}
\]
be the set of available cross-edges omitted from \(F\). If
\[
|D|=O(n^{2-\gamma}),
\]
then \(F\) can be made \(r\)-partite by deleting
\[
O_H\!\left(n^{2-\gamma}+n^{2-1/a}\right)
\]
edges, where \(a\ge1\) depends only on a fixed proper \(k\)-coloring of \(H\). In particular,
\[
\operatorname{dist}(F,\text{\(r\)-partite})
   =O_H\!\left(n^{2-\min\{\gamma,1/h\}}\right).
\]

### Proof

Fix a proper \(k\)-coloring
\[
V(H)=C_1\cup\cdots\cup C_k.
\]
Choose two color classes, say \(C_1,C_2\), and let
\[
J=H[C_1\cup C_2].
\]
There must be at least one edge between \(C_1\) and \(C_2\); otherwise those two colors could be merged, contradicting \(\chi(H)=k\).

Put
\[
a=\min\{|C_1|,|C_2|\},\qquad b=\max\{|C_1|,|C_2|\}.
\]
Then \(J\subseteq K_{a,b}\).

Choose
\[
\varepsilon_0\le \frac{c}{8h},\qquad \theta=\frac{c}{8h}.
\]
Call a vertex \(x\in V_i\) bad if, for some \(j\ne i\),
\[
|\{y\in V_j:xy\in E(G)\setminus E(F)\}|>\theta n.
\]
Let \(X\) be the set of bad vertices. Since every edge of \(D\) is counted at most twice,
\[
|X|\theta n\le 2|D|,
\]
and hence
\[
|X|=O(n^{1-\gamma}).
\]

We claim that, for every \(i\), the graph \(F[V_i\setminus X]\) is \(J\)-free. Suppose otherwise and fix a copy of \(J\) in \(V_i\setminus X\). Map \(C_1\cup C_2\) to this copy. Assign the remaining \(k-2=r-1\) color classes bijectively to the other \(r-1\) parts.

We embed those remaining color classes one vertex at a time, always choosing vertices outside \(X\). If a previously embedded good vertex lies in a different part from the current target part, then it has at most
\[
(\varepsilon_0+\theta)n\le \frac{c}{4h}n
\]
nonneighbors in that target part in \(F\). At every step there are at most \(h\) previously embedded vertices imposing adjacency requirements. Consequently fewer than
\[
h(\varepsilon_0+\theta)n+|X|+h
   \le \frac{c}{4}n+o(n)
\]
vertices are unavailable. Since every target part has at least \(cn\) vertices, the greedy embedding succeeds for all sufficiently large \(n\). This produces a copy of \(H\), a contradiction.

Thus \(F[V_i\setminus X]\) is \(J\)-free and therefore \(K_{a,b}\)-free. By the Kővári–Sós–Turán bound,
\[
e(F[V_i\setminus X])=O_H(n^{2-1/a}).
\]
All internal edges having an endpoint in \(X\) number at most \(|X|n=O(n^{2-\gamma})\). Therefore
\[
\sum_{i=1}^r e(F[V_i])
 =O_H(n^{2-\gamma}+n^{2-1/a}).
\]
Deleting these internal edges makes \(F\) \(r\)-partite. Since \(a\le h\), the weaker exponent \(1/h\) is always available. ∎

### Consequence and remaining issue

This proves the conjectured power bound whenever the approximate stability partition additionally satisfies a polynomial estimate on the number of omitted available cross-edges. It also covers the special case where \(F\) contains every host edge between distinct parts.

The unresolved step is therefore quite concrete:

> Obtain, from \(K_m(t)\)-optimality, a partition for which the number of omitted available cross-edges, or equivalently the number of vertices omitting linearly many such edges, is \(O(n^{2-\gamma})\) or \(O(n^{1-\gamma})\).

The qualitative proof only forces an \(o(n)\)-sized exceptional set. Edges incident with this set may still number \(n^{2-o(1)}\).

---

## 3. An unconditional explicit rate for \(G=K_n\) and edge maximization

The next theorem gives an explicit improvement over \(o(n^2)\), though not a power saving.

### Theorem 3.1

For every fixed graph \(H\) with \(\chi(H)=k\ge3\), there exists \(c_H>0\) such that the following holds.

If \(F\) is an \(n\)-vertex \(H\)-free graph satisfying
\[
e(F)\ge t_{k-1}(n),
\]
where \(t_{k-1}(n)=e(T_{k-1}(n))\), then \(F\) can be made \((k-1)\)-partite by deleting
\[
O_H\!\left(\frac{n^2}{(\log^* n)^{c_H}}\right)
\]
edges.

Consequently, this applies to every edge-extremal \(H\)-free subgraph of \(K_n\), i.e. to the case \(K_m(t)=K_2(1)\).

### 3.1. Polynomially few \(K_k\)'s in an \(H\)-free graph

Let \(s=v(H)\). Since \(H\) has a proper \(k\)-coloring,
\[
H\subseteq K_k(s).
\]
Thus an \(H\)-free graph is \(K_k(s)\)-free.

Consider the \(k\)-uniform hypergraph whose hyperedges are the vertex sets of copies of \(K_k\) in \(F\). If this hypergraph contained a complete \(k\)-partite \(k\)-uniform hypergraph with \(s\) vertices in every class, then \(F\) would contain \(K_k(s)\). Hence the standard complete-partite hypergraph extremal bound gives
\[
N(K_k,F)=O_H(n^{k-\alpha_H})
\]
for some \(\alpha_H>0\); one may take
\[
\alpha_H=s^{-(k-1)}.
\]

For completeness, the exponent follows inductively. For \(k=2\) it is the Kővári–Sós–Turán theorem. For the induction step, if a \(p\)-uniform hypergraph has \(M\) edges, then convexity applied to the common links of \(s\)-sets gives an average common \((p-1)\)-link of order
\[
n^{p-1-s\alpha_p}.
\]
Taking \(\alpha_p=\alpha_{p-1}/s\), beginning with \(\alpha_2=1/s\), yields
\[
\alpha_p=s^{-(p-1)}.
\]

### 3.2. Quantitative removal

A standard regularity-lemma bound for \(K_k\)-removal states that there are constants \(A_k,B_k>0\) such that any graph which requires deletion of at least \(\eta n^2\) edges to become \(K_k\)-free contains at least
\[
\frac{n^k}{\operatorname{twr}(A_k\eta^{-B_k})}
\]
labelled copies of \(K_k\), where \(\operatorname{twr}(q)\) is a tower of twos of height \(\lceil q\rceil\).

Let \(L=\log_2^* n\) and choose
\[
\eta=\left(\frac{4A_k}{L}\right)^{1/B_k}.
\]
Then
\[
A_k\eta^{-B_k}=L/4.
\]
For every fixed \(\alpha_H>0\),
\[
\operatorname{twr}(L/4)=o(n^{\alpha_H}).
\]
Thus, for sufficiently large \(n\),
\[
O_H(n^{k-\alpha_H})
 <
\frac{n^k}{\operatorname{twr}(L/4)}.
\]
The removal lemma therefore gives a set of
\[
d=O_H\!\left(\frac{n^2}{(\log^*n)^{1/B_k}}\right)
\]
edges whose deletion leaves a \(K_k\)-free graph \(F_0\).

Since \(e(F)\ge t_{k-1}(n)\),
\[
e(F_0)\ge t_{k-1}(n)-d.
\]

### 3.3. Quantitative stability for \(K_k\)-free graphs

We use the following standard consequence of the Andrásfai–Erdős–Sós minimum-degree theorem.

#### Lemma 3.2

For each fixed \(r\ge2\), if \(Q\) is \(K_{r+1}\)-free and
\[
e(Q)\ge t_r(n)-D,
\]
then \(Q\) can be made \(r\)-partite by deleting \(O_r(D+1)\) edges.

#### Proof

Put
\[
a_r=\frac{r-1}{r},\qquad
c_r=1-\frac{3}{3r-1}=\frac{3r-4}{3r-1}.
\]
The Andrásfai–Erdős–Sós theorem says that a \(K_{r+1}\)-free graph of order \(N\) and minimum degree greater than \(c_rN\) is \(r\)-partite.

Repeatedly delete a vertex of degree at most \(c_rN\), where \(N\) is the current order, until the remaining graph is \(r\)-partite. Suppose \(s\) vertices are deleted. Counting edges at their deletion times gives
\[
e(Q)\le t_r(n-s)+
 c_r\left(sn-\frac{s(s-1)}2\right).
\]
Since
\[
t_r(x)=\frac{a_r x^2}{2}+O_r(1)
\]
and
\[
a_r-c_r=\frac1{r(3r-1)}>0,
\]
we obtain
\[
D\ge
(a_r-c_r)\left(ns-\frac{s^2}{2}\right)
-\frac{c_rs}{2}-O_r(1).
\]
For sufficiently large \(n\), this implies
\[
sn=O_r(D+1).
\]
Delete all edges incident with the \(s\) removed vertices and make those vertices isolated. The remaining graph is \(r\)-partite, and the number of deleted edges is at most \(sn=O_r(D+1)\). ∎

Apply the lemma with \(r=k-1\), \(Q=F_0\), and \(D=d\). Deleting a further \(O_k(d+1)\) edges makes \(F_0\), and hence \(F\), \((k-1)\)-partite. Altogether,
\[
\operatorname{dist}(F,\text{\((k-1)\)-partite})
 =
O_H\!\left(\frac{n^2}{(\log^*n)^{c_H}}\right)
\]
for \(c_H=1/B_k>0\). This proves Theorem 3.1. ∎

---

## 4. Why this does not prove the conjecture

There are two genuine gaps.

1. **The removal route is not polynomial.**  
   \(H\)-freeness gives a polynomial saving in the number of \(K_k\)'s, but ordinary graph removal only turns this into an inverse-iterated-logarithmic edit bound. General triangle-removal lower-bound constructions rule out a naive power-form removal lemma. Those constructions are not counterexamples here because they need not be optimal subgraphs of a dense host, but they show that extremality must be used essentially.

2. **Cross-edge concentration is uncontrolled.**  
   Once all vertices except \(O(n^{1-\gamma})\) have uniformly dense cross-neighborhoods, Proposition 2.1 gives the desired power saving by a direct embedding and Kővári–Sós–Turán argument. The qualitative stability theorem only supplies \(o(n)\) exceptional vertices. A set of \(n^{1-o(1)}\) exceptional vertices can support \(n^{2-o(1)}\) internal edges, and the present argument does not rule this out.

Thus no counterexample has been produced, but the full \(O(n^{2-\delta(H)})\) assertion remains unproved.