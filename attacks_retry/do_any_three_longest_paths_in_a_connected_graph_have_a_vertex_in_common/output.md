```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Counterexamples of bounded cycle rank have explicitly bounded-size witnesses, giving an exact finite search, while cycle rank at most three is excluded.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; no kernel enumeration was executed, and no novelty claim is made."
}
```

# A bounded-cycle-rank search theorem

I do not obtain a general proof or a counterexample. The main result below is an exact reduction of the **bounded-cycle-rank existence problem**, including all possible subdivision lengths, to a finite search.

The connected-intersection argument from the previous attempt is independently verified below. Rather than extrapolating its splicing arguments to more complicated intersections, I take a different direction: suppress degree-two vertices, but retain enough information to test longest paths exactly. A subtlety is that a competing longest path may have endpoints inside suppressed edges.

Throughout, graphs are finite, undirected, and simple unless explicitly described as multigraphs. Paths are simple, and length means number of edges. For a connected graph, put
\[
\beta(G)=|E(G)|-|V(G)|+1.
\]

## Results

**Theorem 1.** Any three longest paths in a connected graph of cycle rank at most three have a common vertex.

**Theorem 2.** Let \(b\ge 0\), and put
\[
M=3b+9,\qquad F(b)=3M\,M!+1.
\]
If a counterexample to the conjecture exists with cycle rank at most \(b\), then one exists with at most \(F(b)\) vertices.

More precisely, such a counterexample has a representation by:

- a loopless multigraph with at most \(2b+10\) vertices and \(3b+9\) edges;
- three specified simple paths in that multigraph;
- positive integer edge lengths, each at most \(3m!\), where \(m\) is the number of multigraph edges.

Consequently, the existence of a counterexample of cycle rank at most \(b\) can be decided by an exact search taking
\[
2^{O((b+1)^2\log(b+2))}
\]
bit operations.

The second theorem does **not** assert that the search returns “no.” No such search was performed here.

---

## 1. Excluding cycle rank at most three

### Pairwise intersection

Two longest paths in a connected graph always intersect. Indeed, if two disjoint paths of maximum length \(L\) were joined by a shortest connecting path of positive length \(d\), then its interior would avoid both paths. Taking a longer half of each longest path and joining them through the connector would give a simple path of length at least
\[
\left\lceil \frac L2\right\rceil+d+
\left\lceil \frac L2\right\rceil>L.
\]

We need a slightly stronger observation.

### Connected-intersection lemma

**Lemma 3.** Let \(P,Q\) be longest paths. If the graph consisting of their common vertices and common edges is connected, then every longest path meets \(V(P)\cap V(Q)\).

**Proof.** Their intersection is a common subpath \(H\), possibly a single vertex. Orient both paths through \(H\) in the same direction. Let \(c\) be its length, and denote the lengths of the left and right tails of \(P,Q\) by
\[
a_P,b_P,\qquad a_Q,b_Q.
\]
All four tail interiors are mutually disjoint.

Joining the left tail of either path to \(H\) and the right tail of the other always gives a simple path. Maximality therefore gives
\[
a_P=a_Q=:a,\qquad b_P=b_Q=:b.
\]
Thus their common length is
\[
L=a+c+b.
\]

Suppose a longest path \(R\) avoids \(V(H)\). By pairwise intersection, \(R\) meets both \(P-V(H)\) and \(Q-V(H)\). Along \(R\), take two consecutive encounters with \(P\cup Q\) at which ownership changes. The intervening subpath \(C\) has endpoints
\[
x\in P-V(H),\qquad y\in Q-V(H),
\]
and its interior avoids \(P\cup Q\). Write \(d=|E(C)|>0\).

Up to reversing the orientations and interchanging \(P,Q\), there are two cases.

*If \(x,y\) lie in left tails*, let their distances from \(H\) be \(\alpha,\gamma\). Splicing through \(C\) gives two simple paths of lengths
\[
L+d+\alpha-\gamma,\qquad
L+d+\gamma-\alpha.
\]

*If \(x\) lies in a left tail and \(y\) in a right tail*, measure their distances from the respective ends of \(H\) by \(\alpha,\gamma\). One path joins the two left-tail endpoints through \(H\), \(y\), \(C\), and \(x\); the other joins the two right-tail endpoints similarly. Their lengths are
\[
2a+c+\gamma-\alpha+d,\qquad
2b+c+\alpha-\gamma+d.
\]

