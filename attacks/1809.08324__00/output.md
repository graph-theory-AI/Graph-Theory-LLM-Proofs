```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full generalized inequality holds for abelian bi-Cayley digraphs and the original conjecture holds for a coalescent-neighborhood class, while any k=5 counterexample must satisfy strong two-step and giant-core constraints.",
  "would_publish": false,
  "caveats": "These special cases and necessary conditions do not settle k=5 or any other currently open value, and novelty has not been checked."
}
```

# 1. Statement and scope

Let \(G\) be a bipartite digraph with parts \(A,B\), each of cardinality \(n>0\). The conjecture asserts that if

\[
\delta^+(G)>\frac{n}{k+1},
\]

then \(G\) contains a directed cycle of length at most \(2k\).

I do not obtain a proof for arbitrary \(G\), in particular not for the first open case \(k=5\). I prove two all-\(k\) special cases and derive fairly restrictive necessary conditions for a \(k=5\) counterexample.

We repeatedly use the elementary fact that every closed directed walk contains a directed cycle no longer than the walk.

# 2. Abelian bi-Cayley digraphs

This section proves not only the symmetric conjecture, but the generalized asymmetric conjecture from the source paper, for digraphs invariant under a common regular abelian action.

## 2.1 A Cayley expansion lemma

We use the following standard product-set theorem.

**Moser–Scherck–Kemperman–Wehn lemma.**  
If \(C,D\) are finite subsets of an additive group, \(0\in C\cap D\), and

\[
C\cap(-D)=\{0\},
\]

then

\[
|C+D|\ge |C|+|D|-1.
\]

It gives the usual Caccetta–Häggkvist bound for Cayley digraphs.

**Lemma 2.1.**  
Let \(\Gamma\) be a finite group, written additively, and let \(U\subseteq \Gamma\) be nonempty. If

\[
0\notin jU\qquad (1\le j\le k),
\]

then

\[
|\Gamma|\ge 1+k|U|.
\]

Here \(jU\) denotes the \(j\)-fold sumset.

**Proof.**
Put \(D=\{0\}\cup U\) and \(C_i=iD\), so \(C_i\) consists of sums of at most \(i\) elements of \(U\).

For \(0\le i<k\), we claim that

\[
C_i\cap(-D)=\{0\}.
\]

Indeed, if \(x\in C_i\cap(-U)\), then \(x\) is a sum of at most \(i\) elements of \(U\), while \(x=-u\) for some \(u\in U\). This would give \(0\in jU\) for some \(1\le j\le i+1\le k\), contrary to the hypothesis.

The product-set lemma therefore gives

\[
|C_{i+1}|=|C_i+D|\ge |C_i|+|D|-1=|C_i|+|U|.
\]

Since \(|C_0|=1\), induction gives \(|C_k|\ge1+k|U|\). As \(C_k\subseteq\Gamma\), the result follows. \(\square\)

## 2.2 The generalized conjecture for abelian bi-Cayley digraphs

Let \(\Gamma\) be a finite abelian group of order \(n\), and let \(A=\{a_x:x\in\Gamma\}\) and \(B=\{b_x:x\in\Gamma\}\). For nonempty \(S,T\subseteq\Gamma\), define a bipartite digraph by

\[
a_x\longrightarrow b_{x+s}\quad(s\in S),
\qquad
b_y\longrightarrow a_{y+t}\quad(t\in T).
\]

Thus vertices in \(A\) have out-degree \(|S|\), and vertices in \(B\) have out-degree \(|T|\).

**Theorem 2.2.**  
For every \(k\ge1\), if

\[
k|T|+|S|>|\Gamma|,
\]

then this digraph contains a directed cycle of length at most \(2k\).

Consequently, the generalized Seymour–Spirkl conjecture holds for abelian bi-Cayley digraphs: taking

\[
\alpha=\frac{|T|}{n},\qquad \beta=\frac{|S|}{n},
\]

the hypothesis \(k\alpha+\beta>1\) is sufficient.

**Proof.**
Let

\[
U=S+T.
\]

If \(0\in \ell U\), say

\[
s_1+t_1+\cdots+s_\ell+t_\ell=0
\]

with \(s_i\in S\), \(t_i\in T\), then alternating these increments gives a closed directed walk of length \(2\ell\). Thus, if there is no directed cycle of length at most \(2k\), then

\[
0\notin \ell U\qquad(1\le \ell\le k).
\]

By Lemma 2.1,

\[
n\ge 1+k|U|. \tag{2.1}
\]

Let \(H\) be the stabilizer of \(U\):

\[
H=\{h\in\Gamma:U+h=U\}.
\]

Write

\[
h=|H|,\qquad
q=\frac{n}{h},\qquad
\sigma=\frac{|S+H|}{h},\qquad
\tau=\frac{|T+H|}{h},\qquad
\nu=\frac{|U|}{h}.
\]

Kneser’s theorem gives

\[
\nu\ge \sigma+\tau-1. \tag{2.2}
\]

