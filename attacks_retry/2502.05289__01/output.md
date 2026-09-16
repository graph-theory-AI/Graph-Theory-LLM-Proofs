```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For k=2, I prove a no-gap theorem for hereditary classes with a bounded transversal of fully pairable four-sets, covering outerstring graphs and a bounded-interior-string extension.",
  "would_publish": false,
  "caveats": "No separating class or universal reduction is obtained; the catalog question remains unresolved here, and novelty of the partial results is not asserted."
}
```

# A hereditary no-gap criterion

I use the following convention throughout: an induced linkage consists of vertex-disjoint induced paths that are pairwise anticomplete. All terminals are distinct. Algorithms on a graph class receive inputs promised to belong to the class; no recognition algorithm is assumed.

The principal partial result is:

> **Theorem.** Let \(\mathcal C\) be hereditary. Suppose there is a constant \(q\) such that, in every \(G\in\mathcal C\), some set of at most \(q\) vertices intersects every terminal four-set on which all three pairings admit induced linkages. Then Induced \(2\)-Disjoint Paths is polynomial-time Turing reducible to the flow variant on \(\mathcal C\).
>
> Neither the intersecting set nor a way to find it is required as input.

In particular, this rules out the proposed gap on hereditary outerstring classes, and more generally on classes with disk-string representations in which only constantly many strings fail to reach the boundary.

I also strengthen the previous attempt’s residual hardness construction: deciding the third pairing remains NP-complete with **degree-two terminals, bounded maximum degree, and explicit length-four solutions for the other two pairings**.

The missing step is still substantial: these results neither cover every hereditary class nor produce a separating one.

## 1. Heredity turns flow decision into flow search

For a perfect matching \(M\) on four terminals, let
\[
\mathsf L(G,M)
\]
mean that \(G\) has an induced \(M\)-linkage. Label the three matchings
\[
\begin{aligned}
M_0&=\{a_1a_2,a_3a_4\},\\
M_1&=\{a_1a_4,a_2a_3\},\\
M_2&=\{a_1a_3,a_2a_4\}.
\end{aligned}
\]
Here \(a_i a_j\) denotes a terminal pair, not necessarily a graph edge.

Let \(\mathsf F_i\) be the flow query whose \(2\)-\(2\) partition excludes \(M_i\). Directly from the definitions,
\[
\mathsf F_i(G)=\bigvee_{j\ne i}\mathsf L(G,M_j).
\tag{1}
\]

The useful additional leverage is that on a hereditary class, a YES answer can be converted into an explicit linkage.

### Lemma 1: flow self-reduction

Given a flow decision oracle on a hereditary class and a positive instance \((G,S,T)\), an explicit solution can be found using \(O(|V(G)|)\) oracle calls on induced subgraphs.

**Proof.** Starting with \(H=G\), test each nonterminal vertex \(v\), deleting it whenever the flow instance on \(H-v\) remains positive.

The resulting \(H\) is deletion-minimal positive. Indeed, if a vertex was not deletable when tested, subsequent deletions cannot make it deletable: a solution in the later, smaller graph would also have existed at the earlier test.

Take any flow solution in the final \(H\). Its paths must cover \(V(H)\), since otherwise an uncovered nonterminal could be deleted. Because the paths are induced and mutually anticomplete, \(H\) itself is exactly their disjoint union. Thus its two components reveal both the paths and their terminal pairing. ∎

### A three-outcome routine

Suppose the requested pairing is \(M_2\).

1. Query \(\mathsf F_0=M_1\lor M_2\).
   - If NO, reject.
   - Otherwise use Lemma 1 to obtain a linkage.
   - If its pairing is \(M_2\), accept.

2. The obtained pairing must otherwise be \(M_1\). On the **original current graph \(G\)**, query
   \(\mathsf F_1=M_0\lor M_2\).
   - If NO, reject.
   - Otherwise extract a linkage.
   - If its pairing is \(M_2\), accept.

3. Otherwise we have explicit linkages for both \(M_0\) and \(M_1\).

Call the third outcome **ambiguous**. The routine uses \(O(n)\) flow calls and has the following guarantees:

- an acceptance includes a certificate for the requested pairing;
- a rejection is correct;
- an ambiguous outcome supplies certificates for the other two pairings.

Moreover, if an ambiguous instance is actually positive for the requested pairing, then all three pairings are feasible.

A useful elementary observation is that **two distinct feasible pairings already force the four terminals to be independent**. Any edge between two terminals would force those terminals to lie on the same path in every feasible linkage, whereas two distinct perfect matchings on four vertices have no common pair.

