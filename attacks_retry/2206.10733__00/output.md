```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A five-cycle construction gives an asymptotically sharp 5ell^2/4 threshold for eventual equality in the degree bound, and new exact transition values complete the ell=4 case.",
  "would_publish": false,
  "caveats": "The general transition window remains unresolved; the happy-triple definition is taken from the supplied attempt, and novelty has not been independently checked."
}
```

# 1. Formulation and results

I use the definition in the supplied attempt: a **happy triple** is an unordered three-element vertex set spanning at least two edges. Graphs are finite and simple, and their order is unrestricted.

Write
\[
M(k,\ell)=\max\{h(G):e(G)=k,\ \Delta(G)\le \ell\}.
\]
Isolated vertices can be discarded, so this maximum is over graphs with at most \(2k\) vertices and is attained.

The principal new result below is a near-optimal realization theorem for triangle-free almost-regular degree sequences. It improves the supplied attempt’s eventual cutoff from approximately \(2\ell^2\) to approximately \(5\ell^2/4\). The constant \(5/4\) is best possible for such an eventual cutoff.

I also obtain an infinite family of exact values just above the square threshold and complete the case \(\ell=4\).

## Theorem

Let \(\ell\ge2\). Define
\[
2k=Q\ell+R,\qquad 0\le R<\ell,
\]
and
\[
U_\ell(k)
=Q\binom{\ell}{2}+\binom R2
=k(\ell-1)-\frac{R(\ell-R)}2.
\tag{1}
\]

Then:

1. **Universal bound.**
   \[
   M(k,\ell)\le U_\ell(k).
   \tag{2}
   \]

2. **Improved eventual equality.** Put
   \[
   T_\ell=
   \left\lceil
   \frac{\ell}{2}\left(5\left\lceil\frac{\ell}{2}\right\rceil+4\right)
   \right\rceil.
   \tag{3}
   \]
   Then
   \[
   \boxed{M(k,\ell)=U_\ell(k)\qquad(k\ge T_\ell).}
   \tag{4}
   \]
   In particular,
   \[
   T_\ell=
   \begin{cases}
   \dfrac54\ell^2+2\ell,&\ell\text{ even},\\[1mm]
   \left\lceil\dfrac{5\ell^2+13\ell}{4}\right\rceil,
      &\ell\text{ odd}.
   \end{cases}
   \]

3. **The leading constant is optimal.** Define the eventual saturation threshold
   \[
   \kappa_\ell=\min\{K:M(k,\ell)=U_\ell(k)\text{ for every }k\ge K\}.
   \]
   Then
   \[
   \boxed{\kappa_\ell=\frac54\ell^2+O(\ell).}
   \tag{5}
   \]

4. **An exact transition family.** For every \(\ell\ge4\),
   \[
   \boxed{
   M(\ell^2+2,\ell)=\ell^2(\ell-1)+3
   =U_\ell(\ell^2+2)-3.}
   \tag{6}
   \]

5. **Complete answer for \(\ell=4\).** For \(k\le16\), use the square-range formula below. Above that range,
   \[
   \boxed{
   M(k,4)=
   \begin{cases}
   49,&k=17,\\
   51,&k=18,\\
   54,&k=19,\\
   3k,&k\ge20\text{ even},\\
   3k-2,&k\ge21\text{ odd}.
   \end{cases}}
   \tag{7}
   \]

I checked the supplied attempt’s square-range induction, including its cap-monotonicity calculation; it is valid. For completeness, I include a compact proof rather than treating that attempt as an authority.

# 2. Basic bounds and the verified square-range formula

Let \(t(G)\) denote the number of triangles. Counting pairs of incident edges gives
\[
h(G)=\sum_v\binom{d(v)}2-2t(G).
\tag{8}
\]

## 2.1. The degree bound and its equality condition

Among integer vectors with entries in \([0,\ell]\) and sum \(2k\), the maximum of
\[
\sum_v\binom{d(v)}2
\]
is attained by
\[
(\ell^Q,R),
\]
omitting the final entry when \(R=0\). Indeed, if \(0<a\le b<\ell\), moving one unit from \(a\) to \(b\) increases the objective by \(b-a+1>0\).

Consequently, (8) proves (2). It also proves the exact equality criterion:

