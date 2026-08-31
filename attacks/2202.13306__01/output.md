```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture reduces to a bounded-antineighborhood/bounded-cyclic-neighborhood coloring problem, and it holds under bounded complement chromatic number or bounded maximal-clique size, but the required global bound remains open.",
  "would_publish": false,
  "caveats": "Assumes the source convention that + is disjoint union and that all digraphs are finite nonempty oriented graphs."
}
```

# Mathematical writeup

## 1. Statement and conventions

Write
\[
J=\Delta(1,1,H).
\]
Thus \(J\) consists of vertices \(x,y\), a copy \(Q\) of \(H\), and all arcs
\[
x\to y,\qquad y\to Q,\qquad Q\to x.
\]

I use \(K_1+F\) for the disjoint union of \(K_1\) and \(F\), as in the source motivation \(K_1+\overline K_t=\overline K_{t+1}\). For a vertex \(v\), let
\[
\overline N(v)=\{u:uv,vu\notin A(D)\}
\]
be its antineighborhood.

Assume there are constants \(a,b\) such that

1. every \(F\)-free, \(J\)-free oriented graph has dichromatic number at most \(a\);
2. every \((K_1+F)\)-free, \(H\)-free oriented graph has dichromatic number at most \(b\).

The conjecture asks for a bound on \(\vec\chi(D)\) for every \((K_1+F)\)-free, \(J\)-free oriented graph \(D\).

I do not obtain that final bound.

---

## 2. The basic local reduction

### Lemma 2.1

Let \(D\) be \((K_1+F)\)-free and \(J\)-free. Then:

\[
\vec\chi\bigl(D[\overline N(v)]\bigr)\le a
\quad\text{for every }v\in V(D),
\tag{2.1}
\]

and, for every arc \(x\to y\),

\[
\vec\chi\bigl(D[N^+(y)\cap N^-(x)]\bigr)\le b.
\tag{2.2}
\]

#### Proof

If \(D[\overline N(v)]\) contained an induced \(F\), then adjoining \(v\) would give an induced \(K_1+F\). Hence \(D[\overline N(v)]\) is \(F\)-free. It is also \(J\)-free by heredity, so (2.1) follows from the first hypothesis.

Now fix \(x\to y\) and put
\[
C(x,y)=N^+(y)\cap N^-(x).
\]
If \(D[C(x,y)]\) contained a copy \(Q\) of \(H\), then
\[
x\to y,\qquad y\to Q,\qquad Q\to x,
\]
so \(D[\{x,y\}\cup Q]\) would contain \(J\). Thus \(D[C(x,y)]\) is \(H\)-free. It remains \((K_1+F)\)-free, and (2.2) follows from the second hypothesis. ∎

Consequently, the conjecture would follow from the following purely local-to-global statement.

> **Local coloring problem.** Does there exist \(f(a,b)\) such that every oriented graph \(D\) satisfying
> \[
> \sup_v\vec\chi(D[\overline N(v)])\le a
> \]
> and
> \[
> \sup_{x\to y}\vec\chi(D[N^+(y)\cap N^-(x)])\le b
> \]
> has \(\vec\chi(D)\le f(a,b)\)?

I do not prove this local statement. Notice that when \(H=K_1\), condition (2.2) says precisely that \(D\) has no directed triangle. Thus even the case “directed-triangle-free with bounded-dichromatic antineighborhoods” is already a central special case.

For example, taking \(F=\overline K_2\) and \(H=K_1\), the conjecture includes the assertion that directed-triangle-free oriented graphs with independence number at most \(2\) have bounded dichromatic number.

---

## 3. Two necessary restrictions on a nonvacuous instance

### 3.1. The graph \(H\) must be a tournament

Every tournament is induced-\((K_1+F)\)-free, since \(K_1+F\) has a nonadjacent pair. Under the induced-copy convention for heroes, if \(H\) were not a tournament, every tournament would be \(H\)-free. This contradicts the existence of tournaments of arbitrarily large dichromatic number.

Hence \(H\) is necessarily a tournament, and the second hypothesis implies that \(H\) is a hero in tournaments. The proved tournament-hero closure theorem from the Berger-et-al. characterization then implies that
\[
J=\Delta(1,1,H)
\]
is also a hero in tournaments. Let \(c=c(H)\) be such that every \(J\)-free tournament has dichromatic number at most \(c\).

This uses a proved theorem from tournament hero theory, not another open conjecture.

### 3.2. The underlying graph of \(F\) must be a forest

The following standard probabilistic lemma gives this restriction.

#### Lemma 3.1

For every \(r,g\) there is an oriented graph \(D\) whose underlying graph has girth at least \(g\) and for which
\[
\vec\chi(D)>r.
\]

#### Proof

Fix \(r,g\), put \(\varepsilon=1/(2g)\), and let \(p=n^{-1+\varepsilon}\). Generate \(G\sim G(n,p)\), and orient every present edge independently and uniformly.

