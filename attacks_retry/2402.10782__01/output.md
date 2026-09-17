```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "The path-FAS problem is NP-complete, whereas the maximum-degree-1 FAS problem is polynomial-time solvable.",
  "would_publish": true,
  "caveats": "The proof uses the standard deletion definition of a feedback arc set; novelty against later source versions and follow-up literature has not been independently checked."
}
```

# Complexity of path-FAS and matching-FAS

Let \(T\) be a tournament. A feedback arc set is a set \(F\subseteq A(T)\) such that \(T-F\) is acyclic. We identify an arc set with its underlying undirected graph when discussing degrees, paths, and undirected cycles.

## Main result

**Theorem.**
1. One can decide in \(O(n^3)\) time whether an \(n\)-vertex tournament has a feedback arc set of maximum degree at most \(1\).
2. Deciding whether a tournament has a feedback arc set whose underlying graph is a path is NP-complete.

The NP-hardness in part 2 persists even if the input is accompanied by an ordering whose backward graph has maximum degree at most \(2\).

The score-localization argument and the degree-constrained dynamic program in the supplied attempt are sound. The new ingredient is a two-state gadget that resolves the path case by a reduction from 3-SAT.

---

## 1. Orderings and feedback arc sets

For an ordering \(\pi=(v_1,\ldots,v_n)\), write
\[
B_\pi=\{v_jv_i\in A(T):i<j\}
\]
for its backward arcs.

If \(F\) is a feedback arc set and \(\pi\) is a topological ordering of \(T-F\), then
\[
B_\pi\subseteq F. \tag{1}
\]
Conversely, \(B_\pi\) is always a feedback arc set.

Consequently, for every \(d\), the following are equivalent:

- \(T\) has a feedback arc set of maximum degree at most \(d\);
- \(T\) has an ordering \(\pi\) with \(\Delta(B_\pi)\le d\).

For paths, the appropriate ordering formulation uses **linear forests**, meaning disjoint unions of paths and isolated vertices.

**Lemma 1.** For a tournament with at least two vertices, the following are equivalent:
1. \(T\) has a path-FAS;
2. \(T\) has an ordering \(\pi\) for which \(B_\pi\) is a linear forest.

**Proof.** If \(F\) is a path-FAS, take a topological ordering of \(T-F\). By (1), its backward graph is a subgraph of a path, hence a linear forest.

Conversely, suppose \(B_\pi\) is a linear forest. Concatenate its path components, including isolated vertices as singleton components, into a spanning undirected path \(P\). This is possible because the underlying graph of a tournament is complete. Let \(F\) consist of the tournament arcs corresponding to the edges of \(P\). Then \(B_\pi\subseteq F\), so \(T-F\) is a subdigraph of the acyclic digraph \(T-B_\pi\). Thus \(F\) is a path-FAS. ∎

The finitely many smaller inputs can be handled directly according to the chosen convention for an empty path.

---

## 2. Score localization and forced backward arcs

For \(v\in V(T)\), define
\[
a(v)=n-d_T^+(v).
\]

Suppose that \(v\) occupies position \(i\) in an ordering \(\pi\). Let \(L\) be the number of backward arcs from \(v\) to earlier vertices, and \(R\) the number of backward arcs from later vertices into \(v\). Then
\[
d_T^+(v)=n-i+L-R,
\]
and hence
\[
a(v)=i-L+R.
\]
Therefore
\[
\bigl|\operatorname{pos}_\pi(v)-a(v)\bigr|
   \le d_{B_\pi}(v). \tag{2}
\]

In particular, for any two orderings \(\pi,\sigma\),
\[
\bigl|\operatorname{pos}_\pi(v)-\operatorname{pos}_\sigma(v)\bigr|
 \le d_{B_\pi}(v)+d_{B_\sigma}(v). \tag{3}
\]

We will use (3) to force selected long arcs to remain backward. If
\[
\Delta(B_\sigma)\le3,\qquad \Delta(B_\pi)\le2,
\]
then every vertex moves at most five positions between \(\sigma\) and \(\pi\). Thus two vertices more than ten positions apart in \(\sigma\) cannot change their relative order.

---

## 3. A tournament with exactly two matching-FAS choices

For odd \(m=2k+1\ge5\), define a tournament \(U_m\) on
\[
z_0,z_1,\ldots,z_{m-1}
\]
as follows:
\[
z_{i+1}\to z_i \quad(0\le i<m-1),
\]
while
\[
z_i\to z_j \quad\text{whenever }j\ge i+2.
\]
Thus the backward graph in the displayed order is precisely the path
\[
z_0-z_1-\cdots-z_{m-1}.
\]

