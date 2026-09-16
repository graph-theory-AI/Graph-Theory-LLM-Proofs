```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a bounded-odd-cycle-transversal case and give an explicit girth-seven obstruction, but do not establish a uniform girth threshold.",
  "would_publish": false,
  "caveats": "No claim of novelty or optimal constants; the unrestricted conjecture remains unresolved here."
}
```

# 1. Partial results

All graphs below are finite and simple. Write
\[
\tau_{\mathrm{odd}}(G)
=\min\{|T|:G-T\text{ is bipartite}\},
\]
and let \(h(G)\) denote the odd girth, with \(h(G)=\infty\) when \(G\) is bipartite.

The positive partial result is the following.

**Theorem 1.** If \(\Delta(G)\le 3\) and
\[
h(G)>4\tau_{\mathrm{odd}}(G)-1,
\]
then \(G\to C_5\).

Consequently, for every fixed \(k\ge1\), every cubic graph of girth at least \(4k\) that can be made bipartite by deleting at most \(k\) vertices maps to \(C_5\).

On the negative side, I give a self-contained construction and proof of the following familiar type of obstruction.

**Proposition 2.** There is a cubic graph on \(28\) vertices with girth \(7\) and no homomorphism to \(C_5\).

Thus any integer threshold in an affirmative answer to the Pentagon Problem must be at least \(8\). This is not an assertion that \(8\) is sufficient.

# 2. A useful exact characterization

Identify \(V(C_5)\) with \(\mathbb Z/5\mathbb Z\), with consecutive residues adjacent. For \(S\subseteq V(G)\), let \(N(S)\) be its open neighborhood.

**Lemma 3.** A graph \(G\) maps to \(C_5\) if and only if it has a set \(S\subseteq V(G)\) such that:

1. \(S\) is independent;
2. \(N(S)\) is independent;
3. \(G-S\) is bipartite.

**Proof.** Suppose \(\varphi:G\to C_5\). Take \(S=\varphi^{-1}(0)\). Then \(S\) is independent and
\[
N(S)\subseteq \varphi^{-1}(\{1,4\}).
\]
Since \(1\) and \(4\) are nonadjacent in \(C_5\), the latter set is independent. Also, \(G-S\) maps to the path \(C_5-0\), so it is bipartite.

Conversely, suppose \(S\) has the three stated properties. Choose a bipartition \((A,B)\) of \(G-S\), and define
\[
\varphi(v)=
\begin{cases}
0,&v\in S,\\
1,&v\in A\cap N(S),\\
3,&v\in A\setminus N(S),\\
4,&v\in B\cap N(S),\\
2,&v\in B\setminus N(S).
\end{cases}
\]
An edge incident with \(S\) maps to \(01\) or \(04\). Every other edge joins \(A\) to \(B\). Its possible color pairs are \(12,34,32\), except that the forbidden pair \(14\) would require an edge inside \(N(S)\). Hence every edge maps to an edge of \(C_5\). ∎

The importance of using length-three **walks**, rather than just distance three, will appear below.

# 3. Proof of the bounded-transversal theorem

## 3.1. Bipartization in subcubic graphs

Let \(b(G)\) be the minimum number of monochromatic edges in a two-coloring of \(V(G)\). Equivalently, it is the minimum number of edges whose deletion makes \(G\) bipartite.

**Lemma 4.** If \(\Delta(G)\le3\), then
\[
b(G)=\tau_{\mathrm{odd}}(G).
\]
Moreover, the monochromatic edges in any two-coloring attaining \(b(G)\) form a matching.

**Proof.** From any edge bipartization, choose one endpoint of each deleted edge. Deleting the chosen vertices leaves a bipartite graph. Thus
\[
\tau_{\mathrm{odd}}(G)\le b(G).
\]

For the reverse inequality, take an odd-cycle transversal \(T\), properly two-color \(G-T\), and extend the coloring to \(T\) so as to minimize the number of monochromatic edges while keeping the colors outside \(T\) fixed.

Each vertex of \(T\) is incident with at most one monochromatic edge. Otherwise, since its degree is at most three, flipping its color would strictly decrease their number. Every monochromatic edge has an endpoint in \(T\), so there are at most \(|T|\) such edges. Taking \(T\) minimum proves \(b(G)\le\tau_{\mathrm{odd}}(G)\).

Finally, in a globally optimal two-coloring, the same single-vertex flip argument applies at every vertex. Thus no vertex is incident with two monochromatic edges, proving the matching assertion. ∎

## 3.2. An auxiliary graph on the defects

**Proof of Theorem 1.** If \(G\) is bipartite, the conclusion is immediate. Otherwise put
\[
k=\tau_{\mathrm{odd}}(G)\ge1.
\]
By Lemma 4, choose a two-coloring whose monochromatic edges form a matching \(M\) of size \(k\). In particular, \(G-M\) is bipartite.

