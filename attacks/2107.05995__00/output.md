```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but a sharp multi-guess theorem for forests yields explicit bounds for bounded feedback-vertex number, while all one-subdivisions have hat guessing number at most 4.",
  "would_publish": false,
  "caveats": "The bounds use parameters not controlled by degeneracy, so arbitrary 2-degenerate graphs remain untreated; no claim of literature novelty is made."
}
```

# 1. Statement and notation

For a palette \(Q\) of \(q\) colors, a strategy on a graph \(G\) consists of functions
\[
g_v:Q^{N_G(v)}\longrightarrow Q,\qquad v\in V(G).
\]
A coloring \(x\in Q^{V(G)}\) is losing for the players if
\[
x_v\ne g_v(x|_{N_G(v)})\qquad\text{for every }v\in V(G).
\]
Thus \(\operatorname{HG}(G)<q\) precisely when every \(q\)-color strategy has a losing coloring.

I do not prove or disprove the proposed degeneracy bound. I prove:

1. the conjecture for \(d=1\), with the exact value for forests;
2. a sharp auxiliary theorem for the multiple-guess game on forests;
3. an explicit bound in terms of feedback-vertex number;
4. \(\operatorname{HG}(G)\le 4\) for every graph obtained by subdividing every edge of an arbitrary graph once;
5. bounds for graphs obtained in one or boundedly many independent low-degree extension rounds.

These results do not cover arbitrary \(2\)-degenerate graphs.

# 2. A sharp multiple-guess theorem for forests

It is useful to allow every player up to \(s\) guesses. Thus a strategy is now
\[
\Gamma_v:Q^{N(v)}\longrightarrow \binom{Q}{\le s},
\]
and the players win if some \(v\) has \(x_v\in\Gamma_v(x|_{N(v)})\).

## Theorem 2.1

Let \(s\ge1\).

1. On every forest, every \(s\)-guess strategy with
   \[
   q>s(s+1)
   \]
   has a losing coloring.

2. The bound is sharp uniformly over forests: for every \(s\), some finite star has a winning \(s\)-guess strategy with \(q=s(s+1)\).

### Proof of the upper bound

Root each component of the forest. For a nonroot vertex \(v\), with parent \(p(v)\), and a prescribed parent color \(a\in Q\), define \(S_v(a)\subseteq Q\) as follows:

\(b\in S_v(a)\) if there is a coloring of the entire descendant subtree rooted at \(v\), with \(x_v=b\), under which every vertex in that subtree guesses incorrectly, assuming \(x_{p(v)}=a\).

We prove inductively that
\[
|Q\setminus S_v(a)|\le s                                           \tag{2.1}
\]
for every \(v\) and \(a\).

If \(v\) is a leaf, then
\[
S_v(a)=Q\setminus\Gamma_v(a),
\]
so (2.1) follows immediately.

Now let \(v\) have children \(w_1,\dots,w_m\), and assume (2.1) for all children. Fix \(a\in Q\). If \(b\notin S_v(a)\), then for every tuple
\[
(c_1,\dots,c_m)\in \prod_{j=1}^m S_{w_j}(b)
\]
we must have
\[
b\in \Gamma_v(a,c_1,\dots,c_m),                                   \tag{2.2}
\]
since otherwise the losing colorings in the child subtrees could be combined with \(x_v=b\).

Suppose there were \(s+1\) distinct colors \(b_1,\dots,b_{s+1}\notin S_v(a)\). For each child \(w_j\),
\[
\left|\bigcap_{\ell=1}^{s+1}S_{w_j}(b_\ell)\right|
 \ge q-\sum_{\ell=1}^{s+1}|Q\setminus S_{w_j}(b_\ell)|
 \ge q-s(s+1)>0.
\]
Choose
\[
c_j\in\bigcap_{\ell=1}^{s+1}S_{w_j}(b_\ell)
\]
for every child. Applying (2.2) to this same tuple gives
\[
\{b_1,\dots,b_{s+1}\}\subseteq \Gamma_v(a,c_1,\dots,c_m),
\]
contrary to \(|\Gamma_v|\le s\). This proves (2.1).

