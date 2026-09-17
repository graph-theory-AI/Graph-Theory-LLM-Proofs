```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Explicit constructions verify the conjecture for every m≤20, also for m=30,32, and throughout a general near-diagonal range, but do not settle arbitrary m.",
  "would_publish": false,
  "caveats": "I do not claim these special cases are new; their novelty relative to the older papers has not been checked."
}
```

# 1. Results proved here

Write \(b_n=\binom n2\). I prove the following partial results.

**Theorem.**
1. The asserted positive cases hold: \(P(c,m)\) is true when \(m=1\), \(m=2\), or \(m=c\).
2. If
   \[
   m\in\{3,4,\ldots,20,30,32\},
   \]
   then \(P(c,m)\) is false for every \(c>m\).
3. More generally, writing \(d=c-m\ge1\), \(P(c,m)\) is false whenever
   \[
   m\ge \binom{d+1}{2}+2.
   \tag{1}
   \]
4. For each fixed pair \((c,m)\), deciding \(P(c,m)\) reduces to an explicitly bounded finite search: a counterexample, if one exists, has a finite-template representation with at most \(2(c-1)\) exceptional vertices.

The proof is constructive. No computational search is claimed. I have not verified whether some or all of these special cases already appear in the cited literature.

# 2. Finite templates

Let \(S\) be a finite set and \(R\) a countably infinite set disjoint from \(S\). Construct a coloring as follows:

- all edges inside \(R\) have color \(0\);
- for each \(v\in S\), all edges from \(v\) to \(R\) have one color \(\ell(v)\);
- edges inside \(S\) are colored arbitrarily.

For \(T\subseteq S\), define
\[
\sigma(T)=
\left|
\{0\}\cup\{\ell(v):v\in T\}
\cup\{\chi(uv):u,v\in T,\ u\ne v\}
\right|.
\tag{2}
\]
Every infinite vertex set has an infinite intersection with \(R\). Consequently, the set of color counts on infinite complete subgraphs is **exactly**
\[
\{\sigma(T):T\subseteq S\}.
\tag{3}
\]
Thus checking one of these constructions requires checking only finite subsets of its core.

Here and below, different prescribed color classes use different colors unless an equality of colors is explicitly specified.

## Finite-template reduction

Conversely, suppose an exact \(c\)-coloring of \(K_{\mathbb N}\) has no exactly \(m\)-colored infinite complete subgraph.

Choose one witnessing edge of each color, and let \(F\) contain their endpoints. Outside \(F\), infinite Ramsey gives an infinite monochromatic set \(R\), whose color we rename \(0\). Successively thinning \(R\), we can make the edges from each vertex of \(F\) to \(R\) monochromatic.

Keep in \(S\subseteq F\) the endpoints of one witnessing edge for each color other than \(0\). Then
\[
|S|\le 2(c-1).
\]
The restriction to \(S\cup R\) is an exact \(c\)-coloring of the template form and still avoids \(m\).

Therefore a counterexample exists if and only if such a template exists with at most \(2(c-1)\) core vertices. Enumerating all core-edge and link-color assignments, and checking (2) for all subsets, gives a deterministic decision algorithm with running time
\[
c^{O(c^2)}.
\]
This is an effective finite reduction, not a resolution of the general classification.

## Positive cases

The case \(m=1\) is infinite Ramsey, and \(m=c\) uses the entire graph.

For \(m=2\), apply the preceding extraction to any exact coloring, without assuming it is a counterexample. If some \(\ell(v)\ne0\), then \(T=\{v\}\) gives two colors. Otherwise all links have color \(0\), and an edge of a nonzero color in \(S\), together with \(R\), gives two colors.

# 3. Two elementary construction principles

### Rainbow-graph construction

Given a finite simple graph \(H\), color its edges with distinct nonzero colors, and color all other edges—including all links to \(R\)—with \(0\). Its infinite color counts are
\[
1+e(H[T]),\qquad T\subseteq V(H).
\tag{4}
\]

In particular, taking \(H=C_m\) proves
\[
\neg P(m+1,m)\qquad(m\ge3):
\tag{5}
\]
the whole cycle has \(m\) edges, whereas every proper induced subgraph has at most \(m-2\) edges.

### Refinement principle

Splitting a color class into smaller classes never decreases the number of colors on any vertex set. Starting from a finite coloring with \(q\) colors and repeatedly splitting off individual edges realizes every total color count between \(q\) and the rainbow total.

We will use lower bounds that survive refinement, together with upper bounds coming simply from the number of vertices and edges.

# 4. The cases \(m=3,4,5\)

