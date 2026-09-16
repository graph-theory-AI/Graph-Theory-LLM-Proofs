```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds when alpha(G) <= 2 and each nonadjacent pair is contained in at most three induced 5-cycles.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; no novelty claim is made for the restricted result, and no computational checks are asserted."
}
```

## 1. Partial result

Write \(h(G)\) for the largest order of a complete minor of \(G\), with \(h(\varnothing)=0\). For nonempty graphs, the conjecture is equivalent to
\[
|V(G)|\leq \alpha(G)h(G).
\]

I focus on the independence-number-two case identified in the question. The following result is self-contained.

For distinct nonadjacent vertices \(x,y\), let
\[
m_5(x,y;G)
=
\bigl|\{X\subseteq V(G): |X|=5,\ x,y\in X,\ G[X]\cong C_5\}\bigr|.
\]
Define
\[
\mu_5(G)=\max_{xy\notin E(G)}m_5(x,y;G),
\]
taking the maximum to be zero if \(G\) is complete.

**Theorem.** If \(\alpha(G)\leq2\) and \(\mu_5(G)\leq3\), then
\[
h(G)\geq \left\lceil\frac{|V(G)|}{2}\right\rceil.
\]
Consequently, the proposed independence bound holds for these graphs.

In particular, this covers graphs with \(\alpha(G)\leq2\) and no induced \(C_5\).

The argument also gives a quantitative obstruction bound.

**Proposition.** Fix an integer \(r\geq1\). If there is a graph with
\[
\alpha(G)\leq2,\qquad \mu_5(G)\leq r,\qquad |V(G)|>2h(G),
\]
then there is such a graph on at most \(5r\) vertices.

Thus the restricted assertion for any fixed cycle-overlap bound admits a finite verification bound. The proof below settles \(r\leq3\) without enumeration.

## 2. Two elementary minor observations

An edge \(xy\) is **dominating** if every vertex outside \(\{x,y\}\) is adjacent to \(x\) or \(y\). Contracting this edge gives a vertex adjacent to every vertex of \(G-\{x,y\}\). Hence
\[
h(G)\geq 1+h(G-\{x,y\}). \tag{1}
\]

We also need the following clique-extension lemma.

**Lemma 1.** Suppose \(\alpha(G)\leq2\), \(G\) contains a clique of order \(q\), and \(|V(G)|\geq2q+1\). Then \(h(G)\geq q+1\).

**Proof.** Let \(Q\) be a \(q\)-clique and put \(H=G-Q\), so \(|V(H)|\geq q+1\).

If \(H\) is connected, there are two possibilities.

- Every vertex of \(Q\) has a neighbor in \(H\). Contracting \(H\) then produces a \(K_{q+1}\) minor.
- Some vertex of \(Q\) has no neighbor in \(H\). The condition \(\alpha(G)\leq2\) forces \(H\) to be complete, giving a \(K_{q+1}\) subgraph.

If \(H\) is disconnected, it consists of two nonempty cliques \(A,B\): otherwise three independent vertices could be selected from its components. Every vertex of \(Q\) is complete to at least one of \(A,B\), since \(A\) and \(B\) are anticomplete.

Let \(Q_A,Q_B\) be the vertices of \(Q\) complete to \(A,B\), respectively. Then \(Q_A\cup Q_B=Q\), and
\[
\bigl(|A|+|Q_A|\bigr)+\bigl(|B|+|Q_B|\bigr)
\geq |V(H)|+q
\geq2q+1.
\]
Thus one of the cliques \(A\cup Q_A\), \(B\cup Q_B\) has order at least \(q+1\). ∎

## 3. Structure of a smallest counterexample

Both \(\alpha(G)\leq2\) and \(\mu_5(G)\leq r\) are preserved by taking induced subgraphs.

Fix \(r\), and suppose that \(G\) is a minimum-order graph satisfying these two conditions but
\[
n:=|V(G)|>2h(G).
\]
Put \(h=h(G)\).

### 3.1 Its order is exactly \(2h+1\)

