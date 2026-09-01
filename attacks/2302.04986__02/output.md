```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but one has the sharp bound η(G)≤ω(G)^{log_2 3} for (P5, complement-P5)-free graphs, hence η(G)≤3 for P5-free graphs of clique number two, and a square bound for a wider substitution class.",
  "would_publish": false,
  "caveats": "Prime imperfect P5-free quotient graphs with stability number at least three remain untreated, and the novelty of the special-case bounds has not been checked."
}
```

# 1. Statement of the partial results

All graphs below are finite and nonempty. Write \(\alpha(G)\) for the stability number and \(\eta(G)\) for the minimum size of a set meeting every maximum stable set.

Let
\[
p=\log_2 3.
\]

## Theorem A

If \(G\) is both \(P_5\)-free and \(\overline{P_5}\)-free, then
\[
\eta(G)\leq \omega(G)^p.
\]

The exponent \(p\) is best possible, even if a multiplicative constant is allowed.

Consequently, if \(G\) is \(P_5\)-free and \(\omega(G)\leq2\), then
\[
\eta(G)\leq3,
\]
and this is sharp for \(C_5\).

Since \(p<2\), Theorem A gives the conjectured polynomial bound, with \(d=2\), on the subclass of \((P_5,\overline{P_5})\)-free graphs.

## Theorem B

Let \(\mathcal D\) be the smallest class containing \(K_1\) and closed under the following operation: substitute graphs already in \(\mathcal D\) into the vertices of a graph \(H\), where either

1. \(H\) is perfect, or
2. \(\alpha(H)\leq2\).

Then every \(G\in\mathcal D\) satisfies
\[
\eta(G)\leq\omega(G)^2.
\]

Theorem B includes substitution constructions whose quotient graphs are arbitrary graphs of stability number at most two, not only \(C_5\).

# 2. Substitution and the exact formula for \(\eta\)

Let \(H\) have vertices \(1,\dots,m\), and let \(G_i\) be nonempty graphs. Denote by
\[
G=H(G_1,\dots,G_m)
\]
the graph obtained by substituting \(G_i\) for vertex \(i\): distinct bags \(G_i,G_j\) are complete or anticomplete according as \(ij\in E(H)\) or \(ij\notin E(H)\).

Set
\[
a_i=\alpha(G_i),\qquad k_i=\omega(G_i),\qquad e_i=\eta(G_i).
\]

A stable set of \(G\) chooses a stable set \(I\) of \(H\), and then a stable set inside each \(G_i\), \(i\in I\). Hence
\[
\alpha(G)=\max\left\{\sum_{i\in I}a_i:I\text{ stable in }H\right\},
\]
and
\[
\omega(G)=\max\left\{\sum_{i\in Q}k_i:Q\text{ a clique in }H\right\}.
\]

Let \(\mathcal I_a(H)\) be the family of maximum \(a\)-weight stable sets of \(H\).

### Substitution formula

\[
\boxed{
\eta(G)=
\min\left\{
\sum_{i\in X}e_i:
X\cap I\neq\varnothing\ \text{for every }I\in\mathcal I_a(H)
\right\}.}
\tag{1}
\]

Indeed, for a set \(S\subseteq V(G)\), let
\[
X(S)=\{i:S\cap V(G_i)\text{ meets every maximum stable set of }G_i\}.
\]
If \(X(S)\) misses some \(I\in\mathcal I_a(H)\), then in every bag \(G_i\), \(i\in I\), one can choose a maximum stable set avoiding \(S\). Their union is a maximum stable set of \(G\) avoiding \(S\).

Conversely, if \(X(S)\) meets every member of \(\mathcal I_a(H)\), then every maximum stable set of \(G\) uses some bag \(G_i\) in which \(S\) hits all maximum stable sets. This proves (1).

The weighted nature of (1) is important: even if the desired unweighted bound is known for the bags, maximum stable sets of the quotient are determined by the weights \(a_i=\alpha(G_i)\).