Define its two alternating matchings
\[
M_0=\{z_0z_1,z_2z_3,\ldots,z_{m-3}z_{m-2}\},
\]
and
\[
M_1=\{z_1z_2,z_3z_4,\ldots,z_{m-2}z_{m-1}\}.
\]

**Lemma 2.** The only matching feedback arc sets of \(U_m\) are \(M_0\) and \(M_1\). Moreover, each is the backward graph of an ordering of \(U_m\).

**Proof.** Let \(F\) be a matching feedback arc set. For every \(0\le i\le m-3\), the triple
\[
D_i=\{z_i,z_{i+1},z_{i+2}\}
\]
induces a directed triangle. Therefore \(F\) contains an edge of each \(D_i\).

We first exclude every edge \(z_i z_{i+2}\) from \(F\).

- Suppose \(1\le i\le m-4\) and \(z_i z_{i+2}\in F\). Since \(F\) is a matching, hitting \(D_{i-1}\) forces
  \[
  z_{i-1}z_{i+1}\in F,
  \]
  while hitting \(D_{i+1}\) forces
  \[
  z_{i+1}z_{i+3}\in F.
  \]
  These two edges intersect, a contradiction.

- Suppose \(z_0z_2\in F\). Hitting \(D_1\) then forces \(z_1z_3\in F\). But every edge of \(D_2\) meets \(z_2\) or \(z_3\), both already matched outside \(D_2\). Thus \(D_2\) cannot be hit. Here \(m\ge5\) ensures that \(D_2\) exists.

- The case \(z_{m-3}z_{m-1}\in F\) is identical with the indices reversed.

Now let \(e_i=z_i z_{i+1}\). Since the third edge of \(D_i\) is excluded, \(F\) contains at least one of \(e_i,e_{i+1}\). It cannot contain both, since they intersect. Thus membership in \(F\) alternates along
\[
e_0,e_1,\ldots,e_{m-2}.
\]
It follows that \(F\) contains \(M_0\) or \(M_1\).

Each of these matchings covers \(m-1\) vertices. There is therefore no room for any additional edge in the matching \(F\), proving that \(F=M_0\) or \(F=M_1\).

Finally, to realize \(M_t\) as a backward graph, start with the displayed order and swap each adjacent pair belonging to \(M_{1-t}\). These swaps reverse exactly those pairs and no others. The backward graph becomes \(M_t\). ∎

The usefulness of this gadget is that a single binary choice controls arbitrarily many designated edges.

---

## 4. NP-completeness for paths

We reduce from 3-SAT with three distinct variables in each clause. This standard restriction remains NP-complete: repeated literals and tautological clauses can be removed, and shorter clauses can be padded using fresh variables. For example,
\[
(\ell_1\vee\ell_2)
\]
is replaced by
\[
(\ell_1\vee\ell_2\vee y)\wedge
(\ell_1\vee\ell_2\vee\neg y),
\]
and a unit clause can be replaced by the four corresponding clauses using two fresh variables.

Let \(\Phi\) be such a formula. Discard variables with no occurrences.

### 4.1 Variable gadgets and occurrence ports

For every variable \(x\), construct an odd-sized gadget \(U_{m_x}\), with \(m_x\ge5\).

Each occurrence \(o\) of \(x\) receives two consecutive vertices
\[
a_o=z_j,\qquad b_o=z_{j+1}.
\]
All vertices not used as occurrence ports will be called **buffers**. Arrange the list so that:

1. every occurrence pair is immediately preceded and immediately followed by a buffer;
2. the first and last vertices are buffers;
3. \(j\) is even for a positive occurrence \(x\), and odd for a negative occurrence \(\neg x\).

Such a list of length \(O(q_x)\), where \(q_x\) is the number of occurrences of \(x\), is easy to construct. Begin with a buffer. Before appending each occurrence pair, insert zero or one additional buffer to obtain the required starting parity, and append a buffer after the pair. Finally, append buffers if necessary to make the total length odd and at least five.

Interpret state \(M_t\), for \(t\in\{0,1\}\), as assigning \(x=t\). Then
\[
a_ob_o\in M_t
\quad\Longleftrightarrow\quad
\text{the literal at occurrence }o\text{ is false}. \tag{4}
\]

Furthermore, when \(a_ob_o\notin M_t\), each of \(a_o,b_o\) is matched by \(M_t\) to its adjacent buffer. This follows directly from the alternating matching pattern and the buffers on both sides.

### 4.2 The wire matching

