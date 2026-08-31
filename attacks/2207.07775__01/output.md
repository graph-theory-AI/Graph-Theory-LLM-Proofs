```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but the maximum mixed order is always either r(k)-2 or r(k)-1, it is r(k)-2 for k=3,4, and endpoint failure forces strong unique-extension and saturation properties.",
  "would_publish": false,
  "caveats": "No value k≥5 is settled, and the extension equivalence substantially overlaps the source paper's Lemma 5.2."
}
```

## 1. Statement and conventions

Write \(r(k)=R(k,k)\). Let \(K_m[2]\) be the complete \(m\)-partite graph with two vertices in each part. I use “mixed blowup coloring” in the source-paper sense: a red-blue coloring with no monochromatic \(K_k\) which is not a pure blowup, meaning that at least one interpartite \(K_{2,2}\) is not monochromatic.

Define
\[
M(k)=\max\bigl\{m:K_m[2]\text{ has a mixed coloring with no monochromatic }K_k\bigr\}.
\]

The following partial results hold.

### Theorem

For every \(k\ge 3\):

1. \[
   r(k)-2\le M(k)\le r(k)-1.
   \]
   Consequently,
   \[
   M(k)\in\{r(k)-2,r(k)-1\}.
   \]

2. \(M(k)=r(k)-1\) if and only if some red-blue coloring \(H\) of \(K_{r(k)-2}\) with no monochromatic \(K_k\) has two distinct admissible one-vertex extensions to Ramsey colorings of \(K_{r(k)-1}\).

3. If
   \[
   r(k)=2R(k-1,k),
   \]
   then
   \[
   M(k)=r(k)-2.
   \]
   In particular,
   \[
   M(3)=4,\qquad M(4)=16.
   \]
   Thus the conjectured endpoint coloring does not exist for \(k=3\) or \(k=4\).

4. If \(M(k)=r(k)-2\), then every edge in every Ramsey coloring of \(K_{r(k)-1}\) is the unique minority-colored edge of some \(K_k\). In particular, every such coloring contains at least
   \[
   \binom{r(k)-1}{2}
   \]
   almost-monochromatic copies of \(K_k\).

These results reduce the open conjecture to deciding which of the two possible values \(M(k)\) takes infinitely often.

---

## 2. The one-vertex extension equivalence

Let \(m\ge 2\).

### Lemma 2.1

There is a mixed \(K_k\)-free coloring of \(K_m[2]\) if and only if there are two red-blue colorings \(G_0,G_1\) of \(K_m\), both without monochromatic \(K_k\), such that for some vertex \(v\),

\[
G_0-v=G_1-v
\]

as labeled colorings, but \(G_0\ne G_1\).

#### Proof

Suppose first that \(K_m[2]\) has a mixed coloring. Some block between two parts is not monochromatic. In its \(2\times2\) color matrix, either two rows differ or two columns differ. Hence there is a part
\[
P_v=\{v_0,v_1\},
\]
another part \(P_j\), and a vertex \(y\in P_j\) such that
\[
c(v_0y)\ne c(v_1y).
\]

Choose \(y\) as representative of \(P_j\), and choose one arbitrary representative from every other part apart from \(P_v\). The two transversals obtained by choosing \(v_0\) and \(v_1\), respectively, induce two colorings \(G_0,G_1\) of \(K_m\). They agree away from \(v\), differ at the edge \(vy\), and neither contains a monochromatic \(K_k\).

Conversely, suppose \(G_0,G_1\) agree on \(H=G_0-v=G_1-v\). Make one part
\[
P_v=\{v_0,v_1\}
\]
and, for every \(x\in V(H)\), a part \(P_x=\{x_0,x_1\}\). Color every block \(P_x,P_y\) uniformly according to \(H(xy)\), and set
\[
c(v_i x_j)=G_i(vx),\qquad i,j\in\{0,1\}.
\]
Every clique uses at most one vertex from each part. If it uses \(v_i\), its coloring is inherited from \(G_i\); if it avoids \(P_v\), it is inherited from \(H\). Thus there is no monochromatic \(K_k\). Since \(G_0\ne G_1\), at least one block incident with \(P_v\) is mixed. ∎

This also gives an exact extension formulation. If \(H\) is a \(K_k\)-free two-coloring and \(S\subseteq V(H)\), add a vertex \(v\) with red neighborhood \(S\) and blue neighborhood \(V(H)\setminus S\). The extension is Ramsey precisely when

\[
H[S]\text{ has no red }K_{k-1},
\]
and
\[
H[V(H)\setminus S]\text{ has no blue }K_{k-1}.
\]

Call such an \(S\) admissible. Therefore the conjecture for a fixed \(k\) is equivalent to the existence of a coloring \(H\) of \(K_{r(k)-2}\) having at least two admissible subsets.

---

## 3. A universal result one part below the conjectured endpoint

### Proposition 3.1

For every \(k\ge3\),
\[
M(k)\ge r(k)-2.
\]

#### Proof

