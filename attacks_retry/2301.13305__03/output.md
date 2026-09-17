```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact maximum is determined for n ≤ 342, and a modulus-91 construction improves the supplied lower-bound exponent to 0.1383182203.",
  "would_publish": false,
  "caveats": "The asymptotic order remains unresolved; novelty of these partial results has not been checked."
}
```

# 1. Results

Let \(M(n)\) be the maximum cardinality of an admissible family in \(\mathbb F_2^n\), where admissibility means that no difference of two members is the indicator of an interval of positive cube length.

The following exact values hold:
\[
\boxed{
M(n)=
\begin{cases}
2^{n-1},&1\le n\le7,\\[2mm]
93\,2^{n-8},&8\le n\le26,\\[2mm]
11\,2^{n-5},&27\le n\le342.
\end{cases}}
\tag{1}
\]
At the next breakpoint,
\[
\boxed{M(n)\le 5\,2^{n-4}\qquad(n\ge343).}
\tag{2}
\]

For general \(n\), put
\[
\beta=\frac{\log(13/2)}{3\log91}
      =0.1383182203\ldots.
\]
There is an explicit construction, using binary linear subspaces, giving
\[
\boxed{
M(n)\ge \frac{11}{156}\,
\frac{2^n}{(n+1)^\beta}.
}
\tag{3}
\]
This improves the exponent \(0.145141\ldots\) in the supplied attempt.

There is also a useful unconditional comparison with the ordinary cube-difference-free problem. Define
\[
r_3(N)=\max\bigl\{|A|:A\subseteq\{0,\ldots,N-1\},\
|a-b|\ne k^3\text{ for distinct }a,b\in A\bigr\}.
\]
Then, with \(N=n+1\),
\[
\boxed{
\frac{r_3(N)}{4N(1+\log N)}\,2^n
\le M(n)
\le \frac{r_3(N)}{N}\,2^n.
}
\tag{4}
\]
In fact, the lower bound in (4) can also be achieved by a linear family.

The boundary-map and linear-coloring reductions from the previous attempt are valid; they are proved again below. The additional ingredients are odd-cycle homomorphic equivalences for (1), and a composite-modulus construction for (3).

---

# 2. Boundary graphs and their binary Cayley graphs

For a finite graph \(H\) with vertex set \(V\), let
\[
E_V=\left\{z\in\mathbb F_2^V:\sum_{v\in V}z_v=0\right\},
\]
and define
\[
\mathcal C(H)=
\operatorname{Cay}\!\left(
E_V,\{e_u+e_v:uv\in E(H)\}
\right).
\]
Thus \(\mathcal C(H)\) has \(2^{|V|-1}\) vertices.

Let \(D_N\) be the graph on \(\{0,\ldots,n\}\), where \(N=n+1\), whose edges have positive cube difference:
\[
ij\in E(D_N)\quad\Longleftrightarrow\quad |i-j|=k^3
\]
for some positive integer \(k\).

The linear boundary map
\[
\partial(x_1,\ldots,x_n)
=(x_1,x_1+x_2,\ldots,x_{n-1}+x_n,x_n)
\]
is an isomorphism from \(\mathbb F_2^n\) to \(E_{\{0,\ldots,n\}}\). Moreover,
\[
\partial\mathbf 1_{[a,b]}=e_{a-1}+e_b.
\]
Consequently,
\[
\boxed{M(n)=\alpha(\mathcal C(D_N)).}
\tag{5}
\]

## 2.1. A homomorphism principle

A graph homomorphism \(f:H\to K\) induces a linear map
\[
L_f:E_{V(H)}\longrightarrow E_{V(K)},\qquad
L_f(z)=\sum_{v\in V(H)}z_v e_{f(v)}.
\]
Every generator \(e_u+e_v\), with \(uv\in E(H)\), maps to the generator
\[
e_{f(u)}+e_{f(v)}.
\]
Hence
\[
\mathcal C(H)\longrightarrow\mathcal C(K).
\]

Write
\[
\rho(H)=\frac{\alpha(\mathcal C(H))}{2^{|V(H)|-1}}.
\]
Then
\[
H\longrightarrow K\quad\Longrightarrow\quad \rho(H)\ge\rho(K).
\tag{6}
\]

