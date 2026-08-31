```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Relative to the fixed Hamilton cycle, activity has an exact reverse-search algorithm running in O(n^2 2^d), where d is the number of chords of the queried path, and every path with at most one chord is active.",
  "would_publish": false,
  "caveats": "This is an algorithmic/FPT criterion, not a closed-form characterization or a polynomial-time classification."
}
```

## 1. Formalization

Activity is not a property of a path in the bare graph \(K_n\): automorphisms fixing \(c_1\) act transitively on Hamilton paths starting at \(c_1\). The fixed Hamilton cycle is indispensable.

Let
\[
C=c_1c_2\cdots c_nc_1
\]
be the reference Hamilton cycle, and let
\[
P_0=c_1c_2\cdots c_n.
\]
For a Hamilton path
\[
P=p_1p_2\cdots p_n,\qquad p_1=c_1,
\]
and \(1\le i\le n-2\), define the suffix flip
\[
\rho_i(P)
 =p_1\cdots p_i\,p_n p_{n-1}\cdots p_{i+1}.
\]
In a general graph this flip is available when \(p_ip_n\in E(G)\). In \(K_n\) that condition is automatic. Following the source definition, it is an admissible forward flip when the broken edge
\[
p_ip_{i+1}
\]
belongs to \(E(C)\). A path is active if it is obtainable from \(P_0\) by admissible flips.

The opposite traversal \(c_1c_n\cdots c_2\) is already active, since it is \(\rho_1(P_0)\).

I address this Hamilton-path formulation, which is the one occurring in the quoted \(K_6\) example.

---

## 2. Reverse rotations

For a rooted Hamilton path \(P\), put
\[
F(P)=E(P)\setminus E(C)
\]
and let
\[
d(P)=|F(P)|
\]
be its number of chords.

### Lemma 2.1 — Reverse-move criterion

Let \(Q=q_1\cdots q_n\). Then \(Q=\rho_i(P)\) for an admissible forward flip from \(P\) if and only if
\[
P=\rho_i(Q)
\quad\text{and}\quad
q_iq_n\in E(C).
\]

#### Proof

Write
\[
P=p_1\cdots p_i\,p_{i+1}\cdots p_n.
\]
Then
\[
Q=p_1\cdots p_i\,p_n p_{n-1}\cdots p_{i+1}.
\]
Thus \(q_i=p_i\) and \(q_n=p_{i+1}\). The edge broken in the forward flip is therefore
\[
p_ip_{i+1}=q_iq_n.
\]
Also \(\rho_i\) is an involution. Hence the stated condition is exactly forward admissibility. \(\square\)

Consequently, to test activity one may start with \(Q\) and repeatedly do the following:

> Let \(x\) be the current endpoint. Choose one of the two \(C\)-neighbors \(y\) of \(x\), provided \(y\) is not the penultimate vertex, and reverse the suffix strictly after \(y\).

The path is active if and only if some such reverse sequence reaches a path containing no chords.

### Lemma 2.2 — Chords are monotone

Under a forward admissible flip,
\[
F(\rho_i(P))=F(P)
\quad\text{or}\quad
F(P)\cup\{p_ip_n\}.
\]
Under a reverse move, the chord set is unchanged or loses exactly one chord.

#### Proof

As undirected edge sets,
\[
E(\rho_i(P))
 =E(P)-\{p_ip_{i+1}\}+\{p_ip_n\}.
\]
The deleted edge is in \(C\). Thus a forward flip never deletes a chord. Reversing the argument proves the second assertion. \(\square\)

In particular, a reverse search starting from \(P\) never introduces a chord not already in \(F(P)\).

---

## 3. A compressed exact criterion

For \(S\subseteq F(P)\), let \(\mathcal H(S)\) be the collection of rooted Hamilton paths \(Q\) satisfying
\[
F(Q)=S.
\]

The following bound is the main useful observation.

