```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain L_3(n)=3n/2+sqrt(n)/2+O(1), L_3^star(n)=5n/3+O(1), and L_4(n)=7n/4+O(sqrt(n)), but not the general minimum.",
  "would_publish": false,
  "caveats": "The proofs below are independent deductions; novelty relative to the full source text is unverified, and general t remains unresolved."
}
```

# 1. Results and scope

Write \(L_t(n)\) for the minimum length of a \(t\)-reachability network, and \(L_t^\star(n)\) for the minimum with all transpositions incident with \(1\).

I obtain the following partial results.

**Theorem A.** As \(n\to\infty\),
\[
\boxed{L_3(n)=\frac32n+\frac12\sqrt n+O(1).}
\]
More explicitly, for \(n\ge3\),
\[
\frac32(n-3)+\frac12\sqrt{n-3}
\le L_3(n)
\le \frac32n+\frac12\sqrt n+3.
\]

**Theorem B.** For \(n\ge3\),
\[
\boxed{
\left\lceil\frac{5n-16}{3}\right\rceil
\le L_3^\star(n)
\le \left\lfloor\frac{5n}{3}\right\rfloor+5.
}
\]
In particular, \(L_3^\star(n)=5n/3+O(1)\).

**Theorem C.** As \(n\to\infty\),
\[
\boxed{L_4(n)=\frac74n+O(\sqrt n).}
\]
The lower bound proved here is
\[
L_4(n)\ge \frac74(n-4).
\]
For the star variant, I also obtain
\[
\boxed{L_4^\star(n)\ge \frac95(n-4)-1.}
\]

Thus the unrestricted leading constants for \(t=3,4\), and the star leading constant for \(t=3\), are determined by these arguments. Exact additive constants, general \(t\), and the star problem for \(t\ge4\) are not determined.

The main new device in the argument is a count of persistent token bottlenecks. For the sharp \(t=3\) upper bound, I combine this with a three-dimensional linear-algebra certificate for reachability. This is a different approach from the previous high-girth-core construction.

I have not independently checked the full source paper, so I do **not** certify that these partial conclusions are absent from it.

---

# 2. A bottleneck-color accounting lemma

Fix \(s\ge2\), and track only the tokens initially at \(1,\ldots,s\).

A position is **live** at a given time if some choice of switches in the preceding prefix can put one of these \(s\) tokens there. Initially exactly \(s\) positions are live. At a transposition:

* if neither endpoint is live, nothing changes;
* if exactly one endpoint is live, both become live;
* if both endpoints are live, the live set is unchanged.

Call a switch of the second kind an **activation**, and one of the third kind a **mixing switch**.

In an \(s\)-reachable network, all \(n\) positions are live at the end. Hence there are exactly \(n-s\) activations. If there are \(k\) mixing switches, then
\[
\ell\ge n-s+k. \tag{2.1}
\]
For a star word, the hub is always live, so equality holds.

Assign colors to live positions as follows.

* Initially, give the \(s\) live positions distinct colors.
* At an activation, give both endpoints the color of the previously live endpoint.
* At a mixing switch, give its two outputs two fresh colors.

There are therefore \(s+2k\) colors in total.

## 2.1. The key property

For any fixed choice of switches, each color is visited, over its entire lifetime, by at most one of the tracked token identities.

Indeed, a color begins on one wire at one time. An activation cannot inject a tracked token from its dead endpoint. A mixing switch that could inject a different tracked token replaces the old color by fresh colors.

Consequently:

1. Two final positions cannot have the same color in an \(s\)-reachable network.
2. If a mixing switch has parent colors \(a,b\) and child colors \(c,d\), all tracked tokens ever visiting these four colors belong to the at most two token identities visiting \(a,b\).
3. More generally, outputs whose token histories are confined to \(r\) specified colors cannot simultaneously contain more than \(r\) tracked tokens.

Call a color **marked** if it occurs at a final position. There are exactly \(n\) marked colors. Put
\[
h=s+2k-n,
\]
the number of unmarked colors.

Let \(q_i\) be the number of mixing switches having exactly \(i\) marked child colors, for \(i=0,1,2\). If \(a\le s\) initial colors are marked, then
\[
n=a+q_1+2q_2,\qquad
h=(s-a)+2q_0+q_1. \tag{2.2}
\]