Let
\[
n=r(k)-1,
\]
and let \(G\) be a Ramsey coloring of \(K_n\).

The coloring \(G\) is not monochromatic. Indeed, the standard two-block construction gives \(r(k)\ge 2k-1\), so \(n\ge k\), while a monochromatic \(K_n\) contains a monochromatic \(K_k\).

Every nonconstant edge-coloring of a complete graph has a vertex incident with both colors. Otherwise every vertex would have a monochromatic incident star; consistency on each edge would force all these star colors, and hence all edges, to have one common color.

Thus there are vertices \(x,u,v\) such that
\[
c(xu)\ne c(xv).
\]
Put
\[
W=V(G)\setminus\{u,v\};
\]
then \(|W|=n-2\). On the common vertex set \(W\cup\{z\}\), define two colorings:
- in the first, \(z\) has the adjacency pattern of \(u\);
- in the second, \(z\) has the adjacency pattern of \(v\).

These are respectively the induced colorings \(G-v\) and \(G-u\), after relabeling \(u\) or \(v\) as \(z\). They agree on \(W\), differ at \(zx\), and both avoid monochromatic \(K_k\). By Lemma 2.1 they give a mixed coloring of
\[
K_{n-1}[2]=K_{r(k)-2}[2].
\]
∎

For the upper bound, if \(K_m[2]\) has any coloring without a monochromatic \(K_k\), choosing one vertex from each part produces a coloring of \(K_m\) without a monochromatic \(K_k\). Hence \(m\le r(k)-1\).

This proves
\[
M(k)\in\{r(k)-2,r(k)-1\}.
\]

Thus the conjecture concerns the only unresolved part: whether the final extra part can be attained infinitely often.

---

## 4. A numerical obstruction via off-diagonal Ramsey numbers

Let
\[
q=R(k-1,k),\qquad n=r(k)-1.
\]

In a Ramsey coloring \(G\) of \(K_n\), the red neighborhood of any vertex \(v\) contains neither a red \(K_{k-1}\) nor a blue \(K_k\). Therefore
\[
d_R(v)\le q-1.
\]
By exchanging colors,
\[
d_B(v)\le q-1.
\]
Consequently,
\[
n-q\le d_R(v)\le q-1.
\]
The width of this degree interval is
\[
(q-1)-(n-q)=2q-r(k).
\]

### Proposition 4.1

If
\[
r(k)=2R(k-1,k),
\]
then there is no mixed coloring of \(K_{r(k)-1}[2]\).

#### Proof

Under equality \(r(k)=2q\), every vertex in every Ramsey coloring of \(K_{r(k)-1}\) satisfies
\[
d_R(v)=d_B(v)=q-1.
\]

Suppose there were two such colorings \(G_0,G_1\) agreeing outside a vertex \(v\) but differing at some edge \(uv\). All edges at \(u\), apart from \(uv\), agree in the two colorings. Hence
\[
\left|d_R^{G_0}(u)-d_R^{G_1}(u)\right|=1,
\]
contrary to both degrees being \(q-1\). Lemma 2.1 now rules out a mixed endpoint coloring. ∎

The contrapositive gives the necessary numerical condition
\[
M(k)=r(k)-1\quad\Longrightarrow\quad r(k)<2R(k-1,k).
\]
Strictness of the Ramsey recurrence is not sufficient by this argument.

### The cases \(k=3,4\)

For \(k=3\),
\[
r(3)=6,\qquad R(2,3)=3,
\]
so equality holds and
\[
M(3)=r(3)-2=4.
\]

For \(k=4\),
\[
r(4)=18,\qquad R(3,4)=9,
\]
so
\[
M(4)=r(4)-2=16.
\]

For completeness, \(R(3,4)=9\) has a short proof. The Wagner graph on \(\mathbb Z/8\mathbb Z\), with edges \(i(i\pm1)\) and \(i(i+4)\), is triangle-free and has independence number \(3\), proving \(R(3,4)>8\). Conversely, suppose a graph \(F\) on nine vertices is triangle-free with \(\alpha(F)\le3\). Every neighborhood is independent, so every degree is at most \(3\). If some vertex has degree at most \(2\), its at least six nonneighbors contain, by \(R(3,3)=6\), either a triangle or an independent triple. The former is impossible, while the latter together with the original vertex is an independent \(4\)-set. Hence every degree is \(3\), contradicting the handshake lemma on nine vertices.

This proves nonexistence at \(k=3,4\) without using uniqueness classifications of the critical Ramsey colorings.

---

## 5. Necessary saturation if the endpoint fails

Let \(G\) be a Ramsey coloring of \(K_{r(k)-1}\). Consider an edge \(xy\), say red. Recoloring \(xy\) blue cannot create a red \(K_k\). It creates a blue \(K_k\) precisely when there is a set \(W\) of \(k-2\) other vertices such that every edge on
\[
\{x,y\}\cup W
\]
apart from \(xy\) was already blue.

Therefore:

### Proposition 5.1

