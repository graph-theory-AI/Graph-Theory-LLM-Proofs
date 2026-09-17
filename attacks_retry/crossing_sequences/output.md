```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Starting from the known three-term realizations, protected padding yields exactly the sequences whose positive drops can be made nonincreasing by at most one adjacent swap, in either surface category.",
  "would_publish": false,
  "caveats": "Uses the established three-term results quoted in the question; no novelty claim, and the general conjecture remains unresolved."
}
```

# 1. Result and scope

Write
\[
o_g(G)=\operatorname{cr}_{S_g}(G),\qquad
n_i(G)=\operatorname{cr}_{N_i}(G),
\]
where \(S_g\) is the closed orientable surface of genus \(g\), and \(N_i\) is the closed nonorientable surface of genus \(i\). Set \(N_0=S_0\).

For a proposed sequence
\[
a_0>a_1>\cdots>a_r=0,
\]
define its **positive drops**
\[
\delta_i=a_{i-1}-a_i\qquad(1\le i\le r).
\]

I establish the following partial result.

**Theorem.** Suppose that the list
\[
(\delta_1,\ldots,\delta_r)
\]
can be made nonincreasing by exchanging at most one pair of consecutive entries. Then the proposed sequence is realizable in both surface categories, generally by different graphs.

For \(r\ge2\), this is exactly the class obtainable from one three-term realization by repeatedly applying the protected \(K_5\)-padding operation described below.

Equivalently, the permitted drop lists have the form
\[
(u_1,\ldots,u_s,\ p,q,\ v_1,\ldots,v_t),
\tag{1}
\]
where
\[
u_1\ge\cdots\ge u_s\ge \max\{p,q\},
\qquad
\min\{p,q\}\ge v_1\ge\cdots\ge v_t>0,
\]
and \(p,q>0\). Empty prefixes and suffixes are allowed.

The external existence input is precisely the established three-term result supplied in the question: every \((A,B,0)\), with \(A>B>0\), is realizable in either category.

I checked the weighted-graph and topological arguments in the previous attempt. They support its padding lemma, including the essential orientable-complement term in the nonorientable formula. Beyond verifying that lemma, I give:

- the complete description above of its iterative closure;
- a necessary-and-sufficient algebraic test for undoing one padding;
- an obstruction showing why independent min-plus compositions cannot produce the most delayed-drop family.

These are partial results, not a resolution of the conjecture.

# 2. The protected padding lemma

## 2.1 Integer weights and simple graphs

For an integer-weighted graph, assign a crossing between edges \(e,f\) the cost \(w(e)w(f)\).

Such weights can be eliminated exactly, simultaneously on every surface. Replace an edge of weight \(w\) by \(w\) parallel edges.

One inequality follows by drawing the parallel edges in a narrow ribbon around the weighted edge. For the other, take any drawing of the parallel-edge graph and independently select one representative from each bundle. A crossing between distinct bundles of sizes \(w(e),w(f)\) survives with probability
\[
\frac1{w(e)w(f)}.
\]
Its expected weighted contribution is therefore \(1\). Crossings within a single bundle contribute nothing to the selected weighted drawing. Consequently, some selection has weighted crossing cost at most the original crossing count.

Thus the two crossing-number minima agree. Subdividing every parallel edge once produces a simple graph without changing its crossing numbers.

For \(d\ge1\), let \(P_d\) be obtained from a weighted \(K_5\) as follows:

- a distinguished edge \(e=uv\) has weight \(1\);
- the remaining nine edges have weight \(d\).

Its elementary crossing numbers are
\[
o_0(P_d)=n_0(P_d)=d,\qquad o_1(P_d)=n_1(P_d)=0.
\tag{2}
\]
Indeed, every crossing in a spherical drawing of the weighted \(K_5\) involves a weight-\(d\) edge. A one-crossing drawing with \(e\) participating gives equality. Replacing a small disk around that crossing by a punctured handle, or by a Möbius band, resolves the crossing.

## 2.2 The separation lemma

Put \(M=K_5-e\).

**Lemma.** Suppose \(G\sqcup K_5\) is drawn on a closed surface \(S\), and no edge of \(M\) participates in a crossing. Then the drawing of \(G\), with no additional crossings, can be transferred:

- from \(S_g\) to an orientable surface of genus at most \(g-1\);
- from \(N_i\) to a closed surface of Euler genus at most \(i-1\), possibly orientable.

