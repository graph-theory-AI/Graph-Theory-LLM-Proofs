```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For q=r-m>=2, I characterize exactly when the minimum is t+2q or t+2q+1, for both simple and parallel-edge hypergraphs.",
  "would_publish": false,
  "caveats": "The general minimum is not determined; novelty relative to the source paper and covering-design literature is unchecked."
}
```

# A sharp partial solution: the first two possible edge counts

I use the literal containment condition \(E\subseteq M\), with nonempty edges and no uniformity restriction.

Let \(h_{\mathrm s}(r,m,t)\) be the minimum for **simple** intersecting hypergraphs, and let \(h_{\mathrm{multi}}(r,m,t)\) allow parallel edges, counted with multiplicity. A minimum is \(+\infty\) if no such hypergraph exists. Throughout, \(1\le m\le r\) and \(t\ge1\).

The previous attempt’s pairing lower bound is valid; I verify it below. The main additional result is an exact characterization of the next possible edge count. All constructions used for this result are simple, so the ambiguity about parallel edges does not affect it.

## 1. Main result

Put
\[
q=r-m,\qquad L=t+2q,
\]
and define
\[
R_0(L)=\binom L2
\]
and
\[
R_1(L)=
\begin{cases}
6,&L=5,\\[2mm]
\displaystyle\binom{L+1}{2}-14,&6\le L\le9,\\[2mm]
\displaystyle\binom L2-4,&L\ge10.
\end{cases}
\]

### Theorem 1

Suppose \(q\ge2\). For either \(h=h_{\mathrm s}\) or \(h=h_{\mathrm{multi}}\):

1. \(h(r,r-q,t)\ge L\).
2. \(h(r,r-q,t)=L\) if and only if \(r\ge R_0(L)\).
3. \(h(r,r-q,t)=L+1\) if and only if
   \[
   R_1(L)\le r<R_0(L).
   \]
4. If \(r<R_1(L)\), then \(h(r,r-q,t)\ge L+2\), with \(+\infty\) allowed.

The first few thresholds are
\[
\begin{array}{c|r|r}
L&R_0(L)&R_1(L)\\ \hline
5&10&6\\
6&15&7\\
7&21&14\\
8&28&22\\
9&36&31\\
10&45&41
\end{array}
\]

In particular, for every \(L\ge10\), the next-to-minimum case occupies exactly a **four-vertex window**:
\[
h(r,r-q,t)=L+1
\quad\Longleftrightarrow\quad
\binom L2-4\le r<\binom L2.
\]

The proof reduces the next-to-minimum case to a sharp extremal statement about pairwise-intersecting families of triples.

---

## 2. Pairing bounds, including a useful local strengthening

Index the edges as \(E_1,\ldots,E_N\), allowing repetitions when appropriate. For \(A\subseteq V\), write
\[
U(A)=\{i:E_i\cap A\ne\varnothing\}.
\]

The required condition is equivalently
\[
|U(Q)|\le N-t
\qquad\text{for every }Q\in\binom Vq. \tag{2.1}
\]

### Lemma 2

Every feasible hypergraph satisfies
\[
N\ge t+2q. \tag{2.2}
\]
More generally, if \(|A|=a\le q\), then
\[
|U(A)|\le N-t-2(q-a). \tag{2.3}
\]

#### Proof

First consider an intersecting family of \(N\) nonempty edges for which every \(k\)-set avoids at least \(t\) edges.

Any collection of at most \(2k\) edges can be met by at most \(k\) vertices: pair the edges and choose an intersection point from each pair, with one additional point for an unpaired edge. Consequently, \(N\le2k\) is impossible. Having established \(N\ge2k+1\), select \(2k\) edges and meet them with at most \(k\) vertices. Enlarge this set to a \(k\)-set. At least \(t\) other edges must avoid it, so
\[
N\ge2k+t.
\]
For \(k=0\), the corresponding assertion is simply \(N\ge t\).

Apply this first with \(k=q\), obtaining (2.2).

