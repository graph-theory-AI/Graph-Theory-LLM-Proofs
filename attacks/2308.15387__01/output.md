```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general crossover remains open, but it can be determined exactly for at most four colours and in the rainbow regime, where equality is shown not to be monotone in s.",
  "would_publish": false,
  "caveats": "Assumes the standard convention that an r-colouring may leave colours unused; the central large-r asymptotic gap is not narrowed."
}
```

# 1. Definitions

I use the definitions from the source. For an edge-colouring  
\(\chi:E(K_n)\to[r]\) and \(S\subseteq[r]\), let \(G_\chi(S)\) be the spanning graph formed by the edges whose colours lie in \(S\). Put
\[
F_\chi(s)=\max_{|S|\le s}\{\text{order of a largest component of }G_\chi(S)\},
\]
and
\[
G_\chi(s)=\max_{|S|\le s}
   |\{v:d_{G_\chi(S)}(v)>0\}|.
\]
Then
\[
f(n,r,s)=\min_\chi F_\chi(s),\qquad
g(n,r,s)=\min_\chi G_\chi(s).
\]
For \(n\ge2\), one always has \(f(n,r,s)\le g(n,r,s)\).

Define the literal threshold
\[
\sigma(n,r)=\min\{s\in[r]:f(n,r,s)=g(n,r,s)\}.
\]

The case \(n=1\) is omitted because the “incident to an edge” convention makes it exceptional.

# 2. Results obtained

## Theorem A: universal agreement bound

For every \(n\ge2\) and \(r\ge1\),
\[
f(n,r,s)=g(n,r,s)=n
\qquad\text{whenever}\qquad
s\ge \min\left\{n-1,\left\lceil\frac r2\right\rceil\right\}.
\]

Indeed, a spanning tree uses at most \(n-1\) colours. For the other bound, partition the \(r\) colours into sets \(A,B\) of orders at most \(\lceil r/2\rceil\). The graphs \(G_\chi(A)\) and \(G_\chi(B)\) are complementary. A graph or its complement is connected, so one of these two colour sets gives a connected spanning graph.

This does not improve the asymptotic bound from the source, but is useful for the exact small-\(r\) calculations below.

## Theorem B: exact thresholds for \(r\le4\)

For \(n\ge2\),
\[
\sigma(n,1)=\sigma(n,2)=1.
\]

For three colours,
\[
\boxed{
\sigma(n,3)=
\begin{cases}
1,&n\in\{2,3,6\},\\
2,&n=4,5\text{ or }n\ge7.
\end{cases}}
\]

For four colours,
\[
\boxed{
\sigma(n,4)=
\begin{cases}
1,&n\in\{2,3,5\},\\
2,&n=4\text{ or }n\ge6.
\end{cases}}
\]

The three-colour calculation is exact at the level of the two functions:
\[
g(n,3,1)=\left\lceil\frac{2n}{3}\right\rceil,
\]
and
\[
f(n,3,1)=
\begin{cases}
\dfrac n2+1,&n\equiv2\pmod4,\\[2mm]
\left\lceil\dfrac n2\right\rceil,&n\not\equiv2\pmod4.
\end{cases}
\]
Moreover,
\[
f(n,3,s)=g(n,3,s)=n\qquad(s\ge2).
\]

## Theorem C: the rainbow regime and failure of monotonicity

Let \(m=\binom n2\). At \(r=m\), and also for \(r\ge m\) under the usual “at most \(r\) colours” convention,
\[
\boxed{f(n,r,s)=\min\{n,s+1\},\qquad
g(n,r,s)=\min\{n,2s\}.}
\]

Consequently, for every \(n\ge4\),
\[
f(n,r,1)=g(n,r,1)=2,
\]
but
\[
f(n,r,s)<g(n,r,s)\qquad(2\le s\le n-2),
\]
while equality holds again for \(s\ge n-1\).

Thus equality of \(f\) and \(g\) is not monotone in \(s\). In particular, the literal “smallest \(s\)” need not describe the onset of permanent agreement. If one instead defines
\[
\widehat{\sigma}(n,r)=
\min\{s:f(n,r,t)=g(n,r,t)\text{ for every }t\ge s\},
\]
then in the rainbow regime, for \(n\ge4\),
\[
\sigma(n,r)=1,\qquad \widehat{\sigma}(n,r)=n-1.
\]

