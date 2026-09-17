```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I do not determine L, but prove c(T) >= ceil(3(r+1)/4) for regular tournaments of degree r >= 3, and c(T)=r for r<=8.",
  "would_publish": false,
  "caveats": "No improvement of the universal interval [3/22,7/8]; novelty of the tournament results is unverified, and the source bounds are used as supplied."
}
```

## 1. Statement and results

Digraphs below are finite, without loops or parallel arcs. Write
\[
\lambda_D(v)=\max\{|\mathcal C|:\mathcal C
\text{ is a family of directed cycles openly disjoint at }v\}.
\]
Thus
\[
c(D)=\max_v\lambda_D(v),\qquad
c_r=\min_{D\text{ \(r\)-regular}}c(D).
\]

I do **not** determine
\[
L=\lim_{r\to\infty}\frac{c_r}{r}.
\]

The additional partial result obtained here concerns regular tournaments.

### Theorem A
If \(T\) is a regular tournament of degree \(r\ge3\), then
\[
\boxed{c(T)\ge \left\lceil\frac{3(r+1)}4\right\rceil.}
\tag{1.1}
\]

More precisely, if some vertex \(v\) satisfies \(\lambda_T(v)=k<r\), then
\[
\boxed{c(T)\ge
\left\lceil\frac{3r-2k+3}{2}\right\rceil.}
\tag{1.2}
\]

### Theorem B
Every regular tournament of degree \(1\le r\le8\) satisfies
\[
\boxed{c(T)=r.}
\tag{1.3}
\]
This asserts the existence of a vertex with the full packing number, not that every vertex has it.

I rechecked the cycle-transversal/blow-up reduction and the tournament matching reduction from the previous attempt; proofs are included below. The other special-class claims in that attempt are not used. No claim of literature novelty is made for Theorems A or B.

For the original problem, the estimates stated in the supplied abstract give
\[
\boxed{\frac3{22}\le L\le\frac78,}
\tag{1.4}
\]
rather than merely the catalog review's upper bound \(1\). The tournament results do not improve this universal interval.

---

## 2. Exact reductions for the original problem

### 2.1. Local cycle transversals

Vertex-Menger, applied to paths from \(N^+(v)\) to \(N^-(v)\) in \(D-v\), gives
\[
\lambda_D(v)=
\min\bigl\{|S|:S\subseteq V(D)\setminus\{v\},
\ D-S\text{ contains no directed cycle through }v\bigr\}.
\tag{2.1}
\]
A common in- and out-neighbor is allowed as a one-vertex path, corresponding to a directed \(2\)-cycle.

In an \(r\)-regular digraph,
\[
\lambda_D(v)\le r.
\tag{2.2}
\]

### 2.2. Uniform blow-ups preserve the ratio exactly

For a digraph \(H\), let \(H^{(t)}\) be its uniform independent-set blow-up: replace each vertex \(x\) by \(t\) vertices \(V_x\), and replace each arc \(x\to y\) by all arcs from \(V_x\) to \(V_y\).

For every \(u\in V_v\),
\[
\boxed{\lambda_{H^{(t)}}(u)=t\lambda_H(v).}
\tag{2.3}
\]

For the lower bound, take an optimal openly disjoint family at \(v\), and make \(t\) copies of each cycle, using different clones at every vertex other than the fixed root \(u\).

For the upper bound, choose a minimum \(v\)-cycle transversal \(S\) in \(H\). Deleting
\[
\bigcup_{x\in S}V_x
\]
kills every cycle through \(u\): otherwise its projection would be a nontrivial closed directed walk through \(v\) avoiding \(S\), which contains a directed cycle through \(v\). Equation (2.1) proves the upper bound.

Consequently, if \(H\) is \(d\)-regular, then
\[
H^{(t)}\text{ is \(td\)-regular},\qquad
c(H^{(t)})=t\,c(H).
\tag{2.4}
\]

### 2.3. An elementary proof of the infimum formula

Every \(q\)-regular digraph has a spanning \(p\)-regular subdigraph for \(0\le p\le q\). Indeed, its bipartite incidence graph is \(q\)-regular and decomposes into perfect matchings by Hall's theorem.

