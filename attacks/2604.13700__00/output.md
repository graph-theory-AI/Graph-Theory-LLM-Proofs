```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact value remains undetermined; the quoted upper construction gives 3/22 <= L <= 7/8, and every vertex-transitive r-regular digraph satisfies c(D)=r.",
  "would_publish": false,
  "caveats": "No new general bound beyond the source abstract is proved, and the special-class results have not been checked for novelty."
}
```

# 1. Statement and conclusions

For a vertex \(v\) of a finite loopless simple digraph \(D\), let
\[
\lambda_D(v)
\]
denote the maximum number of directed cycles through \(v\) that are pairwise vertex-disjoint outside \(v\). Thus
\[
c(D)=\max_{v\in V(D)}\lambda_D(v),
\qquad
c_r=\min\{c(D):D\text{ is }r\text{-regular}\}.
\]

I do not determine
\[
L=\lim_{r\to\infty}\frac{c_r}{r}.
\]

I obtain the following rigorous partial conclusions.

1. The source abstract itself implies
   \[
   \boxed{\frac{3}{22}\le L\le \frac78}.
   \]
   Thus the catalog interval \([3/22,1]\) overlooks the quoted bound
   \(c_r\le 7\lceil r/8\rceil\).

2. Using blow-ups,
   \[
   \boxed{L=\inf_{r\ge1}\frac{c_r}{r}}.
   \]
   Consequently, any single \(d\)-regular example with
   \(c(D)/d<7/8\) would improve the asymptotic upper bound.

3. Every finite vertex-transitive \(r\)-regular digraph satisfies
   \[
   \boxed{\lambda_D(v)=r\quad\text{for every }v}.
   \]
   Hence no nontrivial upper-bound construction can be vertex-transitive.

4. Every balanced orientation of \(K_{2r,2r}\) satisfies
   \[
   \boxed{\lambda_D(v)=r\quad\text{for every }v}.
   \]

5. If \(T\) is a regular tournament of degree \(r\ge2\), then every vertex satisfies
   \[
   \boxed{\lambda_T(v)\ge
   \left\lceil\frac{2r+2}{3}\right\rceil}.
   \]
   This pointwise bound is sharp for infinitely many \(r\), although the sharp examples at one distinguished vertex do not give a corresponding upper bound on \(c(T)\).

Throughout, opposite arcs are allowed, but loops and parallel arcs are not. If the source uses multidigraphs, some special-class statements require modification.

---

# 2. Local Menger formulation

For \(v\in V(D)\), let
\[
O_v=N^+(v),\qquad I_v=N^-(v).
\]
Deleting \(v\), every directed cycle through \(v\) corresponds to a directed path from \(O_v\) to \(I_v\): if
\[
v\to x\leadsto y\to v
\]
is the cycle, then \(x\leadsto y\) is such a path. A common in- and out-neighbor represents a one-vertex path and hence a directed \(2\)-cycle.

Therefore directed vertex-Menger gives
\[
\lambda_D(v)
=
\min\bigl\{|S|:S\subseteq V(D)\setminus\{v\},
\ D-S\text{ has no directed cycle through }v\bigr\}.
\tag{2.1}
\]
I will call such an \(S\) a \(v\)-cycle transversal.

In particular,
\[
\lambda_D(v)\le |N^+(v)|=r.
\tag{2.2}
\]

This also gives a polynomial-time method to evaluate \(c(D)\): split every vertex \(u\ne v\) into \(u_{\rm in}\to u_{\rm out}\) with capacity \(1\), give the original arcs large capacity, connect a source to the out-neighbors of \(v\), and the in-neighbors of \(v\) to a sink. The maximum integral flow is \(\lambda_D(v)\).

---

# 3. Blow-ups and the numerical interval

## Proposition 3.1
If \(H\) is \(d\)-regular, then for every positive integer \(t\) there is a \(dt\)-regular digraph \(H^{(t)}\) satisfying
\[
c(H^{(t)})\le t\,c(H).
\]

### Proof

Replace every vertex \(x\in V(H)\) by an independent set
\[
V_x=\{(x,1),\dots,(x,t)\}.
\]
For every arc \(x\to y\) of \(H\), insert all \(t^2\) arcs from \(V_x\) to \(V_y\). Every new vertex has in- and out-degree \(dt\).

