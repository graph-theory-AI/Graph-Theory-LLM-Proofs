```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp high-girth pseudoforest theorem yields polynomial-time MIS for the predicted-tractable H when the number of vertex-disjoint short cycles is O(log n).",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; the algorithm requires an additional short-cycle packing bound, and novelty is not claimed."
}
```

## 1. A sharp high-girth special case

I do not obtain a polynomial-time algorithm for unrestricted \(P_\ell\)-free or subdivided-claw-free graphs. The partial result below gives an exact girth threshold for a stronger structural conclusion, followed by an algorithm extending beyond high-girth graphs.

All graphs are finite and simple, and “\(H\)-free” means induced-\(H\)-free. I use the convention that \(S_{i,j,k}\) has three arms of lengths \(i,j,k\) **in edges**, hence \(i+j+k+1\) vertices. A **pseudoforest** is a graph each of whose connected components contains at most one cycle. Forests have infinite girth.

### Theorem 1
Let \(1\le i\le j\le k\), and put
\[
R(i,j,k)=\max\bigl\{\,i+k+1,\;2\min\{k,j+1\}\,\bigr\}.
\]
Every \(S_{i,j,k}\)-free graph of girth greater than \(R(i,j,k)\) is a pseudoforest.

The threshold is sharp: for every \(i,j,k\), there is an \(S_{i,j,k}\)-free non-pseudoforest of girth exactly \(R(i,j,k)\).

For example, every \(S_{1,2,2}\)-free graph of girth at least \(5\) is a pseudoforest. For the symmetric long claw \(S_{t,t,t}\), the sharp threshold is \(2t+1\).

### 1.1. Minimal induced obstructions to being a pseudoforest

Write \(\Theta(a,b,c)\) for the union of three internally vertex-disjoint paths, of lengths \(a,b,c\), between two vertices \(u,v\). At most one path may have length \(1\), so that the graph is simple.

**Lemma 2.** Every non-pseudoforest contains an induced subgraph of one of the following forms:

1. \(K_4\);
2. a theta graph;
3. two cycles meeting in exactly one vertex;
4. two vertex-disjoint cycles joined by a path, with no additional edges.

**Proof.**
Choose a vertex-minimal induced non-pseudoforest \(F\). It is connected and has minimum degree at least \(2\): deleting a leaf cannot eliminate the property that its component contains at least two cycles.

Set
\[
n=|V(F)|,\qquad m=|E(F)|,\qquad e=m-n\ge 1.
\]
For every vertex \(v\), the graph \(F-v\) is a pseudoforest, and therefore
\[
m-d_F(v)\le n-1.
\]
Consequently \(d_F(v)\ge e+1\). Summing gives
\[
n(e+1)\le 2m=2n+2e,
\qquad\text{so}\qquad
n(e-1)\le 2e.
\]

If \(e\ge2\), then \(n\le4\); simplicity forces \(F=K_4\).

If \(e=1\), then
\[
\sum_{v\in V(F)}(d_F(v)-2)=2.
\]
Thus either one vertex has degree \(4\) and every other vertex has degree \(2\), or two vertices have degree \(3\) and every other vertex has degree \(2\). Suppressing degree-\(2\) vertices gives, respectively, two cycles sharing a vertex, or a theta graph or two cycles joined by a path. \(\square\)

We also need the following observation.

**Subdivision observation.** If a graph contains an induced \(S_{i,j,k}\), then every graph obtained from it by subdividing edges still contains an induced \(S_{i,j,k}\).

Indeed, the original witness becomes an induced subdivision of \(S_{i,j,k}\). Truncating its three arms to lengths \(i,j,k\) recovers an induced copy. This justifies the shortening argument for theta graphs below; shortening itself is not being treated as an induced-subgraph operation.

### 1.2. Proof of the upper bound

Suppose \(G\) has girth greater than \(R=R(i,j,k)\) and is not a pseudoforest. Apply Lemma 2 to obtain an induced subgraph \(F\) of one of the four listed types. Its girth is also greater than \(R\).

Since \(R\ge3\), the graph \(F\) is not \(K_4\).

If \(F\) consists of two cycles sharing a vertex or joined by a path, each cycle has length at least
\[
i+j+2
\quad\text{and at least}\quad
k+2,
\]
because \(R\ge i+k+1\). At an attachment vertex, take arms of lengths \(i,j\) in the two directions around one cycle. Take the third arm along the joining path and then, if necessary, around the other cycle. In the shared-vertex case, take it directly around the other cycle.

The length inequalities ensure that no cycle is closed and no extra edge appears between the chosen arms. Thus \(F\) contains an induced \(S_{i,j,k}\).

It remains to consider
\[
F=\Theta(a,b,c),\qquad a\le b\le c.
\]
Its girth is \(a+b>R\). By the subdivision observation, it is enough to find the desired induced claw subdivision in \(\Theta(a,b,b)\).

