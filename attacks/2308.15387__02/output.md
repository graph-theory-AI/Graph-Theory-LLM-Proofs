```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem is solved below for every s<=4 and for r=2s-1, with general covering-design and linear lower bounds for all s.",
  "would_publish": false,
  "caveats": "Isolated vertices are allowed, as is standard for a hypergraph on an r-element ground set; the general case s>=5 remains open, and literature novelty of the small-s results was not checked."
}
```

## 1. Statement of the partial result

Let
\[
M(r,s)=\min\bigl\{|\mathcal H|:\mathcal H\subseteq\tbinom{[r]}s
\text{ is intersecting and }\tau(\mathcal H)=s\bigr\}.
\]

Here isolated ground-set vertices are permitted. This convention is essentially forced by the case \(s=2\): an intersecting graph with cover number \(2\) is a triangle and therefore has support of size \(3\).

The following values are obtained.

### Theorem 1
For \(r\ge 2s-1\):

1. For every \(s\ge2\),
   \[
   M(2s-1,s)=\binom{2s-1}{s}.
   \]

2. For \(s=2\),
   \[
   M(r,2)=3\qquad(r\ge3).
   \]

3. For \(s=3\),
   \[
   M(5,3)=10,\qquad M(r,3)=6\quad(r\ge6).
   \]

4. For \(s=4\),
   \[
   M(r,4)=
   \begin{cases}
   35,&r=7,\\
   17,&r=8,\\
   12,&r=9,\\
   10,&r=10,\\
   9,&r\ge11.
   \end{cases}
   \]

For general \(s\), the following lower bounds hold:
\[
M(r,s)\ge
\left\lceil
\frac{\binom r{s-1}}{\binom{r-s}{s-1}}
\right\rceil,
\tag{1}
\]
and
\[
M(r,s)\ge
\begin{cases}
3,&s=2,\\
2s,&s=3,\\
2s+1,&s\ge4.
\end{cases}
\tag{2}
\]

There is also the asymptotically stronger \(r\)-independent estimate
\[
M(r,s)\ge
\left\lceil
\max_{0\le t\le s-1}
\left[
\left(\frac{s}{s-1}\right)^t(3s-2t-2)-s+1
\right]
\right\rceil,
\tag{3}
\]
which in particular gives
\[
M(r,s)\ge (2\sqrt e-1-o(1))s.
\tag{4}
\]

No claim is made that these lower bounds are best known in the literature.

---

## 2. Complementary covering-design formulation

Let \(V=[r]\), and for \(E\in\mathcal H\) put
\[
C_E=V\setminus E.
\]
Then \(|C_E|=r-s\).

The condition \(\tau(\mathcal H)=s\) is equivalent, given that \(\mathcal H\) is intersecting, to saying that no \((s-1)\)-set is a transversal. Thus, for every \(T\in\binom V{s-1}\), there is some \(E\in\mathcal H\) disjoint from \(T\), equivalently
\[
T\subseteq C_E.
\]
Hence \(\{C_E:E\in\mathcal H\}\) is an \((r,r-s,s-1)\)-covering design.

Moreover,
\[
E\cap F\ne\varnothing
\quad\Longleftrightarrow\quad
C_E\cup C_F\ne V.
\]
Thus the original problem is exactly the minimum size of an \((r,r-s,s-1)\)-covering whose blocks have no two-block union equal to \(V\).

Counting pairs \((T,E)\) with \(T\subseteq C_E\) gives
\[
|\mathcal H|\binom{r-s}{s-1}\ge\binom r{s-1},
\]
which proves (1).

When \(r=2s-1\), the complement of an \((s-1)\)-set \(T\) is the unique \(s\)-set disjoint from \(T\). Consequently every \(s\)-set must be an edge. Hence
\[
M(2s-1,s)=\binom{2s-1}{s}.
\]

The same complete \(s\)-graph on a fixed \(2s-1\) subset gives the universal upper bound
\[
M(r,s)\le\binom{2s-1}{s}
\qquad(r\ge2s-1).
\]

---

## 3. Universal lower bounds in terms of the number of edges

We first use a simple pairing observation.

