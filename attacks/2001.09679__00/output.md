```json
{
  "verdict": "proved",
  "confidence": "medium",
  "one_line": "A two-dimensional grid thickening of bounded-degree expanders attains expansion exponent 1/(2ε)-1 while retaining separator exponent 1-ε, closing Dvořák's gap.",
  "would_publish": true,
  "caveats": "The construction and proof are new and unrefereed; literature priority has not been independently checked."
}
```

# Statement

For a graph \(G\), let \(\operatorname{sep}(G)\) be the minimum size of a vertex set \(Z\) such that every component of \(G-Z\) has at most \(2|V(G)|/3\) vertices. For a hereditary class \(\mathcal C\), use the standard monotone separation function
\[
s_{\mathcal C}(n)
 =\max\{\operatorname{sep}(G):G\in\mathcal C,\ |V(G)|\le n\}.
\]
Let
\[
\nabla_{\mathcal C}(r)
 =\sup_{G\in\mathcal C}\max_{M\preccurlyeq_r G}
   \frac{|E(M)|}{|V(M)|},
\]
where \(M\preccurlyeq_r G\) means that \(M\) is an \(r\)-shallow minor of \(G\).

The parameter in the source paper is
\[
b_\varepsilon
 =\inf\left\{b:\begin{array}{l}
 \text{there is a hereditary class }\mathcal C\text{ with}\\
 s_{\mathcal C}(n)=\Theta(n^{1-\varepsilon})
 \text{ and }\nabla_{\mathcal C}(r)=O(r^b)
 \end{array}\right\}.
\]

Dvořák proved
\[
b_\varepsilon\ge \frac1{2\varepsilon}-1
\qquad(0<\varepsilon<1/2).
\]
I prove the matching construction.

## Theorem

For every \(0<\varepsilon<1/2\), there is a monotone graph class \(\mathcal C_\varepsilon\) such that
\[
s_{\mathcal C_\varepsilon}(n)=\Theta(n^{1-\varepsilon})
\]
and
\[
\nabla_{\mathcal C_\varepsilon}(r)
 =O\!\left(r^{\,1/(2\varepsilon)-1}\right).
\]
Consequently,
\[
\boxed{\,b_\varepsilon=\frac1{2\varepsilon}-1\,}
\qquad(0<\varepsilon<1/2).
\]

Together with the known value \(b_\varepsilon=0\) for \(\varepsilon\ge1/2\), this also shows that \(b_\varepsilon\) is continuous at \(\varepsilon=1/2\).

# 1. The planar block

Fix a sufficiently large integer \(L\). Let \(Q_L\) be the square grid
\[
P_{40L+1}\square P_{40L+1}.
\]
Thus
\[
M_L:=|V(Q_L)|=(40L+1)^2=\Theta(L^2).
\]

Choose four disjoint intervals \(P_1,\dots,P_4\), each consisting of \(L\) consecutive vertices and centered on a different side of the outer face of \(Q_L\). Call them the ports. They may be chosen so that
\[
\operatorname{dist}_{Q_L}(P_i,P_j)\ge 30L
\qquad(i\ne j).
\]

We use three elementary properties of this block.

### Lemma 1

There are absolute constants \(c,C>0\) such that the following hold.

1. For every \(A\subseteq V(Q_L)\), writing
   \[
   \mu(A)=\min\{|A|,M_L-|A|\},
   \]
   and denoting by \(\partial_Q A\) the set of grid edges with one endpoint in \(A\), one outside \(A\),
   \[
   |\partial_Q A|\ge c\frac{\mu(A)}L.
   \tag{1}
   \]

2. Round \(A\) to state \(1\) if \(|A|\ge M_L/2\), and to state \(0\) otherwise. For each port \(P_i\), let \(D_i(A)\) be the number of port vertices whose membership in \(A\) disagrees with that state. Then
   \[
   D_i(A)\le |\partial_Q A|+\frac{\mu(A)}L
            \le C|\partial_Q A|.
   \tag{2}
   \]

3. For each port \(P_i\), there are \(L\) pairwise vertex-disjoint grid crosscuts
   \[
   C_i(1),\dots,C_i(L),
   \]
   each separating \(P_i\) from the other three ports. The four collar regions containing these families can be chosen mutually disjoint.

#### Proof

Inequality (1) is the standard edge-isoperimetric bound for a square grid of side \(\Theta(L)\). It also follows directly by compressing every row and column of the smaller of \(A\) and its complement: compression does not increase edge boundary, and the boundary of the resulting Ferrers diagram is at least a constant times its area divided by \(L\).