Fix \((v,i)\in V_v\), and let \(S_v\subseteq V(H)\setminus\{v\}\) be a \(v\)-cycle transversal of size \(\lambda_H(v)\). Delete
\[
\widehat S_v=\bigcup_{x\in S_v}V_x,
\]
which has size \(t\lambda_H(v)\).

If a cycle through \((v,i)\) avoided \(\widehat S_v\), its projection to \(H\) would be a closed directed walk based at \(v\) avoiding \(S_v\). Removing closed subwalks not containing \(v\) produces a directed cycle through \(v\) avoiding \(S_v\), a contradiction. Thus
\[
\lambda_{H^{(t)}}((v,i))\le t\lambda_H(v).
\]
Taking the maximum over the vertices proves the proposition. \(\square\)

## Corollary 3.2
Assuming the convergence established in the source,
\[
\boxed{L=\inf_{d\ge1}\frac{c_d}{d}}.
\]

### Proof

Let \(a_d=c_d/d\). Proposition 3.1 gives
\[
c_{td}\le t c_d,
\qquad\text{so}\qquad
a_{td}\le a_d.
\]
As \(t\to\infty\), the subsequence \(a_{td}\) converges to \(L\), hence
\[
L\le a_d
\]
for every \(d\). Therefore
\[
L\le \inf_d a_d.
\]
The reverse inequality follows immediately from \(\inf_d a_d\le a_r\) and \(a_r\to L\). \(\square\)

The quoted source bound
\[
c_r\le 7\left\lceil\frac r8\right\rceil
\]
therefore yields
\[
L\le \lim_{r\to\infty}
\frac{7\lceil r/8\rceil}{r}
=\frac78.
\]
Combined with the source lower bound,
\[
\boxed{\frac3{22}\le L\le\frac78}.
\tag{3.1}
\]

This does not resolve the limit, but it corrects the weaker interval stated in the catalog review.

---

# 4. Vertex-transitive digraphs have the full value

I use the following standard finite-product theorem.

## Scherk–Kemperman product lemma
Let \(A,B\) be finite subsets of a group \(G\). If some element of \(AB\) has a unique representation as \(ab\), with \(a\in A\) and \(b\in B\), then
\[
|AB|\ge |A|+|B|-1.
\tag{4.1}
\]

This is a proved classical product-set lemma, not a conjectural input.

## Lemma 4.1: Cayley digraphs

Let \(D=\operatorname{Cay}(G,Q)\) be the right Cayley digraph with arcs
\[
g\to gq,\qquad q\in Q,
\]
where \(1\notin Q\). Then
\[
\lambda_D(g)=|Q|
\qquad\text{for every }g\in G.
\]

### Proof

By translation it is enough to consider the identity \(1\). Let \(Z\) be a \(1\)-cycle transversal and suppose
\[
|Z|<|Q|.
\]
Let \(R\) be the set of vertices reachable from \(1\) in \(D-Z\).

We claim
\[
R\cap Q^{-1}=\varnothing.
\tag{4.2}
\]
Indeed, if \(q^{-1}\in R\), a shortest path from \(1\) to \(q^{-1}\), followed by the arc \(q^{-1}\to1\), gives a directed cycle through \(1\) avoiding \(Z\).

Put
\[
B=\{1\}\cup Q.
\]
The identity has a unique representation in \(RB\): the representation \(1=1\cdot1\). Any other representation would have the form
\[
1=rq,\qquad r\in R,\ q\in Q,
\]
and hence \(r=q^{-1}\), contrary to (4.2).

The product lemma now gives
\[
|RB|\ge |R|+|B|-1=|R|+|Q|.
\tag{4.3}
\]
On the other hand, reachability implies
\[
RB\setminus R\subseteq Z:
\]
if \(rq\notin Z\), then the arc \(r\to rq\) would make \(rq\) reachable. Hence
\[
|Z|\ge |RB|-|R|\ge |Q|,
\]
a contradiction. Thus every \(1\)-cycle transversal has size at least \(|Q|\). The reverse inequality follows by deleting \(N^+(1)\). \(\square\)

