```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained construction gives mader_chi(K_n) >= (1/(2e)-o(1)) n^2/log n, but does not determine the exact threshold.",
  "would_publish": false,
  "caveats": "Logarithms are natural; novelty of the lower bound has not been checked, and no exact value for n >= 3 is established here."
}
```

## 1. Statement of the partial results

Write
\[
M(n)=\mathrm{mader}_{\vec\chi}(\vec K_n),
\]
where \(\vec K_n\) has both arcs between every pair of distinct vertices. Thus \(M(n)\) is the least integer \(k\) such that every digraph of dichromatic number at least \(k\) contains a subdivision of \(\vec K_n\).

I use the usual **arc-by-arc subdivision** convention: replacement paths have pairwise disjoint interiors, and their interiors avoid all branch vertices. In particular, paths replacing two opposite arcs may not share internal vertices.

The following bounds admit self-contained proofs:
\[
M(1)=1,\qquad M(2)=2,
\]
and, for every \(n\ge3\),
\[
\boxed{
M(n)\ge
\max\left\{
n+1,\,
\left\lceil\frac{3(n-2)}2\right\rceil+1
\right\}.
}
\]
More substantially,
\[
\boxed{
\liminf_{n\to\infty}\frac{M(n)\log n}{n^2}
\ge \frac1{2e}.
}
\tag{1}
\]
The witnesses for (1) can all be chosen **bidirected**: they arise from undirected graphs by replacing every edge with a digon.

These are lower-bound results, not a solution of the exact-value problem. I make no claim that these constructions or their asymptotic bound are new.

## 2. A missing-arc obstruction

For a digraph \(D\) and \(B\subseteq V(D)\), define
\[
\mu_D(B)=
|\{(u,v)\in B^2:u\ne v,\ uv\notin A(D)\}|.
\]

**Lemma 1.** If a digraph \(D\) of order \(N\) contains a subdivision of \(\vec K_n\) with branch set \(B\), then
\[
\mu_D(B)\le N-n.
\]

**Proof.**
For each missing arc \(uv\) between branch vertices, its replacement path has at least one internal vertex. Replacement paths have disjoint interiors, so different missing arcs require different internal vertices. There are at most \(N-n\) available internal vertices. ∎

This elementary counting obstruction is the basis of the asymptotic construction.

## 3. Explicit obstructions

For an undirected graph \(G\), let \(\overleftrightarrow G\) denote its bidirected version. Since every edge becomes a directed 2-cycle,
\[
\vec\chi(\overleftrightarrow G)=\chi(G).
\tag{2}
\]

### 3.1. The bound \(M(n)\ge n+1\)

Let
\[
G=K_{n-3}\vee C_5,
\]
where \(\vee\) denotes the graph join, and put \(D=\overleftrightarrow G\). Then
\[
\vec\chi(D)=\chi(G)=(n-3)+3=n.
\]

Suppose \(D\) contained a subdivision of \(\vec K_n\). Every vertex of the \(C_5\) has in-degree and out-degree exactly \(n-1\) in \(D\). Consequently, if such a vertex \(v\) is a branch vertex, all arcs incident with \(v\) must occur in the subdivision.

Every neighbor of \(v\) must then also be a branch vertex. Indeed, if a neighbor \(w\) were internal, both \(vw\) and \(wv\) would occur in the subdivision. The replacement path starting with \(vw\) could not use \(wv\), as that would return to its starting branch vertex. Thus the two arcs would belong to different replacement paths sharing the internal vertex \(w\), which is forbidden.

There is at least one branch vertex on the \(C_5\), since only \(n-3\) vertices lie outside it. The preceding observation propagates around the cycle, making all five cycle vertices branch vertices. It also makes all \(n-3\) universal vertices branch vertices. This gives \(n+2\) branch vertices, a contradiction.

Thus \(D\) has dichromatic number \(n\) and no \(\vec K_n\)-subdivision, proving
\[
M(n)\ge n+1.
\]

In particular, the tempting formula \(M(n)=n\) already fails at \(n=3\).

### 3.2. A stronger explicit linear bound

Let \(D_r\) consist of three bidirected cliques \(A,B,C\), each of order \(r\), with all cross-arcs directed
\[
A\longrightarrow B\longrightarrow C\longrightarrow A.
\]

