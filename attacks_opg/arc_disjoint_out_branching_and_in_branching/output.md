```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For complete independent blow-ups with every part of size at least two, k=3 suffices and is sharp for prescribed roots.",
  "would_publish": false,
  "caveats": "This is a structural special case, not a resolution for arbitrary digraphs; novelty is not claimed."
}
```

# A sharp special case

I do not resolve the general conjecture. I prove a sufficient condition for a structured class, together with an explicit six-vertex obstruction to \(k=2\) when the roots are prescribed.

For a digraph \(D\), write
\[
\delta_D^+(X)=\{xy\in A(D):x\in X,\ y\notin X\}.
\]
Thus \(D\) is \(k\)-arc-strong if every nonempty proper \(X\subset V(D)\) satisfies \(|\delta_D^+(X)|\ge k\).

A **complete independent blow-up** of a loopless simple digraph \(H\) is obtained by replacing each vertex \(x\) by a nonempty independent set \(V_x\), and replacing every arc \(xy\) by all arcs from \(V_x\) to \(V_y\). There are no other arcs.

## Theorem

Let \(H\) be a strongly connected loopless simple digraph with at least two vertices. Let \(D\) be a complete independent blow-up of \(H\), with
\[
|V_x|\ge 2\qquad\text{for every }x\in V(H).
\]

If \(D\) is \(3\)-arc-strong, then \(D\) contains two arc-disjoint strongly connected spanning subdigraphs. Consequently, for every prescribed \(u,v\in V(D)\), it contains an out-branching rooted at \(u\) and an arc-disjoint in-branching rooted at \(v\).

The constant \(3\) is best possible for this class. The obstruction at \(2\) can be chosen to have six vertices, to be Eulerian and Hamiltonian, and to have independence number \(2\).

The proof is self-contained.

# 1. A construction using two or three copies of each vertex

## 1.1 A lifting lemma

Let \(q\in\{2,3\}\), and select \(q\) vertices
\[
x_0,\ldots,x_{q-1}
\]
from each part \(V_x\), with subscripts interpreted in \(\mathbb Z_q\).

For a function
\[
a:A(H)\longrightarrow \mathbb Z_q,
\]
define a spanning subdigraph \(L(a)\) on these selected vertices by including
\[
x_i y_{i+a(xy)}
\qquad
(xy\in A(H),\ i\in\mathbb Z_q).
\]

**Lemma.** If \(H\) has a directed cycle \(C\) such that
\[
\sum_{e\in A(C)}a(e)\ne 0\pmod q,
\]
then \(L(a)\) is strongly connected.

**Proof.** Fix \(c\in V(C)\). Traversing a lift of \(C\) changes the subscript at \(c\) by
\[
s=\sum_{e\in A(C)}a(e).
\]
Because \(q\) is prime and \(s\ne0\), repeated traversals reach all \(q\) copies of \(c\). Those copies therefore lie in one strong component.

For any \(x\in V(H)\), choose directed paths from \(c\) to \(x\) and from \(x\) to \(c\). Lifting the first path from the different copies of \(c\) reaches every copy of \(x\), while lifting the second takes every copy of \(x\) to a copy of \(c\). Hence all selected vertices lie in one strong component. \(\square\)

Also, if
\[
a(e)\ne b(e)\quad\text{for every }e\in A(H),
\]
then \(L(a)\) and \(L(b)\) are arc-disjoint.

## 1.2 Two copies suffice unless the base is an odd directed cycle

Suppose \(H\) is not itself a directed odd cycle. I construct two arc-disjoint strong spanning subdigraphs using two selected vertices per part.

All arithmetic here is in \(\mathbb Z_2\).

### Case A: \(H\) contains an even directed cycle

Choose such a cycle \(C\) and an arc \(e\in A(C)\). Set
\[
a(e)=1,\qquad a(f)=0\quad(f\ne e),
\]
and set \(b(f)=1-a(f)\) for every arc \(f\).

Then
\[
\sum_C a=1,\qquad
\sum_C b=|A(C)|-1=1\pmod2.
\]
The lifting lemma makes both \(L(a)\) and \(L(b)\) strong, and they are arc-disjoint.

### Case B: every directed cycle of \(H\) is odd