# 3. Perfect quotient graphs

We need the following weighted version of a simple fact about perfect graphs.

## Lemma 3.1

Let \(H\) be perfect and let \(a:V(H)\to\mathbb N_{>0}\). There is a clique \(Q\) of \(H\) meeting every maximum \(a\)-weight stable set of \(H\).

### Proof

Replace every vertex \(v\) of \(H\) by an independent set \(B_v\) of size \(a(v)\), with adjacencies between bags inherited from \(H\). The resulting graph \(H^a\) is perfect: this follows from closure of perfect graphs under substitution, or equivalently from the replication lemma applied in the complement.

A maximum stable set of \(H^a\) consists of all the vertices in the bags indexed by a maximum \(a\)-weight stable set of \(H\).

Since \(\overline{H^a}\) is perfect,
\[
\chi(\overline{H^a})=\omega(\overline{H^a})=\alpha(H^a).
\]
In an optimal coloring of \(\overline{H^a}\), every maximum clique uses every color. Thus each color class meets every maximum stable set of \(H^a\). A color class is a clique of \(H^a\), uses at most one vertex from each bag, and projects to a clique \(Q\) of \(H\) meeting every maximum \(a\)-weight stable set. \(\square\)

In particular, taking all \(a(v)=1\) shows that every perfect graph satisfies
\[
\eta(G)\leq\omega(G).
\tag{2}
\]

More generally, if \(G=H(G_1,\dots,G_m)\), \(H\) is perfect, and \(e_i\leq k_i^q\) for some \(q\geq1\), then Lemma 3.1 and (1) give
\[
\eta(G)
 \leq \sum_{i\in Q}e_i
 \leq \sum_{i\in Q}k_i^q
 \leq \left(\sum_{i\in Q}k_i\right)^q
 \leq\omega(G)^q.
\tag{3}
\]

Thus perfect quotient nodes preserve any exponent \(q\geq1\).

# 4. The \(C_5\) inequality

The following numerical inequality is the source of the exponent \(\log_2 3\).

## Lemma 4.1

Let \(p=\log_2 3\), and let \(x_0,\dots,x_4\geq0\), with indices modulo five. Put
\[
K=\max_i(x_i+x_{i+1}).
\]
There is an edge \(i(i+1)\) of \(C_5\) such that
\[
\sum_{j\notin\{i,i+1\}}x_j^p\leq K^p.
\tag{4}
\]

### Proof

By scaling, assume \(K=1\). Choose \(x_0=a=\max_i x_i\). Let the two neighbors of \(x_0\) have values \(b,e\), and let the other two values be \(c,d\), in cyclic order. Remove \(x_0\) together with its larger-valued neighbor. The remaining three values are
\[
m=\min\{b,e\},\quad c,\quad d.
\]
They satisfy
\[
m\leq1-a,\qquad c,d\leq a,\qquad c+d\leq1.
\]

If \(a\geq\frac12\), convexity gives
\[
c^p+d^p\leq a^p+(1-a)^p.
\]
Therefore
\[
m^p+c^p+d^p
 \leq a^p+2(1-a)^p.
\]
The function \(a^p+2(1-a)^p\) is convex on \([1/2,1]\), and its values at both endpoints are
\[
3\cdot2^{-p}=1,\qquad 1.
\]
Hence it is at most \(1\).

If \(a\leq\frac12\), then
\[
m^p+c^p+d^p\leq (1-a)^p+2a^p.
\]
This is again a convex function of \(a\) on \([0,1/2]\), with value \(1\) at both endpoints. Thus it is at most \(1\). This proves (4). \(\square\)

Now suppose the quotient \(H\) in a substitution is \(C_5\). Every maximum \(a\)-weight stable set of \(H\) has two vertices, because all \(a_i>0\). If \(M\) is the complement of an edge of \(C_5\), then \(M\) meets every stable pair. Taking \(x_i=k_i\) in Lemma 4.1 yields
\[
\sum_{i\in M}k_i^p\leq
\left(\max_i(k_i+k_{i+1})\right)^p
=\omega(G)^p.
\tag{5}
\]
Therefore \(C_5\) quotient nodes also preserve the exponent \(p\).

