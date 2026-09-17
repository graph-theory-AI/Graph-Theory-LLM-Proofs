```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A parity-counting argument gives rigorous density, symmetry, and local-completion criteria for edge reconstruction, but does not resolve the general conjecture.",
  "would_publish": false,
  "caveats": "No general proof or counterexample is obtained, and no novelty is claimed for these partial results."
}
```

# A parity-counting attack

All graphs below are finite and simple. Deleting an edge retains every vertex, including newly isolated vertices. Write
\[
\mathcal D_E(G)=\{\!\{G-e:e\in E(G)\}\!\}
\]
for the edge deck.

I will derive an exact counting identity that any counterexample must satisfy. It gives several sufficient conditions for reconstruction, including a factorial-size bound and a local unique-completion criterion.

## 1. The partial result

Let \(G\) have \(m\ge4\) edges. Let \(Q\) be the graph obtained by removing its isolated vertices, and put
\[
t=|V(Q)|,\qquad a=|\operatorname{Aut}(Q)|.
\]
List the degrees of \(Q\) as
\[
d_1\ge d_2\ge\cdots\ge d_t\ge1.
\]

Fix a labeling of \(Q\) on \([t]\). For \(S\subseteq E(Q)\), let \(C_Q(S)\) denote the number of distinct graphs on \([t]\) that are isomorphic to \(Q\) and contain every edge of \(S\).

**Partial theorem.** If \(G\) is not edge-reconstructible, then both of the following hold:

1. For every \(1\le i\le t\),
   \[
   d_i+d_{t+1-i}\le t-1. \tag{1}
   \]

2. For every proper subset \(S\subsetneq E(Q)\),
   \[
   C_Q(S)\ge 2^{m-|S|-1}. \tag{2}
   \]

Consequently, each of the following is sufficient for edge reconstruction:
\[
m>\frac{t(t-1)}4,
\qquad\text{or}\qquad
2^{m-1}>\frac{t!}{a}.
\]
The argument also proves reconstruction whenever the nonisolated core is regular or has a universal vertex.

The proof follows.

## 2. The degree multiset, including isolated vertices, is reconstructible

The deck gives both \(m\), its number of cards, and \(n=|V(G)|\), the order of any card.

Define the degree polynomial
\[
D_G(x)=\sum_{v\in V(G)}x^{d_G(v)}.
\]
A vertex of degree \(d\) has degree \(d-1\) in exactly \(d\) cards and degree \(d\) in the other \(m-d\) cards. Therefore
\[
\sum_{e\in E(G)}D_{G-e}(x)
=mD_G(x)+(1-x)D'_G(x). \tag{3}
\]

Suppose \(G,H\) have the same edge deck. Setting \(R=D_G-D_H\), equation (3) gives
\[
mR+(1-x)R'=0.
\]
Expanding around \(x=1\), or comparing coefficients, shows that
\[
R(x)=c(x-1)^m
\]
for an integer \(c\).

If \(c\ne0\), the coefficient of \(x^{m-1}\) has absolute value at least \(m\). But a graph with \(m\ge4\) edges has at most
\[
\left\lfloor\frac{2m}{m-1}\right\rfloor=2
\]
vertices of degree \(m-1\). The corresponding coefficient of \(D_G-D_H\) thus has absolute value at most \(2\), a contradiction. Hence
\[
D_G=D_H. \tag{4}
\]

In particular, the number \(r\) of isolated vertices is determined. Removing **exactly \(r\)** isolated vertices from every card gives the edge deck of the nonisolated core. This is legitimate even when a card has additional isolated vertices created by the deletion.

Thus any hypothetical nonisomorphic mate of \(G\) gives a nonisomorphic mate of \(Q\), with the same positive degree multiset.

The restriction \(m\ge4\) matters here: \(K_{1,3}\) and \(K_3\sqcup K_1\) have the same three-card edge deck but different degree multisets.

## 3. An exact overlap identity

After removing original isolated vertices, suppose that \(G,H\) are nonisomorphic graphs on \([t]\), each with \(m\) edges, having the same edge deck. Put
\[
E=E(G),\qquad a=|\operatorname{Aut}(G)|.
\]

