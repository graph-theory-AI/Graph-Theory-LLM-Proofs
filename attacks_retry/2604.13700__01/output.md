```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every finite simple r-regular digraph satisfies dtw(D) >= ceil(3r/11), giving the improved interval 3/11 <= epsilon_* <= 1.",
  "would_publish": false,
  "caveats": "The optimal constant remains undetermined; simplicity is essential, and novelty against the full source paper has not been independently checked."
}
```

# A self-contained \(3/11\) lower bound

I obtain a stronger lower bound than the numerical bound quoted in the question.

## Theorem
Let \(D\) be a finite simple loopless digraph, with digons permitted, such that
\[
d_D^+(v)=d_D^-(v)=r\ge 1
\qquad(v\in V(D)).
\]
Then
\[
\boxed{\operatorname{dtw}(D)\ge
\left\lceil\frac{3r}{11}\right\rceil.}
\]

Consequently, with the normalization of directed tree-width specified below,
\[
\boxed{\frac3{11}\le \varepsilon_*\le 1.}
\]

The argument does not use the quoted \(3/22\) theorem. The useful ingredient from the previous attempt is its leaf/digon observation; I reprove and strengthen it to a sparsity statement for every induced subdigraph. The additional ingredient is an Eulerian bound on the edge boundary of every guarded normal set.

I am not claiming that the bound below is absent from the full source paper or other literature; the novelty comparison here is only with the numerical bound supplied in the question.

---

## 1. Definitions and a normal-set boundary bound

For disjoint vertex sets \(A,B\), write \(e_D(A,B)\) for the number of arcs from \(A\) to \(B\), and write
\[
e_D(S)=|A(D[S])|.
\]

A set \(S\subseteq V(D)\setminus X\) is **\(X\)-normal** if no directed walk in \(D-X\) starts and ends in \(S\) while visiting a vertex outside \(S\).

We use the standard arboreal-decomposition definition of directed tree-width. An arboreal decomposition consists of a rooted out-tree \(T\), nonempty bags \(W_t\) partitioning \(V(D)\), and edge-guards \(X_e\). If \(U_e\) is the union of bags below \(e\), then \(U_e\) is \(X_e\)-normal, in particular \(U_e\cap X_e=\varnothing\). Its width is
\[
\max_{t\in V(T)}
\left|W_t\cup\bigcup_{e\ni t}X_e\right|-1.
\]
Thus a one-bag decomposition on \(n\) vertices has width \(n-1\).

### Lemma 1 — Eulerian boundary bound
If \(D\) is \(r\)-regular and \(S\) is \(X\)-normal, then
\[
e_D(S,V(D)\setminus S)\le r|X|.
\]
Equivalently,
\[
\boxed{r(|S|-|X|)\le e_D(S).} \tag{1}
\]

### Proof
Let \(R\) consist of the vertices outside \(S\) reachable from \(S\) in \(D-X\).

Normality implies that no vertex of \(R\) can reach \(S\) in \(D-X\). By the definition of \(R\), all arcs leaving \(R\) go to \(X\). Since \(D\) is Eulerian, every vertex-set has equally many entering and leaving arcs. Hence
\[
e_D(S,R)\le e_D(V(D)\setminus R,R)
=e_D(R,V(D)\setminus R)
=e_D(R,X).
\]
Every arc leaving \(S\) goes to \(X\) or \(R\), so
\[
e_D(S,V(D)\setminus S)
=e_D(S,X)+e_D(S,R)
\le e_D(S,X)+e_D(R,X)
\le r|X|.
\]
Finally,
\[
e_D(S,V(D)\setminus S)=r|S|-e_D(S),
\]
which gives (1). \(\square\)

This is where regularity is crucial: normality alone does not make the boundary small.

---

## 2. Sparsity forced by bounded directed tree-width

Let \(G_{\leftrightarrow}(D)\) be the undirected graph on \(V(D)\) in which \(uv\) is an edge precisely when both \(uv\) and \(vu\) are arcs of \(D\).

