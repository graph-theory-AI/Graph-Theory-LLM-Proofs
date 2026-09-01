```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved for t at most 3 and for several unbounded-treewidth families, and it admits exact finite-minor and separator-density reductions.",
  "would_publish": false,
  "caveats": "The unrestricted case t at least 4 remains open; several corollaries likely overlap known consequences of the source paper."
}
```

## 1. Definitions and summary

All graphs are finite and simple. A nonempty set \(S\subseteq V(G)\) is a \(k\)-island if every vertex of \(S\) has at most \(k\) neighbors in \(V(G)\setminus S\). For a hereditary class \(\mathcal C\), \(\operatorname{col}^{\star}(\mathcal C)\le t\) means that there is a constant \(C\) such that every nonempty graph in \(\mathcal C\) contains a \((t-1)\)-island with at most \(C\) vertices.

I establish the following partial results.

1. The conjecture is equivalent to a finite-graph assertion about
   \[
   \operatorname{Excl}\bigl(K_{t,m},\,I_{t-1}+P_m\bigr).
   \]
2. The two obstruction families have exact minor-theoretic descriptions:
   - minors of some \(K_{t,m}\) are exactly the graphs with vertex-cover number at most \(t\);
   - minors of some \(I_r+P_m\) are exactly the graphs that become a linear forest after deleting at most \(r\) vertices.
3. Consequently, the right side of the conjecture can be computed directly from any finite excluded-minor description.
4. The conjecture holds for all \(t\le 3\).
5. If a proper minor-closed class has asymptotic connected edge density strictly less than \(t\), then \(\operatorname{col}^{\star}\le t\).
6. Consequences include:
   - \(\operatorname{col}^{\star}=4\) for graphs embeddable in any fixed surface;
   - \(\operatorname{col}^{\star}=a+4\) for the class of graphs made embeddable in a fixed surface by deleting at most \(a\) vertices;
   - \(\operatorname{col}^{\star}(\operatorname{Excl}(K_h))=h-1\) for \(2\le h\le7\);
   - the conjecture holds for every minor-closed subclass of the \(K_5\)-minor-free graphs.

The general \(t\ge4\) case is not settled.

---

## 2. The elementary obstruction argument

Write
\[
J_{t,m}:=I_{t-1}+P_m.
\]

### Lemma 2.1
Every nonempty \((t-1)\)-island in either \(K_{t,m}\) or \(J_{t,m}\) has at least \(m-t+1\) vertices.

#### Proof for \(K_{t,m}\)

Let its bipartition be \(A\cup B\), with \(|A|=t\) and \(|B|=m\). If an island \(S\) is disjoint from \(A\), then every \(b\in S\) has all \(t\) vertices of \(A\) outside \(S\), impossible.

Thus \(S\cap A\ne\varnothing\). For \(a\in S\cap A\), all vertices of \(B\setminus S\) are external neighbors, so
\[
|B\setminus S|\le t-1.
\]
Hence \(|S|\ge m-t+2\).

#### Proof for \(J_{t,m}\)

Let \(A\) be the independent set of \(t-1\) hubs and \(P\) the path. If \(S\cap A=\varnothing\), then any path edge crossing from \(S\) to \(P\setminus S\) gives its endpoint in \(S\) the \(t-1\) external hub-neighbors plus one external path-neighbor. Therefore no path edge can cross, and, since \(P\) is connected, \(S=V(P)\).

If \(S\cap A\ne\varnothing\), a hub in \(S\) has every vertex of \(P\setminus S\) as an external neighbor. Thus \(|P\setminus S|\le t-1\). In either case, \(|S|\ge m-t+1\). ∎

This proves the necessary direction of the conjecture: if the class contained either family for arbitrarily large \(m\), no uniform island bound could exist.

---

## 3. An exact finite-graph reformulation

### Proposition 3.1
For fixed \(t\), Conjecture 4 is equivalent to the following assertion:

> For every \(m\), there exists \(C=C(t,m)\) such that every nonempty graph containing neither \(K_{t,m}\) nor \(J_{t,m}\) as a minor has a \((t-1)\)-island of order at most \(C\).

