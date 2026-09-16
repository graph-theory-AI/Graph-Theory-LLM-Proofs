```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a constructive cyclic-order special case and an explicit fractional-colouring bound, but do not resolve arbitrary great-circle arrangements.",
  "would_publish": false,
  "caveats": "Novelty of these partial results is unchecked; neither the general conjecture nor 3-choosability is proved."
}
```

# Partial results

Let \(G=G(S)\) be the arrangement graph of \(n\) great circles satisfying the stated general-position assumption. I prove:

1. **A cyclic-order special case.** If the circles admit signed, indexed normal vectors \(v_0,\ldots,v_{n-1}\) such that
   \[
   \det(v_i,v_j,v_k)>0\qquad(0\le i<j<k<n),
   \tag{C}
   \]
   then \(G\) is \(3\)-colourable, with an explicit construction.

   This includes, for every \(n\), the circles with normals
   \[
   v_i=(1,t_i,t_i^2),\qquad t_0<t_1<\cdots<t_{n-1}.
   \]

2. **A general deletion and fractional-colouring bound.** For every arrangement with \(n\ge3\), there is an independent set of \(n-1\) vertices whose deletion leaves a \(2\)-degenerate graph. In fact, a uniformly covering family of such deletions gives
   \[
   \boxed{\displaystyle \chi_f(G)\le \min\left\{4,\frac{3n}{n-1}\right\}.}
   \tag{1}
   \]
   The deletion statement also holds with arbitrary lists of size three on the remaining vertices.

3. **An obstruction to a symmetry-based shortcut.** Even a five-circle arrangement in the cyclic class need not have an antipodally invariant \(3\)-colouring. Thus requiring the colouring to descend to the projective-plane quotient is too restrictive.

The supplied context already reports fractional bounds of the form \(3+O(1/n)\). I am not claiming an improvement over that literature without checking its constants, nor claiming novelty for the special case below.

The cases \(n\le2\) are immediate; throughout the arguments we take \(n\ge3\).

## 1. A general \(2\)-degenerate deletion

Recall that a graph is \(2\)-degenerate if its vertices admit an ordering in which every vertex has at most two later neighbours. Such a graph is \(3\)-choosable, by greedy colouring in reverse order.

### Lemma 1
For any \(C\in S\), the graph \(G-V(C)\) is \(2\)-degenerate.

**Proof.**
Deleting \(V(C)\) separates the remaining graph into the two open hemispheres bounded by \(C\).

Gnomonic projection maps either hemisphere to an affine plane. The other great circles become straight lines, and the remaining graph is the finite arrangement graph of these lines: its edges join consecutive intersection points along a line.

Choose a linear functional that is nonconstant on each line and takes distinct values at the intersection points. At an intersection of two lines, at most two incident edges lead to a larger value of the functional—at most one along each line. Ordering vertices by increasing value therefore proves \(2\)-degeneracy. Apply this independently in the two hemispheres. \(\square\)

Each circle \(C_i\) contains \(2(n-1)\) vertices, forming an even cycle. Let
\[
X_i^0,\ X_i^1
\]
be its two alternating vertex classes. Both have size \(n-1\).

### Lemma 2
For every \(i\) and \(\varepsilon\in\{0,1\}\), the set \(X_i^\varepsilon\) is independent in \(G\), and \(G-X_i^\varepsilon\) is \(2\)-degenerate.

**Proof.**
Two vertices on \(C_i\) cannot be adjacent along another circle. Indeed, such vertices would have to be the two antipodal intersections of that other circle with \(C_i\); for \(n\ge3\), they are not consecutive on either circle. Thus the alternating classes are independent in the full graph.

In \(G-X_i^\varepsilon\), every vertex of
\[
V(C_i)\setminus X_i^\varepsilon
\]
has lost its two neighbours along \(C_i\), so has degree at most two. Delete all these vertices first. What remains is \(G-V(C_i)\), which is \(2\)-degenerate by Lemma 1. \(\square\)

Consequently, for arbitrary three-element lists, deleting any \(X_i^\varepsilon\) leaves a list-colourable graph. Since
\[
|V(G)|=n(n-1),
\]
this also gives
\[
\alpha(G)\ge
\left\lceil\frac{(n-1)^2}{3}\right\rceil.
\tag{2}
\]

### Proof of the fractional bound

For each of the \(2n\) pairs \((i,\varepsilon)\), properly colour
\[
G-X_i^\varepsilon
\]
with three colours, producing three independent sets. Give each of these independent sets weight
\[
\frac{1}{2n-2}.
\]