### Lemma 2
If \(\operatorname{dtw}(D)\le k\), then \(G_{\leftrightarrow}(D)\) is \(k\)-degenerate.

### Proof
Fix a width-\(k\) arboreal decomposition, and let \(Y\subseteq V(D)\) be nonempty. Choose a deepest node \(t\) whose bag meets \(Y\). Thus the only vertices of \(Y\) in the subtree rooted at \(t\) lie in \(W_t\).

Suppose first that \(t\) is not the root, and let \(X\) be its incoming edge-guard. For \(v\in W_t\cap Y\), every bidirected neighbor of \(v\) in \(Y\setminus W_t\) belongs to \(X\): otherwise the digon through that neighbor would leave the guarded subtree and return while avoiding \(X\).

Consequently,
\[
d_{G_{\leftrightarrow}(D)[Y]}(v)
\le |W_t\cap Y|-1+|X\cap Y|
\le k.
\]
Here \(W_t\cap X=\varnothing\), and their union is contained in the width set at \(t\).

If \(t\) is the root, then \(Y\subseteq W_t\), so again the degree is at most \(|W_t|-1\le k\).

Every induced subgraph therefore has a vertex of degree at most \(k\). \(\square\)

For integers \(m\ge0\), define
\[
g_k(m)=\sum_{i=0}^{m-1}\min\{i,k\},
\qquad
h_k(m)=\binom m2+g_k(m).
\]
A \(k\)-degenerate graph on \(m\) vertices has at most \(g_k(m)\) edges. Every unordered vertex-pair contributes at most one arc, plus one additional arc if it is a digon. Lemma 2 therefore gives
\[
\boxed{e_D(S)\le h_k(|S|)\qquad
\text{whenever }\operatorname{dtw}(D)\le k.} \tag{2}
\]

Explicitly,
\[
g_k(m)=
\begin{cases}
\binom m2,&m\le k+1,\\[2mm]
km-\binom{k+1}{2},&m\ge k+1,
\end{cases}
\]
and hence, for \(m\ge k+1\),
\[
h_k(m)=\frac{m^2+(2k-1)m-k(k+1)}2. \tag{3}
\]

Both sequences are discretely convex, since
\[
g_k(m+1)-g_k(m)=\min\{m,k\},
\]
and
\[
h_k(m+1)-h_k(m)=m+\min\{m,k\}
\]
are nondecreasing.

---

## 3. Two numerical inequalities

For \(k\ge1\), put
\[
\alpha_k=\frac{7k+1}{2},
\qquad
\rho_k=\frac{11k^2-3k}{3k-1}.
\]
Notice that
\[
\rho_k-\alpha_k
=\frac{(k-1)^2}{2(3k-1)}\ge0. \tag{4}
\]

### Lemma 3
For \(2k+1\le s\le3k+1\),
\[
\boxed{h_k(s)<\alpha_k(2s-3k-1).} \tag{5}
\]

### Proof
By (3), the difference
\[
\alpha_k(2s-3k-1)-h_k(s)
\]
is a concave quadratic in \(s\). At the two endpoints its values are respectively
\[
\frac{5k+1}{2}
\quad\text{and}\quad
\frac{7k^2+6k+1}{2},
\]
both positive. It is therefore positive throughout the interval. \(\square\)

### Lemma 4
If
\[
1\le p,q\le2k,\qquad p+q\ge2k+1,
\]
then
\[
\boxed{
h_k(p)+h_k(q)+pq
\le \rho_k(p+q-k-1).
} \tag{6}
\]

