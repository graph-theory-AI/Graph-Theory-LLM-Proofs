```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The biclique-free converse holds with a sharper extraction bound, while no fixed finite family of transductions suffices to test bounded merge-width, even on 2-degenerate C4-free classes.",
  "would_publish": false,
  "caveats": "The unrestricted dense case remains unresolved; standard monadic one-dimensional transductions are assumed; novelty has not been literature-checked."
}
```

# Partial results

I do not resolve the unrestricted conjecture. I rechecked the supplied attempt’s biclique-free approach and retain it below, with an improved extraction argument: instead of counting repetitions of noisy traces, one can extract **exact incidence graphs**.

I also prove an additional limitation theorem: **no finite collection of FO transductions can replace the universal quantifier over transductions**, even for \(2\)-degenerate \(C_4\)-free classes.

No result from the reported 2026 follow-up is used.

## 1. Conventions and the positive result

All graphs are finite, simple, and undirected. Write
\[
\nu_G(A)=\bigl|\{N_G(v)\cap A:v\in V(G)\}\bigr|.
\]
A class has linear neighbourhood complexity if there is a constant \(c\) such that
\[
\nu_G(A)\le c|A|
\]
for every graph in the class and every nonempty vertex set \(A\).

Transductions are monadic, one-dimensional FO transductions: finitely many arbitrary unary predicates may be added, and finitely many copies are allowed. The positive result below uses no copying.

### Theorem 1
Let \(t\ge2\), and let \(\mathcal C\) be a class excluding \(K_{t,t}\) as a **subgraph**, not merely as an induced subgraph. If every FO transduction of \(\mathcal C\) has linear neighbourhood complexity, then \(\mathcal C\) has bounded expansion.

Consequently, the conjecture holds for uniformly \(K_{t,t}\)-free classes, without any closure assumption.

The final consequence uses the established inclusion
\[
\text{bounded expansion}\Longrightarrow\text{bounded merge-width},
\]
and the source paper’s established direction of the conjecture.

---

## 2. Linear traces and biclique exclusion force bounded degeneracy

### Lemma 2
Suppose \(G\) is \(K_{t,t}\)-free and
\[
\nu_G(A)\le a|A|
\tag{1}
\]
for every nonempty \(A\subseteq V(G)\), where \(a\ge1\). Set
\[
q_t=1-e^{-t/4},
\qquad
d=\left\lceil\frac{4at(t-1)}{q_t}\right\rceil.
\tag{2}
\]
Then \(G\) is \(d\)-degenerate.

### Proof
Let \(F\subseteq G\) be any nonempty subgraph, and let \(\delta\) be its minimum degree. It suffices to bound \(\delta\).

Assume first that \(\delta\ge4t\). Choose a maximum cut \(X,Y\) of \(F\), naming its sides so that \(|X|\le |Y|\). Every vertex has at least half its \(F\)-neighbours across this cut.

Choose \(A\subseteq X\) by retaining vertices independently with probability
\[
p=\frac{4t}{\delta}\le1.
\]
For every \(y\in Y\), the random variable \(|N_G(y)\cap A|\) has mean at least \(2t\). The Chernoff bound gives
\[
\Pr\bigl(|N_G(y)\cap A|\ge t\bigr)\ge q_t.
\tag{3}
\]

For a realization of \(A\), let
\[
Y_A=\{y\in Y:|N_G(y)\cap A|\ge t\}.
\]
Any trace of size at least \(t\) occurs for at most \(t-1\) vertices of \(Y\): otherwise \(t\) such vertices and any \(t\) vertices of their common trace form a \(K_{t,t}\). Thus
\[
|Y_A|\le (t-1)a|A|.
\tag{4}
\]
For \(A=\varnothing\), this inequality holds directly because \(Y_A=\varnothing\).

Taking expectations,
\[
q_t|Y|
\le (t-1)ap|X|
\le \frac{4at(t-1)}{\delta}|Y|.
\]
Hence
\[
\delta\le \frac{4at(t-1)}{q_t}.
\]

If \(\delta<4t\), the same upper bound holds because \(a\ge1\), \(t\ge2\), and \(q_t<1\). Since \(F\) was arbitrary, \(G\) is \(d\)-degenerate. \(\square\)

