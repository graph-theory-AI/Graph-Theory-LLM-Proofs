```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted limit is not established, but fixed-star-anchor versions have limits, equal to 1/4 and 1/3 for star budgets 0 and 1, and approaching 1/2 as the budget grows.",
  "would_publish": false,
  "caveats": "The argument does not control star budgets growing arbitrarily with dimension; novelty relative to the full cited preprints has not been checked."
}
```

# 1. Results obtained

I use the code formulation supplied in the question. For \(x,y\in\{0,1,*\}^d\), write
\[
\delta(x,y)=\bigl|\{i:\{x_i,y_i\}=\{0,1\}\}\bigr|.
\]
A code \(\mathcal C\) is **2-neighborly** if
\[
1\le \delta(x,y)\le 2\qquad(x\ne y\in\mathcal C).
\]
Its largest possible size is \(n(2,d)\).

For a fixed nonnegative integer \(s\), define
\[
a_s(d)=\max\left\{|\mathcal C|:
\begin{array}{l}
\mathcal C\text{ is a 2-neighborly code of length }d,\\
\mathcal C\text{ contains a word with at most }s\text{ stars}
\end{array}\right\}.
\]

The following are proved below.

### Theorem
1. For every fixed \(s\), the limit
   \[
   \lambda_s=\lim_{d\to\infty}\frac{a_s(d)}{d^2}
   \]
   exists.
2. The first two constants are
   \[
   \lambda_0=\frac14,\qquad \lambda_1=\frac13.
   \]
3. The sequence \((\lambda_s)\) is nondecreasing, and
   \[
   \lambda_s<\frac12\quad\text{for every fixed }s,
   \qquad
   \lim_{s\to\infty}\lambda_s=\frac12.
   \]
4. Suppose a 2-neighborly code contains a word with \(s\) stars, and put \(m=d-s\). Then
   \[
   |\mathcal C|
   \le
   1+m+\binom m2+A_s(m+1)+B_s, \tag{1}
   \]
   where
   \[
   A_0=0,\qquad A_s=s7^{s-1}\quad(s\ge1),
   \]
   and
   \[
   B_0=B_1=0,\qquad B_s=2\binom s2 7^{s-2}\quad(s\ge2).
   \]
   Consequently, if a sequence of codes has such words with
   \[
   s=s(d),\qquad s7^s=o(d),
   \]
   then
   \[
   |\mathcal C|\le \left(\frac12+o(1)\right)d^2.
   \]

Thus the full-support special case is substantially smaller than the unrestricted problem: its asymptotic constant is \(1/4\), not merely bounded above by \(1/2\).

These results also imply an unconditional structural consequence:

> For every fixed \(s\), all sufficiently high-dimensional extremal codes have more than \(s\) stars in every word.

The main limit question nevertheless remains unresolved here.

---

# 2. Signatures relative to an anchor

Fix an anchor \(x\in\mathcal C\) with exactly \(s\) stars. Permuting coordinates and interchanging \(0,1\) coordinatewise, assume
\[
x=0^m*^s,\qquad m=d-s.
\]

For \(y\in\mathcal C\setminus\{x\}\), define its **signature**
\[
S(y)=\{i\in[m]:y_i=1\}.
\]
Because
\[
|S(y)|=\delta(x,y),
\]
every signature has size one or two.

Also write
\[
Z_y=\{i\in[m]:y_i=0\},
\qquad
u(y)=y|_{\{m+1,\ldots,m+s\}}.
\]
The contribution of the first \(m\) coordinates to the distance between \(y,z\) is
\[
D(y,z)=|S(y)\cap Z_z|+|S(z)\cap Z_y|. \tag{2}
\]

Words with the same signature have no opposing coordinates among the first \(m\) coordinates. In particular:

* for a fixed signature and a fixed outside pattern \(u\), there is at most one word;
* the outside patterns occurring at any fixed signature form a 2-neighborly code.

The useful point is that repeated signatures are scarce when \(s\) is fixed.

## 2.1 A 1-neighborly bound

We shall use the elementary bound
\[
|\mathcal D|\le m+1 \tag{3}
\]
for a 1-neighborly code \(\mathcal D\) of length \(m\).

