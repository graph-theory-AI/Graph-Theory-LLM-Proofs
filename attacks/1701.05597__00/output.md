```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture reduces to balanced complete-bipartite targets, holds in the stronger pervasive sense for bounded-biclique host classes, and natural diffuse Kneser and shift-graph families are not counterexamples.",
  "would_publish": false,
  "caveats": "No unrestricted control radius is obtained; the biclique-rich case, including the reduced complete-bipartite targets, remains untouched."
}
```

# Mathematical writeup

## 1. Definitions and formulation

All graphs below are finite and simple; target multigraphs may have parallel edges. As usual, a subdivision of a multigraph is required to be simple.

For a graph \(G\) and integer \(\rho\geq 0\), write

\[
\chi^\rho(G)=\max_{v\in V(G)}
 \chi\bigl(G[\{x:\operatorname{dist}_G(x,v)\leq \rho\}]\bigr).
\]

A class \(\mathcal C\) is \(\rho\)-controlled if there is a function
\(\phi:\mathbb N\to\mathbb N\) such that

\[
\chi(G)\leq \phi\bigl(\chi^\rho(G)\bigr)
\qquad\text{for every }G\in\mathcal C.
\]

Equivalently, for every \(\tau\) there is \(c\) such that
\(\chi^\rho(G)\leq\tau\) and \(G\in\mathcal C\) imply \(\chi(G)\leq c\).

Under the definition in the source paper, a multigraph \(H\) is widespread if, for every subdivision \(J\) of \(H\) and every clique bound \(\kappa\), there is a radius \(\rho\) such that the class

\[
\mathcal C(J,\kappa)=
\left\{G:
\omega(G)\leq\kappa,\ 
G\text{ has no induced subgraph isomorphic to a subdivision of }J
\right\}
\]

is \(\rho\)-controlled.

Thus the conjecture is equivalent to the assertion that for every \(H,J,\kappa\) there is \(\rho\) such that, for every \(\tau\), sufficiently large chromatic number together with

\[
\omega(G)\leq\kappa,\qquad \chi^\rho(G)\leq\tau
\]

forces an induced subdivision of \(J\).

I do not prove or disprove this assertion.

---

## 2. Downward closure under topological containment

The first reduction substantially narrows the targets that need to be considered.

### Lemma 2.1

Let \(A,B\) be multigraphs. Suppose some subdivision of \(B\) contains a subdivision of \(A\) as a subgraph. If \(B\) is widespread, then \(A\) is widespread.

### Proof

Fix a subdivision \(J_A\) of \(A\) and a clique bound \(\kappa\).

Choose a subdivision \(S\) of \(B\) containing a subdivision \(Q\) of \(A\). Refine the edges of \(Q\), if necessary, so that \(Q\) is also a subdivision of \(J_A\). For every edge of \(S\) not belonging to \(Q\), subdivide that edge at least once. Call the resulting subdivision of \(B\) by \(J_B\).

The construction has the following property:

> Every induced subdivision of \(J_B\) contains, as an induced subgraph, a subdivision of \(J_A\).

Indeed, in a subdivision of \(J_B\), retain precisely the expanded paths corresponding to \(Q\). Every omitted edge of the original \(S\) acquired an internal vertex outside \(Q\); hence an omitted edge cannot produce an unwanted adjacency between two retained vertices. Since the whole \(J_B\)-model is induced, the retained \(J_A\)-model is induced as well.

Consequently,

\[
\mathcal C(J_A,\kappa)\subseteq \mathcal C(J_B,\kappa).
\]

Since \(B\) is widespread, the class on the right is \(\rho\)-controlled for some \(\rho\), and the same control function applies to its subclass on the left. As \(J_A\) and \(\kappa\) were arbitrary, \(A\) is widespread. \(\square\)

### Corollary 2.2: reduction to balanced bicliques

Conjecture 1.8 is equivalent to the assertion that \(K_{n,n}\) is widespread for every \(n\).

### Proof

