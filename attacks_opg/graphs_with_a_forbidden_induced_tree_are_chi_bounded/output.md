```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an explicit polynomial χ-bound after additionally excluding an induced K_{2,s}, but do not resolve the unrestricted conjecture.",
  "would_publish": false,
  "caveats": "The extra induced-biclique exclusion is essential to this argument; no novelty claim is made for the restricted result."
}
```

## 1. A restricted theorem

I do not prove or disprove the Gyárfás–Sumner conjecture. The following is a self-contained partial result: it applies to **every tree**, but imposes an additional forbidden induced subgraph. It yields a degeneracy bound, which is stronger than a chromatic bound.

All graphs below are finite and simple. Write \(N(v)\) and \(N[v]\) for open and closed neighborhoods. Recall that a graph is \(D\)-degenerate if every nonempty induced subgraph has a vertex of degree at most \(D\); such a graph is \((D+1)\)-colorable.

### Theorem
Let \(T\) be a tree with \(t\ge 3\) vertices and maximum degree \(\Delta\), and let \(s\ge 2\). Put
\[
q=\Delta-2,\qquad
a_T=2t-5+q(q-1).
\]
Define
\[
F_{T,s}(k)
=
k+qk(k-1)
+a_T\left(\binom{k+s-1}{s}-k\right).
\]
If a nonempty graph \(G\) has neither an induced \(T\) nor an induced \(K_{2,s}\), and \(\omega(G)=k\), then
\[
\operatorname{degeneracy}(G)\le F_{T,s}(k)-1,
\qquad
\chi(G)\le F_{T,s}(k).
\]

Thus, for fixed \(T,s\), the bound is polynomial of degree at most \(s\).

In particular, since \(K_{2,2}=C_4\), every \(T\)-free graph with no induced \(C_4\) satisfies the explicit quadratic bound
\[
\boxed{\;
\chi(G)\le
k+\bigl(2t-5+(\Delta-1)(\Delta-2)\bigr)\binom{k}{2}.
\;}
\]
Using \(\Delta\le t-1\), the coefficient can be replaced by \(t^2-3t+1\).

The cases \(|T|\le 2\) are trivial: excluding a single vertex permits only the empty graph, and excluding an edge permits only edgeless graphs.

## 2. A counting lemma

The useful additional parameter is the number of common neighbors of a nonadjacent pair.

### Lemma 1
Suppose \(H\) has clique number at most \(r\), and every two nonadjacent vertices have at most \(c\) common neighbors. If \(\alpha(H)\le b\), then
\[
|V(H)|\le br+c\binom b2.
\]

#### Proof
Take a maximum stable set
\[
S=\{v_1,\ldots,v_\ell\},\qquad \ell\le b.
\]
For each \(i\), let
\[
U_i=\{v_i\}\cup
\{x\notin S:N(x)\cap S=\{v_i\}\}.
\]
Each \(U_i\) is a clique. Indeed, if two vertices \(x,y\in U_i\setminus\{v_i\}\) were nonadjacent, replacing \(v_i\) by \(x,y\) would enlarge \(S\). Hence \(|U_i|\le r\).

By maximality of \(S\), every remaining vertex has at least two neighbors in \(S\). The number of such vertices is at most
\[
\sum_{1\le i<j\le\ell}|N(v_i)\cap N(v_j)|
\le c\binom{\ell}{2}.
\]
Consequently,
\[
|V(H)|\le \ell r+c\binom{\ell}{2}
\le br+c\binom b2.
\]
The empty-graph case is immediate. \(\square\)

## 3. An induced-tree embedding lemma

The next lemma supplies the main mechanism. Its local degeneracy assumption will later be obtained by induction on clique number.

### Lemma 2
Let \(T,t,\Delta,q\) be as above. Let \(k\ge2\), and let \(c,d\) be nonnegative integers. Set
\[
L=c(t-3)+q(k-1)+c\binom q2+1.
\]
Suppose a nonempty graph \(G\) satisfies:

