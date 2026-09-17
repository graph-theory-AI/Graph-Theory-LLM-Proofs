```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Triangle-free graphs are reconstructible, and the random-graph failure probability admits the stronger bound 2^{-3n^2/16+O(n log n)}.",
  "would_publish": false,
  "caveats": "The general case n divisible by four remains unresolved; novelty of these partial results has not been verified."
}
```

# Partial results

I interpret the switching deck as a **multiset**, with one card for each vertex.

I do not obtain a complete proof or a counterexample. I obtain three partial results:

1. **Every triangle-free graph on at least five vertices is switching-reconstructible.** The same holds for complements of triangle-free graphs.
2. In the unresolved range \(n=4k\ge 8\), a graph is reconstructible if its deck contains an \(r\)-regular graph with
   \[
   r\notin\{2k-1,2k\}.
   \]
3. For \(G\sim G(n,1/2)\),
   \[
   \Pr(G\text{ is not switching-reconstructible})
   \le 2^{-3n^2/16+O(n\log n)}.
   \]
   Thus the previous attempt’s linear-exponent probability estimate can be replaced by a **quadratic-exponent** estimate.

I rechecked and rederive below the elementary double-switch lemmas and the cube-eigenfunction bound used from the previous attempt. The improvement in the probability estimate comes from a permutation-group argument: a counterexample forces a switching-class automorphism moving at least \(n/2-2\) vertices.

No claim of literature novelty is made.

## 1. Elementary consequences of a common deck

For \(S\subseteq V(G)\), let \(G^S\) denote switching the cut between \(S\) and its complement. Thus
\[
G^S=G^{V(G)\setminus S},\qquad
(G^S)^T=G^{S\triangle T}.
\]

### Edge counts and degrees

If \(G\) has \(n\) vertices and \(m\) edges, then
\[
e(G^{\{v\}})=m+n-1-2d_G(v).
\]
Consequently,
\[
\sum_v e(G^{\{v\}})
=(n-4)m+n(n-1).
\]
For \(n\ne4\), the switching deck therefore determines \(m\), and then determines the degree multiset.

### Common-card lemma

**Lemma 1.** If \(G,H\) have the same switching deck, then for every \(v\in V(G)\), either \(H\cong G\), or
\[
H\cong G^{\{u,v\}}
\]
for some \(u\ne v\).

**Proof.** Match \(G^{\{v\}}\) with a card \(H^{\{w\}}\). Under an isomorphism from that card to \(G^{\{v\}}\), let \(u\) be the image of \(w\). Undoing its switch gives
\[
H\cong (G^{\{v\}})^{\{u\}}.
\]
If \(u=v\), this is \(G\); otherwise it is the asserted double switch. ∎

When \(n\ge5\), a double switch arising in this way must preserve both the edge count and the degree multiset. Edge-count preservation gives
\[
d_G(u)+d_G(v)-2\mathbf1_{uv\in E(G)}=n-2. \tag{1}
\]

### Degree preservation under a double switch

For distinct \(u,v\), put
\[
C=N(u)\cap N(v),
\qquad
Z=V(G)\setminus\bigl(N(u)\cup N(v)\cup\{u,v\}\bigr).
\]

**Lemma 2.** If \(G^{\{u,v\}}\) has the same degree multiset as \(G\), then
\[
|C|=|Z|,
\qquad
\{d(c):c\in C\}=\{d(z)+2:z\in Z\}, \tag{2}
\]
where the second equality is a multiset equality.

If \(C=Z=\varnothing\), then \(G^{\{u,v\}}\cong G\).

**Proof.** Equality of edge counts gives (1), equivalently \(|C|=|Z|\). Under that equation, \(u,v\) exchange degrees. Each vertex of \(C\) loses two neighbors, each vertex of \(Z\) gains two, and all other degrees remain unchanged.

Writing the resulting equality of degree polynomials and factoring \(z^2-1\) gives the multiset equality in (2).

If \(C=Z=\varnothing\), every other vertex is adjacent to exactly one of \(u,v\). Switching \(\{u,v\}\) then has exactly the same effect as transposing \(u,v\). ∎

## 2. Triangle-free graphs

**Theorem 3.** Every triangle-free graph on at least five vertices is switching-reconstructible. The same holds if its complement is triangle-free.

**Proof.** Let \(G\) be triangle-free, and choose a vertex \(v\) of minimum degree \(\delta\). Suppose a nonisomorphic graph \(H\) has the same deck.

By Lemma 1,
\[
H\cong G^{\{u,v\}}
\]
for some \(u\ne v\). This double switch preserves the degree multiset. Use the sets \(C,Z\) from Lemma 2 and write
\[
|C|=|Z|=k.
\]
If \(k=0\), Lemma 2 already gives an isomorphism, a contradiction. Thus \(k>0\).