Every arrangement vertex lies on exactly two circles. It therefore belongs to exactly two of the deletion sets \(X_i^\varepsilon\), and hence occurs in exactly \(2n-2\) of the coloured complements. Its total covering weight is exactly one.

The total weight is
\[
\frac{3(2n)}{2n-2}=\frac{3n}{n-1}.
\]
Also, colouring one independent deletion set with a fourth colour gives \(\chi(G)\le4\). This proves (1).

This argument stops strictly short of \(3\): the discarded vertices have not been incorporated into a common three-colour palette.

## 2. Constructive \(3\)-colouring under the cyclic-normal condition

### Theorem 3
If signed, indexed normals satisfy condition **(C)**, then the spherical arrangement graph is \(3\)-colourable.

We first identify its graph combinatorially, and then give the colouring.

### 2.1. Determining the intersection orders

For distinct \(i,j\), put
\[
q_{ij}=\frac{v_i\times v_j}{\|v_i\times v_j\|}.
\]
Thus \(q_{ji}=-q_{ij}\), and the ordered pairs \((i,j)\), \(i\ne j\), index all arrangement vertices.

Fix \(i\), and list the other indices in cyclic order:
\[
i+1,i+2,\ldots,i-1,
\]
with indices interpreted modulo \(n\). If \(j\) precedes \(k\) in this list, condition (C), together with invariance of a determinant under cyclic permutation, gives
\[
\det(v_i,v_j,v_k)>0.
\]
Moreover,
\[
v_i\cdot(q_{ij}\times q_{ik})
=
\frac{\|v_i\|^2\det(v_i,v_j,v_k)}
{\|v_i\times v_j\|\,\|v_i\times v_k\|}
>0.
\tag{3}
\]

Relative to the first point in the list, all subsequent points therefore have angular coordinates strictly between \(0\) and \(\pi\). Equation (3) orders those coordinates increasingly. Hence the cyclic order of all vertices on circle \(C_i\) is
\[
q_{i,i+1},q_{i,i+2},\ldots,q_{i,i-1},
q_{i+1,i},q_{i+2,i},\ldots,q_{i-1,i}.
\tag{4}
\]

Relabel
\[
q_{i,i+k}\longleftrightarrow(i,k),
\qquad i\in\mathbb Z_n,\quad 1\le k\le n-1.
\]

More generally, define \(B(n,h)\), for \(h\ge2\), to have vertices
\[
(i,k),\qquad i\in\mathbb Z_n,\quad 1\le k\le h,
\]
and edges
\[
(i,k+1)(i,k),\qquad (i,k+1)(i+1,k)
\quad(1\le k<h),
\tag{5}
\]
together with the two boundary cycles
\[
(i,1)(i+1,1),\qquad(i,h)(i+1,h).
\tag{6}
\]

Reading consecutive vertices in (4) gives exactly
\[
G\cong B(n,n-1).
\tag{7}
\]

### 2.2. Row formulation

Write a colouring of row \(k\) as a cyclic word
\[
f_k=(f_k(i))_{i\in\mathbb Z_n}
\]
over \(\{0,1,2\}\). By (5)–(6), a proper colouring is precisely a sequence satisfying
\[
f_{k+1}(i)\notin\{f_k(i),f_k(i+1)\}
\quad\text{for every }i,k,
\tag{8}
\]
whose first and last rows are proper colourings of \(C_n\).

Call a pair of rows \(f,g\) satisfying (8) a **legal transition**, and write \(f\to g\).

### 2.3. Even \(n\)

Here \(n-1\) is odd. Set
\[
f_k(i)=
\begin{cases}
i\bmod2,&k\text{ odd},\\
2,&k\text{ even}.
\end{cases}
\]

Every edge between consecutive rows joins colour \(2\) to colour \(0\) or \(1\). Both boundary rows alternate \(0,1\), and these are proper cyclic words because \(n\) is even.

Thus \(B(n,n-1)\) is \(3\)-colourable for even \(n\).

### 2.4. The case \(n=3\)

For \(k=1,2\), set
\[
f_k(i)=i+2k\pmod3.
\]
The boundary cycles are properly coloured, and the two differences required in (8) are nonzero modulo three.

### 2.5. Odd \(n\ge5\)

