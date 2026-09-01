```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured upper bound remains open, but I prove the constant-order lower bound Omega_d(n^{2-1/d}) for every rational d>1 and give a useful orientation decomposition.",
  "would_publish": false,
  "caveats": "This assumes the source definition rho(H)=max e(H[S])/|S|; novelty relative to the journal version has not been checked."
}
```

# Mathematical writeup

## 1. Statement and convention

I use the standard maximum-density definition
\[
\rho(H):=\max_{\varnothing\neq S\subseteq V(H)}
\frac{e_H(S)}{|S|},
\qquad
\mathcal H_d(n):=\{H:v(H)=n,\ \rho(H)\le d\}.
\]

I do not prove the conjectured upper bound. I prove instead the following strengthening of the lower bound quoted in the prompt.

### Theorem A
For every rational \(d>1\), there are constants \(c_d>0\) and \(n_d\) such that every \(\mathcal H_d(n)\)-universal graph \(G\) satisfies
\[
e(G)\ge c_d n^{\,2-1/d}
\qquad(n\ge n_d).
\]

Thus, for rational \(d\), the \(n^{o(1)}\) loss in the quoted lower bound can be removed.

I also prove a structural decomposition of every graph in \(\mathcal H_d(n)\), recorded in Section 5.

---

## 2. A fractional certificate for bounded density

We use the following elementary observation.

### Lemma 2.1
Let \(F\) be a graph, and suppose that for every incidence \(v\in e\) there is a number \(\lambda_{v,e}\ge0\) such that

1. for every edge \(e=uv\),
   \[
   \lambda_{u,e}+\lambda_{v,e}=1;
   \]
2. for every vertex \(v\),
   \[
   \sum_{e\ni v}\lambda_{v,e}=d.
   \]

Then
\[
e(F)=d\,v(F)
\quad\text{and}\quad
\rho(F)\le d.
\]

#### Proof
Summing the vertex loads gives
\[
d\,v(F)
 =\sum_v\sum_{e\ni v}\lambda_{v,e}
 =\sum_{e=uv}(\lambda_{u,e}+\lambda_{v,e})
 =e(F).
\]

For \(S\subseteq V(F)\), every edge internal to \(S\) contributes exactly \(1\) to the loads of vertices in \(S\), while boundary edges contribute nonnegative amounts. Hence
\[
e_F(S)
 \le \sum_{v\in S}\sum_{e\ni v}\lambda_{v,e}
 =d|S|.
\]
Therefore \(\rho(F)\le d\). ∎

---

## 3. A finite balanced graph of every rational density

The key point is that such a certificate can be constructed explicitly for every rational \(d>1\).

### Lemma 3.1
For every rational \(d>1\), there is a finite simple connected graph \(F=F_d\) satisfying the hypotheses of Lemma 2.1.

#### Proof
Write
\[
d=k+\alpha,
\qquad
k=\lfloor d\rfloor\ge1,
\qquad
0\le\alpha<1.
\]
Choose an integer \(N>2(k+1)\) such that \(N\alpha\in\mathbb Z\). Identify the vertex set with \(\mathbb Z/N\mathbb Z\).

For \(i=0,\dots,N-1\), put
\[
\varepsilon_i
  :=\lfloor(i+1)\alpha\rfloor-\lfloor i\alpha\rfloor
  \in\{0,1\}.
\]
Then
\[
\sum_{i=0}^{N-1}\varepsilon_i=N\alpha.
\]

Define an auxiliary orientation of \(F\) as follows:

- for every \(i\) and every \(j\in\{1,\dots,k\}\), add the arc
  \[
  i\longrightarrow i+j;
  \]
- whenever \(\varepsilon_i=1\), also add
  \[
  i\longrightarrow i+(k+1).
  \]

All arithmetic is modulo \(N\). Since every forward difference is at most \(k+1\) and \(N>2(k+1)\), no two of these arcs give the same underlying undirected edge, and no pair of opposite arcs occurs. Thus the underlying graph \(F\) is simple. Its number of edges is
\[
kN+\sum_i\varepsilon_i
 =(k+\alpha)N=dN.
\]

We now define the incidence weights. For the cycle edge
\[
c_i=\{i,i+1\},
\]
set
\[
x_i:=1+\lfloor(i+1)\alpha\rfloor-(i+1)\alpha\in(0,1],
\]
and assign
\[
\lambda_{i,c_i}=1-x_i,
\qquad
\lambda_{i+1,c_i}=x_i.
\]
For every other auxiliary arc \(i\to j\), assign the entire edge to its tail:
\[
\lambda_{i,\{i,j\}}=1,
\qquad
\lambda_{j,\{i,j\}}=0.
\]

