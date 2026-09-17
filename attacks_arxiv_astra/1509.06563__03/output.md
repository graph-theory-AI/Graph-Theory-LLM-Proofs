```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every fixed control function φ and ε > 0, controlled graphs of girth at least five satisfy χ(G) ≤ C(φ,ε) max{1,Δ(G)}^ε, so the conjecture holds when maximum degree is polynomially bounded in chromatic number.",
  "would_publish": false,
  "caveats": "The unrestricted question remains unresolved; the auxiliary bound's novelty has not been checked."
}
```

## 1. A partial theorem

All graphs below are finite and simple. For a nonempty graph \(H\), write
\[
\chi^2(H)=\max_{v\in V(H)}
 \chi\bigl(H[N_H^2[v]]\bigr),
\]
where \(N_H^2[v]\) consists of vertices at distance at most two from \(v\), with distances measured **in \(H\)**. A graph is \((2,\varphi)\)-controlled if
\[
\chi(H)\le \varphi(\chi^2(H))
\]
for every nonempty induced subgraph \(H\).

In a triangle-free graph, every four-cycle is induced. Thus the graphs relevant to a counterexample are precisely the controlled graphs of girth at least five.

I prove the following degree-dependent bound.

**Theorem.** Fix a non-decreasing function \(\varphi:\mathbb N\to\mathbb N\). Put
\[
\psi(t)=\max\{t,\varphi(t)\},\qquad
b_0=1,\qquad b_h=\psi(b_{h-1}+1)\quad(h\ge1).
\]
If \(G\) is \((2,\varphi)\)-controlled and has girth at least five, then, for every integer \(h\ge2\),
\[
\boxed{\quad
\chi(G)\le
3b_h\,\max\{1,\Delta(G)\}^{\alpha_h},
\qquad
\alpha_h=\frac{4h+2}{h^2+9h-2}.
\quad} \tag{1}
\]
In particular, for every \(\varepsilon>0\), there exists \(C(\varphi,\varepsilon)\) such that
\[
\chi(G)\le C(\varphi,\varepsilon)
            \max\{1,\Delta(G)\}^{\varepsilon}. \tag{2}
\]

For example, the first two exponents in (1) are \(1/2\) and \(7/17\). The exponents tend to zero.

A consequence directly addressing the question is:

**Corollary.** Fix \(\varphi\), \(A\ge1\), and \(d>0\). There is \(n=n(\varphi,A,d)\) such that every \((2,\varphi)\)-controlled triangle-free graph satisfying
\[
\Delta(G)\le A\chi(G)^d
\]
and \(\chi(G)>n\) has a \(4\)-hole.

The proof uses finite induced configurations forced by control, followed by the Lovász local lemma.

## 2. Iterated distance-two extensions

Call a partition \(\mathcal P\) of \(V(F)\) **admissible** if distinct vertices in the same block are nonadjacent and have no common neighbor in \(F\).

For such a partition, construct \(E(F,\mathcal P)\) as follows:

* retain \(F\);
* add a new vertex \(z\);
* for each block \(A\in\mathcal P\), add a vertex \(p_A\);
* add the edges \(zp_A\), and \(p_Ax\) for every \(x\in A\);
* add no other edges.

Thus \(z\) is a new center, and every old vertex has exactly one new parent.

If \(F\) has girth at least five, so does \(E(F,\mathcal P)\). Indeed:

* a new triangle through a parent would require adjacent old vertices in one block;
* a four-cycle through the center, or through two parents, would require an old vertex to belong to two blocks;
* a four-cycle through exactly one parent, but not the center, would require two vertices of its block to have a common old neighbor.

All these possibilities are excluded.

Define finite families \(\mathcal F_h\) recursively:
\[
\mathcal F_0=\{K_2\},
\]
and let \(\mathcal F_h\) consist, up to isomorphism, of all
\[
E(F,\mathcal P),\qquad
F\in\mathcal F_{h-1},
\]
with \(\mathcal P\) admissible.

### Sizes of the configurations

For \(h\ge1\), every \(F\in\mathcal F_h\) satisfies
\[
m_h\le |V(F)|\le M_h,
\qquad
m_h=\frac{h(h+9)}2,\qquad
M_h=3\cdot2^h-1. \tag{3}
\]

Here is the verification.

The upper bound follows from
\[
|V(E(F,\mathcal P))|\le 2|V(F)|+1.
\]