In either case the sum is \(2L+2d>2L\), so one path is longer than \(L\). All concatenations are simple because the tail interiors are disjoint and \(C\) is internally external to \(P\cup Q\). Zero-length tails simply cannot contain a connector endpoint. This contradiction proves the lemma. \(\square\)

### Counting intersection components

Suppose \(P_1,P_2,P_3\) form a counterexample triple, and let
\[
U=P_1\cup P_2\cup P_3.
\]
The graph \(U\) is connected. Write \(k_{ij}\) for the number of components of the graph \(P_i\cap P_j\), including isolated common vertices.

Pairwise intersection and Lemma 3 imply
\[
k_{12},k_{13},k_{23}\ge2.
\]

There is no triple-intersection term in inclusion–exclusion, for vertices or edges. Since each path has edge-minus-vertex count \(-1\), and \(P_i\cap P_j\) is a forest with edge-minus-vertex count \(-k_{ij}\),
\[
\begin{aligned}
\beta(U)
&=\sum_{i=1}^3\bigl(|E(P_i)|-|V(P_i)|\bigr)
-\sum_{i<j}\bigl(|E(P_i\cap P_j)|-|V(P_i\cap P_j)|\bigr)+1\\
&=k_{12}+k_{13}+k_{23}-2\\
&\ge4.
\end{aligned}
\tag{1}
\]
Cycle rank is monotone under taking connected subgraphs, as is seen by extending a spanning tree of the subgraph to one of the graph. Hence \(\beta(G)\ge4\), proving Theorem 1.

---

## 2. A small multigraph kernel

Assume a counterexample exists in a graph of cycle rank at most \(b\). Delete everything outside the union
\[
U=P_1\cup P_2\cup P_3.
\]
The three paths remain longest: deleting edges and vertices cannot introduce a longer path.

