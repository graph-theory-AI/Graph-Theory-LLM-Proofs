```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact local contraction identity is proved, yielding complete characterizations for triangle-free graphs, complete multipartite graphs, cographs recursively, and graphs whose complement has maximum degree at most two.",
  "would_publish": false,
  "caveats": "The exact criterion still involves clique counting, and no global structural characterization or unrestricted recognition complexity is obtained."
}
```

# Partial characterization of social graphs

All graphs below are finite and simple. Let \(\kappa(H)\) denote the number of cliques of \(H\), including the empty clique. Including the empty clique is harmless: excluding it changes both \(\kappa(G)\) and \(\kappa(G/e)\) by one.

## 1. An exact local contraction formula

Let \(uv\in E(G)\), and put
\[
A=N_G(u)\setminus N_G[v],\qquad
B=N_G(v)\setminus N_G[u],\qquad
C=N_G(u)\cap N_G(v),
\]
and \(U=A\cup B\cup C\).

Define \(\mu_G(u,v)\) to be the number of cliques \(Q\) of \(G[U]\) satisfying
\[
Q\cap A\neq\varnothing
\quad\text{and}\quad
Q\cap B\neq\varnothing.
\]

### Theorem 1
For every edge \(uv\),
\[
\boxed{\ \kappa(G/uv)-\kappa(G)
   =\mu_G(u,v)-2\kappa(G[C]).\ }
\tag{1}
\]
Consequently,
\[
G\text{ is social}
\quad\Longleftrightarrow\quad
\mu_G(u,v)\le 2\kappa(G[C])
\quad\text{for every }uv\in E(G).
\tag{2}
\]

### Proof
Cliques of \(G\) can be partitioned into those avoiding \(u,v\), those containing \(u\) but not \(v\), those containing \(v\) but not \(u\), and those containing both. Thus
\[
\begin{aligned}
\kappa(G)
={}&\kappa(G-\{u,v\})
 +\kappa(G[A\cup C])
 +\kappa(G[B\cup C])
 +\kappa(G[C]).
\end{aligned}
\tag{3}
\]

After contracting \(uv\) to a vertex \(w\), the neighborhood of \(w\) is \(U\). Hence
\[
\kappa(G/uv)=\kappa(G-\{u,v\})+\kappa(G[U]).
\tag{4}
\]

A clique of \(G[U]\) not counted by \(\mu_G(u,v)\) avoids \(A\) or avoids \(B\). Inclusion-exclusion therefore gives
\[
\kappa(G[U])
=
\kappa(G[A\cup C])+\kappa(G[B\cup C])
-\kappa(G[C])+\mu_G(u,v).
\tag{5}
\]
Subtracting (3) from (4) proves (1). ∎

This is a formally exact characterization, but it is not yet the desired global structural characterization: \(\mu_G(u,v)\) can encode exponentially many cliques.

---

## 2. Consequences of the local formula

### 2.1 Induced-\(C_4\)-free graphs

For \(a\in A\) and \(b\in B\), the edge \(ab\) exists if and only if
\[
u,v,b,a,u
\]
is an induced \(4\)-cycle: the two missing diagonals are \(ub\) and \(va\).

Every clique counted by \(\mu_G(u,v)\) contains such an edge \(ab\). Therefore:

### Corollary 2
Every induced-\(C_4\)-free graph is social. Indeed, contracting any edge strictly decreases its number of cliques.

### Proof
For every edge \(uv\), there are no edges between \(A\) and \(B\), so \(\mu_G(u,v)=0\). Equation (1) gives
\[
\kappa(G/uv)-\kappa(G)=-2\kappa(G[C])<0.
\]
∎

In particular, every chordal graph is social.

More generally, since every edge between \(A\) and \(B\) is itself a mixed clique, every social graph satisfies the necessary condition
\[
\#\{\text{induced }C_4\text{'s containing }uv\}
=e_G(A,B)\le 2\kappa(G[C])
\tag{6}
\]
for every edge \(uv\).

