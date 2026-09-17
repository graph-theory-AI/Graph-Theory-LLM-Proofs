```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for finite loopless multigraphs with maximum average degree at most 4 and maximum degree at least 8.",
  "would_publish": false,
  "caveats": "A self-contained special case only; no novelty claim, and the general conjecture remains unresolved."
}
```

# A sparse-multigraph case

I use the standard convention that multigraphs are finite and loopless, with degrees counting multiplicities. Define
\[
\operatorname{mad}(H)
=\max_{\substack{F\subseteq H\\V(F)\ne\varnothing}}
\frac{2|E(F)|}{|V(F)|}.
\]

The following result comes from a different route than the previous end-block argument. Its key reduction is an alternating-cycle configuration that need not lie in an end block. I have not verified the literature status of this particular bound and make no novelty claim.

**Theorem.** If \(H\) is a loopless multigraph with \(\operatorname{mad}(H)\le4\), then
\[
\boxed{\quad
\chi_\ell(T(H))\le \max\{9,\Delta(H)+1\}.
\quad}
\]
Consequently, if also \(\Delta(H)\ge8\), then
\[
\boxed{\quad
\chi_\ell(T(H))=\chi(T(H))=\Delta(H)+1.
\quad}
\]

The equality follows from the upper bound because a maximum-degree vertex, together with its incident edges, forms a clique of order \(\Delta(H)+1\) in \(T(H)\).

## 1. Minimal-counterexample setup

We prove the following parameterized version of the upper bound:

> For every integer \(D\ge8\), every multigraph \(H\) satisfying
> \[
> \Delta(H)\le D,\qquad \operatorname{mad}(H)\le4
> \]
> is total-colorable from arbitrary lists of size \(k=D+1\).

Suppose otherwise, and choose a counterexample \((H,L)\) with the fewest vertices. Lists are assigned to both vertices and edges of \(H\). Deleting any nonempty set of vertices, together with their incident edges, gives a smaller multigraph satisfying the same hypotheses. Thus its inherited lists admit a total coloring.

### A star-extension observation

Delete a vertex \(v\), color \(H-v\), and consider a new edge \(e=vu\). At its endpoint \(u\), the colored elements forbidding colors on \(e\) are:

- the vertex \(u\);
- the edges incident with \(u\) that were not deleted.

There are at most \(d_H(u)\) such elements, even when \(vu\) has multiplicity greater than one. Hence
\[
|L_{\mathrm{res}}(e)|\ge k-d_H(u)=D+1-d_H(u).
\tag{1}
\]

All new edges are incident with \(v\), so assigning them distinct colors completes the edge part of the extension. If \(d_H(v)=r\le3\), the vertex \(v\) then has at most \(2r\le6<k\) forbidden colors and can be colored last.

This gives three necessary properties of \(H\).

1. **Every vertex has degree at least two.**

   A vertex of degree zero or one extends immediately.

2. **Both incident edges of every degree-two vertex lead to vertices of degree \(D\).**

   Otherwise the two new edges have residual lists of sizes at least \(1\) and \(2\), respectively, and can receive distinct colors.

3. **For every degree-three vertex, either**
   - at least two incident edges lead to degree-\(D\) vertices; or
   - all three lead to vertices of degree at least \(D-1\).

   Indeed, if neither condition holds, the three residual lists can be ordered to have sizes at least \(1,2,3\). Greedy distinct representatives color the three edges.

Statements about incident edges count multiplicities. In particular, two such edges may have the same other endpoint.

Partition the degree-three vertices into:

- **Type A:** two incident edges lead to degree-\(D\) vertices, while the remaining edge leads to a vertex of degree at most \(D-2\);
- **Type B:** all three incident edges lead to vertices of degree \(D-1\) or \(D\).

Property 3 says that every degree-three vertex belongs to exactly one of these types.

## 2. An auxiliary forest

Construct an auxiliary multigraph \(A\) as follows.

- Its vertices are the degree-\(D\) vertices of \(H\).
- Each degree-two vertex of \(H\) gives an edge joining the other endpoints of its two incident edges.
- Each type-A vertex gives an edge joining the other endpoints of its two edges leading to degree-\(D\) vertices.

Loops and parallel edges are permitted in this construction.

**Lemma.** \(A\) is a forest; in particular, it has no loops or parallel-edge cycles.

**Proof.** Suppose \(A\) contains a cycle, and let \(X\) be the vertices of \(H\) representing its edges.

For each \(x\in X\), designate its two incident edges leading to the corresponding degree-\(D\) vertices as its *main edges*. When the auxiliary cycle has length at least two, these main edges form an even cycle in \(H\). An auxiliary loop instead corresponds to two parallel main edges.

Delete \(X\), and total-color \(H-X\) by minimality.

### Coloring the main edges

Each degree-\(D\) vertex on the auxiliary cycle has exactly two uncolored incident edges. Its vertex element and its other \(D-2\) incident edges are already colored. Consequently, every main edge retains at least
\[
k-(D-1)=2
\]
colors.

The main edge-elements induce an even cycle, or a \(K_2\) in the auxiliary-loop case. They can therefore be colored from these residual lists.

Here is the elementary even-cycle list argument. Trim the lists to size two. If they are all equal, alternate the two colors. Otherwise, choose adjacent vertices with unequal lists, color one with a color absent from the other's list, and proceed greedily around the cycle toward the other vertex. The final vertex has only one forbidden color belonging to its list.

### Coloring the remaining new edges

