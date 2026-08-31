```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem is exactly a Max-Cut problem on a circle conflict graph; an elementary coloring argument strictly refines the Edwards bound, is sharp for several infinite families, and determines the exact worst-case value for every k at most 49.",
  "would_publish": false,
  "caveats": "The first value not settled here is k=50, and I have not checked whether the elementary Max-Cut refinement already appears in the literature."
}
```

# 1. Formulation as a circle-graph Max-Cut problem

Fix the order \(\prec\) of \(V(G)\) along the spine. Two independent edges \(uv,xy\) are called a **conflicting pair** if their four endpoints alternate in \(\prec\). Let \(X=X_\prec(G)\) be the graph whose vertices are the edges of \(G\), with two vertices adjacent precisely when the corresponding edges conflict.

Thus \(X\) is a circle graph. Write
\[
m=|E(X)|,\qquad \operatorname{mc}(X)=\max\{|E_X(A,B)|:(A,B)\text{ is a bipartition of }V(X)\}.
\]

A partition \(E(G)=A\cup B\) assigns the edges of \(G\) to the two pages. A conflicting pair is forced to cross if its two edges are assigned to the same page, while all same-page conflicting pairs can simultaneously be drawn with exactly one crossing each. Consequently,
\[
\boxed{\operatorname{cr}^{\,\prec}_2(G)=m-\operatorname{mc}(X).} \tag{1}
\]

For a standard good one-page drawing, \(m\) is exactly its number of crossings. For an arbitrary drawing with \(k\) crossings, one first redraws canonically in the page; then \(m\le k\), since every alternating pair must have crossed at least once.

Conversely, every circle graph \(X\) is realized in this way by taking \(G\) to be a matching, one edge for each chord. Hence the sharp universal function is
\[
\Psi(k)=
\max_{\substack{X\text{ a circle graph}\\ |E(X)|=k}}
\bigl(k-\operatorname{mc}(X)\bigr).
\]

# 2. A universal bound improving the Edwards bound

Put
\[
T_r=\binom r2,\qquad Q_r=\left\lfloor\frac{r^2}{4}\right\rfloor.
\]
For \(k>0\), let \(r=r(k)\) be the unique integer satisfying
\[
T_r\le k<T_{r+1}.
\]

## Theorem 1

For every graph \(H\) with \(k\) edges,
\[
\operatorname{mc}(H)\ge
\left\lceil \frac{Q_r}{T_r}\,k\right\rceil. \tag{2}
\]
Consequently,
\[
\boxed{\Psi(k)\le
k-\left\lceil \frac{Q_r}{T_r}\,k\right\rceil.} \tag{3}
\]

If \(r\in\{2a-1,2a\}\), then
\[
\frac{Q_r}{T_r}=\frac{a}{2a-1},
\]
so (3) becomes
\[
\boxed{\Psi(k)\le
\left\lfloor\frac{a-1}{2a-1}\,k\right\rfloor.} \tag{4}
\]

### Proof

Because \(k<T_{r+1}\), every subgraph of \(H\) has a vertex of degree at most \(r-1\). Indeed, a subgraph of minimum degree at least \(r\) would have at least \(r+1\) vertices and hence at least
\[
\frac{r(r+1)}2=T_{r+1}
\]
edges. Thus \(H\) is \((r-1)\)-degenerate and therefore \(r\)-colorable.

Fix a proper coloring with color set \([r]\). Choose uniformly a set of \(\lfloor r/2\rfloor\) colors and put their color classes on one side of a cut. For any edge, its endpoint colors are distinct, and the probability that they are separated is
\[
\frac{\lfloor r^2/4\rfloor}{\binom r2}
=\frac{Q_r}{T_r}.
\]
The expected cut size is therefore \(kQ_r/T_r\), so some cut has at least its ceiling. Equation (3) follows from (1). ∎

## Comparison with the Edwards estimate

The Edwards estimate quoted in the source paper is
\[
\operatorname{mc}(H)\ge
\frac{k}{2}+\frac{\sqrt{8k+1}-1}{8}. \tag{5}
\]

If \(r\in\{2a-1,2a\}\), the surplus in (2) over \(k/2\) is
\[
\frac{k}{2(2a-1)}.
\]
In the corresponding block \(k\ge T_{2a-1}\), one has
\[
\frac{k}{2(2a-1)}
\ge \frac{\sqrt{8k+1}-1}{8}. \tag{6}
\]
Indeed, equality holds at \(k=T_{2a-1}\), and thereafter
\[
\frac{d}{dk}\left(\frac{4k}{2a-1}+1\right)
=\frac4{2a-1}
>
\frac4{\sqrt{8k+1}}.
\]
Thus (2) uniformly dominates the Edwards bound. It is sometimes strictly stronger even after integer rounding. For example:
\[
\begin{array}{c|c|c}
k & \text{Edwards crossing bound} & \text{bound (4)}\\ \hline
8&3&2\\
17&7&6\\
19&8&7
\end{array}
\]