If there is an edge of a critical Ramsey coloring which is not the unique minority-colored edge in any \(K_k\), then the conjectured mixed coloring exists for that \(k\).

Equivalently, if no mixed endpoint coloring exists, then:

- every red edge is the unique red edge of some otherwise blue \(K_k\);
- every blue edge is the unique blue edge of some otherwise red \(K_k\).

Since an almost-monochromatic \(K_k\) has a unique minority edge, distinct edges require distinct witnesses. Thus every critical coloring has at least
\[
\binom{r(k)-1}{2}
\]
almost-monochromatic \(K_k\)'s.

This condition is only necessary, not sufficient: simultaneous changes of several edges incident with one vertex may remain possible even when every individual edge change is blocked.

A stronger form follows from uniqueness of admissible extensions. Let \(G-v=H\) and let \(S=N_R^G(v)\). If \(S\) is the unique admissible set, then:

- for each \(x\in S\), there is a blue \(K_{k-1}\), say \(C_x\), with
  \[
  C_x\cap S=\{x\};
  \]
- for each \(y\notin S\), there is a red \(K_{k-1}\), say \(D_y\), with
  \[
  D_y\cap(V(H)\setminus S)=\{y\}.
  \]

Indeed, removing \(x\) from \(S\) can only violate the blue condition, and adding \(y\) can only violate the red condition. These are explicit local certificates that every incident edge of \(v\) is frozen.

---

## 6. Automorphism criteria that would produce a mixed coloring

Let \(H\) be a Ramsey coloring of \(K_{r(k)-2}\), and let \(S\) be admissible.

- If \(\alpha\) is a color-preserving automorphism of \(H\), then \(\alpha(S)\) is admissible.
- If \(\alpha\) reverses the two colors, then
  \[
  \alpha(V(H)\setminus S)
  \]
  is admissible.

Consequently, either of the following suffices for a mixed endpoint coloring:

\[
\alpha(S)\ne S
\]
for some color-preserving automorphism, or
\[
\alpha(V(H)\setminus S)\ne S
\]
for some color-reversing automorphism.

In particular:

### Corollary 6.1

Suppose \(G\) is a critical Ramsey coloring and \(v\in V(G)\) is such that \(G-v\) is self-complementary as a colored graph. If
\[
d_R^G(v)\ne d_B^G(v),
\]
then a mixed coloring of \(K_{r(k)-1}[2]\) exists.

Indeed, a color-reversing automorphism sends the blue-neighbor set to a second admissible red-neighbor set, and the two sets have different cardinalities.

This is a checkable route requiring only one critical Ramsey coloring, rather than an a priori search for two of them.

---

## 7. Fully specified SAT formulation

For a fixed \(k\) and candidate endpoint \(n\), put \(N=n-1\). Introduce:

- \(e_{ij}\), \(1\le i<j\le N\), with \(e_{ij}=1\) meaning red;
- \(s_i,t_i\), encoding two proposed admissible sets \(S,T\).

For every \(k\)-set \(Q\subseteq[N]\), include
\[
\bigvee_{\{i,j\}\subseteq Q}\neg e_{ij},
\qquad
\bigvee_{\{i,j\}\subseteq Q}e_{ij},
\]
forbidding monochromatic \(K_k\)'s in \(H\).

For every \((k-1)\)-set \(A\subseteq[N]\), include
\[
\left(\bigvee_{i\in A}\neg s_i\right)
 \vee
\left(\bigvee_{\{i,j\}\subseteq A}\neg e_{ij}\right),
\]
and
\[
\left(\bigvee_{i\in A}s_i\right)
 \vee
\left(\bigvee_{\{i,j\}\subseteq A}e_{ij}\right),
\]
and the analogous two clauses with \(s\) replaced by \(t\).

Finally impose \(S\ne T\), for example using Tseitin variables \(d_i\leftrightarrow(s_i\oplus t_i)\) and the clause
\[
\bigvee_{i=1}^N d_i.
\]

A satisfying assignment is exactly a pair of distinct admissible extensions and therefore exactly a mixed coloring of \(K_n[2]\). An LRAT-certified unsatisfiability result would prove nonexistence for that particular \(k,n\). To settle the original instance one must additionally know that \(n=r(k)-1\).

No such computation is claimed here.

---

## 8. Remaining gap

The conjecture requires proving
\[
M(k)=r(k)-1
\]
for infinitely many \(k\). The arguments above establish only the sharp one-part dichotomy
\[
M(k)\in\{r(k)-2,r(k)-1\}
\]
and rule out the upper value when the standard Ramsey recurrence is tight.

For \(k\ge5\), neither strictness of
\[
r(k)\le2R(k-1,k)
\]
nor the existence of many nonisomorphic Ramsey colorings by itself guarantees two admissible extensions of the same \((r(k)-2)\)-vertex coloring. The saturation and automorphism criteria provide concrete avenues for a construction or computation, but they do not establish a new positive instance. Thus the infinite-\(k\) conjecture remains unresolved.