For reference, let \(\mathrm{All}_3\) be the problem of deciding whether all three pairings are feasible. The routine proves, on every hereditary class,
\[
\mathrm{Link}_2\in\mathrm P
\quad\Longleftrightarrow\quad
\bigl(\mathrm{Flow}_2\in\mathrm P
\ \text{and}\ 
\mathrm{All}_3\in\mathrm P\bigr).
\tag{2}
\]
For the reverse implication, consult \(\mathrm{All}_3\) only in the ambiguous case. The forward implication follows by testing the two, respectively three, possible matchings.

Equation (2) is a partial complexity characterization, not a resolution of the catalog question.

## 2. Bounded transversals of pairing ambiguity

Call a four-set \(Z\subseteq V(G)\) **fully pairable** if all three perfect matchings on \(Z\) admit induced linkages in \(G\). The three linkage certificates are separate; they need not coexist or be disjoint from one another.

Define
\[
\tau(G)=
\min\bigl\{|X|:\ X\subseteq V(G),\
X\cap Z\ne\varnothing
\text{ for every fully pairable four-set }Z\bigr\}.
\tag{3}
\]
In particular, \(\tau(G)=0\) means that no four-set supports all three pairings.

There is an important distinction here: \(X\) must meet the **terminal sets** of all fully pairable quartets. Merely requiring \(G-X\) to have no fully pairable quartet is weaker, because linkage witnesses in \(G\) may use \(X\) internally.

### Monotonicity

If \(H\) is an induced subgraph of \(G\), every fully pairable four-set of \(H\) is fully pairable in \(G\). Consequently, if \(X\) meets all such four-sets in \(G\), then \(X\cap V(H)\) does so in \(H\).

In particular, deleting a vertex of \(X\) reduces the size of this available transversal by at least one.

### Lemma 2: advancing a terminal

Suppose the four terminals \(v,w,y,z\) are independent and the requested pairing is
\[
M=\{vw,yz\}.
\]
For \(x\in N_G(v)\), put
\[
H_{v,x}
=
G-\bigl(\{v\}\cup(N_G(v)\setminus\{x\})\bigr),
\qquad
M_{v,x}=\{xw,yz\}.
\]
Then
\[
\mathsf L(G,M)
\quad\Longleftrightarrow\quad
\bigvee_{x\in N_G(v)}
\mathsf L(H_{v,x},M_{v,x}).
\tag{4}
\]

**Proof.** In a linkage for \(M\), let \(x\) be the neighbor of \(v\) on its path. Every other vertex of that path avoids \(N_G(v)\), by inducedness; the second path avoids \(N_G(v)\), by anticompleteness. Removing \(v\) therefore gives the required linkage in \(H_{v,x}\).

Conversely, append \(v\) to the \(x\)-end of a linkage in \(H_{v,x}\). Among its selected vertices, \(v\) is adjacent only to \(x\), so the extension is induced and remains anticomplete to the other path. ∎

### Theorem 3: the bounded-transversal reduction

Let \(q\ge 0\) be fixed, and let \(\mathcal C\) be hereditary with
\[
\tau(G)\le q\qquad\text{for all }G\in\mathcal C.
\]
Then prescribed induced two-path linkage can be solved with
\[
O(4^q n^{q+1})
\]
flow-oracle calls on induced subgraphs of the input, plus polynomial overhead for fixed \(q\).

**Proof.** Define a recursive procedure \(R_d(G,M)\).

1. Run the three-outcome routine from Section 1.
2. If it accepts or rejects, return that answer.
3. If it is ambiguous and \(d=0\), return NO.
4. Otherwise, for every terminal \(v\) and every \(x\in N_G(v)\), recursively run
   \[
   R_{d-1}(H_{v,x},M_{v,x}),
   \]
   where the requested matching is updated by replacing terminal \(v\) with \(x\).
5. Accept if any recursive call accepts, extending its certificate by the edge \(vx\). Otherwise reject.

The terminal set in an ambiguous instance is independent, as observed above. Thus the replacements in step 4 have four distinct terminals and do not delete the other three terminals.

We prove two assertions.

**Soundness for every budget.** For every graph and every \(d\), a YES answer comes with a valid requested linkage. This follows inductively from the certificates produced by flow self-reduction and from Lemma 2. This assertion does not require \(\tau(G)\le d\).

**Completeness when \(\tau(G)\le d\).** Suppose the requested linkage exists and let \(X\) be a transversal of size at most \(d\).

If the initial routine finds the requested linkage, there is nothing to prove. It cannot correctly reject a positive instance. Thus consider an ambiguous outcome. Together with the requested linkage, the two alternative certificates show that the current terminal set \(Z\) is fully pairable. Hence
\[
Z\cap X\ne\varnothing.
\]

