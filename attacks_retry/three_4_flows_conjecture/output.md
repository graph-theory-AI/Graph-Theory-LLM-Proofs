```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A different partition gives three 3-flow complements for the cycle-doubling class, including all flower snarks, but the full conjecture remains unresolved.",
  "would_publish": false,
  "caveats": "Novelty has not been checked; the stronger 2,3,3 statement in the supplied discussion is false under its literal disjoint-partition interpretation."
}
```

# 1. Results obtained

I do not prove or disprove the original three \(4\)-flows conjecture.

I obtain three precise results:

1. **An improvement for the previous construction.** If a cubic graph is obtained by doubling vertex-disjoint cycles of a \(3\)-edge-colourable cubic graph, then its edges admit a partition whose three complements all have nowhere-zero **\(3\)-flows**. In particular, this holds for every flower snark.
2. **An unconditional four-part bound.** Every bridgeless graph has a partition into four sets whose complements admit nowhere-zero \(2,3,3,3\)-flows, respectively.
3. **A correction to the supplied context.** The Petersen graph does **not** admit the stated \(2,3,3\) decomposition. This does not contradict the original conjecture: the Petersen graph does admit a \(3,3,3\) decomposition.

Throughout, graphs are finite. A nowhere-zero integer \(k\)-flow is an integer circulation with
\[
0<|f(e)|<k
\]
on every edge of the graph under consideration. Isolated vertices are harmless.

# 2. Three \(3\)-flows for the cycle-doubling construction

The subdivision argument in the previous attempt is sound. The following improvement uses the same construction but a **different edge partition**.

## Theorem 1

Let \(H\) be a loopless cubic graph with a proper \(3\)-edge-colouring
\[
c:E(H)\longrightarrow \{1,2,3\},
\]
and let \(F\) be a union of vertex-disjoint cycles in \(H\).

Construct \(D=D(H,F)\) as follows:

- retain all original vertices;
- retain the edges outside \(F\);
- for each \(v\in V(F)\), introduce \(v^+,v^-\) and the spokes \(vv^+,vv^-\);
- replace each edge \(uv\in E(F)\) by
  \[
  u^+v^-,\qquad u^-v^+.
  \]

Then \(E(D)\) has a partition \(A_1,A_2,A_3\) such that every \(D\setminus A_i\) has a nowhere-zero \(3\)-flow.

### The partition

For \(v\in V(F)\), let \(m_v\) be its unique incident edge outside \(F\). Colour the edges of \(D\) as follows:

- a retained edge \(e\notin E(F)\) receives colour \(c(e)\);
- both copies of \(e\in E(F)\) receive colour \(c(e)\);
- both spokes \(vv^+,vv^-\) receive colour \(c(m_v)\).

Let \(A_i\) be the set of edges receiving colour \(i\).

Notice the local structure:

- an original vertex on \(F\) is monochromatic;
- every new vertex \(v^\pm\) is incident with all three colours;
- an original vertex outside \(F\) is still incident with all three colours.

### Construction of the flows

Fix \(i\in\{1,2,3\}\). The bichromatic subgraph
\[
H_i=H\setminus c^{-1}(i)
\]
is a \(2\)-factor. Orient each of its cycles cyclically.

We define a flow on \(D\setminus A_i\):

1. Every retained edge of \(H_i\setminus F\) receives value \(2\), with its orientation from \(H_i\).
2. Both copies of every edge of \(H_i\cap F\) receive value \(1\), oriented according to the corresponding edge of \(H_i\).
3. If \(c(m_v)\ne i\), both spokes at \(v\) are present. Give them value \(1\), oriented:
   - away from \(v\) if \(m_v\) is directed into \(v\);
   - towards \(v\) if \(m_v\) is directed away from \(v\).

All present edges have now received a value in \(\{1,2\}\).

### Verification of conservation

There are four cases.

**Original vertex outside \(F\).**  
Exactly two incident edges remain. They inherit opposite directions from \(H_i\), and both have value \(2\).