Since \(H\) is strong but is not itself a directed cycle, it has two distinct simple directed cycles \(C_1,C_2\). Indeed, every arc of a strong digraph belongs to a directed cycle, so a strong digraph with only one directed cycle is exactly that cycle.

Choose
\[
e\in A(C_1)\setminus A(C_2).
\]
Such an arc exists because distinct simple directed cycles cannot have one arc set properly contained in the other.

Again set \(a(e)=1\), set \(a=0\) elsewhere, and let \(b=1-a\). Then
\[
\sum_{C_1}a=1,\qquad
\sum_{C_2}b=|A(C_2)|=1\pmod2.
\]
Thus both lifts are strong and arc-disjoint.

This proves:

> If \(H\) is not a directed odd cycle, two selected vertices per part support two arc-disjoint strong spanning subdigraphs.

## 1.3 Three copies always suffice

Now use \(\mathbb Z_3\), and let \(H\) be any strongly connected base of order at least two.

Choose a simple directed cycle \(C\), of length \(\ell\), and an arc \(e\in A(C)\). Define
\[
a(e)=1,\qquad a(f)=0\quad(f\ne e).
\]
Initially define
\[
b(e)=0,\qquad b(f)=1\quad(f\ne e).
\]

We have
\[
\sum_C a=1,\qquad \sum_C b=\ell-1\pmod3.
\]
If the second sum is zero, choose another arc \(f\in A(C)\setminus\{e\}\) and change \(b(f)\) from \(1\) to \(2\). The sum on \(C\) then becomes \(1\).

In either case both cycle sums are nonzero, and
\[
a(g)\ne b(g)\qquad\text{for every }g\in A(H).
\]
The lifting lemma gives two arc-disjoint strong spanning subdigraphs on the three selected vertices per part.

# 2. Extending the construction to all vertices

Suppose two arc-disjoint strong spanning subdigraphs \(F_1,F_2\) have been constructed on two or three selected vertices per part.

For every base vertex \(x\), choose an in-neighbor \(p(x)\) and an out-neighbor \(t(x)\) in \(H\). These exist because \(H\) is strong and has at least two vertices.

For each unselected vertex \(z\in V_x\), add
\[
p(x)_0z,\quad zt(x)_0
\]
to \(F_1\), and add
\[
p(x)_1z,\quad zt(x)_1
\]
to \(F_2\).

All these arcs exist by the definition of the blow-up. They are arc-disjoint:

- the added arcs have an unselected endpoint, so are not core arcs;
- for a fixed \(z\), the two incoming arcs have different tails and the two outgoing arcs have different heads;
- arcs associated with different unselected vertices cannot coincide.

Each added vertex can be reached from, and can reach, the corresponding strong core. Both enlarged subdigraphs are therefore strongly connected and spanning.

We have proved the following sufficient conditions:
\[
\boxed{
\begin{aligned}
&H\text{ not a directed odd cycle},\quad \min_x|V_x|\ge2;\\
&\text{or simply}\quad \min_x|V_x|\ge3.
\end{aligned}}
\]
Either condition guarantees two arc-disjoint strong spanning subdigraphs.

# 3. Applying the construction under \(3\)-arc-connectivity

Let \(D\) satisfy the theorem’s hypotheses.

If \(H\) is not a directed odd cycle, the two-copy construction applies immediately.

Suppose instead that \(H\) is a directed odd cycle. For every part \(V_x\), each vertex in its predecessor part has out-degree exactly \(|V_x|\). Since \(D\) is \(3\)-arc-strong, every vertex has out-degree at least \(3\). Therefore
\[
|V_x|\ge3\qquad\text{for every }x,
\]
and the three-copy construction applies.

Thus \(D\) contains arc-disjoint strong spanning subdigraphs \(F_1,F_2\). Choose an out-branching rooted at the prescribed \(u\) inside \(F_1\), and an in-branching rooted at the prescribed \(v\) inside \(F_2\). Strong connectivity guarantees both exist, and their arc sets are disjoint.

This also covers \(u=v\). If a partition of all arcs into two strong spanning subdigraphs is desired, assign every unused arc to either part. \(\square\)

# 4. A six-vertex obstruction to \(k=2\)