### Lemma 3.1 — Few states for a fixed chord set

For every chord set \(S\),
\[
|\mathcal H(S)|\le 2(n-1).
\]

#### Proof

Fix the second endpoint \(x\ne c_1\) of \(Q\in\mathcal H(S)\), and let
\[
D=E(C)\setminus E(Q)
\]
be the omitted cycle edges.

For every vertex \(v\),
\[
\deg_Q(v)=\deg_S(v)+2-\deg_D(v).
\]
Since the endpoints of \(Q\) are \(c_1,x\), this gives
\[
\deg_D(v)
 =
 \deg_S(v)+\mathbf 1_{v=c_1}+\mathbf 1_{v=x}.
\tag{1}
\]

Write \(e_j=c_jc_{j+1}\), with indices modulo \(n\), and let
\[
\delta_j=\mathbf 1_{e_j\in D}.
\]
Equation (1) becomes
\[
\delta_{j-1}+\delta_j
 =
\deg_S(c_j)+\mathbf 1_{c_j=c_1}+\mathbf 1_{c_j=x}.
\tag{2}
\]
Once \(\delta_1\in\{0,1\}\) is chosen, all other \(\delta_j\) are forced successively by (2). Hence there are at most two possible sets \(D\) for a fixed endpoint \(x\).

For each such \(D\), the edge set
\[
S\cup(E(C)\setminus D)
\]
is fixed. If it is connected, then the degree equations make it a Hamilton path, whose orientation is uniquely determined by requiring it to start at \(c_1\). Thus there are at most two paths for each of the \(n-1\) choices of \(x\). \(\square\)

### Theorem 3.2 — FPT recognition

Given a rooted Hamilton path \(P\) with \(d=d(P)\) chords, activity can be decided by reverse search in

\[
O(n^2 2^d)
\]

time, visiting at most

\[
2(n-1)2^d
\]

states.

#### Proof

By Lemma 2.2, every reverse-reachable path has chord set \(S\subseteq F(P)\). For each fixed \(S\), Lemma 3.1 gives at most \(2(n-1)\) possible paths.

At a state \(Q=q_1\cdots q_n\), a reverse move can use only one of the two \(C\)-neighbors of \(q_n\) as pivot. Hence there are at most two outgoing reverse moves. Locating the pivots and constructing a flipped tuple takes \(O(n)\) time. A depth-first or breadth-first search therefore has the claimed bounds. It accepts exactly when it reaches \(F(Q)=\varnothing\), which by Lemma 2.1 is equivalent to activity. \(\square\)

Thus activity is fixed-parameter tractable in the number of chords. This improves the direct search through all \((n-1)!\) rooted Hamilton paths.

### Corollary 3.3 — Polynomial certificates

If \(P\) is active, it has a reverse certificate of fewer than
\[
2n(d+1)
\]
flips. Consequently, the formal recognition problem belongs to NP.

#### Proof

A successful reverse sequence has exactly \(d\) chord-deleting moves and therefore \(d+1\) phases with a fixed chord set. Within any one phase, cycles can be removed from the sequence, and Lemma 3.1 bounds the number of states by \(2(n-1)\). Hence a simple sequence uses at most
\[
(d+1)(2n-3)+d<2n(d+1)
\]
moves. \(\square\)

---

## 4. Paths with few chords

### Proposition 4.1

Every rooted Hamilton path with at most one chord is active.

#### Proof

The zero-chord paths are the two traversals of \(C\) starting at \(c_1\), and they are active.

Now suppose \(Q\) has exactly one chord \(uv\). Deleting \(uv\) from \(Q\) gives two paths \(A,B\), each consisting entirely of cycle edges. Orient the notation so that
\[
Q=c_1 A u\,vB x,
\]
where \(x\) is the other endpoint.