Let \(D=V(M)\), so \(|D|=2k\). Define a simple auxiliary graph \(H\) on \(D\): distinct \(u,v\in D\) are adjacent in \(H\) if \(G\) has a walk of length one or three from \(u\) to \(v\). Notice that \(M\) is a perfect matching of \(H\).

We first show that if \(H\) is bipartite, then \(G\to C_5\).

Choose one side \(S\) of a bipartition of \(H\). Because \(M\subseteq E(H)\), the set \(S\) contains exactly one endpoint of every edge of \(M\). Therefore \(G-S\) is bipartite. Also, \(S\) is independent in \(G\), since every edge of \(G\) with both endpoints in \(D\) is an edge of \(H\).

To prove that \(N_G(S)\) is independent, suppose \(xy\) were an edge with \(x,y\in N_G(S)\). Choose \(u,v\in S\) with \(ux,vy\in E(G)\).

- If \(u\ne v\), then \(u,x,y,v\) is a length-three walk, giving the forbidden edge \(uv\in E(H[S])\).
- If \(u=v\), then \(u,x,y\) form a triangle.

The second case is impossible because
\[
h(G)>4k-1\ge3.
\]
Thus \(S\) satisfies Lemma 3, and \(G\to C_5\).

It remains to prove that \(H\) is bipartite under the stated odd-girth assumption.

Suppose otherwise, and let \(C\) be a shortest odd cycle of \(H\), of length \(\ell\). It is chordless, and
\[
\ell\le2k-1.
\]
Let \(t\) be the number of matching edges from \(M\) lying on \(C\).

If a vertex of \(C\) has its matching partner also on \(C\), their matching edge must be an edge of \(C\), since \(C\) has no chord. Consequently, exactly \(\ell-2t\) vertices of \(C\) have their partners outside \(C\). There are only \(2k-\ell\) vertices outside \(C\), so
\[
\ell-2t\le2k-\ell,
\qquad\text{hence}\qquad
t\ge\ell-k.
\]

Replace each edge of \(C\cap M\) by its corresponding edge of \(G\), and each other edge of \(C\) by a witnessing odd walk of length at most three. Concatenating these walks gives an odd closed walk in \(G\) of length at most
\[
3\ell-2t
\le 3\ell-2(\ell-k)
=\ell+2k
\le4k-1.
\]
Every odd closed walk contains an odd cycle of no greater length: split at repeated vertices and retain an odd closed subwalk until a cycle remains. Hence
\[
h(G)\le4k-1,
\]
contrary to the hypothesis.

Therefore \(H\) is bipartite, completing the proof. ∎

## 3.3. Constructivity and a localized version

Given an odd-cycle transversal \(T\), no maximum-cut oracle is needed to use this argument. Properly two-color \(G-T\), extend arbitrarily, and perform improving single-vertex flips:

1. first only at vertices of \(T\), obtaining at most \(|T|\) monochromatic edges;
2. then at all vertices, obtaining a monochromatic matching of size at most \(|T|\).

Each flip strictly decreases the number of monochromatic edges, so this procedure is polynomial-time. One then constructs \(H\), two-colors it, and applies Lemma 3.

There is also a useful local strengthening. For any bipartizing matching \(M\), let \(k_i\) be the number of matching edges in a connected component \(H_i\) of its auxiliary graph. The shortest-odd-cycle argument uses only the component containing that cycle. Thus it suffices that
\[
h(G)>4\max_i k_i-1.
\]
This permits arbitrarily many defects overall, provided their auxiliary components are uniformly small.

# 4. An explicit girth-seven obstruction

## 4.1. Construction

Let
\[
P=\mathbb F_2^3\setminus\{0\}.
\]
Define \(Q\) as follows:

- its vertices are the unordered bases \(\{a,b,c\}\) of \(\mathbb F_2^3\);
- two vertices are adjacent when the corresponding triples are disjoint.

There are
\[
\frac{7\cdot6\cdot4}{6}=28
\]
vertices.

For a vertex \(A=\{a,b,c\}\), its complement in \(P\) is
\[
\{a+b,\ a+c,\ b+c,\ a+b+c\}.
\]
Of the four triples contained in this complement, exactly one is dependent:
\[
\{a+b,a+c,b+c\}.
\]
The other three are bases. Hence \(Q\) is cubic.

## 4.2. Verification of girth seven

For three distinct nonzero vectors, dependence is equivalent to their sum being zero.

**No triangles or 5-cycles.** In an \(\ell\)-cycle of disjoint triples, a fixed point of \(P\) can occur in at most \(\lfloor\ell/2\rfloor\) triples. Counting point occurrences would give
\[
3\ell\le7\lfloor\ell/2\rfloor.
\]
This fails for \(\ell=3\) and \(\ell=5\).