For (2.3), retain only the edges avoiding \(A\). They form an intersecting family on \(V\setminus A\), and every \((q-a)\)-set in \(V\setminus A\) avoids at least \(t\) of them, by (2.1). Hence
\[
N-|U(A)|\ge t+2(q-a).
\]
∎

### The minimum level \(N=L\)

If \(N=L=t+2q\), Lemma 2 with \(a=1\) gives
\[
d(v)\le2
\qquad(v\in V).
\]
Every pair of indexed edges must intersect, while a vertex of degree at most two witnesses at most one pair. Therefore
\[
r\ge\binom L2. \tag{2.4}
\]

Conversely, use one vertex \(x_{ij}\) for each pair \(1\le i<j\le L\), and set
\[
E_i=\{x_{ij}:j\ne i\}.
\]
These are distinct, pairwise-intersecting edges. Every \(q\)-set of vertices meets at most \(2q\) edges, leaving at least \(L-2q=t\) edges disjoint from it. Additional isolated vertices may be added.

This verifies the previous attempt’s equality characterization, under both conventions.

---

## 3. The next level is an intersecting-triple covering problem

Now suppose
\[
N=L+1=t+2q+1,\qquad q\ge2.
\]
For each ground vertex \(v\), define its incidence block
\[
B_v=\{i\in[N]:v\in E_i\}.
\]

Pairwise intersection of the original edges says exactly that these blocks cover every pair of \([N]\):
\[
\binom{[N]}2\subseteq\bigcup_{v\in V}\binom{B_v}{2}. \tag{3.1}
\]

Lemma 2 gives
\[
|B_v|\le3
\]
and, for distinct ground vertices \(v,w\),
\[
|B_v\cup B_w|\le5.
\]
Thus the blocks of size three form a pairwise-intersecting triple system.

The converse also holds:

> If blocks of size at most three cover every pair of \([N]\), and their three-element blocks are pairwise intersecting, then they yield a valid indexed hypergraph with \(N=t+2q+1\) edges.

Indeed, consider any \(q\) blocks. If none has size three, their union has size at most \(2q\). Otherwise, if \(k\) of them have size three, order those first. The first contributes three elements, and each subsequent triple contributes at most two because it intersects the first. The remaining blocks contribute at most two each. Hence their union has size at most
\[
3+2(k-1)+2(q-k)=2q+1=N-t. \tag{3.2}
\]

It remains to minimize the number of blocks in such a pair covering.

For a simple triple family \(\mathcal F\), let
\[
\partial_2\mathcal F
=\{P:|P|=2,\ P\subseteq F\text{ for some }F\in\mathcal F\},
\]
and define
\[
\Phi(\mathcal F)=|\partial_2\mathcal F|-|\mathcal F|.
\]

If \(\mathcal F\) is the support of the three-element incidence blocks, every pair outside \(\partial_2\mathcal F\) requires its own two-element block. Thus
\[
r\ge |\mathcal F|+\binom N2-|\partial_2\mathcal F|
=\binom N2-\Phi(\mathcal F). \tag{3.3}
\]

Conversely, take one block for each member of \(\mathcal F\), together with one two-element block for every pair outside its shadow. Equality holds in (3.3).

The key extremal quantity is therefore
\[
\max_{\mathcal F\text{ intersecting}}\Phi(\mathcal F).
\]

---

## 4. A structural lemma for intersecting triples

Write \(\tau(\mathcal F)\) for the transversal number of \(\mathcal F\).

### Lemma 3

An intersecting family of triples with transversal number three uses at most seven vertices.

#### Proof

Choose \(A=\{a_1,a_2,a_3\}\in\mathcal F\). Since no pair is a transversal, for each \(i\) there is an edge
\[
F_i=\{a_i\}\cup P_i
\]
with
\[
F_i\cap A=\{a_i\}.
\]
Here \(P_i\) is a two-element set outside \(A\).

The three pairs \(P_1,P_2,P_3\) are pairwise intersecting. They therefore either form a triangle or have a common vertex.

Let
\[
\mathcal C=\{A,F_1,F_2,F_3\},
\qquad
S=\bigcup_{C\in\mathcal C}C.
\]
The four core edges have no common vertex. Let \(G\) be the graph on \(S\) whose edges are the two-element transversals of \(\mathcal C\).

