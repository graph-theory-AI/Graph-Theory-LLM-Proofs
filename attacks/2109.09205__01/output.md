```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A regularity-free lifting of the book theorem gives exact p-goodness for every connected bounded-vertex-cover target and an additive-constant bound for targets with a fixed separator and bounded components, but it does not recover the full Nikiforov–Rousseau theorem.",
  "would_publish": false,
  "caveats": "The argument uses the Fox–He–Wigderson book theorem as an input and leaves the zero-slack structural step and the remaining cases of Nikiforov–Rousseau Theorem 2.1 unresolved."
}
```

# Mathematical writeup

## 1. Interpretation and status

The theorem of Nikiforov and Rousseau is already proved; the open question concerns whether its proof can be replaced by one not using Szemerédi regularity. Strictly speaking, “regularity-free” is not a formal property of a theorem—one could hide regularity inside a counting or removal lemma—so I interpret the question conventionally: construct an explicit proof whose stated ingredients have elementary, non-regularity proofs.

I do not obtain such a proof in full generality. I give:

1. a general elementary reduction from graphs with a small separator to books;
2. an exact regularity-free result for every connected graph of bounded vertex-cover number;
3. a regularity-free additive-constant approximation for graphs that become bounded-component after deleting a fixed set;
4. an elementary estimate showing that the same reduction incurs only \(O(|G|)\) slack when the red graph has bounded vertex-cover number.

These isolate a concrete remaining obstacle: an exact, zero-slack component-packing or absorption statement.

Throughout, Ramsey containment is ordinary, not induced, containment.

---

## 2. An elementary lifting lemma

Recall
\[
B_{s,N}=K_s\vee \overline K_{N-s}.
\]

### Lemma 2.1 — Lifting from books

Let \(G,H\) be graphs, \(n=v(H)\), and let \(S\subseteq V(H)\) have size \(s\geq 1\). Suppose
\[
V(H)\setminus S=W_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}W_\ell
\]
with no edge of \(H\) joining two distinct \(W_i,W_j\). Put
\[
Q_i=H[W_i],\qquad q_i=v(Q_i),
\]
and define
\[
c=\max_{1\leq i\leq\ell}\bigl(r(G,Q_i)-q_i\bigr),
\]
with \(c=0\) if \(\ell=0\). Then
\[
r(G,H)\leq r(G,B_{s,n+c}).
\]

