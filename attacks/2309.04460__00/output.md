```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general log-log question remains open, but the conjectured O(log n) bound holds sharply for colour-saturated graphs and for commuting matching colour classes.",
  "would_publish": false,
  "caveats": "No general O(log n) bound or superlogarithmic construction is obtained, and no novelty claim about the special cases is made."
}
```

## 1. Extremal formulation

Let \(f(n)\) be the maximum average degree of a properly edge-coloured simple graph on \(n\) vertices containing no rainbow cycle. The cited theorem gives
\[
f(n)=O(\log n\log\log n),
\]
while standard constructions give \(f(n)=\Omega(\log n)\). Thus the question is whether
\[
f(n)=O(\log n).
\]

I do not resolve this in general. I prove the \(O(\log n)\) bound in two substantial special cases, one of them with an exact sharp bound.

Throughout, \(M_1,\dots,M_k\) are the colour classes. Properness means that every \(M_i\) is a matching.

### Basic reformulation

A properly coloured graph has no rainbow cycle if and only if every set containing at most one edge of each colour is a forest. Consequently, if \(c(G)\) denotes the number of connected components,
\[
k\le n-c(G).
\tag{1}
\]

There is also the useful local characterization
\[
\bigl|\{i:M_i\cap E(G[S])\ne\varnothing\}\bigr|\le |S|-1
\quad\text{for every nonempty }S\subseteq V(G).
\tag{2}
\]
Indeed, if \(S\) internally contains at least \(|S|\) colours, choosing one internal edge of each colour produces at least \(|S|\) rainbow edges on \(|S|\) vertices and hence a rainbow cycle. The converse follows by taking \(S\) to be the vertex set of a rainbow cycle.

Also, simply because \(|M_i|\le n/2\),
\[
\overline d(G)=\frac{2}{n}\sum_i |M_i|\le k.
\tag{3}
\]
Thus the conjectured bound already holds whenever \(k=O(\log n)\).

## 2. A binary common-complement criterion

Write
\[
\partial(uv)=\mathbf e_u+\mathbf e_v\in\mathbb F_2^{V(G)}
\]
for the binary incidence vector of an edge, and let
\[
U=\operatorname{span}_{\mathbb F_2}\{\partial e:e\in E(G)\}.
\]
Then
\[
\dim U=n-c(G)=:r.
\]

Call the colouring **binary-complementable** if there is a subspace
\[
W\le U,\qquad \dim W=r-k,
\]
such that, for every choice \(e_i\in M_i\),
\[
U=W\oplus
\operatorname{span}\{\partial e_1,\dots,\partial e_k\}.
\tag{4}
\]

### Theorem 1

If a properly edge-coloured graph with no rainbow cycle is binary-complementable, then
\[
|E(G)|\le \frac n2\log_2 n,
\qquad
\overline d(G)\le \log_2 n.
\tag{5}
\]

#### Proof

Pass to the quotient \(Q=U/W\), which has dimension \(k\). Choose reference edges \(f_i\in M_i\). By (4), their images form a basis of \(Q\), which we identify with the standard basis of \(\mathbb F_2^k\).

For an edge \(e\in M_i\), let \(x(e)\in\mathbb F_2^k\) be its coordinate vector in this basis. Every matrix obtained by choosing one column \(x(e_i)\) from each colour is nonsingular.

First, the \(i\)-th coordinate of every \(x(e)\), \(e\in M_i\), equals \(1\): replace only \(f_i\) by \(e\) in the reference basis. The resulting matrix is the identity except in column \(i\), so its determinant is precisely \(x(e)_i\).

Define a directed graph \(D\) on the colours by putting an arc \(i\to j\), for \(i\ne j\), if some \(e\in M_i\) satisfies \(x(e)_j=1\).

We claim that \(D\) is acyclic. Suppose instead that
\[
i_1\to i_2\to\cdots\to i_s\to i_1
\]
is a shortest directed cycle. For each \(a\), choose \(e_{i_a}\in M_{i_a}\) witnessing \(i_a\to i_{a+1}\), with indices cyclically interpreted. By minimality, the restriction of \(x(e_{i_a})\) to the cycle coordinates has ones exactly in positions \(i_a\) and \(i_{a+1}\): any additional off-diagonal entry would give a chord and hence a shorter directed cycle.

Choose these edges on the cycle and the reference edges for all other colours. The corresponding principal \(s\times s\) submatrix has two ones in every row and its columns sum to zero over \(\mathbb F_2\). It is singular, contradicting (4). Hence \(D\) is acyclic.

