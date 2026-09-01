```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "In the bidirected undirected PMC model, pairwise ambiguity has an exact vertex-boundary characterization, and a normalized bipartite-hole parameter η=o(1) suffices to certify a 1-O(η) fraction of both types, although this does not yield a full necessary-and-sufficient characterization.",
  "would_publish": false,
  "caveats": "The original item is a research direction rather than a formal conjecture; the separator characterization likely overlaps known follow-up work, and efficient algorithms and directed graphs are not addressed."
}
```

# 1. Formal setting

The catalog item is not a proposition with a definite truth value. I therefore use the following standard undirected specialization of the PMC model.

Let \(G=(V,E)\), \(|V|=n\). Each undirected edge is queried in both directions. A report pattern is a collection
\[
r_{uv}\in\{\mathrm T,\mathrm C\},\qquad uv\in E,
\]
where \(r_{uv}\) is \(u\)'s report about \(v\).

A set \(T\subseteq V\) is a **feasible truthful set** if

1. \(|T|>n/2\), and
2. for every \(u\in T\) and \(v\in N(u)\),
   \[
   r_{uv}=\mathrm T \quad\Longleftrightarrow\quad v\in T.
   \]

Vertices outside \(T\) are corrupt and their reports are unrestricted.

For a fixed report pattern, let \(\mathcal F\) be the family of feasible truthful sets. Define
\[
T_{\rm fix}:=\bigcap_{T\in\mathcal F}T,\qquad
C_{\rm fix}:=V\setminus\bigcup_{T\in\mathcal F}T.
\]
These are precisely the vertices whose status is information-theoretically identifiable.

The results below are not claimed to settle the catalog problem, but they give a fairly clean interpolation between spectral expansion and separators.

---

# 2. Exact characterization of pairwise ambiguity

For \(S\subseteq V\), write
\[
\partial S:=N(S)\setminus S
\]
for its external vertex boundary, and let
\[
\pi(S):=|S|\pmod 2\in\{0,1\}.
\]

Define
\[
\mu(G):=
\max\left\{
|S|:\ n-|S|-2|\partial S|>\pi(S)
\right\},
\]
with the maximum equal to \(0\) if there is no nonempty qualifying set.

## Theorem 2.1

The maximum, over all report patterns and all pairs \(T_1,T_2\) of strict-majority feasible truthful sets, of
\[
|T_1\triangle T_2|
\]
is exactly \(\mu(G)\).

Thus, up to the parity correction, a set \(S\) can be switched between two feasible worlds exactly when
\[
|S|+2|\partial S|<n.
\]

### Proof: upper bound

Let \(T_1,T_2\) be distinct feasible truthful sets. Put
\[
A=T_1\cap T_2,\qquad
B=V\setminus(T_1\cup T_2),
\]
and
\[
X=T_1\setminus T_2,\qquad
Y=T_2\setminus T_1,\qquad
D=X\cup Y=T_1\triangle T_2.
\]

No edge joins \(A\) to \(D\). Indeed, if \(u\in A\) and \(v\in D\), then \(u\) is truthful in both worlds while the status of \(v\) differs, so the fixed report \(r_{uv}\) cannot be correct in both worlds. Consequently,
\[
\partial D\subseteq B.
\]

Let \(a=|A|, b=|B|, x=|X|, y=|Y|\), and \(q=a-b\). The two majority inequalities are
\[
q+x-y>0,\qquad q-x+y>0.
\]
Hence
\[
q>|x-y|\ge \pi(D).
\]
Moreover,
\[
n-|D|-2|\partial D|
\ge n-|D|-2b
=a-b=q.
\]
Therefore
\[
n-|D|-2|\partial D|>\pi(D),
\]
so \(|D|\le \mu(G)\).

### Proof: lower bound

Let \(D\subseteq V\) satisfy
\[
q:=n-|D|-2|\partial D|>\pi(D).
\]
Set
\[
B=\partial D,\qquad A=V\setminus(D\cup B).
\]
Then there are no edges between \(A\) and \(D\), and
\[
|A|-|B|=q.
\]

Partition \(D=X\sqcup Y\) so that
\[
\bigl||X|-|Y|\bigr|=\pi(D).
\]
Define
\[
T_1=A\cup X,\qquad T_2=A\cup Y.
\]
Their truthful-minus-corrupt margins are
\[
q+|X|-|Y|,\qquad q-|X|+|Y|,
\]
which are both positive.

It remains to construct one report pattern making both worlds feasible. For each reporter \(u\):