Take a hub \(h\) and \(q\) leaves. Give the \(q\) hub–leaf edges distinct fresh colors. All leaves have the same link color, and all leaf–leaf edges have the same color.

The remaining specifications are:

| Forbidden \(m\) | \(\ell(h)\) | Leaf link color | Leaf–leaf color | Number of colors |
|---|---:|---:|---:|---:|
| \(3\) | \(a\) | \(b\) | \(b\) | \(q+3,\ q\ge1\) |
| \(4\) | \(0\) | \(a\) | \(b\) | \(q+3,\ q\ge2\) |
| \(5\) | \(a\) | \(b\) | \(e\) | \(q+4,\ q\ge2\) |

Here \(0,a,b,e\), when used, are distinct.

For \(m=3\), a subset containing the hub and \(r\ge1\) leaves has \(3+r\ge4\) colors; all other subsets have at most two.

For \(m=4\), hub plus one leaf gives three colors, while hub plus \(r\ge2\) leaves gives \(3+r\ge5\). Without the hub there are at most three colors.

For \(m=5\), hub plus one leaf gives four colors, while hub plus \(r\ge2\) leaves gives \(4+r\ge6\). Without the hub there are at most three colors.

These cover every \(c>m\) for \(m=3,4,5\).

# 5. Sum colorings: \(m=6,8,9,12\)

Color the edges of a core \([n]\) by
\[
\chi(ij)=i+j.
\]
There are \(2n-3\) edge colors. Every \(k\)-vertex subset, \(k\ge2\), uses at least \(2k-3\) colors: if its vertices are
\(x_1<\cdots<x_k\), consider
\[
x_1+x_2<\cdots<x_1+x_k<x_2+x_k<\cdots<x_{k-1}+x_k.
\tag{6}
\]
Refine this coloring arbitrarily.

### One common nonzero link color

Give every core vertex the same link color \(a\), distinct from \(0\) and all core colors. A nonempty \(T\) has
\[
\sigma(T)=2+\#\{\text{core colors on }T\}.
\]
Thus:

- \(|T|\le3\) implies \(\sigma(T)\le5\);
- \(|T|\ge4\) implies \(\sigma(T)\ge7\).

So six is avoided. For each \(n\ge4\), refinements realize every total in
\[
[\,2n-1,\ b_n+2\,].
\]
These intervals cover all integers at least seven. Hence
\[
\neg P(c,6)\qquad(c\ge7).
\]

### Distinct nonzero link colors

Instead give the \(n\) vertices distinct link colors, all disjoint from the core palette. Then
\[
\sigma(T)=1+|T|+\#\{\text{core colors on }T\}.
\tag{7}
\]

- Sets of size at most three use at most seven colors; sets of size at least four use at least ten. Thus eight and nine are avoided.
- Sets of size at most four use at most eleven colors; sets of size at least five use at least thirteen. Thus twelve is avoided.

The available totals for a fixed \(n\) are
\[
[\,3n-2,\ 1+b_{n+1}\,].
\tag{8}
\]
For \(n=4\), this is \([10,11]\); for \(n\ge5\), these intervals cover every integer at least thirteen.

This handles all required \(c\) for \(m=6,8,9,12\), except
\[
(m,c)=(8,9),(8,12),(9,12),
\tag{9}
\]
which are treated in Section 8.

# 6. Two-part constructions

Partition the core into
\[
A=\{a_1,\ldots,a_a\},\qquad
B=\{b_1,\ldots,b_b\}.
\]
Give \(A\) one nonzero link color and \(B\) a different one. Color all edges within the two parts rainbow, using colors not used anywhere else.

## 6.1 Cross-edge sum coloring: \(m=7,10\)

Color \(a_i b_j\) by \(i+j\), using a palette disjoint from the internal and link colors. Refine the cross-edge coloring as desired.

For nonempty index sets \(I,J\),
\[
|I+J|\ge |I|+|J|-1.
\tag{10}
\]

Consequently:

- every set of at most three core vertices uses at most six colors;
- every four core vertices use at least eight colors;
- every set of at most four core vertices uses at most nine colors;
- every five core vertices use at least eleven colors.

For example, the only nontrivial four-vertex split is \(2+2\): there are two internal colors, at least three cross colors, and three background/link colors. For five vertices, the nontrivial split \(3+2\) gives four internal colors, at least four cross colors, and three background/link colors.

Thus both seven and ten are avoided.

