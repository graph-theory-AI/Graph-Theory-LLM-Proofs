```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured lower bound holds for colorings admitting a sufficiently monochromatic balanced cut, including every one-vertex extension of the canonical Ramsey-critical coloring.",
  "would_publish": false,
  "caveats": "The argument does not force an arbitrary low-multiplicity coloring to admit such a cut, so the full conjecture remains open."
}
```

# Mathematical writeup

## 1. Setup

Let \(k=2\ell+1\ge 5\) and \(n=2k-1=4\ell+1\). For a red-blue coloring \(\chi\) of \(K_n\), write
\[
M_\chi(C_k)=N_R(C_k)+N_B(C_k)
\]
for the number of unoriented monochromatic copies of \(C_k\).

Set
\[
H=\frac{(k-1)!}{2}=\frac{(2\ell)!}{2},
\qquad
D=(k-2)!=(2\ell-1)!.
\]
Thus \(H\) is the number of Hamilton cycles in \(K_k\), and \(D\) is the number of Hamilton cycles of \(K_k\) containing a prescribed edge.

The conjecture asserts \(M_\chi(C_k)\ge H\) for every coloring of \(K_{2k-1}\), for all sufficiently large odd \(k\).

The following proves this whenever there is a reasonably red balanced cut. Internal edges on both sides of the cut are completely unrestricted.

---

## 2. A balanced-cut stability theorem

### Theorem

Let \(V(K_{4\ell+1})=A\sqcup B\), where
\[
|A|=2\ell+1=k,\qquad |B|=2\ell=k-1.
\]
Let
\[
S=E_B(A,B)
\]
be the set of blue edges across the cut, and put \(s=|S|\) and \(d=\Delta(S)\), with degrees taken in the bipartite graph \(S\).

If either

\[
s\le 2\ell-1=k-2, \tag{I}
\]
or
\[
d\le \left\lfloor\frac{\ell}{2}\right\rfloor
   =\left\lfloor\frac{k-1}{4}\right\rfloor, \tag{II}
\]
then
\[
M_\chi(C_k)\ge \frac{(k-1)!}{2}.
\]

Under either hypothesis, equality is possible only when all edges inside \(A\) and \(B\) are blue and \(s\le 1\). Conversely, those colorings have exactly \(H\) monochromatic \(C_k\)'s.

The same statement of course holds after interchanging red and blue.

---

## 3. Proof of the balanced-cut theorem

Write \(F=E_R(A)\), and let \(r=|F|\).

### 3.1. Blue cycles inside \(A\)

There are \(H\) Hamilton cycles in the complete graph on \(A\). Each edge of \(F\) belongs to exactly \(D\) such cycles. Hence, by the union bound, the number of blue Hamilton cycles in \(A\) is at least
\[
H-rD. \tag{1}
\]

We next show that every red edge of \(F\) creates at least \(D\) red \(C_k\)'s using only cut edges besides that edge.

### 3.2. Alternating cycles associated with a red edge of \(A\)

Fix \(f=uv\in F\), with its endpoints put in a fixed order. Consider sequences
\[
u,b_1,a_1,b_2,a_2,\ldots,a_{\ell-1},b_\ell,v,
\]
where the \(b_i\) are distinct elements of \(B\), and the \(a_i\) are distinct elements of \(A\setminus\{u,v\}\).

Together with the edge \(uv\), such a sequence gives a \(C_k\) with exactly one cycle-edge internal to \(A\). The total number of these potential cycles is
\[
Q=(2\ell)_\ell(2\ell-1)_{\ell-1}
  =\binom{2\ell}{\ell}D, \tag{2}
\]
where \((x)_j=x(x-1)\cdots(x-j+1)\).

A potential cycle is red precisely when all of its cut edges avoid \(S\).

#### Under hypothesis (I)

A blue cut edge incident with \(u\) or \(v\) lies in exactly \(Q/(2\ell)\) members of this family.

If \(e=ab\in S\) with \(a\notin\{u,v\}\), then \(e\) can occur on either side of one of the \(\ell-1\) internal \(A\)-vertices. Thus it lies in
\[
2(\ell-1)(2\ell-1)_{\ell-1}(2\ell-2)_{\ell-2}
\]
potential cycles. Dividing by \(Q\), this proportion is
\[
\frac{\ell-1}{\ell(2\ell-1)}
\le \frac1{2\ell}.
\]
Consequently, at least
\[
Q\left(1-\frac{s}{2\ell}\right)
\]
members survive. Under \(s\le 2\ell-1\), this is at least
\[
\frac{Q}{2\ell}
 =D\frac{\binom{2\ell}{\ell}}{2\ell}
 >D, \tag{3}
\]
because \(\binom{2\ell}{\ell}>2\ell\) for \(\ell\ge2\).