# 5. Prime \((P_5,\overline{P_5})\)-free graphs

A module of a graph is a set \(M\) such that every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is prime if it has no nontrivial proper module.

## Lemma 5.1

If a prime \((P_5,\overline{P_5})\)-free graph is not perfect, then it is \(C_5\).

### Proof

We first prove that if a \((P_5,\overline{P_5})\)-free graph \(R\) contains an induced cycle
\[
C=c_0c_1c_2c_3c_4c_0,
\]
then either \(R=C\) or \(R\) has a nontrivial module.

For \(x\notin C\), the possible neighborhoods \(N_C(x)\) are precisely among
\[
\varnothing,\quad C,\quad
\{c_{i-1},c_{i+1}\},\quad
\{c_{i-1},c_i,c_{i+1}\}.
\tag{6}
\]
Indeed:

- If \(|N_C(x)|=1\), say \(N_C(x)=\{c_0\}\), then
  \[
  x,c_0,c_1,c_2,c_3
  \]
  induce a \(P_5\).
- The case \(|N_C(x)|=4\) follows by complementation.
- If \(|N_C(x)|=2\) and the two neighbors are consecutive, say \(c_0,c_1\), then
  \[
  x,c_0,c_4,c_3,c_2
  \]
  induce a \(P_5\).
- Thus a two-vertex neighborhood must consist of two nonconsecutive vertices.
- By complementation, a three-vertex neighborhood must consist of three consecutive vertices.

For each \(i\), let \(X_i\) consist of \(c_i\) and all outside vertices which agree with \(c_i\) on \(C\setminus\{c_i\}\). Thus the last two types in (6) belong to some \(X_i\). Let \(A\) and \(B\) be the vertices anticomplete and complete to \(C\), respectively.

We claim that each \(X_i\) is a module. Let \(x\in X_i\).

- If \(y\in A\) and \(xy\in E(R)\), then
  \[
  y,x,c_{i+1},c_{i+2},c_{i+3}
  \]
  induce a \(P_5\). Hence \(A\) is anticomplete to \(X_i\).
- By applying this argument in the complement, \(B\) is complete to \(X_i\).
- Suppose \(y\in X_{i+1}\). If \(xy\notin E(R)\), then
  \[
  x,c_{i-1},c_{i-2},c_{i-3},y
  \]
  induce a \(P_5\). Thus \(X_i\) is complete to \(X_{i+1}\), and similarly to \(X_{i-1}\).
- If \(c_i,c_j\) are nonadjacent and \(x\in X_i,y\in X_j\), an edge \(xy\) would, in the complement, reduce to the preceding adjacent case and induce a \(\overline{P_5}\). Thus \(X_i\) and \(X_j\) are anticomplete.

Therefore every outside vertex treats \(X_i\) uniformly, proving that \(X_i\) is a module.

If some \(X_i\) contains a vertex other than \(c_i\), then \(X_i\) is a nontrivial proper module. Otherwise every vertex outside \(C\) lies in \(A\cup B\), and then \(C\) itself is a module. This proves the claim.

Now let \(R\) be prime, \((P_5,\overline{P_5})\)-free and imperfect. By the Strong Perfect Graph Theorem, \(R\) contains an odd hole or odd antihole. An odd hole of length at least seven contains a \(P_5\), and an odd antihole of length at least seven contains a \(\overline{P_5}\). Thus \(R\) contains an induced \(C_5\). The preceding paragraph and primeness imply \(R=C_5\). \(\square\)

# 6. Proof of Theorem A

Use the standard modular decomposition theorem: every graph with at least two vertices has a partition into proper nonempty modules whose quotient is complete, edgeless, or prime.

A quotient of a \((P_5,\overline{P_5})\)-free graph is again \((P_5,\overline{P_5})\)-free, since choosing one representative from each module realizes the quotient as an induced subgraph.