Consider a vertex \(z\in V(\mathcal F)\setminus S\). Any edge containing \(z\) must have its other two vertices in \(S\): otherwise, at most one vertex could meet all four core edges, which is impossible. Consequently, such edges have the form
\[
\{z\}\cup p,\qquad p\in E(G).
\]
Let \(G_z\subseteq G\) consist of these pairs.

Two facts will be used:

- \(G_z\) contains two disjoint edges. Indeed, take \(p\in G_z\). Since \(p\) is not a transversal of \(\mathcal F\), some edge avoids \(p\). It must intersect \(\{z\}\cup p\), so it contains \(z\), and its other two vertices form an edge of \(G_z\) disjoint from \(p\).
- For distinct outside vertices \(z,w\), the graphs \(G_z,G_w\) are cross-intersecting: every edge of one meets every edge of the other.

We now check all possible patterns of \(P_1,P_2,P_3\).

**Case 1: the \(P_i\) form a triangle.**  
Here \(|S|=6\), and \(G\) is a matching of three edges. There cannot be two cross-intersecting subgraphs of this matching each containing two edges. Hence at most one vertex lies outside \(S\).

**Case 2: \(P_i=\{x,b_i\}\), with the \(b_i\) distinct.**  
Here \(|S|=7\), and
\[
E(G)=\{xa_1,xa_2,xa_3\}.
\]
This graph has no two disjoint edges, so there are no outside vertices.

**Case 3: \(P_i=\{x,b_i\}\), with \(b_1=b_2=b\ne b_3\).**  
Here \(|S|=6\), and
\[
E(G)=\{xa_1,xa_2,xa_3,ba_3\}.
\]
Every matching of size two in \(G\) contains \(ba_3\) and one of \(xa_1,xa_2\). Two subgraphs each containing such a matching cannot be cross-intersecting. Hence there is at most one outside vertex.

**Case 4: \(P_i=\{x,b\}\) for all \(i\).**  
Here \(|S|=5\), and \(G=K_{2,3}\), with parts \(\{x,b\}\) and \(A\).

There are at most two pairwise cross-intersecting subgraphs of \(K_{2,3}\), each containing a matching of size two. To see this, suppose one contains \(xa_1,ba_2\). Every edge of a second must then be one of
\[
xa_2,\quad ba_1;
\]
to contain a matching of size two, it must contain both. No edge of \(K_{2,3}\) meets all four displayed matching edges, so a third subgraph is impossible.

Thus there are at most two outside vertices.

In every case,
\[
|V(\mathcal F)|\le7.
\]
∎

---

## 5. The exact shadow-minus-size bound

### Lemma 4

For intersecting triple families on an \(n\)-element set, \(n\ge6\),
\[
\max \Phi(\mathcal F)=
\begin{cases}
9,&n=6,\\[1mm]
\max\{14,n+3\},&n\ge7.
\end{cases} \tag{5.1}
\]

#### Upper bound for \(n=6\)

Suppose \(\Phi(\mathcal F)\ge10\), and put \(f=|\mathcal F|\). Since
\[
|\partial_2\mathcal F|\le \min\{3f,15\},
\]
we must have \(f=5\) and \(|\partial_2\mathcal F|=15\). Thus every pair occurs in exactly one triple.

At any vertex, its five incident pairs would then be partitioned into groups of two by the triples containing it. This is impossible. Hence
\[
\Phi(\mathcal F)\le9.
\]

#### Upper bound for \(n\ge7\)

The empty family is harmless. For a nonempty intersecting triple family,
\[
1\le\tau(\mathcal F)\le3.
\]

**Case \(\tau=1\).**  
All triples contain some vertex \(x\). They correspond to the edges of a graph \(A\) on the remaining vertices. Their shadow consists of \(E(A)\) and the pairs \(xv\) for \(v\in V(A)\). Therefore
\[
\Phi(\mathcal F)=|V(A)|\le n-1. \tag{5.2}
\]

