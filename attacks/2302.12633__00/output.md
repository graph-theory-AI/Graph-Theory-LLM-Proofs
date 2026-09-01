```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bounds hold, with matching examples, for the unbounded-treewidth planar class obtained by attaching arbitrary trees to a planar core of quadratic metric growth.",
  "would_publish": false,
  "caveats": "This gives no universal improvement for planar graphs whose 2-core has superquadratic or exponential ball growth, and novelty relative to all follow-up literature was not checked."
}
```

# 1. Definitions and statement of the partial result

For a graph \(G\), a nonempty set \(A\subseteq V(G)\), and \(r\ge 0\), write
\[
\mathcal N_r(G,A)
   :=\{B_r^G(v)\cap A:v\in V(G)\}.
\]
The truncated \(r\)-profile of \(v\) on \(A\) is
\[
\rho_r^G(v,A)(a)=
\begin{cases}
d_G(v,a),&d_G(v,a)\le r,\\
\infty,&d_G(v,a)>r,
\end{cases}
\]
and
\[
\mathcal P_r(G,A):=\{\rho_r^G(v,A):v\in V(G)\}.
\]

A **tree extension** of a graph \(H\) is obtained by taking, for every \(x\in V(H)\), a rooted tree \(T_x\) whose root is \(x\), with the trees otherwise vertex-disjoint, and adding no edges other than those of \(H\) and the \(T_x\). Thus every part outside \(H\) attaches to \(H\) through one vertex.

Put
\[
\beta_r(H):=\max_{x\in V(H)}|B_r^H(x)|.
\]

## Partial theorem

Let \(G\) be a tree extension of \(H\). Then for every nonempty \(A\subseteq V(G)\),
\[
\boxed{
|\mathcal N_r(G,A)|
 \le \bigl(2(r+1)(r+2)+\beta_r(H)\bigr)|A|+1
}
\tag{1}
\]
and
\[
\boxed{
|\mathcal P_r(G,A)|
 \le \bigl(14(r+1)^2+(r+1)\beta_r(H)\bigr)|A|+1.
}
\tag{2}
\]

Consequently, if
\[
|B_s^H(x)|\le C(s+1)^2
\qquad\text{for all }x\in V(H),\ s\ge0,
\tag{3}
\]
then
\[
|\mathcal N_r(G,A)|=O_C(r^2|A|),
\qquad
|\mathcal P_r(G,A)|=O_C(r^3|A|).
\tag{4}
\]

If \(H\) is planar, then every such tree extension is planar. The class has unbounded treewidth, since \(H\) may be an arbitrarily large square grid.

Moreover, both exponents in (4) are best possible within this class.

# 2. Two lemmas for trees

## Lemma 1: neighborhoods in a tree

For every tree \(T\), nonempty \(A\subseteq V(T)\), and \(r\ge0\),
\[
|\mathcal N_r(T,A)|\le (2r+1)|A|+1.
\tag{5}
\]

### Proof

Regard \(T\) as a geometric tree by replacing each edge by a unit interval. Let
\[
X=A\cap B_r(v)\ne\varnothing.
\]
Let \(D\) be the diameter of \(X\), let \(\varrho=D/2\), and let \(c\) be the midpoint of a diametral pair \(a,b\in X\).

In a geometric tree, \(B_\varrho(c)\) is the unique smallest ball containing \(X\). Furthermore,
\[
B_\varrho(c)\subseteq B_r(v).
\tag{6}
\]
Indeed, if \(p\) is the projection of \(v\) onto the path \(aTb\), then
\[
\max\{d(v,a),d(v,b)\}=d(v,c)+\varrho.
\]
Since both \(a,b\in B_r(v)\), this is at most \(r\). Hence every \(y\) with
\(d(y,c)\le\varrho\) satisfies
\[
d(v,y)\le d(v,c)+\varrho\le r.
\]
It follows that
\[
X=A\cap B_\varrho(c).
\tag{7}
\]

