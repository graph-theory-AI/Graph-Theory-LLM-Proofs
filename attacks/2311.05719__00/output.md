```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A t-clock-free graph can fail to be clock-free only by containing an induced diamond or a hole of length at most t+1, which proves cleanness when these local obstructions have bounded packing number.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains open; this uses the source-series definition of clean, which accounts for complete bipartite basic obstructions."
}
```

# 1. Statement and conventions

Write \(d_C(x,y)\) for the ordinary graph distance between \(x\) and \(y\) in the cycle \(C\). Thus a \(t\)-clock consists of a hole \(C\) and \(v\notin V(C)\) with two neighbors \(x,y\in V(C)\) satisfying \(d_C(x,y)\ge t\).

I use the source-series meaning of *clean*. For each obstruction size \(r\), let \(\mathcal O_r\) denote the corresponding basic obstructions—under the usual convention these include \(K_r\), \(K_{r,r}\), induced subdivisions of an \(r\)-wall, and induced line graphs of such subdivisions. A class is clean if its \(\mathcal O_r\)-free members have bounded treewidth for every fixed \(r\).

The proved \(t=2\) theorem therefore supplies a function \(c(r)\) such that

\[
\operatorname{tw}(G)\le c(r)
\tag{1}
\]

whenever \(G\) is clock-free and contains no member of \(\mathcal O_r\) as an induced subgraph.

I do not prove Conjecture 1.3 in full. The main partial result below reduces any possible counterexample to one containing arbitrarily many disjoint small local configurations.

# 2. A finite local witness for every allowed clock

Let \(D\) denote the diamond \(K_4-e\), and for \(t\ge3\) define

\[
\mathcal F_t=\{D,C_4,C_5,\ldots,C_{t+1}\}.
\]

## Lemma 2.1

Let \(t\ge3\). Suppose \(C\) is a hole and \(v\notin V(C)\) has two nonadjacent neighbors in \(C\), but \((C,v)\) is not a \(t\)-clock. Then \(G[V(C)\cup\{v\}]\) contains an induced member of \(\mathcal F_t\).

### Proof

Choose nonadjacent \(x,y\in N_C(v)\). Since \((C,v)\) is not a \(t\)-clock,

\[
2\le d_C(x,y)\le t-1.
\]

Let \(P\) be a shortest \(x\)-\(y\) subpath of \(C\), and list the vertices of \(N_C(v)\cap V(P)\) in their order on \(P\):

\[
x=s_0,s_1,\ldots,s_k=y.
\]

Consider two consecutive vertices \(s_i,s_{i+1}\) in this list.

If the \(s_i\)-\(s_{i+1}\) segment \(Q\) of \(P\) has at least two edges, then no internal vertex of \(Q\) is adjacent to \(v\). Since \(C\) is induced,

\[
G[V(Q)\cup\{v\}]
\]

is an induced cycle. Its length is

\[
|E(Q)|+2\in\{4,\ldots,t+1\}.
\]

Thus it is a member of \(\mathcal F_t\).

It remains to consider the case in which every two consecutive \(s_i,s_{i+1}\) are adjacent on \(C\). Then every vertex of \(P\) is adjacent to \(v\). Since \(P\) has length at least two, let \(a,b,c\) be its first three vertices. The induced graph on

\[
\{v,a,b,c\}
\]

has the edges \(va,vb,vc,ab,bc\), while \(ac\notin E(G)\) because \(C\) is a hole. It is therefore a diamond. ∎

## Corollary 2.2

For every \(t\ge3\),

\[
\{\text{\(t\)-clock-free graphs}\}
\cap
\operatorname{Forb}_{\mathrm{ind}}(\mathcal F_t)
\subseteq
\{\text{clock-free graphs}\}.
\tag{2}
\]

Consequently, the class of \(t\)-clock-free graphs with no induced diamond and no hole of length \(4,\ldots,t+1\) is clean.

In particular, the class of \(t\)-clock-free graphs of girth greater than \(t+1\) is clean.

# 3. A quantitative bounded-packing result

For a graph \(G\), let

- \(\nu_t(G)\) be the maximum number of pairwise vertex-disjoint induced subgraphs of \(G\) isomorphic to members of \(\mathcal F_t\);
- \(\tau_t(G)\) be the minimum size of a vertex set meeting every such induced copy.

Because every member of \(\mathcal F_t\) has at most \(t+1\) vertices, a maximal disjoint packing gives

\[
\tau_t(G)\le (t+1)\nu_t(G).
\tag{3}
\]

## Theorem 3.1

Let \(t\ge3\), and let \(G\) be \(t\)-clock-free and \(\mathcal O_r\)-free. Then

\[
\operatorname{tw}(G)
   \le c(r)+\tau_t(G)
   \le c(r)+(t+1)\nu_t(G).
\tag{4}
\]

### Proof

Choose \(X\subseteq V(G)\) of size \(\tau_t(G)\) meeting every induced member of \(\mathcal F_t\). Then \(G-X\) is still \(t\)-clock-free, since that property is hereditary, and \(G-X\) is \(\mathcal F_t\)-free. By Corollary 2.2, \(G-X\) is clock-free.

Also, \(G-X\) remains \(\mathcal O_r\)-free, because it is an induced subgraph of \(G\). Hence the proved clock-free theorem gives

\[
\operatorname{tw}(G-X)\le c(r).
\]

Adding all vertices of \(X\) to every bag of a tree decomposition of \(G-X\) gives

