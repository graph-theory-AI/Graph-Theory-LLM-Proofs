```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds for line graphs of simple graphs and for ordinary Mycielski graphs, using only cycles of lengths k and 2k.",
  "would_publish": false,
  "caveats": "Intended range k≥3; these are structural special cases, with no novelty claim, and the general case is not resolved."
}
```

# Partial results: line graphs and Mycielski graphs

Graphs are finite and simple, and cycles are unoriented, simple, and not necessarily induced. Write
\[
c_j(G)=\#\{\text{cycles of length }j\text{ in }G\},\qquad
b_k=\frac{(k-1)!}{2},\qquad T_k=(k+1)b_k.
\]

I address the intended range \(k\ge3\). Without this restriction, an odd cycle disproves the assertion for \(k=2\).

The results below take a different route from the supplied join argument. They do not assume that argument; the overlapping greedy-path counting ingredient is proved explicitly.

> **Theorem A — Line graphs.**  
> Let \(k\ge3\), and let \(G=L(H)\) be the line graph of a finite simple graph \(H\). If \(\chi(G)>k\), then
> \[
> c_k(G)+c_{2k}(G)\ge T_k.
> \]
> If \(\Delta(H)\le k\), the inequality is strict.
>
> Consequently, among \((k+1)\)-critical line graphs, equality in the original conjecture occurs only for \(K_{k+1}\).

> **Theorem B — Mycielski graphs.**  
> Let \(k\ge3\), and let \(G=M(F)\) be the ordinary Mycielski graph of a finite simple graph \(F\). If \(\chi(G)>k\), then
> \[
> c_k(G)+c_{2k}(G)\ge T_k.
> \]
> In fact, for \(k\ge4\),
> \[
> c_k(G)\ge T_k.
> \]

Both proofs are self-contained.

## 1. An edge-colouring lemma

The following is the part of the usual Vizing fan argument needed for Theorem A. Its proof is included to make the edge-colouring input explicit.

> **Lemma 1.**  
> Suppose \(R\) is a simple graph with \(\Delta(R)\le k\), is not \(k\)-edge-colourable, and becomes \(k\)-edge-colourable after deletion of any edge. Then the vertices of degree \(k\) induce a nonempty graph of minimum degree at least \(2\).

### Proof

We first prove the stronger assertion that, for every edge \(xy\),
\[
x\text{ has at least }k-d_R(y)+1
\text{ neighbours of degree }k\text{ other than }y.
\tag{1}
\]

Fix a proper \(k\)-edge-colouring \(\varphi\) of \(R-xy\). Let \(M(z)\) be the set of colours missing at \(z\).

A **fan at \(x\)** is a sequence of distinct neighbours
\[
y_1=y,y_2,\ldots,y_t
\]
such that, for every \(i\ge2\), the colour of \(xy_i\) is missing at some earlier \(y_j\).

A fan can be rotated to leave \(xy_i\) uncoloured instead of \(xy_1\): follow a chain of the preceding indices and move each edge-colour onto the preceding uncoloured edge. This preserves properness and the set of colours missing at \(x\). In particular, if a colour is missing at both \(x\) and \(y_i\), rotation followed by colouring \(xy_i\) gives a \(k\)-edge-colouring of \(R\), a contradiction.

We claim that
\[
M(x),M(y_1),\ldots,M(y_t)
\quad\text{are pairwise disjoint.}
\tag{2}
\]
Suppose \(j\) is the first index at which this fails. An intersection between \(M(y_j)\) and \(M(x)\) was just ruled out. Thus some colour \(\beta\) is missing at both \(y_i\) and \(y_j\), where \(i<j\).

Choose \(\alpha\in M(x)\); such a colour exists because \(xy\) is uncoloured and \(d_R(x)\le k\). By the minimality of \(j\), \(\alpha\) is present at every \(y_h\) with \(h<j\), and \(\beta\) is missing at exactly one of these vertices, namely \(y_i\). We may also assume \(\alpha\) is present at \(y_j\), since otherwise \(M(x)\cap M(y_j)\ne\varnothing\).

In the subgraph consisting of the \(\alpha\)- and \(\beta\)-coloured edges, each of \(x,y_i,y_j\) has degree one. Therefore the component containing \(x\) cannot contain both \(y_i\) and \(y_j\).

* If \(y_i\) is not in that component, interchange \(\alpha\) and \(\beta\) on the component containing \(y_i\). The fan prefix through \(y_i\) remains valid: colours on edges incident with \(x\) are unchanged, and all earlier fan vertices retain their missing-colour sets. Now \(\alpha\) is missing at both \(x\) and \(y_i\), permitting an extension.
* Otherwise, interchange the colours on the component containing \(y_j\). This component contains neither \(x\) nor \(y_i\). All earlier fan vertices retain their missing-colour sets, so the fan prefix through \(y_j\) remains valid. Again \(\alpha\) is now missing at both ends of the edge to which the fan can be rotated.

Both alternatives contradict the non-\(k\)-edge-colourability of \(R\), proving (2).