When \(s\ge3\), a mixing switch has at most two distinct marked colors among its parents and children. Otherwise three final positions would have token histories confined to two colors.

In particular, a switch counted by \(q_2\) has two distinct, unmarked parent colors.

---

# 3. Lower bounds

## 3.1. The square-root excess for three tokens

Take \(s=3\).

Two different switches counted by \(q_2\) cannot have the same unordered pair of parent colors. Their four marked children would otherwise all have token histories confined to those two colors, contradicting three-reachability.

Thus
\[
q_2\le \binom h2.
\]
Also \(q_1\le h\), by (2.2). Therefore
\[
n=a+q_1+2q_2
\le 3+h+2\binom h2
=3+h^2.
\]
Hence
\[
h\ge\sqrt{n-3}.
\]
Since \(k=(n-3+h)/2\), equation (2.1) gives
\[
\boxed{
L_3(n)\ge
\frac32(n-3)+\frac12\sqrt{n-3}.
} \tag{3.1}
\]

This is the lower half of Theorem A.

## 3.2. A stronger three-token lower bound for star words

In a star word, the hub child color of one mixing switch is the hub parent color of the next mixing switch: intervening activations do not change the hub color.

A \(q_2\)-switch has a marked hub child. Therefore the next mixing switch cannot also be a \(q_2\)-switch, since it would then have a marked parent and two marked children.

Thus the \(q_2\)-switches are nonconsecutive in the sequence of mixing switches, giving
\[
q_2\le \frac{k+1}{2}.
\]
Using (2.2),
\[
n\le3+q_1+2q_2
\le3+k+q_2
\le3+\frac{3k+1}{2}.
\]
It follows that
\[
k\ge\frac{2n-7}{3}.
\]
Since a star word has length \(n-3+k\),
\[
\boxed{L_3^\star(n)\ge\frac{5n-16}{3}.} \tag{3.2}
\]

## 3.3. Four tokens

Now track \(s=4\) tokens.

The parent-color pairs of two different \(q_2\)-switches must be disjoint. If they shared a color, their four marked children would have token histories confined to at most three colors.

Consequently,
\[
2q_2\le h.
\]
Together with \(q_1\le h\), this gives
\[
n\le4+q_1+2q_2\le4+2h.
\]
Thus
\[
h\ge\frac{n-4}{2},
\qquad
k=\frac{n-4+h}{2}\ge\frac34(n-4).
\]
Therefore
\[
\boxed{L_4(n)\ge\frac74(n-4).} \tag{3.3}
\]

## 3.4. A refinement for four-token star words

Partition the \(q_1\)-switches into:

* \(b\) **bad** switches, having a marked parent;
* \(g\) **good** switches, having no marked parent.

A bad switch has exactly one marked parent: two marked parents and its marked child would contradict three-reachability.

Its unmarked child cannot be a parent of a \(q_2\)-switch. To see this, write its parents as \(A,B\), where \(A\) is marked, and its children as \(M,U\), where \(M\) is marked. If a later \(q_2\)-switch had parents \(U,V\) and marked children \(P,Q\), then the four marked colors
\[
A,M,P,Q
\]
would have token histories confined to \(A,B,V\), contradicting four-reachability.

Since the parent pairs of \(q_2\)-switches are disjoint,
\[
2q_2\le h-b\le4+2q_0+g. \tag{3.4}
\]
Also, the mixing switch following a \(q_2\)-switch is either a \(q_0\)-switch or a bad \(q_1\)-switch. Hence
\[
q_2\le q_0+b+1. \tag{3.5}
\]

Put \(c=q_2\), so \(k=q_0+b+g+c\). Equations (3.4)–(3.5) imply
\[
b\ge c-q_0-1,\qquad
g\ge2c-2q_0-4.
\]
Therefore
\[
\begin{aligned}
5k-4(b+g+2c)
&=5q_0+b+g-3c\\
&\ge2q_0-5\\
&\ge-5.
\end{aligned}
\]
Since \(n-4\le b+g+2c\),
\[
k\ge\frac45(n-4)-1.
\]
Adding the \(n-4\) activations proves
\[
\boxed{L_4^\star(n)\ge\frac95(n-4)-1.} \tag{3.6}
\]