The numerical hypothesis and the inequalities
\(|S|\le \sigma h\), \(|T|\le\tau h\) give

\[
(k\tau+\sigma)h\ge k|T|+|S|>qh,
\]

and hence, since the quantities are integral,

\[
q\le k\tau+\sigma-1. \tag{2.3}
\]

On the other hand, (2.1) yields

\[
qh\ge 1+k\nu h,
\]

so

\[
q\ge k\nu+1\ge k(\sigma+\tau-1)+1. \tag{2.4}
\]

But the lower bound in (2.4) exceeds the upper bound in (2.3), because

\[
\begin{aligned}
\bigl[k(\sigma+\tau-1)+1\bigr]
-\bigl[k\tau+\sigma-1\bigr]
&=(k-1)(\sigma-1)+1\\
&\ge1.
\end{aligned}
\]

This contradiction proves the theorem. \(\square\)

**Corollary 2.3.**  
The catalogued conjecture holds for every bipartite digraph admitting a common regular abelian automorphism group on its two parts.

Indeed, after choosing origins in the two parts, every such digraph has the form above. If both out-degrees exceed \(n/(k+1)\), then

\[
k|T|+|S|>n.
\]

## 2.3 Sharp boundary in the symmetric abelian case

The argument also recovers the expected extremal construction.

Suppose \(k\ge2\),

\[
|S|=|T|=\frac{n}{k+1},
\]

and there is no directed cycle of length at most \(2k\). Repeating the proof with the non-strict inequality gives

\[
q\le k\tau+\sigma,
\qquad
q\ge k(\sigma+\tau-1)+1.
\]

Their difference forces \(\sigma=1\), and then equality throughout. In the symmetric case this implies

\[
q=k+1,\qquad \sigma=\tau=\nu=1.
\]

Thus \(S\) and \(T\) are full cosets of \(H\), \(\Gamma/H\) is cyclic of order \(k+1\), and the image of \(S+T\) generates the quotient. The resulting digraph is a complete uniform blow-up of the directed cycle of length \(2(k+1)\). Hence, within this abelian class, the standard extremal example is essentially the only equality example.

# 3. A second all-\(k\) special case

Call a bipartite digraph **coalescent** if

\[
x,y\in N^+(v)\quad\Longrightarrow\quad N^+(x)=N^+(y)
\tag{3.1}
\]

for every vertex \(v\). Thus all out-neighbors of a vertex are out-twins.

**Theorem 3.1.**  
The conjecture holds for coalescent bipartite digraphs, for every \(k\).

**Proof.**
Choose a vertex \(v\), and set \(X_0=N^+(v)\). By (3.1), all vertices in \(X_0\) have the same out-neighborhood; call it \(X_1\). Inductively, every vertex in \(X_i\) has out-neighborhood exactly \(X_{i+1}\). In particular, all arcs from \(X_i\) to \(X_{i+1}\) are present.

There are only finitely many vertex subsets, so the sequence eventually enters a periodic orbit. Its least period is even, say \(2r\), because the sets alternate between the two parts.

The \(r\) periodic sets lying in either fixed part are pairwise disjoint. Indeed, if two such sets \(X_i,X_j\) intersect, a common vertex has both \(X_{i+1}\) and \(X_{j+1}\) as its out-neighborhood, so \(X_{i+1}=X_{j+1}\). On the periodic orbit this contradicts minimality of the period unless \(i\equiv j\pmod{2r}\).

Every \(X_i\) is an out-neighborhood, so

\[
|X_i|>\frac{n}{k+1}.
\]

Since \(r\) pairwise disjoint such sets lie in each part,

\[
r\frac{n}{k+1}<n,
\]

and hence \(r\le k\).

Selecting one vertex from each periodic set gives a directed cycle of length \(2r\le2k\), because every \(X_i\) is complete to \(X_{i+1}\). \(\square\)

This class contains the block-cyclic extremal constructions at equality but is not contained in the abelian bi-Cayley class.

# 4. Necessary structure of a \(k=5\) counterexample

Assume now that \(G\) has parts of size \(n\),

\[
\delta^+(G)>\frac n6,
\]

and no directed cycle of length at most \(10\).

Set

\[
d=\left\lfloor\frac n6\right\rfloor+1.
\]

Delete arcs so that every vertex has out-degree exactly \(d\). This cannot create a short cycle.

## 4.1 Two-step matrices

Let \(X\) be the \(A\)-to-\(B\) adjacency matrix and \(Y\) the \(B\)-to-\(A\) adjacency matrix. Define

\[
M_A=XY,\qquad M_B=YX.
\]

Thus

