```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove M_{F_{2c}}(5)=5 and M_{F_{2c}}(n)=2^{n-2} for every odd n>=11 such that 217 does not divide n-2.",
  "would_publish": false,
  "caveats": "The cases n=7,9 and n=219+434k remain outside this result; novelty has not been externally checked."
}
```

# 1. Result

Write \(M_{2c}(n)=M_{F_{2c}}(n)\). Graphs are simple, labeled, and have a common vertex set. A family is a \(2\)-connected graph-code if the symmetric difference of every two distinct members is \(2\)-connected.

I prove the following partial resolution.

**Theorem.**
1. \(M_{2c}(5)=5\).
2. For every odd \(n\ge 11\) such that \(217\nmid n-2\),
   \[
   M_{2c}(n)=2^{n-2}.
   \]

Thus the upper bound is attained for every odd \(11\le n\le217\), and, more generally, for all odd \(n\ge11\) outside the progression
\[
n=219+434k,\qquad k\ge0.
\]

The main change from the supplied attempt is to use **only even-weight midpoint vectors**, together with an independent bit controlling the two additional vertices. This removes the restriction \(n-2\equiv1\pmod4\). A component analysis using Kneser’s sumset theorem then removes the primality restriction.

All needed circulant calculations and the five-vertex argument are verified below. No computational results are assumed.

---

# 2. The upper bound

For a graph \(G\) and a vertex \(v\), let
\[
\sigma_v(G)\in\mathbb F_2^{n-1}
\]
be the vector of edges incident with \(v\).

If \(\mathcal C\) is a \(2\)-connected graph-code, then for distinct \(G,H\in\mathcal C\),
\[
d_H(\sigma_v(G),\sigma_v(H))
=\deg_{G\triangle H}(v)\ge2.
\]
In particular, the star projection is injective, and its image is an independent set in the hypercube \(Q_{n-1}\). A perfect matching of that hypercube gives
\[
|\mathcal C|\le 2^{n-2}.
\tag{2.1}
\]

There is a useful equality observation. The only independent sets of size \(2^{m-1}\) in \(Q_m\) are its parity classes: such an independent set accounts for every edge of the regular hypercube, so its complement is also independent, and connectedness gives the unique bipartition. Consequently, in a code attaining (2.1), every pairwise difference is Eulerian.

The construction below has precisely this property.

---

# 3. Two circulant ingredients

Throughout the construction, let
\[
m=2r+1\ge9,\qquad \mathbb E_m=\left\{x\in\mathbb F_2^m:\sum_i x_i=0\right\}.
\]
Coordinates are indexed by \(\mathbb Z_m\).

Consider the two sets
\[
\begin{aligned}
A^{(0)}&=\{0,1,\ldots,r-1,r+1\},\\
A^{(1)}&=\{0,2,3,\ldots,r,m-1\}.
\end{aligned}
\tag{3.1}
\]
For either choice \(A\), define the circulant matrix
\[
P_{i,c}=\mathbf1_A(i-c),\qquad i,c\in\mathbb Z_m.
\tag{3.2}
\]

We will use \(A^{(0)}\) when \(7\nmid m\), and \(A^{(1)}\) when \(31\nmid m\).

## Lemma 3.1

Both sets in (3.1) have the following properties.

1. They contain \(0\) and exactly one element of each pair \(\{t,-t\}\), \(t\ne0\). In particular,
   \[
   P+P^T=J+I,\qquad |A|=r+1.
   \tag{3.3}
   \]

2. For every nonzero \(t\in\mathbb Z_m\),
   \[
   |A\triangle(A+t)|\ge4.
   \tag{3.4}
   \]

3. If \(1<d<m\) divides \(m\), put \(q=m/d\). For every residue \(h\pmod d\), the slice
   \[
   A_{d,h}:=\{j\in\mathbb Z_q:h+dj\in A\}
   \tag{3.5}
   \]
   is a cyclic interval of length either \((q-1)/2\) or \((q+1)/2\).
   Convolution by this slice is injective on \(\mathbb E_q\).