The bound is constructive: greedily find the \(r\)-coloring, then use conditional expectation to choose \(\lfloor r/2\rfloor\) color classes whose cut has the required size.

# 3. Sharpness and exact infinite families

Complete graphs are circle graphs: \(K_r\) is represented by \(r\) pairwise intersecting chords. Therefore
\[
\boxed{\Psi(T_r)=T_r-Q_r.} \tag{7}
\]
In particular, the asymptotic form
\[
\Psi(k)\le \frac{k}{2}-\sqrt{\frac{k}{8}}+O(1)
\]
has the best possible coefficient of \(\sqrt{k}\), since equality to within \(O(1)\) occurs along the triangular numbers.

There are several nontriangular exact families as well.

## Proposition 2: small offsets from a triangular number

Let
\[
s\in\{0,1,2,3,4,6\},\qquad 0\le s<r,
\]
and put \(k=T_r+s\). Then
\[
\boxed{\Psi(k)=k-\left\lceil\frac{Q_r}{T_r}k\right\rceil.} \tag{8}
\]

### Proof

Use the following graphs \(Y_s\):
\[
\begin{array}{c|c|c}
s&Y_s&\operatorname{mc}(Y_s)\\ \hline
0&\varnothing&0\\
1&K_2&1\\
2&2K_2&2\\
3&K_3&2\\
4&K_3\cup K_2&3\\
6&K_4&4
\end{array}
\]
For \(r\ge3\),
\[
\frac12<\frac{Q_r}{T_r}\le\frac23,
\]
and direct inspection gives
\[
\operatorname{mc}(Y_s)
=\left\lceil\frac{Q_r}{T_r}s\right\rceil
\]
for the listed values of \(s\). Hence
\[
X=K_r\cup Y_s
\]
has \(T_r+s\) edges and
\[
\operatorname{mc}(X)
=Q_r+\left\lceil\frac{Q_r}{T_r}s\right\rceil
=\left\lceil\frac{Q_r}{T_r}(T_r+s)\right\rceil.
\]
All these graphs are circle graphs. ∎

## Proposition 3: one below a triangular number

For every \(n\ge3\),
\[
\boxed{\Psi(T_n-1)=T_n-1-Q_n.} \tag{9}
\]

### Proof

The graph \(K_n-e\) is a circle graph: duplicate one chord of a representation of \(K_{n-1}\) by a nearby nonintersecting twin. Moreover,
\[
\operatorname{mc}(K_n-e)=Q_n,
\]
because the endpoints of the deleted edge can be placed on the same side of a maximum cut of \(K_n\).

The lower bound (2), with \(r=n-1\), gives the same answer. Explicitly:

- If \(n=2a\), then
  \[
  \frac{Q_{n-1}}{T_{n-1}}(T_n-1)
  =a^2-\frac{a}{2a-1},
  \]
  whose ceiling is \(a^2=Q_n\).

- If \(n=2a+1\), then \(T_n-1=(2a-1)(a+1)\), so the corresponding expression is exactly \(a(a+1)=Q_n\).

∎

# 4. A family where the coloring bound is not sharp

The universal bound (4) is not always exact.

## Lemma 4: balancing five additional edges

Let \(F\) be a simple graph with five edges, and let \(C\) be an independent set of \(F\) with \(|C|\ge7\). There is a cut of \(F\) which cuts at least four edges and divides \(C\) as evenly as possible.

### Proof

Every five-edge graph has a cut of size at least four, by Theorem 1.

