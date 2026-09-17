```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicitly defined substitution-closed infinite class has exactly four exceptions, of orders 4, 10, 16 and 22, but the unrestricted finiteness conjecture is not settled.",
  "would_publish": false,
  "caveats": "Only a generated subclass is classified; the proper-neighborhood definition is used, and literature novelty is unchecked."
}
```

## 1. Definition and the partial result

A **2-homogeneous coloring** means a proper vertex coloring \(\varphi\), with no prescribed bound on its number of colors, such that
\[
|\varphi(N(v))|=2
\]
at every vertex. All graphs below are finite and simple.

I recheck the prism gadget from the previous attempt and obtain two additional conclusions:

* its insertion on an edge can **repair the coloring condition at both endpoints**, without changing any old vertex color;
* the entire class obtained by arbitrarily iterating this insertion on \(K_4\) has exactly four exceptions—not an infinite counterfamily.

The classification also extends to insertions starting from any triangle-covered cubic graph.

### The insertion operation

Let \(R\) be the triangular prism with one triangle edge deleted:
\[
V(R)=\{a,b,c,A,B,C\},
\]
\[
E(R)=\{ac,bc,AB,BC,CA,aA,bB,cC\}.
\]
Its two degree-two vertices, or **terminals**, are \(a,b\).

To **inflate** an edge \(uv\) of a cubic graph, delete \(uv\), take a fresh copy of \(R\), and add
\[
ua,\qquad bv.
\]
An inflation adds six vertices. Subsequent inflations may be performed on any edge, including an edge introduced by an earlier inflation.

Define \(H_i\), for \(0\leq i\leq3\), by starting with \(K_4\) and inflating \(i\) edges of a fixed triangle, each exactly once. Thus
\[
|V(H_i)|=4+6i.
\]

### Partial classification theorem

Let \(\mathcal C\) consist of all graphs obtained by a finite sequence of these inflations from a connected bridgeless cubic graph in which every vertex belongs to a triangle. Then the members of \(\mathcal C\) without a 2-homogeneous coloring are precisely
\[
H_0,\ H_1,\ H_2,\ H_3,
\]
of orders \(4,10,16,22\), respectively.

In particular, this proves a finite-exception statement, with bound \(22\), for an infinite substitution-closed class. It does **not** show that all exceptions to the original conjecture belong to this class.

Inflation preserves simplicity, connectedness and cubicity. It also preserves bridgelessness. Indeed, every internal edge of \(R\) lies on one of
\[
A-B-C-A,\qquad
a-c-b-B-A-a,\qquad
a-c-C-A-a.
\]
The joining edges lie on a cycle obtained from an alternative \(u\)-\(v\) path in the original bridgeless graph and the path
\[
u-a-c-b-v.
\]
Cycles containing other old edges can likewise be retained, replacing \(uv\) by this path when necessary.

---

## 2. Exact boundary behavior of the prism gadget

Attach external neighbors \(x,y\) to \(a,b\), respectively. Prescribe the four boundary colors
\[
\varphi(a)=\alpha,\quad \varphi(b)=\beta,\quad
\varphi(x)=\xi,\quad \varphi(y)=\eta.
\]
We impose properness and the 2-homogeneous condition at all six vertices of \(R\), but impose no neighborhood condition at \(x,y\).

### Lemma 2.1

The prescribed boundary colors extend over \(R\) if and only if
\[
\alpha\ne\beta,\qquad
\xi\ne\eta,\qquad
\alpha\ne\xi,\qquad
\beta\ne\eta. \tag{1}
\]

Thus the gadget forces inequality both between its terminal colors and between its external-neighbor colors.

#### Proof: necessity

The last two inequalities are properness of the joining edges.

The bottom triangle has three distinct colors, which we may name
\[
\varphi(A)=1,\qquad \varphi(B)=2,\qquad \varphi(C)=3.
\]
The neighborhood conditions at \(A,B,C\) give
\[
\varphi(a)\in\{2,3\},\quad
\varphi(b)\in\{1,3\},\quad
\varphi(c)\in\{1,2\}.
\]