In addition:

4. For \(A=A^{(0)}\), \(P\) and \(P^T\) are injective on \(\mathbb E_m\) if \(7\nmid m\).
5. For \(A=A^{(1)}\), \(P\) and \(P^T\) are injective on \(\mathbb E_m\) if \(31\nmid m\).

### Proof of properties 1 and 2

Property 1 follows directly from the descriptions of the sets: \(A^{(0)}\) reverses the choice from \(\{r,-r\}\), while \(A^{(1)}\) reverses the choice from \(\{1,-1\}\).

For property 2, put \(I_0=\{0,1,\ldots,r\}\). Each \(A\) is obtained from \(I_0\) by deleting one point and adding one point.

Since
\[
|A\cap(A+t)|=|A\cap(A-t)|,
\]
it suffices to consider \(t=d\) with \(1\le d\le r\). We have
\[
|I_0\cap(I_0+d)|=r+1-d.
\]
The modification can add at most two points to this intersection, so, for \(d\ge4\),
\[
|A\cap(A+d)|\le r+3-d\le r-1.
\]
For the remaining shifts, direct counting gives, using \(r\ge4\),
\[
\begin{array}{c|ccc}
 &d=1&d=2&d=3\\ \hline
A^{(0)}&r-1&r-1&r-2\\
A^{(1)}&r-1&r-2&r-2.
\end{array}
\]
Thus every nonzero shift has intersection at most \(r-1\). Since \(|A|=r+1\), this proves (3.4). ∎

### Proof of property 3

Write
\[
q=2k+1,\qquad d=2h_0+1.
\]
Then
\[
r=dk+h_0.
\]
The slices of \(I_0=\{0,\ldots,r\}\) are
\[
(I_0)_{d,h}=
\begin{cases}
\{0,\ldots,k\},&0\le h\le h_0,\\
\{0,\ldots,k-1\},&h_0<h<d.
\end{cases}
\tag{3.6}
\]

For \(A^{(0)}\), deleting \(r\) removes the last point of slice \(h_0\), and adding \(r+1\) appends a point to slice \(h_0+1\). All slices remain intervals of length \(k\) or \(k+1\).

For \(A^{(1)}\), deleting \(1\) changes slice \(1\) from
\[
\{0,\ldots,k\}\quad\text{to}\quad\{1,\ldots,k\}.
\]
Adding \(m-1\) changes slice \(d-1\) from
\[
\{0,\ldots,k-1\}\quad\text{to}\quad\{-1,0,\ldots,k-1\}.
\]
Again, all slices are cyclic intervals of the required lengths.

It remains to check injectivity. A cyclic interval of length \(L\), up to a translate, has convolution polynomial
\[
F_L(z)=1+z+\cdots+z^{L-1},
\]
where \(L=(q-1)/2\) or \((q+1)/2\). In either case,
\[
\gcd(L,q)=1.
\]
For every nontrivial \(q\)-th root of unity \(\alpha\) over an algebraic closure of \(\mathbb F_2\),
\[
F_L(\alpha)=\frac{1+\alpha^L}{1+\alpha}\ne0.
\]
Because \(q\) is odd, \(z^q-1\) has distinct roots. If an even-weight vector is in the kernel of this convolution, its polynomial vanishes at all nontrivial \(q\)-th roots, and its even weight gives vanishing at \(1\) as well. The vector is therefore zero. ∎

### Proof of properties 4 and 5

For a circulant polynomial \(f\), it is enough to show that \(f\) has no nontrivial \(m\)-th root of unity as a zero. Indeed, an element of \(\mathbb E_m\) already vanishes at \(1\). The transpose is handled by replacing each root by its inverse.