Let \(C'\subseteq C\) be the vertices incident with \(F\), and put \(c=|C'|\). Since every edge of \(F\) has at most one endpoint in \(C\), \(c\le5\). Reverse the two sides if necessary so that at most \(\lfloor c/2\rfloor\) active vertices lie on the smaller side. The vertices of \(C\setminus C'\) can then normally be assigned freely to balance \(C\).

The only deficient cases are \(|C|\in\{7,8\}\), \(c=5\), with all five active vertices on one side. In that situation each active vertex has degree one in \(F\), and every edge of \(F\) is incident with \(C\). Moving one active vertex either gains its edge, or, if all five edges were crossing, loses only one. Thus at least four crossings remain, and the inactive vertices complete the required balance. ∎

## Proposition 5: an exact odd-clique-plus-five family

For \(a\ge3\),
\[
\boxed{\Psi\!\left(T_{2a+1}+5\right)=a^2+1.} \tag{10}
\]

### Proof

Let \(H\) have
\[
k=T_{2a+1}+5
\]
edges, and put \(r=2a+1\).

If \(\chi(H)\le r-1=2a\), then the coloring argument with \(2a\) colors gives
\[
\operatorname{mc}(H)\ge
\left\lceil\frac{a}{2a-1}k\right\rceil.
\]
A calculation gives
\[
\frac{a}{2a-1}k
=a(a+1)+4-\frac{2a-4}{2a-1},
\]
so
\[
\operatorname{mc}(H)\ge a(a+1)+4=Q_r+4. \tag{11}
\]

Suppose instead that \(\chi(H)=r\). Take an \(r\)-critical subgraph \(J\). Then \(\delta(J)\ge r-1\). If \(|V(J)|\ge r+2\), then
\[
|E(J)|\ge\frac{(r-1)(r+2)}2=T_r+(r-1)>T_r+5,
\]
a contradiction. Thus \(|V(J)|\in\{r,r+1\}\).

If \(|V(J)|=r\), then \(J=K_r\). If \(|V(J)|=r+1\), then any graph on \(r+1\) vertices with chromatic number \(r\) contains \(K_r\): in its complement, two disjoint edges or a triangle would yield an \((r-1)\)-coloring; hence the complement is a star, possibly with isolated vertices.

Thus \(H\) contains \(K_r\). There are five remaining edges. By Lemma 4, one can use a maximum \(a\)-versus-\((a+1)\) cut of the clique while cutting at least four remaining edges. This again gives (11).

For equality, use
\[
K_{2a+1}\cup K_3\cup2K_2.
\]
Its maximum cut has size \(a(a+1)+4\), and all components are circle graphs. Its number of uncut edges is
\[
T_{2a+1}+5-\bigl(a(a+1)+4\bigr)=a^2+1.
\]
∎

For example,
\[
\Psi(26)=10,
\]
whereas (4) gives only \(\Psi(26)\le11\).

# 5. The exceptional value \(k=33\)

A second correction is needed at \(33=T_8+5\).

## Lemma 6

Every loopless integer-weighted graph \(W\) on seven vertices, of total edge weight \(12\), has a \(3\)-versus-\(4\) cut of weight at least \(8\).

### Proof

For a three-element set \(S\), write \(x(S)\) for its cut weight. Every edge is separated by exactly \(20\) of the \(\binom73=35\) such sets, so
\[
\sum_{|S|=3}x(S)=20\cdot12=240.
\]

Suppose every \(x(S)\le7\), and put \(y(S)=7-x(S)\). Then
\[
\sum_{|S|=3}y(S)=245-240=5. \tag{12}
\]

For a vertex \(v\) of weighted degree \(d(v)\),
\[
\sum_{\substack{|S|=3\\v\in S}}x(S)
=10d(v)+8(12-d(v))
=96+2d(v).
\]
Since there are fifteen such triples,
\[
\sum_{\substack{|S|=3\\v\in S}}y(S)
=105-(96+2d(v))
=9-2d(v).
\]
Thus \(d(v)\le4\). Since the total weighted degree is \(24\), at least three vertices have degree four.

There cannot be four such vertices. Indeed, a triple of degree-four vertices has
\[
x(S)=12-2e_W(S),
\]
which is even and at most \(7\), hence \(y(S)\ge1\). A degree-four vertex lying among four such vertices belongs to at least three all-degree-four triples, contradicting that its total \(y\)-incidence is \(1\).

Therefore exactly three vertices have degree four, and the other four have degree three. Let \(S_0\) be the triple of degree-four vertices. Then \(y(S_0)\ge1\), and for each of its vertices the total \(y\)-incidence is exactly one. Hence every other triple containing a degree-four vertex has \(y=0\), so its cut weight is \(7\).

But a triple consisting of one degree-four vertex and two degree-three vertices has total degree \(10\), so its cut weight
\[
10-2e_W(S)
\]
is even and cannot equal \(7\). This contradiction proves the lemma. ∎

## Proposition 7

\[
\boxed{\Psi(33)=13.} \tag{13}
\]

### Proof

Let \(H\) have \(33\) edges.

- If \(\chi(H)\le6\), then
  \[
  \operatorname{mc}(H)\ge
  \left\lceil\frac35\cdot33\right\rceil=20.
  \]

- If \(\chi(H)=7\), take a proper \(7\)-coloring. Every pair of color classes has at least one edge between it, or two classes could be merged. Write the number of edges between color classes \(i,j\) as
  \[
  1+w_{ij}.
  \]
  The excess weights \(w_{ij}\) sum to \(33-T_7=12\). By Lemma 6, a \(3\)-versus-\(4\) division of the colors cuts at least eight excess edges. The baseline \(K_7\) contributes twelve, so the resulting cut has at least \(20\) edges.

- If \(\chi(H)=8\), take an \(8\)-critical subgraph. Minimum degree at least seven shows that it has at most nine vertices. An eight-chromatic graph on eight or nine vertices contains \(K_8\), by the same complement argument used above. Lemma 4, with \(|C|=8\), gives a cut with \(16+4=20\) edges.

Thus every such \(H\) has maximum cut at least \(20\). Equality is attained by
\[
K_8\cup K_3\cup2K_2,
\]
whose maximum cut is \(16+2+1+1=20\). Hence \(\Psi(33)=33-20=13\). ∎

# 6. One further exceptional value

The same sparse-extension argument gives another exact value.

## Lemma 8

Let \(F\) be a simple seven-edge graph, and let \(C\) be an independent set of \(F\) of size \(9\). There is a cut splitting \(C\) into parts of sizes \(4\) and \(5\) and cutting at least five edges of \(F\).

### Proof

Theorem 1 gives a cut of \(F\) of size at least five. Let \(c\le7\) be the number of active vertices of \(C\), and orient the cut so that the smaller side contains \(x\le\lfloor c/2\rfloor\) of them. The inactive vertices balance \(C\) unless
\[
(c,x)\in\{(6,0),(7,0),(7,1)\}.
\]

For \(c=6,x=0\), the total \(F\)-degree of the six active vertices is either six or seven. Thus at least five of them have degree one. If the current cut has at least six edges, moving one such vertex loses at most one. If it has exactly five, either a degree-one noncrossing edge can be gained, or the unique possible degree-two active vertex has two noncrossing incident edges and can be moved.

For \(c=7\), every active vertex has degree one and every edge is incident with \(C\). If \(x=0\), move two active vertices, choosing two noncrossing edges when the cut has size five, one crossing and one noncrossing edge when it has size six, and two crossing edges when it has size seven. At least five crossings remain. If \(x=1\), moving one majority-side active vertex similarly retains at least five crossings. The two inactive vertices then complete a \(4\)-versus-\(5\) split. ∎

## Proposition 9

\[
\boxed{\Psi(43)=18.} \tag{14}
\]

### Proof

If a \(43\)-edge graph \(H\) satisfies \(\chi(H)\le8\), then
\[
\operatorname{mc}(H)\ge
\left\lceil\frac47\cdot43\right\rceil=25.
\]
If \(\chi(H)=9\), a \(9\)-critical subgraph has minimum degree eight. Since eleven vertices would already force at least \(44\) edges, it has nine or ten vertices and contains \(K_9\). Lemma 8 then supplies a cut with
\[
20+5=25
\]
edges.

The circle graph
\[
K_9\cup K_4\cup K_2
\]
has \(43\) edges and maximum cut \(20+4+1=25\). Therefore \(\Psi(43)=43-25=18\). ∎

# 7. Exact values through \(k=49\)

Combining Theorem 1, Propositions 2, 3, 5, 7, and 9 gives the following exact table.

\[
\begin{array}{c|rrrrrrrrrr}
k&0&1&2&3&4&5&6&7&8&9\\ \hline
\Psi(k)&0&0&0&1&1&1&2&2&2&3
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrr}
k&10&11&12&13&14&15&16&17&18&19\\ \hline
\Psi(k)&4&4&4&5&5&6&6&6&7&7
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrr}
k&20&21&22&23&24&25&26&27&28&29\\ \hline
\Psi(k)&8&9&9&9&10&10&10&11&12&12
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrr}
k&30&31&32&33&34&35&36&37&38&39\\ \hline
\Psi(k)&12&13&13&13&14&15&16&16&16&17
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrr}
k&40&41&42&43&44&45&46&47&48&49\\ \hline
\Psi(k)&17&17&18&18&19&20&20&20&21&21
\end{array}
\]

All lower-bound constructions are disjoint unions of complete graphs, except for \(K_n-e\); all are circle graphs. Thus they are realizable as conflict graphs of one-page drawings of matchings.

# 8. Remaining gap

The first value not determined by these arguments is \(k=50\). Here \(r=10\), and Theorem 1 gives
\[
\Psi(50)\le
\left\lfloor\frac49\cdot50\right\rfloor=22.
\]
On the other hand,
\[
K_{10}\cup K_3\cup2K_2
\]
has \(50\) edges and
\[
(45-25)+(5-4)=21
\]
uncut edges in every optimal bipartition, so
\[
\boxed{21\le\Psi(50)\le22.}
\]

Thus the general sharp function remains unresolved. The essential remaining extremal problem is:

\[
\min\{\operatorname{mc}(X):X\text{ is a circle graph with }k\text{ edges}\}.
\]

The coloring estimate gives a simple, constructive improvement over the source paper's Edwards bound and has the optimal asymptotic leading term, but the corrections at \(k=26,33,41,43,\ldots\) show that it is not the complete answer.