**Case \(\tau=2\).**  
Choose a transversal \(\{x,y\}\), and put \(W=V\setminus\{x,y\}\). Write the triples as
\[
\{x\}\cup e\quad(e\in A),\qquad
\{y\}\cup e\quad(e\in B),\qquad
\{x,y,c\}\quad(c\in C),
\]
where \(A,B\) are graphs on \(W\) and \(C\subseteq W\). Every edge of \(A\) meets every edge of \(B\).

Let \(S=V(A)\) and \(T=V(B)\). Counting the shadow gives
\[
\Phi(\mathcal F)
=
|S\cup C|+|T\cup C|-|C|
+\mathbf 1_{C\ne\varnothing}
-|A\cap B|.
\]
Using
\[
|S\cup C|+|T\cup C|-|C|
\le |W|+|S\cap T|,
\]
we obtain
\[
\Phi(\mathcal F)
\le n-1+|S\cap T|-|A\cap B|. \tag{5.3}
\]

For cross-intersecting graphs \(A,B\),
\[
|S\cap T|-|A\cap B|\le4. \tag{5.4}
\]
If either graph uses at most four vertices, this is immediate. Otherwise, \(A\) cannot contain two disjoint edges, since every edge of \(B\) would then lie within their four endpoints. Thus \(A\) is an intersecting graph using more than four vertices, and hence a star with at least four leaves. Every edge of \(B\) must contain its centre. The two graphs are stars with the same centre, and in this case the left side of (5.4) equals one.

Combining (5.3) and (5.4),
\[
\Phi(\mathcal F)\le n+3. \tag{5.5}
\]

**Case \(\tau=3\).**  
By Lemma 3, the family uses at most seven vertices. Thus, with \(f=|\mathcal F|\),
\[
\Phi(\mathcal F)\le\min\{2f,21-f\}\le14. \tag{5.6}
\]

This proves the claimed upper bound.

#### Constructions attaining the bound

**On six vertices**, take
\[
\mathcal F_6=
\{123,124,345,346,156,256\}.
\]
These triples are pairwise intersecting and cover every pair. The pairs \(12,34,56\) occur twice, and all other pairs once. Hence
\[
\Phi(\mathcal F_6)=15-6=9.
\]

**For the value \(14\)**, use the seven triples
\[
\mathcal L=
\{123,145,167,246,257,347,356\}.
\]
They are pairwise intersecting and cover every pair on their seven vertices exactly once. Therefore
\[
\Phi(\mathcal L)=21-7=14.
\]
This family can be embedded in any ambient set of size \(n\ge7\).

**For the value \(n+3\)**, use six distinguished vertices
\[
x,y,a,b,c,d
\]
and a nonempty set \(Z\) of \(n-6\) further vertices. Take
\[
\mathcal T_n=
\{xab,xcd,yac,ybd\}
\cup
\{xyz:z\in Z\}.
\]
The family is pairwise intersecting.

The first four triples cover twelve distinct pairs. The remaining triples add \(xy\) and the \(2|Z|\) pairs \(xz,yz\). Hence
\[
|\partial_2\mathcal T_n|=12+1+2(n-6)=2n+1,
\]
while
\[
|\mathcal T_n|=4+(n-6)=n-2.
\]
Consequently,
\[
\Phi(\mathcal T_n)=n+3.
\]

This proves (5.1). ∎

---

## 6. Completion of Theorem 1

Set \(n=L+1\). By the incidence-block reduction and Lemma 4, the smallest possible number of ground vertices for a hypergraph with exactly \(n\) indexed edges is
\[
\binom n2-
\begin{cases}
9,&n=6,\\
\max\{14,n+3\},&n\ge7.
\end{cases} \tag{6.1}
\]
This is precisely \(R_1(L)\).

For sufficiency, take a triple family attaining Lemma 4 and add a two-element block for every pair outside its shadow. Regard these blocks as ground vertices, and define
\[
E_i=\{B:i\in B\}\qquad(i\in[n]).
\]
Every pair of indices is covered, so the edges \(E_i\) intersect. Equation (3.2) verifies the required condition on \(q\)-sets.

