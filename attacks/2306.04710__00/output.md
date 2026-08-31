```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove necessary tournament and forest obstructions, completely classify singleton and acyclicity-forcing families, and give explicit bounds for several transitive-tournament/forest pairs.",
  "would_publish": false,
  "caveats": "Assumes induced subdigraphs in finite loopless oriented graphs; the general interaction between tournament obstructions and oriented forests remains open."
}
```

## 1. Conventions and summary

I use the convention appropriate to the source: all digraphs are finite oriented graphs, with no loops or digons, and “\(H\)-free” means no induced copy of \(H\).

For an oriented graph \(D\), let \(U(D)\) be its underlying undirected graph, and let
\[
a(D)=\max\{|X|:D[X]\text{ is acyclic}\}.
\]
Then
\[
\vec\chi(D)\ge \frac{|V(D)|}{a(D)}.
\]

The following partial results are established below.

1. **Necessary conditions.** If a finite family \(\mathcal F\) is \(\vec\chi\)-finite, then:
   - some member of \(\mathcal F\) has forest underlying graph;
   - the tournament members of \(\mathcal F\) bound the dichromatic number of tournaments.

2. **Singleton classification.** For a nonempty oriented graph \(H\), the singleton family \(\{H\}\) is \(\vec\chi\)-finite if and only if \(H\) is \(K_1\) or the one-arc tournament \(\vec K_2\).

3. **Exact classification of the bound-one case.** There is a finite, explicit criterion deciding whether every \(\mathcal F\)-free oriented graph is acyclic.

4. **Exact classification of bounded-order families.** The orders of all \(\mathcal F\)-free oriented graphs are bounded if and only if \(\mathcal F\) contains both an edgeless graph and a transitive tournament.

5. **Explicit positive cases.** If \(\mathcal F\) contains a transitive tournament together with an induced out-star, in-star, or \(K_1+\vec P_2\), then explicit Ramsey bounds on \(\vec\chi\) follow.

These do not settle the general classification.

---

## 2. Two unavoidable necessary conditions

Let
\[
\mathcal F_{\mathrm{tour}}
   =\{H\in\mathcal F: H\text{ is a tournament}\}.
\]

### Proposition 2.1: tournament restriction

If \(\mathcal F\) is \(\vec\chi\)-finite, then the class of
\(\mathcal F_{\mathrm{tour}}\)-free tournaments has bounded dichromatic number. In particular, \(\mathcal F_{\mathrm{tour}}\neq\varnothing\).

#### Proof

Every induced subdigraph of a tournament is a tournament. Hence, for every tournament \(T\),
\[
T\text{ is }\mathcal F\text{-free}
\quad\Longleftrightarrow\quad
T\text{ is }\mathcal F_{\mathrm{tour}}\text{-free}.
\]
Thus boundedness for all \(\mathcal F\)-free oriented graphs implies boundedness on this tournament subclass.

It remains to recall self-containedly that tournaments have unbounded dichromatic number. Choose a uniformly random tournament \(T_n\). A vertex set is acyclic precisely when it induces a transitive tournament. For a fixed ordered \(s\)-tuple, the probability that every arc points forward in that order is
\[
2^{-\binom{s}{2}}.
\]
Consequently,
\[
\Pr(a(T_n)\ge s)\le n^s2^{-\binom{s}{2}}.
\]
Taking \(s=\lceil 3\log_2 n\rceil\), the right side tends to zero. Therefore there are tournaments with
\[
a(T_n)<3\log_2 n+1,
\qquad
\vec\chi(T_n)\ge \frac{n}{3\log_2 n+1},
\]
which is unbounded. Hence \(\mathcal F_{\mathrm{tour}}\) cannot be empty. ∎

The second necessary condition follows from oriented graphs having simultaneously large undirected girth and large dichromatic number.

### Lemma 2.2: high-girth, high-dichromatic oriented graphs

For all integers \(g\ge3\) and \(k\ge1\), there exists an oriented graph \(D\) such that
\[
\operatorname{girth}(U(D))>g
\quad\text{and}\quad
\vec\chi(D)>k.
\]

#### Proof