\[
\operatorname{tw}(G)\le \operatorname{tw}(G-X)+|X|
                    \le c(r)+\tau_t(G).
\]

Equation (3) gives the second inequality. ∎

## Corollary 3.2

For every fixed \(t\ge3\) and \(p\ge1\), the class of \(t\)-clock-free graphs containing no \(p\) pairwise vertex-disjoint induced members of \(\mathcal F_t\) is clean.

More explicitly, every \(\mathcal O_r\)-free graph in this class satisfies

\[
\operatorname{tw}(G)\le c(r)+(p-1)(t+1).
\]

Thus any counterexample sequence to Conjecture 1.3, for fixed \(t\) and fixed basic-obstruction size \(r\), must satisfy

\[
\nu_t(G)\longrightarrow\infty.
\]

Indeed, (4) gives the quantitative lower bound

\[
\nu_t(G)\ge
\frac{\operatorname{tw}(G)-c(r)}{t+1}.
\]

# 4. Localization of attachments to long holes

The following elementary structural fact may be useful in extending the \(t=2\) argument.

## Proposition 4.1

Let \(G\) be \(t\)-clock-free, let \(C\) be a hole of length \(n\), and let \(v\notin V(C)\). If

\[
n>3(t-1),
\]

then \(N_C(v)\) is contained in a subpath of \(C\) having at most \(t-1\) edges, and hence in at most \(t\) consecutive vertices of \(C\).

### Proof

Put \(r=t-1\) and \(S=N_C(v)\). Since \(G\) is \(t\)-clock-free,

\[
d_C(x,y)\le r
\qquad\text{for all }x,y\in S.
\tag{5}
\]

The assertion is trivial when \(|S|\le1\). Otherwise, enumerate \(S\) cyclically, and let \(g_1,\ldots,g_m\) be the positive edge-lengths of the cyclic gaps between consecutive members of \(S\).

Suppose no arc of length at most \(r\) contains all of \(S\). For every \(i\), the complementary arc of length \(n-g_i\) contains \(S\), so

\[
n-g_i>r.
\]

Together with (5), this forces \(g_i\le r\) for every \(i\).

Starting at any member of \(S\), add consecutive gaps until their sum \(q\) first exceeds \(r\). Such a proper partial sum exists because \(n-g_m>r\). By minimality,

\[
r<q\le2r<n-r,
\]

where the last inequality uses \(n>3r\). The two endpoints of this arc therefore have cyclic distance

\[
\min(q,n-q)>r,
\]

contrary to (5). Hence an arc of length at most \(r\) contains \(S\). ∎

The constant \(3\) is sharp for this purely cyclic assertion: on a cycle of length \(3(t-1)\), three vertices spaced \(t-1\) edges apart have pairwise cyclic distance \(t-1\), but do not lie in one arc of length \(t-1\).

# 5. Sharpness of Lemma 2.1

Both alternatives in Lemma 2.1 are genuinely necessary.

### The diamond cannot be omitted

Take a hole \(C=c_0c_1\cdots c_{n-1}c_0\), with \(n>t+1\), and add a vertex \(v\) adjacent precisely to \(c_0,c_1,c_2\).

Then \((C,v)\) is an ordinary clock, while all three neighbors of \(v\) have pairwise \(C\)-distance at most two, so it is not a \(t\)-clock for \(t\ge3\). The only holes are \(C\) and the hole obtained by replacing \(c_0c_1c_2\) with \(c_0vc_2\), both of length \(n\). The graph is \(t\)-clock-free and has no hole of length at most \(t+1\), but \(\{v,c_0,c_1,c_2\}\) induces a diamond.

### The upper bound \(t+1\) cannot be reduced

Let \(d=t-1\), and take a theta graph formed by three internally disjoint \(x\)-\(y\) paths of lengths \(d,d,2\), with no additional edges.

The cycle formed by the two length-\(d\) paths is a hole, and the internal vertex of the length-two path has neighbors \(x,y\) at distance \(d=t-1\) on it. Hence the graph contains an ordinary clock but no \(t\)-clock. Its shortest holes have length

\[
d+2=t+1,
\]

and it is triangle-free, hence diamond-free.

# 6. Remaining gap

The quantitative estimate (4) does not bound \(\nu_t(G)\). Large collections of disjoint diamonds or short holes do not by themselves force large treewidth: they may be attached in a tree-like fashion. What remains necessary for the full conjecture is a theorem showing that, inside an \(\mathcal O_r\)-free \(t\)-clock-free graph, a sufficiently large and sufficiently intertwined packing of these local configurations can either be separated off at bounded adhesion or converted into one of the basic induced obstructions.

No such step is established here, so this is not a proof of Conjecture 1.3.

# 7. Definition caveat: the complete-bipartite obstruction is essential

If “clean” were interpreted literally using only the three families displayed in the supplied abstract and did **not** account for complete bipartite graphs, the conjecture would be false for every \(t\ge3\).

Indeed, every hole in \(K_{n,n}\) is a \(C_4\), whose maximum cyclic distance is two. Hence \(K_{n,n}\) is \(t\)-clock-free for every \(t\ge3\), while

\[
\operatorname{tw}(K_{n,n})=n.
\]

Its induced subgraphs are complete bipartite graphs, so it has neither large induced cliques nor large induced wall subdivisions or their line graphs. Under the source-series definition, however, \(K_{n,n}\) is itself a basic complete-bipartite obstruction and therefore is not a counterexample.