## Theorem 4.2
If \(D\) is a finite vertex-transitive \(r\)-regular digraph, then
\[
\lambda_D(v)=r
\qquad\text{for every }v\in V(D).
\]

### Proof

Let a finite group \(G\le\operatorname{Aut}(D)\) act transitively on \(V(D)\). Fix \(v\), and let
\[
H=\{g\in G:g(v)=v\}
\]
be its stabilizer. Define
\[
Q=\{g\in G:v\to g(v)\text{ is an arc of }D\}.
\]
For each out-neighbor \(w\) of \(v\), exactly \(|H|\) elements of \(G\) send \(v\) to \(w\). Consequently
\[
|Q|=r|H|.
\]

Consider the Cayley digraph \(\operatorname{Cay}(G,Q)\) and the projection
\[
\pi:G\to V(D),\qquad \pi(g)=g(v).
\]
Every Cayley arc \(g\to gq\) projects to the arc
\[
g(v)\to gq(v)
\]
of \(D\).

Let \(Z\) be a \(v\)-cycle transversal in \(D\). Then
\[
\widetilde Z=\pi^{-1}(Z)
\]
has size \(|H||Z|\). Moreover, it is a cycle transversal through the identity in \(\operatorname{Cay}(G,Q)\): a Cayley cycle avoiding \(\widetilde Z\) would project to a closed directed walk through \(v\) avoiding \(Z\), and such a walk contains a directed cycle through \(v\).

Lemma 4.1 therefore gives
\[
|H||Z|\ge |Q|=r|H|,
\]
and hence \(|Z|\ge r\). Together with (2.2), this proves
\[
\lambda_D(v)=r.
\]
\(\square\)

Thus every graph witnessing \(c_r<r\) is necessarily asymmetric enough not to be vertex-transitive.

---

# 5. Balanced orientations of complete bipartite graphs

A bipartite tournament is an orientation of a complete bipartite graph.

## Theorem 5.1
Let \(D\) be an orientation of \(K_{2r,2r}\) in which every vertex has in- and out-degree \(r\). Then
\[
\lambda_D(v)=r
\qquad\text{for every }v.
\]

### Proof

Let the bipartition be \(A\cup B\), and fix \(v\in A\). Write
\[
O=N^+(v)\subseteq B,\qquad I=N^-(v)\subseteq B.
\]
Both sets have size \(r\) and partition \(B\).

Suppose that \(S\) is a \(v\)-cycle transversal of size less than \(r\). Set
\[
S_A=S\cap A,\qquad S_B=S\cap B,
\]
and write
\[
a=|S_A|,\qquad b=|S_B|.
\]

In \(D-v-S\), let \(R\) be the set reachable from \(O\setminus S_B\). Since \(S\) hits all cycles through \(v\), no vertex of \(I\setminus S_B\) is reachable. Hence
\[
R\cap B=O\setminus S_B.
\]
Put
\[
X=R\cap A,\qquad Y=R\cap B,\qquad x=|X|,\ y=|Y|.
\]

Every \(y_0\in Y\) has all its \(r\) out-neighbors in \(X\cup S_A\): it does not point to \(v\), and an arc from \(Y\) to an undeleted vertex outside \(R\) would contradict the definition of \(R\). Hence
\[
x+a\ge r,
\qquad\text{so}\qquad
x\ge r-a.
\tag{5.1}
\]

Because \(b<r\), there is a vertex \(z\in I\setminus S_B\). Closure of \(R\) implies
\[
z\to x_0
\qquad\text{for every }x_0\in X.
\]
Also \(z\to v\). Since \(z\) has out-degree \(r\),
\[
x+1\le r,
\qquad\text{so}\qquad
x\le r-1.
\tag{5.2}
\]
In particular \(a\ge1\).

Every \(x_0\in X\) has all its out-neighbors in \(Y\cup S_B\), so
\[
e(X,Y)\ge x(r-b).
\tag{5.3}
\]
Similarly,
\[
e(Y,X)\ge y(r-a).
\tag{5.4}
\]
Every pair in \(X\times Y\) supports exactly one directed arc, and therefore
\[
xy=e(X,Y)+e(Y,X)
 \ge x(r-b)+y(r-a).
\tag{5.5}
\]