Only the reverse implication needs proof. Let \(H\) be a finite loopless multigraph. Subdivide every edge of \(H\) once, using a different new vertex for each edge occurrence. The resulting incidence graph is simple and bipartite, with bipartition

\[
V(H)\quad\text{and}\quad E(H).
\]

It is a subgraph of \(K_{N,N}\) for sufficiently large \(N\). Thus \(H\) is topologically contained in \(K_{N,N}\), and Lemma 2.1 applies.

If loops are admitted, replace each loop by a distinct even cycle through its incident vertex; the same bipartite embedding works. \(\square\)

The same proof gives a reduction to complete graphs \(K_N\), but the balanced-biclique formulation is sharper: a counterexample, if one exists, can be chosen among simple bipartite regular multigraph targets of diameter two. The first case not covered by the familiar \(K_{2,n}\)-type “banana” configurations is \(K_{3,3}\).

---

## 3. Bounded-biclique host classes satisfy a stronger conclusion

I use the following established theorem of Kühn and Osthus:

> **Kühn–Osthus theorem.**  
> For every finite simple graph \(F\) and integer \(s\geq2\), there is
> \(d=d(F,s)\) such that every graph of average degree at least \(d\)
> contains either \(K_{s,s}\) as a subgraph or an induced subdivision of
> \(F\).

This is the theorem from D. Kühn and D. Osthus, *Induced subdivisions in \(K_{s,s}\)-free graphs of large average degree*, Combinatorica 24 (2004), 287–304.

### Proposition 3.1

For every finite graph \(F\) and integer \(s\), the class of graphs containing neither \(K_{s,s}\) as a subgraph nor an induced subdivision of \(F\) has bounded chromatic number.

### Proof

Let \(d=d(F,s)\) be supplied by the theorem. If \(G\) has neither configuration, then every induced subgraph \(G[X]\) also has neither configuration, and therefore has average degree less than \(d\). Thus every nonempty induced subgraph has a vertex of degree at most \(\lceil d\rceil-1\). Hence \(G\) is \((\lceil d\rceil-1)\)-degenerate and

\[
\chi(G)\leq \lceil d\rceil.
\qquad\square
\]

Therefore every multigraph is not merely widespread but pervasive in any host ideal with bounded biclique number.

A version involving induced bicliques is also useful.

### Corollary 3.2

For every graph \(F\) and integers \(\kappa,b\), there is \(c=c(F,\kappa,b)\) such that every graph \(G\) with

\[
\omega(G)\leq\kappa,\qquad \chi(G)>c
\]

contains either an induced subdivision of \(F\) or an induced \(K_{b,b}\).

### Proof

Let

\[
S=R(\kappa+1,b),
\]

where \(R\) is the ordinary Ramsey number. Apply Proposition 3.1 with \(s=S\). If the conclusion gives a \(K_{S,S}\) subgraph with sides \(A,B\), then \(G[A]\) and \(G[B]\) have clique number at most \(\kappa\), so each contains an independent set of size \(b\). The two independent sets are complete to one another, and hence induce \(K_{b,b}\). \(\square\)

### Consequences

1. For every fixed target subdivision \(J\), any \(J\)-free bounded-clique family of unbounded chromatic number must contain induced \(K_{b,b}\)'s of arbitrarily large order.

2. No high-girth construction can disprove the conjecture. In particular, graphs of girth at least five contain no \(K_{2,2}\) subgraph, so for every fixed \(J\),

   \[
   \sup\{\chi(G):
   \operatorname{girth}(G)\geq5,\ 
   G\text{ has no induced subdivision of }J\}<\infty.
   \]

3. The remaining difficulty is genuinely biclique-rich. This is not controlled by local chromatic number alone: \(K_{b,b}\) has chromatic number two, independently of \(b\).

---

## 4. A natural diffuse candidate family: Kneser graphs

A tempting source of counterexamples is a sequence with bounded clique number, unbounded chromatic number, and uniformly bipartite bounded-radius balls. Near-bipartite Kneser graphs have precisely these properties. Nevertheless, they contain induced subdivisions of every fixed graph.