> \[
> h(G)=U_\ell(k)
> \]
> if and only if \(G\) is triangle-free and its positive degree sequence is \((\ell^Q,R)\), with \(R=0\) omitted.

This criterion is central both to the constructions and to the obstructions below.

## 2.2. An explicit lower bound above the square threshold

Write
\[
k=q\ell+s,\qquad 0\le s<\ell.
\]
For \(k\ge\ell^2\), so \(q\ge\ell\), define
\[
B_\ell(k)
=2\left(q\binom{\ell}{2}+\binom s2\right)
=k(\ell-1)-s(\ell-s).
\tag{9}
\]
Then
\[
\boxed{B_\ell(k)\le M(k,\ell)\le U_\ell(k).}
\tag{10}
\]

Here is a construction for the lower bound. Start with an \(\ell\)-regular bipartite graph on \(q+q\) vertices containing a specified perfect matching. One explicit choice has both parts indexed by \(\mathbb Z_q\), with \(i\) adjacent to
\[
i,i+1,\ldots,i+\ell-1.
\]
Delete \(s\) edges of the matching. Add one new vertex in each part, and reconnect each endpoint of a deleted edge to the new vertex in the opposite part.

The resulting bipartite graph has degree sequence \((\ell^q,s)\) on each side and exactly \(q\ell+s\) edges. Its happy-triple count is (9).

The gap in (10) is particularly simple:
\[
U_\ell(k)-B_\ell(k)=\min\{s,\ell-s\}^2.
\tag{11}
\]

## 2.3. Exact answer for \(k\le\ell^2\)

For \(k=q\ell+s\), \(0\le s<\ell\), put
\[
\Phi_\ell(k)
=
q\binom{\ell}{2}+\binom s2
+\ell\binom q2+sq.
\tag{12}
\]
Then
\[
\boxed{M(k,\ell)=\Phi_\ell(k)\qquad(k\le\ell^2).}
\tag{13}
\]

### Upper bound

We use induction on \(\ell\), and within it induction on \(k\). The case \(\ell=1\) is immediate.

Three elementary identities or inequalities are needed:
\[
\Phi_\ell(k)
=\Phi_\ell(k-\ell)+\binom{\ell}{2}+k-\ell
\qquad(k\ge\ell),
\tag{14}
\]
\[
\Phi_L(m)\le\Phi_{L+1}(m)
\qquad(m\le L^2),
\tag{15}
\]
and
\[
\Phi_\ell(k)\ge k(\ell-2)
\qquad((\ell-1)^2<k\le\ell^2).
\tag{16}
\]

For clarity, the algebra behind the last two assertions is as follows. If \(m=aL+b\), \(0\le b<L\), then \(a\le L\), and
\[
\Phi_{L+1}(m)-\Phi_L(m)
=
\begin{cases}
a(L-b),&b\ge a,\\
b(L-a),&b<a.
\end{cases}
\]
For (16), the possible quotients \(q=\lfloor k/\ell\rfloor\) are \(\ell-2,\ell-1,\ell\). The corresponding differences
\(\Phi_\ell(k)-k(\ell-2)\) are
\[
\binom s2,\qquad
\frac{\ell(\ell-1)+s(s+1)}2,\qquad
\ell^2,
\]
respectively.

Now let \(G\) have \(k\le\ell^2\) edges.

If \(\Delta(G)\le\ell-1\), then for \(k\le(\ell-1)^2\), induction and (15) apply. For larger \(k\), (8) gives
\[
h(G)\le k(\ell-2)\le\Phi_\ell(k).
\]

Otherwise choose \(v\) with degree \(\ell\), and put
\[
A=N(v),\qquad B=V(G)\setminus(A\cup\{v\}).
\]
The happy triples containing \(v\) are precisely the \(\binom{\ell}{2}\) triples using two vertices of \(A\), together with the triples corresponding to edges between \(A\) and \(B\). Thus
\[
h(G)=h(G-v)+\binom{\ell}{2}+e(A,B)
\le h(G-v)+\binom{\ell}{2}+k-\ell.
\]
Induction and (14) finish the upper bound.

### Construction

Take \(q\) vertices adjacent to all \(\ell\) vertices in the opposite bipartition class, and, if \(s>0\), one additional vertex adjacent to \(s\) of those \(\ell\) vertices.

