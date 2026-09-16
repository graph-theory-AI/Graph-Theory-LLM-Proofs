```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain sharp subclass suprema, including an explicit family of planar triangulations approaching circular choosability 6, and quantitative bounds for K_{2,n}, but do not improve the general upper bound 8.",
  "would_publish": false,
  "caveats": "The general 6–8 gap is unchanged; novelty of the subclass results has not been established."
}
```

# Partial results

I use the standard convention that \(p,q\) are positive integers and graphs are finite and simple. The general planar problem is not resolved below.

Two self-contained results can be obtained.

**Theorem 1.** Let
\[
T_N=K_2\vee P_N,
\]
where the join adds every edge between the two graphs. Then \(T_N\) is a planar triangulation and
\[
\operatorname{cch}(T_N)\le 6.
\]
For every positive integer \(q\),
\[
\operatorname{cch}\!\left(T_{\,2q(6q-3)^2}\right)
   \ge 6-\frac3q.
\]
Consequently,
\[
\sup_N\operatorname{cch}(T_N)=6,
\]
and the sharp supremum for **3-degenerate planar graphs** is \(6\). The lower bound already holds for graphs of pathwidth \(3\).

**Theorem 2.** For \(n\ge18\), put \(k=\lfloor\sqrt n\rfloor\). Then
\[
\boxed{\quad
\frac{4k}{k+2}
\le \operatorname{cch}(K_{2,n})
\le \frac{4\sqrt n}{\sqrt n+\sqrt2}.
\quad}
\]
In particular,
\[
4-\operatorname{cch}(K_{2,n})=\Theta(n^{-1/2}).
\]
Thus the sharp supremum for 2-degenerate planar graphs is \(4\).

Theorem 1 gives an explicit, quantified realization of the lower-bound phenomenon in the question, rather than a stronger general lower bound. Theorem 2 improves the elementary degeneracy bound quantitatively on a particular planar family. I have not established that either result is new.

## 1. Preliminaries

Write \(\mathbb Z_p=\{0,\ldots,p-1\}\), with arithmetic modulo \(p\). When \(p\ge2q\), define the forbidden neighborhood of a color \(a\) by
\[
F(a)=\{a-q+1,\ldots,a+q-1\}\pmod p.
\]
It has
\[
r:=2q-1
\]
elements. A color at a neighbor of a vertex colored \(a\) must avoid \(F(a)\).

We will use two elementary facts.

### Greedy bound

If \(G\) is \(d\)-degenerate, \(d\ge1\), then lists of size at least
\[
d(2q-1)+1
\]
always admit a \((p,q)\)-coloring. Indeed, color in reverse degeneracy order; at most \(d\) already colored neighbors forbid at most \(d(2q-1)\) colors.

In particular,
\[
\operatorname{cch}(G)\le2d.
\tag{1}
\]
For this conclusion, every nonvacuous list assignment has \(p\ge2dq\ge2q\), so the forbidden-neighborhood description applies.

### A bad assignment gives a lower bound

If a graph has an uncolorable \((p,q)\)-list assignment in which every list has \(m\) colors, then
\[
\operatorname{cch}(G)\ge \frac mq.
\tag{2}
\]
This follows from monotonicity of circular \(t\)-choosability in \(t\). No assertion that the defining infimum is attained is needed.

## 2. A path obstruction

The following small gadget drives the lower bound \(6\).

**Lemma 3.** For any positive integer \(q\), let a path have vertices \(x_1,\ldots,x_{2q}\), in order, and give \(x_i\) the integer interval
\[
I_i=\{(i-1)(q-1),\ldots,(i+1)(q-1)\}.
\]
Each list has \(2q-1\) elements. There is no choice \(c_i\in I_i\) satisfying
\[
|c_{i+1}-c_i|\ge q
\qquad(1\le i<2q).
\]

**Proof.** For any choices from consecutive lists,
\[
c_i-c_{i+1}
\le (i+1)(q-1)-i(q-1)=q-1.
\]
Thus the separation condition would force
\[
c_{i+1}\ge c_i+q.
\]
Since \(c_1\ge0\), this gives
\[
c_{2q}\ge(2q-1)q.
\]
But the last list has maximum
\[
(2q+1)(q-1)=(2q-1)q-1,
\]
a contradiction. \(\square\)

Translating every list by the same integer preserves this obstruction. Moreover, it is also an obstruction to circular coloring whenever the translated lists are placed in a larger palette: the circular condition includes the necessary condition \(|c_{i+1}-c_i|\ge q\).

## 3. Proof of Theorem 1

### 3.1. Planarity and the upper bound

Write
\[
V(T_N)=\{u,v,w_1,\ldots,w_N\}.
\]
Its edges are \(uv\), all \(uw_i,vw_i\), and the path edges \(w_iw_{i+1}\).

To embed it, start with the triangle \(uvw_1\). Insert \(w_2\) into the face \(uvw_1\), then insert \(w_3\) into the face \(uvw_2\), and continue. Each insertion joins the new vertex to the three vertices of that face. This constructs exactly \(T_N\), proving planarity.

