```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Weighted padding proves NP-hardness for P_(2k) at every c < 1/2 - 1/(2k), for k >= 2, and extends to connected trees and linear forests.",
  "would_publish": false,
  "caveats": "The general classification and most boundary cases remain unresolved; literature novelty has not been established."
}
```

## 1. Interpretation and results

I interpret the degree condition as the promise
\[
\delta(G)\ge c|V(G)|,
\]
and copies of \(H\) are not required to be induced.

The following gives additional hardness results, improving the supplied attempt for even paths of order at least six. The argument does **not** use its strict independent-neighbourhood condition. Instead, it assigns different weights to different padding components.

The only external complexity input is the unrestricted factor NP-completeness theorem supplied in the question.

### Path consequence

For every fixed \(m\ge3\), the \(P_m\)-factor problem is NP-hard under the minimum-degree promise whenever
\[
0<c<\frac{\lfloor(m-1)/2\rfloor}{m}.
\tag{1}
\]
Thus:
\[
\begin{array}{c|c}
H & \text{proved NP-hard range}\\ \hline
P_4 & 0<c<1/4\\
P_6 & 0<c<1/3\\
P_8 & 0<c<3/8\\
P_{10} & 0<c<2/5\\
P_{12} & 0<c<5/12
\end{array}
\]

More generally, if \(H\) is a linear forest with component orders
\(\ell_1,\dots,\ell_r\), at least one of which is at least three, then hardness holds whenever
\[
0<c<
\frac{\displaystyle\sum_{i=1}^r
       \left\lfloor\frac{\ell_i-1}{2}\right\rfloor}
     {\displaystyle\sum_{i=1}^r\ell_i}.
\tag{2}
\]

For example, this proves hardness for \(P_3\dot\cup P_5\) throughout \(0<c<3/8\).

### Connected-tree consequence

Let \(T\) be a fixed tree of order \(f\ge3\), let \(\Delta=\Delta(T)\), and set
\[
b(T)=\alpha\bigl(T[\{v:d_T(v)=\Delta\}]\bigr).
\]
Then \(T\)-factor is NP-hard whenever
\[
0<c<\frac{b(T)}{f}.
\tag{3}
\]

These consequences follow from a somewhat more general forest theorem, proved below. For rational \(c\), all stated restricted problems are NP-complete.

---

## 2. The forest theorem

For a forest \(H\), write \(h=|H|\) and \(\Delta=\Delta(H)\). For each component \(T\) of \(H\), define
\[
b_\Delta(T)
=
\alpha\bigl(T[\{v:d_T(v)=\Delta\}]\bigr),
\]
where the independence number of the empty graph is zero. Components are counted with multiplicity in
\[
\beta(H)=\sum_{T\text{ component of }H}b_\Delta(T).
\tag{4}
\]

**Theorem.**  
Let \(H\) be a fixed forest whose largest component order is \(f\ge3\). Suppose all components of order \(f\) are isomorphic to the same tree \(F\). Then \(H\)-factor is NP-hard under the promise
\[
\delta(G)\ge c|G|
\]
for every fixed
\[
0<c<\frac{\beta(H)}h.
\tag{5}
\]
If \(b_\Delta(F)=0\), hardness also holds at
\[
c=\frac{\beta(H)}h.
\tag{6}
\]

For rational \(c\), these restricted languages are NP-complete. For arbitrary fixed real \(c\), the assertion is NP-hardness by promise-preserving reductions.

The hypothesis concerning largest components is automatic for connected trees and for linear forests.

### Why these parameters arise

Choose an independent set \(S\) consisting of vertices of degree \(\Delta\) in a tree \(T\). Deleting \(S\) creates exactly
\[
1+(\Delta-1)|S|
\tag{7}
\]
components.

We will place \(S\) in a universal clique, and replace each component of \(T-S\) by a clique of the same order. Suitable weights make this configuration saturate a counting inequality. A copy meeting the source instance and also leaving it has strict inequality, so it cannot occur in a factor.

---

## 3. A weighted separation lemma

Fix integers \(f\ge3\) and \(\Delta\ge2\), and put
\[
D=f(\Delta-1)+1.
\tag{8}
\]

Consider a graph with vertex partition
\[
V(G)=X\dot\cup A\dot\cup B
\]
such that:

* \(G[A]\) is a disjoint union of cliques, each of order at most \(f\);
* there are no edges between \(A\) and \(X\).