Let
\[
p=x-(r-a)\ge0.
\]
By (5.2),
\[
p\le a-1.
\]
If
\[
o=|S_B\cap O|,\qquad i=|S_B\cap I|,
\]
then \(b=o+i\) and
\[
y=r-o=(r-b)+i.
\]
Thus, with \(q=i\le b\), inequality (5.5) becomes
\[
pq\ge (r-a)(r-b).
\tag{5.6}
\]
But
\[
pq\le(a-1)b,
\]
while \(a+b<r\) gives
\[
r-a>b,\qquad r-b>a,
\]
and hence
\[
(r-a)(r-b)>ab\ge(a-1)b.
\]
This contradicts (5.6).

Therefore no \(v\)-cycle transversal has size below \(r\), and equality follows from the trivial upper bound. The case \(v\in B\) is symmetric. \(\square\)

---

# 6. Regular tournaments

Let \(T\) be a tournament and \(v\in V(T)\). Put
\[
O=N^+(v),\qquad I=N^-(v).
\]
Define a bipartite graph \(B_v\) with parts \(O,I\), putting an edge \(oi\) precisely when
\[
o\to i
\]
in \(T\).

## Lemma 6.1
For every tournament \(T\),
\[
\lambda_T(v)=\nu(B_v),
\]
where \(\nu\) denotes maximum matching size.

### Proof

A matching
\[
o_1i_1,\dots,o_ki_k
\]
gives openly disjoint directed triangles
\[
v\to o_j\to i_j\to v.
\]
Thus \(\lambda_T(v)\ge\nu(B_v)\).

Conversely, let \(S\) be a vertex cover of \(B_v\). In \(T-v-S\), every remaining arc between \(I\) and \(O\) is directed from \(I\) to \(O\). Hence there is no path from \(O\setminus S\) to \(I\setminus S\): any such path would have a first arc entering \(I\), necessarily directed from \(O\) to \(I\). Thus \(S\) is a \(v\)-cycle transversal. König's theorem now gives
\[
\lambda_T(v)\le \tau(B_v)=\nu(B_v).
\]
\(\square\)

In particular, in a tournament all cycles needed for an optimal openly disjoint family may be chosen to be triangles.

## Theorem 6.2
If \(T\) is a regular tournament of degree \(r\ge2\), then every vertex \(v\) satisfies
\[
\lambda_T(v)\ge
\left\lceil\frac{2r+2}{3}\right\rceil.
\]

### Proof

The tournament has \(2r+1\) vertices, and
\[
|O|=|I|=r.
\]
Let \(S=A\cup B\) be a minimum vertex cover of \(B_v\), where
\[
A\subseteq O,\qquad B\subseteq I,
\]
and put
\[
a=|A|,\qquad b=|B|.
\]
If \(a+b=r\), the assertion follows. Suppose \(a+b<r\), and set
\[
O'=O\setminus A,\quad I'=I\setminus B,\quad
x=|O'|=r-a,\quad y=|I'|=r-b.
\]
Since \(S\) covers all edges of \(B_v\), every arc between \(I'\) and \(O'\) is directed
\[
I'\to O'.
\]

