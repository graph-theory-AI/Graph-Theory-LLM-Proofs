```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A punctured-coset obstruction gives T(G) <= 3 sqrt(|G|) - 4 for every abelian group of square order at least 16, and a sharp packing criterion gives square-root-scale lower bounds for structured sets.",
  "would_publish": false,
  "caveats": "The universal lower bound and prime-order upper bound are not obtained; novelty of the partial results has not been checked."
}
```

# Partial results

I do not resolve Conjecture 7. I obtain three precise results:

1. An upper-bound construction requiring only a **balanced subgroup**, rather than the balanced direct-product decomposition used in the previous attempt. In particular,
   \[
   T(G)\le 3\sqrt{|G|}-4
   \]
   for every finite abelian group of square order at least \(16\), including cyclic groups of square order.
2. An exact characterization of when a punctured subgroup \(H\setminus\{0\}\) is a minimal complement in an ambient group.
3. A sufficient condition
   \[
   |G|>(|C|-1)|2C-2C|
   \tag{1}
   \]
   for \(C\) to be a minimal complement. The strict inequality is sharp for an infinite family.

Only the elementary private-sum characterization from the previous attempt is used; I verify it below. None of that attempt’s probabilistic estimates is assumed.

## 1. Definitions and private sums

Let \(G\) be a finite abelian group of order \(n\). Use the threshold definition
\[
T(G)=\max\left\{t\le n:
  \text{every nonempty }C\subseteq G,\ |C|\le t,
  \text{ is a minimal complement to some }W\subseteq G
\right\}.
\]

For \(C,W\subseteq G\), write
\[
r_{C,W}(g)=|\{(c,w)\in C\times W:c+w=g\}|.
\]

Suppose \(C+W=G\). Then \(C\) is minimal for \(W\) if and only if, for every \(c\in C\), there is a \(g\in G\) whose unique representation is \(g=c+w\).

Indeed, removing \(c\) destroys coverage precisely when some
\[
g\in(c+W)\setminus((C\setminus\{c\})+W)
\]
exists. Once \(c\) and \(g\) are specified, \(w=g-c\) is unique. Private sums for different elements of \(C\) must be different. Consequently,
\[
C\text{ minimal for }W
\quad\Longrightarrow\quad
|\{g:r_{C,W}(g)=1\}|\ge |C|.
\tag{2}
\]

## 2. An obstruction from almost-full subgroup cosets

The following counting observation removes the need for a split extension.

### Proposition 2.1

Let \(H\le G\), with
\[
|H|=h,\qquad [G:H]=q.
\]
Suppose every nonempty intersection of \(C\) with an \(H\)-coset has between \(h-r\) and \(h-1\) elements, where \(1\le r<h\).

For every \(W\subseteq G\) satisfying \(C+W=G\),
\[
|\{g:r_{C,W}(g)=1\}|\le 2rq.
\tag{3}
\]
In particular, if \(|C|>2rq\), then \(C\) is not a minimal complement.

#### Proof

Write the nonempty fibers of \(C\) as
\[
C_i=C\cap Q_i,
\]
where the \(Q_i\) are distinct \(H\)-cosets.

Fix an output coset \(Q\). Consider the indexed family
\[
\mathcal F_Q=
\bigl(C_i+w:\ Q_i+w=Q,\ w\in W\bigr),
\]
counted with multiplicity. Let its number of members be \(t\).

Every member is a proper subset of \(Q\) omitting at most \(r\) points. Since \(C+W=G\), this family covers \(Q\). Thus \(t\ge2\).

For \(g\in Q\), the number of members containing \(g\) is exactly \(r_{C,W}(g)\). If \(u\) points of \(Q\) have exactly one representation, each is omitted by \(t-1\) members. Counting omissions gives
\[
u(t-1)
\le
\sum_{F\in\mathcal F_Q}|Q\setminus F|
\le rt.
\]
Hence
\[
u\le \frac{rt}{t-1}\le 2r.
\]
Summing over the \(q\) output cosets proves (3). The last assertion follows from (2). ∎

### Corollary 2.2: balanced-subgroup upper bound

If \(G\) has a subgroup of order \(h\ge4\) and index \(q\), then
\[
T(G)\le
(h-1)\left(\left\lfloor\frac{2q}{h-1}\right\rfloor+1\right)-1
\le h+2q-2.
\tag{4}
\]

#### Proof

Set
\[
k=\left\lfloor\frac{2q}{h-1}\right\rfloor+1.
\]
Since \(h-1>2\), we have \(k\le q\). Choose \(k\) distinct \(H\)-cosets and delete exactly one point from each. Their union \(C\) has
\[
|C|=k(h-1)>2q.
\]
Proposition 2.1 with \(r=1\) shows that \(C\) is not a minimal complement. This gives the first inequality in (4); the second follows from
\[
k(h-1)\le 2q+h-1.
\]
∎

