```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The finiteness conjecture remains unresolved, but there is an explicit 10-vertex connected bridgeless cubic exception, an exact component-selection characterization, and two broad sufficient conditions for colorability.",
  "would_publish": false,
  "caveats": "No finite bound or infinite counterfamily is obtained; the standard proper-neighborhood definition is assumed, and the literature novelty of the 10-vertex exception was not checked."
}
```

# 1. Definition and scope

I use the definition suggested by the cited NMNR correspondence:

> A **2-homogeneous coloring** of a cubic graph \(G\) is a proper vertex coloring \(\varphi\) such that
> \[
> |\varphi(N(v))|=2
> \qquad\text{for every }v\in V(G).
> \]
> Thus the three neighbors of every vertex have color multiplicities \(2+1\): their colors are neither monochromatic nor rainbow.

Colors are not bounded in number. Graphs are assumed finite and simple.

I do not resolve the asserted finiteness. I give:

1. an exact structural reformulation;
2. an explicit connected bridgeless cubic exception on ten vertices;
3. an analysis showing that its most obvious serial inflation becomes colorable;
4. two elementary but fairly broad sufficient conditions.

I make no claim that the ten-vertex graph is new to the literature.

---

# 2. An exact component-selection characterization

For every \(v\in V(G)\), choose one of the three unordered pairs contained in \(N(v)\). Let that chosen pair be \(P_v\), and let \(s(v)\) be the remaining, singleton neighbor. Define an auxiliary graph
\[
Q=Q(P)
\]
on \(V(G)\) by adding the edge \(xy\) whenever \(P_v=\{x,y\}\) for some \(v\). Parallel choices are irrelevant; only connected components matter.

## Proposition 2.1

A cubic graph \(G\) admits a 2-homogeneous coloring if and only if one can choose the pairs \(P_v\) so that:

1. no connected component of \(Q\) contains both ends of an edge of \(G\); and
2. for every \(v\), the singleton \(s(v)\) is not in the \(Q\)-component containing the two vertices of \(P_v\).

### Proof

Suppose first that \(\varphi\) is 2-homogeneous. For each \(v\), let \(P_v\) be the unique pair of equally colored vertices in \(N(v)\). Every edge of \(Q\) therefore joins vertices of the same color, so every component of \(Q\) is monochromatic. Properness of \(\varphi\) gives condition 1. The singleton neighbor has a different color from the repeated pair, giving condition 2.

Conversely, suppose a selection satisfying 1 and 2 is given. Give each component of \(Q\) its own color. Condition 1 makes this coloring proper. At a vertex \(v\), the two members of \(P_v\) have the same color, while condition 2 says that \(s(v)\) has a different color. Hence \(N(v)\) has exactly two colors. ∎

This removes color names from the problem entirely: the issue is whether one can choose one pair in each neighborhood without creating a forbidden connected equality component.

It also gives an exact \(O(3^n\operatorname{poly}(n))\) decision algorithm. For each of the \(3^n\) choices of singleton neighbors, construct \(Q\) using union-find and test the two conditions above. A successful assignment directly returns a coloring by component labels.

---

# 3. A ten-vertex bridgeless cubic exception

Let \(R\) be a triangular prism with one top edge deleted. More explicitly, let its top vertices be \(a,b,c\), its bottom vertices \(A,B,C\), and take edges
\[
ac,\ bc,\ AB,\ BC,\ CA,\ aA,\ bB,\ cC.
\]
Thus \(a\) and \(b\) have degree two in \(R\).

Let \(D\) be the diamond \(K_4-rs\), with vertices \(p,q,r,s\) and edges
\[
pq,\ pr,\ ps,\ qr,\ qs.
\]
The vertices \(r,s\) have degree two in \(D\).

Finally add the edges
\[
ar,\qquad bs.
\]
Call the resulting graph \(H\). It has ten vertices and is cubic.

## Lemma 3.1: the diamond is an equality gadget

In every 2-homogeneous coloring of a cubic graph containing this diamond with \(p,q\) having exactly the displayed neighbors,
\[
\varphi(r)=\varphi(s).
\]

### Proof

At \(p\), the neighborhood is \(\{q,r,s\}\). Since \(q\) is adjacent to both \(r\) and \(s\), properness gives
\[
\varphi(q)\ne\varphi(r),\qquad
\varphi(q)\ne\varphi(s).
\]
For these three neighbor colors to use exactly two colors, \(r\) and \(s\) must have the same color. ∎

## Lemma 3.2: the deleted-edge prism forces inequality

Suppose vertices \(x,y\) are attached to \(a,b\), respectively, in \(R\). Any proper coloring satisfying the 2-homogeneous condition at all six vertices of \(R\) must satisfy
\[
\varphi(x)\ne\varphi(y).
\]

### Proof

