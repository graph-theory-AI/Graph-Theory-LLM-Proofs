```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "A selector blow-up of the known k=3 construction gives D(n,4) at least n^(7/3)/exp(O(sqrt(log n))), establishing a superquadratic diameter but not the conjectured near-cubic bound.",
  "would_publish": false,
  "caveats": "This uses the standard token-jumping/component-diameter convention, and the novelty of the amplification has not been independently literature-checked."
}
```

## 1. Statement of the partial result

I use the standard convention that two independent \(k\)-sets are adjacent when they intersect in \(k-1\) vertices, and that \(D(n,k)\) is the maximum finite diameter of a connected component of this reconfiguration graph.

The following amplification gives a stronger lower bound than the one quoted in the catalog.

### Theorem
For all sufficiently large \(n\),
\[
D(n,4)\ge
\frac{n^{7/3}}{\exp\!\bigl(O(\sqrt{\log n})\bigr)}
=n^{7/3-o(1)}.
\]

In particular,
\[
\frac{D(n,4)}{n^2}\longrightarrow\infty.
\]
Thus the subsidiary question of whether a superquadratic diameter exists has an affirmative answer, subject to verification of the construction below. The conjecture
\[
D(n,4)=n^{3-o(1)}
\]
remains open.

The only external input is the proved source-paper bound
\[
D(t,3)\ge \frac{t^2}{\exp(O(\sqrt{\log t}))}.
\]

---

## 2. Clique reformulation

Let \(G\) be the original graph and \(H=\overline G\). Independent \(k\)-sets of \(G\) are precisely \(K_k\)'s of \(H\), and two configurations are adjacent precisely when their \(K_k\)'s share a \(K_{k-1}\).

For a graph \(F\), let \(\mathcal T(F)\) denote its triangle graph: its vertices are the triangles of \(F\), with two triangles adjacent when they share an edge.

We will prove the following more general amplification.

### Proposition
For every \(t\) and every integer \(q\ge4\),
\[
D\bigl(3qt+2q+4q^3-3,4\bigr)
   \ge q^3D(t,3).
\tag{1}
\]

Taking \(t=q^2\) will give the theorem.

---

## 3. Preparing a tripartite three-token instance

Let \(G_0\) be a \(t\)-vertex graph with two independent triples at distance
\[
L=D(t,3)
\]
in one component, and let \(F_0=\overline{G_0}\). Thus \(\mathcal T(F_0)\) contains two triangles \(S,T\) at distance \(L\).

### 3.1 Tripartite lift

Construct a tripartite graph \(F_1\) with parts
\[
A=V(F_0)\times\{A\},\qquad
B=V(F_0)\times\{B\},\qquad
C=V(F_0)\times\{C\},
\]
where
\[
(u,X)(v,Y)\in E(F_1)
\quad\Longleftrightarrow\quad
X\ne Y\text{ and }uv\in E(F_0).
\]

Every triangle of \(F_1\) projects to a triangle of \(F_0\). Moreover:

* a path in \(\mathcal T(F_1)\) projects, without decreasing its length, to a path in \(\mathcal T(F_0)\);
* any path in \(\mathcal T(F_0)\) can be lifted after choosing a coloring of its initial triangle: when a vertex is replaced, give the new vertex the part of the removed vertex.

Consequently, \(F_1\) contains triangles, still denoted \(S,T\), lying in one component and satisfying
\[
\operatorname{dist}_{\mathcal T(F_1)}(S,T)\ge L.
\]

### 3.2 Exposed terminal edges

Write
\[
S=(s_A,s_B,s_C),\qquad T=(t_A,t_B,t_C).
\]
Add a new vertex \(\sigma\in A\), adjacent only to \(s_B,s_C\), and a new vertex \(\tau\in A\), adjacent only to \(t_B,t_C\). Define
\[
U=(\sigma,s_B,s_C),\qquad
V=(\tau,t_B,t_C).
\]

The edge \(\sigma s_B\) lies in exactly one triangle, namely \(U\), and \(\tau t_B\) lies in exactly one triangle, namely \(V\).