**Proof.** Take a sufficiently small connected regular neighbourhood \(R\) of the embedded \(M\), disjoint from the drawing of \(G\). Let \(b\) be its number of boundary components, and let \(C_1,\ldots,C_k\) be the components of the closure of its complement.

For a connected surface with boundary, let \(\epsilon(X)\) denote the Euler genus after capping its boundary components. Euler characteristic gives
\[
\epsilon(S)
=
\epsilon(R)+\sum_{j=1}^{k}\epsilon(C_j)+2(b-k).
\tag{3}
\]
Every complementary component has boundary, so \(b\ge k\).

If \(\epsilon(R)>0\), at least one unit of Euler genus lies outside the capped complementary components. On an orientable surface, at least two units do.

Now suppose \(\epsilon(R)=0\). The two ends of \(e\), viewed in their incident boundary corners of \(R\), lie on different boundary components. Otherwise, after capping \(R\), one could add \(e\) through a single cap disk, obtaining a planar embedding of \(K_5\).

The interior of \(e\) avoids \(M\), so \(R\) may be chosen such that the remainder of \(e\) lies in one complementary component. That component is incident with at least two boundary components of \(R\). Hence \(b-k\ge1\), accounting for at least two units of Euler genus in (3).

The entire drawing of \(G\) lies in the complementary components. Cap them and take connected sums through disks disjoint from the drawing. Its crossing count is unchanged. Equation (3) gives the claimed bounds. ∎

The distinguished edge \(e\) is allowed to cross \(G\). Thus this lemma is stronger than merely separating two disjoint embedded subgraphs.

## 2.3 Exact formulas

For every graph \(G\) and \(d\ge1\),
\[
\boxed{
o_g(G\sqcup P_d)
=
\min\{o_g(G)+d,\ o_{g-1}(G)\}
\qquad(g\ge1).
}
\tag{4}
\]

In the nonorientable category,
\[
\boxed{
n_i(G\sqcup P_d)
=
\min\left\{
n_i(G)+d,\ n_{i-1}(G),\
o_{\lfloor(i-1)/2\rfloor}(G)
\right\}
\qquad(i\ge1).
}
\tag{5}
\]

On the sphere,
\[
o_0(G\sqcup P_d)=n_0(G\sqcup P_d)=o_0(G)+d.
\tag{6}
\]

**Upper bounds.** For the first terms, put a planar drawing of \(P_d\) in a disk disjoint from \(G\). For the second terms, allocate one handle or one crosscap to an embedding of \(P_d\).

For the third term of (5), put \(h=\lfloor(i-1)/2\rfloor\). A drawing of \(G\) on \(S_h\), together with a projective-plane embedding of \(P_d\), fits on
\[
S_h\#N_1\cong N_{2h+1}.
\]
An unused crosscap can be added if necessary.

**Lower bounds.** Work in the equivalent weighted model. Let \(C_G\) count crossings internal to \(G\).

If an edge of \(M\) participates in a crossing, that crossing costs at least \(d\), and is not included in \(C_G\). Therefore
\[
C\ge C_G+d.
\]
This gives the first alternative in (4) or (5).

Otherwise, the separation lemma applies. On \(S_g\), it gives
\[
C\ge C_G\ge o_{g-1}(G).
\]
On \(N_i\), the transferred drawing is either nonorientable of genus at most \(i-1\), or orientable of genus at most \(\lfloor(i-1)/2\rfloor\). This gives one of the other two alternatives in (5).

Equation (6) follows by restricting a spherical drawing to its two parts, and by drawing the parts in disjoint disks. ∎

No additivity assertion for arbitrary disjoint unions on surfaces is being used.

One can also join \(G\) to \(P_d\) by a bridge: deleting the bridge gives the same lower bounds, and every upper-bound construction accommodates it. Thus connected seeds can remain connected throughout.

# 3. When the nonorientable formula becomes scalar

The extra orientable term in (5) cannot simply be omitted for an arbitrary graph.

Consider the property
\[
n_{2h}(G)\le o_h(G)\qquad(h\ge0).
\tag{7}
\]
Every nonorientable three-term seed satisfies it: equality holds at \(h=0\), while \(n_{2h}(G)=0\) for \(h\ge1\).

Property (7) is preserved by padding. For \(h\ge1\), formulas (4)–(5) give
\[
\begin{aligned}
n_{2h}(G\sqcup P_d)
&\le \min\{n_{2h}(G)+d,\ o_{h-1}(G)\}\\
&\le \min\{o_h(G)+d,\ o_{h-1}(G)\}\\
&=o_h(G\sqcup P_d).
\end{aligned}
\]
The assertion at \(h=0\) follows from (6).

