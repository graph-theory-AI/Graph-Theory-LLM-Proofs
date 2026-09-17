```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Finding a largest induced prism is W[1]-hard even when a valid larger prism-free promise is supplied, while minimal separators have small clique witnesses; neither result settles FPT MWIS.",
  "would_publish": false,
  "caveats": "The hardness concerns prism preprocessing, not MWIS; no novelty claim is made, and the exact Abrishami et al. result was not verified."
}
```

## 1. Interpretation and outcome

Let \(\mathsf{Pr}_k\) denote two \(k\)-cliques joined by exactly a perfect matching. The algorithmic question is whether MWIS on
\[
\mathcal C_k=\{G:G\text{ has no induced cycle of length at least five and no induced }\mathsf{Pr}_k\}
\]
admits a running time \(f(k)n^{O(1)}\), with polynomial dependence on the weight encoding.

I do not settle this question. I obtain two precise side results:

1. **Finding the largest prism is not an innocuous FPT preprocessing step:** it is W[1]-hard even on co-bipartite graphs supplied with a valid promise that they contain no \(\mathsf{Pr}_K\), parameterized by \(K\).
2. **Every nonempty minimal separator has a small clique witness:** in each full component it is dominated by a clique of size less than \(k\), with a corresponding induced prism certifying the witness size.

The second result supplies a genuinely bounded structural object, but I give a small example showing why it does not immediately supply boundedly many MWIS boundary states.

I set aside the previous attempt’s all-PMC enumeration approach. The shared co-bipartite/induced-matching observation is proved below; none of the argument relies on the previous PMC construction.

---

## 2. Co-bipartite graphs and prisms

A graph is **co-bipartite** if its vertices can be partitioned into two cliques \(A,B\). Let \(H\) be its bipartite graph of cross-edges:
\[
V(H)=A\cup B,\qquad E(H)=E(G)\cap(A\times B).
\]

Write \(\operatorname{im}(H)\) for the maximum size of an induced matching in \(H\).

### Lemma 1

Every co-bipartite graph is long-hole-free. Moreover, for every \(r\geq 3\),
\[
G\text{ contains an induced }\mathsf{Pr}_r
\quad\Longleftrightarrow\quad
\operatorname{im}(H)\geq r.
\]

#### Proof

An induced cycle of length at least five would have at least three vertices in one of \(A,B\). Three vertices in a clique cannot belong to an induced cycle of length at least four.

An induced matching of size \(r\) in \(H\), together with the clique edges in \(A\) and \(B\), gives an induced \(\mathsf{Pr}_r\).

Conversely, suppose \(G[U]\cong\mathsf{Pr}_r\), where \(r\geq3\). Every clique in \(\mathsf{Pr}_r\) has size at most \(r\), and a clique meeting both of its canonical wings has size at most two. Since \(A\cap U\) and \(B\cap U\) are cliques partitioning \(2r\) vertices, both have size \(r\). They must therefore be the two canonical wings. Their cross-edges form an induced matching in \(H\). ∎

---

## 3. Parameterized hardness of prism preprocessing

### Theorem 2

The following statements hold.

1. Detecting an induced \(\mathsf{Pr}_r\) is W[1]-complete parameterized by \(r\), even on co-bipartite graphs.
2. Suppose an algorithm is given a co-bipartite graph \(G\), an integer \(K\), and the **correct promise** that \(G\) is \(\mathsf{Pr}_K\)-free. Computing the largest induced prism in \(G\) is W[1]-hard parameterized by \(K\).

Thus the second hardness statement already applies to valid instances of the graph class in the question.

The proof is fully specified below. The parameterized benchmark is **Multicolored Clique**, with the number of colors as parameter.

### 3.1 A conflict graph encoding Multicolored Clique

Let the input graph have color classes
\[
V_1,\ldots,V_\ell,\qquad \ell\geq2.
\]
Put
\[
c=\binom{\ell}{2},\qquad m=\ell+c.
\]

Construct a graph \(F\) with \(m\) groups:

- \(X_i\) contains one candidate \(x_u\) for each \(u\in V_i\).
- \(Y_{ij}\), for \(i<j\), contains one candidate \(y_e\) for each input edge between \(V_i\) and \(V_j\).

Make every group a clique.