Now take a maximal fan. Every colour missing at a fan vertex is present at \(x\), by (2). Its edge at \(x\) must lead to another fan vertex, by maximality. Since \(xy_1\) is uncoloured, this gives
\[
\left|\bigcup_{i=1}^{t}M(y_i)\right|\le t-1.
\tag{3}
\]

Let \(q\) be the number of vertices of degree \(k\) among \(y_2,\ldots,y_t\). By (2),
\[
\begin{aligned}
\left|\bigcup_{i=1}^{t}M(y_i)\right|
&=\sum_{i=1}^{t}|M(y_i)|\\
&\ge k-d_R(y_1)+1+(t-1-q).
\end{aligned}
\]
Together with (3), this proves (1).

Applying (1) to any edge shows that vertices of degree \(k\) exist. If \(x\) has degree \(k\), then either all its neighbours have degree \(k\), or it has a neighbour \(y\) with \(d_R(y)\le k-1\). In the latter case, (1) supplies at least two degree-\(k\) neighbours of \(x\). Thus the degree-\(k\) vertices induce a graph of minimum degree at least two. \(\square\)

## 2. Proof for line graphs

Recall that vertices of \(L(H)\) are edges of \(H\), with adjacency corresponding to incidence. Thus
\[
\chi(L(H))=\chi'(H).
\]

If \(H\) has a vertex of degree at least \(k+1\), its incident edges give a \(K_{k+1}\) in \(L(H)\). This supplies
\[
(k+1)\frac{(k-1)!}{2}=T_k
\]
cycles of length \(k\).

It remains to consider \(\Delta(H)\le k\). Choose an edge-minimal subgraph \(R\subseteq H\) that is not \(k\)-edge-colourable. By Lemma 1, the degree-\(k\) vertices of \(R\) induce a graph containing a cycle. Choose a shortest such cycle,
\[
Q=u_1u_2\cdots u_\ell u_1.
\]
It is chordless in \(R\): any chord would also be an edge between degree-\(k\) vertices and would yield a shorter cycle.

Put
\[
e_i=u_i u_{i+1},
\]
with subscripts modulo \(\ell\). In \(L(R)\), the \(k\) edges incident with \(u_i\) form a clique \(K_i\cong K_k\). Write
\[
V(K_i)=\{e_{i-1},e_i\}\cup B_i,
\qquad |B_i|=k-2.
\]
Because \(Q\) is chordless and \(R\) is simple, the sets \(B_i\) are pairwise disjoint and avoid all \(e_j\).

### 2.1 Cycles inside the star cliques

Each \(K_i\) supplies \(b_k\) cycles of length \(k\). These cycles are distinct for different \(i\), since two star cliques intersect in at most one vertex. Hence
\[
c_k(L(R))\ge \ell b_k.
\tag{4}
\]

### 2.2 Cycles going around the clique necklace

Choose integers \(0\le t_i\le k-2\). At each \(u_i\), choose an ordered list of \(t_i\) distinct elements of \(B_i\). Insert this list between \(e_{i-1}\) and \(e_i\). The resulting sequence is a simple cycle in \(L(R)\), of length
\[
\ell+\sum_i t_i.
\]

For a fixed vector \((t_1,\ldots,t_\ell)\), the number of cycles obtained is
\[
\prod_{i=1}^{\ell}\frac{(k-2)!}{(k-2-t_i)!}.
\tag{5}
\]
There is no division by two: fixing the cyclic order of the distinguished vertices \(e_1,\ldots,e_\ell\) fixes the orientation in which the chosen lists are recovered. Thus different lists give different unoriented cycles.

Let
\[
a=(k-2)!,
\qquad b_k=\frac{(k-1)a}{2}.
\]

We now show that (4), supplemented by suitable \(2k\)-cycles from (5), is strictly larger than \(T_k\).

#### Case 1: \(\ell\ge k+1\)

If \(\ell>k+1\), (4) already gives more than \(T_k\) cycles.

If \(\ell=k+1\), (4) gives exactly the required lower bound. Taking
\[
t_1=k-2,\qquad t_2=1,\qquad t_i=0\quad(i\ge3)
\]
produces at least one additional cycle of length \(2k\).

#### Case 2: \(\ell=3\)

Take
\[
t_1=t_2=k-2,\qquad t_3=1.
\]
This produces
\[
N=a^2(k-2)
\]
cycles of length \(2k\). Since
\[
2(k-2)!\ge k-1,
\]
we have
\[
N\ge (k-2)b_k.
\]
Together with the \(3b_k\) star-clique cycles, this gives \(T_k\).

The inequality is strict for \(k\ge4\). For \(k=3\), the three vertices \(e_1,e_2,e_3\) give one further triangle, distinct from all the star-clique triangles. Thus the total is again strictly larger than \(T_k\).

#### Case 3: \(4\le\ell\le k\)