Let \(KG(n,k)\) be the graph whose vertices are the \(k\)-subsets of an \(n\)-element set, with adjacency defined by disjointness.

### Lemma 4.1: universal induced one-subdivisions

Let \(F\) be a simple graph on \(q\geq3\) vertices. If

\[
n=2k+t,\qquad t\geq1,\qquad k>(q-2)t,
\]

then \(KG(n,k)\) contains an induced subgraph isomorphic to the one-subdivision of \(F\).

### Proof

Partition the \(n\)-element ground set into disjoint sets

\[
C,\ X_1,\ldots,X_q,\ R
\]

with

\[
|C|=k-t,\qquad |X_i|=t,\qquad
|R|=k-(q-2)t.
\]

The assumed strict inequality makes \(C\) and \(R\) nonempty. The total size is

\[
(k-t)+qt+\bigl(k-(q-2)t\bigr)=2k+t=n.
\]

For each \(i\in V(F)\), define the branch set

\[
A_i=C\cup X_i.
\]

For each edge \(ij\in E(F)\), define

\[
B_{ij}=R\cup\bigcup_{\ell\notin\{i,j\}}X_\ell.
\]

All these sets have size \(k\). Moreover:

- \(A_i\cap A_j\supseteq C\), so no two branch vertices are adjacent;
- \(A_i\cap B_{ij}=A_j\cap B_{ij}=\varnothing\);
- if \(h\notin\{i,j\}\), then \(A_h\cap B_{ij}\supseteq X_h\);
- any two sets \(B_{ij},B_{pq}\) meet in \(R\).

Thus in the induced disjointness graph on the selected vertices, \(B_{ij}\) is adjacent precisely to \(A_i\) and \(A_j\), and there are no other edges. This is exactly the one-subdivision of \(F\). \(\square\)

### Lemma 4.2: the complementary parameter range has bounded diameter

If \(n=2k+t\), \(t>0\), and

\[
k\leq(q-2)t,
\]

then

\[
\operatorname{diam}(KG(n,k))\leq 2(q-2).
\]

### Proof

Let \(A,B\) be arbitrary \(k\)-sets. Transform \(A\) into \(B\) in

\[
m=\left\lceil\frac{|A\setminus B|}{t}\right\rceil
\leq \left\lceil\frac{k}{t}\right\rceil
\leq q-2
\]

steps, replacing at most \(t\) elements at each step. This gives \(k\)-sets

\[
A=A_0,A_1,\ldots,A_m=B
\]

such that \(|A_{i-1}\cup A_i|\leq k+t\). The complement of this union has size at least \(k\), so there is a \(k\)-set \(D_i\) disjoint from both. Therefore

\[
A_{i-1}-D_i-A_i
\]

is a two-edge walk in the Kneser graph. Concatenating these walks gives distance at most \(2m\leq2(q-2)\). \(\square\)

### Proposition 4.3

For every fixed graph \(F\), the family of full Kneser graphs satisfies the widespread conclusion for \(F\), with an explicit radius depending only on \(|V(F)|\).

More precisely, after adjoining isolated vertices to assume \(q=|V(F)|\geq3\), every \(F\)-subdivision-free Kneser graph \(G\) satisfies

\[
\chi(G)\leq \max\{2,\chi^{\,2(q-2)}(G)\}.
\]

### Proof

Write \(G=KG(n,k)\).

- If \(n<2k\), then \(G\) is edgeless.
- If \(n=2k\), then \(G\) is a matching.
- If \(n=2k+t\) with \(t>0\) and \(k>(q-2)t\), Lemma 4.1 gives an induced subdivision of \(F\), contrary to the hypothesis.
- Otherwise, Lemma 4.2 says every radius-\(2(q-2)\) ball is the entire connected graph, so its chromatic number equals \(\chi(G)\).

This proves the claimed inequality. \(\square\)

### Why this rules out a particularly strong candidate

Set

\[
G_m=KG(2m^3+m,m^3).
\]

Then:

- \(\omega(G_m)=2\);
- by the Kneser theorem, \(\chi(G_m)=m+2\);
- for every fixed \(r\), all radius-\(r\) balls are bipartite once \(m\) is sufficiently large.

For the last assertion, write \(k=m^3,t=m\). If

\[
A_0A_1\cdots A_{2\ell}A_0
\]

is an odd cycle, then \(A_{2i}\) and \(A_{2i+2}\) are both contained in the \((k+t)\)-element complement of \(A_{2i+1}\), and hence

\[
|A_{2i}\setminus A_{2i+2}|\leq t.
\]

Since \(A_{2\ell}\) is disjoint from \(A_0\),

\[
k=|A_0\setminus A_{2\ell}|\leq \ell t.
\]

Thus the odd girth is at least \(2\lceil k/t\rceil+1\). A nonbipartite radius-\(r\) ball would contain an odd cycle of length at most \(2r+1\), so fixed-radius balls are eventually bipartite.

This sequence therefore has exactly the local diffuseness required for a strong counterexample. Nevertheless, for every fixed target subdivision \(J\), Lemma 4.1 applies for all sufficiently large \(m\), and \(G_m\) contains an induced one-subdivision of \(J\). Hence it cannot witness failure of widespreadness.

---

## 5. Shift graphs also contain all fixed one-subdivisions

Let \(\operatorname{Sh}(N)\) have vertices \((a,b)\), \(1\leq a<b\leq N\), with two vertices adjacent when the second coordinate of one equals the first coordinate of the other.

### Lemma 5.1

If \(F\) has \(q\) vertices and \(N\geq2q\), then \(\operatorname{Sh}(N)\) contains an induced one-subdivision of \(F\).

### Proof

Choose labels

\[
a_1<b_1<a_2<b_2<\cdots<a_q<b_q.
\]

Represent vertex \(i\) of \(F\) by

\[
v_i=(a_i,b_i).
\]

For every edge \(ij\), with \(i<j\), use

\[
w_{ij}=(b_i,a_j)
\]

as its subdivision vertex. Then \(w_{ij}\) is adjacent to \(v_i\) and \(v_j\). Because all \(a_i,b_i\) are distinct, it has no other selected neighbors; no two \(v_i\)'s are adjacent, and no two \(w_{ij}\)'s are adjacent. Thus the selected graph is exactly the one-subdivision of \(F\). \(\square\)

Consequently the usual full shift-graph sequence, despite being triangle-free with unbounded chromatic number, also cannot be a counterexample.

---

## 6. Exact shape required of a counterexample

By Corollary 2.2, a counterexample can be sought with target \(K_{N,N}\). More precisely, failure would supply a subdivision \(J\) of some \(K_{N,N}\) and a clique bound \(\kappa\) such that for every radius \(\rho\), the class \(\mathcal C(J,\kappa)\) is not \(\rho\)-controlled.

For a fixed \(\rho\), failure of control is equivalent to the existence of an integer \(\tau_\rho\) and graphs \(G_{\rho,m}\) satisfying

\[
\begin{aligned}
&\omega(G_{\rho,m})\leq\kappa,\\
&G_{\rho,m}\text{ has no induced subdivision of }J,\\
&\chi^\rho(G_{\rho,m})\leq\tau_\rho,\\
&\chi(G_{\rho,m})\longrightarrow\infty.
\end{aligned}
\]

Corollary 3.2 then forces, for every fixed \(b\), induced \(K_{b,b}\)'s in all sufficiently chromatic members of each such sequence.

Thus any counterexample must simultaneously be:

1. locally chromatically bounded at every prescribed radius;
2. globally of unbounded chromatic number;
3. rich in induced bicliques of unbounded order;
4. free of a fixed induced subdivision of a subdivision of \(K_{N,N}\).

The bounded-biclique theorem excludes sparse/high-girth constructions, while the explicit Kneser and shift constructions show that two standard biclique-rich diffuse families contain all fixed target subdivisions. I do not have an argument covering arbitrary biclique-rich hereditary classes, and that is the unresolved gap.