These constructions have distinct edges:

- For \(\mathcal F_6\), numbering its six displayed blocks in order, the incidence columns are
  \[
  125,\ 126,\ 134,\ 234,\ 356,\ 456.
  \]
- For \(\mathcal L\), the seven original indices have distinct nonempty line-incidence patterns. Additional indices have no line incidences and are distinguished by the added pair blocks.
- For \(\mathcal T_n\), the six distinguished indices have six distinct incidence patterns on the first four triples. Every \(z\in Z\) has zero incidence on those four and is distinguished from the other outside indices by its block \(xyz\).

Thus the resulting hypergraphs are simple. Padding with isolated vertices gives the construction for every \(r\ge R_1(L)\).

Section 2 already characterized the level \(L\). Since \(R_1(L)<R_0(L)\), these facts prove all parts of Theorem 1.

---

## 7. Complete small-parameter consequences

The result gives some complete families, not only threshold statements.

### 7.1. Every \((r-2)\)-set must contain an edge

For both conventions, and \(r\ge3\),
\[
h(r,r-2,1)=
\begin{cases}
\infty,&r\le4,\\
10,&r=5,\\
6,&6\le r\le9,\\
5,&r\ge10.
\end{cases} \tag{7.1}
\]

Here is the boundary argument needed in addition to Theorem 1.

In any feasible hypergraph, every edge has size at least \(q+1\). Otherwise an \(m\)-set could be chosen disjoint from that edge, and an edge contained in that \(m\)-set would contradict intersection.

For \(r=5,q=2,m=3\), every edge contributing to the condition must therefore have size three. Every three-set must itself be an edge, requiring all ten triples. They are pairwise intersecting.

For \(r\le4\), there are two disjoint \((r-2)\)-sets, making feasibility impossible.

### 7.2. Every \((r-2)\)-set must contain two edges

For parallel edges,
\[
h_{\mathrm{multi}}(r,r-2,2)=
\begin{cases}
\infty,&r\le4,\\
20,&r=5,\\
10,&r=6,\\
7,&7\le r\le14,\\
6,&r\ge15.
\end{cases} \tag{7.2}
\]
For simple hypergraphs the same formula holds except that the value at \(r=5\) is \(+\infty\).

Only \(r=6\) needs an additional construction and lower bound. Every edge has size at least three, so its complement contains at most three pairs. Every pair must lie in at least two complements. Thus
\[
3N\ge2\binom62=30,
\]
giving \(N\ge10\).

For equality, take the ten complementary triples
\[
\begin{split}
\mathcal D=\{&
123,124,345,346,156,256,\\
&135,146,236,245\}.
\end{split}
\]
Every pair occurs exactly twice, and no two members are complementary. Therefore
\[
\{[6]\setminus D:D\in\mathcal D\}
\]
is a simple intersecting hypergraph with ten edges satisfying the required condition.

At \(r=5,m=3\), two copies of every triple are necessary in the parallel-edge version; in the simple version, each three-set can contain at most one admissible edge.

### 7.3. An example with larger codimension

Taking \(q=3,t=1\), Theorem 1 gives
\[
h(r,r-3,1)=
\begin{cases}
7,&r\ge21,\\
8,&14\le r\le20.
\end{cases}
\]
For \(r<14\), it proves \(h(r,r-3,1)\ge9\), but does not generally determine the answer.

---

## 8. What remains unresolved

The general minimum is not determined here. The proof completely characterizes only the two lowest possible levels
\[
t+2(r-m),\qquad t+2(r-m)+1
\]
when \(r-m\ge2\), together with the complete families in Section 7.

At the next level, \(N=t+2q+2\), incidence blocks can have size four. The local conditions include
\[
|B_v|\le4,\qquad |B_v\cup B_w|\le6,
\]
and further restrictions on unions of larger collections. The sharp intersecting-triple optimization above no longer suffices. Even \(h(r,r-2,t)\) for arbitrary \(t\) is not determined by this argument.

All results stated here have self-contained proofs and explicit constructions. I have not checked whether these particular threshold results already occur in the source paper or the covering-design literature.