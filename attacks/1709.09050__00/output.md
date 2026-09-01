```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full structural partition is not obtained, but there is an exact O(n^3) certifying algorithm, complete classifications for several planar subclasses, and a robust retract-based sufficient condition for cop number 3.",
  "would_publish": false,
  "caveats": "The algorithm is the generic finite reachability-game solver, and the structural lemmas are likely standard; arbitrary planar two-cop versus three-cop cores remain unresolved."
}
```

# Mathematical writeup

## 1. Conventions and statement of the partial results

All graphs are finite, simple, and connected. Cops and robber may stay in place. The cops choose their initial vertices first, the robber then chooses his vertex, and the cops move first. Write \(N[v]\) for the closed neighborhood of \(v\).

The following partial classification is established.

1. **Algorithmic classification.** For an \(n\)-vertex planar graph, its cop number \(1,2,\) or \(3\) can be determined, with positional strategies or evasion certificates, in \(O(n^3)\) time and space.

2. **Cop number one in \(K_4\)-minor-free graphs.**
   \[
   G\text{ connected and }K_4\text{-minor-free}
   \quad\Longrightarrow\quad
   c(G)=1\iff G\text{ is chordal}.
   \]
   Consequently, using the established bound \(c(G)\leq 2\) for outerplanar graphs,
   \[
   c(G)=
   \begin{cases}
   1,&G\text{ chordal},\\
   2,&G\text{ nonchordal},
   \end{cases}
   \qquad\text{for connected outerplanar }G.
   \]

3. **Triangle-free and feedback-vertex special cases.**
   - A connected triangle-free graph is cop-win if and only if it is a tree.
   - If \(G\) has a feedback vertex set of size at most one, then \(c(G)\leq2\). Thus such a graph has cop number \(1\) precisely when it is dismantlable, and otherwise has cop number \(2\).
   - In particular, a connected triangle-free graph with a cycle and feedback vertex number at most one has cop number \(2\).

4. **A sufficient condition for cop number three.** If a planar graph \(G\) has a move-retract \(H\) with
   \[
   \delta(H)\geq3,\qquad \operatorname{girth}(H)\geq5,
   \]
   then \(c(G)=3\).

5. **A partial girth-\(\geq5\) core classification.** Let \(G\) be connected and planar of girth at least five, and let \(K\) be its nonempty \(2\)-core. Then
   \[
   \begin{array}{c|c}
   K & c(G)\\ \hline
   K\text{ absent} & 1,\\
   K\text{ a cycle} & 2,\\
   \delta(K)\geq3 & 3.
   \end{array}
   \]
   The remaining mixed case, where \(K\) has both degree-two and degree-at-least-three vertices, contains graphs of both cop numbers \(2\) and \(3\), even among 2-connected planar graphs.

These results do not give the desired structural characterization of all planar two-cop and three-cop graphs.

---

## 2. Exact \(O(n^3)\) algorithmic classification

### 2.1 The two-cop arena

Use ordered cop positions; allowing the two cops to coincide causes no problem. The states are

\[
(x,y,r,\mathsf C),\qquad (x,y,r,\mathsf R),
\]

where \(x,y\) are cop positions, \(r\) is the robber position, and the last coordinate indicates whose turn it is.

The legal transitions are

\[
(x,y,r,\mathsf C)\longrightarrow (x',y',r,\mathsf R),
\quad x'\in N[x],\quad y'\in N[y],
\]

and

