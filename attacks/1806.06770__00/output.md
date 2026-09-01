```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact constant remains unresolved, but the P4 bound is proved for graphs of order at most five, trees and their complements, non-pendant bridge cuts, and all generalized P4-substitutions.",
  "would_publish": false,
  "caveats": "No universal improvement over [1/2, 2-sqrt(2)]; general graphs of order at least six, including pendant-bridge cases, remain."
}
```

# Mathematical writeup

## 1. Formulation and current bounds

Write
\[
a(G):=\lambda_2(G),\qquad
F(G):=\max\{a(G),a(\overline G)\},
\]
and let
\[
c_*=\inf_{\substack{G\text{ finite simple}\\ |V(G)|\ge2}}F(G).
\]
This infimum is the supremum asked for in the problem.

If \(G\) has order \(n\), then
\[
L(G)+L(\overline G)=nI-J.
\]
Consequently, on \(\mathbf 1^\perp\),
\[
L(\overline G)=nI-L(G),
\]
and hence
\[
a(\overline G)=n-\lambda_n(G). \tag{1}
\]
Thus
\[
F(G)=\max\{\lambda_2(G),\,n-\lambda_n(G)\}.
\]

The theorem of Einollahzadeh and Karkhaneei stated in the prompt gives
\[
a(G)+a(\overline G)\ge1,
\]
and therefore
\[
c_*\ge\frac12.
\]
Since \(P_4\cong\overline{P_4}\) and
\[
\operatorname{Spec}L(P_4)=\{0,\,2-\sqrt2,\,2,\,2+\sqrt2\},
\]
we have
\[
c_*\le \tau:=2-\sqrt2.
\]

The results below do not close this interval, but they substantially restrict where a counterexample to \(c_*=\tau\) could occur.

---

## 2. A canonical induced \(P_4\) in every possible counterexample

We first record an elementary extremal-vector lemma.

### Lemma 2.1
Let \(H\) be connected and \(a(H)<1\). Then \(H\) has two vertices \(u,v\) which are nonadjacent and have no common neighbor. In particular, \(uv\) is a dominating edge of \(\overline H\).

#### Proof
Let \(x\perp\mathbf1\) be a Fiedler vector, normalized arbitrarily, with
\[
L(H)x=a(H)x.
\]
Choose \(u,v\) such that
\[
x_u=\max_i x_i>0,\qquad x_v=\min_i x_i<0.
\]

For every neighbor \(w\) of \(u\), the quantity \(x_u-x_w\) is nonnegative. If some neighbor satisfied \(x_w\le0\), then
\[
a(H)x_u=\sum_{w\sim u}(x_u-x_w)\ge x_u,
\]
contrary to \(a(H)<1\). Thus every neighbor of \(u\) has positive \(x\)-coordinate.

Similarly, every neighbor of \(v\) has negative \(x\)-coordinate. Therefore \(u,v\) are nonadjacent and cannot have a common neighbor.

For every third vertex \(z\), at least one of \(uz,vz\) is therefore absent from \(H\). Hence in \(\overline H\), the edge \(uv\) dominates every vertex. ∎

The lemma can be applied simultaneously to \(G\) and its complement.

### Proposition 2.2
Suppose \(G\) and \(\overline G\) are connected and
\[
a(G)<1,\qquad a(\overline G)<1.
\]
Then there are four distinct vertices \(u,s,t,v\) inducing the path
\[
u-s-t-v.
\]
Moreover:

1. \(uv\) is a dominating edge of \(\overline G\);
2. \(st\) is a dominating edge of \(G\);
3. \(\operatorname{diam}(G)=\operatorname{diam}(\overline G)=3\).

#### Proof
Apply Lemma 2.1 to \(G\), obtaining nonadjacent vertices \(u,v\) with no common neighbor. Thus \(uv\) dominates \(\overline G\).

Apply the lemma to \(\overline G\), obtaining vertices \(s,t\) which are nonadjacent in \(\overline G\), have no common neighbor there, and hence form a dominating edge in \(G\).

The pairs \(\{u,v\}\) and \(\{s,t\}\) are disjoint. Indeed, suppose for example that \(s=u\). Since \(st\in E(G)\), the vertex \(t\) is adjacent to \(u\). Since \(st\) dominates \(G\), the vertex \(v\) is adjacent to \(s=u\) or to \(t\). The former is impossible because \(uv\notin E(G)\); the latter would make \(t\) a common neighbor of \(u,v\), also impossible.

Because \(st\) dominates \(G\), each of \(u,v\) is adjacent to at least one of \(s,t\). They cannot be adjacent to the same one, because \(u,v\) have no common neighbor. After interchanging \(s,t\), we therefore have
\[
us,tv,st\in E(G),\qquad ut,sv,uv\notin E(G).
\]
Thus \(u,s,t,v\) induce \(P_4\).