### Proof
Write \(s=p+q\). Since \(g_k\) is discretely convex, its sum at two arguments of fixed total is maximized by making those arguments as unequal as permitted. Thus
\[
g_k(p)+g_k(q)
\le g_k(2k)+g_k(s-2k).
\]
Using
\[
h_k(p)+h_k(q)+pq
=\binom s2+g_k(p)+g_k(q),
\]
and setting \(j=s-2k\), we obtain
\[
h_k(p)+h_k(q)+pq
\le h_k(2k)+h_k(j)+2kj,
\qquad 1\le j\le2k.
\]

The expression
\[
N(j)=h_k(2k)+h_k(j)+2kj
\]
is discretely convex. Its endpoint values are
\[
N(1)=k\alpha_k,
\qquad
N(2k)=(3k-1)\rho_k.
\]
By (4), both endpoints lie below or on the affine function
\[
j\longmapsto \rho_k(j+k-1).
\]
Discrete convexity places \(N(j)\) below the chord joining its endpoint values, so
\[
N(j)\le \rho_k(j+k-1).
\]
Since \(j+k-1=s-k-1\), this proves (6). \(\square\)

---

## 4. The main decomposition argument

We first prove a slightly more precise estimate.

### Proposition 5
If \(D\) is simple and \(r\)-regular, and
\[
k=\operatorname{dtw}(D)\ge1,
\]
then
\[
\boxed{r\le \rho_k=\frac{11k^2-3k}{3k-1}.} \tag{7}
\]

### Proof
Suppose instead that \(r>\rho_k\), and fix a width-\(k\) arboreal decomposition.

For a node \(t\), let \(U_t\) denote the union of all bags in its rooted subtree, and put
\[
B_t=W_t\cup\bigcup_{e\ni t}X_e.
\]
Thus \(|B_t|\le k+1\). Every edge-guard has size at most \(k\), because it is disjoint from the nonempty bag at its child endpoint.

Since
\[
|V(D)|\ge r+1>2k+1,
\]
we may choose a deepest node \(t\) with
\[
|U_t|\ge2k+1.
\]
Every child-subtree of \(t\) then has at most \(2k\) vertices.

Let \(X\) be the incoming guard of \(t\), or let \(X=\varnothing\) if \(t\) is the root. Write
\[
x=|X|,\qquad B=B_t,\qquad S=U_t\setminus B.
\]
Because \(X\subseteq B\) and \(X\cap U_t=\varnothing\),
\[
|B\cap U_t|\le k+1-x. \tag{8}
\]

### Step 1: \(S\) still has at least \(2k+1\) vertices

Suppose \(|S|\le2k\), and put \(s=|U_t|\). By (8),
\[
2k+1\le s\le3k+1-x.
\]
In particular,
\[
s-x\ge2s-3k-1.
\]

The set \(U_t\) is \(X\)-normal, so Lemmas 1 and 2 give
\[
r(s-x)\le e_D(U_t)\le h_k(s).
\]
On the other hand, \(r>\rho_k\ge\alpha_k\), and Lemma 3 gives
\[
r(s-x)
\ge\alpha_k(2s-3k-1)
>h_k(s),
\]
a contradiction. Therefore
\[
|S|\ge2k+1. \tag{9}
\]

### Step 2: Find a medium-sized normal prefix

The set \(S\) is \(B\)-normal: a walk in \(D-B\) leaving \(S\) also leaves \(U_t\), while avoiding \(X\).

Moreover, every strongly connected component of \(D-B\) meeting \(S\) lies entirely in one child-subtree of \(t\). Otherwise a closed walk in that component would leave and return to a child-subtree while avoiding its edge-guard, which is contained in \(B\).

Thus the strongly connected components contained in \(S\) all have size at most \(2k\). Order them topologically, and take the first prefix whose total size is at least \(2k+1\). Write this prefix as
\[
A=P\cup Q,
\]
where \(Q\) is the last component added and \(P\) is the union of the preceding components.

By minimality of the prefix,
\[
1\le p:=|P|\le2k,\qquad
1\le q:=|Q|\le2k,\qquad
p+q\ge2k+1. \tag{10}
\]
There is no arc from \(Q\) to \(P\).