Choose \(v\in Z\cap X\), and let \(x\) be its first neighbor on a requested linkage. By Lemma 2, the corresponding recursive instance is positive. Its graph is induced in \(G\), and \(v\) has been deleted, so
\[
(X\setminus\{v\})\cap V(H_{v,x})
\]
is a transversal of size at most \(d-1\). Induction therefore makes this branch accept.

For \(d=0\), an ambiguous positive instance is impossible: its terminal set would be fully pairable despite the existence of an empty transversal.

These two assertions also justify exploring branches that do not delete a vertex of \(X\). Such branches might receive too small a budget and miss a solution, but they can never produce a false YES.

There are at most \(4n\) recursive children at each node, the depth is at most \(q\), and each node makes \(O(n)\) flow calls. This gives the claimed bound. All oracle inputs lie in \(\mathcal C\), by heredity. ∎

Since flow is the disjunction of two prescribed-pair instances, this gives polynomial-time Turing equivalence on the stated classes.

The implication is unconditional:
\[
\mathrm{Flow}_2\in\mathrm P
\ \Longrightarrow\
\mathrm{Link}_2\in\mathrm P.
\]
Its interpretation as ruling out an NP-complete-versus-P gap uses the usual assumption \(\mathrm P\ne\mathrm{NP}\).

## 3. Geometric and structural consequences

### 3.1 Outerstring graphs, and boundedly many interior strings

Consider a representation of \(G\) by finitely many polygonal strings in a closed disk \(D\), with adjacency corresponding exactly to intersection. Call a vertex **boundary-anchored** when its representing string has an endpoint on \(\partial D\).

We use the elementary disk-crossing fact:

> If \(p_1,p_2,p_3,p_4\) occur in this cyclic order on the boundary of a disk, two disjoint connected finite unions of polygonal arcs cannot respectively contain \(\{p_1,p_3\}\) and \(\{p_2,p_4\}\).

For completeness, take a simple arc in the first connected union joining \(p_1\) to \(p_3\). Within a sufficiently small neighborhood disjoint from the second union, perturb it into a crosscut whose interior lies in the disk’s interior. The two boundary intervals between \(p_1\) and \(p_3\) lie on opposite sides of this crosscut. A connected set containing \(p_2\) and \(p_4\) must cross it, a contradiction.

### Proposition 4

In such a representation, every fully pairable terminal four-set contains a vertex that is not boundary-anchored.

**Proof.** Suppose a fully pairable four-set consists entirely of boundary-anchored vertices. Its terminals are independent, so their strings are pairwise disjoint and their selected boundary endpoints are distinct.

Order these endpoints cyclically as \(p_1,p_2,p_3,p_4\). Full pairability includes the matching joining opposite points.

For each path in such a linkage, the union of the strings representing its vertices is connected: consecutive path vertices have intersecting strings. The unions for the two paths are disjoint, because the paths are anticomplete. They would therefore be disjoint connected sets joining alternating boundary points, contradicting the disk-crossing fact. ∎

### Corollary 5

Fix \(q\). On every hereditary class whose graphs admit a disk-string representation with at most \(q\) non-boundary-anchored strings,
\[
\mathrm{Flow}_2\in\mathrm P
\quad\Longleftrightarrow\quad
\mathrm{Link}_2\in\mathrm P.
\]

**Proof.** The vertices represented by the at most \(q\) exceptional strings meet every fully pairable four-set, so \(\tau(G)\le q\). Apply Theorem 3. ∎

For \(q=0\), this includes the standard outerstring class.

The representation need not be supplied to the algorithm: it is used only to prove the bound on \(\tau\). The hypothesis concerns a representation of the **whole graph**; I am not asserting the same conclusion merely from deleting \(q\) vertices to obtain an outerstring graph.

### 3.2 A necessary abundance of ambiguity

Let \(\nu(G)\) be the maximum number of pairwise vertex-disjoint fully pairable four-sets. Their linkage witnesses are allowed to overlap; only the terminal four-sets must be disjoint.

A maximal collection of such four-sets has a union meeting every fully pairable four-set. Hence
\[
\tau(G)\le 4\nu(G).
\tag{5}
\]

Consequently, a hereditary class with uniformly bounded \(\nu(G)\) also cannot give the proposed gap.

Thus a genuine separating class must support arbitrarily many pairwise disjoint fully pairable terminal four-sets. This is stronger than merely needing one ambiguous quartet.

## 4. The residual third-pairing problem is still robustly NP-complete

The preceding criterion does not make \(\mathrm{All}_3\) easy in general. Here is a strengthened masking construction.

### Theorem 6