Its two degree lists are
\[
(\ell^q,s),\qquad ((q+1)^s,q^{\ell-s}).
\]
Because \(k\le\ell^2\), every degree is at most \(\ell\). It is triangle-free, and its degree sum of wedges is exactly (12).

This proves (13).

In particular, the divisible case is completely settled:
\[
M(q\ell,\ell)=
\begin{cases}
\dfrac{q\ell}{2}(\ell+q-2),&q\le\ell,\\[2mm]
q\ell(\ell-1),&q\ge\ell.
\end{cases}
\tag{17}
\]

# 3. Two elementary facts about nonbipartite triangle-free graphs

The following lemma supplies both the asymptotic obstruction and the transition arguments.

## Lemma 1

If \(H\) is triangle-free and nonbipartite, on \(n\) vertices, then
\[
\delta(H)\le\frac{2n}{5}
\tag{18}
\]
and
\[
e(H)\le \left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\tag{19}
\]

### Proof

Let \(C\) be a shortest odd cycle, of length \(g\ge5\). It has no chord.

Every vertex outside \(C\) has at most two neighbors on \(C\). Indeed, if it had at least three, the cyclic gaps between consecutive neighbors would all have length at least two. Since their sum is odd, one gap would be odd, and that gap would have length at most \(g-4\). Together with the outside vertex it would give a shorter odd cycle.

It follows that
\[
\sum_{v\in C}d(v)\le2g+2(n-g)=2n.
\]
Hence \(g\delta(H)\le2n\), proving (18).

Also, the subgraph outside \(C\) is triangle-free. Mantel’s bound gives
\[
e(H)\le g+2(n-g)+\left\lfloor\frac{(n-g)^2}{4}\right\rfloor.
\]
The right side decreases with \(g\), so it is at most its value at \(g=5\):
\[
2n-5+\left\lfloor\frac{(n-5)^2}{4}\right\rfloor
=
\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]
This proves (19).

For completeness, Mantel’s bound follows from
\(d(u)+d(v)\le n\) for each edge \(uv\) of a triangle-free graph:
\[
\sum_v d(v)^2\le ne(H),
\]
and Cauchy–Schwarz then gives \(e(H)\le n^2/4\). ∎

# 4. The five-cycle realization theorem

This is the main additional construction.

## Lemma 2: Almost-regular triangle-free realization

Let \(d\ge2\), \(0\le r\le d\), and
\[
n\ge5\left(\left\lceil\frac d2\right\rceil+1\right).
\tag{20}
\]
If \((n-1)d+r\) is even, there exists a triangle-free graph with degree list
\[
(d^{\,n-1},r).
\tag{21}
\]
When \(r=0\), the final vertex is isolated.

We first record a simple bipartite realization fact.

### Balanced-side realization fact

Suppose one side of a bipartite graph has prescribed degrees
\[
c_1,\ldots,c_p,\qquad 0\le c_i\le q.
\]
There is a realization in which the \(q\) degrees on the other side differ by at most one.

To construct it, index the other side cyclically by \(\mathbb Z_q\). Give the first vertex the first \(c_1\) consecutive residues, the next vertex the next \(c_2\), and so on, continuing cyclically. Each left vertex has distinct neighbors, and the total usage of the residues is balanced. By relabeling, any prescribed balanced degree list on the other side with the correct sum is obtained.

### Proof of Lemma 2

Write
\[
n=5a+b,\qquad 0\le b<5.
\]
By (20),
\[
a\ge\left\lceil\frac d2\right\rceil+1.
\tag{22}
\]

Partition the vertices into five sets \(A_0,\ldots,A_4\), indexed cyclically, with
\[
a_i:=|A_i|=
\begin{cases}
a+1,&0\le i<b,\\
a,&b\le i\le4.
\end{cases}
\]
Choose the exceptional vertex \(z\) in \(A_0\).

We shall put edges only between consecutive parts of this five-cycle. Any resulting graph is automatically triangle-free.

Let
\[
\eta=d-r,\qquad
D_0=da_0-\eta,\qquad D_i=da_i\quad(i\ne0).
\]
Thus \(D_i\) is the required total degree of part \(A_i\).

The number \(x_i\) of edges between \(A_i\) and \(A_{i+1}\) is forced by
\[
x_{i-1}+x_i=D_i.
\]
The solution is
\[
x_i=\frac{D_i+D_{i+1}-D_{i+2}+D_{i+3}-D_{i+4}}2.
\tag{23}
\]
These are integers, since \(\sum_iD_i=(n-1)d+r\) is even.