Here is the linear-algebra proof, so this use of the previous attempt does not depend on its authority. Each coordinate gives a complete bipartite adjacency matrix \(E_i\), and
\[
J-I=\sum_{i=1}^m E_i.
\]
Each \(E_i\) has at most one negative eigenvalue. Negative inertia is subadditive: intersect subspaces on which the summands are nonnegative. Since \(J-I\) has \(|\mathcal D|-1\) negative eigenvalues, (3) follows.

## 2.2 Repeated-signature lemma

For an occurring signature \(S\), let \(r_S\) be its multiplicity.

### Lemma
\[
\sum_S(r_S-1)\le A_s(m+1)+B_s. \tag{4}
\]

### Proof
Fix two outside patterns \(u,v\) which occur together at some signature. Necessarily
\[
h=\delta(u,v)\in\{1,2\}.
\]
Suppose both patterns occur at two distinct signatures \(S,T\). Denote the four corresponding words by
\[
y_{S,u},\ y_{S,v},\ y_{T,u},\ y_{T,v}.
\]

Equation (2) gives the four-point identity
\[
\begin{aligned}
&D(y_{S,u},y_{T,u})+D(y_{S,v},y_{T,v})\\
&\hspace{1cm}=
D(y_{S,u},y_{T,v})+D(y_{S,v},y_{T,u}). \tag{5}
\end{aligned}
\]

The two terms on the left are at least \(1\), because their outside patterns are identical.

If \(h=2\), both terms on the right must be zero, a contradiction. Thus any fixed pair \(u,v\) at outside distance \(2\) occurs together at at most one signature.

If \(h=1\), both terms on the right are at most \(1\). Equality in (5) forces all four terms to equal \(1\). Therefore, over all signatures supporting both \(u,v\), the first-\(m\)-coordinate projections of the words with outside pattern \(u\) form a 1-neighborly code. By (3), there are at most \(m+1\) such signatures.

There are exactly
\[
s7^{s-1}=A_s
\]
unordered pairs of ternary words of length \(s\) at opposition distance \(1\), and exactly
\[
2\binom s2 7^{s-2}=B_s
\]
at opposition distance \(2\). Indeed, an ordered coordinate pair has two opposing possibilities and seven nonopposing possibilities.

Finally,
\[
r_S-1\le \binom{r_S}{2}.
\]
Summing over signatures and then over pairs of outside patterns proves (4). \(\square\)

There are at most \(m+\binom m2\) signatures. Consequently,
\[
|\mathcal C|
=1+\sum_S r_S
\le 1+m+\binom m2+A_s(m+1)+B_s,
\]
proving (1).

In particular, for fixed \(s\), all but \(O_s(m)\) words have distinct signatures. The same estimate proves the claimed growing-budget consequence when \(s7^s=o(d)\).

---

# 3. Existence of every fixed-budget limit

Let \(g_s(m)\) be the maximum number of nonanchor words in a code containing \(0^m*^s\), subject to every nonanchor word having a signature of size exactly two.

For \(2\le r\le m\), choose a uniformly random \(r\)-subset \(R\subseteq[m]\). Retain precisely the words whose signatures lie in \(R\), retain the anchor, and delete the coordinates in \([m]\setminus R\).

This preserves every distance between retained words. Indeed, every retained word has only \(0\) or \(*\) in a deleted coordinate, so no deleted coordinate was opposing. Each nonanchor word is retained with probability
\[
\frac{\binom r2}{\binom m2}.
\]
It follows that
\[
g_s(r)\ge \frac{\binom r2}{\binom m2}g_s(m). \tag{6}
\]
Thus
\[
\frac{g_s(m)}{\binom m2}
\]
is nonincreasing for \(m\ge2\). It is nonnegative, and the repeated-signature lemma gives
\[
g_s(m)\le \binom m2+O_s(m).
\]
Hence its limit, say \(\gamma_s\), exists and belongs to \([0,1]\).

Let \(F_s(m)\) be the maximum size of a code containing the specified anchor \(0^m*^s\), now allowing signatures of size one as well. There are at most \(3^s\) words at any given singleton signature. Therefore
\[
g_s(m)+1
\le F_s(m)
\le g_s(m)+3^s m+1.
\]
Consequently,
\[
\lim_{m\to\infty}\frac{F_s(m)}{(m+s)^2}
=\frac{\gamma_s}{2}. \tag{7}
\]