For the lower bound, every closed neighborhood in \(F\) meets each admissible block at most once. Consequently,
\[
|\mathcal P|\ge \Delta(F)+1. \tag{4}
\]
Also every old vertex gains one neighbor, so maximum degree increases by at least one under an extension.

The family \(\mathcal F_1\) consists only of \(C_5\). Since every pair of vertices of \(C_5\) has distance at most two, \(\mathcal F_2\) also consists of one graph: a \(C_5\), a new center, and five length-two spokes. It has eleven vertices and maximum degree five.

It follows that every member of \(\mathcal F_h\), for \(h\ge2\), has maximum degree at least \(h+3\). Therefore an extension at step \(h\ge3\) adds at least \(h+4\) vertices, by (4). Starting with eleven vertices at step two gives
\[
11+\sum_{j=3}^{h}(j+4)=\frac{h(h+9)}2.
\]
The case \(h=1\) is immediate.

## 3. Control forces these configurations

**Lemma 1.** If \(G\) is \((2,\varphi)\)-controlled, has girth at least five, and
\[
\chi(G)>b_h,
\]
then \(G\) contains an induced member of \(\mathcal F_h\).

**Proof.** We may use the larger control function \(\psi\). The assertion for \(h=0\) just says that a graph of chromatic number greater than one has an edge.

Suppose \(h\ge1\), and inductively assume the assertion for \(h-1\). Since
\[
\chi(G)>\psi(b_{h-1}+1),
\]
control and monotonicity imply
\[
\chi^2(G)>b_{h-1}+1.
\]
Choose \(v\) attaining a ball with chromatic number greater than this quantity, and put
\[
L_i=\{x:\operatorname{dist}_G(v,x)=i\}.
\]

The set \(L_1\) is stable. Coloring \(L_1\) with one new color shows that
\[
\chi\bigl(G[N_G^2[v]]\bigr)
 \le \max\{2,\chi(G[L_2])+1\}.
\]
It follows that
\[
\chi(G[L_2])>b_{h-1}.
\]

The graph \(G[L_2]\) is again controlled. By induction it contains an induced member \(F\) of \(\mathcal F_{h-1}\).

Every vertex of \(L_2\) has a unique neighbor in \(L_1\): two such neighbors would give a four-cycle through \(v\). Partition \(V(F)\) according to these unique parents. This partition is admissible:

* adjacent vertices with the same parent would form a triangle;
* vertices with a common neighbor in \(F\) and the same parent would form a four-cycle.

The subgraph induced by \(V(F)\), its parents, and \(v\) is therefore exactly an admissible extension of \(F\), and belongs to \(\mathcal F_h\). ∎

The hereditary part of control is essential here: the induction is applied to \(G[L_2]\), not merely to \(G\).

## 4. Counting copies using the absence of four-cycles

The next lemma is the principal counting point. Although configurations in \(\mathcal F_h\) have quadratically many vertices in \(h\), their embeddings have only linearly many degree-dependent choices.

Let
\[
D=\max\{1,\Delta(G)\}.
\]

**Lemma 2.** If \(G\) has girth at least five, then, for every vertex \(v\), the number of vertex sets \(U\) containing \(v\) such that
\[
G[U]\in\mathcal F_h
\]
is at most
\[
3^hD^{2h+1}. \tag{5}
\]

**Proof.** Two distinct vertices of \(G\) have at most one common neighbor.

Consequently, once an old copy \(W\) and a proposed new center \(z\) are fixed, there is at most one extension of \(W\) centered at \(z\). For each \(x\in W\), its new parent must be the unique common neighbor of \(x\) and \(z\). Thus the entire new parent set, and hence the entire extension, is forced.

We induct on \(h\). For \(h=0\), the number of edges containing \(v\) is at most \(D\).

For \(h\ge1\), consider an extension description of a copy containing \(v\), with old copy \(W\in\mathcal F_{h-1}\) and new center \(z\). There are three cases.

1. **\(v\in W\).**  
   There are at most \(3^{h-1}D^{2h-1}\) choices for \(W\). The center \(z\) has distance two from \(v\), giving at most \(D^2\) choices.

2. **\(v=z\).**  
   Choose an old vertex \(x\in W\), at distance two from \(v\), in at most \(D^2\) ways. There are then at most \(3^{h-1}D^{2h-1}\) old copies containing \(x\).