Take
\[
t_1=k-2,\qquad t_2=k+2-\ell,\qquad t_i=0\quad(i\ge3).
\]
These choices are valid, and the resulting cycles have length \(2k\). Their number is
\[
N=\frac{a^2}{(\ell-4)!}.
\]
Moreover,
\[
\begin{aligned}
\frac{N}{b_k}
&=\frac{2(k-2)!}{(k-1)(\ell-4)!}\\
&\ge \frac{2(k-2)(k-3)}{k-1}\\
&>k-3\\
&\ge k+1-\ell.
\end{aligned}
\]
Consequently,
\[
\ell b_k+N>(k+1)b_k=T_k.
\]

These cases exhaust all possibilities. Since \(L(R)\subseteq L(H)\), Theorem A follows. \(\square\)

### Critical equality

Suppose \(G=L(H)\) is \((k+1)\)-critical and has exactly \(T_k\) cycles whose lengths are divisible by \(k\).

If \(\Delta(H)\le k\), Theorem A gives a strict inequality, a contradiction. Otherwise \(G\) contains \(K_{k+1}\). Criticality then forces
\[
G=K_{k+1}.
\]
Conversely, \(K_{k+1}\) has exactly \(T_k\) relevant cycles.

## 3. Proof for ordinary Mycielski graphs

For a graph \(F\), its ordinary Mycielski graph \(M(F)\) has:

* the original vertices \(V(F)\);
* a shadow \(x'\) for every \(x\in V(F)\);
* one additional vertex \(w\).

It retains all edges of \(F\), adds \(x'y\) and \(y'x\) for every \(xy\in E(F)\), and joins \(w\) to every shadow. There are no edges between shadows.

Colouring each shadow like its original vertex and using a new colour for \(w\) shows that
\[
\chi(M(F))\le\chi(F)+1.
\]
Therefore \(\chi(M(F))>k\) implies \(\chi(F)\ge k\).

### 3.1 The case \(k\ge4\)

Choose a \(k\)-critical subgraph \(F_0\subseteq F\), and write \(n=|V(F_0)|\). Criticality gives
\[
\delta(F_0)\ge k-1.
\]

Count ordered simple paths on \(k-1\) vertices in \(F_0\). There are \(n\) choices for the first vertex, then at least
\[
k-1,\ k-2,\ \ldots,\ 2
\]
choices at successive steps. Thus the number of these ordered paths is at least
\[
n(k-1)!.
\tag{6}
\]

An ordered path
\[
x_0x_1\cdots x_{k-2}
\]
gives the following \(k\)-cycle in \(M(F_0)\):
\[
w\,x_0'\,x_1\,x_2\,\cdots\,x_{k-3}\,x_{k-2}'\,w.
\tag{7}
\]
The assumption \(k\ge4\) ensures that there is at least one original vertex between the two shadows.

Each cycle constructed in (7) determines its underlying path up to reversal. Consequently, (6) gives at least
\[
\frac{n(k-1)!}{2}=n b_k
\tag{8}
\]
distinct \(k\)-cycles through \(w\).

If \(n\ge k+1\), (8) is already at least \(T_k\). If \(n=k\), then \(\delta(F_0)\ge k-1\) forces \(F_0=K_k\). Its \(b_k\) Hamilton cycles avoid \(w\), and are additional to (8). Hence in this case too,
\[
c_k(M(F_0))\ge kb_k+b_k=T_k.
\]

Since \(M(F_0)\subseteq M(F)\), this proves the stronger assertion in Theorem B for \(k\ge4\).

### 3.2 The case \(k=3\)

Here \(\chi(F)\ge3\), so \(F\) contains an odd cycle \(C\).

If \(C\) is a triangle, \(M(C)\) contains four triangles: the original triangle and the three triangles obtained by replacing exactly one original vertex by its shadow.

Otherwise, let \(C\) have odd length \(n\ge5\). It has \(2n\) ordered paths of four edges that follow the cycle. Every such path
\[
x_0x_1x_2x_3x_4
\]
gives the \(6\)-cycle
\[
w\,x_0'\,x_1\,x_2\,x_3\,x_4'\,w.
\]
Again the underlying path is recoverable up to reversal, so these give \(n\ge5\) distinct \(6\)-cycles.

Thus in either case \(M(F)\) has at least
\[
T_3=4
\]
cycles of length divisible by \(3\). This completes the proof of Theorem B. \(\square\)

## 4. Scope and remaining gap

The partial results establish
\[
\boxed{\quad c_k(G)+c_{2k}(G)\ge T_k\quad}
\]
for both structural classes above. For ordinary Mycielski graphs and \(k\ge4\), cycles of length exactly \(k\) suffice.

By subgraph monotonicity, the same conclusions apply whenever an arbitrary graph contains an appropriately high-chromatic subgraph of either type.

However, no reduction of a general \((k+1)\)-critical graph to these configurations has been proved. The limitation is substantial:

* the line-graph argument relies on a cyclic arrangement of large star cliques;
* the Mycielski argument relies on shadow vertices and an apex.

In particular, neither mechanism supplies a general high-girth argument: the line-graph certificate contains triangles, while a high-chromatic ordinary Mycielski graph contains a \(4\)-cycle.

Thus this is a rigorous special-case result, not a proof of the conjecture for arbitrary graphs. I make no claim that these special cases are new.