For balanced parts, \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\), the available totals form
\[
[\,2+n+b_a+b_b,\ 3+b_n\,].
\tag{11}
\]
The first intervals are
\[
[8,9],\quad[11,13],\quad[14,18],\quad[18,24].
\]
Thereafter they overlap or touch. Indeed, for \(n\ge6\),
\[
(a-1)(b-1)\ge n-2.
\]
Thus this construction supplies every \(c\ge11\), and also \(c=8,9\). Only \((m,c)=(7,10)\) remains.

## 6.2 Symmetric cross-edge identifications: \(m=11,19,20,32\)

Assume \(a\le b\). Start with every core edge rainbow, then identify the colors of
\[
a_i b_j\quad\text{and}\quad a_j b_i
\qquad(1\le i<j\le a).
\tag{12}
\]
All these identified pairs have different colors. Any selection of these identifications may subsequently be undone.

For a subset with \(x\) vertices in \(A\), \(y\) in \(B\), and \(t\) common indices, its core color count is at least
\[
b_{x+y}-b_t,\qquad t\le\min(x,y).
\tag{13}
\]
A mixed subset has three background/link colors; a subset in one part has two.

The resulting local gaps are:

| Forbidden values | Maximum on sets of size at most \(r-1\) | Minimum on \(r\)-sets |
|---|---:|---:|
| \(10,11\), \(r=5\) | \(9\) | \(12\) |
| \(19,20\), \(r=7\) | \(18\) | \(21\) |
| \(32\), \(r=9\) | \(31\) | \(33\) |

For instance, on a mixed seven-set the lower bound is
\[
3+b_7-b_3=21;
\]
a seven-set contained in one part has \(2+b_7=23\).

For balanced parts the available total-color interval is
\[
[\,3+b_n-b_{\lfloor n/2\rfloor},\ 3+b_n\,].
\tag{14}
\]
For \(n=5,6,7,8,9,10\), these are
\[
[12,13],\ [15,18],\ [21,24],\ [25,31],\
[33,39],\ [38,48].
\]
For \(n\ge10\), the intervals overlap or touch, since
\(b_{\lfloor n/2\rfloor}\ge n-2\).

Hence the outstanding pairs from this construction are:

- \(m=11\): \(c=14,19,20,32\);
- \(m=19\): \(c=20,32\);
- \(m=20\): \(c=32\).

There are no outstanding pairs for \(m=32\).

# 7. Linear four-block compression

This construction gives all \(m=13,\ldots,18\), as well as \(m=30\).

A **four-block packing** is a family \(\mathcal Q\) of four-element subsets of the core such that distinct blocks intersect in at most one vertex.

Inside a block \(Q\), partition its six edges into the three pairs of opposite edges. Independently for each pair, either give its two edges one common color or leave them differently colored. All other color classes are distinct.

Let \(d_Q\in\{0,1,2,3\}\) be the number of identifications made in block \(Q\). Then the number of core colors on \(T\) is exactly
\[
r(T)=b_{|T|}-\sum_{\substack{Q\in\mathcal Q\\Q\subseteq T}}d_Q.
\tag{15}
\]
Indeed, a proper subset of a four-block contains at most one edge from each opposite pair.

Two elementary consequences are crucial:

- a six-set contains at most one block, so \(r(T)\ge12\) on every six-set;
- an eight-set contains at most two blocks, so \(r(T)\ge22\) on every eight-set.

For the second assertion, three four-blocks have union of size at least \(12-3=9\).

With \(p\) blocks, every total reduction
\[
D\in\{0,1,\ldots,3p\}
\tag{16}
\]
is obtainable.

## 7.1 Packings with four vertex labels

We need packings in which every block contains all four labels.

A useful ten-vertex example has vertices
\[
p_1,p_2,p_3,p_4,\qquad e_{ij}\quad(1\le i<j\le4),
\]
and four blocks
\[
Q_i=\{p_i\}\cup\{e_{ij}:j\ne i\}.
\tag{17}
\]
Give the six \(e_{ij}\) the three labels of a proper three-edge-coloring of \(K_4\), and give all \(p_i\) the fourth label. Every block has all four labels.

There are also such packings with:

\[
\begin{array}{c|rrrr}
n&6&7&8&9\\ \hline
p&1&2&2&3
\end{array}
\tag{18}
\]
For \(n=7\), use two blocks meeting in one vertex; for \(n=8\), add an unused vertex; the \(n=9\) example comes from (17) by deleting \(p_4\).

For \(n=10q+s\ge10\), \(0\le s\le9\), use disjoint copies of (17), together with \(\lfloor s/4\rfloor\) extra blocks. This gives
\[
p=4q+\lfloor s/4\rfloor,\qquad 3p\ge n-2.
\tag{19}
\]

### Applying \(h=1,2,3,4\) link colors