For (2), suppose first that \(A\) has state \(1\). From each vertex of \(P_i\setminus A\), draw the length-\(L\) grid path perpendicular to the corresponding side. These paths are pairwise vertex-disjoint. If such a path meets \(A\), it contains an edge of \(\partial_Q A\); otherwise all its \(L\) vertices lie in \(V(Q_L)\setminus A\). Hence
\[
|P_i\setminus A|
 \le |\partial_Q A|+\frac{|V(Q_L)\setminus A|}{L}.
\]
The state-\(0\) case follows by interchanging \(A\) and its complement. The second inequality in (2) follows from (1).

For (3), take nested U-shaped grid paths surrounding the relevant boundary interval. Because the square has side \(40L\) while each port has length \(L\), one can choose \(L\) disjoint such paths for each port, and the four systems can be placed in disjoint collar regions. ∎

# 2. Thickening an expander into a surface graph

There is an absolute \(\alpha>0\) such that, for every sufficiently large \(g\), there is a simple \(4\)-regular graph \(H_g\) satisfying
\[
|\delta_{H_g}(U)|
 \ge \alpha\min\{|U|,g-|U|\}
\qquad(U\subseteq V(H_g)).
\tag{3}
\]
The standard random regular graph argument gives such graphs uniformly in \(g\).

For each \(v\in V(H_g)\), take a disjoint copy \(Q_v\) of \(Q_L\), and bijectively associate the four ports of \(Q_v\) with the four edges incident with \(v\). For every edge \(e=uv\) of \(H_g\), join the two corresponding ports by an order-preserving perfect matching of size \(L\). Denote the resulting graph by
\[
X(g,L).
\]

It has
\[
N:=|V(X(g,L))|=gM_L=\Theta(gL^2)
\tag{4}
\]
and bounded maximum degree.

## Surface genus

Embed each \(Q_v\) in a disk. For each edge \(uv\in E(H_g)\), attach a rectangular band between the corresponding boundary intervals and draw the matching edges disjointly across that band. Thus \(X(g,L)\) embeds in a surface obtained from \(g\) disks by attaching \(2g\) bands. In particular,
\[
\operatorname{eg}(X(g,L))=O(g),
\tag{5}
\]
where \(\operatorname{eg}\) denotes Euler genus.

The following standard consequence of Euler's formula will be used repeatedly.

### Lemma 2

If a simple graph \(J\) embeds in a surface of Euler genus \(\gamma\), then
\[
\frac{|E(J)|}{|V(J)|}=O(\sqrt{\gamma+1}).
\tag{6}
\]

#### Proof

Writing \(q=|V(J)|\), Euler's formula gives
\[
|E(J)|\le 3q-6+3\gamma,
\]
while simplicity gives \(|E(J)|\le q(q-1)/2\). If \(q\ge\sqrt{\gamma+1}\), use the first bound; otherwise use the second. ∎

Since minors remain embeddable in the same surface, (5) and Lemma 2 imply that every minor \(J\) of \(X(g,L)\) satisfies
\[
\frac{|E(J)|}{|V(J)|}=O(\sqrt g).
\tag{7}
\]

# 3. The full graph has separator order \(\Theta(gL)\)

We first prove a stronger edge-isoperimetric statement.

### Lemma 3

There is an absolute \(c>0\) such that, for every
\(S\subseteq V(X(g,L))\),
\[
|\partial_X S|
 \ge \frac cL\min\{|S|,N-|S|\}.
\tag{8}
\]

#### Proof

For each \(v\in V(H_g)\), put
\[
S_v=S\cap V(Q_v),\qquad
s_v=|S_v|,\qquad
\mu_v=\min\{s_v,M_L-s_v\}.
\]
Let \(b_v\) be the number of edges of \(\partial_X S\) lying inside \(Q_v\). By Lemma 1,
\[
b_v\ge c_0\frac{\mu_v}{L}.
\tag{9}
\]

Let
\[
U=\{v:s_v\ge M_L/2\}.
\]
Consider an edge \(uv\in\delta_{H_g}(U)\), say \(u\in U\) and \(v\notin U\). Its two ports are joined by \(L\) matching edges. A matching edge which does not cross \(S\) must have either:

- its endpoint in \(Q_u\) disagreeing with the state of \(Q_u\), or
- its endpoint in \(Q_v\) disagreeing with the state of \(Q_v\).

By Lemma 1,
\[
L\le c_{uv}+C(b_u+b_v),
\tag{10}
\]
where \(c_{uv}\) is the number of crossing matching edges at this interface. Summing over \(\delta_{H_g}(U)\), and using the fact that \(H_g\) has degree four, gives
\[
L|\delta_{H_g}(U)|\le C_1|\partial_X S|.
\tag{11}
\]

Moreover, (9) gives
\[
\sum_v\mu_v\le C_2L|\partial_X S|.
\tag{12}
\]