Fix \(d\), take a \(d\)-regular \(H\) with \(c(H)=c_d\), and put \(t=\lceil r/d\rceil\). A spanning \(r\)-regular subdigraph of \(H^{(t)}\) gives
\[
c_r\le \left\lceil\frac rd\right\rceil c_d.
\tag{2.5}
\]
Thus, with \(\alpha=\inf_d c_d/d\),
\[
\limsup_{r\to\infty}\frac{c_r}{r}\le \frac{c_d}{d}
\quad\text{for every }d,
\qquad
\liminf_{r\to\infty}\frac{c_r}{r}\ge\alpha.
\]
Hence
\[
\boxed{L=\inf_{d\ge1}\frac{c_d}{d}.}
\tag{2.6}
\]

This reduction does not produce an improved example. Taking the supplied estimates
\[
c_r\ge\left\lceil\frac{3r}{22}\right\rceil,
\qquad
c_r\le7\left\lceil\frac r8\right\rceil
\]
as inputs gives (1.4).

---

## 3. The tournament matching formulation

Fix a vertex \(v\) of a tournament \(T\). Put
\[
O=N^+(v),\qquad I=N^-(v),
\]
and form the bipartite graph \(B_v\) with parts \(O,I\), where \(oi\) is an edge exactly when \(o\to i\) in \(T\).

Then
\[
\boxed{\lambda_T(v)=\nu(B_v).}
\tag{3.1}
\]

A matching gives openly disjoint triangles \(v\to o\to i\to v\). Conversely, every directed cycle through \(v\) contains such a triangle on a subset of its vertices: along the cycle minus \(v\), take a transition from \(O\) to \(I\). Applying this separately to openly disjoint cycles gives a matching.

Now suppose that \(T\) is regular of degree \(r\) and
\[
k=\lambda_T(v)<r.
\]
By König's theorem, \(B_v\) has a vertex cover \(A\cup B\) of size \(k\), with
\[
A\subseteq O,\qquad B\subseteq I.
\]
Set
\[
\begin{aligned}
&a=|A|,\quad b=|B|,\quad a+b=k,\\
&X=O\setminus A,\quad Y=I\setminus B,\quad S=A\cup B,\\
&x=|X|=r-a,\qquad y=|Y|=r-b.
\end{aligned}
\tag{3.2}
\]
The cover property gives
\[
Y\to X,\qquad Y\to v\to X.
\tag{3.3}
\]

Summing the out-degrees of \(Y\), and then the indegrees of \(X\), gives
\[
ry\ge xy+y+\frac{y(y-1)}2,
\qquad
rx\ge xy+x+\frac{x(x-1)}2.
\]
Equivalently,
\[
\boxed{2a+b\ge r+1,\qquad a+2b\ge r+1.}
\tag{3.4}
\]
In particular, writing \(d=r-k\),
\[
\boxed{a,b\ge d+1.}
\tag{3.5}
\]

Adding (3.4) also recovers the pointwise bound from the previous attempt:
\[
\lambda_T(v)\ge
\left\lceil\frac{2r+2}{3}\right\rceil
\qquad(r\ge2).
\tag{3.6}
\]
The improvement below comes from finding a better root inside \(X\) or \(Y\).

---

## 4. Two auxiliary matching lemmas

### Lemma 4.1: a minimum-degree vertex

Let \(R\) be a tournament of minimum out-degree \(\delta\ge1\), and let \(w\) have out-degree \(\delta\). Then
\[
\lambda_R(w)\ge\left\lceil\frac{\delta+1}{2}\right\rceil.
\tag{4.1}
\]
The analogous assertion holds for a vertex of minimum indegree.

#### Proof

Use the bipartite triangle graph at \(w\), whose out-neighbor part has size \(\delta\). Consider a vertex cover \(P\cup Q\).

If \(P\) contains all out-neighbors, the cover has size at least \(\delta\). Otherwise let
\[
Z=N^+(w)\setminus P,\qquad z=|Z|>0.
\]
There are no arcs from \(Z\) to \(N^-(w)\setminus Q\). Since every vertex of \(Z\) has out-degree at least \(\delta\),
\[
\delta z
\le \frac{z(z-1)}2+z(\delta-z)+z|Q|.
\]
Therefore
\[
|Q|\ge\frac{z+1}{2},
\]
and the cover has size at least
\[
(\delta-z)+\frac{z+1}{2}
\ge\frac{\delta+1}{2}.
\]
Apply König's theorem and (3.1). Reversing all arcs proves the indegree version. \(\square\)