Because \(N\alpha\) is an integer, the sequence \(x_i\) is cyclic, with \(x_{-1}=x_{N-1}=1\). Moreover,
\[
x_i-x_{i-1}
 =\lfloor(i+1)\alpha\rfloor-\lfloor i\alpha\rfloor-\alpha
 =\varepsilon_i-\alpha.
\]

If all edges were assigned completely to their auxiliary tails, vertex \(i\) would have load \(k+\varepsilon_i\). The modified weights on the cycle subtract \(x_i\) at the outgoing cycle edge and add \(x_{i-1}\) at the incoming one. Consequently its actual load is
\[
k+\varepsilon_i-x_i+x_{i-1}
 =k+\varepsilon_i-(\varepsilon_i-\alpha)
 =k+\alpha=d.
\]
Lemma 2.1 now applies. The edges of cyclic difference \(1\) form a spanning cycle, so \(F\) is connected. ∎

For example, when \(d=6/5\), one may take a \(5\)-cycle together with one appropriately placed chord.

---

## 4. Counting lifts: proof of Theorem A

Fix the graph \(F\) from Lemma 3.1. Write
\[
N=v(F),\qquad Q=e(F)=dN.
\]

For an integer \(t\ge1\), a \(t\)-lift of \(F\) is defined on
\[
V(F)\times[t].
\]
For each base edge \(uv\), choose a permutation \(\pi_{uv}\in S_t\), and replace \(uv\) by the perfect matching
\[
\{(u,i)(v,\pi_{uv}(i)):i\in[t]\}.
\]

### 4.1 Every lift has density at most \(d\)

Give every lifted edge over \(uv\) the same endpoint weights as the base edge \(uv\). Every lifted vertex \((v,i)\) is incident with exactly one lifted edge over each base edge incident with \(v\). Its total load is therefore exactly the load of \(v\), namely \(d\).

By Lemma 2.1, every \(t\)-lift \(L\) satisfies
\[
\rho(L)\le d,
\qquad
v(L)=Nt,
\qquad
e(L)=Qt=dNt.
\]

The spanning cycle in \(F\) also shows that every lift has minimum degree at least \(2\).

### 4.2 Number of nonisomorphic lifts

For every one of the \(Q\) base edges we may choose an arbitrary permutation in \(S_t\). These choices give
\[
(t!)^Q
\]
distinct labeled graphs on the fixed vertex set \(V(F)\times[t]\): because \(F\) is simple, the matching between each fixed pair of fibers recovers its permutation.

An isomorphism class of graphs on \(Nt\) vertices has at most \((Nt)!\) labeled representatives. Hence the number \(\mathscr L_t\) of isomorphism types among these lifts satisfies
\[
|\mathscr L_t|
 \ge \frac{(t!)^Q}{(Nt)!}.
\]

Let \(n_t=Nt\). Using
\[
t!\ge (t/\mathrm e)^t,
\qquad
(Nt)!\le(Nt)^{Nt},
\]
we obtain
\[
\begin{aligned}
|\mathscr L_t|
&\ge
\frac{(t/\mathrm e)^{tdN}}{(Nt)^{Nt}}\\
&=
\left(\mathrm e^{-d}N^{-d}\,n_t^{\,d-1}\right)^{n_t}.
\end{aligned}
\tag{4.1}
\]

### 4.3 Counting edge subsets in a universal host

Let \(G\) be universal for \(\mathcal H_d(n_t)\), and put \(m=e(G)\). It must contain every graph in \(\mathscr L_t\). A copy of a lift is determined, as an abstract graph, by an edge subset of \(G\) having exactly \(dn_t\) edges. Since lifts have no isolated vertices, the same edge subset cannot represent two nonisomorphic lifts. Therefore
\[
\binom{m}{dn_t}\ge |\mathscr L_t|.
\]

Using
\[
\binom{m}{dn_t}
 \le
\left(\frac{\mathrm e m}{dn_t}\right)^{dn_t}
\]
and (4.1), we get
\[
\left(\frac{\mathrm e m}{dn_t}\right)^{dn_t}
 \ge
\left(\mathrm e^{-d}N^{-d}n_t^{d-1}\right)^{n_t}.
\]
Taking \(dn_t\)-th roots gives
\[
m\ge
\frac{d}{\mathrm e^2N}\,
n_t^{\,2-1/d}.
\tag{4.2}
\]