For \(A^{(0)}\), the polynomial is
\[
f_0(z)=1+z+\cdots+z^{r-1}+z^{r+1}.
\]
Suppose \(\alpha^m=1\), \(\alpha\ne1\), and \(f_0(\alpha)=0\). Multiplying by \(1+\alpha\) gives
\[
\alpha^r(1+\alpha+\alpha^2)=1.
\]
Squaring and using \(\alpha^{2r}=\alpha^{-1}\) yields
\[
\alpha^4+\alpha^2+\alpha+1=0.
\]
But
\[
z^4+z^2+z+1=(z+1)(z^3+z^2+1).
\]
The cubic is irreducible over \(\mathbb F_2\), and its roots have multiplicative order \(7\). Thus \(7\mid m\). This proves property 4.

For \(A^{(1)}\), write
\[
F(z)=1+z+\cdots+z^r,\qquad
f_1(z)=F(z)+z+z^{m-1}.
\]
At a nontrivial \(m\)-th root \(\alpha\),
\[
F(\alpha)^2
=\frac{1+\alpha^{2r+2}}{1+\alpha^2}
=\frac1{1+\alpha}.
\]
If \(f_1(\alpha)=0\), then \(F(\alpha)=\alpha+\alpha^{-1}\), so
\[
\frac1{1+\alpha}=\alpha^2+\alpha^{-2}.
\]
Equivalently,
\[
\alpha^5+\alpha^4+\alpha^2+\alpha+1=0.
\tag{3.7}
\]
The polynomial
\[
h(z)=z^5+z^4+z^2+z+1
\]
has no root in \(\mathbb F_2\), and its remainder modulo the unique irreducible quadratic \(z^2+z+1\) is \(1\). A reducible polynomial of degree \(5\) must have a factor of degree at most \(2\); hence \(h\) is irreducible. Its roots have order \(31\), since \(\mathbb F_{32}^{\times}\) has prime order \(31\). Equation (3.7) therefore implies \(31\mid m\). This proves property 5. ∎

---

# 4. Structure of the midpoint graphs

For \(c\in\mathbb Z_m\), let
\[
M_c=\left\{\{i,j\}:i\ne j,\ \frac{i+j}{2}=c\right\}.
\]
Here division by \(2\) is in \(\mathbb Z_m\). Each \(M_c\) is a matching leaving exactly \(c\) unmatched.

For \(S\subseteq\mathbb Z_m\), put
\[
H_S=\bigcup_{c\in S}M_c.
\]

The next lemma is what permits composite \(m\).

## Lemma 4.1

Suppose \(|S|\ge2\), choose \(s_0\in S\), and let
\[
d=\gcd\bigl(m,\{s-s_0:s\in S\}\bigr),\qquad q=m/d.
\]
Put \(D=d\mathbb Z_m\).

The components of \(H_S\) are:

- the special component on \(C=s_0+D\);
- one component on each pair of cosets
  \[
  (s_0+h+D)\cup(s_0-h+D),\qquad h\ne0\pmod d,
  \]
  counting each pair once.

Moreover:

1. If \(|S|=2\), the special component is a Hamilton path on \(C\), with endpoints the two elements of \(S\).
2. If \(|S|\ge3\), the special component is \(2\)-connected.
3. Every paired-coset component is \(2\)-connected.

### Proof

The matching \(M_c\) implements the reflection
\[
\rho_c(i)=2c-i,
\]
apart from its fixed point \(c\). The group generated by these reflections contains exactly the translations generated by
\[
2(s-s_0),\qquad s\in S.
\]
Since \(m\) is odd, that translation subgroup is \(D\). Its orbits together with reflection about \(s_0\) give precisely the asserted components.

On \(C\), after translation and division by \(d\), the graph is \(H_T\) on \(\mathbb Z_q\), where the differences of elements of \(T\) generate \(\mathbb Z_q\). It is connected. If \(|T|=2\), its two centers have degree one and all other vertices have degree two, proving assertion 1.

For assertion 2, suppose \(H_T-v\) is disconnected. Partition its vertices into nonempty sets \(U,W\) with no edge between them. Then
\[
|U|+|W|=q-1,\qquad \frac{U+W}{2}\cap T=\varnothing.
\tag{4.1}
\]
Let \(L\) be the stabilizer of \(U+W\), and let \(h=|L|\). Kneser’s sumset theorem gives
\[
|U+W|\ge |U+L|+|W+L|-h.
\tag{4.2}
\]

