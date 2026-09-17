```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound is attained by every balanced cyclic three-part blow-up, and it also holds for several explicit perturbations of these examples.",
  "would_publish": false,
  "caveats": "No proof or counterexample for arbitrary tournaments; the novelty of these special-case results has not been checked."
}
```

## 1. Results obtained

Let \(\nu(T)\) denote the maximum number of arc-disjoint transitive triples in a tournament \(T\), and put
\[
g(n)=\left\lceil\frac{n(n-3)}6\right\rceil.
\]
Writing \(n=3m+r\), where \(r\in\{0,1,2\}\), gives the useful identity
\[
g(3m+r)=3\binom m2+rm. \tag{1}
\]

I prove the following special cases.

**Theorem 1.** Suppose that \(V(T)=A\sqcup B\sqcup C\), the three sizes differ by at most one, and the arcs between each pair of parts are oriented uniformly. Then
\[
\nu(T)\ge g(|T|).
\]
If the interpart orientations are cyclic,
\[
A\longrightarrow B,\qquad B\longrightarrow C,\qquad C\longrightarrow A,
\]
then equality holds, regardless of the tournaments inside the parts.

The construction also gives two robustness statements.

**Theorem 2.** Let \(T_0\) be a cyclic three-part blow-up with three parts of size \(m\).

1. Adding one vertex with completely arbitrary incident orientations produces a tournament satisfying the conjectured bound.
2. If \(m\) is odd, the same holds after adding two arbitrary vertices.
3. If \(m\) is odd, the bound still holds after reversing any set of cross-arcs that forms a matching between each pair of parts. Thus as many as \(3m\) suitably distributed cross-arcs may be reversed.

Finally, the natural arc-cover analogue has a simple exact characterization: its minimum possible value is \(g(n)\), and precisely the balanced cyclic blow-ups attain that minimum. Theorem 1 consequently settles the packing conjecture whenever this arc-cover bound is tight.

These are special-case results, not an improvement of the universal asymptotic lower bound.

---

## 2. An edge-colouring lemma

All the packing constructions will first be described on underlying unordered edges.

**Lemma.** The edges of \(K_m\) admit a proper colouring with \(m\) colours having the following properties.

- If \(m\) is odd, each colour is absent at exactly one vertex, and these missing vertices are all different.
- If \(m=2k\), the vertices can be partitioned into pairs
  \[
  \{v_i^0,v_i^1\},\qquad 1\le i\le k,
  \]
  such that \(k\) colours are perfect matchings, while each of the other \(k\) colours is absent precisely at one prescribed pair.

In the even case, the pairing and the correspondence between pairs and deficient colours can be prescribed by relabelling.

**Proof.**

For odd \(m\ge3\), label the vertices and colours by \(\mathbb Z_m\), and give \(\{x,y\}\) colour
\[
\frac{x+y}{2}\pmod m.
\]
Colour \(c\) matches every vertex except \(c\). The case \(m=1\) is immediate.

For \(m=2k\ge4\), use the standard one-factorization of \(K_{2k}\) on
\[
\{\infty\}\cup\mathbb Z_{2k-1}.
\]
Colour \(\{\infty,x\}\) by \(x\), and colour \(\{x,y\}\) by \((x+y)/2\), with arithmetic modulo \(2k-1\).

The edges
\[
\{0,1\},\{2,3\},\ldots,\{2k-4,2k-3\}
\]
form a matching and have distinct colours: their colours are \((4j+1)/2\), for \(0\le j\le k-2\). Recolour these \(k-1\) edges with one additional colour.

Each of their old colours now misses its two endpoints. The additional colour misses the two unmatched vertices. Thus there are \(k\) deficient colours, whose missing pairs partition the vertices, and \(k\) unchanged perfect-matching colours.

For \(m=2\), use one colour on the single edge and one empty colour. Relabelling completes the proof. \(\square\)

---

## 3. Packing the balanced three-part examples

### 3.1 Equal part sizes

Initially let
\[
|A|=|B|=|C|=m.
\]