**Original vertex \(v\in V(F)\) with \(c(m_v)=i\).**  
Its three incident edges in \(D\) all have colour \(i\), so it is isolated in \(D\setminus A_i\).

**Original vertex \(v\in V(F)\) with \(c(m_v)\ne i\).**  
The edge \(m_v\) has value \(2\), while the two spokes have value \(1\) and point in the opposite direction. Thus conservation is \(2=1+1\).

**New vertex \(v^\pm\).**

- If \(c(m_v)=i\), its spoke is absent. Both incident copied edges remain, with one entering and one leaving, each of value \(1\).
- If \(c(m_v)\ne i\), exactly one copied edge remains, together with the spoke. Their directions are opposite, and both have value \(1\).

Consequently, the assignment is a nowhere-zero \(3\)-flow on \(D\setminus A_i\). This works independently for all three \(i\). \(\square\)

The graph \(D\) is cubic. It is also automatically bridgeless: every edge belongs to two of the flow-supporting complements, whereas an edge that is a bridge in \(D\) cannot carry a nonzero circulation in any subgraph of \(D\).

# 3. Explicit application to all flower snarks

For odd \(n\ge5\), write the flower graph \(J_n\) with vertices
\[
a_i,b_i,c_i,d_i\qquad(0\le i<n),
\]
spokes
\[
a_ib_i,\quad a_ic_i,\quad a_id_i,
\]
and tracks
\[
b_0b_1\cdots b_{n-1}b_0
\]
and
\[
c_0c_1\cdots c_{n-1}d_0d_1\cdots d_{n-1}c_0.
\]

Here is an explicit partition, given as a three-colouring of the edges.

- All three spokes at \(a_0\) receive colour \(2\).
- All three spokes at \(a_{n-1}\) receive colour \(1\).
- All three spokes at every other \(a_i\) receive colour \(3\).
- For \(0\le i\le n-2\), the three edges
  \[
  b_ib_{i+1},\quad c_ic_{i+1},\quad d_id_{i+1}
  \]
  receive colour \(1\) when \(i\) is even and colour \(2\) when \(i\) is odd.
- The three closing edges
  \[
  b_{n-1}b_0,\quad c_{n-1}d_0,\quad d_{n-1}c_0
  \]
  receive colour \(3\).

Let \(A_j\) consist of the edges of colour \(j\).

## Corollary 2

Each of
\[
J_n\setminus A_1,\qquad J_n\setminus A_2,\qquad J_n\setminus A_3
\]
has a nowhere-zero \(3\)-flow.

### Proof

Take the prism \(H_n\) on vertices \(a_i,b_i\), with its two \(n\)-cycles and rungs \(a_ib_i\). Give both horizontal edges between positions \(i\) and \(i+1\) alternating colours \(1,2\), for \(0\le i\le n-2\), and give the two closing horizontal edges colour \(3\). Give the rungs at positions \(0,n-1\) colours \(2,1\), respectively, and all other rungs colour \(3\).

Because \(n\) is odd, this is a proper \(3\)-edge-colouring.

Apply Theorem 1 with \(F\) equal to the \(a\)-cycle. Identify
\[
(c_i,d_i)=
\begin{cases}
(a_i^+,a_i^-),&i\text{ even},\\
(a_i^-,a_i^+),&i\text{ odd}.
\end{cases}
\]
The doubled edges become the stated twisted \(c,d\)-track, and the partition is exactly the one above. The flow construction in Theorem 1 supplies the certificates. \(\square\)

This improves the largest flow bound in the previous flower-snark result from \(4\) to \(3\). It does **not** preserve the previous partition’s \(2\)-flow complement.

The construction also includes the Petersen graph:
\[
P\cong D(K_4,F),
\]
where \(F\) is a triangle of \(K_4\). Thus the Petersen graph itself has a \(3,3,3\) decomposition.

# 4. An unconditional four-part analogue

The following general bound uses the classical six-flow theorem, not an unproved conjecture.

## Theorem 3

