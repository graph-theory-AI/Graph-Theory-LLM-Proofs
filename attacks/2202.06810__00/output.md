```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I determine M_{F_{2c}}(5)=5 and attain the upper bound M_{F_{2c}}(p+2)=2^p for every prime p congruent to 1 modulo 4 with p at least 13.",
  "would_publish": false,
  "caveats": "Other odd orders remain unresolved, and I have not externally checked the novelty of the prime-order construction."
}
```

# 1. Statement of the partial result

All graphs below are simple graphs on a common labeled vertex set, and only pairwise symmetric differences are required to be 2-connected.

I prove the following.

**Theorem.**

1. \(M_{F_{2c}}(5)=5\).
2. If \(p\ge 13\) is a prime with \(p\equiv1\pmod 4\), then
   \[
   M_{F_{2c}}(p+2)=2^p=2^{(p+2)-2}.
   \]

Thus the known upper bound is sharp for infinitely many odd \(n\), namely for
\[
n=p+2,\qquad p\ge13\text{ prime},\quad p\equiv1\pmod4.
\]
The first examples are \(n=15,19,31,39,\ldots\).

The proof is self-contained apart from the standard Cauchy–Davenport theorem.

---

# 2. The general upper bound and its equality structure

For a graph \(G\) and a vertex \(v\), let
\[
\sigma_v(G)\in\mathbb F_2^{n-1}
\]
be the incidence vector of the edges of \(G\) incident with \(v\).

If \(\mathcal C\) is an \(F_{2c}\)-code and \(G,H\in\mathcal C\) are distinct, then
\[
d_H\bigl(\sigma_v(G),\sigma_v(H)\bigr)
   =\deg_{G\triangle H}(v)\ge2.
\]
Thus \(\sigma_v(\mathcal C)\) is an independent set in the hypercube \(Q_{n-1}\). Since
\[
\alpha(Q_{n-1})=2^{n-2},
\]
this gives
\[
|\mathcal C|\le2^{n-2}.
\]

There is also a useful equality condition. The only independent sets of size \(2^{m-1}\) in the connected hypercube \(Q_m\) are its two parity classes. Indeed, such an independent set meets every edge exactly once and hence is one side of the unique bipartition.

Consequently, if \(|\mathcal C|=2^{n-2}\), then for every vertex \(v\), all vectors \(\sigma_v(G)\), \(G\in\mathcal C\), have the same parity. Therefore every symmetric difference \(G\triangle H\) is Eulerian. After translating the family by one member, an extremal family may thus be assumed to consist entirely of Eulerian graphs.

The construction below is a linear family with precisely this property.

---

# 3. An infinite family of odd orders attaining the upper bound

## 3.1. The indexing set

Let
\[
p=2r+1\ge13
\]
be prime, with \(p\equiv1\pmod4\). Thus \(r\) is even.

Work in the additive group \(\mathbb Z_p\), and put
\[
A=\{0,1,\ldots,r-1,r+1\}\subseteq\mathbb Z_p.
\]

This set has three properties that will be used.

### Lemma 3.1

The set \(A\) satisfies:

1. \(A\cap(-A)=\{0\}\) and \(A\cup(-A)=\mathbb Z_p\);
2. the circulant matrix
   \[
   P_{i,c}=\mathbf 1_A(i-c),\qquad i,c\in\mathbb Z_p,
   \]
   is nonsingular over \(\mathbb F_2\);
3. for every nonzero \(t\in\mathbb Z_p\),
   \[
   |A\triangle(A+t)|\ge4.
   \]

### Proof

For the first assertion, \(A\) contains \(1,\ldots,r-1\), and from the pair \(\{r,-r\}=\{r,r+1\}\) it contains \(r+1\). Thus it contains exactly one element from every pair \(\{t,-t\}\), \(t\ne0\).