An acyclic vertex set meets each clique in at most one vertex and cannot meet all three cliques. Hence
\[
\vec\chi(D_r)\ge \left\lceil\frac{3r}{2}\right\rceil.
\tag{3}
\]
Equality also holds: pair vertices from different cliques, leaving at most one singleton. For \(r=2u\), use \(u\) pairs of each of the types \(AB,BC,CA\); for \(r=2u+1\), use \(u+1,u,u\) such pairs, respectively, and one singleton in \(C\).

We can determine exactly the largest complete bidirected subdivision in \(D_r\).

Suppose its branch set has \(a,b,c\) vertices in \(A,B,C\). Every replacement path from a branch vertex in \(B\) to one in \(A\) must use an internal vertex in \(C\). Consequently,
\[
ab\le r-c.
\]
Cyclically,
\[
bc\le r-a,\qquad ca\le r-b.
\tag{4}
\]

If at least two branch counts are positive, say \(a,b\ge1\), then
\[
r\ge ab+c\ge a+b+c-1,
\]
because \(ab\ge a+b-1\). If only one branch count is positive, there are at most \(r\) branches. Thus every complete bidirected subdivision in \(D_r\) has order at most \(r+1\).

Conversely, \(D_r\) contains a subdivision of \(\vec K_{r+1}\): take all \(r\) vertices of \(A\) and one vertex \(b\in B\) as branches. Use direct arcs inside \(A\) and from \(A\) to \(b\), and replace each arc \(b\to a\) by
\[
b\to c_a\to a,
\]
using distinct \(c_a\in C\).

Taking \(r=n-2\), equation (3) therefore gives
\[
M(n)\ge \left\lceil\frac{3(n-2)}2\right\rceil+1.
\]

### 3.3. The exact first two values

Clearly \(M(1)=1\). A subdivision of \(\vec K_2\) is precisely a directed cycle. A digraph has dichromatic number at least \(2\) exactly when it is not acyclic. Therefore \(M(2)=2\).

## 4. The asymptotic lower bound

The useful refinement over a direct random-graph construction is to take a **clique blow-up** of a smaller random graph. This keeps the independence number small without changing the leading missing-arc obstruction.

### 4.1. A blow-up lemma

Let \(G[K_t]\) denote the graph obtained by replacing every vertex of \(G\) by a \(t\)-clique, with complete joins between cliques corresponding to edges of \(G\).

**Lemma 2.** Let \(G\) have \(m\) vertices, let \(n\le mt\), and put
\[
s=\left\lfloor\frac nt\right\rfloor.
\]
For every \(n\)-vertex set \(B\) in
\[
D=\overleftrightarrow{G[K_t]},
\]
we have
\[
\mu_D(B)\ge
2t^2\min_{\substack{S\subseteq V(G)\\|S|=s}}
e(\overline G[S]).
\tag{5}
\]

**Proof.**
Let \(b_i\) count the vertices of \(B\) in the clique corresponding to \(i\in V(G)\). Then
\[
0\le b_i\le t,\qquad \sum_i b_i=n,
\]
and
\[
\mu_D(B)=
2\sum_{ij\in E(\overline G)}b_i b_j.
\tag{6}
\]

Consider the quadratic expression
\[
Q(b)=\sum_{ij\in E(\overline G)}b_i b_j.
\]
If two coordinates satisfy \(0<b_i,b_j<t\), vary them as
\[
(b_i,b_j)\mapsto(b_i+x,b_j-x).
\]
On the feasible interval, \(Q\) is a concave function of \(x\): its quadratic coefficient is \(-1\) if \(ij\in E(\overline G)\), and \(0\) otherwise. Therefore one endpoint of the interval does not increase \(Q\).

Repeating this operation leaves at most one coordinate strictly between \(0\) and \(t\). The resulting vector has exactly \(s\) coordinates equal to \(t\), with a possible additional coordinate equal to \(n-st\). If \(S\) is the set of full coordinates, nonnegativity of the remaining terms gives
\[
Q(b)\ge t^2e(\overline G[S]).
\]
Now use (6). ∎

### 4.2. Choosing the random base graph

Fix constants
\[
0<q<1,\qquad 0<\varepsilon<q/3,
\]
and write
\[
L=\log(1/q),\qquad C=3\varepsilon^{-2}.
\]

For sufficiently large \(n\), define
\[
t=\left\lfloor\frac{n}{C\log n}\right\rfloor,\qquad
s=\left\lfloor\frac nt\right\rfloor,\qquad
m=\left\lfloor\frac{(q-2\varepsilon)n^2}{t}\right\rfloor.
\tag{7}
\]
Then
\[
s\sim C\log n,\qquad
m\sim(q-2\varepsilon)C\,n\log n,\qquad
\log m\sim\log n.
\tag{8}
\]