In particular, under the hypothesis of Theorem 1, the identity transduction supplies a uniform \(a\), and Lemma 2 supplies a uniform \(d\). We will use
\[
|E(G[Z])|\le d|Z|
\tag{5}
\]
for every \(G\in\mathcal C\) and \(Z\subseteq V(G)\).

The fact that \(F\) need not belong to \(\mathcal C\) is important: throughout the sampling argument, neighbourhood traces are taken in \(G\), not in \(F\).

---

## 3. Extracting exact incidence graphs from shallow topological models

Here is the main extraction argument. It also proves a useful statement independently of biclique exclusion:

> For a uniformly degenerate class, linear neighbourhood complexity of the explicit path transductions defined below already forces bounded expansion.

Fix an integer \(\ell\ge2\). Suppose a simple graph \(H\) has a topological model in a \(d\)-degenerate graph \(G\), and consider just the model paths of length exactly \(\ell\).

Let

- \(B\) be the branch set, with \(|B|=n\);
- \(\mathcal P\) be these length-\(\ell\) paths, with \(|\mathcal P|=m\).

Their interiors are pairwise disjoint and disjoint from \(B\), and their endpoint pairs are distinct. If \(m<n\), there is already a linear bound. Hence assume \(m\ge n\).

### 3.1. Selecting paths with bounded interference

For \(P\in\mathcal P\), define
\[
Q(P)=\{b\in B:b\text{ has a neighbour in the interior of }P\},
\qquad q(P)=|Q(P)|.
\]
Writing \(I\) for the union of the interiors, we have
\[
\sum_{P\in\mathcal P}q(P)
\le e_G(B,I)
\le d\bigl(n+(\ell-1)m\bigr)
\le d\ell m.
\tag{6}
\]
Therefore at least \(m/2\) paths satisfy
\[
q(P)\le s_\ell:=2d\ell.
\tag{7}
\]

On these paths, form the conflict graph: two paths are adjacent when an edge of \(G\) joins their interiors. For any subfamily \(\mathcal U\), each conflict edge has a distinct witnessing edge between the corresponding interiors, so
\[
|E(J[\mathcal U])|
\le d(\ell-1)|\mathcal U|.
\]
Thus \(J\) is colourable with
\[
k_\ell:=2d(\ell-1)+1
\tag{8}
\]
colours. We obtain a subfamily \(\mathcal S\) such that
\[
|\mathcal S|\ge \frac{m}{2k_\ell},
\tag{9}
\]
every \(P\in\mathcal S\) satisfies (7), and **no edge joins interiors of distinct paths in \(\mathcal S\)**.

### 3.2. A fixed path-reading transduction

Orient each selected path as
\[
u_Px_1x_2\cdots x_{\ell-1}v_P.
\]
Use unary predicates \(U,Q_1,\ldots,Q_{\ell-1}\). The intended colouring will put selected branch vertices in \(U\), and position-\(i\) interior vertices in \(Q_i\).

The transduction \(\mathsf T_\ell\) has domain \(U\cup Q_1\). Its edges are only between \(Q_1\) and \(U\). For \(\ell=2\), use
\[
\theta_2(x,b)=E(x,b).
\]
For \(\ell\ge3\), use
\[
\begin{split}
\theta_\ell(x,b):={}&E(x,b)\ \lor\\
&\exists z_2\cdots z_{\ell-1}
\left(
 \bigwedge_{i=2}^{\ell-1}Q_i(z_i)
 \land E(x,z_2)
 \land\bigwedge_{i=2}^{\ell-2}E(z_i,z_{i+1})
 \land E(z_{\ell-1},b)
\right).
\end{split}
\tag{10}
\]
Formally, the output edge relation is the symmetric closure of
\[
Q_1(x)\land U(b)\land\theta_\ell(x,b),
\]
with loops deleted. Thus this defines a transduction on all unary expansions, including those not used in the proof.

On the intended colourings, a position-respecting chain in (10) cannot move between selected model paths. Consequently, the representative \(x_1\) of \(P\)

- is adjacent in the output to both endpoints of \(P\), if those endpoints are marked by \(U\);
- has no output neighbour among marked branch vertices outside \(Q(P)\).

