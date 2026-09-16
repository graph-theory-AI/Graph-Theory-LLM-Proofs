```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A constructive two-vertex reduction proves the conjecture when deleting one vertex makes the tournament transitive, and a dominant-cut criterion gives another family.",
  "would_publish": false,
  "caveats": "No unrestricted proof or counterexample; novelty of these elementary special cases is not claimed."
}
```

## 1. What is proved here

Write
\[
e_D(v)=d_D^+(v)-d_D^-(v),\qquad
\operatorname{ex}(D)=\sum_v(e_D(v))_+,
\]
where \(x_+=\max\{x,0\}\). All paths below are vertex-simple and nonempty, and a decomposition partitions the arcs.

I prove the conjectured equality for two classes:

1. **Even tournaments that become transitive after deleting one vertex.**
2. **Tournaments admitting a dominant cut \(A\to B\)** satisfying
   \[
   d^-_{T[A]}(a)\le |B|\quad(a\in A),\qquad
   d^+_{T[B]}(b)\le |A|\quad(b\in B).
   \]
   This includes every tournament with a balanced dominant cut, and every even tournament whose strongly connected components have order at most three.

The first result follows from a local extension lemma that also restricts the structure of a minimum-order counterexample.

### Endpoint accounting

For a path decomposition \(\mathcal P\), let \(s(v)\) and \(t(v)\) count its paths starting and ending at \(v\). Then
\[
s(v)-t(v)=e_D(v),
\]
and consequently
\[
|\mathcal P|-\operatorname{ex}(D)
=\sum_v\min\{s(v),t(v)\}\ge 0. \tag{1}
\]

Call a decomposition **perfect** if it has exactly \(\operatorname{ex}(D)\) paths. Equation (1) shows that in a perfect decomposition:

- if \(e_D(v)>0\), exactly \(e_D(v)\) paths start at \(v\), and none end there;
- if \(e_D(v)<0\), exactly \(-e_D(v)\) paths end at \(v\), and none start there.

For an even tournament, every \(e_D(v)\) is odd and hence nonzero.

## 2. A two-vertex extension lemma

**Lemma.** Let \(H\) be an even tournament of order \(r\ge2\) with a perfect path decomposition, and fix \(v\in V(H)\). Add vertices \(a,b\) such that
\[
a\to b,\qquad a\to x\to b
\quad\text{for every }x\in V(H)\setminus\{v\}.
\]
The orientations between \(v\) and \(\{a,b\}\) are arbitrary. Then the resulting tournament \(T\) has a perfect path decomposition.

**Proof.** Put \(\varepsilon=e_H(v)\), which is nonzero. Every old vertex other than \(v\) receives one new incoming arc and one new outgoing arc, so its excess is unchanged. There are four cases.

### Case 1: \(a\to v\to b\)

All old excesses are unchanged, while
\[
e_T(a)=r+1,\qquad e_T(b)=-(r+1).
\]
Thus
\[
\operatorname{ex}(T)=\operatorname{ex}(H)+r+1.
\]

Add the \(r\) paths
\[
a\to x\to b\qquad(x\in V(H))
\]
and the one-arc path \(a\to b\). These cover precisely the new arcs and give the required count.

### Case 2: \(v\to a\) and \(v\to b\)

Here
\[
e_T(a)=r-1,\qquad e_T(b)=-(r+1),\qquad
e_T(v)=\varepsilon+2.
\]
Set
\[
k=\min\{2,(-\varepsilon)_+\}.
\]
Then
\[
\begin{aligned}
\operatorname{ex}(T)-\operatorname{ex}(H)
&=r-1+(\varepsilon+2)_+-\varepsilon_+\\
&=r+1-k. \tag{2}
\end{aligned}
\]

Initially add the \(r+1\) paths
\[
a\to x\to b\quad(x\ne v),\qquad
v\to a\to b,\qquad v\to b.
\]
If \(k>0\), the perfect decomposition of \(H\) has at least \(k\) distinct paths ending at \(v\). Concatenate \(k\) such paths with \(k\) of the two new paths starting at \(v\).