The bottom triangle has three distinct colors. Write
\[
\varphi(A)=\alpha,\qquad
\varphi(B)=\beta,\qquad
\varphi(C)=\gamma.
\]

At \(A,B,C\), respectively, the condition on the neighborhood gives
\[
\varphi(a)\in\{\beta,\gamma\},\qquad
\varphi(b)\in\{\alpha,\gamma\},\qquad
\varphi(c)\in\{\alpha,\beta\}.
\]

Now
\[
N(c)=\{a,b,C\}.
\]
Using also the proper edges \(ac\) and \(bc\), there are only two possible cases:

\[
\begin{array}{c|ccc}
&\varphi(a)&\varphi(b)&\varphi(c)\\ \hline
\text{I}&\gamma&\alpha&\beta\\
\text{II}&\beta&\gamma&\alpha.
\end{array}
\]

Indeed, \((\varphi(a),\varphi(b))=(\beta,\alpha)\) makes \(N(c)\) rainbow, while \((\gamma,\gamma)\) makes it monochromatic.

In Case I, at \(a\) the neighbor colors are
\[
\varphi(x),\beta,\alpha,
\]
so
\[
\varphi(x)\in\{\alpha,\beta\}.
\]
At \(b\), the neighbor colors are
\[
\varphi(y),\beta,\beta,
\]
so \(\varphi(y)\ne\beta\); properness of \(by\), since \(\varphi(b)=\alpha\), also gives \(\varphi(y)\ne\alpha\). Hence \(\varphi(x)\ne\varphi(y)\).

In Case II, at \(b\) the colors
\[
\varphi(y),\alpha,\beta
\]
force \(\varphi(y)\in\{\alpha,\beta\}\). At \(a\), the colors
\[
\varphi(x),\alpha,\alpha
\]
force \(\varphi(x)\ne\alpha\), while properness of \(ax\), since \(\varphi(a)=\beta\), gives \(\varphi(x)\ne\beta\). Again \(\varphi(x)\ne\varphi(y)\). ∎

## Theorem 3.3

The graph \(H\) is a connected bridgeless cubic graph with no 2-homogeneous coloring.

### Proof

Cubicity and connectedness are immediate.

Every edge is on a cycle:

- all edges of the diamond lie in one of the triangles \(pqr\) or \(pqs\);
- the bottom edges lie in the triangle \(ABC\);
- the edges \(ac,bc,aA,bB\) lie on
  \[
  a-c-b-B-A-a;
  \]
- the edge \(cC\) lies on
  \[
  c-C-A-a-c;
  \]
- the two joining edges lie on
  \[
  a-r-p-s-b-c-a.
  \]

Thus \(H\) is bridgeless.

If \(\varphi\) were 2-homogeneous, Lemma 3.1 would give
\[
\varphi(r)=\varphi(s).
\]
But \(r,s\) are precisely the two external vertices attached to \(a,b\) in Lemma 3.2, which requires
\[
\varphi(r)\ne\varphi(s).
\]
This is a contradiction. ∎

Thus there are at least two connected bridgeless cubic exceptions: \(K_4\) and \(H\). For \(K_4\), every proper coloring gives three distinct colors in every neighborhood.

This does not contradict the conjecture, which permits finitely many exceptions.

---

# 4. The natural diamond-chain inflation does not give infinitely many exceptions

It is tempting to replace the single diamond in \(H\) by a long chain of diamonds. This does not produce an infinite counterfamily.

For \(k\geq1\), take diamonds
\[
D_i=\{p_i,q_i,x_i,y_i\},\qquad
E(D_i)=\{p_iq_i,p_ix_i,p_iy_i,q_ix_i,q_iy_i\}.
\]
Join
\[
y_i x_{i+1}\qquad(1\le i<k),
\]
and attach the two ends to the deleted-edge prism \(R\) by
\[
ax_1,\qquad by_k.
\]
Call the resulting bridgeless cubic graph \(H_k\). Then \(H_1=H\).

## Proposition 4.1

The graph \(H_1\) is not 2-homogeneously colorable, whereas every \(H_k\) with \(k\ge2\) has a 2-homogeneous coloring using three colors.

### Proof

The case \(k=1\) is Theorem 3.3.

Let \(k\ge2\), and use colors \(\{1,2,3\}\). Choose
\[
t_1,\dots,t_k\in\{1,2,3\}
\]
such that adjacent terms differ and \(t_1\ne t_k\). Such a sequence exists for every \(k\ge2\).

In \(D_i\), color both terminals \(x_i,y_i\) with \(t_i\), and color \(p_i,q_i\) with the other two colors. Every central diamond vertex then sees a \(2+1\) pattern. At an internal terminal, its two central neighbors have the two colors different from \(t_i\), and the adjacent terminal in the next diamond has one of those colors because its color differs from \(t_i\). Hence every diamond vertex satisfies the condition.