The same argument at a root, with no parent color, shows that at most \(s\) root colors are infeasible. Since \(q>s\), a feasible root color exists. Choosing the corresponding subtree colorings gives a losing coloring of each component, and hence of the forest. ∎

### Sharpness

Set \(q=s(s+1)\), and let \(Q\) be the palette. Construct a star with center \(z\), having one leaf \(\ell_T\) for every \((s+1)\)-element set \(T\subseteq Q\).

For every such \(T\), choose a partition
\[
Q=\mathop{\dot\bigcup}_{b\in T}P_{T,b},
\qquad |P_{T,b}|=s.
\]
If the center has color \(b\in T\), let the leaf \(\ell_T\) guess all colors in \(P_{T,b}\). For center colors outside \(T\), define an arbitrary \(s\)-element guess set.

Given the vector \(y=(y_T)\) of leaf colors, define
\[
C(y)=\left\{b\in Q:
 y_T\notin \Gamma_{\ell_T}(b)\text{ for every }T\right\}.
\]
This is the set of center colors for which every leaf would be wrong. I claim that
\[
|C(y)|\le s.
\]
Otherwise, choose \(T\subseteq C(y)\) with \(|T|=s+1\). Then
\[
y_T\notin P_{T,b}\qquad\text{for every }b\in T,
\]
which is impossible because the sets \(P_{T,b}\), \(b\in T\), partition \(Q\).

The center guesses every color in \(C(y)\), padding its list arbitrarily if necessary. If some leaf is correct, the players win; if all leaves are wrong, the actual center color belongs to \(C(y)\), so the center is correct. ∎

For \(s=1\), Theorem 2.1 gives the exact standard-game bound for forests.

## Corollary 2.2

If \(F\) is a forest, then
\[
\operatorname{HG}(F)=
\begin{cases}
1,&E(F)=\varnothing,\\
2,&E(F)\ne\varnothing.
\end{cases}
\]

Indeed, Theorem 2.1 with \(s=1\) excludes every \(q\ge3\). If \(F\) has an edge \(uv\), the two endpoints win with two colors by letting \(u\) guess \(x_v\) and \(v\) guess \(1-x_u\).

Thus the degeneracy conjecture holds exactly for \(d=1\), with \(f(1)=2\).

# 3. A bound using feedback-vertex number

The multiple-guess theorem gives a useful modulator result.

For \(k\ge1\), define
\[
a(k)=\min\left\{
  \prod_{i=1}^k r_i:
  r_i\ge2,\quad
  \sum_{i=1}^k\frac1{r_i}<1
\right\},
\]
and put \(a(0)=1\). Taking all \(r_i=k+1\) shows
\[
a(k)\le (k+1)^k.                                                    \tag{3.1}
\]

## Theorem 3.1

If \(G\) has a feedback vertex set of size \(k\), then
\[
\operatorname{HG}(G)\le a(k)\bigl(a(k)+1\bigr)
 \le (k+1)^k\bigl((k+1)^k+1\bigr).                                 \tag{3.2}
\]

### Proof

Let \(C=\{c_1,\dots,c_k\}\) be a feedback vertex set, so
\[
F=G-C
\]
is a forest. Put \(s=a(k)\), and choose integers \(r_1,\dots,r_k\) witnessing the definition of \(a(k)\).

Consider an arbitrary strategy with a palette \(Q\) satisfying
\[
q>s(s+1).                                                          \tag{3.3}
\]
For each \(i\), choose a set \(R_i\subseteq Q\) with \(|R_i|=r_i\), and put
\[
\mathcal X=\prod_{i=1}^kR_i.
\]
Thus \(|\mathcal X|=s\).

For every \(v\in V(F)\) and every coloring \(z\) of its neighbors inside \(F\), define the set of possible guesses
\[
\Gamma_v(z)=
 \left\{
 g_v\bigl(z,x|_{N(v)\cap C}\bigr):x\in\mathcal X
 \right\}.
\]
This has size at most \(s\). By Theorem 2.1 and (3.3), there is a coloring
\[
y\in Q^{V(F)}
\]
such that
\[
y_v\notin\Gamma_v(y|_{N_F(v)})
\qquad\text{for every }v\in V(F).                                  \tag{3.4}
\]
Consequently, every vertex of \(F\) is wrong for every core coloring \(x\in\mathcal X\).

