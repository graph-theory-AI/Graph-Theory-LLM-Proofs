```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I give explicit counterexamples for arc-connectivity and sharp special-case bounds for vertex-connectivity, without resolving the general κ question.",
  "would_publish": false,
  "caveats": "The negative arc-connectivity conclusion is already recorded in the supplied review; no novelty or complete κ result is claimed."
}
```

## 1. Definitions and scope

All digraphs below are finite, loopless, and simple; antiparallel arcs are allowed. A subdivision replaces each arc by a directed path, with all replacement paths internally vertex-disjoint and with no branch vertex internal to a replacement path.

Write
\[
\mu_\kappa(F)=\min\{k:\text{every }D\text{ with }\kappa(D)\ge k
\text{ contains a subdivision of }F\},
\]
and put \(\mu_\kappa(F)=\infty\) if no such \(k\) exists. Define \(\mu_{\kappa'}(F)\) analogously. We use the convention
\(\kappa(\overleftrightarrow{K_m})=m-1\).

The results proved here are:

1. An explicit family of **oriented** digraphs \(D_d\) satisfies
   \[
   \kappa'(D_d)=d+1,\qquad \kappa(D_d)=1,
   \]
   and contains no subdivision of \(\overleftrightarrow{K_4}\).
2. If an \(n\)-vertex digraph \(F\) becomes an orientation of a forest after deleting all arcs entering one vertex, then
   \[
   \mu_\kappa(F)=n-1.
   \]
3. For every \(n\)-vertex digraph \(F\), \(n\ge2\),
   \[
   \mu_\kappa(F)\ge
   \max\{n-1,\tau_{\rm arc}(F)\},
   \]
   where \(\tau_{\rm arc}(F)\) is the minimum number of arcs whose deletion makes \(F\) acyclic. In particular,
   \[
   \mu_\kappa(\overleftrightarrow{K_t})\ge \binom t2.
   \]

The first conclusion is already reported in the supplied review. The construction and proof below are self-contained.

## 2. Explicit counterexamples for strong arc-connectivity

### 2.1. An out-regular digraph with only odd directed cycles

Fix \(d\ge1\). Let \(T_d\) be the rooted tree of height \(2d\) in which every nonleaf has exactly \(d\) children. Orient every tree edge away from the root.

For each leaf \(z\), add arcs from \(z\) to its ancestors at depths
\[
0,2,4,\ldots,2d-2.
\]
Call the resulting oriented digraph \(G_d\).

Every vertex of \(G_d\) has out-degree exactly \(d\): nonleaves have their \(d\) children as out-neighbors, and leaves have the \(d\) specified ancestors.

**Claim. Every directed cycle in \(G_d\) has odd length.**

Let \(C\) be a directed cycle, and choose a vertex \(x\) of minimum depth on \(C\). Starting at \(x\), the cycle follows downward tree arcs until reaching a leaf \(z\). Its next arc goes to an ancestor \(a\) of \(z\).

By minimality of the depth of \(x\), the vertex \(a\) lies on the already traversed \(x\)-to-\(z\) tree path. Since \(C\) is a simple cycle, necessarily \(a=x\). Thus \(x\) has even depth and
\[
|C|=2d-\operatorname{depth}(x)+1
\]
is odd. ∎

### 2.2. A parity obstruction

**Lemma. Every subdivision of \(\overleftrightarrow{K_3}\) contains an even directed cycle.**

**Proof.** Label the branch vertices \(1,2,3\), and let \(\ell_{ij}\) be the length of the path replacing \(i\to j\).

The three directed cycles corresponding to the digons have lengths
\[
\ell_{12}+\ell_{21},\qquad
\ell_{13}+\ell_{31},\qquad
\ell_{23}+\ell_{32}.
\]
The two directed triangles have lengths
\[
\ell_{12}+\ell_{23}+\ell_{31},
\qquad
\ell_{13}+\ell_{32}+\ell_{21}.
\]
The sum of the first three lengths equals the sum of the last two. They therefore cannot all be odd. ∎

Consequently, neither \(G_d\) nor its arc-reversal contains a subdivision of \(\overleftrightarrow{K_3}\).

### 2.3. Construction of \(D_d\)

Take disjoint copies
\[
A\cong G_d,\qquad B\cong G_d^{\mathrm{rev}},
\]
and one additional vertex \(c\). Add all arcs
\[
a\to c\quad(a\in A),\qquad
c\to b\quad(b\in B),\qquad
b\to a\quad(b\in B,\ a\in A).
\]

Let \(N=|A|=|B|\). Notice that \(N\ge d+1\), and that \(D_d\) is oriented. It is strongly connected, using the cyclic arrangement
\[
A\longrightarrow c\longrightarrow B\longrightarrow A.
\]

### 2.4. Exact strong arc-connectivity

We prove
\[
\kappa'(D_d)=d+1.
\]

Every vertex of \(A\) has out-degree \(d+1\), so
\[
\kappa'(D_d)\le d+1.
\]

For the reverse inequality, let \(S\) be a nonempty proper subset of \(V(D_d)\). First suppose \(c\notin S\).

If \(S\cap B\ne\varnothing\), fix \(b\in S\cap B\). For each \(a\in A\), one of the following arcs leaves \(S\):

- \(a\to c\), if \(a\in S\);
- \(b\to a\), if \(a\notin S\).

These are \(N\) distinct arcs. Hence
\[
|\delta^+(S)|\ge N\ge d+1.
\]

Otherwise, \(S\subseteq A\). Put \(s=|S|\). If \(s\ge d+1\), the \(s\) arcs from \(S\) to \(c\) suffice. If \(1\le s\le d+1\), each vertex of \(S\) has \(d+1\) out-neighbors and at most \(s-1\) of them lie in \(S\). Therefore
\[
|\delta^+(S)|\ge s(d+2-s)\ge d+1,
\]
where the last inequality follows from
\[
s(d+2-s)-(d+1)=(s-1)(d+1-s)\ge0.
\]

The construction is isomorphic to its arc-reversal, by exchanging \(A\) and \(B\) and fixing \(c\). Thus the case \(c\in S\) follows by applying the preceding argument to \(V(D_d)\setminus S\) in the reversed digraph.

Every nontrivial directed cut has at least \(d+1\) arcs, proving the claimed equality.

### 2.5. Excluding \(\overleftrightarrow{K_4}\)

Suppose that \(D_d\) contained a subdivision \(Q\) of \(\overleftrightarrow{K_4}\). Then \(Q\) contains a subdivision of \(\overleftrightarrow{K_3}\) avoiding \(c\):

- If \(c\) is absent from \(Q\), choose any three branch vertices.
- If \(c\) is a branch vertex, discard it.
- If \(c\) is internal to a replacement path, discard one endpoint of that path.

In the last case, internal disjointness ensures that \(c\) lies on no other replacement path.

But \(D_d-c\) has only arcs from \(B\) to \(A\), and none from \(A\) to \(B\). Hence every strongly connected subdigraph of \(D_d-c\) lies entirely in \(A\) or entirely in \(B\). A subdivision of \(\overleftrightarrow{K_3}\) is strongly connected, so this contradicts Section 2.2.

Thus
\[
\boxed{\mu_{\kappa'}(\overleftrightarrow{K_4})=\infty.}
\]

Finally, \(D_d\) is strong but \(D_d-c\) is not, so
\[
\boxed{\kappa(D_d)=1.}
\]
This last observation is essential: the construction does not refute the vertex-connectivity half.

## 3. A sharp positive class for strong vertex-connectivity

Here is a special case of the remaining question with the smallest possible threshold.

### Theorem

Let \(F\) be a digraph on \(n\ge2\) vertices. Suppose there is a vertex \(r\) such that deleting every arc with head \(r\) leaves an orientation of a forest. Then
\[
\boxed{\mu_\kappa(F)=n-1.}
\]

More strongly, in every digraph \(D\) with \(\kappa(D)\ge n-1\), the image of \(r\) can be prescribed arbitrarily.

The same conclusion holds with “head” replaced by “tail.”

### Proof

Let
\[
F_0=F-\{ur:ur\in A(F)\}.
\]
By hypothesis, \(F_0\) is an orientation of a forest. Fix \(x\in V(D)\), to be the image of \(r\).

Since \(\kappa(D)\ge n-1\),
\[
\delta^+(D),\delta^-(D)\ge n-1.
\]
Consequently, \(F_0\) can be embedded as a subgraph of \(D\), with \(r\) mapped to \(x\): root its underlying forest, start the component containing \(r\) at \(x\), and embed vertices one at a time along forest edges. When adding a vertex, at most \(n-2\) already used vertices can be forbidden neighbors of its parent, whereas the required in- or out-neighborhood has size at least \(n-1\). Roots of other components can be placed at arbitrary unused vertices.

Write this embedding as \(\phi\). Let
\[
U=\phi(N_F^-(r)),\qquad q=|U|.
\]
If \(q=0\), the embedding already gives \(F\).

Suppose \(q\ge1\), and delete
\[
S=\phi(V(F))\setminus\bigl(U\cup\{x\}\bigr).
\]
Then
\[
|S|=n-q-1
\]
and
\[
\kappa(D-S)\ge(n-1)-(n-q-1)=q.
\]

We use the directed fan consequence of Menger’s theorem:

> If \(G\) is strongly \(q\)-connected, \(x\notin U\), and \(|U|=q\), then there are directed \(u\)-to-\(x\) paths, one for each \(u\in U\), whose only common vertex is \(x\).

Indeed, add a new source adjacent to every vertex of \(U\). A separator of size less than \(q\) leaves some vertex of \(U\), which can still reach \(x\) by strong \(q\)-connectivity.

Apply this fact in \(D-S\). The resulting paths meet the embedded vertices of \(F\) only at their respective starting vertices and at \(x\): all other embedded vertices were deleted, and a fan path cannot contain another member of \(U\).

Use these paths to replace the deleted arcs entering \(r\), and retain the embedded forest arcs. This is a subdivision of \(F\), proving
\[
\mu_\kappa(F)\le n-1.
\]

For the reverse inequality, \(\overleftrightarrow{K_{n-1}}\) has connectivity \(n-2\) and has too few vertices to contain a subdivision of \(F\). Thus equality holds.

Reversing all arcs proves the common-tail version. ∎

### Examples

The theorem includes:

- every orientation of a forest;
- an out-arborescence with any additional arcs directed to its root;
- any collection of directed cycles sharing exactly one common vertex and otherwise vertex-disjoint.

In particular, if \(S\) is a star with \(q\) leaves, then
\[
\boxed{\mu_\kappa(\overleftrightarrow S)=q.}
\]
Thus bidirected stars have an exact positive answer for vertex-connectivity, despite the negative arc-connectivity phenomenon reported in the question.

## 4. A general lower bound for the remaining question

Let \(\tau_{\rm arc}(F)\) denote the minimum size of a feedback arc set of \(F\).

### Proposition

For every digraph \(F\) on \(n\ge2\) vertices,
\[
\boxed{\mu_\kappa(F)\ge
\max\{n-1,\tau_{\rm arc}(F)\}.}
\]

### Proof

The lower bound \(n-1\) follows from \(\overleftrightarrow{K_{n-1}}\), as above.

Suppose \(\tau_{\rm arc}(F)\ge2\), and put
\[
q=\tau_{\rm arc}(F)-1,\qquad \ell=n+1.
\]
Construct a digraph \(C_{\ell,q}\) with independent vertex classes
\[
V_0,\ldots,V_{\ell-1},
\qquad |V_i|=q,
\]
and all arcs from \(V_i\) to \(V_{i+1}\), with indices modulo \(\ell\). There are no other arcs.

Deleting fewer than \(q\) vertices leaves every class nonempty, and the resulting digraph remains strongly connected. Deleting an entire class leaves an acyclic digraph with at least two vertices. Hence
\[
\kappa(C_{\ell,q})=q.
\]

Suppose \(C_{\ell,q}\) contained a subdivision of \(F\). Since there are \(n\) branch vertices and \(n+1\) classes, some class \(V_j\) contains no branch vertex.

Let \(E_0\subseteq A(F)\) consist of the arcs whose replacement paths meet \(V_j\). All such meetings are at internal vertices. Internal disjointness therefore gives
\[
|E_0|\le |V_j|=q.
\]

Every directed cycle of the subdivision meets \(V_j\), because \(C_{\ell,q}-V_j\) is acyclic. Consequently, every directed cycle of \(F\) contains an arc of \(E_0\). Thus \(E_0\) is a feedback arc set, contradicting
\[
\tau_{\rm arc}(F)=q+1.
\]

This proves the feedback-arc lower bound when \(\tau_{\rm arc}(F)\ge2\); the remaining cases follow already from \(n-1\ge1\). ∎

For a bidirected graph \(\overleftrightarrow G\),
\[
\tau_{\rm arc}(\overleftrightarrow G)=|E(G)|.
\]
At least one arc must be deleted from each digon, and equality is achieved by retaining only arcs directed forward in a fixed vertex ordering. Therefore
\[
\mu_\kappa(\overleftrightarrow G)
\ge \max\{|V(G)|-1,\ |E(G)|\}.
\]

In particular,
\[
\boxed{\mu_\kappa(\overleftrightarrow{K_t})\ge\binom t2.}
\]
For example, the cyclic blow-up with five classes of five vertices is strongly \(5\)-connected and contains no subdivision of \(\overleftrightarrow{K_4}\).

## 5. What remains unresolved

The universal \(\kappa'\)-maderian assertion is false, with the explicit construction above supplying a complete counterexample.

The universal \(\kappa\)-maderian assertion is **not settled here**. The positive theorem works because all missing arcs can be supplied by one directed fan to a common head. For arbitrary targets, the required paths have several prescribed heads and tails, and the argument supplies no corresponding simultaneous linkage. Iterating the fan construction is also unjustified: the first fan may use arbitrarily many vertices.

Thus the remaining gap is precisely the existence of a finite connectivity threshold for every fixed target—not any unverified case in the constructions or special-case proofs above.