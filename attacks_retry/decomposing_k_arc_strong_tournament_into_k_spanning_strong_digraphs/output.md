```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A one-vertex repair lemma implies that every counterexample contains an induced counterexample on at most (k+1)(k+2) vertices.",
  "would_publish": false,
  "caveats": "The semidegree-critical case, including regular tournaments, remains untreated; novelty of these partial results is unverified."
}
```

# A one-vertex repair lemma and a bound on minimal counterexamples

I do not resolve the full conjecture. I checked the previous attempt’s nontrivial tight-cut argument and find it valid. The additional result below handles a different situation: deleting a vertex preserves minimum semidegree \(k\), but destroys \(k\)-arc-strong connectivity.

This yields a quadratic bound on the order of an induced minimal counterexample. I make no claim that these results are new or absent from the cited literature.

Throughout, \(k\ge 1\). For a digraph \(D\), write
\[
d_D^+(X)=|E_D(X,V(D)\setminus X)|,\qquad
d_D^-(X)=|E_D(V(D)\setminus X,X)|,
\]
and
\[
\delta^0(D)=\min_{x\in V(D)}\min\{d_D^+(x),d_D^-(x)\}.
\]
For a nontrivial digraph, let
\[
\lambda(D)=\min_{\varnothing\ne X\subsetneq V(D)}d_D^+(X).
\]
Thus \(D\) is \(k\)-arc-strong exactly when every nonempty proper set has at least \(k\) entering and at least \(k\) leaving arcs.

Producing \(k\) pairwise arc-disjoint spanning strong subdigraphs suffices: all unused arcs can subsequently be assigned arbitrarily to the parts.

## 1. The additional partial results

**Theorem A — one-vertex repair.**  
Let \(T\) be a \(k\)-arc-strong tournament, and suppose \(v\in V(T)\) satisfies
\[
\delta^0(T-v)\ge k
\qquad\text{but}\qquad
\lambda(T-v)<k.
\]
Then \(T\) decomposes into \(k\) spanning strong digraphs.

**Theorem B — bounded induced counterexamples.**  
If a \(k\)-arc-strong tournament is a counterexample to the conjecture, it contains an induced counterexample \(S\) such that
\[
|V(S)|\le (k+1)(k+2).
\]
Moreover, \(S\) can be chosen to satisfy
\[
\lambda(S)=\delta^0(S)=k,
\qquad
\delta^0(S-x)=k-1\quad\text{for every }x\in V(S),
\]
and every minimum directed cut of \(S\) has a singleton side.

The essential new ingredient relative to the supplied attempt is a pruning lemma for arcs entering one side of a deficient cut.

## 2. Two tools for the construction

### 2.1. Partitioning a bipartite graph into edge covers

**Lemma 1.** If a bipartite graph \(G\) has minimum degree at least \(k\), its edges can be partitioned into \(k\) edge covers.

**Proof.** At every vertex, partition its incident edges into groups of size \(k\), with at most one smaller residual group. Split the vertex into one vertex per group, retaining the corresponding incidences. The resulting bipartite graph has maximum degree at most \(k\), and each original vertex has a split copy of degree exactly \(k\).

A bipartite graph of maximum degree at most \(k\) has a proper edge-colouring with \(k\) colours. One proof is to complete it to a \(k\)-regular bipartite multigraph and repeatedly remove perfect matchings; Hall’s condition holds in every regular bipartite multigraph.

Project the colouring back. At a degree-\(k\) split copy, every colour occurs. Hence every original vertex is incident with every colour, as required. \(\square\)

### 2.2. Packing arborescences with a prescribed root list

I use the standard rooted arborescence-packing theorem: a digraph with root \(r\) contains \(k\) arc-disjoint spanning out-arborescences rooted at \(r\) if every nonempty set not containing \(r\) has at least \(k\) entering arcs.

The following root-list version follows immediately.

**Lemma 2.** Let \(J\) be a digraph on a nonempty vertex set \(A\), and let
\[
a_1,\ldots,a_k\in A
\]
be a labelled list, possibly with repetitions. If
\[
d_J^-(X)+|\{i:a_i\in X\}|\ge k
\qquad(\varnothing\ne X\subseteq A),
\]
then \(J\) contains pairwise arc-disjoint spanning out-arborescences \(O_i\), with \(O_i\) rooted at \(a_i\).

