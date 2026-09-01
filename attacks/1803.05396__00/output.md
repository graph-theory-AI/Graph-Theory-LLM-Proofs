```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted fixed-t problem remains open, but fixed-t NP-hardness contradicts ETH under the reported quasi-polynomial algorithm, and rigorous polynomial algorithms follow for logarithmic 3-core degree, bounded planar-deletion number, and a broader clique-cutset decomposition class.",
  "would_publish": false,
  "caveats": "No unrestricted case t >= 8 is settled; the quasi-polynomial upper bound and current literature status are taken from the supplied review."
}
```

# Mathematical writeup

## 1. Interpretation and status

For a fixed integer \(t\), let

\[
\mathcal C_t=\{G:\text{\(G\) has no induced copy of }P_t\}.
\]

The intended problem is to determine the complexity of \(3\)-Colourability on \(\mathcal C_t\), separately for every fixed \(t\ge 8\). I do not resolve any such unrestricted case.

The classes are nested:

\[
\mathcal C_s\subseteq \mathcal C_t\qquad (s<t),
\]

because every induced \(P_t\) contains an induced \(P_s\). Consequently:

- polynomial-time solvability for \(\mathcal C_t\) implies it for every \(\mathcal C_s\), \(s<t\);
- NP-hardness on \(\mathcal C_s\) implies NP-hardness on every \(\mathcal C_t\), \(t>s\).

The extracted phrase mentioning both polynomial solvability and “hardness for \(P_7\)-free graphs” cannot mean hardness of the same \(3\)-colourability problem unless \(P=NP\). The supplied source abstract instead discusses hardness for \(4\)-colourability, and I interpret the background accordingly.

---

## 2. Two complexity observations

### Proposition 2.1: Variable \(t\) is already NP-hard

If \(t\) is part of the input rather than a fixed constant, the promised problem is NP-hard.

#### Proof

Given an arbitrary graph \(G\) on \(n\) vertices, set

\[
t=\max\{8,n+1\}.
\]

Then \(G\) is automatically \(P_t\)-free, and \(G\) is \(3\)-colourable exactly when the promised instance \((G,t)\) is a yes-instance. Thus the variable-\(t\) promised problem contains unrestricted \(3\)-Colourability. \(\square\)

This does not address the intended fixed-\(t\) question.

### Proposition 2.2: Fixed-\(t\) NP-hardness would contradict ETH

Assume the reported algorithm with running time

\[
n^{O_t(\log^2 n)}=\exp(O_t(\log^3 n))
\]

for every fixed \(t\). Then, under the Exponential Time Hypothesis, \(3\)-Colourability on \(P_t\)-free graphs is not NP-hard under polynomial-time many-one reductions for any fixed \(t\).

#### Proof

Suppose it were NP-hard for a fixed \(t\). Apply the reduction to a sparse \(3\)-SAT instance of size \(m\). Its output has size \(N\le m^c\) for some constant \(c\). Running the quasi-polynomial algorithm would take

\[
\exp(O_t(\log^3 N))
 =\exp(O_t(\log^3 m))
 =2^{o(m)},
\]

contradicting the sparse form of ETH. Equivalently, NP-hardness together with the reported upper bound would imply \(\mathrm{NP}\subseteq\mathrm{QP}\). \(\square\)

Thus the usual “polynomial or NP-hard” phrasing is not an unconditional dichotomy here: an NP-intermediate outcome is logically possible.

---

## 3. An explicit pathwidth bound

The following rederives, with explicit proof, the maximum-degree phenomenon mentioned in the source paper.

### Theorem 3.1

Let \(G\) be a \(P_t\)-free graph of maximum degree \(\Delta\). Then

\[
\operatorname{pw}(G)\le (t-1)\Delta+1.
\]

#### Proof

It suffices to treat a connected component \(R_1\). Choose \(q_1\in V(R_1)\) and define a recursive ordering.

At the root, put

\[
S_1=N_{R_1}[q_1],
\]

output all vertices of \(S_1\), and then process each component \(R_2\) of \(R_1-S_1\). Since \(R_1\) is connected, there is a vertex \(q_2\in S_1\) adjacent to \(R_2\); necessarily \(q_2\ne q_1\).

More generally, a non-root recursive call consists of a connected set \(R_i\) and a vertex \(q_i\notin R_i\) having a neighbour in \(R_i\). Put

\[
S_i=N_G(q_i)\cap R_i.
\]

Output \(S_i\), and process the components \(R_{i+1}\) of \(R_i-S_i\) one at a time. For each such component choose \(q_{i+1}\in S_i\) adjacent to \(R_{i+1}\).

The vertices

\[
q_1,q_2,\ldots,q_i
\]

form an induced path. Indeed, \(q_{j+1}\) is adjacent to \(q_j\), while every descendant region of \(R_j-S_j\) contains no neighbour of \(q_j\). Thus \(q_{j+1}\) has no neighbour among \(q_1,\ldots,q_{j-1}\). Since \(G\) is \(P_t\)-free, the recursion has depth at most \(t-1\).

