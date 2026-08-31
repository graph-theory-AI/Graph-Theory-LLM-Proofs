```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general characterization remains open, but the hereditary class defined by one forbidden induced graph is completely classified, and the maximum n-vertex ratio is shown to have order sqrt(n log n).",
  "would_publish": false,
  "caveats": "Arbitrary hereditary classes with several or infinitely many forbidden induced graphs are not characterized, and the literature novelty of the auxiliary results has not been verified."
}
```

## 1. Definitions and summary of results

All graphs below are finite and simple. A set \(P\subseteq V(G)\) is **2-independent** if distinct vertices of \(P\) have distance greater than \(2\). Write
\[
\alpha _2(G)=\max\{|P|:P\text{ is 2-independent}\}.
\]
For nonempty graphs, \(\alpha _2(G)\ge 1\).

I prove the following partial characterization.

### Theorem 1: one forbidden induced graph

Let \(H\) be a nonempty graph, and let
\[
\operatorname{Forb}_{\mathrm{ind}}(H)
   =\{G: G\text{ has no induced copy of }H\}.
\]
Then
\[
\sup_{G\in \operatorname{Forb}_{\mathrm{ind}}(H)}
   \frac{\gamma(G)}{\alpha _2(G)}<\infty
\]
if and only if one of the following holds:

1. \(H=sK_1\) is edgeless; or
2. \(H=F+sK_1\), where
   \[
   F\in\{K_2,P_3,P_4\}
   \quad\text{and}\quad s\ge 0.
   \]

Equivalently, \(H\) has at most one component containing an edge, and that component, if present, is an induced subgraph of \(P_4\).

In the positive cases one may take
\[
\frac{\gamma(G)}{\alpha _2(G)}
   \le
   \begin{cases}
   s-1,&H=sK_1,\\[2mm]
   \max\{2,\,|V(F)|+s-1\},&H=F+sK_1.
   \end{cases}
\]

Consequently:

- the class of induced-\(P_t\)-free graphs has bounded ratio exactly for \(t\le 4\);
- the class of induced-\(K_{1,t}\)-free graphs has bounded ratio exactly for \(t\le 2\);
- split graphs, chordal graphs, \(P_5\)-free graphs, line graphs, claw-free graphs, and bipartite graphs all have unbounded ratio.

I also prove the following finite-order estimate.

### Theorem 2: extremal order

Let
\[
R(n)=\max_{\substack{|V(G)|=n\\G\ne\varnothing}}
       \frac{\gamma(G)}{\alpha _2(G)}.
\]
There are absolute constants \(c,C>0\) such that
\[
c\sqrt{n\log n}\le R(n)\le C\sqrt{n\log n}.
\]
More explicitly,
\[
R(n)\le 2\sqrt{n(1+\log n)}+2,
\]
and the lower bound can be attained by graphs of diameter two, for which \(\alpha _2=1\).

The general problem for arbitrary hereditary classes remains open.

---

## 2. A split-graph encoding of arbitrary set systems

Let \(\mathcal H=(X,\mathcal E)\) be a finite hypergraph in which every edge is nonempty and \(\bigcup\mathcal E=X\). Form a split graph \(S(\mathcal H)\) as follows:

- \(X\) is made into a clique;
- for every \(E\in\mathcal E\), add an independent vertex \(v_E\);
- join \(v_E\) precisely to the vertices of \(E\).

Let \(\nu(\mathcal H)\) be the matching number of the hypergraph, and define
\[
\tau^\dagger(\mathcal H)
 =\min_{A\subseteq X}
   \left(
      |A|+
      |\{E\in\mathcal E:E\cap A=\varnothing\}|
   \right).
\]

### Lemma 2.1
For every such \(\mathcal H\),
\[
\alpha _2(S(\mathcal H))=\nu(\mathcal H)
\quad\text{and}\quad
\gamma(S(\mathcal H))=\tau^\dagger(\mathcal H).
\]

#### Proof

Two independent-side vertices \(v_E,v_F\) have distance two exactly when \(E\cap F\ne\varnothing\). If \(E\cap F=\varnothing\), they have distance three, using the fact that \(X\) is a clique. Thus 2-independent sets contained in the independent side correspond precisely to hypergraph matchings.

