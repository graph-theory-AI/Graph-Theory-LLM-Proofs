```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Yes: the primitive case satisfies the stronger isomorphism-or-clique-image dichotomy, and the imprimitive cases have complete cores.",
  "would_publish": false,
  "caveats": "This is a self-contained exposition of the known resolution reported in the supplied catalog, not a claim of novelty."
}
```

# Statement and status

The answer is **yes**. The supplied catalog reports the affirmative resolution by Roberson. Below is a self-contained proof of the stronger homomorphism statement reported there, followed by the treatment of all imprimitive cases.

All graphs are finite and simple. A graph is a **core** if every endomorphism is an automorphism; the core of a graph is its unique, up to isomorphism, homomorphically equivalent core. A nontrivial strongly regular graph is **primitive** if both it and its complement are connected.

**Theorem.** Let \(G\) and \(H\) be primitive strongly regular graphs with the same parameters. Every homomorphism
\[
\varphi:G\longrightarrow H
\]
is either an isomorphism or has a clique as its image.

Taking \(H=G\) will settle the nontrivial part of the core question.

# 1. Connectivity of the non-neighbours

Write \((n,k,\lambda,\mu)\) for the parameters of \(G\). Primitivity implies
\[
0<\mu<k.
\]
Indeed, \(\mu=0\) forces each connected component to be a clique. If \(\mu=k\), nonadjacent vertices have identical neighbourhoods; nonadjacency, together with equality, then partitions the vertices into independent parts with every possible edge between different parts. Thus \(G\) would be complete multipartite.

We also have the standard counting identity
\[
k(k-\lambda-1)=(n-k-1)\mu>0. \tag{1}
\]

For a vertex \(v\), let
\[
W_v=V(G)\setminus\bigl(\{v\}\cup N(v)\bigr).
\]

**Lemma.** For every vertex \(v\) of a primitive strongly regular graph, \(G[W_v]\) is connected.

**Proof.** Suppose \(G[W_v]\) has at least two components. If \(x,y\) lie in different components, they are nonadjacent and every common neighbour of \(x,y\) lies in \(N(v)\). But
\[
|N(x)\cap N(v)|=|N(y)\cap N(v)|=\mu,
\]
and \(x,y\) have exactly \(\mu\) common neighbours. Consequently
\[
N(x)\cap N(v)=N(y)\cap N(v).
\]

Comparing vertices in different components shows that there is one fixed set \(S\subseteq N(v)\), of size \(\mu\), such that
\[
N(x)\cap N(v)=S\qquad\text{for every }x\in W_v.
\]

Since \(\mu<k\), choose \(t\in N(v)\setminus S\). The vertex \(t\) has no neighbours in \(W_v\). Its degree is \(k\), so it must be adjacent to all \(k\) other vertices of \(\{v\}\cup N(v)\). The adjacent pair \(v,t\) therefore has \(k-1\) common neighbours. This gives \(\lambda=k-1\), contradicting (1). \(\square\)

# 2. A spectral homomorphism matrix

Let \(A_G\) be the adjacency matrix of \(G\), and let \(J\) be the all-ones matrix. Strong regularity gives
\[
A_G^2=(k-\mu)I+(\lambda-\mu)A_G+\mu J.
\]
Thus the two restricted eigenvalues are the roots \(r,s\) of
\[
x^2-(\lambda-\mu)x-(k-\mu)=0,
\]
with
\[
r>0>s.
\]

Set
\[
c=\frac{k-r}{n}.
\]
The orthogonal projection onto the \(s\)-eigenspace is
\[
E_G=\frac{rI-A_G+cJ}{r-s}. \tag{2}
\]
Indeed, the right-hand side acts as zero on the all-ones vector and on the \(r\)-eigenspace, and as the identity on the \(s\)-eigenspace. In particular,
\[
E_G\succeq0,\qquad (A_G-sI)E_G=0.
\]

Define \(E_H\) analogously. Because \(G,H\) have the same parameters, their projection matrices have the same diagonal entry and the same entry on adjacent pairs.

Let \(P\) be the matrix of \(\varphi\):
\[
P_{u,x}=
\begin{cases}
1,&x=\varphi(u),\\
0,&\text{otherwise}.
\end{cases}
\]
The pullback
\[
F=PE_HP^{\mathsf T}
\]
is positive semidefinite. Since \(\varphi\) preserves edges, \(F\) agrees with \(E_G\) on the diagonal and on every adjacent pair of \(G\).

Now put
\[
B=A_G-sI.
\]
This is positive semidefinite because \(s\) is the least eigenvalue. Its entries are zero away from the diagonal and the edges. Hence
\[
\operatorname{tr}(BF)
=\operatorname{tr}(BE_G)
=0.
\]
For positive semidefinite matrices \(B,F\), trace zero implies \(BF=0\): this follows from
\[
\operatorname{tr}(BF)
=\left\|B^{1/2}F^{1/2}\right\|_{\mathrm F}^{2}.
\]
Therefore
\[
(A_G-sI)F=0.
\]

Define the symmetric matrix
\[
M=(r-s)(F-E_G).
\]
We have
\[
A_GM=sM. \tag{3}
\]