# 3. Structural formulations

Two elementary reformulations are useful.

## 3.1. An exact set-system formulation for \(g\)

Let \(\mathcal A=(A_1,\dots,A_n)\) be a sequence of nonempty, pairwise-intersecting subsets of \([r]\), repetitions allowed. Define
\[
\Gamma_s(\mathcal A)
 =\max_{\substack{S\subseteq[r]\\|S|\le s}}
   |\{j:A_j\cap S\ne\varnothing\}|.
\]
Then
\[
\boxed{
g(n,r,s)=
\min_{\mathcal A}\Gamma_s(\mathcal A),
}
\tag{1}
\]
where the minimum ranges over all such pairwise-intersecting sequences.

To see this, given a colouring put
\[
A_v=\{i:v\text{ is incident to an edge of colour }i\}.
\]
For distinct \(u,v\), the colour of \(uv\) belongs to \(A_u\cap A_v\), so these sets are pairwise intersecting, and \(\Gamma_s(\mathcal A)=G_\chi(s)\).

Conversely, given a pairwise-intersecting sequence, colour each edge \(uv\) by an arbitrary member of \(A_u\cap A_v\). The actual set of colours incident with \(v\) is then a subset of \(A_v\), so the resulting value of \(G_\chi(s)\) is at most \(\Gamma_s(\mathcal A)\). This proves (1).

## 3.2. An exact hypergraph formulation for \(f(n,r,1)\)

Let \(M_r(k)\) be the maximum number of edges, counted with multiplicity, in an intersecting \(r\)-partite \(r\)-uniform multihypergraph of maximum degree at most \(k\). Then
\[
\boxed{
f(n,r,1)=\min\{k:M_r(k)\ge n\}.
}
\tag{2}
\]

Given a colouring whose monochromatic components all have order at most \(k\), make one part for each colour, with one hypergraph vertex for every monochromatic component of that colour. Each vertex \(v\in V(K_n)\) gives the hyperedge consisting of the \(r\) monochromatic components containing \(v\). Two such hyperedges intersect because the edge between the corresponding vertices has some colour. Component orders are exactly the relevant hypergraph degrees.

Conversely, from an intersecting \(r\)-partite hypergraph, assign to every pair of hyperedges a colour corresponding to one of their common coordinates. A monochromatic component is contained in a coordinate fibre, and hence has order at most \(k\).

# 4. Exact calculation for three colours

## 4.1. Calculation of \(g(n,3,1)\)

Let \(N_3(k)\) be the maximum length of a pairwise-intersecting sequence of nonempty subsets of \([3]\), with every element occurring at most \(k\) times.

If the sequence contains a singleton \(\{i\}\), then all sets contain \(i\), so its length is at most \(k\). Otherwise every set has order at least two, and hence
\[
2|\mathcal A|\le \sum_{i=1}^3 d(i)\le3k.
\]
Thus
\[
N_3(k)\le\left\lfloor\frac{3k}{2}\right\rfloor.
\]
Equality is attained using the three sets \(12,13,23\) with balanced multiplicities. Hence
\[
N_3(k)=\left\lfloor\frac{3k}{2}\right\rfloor.
\]
Taking the inverse using (1) gives
\[
g(n,3,1)=\left\lceil\frac{2n}{3}\right\rceil.
\]

## 4.2. Intersecting three-partite hypergraphs

We need the following exact extremal value:
\[
M_3(k)=
\begin{cases}
2k,&k\text{ even},\\
2k-1,&k\text{ odd}.
\end{cases}
\tag{3}
\]

### A two-vertex transversal lemma

Every intersecting three-partite three-uniform hypergraph has a vertex cover of order at most two.

Choose an edge \(e=(x_1,x_2,x_3)\). If some pair of its vertices meets every edge, we are done. Otherwise, for each \(i\) there is an edge meeting \(e\) only in \(x_i\). Pairwise intersection forces these three edges to have the form
\[
(x_1,y_2,y_3),\qquad
(y_1,x_2,y_3),\qquad
(y_1,y_2,x_3),
\]
where \(x_i\ne y_i\).