#### Under hypothesis (II)

Suppose \(\Delta(S)\le d\le\lfloor\ell/2\rfloor\). Choose \(b_1\) red-adjacent to \(u\), then \(b_\ell\ne b_1\) red-adjacent to \(v\), and choose the remaining \(b_i\)'s arbitrarily. This gives at least
\[
(2\ell-d)(2\ell-d-1)(2\ell-2)_{\ell-2}
\]
ordered choices for the \(B\)-vertices.

For each \(i\), the vertices \(b_i,b_{i+1}\) have at least \(2\ell+1-2d\) common red neighbors in \(A\). Choosing the \(a_i\)'s successively while avoiding \(u,v\) and previous choices gives at least
\[
(2\ell-2d-1)_{\ell-1}
\]
choices. Hence the number \(L_d\) of red cycles associated with \(f\) is at least
\[
L_d=(2\ell-d)(2\ell-d-1)(2\ell-2)_{\ell-2}
           (2\ell-2d-1)_{\ell-1}. \tag{4}
\]

If \(d<\ell/2\), then
\[
\frac{L_d}{D}
=
\frac{(2\ell-d)(2\ell-d-1)}
     {(2\ell-1)(\ell-2d)}
\binom{2\ell-2d-1}{\ell}>1. \tag{5}
\]
Indeed, the first fraction is greater than \(1\), since
\[
(2\ell-d)(2\ell-d-1)-(2\ell-1)(\ell-2d)
=2\ell^2-\ell+d^2-d>0.
\]

If \(d=\ell/2\), necessarily \(\ell\) is even, and
\[
\frac{L_d}{D}
=
\frac{(3\ell/2)(3\ell/2-1)}{\ell(2\ell-1)}.
\]
This is greater than \(1\) for \(\ell\ge4\).

The remaining boundary case is \((\ell,d)=(2,1)\). Here \(S\) is a matching, \(Q=36\), and \(D=6\). A blue cut edge incident with \(u\) or \(v\) blocks nine potential cycles, while one incident with an internal \(A\)-vertex blocks six. If at most one endpoint of \(f\) is incident with \(S\), at most \(27\) cycles are blocked. If both are incident with \(S\), their two blocking families intersect in three cycles, again leaving at least \(9>D\) red cycles.

Thus in every case covered by (II), each \(f\in F\) produces strictly more than \(D\) red cycles.

### 3.3. Summation

Cycles arising from different \(f\in F\) are distinct because each has a unique cycle-edge internal to \(A\). Combining their count with (1),
\[
M_\chi(C_k)
\ge H-rD+rL,
\]
where \(L>D\) under either hypothesis. Therefore
\[
M_\chi(C_k)\ge H,
\]
with strict inequality whenever \(r>0\).

This proves the lower bound.

---

## 4. Equality under the balanced-cut hypotheses

Suppose \(M_\chi(C_k)=H\). The strictness above implies that \(F=\varnothing\), so \(A\) is a blue \(K_k\) and already contributes exactly \(H\) blue cycles.

We show that \(B\) must also be blue.

### Under hypothesis (I)

If \(xy\) is a red edge inside \(B\), consider alternating \(x\)-\(y\) paths
\[
x,a_1,b_1,a_2,\ldots,b_{\ell-1},a_\ell,y.
\]
There are
\[
Q_B=(2\ell+1)_\ell(2\ell-2)_{\ell-1}
\]
potential paths. Every blue cut edge belongs to at most \(Q_B/(2\ell+1)\) of them. Since \(s\le2\ell-1\), at least one path avoids \(S\), producing an additional red \(C_k\), a contradiction.

### Under hypothesis (II)

Let \(xy\) be red inside \(B\). Starting at \(x\), greedily choose
\[
x,a_1,b_1,a_2,\ldots,b_{\ell-1}
\]
with red cut edges and all vertices distinct. At step \(i\), there are at least
\[
2\ell-d-i-1\ge \ell-d>0
\]
choices for \(b_i\). Finally, \(b_{\ell-1}\) and \(y\) have at least \(2\ell+1-2d\) common red neighbors in \(A\); after excluding the \(\ell-1\) used \(A\)-vertices, at least
\[
\ell+2-2d\ge2
\]
remain. Thus there is again an additional red \(C_k\), a contradiction.

Hence \(B\) is also a blue clique.