Fix this \(y\). It remains to choose \(x\in\mathcal X\) making every vertex of \(C\) wrong. For \(i=1,\dots,k\), let
\[
A_i=\left\{
x\in\mathcal X:
x_{c_i}=g_{c_i}\bigl(x|_{N(c_i)\cap C},y|_{N(c_i)\cap F}\bigr)
\right\}.
\]
After all coordinates other than \(c_i\) are fixed, at most one value of \(x_{c_i}\) can lie in \(A_i\). Hence
\[
|A_i|\le \frac{s}{r_i}.
\]
It follows that
\[
\left|\bigcup_{i=1}^kA_i\right|
 \le s\sum_{i=1}^k\frac1{r_i}
 <s=|\mathcal X|.
\]
Choose \(x\in\mathcal X\setminus\bigcup_iA_i\). All vertices of \(C\) are then wrong, and (3.4) says that all vertices of \(F\) are wrong. Hence every \(q>s(s+1)\) strategy loses. ∎

For \(k=1\), \(a(1)=2\), giving the following concrete \(2\)-degenerate special case.

## Corollary 3.2

Every graph that becomes a forest after deleting one vertex has
\[
\operatorname{HG}(G)\le6.
\]

More generally, the same bound applies componentwise. Since the hat guessing number of a disjoint union is the maximum of the component hat guessing numbers, every pseudoforest satisfies
\[
\operatorname{HG}(G)\le6.
\]

Indeed, if no component has a winning \(q\)-strategy, choose a losing coloring independently in each component and combine them.

# 4. Independent low-degree extensions

A second useful reduction handles one round of adding independent low-degree vertices.

## Theorem 4.1

Let \(W\subseteq V(G)\) be independent, let \(H=G-W\), and suppose every \(w\in W\) has at most \(k\) neighbors in \(H\), where \(k\ge1\). If
\[
\operatorname{HG}(H)\le h,
\]
then
\[
\operatorname{HG}(G)\le(h+1)^k.                                   \tag{4.1}
\]

### Proof

Put \(r=h+1\), and suppose
\[
q>r^k.
\]
Choose \(R\subseteq Q\) with \(|R|=r\).

For \(w\in W\), as the coloring of \(H\) ranges over \(R^{V(H)}\), the set of possible guesses of \(w\) has size at most
\[
r^{|N(w)|}\le r^k<q.
\]
Choose \(y_w\in Q\) outside this set. Since \(W\) is independent, these choices can be made separately. They ensure that every vertex in \(W\) is wrong for every coloring of \(H\) using only colors from \(R\).

Now fix \(y\in Q^W\). The strategies at vertices of \(H\), with \(y\) fixed, induce an \(r\)-color strategy on \(H\). If an original guess lies outside \(R\), replace it by an arbitrary element of \(R\); a coloring losing for the modified strategy also loses for the original one. Since \(r=h+1>\operatorname{HG}(H)\), there is a losing \(R\)-coloring of \(H\). Together with \(y\), this loses on all of \(G\). ∎

## Consequences

### One-subdivisions

Let \(S(J)\) be obtained from an arbitrary simple graph \(J\) by subdividing every edge exactly once. The original vertices form an independent set \(H\) with \(\operatorname{HG}(H)\le1\), while the subdivision vertices form an independent set \(W\), each having degree two into \(H\). Hence
\[
\boxed{\operatorname{HG}(S(J))\le4.}
\]
These graphs are \(2\)-degenerate, even when \(J\) is arbitrarily dense and has arbitrarily large treewidth.

### Bipartite graphs with bounded degree on one side

If \(G\) is bipartite with parts \(H,W\), and every vertex of \(W\) has degree at most \(d\), then
\[
\operatorname{HG}(G)\le2^d.
\]

