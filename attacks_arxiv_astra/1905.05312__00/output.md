```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound, including its equality characterization, holds for K4-free graphs with minimum degree at least n/2.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; the minimum-degree and K4-free restrictions are substantial, and novelty of this special case is unchecked."
}
```

## 1. A restricted theorem

Write \(t(G)\) for the number of triangles and
\[
c_G(xy)=|N_G(x)\cap N_G(y)|
\]
for the number of triangles containing an edge \(xy\). Thus the book number is \(\max_{xy\in E(G)}c_G(xy)\).

I prove the following special case, without making a claim of novelty.

**Theorem.** Let \(n,b\) be positive integers with
\[
\frac n6\le b<\frac n4.
\]
Suppose that \(G\) is a \(K_4\)-free graph on \(n\) vertices satisfying
\[
\delta(G)\ge \frac n2,\qquad \operatorname{bk}(G)\le b,
\]
and that \(G\) is not the balanced complete bipartite graph. Then
\[
t(G)\ge b^2(n-4b).
\]
Equality holds if and only if \(n\) is even and \(G\cong S_{b,n}\).

The edge-count hypothesis of the original conjecture is automatic here. For odd \(n\), this theorem gives strict inequality; the odd-order construction \(S_{b,n}\) has minimum degree below \(n/2\), so is outside this restricted class.

Put
\[
p=\frac n2,\qquad a=p-2b.
\]
The parameter range becomes
\[
0<a\le b,\qquad p=2b+a,
\]
and the desired bound is
\[
t(G)\ge 2ab^2. \tag{1}
\]

## 2. A codegree inequality

The following observation does not require \(K_4\)-freeness.

Suppose \(\delta(G)\ge p\). For every triangle \(xyz\), inclusion–exclusion gives
\[
\begin{aligned}
c_G(xy)+c_G(yz)+c_G(zx)
&=d(x)+d(y)+d(z)-|N(x)\cup N(y)\cup N(z)|\\
&\qquad+|N(x)\cap N(y)\cap N(z)|\\
&\ge 3p-2p=p.
\end{aligned} \tag{2}
\]
Consequently, every edge that lies in a triangle has codegree at least
\[
p-2b=a. \tag{3}
\]

Let \(m_+\) be the number of edges that lie in at least one triangle. For such an edge, \(a\le c_G(e)\le b\), and therefore
\[
c_G(e)^2\le (a+b)c_G(e)-ab.
\]
Summing and using (2),
\[
pt(G)
\le \sum_e c_G(e)^2
\le 3(a+b)t(G)-abm_+.
\]
Since \(3(a+b)-p=b+2a\), this proves
\[
\boxed{\quad t(G)\ge \frac{ab}{b+2a}\,m_+.\quad} \tag{4}
\]

In particular, if every edge lies in a triangle, then \(m_+=e(G)\ge p^2\), so
\[
t(G)\ge \frac{abp^2}{b+2a}>2ab^2. \tag{5}
\]
The strict inequality follows from
\[
p^2-2b(b+2a)=(2b+a)^2-2b(b+2a)=2b^2+a^2>0.
\]

Thus a graph relevant to equality—or to a counterexample with minimum degree at least \(n/2\)—must have an edge lying in no triangle.

## 3. An auxiliary inequality for triangle-free graphs

The next lemma supplies the sharp estimate when such an edge exists.

**Lemma.** Let \(0<a\le b\), and put \(p=2b+a\). Suppose \(H\) is a nonempty triangle-free graph such that
\[
\Delta(H)\le b
\]
and
\[
d_H(u)+d_H(v)\ge p-b=b+a
\quad\text{for every }uv\in E(H).
\]
Then
\[
p\,e(H)-\sum_{v\in V(H)}d_H(v)^2\ge ab^2. \tag{6}
\]
Equality holds precisely when, after deleting isolated vertices, \(H\) is either \(K_{b,a}\) or \(K_{b,b}\). As usual, an equality alternative is possible only when its part sizes are integers.