Relabeling colors, assume
\[
t_1=1,\qquad t_k=3.
\]
Color the deleted-edge prism by
\[
\varphi(A)=1,\quad \varphi(B)=2,\quad \varphi(C)=3,
\]
and
\[
\varphi(a)=3,\quad \varphi(b)=1,\quad \varphi(c)=2.
\]
With external colors \(1\) at \(a\) and \(3\) at \(b\), direct inspection gives:

\[
\begin{array}{c|c}
v&\varphi(N(v))\\ \hline
a&\{1,1,2\}\\
b&\{2,2,3\}\\
c&\{1,3,3\}\\
A&\{2,3,3\}\\
B&\{1,1,3\}\\
C&\{1,2,2\}.
\end{array}
\]

The coloring is proper as well. Thus \(H_k\) is 2-homogeneously colorable for every \(k\ge2\). ∎

This calculation shows why the equality gadget cannot simply be stretched to disprove finiteness: adjacent diamonds can change their terminal color, and a third color removes any parity obstruction.

---

# 5. Two sufficient conditions

## Proposition 5.1: triangle-covered cubic graphs

Let \(G\) be a connected simple cubic graph in which every vertex belongs to a triangle. Then \(G\) has a 2-homogeneous coloring unless \(G=K_4\).

### Proof

If \(G\ne K_4\), Brooks' theorem gives a proper 3-coloring of \(G\).

Fix \(v\), and let \(x,y\) be its two neighbors in a triangle containing \(v\). Since \(xy\in E(G)\), the colors of \(x,y\) are distinct. Both differ from the color of \(v\), so they are the two other colors in the 3-coloring. The third neighbor of \(v\) also differs from \(v\), and hence repeats one of the colors of \(x,y\). Thus \(N(v)\) has exactly two colors.

For \(K_4\), every proper coloring assigns four distinct colors to the vertices, so every neighborhood is rainbow. ∎

In particular, this covers all connected cubic graphs with a spanning triangle factor, apart from \(K_4\).

## Proposition 5.2: a favorable perfect matching

Suppose a cubic graph \(G\) has a perfect matching \(M\) such that:

1. every component of \(G-M\) is an even cycle; and
2. every edge of \(M\) joins two distinct components of \(G-M\).

Then \(G\) has a 2-homogeneous coloring.

### Proof

For every cycle \(C\) of \(G-M\), choose two colors
\[
\alpha_C,\beta_C
\]
not used for any other cycle. Alternate them around \(C\), which is possible because \(C\) is even.

This is proper on \(G-M\). Every matching edge joins different cycles, whose palettes are disjoint, so it is also proper on \(M\).

For \(v\in C\), its two cycle neighbors both have the color opposite to \(\varphi(v)\) in the alternating coloring. Its matching neighbor lies in a different cycle and therefore has a color different from both \(\alpha_C\) and \(\beta_C\). Consequently the three neighbor colors have multiplicities \(2+1\). ∎

In terms of Proposition 2.1, one chooses at every vertex the pair formed by its two neighbors on the complementary even cycle.

---

# 6. Computational formulation

For a fully reproducible exhaustive check on a given cubic graph \(G\), no a priori color bound beyond \(n=|V(G)|\) is needed.

For each vertex \(v\), order its neighbors as
\[
N(v)=\{n_v(0),n_v(1),n_v(2)\}.
\]
Enumerate all functions
\[
s:V(G)\longrightarrow\{0,1,2\},
\]
where \(n_v(s(v))\) is the singleton neighbor. For each such \(s\):

1. initialize a union-find structure on \(V(G)\);
2. for each \(v\), union the other two members of \(N(v)\);
3. reject if an edge \(xy\in E(G)\) has \(x,y\) in the same union-find class;
4. reject if, for some \(v\), the singleton \(n_v(s(v))\) is in the same class as either member of the selected pair;
5. otherwise return the union-find classes as the color classes.

By Proposition 2.1 this algorithm is exact. It can be combined with a generator of connected simple cubic graphs followed by a standard bridge test. I have not run such an enumeration here, so I claim no computational classification or order bound.

---

# 7. What remains open

The ten-vertex graph \(H\) shows that bridgelessness does not eliminate all local equality-versus-inequality obstructions. However:

- it provides only one additional exception;
- its obvious diamond-chain inflation is colorable as soon as the chain has length at least two;
- the sufficient conditions above do not cover general cyclically highly connected cubic graphs or general snarks;
- Proposition 2.1 gives no reason that the forbidden component configurations can occur only in bounded order.

Thus neither direction of the conjecture is settled. A proof would need a universal order bound or a reduction theorem for large bridgeless cubic graphs. A disproof would require an infinite family of pair-selection obstructions; the natural family arising from the ten-vertex example does not work.