We induct on \(|V(G)|\). Let
\[
G=H(G_1,\dots,G_m)
\]
be a modular decomposition step. By Lemma 5.1, the quotient \(H\) is either perfect or \(C_5\); complete and edgeless quotients are perfect.

By induction,
\[
e_i=\eta(G_i)\leq k_i^p.
\]

- If \(H\) is perfect, inequality (3) gives
  \[
  \eta(G)\leq\omega(G)^p.
  \]
- If \(H=C_5\), inequality (5), together with the substitution formula (1), gives the same conclusion.

This proves Theorem A.

# 7. Sharpness of the exponent

Let \(G_0=K_1\), and recursively define
\[
G_{r+1}=C_5(G_r,G_r,G_r,G_r,G_r).
\]

Both \(P_5\) and \(\overline{P_5}\) are prime graphs. Consequently, the class of \((P_5,\overline{P_5})\)-free graphs is closed under substitution: an induced \(P_5\) or \(\overline{P_5}\) spanning more than one bag would use at most one vertex per bag and project to the same forbidden graph in the quotient.

For the above sequence,
\[
\omega(G_{r+1})=2\omega(G_r).
\]
All five bags have the same stability number, so the maximum stable sets of the quotient are all five stable pairs of \(C_5\). A transversal of these pairs has minimum size three. Formula (1) therefore gives
\[
\eta(G_{r+1})=3\eta(G_r).
\]
Hence
\[
\omega(G_r)=2^r,\qquad \eta(G_r)=3^r
  =\omega(G_r)^{\log_2 3}.
\]

Thus no exponent smaller than \(\log_2 3\) works on this subclass, even with a fixed multiplicative constant.

# 8. The exact clique-number-two case

If \(G\) is \(P_5\)-free and \(\omega(G)\leq2\), then \(G\) is triangle-free. Since \(\overline{P_5}\) contains a triangle—the vertices \(1,3,5\) of the underlying path form one in the complement—\(G\) is also \(\overline{P_5}\)-free. Theorem A gives
\[
\eta(G)\leq 2^{\log_2 3}=3.
\]

For \(C_5\), the maximum stable sets are its five nonadjacent pairs. Two vertices cannot meet all of them, while three vertices whose complement is an edge do. Thus
\[
\eta(C_5)=3,
\]
so the bound is sharp.

# 9. A wider square-bound substitution class

We now prove Theorem B.

## Lemma 9.1: weighted triangle-free vertex cover

Let \(F\) be triangle-free, with positive vertex weights \(b_v\), and let
\[
A=\max\left\{\sum_{v\in I}b_v:I\text{ stable in }F\right\}.
\]
Then \(F\) has a vertex cover \(C\) satisfying
\[
\sum_{v\in C}b_v^2\leq A^2.
\tag{7}
\]

### Proof

Let \(I\) be a maximum \(b\)-weight stable set and put \(C=V(F)\setminus I\). For every \(v\in C\),
\[
(I\setminus N(v))\cup\{v\}
\]
is stable, so maximality in weight gives
\[
b_v\leq\sum_{u\in I\cap N(v)}b_u.
\]
Therefore
\[
\begin{aligned}
\sum_{v\in C}b_v^2
&\leq
\sum_{v\in C}b_v
 \sum_{u\in I\cap N(v)}b_u\\
&=
\sum_{u\in I}b_u
 \sum_{v\in C\cap N(u)}b_v.
\end{aligned}
\]
Because \(F\) is triangle-free, \(N(u)\) is stable, and hence its total \(b\)-weight is at most \(A\). Thus the last expression is at most
\[
A\sum_{u\in I}b_u=A^2.
\]
\(\square\)

## Lemma 9.2: quotient graphs of stability number two