For an edge \(e=uv\), with \(u\in V_i\) and \(v\in V_j\), add the following cross-group conflicts:
\[
x_{u'}y_e\in E(F)\quad\Longleftrightarrow\quad u'\neq u,
\]
and
\[
x_{v'}y_e\in E(F)\quad\Longleftrightarrow\quad v'\neq v.
\]
There are no other cross-group edges.

Since each group is a clique,
\[
\alpha(F)\leq m.
\]
Furthermore,
\[
\alpha(F)=m
\quad\Longleftrightarrow\quad
\text{the input has a multicolored clique}. \tag{1}
\]

Indeed, an independent set of size \(m\) chooses one vertex candidate from each \(X_i\) and one edge candidate from each \(Y_{ij}\). Absence of conflicts forces every selected edge to join the selected vertices of its two colors. The converse is immediate.

Empty groups cause no problem: then \(\alpha(F)<m\), as required.

### 3.2 An elementary matching bound

We use the following observation.

### Lemma 3

Let a bipartite graph have label maps on its two sides, and suppose every pair with unequal labels is an edge. Equal-label pairs may or may not be edges.

An induced matching contains at most two edges whose endpoints have unequal labels.

#### Proof

Suppose three such edges are \(a_i b_i\), \(i=1,2,3\). Write their labels as \(\lambda_i,\mu_i\), respectively.

For \(i\neq j\), the absence of \(a_i b_j\) implies
\[
\lambda_i=\mu_j.
\]
Thus
\[
\lambda_1=\mu_2=\mu_3,\qquad
\lambda_2=\mu_1=\mu_3.
\]
Consequently \(\lambda_1=\mu_1\), contradicting that \(a_1b_1\) has unequal endpoint labels. ∎

### 3.3 Amplifying the intended matching edges

Set
\[
\beta=2(m+4c),\qquad t=\beta+1.
\]

Construct a bipartite graph \(H\) with parts
\[
A=\{a_{z,h}:z\in V(F),\ h\in[t]\},
\qquad
B=\{b_{z,h}:z\in V(F),\ h\in[t]\}.
\]

Its edges are:

- **Identity edges**
  \[
  a_{z,h}b_{z,h}
  \quad(z\in V(F),\ h\in[t]).
  \]
- **Conflict edges:** for every \(zw\in E(F)\), add all edges between
  \[
  \{a_{z,h}:h\in[t]\}\quad\text{and}\quad
  \{b_{w,h}:h\in[t]\},
  \]
  and also all edges in the reverse ordered block.

There are no other edges.

I claim that
\[
t\alpha(F)\leq \operatorname{im}(H)\leq t\alpha(F)+\beta. \tag{2}
\]

For the lower bound, take an independent set \(I\) in \(F\) and select all \(t\) identity edges for each \(z\in I\). These form an induced matching.

For the upper bound, let \(M\) be any induced matching in \(H\).

**Identity edges.** The candidates \(z\) whose identity edges occur in \(M\) form an independent set in \(F\): two conflicting candidates would create cross-edges between their selected identity edges. Hence \(M\) contains at most \(t\alpha(F)\) identity edges.

**Conflict edges.** Partition these according to the ordered pair of candidate groups containing their endpoints. There are at most

- \(m\) diagonal group blocks; and
- \(4c\) ordered incidence blocks, since each \(Y_{ij}\) interacts with \(X_i\) and \(X_j\), in both directions.

Each block contributes at most two conflict edges to \(M\):

- In a diagonal block, label vertices by their underlying candidate \(z\). Different candidates conflict, so Lemma 3 applies.
- In an \(X_i,Y_{ij}\) block, label an \(X_i\)-candidate by its input vertex, and a \(Y_{ij}\)-candidate by its endpoint in \(V_i\). Conflict means precisely unequal labels. Lemma 3 again applies. The reverse block is identical.

Thus the number of conflict edges in \(M\) is at most
\[
2(m+4c)=\beta.
\]
This proves (2).

### 3.4 The detection threshold and a valid larger promise

Define
\[
R=tm,\qquad K=t(m+1).
\]

If the Multicolored Clique instance is positive, (1) and (2) give
\[
\operatorname{im}(H)\geq tm=R.
\]

If it is negative, then \(\alpha(F)\leq m-1\), and
\[
\operatorname{im}(H)
 \leq t(m-1)+\beta
 =tm-1
 =R-1.
\]

Moreover, **for every input**, positive or negative,
\[
\operatorname{im}(H)
 \leq tm+\beta
 =t(m+1)-1
 =K-1. \tag{3}
\]

Now obtain \(G\) by making both \(A\) and \(B\) cliques. Lemma 1 gives
\[
G\text{ contains }\mathsf{Pr}_R
\quad\Longleftrightarrow\quad
\text{the input has a multicolored clique},
\]
while (3) guarantees that \(G\) is \(\mathsf{Pr}_K\)-free.

The graph \(G\) is automatically long-hole-free. Also,
\[
R,K=O(\ell^4),
\]
and the construction has size polynomial in the input size and \(\ell\). This is a parameterized reduction.

It proves W[1]-hardness of \(\mathsf{Pr}_R\)-detection. More strongly, an FPT algorithm computing the largest prism under the correct \(\mathsf{Pr}_K\)-free promise could be applied to \((G,K)\); comparing its answer with \(R\) would solve Multicolored Clique in FPT time.

### 3.5 Membership in W[1]

For completeness, induced \(\mathsf{Pr}_r\)-detection reduces to Multicolored Clique.

Create one color class for each of the \(2r\) pattern vertices, containing a copy of every vertex of \(G\). Two copies in different classes are adjacent exactly when:

1. they represent distinct vertices of \(G\); and
2. their adjacency or nonadjacency in \(G\) agrees with that of the corresponding pattern vertices.

A multicolored clique selects precisely an induced embedding of \(\mathsf{Pr}_r\). The new parameter is \(2r\). This completes the proof of Theorem 2. ∎

### Why this is not MWIS hardness

Every graph produced above is co-bipartite, so every independent set has size at most two. For arbitrary vertex weights,
\[
\alpha_w(G)=
\max\left\{
0,\ 
\max_{v\in V(G)}w(v),\
\max_{\substack{a\in A,\ b\in B\\ab\notin E(G)}}
\bigl(w(a)+w(b)\bigr)
\right\}.
\]
This is computable in \(O(n^2)\) arithmetic/comparison operations.

Therefore the reduction makes prism preprocessing hard **while leaving MWIS easy**. It rules out an exact maximum-prism preprocessing strategy under the usual assumption \(\mathrm{FPT}\neq\mathrm{W[1]}\), not an FPT MWIS algorithm.

---

## 4. A bounded clique witness for every minimal separator

Here is a positive structural fact relevant to the original class.

For a separator \(S\), a component \(C\) of \(G-S\) is **full** if \(N(C)=S\). A minimal separator has at least two full components.

### Theorem 4

Let \(G\) be long-hole-free, let \(S\neq\varnothing\) be a minimal separator, and let \(C\) be any full component of \(G-S\).

There exist cliques
\[
X\subseteq C,\qquad Y\subseteq S
\]
such that:

1. \(X\) dominates \(S\);
2. \(|X|=|Y|\); and
3. the edges between \(X\) and \(Y\) are exactly a perfect matching.

Consequently, if \(G\) is \(\mathsf{Pr}_k\)-free, then \(X\) can be chosen with
\[
|X|\leq k-1.
\]

Given \(S\) and \(C\), such an \(X\) can be found in polynomial time.

#### Proof

Choose another full component \(D\neq C\).

Start with \(T=C\), and repeatedly delete a vertex whenever the remaining set stays connected and continues to dominate \(S\). Let \(T\) be the resulting set.

If \(T\) is a singleton, the conclusion follows by taking any one of its neighbors in \(S\). Assume \(|T|\geq2\).

For every non-cutvertex \(v\) of \(G[T]\), there is a private neighbor \(s_v\in S\) with
\[
N(s_v)\cap T=\{v\};
\]
otherwise \(v\) could have been deleted. Private neighbors for distinct vertices are distinct.

Take distinct non-cutvertices \(v,w\) of \(G[T]\), and a shortest \(v\)-\(w\) path \(P\) in \(G[T]\).

First, \(s_v\) and \(s_w\) must be adjacent. If not, take a shortest \(s_v\)-\(s_w\) path whose interior lies in \(D\). Together with
\[
s_v-v-P-w-s_w,
\]
it forms an induced cycle of length at least five. There are no edges between \(C\) and \(D\), and the private-neighbor conditions prevent chords into \(P\).

Second, \(v\) and \(w\) must be adjacent. Otherwise \(P\) has length at least two, and
\[
s_v-v-P-w-s_w-s_v
\]
is an induced cycle of length at least five.

Thus the non-cutvertices of \(G[T]\) form a clique.

A connected graph whose non-cutvertices form a clique has no cutvertex. Indeed, if \(z\) were a cutvertex, each of two different components of \(G[T]-z\) would contain a leaf of a spanning tree of \(G[T]\). Such leaves are non-cutvertices of \(G[T]\), but vertices in different components are nonadjacent. This is a contradiction.

Therefore every vertex of \(T\) is a non-cutvertex, and \(T\) itself is a clique. Set
\[
X=T,\qquad Y=\{s_v:v\in T\}.
\]
The preceding argument also shows that \(Y\) is a clique. By the private-neighbor property, the cross-edges between \(X\) and \(Y\) are exactly \(vs_v\).

Hence \(G[X\cup Y]\cong\mathsf{Pr}_{|X|}\). If \(|X|\geq k\), selecting \(k\) matched pairs gives an induced \(\mathsf{Pr}_k\), proving the bound.

The deletion procedure uses polynomially many connectivity and domination tests, so it is polynomial-time. ∎

### Corollary 5

With \(X\) as above, every independent set \(I\subseteq S\) is dominated by a single vertex of \(X\).

#### Proof

For nonadjacent \(s,t\in S\), the nonempty sets \(N_X(s)\) and \(N_X(t)\) are comparable by inclusion.

Otherwise choose
\[
x\in N_X(s)\setminus N_X(t),\qquad
y\in N_X(t)\setminus N_X(s).
\]
Since \(X\) is a clique, \(s-x-y-t\) is an induced path. Closing it through the full component \(D\) gives a long hole.

Thus the neighborhoods \(N_X(s)\), \(s\in I\), form a chain of nonempty sets. Their smallest member contains a vertex adjacent to all of \(I\). ∎

---

## 5. Why the clique witness is not an MWIS boundary state

The preceding corollary suggests trying to represent \(I\cap S\) merely by a vertex of \(X\) dominating it. This loses essential information, even when \(|X|=1\).

Consider the five-vertex graph with vertices
\[
\{s,t,x,y,z\}
\]
and edges
\[
sx,\ tx,\ xy,\ sy,\ sz,\ tz.
\]
It is long-hole-free: the only possible long hole would use all five vertices, but their induced graph is not a \(C_5\). It is also \(\mathsf{Pr}_3\)-free because it has only five vertices.

The set
\[
S=\{s,t\}
\]
is a minimal separator with full components
\[
C=\{x,y\},\qquad D=\{z\}.
\]
The singleton \(X=\{x\}\) dominates \(S\).

Both independent boundary choices \(\{s\}\) and \(\{t\}\) have the same dominating witness \(x\). Nevertheless:

- choosing \(s\) forbids both \(x\) and \(y\) in \(C\);
- choosing \(t\) forbids \(x\), but allows \(y\).

With \(w(y)=1\), their optimum contributions from \(C\) differ. Hence the dominating witness alone is not an exact dynamic-programming state.

This does not rule out a more sophisticated state compression. It identifies the missing step in this particular structural approach.

---

## 6. What remains unresolved

The results establish two constraints on a possible FPT proof:

- It cannot simply assume that an exact largest-prism computation is an available FPT preprocessing primitive—even under a valid larger prism-free promise.
- The small clique witnesses for separators do not, by themselves, compress all MWIS boundary interactions into fewer than \(k\) states.

Neither constraint excludes an FPT MWIS algorithm. Such an algorithm might avoid maximum-prism computation, construct a different decomposition, or retain richer but still FPT-sized boundary information.

Finally, the excerpt does not specify the theorem denoted by Abrishami et al. [1]. I have not verified its statement or algorithmic consequences, so I do not infer from the parenthetical remark whether the existential FPT question is already answered using that result. The mathematical progress above is independent of that literature-status issue.