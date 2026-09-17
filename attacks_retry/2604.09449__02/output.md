```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A palette argument gives sharp large-host single-star bounds for infinitely many k, while projective-plane colourings force an Omega(sqrt(k) Delta) recolouring obstruction.",
  "would_publish": false,
  "caveats": "The extract omits the definition of f_h; no upper-bound improvement for arbitrary spanning forests, or claim of literature novelty, is made."
}
```

# Partial results: sharp small-star bounds and a growing recolouring obstruction

I obtain two rigorous partial results:

1. **An exact extremal theorem for a single star with isolated vertices**, when the host is sufficiently large, for infinitely many values of \(k\).
2. **A lower bound of order \(\sqrt{k}\) on the leading coefficient in the recolouring-distance normalization**, already for star forests. The same obstruction extends to spanning trees, with an additive \(O_k(1)\) loss.

The second result is substantially different from a one-star obstruction with a coefficient bounded independently of \(k\). Neither result proves an improved upper bound for arbitrary spanning forests.

## 1. Normalizations

The supplied extract does not define \(f_h(F)\), so I state the results for explicit colour-count errors rather than identify \(f_h\) with an unverified normalization.

Let \(h:E(K_N)\to[k]\) be balanced:
\[
|h^{-1}(i)|=\frac1k\binom N2
\qquad(i\in[k]).
\]
For a spanning graph \(F\), put \(m=e(F)\). If \(\phi\) is a bijective embedding, write \(a_i(\phi)\) for its number of colour-\(i\) edges. Define
\[
D_h(F)=\min_\phi\max_{i\in[k]}
\left|a_i(\phi)-\frac mk\right|
\]
and
\[
R_h(F)=\min_\phi\frac12\sum_{i=1}^k
\left|a_i(\phi)-\frac mk\right|.
\]
Since the deviations sum to zero,
\[
\frac12\sum_i\left|a_i-\frac mk\right|
=\sum_i\left(a_i-\frac mk\right)_+
=\sum_i\left(\frac mk-a_i\right)_+.
\]
When \(k\mid m\), \(R_h(F)\) is exactly the minimum number of edges that must be recoloured to make the embedded copy colour-balanced.

The constructions and proofs below do not use the previous attempt’s degree-cap lemma or its near-spanning-star extremal theorem.

---

# 2. A general upper bound for one star in a large host

Write
\[
S_{N,\Delta}=K_{1,\Delta}\cup (N-\Delta-1)K_1.
\]

The elementary observation behind the upper bound is that a balanced colouring cannot have too few substantial colour-degrees at every vertex.

### Lemma 1: substantial palettes

Let
\[
r=\lceil\sqrt{k}\rceil,\qquad T\ge1.
\]
If a balanced \(k\)-colouring of \(K_N\) satisfies
\[
N>
\frac{k+2k^2(T-1)}{k-(r-1)^2},                                      \tag{1}
\]
then some vertex has degree at least \(T\) in at least \(r\) colours.

#### Proof

For each colour \(i\), let
\[
X_i=\{v:d_i(v)\ge T\}.
\]
Suppose that no vertex belongs to \(r\) of these sets. Then
\[
\sum_{i=1}^k |X_i|\le (r-1)N,
\]
so some colour \(i\) has
\[
s:=|X_i|\le \frac{(r-1)N}{k}.
\]

Every colour-\(i\) edge either lies inside \(X_i\) or has an endpoint outside \(X_i\). Consequently,
\[
\begin{aligned}
\frac{N(N-1)}{2k}
&\le \binom{s}{2}+\sum_{v\notin X_i}d_i(v)\\
&\le \frac{s^2}{2}+N(T-1)\\
&\le \frac{(r-1)^2N^2}{2k^2}+N(T-1).
\end{aligned}
\]
Rearranging gives
\[
\bigl(k-(r-1)^2\bigr)N\le k+2k^2(T-1),
\]
contrary to (1). The denominator in (1) is positive because \(r-1<\sqrt{k}\). ∎

### Proposition 2: single-star upper bound

