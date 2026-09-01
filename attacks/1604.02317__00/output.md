```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The fixed-k conjecture remains unresolved, but stability-two instances are polynomial-time solvable when directed cycle packing, feedback vertex number, or directed circumference is bounded, including an explicit O(n^{2k}) algorithm for acyclic digraphs.",
  "would_publish": false,
  "caveats": "No hardness reduction or unrestricted polynomial algorithm is obtained; the unbounded-k interpretation is already NP-complete on tournaments."
}
```

# 1. Statement and interpretation

For a digraph \(D\), two vertices are **nonadjacent** if neither orientation of an arc joins them. Its stability number \(\alpha(D)\) is the maximum size of a pairwise nonadjacent vertex set.

The intended problem is:

> For a fixed \(k\ge 2\), given \(D\) with \(\alpha(D)\le 2\) and distinct terminal pairs
> \[
> (s_1,t_1),\ldots,(s_k,t_k),
> \]
> decide whether there are pairwise vertex-disjoint directed \(s_i\)-\(t_i\) paths.

The strongest and most natural version is \(k=2\). I do not resolve this unrestricted problem. I prove below a bounded-witness theorem which yields polynomial algorithms for several cyclically restricted classes, including all acyclic stability-two digraphs. These classes are not subsumed by a bounded semicomplete-partition assumption.

# 2. A shortest-path lemma

Let
\[
P=v_0v_1\cdots v_{r-1}
\]
be a shortest directed path between its endpoints in the subdigraph induced by \(V(P)\).

If \(j\ge i+2\), then \(v_i\to v_j\) is not an arc, since it would shortcut \(P\). Consequently, if \(v_i,v_j\) are adjacent, the only possible orientation is
\[
v_j\to v_i.
\]
In that case,
\[
v_iPv_j\cup\{v_jv_i\}
\]
is a directed cycle.

Thus every adjacency between nonconsecutive vertices of a shortest path supplies a backward chord and hence a directed cycle.

# 3. Bounded witness from bounded directed cycle packing

Let \(\nu(D)\) denote the maximum number of pairwise vertex-disjoint directed cycles in \(D\).

## Theorem 1

Let \(a,k,p\) be nonnegative integers with \(a\ge1\). Suppose that

\[
\alpha(D)\le a,\qquad \nu(D)\le p.
\]

If \(D\) contains a linkage for \(k\) prescribed terminal pairs, then it contains one using at most

\[
(2a+1)p+2ak
\]

vertices in total.

For stability number two, this becomes

\[
5p+4k
\]

vertices, hence at most

\[
5p+2k
\]

internal vertices.

### Proof

Start with any linkage \(P_1,\ldots,P_k\). For every \(i\), replace \(P_i\) by a shortest \(s_i\)-\(t_i\) path in \(D[V(P_i)]\). This preserves disjointness because the replacement only deletes vertices from \(P_i\).

Fix one resulting path
\[
P_i=v_0v_1\cdots v_{n_i-1}.
\]
Partition its vertex sequence into consecutive full blocks of \(2a+1\) vertices, followed by a remainder.

Inside a full block beginning at \(v_r\), consider
\[
v_r,v_{r+2},v_{r+4},\ldots,v_{r+2a}.
\]
These are \(a+1\) vertices. Since \(\alpha(D)\le a\), some two of them are adjacent. They are nonconsecutive on \(P_i\), so by the shortest-path observation their adjacency is a backward chord and produces a directed cycle contained entirely in this block.

Different full blocks give vertex-disjoint cycles. Moreover, blocks belonging to different linkage paths are disjoint. Therefore

\[
\sum_{i=1}^k \left\lfloor \frac{n_i}{2a+1}\right\rfloor\le \nu(D)\le p.
\]

Write
\[
n_i=(2a+1)q_i+r_i,\qquad 0\le r_i\le 2a.
\]
Then
\[
\sum_i n_i
=(2a+1)\sum_iq_i+\sum_ir_i
\le (2a+1)p+2ak.
\]
This proves the theorem. \(\square\)

## Deterministic consequence

Given an upper bound \(p\ge\nu(D)\), one can enumerate all ordered collections of candidate paths with at most

\[
L=(2a+1)p+2(a-1)k
\]

internal vertices in total. For fixed \(a,k,p\), this takes

\[
n^{L+O(1)}
\]

time.

For \(\alpha(D)\le2\), the running time is therefore

\[
n^{5p+2k+O(1)}.
\]

This is a promise algorithm if only the numerical upper bound \(p\) is supplied; a feedback vertex set gives a directly verifiable such upper bound.

# 4. Acyclic stability-two digraphs

Acyclicity gives the cleanest special case.

## Corollary 2

If \(D\) is acyclic and \(\alpha(D)\le2\), then every reachable ordered pair has a directed path with at most four vertices. Consequently, the fixed-\(k\) disjoint paths problem is solvable in

\[
O(n^{2k+O(1)})
\]

time on this class.

### Direct proof of the path bound

Let
\[
P=v_0v_1\cdots v_r
\]
be a shortest directed path. If it had at least five vertices, then
\[
v_0,v_2,v_4
\]
would be pairwise nonadjacent:

- a forward arc between any two would shortcut \(P\);
- a backward arc would form a directed cycle, contrary to acyclicity.

This is a stable set of size three, contradicting \(\alpha(D)\le2\).

### Explicit algorithm

Let \(T\) be the set of the \(2k\) terminals. For each pair \((s_i,t_i)\), list all paths of the following forms whose internal vertices avoid \(T\):

\[
s_i t_i,\qquad
s_ixt_i,\qquad
s_ixyt_i.
\]