**No 4-cycles.** Two distinct triples \(A,B\) have at most one common neighbor: such a neighbor must be a three-element subset of \(P\setminus(A\cup B)\), which has at most three elements.

**No 6-cycles.** Suppose a 6-cycle existed, and let \(A,C,E\) be its three alternating vertices. Each pair has a common neighbor, so each pair intersects in exactly two points.

Three distinct three-element sets with pairwise intersections of size two either are contained in a four-element set or have a common two-element set. In the first case, all three pairwise unions coincide, and their unique possible common neighbors coincide, contradicting the six distinct vertices of the cycle.

In the second case, write
\[
A=X\cup\{z_1\},\quad
C=X\cup\{z_2\},\quad
E=X\cup\{z_3\},
\]
where \(|X|=2\), and put
\[
Y=P\setminus\bigl(X\cup\{z_1,z_2,z_3\}\bigr).
\]
Then \(|Y|=2\), and the other three cycle vertices are precisely
\[
Y\cup\{z_1\},\quad Y\cup\{z_2\},\quad Y\cup\{z_3\}.
\]

Write \(X=\{x_1,x_2\}\) and \(s_X=x_1+x_2\). Since all three triples \(X\cup\{z_i\}\) are bases, \(s_X\notin\{z_1,z_2,z_3\}\), and therefore \(s_X\in Y\). Similarly, the sum \(s_Y\) of the two elements of \(Y\) belongs to \(X\).

But if \(Y=\{s_X,y\}\) and \(s_X+y\in\{x_1,x_2\}\), then \(y\in\{x_1,x_2\}\), contradicting \(X\cap Y=\varnothing\). Thus there is no 6-cycle.

Finally, label the nonzero binary vectors by \(1,\ldots,7\), with vector addition given by bitwise XOR, and abbreviate \(\{i,j,k\}\) to \(ijk\). The sequence
\[
146,\ 237,\ 456,\ 137,\ 256,\ 147,\ 235,\ 146
\]
is a 7-cycle. Consecutive triples are disjoint, and their sums are respectively
\[
3,\ 6,\ 7,\ 5,\ 1,\ 2,\ 4,
\]
so all seven triples are bases.

Therefore \(Q\) has girth exactly seven.

## 4.3. Why \(Q\) cannot map to \(C_5\)

Call an unordered pair of incident edges a **wedge**. Under a homomorphism \(\varphi:G\to C_5\), a wedge \(u-v-w\) is **folded** if
\[
\varphi(u)=\varphi(w).
\]

Two observations give an obstruction.

**First, every cubic vertex has a folded wedge.** Its three neighbors map into the two neighbors of its image in \(C_5\), so two receive the same image.

**Second, every 7-cycle has exactly two folded wedges.** Orient such a cycle \(v_0v_1\cdots v_6v_0\), and write its successive color differences as
\[
\varepsilon_i\in\{+1,-1\}.
\]
Their integer sum is divisible by five. Since it is odd and between \(-7\) and \(7\), it equals \(5\) or \(-5\). Thus six signs agree and one is opposite. A wedge is folded precisely where consecutive signs differ, so there are exactly two folded wedges.

Now use the symmetry of \(Q\). The group \(\operatorname{GL}(3,2)\) acts transitively on its vertices. The stabilizer of a basis contains all permutations of its three basis vectors; these induce all permutations of its three neighbors. Consequently, the group acts transitively on wedges.

Let \(\mathcal C\) be the set of 7-cycles of \(Q\), and write \(t=|\mathcal C|\). Every wedge therefore belongs to the same number \(\lambda>0\) of these cycles. Counting cycle–wedge incidences gives
\[
7t=3|V(Q)|\lambda.
\]

If a homomorphism \(Q\to C_5\) existed, every vertex would contribute at least one folded wedge, each appearing in \(\lambda\) cycles. Hence the total number of folded cycle–wedge incidences would be at least
\[
|V(Q)|\lambda.
\]
On the other hand, every 7-cycle contributes exactly two, making that total
\[
2t=\frac67|V(Q)|\lambda,
\]
a contradiction. This proves Proposition 2. ∎

# 5. The remaining gap

Neither result settles the original problem.

- The graph \(Q\) has fixed girth seven. A disproof requires non-\(C_5\)-colorable cubic graphs of **arbitrarily large** girth.
- Theorem 1 retains an additional hypothesis involving an odd-cycle transversal, or the sizes of the auxiliary defect components. The argument supplies no uniform control of these parameters from girth alone.
- Bipartiteness of the auxiliary graph \(H\) is only a sufficient condition. A nonbipartite \(H\) is **not** a certificate that \(G\not\to C_5\); another choice of transversal or coloring may work.

Thus the established conclusions are a quantitative bounded-transversal case and the explicit lower restriction \(g_0\ge8\) on any possible universal threshold. The existence of such an absolute threshold remains unanswered by this argument.