No other edge assumptions are needed for this lemma.

Give every vertex in an \(A\)-clique of order \(s\) the weight
\[
w_s=\frac{f-s}{s}.
\tag{9}
\]
These weights are nonnegative; a clique of order \(f\) has weight zero.

For a copy \(C\) of a tree, let \(W_A(C)\) be the total weight of its vertices in \(A\), and let \(b_C=|V(C)\cap B|\).

**Lemma.**  
If \(C\) is a copy of a tree \(T\) with
\[
\ell=|T|\le f,\qquad \Delta(T)\le\Delta,
\]
then
\[
W_A(C)-D b_C\le f-\ell.
\tag{10}
\]
Moreover:

* if \(\ell<f\) and \(C\) meets \(X\), inequality (10) is strict;
* if \(\ell=f\) and \(C\) meets \(X\), equality in (10) is possible only when \(C\) lies entirely in \(X\).

### Proof

Use the tree edges of the chosen copy; extra host-graph edges are irrelevant. Put
\[
a=|V(C)\cap A|,\qquad b=|V(C)\cap B|.
\]

Deleting \(b\) vertices from a tree of maximum degree at most \(\Delta\) leaves at most
\[
1+(\Delta-1)b
\tag{11}
\]
components. For completeness, if the deleted vertex set is \(S\), the exact number is
\[
1+\sum_{v\in S}(d_T(v)-1)-e_T(S),
\]
which implies (11).

Every component of \(C-B\) lies entirely in \(A\) or entirely in \(X\), since there are no \(A\)-\(X\) edges. A component lying in \(A\) must lie in a single \(A\)-clique.

Suppose such a component has order \(u\) and lies in a clique of order \(s\). Since \(u\le s\), its weight is
\[
u\frac{f-s}{s}\le f-u.
\tag{12}
\]
If there are \(r_A\) components of \(C-B\) lying in \(A\), summing (12) gives
\[
W_A(C)\le f r_A-a.
\tag{13}
\]

First suppose \(C\) does not meet \(X\). Then \(a+b=\ell\), and (11)–(13) imply
\[
\begin{aligned}
W_A(C)-Db
&\le f\bigl(1+(\Delta-1)b\bigr)-a-Db\\
&=f-a-b\\
&=f-\ell.
\end{aligned}
\tag{14}
\]

Now suppose \(C\) meets \(X\). At least one component of \(C-B\) lies in \(X\), so
\[
r_A\le(\Delta-1)b.
\]
Consequently,
\[
W_A(C)-Db
\le f(\Delta-1)b-a-Db
=-a-b
\le0.
\tag{15}
\]
If \(C\) is not entirely in \(X\), then \(a+b>0\), making (15) strict. Comparing with \(f-\ell\ge0\) proves both equality assertions. \(\square\)

This lemma is the separation mechanism: a largest tree component can achieve equality inside \(X\), but not by straddling \(X\) and the padding. Smaller components cannot achieve equality while meeting \(X\) at all.

---

## 4. Saturating padding templates

Return to the forest \(H\) in the theorem. For each component \(T\), choose a maximum independent set
\[
S_T\subseteq\{v:d_T(v)=\Delta\}.
\]
Write
\[
\ell=|T|,\qquad b_T=|S_T|=b_\Delta(T).
\]

Construct a padding template for \(T\) as follows:

* put the vertices of \(S_T\) in \(B\);
* replace every component of \(T-S_T\) by a clique of the same order in \(A\).

Eventually \(B\) will be a clique complete to everything else. Thus this template contains a copy of \(T\).

Since \(S_T\) is independent and all its vertices have degree \(\Delta\),
\[
\operatorname{comp}(T-S_T)=1+(\Delta-1)b_T.
\tag{16}
\]
If the resulting \(A\)-cliques have orders \(s_1,\dots,s_p\), their total weight is
\[
\begin{aligned}
\sum_{i=1}^p(f-s_i)
&=f\bigl(1+(\Delta-1)b_T\bigr)-(\ell-b_T)\\
&=D b_T+f-\ell.
\end{aligned}
\tag{17}
\]
Thus each template attains equality in (10).

The same formulas apply when \(S_T=\varnothing\): the template is simply one clique of order \(\ell\).

---

## 5. The reduction

Let \(t\) be the number of components of \(H\) isomorphic to \(F\), and put
\[
b=b_\Delta(F),\qquad \beta=\beta(H).
\]