We first construct a four-row colouring. In the following words, exponents denote repetition of symbols or blocks:
\[
\begin{aligned}
a&=(01)^{(n-1)/2}\,2,\\
b&=2^{\,n-2}\,01,\\
c&=0^{\,n-3}\,120,\\
d&=(12)^{(n-3)/2}\,012.
\end{aligned}
\tag{9}
\]
All four words have length \(n\), and \(a,d\) properly colour \(C_n\).

The transitions
\[
a\to b\to c\to d
\tag{10}
\]
are legal:

- In \(a\), the first \(n-2\) adjacent pairs alternate \(01,10\), forcing colour \(2\) in \(b\); the last two pairs are \(12,20\), forcing \(0,1\).
- In \(b\), the first \(n-3\) adjacent pairs are \(22\), allowing colour \(0\) in \(c\); the final three pairs \(20,01,12\) force \(1,2,0\).
- In \(c\), the initial \(00\) pairs allow the alternating \(1,2\) block in \(d\). The subsequent pairs \(01,12,20\) force \(2,0,1\), and the final cyclic pair \(00\) allows the final \(2\).

It remains to increase the height from four to \(n-1\).

Let \(S\) denote cyclic shift:
\[
(Sf)(i)=f(i+1).
\]
A useful elementary observation is
\[
f\to g\quad\Longrightarrow\quad g\to Sf.
\tag{11}
\]
Indeed, \(f(i+1)\) differs from both \(g(i)\) and \(g(i+1)\), by legality at positions \(i\) and \(i+1\).

Put
\[
r=\frac{n-5}{2}.
\]
Use the row sequence
\[
a,b,\ Sa,Sb,\ \ldots,\ S^r a,S^r b,\ S^r c,S^r d.
\tag{12}
\]
Every transition is legal by (10), (11), and shift invariance. The first and last rows properly colour \(C_n\). The number of rows is
\[
2(r+1)+2=2r+4=n-1.
\]
Thus (12) properly colours \(B(n,n-1)\).

This covers every parity and completes the proof of Theorem 3. \(\square\)

### Explicit geometric examples

For
\[
v_i=(1,t_i,t_i^2),\qquad t_0<\cdots<t_{n-1},
\]
the Vandermonde determinant is
\[
\det(v_i,v_j,v_k)
=(t_j-t_i)(t_k-t_i)(t_k-t_j)>0
\qquad(i<j<k).
\]
Thus these normals satisfy (C), and no three corresponding great circles meet at a point. The theorem gives an explicit \(3\)-colouring for every such arrangement.

## 3. Why antipodally invariant colouring is too strong

The preceding special case already exhibits an obstruction to descending the colouring to the projective plane.

Take \(n=5\) in the cyclic-normal class, and let \(H\) be the quotient of \(G\) obtained by identifying antipodal vertices. Its vertices are the unordered circle pairs. With indices modulo five, write
\[
a_i=\{i,i+1\},\qquad b_i=\{i,i+2\}.
\]

The cyclic orders (4) give:

- the cycle \(a_0a_1a_2a_3a_4a_0\);
- the triangles
  \[
  a_i a_{i+1} b_i;
  \]
- the cycle
  \[
  b_0b_2b_4b_1b_3b_0.
  \]

Suppose \(H\) had a proper \(3\)-colouring. A properly \(3\)-coloured \(5\)-cycle has colour multiplicities \(2,2,1\). After rotating indices and permuting colours, its \(a\)-cycle therefore has colours
\[
(0,1,0,1,2).
\]
The first three displayed triangles force
\[
c(b_0)=c(b_1)=c(b_2)=2.
\]
But \(b_0b_2\) is an edge, a contradiction.

Hence \(H\) is not \(3\)-colourable. Equivalently, this spherical arrangement has **no antipodally invariant \(3\)-colouring**.

This is **not** a counterexample to the conjecture: its spherical graph is \(3\)-colourable by Theorem 3. It only rules out imposing antipodal invariance as a universal simplification.

## 4. The remaining gap

The general conjecture is not established by these arguments:

- The explicit colouring uses the intersection orders forced by condition (C). No argument here handles arbitrary great-circle intersection orders.
- The universal deletion lemma gives \(3\)-choosability only **after deleting vertices**; it does not supply an extension over those vertices.
- The fractional bound remains strictly above \(3\), and fractional colouring would not by itself settle ordinary \(3\)-colourability.
- Antipodal identification cannot close the gap, since its quotient can already require more than three colours.

Thus the outcome is a fully proved constructive special case and a general deletion/fractional bound, not a proof or counterexample for the original conjecture.