We now split each vertex’s degree between its two neighboring parts.

#### Normal parts

Define
\[
T_i=a_{i+1}-a_{i+2}+a_{i+3}-a_{i+4}.
\]
For the consecutive placement of the larger parts, the five possibilities are
\[
\begin{array}{c|rrrrr}
b&T_0&T_1&T_2&T_3&T_4\\ \hline
0&0&0&0&0&0\\
1&0&-1&1&-1&1\\
2&1&-1&0&0&0\\
3&0&0&0&-1&1\\
4&1&-1&1&-1&0
\end{array}
\tag{24}
\]
and
\[
\frac{x_i}{a_i}
=\frac d2+\frac{dT_i+\varepsilon_i\eta}{2a_i},
\qquad
(\varepsilon_0,\ldots,\varepsilon_4)=(-1,1,-1,1,-1).
\tag{25}
\]

For \(i\ne0\), table (24) shows
\[
|dT_i+\varepsilon_i\eta|\le d.
\]
Consequently,
\[
\frac d2-1\le\frac{x_i}{a_i}\le\frac d2+1.
\tag{26}
\]

On each normal part \(A_i\), choose a balanced list of degrees toward \(A_{i+1}\), summing to \(x_i\). Give each vertex its complementary degree, up to total \(d\), toward \(A_{i-1}\). Both lists are balanced.

By (22) and (26), all these degrees are nonnegative and at most \(a\), hence no greater than the size of the neighboring part.

#### The exceptional part

Give \(z\) degree
\[
u=\lfloor r/2\rfloor
\]
toward \(A_1\), and degree \(r-u\) toward \(A_4\).

For the other \(a_0-1\) vertices of \(A_0\), choose a balanced list of degrees toward \(A_1\), summing to \(x_0-u\), and use complementary degrees toward \(A_4\). Their forward average is
\[
\frac{x_0-u}{a_0-1}
=
\frac d2+
\frac{dT_0+r-2u}{2(a_0-1)}.
\tag{27}
\]

Here \(T_0\in\{0,1\}\) and \(r-2u\in\{0,1\}\). If \(T_0=1\), then \(b=2\) or \(4\), so \(a_0=a+1\), and the last term is at most
\[
\frac{d+1}{2a}<1.
\]
If \(T_0=0\), it is at most \(1/[2(a_0-1)]\le1\).

Thus all degrees assigned in \(A_0\), including their complementary degrees, are again between \(0\) and \(a\). The two assigned degrees of \(z\) also satisfy the required bounds.

#### Realizing the five links

For each consecutive pair of parts, the two assigned degree lists have the same sum \(x_i\).

- Between two normal parts, both lists are balanced.
- For either link incident with \(A_0\), the list on the other part is balanced.

The balanced-side realization fact therefore realizes each link independently. The resulting simple graph has the prescribed degree list (21), and, being a subgraph of a blow-up of \(C_5\), is triangle-free. ∎

## Applying the lemma

Let
\[
N_\ell=5\left(\left\lceil\frac{\ell}{2}\right\rceil+1\right).
\]
For \(2k=Q\ell+R\), apply Lemma 2 with
\[
d=\ell,\qquad n=Q+1,\qquad r=R.
\]
It applies whenever \(Q\ge N_\ell-1\), equivalently whenever
\[
k\ge
\left\lceil\frac{\ell(N_\ell-1)}2\right\rceil=T_\ell.
\]
The constructed graph attains the equality criterion following (8). This proves (4).

# 5. Why the constant \(5/4\) cannot be reduced

We prove (5) by exhibiting failures of \(M(k,\ell)=U_\ell(k)\) just below \(5\ell^2/4\).

## Even \(\ell\)

Let \(n\) be the largest odd integer satisfying
\[
n<\frac{5\ell}{2},
\]
and put \(k=n\ell/2\).

Equality in the degree bound would require a triangle-free \(\ell\)-regular graph on \(n\) vertices. It cannot be bipartite: a nonempty regular bipartite graph has equal-sized bipartition classes and hence even order. But Lemma 1 would then give
\[
\ell\le\frac{2n}{5}<\ell,
\]
a contradiction.

Since \(n\ge5\ell/2-2\),
\[
\kappa_\ell\ge k+1\ge\frac54\ell^2-\ell+1.
\tag{28}
\]