#### Proof

If the conjecture holds, apply it to the minor-closed class
\[
\mathcal X_{t,m}:=\operatorname{Excl}(K_{t,m},J_{t,m}).
\]

Conversely, suppose a minor-closed class \(\mathcal G\) omits \(K_{t,m_1}\) and \(J_{t,m_2}\). Let \(m=\max(m_1,m_2)\). Since the versions with smaller path or bipartition side are minors of those with larger parameter, \(\mathcal G\) avoids both \(K_{t,m}\) and \(J_{t,m}\) as minors. The finite assertion then supplies the required uniform island bound. ∎

Thus the unresolved content is a single finite-minor theorem, rather than a quantification over arbitrary classes.

---

## 4. What the two obstruction families measure

Let \(\tau(H)\) denote the vertex-cover number of \(H\). Define
\[
\lambda(H):=\min\{|X|:H-X\text{ is a linear forest}\},
\]
where a linear forest is a disjoint union of paths, including isolated vertices.

### Lemma 4.1
For every graph \(H\) and integer \(t\ge1\),
\[
H\preccurlyeq K_{t,m}\text{ for some }m
\quad\Longleftrightarrow\quad
\tau(H)\le t.
\]

#### Proof

Suppose \(H\) is a minor of \(K_{t,m}\), whose bipartition is \(A\cup B\), \(|A|=t\). In a minor model, let \(X\) consist of vertices of \(H\) whose branch sets meet \(A\). Then \(|X|\le t\). Branch sets corresponding to vertices outside \(X\) lie entirely in the independent set \(B\), so there are no edges between such vertices. Thus \(X\) is a vertex cover.

Conversely, let \(X=\{x_1,\dots,x_s\}\) be a vertex cover of \(H\), where \(s\le t\). Represent \(x_i\) by the \(i\)-th vertex on the \(t\)-side. Represent each vertex of \(H-X\) by a distinct vertex on the other side. For each edge \(x_ix_j\) of \(H[X]\), use one additional vertex on the large side, include it in the branch set for \(x_i\), and retain its edge to \(x_j\). All unwanted edges can be deleted. Thus a sufficiently large \(K_{t,m}\) contains \(H\) as a minor. ∎

An explicit sufficient value is
\[
m\ge |V(H)\setminus X|+|E(H[X])|.
\]

### Lemma 4.2
For every graph \(H\) and integer \(r\ge0\),
\[
H\preccurlyeq I_r+P_m\text{ for some }m
\quad\Longleftrightarrow\quad
\lambda(H)\le r.
\]

#### Proof

Let \(H\) be a minor of \(I_r+P_m\), and let \(X\) consist of vertices whose branch sets meet the \(I_r\)-part. Then \(|X|\le r\). Every remaining branch set is an interval of the host path. Their adjacency graph is therefore a subgraph of a path after contractions and deletions, hence a linear forest. Thus \(H-X\) is a linear forest.

Conversely, suppose \(X=\{x_1,\dots,x_s\}\), \(s\le r\), and \(H-X\) is a linear forest. Use \(s\) of the independent hubs to represent \(X\). Lay the path components of \(H-X\) consecutively along the host path, deleting host-path edges between distinct components. Cross-edges from \(X\) to \(H-X\) are available because of the join. As in Lemma 4.1, each edge of \(H[X]\) can be realized using one additional path vertex included in one endpoint's branch set. ∎

Again,
\[
m\ge |V(H)\setminus X|+|E(H[X])|
\]
is sufficient.

### Corollary 4.3: exact description of the conjectured value

For a proper minor-closed class \(\mathcal G\), define
\[
a(\mathcal G):=\min_{H\notin\mathcal G}\tau(H),
\qquad
b(\mathcal G):=1+\min_{H\notin\mathcal G}\lambda(H),
\]
and
\[
T(\mathcal G):=\max\{a(\mathcal G),b(\mathcal G)\}.
\]