---

# 4. Linear algebra as a reachability certificate

The following elementary observation is useful for the sharp three-token construction.

**Lemma 4.1.** Consider a transposition word
\[
\tau_1,\ldots,\tau_\ell
\]
on \(n\) positions. For each \(\tau_i=(a,b)\), choose an \(n\times n\) matrix \(M_i\) that is the identity outside its principal \(2\times2\) block on \(a,b\).

Start with the \(n\times s\) matrix
\[
A_0=\begin{pmatrix}I_s\\0\end{pmatrix},
\qquad
A_\ell=M_\ell\cdots M_1A_0.
\]
If the rows indexed by \(S\), where \(|S|=s\), form a nonsingular minor of \(A_\ell\), then some subword of the transposition word maps the occupied set \([s]\) onto \(S\).

**Proof.** Repeated Cauchy–Binet expansion expresses that minor as a sum over sequences
\[
S_0=[s],S_1,\ldots,S_\ell=S
\]
of products
\[
\prod_{i=1}^{\ell}\det M_i[S_i,S_{i-1}].
\]
A nonzero sum has a nonzero summand.

For a matrix supported on the block \(\{a,b\}\), a nonzero minor between two \(s\)-sets requires the sets to agree outside \(\{a,b\}\). Hence
\[
S_i=S_{i-1}
\quad\text{or}\quad
S_i=\tau_i(S_{i-1}).
\]
Choosing the corresponding optional switches routes the occupied set. ∎

This certifies **unlabelled** reachability. For \(s=3\), prepend
\[
Q=((1,2),(1,3),(1,2)).
\]
Its subwords realize every permutation of \(\{1,2,3\}\).

If a chosen subword sends the three input tokens bijectively onto a target set, a suitable initial permutation of their labels realizes any prescribed ordering on that target set. Thus:

> An unlabelled three-token network becomes a labelled three-reachability network after adding three switches.

The matrices in Lemma 4.1 are certificates, not additional operations permitted in the network.

---

# 5. A sharp three-token construction

We work over \(\mathbb Q\), viewing nonzero vectors in \(\mathbb Q^3\) as projective points. A projective line is a two-dimensional vector subspace.

## 5.1. Producing many core directions cheaply

**Lemma 5.1.** For every even \(m\ge4\), there is a word of
\[
\frac32m-3
\]
transpositions on \(m\) core positions, with a choice of matrices as in Lemma 4.1, producing \(m\) distinct projective points with the following properties:

1. Every line containing at least three of the points contains exactly four.
2. There are precisely
   \[
   r=\frac{m-4}{2}
   \]
   such four-point lines.
3. There is a perfect matching \(M\) on the \(m\) points whose matched pairs determine distinct projective lines.
4. The total number of distinct lines determined by pairs of points is
   \[
   D(m)=\binom m2-5r
   =\frac{m^2-6m+20}{2}. \tag{5.1}
   \]

**Proof.**

Start with \(e_1,e_2,e_3,0\). The three switches
\[
(1,4),\quad(2,4),\quad(1,3)
\]
can produce the rows
\[
e_1+e_3,\quad e_1+e_2,\quad e_1+2e_3,\quad 2e_1+e_2.
\]
For example, first copy \(e_1\) into row \(4\), keeping row \(1\), and then use the block
\[
\begin{pmatrix}1&1\\1&2\end{pmatrix}
\]
at each of the other two switches.

No three of these four projective points are collinear. Take the initial matching
\[
M=\{\{1,3\},\{2,4\}\}.
\]

Inductively, choose an **ordinary pair** \(a,b\): its line contains exactly those two current points. Also require \(\{a,b\}\notin M\).

Introduce two zero rows \(u,v\). The switches
\[
(a,u),\quad(b,v),\quad(u,v)
\]
can:

* copy the vectors at \(a,b\) into \(u,v\), keeping the old rows unchanged;
* replace \(u,v\) by two generic distinct points on the line \(ab\).