**Proof.** Let \(D=\Delta(H)\), choose a vertex \(u\) of degree \(D\), and set
\[
X=N_H(u),\qquad Y=V(H)\setminus X,\qquad s=b+a-D.
\]
The edge-degree condition implies
\[
\frac{b+a}{2}\le D\le b,\qquad a\le s\le D,
\]
and every \(x\in X\) has degree between \(s\) and \(D\).

Because \(H\) is triangle-free, \(X\) is independent. Write
\[
E=\sum_{x\in X}d_H(x)=e_H(X,Y),\qquad q=e(H[Y]).
\]
Then \(e(H)=E+q\), while
\[
\sum_{y\in Y}d_H(y)^2
\le D\sum_{y\in Y}d_H(y)=D(E+2q).
\]
Hence
\[
\begin{aligned}
p\,e(H)-\sum_vd_H(v)^2
&\ge \sum_{x\in X}d_H(x)\bigl(p-D-d_H(x)\bigr)+(p-2D)q.
\end{aligned} \tag{7}
\]

For \(s\le r\le D\le b\), the identity \(p-D-s=b\) gives
\[
r(p-D-r)=bs+(r-s)(b-r)\ge bs.
\]
Also \(p-2D\ge a>0\). Thus (7) is at least
\[
bDs=bD(b+a-D)
=ab^2+b(b-D)(D-a)\ge ab^2.
\]

For equality, necessarily \(D=b\) and \(q=0\). Equality in the square-degree estimate also forces every nonisolated vertex of \(Y\) to have degree \(b\). Since \(|X|=b\), each such vertex is adjacent to all of \(X\). If there are \(k\) of these vertices, the nontrivial component is therefore \(K_{b,k}\). Finally, equality in
\[
r(p-b-r)=ba+(r-a)(b-r)
\]
forces \(k=a\) or \(k=b\). Both stated graphs attain equality. ∎

## 4. Proof of the theorem: a triangle-free edge

By (5), we may assume that \(G\) has an edge \(xy\) with
\[
N(x)\cap N(y)=\varnothing.
\]
The minimum-degree condition implies
\[
n\ge d(x)+d(y)\ge 2p=n.
\]
Consequently, \(n\) is even, \(d(x)=d(y)=p\), and
\[
A=N(x),\qquad B=N(y)
\]
partition \(V(G)\), with \(|A|=|B|=p\).

Let
\[
H_A=G[A],\qquad H_B=G[B].
\]
Both graphs are triangle-free: a triangle in \(N(x)\), for example, would form a \(K_4\) with \(x\). Moreover,
\[
d_{H_A}(v)=c_G(xv)\le b\qquad(v\in A),
\]
and similarly \(\Delta(H_B)\le b\).

Neither internal graph is empty. Indeed, if \(H_A\) were empty, minimum degree would force every edge between \(A\) and \(B\). An edge inside \(B\) would then have at least \(p>b\) common neighbors. Hence \(H_B\) would also be empty, giving the excluded graph \(K_{p,p}\).

For an edge \(uv\in E(H_A)\), its endpoints have at least
\[
p-d_{H_A}(u),\qquad p-d_{H_A}(v)
\]
neighbors in \(B\). Therefore
\[
b\ge c_G(uv)\ge p-d_{H_A}(u)-d_{H_A}(v),
\]
so
\[
d_{H_A}(u)+d_{H_A}(v)\ge p-b.
\]
The same holds in \(H_B\). The lemma applies to both internal graphs.

Every triangle has exactly one internal edge in one of these two graphs. Counting through that edge gives
\[
\begin{aligned}
t(G)
&\ge \sum_{uv\in E(H_A)}
       \bigl(p-d_{H_A}(u)-d_{H_A}(v)\bigr)\\
&\qquad+\sum_{uv\in E(H_B)}
       \bigl(p-d_{H_B}(u)-d_{H_B}(v)\bigr)\\
&=\left(p\,e(H_A)-\sum_{v\in A}d_{H_A}(v)^2\right)
 +\left(p\,e(H_B)-\sum_{v\in B}d_{H_B}(v)^2\right)\\
&\ge 2ab^2.
\end{aligned}
\]
This proves (1).

## 5. Equality