The vertices \(u,v\) have distance at least three and are joined by the displayed three-edge path, so their distance is exactly three. The dominating edge \(st\) shows that every two vertices of \(G\) are at distance at most three. Hence \(\operatorname{diam}(G)=3\). The complement statement is symmetric. ∎

Thus every strict counterexample to \(F(G)\ge\tau\) must have both diameters exactly three and must contain this particularly constrained induced \(P_4\).

---

## 3. Exact determination through order five

### Proposition 3.1
For \(n=2,3,4,5\), the minimum of \(F(G)\) over graphs of order \(n\) is respectively
\[
2,\qquad 1,\qquad 2-\sqrt2,\qquad \frac{5-\sqrt{13}}2.
\]
In particular, \(F(G)\ge2-\sqrt2\) for every graph of order at most five, with equality only for \(P_4\).

#### Proof

If \(G\) is disconnected, then \(\overline G\) contains the complete multipartite graph whose parts are the components of \(G\). It follows by edge monotonicity that
\[
a(\overline G)\ge1. \tag{2}
\]
Thus a graph with \(F(G)<1\) must be connected and co-connected.

The cases \(n=2,3\) are immediate.

For \(n=4\), if both \(G\) and \(\overline G\) are connected, each has at least three edges. Since together they have six edges, both have exactly three edges and hence are trees. The only tree of order four whose complement is connected is \(P_4\). This gives the value \(2-\sqrt2\).

Now let \(n=5\), and suppose \(F(G)<1\). Proposition 2.2 gives an induced path
\[
u-s-t-v
\]
such that \(st\) dominates \(G\), while \(uv\) dominates \(\overline G\). Let \(w\) be the fifth vertex. Therefore:

- \(w\) is adjacent to at least one of \(s,t\);
- \(w\) is not adjacent to both \(u,v\).

Modulo reversing the path, there are five possibilities:
\[
\begin{array}{c|c}
\text{type}&N(w)\cap\{u,s,t,v\}\\ \hline
A&\{s\}\\
B&\{u,s\}\\
C&\{s,v\}\\
D&\{s,t\}\\
E&\{u,s,t\}.
\end{array}
\]
Taking complements interchanges \(A\leftrightarrow E\) and \(B\leftrightarrow C\), while \(D\) is self-complementary.

For types \(A\) and \(B\), the nontrivial quotient eigenvalues are the roots of
\[
p(z)=z^3-7z^2+13z-5. \tag{3}
\]
In type \(A\) there is one additional eigenvalue \(1\), and in type \(B\) one additional eigenvalue \(3\).

Let
\[
T=\frac{5+\sqrt{13}}2.
\]
Since \(T^2-5T+3=0\), direct substitution gives
\[
p(T)=1.
\]
Also \(p(4)=-1\), and
\[
p'(z)=3z^2-14z+13>0\qquad(z\ge4).
\]
Therefore the largest root \(R\) of \(p\) satisfies
\[
R<T.
\]
By (1),
\[
a(\overline G)=5-R>5-T=\frac{5-\sqrt{13}}2. \tag{4}
\]
The same conclusion holds for the complementary types \(C,E\).

Type \(D\) is the bull graph: a triangle with pendant vertices attached at two distinct triangle vertices. Its Laplacian spectrum is
\[
0,\quad
\frac{5-\sqrt{13}}2,\quad
\frac{5-\sqrt5}2,\quad
\frac{5+\sqrt5}2,\quad
\frac{5+\sqrt{13}}2.
\]
Hence
\[
F(G)=\frac{5-\sqrt{13}}2.
\]
This proves the \(n=5\) assertion. Since
\[
\frac{5-\sqrt{13}}2>2-\sqrt2,
\]
the only equality case through order five is \(P_4\). ∎

---

## 4. Trees and complements of trees

### Proposition 4.1
If \(T\) is a tree, then
\[
F(T)\ge2-\sqrt2.
\]
Equality holds only for \(T=P_4\). The same conclusion holds whenever \(\overline G\) is a tree.

#### Proof
The cases of order at most four follow from Proposition 3.1. Let \(n\ge5\).

If \(T\) is a star, then \(a(T)=1\), so there is nothing to prove. Assume \(T\) is not a star. Then
\[
\Delta(T)\le n-2.
\]

Because \(T\) is bipartite, \(L(T)\) is diagonally similar to the signless Laplacian
\[
Q(T)=D(T)+A(T).
\]
Thus \(\lambda_n(T)=\rho(Q(T))\). Applying the Collatz–Wielandt bound to the positive degree vector gives
\[
\lambda_n(T)\le
\max_{v\in V(T)}
\left(
d(v)+\frac{1}{d(v)}\sum_{u\sim v}d(u)
\right). \tag{5}
\]