Put \(b'=\beta(U)\le b\). Because no vertex belongs to all three designated paths,
\[
\Delta(U)\le4.
\tag{2}
\]

Mark all endpoints of \(P_1,P_2,P_3\), at most six vertices. Suppress every unmarked degree-two vertex, retaining parallel edges when they arise. Call the resulting multigraph \(K\). Each edge \(e\) represents a chain in \(U\); give it the positive integer length \(x_e\) of that chain.

### Why the three paths project correctly

At an unmarked degree-two vertex, every designated path using one incident edge must use the other. Consequently, the set of designated paths using an edge is constant along each suppressed chain.

Thus each \(P_i\) projects to a simple path \(\Pi_i\) in \(K\), and
\[
|E(P_i)|=\sum_{e\in E(\Pi_i)}x_e.
\tag{3}
\]
The paths \(\Pi_1,\Pi_2,\Pi_3\) cover \(K\), and no vertex of \(K\) belongs to all three.

Also, \(K\) has no loops. A suppressed chain returning to the same retained vertex would have constant nonempty path membership; some \(P_i\) would therefore contain the entire resulting cycle, which is impossible for a simple path.

### Kernel-size bounds

Let \(n_j\) count the vertices of degree \(j\) in \(K\). There are no isolated vertices, and degrees are at most four. Every degree-one or degree-two vertex of \(K\) is a marked endpoint, so
\[
n_1+n_2\le6.
\tag{4}
\]
Suppression preserves cycle rank. The degree sum gives
\[
-n_1+n_3+2n_4=2b'-2.
\]
Therefore
\[
\begin{aligned}
|V(K)|
&=2b'-2+2n_1+n_2-n_4\\
&\le2b'+10,
\end{aligned}
\]
and hence
\[
|E(K)|=|V(K)|+b'-1\le3b'+9.
\tag{5}
\]

The remaining issue is to control the integer lengths \(x_e\).

---

## 3. Testing longest paths after subdivision

It is not enough to test weighted simple paths in \(K\). For example, if \(K\) consists of two parallel edges of lengths \(a,b\), its subdivision is a cycle. Its longest path has length \(a+b-1\), whereas a weighted simple path in \(K\) has length at most \(\max(a,b)\).

The missing paths have endpoints inside the subdivided edges.

### Path templates

Let \(B\) be a simple path in \(K\), with endpoints \(u,v\). A one-vertex path is allowed. Start with its weighted length
\[
h_B(x)=\sum_{e\in E(B)}x_e.
\]

Permit the following terminal additions:

1. **No addition:** length \(h_B(x)\).

2. **One addition:** choose an edge \(e\notin E(B)\) joining an endpoint of \(B\) to another vertex of \(B\). Add
   \[
   x_e-1.
   \]

3. **Two additions:** choose distinct edges \(e,f\notin E(B)\), one incident with \(u\), the other with \(v\), whose other endpoints belong to \(V(B)\). Add
   \[
   x_e+x_f-2.
   \]

A terminal addition traverses all internal vertices of its subdivided edge, stopping immediately before its other endpoint. If \(x_e=1\), the addition has length zero and is simply omitted.

Each template has length
\[
\ell_T(x)=\sum_{e\in S_T}x_e-c_T,
\qquad c_T\in\{0,1,2\},
\tag{6}
\]
where every edge in \(S_T\) occurs once.

**Lemma 4.** For every positive integer length vector whose subdivision is simple, the longest-path length in that subdivision is
\[
\max_T\ell_T(x).
\tag{7}
\]

**Proof.** Every listed template is realized by a simple path. Distinct subdivided edges have disjoint interiors, and each terminal addition avoids its far endpoint, which is already on \(B\).

Conversely, take a longest path \(R\) in the subdivision.

If it contains no kernel vertex, it lies inside a single subdivided edge and is no longer than the corresponding full-edge template.

Otherwise, list the kernel vertices encountered along \(R\). Between consecutive ones, \(R\) traverses an entire subdivided edge. These vertices and edges form a simple kernel path \(B\).

Any remaining segment at an end of \(R\) lies in a subdivided edge not used by \(B\). The other kernel endpoint of that edge must already belong to \(B\): otherwise the terminal segment could be extended toward that endpoint, contradicting maximality.

There are at most two such terminal segments.

- If they use distinct edges, their lengths are at most the respective \(x_e-1\), giving a listed template.
- If they use the same edge, their combined length is at most \(x_e-1\), since at least one edge of that chain must remain unused between the two terminal portions. The corresponding one-addition template is at least as long.

Thus some template is at least as long as \(R\). Since every template is an actual path, equality follows. \(\square\)

This lemma supplies a finite, exact list of length inequalities; it does not overlook competitors whose endpoints lie inside suppressed chains.

---

## 4. The integer feasibility system

Fix a kernel \(K\) and a covering triple \(\Pi_1,\Pi_2,\Pi_3\) with empty common vertex intersection. Put
\[
L_i(x)=\sum_{e\in E(\Pi_i)}x_e.
\]
The designated paths are all longest exactly when
\[
L_1(x)=L_2(x)=L_3(x)
\tag{8}
\]
and
\[
\ell_T(x)\le L_1(x)
\quad\text{for every template }T.
\tag{9}
\]

We must also ensure that the subdivision is simple. Since \(K\) is loopless, the only obstruction is having two parallel edges both of length one.

Choose the set \(F\) of edges that have length one, allowing at most one edge of each parallel class in \(F\), and impose
\[
x_e=1\quad(e\in F),\qquad
x_e\ge2\quad(e\notin F).
\tag{10}
\]
There are finitely many choices of \(F\).

For each choice, (8)–(10) form a finite integer linear system in \(m=|E(K)|\) variables. After expressing equalities as pairs of inequalities:

- every matrix entry belongs to \(\{-1,0,1\}\);
- every right-hand side has absolute value at most \(2\);
- every feasible point has \(x_e\ge1\).

The coefficient assertion uses the fact that a template uses each kernel edge at most once.

The following elementary bound now applies.

### A small-integer-point lemma

**Lemma 5.** Suppose
\[
\mathcal P=\{x\in\mathbb R^m:Ax\le d\}\subseteq[1,\infty)^m,
\]
where \(A\) has entries in \(\{-1,0,1\}\) and \(d\) is integral with \(|d_i|\le2\). If \(\mathcal P\) contains an integer point, it contains one satisfying
\[
1\le x_j\le3m!\qquad(1\le j\le m).
\tag{11}
\]

**Proof.** The polyhedron is pointed. Use its standard decomposition into the convex hull of its vertices plus its recession cone.

At any vertex, choose \(m\) linearly independent active constraints. Cramer’s rule gives
\[
|x_j|\le2m!,
\tag{12}
\]
because the denominator is a nonzero integer, while the numerator determinant has at most \(m!\) terms, each of absolute value at most \(2\).

Each extreme ray of the recession cone can be represented by an integer vector \(r\) with
\[
0\le r_j\le(m-1)!.
\tag{13}
\]
Indeed, choose \(m-1\) independent tight rows defining that ray and use their cofactor vector. Nonnegativity follows because the recession cone is contained in the nonnegative orthant.

Let \(z\) be an integer point of \(\mathcal P\). By the vertex-plus-ray decomposition and conic Carathéodory, write
\[
z=v+\sum_{j=1}^{t}\lambda_jr_j,
\qquad t\le m,\quad \lambda_j\ge0,
\]
where \(v\) is a convex combination of vertices and the \(r_j\) satisfy (13).

Set
\[
z'=z-\sum_{j=1}^{t}\lfloor\lambda_j\rfloor r_j.
\]
This is integral and remains in \(\mathcal P\), since
\[
z'=v+\sum_{j=1}^{t}
\bigl(\lambda_j-\lfloor\lambda_j\rfloor\bigr)r_j.
\]
Each coordinate is therefore at most
\[
2m!+m(m-1)!=3m!.
\]
Its lower bound is supplied by \(\mathcal P\subseteq[1,\infty)^m\). \(\square\)

---

## 5. Proof of the bounded-size witness theorem

Return to an actual counterexample and its kernel. Its original length vector is an integer solution of (8)–(10), for the appropriate set \(F\).

Lemma 5 supplies another solution with
\[
1\le x_e\le3m!.
\]
Subdivide \(K\) with these new lengths.

- Conditions (10) make the resulting graph simple.
- The three designated paths still have empty common intersection.
- Conditions (8), (9), and Lemma 4 make all three longest.
- Subdivision preserves the cycle rank \(b'\).

The number of vertices in this new counterexample is
\[
\begin{aligned}
|V(K)|+\sum_{e\in E(K)}(x_e-1)
&=\sum_e x_e+1-b'\\
&\le3m\,m!+1\\
&\le3(3b+9)(3b+9)!+1.
\end{aligned}
\]
This proves the size assertion of Theorem 2.

### A fully specified exact search

For a given \(b\), perform the following finite search:

1. Enumerate all connected loopless multigraphs \(K\) with
   \[
   |V(K)|\le2b+10,\quad |E(K)|\le3b+9,\quad
   \Delta(K)\le4,\quad \beta(K)\le b.
   \]
2. Enumerate all triples of nontrivial simple paths covering \(K\) and having no common vertex.
3. For each triple, enumerate all integer vectors
   \[
   x\in\{1,\ldots,3m!\}^{E(K)}.
   \]
4. Reject vectors giving two parallel edges length one.
5. Compute the maximum in (7). Accept precisely when all three designated path lengths equal that maximum.

An accepted object expands to an explicit counterexample. Conversely, the preceding proof shows that every bounded-rank counterexample produces an accepted object somewhere in this search.

There are \(2^{O(b\log(b+2))}\) kernel candidates. In a maximum-degree-four kernel on \(O(b)\) vertices, there are \(2^{O(b)}\) simple paths and path templates, up to polynomial factors. The length-vector enumeration has size
\[
(3m!)^m=2^{O(b^2\log(b+2))},
\]
and its integers have \(O(b\log(b+2))\) bits. This establishes the claimed running-time bound.

---

## 6. What remains open

The first rank not excluded by the splicing argument is \(b=4\). In that case, (1) forces
\[
k_{12}=k_{13}=k_{23}=2.
\]
The kernel reduction limits a potential counterexample union to at most
\[
18\text{ kernel vertices and }21\text{ kernel edges}.
\]

Thus the infinitely many possible subdivisions at cycle rank four can be handled by a finite family of exact integer systems. However, **I have not enumerated those kernels or established infeasibility of their systems**.

The proved progress is therefore:

- an independently checked cycle-rank-three special case;
- an explicit bounded-size witness theorem and exact decision procedure for every fixed cycle-rank bound.

There is no argument here excluding feasible kernels of arbitrary rank, so the original three-longest-paths conjecture remains unresolved.