At \(c\), the choice \((\varphi(a),\varphi(b))=(2,1)\) gives a rainbow neighborhood, while \((3,3)\) gives a monochromatic neighborhood. Properness of \(ac,bc\) therefore leaves exactly these cases:
\[
\begin{array}{c|ccc|c|c}
&\varphi(a)&\varphi(b)&\varphi(c)&\varphi(x)&\varphi(y)\\ \hline
\mathrm{I}&3&1&2&\in\{1,2\}&\notin\{1,2\}\\
\mathrm{II}&2&3&1&\notin\{1,2\}&\in\{1,2\}.
\end{array}
\]
The restrictions in the last two columns follow from the conditions at \(a,b\), together with properness of their external edges. In either case,
\[
\varphi(a)\ne\varphi(b),\qquad
\varphi(x)\ne\varphi(y).
\]

#### Proof: sufficiency

Suppose (1) holds. Choose a color \(\gamma\) such that
\[
\gamma\notin\{\alpha,\beta,\eta\},
\qquad
\xi\in\{\beta,\gamma\}.
\]
This is possible: if \(\xi\ne\beta\), take \(\gamma=\xi\); otherwise take a fresh color.

Set
\[
\varphi(c)=\gamma,\quad
\varphi(A)=\beta,\quad
\varphi(B)=\gamma,\quad
\varphi(C)=\alpha.
\]
This is proper. The neighborhood color multisets are
\[
\begin{array}{c|c}
a&\{\gamma,\beta,\xi\}\\
b&\{\gamma,\gamma,\eta\}\\
c&\{\alpha,\beta,\alpha\}\\
A&\{\gamma,\alpha,\alpha\}\\
B&\{\beta,\alpha,\beta\}\\
C&\{\beta,\gamma,\gamma\}.
\end{array}
\]
Each uses exactly two colors. ∎

This proves, rather than merely assumes, the inequality property used in the previous attempt. The extension direction will be important below.

---

## 3. Inflation repairs both endpoints

### Lemma 3.1 — Local repair

Let \(\varphi\) be any proper coloring of a cubic graph \(G\), and let \(uv\in E(G)\). After inflating \(uv\), there is a proper coloring extending all old vertex colors such that:

1. every vertex of the inserted copy of \(R\) satisfies the 2-homogeneous condition;
2. both \(u\) and \(v\) satisfy that condition;
3. the neighborhood color pattern at every other old vertex is unchanged.

#### Proof

At \(u\), inspect the colors of its two neighbors other than \(v\).

* If those colors are distinct, the new terminal color at \(a\) may be either of them.
* If those colors are equal, give \(a\) a fresh color.

Either choice makes the new neighborhood of \(u\) use exactly two colors and is proper on \(ua\). Make the analogous choice at \(v\).

The terminal colors can be chosen distinct. If both choices come from two-element sets, select unequal representatives. If either choice uses a fresh color, choose it to differ from the other terminal color.

The external colors are \(\varphi(u)\ne\varphi(v)\), since \(\varphi\) is proper on the old edge \(uv\). Thus all four conditions of Lemma 2.1 hold, and the coloring extends over \(R\).

No old vertex color changes. Only \(u,v\) have their neighborhoods changed, proving the last assertion. ∎

Two consequences are useful.

### Corollary 3.2 — Preservation

Inflating an edge of a 2-homogeneously colorable cubic graph produces another 2-homogeneously colorable graph.

Consequently, once a graph in an inflation sequence is colorable, every later graph in that sequence is colorable.

### Proposition 3.3 — Exact reduction for simultaneous first-level insertions

Let \(S\subseteq E(G)\), and let \(G_S\) be obtained by inflating every edge of \(S\) exactly once. Put
\[
T=V(G)\setminus V(S),
\]
where \(V(S)\) is the set of endpoints of the edges in \(S\).

Then \(G_S\) has a 2-homogeneous coloring if and only if \(G\) has a proper coloring satisfying the 2-homogeneous condition at every vertex of \(T\).

#### Proof

For the forward direction, restrict a coloring of \(G_S\) to the original vertices. Every original edge not in \(S\) still forces unequal endpoint colors. Every edge in \(S\) also has unequal endpoint colors by Lemma 2.1. Thus the restricted coloring is proper on \(G\).