### Lemma 2
Every intersecting hypergraph with \(m\) edges has a transversal of size at most
\[
\left\lceil\frac m2\right\rceil.
\]

#### Proof
Pair the edges arbitrarily, choose a point in the intersection of each pair, and if \(m\) is odd choose one point from the remaining edge. ∎

Thus \(\tau(\mathcal H)=s\) implies
\[
m\ge2s-1.
\tag{5}
\]

### Lemma 3
If \(s\ge3\), then \(m\ne2s-1\).

#### Proof
Suppose \(m=2s-1\). If a vertex has degree at least \(3\), select it and pair the at most \(2s-4\) remaining edges. This gives a transversal of size at most
\[
1+(s-2)=s-1,
\]
a contradiction. Hence every vertex has degree at most \(2\).

Fix an edge \(E\). Each of its \(s\) vertices can account for intersection with at most one other edge, but \(E\) must intersect the other \(2s-2>s\) edges. Contradiction. ∎

Therefore \(m\ge2s\) for \(s\ge3\). Equality is possible for \(s=3\), but not for \(s\ge4\).

### Lemma 4
If \(s\ge4\), then \(m\ne2s\).

#### Proof
Suppose \(m=2s\).

A vertex of degree at least \(4\), together with a pairing of the remaining at most \(2s-4\) edges, gives an \((s-1)\)-transversal. Hence every vertex has degree at most \(3\).

For each degree-three vertex \(x\), let
\[
I(x)=\{i:x\in E_i\}\in\binom{[2s]}3.
\]
Any two such triples intersect: otherwise the corresponding two vertices hit six distinct edges, and pairing the remaining \(2s-6\) edges again gives an \((s-1)\)-transversal.

Let \(t_i\) be the number of degree-three vertices in \(E_i\), and let \(b\) be the number of degree-three vertices. Since \(E_i\) must meet \(2s-1\) other edges,
\[
2t_i+(s-t_i)\ge2s-1,
\]
so
\[
t_i\ge s-1.
\tag{6}
\]
Thus
\[
3b=\sum_i t_i\ge2s(s-1).
\tag{7}
\]

On the other hand, the triples \(I(x)\) are pairwise intersecting, so
\[
\binom b2\le\sum_{i=1}^{2s}\binom{t_i}{2}.
\]
Since \(t_i\le s\),
\[
\sum_i\binom{t_i}{2}
\le\frac{s-1}{2}\sum_i t_i
=\frac{3b(s-1)}2.
\]
Consequently
\[
b\le3s-2.
\tag{8}
\]
For \(s\ge5\), (7) and (8) are incompatible:
\[
\frac{2s(s-1)}3>3s-2.
\]

It remains to exclude \(s=4\). Now \(t_i\in\{3,4\}\). Let \(x\) be the number of indices with \(t_i=4\). If \(t_i=3\), the three corresponding incidence triples must cover six distinct other indices. If \(t_i=4\), their eight companion incidences cover seven other indices, with exactly one repetition. Hence repeated pairs occur only between the \(x\) high-degree indices and form a matching. In particular, \(x\) is even.

Also
\[
3b=24+x,
\]
so \(x\) is divisible by \(3\). Thus \(x=0\) or \(x=6\).

Each pair of incidence triples intersects. A pair intersecting in two indices corresponds exactly to one of the \(x/2\) repeated pairs. Therefore
\[
\binom b2
=\sum_{i=1}^8\binom{t_i}{2}-\frac x2.
\tag{9}
\]
For \(x=0\), \(b=8\), and (9) reads \(28=24\). For \(x=6\), \(b=10\), and it reads
\[
45=6\binom42+2\binom32-3=39.
\]
Both are impossible. ∎

Lemmas 2–4 prove (2).

---

## 4. The cases \(s=2\) and \(s=3\)

For \(s=2\), an intersecting graph with no one-vertex cover is a triangle. Hence \(M(r,2)=3\).

For \(s=3\), the boundary case gives \(M(5,3)=\binom53=10\). For \(r\ge6\), Lemmas 2 and 3 give \(M(r,3)\ge6\).

