```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact formula yields the sharp bound floor((2k+1)/3) for four-terminal grafts with independent nonterminals, but does not resolve the general conjecture.",
  "would_publish": false,
  "caveats": "Restricted special case; no claim of novelty or improvement of the general bound."
}
```

# 1. A sharp special case

Write
\[
\lambda(G,T)=\min\{|\delta(X)|:|X\cap T|\text{ is odd}\}
\]
and let \(\nu(G,T)\) be the maximum number of pairwise edge-disjoint \(T\)-joins.

I obtain an exact solution for the following class. The proof is self-contained; I do not claim that this special case is new.

**Theorem.** Let \(G\) be a finite loopless multigraph, let
\[
T=\{t_1,t_2,t_3,t_4\},
\]
and suppose \(V(G)\setminus T\) is independent. Then
\[
\boxed{\displaystyle
\nu(G,T)\ge
\left\lfloor\frac{2\lambda(G,T)+1}{3}\right\rfloor .}
\tag{1}
\]
For every positive integer value of \(\lambda\), equality is attained by a simple bipartite graph in this class.

Thus the conjectured inequality holds in this class with \(c=1/3\), and that constant is best possible **within this class**. An exact formula for \(\nu\) is proved below.

Subdividing an edge with a new nonterminal preserves both \(\lambda\) and \(\nu\): a join must use both subdivision edges or neither, and minimum cuts have the same value. Consequently, the theorem also covers subdivisions of graphs in the stated class.

## A four-vertex lemma

**Lemma 1.** If \(H\) is a loopless multigraph on four vertices and \(T=V(H)\), then
\[
\nu(H,T)=\delta(H).
\]

**Proof.** The upper bound follows from the four singleton \(T\)-cuts. For the lower bound, prove by induction on \(d\) that minimum degree at least \(d\) guarantees \(d\) disjoint \(T\)-joins.

If \(H\) has a perfect matching, delete it and apply induction.

Otherwise, if \(d>0\), the underlying simple graph is a spanning star. Indeed, a graph on four vertices with no isolated vertex and no perfect matching must be a star: after choosing an edge \(ab\), the other two vertices cannot be adjacent, and the absence of a perfect matching forces both to have the same sole neighbour among \(a,b\).

Choose one edge to each leaf. These three edges form a \(T\)-join. Each leaf loses one incident edge. The centre originally has degree at least \(3d\), so afterward its degree is at least
\[
3d-3\ge d-1.
\]
Induction completes the proof. \(\square\)

We will also use the following elementary pairing fact.

**Lemma 2.** Suppose objects of four types have multiplicities \(b_1,\ldots,b_4\). They can be partitioned into pairs of different types if and only if
\[
\sum_i b_i\text{ is even},
\qquad
b_i\le \sum_{j\ne i}b_j\quad\text{for every }i.
\]

**Proof.** Necessity is immediate. For sufficiency, repeatedly pair objects from the two currently largest nonempty types. If the current total is \(2s\) and every multiplicity is at most \(s\), then after this operation every multiplicity is at most \(s-1\). Induction applies. \(\square\)

# 2. An exact formula

Put \(N=V(G)\setminus T\). For \(v\in N\), define
\[
a_{vi}=|E(v,t_i)|,\qquad d_v=\sum_{i=1}^4 a_{vi},
\]
and
\[
b_{vi}=\min\{a_{vi},d_v-a_{vi}\}.
\]
Let \(d_i^0\) be the degree of \(t_i\) in \(G[T]\), and set
\[
u_i=d_i^0+\sum_{v\in N}b_{vi},
\qquad
S=\sum_{i=1}^4u_i.
\]

Call a nonterminal \(v\) **defective** if
\[
d_v\text{ is odd}
\quad\text{and}\quad
2a_{vi}<d_v\quad\text{for every }i.
\]
Let \(D\) be the set of defective vertices, and write
\[
h=|D|,
\qquad
h_i=|\{v\in D:a_{vi}=0\}|.
\]
Every defective vertex has at least three distinct terminal neighbours.