Coarsen the four vertex labels onto \(h\) nonzero link colors, using all \(h\). Every block still contains every link color.

A set of at most five core vertices uses at most
\[
1+h+b_5=h+11
\]
colors.

Consider a six-set. If it uses all \(h\) link colors, it has at least
\[
1+h+12=h+13
\]
colors. If it omits some link color, it contains no complete block and its core is rainbow; it therefore has at least \(17\) colors. Since \(h\le4\), this is again at least \(h+13\).

Thus
\[
m=h+12
\tag{20}
\]
is avoided.

The total-color intervals are
\[
[\,1+h+b_n-3p,\ 1+h+b_n\,].
\tag{21}
\]
Using (18), their first four instances are
\[
[h+13,h+16],\quad[h+16,h+22],\quad
[h+23,h+29],\quad[h+28,h+37].
\]
For \(n\ge10\), (19) ensures that consecutive intervals overlap or touch. Hence every \(c\ge h+13=m+1\) is covered.

This proves all the cases \(m=13,14,15,16\).

## 7.2 Distinct link colors

Give every core vertex its own link color. Equation (15) now gives
\[
\sigma(T)=1+|T|+r(T).
\]

- Sets of size at most five use at most sixteen colors, while six-sets use at least nineteen. Thus seventeen and eighteen are avoided.
- Sets of size at most seven use at most twenty-nine colors, while eight-sets use at least thirty-one. Thus thirty is avoided.

For more blocks, use a ten-vertex packing whose vertices are the edges of \(K_5\), with five blocks consisting of the four edges incident with each vertex of \(K_5\). Different blocks meet in one vertex.

Thus, for \(n=10q+s\ge10\), we can take
\[
p=5q+\lfloor s/4\rfloor,
\qquad 3p\ge n+1.
\tag{22}
\]
For \(n=6,7,8,9\), use (18). The total-color intervals are now
\[
[\,1+b_{n+1}-3p,\ 1+b_{n+1}\,].
\tag{23}
\]
Their union is
\[
[19,29]\ \cup\ [31,\infty).
\tag{24}
\]

Consequently, this proves all cases for \(m=30\), and all cases for \(m=17,18\) except
\[
(17,18),\quad(17,30),\quad(18,30).
\tag{25}
\]

# 8. The finite list of exceptional pairs

Here are explicit constructions for every pair left above.

Terminology:

- **Common links:** all core vertices have one nonzero link color; the infinite palette has \(2+r(T)\) colors for nonempty \(T\).
- **Base links:** all links have color \(0\).
- **Collapsed triangle:** its three edges receive one color.
- **Factored \(K_4\):** each of its three perfect matchings receives one color.

All unspecified core edges are rainbow, and all specified blocks in the following table are vertex-disjoint.

| \((m,c)\) | Links | Core |
|---|---|---|
| \((7,10)\) | Common | \(K_5\), one collapsed triangle |
| \((8,12)\) | Base | \(K_6\), two collapsed triangles |
| \((9,12)\) | Base | Rainbow graph \(K_5\sqcup K_2\); nonedges have color \(0\) |
| \((11,14)\) | Base | Rainbow graph \(K_6\) minus two disjoint edges; nonedges have color \(0\) |
| \((11,19)\) | Common | \(K_7\), two collapsed triangles |
| \((11,20)\) | Common | \(K_7\), one factored \(K_4\) |
| \((11,32)\), \((20,32)\) | Common | \(K_9\), three collapsed triangles |
| \((19,32)\) | Common | \(K_9\), two factored \(K_4\)'s |
| \((18,30)\) | Common | Rainbow \(K_8\) |

The pairs \((8,9),(17,18),(19,20)\) follow from the cycle construction (5).

For completeness, the palette checks for the table are as follows.

### Collapsed triangles

With vertex-disjoint collapsed triangles,
\[
r(T)=b_{|T|}-2u(T),
\tag{26}
\]
where \(u(T)\) counts the complete triangles contained in \(T\).

- On \(K_5\) with one collapsed triangle, core count five is impossible: up to three vertices give at most three colors, four vertices give four or six, and the full core gives eight.
- On \(K_6\) with two collapsed triangles, core count seven is impossible: up to four vertices give at most six, five vertices give an even count, and the full core gives eleven.
- On \(K_7\) with two, or \(K_9\) with three, collapsed triangles, core count nine is impossible: five-vertex counts are even, and every six-set has at least \(15-4=11\) colors.
- On \(K_9\) with three collapsed triangles, core count eighteen is impossible: up to six vertices give at most fifteen, seven-vertex counts are odd, and every eight-set has at least \(28-4=24\) colors.