Appending common star coordinates shows that \(\gamma_s\), and hence these limits, are nondecreasing in \(s\). Finally,
\[
a_s(d)=\max_{0\le t\le s}F_t(d-t)
\]
for all sufficiently large \(d\). This is a maximum over finitely many convergent normalized sequences, whose limiting values are nondecreasing in \(t\). Thus
\[
\lambda_s=\lim_{d\to\infty}\frac{a_s(d)}{d^2}
=\frac{\gamma_s}{2}.
\]

This proves existence and monotonicity for every fixed budget.

---

# 4. A forbidden signature configuration

The next lemma supplies a stronger asymptotic restriction.

### Lemma
Suppose a collection of words has exactly two \(1\)'s per word among a set of coordinates, and all words have the same pattern outside those coordinates. If the words are 2-neighborly, their two-element signatures cannot include all the edges of \(K_{2,2,2}\).

### Proof
Suppose otherwise. Restrict attention to the six coordinates forming the three parts of \(K_{2,2,2}\), and to its twelve edge-words. Coordinates outside these six contribute no opposition: outside patterns are identical, and the remaining base coordinates have no \(1\)'s.

For an edge \(e\) and a coordinate \(w\notin e\), let
\[
z_{e,w}=
\begin{cases}
1,&\text{if the edge-word for }e\text{ has }0\text{ at }w,\\
0,&\text{if it has }*\text{ at }w.
\end{cases}
\]

Let \(Z_{\parallel}\) be the sum of incidences \(z_{e,w}\) where \(w\) lies in the same part as an endpoint of \(e\), and let \(Z_{\perp}\) count those where \(w\) lies in the third part.

**Same-part incidences.** Fix a vertex \(v\) in one part and the two vertices \(u,u'\) in another. The words for \(uv,u'v\) must oppose, so
\[
z_{uv,u'}+z_{u'v,u}\ge1.
\]
The twelve such inequalities partition the same-part incidences. Hence
\[
Z_{\parallel}\ge12. \tag{8}
\]

**Third-part incidences.** In each of the eight triangles, put
\[
a=z_{uv,w},\qquad b=z_{uw,v},\qquad c=z_{vw,u}.
\]
Neighborliness gives
\[
a+b\ge1,\qquad a+c\ge1,\qquad b+c\ge1.
\]
Since \(a,b,c\in\{0,1\}\), their sum is at least \(2\). Thus
\[
Z_{\perp}\ge16. \tag{9}
\]

There are
\[
\binom{12}{2}-6\binom42=30
\]
pairs of disjoint edges. Their distances sum to at most \(60\).

Each same-part incidence contributes to exactly three of these distances, while each third-part incidence contributes to exactly two. Therefore the same sum is
\[
3Z_{\parallel}+2Z_{\perp}
\ge 3\cdot12+2\cdot16=68,
\]
a contradiction. \(\square\)

We use below the standard Erdős–Stone theorem in the form
\[
\operatorname{ex}(m,K_r(L))
=
\left(\frac12-\frac{1}{2(r-1)}+o(1)\right)m^2 \tag{10}
\]
for fixed \(r,L\), where \(K_r(L)\) is complete \(r\)-partite with \(L\) vertices in each part.

---

# 5. The full-support constant is \(1/4\)

Suppose \(s=0\). Every signature occurs at most once. Make a graph \(G\) on \([d]\) whose edges are the occurring two-element signatures.

The preceding lemma says that \(G\) is \(K_{2,2,2}\)-free. Thus
\[
|\mathcal C|\le 1+d+e(G)
\le \left(\frac14+o(1)\right)d^2
\]
by (10).

For the lower bound, let
\[
L_m=
\{1^j0*^{m-j-1}:0\le j<m\}\cup\{1^m\}.
\]
It is a 1-neighborly code of size \(m+1\). Hence
\[
L_{\lfloor d/2\rfloor}\times L_{\lceil d/2\rceil}
\]
is 2-neighborly, contains a full-support word, and has size
\[
(\lfloor d/2\rfloor+1)(\lceil d/2\rceil+1)
=\left(\frac14+o(1)\right)d^2.
\]
Therefore
\[
\boxed{\lambda_0=\frac14}.
\]