Then the right side of Conjecture 4 holds for \(t\) exactly when
\[
t\ge T(\mathcal G).
\]
Moreover, the elementary necessary direction gives
\[
\operatorname{col}^{\star}(\mathcal G)\ge T(\mathcal G).
\]

Consequently, Conjecture 4 is exactly the equality
\[
\boxed{\operatorname{col}^{\star}(\mathcal G)=T(\mathcal G).}
\]

If
\[
\mathcal G=\operatorname{Excl}(\mathcal F)
\]
for a finite list \(\mathcal F\), then
\[
T(\mathcal G)=
\max\left\{
\min_{F\in\mathcal F}\tau(F),\
1+\min_{F\in\mathcal F}\lambda(F)
\right\}.
\]

For fixed \(t\), the hypothesis can therefore be checked from a supplied excluded-minor list by enumerating:

- subsets of at most \(t\) vertices and testing whether they are vertex covers;
- subsets of at most \(t-1\) vertices and testing whether their deletion leaves an acyclic graph of maximum degree at most two.

This takes polynomial time for fixed \(t\), with a direct \(O(n^t(n+e))\) implementation for each excluded graph.

---

## 5. The conjecture for \(t\le3\)

### Theorem 5.1
Conjecture 4 holds for \(t=1,2,3\).

#### Proof

Suppose the two stated obstructions are excluded.

- For \(t=1\), \(K_{1,m}\) is planar.
- For \(t=2\), \(K_{2,m}\) is planar.
- For \(t=3\), \(I_2+P_m\) is planar: draw the path on a line, one hub above it and the other below it.

A minor-closed class excluding a fixed planar graph has bounded treewidth: every fixed planar graph is a minor of a sufficiently large grid, and the grid-minor theorem then gives a uniform treewidth bound.

The bounded-treewidth case is precisely Theorem 7 of the source paper. Hence the two excluded families imply
\[
\operatorname{col}^{\star}(\mathcal G)\le t
\]
for \(t\le3\). The converse is Lemma 2.1. ∎

Thus the first genuinely unresolved value is \(t=4\).

For completeness, \(t=1\) also has a direct elementary proof. A connected graph excluding both \(K_{1,m}\) and \(P_m\) has a spanning tree of maximum degree less than \(m\) and depth less than \(m\), hence bounded order. Its connected components are therefore uniformly bounded \(0\)-islands.

---

## 6. A separator-density theorem

The following gives a broad sufficient condition.

### Lemma 6.1: bounded-component partition

Suppose every \(n\)-vertex graph in a hereditary class \(\mathcal C\) has a separator of order at most
\[
c n^{1-\varepsilon},
\]
whose removal leaves components of order at most \(\alpha n\), where \(c>0\), \(\varepsilon>0\), and \(\alpha<1\) are fixed.

Then there is \(K=K(c,\varepsilon,\alpha)\) such that, for every integer \(R\ge1\) and every \(G\in\mathcal C\), one can delete a set \(X\) satisfying
\[
|X|\le K|V(G)|R^{-\varepsilon}
\]
so that every component of \(G-X\) has at most \(R\) vertices.

#### Proof

Recursively apply balanced separators to components of order greater than \(R\). Group recursion nodes \(U\) according to
\[
2^jR<|U|\le2^{j+1}R.
\]
Along any root-to-leaf recursion chain, the sizes decrease by a factor at most \(\alpha\), so only a bounded number \(L=L(\alpha)\) of nodes in the same dyadic range can contain any fixed vertex. Therefore
\[
\sum_{U\text{ in range }j}|U|\le L|V(G)|.
\]
Consequently the separators used in this range have total order at most
\[
c\sum_U |U|^{1-\varepsilon}
 \le cL|V(G)|(2^jR)^{-\varepsilon}.
\]
Summing the geometric series over \(j\ge0\) proves the claim. ∎

### Theorem 6.2
Let \(\mathcal C\) be a hereditary class with strongly sublinear separators as above. Suppose there are \(\delta>0\) and \(N\) such that every connected \(G\in\mathcal C\) with \(|V(G)|\ge N\) satisfies
\[
|E(G)|\le (t-\delta)|V(G)|.
\]
Then
\[
\operatorname{col}^{\star}(\mathcal C)\le t.
\]

