```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A star-parity argument proves a linear bound when some vertex is incident with O(n^2) crossings, and also gives a bounded-alternation special case.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled; there is no improvement to the quoted general lower bound, and novelty of these restricted-case observations is not asserted."
}
```

## 1. Statement and partial result

Use the standard definition of a simple topological drawing: edges are Jordan arcs, adjacent edges meet only at their common endpoint, and independent edges meet at most once, at a proper crossing. We assume general position.

For a drawing \(D\) of \(K_n\), let
\[
\mu(D)=\max\{|M|:M\text{ consists of pairwise disjoint drawn edges}\}.
\]
Here disjointness excludes both crossings and shared endpoints. The question is whether \(\mu(D)\ge cn\) for an absolute \(c>0\), in every such drawing.

I do not establish this. The following parameterized bound is what I can prove.

Fix a vertex \(v\), and let \(h_v\) be the number of crossings involving an edge incident with \(v\). Since edges incident with \(v\) cannot cross each other, every such crossing has exactly one edge in the star at \(v\).

### Theorem 1
Let \(D\) be a simple drawing of \(K_n\), where \(n\ge2\), and put
\[
m=\left\lfloor\frac n2\right\rfloor,
\qquad
q_v=\left\lfloor\frac{h_v}{n-1}\right\rfloor.
\]
There is an ordinary matching of size \(m\) whose drawn edges have at most \(q_v\) mutual crossings. Consequently,
\[
\boxed{\displaystyle
\mu(D)\ge
\left\lceil\frac{m^2}{m+2q_v}\right\rceil.}
\tag{1}
\]

For \(n\ge3\), define
\[
\overline d_v=\frac{h_v}{\binom{n-1}{2}}.
\]
This is the average, over edges not incident with \(v\), of the number of spokes at \(v\) that they cross. If \(\overline d_v\le d\), then
\[
\boxed{\displaystyle
\mu(D)\ge
\left\lceil\frac{\lfloor n/2\rfloor}{1+2d}\right\rceil.}
\tag{2}
\]

In particular, the conjectured linear conclusion holds for every family of drawings having a vertex \(v\) with \(h_v=O(n^2)\). Also, \(h_v<n-1\) guarantees a disjoint matching of the maximum possible size \(\lfloor n/2\rfloor\).

The proof uses a parity constraint at a vertex and a rotational family of matchings.

## 2. The star-parity lemma

The edges incident with \(v\) have a cyclic order around \(v\). For four distinct vertices \(a,b,c,d\ne v\), say that the pairs \(\{a,b\}\) and \(\{c,d\}\) **alternate** if their spokes occur alternately in this cyclic order.

Write \(\chi(e,f)=1\) if edges \(e,f\) cross, and \(0\) otherwise.

### Lemma 2
If \(\{a,b\}\) and \(\{c,d\}\) do not alternate around \(v\), then
\[
\chi(ab,cd)\equiv
\chi(ab,vc)+\chi(ab,vd)
+\chi(cd,va)+\chi(cd,vb)
\pmod 2.
\tag{3}
\]

#### Proof

The three edges \(va,ab,bv\) form a Jordan curve \(C_{ab}\): each two are adjacent and therefore have no intersection other than their common endpoint. Similarly, \(vc,cd,dv\) form a Jordan curve \(C_{cd}\).

Take a sufficiently small disk about \(v\). Because the two pairs of spokes do not alternate, the portions of the two curves inside the disk can be replaced by disjoint connecting arcs. This removes their shared point \(v\), without introducing any crossing.

Two closed Jordan curves in general position cross an even number of times: traversing one, every entrance into the interior of the other is paired with an exit. Outside the small disk, the possible intersections of our two curves are precisely the five types appearing in (3), including \(ab\) crossing \(cd\). Their total is therefore even. ∎

A useful consequence is a charging bound.

For an edge \(e\) not incident with \(v\), let
\[
c_v(e)=|\{x\ne v:e\text{ crosses }vx\}|.
\]
For an ordinary matching \(M\), define
\[
W_v(M)=\sum_{\substack{e\in M\\v\notin e}}c_v(e).
\]