For nonsingularity, the associated circulant polynomial is
\[
f(z)=1+z+\cdots+z^{r-1}+z^{r+1}.
\]
It suffices to prove
\[
\gcd(f(z),z^p-1)=1
\]
over \(\mathbb F_2\).

First,
\[
f(1)=|A|\equiv r+1\equiv1\pmod2,
\]
because \(r\) is even. Thus \(1\) is not a root.

Suppose that \(\alpha^p=1\), \(\alpha\ne1\), and \(f(\alpha)=0\). Multiplication by \(1+\alpha\) gives
\[
1+\alpha^r+\alpha^{r+1}+\alpha^{r+2}=0.
\]
Writing \(\beta=\alpha^r\), this is
\[
\beta(1+\alpha+\alpha^2)=1.
\]
Squaring and using
\[
\beta^2=\alpha^{2r}=\alpha^{p-1}=\alpha^{-1}
\]
gives
\[
\alpha^{-1}(1+\alpha^2+\alpha^4)=1,
\]
and hence
\[
\alpha^4+\alpha^2+\alpha+1=0.
\]
Over \(\mathbb F_2\),
\[
z^4+z^2+z+1=(z+1)(z^3+z^2+1).
\]
The cubic \(z^3+z^2+1\) is irreducible over \(\mathbb F_2\), so any of its roots has multiplicative order \(7\). This is incompatible with \(\alpha^p=1\), since \(p\ne7\) is prime. Therefore \(P\) is nonsingular.

For the third assertion, let
\[
I=\{0,1,\ldots,r\}.
\]
Then \(A\) is obtained from \(I\) by replacing \(r\) by \(r+1\).

Since
\[
|A\cap(A+t)|=|A\cap(A-t)|,
\]
we may take \(t=d\) with \(1\le d\le r\). For \(I\),
\[
|I\cap(I+d)|=r+1-d.
\]
Replacing \(I\) by \(A\) in both copies can increase the intersection by at most \(2\). Hence, for \(d\ge4\),
\[
|A\cap(A+d)|\le r+1-d+2\le r-1.
\]
Directly,
\[
\begin{aligned}
|A\cap(A+1)|&=r-1,\\
|A\cap(A+2)|&=r-1,\\
|A\cap(A+3)|&=r-2.
\end{aligned}
\]
Thus in every case
\[
|A\cap(A+t)|\le r-1.
\]
Since \(|A|=r+1\),
\[
|A\triangle(A+t)|
 =2|A|-2|A\cap(A+t)|
 \ge4.
\]
∎

---

## 3.2. Definition of the graph family

Let
\[
V=\mathbb Z_p\cup\{a,b\}.
\]
For each vector
\[
x=(x_c)_{c\in\mathbb Z_p}\in\mathbb F_2^p,
\]
define a graph \(G_x\) on \(V\) as follows.

For distinct \(i,j\in\mathbb Z_p\), put
\[
ij\in E(G_x)
 \quad\Longleftrightarrow\quad
 x_{(i+j)/2}=1,
\]
where division by \(2\) is in \(\mathbb Z_p\).

Let
\[
y=Px,\qquad z=P^{T}x.
\]
Put
\[
ai\in E(G_x)\iff y_i=1,\qquad
bi\in E(G_x)\iff z_i=1.
\]
Finally,
\[
ab\in E(G_x)
 \quad\Longleftrightarrow\quad
 \sum_{c\in\mathbb Z_p}x_c=1
 \quad\text{in }\mathbb F_2.
\]

Every edge indicator is a linear function of \(x\). Therefore
\[
G_x\triangle G_{x'}=G_{x+x'}.
\]
It remains to prove that \(G_x\) is 2-connected whenever \(x\ne0\).

---

## 3.3. Parity identities

Let
\[
s=\sum_c x_c\in\mathbb F_2.
\]
From \(A\cap(-A)=\{0\}\) and \(A\cup(-A)=\mathbb Z_p\), we have
\[
P^T=P+J+I,
\]
where \(J\) is the all-one matrix. Hence
\[
z_i=y_i+s+x_i.
\]