Let \(c_\ell\ge1\) be a linear-neighbourhood-complexity constant for \(\mathsf T_\ell(\mathcal C)\).

### 3.3. Sampling away all spurious neighbours

Choose a random set \(A\subseteq B\), retaining each branch vertex independently with probability \(p\). Let
\[
\mathcal S_A
=
\{P\in\mathcal S:A\cap Q(P)=\{u_P,v_P\}\}.
\tag{11}
\]
For this realization, mark \(U=A\), and use the position predicates only on paths in \(\mathcal S_A\).

The output of \(\mathsf T_\ell\) is now exactly the incidence graph of a simple graph on \(A\): the path representative for \(P\in\mathcal S_A\) has neighbourhood
\[
\{u_P,v_P\}.
\]
These two-element traces are distinct. Therefore
\[
|\mathcal S_A|\le c_\ell |A|.
\tag{12}
\]
When \(A=\varnothing\), both sides of (12) are zero.

For each \(P\in\mathcal S\),
\[
\Pr(P\in\mathcal S_A)
=p^2(1-p)^{q(P)-2}
\ge p^2(1-p)^{s_\ell-2}.
\]
Taking expectations in (12) gives
\[
p^2(1-p)^{s_\ell-2}|\mathcal S|
\le c_\ell pn.
\tag{13}
\]
Choose \(p=1/(s_\ell-1)\). Since \(s_\ell\ge4\),
\[
\frac{1}{p(1-p)^{s_\ell-2}}
=(s_\ell-1)
 \left(1+\frac1{s_\ell-2}\right)^{s_\ell-2}
\le e(s_\ell-1).
\]
Combining this with (9) and (13),
\[
m\le 2e\,k_\ell(s_\ell-1)c_\ell n.
\tag{14}
\]

Thus, whether or not \(m\ge n\),
\[
m\le \beta_\ell n,
\qquad
\beta_\ell
=
\max\!\left\{
1,\,
2e[2d(\ell-1)+1](2d\ell-1)c_\ell
\right\}.
\tag{15}
\]
In particular,
\[
\beta_\ell=O(d^2\ell^2c_\ell).
\]
The transduction \(\mathsf T_\ell\) depends only on \(\ell\), not on \(d\) or on the model.

### 3.4. Completion of Theorem 1

Now suppose every edge of \(H\) is represented by a path of length at most \(L\). The length-one paths contribute at most
\[
|E(G[B])|\le dn.
\]
Apply (15) separately to each other length. We obtain
\[
|E(H)|
\le
\left(d+\sum_{\ell=2}^{L}\beta_\ell\right)|V(H)|.
\tag{16}
\]

The standard shallow-topological-minor characterization of bounded expansion says that these uniform density bounds, for every fixed \(L\), are equivalent to bounded expansion. Hence \(\mathcal C\) has bounded expansion, proving Theorem 1. \(\square\)

### Corollary 3: every weakly sparse transduct has bounded expansion
Suppose every FO transduction of \(\mathcal C\) has linear neighbourhood complexity. If
\[
\mathcal D\subseteq \mathsf T(\mathcal C)
\]
for some FO transduction \(\mathsf T\), and \(\mathcal D\) is uniformly \(K_{t,t}\)-free, then \(\mathcal D\) has bounded expansion.

Indeed, closure of FO transductions under composition implies that every transduction of \(\mathcal D\) has linear neighbourhood complexity. Apply Theorem 1.

---

## 4. No finite collection of transductions suffices

The next theorem explains why the family of path transductions above cannot simply be replaced by finitely many tests.

### Theorem 4
For every finite collection of FO transductions
\[
\mathsf R_1,\ldots,\mathsf R_k,
\]
there is a class \(\mathcal D\) of \(2\)-degenerate \(C_4\)-free graphs such that

1. each \(\mathsf R_i(\mathcal D)\) has linear neighbourhood complexity;
2. \(\mathcal D\) does not have bounded merge-width.

This is **not** a counterexample to the conjecture: another FO transduction of \(\mathcal D\) will explicitly fail linear neighbourhood complexity.

The proof uses Gaifman locality and sufficiently long subdivisions.