### 2.2 Triangle-free graphs

If \(G\) is triangle-free, then \(C=\varnothing\), so \(\kappa(G[C])=1\). Moreover, every mixed clique has exactly two vertices, one in \(A\) and one in \(B\). Thus \(\mu_G(u,v)=e_G(A,B)\).

### Corollary 3
A triangle-free graph \(G\) is social if and only if every edge of \(G\) lies in at most two \(4\)-cycles.

### Proof
In a triangle-free graph every \(4\)-cycle is induced, and the induced \(4\)-cycles containing \(uv\) are in bijection with edges between \(A\) and \(B\). Equation (1) becomes
\[
\kappa(G/uv)-\kappa(G)
=
\#\{C_4\ni uv\}-2.
\]
∎

For example,
\[
K_{a,b}\text{ is social}
\quad\Longleftrightarrow\quad
(a-1)(b-1)\le 2.
\]

### 2.3 \(K_4\)-free graphs

If \(G\) is \(K_4\)-free, then \(G[C]\) is independent: an edge inside \(C\), together with \(u,v\), would form a \(K_4\). Let \(t_{uv}\) be the number of triangles of \(G[U]\) meeting both \(A\) and \(B\). Since every clique has size at most three,
\[
\mu_G(u,v)=e_G(A,B)+t_{uv}.
\]

Hence a \(K_4\)-free graph is social exactly when
\[
e_G(A,B)+t_{uv}\le 2(1+|C|)
\tag{7}
\]
for every edge \(uv\).

More generally, for each fixed \(r\), sociality can be recognized in polynomial time on the class \(\omega(G)\le r\), by enumerating all cliques of size at most \(r\) in the sets occurring in (2). A naive bound is \(O(n^{r+2})\).

---

## 3. Complete multipartite graphs

Let
\[
G=K_{n_1,\ldots,n_s}
\]
with nonempty parts \(V_1,\ldots,V_s\). Consider an edge \(uv\) with \(u\in V_i\), \(v\in V_j\), \(i\ne j\). Then
\[
A=V_j\setminus\{v\},\qquad
B=V_i\setminus\{u\},\qquad
C=\bigcup_{\ell\notin\{i,j\}}V_\ell.
\]
A clique in \(C\) chooses at most one vertex from each remaining part, so
\[
\kappa(G[C])=\prod_{\ell\notin\{i,j\}}(n_\ell+1).
\]
A mixed clique chooses exactly one vertex from \(A\), exactly one from \(B\), and an arbitrary clique from \(C\). Consequently
\[
\mu_G(u,v)
=(n_i-1)(n_j-1)
 \prod_{\ell\notin\{i,j\}}(n_\ell+1).
\]

### Corollary 4
A complete multipartite graph \(K_{n_1,\ldots,n_s}\) is social if and only if
\[
\boxed{\ (n_i-1)(n_j-1)\le 2
\quad\text{for every }i\ne j.\ }
\tag{8}
\]

Equivalently, if \(n_1\ge n_2\ge\cdots\), it is enough to require
\[
(n_1-1)(n_2-1)\le 2.
\]
Thus either at most one part is nonsingleton, or the largest part has size at most \(3\) and every other part has size at most \(2\). This includes complements of matchings.

---

## 4. Joins, disjoint unions, and cographs

For a nonempty graph \(X\) and \(x\in V(X)\), define
\[
a_X(x)=\kappa(X[N_X(x)]),
\]
\[
d_X(x)=\kappa(X-x)-a_X(x),
\]
and
\[
\sigma_X(x)=\frac{d_X(x)}{a_X(x)},\qquad
\rho(X)=\max_{x\in V(X)}\sigma_X(x).
\tag{9}
\]
Here \(d_X(x)\) counts the cliques of \(X-x\) containing at least one nonneighbor of \(x\).