On a length-\(b\) path from \(u\) to \(v\), prefixes of lengths \(x\) from \(u\) and \(y\) from \(v\) are disjoint and nonadjacent precisely when
\[
x+y\le b-2.
\]

#### Case A: \(b\le k\)

From
\[
a+b>2\min\{k,j+1\},\qquad a+b\le2b\le2k,
\]
we obtain \(k>j\) and \(b\ge j+2\). Also,
\[
a+b\ge i+k+2.
\]

Construct the length-\(k\) arm by following the entire length-\(a\) path from \(u\) to \(v\), then following one length-\(b\) path backwards for \(k-a\) edges.

On that same length-\(b\) path, take the length-\(i\) arm starting at \(u\). These two portions are disjoint and nonadjacent because
\[
i+(k-a)\le b-2.
\]
Take the length-\(j\) arm from \(u\) along the remaining length-\(b\) path. Since \(j\le b-2\), its endpoint is not adjacent to \(v\).

The selected vertices induce \(S_{i,j,k}\).

#### Case B: \(b\ge k+1\)

If \(a\ge i+1\), take initial segments of lengths \(i,j,k\) on the three paths. None reaches \(v\), and these segments induce the required graph.

Suppose instead that \(a\le i\). The equality \(b=k+1\) is impossible, since it would give
\[
a+b\le i+k+1\le R.
\]
Hence \(b\ge k+2\). Furthermore,
\[
a+b\ge i+j+2.
\]

Now construct the length-\(i\) arm by following the entire length-\(a\) path to \(v\), then following one length-\(b\) path backwards for \(i-a\) edges. Take the length-\(j\) arm from \(u\) along that same path. They are disjoint and nonadjacent because
\[
j+(i-a)\le b-2.
\]
Take the length-\(k\) arm along the remaining path; \(k\le b-2\) prevents an extra edge to \(v\).

Again the selected vertices induce \(S_{i,j,k}\). This completes the upper-bound proof. \(\square\)

### 1.3. Sharpness

Put
\[
L=i+k+1,\qquad M=2\min\{k,j+1\}.
\]

First consider
\[
T_1=\Theta(i,k+1,k+1),
\]
which has girth \(L\). I claim it is \(S_{i,j,k}\)-free.

The center of any proposed induced copy must be one of the two degree-\(3\) vertices, say \(u\). The arm entering the length-\(i\) path must reach the other branch vertex \(v\), because every required arm has length at least \(i\).

The length-\(k\) arm must be this arm: otherwise it follows a length-\((k+1)\) path from \(u\) and ends at a neighbor of \(v\), creating an extra edge to the arm containing \(v\).

After reaching \(v\), the length-\(k\) arm continues \(k-i\) edges along one of the other paths. That path also contains another arm, of length at least \(i\), starting at \(u\). Disjointness and absence of an extra edge would require
\[
i+(k-i)\le(k+1)-2,
\]
which is impossible. When \(k=i\), the same inequality applies with a zero-length continuation. Thus \(T_1\) is \(S_{i,j,k}\)-free.

For the second construction, let
\[
q=\min\{k,j+1\},\qquad T_2=\Theta(q,q,q).
\]
Whenever \(M>L\), we have \(q\ge2\), so this is a simple graph of girth \(M\).

- If \(k=j\), then \(q=k\). Two required arms have length \(k\), so both would have to reach the other branch vertex, which is impossible.
- If \(k>j\), then \(q=j+1\). The length-\(k\) arm must reach the other branch vertex, while the length-\(j=q-1\) arm ends at its neighbor, creating an extra edge.

Therefore \(T_2\) is also \(S_{i,j,k}\)-free. Use \(T_1\) when \(L\ge M\), and \(T_2\) otherwise. Both are non-pseudoforests, proving sharpness.

## 2. A structural analogue of the conjectured boundary

For paths there is a simpler observation:
\[
G\text{ is }P_\ell\text{-free and }\operatorname{girth}(G)>\ell
\quad\Longrightarrow\quad
G\text{ is a forest}.
\]
Otherwise a shortest cycle is chordless, has more than \(\ell\) vertices, and contains an induced \(P_\ell\). The cases \(\ell=1,2\) are immediate.

Together with Theorem 1, this proves the following exact structural characterization.

### Corollary 3
For a fixed connected graph \(H\), the following are equivalent:

1. For some integer \(r\), every \(H\)-free graph of girth greater than \(r\) is a pseudoforest.
2. \(H\) is a path or a subdivided claw.

**Proof of the remaining implication.**
Let \(h=|V(H)|\), and suppose \(H\) is neither a path nor a subdivided claw. Consider \(\Theta(t,t,t)\) for arbitrarily large \(t>h\). This graph has maximum degree \(3\), girth \(2t\), and exactly two degree-\(3\) vertices, at distance \(t\).

A connected \(H\) outside the stated families either:

- contains a cycle;
- has a vertex of degree at least \(4\); or
- is a tree with at least two degree-\(3\) vertices.