To see this directly, take a maximum independent set \(I\) of \(\mathcal C(K)\). For each \(z\in E_{V(K)}\), the preimage
\[
L_f^{-1}(I+z)
\]
is independent in \(\mathcal C(H)\). Averaging its cardinality over \(z\) gives density exactly \(\rho(K)\).

In particular, if \(K\) is a subgraph of \(H\) and \(H\to K\), then
\[
\boxed{\rho(H)=\rho(K).}
\tag{7}
\]

---

# 3. Exact values through \(n=342\)

## 3.1. The binary Cayley graph of an odd cycle

For a cycle \(C_m\), choose the edge-vectors of a spanning path as a basis of its even-weight space. The remaining edge-vector is the sum of that basis. Thus
\[
\mathcal C(C_m)\cong
\operatorname{Cay}\!\left(
\mathbb F_2^{m-1},
\{e_1,\ldots,e_{m-1},\mathbf 1\}
\right).
\]

When \(m=2s+1\) is odd, this is the \(2s\)-dimensional cube with antipodal edges added.

### Lemma
For \(s\ge1\),
\[
\boxed{
\alpha(\mathcal C(C_{2s+1}))
=\sum_{j=0}^{s-1}\binom{2s}{j}.
}
\tag{8}
\]

### Proof

On \(\mathbb F_2^{2s}\), define the involution
\[
\Phi(x)=
\begin{cases}
x,& |x|\text{ is even},\\
x+\mathbf 1,& |x|\text{ is odd}.
\end{cases}
\]
Complementation preserves weight parity because \(2s\) is even.

If \(x,y\) have the same parity, then
\[
d(\Phi(x),\Phi(y))=d(x,y).
\]
If they have opposite parity, then
\[
d(\Phi(x),\Phi(y))=2s-d(x,y).
\]
Therefore a family avoids distances \(1\) and \(2s\) if and only if its image under \(\Phi\) has diameter at most \(2s-2\).

Now use the classical binary diametric theorem: a family in \(\mathbb F_2^d\) of diameter at most \(2r<d\) has cardinality at most
\[
\sum_{j=0}^r\binom dj,
\]
with equality attained by a Hamming ball of radius \(r\). Applying this with \(d=2s\) and \(r=s-1\) proves (8). \(\square\)

In particular,
\[
\alpha(\mathcal C(C_9))=1+8+28+56=93,
\]
\[
\alpha(\mathcal C(C_7))=1+6+15=22,
\]
and
\[
\alpha(\mathcal C(C_5))=1+4=5.
\tag{9}
\]

The binary diametric theorem is the only external extremal theorem needed for these finite exact values.

## 3.2. The range \(1\le n\le7\)

Only length \(1\) is forbidden. Thus the forbidden-difference graph is the ordinary \(n\)-cube, and
\[
M(n)=2^{n-1}.
\]

## 3.3. The range \(8\le n\le26\)

The available cube distances are \(1\) and \(8\). Reduction modulo \(9\) gives a homomorphism
\[
D_N\longrightarrow C_9,
\]
since both distances are congruent to \(\pm1\pmod9\).

Conversely, the vertices \(0,\ldots,8\), with the successive distance-\(1\) edges and the closing distance-\(8\) edge, contain a \(C_9\). By (7),
\[
\rho(D_N)=\rho(C_9)=\frac{93}{256}.
\]
Hence
\[
M(n)=93\,2^{n-8}.
\]

## 3.4. The range \(27\le n\le342\)

The positive cube roots involved are at most \(6\). Every nonzero cube modulo \(7\) is \(1\) or \(-1\), so reduction modulo \(7\) gives
\[
D_N\longrightarrow C_7.
\]

There is also a \(7\)-cycle in \(D_N\):
\[
0,\ 1,\ 2,\ 3,\ 11,\ 19,\ 27,\ 0.
\]
Its edge lengths are
\[
1,1,1,8,8,8,27.
\]
Therefore
\[
\rho(D_N)=\rho(C_7)=\frac{22}{64}=\frac{11}{32},
\]
which proves
\[
M(n)=11\,2^{n-5}.
\]

These equalities also give explicit extremal families: pull back a maximum independent set of the appropriate folded cube under the linear map induced by reduction modulo \(9\) or \(7\).