I claim that \(\{x_1,y_1\}\) meets every edge. An edge avoiding both would have to choose its second and third coordinates so as to meet all four pairs
\[
(x_2,x_3),\quad (y_2,y_3),\quad (x_2,y_3),\quad (y_2,x_3).
\]
If its second coordinate is \(x_2\), the second and fourth requirements force its third coordinate to equal both \(y_3\) and \(x_3\), a contradiction. If its second coordinate is not \(x_2\), the first and third requirements give the same contradiction. Thus the claimed two-cover exists.

It follows immediately that an intersecting three-partite hypergraph of maximum degree \(k\) has at most \(2k\) edges.

### Equality forces \(k\) even

Suppose there are \(2k\) edges. For a two-cover \(\{x,y\}\), equality forces
\[
d(x)=d(y)=k
\]
and no edge may contain both \(x\) and \(y\).

If \(x,y\) belong to different parts, every edge through \(x\) and every edge through \(y\) can intersect only in the third part. Consequently all \(2k\) edges contain a common vertex in that part, contradicting the maximum-degree bound.

Thus \(x,y\) lie in the same part. Project the \(k\) edges through \(x\) and the \(k\) edges through \(y\) onto the other two parts. This gives two cross-intersecting multisets \(\mathcal P,\mathcal Q\) of edges of a bipartite graph.

The support of \(\mathcal P\) must contain two disjoint edges. Otherwise it is a star, and cross-intersection forces \(\mathcal Q\) to use a vertex already saturated by the \(k\) members of \(\mathcal P\). Let the two disjoint edges be
\[
b_1c_1,\qquad b_2c_2.
\]
Every edge of \(\mathcal Q\) is then one of
\[
b_1c_2,\qquad b_2c_1,
\]
and both types must occur. Cross-intersection in the other direction forces \(\mathcal P\) to use only the two diagonal types.

Let their multiplicities in \(\mathcal P\) be \(a,k-a\), and let the multiplicities of the two off-diagonal types in \(\mathcal Q\) be \(b,k-b\). The four degree inequalities give
\[
a+b=k,\qquad a=b,
\]
and hence \(2a=k\). Therefore \(k\) is even.

For even \(k=2t\), take \(t\) copies of each of
\[
(x,b_1,c_1),\quad (x,b_2,c_2),\quad
(y,b_1,c_2),\quad (y,b_2,c_1).
\]
This gives \(2k\) edges and maximum degree \(k\).

For odd \(k=2t+1\), take multiplicities \(t+1,t,t,t\) of these four types. This gives \(2k-1\) edges and maximum degree \(k\). This proves (3).

## 4.3. Inverting \(M_3(k)\)

By (2) and (3),
\[
f(n,3,1)=
\begin{cases}
n/2+1,&n\equiv2\pmod4,\\[1mm]
\lceil n/2\rceil,&\text{otherwise}.
\end{cases}
\]

For \(s=2\), put one colour in one class and the other two in the complementary class. One of the two resulting complementary graphs is connected. Hence
\[
f(n,3,2)=g(n,3,2)=n.
\]

Finally,
\[
f(n,3,1)=g(n,3,1)
\]
holds exactly for \(n=2,3,6\). Indeed, the values for \(n=2,\dots,6\) are respectively
\[
\begin{array}{c|ccccc}
n&2&3&4&5&6\\ \hline
f(n,3,1)&2&2&2&3&4\\
g(n,3,1)&2&2&3&4&4,
\end{array}
\]
and for \(n>6\),
\[
f(n,3,1)\le\frac n2+1<\frac{2n}{3}\le g(n,3,1).
\]

# 5. Four colours

Since the colours can be partitioned into two pairs, the graph/complement argument gives
\[
f(n,4,2)=g(n,4,2)=n.
\]
Thus only \(s=1\) has to be examined.

For every four-colouring, the incidence-set argument gives
\[
g(n,4,1)\ge \left\lceil\frac n2\right\rceil:
\]
if an incidence set is a singleton, its colour occurs at every vertex; otherwise every incidence set has order at least two, so there are at least \(2n\) incidences among four colours.

For upper bounds on \(f\), use the following four-partite intersecting hypergraph. For each \((x,y)\in\mathbb F_3^2\), take the edge
\[
(x,\ y,\ x+y,\ x+2y).
\tag{4}
\]
Any two distinct such edges intersect: every nonzero \((a,b)\in\mathbb F_3^2\) satisfies one of
\[
a=0,\qquad b=0,\qquad a+b=0,\qquad a+2b=0.
\]
There are nine edges, and every coordinate vertex has degree three.