Deleting endpoints of the remaining path successively gives a 3-degeneracy ordering. Hence (1) yields
\[
\operatorname{cch}(T_N)\le6.
\tag{3}
\]

For \(N\ge2\), the bags
\[
\{u,v,w_i,w_{i+1}\},\qquad 1\le i<N,
\]
give a path decomposition of width \(3\). Since \(T_N\) contains \(K_4\), its pathwidth is exactly \(3\).

### 3.2. Explicit bad lists

Fix \(q\ge1\), and set
\[
m=6q-3,\qquad N=2qm^2,\qquad p=2q^2+22q.
\]
Give the two universal vertices the lists
\[
A=L(u)=\{q,\ldots,7q-4\},
\]
\[
B=L(v)=\{10q,\ldots,16q-4\}.
\]
Both have \(m\) elements.

Partition the path \(P_N\) into \(m^2\) consecutive blocks, each containing \(2q\) vertices, and index the blocks by pairs
\[
(a,b)\in A\times B.
\]
Let the vertices of the corresponding block be \(w_{a,b,1},\ldots,w_{a,b,2q}\).

For \(1\le i\le2q\), define
\[
J_i=
\{20q+(i-1)(q-1),\ldots,20q+(i+1)(q-1)\}.
\]
Give the block vertex the list
\[
L(w_{a,b,i})=F(a)\cup F(b)\cup J_i.
\tag{4}
\]

These three sets are pairwise disjoint. Indeed,
\[
F(a)\subseteq\{1,\ldots,8q-5\},
\]
\[
F(b)\subseteq\{9q+1,\ldots,17q-5\},
\]
whereas every \(J_i\) begins at or above \(20q\). All these sets lie inside \(\mathbb Z_p\), since the largest color used is
\[
20q+(2q+1)(q-1)=2q^2+19q-1<p.
\]
Thus every list in (4) has exactly
\[
3(2q-1)=m
\]
colors.

Suppose there were a coloring from these lists. Let
\[
c(u)=a,\qquad c(v)=b.
\]
Every vertex in block \((a,b)\) is adjacent to both \(u\) and \(v\). Consequently, its color must avoid \(F(a)\cup F(b)\), and therefore must belong to \(J_i\).

But the lists \(J_1,\ldots,J_{2q}\) are a common translate of the lists in Lemma 3. The path within this block cannot be colored. This contradiction proves that the assignment is uncolorable.

By (2),
\[
\operatorname{cch}(T_N)\ge\frac{6q-3}{q}
=6-\frac3q.
\]
Together with (3), this proves Theorem 1. \(\square\)

The construction has
\[
2+2q(6q-3)^2
\]
vertices. In particular, approaching \(6\) does not require large treewidth or a grid-like planar graph.

## 4. A counting lemma for two roots

For \(K_{2,n}\), once the colors of its two vertices in the smaller part are chosen, its remaining vertices can be colored independently. This permits a quantitative improvement over the degeneracy bound.

**Lemma 4.** Suppose
\[
3q\le m\le4q-2,\qquad p\ge2m.
\]
Let \(A,B\subseteq\mathbb Z_p\) be disjoint, and let \(S\subseteq\mathbb Z_p\) have \(m\) elements. Put
\[
r=2q-1,\qquad \delta=2r-m.
\]
Then the number of ordered pairs \((a,b)\in A\times B\) satisfying
\[
S\subseteq F(a)\cup F(b)
\tag{5}
\]
is at most
\[
\binom{\delta+2}{2}.
\tag{6}
\]

**Proof.** If no pair satisfies (5), there is nothing to prove. Otherwise fix one such pair.

The complement of two cyclic intervals of length \(r\) has at most two components and contains at least \(p-2r\) colors. Consequently, \(S\) has a gap of consecutive absent colors of length at least
\[
\left\lceil\frac{p-2r}{2}\right\rceil
\ge m-r=r-\delta.
\]
Moreover,
\[
\delta=4q-2-m\le q-2,
\]
so \(r-\delta>\delta\). Fix a maximal gap of \(S\) having length greater than \(\delta\).

For **any** pair satisfying (5), counting memberships in its two forbidden intervals gives
\[
|F(a)\setminus S|+|F(b)\setminus S|
=
2r-m-|F(a)\cap F(b)\cap S|
\le\delta.
\tag{7}
\]
Thus neither interval can contain the entire fixed gap.

Cut the cyclic ordering along this gap, and label the first and last elements of \(S\) by \(0\) and \(\ell\). Since \(m>r\), an interval of length \(r\) cannot cover both endpoints through the linear span of \(S\); it cannot cover both through the gap either, by (7). Therefore one forbidden interval covers \(0\), and the other covers \(\ell\).

Their integer lifts have the form
\[
[-h,r-1-h]
\quad\text{and}\quad
[\ell+k-r+1,\ell+k],
\]
for nonnegative integers \(h,k\). The first has \(h\) colors extending into the gap before \(0\), and the second has \(k\) extending into the gap after \(\ell\). Equation (7) implies
\[
h+k\le\delta.
\]