Let \(D_0\) have independent parts
\[
A=\{u,v\},\qquad B=\{b_1,b_2\},\qquad C=\{c_1,c_2\},
\]
with all arcs
\[
A\longrightarrow B,\qquad B\longrightarrow C,\qquad C\longrightarrow A,
\]
and no others. Thus \(D_0\) is the complete independent blow-up of a directed triangle, with two vertices per part.

Every vertex has in-degree and out-degree \(2\).

## 4.1 Arc-connectivity

The arcs of \(D_0\) partition into the Hamilton cycle
\[
K=u\,b_1\,c_1\,v\,b_2\,c_2\,u
\]
and the two directed triangles
\[
Q_1=u\,b_2\,c_1\,u,\qquad
Q_2=v\,b_1\,c_2\,v.
\]

Let \(X\) be nonempty and proper. The Hamilton cycle contributes at least one arc to \(\delta^+(X)\).

If \(Q_1\cup Q_2\) contributes an outgoing arc, then \(|\delta^+(X)|\ge2\). Otherwise \(X\) must be exactly the vertex set of one of the two triangles. The Hamilton cycle alternates between those vertex sets, so it contributes three outgoing arcs.

Hence \(D_0\) is \(2\)-arc-strong. Its arc-connectivity is exactly \(2\), since every vertex has out-degree \(2\).

The graph is Eulerian and Hamiltonian. Its independence number is \(2\): vertices in different parts are adjacent in one direction, and each part has size two.

## 4.2 No good pair for the prescribed roots \(u,v\)

Suppose there were arc-disjoint branchings \(T,S\), where \(T\) is an out-branching rooted at \(u\), and \(S\) is an in-branching rooted at \(v\).

For every \(z\ne v\), the in-branching \(S\) uses one outgoing arc of \(z\). Since \(d_{D_0}^+(z)=2\),
\[
d_T^+(z)\le1\qquad(z\ne v).
\]

Moreover, \(d_T^+(v)\le1\). Otherwise \(T\) would contain both \(vb_1\) and \(vb_2\). But its root \(u\) must also have an outgoing arc, necessarily to one of \(b_1,b_2\). That vertex would then have in-degree at least two in \(T\), impossible.

Thus every vertex has out-degree at most one in \(T\). A spanning out-branching with this property is a Hamilton path starting at its root. The cyclic arrangement of the parts forces
\[
T=u\,b_i\,c_j\,v\,b_{3-i}\,c_{3-j}
\]
for some \(i,j\in\{1,2\}\).

In \(D_0-A(T)\), the vertices
\[
u,\quad b_{3-i},\quad c_j
\]
form the directed triangle
\[
u\longrightarrow b_{3-i}\longrightarrow c_j\longrightarrow u.
\]
Each has exactly one remaining outgoing arc, namely the displayed arc. Therefore this set has no outgoing arc in \(D_0-A(T)\).

It does not contain \(v\). Consequently \(D_0-A(T)\) has no directed path from \(u\) to \(v\), and cannot contain the alleged in-branching \(S\). This contradiction proves the obstruction.

Hence any universal constant in the original conjecture must satisfy
\[
k\ge3.
\]

## 4.3 Why prescribed roots matter

This six-vertex graph does have good pairs when the roots may be chosen. For example, both roots can be \(u\), using
\[
T_0=\{ub_1,ub_2,b_1c_1,b_2c_2,c_1v\}
\]
and
\[
S_0=\{vb_1,b_1c_2,c_2u,b_2c_1,c_1u\}.
\]
These are arc-disjoint out- and in-branchings rooted at \(u\).

Thus the example does not contradict statements guaranteeing an unspecified-root good pair on small digraphs or on digraphs of independence number at most two.

# 5. What remains unresolved

The theorem requires a substantial additional hypothesis: a partition into independent parts of size at least two, with complete adjacency between every ordered pair of adjacent parts.

Allowing singleton parts would remove that restriction, but the proof would no longer apply. Nor can one solve the general problem by first blowing up an arbitrary digraph and then contracting the parts: the two lifted subdigraphs use different copies of the same base arcs, so contraction destroys arc-disjointness.

Therefore the argument supplies:

- a sharp \(k=3\) result for the stated blow-up class;
- an explicit prescribed-root obstruction at \(k=2\);
- no universal upper bound for arbitrary digraphs.

No novelty claim is made for these special-case constructions.