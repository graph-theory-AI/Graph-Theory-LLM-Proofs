```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A completion argument proves the conjecture for a concrete forbidden-missing-subgraph class and gives an additive bound controlled by a vertex cover of the unsafe missing pairs.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved, and novelty of these structural partial results is not claimed."
}
```

# A completion-based partial result

Throughout, graphs are finite and nonempty. An oriented graph has no loops or antiparallel pairs.

Write
\[
N_1(v)=\{u:v\to u\},\qquad
N_2(v)=\{z:\operatorname{dist}(v,z)=2\},
\]
and \(d_i(v)=|N_i(v)|\). In particular, \(N_1(v)\) and \(N_2(v)\) are disjoint.

I obtain the following two partial results:

1. **A special case:** Seymour’s conjecture holds whenever the graph of missing pairs contains no induced \(2K_2\), \(P_4\), or \(C_4\).
2. **An additive bound for arbitrary oriented graphs:** certain missing pairs can be identified as *unsafe*. If their graph has a vertex cover of size \(k\), some vertex satisfies
   \[
   d_2(v)\ge d_1(v)-k.
   \]
   In fact, the proof gives a stronger, localized error term.

Both results hold with arbitrary positive vertex weights. The argument below is self-contained; I do not claim novelty.

## 1. Safe directions and the main theorem

A **missing pair** is an unordered pair \(\{a,b\}\) with neither \(a\to b\) nor \(b\to a\).

For a missing pair, call the proposed direction \(a\to b\) **safe** if
\[
x\to a\text{ in }D
\quad\Longrightarrow\quad
b\in N_1(x)\cup N_2(x)
\qquad\text{for every }x\in V(D).
\tag{1}
\]
Thus adding this arc cannot give an original inneighbour of \(a\) a genuinely new vertex reachable within two steps.

A missing pair is **unsafe** if neither direction is safe. Let \(H_{\mathrm{bad}}(D)\) be the undirected graph whose edges are the unsafe missing pairs.

For positive vertex weights \(w\), put
\[
w(S)=\sum_{x\in S}w(x),
\qquad
R(v)=V(D)\setminus\bigl(\{v\}\cup N_1(v)\cup N_2(v)\bigr).
\]

### Theorem 1
Let \(C\) be any vertex cover of \(H_{\mathrm{bad}}(D)\). Then there is a vertex \(v\) such that
\[
\boxed{\quad
w(N_2(v))+w(C\cap R(v))\ \ge\ w(N_1(v)).
\quad}
\tag{2}
\]

Consequently, writing
\[
\tau_w(H_{\mathrm{bad}})=
\min\{w(C):C\text{ is a vertex cover of }H_{\mathrm{bad}}\},
\]
some vertex satisfies
\[
w(N_2(v))\ge w(N_1(v))-\tau_w(H_{\mathrm{bad}}).
\tag{3}
\]

In particular, if every missing pair has a safe direction, then \(D\) satisfies the weighted second-neighbourhood inequality.

The proof uses the following tournament lemma.

## 2. A weighted tournament lemma

### Lemma 2
Every positively vertex-weighted tournament \(T\) has a vertex \(f\) satisfying
\[
w(N_2^T(f))\ge w(N_1^T(f)).
\tag{4}
\]

More specifically, this holds for the last vertex of any order
\[
L=(v_1,\ldots,v_n)
\]
having the following **right-feedback property**: for all \(p\le q\),
\[
w\!\left(N_T^-(v_q)\cap\{v_p,\ldots,v_{q-1}\}\right)
\ge
w\!\left(N_T^+(v_q)\cap\{v_p,\ldots,v_{q-1}\}\right).
\tag{5}
\]

#### Existence of such an order

Choose an order maximizing
\[
\Phi(L)=
\sum_{\substack{i<j\\v_i\to v_j}}
w(v_i)w(v_j).
\]
Moving \(v_q\) to immediately before \(v_p\) changes this score by
\[
w(v_q)\left(
w(N_T^+(v_q)\cap\{v_p,\ldots,v_{q-1}\})
-
w(N_T^-(v_q)\cap\{v_p,\ldots,v_{q-1}\})
\right).
\]
Maximality and \(w(v_q)>0\) imply (5).

#### Proof of the inequality

Let \(f=v_n\), and partition the other vertices into
\[
A=N_1^T(f),\qquad B=N_2^T(f),\qquad
R=V(T)\setminus(\{f\}\cup A\cup B).
\]

Every \(r\in R\) dominates every \(a\in A\). Indeed, otherwise
\[
f\to a\to r
\]
would put \(r\) in \(B\).

