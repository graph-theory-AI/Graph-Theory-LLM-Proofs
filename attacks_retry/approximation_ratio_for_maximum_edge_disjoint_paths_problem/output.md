```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For planar instances with distinct terminals, a set of h vertices whose deletion makes the supply graph subcubic gives a tilde-O(n^(9/19)) + 2h approximation.",
  "would_publish": false,
  "caveats": "Uses the planar MaxNDP approximation theorem quoted in the question; no improvement for all planar graphs or novelty claim is made."
}
```

# A partial result via subcubic modulators

I do not obtain an improved approximation for all planar MaxEDP instances. I obtain a structural corollary of the planar MaxNDP approximation theorem quoted in the question.

The structural parameter here is different from the feedback-vertex-set parameter in the previous attempt: we delete vertices to obtain a **subcubic graph**, not necessarily a forest. Thus the result includes subcubic planar graphs with arbitrarily large feedback vertex number.

The only ingredient reused from the previous attempt is its rooted comparison idea. I prove that ingredient below; its feedback-vertex-set LP argument is not used.

## 1. Statement and algorithmic input

I use undirected, unit-capacity, unweighted MaxEDP: each listed demand may be selected at most once. Demand endpoints within a pair are distinct.

The algorithmic input from the question is:

> **Planar MaxNDP approximation theorem.** On a planar graph with \(N\) vertices, there is a randomized polynomial-time approximation algorithm for maximum node-disjoint paths with ratio
> \[
> \alpha(N)=\widetilde O(N^{9/19}).
> \]
> We may take \(\alpha\) to be nondecreasing and at least one.

I use this as the established theorem supplied in the question, not as a new or independently updated literature survey.

Here is the partial result.

**Theorem.** Suppose \(G\) is planar, has \(n\) vertices, and the \(2k\) terminal vertices in its demand list are all distinct. Let \(X\subseteq V(G)\) be supplied, with
\[
h=|X|,\qquad \Delta(G-X)\le 3.
\]
Then MaxEDP has a polynomial-time approximation algorithm with ratio
\[
\alpha(4n)+2h
=
\widetilde O(n^{9/19})+2h.
\tag{1}
\]
Its randomness comes only from the planar MaxNDP algorithm. Every returned routing has congestion one.

The set \(X\) need not be optimized: taking all vertices of degree at least four always satisfies the hypothesis. Consequently, (1) gives an improved asymptotic ratio whenever the number of such vertices is \(o(\sqrt n)\).

A version allowing repeated terminal vertices appears in Section 5.

---

## 2. An exact planar reduction for subcubic supply graphs

The first ingredient is an exact reduction, with linear vertex blow-up.

**Lemma 1.** Let \(F\) be a subcubic planar graph whose demand endpoints are all distinct. There is a planar MaxNDP instance \(H\), with distinct degree-one terminals, such that
\[
\operatorname{OPT}_{\mathrm{NDP}}(H)
=
\operatorname{OPT}_{\mathrm{EDP}}(F).
\tag{2}
\]
Moreover, if \(F\) has \(n_F\) vertices, \(m_F\) edges, and \(k_F\) demands, then
\[
|V(H)|=m_F+4k_F\le \frac72 n_F.
\tag{3}
\]

### Construction

Start with the line graph of \(F\): for every supply edge \(e\), introduce a vertex \(q_e\), and join \(q_e\) and \(q_f\) whenever \(e\) and \(f\) share an endpoint.

For each terminal vertex \(v\) of \(F\), introduce two further vertices \(a_v,b_v\). Add

* the edge \(a_vb_v\);
* the edges \(a_vq_e\) for all supply edges \(e\) incident with \(v\).

The new demand corresponding to \((s_i,t_i)\) is \((b_{s_i},b_{t_i})\). Each \(b_v\) is a private degree-one terminal.

### Planarity

Here the subcubic hypothesis is essential.

Take a plane embedding of \(F\). Replace each original vertex \(v\) by a small disk, with one port for each incident edge. Inside the disk, join all its ports into a clique. There are at most three ports, so this clique can be drawn with all ports on the disk boundary.

If \(v\) is a terminal, place \(a_v\) inside the disk, adjacent to every port, and attach the leaf \(b_v\). With three ports, the local graph is a \(K_4\) whose outer triangle consists of the ports, together with a pendant edge. It has the required drawing inside the disk. The cases of fewer ports are immediate.

Outside the disks, connect corresponding ports along the original supply edges. Now contract each such connecting edge. These contractions produce exactly the graph \(H\) above, and preserve planarity.

### From EDP in \(F\) to NDP in \(H\)

A simple supply path with edge sequence
\[
e_1,e_2,\ldots,e_\ell
\]
for demand \((s,t)\) becomes the path
\[
b_s,a_s,q_{e_1},q_{e_2},\ldots,q_{e_\ell},a_t,b_t.
\]

For a collection of edge-disjoint supply paths:

* their \(q_e\)-vertices are disjoint because their supply edges are disjoint;
* their \(a_v,b_v\)-vertices are disjoint because all demand endpoints are distinct.