Let \(X\vee Y\) denote the join of \(X\) and \(Y\).

### Theorem 5
For nonempty graphs \(X,Y\),
\[
\boxed{\ X\vee Y\text{ is social}
\iff
X,Y\text{ are social and }\rho(X)\rho(Y)\le2.\ }
\tag{10}
\]
Moreover,
\[
\rho(X\vee Y)=\max\{\rho(X),\rho(Y)\}.
\tag{11}
\]

### Proof
First,
\[
\kappa(X\vee Y)=\kappa(X)\kappa(Y).
\]
If \(e\) is an edge internal to \(X\), then
\[
(X\vee Y)/e=(X/e)\vee Y,
\]
so
\[
\kappa((X\vee Y)/e)-\kappa(X\vee Y)
=
\kappa(Y)\bigl(\kappa(X/e)-\kappa(X)\bigr).
\]
Thus all internal edges are safe exactly when \(X\) and \(Y\) are social.

Now let \(xy\) be a cross-edge, with \(x\in X\), \(y\in Y\). In the notation of Theorem 1,
\[
A=V(Y)\setminus N_Y[y],\qquad
B=V(X)\setminus N_X[x],
\]
while the common neighborhood induces
\[
X[N_X(x)]\vee Y[N_Y(y)].
\]
Hence
\[
\kappa(C)=a_X(x)a_Y(y).
\]
A mixed clique decomposes uniquely into a clique of \(X-x\) meeting \(B\) and a clique of \(Y-y\) meeting \(A\). Therefore
\[
\mu_{X\vee Y}(x,y)=d_X(x)d_Y(y).
\]
By Theorem 1, the cross-edge is safe exactly when
\[
\sigma_X(x)\sigma_Y(y)\le2.
\]
This holds for all \(x,y\) exactly when \(\rho(X)\rho(Y)\le2\).

Finally, for \(x\in X\),
\[
a_{X\vee Y}(x)=a_X(x)\kappa(Y),\qquad
d_{X\vee Y}(x)=d_X(x)\kappa(Y),
\]
so \(\sigma_{X\vee Y}(x)=\sigma_X(x)\), and similarly for vertices of \(Y\). This proves (11). ∎

Disjoint unions behave even more simply:

### Proposition 6
A disjoint union is social if and only if every component is social.

Indeed,
\[
\kappa(X\mathbin{\dot\cup}Y)=\kappa(X)+\kappa(Y)-1,
\]
and contraction inside one component changes only that component's summand.

### Complete recursive characterization of social cographs

Define cographs recursively from \(K_1\) by disjoint unions and joins. The preceding results give an exact cotree characterization:

- At a disjoint-union node, the resulting graph is social iff all children are social.
- At a join node with child graphs \(X_1,\ldots,X_s\), the resulting graph is social iff all children are social and
  \[
  \rho(X_i)\rho(X_j)\le2
  \quad\text{for all }i\ne j.
  \tag{12}
  \]

The quantities needed at higher cotree nodes can be computed recursively. For \(Z=X_1\dot\cup\cdots\dot\cup X_s\) and \(v\in X_i\),
\[
a_Z(v)=a_{X_i}(v),
\qquad
d_Z(v)=d_{X_i}(v)+\sum_{j\ne i}\bigl(\kappa(X_j)-1\bigr).
\tag{13}
\]
For \(Z=X_1\vee\cdots\vee X_s\),
\[
a_Z(v)=a_{X_i}(v)\prod_{j\ne i}\kappa(X_j),
\qquad
d_Z(v)=d_{X_i}(v)\prod_{j\ne i}\kappa(X_j).
\tag{14}
\]
Also,
\[
\kappa(X_1\dot\cup\cdots\dot\cup X_s)
=1+\sum_i(\kappa(X_i)-1),
\qquad
\kappa(X_1\vee\cdots\vee X_s)=\prod_i\kappa(X_i).
\]
These formulas give a polynomial-time exact recognition algorithm for social cographs using integer arithmetic of \(O(n)\)-bit size.