Reduce from unrestricted \(F\)-factor. By the theorem supplied in the question, this is NP-complete because \(F\) is connected and has at least three vertices.

We may restrict source instances to graphs \(X\) of order
\[
|X|=fk,\qquad k\ge1.
\]
Other orders are immediately decidable and can be replaced by fixed positive or negative instances of order \(f\).

Choose a fixed integer \(L\ge2\) such that
\[
\frac{\beta}{h}-\frac{b}{hL}\ge c.
\tag{18}
\]
Such an \(L\) exists for every \(c<\beta/h\). If \(b=0\), it also exists for \(c=\beta/h\).

Set
\[
Q=Lk.
\]

### Construction

Start with the component lists of \(Q\) formal copies of \(H\). There are \(tQ\) occurrences of \(F\), so we may discard \(k\) of them.

For every remaining tree component, construct its padding template from Section 4. Keep all the resulting \(A\)-cliques mutually disjoint.

Now:

1. insert the original graph \(X\);
2. make \(B\) a clique;
3. join \(B\) completely to \(A\cup X\);
4. add no \(A\)-\(X\) edges and no edges between distinct \(A\)-cliques.

The discarded components had altogether \(fk\) vertices, exactly the number inserted in \(X\). Hence
\[
n=|G|=hQ.
\tag{19}
\]
Also,
\[
|B|=\beta Q-bk,
\tag{20}
\]
and therefore
\[
\frac{\delta(G)}n
\ge \frac{|B|}{hQ}
=\frac{\beta}{h}-\frac{b}{hL}
\ge c.
\tag{21}
\]

The construction has \(O(|X|)\) vertices and polynomially many edges. In particular, every output satisfies both the degree promise and \(h\mid n\).

### Forward implication

Suppose \(X\) has an \(F\)-factor. It supplies \(k\) copies of \(F\), replacing the \(k\) discarded component occurrences.

Every padding template supplies its designated tree component. The combined multiset of component copies is exactly the multiset of components of \(Q\) copies of \(H\). Grouping them accordingly gives an \(H\)-factor.

Additional edges between these components cause no difficulty because copies are non-induced.

### Reverse implication

Let the component orders of one copy of \(H\), with multiplicity, be
\[
\ell_1,\dots,\ell_r,
\]
and put
\[
\Phi=\sum_{i=1}^r(f-\ell_i).
\tag{22}
\]

Before discarding the \(k\) copies of \(F\), equation (17) gives total padding weight
\[
D\beta Q+Q\Phi.
\]
Each discarded \(F\)-template has \(b\) vertices in \(B\) and \(A\)-weight \(Db\), because \(|F|=f\). Thus the constructed graph satisfies
\[
W(A)-D|B|=Q\Phi.
\tag{23}
\]

Suppose \(G\) has an \(H\)-factor. Fix its embeddings and consider all their designated tree-component copies. Apply (10) to each one. Since the factor covers every vertex,
\[
\begin{aligned}
W(A)-D|B|
&=\sum_C\bigl(W_A(C)-Db_C\bigr)\\
&\le\sum_C(f-|C|)\\
&=Q\Phi.
\end{aligned}
\tag{24}
\]
By (23), equality holds. Every individual inequality in (24) must therefore be an equality.

The separation lemma now shows that every component copy meeting \(X\):

* has order \(f\); and
* lies entirely in \(X\).

By the theorem’s hypothesis, every component of \(H\) of order \(f\) is isomorphic to \(F\). Hence all vertices of \(X\) are covered by copies of \(F\) lying entirely in \(X\). This is an \(F\)-factor.

We have proved
\[
X\text{ has an }F\text{-factor}
\quad\Longleftrightarrow\quad
G\text{ has an }H\text{-factor}.
\tag{25}
\]

This completes the NP-hardness proof. For rational \(c\), the degree condition and an \(H\)-factor certificate can both be checked in polynomial time, proving NP-completeness. \(\square\)

---

## 6. Consequences and comparisons

### 6.1 Connected trees

For \(H=T\) connected, the largest-component hypothesis is automatic, and
\[
\beta(H)=b(T).
\]
The theorem gives (3).

This is complementary to the previous attempt’s expansion condition, not uniformly stronger than it. It does, however, always give at least \(c<1/|T|\), because a tree’s maximum-degree vertex set is nonempty.

### 6.2 Paths