Every clique vertex is at distance at most two from every vertex of the graph, so a 2-independent set containing a clique vertex has size one. Since \(\mathcal E\ne\varnothing\), \(\nu(\mathcal H)\ge1\), proving
\[
\alpha _2(S(\mathcal H))=\nu(\mathcal H).
\]

Now let \(D\) be a dominating set, and put \(A=D\cap X\). If \(E\cap A=\varnothing\), then \(v_E\) has no neighbor in \(A\), and no other independent-side vertex can dominate it. Hence \(v_E\in D\). Therefore
\[
|D|\ge |A|+|\{E:E\cap A=\varnothing\}|.
\]

Conversely, for any \(A\subseteq X\), take
\[
D_A=A\cup\{v_E:E\cap A=\varnothing\}.
\]
If \(A\ne\varnothing\), the clique \(X\) is dominated by \(A\), while every \(v_E\) either meets \(A\) or belongs to \(D_A\). If \(A=\varnothing\), then all independent-side vertices are selected, and they dominate \(X\) because the hypergraph covers \(X\). Thus \(D_A\) is dominating, proving the second equality. \(\square\)

This shows that already inside split graphs the problem contains arbitrary hypergraph matching-versus-penalized-transversal phenomena. Taking induced subgraphs corresponds essentially to taking subfamilies and traces of the set system.

---

## 3. Three obstruction families

### 3.1 Diameter-two split graphs

Let \(q\) be a prime power and consider the projective plane \(PG(2,q)\). It has
\[
N=q^2+q+1
\]
points and the same number of lines. Every line contains \(q+1\) points, every point belongs to \(q+1\) lines, and any two lines meet in exactly one point.

Apply the split construction above with points as \(X\) and projective lines as the hyperedges. Call the resulting graph \(S_q\).

Because every two projective lines meet, the corresponding hypergraph has matching number one. Hence
\[
\alpha _2(S_q)=1.
\]
Indeed, \(S_q\) has diameter two.

We next compute its domination number. For a set \(A\) of \(t\) points, let \(u(A)\) denote the number of projective lines avoiding \(A\). If \(t\le q\), at most \(t(q+1)\) lines meet \(A\), and therefore
\[
u(A)\ge N-t(q+1).
\]
Moreover,
\[
N-t(q+1)-(q+1-t)=q(q-t)\ge0,
\]
so
\[
t+u(A)\ge q+1.
\]
For \(t\ge q+1\), this inequality is immediate. Lemma 2.1 therefore gives
\[
\gamma(S_q)\ge q+1.
\]
Conversely, the \(q+1\) points of any projective line meet every line, so they form a dominating set of \(S_q\). Thus
\[
\boxed{\gamma(S_q)=q+1,\qquad \alpha _2(S_q)=1.}
\]

Every split graph is:

- \(2K_2\)-free;
- chordal;
- \(P_5\)-free, since an induced \(P_5\) contains an induced \(2K_2\) on its two end edges.

Consequently, the ratio is unbounded even among diameter-two split graphs, and hence among chordal graphs and among \(P_5\)-free graphs.

---

### 3.2 Diameter-two claw-free graphs

Let \(R_n\) be the rook graph on \([n]\times[n]\), where
\[
(i,j)\sim(i',j')
\quad\Longleftrightarrow\quad
i=i'\text{ or }j=j'.
\]
Equivalently, \(R_n=L(K_{n,n})\).

