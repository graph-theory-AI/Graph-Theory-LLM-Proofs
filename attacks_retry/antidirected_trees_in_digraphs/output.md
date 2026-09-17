```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured threshold holds for every antidirected spider whose legs have length at most two, with an exact extremal classification in the non-star cases.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; the novelty of this independently proved special case has not been checked."
}
```

# A sharp result for short-legged antidirected spiders

I replace the earlier split-graph approach by a link-graph matching argument. In particular, this proves the conjectured threshold, without any restriction on the host digraph, for the subdivided-star family highlighted in the previous attempt. None of that attempt’s embedding lemmas is assumed below.

Digraphs are finite and loopless, with no parallel arcs; opposite arcs are allowed. Containment means containment as a not necessarily induced subdigraph.

## 1. The partial result

For integers \(r\ge 1\) and \(q\ge 0\), define \(T_{r,q}\) to have vertices
\[
c,\quad u_1,\ldots,u_r,\quad w_1,\ldots,w_r,\quad z_1,\ldots,z_q
\]
and arcs
\[
u_i\to c,\qquad u_i\to w_i\quad(1\le i\le r),
\qquad
z_j\to c\quad(1\le j\le q).
\]
Its underlying tree is a spider with \(r\) legs of length two and \(q\) legs of length one. Its order is
\[
k=2r+q+1.
\]

Write \(x_+=\max\{x,0\}\).

**Theorem.** If an \(n\)-vertex digraph \(D\) contains no \(T_{r,q}\), then
\[
\sum_{v\in V(D)}\bigl(d_D^+(v)-r\bigr)_+
   \le (r+q-1)n.                                      \tag{1}
\]
Consequently,
\[
|A(D)|\le (2r+q-1)n=(k-2)n.                           \tag{2}
\]

Furthermore, if \(r+q\ge2\), equality in (2) holds for a \(T_{r,q}\)-free digraph if and only if \(D\) is a disjoint union of bidirected complete graphs of order
\[
2r+q=k-1.
\]

Reversing all arcs proves the same containment statement for the other antidirected orientation. Directed stars follow immediately from average indegree or average outdegree. Thus:

**Corollary.** The conjecture holds for every antidirected spider all of whose legs have length at most two.

For \(r\ge3\), the trees \(T_{r,q}\) are not caterpillars: deleting their leaves leaves a star with \(r\) edges, not a path. For example, the antidirected once-subdivided \(K_{1,3}\), of order seven, is forced by
\[
|A(D)|>5|V(D)|
\]
in an arbitrary digraph.

The proof uses the standard Tutte–Berge formula, but no results from the papers listed in the question.

## 2. A weighted matching inequality

For a graph \(G\), a vertex set \(A\subseteq V(G)\), and an integer \(r\ge1\), put
\[
\Phi_r(G;A)
  =\sum_{x\in A}\left(1-\frac{r}{d_G(x)+1}\right)_+.
\]

### Lemma 1

If the matching number of \(G\) is at most \(r-1\), then
\[
\Phi_r(G;V(G))\le r-1.                                \tag{3}
\]
If \(r\ge2\), equality is possible only when \(G\) consists of one \(K_{2r-1}\) and isolated vertices.

**Proof.** The Tutte–Berge formula can be written as
\[
\nu(G)=
\min_{X\subseteq V(G)}
\left(
 |X|+\sum_{C\in\operatorname{comp}(G-X)}
          \left\lfloor\frac{|C|}{2}\right\rfloor
\right).
\]
Choose a minimizing \(X\), and write \(a=|X|\). For a component \(C\) of \(G-X\), write
\[
c=|C|,\qquad b=\lfloor c/2\rfloor.
\]
Then
\[
a+\sum_C b=\nu(G)\le r-1,
\]
so in particular \(r\ge a+b+1\).

For \(x\in C\), we have \(d_G(x)+1\le a+c\). Therefore
\[
\left(1-\frac{r}{d_G(x)+1}\right)_+
 \le
\left(1-\frac{r}{a+c}\right)_+
 \le \frac{b}{a+c},
\]
where the last inequality follows from
\[
a+c-r\le c-b-1\le b.
\]
The total contribution of \(C\) is consequently at most \(b\). Each vertex of \(X\) contributes less than one. Summing gives
\[
\Phi_r(G;V(G))
 \le a+\sum_C b
 =\nu(G)\le r-1.
\]

Suppose equality holds and \(r\ge2\). The strict inequality for vertices of \(X\) forces \(X=\varnothing\), and \(\nu(G)=r-1\).

For a component of order \(c\), its contribution is at most \((c-r)_+\). If \(c=2b\ge2\), this is strictly less than \(b\), because \(r\ge b+1\). If \(c=2b+1\) with \(b>0\), equality requires \(r=b+1\). Thus there is exactly one nontrivial component, it has order \(2r-1\), and equality in the degree estimates forces it to be complete. All remaining components are isolated vertices. \(\square\)