Choose the new points to avoid every other line determined by old points. Only finitely many points on \(ab\) are forbidden, so rational choices exist.

This creates exactly one new four-point line, introduces no other collinear triple, and leaves all old four-point lines unchanged. Add \(\{u,v\}\) to \(M\). Its line is distinct from all previous matching lines because the parent pair was ordinary and was not in \(M\).

There is always an available parent pair. At a stage with \(m=4+2r\) points, the four-point lines account for exactly \(6r\) nonordinary pairs. The only ordinary pairs belonging to \(M\) are its two initial pairs. Thus the number of eligible pairs is
\[
\binom m2-6r-2
=\frac{m^2-7m+20}{2}>0.
\]

Each extension adds two points and three switches, giving length
\[
3+3r=\frac32m-3.
\]
Finally, each four-point line identifies six point-pairs with one line, reducing the line count by five. This proves (5.1). ∎

## 5.2. Reading out two outputs per line

A core pair \(a,b\) can supply two new output positions \(x,y\) using three switches:
\[
(a,x),\quad(b,y),\quad(x,y). \tag{5.2}
\]
In the matrix certificate, the first two switches copy the core vectors while preserving them. The last switch chooses an arbitrary basis of their two-dimensional span.

For a matching pair \(\{a,b\}\in M\), no copying is needed: one final switch \((a,b)\) makes the two core positions themselves the two outputs from that line.

If one additional output is needed, a new position \(z\) can be assigned a generic vector on the line \(ab\) using
\[
(a,z),\quad(b,z). \tag{5.3}
\]
Choose the blocks to preserve the core rows, first copying \(a\) and then adding a multiple of \(b\) to the new row.

All copying operations are performed before the final matching switches on the core.

## 5.3. Why distinct lines suffice

**Lemma 5.2.** Suppose output vectors are grouped into distinct two-dimensional subspaces of \(\mathbb Q^3\), with at most two outputs assigned to each subspace. The vectors can be chosen so that every three outputs are linearly independent, with each two-output group forming a basis of its assigned subspace.

**Proof.** For any particular triple of outputs, its determinant is not the zero polynomial in the available coefficients.

If two outputs belong to a plane \(P\) and one to a distinct plane \(Q\), choose a basis of \(P\) and a vector of \(Q\setminus P\).

If the outputs belong to three distinct planes \(P,Q,R\), choose
\[
u\in P\setminus R,
\]
then choose \(v\in Q\) independent of \(u\). The plane \(\langle u,v\rangle\) is not \(R\), so a vector
\[
w\in R\setminus\langle u,v\rangle
\]
completes an independent triple.

There are finitely many triple determinants. Their product, together with the determinants requiring each two-output group to be a basis, is a nonzero polynomial. It has a nonzero value over the infinite field \(\mathbb Q\). ∎

By Lemma 4.1, the resulting word is unlabelled three-reachable. Prepending \(Q\) makes it labelled three-reachable.

## 5.4. Counting switches

Let
\[
\varepsilon=n\bmod2.
\]
Choose the least even \(m\ge4\) such that
\[
m^2-6m+20\ge n+\varepsilon. \tag{5.4}
\]
There are enough distinct lines to assign:

* the \(m/2\) matching pairs, accounting for all core outputs;
* \((n-m-\varepsilon)/2\) external two-output groups;
* one external singleton if \(\varepsilon=1\).

The total length, including the initial three-switch label permutation, is
\[
\begin{aligned}
&3+\left(\frac32m-3\right)
+\frac m2
+3\frac{n-m-\varepsilon}{2}
+2\varepsilon\\
&\hspace{3cm}
=\frac32n+\frac12m+\frac12\varepsilon. \tag{5.5}
\end{aligned}
\]

For \(n\ge4\), this choice has \(m\le n\) and
\[
m<\sqrt n+5.
\]
Indeed, for \(n+\varepsilon>12\), condition (5.4) is
\[
(m-3)^2\ge n+\varepsilon-11,
\]
and rounding up to an even integer adds less than two. The remaining cases use \(m=4\).

Thus
\[
L_3(n)\le\frac32n+\frac12\sqrt n+3.
\]
The case \(n=3\) is handled by \(Q\). Combining this with (3.1) proves Theorem A.

