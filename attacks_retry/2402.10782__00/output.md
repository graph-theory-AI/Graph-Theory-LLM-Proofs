```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every fixed prime modular quotient size q, the conjectured gap algorithm exists with f_q(k)=q^(k-2).",
  "would_publish": false,
  "caveats": "This is a bounded-modular-width special case; that width is unbounded even when the tournament clique number is two, and novelty has not been checked."
}
```

## 1. Result obtained

I do not resolve the unrestricted conjecture. I obtain a special case that handles arbitrarily large tournament clique number and has a directly verifiable structural promise.

For an ordering \(\sigma\) of a tournament \(T\), let \(B_\sigma=T^\sigma\) be its backedge graph, and write
\[
\lambda(T)=\overrightarrow{\omega}(T)
          =\min_\sigma \omega(B_\sigma).
\]
Write \(\chi_{\mathrm d}(T)\) for the dichromatic number: the minimum number of parts in a partition of \(V(T)\) into transitive subtournaments.

If \(Q\) is a tournament on \(\{1,\ldots,s\}\), its **substitution**
\[
Q(T_1,\ldots,T_s)
\]
is obtained by replacing vertex \(i\) with \(T_i\), with all arcs between \(T_i,T_j\) directed according to the arc between \(i,j\) in \(Q\).

Fix \(q\ge 3\). Let \(\mathcal M_q\) be the class generated from the one-vertex tournament by substitutions with quotient tournaments having at most \(q\) vertices. Equivalently, these are the tournaments whose prime modular quotients have at most \(q\) vertices. Arbitrarily large transitive quotients are harmless: they can be represented by repeated two-vertex transitive substitutions.

### Theorem 1
For every nonempty \(T\in\mathcal M_q\),
\[
\boxed{\quad
\chi_{\mathrm d}(T)\le q^{\lambda(T)-1}.
\quad} \tag{1}
\]

Consequently, for fixed \(q\) and every \(k\ge 2\), there is an algorithm running in time \(n^{q+O(1)}\) which, on a tournament \(T\in\mathcal M_q\), either

* correctly concludes that \(\lambda(T)\ge k\), or
* constructs an order \(\pi\) satisfying
  \[
  \boxed{\quad \omega(B_\pi)\le q^{k-2}.\quad} \tag{2}
  \]

Membership in \(\mathcal M_q\) and a suitable decomposition are computable in polynomial time; the decomposition need not be supplied.

The proof is independent of both the reported \(k=3\) result and the previous attempt.

---

## 2. Preliminary facts

The class \(\mathcal M_q\) is hereditary. Indeed, restricting a substitution tree to an induced subtournament merely deletes empty children and restricts quotient tournaments.

Both \(\lambda\) and \(\chi_{\mathrm d}\) are monotone under induced subtournaments.

Also,
\[
\lambda(T)\le \chi_{\mathrm d}(T). \tag{3}
\]
To see this constructively, take a transitive coloring, concatenate its color classes, and order each class in its transitive order. Each class is independent in the resulting backedge graph, so a backedge clique contains at most one vertex from each class.

The essential point of Theorem 1 is the reverse, class-dependent bound (1).

---

## 3. A restriction on cyclic triples of modules

We prove (1) by induction. The following observation supplies the structural step.

Suppose \(r\ge2\), and suppose that every member \(S\) of \(\mathcal M_q\) with \(\lambda(S)\le r-1\) satisfies
\[
\chi_{\mathrm d}(S)\le h. \tag{4}
\]
Let \(T\in\mathcal M_q\) have an order \(\sigma\) with
\[
\omega(B_\sigma)\le r. \tag{5}
\]

Consider three modules \(A,B,C\) in a substitution decomposition of \(T\), with
\[
A\longrightarrow B\longrightarrow C\longrightarrow A.
\]

### Lemma 2
If \(\chi_{\mathrm d}(T[A])>2h\), then
\[
\chi_{\mathrm d}(T[B])\le h
\quad\text{and}\quad
\chi_{\mathrm d}(T[C])\le h. \tag{6}
\]

### Proof