### Lemma 4.2: external matching

Use the partition in (3.2), and put
\[
W=X\cup\{v\},\qquad q=|W|=x+1,
\qquad
\eta=b-\frac{x+1}{2}.
\tag{4.2}
\]
By (3.4), \(\eta\ge0\).

For any \(U\subseteq S\), let \(H\) be the bipartite graph from \(W\) to \(U\), with edges corresponding to arcs \(w\to u\) of \(T\). If \(p=|U|\), then
\[
\boxed{\nu(H)\ge
\min\{q,\lceil p-\eta\rceil\}.}
\tag{4.3}
\]

#### Proof

Consider a vertex cover of \(H\). Let \(W_0,U_0\) be the uncovered vertices, of sizes \(z,u\), respectively. If one is empty, the desired estimate follows immediately.

Otherwise
\[
U_0\to W_0.
\tag{4.4}
\]
There are three cases.

* If \(v\notin W_0\), then \(W_0\subseteq X\). Summing its indegrees, including all arcs from \(Y\), from \(v\), and from \(U_0\), gives
  \[
  2u+z\le2b-1.
  \tag{4.5}
  \]

* If \(v\in W_0\) and \(z\ge2\), apply the same count to \(W_0\setminus\{v\}\):
  \[
  2u+z\le2b.
  \tag{4.6}
  \]

* If \(W_0=\{v\}\), then \(U_0\subseteq B\), so \(u\le b\).

In all cases,
\[
u+z\le b+\frac q2=q+\eta.
\tag{4.7}
\]
For the singleton case, use \(q\ge2\); this follows already from \(k<r\) and (3.5).

The cover therefore has size
\[
p+q-u-z\ge p-\eta.
\]
Together with the cases in which one uncovered part is empty, König's theorem gives (4.3). \(\square\)

The two inequalities (4.5)–(4.6), not just their consequence (4.3), will also be useful for degree eight.

---

## 5. Proof of Theorem A

We prove the stronger tradeoff (1.2).

Take a vertex \(v\) with \(\lambda_T(v)=k<r\), and the partition from Section 3. Reversing the tournament if necessary, assume
\[
a\le b.
\tag{5.1}
\]
Reversal preserves all local packing numbers.

Choose \(w\in Y\) of minimum indegree in \(T[Y]\), and denote that indegree by \(\delta\).

Every vertex of \(Y\) sends arcs to all \(x+1\) vertices of \(X\cup\{v\}\), so its out-degree inside \(Y\) is at most \(a-1\). Consequently,
\[
\boxed{r-k\le\delta\le\frac{y-1}{2}
=\frac{r-b-1}{2}.}
\tag{5.2}
\]

By Lemma 4.1, there are at least
\[
h=\left\lceil\frac{\delta+1}{2}\right\rceil
\tag{5.3}
\]
openly disjoint cycles at \(w\) lying entirely in \(Y\).

All inneighbors of \(w\) outside \(Y\) lie in \(S\). Let
\[
U=N^-(w)\cap S.
\]
Regularity gives
\[
p=|U|=r-\delta.
\tag{5.4}
\]
Every vertex of \(W=X\cup\{v\}\) is an out-neighbor of \(w\). A matching from \(W\) to \(U\) therefore supplies openly disjoint triangles through \(w\), all disjoint from the internal cycles outside their common root.

Lemma 4.2 gives
\[
\lambda_T(w)\ge
h+\min\{q,\lceil p-\eta\rceil\},
\tag{5.5}
\]
where
\[
q=r-a+1,\qquad
\eta=b-\frac{r-a+1}{2}.
\]

We now bound both alternatives in (5.5).

First, using \(\delta\ge r-k\) and \(2a\le k\),
\[
\begin{aligned}
q+h
&\ge r-a+1+\frac{r-k+1}{2}\\
&=\frac{3r-2a-k+3}{2}\\
&\ge\frac{3r-2k+3}{2}.
\end{aligned}
\tag{5.6}
\]