Thus, if \(G\) has a subgroup satisfying
\[
\frac{\sqrt n}{L}\le h\le L\sqrt n,
\]
then
\[
T(G)\le 3L\sqrt n-2.
\tag{5}
\]
In particular, a subgroup balanced within polylogarithmic factors suffices for the conjectured upper order.

### Corollary 2.3: every square-order abelian group

For every finite abelian group of order \(s^2\), where \(s\ge4\),
\[
\boxed{T(G)\le 3s-4.}
\tag{6}
\]

#### Proof

A finite abelian group has a subgroup of every order dividing its order: this follows componentwise from its cyclic primary decomposition. Choose \(H\) of order \(s\), hence index \(s\).

Take three \(H\)-cosets and delete one point from each. The resulting set has
\[
3(s-1)>2s
\]
elements, so Proposition 2.1 applies. ∎

For the cyclic group \(G=\mathbb Z/s^2\mathbb Z\), an explicit example is
\[
C=
\{\,i+js:\ i\in\{0,1,2\},\ 1\le j\le s-1\,\}.
\tag{7}
\]
It consists of three punctured cosets of the subgroup
\[
H=\{0,s,\ldots,(s-1)s\}.
\]

This specifically covers cyclic groups such as \(\mathbb Z/p^2\mathbb Z\), which the previous direct-product construction did not handle. These are obstructions at the conjectured scale, not counterexamples to the conjecture.

## 3. Exact classification for a punctured subgroup

A single punctured subgroup admits a sharper analysis than Proposition 2.1.

For a finite abelian group \(H\), define
\[
H[2]=\{x\in H:2x=0\}.
\]

### Theorem 3.1

Let \(H\le G\), with \(h=|H|\ge2\) and \(q=[G:H]\). Then
\[
\boxed{
H\setminus\{0\}\text{ is a minimal complement in }G
\quad\Longleftrightarrow\quad
q\ge \frac{h+|H[2]|-2}{2}.
}
\tag{8}
\]

#### Proof

Put \(C=H\setminus\{0\}\). Since \(C\subseteq H\), distinct \(H\)-cosets can be analyzed independently.

For an \(H\)-coset \(Q\), set \(W_Q=W\cap Q\). For every \(z\in Q\),
\[
r_{C,W}(z)=|W_Q|-\mathbf 1_{\{z\in W_Q\}}.
\tag{9}
\]
Indeed, every \(w\in W_Q\) gives \(z-w\in H\), and the only forbidden summand is \(z-w=0\), equivalently \(w=z\).

It follows that:

- Coverage of \(Q\) requires \(|W_Q|\ge2\).
- If \(|W_Q|\ge3\), no point of \(Q\) has a unique representation.
- If \(W_Q=\{u,v\}\), its two uniquely represented points are \(u\) and \(v\), with corresponding \(C\)-summands
  \[
  u-v,\qquad v-u.
  \]

Thus each ambient coset can make essential the elements of at most one inversion orbit
\[
\{d,-d\}\subseteq H\setminus\{0\}.
\]

The number of these orbits is
\[
\nu(H)
=
\frac{(h-1)+(|H[2]|-1)}2
=
\frac{h+|H[2]|-2}{2}.
\tag{10}
\]
Therefore minimality requires \(q\ge\nu(H)\).

Conversely, suppose \(q\ge\nu(H)\). Assign a distinct ambient coset to each inversion orbit, and choose a representative \(d\ne0\) of that orbit. In its assigned coset \(t+H\), put
\[
W\cap(t+H)=\{t,t+d\}.
\]
Use any two distinct points in each remaining coset.

Equation (9) shows that every coset is covered. The assigned coset supplies private sums for both \(d\) and \(-d\), or for their single common value when \(d=-d\). Every element of \(C\) is therefore essential. ∎

Two useful special cases are
\[
\nu(H)=
\begin{cases}
(h-1)/2,& |H|\text{ odd},\\[2mm]
h-1,& H\text{ elementary abelian of exponent }2.
\end{cases}
\tag{11}
\]

This is an exact quadratic-scale transition: a punctured subgroup of size approximately \(h\) needs approximately \(h\) ambient cosets, with the precise constant controlled by its involutions.

## 4. A sharp structured-set lower bound

Write
\[
2C-2C=C+C-C-C.
\]

### Theorem 4.1

Every nonempty \(C\subseteq G\), with \(m=|C|\), satisfying
\[
\boxed{n>(m-1)|2C-2C|}
\tag{12}
\]
is a minimal complement.

#### Proof