If \(h=1\), then \(|U+W|\ge q-2\), and (4.1) forces \(|T|\le2\).

If \(h>1\), the sum \(|U+L|+|W+L|\) is a multiple of \(h\) and is at least \(q-1\), hence is at least \(q\). Thus
\[
|U+W|\ge q-h.
\]
Its nonempty complement is a union of \(L\)-cosets of total size at most \(h\), so it is one coset. By (4.1), \(T\) lies in a coset of \(L\). This contradicts the assumption that differences of elements of \(T\) generate \(\mathbb Z_q\). Therefore \(H_T\) has no cut vertex.

For assertion 3, translate \(s_0\) to zero. A paired component can be coordinatized as two copies of \(\mathbb Z_q\), with an edge between \(t\) in the first copy and \(u\) in the second precisely when
\[
t+u\in2T.
\]
The maps
\[
(t,u)\longmapsto(t+a,u-a)
\]
and the interchange of the two copies act transitively on its vertices. It is connected by the component description above, and has at least three vertices.

A finite connected vertex-transitive graph with at least three vertices has no cut vertex: every connected graph has a non-cut vertex, for example a leaf of a spanning tree, and vertex transitivity then makes every vertex a non-cut vertex. This proves assertion 3. ∎

---

# 5. Construction of the code

Assume now that
\[
217\nmid m.
\]
Choose
\[
A=
\begin{cases}
A^{(0)},&7\nmid m,\\
A^{(1)},&7\mid m.
\end{cases}
\tag{5.1}
\]
In the second case, \(31\nmid m\), so all conclusions of Lemma 3.1 apply.

Take the vertex set
\[
V=\mathbb Z_m\cup\{a,b\}.
\]
For each
\[
x\in\mathbb E_m,\qquad \varepsilon\in\mathbb F_2,
\]
define \(G_{x,\varepsilon}\) as follows:

- for distinct \(i,j\in\mathbb Z_m\),
  \[
  ij\in E(G_{x,\varepsilon})
  \iff x_{(i+j)/2}=1;
  \]
- put
  \[
  y=Px+\varepsilon\mathbf1,\qquad
  z=P^Tx+\varepsilon\mathbf1,
  \tag{5.2}
  \]
  and use \(y,z\) as the incidence vectors of the edges from \(a,b\), respectively, to \(\mathbb Z_m\);
- include \(ab\) exactly when \(\varepsilon=1\).

All edge indicators are linear in \((x,\varepsilon)\), so
\[
G_{x,\varepsilon}\triangle G_{x',\varepsilon'}
=G_{x+x',\,\varepsilon+\varepsilon'}.
\tag{5.3}
\]
The internal edges determine \(x\), because the nonempty matchings \(M_c\) partition \(E(K_m)\), and the edge \(ab\) determines \(\varepsilon\). Consequently the family has
\[
2^{m-1}\cdot2=2^m
\tag{5.4}
\]
distinct graphs.

We must prove that every nonzero \(G_{x,\varepsilon}\) is \(2\)-connected.

## 5.1. Identities and attachment facts

Since \(x\) has even weight, (3.3) gives
\[
z=y+x.
\tag{5.5}
\]
Also \(Px\) and \(P^Tx\) both have even weight. Thus
\[
\sum_i y_i=\sum_i z_i=\varepsilon.
\]
The parity of the internal degree at \(i\) is \(x_i\), while the two hub edges have parity \(y_i+z_i=x_i\). Hence every \(G_{x,\varepsilon}\) is Eulerian.

When \(x\ne0\), injectivity on \(\mathbb E_m\) shows that \(Px\) and \(P^Tx\) are nonzero even-weight vectors. Therefore:

- if \(\varepsilon=0\), each hub has at least two internal neighbors;
- if \(\varepsilon=1\), each hub has a nonempty internal neighborhood, since the complement of an even-weight vector of odd length has odd weight.