Every bridgeless graph \(G\) has an edge partition
\[
A_\infty,A_0,A_1,A_2
\]
such that \(G\setminus A_\infty\) has a nowhere-zero \(2\)-flow and each \(G\setminus A_t\), \(t\in\{0,1,2\}\), has a nowhere-zero \(3\)-flow.

### Proof

Take a nowhere-zero integer \(6\)-flow \(f\), relative to a fixed orientation. Thus
\[
f(e)\in\{\pm1,\pm2,\pm3,\pm4,\pm5\}.
\]

Let
\[
C=\{e:f(e)\text{ is odd}\}.
\]
Reducing conservation modulo \(2\) shows that \(C\) is an even subgraph. Choose an Eulerian orientation of \(C\), giving an integer circulation \(g\) with
\[
g(e)\in\{-1,1\}\quad(e\in C),\qquad g(e)=0\quad(e\notin C).
\]

Over \(\mathbb F_3\), put
\[
h=f\bmod3,\qquad s=g\bmod3.
\]
The pair \((h,s)\) is nowhere zero:

- on \(C\), \(s\ne0\);
- outside \(C\), \(f(e)\in\{\pm2,\pm4\}\), so \(h(e)\ne0\).

Define
\[
A_\infty=\{e:s(e)=0\},
\qquad
A_t=\{e:h(e)-t\,s(e)=0\}\quad(t\in\mathbb F_3).
\]
These sets partition \(E(G)\): when \(s(e)\ne0\), precisely one value of \(t\) satisfies \(h(e)=t\,s(e)\).

Now \(G\setminus A_\infty=C\), which has the \(2\)-flow \(g\). For each finite \(t\), the circulation
\[
h-ts
\]
is a nowhere-zero \(\mathbb Z_3\)-flow on \(G\setminus A_t\).

For completeness, such a modular flow lifts to a nowhere-zero integer \(3\)-flow. Choose representatives \(r(e)\in\{1,2\}\), and let \(B\) be the oriented incidence matrix. Then
\[
Br=3b
\]
for an integer vector \(b\). The bounded system
\[
Bx=b,\qquad 0\le x\le1
\]
has the fractional solution \(x=r/3\), and it has an integral solution. One elementary justification is to round along cycles of fractional edges: a nonempty fractional-edge subgraph cannot have a vertex incident with exactly one fractional edge, because its prescribed divergence is integral. Hence it contains a cycle, along which one can adjust until another variable becomes integral.

For an integral solution \(x\),
\[
r-3x
\]
is a circulation with values in \(\{-2,-1,1,2\}\). This is the required integer \(3\)-flow. \(\square\)

This is a genuine nearby bound, but it does not justify merging two parts. Removing their union can create a degree-one vertex or a bridge.

# 5. The quoted \(2,3,3\) strengthening fails for the Petersen graph

The supplied discussion claims that the Petersen graph has a partition \(A,B_1,B_2\) such that
\[
P\setminus A\text{ has a }2\text{-flow},\qquad
P\setminus B_1,\ P\setminus B_2\text{ have }3\text{-flows}.
\]
Under the literal disjoint-partition interpretation, this is false.

## Proposition 4

The Petersen graph has no such \(2,3,3\) decomposition.

### Preliminary facts about the Petersen graph

We use three elementary properties.

1. It has girth \(5\).
2. Any two nonadjacent vertices have a common neighbour.
3. Every \(2\)-factor consists of two \(5\)-cycles.

The first two follow directly from the model whose vertices are the \(2\)-subsets of a \(5\)-set, with adjacency meaning disjointness.

Here is a verification of the third. In the usual outer–inner notation, let the outer edges be \(u_iu_{i+1}\), the inner edges \(v_iv_{i+2}\), and the spokes \(u_iv_i\), with indices modulo \(5\). A perfect matching contains an odd number of spokes.