Second, using the upper bound on \(\delta\) in (5.2),
\[
\begin{aligned}
p-\eta+h
&\ge r-\eta-\frac{\delta}{2}+\frac12\\
&\ge
r-\left(b-\frac{r-a+1}{2}\right)
-\frac{r-b-1}{4}+\frac12\\
&=\frac{5r-2a-3b+5}{4}\\
&=\frac{5r-3k+a+5}{4}.
\end{aligned}
\]
By (3.5), \(a\ge r-k+1\), so
\[
p-\eta+h\ge\frac{3r-2k+3}{2}.
\tag{5.7}
\]

Equations (5.5)–(5.7) prove
\[
c(T)\ge
\left\lceil\frac{3r-2k+3}{2}\right\rceil,
\]
which is (1.2).

Finally, if \(c(T)<r\), choose \(v\) with \(k=c(T)\). Then
\[
c(T)\ge\frac{3r-2c(T)+3}{2},
\]
and hence
\[
4c(T)\ge3r+3.
\]
If \(c(T)=r\), the same claimed lower bound holds for \(r\ge3\). This proves Theorem A. \(\square\)

In particular, Theorem A and the elementary cases \(r=1,2\) give
\[
c(T)=r\qquad(1\le r\le6).
\tag{5.8}
\]

---

## 6. The full value in degrees seven and eight

We now prove the remaining part of Theorem B.

Let \(r\in\{7,8\}\), and suppose for a contradiction that \(c(T)<r\). Theorem A implies
\[
c(T)=r-1.
\]
Choose \(v\) attaining this value and a corresponding cover as in Section 3. After reversal, assume \(a\le b\). Here
\[
k=r-1,\qquad a,b\ge2,
\]
so
\[
a\in\{2,3\}.
\tag{6.1}
\]

### Case 1: \(a=2\)

Now \(y=3\). Every vertex of \(Y\) has internal out-degree at most \(a-1=1\), so \(T[Y]\) is a directed triangle. Moreover, with
\[
W=X\cup\{v\},
\]
we have
\[
|W|=|S|=r-1,\qquad
Y\to W,\qquad S\to Y.
\tag{6.2}
\]
The last domination follows because each vertex of \(Y\) already has \(r-1\) out-neighbors in \(W\) and one inside \(Y\).

I claim that the bipartite graph of arcs from \(W\) to \(S\) has a perfect matching. Otherwise a vertex cover of size at most \(r-2\) leaves nonempty sets \(W_0,S_0\), of sizes \(z,u\), with
\[
u+z\ge r,\qquad S_0\to W_0.
\]
Degree sums, using the three vertices of \(Y\), give
\[
2z+u\le2r-5,\qquad z+2u\le2r-5.
\]
Thus
\[
3(u+z)\le4r-10<3r
\]
for \(r=7,8\), a contradiction.

A perfect matching provides \(r-1\) external triangles through any fixed vertex of \(Y\), and the triangle \(T[Y]\) supplies one more. Hence \(c(T)=r\), a contradiction.

### Case 2: \(a=3\)

Here
\[
|Y|=4,\qquad |W|=r-2,\qquad |S|=r-1,
\qquad b=r-4.
\tag{6.3}
\]
Every vertex of \(T[Y]\) has out-degree at most \(2\). Its score multiset is consequently one of
\[
(2,2,2,0),\qquad (2,2,1,1).
\]

In either case, the four vertices can be named \(w,h,z,t\) so that
\[
w\to h\to z\to w,\qquad w\to t,
\tag{6.4}
\]
and
\[
d^+_{T[Y]}(w)=2,\qquad d^+_{T[Y]}(t)\le1.
\tag{6.5}
\]

For completeness:

* In the first score pattern, the three vertices of out-degree \(2\) form a directed triangle, and \(t\) is the sink.
* In the second, name the two out-degree-\(2\) vertices \(w,h\) so that \(w\to h\). The vertex \(h\) dominates both low-degree vertices. One of them, \(z\), dominates \(w\), and the other is \(t\).