Because every row of \(P\) has exactly one \(1\), \(PJP^{\mathsf T}=J\). Expanding (2) gives
\[
M=r(PP^{\mathsf T}-I)-PA_HP^{\mathsf T}+A_G.
\]
Consequently \(M\) is zero on the diagonal and on edges of \(G\). For distinct nonadjacent \(u,v\), its entries are exactly
\[
M_{uv}=
\begin{cases}
r,&\varphi(u)=\varphi(v),\\
-1,&\varphi(u)\sim_H\varphi(v),\\
0,&\varphi(u)\ne\varphi(v)\text{ and }\varphi(u)\not\sim_H\varphi(v).
\end{cases} \tag{4}
\]

The signs in this table are the key point.

# 3. Propagation of the zero entries

Fix \(v\in V(G)\), and define
\[
Z_v=\{u\in W_v:M_{uv}=0\}.
\]

Suppose \(u\in Z_v\). By (4), \(\varphi(u)\) and \(\varphi(v)\) are distinct and nonadjacent. Therefore no neighbour \(w\) of \(u\) can satisfy
\[
\varphi(w)=\varphi(v),
\]
because \(\varphi\) preserves the edge \(uw\).

It follows from (4), including the zero entries on the diagonal and edges, that
\[
M_{wv}\le 0\qquad\text{for every }w\in N(u).
\]
On the other hand, (3) gives
\[
0=sM_{uv}=(A_GM)_{uv}
=\sum_{w\in N(u)}M_{wv}.
\]
Every summand is nonpositive, so every summand is zero.

In particular, there is no edge of \(G[W_v]\) between \(Z_v\) and \(W_v\setminus Z_v\). By the lemma,
\[
Z_v=\varnothing
\quad\text{or}\quad
Z_v=W_v.
\]

Thus every column of \(M\) has one of two forms:

* it is identically zero; or
* it is nonzero at every non-neighbour of its indexing vertex, and zero elsewhere.

Let
\[
T=\{v:M_{\cdot v}=0\}
\]
be the set of zero columns. If \(v\in T\) and \(u\) is nonadjacent to \(v\), then
\[
M_{vu}=M_{uv}=0.
\]
The column dichotomy applied to \(u\) forces \(u\in T\). Hence \(T\) is a union of connected components of \(\overline G\). Since \(\overline G\) is connected,
\[
T=V(G)\quad\text{or}\quad T=\varnothing.
\]

We now obtain the desired alternatives.

### Case 1: \(T=V(G)\)

Then \(M=0\). By (4), distinct nonadjacent vertices cannot be identified and must remain nonadjacent. Adjacent vertices also cannot be identified, because \(H\) has no loops.

Thus \(\varphi\) is injective and preserves both adjacency and nonadjacency. Since \(G,H\) have the same number of vertices, \(\varphi\) is an isomorphism.

### Case 2: \(T=\varnothing\)

Then
\[
M_{uv}\ne0
\qquad\text{whenever }u\ne v\text{ and }u\not\sim_Gv.
\]
By (4), every nonadjacent pair in \(G\) maps either to one vertex or to an adjacent pair in \(H\). Adjacent pairs already map to adjacent pairs.

It follows that every two distinct vertices in \(\varphi(V(G))\) are adjacent. Thus the image is a clique.

This proves the theorem. \(\square\)

# 4. Consequence for cores, including imprimitive graphs

Suppose first that \(G\) is primitive.

* If every endomorphism is an automorphism, then \(G\) is a core.
* Otherwise, the theorem supplies an endomorphism whose image is a clique \(K_t\). The homomorphism \(G\to K_t\) and the inclusion \(K_t\hookrightarrow G\) show that \(G\) and \(K_t\) are homomorphically equivalent. Since a complete graph is a core, the core of \(G\) is \(K_t\).

Moreover, such a clique-image endomorphism is an optimal coloring:
\[
\omega(G)\le \chi(G)\le t\le\omega(G),
\]
so
\[
t=\chi(G)=\omega(G).
\]

It remains to handle the nonprimitive and degenerate cases.

1. **Disconnected strongly regular graphs.**  
   Vertices in different components show that \(\mu=0\). A connected component cannot contain a nonadjacent pair at distance two, so every component is a clique. Regularity makes all components copies of \(K_{k+1}\). Mapping every component isomorphically onto one selected component is a retraction, and the core is \(K_{k+1}\).

2. **Graphs with disconnected complement.**  
   The complement of a strongly regular graph is strongly regular. By the preceding classification, it is a disjoint union of equally sized cliques. Thus \(G\) is complete multipartite. If it has \(t\) parts, choosing one representative from each part gives a retraction onto \(K_t\), which is its core.

3. **Degenerate cases.**  
   A complete graph is its own core. A nonempty edgeless graph has core \(K_1\). The zero-vertex graph, if admitted, is its own core.

Therefore every strongly regular graph has either itself or a complete graph as its core.

All primitive, imprimitive, and degenerate cases are covered. No conjectural input remains; the argument is an exposition of the already-known resolution rather than a new research contribution.