1. \(\omega(G)\le k\);
2. every nonadjacent pair has at most \(c\) common neighbors;
3. \(G[N(v)]\) is \(d\)-degenerate for every vertex \(v\);
4. \(\delta(G)\ge d+2L+c\).

Then \(G\) contains an induced copy of \(T\).

### Proof

Call a neighbor \(z\) of \(x\) **forward from \(x\)** if
\[
|N(z)\setminus N[x]|\ge L.
\]

We first establish that sufficiently large private neighborhoods contain many forward neighbors.

#### Claim
Fix \(x\). Let either

- \(P=N(x)\), or
- \(P=N(x)\setminus N[p]\), where \(p\) is a neighbor of \(x\).

If \(|P|\ge L\), then \(P\) contains at least \(L\) vertices forward from \(x\).

Let \(A\) be the forward vertices in \(P\), and suppose \(|A|\le L-1\). Put \(B=P\setminus A\), which is nonempty.

For \(z\in B\), there are at most:

- \(L-1\) neighbors outside \(N[x]\);
- one neighbor equal to \(x\);
- \(L-1\) neighbors in \(A\);
- \(c\) neighbors in \(N(x)\setminus P\).

The last assertion is automatic if \(P=N(x)\). Otherwise, \(z\) is nonadjacent to \(p\), and
\[
N(x)\setminus P=N(x)\cap N[p].
\]
Every neighbor of \(z\) in this set is a common neighbor of \(z,p\), of which there are at most \(c\).

It follows that every \(z\in B\) has
\[
\deg_{G[B]}(z)
\ge \delta(G)-(L-1)-1-(L-1)-c
\ge d+1.
\]
But \(B\subseteq N(x)\), contradicting the \(d\)-degeneracy of \(G[N(x)]\). This proves the claim.

#### Constructing the induced tree

Root \(T\) at a leaf. Every vertex then has at most
\[
\Delta-1=q+1
\]
children, including the root, which has one child.

We build the induced copy by adding **all children of a vertex at once**. Maintain the additional invariant that every selected parent–child edge \(px\) satisfies
\[
|N(x)\setminus N[p]|\ge L.
\]

Start with any vertex as the root. Suppose an already embedded vertex \(x\) is to receive its children.

- If \(x\) is the root, the current embedded set consists only of \(x\); take \(P=N(x)\).
- Otherwise let \(p\) be its parent and take
  \[
  P=N(x)\setminus N[p].
  \]
  The invariant guarantees \(|P|\ge L\).

In the root case, \(|P|\ge L\) follows from the minimum-degree hypothesis. By the claim, \(P\) contains a set \(A\) of at least \(L\) forward neighbors of \(x\).

Let \(S\) be the current embedded vertex set. Since \(x\) has not previously been expanded, its only neighbor in \(S\) is its parent, if it has one. Thus every other vertex \(w\in S\setminus\{x,p\}\) is nonadjacent to \(x\). Each such \(w\) excludes at most \(c\) candidates in \(A\), because \(A\subseteq N(x)\).

Since at least one vertex of \(T\) remains to be added,
\[
|S\setminus\{x,p\}|\le t-3
\]
in the nonroot case. In the root case there are no such vertices. Removing from \(A\) all candidates adjacent to these old vertices leaves at least
\[
L-c(t-3)
=
q(k-1)+c\binom q2+1
\]
candidates.

These candidates lie in \(N(x)\), so their induced subgraph has clique number at most \(k-1\). It also inherits the common-neighbor bound \(c\). Lemma 1 therefore guarantees a stable set of size at least \(q+1\).

Choose as many vertices from this stable set as \(x\) has children. They:

- are mutually nonadjacent;
- are adjacent to \(x\);
- have no other neighbors in the old embedded set;
- are forward from \(x\), preserving the invariant.

Continuing until all vertices of \(T\) have been embedded produces the required induced copy. \(\square\)

## 4. Proof of the polynomial bound

### Bounding nonadjacent codegrees