Since \(w\) already has \(r-2\) out-neighbors in \(W\) and two in \(Y\),
\[
S\to w.
\tag{6.6}
\]
Also, \(t\) has at least one out-neighbor in \(S\), because
\[
d^+(t)=r,\qquad
|W|+d^+_{T[Y]}(t)\le r-1.
\tag{6.7}
\]

Let \(H\) be the bipartite graph of arcs from \(W\) to \(S\). If we can choose
\[
s\in N^+(t)\cap S
\]
so that \(H-s\) has a perfect matching, then we obtain \(r\) openly disjoint triangles at \(w\):

1. \(w\to h\to z\to w\);
2. \(w\to t\to s\to w\);
3. the \(r-2\) triangles supplied by that matching.

It remains to find such an \(s\).

#### Degree seven

Here \(|W|=5\), \(|S|=6\), and \(\eta=1/2\). For any \(s\in S\), Lemma 4.2 applied to \(U=S\setminus\{s\}\) gives
\[
\nu(H-s)\ge
\min\{5,\lceil5-\tfrac12\rceil\}=5.
\]
Thus any out-neighbor of \(t\) in \(S\) works.

#### Degree eight

Here \(|W|=6\), \(|S|=7\), \(b=4\), and \(\eta=1\). Lemma 4.2 first gives
\[
\nu(H)=6.
\tag{6.8}
\]

We need the following consequence of the proof of that lemma:

> If \(H-s\) has no perfect matching, there is a vertex  
> \(s_0\in S\setminus\{s\}\) with \(s_0\to W\).

Indeed, choose a vertex cover of \(H-s\) of size \(5\). Its uncovered sets \(U_0,W_0\) have sizes \(u,z\) satisfying
\[
u+z=7.
\]
If \(v\notin W_0\), inequality (4.5), together with \(z\le5\), gives \(u+z\le6\). If \(W_0=\{v\}\), then \(u+z\le5\). Thus \(v\in W_0\) and \(z\ge2\), and (4.6) yields
\[
2u+z\le8.
\]
Consequently \(u=1,z=6\), so the sole vertex of \(U_0\) dominates all of \(W\).

By (6.8), at most one vertex \(s_0\in S\) can dominate \(W\).

* If there is no such vertex, every deletion \(H-s\) has a perfect matching, and any \(s\in N^+(t)\cap S\) works.
* Suppose such an \(s_0\) exists. Every vertex of \(Y\) of internal out-degree \(2\) is dominated by all of \(S\), by the same degree calculation as (6.6). There are at least two such vertices. Thus \(s_0\) has its six out-neighbors in \(W\), plus at least two in \(Y\).

  Three high-degree vertices would give out-degree at least \(9\), impossible. Hence the score pattern is \((2,2,1,1)\), and the two high-degree vertices exhaust the remaining two out-neighbors of \(s_0\). In particular,
  \[
  t\to s_0.
  \]
  Every size-six matching in \(H\) avoids \(s_0\), so \(H-s_0\) has a perfect matching.

Again we obtain \(r\) openly disjoint triangles at \(w\), a contradiction.

Both cases are exhausted, proving Theorem B. \(\square\)

---

## 7. What this does—and does not—say about \(L\)

The tournament bound is stronger than the pointwise \(2/3\)-bound in the earlier attempt because it exploits a deficient vertex to find a better vertex elsewhere. The tradeoff
\[
\lambda_T(v)=k<r
\quad\Longrightarrow\quad
c(T)\ge\left\lceil\frac{3r-2k+3}{2}\right\rceil
\]
is the central additional conclusion.

Uniform blow-ups preserve \(c(D)/r\) exactly. Therefore uniform blow-ups of regular tournaments also have ratio at least \(3/4\); such constructions cannot produce a ratio below \(3/4\). This is a restriction on one natural construction class, not a bound on arbitrary regular digraphs.

The unresolved gap is substantive:

* No \(r\)-regular example with \(c(D)/r<7/8\) is constructed here.
* No universal lower bound better than the supplied \(3/22\) is proved.
* The tournament argument relies on every pair of distinct vertices having exactly one directed arc between them. Its degree counts and triangle matching formulation do not extend to arbitrary regular digraphs.

Thus the rigorous conclusion for the original limit remains
\[
\boxed{\frac3{22}\le L\le\frac78,}
\]
with its exact value undetermined.