**Proposition.** Under the hypotheses of the theorem,
\[
\lambda(G,T)=\min_i u_i
\tag{2}
\]
and
\[
\boxed{\displaystyle
\nu(G,T)=
\min\left\{
\min_i u_i,\;
\left\lfloor\frac{S-h}{4}\right\rfloor,\;
\min_i\left\lfloor\frac{S-u_i-h_i}{3}\right\rfloor
\right\}.}
\tag{3}
\]

For simple graphs, the defective vertices are exactly the degree-three nonterminals. Formula (3) therefore has particularly simple data in that case.

## 2.1. Computing the minimum \(T\)-cut

A \(T\)-cut has either one or three terminals on one side. Complementing the shore, it suffices to consider cuts with
\[
X\cap T=\{t_i\}.
\]

Since \(N\) is independent, each \(v\in N\) can independently be placed inside or outside \(X\). Its contribution is respectively \(d_v-a_{vi}\) or \(a_{vi}\), with minimum \(b_{vi}\). Hence the minimum such cut has size \(u_i\), proving (2).

## 2.2. Local pairings at nonterminals

The vectors \(b_v=(b_{v1},\ldots,b_{v4})\) have the following useful properties.

* If some \(a_{vi}>d_v/2\), this index is unique, and
  \[
  b_{vi}=\sum_{j\ne i}a_{vj},\qquad b_{vj}=a_{vj}\quad(j\ne i).
  \]
  Thus \(b_v\) has even total and satisfies Lemma 2.

* If no \(a_{vi}>d_v/2\) and \(d_v\) is even, then \(b_v=a_v\), again satisfying Lemma 2.

* If \(v\) is defective, then \(b_v=a_v\). For **any** terminal neighbour \(t_i\), the vector
  \[
  b_v-\mathbf e_i
  \]
  has even total \(d_v-1\), and every entry is at most \((d_v-1)/2\). It therefore satisfies Lemma 2.

Consequently, at a nondefective vertex we can retain and pair arms with terminal multiplicities \(b_v\). At a defective vertex we can do the same after choosing one terminal neighbour at which to lose one arm.

Replace each pair of arms by an auxiliary edge between its two distinct terminals. Together with \(G[T]\), these edges form a multigraph \(H\) on the four terminals.

If \(\ell_i\) defective vertices choose to lose an arm at \(t_i\), then
\[
d_H(t_i)=u_i-\ell_i.
\tag{4}
\]
Every \(T\)-join packing in \(H\) lifts to one in \(G\): replace each auxiliary edge by its two-edge path. The paths use distinct original edges, and every nonterminal receives even degree.

## 2.3. Choosing where to lose the arms

Fix an integer \(q\ge0\). We want to assign each defective vertex \(v\) to one of its terminal neighbours, with at most
\[
u_i-q
\]
vertices assigned to \(t_i\).

This is a capacitated bipartite matching problem. Hall's condition says that, for every \(U\subseteq T\),
\[
|\{v\in D:N_G(v)\subseteq U\}|
\le \sum_{t_i\in U}(u_i-q).
\tag{5}
\]
Here the capacities must also be nonnegative.

Because every defective vertex has at least three terminal neighbours, only sets \(U\) of size three or four can give nontrivial conditions. Thus the complete list is
\[
q\le u_i\quad(1\le i\le4),
\tag{6}
\]
\[
h\le S-4q,
\tag{7}
\]
and
\[
h_i\le S-u_i-3q\quad(1\le i\le4).
\tag{8}
\]

Whenever these inequalities hold, the resulting \(H\) has minimum degree at least \(q\). Lemma 1 and lifting then produce \(q\) disjoint \(T\)-joins in \(G\). This proves the lower bound in (3).

## 2.4. Why every packing satisfies the same conditions

Let \(J_1,\ldots,J_p\) be disjoint \(T\)-joins.

Within each \(J_r\), delete pairs of parallel edges joining a nonterminal to the same terminal until at most one such edge remains. Each deletion changes two vertex degrees by two, so all joins remain \(T\)-joins and remain disjoint.