Since
\[
\left||S|-M_L|U|\right|\le\sum_v\mu_v,
\]
we have
\[
\begin{aligned}
\min\{|S|,N-|S|\}
 &\le M_L\min\{|U|,g-|U|\}+\sum_v\mu_v\\
 &\le \frac{M_L}{\alpha}|\delta_{H_g}(U)|
       +C_2L|\partial_X S|\\
 &\le C_3L|\partial_X S|,
\end{aligned}
\]
where we used \(M_L=\Theta(L^2)\), (3), and (11). This is (8). ∎

### Corollary 4

\[
\operatorname{sep}(X(g,L))=\Omega(gL).
\tag{13}
\]

#### Proof

Let \(Z\) be a balanced separator. If \(|Z|\ge N/6\), the conclusion is immediate. Otherwise, among the components of \(X-Z\) one can choose a union \(A\) satisfying
\[
N/6\le |A|\le N/2.
\]
All edges leaving \(A\) have their other endpoint in \(Z\). Since \(X\) has bounded maximum degree,
\[
|\partial_X A|\le \Delta|Z|.
\]
Lemma 3 now gives
\[
|Z|\ge c\frac NL=\Omega(gL).
\]
∎

# 4. Separators in every subgraph

The main reason for using two-dimensional blocks rather than ordinary edge subdivisions is the following hereditary estimate.

### Lemma 5

Every subgraph \(F\subseteq X(g,L)\), with \(n=|V(F)|\), has a balanced separator of order
\[
O\left(\frac nL+\sqrt n\right).
\tag{14}
\]

#### Proof

In every block \(Q_v\), and for each of its four ports, choose from Lemma 1 a crosscut minimizing the number of vertices of \(F\) on it. Since there are \(L\) disjoint choices,
\[
|V(F)\cap C_i(k_i)|
 \le \frac{|V(F)\cap V(Q_v)|}{L}.
\]
Taking all four ports and summing over the blocks produces a set \(Z\subseteq V(F)\) with
\[
|Z|\le \frac{4n}{L}.
\tag{15}
\]

Deleting the chosen crosscuts isolates each port collar from the other ports of its block. Consequently, every component of \(F-Z\) is contained either:

- in a planar region of one block, or
- in two port collars joined by the matching belonging to one edge of \(H_g\).

The latter graph is also planar: it embeds in the union of two disks and one rectangular band. Thus every component of \(F-Z\) is planar.

If every such component has at most \(2n/3\) vertices, then \(Z\) is balanced. Otherwise there is a unique component \(K\) with more than \(2n/3\) vertices. A planar separator in \(K\) has order \(O(\sqrt{|K|})=O(\sqrt n)\). Adding it to \(Z\) yields a balanced separator of \(F\), proving (14). ∎

Applying this to \(F=X(g,L)\), and using \(N=\Theta(gL^2)\), gives
\[
\operatorname{sep}(X(g,L))
 =O(gL+\sqrt g\,L)=O(gL).
\]
Together with Corollary 4,
\[
\boxed{\operatorname{sep}(X(g,L))=\Theta(gL).}
\tag{16}
\]

# 5. Shallow minors below the block scale

Although \(X(g,L)\) has genus \(O(g)\), contractions of radius much less than \(L\) cannot simultaneously exploit many handles.

### Lemma 6

There are absolute constants \(\eta,C>0\) such that, whenever
\[
0\le r<\eta L,
\]
every \(r\)-shallow minor \(J\) of \(X(g,L)\) satisfies
\[
|E(J)|\le C|V(J)|.
\tag{17}
\]

#### Proof

Let \(\{B_x:x\in V(J)\}\) be an \(r\)-shallow minor model, and choose a center \(c_x\in B_x\) such that every vertex of \(B_x\) is at distance at most \(r\) from \(c_x\). Let \(\beta(x)\in V(H_g)\) be the block containing \(c_x\).

Distinct ports in a block are at distance at least \(30L\). Choose \(\eta>0\) sufficiently small. Then:

1. a branch set \(B_x\) can meet at most two blocks, and if it meets two, those blocks are adjacent in \(H_g\);
2. if \(xy\in E(J)\), then
   \[
   \operatorname{dist}_X(c_x,c_y)\le2r+1,
   \]
   so \(\beta(x)=\beta(y)\) or \(\beta(x)\beta(y)\in E(H_g)\);
3. if \(\beta(x)=v\) and \(xy\in E(J)\), both \(B_x\) and \(B_y\) are contained in the union of the blocks indexed by the radius-two ball \(N^2_{H_g}[v]\).

Orient the edges of \(J\) arbitrarily. For each \(v\in V(H_g)\), let \(E_v\) be the set of oriented edges whose tail \(x\) satisfies \(\beta(x)=v\), and let \(W_v\) be their endpoint set.