On the vertex set \([6]\), take
\[
456,\quad356,\quad126,\quad125,\quad234,\quad134.
\tag{10}
\]
These six triples are pairwise intersecting. Their complements are
\[
123,\quad124,\quad345,\quad346,\quad156,\quad256,
\]
which cover all pairs of \([6]\). Thus no two vertices cover (10), while any edge is a three-vertex transversal. Hence \(\tau=3\), proving \(M(r,3)=6\) for \(r\ge6\).

---

## 5. The complete solution for \(s=4\)

We use the incidence dual. If
\[
\mathcal H=\{E_1,\dots,E_m\},
\]
then every ground-set vertex \(x\) defines a block
\[
B_x=\{i:x\in E_i\}\subseteq[m].
\]
The following are equivalent to the relevant properties of \(\mathcal H\):

- every \(i\in[m]\) belongs to exactly four blocks \(B_x\);
- every pair \(i,j\) is contained in some common block \(B_x\);
- \(\tau(\mathcal H)\) is the minimum number of blocks \(B_x\) whose union is \([m]\).

### 5.1. Nine edges require at least eleven support vertices

Suppose \(m=9\) and \(\tau=4\). A dual block has size at most \(4\): a vertex in at least five edges, followed by pairing the remaining at most four edges, would give a three-vertex transversal.

Similarly, the union of two dual blocks has size at most \(6\), since if it had size at least \(7\), the at most two uncovered edges could be hit by one further vertex.

If all dual blocks have size at most \(3\), then for any point \(i\), its four incident blocks must each be triples and must partition the other eight points into four pairs. Thus every pair of points occurs in exactly one block: the blocks form a Steiner triple system on nine points.

Every Steiner triple system on nine points has a parallel class. Indeed, for a block \(A\), exactly two blocks are disjoint from \(A\), and they must partition the remaining six points. These three blocks cover all nine points, contradicting \(\tau=4\).

Hence there is a four-element dual block \(Q\). Put \(O=[9]\setminus Q\), so \(|O|=5\). Every other dual block contains at most two points of \(O\), for otherwise its union with \(Q\) would have size at least \(7\). Covering the ten pairs of \(O\) therefore needs at least ten further dual blocks. Thus every nine-edge example has support at least
\[
1+10=11.
\tag{11}
\]

### 5.2. A nine-edge construction on eleven vertices

Let the ground vertices be
\[
z,\quad x_{ij}\quad(1\le i<j\le5).
\]
Define nine four-edges:
\[
\begin{aligned}
E_1&=\{x_{12},x_{13},x_{14},x_{15}\},\\
E_2&=\{x_{12},x_{23},x_{24},x_{25}\},\\
E_3&=\{x_{13},x_{23},x_{34},x_{35}\},\\
E_4&=\{x_{14},x_{24},x_{34},x_{45}\},\\
E_5&=\{x_{15},x_{25},x_{35},x_{45}\},\\
E_A&=\{z,x_{12},x_{13},x_{45}\},\\
E_B&=\{z,x_{12},x_{34},x_{35}\},\\
E_C&=\{z,x_{13},x_{24},x_{25}\},\\
E_D&=\{z,x_{14},x_{15},x_{23}\}.
\end{aligned}
\tag{12}
\]

The first five edges meet pairwise in the appropriate \(x_{ij}\); the last four meet at \(z\). The incidences of \(A,B,C,D\) with the pairs of \(K_5\) are
\[
\begin{aligned}
A&:\ 12,13,45,\\
B&:\ 12,34,35,\\
C&:\ 13,24,25,\\
D&:\ 14,15,23.
\end{aligned}
\tag{13}
\]
Each line in (13) is an edge cover of \(K_5\), so every one of \(E_A,E_B,E_C,E_D\) meets every \(E_i\).

There is no three-vertex transversal. If \(z\) is chosen, two more vertices \(x_{ij}\) cover at most four of \(E_1,\dots,E_5\). If \(z\) is not chosen, the three selected \(x_{ij}\)'s must form a three-edge cover of \(K_5\). To cover all four labels \(A,B,C,D\), one of those graph edges must carry \(D\), while the other two must cover \(A,B,C\). The only possible pairs for the latter are
\[
\{12,13\},\ \{12,24\},\ \{12,25\},\
\{13,34\},\ \{13,35\}.
\]
The missing pairs of \(K_5\) are respectively
\[
45,\ 35,\ 34,\ 25,\ 24,
\]
none of which carries \(D\). Thus no three vertices cover all nine edges.

