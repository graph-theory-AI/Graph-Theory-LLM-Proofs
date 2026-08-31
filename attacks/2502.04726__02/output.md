```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard spanning-rooted-path definition of activity, testing even one cycle vertex is NP-complete when an optimal lollipop and its cycle are supplied, while a Held–Karp subset dynamic program computes all active vertices exponentially.",
  "would_publish": false,
  "caveats": "“Simple” is not formal; this rules out a general polynomial-time algorithm unless P=NP but does not preclude a structural characterization or algorithms for restricted graph classes."
}
```

# Formalized statement

The catalog question is not literally a yes/no mathematical statement, because “simple” is undefined and an optimal lollipop need not be unique. I address the natural algorithmic formulation in which an optimal lollipop is already supplied.

Let \(L=(P,C)\) be a lollipop with attachment vertex
\[
\rho=V(P)\cap V(C).
\]
Under the usual active-vertex definition, a vertex \(x\in V(C)\) is active precisely when \(G[V(C)]\) has a Hamiltonian \(\rho\)-\(x\) path. In the equivalent convention where an active path includes the handle \(P\), one concatenates the fixed handle with such a path. The reduction below works under either convention.

The main result is the following.

> **Theorem.** Given a simple undirected graph \(H\), an explicitly listed Hamiltonian cycle \(C_H\), and two specified vertices \(\rho,\tau\), deciding whether \(H\) has a Hamiltonian \(\rho\)-\(\tau\) path is NP-complete.
>
> Consequently, deciding whether one specified vertex of the cycle of a supplied optimal lollipop is active is NP-hard. The hardness persists for connected graphs of minimum degree \(2\), with a visibly optimal lollipop whose cycle omits only two vertices.

Thus a polynomial-time procedure computing all active vertices would imply \(P=NP\), even if the computationally difficult task of finding an optimal lollipop has already been done.

# 1. Hamiltonian endpoint paths remain hard with a known Hamiltonian cycle

Define the decision problem:

\[
\mathsf{KCHP}=\left\{
(H,C_H,\rho,\tau):
\begin{array}{l}
C_H\text{ is a Hamiltonian cycle of }H,\\
H\text{ has a Hamiltonian }\rho\text{-}\tau\text{ path}
\end{array}\right\}.
\]

Membership in NP is immediate. We prove NP-hardness in two stages.

## 1.1 A directed intermediate construction

We start from the directed Hamiltonian \(s\)-\(t\) path problem, which is NP-complete. For completeness, this follows from Hamiltonian cycle as follows: replace every undirected edge by both orientations, choose one vertex \(z\), split \(z\) into a source \(s\) carrying all arcs formerly leaving \(z\) and a sink \(t\) carrying all arcs formerly entering \(z\). A Hamiltonian cycle through \(z\) is then equivalent to a Hamiltonian \(s\)-\(t\) path in the split digraph.

Let \(D\) be a directed graph with specified distinct vertices \(s,t\). Write
\[
V(D)=\{v_1,\dots,v_n\}.
\]
Construct a directed graph \(B\) with three vertices
\[
a_v,\ c_v,\ b_v
\]
for every \(v\in V(D)\).

Add the following arcs:

1. for each \(v\),
   \[
   a_v\to c_v,\quad c_v\to b_v,\quad
   b_v\to c_v,\quad c_v\to a_v;
   \]

2. for every arc \(v\to w\) of \(D\), add
   \[
   b_v\to a_w;
   \]

3. add the scaffold arcs
   \[
   a_{v_i}\to b_{v_{i+1}}
   \qquad (1\le i\le n),
   \]
   where indices are taken modulo \(n\).

The scaffold gives an explicitly known directed Hamiltonian cycle:
\[
b_{v_1},c_{v_1},a_{v_1},
b_{v_2},c_{v_2},a_{v_2},
\dots,
b_{v_n},c_{v_n},a_{v_n},
b_{v_1}.
\]

We claim that
\[
D\text{ has a Hamiltonian }s\text{-}t\text{ path}
\iff
B\text{ has a Hamiltonian }a_s\text{-}b_t\text{ path}. \tag{1}
\]

Indeed, in any Hamiltonian \(a_s\)-\(b_t\) path of \(B\), the vertex \(c_v\) is not an endpoint and its only possible predecessor and successor are \(a_v,b_v\). Thus the three vertices belonging to \(v\) occur consecutively, in one of the two orders
\[
a_v,c_v,b_v
\quad\text{or}\quad
b_v,c_v,a_v.
\]
Since the path starts at \(a_s\), the \(s\)-block has the first orientation. After a forward block \(a_v,c_v,b_v\), the only possible unused external successor of \(b_v\) is some \(a_w\) such that \(v\to w\) is an arc of \(D\). Consequently the next block is also forward. Inductively every block is forward, and contracting the blocks gives a Hamiltonian \(s\)-\(t\) path in \(D\).

Conversely, replacing every vertex \(v\) of a Hamiltonian \(s\)-\(t\) path in \(D\) by
\[
a_v,c_v,b_v
\]
gives the required path in \(B\). This proves (1).

## 1.2 Removing the directions

For every vertex \(z\in V(B)\), create three vertices
\[
z^-,z^0,z^+
\]
and the two edges
\[
z^-z^0,\qquad z^0z^+.
\]
For every directed arc \(z\to w\) of \(B\), add the undirected edge
\[
z^+w^-.
\]
Call the resulting simple undirected graph \(U\).

Every directed Hamiltonian cycle
\[
z_1\to z_2\to\cdots\to z_m\to z_1
\]
of \(B\) yields the explicitly known Hamiltonian cycle
\[
z_1^-,z_1^0,z_1^+,
z_2^-,z_2^0,z_2^+,
\dots,
z_m^-,z_m^0,z_m^+,
z_1^-                                             \tag{2}
\]
of \(U\).