Split the order into consecutive blocks ending at the vertices of \(R\), in their order of appearance, and finally at \(f\). Every vertex preceding the endpoint within one of these blocks belongs to \(A\cup B\).

Consider a block ending at \(r\in R\), and let \(I\) be its vertices before \(r\). All vertices of \(A\cap I\) are outneighbours of \(r\), while every inneighbour of \(r\) in \(I\) belongs to \(B\). Applying (5) to this block gives
\[
\begin{aligned}
w(A\cap I)
&\le w(N_T^+(r)\cap I)\\
&\le w(N_T^-(r)\cap I)\\
&\le w(B\cap I).
\end{aligned}
\tag{6}
\]

For the final block, ending at \(f\), property (5) directly gives
\[
w(A\cap I)\le w(B\cap I),
\tag{7}
\]
because \(f\) dominates \(A\) and is dominated by \(B\).

Every vertex of \(A\cup B\) occurs in exactly one of these block interiors. Summing (6) and (7) proves \(w(A)\le w(B)\). ∎

## 3. Proof of the additive bound

We now prove Theorem 1.

Complete \(D\) to a tournament \(T\) as follows:

- For each missing pair having a safe direction, choose such a direction.
- For each unsafe missing pair, orient it towards an endpoint in \(C\). This is possible because \(C\) is a vertex cover of \(H_{\mathrm{bad}}(D)\).

Choose a right-feedback order \(L\) of \(T\), and let \(f\) be its last vertex.