For every vertex \(v\), minimality gives
\[
n-1\leq2h(G-v)\leq2h.
\]
Consequently,
\[
n=2h+1. \tag{2}
\]

A disconnected graph with independence number at most two consists of at most two cliques, and therefore satisfies \(h(G)\geq\lceil n/2\rceil\). Thus \(G\) is connected. It is also not complete.

Equation (1) and minimality show that \(G\) has no dominating edge.

Finally,
\[
\omega(G)\leq h-1. \tag{3}
\]
Indeed, if \(\omega(G)=h\), Lemma 1 and \(n=2h+1\) give a \(K_{h+1}\) minor.

### 3.2 Complementary structure

Let \(F=\overline G\). Since \(\alpha(G)\leq2\), the graph \(F\) is triangle-free.

The absence of a dominating edge in \(G\) says that every nonadjacent pair in \(F\) has a common neighbor. In particular, \(F\) has no isolated vertices.

Every neighborhood in \(F\) is an independent set of \(F\), hence a clique of \(G\). Therefore (3) gives
\[
\Delta(F)\leq h-1. \tag{4}
\]

We will also need that \(F\) contains a \(5\)-cycle. Here is a direct argument.

Because \(G\) is connected and not complete, it contains an induced path \(a-b-c\). Since neither \(ab\) nor \(bc\) is dominating, choose vertices \(x,y\) such that
\[
xa,xb,yb,yc\notin E(G).
\]
The condition \(\alpha(G)\leq2\) forces
\[
xc,ya,xy\in E(G).
\]
The vertices are distinct, and
\[
a-b-c-x-y-a
\]
is an induced \(C_5\). Since \(C_5\) is self-complementary, \(F\) also contains an induced \(C_5\).

## 4. Counting five-cycles through an edge

For an edge \(ab\) of \(F\), let \(c_5(ab;F)\) denote the number of \(5\)-cycles containing that edge. Every \(5\)-cycle in a triangle-free graph is induced. Self-complementarity of \(C_5\) therefore gives
\[
c_5(ab;F)=m_5(a,b;G)\leq r. \tag{5}
\]

We claim that
\[
c_5(ab;F)\geq n-d_F(a)-d_F(b). \tag{6}
\]

To see this, put
\[
Z=V(F)\setminus\bigl(N_F(a)\cup N_F(b)\bigr).
\]
Because \(F\) is triangle-free and \(ab\) is an edge, the two neighborhoods are disjoint and their union contains \(a,b\). Hence
\[
|Z|=n-d_F(a)-d_F(b).
\]

For every \(z\in Z\), the common-neighbor property provides
\[
x\in N_F(a)\cap N_F(z),\qquad
y\in N_F(b)\cap N_F(z).
\]
Triangle-freeness ensures that
\[
a-x-z-y-b-a
\]
is an induced \(5\)-cycle. Different choices of \(z\) produce different cycles: in a \(5\)-cycle containing \(ab\), exactly one vertex is nonadjacent to both \(a\) and \(b\). This proves (6).

### The finite counterexample bound

Fix a \(5\)-cycle \(v_0v_1v_2v_3v_4v_0\) in \(F\), with indices modulo five. Combining (5) and (6) gives
\[
d_F(v_i)+d_F(v_{i+1})\geq n-r.
\]
Summing,
\[
2\sum_{i=0}^4 d_F(v_i)\geq5(n-r). \tag{7}
\]

Every vertex of \(F\) has at most two neighbors on this cycle: its neighbors there form an independent set in a \(C_5\). Thus
\[
\sum_{i=0}^4 d_F(v_i)\leq2n.
\]
Together with (7), this yields
\[
5(n-r)\leq4n,
\qquad\text{so}\qquad
n\leq5r. \tag{8}
\]
This proves the proposition.

## 5. Excluding cycle-overlap bound three

Now assume \(r=3\). For every edge \(ab\) of \(F\), equations (2), (4), (5), and (6) give
\[
3
\geq c_5(ab;F)
\geq n-d_F(a)-d_F(b)
\geq (2h+1)-2(h-1)
=3.
\]
Every inequality is therefore an equality.