Under (7), the third term in (5) is redundant. For odd \(i\), this follows directly from (7). For even \(i=2h\), use the universal inequality
\[
n_{2h-1}(G)\le o_{h-1}(G),
\]
obtained by adding a crosscap to \(S_{h-1}\).

Consequently, all nonorientable constructions starting from the quoted three-term seeds obey the same numerical rule as the orientable ones.

For a sequence \(a\), extended by zeros after its first zero, define
\[
(T_da)_0=a_0+d,\qquad
(T_da)_i=\min\{a_i+d,a_{i-1}\}\quad(i\ge1).
\tag{8}
\]
Padding realizes \(T_d\) in the orientable category for every graph, and in the nonorientable constructions just described.

# 4. Realizing the stated family

There are two useful endpoint rules.

If
\[
d\ge \max_i\delta_i,
\]
then \(T_d\) prepends the drop \(d\):
\[
(\delta_1,\ldots,\delta_r)
\longmapsto
(d,\delta_1,\ldots,\delta_r).
\tag{9}
\]

If
\[
d\le \min_i\delta_i,
\]
then \(T_d\) appends the drop \(d\):
\[
(\delta_1,\ldots,\delta_r)
\longmapsto
(\delta_1,\ldots,\delta_r,d).
\tag{10}
\]
Both statements follow immediately from (8).

Now take a target drop list of the form (1). Start with a known three-term realization
\[
(p+q,q,0),
\]
whose drops are \((p,q)\).

Append \(v_1,\ldots,v_t\), in that order, using (10). Then prepend \(u_s,\ldots,u_1\), in that order, using (9). The stated inequalities ensure that every application is valid.

This proves the theorem for \(r\ge2\). The cases \(r=0,1\) are supplied by a planar graph and \(P_{a_0}\), respectively.

For example, the drop list
\[
(12,9,2,7,2,1)
\]
becomes nonincreasing after swapping its middle \(2,7\). Thus
\[
(33,21,12,10,3,1,0)
\]
is realizable in both categories. One may start with \((9,7,0)\), append drops \(2,1\), and prepend drops \(9,12\).

## Four-term consequence

For
\[
(a,b,c,0),
\]
the drops are
\[
x=a-b,\qquad y=b-c,\qquad z=c.
\]
A three-entry drop list belongs to the stated class exactly when \(x\ge z\). Therefore
\[
a>b>c>0,\qquad a\ge b+c
\]
is sufficient in both categories.

This recovers and verifies the four-term region in the previous attempt.

# 5. Why this is the entire padding closure

The operators \(T_d\) commute. With negative-index entries interpreted as \(+\infty\),
\[
(T_dT_ea)_i
=
\min\{a_i+d+e,\ a_{i-1}+d,\ a_{i-1}+e,\ a_{i-2}\},
\]
which is symmetric in \(d,e\).

If a three-term seed has drops \(p\ge q\), its numerical sequence is the same as that obtained from two one-handle pads of weights \(p,q\). Any further pads simply produce a nonincreasing list of drops: reorder the commuting operators and apply (10).

It remains to consider a seed with \(p<q\). Directly from (8), padding this seed gives the following three drops:
\[
\begin{cases}
(p,q,d),&d\le p,\\[2mm]
(d,p+q-d,d),&p\le d\le q,\\[2mm]
(d,p,q),&d\ge q.
\end{cases}
\tag{11}
\]

Suppose an existing drop list has a nonincreasing prefix, then \(p<q\), then a nonincreasing suffix, with every prefix entry at least \(q\) and every suffix entry at most \(p\). By commutativity, a new padding operator may first be applied to the two-drop seed.

- If \(d\ge q\), insert \(d\) into the nonincreasing prefix.
- If \(d\le p\), insert \(d\) into the nonincreasing suffix.
- If \(p<d<q\), the local list is
  \[
  (d,m,d),\qquad m=p+q-d.
  \]
  Both \(d\) and \(m\) lie strictly between \(p\) and \(q\).
  - If \(m\le d\), regard the list as a prefix entry \(d\), followed by the pair \((m,d)\).
  - If \(m\ge d\), regard it as the pair \((d,m)\), followed by a suffix entry \(d\).

The inequalities separating the old prefix and suffix from the new pair remain valid. If \(m=d\), the local list is nonincreasing.