The possible values of \(\varrho\) are
\[
0,\frac12,1,\frac32,\ldots,r.
\]
Fix one positive value \(\varrho\). Root the geometric tree at an arbitrary point \(o\). For a ball \(B_\varrho(c)\) arising as above, the diametral witnesses \(a,b\) lie in different components of \(T-c\). At most one of these components is the component towards \(o\), so one witness, say \(a\), is a descendant of \(c\). Thus \(c\) is the unique point on the path \(oTa\) at distance \(\varrho\) from \(a\). Hence there are at most \(|A|\) possible centers \(c\) for each fixed \(\varrho\).

For \(\varrho=0\), the center belongs to \(A\), again giving at most \(|A|\) possibilities. Thus there are at most \((2r+1)|A|\) nonempty traces, plus the empty trace. ∎

## Lemma 2: profiles in a tree

For every tree \(T\), nonempty \(A\subseteq V(T)\), and \(r\ge0\),
\[
|\mathcal P_r(T,A)|\le 4(r+1)^2|A|+1.
\tag{8}
\]

### Proof

Let \(S\) be the minimal subtree of \(T\) containing \(A\). Every vertex
\(v\in V(T)\) has a unique projection \(x\in V(S)\): if \(v\notin S\), the component of \(T-S\) containing \(v\) attaches to \(S\) at \(x\). Put
\[
h=d_T(v,x).
\]
Then for every \(a\in A\),
\[
d_T(v,a)=h+d_S(x,a).
\tag{9}
\]
Thus the profile of \(v\) is determined by the pair \((x,h)\). A nonempty profile requires
\[
h+d_S(x,A)\le r.
\tag{10}
\]

We count the possible pairs satisfying (10). Mark all vertices of \(A\), together with all vertices of \(S\) of degree at least three. Suppressing all unmarked degree-two vertices gives a tree with at most \(2|A|-2\) vertices and therefore at most \(2|A|-3\) edges when \(|A|\ge2\).

Each reduced edge corresponds to a path \(P\) in \(S\) whose internal vertices are unmarked and have degree two. Both sides of \(P\) contain a vertex of \(A\). If \(x\in P\) satisfies \(d_S(x,A)\le r\), then \(x\) lies within distance \(r\) of at least one endpoint of \(P\). Hence there are at most \(2(r+1)\) possible vertices \(x\) on \(P\). For each such \(x\), there are at most \(r+1\) possible values of \(h\).

Therefore the total number of relevant pairs is at most
\[
2(r+1)^2(2|A|-3)<4(r+1)^2|A|.
\]
The case \(|A|=1\) is immediate. Finally, all pairs violating (10) give the single all-\(\infty\) profile. ∎

Both tree bounds have the correct orders: trees can have neighborhood complexity \(\Omega(r|A|)\), while a path with a pendant path attached at each of \(\Theta(r)\) positions and two marked endpoints gives \(\Omega(r^2|A|)\) profiles.

# 3. Proof of the tree-extension theorem

Let
\[
A_x:=A\cap V(T_x),\qquad n_x:=|A_x|.
\]
These sets partition \(A\). For \(a\in A_y\), put
\[
\delta(a):=d_{T_y}(y,a).
\]
For \(v\in T_x\), write
\[
h(v):=d_{T_x}(v,x).
\]

If \(y\ne x\), then every path from \(v\) to \(a\in A_y\) passes through \(x\) and \(y\), so
\[
d_G(v,a)=h(v)+d_H(x,y)+\delta(a).
\tag{11}
\]

We distinguish occupied roots \(x\), for which \(A_x\ne\varnothing\), from empty roots.

## 3.1. Neighborhood traces at occupied roots

Fix \(x\) with \(A_x\ne\varnothing\). The local part
\[
B_r(v)\cap A_x
\]
has at most
\[
(2r+1)n_x+1
\]
possibilities by Lemma 1.

If \(h(v)\le r\), the external part of the trace is a deterministic function of \(x\) and \(h(v)\), by (11). Thus the global trace is determined by the local trace and one of the \(r+1\) possible values of \(h(v)\).