---

# 6. A \(5n/3+O(1)\) three-token star construction

Use core positions \(1,2,3\). Order the other
\[
N=n-3
\]
positions, and assign them types according to the repeating pattern
\[
X,Y,Z,X,Y,Z,\ldots.
\]

Write \(s_v=(1,v)\), and let
\[
Q=(s_2,s_3,s_2).
\]

Use the following word:

1. \(Q\);
2. \(s_2\), then all \(s_y\) for type-\(Y\) positions, then \(s_2\);
3. \(s_3\), then all \(s_z\) for type-\(Z\) positions, then \(s_3\);
4. one sweep through all \(N\) outside positions in their specified order;
5. \(Q\).

Selecting the wrappers and just one \(s_y\) in stage 2 realizes \((2,y)\). Thus stage 2 can preload one chosen \(Y\)-position from core position \(2\), or do nothing. Stage 3 does the same for a chosen \(Z\)-position and core position \(3\).

## 6.1. Routing up to three outside targets

Suppose there are \(r\in\{1,2,3\}\) outside targets, at sweep positions
\[
p_1<\cdots<p_r.
\]

We use one token initially at the hub and \(r-1\) preloaded tokens.

* For \(r=1\), no preload is needed.
* For \(r=2\), the interval \([p_1,p_2]\) contains a \(Y\)- or \(Z\)-position, because it contains at least two consecutive positions and there are no consecutive \(X\)'s.
* For \(r=3\), each of
  \[
  [p_1,p_2],\qquad[p_2,p_3]
  \]
  contains a \(Y\)- or \(Z\)-position. Their union contains at least three consecutive positions and therefore contains both types. Hall's condition for these two intervals gives one preload of type \(Y\) and one of type \(Z\), one in each interval.

Thus the preload positions can be chosen as
\[
u_i\in[p_i,p_{i+1}],\qquad 1\le i<r,
\]
using each preload type at most once.

To verify routing during the final sweep, let \(D(j)\) be the number of target positions at or before \(j\), and \(S(j)\) the number of preload positions at or before \(j\). The interlacing gives
\[
0\le D(j)-S(j)\le1.
\]
The hub occupancy after processing position \(j\) can therefore be
\[
1+S(j)-D(j)\in\{0,1\}.
\]

Scan the positions in order. If a leaf already has its required final occupancy, skip its switch; otherwise swap. The displayed condition ensures that the required swap always has the appropriate hub occupancy. At the end, the \(r\) outside targets are occupied and the hub is empty.

The initial \(Q\) assigns the prescribed token labels to these unlabelled routes. The unused tracked tokens stay at unused core positions. The final \(Q\) sends those tokens to their prescribed core targets.

If there are no outside targets, skip the intervening stages and route entirely inside the core.

## 6.2. Length

There are \(\lceil N/3\rceil\) positions of type \(X\). Hence the length is
\[
2N-\left\lceil\frac N3\right\rceil+10
=\left\lfloor\frac{5n}{3}\right\rfloor+5.
\]
Together with (3.2), this proves Theorem B.

---

# 7. A \(7n/4+O(\sqrt n)\) four-token construction

This construction uses an elementary four-output gadget.

## 7.1. A bounded-token core router

On \(m\) positions containing hub \(1\), repeat the star sweep
\[
(1,2),(1,3),\ldots,(1,m)
\]
twelve times.

This word can route at most four labelled tokens from any distinct starting positions to any prescribed distinct destinations.

Indeed, greedily fixing the tokens uses at most four arbitrary transpositions without disturbing tokens already fixed. Each arbitrary transposition is a product of at most three hub transpositions. Any word of at most twelve hub transpositions embeds in the twelve sweeps, one transposition per sweep.

Its length is \(12(m-1)\).

## 7.2. The four-output gadget

Take two vertex-disjoint core edges
\[
e=\{a,b\},\qquad f=\{c,d\}.
\]
Introduce four outside positions
\[
u_e,v_e,u_f,v_f.
\]
Use seven switches:
\[
\begin{gathered}
(a,u_e),(b,v_e),(c,u_f),(d,v_f),\\
(u_e,v_e),(u_f,v_f),(v_e,v_f).
\end{gathered} \tag{7.1}
\]