Order the colours topologically as \(1,\dots,k\). Then for every \(e\in M_i\),
\[
x(e)_i=1,\qquad x(e)_j=0\quad(j<i).
\tag{6}
\]

For each coordinate functional on \(Q\), compose with \(U\to Q\). Every linear functional \(\lambda:U\to\mathbb F_2\) is represented on graph edges by a vertex cut: there is a function \(s:V(G)\to\mathbb F_2\) such that
\[
\lambda(\partial(uv))=s(u)+s(v)
\quad\text{for every }uv\in E(G).
\tag{7}
\]
To see this, choose a root in each component and define \(s(v)\) by summing \(\lambda\) along a root-to-\(v\) path; cycle sums vanish, so this is well defined.

Let \(s_i\) represent the \(i\)-th coordinate. By (6), every colour-\(i\) edge has endpoints agreeing on
\[
s_1,\dots,s_{i-1}
\]
and disagreeing on \(s_i\).

Partition \(V(G)\) into atoms according to the first \(i-1\) bits. If an atom \(A\) is split by \(s_i\) into parts of sizes \(a_0,a_1\), then the colour-\(i\) edges inside \(A\) form a matching across that split. Therefore
\[
|M_i|\le \sum_A \min(a_0,a_1).
\tag{8}
\]

Let \(X\) be a uniformly random vertex and put \(S_i=s_i(X)\). Since
\[
h_2(p)\ge 2\min(p,1-p)
\tag{9}
\]
for binary entropy \(h_2\), (8) gives
\[
|M_i|
 \le \frac n2 H(S_i\mid S_1,\dots,S_{i-1}).
\]
Summing and using the chain rule,
\[
|E(G)|
 \le \frac n2 H(S_1,\dots,S_k)
 \le \frac n2 H(X)
 \le \frac n2\log_2 n.
\]
This proves (5). \(\square\)

The common-complement hypothesis is not automatic. For example, the properly \(3\)-edge-coloured \(K_{3,3}\) below has nine edges, whereas \((6/2)\log_2 6<8\), so it cannot admit such a complement.

## 3. The colour-saturated case

Equality in (1) gives a concrete and sharp special case.

### Theorem 2

Suppose \(G\) has no rainbow cycle and
\[
k=n-c(G).
\tag{10}
\]
If the connected components have orders \(n_1,\dots,n_{c(G)}\), then
\[
|E(G)|\le \frac12\sum_j n_j\log_2 n_j
\le \frac n2\log_2 n.
\tag{11}
\]
In particular,
\[
\overline d(G)\le\log_2 n.
\]

#### Proof

Every full rainbow transversal has \(k=n-c(G)\) edges and is a forest, hence is a spanning forest of \(G\). Thus the binary-complement condition holds with \(W=\{0\}\), proving the second inequality in (11) directly from Theorem 1.

For the componentwise form, fix a rainbow spanning forest \(T\). A colour cannot occur in two distinct components: if its reference edge lies in one component and another edge of that colour lies in a second component, replacing the reference edge by the latter adds an edge to an already spanned tree in the second component and creates a rainbow cycle. Thus each component of order \(n_j\) has exactly \(n_j-1\) colours, and Theorem 1 applies componentwise. \(\square\)

There is also a useful graphical normal form in the connected case. Identify the colours with the edges of a fixed rainbow spanning tree \(T\). In the binary tree basis, the coordinate vector of an edge \(uv\) is the characteristic vector of the tree path \(P_T(u,v)\). The acyclicity argument in Theorem 1 therefore gives an ordering \(\prec\) of \(E(T)\) such that
\[
\operatorname{colour}(uv)
  =\min\nolimits_{\prec} E(P_T(u,v)).
\tag{12}
\]

Conversely, any colouring satisfying (12) has no rainbow cycle. Indeed, for a cycle \(C\), choose the earliest tree edge \(t\) appearing in one of the paths \(P_T(e)\), \(e\in E(C)\). The cycle crosses the fundamental cut of \(t\) a positive even number of times. Every cycle edge crossing that cut is coloured \(t\), so \(C\) has a repeated colour.

Formula (12) also gives a direct recurrence. If the earliest tree edge splits \(T\) into vertex sets of sizes \(a\le b\), every graph edge crossing the split has the same colour and hence these crossing edges form a matching of size at most \(a\). Therefore
\[
F(a+b)\le F(a)+F(b)+a.
\tag{13}
\]
The induction \(F(n)\le \frac n2\log_2 n\) follows from
\[
n\log_2n-a\log_2a-b\log_2b
   =n\,h_2(a/n)\ge 2a.
\]