The three displayed properties of \(\Theta(t,t,t)\), respectively, exclude each possibility. Thus these are \(H\)-free non-pseudoforests of arbitrarily large girth. \(\square\)

This is a structural dichotomy, not the requested computational dichotomy.

## 3. Extension to graphs with few disjoint short cycles

For an integer \(r\ge3\), let
\[
\nu_r(G)=
\max\bigl\{|\mathcal C|:
\mathcal C\text{ is a family of vertex-disjoint cycles of length at most }r
\bigr\}.
\]

### Theorem 4
Fix \(H=S_{i,j,k}\), and let \(r=R(i,j,k)\). Maximum Weight Independent Set on \(H\)-free graphs can be solved in
\[
O_H\!\left(n^r+
2^{\,r\nu_r(G)}(n+m)\right)
\]
arithmetic operations.

Consequently, for every fixed constant \(c\), it is polynomial-time solvable on the \(H\)-free graphs satisfying
\[
\nu_r(G)\le c\log_2 n.
\]

The same statement holds for \(H=P_\ell\), \(\ell\ge3\), with \(r=\ell\).

### Proof

#### Step 1: Find a small deletion set to pseudoforests

Greedily construct a maximal vertex-disjoint family of cycles of length at most \(r\), and let \(X\) be the union of their vertex sets.

A fully specified implementation is to enumerate all ordered \(q\)-tuples of distinct vertices, for \(3\le q\le r\). Whenever a tuple describes a cycle disjoint from the currently marked vertices, mark all its vertices. For fixed \(H\), this takes \(O_H(n^r)\) time.

If the chosen family has \(p\) cycles, then
\[
|X|\le rp\le r\nu_r(G).
\]
Its maximality implies that \(G-X\) has no cycle of length at most \(r\). Since \(H\)-freeness is hereditary, Theorem 1 implies that \(G-X\) is a pseudoforest. In the path case it is a forest.

Computing the optimum packing number \(\nu_r(G)\) is not necessary.

#### Step 2: Enumerate the intersection of the solution with \(X\)

For every independent subset \(A\subseteq X\), compute
\[
w(A)+\alpha_w\bigl(G-(X\cup N(A))\bigr).
\]
Then
\[
\alpha_w(G)=
\max_{\substack{A\subseteq X\\ A\text{ independent}}}
\left[
w(A)+\alpha_w\bigl(G-(X\cup N(A))\bigr)
\right].
\]

This equality follows by partitioning independent sets according to their intersection with \(X\). Every residual graph is an induced subgraph of \(G-X\), hence is a pseudoforest.

#### Step 3: Solve the residual pseudoforests

For a rooted tree, use the standard recurrences
\[
F_1(v)=w(v)+\sum_{u\text{ child of }v}F_0(u),
\]
\[
F_0(v)=
\sum_{u\text{ child of }v}\max\{F_0(u),F_1(u)\}.
\]

For a connected unicyclic component \(Q\), choose a vertex \(z\) on its cycle and use
\[
\alpha_w(Q)=
\max\left\{
\alpha_w(Q-z),\
w(z)+\alpha_w(Q-N[z])
\right\}.
\]
Both graphs on the right are forests. Thus a pseudoforest is solved in linear time, and an optimum independent set can be recovered by recording the choices.

There are at most \(2^{|X|}\le2^{r\nu_r(G)}\) subsets to consider, proving the running-time bound. Binary-encoded weights add only the usual polynomial bit-complexity factor.

If \(\nu_r(G)\le c\log_2 n\), then
\[
2^{r\nu_r(G)}\le n^{rc},
\]
so the algorithm is polynomial. \(\square\)

The same deletion argument also gives the structural bound
\[
\operatorname{tw}(G)\le r\nu_r(G)+2:
\]
pseudoforests have treewidth at most \(2\), and adding \(X\) to every bag increases the width by at most \(|X|\).

## 4. What remains unresolved

The additional packing hypothesis is not implied by \(H\)-freeness. For example, every complete graph is \(S_{i,j,k}\)-free, but
\[
\nu_r(K_n)=\lfloor n/3\rfloor
\qquad(r\ge3).
\]
Thus the algorithm above can have an exponential bound on unrestricted \(S_{i,j,k}\)-free inputs—even though complete graphs themselves are easy. Nothing here controls arbitrary interactions among many short cycles.

Accordingly, this does **not** establish polynomial-time MIS for any unrestricted open member of the conjectured family. The proved contributions are the sharp girth threshold, its structural characterization, and the short-cycle-packing algorithm.

Finally, two complexity qualifications in the supplied discussion matter:

- NP-completeness gives the literal “not in \(\mathsf P\)” conclusion only under \(\mathsf P\ne\mathsf{NP}\).
- A quasi-polynomial algorithm does not unconditionally rule out NP-hardness; such hardness would imply \(\mathsf{NP}\subseteq\mathsf{QP}\), which is not known to be impossible.

None of the partial results above uses either unproved exclusion.