\[
M_A(a,a')=
|\{b\in B:a\to b\to a'\}|.
\]

Every row of \(M_A\) and \(M_B\) has sum exactly \(d^2\), and every entry is at most \(d\).

Let \(D_A\) be the support digraph of \(M_A\), with \(a\to a'\) whenever \(M_A(a,a')>0\). A directed \(r\)-cycle in \(D_A\) lifts to a closed directed walk of length \(2r\) in \(G\). Therefore

\[
g(D_A),g(D_B)\ge6. \tag{4.1}
\]

Moreover, since every row has weight \(d^2\) and each entry is at most \(d\),

\[
\delta^+(D_A),\delta^+(D_B)\ge d>\frac n6. \tag{4.2}
\]

Thus the first open bipartite case produces two \(n\)-vertex auxiliary digraphs at the extremal \(1/6\) density, but with the additional factorization \(M_A=XY\), \(M_B=YX\).

## 4.2 Forced concentration of two-step paths

Let

\[
\mu_A=\max_{a,a'}M_A(a,a').
\]

Because \(G\) has no directed cycle of length at most \(4\), the support of \(M_A\) has neither loops nor antiparallel pairs. Consequently it has at most \(n(n-1)/2\) nonzero entries. Since the sum of all entries is \(nd^2\),

\[
nd^2\le \frac{n(n-1)}2\,\mu_A.
\]

Hence

\[
\mu_A\ge
\left\lceil\frac{2d^2}{n-1}\right\rceil
>\frac d3. \tag{4.3}
\]

The same conclusion holds for \(M_B\).

Thus any \(k=5\) counterexample contains, on each side, two vertices joined in one direction by more than \(d/3\) distinct directed two-paths. Random-like low-codegree configurations are therefore impossible.

## 4.3 Weight restriction on auxiliary six-cycles

Suppose

\[
a_0a_1\cdots a_5a_0
\]

is a directed six-cycle in \(D_A\), and put

\[
I_i=\{b\in B:a_i\to b\to a_{i+1}\}.
\]

Then the six sets \(I_i\) are pairwise disjoint. If some \(b\) belonged to both \(I_i\) and \(I_j\), choosing \(b\) as the intermediate vertex on both corresponding two-steps would produce a closed directed walk of length \(12\) with a repeated \(B\)-vertex. The segment between two consecutive occurrences of that vertex would be a proper closed directed walk of length at most \(10\), contrary to the assumption.

It follows that every directed six-cycle in \(D_A\) satisfies

\[
\sum_{i=0}^{5}M_A(a_i,a_{i+1})\le n. \tag{4.4}
\]

The analogous statement holds in \(D_B\).

The known \(k=6\) case from the source paper applies because \(d>n/7\). Hence a putative \(k=5\) counterexample has girth exactly \(12\), and in particular each auxiliary support contains at least one directed six-cycle satisfying (4.4).

The extremal blow-up at equality \(d=n/6\) has weight \(d\) on each edge of such a six-cycle, so equality holds in (4.4). The unresolved issue is a strict stability assertion: when \(6d>n\), one needs to force either an auxiliary cycle of length at most five or a six-cycle whose total edge weight exceeds \(n\). The row-sum information \(d^2\) alone does not presently yield this.

## 4.4 A giant sink strongly connected component

Here I use the generalized \(k=4\) result explicitly quoted in the prompt: a bipartite digraph with part sizes \(a,b\), \(A\)-outdegree at least \(\beta b\), \(B\)-outdegree at least \(\alpha a\), and

\[
\alpha+\beta>\frac25
\]

contains a directed cycle of length at most \(8\).

Let \(S\) be a sink strongly connected component of a putative \(k=5\) counterexample, and write

\[
a=|A\cap S|,\qquad b=|B\cap S|,\qquad
\delta=\delta^+(G).
\]

All outgoing arcs of vertices in \(S\) remain in \(S\). Applying the quoted \(k=4\) theorem inside \(S\), absence of a cycle of length at most \(8\) implies

\[
\frac{\delta}{a}+\frac{\delta}{b}\le\frac25. \tag{4.5}
\]

Since \(a,b\le n\) and \(\delta>n/6\), we have \(\delta/b>1/6\), and therefore

\[
\frac{\delta}{a}<\frac25-\frac16=\frac7{30}.
\]

Thus

\[
a>\frac{30}{7}\delta>\frac{5n}{7}.
\]

Symmetrically,

\[
b>\frac{5n}{7}. \tag{4.6}
\]

Consequently, every \(k=5\) counterexample has a unique sink strongly connected component containing more than \(5n/7\) vertices from each part.

# 5. Remaining gap

The abelian and coalescent arguments do not extend by averaging or regularization to arbitrary digraphs: averaging translates can create a cycle whose arcs come from different translates, while arbitrary arc deletion destroys the coalescent condition.

For \(k=5\), a counterexample would yield \(0\)-\(1\) matrices \(X,Y\) with row sum \(d\), \(6d>n\), such that:

1. the supports of \(XY\) and \(YX\) have directed girth at least \(6\);
2. their rows have total weight \(d^2\) and entries at most \(d\);
3. some entry on each side exceeds \(d/3\);
4. every directed six-cycle has total matrix weight at most \(n\);
5. the original digraph has a unique sink component containing more than \(5n/7\) vertices of each part.

I do not have an argument showing these conditions are inconsistent. Thus the arbitrary \(k=5\) case, and hence the full conjecture, remains open in this writeup.