If \(h(v)>r\), the external part is empty, and the local trace alone determines the global trace. Hence the number contributed by the fiber \(T_x\) is at most
\[
(r+2)\bigl((2r+1)n_x+1\bigr).
\]
Summing over occupied roots and using that their number is at most \(|A|\) gives
\[
\sum_{x:A_x\ne\varnothing}
|\{\text{traces centered in }T_x\}|
\le 2(r+1)(r+2)|A|.
\tag{12}
\]

## 3.2. Neighborhood traces at empty roots

Now let \(A_x=\varnothing\), and define
\[
D_x(a):=d_H(x,y)+\delta(a)
\qquad(a\in A_y).
\]
For a center at depth \(h\) in \(T_x\), its trace is
\[
\{a\in A:D_x(a)\le r-h\}.
\tag{13}
\]
For fixed \(x\), as \(h\) varies, these are nested sets. The number of distinct nonempty sets in (13) is at most
\[
I_x:=|\{a\in A:D_x(a)\le r\}|.
\]
Interchanging the order of summation,
\[
\begin{aligned}
\sum_x I_x
&\le
\sum_{a\in A_y}
|\{x:d_H(x,y)+\delta(a)\le r\}|\\
&\le
\sum_{a\in A}|B_{r-\delta(a)}^H(y)|\\
&\le \beta_r(H)|A|.
\end{aligned}
\tag{14}
\]
Adding the single empty trace, (12) and (14) prove (1).

## 3.3. Profiles at occupied roots

Fix \(x\) with \(A_x\ne\varnothing\). For centers with \(h(v)\le r\), consider the local profile on
\[
A_x\cup\{x\}.
\]
It records both the profile on \(A_x\) and the exact value \(h(v)\). By Lemma 2, the number of possibilities is at most
\[
4(r+1)^2(n_x+1)+1.
\]
This augmented local profile determines the entire global profile via (11).

For centers with \(h(v)>r\), every external coordinate is \(\infty\), so the profile is determined by the local profile on \(A_x\), of which there are at most
\[
4(r+1)^2n_x+1.
\]
Summing these bounds over occupied roots gives at most
\[
14(r+1)^2|A|
\tag{15}
\]
profiles.

## 3.4. Profiles at empty roots

For an empty root \(x\), every center at depth \(h\) has profile
\[
a\longmapsto
\begin{cases}
h+D_x(a),&h+D_x(a)\le r,\\
\infty,&h+D_x(a)>r.
\end{cases}
\tag{16}
\]
There are at most \(r+1\) nonempty profiles for each root \(x\) for which \(I_x>0\). The number of such roots is at most
\[
\sum_x I_x\le\beta_r(H)|A|.
\]
Thus the empty fibers contribute at most
\[
(r+1)\beta_r(H)|A|
\]
nonempty profiles. Adding the all-\(\infty\) profile and (15) proves (2). ∎

# 4. Interpretation via the 2-core

If a connected graph \(G\) has nonempty 2-core \(H\), every component of \(G-V(H)\) is a tree attached to exactly one vertex of \(H\). Indeed, such a component cannot contain a cycle, and attachment to two core vertices would put the connecting path into a subgraph of minimum degree at least two, contradicting maximality of the 2-core.

Thus the theorem applies directly with \(H\) equal to the 2-core.

In particular:

> If the 2-core of a planar graph has uniformly quadratic ball growth, then its neighborhood complexity is \(O(r^2|A|)\) and its profile complexity is \(O(r^3|A|)\).

This includes planar graphs obtained from square grids, triangular-grid pieces, or other quadratic-growth planar cores by attaching arbitrary trees of unrestricted degrees and depths. It is not a bounded-treewidth result.

# 5. Matching constructions inside this subclass

The upper exponents are both attained by tree extensions of finite square grids.

## 5.1. Profile lower bound \(\Omega(r^3)\)