### Sharpness within the saturated class

For \(n=2^h\), equality in (11) is attainable.

Take \(T=P_n\). Recursively delete the central edge of each current subpath, ordering a separator before the separators below it. For every separator \(t\), whose current subpath is split into equal sets \(A,B\), let the colour corresponding to \(t\) be a perfect matching between \(A\) and \(B\) containing \(t\).

Every vertex pair is eligible at only one node of the recursive decomposition, so the resulting graph is simple. Every colour class is a matching, and (12) holds. Hence the colouring is proper and has no rainbow cycle. There are \(h\) recursion levels, each contributing \(n/2\) edges, so
\[
|E(G)|=\frac n2h=\frac n2\log_2n.
\]
The graph uses \(n-1\) colours and is \(\log_2n\)-regular. Thus Theorem 2 is exact for powers of two.

## 4. Commuting colour matchings

A different special case covers cube-like colourings even when the number of colours is far below \(n-c(G)\).

For each colour \(i\), let \(\sigma_i\) be the involution of \(V(G)\) that swaps the endpoints of every edge in \(M_i\) and fixes all other vertices.

### Theorem 3

If the involutions \(\sigma_1,\dots,\sigma_k\) commute pairwise and \(G\) has no rainbow cycle, then
\[
\Delta(G)\le\lfloor\log_2 n\rfloor.
\tag{14}
\]

#### Proof

Fix \(v\), and let \(C(v)\) be the set of colours incident with \(v\). Properness gives \(|C(v)|=d(v)\).

For \(S\subseteq C(v)\), define
\[
\phi(S)=\prod_{i\in S}\sigma_i(v),
\]
which is unambiguous because the involutions commute. Suppose \(\phi(S)=\phi(T)\). Then
\[
\prod_{i\in S\triangle T}\sigma_i(v)=v.
\tag{15}
\]
If \(S\triangle T\ne\varnothing\), apply these distinct involutions one at a time. Every step moves along an edge: if a colour \(i\in C(v)\) fixed an intermediate vertex \(\tau(v)\), commutativity would imply
\[
\sigma_i(v)=\tau^{-1}\sigma_i\tau(v)=v,
\]
contrary to \(i\in C(v)\). Thus (15) gives a nonempty closed walk whose edge colours are all distinct. A shortest closed subwalk is a rainbow cycle, contradiction.

Hence \(\phi\) is injective, so
\[
2^{d(v)}\le n.
\]
This proves (14). \(\square\)

More generally, if the colours can be partitioned into \(q\) classes such that the involutions commute pairwise within each class, then the same argument at each vertex gives
\[
\Delta(G)\le q\log_2 n.
\tag{16}
\]
Thus a bounded number of commuting batches also eliminates the \(\log\log n\) factor.

## 5. An explicit logarithmic lower construction

Let the parts of \(K_{3,3}\) both be indexed by \(\mathbb Z_3\), and colour the edge \(ij\) by \(i+j\pmod 3\). This is a proper \(3\)-edge-colouring. Since \(K_{3,3}\) is bipartite, every cycle has length at least \(4\), while only three colours are available; hence there is no rainbow cycle.

Cartesian products preserve this property when colours are tagged by their coordinate. Indeed, a rainbow cycle in a Cartesian product projects in each coordinate to a closed walk with distinct colours. Any nonempty such closed walk contains a rainbow cycle in the factor.

Consequently, the \(t\)-fold Cartesian power of this coloured \(K_{3,3}\) has
\[
N=6^t,\qquad \overline d=3t
   =\frac{3}{\log_2 6}\log_2N
   \approx 1.1606\log_2N,
\]
and has no rainbow cycle. This is an elementary \(\Omega(\log n)\) lower bound, slightly stronger in its constant than the coordinate-coloured hypercube.

## 6. Remaining gap

The results above do not settle the catalogued question.

- If the number of colours is \(O(\log n)\), the desired bound follows trivially from \(\overline d\le k\).
- If the number of colours is maximal, \(k=n-c(G)\), Theorem 2 gives the exact bound \(\overline d\le\log_2n\).
- Theorem 1 covers the broader class admitting a common binary complement.
- Theorem 3 covers commuting, cube-like systems.

The unresolved regime consists of noncommuting colour matchings with substantial rank deficiency
\[
n-c(G)-k>0
\]
and no common binary complement. The \(K_{3,3}\) example already shows that such a complement cannot simply be assumed. No argument above bounds that general regime by \(O(\log n)\), and no construction here yields \(\omega(\log n)\). Thus the necessity of the \(\log\log n\) factor remains open.