- if \(u\in A\), report according to the common statuses of \(A\) and \(B\); there are no neighbors of \(u\) in \(D\);
- if \(u\in X\), report according to \(T_1\);
- if \(u\in Y\), report according to \(T_2\);
- if \(u\in B\), report arbitrarily.

A vertex of \(X\) is truthful only in the first world, and a vertex of \(Y\) only in the second, so there is no conflict. Thus \(T_1,T_2\) are both feasible and differ on all of \(D\). ∎

## Consequence and limitation

Selecting any feasible assignment gives a classification differing from the actual one on at most \(\mu(G)\) vertices. Conversely, a maximizing set produces two worlds in which every vertex of that set is non-identifiable.

However, \(\mu(G)\) controls only the distance between two feasible worlds. It does **not** bound the union of all vertices whose status varies among many feasible worlds. This distinction is essential for the original corruption-detection question.

---

# 3. A normalized bipartite-hole expansion parameter

Define
\[
\eta(G):=
\max_{\substack{X,Y\ne\varnothing\\X\cap Y=\varnothing\\e(X,Y)=0}}
\frac{|X||Y|}{(n-|X|)(n-|Y|)}.
\]
Set \(\eta(G)=0\) if there is no such pair.

Small \(\eta(G)\) says that two disjoint anticomplete sets cannot both be moderately large. This is the expansion property actually used in the argument below.

If \(G\) is \(d\)-regular and
\[
\lambda=\max_{i\ge2}|\lambda_i(G)|,
\]
then the expander-mixing calculation gives
\[
\eta(G)\le \left(\frac{\lambda}{d}\right)^2.
\]
Indeed, if \(e(X,Y)=0\), then
\[
\frac{d|X||Y|}{n}
 \le
\lambda\sqrt{|X|\left(1-\frac{|X|}{n}\right)
             |Y|\left(1-\frac{|Y|}{n}\right)},
\]
and squaring and simplifying yields the assertion.

The preceding pairwise theorem also immediately gives:

## Corollary 3.1

If \(\eta(G)<1\), then any two feasible truthful sets satisfy
\[
\frac{|T_1\triangle T_2|}{n}
<
\frac{\eta(G)}{1-\eta(G)}.
\]

In particular, for a \(d\)-regular graph,
\[
|T_1\triangle T_2|
<
\frac{\lambda^2}{d^2-\lambda^2}\,n.
\]

For a Ramanujan-type bound \(\lambda\le2\sqrt{d-1}\), this becomes
\[
|T_1\triangle T_2|
<
\frac{4(d-1)}{(d-2)^2}\,n
=
\left(\frac4d+O(d^{-2})\right)n.
\]

More generally, the Ramanujan constant \(2\) is irrelevant here: every bound
\[
\lambda\le C\sqrt d
\]
gives pairwise error \(O_C(n/d)\), and \(\lambda=o(d)\) gives \(o(n)\).

---

# 4. Certification from bipartite-hole expansion

The next result concerns genuine identification, not merely approximate reconstruction.

For \(0\le z\le1/10\), define
\[
q(z)=
\frac{1-\sqrt{(1-9z)/(1-z)}}{2}
\]
and
\[
p(z)=
\frac{2z(1+q(z))}
     {1-q(z)+z(1+q(z))}.
\]
As \(z\to0\),
\[
q(z)=2z+O(z^2),\qquad p(z)=2z+O(z^2).
\]

## Theorem 4.1

Suppose \(\eta(G)\le 1/10\). For every report pattern and every actual feasible partition \(V=T\sqcup C\), one has
\[
|T\setminus T_{\rm fix}|<q(\eta(G))\,|C|
\]
and
\[
|C\setminus C_{\rm fix}|<p(\eta(G))\,|C|.
\]

Consequently, if \(\eta(G)=o(1)\), a \(1-o(1)\) fraction of each type is identifiable. If \(G\) is \(d\)-regular and \(\lambda=o(d)\), then
\[
\frac{|T\setminus T_{\rm fix}|}{|T|}
,\ 
\frac{|C\setminus C_{\rm fix}|}{|C|}
=
O\!\left(\frac{\lambda^2}{d^2}\right).
\]

### Proof

Write
\[
t=|T|,\qquad c=|C|,\qquad t>c.
\]

#### Step 1: \(G[T]\) has one large component

Let \(L\) be a largest connected component of \(G[T]\), of size \(l\).