Whenever a set \(X\) is entirely backedge-adjacent to a vertex \(v\notin X\), condition (5) implies
\[
\omega(B_\sigma[X])\le r-1.
\]
Consequently \(\lambda(T[X])\le r-1\), and heredity together with (4) gives
\[
\chi_{\mathrm d}(T[X])\le h. \tag{7}
\]

Fix \(c\in C\), and let \(b\) be the first vertex of \(B\) in \(\sigma\).

* If \(c<_{\sigma}b\), then every vertex of \(B\) is later than \(c\) and sends an arc to \(c\). Thus \(B\) is entirely backedge-adjacent to \(c\), giving
  \[
  \chi_{\mathrm d}(T[B])\le h.
  \]

* If \(b<_{\sigma}c\), partition \(A\) into the vertices before \(c\) and those after \(c\). The first part is entirely backedge-adjacent to \(c\), since \(C\to A\). The second part is entirely backedge-adjacent to \(b\), since \(A\to B\) and \(b<_{\sigma}c\). Hence each part has dichromatic number at most \(h\), giving
  \[
  \chi_{\mathrm d}(T[A])\le2h.
  \]

We have proved
\[
\chi_{\mathrm d}(T[A])>2h
   \ \Longrightarrow\
\chi_{\mathrm d}(T[B])\le h. \tag{8}
\]

There is a symmetric implication in the other direction. Let \(a\) be the last vertex of \(A\).

* If \(a<_{\sigma}c\), then all of \(A\) is backedge-adjacent to \(c\), so \(\chi_{\mathrm d}(T[A])\le h\).
* If \(c<_{\sigma}a\), split \(B\) at \(c\). Its part before \(c\) is backedge-adjacent to \(a\), and its part after \(c\) is backedge-adjacent to \(c\). Thus \(\chi_{\mathrm d}(T[B])\le2h\).

Therefore
\[
\chi_{\mathrm d}(T[B])>2h
   \ \Longrightarrow\
\chi_{\mathrm d}(T[A])\le h. \tag{9}
\]

Applying (9) after cyclically relabelling \((A,B,C)\) proves the second conclusion in (6). \(\square\)

Thus, in the quotient tournament, a directed triangle containing a module of dichromatic number greater than \(2h\) can contain only modules of dichromatic number at most \(h\) in its other two positions.

---

## 4. Proof of the dichromatic bound

We prove the following formulation of (1):
\[
T\in\mathcal M_q,\quad \lambda(T)\le r
\quad\Longrightarrow\quad
\chi_{\mathrm d}(T)\le q^{r-1}. \tag{10}
\]

We use induction on \(r\), and, for fixed \(r\), induction on \(|V(T)|\).

For \(r=1\), a witnessing backedge graph has no edges. Hence \(T\) is transitive and \(\chi_{\mathrm d}(T)=1\).

Now suppose \(r\ge2\), and put
\[
h=q^{r-2},\qquad g=qh=q^{r-1}.
\]
The induction on \(r\) supplies hypothesis (4).

If \(T\) has one vertex, there is nothing to prove. Otherwise, choose a substitution representation
\[
T=Q(T_1,\ldots,T_s),
\qquad 2\le s\le q.
\]
Put
\[
w_i=\chi_{\mathrm d}(T_i).
\]
Each \(T_i\) is smaller than \(T\) and has \(\lambda(T_i)\le r\), so induction on the number of vertices gives
\[
w_i\le g \qquad (1\le i\le s). \tag{11}
\]

Classify quotient vertices into
\[
\begin{aligned}
H&=\{i:w_i>2h\},\\
M&=\{i:h<w_i\le2h\},\\
L&=\{i:w_i\le h\}.
\end{aligned}
\]

We construct a transitive coloring of \(T\) with at most \(g\) colors.

### Case 1: \(H=\varnothing\)

All \(w_i\le2h\).

If \(s=2\), give both modules the same palette of \(2h\) colors. Every color then occurs in at most two modules, so its vertices induce a transitive tournament.

If \(s\ge3\), take an auxiliary undirected cycle on the quotient vertices. Assign a distinct palette of \(h\) colors to each cycle edge. Module \(T_i\) may use the palettes on its two incident edges, giving it \(2h\) available colors.

Every color occurs in at most two modules. Thus this is again a transitive coloring, using
\[
sh\le qh=g
\]
colors.