For later use, suppose \(S=\operatorname{supp}(x)=\{c,d\}\). Then
\[
y_c+y_d=P_{c,c}+P_{c,d}+P_{d,c}+P_{d,d}=1.
\tag{5.6}
\]
Thus the two endpoints \(c,d\) are attached to opposite hubs, for either value of \(\varepsilon\).

We use standard elementary facts about \(2\)-connectivity:

- adding a vertex with at least two neighbors preserves \(2\)-connectivity;
- adding an ear preserves \(2\)-connectivity;
- the union of two \(2\)-connected graphs sharing at least two vertices is \(2\)-connected;
- joining two disjoint \(2\)-connected graphs by two edges with four distinct endpoints gives a \(2\)-connected graph.

Each follows directly by checking connectedness after deleting one vertex.

## 5.2. The case \(x=0\)

The only nonzero message is \((0,1)\), which gives
\[
G_{0,1}=K_{2,m}+ab.
\]
This graph is \(2\)-connected.

Henceforth \(x\ne0\), so \(|S|\ge2\) is even.

## 5.3. The case \(d=1\)

Use the notation of Lemma 4.1.

### Subcase \(|S|\ge4\)

The internal graph \(H_S\) is \(2\)-connected.

If \(\varepsilon=0\), both hubs have at least two neighbors in \(H_S\), so adding them preserves \(2\)-connectivity.

If \(\varepsilon=1\), the edge \(ab\) is present, and both internal neighborhoods are nonempty. They cannot both be the same singleton: that would give \(y=z\), contradicting (5.5) and \(x\ne0\). Choose distinct internal vertices \(u,v\) adjacent to \(a,b\), respectively. The path
\[
u-a-b-v
\]
is an ear on \(H_S\). All other edges can then be added without destroying \(2\)-connectivity.

### Subcase \(|S|=2\)

The internal graph is a Hamilton path with endpoints \(c,d\), which are attached to opposite hubs by (5.6).

If \(\varepsilon=1\), this path, its two endpoint attachments, and \(ab\) form a spanning cycle.

Suppose \(\varepsilon=0\), and put \(Y=\operatorname{supp}(y)\). Then
\[
|Y|=|(A+c)\triangle(A+d)|\ge4.
\]
Exactly one of \(c,d\) belongs to \(Y\), so there are at least three internal path vertices adjacent to both hubs.

This gives \(2\)-connectivity. Indeed, deleting either hub leaves the internal path connected. Deleting an internal path vertex leaves at most two path pieces; the original endpoints attach these pieces to opposite hubs, and a surviving common neighbor connects the hubs. Endpoint deletion is handled in the same way.

This finishes \(d=1\).

## 5.4. The case \(d>1\)

Translate internal labels so that \(s_0=0\). Thus \(S\subseteq D=d\mathbb Z_m\), and its restriction to \(D\) is a nonzero even-weight vector \(u\in\mathbb E_q\).

For a coset \(h+D\), the restriction of \(Px\) is convolution of \(u\) by the slice \(A_{d,h}\). Lemma 3.1 therefore shows that this restriction is nonzero and even-weight. The same is true of \(P^Tx\): the slices of \(-A\) are translates of reversals of slices of \(A\), and are cyclic intervals of the same lengths.

It follows that, on every coset:

- for \(\varepsilon=0\), each of \(y,z\) has positive even weight;
- for \(\varepsilon=1\), each has positive odd weight.

Outside the special coset \(D\), equation (5.5) says \(y=z\). Consequently, every paired-coset component has at least two vertices adjacent to both hubs: for \(\varepsilon=1\), there is at least one in each coset, and for \(\varepsilon=0\), there are at least two in each coset.

Each paired component is \(2\)-connected by Lemma 4.1. Adjoining both hubs to it therefore gives a \(2\)-connected graph. Their union, denoted \(B\), is \(2\)-connected because all these graphs share \(a,b\). There is at least one paired component since \(d>1\) is odd.

It remains to attach the special component.

