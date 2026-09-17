Attack the following open graph-theory problem.

Catalog id: algorithm_for_graph_homomorphisms
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/algorithm_for_graph_homomorphisms/
Original entry: http://www.openproblemgarden.org/op/algorithm_for_graph_homomorphisms
Problem attributed to: Fomin, Fedor V., Heggernes, Pinar, Kratsch, Dieter (posted 2010-07-08)

=== Problem statement (OpenProblemGarden) ===
Title: Algorithm for graph homomorphisms
Question Is there an algorithm that decides, for input graphs $ G $ and $ H $ , whether there exists a homomorphism from $ G $ to $ H $ in time $ O(c^{|V(G)|+|V(H)|}) $ for some constant $ c $ ?

=== Discussion / context (OpenProblemGarden) ===
An affirmative answer is known in several cases: if $ H=K_k $ (graph coloring) [L], [BH], [K]; if $ H $ has bounded treewidth [FHK]; if $ H $ has bounded cliquewidth [W].

=== References listed by OpenProblemGarden ===
- [BH] Andreas Björklund, Thore Husfeldt: Inclusion--Exclusion Algorithms for Counting Set Partitions, Proc. FOCS'06 (2006).
- *[FHK] Fedor V. Fomin, Pinar Heggernes, Dieter Kratsch: Exact Algorithms for Graph Homomorphisms, Theory Comput. Syst. 41 (2007), no. 2, 381--393. MathSciNet
- [K] Mikko Koivisto: An Algorithm for Graph Coloring and Other Partitioning Problems via Inclusion--Exclusion, Proc. FOCS'06 (2006).
- [L] Eugene L. Lawler: A note on the complexity of the chromatic number problem, Information Processing Lett. 5 (1976), no. 3, 66--67. MathSciNet
- [W] Magnus Wahlström: New Plain-Exponential Time Classs for Graph Homomorphism, CSR2009, LNCS5675 (2009), 346--355.

=== Catalog page (statement + literature review) ===
Algorithm for graph homomorphisms — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The original question of whether there is an algorithm deciding the existence of a homomorphism from $G$ to $H$ in time $O(c^{|V(G)|+|V(H)|})$ for some absolute constant $c$ remains open in full generality. Since 2010, several works have extended the list of graph classes admitting such plain-exponential algorithms (e.g., Wahlstrom-type results were generalized by Dadsetan and Bulatov to further classes for the counting version, and Rzazewski gave an $O^{*}((b+2)^{|V(G)|})$ algorithm parametrized by the bandwidth of the complement of $H$), and Fomin, Golovnev, Kulikov, and Mihajlin proved an ETH lower bound of $2^{\Omega(n \log h / \log\log h)}$ for the general problem, which however does not rule out a $c^{n+h}$ algorithm.

 Cited literature (4)

 
 
 
partial Lower Bounds for the Graph Homomorphism Problem
 (2015)
 

 
 Fedor V. Fomin, Alexander Golovnev, Alexander S. Kulikov, Ivan Mihajlin · ICALP 2015 / arXiv preprint · arXiv:1502.05447 · doi:10.1007/978-3-662-47672-7_39

Proves an ETH-based lower bound of $2^{\Omega(n \log h / \log\log h)}$ for deciding graph homomorphism, ruling out single-exponential-in-$n\log h$ algorithms but not a $c^{|V(G)|+|V(H)|}$ algorithm.
 

 
 
partial Exact Algorithm for Graph Homomorphism and Locally Injective Graph Homomorphism
 (2014)
 

 
 Pawel Rzazewski · Information Processing Letters / arXiv preprint · arXiv:1310.3341 · doi:10.1016/j.ipl.2014.02.012

Gives an exact algorithm for graph homomorphism running in time $O^{*}((b+2)^{|V(G)|})$, where $b$ is the bandwidth of the complement of $H$, expanding the list of classes for which the problem is solvable in plain-exponential time.
 

 
 
partial Counting homomorphisms in plain exponential time
 (2018)
 

 
 Amineh Dadsetan, Andrei A. Bulatov · arXiv preprint · arXiv:1810.03087

Generalizes Wahlstrom's result for counting graph homomorphisms in time $k^{|V(G)|+|V(H)|}\cdot\mathrm{poly}$ from bounded clique-width to additional classes of target graphs $H$, enlarging the known cases of plain-exponential algorithms.
 

 
 
partial The Fine-Grained Complexity of Graph Homomorphism Parameterized by Clique-Width
 (2022)
 

 
 Robert Ganian, Thekla Hamm, Viktoriia Korchemna, Karolina Okrasa, Kirill Simonov · ICALP 2022 / arXiv preprint · arXiv:2210.06845 · doi:10.4230/LIPIcs.ICALP.2022.66