Properly colour the edges of \(K_A\) using the vertices of \(B\) as colours. For every edge \(aa'\) coloured \(b\), take the triangle
\[
\{a,a',b\}.
\]
Do the same cyclically:

- colour \(K_A\) by \(B\);
- colour \(K_B\) by \(C\);
- colour \(K_C\) by \(A\).

Every resulting triangle is transitive: its third vertex either dominates both endpoints of its internal edge or is dominated by both.

Properness of the colouring ensures that a cross-edge is used at most once. Moreover, the three families use different pairs of parts for their cross-edges. Consequently this is an arc-disjoint packing of size
\[
3\binom m2, \tag{2}
\]
covering every internal edge exactly once.

We will need control of the unused edges, or *leave*.

#### Odd \(m\)

Label the parts
\[
A=\{a_i\},\qquad B=\{b_i\},\qquad C=\{c_i\}.
\]
Choose the colourings so that \(b_i\) misses \(a_i\), \(c_i\) misses \(b_i\), and \(a_i\) misses \(c_i\). The leave is exactly
\[
\bigcup_{i=1}^m
\{a_ib_i,\ b_ic_i,\ c_ia_i\}. \tag{3}
\]
Thus the leave consists of \(m\) vertex-disjoint triangles. Under cyclic interpart orientations, these are directed cycles.

#### Even \(m=2k\)

Label each part in pairs:
\[
A=\{a_i^0,a_i^1:1\le i\le k\},
\]
and similarly for \(B,C\).

Use the lemma so that colour \(b_i^0\) misses precisely \(a_i^0,a_i^1\), while all colours \(b_i^1\) are perfect matchings. Make the corresponding choices cyclically.

The leave is a disjoint union of six-vertex graphs \(L_i\), with
\[
\begin{aligned}
E(L_i)=\{&
a_i^0b_i^0,\ a_i^1b_i^0,\\
&b_i^0c_i^0,\ b_i^1c_i^0,\\
&c_i^0a_i^0,\ c_i^1a_i^0
\}.
\end{aligned} \tag{4}
\]
Each \(L_i\) is a triangle on \(a_i^0,b_i^0,c_i^0\), with one pendant edge at each vertex.

### 3.2 Adding the balancing vertices

For \(n=3m+r\), label the parts so that the extra vertex, when \(r\ge1\), is \(x\in A\), and the second extra vertex, when \(r=2\), is \(y\in B\). Start with the equal-size construction on the remaining vertices.

If \(m\) is odd, add
\[
\{x,a_i,b_i\}\qquad(1\le i\le m),
\]
and, when \(r=2\), also add
\[
\{y,b_i,c_i\}\qquad(1\le i\le m).
\]
Their old edges are distinct edges of the leave (3).

If \(m=2k\), add, for each \(i\),
\[
\{x,a_i^1,b_i^0\},\qquad
\{x,a_i^0,c_i^1\}, \tag{5}
\]
and, when \(r=2\), also add
\[
\{y,b_i^1,c_i^0\},\qquad
\{y,b_i^0,a_i^0\}. \tag{6}
\]

Every displayed triangle has two vertices in one part and one in another, so is transitive. Their old edges are distinct edges of (4). For each new vertex, the old endpoints used are all distinct, so its incident arcs are not repeated. The edge \(xy\), if present, is unused.

The resulting packing has
\[
3\binom m2+rm=g(n)
\]
members by (1). The cases \(n=1,2\) require only the empty packing.

This proves the lower bound in Theorem 1.

### 3.3 Sharpness for cyclic interpart orientations

Now assume the three interpart directions are cyclic. A triple meeting all three parts is a directed cycle. Therefore every transitive triple contains an internal edge.

Any arc-disjoint transitive-triple packing consequently has size at most
\[
\binom{|A|}{2}+\binom{|B|}{2}+\binom{|C|}{2}
=3\binom m2+rm
=g(n).
\]
The construction attains this upper bound. This proves Theorem 1 in full. \(\square\)

---

## 4. Arbitrary exceptional vertices

Here the interpart orientations of the equal-size core are assumed cyclic.

For a new vertex \(x\), call an old arc \(u\to v\) *good for \(x\)* if \(\{x,u,v\}\) is transitive. It is bad precisely when
\[
x\to u\to v\to x. \tag{7}
\]

### 4.1 Odd part size: two arbitrary vertices

Use the packing whose leave is the directed-triangle factor (3).

For any new vertex \(x\), at least two edges of each directed triangle are good for \(x\). Indeed, among the edges of a directed triangle, at most one goes from \(N^+(x)\) to \(N^-(x)\).

Thus, for one new vertex, choose one good edge from each leave triangle and extend it through \(x\). This adds \(m\) transitive triples.

For two new vertices \(x,y\), each has at least two good edges in every leave triangle. Hence we can choose an edge good for \(x\) and a **different** edge good for \(y\). Extend these through \(x\) and \(y\), respectively.

These triples are arc-disjoint:

- their old edges are distinct;
- for each new vertex, the chosen edges lie in vertex-disjoint leave triangles;
- an arc incident with \(x\) cannot equal one incident with \(y\), since \(xy\) is never used.

The resulting sizes are
\[
3\binom m2+m=g(3m+1)
\quad\text{and}\quad
3\binom m2+2m=g(3m+2).
\]

### 4.2 Even part size: one arbitrary vertex

Let \(m=2k\), and let \(x\) be the new vertex. Pair the vertices in each part arbitrarily. In each pair, choose the superscript-\(0\) vertex to belong to \(N^+(x)\) whenever that is possible.

Construct the core packing with leave (4). Its three pendant arcs in component \(i\) are
\[
a_i^1\to b_i^0,\qquad
b_i^1\to c_i^0,\qquad
c_i^1\to a_i^0. \tag{8}
\]

A pendant arc can be bad only if its source pair lies entirely in \(N^+(x)\) and its target pair lies entirely in \(N^-(x)\):

- a superscript-\(1\) vertex lies in \(N^+(x)\) only when both vertices of its pair do;
- a superscript-\(0\) vertex lies in \(N^-(x)\) only when both vertices of its pair do.

Around the directed cycle of three pairs, at most one transition can go from an entirely-out pair to an entirely-in pair. Therefore at least two of the pendant arcs (8) are good for \(x\).

The three pendant edges form a matching. Choose two good ones in each component and extend them through \(x\). This adds \(2k=m\) arc-disjoint transitive triples, attaining \(g(3m+1)\).

This proves the first two assertions of Theorem 2. \(\square\)

---

## 5. Matching-distributed cross-arc errors

Suppose \(m\) is odd, and let \(F\) be a set of cross-arcs of the equal-size cyclic blow-up such that
\[
F[A,B],\qquad F[B,C],\qquad F[C,A]
\]
are matchings, viewed as undirected edge sets.

Extend each of these three matchings to a perfect matching between its two parts. The odd case of the colouring lemma allows the equal-size packing to have **any prescribed perfect matching** as its leave between each pair of parts: simply assign each colour to its desired missing vertex. The three choices are independent.

We can therefore construct a packing of size
\[
3\binom m2=g(3m)
\]
whose leave contains every arc of \(F\). Reversing the arcs in \(F\) does not change any triangle in the packing.

This proves the final assertion of Theorem 2. \(\square\)

---

## 6. The exact arc-cover analogue

Define
\[
\tau(T)=\min\{|F|:T-F\text{ contains no transitive triple}\}.
\]

**Proposition.** Every \(n\)-vertex tournament satisfies
\[
\tau(T)\ge g(n).
\]
For \(n\ge3\), equality holds if and only if \(T\) is a balanced cyclic three-part blow-up. In particular,
\[
\tau(T)=g(n)\quad\Longrightarrow\quad \nu(T)=g(n).
\]

**Proof.** Let \(F\) meet every transitive triple and put \(D=T-F\).

The underlying graph of \(D\) is \(K_4\)-free: every tournament on four vertices contains a transitive triple, since some vertex has at least two out-neighbours.

The classical \(K_4\)-free form of Turán’s theorem gives
\[
|E(D)|\le \left\lfloor\frac{n^2}{3}\right\rfloor.
\]
Consequently
\[
|F|\ge \binom n2-\left\lfloor\frac{n^2}{3}\right\rfloor
=\left\lceil\frac{n(n-3)}6\right\rceil.
\]

If equality holds, the equality case of Turán’s theorem says that the underlying graph of \(D\) is complete balanced tripartite.

Every triangle with one vertex in each part must be cyclic. This forces uniform cyclic interpart orientations. To see this, fix one cyclic triple \(a_0\to b_0\to c_0\to a_0\). The triangles using two of these fixed vertices determine the orientations from every other vertex to them; then a triangle using one fixed vertex determines the orientation between any two vertices in the other two parts.

Conversely, deleting all internal arcs of a balanced cyclic blow-up destroys every transitive triple and uses exactly \(g(n)\) arcs. The packing equality then follows from Theorem 1. \(\square\)

---

## 7. What remains unresolved

The construction settles all parity cases for the extremal family and provides the explicit robustness results above. It does **not** supply a packing of size \(g(n)\) in a general tournament.

In particular, the cover inequality is not a proof of the conjecture: the general relation is
\[
\nu(T)\le \tau(T),
\]
not the reverse. Nor is there a justification for assuming that an arbitrary tournament admits the homogeneous partition or controlled leave used in the constructions.

Thus no complete proof, counterexample, or improved universal asymptotic bound is established here. I also make no claim that these special-case constructions are new relative to the cited literature.