Thus the class in the theorem is invariant under every padding operation. Since every member was constructed in Section 4, it is exactly the closure of the three-term seeds under these operations.

This is a characterization of the **construction**, not a characterization of all crossing sequences.

# 6. An exact test for undoing one padding

There is also a useful inversion criterion that does not assume the parent sequence is itself in the preceding class.

**Algebraic inversion lemma.** Let
\[
a_0>\cdots>a_r=0,\qquad r\ge2,
\]
and let \(\delta_i=a_{i-1}-a_i\). For a positive integer \(d\), there exists a strictly decreasing integer sequence
\[
b_0>\cdots>b_{r-1}=0
\]
with \(a=T_db\) if and only if
\[
\delta_r\le d\le\delta_1
\tag{12}
\]
and
\[
\text{there is no }i\in\{1,\ldots,r-1\}
\text{ with }\delta_{i+1}<d<\delta_i.
\tag{13}
\]

When these conditions hold, a canonical parent is
\[
b_i=\max\{a_i-d,a_{i+1}\}
\qquad(0\le i\le r-1).
\tag{14}
\]

**Proof.** Any parent must satisfy
\[
b_0=a_0-d,\qquad b_{r-1}=0,
\]
and
\[
b_i\ge a_i-d,\qquad b_i\ge a_{i+1}.
\]
The endpoint conditions imply (12), and every candidate parent is coordinatewise at least the list in (14).

Under (12), that list has the correct endpoints and is strictly decreasing. For \(1\le i\le r-1\), writing \(x_+=\max\{x,0\}\), one computes
\[
\min\{b_i+d,b_{i-1}\}-a_i
=
\min\bigl\{(d-\delta_{i+1})_+,(\delta_i-d)_+\bigr\}.
\tag{15}
\]
Thus it gives the required sequence exactly when (13) holds.

If it fails, every other candidate parent is coordinatewise larger, and \(T_d\) is monotone. Hence no other candidate can work. ∎

The lemma concerns numerical sequences; it does not assert that an arbitrary canonical parent is realizable by a graph.

For instance, consider
\[
(11,8,7,2,0),
\]
with drops
\[
(3,1,5,2).
\]
Condition (12) leaves only \(d=2,3\). The descent \(3\to1\) excludes \(d=2\), and the descent \(5\to2\) excludes \(d=3\). Therefore this sequence is not the output of a single scalar padding \(T_d\), regardless of the parent sequence. This is not a nonrealizability result for graphs.

# 7. A stronger limitation of independent-block constructions

The following obstruction applies more generally to numerical constructions that allocate genus independently among blocks.

Suppose
\[
a_i=\min_{j+k=i}(u_j+v_k),
\tag{16}
\]
where \(u\) and \(v\) are strictly decreasing sequences first reaching zero at positive indices \(p\) and \(q\). Then \(a\) first reaches zero at \(r=p+q\), and
\[
a_p\le v_0,\qquad a_q\le u_0.
\]
Consequently,
\[
\boxed{a_p+a_q\le a_0.}
\tag{17}
\]

Now consider, for \(r\ge3\) and \(N\ge2\),
\[
a_i=N+r-1-i\quad(0\le i<r),\qquad a_r=0.
\tag{18}
\]
Its drops are
\[
(1,\ldots,1,N).
\]
For every split \(r=p+q\) with \(p,q>0\),
\[
a_p+a_q
=
2N+r-2
>
N+r-1
=
a_0.
\]
Thus (18) admits no nontrivial factorization of the form (16), even if completely general shorter sequences are allowed as the factors.

This does **not** assert that arbitrary graph unions satisfy (16). It shows that a successful construction for (18) must do more than independently allocate genus to smaller blocks.

For this family,
\[
\frac{a_0-a_{r-1}}{a_{r-1}-a_r}
=
\frac{r-1}{N}\longrightarrow0,
\]
so it is exactly of the delayed-large-improvement type emphasized in the problem.

# 8. Remaining gap

The full conjecture is not proved or disproved here. In particular, this argument does not realize
\[
(N+2,N+1,N,0)\qquad(N\ge2),
\]
nor its longer analogues (18).

The verified partial result is a realization theorem for the one-adjacent-swap class, together with an exact description of what protected padding can generate. The inversion and min-plus obstructions demonstrate that the missing cases require a genuinely different interaction, rather than a more elaborate iteration of the same padding operation.

I have not verified whether these closure and inversion observations have appeared previously, so I make no novelty claim.