Suppose \(l\le t/2\). By grouping connected components, one can partition \(T=U\sqcup W\) so that
\[
t/3\le |U|,|W|\le2t/3.
\]
There are no edges between \(U\) and \(W\). If \(u=|U|\), \(w=|W|\), then
\[
uw\ge \frac{2t^2}{9}.
\]
Moreover,
\[
(n-u)(n-w)=n(n-t)+uw.
\]
Since \(t>n/2\), it follows that
\[
\frac{uw}{(n-u)(n-w)}>\frac1{10},
\]
contradicting \(\eta(G)\le1/10\). Hence
\[
l>t/2.
\]

Let
\[
R=T\setminus L,\qquad r=|R|.
\]
Since \(e(L,R)=0\),
\[
\frac{lr}{(n-l)(n-r)}\le\eta,
\qquad \eta:=\eta(G).
\]

If \(c>0\), put
\[
x=\frac rc,\qquad y=\frac tc>1.
\]
Since \(l=t-r>t/2\), one has \(x<y/2\). The preceding inequality becomes
\[
\frac{(y-x)x}{(1+x)(y-x+1)}\le\eta.
\]

If \(x\ge1/2\), then \(y-x>x\), and the left side is greater than
\[
\left(\frac{x}{1+x}\right)^2\ge\frac19,
\]
a contradiction. Thus \(x<1/2\). Since \(y>1\),
\[
\frac{(y-x)x}{(1+x)(y-x+1)}
>
\frac{x(1-x)}{(1+x)(2-x)}.
\]
Solving
\[
\frac{x(1-x)}{(1+x)(2-x)}=\eta
\]
for the smaller root gives \(x=q(\eta)\). Therefore
\[
r<q(\eta)c.
\]

If \(c=0\), the same no-edge inequality forces \(r=0\).

#### Step 2: the component \(L\) is certainly truthful

Call an edge \(uv\) **positive** if both endpoints report the other as truthful. In any feasible world, the endpoints of a positive edge have the same status: if exactly one were truthful, that endpoint's positive report would be false.

Every edge of \(G[T]\) is positive, while no edge between \(T\) and \(C\) is positive. Thus \(L\) is a connected component of the positive-edge graph and is monochromatic in every feasible world.