Let \(c_{vi}\) count the remaining used edges between \(v\) and \(t_i\), over all joins. Since each join has even degree at \(v\) and at most one edge there to each terminal,
\[
c_{vi}\le\sum_{j\ne i}c_{vj}.
\]
Together with the edge capacities, this gives
\[
c_{vi}\le \min\{a_{vi},d_v-a_{vi}\}=b_{vi}.
\tag{9}
\]

If \(v\) is defective, the total number of used arms at \(v\) is even, whereas \(d_v\) is odd. Some arm is therefore unused. Choose a terminal neighbour \(\sigma(v)\) with such an unused arm. Then
\[
c_{vi}\le b_{vi}-\mathbf 1_{\{\sigma(v)=i\}}.
\tag{10}
\]

Each of the \(p\) joins has positive odd degree at every terminal. Hence, writing \(\ell_i=|\sigma^{-1}(i)|\),
\[
p
\le \sum_{r=1}^p d_{J_r}(t_i)
\le d_i^0+\sum_v c_{vi}
\le u_i-\ell_i.
\]
Thus the choices \(\sigma(v)\) provide an assignment with capacities \(u_i-p\). Conditions (6)–(8) must hold for \(q=p\). This proves the reverse inequality in (3). \(\square\)

The proof is constructive: a capacitated matching, local pairings, and the decomposition in Lemma 1 find an optimal packing.

# 3. Deriving the sharp \(2/3\) bound

Let
\[
\lambda=\min_i u_i,
\qquad
q=\left\lfloor\frac{2\lambda+1}{3}\right\rfloor.
\]
We verify that all terms in (3) are at least \(q\).

## 3.1. The total-capacity term

Each defective vertex contributes at least three to \(S\), so
\[
3h\le S.
\tag{11}
\]
Also,
\[
S-h\quad\text{is even}.
\tag{12}
\]
Indeed, terminal-terminal edges contribute an even total to \(S\); every nondefective \(b_v\) has even total; and every defective \(b_v\) has odd total.

Therefore the integer \(L=(S-h)/2\) satisfies
\[
L\ge \frac S3\ge\frac{4\lambda}{3}.
\]
It follows that
\[
\left\lfloor\frac{S-h}{4}\right\rfloor
=\left\lfloor\frac L2\right\rfloor
\ge
\left\lfloor\frac{\lceil4\lambda/3\rceil}{2}\right\rfloor
=
\left\lfloor\frac{2\lambda+1}{3}\right\rfloor.
\tag{13}
\]
The last equality follows by considering \(\lambda\bmod3\).

## 3.2. The three-terminal terms

Every vector \(b_v\) satisfies
\[
b_{vi}\le\sum_{j\ne i}b_{vj}.
\]
A defective vertex missing \(t_i\) contributes at least three to
\[
\sum_{j\ne i}b_{vj}-b_{vi}.
\]
Terminal-terminal edges also contribute nonnegatively to the analogous difference. Consequently,
\[
S-2u_i\ge3h_i.
\tag{14}
\]

Writing \(A_i=S-u_i=\sum_{j\ne i}u_j\), we get
\[
\frac{S-u_i-h_i}{3}
\ge \frac{2A_i+u_i}{9}
\ge \frac{7\lambda}{9}.
\tag{15}
\]
For \(\lambda\ge3\),
\[
\frac{7\lambda}{9}\ge\frac{2\lambda+1}{3}\ge q.
\]
Also \(u_i\ge\lambda\ge q\). Formula (3) now proves (1).

For \(\lambda=0\), the assertion is trivial. For \(\lambda=1,2\), its right-hand side is one. Positive minimum \(T\)-cut size ensures that every component meets \(T\) evenly, which guarantees a \(T\)-join: in a rooted spanning tree of each component, include a parent edge precisely when its descendant subtree contains an odd number of terminals. This covers the remaining cases. \(\square\)

A further consequence of (3) is worth recording:

**Corollary.** If there are no defective vertices, then
\[
\nu(G,T)=\lambda(G,T).
\]
In particular, this holds in the stated class whenever every nonterminal has even degree.

