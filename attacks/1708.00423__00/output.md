```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not resolved here, but the factorial estimate sharpens to γ(D) ≤ a! Σ_{j=0}^{a-1} 1/j! < e a!, while an explicit family has γ(D)=a+1 and hence forces ℓ≥2 in the literal formulation.",
  "would_publish": false,
  "caveats": "The improvement is only a factor of order a and may be implicit in the source proof; it remains factorial rather than polynomial."
}
```

## 1. Statement and conventions

Let \(D\) be a finite digraph, and let \(\alpha(D)\) be the independence number of its underlying undirected graph. A set \(S\subseteq V(D)\) is dominating if every vertex lies in \(S\) or receives an arc from a vertex of \(S\). Thus
\[
N^+[S]=S\cup\{v:\text{there is }s\in S\text{ with }s\to v\}=V(D).
\]
A directed triangle means a directed cycle on three distinct vertices; additional arcs, if digons are permitted, do not destroy such a triangle.

Write
\[
f(a)=\sup\{\gamma(D):D\text{ is directed-triangle-free and }\alpha(D)\le a\}.
\]
The conjecture asks whether \(f(a)\le a^\ell\) for some absolute integer \(\ell\).

I obtain a modest sharpening of the known factorial bound, together with an explicit lower-bound family and a structural description of where the factorial recursion loses information.

---

## 2. A refined factorial upper bound

### Proposition 2.1
For every integer \(a\ge1\),
\[
f(a)\le a!\sum_{j=0}^{a-1}\frac1{j!}<e\,a!.
\]
In particular, for \(a\ge3\) this is strictly smaller than the published estimate \(a\,a!\).

### Lemma 2.2
Every digraph \(D\) has an induced acyclic dominating set.

#### Proof
Start with \(A=\varnothing\). While some vertex is not dominated by \(A\), choose such a vertex and append it to \(A\). Write the selected vertices in order as
\[
v_1,v_2,\dots,v_m.
\]
When \(v_j\) was selected, it was not dominated by any earlier \(v_i\). Hence there is no arc \(v_i\to v_j\) for \(i<j\). Consequently every arc in \(D[A]\) goes from a larger index to a smaller index, so \(D[A]\) is acyclic. At termination, \(A\) dominates \(D\). \(\square\)

### Lemma 2.3
Every acyclic digraph \(H\) has an independent dominating set of size at most \(\alpha(H)\).

#### Proof
Take a topological ordering \(w_1,\dots,w_t\), with all arcs directed from earlier to later vertices. Scan this order, adding \(w_i\) whenever it has not already been dominated by a previously selected vertex.

If \(w_i,w_j\) are both selected and \(i<j\), then \(w_i\not\to w_j\), since otherwise \(w_j\) would already have been dominated. Also \(w_j\not\to w_i\) by the topological ordering. Thus the selected set is independent. It dominates \(H\) by construction and consequently has size at most \(\alpha(H)\). \(\square\)

### Proof of Proposition 2.1

Let \(D\) be directed-triangle-free with \(\alpha(D)\le a\). By Lemma 2.2, choose an acyclic dominating set \(A\). By Lemma 2.3, \(D[A]\) has an independent dominating set
\[
Q\subseteq A,\qquad |Q|\le a.
\]

Let
\[
R=V(D)\setminus N^+[Q]
\]
be the vertices not dominated by \(Q\). We claim that every \(x\in R\) is nonadjacent to at least one vertex of \(Q\).

Indeed, because \(A\) dominates \(D\), some \(y\in A\) satisfies \(y\to x\). We cannot have \(y=x\), since \(Q\) dominates every vertex of \(A\), whereas \(x\notin N^+[Q]\). We also cannot have \(y\in Q\). As \(Q\) dominates \(A\), there is therefore \(q\in Q\) with
\[
q\to y\to x.
\]
The arc \(q\to x\) is absent because \(x\in R\). The reverse arc \(x\to q\) would create the directed triangle
\[
q\to y\to x\to q.
\]
Thus \(q\) and \(x\) are nonadjacent.

For \(q\in Q\), let
\[
\overline N(q)=\{x\ne q:xq,qx\notin A(D)\}.
\]
We have shown that
\[
R\subseteq\bigcup_{q\in Q}\overline N(q).
\]
Moreover,
\[
\alpha\bigl(D[\overline N(q)]\bigr)\le a-1,
\]
because any independent set in \(\overline N(q)\) can be augmented by \(q\).

For every \(q\in Q\), take a dominating set of \(D[\overline N(q)]\) of size at most \(f(a-1)\). Together with \(Q\), these sets dominate all of \(D\). Hence
\[
f(a)\le a\bigl(1+f(a-1)\bigr),\qquad f(0)=0.
\]
Let \(b_0=0\) and \(b_a=a(1+b_{a-1})\). A direct induction gives
\[
b_a=a!\sum_{j=0}^{a-1}\frac1{j!}.
\]
Therefore \(f(a)\le b_a<e\,a!\), as claimed. \(\square\)

This changes the published \(a\,a!\) estimate by a factor asymptotic to \(a/e\), but does not change its factorial nature.

---

## 3. An explicit lower-bound family

The following family shows that \(\gamma(D)\le\alpha(D)\) is false even for directed-triangle-free digraphs, and that the exponent in the literal bound \(\gamma(D)\le\alpha(D)^\ell\) must satisfy \(\ell\ge2\).

### Proposition 3.1
For every \(a\ge2\) and every \(k\ge1\), there is an oriented directed-triangle-free graph \(D_{a,k}\) such that
\[
\alpha(D_{a,k})=a,\qquad \gamma(D_{a,k})=a+1.
\]

