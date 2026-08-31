```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but for red two-graphs the restricted Ramsey number is exactly 2n+1 when 3 divides n and 2n otherwise.",
  "would_publish": false,
  "caveats": "Only the even-on-every-four-set subclass is settled; the random-greedy estimate needed for the full lower bound remains unproved."
}
```

# 1. Reformulation of the problem

Let \(H\) be the red 3-uniform hypergraph and let, for \(v\in V(H)\),
\[
L_H(v)=\bigl\{xy:\;vxy\in E(H)\bigr\}
\]
be its link graph.

Two elementary equivalences are fundamental.

1. \(H\) is \(K_{4-e}^{(3)}\)-free if and only if every \(L_H(v)\) is triangle-free.

   Indeed, three triples on a fixed four-set have a common vertex, namely the vertex opposite the missing triple.

2. The blue complement of \(H\) contains a copy of \(S_n^{(3)}\) centered at \(v\) if and only if
   \[
   \alpha(L_H(v))\ge n.
   \]

Thus the conjectured lower bound asks for a \(K_{4-e}^{(3)}\)-free 3-graph on
\[
N=\Omega\!\left(\frac{n^2}{\log n}\right)
\]
vertices such that
\[
\alpha(L_H(v))<n\qquad\text{for every }v.
\]

There is also a useful codegree constraint. For every pair \(x,y\), its common red neighborhood
\[
N_H(xy)=\{z:xyz\in E(H)\}
\]
is independent in both \(L_H(x)\) and \(L_H(y)\). Indeed, if \(z,w\in N_H(xy)\), then \(xyz\) and \(xyw\) are red, so \(xzw\) and \(yzw\) must both be absent. Consequently, any putative extremal construction satisfies
\[
d_H(xy)\le n-1
\]
for every pair \(x,y\).

The known upper bound follows immediately from the triangle-free Ramsey bound applied to any link. The missing issue is the simultaneous construction of Ramsey-optimal triangle-free links subject to triple-consistency.

# 2. An exact special case: red two-graphs

Call a 3-graph \(H\) **even** if every four vertices span an even number of red triples:
\[
|E(H[Q])|\equiv 0\pmod 2
\qquad\text{for every }Q\in\binom{V(H)}4.
\]
Such triple systems are usually called two-graphs.

Let \(r_{\mathrm{even}}(K_{4-e}^{(3)},S_n^{(3)})\) denote the corresponding Ramsey number when the red hypergraph is additionally required to be even.

## Theorem

For every \(n\ge2\),
\[
r_{\mathrm{even}}(K_{4-e}^{(3)},S_n^{(3)})
=
\begin{cases}
2n+1,&3\mid n,\\[2mm]
2n,&3\nmid n.
\end{cases}
\]

In particular, every construction based on a two-graph has only linear order and cannot approach the conjectured \(n^2/\log n\) scale.

## 2.1. Graph representation

Fix a vertex \(v_0\), put \(W=V(H)\setminus\{v_0\}\), and let
\[
G=L_H(v_0).
\]
Evenness gives, for distinct \(x,y,z\in W\),
\[
1_H(xyz)
\equiv
1_G(xy)+1_G(xz)+1_G(yz)
\pmod 2. \tag{1}
\]

Thus \(H\) is determined by the graph \(G\).

### Lemma 1

If \(H\) is even and \(K_{4-e}^{(3)}\)-free, then \(G\) is both triangle-free and induced-\(2K_2\)-free.

### Proof

Triangle-freeness follows from the link characterization.

Suppose \(G[x,y,z,w]\) is an induced matching with edges \(xy\) and \(zw\). By (1), each of
\[
xyz,\quad xyw,\quad xzw,\quad yzw
\]
is red, since each corresponding triple spans exactly one edge of \(G\). Hence \(H[x,y,z,w]\) has all four triples red and therefore contains \(K_{4-e}^{(3)}\), a contradiction. ∎

Conversely, every triangle-free, induced-\(2K_2\)-free graph \(G\), together with (1), produces an even \(K_{4-e}^{(3)}\)-free 3-graph. For four vertices not containing \(v_0\), evenness implies that a violation would consist of all four triples. Since \(G\) is triangle-free, this would force every three-vertex subset to span exactly one edge, hence \(G\) would induce a \(2K_2\).

## 2.2. Structure of \((K_3,2K_2)\)-free graphs

### Lemma 2

Let \(G\) be triangle-free and induced-\(2K_2\)-free.

- At most one component of \(G\) contains an edge.
- If that component is nonbipartite, then it is a complete blow-up of \(C_5\).

### Proof

Two edge-containing components would provide an induced \(2K_2\).

Suppose the unique nontrivial component is connected and nonbipartite. A shortest odd cycle is induced. It cannot have length at least seven, since an induced cycle of length at least six contains an induced \(2K_2\). It is therefore an induced cycle
\[
C=v_0v_1v_2v_3v_4v_0.
\]

