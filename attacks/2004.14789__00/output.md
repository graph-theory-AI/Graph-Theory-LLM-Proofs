```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general conjecture remains open, but it holds for constant expansion and for universal classes of sufficiently stretched subdivisions, while polynomial expansion always gives an explicit sublinear twin-width bound.",
  "would_publish": false,
  "caveats": "The subdivision argument does not cover selectively chosen or highly nonuniform cores, and the general quantitative bound still grows with the number of vertices."
}
```

# 1. Statement and conventions

For a graph \(G\), write

\[
\nabla_r(G)=\max\left\{\frac{|E(H)|}{|V(H)|}:H\text{ is an }r\text{-shallow minor of }G\right\}.
\]

A class \(\mathcal C\) has polynomial expansion if there are constants \(C>0\) and an integer \(k\ge 0\) such that

\[
\nabla_r(G)\le C(r+1)^k
\qquad
\text{for all }G\in\mathcal C,\ r\ge 0.
\tag{1}
\]

The conjecture asks whether (1) implies

\[
\sup_{G\in\mathcal C}\operatorname{tww}(G)<\infty.
\]

I do not resolve this. I prove three partial statements:

1. The conjecture is true when \(k=0\).
2. In general, polynomial expansion implies an explicit sublinear upper bound on twin-width.
3. The conjecture is true for a broad and natural family of potential counterexamples: universal classes of stretched subdivisions of arbitrary bounded-degree graphs.

The third result rests on a self-contained logarithmic-subdivision lemma.

---

# 2. Constant expansion

## Proposition 2.1

If \(\nabla_r(G)\le C\) for every \(G\in\mathcal C\) and every \(r\), then \(\mathcal C\) has bounded twin-width.

### Proof

Every ordinary minor \(H\) of a finite graph \(G\) is an \(r\)-shallow minor for some finite \(r\): take a minor model of \(H\) and let \(r\) be the maximum radius of its branch sets. Consequently every minor \(H\) of every \(G\in\mathcal C\) satisfies

\[
\frac{|E(H)|}{|V(H)|}\le C.
\]

Choose \(t\) with \((t-1)/2>C\). Then \(K_t\) is not a minor of any \(G\in\mathcal C\). Hence \(\mathcal C\) is contained in the proper minor-closed class of \(K_t\)-minor-free graphs. Proper minor-closed classes have bounded twin-width, as established in the source paper. ∎

Thus the first genuinely unresolved case is expansion growing with \(r\).

---

# 3. A general sublinear twin-width bound

This does not prove boundedness, but it shows that every counterexample must have twin-width growing strictly sublinearly in its order.

## Lemma 3.1

For every graph \(G\),

\[
\operatorname{tww}(G)\le \operatorname{pw}(G)+1.
\tag{2}
\]

### Proof

Let \(B_1,\ldots,B_m\) be a nice path decomposition of width \(w\). Order the vertices \(v_1,\ldots,v_n\) by their forget times. Starting with \(A_1=\{v_1\}\), successively contract \(A_{i-1}\) with \(v_i\), obtaining

\[
A_i=\{v_1,\ldots,v_i\}.
\]

At the cut immediately after \(v_i\) is forgotten, every uncontracted vertex \(x\) not present in the current path-decomposition bag was introduced later. Such an \(x\) is anticomplete to \(A_i\), because no bag contains \(x\) together with any already forgotten vertex.

It follows that every red neighbor of \(A_i\) is among the at most \(w+1\) vertices active at that cut. All other uncontracted vertices are singletons and therefore have at most the single red neighbor \(A_i\). Thus the sequence has red degree at most \(w+1\). ∎

We next use the standard shallow-clique-minor separator theorem: there is a universal constant \(a\) such that, for every \(m\)-vertex graph \(F\) and positive integers \(\ell,h\), either

- \(F\) contains \(K_h\) as an \(a\ell\log(2m)\)-shallow minor, or
- \(F\) has a \(2/3\)-balanced separator of size at most
  \[
  a\left(\frac m\ell+\ell h^2\log(2m)\right).
  \tag{3}
  \]

This is an established separator theorem, not a conjectural input.

## Proposition 3.2

Suppose \(G\) has \(n\) vertices and satisfies

\[
\nabla_r(G)\le C(r+1)^k
\qquad\text{for all }r.
\]

Then, for \(k\ge1\),