Deciding whether all three pairings of four terminals admit induced linkages is NP-complete, even under all of the following restrictions:

- the four terminals have degree two;
- maximum degree is bounded by an absolute constant;
- two pairings have explicitly given solutions consisting of length-four paths.

**Proof.** Membership in NP follows by providing three linkage certificates.

For hardness, use the bounded-degree NP-hardness of prescribed induced two-path linkage stated in the supplied source abstract. Let an input be
\[
(G;\{c_1c_3,c_2c_4\}),
\]
where the \(c_i\) are distinct and \(\Delta(G)\le \Delta_0\) for the fixed constant supplied by that hardness result.

Add sixteen vertices forming the induced cycle
\[
a_1\ell_1b_1r_1
a_2\ell_2b_2r_2
a_3\ell_3b_3r_3
a_4\ell_4b_4r_4a_1,
\tag{6}
\]
and add the four edges \(b_i c_i\). There are no other edges between the cycle and \(G\). Call the result \(H\), with terminals \(a_1,a_2,a_3,a_4\).

#### The two easy pairings

For
\[
M_0=\{a_1a_2,a_3a_4\},
\]
use
\[
a_1\ell_1b_1r_1a_2,
\qquad
a_3\ell_3b_3r_3a_4.
\]
For
\[
M_1=\{a_1a_4,a_2a_3\},
\]
use the analogous arcs through \(b_4\) and \(b_2\).

These are induced and mutually anticomplete, and each path has length four.

#### The opposite pairing preserves the input

We claim
\[
\mathsf L(H,\{a_1a_3,a_2a_4\})
\quad\Longleftrightarrow\quad
\mathsf L(G,\{c_1c_3,c_2c_4\}).
\tag{7}
\]

For the reverse implication, extend each old terminal \(c_i\) by the tail
\[
c_i b_i\ell_i a_i.
\]
All the \(r_i\) are unused. Among the selected vertices, the added parts are exactly four disjoint tails, so inducedness and anticompleteness are preserved.

For the forward implication, consider an induced linkage for the opposite pairing on the \(a_i\).

Starting at \(a_i\), its path must first reach one of the ports
\[
b_{i-1},\ b_i,
\]
with indices modulo four. At that port, it must enter \(G\): continuing along the cycle would reach an adjacent terminal \(a_{i-1}\) or \(a_{i+1}\), which belongs to the other linkage path.

The four chosen ports are distinct. A shared port could only be chosen by two adjacent terminals, which lie on different paths and therefore cannot share a vertex.

Thus the choices form a perfect matching between the four terminals and their incident ports. This incidence graph is an \(8\)-cycle, whose two perfect matchings are
\[
a_i\longmapsto b_i\quad\text{for every }i,
\]
and
\[
a_i\longmapsto b_{i-1}\quad\text{for every }i.
\]
Both assignments preserve opposite pairing.

Finally, a path cannot make an intermediate excursion through the added cycle between two ports: every cycle route between ports encounters a terminal. Consequently, its intersection with \(G\) is a path between the corresponding \(c_i\). The two restrictions to \(G\) form an induced linkage for
\(\{c_1c_3,c_2c_4\}\), proving (7).

Since \(M_0\) and \(M_1\) are always feasible, all three pairings are feasible exactly when the original prescribed-pair instance is positive.

Each new terminal \(a_i\) has degree two. The ports have degree three, the other new vertices degree two, and each \(c_i\) gains one neighbor. Therefore
\[
\Delta(H)\le \max\{\Delta_0+1,3\}.
\]
This proves the theorem. ∎

Every one of the three flow queries on the new terminal set answers YES, regardless of the input’s answer. The construction therefore verifies the hardness of the residual information even with bounded degree and degree-two terminals.

It does **not** give a separating hereditary class. In particular,
\[
H[V(G)]=G,
\]
so taking hereditary closure exposes the original hard core. No polynomial flow algorithm for that closure is obtained.

## 5. What remains unresolved

The actual progress is:

1. Hereditary flow decision admits a useful search self-reduction.
2. A bounded transversal of fully pairable terminal four-sets yields an explicit polynomial oracle reduction from linkage to flow.
3. This covers outerstring graphs and representations with a bounded number of interior strings, without requiring the representation as input.
4. The residual third-pairing problem remains NP-complete with degree-two terminals, bounded degree, and very short certificates for the two alternatives.

The gap to the catalog problem is that an arbitrary hereditary class need not have bounded \(\tau(G)\). I have neither removed that restriction nor constructed a class with unbounded ambiguity on which flow is polynomial but prescribed linkage is NP-complete. The existential separation question is therefore unresolved by this argument.