Therefore
\[
M(r,4)=9\qquad(r\ge11),
\]
using (11) and padding by isolated vertices.

### 5.3. Ten vertices

On \(\mathbb Z_{10}\), let
\[
D=\{0,1,3,5\}
\]
and take the ten translates \(D+i\).

Since \(D-D=\mathbb Z_{10}\), the family is intersecting. No three translates of \(D\) cover \(\mathbb Z_{10}\). After normalizing two translates to \(D\) and \(D+a\), \(1\le a\le5\), the uncovered sets are
\[
\begin{array}{c|c}
a&\mathbb Z_{10}\setminus(D\cup(D+a))\\ \hline
1&\{7,8,9\}\\
2&\{4,6,8,9\}\\
3&\{2,7,9\}\\
4&\{2,6,8\}\\
5&\{2,4,7,9\},
\end{array}
\]
and none is contained in a translate of \(D\). By reflection, the same is true for translates of \(-D\), which are the incidence sets of individual vertices. Hence no three vertices hit all ten edges.

Thus \(M(10,4)\le10\). A nine-edge example would require support at least eleven by (11), so
\[
M(10,4)=10.
\]

### 5.4. Nine vertices

#### Lower bound

Nine edges are impossible by (11).

Suppose first that \(m=10\). In the dual, each of the ten points belongs to four blocks, so the total block incidence is \(40\), and
\[
\sum_{i<j}|B_i\cap B_j|=10\binom42=60.
\]
Every block has size at most \(5\), and every two blocks have union at most \(7\). Thus there are at least eight nonempty blocks and at most nine. If their number is \(n\), then
\[
\sum_{i<j}|B_i\cup B_j|
=(n-1)40-60.
\]
For \(n=8\) this is \(220>7\binom82=196\), and for \(n=9\) it is \(260>7\binom92=252\). Thus \(m=10\) is impossible.

Now suppose \(m=11\). Dual blocks have size at most \(6\), so there are \(n=8\) or \(9\) nonempty blocks. Every two blocks have union at most \(8\), and
\[
\sum_{i<j}|B_i\cap B_j|=11\binom42=66.
\]
If \(n=8\), then
\[
\sum_{i<j}|B_i\cup B_j|=7\cdot44-66=242>8\binom82=224.
\]
Hence \(n=9\).

Write
\[
u_{ij}=8-|B_i\cup B_j|\ge0.
\]
Since
\[
\sum_{i<j}|B_i\cup B_j|=8\cdot44-66=286,
\]
we have
\[
\sum_{i<j}u_{ij}=288-286=2.
\tag{14}
\]

Let \(d_i=|B_i|\) and \(U_i=\sum_{j\ne i}u_{ij}\). On one hand,
\[
\sum_{j\ne i}|B_i\cup B_j|=64-U_i.
\]
On the other hand, every point of \(B_i\) occurs in three other blocks, so
\[
\sum_{j\ne i}|B_i\cap B_j|=3d_i,
\]
and consequently
\[
\sum_{j\ne i}|B_i\cup B_j|
=8d_i+(44-d_i)-3d_i
=44+4d_i.
\]
Therefore
\[
U_i=20-4d_i.
\tag{15}
\]
Every \(U_i\) is thus a nonnegative multiple of \(4\). But (14) gives
\[
\sum_iU_i=4,
\]
while each \(U_i\le\sum_{a<b}u_{ab}=2\). This is impossible. Hence \(m\ge12\).

#### Construction

On \(\mathbb Z_9\), put
\[
D=\{0,2,5,6\}
\]
and take its nine translates. They are pairwise intersecting. A direct normalization shows that their three-element transversals are precisely
\[
T_i=\{i,i+1,i+2\}\qquad(i\in\mathbb Z_9).
\]