The cycle dominates \(G\). Otherwise, along a shortest path from \(C\) to a vertex at distance two, let \(xy\) be the last edge, where \(x\) has no neighbor on \(C\). The neighbors of \(y\) on \(C\) form an independent set and hence have size at most two. Some edge \(ab\) of \(C\) avoids all these neighbors, and then \(xy,ab\) induce a \(2K_2\).

Every vertex \(x\notin C\) has exactly two neighbors on \(C\). Its neighborhood on \(C\) is independent. It cannot have only one neighbor \(v_i\), since then \(xv_i\) together with the edge \(v_{i+2}v_{i-2}\) induces a \(2K_2\). Hence there is a unique \(i\) such that
\[
N_C(x)=\{v_{i-1},v_{i+1}\}.
\]

Let \(P_i\) consist of \(v_i\) and all such vertices \(x\).

- Each \(P_i\) is independent.
- There are no edges between nonconsecutive \(P_i,P_j\), since such vertices have a common neighbor on \(C\).
- Every possible edge between \(P_i\) and \(P_{i+1}\) is present. If \(x\in P_i\), \(y\in P_{i+1}\) were nonadjacent, then
  \[
  xv_{i-1},\qquad yv_{i+2}
  \]
  would induce a \(2K_2\).

Thus \(G\) is a complete blow-up of \(C_5\), apart from possible isolated vertices. ∎

# 3. The six-vertex template

Let \(F\) be the graph consisting of a \(C_5\) on vertices \(\mathbb Z_5\) and an isolated vertex \(\infty\). Define a 3-graph \(\mathcal T\) on these six vertices by
\[
ijk\in E(\mathcal T)
\quad\Longleftrightarrow\quad
F[\{i,j,k\}]\text{ has an odd number of edges}.
\]

Every link of \(\mathcal T\) is a \(C_5\):

- \(L_{\mathcal T}(\infty)=C_5\);
- a direct calculation gives, for \(i\in\mathbb Z_5\), the cycle
  \[
  \infty,\ i+1,\ i-2,\ i+2,\ i-1,\ \infty
  \]
  in \(L_{\mathcal T}(i)\).

If the representing graph \(G\) from the preceding section is nonbipartite, Lemma 2 shows that \(H\) is a blow-up of \(\mathcal T\). More precisely, there are six vertex classes
\[
A_\infty,A_0,\dots,A_4
\]
such that triples using two vertices from one class are absent, while triples from three distinct classes follow the edge relation of \(\mathcal T\).

Write
\[
a_i=|A_i|,\qquad N=\sum_i a_i.
\]

For \(v\in A_i\), the vertices of \(A_i\setminus\{v\}\) are isolated in \(L_H(v)\), and the remaining five classes form a complete blow-up of a \(C_5\). Hence
\[
\alpha(L_H(v))
=
a_i-1+
\max_{\substack{j,k\ne i\\ ijk\notin E(\mathcal T)}}(a_j+a_k). \tag{2}
\]

It follows that \(H\) has no blue \(S_n^{(3)}\) precisely when
\[
a_i+a_j+a_k\le n
\qquad
\text{for every }ijk\notin E(\mathcal T). \tag{3}
\]

There are ten nonedges of \(\mathcal T\), and each base vertex belongs to exactly five of them. Summing (3) over all ten gives
\[
5\sum_i a_i\le10n,
\]
and therefore
\[
N\le2n. \tag{4}
\]

If equality holds in (4), all ten inequalities in (3) must be equalities. The nonedges of \(\mathcal T\) are
\[
\{\infty,i,i+2\}
\quad\text{and}\quad
\{i-1,i,i+1\},
\qquad i\in\mathbb Z_5.
\]
Writing the five cycle weights as \(x_i\) and \(a_\infty=z\), equality gives
\[
x_{i-1}+x_i+x_{i+1}=n.
\]
Subtracting consecutive equations yields
\[
x_{i-1}=x_{i+2}.
\]
Since addition by \(3\) generates \(\mathbb Z_5\), all \(x_i\) are equal, say \(x_i=x\). Thus
\[
3x=n,\qquad z+2x=n,
\]
so \(3\mid n\) and all six weights equal \(n/3\).

If the representing link \(G\) is bipartite instead, then
\[
\alpha(G)\ge \left\lceil\frac{N-1}{2}\right\rceil.
\]
The absence of a blue \(S_n^{(3)}\) consequently forces \(N\le2n-1\).

We have proved:

- if \(3\mid n\), every admissible even construction has \(N\le2n\);
- if \(3\nmid n\), it has \(N\le2n-1\).

## Sharp constructions

Let \(n=3a+r\).

- If \(r=0\), take all six class sizes equal to \(a\). Then every link has independence number
  \[
  (a-1)+2a=n-1,
  \]
  giving an example on \(2n\) vertices.

- If \(r=1\), take one class of size \(a+1\) and the other five of size \(a\). Every nonedge triple has total weight at most \(3a+1=n\). This gives \(2n-1\) vertices.