#### Proof

Choose \(R\) sufficiently large that
\[
tKR^{-\varepsilon}<\delta,
\]
where \(K\) is from Lemma 6.1.

Suppose a connected \(G\in\mathcal C\), of order \(n\ge N\), has no \((t-1)\)-island of order at most \(R\). Delete \(X\) as in Lemma 6.1, and let the components of \(G-X\) be \(Q_1,\dots,Q_s\), each of order at most \(R\).

Fix one \(Q_i\). Starting with \(R_1=V(Q_i)\), repeatedly choose \(v_j\in R_j\) having at least \(t\) neighbors outside \(R_j\), and put
\[
R_{j+1}=R_j\setminus\{v_j\}.
\]
Such a vertex exists because \(R_j\) is not a \((t-1)\)-island and \(|R_j|\le R\).

There are no edges between different components of \(G-X\). Hence each \(v_j\) has at least \(t\) neighbors among
\[
X\cup\{v_1,\dots,v_{j-1}\}.
\]
Order all vertices of \(X\) first, followed by the sequences obtained from the components. Every vertex outside \(X\) then has at least \(t\) earlier neighbors. Counting each edge at its later endpoint gives
\[
|E(G)|\ge t(n-|X|)
   \ge t(1-KR^{-\varepsilon})n
   >(t-\delta)n,
\]
contrary to the assumed edge bound.

Connected graphs of order less than \(N\) are themselves bounded islands. Applying the argument to a connected component gives the conclusion for arbitrary graphs. ∎

Define the asymptotic connected density by
\[
d_{\mathrm{conn}}(\mathcal C):=
\limsup_{\substack{G\in\mathcal C,\ G\text{ connected}\\|V(G)|\to\infty}}
\frac{|E(G)|}{|V(G)|}.
\]

Every proper minor-closed class has strongly sublinear separators. Therefore:

### Corollary 6.3
If \(\mathcal C\) is proper and minor-closed and
\[
d_{\mathrm{conn}}(\mathcal C)<t,
\]
then
\[
\operatorname{col}^{\star}(\mathcal C)\le t.
\]

Combined with Corollary 4.3, this proves Conjecture 4 for every class satisfying
\[
d_{\mathrm{conn}}(\mathcal C)<T(\mathcal C).
\]

---

## 7. Consequences

### 7.1 Fixed surfaces

For a fixed surface \(\Sigma\), graphs embeddable in \(\Sigma\) have strongly sublinear separators and
\[
|E(G)|\le 3|V(G)|+O_\Sigma(1).
\]
Thus Theorem 6.2 with \(t=4\) gives
\[
\operatorname{col}^{\star}(\mathcal G_\Sigma)\le4.
\]

Since every \(I_2+P_m\) is planar and hence belongs to \(\mathcal G_\Sigma\), Lemma 2.1 gives the reverse inequality. Therefore
\[
\boxed{\operatorname{col}^{\star}(\mathcal G_\Sigma)=4.}
\]

It follows that Conjecture 4 holds for every minor-closed subclass of the graphs embeddable in a fixed surface:

- for \(t\le3\), use Theorem 5.1;
- for \(t\ge4\), use \(\operatorname{col}^{\star}\le4\).

### 7.2 Boundedly many apices

Let \(\mathcal A_{a,\Sigma}\) be the class of graphs \(G\) for which some \(A\subseteq V(G)\), \(|A|\le a\), satisfies \(G-A\in\mathcal G_\Sigma\).

More generally, if \(\operatorname{col}^{\star}(\mathcal C)\le s\), then
\[
\operatorname{col}^{\star}(\mathcal A_a(\mathcal C))\le s+a.
\]
Indeed, an \((s-1)\)-island in \(G-A\) becomes an \((s+a-1)\)-island in \(G\).