## 3.5. The breakpoint \(n=343\)

The identity
\[
343=216+125+1+1
\]
gives a \(5\)-cycle in \(D_N\), on the vertices
\[
0,\ 1,\ 2,\ 127,\ 343,\ 0.
\]
Thus, for every \(n\ge343\),
\[
\rho(D_N)\le \rho(C_5)=\frac5{16}.
\]
This proves (2). It does not, by itself, prove equality.

---

# 4. Linear families and a logarithmic-factor comparison

Let \(M_{\mathrm{lin}}(n)\) denote the maximum cardinality of an admissible binary linear subspace.

For \(0\le j\le n\), put
\[
p_j=\mathbf 1_{\{1,\ldots,j\}},\qquad p_0=0.
\]

## 4.1. Exact linear-family formula

We have
\[
\boxed{
M_{\mathrm{lin}}(n)
=2^{\,n-\lceil\log_2\chi(D_N)\rceil}.
}
\tag{10}
\]

Indeed, if \(C\le\mathbb F_2^n\) is admissible and has codimension \(d\), color vertex \(j\) of \(D_N\) by \(p_j+C\). Adjacent vertices receive different colors, because their difference is a forbidden interval vector. Thus
\[
\chi(D_N)\le 2^d.
\]

Conversely, label the colors of a proper coloring of \(D_N\) by distinct vectors
\[
c_0,\ldots,c_n\in\mathbb F_2^d,
\qquad d=\lceil\log_2\chi(D_N)\rceil.
\]
Define
\[
T(e_j)=c_{j-1}+c_j,\qquad 1\le j\le n.
\]
For every interval,
\[
T(\mathbf 1_{[a,b]})=c_{a-1}+c_b.
\]
This is nonzero whenever the interval has cube length. Hence \(\ker T\) is admissible and has codimension at most \(d\). The preceding lower bound on codimension forces equality.

In particular,
\[
M_{\mathrm{lin}}(n)\ge \frac{2^n}{2\chi(D_N)}.
\tag{11}
\]

## 4.2. Fractional-chromatic upper bound

The map \(j\mapsto p_j\) is a graph homomorphism
\[
D_N\longrightarrow\mathcal C(D_N).
\]
Fractional chromatic number is monotone under graph homomorphisms, and for a finite vertex-transitive graph \(G\),
\[
\chi_f(G)=\frac{|V(G)|}{\alpha(G)}.
\]
The latter identity follows by assigning equal weights to all translates of a maximum independent set.

Consequently,
\[
\boxed{
M(n)\le \frac{2^n}{\chi_f(D_N)}
\le \frac{r_3(N)}{N}\,2^n.
}
\tag{12}
\]

The second inequality uses \(\chi_f(D_N)\ge N/r_3(N)\).

## 4.3. Linear families are within a logarithmic factor of optimal

For every graph \(H\) on \(N\) vertices,
\[
\chi(H)\le (1+\log N)\chi_f(H).
\tag{13}
\]

Here is the standard greedy-cover argument. Repeatedly choose an independent set covering as many uncovered vertices as possible. If a step covers \(s\) new vertices, charge each of them \(1/s\). For any independent set \(I\), its vertices, ordered by when they are covered, receive total charge at most
\[
1+\frac12+\cdots+\frac1{|I|}\le1+\log N.
\]
Multiplying this inequality by the weights of an optimal fractional coloring and summing bounds the total number of greedy color classes by the right side of (13).

Combining (11)–(13),
\[
M_{\mathrm{lin}}(n)
\ge
\frac{2^n}{2(1+\log N)\chi_f(D_N)}
\ge
\frac{M(n)}{2(1+\log N)}.
\tag{14}
\]
Thus nonlinear families can improve on optimal linear families by at most a logarithmic factor.

## 4.4. Comparison with \(r_3(N)\)

Let \(A\subseteq\{0,\ldots,N-1\}\) be cube-difference-free and have size \(r=r_3(N)\). For
\[
-(N-1)\le t\le N-1,
\]
the set
\[
(A+t)\cap\{0,\ldots,N-1\}
\]
is independent in \(D_N\). Each vertex lies in exactly \(r\) of these translated sets. Assigning weight \(1/r\) to every translate gives
\[
\chi_f(D_N)\le \frac{2N-1}{r}.
\tag{15}
\]