### 4.1. A long-subdivision locality lemma

For a graph \(H\), let \(S_L(H)\) denote the graph obtained by replacing every edge of \(H\) by a path of length exactly \(L\).

Fix a finite unary expansion of the graph language and a finite family \(\Phi\) of FO formulas \(\varphi(x,y)\). Define the joint trace of \(v\) on \(A\) by
\[
\operatorname{tr}_{\Phi}(v,A)
=
\left(\{a\in A:G\models\varphi(v,a)\}\right)_{\varphi\in\Phi}.
\]

### Lemma 5
There exist \(L\) and \(C\), depending only on the language and \(\Phi\), such that every unary expansion \(G\) of every \(S_L(H)\) satisfies
\[
\bigl|\{\operatorname{tr}_{\Phi}(v,A):v\in V(G)\}\bigr|
\le C|A|
\tag{17}
\]
for every nonempty \(A\subseteq V(G)\).

### Proof

#### The locality input

Gaifman’s locality theorem gives a radius \(r\ge1\) with the following consequences for the finite family \(\Phi\).

For a fixed expanded graph \(G\):

- The truth values of the formulas in \(\Phi\) at \((v,a)\) are determined by the rooted induced structure
  \[
  G[\operatorname{Ball}_r(v)\cup\operatorname{Ball}_r(a)]
  \]
  together with truth values of finitely many sentences of \(G\).

- When \(\operatorname{dist}(v,a)>2r+1\), these truth values are determined by the individual rooted \(r\)-balls’ types of some fixed finite quantifier rank, together with those same sentence values.

For the second assertion, the two balls are disjoint and have no edges between them. Bounded-rank types of their rooted components determine the bounded-rank type of their disjoint union. There are only finitely many such individual types; write their number as \(h\).

Set
\[
D=2r+1,\qquad R=2D+r=5r+2,
\]
and choose
\[
L>2R+1.
\tag{18}
\]

Let \(Z\) be the original vertices of \(H\), viewed as vertices of \(S_L(H)\). Distinct vertices of \(Z\) are at distance at least \(L\). Each radius-\(R\) ball centred in \(Z\) is a subdivided star whose arms have length \(R\), and these balls are pairwise disjoint.

We count joint traces.

#### Vertices far from \(A\)

If
\[
\operatorname{dist}(v,A)>D,
\]
the joint trace of \(v\) is determined by its individual local type. Thus these vertices contribute at most \(h\) traces.

#### Nearby vertices far from all original vertices

Consider vertices satisfying
\[
\operatorname{dist}(v,A)\le D,
\qquad
\operatorname{dist}(v,Z)>D.
\tag{19}
\]
For any fixed \(a\in A\), a path of length at most \(D\) from \(a\) to such a \(v\) cannot encounter \(Z\). It therefore lies inside one subdivided edge. There are at most \(2D+1\) possibilities for \(v\) for each \(a\). The vertices in (19) consequently contribute at most
\[
(2D+1)|A|
\]
traces.

#### Vertices near an original vertex

Every remaining vertex within distance \(D\) of \(A\) lies within distance \(D\) of a vertex in
\[
Z_A=\{z\in Z:\operatorname{dist}(z,A)\le2D\}.
\]
Since \(L>4D\), each \(a\in A\) is within distance \(2D\) of at most one original vertex. Hence
\[
|Z_A|\le |A|.
\tag{20}
\]

For each \(z\in Z_A\), call an arm of \(\operatorname{Ball}_R(z)\) **marked** if it contains a vertex of \(A\). The radius-\(R\) balls are disjoint, so the total number of marked arms over all \(z\in Z_A\) is at most \(|A|\).

The centres and the first \(D\) vertices of marked arms account for at most
\[
(D+1)|A|
\]
vertices.

It remains to consider the first \(D\) vertices of unmarked arms. Suppose there are \(p\) unary predicates. An arm’s first \(R\) vertices have a colour word over an alphabet of size \(2^p\). Classify a vertex by

1. its distance \(i\in\{1,\ldots,D\}\) from \(z\);
2. its arm’s length-\(R\) colour word.

For each fixed \(z\), there are at most
\[
D\,2^{pR}
\tag{21}
\]
classes.

