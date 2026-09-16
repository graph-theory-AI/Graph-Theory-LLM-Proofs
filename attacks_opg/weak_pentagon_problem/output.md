```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured conclusion for triangle-free cubic graphs that become bipartite after deleting at most three edges.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved, and novelty of this special case has not been checked."
}
```

## A proved special case

For a graph \(G\), define its **edge-bipartization number**
\[
\beta(G)=\min\{|D|:D\subseteq E(G),\ G-D\text{ is bipartite}\}.
\]

I establish the following partial result, using an explicit construction.

**Theorem.** Let \(G\) be a finite simple triangle-free cubic graph. If
\[
\beta(G)\le 3,
\]
then \(G\) admits a homomorphism to the Clebsch graph. Consequently, its edges can be colored with five colors so that the complement of every color class is bipartite.

The construction also gives an additional sufficient condition with no bound on \(\beta(G)\), stated below. It does not settle the full conjecture.

## 1. A useful model of the Clebsch graph

Work in \(\mathbb F_2^5\). Let \(\mathbf 1=(1,1,1,1,1)\), and put
\[
s_i=\mathbf 1+e_i\qquad(1\le i\le5).
\]
Thus \(s_i\) has a zero in coordinate \(i\) and ones elsewhere. In particular,
\[
s_1+s_2+s_3+s_4+s_5=0.
\]

Let \(\mathcal C\) have as vertices the sixteen even-weight vectors, with
\[
x\sim y\quad\Longleftrightarrow\quad x+y\in\{s_1,\ldots,s_5\}.
\]
This is \(PQ_4\), the Clebsch graph: each antipodal pair in \(Q_5\) has a unique even-weight representative, and flipping coordinate \(i\), followed by taking that representative, adds \(s_i\).

Here is also a direct verification of the required edge-coloring consequence. Given a homomorphism \(f:G\to\mathcal C\), color \(uv\) with the unique \(i\) satisfying
\[
f(u)+f(v)=s_i.
\]
For any fixed \(j\), every edge not colored \(j\) has endpoints whose \(j\)-th coordinates differ. Hence
\[
v\longmapsto f(v)_j
\]
is a bipartition of the complement of color class \(j\).

It therefore suffices to construct \(f\).

## 2. Maximum-cut structure with at most three defects

The number \(\beta(G)\) is also the minimum possible number of edges lying within the parts of a vertex bipartition. Indeed, deleting those edges makes the graph bipartite; conversely, a bipartition of \(G-D\) leaves at most \(|D|\) edges within its parts.

Choose a maximum cut with parts \(A,B\), and write
\[
M=E(G[A])\cup E(G[B]).
\]
Then \(|M|=\beta(G)\).

Because \(G\) is cubic, \(M\) is a matching. Otherwise, a vertex incident with at least two edges of \(M\) could be moved to the other part, increasing the cut.

Put
\[
a=|E(G[A])|,\qquad b=|E(G[B])|.
\]
Counting degrees on the two sides gives
\[
3|A|=2a+|\delta(A)|,\qquad
3|B|=2b+|\delta(A)|,
\]
and therefore
\[
3(|A|-|B|)=2(a-b).
\tag{1}
\]
In particular, \(a-b\) is divisible by three. Thus:

- \(\beta(G)=1\) is impossible;
- if \(\beta(G)=2\), then \(a=b=1\);
- if \(\beta(G)=3\), all three edges of \(M\) lie in the same part.

The case \(\beta(G)=0\) is immediate, since a bipartite graph maps to any edge of \(\mathcal C\). We handle the other two possibilities separately.

## 3. Two defects: an explicit eight-vertex construction

Suppose
\[
M=\{aa',bb'\},\qquad a,a'\in A,\quad b,b'\in B.
\]
Let
\[
D=G-M,
\]
which is bipartite with parts \(A,B\).