# 4. Sharp examples for every minimum cut value

For nonnegative integers \(a_1,a_2,a_3,a_4\), construct a simple bipartite graph as follows:

* one side is \(T=\{t_1,t_2,t_3,t_4\}\);
* for each \(i\), add \(a_i\) nonterminals adjacent to exactly \(T\setminus\{t_i\}\).

Put \(A=\sum_i a_i\). All nonterminals are defective, and
\[
u_i=A-a_i,\qquad S=3A,\qquad h=A,\qquad h_i=a_i.
\]
Thus (2)–(3) give
\[
\boxed{\displaystyle
\lambda=A-\max_i a_i,\qquad
\nu=\min\left\{A-\max_i a_i,\left\lfloor\frac A2\right\rfloor\right\}.}
\tag{16}
\]

The packing obstruction has a direct interpretation. A degree-three nonterminal can be used by at most one join in a packing, because every join uses an even number of its incident edges. Every join needs at least two nonterminals to give all four terminals odd degree. Therefore \(\nu\le\lfloor A/2\rfloor\).

The following choices attain (1) for every positive \(\lambda\):
\[
\begin{array}{c|c|c}
\lambda &(a_1,a_2,a_3,a_4)&\nu\\ \hline
3r &(r,r,r,r)&2r\\
3r+1 &(r+1,r+1,r,r)&2r+1\\
3r+2 &(r+1,r+1,r+1,r)&2r+1.
\end{array}
\]
In particular, \(a_i=r\) gives
\[
\lambda=3r,\qquad \nu=2r,
\]
while the last row shows that \(c<1/3\) is impossible for this subclass.

# 5. For the general conjecture, \(c\ge1\) is necessary

The better additive constant above cannot extend to all grafts. The Petersen graph gives a short, fully checkable obstruction.

Use vertices \(a_i,b_i\), indexed modulo five, and edges
\[
a_i a_{i+1},\qquad b_i b_{i+2},\qquad a_i b_i,
\]
and take \(T=V(G)\).

The graph is cubic and bridgeless. Every odd-vertex cut therefore has odd size at least three, and singleton cuts have size three. Hence
\[
\lambda(G,T)=3.
\]

If there were two disjoint \(T\)-joins, each would have degree one at every vertex: two positive odd degrees must sum to at most three. Thus they would be disjoint perfect matchings.

The Petersen graph has no two disjoint perfect matchings, as follows directly from its construction. A perfect matching has an odd number of spokes \(a_i b_i\). It cannot have three: the two indices without spokes would have to be adjacent both in the outer cycle and in the inner cycle, requiring their difference to be both \(\pm1\) and \(\pm2\) modulo five. Thus it has one or five spokes.

There is one matching with five spokes, and exactly one for each choice of a single spoke. The five-spoke matching meets all the others. Among single-spoke matchings, choices at cyclic distance one share an inner edge, while choices at distance two share an outer edge. For example, choices \(0,1\) share \(b_2b_4\), and choices \(0,2\) share \(a_3a_4\); rotation and reflection cover all pairs.

Consequently,
\[
\nu(G,T)=1.
\]
Any universal inequality
\[
\nu(G,T)\ge \frac23\lambda(G,T)-c
\]
must therefore have
\[
\boxed{c\ge1.}
\]
So the proposed value \(c=1\), if valid, is best possible.

# 6. What remains unresolved

The exact formula depends essentially on two restrictions:

1. **Independent nonterminals.** Their arms can be paired independently, and minimum \(T\)-cuts are computed by four sums of local contributions. General nonterminal components couple these decisions.
2. **Exactly four terminals.** Lemma 1 makes minimum degree sufficient for packing joins in the auxiliary graph. This is false for larger terminal sets; the Petersen example already demonstrates that failure.

No extension of either step to arbitrary grafts is established here. In particular, this argument does **not** improve the general \(\lfloor k/3\rfloor\) guarantee stated in the question.

The partial result determines the exact packing number in an extremal subclass and identifies the one-unused-arm loss at cubic nonterminals as its \(2/3\) obstruction. It does not prove the uniform conjecture.