Since \(F\) has no isolated vertices, it follows that:

- \(F\) is \(d\)-regular, where \(d=h-1\);
- \(n=2d+3\);
- every edge of \(F\) lies in exactly three \(5\)-cycles.

By (8), \(n\leq15\), so \(d\leq6\). Since \(n\) is odd, the handshake lemma makes \(d\) even. Also \(d>0\), because \(F\) contains a \(5\)-cycle. Hence
\[
d\in\{2,4,6\}.
\]

Let \(N_5\) be the number of \(5\)-cycles of \(F\). Counting edge-cycle incidences,
\[
5N_5=3|E(F)|=\frac{3nd}{2}.
\]
In particular, \(5\mid nd\). For \(n=2d+3\), the possibilities \(d=2,4\) give \(nd=14,44\), respectively, and are impossible. Thus
\[
d=6,\qquad n=15. \tag{9}
\]

### The last possible structure is also impossible

Fix a \(5\)-cycle \(C=v_0v_1v_2v_3v_4v_0\) in \(F\). By (9),
\[
\sum_{i=0}^4d_F(v_i)=30=2n.
\]
The inequality used in (7) is consequently tight: **every vertex of \(F\) has exactly two neighbors on \(C\)**.

Those two neighbors are nonadjacent on \(C\). Define
\[
A_i=\{x\in V(F):N_F(x)\cap V(C)=\{v_{i-1},v_{i+1}\}\}.
\]
These five sets partition \(V(F)\), with \(v_i\in A_i\). Moreover,
\[
N_F(v_i)=A_{i-1}\cup A_{i+1},
\]
so, writing \(a_i=|A_i|\),
\[
a_{i-1}+a_{i+1}=6
\qquad(i\in\mathbb Z/5\mathbb Z).
\]
These five equations force
\[
a_0=a_1=a_2=a_3=a_4=3.
\]

Vertices in the same class, or in nonconsecutive classes, share a neighbor on \(C\), and hence cannot be adjacent in the triangle-free graph \(F\). Thus a vertex in \(A_i\) can have neighbors only in \(A_{i-1}\cup A_{i+1}\). That union has six vertices, and every vertex has degree six, so all those possible edges are present.

Therefore \(F\) is the blow-up of \(C_5\) obtained by replacing each cycle vertex by an independent set of size three.

But any edge between \(A_0\) and \(A_1\) lies in at least
\[
|A_2||A_3||A_4|=27
\]
distinct \(5\)-cycles, obtained by choosing one vertex from each remaining class. This contradicts the assertion that every edge lies in exactly three.

The assumed counterexample does not exist, proving the theorem. ∎

To translate back to the requested bound:

- If \(\alpha(G)=2\), then \(n\leq2h(G)\leq2t\).
- If \(\alpha(G)=1\), then \(G\) is complete, so \(n=h(G)\leq t\).
- The empty graph is immediate.

The minor bound \(h(G)\geq n/2\) is sharp in this class: two disjoint copies of \(K_t\) have \(n=2t\), \(\alpha=2\), and \(h=t\).

## 6. What remains unresolved

The unrestricted conjecture does **not** follow from this argument.

For a smallest independence-two counterexample, the proof establishes
\[
n=2h+1,\qquad \omega(G)\leq h-1,
\]
and shows that its triangle-free complement has every nonadjacent pair joined by a common neighbor. Every edge of that complement lies in at least three \(5\)-cycles, and the argument above shows that some edge must lie in at least four.

The cutoff three is essential to the equality argument. With cutoff four, it gives only
\[
h-2\leq d_F(v)\leq h-1,
\]
rather than regularity. The proposition bounds a smallest counterexample in that class by \(20\) vertices, or \(19\) using its odd order, but no exhaustive check or further exclusion of those cases is supplied here.

Graphs with unrestricted five-cycle overlap, and the general case \(\alpha(G)\geq3\), remain untreated. I also have not verified whether this restricted theorem is already in the literature; no priority claim is intended.