Choose \(G\) randomly on \(m\) vertices, including each edge independently with probability \(1-q\). We require two properties:

1. \(\alpha(G)\le (2/L)\log m+O(1)\);
2. every \(s\)-vertex set has at least
   \[
   (q-\varepsilon)\binom{s}{2}
   \]
   nonedges.

Both hold simultaneously with probability tending to one.

For the first, put
\[
a=\left\lceil\frac{2\log m}{L}+3\right\rceil.
\]
The probability of an independent \(a\)-set is at most
\[
\binom ma q^{\binom a2}
\le
\exp\left(a\log m-\frac{La(a-1)}2\right)
\le e^{-La}=o(1).
\tag{9}
\]
Thus \(\alpha(G)<a\) with probability \(1-o(1)\).

For the second, the number \(X_S\) of nonedges in a fixed \(s\)-set is binomial with parameters \(\binom s2,q\). The standard Hoeffding bound gives
\[
\Pr\left(X_S<(q-\varepsilon)\binom s2\right)
\le
\exp\bigl(-\varepsilon^2s(s-1)\bigr).
\]
A union bound over all \(s\)-sets bounds the failure probability by
\[
\exp\bigl(s\log m-\varepsilon^2s(s-1)\bigr).
\tag{10}
\]
By (8) and \(C=3\varepsilon^{-2}\), the exponent in (10) is
\[
(-2+o(1))s\log n,
\]
so this probability also tends to zero.

Consequently, for every sufficiently large \(n\), a graph \(G\) satisfying both properties exists.

### 4.3. Excluding the subdivision

Take such a graph \(G\), and set
\[
D=\overleftrightarrow{G[K_t]},\qquad N=mt.
\]
For every \(n\)-vertex set \(B\), Lemma 2 gives
\[
\mu_D(B)\ge
(q-\varepsilon)t^2s(s-1).
\tag{11}
\]

Since \(st/n\to1\) and \(s\to\infty\),
\[
t^2s(s-1)=(1-o(1))n^2.
\]
On the other hand, the definition of \(m\) gives
\[
N\le(q-2\varepsilon)n^2.
\]
Because \(q-\varepsilon>q-2\varepsilon\), equation (11) implies, for all sufficiently large \(n\),
\[
\mu_D(B)>N
\]
for every possible branch set \(B\). This contradicts the necessary condition in Lemma 1. Hence \(D\) contains no subdivision of \(\vec K_n\).

### 4.4. Its dichromatic number

An independent set in \(G[K_t]\) contains at most one vertex from each replacement clique, and its represented base vertices form an independent set in \(G\). Thus
\[
\alpha(G[K_t])=\alpha(G)<a.
\]
Using (2),
\[
\vec\chi(D)=\chi(G[K_t])
\ge \frac{N}{\alpha(G)}
\ge \frac Na.
\]
Equations (7)–(9) now give
\[
\frac Na=
\left(\frac{(q-2\varepsilon)L}{2}+o(1)\right)
\frac{n^2}{\log n}.
\]

Since \(D\) is a counterexample to forcing \(\vec K_n\), it follows that
\[
\liminf_{n\to\infty}
\frac{M(n)\log n}{n^2}
\ge \frac{(q-2\varepsilon)\log(1/q)}2.
\]
Letting \(\varepsilon\downarrow0\),
\[
\liminf_{n\to\infty}
\frac{M(n)\log n}{n^2}
\ge \frac{q\log(1/q)}2.
\]
Finally, \(q\log(1/q)\) is maximized at \(q=e^{-1}\), where its value is \(e^{-1}\). This proves (1).

## 5. What remains unresolved

Combining this construction with the upper bound supplied in the question gives
\[
\left(\frac1{2e}-o(1)\right)\frac{n^2}{\log n}
\le M(n)
\le (n-1)4^{(n-1)^2}+1.
\]

The lower bound shows that no linear answer is possible and that even restricting potential counterexamples to bidirected graphs leaves a nearly quadratic obstruction.

However, the gap to the supplied upper bound is enormous. No matching forcing theorem, polynomial upper bound, or exact value for \(n\ge3\) has been proved here. Thus this is a rigorous partial attack on Problem 12, not its resolution.