This proves the claimed lower bound whenever \(n\) is a multiple of \(N\).

For arbitrary \(n\ge2N\), let \(t=\lfloor n/N\rfloor\) and \(n_0=Nt\). Pad every lift on \(n_0\) vertices with \(n-n_0\) isolated vertices. These padded graphs remain in \(\mathcal H_d(n)\), and distinct core lifts remain nonisomorphic because the cores have no isolated vertices. Since \(n_0\ge n/2\), (4.2) yields
\[
e(G)\ge
\frac{d}{\mathrm e^2N}\,
2^{-(2-1/d)}n^{\,2-1/d}.
\]
This proves Theorem A. ∎

---

## 5. A structural decomposition for rational density

The following exact decomposition may be useful in approaching the upper bound.

### Proposition 5.1
Let \(d=a/b>1\), with \(a,b\in\mathbb N\), and let \(H\in\mathcal H_d(n)\). Then
\[
E(H)=E(B)\mathbin{\dot\cup}E(D),
\]
where

- \(B\) has maximum degree at most \(a\);
- \(D\) admits an orientation with maximum outdegree at most
  \[
  \left\lfloor\frac ab\right\rfloor=\lfloor d\rfloor;
  \]
- in fact the orientation can be chosen so that
  \[
  d_B(v)+b\,d_D^+(v)\le a
  \qquad\text{for every }v.
  \tag{5.1}
  \]

Consequently, \(D\) is the union of \(\lfloor d\rfloor\) pseudoforests.

#### Proof
Replace every edge of \(H\) by \(b\) parallel copies, obtaining a multigraph \(bH\). For every \(S\subseteq V(H)\),
\[
e_{bH}(S)=b\,e_H(S)\le a|S|.
\tag{5.2}
\]

We use the elementary assignment fact that a loopless multigraph \(M\) has an orientation of maximum outdegree at most \(a\) if and only if
\[
e_M(S)\le a|S|
\quad\text{for all }S.
\]
For completeness, construct a bipartite graph whose left side is \(E(M)\) and whose right side consists of \(a\) copies of every vertex. An edge-node is adjacent to all copies of its two endpoints. For any collection \(X\subseteq E(M)\), if \(W\) is the set of its endpoints, then
\[
|X|\le e_M(W)\le a|W|.
\]
Thus Hall's condition holds. Matching every edge-node to an endpoint assigns each edge to one endpoint, with no endpoint receiving more than \(a\) edges; orient away from the assigned endpoint.

Apply this to \(bH\) using (5.2). For an original edge \(uv\), let \(r_{uv}\) of its \(b\) copies be oriented \(u\to v\).

Put \(uv\) in \(D\) if \(r_{uv}\in\{0,b\}\), orienting it in the common direction of all its copies. Put \(uv\) in \(B\) if
\[
1\le r_{uv}\le b-1.
\]
Every \(B\)-edge incident with \(v\) consumes at least one unit of the outgoing-copy capacity at \(v\), while every outward \(D\)-edge consumes \(b\) units. Hence
\[
d_B(v)+b\,d_D^+(v)\le a.
\]
This proves all stated degree bounds.

Finally, color the outward \(D\)-edges at each vertex injectively with colors \(1,\dots,\lfloor d\rfloor\). Each color class has an orientation of outdegree at most \(1\), and hence every one of its components has at most one cycle. Thus each color class is a pseudoforest. ∎

In particular, when \(1<d<2\), every \(H\in\mathcal H_d(n)\) is the union of one pseudoforest and a graph of bounded maximum degree, with the stronger local coupling (5.1).

---

## 6. Remaining gap

Neither Theorem A nor Proposition 5.1 supplies the required universal graph.

The obstruction to using Proposition 5.1 directly is synchronization. A universal graph for \(B\) and a separate universal graph for \(D\) may embed the same vertex of \(H\) at different places. Taking a disjoint union or simply overlaying independently universal hosts does not produce a common embedding of \(B\cup D\). A proof of the conjecture needs a sparse construction supporting these two structures under one vertex map.

Thus the conjectured upper bound
\[
e(G)=O_d\!\left(n^{2-1/d}\right)
\]
remains open here. The established progress is the exact \(\Omega_d(n^{2-1/d})\) lower bound and the rational orientation decomposition above.