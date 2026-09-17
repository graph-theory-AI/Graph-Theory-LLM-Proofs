```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every tree with exactly one branching vertex of degree three, four, or five is reconstructible among all trees, and I determine the optimal finite-prefix bound for these classes.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of these special-case results has not been checked."
}
```

# A partial reconstruction theorem

All trees are finite, simple, and considered up to isomorphism. Write
\[
\gamma_j(T)=|V(L^j(T))|.
\]
A **\(d\)-spider** is a tree with exactly one vertex of degree greater than two, that vertex having degree \(d\ge3\). Denote it by
\[
S_d(a_1,\ldots,a_d),
\]
where the positive integers \(a_i\) are the edge-lengths of its arms.

I independently rederive the tail-capping argument in the supplied attempt. The additional result proved here is that **every four- or five-arm spider can be recognized among all trees from its first five Graham entries**, including the cases not covered by that attempt’s recognition criterion.

## Main theorem

For \(d\in\{3,4,5\}\) and \(n\ge d+1\), define
\[
\kappa(n,d)=
\begin{cases}
4,&(n,d)\in\{(8,4),(9,5)\},\\[2mm]
\displaystyle\left\lfloor\frac{n-d+3}{2}\right\rfloor,
&\text{otherwise}.
\end{cases}
\]

**Theorem.** Every \(n\)-vertex \(d\)-spider, \(d\in\{3,4,5\}\), is determined among all trees by
\[
\gamma_0,\gamma_1,\ldots,\gamma_{\kappa(n,d)}.
\]
Moreover, \(\kappa(n,d)\) is optimal uniformly over the \(n\)-vertex \(d\)-spiders: no smaller truncation index works for every member of that class.

Thus the conjecture holds for every tree having exactly one branching vertex of degree at most five. This does **not** include, for example, all four-leaf trees: a four-leaf tree can instead have two degree-three vertices.

---

## 1. Reconstruction within the class of spiders

For a tree of order \(n\ge2\),
\[
\gamma_1=n-1,\qquad
\gamma_2=\sum_v\binom{d(v)}2.
\]
Consequently,
\[
\boxed{
B(T):=\gamma_2-n+2
=\sum_v\binom{d(v)-1}{2}.
} \tag{1}
\]

In particular:

- \(B=0\) characterizes paths;
- \(B=1\) characterizes three-arm spiders;
- for a \(d\)-spider,
  \[
  B=\binom{d-1}{2}.
  \]

Thus \(\gamma_0,\gamma_2\) determine \(d\) when the tree is known to be a spider.

### 1.1. Tail capping

Let \(T=S_d(a_1,\ldots,a_d)\). For \(t\ge1\), put
\[
H_t=L^t\!\left(S_d(\min(a_1,t),\ldots,\min(a_d,t))\right).
\]

**Lemma 1.** The graph \(L^t(T)\) is obtained from \(H_t\) by attaching pendant paths of lengths
\[
(a_i-t)_+
\]
at distinct marked vertices. Every marked vertex corresponding to an arm with \(a_i\ge t\) has degree \(d-1\) in \(H_t\).

**Proof.**
For \(t=1\), the core is \(K_d\), with the remaining portions of the arms attached at its vertices.

For the induction step, include the first edge of each nonempty pendant path in the core before taking the line graph. If such an edge starts at a core vertex of degree \(b\), its endpoint degrees in the enlarged core are \(b+1\) and \(1\). The corresponding new marked vertex therefore has degree
\[
(b+1)+1-2=b.
\]
The remaining pendant path becomes shorter by one. Applying this construction also to the spider capped at \(t+1\) identifies the new core with \(H_{t+1}\). Starting with \(b=d-1\) proves the claim. ∎

Set
\[
h_t=|V(H_t)|,\qquad e_t=|E(H_t)|,\qquad
w_t=\sum_{v\in V(H_t)}\binom{d_{H_t}(v)}2,
\]
and
\[
R_t=\sum_i(a_i-t)_+,\qquad q_t=|\{i:a_i>t\}|.
\]
Then
\[
\boxed{
\begin{aligned}
\gamma_t(T)&=h_t+R_t,\\
\gamma_{t+1}(T)&=e_t+R_t,\\
\gamma_{t+2}(T)&=w_t+R_t+(d-2)q_t.
\end{aligned}
} \tag{2}
\]

