```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The three-factor sharpness remains unresolved, but the bound improves to O(hb+t) for one-layer simplicial clique extensions of forests, and an explicit forest family shows that the hb interaction is unavoidable.",
  "would_publish": false,
  "caveats": "The special-class argument is elementary, gives no global o(thb) bound, and makes no claim of literature novelty."
}
```

# 1. Formulation

Let \(B_h\) denote the complete rooted binary tree with \(h\) levels, hence
\[
|V(B_h)|=2^h-1.
\]
If the source counts height in edges, all indices below shift by one and none of the asymptotic conclusions changes. Let \(\ell(G)\) denote the maximum number of vertices in a path of \(G\), and define
\[
F(t,h,b)=\max\{\operatorname{td}(G):
 \operatorname{tw}(G)<t,\ B_h\npreccurlyeq G,\ \ell(G)<2^b\}.
\]
The published result gives
\[
F(t,h,b)=O(thb).
\]

I do not resolve whether \(F(t,h,b)=\Omega(thb)\) for a cofinal family of triples, nor prove a global bound such as
\[
O(th+tb+hb).
\]

What follows are three rigorous partial results.

---

# 2. A universal pointwise improvement

## Proposition 2.1
Every graph \(G\) satisfies
\[
\operatorname{td}(G)\leq \ell(G).
\]
Consequently,
\[
F(t,h,b)\leq \min\{Cthb,\,2^b-1\}
\]
for the absolute constant \(C\) in the published theorem.

### Proof
Run depth-first search in each component of \(G\). In an undirected graph, every edge has ancestor-comparable endpoints in the resulting DFS forest \(T\). Thus
\[
G\subseteq \operatorname{clos}(T).
\]
Every root-to-leaf path in \(T\) is a path in \(G\), so the height of \(T\) is at most \(\ell(G)\). Hence
\[
\operatorname{td}(G)\leq \ell(G).
\]
If \(G\) has no \(2^b\)-vertex path, then \(\ell(G)\leq 2^b-1\). ∎

This improves the product bound when \(2^b\ll thb\), but it does not affect the main regime \(2^b\gg thb\).

---

# 3. A class where the factor \(t\) is only additive

The following elementary extension lemma isolates a fairly broad family which cannot witness three-factor sharpness.

## Lemma 3.1: simplicial-clique extension
Let \(H\) be a graph. For each \(i\), choose a clique \(C_i\subseteq V(H)\), possibly empty, and add a new clique \(X_i\). Make \(X_i\) complete to \(C_i\), anticomplete to \(V(H)\setminus C_i\), and put no edges between distinct \(X_i\)'s. If
\[
s=\max_i |X_i|,
\]
then
\[
\operatorname{td}(G)\leq \operatorname{td}(H)+s.
\]

### Proof
Let \(R\) be a treedepth forest for \(H\) of height \(d=\operatorname{td}(H)\). Since \(C_i\) is a clique, its vertices are pairwise comparable in the ancestor order of \(R\). Thus they lie on one root-to-leaf chain.

If \(C_i\neq\varnothing\), let \(z_i\) be its deepest vertex and attach below \(z_i\) a rooted path whose vertex set is \(X_i\). If \(C_i=\varnothing\), use such a path as a new component. Different paths may be attached as siblings.

Every edge within \(X_i\) is covered because \(X_i\) is placed on a chain. Every vertex of \(C_i\) is an ancestor of every vertex of \(X_i\), so all edges between \(C_i\) and \(X_i\) are covered. There are no other new edges. The resulting forest has height at most \(d+s\). ∎

## Corollary 3.2
Suppose \(G\) is obtained as in Lemma 3.1 from a forest \(H\), and suppose
\[
\operatorname{tw}(G)<t,\qquad
B_h\npreccurlyeq G,\qquad
\ell(G)<2^b.
\]
Then
\[
\operatorname{td}(G)=O(hb+t).
\]