### Case 2: \(H\ne\varnothing\)

Lemma 2 implies that no directed triangle in \(Q\) contains both a vertex of \(H\) and another vertex of \(H\cup M\).

It follows that:

1. \(Q[H]\) is transitive;
2. \(Q[H\cup\{\ell\}]\) is transitive for every \(\ell\in L\);
3. \(Q[H\cup P]\) is transitive for every \(P\subseteq M\) with \(|P|\le2\).

For the third assertion, a directed triangle would have to contain a vertex of \(H\), since \(|P|\le2\), and would then contain another vertex of \(H\cup M\), which is forbidden.

Allocate palettes to \(L\cup M\) as follows.

* Each vertex of \(L\) gets its own palette of \(h\) colors.
* If \(|M|=1\), its single vertex gets a separate palette of \(2h\) colors.
* If \(|M|\ge2\), use the two-module or auxiliary-cycle construction from Case 1 on \(M\). This uses \(|M|h\) colors and gives every module in \(M\) access to \(2h\) colors.

Keep these palettes disjoint. Their total size is
\[
\begin{cases}
|L|h,&|M|=0,\\
(|L|+2)h,&|M|=1,\\
(|L|+|M|)h,&|M|\ge2.
\end{cases}
\]
Because \(H\ne\varnothing\) and \(|H|+|M|+|L|\le q\), this total is at most \(qh=g\).

Extend the palette to exactly \(g\) colors if necessary. By (11), every module indexed by \(H\) can color itself using this common palette.

The quotient support of each resulting color consists of:

* vertices of \(H\) alone;
* vertices of \(H\) and at most one vertex of \(L\); or
* vertices of \(H\) and at most two vertices of \(M\).

Each support is transitive by the three assertions above. Inside every module the color is transitive, and all cross-arcs follow the quotient. Hence every global color is transitive.

Thus \(\chi_{\mathrm d}(T)\le g\), completing both inductions and proving Theorem 1’s structural assertion. \(\square\)

---

## 5. Finding the decomposition

Here are algorithmic details so that the structural promise is not an additional certificate supplied with the input.

A nonempty set \(X\subseteq V(T)\) is a module if every vertex outside \(X\) either dominates all of \(X\) or is dominated by all of \(X\).

### 5.1 Computing the smallest module containing a pair

For distinct \(u,v\), start with \(X=\{u,v\}\). While some outside vertex has both an inneighbor and an outneighbor in \(X\), add that vertex to \(X\).

Every such vertex must belong to any module containing the current \(X\). At termination \(X\) is a module. Thus this procedure computes the smallest module containing \(u,v\), in polynomial time.

### 5.2 Decomposing a strongly connected tournament

In a strongly connected tournament, the maximal proper modules are pairwise disjoint.

Indeed, suppose two such modules overlap and neither contains the other. Their union is a module, so maximality forces their union to be the entire vertex set. The module identities then force the three nonempty sets
\[
X\setminus Y,\quad X\cap Y,\quad Y\setminus X
\]
to be uniformly oriented in a transitive order, contradicting strong connectivity.

The maximal proper modules therefore partition the vertex set. Two vertices belong to the same part precisely when their smallest containing module is proper. Hence all parts can be recovered from the pair-closure procedure above.

Their quotient is prime: a nontrivial proper module of the quotient would lift to a proper module containing more than one maximal proper module.

### 5.3 Complete recognition procedure

Recursively:

* If the tournament is not strongly connected, decompose it into its strongly connected components. Their quotient is transitive.
* Otherwise, compute its maximal proper modules. If their number exceeds \(q\), reject membership in \(\mathcal M_q\); otherwise recurse on them.

Transitive component quotients can be represented by binary substitutions.

This procedure recognizes \(\mathcal M_q\). For necessity, in any bounded-arity substitution representation of a strongly connected tournament, each root child is contained in a maximal proper module. Thus there are at most \(q\) such maximal modules. Heredity handles recursion.

The entire decomposition procedure is polynomial-time.

---

## 6. Computing the dichromatic number exactly on this class

Only the dichromatic number—not \(\lambda\)—is optimized in the following dynamic program.