- If \(|S|=2\), it is a path with endpoints attached to opposite hubs. Together with its endpoint attachments, it is an ear on \(B\).
- If \(|S|\ge4\), the special component is \(2\)-connected. Both hubs have nonempty neighborhoods in it. These neighborhoods cannot both be the same singleton, since their symmetric difference is the nonzero vector \(x|_D\). Thus there are distinct \(u,v\in D\) with \(au,bv\) present. These two edges join the special component to \(B\) with four distinct endpoints, giving a \(2\)-connected graph.

All remaining edges may be added harmlessly.

This covers every nonzero message.

## 5.5. Conclusion

By (5.3)–(5.4), the family
\[
\mathcal C_m=\{G_{x,\varepsilon}:x\in\mathbb E_m,\ \varepsilon\in\mathbb F_2\}
\]
is a \(2\)-connected graph-code of size \(2^m\) on \(m+2\) vertices. Combining this with (2.1) gives
\[
\boxed{M_{2c}(m+2)=2^m}
\]
for every odd \(m\ge9\) with \(217\nmid m\).

---

# 6. The exact value on five vertices

For completeness, here is the independently checked five-vertex argument from the supplied lead.

## 6.1. A code of size five

On vertex set \(\{1,2,3,4,5\}\), let
\[
S_i=\{1,2,3,4\}\setminus\{i\},\qquad 1\le i\le4,
\]
and let \(\delta(S)\) denote the complete bipartite cut determined by \(S\).

The family
\[
\{\varnothing,\delta(S_1),\delta(S_2),\delta(S_3),\delta(S_4)\}
\]
has five members. Its nonempty members are \(K_{3,2}\), and, for \(i\ne j\),
\[
\delta(S_i)\triangle\delta(S_j)
=\delta(S_i\triangle S_j)
=\delta(\{i,j\})\cong K_{2,3}.
\]
Hence \(M_{2c}(5)\ge5\).

## 6.2. A hypercube observation

**Lemma.** An independent set of \(Q_4\) containing vectors of both parities has size at most five.

**Proof.** Translate the independent set so that it contains \(0000\). It contains no vector of weight one, so its odd vectors all have weight three. If \(B\) is the set of these odd vectors and \(|B|=b\), their neighborhoods among the eight even vectors satisfy
\[
\begin{array}{c|cccc}
b&1&2&3&4\\ \hline
|N(B)|&4&6&7&7.
\end{array}
\]
Thus the independent set has size at most
\[
b+8-|N(B)|\le5.
\]
∎

## 6.3. Upper bound

Suppose a code on five vertices has at least six members. Applying the lemma to every star projection shows that all pairwise differences have even degree at every vertex. Translate by one codeword; all members are then Eulerian.

An Eulerian \(2\)-connected graph on five vertices has every degree equal to \(2\) or \(4\). If \(t\) vertices have degree \(4\), it has \(5+t\) edges. When the edge count is even, \(t\) is odd.

- \(t=1\) gives two triangles sharing the unique degree-four vertex, which is a cut vertex.
- \(t=3\) is impossible, since either remaining vertex would have at least three neighbors.
- \(t=5\) gives \(K_5\).

Thus the only even-edge Eulerian \(2\)-connected graph on five vertices is \(K_5\).

Partition the translated code by parity of edge count. Two distinct members of the same part must differ by \(K_5\). Each part therefore has size at most two: three members cannot all differ pairwise by the same nonzero graph. The code consequently has size at most four, contradicting the assumed size at least six.

Therefore
\[
\boxed{M_{2c}(5)=5}.
\]

---

# 7. What remains unresolved

The stated partial theorem leaves:

- \(n=7\);
- \(n=9\);
- the odd orders
  \[
  n=219+434k,\qquad k\ge0.
  \]

The last progression is a limitation of the two explicitly verified circulant choices, not an upper-bound obstruction. Their possible nontrivial kernels arise from roots of orders \(7\) and \(31\), respectively; neither choice supplies the needed injectivity when both divide \(n-2\).

Accordingly, this does **not** determine \(M_{2c}(n)\) for every odd \(n\), but it does attain the catalog’s upper bound for all but one residue class among odd orders \(n\ge11\).