#### Construction
Let
\[
n=(a+1)(k+1)-1
\]
and take vertex set \(\mathbb Z_n\). Put an arc
\[
i\to i+j\pmod n
\qquad\text{for every }1\le j\le k.
\]

#### Directed-triangle-freeness
A directed triangle would give three increments \(p,q,r\in\{1,\dots,k\}\) satisfying
\[
p+q+r\equiv0\pmod n.
\]
But
\[
0<p+q+r\le3k<n,
\]
where \(n>3k\) follows from \(a\ge2\). This is impossible.

#### Independence number
Two vertices are adjacent in the underlying graph exactly when their cyclic distance in one direction is at most \(k\). Thus consecutive vertices of an independent set around the cyclic order must be separated by at least \(k+1\) positions. Hence
\[
\alpha(D_{a,k})\le \left\lfloor\frac{n}{k+1}\right\rfloor=a.
\]
Equality is attained by
\[
0,\ k+1,\ 2(k+1),\dots,(a-1)(k+1).
\]

#### Domination number
Each closed out-neighborhood is a cyclic interval of exactly \(k+1\) vertices:
\[
N^+[i]=\{i,i+1,\dots,i+k\}.
\]
Therefore any dominating set has size at least
\[
\left\lceil\frac{n}{k+1}\right\rceil=a+1.
\]
Conversely, the \(a+1\) vertices
\[
0,\ k+1,\ 2(k+1),\dots,a(k+1)
\]
have closed out-neighborhoods covering \(\mathbb Z_n\). Thus
\[
\gamma(D_{a,k})=a+1.
\]
\(\square\)

For \(k=1\), this is simply the directed cycle \(C_{2a+1}\). Allowing arbitrary \(k\) also shows that the number of vertices is unbounded even when \(\alpha\) and \(\gamma\) are fixed.

---

## 4. Why the factorial recursion is wasteful

The proof of Proposition 2.1 treats the nonneighbor regions \(\overline N(q)\), \(q\in Q\), separately. All \(a\) regions can genuinely be needed for a particular choice of \(Q\), so one cannot simply delete one branch.

For \(a\ge2\), define a digraph \(H_a\) on
\[
S=\{s_1,\dots,s_a\},\quad
P=\{p_1,\dots,p_a\},\quad
X=\{x_1,\dots,x_a\}
\]
with arcs
\[
s_i\to p_i,\qquad p_i\to x_i,
\]
and, for \(i\ne j\),
\[
x_i\to s_j,\qquad x_i\to p_j,
\]
and no other arcs.

Every underlying triangle is of the form \(\{s_i,p_i,x_j\}\) with \(j\ne i\), and it is oriented transitively:
\[
x_j\to s_i\to p_i,\qquad x_j\to p_i.
\]
Hence \(H_a\) is directed-triangle-free.

One checks that \(\alpha(H_a)=a\):

- each of \(S,P,X\) is independent of size \(a\);
- an independent set meeting both \(S\) and \(P\) chooses at most one endpoint from each pair \(\{s_i,p_i\}\);
- \(P\) is complete to \(X\) in the underlying graph;
- one vertex \(x_i\) can be combined only with \(s_i\), while two distinct vertices of \(X\) cannot be combined with any vertex of \(S\).

Now \(S\cup P\) is an acyclic dominating set, and \(Q=S\) independently dominates it. The residual set after selecting \(Q\) is exactly \(X\). Moreover, among the vertices of \(Q\), the vertex \(x_i\) is nonadjacent only to \(s_i\). Thus all \(a\) nonneighbor regions are required to cover this residual set.

Nevertheless,
\[
\gamma(H_a)=a.
\]
Indeed, each \(x_i\) can be dominated only by \(p_i\) or by itself, giving the lower bound \(a\), while \(X\) itself dominates all of \(H_a\).

Thus the separate treatment of the \(a\) regions can grossly overcount: arcs between different regions may permit a joint dominating set much smaller than the sum of dominating sets for the regions. Any polynomial proof along this route has to retain and exploit those cross-region arcs.

This example does not rule out choosing the initial acyclic set and \(Q\) more intelligently—in \(H_a\), \(X\) is already an independent dominating set—but it rules out a uniform claim that one of the \(a\) branches is always redundant for an arbitrary \(Q\).

---

## 5. A natural special case

Let \(\tau_{\mathrm{FVS}}(D)\) be the minimum size of a directed feedback vertex set. For every digraph,
\[
\gamma(D)\le \alpha(D)+\tau_{\mathrm{FVS}}(D).
\]
Indeed, if \(T\) is a feedback vertex set, then \(D-T\) is acyclic and hence has an independent dominating set of size at most \(\alpha(D-T)\le\alpha(D)\); adjoining \(T\) gives a dominating set of \(D\).

Consequently, the conjectured polynomial bound holds on every class for which the directed feedback vertex number is polynomially bounded in \(\alpha\). This does not settle the general case: cyclic blow-ups of a directed \(C_5\) by arbitrarily large transitive tournaments have independence number \(2\) but require deletion of an entire part to destroy all directed cycles, so their feedback vertex number is unbounded.

---

## 6. Remaining gap

The sharpened recurrence
\[
f(a)\le a\bigl(1+f(a-1)\bigr)
\]
still gives \(f(a)=2^{\Theta(a\log a)}\), far above every fixed power of \(a\). The only lossy step is replacing the joint residual set by \(a\) separately dominated nonneighbor subgraphs. The example \(H_a\) shows simultaneously that:

1. all \(a\) branches may be present, but
2. their cross-arcs may collapse their joint domination number.

I do not have a lemma controlling that joint domination polynomially, nor a construction with domination superpolynomial in \(\alpha\). Thus there is neither a proof nor a counterexample to Conjecture 3.5 here.