It cannot contain exactly three: the two unmatched outer indices would have to differ by \(\pm1\), while the same two inner indices would have to differ by \(\pm2\). Five spokes give the two obvious \(5\)-cycles as complement. With exactly one spoke, rotation permits taking it to be \(u_0v_0\); the remaining matching edges are forced, and the complementary cycles are
\[
u_0u_1v_1v_4u_4u_0
\]
and
\[
v_0v_2u_2u_3v_3v_0.
\]
Thus every perfect-matching complement consists of two \(5\)-cycles. In particular, \(P\) is not Hamiltonian.

We also use the elementary fact that a cubic graph with a nowhere-zero \(3\)-flow is bipartite. Indeed, after reduction modulo \(3\) and suitable edge reversals, every edge has value \(1\); conservation at a cubic vertex forces all three edges to point in or all three to point out.

### Form forced by a \(2,3,3\) partition

Suppose such a partition exists, and put
\[
T=P\setminus A=B_1\cup B_2.
\]
Because \(T\) has a nowhere-zero \(2\)-flow, every vertex of \(T\) has even degree. Since \(P\) is cubic, its nontrivial components are vertex-disjoint cycles.

At a vertex of \(T\), the two incident edges of \(T\) must belong to different \(B_i\). Otherwise deleting one \(B_i\) leaves degree one at that vertex, precluding a nowhere-zero flow. Consequently, every cycle of \(T\) is even, with \(B_1,B_2\) alternating.

The subgraph \(T\) cannot be empty, since \(P\) itself has no \(3\)-flow. Girth \(5\), order \(10\), and non-Hamiltonicity therefore leave only two possibilities: \(T\) is a \(6\)-cycle or an \(8\)-cycle.

### Case 1: \(T\) is a \(6\)-cycle

There is no chord of \(T\), since a chord would create a triangle or a \(4\)-cycle. The four vertices outside \(T\) consequently induce a tree with three edges.

That tree cannot be a path. Its endpoints would have a common neighbour outside the path, hence on \(T\); this would give a cycle vertex two neighbours outside \(T\), impossible in a cubic graph. Thus the outside tree is a claw.

Call its leaves \(a,b,c\). Each leaf has two neighbours on \(T\), and girth \(5\) forces these neighbours to be opposite on the \(6\)-cycle. The attachment sequence around \(T\) is therefore
\[
a,b,c,a,b,c.
\]

Delete either alternating matching of \(T\), and suppress the resulting degree-two vertices of \(T\). The three remaining cycle edges produce the triangle \(ab,bc,ca\), while the outside claw remains. The suppressed graph is \(K_4\).

Suppression preserves the existence of a nowhere-zero \(3\)-flow, but \(K_4\) is cubic and nonbipartite. Hence neither required complement has a \(3\)-flow.

### Case 2: \(T\) is an \(8\)-cycle

Let \(u,v\) be the two vertices outside \(T\). They must be adjacent: otherwise a common neighbour on \(T\) would have two neighbours outside the cycle.

Let \(Q\) be either alternating matching of \(T\). Then
\[
Q\cup\{uv\}
\]
is a perfect matching of \(P\), so its complement consists of two \(5\)-cycles.

The endpoints of \(uv\) lie on different complementary cycles. If they lay on the same \(5\)-cycle, \(uv\) would be a chord and would create a triangle. Therefore
\[
P\setminus Q
\]
is precisely two \(5\)-cycles joined by the bridge \(uv\). It has no nowhere-zero flow.

Both cases are impossible. \(\square\)

Thus the \(2,3,3,3\) bound in Theorem 3 cannot generally be reduced to \(2,3,3\). Also, the previous \(2,4,4\) certificate and the new \(3,3,3\) certificate cannot simply be combined: Petersen already prevents that inference.

# 6. What remains open in this attack

The cycle-doubling theorem gives complete, explicit certificates for a nontrivial infinite class, including every flower snark and the Petersen graph. It lowers all three flow bounds to \(3\), although with a different partition from the previous attempt.

The general argument gives four complements, not three. No operation has been established that converts its four-part partition into the three-part partition required by the original conjecture. Nor is there a reason established here that an arbitrary cubic snark has the cycle-doubling structure.

Accordingly, the original three \(4\)-flows conjecture remains unresolved by these arguments.