Each concatenation is simple: beyond the common vertex \(v\), the appended portion uses only the new vertices \(a,b\). Each concatenation reduces the number of paths by one. The resulting count is exactly the value required by (2).

### Case 3: \(a\to v\) and \(b\to v\)

Reverse all arcs and interchange the names \(a,b\). This gives Case 2. Reversal preserves \(\operatorname{ex}\) and reverses each path, so the conclusion follows.

### Case 4: \(v\to a\) and \(b\to v\)

Now every old excess is unchanged, and
\[
e_T(a)=r-1,\qquad e_T(b)=-(r-1).
\]
Hence
\[
\operatorname{ex}(T)=\operatorname{ex}(H)+r-1. \tag{3}
\]

Alongside the old decomposition, take the \(r-1\) paths
\[
A_x=a\to x\to b\qquad(x\ne v).
\]
The remaining new arcs form the triangle
\[
v\to a\to b\to v.
\]

Choose any \(x\ne v\).

If \(\varepsilon>0\), choose an old path
\[
P=(v,p_1,\ldots,p_\ell)
\]
starting at \(v\). Replace \(P\) and \(A_x\) by
\[
(a,b,v,p_1,\ldots,p_\ell)
\quad\text{and}\quad
(v,a,x,b). \tag{4}
\]
These two paths cover exactly the arcs of \(P\), \(A_x\), and the additional triangle.

Both are simple. The first merely prepends two new vertices to \(P\), and the second has four distinct vertices. It does not matter whether \(x\) occurs in \(P\), since different paths may share vertices.

If \(\varepsilon<0\), choose an old path
\[
P=(p_0,\ldots,p_\ell=v)
\]
ending at \(v\), and replace \(P,A_x\) by
\[
(p_0,\ldots,p_\ell=v,a,b)
\quad\text{and}\quad
(a,x,b,v). \tag{5}
\]
The same verification applies.

In either situation, the triangle is absorbed without changing the number of paths. The final count is therefore \(\operatorname{ex}(H)+r-1\), as required by (3). This covers all four orientations. \(\square\)

## 3. Deleting one vertex leaves a transitive tournament

**Theorem.** If \(T\) is an even tournament and \(T-v\) is transitive for some vertex \(v\), then \(T\) has a perfect path decomposition.

**Proof.** Induct on the even order \(n\). Order two is immediate.

For \(n\ge4\), write the transitive ordering of \(T-v\) as
\[
w_1,w_2,\ldots,w_{n-1},
\qquad w_i\to w_j\quad(i<j).
\]
Set
\[
a=w_1,\qquad b=w_{n-1},\qquad H=T-\{a,b\}.
\]
The tournament \(H\) has even order, and \(H-v\) is transitive. By induction, \(H\) has a perfect decomposition.

Moreover,
\[
a\to b,\qquad a\to x\to b
\quad\text{for all }x\in V(H)\setminus\{v\}.
\]
The extension lemma therefore gives a perfect decomposition of \(T\). \(\square\)

This is not restricted to acyclic or non-strong tournaments. For example, requiring
\[
v\to w_1,\qquad w_{n-1}\to v
\]
makes the tournament strongly connected, regardless of the orientations between \(v\) and the intermediate vertices.

The proof is constructive. Given \(v\) and the transitive ordering, each inductive step adds \(O(n)\) short paths and changes at most two existing paths. With linked-list path representations and endpoint lists, the construction takes \(O(n^2)\) time, matching the size of the arc output.

### Small-order consequence

Every tournament of order four contains a transitive triple: any vertex has either two outneighbours or two inneighbours, and those three vertices induce a transitive tournament. Thus the theorem proves the conjecture for orders two and four without enumeration.

## 4. A dominant-cut criterion

Here is an independent sufficient condition that can accommodate arbitrarily many vertex-disjoint directed cycles.