- If \(r=2\), choose a red triple of \(\mathcal T\), give its three classes size \(a+1\), and give the remaining classes size \(a\). A nonedge triple cannot contain all three enlarged classes, so its weight is at most
  \[
  3a+2=n.
  \]
  Again the order is \(2n-1\).

This proves the stated exact formula for \(r_{\mathrm{even}}\).

# 4. Other natural constructions that necessarily remain linear

Two further common ansätze also fail for exact structural reasons.

### Cyclic triples of a tournament

If the red triples are the cyclic triangles of a tournament, then for a fixed center \(v\), the link \(L_H(v)\) is bipartite between the in-neighbors and out-neighbors of \(v\). Thus
\[
\alpha(L_H(v))\ge\frac{N-1}{2},
\]
so this construction already produces a blue \(S_n^{(3)}\) once \(N\ge2n\).

### Translation invariance on \(\mathbb F_2^d\)

A nonempty translation-invariant 3-graph on \(\mathbb F_2^d\) cannot be \(K_{4-e}^{(3)}\)-free. If \(abc\) is an edge and
\[
d=a+b+c,
\]
then translating \(abc\) by \(a+b\), \(a+c\), and \(b+c\) shows that all four triples on \(\{a,b,c,d\}\) are edges.

Thus neither tournament constructions, two-graphs, nor elementary \(2\)-group Cayley constructions can reach the conjectured scale.

# 5. Exact random-greedy formulation of the unresolved part

There is a convenient auxiliary hypergraph formulation.

Let \(\mathcal A_N\) be the 3-uniform hypergraph whose vertices are the triples of \([N]\). Three such vertices form an edge of \(\mathcal A_N\) when they are three of the four triples on a common four-set. Then:

- independent sets in \(\mathcal A_N\) are exactly the \(K_{4-e}^{(3)}\)-free 3-graphs on \([N]\);
- \(\mathcal A_N\) has
  \[
  M=\binom N3
  \]
  vertices;
- it is \(D\)-regular with
  \[
  D=3(N-3);
  \]
- its maximum pair-codegree is \(2\).

For \(v\in[N]\) and \(U\subseteq[N]\setminus\{v\}\), \(|U|=n\), define
\[
B(v,U)=\{\{v,x,y\}:x,y\in U\}.
\]
Then
\[
|B(v,U)|=\binom n2,
\]
and the desired red hypergraph is precisely an independent set in \(\mathcal A_N\) intersecting every \(B(v,U)\).

Consider the random greedy independent-set process in \(\mathcal A_N\). If the selected density is \(s\), a naive independence calculation predicts that a potential triple remains open with probability
\[
q(s)\approx
(1-3s^2+2s^3)^{N-3}
=
\exp\bigl(-(3+o(1))Ns^2\bigr).
\]
The natural stopping density is therefore
\[
p=a\sqrt{\frac{\log N}{N}}
\]
for a sufficiently small constant \(a>0\).

At
\[
N=c\frac{n^2}{\log n},
\]
one has
\[
p\binom n2
=
\left(\frac{a}{\sqrt{2c}}+o(1)\right)n\log n,
\]
while
\[
\log\!\left(N\binom{N-1}{n}\right)
=
(1+o(1))n\log n.
\]
Thus the constants permit a union bound if one can prove a uniform local trajectory estimate of the following form:

> There exist constants \(a,\gamma>0\) such that, with probability \(1-o(1)\), for every \(B(v,U)\) not yet hit and every step up to density \(p\),
> \[
> \frac{|O_i\cap B(v,U)|}{|O_i|}
> \ge
> \gamma\frac{|B(v,U)|}{M},
> \]
> where \(O_i\) is the current set of open triples.

Indeed, under this estimate the probability that a fixed \(B(v,U)\) remains unhit is at most
\[
\exp\!\left(-\gamma p\binom n2\right),
\]
and choosing \(c>0\) sufficiently small would make the union bound succeed.

There is some additional favorable structure: conditional on \(B(v,U)\) being unhit, a triple \(vxy\in B(v,U)\) cannot be closed using a fourth vertex \(z\in U\), because two of the three possible supporting triples, \(vxz\) and \(vyz\), also belong to \(B(v,U)\). Nevertheless, obtaining the required trajectory estimate simultaneously for
\[
N\binom{N-1}{n}
=
\exp((1+o(1))n\log n)
\]
sets is precisely the unproved step. A fixed-set heuristic or polynomial-tail concentration is not enough.

# 6. Conclusion and gap

The full conjecture is not proved here. The substantive rigorous result is the exact resolution of the even/two-graph subclass:
\[
r_{\mathrm{even}}(K_{4-e}^{(3)},S_n^{(3)})
=
\begin{cases}
2n+1,&3\mid n,\\
2n,&3\nmid n.
\end{cases}
\]
This rules out a broad algebraic parity-based family of constructions and identifies a unique six-vertex \(C_5\)-link template governing the nonbipartite case.

For the unrestricted problem, the auxiliary random-greedy process has exactly the correct density and entropy balance. What remains missing is a journal-level proof of uniform local openness, with failure probability strong enough to handle exponentially many prospective blue stars.