### Proof
Because \(H\subseteq G\), the forest \(H\) also excludes \(B_h\) as a minor and \(P_{2^b}\) as a subgraph. Applying the published theorem to \(H\), whose treewidth is less than \(2\), gives
\[
\operatorname{td}(H)=O(hb).
\]
Moreover, every \(X_i\) is a clique of \(G\), so
\[
|X_i|\leq \omega(G)\leq \operatorname{tw}(G)+1\leq t.
\]
Lemma 3.1 now gives
\[
\operatorname{td}(G)\leq \operatorname{td}(H)+t=O(hb+t).
\]
∎

This class includes, for example, forests whose vertices or edges are decorated by arbitrary pairwise noninteracting cliques. Thus simple “replace forest edges by cliques” constructions cannot establish an \(\Omega(thb)\) lower bound.

---

# 4. An explicit forest family forcing the \(hb\) product

I next give a completely specified family showing that \(hb\) cannot in general be replaced by \(h+b\), even when the treewidth is \(1\).

## Construction

For integers \(k\geq1\) and \(n\geq2\), define a subcubic tree \(T_{k,n}\) recursively.

- \(T_{1,n}=P_n\).
- Given \(T_{k-1,n}\), take a fresh path
  \[
  Q=v_1v_2\cdots v_n.
  \]
  At each \(v_i\), attach by one edge a disjoint copy of \(T_{k-1,n}\), using a leaf of that copy as the attachment vertex.

Each attached leaf has its degree raised from \(1\) to \(2\), while each internal spine vertex has degree \(3\). Hence
\[
\Delta(T_{k,n})\leq3.
\]

Let \(N_k=|V(T_{k,n})|\) and let \(L_k=\ell(T_{k,n})\).

## Lemma 4.1: order and longest path
For every \(k,n\),
\[
N_k\geq n^k
\]
and
\[
L_k\leq (2^k-1)n.
\]

### Proof
The order satisfies
\[
N_1=n,\qquad N_k=n+nN_{k-1},
\]
so \(N_k\geq n^k\).

A path meeting the top spine \(Q\) can have vertices outside \(Q\) in at most two attached copies: one at each end of its intersection with \(Q\). Indeed, entering and returning from a pendant copy would repeat the unique attachment vertex. Therefore
\[
L_k\leq n+2L_{k-1}.
\]
Together with \(L_1=n\), this yields
\[
L_k\leq(2^k-1)n.
\]
∎

## Lemma 4.2: pathwidth
\[
\operatorname{pw}(T_{k,n})\leq k.
\]

### Proof
The assertion is clear for \(k=1\). Suppose each attached copy has a path decomposition of width at most \(k-1\). Add its attachment spine vertex \(v_i\) to every bag of that decomposition, obtaining bags of size at most \(k+1\). Concatenate these decompositions in spine order and insert bags \(\{v_i,v_{i+1}\}\) between consecutive pieces. This is a path decomposition of \(T_{k,n}\) of width at most \(k\). ∎

We use the standard fact
\[
\operatorname{pw}(B_r)=\left\lfloor\frac r2\right\rfloor.
\]
For completeness, the needed lower bound follows from the path-removal characterization of pathwidth for trees: if \(\operatorname{pw}(T)\leq q\), there is a path \(P\subseteq T\) such that every component of \(T-P\) has pathwidth at most \(q-1\). Every path in \(B_r\) misses one of the four copies of \(B_{r-2}\) rooted at depth two, and hence
\[
\operatorname{pw}(B_r)\geq \operatorname{pw}(B_{r-2})+1.
\]
The initial cases give the displayed formula.

Because pathwidth is minor-monotone, Lemma 4.2 implies
\[
B_{2k+2}\npreccurlyeq T_{k,n}.
\]

## Lemma 4.3: treedepth from order and degree
If \(T\) is a tree of maximum degree at most \(3\) and treedepth \(d\), then
\[
|V(T)|\leq \frac{3^d-1}{2}.
\]
In particular,
\[
\operatorname{td}(T)>\log_3 |V(T)|.
\]