### Lemma 3
Suppose the pairs represented by the edges of \(M\) not incident with \(v\) are pairwise nonalternating around \(v\). Then
\[
\operatorname{cr}(M)\le W_v(M),
\tag{4}
\]
where \(\operatorname{cr}(M)\) counts crossings between edges of \(M\).

#### Proof

If two non-spoke edges \(ab,cd\in M\) cross, Lemma 2 shows that at least one of
\[
ab\text{ with }vc,\quad ab\text{ with }vd,\quad
cd\text{ with }va,\quad cd\text{ with }vb
\]
is a crossing.

These witnesses cannot be shared by distinct pairs of matching edges. Indeed, a crossing of \(ab\in M\) with a spoke \(vx\) can support only the pair consisting of \(ab\) and the unique matching edge containing \(x\), if such an edge exists.

If \(M\) contains a spoke \(vx\), its crossings with the other matching edges are counted directly in \(W_v(M)\), and those witnesses support no other matching pair. Summing proves (4). ∎

## 3. A rotational family of maximum matchings

Set \(N=n-1\), and list the vertices other than \(v\) as
\[
u_0,u_1,\ldots,u_{N-1}
\]
in the cyclic order of their spokes at \(v\). Indices below are taken modulo \(N\).

For each \(s\in\mathbb Z/N\mathbb Z\), form the matching
\[
P_s=\{u_i u_j:i\ne j,\ i+j=s\},
\]
with each unordered edge included once. These are the pairs of the involution
\[
i\longmapsto s-i.
\]

The pairs in \(P_s\) are nonalternating. To see this, place the indices on a regular \(N\)-gon in the same cyclic order. The involution is reflection in a diameter, and the chords joining reflected pairs are parallel and disjoint. For \(N\le2\), nonalternation is vacuous.

Extend \(P_s\) to a matching \(M_s\) as follows:

- If \(N\) is odd, the involution has one fixed index. Add the spoke to that vertex.
- If \(N\) is even and \(s\) is odd, there are no fixed indices. Add nothing.
- If \(N\) is even and \(s\) is even, there are two fixed indices. Add the spoke to either one of them.

In every case,
\[
|M_s|=\left\lfloor\frac n2\right\rfloor=m.
\]

Every edge \(u_i u_j\) not incident with \(v\) belongs to exactly one \(P_s\), namely the one with \(s=i+j\). Therefore
\[
\sum_{s\in\mathbb Z/N\mathbb Z}W_v(M_s)
=
\sum_{\substack{e\in E(K_n)\\v\notin e}}c_v(e)
=h_v.
\tag{5}
\]

Some \(s\) consequently satisfies
\[
W_v(M_s)\le
\left\lfloor\frac{h_v}{N}\right\rfloor=q_v.
\]
Lemma 3 gives
\[
\operatorname{cr}(M_s)\le q_v.
\]
This proves the first assertion of Theorem 1.

## 4. Extracting disjoint edges

Let \(H\) be the crossing graph of this matching: its \(m\) vertices are the edges of \(M_s\), and two vertices of \(H\) are adjacent when the corresponding drawn edges cross. Then
\[
e(H)\le q_v.
\]

For any graph \(H\) on \(m\) vertices,
\[
\alpha(H)\ge
\sum_{x\in V(H)}\frac1{d_H(x)+1}
\ge
\frac{m^2}{m+2e(H)}.
\tag{6}
\]
For completeness, the first inequality follows by randomly ordering the vertices and selecting those preceding all their neighbors. The selected set is independent, and its expected size is the displayed sum. The second inequality is Cauchy–Schwarz.

An independent set in \(H\) corresponds to pairwise disjoint drawn edges, since \(M_s\) already has distinct endpoints. Thus (6) proves (1).