The neighborhoods of vertices in \(T\) were not changed, so those vertices satisfy the required condition.

Conversely, start with the specified proper coloring of \(G\). Inflate the edges of \(S\) one at a time, applying Lemma 3.1. Each insertion repairs its endpoints and creates no new failure elsewhere. Every original vertex outside \(T\) is eventually repaired, and every vertex of \(T\) was already satisfactory. ∎

In particular:

> **Inflating an edge cover of any cubic graph always produces a 2-homogeneously colorable graph.**

No colorability hypothesis on the original cubic graph is needed.

---

## 4. First-level insertions on \(K_4\)

Suppose only original edges of \(K_4\) are inflated, each at most once, and let \(S\) be the set of inflated edges.

In any 2-homogeneous coloring of the resulting graph, the four original vertices must have pairwise distinct colors: ordinary original edges force this by properness, and inflated original edges force it by Lemma 2.1.

If some original vertex is not incident with \(S\), its neighborhood consists of the other three original vertices. That neighborhood is rainbow. Hence the graph is not colorable.

Conversely, if \(S\) covers all four original vertices, Proposition 3.3 gives a coloring.

We have therefore proved
\[
(K_4)_S\text{ is 2-homogeneously colorable}
\quad\Longleftrightarrow\quad
S\text{ is an edge cover of }K_4. \tag{2}
\]

Up to automorphism of \(K_4\), the edge sets that do not cover all vertices are:

* the empty set;
* one edge;
* two incident edges;
* the three edges of a triangle.

These give exactly \(H_0,H_1,H_2,H_3\). The graph \(H_1\) is the ten-vertex exception constructed in the previous attempt: the uninflated part of \(K_4\) is a diamond.

What remains to prove is that **inflating newly introduced edges cannot generate further exceptions**.

---

## 5. A second-level insertion destroys the obstruction

We need a slightly weaker boundary requirement than that of the original \(R\).

Say that a two-terminal gadget has property \((*)\) if it extends every assignment of boundary colors satisfying
\[
\varphi(a)\ne\varphi(b),\qquad
\varphi(a)\ne\varphi(x),\qquad
\varphi(b)\ne\varphi(y), \tag{*}
\]
with no requirement that \(\varphi(x)\ne\varphi(y)\). As before, extension includes properness and the neighborhood condition at every gadget vertex.

### Lemma 5.1 — Two copies in series

Two copies of \(R\) joined in series have property \((*)\). In fact, the condition that the two outer terminal colors differ is unnecessary.

#### Proof

Write the terminal pairs as \(a_1,b_1\) and \(a_2,b_2\), and join \(b_1a_2\). The outer terminals are \(a_1,b_2\).

After prescribing the outer terminal and external colors, give \(b_1,a_2\) two distinct fresh colors. Each copy of \(R\) then satisfies all four boundary inequalities in Lemma 2.1. Extend the two copies separately. ∎

### Lemma 5.2 — Inflating an internal edge

Let \(R'\) be obtained by inflating any internal edge of \(R\). Then \(R'\) has property \((*)\).

#### Proof

If the external colors are distinct, Lemma 2.1 first colors \(R\), and Lemma 3.1 extends the coloring through the internal inflation.

It remains to consider equal external colors. Under \((*)\), the two terminal colors and the common external color are distinct, so rename them as
\[
\varphi(a)=1,\qquad \varphi(b)=2,\qquad
\varphi(x)=\varphi(y)=3.
\]

The following table gives proper colorings of the uninflated \(R\). In each row, the only vertex failing the neighborhood condition is an endpoint of the edge to be inflated:
\[
\begin{array}{c|rrrr|c}
\text{edge to inflate}
&\varphi(c)&\varphi(A)&\varphi(B)&\varphi(C)
&\text{only failing vertex}\\ \hline
ac&3&3&1&2&a\\
aA&4&4&3&2&A\\
cC&3&2&4&1&C\\
AB&4&3&4&2&A\\
AC&3&4&1&2&C
\end{array}
\]
Here \(4\) is a fresh color.