For large \(n\), set
\[
p=n^{-1+1/(2g)}.
\]
Independently for each unordered vertex pair, put no arc with probability \(1-p\), and put either possible arc with probability \(p/2\) each.

Set
\[
s=\left\lceil\frac{n}{4k}\right\rceil.
\]
If a fixed \(s\)-set is acyclic, it admits a topological ordering. For a fixed ordered \(s\)-tuple, every pair must avoid the arc pointing backward, an event of probability
\[
(1-p/2)^{\binom{s}{2}}.
\]
Thus
\[
\Pr(a(D)\ge s)
 \le n^s(1-p/2)^{\binom{s}{2}}
 \le \exp\left(s\log n-\frac p2\binom{s}{2}\right).
\]
The positive term is \(O(n\log n)\), while the negative term has order
\[
p s^2=\Theta\!\left(n^{1+1/(2g)}\right).
\]
Hence this probability tends to zero.

Let \(X\) be the number of cycles of length at most \(g\) in \(U(D)\). For \(3\le\ell\le g\),
\[
\mathbb E[X_\ell]
 \le \frac{n^\ell p^\ell}{2\ell}
 =\frac{n^{\ell/(2g)}}{2\ell}.
\]
Therefore
\[
\mathbb E[X]=O_g(n^{1/2})=o(n),
\]
and by Markov's inequality, \(\Pr(X\ge n/2)=o(1)\).