## 5.1 A strict gap below \(1/2\) for every fixed budget

For a general fixed \(s\), choose one word for each occurring two-element signature and color that signature by its outside pattern. This gives an edge-colored graph \(G\) with at most
\[
q=3^s
\]
colors. Every color class is \(K_{2,2,2}\)-free, by the lemma.

Let \(R=R_q(6)\) be the ordinary finite Ramsey number ensuring a monochromatic \(K_6\) in every \(q\)-coloring of \(K_R\). Since \(K_6\) contains \(K_{2,2,2}\), the graph \(G\) is \(K_R\)-free. Turán's theorem gives
\[
e(G)\le \frac12\left(1-\frac1{R-1}\right)m^2.
\]
Repeated signatures contribute only \(O_s(m)\), so
\[
\boxed{\lambda_s\le
\frac12\left(1-\frac1{R_{3^s}(6)-1}\right)<\frac12}. \tag{11}
\]

The gap in (11) is very small, but it is positive for every fixed \(s\).

---

# 6. The one-star constant is \(1/3\)

We now prove the sharper value for \(s=1\).

## 6.1 Upper bound

Normalize the anchor to \(0^m*\). Choose one word for each two-element signature, producing a graph \(G\) on \([m]\). Its edge-word has a tag in \(\{0,1,*\}\) at the final coordinate.

By (4), the total number of repeated signatures is at most \(m+1\), so
\[
|\mathcal C|\le e(G)+2m+2. \tag{12}
\]

We show that \(G\) excludes \(K_4(L)\) for some fixed finite \(L\).

Suppose a sufficiently large complete four-partite subgraph exists. Finite Ramsey theory allows us to retain two vertices in each part such that:

* all edge-words between parts \(i,j\) have a common tag \(u_{ij}\);
* for distinct parts \(i,j,k\), the indicator that an \(ij\)-edge-word has \(0\) at a vertex of part \(k\) is constant, say \(z_{ij,k}\).

For completeness, this is a finite, precisely specified extraction. Color each transversal triple by its three edge-tags and its three zero-indicators; there are at most \(3^3 2^3=216\) colors. If all four parts are indexed by \([L]\), color each increasing triple of indices by the data for the four triples of parts. The finite hypergraph Ramsey number
\[
L=R^{(3)}_{216^4}(8)
\]
suffices. From a homogeneous eight-set, assign consecutive pairs of indices to the four parts.

For three distinct parts \(i,j,k\), put
\[
D_{i;jk}
=\delta(u_{ij},u_{ik})+z_{ij,k}+z_{ik,j}. \tag{13}
\]
Comparing edge-words for \(ab,ac\), with \(a,b,c\) in parts \(i,j,k\), shows that \(D_{i;jk}\in\{1,2\}\).