## 3. Matchings with unused marked vertices

The extra \(q\) short legs require a refinement of Lemma 1.

### Lemma 2

Let \(A\) be a vertex cover of a graph \(G\). Suppose \(G\) does not contain both

- \(r\) pairwise vertex-disjoint edges, and
- \(q\) distinct vertices of \(A\) outside those edges.

Then
\[
\Phi_r(G;A)\le r+q-1.                                 \tag{4}
\]

If \(r+q-1>0\), equality is possible only when \(G\) consists of a clique of order
\[
2r+q-1
\]
and isolated vertices, with every vertex of that clique belonging to \(A\).

**Proof.** When \(q=0\), this follows from Lemma 1, including its equality statement. Assume \(q\ge1\), and set
\[
R=r+q-1.
\]

Add a set \(Z\) of \(q\) new independent vertices, each adjacent to every vertex of \(A\), obtaining a graph \(H\).

The forbidden configuration exists in \(G\) if and only if \(H\) has a matching of size at least \(r+q\). One implication is immediate. For the other, a matching of that size can be modified to saturate all of \(Z\): if \(z\in Z\) is unmatched, replace an original matching edge incident with \(A\) by an edge from \(z\) to its endpoint in \(A\). Such an original edge exists because the matching has at least \(r+q\) edges. After saturating \(Z\), remove its \(q\) matching edges. The remaining matching and their \(q\) endpoints in \(A\) give the required configuration.

Hence
\[
\nu(H)\le R.                                         \tag{5}
\]

Choose a Tutte–Berge minimizing set \(X\) for \(H\).

### Case 1: \(Z\subseteq X\)

Writing \(X_0=X\setminus Z\), the Tutte–Berge expression gives
\[
|X_0|+
\sum_{C\in\operatorname{comp}(G-X_0)}
 \left\lfloor\frac{|C|}{2}\right\rfloor
\le r-1.
\]
Thus \(\nu(G)\le r-1\), and Lemma 1 gives
\[
\Phi_r(G;A)\le r-1<R.
\]

### Case 2: \(Z\not\subseteq X\)

Put
\[
q'=|Z\setminus X|\ge1,\qquad b=|X\setminus Z|,
\qquad R'=r+q'-1.
\]
If \(A\subseteq X\), then
\[
\Phi_r(G;A)\le |A|\le |X|\le R,
\]
with strict inequality when equality with \(R>0\) is considered.

Otherwise, all vertices of \(A\setminus X\) and \(Z\setminus X\) lie in a single component \(C\) of \(H-X\). Every other component is an isolated vertex: this uses the assumption that \(A\) covers every edge of \(G\).