Thus the new paths are node-disjoint. Notice that a path passing through another demand's terminal vertex in \(F\) uses the corresponding line-graph clique, not that terminal's \(a_v\)-vertex.

### From NDP in \(H\) to EDP in \(F\)

Consider a path in \(H\) joining \(b_s\) to \(b_t\), and let
\[
R=\{e:q_e\text{ occurs on this path}\}.
\]
The edges in \(R\) form a connected edge set in \(F\) containing \(s\) and \(t\). Indeed, consecutive edge-vertices on the path correspond to incident supply edges; an intervening \(a_v\) also connects only edges incident with \(v\). Private leaves cannot occur internally.

Consequently, \(F[R]\) contains a simple \(s\)-\(t\) path, which can be found in polynomial time.

Node-disjoint paths in \(H\) have disjoint sets of \(q_e\)-vertices, so their extracted supply paths use disjoint edge sets. This proves (2).

Finally,
\[
m_F\le \frac32n_F,\qquad 2k_F\le n_F,
\]
which gives (3). ∎

This lemma does **not** assert that EDP and NDP are equivalent on the original subcubic graph when terminals need not be leaves. The terminal gadgets are necessary for that distinction.

---

## 3. A rooted comparison algorithm

The second ingredient applies to arbitrary undirected graphs and allows repeated terminal vertices.

**Lemma 2.** For any vertex \(v\), there is a deterministic polynomial-time algorithm returning a feasible routing of at least \(b/2\) demands whenever some feasible routing of \(b\) demands has every path containing \(v\).

The returned paths need not themselves contain \(v\).

### Proof

Give demand \(i=(s_i,t_i)\) two distinct tokens, located at \(s_i\) and \(t_i\). Tokens belonging to different demands remain distinct even when their locations coincide.

For a token set \(A\), let \(r(A)\) be the maximum number of tokens in \(A\) that can be linked to \(v\) by mutually edge-disjoint paths. A token located at \(v\) has a length-zero link.

This rank is computable by maximum flow. Introduce a source with a unit-capacity arc to the location of each token in \(A\), and replace every undirected supply edge by two oppositely directed unit-capacity arcs. Oppositely directed flow on one supply edge can be cancelled. An integral flow then decomposes into edge-disjoint undirected links.

Writing \(T_U\) for the tokens located in \(U\), the min-cut formula is
\[
r(A)=
\min_{U\subseteq V(G)\setminus\{v\}}
\left(|\delta(U)|+|A\setminus T_U|\right).
\tag{4}
\]

In particular, \(r\) is monotone, integral, and submodular. For the last assertion, take minimizing sets \(U,W\) for \(A,B\). Use cut submodularity and the elementwise inequality
\[
\begin{aligned}
|A\setminus T_U|+|B\setminus T_W|
\ge{}&
|(A\cup B)\setminus T_{U\cup W}|\\
&+|(A\cap B)\setminus T_{U\cap W}|.
\end{aligned}
\]
Together with (4), these give
\[
r(A)+r(B)\ge r(A\cup B)+r(A\cap B).
\]

Now greedily add demands, in any order, whenever all endpoint tokens of the selected demands remain jointly linkable to \(v\). Let \(A\) be the final token set, and let \(a\) be the number of selected demands. Then
\[
r(A)=|A|=2a.
\]

A rejected demand cannot become feasible after additional tokens are selected. Hence, if \(T_i\) is the two-token set of any demand \(i\),
\[
r(A\cup T_i)-r(A)\le 1.
\tag{5}
\]
For selected demands the increment is zero.

Suppose a feasible routing of \(b\) demands has every path containing \(v\), and let \(B\) be its endpoint-token set. Splitting each path at \(v\) gives edge-disjoint links for all these tokens, so
\[
r(B)=2b.
\]
Submodularity and (5) imply
\[
\begin{aligned}
2b
&=r(B)\\
&\le r(A\cup B)\\
&\le r(A)+
 \sum_{i\text{ among these }b\text{ demands}}
 \bigl(r(A\cup T_i)-r(A)\bigr)\\
&\le 2a+b.
\end{aligned}
\]
Thus \(a\ge b/2\).

Finally, compute links for all selected endpoint tokens. Concatenate the two links belonging to each demand, reversing one. Delete cycles from the resulting trail. Since different demands' links have disjoint edge sets, the resulting demand paths remain edge-disjoint. ∎

---

## 4. Proof of the approximation theorem

Let \(\mathcal D_X\) consist of demands with both endpoints outside \(X\).

The algorithm constructs the following candidate routings.

1. Apply Lemma 1 to the instance \((G-X,\mathcal D_X)\), obtaining a planar NDP instance with at most \(4n\) vertices. Run the planar MaxNDP approximation algorithm and translate its solution back. Let the resulting routing size be \(a_0\).
2. For every \(v\in X\), run Lemma 2 on the original instance. Let its routing size be \(a_v\).
3. Return the largest candidate, of size
   \[
   z=\max\bigl(\{a_0\}\cup\{a_v:v\in X\}\bigr).
   \]