The two cycle edges absent from \(Q\) connect the endpoints of \(A\) and \(B\). Since \(uv\) is not a cycle edge, these omitted edges must be
\[
c_1v\quad\text{and}\quad ux.
\]
Therefore the cycle traversal starting at \(c_1\) and ending at \(v\) has the form
\[
c_1 A u\,x\overleftarrow{B}v.
\]
An admissible flip at \(u\) breaks the cycle edge \(ux\), adds the chord \(uv\), and produces exactly \(Q\). \(\square\)

The result is sharp: the six exceptional \(K_6\) paths below all have two chords.

### A criterion for two chords

Call a reverse move neutral if it preserves the chord set. Neutral moves are reversible, since they exchange one cycle edge for another.

For a fixed chord set \(S\), let \(\sim_S\) denote connectivity under neutral moves. A chord \(q_iq_{i+1}\) of \(Q=q_1\cdots q_n\) is exposed if
\[
q_iq_n\in E(C);
\]
the corresponding reverse move deletes that chord.

If \(d(P)=2\), then
\[
P\text{ is active}
\iff
\text{some }Q\sim_{F(P)}P\text{ has an exposed chord}.
\tag{3}
\]
Indeed, deleting an exposed chord leaves a one-chord path, which is active by Proposition 4.1. Conversely, the first chord-deleting move in any successful reverse sequence must be preceded only by neutral moves.

This gives an \(O(n^2)\) exact criterion for the two-chord case, since a neutral component has at most \(2(n-1)\) states.

---

## 5. The \(K_6\) computation

The following exhaustive program implements the forward definition directly.

```python
from itertools import permutations
from collections import deque

def cycle_edge(a, b, n):
    return (a - b) % n in (1, n - 1)

def flip(P, i):
    # i is zero-based; reverse the suffix strictly after P[i]
    return P[:i+1] + P[i+1:][::-1]

def active_paths(n):
    start = tuple(range(1, n + 1))
    seen = {start}
    queue = deque([start])

    while queue:
        P = queue.popleft()
        # Nontrivial suffix flips: pivot positions 0,...,n-3.
        for i in range(n - 2):
            if cycle_edge(P[i], P[i+1], n):
                Q = flip(P, i)       # Added edge exists in K_n.
                if Q not in seen:
                    seen.add(Q)
                    queue.append(Q)
    return seen

n = 6
universe = {
    (1,) + tail
    for tail in permutations(range(2, n + 1))
}
A = active_paths(n)
bad = sorted(universe - A)

assert len(universe) == 120
assert len(A) == 114
print(bad)
```

The six non-active paths are

\[
\begin{aligned}
&c_1c_2c_5c_4c_3c_6, &&
c_1c_2c_5c_6c_3c_4,\\
&c_1c_4c_3c_2c_6c_5, &&
c_1c_4c_5c_6c_2c_3,\\
&c_1c_6c_3c_2c_5c_4, &&
c_1c_6c_3c_4c_5c_2.
\end{aligned}
\]

Their obstruction can also be checked without forward enumeration. They form two closed neutral reverse components:

\[
\begin{array}{c|l}
\text{Chord set} & \text{closed component}\\ \hline
\{c_2c_5,c_3c_6\}
&
\{125436,\ 125634,\ 163254,\ 163452\}\\[2mm]
\{c_1c_4,c_2c_6\}
&
\{145623,\ 143265\}.
\end{array}
\]

For every path in either row, all nontrivial reverse predecessors remain in the same row. No chord is exposed anywhere in either component, so neither component can reach a chordless path.

---

## 6. What remains open

The reverse formulation gives an exact bounded-search criterion, an \(O(n^2 2^d)\) algorithm, NP membership, and a complete answer for paths with at most two chords via neutral components. It does not give:

1. a forbidden-pattern or other closed-form characterization;
2. a polynomial-time algorithm for unrestricted \(d\);
3. an NP-hardness result;
4. a proof that the active paths form a known permutation class.

Thus I would regard the catalogued request for a “simple criterion” as still unresolved.