Set
\[
\rho=(a_s)^-,
\qquad
\tau=(b_t)^+.
\]
Then
\[
B\text{ has a directed Hamiltonian }a_s\text{-}b_t\text{ path}
\iff
U\text{ has an undirected Hamiltonian }\rho\text{-}\tau\text{ path}. \tag{3}
\]

To see the reverse implication, note that every \(z^0\) has degree exactly \(2\). Hence every Hamiltonian \(\rho\)-\(\tau\) path uses each triple consecutively. At the initial triple, the path is forced to traverse
\[
(a_s)^-,(a_s)^0,(a_s)^+.
\]
Every external edge then goes from a plus-port \(z^+\) to a minus-port \(w^-\), corresponding to an arc \(z\to w\) of \(B\). Induction therefore fixes the forward orientation of every triple. Contracting the triples gives a directed Hamiltonian path in \(B\), ending at \(b_t\). The converse is immediate.

Combining (1) and (3) proves NP-hardness of \(\mathsf{KCHP}\), and hence the theorem.

# 2. Embedding the hardness in an optimal lollipop

Let \(U,C_U,\rho,\tau\) be the output of the preceding reduction. Add two new vertices \(\alpha,\beta\) and the edges
\[
\alpha\beta,\qquad \beta\rho,\qquad \rho\alpha.
\]
Thus \(\alpha,\beta,\rho\) span a triangle meeting \(U\) only in \(\rho\). Let \(G\) denote the resulting graph, and take
\[
P=\alpha\beta\rho,\qquad C=C_U.
\]

Then \(L=(P,C)\) is a lollipop: \(P\) and \(C\) meet exactly in the endpoint \(\rho\).

It is also visibly optimal under the usual lollipop objective based on the number of covered vertices and the length of the cycle:

* \(V(P)\cup V(C)=V(G)\), so it covers every vertex;
* \(\rho\) is a cut vertex separating \(\{\alpha,\beta\}\) from \(U-\rho\);
* consequently every cycle of \(G\) lies either in \(U\) or in the added triangle;
* \(C_U\) has \(|V(U)|\) vertices and is therefore a longest cycle of \(G\).

Thus \(L\) simultaneously has maximum possible order and maximum possible cycle length.

Moreover,
\[
\tau\text{ is active in }L
\iff
U\text{ has a Hamiltonian }\rho\text{-}\tau\text{ path}. \tag{4}
\]
Under the cycle-only definition of activity, this is immediate because \(G[V(C)]=U\). Under the whole-lollipop-path convention, any Hamiltonian path from \(\alpha\) to \(\tau\) must first traverse
\[
\alpha,\beta,\rho:
\]
if it used \(\alpha\rho\) first, then \(\beta\) could not subsequently be covered without revisiting \(\alpha\) or \(\rho\). The remaining portion is exactly a Hamiltonian \(\rho\)-\(\tau\) path in \(U\).

Finally, \(U\) contains a Hamiltonian cycle, so every vertex of \(U\) has degree at least \(2\), while \(\alpha,\beta\) have degree \(2\). Hence
\[
\delta(G)\ge 2.
\]

This proves:

> **Corollary.** Testing whether a specified cycle vertex is active is NP-hard even when an optimal lollipop is supplied explicitly, the host graph has minimum degree \(2\), and the optimal cycle contains all but two vertices.

The ordinary active-vertex decision problem is in NP because an active path is a polynomially checkable certificate. Formally, the unrestricted problem is therefore NP-complete, with NP-hardness already occurring on the promised subclass of optimal lollipops.

In particular, a polynomial-time algorithm outputting all active vertices would decide whether \(\tau\) is active and would solve directed Hamiltonian path in polynomial time.

# 3. A simple exact exponential algorithm

There is nevertheless a direct Held–Karp dynamic program computing all active vertices simultaneously.

Let
\[
H=G[V(C)],\qquad m=|V(C)|,
\]
and let \(\rho\) be the attachment vertex. For every subset \(S\subseteq V(C)\) containing \(\rho\) and every \(v\in S\), define
\[
T[S,v]=1
\]
if and only if \(H[S]\) has a \(\rho\)-\(v\) path whose vertex set is exactly \(S\).

Initialize
\[
T[\{\rho\},\rho]=1.
\]
For all other states use
\[
T[S,v]
=
\bigvee_{\substack{u\in S\setminus\{v\}\\uv\in E(H)}}
T[S\setminus\{v\},u].                              \tag{5}
\]
The recurrence is correct by deleting, or appending, the last vertex of the path.

The full active set is
\[
\operatorname{Act}(L)
=
\{v\in V(C):T[V(C),v]=1\}.
\]
It can be computed in
\[
O(m^2 2^m)
\]
time and
\[
O(m2^m)
\]
space, with predecessor pointers if explicit active paths are wanted. If the definition permits reordering all vertices of \(P\cup C\), one applies the same recurrence to that vertex set with the free endpoint of \(P\) as the fixed start.

# What is and is not resolved

The reduction separates two sources of difficulty:

1. finding an optimal lollipop is NP-hard, as already observed in the source;
2. even after an optimal lollipop is supplied, recognizing its active vertices remains NP-hard.

Thus there is no general polynomial-time exact procedure unless \(P=NP\). This does not rule out:

* a useful nonalgorithmic characterization;
* polynomial algorithms on restricted graph classes or under bounded parameters;
* algorithms that find only sufficiently many active vertices;
* a different answer if “active” means reachability in a specifically restricted rotation graph rather than existence of an arbitrary spanning rooted path.

Because the original word “simple” has no formal complexity meaning, the qualitative question itself is not completely settled, but its natural polynomial-time interpretation receives a sharp negative complexity classification.