More generally, \(c\) may be replaced by any \(c'\geq c\).

#### Proof

Consider a red-blue coloring of
\[
K_{r(G,B_{s,n+c})}
\]
with no red \(G\). It contains a blue \(B_{s,n+c}\). Let \(X\) be its spine and \(P\) its page set. Thus
\[
|X|=s,\qquad |P|=\sum_iq_i+c,
\]
\(X\) is a blue clique, and every edge between \(X\) and \(P\) is blue.

We greedily find disjoint blue copies of \(Q_1,\ldots,Q_\ell\) in \(P\). If \(I\) is the set of blocks still to be embedded, then the unused page set has size
\[
c+\sum_{i\in I}q_i.
\]
For any \(i\in I\), this is at least
\[
c+q_i\geq r(G,Q_i).
\]
Since the whole coloring has no red \(G\), the unused page set contains a blue \(Q_i\). Remove only the vertices of that copy and continue.

After all blocks have been embedded, map \(H[S]\) into the blue clique \(X\). Every required edge from \(S\) to a block is present because all spine-page edges are blue, and there are no required edges between distinct blocks. Hence there is a blue \(H\). ∎

This argument uses only finite Ramsey numbers and greedy packing.

---

## 3. Consequence of the regularity-free book theorem

The external input supplied in the question is the Fox–He–Wigderson theorem
\[
n\geq 2^{k^{10p}}
\quad\Longrightarrow\quad
r(K_p,B_{k,n})=(p-1)(n-1)+1.
\tag{3.1}
\]

### Theorem 3.1 — Additive-constant goodness for bounded-component separators

Fix \(p\geq2\), \(s\geq1\), and \(d\geq1\). Define
\[
C_{p,d}
 =
 \max_{\substack{Q\text{ a graph}\\1\leq v(Q)\leq d}}
 \bigl(r(K_p,Q)-v(Q)\bigr).
\tag{3.2}
\]
Let \(H\) be a connected \(n\)-vertex graph admitting a set \(S\) of size at most \(s\) such that every component of \(H-S\) has at most \(d\) vertices. If
\[
n+C_{p,d}\geq 2^{s^{10p}},
\]
then
\[
(p-1)(n-1)+1
\leq r(K_p,H)
\leq
(p-1)(n+C_{p,d}-1)+1.
\tag{3.3}
\]

In particular, the error above the goodness bound is at most
\[
(p-1)C_{p,d},
\]
a constant depending only on \(p,d\).

#### Proof

If necessary, enlarge \(S\) to size exactly \(s\); deleting more vertices cannot increase the sizes of the remaining components. Apply Lemma 2.1 to the components \(Q_i\) of \(H-S\), using \(c'=C_{p,d}\). By (3.1),
\[
r(K_p,H)
 \leq r(K_p,B_{s,n+C_{p,d}})
 =(p-1)(n+C_{p,d}-1)+1.
\]

For the lower bound, color the complete graph on \((p-1)(n-1)\) vertices by partitioning it into \(p-1\) sets of size \(n-1\), coloring edges inside a set blue and edges between sets red. The red graph is \((p-1)\)-partite and hence contains no \(K_p\). Every blue component has only \(n-1\) vertices, so it contains no connected \(n\)-vertex \(H\). ∎

The constant in (3.2) is completely finite and can be bounded explicitly:
\[
C_{p,d}
\leq r(K_p,K_d)-1
\leq \binom{p+d-2}{p-1}-1.
\]

### Fan-type specialization

Let \(F,J\) be fixed graphs with \(s=v(F)\geq1\), \(j=v(J)\), and let
\[
H_t=F\vee(tJ),
\qquad n=s+tj,
\]
where \(tJ\) denotes \(t\) disjoint copies of \(J\). Put
\[
c_{p,J}=r(K_p,J)-j.
\]
Lemma 2.1, using the \(t\) copies of \(J\) as the blocks, gives for sufficiently large \(t\)
\[
(p-1)(n-1)+1
\leq r(K_p,H_t)
\leq
(p-1)(n+c_{p,J}-1)+1.
\tag{3.4}
\]
Thus these fan-type graphs are regularity-free \(p\)-good up to an additive constant independent of \(t\). This does not establish exact goodness.

---

## 4. Exact result for bounded vertex cover

Let \(\tau(H)\) denote the vertex-cover number.

### Proposition 4.1 — Books are spanning-universal for bounded vertex cover

If \(H\) has \(n\) vertices, \(\tau(H)\leq k\), and \(k\leq n\), then \(H\) is a spanning subgraph of \(B_{k,n}\).

#### Proof

Let \(C\) be a vertex cover of size \(c\leq k\). Then \(V(H)\setminus C\) is independent. Add \(k-c\) vertices of \(V(H)\setminus C\) to \(C\), obtaining a \(k\)-element set \(C'\). Map \(C'\) to the spine of \(B_{k,n}\) and all remaining vertices to pages. Every edge of \(H\) either lies within \(C'\) or has one endpoint in \(C'\), and all such edges are present in the book. ∎

This is also the case \(d=1\) of Theorem 3.1, because
\[
C_{p,1}=r(K_p,K_1)-1=0.
\]

### Theorem 4.2 — Uniform regularity-free goodness for bounded vertex cover

Let \(p\geq2\), and let \(H\) be a connected \(n\)-vertex graph with
\[
t=\tau(H)\geq1.
\]
If
\[
n\geq 2^{t^{10p}},
\]
then
\[
r(K_p,H)=(p-1)(n-1)+1.
\tag{4.1}
\]

#### Proof

The lower bound is the standard coloring from Theorem 3.1. By Proposition 4.1,
\[
H\subseteq B_{t,n}.
\]
Hence, by (3.1),
\[
r(K_p,H)\leq r(K_p,B_{t,n})
=(p-1)(n-1)+1.
\]
The two bounds agree. ∎

Consequently, (4.1) holds uniformly even when the vertex-cover number grows slowly with \(n\), for example whenever
\[
\tau(H)\leq(\log_2 n)^{1/(10p)}.
\]

### Complete multipartite consequence

Let \(q\geq2\), let \(a_1,\ldots,a_{q-1}\) be positive integers, and put
\[
t=a_1+\cdots+a_{q-1},\qquad a_q=n-t\geq1.
\]
The union of the first \(q-1\) parts is a vertex cover of
\[
K_q(a_1,\ldots,a_q).
\]
Therefore, if \(n\geq2^{t^{10p}}\),
\[
r\!\left(K_p,K_q(a_1,\ldots,a_{q-1},n-t)\right)
=(p-1)(n-1)+1.
\tag{4.2}
\]
Thus the regularity-free book theorem already covers arbitrary complete multipartite targets with all but one part of bounded total size, not merely books whose small parts are singletons.

---

## 5. Exact transfer for more general red graphs

For a graph \(G\) with \(\chi(G)=p\), define
\[
\sigma(G)=
\min\bigl\{|C|:\ C\text{ is a color class in a proper }p\text{-coloring of }G\bigr\}.
\]

### Proposition 5.1

Suppose \(\sigma(G)\leq n\) and
\[
r(G,B_{k,n})=(p-1)(n-1)+\sigma(G).
\tag{5.1}
\]
Then every connected \(n\)-vertex graph \(H\) with \(\tau(H)\leq k\) satisfies
\[
r(G,H)=(p-1)(n-1)+\sigma(G).
\tag{5.2}
\]

#### Proof

The upper bound follows from \(H\subseteq B_{k,n}\).

For the lower bound, use \(p\) blue cliques: \(p-1\) of order \(n-1\), and one of order \(\sigma(G)-1\), with all cross-edges red. Every blue component has fewer than \(n\) vertices. If the red graph contained \(G\), its intersections with the \(p\) blue cliques would give a proper \(p\)-coloring of \(G\) having one class of size at most \(\sigma(G)-1\), a contradiction. ∎

Therefore every regularity-free book equality already proved by Fox–He–Wigderson transfers without change to all connected targets of the same order and bounded vertex-cover number. In particular, this applies to the complete multipartite red graphs in every parameter range where their book theorem gives the corresponding equality.

---

## 6. Bounded-cover red graphs and bounded components

The lifting constant in Lemma 2.1 is \(r(G,Q_i)-v(Q_i)\). When \(G\) itself has bounded vertex cover and the \(Q_i\) are bounded, this cost is only linear in \(v(G)\), by an elementary supersaturation argument.

### Proposition 6.1

Let \(G\) have \(g\) vertices and \(\tau(G)\leq A\leq g\). Let \(Q\) be any graph, and put
\[
R=\max\{A+1,r(K_{A+1},Q)\},
\qquad
D=\binom{R}{A+1}.
\]
Then
\[
r(G,Q)
\leq
\max\{R,\ A+D(g-A)\}.
\tag{6.1}
\]

#### Proof

Set
\[
N=\max\{R,\ A+D(g-A)\}
\]
and consider a red-blue coloring of \(K_N\) with no blue \(Q\). Every \(R\)-vertex set contains a red \(K_{A+1}\).

Let \(t_{A+1}\) be the number of red \(K_{A+1}\)'s. Double-counting pairs consisting of an \(R\)-set and a red \(K_{A+1}\) contained in it gives
\[
t_{A+1}\binom{N-A-1}{R-A-1}\geq\binom NR.
\]
Using
\[
\frac{\binom NR}{\binom{N-A-1}{R-A-1}}
=
\frac{\binom N{A+1}}{\binom R{A+1}},
\]
we obtain
\[
t_{A+1}\geq \frac{\binom N{A+1}}{D}.
\]

For each red \(K_A\), count its common red neighbors. Summing over all red \(K_A\)'s counts every red \(K_{A+1}\) exactly \(A+1\) times. Since there are at most \(\binom NA\) red \(K_A\)'s, some red \(K_A\) has at least
\[
\frac{(A+1)t_{A+1}}{\binom NA}
\geq
\frac{(A+1)\binom N{A+1}}{D\binom NA}
=
\frac{N-A}{D}
\geq g-A
\]
common red neighbors.

It follows that the red graph contains \(B_{A,g}\). Since \(\tau(G)\leq A\), Proposition 4.1 implies \(G\subseteq B_{A,g}\), so the red graph contains \(G\). ∎

If every block \(Q_i\) has at most \(d\) vertices, one may take
\[
R_0=\max\{A+1,r(K_{A+1},K_d)\},
\qquad
D_0=\binom{R_0}{A+1},
\]
uniformly. Consequently,
\[
r(G,Q_i)=O_{A,d}(g),
\]
and Lemma 2.1 gives the regularity-free reduction
\[
r(G,H)
\leq
r\!\left(G,B_{s,n+O_{A,d}(g)}\right).
\tag{6.2}
\]

This is relevant to the complete multipartite red graphs described in the prompt: the union of their fixed-size parts is a vertex cover of bounded size. When \(g\leq\delta n\), the inflation in (6.2) is \(O(\delta n)\). Thus the component-extraction portion can be performed without regularity at the cost of a small proportional error. It does not give the exact Ramsey number, because even an \(O(g)\) inflation changes the claimed answer.

---

## 7. The unresolved zero-slack step

Lemma 2.1 packs the components of \(H-S\) after retaining
\[
r(G,Q_i)-v(Q_i)
\]
spare page vertices. To recover the exact Nikiforov–Rousseau formula, these spare vertices must be eliminated. Merely knowing that the page coloring has no red \(G\) is insufficient for a spanning component factor: parity and divisibility obstructions can prevent a perfect blue packing even though a packing leaving \(O(1)\) vertices is immediate.

There are also competing lower-bound phenomena when the red graph grows. For example, let \(n\) be even and color \(K_n\) red as a perfect matching. For every \(m\geq2\), there is no red \(K_{1,m}\). The blue graph has no universal vertex, so it has no spanning \(B_{k,n}\) for any \(k\geq1\). Thus one cannot extrapolate a goodness formula based only on chromatic number and smallest color class to all growing sparse red graphs.

A complete regularity-free proof would therefore require an elementary stability/absorption theorem that:

1. works at the exact extremal number of vertices;
2. produces the required core together with a zero-slack packing of all components;
3. handles all competing lower-bound configurations in Nikiforov–Rousseau Theorem 2.1.

No such argument is provided here. The catalog problem remains open.