The graph \((W_v,E_v)\) is a minor of the subgraph of \(X(g,L)\) induced by the blocks in \(N^2_{H_g}[v]\). Since \(H_g\) has degree four, this involves only a bounded number of blocks and bands. It therefore embeds in a surface of bounded Euler genus. Lemma 2 gives
\[
|E_v|\le C_0|W_v|.
\tag{18}
\]

A fixed minor vertex \(x\) can belong to \(W_v\) only when
\[
v\in\{\beta(x)\}\cup N_{H_g}(\beta(x)),
\]
so it is counted in at most five of the sets \(W_v\). Consequently,
\[
|E(J)|
 =\sum_v|E_v|
 \le C_0\sum_v|W_v|
 \le5C_0|V(J)|.
\]
∎

Combining Lemma 6 with the global genus estimate (7), we have
\[
\nabla_r(X(g,L))
 \le
 \begin{cases}
 C,&r<\eta L,\\[2mm]
 C\sqrt g,&r\ge\eta L.
 \end{cases}
\tag{19}
\]

# 6. Choice of parameters

Fix \(0<\varepsilon<1/2\), and put
\[
p=\frac1\varepsilon-2>0.
\tag{20}
\]
For every sufficiently large \(L\), choose
\[
g_L=\Theta(L^p)
\tag{21}
\]
and a \(4\)-regular \(\alpha\)-expander \(H_{g_L}\). Let
\[
X_L=X(g_L,L).
\]
Define \(\mathcal C_\varepsilon\) to consist of all subgraphs of all the graphs \(X_L\). This is monotone, hence hereditary.

By (4), (20), and (21),
\[
N_L:=|V(X_L)|
 =\Theta(g_LL^2)
 =\Theta(L^{p+2})
 =\Theta(L^{1/\varepsilon}).
\tag{22}
\]

By (16),
\[
\operatorname{sep}(X_L)
 =\Theta(g_LL)
 =\Theta(L^{p+1})
 =\Theta\left(N_L^{(p+1)/(p+2)}\right)
 =\Theta(N_L^{1-\varepsilon}).
\tag{23}
\]

For an arbitrary \(n\)-vertex subgraph \(F\subseteq X_L\), Lemma 5 gives
\[
\operatorname{sep}(F)
 =O\left(\frac nL+\sqrt n\right).
\]
Since \(n\le N_L=O(L^{1/\varepsilon})\),
\[
n^\varepsilon=O(L),
\]
and hence
\[
\frac nL=O(n^{1-\varepsilon}).
\]
Also \(\sqrt n\le n^{1-\varepsilon}\), because \(\varepsilon<1/2\). Therefore
\[
\operatorname{sep}(F)=O(n^{1-\varepsilon}).
\tag{24}
\]

The orders \(N_L\) have bounded consecutive ratios, and the graphs \(X_L\) themselves supply the matching lower bound (23). Thus
\[
s_{\mathcal C_\varepsilon}(n)=\Theta(n^{1-\varepsilon}).
\tag{25}
\]

If one defines \(s_{\mathcal C}(n)\) using graphs of order exactly \(n\), rather than the monotone envelope over orders at most \(n\), the same conclusion follows by adjoining the required number \(o(N_L)\) of isolated vertices between consecutive values \(N_L\). The expander-isoperimetric argument still forces an \(\Omega(N_L/L)\) separator in the non-isolated component.

Finally, let \(J\) be an \(r\)-shallow minor of some \(X_L\). From (19):

- if \(r<\eta L\), then \(|E(J)|/|V(J)|=O(1)\);
- if \(r\ge\eta L\), then
  \[
  \frac{|E(J)|}{|V(J)|}
   =O(\sqrt{g_L})
   =O(L^{p/2})
   =O(r^{p/2}).
  \]

Therefore
\[
\nabla_{\mathcal C_\varepsilon}(r)
 =O(r^{p/2})
 =O\left(r^{1/(2\varepsilon)-1}\right).
\tag{26}
\]

This proves
\[
b_\varepsilon\le\frac1{2\varepsilon}-1.
\]
Combining it with Dvořák's established reverse inequality gives
\[
\boxed{b_\varepsilon=\frac1{2\varepsilon}-1}.
\]

# Gaps and status

The argument uses only:

- existence of fixed-degree expanders,
- the elementary isoperimetric properties of square grids,
- the planar separator theorem, and
- Euler's formula for graphs embedded in a surface.

No unproved conjecture is invoked. The potentially delicate hereditary and small-radius issues are handled respectively by Lemmas 5 and 6. The proof is nevertheless new and has not been peer reviewed, and I have not independently checked whether the same construction already appears in literature not covered by the catalog review.