**Proof.** Add a new source \(r\) and the \(k\) labelled arcs \(ra_i\), allowing parallel arcs. Apply the rooted packing theorem.

Each of the \(k\) arborescences uses at least one arc leaving \(r\). There are exactly \(k\) such arcs, so each arborescence uses exactly one. Deleting \(r\) therefore gives the required spanning out-arborescences. \(\square\)

The analogous statement for in-arborescences follows by reversing all arcs.

## 3. Pruning the arcs that repair a deficient cut

We first record two elementary tournament facts.

Let \(U\) be a tournament with \(\delta^0(U)\ge k\). If \(|X|=s\), then
\[
d_U^-(X)
=\sum_{x\in X}d_U^-(x)-\binom{s}{2}
\ge ks-\binom{s}{2}.
\]
For \(1\le s\le 2k\),
\[
ks-\binom{s}{2}
=\frac{s(2k+1-s)}2
\ge k.
\]
Consequently,
\[
d_U^-(X)<k\quad\Longrightarrow\quad |X|\ge 2k+1. \tag{1}
\]
The analogous assertion holds for outgoing cuts.

Also, two sets with entering cuts smaller than \(k\) cannot be disjoint. Indeed, if \(X,Y\) were disjoint, every arc between them would contribute to
\(d_U^-(X)+d_U^-(Y)\), giving
\[
|X||Y|\le d_U^-(X)+d_U^-(Y)\le 2k-2,
\]
contrary to (1).

The following lemma is the main additional ingredient.