There are exactly \(\binom{\delta+2}{2}\) possible pairs \((h,k)\). Each determines the unordered pair of interval centers. Because \(A\cap B=\varnothing\), at most one ordering of these centers belongs to \(A\times B\). This proves (6). \(\square\)

The disjointness of \(A\) and \(B\) is important: it removes a potential factor of two in the count.

## 5. Proof of the upper bound in Theorem 2

Fix \(n\ge18\), and put
\[
t=\frac{4\sqrt n}{\sqrt n+\sqrt2},
\qquad
\varepsilon=4-t.
\]
Then \(t\ge3\) and
\[
\frac{n\varepsilon^2}{2}=t^2.
\tag{8}
\]

Consider any \(t\)-\((p,q)\)-list assignment on \(K_{2,n}\). Trim each list to size
\[
m=\lceil tq\rceil.
\]
Let \(A,B\) be the lists of the two vertices in the smaller part.

If \(A\cap B\ne\varnothing\), color both vertices with a common color. Every other vertex then has only \(2q-1\) forbidden colors, fewer than \(m\), so the coloring extends.

We may therefore assume \(A\cap B=\varnothing\), implying \(p\ge2m\). If
\[
m>4q-2,
\]
every pair of root colors extends, because two forbidden neighborhoods together have at most \(4q-2\) elements.

It remains to consider
\[
3q\le m\le4q-2.
\]
For a leaf with list \(S\), call a root-color pair bad if it satisfies
\[
S\subseteq F(a)\cup F(b).
\]
By Lemma 4, each leaf makes at most
\[
\binom{4q-m}{2}
\]
root pairs bad.

Put \(D=4q-m\). Since \(D\ge2\) and \(D\le\varepsilon q\), the total number of root pairs made bad by at least one leaf is at most
\[
n\binom D2
<
\frac{nD^2}{2}
\le
\frac{n\varepsilon^2q^2}{2}
=
t^2q^2
\le m^2,
\]
using (8).

There are \(m^2\) root-color pairs. Hence some pair is bad for no leaf. Choose that pair and then color every leaf independently. This proves circular \(t\)-choosability, including the asserted endpoint \(t\).

## 6. Proof of the lower bound in Theorem 2

We give an explicit bad assignment on \(K_{2,k^2}\) for every positive integer \(k\).

Set
\[
q=k+2,\qquad p=8kq.
\]
For \(0\le i<2k\), define the four-color block
\[
C_i=\{4qi+q,\ldots,4qi+q+3\}.
\]
Its common forbidden neighborhood is
\[
D_i:=\bigcap_{c\in C_i}F(c)
=\{4qi+4,\ldots,4qi+2q-1\}.
\]
Thus
\[
|D_i|=2q-4=2k.
\]
The blocks and their common forbidden neighborhoods are well separated and do not wrap around the palette.

Give the two roots the lists
\[
A=\bigcup_{i=0}^{k-1}C_i,
\qquad
B=\bigcup_{j=0}^{k-1}C_{k+j}.
\]
Both have \(4k\) colors.

Index the leaves by \((i,j)\in\{0,\ldots,k-1\}^2\), and give leaf \((i,j)\) the list
\[
D_i\cup D_{k+j}.
\]
Each leaf list also has \(4k\) colors.

In any purported coloring, the first root chooses a color from some \(C_i\), and the second chooses a color from some \(C_{k+j}\). Every color on the corresponding leaf’s list is forbidden by one of those root colors. Therefore no coloring exists, and
\[
\operatorname{cch}(K_{2,k^2})
\ge \frac{4k}{k+2}.
\]
If \(k^2\le n\), the same obstruction extends to \(K_{2,n}\) by assigning full-palette lists to the additional leaves. Taking \(k=\lfloor\sqrt n\rfloor\) proves the lower bound.

Combining both bounds gives the explicit deficit estimates
\[
\frac{4\sqrt2}{\sqrt n+\sqrt2}
\le
4-\operatorname{cch}(K_{2,n})
\le
\frac{8}{\lfloor\sqrt n\rfloor+2},
\]
which establish the claimed \(\Theta(n^{-1/2})\) behavior. \(\square\)

## 7. What remains unresolved

These arguments establish sharp bounds for two restricted planar classes:

- 2-degenerate planar graphs have supremum \(4\);
- 3-degenerate planar graphs have supremum \(6\), already witnessed by planar triangulations of pathwidth \(3\).

They do **not** control general planar graphs at \(6\), or at any constant below the supplied upper bound \(8\). The greedy extension used above stops at degree \(3\); the counting argument depends on the remaining vertices being independent after two root colors are fixed.

In particular, this attack provides neither:

1. an upper bound below \(8\) for all planar graphs, nor
2. a planar graph with circular choosability greater than \(6\).

Thus the general \(6\)–\(8\) gap stated in the question remains unchanged. The present-day literature status, and the novelty of these auxiliary estimates, have not been independently verified.