Call \(u_e,u_f\) the **narrow outputs**, and \(v_e,v_f\) the **rich outputs**.

Routing through this gadget can be described as follows.

* A token for \(u_e\) uses one endpoint of \(e\).
* A token for \(u_f\) uses one endpoint of \(f\).
* One selected rich output can use either \(e\) or \(f\).
* If both rich outputs are selected, assign one token to each of \(e,f\).

Each core edge receives at most two token demands. The first pair switches route its demands to its narrow output and/or its intermediate position. The final switch routes the rich demands to their prescribed rich outputs.

## 7.3. A matching observation

**Lemma 7.1.** In a triangle-free simple graph, a multiset of at most four edges, each having multiplicity at most two, fails Hall's endpoint condition only if two adjacent edges are both doubled.

**Proof.** A family of at most three demands always satisfies Hall: a single edge has multiplicity at most two, while two distinct edges have at least three endpoints.

A failing family of four demands must have at most three endpoints. A triangle-free graph on three vertices has at most two edges. Thus the family consists of two adjacent edges, each doubled. ∎

## 7.4. Combining gadgets

Let the core contain a complete bipartite graph
\[
H=K_{2k,2k}.
\]
Partition its edges into pairs of vertex-disjoint edges. Such a partition is obtained by partitioning each vertex class into pairs and, in every resulting \(K_{2,2}\), pairing opposite edges.

Use any desired number of these edge-pairs for gadgets (7.1). No core edge is used twice.

Consider at most four prescribed outside targets. Assign rich demands to core edges according to the gadget rules.

If the resulting edge demands fail Hall, Lemma 7.1 says that two adjacent core edges \(e,f\) are doubled. This uses all four demands: the two narrow outputs corresponding to \(e,f\), and one rich output from each of their gadgets.

The edges \(e,f\) cannot be paired with each other, because paired edges are vertex-disjoint. Reassign the rich demand using \(e\) to the other edge \(e'\) in its gadget. Since the only selected narrow outputs correspond to \(e,f\), the edge \(e'\) is not doubled. There is now at most one doubled edge, so Hall holds.

We may therefore match all outside-token demands to distinct core vertices.

Use the first core router to put each outside-bound token at its matched core vertex; put the remaining tracked tokens at unused core vertices. Execute only the attachment switches corresponding to matched demands. These selected attachments are pairwise disjoint. The internal gadget switches then deliver the outside tokens, with labels, to their targets.

Finally, use a second core router to finish the tokens whose targets lie in the core.

## 7.5. Choosing the core size

Let \(r=n\bmod4\), choose
\[
k=\left\lceil\sqrt{n/8}\right\rceil,
\qquad
m=4k+r.
\]
Then \(m\le n\), \(n-m\) is divisible by four, and
\[
m=O(\sqrt n).
\]

The graph \(K_{2k,2k}\) supplies \(2k^2\) edge-pairs, hence capacity for \(8k^2\ge n\) outside positions. Thus there are enough gadgets for all \(n-m\) outside positions.

The total length is
\[
\frac74(n-m)+24(m-1)
=\frac74n+O(\sqrt n).
\]
Combining this with (3.3) proves Theorem C.

---

# 8. What is and is not settled

The arguments above establish
\[
L_3(n)=\frac32n+\frac12\sqrt n+O(1),
\qquad
L_3^\star(n)=\frac53n+O(1),
\]
and
\[
L_4(n)=\frac74n+O(\sqrt n).
\]
They also give the star lower bound
\[
L_4^\star(n)\ge\frac95n-O(1).
\]

By monotonicity, the four-token lower bounds apply to every \(t\ge4\).

There remain substantial gaps:

* the exact bounded additive term for \(L_3(n)\);
* the exact additive term for \(L_3^\star(n)\);
* the lower-order term for \(L_4(n)\);
* a matching star upper bound for \(t=4\);
* the general dependence on \(t\).

No computational results or unverified literature claims are used. The uncertainty is about **novelty relative to the full source**, not about an omitted case in the stated partial results.