For \(X\in\{G,H\}\) and \(S\subseteq E\), define
\[
T_X(S)=
\bigl|\{\pi\in S_t:S\subseteq E(\pi X)\}\bigr|.
\]
These counts use permutations, rather than distinct labeled images.

### Proper-subgraph counts agree

For \(|S|<m\),
\[
\sum_{e\in E(X)}T_{X-e}(S)
=(m-|S|)T_X(S). \tag{5}
\]
Indeed, a permutation counted by \(T_X(S)\) remains valid after deleting precisely those edges outside the copy of \(S\), of which there are \(m-|S|\).

The left side of (5) is determined by the edge deck. Consequently,
\[
T_G(S)=T_H(S)\qquad(S\subsetneq E). \tag{6}
\]
This argument also applies when the spanning graph with edge set \(S\) has isolated vertices.

For \(S=E\), equal edge counts and nonisomorphism give
\[
T_G(E)=a,\qquad T_H(E)=0. \tag{7}
\]

### Inclusion–exclusion turns containment into exact intersection

Define
\[
Z_X(S)=
\bigl|\{\pi\in S_t:E(\pi X)\cap E=S\}\bigr|.
\]
Then
\[
T_X(S)=\sum_{R:\,S\subseteq R\subseteq E}Z_X(R).
\]
By inclusion–exclusion,
\[
Z_G(S)-Z_H(S)
=\sum_{R:\,S\subseteq R\subseteq E}
(-1)^{|R|-|S|}\bigl(T_G(R)-T_H(R)\bigr).
\]
All terms except \(R=E\) vanish by (6). Using (7), we obtain
\[
\boxed{
Z_G(S)-Z_H(S)=(-1)^{m-|S|}a
\qquad(S\subseteq E).
} \tag{8}
\]

In particular:

- if \(m-|S|\) is even, then \(Z_G(S)\ge a\);
- if \(m-|S|\) is odd, then \(Z_H(S)\ge a\).

Thus a hypothetical counterexample forces a relabeling of \(G\) realizing **every even-codimension intersection pattern** with its own edge set.

## 4. Deriving the two necessary conditions

### 4.1. The degree obstruction

Taking \(S=\varnothing\) in (8) shows that at least one of \(G,H\) has a relabeling \(J\) edge-disjoint from \(G\). By Section 2, \(J\) has the same degree multiset as \(G\).

Suppose that, for some \(i\),
\[
d_i+d_{t+1-i}>t-1.
\]
There are at least \(i\) vertices of \(G\) having degree at least \(d_i\), and at least \(t+1-i\) vertices of \(J\) having degree at least \(d_{t+1-i}\). These two vertex sets intersect. At a vertex in their intersection,
\[
d_G(v)+d_J(v)>t-1,
\]
which is impossible for two edge-disjoint simple graphs on \([t]\).

This proves (1).

Summing (1) over all \(i\) yields
\[
4m=2\sum_{i=1}^t d_i\le t(t-1).
\]
Hence
\[
\boxed{m>\frac{t(t-1)}4\quad\Longrightarrow\quad G
\text{ is edge-reconstructible}.} \tag{9}
\]

Also, if the nonisolated core has a universal vertex, then
\[
d_1+d_t\ge(t-1)+1=t,
\]
contradicting (1). Such graphs are therefore edge-reconstructible.

### 4.2. The local counting obstruction

Fix \(S\subsetneq E\), and put \(q=m-|S|\ge1\). Exactly \(2^{q-1}\) supersets \(R\), with
\[
S\subseteq R\subseteq E,
\]
satisfy \(m-|R|\) even. Equation (8) gives
\[
T_G(S)=\sum_{R\supseteq S}Z_G(R)
\ge 2^{q-1}a.
\]
Every distinct labeled copy of \(G\) is produced by exactly \(a\) permutations, so
\[
C_G(S)=\frac{T_G(S)}a\ge2^{q-1}.
\]
This proves (2).