At an internal vertex \(i\in\mathbb Z_p\), as \(j\) ranges over \(\mathbb Z_p\setminus\{i\}\), the midpoint \((i+j)/2\) ranges bijectively over \(\mathbb Z_p\setminus\{i\}\). Thus the parity of the internal degree at \(i\) is
\[
s+x_i.
\]
The two edges to \(a,b\) have parity
\[
y_i+z_i=s+x_i.
\]
Therefore every internal vertex has even degree.

Every row and column of \(P\) has \(|A|=r+1\), which is odd. Consequently
\[
\sum_i y_i=s,\qquad \sum_i z_i=s.
\]
The edge \(ab\) is present exactly when \(s=1\), so \(a\) and \(b\) also have even degree.

Since \(P\) and \(P^T\) are nonsingular, a nonzero \(x\) gives nonempty neighborhoods at both \(a\) and \(b\). The internal stars are also nonzero: if all internal edges at \(i\) vanished, then \(x\) would be supported only at \(i\), in which case both \(ai\) and \(bi\) are present because \(P_{i,i}=1\).

Thus every nonzero \(G_x\) is spanning and Eulerian, with minimum degree at least \(2\).

---

## 3.4. The midpoint graphs

For \(c\in\mathbb Z_p\), let
\[
M_c=\left\{\{i,j\}:i\ne j,\ \frac{i+j}{2}=c\right\}.
\]
The graph \(M_c\) is a matching on \(\mathbb Z_p\setminus\{c\}\), leaving \(c\) unmatched.

If
\[
S=\{c:x_c=1\},
\]
then the graph induced by \(G_x\) on \(\mathbb Z_p\) is
\[
H_S=\bigcup_{c\in S}M_c.
\]

### Lemma 3.2

For \(S\subseteq\mathbb Z_p\):

1. if \(|S|=1\), \(H_S\) is a near-perfect matching;
2. if \(|S|=2\), \(H_S\) is a Hamilton path whose endpoints are the two elements of \(S\);
3. if \(|S|\ge3\), \(H_S\) is 2-connected.

### Proof

The first assertion is immediate.

Let \(S=\{c,d\}\), \(c\ne d\). The two matchings arise from the reflections
\[
\rho_c(t)=2c-t,\qquad \rho_d(t)=2d-t.
\]
Their composition is a nonzero translation of \(\mathbb Z_p\). Since \(p\) is prime, this translation acts transitively. Hence \(M_c\cup M_d\) is connected. Its only degree-one vertices are \(c,d\), and all other vertices have degree two, so it is a Hamilton path.

For the remaining claims, use Cauchy–Davenport. If \(H_S\) were disconnected, take a nontrivial partition
\[
\mathbb Z_p=U\mathbin{\dot\cup}W
\]
with no \(U\)-\(W\) edge. Then
\[
\frac{U+W}{2}\cap S=\varnothing.
\]
But
\[
|U+W|\ge \min(p,|U|+|W|-1)=p-1,
\]
so \(|S|\le1\).

Similarly, if \(v\) were a cut vertex, let \(U,W\) be nonempty unions of components of \(H_S-v\). Then
\[
|U|+|W|=p-1
\]
and again \((U+W)/2\) is disjoint from \(S\). Hence
\[
|U+W|\ge p-2,
\]
so \(|S|\le2\). Thus \(|S|\ge3\) implies 2-connectivity. ∎

---

## 3.5. Proof that every \(G_x\), \(x\ne0\), is 2-connected

Write
\[
Y=\{i:y_i=1\},\qquad Z=\{i:z_i=1\}.
\]

### Case 1: \(|S|\ge3\)

By Lemma 3.2, \(H_S\) is 2-connected.