## Odd \(\ell\ge3\)

Let \(n\) be the largest odd integer satisfying
\[
n<\frac{5(\ell-1)}2,
\]
and put
\[
k=\frac{n\ell-1}{2}.
\]
Equality would require degree sequence
\[
(\ell^{n-1},\ell-1).
\]

Such a graph cannot be bipartite. If the exceptional vertex lies in one part, equality of the degree sums of the two parts would imply that \(\ell\) divides \(\ell-1\).

It would therefore be nonbipartite and triangle-free, with minimum degree \(\ell-1\). Lemma 1 again contradicts the choice of \(n\).

Since \(n\ge5(\ell-1)/2-2\),
\[
\kappa_\ell\ge k+1
\ge\frac54\ell^2-\frac94\ell+\frac12.
\tag{29}
\]

Combining (28)–(29) with the upper bound \(T_\ell\) proves
\[
\kappa_\ell=\frac54\ell^2+O(\ell).
\]

Thus the improved leading constant is not merely a feature of the construction: it is forced by triangle-free degree constraints.

# 6. Exact value at \(k=\ell^2+2\)

We now prove (6).

## Construction

Start with \(K_{\ell,\ell}\), subdivide one edge, and attach a new leaf to the subdivision vertex.

The graph is triangle-free, has \(\ell^2+2\) edges, and has degree sequence
\[
(\ell^{2\ell},3,1).
\]
Hence
\[
h(G)=2\ell\binom{\ell}{2}+\binom32
=\ell^2(\ell-1)+3.
\tag{30}
\]

## Upper bound

Let \(G\) have \(\ell^2+2\) edges and maximum degree at most \(\ell\), where \(\ell\ge4\). Discard isolated vertices and write \(n=v(G)\). Necessarily \(n\ge2\ell+1\).

### Case 1: \(n\ge2\ell+2\)

Among positive degree lists with sum \(2\ell^2+4\), cap \(\ell\), and at least \(2\ell+2\) entries, convexity gives
\[
\sum_v\binom{d(v)}2
\le 2\ell\binom{\ell}{2}+\binom32.
\tag{31}
\]

One formal way to see this is to put \(x_v=d(v)-1\). For fixed \(n\), concentrate the \(2\ell^2+4-n\) units into buckets of capacity \(\ell-1\). The resulting maximum is increasing in the number of units, so it is largest when \(n=2\ell+2\). The extremal list is then \((\ell^{2\ell},3,1)\).

Equation (8) and (31) give the required bound.

### Case 2: \(n=2\ell+1\)

The unconstrained degree bound is
\[
\sum_v\binom{d(v)}2
\le \ell^2(\ell-1)+6.
\tag{32}
\]
We show that \(G\) has at least two triangles.

It cannot be triangle-free:

- If bipartite, one part has at most \(\ell\) vertices, so
  \(e(G)\le\ell^2\).
- If nonbipartite, Lemma 1 gives
  \(e(G)\le\ell^2+1\).

Suppose, then, that \(abc\) is the unique triangle.

The total deficiency from degree \(\ell\) is
\[
\sum_v(\ell-d(v))=(2\ell+1)\ell-2(\ell^2+2)=\ell-4.
\]
Therefore
\[
d(a)+d(b)+d(c)\ge3\ell-(\ell-4)=2\ell+4.
\tag{33}
\]
Every outside vertex has at most one neighbor in \(\{a,b,c\}\), because the triangle is unique. Consequently,
\[
d(a)+d(b)+d(c)-6\le2\ell-2.
\]
Together with (33), this forces equality throughout.

Thus every outside vertex:

- has degree \(\ell\);
- has exactly one neighbor in the triangle.

The induced outside graph is therefore triangle-free and \((\ell-1)\)-regular on \(2(\ell-1)\) vertices. It must be \(K_{\ell-1,\ell-1}\): the neighborhood of any vertex is independent, and every vertex in that neighborhood must be adjacent to every vertex outside it.

For each of \(a,b,c\), its outside neighborhood is independent and hence lies entirely in one side of this complete bipartite graph. These three neighborhoods partition the outside vertices, and each has size at most \(\ell-2\). But each side has size \(\ell-1\), so each side requires at least two of the three neighborhoods—a contradiction.