Construct an undirected matching \(W\) as follows.

For every clause with occurrences \(o_1,o_2,o_3\), put into \(W\) the three edges
\[
b_{o_1}a_{o_2},\qquad
b_{o_2}a_{o_3},\qquad
b_{o_3}a_{o_1}. \tag{5}
\]
Thus, if all three occurrence-pair edges were present, they would form the six-cycle
\[
a_{o_1}-b_{o_1}-a_{o_2}-b_{o_2}
-a_{o_3}-b_{o_3}-a_{o_1}. \tag{6}
\]

For every buffer \(z\), create a new private vertex \(\lambda_z\), and put
\[
z\lambda_z
\]
into \(W\).

Every vertex of every variable gadget is now incident with exactly one edge of \(W\). Each private vertex is also incident with exactly one such edge. Hence \(W\) is indeed a matching.

Importantly, every clause wire joins different variable gadgets, because the three variables of a clause are distinct.

### 4.3 Assembling the tournament

Choose any order of the variable gadgets, followed by one block containing all private vertices. Insert twelve new padding vertices between every two consecutive blocks.

Let \(\sigma\) be the resulting reference ordering, using the natural order \(z_0,\ldots,z_{m_x-1}\) inside each variable gadget.

Orient the tournament as follows:

- each variable gadget induces its prescribed \(U_{m_x}\);
- every edge of \(W\) is oriented backward in \(\sigma\);
- every remaining pair is oriented forward in \(\sigma\).

These rules are consistent because no edge of \(W\) has both endpoints in a variable gadget.

The backward graph of \(\sigma\) consists exactly of \(W\) together with the natural path inside each variable gadget. Therefore
\[
\Delta(B_\sigma)\le3. \tag{7}
\]

Every wire joins distinct blocks, so its endpoints are at least thirteen positions apart in \(\sigma\).

The construction has \(O(|V(\Phi)|+|\Phi|)\) vertices and is polynomial-time.

### 4.4 Every linear-forest ordering gives a satisfying assignment

Suppose that \(T\) has an ordering \(\pi\) for which \(B_\pi\) is a linear forest. Then
\[
\Delta(B_\pi)\le2.
\]
By (3) and (7),
\[
\bigl|\operatorname{pos}_\pi(v)-\operatorname{pos}_\sigma(v)\bigr|\le5
\]
for every vertex.

Since the endpoints of every wire are at least thirteen positions apart in \(\sigma\), their relative order cannot change. Consequently,
\[
W\subseteq B_\pi. \tag{8}
\]

Every variable-gadget vertex already has one incident backward wire. Its backward degree inside its own gadget is therefore at most one. Restricting \(\pi\) to that gadget gives a matching backward graph, so Lemma 2 forces it to be exactly \(M_0\) or \(M_1\).

Use these states as the truth assignment.

If a clause were unsatisfied, all three of its occurrence-pair edges would belong to \(B_\pi\), by (4). Together with its three mandatory wires from (8), these edges form the undirected six-cycle (6). This contradicts the assumption that \(B_\pi\) is a linear forest.

Thus \(\Phi\) is satisfiable.

### 4.5 Every satisfying assignment gives a linear-forest ordering

Conversely, suppose that \(\Phi\) has a satisfying assignment.

Keep the blocks, padding vertices, and private vertices in their reference order. Within each variable gadget, use the ordering from Lemma 2 whose backward graph is the matching corresponding to its assigned truth value.

For the resulting ordering \(\pi\),
\[
B_\pi=W\ \cup\ \bigcup_x M_{t_x}. \tag{9}
\]
Indeed, the internal backward graphs are the selected matchings, and all relative orders between distinct blocks remain unchanged.

Both parts of (9) are matchings, so
\[
\Delta(B_\pi)\le2.
\]

We show that \(B_\pi\) has no undirected cycle.

- A private vertex \(\lambda_z\) has degree one, so no cycle contains it.
- A buffer \(z\) has its wire to \(\lambda_z\) and at most one other incident edge. Therefore no cycle can contain \(z\), either.
- Padding vertices are isolated.

Thus every possible cycle must lie entirely on occurrence ports. On these vertices, the only edges are:

1. the clause wires in (5);
2. the occurrence-pair edges corresponding to false literals.

There are no matching edges between different occurrence pairs, because buffers separate them. Therefore the port-induced graph is a disjoint union, over clauses, of subgraphs of the six-cycles (6).

Each clause is satisfied, so at least one of its three occurrence-pair edges is absent. Every such subgraph is consequently a forest. Hence \(B_\pi\) is a linear forest.