These prove the corresponding rows after adding the background/link colors.

### Factored four-blocks

With vertex-disjoint factored \(K_4\)'s,
\[
r(T)=b_{|T|}-3v(T).
\tag{27}
\]

- One factored \(K_4\) in \(K_7\) avoids core count nine: a five-set has seven or ten colors, and a six-set has at least twelve.
- Two disjoint factored \(K_4\)'s in \(K_9\) avoid core count seventeen: up to six vertices give at most fifteen, and a seven-set contains at most one whole block, giving at least eighteen.

### The rainbow graphs

For \(K_5\sqcup K_2\), the induced edge counts are \(b_t+\varepsilon\), with \(0\le t\le5\) and \(\varepsilon\in\{0,1\}\); eight is absent.

For \(K_6\) minus two disjoint edges, every five-set still contains at least one missing edge, so has at most nine edges. Smaller sets have at most six edges, and the full graph has thirteen. Thus ten is absent.

For common-link rainbow \(K_8\), the possible counts are
\[
\{1\}\cup\{2+b_t:1\le t\le8\},
\]
which does not contain eighteen.

### The remaining pair \((m,c)=(17,30)\)

Take eight core vertices partitioned into two four-sets. Factor each four-set, reducing the core palette by six colors. Among the cross edges, identify the colors of two disjoint edges, producing one further reduction. Give all eight vertices distinct nonzero link colors.

The total is
\[
1+8+b_8-7=30.
\]
A set of at most five core vertices uses at most sixteen colors. A six-set cannot contain both four-blocks, so its core loses at most \(3+1=4\) colors; hence it uses at least
\[
1+6+(15-4)=18
\]
colors. Seventeen is avoided.

This finishes every exceptional pair. Together, Sections 4–8 prove part 2 of the theorem.

# 9. A uniform near-diagonal range

I now prove (1), which applies to unbounded \(m\), not just the numerical cases above.

Put
\[
d=c-m,\qquad r=d+1,\qquad E=c-1.
\]
Condition (1) is equivalent to
\[
E\ge \binom{r+1}{2}.
\tag{28}
\]
It suffices, by (4), to construct a graph with \(E\) edges having no induced subgraph with \(E-d\) edges.

Set
\[
E_0=\binom{r+1}{2},
\qquad
A=\left\lceil\frac{r(r+2)}2\right\rceil.
\]

### Case 1: \(E_0\le E<A\)

Let \(L=E-E_0\), and take
\[
H=K_{r+1}\sqcup L K_2.
\]
Here
\[
L\le \lceil r/2\rceil-1<r-1=d.
\]
An induced subgraph retaining the whole clique loses at most \(L<d\) edges. One omitting a clique vertex loses at least \(r=d+1\) edges. Thus it cannot lose exactly \(d\) edges.

### Case 2: \(E\ge A\)

There is a graph with \(E\) edges and minimum degree at least \(r\).

To see this, choose the smallest \(n\ge r+2\) with \(E\le b_n\). Then
\[
E\ge \left\lceil\frac{nr}{2}\right\rceil.
\tag{29}
\]
For \(n=r+2\), this is the definition of \(A\). For \(n\ge r+3\), minimality gives \(E\ge b_{n-1}+1\), and
\[
b_{n-1}+1-\frac{nr}{2}
=\frac{n(n-r-3)+4}{2}>0.
\]

Among all \(n\)-vertex graphs with \(E\) edges, choose one minimizing the sum of squared degrees. Its degrees differ by at most one: otherwise an edge can be transferred from a higher-degree vertex to a lower-degree vertex, decreasing that sum. Hence its minimum degree is
\[
\left\lfloor\frac{2E}{n}\right\rfloor\ge r.
\]
Every proper induced subgraph therefore loses at least \(r=d+1\) edges, and cannot have \(E-d\) edges.

Applying the rainbow-graph construction proves (1).

# 10. What remains unresolved by this argument

The constructions above establish the claimed negative direction for all
\[
m\le20,\qquad m=30,32,
\]
and for the general strip
\[
c-m=d,\qquad m\ge\binom{d+1}{2}+2.
\]

They do **not** establish \(\neg P(c,m)\) for every \(3\le m<c\). The local palette-gap constructions work by arranging a jump between the maximum palette on small core subsets and the minimum palette on larger ones; the arguments given here provide no such construction for arbitrary prescribed \(m\) and \(c\).

The finite-template reduction makes every individual pair decidable, but I have not run that enumeration and it does not by itself prove the conjectured uniform answer. Thus the verdict is partial, with no claim of novelty for the special cases.