3. **\(v\) is a new parent.**  
   Choose the center \(z\in N_G(v)\) and an old vertex \(x\in W\cap N_G(v)\), in at most \(D^2\) ways. Again there are at most \(3^{h-1}D^{2h-1}\) old copies containing \(x\).

In each case, the extension is forced by \(W\) and \(z\). Summing gives (5). Copies with multiple extension descriptions are merely overcounted. ∎

## 5. A local-lemma partition

Fix \(h\ge2\), and abbreviate
\[
m=m_h,\qquad M=M_h,\qquad a=2h+1,
\qquad \alpha=\frac{a}{m-1}.
\]
Notice that this \(\alpha\) is precisely \(\alpha_h\) in (1).

Independently assign each vertex one of
\[
q=\left\lceil 2D^\alpha\right\rceil
\]
auxiliary colors.

For every vertex set inducing a member of \(\mathcal F_h\), let its bad event be that all its vertices receive the same auxiliary color. By (3), each bad event has probability at most
\[
p=q^{-(m-1)}
 \le 2^{-(m-1)}D^{-a}. \tag{6}
\]

Events on disjoint vertex sets are independent. By Lemma 2, a bad event depends on at most
\[
d\le M\,3^hD^a
\]
other bad events. In particular,
\[
d+1
 \le (3^hM+1)D^a
 \le 3\cdot6^hD^a. \tag{7}
\]

For \(h\ge2\),
\[
m-1=\frac{h(h+9)}2-1\ge3h+4.
\]
Combining this with (6) and (7) gives
\[
ep(d+1)
 \le \frac{3e\,6^h}{2^{m-1}}
 \le \frac{3e}{16}\left(\frac34\right)^h
 <1.
\]
The symmetric Lovász local lemma therefore provides an auxiliary coloring with no bad event.

Thus \(V(G)\) is partitioned into \(q\) sets, each inducing an \(\mathcal F_h\)-free graph. Each induced graph remains controlled and has girth at least five. By Lemma 1, each has chromatic number at most \(b_h\). Using disjoint palettes for the parts,
\[
\chi(G)\le qb_h
 \le 3b_hD^\alpha.
\]
This proves (1).

Finally,
\[
\alpha_h=\frac{4h+2}{h^2+9h-2}\le\frac4h.
\]
Choosing \(h\ge\max\{2,\lceil4/\varepsilon\rceil\}\) proves (2), with the explicit choice
\[
C(\varphi,\varepsilon)=3b_h.
\]

## 6. Consequences and the remaining gap

### Polynomial maximum degree

Suppose
\[
\Delta(G)\le A\chi(G)^d,
\qquad A\ge1,\quad d>0.
\]
Choose an integer \(h\ge\max\{2,8d\}\). Then \(\alpha_h\le1/(2d)\), and (1) yields
\[
\chi(G)
 \le 3b_h\bigl(A\chi(G)^d\bigr)^{1/(2d)}
 =3b_hA^{1/(2d)}\chi(G)^{1/2}.
\]
Hence
\[
\boxed{\chi(G)\le9b_h^2A^{1/d}.} \tag{8}
\]
This proves the stated corollary: under a fixed polynomial relation between maximum degree and chromatic number, sufficiently large chromatic number forces a \(4\)-hole.

### What a counterexample family would require

For fixed \(\varphi\), any sequence of controlled girth-at-least-five graphs \(G_i\) with \(\chi(G_i)\to\infty\) would necessarily satisfy
\[
\frac{\Delta(G_i)}{\chi(G_i)^p}\longrightarrow\infty
\qquad\text{for every fixed }p>0.
\]
Indeed, apply (2) with \(\varepsilon=1/(p+1)\).

This conclusion also holds after passing to induced chromatic-critical subgraphs, since control and girth are inherited. Thus the necessary large maximum degree cannot be supplied merely by appending leaves to a high-chromatic core.

### Why this does not settle the question

There is still no chromatic bound independent of maximum degree. Although \(\alpha_h\to0\), the coefficient \(b_h\) involves increasingly many iterations of the control function. One cannot let \(h\) tend to infinity while retaining a fixed coefficient.

The unrestricted conjecture therefore remains open in this argument. The precise progress is the subpower bound (1)–(2), and the resulting exclusion of every counterexample family whose critical members have maximum degree bounded by a fixed polynomial in their chromatic number.