Now change the directions of added arcs incident with \(f\), where necessary, so that **every originally missing pair incident with \(f\) is directed into \(f\)**. Call the resulting tournament \(T'\). No original arc of \(D\) is changed.

The order \(L\) still has the right-feedback property in \(T'\):

- An interval ending before \(f\) is unaffected.
- In an interval ending at \(f\), each reversal changes an outneighbour of \(f\) into an inneighbour, so it only strengthens (5).

By Lemma 2,
\[
w(N_2^{T'}(f))\ge w(N_1^{T'}(f)).
\tag{8}
\]
By construction,
\[
N_1^{T'}(f)=N_1^D(f).
\tag{9}
\]

We claim
\[
N_2^{T'}(f)
\subseteq
N_2^D(f)\cup(C\cap R_D(f)).
\tag{10}
\]

To check this, take \(z\in N_2^{T'}(f)\), witnessed by
\[
f\to u\to z.
\]
The arc \(f\to u\) belongs to \(D\), by (9). There are three possibilities for \(u\to z\).

1. **It is an original arc.**  
   Then \(f\to u\to z\) is a path in \(D\). Since \(z\notin N_1^{T'}(f)=N_1^D(f)\), it follows that \(z\in N_2^D(f)\).

2. **It was added in a safe direction.**  
   Neither endpoint is \(f\), so this direction was not subsequently changed. Applying (1) to \(f\to u\) gives
   \[
   z\in N_1^D(f)\cup N_2^D(f).
   \]
   Again, the first alternative is excluded.

3. **It corresponds to an unsafe missing pair.**  
   Its direction was chosen towards \(C\), and was not changed because neither endpoint is \(f\). Hence \(z\in C\). If \(z\notin N_2^D(f)\), then \(z\in R_D(f)\), since \(z\ne f\) and \(z\notin N_1^D(f)\).

This proves (10). Therefore
\[
\begin{aligned}
w(N_1^D(f))
&=w(N_1^{T'}(f))\\
&\le w(N_2^{T'}(f))\\
&\le w(N_2^D(f))+w(C\cap R_D(f)),
\end{aligned}
\]
which is (2). ∎

### A structural ratio bound

In the unweighted case, let
\[
k=\tau(H_{\mathrm{bad}}(D)),\qquad \delta=\delta^+(D).
\]
If \(\delta>0\), Theorem 1 gives a vertex with
\[
\frac{d_2(v)}{d_1(v)}
\ge 1-\frac{k}{d_1(v)}
\ge 1-\frac{k}{\delta}.
\tag{11}
\]
If \(\delta=0\), a sink already satisfies Seymour’s inequality.

This is useful when the unsafe-pair graph has a small vertex cover relative to the minimum outdegree. It is **not** a universal improvement on the constant stated in the question, because \(k\) need not be small.

## 4. A forbidden-missing-subgraph special case

Let \(M(D)\) be the undirected graph of **all** missing pairs of \(D\).

### Theorem 3
If \(M(D)\) has no induced subgraph isomorphic to
\[
2K_2,\qquad P_4,\qquad C_4,
\tag{12}
\]
then every missing pair has a safe direction. Consequently, for every positive vertex weighting, some vertex satisfies
\[
w(N_2(v))\ge w(N_1(v)).
\tag{13}
\]

Thus Seymour’s conjecture holds for this class. The graphs characterized by (12) are commonly called threshold graphs.

#### Proof

Suppose a missing pair \(\{a,b\}\) is unsafe. Failure of safety in the two directions provides vertices \(x,y\) such that
\[
x\to a,\qquad b\notin N_1(x)\cup N_2(x),
\tag{14}
\]
and
\[
y\to b,\qquad a\notin N_1(y)\cup N_2(y).
\tag{15}
\]

The vertices \(a,b,x,y\) are distinct. In particular, \(x=y\) would contradict (14), since then \(x\to b\).

Moreover, \(x,y\) form a missing pair:

- If \(x\to y\), then \(x\to y\to b\), contradicting (14).
- If \(y\to x\), then \(y\to x\to a\), contradicting (15).

On these four vertices, \(M(D)\) therefore has edges \(ab\) and \(xy\), but does not have edges \(xa\) and \(yb\). The only undetermined pairs are \(ay\) and \(bx\). According as neither, exactly one, or both are missing, the induced missing graph is
\[
2K_2,\quad P_4,\quad\text{or }C_4.
\]
This contradicts (12).

Hence \(H_{\mathrm{bad}}(D)\) has no edges. Apply Theorem 1 with \(C=\varnothing\). ∎

Concrete examples include:

- tournaments;
- tournaments with the edges of a star deleted;
- tournaments with all edges inside one vertex subset deleted;
- more generally, every orientation whose missing graph satisfies (12).

### The forbidden family is exact for this safety criterion

There is also a converse to the assertion about safe directions:

> An undirected graph \(H\) guarantees that every missing pair has a safe direction in every orientation of its complement if and only if \(H\) has none of the induced subgraphs in (12).

Only the reverse implication remains to prove. Suppose \(H\) contains one of those configurations. Label its vertices \(a,b,x,y\) so that
\[
ab,xy\in E(H),\qquad xa,yb\notin E(H),
\]
with \(ay,bx\) optional.

Orient the complement edges on these vertices by
\[
x\to a,\qquad y\to b,
\]
and, when the corresponding edges exist, by
\[
a\to y,\qquad b\to x.
\]
Orient every complement edge between an outside vertex and these four vertices towards the four-vertex set. Orient all remaining edges arbitrarily.

Then \(x\) has only the outneighbour \(a\), and \(y\) has only the outneighbour \(b\). Since \(ab\) is missing,
\[
b\notin N_1(x)\cup N_2(x),\qquad
a\notin N_1(y)\cup N_2(y).
\]
Thus neither direction of \(ab\) is safe.

This characterizes the reachability-preserving completion condition—not the full class of graphs satisfying Seymour’s conjecture.

## 5. Constructivity

The argument does not require finding a globally optimal tournament order.

In the unweighted case, start with any order. Whenever an interval violates (5), move its last vertex to the beginning of that interval. This strictly increases the number of forward arcs, by at least one. There are at most \(\binom n2\) forward arcs, so at most \(\binom n2\) such moves occur.

All intervals can be checked in \(O(n^2)\) time per iteration using cumulative in/out counts. Thus, given a vertex cover \(C\) of \(H_{\mathrm{bad}}(D)\), the proof finds a vertex satisfying (2) in polynomial time; a straightforward implementation takes \(O(n^4)\) time.

The unsafe pairs themselves can be determined in \(O(n^3)\) time by first computing reachability within two steps and then testing (1). This does not assert that a minimum vertex cover can be found efficiently.

## 6. What remains unresolved

The missing step for the general conjecture is eliminating the error term
\[
w(C\cap R(v)).
\]
The proof gives no reason for this term to vanish in an arbitrary oriented graph.

Indeed, unsafe pairs already occur in the directed four-cycle
\[
0\to1\to2\to3\to0.
\]
Both missing pairs, \(02\) and \(13\), are unsafe. Nevertheless, every vertex has
\[
d_1(v)=d_2(v)=1.
\]
Thus unsafe pairs are an obstruction to this particular completion method, not an obstruction to Seymour’s conjecture.

The established output is therefore a weighted special case, an exact characterization of when the missing graph alone guarantees safe completion, and an additive defect bound. It is not a proof or disproof of the general conjecture.