\[
\operatorname{tww}(G)
 =
 O_{C,k}\!\left(
   (n\log(2n))^{\,1-\frac1{2k+2}}
 \right).
\tag{4}
\]

### Proof

Every subgraph \(F\subseteq G\) satisfies the same expansion bound. Let \(m=|V(F)|\), let

\[
R=\left\lceil a\ell\log(2m)\right\rceil,
\]

and choose

\[
h=\left\lfloor 2C(R+1)^k\right\rfloor+2.
\]

The first outcome of the separator theorem is impossible, since an \(R\)-shallow \(K_h\)-minor would give

\[
\nabla_R(F)\ge \frac{h-1}{2}>C(R+1)^k.
\]

Therefore \(F\) has a balanced separator of size

\[
O_{C,k}\left(
 \frac m\ell+
 \ell^{2k+1}(\log(2m))^{2k+1}
\right).
\]

Put \(q=2k+2\) and choose, up to integer rounding,

\[
\ell=\frac{m^{1/q}}{(\log(2m))^{(q-1)/q}}.
\]

Both terms are then

\[
O_{C,k}\left(
 (m\log(2m))^{(q-1)/q}
\right).
\]

Thus every \(m\)-vertex subgraph has a balanced separator of size

\[
s(m)=O_{C,k}\left(
 (m\log(2m))^{\,1-\frac1{2k+2}}
\right).
\tag{5}
\]

Recursively decompose along these separators. If \(P(m)\) denotes the maximum bag size in the resulting path decomposition, concatenating the decompositions of the components and adding the separator to every bag gives

\[
P(m)\le s(m)+\max_i P(m_i),
\qquad m_i\le \frac{2m}{3}.
\]

Since the exponent in (5) is positive, summation over the recursion depth is a convergent geometric series. Hence \(P(n)=O(s(n))\). Applying Lemma 3.1 proves (4). ∎

This estimate is not claimed to be optimal. Its important feature is \(o(n)\) for every fixed polynomial expansion bound.

---

# 4. A logarithmic-subdivision lemma

A natural attempted counterexample is to start with bounded-degree graphs of unbounded twin-width and subdivide their edges sufficiently to force polynomial expansion. The following lemma shows why uniform subdivision constructions encounter a serious obstacle.

## Lemma 4.1

Let \(H\) be an \(n\)-vertex graph, \(n\ge2\). Let \(G\) be obtained by replacing every edge of \(H\) with a path containing at least

\[
2\left\lceil\log_2 n\right\rceil+1
\tag{6}
\]

new internal vertices. Then

\[
\operatorname{tww}(G)\le4.
\tag{7}
\]

No bound on the maximum degree of \(H\) is required.

### Proof

We use the bag interpretation of contractions: two bags have a black edge if they are complete to one another, no edge if they are anticomplete, and a red edge otherwise.

Set \(h=\lceil\log_2 n\rceil\). Let \(T\) be a rooted binary tree of height \(h\), and injectively assign every vertex \(v\in V(H)\) to a leaf \(\lambda(v)\) of \(T\). The maximum degree of \(T\) is three, and every path between two leaves contains at most \(2h+1\) vertices.

For an edge \(e=uv\in E(H)\), let

\[
P_e=(x_1,\ldots,x_q)
\]

be the path in \(T\) from \(\lambda(u)\) to \(\lambda(v)\). Thus \(q\le2h+1\). Partition the internal vertices of the subdivided \(uv\)-path into \(q\) nonempty consecutive intervals

\[
I_{e,x_1},\ldots,I_{e,x_q},
\]

with the first and last intervals singletons. This is possible by (6); any surplus vertices are put into an interior interval.

### Phase 1: make the interval bags

Within every \(I_{e,x}\), successively contract consecutive vertices. A growing interval bag has possible red relations only to the two neighboring portions of its subdivided path. The endpoint intervals are singletons, so no original vertex of \(H\) acquires red degree during this phase. Hence the red degree is at most two.

Let the resulting bag be denoted \(X_{e,x}\).

### Phase 2: aggregate by nodes of \(T\)

For each \(x\in V(T)\), we shall form a global bag \(B_x\) containing all \(X_{e,x}\) with \(x\in P_e\). Process the edges of \(H\) one at a time. While processing \(e\), traverse \(P_e\) in order and merge \(X_{e,x}\) into \(B_x\), creating \(B_x\) if this is its first piece.

At every intermediate stage:

- a global bag \(B_x\) can be related to global bags only at neighbors of \(x\) in \(T\);
- while processing the current route, there can additionally be one not-yet-absorbed next bag \(X_{e,y}\);
- an original vertex \(v\) is adjacent only to endpoint pieces assigned to its leaf \(\lambda(v)\).

Because \(\lambda(v)\) is a leaf, a path between two other assigned leaves never passes through \(\lambda(v)\). Furthermore, endpoint intervals are singletons. Therefore every constituent of \(B_{\lambda(v)}\) is adjacent to \(v\), and this relation remains black rather than red.

Since \(\Delta(T)\le3\), every global bag has red degree at most \(3+1=4\). The moving unabsorbed path piece has red degree at most two. Thus Phase 2 has width at most four.

### Phase 3: finish

After all edge paths have been processed, merge each nonisolated original vertex \(v\) into \(B_{\lambda(v)}\). It has no neighbors outside that bag. Isolated original vertices may be merged separately.

The support of all remaining nonzero relations among the \(B_x\)'s is a subgraph of the tree \(T\), hence a forest of maximum degree at most three. Repeatedly contract a leaf bag into its neighbor. This does not increase the red degree beyond three. Finally merge the different components, which are mutually anticomplete.

The maximum red degree over the whole sequence is at most four. ∎

The logarithmic dependence is essential to the construction: the binary tree supplies a bounded-degree routing network for all core edges.

---

# 5. Expansion of subdivided graphs

The next elementary estimate permits a fairly complete analysis of universal subdivision classes.

## Lemma 5.1

Let \(G\) be a subdivision of an \(n\)-vertex graph \(H\), where every edge of \(H\) receives at least \(L\) new internal vertices. Then

\[
\nabla_r(G)\le
\begin{cases}
2, & 4r<L,\\[2mm]
n, & 4r\ge L.
\end{cases}
\tag{8}
\]

### Proof

Call the original vertices of \(H\) the nails.

Consider a shallow-minor model in \(G\). A branch set avoiding all nails lies within the interior of a single subdivided edge, and hence is an interval of a path. It has degree at most two in the resulting minor.

Suppose \(4r<L\). Distinct nails have distance at least \(L+1\). A radius-\(r\) branch set has diameter at most \(2r\), so it contains at most one nail. Moreover, two nail-containing branch sets cannot be adjacent: if they were, their nails would have distance at most \(4r+1<L+1\). Thus the vertices corresponding to nail-containing branch sets form an independent set, while every other vertex has degree at most two. Every subgraph therefore has a vertex of degree at most two, proving density at most two.

For arbitrary \(r\), there are at most \(n\) branch sets containing nails. Every other branch set still has degree at most two. Hence every subgraph either contains a vertex of degree at most two or consists of at most \(n\) nail-containing vertices. The minor is therefore \(n\)-degenerate, and its density is at most \(n\). ∎

---

# 6. Universal subdivision families

Fix \(\Delta\ge3\), or allow \(\Delta=\infty\). Let \(f:\mathbb N\to\mathbb N_0\). Define \(\mathcal U_{f,\Delta}\) to contain every subdivision of every \(n\)-vertex graph \(H\) with \(\Delta(H)\le\Delta\), subject only to the condition that each edge receives at least \(f(n)\) new internal vertices.

## Theorem 6.1

For every fixed \(\Delta\ge3\), including \(\Delta=\infty\), the following are equivalent:

1. \(\mathcal U_{f,\Delta}\) has polynomial expansion.
2. There are \(c,\varepsilon>0\) such that
   \[
   f(n)\ge c n^\varepsilon
   \tag{9}
   \]
   for all sufficiently large \(n\).

Whenever these conditions hold, \(\mathcal U_{f,\Delta}\) has bounded twin-width. Indeed, every sufficiently large member has twin-width at most four.

### Sufficiency of (9) for polynomial expansion

Let \(G\in\mathcal U_{f,\Delta}\) have an \(n\)-vertex core. By Lemma 5.1, either \(\nabla_r(G)\le2\), or

\[
f(n)\le4r.
\]

In the second case, for sufficiently large \(n\),

\[
c n^\varepsilon\le4r,
\qquad\text{so}\qquad
n\le \left(\frac{4r}{c}\right)^{1/\varepsilon}.
\]

Again by Lemma 5.1,

\[
\nabla_r(G)\le
\max\left\{
2,N_0,\left(\frac{4r}{c}\right)^{1/\varepsilon}
\right\},
\]

where \(N_0\) absorbs the finitely many exceptional core orders. This is bounded by a polynomial in \(r\).