Thus \(t(G)\ge2\). By (8) and (32),
\[
h(G)\le\ell^2(\ell-1)+6-4
=\ell^2(\ell-1)+2,
\]
which is even smaller than (30).

Both cases establish (6).

# 7. Completing \(\ell=4\)

Only \(k=19\) requires an additional obstruction beyond the preceding results and easy constructions.

## 7.1. The value at \(k=19\)

Here
\[
U_4(19)=55.
\]
Equality would require a triangle-free graph with degree sequence
\[
(4^9,2).
\]
Let \(z\) be its degree-two vertex and set \(F=G-z\). Then \(F\) is triangle-free, has nine vertices and seventeen edges, and has degree sequence
\[
(4^7,3,3).
\tag{34}
\]

It is not bipartite: seventeen edges and maximum degree four would require at least five vertices in each bipartition class.

In the proof of Lemma 1, equality at \(n=9,e=17\) forces:

- a shortest odd cycle \(C\) of length five;
- the other four vertices to induce \(K_{2,2}\);
- each of those four vertices to have exactly two neighbors on \(C\).

Let \(X,Y\) be the two sides of this \(K_{2,2}\). Put
\[
S=\bigcup_{x\in X}N_C(x),\qquad
T=\bigcup_{y\in Y}N_C(y).
\]
Triangle-freeness gives \(S\cap T=\varnothing\). Both sets have size at least two. By (34), every cycle vertex has an outside neighbor, so \(S\cup T=V(C)\). Thus their sizes are two and three.

Suppose \(|S|=2\). The two vertices of \(X\) have the same independent pair \(S\) as their cycle neighborhood. The complement \(T\) of an independent pair in \(C_5\) consists of an edge and an isolated vertex.

Each vertex of \(Y\) must choose an independent pair in \(T\), and their neighborhoods must cover \(T\). Hence they both use the isolated vertex and use different endpoints of the edge. It follows that the two degree-three vertices of \(F\) are precisely those adjacent endpoints.

But these are the two neighbors of \(z\). Restoring \(z\) creates a triangle, a contradiction.

Therefore \(M(19,4)\le54\). The bipartite construction in Section 2.2 has degree sequence
\[
(4^8,3,3)
\]
and attains \(54\). Hence
\[
M(19,4)=54.
\]

## 7.2. All other values

- For \(k\le16\), use (13).
- Subdividing an edge of \(K_{4,4}\) gives \(M(17,4)=49\).
- Equation (6) gives \(M(18,4)=51\).

For all even \(k\ge20\), put \(n=k/2\ge10\). On \(\mathbb Z_n\), join each vertex to those at differences
\[
\pm1,\ \pm3.
\]
This is a simple 4-regular triangle-free graph.

To verify triangle-freeness, a triangle would give three steps from \(\{\pm1,\pm3\}\) summing to zero modulo \(n\). If \(n\) is even, that is impossible by parity. If \(n\) is odd, then \(n\ge11\), while such a sum has absolute value at most nine and is an odd, nonzero integer.

The graph has \(k\) edges and \(3k\) happy triples.

For odd \(k\ge21\), subdivide one edge of the preceding construction with \(k-1\) edges. Its degree sequence is
\[
(4^{(k-1)/2},2),
\]
and its happy-triple count is \(3k-2\).

These match (1), completing (7).

# 8. What remains unresolved

The original two-parameter problem is not fully settled here. For general \(\ell\), the remaining values can lie in the finite transition window
\[
\ell^2<k<T_\ell,
\]
after removing the exact families and divisible cases proved above.

Throughout that window,
\[
B_\ell(k)\le M(k,\ell)\le U_\ell(k),
\]
with explicit gap \(\min\{s,\ell-s\}^2\). Equality at the upper endpoint is equivalent to a triangle-free realization of one prescribed almost-regular degree sequence. When that realization does not exist, determining \(M(k,\ell)\) requires accounting for both degree-sum losses and triangle penalties.

The new conclusions are nevertheless substantive:

- the eventual equality threshold has the sharp leading term \(5\ell^2/4\);
- the bound \(U_\ell(k)\) fails by exactly three at every \(k=\ell^2+2\), \(\ell\ge4\);
- the maximum-degree-four problem is completely determined.

All arguments above are self-contained; no computational checks or unverified external results are used. Novelty relative to literature beyond the supplied material remains unchecked.