Let
\[
H_q=\{0,\ldots,q\}\square\{0,\ldots,q\}.
\]
At every grid vertex \(z=(i,j)\), attach a pendant path of length \(q\), and let \(v_{i,j,h}\) be its vertex at depth \(h\), where \(0\le h\le q\).

Take
\[
A=\{a=(0,0),\,b=(q,0),\,c=(0,q)\}.
\]
For \(r\ge3q\),
\[
\begin{aligned}
d(v_{i,j,h},a)&=h+i+j,\\
d(v_{i,j,h},b)&=h+q-i+j,\\
d(v_{i,j,h},c)&=h+i+q-j.
\end{aligned}
\tag{17}
\]
All three distances are at most \(3q\), and the triple determines \(i,j,h\):
\[
i=\frac{d_a-d_b+q}{2},
\qquad
j=\frac{d_a-d_c+q}{2},
\qquad
h=d_a-i-j.
\]
Therefore the \((q+1)^3\) selected centers have distinct profiles. Taking
\(q=\lfloor r/3\rfloor\) gives
\[
\frac{|\mathcal P_r(G,A)|}{|A|}=\Omega(r^3).
\]

## 5.2. Neighborhood lower bound \(\Omega(r^2)\)

Again use \(H_q\) and attach a distinguished path of length \(q\) at every grid vertex. Let the three portals be
\[
a=(0,0),\qquad b=(q,0),\qquad c=(0,q).
\]

Fix a radius \(R\ge6\) and put \(q=\lfloor R/6\rfloor\). At each portal
\(p\in\{a,b,c\}\), attach internally disjoint terminal paths indexed by
\(k=0,\ldots,3q\), of lengths
\[
\ell_k=R-3q+k.
\]
Let \(p_k\) be the terminal endpoint, and put
\[
A=\{p_k:p\in\{a,b,c\},\ 0\le k\le3q\}.
\]
Thus
\[
|A|=3(3q+1)=9q+3.
\]

For the center \(v_{i,j,h}\), define
\[
\begin{aligned}
D_a&=h+i+j,\\
D_b&=h+q-i+j,\\
D_c&=h+i+q-j.
\end{aligned}
\]
Each lies between \(0\) and \(3q\). Moreover,
\[
d(v_{i,j,h},p_k)=D_p+R-3q+k,
\]
so
\[
p_k\in B_R(v_{i,j,h})
\quad\Longleftrightarrow\quad
k\le3q-D_p.
\tag{18}
\]
Thus the intersection with the terminal group at portal \(p\) determines \(D_p\). The three values \(D_a,D_b,D_c\) then determine \(i,j,h\) by the same formulas as above.

Hence the \((q+1)^3\) centers give distinct radius-\(R\) neighborhood traces, and
\[
\frac{|\mathcal N_R(G,A)|}{|A|}
\ge
\frac{(q+1)^3}{9q+3}
=\Omega(R^2).
\]

The base grids satisfy
\[
|B_s^{H_q}(x)|\le (2s+1)^2\le4(s+1)^2,
\]
so these examples belong to the quadratic-core class.

Consequently, for the class of planar tree extensions of planar quadratic-growth cores,
\[
\boxed{\text{profile complexity }=\Theta(r^3)}
\]
and
\[
\boxed{\text{neighborhood complexity }=\Theta(r^2)}.
\]

# 6. Remaining gap

The quadratic-growth hypothesis on the 2-core is not automatic for planar graphs. For example, take a large plane binary tree and join its leaves in their cyclic order by an outer cycle. The resulting planar graph has minimum degree at least two, hence is its own 2-core, while balls around the root contain exponentially many vertices up to the depth of the tree.

For such graphs, \(\beta_r(H)\) can be exponential, and bounds (1)–(2) become useless compared with the known universal \(O(r^4|A|)\) result. A complete proof would have to count traces in these high-growth planar cores without counting their vertices individually. The argument above does not do that, so neither of the two original planar gaps is resolved universally.