Let
\[
h=|C\setminus Z|.
\]
By (5) and the Tutte–Berge formula,
\[
b+q-q'+\left\lfloor\frac{h+q'}2\right\rfloor\le R.
\]
Equivalently,
\[
b+\left\lfloor\frac{h+q'}2\right\rfloor\le R'.
\]
In particular,
\[
b\le R',
\qquad
2b+h\le 2r+q'-1=r+R'.                               \tag{6}
\]

Every \(u\in A\setminus X\) satisfies
\[
d_G(u)+1\le b+h.
\]
Writing \(M=b+h\), we obtain
\[
\Phi_r(G;A)
 \le b+h\left(1-\frac rM\right)_+.
\]
If \(M\le r\), this is at most \(b\le R'\). If \(M>r\), then (6) gives
\[
\begin{aligned}
\Phi_r(G;A)
&\le b+(M-b)\left(1-\frac rM\right)\\
&=M-r+\frac{rb}{M}\\
&\le (R'-b)+b\\
&=R'\le R.
\end{aligned}
\]
This proves (4).

For completeness, consider equality with \(R>0\). The preceding cases are strict unless we are in the last calculation. If \(b>0\), the contribution from \(A\cap X\) is strictly less than \(b\), so equality requires \(b=0\). It also requires \(q'=q\) and
\[
h=2r+q-1.
\]
All \(h\) original vertices in \(C\) must belong to \(A\), and each must have degree \(h-1\) in \(G\). Thus they form \(K_h\); all remaining vertices of \(G\) are isolated. \(\square\)

## 4. Applying the matching inequality to a digraph

Suppose \(D\) contains no \(T_{r,q}\).

For each vertex \(v\in V(D)\), let
\[
A_v=N_D^-(v).
\]
Define an undirected link graph \(L_v\) on \(V(D)\setminus\{v\}\) by
\[
E(L_v)=
\left\{
 \{u,w\}:
 u\in A_v,\quad u\to w\in A(D),\quad w\ne v
\right\}.
\]
In particular, \(A_v\) is a vertex cover of \(L_v\).

A matching of \(r\) edges in \(L_v\), together with \(q\) unused vertices of \(A_v\), would give a copy of \(T_{r,q}\) centered at \(v\). For each matching edge, choose an endpoint \(u\in A_v\) whose outgoing arc generated that edge. Its other endpoint supplies the corresponding \(w_i\). The matching and the unused marked vertices ensure that every chosen vertex is distinct.

Therefore Lemma 2 applies to \((L_v,A_v)\).

For every \(u\in A_v\), all outneighbors of \(u\), except \(v\), are neighbors of \(u\) in \(L_v\). Hence
\[
d_{L_v}(u)+1\ge d_D^+(u).
\]
Since \(x\mapsto (1-r/x)_+\) is nondecreasing for \(x>0\), Lemma 2 yields
\[
\sum_{u\in N_D^-(v)}
 \left(1-\frac{r}{d_D^+(u)}\right)_+
\le r+q-1.                                          \tag{7}
\]
The denominators are nonzero because every summand corresponds to an arc \(u\to v\).

Summing (7) over all \(v\),
\[
\begin{aligned}
(r+q-1)n
&\ge
\sum_v\sum_{u\in N_D^-(v)}
 \left(1-\frac{r}{d_D^+(u)}\right)_+\\
&=
\sum_{u:d_D^+(u)>0}
d_D^+(u)\left(1-\frac{r}{d_D^+(u)}\right)_+\\
&=
\sum_u\bigl(d_D^+(u)-r\bigr)_+.
\end{aligned}
\]
This proves (1). Finally,
\[
\begin{aligned}
|A(D)|
&=\sum_u d_D^+(u)\\
&=\sum_u\min\{d_D^+(u),r\}
  +\sum_u\bigl(d_D^+(u)-r\bigr)_+\\
&\le rn+(r+q-1)n\\
&=(2r+q-1)n.
\end{aligned}
\]
Thus the conjectured strict density threshold forces \(T_{r,q}\).

## 5. Equality and sharpness

Assume \(r+q\ge2\), and put
\[
R=r+q-1>0,\qquad c=2r+q-1=r+R.
\]
Suppose \(D\) is \(T_{r,q}\)-free and
\[
|A(D)|=cn.
\]

Equality in the proof forces
\[
d_D^+(u)\ge r\quad\text{for every }u,
\]
and equality in (7) for every \(v\). Lemma 2 consequently shows that \(L_v\) consists of a clique \(C_v\) of order \(c\) and isolated vertices, with \(C_v\subseteq A_v\).

Every vertex has positive outdegree and thus belongs to some \(A_v\). The inequality
\[
d_D^+(u)\le d_{L_v}(u)+1
\]
then shows that every outdegree is at most \(c\). Since their average is \(c\), all outdegrees equal \(c\).

Because \(c\ge2\), no member of \(A_v\) can be isolated in \(L_v\). Therefore
\[
A_v=C_v,\qquad d_D^-(v)=c.
\]
Moreover, for every \(u\in C_v\),
\[
N_D^+(u)=\bigl(C_v\cup\{v\}\bigr)\setminus\{u\}.       \tag{8}
\]

Set \(W_v=C_v\cup\{v\}\). I claim that \(v\) has no outneighbor outside \(W_v\). Otherwise, take \(v\to w\) with \(w\notin W_v\). Then \(v\in C_w\). Since \(|C_w|=c\ge2\), choose
\[
x\in C_w\setminus\{v\}.
\]
By (8), \(x\to v\) and \(x\to w\). Thus \(x\in C_v\), but (8) applied at \(v\) says that every outneighbor of \(x\) lies in \(W_v\), a contradiction.

It follows that \(v\) dominates all of \(C_v\). Together with (8), this makes \(D[W_v]\) a bidirected \(K_{c+1}\). Every vertex already has indegree and outdegree \(c\) within this clique, so there are no arcs between it and the rest of \(D\). Repeating proves the asserted decomposition.

Conversely, disjoint unions of bidirected \(K_{c+1}=K_{k-1}\) have exactly
\[
(k-2)|V(D)|
\]
arcs and cannot contain a connected tree of order \(k\). Thus the bound and equality classification are sharp.

## 6. What remains unresolved

This proves the original threshold for an unrestricted-host family containing genuine non-caterpillars. In particular, it removes the forbidden-transitive-triangle assumption previously needed for the once-subdivided stars.

It does **not** settle all antidirected trees, or even all diameter-four antidirected trees. A general diameter-four tree can have a neighbor of its center supporting several pendant leaves. Its link-graph representation requires packing rooted stars rather than matching edges, and the matching inequalities proved here do not address that problem.

No proof or counterexample to the full conjecture is obtained.