If \(|S|\) is even, then \(ab\) is absent and \(|Y|,|Z|\) are positive even integers. Thus each is at least \(2\). Adding a new vertex with at least two neighbors to a 2-connected graph preserves 2-connectivity, so adjoining \(a\) and then \(b\) gives a 2-connected graph.

Suppose \(|S|\) is odd. Then \(ab\) is present and \(|Y|,|Z|\) are positive odd integers.

- If at least one of \(|Y|,|Z|\) is at least \(3\), first add that vertex to \(H_S\), and then add the other using its internal neighbor and the edge \(ab\).
- If \(|Y|=|Z|=1\), say \(Y=\{u\}\), \(Z=\{v\}\), then if \(u\ne v\), the path
  \[
  u-a-b-v
  \]
  is an ear added to the 2-connected graph \(H_S\), so the result is 2-connected.

The only potentially bad possibility is \(Y=Z=\{u\}\). But \(y=z\) implies
\[
(J+I)x=0.
\]
For nonzero \(x\) of odd weight, this forces \(x=\mathbf1\). In that case
\[
y=P\mathbf1=\mathbf1,
\]
because every row of \(P\) has odd weight. Thus \(Y\) is not a singleton. This excludes the final bad case.

### Case 2: \(|S|=1\)

Let \(S=\{c\}\). Then
\[
Y=A+c,\qquad Z=-A+c.
\]
These sets intersect only in \(c\). Each matching edge of \(M_c\) has one endpoint in \(Y\setminus\{c\}\) and one in \(Z\setminus\{c\}\).

Consequently, \(G_x\) is the union of internally vertex-disjoint \(a\)-\(b\) paths:

- the edge \(ab\);
- the path \(a-c-b\);
- for every edge \(uv\in M_c\), a path \(a-u-v-b\).

A union of at least two internally disjoint paths with common endpoints is 2-connected.

### Case 3: \(|S|=2\)

Let \(S=\{c,d\}\). By Lemma 3.2, \(H_S\) is a Hamilton path with endpoints \(c,d\).

Here \(ab\) is absent, and
\[
Z=Y\triangle\{c,d\}.
\]
Exactly one of \(c,d\) belongs to \(Y\). Indeed, writing \(t=d-c\),
\[
\mathbf1_Y(c)=1+\mathbf1_A(-t),\qquad
\mathbf1_Y(d)=1+\mathbf1_A(t),
\]
and the two values differ because
\[
\mathbf1_A(t)+\mathbf1_A(-t)=1.
\]

Every internal vertex in
\[
R:=Y\setminus\{c,d\}
\]
is adjacent to both \(a\) and \(b\). The two endpoints \(c,d\) are adjacent to opposite members of \(\{a,b\}\).

Moreover,
\[
|Y|=|(A+c)\triangle(A+d)|
     =|A\triangle(A+t)|\ge4
\]
by Lemma 3.1. Hence \(|R|\ge3\).

A Hamilton path whose endpoints are attached to opposite vertices \(a,b\), and with at least two internal vertices adjacent to both \(a\) and \(b\), becomes 2-connected. To check this directly, delete any vertex:

- deleting \(a\) or \(b\) leaves the Hamilton path connected;
- deleting a path vertex splits the path into at most two pieces, while a surviving vertex of \(R\) connects \(a\) to \(b\), and the two path endpoints connect the two pieces to opposite sides.

Thus \(G_x\) is 2-connected.

This completes all cases.

Since the map \(x\mapsto G_x\) is linear and \(P\) is nonsingular,
\[
\mathcal C=\{G_x:x\in\mathbb F_2^p\}
\]
has \(2^p\) distinct members, and every nonzero symmetric difference is 2-connected. Therefore
\[
M_{F_{2c}}(p+2)\ge2^p.
\]
Together with the general upper bound,
\[
\boxed{M_{F_{2c}}(p+2)=2^p}
\]
for all primes \(p\ge13\) with \(p\equiv1\pmod4\).