Suppose now that \(t(G)=2ab^2\).

### First, equality forces regularity

For \(v\in V(G)\), write
\[
\varepsilon_v=d_G(v)-p\ge0,
\]
and let \(h_v\) denote its degree within its own part, \(A\) or \(B\).

The preceding common-neighbor estimate can be sharpened to
\[
c_G(uv)\ge p-h_u-h_v+\varepsilon_u+\varepsilon_v
\]
for every internal edge \(uv\). Consequently,
\[
t(G)\ge
\left(p\,e(H_A)-\sum_{v\in A}h_v^2\right)
+\left(p\,e(H_B)-\sum_{v\in B}h_v^2\right)
+\sum_v\varepsilon_vh_v.
\]
Equality forces \(\varepsilon_vh_v=0\) for every \(v\). If \(h_v>0\), this gives \(d_G(v)=p\). If \(h_v=0\), all neighbors of \(v\) lie in an opposite part of size \(p\), so again \(d_G(v)=p\).

Thus \(G\) is \(p\)-regular. In particular,
\[
e(H_A)=e(H_B). \tag{8}
\]

### The internal graphs and missing cross-edges

By the equality statement of the lemma, each internal graph is either \(K_{b,a}\) or \(K_{b,b}\), together with isolated vertices. Equation (8) forces the same alternative on both sides.

We may therefore write
\[
A=A_0\sqcup A_1\sqcup A_2,\qquad
B=B_0\sqcup B_1\sqcup B_2,
\]
where the internal edges are exactly \(A_1A_2\) and \(B_1B_2\), and
\[
|A_1|=|B_1|=b,\qquad |A_2|=|B_2|=s,
\]
with \(s\in\{a,b\}\). The isolated parts have size
\[
|A_0|=|B_0|=q=p-b-s,
\]
so \(\{q,s\}=\{a,b\}\).

Let \(M\) be the bipartite graph of **missing** edges between \(A\) and \(B\). Regularity gives
\[
d_M(v)=h_v.
\]
For every internal edge \(uv\), equality in the common-neighbor estimate says
\[
N_M(u)\cap N_M(v)=\varnothing. \tag{9}
\]
Thus the missing neighbors of any vertex lie wholly in one of the two active parts on the opposite side. There are no missing edges incident to \(A_0\) or \(B_0\).

If \(s<b\), each vertex of \(A_2\) has \(b\) missing neighbors, all in one opposite active part. It must therefore miss all of \(B_1\). The remaining degree requirements force all of \(A_1B_2\) to be missing, and no other cross-edges to be missing.

If \(s=b\), the same conclusion holds after possibly interchanging \(B_1\) and \(B_2\): degree \(b\) and (9) force a pairing of the two active parts.

Hence, after labeling appropriately,
\[
E(M)=A_1B_2\;\cup\;A_2B_1.
\]
The two triples of parts
\[
(A_0,B_1,B_2),\qquad (B_0,A_1,A_2)
\]
form the two blown-up triangles of a triangular prism, and the edges between them are precisely the three matching pairs. Their matched part sizes are \(q,b,s\), namely \(b,b,a\).

Therefore \(G\cong S_{b,n}\).

Conversely, for even \(n\), the prism blow-up with matched sizes \(b,b,a\) is \(p\)-regular and \(K_4\)-free, has book number \(b\), and has
\[
2b^2a=b^2(n-4b)
\]
triangles. This completes the equality characterization.

## 6. What this leaves open

The original conjecture assumes only an edge count, not a minimum degree, and permits \(K_4\)'s. Neither restriction has been removed here.

The proof does give a useful necessary condition for any counterexample satisfying \(\delta(G)\ge n/2\):

- It must contain an edge lying in no triangle, by (5).
- For **every** such edge \(xy\), at least one of \(x,y\) must lie in a \(K_4\).

Indeed, the second part of the proof only needs \(G[N(x)]\) and \(G[N(y)]\) to be triangle-free, rather than global \(K_4\)-freeness.

Thus the restricted theorem is complete, but there is no argument here establishing the conjecture for arbitrary graphs at the prescribed edge density.