Moreover,
\[
d:=\operatorname{dist}_{\mathcal T(F)}(U,V)\ge L,
\tag{2}
\]
where \(F\) is the resulting tripartite graph. Indeed, \(U\) attaches to the clique of old triangles containing \(s_Bs_C\), every member of which is at distance at most one from \(S\); similarly for \(V\) and \(T\). Hence any route from \(U\) to \(V\) has length at least
\[
1+(L-2)+1=L.
\]
The exceptional case where \(U,V\) are directly adjacent forces \(S,T\) to share the same \(BC\)-edge, and then \(L\le1\), so (2) still holds.

The graph \(F\) has \(3t+2\) vertices.

---

## 4. A sequence of selector words

We need \(q^3\) distinct words in \(\mathbb Z_q^3\), with consecutive words differing in every coordinate.

Write
\[
r=aq^2+bq+c,\qquad 0\le a,b,c<q,
\]
and define
\[
\omega_r=(x_r,y_r,z_r)
       :=(c,\ b+c,\ a+b+c)\pmod q.
\tag{3}
\]

The map \((a,b,c)\mapsto(c,b+c,a+b+c)\) is bijective, so the \(q^3\) words are distinct. Consecutive words differ in all coordinates:

* without a carry, the coordinate differences are \((1,1,1)\);
* with a carry in \(c\), they are \((1,2,2)\);
* with simultaneous carries in \(b,c\), they are \((1,2,3)\).

All are nonzero modulo \(q\) when \(q\ge4\).

Let
\[
m=q^3
\]
and enumerate these words as
\[
\omega_i=(x_i,y_i,z_i),\qquad 1\le i\le m.
\]

---

## 5. The four-partite compatibility graph

We construct a four-partite graph \(H\), whose \(K_4\)-reconfiguration graph will have the desired diameter. Its parts are denoted \(A^\star,B^\star,C^\star,P\).

### 5.1 Blown-up core

Replace every vertex of \(F\) by \(q\) independent clones. Thus
\[
A^\star_{\rm core}=A(F)\times\mathbb Z_q,
\]
and similarly for \(B,C\). If \(uv\in E(F)\), join every clone of \(u\) to every clone of \(v\).

For each \(i\), add a controller vertex \(p_i\in P\), and join it to exactly the core vertices
\[
(a,x_i),\quad a\in A(F);
\qquad
(b,y_i),\quad b\in B(F);
\qquad
(c,z_i),\quad c\in C(F).
\tag{4}
\]

Consequently, the triangles in the core neighborhood of \(p_i\) form a copy of \(\mathcal T(F)\). Moreover, every core triangle is supported by exactly one controller, since its three clone indices determine a unique word of \(\mathbb Z_q^3\).

Let \(U_i,V_i\) denote the copies of \(U,V\) selected by the word \(\omega_i\).

### 5.2 Connectors between successive rows

For each \(1\le i<m\), add three private vertices
\[
\alpha_i\in A^\star,\qquad
\beta_i\in B^\star,\qquad
\gamma_i\in C^\star.
\]
Join each of them to both \(p_i\) and \(p_{i+1}\).

Writing
\[
V_i=(v_A^i,v_B^i,v_C^i),\qquad
U_{i+1}=(u_A^{i+1},u_B^{i+1},u_C^{i+1}),
\]
add exactly the non-controller edges needed to make the following seven triples triangles:
\[
\begin{aligned}
&V_i,\\
&(v_A^i,v_B^i,\gamma_i),\\
&(\alpha_i,v_B^i,\gamma_i),\\
&M_i:=(\alpha_i,\beta_i,\gamma_i),\\
&(u_A^{i+1},\beta_i,\gamma_i),\\
&(u_A^{i+1},u_B^{i+1},\gamma_i),\\
&U_{i+1}.
\end{aligned}
\tag{5}
\]
There are no other edges incident with the private vertices, apart from their edges to \(p_i,p_{i+1}\).

The whole graph \(H\) is four-partite, with no edges inside a part. Hence every \(K_4\) contains exactly one controller from \(P\) and one vertex from each of \(A^\star,B^\star,C^\star\).

---

## 6. Verification of the configuration graph

Fix \(i\). Configurations containing \(p_i\) correspond to triangles in its \(ABC\)-neighborhood.

Because consecutive selector words differ in all three coordinates, \(p_i\) sees none of the core vertices selected by \(\omega_{i+1}\), and conversely. Using also the exposed \(AB\)-edges of \(U,V\), direct inspection of (5) gives:

* the core configurations containing \(p_i\) induce a copy of \(\mathcal T(F)\);
* if \(i<m\), a three-edge tail runs from \(V_i\) to \(M_i\);
* if \(i>1\), a three-edge tail runs from \(M_{i-1}\) to \(U_i\);
* these tails have no other attachment to the core.

Thus, within configurations containing \(p_i\), every path from the incoming connector to the outgoing connector must traverse the core from \(U_i\) to \(V_i\), at cost at least \(d\ge L\).

It remains to check controller changes. A move replacing \(p_i\) by \(p_j\) is possible exactly when the retained \(ABC\)-triangle is supported by both controllers.

* Distinct core selector words support no common core triangle.
* A private vertex is adjacent only to the two controllers associated with its connector.
* For consecutive controllers \(p_i,p_{i+1}\), their normal core neighborhoods are disjoint in all three parts, and their only common supported triangle is \(M_i\).

Therefore the unique configuration edge changing the controller from \(p_i\) to \(p_{i+1}\) is
\[
\{p_i\}\cup M_i
\quad\longleftrightarrow\quad
\{p_{i+1}\}\cup M_i.
\tag{6}
\]
There are no controller-changing edges between nonconsecutive controllers.

The edges in (6) are consequently bridges separating controller labels
\[
\{p_1,\dots,p_i\}
\quad\text{from}\quad
\{p_{i+1},\dots,p_m\}.
\]
Any path from
\[
X=\{p_1\}\cup U_1
\quad\text{to}\quad
Y=\{p_m\}\cup V_m
\]
must cross these bridges in order and must traverse a copy of \(F\) from \(U_i\) to \(V_i\) in every row. Hence
\[
\operatorname{dist}(X,Y)
   \ge m\,d
   \ge q^3L.
\tag{7}
\]
In fact the construction gives the exact value
\[
m\,d+7(m-1),
\]
but the lower bound (7) is sufficient.

Finally, take \(G=\overline H\). Its independent \(4\)-set reconfiguration graph is exactly the \(K_4\)-overlap graph just analyzed.

### Vertex count

The blown-up core has
\[
q(3t+2)
\]
vertices. There are \(q^3\) controllers and \(3(q^3-1)\) private connector vertices. Thus
\[
|V(H)|=q(3t+2)+q^3+3(q^3-1)
      =3qt+2q+4q^3-3.
\]
Together with (7), this proves Proposition (1).

---

## 7. Asymptotic consequence

Use the source paper's established estimate
\[
D(t,3)\ge
\frac{t^2}{\exp(O(\sqrt{\log t}))}.
\]
Set \(t=q^2\). The construction then has
\[
N_q=7q^3+2q-3=\Theta(q^3)
\]
vertices and diameter at least
\[
q^3D(q^2,3)
 \ge
\frac{q^7}{\exp(O(\sqrt{\log q}))}.
\]
Since \(q=\Theta(N_q^{1/3})\),
\[
D(N_q,4)\ge
\frac{N_q^{7/3}}{\exp(O(\sqrt{\log N_q}))}.
\]

For arbitrary sufficiently large \(n\), choose the largest \(q\) with \(N_q\le n\) and add isolated vertices to \(H\), equivalently universal vertices to \(G\). Such vertices lie in no \(K_4\) of \(H\), so the constructed component is unchanged. Since \(N_q=\Theta(n)\), this gives
\[
\boxed{
D(n,4)\ge
\frac{n^{7/3}}{\exp(O(\sqrt{\log n}))}
}.
\]

## 8. Remaining gap

This establishes exponent \(7/3-o(1)\), not \(3-o(1)\). The selector amplification has the general scale
\[
n=O(qt+q^3),\qquad
\operatorname{diameter}\ge q^3D(t,3).
\]
With \(D(t,3)=t^{2-o(1)}\), balancing \(qt\) and \(q^3\) forces \(t\asymp q^2\), yielding exponent \(7/3\). A substantially different construction is therefore needed to approach the conjectured cubic exponent.

I have not independently verified whether this amplification already exists in the literature; the mathematical argument above is otherwise self-contained apart from the source paper's proved \(k=3\) lower bound.