Consider an optimum routing in \(G\). Partition its paths into:

* \(q_0\) paths avoiding \(X\);
* \(q_1\) paths meeting \(X\).

The first group is a feasible routing in \((G-X,\mathcal D_X)\). Lemma 1 and the NDP approximation guarantee therefore give
\[
q_0\le \alpha(4n)a_0\le \alpha(4n)z.
\tag{6}
\]

For \(v\in X\), let \(b_v\) be the number of paths in the second group containing \(v\). Every path in that group is counted at least once, so
\[
q_1\le \sum_{v\in X}b_v.
\]
Lemma 2 gives \(b_v\le 2a_v\), whence
\[
q_1\le 2\sum_{v\in X}a_v\le 2hz.
\tag{7}
\]

Combining (6) and (7),
\[
\operatorname{OPT}
=q_0+q_1
\le \bigl(\alpha(4n)+2h\bigr)z,
\]
as claimed.

The empty cases cause no difficulty: if \(X=\varnothing\), there are no rooted candidates; if the reduced instance has no demands, set \(a_0=0\).

All transformations and rooted procedures are polynomial-time. The approximation guarantee inherits the probabilistic form of the NDP algorithm. If that guarantee is formulated in expectation, taking expectations in the same inequalities proves the corresponding expected guarantee. ∎

### Consequences

For distinct-terminal planar instances:

* If \(G\) is subcubic, the ratio is
  \[
  \widetilde O(n^{9/19}).
  \]
* If a subcubic modulator has size \(h=O(n^{9/19})\), the same asymptotic ratio holds.
* If \(h=o(\sqrt n)\), the ratio is \(o(\sqrt n)\), since
  \[
  \widetilde O(n^{9/19})=o(\sqrt n).
  \]

There is no requirement that adding the demand edges preserve planarity.

---

## 5. A repeated-terminal variant without a hidden demand-size blow-up

The distinct-terminal assumption above should not be silently treated as free when the approximation is measured in the original number \(n\) of supply vertices. Adding one private leaf per demand endpoint can add \(\Theta(k)\) vertices.

There is, however, a useful version for arbitrary terminal repetitions.

Let \(X\subseteq V(G)\), and let \(d_X(v)\) be the number of endpoint occurrences at \(v\) among demands whose two endpoints lie outside \(X\). Suppose
\[
\deg_{G-X}(v)+d_X(v)\le 3
\qquad\text{for every }v\notin X.
\tag{8}
\]

Then the same bound
\[
\alpha(4n)+2|X|
\tag{9}
\]
holds, without assuming distinct original terminals.

To prove this, add a private leaf for every endpoint occurrence of every retained demand in \(G-X\), and move that demand endpoint to its leaf. Call the resulting graph \(J\).

This is an exact transformation for EDP. Condition (8) makes \(J\) subcubic, and all its demand endpoints are distinct leaves. In this situation every edge-disjoint routing is already node-disjoint: if two paths shared a vertex, that vertex could not be one of their distinct leaf endpoints, so it would be internal to both paths and require four distinct incident edges.

Moreover,
\[
|V(J)|
=(n-|X|)+\sum_{v\notin X}d_X(v)
\le 4(n-|X|)
\le 4n.
\]
Thus the planar NDP algorithm supplies the avoiding-\(X\) candidate directly. Lemma 2 and the argument in Section 4 are unchanged.

A readily computable choice satisfying (8) is
\[
X=\{v:\deg_G(v)+d(v)\ge 4\},
\]
where \(d(v)\) counts all demand-endpoint occurrences at \(v\).

---

## 6. Why this does not settle unrestricted planar MaxEDP

Two obstructions are explicit.

### Planarity does not give a small subcubic modulator

Consider the \(q\times q\) grid. Every interior vertex has degree four. If \(\Delta(G-X)\le 3\), each interior vertex either belongs to \(X\) or has a neighbor in \(X\).

One vertex of \(X\) can cover at most five interior vertices in this manner. Therefore
\[
5|X|\ge (q-2)^2.
\]
Since \(n=q^2\), every such modulator has size \(\Omega(n)\). Thus the additive \(2h\) term cannot yield a general planar improvement by this route.

### The line-graph reduction is not planar-preserving in degree four

For example, the planar octahedral graph has six vertices, twelve edges, and degree four at every vertex. Its line graph has twelve vertices and
\[
6\binom42=36
\]
edges, exceeding the planar simple-graph bound \(3\cdot12-6=30\). Hence that line graph is nonplanar.

So the exact reduction in Lemma 1 cannot simply be applied to unrestricted planar supply graphs.

Finally, the supplied catalog reports a later wall-graph hardness theorem answering the stronger-than-\(\mathcal{APX}\)-hardness alternative under that theorem's complexity assumptions. I have not re-proved or independently updated that literature result. Any hardness on planar walls also applies to general graphs.

**What is established here is only the structural approximation bound (1), together with its repeated-terminal variant (9). No new general-planar upper bound or new inapproximability theorem is claimed.**