Attack the following open graph-theory problem.

Catalog id: grahams_conjecture_on_tree_reconstruction
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/grahams_conjecture_on_tree_reconstruction/
Original entry: http://www.openproblemgarden.org/op/grahams_conjecture_on_tree_reconstruction
Problem attributed to: Graham, Ronald L. (posted 2007-03-18)

=== Problem statement (OpenProblemGarden) ===
Title: Graham's conjecture on tree reconstruction
Problem for every graph $ G $ , we let $ L(G) $ denote the line graph of $ G $ . Given that $ G $ is a tree, can we determine it from the integer sequence $ |V(G)|, |V(L(G))|, |V(L(L(G)))|, \ldots $ ?

=== Discussion / context (OpenProblemGarden) ===
Graph reconstruction is a notoriously difficult subject. This conjecture is an unusual type of reconstruction problem where our class of graphs is very limited - just trees, but we are also given relatively little information - just a sequence of integers.

=== References listed by OpenProblemGarden ===
- [GR] C. Godsil and G. Royle, Algebraic graph theory. Graduate Texts in Mathematics, 207. Springer-Verlag, New York, 2001 (page 18).

=== Catalog page (statement + literature review) ===
Graham's conjecture on tree reconstruction — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Graham's conjecture remains open. Cooper, Kay, and Swifton (arXiv 2011, J. Combinatorics 2018) showed that the number of trees on $n$ vertices distinguishable by their Graham sequence is at least $e^{\Omega((\log n)^{3/2})}$, by constructing many caterpillars via the Prouhet-Tarry-Escott problem; this gives a strong lower bound but does not resolve the conjecture. Weatherspoon and Zeilberger (2025, experimental note) computationally verified the conjecture for all trees up to 11 vertices, with partial verification up to 16 vertices.

 Cited literature (3)

 
 
 
partial Graham's Tree Reconstruction Conjecture and a Waring-Type Problem on Partitions
 (2011)
 

 
 Joshua Cooper, Bill Kay, Anton Swifton · arXiv preprint (later J. Combinatorics 9(3), 2018) · arXiv:1109.0522

Provides a lower bound: the number of trees on $n$ vertices distinguishable by their iterated line-graph vertex-count sequence is at least $e^{\Omega((\log n)^{3/2})}$, via caterpillar constructions linked to the Prouhet-Tarry-Escott problem.
 

 
 
partial An Experimental Note on Graham's Tree Reconstruction Conjecture
 (2025)
 

 
 Kaylee Weatherspoon, Doron Zeilberger · Personal Journal of Shalosh B. Ekhad and Doron Zeilberger

Computationally verifies Graham's conjecture for all trees on up to 11 vertices, with partial verification for trees on 12-16 vertices.
 

 
 
partial Addressing Johnson graphs, complete multipartite graphs, odd cycles and other graphs
 (2018)
 

 
 Noga Alon, Sebastian M. Cioabă, Brandon D. Gilbert, Jack H. Koolen, Brendan D. McKay · arXiv preprint · arXiv:1808.04757

Resolves the question: the formula is confirmed for $n \in \{6, 7, 8, 9\}$ (corresponding odd cycles $C_{13}, C_{15}, C_{17}, C_{19}$) but shown to fail for $n = 11$.
 

 

 Reviewer notes. The arXiv version (1109.0522) was verified directly; the published Journal of Combinatorics 2018 PDF (Int. Press) returned only binary content via WebFetch but its existence and TOC reference is consistent with the arXiv v2 (Aug 2017) timing. Weatherspoon-Zeilberger note is verified via Zeilberger's personal journal listing and HTML version; it is not on arXiv. The original conjecture as stated remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Problem. for every graph $ G $ , we let $ L(G) $ denote the line graph of $ G $ . Given that $ G $ is a tree, can we determine it from the integer sequence $ |V(G)|, |V(L(G))|, |V(L(L(G)))|, \ldots $ ?

Keywords:
reconstruction · tree

Discussion

Graph reconstruction is a notoriously difficult subject. This conjecture is an unusual type of reconstruction problem where our class of graphs is very limited - just trees, but we are also given relatively little information - just a sequence of integers.