Also, \(A\) is \(B\)-normal. Indeed, a walk cannot leave \(S\) and return because \(S\) is \(B\)-normal; within \(S\), it cannot leave a topological prefix and return.

### Step 3: Contradiction

Applying Lemma 1 to \(A\), and using \(|B|\le k+1\), gives
\[
r(p+q-k-1)\le e_D(A).
\]
Since there are no arcs from \(Q\) to \(P\), (2) and Lemma 4 yield
\[
e_D(A)
\le h_k(p)+h_k(q)+pq
\le \rho_k(p+q-k-1).
\]
The factor \(p+q-k-1\) is at least \(k>0\). Consequently \(r\le\rho_k\), contradicting our assumption. \(\square\)

---

## 5. Rounding and the exceptional width-one case

For \(r\ge1\), directed tree-width cannot be zero. Indeed, a width-zero decomposition has a one-vertex leaf bag with empty incoming guard; applying Lemma 1 to that bag gives \(r\le0\).

Thus \(k=\operatorname{dtw}(D)\ge1\).

For \(k\ge2\), rewrite (7) as
\[
r\le
\frac{11k}{3}+\frac{2k}{3(3k-1)}.
\]
The second term is strictly less than \(1/3\). Since the fractional part of \(11k/3\) is a multiple of \(1/3\), integrality gives
\[
r\le\left\lfloor\frac{11k}{3}\right\rfloor. \tag{11}
\]

When \(k=1\), Proposition 5 gives only \(r\le4\). We must exclude \(r=4\).

Suppose \(k=1\) and \(r=4\). The construction and Step 1 of the preceding proof remain valid: that step required only \(r\ge\alpha_k\), and \(\alpha_1=4\). We therefore have a node whose child-subtrees have size at most \(2\), a set \(B\) of size at most \(2\), and a \(B\)-normal set \(S\) of size at least \(3\).

No child-subtree can have size \(2\). Such a subtree has an incoming guard of size at most \(1\), so (1) would give
\[
4(2-1)\le e_D(U)\le2,
\]
which is impossible. Hence all strongly connected components contained in \(S\) are singletons.

Take a topological prefix \(A\subseteq S\) of three vertices. It is \(B\)-normal and induces an acyclic digraph, so \(e_D(A)\le3\). But (1) gives
\[
4(3-|B|)\le e_D(A)\le3,
\]
contradicting \(|B|\le2\).

Thus \(k=1\) implies \(r\le3\). Together with (11), this proves
\[
11k\ge3r
\]
in every case, and therefore
\[
\boxed{\operatorname{dtw}(D)\ge
\left\lceil\frac{3r}{11}\right\rceil.}
\]

---

## 6. Consequence for the optimal constant, and remaining gap

Under the simple loopless convention, define
\[
\varepsilon_*=
\inf_{r\ge1}
\inf_{\substack{D\text{ is}\\r\text{-regular}}}
\frac{\operatorname{dtw}(D)}r.
\]
The theorem proves
\[
\varepsilon_*\ge\frac3{11}.
\]

For the upper bound, the complete bidirected graph
\[
D=\overleftrightarrow K_{r+1}
\]
is \(r\)-regular and has a one-bag decomposition of width \(r\). In fact its directed tree-width is exactly \(r\), since Lemma 2 applied to its digon graph \(K_{r+1}\) gives the reverse inequality. Hence
\[
\varepsilon_*\le1.
\]

Thus the result established here is
\[
\boxed{\frac3{11}\le\varepsilon_*\le1.}
\]

**What remains unresolved:** there is no matching construction, and this argument does not even produce an \(r\)-regular digraph with directed tree-width strictly below \(r\). It is a lower-bound improvement, not a determination of the optimal constant.

Finally, simplicity is essential. With \(r\) parallel arcs in each direction between two vertices, the degree is \(r\) while directed tree-width is \(1\); under that multigraph convention no positive universal constant exists.