For a vertex \(v\), deleting \(v\) produces \(d(v)\) rooted components. If the component containing a neighbor \(u\) has order \(n_u\), then \(d(u)\le n_u\). Hence
\[
\sum_{u\sim v}d(u)\le\sum_{u\sim v}n_u=n-1. \tag{6}
\]

If \(d(v)=1\), the expression in (5) is at most \(1+\Delta(T)\le n-1\). If \(2\le d(v)\le n-2\), then it is at most
\[
d(v)+\frac{n-1}{d(v)}.
\]
This is convex as a function of \(d(v)>0\), so its maximum on \([2,n-2]\) occurs at an endpoint. For \(n\ge5\),
\[
n-2+\frac{n-1}{n-2}
\ge
2+\frac{n-1}{2},
\]
because their difference is
\[
\frac{(n-3)(n-4)}{2(n-2)}\ge0.
\]
Consequently,
\[
\lambda_n(T)\le n-1+\frac1{n-2}.
\]
By (1),
\[
a(\overline T)\ge1-\frac1{n-2}\ge\frac23>2-\sqrt2.
\]
Thus \(F(T)>2-\sqrt2\) for every nonstar tree of order at least five. The unique tree equality case is \(P_4\).

Since \(F(G)=F(\overline G)\), the complementary statement follows. ∎

---

## 5. Bridges separating two nontrivial sides

### Proposition 5.1
Suppose \(G\) has a bridge whose deletion leaves components of orders \(a,b\ge2\). Then
\[
F(G)\ge2-\sqrt2.
\]
Equality is possible only when \(a=b=2\), in which case \(G=P_4\). The same holds with \(G\) and \(\overline G\) interchanged.

#### Proof
Let \(xy\) be the bridge, with \(x\) and \(y\) in components of orders \(a,b\). Every other pair crossing the two components is an edge of \(\overline G\). Hence
\[
K_{a,b}-xy\subseteq\overline G
\]
as a spanning subgraph, and therefore
\[
a(\overline G)\ge a(K_{a,b}-xy). \tag{7}
\]

If \(\min\{a,b\}\ge3\), then
\[
L(K_{a,b}-xy)=L(K_{a,b})-(e_x-e_y)(e_x-e_y)^{\!T}.
\]
The subtracted rank-one matrix has largest eigenvalue \(2\). Weyl's inequality gives
\[
a(K_{a,b}-xy)\ge a(K_{a,b})-2
=\min\{a,b\}-2\ge1.
\]

It remains to consider \(a=2\), say. For \(b\ge2\), a direct equitable-partition calculation gives
\[
\det(zI-L(K_{2,b}-e))
=
z(z-2)^{b-2}p_b(z),
\]
where
\[
p_b(z)
=
z^3-(2b+2)z^2+(b^2+3b)z-(b+2)(b-1). \tag{8}
\]
At \(\tau=2-\sqrt2\), using \(\tau^2=4\tau-2\),
\[
p_b(\tau)
=
(b-2)\big((b-3)\tau-(b-1)\big). \tag{9}
\]
For \(b=2\), this is zero and \(K_{2,2}-e=P_4\).

For \(b\ge3\), (9) is negative. Moreover, for \(0\le z\le\tau<1\),
\[
p_b'(z)
=3z^2-2(2b+2)z+b^2+3b
\ge b^2-b-4>0.
\]
Thus \(p_b\) has no root in \((0,\tau]\), and
\[
a(K_{2,b}-e)>\tau.
\]
Together with (7), this proves the inequality.

If \(a=b=2\), each bridge component is a connected graph on two vertices, so \(G\) is exactly \(P_4\). ∎

This leaves only pendant bridges in a possible general counterexample; Proposition 4.1 handles them when the whole graph is a tree.

---

## 6. Generalized \(P_4\)-substitutions

A generalized \(P_4\)-substitution is obtained as follows. Partition
\[
V(G)=V_1\sqcup V_2\sqcup V_3\sqcup V_4
\]
into nonempty parts, put arbitrary graphs inside the \(V_i\), make all possible edges between \(V_i,V_{i+1}\), and put no edges between nonconsecutive parts.

### Theorem 6.1
Every generalized \(P_4\)-substitution satisfies
\[
F(G)\ge2-\sqrt2.
\]
Equality holds only when all four parts are singletons, so that \(G=P_4\).

#### Proof
Put
\[
|V_1|=a,\quad |V_2|=b,\quad |V_3|=c,\quad |V_4|=d,\qquad
n=a+b+c+d.
\]