**Theorem.** Suppose
\[
V(T)=A\mathbin{\dot\cup}B,\qquad A,B\ne\varnothing,
\]
and every arc between the parts is directed from \(A\) to \(B\). Assume
\[
d^-_{T[A]}(a)\le |B|\quad(a\in A), \tag{6}
\]
and
\[
d^+_{T[B]}(b)\le |A|\quad(b\in B). \tag{7}
\]
Then \(T\) has a perfect decomposition into \(|A||B|\) paths, each of length at most three.

**Proof.** For each \(a\in A\), use (6) to assign its incoming arcs in \(T[A]\) injectively to its \(|B|\) outgoing crossing arcs. Thus an internal arc \(x\to a\) is assigned to some crossing arc \(a\to b\).

Independently, for each \(b\in B\), use (7) to assign its outgoing arcs in \(T[B]\) injectively to its \(|A|\) incoming crossing arcs. Thus an internal arc \(b\to y\) is assigned to some crossing arc \(a\to b\).

For each crossing arc \(a\to b\), form one path:

- prepend \(x\) if \(x\to a\) was assigned to \(a\to b\);
- append \(y\) if \(b\to y\) was assigned to \(a\to b\).

The resulting path has one of the forms
\[
(a,b),\quad (x,a,b),\quad (a,b,y),\quad (x,a,b,y).
\]
It is simple because it contains at most two distinct vertices from each of the disjoint parts.

Every crossing arc appears once, and every internal arc appears once by its assignment. Hence these are \(|A||B|\) paths decomposing \(T\).

Finally, for \(a\in A\),
\[
e_T(a)=|B|+d^+_{T[A]}(a)-d^-_{T[A]}(a)\ge0,
\]
whereas for \(b\in B\),
\[
e_T(b)=d^+_{T[B]}(b)-d^-_{T[B]}(b)-|A|\le0.
\]
Therefore
\[
\operatorname{ex}(T)
=\sum_{a\in A}e_T(a)
=|A||B|,
\]
since the internal degree differences in \(T[A]\) sum to zero. \(\square\)

### Two consequences

**Balanced dominant cuts.** If \(|A|=|B|=m\), conditions (6)–(7) hold automatically. Thus any tournament consisting of an arbitrary \(m\)-vertex tournament dominating another arbitrary \(m\)-vertex tournament has a perfect decomposition into \(m^2\) paths.

**Strong components of order at most three.** Every even tournament whose strongly connected components have order at most three also satisfies the conjecture.

To verify the second claim, linearly order the strong components by domination. Their orders are one or three. Write \(n=2m\).

If a component boundary occurs after exactly \(m\) vertices, use the balanced-cut consequence. Otherwise the midpoint lies inside a directed triangle \(C\). The numbers of vertices before and after \(C\) are then \(m-1,m-2\), in one order.

Suppose there are \(m-1\) vertices before \(C\). Take these as \(A\), and take \(C\) together with the remaining \(m-2\) vertices as \(B\). Then
\[
|A|=m-1,\qquad |B|=m+1.
\]
Condition (6) is automatic. Every vertex of \(C\) has exactly one outneighbour in \(C\), so every vertex of \(B\) has internal outdegree at most
\[
1+(m-2)=m-1=|A|.
\]
Thus (7) holds. The other ordering follows by reversal.

## 5. What remains missing

The extension lemma gives a genuine reduction:

> A minimum-order counterexample cannot contain vertices \(a,b,v\) with
> \[
> a\to b,\qquad a\to x\to b
> \quad\text{for all }x\notin\{a,b,v\}.
> \]

Indeed, deleting \(a,b\) would leave a smaller even tournament, to which minimality and then the lemma would apply.

But tournaments need not contain such a pair. In particular, an almost regular tournament of even order at least six has indegree and outdegree at least two at every vertex. It therefore cannot contain the extreme pair required by the lemma: that pair has \(d^-(a)\le1\) and \(d^+(b)\le1\).

The dominant-cut argument likewise does not address general strongly connected tournaments. In particular, it does not resolve the difficult almost-regular case, where the desired paths must all be Hamilton paths.

Thus the arguments above establish constructive special cases and a local reduction, but supply neither an unrestricted proof nor a counterexample.