Because \(G\) is triangle-free, \(u,v\) cannot be adjacent. Define the two exclusive-neighbor sets
\[
U=N(u)\setminus C,\qquad V=N(v)\setminus C.
\]
The vertices other than \(u,v\) are partitioned into \(C,Z,U,V\).

Triangle-freeness implies that there are no edges inside \(C\), from \(C\) to \(U\), or from \(C\) to \(V\). Hence
\[
\sum_{c\in C}d(c)=2k+e(C,Z).
\]
On the other hand,
\[
\sum_{z\in Z}d(z)
=e(C,Z)+e(Z,U\cup V)+2e(Z).
\]
The degree-multiset identity (2) says that these sums differ by exactly \(2k\). Therefore
\[
e(Z,U\cup V)=e(Z)=0. \tag{3}
\]

In particular, every vertex of \(Z\) has all its neighbors in \(C\). Since \(v\) has minimum degree,
\[
\delta\le d(z)\le k\le d(v)=\delta
\qquad(z\in Z).
\]
Thus
\[
k=\delta,\qquad V=\varnothing,
\]
and \(G[C,Z]\) is complete bipartite.

We can now exhibit an isomorphism from \(G\) to \(G^{\{u,v\}}\):

- interchange \(u,v\);
- interchange \(C,Z\) using any bijection between them;
- fix \(U\).

Indeed, the only edges incident with \(C\cup Z\), apart from the complete bipartite graph between those sets, are the edges from \(u,v\) to \(C\). Equation (3) excludes additional edges from \(Z\), and triangle-freeness excludes additional edges from \(C\). Switching \(\{u,v\}\) changes precisely these attachments in the way prescribed by the permutation.

This contradicts \(H\not\cong G\).

Finally, complementation commutes with switching, so reconstruction of \(G\) is equivalent to reconstruction of \(\overline G\). ∎

## 3. A regular-card criterion

A regular card can be useful even when the unknown graph itself is far from regular.

**Theorem 4.** Let \(n=4k\ge8\), and suppose the switching deck of \(G\) contains an \(r\)-regular graph \(R\). If
\[
r\le 2k-2
\quad\text{or}\quad
r\ge 2k+1,
\]
then \(G\) is switching-reconstructible.

**Proof.** Put \(q=n/2\). By complementation it suffices to consider \(r\le q-2\).

Since \(R\) is a card, we may write
\[
G\cong R^{\{v\}}.
\]
Any graph \(H\) with the same deck also has \(R\) as a card, so
\[
H\cong R^{\{w\}}
\]
for some \(w\in V(R)\).

In \(R^{\{v\}}\), the switched vertex has degree
\[
n-1-r\ge q+1,
\]
whereas every other vertex has degree \(r-1\) or \(r+1\), at most \(q-1\). Thus the switched vertex is the unique maximum-degree vertex. Consequently,
\[
R^{\{v\}}\cong R^{\{w\}}
\quad\Longleftrightarrow\quad
v,w\text{ lie in the same }\operatorname{Aut}(R)\text{-orbit}. \tag{4}
\]

Assume for a contradiction that \(G,H\) are nonisomorphic.

### Case 1: \(r\le q-3\)

For any two vertices \(x,y\ne v\) in \(G=R^{\{v\}}\),
\[
d_G(x)+d_G(y)-2\mathbf1_{xy\in E(G)}
\le 2r+2\le n-4.
\]
Such a pair cannot satisfy (1).

Applying Lemma 1 at any \(x\ne v\), its double-switch partner must therefore be \(v\). Hence
\[
H\cong R^{\{x\}}\qquad(x\ne v).
\]
The symmetric argument gives
\[
G\cong R^{\{x\}}\qquad(x\ne w).
\]
Choosing \(x\notin\{v,w\}\) contradicts \(G\not\cong H\).

### Case 2: \(r=q-2\)

If \(x\in N_R(v)\), then \(d_G(x)=r-1\). For every \(y\ne v\),
\[
d_G(x)+d_G(y)-2\mathbf1_{xy\in E(G)}
\le 2r=n-4.
\]
Again Lemma 1 forces
\[
H\cong R^{\{x\}}\qquad(x\in N_R(v)).
\]

Let \(A,B\) be the distinct \(\operatorname{Aut}(R)\)-orbits of \(v,w\). By (4),
\[
N_R(A)\subseteq B.
\]
Applying the same argument to \(H\) gives
\[
N_R(B)\subseteq A.
\]

Thus \(R[A\cup B]\) is an \(r\)-regular bipartite graph with no edges to the remaining vertices. Since \(r>0\), its parts have equal size, say
\[
|A|=|B|=t.
\]
Moreover,
\[
q-2=r\le t\le q.
\]