The singleton case is immediate. Assume \(m\ge2\), and enumerate
\[
C=\{c_1,\ldots,c_m\}.
\]
Put
\[
D=C-C,\qquad E=D-D=2C-2C.
\]

We can greedily choose \(g_1,\ldots,g_m\in G\) so that the translates
\[
g_i+D
\]
are pairwise disjoint. After choosing \(g_1,\ldots,g_{i-1}\), a new choice need only avoid
\[
\bigcup_{j<i}(g_j+E),
\]
whose size is at most \((i-1)|E|<n\).

Define
\[
Y_i=g_i-(C\setminus\{c_i\}),\qquad
Y=\bigcup_{i=1}^mY_i,\qquad
W=G\setminus Y.
\]

First,
\[
w_i:=g_i-c_i\in W.
\]
It is not in \(Y_i\). If it belonged to \(Y_j\), \(j\ne i\), then for some \(c\in C\),
\[
g_i-c_i=g_j-c,
\]
giving \(g_i-g_j=c_i-c\in D\subseteq E\), contrary to the construction.

We next prove coverage. If a translate \(z-C\) meets \(Y_i\), then
\[
z\in g_i+(C-C)=g_i+D.
\]
Since the latter translates are pairwise disjoint, \(z-C\) can meet at most one \(Y_i\). It therefore cannot be contained in \(Y\): it has \(m\) elements, whereas each \(Y_i\) has only \(m-1\).

Consequently, for every \(z\in G\), some \(z-c\) lies in \(W\), proving \(C+W=G\).

Finally, \(g_i=c_i+w_i\), while
\[
g_i-c_j\in Y_i
\qquad(j\ne i).
\]
Thus \(g_i\) is private to \(c_i\). Every element of \(C\) is essential. ∎

### Square-root consequences

If
\[
|2C-2C|\le K|C|,
\]
then Theorem 4.1 applies whenever
\[
K|C|^2\le n.
\tag{13}
\]
Thus the conjectured square-root lower scale holds for the class of sets whose fourfold difference set has at most a polylogarithmic expansion factor.

For an elementary example, suppose \(C\) lies in a proper arithmetic progression of length \(\ell\), and
\[
|C|\ge\delta\ell.
\]
Then
\[
|2C-2C|\le4\ell-3\le\frac{4|C|}{\delta}.
\]
Hence
\[
\boxed{
n\ge\frac{4|C|^2}{\delta}
\quad\Longrightarrow\quad
C\text{ is a minimal complement}.
}
\tag{14}
\]
Unlike a bounded-difference-multiplicity criterion, this permits differences occurring almost \(|C|\) times.

### Sharpness of the strict inequality

Let
\[
H=(\mathbb Z/2\mathbb Z)^a,\qquad h=2^a\ge4,
\]
and take
\[
G=H\times\mathbb Z/(h-2)\mathbb Z,
\qquad
C=(H\setminus\{0\})\times\{0\}.
\]

The subgroup \(H\times\{0\}\) has index \(h-2\). By Theorem 3.1, \(C\) is not a minimal complement, since
\[
h-2<h-1=\nu(H).
\]

Moreover, \(C-C=H\times\{0\}\), so
\[
|2C-2C|=h.
\]
Writing \(m=|C|=h-1\), we obtain
\[
|G|=h(h-2)=(m-1)|2C-2C|.
\tag{15}
\]
Thus replacing the strict inequality in Theorem 4.1 by a non-strict one would be false.

These examples also give
\[
|G|=m^2-1,\qquad
T(G)\le m-1=\sqrt{|G|+1}-1,
\tag{16}
\]
an explicit infinite family of obstructions essentially at the square-root scale.

## 5. What remains unresolved

The results above do **not** establish either missing universal estimate.

- **Lower bound:** Condition (12) is effective for small fourfold difference sets, but arbitrary sets of size \(\sqrt n/\operatorname{polylog}n\) need not satisfy it. Sets may simultaneously have large difference multiplicities and large fourfold difference sets, escaping both this argument and the previous attempt’s bounded-multiplicity method.
- **Upper bound:** The punctured-coset construction requires a suitably sized subgroup. For \(\mathbb Z/p\mathbb Z\), the only usable subgroup is the whole group, giving merely a linear-size obstruction. No improvement of the supplied general \(O(n^{3/4+\varepsilon})\) bound is proved here.
- Even for square-order groups, (6) establishes only the conjectured **upper** order, not the matching universal lower order.

The main advance over the supplied attempt is therefore the nonsplit, balanced-subgroup obstruction, together with the exact punctured-subgroup classification and the sharp structured-set packing criterion. I have not checked whether these elementary results already occur in the source paper or subsequent literature, so I make no novelty claim.