Let \(H\) satisfy \(\alpha(H)\leq2\). Give its vertices positive stable-set weights \(a_v\) and positive auxiliary weights \(b_v\). Put
\[
K=\max\left\{\sum_{v\in Q}b_v:Q\text{ a clique in }H\right\}.
\]
Then there is a set \(M\) meeting every maximum \(a\)-weight stable set of \(H\) such that
\[
\sum_{v\in M}b_v^2\leq K^2.
\tag{8}
\]

### Proof

Let \(F=\overline H\), which is triangle-free. Stable sets of \(H\) are vertices and edges of \(F\).

Let \(Z\) be the isolated vertices of \(F\), and let \(U\subseteq Z\) consist of those vertices whose singleton is a maximum \(a\)-weight stable set of \(H\). A non-isolated singleton cannot be maximum because it can be extended along an edge of \(F\), all \(a\)-weights being positive.

Apply Lemma 9.1 to \(F-Z\). If \(A\) is the maximum \(b\)-weight of a stable set in \(F-Z\), we obtain a vertex cover \(C\) of \(F-Z\) with
\[
\sum_{v\in C}b_v^2\leq A^2.
\]
Then \(M=U\cup C\) hits all maximum singletons and all maximum edges.

Moreover,
\[
K=\sum_{z\in Z}b_z+A,
\]
because cliques of \(H\) are stable sets of \(F\), and every maximum-weight stable set of \(F\) contains all its isolated vertices. Consequently,
\[
\sum_{v\in M}b_v^2
 \leq \left(\sum_{u\in U}b_u\right)^2+A^2
 \leq \left(\sum_{z\in Z}b_z+A\right)^2
 =K^2.
\]
\(\square\)

Theorem B now follows by induction over the substitution construction. At a perfect quotient node, use Lemma 3.1 with exponent \(2\). At a quotient node \(H\) with \(\alpha(H)\leq2\), apply Lemma 9.2 with
\[
a_i=\alpha(G_i),\qquad b_i=\omega(G_i).
\]
Together with (1) and the induction hypothesis \(e_i\leq k_i^2\), this yields
\[
\eta(G)\leq\omega(G)^2.
\]

# 10. The remaining gap

The structural lemma for \((P_5,\overline{P_5})\)-free graphs does not extend to all \(P_5\)-free graphs. There are prime, imperfect, \(P_5\)-free graphs with stability number at least three.

For example, take a cycle \(c_0c_1c_2c_3c_4c_0\) and add a vertex \(x\) adjacent precisely to \(c_0,c_1,c_3\). This graph is \(P_5\)-free:

- the five cycle vertices induce \(C_5\);
- after omitting \(c_0\) or \(c_1\), the remaining five-vertex graph has a vertex of degree three;
- after omitting \(c_2,c_3\), or \(c_4\), it contains the triangle \(xc_0c_1\).

It is imperfect because it contains the induced \(C_5\), and
\[
\{x,c_2,c_4\}
\]
is stable. It is also prime. Indeed, if \(M\) is a module and \(S=M\cap V(C_5)\), then \(S\) is a module of \(C_5\), so \(S\) is empty, a singleton, or all of \(C_5\). The only remaining possible proper nontrivial modules are pairs \(\{x,c_i\}\), and each such pair is distinguished by another cycle vertex.

Thus Theorem B does not cover all prime \(P_5\)-free quotient graphs.

More generally, formula (1) shows what this modular approach would require. It would suffice to find a fixed \(d\) such that for every prime \(P_5\)-free graph \(H\), every pair of positive weight systems \(a,b\), there is a set \(X\) meeting all maximum \(a\)-weight stable sets and satisfying
\[
\sum_{v\in X}b_v^d
\leq
\left(
\max_{Q\text{ clique in }H}\sum_{v\in Q}b_v
\right)^d.
\tag{9}
\]
The arguments above establish (9) for perfect \(H\), for \(C_5\), and with \(d=2\) for all \(H\) with \(\alpha(H)\leq2\). No argument is supplied for general prime imperfect \(P_5\)-free \(H\) with \(\alpha(H)\geq3\). This is the substantive unresolved case, so the original conjecture is not proved.