Let \(k\ge3\), \(1\le\Delta\le N-1\), and put
\[
r=\lceil\sqrt{k}\rceil,\qquad T=\left\lceil\frac{\Delta}{r}\right\rceil.
\]
If (1) holds, then every balanced \(k\)-colouring satisfies
\[
\boxed{
D_h(S_{N,\Delta})
\le
\max\left\{
\frac{\Delta}{k},
\left\lceil\frac{\Delta}{r}\right\rceil-\frac{\Delta}{k}
\right\}.}                                                        \tag{2}
\]
If also \(k\mid\Delta\), then
\[
\boxed{
R_h(S_{N,\Delta})\le \frac{k-r}{k}\Delta.}                           \tag{3}
\]

#### Proof

By Lemma 1, there is a vertex \(v\) having at least \(T\) neighbours in each of \(r\) distinct colours. Choose \(\Delta\) incident edges, distributed as equally as possible among these \(r\) colours. Thus the selected colour counts are
\[
\left\lfloor\frac{\Delta}{r}\right\rfloor
\quad\text{or}\quad
\left\lceil\frac{\Delta}{r}\right\rceil,
\]
and all other counts are zero. These edges form the required star; unused vertices are isolated.

Every downward deviation is at most \(\Delta/k\), and every upward deviation is at most \(T-\Delta/k\). This proves (2).

If \(k\mid\Delta\), write \(b=\Delta/k\). Since \(r\le k\),
\[
\left\lfloor\frac{\Delta}{r}\right\rfloor\ge b.
\]
Hence the only deficient colours are the \(k-r\) unused ones, each with deficit \(b\). This proves (3). ∎

This is an upper bound for every \(k\). The next construction shows that it is exactly sharp for infinitely many \(k\), including its leading coefficient.

---

# 3. Projective-plane colourings make the star bound sharp

Fix a prime power \(q\ge2\), and put
\[
k=q^2+q+1,\qquad r=q+1.
\]
In particular, \(r=\lceil\sqrt{k}\rceil\).

Use the projective plane over \(\mathbb F_q\). Its points and lines can be defined as the one- and two-dimensional subspaces of \(\mathbb F_q^3\). The properties needed here are:

- there are \(k\) points and \(k\) lines;
- every line contains \(r\) points;
- every point lies on \(r\) lines;
- two distinct lines meet in exactly one point.

### Proposition 3: a regular small-palette colouring

For every
\[
n=1+2ra,\qquad a\ge1,
\]
there is a balanced \(k\)-colouring of \(K_N\), where \(N=kn\), such that every vertex is incident with exactly \(r\) colours and has degree
\[
d=\frac{N-1}{r}                                                     \tag{4}
\]
in each of those colours.

#### Construction and verification

Identify the colours with the projective-plane points. Partition the host vertices into classes
\[
V_L,\qquad |V_L|=n,
\]
indexed by the projective-plane lines.