Suppose another feasible truthful set \(T'\) classified any vertex of \(L\) as corrupt. It would then classify all of \(L\) as corrupt, so
\[
|T\triangle T'|\ge l>t/2>n/4.
\]
But Corollary 3.1 gives
\[
|T\triangle T'|
<
\frac{\eta}{1-\eta}n
\le\frac n9,
\]
a contradiction. Hence
\[
L\subseteq T_{\rm fix}.
\]
Therefore
\[
|T\setminus T_{\rm fix}|
\le r<q(\eta)c.
\]

#### Step 3: almost every corrupt vertex neighbors \(L\)

Every vertex outside \(L\) adjacent to \(L\) is corrupt in the actual world, since \(L\) is a component of \(G[T]\). Since vertices of \(L\) are certainly truthful, their reports certify all such neighbors as corrupt.

Let \(C_0\subseteq C\) be the corrupt vertices having no neighbor in \(L\), and put \(c_0=|C_0|\). Then \(e(L,C_0)=0\), so
\[
\frac{lc_0}{(n-l)(n-c_0)}\le\eta.
\]

For \(c>0\), put \(z=c_0/c\), and retain \(x=r/c\), \(y=t/c\). This becomes
\[
\frac{(y-x)z}{(1+x)(y+1-z)}\le\eta.
\]
Solving for \(z\),
\[
z\le
\frac{\eta(1+x)(y+1)}
     {y-x+\eta(1+x)}.
\]
For fixed \(x\), the right side decreases with \(y\), and \(y>1\). It increases with \(x\). Since \(x<q(\eta)\),
\[
z<
\frac{2\eta(1+q(\eta))}
     {1-q(\eta)+\eta(1+q(\eta))}
=p(\eta).
\]
Thus
\[
|C\setminus C_{\rm fix}|\le c_0<p(\eta)c.
\]
This proves the theorem. ∎

## Spectral corollary

If \(G\) is \(d\)-regular and
\[
s:=\left(\frac{\lambda}{d}\right)^2\le\frac1{10},
\]
then Theorem 4.1 applies with \(\eta(G)\le s\). In particular,
\[
\frac{|T\setminus T_{\rm fix}|}{|T|},
\frac{|C\setminus C_{\rm fix}|}{|C|}
\le 2\frac{\lambda^2}{d^2}
   +O\!\left(\frac{\lambda^4}{d^4}\right).
\]

For \(\lambda\le2\sqrt{d-1}\), this is
\[
1-\frac{8+o(1)}d
\]
identification for both types. The numerical assumption \(s\le1/10\) holds, for example, for this Ramanujan bound when \(d\ge39\); the finitely many smaller degrees are not covered by this particular argument.

---

# 5. Relation to the separator obstruction

Suppose deleting \(Z\), \(|Z|=z\), leaves components of order at most \(h\). Partition those components into two unions \(X,Y\) whose sizes differ by at most \(h\). Then
\[
|X|,|Y|\ge\frac{n-z-h}{2}
\]
and \(e(X,Y)=0\). Hence
\[
\eta(G)\ge
\left(\frac{n-z-h}{n+z+h}\right)^2.
\]
In particular, if \(z,h\le\epsilon n\), then
\[
\eta(G)\ge
\left(\frac{1-2\epsilon}{1+2\epsilon}\right)^2.
\]

Thus the separator obstruction forces the bipartite-hole parameter close to \(1\), while the sufficient result above requires it to be small.

The separator also explains why pairwise ambiguity alone is insufficient. Assume \(z+h<n/2\). Give the following reports:

- every edge internal to a component of \(G-Z\) is reported truthful in both directions;
- on an edge \(uz\) with \(u\notin Z\) and \(z\in Z\), let \(u\) report \(z\) corrupt and \(z\) report \(u\) truthful;
- reports internal to \(Z\) are arbitrary.

Then \(V\setminus Z\) is a feasible truthful set. For every component \(K\) of \(G-Z\),
\[
(V\setminus Z)\setminus K
\]
is also a feasible truthful set because
\[
n-z-|K|>n/2.
\]
Consequently, every vertex outside \(Z\) is non-identifiable, even if the actual corrupt set is only \(Z\). Yet any one alternative may differ from the actual world on only \(h\) vertices.

---

# 6. Strong spectral expansion is not necessary

There can be perfect information-theoretic detection even when the conventional spectral gap is arbitrarily poor.

Let \(H_m\) consist of two \(m\)-cliques \(L,R\), together with a perfect matching between corresponding vertices. It is \(d=m\)-regular on \(2m\) vertices, with adjacency matrix
\[
\begin{pmatrix}
J-I&I\\
I&J-I
\end{pmatrix}.
\]
Its spectrum is
\[
m,\quad m-2,\quad 0^{(m-1)},\quad (-2)^{(m-1)}.
\]
Thus
\[
\frac{\lambda_2(H_m)}d=1-\frac2m\longrightarrow1.
\]

Nevertheless, \(\mu(H_m)=0\). Indeed, if \(S\) meets both cliques, then every vertex outside \(S\) belongs to \(\partial S\). If \(S\) is contained in exactly one clique and is nonempty, then
\[
|\partial S|=m.
\]
In all cases,
\[
2|\partial S|+|S|\ge2m=n.
\]
By Theorem 2.1, no report pattern admits two distinct strict-majority feasible worlds. Hence every status is identifiable whenever a feasible world exists.

This example is dense (\(n=2d\)), so it does not settle the sparse \(n\gg d\) regime. It does show that no unrestricted necessary-and-sufficient criterion can depend only on the ordinary spectral ratio \(\lambda/d\); vertex-separator or bipartite-hole information is genuinely different.

---

# 7. What remains open

The arguments establish:

1. an exact vertex-boundary formula for the maximum distance between two feasible worlds;
2. a direct expansion parameter \(\eta(G)\) under which almost all truthful and corrupt vertices are certified;
3. the spectral implication
   \[
   \eta(G)\le(\lambda/d)^2;
   \]
4. an explicit demonstration that strong spectral expansion is not necessary.

They do **not** give a full characterization of the number of vertices fixed across an entire family of feasible worlds. A collection of many small alternative worlds can make almost every vertex ambiguous even though every pair is close. A sharp characterization therefore requires a multiway separator or separability parameter, not merely the two-world parameter \(\mu(G)\).

The supplied literature review indicates that Jin–Mossel–Ramnarayan introduced such a vertex-separability parameter for arbitrary graphs. I have not compared the precise conventions closely enough to claim that Theorem 2.1 is new rather than a parity-refined reformulation of part of that work. The present argument is also information-theoretic: finding all feasible assignments, or even one suitable assignment, may be computationally hard.