Sum the out-degrees of the vertices in \(I'\). They send all \(xy\) arcs to \(O'\), all \(y\) arcs to \(v\), and there are \(y(y-1)/2\) internal arcs in \(T[I']\). Hence
\[
ry\ge xy+y+\frac{y(y-1)}2.
\]
After division and substitution,
\[
2a+b\ge r+1.
\tag{6.1}
\]

Similarly, summing the indegrees of the vertices in \(O'\) gives
\[
rx\ge xy+x+\frac{x(x-1)}2,
\]
and therefore
\[
a+2b\ge r+1.
\tag{6.2}
\]
Adding (6.1) and (6.2),
\[
3(a+b)\ge2r+2.
\]
By Lemma 6.1,
\[
\lambda_T(v)=a+b\ge
\left\lceil\frac{2r+2}{3}\right\rceil.
\]
\(\square\)

## Pointwise sharpness

For every \(k\ge1\), put
\[
r=3k-1.
\]
There is a regular tournament \(T\) of degree \(r\) with a vertex \(v\) satisfying
\[
\lambda_T(v)=2k=\frac{2r+2}{3}.
\]

Take disjoint sets
\[
|X|=|Y|=2k-1,\qquad |Z|=2k+1.
\]
Put regular tournaments on each of \(X,Y,Z\), and choose \(v\in Z\). Orient the cross-arcs by
\[
Y\to X,\qquad
X\to Z\setminus\{v\},\qquad
Z\setminus\{v\}\to Y,
\]
together with
\[
Y\to v,\qquad v\to X.
\]
The tournament inside \(Z\) is left unchanged.

Every \(x\in X\) has out-degree
\[
(k-1)+2k=3k-1.
\]
Every \(y\in Y\) has out-degree
\[
(k-1)+(2k-1)+1=3k-1.
\]
Every \(z\in Z\setminus\{v\}\) has out-degree
\[
k+(2k-1)=3k-1,
\]
and \(v\) has out-degree
\[
k+(2k-1)=3k-1.
\]
Thus \(T\) is regular.

At \(v\), deleting \(Z\setminus\{v\}\), of size \(2k\), leaves all remaining in-neighbors in \(Y\), all remaining out-neighbors in \(X\), and all arcs directed \(Y\to X\). Hence
\[
\lambda_T(v)\le2k.
\]
Theorem 6.2 gives equality.

This only proves sharpness for a prescribed vertex. Other vertices of this tournament may have larger local packing number, so this is not an upper construction for \(c_r\).

---

# 7. Exact finite search formulation

For a fixed number \(n\) of vertices, the existence of an \(r\)-regular digraph with \(c(D)\le k\) has a direct \(0\)-\(1\) linear formulation.

Use variables \(x_{ij}\) for arcs \(i\to j\), with
\[
\sum_{j\ne i}x_{ij}=r,\qquad
\sum_{j\ne i}x_{ji}=r.
\]

For every possible root \(v\), introduce binary variables

- \(z_{vu}=1\) if \(u\) lies in a chosen \(v\)-cycle transversal;
- \(p_{vu}=1\) if \(u\) lies in a set \(R_v\) containing \(v\).

Impose
\[
z_{vv}=0,\qquad p_{vv}=1,\qquad
p_{vu}+z_{vu}\le1,\qquad
\sum_u z_{vu}\le k.
\]
The constraints
\[
x_{ij}+p_{vi}-p_{vj}-z_{vj}\le1
\tag{7.1}
\]
for all \(i\ne j\) forbid arcs from \(R_v\) to
\(V(D)\setminus(R_v\cup Z_v)\). Finally,
\[
x_{iv}+p_{vi}\le1
\qquad(i\ne v)
\tag{7.2}
\]
forbids arcs from \(R_v\setminus\{v\}\) back to \(v\).

These constraints are exact:

- If they hold, every walk from \(v\) in \(D-Z_v\) stays in \(R_v\), and (7.2) prevents it from returning to \(v\).
- Conversely, if \(Z_v\) meets all cycles through \(v\), take \(R_v\) to be the set reachable from \(v\) in \(D-Z_v\).

Thus feasibility is equivalent to the existence of an \(r\)-regular \(n\)-vertex digraph with \(c(D)\le k\). Any candidate can then be independently certified by the node-splitting max-flow computation from Section 2.

A feasible instance with
\[
\frac{k}{r}<\frac78
\]
would, by Proposition 3.1, improve the current asymptotic upper bound. A negative result for one fixed \(n\), however, says nothing about larger orders.

---

# 8. Remaining gap

The exact value of \(L\) is still open. The special classes above show that an extremal family cannot be obtained from the most symmetric regular constructions, Cayley digraphs, or balanced complete bipartite orientations. They do not improve the universal lower bound \(3/22\), because arbitrary regular digraphs can be highly asymmetric.

The present rigorous numerical conclusion is therefore only
\[
\boxed{\frac3{22}\le L\le\frac78}.
\]
Determining \(L\) requires either:

- a stronger universal lower bound on \(\max_v\lambda_D(v)\), or
- a finite regular construction with \(c(D)/r<7/8\), which would propagate asymptotically by blow-up.