Add the three edges
\[
\{5,6,7,8\},\qquad
\{8,0,1,2\},\qquad
\{2,3,4,5\}.
\tag{16}
\]
They are pairwise intersecting. Each meets every translate of \(D\): equivalently, no translate of \(D\) is contained in any of the complementary five-point cyclic intervals.

The first edge in (16) is disjoint from \(T_0,T_1,T_2\), the second from \(T_3,T_4,T_5\), and the third from \(T_6,T_7,T_8\). Thus all three-element transversals of the original nine-edge family are destroyed. The resulting twelve-edge family has cover number four.

Therefore
\[
M(9,4)=12.
\]

### 5.5. Eight vertices

Taking complements, the desired object is equivalent to an intersecting family \(\mathcal B\subseteq\binom{[8]}4\) which covers every triple.

#### Lower bound \(17\)

For every vertex \(x\), the blocks through \(x\) must cover all pairs on the other seven vertices. Since a block through \(x\) covers three such pairs,
\[
d_{\mathcal B}(x)\ge7.
\tag{17}
\]

If \(d(x)=7\), its link is a Steiner triple system on seven points, i.e. a Fano plane. There are \(28\) nonline triples on those seven points. A block \(Q\) not containing \(x\) cannot be the complement of a Fano line, since it would then be disjoint from the corresponding block through \(x\). Every other four-set contains exactly one Fano line, and hence at most three nonline triples. Thus at least ten blocks not containing \(x\) are needed, giving
\[
|\mathcal B|\ge7+10=17.
\tag{18}
\]

Suppose \(|\mathcal B|\le16\). If \(|\mathcal B|\le15\), (17) and the degree sum force some vertex to have degree \(7\), contradicting (18). If \(|\mathcal B|=16\), either some vertex has degree \(7\), or all eight degrees equal \(8\).

We need the following elementary fact.

**Claim.** Every collection of eight triples on seven points which covers all pairs consists of a Fano plane plus one additional triple.

Indeed, every point has triple-degree at least \(3\), and no point can have degree at least \(5\): if one point lies in \(r\ge5\) triples, the \(r\) triples through it and the remaining \(8-r\) triples can cover at most
\[
r+3(8-r)=24-2r<15
\]
pairs among the other six points. Thus the degree sequence is
\[
4,4,4,3,3,3,3.
\]
The only repeated pairs are the three pairs among the degree-four points, each repeated once. A short incidence count then shows that the triple on the three degree-four points must occur; removing it leaves every pair covered exactly once, namely a Fano plane.

Returning to the degree-eight link, the eight blocks through \(x\) therefore induce a Fano plane plus one nonline triple. The remaining eight blocks can each cover at most three of the other \(27\) nonline triples, a contradiction. Hence
\[
|\mathcal B|\ge17.
\]

#### A seventeen-block construction

Let the ground set be
\[
\{\infty\}\cup\mathbb Z_7.
\]
Take the seven blocks
\[
\{\infty\}\cup L_i,\qquad
L_i=\{i,i+1,i+3\},\quad i\in\mathbb Z_7,
\tag{19}
\]
where the \(L_i\)'s are the Fano lines.

The \(28\) nonline triples of \(\mathbb Z_7\) are
\[
\begin{aligned}
A_i&=\{i,i+1,i+2\},\\
C_i&=\{i,i+1,i+5\},\\
D_i&=\{i,i+1,i+4\},\\
E_i&=\{i,i+2,i+4\}.
\end{aligned}
\]
Let
\[
\mathcal S=
\{C_2,C_4,C_6,A_2,A_3,A_6,D_0,D_5,E_1,E_4\}.
\tag{20}
\]
For every \(N\in\mathcal S\), add the block
\[
\mathbb Z_7\setminus N.
\tag{21}
\]

The ten triples in \(\mathcal S\) openly dominate all nonline triples under disjointness. This follows from
\[
\begin{aligned}
\Gamma(A_i)&=\{A_{i+3},A_{i+4},C_{i+5}\},\\
\Gamma(C_i)&=\{A_{i+2},D_{i+2},E_{i+2}\},\\
\Gamma(D_i)&=\{D_{i+2},D_{i+5},C_{i+5}\},\\
\Gamma(E_i)&=\{E_{i+1},E_{i+6},C_{i+5}\},
\end{aligned}
\tag{22}
\]
with indices modulo \(7\); substitution of (20) into (22) covers all four types and all seven indices.