Consider a prefix of the resulting depth-first vertex ordering. Let its frontier be the already output vertices having a neighbour not yet output. Any completed child region has no edge to a later sibling, and all its edges leaving that region end in an already output ancestor separator. Hence every frontier vertex lies in one of the separator sets on the active recursion stack. Their total size is at most

\[
|S_1|+\sum_{i=2}^{t-1}|S_i|
   \le (\Delta+1)+(t-2)\Delta
   =(t-1)\Delta+1.
\]

The vertex-separation characterization of pathwidth now gives the asserted bound. Explicitly, if \(v_1,\ldots,v_n\) is this ordering and \(F_i\) is its frontier after \(v_i\), then

\[
X_i=F_{i-1}\cup\{v_i\}
\]

is a path decomposition of width at most \((t-1)\Delta+1\). \(\square\)

### Corollary 3.2: A core-degree algorithm

Let \(C_3(G)\) denote the \(3\)-core of \(G\), obtained by repeatedly deleting vertices of current degree at most two, and put

\[
d=\Delta(C_3(G)).
\]

For fixed \(t\), \(3\)-Colourability of a \(P_t\)-free graph can be decided in time

\[
3^{(t-1)d+O(1)}n^{O(1)}.
\]

In particular, the problem is polynomial-time solvable whenever \(d=O(\log n)\).

#### Proof

A graph is \(3\)-colourable if and only if its \(3\)-core is. One direction is immediate. Conversely, reinsert the deleted vertices in reverse order. At reinsertion, a deleted vertex has at most two already coloured neighbours, so one of the three colours remains available.

The core is an induced subgraph and hence is still \(P_t\)-free. Apply Theorem 3.1 and standard dynamic programming over the resulting path decomposition. A width-\(w\) decomposition has at most \(3^{w+1}\) colour states per bag. \(\square\)

This is strictly stronger than merely assuming \(\Delta(G)=O(\log n)\): arbitrary high-degree trees, leaves, and other degree-two appendages disappear in the core.

---

## 4. Clique cutsets and small dominating sets

Two elementary reductions enlarge the tractable region.

### Lemma 4.1: Clique-cutset decomposition

Let \(S\) be a clique of size at most three such that \(G-S\) has components \(C_1,\ldots,C_q\). Then

\[
G\text{ is \(3\)-colourable}
\quad\Longleftrightarrow\quad
G[S\cup C_i]\text{ is \(3\)-colourable for every }i.
\]

#### Proof

The forward implication is immediate. Conversely, choose a \(3\)-colouring of each piece. Since \(S\) is a clique, every colouring restricts to an injective assignment on \(S\). Any two injective assignments \(S\to\{1,2,3\}\) differ by a permutation of the three colours. Permuting the colouring of each piece makes all restrictions agree on \(S\), after which the colourings can be united. \(\square\)

A \(K_4\) can first be rejected. Thereafter all clique cutsets have size at most three and can be found by exhaustive polynomial-time search. Every resulting piece remains \(P_t\)-free.

### Lemma 4.2: Dominating-set algorithm

If a graph \(H\) has a given dominating set \(D\) of size \(d\), then its \(3\)-colourability can be decided in time

\[
3^d |V(H)|^{O(1)}.
\]

#### Proof

Enumerate the proper colourings of \(H[D]\). For a fixed colouring \(\phi\), every vertex \(v\notin D\) receives the list

\[
L(v)=\{1,2,3\}\setminus \phi(N(v)\cap D).
\]

Since \(D\) dominates \(H\), every such list has size at most two. List-colouring with lists of size at most two reduces to \(2\)-SAT: for every edge \(xy\) and colour \(c\in L(x)\cap L(y)\), add the clause forbidding \(x=y=c\). \(\square\)

For fixed \(d\), a dominating set of size at most \(d\) can be found by enumerating \(O(n^d)\) subsets.

### Corollary 4.3: A hybrid polynomial subclass

Fix \(t,d\), and a constant \(c\). There is a polynomial-time algorithm for \(P_t\)-free graphs satisfying the following condition:

> after recursive clique-cutset decomposition, every leaf piece \(H\) is either  
> 1. bipartite;  
> 2. has domination number at most \(d\); or  
> 3. satisfies \(\Delta(C_3(H))\le c\log n\).

Bipartite pieces are accepted directly, the second kind is handled by Lemma 4.2, and the third by Corollary 3.2. Lemma 4.1 combines the answers.

No claim is made that all \(P_t\)-free graphs satisfy this structural condition.

---

## 5. Bounded planar-deletion number

This gives another tractable subclass not controlled by maximum degree.

### Theorem 5.1