In fact,
\[
D_{i;jk}=1. \tag{14}
\]
To see this, suppose it were \(2\). Compare the words for \(ab,a'c\), where \(a\ne a'\) are the two selected vertices in part \(i\). The contribution in (13) already equals \(2\), forcing both possible additional oppositions at \(a,a'\) to vanish. Varying the choices forces
\[
z_{ab,a'}=z_{a'b,a}=0.
\]
But then the words for \(ab,a'b\) have distance zero, a contradiction.

Consider a triangle of parts. Write its three tags as \(u,v,w\), and its three zero-indicators as \(a,b,c\). Equation (14) gives
\[
a+b=1-\delta(u,v),\qquad
a+c=1-\delta(u,w),\qquad
b+c=1-\delta(v,w). \tag{15}
\]
Adding these equations shows that the number of opposing tag-pairs must be odd.

For three symbols from \(\{0,1,*\}\), this happens exactly when the tags are \(0,1,*\), all distinct. Moreover, (15) then says that the zero-indicator belonging to the \(*\)-tagged edge is \(1\), and those belonging to the \(0\)- and \(1\)-tagged edges are \(0\).

Thus every triangle of the four part-indices has all three edge-colors \(0,1,*\). This is a proper three-edge-coloring of \(K_4\), so each color forms a perfect matching.

Take the two disjoint edges colored \(0\). Their tags are equal. Every zero-indicator toward an endpoint of the other edge is zero, by the triangle conclusion above. Their edge-words therefore have distance zero, a final contradiction.

Hence \(G\) is \(K_4(L)\)-free for a fixed \(L\). By Erdős–Stone and (12),
\[
|\mathcal C|\le \left(\frac13+o(1)\right)m^2.
\]

## 6.2 Lower bound

Put
\[
P_m=\{1^j0*^{m-j-1}:0\le j<m\}.
\]
Distinct words in \(P_m\) have opposition distance \(1\), and
\[
\delta(u,1^m)=1\qquad(u\in P_m).
\]

Use three blocks \(A,B,C\), each of length \(m\), and one tag coordinate. Take the anchor
\[
x=(1^m,1^m,1^m,*)
\]
and the three groups
\[
\begin{aligned}
\mathcal G_{AB}&=\{(u,v,1^m,*):u,v\in P_m\},\\
\mathcal G_{AC}&=\{(u,*^m,w,0):u,w\in P_m\},\\
\mathcal G_{BC}&=\{(*^m,v,w,1):v,w\in P_m\}.
\end{aligned}
\]

Within a group, distances are one or two. Between \(\mathcal G_{AB}\) and either other group, there is one opposition from block \(C\), plus at most one from the shared active block. Between \(\mathcal G_{AC}\) and \(\mathcal G_{BC}\), there is one opposition in the tag, plus at most one in block \(C\). Every nonanchor word has distance exactly two from \(x\).

The code therefore has length \(3m+1\), size \(3m^2+1\), and an anchor with one star. Padding with common fixed coordinates handles all dimensions asymptotically. Thus
\[
\boxed{\lambda_1=\frac13}.
\]

---

# 7. The fixed-budget constants approach \(1/2\)

Here is a directly checked anchored variant of the tagged-block construction in the supplied attempt.

Fix \(r\ge2\), and put
\[
g=\binom r2.
\]
Use \(r\) factor blocks of length \(m\), together with \(g-1\) tag coordinates. Assign to the \(g\) pairs \(e\in\binom{[r]}2\) the distinct tags of \(L_{g-1}\).

For \(e=\{i,j\}\), take all words which have:

* arbitrary members of \(P_m\) in blocks \(i,j\);
* stars in all other factor blocks;
* the tag assigned to \(e\).

Add the anchor
\[
x=(1^{rm},*^{g-1}).
\]

Words from the same group have distance one or two. Words from different groups have one opposition in their tags, plus at most one in their common factor block. Every nonanchor word has exactly two oppositions with the anchor.

Thus
\[
N=g m^2+1,\qquad D=rm+g-1.
\]
For every \(s\ge g-1\), append \(s-(g-1)\) common star coordinates. Letting \(m\to\infty\) gives
\[
\lambda_s\ge \frac{g}{r^2}
=\frac{r-1}{2r}
\qquad\left(s\ge \binom r2-1\right). \tag{16}
\]
Combining (16), monotonicity, and (11),
\[
\boxed{\lambda_s\uparrow\frac12}.
\]

These constructions also recover the unrestricted lower bound
\[
\liminf_{d\to\infty}\frac{n(2,d)}{d^2}\ge\frac12.
\]

---

# 8. What is still missing

The proved iterated limit is
\[
\lim_{s\to\infty}\ \lim_{d\to\infty}\frac{a_s(d)}{d^2}
=\frac12.
\]
The original problem concerns the diagonal:
\[
n(2,d)=a_d(d).
\]
No interchange of these limits has been justified.

Estimate (1) provides sufficient uniformity only when an anchor has
\[
s7^s=o(d).
\]
A general extremal code has not been shown to possess such an anchor, nor to admit a modification producing one while losing only \(o(d^2)\) words.

Indeed, the results expose a genuine escape from every fixed-budget class. For fixed \(s\),
\[
\lambda_s<\frac12,
\]
whereas the unrestricted lower bound has constant \(1/2\). Hence, for sufficiently large \(d\), an extremal code cannot contain any word with at most \(s\) stars.

Accordingly, this is a family of resolved anchored special cases and a uniform bound in a slowly growing-star regime—not a proof of existence of the unrestricted limit.