---

# 4. The exact value for \(n=5\)

## 4.1. Lower bound

Let the vertex set be \(\{1,2,3,4,5\}\). For \(i=1,2,3,4\), put
\[
S_i=\{1,2,3,4\}\setminus\{i\},
\]
and let \(\delta(S_i)\) be the complete bipartite cut between \(S_i\) and its complement.

The family
\[
\mathcal C=\{\varnothing,\delta(S_1),\delta(S_2),\delta(S_3),\delta(S_4)\}
\]
has size \(5\). Each nonzero member is \(K_{3,2}\), while
\[
\delta(S_i)\triangle\delta(S_j)
 =\delta(S_i\triangle S_j)
 =\delta(\{i,j\})\cong K_{2,3}.
\]
Thus every nonzero difference is 2-connected, and
\[
M_{F_{2c}}(5)\ge5.
\]

## 4.2. A hypercube lemma

**Lemma 4.1.** If \(I\) is an independent set in \(Q_4\) containing vectors of both parities, then \(|I|\le5\).

**Proof.**
Translate so that \(0000\in I\). No weight-one vector belongs to \(I\), so every odd vector in \(I\) has weight three. If there are \(b\) such vectors, their neighborhoods among the eight even vectors have sizes

\[
\begin{array}{c|cccc}
b&1&2&3&4\\ \hline
|N(B)|&4&6&7&7.
\end{array}
\]

Hence
\[
|I|\le b+8-|N(B)|\le5.
\]
∎

## 4.3. Upper bound

Suppose that an \(F_{2c}\)-code \(\mathcal C\) on five vertices has at least six members. For each vertex \(v\), the set \(\sigma_v(\mathcal C)\) is an independent set in \(Q_4\). By Lemma 4.1 it lies in a single parity class. Hence every symmetric difference of two members of \(\mathcal C\) is Eulerian.

Translate \(\mathcal C\) so that it contains the empty graph. All its members are then Eulerian, and every nonzero pairwise difference is Eulerian and 2-connected.

We classify the even-sized Eulerian 2-connected graphs on five vertices. Every degree is either \(2\) or \(4\). Let \(t\) be the number of degree-four vertices. Then
\[
|E|=5+t.
\]
If \(|E|\) is even, \(t\) is odd.

- If \(t=1\), the unique degree-four vertex is universal, and the other four vertices induce a perfect matching. Deleting the universal vertex disconnects the graph.
- If \(t=3\), each of the remaining two vertices is adjacent to the three universal vertices, contradicting its degree being \(2\).
- If \(t=5\), the graph is \(K_5\).

Thus the only even-sized Eulerian 2-connected graph on five vertices is \(K_5\).

Partition the translated family according to the parity of its edge count. If \(G,H\) are distinct members in the same part, then \(G\triangle H\) has an even number of edges and hence must equal \(K_5\). No such parity part can contain three graphs: if
\[
G\triangle H=K_5=G\triangle L,
\]
then \(H=L\). Therefore each parity part has size at most two, and the whole Eulerian-difference family has size at most four.

This contradicts the assumed size at least six. Therefore every \(F_{2c}\)-code on five vertices has size at most five. Combined with the construction,
\[
\boxed{M_{F_{2c}}(5)=5}.
\]

---

# 5. Remaining gaps

The argument does not determine \(M_{F_{2c}}(n)\) for all odd \(n\). In particular, it leaves unresolved:

- \(n=7,9,11,13\);
- orders \(n=p+2\) with \(p\equiv3\pmod4\);
- most composite values of \(n-2\).

The prime construction relies in an essential way on:

1. the prime cyclic midpoint factorization, through Cauchy–Davenport;
2. the odd cardinality of \(A\), which here corresponds to \(p\equiv1\pmod4\);
3. the shift condition \(|A\triangle(A+t)|\ge4\).

No claim is made here about the remaining odd orders.