There are \(O(n^2)\) candidates per terminal pair. Test all choices of one candidate per pair and accept exactly when the chosen paths are pairwise vertex-disjoint. Correctness follows by shortening each path of any linkage inside its own vertex set. The number of choices is \(O(n^{2k})\).

This acyclic result genuinely goes beyond the bounded-semcomplete-partition theorem in the source paper: the missing-edge graph can be an arbitrary triangle-free graph of unbounded chromatic number, oriented acyclically by a total vertex order.

# 5. Given a directed feedback vertex set

Suppose \(F\subseteq V(D)\) is a directed feedback vertex set, so \(D-F\) is acyclic, and let \(f=|F|\). Every directed cycle meets \(F\), and pairwise vertex-disjoint cycles meet distinct vertices of \(F\). Hence

\[
\nu(D)\le f.
\]

For stability number two, Theorem 1 yields:

## Corollary 3

Given a stability-two digraph together with a directed feedback vertex set of size \(f\), every yes-instance has a linkage with at most

\[
5f+4k
\]

vertices, or \(5f+2k\) internal vertices. Thus there is a deterministic algorithm with running time

\[
n^{5f+2k+O(1)}.
\]

For fixed \(f\) and fixed \(k\), this is polynomial.

## Randomized FPT implementation

The bounded witness can also be found by color-coding, yielding a one-sided randomized algorithm fixed-parameter tractable in \(f+k\).

Set
\[
L=5f+2k.
\]
Randomly color every nonterminal vertex with one of \(L\) colors.

For each commodity \(i\), dynamic programming over states \((S,v)\), where \(S\subseteq[L]\), determines whether there is a directed \(s_i\)-\(v\) path whose internal vertices have distinct colors exactly \(S\). Other terminal vertices are forbidden as internal vertices. This takes \(O(2^L(n+m))\) time per commodity.

Let \(\mathcal F_i\) be the family of color sets realized by colorful \(s_i\)-\(t_i\) paths. A second dynamic program chooses one member of every \(\mathcal F_i\), with the chosen color sets pairwise disjoint. A direct implementation takes \(O(k3^L)\) time.

If a bounded linkage has \(r\le L\) internal vertices, the probability that they all receive distinct colors is

\[
\frac{(L)_r}{L^r}\ge \frac{L!}{L^L}\ge e^{-L}.
\]

Repeating \(O(e^L\log(1/\delta))\) times gives failure probability at most \(\delta\). Any reported linkage is genuine, so the algorithm has no false positives. A coarse running-time bound is

\[
O\!\left(k(3e)^L(n+m+1)\log(1/\delta)\right).
\]

# 6. Bounded directed circumference

There is another restriction not controlled by cycle packing. Let \(c\) be the maximum number of vertices in a directed cycle of \(D\), taking \(c=0\) when \(D\) is acyclic, and put

\[
q=\max\{2,c\}.
\]

## Proposition 4

If \(\alpha(D)\le2\) and the directed circumference is at most \(c\), then every reachable pair has a directed path with at most \(2q\) vertices.

### Proof

Take a shortest path \(P=v_0\cdots v_{r-1}\). If \(j-i\ge q\), then:

- \(v_i\to v_j\) would shortcut \(P\);
- \(v_j\to v_i\) would create a directed cycle of length
  \[
  j-i+1\ge q+1>c.
  \]

Hence \(v_i,v_j\) are nonadjacent whenever their indices differ by at least \(q\).

If \(P\) had at least \(2q+1\) vertices, then
\[
v_0,v_q,v_{2q}
\]
would be a stable set of size three, a contradiction. \(\square\)

Thus fixed-\(k\) disjoint paths is solvable on this class in

\[
n^{k(2q-2)+O(1)}
\]

time by bounded-path enumeration. The acyclic result is the case \(c=0\), \(q=2\).

# 7. Why this does not settle the conjecture

Stability number two alone does not bound the length of a shortest path or the number of disjoint directed cycles. Indeed, for \(n\ge2\), define a tournament \(D_n\) on

\[
v_0,\ldots,v_{n-1}
\]

by putting

\[
v_i\to v_{i+1}\quad(0\le i<n-1)
\]
and
\[
v_j\to v_i\quad\text{whenever }j\ge i+2.
\]

Then \(\alpha(D_n)=1\), but the unique simple directed \(v_0\)-\(v_{n-1}\) path is

\[
v_0v_1\cdots v_{n-1}.
\]

Indeed, after reaching \(v_i\), its only outgoing arc to a higher-index vertex is \(v_i\to v_{i+1}\), while all lower-index out-neighbors have already been visited. The digraph also contains linearly many vertex-disjoint directed triangles.

Therefore no bounded-witness argument depending only on \(k\) and \(\alpha(D)\) can work. The semicomplete case handles such long paths by substantially different structural methods. The missing step here is either:

1. a reduction proving NP-hardness for some fixed \(k\), ideally \(k=2\), while keeping the missing-edge graph triangle-free; or
2. an algorithm capable of treating stability-two digraphs with unbounded directed cycle packing and unbounded chromatic number of the missing-edge graph.

Neither is supplied here.

# 8. The unbounded-\(k\) ambiguity

If \(k\) is part of the input, the statement is not open in the form written. The supplied literature review reports NP-completeness already on tournaments, which have stability number one. Hence it immediately holds for the class \(\alpha(D)\le2\).

Even if “stability number two” means exactly two, take a tournament instance and add one isolated nonterminal vertex \(z\). The resulting digraph has stability number exactly two: a stable set may contain \(z\) and at most one tournament vertex. Since \(z\) is isolated, it cannot participate in any terminal path, so the linkage instance is unchanged.

Thus the unresolved content is specifically the fixed-\(k\), and most importantly fixed-\(k=2\), problem.