Using (11), (13), and (15),
\[
M(n)\ge M_{\mathrm{lin}}(n)
\ge
\frac{r}{2(2N-1)(1+\log N)}\,2^n
\ge
\frac{r}{4N(1+\log N)}\,2^n.
\]
Together with (12), this proves (4).

This is an unconditional finite-\(n\) comparison, not an assumption about the asymptotics of \(r_3(N)\).

---

# 5. A modulus-\(91\) construction

The improvement over the supplied modulus-\(7\) construction comes from using a composite modulus. Independent sets in the relevant product graph can be larger than products of independent sets in its factors.

## 5.1. The finite residue graph

Let \(H\) be the graph on \(\mathbb Z_{91}\) in which distinct residues are adjacent when their difference is a cube modulo \(91\).

By the Chinese remainder theorem,
\[
\mathbb Z_{91}\cong\mathbb Z_7\times\mathbb Z_{13}.
\]
The nonzero cubes modulo \(7\) and \(13\) are, respectively,
\[
\{\pm1\},\qquad \{\pm1,\pm5\}.
\]
Thus \((i,j)\) and \((i',j')\) are adjacent precisely when
\[
(i'-i,j'-j)\in
\bigl(\{0,\pm1\}\times\{0,\pm1,\pm5\}\bigr)
\setminus\{(0,0)\}.
\tag{16}
\]

Define
\[
(t_0,t_1,\ldots,t_6)=(0,2,4,6,8,1,7)
\quad\text{in }\mathbb Z_{13},
\]
and set
\[
A=\bigcup_{i\in\mathbb Z_7}
\{(i,t_i),(i,t_i+4)\}.
\tag{17}
\]
This is an independent set of size \(14\).

To check this:

* In one row, the two second coordinates differ by \(4\), which is not a nonzero cube modulo \(13\).
* Nonadjacent rows in \(C_7\) cannot produce an edge of \(H\).
* For consecutive rows,
  \[
  t_{i+1}-t_i\in\{2,6\}\pmod{13},
  \]
  including the wraparound \(i=6\).
  Cross-row second-coordinate differences therefore lie in
  \[
  \{2,6,-2\}\quad\text{or}\quad\{6,10,2\},
  \]
  none of which belongs to \(\{0,\pm1,\pm5\}\).

For a certificate directly in \(\mathbb Z_{91}\), the set in (17) is
\[
A=\{0,5,10,15,20,25,30,40,45,56,60,71,76,86\}.
\tag{18}
\]

## 5.2. Exact multicoloring of the residue graph

Translate \(A\) by all \(13\) elements in the second coordinate. Each vertex of \(H\) belongs to exactly two of these independent sets. Thus they give a \(2\)-fold coloring with \(13\) colors.

More explicitly, a vertex \((i,j)\) belongs to the translates whose labels are
\[
j-t_i,\qquad j-t_i-4.
\tag{19}
\]
These pairs are the edges of the \(13\)-cycle on \(\mathbb Z_{13}\) with step \(4\). A vertex cover of that cycle has size \(7\). Restricting to the corresponding seven translates still covers every vertex, giving an ordinary \(7\)-coloring.

It follows that the \(h\)-fold chromatic number satisfies
\[
\chi_h(H)\le \left\lceil\frac{13h}{2}\right\rceil.
\tag{20}
\]
Indeed, write \(h=2q+r\), where \(r\in\{0,1\}\), and use \(q\) disjoint copies of the \(2\)-fold coloring and, if needed, one \(7\)-coloring.

In fact, equality holds in (20). Here is a short verification.

Let
\[
G=\operatorname{Cay}(\mathbb Z_{13},\{\pm1,\pm5\}).
\]
Then \(\alpha(G)=4\). The set \(\{0,2,4,6\}\) shows the lower bound. For the upper bound, an independent set of size five would have five cyclic gaps, each at least \(2\), summing to \(13\). The possibilities, up to order, are
\[
(5,2,2,2,2),\qquad
(4,3,2,2,2),\qquad
(3,3,3,2,2).
\]
The first has a forbidden gap \(5\); each of the other two necessarily has consecutive gaps \(3,2\), again producing forbidden difference \(5\).