Fix \(t\) and \(k\). Suppose \(G\) is \(P_t\)-free and has a set \(A\), \(|A|\le k\), such that \(G-A\) is planar. Given \(A\), list \(3\)-colourability—and hence ordinary \(3\)-colourability—can be decided in time

\[
3^{\,k+3(t-2)+O(1)}n^{O(1)}.
\]

If \(A\) is not supplied but \(k\) is fixed, it can be found in \(n^{k+O(1)}\) time by exhaustive search and planarity testing.

#### Proof

Every connected \(P_t\)-free graph has diameter at most \(t-2\): a shortest path is induced, so a pair at distance at least \(t-1\) would yield an induced \(P_t\).

Each component of \(G-A\) is planar, \(P_t\)-free, and therefore has radius at most \(t-2\). The standard planar radius/treewidth bound gives

\[
\operatorname{tw}(H)\le 3\,\operatorname{rad}(H)+O(1)
\]

for every connected planar graph \(H\). One proof uses a BFS tree and the planar tree-cotree construction; the resulting bags are unions of a constant number of root paths.

Thus

\[
\operatorname{tw}(G-A)\le 3(t-2)+O(1).
\]

Adding every vertex of \(A\) to every bag gives

\[
\operatorname{tw}(G)\le k+3(t-2)+O(1).
\]

Standard tree-decomposition dynamic programming solves list \(3\)-colourability within the stated time. \(\square\)

---

## 6. A structural stress test

The preceding degree, domination, and planar-deletion conditions do not by themselves capture all \(P_8\)-free \(3\)-colourable graphs.

For integers \(m\ge1\) and \(r\ge3\), define \(F_{m,r}\) as follows. Take adjacent vertices \(u,v\). For each \(i\in\{1,\ldots,m\}\), introduce pairwise disjoint independent sets

\[
A_i,\ B_i,\ C_i
\]

of size \(r\), and put in all edges

\[
uA_i,\qquad A_iB_i,\qquad B_iC_i,\qquad C_iv,
\]

together with \(uv\), and no others.

### Properties

1. **\(F_{m,r}\) is \(3\)-colourable.**  
   Assign
   \[
   u=1,\quad v=2,\quad A_i=2,\quad B_i=3,\quad C_i=1.
   \]

2. **It is non-bipartite and \(2\)-connected.**  
   Choosing one vertex from each of \(A_i,B_i,C_i\) gives a \(5\)-cycle
   \[
   u-a-b-c-v-u.
   \]
   Deleting any one vertex leaves the graph connected.

3. **Its entire vertex set is its \(3\)-core.**  
   Vertices in \(A_i,C_i\) have degree \(r+1\), vertices in \(B_i\) have degree \(2r\), and
   \[
   \deg(u)=\deg(v)=mr+1.
   \]

4. **Its domination number is at least \(m\).**  
   No vertex outside \(A_i\cup B_i\cup C_i\) is adjacent to a vertex of \(B_i\). Hence every dominating set must meet every branch \(A_i\cup B_i\cup C_i\).

5. **Its planar-deletion number is at least \(m(r-2)\).**  
   Each \(A_i\cup B_i\) contains a \(K_{r,r}\). To destroy all \(K_{3,3}\) subgraphs, at least \(r-2\) vertices must be deleted from \(A_i\cup B_i\) for each \(i\).

6. **It is \(P_8\)-free.**

For the last assertion, each of \(A_i,B_i,C_i\) is a false-twin class. An induced path on at least four vertices contains at most one vertex from any false-twin class: if false twins \(x,y\) both occur, inducedness forces a subpath \(x-z-y\), and the path cannot extend at either end.

It therefore suffices to inspect the quotient with paths

\[
u-A_i-B_i-C_i-v
\]

and edge \(uv\). An induced path:

- using neither \(u\) nor \(v\) lies in one branch and has at most three vertices;
- using exactly one of \(u,v\) can use at most three vertices in each of two branches, hence at most seven vertices;
- using both has \(u,v\) consecutive, and can extend by at most two vertices on each side, hence has at most six vertices.

Thus no induced \(P_8\) exists.

This family shows that even \(2\)-connected \(P_8\)-free yes-instances may simultaneously have unbounded maximum \(3\)-core degree, domination number, and planar-deletion number. It also explains the relevance of clique-cutset decomposition: \(\{u,v\}\) is a clique cutset, and each resulting one-branch piece has a dominating set of size three.

---

## 7. Remaining gap

The unrestricted problem would still require handling clique-cutset-free, non-bipartite \(P_t\)-free pieces whose \(3\)-cores have large maximum degree and which have no bounded dominating set or bounded planar modulator. Nothing above proves that such pieces have a further useful decomposition, nor does it give an NP-hardness construction.

Accordingly:

- no fixed \(t\ge8\) is classified here;
- the ETH argument only makes NP-hardness conditionally implausible;
- the structural algorithms give rigorous tractable subclasses and localize some of the obstruction, but do not reach the full conjectured polynomial-time algorithm.