### Bounded vertex cover

If \(G\) has a vertex cover \(C\) of size \(k\), then \(W=V(G)\setminus C\) is independent. Also
\[
\operatorname{HG}(G[C])\le k
\]
by the elementary first-moment bound. Therefore
\[
\operatorname{HG}(G)\le(k+1)^k.
\]

### Boundedly many independent elimination layers

Suppose
\[
V(G)=L_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}L_m,
\]
every \(L_i\) is independent, and every vertex in \(L_i\) has at most \(d\) neighbors in
\[
L_{i+1}\cup\cdots\cup L_m.
\]
Define
\[
b_1=1,\qquad b_{j+1}=(b_j+1)^d.
\]
Repeated application of Theorem 4.1 gives
\[
\operatorname{HG}(G)\le b_m.
\]
Thus the conjectured conclusion holds for bounded independent-elimination depth, though this depth need not be bounded by degeneracy.

## A sharper bound for complete bipartite-type examples

The following diagonal argument rules out \(K_{d,n}\) as a source of an unbounded counterexample.

### Proposition 4.2

If \(G\) is bipartite with parts \(A,B\) and \(|A|=t\), then
\[
\operatorname{HG}(G)\le t+1.
\]

### Proof

Let \(q>t+1\), and choose a set \(D\subseteq Q\) of \(t+1\) colors. For \(c\in D\), let \(x^c\) be the coloring of \(A\) assigning color \(c\) to every vertex of \(A\).

For each \(b\in B\), its guesses over the \(t+1\) colorings \(x^c\) take at most \(t+1<q\) values. Choose \(y_b\) outside those values. Thus every vertex of \(B\) is wrong for every coloring \(x^c\).

After \(y\) is fixed, every \(a\in A\) has a fixed guess \(z_a\), since \(A\) is independent. At most \(t\) colors from \(D\) occur among the \(z_a\). Choose
\[
c\in D\setminus\{z_a:a\in A\}.
\]
Then the coloring \(x^c\cup y\) makes every vertex wrong. ∎

In particular,
\[
\operatorname{HG}(K_{d,n})\le d+1
\]
uniformly in \(n\).

# 5. Why this does not prove the degeneracy conjecture

There is a natural degeneracy decomposition.

## Lemma 5.1

Every \(d\)-degenerate graph \(G\), \(d\ge1\), has a partition
\[
V(G)=A\mathbin{\dot\cup}B
\]
such that \(A\) is independent and \(G[B]\) is \((d-1)\)-degenerate.

### Proof

Choose an ordering \(v_1,\dots,v_n\) in which each \(v_i\) has at most \(d\) neighbors of larger index. Process vertices from \(v_n\) down to \(v_1\). Put \(v_i\) in \(A\) if it has no already processed neighbor in \(A\), and put it in \(B\) otherwise.

Then \(A\) is independent. If \(v_i\in B\), it has at least one later neighbor in \(A\), so among its at most \(d\) later neighbors, at most \(d-1\) lie in \(B\). The same ordering witnesses that \(G[B]\) is \((d-1)\)-degenerate. ∎

If the degrees from \(A\) into \(B\) were bounded by a function of \(d\), Theorem 4.1 would suggest an induction on \(d\). They are not. This obstruction occurs already for trees: take two adjacent high-degree centers and attach many leaves to each. In either bipartition class, one of the two high-degree centers occurs, so no choice of the independent side has bounded degree.

The sharp forest argument succeeds despite such high degrees because it uses an intersection property of feasible color sets, not uniform control over all possible guesses. I do not have an analogue of that intersection argument for the \((d-1)\)-degenerate remainder in Lemma 5.1.

Consequently:

- \(d=1\) is completely settled: \(f(1)=2\);
- pseudoforests have \(\operatorname{HG}\le6\);
- all one-subdivisions have \(\operatorname{HG}\le4\);
- bounded feedback-vertex number, bounded vertex cover, and bounded independent-elimination depth give explicit bounds;
- no argument above bounds all \(2\)-degenerate graphs, so the original conjecture remains open.