If \(n=9q+a\), take \(q\) copies of all nine edges and \(a\) additional distinct edges. The extra edges can be chosen so that the maximum degree is at most
\[
\begin{cases}
3q,&a=0,\\
3q+1,&a=1,\\
3q+2,&a=2,3,\\
3q+3,&4\le a\le8.
\end{cases}
\tag{5}
\]
For \(a=3\), choose three non-collinear points of \(\mathbb F_3^2\). By (2), this gives corresponding upper bounds on \(f(n,4,1)\). A direct check of (5) gives
\[
f(n,4,1)<\left\lceil\frac n2\right\rceil\le g(n,4,1)
\qquad(n\ge7).
\]

The remaining cases are as follows.

- \(n=2,3\): a rainbow colouring is possible, and \(f=g=2\).
- \(n=4\): \(f(4,4,1)=2\), since \(K_4\) is properly edge-colourable with three colours, while \(g(4,4,1)>2\), since six separate colours would be required for every colour support to have order at most two.
- \(n=5\): \(f(5,4,1)=3\). It cannot be two because \(\chi'(K_5)=5\), while five edges from (4) give the upper bound three. Also \(g(5,4,1)=3\): the pairwise-intersecting sequence
  \[
  12,\ 13,\ 14,\ 234,\ 234
  \]
  has maximum element frequency three.
- \(n=6\): similarly \(f(6,4,1)=3\). But \(g(6,4,1)\ge4\). Otherwise six pairwise-intersecting incidence sets would each have order two, with every ground element occurring at most three times. A pairwise-intersecting family of two-subsets is contained in either a star or a triangle; the former has a common element occurring six times, while the latter uses only three ground elements and has total capacity at most nine incidences, less than the required twelve.

This proves the stated four-colour threshold.

# 6. Rainbow regime and nonmonotonicity

A refinement of a colouring cannot increase either \(F_\chi(s)\) or \(G_\chi(s)\): any set of at most \(s\) refined colours maps to at most \(s\) old colours, and its graph and support are subgraphs/subsets of the corresponding old union.

When \(r\ge m=\binom n2\), the rainbow colouring is a refinement of every colouring and is itself allowed. It therefore minimizes both functions.

In the rainbow colouring, selecting \(s\) colours is selecting \(s\) edges. A graph with \(s\) edges has no connected component on more than \(s+1\) vertices, and a tree attains this bound. Hence
\[
f(n,r,s)=\min\{n,s+1\}.
\]
The endpoints of \(s\) edges number at most \(2s\), and a matching, followed if necessary by one overlapping edge, attains \(\min\{n,2s\}\). Thus
\[
g(n,r,s)=\min\{n,2s\}.
\]

For \(n\ge4\), these formulas give equality at \(s=1\), strict inequality for \(2\le s\le n-2\), and equality again for \(s\ge n-1\). This establishes the claimed nonmonotonicity even under a convention requiring every colour to be used, by taking exactly \(r=\binom n2\).

# 7. A further exact boundary at \(s=1\)

Let \(\chi'(K_n)\) denote the edge-chromatic number:
\[
\chi'(K_n)=
\begin{cases}
n-1,&n\text{ even},\\
n,&n\text{ odd}.
\end{cases}
\]
Then
\[
f(n,r,1)=2\quad\Longleftrightarrow\quad r\ge\chi'(K_n),
\]
because all monochromatic components have order at most two exactly when every colour class is a matching.

Also,
\[
g(n,r,1)=2\quad\Longleftrightarrow\quad r\ge\binom n2,
\]
because a colour supported on at most two vertices contains at most one edge.

Consequently,
\[
f(n,r,1)<g(n,r,1)
\qquad\text{whenever}\qquad
\chi'(K_n)\le r<\binom n2.
\]

# 8. What remains open

These results give exact finite slices and identify a genuine issue with interpreting the first equality as a monotone transition. They do not determine \(\sigma(n,r)\) for general \(r\ge5\), nor do they improve the source paper’s asymptotic gap between the separation range \(s\ll\sqrt r/\log r\) and the agreement range \(s\ge\sqrt{r\log r}\). A full solution would need substantially more information about unions of several coordinate classes in intersecting multipartite hypergraphs, not merely the one-colour extremal quantities used above.