Indeed, a pendant path of length \(r\) adds \(r\) vertices and edges. If \(r>0\), its contribution to the degree-binomial sum is
\[
\left[\binom d2-\binom{d-1}2\right]+(r-1)
=r+d-2,
\]
giving the third identity.

### 1.2. Exact first difference

Suppose two \(d\)-spiders \(T,T'\) have the same order. Let \(m_s(T)\) be the number of arms of length \(s\), and suppose \(t\) is the least index with
\[
m_t(T)\ne m_t(T').
\]
Their spiders capped at \(t\) are isomorphic, and their values of \(R_t\) agree. Equation (2), also applied at earlier caps, gives
\[
\boxed{
\begin{aligned}
\gamma_j(T)&=\gamma_j(T') &&(0\le j\le t+1),\\
\gamma_{t+2}(T)-\gamma_{t+2}(T')
&=-(d-2)\bigl(m_t(T)-m_t(T')\bigr)\ne0.
\end{aligned}
} \tag{3}
\]

This proves injectivity of the Graham sequence on spiders.

It also proves the sharp bound
\[
K(n,d)=\left\lfloor\frac{n-d+3}{2}\right\rfloor
\tag{4}
\]
for reconstruction among spiders. To see this, remove the common arms of lengths below \(t\). If \(m\) arms remain on each side, then \(m\ge2\), and their common total length is at least \(mt+2\): excess zero or one above \(mt\) permits only one multiset. Hence
\[
n-1\ge(d-m)+mt+2\ge d+2t,
\]
so \(t+2\le K(n,d)\).

For sharpness when \(n\ge d+3\), put
\[
t=\left\lfloor\frac{n-d-1}{2}\right\rfloor,\qquad
\varepsilon=n-d-1-2t\in\{0,1\}.
\]
The spiders
\[
\begin{aligned}
S_d(1^{d-2},t,t+2+\varepsilon),\\
S_d(1^{d-2},t+1,t+1+\varepsilon)
\end{aligned}
\tag{5}
\]
first differ at Graham index \(t+2=K(n,d)\), by (3).

The remaining task is to recognize the relevant spiders among arbitrary trees.

---

## 2. Two low-order formulas

The following identities will be used only for trees having at least one branching vertex.

Index the branching vertices by \(i\), and define
\[
x_i=d(v_i)-2,\qquad b_i=\binom{x_i+1}{2},\qquad B=\sum_i b_i.
\]
Let

- \(E_1\) be the pairs of branching vertices at distance one;
- \(E_2\) be the pairs of branching vertices at distance two;
- \(c_i\) be the number of leaf neighbours of \(v_i\);
- \(p_i\) be the number of pendant paths of length two from \(v_i\) to a leaf;
- \(s_i=\sum_{j:ij\in E_1}x_j\).

Define
\[
\begin{aligned}
f(x)&=\binom{x+1}{2}(2x^2+8x+11),\\
A(x)&=\frac{x(5x+9)}2,\\
W(x,y)&=\frac{xy(5x+5y+14)}2.
\end{aligned}
\]

**Lemma 2.**
\[
\boxed{
\gamma_3
=n-3+4B+\sum_i b_ix_i
+\sum_{ij\in E_1}x_ix_j-\sum_i x_ic_i.
} \tag{6}
\]
Also,
\[
\boxed{
\begin{aligned}
\gamma_4={}&n-4+\sum_i f(x_i)
+\sum_{ij\in E_1}W(x_i,x_j)
+\sum_{ij\in E_2}x_ix_j\\
&-\sum_i c_i\bigl(A(x_i)+s_i\bigr)
+\sum_i\binom{c_i}{2}
-\sum_i x_ip_i.
\end{aligned}
} \tag{7}
\]

**Proof.**
For (6), use
\[
\gamma_3=\sum_{uv\in E(T)}
\binom{d(u)+d(v)-2}{2}.
\]
Put \(z_v=d(v)-2\) and expand
\[
\binom{2+z_u+z_v}{2}
=1+\frac32(z_u+z_v)+\frac12(z_u^2+z_v^2)+z_uz_v.
\]
The number of leaves is \(2+\sum_i x_i\). The product term contributes \(x_ix_j\) on branch–branch edges and \(-x_i\) on branch–leaf edges; all other such products vanish. Collecting terms gives (6).

For (7), edges of \(L(T)\) correspond to unordered two-edge paths \(u-v-w\), so
\[
\gamma_4=
\sum_v\ \sum_{\{u,w\}\subseteq N(v)}
\binom{d(u)+2d(v)+d(w)-6}{2}. \tag{8}
\]
For a degree-two centre, expansion of (8) gives a baseline contribution \(1\); a branching neighbour of weight \(x\) adds \(x(x+3)/2\), and a leaf neighbour adds \(-1\). Cross-products contribute \(x_ix_j\) for branching endpoints and \(-x_i\) for a branch–leaf path of length two.

For a branching centre of weight \(x\), the baseline is
\[
\binom{x+2}{2}\binom{2x+2}{2}.
\]
Expanding its neighbour terms, and combining with the degree-two contributions, gives:

- \(W(x_i,x_j)\) for each direct branch–branch edge;
- \(x_ix_j\) for each branch pair at distance two;
- \(-A(x_i)c_i-c_is_i+\binom{c_i}{2}-x_ip_i\) for the short pendant-path terms.

Finally, using the leaf count above, the constant contribution at a branching vertex simplifies to
\[
\binom{x+2}{2}\binom{2x+2}{2}
+\frac{x(x+3)(x+2)}2-1-2x
=f(x).
\]
This proves (7). ∎

Useful values are
\[
f(1)=21,\quad f(2)=105,\quad f(3)=318,
\]
\[
A(1)=7,\quad A(2)=19,\quad A(3)=36,
\]
and
\[
W(1,1)=12,\quad W(2,1)=29,\quad W(2,2)=68.
\]

For a spider, let \(c\) and \(p\) be its numbers of arms of lengths one and two. Equations (6)–(7) give
\[
\begin{array}{c|c|c}
d&\gamma_3-n&\gamma_4-n\\ \hline
4&15-2c&101-19c+\binom c2-2p\\
5&39-3c&314-36c+\binom c2-3p.
\end{array}
\tag{9}
\]

---

## 3. Recognizing every four-arm spider

Suppose a tree \(U\) shares \(\gamma_0,\gamma_2,\gamma_3,\gamma_4\) with a four-arm spider \(T\). By (1), \(B(U)=3\). Unless \(U\) is itself a four-arm spider, its branching weights must be
\[
(1,1,1).
\]
Such a tree has five leaves and at least eight vertices.

Suppress the paths between its three branching vertices. Their reduced branching tree is a path. Label its vertices in path order. Their numbers of pendant arms are \(2,1,2\).

Let \(e\in\{0,1,2\}\) count direct branch–branch edges, let
\[
\ell=c_1+c_2+c_3,
\]
and let \(q\) count branch pairs at distance two. Formula (6), compared with (9), gives
\[
\ell=e+2c-3. \tag{10}
\]
Writing \(r_i\) for the number of direct branching neighbours of vertex \(i\), formula (7) gives
\[
\gamma_4(U)-n
=59+12e+q-7\ell
+\sum_i\binom{c_i}{2}
-\sum_i r_ic_i-\sum_i p_i. \tag{11}
\]

Here
\[
0\le(c_1,c_2,c_3)\le(2,1,2)
\]
coordinatewise. Up to reflection, the vectors \(r\) are
\[
(0,0,0),\quad(1,1,0),\quad(1,2,1)
\]
for \(e=0,1,2\), respectively. Corresponding upper bounds for \(q\) are \(2,1,1\).

Maximizing (11) over these explicitly specified integer triples, subject to (10), and dropping the nonpositive term \(-\sum p_i\), gives
\[
\begin{array}{c|ccc}
c&e=0&e=1&e=2\\ \hline
1&\text{impossible}&72&76\\
2&54&59&61\\
3&41&44&45.
\end{array}
\tag{12}
\]
For example, when \(e=2,c=2\), one has \(\ell=3\), and
\[
\sum_i\binom{c_i}{2}-\sum_i r_ic_i\le-2.
\]
Thus (11) is at most \(59+24+1-21-2=61\).

These bounds contradict the spider’s value in every case:

- **\(c=0\):** equation (10) is impossible.
- **\(c=1\):** equation (10) gives \(\ell\le1\). At least four of \(U\)’s five pendant arms therefore contain degree-two vertices, so \(n\ge12\). Hence the spider cannot have all three other arms of length two, and \(p\le2\). Thus
  \[
  \gamma_4(T)-n=82-2p\ge78>76.
  \]
- **\(c=2\):** since \(n\ge8\), the spider’s two other arms cannot both have length two; that would give \(n=7\). Thus
  \[
  \gamma_4(T)-n=64-2p\ge62>61.
  \]
- **\(c=3\):** its remaining arm has length at least four, so
  \[
  \gamma_4(T)-n=47>45.
  \]
- **\(c=4\):** the spider has only five vertices, whereas \(U\) has at least eight.

Therefore every four-arm spider is recognized among all trees by its first five entries.

---

## 4. Recognizing every five-arm spider

Now suppose \(T\) is a five-arm spider and \(U\) shares its first five entries. Here \(B=6\). If \(U\) is not a five-arm spider, its branching-weight multiset is exactly one of
\[
(2,2),\qquad (2,1,1,1),\qquad (1,1,1,1,1,1).
\tag{13}
\]
Their minimum orders are \(8,11,14\), respectively. We exclude all three.

### 4.1. Two branching weights \(2,2\)

Let \(e\in\{0,1\}\) indicate whether the branching vertices are adjacent, and let \(\ell\) be their total number of leaf neighbours. Each has three pendant arms.

Formula (6) gives
\[
\gamma_3(U)-n=33+4e-2\ell.
\]
Equality with the spider’s value implies
\[
2\ell=4e-6+3c. \tag{14}
\]
Thus \(c\) is even. Apart from the impossible cases \(c=0\) and \(c=5\), only \(c=2,4\) remain.

Let \(h\) indicate whether the branching vertices are at distance two, and let \(p_U=\sum p_i\). Formula (7) gives
\[
\gamma_4(U)-n
=206+68e+4h-(19+2e)\ell
+\binom{c_1}{2}+\binom{c_2}{2}-2p_U.
\tag{15}
\]
Using \(c_i\le3\), \(h\le1-e\), and (14), we obtain
\[
\begin{array}{c|cc|c}
c&e=0&e=1&\text{lower bound for }\gamma_4(T)-n\\ \hline
2&210&233&234\\
4&156&173&176.
\end{array}
\tag{16}
\]
For the last column, use (9). When \(c=2\), \(p\le3\). When \(c=4\), \(p=1\) would make the spider have seven vertices, below the minimum order eight of \(U\); hence \(p=0\).

Thus this branching-weight multiset is impossible.

### 4.2. Branching weights \(2,1,1,1\)

Call the weight-two branching vertex \(v_0\). Write
\[
a=c_0,\qquad P=2a+c_1+c_2+c_3.
\]
Every branching vertex has a path to another branching vertex, so
\[
a\le3,\qquad c_i\le2\quad(i=1,2,3). \tag{17}
\]

Let \(r\) count direct edges from \(v_0\) to the other branching vertices, and \(s\) count direct edges between the weight-one vertices. Put
\[
E=2r+s.
\]
The direct branching graph is a forest on four vertices, so \(E\le6\).

Equation (6) becomes
\[
\gamma_3(U)-n=30+E-P,
\]
and equality with the spider implies
\[
P=E-9+3c. \tag{18}
\]

Define the nonnegative leaf penalty
\[
\Pi=\sum_i c_i\bigl(A(x_i)+s_i\bigr)-\sum_i\binom{c_i}{2}.
\]
The total product \(x_ix_j\) over all six branch pairs is \(9\). Therefore the distance-two contribution \(Q_2\) satisfies
\[
Q_2\le9-E.
\]
By (7),
\[
\gamma_4(U)-n
\le164+29r+12s+Q_2-\Pi. \tag{19}
\]

The bounds (17) imply
\[
7c_i-\binom{c_i}{2}\ge\frac{13}{2}c_i
\quad(i=1,2,3),
\]
and
\[
19a-\binom a2\ge18a.
\]
Consequently,
\[
\boxed{\Pi\ge\frac{13}{2}P+5a.} \tag{20}
\]
Combining (18)–(20), and using \(29r+12s\le(29/2)E\), yields
\[
\boxed{
\gamma_4(U)-n
\le\frac{463}{2}+7E-\frac{39}{2}c-5a.
} \tag{21}
\]

For the few large values of \(E\), we need the following additional information. Put
\[
C_0=164+29r+12s+Q_2.
\]
Then
\[
\begin{array}{c|c|c|l}
E&(r,s)&C_0&\text{additional information}\\ \hline
4&(2,0)\text{ or }(1,2)&\le225&\\
5&(2,1)&237&a\le2,\ \sum_{i=1}^3c_i\le5,\ s_0=2\\
6&(3,0)&254&a\le1,\ s_0=3,\ s_i=2\ (i>0).
\end{array}
\tag{22}
\]

Here is a verification of the structural entries:

- For \(E=4,(r,s)=(2,0)\), the direct branching graph is a two-edge star plus an isolated vertex. The existing distance-two pair contributes \(1\), and the one remaining edge of the reduced branching tree can contribute at most \(2\) if subdivided once. Thus \(Q_2\le3\), giving \(C_0\le225\).
- For \(E=4,(r,s)=(1,2)\), the direct branching graph is a tree, with the weight-two vertex a leaf. Its distance-two contribution is at most \(5\), giving \(C_0\le222\).
- For \(E=5\), the direct branching graph is a path with \(v_0\) internal; \(Q_2=3\).
- For \(E=6\), it is the star centred at \(v_0\); again \(Q_2=3\).

In the \(E=6\) case,
\[
\Pi=22a+\sum_{i=1}^3\left(9c_i-\binom{c_i}{2}\right).
\]
Checking \(a=0,1\), with \(c_i\le2\), gives
\[
\begin{array}{c|cccc}
P&0&3&6&9\\ \hline
\text{lower bound for }\Pi&0&26&51&\text{infeasible}.
\end{array}
\tag{23}
\]

These inequalities give the following complete bounds:
\[
\begin{array}{c|c|c}
c&\text{upper bound for }\gamma_4(U)-n&
\text{lower bound for }\gamma_4(T)-n\\ \hline
1&254&266\\
2&228&234\\
3&204&206\\
4&174&176.
\end{array}
\tag{24}
\]

For completeness, the case coverage behind the middle column is:

- \(c=1\): (18) forces \(E=6,P=0\).
- \(c=2\): for \(E\le4\), (21) gives at most \(220\); \(E=5\) gives at most \(237-13=224\); \(E=6\) gives at most \(254-26=228\).
- \(c=3\): for \(E\le4\), (21) gives at most \(201\); \(E=5\) gives at most \(204\); \(E=6\) gives at most \(203\).
- \(c=4\): for \(E\le3\), (21) gives at most \(174\). For \(E=4\), \(P=7\) forces \(a\ge1\), so (20) and (22) give at most \(174\). For \(E=5\), \(P=8\) forces \(a=2\) and \(\sum_{i>0}c_i=4\). The weight-two vertex contributes \(41\) to \(\Pi\), and the others contribute at least \(26\), giving at most \(237-67=170\). The case \(E=6\) is infeasible.

The last column follows from (9) and \(n\ge11\). In particular, for \(c=3\), having both remaining arms of length two would give \(n=8\); hence \(p\le1\). For \(c=4\), \(p=0\).

Finally, \(c=0\) is impossible in (18), since \(E\le6\), and \(c=5\) gives a six-vertex spider. Thus this branching-weight multiset is also excluded.

### 4.3. Six branching weights equal to one

Let \(e\le5\) count direct branch–branch edges, and let \(\ell=\sum c_i\). Formula (6) gives
\[
\gamma_3(U)-n=27+e-\ell,
\]
so equality requires
\[
\ell=e-12+3c. \tag{25}
\]
The cases \(c=0,1,2\) are impossible because \(\ell<0\); \(c=5\) is impossible by order.

Each \(c_i\le2\), and the distance-two contribution is at most \(15-e\). Hence (7) gives
\[
\begin{aligned}
\gamma_4(U)-n
&\le122+12e+(15-e)-\frac{13}{2}\ell\\
&=215+\frac92e-\frac{39}{2}c.
\end{aligned}
\tag{26}
\]
For \(c=3\), this is at most \(179\); for \(c=4\), it is at most \(159\). Since \(n\ge14\), the corresponding spider values are at least \(206\) and \(176\), respectively.

This excludes the last alternative in (13), completing recognition of all five-arm spiders.

---

## 5. The optimal truncation indices

For three-arm spiders, \(B=1\) already recognizes the class among all trees, so the bound \(K(n,3)\) from Section 1 applies directly.

For four-arm spiders, the recognition argument uses index \(4\). Whenever \(n\ge9\), one has \(K(n,4)\ge4\), so \(K(n,4)\) suffices. For \(n\le7\), the alternative branching-weight multiset \((1,1,1)\) requires too many vertices, so \(\gamma_0,\gamma_2\) already recognize the class. Only \(n=8\) needs separate treatment.

For five-arm spiders, the same reasoning applies for \(n\ge10\), and orders \(6,7\) admit no alternative in (13). At order \(8\), the only possible nonspider alternative is the unsubdivided double star with two degree-four vertices. Its \(\gamma_3\) equals \(33\). The two eight-vertex five-arm spiders have arm multisets
\[
(1,1,1,1,3),\qquad(1,1,1,2,2),
\]
and have \(\gamma_3=35,38\), respectively. Thus index \(K(8,5)=3\) suffices. Only \(n=9\) needs index \(4\).

### The two exceptional orders really require index four

For \((n,d)=(8,4)\), take
\[
T=S_4(1,1,1,4).
\]
Let \(U\) have three degree-three vertices forming a path, with all other vertices leaves. Their prefixes are
\[
\begin{aligned}
(\gamma_0,\ldots,\gamma_4)(T)&=(8,7,9,17,55),\\
(\gamma_0,\ldots,\gamma_4)(U)&=(8,7,9,17,53).
\end{aligned}
\]
Thus index three does not suffice.

For \((n,d)=(9,5)\), take
\[
T=S_5(1,1,1,1,4).
\]
Let \(U\) be formed from two adjacent degree-four vertices, each initially with three leaf neighbours, by subdividing one pendant edge once. Then
\[
\begin{aligned}
(\gamma_0,\ldots,\gamma_4)(T)&=(9,8,13,36,185),\\
(\gamma_0,\ldots,\gamma_4)(U)&=(9,8,13,36,180).
\end{aligned}
\]
Again index three does not suffice.

At every other order \(n\ge d+3\), the spider pairs (5) establish the required lower bound \(K(n,d)\). At orders \(n=d+1,d+2\), the stated bound is two, and index one cannot suffice because every \(n\)-vertex tree has initial entries \(n,n-1\).

This proves both the reconstruction theorem and optimality of \(\kappa(n,d)\).

---

## 6. What remains unresolved

The argument proves:

1. A sharp finite-prefix reconstruction theorem **within the class of all spiders**.
2. Recognition among arbitrary trees of **every three-, four-, and five-arm spider**.
3. Exact optimal truncation indices for these three classes, including two exceptional orders.

It does not reconstruct arbitrary trees with multiple branching vertices. Nor does this writeup recognize all spiders of degree at least six among arbitrary trees.

The displayed nonisomorphic pairs are only finite-prefix collisions—their fourth iterates have different orders—and are not counterexamples to Graham’s conjecture. No equality of infinite Graham sequences for nonisomorphic trees is established here.