Hence
\[
\operatorname{col}^{\star}(\mathcal A_{a,\Sigma})\le a+4.
\]
On the other hand,
\[
I_{a+2}+P_m\in\mathcal A_{a,\Sigma}
\]
for every \(m\), because deleting any \(a\) hubs leaves the planar graph \(I_2+P_m\). Therefore
\[
\operatorname{col}^{\star}(\mathcal A_{a,\Sigma})>a+3.
\]
Thus
\[
\boxed{\operatorname{col}^{\star}(\mathcal A_{a,\Sigma})=a+4.}
\]

This verifies the conjectured characterization for these particular, generally unbounded-treewidth, minor-closed classes.

### 7.3 Excluding small complete minors

For \(2\le h\le7\), the standard sharp extremal theorem for clique minors gives
\[
|E(G)|\le (h-2)|V(G)|-\binom{h-1}{2}
\]
for sufficiently large \(K_h\)-minor-free graphs. Hence
\[
d_{\mathrm{conn}}(\operatorname{Excl}(K_h))\le h-2<h-1.
\]
Theorem 6.2 gives
\[
\operatorname{col}^{\star}(\operatorname{Excl}(K_h))\le h-1.
\]

Moreover,
\[
\tau(K_h)=h-1,\qquad \lambda(K_h)=h-2.
\]
Corollary 4.3 supplies the matching lower bound, so
\[
\boxed{\operatorname{col}^{\star}(\operatorname{Excl}(K_h))=h-1
\quad(2\le h\le7).}
\]

In particular,
\[
\operatorname{col}^{\star}(\operatorname{Excl}(K_5))=4.
\]
Consequently, Conjecture 4 holds for every minor-closed subclass of the \(K_5\)-minor-free graphs: the cases \(t\le3\) follow from Theorem 5.1, while \(t\ge4\) follows from the uniform upper bound \(4\).

---

## 8. What a counterexample would have to look like

Fix \(t,m\) and let
\[
\mathcal X=\operatorname{Excl}(K_{t,m},J_{t,m}).
\]
This is a proper minor-closed class, so its graphs have \(O(\sqrt n)\)-size balanced separators.

If the finite assertion of Proposition 3.1 fails, then for every \(C\) there is a connected \(G_C\in\mathcal X\) having no \((t-1)\)-island of order at most \(C\). The proof of Theorem 6.2 then gives
\[
|E(G_C)|
 \ge t\bigl(1-O_{t,m}(C^{-1/2})\bigr)|V(G_C)|.
\]
In addition:

- \(\delta(G_C)\ge t\), since no singleton is an island;
- after deleting \(O(|V(G_C)|/\sqrt C)\) vertices, the remaining vertices admit an ordering in which each has at least \(t\) earlier neighbors;
- the treewidths of such witnesses must tend to infinity, since the bounded-treewidth theorem would otherwise give a uniform island bound.

Thus a counterexample would require an unbounded-treewidth sequence avoiding both prescribed minors and asymptotically attaining at least \(t\) edges per vertex.

---

## 9. Why the density criterion does not finish the conjecture

The two excluded families alone do not imply connected density less than \(t\).

For example, fix \(N>2t\), and let \(\mathcal B_N\) be the minor-closed class of graphs all of whose blocks have at most \(N\) vertices. Chains of copies of \(K_N\), consecutive copies sharing one cutvertex, have
\[
n=q(N-1)+1,\qquad
e=q\binom N2,
\]
and hence
\[
\frac en\longrightarrow \frac N2>t.
\]

Nevertheless, \(\operatorname{col}^{\star}(\mathcal B_N)\le2\): a leaf block minus its unique cutvertex is a \(1\)-island of order at most \(N-1\), while a graph consisting of one block has bounded order.

For sufficiently large \(m\), both \(K_{t,m}\) and \(J_{t,m}\) are 2-connected and have more than \(N\) vertices, so neither belongs to \(\mathcal B_N\). Thus this class satisfies the conjecture's exclusions despite arbitrarily large connected density.

The missing argument must therefore distinguish bounded dense pieces, which produce small islands through low-order sums, from genuinely large highly connected torsos. The bounded-treewidth theorem performs this distinction in that setting. I do not have a complete extension to the unbounded-treewidth case, and in particular I do not settle the unrestricted \(t=4\) case.