Triangle-freeness implies that the edges between \(\{a,a'\}\) and \(\{b,b'\}\) form a matching. After interchanging \(b,b'\) if necessary, we may therefore assume
\[
ab',\ a'b\notin E(G).
\]

Set
\[
L=\{a,b\},\qquad R=\{a',b'\}.
\]
Then
\[
\operatorname{dist}_D(L,R)\ge3.
\tag{2}
\]
To see this, \(a,a'\) lie in the same bipartition class, and a length-two \(a\)-\(a'\) path would form a triangle with \(aa'\). Thus their distance in \(D\) is at least four, or infinite. The same holds for \(b,b'\). The other two pairs are in opposite classes and are nonadjacent, so their distances are at least three.

Define
\[
h(v)=\min\{3,\operatorname{dist}_D(v,L)\},
\]
taking \(h(v)=3\) in components not meeting \(L\). Every edge \(uv\in E(D)\) satisfies
\[
|h(u)-h(v)|\le1.
\]
Moreover, \(h=0\) on \(L\) and \(h=3\) on \(R\).

Let \(p(v)=0\) on \(A\) and \(p(v)=1\) on \(B\), and put
\[
q(v)=p(v)+h(v)\pmod2.
\]
Define
\[
f(v)=q(v)s_4+\sum_{i=1}^{h(v)}s_i,
\tag{3}
\]
where an empty sum is zero.

We check every type of edge.

- If \(uv\in E(D)\) and \(h(u)=h(v)\), then \(p(u)\ne p(v)\), so
  \[
  f(u)+f(v)=s_4.
  \]

- If \(uv\in E(D)\) and the heights differ by one, then \(q(u)=q(v)\). Consequently,
  \[
  f(u)+f(v)=s_j
  \]
  for the appropriate \(j\in\{1,2,3\}\).

- Each edge of \(M\) joins a height-zero vertex to a height-three vertex in the same part. Its endpoint labels consequently differ by
  \[
  s_4+s_1+s_2+s_3=s_5.
  \]

Thus (3) is a homomorphism to \(\mathcal C\).

In fact, the eight possible labels in (3) support two four-vertex paths, their rungs, and the two crossed end-edges: the usual eight-vertex Wagner graph. So this case admits a smaller target than the full Clebsch graph.

## 4. Three defects: a small auxiliary coloring problem

Now suppose \(\beta(G)=3\). By (1), after exchanging the parts, we have
\[
G[B]\text{ edgeless},\qquad E(G[A])=M,
\]
where \(M\) is a three-edge matching.

For each endpoint \(u\) of \(M\), let
\[
N_u=N_G(u)\cap B.
\]
Each \(N_u\) has exactly two vertices. If \(uv\in M\), triangle-freeness gives
\[
N_u\cap N_v=\varnothing.
\]

Construct a simple auxiliary graph \(F\) on vertex set \(B\). For every \(uv\in M\), add all four edges between \(N_u\) and \(N_v\). Thus
\[
|E(F)|\le 12.
\]

The graph \(F\) is 4-degenerate. Indeed, a subgraph of minimum degree at least five would have at least six vertices and therefore at least fifteen edges. Hence \(F\) has a proper coloring
\[
c:B\longrightarrow[5].
\]

For \(uv\in M\), the two sets
\[
c(N_u),\qquad c(N_v)
\]
are disjoint, and each has size at most two. Choose disjoint two-element sets
\[
P_u,P_v\subseteq[5]
\]
such that
\[
c(N_u)\subseteq P_u,\qquad c(N_v)\subseteq P_v.
\tag{4}
\]
There are enough colors to do this: enlarging the two sets requires a total of four distinct colors, from a palette of five. Make these choices independently for the three edges of \(M\).

Identify subsets of \([5]\) with their characteristic vectors, and define
\[
f(x)=
\begin{cases}
s_{c(x)},&x\in B,\\[2mm]
0,&x\in A\setminus V(M),\\[2mm]
\mathbf 1_{P_x},&x\in V(M).
\end{cases}
\tag{5}
\]
All these vectors have even weight.

Again, every edge can be checked explicitly.

- If \(xy\) joins \(x\in A\setminus V(M)\) to \(y\in B\), its labels differ by \(s_{c(y)}\).

- Suppose \(x\in V(M)\), \(y\in B\), and \(xy\in E(G)\). By (4), write
  \[
  P_x=\{c(y),k\}.
  \]
  Then
  \[
  f(x)+f(y)
  =(e_{c(y)}+e_k)+(\mathbf1+e_{c(y)})
  =s_k.
  \]

- If \(uv\in M\), the sets \(P_u,P_v\) are disjoint and have size two. Their characteristic vectors differ in exactly four coordinates, so their difference is some \(s_i\).

There are no other edges. Therefore (5) is a homomorphism \(G\to\mathcal C\), completing the theorem. \(\square\)

## 5. A further sufficient condition

The auxiliary construction has a useful extension beyond bounded edge-bipartization.

**Corollary.** Suppose a triangle-free cubic graph \(G\) has a partition \(A,B\) such that:

1. \(B\) is independent;
2. \(G[A]\) consists of a matching \(M\) and isolated vertices;
3. every vertex of \(B\) has at most two neighbors in \(V(M)\).

Then \(G\) admits the conjectured five-coloring.

**Proof.** Form the same auxiliary graph \(F\). Each neighbor \(u\in V(M)\) of a vertex \(x\in B\) contributes at most two neighbors of \(x\) in \(F\), namely the two \(B\)-neighbors of the partner of \(u\) in \(M\). Thus
\[
\Delta(F)\le4.
\]
Greedy coloring gives a proper five-coloring of \(F\), and construction (4)–(5) applies unchanged. \(\square\)

More generally, the construction works whenever this explicitly defined auxiliary graph is five-colorable; no assertion that this always happens is needed for either proved result.

## 6. Algorithmic content and the remaining gap

The theorem is constructive. Given the relevant maximum cut, both homomorphism constructions take linear time.

One can also recognize and handle the case \(\beta(G)\le3\) without an unrestricted maximum-cut algorithm:

1. Enumerate \(D\subseteq E(G)\) in increasing size, up to size three.
2. Test the parity constraints
   \[
   p(u)+p(v)=
   \begin{cases}
   0,&uv\in D,\\
   1,&uv\notin D,
   \end{cases}
   \qquad\text{over }\mathbb F_2.
   \]
3. The first feasible \(D\) is a minimum cut-complement. Apply the appropriate construction above.

Each parity test is a graph traversal, giving total time
\[
O\!\left(m^3(n+m)\right).
\]
This is an algorithm specification, not a claim of computational experiments.

For arbitrary graphs with \(\beta(G)\ge4\), the argument gives no general conclusion. Already at \(\beta(G)=4\), equation (1) permits—and forces—a maximum-cut complement with two edges in each part. The one-sided auxiliary construction no longer applies, and the height construction above only handles one defect edge in each part.

Thus any counterexample to the original conjecture must have edge-bipartization number at least four, but its existence or nonexistence remains unresolved here. No novelty claim or improvement to the high-girth projective-cube question is asserted.