Provides a fine-grained classification of the homomorphism problem in time $O^{*}(s(H)^{cw})$ with matching SETH-based lower bounds, refining the picture for restricted target graphs $H$ (clique-width-parametrized) but leaving the general $c^{|V(G)|+|V(H)|}$ question open.
 

 

 Reviewer notes. The original question concerns the decision version with constant base $c$ independent of $G,H$. The 2015 ETH lower bound of $2^{\Omega(n \log h / \log\log h)}$ does NOT rule out a $c^{|V(G)|+|V(H)|}$ algorithm (e.g., when $h \gg n$, $c^{n+h}$ can exceed the lower bound). All cited papers extend the known classes of $H$ for which plain-exponential algorithms exist, or give lower bounds for restricted parameterizations, but none affirmatively or negatively resolves the original FHK question. The exact published year/venue of arXiv:1810.03087 was not verified beyond the preprint.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Question. Is there an algorithm that decides, for input graphs $ G $ and $ H $ , whether there exists a homomorphism from $ G $ to $ H $ in time $ O(c^{|V(G)|+|V(H)|}) $ for some constant $ c $ ?

Keywords:
algorithm · Exponential-time algorithm · homomorphism

Discussion

An affirmative answer is known in several cases: if $ H=K_k $ (graph coloring) [L], [BH], [K]; if $ H $ has bounded treewidth [FHK]; if $ H $ has bounded cliquewidth [W].

Bibliography

 [BH]
 Andreas Björklund, Thore Husfeldt: Inclusion--Exclusion Algorithms for Counting Set Partitions, Proc. FOCS'06 (2006).