For distinct lines \(L,L'\), colour every edge between \(V_L\) and \(V_{L'}\) with the point \(L\cap L'\).

Inside \(V_L\), use the \(r\) colours belonging to \(L\), each with degree
\[
\frac{n-1}{r}=2a
\]
at every vertex. Here is an explicit construction of this internal colouring. Label the vertices by \(\mathbb Z_n\). The undirected cyclic difference classes
\[
\{\pm1\},\ldots,\{\pm(n-1)/2\}
\]
partition \(E(K_n)\), each giving a \(2\)-regular graph. Partition these \(ra\) difference classes into \(r\) groups of \(a\) classes and assign them to the points of \(L\).

Now take \(v\in V_L\). If the point \(P\) belongs to \(L\), there are \(q\) other lines through \(P\). Therefore
\[
d_P(v)=qn+\frac{n-1}{r}
=\frac{kn-1}{r}
=\frac{N-1}{r}.
\]
If \(P\notin L\), then \(d_P(v)=0\).

For a fixed colour \(P\), exactly \(rn\) vertices have positive degree in that colour. Hence
\[
2|h^{-1}(P)|
=rn\frac{N-1}{r}
=n(N-1),
\]
or
\[
|h^{-1}(P)|=\frac{N(N-1)}{2k}.
\]
Thus the colouring is balanced. ∎

### Proposition 4: exact star error in this colouring

For the colouring in Proposition 3 and every \(1\le\Delta\le N-1\),
\[
D_h(S_{N,\Delta})
=
\max\left\{
\frac{\Delta}{k},
\left\lceil\frac{\Delta}{r}\right\rceil-\frac{\Delta}{k}
\right\}.                                                         \tag{5}
\]
If \(k\mid\Delta\), then
\[
R_h(S_{N,\Delta})=\frac{k-r}{k}\Delta.                              \tag{6}
\]

#### Proof

Every possible centre is incident with only \(r\) colours. Thus every embedded star misses at least \(k-r\) colours, and some used colour has at least \(\lceil\Delta/r\rceil\) edges. These give the two lower bounds in (5), and the missing colours give the lower bound in (6).

Conversely, every available colour at a centre has degree \(d=(N-1)/r\). Since
\[
\left\lceil\frac{\Delta}{r}\right\rceil\le d,
\]
we can distribute the \(\Delta\) selected edges as equally as possible among all \(r\) available colours. This attains both bounds, using the same calculation as in Proposition 2. ∎

## An exact extremal theorem

Combining the universal upper bound with this construction yields the following finite statement.

### Theorem 5

Let \(q\ge2\) be a prime power, and let
\[
k=q^2+q+1.
\]
Suppose
\[
n\equiv1\pmod{2(q+1)},\qquad n\ge2\Delta+1,\qquad N=kn.
\]
Then
\[
\boxed{
\max_{h\ {\rm balanced}}D_h(S_{N,\Delta})
=
\left\lceil\frac{\Delta}{q+1}\right\rceil-\frac{\Delta}{k}.}          \tag{7}
\]
If \(k\mid\Delta\), then
\[
\boxed{
\max_{h\ {\rm balanced}}R_h(S_{N,\Delta})
=
\frac{q^2}{k}\Delta.}                                              \tag{8}
\]

#### Verification of the host-size condition

Here
\[
k-(r-1)^2=r.
\]
Writing \(T=\lceil\Delta/r\rceil\), the right side of (1) is
\[
\frac{k+2k^2(T-1)}r
<
\frac kr+\frac{2k^2\Delta}{r^2}
<
k+2k\Delta
\le N.
\]
Thus Proposition 2 applies. Also \(k\ge2r\) for \(q\ge2\), so the second term in the maximum in (5) is the larger one. ∎

For example, when \(k=7\), the exact worst-case errors in this range are
\[
D_h(S_{N,\Delta})
=\left\lceil\frac{\Delta}{3}\right\rceil-\frac{\Delta}{7},
\qquad
R_h(S_{N,\Delta})=\frac47\Delta
\quad(7\mid\Delta).
\]

For fixed \(k=q^2+q+1\), along the specified host orders and with
\(\Delta\to\infty\), \(\Delta=o(N)\), the sharp leading coefficients for this family are therefore
\[
\frac{q^2}{(q+1)(q^2+q+1)}
\quad\text{for }D_h,
\qquad
\frac{q^2}{q^2+q+1}
\quad\text{for }R_h.
\]

Thus the single-star problem in a genuinely large host has a different extremal mechanism from the nearly spanning star considered in the previous attempt.

---

# 4. A recolouring coefficient growing with \(k\)

The same colouring gives a stronger obstruction when the forest has several large stars.

The key fact is that the union of any \(t\) projective-plane lines has at most
\[
r+(t-1)(r-1)=1+tq                                                   \tag{9}
\]
points: every additional line meets the first line, so it contributes at most \(q\) new points.

### Theorem 6: star-forest lower bound

Fix a prime power \(q\ge2\), put \(k=q^2+q+1\), and let \(1\le t\le q\). There are arbitrarily large \(\Delta\), balanced colourings \(h\) of complete graphs \(K_{kn}\), and spanning forests \(F\) of maximum degree \(\Delta\), such that
\[
\boxed{
R_h(F)\ge
\frac{q\,t(q+1-t)}{k}\Delta.}                                      \tag{10}
\]

These examples can be chosen to have exactly \(k\) components, only \(k-t\) of which are isolated vertices.

#### Proof

For an arbitrary positive integer \(b\), set
\[
\Delta=2k(q+1)b,\qquad N=t\Delta+k.
\]
Then
\[
\frac Nk=1+2(q+1)tb,
\]
so Proposition 3 supplies the required balanced colouring.

Take
\[
F=tK_{1,\Delta}\cup(k-t)K_1.
\]
This is a spanning forest on \(N\) vertices, with maximum degree \(\Delta\) and
\[
e(F)=t\Delta,
\qquad k\mid e(F).
\]

Consider any embedded copy. The \(t\) star centres have palettes corresponding to at most \(t\) projective-plane lines. Every edge of \(F\) is incident with one of these centres. By (9), all its edges therefore use at most \(1+tq\) colours.

Consequently at least
\[
z=k-1-tq=q(q+1-t)
\]
colours are absent. Each absent colour has deficit \(t\Delta/k\). Hence
\[
R_h(F)\ge z\frac{t\Delta}{k}
=\frac{q\,t(q+1-t)}{k}\Delta.
\]
This holds for every embedding. ∎

### Consequence for a universal leading coefficient

Suppose a universal estimate of the form
\[
R_h(F)\le C_k\Delta(F)+O_k(1)                                      \tag{11}
\]
holds for all the spanning forests under consideration. Optimizing (10) over integer \(t\) gives
\[
\boxed{
C_{q^2+q+1}\ge
\frac{q}{q^2+q+1}
\left\lfloor\frac{(q+1)^2}{4}\right\rfloor.}                        \tag{12}
\]
In particular,
\[
C_k\ge \left(\frac14+o(1)\right)\sqrt{k}
\]
along \(k=q^2+q+1\).

For instance, \(q=4\), \(k=21\), and \(t=2\) give
\[
C_{21}\ge\frac87.
\]
Thus a \(k\)-independent leading coefficient is impossible for the recolouring-distance normalization.

If the intended forest regime requires \(\Delta=o(N)\), the same obstruction still works **with isolated vertices allowed**: keep the same \(t\) stars and place them, together with additional isolates, in a much larger host from Proposition 3. The palette argument is unchanged.

---

# 5. The obstruction also extends to spanning trees

The few isolated vertices in Theorem 6 are not essential for obtaining the lower coefficient in unrestricted host orders.

Start with its forest
\[
F=tK_{1,\Delta}\cup(k-t)K_1.
\]
Choose an anchor in each of its \(k\) components: a leaf in every large star, and the vertex itself in an isolated component. Join the anchors in a path.

The resulting graph \(T\) is a spanning tree. Its maximum degree is still \(\Delta\), because a star-leaf anchor acquires at most two additional edges, and \(\Delta\ge3\). Exactly \(k-1\) edges have been added.

In any embedding, the original star edges still use at most \(1+tq\) colours. For the other
\[
z=q(q+1-t)
\]
colours, the total number of edges is at most \(k-1\). Since
\[
e(T)=t\Delta+k-1,
\]
we obtain
\[
\begin{aligned}
R_h(T)
&\ge z\frac{t\Delta+k-1}{k}-(k-1)\\
&\ge \frac{q\,t(q+1-t)}{k}\Delta-(k-1).                             \tag{13}
\end{aligned}
\]
Thus (12) also holds for half-\(\ell_1\) discrepancy restricted to spanning trees.

There is a divisibility issue if this is phrased as *exact* recolouring to equal counts: a tree in \(K_{kn}\) has \(kn-1\) edges. For balancing the counts as evenly as possible, however, the same leading coefficient follows. The target vector has one coordinate \(n-1\) and \(k-1\) coordinates \(n\), whose half-\(\ell_1\) distance from the constant vector with coordinate \(n-1/k\) is
\[
\frac{k-1}{k}<1.
\]
Thus changing from the centred norm to this integer recolouring target changes the error by less than one.

The tree examples here have \(\Delta\) comparable to \(N\) for fixed \(k\); they do not establish the analogous obstruction for connected trees with \(\Delta=o(N)\).

---

# 6. What remains open

The results above leave the main optimization problem unresolved.

- **For \(\ell_\infty\) discrepancy:** Theorem 5 gives a sharp upper bound only for a single star with isolates in a sufficiently large host. It does not improve a universal coefficient for arbitrary spanning forests.
- **For recolouring distance:** Theorem 6 gives a leading-coefficient obstruction of order \(\sqrt{k}\). This is a lower bound, not a matching upper bound.
- The \(\sqrt{k}\) conclusion is **specific to the recolouring/half-\(\ell_1\) normalization**. It must not be interpreted as an \(\ell_\infty\) lower bound of that order.
- The palette upper bound cannot simply be summed over components: doing so controls error in terms of the number of edges rather than only \(\Delta(F)\).
- Without the omitted definition of \(f_h\) and the source’s precise numerical theorem, I cannot claim a direct improvement to its stated coefficient or verified novelty.

The rigorous progress is therefore an exact large-host star theorem and a stronger, growing-in-\(k\) obstruction for recolouring-error bounds, rather than a solution for arbitrary spanning forests.