If \(S\) contains two distinct edges, they create an additional blue \(C_k\):

- if they share an endpoint in \(A\), join their endpoints in \(B\) by a blue path of length \(2\ell-1\);
- if they share an endpoint in \(B\), use a blue path of length \(2\ell-1\) in \(A\);
- if they are disjoint, use the blue edge between their \(A\)-endpoints and a blue path of length \(2\ell-2\) between their \(B\)-endpoints.

Thus equality forces \(|S|\le1\).

Conversely, if \(A\) and \(B\) are blue cliques and there is at most one blue cut edge, the blue cut edge is a bridge and belongs to no cycle. The red graph is bipartite. Therefore the only monochromatic \(C_k\)'s are the \(H\) Hamilton cycles in \(A\).

This completes the proof.

---

## 5. Two useful corollaries

### Corollary 1: one color bipartite

If either color graph is bipartite, then \(M_\chi(C_k)\ge H\).

Indeed, suppose the red graph has bipartition \(P\sqcup Q\), with \(|P|+|Q|=2k-1\). Every edge inside \(P\) and \(Q\) is blue, so the number of blue \(C_k\)'s is at least
\[
\left(\binom{|P|}{k}+\binom{|Q|}{k}\right)H.
\]
One of \(P,Q\) has size at least \(k\), so this is at least \(H\).

In particular, a counterexample would have to have both color graphs non-bipartite.

### Corollary 2: extending the canonical critical coloring by one vertex

Let \(X,Y\) have size \(k-1=2\ell\), let \(z\) be one further vertex, color \(X\) and \(Y\) internally blue and all \(X\)-\(Y\) edges red, and color the edges incident with \(z\) arbitrarily.

Let
\[
p=|N_B(z)\cap X|,\qquad q=|N_B(z)\cap Y|.
\]
Then the exact number of monochromatic \(C_k\)'s is
\[
\boxed{
M_\chi(C_k)
=
\left(\binom p2+\binom q2\right)(k-3)!
+
(2\ell-p)(2\ell-q)
\left(\frac{(2\ell-1)!}{\ell!}\right)^2.
} \tag{6}
\]

The first term counts blue cycles through \(z\) and all of \(X\), or through \(z\) and all of \(Y\). The second counts red cycles through \(z\); after orienting such a cycle to leave \(z\) first into \(X\), its remaining vertices alternate between \(X\) and \(Y\).

Formula (6) is always at least \(H\). If \(p=2\ell\) or \(q=2\ell\), the corresponding blue term already equals \(H\). If \(p,q\le2\ell-1\), then for \(\ell\ge3\) the red term alone is at least
\[
\left(\frac{(2\ell-1)!}{\ell!}\right)^2>H.
\]
For \(\ell=2\), this is checked directly: if both red attachment degrees are positive, either their product is at least \(2\), giving at least \(18>12\) red cycles, or \(p=q=3\), in which case the blue term is already \(12\).

Equality in (6) occurs precisely when
\[
(p,q)=(2\ell,0),(2\ell,1),(0,2\ell),(1,2\ell).
\]
Thus every one-vertex extension of the exact canonical \(C_k\)-free coloring of \(K_{2k-2}\) satisfies the conjectured bound.

---

## 6. Consequences for a hypothetical counterexample

Any counterexample must satisfy all of the following:

1. Neither color contains a \(K_k\), since such a clique already supplies \(H\) monochromatic Hamilton cycles.
2. Neither color is bipartite.
3. For every partition \(A\sqcup B\) with \((|A|,|B|)=(k,k-1)\), and for either choice of intended cut color, the opposite-color cut graph \(S\) must satisfy
   \[
   |S|\ge k-1
   \quad\text{and}\quad
   \Delta(S)\ge
   \left\lfloor\frac{k-1}{4}\right\rfloor+1.
   \]
4. It cannot be a one-vertex extension of the canonical critical coloring described above.

The balanced-cut theorem allows arbitrary errors inside both parts and, under the maximum-degree condition, permits \(\Theta(k^2)\) cut errors. Thus it is more than a constant-edit local check.

## 7. Remaining gap

The missing global step is a stability theorem forcing a coloring with fewer than \(H\) monochromatic \(C_k\)'s to admit a balanced cut satisfying one of the two hypotheses above. No such statement is proved here. A coloring that is far from every two-cluster configuration is not covered, even though one expects such a coloring to have substantially more monochromatic cycles.

Accordingly, this is a rigorous structural partial result, not a proof of Conjecture 4. I also make no claim that this exact balanced-cut lemma has not appeared elsewhere.