Consequently:

- triples containing \(\infty\) are covered by (19);
- Fano-line triples are covered by (19);
- every nonline triple is contained in some block (21).

The family is intersecting: blocks of type (21) are four-subsets of a seven-set, while a block \(\{\infty\}\cup L_i\) could be disjoint from \(\mathbb Z_7\setminus N\) only if \(N=L_i\), and every \(N\in\mathcal S\) is a nonline.

Taking complements gives a four-uniform intersecting hypergraph with cover number four and seventeen edges. Thus
\[
M(8,4)=17.
\]

Finally, \(M(7,4)=\binom74=35\) is the boundary case \(r=2s-1\).

This completes the proof of all entries for \(s=4\).

---

## 6. A general greedy lower bound

Let a nonempty residual intersecting family have \(q\) edges. Fix one edge \(A\). Since every other edge meets \(A\),
\[
\sum_{x\in A}(d(x)-1)\ge q-1.
\]
Hence some vertex has residual degree at least
\[
1+\frac{q-1}{s}.
\]

Greedily select such a vertex. If \(q_i\) edges remain after \(i\) selections, then
\[
q_{i+1}\le\frac{s-1}{s}(q_i-1).
\]
Writing \(a=(s-1)/s\), induction gives
\[
q_t\le a^t(m+s-1)-(s-1).
\tag{23}
\]

The remaining \(q_t\) edges can be hit by pairing, using at most \(\lceil q_t/2\rceil\) further vertices. Since \(\tau=s\),
\[
t+\left\lceil\frac{q_t}{2}\right\rceil\ge s,
\]
so
\[
q_t\ge2(s-t)-1.
\]
Combining this with (23) gives
\[
m\ge
\left(\frac{s}{s-1}\right)^t(3s-2t-2)-s+1.
\]
Maximizing over \(t\) proves (3). Taking \(t=\lfloor s/2\rfloor\) proves (4).

---

## 7. A general construction from projective planes

If \(q=s-1\ge2\) is a prime power, take the Desarguesian projective plane of order \(q\) and delete one line from its line set. This leaves
\[
q^2+q=s(s-1)
\]
edges, each of size \(q+1=s\), on
\[
q^2+q+1=s^2-s+1
\]
vertices.

The family remains intersecting. A set of \(t\le q\) points meets at most
\[
tq+1
\]
lines: the first point accounts for \(q+1\) lines and each further point adds at most \(q\). Thus at least \(q\) projective lines avoid the set when \(t=q\), and at least one remains after the deletion. Hence the covering number is \(q+1=s\). Therefore
\[
M(r,s)\le s(s-1)
\]
whenever \(s-1\) is a prime power and \(r\ge s^2-s+1\).

---

## 8. Exact integer-programming formulation

For finite checks, introduce one binary variable \(x_E\) for every \(E\in\binom{[r]}s\), and minimize
\[
\sum_E x_E
\]
subject to
\[
x_E+x_F\le1
\qquad(E\cap F=\varnothing)
\]
and
\[
\sum_{\substack{E\in\binom{[r]}s\\E\cap T=\varnothing}}x_E\ge1
\qquad\left(T\in\binom{[r]}{s-1}\right).
\]
The first constraints impose intersection; the second say that no \((s-1)\)-set is a transversal. Since every selected edge is itself an \(s\)-vertex transversal of an intersecting family, these constraints are exactly equivalent to \(\tau=s\).

---

## 9. Remaining gap

The arguments above settle the entire question for \(s\le4\), as well as the boundary \(r=2s-1\) for arbitrary \(s\). They do not determine \(M(r,s)\) for general \(s\ge5\). In particular, even the stabilized value for sufficiently large \(r\)—the minimum number of edges of an unrestricted \(s\)-uniform intersecting hypergraph with covering number \(s\)—is not determined here.