Set \(s=\lfloor n/(3r)\rfloor\). For a fixed \(s\)-set \(S\), if \(D[S]\) is acyclic, it has a topological ordering. For any prescribed ordering, every unordered pair must avoid being an edge directed backwards. Therefore
\[
\Pr(D[S]\text{ is acyclic})
 \le s!(1-p/2)^{\binom{s}{2}}.
\]
A union bound over all \(S\) gives
\[
\Pr(\text{some acyclic }s\text{-set})
 \le \binom ns s!
       \exp\!\left(-\frac p2\binom{s}{2}\right)=o(1),
\]
because the positive logarithmic terms are \(O(n\log n)\), whereas
\(ps^2=\Theta(n^{1+\varepsilon})\).

The expected number of underlying cycles of length less than \(g\) is at most
\[
\sum_{\ell=3}^{g-1}\frac{(np)^\ell}{2\ell}
 =O\!\left(n^{\varepsilon(g-1)}\right)=o(n).
\]
With positive probability, therefore, there is no acyclic \(s\)-set and there are fewer than \(n/3\) short underlying cycles. Delete one vertex from each such cycle. The remaining oriented graph \(D'\) has at least \(2n/3\) vertices and underlying girth at least \(g\).

If \(\vec\chi(D')\le r\), some color class has more than \(2n/(3r)>s\) vertices, and hence contains an acyclic \(s\)-set, a contradiction. ∎

Now suppose the underlying graph of \(F\) contains a cycle. Taking \(g>|V(F)|\), Lemma 3.1 gives \(F\)-free oriented graphs of arbitrarily large dichromatic number. Their underlying graphs are triangle-free, so they are also \(J\)-free because \(J\) contains a directed triangle. This contradicts the first hero hypothesis.

Thus every nonvacuous instance has \(H\) a tournament and the underlying graph of \(F\) a forest.

---

## 4. A quantitative partial transfer theorem

Let \(G_D\) denote the underlying graph of \(D\), and let \(\overline{G_D}\) be its ordinary complement. Define
\[
\mu(G_D)=\min\{|K|:K\text{ is a maximal clique of }G_D\}.
\]

### Theorem 4.1

Every \((K_1+F)\)-free, \(J\)-free oriented graph \(D\) satisfies
\[
\vec\chi(D)
 \le
 \min\left\{
 c\,\chi(\overline{G_D}),
 \quad c+a\,\mu(G_D)
 \right\}.
\tag{4.1}
\]

#### Proof of the complement-coloring bound

A proper coloring of \(\overline{G_D}\) partitions \(V(D)\) into cliques of \(G_D\). Each such clique induces a tournament in \(D\), and that tournament is \(J\)-free. It therefore has dichromatic number at most \(c\). Using disjoint palettes for the complement-color classes gives
\[
\vec\chi(D)\le c\,\chi(\overline{G_D}).
\]

#### Proof of the maximal-clique bound

Let \(K\) be any maximal clique of \(G_D\). Then \(D[K]\) is a \(J\)-free tournament, so
\[
\vec\chi(D[K])\le c.
\]

By maximality, every vertex \(x\notin K\) is nonadjacent to at least one vertex of \(K\). Assign \(x\) to one such vertex \(q(x)\in K\), and write
\[
B_q=\{x\notin K:q(x)=q\}.
\]
Then \(B_q\subseteq\overline N(q)\), and Lemma 2.1 gives
\[
\vec\chi(D[B_q])\le a.
\]
Coloring \(D[K]\) and the \(|K|\) sets \(B_q\) with disjoint palettes gives
\[
\vec\chi(D)\le c+a|K|.
\]
Minimizing over maximal cliques proves (4.1). ∎

### Consequences

The desired transfer is therefore valid on each of the following subclasses:

1. classes in which \(\chi(\overline{G_D})\) is uniformly bounded;
2. classes in which some maximal clique has uniformly bounded order.

In particular, when \(F=K_1\), the target class is the class of tournaments, \(\chi(\overline{G_D})=1\), and the conclusion follows from the tournament theorem.

---

## 5. A stronger fixed-copy decomposition when \(H\) is strongly connected

The following lemma appears to isolate the main remaining obstruction.

### Lemma 5.1

Assume \(H\) is a strongly connected tournament of order \(h\). Let \(Q\subseteq D\) be an induced copy of \(H\). Then there are sets \(L_Q,R_Q,E_Q\) partitioning \(V(D)\setminus Q\) such that

1. \(L_Q\to Q\to R_Q\);
2. there are no arcs from \(R_Q\) to \(L_Q\);
3.
   \[
   \vec\chi(D[E_Q])
   \le ha+(2^h-2)b.
   \]

Consequently,
\[
\vec\chi(D)
 \le ha+(2^h-2)b+
 \max\{\vec\chi(D[L_Q]),\vec\chi(H),\vec\chi(D[R_Q])\}.
\tag{5.1}
\]

#### Proof

Let
\[
Z_Q=\{v\notin Q:v\text{ is nonadjacent to some }q\in Q\}.
\]
Since
\[
Z_Q\subseteq\bigcup_{q\in Q}\overline N(q),
\]
Lemma 2.1 and subadditivity give
\[
\vec\chi(D[Z_Q])\le ha.
\tag{5.2}
\]

Every vertex \(v\notin Q\cup Z_Q\) is adjacent to every vertex of \(Q\). Define its pattern
\[
S(v)=\{q\in Q:q\to v\}.
\]
For each nonempty proper \(S\subsetneq Q\), let
\[
P_S=\{v:S(v)=S\}.
\]

Because \(Q\) is strongly connected, there are \(q_0\in Q\setminus S\) and \(q_1\in S\) with
\[
q_0\to q_1.
\]
If \(P_S\) contained a copy \(R\) of \(H\), then
\[
q_0\to q_1,\qquad q_1\to R,\qquad R\to q_0,
\]
which is a copy of \(J\). Hence \(P_S\) is \(H\)-free and
\[
\vec\chi(D[P_S])\le b.
\]
There are \(2^h-2\) nonempty proper patterns, so, putting
\[
M_Q=\bigcup_{\varnothing\ne S\subsetneq Q}P_S,
\]
we have
\[
\vec\chi(D[M_Q])\le(2^h-2)b.
\tag{5.3}
\]

Set
\[
E_Q=Z_Q\cup M_Q,
\]
and define
\[
L_Q=\{v:v\to Q\},\qquad R_Q=\{v:Q\to v\}.
\]
Equations (5.2) and (5.3) prove the asserted bound on \(E_Q\).

If \(r\in R_Q\), \(l\in L_Q\), and \(r\to l\), then
\[
Q\to r\to l\to Q
\]
is a copy of \(J\). Therefore no arc goes from \(R_Q\) to \(L_Q\).

Thus \(L_Q,Q,R_Q\) occur in a one-way order. Colorings of these three subdigraphs can use the same palette: a directed cycle meeting more than one of the three sets would require an arc going backwards in this order. This proves (5.1). ∎

### Remark on non-strong \(H\)

If the strong components of \(H\) are
\[
C_1\Rightarrow C_2\Rightarrow\cdots\Rightarrow C_t,
\]
the same argument shows that a pattern class \(P_S\) is \(H\)-free unless
\[
S=C_1\cup\cdots\cup C_i
\]
for some \(0\le i\le t\). Thus only the \(t+1\) “insertion patterns” between consecutive strong components escape the \(b\)-bound.

---

## 6. Why the separator lemma does not finish the proof

A tempting induction from (5.1) fails. If one assumes inductively that
\[
\vec\chi(D[L_Q]),\vec\chi(D[R_Q])\le C,
\]
then (5.1) only yields
\[
\vec\chi(D)\le C+ha+(2^h-2)b.
\]
Along a nested sequence of copies of \(H\), the exceptional sets \(E_Q\) may occur at arbitrarily many levels. Nothing proved above allows their color palettes to be reused globally.

This is also visible in Theorem 4.1: a maximal clique can be arbitrarily large, and the proof currently pays \(a\) new colors for every clique vertex. The missing argument must exploit the ordered tournament structure of a large clique or a long chain of copies of \(H\) to reuse these colors.

---

## 7. Structure of any unbounded counterexample family

Suppose, contrary to the conjecture, that there are target digraphs of arbitrarily large dichromatic number. Taking induced vertex-critical subdigraphs, let \(D\) be \(k\)-dicritical.

For every vertex \(v\),
\[
d^+(v),d^-(v)\ge k-1.
\tag{7.1}
\]
Indeed, color \(D-v\) with \(k-1\) acyclic colors. If one color class contained no outneighbor of \(v\), or no inneighbor of \(v\), then \(v\) could be added to that class without creating a directed cycle.

Moreover, Theorem 4.1 implies
\[
\chi(\overline{G_D})\ge \frac{k}{c}
\tag{7.2}
\]
and, when \(a>0\), every maximal clique \(K\) satisfies
\[
|K|\ge\frac{k-c}{a}.
\tag{7.3}
\]
Since \(D[K]\) can be partitioned into at most \(c\) transitive subtournaments, every maximal clique contains a transitive subtournament of order at least
\[
\frac{k-c}{ac}.
\tag{7.4}
\]

Thus a counterexample cannot arise from sparse or bounded-clique configurations: it must simultaneously have large minimum in- and outdegree, large complement chromatic number, and arbitrarily long transitive cliques, while still satisfying the two local bounds (2.1)–(2.2).

---

## 8. Conclusion

The conjecture remains unresolved here. The main rigorous progress is:

- the two local bounds (2.1)–(2.2);
- the necessary restrictions that \(H\) is a tournament and the underlying graph of \(F\) is a forest;
- the quantitative bounds (4.1), proving the transfer under bounded complement chromatic number or bounded maximal-clique size;
- the strong-\(H\) separator lemma (5.1), which reduces the remaining difficulty to controlling exceptional sets across an unbounded chain of copies of \(H\).

The unresolved step is a genuinely global palette-reuse argument; the fixed-copy decomposition alone does not supply it.