These entries are checked directly from the eight edges of \(R\). For example, in the row for \(aA\), the neighborhood multisets are
\[
\begin{array}{c|c}
a&\{4,4,3\}\\
b&\{4,3,3\}\\
c&\{1,2,2\}\\
A&\{3,2,1\}\\
B&\{4,2,2\}\\
C&\{4,3,4\}.
\end{array}
\]
Only \(A\) fails.

The automorphism
\[
a\leftrightarrow b,\qquad A\leftrightarrow B
\]
covers the remaining edges \(bc,bB,BC\), with the corresponding renaming of terminal colors. Thus all eight internal edges are covered.

Apply Lemma 3.1 to the indicated edge. It repairs both endpoints, preserves all four prescribed boundary colors, and leaves every other satisfactory neighborhood unchanged. This proves \((*)\). ∎

### Lemma 5.3 — A flexible replacement colors \(K_4\)

If one edge of \(K_4\) is replaced by any gadget satisfying \((*)\), the resulting graph has a 2-homogeneous coloring.

#### Proof

Let the replaced edge be \(uv\), and let the other original vertices be \(w,z\). Give the original vertices colors
\[
\varphi(u)=\varphi(v)=1,\qquad
\varphi(w)=2,\qquad
\varphi(z)=3.
\]
Give the gadget terminal adjacent to \(u\) color \(2\), and the terminal adjacent to \(v\) color \(3\).

These boundary colors satisfy \((*)\), so extend through the gadget. The four original neighborhood color multisets are
\[
\begin{array}{c|c}
u&\{2,3,2\}\\
v&\{2,3,3\}\\
w&\{1,1,3\}\\
z&\{1,1,2\}.
\end{array}
\]
All conditions hold. ∎

---

## 6. Completion of the classification

First consider an arbitrary inflation sequence starting from \(K_4\).

If the sequence inflates only original edges, Section 4 gives exactly the four exceptions \(H_0,H_1,H_2,H_3\).

Otherwise, consider the **first** inflation of an edge that was not an original edge of \(K_4\). Immediately before this step, all existing inserted gadgets are pristine copies of \(R\). The selected edge is therefore either:

1. an internal edge of one such copy; or
2. a joining edge between such a copy and an original vertex.

In the first case, the affected original edge is now represented by a gadget satisfying \((*)\), by Lemma 5.2. In the second case, it is represented by two copies of \(R\) in series, which satisfy \((*)\) by Lemma 5.1.

By Lemma 5.3, \(K_4\) with this affected edge replacement is colorable. All the insertions on other original edges can be performed afterwards, and preserve colorability by Corollary 3.2. Thus the graph at this first second-level step is colorable. Every subsequent inflation preserves colorability as well.

This proves that the entire inflation closure of \(K_4\) has precisely the four exceptions claimed.

Now let the starting graph \(B\) be connected and cubic, with every vertex belonging to a triangle, and suppose \(B\ne K_4\). Brooks’ theorem gives a proper 3-coloring of \(B\). For a vertex \(v\), two of its neighbors lie with it in a triangle and therefore have different colors. Those are the two colors different from \(\varphi(v)\); the third neighbor must have one of them. Hence the coloring is 2-homogeneous.

Every inflation of \(B\) remains colorable by Corollary 3.2. Combining this with the classification for the starting graph \(K_4\) proves the stated theorem for \(\mathcal C\). ∎

---

## 7. What this establishes—and the remaining gap

The rigorously established partial results are:

1. **An exact boundary relation** for the deleted-edge triangular prism.
2. **A local repair operation:** its insertion repairs both edge endpoints while preserving every old vertex color.
3. **An exact reduction** for arbitrary sets of first-level insertions, including the edge-cover sufficient condition.
4. **Four explicit connected bridgeless cubic exceptions**, of orders \(4,10,16,22\).
5. **A complete classification in an infinite substitution-closed class:** no further exceptions arise by arbitrarily iterating this operation from triangle-covered cubic graphs.

The unrestricted conjecture is not resolved. There is no argument here that an arbitrary noncolorable connected bridgeless cubic graph reduces to a triangle-covered graph under inverse insertions. In particular, the proof gives no general structural control over triangle-free cubic graphs or over other possible obstruction gadgets.

The examples of orders \(16\) and \(22\), and the partial classification, are not asserted to be new to the literature. No computational enumeration or externally verified literature resolution is being claimed.