Any two nonadjacent cells \((i,j)\) and \((i',j')\) have the common two-step path
\[
(i,j)-(i,j')-(i',j'),
\]
so \(R_n\) has diameter two and
\[
\alpha _2(R_n)=1.
\]

For a dominating set \(D\), let \(A\) be the set of rows occupied by \(D\), and \(B\) the set of columns occupied by \(D\). A cell \((i,j)\) is dominated exactly when
\[
i\in A\quad\text{or}\quad j\in B.
\]
If some row and some column are both unoccupied, their intersection is undominated. Thus either every row or every column is occupied, forcing
\[
|D|\ge n.
\]
A full row is a dominating set of size \(n\), so
\[
\boxed{\gamma(R_n)=n,\qquad \alpha _2(R_n)=1.}
\]

The neighbors of a cell are the union of its row clique and its column clique, so no cell can have three pairwise nonadjacent neighbors. Hence \(R_n\) is claw-free.

Thus the ratio is unbounded for line graphs and for claw-free graphs.

---

### 3.3 Bipartite graphs of girth at least six

Let \(B_q\) be the ordinary point-line incidence graph of \(PG(2,q)\). It is bipartite, \((q+1)\)-regular, and has
\[
2N=2(q^2+q+1)
\]
vertices. It has no \(4\)-cycle because two points lie on a unique common line, so its girth is at least six.

Any two points have distance two, as do any two lines. Hence a 2-independent set contains at most one point and at most one line. A nonincident point-line pair has distance three, so
\[
\alpha _2(B_q)=2.
\]

Every closed neighborhood has size \(q+2\). Consequently, for every dominating set \(D\),
\[
2N\le |D|(q+2),
\]
and hence
\[
\gamma(B_q)\ge \frac{2N}{q+2}.
\]
It follows that
\[
\frac{\gamma(B_q)}{\alpha _2(B_q)}
 \ge \frac{q^2+q+1}{q+2}\longrightarrow\infty.
\]

Thus the ratio is unbounded even among bipartite \(C_4\)-free graphs, and in particular among graphs of girth at least six.

---

## 4. The \(P_4\)-free positive case

We need the following elementary fact about cographs.

### Lemma 4.1
Every \(P_4\)-free graph \(G\) satisfies
\[
\gamma(G)\le 2\alpha _2(G).
\]

#### Proof

First suppose \(G\) is connected and has at least two vertices. We show that \(\overline G\) is disconnected. This is the usual cograph decomposition, but a proof is included.

Proceed by induction on \(|V(G)|\), choosing \(v\in V(G)\).

If \(G-v\) is disconnected, let its components be \(C_1,\ldots,C_r\), where \(r\ge2\). Since \(G\) is connected, \(v\) has a neighbor in every \(C_i\). If \(v\) also had a nonneighbor in some \(C_i\), a path inside \(C_i\) from a neighbor to a nonneighbor would contain adjacent vertices \(a,b\) with
\[
va\in E(G),\qquad vb\notin E(G).
\]
Choosing a neighbor \(z\) of \(v\) in another component, the vertices
\[
b,a,v,z
\]
would induce a \(P_4\). Hence \(v\) is universal, and therefore isolated in \(\overline G\).

If \(G-v\) is connected, induction says that \(\overline{G-v}\) has components \(A_1,\ldots,A_r\), \(r\ge2\). Thus all edges between distinct \(A_i\)'s occur in \(G\). If \(v\) is complete to some \(A_i\), then \(A_i\) is a component of \(\overline G\). Otherwise \(v\) has a nonneighbor in every \(A_i\). Since \(G\) is connected, \(v\) has a neighbor \(x\) in some \(A_j\). Along a path in the connected graph \(\overline G[A_j]\), choose consecutive vertices \(x',y'\) such that \(vx'\) is an edge and \(vy'\) is not. Choose \(z\) in another \(A_i\) nonadjacent to \(v\). Then
\[
v,x',z,y'
\]
induces a \(P_4\), a contradiction.

Thus \(\overline G\) is disconnected. Its components give a nontrivial join decomposition of \(G\). Choosing one vertex from each of two distinct complement-components gives a dominating set of size two. Therefore every connected \(P_4\)-free graph has domination number at most two.

For a disconnected \(P_4\)-free graph with \(c\) components,
\[
\gamma(G)\le2c.
\]
Choosing one vertex from each component gives a 2-independent set, so \(\alpha _2(G)\ge c\). Hence
\[
\gamma(G)\le2\alpha _2(G).
\]
\(\square\)

The factor two is sharp, for example on \(C_4\), where \(\gamma(C_4)=2\) and \(\alpha _2(C_4)=1\).

---

## 5. Proof of the single-forbidden-induced-graph classification

We now prove Theorem 1.

### 5.1 Sufficiency

First let \(H=sK_1\). If \(G\) is \(H\)-free, then its ordinary independence number satisfies
\[
\alpha(G)\le s-1.
\]
A maximal independent set is dominating, so
\[
\gamma(G)\le s-1.
\]
Since \(\alpha _2(G)\ge1\), the ratio is bounded.

Now let
\[
H=F+sK_1,\qquad F\in\{K_2,P_3,P_4\}.
\]

If \(G\) has no induced copy of \(F\), then \(G\) is \(P_4\)-free, because every \(P_4\) contains an induced \(K_2\), \(P_3\), and \(P_4\). Lemma 4.1 gives
\[
\gamma(G)\le2\alpha _2(G).
\]

Suppose instead that \(G\) contains an induced copy \(X\) of \(F\). Necessarily \(s\ge1\), since \(G\) is \(H\)-free. Let
\[
U=\{v\in V(G)\setminus X:N(v)\cap X=\varnothing\}.
\]
If \(G[U]\) had an independent set of size \(s\), then that set together with \(X\) would induce \(F+sK_1=H\). Therefore
\[
\alpha(G[U])\le s-1.
\]
Choose a maximal independent set \(I\) of \(G[U]\). Then \(|I|\le s-1\), and \(I\) dominates \(U\). Every vertex outside \(X\cup U\) has a neighbor in \(X\). Hence
\[
X\cup I
\]
is a dominating set of \(G\), of size at most
\[
|V(F)|+s-1.
\]
This proves boundedness in all listed positive cases.

---

### 5.2 Necessity

Suppose first that \(H\) has at least two components containing edges. Choosing one edge from each of two such components gives an induced \(2K_2\) inside \(H\). Since every \(S_q\) is \(2K_2\)-free, it is also \(H\)-free. But
\[
\frac{\gamma(S_q)}{\alpha _2(S_q)}=q+1\to\infty.
\]

It remains to consider
\[
H=F+sK_1,
\]
where \(F\) is connected, contains an edge, and is not one of \(K_2,P_3,P_4\). It suffices to find an unbounded-ratio family avoiding \(F\).

There are four exhaustive cases.

1. **\(F\) is cyclic and chordal.**  
   Every cyclic chordal graph contains a triangle. The bipartite graphs \(B_q\) are therefore \(F\)-free and have unbounded ratio.

2. **\(F\) is nonchordal.**  
   Every induced subgraph of a chordal graph is chordal. Thus the chordal split graphs \(S_q\) are \(F\)-free and have unbounded ratio.

3. **\(F\) is a tree with maximum degree at least three.**  
   Then \(F\) contains an induced claw. The claw-free rook graphs \(R_n\) are \(F\)-free and have unbounded ratio.

4. **\(F\) is a tree with maximum degree at most two.**  
   Then \(F=P_t\). Since \(F\notin\{K_2,P_3,P_4\}\), one has \(t\ge5\). The \(P_5\)-free split graphs \(S_q\) are \(F\)-free and have unbounded ratio.

These cases prove necessity and complete the proof of Theorem 1. \(\square\)

In particular,
\[
\rho(\operatorname{Forb}_{\mathrm{ind}}(P_t))<\infty
\quad\Longleftrightarrow\quad t\le4,
\]
and
\[
\rho(\operatorname{Forb}_{\mathrm{ind}}(K_{1,t}))<\infty
\quad\Longleftrightarrow\quad t\le2.
\]

---

## 6. Extremal growth on \(n\) vertices

### 6.1 Upper bound

Let \(G\) have \(n\) vertices and put
\[
k=\alpha _2(G),\qquad a=1+\log n.
\]

If \(k>n/a\), then the trivial bound \(\gamma(G)\le n\) gives
\[
\frac{\gamma(G)}k<a.
\]

Suppose now that \(k\le n/a\), and set
\[
x=\sqrt{\frac{na}{k}},
\qquad
T=\lceil x\rceil.
\]
Then \(T\ge a\).

Let
\[
L=\{v\in V(G):d(v)<T\}.
\]
Choose a maximal 2-independent set \(P\subseteq L\), where distances are measured in \(G\). Then \(|P|\le k\), and every vertex of \(L\) is at distance at most two from \(P\). Consequently,
\[
D_0=\bigcup_{p\in P}N[p]
\]
dominates \(L\). Since \(d(p)<T\),
\[
|D_0|\le T|P|\le Tk.
\]

Every vertex outside \(L\) has degree at least \(T\). Independently select every vertex of \(G\) with probability
\[
r=\frac aT\le1,
\]
and call the resulting set \(R\). Add to \(R\) every vertex of \(V(G)\setminus L\) not dominated by \(R\); call this added set \(U\). Then \(D_0\cup R\cup U\) dominates \(G\), and
\[
\mathbb E|R|=\frac{an}{T}.
\]
For \(v\notin L\),
\[
\Pr(N[v]\cap R=\varnothing)
 =(1-r)^{d(v)+1}
 \le e^{-r(T+1)}
 \le e^{-a}.
\]
Thus
\[
\mathbb E|U|\le ne^{-a}=e^{-1}.
\]
Some realization therefore satisfies
\[
\gamma(G)\le Tk+\frac{an}{T}+1.
\]
Using \(T\le x+1\) and \(T\ge x\),
\[
Tk\le \sqrt{nak}+k,
\qquad
\frac{an}{T}\le\sqrt{nak}.
\]
Therefore
\[
\gamma(G)\le 2\sqrt{nak}+k+1,
\]
and hence
\[
\frac{\gamma(G)}{\alpha _2(G)}
 \le 2\sqrt{\frac{n(1+\log n)}{k}}+2
 \le 2\sqrt{n(1+\log n)}+2.
\]

---

### 6.2 Matching lower bound

For sufficiently large \(n\), let
\[
p=2\sqrt{\frac{\log n}{n}},
\qquad
s=\left\lfloor \frac18\sqrt{n\log n}\right\rfloor,
\]
and take \(G\sim G(n,p)\).

For a fixed pair \(u,v\), the probability that they have distance greater than two is at most
\[
(1-p)(1-p^2)^{n-2}
 \le \exp(-p^2(n-2))
 =n^{-4+o(1)}.
\]
A union bound over all pairs shows that \(G\) has diameter at most two with probability \(1-o(1)\). On this event,
\[
\alpha _2(G)=1.
\]

For a fixed set \(S\) of size \(s\), the probability that \(S\) dominates \(G\) is
\[
\left(1-(1-p)^s\right)^{n-s}
 \le \exp\left(-(n-s)(1-p)^s\right).
\]
For \(p\le1/2\),
\[
\log(1-p)\ge-p-p^2.
\]
Here
\[
ps\le \tfrac14\log n,\qquad p^2s=o(\log n),
\]
so, for all sufficiently large \(n\),
\[
(1-p)^s\ge n^{-1/3}.
\]
Therefore
\[
\Pr(S\text{ dominates }G)
 \le \exp\left(-\tfrac12n^{2/3}\right).
\]
Meanwhile,
\[
\binom ns
 \le \left(\frac{en}{s}\right)^s
 =\exp\!\left(O\!\left(\sqrt n(\log n)^{3/2}\right)\right)
 =\exp(o(n^{2/3})).
\]
A union bound shows that, with probability \(1-o(1)\), no set of size \(s\) dominates \(G\). A smaller dominating set could be enlarged to one of size \(s\), so
\[
\gamma(G)>s.
\]

Thus for every sufficiently large \(n\), there exists a diameter-two graph satisfying
\[
\frac{\gamma(G)}{\alpha _2(G)}
 =\gamma(G)
 \ge \frac19\sqrt{n\log n},
\]
say. Together with the upper bound, this proves
\[
R(n)=\Theta(\sqrt{n\log n}).
\]

---

## 7. What remains open

Theorem 1 settles only hereditary classes defined by a single forbidden induced graph. It does not handle classes defined by several forbidden induced graphs, where different restrictions can simultaneously eliminate the split, claw-free, and bipartite obstruction families.

More fundamentally, Lemma 2.1 shows that hereditary subclasses of split graphs already encode hypergraph classes closed under subfamilies and traces. A full hereditary characterization must therefore control quite general packing-versus-covering behavior in set systems; the three explicit obstruction families above are not claimed to be exhaustive for arbitrary hereditary classes.

No extension of the source paper's characterization to all monotone classes or to arbitrary dense hereditary classes is proved here.