Choose an outcome with \(a(D)<s\) and \(X<n/2\). Delete one chosen vertex from each short cycle. The resulting induced subdigraph \(D'\) has more than \(n/2\) vertices and underlying girth greater than \(g\). Moreover,
\[
a(D')\le a(D)<s,
\]
and, since \(a(D')\le s-1<n/(4k)\),
\[
\vec\chi(D')
 \ge \frac{|V(D')|}{a(D')}
 >\frac{n/2}{n/(4k)}
 =2k>k.
\]
∎

### Proposition 2.3: forest restriction

If a finite family \(\mathcal F\) is \(\vec\chi\)-finite, then some \(H\in\mathcal F\) has \(U(H)\) a forest.

#### Proof

Suppose instead that every \(U(H)\), \(H\in\mathcal F\), contains a cycle. Let
\[
m=\max_{H\in\mathcal F}|V(H)|.
\]
By Lemma 2.2, for every \(k\) there is an oriented graph \(D\) with
\[
\operatorname{girth}(U(D))>m,\qquad \vec\chi(D)>k.
\]
Every \(U(H)\) contains a cycle of length at most \(|V(H)|\le m\), so \(U(H)\) cannot occur even as a noninduced subgraph of \(U(D)\). Thus \(D\) is \(\mathcal F\)-free. Since \(k\) is arbitrary, \(\mathcal F\) is not \(\vec\chi\)-finite. ∎

Hence every nontrivial candidate family must simultaneously contain an oriented forest and enough tournaments to bound the tournament subclass.

---

## 3. Complete classification for singleton families

### Theorem 3.1

For a nonempty oriented graph \(H\), the singleton family \(\{H\}\) is \(\vec\chi\)-finite if and only if
\[
H=K_1
\quad\text{or}\quad
H=\vec K_2.
\]

#### Proof

If \(H=K_1\), the only \(H\)-free graph is the empty graph.

If \(H=\vec K_2\), an \(H\)-free oriented graph has no arcs and hence has dichromatic number at most one.

Conversely, suppose \(|V(H)|\ge3\).

- If \(H\) is not a tournament, every tournament is induced-\(H\)-free, and Proposition 2.1 supplies induced-\(H\)-free tournaments with unbounded dichromatic number.
- If \(H\) is a tournament, then \(U(H)\) contains a triangle. Proposition 2.3, or directly Lemma 2.2 with girth greater than \(|V(H)|\), gives induced-\(H\)-free oriented graphs with unbounded dichromatic number.

These exhaust all cases. ∎

Thus any genuinely nontrivial \(\vec\chi\)-finite family must have at least two members.

---

## 4. Exact classification of families forcing acyclicity

Call an oriented graph a **directed linear forest** if every component is a consistently directed path. Isolated vertices count as one-vertex directed paths.

For such a graph \(L\), let \(\kappa(L)\) denote its number of components. Given a finite family \(\mathcal F\), define
\[
\tau(\mathcal F)
 =\min\bigl\{|V(L)|+\kappa(L):
              L\in\mathcal F,\ L\text{ is a directed linear forest}\bigr\},
\]
with \(\tau(\mathcal F)=\infty\) if no such member exists.

### Theorem 4.1

Every \(\mathcal F\)-free oriented graph is acyclic if and only if:

1. \(\tau(\mathcal F)<\infty\), and
2. for every integer \(n\) with
   \[
   3\le n<\tau(\mathcal F),
   \]
   the directed cycle \(\vec C_n\) contains an induced copy of some member of \(\mathcal F\).

#### Proof

First observe that every cyclic oriented graph contains an induced directed cycle. Indeed, choose a shortest directed cycle. Any chord, in whichever direction it is oriented, combines with one of the two directed portions of the cycle to form a shorter directed cycle.

Next, a proper induced subdigraph of \(\vec C_n\) is a directed linear forest: its components are the selected consecutive runs around the cycle.

If \(L\) is a directed linear forest with \(s\) vertices and \(c\) components, then \(L\) embeds inducedly in every \(\vec C_n\) with
\[
n\ge s+c.
\]
Place the \(c\) directed-path components in \(c\) consecutive runs, separated cyclically by at least one unused vertex.

Now suppose the two stated conditions hold, and choose \(L\in\mathcal F\) attaining \(\tau(\mathcal F)\). For every \(n\ge\tau(\mathcal F)\), the cycle \(\vec C_n\) contains \(L\); for \(3\le n<\tau(\mathcal F)\), the second condition gives some forbidden induced subdigraph. Thus every directed cycle contains a member of \(\mathcal F\). Since every cyclic oriented graph contains an induced directed cycle, every \(\mathcal F\)-free graph is acyclic.

Conversely, suppose every \(\mathcal F\)-free graph is acyclic. Then each \(\vec C_n\) contains a member of \(\mathcal F\). Taking \(n\) larger than every order appearing in \(\mathcal F\), such a member is a proper induced subgraph of \(\vec C_n\), and therefore is a directed linear forest. Thus \(\tau(\mathcal F)<\infty\). Every smaller cycle must also contain a member of \(\mathcal F\), proving condition 2. ∎

This is an effective finite decision procedure for the case \(\vec\chi\le1\).

### Example 4.2

For every \(r\ge3\),
\[
\mathcal F_r=
 \{\vec C_3,\vec C_4,\ldots,\vec C_r,\vec P_r\}
\]
forces acyclicity. Indeed, \(\vec P_r\) has threshold \(r+1\), while all directed cycles of lengths \(3,\ldots,r\) are explicitly forbidden.

In particular,
\[
\{\vec C_3,\vec P_3\}
\]
is \(\vec\chi\)-finite with bound one: a shortest directed cycle is either a directed triangle or contains an induced directed three-vertex path.

---

## 5. Exact classification of families forcing bounded order

Let \(TT_t\) denote the transitive tournament on \(t\) vertices. Let \(q_t\) be the least integer such that every \(q_t\)-vertex tournament contains \(TT_t\). The standard induction gives
\[
q_t\le 2^{t-1}.
\]

### Theorem 5.1

The orders of all \(\mathcal F\)-free oriented graphs are bounded if and only if \(\mathcal F\) contains both:

- an edgeless graph \(\overline K_r\), and
- a transitive tournament \(TT_t\).

#### Proof

For necessity, consider arbitrarily large edgeless graphs. Every induced subgraph of an edgeless graph is edgeless, so some edgeless graph must belong to \(\mathcal F\). Similarly, every induced subgraph of a transitive tournament is a transitive tournament, so considering arbitrarily large transitive tournaments forces \(TT_t\in\mathcal F\) for some \(t\).

Conversely, suppose \(\overline K_r,TT_t\in\mathcal F\). For an \(\mathcal F\)-free oriented graph \(D\), the underlying graph \(G=U(D)\) has no independent set of size \(r\). It also has no clique of size \(q_t\), because any orientation of such a clique contains \(TT_t\). Ordinary Ramsey's theorem therefore gives
\[
|V(D)|<R(r,q_t)\le R(r,2^{t-1}),
\]
where \(R(a,b)\) denotes the least order forcing either an independent \(a\)-set or a \(b\)-clique. ∎

This characterizes the strongest, finite-order form of \(\vec\chi\)-finiteness.

---

## 6. Explicit Ramsey-bounded positive cases

Let \(\vec S_r^+\) be the induced out-star with center \(v\), leaves \(x_1,\ldots,x_r\), and arcs \(v\to x_i\). Let \(\vec S_r^-\) be its reversal.

We first use a simple coloring lemma.

### Lemma 6.1

For every oriented graph \(D\),
\[
\vec\chi(D)\le \Delta^+(D)+1
\quad\text{and}\quad
\vec\chi(D)\le \Delta^-(D)+1.
\]

#### Proof

Fix an ordering \(v_1,\ldots,v_n\). Process the vertices in this order, coloring \(v_i\) with one of \(\Delta^+(D)+1\) colors not used on an already colored out-neighbor.

If \(v_i\to v_j\) is monochromatic, then necessarily \(i<j\). Hence every arc in a color class points forward in the fixed ordering, so no color class contains a directed cycle. The indegree version follows by reversing every arc. ∎

### Proposition 6.2: one-way stars

For \(r\ge2\) and \(t\ge3\), every
\[
\{\vec S_r^+,TT_t\}\text{-free}
\]
oriented graph satisfies
\[
\vec\chi(D)\le R(r,q_t-1)
             \le R(r,2^{t-1}-1).
\]
The same bound holds with \(\vec S_r^-\) in place of \(\vec S_r^+\).

#### Proof

Since \(D\) is \(TT_t\)-free, \(U(D)\) has no clique of size \(q_t\).

For any vertex \(v\), the graph \(U(D)[N^+(v)]\) has:

- no independent set of size \(r\), since that set together with \(v\) would induce \(\vec S_r^+\);
- no clique of size \(q_t-1\), since together with \(v\) it would form a \(q_t\)-clique.

Therefore
\[
|N^+(v)|<R(r,q_t-1)
\]
for every \(v\). Lemma 6.1 gives the stated bound. The in-star case is dual. ∎

### Proposition 6.3: \(K_1+\vec P_2\)

Every
\[
\{K_1+\vec P_2,TT_t\}\text{-free}
\]
oriented graph satisfies
\[
\vec\chi(D)\le q_t-1\le 2^{t-1}-1.
\]

#### Proof

An oriented graph is \(K_1+\vec P_2\)-free precisely when its underlying graph has no induced \(K_1+K_2\). Such an underlying graph is complete multipartite.

Indeed, define \(x\sim y\) if \(x=y\) or \(x,y\) are nonadjacent. If \(x\sim y\), \(y\sim z\), but \(xz\) is an edge, then \(\{x,y,z\}\) induces exactly one edge, a contradiction. Thus \(\sim\) is an equivalence relation whose classes are independent, with every pair of distinct classes complete to one another.

There are at most \(q_t-1\) parts: choosing one vertex from each of \(q_t\) parts would give a \(q_t\)-vertex tournament and hence an induced \(TT_t\). Coloring each independent part separately gives the result. ∎

---

## 7. What remains open

The necessary conditions from Section 2 are far from a complete characterization. In particular:

- bounding the tournament subclass need not bound general oriented graphs;
- the high-girth argument only detects whether some forbidden member has forest underlying graph and says nothing about which orientations or disconnected forests suffice;
- Proposition 6.2 uses the strong fact that a transitive tournament bounds the size of every underlying clique; it does not handle tournament obstructions such as \(\vec C_3\), which can bound tournament dichromatic number while allowing arbitrarily large transitive tournaments;
- mixed oriented stars, general oriented trees, and interactions among several forest obstructions require substantially more structure.

Thus the overarching classification remains unresolved. The results above provide rigorous filters, exact classifications in three restricted regimes, and explicit positive families, but not a general answer.