On the subspace of vectors constant on each part, the Laplacian is represented in the normalized part basis by
\[
Q=
\begin{pmatrix}
b&-\sqrt{ab}&0&0\\
-\sqrt{ab}&a+c&-\sqrt{bc}&0\\
0&-\sqrt{bc}&b+d&-\sqrt{cd}\\
0&0&-\sqrt{cd}&c
\end{pmatrix}. \tag{10}
\]
On the subspace supported in \(V_i\) and summing to zero there, the Laplacian is
\[
L(G[V_i])+\delta_i I,
\]
where
\[
(\delta_1,\delta_2,\delta_3,\delta_4)
=(b,a+c,b+d,c).
\]
All these additional eigenvalues are at least \(1\).

Both \(G\) and \(\overline G\) have a dominating edge: choose one vertex from each of the two middle parts of the appropriate path ordering. A graph with a dominating edge contains a spanning double star. Deleting the central edge of that double star leaves two stars, whose third Laplacian eigenvalue is at least \(1\). Edge monotonicity therefore gives
\[
\lambda_3(G)\ge1,\qquad \lambda_3(\overline G)\ge1. \tag{11}
\]
Consequently, if \(0<r_1\le r_2\le r_3\) are the nonzero eigenvalues of \(Q\), then
\[
r_2\ge1. \tag{12}
\]

A determinant calculation from (10) gives the cubic whose roots are \(r_1,r_2,r_3\):
\[
p_G(z)
=
z^3-(n+b+c)z^2+
\big(n(b+c)+ad+bc\big)z-nbc. \tag{13}
\]
The complement is another \(P_4\)-substitution, in path order
\[
V_3,V_1,V_4,V_2.
\]
Its quotient cubic is
\[
p_{\overline G}(z)
=
z^3-(n+a+d)z^2+
\big(n(a+d)+ad+bc\big)z-nad. \tag{14}
\]

Suppose that
\[
a(G)\le\tau,\qquad a(\overline G)\le\tau.
\]
All nonquotient eigenvalues are at least \(1\), and by (12) the second positive quotient roots are at least \(1\). Therefore
\[
p_G(\tau)\ge0,\qquad p_{\overline G}(\tau)\ge0. \tag{15}
\]

Set
\[
A=a+d,\quad B=b+c,\quad X=ad,\quad Y=bc,\quad S=X+Y.
\]
Using
\[
\tau^2=4\tau-2,\qquad \tau^3=14\tau-8,
\]
addition of (13) and (14) at \(z=\tau\) gives
\[
p_G(\tau)+p_{\overline G}(\tau)
=
-16+6n-nS+
\tau\big(n^2-12n+28+2S\big). \tag{16}
\]

Since the part sizes are positive integers,
\[
ad\ge a+d-1,\qquad bc\ge b+c-1,
\]
and hence
\[
S\ge n-2. \tag{17}
\]
The coefficient of \(S\) in (16) is \(-n+2\tau<0\). Substituting the lower bound (17) therefore yields
\[
\begin{aligned}
p_G(\tau)+p_{\overline G}(\tau)
&\le -(n-4)^2+\tau(n-4)(n-6)\\
&=(n-4)\big(-(n-4)+\tau(n-6)\big).
\end{aligned} \tag{18}
\]
For every \(n>4\), the right side is strictly negative. This contradicts (15). Thus \(F(G)>\tau\) whenever \(n>4\).

If \(n=4\), all four nonempty parts are singletons, and the graph is \(P_4\), which gives equality. ∎

---

## 7. What remains open

Combining the results above, any graph satisfying
\[
F(G)<2-\sqrt2
\]
would necessarily have all of the following properties:

1. \(n\ge6\);
2. both \(G\) and \(\overline G\) are connected;
3. both have diameter exactly three;
4. there is a canonical induced path \(u-s-t-v\) with \(st\) dominating \(G\) and \(uv\) dominating \(\overline G\);
5. neither graph is a tree;
6. neither graph has a bridge separating two sides of order at least two;
7. it is not a generalized \(P_4\)-substitution.

For a vertex \(w\) outside the canonical path, the structural reduction only forces
\[
N(w)\cap\{s,t\}\ne\varnothing,\qquad
\{u,v\}\nsubseteq N(w).
\]
Thus there are nine possible attachment patterns to the canonical \(P_4\), and edges among the remaining vertices are still arbitrary. The arguments above do not control mixtures of those patterns. In particular, they neither prove
\[
c_*=2-\sqrt2
\]
nor produce a family with \(F(G)<2-\sqrt2\).

Accordingly, the certified global interval remains
\[
\boxed{\frac12\le c_*\le2-\sqrt2}.
\]