For (2), observe that
\[
2q_v\le \frac{2h_v}{n-1}
=\overline d_v(n-2)
\le 2\overline d_v\,m.
\]
Substitution in (1) gives
\[
\mu(D)\ge
\left\lceil\frac{m}{1+2\overline d_v}\right\rceil
\ge
\left\lceil\frac{m}{1+2d}\right\rceil.
\]
This completes the proof of Theorem 1.

The low-star-crossing hypothesis is nonvacuous for arbitrarily large complete graphs. For example, put \(n-1\) generic points on a circle and invert their straight-line complete drawing through that circle, choosing the points so that no chord passes through the center. All leaf-to-leaf edges then lie outside the circle. Adding the center \(v\) and radial spokes gives a simple complete drawing with \(h_v=0\).

## 5. A refinement using crossing intervals

Counting all spoke crossings loses the parity cancellations in (3). One can instead bound the number of changes in the crossed-spoke set.

Keep the cyclic order \(u_0,\ldots,u_{N-1}\), and put
\[
m_0=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Consider the consecutive-pair matching
\[
M_0=\{u_0u_1,u_2u_3,\ldots,u_{2m_0-2}u_{2m_0-1}\}.
\]
For \(e\in M_0\), let
\[
S_e=\{i:e\text{ crosses }vu_i\},
\]
and let \(r(e)\) be the number of circular runs in \(S_e\), with \(r(e)=0\) when \(S_e\) is empty.

### Proposition 4
For \(n\ge3\),
\[
\boxed{\displaystyle
\mu(D)\ge
\left\lceil
\frac{m_0^2}{m_0+4\sum_{e\in M_0}r(e)}
\right\rceil.}
\tag{7}
\]
In particular, if \(r(e)\le r\) for every \(e\in M_0\), then
\[
\mu(D)\ge
\left\lceil\frac{\lfloor(n-1)/2\rfloor}{4r+1}\right\rceil.
\tag{8}
\]

#### Proof

For distinct \(e,f\in M_0\), define
\[
\varepsilon_{ef}
=
|S_e\cap\{\text{indices of the endpoints of }f\}|
\pmod 2.
\]
The matching pairs are nonalternating, so Lemma 2 gives
\[
\chi(e,f)\equiv \varepsilon_{ef}+\varepsilon_{fe}\pmod2.
\]
Consequently, a crossing pair has at least one of \(\varepsilon_{ef},\varepsilon_{fe}\) equal to \(1\).

For fixed \(e\), the condition \(\varepsilon_{ef}=1\) means that the two consecutive endpoints of \(f\) lie on different sides of the membership boundary of \(S_e\). There are at most \(2r(e)\) such transitions around the cyclic order. Hence
\[
|\{f\in M_0\setminus\{e\}:\varepsilon_{ef}=1\}|
\le 2r(e).
\]
The crossing graph of \(M_0\) therefore has at most
\[
2\sum_{e\in M_0}r(e)
\]
edges. Applying (6) proves (7), and (8) follows immediately. ∎

Thus a bounded number of crossing intervals also suffices for a linear disjoint-edge bound, even if individual candidate edges cross many spokes.

## 6. Why this does not settle the conjecture

The hypothesis \(h_v=O(n^2)\) cannot simply be guaranteed by choosing a suitable vertex.

In a generic straight-line drawing with all \(n\) vertices in convex position, every four vertices determine exactly one crossing. For every vertex \(v\),
\[
h_v=\binom{n-1}{3},
\qquad
\overline d_v=\frac{n-3}{3}.
\]
Thus every star has cubic crossing load, and the total-load estimate (1) gives only a constant-size guarantee. Nevertheless, this drawing has a disjoint matching of size \(\lfloor n/2\rfloor\).

This example exhibits the information lost in the charging argument: crossing both endpoint spokes of another candidate edge contributes twice to \(W_v(M)\), but cancels modulo two in (3). The interval refinement retains some of this information. However, the argument supplies no absolute bound on the relevant average number of runs for arbitrary simple drawings.

Accordingly, the general \(\Omega(n)\) conjecture remains unproved here. The rigorous progress is confined to the two stated restricted settings; it does not improve the general \(\Omega(n^{1/2})\) bound quoted in the question.