\[
(x,y,r,\mathsf R)\longrightarrow (x,y,r',\mathsf C),
\quad r'\in N[r].
\]

Let

\[
A_0=\{(x,y,r,t):r=x\text{ or }r=y\}
\]

be the capture states. Recursively define

\[
\begin{aligned}
A_{j+1}=A_j
&\cup\bigl\{(x,y,r,\mathsf C):
   \text{some legal successor lies in }A_j\bigr\}\\
&\cup\bigl\{(x,y,r,\mathsf R):
   \text{every legal successor lies in }A_j\bigr\}.
\end{aligned}
\]

Since there are only \(2n^3\) states, this stabilizes at a set \(A_\infty\).

### 2.2 Correctness

A state belongs to \(A_\infty\) if and only if the cops can force capture from that state.

Indeed, if a state first enters at stage \(j+1\), then:

- at a cops' state, the cops choose a successor of smaller rank;
- at a robber state, every robber move has smaller rank.

Thus capture is forced in finitely many moves.

Conversely, the complement \(L\) of \(A_\infty\) has the following closure properties:

- from a cops' state in \(L\), every cop move remains in \(L\);
- from a robber state in \(L\), the robber has at least one move remaining in \(L\);
- no state in \(L\) is a capture state.

Thus the robber has a positional strategy to evade forever from every state in \(L\).

It follows that two cops win precisely when

\[
\exists x,y\in V(G)\quad
\forall r\in V(G),\qquad
(x,y,r,\mathsf C)\in A_\infty.
\]

The corresponding construction with one cop decides whether \(c(G)=1\). Therefore, using the planar upper bound \(c(G)\leq3\),

\[
c(G)=
\begin{cases}
1,&\text{one cop wins},\\
2,&\text{one cop loses and two cops win},\\
3,&\text{two cops lose}.
\end{cases}
\]

The set \(A_\infty\), together with its entry ranks, certifies a winning strategy. Its complement, together with one selected escaping move at each robber state, certifies failure of two cops.

### 2.3 Complexity on planar graphs

Let

\[
s(v)=|N[v]|=d(v)+1,\qquad
S=\sum_{v\in V(G)}s(v)=n+2m.
\]

The total number of arcs out of cops' states is

\[
\sum_{x,y,r}s(x)s(y)
   =n\left(\sum_xs(x)\right)^2
   =nS^2.
\]

The total number of arcs out of robber states is

\[
\sum_{x,y,r}s(r)=n^2S.
\]

For a planar graph, \(m=O(n)\), hence \(S=O(n)\), and the arena has \(O(n^3)\) arcs. The attractor can be computed in time linear in the arena size by retaining predecessor lists and, for robber states, counters of successors not yet in the attractor. Thus the total time and explicit storage are \(O(n^3)\).

This is an exact algorithmic partition, but it is not the sought structural classification.

---

## 3. Dominated vertices and move-retracts

### 3.1 Corner deletion preserves cop number

A vertex \(v\) is a **corner** if there is a distinct vertex \(u\) such that

\[
N[v]\subseteq N[u].
\]

Let \(H=G-v\).

**Lemma 3.1.** If \(v\) is a corner, then

\[
c(G)=c(H).
\]

**Proof.**

Define \(\rho:V(G)\to V(H)\) by \(\rho(v)=u\) and \(\rho(w)=w\) for \(w\neq v\). Since \(N[v]\subseteq N[u]\), every legal move in \(G\) maps under \(\rho\) to a legal move or a stay in \(H\).

First, \(c(H)\leq c(G)\): simulate a winning strategy on \(G\), placing the actual cops in \(H\) at the projections of the simulated cop positions. A robber moving in \(H\) also makes legal moves in \(G\). If a simulated cop reaches the robber, its projection reaches the same robber vertex in \(H\).

For the reverse inequality, let \(k=c(H)\). The \(k\) cops stay in \(H\) and play their winning strategy against the projected robber position \(\rho(r)\). If a cop meets \(\rho(r)\) and \(r\in H\), capture is immediate. The only other possibility is \(r=v\) and a cop is at \(u\). On the robber's next move, he either stays at \(v\) or moves to some \(w\in N(v)\). In either case the cop at \(u\) can capture on the following move, because \(N[v]\subseteq N[u]\). Hence \(c(G)\leq c(H)\). ∎

Thus any sequence of corner deletions preserves the exact cop number.

### 3.2 General move-retract lower bound

Call a map \(\rho:V(G)\to V(H)\) a **move-retraction** if it fixes \(H\) and

\[
\rho(N_G[z])\subseteq N_H[\rho(z)]
\]

for every \(z\in V(G)\). In other words, every legal move projects to a legal move or stay.

The first half of the preceding proof gives:

**Lemma 3.2.** If \(H\) is a move-retract of \(G\), then

\[
c(H)\leq c(G).
\]

This is useful for transferring three-cop lower bounds from a controlled subgraph.

---

## 4. Cop-win special classes

### 4.1 Triangle-free graphs

**Proposition 4.1.** A connected triangle-free graph is cop-win if and only if it is a tree.

**Proof.**

In a triangle-free graph, a corner has degree at most one. Indeed, suppose \(N[v]\subseteq N[u]\), and let \(w\neq u\) be another neighbor of \(v\). Then \(w\in N[u]\), so \(u,v,w\) form a triangle.

A tree dismantles by repeatedly deleting leaves, so every tree is cop-win.

Conversely, suppose a triangle-free graph contains a cycle \(C\). In any purported dismantling order, consider the first vertex of \(C\) to be deleted. At that moment all vertices and edges of \(C\) are still present, so that vertex has degree at least two. It therefore cannot be a corner. This contradicts dismantlability. ∎

### 4.2 A necessary \(K_4\)-minor for nonchordal cop-win graphs

**Proposition 4.2.** If a connected \(K_4\)-minor-free graph is cop-win, then it is chordal.

**Proof.**

Suppose \(G\) is dismantlable and contains an induced cycle \(C\) of length at least four. In a dismantling order, let \(v\) be the first vertex of \(C\) deleted, and let \(a,c\) be its two neighbors on \(C\). Let \(u\) dominate \(v\) at this step.

The vertex \(u\) cannot lie on \(C\). If \(u=a\), for example, domination would force the chord \(ac\), contrary to \(C\) being induced; similarly for \(u=c\), and no other cycle vertex is adjacent to \(v\).

Thus \(u\notin C\), and \(u\) is adjacent to all three of \(a,v,c\). Let \(P=C-v\), the \(a\)-to-\(c\) path around the rest of the cycle. The four disjoint connected branch sets

\[
\{u\},\quad \{v\},\quad \{c\},\quad V(P)\setminus\{c\}
\]

are pairwise adjacent:

- \(u\) is adjacent to \(v,c,a\);
- \(v\) is adjacent to \(c,a\);
- the last two branch sets are adjacent along \(P\).

They therefore form a \(K_4\)-minor, a contradiction. ∎

Conversely, every connected chordal graph is dismantlable: repeatedly choose a simplicial vertex \(v\); any neighbor \(u\) dominates \(v\), since the neighbors of \(v\) form a clique. Therefore:

**Corollary 4.3.**
\[
G\text{ connected and }K_4\text{-minor-free}
\quad\Longrightarrow\quad
c(G)=1\iff G\text{ is chordal}.
\]

In particular, every outerplanar graph is \(K_4\)-minor-free. Combining this with the established outerplanar upper bound \(c(G)\leq2\) yields the complete special-case classification

\[
c(G)=
\begin{cases}
1,&G\text{ chordal},\\
2,&G\text{ nonchordal},
\end{cases}
\qquad G\text{ connected and outerplanar}.
\]

This also gives explicit subclasses:

- If \(G\) is a connected cactus, then \(c(G)=1\) exactly when every cycle is a triangle; otherwise \(c(G)=2\).
- If \(G\) is unicyclic with unique cycle \(C_\ell\), then
  \[
  c(G)=
  \begin{cases}
  1,&\ell=3,\\
  2,&\ell\geq4.
  \end{cases}
  \]
  This also follows directly by deleting all attached trees and using Lemma 3.1.

The \(K_4\)-minor condition is genuinely needed: a planar wheel with rim \(C_4\) has an induced \(4\)-cycle but is cop-win because its hub is universal.

---

## 5. A feedback-vertex upper bound

**Proposition 5.1.** If \(F\) is a feedback vertex set of \(G\), then

\[
c(G)\leq |F|+1.
\]

**Proof.**

Place one stationary cop on each vertex of \(F\). The robber must start in, and can never leave without capture, one component of \(G-F\). Each such component is a tree. One additional cop travels to that component and catches the robber there.

For completeness, one cop catches a robber in a finite tree from any initial position: on each move, the cop advances along the unique path toward the robber. The component on the robber's side of the new cop position strictly decreases whenever capture does not occur. ∎

Consequently, if \(G\) has feedback vertex number at most one, then

\[
c(G)=
\begin{cases}
1,&G\text{ dismantlable},\\
2,&G\text{ not dismantlable}.
\end{cases}
\]

For a connected triangle-free graph in this class, Proposition 4.1 simplifies this to: trees have cop number one and cyclic graphs have cop number two.

---

## 6. A local lower bound for two cops

**Proposition 6.1.** If \(H\) has minimum degree at least three and girth at least five, then two cops do not suffice on \(H\).

**Proof.**

We first show that after any two initial cop placements \(a,b\), there is a vertex outside \(N[a]\cup N[b]\).

If \(a=b\), choose a neighbor \(x\) of \(a\), and then a neighbor \(y\neq a\) of \(x\). Triangle-freeness gives \(y\notin N[a]\).

Now suppose \(a\neq b\), and assume for contradiction that \(N[a]\cup N[b]=V(H)\). Choose \(x\in N(a)\setminus\{b\}\).

If \(x\) is adjacent to \(b\), then because \(d(x)\geq3\), it has a neighbor \(y\notin\{a,b\}\). Triangle-freeness implies that \(y\) is adjacent to neither \(a\) nor \(b\), contradicting domination by \(\{a,b\}\).

Thus \(xb\notin E(H)\). Choose distinct neighbors \(y,z\neq a\) of \(x\). Neither is adjacent to \(a\). Since \(\{a,b\}\) dominates the graph, both must be adjacent to \(b\). But then

\[
x-y-b-z-x
\]

is a \(4\)-cycle, again a contradiction.

Hence the robber can initially choose \(r\) at distance at least two from both cops.

Maintain the following invariant at the beginning of every cops' turn:

\[
d(r,c_i)\geq2,\qquad i=1,2.
\]

After the cops move, neither can have reached \(r\). Fix a new cop position \(p\). At most one neighbor of \(r\) lies in \(N[p]\):

- if \(p\) is adjacent to \(r\), a second such neighbor would form a triangle;
- if \(p\) is not adjacent to \(r\), two common neighbors of \(p\) and \(r\) would form a \(4\)-cycle.

Thus the two cops together threaten at most two neighbors of \(r\). Since \(d(r)\geq3\), the robber can move to a neighbor \(s\) outside both closed cop neighborhoods. This restores the invariant.

The robber therefore evades forever. ∎

For planar graphs, the quoted three-cop upper bound now gives:

**Corollary 6.2.** Every connected planar graph of minimum degree at least three and girth at least five has cop number exactly three.

Combining this with Lemma 3.2 gives the stronger retract formulation:

**Corollary 6.3.** If a connected planar graph \(G\) has a move-retract \(H\) satisfying

\[
\delta(H)\geq3,\qquad \operatorname{girth}(H)\geq5,
\]

then \(c(G)=3\).

---

## 7. The girth-\(\geq5\) core trichotomy

Let \(G\) be connected and of girth at least five. Since \(G\) is triangle-free, its corners are exactly its current leaves. If \(G\) contains a cycle, repeatedly deleting leaves reaches its \(2\)-core \(K\), and Lemma 3.1 gives

\[
c(G)=c(K).
\]

Therefore, for connected planar \(G\) of girth at least five:

1. If the \(2\)-core is empty, \(G\) is a tree and \(c(G)=1\).

2. If the \(2\)-core is \(2\)-regular, it is a cycle \(C_\ell\), necessarily with \(\ell\geq5\), and \(c(G)=2\).

3. If the \(2\)-core has minimum degree at least three, Proposition 6.1 and planarity give \(c(G)=3\).

This leaves only cores containing both degree-two and degree-at-least-three vertices.

### Both values occur in the mixed case

The mixed case cannot be assigned a single cop number.

#### A mixed-core graph with cop number two

Let \(\Theta_{3,3,3}\) consist of three internally vertex-disjoint \(a\)-\(b\) paths

\[
a-x_i-y_i-b,\qquad i=1,2,3.
\]

It is planar, 2-connected, and has girth six. Its entire vertex set is its \(2\)-core; \(a,b\) have degree three and all other vertices have degree two.

Deleting \(a\) leaves a tree, so Proposition 5.1 gives \(c(\Theta_{3,3,3})\leq2\). It is triangle-free and contains a cycle, so Proposition 4.1 gives \(c(\Theta_{3,3,3})\neq1\). Hence

\[
c(\Theta_{3,3,3})=2.
\]

#### A mixed-core graph with cop number three

Let \(D\) be the dodecahedral graph, a planar cubic graph of girth five. Proposition 6.1 gives \(c(D)=3\).

Choose an edge \(uv\in E(D)\), retain \(uv\), and add an internally disjoint path

\[
P=u-p_1-p_2-p_3-v
\]

of length four, drawn alongside \(uv\). Call the resulting graph \(G_3\).

The graph \(G_3\) is planar and 2-connected. Every new cycle using \(P\) consists of \(P\) together with a \(u\)-\(v\) path in \(D\). Using the edge \(uv\) gives a \(5\)-cycle; any other such path has length at least four because \(D\) has girth five. Thus \(G_3\) also has girth five.

Define a move-retraction onto \(D\) by

\[
p_1\mapsto u,\qquad p_2\mapsto u,\qquad p_3\mapsto v,
\]

and fix all vertices of \(D\). Every edge of \(P\) maps either to equality or to the edge \(uv\). Hence \(D\) is a move-retract of \(G_3\), so

\[
3=c(D)\leq c(G_3)\leq3.
\]

Thus \(c(G_3)=3\). Its \(2\)-core is the whole graph and contains both degree-two and higher-degree vertices.

Therefore, even among 2-connected planar graphs of girth at least five with mixed-degree \(2\)-cores, both cop numbers two and three occur.

---

## 8. What remains open

The \(O(n^3)\) fixed-point construction gives an exact decision procedure, but it merely unfolds the game graph; it does not provide a structural description in terms of embeddings, decompositions, forbidden configurations, or canonical planar cores.

The proved structural criteria leave unresolved, among others:

- planar cores containing triangles or \(4\)-cycles;
- most 2-connected planar graphs whose \(2\)-core has degree-two chains between branching vertices;
- a structural criterion distinguishing the two mixed-core examples above;
- a useful replacement for the \(O(n^3)\)-state losing-region certificate.

Accordingly, the requested full classification of connected planar graphs with cop number \(2\) versus \(3\) remains open.