Any two vertices \(v,w\) in the same class have identical joint traces on \(A\). Indeed, swapping their two arms is a colour-preserving automorphism of \(\operatorname{Ball}_R(z)\) fixing every vertex of \(A\) in that ball. It also shows that \(v\) and \(w\) have the same individual rooted \(r\)-ball type.

For any \(a\in A\):

- If \(\operatorname{dist}(v,a)\le D\), then
  \[
  \operatorname{Ball}_r(v)\cup\operatorname{Ball}_r(a)
  \subseteq \operatorname{Ball}_R(z).
  \]
  The arm swap fixes \(a\), maps the relevant rooted local structures, and gives equal truth values for all formulas in \(\Phi\).

- The same argument with \(v,w\) interchanged shows that either both are within distance \(D\) of \(a\), or neither is. In the latter case, equality follows from their equal individual local types.

By (20)–(21), unmarked arms contribute at most
\[
D\,2^{pR}|A|
\]
traces.

Adding the contributions and using \(|A|\ge1\), we obtain (17), for example with
\[
C=h+3D+2+D\,2^{pR}.
\]
This proves the lemma. \(\square\)

### 4.2. Applying the lemma to transductions, including copying

A fixed finite-copying transduction can be translated into finitely many formulas
\[
\varphi_{ij}(x,y)
\]
on a unary expansion of the original graph, one formula for each pair of copy indices. Its output-domain formulas only discard possible vertices.

Apply Lemma 5 simultaneously to all the formulas arising from
\(\mathsf R_1,\ldots,\mathsf R_k\), using a common finite unary vocabulary. Choose the resulting \(L\).

To see explicitly why copying causes no difficulty, let \(A\) be a set of output vertices, and let \(A^*\) be its projection onto original input vertices. Then
\[
|A^*|\le |A|.
\]
For a fixed witness-copy index \(i\), its joint traces under all \(\varphi_{ij}\) on \(A^*\) determine its entire output neighbourhood in \(A\). Lemma 5 bounds the number of such traces by \(C|A^*|\). Summing over the fixed number of witness copies still gives \(O(|A|)\).

Consequently, each \(\mathsf R_i\) has linear neighbourhood complexity on the class
\[
\mathcal D=\{S_L(K_n):n\ge1\}.
\tag{22}
\]

### 4.3. An omitted transduction detects unbounded complexity

Apply the path transduction \(\mathsf T_L\) from Section 3 to \(S_L(K_n)\):

- mark all original vertices as branch vertices;
- orient every subdivided edge;
- mark its interior vertices by their positions.

There are no additional edges between path interiors. The output is exactly the incidence graph of \(K_n\).

Taking \(A\) to be its \(n\) branch vertices, the edge-representatives give
\[
\binom n2
\]
distinct neighbourhood traces on \(A\). Hence
\[
\nu(A)\ge \binom n2,
\]
and \(\mathsf T_L(\mathcal D)\) does not have linear neighbourhood complexity.

By the source paper’s established direction, \(\mathcal D\) therefore cannot have bounded merge-width.

Finally, since \(L\ge2\), the graphs in (22) are \(2\)-degenerate. Every cycle has length at least \(3L\ge6\), so they are \(C_4\)-free. This completes the proof of Theorem 4. \(\square\)

---

## 5. What remains unresolved

The positive argument settles the converse whenever a fixed biclique is excluded, and more generally shows that every uniformly biclique-free FO image of a class satisfying the conjecture’s hypothesis has bounded expansion.

It does not handle unrestricted dense classes. The essential failure occurs in Lemma 2: without biclique exclusion, a large sampled trace can occur arbitrarily many times. Complete bipartite graphs illustrate why this cannot be repaired by trying to force bounded degeneracy or bounded expansion in the dense setting.

Thus the missing ingredient is a way to organize repeated dense neighbourhood patterns into bounded-width merge sequences. No such construction is supplied here.

The finite-test theorem adds a separate warning: even in the sparse setting, arbitrarily long fixed subdivisions can hide the obstruction from any prescribed finite list of transductions. The universal quantification over logical scales is genuinely necessary.

Accordingly, these are complete partial results, not a proof of the unrestricted conjecture.