Now let \(S\) be independent in \(H\), and let \(S_i\) be its second coordinates in row \(i\). For consecutive rows, \(S_i\) and \(S_{i+1}\) are disjoint and their union is independent in \(G\). Therefore
\[
|S_i|+|S_{i+1}|\le4.
\]
Summing around the seven rows gives \(|S|\le14\). Thus
\[
\alpha(H)=14.
\]
Every color in an \(h\)-fold coloring covers at most \(14\) vertices, so at least
\[
\left\lceil\frac{91h}{14}\right\rceil
=\left\lceil\frac{13h}{2}\right\rceil
\]
colors are necessary. Hence
\[
\boxed{\chi_h(H)=\left\lceil\frac{13h}{2}\right\rceil.}
\tag{21}
\]

## 5.3. Digit sampling

Set
\[
t=\left\lceil\log_{91^3}N\right\rceil.
\]
Write each \(x\in\{0,\ldots,N-1\}\) in base \(91\):
\[
x=\sum_{\nu=0}^{3t-1}d_\nu(x)91^\nu.
\]
Keep every third digit:
\[
\pi(x)=\bigl(d_0(x),d_3(x),\ldots,d_{3t-3}(x)\bigr).
\]

Let \(L_t\) be the graph on \(\mathbb Z_{91}^t\) in which two strings are adjacent when, at their first differing coordinate read from low to high, their entries are adjacent in \(H\). Thus \(L_t\) is the \(t\)-fold lexicographic power of \(H\).

I claim
\[
D_N\longrightarrow L_t.
\tag{22}
\]

Suppose \(y-x=k^3\). Write
\[
s=\min\{v_7(k),v_{13}(k)\}.
\]
Since \(91\) is squarefree, the exact exponent of \(91\) dividing \(k^3\) is \(3s\). Consequently, the base-\(91\) digits of \(x,y\) agree below position \(3s\), and their digit difference at position \(3s\) is
\[
\left(\frac{k}{91^s}\right)^3\pmod{91}.
\]
This residue is nonzero and is a cube modulo \(91\), hence is an edge difference of \(H\). This proves (22).

## 5.4. Counting colors and constructing the code

Put \(h_t=\chi(L_t)\), with \(h_0=1\). For lexicographic products,
\[
\chi(G[K])=\chi_{\chi(K)}(G),
\]
because adjacent outer vertices must receive disjoint palettes, each large enough to color \(K\). Using (21),
\[
h_t=\left\lceil\frac{13}{2}h_{t-1}\right\rceil.
\]
The rounding error is at most \(1/2\), so
\[
h_t\le
\left(\frac{13}{2}\right)^t
+\frac12\sum_{j=0}^{t-1}\left(\frac{13}{2}\right)^j
=
\frac{12}{11}\left(\frac{13}{2}\right)^t-\frac1{11}.
\]
Since \(t<\log_{91^3}N+1\),
\[
\chi(D_N)\le h_t
<
\frac{78}{11}N^\beta,
\qquad
\beta=\frac{\log(13/2)}{3\log91}.
\tag{23}
\]

Finally, (10) gives
\[
M(n)\ge
2^{n-\lceil\log_2\chi(D_N)\rceil}
\ge
\frac{2^n}{2\chi(D_N)}
\ge
\frac{11}{156}\frac{2^n}{N^\beta}.
\]
This proves (3).

All parts of this construction are specified explicitly: the residue independent set, its translated colorings, the recursive palettes, and the linear map from a coloring to a code.

---

# 6. What remains unresolved

The exact asymptotic maximum is not determined here.

The polynomial-difference theorem supplied in the question gives
\[
r_3(N)=o(N).
\]
Together with (4), this recovers \(M(n)=o(2^n)\). The quantitative gap remains substantial:
\[
\frac{2^n}{n^{0.1383182203\ldots}}
\ \lesssim\ M(n)=o(2^n).
\]

The progress is:

* exact unrestricted values for every \(n\le342\);
* an explicit improved polynomial lower bound;
* an unconditional logarithmic-factor comparison with cube-difference-free density;
* and a logarithmic-factor bound on the possible advantage of nonlinear families.

The argument does not determine the unrestricted maximum for \(n\ge343\), provide a matching polynomial upper bound, or establish optimality of the modulus-\(91\) exponent.