### Necessity of polynomial stretching

Assume

\[
\nabla_r(G)\le C(r+1)^k
\tag{10}
\]

throughout \(\mathcal U_{f,\Delta}\).

If \(k=0\), the argument below already yields a contradiction, so assume \(k\ge1\).

For each \(t\), construct a subcubic graph \(Q_t\) having \(K_t\) as an \(O(\log t)\)-shallow minor. For each \(i\in[t]\), take a binary tree \(T_i\) of height

\[
h=\lceil\log_2(t-1)\rceil
\]

with a distinguished leaf \(\ell_{ij}\) for each \(j\ne i\). Add the edge \(\ell_{ij}\ell_{ji}\) for every unordered pair \(\{i,j\}\). Then:

- \(Q_t\) has maximum degree at most three;
- \(|V(Q_t)|<4t^2\);
- contracting each \(T_i\) gives a \(K_t\) shallow-minor model of radius \(h\).

Given a sufficiently large \(n\), choose \(t=\lfloor\sqrt n/3\rfloor\) and pad \(Q_t\) with isolated vertices to obtain an \(n\)-vertex subcubic graph. Subdivide each edge exactly \(f(n)\) times; this graph belongs to \(\mathcal U_{f,\Delta}\).

The \(K_t\)-model lifts through the subdivision. Include all subdivision vertices on the internal tree edges in the corresponding branch set and divide each subdivided cross-edge between its two endpoint branch sets. The resulting branch-set radius is at most

\[
R=(f(n)+1)(h+1).
\]

Consequently,

\[
\frac{t-1}{2}
 \le \nabla_R(G)
 \le C(R+1)^k
 \le C'\bigl((f(n)+1)\log(2n)\bigr)^k.
\]

Since \(t=\Theta(\sqrt n)\),

\[
f(n)+1
  \ge
  c'\frac{n^{1/(2k)}}{\log(2n)}.
\tag{11}
\]

In particular, after decreasing the exponent,

\[
f(n)\ge c'' n^{1/(4k)}
\]

for all sufficiently large \(n\). This proves (9).

### Bounded twin-width

Condition (9) implies

\[
f(n)\ge2\lceil\log_2 n\rceil+1
\]

for all sufficiently large \(n\). Lemma 4.1 then gives twin-width at most four.

For the finitely many remaining core orders, all such subdivisions have treewidth bounded in terms of the maximum core order: subdividing an edge does not increase treewidth beyond \(\max\{2,\operatorname{tw}(H)\}\). They therefore lie in a fixed proper minor-closed class and have bounded twin-width. ∎

For \(\Delta\le2\), every member is a disjoint union of paths and cycles, so both expansion and twin-width are bounded without any assumption on \(f\).

---

# 7. Consequences for counterexample searches

Theorem 6.1 rules out the most direct subdivision construction.

Suppose one starts with all subcubic graphs on \(n\) vertices and subdivides every edge according to a common stretch profile \(f(n)\).

- If \(f(n)\) is too short to be polynomial in \(n\), the resulting universal class does not have polynomial expansion.
- If \(f(n)\) is polynomially large, it eventually exceeds the logarithmic threshold of Lemma 4.1, and the resulting class has bounded twin-width, in fact at most four apart from finitely many core orders.

Thus a counterexample cannot simply be “all bounded-degree graphs with a suitable uniform subdivision.” It would have to exploit at least one of:

1. a selectively chosen sequence of cores rather than all bounded-degree cores;
2. strongly nonuniform subdivision lengths;
3. a structure not naturally decomposable into a bounded-size core plus long routed paths.

The lower bound (11) relies crucially on the presence of the subcubic shallow-clique gadgets \(Q_t\). An arbitrary polynomial-expansion class need not contain those gadgets, so this argument does not extend to the full conjecture.

---

# 8. Remaining gap

The separator argument gives only

\[
\operatorname{tww}(G)
 =
 O\!\left(
 (|V(G)|\log |V(G)|)^{1-\delta}
 \right)
\]

for a fixed \(\delta>0\). Turning this into a constant would require much more than recursively small separators: one would need to merge the interfaces of many recursive pieces into only constantly many red neighborhoods. Polynomial expansion currently gives no evident mechanism forcing that homogeneity.

Accordingly, the full implication

\[
\text{polynomial expansion}\Longrightarrow\text{bounded twin-width}
\]

remains unproved and undisproved here.