---

## 5. Graphs whose complement has maximum degree at most two

This class is close to the dense regime motivating social graphs.

Let \(H=\overline G\), and let \(uv\notin E(H)\), so \(uv\in E(G)\). In terms of \(H\), the sets from Theorem 1 are
\[
A=N_H(v)\setminus N_H(u),\qquad
B=N_H(u)\setminus N_H(v),
\]
and
\[
C=V(H)\setminus\bigl(N_H[u]\cup N_H[v]\bigr).
\tag{15}
\]
Cliques of \(G\) are independent sets of \(H\). Thus \(\mu_G(u,v)\) is the number of independent sets of \(H[A\cup B\cup C]\) meeting both \(A\) and \(B\), while
\[
\kappa(G[C])=i(H[C]),
\]
where \(i(F)\) denotes the number of independent sets of \(F\), including the empty set.

### 5.1 Complements of paths and cycles

Let
\[
I_r=i(P_r),\qquad I_0=1,\quad I_1=2,\quad
I_r=I_{r-1}+I_{r-2}.
\tag{16}
\]

### Proposition 7
For \(n\ge1\),
\[
\overline{P_n}\text{ is social}\iff n\le5.
\tag{17}
\]
For \(n\ge3\),
\[
\overline{C_n}\text{ is social}\iff n\le6.
\tag{18}
\]

### Proof: small cases
Every edge of \(\overline H\) corresponds to a nonedge of \(H\). The following tables list all nonedge orbits under path reversal or cycle symmetry. The last two columns are \(\mu\) and \(i(H[C])\).

For paths:
\[
\begin{array}{c|c|c|c}
H&\{u,v\}&\mu&i(H[C])\\ \hline
P_3&13&0&1\\
P_4&13,\ 14&0,\ 0&1,\ 1\\
P_5&13,\ 24,\ 14,\ 15&0,\ 1,\ 1,\ 1&2,\ 1,\ 1,\ 2
\end{array}
\]
The pairs omitted are reversals of listed pairs. \(P_1,P_2\) have no nonedges giving nontrivial checks. All entries satisfy \(\mu\le2i(H[C])\).

For cycles, writing \(d\) for cyclic distance:
\[
\begin{array}{c|c|c|c}
H&d(u,v)&\mu&i(H[C])\\ \hline
C_4&2&0&1\\
C_5&2&0&1\\
C_6&2&1&2\\
C_6&3&2&1
\end{array}
\]
The graph \(C_3\) has no nonedges. Thus the asserted small complements are social.

### Proof: long paths
Let \(H=P_n\) with \(n\ge6\), take \(u=2\), \(v=5\), and put \(r=n-6\). Then
\[
A=\{4,6\},\qquad B=\{1,3\},\qquad C=\{7,\ldots,n\},
\]
where \(H[C]\cong P_r\). Moreover,
\[
H[A\cup B\cup C]\cong P_1\dot\cup P_2\dot\cup P_{r+1}.
\]
Inclusion-exclusion over the requirements to meet \(A\) and \(B\) gives
\[
\begin{aligned}
\mu
&=6I_{r+1}-4I_r-2I_{r+1}+I_r\\
&=4I_{r+1}-3I_r.
\end{aligned}
\tag{19}
\]
For \(r=0\), this is \(5>2=2I_0\). For \(r\ge1\),
\[
\mu-2I_r=4I_{r-1}-I_r>0,
\]
since \(I_r\le2I_{r-1}\). Thus the edge \(25\) is increasing in \(\overline{P_n}\).