Suppose a decomposition node is
\[
T=Q(T_1,\ldots,T_s),
\qquad s\le q,
\]
and optimal transitive colorings of the children are known, with sizes \(w_1,\ldots,w_s\).

A global color can be used in a set of child modules precisely when that set induces a transitive subtournament of \(Q\). Consequently, the required number of colors is the minimum number of transitive subsets of \(Q\), allowing repetitions, that cover vertex \(i\) at least \(w_i\) times.

This characterization is exact:

* A coloring of \(T\) gives such a cover by taking the quotient support of each color.
* Conversely, from such a cover, assign the \(w_i\) color classes of \(T_i\) to \(w_i\) distinct occurrences covering \(i\). Every global color remains transitive.

Excess covering occurrences can simply be left unused.

Enumerate the at most \(2^s\) transitive subsets of \(Q\). For a remaining-demand vector
\[
d=(d_1,\ldots,d_s),\qquad 0\le d_i\le w_i,
\]
use
\[
D(0)=0
\]
and
\[
D(d)=
1+\min_{\substack{\varnothing\ne S\subseteq \{i:d_i>0\}\\Q[S]\text{ transitive}}}
D(d-\mathbf 1_S).
\]
There are at most
\[
\prod_{i=1}^s(w_i+1)\le(n+1)^q
\]
states, with at most \(2^q\) transitions per state. Reconstruction gives an optimal coloring.

At a transitive component node, the answer is simply the maximum of the children’s dichromatic numbers, with palettes reused.

Thus an optimal transitive coloring is computable in \(n^{q+O(1)}\) time.

### The gap algorithm

For \(k\ge2\), set
\[
F=q^{k-2}.
\]

1. Recognize membership in \(\mathcal M_q\) and obtain the decomposition.
2. Compute \(c=\chi_{\mathrm d}(T)\) and an optimal transitive coloring.
3. If \(c>F\), conclude \(\lambda(T)\ge k\). This follows from (1).
4. Otherwise concatenate the \(c\) color classes in their transitive orders. By (3), the resulting order satisfies
   \[
   \omega(B_\pi)\le c\le F.
   \]

Empty tournaments and \(k\le1\) are immediate.

On an input outside \(\mathcal M_q\), the recognition failure is **not** a certificate that \(\lambda(T)\ge k\). This is the explicit limitation of the algorithm.

---

## 7. Scope of the special case

### 7.1 It includes unbounded tournament clique number

Let \(R_1\) be the one-vertex tournament and define
\[
R_{d+1}=C_3(R_d,R_d,R_d).
\]
Every \(R_d\) belongs to \(\mathcal M_3\).

In any order of \(R_{d+1}\), let \(v\) be the first vertex. One entire other module dominates the module containing \(v\). Every vertex of that module is therefore backedge-adjacent to \(v\). It follows that
\[
\lambda(R_{d+1})\ge \lambda(R_d)+1.
\]
Hence
\[
\lambda(R_d)\ge d.
\]

Thus the special case is not merely an algorithm for a class whose tournament clique number was already bounded.

### 7.2 Modular width is not bounded in terms of \(\lambda\)

For \(a\ge1\), let \(P_{2a+1}\) have vertices \(\mathbb Z/(2a+1)\mathbb Z\), with
\[
i\to j
\quad\Longleftrightarrow\quad
j-i\pmod{2a+1}\in\{1,\ldots,a\}.
\]

In the order \(0,1,\ldots,2a\), a backedge joins \(i<j\) exactly when \(j-i>a\). Three vertices cannot be pairwise joined by backedges, because this would require two consecutive gaps each greater than \(a\). The tournament is nontransitive, so
\[
\lambda(P_{2a+1})=2.
\]

These tournaments are prime. Their in- and outneighborhoods are transitive, so every proper module is transitive. A nontrivial transitive module would contain a two-vertex module, by taking its first two vertices.

But no pair is a module. After rotation, an arc has the form \(0\to d\), \(1\le d\le a\), and
\[
d\to a+1\to0
\]
distinguishes its endpoints.

Thus prime modular quotient size is unbounded even at \(\lambda=2\).

### 7.3 Why the dichromatic argument cannot be extended verbatim

There is no bound on \(\chi_{\mathrm d}(T)\) in terms of \(\lambda(T)\) for arbitrary tournaments.