★ [FHK]
 Fedor V. Fomin, Pinar Heggernes, Dieter Kratsch: Exact Algorithms for Graph Homomorphisms, Theory Comput. Syst. 41 (2007), no. 2, 381--393. MathSciNet
 MathSciNet

 [K]
 Mikko Koivisto: An $ O^\ast(2^n) $ Algorithm for Graph Coloring and Other Partitioning Problems via Inclusion--Exclusion, Proc. FOCS'06 (2006).

 [L]
 Eugene L. Lawler: A note on the complexity of the chromatic number problem, Information Processing Lett. 5 (1976), no. 3, 66--67. MathSciNet
 MathSciNet

 [W]
 Magnus Wahlström: New Plain-Exponential Time Classs for Graph Homomorphism, CSR2009, LNCS5675 (2009), 346--355.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sublinear-vertex reduction from bounded-degree 3-coloring to balanced homomorphism instances gives an ETH obstruction to the proposed running time.",
  "would_publish": false,
  "caveats": "This is not an unconditional nonexistence proof, and no novelty is claimed for the lower-bound conclusion; the catalog's dismissal of the ETH obstruction is misleading."
}
```

# A balanced-instance obstruction

There is an important problem with the supplied review: the regime \(h\gg n\) does not protect an algorithm required to work for **every** pair of graphs. An ETH obstruction can already occur when \(h=n\).

I will not assume missing quantifiers in the catalog’s summary of the literature. Instead, I give a self-contained reduction establishing a weaker, but sufficient, obstruction.

All graphs below are finite, simple, undirected, and loopless.

## 1. Unconditional partial result

**Theorem.** There is a polynomial-time reduction taking an \(N\)-vertex graph \(X\) of maximum degree at most \(5\) to graphs \(G_X,H_X\) such that
\[
X\text{ is 3-colorable}\quad\Longleftrightarrow\quad G_X\longrightarrow H_X,
\]
and
\[
|V(G_X)|=|V(H_X)|
=O\!\left(\frac{N}{\sqrt{\log\log N}}\right).
\]

Consequently, an algorithm as in the question would give a
\[
2^{O(N/\sqrt{\log\log N})}=2^{o(N)}
\]
algorithm for bounded-degree 3-coloring. A linear-size reduction given below then yields a \(2^{o(v+m)}\)-time algorithm for 3-SAT with \(v\) variables and \(m\) clauses.

The theorem is unconditional. Invoking sparse ETH gives the conditional conclusion that the requested algorithm does not exist—even when the two input graphs have equal orders.

## 2. Grouping into a small-target list-homomorphism instance

A **list homomorphism** from \(P\) to \(R\), with lists \(\mathcal L(x)\subseteq V(R)\), is a homomorphism \(f:P\to R\) satisfying \(f(x)\in\mathcal L(x)\) for every \(x\).

Fix a constant degree bound \(\Delta\), eventually \(\Delta=5\), and an integer \(r\geq1\).

Partition \(V(X)\) arbitrarily into
\[
q=\lceil N/r\rceil
\]
nonempty buckets of size at most \(r\). Number the vertices within each bucket by distinct elements of \([r]\). Let \(Q\) be the quotient graph: two different buckets are adjacent when an edge of \(X\) joins them.

Since \(\Delta(Q)\leq \Delta r\), the square \(Q^2\) can be greedily colored with
\[
L=(\Delta r)^2+1
\]
colors. Write \(\lambda_B\in[L]\) for the label of bucket \(B\). In particular, the neighbors of any bucket have pairwise distinct labels.

For each bucket \(B\), record its external-edge description
\[
E_B\subseteq [r]\times[L]\times[r].
\]
A triple \((i,\mu,j)\) belongs to \(E_B\) precisely when the vertex in position \(i\) of \(B\) is adjacent in \(X\) to the vertex in position \(j\) of a neighboring bucket labeled \(\mu\). This description is unambiguous because neighboring buckets have distinct labels. Also,
\[
|E_B|\leq\Delta r.
\]

Construct a universal target \(R=R_{r,\Delta}\). Its vertices are all triples
\[
(\lambda,a,E),
\]
where
\[
\lambda\in[L],\qquad a\in[3]^r,\qquad
E\subseteq[r]\times[L]\times[r],\quad |E|\leq\Delta r.
\]

Two such vertices \((\lambda,a,E)\) and \((\mu,b,F)\) are adjacent exactly when \(\lambda\neq\mu\) and both conditions hold:
\[
a_i\neq b_j \quad\text{for every }(i,\mu,j)\in E,
\]
\[
b_j\neq a_i \quad\text{for every }(j,\lambda,i)\in F.
\]
This defines a simple undirected graph.

Give bucket \(B\) the list consisting of all
\[
(\lambda_B,a,E_B)
\]
for which \(a\), restricted to the occupied positions of \(B\), properly 3-colors \(X[B]\).

Then
\[
X\text{ is 3-colorable}
\quad\Longleftrightarrow\quad
(Q,R,\mathcal L)\text{ has a list homomorphism}.
\]

Indeed, a coloring supplies the vector for each bucket, and every quotient edge tests exactly the original edges between its two buckets. Conversely, list membership handles internal edges, while target adjacency handles external edges.

The number \(h=|V(R)|\) satisfies
\[
\begin{aligned}
h
&=
L\,3^r\sum_{j=0}^{\Delta r}
 \binom{r^2L}{j}\\
&\leq
L\,3^r(\Delta r+1)(r^2L)^{\Delta r}\\
&=2^{O(r\log(r+2))},
\end{aligned}
\]
where the constant depends only on \(\Delta\).

Thus grouping reduces the source order to \(\lceil N/r\rceil\), while the target order depends only on \(r\).

## 3. Removing lists with overhead depending only on the target

The following elementary gadget suffices. Its exponential dependence on \(h\) is intentionally not optimized.

**Lemma.** Given a list-homomorphism instance \((P,R,\mathcal L)\), where \(|V(R)|=h\geq1\), one can explicitly construct an equivalent ordinary homomorphism instance \((S,T)\) with
\[
|V(S)|=|V(P)|+O(32^h),
\qquad
|V(T)|=O(32^h).
\]
Moreover, \(S\) has no isolated vertices.

### 3.1 An explicit anchor graph

We need a triangle-free, vertex-critical \(k\)-chromatic graph \(A\): thus
\[
\chi(A)=k,\qquad \chi(A-v)\leq k-1
\quad\text{for every }v\in V(A).
\]

Such graphs are obtained explicitly by iterating the Mycielski construction starting with \(K_2\). For completeness, if \(F\) has vertices \(v_i\), its Mycielski graph has:

- the original vertices \(v_i\), inducing \(F\);
- independent shadow vertices \(u_i\), where \(u_i v_j\) is an edge whenever \(v_i v_j\in E(F)\);
- an apex adjacent to every \(u_i\).

Triangle-freeness is preserved. If \(\chi(F)=k\), the new graph has chromatic number \(k+1\): in a hypothetical \(k\)-coloring, take the apex color to be \(k\), and recolor every original vertex of color \(k\) with its shadow’s color. This would \((k-1)\)-color \(F\).

Vertex-criticality is also preserved:

- after deleting the apex, color each shadow like its original;
- after deleting \(u_i\), \((k-1)\)-color \(F-v_i\), give \(v_i\) and the apex color \(k\), and let the remaining shadows inherit their originals’ colors;
- after deleting \(v_i\), \((k-1)\)-color \(F-v_i\), give all shadows color \(k\), and give the apex color \(1\).

Hence the resulting \(k\)-chromatic anchor has
\[
|V(A)|=3\cdot 2^{k-2}-1.
\]

### 3.2 Construction

Set
\[
M=2h+1,\qquad k=5h+4,
\]
and take the anchor \(A\) just described. Choose an edge \(\alpha\beta\) of \(A\), and additional distinct vertices
\[
p_1,\ldots,p_{M-1},z.
\]
There are enough vertices since \(|V(A)|\geq k>M+2\).

Define nested sets
\[
D_i=\{\alpha,\beta,p_1,\ldots,p_{i-1}\},
\qquad 1\leq i\leq M.
\]
Thus \(|D_i|=i+1\), and \(z\notin D_M\).

Number \(V(R)=\{y_1,\ldots,y_h\}\).

The target \(T\) contains:

1. a copy of \(A\);
2. a marker clique \(q_1,\ldots,q_M\);
3. a copy of \(R\).

Add the following cross edges:

- \(q_i\) is adjacent to exactly \(D_i\) in \(A\);
- every \(y_j\) is adjacent to \(\alpha,\beta,z\);
- \(q_i y_j\) is an edge exactly when \(1\leq i\leq h\) and \(i\neq j\).

The source \(S\) contains copies of \(A\), the same marker clique with the same anchor neighborhoods, and \(P\). For each \(x\in V(P)\):

- join \(x\) to \(\alpha,\beta,z\);
- join \(x\) to \(q_i\) for every \(i\in[h]\setminus\mathcal L(x)\).

There are no other cross edges.

A list homomorphism extends to \(S\to T\) by fixing the anchor and markers. We prove the converse.

### 3.3 Every homomorphism fixes the marker roles

First consider the restriction of a homomorphism \(f:S\to T\) to \(A\).

There are
\[
t=M+h=3h+1
\]
vertices outside \(A\) in \(T\), each with at most
\[
d=M+1=2h+2
\]
neighbors in \(A\). For every \(v\in V(A)\), a \((k-1)\)-coloring of \(A-v\) extends greedily to \(T-v\): when coloring an outside vertex, at most
\[
d+t-1=5h+2=k-2
\]
colors are forbidden. Consequently,
\[
\chi(T-v)\leq k-1.
\]

Because \(\chi(A)=k\), the image \(f(A)\) cannot omit any vertex of the target copy of \(A\). Cardinality therefore forces \(f|_A\) to be an automorphism \(\sigma\) of \(A\).

Each source marker is adjacent to \(\alpha,\beta\). Since \(A\) is triangle-free, its image cannot belong to \(A\). The markers consequently map injectively to an \(M\)-clique outside \(A\).

The only such clique is the marker clique. Indeed, a clique containing a vertex of \(R\) contains at most \(h\) vertices of \(R\) and at most \(h-1\) markers, hence has size at most
\[
2h-1<M.
\]

Thus \(f(q_i)=q_{\pi(i)}\) for a permutation \(\pi\) of \([M]\). The anchor edges imply
\[
\sigma(D_i)\subseteq D_{\pi(i)}.
\]
Taking cardinalities gives \(i\leq\pi(i)\) for every \(i\), which forces \(\pi\) to be the identity. In particular,
\[
\sigma(D_M)=D_M.
\]

### 3.4 Every data vertex respects its list

Let \(x\in V(P)\).

Its adjacency to \(\alpha,\beta\) prevents \(f(x)\) from lying in \(A\). Also,
\[
\sigma(z)\notin D_M,
\]
whereas every marker has its anchor neighborhood contained in \(D_M\). The edge \(xz\) therefore prevents \(f(x)\) from being a marker.

Hence \(f(x)\in V(R)\). If \(f(x)=y_j\), its adjacency to every forbidden marker \(q_i\), \(i\notin\mathcal L(x)\), implies \(j\neq i\). Thus
\[
j\in\mathcal L(x).
\]
The restriction to \(P\) is the required list homomorphism.

Finally,
\[
|V(A)|=3\cdot2^{5h+2}-1=12\cdot32^h-1,
\]
which proves the size bounds. Every source vertex has positive degree. This proves the lemma.

## 4. Choosing the parameters and balancing the orders

Apply the grouping construction with \(\Delta=5\) and, for sufficiently large \(N\),
\[
r=\left\lfloor\sqrt{\log_2\log_2 N}\right\rfloor.
\]
Then
\[
\log h=O(r\log(r+2))=o(\log\log N),
\]
so
\[
h=(\log N)^{o(1)}
\quad\text{and}\quad
32^h=N^{o(1)}.
\]

After removing lists, the two orders are
\[
|V(S)|=\lceil N/r\rceil+M+|V(A)|,
\]
\[
|V(T)|=h+M+|V(A)|.
\]
In particular,
\[
|V(S)|=O(N/r).
\]

For sufficiently large \(N\), \(\lceil N/r\rceil\geq h\). Add
\[
\lceil N/r\rceil-h
\]
isolated vertices to \(T\). This preserves the homomorphism answer because \(S\) has no isolated vertices: no source vertex can map to an isolated target vertex.

The resulting graphs have equal order
\[
O(N/r)
=
O\!\left(\frac{N}{\sqrt{\log\log N}}\right).
\]

All constructions are polynomial-time in \(N\):

- the target configurations are explicitly enumerated;
- each bucket has at most \(3^r\) list entries;
- the anchor is explicitly constructed and has \(N^{o(1)}\) vertices;
- all graph assembly takes polynomial time.

The finitely many exceptional small sizes can be handled directly, outputting \(K_2\to K_2\) for a yes-instance and \(K_2\to\overline{K_2}\) for a no-instance.

This completes the proof of the compression theorem.

## 5. Why this gives a sparse-3-SAT obstruction

Here is the required linear-size connection, without relying on a bounded-degree coloring hardness citation.

### From 3-SAT to ordinary 3-coloring

For each clause \(a\lor b\lor c\), introduce a fresh Boolean variable \(s\) and replace the clause by
\[
\operatorname{NAE}(a,b,s)
\quad\land\quad
\operatorname{NAE}(\neg s,c,F),
\]
where \(F\) is the constant false. An assignment to \(a,b,c\) extends to these two constraints exactly when at least one of \(a,b,c\) is true.

Use a palette triangle with vertices \(T,F,B\). For each Boolean variable, introduce two adjacent literal vertices, both adjacent to \(B\); they must receive the colors \(T,F\) in opposite orders.

For a constraint \(\operatorname{NAE}(\ell_1,\ell_2,\ell_3)\), introduce a fresh triangle \(z_1z_2z_3\), joining \(z_i\) to \(\ell_i\). This triangle can be colored exactly when the three literal colors are not all equal:

- if they are equal, every \(z_i\) has the same forbidden color, leaving only two colors for a triangle;
- otherwise, give one suitable \(z_i\) color \(T\), another color \(F\), and the remaining one color \(B\).

This produces a graph with \(O(v+m)\) vertices and edges.

### Reducing the maximum degree to five

For a vertex of degree \(d\geq1\), create \(d\) clones, one for each incident edge. Join each consecutive pair of clones by an equality gadget: two adjacent new vertices, each adjacent to both clones.

In every 3-coloring, the two clones must have the same color. Conversely, equal clone colors extend across the gadget. Chaining these gadgets forces all clones of the original vertex to agree.

Each clone has one original-edge incidence and belongs to at most two equality gadgets, so its degree is at most
\[
1+2+2=5.
\]
The auxiliary vertices have degree three. The size increase is linear in the original number of vertices and edges.

Thus 3-SAT reduces to maximum-degree-five 3-coloring with \(O(v+m)\) vertices.

Combining this with the compression theorem shows:

\[
\boxed{
\text{An }O(c^{|V(G)|+|V(H)|})\text{ homomorphism algorithm}
\ \Longrightarrow\
\text{a }2^{o(v+m)}\text{ algorithm for 3-SAT}.
}
\]

For \(m=O(v)\), this contradicts the usual sparse formulation of ETH.

## 6. What this does and does not settle

The reduction is an unconditional result. The conclusion that the requested algorithm **does not exist** remains conditional on ETH; I am not treating ETH as proved, and therefore do not label the original question “disproved.”

Nevertheless, the catalog’s explanation is misleading. Our hard instances satisfy
\[
|V(G)|=|V(H)|=n,
\]
so the proposed running time is simply \(2^{O(n)}\). The possibility that \(c^{n+h}\) is large in some other regime, such as \(h\gg n\), is irrelevant.

Likewise, a lower bound excluding
\[
2^{o(n\log h/\log\log h)}
\]
on a range including \(h=n\) would exclude the proposed algorithm, because
\[
2^{O(n)}
=
2^{o(n\log n/\log\log n)}.
\]
One must check the theorem’s parameter range, not dismiss it by considering a different range.

**Bottom line:** there is a rigorous ETH obstruction already on balanced instances. This is a precise complexity-theoretic partial answer, but not an unconditional resolution of the existence question.