The bipartite complement between \(A,B\) is therefore regular of degree
\[
t-r\in\{0,1,2\}.
\]
Every regular bipartite graph of degree \(0,1,\) or \(2\) has an automorphism interchanging its parts:

- degree \(0\): choose any bijection between the parts;
- degree \(1\): interchange the endpoints of every matching edge;
- degree \(2\): its components are even cycles, each admitting a part-interchanging automorphism.

This gives a part-interchanging automorphism of \(R[A\cup B]\). Extending it by the identity outside \(A\cup B\) produces an automorphism of \(R\) taking a vertex of \(A\) into \(B\), a contradiction. ∎

In particular, a counterexample with a regular card must have a card of one of the two central degrees \(n/2-1,n/2\). A vertex-transitive regular card also immediately guarantees reconstruction, since all its single-vertex switchings are isomorphic.

## 4. A quadratic-exponent random-graph bound

The main quantitative improvement uses a lower bound from the previous attempt, followed by a new group-action estimate.

### 4.1 A counterexample has a large self-switching orbit

Define
\[
\rho(G)=\frac12
\left|\{S\subseteq V(G):G^S\cong G\}\right|.
\]
This counts distinct labeled switchings isomorphic to \(G\), identifying complementary switching sets.

**Lemma 5.** If nonisomorphic \(G,H\) have the same switching deck, then \(4\mid n\) and
\[
\rho(G),\rho(H)\ge 2^{n/2-2}. \tag{5}
\]

**Proof.** By a common card, relabel \(H\) so that it belongs to the labeled switching class of \(G\).

On the cube \(\{0,1\}^n\), let
\[
A=\{x:G^x\cong G\},\qquad
B=\{x:G^x\cong H\},
\]
and write \(a=|A|,\ b=|B|\). Define
\[
f=\frac{\mathbf1_A}{a}-\frac{\mathbf1_B}{b}.
\]

Partition the cube by the isomorphism type of \(G^x\). This partition is equitable for cube adjacency: if \(C,D\) are classes, the number \(p_{C,D}\) of neighbors in \(D\) of a point of \(C\) is the multiplicity of type \(D\) in the deck of type \(C\). Also,
\[
|C|p_{C,D}=|D|p_{D,C}.
\]
Equality of the decks of \(G,H\) therefore implies, for the cube adjacency operator \(L\),
\[
Lf=0. \tag{6}
\]

The cube characters
\[
\chi_U(x)=(-1)^{|U\cap x|}
\]
have eigenvalues \(n-2|U|\). Thus \(n\) is even and \(f\) has Fourier support entirely in degree \(q=n/2\).

Furthermore, \(f(x+\mathbf1)=f(x)\), because complementary switching sets give the same graph. A degree-\(q\) character changes by \((-1)^q\) under this translation. Hence \(q\) is even, proving \(4\mid n\).

For a degree-\(q\) cube eigenfunction,
\[
\sum_{d(x,y)=j}f(y)=K_j(q)f(x),
\]
where
\[
\sum_{j=0}^nK_j(q)z^j=(1-z)^q(1+z)^q=(1-z^2)^q.
\]
Consequently,
\[
\sum_{j=0}^n|K_j(q)|=2^q.
\]
As \(\|f\|_1=2\), taking \(x\in A\) gives
\[
2\ge
\sum_j\left|\sum_{d(x,y)=j}f(y)\right|
=2^q/a.
\]
Thus \(a\ge2^{q-1}\), and similarly \(b\ge2^{q-1}\). Since \(a=2\rho(G)\) and \(b=2\rho(H)\), (5) follows. ∎

This also reproves the \(n\not\equiv0\pmod4\) result quoted in the question.

### 4.2 Large self-switching orbits force large permutation support

Let \(\mathcal T(G)\) be the collection of triples spanning an odd number of edges, and put
\[
\Gamma(G)=\operatorname{Aut}(\mathcal T(G)).
\]

Two labeled graphs have the same triple parities exactly when one is a switching of the other. Indeed, if their edgewise difference is \(c_{ij}\in\mathbb F_2\), equality of triple parities gives
\[
c_{ij}=c_{ir}+c_{jr}
\]
after fixing a vertex \(r\); hence the difference is a cut.

It follows that the \(\Gamma(G)\)-orbit of \(G\) consists exactly of its labeled switchings isomorphic to \(G\). In particular, that orbit has size \(\rho(G)\).

**Lemma 6.** Suppose \(0\le t\le n/2\) and \(\rho(G)\ge2^t\). Then \(\Gamma(G)\) contains a permutation moving at least \(t\) vertices.