Fix \(s\ge2\), and define
\[
c_k=\binom{k+s-2}{s-1}-1.
\]
If \(G\) has clique number at most \(k\) and no induced \(K_{2,s}\), every nonadjacent pair has at most \(c_k\) common neighbors.

Indeed, for nonadjacent \(x,y\), put
\[
H=G[N(x)\cap N(y)].
\]
Then:

- \(\omega(H)\le k-1\), because any clique in \(H\), together with \(x\), is a larger clique in \(G\);
- \(\alpha(H)\le s-1\), because \(s\) stable common neighbors, together with \(x,y\), induce \(K_{2,s}\).

The elementary Ramsey bound
\[
R(k,s)\le\binom{k+s-2}{s-1}
\]
therefore gives \(|V(H)|\le c_k\). This Ramsey bound follows by induction from
\[
R(a,b)\le R(a-1,b)+R(a,b-1)
\]
and \(R(1,b)=R(a,1)=1\).

### Induction on clique number

Define
\[
D_1=0
\]
and, for \(k\ge2\),
\[
D_k
=
D_{k-1}+a_Tc_k+2q(k-1)+1.
\]
I claim that every graph with neither an induced \(T\) nor an induced \(K_{2,s}\), and with clique number at most \(k\), is \(D_k\)-degenerate.

The case \(k=1\) is immediate.

Assume the claim for \(k-1\), and let \(J\) be any nonempty induced subgraph of such a graph \(G\). Every neighborhood \(J[N_J(v)]\):

- has clique number at most \(k-1\);
- still excludes induced \(T\) and induced \(K_{2,s}\).

It is therefore \(D_{k-1}\)-degenerate by induction. Also, every nonadjacent pair in \(J\) has at most \(c_k\) common neighbors.

Apply Lemma 2 with \(d=D_{k-1}\), \(c=c_k\), and
\[
L=c_k(t-3)+q(k-1)+c_k\binom q2+1.
\]
The definitions give
\[
2L+c_k-1
=
a_Tc_k+2q(k-1)+1.
\]
Consequently,
\[
D_k+1=D_{k-1}+2L+c_k.
\]
If \(\delta(J)\ge D_k+1\), Lemma 2 would give an induced \(T\) in \(J\), a contradiction. Hence \(\delta(J)\le D_k\).

Since this holds for every nonempty induced \(J\), the graph \(G\) is \(D_k\)-degenerate.

Finally,
\[
\sum_{j=2}^k c_j
=
\sum_{j=2}^k
\left(\binom{j+s-2}{s-1}-1\right)
=
\binom{k+s-1}{s}-k.
\]
Summing the recurrence yields
\[
D_k
=
(k-1)+qk(k-1)
+a_T\left(\binom{k+s-1}{s}-k\right)
=
F_{T,s}(k)-1.
\]
Greedy coloring proves the theorem.

For \(s=2\),
\[
\binom{k+1}{2}-k=\binom{k}{2},
\qquad
qk(k-1)=2q\binom{k}{2},
\]
and
\[
a_T+2q
=
2t-5+(\Delta-1)(\Delta-2),
\]
giving the stated quadratic bound.

## 5. The gap to the original conjecture

The indispensable extra input is a **cardinality bound on common neighborhoods of nonadjacent vertices**. It is used twice:

1. to show that a private neighborhood contains many forward neighbors;
2. to avoid unwanted edges to previously embedded branches.

No such bound follows merely from excluding a tree and bounding the clique number. For example, \(K_{n,n}\) is \(P_4\)-free and satisfies
\[
\omega(K_{n,n})=\chi(K_{n,n})=2,
\]
but two vertices in the same part have \(n\) common neighbors. In fact, every non-star tree contains an induced \(P_4\), so these complete bipartite graphs are \(T\)-free for every non-star tree \(T\).

Thus the additional hypothesis cannot simply be deduced from \(T\)-freeness. Nor can it safely be enforced by deleting edges: induced-\(T\)-freeness is not preserved under edge deletion.

The argument therefore establishes a polynomially bounded restricted class, but supplies neither a proof nor a counterexample for the unrestricted Gyárfás–Sumner conjecture.