For \(P_m\), \(m\ge3\), the maximum-degree vertices are its \(m-2\) internal vertices. They induce \(P_{m-2}\), so
\[
b(P_m)
=\left\lceil\frac{m-2}{2}\right\rceil
=\left\lfloor\frac{m-1}{2}\right\rfloor.
\]
This proves (1).

In particular,
\[
\begin{aligned}
P_{2k+1}:&\qquad c<\frac{k}{2k+1},\\
P_{2k}:&\qquad c<\frac{k-1}{2k}
=\frac12-\frac1{2k}.
\end{aligned}
\tag{26}
\]

The even-path construction is particularly concrete. For each padding copy of \(P_{2k}\), use:

* one edge in \(A\);
* \(k-1\) isolated vertices in \(A\);
* \(k-1\) vertices in \(B\).

These support the path
\[
\text{edge},\,B,\,A,\,B,\,A,\ldots,B,A.
\]
The isolated \(A\)-vertices have weight \(2k-1\), the two endpoints of the \(A\)-edge each have weight \(k-1\), and each \(B\)-vertex has budget
\[
D=2k+1.
\]
The template’s weight exactly exhausts that budget. The separation lemma, rather than strict independent-set expansion, prevents leakage into the source graph.

### 6.3 Linear forests

If \(H\) is a linear forest with some component of order at least three, then \(\Delta(H)=2\). A path component of order \(\ell\) contributes
\[
\left\lfloor\frac{\ell-1}{2}\right\rfloor
\]
to \(\beta(H)\), including contribution zero for \(K_1\) and \(K_2\). All largest components are copies of the same path, proving (2).

There is a useful numerical comparison with the catalog’s critical-chromatic parameter. For a linear forest with at least one edge, the smallest possible colour-class size in a proper two-colouring is
\[
\sigma(H)=\sum_i\left\lfloor\frac{\ell_i}{2}\right\rfloor,
\]
and
\[
1-\frac1{\chi_{\mathrm{cr}}(H)}=\frac{\sigma(H)}h.
\]
If \(e\) denotes the number of even-order components, then
\[
\frac{\beta(H)}h
=
\frac{\sigma(H)-e}{h}.
\tag{27}
\]
Consequently, for linear forests all of whose components have odd order, the reduction reaches the critical-chromatic parameter **strictly from below**.

This is a numerical comparison, not a claim of literature novelty or a new proof of the catalog’s polynomial-time result.

### 6.4 An equality case for the proved bound

Take
\[
H=P_6\dot\cup K_{1,3}.
\]
Here \(h=10\), the unique largest component is \(F=P_6\), and \(\Delta(H)=3\). Therefore
\[
b_\Delta(F)=0,\qquad \beta(H)=1.
\]
The theorem proves NP-completeness even at
\[
\delta(G)\ge |G|/10.
\tag{28}
\]

Explicitly, from an input \(X\) of order \(6k\), take \(Q=2k\), let \(B\) be a universal clique of order \(Q\), and let \(A\) consist of
\[
(Q-k)K_6\ \dot\cup\ 3QK_1.
\]
Then \(|G|=10Q\) and \(\delta(G)=Q\). The general proof gives the exact factor equivalence.

This is equality in our particular bound, **not** equality at the catalog’s critical-chromatic threshold.

---

## 7. Scope and remaining gaps

The argument above is complete for its stated classes and ranges. It does not settle the original general classification.

In particular:

* For \(P_{2k}\), the hardness endpoint proved here is
  \[
  \frac12-\frac1{2k},
  \]
  whereas the critical-chromatic parameter is \(1/2\). The intervening densities are not classified by this proof.
* The forest theorem does not cover forests having nonisomorphic largest components. In that situation, saturation would only show that the source is covered by largest components, not by the particular source tree \(F\).
* Arbitrary cyclic \(H\) are not addressed by this tree-template argument.
* Except for the explicitly stated \(b_\Delta(F)=0\) case, equality at our hardness bounds is not established.
* No novelty claim is made relative to the literature.

For completeness, the easy unrestricted case remains easy under every degree promise: if
\[
H=aK_2\dot\cup bK_1
\]
and \(n=(2a+b)Q\), an \(H\)-factor exists exactly when \(G\) has a matching of size at least \(aQ\).

**Conclusion.** The original problem remains unresolved here. The additional proved progress is a weighted saturation method yielding the even-path bound \(c<1/2-1/(2k)\), the linear-forest bound (2), and the connected-tree bound (3), with a limited family of exact-boundary hardness results.