**Proof.** Write \(\Gamma=\Gamma(G)\), and let \(c\) be its number of vertex orbits. The average support size of an element of \(\Gamma\) is
\[
n-c. \tag{7}
\]
This follows by summing, over the vertex orbits, the average number of fixed vertices.

If \(\Gamma\) has no globally fixed vertex, all its vertex orbits have size at least two. Thus \(c\le n/2\), and some element moves at least \(n/2\ge t\) vertices.

Now suppose that \(\Gamma\) fixes a vertex \(r\). Switch \(G\) to a graph \(F\) in which \(r\) is isolated, and write
\[
G=F^S,\qquad r\notin S.
\]
Every element of \(\Gamma\) is an automorphism of \(F\): the edges of \(F-r\) are precisely the odd triple parities involving \(r\).

Let the vertex orbits of \(\Gamma\) have sizes \(s_1,\ldots,s_c\), and put \(k_i=|S\cap O_i|\). Then
\[
\rho(G)=|\Gamma S|
\le\prod_{i=1}^c\binom{s_i}{k_i}
\le\prod_{i=1}^c2^{s_i-1}
=2^{n-c}. \tag{8}
\]
Here switching sets in this orbit all avoid \(r\), so no two are identified by complementation.

Equations (7) and (8) show that some element has support at least
\[
n-c\ge\log_2\rho(G)\ge t.
\]
∎

Combining Lemmas 5 and 6 gives the important necessary condition
\[
G\text{ not reconstructible}
\quad\Longrightarrow\quad
\Gamma(G)\text{ contains a permutation moving at least }n/2-2
\text{ vertices}. \tag{9}
\]

### 4.3 Counting such symmetries in a random graph

**Theorem 7.** For \(4\mid n,\ n\ge8\), define
\[
V_n=
\sum_{s=n/2-2}^{n}
(2n)^s\,2^{-s(2n-s-2)/4}.
\]
Then
\[
\Pr_{G\sim G(n,1/2)}
(G\text{ is not switching-reconstructible})
\le \min\{1,V_n\}, \tag{10}
\]
and consequently
\[
\Pr(G\text{ is not switching-reconstructible})
\le 2^{-3n^2/16+O(n\log n)}. \tag{11}
\]
For \(4\nmid n\), the probability is zero.

**Proof.** Fix a permutation \(\pi\) moving exactly \(s\) vertices. Membership in \(\Gamma(G)\) means that
\[
\pi(G)=G^S
\]
for some cut \(S\).

There are at most \(2^s\) potentially feasible cuts, modulo complementation. If \(\pi\) has fixed vertices, all their switching bits must agree whenever there are at least two; normalize their common bit to zero. With one fixed vertex, normalize its bit to zero. With no fixed vertices, the bound \(2^s\) is immediate.

Let \(N=\binom n2\), and let \(c(\pi)\) denote the number of orbits of \(\pi\) on unordered pairs. For fixed \(\pi,S\), the equation \(\pi(G)=G^S\) is either inconsistent, or leaves exactly one free edge bit per pair orbit. Its probability is at most
\[
2^{-(N-c(\pi))}.
\]

At most
\[
\binom{n-s}{2}+\frac s2
\]
unordered pairs are fixed by \(\pi\). All other pair orbits have size at least two, so
\[
N-c(\pi)\ge\frac{s(2n-s-2)}4.
\]
There are at most \(n^s\) permutations with support size \(s\). Hence
\[
\Pr\bigl(\exists\pi\in\Gamma(G):|\operatorname{supp}\pi|=s\bigr)
\le (2n)^s\,2^{-s(2n-s-2)/4}.
\]
Equation (9) and a union bound prove (10).

For the asymptotic estimate, put \(s_0=n/2-2\). On \(s_0\le s\le n\),
\[
s(2n-s-2)\ge s_0(2n-s_0-2)
=\frac{3n^2}{4}-3n.
\]
Therefore the explicit, slightly looser estimate
\[
V_n\le
n(2n)^n\,2^{-3n^2/16+3n/4}
\]
suffices to prove (11). ∎

## 5. What remains unresolved

These arguments do not exclude every graph of order \(4k\ge8\). They show that a counterexample must, among other things,

- contain a triangle and an independent triple;
- have a switching-class automorphism moving at least \(n/2-2\) vertices;
- if it has a regular card, have such a card of degree \(n/2-1\) or \(n/2\), rather than a noncentral degree.

The large-symmetry condition is extremely restrictive probabilistically, yielding the quadratic-exponent bound, but it is not a deterministic contradiction. Highly symmetric switching classes certainly exist, and the arguments do not classify all possible equal-deck pairs inside them.

Thus the original conjecture remains unproved here.