Bibliography

 [GR]
 C. Godsil and G. Royle, Algebraic graph theory. Graduate Texts in Mathematics, 207. Springer-Verlag, New York, 2001 (page 18).

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a sharp finite-prefix reconstruction theorem for spiders, together with a low-order criterion that upgrades it to reconstruction among all trees for a substantial subclass.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved by this argument, and no novelty claim is made for these special-case results."
}
```

# A sharp partial reconstruction theorem

Write
\[
\gamma_j(T)=|V(L^j(T))|,\qquad j\ge 0,
\]
where \(L^0(T)=T\). All trees below are finite and simple.

A **\(d\)-spider**, \(d\ge3\), is a tree with exactly one vertex of degree greater than two, that vertex having degree \(d\). Write
\[
S_d(a_1,\ldots,a_d)
\]
for the spider whose \(d\) arms have positive edge-lengths \(a_1,\ldots,a_d\). Its order is
\[
n=1+\sum_{i=1}^d a_i,
\]
and its isomorphism type is exactly the multiset of arm lengths.

## Main partial result

**Theorem.** Let \(T=S_d(a_1,\ldots,a_d)\) have \(n\) vertices, and put
\[
K(n,d)=\left\lfloor\frac{n-d+3}{2}\right\rfloor.
\]

1. The prefix
   \[
   \gamma_0(T),\gamma_1(T),\ldots,\gamma_{K(n,d)}(T)
   \]
   determines \(T\) **among all spiders**.

2. For fixed \(n,d\), this truncation index is optimal whenever \(n\ge d+3\): there are two nonisomorphic \(n\)-vertex \(d\)-spiders agreeing at every index below \(K(n,d)\).

3. The same prefix determines \(T\) **among all trees** in either of the following cases:
   - \(d=3\);
   - \(d\ge4\), and at most
     \[
     \left\lfloor\frac{d-4}{2}\right\rfloor
     \]
     arms have length one.

In particular, every tree with exactly three leaves, and every spider whose branching vertex has no leaf neighbour, is reconstructible from its Graham sequence.

For three-leaf trees, the optimal truncation index is \(\lfloor n/2\rfloor\). Consequently, any general finite-prefix reconstruction theorem must sometimes use at least that many line-graph iterations.

The proof is self-contained.

---

## 1. The first degree invariant

For a tree \(T\) of order \(n\ge2\),
\[
\gamma_2(T)=\sum_{v\in V(T)}\binom{d(v)}2.
\]
Since
\[
\sum_v(d(v)-1)=n-2,
\]
we obtain
\[
\boxed{\;
B(T):=\gamma_2(T)-n+2
=\sum_{v\in V(T)}\binom{d(v)-1}{2}.
\;} \tag{1}
\]

All summands are nonnegative. Thus:

- \(B(T)=0\) precisely when \(T\) is a path;
- \(B(T)=1\) precisely when \(T\) has one degree-three vertex and all other degrees at most two.

The latter trees are exactly the three-leaf trees.

For a \(d\)-spider,
\[
B(T)=\binom{d-1}{2}.
\]
Hence \(\gamma_0,\gamma_2\) determine \(d\), provided the tree is known to be a spider.

---

## 2. Pendant tails survive line-graph iteration in a controlled way

The central observation is that a long pendant path can be separated from an iterated-line-graph “core,” and its attachment degree remains constant.

### Lemma 1: capped-spider decomposition

Let
\[
T=S_d(a_1,\ldots,a_d),
\]
and, for \(t\ge1\), define
\[
H_t=L^t\!\left(S_d(\min(a_1,t),\ldots,\min(a_d,t))\right).
\]

Then \(L^t(T)\) is obtained from \(H_t\) by attaching pendant paths of lengths
\[
(a_i-t)_+
\]
at pairwise distinct marked vertices. For each \(i\) with \(a_i\ge t\), the corresponding marked vertex has degree \(d-1\) in \(H_t\).

#### Proof

At \(t=1\), the core is \(K_d\): its vertices correspond to the first edge of each arm. Each remaining arm becomes a pendant path of length \(a_i-1\), attached at a vertex of core degree \(d-1\).

For the induction step, consider a graph \(H\) with a pendant path attached at a marked vertex \(u\). Suppose \(u\) has degree \(b\) in \(H\). Include the first edge of each nonempty pendant path in an enlarged core \(H^+\), then take the line graph.

The remaining portion of each path becomes a pendant path shorter by one. Its new attachment vertex is the vertex of \(L(H^+)\) corresponding to that first edge. In \(H^+\), this edge has endpoint degrees \(b+1\) and \(1\), so its degree in \(L(H^+)\) is
\[
(b+1)+1-2=b.
\]
Thus the marked degree remains \(d-1\).

Applying the induction hypothesis also to the spider capped at length \(t+1\) shows that the new core is exactly \(H_{t+1}\). The marks are defined by this construction and are consistent under capping. ∎

Set
\[
h_t=|V(H_t)|,\qquad e_t=|E(H_t)|,\qquad
w_t=\sum_{v\in V(H_t)}\binom{d_{H_t}(v)}2,
\]
and
\[
R_t=\sum_i(a_i-t)_+,\qquad q_t=|\{i:a_i>t\}|.
\]

### Lemma 2: three consecutive counts

For every \(t\ge1\),
\[
\boxed{
\begin{aligned}
\gamma_t(T)&=h_t+R_t,\\
\gamma_{t+1}(T)&=e_t+R_t,\\
\gamma_{t+2}(T)&=w_t+R_t+(d-2)q_t.
\end{aligned}} \tag{2}
\]

#### Proof

A pendant path of length \(r\) adds \(r\) vertices and \(r\) edges, proving the first two identities.

For the third, use
\[
|V(L^2(G))|=\sum_{v\in V(G)}\binom{d_G(v)}2.
\]
A nonempty tail attached at a core vertex of degree \(d-1\) increases that vertex’s contribution by
\[
\binom d2-\binom{d-1}2=d-1.
\]
A tail of length \(r\) has \(r-1\) new degree-two vertices and one new leaf. Its total additional contribution is therefore
\[
(d-1)+(r-1)=r+d-2.
\]
Summing over the nonempty tails gives the last identity. ∎

---

## 3. The first differing arm length gives the first differing Graham entry

Let \(T,T'\) be \(d\)-spiders with the same order. Write
\[
m_s(T)=|\{i:a_i=s\}|
\]
for the multiplicity of arm length \(s\).

Suppose \(T\not\cong T'\), and let \(t\) be the least positive integer for which
\[
m_t(T)\ne m_t(T').
\]

Capping all arms at \(t\) produces isomorphic spiders: all arm multiplicities below \(t\) agree, and every remaining arm is replaced by one of length \(t\). Consequently, their cores \(H_t\) are isomorphic.

Moreover, \(R_t\) is the same for both trees, since their total arm lengths and their capped total arm lengths agree. Equation (2) gives agreement at indices \(t\) and \(t+1\). Applying the same reasoning at earlier caps gives agreement at all preceding indices.

At the next index,
\[
\begin{aligned}
\gamma_{t+2}(T)-\gamma_{t+2}(T')
&=(d-2)\bigl(q_t(T)-q_t(T')\bigr)\\
&=-(d-2)\bigl(m_t(T)-m_t(T')\bigr).
\end{aligned}
\]
Thus
\[
\boxed{
\begin{gathered}
\gamma_j(T)=\gamma_j(T')\quad(0\le j\le t+1),\\
\gamma_{t+2}(T)-\gamma_{t+2}(T')
=-(d-2)\bigl(m_t(T)-m_t(T')\bigr)\ne0.
\end{gathered}} \tag{3}
\]

This proves injectivity on spiders.

It also gives a reconstruction procedure. Once the multiplicities below \(t\) are known, \(H_t\) is known, and
\[
q_t=
\frac{\gamma_{t+2}-\gamma_t-w_t+h_t}{d-2}.
\]
Starting with \(q_0=d\), one obtains
\[
m_t=q_{t-1}-q_t.
\]

### Bounding the first differing length

We now prove the claimed finite-prefix bound.

Remove the common arms of lengths below \(t\). Suppose \(m\) arms remain on each side. They have equal total length, every remaining length is at least \(t\), and the two remaining multisets differ.

Necessarily \(m\ge2\). Also, their common total is at least \(mt+2\): totals \(mt\) and \(mt+1\) each permit only one multiset of \(m\) integers at least \(t\).

The removed \(d-m\) arms each have length at least one. Therefore
\[
n-1\ge mt+2+(d-m)
=d+m(t-1)+2
\ge d+2t.
\]
Hence
\[
t+2\le
\left\lfloor\frac{n-d+3}{2}\right\rfloor.
\]
Together with (3), this proves the upper bound.

### Sharpness

Assume \(n\ge d+3\), and put
\[
t=\left\lfloor\frac{n-d-1}{2}\right\rfloor,\qquad
\varepsilon=n-d-1-2t\in\{0,1\}.
\]
Consider
\[
\begin{aligned}
T&=S_d(\underbrace{1,\ldots,1}_{d-2},\,t,\,t+2+\varepsilon),\\
T'&=S_d(\underbrace{1,\ldots,1}_{d-2},\,t+1,\,t+1+\varepsilon).
\end{aligned}
\]
Both have \(n\) vertices. Their first differing arm multiplicity occurs at \(t\), and differs by one. By (3), they agree through index \(t+1\) and differ at index
\[
t+2=K(n,d).
\]
Indeed, the difference at that index is exactly \(d-2\) in absolute value.

This proves optimality.

---

## 4. When can the spider be recognized among arbitrary trees?

Equation (1) already settles this for \(d=3\): any tree sharing the sequence of a three-leaf tree has \(B=1\), so is itself a three-leaf tree.

For larger \(d\), we need an additional invariant. The following extremal bound provides one.

### A formula for \(\gamma_3\)

Let the branching vertices of a tree \(T\) be indexed by \(i\), and put
\[
x_i=d(v_i)-2\ge1,\qquad b_i=\binom{x_i+1}{2}.
\]
Then
\[
B=\sum_i b_i.
\]
Let \(F\) be the forest consisting of edges joining branching vertices directly, and let \(\lambda_i\) be the number of leaf neighbours of \(v_i\).

We have
\[
\boxed{
\gamma_3(T)
=n-3+4B+\sum_i b_i x_i
+\sum_{ij\in E(F)}x_ix_j
-\sum_i\lambda_i x_i.
} \tag{4}
\]

To verify this, use
\[
\gamma_3(T)=
\sum_{uv\in E(T)}
\binom{d(u)+d(v)-2}{2}.
\]
Set \(z_v=d(v)-2\), so that
\[
\binom{d(u)+d(v)-2}{2}
=1+\frac32(z_u+z_v)+\frac12(z_u+z_v)^2.
\]
The number of leaves is \(2+\sum_i x_i\). Substitution and expansion give (4); in the product term, branch–branch edges contribute \(x_ix_j\), branch–leaf edges contribute \(-x_i\), and edges incident with degree-two vertices contribute zero.

### Lemma 3: an extremal gap for multiple branching vertices

Suppose
\[
B(T)=\binom{D+1}{2},\qquad D\ge2,
\]
and \(T\) has at least two branching vertices. Define
\[
\eta_D=
\begin{cases}
1,&D=2,\\
2,&D=3,\\
D(D-1)/2,&D\ge4.
\end{cases}
\]
Then
\[
\boxed{
\gamma_3(T)
\le n-3+(D+4)B(T)-\eta_D.
} \tag{5}
\]

#### Proof

Write
\[
Q=\sum_i b_i x_i+\sum_{ij\in E(F)}x_ix_j,
\qquad M=\max_i x_i.
\]
Since there is more than one branching vertex,
\[
M\le D-1.
\]

Choose a branching vertex \(r\) with \(x_r=M\). Complete \(F\) to a tree on the branching vertices and root it at \(r\). Adding edges only increases the weighted edge sum, and every parent has weight at most \(M\). Thus
\[
\sum_{ij\in E(F)}x_ix_j
\le M\sum_{i\ne r}x_i,
\]
and consequently
\[
Q\le M\binom{M+1}{2}
+\sum_{i\ne r}\left(x_i\binom{x_i+1}{2}+Mx_i\right). \tag{6}
\]

First suppose \(D\ge4\).

**Case 1: \(M=D-1\).**  
The maximum \(M\) occurs only once, because
\[
2\binom{M+1}{2}>\binom{D+1}{2}.
\]
Hence all other \(x_i\) lie between \(1\) and \(M-1\). For this range,
\[
(M+1)\binom{x+1}{2}
-\left(x\binom{x+1}{2}+Mx\right)
=\frac{x}{2}(x-1)(M-1-x)\ge0.
\]
Using (6),
\[
Q\le DB-\binom D2=DB-\eta_D.
\]

**Case 2: \(M\le D-2\).**  
For \(1\le x\le M\),
\[
(M+2)\binom{x+1}{2}
-\left(x\binom{x+1}{2}+Mx\right)
=\frac{x}{2}\bigl((x-1)(M-x)+2\bigr)\ge0.
\]
Therefore
\[
Q\le (M+2)B-M(M+1).
\]
The right side increases with integer \(M\) in \(1\le M\le D-2\), since its successive difference is
\[
B-2(M+1)>0.
\]
It follows that
\[
Q\le DB-(D-2)(D-1)
\le DB-\frac{D(D-1)}2.
\]

For \(D=2,3\), all possible branching-weight multisets can be listed:
\[
\begin{array}{c|c|c}
D& (x_i)&\text{upper bound for }Q\\ \hline
2&(1,1,1)&5\\
3&(2,2)&16\\
3&(2,1,1,1)&15\\
3&(1,1,1,1,1,1)&11.
\end{array}
\]
These are exactly \(Q\le DB-\eta_D\) in the required cases.

Finally, the last term of (4) is nonpositive. Substituting the bound on \(Q\) into (4) proves (5). ∎

The constants \(\eta_D\) are sharp when the order is allowed to be sufficiently large. For \(D=2\) or \(D\ge4\), take a branching vertex of weight \(D-1\) adjacent to \(D\) branching vertices of weight \(1\), and fill the remaining degrees with pendant arms of length two. For \(D=3\), take two adjacent degree-four vertices, each with three pendant arms of length two. These constructions attain equality in (5).

### Applying the gap to a spider

Let \(T\) be a \(d\)-spider, put \(D=d-2\), and let \(c\) be its number of length-one arms. Formula (4) becomes
\[
\gamma_3(T)
=n-3+(D+4)\binom{D+1}{2}-Dc. \tag{7}
\]

Suppose another tree \(T'\) has the same \(\gamma_0,\gamma_2,\gamma_3\). It has the same \(n\) and the same
\[
B=\binom{D+1}{2}.
\]
If
\[
Dc<\eta_D, \tag{8}
\]
then (5) and (7) rule out the possibility that \(T'\) has multiple branching vertices. Thus \(T'\) must also be a \(d\)-spider.

For \(d\ge4\), the sufficient condition
\[
c\le\left\lfloor\frac{d-4}{2}\right\rfloor
\]
implies (8): for \(D=2,3\), it forces \(c=0\); for \(D\ge4\),
\[
c<\frac{D-1}{2}.
\]

The spider reconstruction theorem now applies. The stated prefix contains \(\gamma_3\) in these cases, since
\[
n\ge 2d-c+1.
\]
This completes the proof of the main theorem.

---

## 5. What remains unresolved

The argument does **not** reconstruct arbitrary trees with multiple branching vertices. Nor does it prove reconstruction among all trees for every spider: the recognition criterion above is only sufficient.

The distinction matters. For example, \(B=3\) can arise either from one degree-four vertex or from three degree-three vertices. Even the first four entries can coincide across these two structures:

- \(S_4(1,1,1,4)\);
- the eight-vertex tree whose three degree-three vertices form a path, with all remaining vertices leaves.

Both have
\[
(\gamma_0,\gamma_1,\gamma_2,\gamma_3)=(8,7,9,17).
\]
This is only a finite-prefix collision, not a counterexample to Graham’s conjecture.

The rigorous conclusions are therefore:

- injectivity on spiders;
- an exact optimal prefix length for that class;
- reconstruction among all trees for three-leaf trees and the stated additional spider subclass;
- a sharp extremal gap for \(\gamma_3\) under a triangular value of \(B\).

No equality of infinite Graham sequences for nonisomorphic trees is established, and the unrestricted conjecture is not settled here.