### Proof
Let \(M_d\) be the maximum order of such a tree of treedepth at most \(d\). For an optimal first vertex \(v\) in the treedepth recurrence, \(T-v\) has at most three components, each of treedepth at most \(d-1\). Thus
\[
M_1=1,\qquad M_d\leq1+3M_{d-1}.
\]
Induction gives \(M_d\leq(3^d-1)/2\). ∎

Combining Lemmas 4.1 and 4.3,
\[
\operatorname{td}(T_{k,n})
 \geq k\log_3 n.
\]

## Theorem 4.4: explicit \(hb\) lower bound
Let
\[
h=2k+2,\qquad b\geq h,
\qquad n=2^{\,b-k-1}.
\]
Then \(T_{k,n}\) satisfies

\[
\operatorname{tw}(T_{k,n})=1,
\]
\[
B_h\npreccurlyeq T_{k,n},
\]
\[
\ell(T_{k,n})<2^b,
\]
and
\[
\operatorname{td}(T_{k,n})
 \geq \frac{\log_3 2}{8}\,hb.
\]

### Proof
The treewidth assertion is immediate. We have already proved exclusion of \(B_{2k+2}=B_h\).

Moreover,
\[
\ell(T_{k,n})
 \leq (2^k-1)2^{b-k-1}
 <2^{b-1}<2^b.
\]
Finally,
\[
\operatorname{td}(T_{k,n})
 \geq k(b-k-1)\log_3 2.
\]
Since \(b\geq2k+2\),
\[
b-k-1\geq \frac b2,
\]
and since \(h=2k+2\geq4\),
\[
k\geq\frac h4.
\]
The claimed lower bound follows. ∎

Thus, for \(b\geq h\) and infinitely many \(h\),
\[
F(2,h,b)=\Theta(hb).
\]
In particular, no universal \(O(h+b)\) bound is possible even for forests.

---

# 5. Sharpness of the special-class bound

The \(O(hb+t)\) estimate from Corollary 3.2 is asymptotically tight for that class over a natural parameter range.

Take the disjoint union
\[
G=T_{k,n}\ \dot\cup\ K_t
\]
from Theorem 4.4. This is a simplicial-clique extension of the forest \(T_{k,n}\), allowing the empty attachment clique.

If
\[
t\leq \min\{2^b-1,\,2^h-2\},
\]
then:

- \(K_t\) has no \(2^b\)-vertex path;
- \(K_t\) cannot contain \(B_h\) as a minor, since every minor of \(K_t\) has at most \(t<2^h-1\) vertices;
- \(\operatorname{tw}(G)=t-1<t\);
- and
  \[
  \operatorname{td}(G)
   =\max\{\operatorname{td}(T_{k,n}),t\}
   =\Omega(hb+t).
  \]

Together with Corollary 3.2, this gives
\[
\operatorname{td}(G)=\Theta(hb+t)
\]
for this special class, in the indicated range.

---

# 6. Remaining gap

These arguments do not settle the catalog problem.

The extension lemma works because all dense pieces form only one simplicial layer over a forest. In a general treewidth-\((t-1)\) graph, clique separators can be nested. A naive application of Lemma 3.1 at every nested level can incur the factor \(t\) repeatedly, returning to \(O(thb)\). Controlling how such nested separators simultaneously create long paths or binary-tree minors is precisely the missing global argument.

Conversely, the forest construction above gives the full \(hb\) interaction but has fixed treewidth. Adding a disjoint \(K_t\) produces only an additive \(t\), not a simultaneous \(t\)-multiplier. No explicit family here has treedepth \(\Omega(thb)\) with all three canonical parameters tending to infinity independently.

Hence the principal alternatives remain open:

- construct graphs witnessing \(\Omega(thb)\), or
- prove a genuinely smaller global bound, plausibly of pairwise-product form such as \(O(th+tb+hb)\).