Every type-A vertex in \(X\) has one additional edge, whose other endpoint has degree at most \(D-2\). Degree-two vertices in \(X\) have no additional edge.

The additional edges consist of:

- stars centered at vertices outside \(X\); and
- a matching whose endpoints both lie in \(X\).

These edge-components are mutually nonincident, because every vertex in \(X\) has at most one additional edge.

Consider a star with center \(u\notin X\), containing \(q\) additional edges. For an edge \(xu\) of this star, the colored elements that forbid colors are at most:

- the vertex \(u\);
- the \(d_H(u)-q\) already colored edges at \(u\);
- the two main edges at \(x\).

Thus
\[
\begin{aligned}
|L_{\mathrm{res}}(xu)|
&\ge k-\bigl(1+d_H(u)-q+2\bigr)\\
&=D-d_H(u)+q-2\\
&\ge q,
\end{aligned}
\tag{2}
\]
because \(d_H(u)\le D-2\). The \(q\) edges can receive distinct colors greedily.

An additional edge with both endpoints in \(X\) loses at most four colors, those on the main edges at its endpoints. It retains at least \(k-4>0\) colors. These internal additional edges form a matching, so they can also be colored.

Finally, color the vertex elements in \(X\). Each has degree at most three in \(H\), hence at most six neighbors in \(T(H)\). Since \(k\ge9\), greedy coloring finishes the extension.

This contradicts the choice of \(H\). Therefore \(A\) is a forest. \(\square\)

Let
\[
\begin{aligned}
p&=\#\{\text{degree-two vertices}\},\\
a&=\#\{\text{type-A vertices}\},\\
b&=\#\{\text{type-B vertices}\},\\
h&=\#\{\text{degree-}D\text{ vertices}\},\\
g&=\#\{\text{degree-}(D-1)\text{ vertices}\}.
\end{aligned}
\]
The auxiliary forest has \(h\) vertices and \(p+a\) edges. Consequently,
\[
p+a\le h-1\qquad\text{if }h>0,
\tag{3}
\]
and \(p=a=0\) if \(h=0\).

## 3. Counting degrees

Because \(\operatorname{mad}(H)\le4\),
\[
S:=\sum_{v\in V(H)}(d_H(v)-4)\le0.
\tag{4}
\]

Write
\[
R=\sum_{j=5}^{D-2}(j-4)n_j\ge0,
\]
where \(n_j\) is the number of degree-\(j\) vertices. Since there are no vertices of degree zero or one,
\[
S=-2p-a-b+(D-4)h+(D-5)g+R.
\tag{5}
\]

Count incidences at vertices of degrees \(D\) and \(D-1\).

- Each degree-two vertex contributes two such incidences.
- Each type-A vertex contributes two.
- Each type-B vertex contributes three.

Therefore
\[
2p+2a+3b\le Dh+(D-1)g.
\tag{6}
\]
Substituting the resulting upper bound on \(b\) into (5) gives
\[
3S\ge
(2D-12)h+(2D-14)g-4p-a+3R.
\tag{7}
\]

### Case 1: \(h>0\)

By the forest inequality,
\[
4p+a\le4(p+a)\le4h-4.
\]
Hence
\[
3S\ge
(2D-16)h+(2D-14)g+4+3R.
\tag{8}
\]
For \(D\ge8\), the right-hand side is strictly positive. This contradicts (4).

### Case 2: \(h=0\)

Then \(p=a=0\), and (7) gives
\[
3S\ge(2D-14)g+3R.
\]
Since \(S\le0\), \(D\ge8\), and \(R\ge0\), we obtain \(g=R=0\). Equation (6) now gives \(b=0\).

Thus every vertex of \(H\) has degree four. But then
\[
\Delta(T(H))\le8:
\]
a vertex element has at most four incident edge-elements and four neighboring vertex-elements, and an edge-element has at most eight neighbors. Therefore \(T(H)\) is greedily colorable from lists of size at least nine, again a contradiction.

Both cases are impossible. This proves the parameterized statement and hence
\[
\chi_\ell(T(H))\le\max\{9,\Delta(H)+1\}.
\]
The asserted equality for \(\Delta(H)\ge8\) follows from the clique lower bound. \(\square\)

## 4. Consequences and limitations

This settles the conjecture, with the exact value \(\Delta(H)+1\), for a family substantially larger than the cactus family in the previous attempt. For example, it covers:

- every \(2\)-degenerate graph with maximum degree at least eight;
- every simple triangle-free planar graph with maximum degree at least eight.

The first inclusion follows by repeatedly deleting vertices of degree at most two; the second follows from the planar edge bound applied to every subgraph.

There is also a useful consequence stated directly in terms of the conjecture:

> If \(H\) has \(\operatorname{mad}(H)\le4\) and  
> \(\chi(T(H))\ge9\), then \(\chi_\ell(T(H))=\chi(T(H))\).

Indeed, apply the parameterized theorem with \(D=\chi(T(H))-1\); the clique bound guarantees \(\Delta(H)\le D\). Thus any counterexample within the class \(\operatorname{mad}(H)\le4\) must have total chromatic number at most eight.

The remaining gaps are genuine:

- Without the maximum-average-degree hypothesis, inequality (4) is unavailable.
- For \(D=7\), the coefficient \(2D-16\) in (8) becomes negative, so this counting argument does not establish the corresponding eight-list bound.
- The proof therefore does not settle dense multigraphs or all low-degree sparse multigraphs.

No proof or counterexample to the full List Total Colouring Conjecture is obtained here.