### Proof: long cycles
Let \(H=C_n\) with \(n\ge7\), take \(u=0\), \(v=3\), and put \(r=n-6\ge1\). Then
\[
A=\{2,4\},\qquad B=\{1,n-1\},\qquad
C=\{5,\ldots,n-2\},
\]
with \(H[C]\cong P_r\), while
\[
H[A\cup B\cup C]\cong P_2\dot\cup P_{r+2}.
\]
Consequently,
\[
\begin{aligned}
\mu
&=3I_{r+2}-4I_{r+1}+I_r\\
&=3I_r-I_{r-1}.
\end{aligned}
\]
Hence
\[
\mu-2I_r=I_r-I_{r-1}>0.
\]
Thus \(\overline{C_n}\) is not social for \(n\ge7\). ∎

For example, contracting the edge corresponding to \(2,5\) in \(\overline{P_6}\) increases the clique count by \(3\), and the displayed edge in \(\overline{C_7}\) increases it by \(1\).

### 5.2 Combining components

For \(G=\overline H\), equation (9) becomes
\[
\sigma_{\overline H}(v)
=
\frac{i(H-v)}{i(H-N_H[v])}-1.
\tag{20}
\]
For the social path and cycle factors, this gives:
\[
\begin{array}{c|ccccccccc}
F&P_1&P_2&P_3&P_4&P_5&C_3&C_4&C_5&C_6\\ \hline
\rho(\overline F)
&0&1&3&2&\frac73&2&\frac32&\frac53&\frac85
\end{array}
\tag{21}
\]

For paths, these values follow from
\[
\sigma_{\overline{P_n}}(j)
=
\frac{I_{j-1}I_{n-j}}
 {I_{\max(j-2,0)}I_{\max(n-j-1,0)}}-1.
\tag{22}
\]
For cycles, every vertex has the same value
\[
\sigma_{\overline{C_n}}(v)=\frac{I_{n-1}}{I_{n-3}}-1.
\tag{23}
\]

Every graph \(H\) with \(\Delta(H)\le2\) is a disjoint union of paths and cycles, and
\[
\overline{H_1\dot\cup\cdots\dot\cup H_s}
=
\overline{H_1}\vee\cdots\vee\overline{H_s}.
\]
The join theorem therefore gives the following complete characterization.

### Theorem 8
Let \(H\) satisfy \(\Delta(H)\le2\). Then \(\overline H\) is social if and only if \(H\) has one of the following forms, where \(r,s\ge0\):

1. 
   \[
   rP_2\dot\cup sP_1;
   \]
2. 
   \[
   F\dot\cup rP_2\dot\cup sP_1,
   \qquad
   F\in\{P_4,C_3,C_4,C_5,C_6\};
   \]
3. 
   \[
   F\dot\cup sP_1,
   \qquad
   F\in\{P_3,P_5\}.
   \]

### Proof
Proposition 7 first restricts every path component to order at most \(5\) and every cycle component to order at most \(6\).

From (21), every allowed component on at least three vertices has \(\rho\ge3/2\). Two such components have product at least \(9/4>2\), so Theorem 5 allows at most one of them.

A \(P_1\)-component has \(\rho=0\), hence imposes no restriction. A \(P_2\)-component has \(\rho=1\), so it can coexist with the exceptional component precisely when the latter has \(\rho\le2\). By (21), these are
\[
P_4,C_3,C_4,C_5,C_6,
\]
whereas \(P_3\) and \(P_5\) have \(\rho>2\). Multiple \(P_2\)-components are mutually compatible since \(1\cdot1\le2\). This gives exactly the three listed forms. ∎

## 6. Remaining gap

Theorem 1 reduces sociality to a precise local inequality, and the subsequent results give genuine structural characterizations in several broad classes:

- all triangle-free graphs;
- all complete multipartite graphs;
- all cographs, recursively;
- all graphs \(G\) with \(\Delta(\overline G)\le2\).

However, for unrestricted graphs the mixed-clique quantity \(\mu_G(u,v)\) can involve cliques of unbounded size and complicated overlap. The argument does not produce a global decomposition theorem, a forbidden-configuration characterization, or a polynomial-time recognition algorithm for arbitrary graphs. Thus the general characterization problem remains open.