Taking \(S=\varnothing\), we have \(C_G(\varnothing)=t!/a\). Thus
\[
\boxed{
2^{m-1}>\frac{t!}{a}
\quad\Longrightarrow\quad
G\text{ is edge-reconstructible}.
} \tag{10}
\]
Equivalently, the sufficient condition is
\[
m>1+\log_2\!\left(\frac{t!}{a}\right).
\]
Even without using automorphisms, \(m>1+\log_2(t!)\) suffices.

## 5. Local completion certificates

Condition (2) is stronger than its special case \(S=\varnothing\).

### Unique completion after deleting two edges

Suppose that deleting two edges of \(G\) leaves a spanning subgraph \(F\) such that the only graph on the same labeled vertex set which

- contains \(F\), and
- is isomorphic to \(G\),

is \(G\) itself.

Then
\[
C_G(E(F))=1,
\]
whereas a nonreconstructible graph would require
\[
C_G(E(F))\ge 2^{m-(m-2)-1}=2.
\]
Therefore \(G\) is edge-reconstructible.

### Application: regular nonisolated cores

Suppose the core is \(r\)-regular.

If \(r=1\), it is a matching, and its degree multiset determines it.

If \(r\ge2\), choose two edges \(uv,uw\) incident with the same vertex, where \(v\ne w\), and let
\[
F=G-\{uv,uw\}.
\]
Any labeled copy of \(G\) containing \(F\) must be an \(r\)-regular completion of \(F\) by two edges. The degree deficits are:

- \(2\) at \(u\);
- \(1\) at each of \(v,w\);
- \(0\) everywhere else.

The only two-edge simple graph supplying these deficits consists of \(uv\) and \(uw\). Hence this completion is unique, and \(G\) is edge-reconstructible.

This covers every regular nonisolated core, connected or disconnected.

### A subgraph-count version

Let \(F\subseteq G\) have \(v\) vertices and \(k<m\) edges, and let \(s(F,G)\) count its copies as a not-necessarily-induced subgraph. For a fixed labeled copy with edge set \(S\),
\[
T_G(S)
=(t-v)!\,|\operatorname{Aut}(F)|\,s(F,G).
\]
Consequently,
\[
C_G(S)=
\frac{(t-v)!\,|\operatorname{Aut}(F)|\,s(F,G)}{a}.
\]
We obtain the sufficient condition
\[
\boxed{
(t-v)!\,|\operatorname{Aut}(F)|\,s(F,G)
<
2^{m-k-1}a
\quad\Longrightarrow\quad
G\text{ is edge-reconstructible}.
} \tag{11}
\]

For example, a uniquely occurring asymmetric spanning subgraph with at most \(m-2\) edges gives such a certificate. Uniqueness forces every automorphism of \(G\) to preserve that subgraph, so both automorphism groups are trivial and the left side of (11) equals \(1\).

## 6. The remaining gap

The inequalities above are necessary for a counterexample, not sufficient for one. They do not collectively settle all graphs.

This limitation can be seen explicitly on paths. Let \(G=P_t\), where \(t\ge5\) and \(m=t-1\). Its degree sequence satisfies (1), since every paired degree sum is at most \(4\le t-1\).

For any \(S\subsetneq E(P_t)\), let \(c=t-|S|\) be the number of components of the spanning forest \(([t],S)\), and let \(p\) be the number of its nontrivial components. A Hamiltonian path containing \(S\) is obtained by ordering the \(c\) path components and orienting their \(p\) nontrivial members, with global reversal counted twice. Therefore
\[
C_{P_t}(S)=c!\,2^{p-1}.
\]
Since \(c!\ge2^{c-1}\),
\[
C_{P_t}(S)\ge2^{c-2}
=2^{m-|S|-1}.
\]
Thus paths satisfy every inequality in the partial theorem.

Paths are nevertheless reconstructible: their degree multiset permits only one path component together with possible cycle components, and any such cycle would have fewer than \(m\) edges and would be detected by the proper-subgraph counts in (5).

So the nonnegativity bounds extracted from (8) are not an exhaustive reconstruction criterion. The exact overlap identity contains further information, but I have not shown how to turn it into a contradiction for an arbitrary hypothetical mate. No proof of the full conjecture or counterexample is obtained.