To see the obstruction, take a triangle-free graph \(G\) of arbitrarily large chromatic number, fix an order \(\sigma\), and orient a tournament forward along \(\sigma\), except that the edges of \(G\) are reversed. Then
\[
B_\sigma=G,\qquad \lambda(T)\le2.
\]

If \(S\) induces a transitive subtournament, then \(G[S]\) is the inversion graph between \(\sigma|_S\) and the transitive order of \(T[S]\). Since it is triangle-free, the corresponding permutation has no decreasing subsequence of length three and can be partitioned into two increasing subsequences. Hence \(G[S]\) is bipartite.

Therefore a transitive coloring of \(T\) with \(c\) colors gives a coloring of \(G\) with at most \(2c\) colors:
\[
\chi(G)\le2\chi_{\mathrm d}(T).
\]
Taking triangle-free graphs of unbounded chromatic number shows that \(\chi_{\mathrm d}(T)\) is unbounded while \(\lambda(T)\le2\).

So the bounded-width hypothesis is doing essential work in Theorem 1.

---

## 8. A separate obstruction to feedback-arc-count approximation

There is also a concrete obstruction to a natural strategy suggested by the source paper: first approximate the **number** of feedback arcs, and hope that the resulting order has bounded backedge clique number.

That strategy cannot work, even for tournaments with dichromatic number two.

### Proposition 3
For every real \(\alpha\ge1\) and every integer \(t\ge2\), there is a tournament \(T\) with
\[
\lambda(T)=\chi_{\mathrm d}(T)=2
\]
such that every ordering whose number of backedges is at most \(\alpha\) times optimum has a backedge clique of size \(t\).

### Proof

Let
\[
C=\{c_1,\ldots,c_t\},
\]
and take disjoint anchor sets \(A_1,\ldots,A_{t-1}\), each of size \(M\), where
\[
M>\alpha\binom t2.
\]

Fix the reference order
\[
\tau=(c_t,A_{t-1},c_{t-1},\ldots,c_2,A_1,c_1),
\]
with an arbitrary fixed order inside each anchor set.

Orient every pair forward in \(\tau\), except pairs inside \(C\), which are oriented
\[
c_i\to c_j\qquad(i<j).
\]

Both \(T[C]\) and \(T[\bigcup_i A_i]\) are transitive. The tournament contains directed triangles, so
\[
\chi_{\mathrm d}(T)=\lambda(T)=2.
\]

The order \(\tau\) has exactly
\[
b=\binom t2
\]
backedges.

Suppose an order \(\pi\) does not list \(C\) in the relative order \(c_t,\ldots,c_1\). Then some \(i\) satisfies
\[
c_i<_{\pi}c_{i+1}.
\]
For each \(a\in A_i\), there is a directed triangle
\[
c_{i+1}\to a\to c_i\to c_{i+1}.
\]
Its \(C\)-edge is forward in \(\pi\), so at least one of its two anchor edges is backward. Distinct anchors give distinct edges. Thus \(\pi\) has at least \(M\) backedges.

Consequently, since \(M>b\), the optimum number of backedges is exactly \(b\): orders reversing \(C\) have at least \(b\), while all other orders have at least \(M>b\).

Any \(\alpha\)-approximate order has at most \(\alpha b<M\) backedges, so it must reverse \(C\). Then \(C\) is a \(K_t\) in its backedge graph. \(\square\)

This is not a counterexample to the conjecture: good clique-bounded orders exist. It shows that even an exact minimum-feedback-arc ordering can be unsuitable.

---

## 9. Remaining gap

The proved contribution is the explicit bound
\[
\chi_{\mathrm d}(T)\le q^{\overrightarrow{\omega}(T)-1}
\]
for bounded prime modular quotient size, together with a polynomial-time implementation of the resulting gap algorithm.

The unrestricted problem remains unresolved by these arguments. In particular:

* prime quotient size cannot be bounded in terms of \(k\);
* replacing the structural argument with a general dichromatic bound is impossible;
* optimizing feedback-arc count, even exactly, does not supply the desired ordering.

No computational experiments or unverified literature results were used. I have not independently checked the novelty of the partial theorem against the literature.