By Lemma 1, \(T\) has a path-FAS.

We have proved
\[
\Phi\text{ is satisfiable}
\quad\Longleftrightarrow\quad
T\text{ has a path-FAS}. \tag{10}
\]

### 4.6 NP membership and the stronger promise

By Lemma 1, an ordering whose backward graph is a linear forest is a polynomially checkable certificate. Thus path-FAS is in NP, and (10) proves NP-completeness.

Moreover, any assignment—not necessarily satisfying—produces the ordering in (9), whose backward graph has maximum degree at most two. The reduction can supply, for example, the ordering obtained by assigning every variable false. Hence the hardness persists when such a degree-two ordering is supplied with the input.

---

## 5. Polynomial-time recognition for matching-FAS

For completeness, here is a verified version of the degree-constrained dynamic program. It proves the more general bound
\[
O(2^{4d}n^3)
\]
for deciding whether \(\Delta(B_\pi)\le d\) is possible.

### 5.1 Position intervals

By (2), every acceptable ordering must put \(v\) in
\[
I_v=[\ell(v),r(v)]
 =
[\max\{1,a(v)-d\},\min\{n,a(v)+d\}]. \tag{11}
\]

For a cut after position \(i\), define
\[
D_i=\{v:r(v)\le i\},
\qquad
X_i=\{v:\ell(v)\le i<r(v)\}.
\]

Every prefix set \(S\) of size \(i\) in a complete interval-respecting ordering has the form
\[
S=D_i\cup Y,\qquad Y\subseteq X_i. \tag{12}
\]

There is a useful rejection rule:
\[
|X_i|>4d \quad\Longrightarrow\quad
\text{no interval-respecting ordering exists}. \tag{13}
\]

To prove it, suppose \(v\in X_i\), where \(1\le i<n\). Then
\[
i-d<a(v)\le i+d.
\]
Consequently its entire interval \(I_v\) lies in
\[
[i-2d+1,i+2d],
\]
which contains at most \(4d\) positions. All vertices of \(X_i\) would have to occupy distinct positions in this common range. This proves (13).

After applying this rejection rule, there are at most \(2^{4d}\) possible prefix sets at each layer.

### 5.2 States and transitions

A state at layer \(i\) is a reachable set
\[
S=D_i\cup Y,\qquad Y\subseteq X_i,\qquad |S|=i.
\]

For \(v\notin S\), define
\[
\beta(v,S)
=
|\{u\in S:v\to u\}|
+
|\{w\notin S\cup\{v\}:w\to v\}|. \tag{14}
\]

If \(v\) is placed next, this is its total backward degree in every completion: the first term counts its backward arcs to the prefix, and the second its backward arcs from the remaining vertices.

Allow the transition
\[
S\longrightarrow S'=S\cup\{v\}
\]
if:

1. \(i+1\in I_v\);
2. \(\beta(v,S)\le d\);
3. \(S'\) has the required state form at layer \(i+1\), namely
   \[
   D_{i+1}\subseteq S'\subseteq D_{i+1}\cup X_{i+1}.
   \]

Start from the empty set and accept if the state \(V(T)\) is reachable.

### 5.3 Correctness

When a vertex is placed, (14) determines its final backward degree independently of the internal order of the existing prefix and of the future order of the unplaced vertices. Thus an already verified vertex never needs to be reconsidered.

A path through the state graph from the empty set to \(V(T)\) therefore gives an ordering in which every vertex has backward degree at most \(d\).

Conversely, any ordering satisfying that degree bound respects (11), is not eliminated by (13), and follows permitted transitions through all its prefix sets.

This also explains why histories with the same prefix set may safely be merged.

There are at most \(n2^{4d}\) states. Trying all \(n\) candidate next vertices and evaluating (14) naively in \(O(n)\) time gives
\[
O(2^{4d}n^3)
\]
time. Back-pointers recover an ordering and hence the required feedback arc set.

Taking \(d=1\) proves the \(O(n^3)\) matching-FAS result.

---

## 6. Conclusion and scope

Under the feedback-arc-set definition in the question, the two cases have different complexity:

\[
\boxed{\text{Matching-FAS is in P}}
\qquad\text{and}\qquad
\boxed{\text{Path-FAS is NP-complete}.}
\]

The path reduction also identifies exactly why the degree-two relaxation does not resolve the problem: its instances always have degree-two backward orderings, while excluding their undirected cycles encodes 3-SAT.

No unresolved mathematical case remains in the argument above. The outstanding caveat is bibliographic: I have not independently checked whether these classifications or arguments appear in a later version of the source or in follow-up work.