**Lemma 3 — root pruning.**  
Let \(U\) be a tournament with \(\delta^0(U)\ge k\), and let
\[
m=\lambda(U)<k.
\]
Suppose \(A\) is a nonempty proper set with \(d_U^-(A)=m\). Let \(Q\subseteq A\) satisfy
\[
d_U^-(X)+|Q\cap X|\ge k
\qquad(\varnothing\ne X\subseteq A). \tag{2}
\]
Then there is \(Q'\subseteq Q\), of size exactly \(k-m\), such that
\[
d_U^-(X)+|Q'\cap X|\ge k
\qquad(\varnothing\ne X\subseteq A). \tag{3}
\]

**Proof.** Choose an inclusion-minimal \(Q'\subseteq Q\) satisfying (3), and put
\[
h(X)=d_U^-(X)+|Q'\cap X|.
\]

For every \(q\in Q'\), minimality supplies a nonempty set \(X_q\subseteq A\) such that
\[
q\in X_q,\qquad h(X_q)=k.
\]
Since \(q\in Q'\cap X_q\), we have
\[
d_U^-(X_q)<k.
\]
Thus the sets \(X_q\) are pairwise intersecting by the preceding observation.

For any two sets \(X,Y\), the tournament cut identity is
\[
d_U^-(X)+d_U^-(Y)
=
d_U^-(X\cap Y)+d_U^-(X\cup Y)
+|X\setminus Y|\,|Y\setminus X|.
\]
Adding the modular function \(|Q'\cap X|\) gives the same identity for \(h\).

Apply it to two witness sets \(X_q,X_{q'}\). Their intersection is nonempty, and their union is contained in \(A\). Hence both the intersection and the union satisfy (3), so
\[
2k
\ge 2k+|X_q\setminus X_{q'}|\,|X_{q'}\setminus X_q|.
\]
Therefore one witness set contains the other. The witness sets form a chain.

Let \(X_*\) be its largest member. Every element of \(Q'\) belongs to \(X_*\), so
\[
|Q'|
=|Q'\cap X_*|
=k-d_U^-(X_*)
\le k-m.
\]
On the other hand, applying (3) to \(A\) gives
\[
m+|Q'|\ge k.
\]
Thus \(|Q'|=k-m\). \(\square\)

There is, of course, an outgoing-cut version obtained by reversing \(U\).

## 4. Proof of the one-vertex repair theorem

Let
\[
U=T-v,\qquad m=\lambda(U)<k,\qquad r=k-m.
\]
Choose a minimum cut
\[
V(U)=A\mathbin{\dot\cup}B,\qquad |E_U(B,A)|=m.
\]
Because \(\delta^0(U)\ge k\), equation (1) and its outgoing analogue give
\[
|A|,|B|\ge 2k+1. \tag{4}
\]

### Selecting exactly \(r\) arcs on each side of \(v\)

Set
\[
Q=N_T^+(v)\cap A.
\]
For every nonempty \(X\subseteq A\),
\[
d_U^-(X)+|Q\cap X|
=d_T^-(X)
\ge k.
\]
By Lemma 3, there is a set
\[
Q'=\{a_{m+1},\ldots,a_k\}\subseteq Q,
\qquad |Q'|=r,
\]
such that
\[
d_U^-(X)+|Q'\cap X|\ge k
\qquad(\varnothing\ne X\subseteq A). \tag{5}
\]

Dually, with
\[
P=N_T^-(v)\cap B,
\]
there is
\[
P'=\{b_{m+1},\ldots,b_k\}\subseteq P,
\qquad |P'|=r,
\]
such that
\[
d_U^+(Y)+|P'\cap Y|\ge k
\qquad(\varnothing\ne Y\subseteq B). \tag{6}
\]

Label the \(m\) actual arcs from \(B\) to \(A\) as
\[
b_i a_i,\qquad 1\le i\le m.
\]
Pair the elements of \(P'\) and \(Q'\) arbitrarily, producing the \(r\) directed paths
\[
b_i v a_i,\qquad m<i\le k.
\]
These paths are pairwise arc-disjoint: their arcs entering \(v\) are distinct, as are their arcs leaving \(v\).

### Packing the trees on the two sides

For every nonempty \(X\subseteq A\),
\[
\begin{aligned}
d_{U[A]}^-(X)+|\{i:a_i\in X\}|
&=d_U^-(X)+|Q'\cap X|\\
&\ge k.
\end{aligned}
\]
Lemma 2 gives pairwise arc-disjoint spanning out-arborescences
\[
O_i\subseteq U[A],
\]
rooted at \(a_i\).

Likewise, (6) gives pairwise arc-disjoint spanning in-arborescences
\[
I_i\subseteq U[B],
\]
rooted at \(b_i\).

### Providing the forward crossings

Consider the bipartite graph of arcs from \(A\) to \(B\). Since only \(m\) crossing pairs are oriented backwards, every vertex of this graph has degree at least
\[
\min\{|A|,|B|\}-m\ge 2k+1-m\ge k.
\]
By Lemma 1, partition these forward arcs into edge covers
\[
F_1,\ldots,F_k.
\]

For \(i\le m\), let
\[
H_i=O_i\cup I_i\cup F_i\cup\{b_i a_i\}.
\]
For \(i>m\), let
\[
H_i=O_i\cup I_i\cup F_i\cup\{b_i v,va_i\}.
\]

For each \(i\), the construction is strong on \(A\cup B\), together with \(v\) when its connecting path uses \(v\). To see this, use \(a_i\) as a reference vertex:

- \(a_i\) reaches all of \(A\) through \(O_i\).
- Since every \(b\in B\) has an incoming arc in \(F_i\), \(a_i\) reaches all of \(B\).
- Every vertex of \(B\) reaches \(b_i\) through \(I_i\), and then reaches \(a_i\) through the connecting arc or path.
- Every vertex of \(A\) has an outgoing arc in \(F_i\), so it also reaches \(a_i\).
- If the connecting path is \(b_i v a_i\), then \(v\) is mutually reachable with \(a_i\).

The \(H_i\) are pairwise arc-disjoint.

### Adding \(v\) to the other \(m\) parts

Exactly \(r\) incoming and \(r\) outgoing arcs at \(v\) have been used. Since \(T\) is \(k\)-arc-strong,
\[
d_T^-(v),d_T^+(v)\ge k.
\]
There remain at least \(k-r=m\) unused arcs of each direction at \(v\).

For each \(i\le m\), choose a distinct unused incoming arc \(x_i v\) and a distinct unused outgoing arc \(vy_i\), and add them to \(H_i\). This extends its strong subdigraph on \(A\cup B\) to a spanning strong subdigraph of \(T\). If \(m=0\), this step is empty.

Assign all remaining arcs arbitrarily to the parts. This proves Theorem A. \(\square\)

## 5. Verification of the nontrivial tight-cut result

For completeness, the earlier attempt’s main theorem follows from the same construction.

**Lemma 4 — nontrivial tight cuts.**  
Let \(T\) be \(k\)-arc-strong, and suppose
\[
V(T)=A\mathbin{\dot\cup}B,\qquad |A|,|B|\ge2,\qquad |E_T(B,A)|=k.
\]
Then \(T\) decomposes into \(k\) spanning strong digraphs.

**Proof.** Put \(a=|A|\). Summing indegrees over \(A\) gives
\[
ka\le \binom a2+k,
\]
or
\[
(a-1)(a-2k)\ge0.
\]
As \(a\ge2\), we obtain \(a\ge2k\). Similarly, summing outdegrees over \(B\) gives \(|B|\ge2k\).

Label the backward arcs \(b_i a_i\), \(1\le i\le k\). For every nonempty \(X\subseteq A\),
\[
d_{T[A]}^-(X)+|\{i:a_i\in X\}|=d_T^-(X)\ge k.
\]
Thus Lemma 2 supplies the \(k\) out-arborescences on \(A\); its dual supplies the \(k\) in-arborescences on \(B\).

The bipartite graph of forward crossing arcs has minimum degree at least
\[
\min\{|A|,|B|\}-k\ge k,
\]
so it has \(k\) edge covers. The \(O_i,I_i,F_i,b_i a_i\) construction in the preceding proof gives the required strong subdigraphs. \(\square\)

This verifies, rather than merely assumes, the previous attempt’s key sufficient condition.

## 6. Proof of the bound on induced counterexamples

We first use the elementary vertex-extension principle.

> If \(T-x\) has \(k\) arc-disjoint spanning strong subdigraphs and \(x\) has at least \(k\) inneighbours and at least \(k\) outneighbours in \(T-x\), then \(T\) has the required decomposition.

Indeed, add a distinct pair \(u_i x,xw_i\) to each part.

Now suppose \(T\) is a counterexample. Choose an induced counterexample \(S\subseteq T\) with minimum order.

### 6.1. Every vertex deletion lowers the minimum semidegree

Suppose some \(x\in V(S)\) satisfies
\[
\delta^0(S-x)\ge k.
\]

- If \(S-x\) is \(k\)-arc-strong, minimality of \(S\) gives the desired decomposition of \(S-x\). The extension principle gives one for \(S\), a contradiction.
- If \(S-x\) is not \(k\)-arc-strong, Theorem A directly gives the desired decomposition of \(S\), again a contradiction.

Hence
\[
\delta^0(S-x)<k\qquad\text{for every }x.
\]
Deleting a vertex reduces any remaining indegree or outdegree by at most one. Since \(\delta^0(S)\ge k\), it follows that
\[
\delta^0(S)=k,\qquad
\delta^0(S-x)=k-1\quad\text{for every }x.
\]
Consequently,
\[
\lambda(S)=k.
\]
Lemma 4 now shows that every minimum directed cut of \(S\) has a singleton side.

### 6.2. Counting the vertices of a semidegree-critical tournament

Write \(n=|V(S)|\). Necessarily \(n\ge2k+1\). If \(n=2k+1\), the desired bound is immediate, so assume \(n>2k+1\).

Let
\[
L^-=\{u:d_S^-(u)=k\},\qquad
L^+=\{u:d_S^+(u)=k\},
\]
and put
\[
a=|L^-|,\qquad b=|L^+|.
\]
The two sets are disjoint: membership in both would give \(n-1=2k\).

Let
\[
C=V(S)\setminus(L^-\cup L^+).
\]
For every \(z\in C\), deleting \(z\) lowers some remaining indegree or outdegree to \(k-1\). Therefore either
\[
z\to u\quad\text{for some }u\in L^-,
\]
or
\[
w\to z\quad\text{for some }w\in L^+.
\]
It follows that
\[
|C|\le e_S(C,L^-)+e_S(L^+,C). \tag{7}
\]

Set \(e=e_S(L^+,L^-)\). Summing indegrees over \(L^-\) gives
\[
e_S(C,L^-)=ka-\binom a2-e.
\]
Summing outdegrees over \(L^+\) gives
\[
e_S(L^+,C)=kb-\binom b2-e.
\]
Combining these with (7),
\[
n\le (k+1)(a+b)-\binom a2-\binom b2-2e. \tag{8}
\]

For every nonnegative integer \(t\),
\[
(k+1)t-\binom t2
\le \frac{(k+1)(k+2)}2.
\]
Indeed, the difference between the right and left sides is
\[
\frac{(t-k-1)(t-k-2)}2\ge0.
\]
Applying this twice in (8) proves
\[
n\le(k+1)(k+2).
\]
This completes the proof of Theorem B. \(\square\)

The more detailed inequality (8) is also a useful restriction: every arc from a minimum-outdegree vertex to a minimum-indegree vertex reduces this upper bound by two.

## 7. Examples with only singleton minimum cuts

Theorem A is not restricted to tournaments satisfying the nontrivial-minimum-cut condition.

Fix \(k\ge2\). Take regular tournaments \(A,B\), each of order
\[
t=2k+1.
\]
Orient all crossing pairs from \(A\) to \(B\), except for \(k-1\) arbitrary reversed arcs. Add a vertex \(v\) such that

- \(v\) has exactly two outneighbours in \(A\);
- \(v\) has exactly two inneighbours in \(B\).

All other pairs involving \(v\) have the opposite orientations.

Let \(U=T-v\). Its internal block degrees already give
\[
\delta^0(U)\ge k.
\]
In a regular tournament of order \(2k+1\), a set of size \(s\) has outgoing cut
\[
\frac{s(2k+1-s)}2\ge k
\qquad(1\le s\le2k).
\]
Thus any cut of \(U\) splitting a block has at least \(k\) arcs, while the cut from \(B\) to \(A\) has size \(k-1\). Hence
\[
\lambda(U)=k-1.
\]

The same internal-cut calculation shows that every cut of \(T\) splitting a block has at least \(k\) arcs. The cuts not splitting either block have sizes
\[
k+1,\qquad 2k+1,\qquad (2k+1)^2+k.
\]
Therefore \(T\) is \(k\)-arc-strong, and Theorem A applies.

In fact, all its minimum cuts have a singleton side. Here are the details.

A cut of size \(k\) must split exactly one block, and its intersection with that block must have size \(1\) or \(2k\).

- If it splits \(A\), the abundance of forward \(A\)-to-\(B\) arcs forces all of \(B\) onto the outgoing side of the cut. The two arcs from \(B\) to \(v\) then force \(v\) onto that side as well. Since \(v\) has two outneighbours in \(A\), the opposite side must be a singleton of \(A\).
- If it splits \(B\), the forward crossing arcs force all of \(A\) outside the outgoing side. The two arcs from \(v\) to \(A\) force \(v\) outside as well. Since two vertices of \(B\) send arcs to \(v\), the outgoing side must be a singleton of \(B\).

Finally, only \(k+1\) arcs enter \(A\) from outside, so some vertex of \(A\) receives none of them and has indegree exactly \(k\). Thus \(\lambda(T)=k\).

This supplies an explicit family covered by Theorem A despite having no nontrivial minimum directed cut.

## 8. What remains unresolved

The reduction leaves tournaments that are **vertex-critical for minimum semidegree \(k\)**:
\[
\delta^0(T)=k,\qquad
\delta^0(T-v)=k-1\quad\text{for every }v.
\]
The order bound does not settle this class.

In particular, a regular tournament of order \(2k+1\) lies entirely in the remaining case. Deleting any vertex lowers the minimum semidegree to \(k-1\), and
\[
d_T^+(X)=\frac{|X|(2k+1-|X|)}2
\]
shows that its minimum cuts have singleton sides.

Moreover, such a tournament has exactly \(k|V(T)|\) arcs. Every spanning strong subdigraph has at least \(|V(T)|\) arcs, so a decomposition into \(k\) such subdigraphs must consist of \(k\) directed Hamilton cycles.

Thus the argument proves the one-vertex repair special case and the quadratic bound on induced minimal counterexamples, but it does not resolve the regular case or the full Bang-Jensen–Yeo conjecture. No computational enumeration or novelty claim is being made.